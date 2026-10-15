from __future__ import annotations

import hashlib
import json
import os
import re
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


TOOLS = Path(__file__).resolve().parents[1]
ROOT = TOOLS.parent
sys.path.insert(0, str(TOOLS))

from analytical_preflight import ROUTING_OUTPUTS, routing_preflight  # noqa: E402
from character_index_core import GitSnapshot, SnapshotEntry, run_git  # noqa: E402
from validate_repository import (  # noqa: E402
    PROJECT_INITIATION_GATE_PATH,
    _load_project_initiation_gate,
    project_initiation_baseline_paths,
    validate_project_initiation_gate,
    worktree_paths,
    worktree_snapshot,
)


def authority_markdown(artifact_type: str, body: str = "") -> bytes:
    return (
        "---\n"
        f"artifact_type: {artifact_type}\n"
        "status: canonical\n"
        "supersedes: []\n"
        "superseded_by: []\n"
        "do_not_use_as_current_authority: false\n"
        "---\n\n"
        f"{body}\n"
    ).encode("utf-8")


class ProjectInitiationGateTests(unittest.TestCase):
    prefix = "series/example/"
    entrypoint = prefix + "CURRENT_STATE_AND_CORPUS_MAP.md"
    method = prefix + "METHOD.md"
    architecture = prefix + "ARCHITECTURE.md"
    infrastructure = prefix + "LEDGER.md"
    sequential = prefix + "SOURCE_UNIT_01.md"

    @classmethod
    def setUpClass(cls) -> None:
        cls.history_directory = tempfile.TemporaryDirectory(prefix="terminal-gate-history-")
        cls.addClassCleanup(cls.history_directory.cleanup)
        cls.history_root = Path(cls.history_directory.name)
        run_git(cls.history_root, "init", "--quiet")
        run_git(cls.history_root, "config", "user.name", "Gate fixture")
        run_git(cls.history_root, "config", "user.email", "fixture@example.invalid")
        run_git(cls.history_root, "config", "core.autocrlf", "false")
        reading = cls.history_root / cls.sequential
        reading.parent.mkdir(parents=True)
        reading.write_bytes(authority_markdown("volume_deep_reading"))
        run_git(cls.history_root, "add", "--", cls.sequential)
        run_git(cls.history_root, "commit", "--quiet", "-m", "Accepted reading")
        cls.completion_commit = run_git(cls.history_root, "rev-parse", "HEAD").decode().strip()
        # Run stops must name a commit on main; main is the accepted reading here.
        run_git(cls.history_root, "update-ref", "refs/remotes/origin/main", cls.completion_commit)
        cls.reading_blob = run_git(cls.history_root, "rev-parse", f"HEAD:{cls.sequential}").decode().strip()
        reading.write_bytes(authority_markdown("volume_deep_reading", "Changed"))
        run_git(cls.history_root, "add", "--", cls.sequential)
        run_git(cls.history_root, "commit", "--quiet", "-m", "Different historical reading")
        cls.different_commit = run_git(cls.history_root, "rev-parse", "HEAD").decode().strip()
        run_git(cls.history_root, "update-index", "--cacheinfo", f"120000,{cls.reading_blob},{cls.sequential}")
        run_git(cls.history_root, "commit", "--quiet", "-m", "Nonregular historical reading")
        cls.nonregular_commit = run_git(cls.history_root, "rev-parse", "HEAD").decode().strip()

    @staticmethod
    def control() -> dict:
        return {
            "schema": "anime-manga-ln-games-analysis/project-initiation-gate/v1",
            "governing_policy": (
                "governance/source-policies/"
                "MANGA_ANIME_PROJECT_INITIATION_AND_ARCHITECTURE_POLICY.md"
            ),
            "activation_baseline_commit": "a" * 40,
            "prospective_registry_marker": {
                "field": "project_initiation_gate",
                "required_value": "REQUIRED",
            },
            "legacy_compatibility": {
                "baseline_rule": "ROOT_PRESENT_AT_ACTIVATION",
                "git_native_migration_scope_prefix": "GIT_NATIVE_POST_CUTOVER_",
                "new_sequential_work_requires_current_architecture": True,
            },
            "sequential_artifact_classification": {
                "front_matter_field": "artifact_type",
                "exact_types": [
                    "canonical_chronological_supplemental_reading",
                    "case_reading",
                    "continuous_sequential_case_reading",
                    "deep_reading",
                    "soma_character_reading",
                ],
                "suffixes": ["_deep_reading"],
                "untyped_fallback_directory_keywords": [
                    "case reading",
                    "deep reading",
                    "sequential reading",
                    "source facing reading",
                ],
            },
        }

    def state(
        self,
        *,
        method: str | None = "METHOD.md",
        architecture: str | None = "ARCHITECTURE.md",
        infrastructure_initialized: object = True,
        infrastructure: object = None,
        lock: object = "OPEN",
    ) -> str:
        lines = ["```yaml", "project_initialization:"]
        if method is not None:
            lines.append(f"  governing_method: {method}")
        if architecture is not None:
            lines.append(f"  synthesis_architecture: {architecture}")
        if infrastructure_initialized is not None:
            value = (
                str(infrastructure_initialized).lower()
                if isinstance(infrastructure_initialized, bool)
                else str(infrastructure_initialized)
            )
            lines.append(f"  required_day_one_infrastructure_initialized: {value}")
        if infrastructure is not None:
            lines.append("  required_day_one_infrastructure:")
            for value in infrastructure:
                lines.append(f"    - {value}")
        if lock is not None:
            lines.append(f"  sequential_analysis_lock: {lock}")
        lines.append("```")
        return "\n".join(lines)

    def snapshot(
        self,
        *,
        state: str | None = None,
        include_method: bool = True,
        include_architecture: bool = True,
        include_infrastructure: bool = True,
        include_sequential: bool = True,
        method_status: str = "canonical",
        architecture_status: str = "canonical",
        marker: bool = True,
        migration_scope: str | None = None,
        sequential_path: str | None = None,
        sequential_artifact_type: str | None = "volume_deep_reading",
    ) -> GitSnapshot:
        row = {
            "series_id": "example",
            "stable_slug": "example",
            "canonical_title": "Example",
            "repository_path": self.prefix,
            "canonical_entrypoint": self.entrypoint,
            "canonical_entrypoint_status": "PRESENT_VERIFIED",
        }
        if marker:
            row["project_initiation_gate"] = "REQUIRED"
        if migration_scope is not None:
            row["migration_scope"] = migration_scope
        entries = {
            "series/registry.json": SnapshotEntry(
                "series/registry.json",
                "100644",
                (json.dumps({"series": [row]}) + "\n").encode(),
            ),
            "studies/registry.json": SnapshotEntry(
                "studies/registry.json", "100644", b'{"studies":[]}\n'
            ),
            PROJECT_INITIATION_GATE_PATH: SnapshotEntry(
                PROJECT_INITIATION_GATE_PATH,
                "100644",
                (json.dumps(self.control()) + "\n").encode(),
            ),
            self.control()["governing_policy"]: SnapshotEntry(
                self.control()["governing_policy"], "100644", b"# Policy\n"
            ),
            self.entrypoint: SnapshotEntry(
                self.entrypoint,
                "100644",
                authority_markdown(
                    "corpus_map", state if state is not None else self.state()
                ),
            ),
        }
        if include_method:
            entries[self.method] = SnapshotEntry(
                self.method,
                "100644",
                authority_markdown("analytical_method").replace(
                    b"status: canonical", f"status: {method_status}".encode()
                ),
            )
        if include_architecture:
            entries[self.architecture] = SnapshotEntry(
                self.architecture,
                "100644",
                authority_markdown("synthesis_architecture").replace(
                    b"status: canonical", f"status: {architecture_status}".encode()
                ),
            )
        if include_infrastructure:
            entries[self.infrastructure] = SnapshotEntry(
                self.infrastructure, "100644", authority_markdown("ledger")
            )
        if include_sequential:
            path = sequential_path or self.sequential
            data = (
                authority_markdown(sequential_artifact_type)
                if sequential_artifact_type is not None
                else b"# Substantive source-unit reading\n"
            )
            entries[path] = SnapshotEntry(path, "100644", data)
        return GitSnapshot(ROOT, "IN_MEMORY_PROJECT_GATE", entries)

    def failures(
        self, snapshot: GitSnapshot, baseline_paths: set[str] | None = None
    ) -> list[str]:
        return validate_project_initiation_gate(snapshot, baseline_paths or set())

    def assert_failure_contains(self, failures: list[str], text: str) -> None:
        self.assertTrue(any(text in failure for failure in failures), failures)

    def test_first_sequential_reading_requires_synthesis_architecture_artifact(self) -> None:
        failures = self.failures(self.snapshot(include_architecture=False))
        self.assert_failure_contains(
            failures, "referenced governing synthesis architecture is missing"
        )

    def test_method_without_synthesis_architecture_declaration_fails(self) -> None:
        failures = self.failures(
            self.snapshot(state=self.state(architecture=None), include_architecture=False)
        )
        self.assert_failure_contains(failures, "does not identify governing synthesis architecture")

    def test_synthesis_architecture_without_method_declaration_fails(self) -> None:
        failures = self.failures(
            self.snapshot(state=self.state(method=None), include_method=False)
        )
        self.assert_failure_contains(failures, "does not identify governing analytical method")

    def test_entrypoint_must_identify_both_governing_artifacts(self) -> None:
        failures = self.failures(
            self.snapshot(
                state=self.state(method=None, architecture=None),
                include_method=False,
                include_architecture=False,
            )
        )
        self.assert_failure_contains(failures, "does not identify governing analytical method")
        self.assert_failure_contains(failures, "does not identify governing synthesis architecture")

    def test_referenced_governing_artifacts_must_exist(self) -> None:
        for field, state, expected in (
            (
                "method",
                self.state(method="MISSING.md"),
                "governing analytical method is missing",
            ),
            (
                "architecture",
                self.state(architecture="MISSING.md"),
                "governing synthesis architecture is missing",
            ),
        ):
            with self.subTest(field=field):
                self.assert_failure_contains(self.failures(self.snapshot(state=state)), expected)

    def test_governing_artifacts_must_be_current_eligible(self) -> None:
        for field, kwargs, expected in (
            (
                "method",
                {"method_status": "draft_noncurrent"},
                "governing analytical method is not current-eligible",
            ),
            (
                "architecture",
                {"architecture_status": "historical_legacy"},
                "governing synthesis architecture is not current-eligible",
            ),
        ):
            with self.subTest(field=field):
                self.assert_failure_contains(self.failures(self.snapshot(**kwargs)), expected)

    def test_sequential_reading_fails_while_lock_is_closed(self) -> None:
        failures = self.failures(self.snapshot(state=self.state(lock="CLOSED")))
        self.assert_failure_contains(failures, "requires sequential_analysis_lock OPEN")

    def test_sequential_reading_requires_present_well_formed_lock(self) -> None:
        for lock in (None, "READY", True):
            with self.subTest(lock=lock):
                failures = self.failures(self.snapshot(state=self.state(lock=lock)))
                self.assert_failure_contains(
                    failures, "sequential_analysis_lock must be explicitly OPEN or CLOSED"
                )

    def test_sequential_reading_requires_initialized_infrastructure(self) -> None:
        failures = self.failures(
            self.snapshot(state=self.state(infrastructure_initialized=False))
        )
        self.assert_failure_contains(
            failures,
            "required day-one infrastructure must be explicitly initialized",
        )
        missing_path = self.failures(
            self.snapshot(
                state=self.state(infrastructure=["MISSING_LEDGER.md"]),
                include_infrastructure=False,
            )
        )
        self.assert_failure_contains(missing_path, "required day-one infrastructure is missing")

    def test_bootstrap_only_project_may_remain_closed_and_incomplete(self) -> None:
        snapshot = self.snapshot(
            state=self.state(
                method=None,
                architecture=None,
                infrastructure_initialized=False,
                lock="CLOSED",
            ),
            include_method=False,
            include_architecture=False,
            include_infrastructure=False,
            include_sequential=False,
        )
        self.assertEqual(self.failures(snapshot), [])

    def test_fully_initialized_new_project_with_first_reading_passes(self) -> None:
        snapshot = self.snapshot(
            state=self.state(infrastructure=["LEDGER.md"]),
            sequential_path=self.prefix + "02 Sequential Readings/UNIT_01.md",
        )
        self.assertEqual(self.failures(snapshot), [])

    def test_new_root_requires_prospective_registry_marker(self) -> None:
        failures = self.failures(self.snapshot(marker=False, include_sequential=False))
        self.assert_failure_contains(failures, "project_initiation_gate must equal 'REQUIRED'")

    def test_git_native_baseline_root_is_checked_before_its_next_reading(self) -> None:
        snapshot = self.snapshot(
            marker=False,
            migration_scope="GIT_NATIVE_POST_CUTOVER_EXAMPLE_BOOTSTRAP_V0_1",
            state=self.state(architecture=None, lock="OPEN"),
            include_architecture=False,
        )
        failures = self.failures(snapshot, {self.prefix + "BASELINE.md"})
        self.assert_failure_contains(failures, "does not identify governing synthesis architecture")

    def test_legacy_root_uses_coherent_current_architecture_without_new_block(self) -> None:
        entrypoint_body = "Governing method: `METHOD.md`\nArchitecture: `ARCHITECTURE.md`"
        snapshot = self.snapshot(
            marker=False,
            state=entrypoint_body,
            migration_scope="G5_FINAL_AGGREGATE",
        )
        self.assertEqual(self.failures(snapshot, {self.prefix + "BASELINE.md"}), [])

    def test_baseline_readings_do_not_retroactively_require_initialization(self) -> None:
        for scope in ('G5_FINAL_AGGREGATE', 'GIT_NATIVE_POST_CUTOVER_EXAMPLE'):
            with self.subTest(scope=scope):
                snapshot = self.snapshot(
                    marker=False, migration_scope=scope, state='',
                    include_method=False, include_architecture=False,
                    include_infrastructure=False,
                )
                self.assertEqual(self.failures(snapshot, set(snapshot.entries)), [])

    def test_pre_enforcement_branch_reading_uses_baseline_paths_not_authored_date(self) -> None:
        snapshot = self.snapshot(
            marker=False, migration_scope='GIT_NATIVE_POST_CUTOVER_EXAMPLE', state='',
        )
        original = snapshot.entries[self.sequential]
        snapshot.entries[self.sequential] = SnapshotEntry(
            original.path, original.mode,
            original.data.replace(b'---\n', b'---\nauthored_at: "2020-01-01"\n', 1),
        )
        baseline = set(snapshot.entries) - {self.sequential}
        self.assert_failure_contains(self.failures(snapshot, baseline), 'requires sequential_analysis_lock OPEN')
        self.assertEqual(self.failures(snapshot, set(snapshot.entries)), [])

    def test_legacy_branch_reading_requires_routes_but_not_a_new_initialization_block(self) -> None:
        snapshot = self.snapshot(
            marker=False, migration_scope='G5_FINAL_AGGREGATE', state='',
        )
        baseline = set(snapshot.entries) - {self.sequential}
        self.assert_failure_contains(self.failures(snapshot, baseline), 'legacy continuation does not identify')
        snapshot.entries[self.entrypoint] = SnapshotEntry(
            self.entrypoint, '100644',
            authority_markdown('corpus_map', 'Read `METHOD.md` and `ARCHITECTURE.md`.'),
        )
        self.assertEqual(self.failures(snapshot, baseline), [])

    def test_material_restart_requires_contract_even_when_all_paths_are_in_baseline(self) -> None:
        snapshot = self.snapshot(marker=True, state='')
        self.assert_failure_contains(self.failures(snapshot, set(snapshot.entries)), 'must be explicitly OPEN or CLOSED')

    def test_structured_role_not_filename_drives_detection(self) -> None:
        failures = self.failures(
            self.snapshot(
                state=self.state(lock="CLOSED"),
                sequential_path=self.prefix + "NOT_NAMED_DEEP_READING.md",
                sequential_artifact_type="episode_deep_reading",
            )
        )
        self.assert_failure_contains(failures, "requires sequential_analysis_lock OPEN")

    def test_untyped_sequential_directory_artifact_fails_closed(self) -> None:
        failures = self.failures(
            self.snapshot(
                state=self.state(lock="CLOSED"),
                sequential_path=self.prefix + "02 Sequential Readings/UNIT_01.md",
                sequential_artifact_type=None,
            )
        )
        self.assert_failure_contains(failures, "requires a structured artifact_type")

    def terminal_declarations(self) -> str:
        return (
            self.state(lock="CLOSED", infrastructure=["LEDGER.md"])
            .removeprefix("```yaml\n").removesuffix("\n```")
            + "\n  next_permitted_operation: NONE_ADMITTED_BOUNDARIES_COMPLETE\n"
            + "sequential_execution:\n  run_state: complete\n"
            + "  next_candidate_operation: NONE_TERMINAL_BOUNDARY_COMPLETE\n"
            + "supplemental_execution:\n  current_state: CLOSED_BOUNDARY_COMPLETE\n"
            + "  other_narrative_admission: NOT_AUTHORIZED\n"
        )

    def terminal_snapshot(self) -> GitSnapshot:
        snapshot = self.snapshot(state="")
        snapshot.root = self.history_root
        declarations = self.terminal_declarations()
        entry = snapshot.entries[self.entrypoint]
        snapshot.entries[self.entrypoint] = SnapshotEntry(
            self.entrypoint, entry.mode,
            entry.data.replace(b"---\n\n", declarations.encode() + b"---\n\n", 1)
            + b"SEQUENTIAL_ANALYSIS_LOCK = CLOSED\n",
        )
        control = self.control()
        control["terminal_closures"] = {self.prefix: {
            "canonical_entrypoint": self.entrypoint,
            "completion_commit": self.completion_commit,
            "supplemental_execution_required": True,
            "frozen_sequential_artifacts": {
                self.sequential: hashlib.sha256(snapshot.entries[self.sequential].data).hexdigest()
            },
        }}
        snapshot.entries[PROJECT_INITIATION_GATE_PATH] = SnapshotEntry(
            PROJECT_INITIATION_GATE_PATH, "100644", json.dumps(control).encode()
        )
        return snapshot

    def test_terminal_closure_preserves_only_reviewed_completed_readings(self) -> None:
        snapshot = self.terminal_snapshot()
        for baseline in (set(), set(snapshot.entries)):
            with self.subTest(baseline=bool(baseline)):
                self.assertEqual(self.failures(snapshot, baseline), [])
        # Completion metadata alone is never an exemption from the OPEN gate.
        snapshot.entries[PROJECT_INITIATION_GATE_PATH] = self.snapshot().entries[PROJECT_INITIATION_GATE_PATH]
        self.assert_failure_contains(self.failures(snapshot), "requires sequential_analysis_lock OPEN")

    def test_terminal_closure_rejects_added_changed_missing_and_renamed_readings(self) -> None:
        for mutation in ("added", "changed", "missing", "renamed", "retyped", "untracked"):
            for baseline_contains_reading in (False, True):
                with self.subTest(mutation=mutation, baseline=baseline_contains_reading):
                    snapshot = self.terminal_snapshot()
                    baseline = set(snapshot.entries) if baseline_contains_reading else set()
                    entry = snapshot.entries[self.sequential]
                    if mutation in {"added", "renamed"}:
                        path = self.prefix + "ANOTHER_SOURCE.md"
                        snapshot.entries[path] = SnapshotEntry(path, entry.mode, entry.data)
                    if mutation in {"missing", "renamed"}:
                        del snapshot.entries[self.sequential]
                    if mutation == "changed":
                        snapshot.entries[self.sequential] = SnapshotEntry(entry.path, entry.mode, entry.data + b"Changed\n")
                    if mutation == "retyped":
                        snapshot.entries[self.sequential] = SnapshotEntry(entry.path, entry.mode, authority_markdown("essay"))
                    if mutation == "untracked":
                        snapshot.entries[self.sequential] = SnapshotEntry(entry.path, entry.mode, entry.data, tracked=False)
                    self.assert_failure_contains(self.failures(snapshot, baseline), "terminal")

    def test_terminal_closure_requires_closed_completed_consistent_routing_and_foundation(self) -> None:
        for old, new, expected in (
            (b"sequential_analysis_lock: CLOSED", b"sequential_analysis_lock: OPEN", "requires sequential_analysis_lock CLOSED"),
            (b"SEQUENTIAL_ANALYSIS_LOCK = CLOSED", b"SEQUENTIAL_ANALYSIS_LOCK = OPEN", "contradicts prose lock OPEN"),
            (b"run_state: complete", b"run_state: running", "requires run_state complete"),
            (b"next_permitted_operation: NONE_ADMITTED_BOUNDARIES_COMPLETE", b"next_permitted_operation: READ_NEXT", "requires next_permitted_operation NONE"),
            (b"next_candidate_operation: NONE_TERMINAL_BOUNDARY_COMPLETE", b"next_candidate_operation: READ_NEXT", "requires next_candidate_operation NONE"),
            (b"required_day_one_infrastructure_initialized: true", b"required_day_one_infrastructure_initialized: false", "infrastructure must be explicitly initialized"),
            (b"governing_method: METHOD.md", b"governing_method: MISSING.md", "governing analytical method is missing"),
            (b"synthesis_architecture: ARCHITECTURE.md", b"synthesis_architecture: MISSING.md", "governing synthesis architecture is missing"),
            (b"current_state: CLOSED_BOUNDARY_COMPLETE", b"current_state: OPEN", "terminal supplemental execution must be CLOSED"),
        ):
            with self.subTest(expected=expected):
                snapshot = self.terminal_snapshot()
                entry = snapshot.entries[self.entrypoint]
                self.assertEqual(entry.data.count(old), 1)
                snapshot.entries[self.entrypoint] = SnapshotEntry(entry.path, entry.mode, entry.data.replace(old, new, 1))
                self.assert_failure_contains(self.failures(snapshot), expected)
        snapshot = self.terminal_snapshot()
        snapshot.entries[self.method] = SnapshotEntry(self.method, "100644", authority_markdown("analytical_method").replace(b"status: canonical", b"status: draft_noncurrent"))
        self.assert_failure_contains(self.failures(snapshot), "governing analytical method is not current-eligible")

    def test_terminal_closure_control_fails_closed_on_malformed_or_unregistered_records(self) -> None:
        for mutation in ("root", "fields", "commit", "entrypoint", "outside", "hash", "empty", "unregistered", "supplemental_required", "supplemental_missing"):
            with self.subTest(mutation=mutation):
                snapshot = self.terminal_snapshot()
                control = json.loads(snapshot.entries[PROJECT_INITIATION_GATE_PATH].data)
                closure = control["terminal_closures"][self.prefix]
                if mutation == "root":
                    control["terminal_closures"] = {"../example/": closure}
                elif mutation == "fields":
                    closure["unreviewed_bypass"] = True
                elif mutation == "commit":
                    closure["completion_commit"] = "main"
                elif mutation == "entrypoint":
                    closure["canonical_entrypoint"] = None
                elif mutation == "outside":
                    closure["frozen_sequential_artifacts"] = {"series/other/READING.md": "a" * 64}
                elif mutation == "hash":
                    closure["frozen_sequential_artifacts"][self.sequential] = "not-a-digest"
                elif mutation == "empty":
                    closure["frozen_sequential_artifacts"] = {}
                elif mutation == "supplemental_required":
                    closure["supplemental_execution_required"] = "true"
                elif mutation == "supplemental_missing":
                    del closure["supplemental_execution_required"]
                else:
                    snapshot.entries["series/registry.json"] = SnapshotEntry("series/registry.json", "100644", b'{"series":[]}\n')
                snapshot.entries[PROJECT_INITIATION_GATE_PATH] = SnapshotEntry(PROJECT_INITIATION_GATE_PATH, "100644", json.dumps(control).encode())
                self.assert_failure_contains(self.failures(snapshot), "terminal")

    def test_terminal_closure_resolves_commit_objects_offline(self) -> None:
        for commit in ("0" * 40, self.reading_blob, self.different_commit):
            with self.subTest(commit=commit):
                snapshot = self.terminal_snapshot()
                control = json.loads(snapshot.entries[PROJECT_INITIATION_GATE_PATH].data)
                control["terminal_closures"][self.prefix]["completion_commit"] = commit
                snapshot.entries[PROJECT_INITIATION_GATE_PATH] = SnapshotEntry(
                    PROJECT_INITIATION_GATE_PATH, "100644", json.dumps(control).encode()
                )
                self.assert_failure_contains(self.failures(snapshot), "completion_commit")

    def test_terminal_closure_rejects_joint_reading_and_digest_replacement(self) -> None:
        snapshot = self.terminal_snapshot()
        entry = snapshot.entries[self.sequential]
        replacement = entry.data + b"Unreviewed replacement\n"
        snapshot.entries[self.sequential] = SnapshotEntry(entry.path, entry.mode, replacement)
        control = json.loads(snapshot.entries[PROJECT_INITIATION_GATE_PATH].data)
        control["terminal_closures"][self.prefix]["frozen_sequential_artifacts"][self.sequential] = hashlib.sha256(replacement).hexdigest()
        snapshot.entries[PROJECT_INITIATION_GATE_PATH] = SnapshotEntry(
            PROJECT_INITIATION_GATE_PATH, "100644", json.dumps(control).encode()
        )
        self.assert_failure_contains(self.failures(snapshot), "seal does not match completion_commit tree")

    def test_terminal_closure_rejects_missing_or_nonregular_historical_reading(self) -> None:
        for mutation in ("missing", "nonregular"):
            with self.subTest(mutation=mutation):
                snapshot = self.terminal_snapshot()
                control = json.loads(snapshot.entries[PROJECT_INITIATION_GATE_PATH].data)
                closure = control["terminal_closures"][self.prefix]
                if mutation == "missing":
                    path = self.prefix + "NOT_IN_HISTORY.md"
                    entry = snapshot.entries.pop(self.sequential)
                    snapshot.entries[path] = SnapshotEntry(path, entry.mode, entry.data)
                    closure["frozen_sequential_artifacts"] = {path: hashlib.sha256(entry.data).hexdigest()}
                else:
                    closure["completion_commit"] = self.nonregular_commit
                snapshot.entries[PROJECT_INITIATION_GATE_PATH] = SnapshotEntry(
                    PROJECT_INITIATION_GATE_PATH, "100644", json.dumps(control).encode()
                )
                self.assert_failure_contains(self.failures(snapshot), "seal does not match completion_commit tree")

    def test_terminal_closure_requires_declared_supplemental_lane(self) -> None:
        lane = (
            b"supplemental_execution:\n  current_state: CLOSED_BOUNDARY_COMPLETE\n"
            b"  other_narrative_admission: NOT_AUTHORIZED\n"
        )
        for replacement in (
            b"", b"supplemental_execution: null\n", b"supplemental_execution: []\n",
            b"supplemental_execution:\n  current_state: CLOSED\n",
            lane.replace(b"NOT_AUTHORIZED", b"AUTHORIZED"),
        ):
            with self.subTest(replacement=replacement):
                snapshot = self.terminal_snapshot()
                entry = snapshot.entries[self.entrypoint]
                self.assertEqual(entry.data.count(lane), 1)
                snapshot.entries[entry.path] = SnapshotEntry(entry.path, entry.mode, entry.data.replace(lane, replacement, 1))
                self.assert_failure_contains(self.failures(snapshot), "terminal supplemental execution must be CLOSED")

    def test_terminal_closure_without_required_lane_remains_valid_and_checks_present_lane(self) -> None:
        snapshot = self.terminal_snapshot()
        control = json.loads(snapshot.entries[PROJECT_INITIATION_GATE_PATH].data)
        control["terminal_closures"][self.prefix]["supplemental_execution_required"] = False
        snapshot.entries[PROJECT_INITIATION_GATE_PATH] = SnapshotEntry(
            PROJECT_INITIATION_GATE_PATH, "100644", json.dumps(control).encode()
        )
        entry = snapshot.entries[self.entrypoint]
        snapshot.entries[entry.path] = SnapshotEntry(entry.path, entry.mode, entry.data.replace(b"current_state: CLOSED_BOUNDARY_COMPLETE", b"current_state: OPEN"))
        self.assert_failure_contains(self.failures(snapshot), "terminal supplemental execution must be CLOSED")
        snapshot.entries[entry.path] = SnapshotEntry(entry.path, entry.mode, entry.data.replace(
            b"supplemental_execution:\n  current_state: CLOSED_BOUNDARY_COMPLETE\n  other_narrative_admission: NOT_AUTHORIZED\n", b""
        ))
        self.assertEqual(self.failures(snapshot), [])

    def test_terminal_closure_validates_staged_snapshot_against_recorded_history(self) -> None:
        # HEAD deliberately differs from completion_commit. The staged candidate
        # retains the accepted bytes and needs neither a network nor a commit.
        snapshot = self.terminal_snapshot()
        with tempfile.TemporaryDirectory(prefix="terminal-gate-index-") as directory:
            root = Path(directory)
            run_git(root, "clone", "--quiet", "--no-checkout", "--no-hardlinks", str(self.history_root), ".")
            run_git(root, "config", "core.autocrlf", "false")
            # Any real checkout carries main; the gate reads run stops from it.
            run_git(root, "update-ref", "refs/remotes/origin/main", self.completion_commit)
            for path, entry in snapshot.entries.items():
                full = root / path
                full.parent.mkdir(parents=True, exist_ok=True)
                full.write_bytes(entry.data)
            run_git(root, "add", "--", *sorted(snapshot.entries))
            staged = GitSnapshot.from_index(root)
            self.assertEqual(self.failures(staged), [])
            self.assertNotEqual(run_git(root, "rev-parse", "HEAD").decode().strip(), self.completion_commit)

    def block_terminal_snapshot(self, declarations: str | None = None) -> GitSnapshot:
        """Return the reviewed closure with terminal state only in a fenced block."""

        snapshot = self.terminal_snapshot()
        body = (
            "```yaml\n" + (declarations or self.terminal_declarations())
            + "```\n\nSEQUENTIAL_ANALYSIS_LOCK = CLOSED"
        )
        snapshot.entries[self.entrypoint] = SnapshotEntry(
            self.entrypoint, "100644", authority_markdown("corpus_map", body)
        )
        return snapshot

    def test_terminal_closure_reads_recognized_initialization_block_like_the_lock(self) -> None:
        # The lock reader accepts a fenced project_initialization block. The
        # terminal reader must read that same surface instead of forcing a
        # cosmetic move into front matter; its requirements are unchanged.
        self.assertEqual(self.failures(self.block_terminal_snapshot()), [])
        completed = self.terminal_declarations().replace(
            "run_state: complete\n", "run_state: completed\n"
        )
        self.assertEqual(self.failures(self.block_terminal_snapshot(completed)), [])
        for old, new, expected in (
            (b"sequential_analysis_lock: CLOSED", b"sequential_analysis_lock: OPEN", "requires sequential_analysis_lock CLOSED"),
            (b"run_state: complete\n", b"run_state: running\n", "requires run_state complete"),
            (b"run_state: complete\n", b"run_state: [complete]\n", "requires run_state complete"),
            (b"next_permitted_operation: NONE_ADMITTED_BOUNDARIES_COMPLETE", b"next_permitted_operation: READ_NEXT", "requires next_permitted_operation NONE"),
            (b"next_candidate_operation: NONE_TERMINAL_BOUNDARY_COMPLETE", b"next_candidate_operation: READ_NEXT", "requires next_candidate_operation NONE"),
            (b"other_narrative_admission: NOT_AUTHORIZED", b"other_narrative_admission: AUTHORIZED", "terminal supplemental execution must be CLOSED"),
        ):
            with self.subTest(expected=expected, new=new):
                snapshot = self.block_terminal_snapshot()
                entry = snapshot.entries[self.entrypoint]
                self.assertEqual(entry.data.count(old), 1)
                snapshot.entries[self.entrypoint] = SnapshotEntry(
                    entry.path, entry.mode, entry.data.replace(old, new, 1)
                )
                self.assert_failure_contains(self.failures(snapshot), expected)

    def test_terminal_closure_fails_closed_on_contradictory_or_malformed_surfaces(self) -> None:
        for block, expected in (
            (
                "project_initialization:\n  next_permitted_operation: READ_NEXT\n",
                "contradictory terminal declarations for project_initialization.next_permitted_operation",
            ),
            (
                "project_initialization: {}\nsequential_execution:\n  run_state: running\n",
                "contradictory terminal declarations for sequential_execution.run_state",
            ),
            (
                "project_initialization: {}\nsupplemental_execution:\n  other_narrative_admission: AUTHORIZED\n",
                "contradictory terminal declarations for supplemental_execution.other_narrative_admission",
            ),
            (
                "project_initialization: {}\nsequential_execution: null\n",
                "terminal sequential_execution must be a mapping wherever declared",
            ),
            ("project_initialization: {}\nsequential_execution:\n  run_state: complete\n", None),
        ):
            with self.subTest(block=block):
                snapshot = self.terminal_snapshot()
                entry = snapshot.entries[self.entrypoint]
                snapshot.entries[self.entrypoint] = SnapshotEntry(
                    entry.path, entry.mode,
                    entry.data + b"\n```yaml\n" + block.encode() + b"```\n",
                )
                failures = self.failures(snapshot)
                if expected is None:
                    self.assertEqual(failures, [])  # Agreeing restatement is harmless.
                else:
                    self.assert_failure_contains(failures, expected)

    def test_completed_run_requires_reviewed_global_closure_to_close_its_lock(self) -> None:
        # Medalist regression: truthful completion metadata in the series
        # entrypoint cannot by itself retain post-baseline readings behind
        # CLOSED, and a completed run may not keep OPEN under its closure.
        snapshot = self.block_terminal_snapshot(
            self.terminal_declarations().replace("run_state: complete\n", "run_state: completed\n")
        )
        reviewed = snapshot.entries[PROJECT_INITIATION_GATE_PATH]
        snapshot.entries[PROJECT_INITIATION_GATE_PATH] = self.snapshot().entries[PROJECT_INITIATION_GATE_PATH]
        self.assert_failure_contains(self.failures(snapshot), "requires sequential_analysis_lock OPEN")
        snapshot.entries[PROJECT_INITIATION_GATE_PATH] = reviewed
        self.assertEqual(self.failures(snapshot), [])
        entry = snapshot.entries[self.entrypoint]
        reopened = entry.data.replace(
            b"sequential_analysis_lock: CLOSED", b"sequential_analysis_lock: OPEN"
        ).replace(b"SEQUENTIAL_ANALYSIS_LOCK = CLOSED", b"SEQUENTIAL_ANALYSIS_LOCK = OPEN")
        snapshot.entries[self.entrypoint] = SnapshotEntry(entry.path, entry.mode, reopened)
        failures = self.failures(snapshot)
        self.assert_failure_contains(failures, "requires sequential_analysis_lock CLOSED")
        self.assert_failure_contains(failures, "contradicts prose lock OPEN")

    def test_terminal_closure_permits_evidence_backed_revision_without_admission(self) -> None:
        # Revising interpretations of already-admitted evidence uses
        # non-sequential homes. The closure neither blocks that revision nor
        # treats it as authorization to admit or rewrite a sealed reading.
        directory = self.prefix + "02 Sequential Readings/"
        erratum = directory + "SOURCE_UNIT_01_ERRATUM.md"
        synthesis = self.prefix + "SPECIALIST_SYNTHESIS_V2.md"

        def revised() -> GitSnapshot:
            snapshot = self.terminal_snapshot()
            snapshot.entries[self.infrastructure] = SnapshotEntry(
                self.infrastructure, "100644",
                authority_markdown("ledger", "CLAIM-0001 REVISE with locator; prior version retained."),
            )
            snapshot.entries[erratum] = SnapshotEntry(
                erratum, "100644",
                authority_markdown("sequential_reading_erratum", "Corrects SOURCE_UNIT_01 without altering its sealed bytes."),
            )
            snapshot.entries[synthesis] = SnapshotEntry(
                synthesis, "100644", authority_markdown("specialist_synthesis")
            )
            return snapshot

        self.assertEqual(self.failures(revised()), [])
        for mutation, expected in (
            ("in_place", "terminal frozen reading bytes changed"),
            ("sequential_type", "terminal sequential corpus differs from reviewed closure"),
            ("untyped", "requires a structured artifact_type"),
        ):
            with self.subTest(mutation=mutation):
                snapshot = revised()
                if mutation == "in_place":
                    entry = snapshot.entries[self.sequential]
                    snapshot.entries[self.sequential] = SnapshotEntry(
                        entry.path, entry.mode, entry.data + b"Corrected in place.\n"
                    )
                elif mutation == "sequential_type":
                    snapshot.entries[erratum] = SnapshotEntry(
                        erratum, "100644", authority_markdown("volume_deep_reading")
                    )
                else:
                    snapshot.entries[erratum] = SnapshotEntry(
                        erratum, "100644", b"# Correction without structured role\n"
                    )
                self.assert_failure_contains(self.failures(snapshot), expected)

    def test_series_local_exception_declarations_cannot_create_terminal_authority(self) -> None:
        # A series-scoped task cannot write the global closure control, and no
        # unrecognized declaration substitutes for it: only the schema-bound
        # .repository/run-closure.json record is read from a project.
        reviewed = json.loads(self.terminal_snapshot().entries[PROJECT_INITIATION_GATE_PATH].data)
        snapshot = self.terminal_snapshot()
        snapshot.entries[PROJECT_INITIATION_GATE_PATH] = self.snapshot().entries[PROJECT_INITIATION_GATE_PATH]
        entry = snapshot.entries[self.entrypoint]
        claimed = (
            "analytical_fidelity_exception:\n  status: APPROVED\n"
            "  waives: project_initiation_gate\n"
            "terminal_closures: " + json.dumps(reviewed["terminal_closures"]) + "\n"
        ).encode()
        snapshot.entries[self.entrypoint] = SnapshotEntry(
            entry.path, entry.mode, entry.data.replace(b"---\n\n", claimed + b"---\n\n", 1)
        )
        local = self.prefix + ".repository/project-initiation-gate.json"
        snapshot.entries[local] = SnapshotEntry(
            local, "100644", json.dumps({"terminal_closures": reviewed["terminal_closures"]}).encode()
        )
        self.assert_failure_contains(self.failures(snapshot), "requires sequential_analysis_lock OPEN")

        control = self.control()
        control["analytical_fidelity_exceptions"] = {self.prefix: {"waive": "terminal_closures"}}
        snapshot.entries[PROJECT_INITIATION_GATE_PATH] = SnapshotEntry(
            PROJECT_INITIATION_GATE_PATH, "100644", json.dumps(control).encode()
        )
        self.assert_failure_contains(self.failures(snapshot), "requires sequential_analysis_lock OPEN")

        reviewed["terminal_closures"][self.prefix]["analytical_fidelity_exception"] = "APPROVED"
        snapshot.entries[PROJECT_INITIATION_GATE_PATH] = SnapshotEntry(
            PROJECT_INITIATION_GATE_PATH, "100644", json.dumps(reviewed).encode()
        )
        self.assert_failure_contains(self.failures(snapshot), "invalid terminal closure fields")

    run_closure = prefix + ".repository/run-closure.json"

    def run_closure_snapshot(self, state: str = "CLOSED") -> GitSnapshot:
        """Move the reviewed terminal fixture's record into the project's own run closure."""

        snapshot = self.terminal_snapshot()
        closure = json.loads(snapshot.entries[PROJECT_INITIATION_GATE_PATH].data)["terminal_closures"][self.prefix]
        snapshot.entries[PROJECT_INITIATION_GATE_PATH] = self.snapshot().entries[PROJECT_INITIATION_GATE_PATH]
        record = {"schema": "anime-manga-ln-games-analysis/project-run-closure/v1", "state": state, **closure}
        snapshot.entries[self.run_closure] = SnapshotEntry(
            self.run_closure, "100644", (json.dumps(record, indent=2) + "\n").encode()
        )
        if state == "REOPENED":
            # The next authorized run: the ordinary OPEN contract, no terminal state.
            snapshot.entries[self.entrypoint] = self.snapshot().entries[self.entrypoint]
        return snapshot

    def test_project_run_closure_seals_a_completed_run_like_a_terminal_closure(self) -> None:
        self.assertEqual(self.failures(self.run_closure_snapshot()), [])
        later = self.prefix + "SOURCE_UNIT_02.md"
        for mutation, expected in (
            ("changed", "terminal frozen reading bytes changed"),
            ("added", "terminal sequential corpus differs from reviewed closure"),
            ("open", "requires sequential_analysis_lock CLOSED"),
        ):
            with self.subTest(mutation=mutation):
                snapshot = self.run_closure_snapshot()
                if mutation == "changed":
                    entry = snapshot.entries[self.sequential]
                    snapshot.entries[self.sequential] = SnapshotEntry(entry.path, entry.mode, entry.data + b"Edited.\n")
                elif mutation == "added":
                    snapshot.entries[later] = SnapshotEntry(later, "100644", authority_markdown("volume_deep_reading", "Second"))
                else:
                    entry = snapshot.entries[self.entrypoint]
                    snapshot.entries[self.entrypoint] = SnapshotEntry(
                        entry.path, entry.mode,
                        entry.data.replace(b"sequential_analysis_lock: CLOSED", b"sequential_analysis_lock: OPEN"),
                    )
                self.assert_failure_contains(self.failures(snapshot), expected)

    def test_reopened_run_closure_keeps_seals_while_the_next_run_adds_readings(self) -> None:
        later = self.prefix + "SOURCE_UNIT_02.md"
        snapshot = self.run_closure_snapshot("REOPENED")
        self.assertEqual(self.failures(snapshot), [])
        snapshot.entries[later] = SnapshotEntry(later, "100644", authority_markdown("volume_deep_reading", "Second"))
        self.assertEqual(self.failures(snapshot), [])
        for mutation, expected in (
            ("changed", "terminal frozen reading bytes changed"),
            ("retyped", "reopened run closure no longer finds sealed readings"),
            ("missing", "terminal frozen reading bytes changed or are missing"),
            ("closed", "requires sequential_analysis_lock OPEN"),
        ):
            with self.subTest(mutation=mutation):
                snapshot = self.run_closure_snapshot("REOPENED")
                snapshot.entries[later] = SnapshotEntry(later, "100644", authority_markdown("volume_deep_reading", "Second"))
                if mutation == "changed":
                    entry = snapshot.entries[self.sequential]
                    snapshot.entries[self.sequential] = SnapshotEntry(entry.path, entry.mode, entry.data + b"Edited.\n")
                elif mutation == "retyped":
                    snapshot.entries[self.sequential] = SnapshotEntry(
                        self.sequential, "100644", authority_markdown("reconstruction_checkpoint")
                    )
                elif mutation == "missing":
                    del snapshot.entries[self.sequential]
                else:
                    snapshot.entries[self.entrypoint] = self.snapshot(state=self.state(lock="CLOSED")).entries[self.entrypoint]
                self.assert_failure_contains(self.failures(snapshot), expected)

    def test_project_run_closure_fails_closed_on_malformed_or_duplicate_records(self) -> None:
        def mutated(change) -> list[str]:
            snapshot = self.run_closure_snapshot()
            record = json.loads(snapshot.entries[self.run_closure].data)
            change(record)
            snapshot.entries[self.run_closure] = SnapshotEntry(self.run_closure, "100644", json.dumps(record).encode())
            return self.failures(snapshot)

        cases = (
            (lambda record: record.update(schema="other"), "run closure schema is not recognized"),
            (lambda record: record.update(state="OPEN"), "run closure state must be CLOSED or REOPENED"),
            (lambda record: record.update(waiver=True), "invalid terminal closure fields"),
            (lambda record: record.update(completion_commit="HEAD"), "completion_commit must be a full commit ID"),
            (lambda record: record["frozen_sequential_artifacts"].update({"series/other/X.md": "0" * 64}),
             "artifact must be Markdown inside its project"),
        )
        for change, expected in cases:
            with self.subTest(expected=expected):
                self.assert_failure_contains(mutated(change), expected)
        both = self.run_closure_snapshot()
        both.entries[PROJECT_INITIATION_GATE_PATH] = self.terminal_snapshot().entries[PROJECT_INITIATION_GATE_PATH]
        self.assert_failure_contains(self.failures(both), "cannot both be present")
        nonregular = self.run_closure_snapshot()
        entry = nonregular.entries[self.run_closure]
        nonregular.entries[self.run_closure] = SnapshotEntry(entry.path, "120000", entry.data)
        self.assert_failure_contains(self.failures(nonregular), "run closure must be a tracked regular")

    def set_main(self, commit: str | None) -> None:
        if commit is None:
            run_git(self.history_root, "update-ref", "-d", "refs/remotes/origin/main")
        else:
            run_git(self.history_root, "update-ref", "refs/remotes/origin/main", commit)

    def main_with_run_closure(self, record: bytes) -> str:
        """Commit main's registry and run-closure record over the accepted reading, without touching HEAD."""

        registry = self.snapshot().entries["series/registry.json"].data

        with tempfile.TemporaryDirectory() as directory:
            env = dict(os.environ, GIT_INDEX_FILE=str(Path(directory) / "index"))

            def git(*args: str, data: bytes | None = None) -> str:
                return subprocess.run(
                    ["git", "-C", str(self.history_root), *args], input=data, env=env,
                    capture_output=True, check=True,
                ).stdout.decode().strip()

            git("read-tree", self.completion_commit)
            for target, data in ((self.run_closure, record), ("series/registry.json", registry)):
                blob = git("hash-object", "-w", "--stdin", data=data)
                git("update-index", "--add", "--cacheinfo", f"100644,{blob},{target}")
            tree = git("write-tree")
            return git("commit-tree", tree, "-p", self.completion_commit, "-m", "Run stop on main")

    def test_run_closure_completion_commit_must_be_on_main(self) -> None:
        snapshot = self.run_closure_snapshot()
        record = json.loads(snapshot.entries[self.run_closure].data)
        record["completion_commit"] = self.different_commit  # a later, unmerged commit
        snapshot.entries[self.run_closure] = SnapshotEntry(self.run_closure, "100644", json.dumps(record).encode())
        self.assert_failure_contains(self.failures(snapshot), "is not on main")
        try:
            self.set_main(None)
            self.assert_failure_contains(
                self.failures(self.run_closure_snapshot()), "needs refs/remotes/origin/main"
            )
        finally:
            self.set_main(self.completion_commit)

    def test_run_closure_seals_persist_relative_to_main(self) -> None:
        stop = self.run_closure_snapshot()
        digest = json.loads(stop.entries[self.run_closure].data)["frozen_sequential_artifacts"][self.sequential]
        continuity = "was dropped or re-sealed relative to main's run closure"

        def with_releases(snapshot: GitSnapshot, release: dict | None) -> GitSnapshot:
            control = self.control()
            if release is not None:
                control["run_closure_amendments"] = {self.prefix: {
                    "authorization": "Owner approved releasing SOURCE_UNIT_01 (fixture).",
                    "release": release,
                }}
            snapshot.entries[PROJECT_INITIATION_GATE_PATH] = SnapshotEntry(
                PROJECT_INITIATION_GATE_PATH, "100644", json.dumps(control).encode()
            )
            return snapshot

        try:
            self.set_main(self.main_with_run_closure(stop.entries[self.run_closure].data))
            self.assertEqual(self.failures(stop), [])
            self.assertEqual(self.failures(self.run_closure_snapshot("REOPENED")), [])

            deleted = self.run_closure_snapshot()
            del deleted.entries[self.run_closure]
            self.assert_failure_contains(self.failures(deleted), continuity)

            # Rewriting a sealed reading and its seal together is a replacement.
            resealed = self.run_closure_snapshot()
            edited = resealed.entries[self.sequential].data + b"Rewritten.\n"
            resealed.entries[self.sequential] = SnapshotEntry(self.sequential, "100644", edited)
            record = json.loads(resealed.entries[self.run_closure].data)
            record["frozen_sequential_artifacts"][self.sequential] = hashlib.sha256(edited).hexdigest()
            resealed.entries[self.run_closure] = SnapshotEntry(self.run_closure, "100644", json.dumps(record).encode())
            self.assert_failure_contains(self.failures(resealed), continuity)

            # An owner-merged release of the exact sealed digest lets the project
            # leave the run stop; the ordinary OPEN gate then applies in full.
            released = with_releases(self.snapshot(), {self.sequential: digest})
            released.root = self.history_root
            self.assertEqual(self.failures(released), [])
            # A release naming any other digest is spent or wrong and releases nothing.
            stale = with_releases(self.snapshot(), {self.sequential: "0" * 64})
            stale.root = self.history_root
            self.assert_failure_contains(self.failures(stale), continuity)

            # Moving or deregistering the root does not discard main's seals.
            moved = self.run_closure_snapshot()
            registry = json.loads(moved.entries["series/registry.json"].data)
            registry["series"][0]["repository_path"] = "series/example-moved/"
            moved.entries["series/registry.json"] = SnapshotEntry(
                "series/registry.json", "100644", json.dumps(registry).encode()
            )
            self.assert_failure_contains(self.failures(moved), "its root is no longer registered")

            # Converting to a terminal closure keeps the seals and removes the record.
            terminal = self.terminal_snapshot()
            self.assertFalse(any(continuity in failure for failure in self.failures(terminal)))
        finally:
            self.set_main(self.completion_commit)

    def test_run_closure_needs_main_and_cannot_seal_a_nested_root(self) -> None:
        unlinked = self.run_closure_snapshot()
        del unlinked.entries[self.run_closure]
        try:
            self.set_main(None)
            self.assert_failure_contains(
                self.failures(unlinked), "needs refs/remotes/origin/main to check run-stop continuity"
            )
        finally:
            self.set_main(self.completion_commit)

        nested_root = self.prefix + "Nested Project/"
        nested_reading = nested_root + "SOURCE_UNIT_N.md"
        snapshot = self.run_closure_snapshot()
        data = authority_markdown("volume_deep_reading", "Nested")
        snapshot.entries[nested_reading] = SnapshotEntry(nested_reading, "100644", data)
        registry = json.loads(snapshot.entries["series/registry.json"].data)
        registry["series"].append({
            "series_id": "nested", "stable_slug": "nested", "canonical_title": "Nested",
            "repository_path": nested_root, "canonical_entrypoint": None,
            "canonical_entrypoint_status": "MISSING",
        })
        snapshot.entries["series/registry.json"] = SnapshotEntry(
            "series/registry.json", "100644", json.dumps(registry).encode()
        )
        failures = self.failures(snapshot)
        # The parent's seal set excludes the nested root's readings ...
        self.assertFalse(any("terminal sequential corpus differs" in failure for failure in failures), failures)
        # ... and the parent's record may not seal them.
        record = json.loads(snapshot.entries[self.run_closure].data)
        record["frozen_sequential_artifacts"][nested_reading] = hashlib.sha256(data).hexdigest()
        snapshot.entries[self.run_closure] = SnapshotEntry(self.run_closure, "100644", json.dumps(record).encode())
        self.assert_failure_contains(
            self.failures(snapshot), f"which belongs to the nested registered root {nested_root}"
        )

    def test_run_closure_amendments_and_orphans_fail_closed(self) -> None:
        cases = (
            ([], "run_closure_amendments must be an object"),
            ({"../x/": {"authorization": "x", "release": {"x.md": "0" * 64}}}, "invalid project root"),
            ({self.prefix: {"authorization": "", "release": {self.sequential: "0" * 64}}},
             "needs a nonempty authorization and a nonempty release object"),
            ({self.prefix: {"authorization": "x", "release": {}}},
             "needs a nonempty authorization and a nonempty release object"),
            ({self.prefix: {"authorization": "x", "seals": {self.sequential: None}}},
             "needs a nonempty authorization and a nonempty release object"),
            ({self.prefix: {"authorization": "x", "release": {"series/other/X.md": "0" * 64}}},
             "released path must be Markdown inside its project"),
            ({self.prefix: {"authorization": "x", "release": {self.sequential: None}}},
             "release must name the sealed SHA-256"),
        )
        for amendments, expected in cases:
            with self.subTest(expected=expected):
                control = self.control()
                control["run_closure_amendments"] = amendments
                snapshot = self.snapshot()
                snapshot.entries[PROJECT_INITIATION_GATE_PATH] = SnapshotEntry(
                    PROJECT_INITIATION_GATE_PATH, "100644", json.dumps(control).encode()
                )
                self.assert_failure_contains(self.failures(snapshot), expected)
        orphan = "series/unregistered/.repository/run-closure.json"
        snapshot = self.snapshot()
        snapshot.entries[orphan] = SnapshotEntry(orphan, "100644", b"{}\n")
        self.assert_failure_contains(self.failures(snapshot), "project run closure has no registered project")

    def test_current_repository_examples_remain_compatible(self) -> None:
        snapshot = worktree_snapshot(ROOT, worktree_paths(ROOT))
        snapshot = GitSnapshot(
            ROOT,
            "IN_MEMORY_CURRENT_REPOSITORY",
            {
                path: SnapshotEntry(entry.path, entry.mode, entry.data, tracked=True)
                for path, entry in snapshot.entries.items()
            },
        )
        # A source checkout may legitimately await housekeeping. Normalize only
        # routing in this disposable fixture, as fixture_baseline does in the
        # analytical-preflight tests; never rewrite authored evidence or disk.
        source = snapshot
        for path in sorted(source.entries):
            match = re.fullmatch(
                r"((series|studies)/[a-z0-9][a-z0-9-]*)/\.repository/(series|study)-registry\.json",
                path,
            )
            if match and match[3] == ("series" if match[2] == "series" else "study"):
                snapshot, _ = routing_preflight(snapshot, match[1])
        for path, entry in source.entries.items():
            if path not in ROUTING_OUTPUTS:
                self.assertEqual(snapshot.entries[path], entry, path)
        registry = json.loads(snapshot.entries["series/registry.json"].data)
        ids = {row["series_id"] for row in registry["series"]}
        self.assertTrue(
            {"ascendance-of-a-bookworm", "kimishinu", "lycoris-recoil"} <= ids
        )
        control, control_errors = _load_project_initiation_gate(snapshot)
        self.assertEqual(control_errors, [])
        assert control is not None
        # Existing reviewed terminal closures must remain valid under this gate.
        self.assertIn("series/ntr-netsuzou-trap/", control.get("terminal_closures", {}))
        failures = validate_project_initiation_gate(
            snapshot, project_initiation_baseline_paths(ROOT, control), control
        )
        self.assertEqual(failures, [])


if __name__ == "__main__":
    unittest.main()
