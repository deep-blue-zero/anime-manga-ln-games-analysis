from __future__ import annotations

import contextlib
import copy
import io
import json
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock

TOOLS = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(TOOLS))
import audit_execution as execution
from audit_timing import AuditTimer, write_report
from character_index_core import DomainError, GitSnapshot, SnapshotEntry


def policy_fixture():
    return json.loads((TOOLS.parent / execution.POLICY).read_text(encoding="utf-8"))


def snapshot_fixture(policy=None, catalog=None):
    documents = {
        execution.POLICY: policy if policy is not None else policy_fixture(),
        "series/registry.json": {"series": [{"repository_path": "series/example/"}]},
        "studies/registry.json": {"studies": []},
    }
    if catalog is not None:
        documents[execution.CATALOG] = {"schema": "repository-test-catalog/v1", "tests": catalog}
    return GitSnapshot(TOOLS.parent, "TEST", {
        path: SnapshotEntry(path, "100644", (json.dumps(document) + "\n").encode())
        for path, document in documents.items()
    })


def catalog_fixture():
    return {
        "fixture.live": {"group": "live_corpus", "smoke": False, "inputs": ["candidate corpus"], "purpose": "live guard"},
        "fixture.smoke": {"group": "regression", "smoke": True, "inputs": ["controlled fixture"], "purpose": "smoke"},
        "fixture.other": {"group": "synthetic_git", "smoke": False, "inputs": ["controlled fixture"], "purpose": "regression"},
    }


class ExecutionPlanTests(unittest.TestCase):
    def plan(self, paths, *, reasons=None, unknown=False):
        catalog = catalog_fixture()
        ids = list(catalog) + (["fixture.new"] if unknown else [])
        return execution.plan_content(snapshot_fixture(), policy_fixture(), catalog, ids, paths, reasons or [])

    def test_content_plan_keeps_live_checks_and_smoke_and_is_advisory(self):
        plan = self.plan(["series/example/reading.md"])
        self.assertEqual(plan["proposed_profile"], "content")
        self.assertEqual(plan["selected_ids"], ["fixture.live", "fixture.smoke"])
        self.assertEqual(plan["excluded_ids"], ["fixture.other"])
        self.assertTrue(plan["advisory_only"])
        self.assertFalse(plan["baseline_authenticated"])
        self.assertTrue(plan["activation_blockers"])

    def test_controls_unknown_paths_and_embedded_scripts_force_full(self):
        for path in ("tools/new.py", ".github/workflows/repository-audit.yml", "governance/source-policies/new.md", "AGENTS.md", "series/example/scripts/script.py", "series/example/policies/rules.md", "series/example/AGENTS.md", "series/example/script.js", "unrecognized.md", "series/new/reading.md"):
            with self.subTest(path=path):
                plan = self.plan(["series/example/reading.md", path])
                self.assertEqual(plan["proposed_profile"], "full")
                self.assertIn(path, plan["full_trigger_paths"])

    def test_registry_and_sheet_data_remain_content_candidates(self):
        for path in ("characters/registry.jsonl", "series/registry.json", "series/example/package/tab.tsv"):
            self.assertEqual(self.plan([path])["proposed_profile"], "content")

    def test_missing_baseline_unknown_tests_and_runtime_force_full(self):
        self.assertEqual(self.plan([], reasons=["baseline_unavailable"])["proposed_profile"], "full")
        self.assertEqual(self.plan([], unknown=True)["proposed_profile"], "full")
        with mock.patch.object(execution.unicodedata, "unidata_version", "other"):
            self.assertIn("runtime_outside_envelope", self.plan([])["reasons"])

    def test_selection_cannot_be_enabled_by_flipping_policy(self):
        policy = policy_fixture()
        policy["selection_enabled"] = True
        with self.assertRaisesRegex(DomainError, "selection disabled"):
            execution.load_policy(snapshot_fixture(policy))

    def test_malformed_policy_groups_fail_closed(self):
        for value in (None, {}, [None], ["regression", "regression"]):
            policy = policy_fixture()
            policy["full_groups"] = value
            with self.subTest(value=value), self.assertRaises(DomainError):
                execution.load_policy(snapshot_fixture(policy))

    def test_complete_delta_uses_no_renames_and_exact_base(self):
        with mock.patch.object(execution, "run_git", side_effect=[b"commit\n", b"", b"tools/prior.py\0series/example/new.md\0"]) as git:
            paths, reasons = execution.changed_paths(Path("."), "commit", "b" * 40, "a" * 40)
            self.assertEqual(reasons, [])
            self.assertIn("tools/prior.py", paths)
            self.assertEqual(git.call_args.args[1:], ("diff", "--name-only", "--no-renames", "-z", "a" * 40, "b" * 40, "--"))

    def test_index_diff_and_unavailable_baselines_do_not_use_latest_commit_only(self):
        with mock.patch.object(execution, "run_git", side_effect=[b"commit\n", b"b" * 40 + b"\n", b"", b"series/example/old.md\0"]) as git:
            execution.changed_paths(Path("."), "index", None, "a" * 40)
            self.assertIn("--cached", git.call_args.args)
        for base in (None, "main", "0" * 40):
            with mock.patch.object(execution, "run_git") as git:
                _, reasons = execution.changed_paths(Path("."), "commit", "b" * 40, base)
                self.assertTrue(reasons)
                git.assert_not_called()
        with mock.patch.object(execution, "run_git", side_effect=DomainError("unavailable")):
            self.assertTrue(execution.changed_paths(Path("."), "commit", "b" * 40, "a" * 40)[1])

    def test_catalog_rejects_stale_duplicate_and_missing_mandatory_groups(self):
        catalog = catalog_fixture()
        tests = [mock.Mock(**{"id.return_value": name}) for name in catalog]
        self.assertEqual(execution.validate_catalog(snapshot_fixture(catalog=catalog), tests)[1], [])
        with self.assertRaisesRegex(DomainError, "duplicated"):
            execution.validate_catalog(snapshot_fixture(catalog=catalog), tests + [tests[0]])
        with self.assertRaisesRegex(DomainError, "stale"):
            execution.validate_catalog(snapshot_fixture(catalog=catalog), tests[:-1])
        changed = copy.deepcopy(catalog)
        changed["fixture.live"]["group"] = "regression"
        with self.assertRaisesRegex(DomainError, "mandatory group"):
            execution.validate_catalog(snapshot_fixture(catalog=changed), tests)

    def test_uncatalogued_test_is_retained_for_full_execution(self):
        catalog = catalog_fixture()
        tests = [mock.Mock(**{"id.return_value": name}) for name in [*catalog, "fixture.new"]]
        _, unknown = execution.validate_catalog(snapshot_fixture(catalog=catalog), tests)
        self.assertEqual(unknown, ["fixture.new"])


class ExecutionResultTests(unittest.TestCase):
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

    def test_shadow_executes_every_discovered_test_once(self):
        class Cases(unittest.TestCase):
            calls = 0
            def test_pass(self):
                Cases.calls += 1
        suite = unittest.defaultTestLoader.loadTestsFromTestCase(Cases)
        test_id = next(execution.flatten(suite)).id()
        catalog = {test_id: {"group": "live_corpus", "smoke": True, "inputs": ["fixture"], "purpose": "test"}}
        snapshot = snapshot_fixture(catalog=catalog)
        with mock.patch.object(execution, "run_git", return_value=b""), mock.patch.object(execution.GitSnapshot, "from_index", return_value=snapshot), mock.patch.object(unittest.TestLoader, "discover", return_value=suite), mock.patch.object(execution, "changed_paths", return_value=([], [])), contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()):
            self.assertEqual(execution.main(["--profile", "shadow"]), 0)
        self.assertEqual(Cases.calls, 1)

    def test_empty_discovery_cannot_succeed(self):
        with self.assertRaisesRegex(DomainError, "empty"):
            execution.validate_catalog(snapshot_fixture(catalog={}), [])

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
