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
    AuthorityGraph,
    DomainError,
    GitSnapshot,
    SnapshotEntry,
    current_layout_errors,
    discovery_commit_snapshot,
    is_discovery_output,
    read_discovery_registry,
)
from character_registry import export, normalize, replay, unstaged_registry_paths  # noqa: E402
from generate_character_index import (  # noqa: E402
    generated_output_errors,
    render_outputs,
    write_outputs,
)
from test_character_index_v2 import (  # noqa: E402
    authority_bytes,
    partition_documents,
    record,
    snapshot,
)
from validate_repository import validate_change_obligations, validate_markdown_links  # noqa: E402


def line(item: dict) -> bytes:
    return (json.dumps(item, ensure_ascii=False, sort_keys=True, separators=(",", ":")) + "\n").encode()


def bob(subject_id: str = "example:bob@anime", **kwargs) -> dict:
    item = record(subject_id, entity_id="example:bob", **kwargs)
    item["preferred_name"] = "Bob"
    item["entity_aliases"] = []
    return item


class RegistryLayoutTests(unittest.TestCase):
    def test_partitions_form_one_logical_registry_with_source_labels(self) -> None:
        alice = record("example:alice@anime")
        other = record("other:carol@anime", entity_id="other:carol", series_id="other")
        registry = read_discovery_registry(
            snapshot(
                ("characters/registry/example.jsonl", line(alice) + line(bob())),
                ("characters/registry/other.jsonl", line(other)),
            )
        )
        self.assertEqual(registry.layout, PARTITIONED_LAYOUT)
        self.assertEqual(registry.layout_errors, ())
        self.assertEqual(registry.records, [alice, bob(), other])
        self.assertEqual(
            registry.labels,
            [
                "characters/registry/example.jsonl:1",
                "characters/registry/example.jsonl:2",
                "characters/registry/other.jsonl:1",
            ],
        )

    def test_retired_single_file_is_read_but_rejected_as_current(self) -> None:
        registry = read_discovery_registry(
            snapshot(("characters/registry.jsonl", line(bob()) + line(record("example:alice@anime"))))
        )
        self.assertEqual(registry.layout, LEGACY_LAYOUT)
        self.assertEqual(len(registry.records), 2)
        self.assertTrue(any("is retired" in item for item in current_layout_errors(registry)))

    def test_absent_registry_reads_as_no_rows_but_is_not_current(self) -> None:
        # Pre-registry commits read as empty; a current snapshot must have partitions.
        registry = read_discovery_registry(snapshot(("series/registry.json", b"{}\n")))
        self.assertEqual((registry.layout, registry.records), (ABSENT_LAYOUT, []))
        self.assertTrue(any("is absent" in item for item in current_layout_errors(registry)))

    def test_layouts_cannot_coexist(self) -> None:
        with self.assertRaisesRegex(DomainError, "cannot coexist"):
            read_discovery_registry(
                snapshot(
                    ("characters/registry.jsonl", line(bob())),
                    ("characters/registry/example.jsonl", line(record("example:alice@anime"))),
                )
            )

    def test_placement_order_and_byte_form_are_enforced(self) -> None:
        alice = line(record("example:alice@anime"))
        cases = {
            "belongs in characters/registry/example.jsonl": (
                ("characters/registry/other.jsonl", alice),
            ),
            "strictly ascending": (("characters/registry/example.jsonl", line(bob()) + alice),),
            "duplicate analysis_subject_id": (("characters/registry/example.jsonl", alice + alice),),
            "no blank lines": (("characters/registry/example.jsonl", alice + b"\n"),),
            "final LF": (("characters/registry/example.jsonl", alice.rstrip(b"\n")),),
            "holds no rows": (("characters/registry/example.jsonl", b""),),
            "unexpected path": (("characters/registry/nested/example.jsonl", alice),),
            "unexpected path in": (("characters/registry/Example.jsonl", alice),),
        }
        for expected, entries in cases.items():
            with self.subTest(expected=expected):
                errors = read_discovery_registry(snapshot(*entries)).layout_errors
                self.assertTrue(any(expected in item for item in errors), errors)

    def test_discovery_outputs_cover_both_layouts_and_nothing_else(self) -> None:
        for path in (
            "CHARACTER_ANALYSIS_INDEX.md",
            "characters/registry.jsonl",
            "characters/registry/example.jsonl",
            "characters/index/example.md",
        ):
            self.assertTrue(is_discovery_output(path), path)
        for path in (
            "characters/README.md",
            "characters/reconstruction_capabilities.jsonl",
            "characters/CHARACTER_RECONSTRUCTION_INDEX.md",
            "series/example/A.md",
        ):
            self.assertFalse(is_discovery_output(path), path)


class GeneratedPagesTests(unittest.TestCase):
    def setUp(self) -> None:
        self.path_a = "series/example/A.md"
        self.path_b = "series/other/B.md"
        self.alice = record("example:alice@anime", evidence_path=self.path_a, included=True)
        self.carol = record(
            "other:carol@anime",
            entity_id="other:carol",
            series_id="other",
            evidence_path=self.path_b,
            included=True,
        )
        self.carol["preferred_name"] = "Carol"
        self.carol["entity_aliases"] = []
        self.candidate = bob()
        self.evidence = snapshot((self.path_a, authority_bytes()), (self.path_b, authority_bytes()))
        self.outputs = render_outputs(
            [self.alice, self.carol, self.candidate], AuthorityGraph(self.evidence)
        )

    def test_one_page_per_namespace_with_included_rows(self) -> None:
        self.assertEqual(
            sorted(self.outputs),
            ["CHARACTER_ANALYSIS_INDEX.md", "characters/index/example.md", "characters/index/other.md"],
        )
        root = self.outputs["CHARACTER_ANALYSIS_INDEX.md"]
        self.assertIn("[Alice](characters/index/example.md#alice)", root)
        self.assertIn("`other:carol@anime`", root)
        self.assertIn("Alice Example", root)
        self.assertNotIn("Bob", root + self.outputs["characters/index/example.md"])
        page = self.outputs["characters/index/example.md"]
        self.assertIn('<a id="alice"></a>', page)
        self.assertIn("](../../series/example/A.md)", page)
        self.assertNotIn("Carol", page)

    def test_every_generated_link_resolves(self) -> None:
        tree = dict(self.evidence.entries)
        for path, data in partition_documents([self.alice, self.carol]).items():
            tree[path] = SnapshotEntry(path, "100644", data)
        for path, text in self.outputs.items():
            tree[path] = SnapshotEntry(path, "100644", text.encode())
        self.assertEqual(validate_markdown_links(GitSnapshot(Path("."), "TEST", tree)), [])

    def test_missing_stale_and_orphan_pages_are_reported(self) -> None:
        current = snapshot(*((path, text.encode()) for path, text in self.outputs.items()))
        self.assertEqual(generated_output_errors(current, self.outputs), [])
        edited = dict(current.entries)
        del edited["characters/index/other.md"]
        edited["characters/index/example.md"] = SnapshotEntry(
            "characters/index/example.md", "100644", b"# Edited\n"
        )
        edited["characters/index/retired.md"] = SnapshotEntry(
            "characters/index/retired.md", "100644", b"# Retired\n"
        )
        errors = generated_output_errors(GitSnapshot(Path("."), "TEST", edited), self.outputs)
        self.assertIn("generated character index output is missing: characters/index/other.md", errors)
        self.assertIn("characters/index/example.md is out of date", errors)
        self.assertTrue(any("characters/index/retired.md is not a generated" in item for item in errors))

    def test_empty_registry_renders_only_the_root(self) -> None:
        outputs = render_outputs([self.candidate], AuthorityGraph(self.evidence))
        self.assertEqual(list(outputs), ["CHARACTER_ANALYSIS_INDEX.md"])
        self.assertIn("No reviewed entries", outputs["CHARACTER_ANALYSIS_INDEX.md"])


class ChangeObligationTests(unittest.TestCase):
    def obligations(self, trigger: dict) -> list[str]:
        document = {
            "schema": "anime-manga-ln-games-analysis/change-obligations/v1",
            "rules": [
                {
                    "id": "character-discovery",
                    "description": "Index follows the registry partitions.",
                    "trigger": trigger,
                    "required_outputs": ["CHARACTER_ANALYSIS_INDEX.md"],
                }
            ],
        }
        return validate_change_obligations(
            snapshot(
                ("governance/repository-controls/change-obligations.json", json.dumps(document).encode()),
                ("CHARACTER_ANALYSIS_INDEX.md", b"# Index\n"),
            )
        )

    def test_prefix_trigger_must_name_a_directory(self) -> None:
        self.assertEqual(
            self.obligations({"kind": "path_prefix_changed", "prefix": "characters/registry/"}), []
        )
        for prefix in ("characters/registry", "", "../registry/", None):
            with self.subTest(prefix=prefix):
                self.assertTrue(self.obligations({"kind": "path_prefix_changed", "prefix": prefix}))


class RegistryToolTests(unittest.TestCase):
    """normalize and export against a disposable Git repository."""

    def setUp(self) -> None:
        base_value = os.environ.get("MANGA_ANIME_TEST_TMP")
        if not base_value:
            self.skipTest("MANGA_ANIME_TEST_TMP is not set")
        base = Path(base_value).resolve(strict=True)
        self.root = Path(tempfile.mkdtemp(prefix="registry-partitions-", dir=base)).resolve(strict=True)
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

    def commit(self, message: str) -> str:
        self.git("add", "--all", "--", "characters")
        self.git("commit", "--quiet", "-m", message)
        return self.git("rev-parse", "HEAD")

    def test_migration_moves_rows_byte_for_byte_and_export_is_unchanged(self) -> None:
        other = record("other:carol@anime", entity_id="other:carol", series_id="other")
        # Unsorted keys and order prove that rows are moved, never re-serialized.
        raw_bob = json.dumps(bob(), separators=(",", ":")).encode() + b"\n"
        legacy = raw_bob + line(other) + line(record("example:alice@anime"))
        self.write("characters/registry.jsonl", legacy)
        before = self.commit("single file")
        changed = normalize(self.root)
        self.assertEqual(
            changed,
            [
                "characters/registry.jsonl",
                "characters/registry/example.jsonl",
                "characters/registry/other.jsonl",
            ],
        )
        self.assertFalse((self.root / "characters/registry.jsonl").exists())
        self.assertEqual(
            (self.root / "characters/registry/example.jsonl").read_bytes(),
            line(record("example:alice@anime")) + raw_bob,
        )
        self.assertEqual(normalize(self.root), [])
        self.assertEqual(
            unstaged_registry_paths(self.root),
            [
                "characters/registry.jsonl",
                "characters/registry/example.jsonl",
                "characters/registry/other.jsonl",
            ],
        )
        after = self.commit("partitions")
        self.assertEqual(unstaged_registry_paths(self.root), [])
        self.assertEqual(
            sorted((self.root / "characters/registry/example.jsonl").read_bytes().splitlines()
                   + (self.root / "characters/registry/other.jsonl").read_bytes().splitlines()),
            sorted(legacy.splitlines()),
        )
        self.assertEqual(
            export(discovery_commit_snapshot(self.root, before)),
            export(discovery_commit_snapshot(self.root, after)),
        )
        selected = discovery_commit_snapshot(self.root, after)
        self.assertEqual(
            sorted(selected.entries),
            ["characters/registry/example.jsonl", "characters/registry/other.jsonl"],
        )
        self.assertEqual(read_discovery_registry(selected).layout_errors, ())

    def test_normalize_moves_misplaced_rows_and_deletes_emptied_partitions(self) -> None:
        self.write("characters/registry/example.jsonl", line(bob()))
        self.write("characters/registry/stray.jsonl", line(record("example:alice@anime")))
        self.assertEqual(
            normalize(self.root),
            ["characters/registry/example.jsonl", "characters/registry/stray.jsonl"],
        )
        self.assertFalse((self.root / "characters/registry/stray.jsonl").exists())
        self.assertEqual(
            (self.root / "characters/registry/example.jsonl").read_bytes(),
            line(record("example:alice@anime")) + line(bob()),
        )

    def test_replay_carries_branch_curation_across_the_migration(self) -> None:
        alice, carol = record("example:alice@anime"), record(
            "other:carol@anime", entity_id="other:carol", series_id="other"
        )
        revised_bob = bob()
        revised_bob["notes"] = "Revised on the branch."
        self.write("characters/registry.jsonl", line(alice) + line(bob()))
        base = self.commit("merge base")
        # The pre-migration branch revises Bob and enrolls Carol in the single file.
        self.write("characters/registry.jsonl", line(alice) + line(revised_bob) + line(carol))
        head = self.commit("pending curation")
        # Main meanwhile migrated, and separately revised Alice.
        revised_alice = record("example:alice@anime")
        revised_alice["notes"] = "Revised on main."
        (self.root / "characters/registry.jsonl").unlink()
        self.write("characters/registry/example.jsonl", line(revised_alice) + line(bob()))
        self.assertEqual(
            replay(self.root, base, head),
            ["characters/registry/example.jsonl", "characters/registry/other.jsonl"],
        )
        self.assertEqual(
            (self.root / "characters/registry/example.jsonl").read_bytes(),
            line(revised_alice) + line(revised_bob),
        )
        self.assertEqual((self.root / "characters/registry/other.jsonl").read_bytes(), line(carol))
        self.assertEqual(replay(self.root, base, head), [])

        # A row both sides changed stops the run before anything is written.
        main_bob = bob()
        main_bob["notes"] = "Revised on main."
        self.write("characters/registry/example.jsonl", line(revised_alice) + line(main_bob))
        before = (self.root / "characters/registry/example.jsonl").read_bytes()
        with self.assertRaisesRegex(DomainError, "example:bob@anime"):
            replay(self.root, base, head)
        self.assertEqual((self.root / "characters/registry/example.jsonl").read_bytes(), before)

    def test_staging_report_covers_edits_normalization_leaves_untouched(self) -> None:
        self.write("characters/registry/example.jsonl", line(record("example:alice@anime")) + line(bob()))
        self.commit("partition")
        # A row revised in place keeps its order, so normalization rewrites nothing.
        revised = bob()
        revised["notes"] = "Revised in place."
        self.write("characters/registry/example.jsonl", line(record("example:alice@anime")) + line(revised))
        # A new partition written already sorted needs no rewriting either.
        self.write(
            "characters/registry/other.jsonl",
            line(record("other:carol@anime", entity_id="other:carol", series_id="other")),
        )
        self.assertEqual(normalize(self.root), [])
        self.assertEqual(
            unstaged_registry_paths(self.root),
            ["characters/registry/example.jsonl", "characters/registry/other.jsonl"],
        )
        self.git("add", "--", "characters/registry/example.jsonl")
        self.assertEqual(unstaged_registry_paths(self.root), ["characters/registry/other.jsonl"])

    def test_writers_refuse_symlinked_managed_directories(self) -> None:
        outside = Path(tempfile.mkdtemp(prefix="registry-outside-", dir=self.root.parent))
        self.addCleanup(shutil.rmtree, outside)
        sentinel = outside / "unrelated.jsonl"
        sentinel.write_bytes(line(record("example:alice@anime")))
        (self.root / "characters").mkdir()
        for prefix, run in (
            ("registry", lambda: normalize(self.root)),
            ("index", lambda: write_outputs(
                self.root,
                GitSnapshot(self.root, "TEST", {}),
                {"CHARACTER_ANALYSIS_INDEX.md": "# Index\n", "characters/index/example.md": "# Page\n"},
            )),
        ):
            with self.subTest(prefix=prefix):
                link = self.root / "characters" / prefix
                link.symlink_to(outside, target_is_directory=True)
                with self.assertRaisesRegex(DomainError, "symlink"):
                    run()
                link.unlink()
                self.assertEqual(sorted(item.name for item in outside.iterdir()), ["unrelated.jsonl"])
                self.assertEqual(sentinel.read_bytes(), line(record("example:alice@anime")))
        self.assertFalse((self.root / "CHARACTER_ANALYSIS_INDEX.md").exists())

    def test_pre_migration_branch_merges_identical_rows_and_refuses_conflicts(self) -> None:
        alice = line(record("example:alice@anime"))
        # A branch that kept its single file beside main's partitions after a merge.
        self.write("characters/registry/example.jsonl", alice)
        self.write("characters/registry.jsonl", alice + line(bob()))
        self.assertEqual(
            normalize(self.root),
            ["characters/registry.jsonl", "characters/registry/example.jsonl"],
        )
        self.assertEqual(
            (self.root / "characters/registry/example.jsonl").read_bytes(), alice + line(bob())
        )
        revised = record("example:alice@anime")
        revised["notes"] = "Revised on the branch."
        self.write("characters/registry.jsonl", line(revised))
        with self.assertRaisesRegex(DomainError, "conflicting rows"):
            normalize(self.root)
        # Nothing is written or removed when a conflict stops the run.
        self.assertTrue((self.root / "characters/registry.jsonl").exists())
        self.assertEqual(
            (self.root / "characters/registry/example.jsonl").read_bytes(), alice + line(bob())
        )


if __name__ == "__main__":
    unittest.main()
