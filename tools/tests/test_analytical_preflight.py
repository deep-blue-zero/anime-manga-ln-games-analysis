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
from character_index_core import AuthorityGraph, DomainError, GitSnapshot, SnapshotEntry
from generate_character_index import render
from update_repository_indexes import expected_outputs
from validate_repository import (
    validate_generated_index, validate_registered_root_topology, validate_series_registry,
)

SOURCE_SHA = "a" * 40
ENTRYPOINT = "series/example/CURRENT.md"
DESCRIPTOR = "series/example/.repository/series-registry.json"


def entry(path: str, data: bytes) -> SnapshotEntry:
    return SnapshotEntry(path, "100644", data)


def fixture(*, new_root: bool = True) -> GitSnapshot:
    entries = {}
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
            "do_not_use_as_current_authority: false\n---\n# Completed new analysis\n"
        ).encode())
        descriptor = {
            "series_id": "example", "stable_slug": "example", "canonical_title": "Example",
            "repository_path": "series/example/", "canonical_entrypoint": ENTRYPOINT,
            "canonical_entrypoint_status": "PRESENT_VERIFIED",
            "migration_scope": "GIT_NATIVE_POST_CUTOVER_EXAMPLE",
        }
        entries[DESCRIPTOR] = entry(DESCRIPTOR, (json.dumps(descriptor) + "\n").encode())
    return GitSnapshot(TOOLS.parent, SOURCE_SHA, entries)


def fixture_baseline(source: GitSnapshot) -> tuple[GitSnapshot, list[str]]:
    """Normalize inherited routing only in the disposable CLI test fixture.

    A source checkout can legitimately await its own housekeeping. Materialize
    its descriptors before adding the separate synthetic series/example root.
    This does not depend on AUDIT_BRANCH, which the nested test deliberately changes.
    """
    projected = source
    for path in sorted(source.entries):
        match = re.fullmatch(
            r"((series|studies)/[a-z0-9][a-z0-9-]*)/\.repository/(series|study)-registry\.json", path,
        )
        if match and match[3] == ("series" if match[2] == "series" else "study"):
            projected, _ = routing_preflight(projected, match[1])
    changed = sorted(path for path in ROUTING_OUTPUTS if projected.entries[path] != source.entries[path])
    return projected, changed


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

    def test_cli_pending_then_materialized_integration(self) -> None:
        base_value = os.environ.get("MANGA_ANIME_TEST_TMP")
        if not base_value or not Path(base_value).is_dir():
            self.skipTest("MANGA_ANIME_TEST_TMP is not available")
        with tempfile.TemporaryDirectory(dir=base_value) as directory:
            root = Path(directory) / "repository"
            environment = dict(os.environ, PYTHONDONTWRITEBYTECODE="1")
            clone = subprocess.run(
                ["git", "clone", "--shared", str(TOOLS.parent), str(root)],
                env=environment, capture_output=True, text=True, check=False,
            )
            self.assertEqual(clone.returncode, 0, clone.stderr)
            baseline, changed = fixture_baseline(GitSnapshot.from_index(root))
            for path in changed:
                (root / path).write_bytes(baseline.entries[path].data)
            if changed:
                subprocess.run(
                    ["git", "-C", str(root), "add", "--", *changed],
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
            strict = subprocess.run(
                command, cwd=root, env=environment, capture_output=True, text=True, check=False,
            )
            self.assertNotEqual(strict.returncode, 0)
            self.assertIn("unregistered series root: series/example/", strict.stdout)
            projected, deferred = routing_preflight(GitSnapshot.from_index(root), "series/example")
            for path in deferred:
                (root / path).write_bytes(projected.entries[path].data)
            subprocess.run(
                ["git", "-C", str(root), "add", "--", *deferred],
                env=environment, capture_output=True, check=True,
            )
            complete = subprocess.run(
                command, cwd=root, env=environment, capture_output=True, text=True, check=False,
            )
            self.assertEqual(complete.returncode, 0, complete.stdout + complete.stderr)
            self.assertNotIn("AWAITING_SYNCHRONIZATION", complete.stdout)

    def test_nonregular_descriptor_is_not_admissible(self) -> None:
        source = fixture()
        source.entries[DESCRIPTOR] = SnapshotEntry(DESCRIPTOR, "120000", b"elsewhere")
        with self.assertRaisesRegex(DomainError, "tracked regular Git blob"):
            routing_preflight(source, "series/example")


if __name__ == "__main__":
    unittest.main()
