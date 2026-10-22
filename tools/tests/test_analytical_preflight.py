from __future__ import annotations

import json
import os
import re
import subprocess
import tempfile
import sys
import unittest
from pathlib import Path
from unittest import mock

TOOLS = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(TOOLS))
from analytical_preflight import ROUTING_OUTPUTS, routing_preflight
from character_index_core import (
    RECONSTRUCTION_POLICY_PATH, AuthorityGraph, DomainError, GitSnapshot, SnapshotEntry,
)
from generate_character_index import render
from update_repository_indexes import expected_outputs
from validate_repository import (
    RECONSTRUCTION_OUTPUTS, _policy_from_snapshot, _reconstruction_delta_paths,
    _reconstruction_integration_base, _reconstruction_target_commit, validate_bytes,
    validate_generated_index, validate_generated_repository_indexes, validate_paths,
    validate_reconstruction_domain, validate_registered_root_topology, validate_series_registry,
)

SOURCE_SHA = "a" * 40
ENTRYPOINT = "series/example/CURRENT.md"
DESCRIPTOR = "series/example/.repository/series-registry.json"
OUTPUT_ISOLATION_ERROR = "reconstruction production outputs must change alone"


def entry(path: str, data: bytes) -> SnapshotEntry:
    return SnapshotEntry(path, "100644", data)


def fixture(*, new_root: bool = True) -> GitSnapshot:
    state_path = "governance/archive/migration/AUTHORITY_STATE.yaml"
    entries = {state_path: entry(state_path, b"state: GIT_ACTIVE_ACCEPTED\n")}
    for namespace, schema in (
        ("series", "anime-manga-ln-games-analysis/series-registry/v2"),
        ("studies", "anime-manga-ln-games-analysis/study-registry/v1"),
    ):
        path = f"{namespace}/registry.json"
        entries[path] = entry(path, (json.dumps({"schema": schema, namespace: []}) + "\n").encode())
    for path, names in (
        ("series/README.md", ("SERIES CATALOG",)),
        ("studies/README.md", ("STUDY CATALOG",)),
        ("governance/MANGA_ANIME_CORPUS_INDEX.md", ("CORPUS SERIES CATALOG", "CORPUS STUDY CATALOG")),
    ):
        text = "# Preserved author introduction\n\n"
        for name in names:
            text += f"<!-- BEGIN GENERATED {name} -->\n\n<!-- END GENERATED {name} -->\n"
        text += "\nPreserved author footer.\n"
        entries[path] = entry(path, text.encode())
    base = GitSnapshot(TOOLS.parent, SOURCE_SHA, entries)
    for path, data in expected_outputs(base).items():
        entries[path] = entry(path, data)
    entries["characters/registry.jsonl"] = entry("characters/registry.jsonl", b"")
    entries["CHARACTER_ANALYSIS_INDEX.md"] = entry(
        "CHARACTER_ANALYSIS_INDEX.md", render([], AuthorityGraph(base)).encode(),
    )
    if new_root:
        entries[ENTRYPOINT] = entry(ENTRYPOINT, (
            "---\nstatus: canonical\nsupersedes: []\nsuperseded_by: []\n"
            "do_not_use_as_current_authority: false\n"
            "project_initialization:\n  sequential_analysis_lock: CLOSED\n"
            "---\n# Completed new analysis\n"
        ).encode())
        descriptor = {
            "series_id": "example", "stable_slug": "example", "canonical_title": "Example",
            "repository_path": "series/example/", "canonical_entrypoint": ENTRYPOINT,
            "canonical_entrypoint_status": "PRESENT_VERIFIED",
            "migration_scope": "GIT_NATIVE_POST_CUTOVER_EXAMPLE",
            "project_initiation_gate": "REQUIRED",
        }
        entries[DESCRIPTOR] = entry(DESCRIPTOR, (json.dumps(descriptor) + "\n").encode())
    return GitSnapshot(TOOLS.parent, SOURCE_SHA, entries)


def fixture_baseline(
    source: GitSnapshot, published: GitSnapshot | None = None,
) -> tuple[GitSnapshot, list[str]]:
    """Normalize inherited routing and evaluator outputs only in the disposable CLI test fixture.

    A source checkout can legitimately await its own housekeeping. Materialize
    its descriptors before adding the separate synthetic series/example root.
    The evaluator's branch can likewise carry unpublished reconstruction
    outputs, which must change alone: restore them to `published`, the
    validator's integration base, so the synthetic root never mixes with them.
    A candidate that also amends the reconstruction policy keeps its outputs,
    exactly as the validator permits.
    This does not depend on AUDIT_BRANCH, which the nested test deliberately changes.
    """
    projected = source
    for path in sorted(source.entries):
        match = re.fullmatch(
            r"((series|studies)/[a-z0-9][a-z0-9-]*)/\.repository/(series|study)-registry\.json", path,
        )
        if match and match[3] == ("series" if match[2] == "series" else "study"):
            projected, _ = routing_preflight(projected, match[1])
    if published is not None and (
        source.get(RECONSTRUCTION_POLICY_PATH) == published.get(RECONSTRUCTION_POLICY_PATH)
    ):
        entries = dict(projected.entries)
        for path in RECONSTRUCTION_OUTPUTS:
            restored = published.get(path)
            if restored is None:
                entries.pop(path, None)
            else:
                entries[path] = restored
        projected = GitSnapshot(projected.root, projected.identity, entries)
    changed = sorted(
        path for path in ROUTING_OUTPUTS | RECONSTRUCTION_OUTPUTS
        if projected.get(path) != source.get(path)
    )
    return projected, changed


def reconstruction_base(root: Path) -> str:
    """Return the integration base the validator compares a staged index with."""

    target = _reconstruction_target_commit(root, "index", None)
    base = _reconstruction_integration_base(root, target, "index")
    if base is None:
        raise AssertionError(f"no reconstruction integration base in {root}")
    return base


def unpublished_reconstruction_fixture() -> tuple[GitSnapshot, GitSnapshot]:
    """Return a source carrying unpublished reconstruction outputs, and its published state."""

    published = fixture(new_root=False)
    for path in RECONSTRUCTION_OUTPUTS | {RECONSTRUCTION_POLICY_PATH}:
        published.entries[path] = entry(path, b"published\n")
    source = fixture()
    source.entries[RECONSTRUCTION_POLICY_PATH] = published.entries[RECONSTRUCTION_POLICY_PATH]
    for path in RECONSTRUCTION_OUTPUTS:
        source.entries[path] = entry(path, b"unpublished evaluator output\n")
    return source, published


def published_reconstruction(root: Path) -> GitSnapshot:
    """Read the reconstruction policy and outputs at the validator's integration base."""

    return GitSnapshot.from_commit(
        root, reconstruction_base(root), paths=RECONSTRUCTION_OUTPUTS | {RECONSTRUCTION_POLICY_PATH},
    )


def evaluator_candidate(source: GitSnapshot, published: GitSnapshot) -> GitSnapshot:
    """Model the evaluator's branch on `source`: unpublished outputs under the published policy.

    The evaluator never amends the policy, so the model keeps the integration
    base's policy bytes whatever policy change the checkout under test carries.
    """

    entries = dict(source.entries)
    entries[RECONSTRUCTION_POLICY_PATH] = published.entries[RECONSTRUCTION_POLICY_PATH]
    for path in RECONSTRUCTION_OUTPUTS:
        entries[path] = entry(path, b"Unpublished evaluator output.\n")
    return GitSnapshot(source.root, source.identity, entries)


class AnalyticalPreflightTests(unittest.TestCase):
    def test_new_root_defers_only_routing_and_preserves_all_authored_bytes(self) -> None:
        source = fixture()
        before = dict(source.entries)
        self.assertIn("unregistered series root: series/example/", validate_registered_root_topology(source))
        projected, deferred = routing_preflight(source, "series/example")
        self.assertEqual(set(deferred), {
            "series/registry.json", "series/README.md", "governance/MANGA_ANIME_CORPUS_INDEX.md",
        })
        self.assertEqual(source.entries, before)
        self.assertEqual(validate_series_registry(projected), [])
        self.assertEqual(validate_registered_root_topology(projected), [])
        self.assertEqual(validate_generated_index(projected, "commit"), [])
        for path in before:
            if path not in ROUTING_OUTPUTS:
                self.assertEqual(projected.entries[path], before[path], path)
        self.assertIn(b"Preserved author footer.", projected.entries["series/README.md"].data)

    def test_materialized_outputs_require_no_deferral(self) -> None:
        projected, _ = routing_preflight(fixture(), "series/example")
        final, deferred = routing_preflight(projected, "series/example")
        self.assertEqual(deferred, [])
        self.assertEqual(final.entries, projected.entries)

    def test_empty_branch_is_not_a_new_root(self) -> None:
        source = fixture(new_root=False)
        projected, deferred = routing_preflight(source, "series/empty")
        self.assertEqual(deferred, [])
        self.assertEqual(projected.entries, source.entries)

    def test_real_new_root_requires_a_descriptor(self) -> None:
        source = fixture()
        del source.entries[DESCRIPTOR]
        with self.assertRaisesRegex(DomainError, "requires declarative input"):
            routing_preflight(source, "series/example")

    def test_projection_does_not_make_draft_entrypoint_current(self) -> None:
        source = fixture()
        source.entries[ENTRYPOINT] = entry(ENTRYPOINT, (
            "---\nstatus: draft_noncurrent\nsupersedes: []\nsuperseded_by: []\n"
            "do_not_use_as_current_authority: true\n---\n# Draft\n"
        ).encode())
        projected, _ = routing_preflight(source, "series/example")
        self.assertTrue(any("not current-eligible" in error for error in validate_series_registry(projected)))

    def test_projection_does_not_repair_or_ignore_a_broken_character_index(self) -> None:
        source = fixture()
        source.entries["CHARACTER_ANALYSIS_INDEX.md"] = entry("CHARACTER_ANALYSIS_INDEX.md", b"# Stale\n")
        projected, _ = routing_preflight(source, "series/example")
        self.assertIn("CHARACTER_ANALYSIS_INDEX.md is out of date", validate_generated_index(projected, "commit"))

    def test_projector_cannot_expand_its_write_boundary(self) -> None:
        with mock.patch("analytical_preflight.synchronize_snapshot", return_value={ENTRYPOINT: "changed"}):
            with self.assertRaisesRegex(DomainError, "prohibited output"):
                routing_preflight(fixture(), "series/example")

    def test_fixture_baseline_handles_inherited_pending_root_without_changing_content(self) -> None:
        source = fixture()
        before = dict(source.entries)
        self.assertIn("unregistered series root: series/example/", validate_registered_root_topology(source))
        projected, changed = fixture_baseline(source)
        self.assertTrue(changed)
        self.assertLessEqual(set(changed), ROUTING_OUTPUTS)
        self.assertEqual(validate_registered_root_topology(projected), [])
        self.assertEqual(validate_series_registry(projected), [])
        self.assertEqual(source.entries, before)
        for path in before.keys() - ROUTING_OUTPUTS:
            self.assertEqual(projected.entries[path], before[path], path)
        self.assertEqual(fixture_baseline(projected)[1], [])

    def test_fixture_baseline_restores_published_reconstruction_outputs(self) -> None:
        source, published = unpublished_reconstruction_fixture()
        before = dict(source.entries)
        projected, changed = fixture_baseline(source, published)
        self.assertLessEqual(RECONSTRUCTION_OUTPUTS, set(changed))
        self.assertLessEqual(set(changed), ROUTING_OUTPUTS | RECONSTRUCTION_OUTPUTS)
        for path in RECONSTRUCTION_OUTPUTS:
            self.assertEqual(projected.entries[path], published.entries[path], path)
        self.assertEqual(source.entries, before)
        for path in before.keys() - ROUTING_OUTPUTS - RECONSTRUCTION_OUTPUTS:
            self.assertEqual(projected.entries[path], before[path], path)
        self.assertEqual(fixture_baseline(projected, published)[1], [])

    def test_fixture_baseline_keeps_outputs_when_the_candidate_amends_policy(self) -> None:
        # A reviewed policy amendment may change the outputs beside other paths.
        source, published = unpublished_reconstruction_fixture()
        source.entries[RECONSTRUCTION_POLICY_PATH] = entry(RECONSTRUCTION_POLICY_PATH, b"amended\n")
        before = dict(source.entries)
        amended, changed = fixture_baseline(source, published)
        self.assertFalse(set(changed) & RECONSTRUCTION_OUTPUTS)
        self.assertEqual(source.entries, before)
        for path in RECONSTRUCTION_OUTPUTS | {RECONSTRUCTION_POLICY_PATH}:
            self.assertEqual(amended.entries[path], before[path], path)

    def clone_checkout(self, root: Path, environment: dict[str, str]) -> None:
        """Clone the checkout under test and pin the clone's main to the source's."""

        clone = subprocess.run(
            ["git", "clone", "--config", "core.longpaths=true", "--shared", str(TOOLS.parent), str(root)],
            env=environment, capture_output=True, text=True, check=False,
        )
        self.assertEqual(clone.returncode, 0, clone.stderr)
        # The gate reads run stops from main. A CI checkout has no local
        # branches, so pin the clone's main to the source's explicitly.
        source_main = subprocess.run(
            ["git", "-C", str(TOOLS.parent), "rev-parse", "--verify", "-q",
             "refs/remotes/origin/main^{commit}"],
            env=environment, capture_output=True, text=True, check=False,
        ).stdout.strip() or subprocess.run(
            ["git", "-C", str(TOOLS.parent), "rev-parse", "HEAD"],
            env=environment, capture_output=True, text=True, check=True,
        ).stdout.strip()
        subprocess.run(
            ["git", "-C", str(root), "update-ref", "refs/remotes/origin/main", source_main],
            env=environment, capture_output=True, check=True,
        )

    def stage_cli_fixture(self, root: Path, environment: dict[str, str], candidate: GitSnapshot,
                          *, pin_main: bool = False) -> None:
        """Make the clone's index exactly `candidate`, normalize its baseline, then add the synthetic root.

        With `pin_main`, the normalized candidate becomes the clone's main, so
        the staged delta models a series branch carrying only the synthetic root.
        """

        cloned = GitSnapshot.from_index(root)
        candidate_paths = sorted(
            path for path in candidate.entries.keys() | cloned.entries.keys()
            if candidate.get(path) != cloned.get(path)
        )
        for path in candidate_paths:
            target = root / path
            entry = candidate.get(path)
            if entry is None:
                target.unlink()
            else:
                self.assertEqual(entry.mode, "100644")
                target.parent.mkdir(parents=True, exist_ok=True)
                target.write_bytes(entry.data)
        if candidate_paths:
            subprocess.run(
                ["git", "-C", str(root), "add", "--", *candidate_paths],
                env=environment, capture_output=True, check=True,
            )
        self.assertEqual(GitSnapshot.from_index(root).entries, candidate.entries)
        baseline, changed = fixture_baseline(GitSnapshot.from_index(root), published_reconstruction(root))
        for path in changed:
            entry = baseline.get(path)
            if entry is None:
                (root / path).unlink()
            else:
                (root / path).write_bytes(entry.data)
        if changed:
            subprocess.run(
                ["git", "-C", str(root), "add", "--", *changed],
                env=environment, capture_output=True, check=True,
            )
        if pin_main:
            identity = dict(
                environment,
                GIT_AUTHOR_NAME="deep-blue-zero", GIT_AUTHOR_EMAIL="50891441+peipw@users.noreply.github.com",
                GIT_COMMITTER_NAME="deep-blue-zero", GIT_COMMITTER_EMAIL="50891441+peipw@users.noreply.github.com",
            )
            subprocess.run(
                ["git", "-C", str(root), "commit", "-q", "--allow-empty", "--no-verify", "-m", "fixture main"],
                env=identity, capture_output=True, check=True,
            )
            subprocess.run(
                ["git", "-C", str(root), "update-ref", "refs/remotes/origin/main", "HEAD"],
                env=environment, capture_output=True, check=True,
            )
        source = fixture()
        for path in (ENTRYPOINT, DESCRIPTOR):
            target = root / path
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(source.entries[path].data)
        subprocess.run(
            ["git", "-C", str(root), "add", "--", ENTRYPOINT, DESCRIPTOR],
            env=environment, capture_output=True, check=True,
        )

    def assert_evaluator_outputs_isolated(self, root: Path) -> None:
        changed = _reconstruction_delta_paths(root, "index", reconstruction_base(root), None)
        self.assertLessEqual({ENTRYPOINT, DESCRIPTOR}, changed)
        self.assertEqual(changed & RECONSTRUCTION_OUTPUTS, set())
        # Only the isolation rule is this fixture's concern: the modelled
        # published policy need not satisfy an amended gate under test.
        errors, _notices = validate_reconstruction_domain(root, GitSnapshot.from_index(root), "index", None)
        self.assertEqual([error for error in errors if OUTPUT_ISOLATION_ERROR in error], [])

    def test_cli_fixture_does_not_mix_unpublished_reconstruction_outputs(self) -> None:
        base_value = os.environ.get("MANGA_ANIME_TEST_TMP")
        if not base_value or not Path(base_value).is_dir():
            self.skipTest("MANGA_ANIME_TEST_TMP is not available")
        with tempfile.TemporaryDirectory(dir=base_value) as directory:
            root = Path(directory) / "repository"
            environment = dict(os.environ, PYTHONDONTWRITEBYTECODE="1")
            self.clone_checkout(root, environment)
            candidate = evaluator_candidate(GitSnapshot.from_index(TOOLS.parent), published_reconstruction(root))
            self.stage_cli_fixture(root, environment, candidate)
            self.assert_evaluator_outputs_isolated(root)

    def test_cli_fixture_from_a_policy_amending_checkout(self) -> None:
        base_value = os.environ.get("MANGA_ANIME_TEST_TMP")
        if not base_value or not Path(base_value).is_dir():
            self.skipTest("MANGA_ANIME_TEST_TMP is not available")
        with tempfile.TemporaryDirectory(dir=base_value) as directory:
            root = Path(directory) / "repository"
            environment = dict(os.environ, PYTHONDONTWRITEBYTECODE="1")
            self.clone_checkout(root, environment)
            # Model a checkout that amends the policy: the live policy with one
            # more trailing newline, its valid outputs unchanged.
            amended = GitSnapshot.from_index(TOOLS.parent)
            policy = amended.entries[RECONSTRUCTION_POLICY_PATH]
            amended.entries[RECONSTRUCTION_POLICY_PATH] = SnapshotEntry(
                policy.path, policy.mode, policy.data + b"\n",
            )
            # The amendment keeps its outputs, and the validator exempts the delta.
            self.stage_cli_fixture(root, environment, amended)
            changed = _reconstruction_delta_paths(root, "index", reconstruction_base(root), None)
            self.assertLessEqual({RECONSTRUCTION_POLICY_PATH, ENTRYPOINT, DESCRIPTOR}, changed)
            staged = GitSnapshot.from_index(root)
            for path in RECONSTRUCTION_OUTPUTS:
                self.assertEqual(staged.get(path), amended.get(path), path)
            errors, _notices = validate_reconstruction_domain(root, staged, "index", None)
            self.assertEqual(errors, [])
            # Restaged in the same clone, the evaluator model built from this
            # checkout still isolates its outputs.
            self.stage_cli_fixture(root, environment, evaluator_candidate(amended, published_reconstruction(root)))
            self.assert_evaluator_outputs_isolated(root)

    def test_cli_pending_then_materialized_integration(self) -> None:
        base_value = os.environ.get("MANGA_ANIME_TEST_TMP")
        if not base_value or not Path(base_value).is_dir():
            self.skipTest("MANGA_ANIME_TEST_TMP is not available")
        with tempfile.TemporaryDirectory(dir=base_value) as directory:
            root = Path(directory) / "repository"
            environment = dict(os.environ, PYTHONDONTWRITEBYTECODE="1")
            # A local full gate runs before commit: overlay its exact staged
            # candidate so nested CLIs do not accidentally test the old HEAD.
            self.clone_checkout(root, environment)
            self.stage_cli_fixture(root, environment, GitSnapshot.from_index(TOOLS.parent), pin_main=True)
            command = [
                sys.executable, str(root / "tools/validate_repository.py"),
                "--phase", "current", "--snapshot", "index", "--repo", str(root),
            ]
            pending = subprocess.run(
                command + ["--routing-preflight", "series/example"],
                cwd=root, env=environment, capture_output=True, text=True, check=False,
            )
            self.assertEqual(pending.returncode, 0, pending.stdout + pending.stderr)
            self.assertIn("AWAITING_SYNCHRONIZATION", pending.stdout)
            projected_tests = subprocess.run(
                [sys.executable, "-m", "unittest", "discover", "-s", "tools/tests",
                 "-p", "test_repository_indexes.py"],
                cwd=root, env=dict(environment, AUDIT_EVENT="push", AUDIT_BRANCH="series/example"),
                capture_output=True, text=True, check=False,
            )
            self.assertEqual(projected_tests.returncode, 0, projected_tests.stdout + projected_tests.stderr)
            # The CLI run above checks paths, bytes and identities before it
            # projects routing, then everything else on the projection except
            # the catalog render it defers. Check exactly that remainder here:
            # the strict topology failure without preflight, and the committed
            # projection's paths, bytes and catalogs.
            staged = GitSnapshot.from_index(root)
            self.assertIn(
                "unregistered series root: series/example/",
                validate_registered_root_topology(staged),
            )
            projected, deferred = routing_preflight(staged, "series/example")
            for path in deferred:
                (root / path).write_bytes(projected.entries[path].data)
            subprocess.run(
                ["git", "-C", str(root), "add", "--", *deferred],
                env=environment, capture_output=True, check=True,
            )
            complete = GitSnapshot.from_index(root)
            self.assertEqual(complete.entries, projected.entries)
            self.assertEqual(routing_preflight(complete, "series/example")[1], [])
            self.assertEqual(validate_registered_root_topology(complete), [])
            self.assertEqual(validate_generated_repository_indexes(complete), [])
            policy = _policy_from_snapshot(complete)
            self.assertEqual(validate_paths(complete, policy), [])
            self.assertEqual(validate_bytes(complete, policy, "current"), [])

    def test_nonregular_descriptor_is_not_admissible(self) -> None:
        source = fixture()
        source.entries[DESCRIPTOR] = SnapshotEntry(DESCRIPTOR, "120000", b"elsewhere")
        with self.assertRaisesRegex(DomainError, "tracked regular Git blob"):
            routing_preflight(source, "series/example")


if __name__ == "__main__":
    unittest.main()
