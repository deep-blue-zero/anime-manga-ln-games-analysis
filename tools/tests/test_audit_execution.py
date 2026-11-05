from __future__ import annotations

import contextlib
import io
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock

TOOLS = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(TOOLS))
import audit_execution as execution
from audit_timing import AuditTimer, write_report


class ExecutionResultTests(unittest.TestCase):
    def run_main(self, suite, argv=()):
        with mock.patch.object(execution, "run_git", return_value=b""), \
                mock.patch.object(unittest.TestLoader, "discover", return_value=suite), \
                contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()):
            return execution.main(list(argv))

    def test_timed_runner_preserves_failures_errors_subtests_and_skips(self):
        class Cases(unittest.TestCase):
            def test_pass(self):
                pass
            def test_failure(self):
                with self.subTest(case="broken"):
                    self.fail("expected fixture failure")
            def test_error(self):
                raise RuntimeError("expected fixture error")
            @unittest.skip("fixture skip")
            def test_skip(self):
                pass
        result = execution.execute_suite(unittest.defaultTestLoader.loadTestsFromTestCase(Cases), io.StringIO())
        self.assertFalse(result.wasSuccessful())
        self.assertEqual((result.testsRun, len(result.failures), len(result.errors), len(result.skipped)), (4, 1, 1, 1))
        self.assertEqual(len(result.timings), 4)

    def test_every_discovered_test_runs_exactly_once(self):
        class Cases(unittest.TestCase):
            calls = 0
            def test_first(self):
                Cases.calls += 1
            def test_second(self):
                Cases.calls += 1
        suite = unittest.defaultTestLoader.loadTestsFromTestCase(Cases)
        self.assertEqual(self.run_main(suite), 0)
        self.assertEqual(Cases.calls, 2)

    def test_a_failing_test_fails_the_run(self):
        class Cases(unittest.TestCase):
            def test_failure(self):
                self.fail("expected fixture failure")
        self.assertEqual(self.run_main(unittest.defaultTestLoader.loadTestsFromTestCase(Cases)), 1)

    def test_empty_discovery_cannot_succeed(self):
        self.assertEqual(self.run_main(unittest.TestSuite()), 1)

    def test_commit_execution_requires_the_exact_checked_out_commit(self):
        suite = unittest.TestSuite()
        for argv in (["--snapshot", "commit"], ["--snapshot", "commit", "--commit", "main"],
                     ["--snapshot", "index", "--commit", "a" * 40]):
            with self.subTest(argv=argv):
                self.assertEqual(self.run_main(suite, argv), 1)
        with mock.patch.object(execution, "run_git", return_value=b"b" * 40 + b"\n"), \
                contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()):
            self.assertEqual(execution.main(["--snapshot", "commit", "--commit", "a" * 40]), 1)

    def test_telemetry_cannot_pollute_repository_and_records_failure(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            with self.assertRaisesRegex(ValueError, "outside"):
                write_report(root, root / "inside.json", {})
        timer = AuditTimer()
        def fail():
            raise RuntimeError("fixture")
        with self.assertRaises(RuntimeError):
            timer.call("failing-stage", fail)
        self.assertFalse(timer.report()["stages"][0]["completed"])


if __name__ == "__main__":
    unittest.main()
