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
from character_index_core import AuthorityGraph, GitSnapshot, SnapshotEntry, run_git  # noqa: E402
from completed_run_publication import PROOF_NAME, build_proof, object_id  # noqa: E402
from validate_repository import (  # noqa: E402
    PROJECT_INITIATION_GATE_PATH,
    _is_substantive_sequential_artifact,
    _load_project_initiation_gate,
    _validate_legacy_architecture_route,
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
            "activation_baseline_commit": "2eec12ae1200d3aaaff3f754fd535808161226f8",
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
        if (include_sequential and state != ""
                and (marker or str(migration_scope).startswith("GIT_NATIVE_POST_CUTOVER_"))
                and "sequential_execution:" not in (state or "")
                and (state is None or "sequential_analysis_lock: OPEN" in state)):
            entry = entries[self.entrypoint]
            run = ("\n```yaml\nproject_initialization:\n  next_permitted_operation: V01\n"
                   "sequential_execution:\n  mode: single_operation\n  authorized_start: V01\n"
                   "  terminal_boundary: V01\n  next_candidate_operation: V01\n  run_state: active\n```\n")
            entries[self.entrypoint] = SnapshotEntry(entry.path, entry.mode, entry.data + run.encode())
        # Synthetic projects read their own main, not the live checkout's
        # later publication grants for unrelated registered projects.
        return GitSnapshot(self.history_root, "IN_MEMORY_PROJECT_GATE", entries)

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
                snapshot.root = self.history_root
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
        # Separately preserve the exact reading already accepted on main.
        snapshot.entries[self.sequential] = original
        snapshot.root = self.history_root
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
        # NTR's prospective checkpoints and supplemental postread freeze have
        # different responsibilities from a source-unit deep reading. Their
        # historical preservation is not permission to relabel them as one.
        for kind, sequential in (("reconstruction_checkpoint", False),
                                 ("supplemental_postread_freeze", False),
                                 ("supplemental_deep_reading", True)):
            path = self.prefix + "01 Sequential Readings/HISTORICAL.md"
            entry = SnapshotEntry(path, "100644", authority_markdown(kind))
            self.assertEqual(_is_substantive_sequential_artifact(
                path, entry, self.control()["sequential_artifact_classification"]
            ), (sequential, False, []))

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

    def test_terminal_independent_execution_fences_cannot_hide_conflicts(self) -> None:
        for block in ("sequential_execution:\n  run_state: active\n",
                      "sequential_execution: [\n",
                      "supplemental_execution:\n  current_state: OPEN\n"):
            with self.subTest(block=block):
                snapshot = self.terminal_snapshot()
                entry = snapshot.entries[self.entrypoint]
                snapshot.entries[entry.path] = SnapshotEntry(
                    entry.path, entry.mode, entry.data + ("\n```yaml\n" + block + "```\n").encode()
                )
                self.assertTrue(self.failures(snapshot))

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

    def main_with_run_closure(self, record: bytes, control: dict | None = None) -> str:
        """Commit main's registry, gate control and run-closure record over the accepted reading.

        HEAD and the worktree are untouched; the commit only becomes main.
        """

        registry = self.snapshot().entries["series/registry.json"].data
        control_bytes = json.dumps(control if control is not None else self.control()).encode()

        with tempfile.TemporaryDirectory() as directory:
            env = dict(os.environ, GIT_INDEX_FILE=str(Path(directory) / "index"))

            def git(*args: str, data: bytes | None = None) -> str:
                return subprocess.run(
                    ["git", "-C", str(self.history_root), *args], input=data, env=env,
                    capture_output=True, check=True,
                ).stdout.decode().strip()

            git("read-tree", self.completion_commit)
            for target, data in (
                (self.run_closure, record),
                ("series/registry.json", registry),
                (PROJECT_INITIATION_GATE_PATH, control_bytes),
            ):
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
        record_bytes = stop.entries[self.run_closure].data
        digest = json.loads(record_bytes)["frozen_sequential_artifacts"][self.sequential]
        continuity = "was dropped or re-sealed relative to main's run closure"

        def control_with_release(record_sha256: str, release_digest: str) -> dict:
            control = self.control()
            control["run_closure_amendments"] = {self.prefix: {
                "authorization": "Owner approved releasing SOURCE_UNIT_01 (fixture).",
                "record_sha256": record_sha256,
                "release": {self.sequential: release_digest},
            }}
            return control

        def leave_run_stop() -> GitSnapshot:
            snapshot = self.snapshot()  # ordinary OPEN gate, no run-closure record
            snapshot.root = self.history_root
            return snapshot

        record_sha256 = hashlib.sha256(record_bytes).hexdigest()
        try:
            self.set_main(self.main_with_run_closure(record_bytes))
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

            # A release in the candidate's own control does not count.
            self_granted = leave_run_stop()
            self_granted.entries[PROJECT_INITIATION_GATE_PATH] = SnapshotEntry(
                PROJECT_INITIATION_GATE_PATH, "100644",
                json.dumps(control_with_release(record_sha256, digest)).encode(),
            )
            self.assert_failure_contains(self.failures(self_granted), continuity)

            # A release already on main, bound to main's exact record and seal,
            # lets the project leave its run stop under the ordinary OPEN gate.
            self.set_main(self.main_with_run_closure(record_bytes, control_with_release(record_sha256, digest)))
            self.assertEqual(self.failures(leave_run_stop()), [])
            # Bound to another record, or naming another digest, it releases nothing.
            for bound, named in (("0" * 64, digest), (record_sha256, "0" * 64)):
                with self.subTest(bound=bound[:8], named=named[:8]):
                    self.set_main(self.main_with_run_closure(record_bytes, control_with_release(bound, named)))
                    self.assert_failure_contains(self.failures(leave_run_stop()), continuity)
            self.set_main(self.main_with_run_closure(record_bytes))

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

    def test_run_closure_needs_main_and_covers_nested_roots(self) -> None:
        unlinked = self.run_closure_snapshot()
        del unlinked.entries[self.run_closure]
        try:
            self.set_main(None)
            self.assert_failure_contains(
                self.failures(unlinked), "needs refs/remotes/origin/main to check run-stop continuity"
            )
        finally:
            self.set_main(self.completion_commit)

        # A closed parent covers readings under a nested registered root, even a
        # legacy one whose own gate is not strict: a new nested reading is an
        # addition to the parent's sealed corpus.
        nested_root = self.prefix + "Nested Project/"
        nested_reading = nested_root + "SOURCE_UNIT_N.md"
        snapshot = self.run_closure_snapshot()
        registry = json.loads(snapshot.entries["series/registry.json"].data)
        registry["series"].append({
            "series_id": "nested", "stable_slug": "nested", "canonical_title": "Nested",
            "repository_path": nested_root, "canonical_entrypoint": None,
            "canonical_entrypoint_status": "MISSING",
        })
        snapshot.entries["series/registry.json"] = SnapshotEntry(
            "series/registry.json", "100644", json.dumps(registry).encode()
        )
        baseline = set(snapshot.entries) | {nested_root + "LEGACY_NOTES.md"}
        snapshot.entries[nested_reading] = SnapshotEntry(
            nested_reading, "100644", authority_markdown("volume_deep_reading", "Nested")
        )
        self.assert_failure_contains(
            self.failures(snapshot, baseline), "terminal sequential corpus differs from reviewed closure"
        )

    def test_run_closure_amendments_and_orphans_fail_closed(self) -> None:
        cases = (
            ([], "run_closure_amendments must be an object"),
            ({"../x/": {"authorization": "x", "record_sha256": "0" * 64, "release": {"x.md": "0" * 64}}},
             "invalid project root"),
            ({self.prefix: {"authorization": "", "record_sha256": "0" * 64, "release": {self.sequential: "0" * 64}}},
             "needs a nonempty authorization, the record_sha256"),
            ({self.prefix: {"authorization": "x", "record_sha256": "0" * 64, "release": {}}},
             "needs a nonempty authorization, the record_sha256"),
            ({self.prefix: {"authorization": "x", "release": {self.sequential: "0" * 64}}},
             "needs a nonempty authorization, the record_sha256"),
            ({self.prefix: {"authorization": "x", "record_sha256": "HEAD", "release": {self.sequential: "0" * 64}}},
             "needs a nonempty authorization, the record_sha256"),
            ({self.prefix: {"authorization": "x", "record_sha256": "0" * 64, "release": {"series/other/X.md": "0" * 64}}},
             "released path must be Markdown inside its project"),
            ({self.prefix: {"authorization": "x", "record_sha256": "0" * 64, "release": {self.sequential: None}}},
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


class RunAdmissionTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp = tempfile.TemporaryDirectory(prefix="run-admission-")
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        run_git(self.root, "init", "--quiet")
        run_git(self.root, "config", "user.name", "Run fixture")
        run_git(self.root, "config", "user.email", "run@example.invalid")
        self.fixture = ProjectInitiationGateTests()
        self.fixture.history_root = self.root
        self.main = None
        self.publish(self.candidate())

    def candidate(self, run="completed", *, new=False, lock="OPEN") -> GitSnapshot:
        f = self.fixture
        snapshot = f.snapshot()
        snapshot.root = self.root
        operation = "V02" if run == "active" else "NONE_RUN_COMPLETE"
        body = f.state(lock=lock) + (
            "\n```yaml\nproject_initialization:\n"
            f"  next_permitted_operation: {operation}\n"
            "sequential_execution:\n  mode: continuous_sequential\n"
            "  authorized_start: V01\n  terminal_boundary: V02\n"
            f"  committed_high_water_mark: {'V01' if run == 'active' else 'V02'}\n"
            f"  next_candidate_operation: {operation}\n  run_state: {run}\n```\n"
        )
        snapshot.entries[f.entrypoint] = SnapshotEntry(f.entrypoint, "100644", authority_markdown("corpus_map", body))
        if new:
            path = f.prefix + "SOURCE_UNIT_02.md"
            snapshot.entries[path] = SnapshotEntry(path, "100644", authority_markdown("deep_reading", "New unit"))
        return snapshot

    def publish(self, snapshot):
        run_git(self.root, "read-tree", "--empty")
        for path, entry in snapshot.entries.items():
            oid = run_git(self.root, "hash-object", "-w", "--stdin", input_bytes=entry.data).decode().strip()
            run_git(self.root, "update-index", "--add", "--cacheinfo", f"{entry.mode},{oid},{path}")
        tree = run_git(self.root, "write-tree").decode().strip()
        parents = ["-p", self.main] if self.main else []
        self.main = run_git(self.root, "commit-tree", tree, *parents, input_bytes=b"Fixture transaction\n").decode().strip()
        run_git(self.root, "update-ref", "refs/remotes/origin/main", self.main)
        return self.main

    def failures(self, snapshot, baseline=None):
        return validate_project_initiation_gate(snapshot, baseline or set())

    def relocate_entrypoint(self, prior, *, data=None):
        candidate = GitSnapshot(self.root, "RELOCATED_LEGACY_RUN", dict(prior.entries))
        relocated = self.fixture.prefix + "MOVED_CURRENT_STATE.md"
        candidate.entries.pop(self.fixture.entrypoint, None)
        candidate.entries[relocated] = SnapshotEntry(
            relocated, "100644", data if data is not None else
            authority_markdown("corpus_map", self.fixture.state())
        )
        registry_path = "series/registry.json"
        registry = json.loads(candidate.entries[registry_path].data)
        registry["series"][0]["canonical_entrypoint"] = relocated
        candidate.entries[registry_path] = SnapshotEntry(
            registry_path, "100644", (json.dumps(registry) + "\n").encode()
        )
        reading = self.fixture.prefix + "SOURCE_UNIT_02.md"
        candidate.entries[reading] = SnapshotEntry(reading, "100644", authority_markdown("deep_reading"))
        return candidate, relocated

    def test_completed_open_run_preserves_readings_but_rejects_new_admission(self):
        self.assertEqual(self.failures(self.candidate()), [])
        self.assertTrue(any("active authorized run" in e for e in self.failures(self.candidate(new=True))))

    def frozen_publication(self, *, authorize=True):
        from frozen_publication import FIELD

        f = self.fixture
        candidate = self.candidate()
        scope = f.prefix + "G2/"
        reading = scope + "READING.md"
        boundary = scope + "SOURCE_BOUNDARY.json"
        manifest = scope + "PUBLICATION_MANIFEST.json"
        notice = scope + "PUBLICATION_README.md"
        body = authority_markdown("deep_reading", "Completed independent reading").replace(
            b"status: canonical", b"generation: G2\nstatus: draft_noncurrent"
        ).replace(b"do_not_use_as_current_authority: false", b"do_not_use_as_current_authority: true")
        source = b'{"units":["V01"],"admission":"CLOSED"}\n'
        notice_body = body.replace(b"artifact_type: deep_reading", b"artifact_type: publication_notice")
        digest = lambda data: hashlib.sha256(data).hexdigest()
        artifacts = []
        for path, data in ((reading, body), (boundary, source)):
            artifacts.append({
                "path": path, "original_commit": "a" * 40, "original_blob": "b" * 40,
                "original_bytes": len(data), "original_sha256": digest(data),
                "publication_bytes": len(data), "publication_sha256": digest(data),
                "transformation": "byte-identical",
            })
        payload = {
            "schema": "fixture-publication/1", "generation": "G2", "status": "draft_noncurrent",
            "supersedes": [], "superseded_by": [], "do_not_use_as_current_authority": True,
            "independent_frozen_commit": "a" * 40, "independent_frozen_corpus_tree": "c" * 40,
            "original_comparison_commit": "d" * 40, "comparison_V1_boundary_commit": "e" * 40,
            "unchanged_source_boundary_sha256": digest(source), "artifacts": artifacts,
        }
        manifest_bytes = (json.dumps(payload) + "\n").encode()
        grant = {
            "project_root": f.prefix, "canonical_entrypoint": f.entrypoint,
            "scope_prefixes": [scope], "manifest_schema": payload["schema"],
            "manifest_sha256": digest(manifest_bytes), "frozen_commit": "a" * 40,
            "frozen_corpus_tree": "c" * 40, "comparison_commit": "d" * 40,
            "comparison_v1_boundary": "e" * 40, "source_boundary": boundary,
            "source_boundary_sha256": digest(source), "generations": ["G2"],
            "provenance_files": {notice: digest(notice_body)},
            "authorization": "Owner-reviewed exact independent frozen publication; no narrative admission",
        }
        control = self.fixture.control()
        control[FIELD] = {manifest: grant}
        candidate.entries[PROJECT_INITIATION_GATE_PATH] = SnapshotEntry(
            PROJECT_INITIATION_GATE_PATH, "100644", (json.dumps(control) + "\n").encode()
        )
        if authorize:
            self.publish(candidate)  # Owner merges governance before the import.
        for path, data in ((reading, body), (boundary, source), (notice, notice_body), (manifest, manifest_bytes)):
            candidate.entries[path] = SnapshotEntry(path, "100644", data)
        return candidate, {"reading": reading, "boundary": boundary, "manifest": manifest, "notice": notice}

    def test_reviewed_frozen_publication_accepts_complete_noncurrent_import_and_squash_audit(self):
        candidate, paths = self.frozen_publication()
        original_v1 = self.candidate().entries[self.fixture.sequential].data
        self.assertEqual(self.failures(candidate), [])
        head = self.publish(candidate)
        # Original analytical commits are intentionally not objects in this repository.
        self.assertNotEqual(subprocess.run(
            ["git", "-C", str(self.root), "cat-file", "-e", "a" * 40],
            stdout=subprocess.PIPE, stderr=subprocess.PIPE,
        ).returncode, 0)
        integrated = GitSnapshot.from_commit(self.root, head)
        self.assertEqual(self.failures(integrated), [])
        self.assertEqual(integrated.entries[self.fixture.sequential].data, original_v1)
        self.assertIn(paths["reading"], integrated.entries)

    def test_frozen_publication_cannot_authorize_itself_or_use_draft_as_bypass(self):
        candidate, paths = self.frozen_publication(authorize=False)
        self.assertTrue(any("active authorized run" in e for e in self.failures(candidate)))
        candidate.entries.pop(paths["manifest"])
        self.assertTrue(self.failures(candidate))

    def test_frozen_publication_rejects_changed_missing_retyped_and_nonregular_files(self):
        candidate, paths = self.frozen_publication()
        for name in paths:
            for mutation in ("change", "remove", "symlink"):
                with self.subTest(name=name, mutation=mutation):
                    changed = GitSnapshot(self.root, "MUTATED_PUBLICATION", dict(candidate.entries))
                    entry = changed.entries[paths[name]]
                    if mutation == "remove":
                        del changed.entries[entry.path]
                    else:
                        changed.entries[entry.path] = SnapshotEntry(
                            entry.path, "120000" if mutation == "symlink" else entry.mode,
                            entry.data if mutation == "symlink" else entry.data + b"Changed\n",
                        )
                    self.assertTrue(self.failures(changed))
        changed = GitSnapshot(self.root, "RETYPED_PUBLICATION", dict(candidate.entries))
        entry = changed.entries[paths["reading"]]
        changed.entries[entry.path] = SnapshotEntry(entry.path, entry.mode, entry.data.replace(b"deep_reading", b"claim_revision"))
        self.assertTrue(self.failures(changed))

    def test_frozen_publication_rejects_added_readings_inside_and_outside_envelope(self):
        candidate, _ = self.frozen_publication()
        for path in (self.fixture.prefix + "G2/UNREVIEWED.md", self.fixture.prefix + "UNREVIEWED.md"):
            with self.subTest(path=path):
                changed = GitSnapshot(self.root, "EXTRA_READING", dict(candidate.entries))
                changed.entries[path] = SnapshotEntry(path, "100644", authority_markdown("deep_reading"))
                self.assertTrue(self.failures(changed))

    def test_frozen_publication_rejects_changed_manifest_source_identity_or_authority(self):
        candidate, paths = self.frozen_publication()
        for before, after in ((b"draft_noncurrent", b"canonical"),
                              (("a" * 40).encode(), ("f" * 40).encode()),
                              (b'"units":["V01"]', b'"units":["V02"]')):
            with self.subTest(after=after):
                changed = GitSnapshot(self.root, "CHANGED_BOUNDARY", dict(candidate.entries))
                for name in ("manifest", "boundary", "reading"):
                    entry = changed.entries[paths[name]]
                    changed.entries[entry.path] = SnapshotEntry(entry.path, entry.mode, entry.data.replace(before, after))
                self.assertTrue(self.failures(changed))

    def test_frozen_publication_preserves_architecture_and_published_grant(self):
        from frozen_publication import FIELD

        candidate, _ = self.frozen_publication()
        changed = GitSnapshot(self.root, "MISSING_ARCHITECTURE", dict(candidate.entries))
        del changed.entries[self.fixture.architecture]
        self.assertTrue(self.failures(changed))
        for stage in ("initial_import", "already_published"):
            with self.subTest(stage=stage):
                if stage == "already_published":
                    self.publish(candidate)
                changed = GitSnapshot(self.root, "REMOVED_GRANT", dict(candidate.entries))
                control = json.loads(changed.entries[PROJECT_INITIATION_GATE_PATH].data)
                control.pop(FIELD)
                changed.entries[PROJECT_INITIATION_GATE_PATH] = SnapshotEntry(
                    PROJECT_INITIATION_GATE_PATH, "100644", (json.dumps(control) + "\n").encode()
                )
                self.assertTrue(any("cannot be removed or rewritten" in e for e in self.failures(changed)))

    def test_frozen_publication_rejects_promoted_bytes_even_with_matching_reviewed_hashes(self):
        from frozen_publication import FIELD

        candidate, paths = self.frozen_publication(authorize=False)
        entry = candidate.entries[paths["reading"]]
        promoted = entry.data.replace(b"status: draft_noncurrent", b"status: canonical")
        candidate.entries[entry.path] = SnapshotEntry(entry.path, entry.mode, promoted)
        payload = json.loads(candidate.entries[paths["manifest"]].data)
        artifact = next(a for a in payload["artifacts"] if a["path"] == entry.path)
        artifact["publication_bytes"] = len(promoted)
        artifact["publication_sha256"] = hashlib.sha256(promoted).hexdigest()
        manifest = (json.dumps(payload) + "\n").encode()
        candidate.entries[paths["manifest"]] = SnapshotEntry(paths["manifest"], "100644", manifest)
        control = json.loads(candidate.entries[PROJECT_INITIATION_GATE_PATH].data)
        control[FIELD][paths["manifest"]]["manifest_sha256"] = hashlib.sha256(manifest).hexdigest()
        candidate.entries[PROJECT_INITIATION_GATE_PATH] = SnapshotEntry(
            PROJECT_INITIATION_GATE_PATH, "100644", (json.dumps(control) + "\n").encode()
        )
        governance = GitSnapshot(self.root, "REVIEWED_PROMOTION_ATTEMPT", dict(candidate.entries))
        for path in paths.values():
            del governance.entries[path]
        self.publish(governance)
        self.assertTrue(any("must remain noncurrent" in e for e in self.failures(candidate)))

    def test_active_bounded_run_can_admit_and_post_merge_check_agrees(self):
        candidate = self.candidate("active", new=True)
        self.assertEqual(self.failures(candidate), [])
        head = self.publish(candidate)
        self.assertEqual(self.failures(GitSnapshot.from_commit(self.root, head)), [])

    def test_final_transaction_can_complete_existing_active_run_without_retroactive_failure(self):
        self.publish(self.candidate("active"))
        candidate = self.candidate(new=True)
        self.assertEqual(self.failures(candidate), [])
        head = self.publish(candidate)
        self.assertEqual(self.failures(GitSnapshot.from_commit(self.root, head)), [])
        self.assertEqual(self.failures(self.candidate(new=True)), [])

    def test_completed_state_cannot_launder_admission_in_post_merge_audit(self):
        head = self.publish(self.candidate(new=True))
        errors = self.failures(GitSnapshot.from_commit(self.root, head))
        self.assertTrue(any("active authorized run" in e for e in errors), errors)

    def test_final_transaction_rejects_prior_prose_closed_lock(self):
        prior = self.candidate("active")
        entry = prior.entries[self.fixture.entrypoint]
        prior.entries[entry.path] = SnapshotEntry(
            entry.path, entry.mode, entry.data + b"\nSEQUENTIAL_ANALYSIS_LOCK = CLOSED\n"
        )
        self.publish(prior)
        candidate = self.candidate(new=True)
        errors = self.failures(candidate)
        self.assertTrue(any("active authorized run" in error for error in errors), errors)
        head = self.publish(candidate)
        errors = self.failures(GitSnapshot.from_commit(self.root, head))
        self.assertTrue(any("active authorized run" in error for error in errors), errors)

    def test_inconsistent_missing_and_ambiguous_run_fields_fail_closed(self):
        changes = (
            (b"run_state: active", b"run_state: completed"),
            (b"sequential_analysis_lock: OPEN", b"sequential_analysis_lock: CLOSED"),
            (b"next_permitted_operation: V02", b"next_permitted_operation: V03"),
            (b"next_candidate_operation: V02", b"next_candidate_operation: NONE"),
            (b"  run_state: active\n", b""),
            (b"run_state: active", b"run_state: {bad: value}"),
            (b"mode: continuous_sequential", b"mode: []"),
            (b"  terminal_boundary: V02\n", b""),
            (b"mode: continuous_sequential", b"mode: single_operation"),
            (b"mode: continuous_sequential\n  authorized_start: V01\n  terminal_boundary: V02", b"mode: single_operation\n  authorized_start: V01\n  terminal_boundary: V01"),
            (b"sequential_execution:\n", b"sequential_execution: null\nignored:\n"),
        )
        for old, new in changes:
            with self.subTest(old=old, new=new):
                candidate = self.candidate("active", new=True)
                entry = candidate.entries[self.fixture.entrypoint]
                candidate.entries[entry.path] = SnapshotEntry(entry.path, entry.mode, entry.data.replace(old, new))
                self.assertTrue(self.failures(candidate))
        candidate = self.candidate("active", new=True)
        entry = candidate.entries[self.fixture.entrypoint]
        extra = b"\n```yaml\nsequential_execution:\n  run_state: completed\n```\n"
        candidate.entries[entry.path] = SnapshotEntry(entry.path, entry.mode, entry.data + extra)
        self.assertTrue(any("contradictory execution" in e for e in self.failures(candidate)))

    def test_completion_transition_cannot_expand_recorded_bounds(self):
        self.publish(self.candidate("active"))
        candidate = self.candidate(new=True)
        entry = candidate.entries[self.fixture.entrypoint]
        candidate.entries[entry.path] = SnapshotEntry(entry.path, entry.mode, entry.data.replace(b"V02", b"V03"))
        self.assertTrue(any("active authorized run" in e for e in self.failures(candidate)))
        for old, new in ((b"mode: continuous_sequential", b"mode: single_operation"),
                         (b"authorized_start: V01", b"authorized_start: NONE")):
            with self.subTest(invalid_prior=new):
                prior = self.candidate("active")
                entry = prior.entries[self.fixture.entrypoint]
                prior.entries[entry.path] = SnapshotEntry(entry.path, entry.mode, entry.data.replace(old, new))
                self.publish(prior)
                candidate = self.candidate(new=True)
                entry = candidate.entries[self.fixture.entrypoint]
                candidate.entries[entry.path] = SnapshotEntry(entry.path, entry.mode, entry.data.replace(old, new))
                self.assertTrue(any("active authorized run" in e for e in self.failures(candidate)))

    def test_retrospective_correction_preserves_accepted_legacy_state(self):
        candidate = self.candidate()
        entry = candidate.entries[self.fixture.entrypoint]
        # An existing inconsistent state is not a license to admit; nor does
        # it force a corpus sweep before unrelated, evidence-backed correction.
        legacy = entry.data.replace(b"run_state: completed", b"run_state: active")
        candidate.entries[entry.path] = SnapshotEntry(entry.path, entry.mode, legacy)
        self.publish(candidate)
        candidate.entries[entry.path] = SnapshotEntry(entry.path, entry.mode, legacy + b"\nRetrospective correction route.\n")
        correction = self.fixture.prefix + "ERRATUM.md"
        candidate.entries[correction] = SnapshotEntry(correction, "100644", authority_markdown("claim_revision", "Evidence-backed correction"))
        self.assertEqual(self.failures(candidate), [])
        extra = self.fixture.prefix + "SOURCE_UNIT_02.md"
        candidate.entries[extra] = SnapshotEntry(extra, "100644", authority_markdown("deep_reading"))
        self.assertTrue(self.failures(candidate))

    def test_legacy_route_does_not_hide_partial_or_malformed_run_declarations(self):
        prior = self.fixture.snapshot(marker=False, migration_scope="IMPORTED_REVIEWED")
        prior.root = self.root
        self.publish(prior)
        baseline = set(prior.entries)
        for new_reading in (False, True):
            candidate = GitSnapshot(self.root, "LEGACY_RUN", dict(prior.entries))
            if new_reading:
                path = self.fixture.prefix + "SOURCE_UNIT_02.md"
                candidate.entries[path] = SnapshotEntry(path, "100644", authority_markdown("deep_reading"))
            self.assertEqual(self.failures(candidate, baseline), [])
            entry = prior.entries[self.fixture.entrypoint]
            for declaration in ("sequential_execution: {}", "sequential_execution: null",
                                "sequential_execution: [", "sequential_execution:\n  mode: single_operation"):
                with self.subTest(new_reading=new_reading, declaration=declaration):
                    candidate.entries[entry.path] = SnapshotEntry(
                        entry.path, entry.mode, entry.data + ("\n```yaml\n" + declaration + "\n```\n").encode()
                    )
                    self.assertTrue(self.failures(candidate, baseline))

        # Legacy absence never overrides an explicit stop or malformed lock.
        candidate = GitSnapshot(self.root, "LEGACY_STOP", dict(prior.entries))
        path = self.fixture.prefix + "SOURCE_UNIT_02.md"
        candidate.entries[path] = SnapshotEntry(path, "100644", authority_markdown("deep_reading"))
        for data in (
            *(entry.data.replace(b"sequential_analysis_lock: OPEN", b"sequential_analysis_lock: " + value)
              for value in (b"CLOSED", b"null", b"[]", b"UNKNOWN")),
            entry.data + b"\nSEQUENTIAL_ANALYSIS_LOCK = CLOSED\n",
            entry.data + b"\n```yaml\nproject_initialization:\n  next_permitted_operation: NONE\n```\n",
        ):
            with self.subTest(legacy_stop=data):
                candidate.entries[entry.path] = SnapshotEntry(entry.path, entry.mode, data)
                self.assertTrue(self.failures(candidate, baseline))

    def test_existing_path_retyping_or_replacement_does_not_hide_admission(self):
        for original_type in ("claim_revision", "deep_reading"):
            with self.subTest(original_type=original_type):
                base = self.candidate()
                path = self.fixture.prefix + "OLD.md"
                base.entries[path] = SnapshotEntry(path, "100644", authority_markdown(original_type, "Old"))
                self.publish(base)
                base.entries[path] = SnapshotEntry(path, "100644", authority_markdown("deep_reading", "New unit"))
                self.assertTrue(self.failures(base, set(base.entries)))

    def test_entrypoint_relocation_cannot_drop_completed_run_state(self):
        prior = self.fixture.snapshot(marker=False, migration_scope="IMPORTED_REVIEWED")
        prior.root = self.root
        prior.entries[self.fixture.entrypoint] = self.candidate().entries[self.fixture.entrypoint]
        self.publish(prior)
        candidate, relocated = self.relocate_entrypoint(prior)
        self.assertEqual(_validate_legacy_architecture_route(
            candidate, AuthorityGraph(candidate), self.fixture.prefix, relocated
        ), [])
        for identity in ("example", "renamed-example"):
            with self.subTest(identity=identity):
                registry_path = "series/registry.json"
                registry = json.loads(candidate.entries[registry_path].data)
                registry["series"][0]["series_id"] = identity
                candidate.entries[registry_path] = SnapshotEntry(
                    registry_path, "100644", (json.dumps(registry) + "\n").encode()
                )
                failures = self.failures(candidate, set(prior.entries))
                self.assertTrue(any("active authorized run" in error for error in failures), failures)

    def test_legacy_entrypoint_relocation_preserves_absent_run_compatibility(self):
        prior = self.fixture.snapshot(marker=False, migration_scope="IMPORTED_REVIEWED")
        prior.root = self.root
        self.publish(prior)
        candidate, _relocated = self.relocate_entrypoint(prior)
        self.assertEqual(self.failures(candidate, set(prior.entries)), [])
        head = self.publish(candidate)
        self.assertEqual(self.failures(GitSnapshot.from_commit(self.root, head), set(prior.entries)), [])

    def test_entrypoint_relocation_preserves_active_run_completion(self):
        prior = self.fixture.snapshot(marker=False, migration_scope="IMPORTED_REVIEWED")
        prior.root = self.root
        prior.entries[self.fixture.entrypoint] = self.candidate("active").entries[self.fixture.entrypoint]
        self.publish(prior)
        candidate, _relocated = self.relocate_entrypoint(
            prior, data=self.candidate().entries[self.fixture.entrypoint].data
        )
        self.assertEqual(self.failures(candidate, set(prior.entries)), [])
        head = self.publish(candidate)
        self.assertEqual(self.failures(GitSnapshot.from_commit(self.root, head), set(prior.entries)), [])

    def test_entrypoint_relocation_fails_closed_when_prior_state_is_unavailable(self):
        prior = self.fixture.snapshot(marker=False, migration_scope="IMPORTED_REVIEWED")
        prior.root = self.root
        del prior.entries[self.fixture.entrypoint]
        self.publish(prior)
        candidate, _relocated = self.relocate_entrypoint(prior)
        failures = self.failures(candidate, set(prior.entries))
        self.assertTrue(any("prior canonical entrypoint is unavailable" in error for error in failures), failures)

    def test_entrypoint_relocation_fails_closed_on_ambiguous_prior_identity(self):
        prior = self.fixture.snapshot(marker=False, migration_scope="IMPORTED_REVIEWED")
        prior.root = self.root
        registry_path = "series/registry.json"
        registry = json.loads(prior.entries[registry_path].data)
        registry["series"].append({**registry["series"][0], "series_id": "other",
                                   "repository_path": "series/other/"})
        prior.entries[registry_path] = SnapshotEntry(
            registry_path, "100644", (json.dumps(registry) + "\n").encode()
        )
        self.publish(prior)
        candidate, _relocated = self.relocate_entrypoint(prior)
        registry = json.loads(candidate.entries[registry_path].data)
        registry["series"] = [{**registry["series"][0], "series_id": "other"}]
        candidate.entries[registry_path] = SnapshotEntry(
            registry_path, "100644", (json.dumps(registry) + "\n").encode()
        )
        failures = self.failures(candidate, set(prior.entries))
        self.assertTrue(any("ambiguous prior project routes" in error for error in failures), failures)

    def test_missing_main_and_moved_activation_baseline_fail_closed(self):
        run_git(self.root, "update-ref", "-d", "refs/remotes/origin/main")
        self.assertTrue(any("needs refs/remotes/origin/main" in e for e in self.failures(self.candidate("active", new=True))))
        with self.assertRaisesRegex(Exception, "immutable activation baseline"):
            project_initiation_baseline_paths(self.root, {"activation_baseline_commit": self.main})

    def completed_batch(self, *, active=None, completed=None):
        base = self.main
        self.publish(active or self.candidate("active"))
        candidate = completed or self.candidate(new=True)
        completion = self.publish(candidate)
        self.main = base
        run_git(self.root, "update-ref", "refs/remotes/origin/main", base)
        self.bind_completion(candidate, completion)
        return candidate, completion

    def bind_completion(self, candidate, completion):
        f = self.fixture
        proof = build_proof(candidate, f.prefix, f.entrypoint, completion)
        path = f.prefix + PROOF_NAME
        candidate.entries[path] = SnapshotEntry(path, "100644", (json.dumps(proof) + "\n").encode())

    def test_completed_batch_and_squash_audit_without_source_objects(self):
        candidate, completion = self.completed_batch()
        self.assertEqual(self.failures(candidate), [])
        squash = self.publish(candidate)
        with tempfile.TemporaryDirectory(prefix="squashed-admission-") as directory:
            root = Path(directory)
            run_git(root, "init", "--quiet")
            run_git(root, "fetch", "--quiet", "--no-tags", str(self.root),
                    "refs/remotes/origin/main:refs/remotes/origin/main")
            with self.assertRaises(Exception):
                run_git(root, "cat-file", "-e", completion)
            self.assertEqual(self.failures(GitSnapshot.from_commit(root, squash)), [])
        self.assertEqual(self.failures(GitSnapshot.from_commit(self.root, squash)), [])

    def test_completion_proof_rejects_missing_or_corrupt_historical_objects(self):
        candidate, _ = self.completed_batch()
        path = self.fixture.prefix + PROOF_NAME
        original = candidate.entries[path]
        for mutation in ("commit", "tree", "blob", "tree_hash", "blob_hash",
                         "parent", "route", "schema", "shape"):
            with self.subTest(mutation=mutation):
                record = json.loads(original.data)
                if mutation == "commit":
                    record["commits"][record["active_commit"]] += "tampered"
                elif mutation == "tree":
                    record["trees"].clear()
                elif mutation == "blob":
                    record["blobs"].clear()
                elif mutation == "tree_hash":
                    rows = next(rows for rows in record["trees"].values() if rows)
                    rows[0][2] = "0" * 40
                elif mutation == "blob_hash":
                    oid = next(iter(record["blobs"]))
                    record["blobs"][oid] += "tampered"
                elif mutation == "parent":
                    record["commits"].pop(record["active_commit"])
                    record["active_commit"] = self.main
                    record["commits"][self.main] = run_git(
                        self.root, "cat-file", "commit", self.main).decode()
                elif mutation == "route":
                    record["project_root"] = "series/other/"
                elif mutation == "schema":
                    record["schema"] = "unknown"
                else:
                    record["trees"] = []
                candidate.entries[path] = SnapshotEntry(path, "100644", json.dumps(record).encode())
                self.assertTrue(any("publication proof" in error for error in self.failures(candidate)))

    def test_completion_proof_rejects_added_changed_dropped_and_retyped_readings(self):
        for mutation in ("added", "changed", "dropped", "retyped", "nonregular"):
            with self.subTest(mutation=mutation):
                candidate, completion = self.completed_batch()
                path = self.fixture.sequential
                original = candidate.entries[path]
                if mutation == "added":
                    extra = self.fixture.prefix + "SOURCE_UNIT_03.md"
                    candidate.entries[extra] = SnapshotEntry(extra, "100644", authority_markdown("deep_reading"))
                elif mutation == "dropped":
                    del candidate.entries[path]
                elif mutation == "retyped":
                    candidate.entries[path] = SnapshotEntry(path, "100644", authority_markdown("ledger"))
                elif mutation == "nonregular":
                    candidate.entries[path] = SnapshotEntry(path, "120000", original.data)
                else:
                    candidate.entries[path] = SnapshotEntry(path, "100644", original.data + b"Changed after completion.\n")
                # Regeneration cannot launder a change: the historical blob is
                # supplied, checked, classified, and compared with the candidate.
                self.bind_completion(candidate, completion)
                self.assertTrue(any("publication proof" in error for error in self.failures(candidate)))

    def test_completion_proof_requires_valid_active_parent_and_unchanged_bounds(self):
        for mutation in ("inactive", "closed", "prose_closed", "bounds", "high_water"):
            with self.subTest(mutation=mutation):
                active = self.candidate("active")
                completed = self.candidate(new=True)
                f = self.fixture
                if mutation in {"inactive", "closed", "prose_closed"}:
                    entry = active.entries[f.entrypoint]
                    data = entry.data
                    if mutation == "inactive":
                        data = data.replace(b"run_state: active", b"run_state: blocked")
                    elif mutation == "closed":
                        data = data.replace(b"sequential_analysis_lock: OPEN", b"sequential_analysis_lock: CLOSED")
                    else:
                        data += b"\nSEQUENTIAL_ANALYSIS_LOCK = CLOSED\n"
                    active.entries[entry.path] = SnapshotEntry(entry.path, entry.mode, data)
                else:
                    entry = completed.entries[f.entrypoint]
                    old, new = ((b"terminal_boundary: V02", b"terminal_boundary: V03")
                                if mutation == "bounds" else
                                (b"committed_high_water_mark: V02", b"committed_high_water_mark: V01"))
                    completed.entries[entry.path] = SnapshotEntry(entry.path, entry.mode, entry.data.replace(old, new))
                candidate, _ = self.completed_batch(active=active, completed=completed)
                self.assertTrue(any("active-to-completed" in error for error in self.failures(candidate)))

    def test_completion_proof_cannot_override_current_or_main_active_bounds(self):
        candidate, completion = self.completed_batch()
        entry = candidate.entries[self.fixture.entrypoint]
        candidate.entries[entry.path] = SnapshotEntry(
            entry.path, entry.mode, entry.data.replace(b"terminal_boundary: V02", b"terminal_boundary: V03"))
        self.bind_completion(candidate, completion)
        self.assertTrue(any("operational state disagree" in error for error in self.failures(candidate)))
        candidate.entries[entry.path] = entry
        prior = self.candidate("active")
        original = prior.entries[entry.path]
        prior.entries[entry.path] = SnapshotEntry(
            entry.path, entry.mode, original.data.replace(b"terminal_boundary: V02", b"terminal_boundary: V03"))
        self.publish(prior)
        self.assertTrue(any("active authorized run" in error for error in self.failures(candidate)))

    def test_completion_proof_cannot_replace_blocked_interrupted_or_malformed_main(self):
        candidate, _ = self.completed_batch()
        self.assertEqual(self.failures(candidate), [])
        base = self.main
        stops = (
            (b"run_state: completed", b"run_state: blocked"),
            (b"run_state: completed", b"run_state: interrupted_pending_recovery"),
            (b"run_state: completed", b"run_state: {bad: value}"),
            (b"  run_state: completed\n", b""),
            (b"run_state: completed\n```\n",
             b"run_state: completed\n```\n\n```yaml\nsequential_execution:\n  run_state: active\n```\n"),
            # A completed run that still names a next operation is inconsistent.
            (b"next_candidate_operation: NONE_RUN_COMPLETE", b"next_candidate_operation: V03"),
            (b"next_permitted_operation: NONE_RUN_COMPLETE", b"next_permitted_operation: V03"),
            (b"operation: NONE_RUN_COMPLETE", b"operation: V03"),
        )
        for old, new in stops:
            with self.subTest(main=new):
                self.main = base
                prior = self.candidate()
                entry = prior.entries[self.fixture.entrypoint]
                self.assertIn(old, entry.data)
                prior.entries[entry.path] = SnapshotEntry(entry.path, entry.mode, entry.data.replace(old, new))
                self.publish(prior)
                # A published stop or unreadable main state keeps the ordinary
                # route; a valid proof is never substituted for it, before or
                # after integration.
                errors = self.failures(candidate)
                self.assertTrue(any("active authorized run" in error for error in errors), errors)
                head = self.publish(candidate)
                errors = self.failures(GitSnapshot.from_commit(self.root, head))
                self.assertTrue(any("active authorized run" in error for error in errors), errors)

    def test_stale_completion_proof_does_not_block_main_active_completion(self):
        candidate, _ = self.completed_batch()
        self.publish(candidate)
        f = self.fixture
        proof = candidate.entries[f.prefix + PROOF_NAME]

        def second_run(run, *units):
            snapshot = self.candidate(run)
            entry = snapshot.entries[f.entrypoint]
            data = entry.data
            for old, new in ((b"authorized_start: V01", b"authorized_start: V03"),
                             (b"terminal_boundary: V02", b"terminal_boundary: V04"),
                             (b"committed_high_water_mark: V01", b"committed_high_water_mark: V03"),
                             (b"committed_high_water_mark: V02", b"committed_high_water_mark: V04"),
                             (b"operation: V02", b"operation: V04")):
                data = data.replace(old, new)
            snapshot.entries[entry.path] = SnapshotEntry(entry.path, entry.mode, data)
            for unit in ("02", *units):
                path = f"{f.prefix}SOURCE_UNIT_{unit}.md"
                snapshot.entries[path] = candidate.entries.get(path) or SnapshotEntry(
                    path, "100644", authority_markdown("deep_reading", f"Unit {unit}"))
            snapshot.entries[proof.path] = proof
            return snapshot

        # The earlier run's proof stays tracked while a later run is published
        # active on main and then completed through the ordinary route.
        active = second_run("active", "03")
        self.assertEqual(self.failures(active), [])
        self.publish(active)
        completed = second_run("completed", "03", "04")
        self.assertEqual(self.failures(completed), [])
        head = self.publish(completed)
        self.assertEqual(self.failures(GitSnapshot.from_commit(self.root, head)), [])

    def test_completion_proof_reads_commit_parents_exactly_as_git(self):
        candidate, _ = self.completed_batch()
        path = self.fixture.prefix + PROOF_NAME
        original = json.loads(candidate.entries[path].data)
        active = original["active_commit"]
        headers, message = original["commits"][original["completion_commit"]].split("\n\n", 1)
        unparented = [line for line in headers.split("\n") if not line.startswith("parent ")]
        # Git reads parents only from LF-separated lines right after the tree,
        # so neither a later header nor another line break can supply one.
        for forged in (f"x-note  parent {active}", f"parent {active}"):
            with self.subTest(forged=forged):
                record = json.loads(candidate.entries[path].data)
                text = "\n".join(unparented + [forged]) + "\n\n" + message
                oid = object_id("commit", text.encode("utf-8"), len(active))
                record["commits"] = {active: original["commits"][active], oid: text}
                record["completion_commit"] = oid
                candidate.entries[path] = SnapshotEntry(path, "100644", json.dumps(record).encode())
                errors = self.failures(candidate)
                self.assertTrue(any("active first parent" in error for error in errors), errors)

    def test_completion_proof_preserves_nonreading_corrections_and_existing_gate(self):
        candidate, completion = self.completed_batch()
        path = self.fixture.infrastructure
        original = candidate.entries[path]
        candidate.entries[path] = SnapshotEntry(path, "100644", original.data + b"Retrospective ledger update.\n")
        self.bind_completion(candidate, completion)
        self.assertEqual(self.failures(candidate), [])
        del candidate.entries[self.fixture.method]
        self.bind_completion(candidate, completion)
        errors = self.failures(candidate)
        self.assertTrue(any("method" in error for error in errors), errors)
        self.assertFalse(any("publication proof" in error for error in errors), errors)




if __name__ == "__main__":
    unittest.main()
