from __future__ import annotations

import json
import sys
import unittest
from pathlib import Path


TOOLS = Path(__file__).resolve().parents[1]
ROOT = TOOLS.parent
sys.path.insert(0, str(TOOLS))

from character_index_core import GitSnapshot, SnapshotEntry  # noqa: E402
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
        registry = json.loads(snapshot.entries["series/registry.json"].data)
        ids = {row["series_id"] for row in registry["series"]}
        self.assertTrue(
            {"ascendance-of-a-bookworm", "kimishinu", "lycoris-recoil"} <= ids
        )
        control, control_errors = _load_project_initiation_gate(snapshot)
        self.assertEqual(control_errors, [])
        assert control is not None
        failures = validate_project_initiation_gate(
            snapshot, project_initiation_baseline_paths(ROOT, control), control
        )
        self.assertEqual(failures, [])


if __name__ == "__main__":
    unittest.main()
