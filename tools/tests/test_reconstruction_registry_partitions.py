from __future__ import annotations

import json
import os
import shutil
import stat
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

TOOLS = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(TOOLS))

from character_index_core import (  # noqa: E402
    ABSENT_LAYOUT,
    LEGACY_LAYOUT,
    PARTITIONED_LAYOUT,
    DomainError,
    GitSnapshot,
    current_reconstruction_layout_errors,
    is_reconstruction_output,
    read_reconstruction_registry,
    reconstruction_commit_snapshot,
    reconstruction_partition_path,
    reconstruction_partition_subject,
)
from generate_reconstruction_index import generated_output_errors, write_outputs  # noqa: E402
from reconstruction_registry import export, normalize, replay, unstaged_registry_paths  # noqa: E402
from test_character_index_v2 import snapshot  # noqa: E402

LEGACY = "characters/reconstruction_capabilities.jsonl"
ALICE = "characters/reconstruction_capabilities/example/alice@anime.jsonl"
BOB = "characters/reconstruction_capabilities/example/bob@anime.jsonl"
CAROL = "characters/reconstruction_capabilities/other/carol@anime.jsonl"


def record(assessment_id: str, subject_id: str = "example:alice@anime", **fields: object) -> dict:
    item = {"assessment_id": assessment_id, "analysis_subject_id": subject_id, "assessment_status": "CANDIDATE"}
    item.update(fields)
    return item


def line(item: dict) -> bytes:
    return (json.dumps(item, ensure_ascii=False, sort_keys=True, separators=(",", ":")) + "\n").encode()


class RegistryLayoutTests(unittest.TestCase):
    def test_partition_paths_round_trip_subject_ids(self) -> None:
        self.assertEqual(reconstruction_partition_path("example:alice@anime"), ALICE)
        self.assertEqual(reconstruction_partition_subject(ALICE), "example:alice@anime")
        for path in (
            "characters/reconstruction_capabilities/example.jsonl",
            "characters/reconstruction_capabilities/example/alice.jsonl",
            "characters/reconstruction_capabilities/example/nested/alice@anime.jsonl",
            "characters/reconstruction_capabilities/Example/alice@anime.jsonl",
            "characters/reconstruction_capabilities/example/alice@anime.json",
            LEGACY,
        ):
            self.assertIsNone(reconstruction_partition_subject(path), path)
        with self.assertRaises(DomainError):
            reconstruction_partition_path("example:alice")

    def test_partitions_form_one_logical_registry_in_assessment_order(self) -> None:
        alice_v1, alice_v2 = record("alice-anime-v1"), record("alice-anime-v2")
        carol = record("a-carol-v1", "other:carol@anime")
        registry = read_reconstruction_registry(
            snapshot((ALICE, line(alice_v1) + line(alice_v2)), (CAROL, line(carol)))
        )
        self.assertEqual(registry.layout, PARTITIONED_LAYOUT)
        self.assertEqual(registry.layout_errors, ())
        # The logical order is ASCII assessment_id, as in the retired single file.
        self.assertEqual(registry.records, [carol, alice_v1, alice_v2])
        self.assertEqual([row.label for row in registry.rows], [f"{CAROL}:1", f"{ALICE}:1", f"{ALICE}:2"])
        self.assertEqual(current_reconstruction_layout_errors(registry), [])

    def test_retired_single_file_is_read_but_rejected_as_current(self) -> None:
        registry = read_reconstruction_registry(
            snapshot((LEGACY, line(record("alice-anime-v1")) + line(record("bob-anime-v1", "example:bob@anime"))))
        )
        self.assertEqual(registry.layout, LEGACY_LAYOUT)
        self.assertEqual(len(registry.records), 2)
        self.assertTrue(any("is retired" in item for item in current_reconstruction_layout_errors(registry)))

    def test_absent_registry_reads_as_no_records_but_is_not_current(self) -> None:
        registry = read_reconstruction_registry(snapshot(("series/registry.json", b"{}\n")))
        self.assertEqual((registry.layout, registry.records), (ABSENT_LAYOUT, []))
        self.assertTrue(any("is absent" in item for item in current_reconstruction_layout_errors(registry)))

    def test_layouts_cannot_coexist(self) -> None:
        with self.assertRaisesRegex(DomainError, "cannot coexist"):
            read_reconstruction_registry(
                snapshot((LEGACY, line(record("alice-anime-v1"))), (ALICE, line(record("alice-anime-v2"))))
            )

    def test_placement_order_and_byte_form_are_enforced(self) -> None:
        v1, v2 = line(record("alice-anime-v1")), line(record("alice-anime-v2"))
        cases = {
            f"belongs in {ALICE}": ((BOB, v1),),
            "ordered by ASCII assessment_id": ((ALICE, v2 + v1),),
            "must be unique": ((ALICE, v1 + v1),),
            "duplicate assessment_id alice-anime-v1": ((ALICE, v1), (BOB, line(record("alice-anime-v1", "example:bob@anime")))),
            "blank lines are prohibited": ((ALICE, v1 + b"\n" + v2),),
            "must end with LF": ((ALICE, v1.rstrip(b"\n")),),
            "holds no records": ((ALICE, b""),),
            "unexpected path": (("characters/reconstruction_capabilities/example.jsonl", v1),),
        }
        for expected, entries in cases.items():
            with self.subTest(expected=expected):
                errors = read_reconstruction_registry(snapshot(*entries)).layout_errors
                self.assertTrue(any(expected in item for item in errors), errors)

    def test_reconstruction_outputs_cover_both_layouts_and_nothing_else(self) -> None:
        for path in (LEGACY, ALICE, "characters/CHARACTER_RECONSTRUCTION_INDEX.md", "characters/reconstruction_index/example.md"):
            self.assertTrue(is_reconstruction_output(path), path)
        for path in (
            "characters/README.md",
            "characters/RECONSTRUCTION_CAPABILITY_SPEC.md",
            "characters/registry.jsonl",
            "characters/registry/example.jsonl",
            "characters/index/example.md",
            "CHARACTER_ANALYSIS_INDEX.md",
            "series/example/A.md",
        ):
            self.assertFalse(is_reconstruction_output(path), path)


class RegistryToolTests(unittest.TestCase):
    """normalize, replay and export against a disposable Git repository."""

    def setUp(self) -> None:
        base_value = os.environ.get("MANGA_ANIME_TEST_TMP")
        if not base_value:
            self.skipTest("MANGA_ANIME_TEST_TMP is not set")
        base = Path(base_value).resolve(strict=True)
        self.root = Path(tempfile.mkdtemp(prefix="reconstruction-partitions-", dir=base)).resolve(strict=True)
        self.assertTrue(self.root.is_relative_to(base))
        self.git("init", "--quiet")
        self.git("config", "user.name", "Character Index Test")
        self.git("config", "user.email", "character-index-test.invalid@example.invalid")

    def tearDown(self) -> None:
        def clear_readonly(function, path, _exception):
            os.chmod(path, stat.S_IWRITE | stat.S_IREAD)
            function(path)

        root = getattr(self, "root", None)
        if root is not None:
            shutil.rmtree(root, onexc=clear_readonly)

    def git(self, *args: str) -> str:
        return subprocess.check_output(
            ["git", "-C", str(self.root), *args], stderr=subprocess.PIPE, text=True
        ).strip()

    def write(self, path: str, data: bytes) -> None:
        target = self.root / Path(path)
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(data)

    def read(self, path: str) -> bytes:
        return (self.root / Path(path)).read_bytes()

    def commit(self, message: str) -> str:
        self.git("add", "--all", "--", "characters")
        self.git("commit", "--quiet", "-m", message)
        return self.git("rev-parse", "HEAD")

    def test_migration_moves_records_byte_for_byte_and_export_is_unchanged(self) -> None:
        # Unsorted keys prove that records are moved, never re-serialized.
        raw_bob = json.dumps(record("bob-anime-v1", "example:bob@anime"), separators=(",", ":")).encode() + b"\n"
        alice_v1, alice_v2 = line(record("alice-anime-v1")), line(record("alice-anime-v2", overall_tier="B"))
        carol = line(record("a-carol-v1", "other:carol@anime"))
        legacy = carol + alice_v1 + alice_v2 + raw_bob
        self.write(LEGACY, legacy)
        before = self.commit("single file")
        # Byte order: the retired file sorts before the directory it is replaced by.
        self.assertEqual(normalize(self.root), [LEGACY, ALICE, BOB, CAROL])
        self.assertFalse((self.root / LEGACY).exists())
        self.assertEqual(self.read(ALICE), alice_v1 + alice_v2)
        self.assertEqual(self.read(BOB), raw_bob)
        self.assertEqual(self.read(CAROL), carol)
        self.assertEqual(normalize(self.root), [])
        self.assertEqual(unstaged_registry_paths(self.root), [LEGACY, ALICE, BOB, CAROL])
        after = self.commit("partitions")
        self.assertEqual(unstaged_registry_paths(self.root), [])
        exported = export(reconstruction_commit_snapshot(self.root, after))
        self.assertEqual(exported, legacy)
        self.assertEqual(exported, export(reconstruction_commit_snapshot(self.root, before)))
        selected = reconstruction_commit_snapshot(self.root, after)
        self.assertEqual(sorted(selected.entries), [ALICE, BOB, CAROL])
        registry = read_reconstruction_registry(selected)
        self.assertEqual(registry.layout_errors, ())
        self.assertEqual([row.record["assessment_id"] for row in registry.rows],
                         ["a-carol-v1", "alice-anime-v1", "alice-anime-v2", "bob-anime-v1"])

    def test_normalize_moves_misplaced_records_and_deletes_emptied_partitions(self) -> None:
        stray = "characters/reconstruction_capabilities/other/stray@anime.jsonl"
        self.write(ALICE, line(record("alice-anime-v2")))
        self.write(stray, line(record("alice-anime-v1")))
        self.assertEqual(normalize(self.root), [ALICE, stray])
        self.assertFalse((self.root / stray).exists())
        self.assertFalse((self.root / "characters/reconstruction_capabilities/other").exists())
        self.assertEqual(self.read(ALICE), line(record("alice-anime-v1")) + line(record("alice-anime-v2")))

    def test_replay_carries_branch_assessments_across_the_migration(self) -> None:
        alice = record("alice-anime-v1")
        bob = record("bob-anime-v1", "example:bob@anime")
        self.write(LEGACY, line(alice) + line(bob))
        base = self.commit("merge base")
        # The pre-migration branch reconciles Bob as STALE and adds Carol's candidate.
        stale_bob = dict(bob, assessment_status="STALE", stale_reason="Evidence changed.")
        carol = record("carol-anime-v1", "other:carol@anime")
        self.write(LEGACY, line(alice) + line(stale_bob) + line(carol))
        head = self.commit("pending assessments")
        # Main meanwhile migrated, and separately added a superseding Alice record.
        alice_v2 = record("alice-anime-v2", supersedes_assessment_id="alice-anime-v1")
        (self.root / LEGACY).unlink()
        self.write(ALICE, line(alice) + line(alice_v2))
        self.write(BOB, line(bob))
        self.assertEqual(replay(self.root, base, head), [BOB, CAROL])
        self.assertEqual(self.read(ALICE), line(alice) + line(alice_v2))
        self.assertEqual(self.read(BOB), line(stale_bob))
        self.assertEqual(self.read(CAROL), line(carol))
        self.assertEqual(replay(self.root, base, head), [])

        # A record both sides changed stops the run before anything is written.
        main_bob = dict(bob, assessment_status="SUPERSEDED", superseded_by_assessment_id="bob-anime-v2")
        self.write(BOB, line(main_bob))
        before = self.read(BOB)
        with self.assertRaisesRegex(DomainError, "bob-anime-v1"):
            replay(self.root, base, head)
        self.assertEqual(self.read(BOB), before)

    def test_replay_refuses_the_retired_file_in_the_worktree(self) -> None:
        self.write(LEGACY, line(record("alice-anime-v1")))
        base = self.commit("single file")
        with self.assertRaisesRegex(DomainError, "needs the partitioned layout"):
            replay(self.root, base, base)

    def test_staging_report_covers_edits_normalization_leaves_untouched(self) -> None:
        self.write(ALICE, line(record("alice-anime-v1")))
        self.commit("partition")
        # A lifecycle transition in place keeps its order, so normalization rewrites nothing.
        stale = record("alice-anime-v1", assessment_status="STALE", stale_reason="Evidence changed.")
        self.write(ALICE, line(stale))
        # A new partition written already sorted needs no rewriting either.
        self.write(CAROL, line(record("carol-anime-v1", "other:carol@anime")))
        self.assertEqual(normalize(self.root), [])
        self.assertEqual(unstaged_registry_paths(self.root), [ALICE, CAROL])
        self.git("add", "--", ALICE)
        self.assertEqual(unstaged_registry_paths(self.root), [CAROL])

    def test_writers_refuse_symlinked_managed_directories(self) -> None:
        outside = Path(tempfile.mkdtemp(prefix="reconstruction-outside-", dir=self.root.parent))
        self.addCleanup(shutil.rmtree, outside)
        sentinel = outside / "unrelated.jsonl"
        sentinel.write_bytes(line(record("alice-anime-v1")))
        (self.root / "characters").mkdir()
        for name, run in (
            ("reconstruction_capabilities", lambda: normalize(self.root)),
            ("reconstruction_index", lambda: write_outputs(
                self.root,
                GitSnapshot(self.root, "TEST", {}),
                {
                    "characters/CHARACTER_RECONSTRUCTION_INDEX.md": "# Index\n",
                    "characters/reconstruction_index/example.md": "# Page\n",
                },
            )),
        ):
            with self.subTest(name=name):
                link = self.root / "characters" / name
                link.symlink_to(outside, target_is_directory=True)
                with self.assertRaisesRegex(DomainError, "symlink"):
                    run()
                link.unlink()
                self.assertEqual(sorted(item.name for item in outside.iterdir()), ["unrelated.jsonl"])
                self.assertEqual(sentinel.read_bytes(), line(record("alice-anime-v1")))
        self.assertFalse((self.root / "characters/CHARACTER_RECONSTRUCTION_INDEX.md").exists())

    def test_pre_migration_branch_merges_identical_records_and_refuses_conflicts(self) -> None:
        alice = line(record("alice-anime-v1"))
        # A branch that kept its single file beside main's partitions after a merge.
        self.write(ALICE, alice)
        self.write(LEGACY, alice + line(record("bob-anime-v1", "example:bob@anime")))
        self.assertEqual(normalize(self.root), [LEGACY, BOB])
        self.assertEqual(self.read(ALICE), alice)
        self.assertEqual(self.read(BOB), line(record("bob-anime-v1", "example:bob@anime")))
        self.write(LEGACY, line(record("alice-anime-v1", assessment_status="STALE")))
        with self.assertRaisesRegex(DomainError, "conflicting records"):
            normalize(self.root)
        # Nothing is written or removed when a conflict stops the run.
        self.assertTrue((self.root / LEGACY).exists())
        self.assertEqual(self.read(ALICE), alice)

    def test_generated_pages_are_written_checked_and_pruned(self) -> None:
        rendered = {
            "characters/CHARACTER_RECONSTRUCTION_INDEX.md": "# Index\n",
            "characters/reconstruction_index/example.md": "# Example\n",
        }
        self.write("characters/reconstruction_index/retired.md", b"# Retired\n")
        self.commit("stale page")
        tracked = GitSnapshot.from_index(self.root)
        self.assertEqual(
            write_outputs(self.root, tracked, rendered),
            [
                "characters/CHARACTER_RECONSTRUCTION_INDEX.md",
                "characters/reconstruction_index/example.md",
                "characters/reconstruction_index/retired.md",
            ],
        )
        self.assertFalse((self.root / "characters/reconstruction_index/retired.md").exists())
        self.assertEqual(write_outputs(self.root, tracked, rendered), ["characters/reconstruction_index/retired.md"])
        errors = generated_output_errors(tracked, rendered)
        self.assertIn("generated reconstruction index output is missing: characters/CHARACTER_RECONSTRUCTION_INDEX.md", errors)
        self.assertTrue(any("retired.md is not a generated namespace page" in item for item in errors))
        self.commit("pages")
        self.assertEqual(generated_output_errors(GitSnapshot.from_index(self.root), rendered), [])


if __name__ == "__main__":
    unittest.main()
