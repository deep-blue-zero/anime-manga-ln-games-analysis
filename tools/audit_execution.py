#!/usr/bin/env python3
"""Time full regression execution and preview conservative content selection.

This rollout deliberately cannot skip tests. Shadow plans are advisory, do not
authenticate a baseline, and cannot certify a commit or satisfy an audit gate.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
import time
import unicodedata
import unittest
from pathlib import Path, PurePosixPath

from audit_timing import AuditTimer, report_path, write_report
from character_index_core import DomainError, FULL_COMMIT_RE, GitSnapshot, decode_json, run_git, validate_repository_path

POLICY = "governance/repository-controls/test-execution-policy.json"
CATALOG = "tools/tests/test-catalog.json"
GROUPS = {"live_corpus", "regression", "synthetic_git", "dormant_reconstruction"}


def load_policy(snapshot: GitSnapshot) -> dict:
    entry = snapshot.get(POLICY)
    if entry is None or not entry.qualifies_as_evidence:
        raise DomainError("test execution policy is absent or unsafe")
    policy = decode_json(entry.data, POLICY)
    expected = {"schema", "rollout_stage", "selection_enabled", "catalog", "runtime", "content_extensions", "content_global_paths", "mandatory_groups", "full_groups", "enablement_requires"}
    if not isinstance(policy, dict) or set(policy) != expected:
        raise DomainError("invalid test execution policy fields")
    if (policy["schema"] != "anime-manga-ln-games-analysis/test-execution/v1"
            or policy["selection_enabled"] is not False
            or policy["rollout_stage"] != "FULL_COVERAGE_SHADOW_PLANNING"
            or policy["catalog"] != CATALOG):
        raise DomainError("this rollout requires full coverage with selection disabled")
    if policy["runtime"] != {"python_major_minor": [3, 12], "unicode": "15.0.0"}:
        raise DomainError("test runtime contract differs from the reviewed envelope")
    for field in ("content_extensions", "content_global_paths", "enablement_requires", "full_groups"):
        values = policy[field]
        if not isinstance(values, list) or not values or any(not isinstance(v, str) or not v for v in values) or len(values) != len(set(values)):
            raise DomainError(f"invalid test execution policy {field}")
    if policy["mandatory_groups"] != ["live_corpus", "smoke"] or set(policy["full_groups"]) != GROUPS:
        raise DomainError("test execution groups differ from the reviewed contract")
    return policy


def flatten(suite):
    for test in suite:
        if isinstance(test, unittest.TestSuite):
            yield from flatten(test)
        else:
            yield test


def validate_catalog(snapshot: GitSnapshot, tests: list) -> tuple[dict, list[str]]:
    entry = snapshot.get(CATALOG)
    if entry is None or not entry.qualifies_as_evidence:
        raise DomainError("test catalog is absent or unsafe")
    catalog = decode_json(entry.data, CATALOG)
    if not isinstance(catalog, dict) or set(catalog) != {"schema", "tests"} or catalog["schema"] != "repository-test-catalog/v1" or not isinstance(catalog["tests"], dict):
        raise DomainError("invalid test catalog")
    rows = catalog["tests"]
    ids = [test.id() for test in tests]
    if not ids or len(ids) != len(set(ids)):
        raise DomainError("empty or duplicated test discovery")
    if set(rows) - set(ids):
        raise DomainError("test catalog contains stale test IDs")
    for test_id, row in rows.items():
        if not isinstance(row, dict) or set(row) != {"group", "smoke", "inputs", "purpose"}:
            raise DomainError(f"invalid catalog entry: {test_id}")
        if not isinstance(row["group"], str) or row["group"] not in GROUPS or type(row["smoke"]) is not bool:
            raise DomainError(f"invalid test group: {test_id}")
        if not isinstance(row["purpose"], str) or not row["purpose"] or not isinstance(row["inputs"], list) or not row["inputs"] or any(not isinstance(v, str) or not v for v in row["inputs"]):
            raise DomainError(f"missing test purpose or dependencies: {test_id}")
    if not any(row["group"] == "live_corpus" for row in rows.values()) or not any(row["smoke"] for row in rows.values()):
        raise DomainError("test catalog is missing a mandatory group")
    return rows, sorted(set(ids) - set(rows))


def changed_paths(root: Path, snapshot: str, target: str | None, base: str | None) -> tuple[list[str], list[str]]:
    if not base or not FULL_COMMIT_RE.fullmatch(base) or set(base) == {"0"}:
        return [], ["baseline_unavailable"]
    try:
        if run_git(root, "cat-file", "-t", base).strip() != b"commit":
            return [], ["baseline_is_not_commit"]
        head = target or run_git(root, "rev-parse", "HEAD").decode().strip()
        run_git(root, "merge-base", "--is-ancestor", base, head)
        args = ["diff", "--name-only", "--no-renames", "-z"]
        args += ["--cached", base] if snapshot == "index" else [base, head]
        raw = run_git(root, *args, "--")
        paths = sorted(item.decode("utf-8", "strict") for item in raw.split(b"\0") if item)
        for path in paths:
            validate_repository_path(path)
        return paths, []
    except (DomainError, OSError, UnicodeError):
        return [], ["baseline_or_diff_unavailable"]


def plan_content(snapshot: GitSnapshot, policy: dict, catalog: dict, ids: list[str], paths: list[str], reasons: list[str]) -> dict:
    reasons = list(reasons)
    if list(sys.version_info[:2]) != policy["runtime"]["python_major_minor"] or unicodedata.unidata_version != policy["runtime"]["unicode"]:
        reasons.append("runtime_outside_envelope")
    roots = set()
    try:
        for namespace in ("series", "studies"):
            path = f"{namespace}/registry.json"
            entry = snapshot.get(path)
            if entry is None or not entry.qualifies_as_evidence:
                raise DomainError("missing registry")
            document = decode_json(entry.data, path)
            for row in document[namespace]:
                value = row["repository_path"]
                if not isinstance(value, str) or not re.fullmatch(rf"{namespace}/[a-z0-9][a-z0-9-]*/", value):
                    raise DomainError("invalid registered root")
                roots.add(value)
    except (DomainError, KeyError, TypeError):
        reasons.append("registered_roots_unavailable")
    full_paths = []
    for path in paths:
        parts = PurePosixPath(path).parts
        root = "/".join(parts[:2]) + "/"
        content = path in policy["content_global_paths"] or (
            len(parts) >= 3 and root in roots
            and PurePosixPath(path).suffix in policy["content_extensions"]
            and not any(part in {"tools", "scripts", "schemas", "policies", "governance", "tests"} for part in parts[2:-1])
            and parts[-1] not in {"AGENTS.md", "SKILL.md", "requirements.txt"}
        )
        if not content:
            full_paths.append(path)
    if full_paths:
        reasons.append("control_or_unknown_path")
    unknown = sorted(set(ids) - set(catalog))
    if unknown:
        reasons.append("uncatalogued_tests")
    proposed = sorted(ids if reasons else [test_id for test_id in ids if catalog[test_id]["group"] == "live_corpus" or catalog[test_id]["smoke"]])
    return {
        "advisory_only": True, "baseline_authenticated": False,
        "activation_blockers": policy["enablement_requires"],
        "proposed_profile": "full" if reasons else "content",
        "reasons": sorted(set(reasons)), "full_trigger_paths": full_paths,
        "uncatalogued_tests": unknown, "selected_ids": proposed,
        "excluded_ids": sorted(set(ids) - set(proposed)),
    }


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
    parser.add_argument("--base")
    parser.add_argument("--profile", choices=("full", "shadow"), default="full")
    parser.add_argument("--report-json", type=Path)
    args = parser.parse_args(argv)
    root = args.repo.resolve()
    timer = AuditTimer()
    report = {"schema": "repository-test-execution/v1", "outcome": "failure", "requested_profile": args.profile, "executed_profile": "full", "selection_enabled": False, "snapshot": args.snapshot, "commit": args.commit, "base": args.base}
    output = None
    try:
        if args.report_json:
            output = report_path(root, args.report_json)
        if args.snapshot == "commit":
            if not args.commit or not FULL_COMMIT_RE.fullmatch(args.commit):
                raise DomainError("commit execution requires an exact commit SHA")
            if run_git(root, "rev-parse", "HEAD").decode().strip() != args.commit:
                raise DomainError("test checkout does not match the audited commit")
            run_git(root, "diff", "--exit-code", "HEAD", "--")
            snapshot = timer.call("snapshot", GitSnapshot.from_commit, root, args.commit)
        else:
            if args.commit:
                raise DomainError("--commit is valid only with --snapshot commit")
            run_git(root, "diff", "--exit-code", "--")
            snapshot = timer.call("snapshot", GitSnapshot.from_index, root)
        policy = load_policy(snapshot)
        report["policy_sha256"] = hashlib.sha256(snapshot.entries[POLICY].data).hexdigest()
        loader = unittest.TestLoader()
        suite = timer.call("discovery", loader.discover, str(root / "tools/tests"), pattern="test_*.py")
        if loader.errors:
            raise DomainError("test discovery failed: " + "\n".join(loader.errors))
        tests = list(flatten(suite))
        catalog, unknown = validate_catalog(snapshot, tests)
        ids = [test.id() for test in tests]
        report["discovered_tests"] = len(ids)
        report["uncatalogued_tests"] = unknown
        if args.profile == "shadow":
            paths, reasons = changed_paths(root, args.snapshot, args.commit, args.base)
            report["changed_paths"] = paths
            report["shadow_plan"] = plan_content(snapshot, policy, catalog, ids, paths, reasons)
        print(f"EXECUTION: full ({len(ids)} tests); selection disabled", flush=True)
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
        summary = {key: report[key] for key in ("outcome", "executed_profile", "selection_enabled", "seconds")}
        summary["tests_run"] = report.get("tests_run", 0)
        summary["slowest_tests"] = sorted(report.get("tests", []), key=lambda row: row["seconds"], reverse=True)[:20]
        summary["git_in_process"] = report.get("git_in_process", {})
        print("TEST_EXECUTION_SUMMARY: " + json.dumps(summary, sort_keys=True), flush=True)


if __name__ == "__main__":
    raise SystemExit(main())
