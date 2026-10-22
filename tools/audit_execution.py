#!/usr/bin/env python3
"""Run every discovered regression test against the exact audited snapshot.

Every audit runs every test; nothing is selected or skipped by path. The
report records per-test timings for the audit summary.
"""
from __future__ import annotations

import argparse
import json
import sys
import time
import unittest
from pathlib import Path

from audit_timing import AuditTimer, report_path, write_report
from character_index_core import DomainError, FULL_COMMIT_RE, run_git


def flatten(suite):
    for test in suite:
        if isinstance(test, unittest.TestSuite):
            yield from flatten(test)
        else:
            yield test


class TimedResult(unittest.TextTestResult):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.timings = []
        self._started = {}

    def startTest(self, test):
        self._started[test.id()] = time.perf_counter()
        super().startTest(test)

    def stopTest(self, test):
        self.timings.append({"id": test.id(), "seconds": time.perf_counter() - self._started.pop(test.id())})
        super().stopTest(test)


def execute_suite(suite, stream=None):
    return unittest.TextTestRunner(stream=stream or sys.stderr, verbosity=1, resultclass=TimedResult).run(suite)


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--snapshot", choices=("index", "commit"), default="index")
    parser.add_argument("--commit")
    parser.add_argument("--report-json", type=Path)
    args = parser.parse_args(argv)
    root = args.repo.resolve()
    timer = AuditTimer()
    report = {"schema": "repository-test-execution/v2", "outcome": "failure", "snapshot": args.snapshot, "commit": args.commit}
    output = None
    try:
        if args.report_json:
            output = report_path(root, args.report_json)
        # Tests import the checked-out tools, so the checkout must be exactly the audited bytes.
        if args.snapshot == "commit":
            if not args.commit or not FULL_COMMIT_RE.fullmatch(args.commit):
                raise DomainError("commit execution requires an exact commit SHA")
            if run_git(root, "rev-parse", "HEAD").decode().strip() != args.commit:
                raise DomainError("test checkout does not match the audited commit")
            run_git(root, "diff", "--exit-code", "HEAD", "--")
        else:
            if args.commit:
                raise DomainError("--commit is valid only with --snapshot commit")
            run_git(root, "diff", "--exit-code", "--")
        loader = unittest.TestLoader()
        suite = timer.call("discovery", loader.discover, str(root / "tools/tests"), pattern="test_*.py")
        if loader.errors:
            raise DomainError("test discovery failed: " + "\n".join(loader.errors))
        ids = [test.id() for test in flatten(suite)]
        if not ids or len(ids) != len(set(ids)):
            raise DomainError("empty or duplicated test discovery")
        report["discovered_tests"] = len(ids)
        print(f"EXECUTION: full ({len(ids)} tests)", flush=True)
        result = timer.call("regressions", execute_suite, suite)
        report.update(tests_run=result.testsRun, failures=len(result.failures), errors=len(result.errors), skipped=len(result.skipped), expected_failures=len(result.expectedFailures), unexpected_successes=len(result.unexpectedSuccesses), tests=result.timings)
        if result.testsRun != len(ids):
            raise DomainError("test execution did not cover every discovered test")
        success = result.wasSuccessful()
        report["outcome"] = "success" if success else "failure"
        return 0 if success else 1
    except (DomainError, OSError, ValueError) as exc:
        report["error"] = str(exc)
        print(f"FAIL: {exc}", file=sys.stderr)
        return 1
    finally:
        report.update(timer.report())
        if output:
            write_report(root, output, report)
        summary = {key: report[key] for key in ("outcome", "seconds")}
        summary["tests_run"] = report.get("tests_run", 0)
        summary["slowest_tests"] = sorted(report.get("tests", []), key=lambda row: row["seconds"], reverse=True)[:20]
        summary["git_in_process"] = report.get("git_in_process", {})
        print("TEST_EXECUTION_SUMMARY: " + json.dumps(summary, sort_keys=True), flush=True)


if __name__ == "__main__":
    raise SystemExit(main())
