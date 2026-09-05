from __future__ import annotations

import json
import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


TOOLS = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(TOOLS))

from character_index_core import DomainError  # noqa: E402
from synchronize_global_registries import synchronize  # noqa: E402


def write_json(path: Path, value: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes((json.dumps(value, ensure_ascii=False, indent=2) + "\n").encode("utf-8"))


class GlobalIndexAutomationTests(unittest.TestCase):
    def temporary(self) -> tempfile.TemporaryDirectory[str]:
        base_value = os.environ.get("MANGA_ANIME_TEST_TMP")
        if not base_value:
            self.skipTest("MANGA_ANIME_TEST_TMP is not set")
        base = Path(base_value).resolve()
        if not base.is_absolute() or not base.is_dir():
            self.skipTest("MANGA_ANIME_TEST_TMP must name an existing absolute directory")
        return tempfile.TemporaryDirectory(dir=base)

    def root(self, temporary: str) -> Path:
        root = Path(temporary)
        for namespace in ("series", "studies"):
            write_json(root / namespace / "registry.json", {namespace: []})
        return root

    def descriptor(self, root: Path, namespace: str = "series") -> dict[str, str]:
        singular = "series" if namespace == "series" else "study"
        value = {
            f"{singular}_id": "example",
            "stable_slug": "example",
            "repository_path": f"{namespace}/example/",
        }
        write_json(
            root / namespace / "example/.repository" / f"{singular}-registry.json",
            value,
        )
        return value

    def test_series_routing_does_not_depend_on_character_files(self) -> None:
        with self.temporary() as temporary:
            root = self.root(temporary)
            descriptor = self.descriptor(root)
            self.assertFalse((root / "characters").exists())
            outputs = synchronize(root, "series/example")
            self.assertEqual(set(outputs), {"series/registry.json"})
            self.assertEqual(json.loads(outputs["series/registry.json"])["series"], [descriptor])
            self.assertFalse((root / "characters").exists())

    def test_legacy_character_proposals_are_never_replacement_inputs(self) -> None:
        with self.temporary() as temporary:
            root = self.root(temporary)
            self.descriptor(root)
            source = root / "series/example/.repository/character-registry-upserts.jsonl"
            proposals = (
                json.dumps({
                    "analysis_subject_id": "example:alice@anime",
                    "series_id": "example",
                    "evidence": [{"repository_path": "series/other/ALICE.md"}],
                }) + "\n",
                "malformed historical proposal\n",
            )
            for proposal in proposals:
                with self.subTest(proposal=proposal):
                    source.write_text(proposal, encoding="utf-8")
                    outputs = synchronize(root, "series/example")
                    self.assertEqual(set(outputs), {"series/registry.json"})
                    self.assertEqual(source.read_text(encoding="utf-8"), proposal)

    def test_write_and_check_preserve_character_bytes_and_proposals(self) -> None:
        with self.temporary() as temporary:
            root = self.root(temporary)
            self.descriptor(root)
            preserved = {
                "characters/registry.jsonl": b'{"unparsed": "agent-owned"}\r\n',
                "CHARACTER_ANALYSIS_INDEX.md": b"# Agent-owned index\n",
                "series/example/.repository/character-registry-upserts.jsonl":
                    b"malformed legacy proposal\n",
            }
            for name, data in preserved.items():
                path = root / name
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_bytes(data)
            for operation in ("--write", "--check"):
                result = subprocess.run(
                    [
                        sys.executable, str(TOOLS / "synchronize_global_registries.py"),
                        "--repo", str(root), "--branch", "series/example", operation,
                    ],
                    capture_output=True, text=True, check=False,
                )
                self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
                for name, data in preserved.items():
                    self.assertEqual((root / name).read_bytes(), data, name)

    def test_study_routing_remains_independent(self) -> None:
        with self.temporary() as temporary:
            root = self.root(temporary)
            descriptor = self.descriptor(root, "studies")
            outputs = synchronize(root, "studies/example")
            self.assertEqual(set(outputs), {"studies/registry.json"})
            self.assertEqual(json.loads(outputs["studies/registry.json"])["studies"], [descriptor])

    def test_existing_root_without_descriptor_preserves_registered_row(self) -> None:
        with self.temporary() as temporary:
            root = self.root(temporary)
            row = {"series_id": "example", "stable_slug": "example"}
            write_json(root / "series/registry.json", {"series": [row]})
            outputs = synchronize(root, "series/example")
            self.assertEqual(json.loads(outputs["series/registry.json"])["series"], [row])

    def test_new_root_without_descriptor_fails_closed(self) -> None:
        with self.temporary() as temporary:
            root = self.root(temporary)
            with self.assertRaisesRegex(DomainError, "requires declarative input"):
                synchronize(root, "series/unregistered")

    def test_routing_descriptor_cannot_cross_branch_boundary(self) -> None:
        with self.temporary() as temporary:
            root = self.root(temporary)
            descriptor = self.descriptor(root)
            descriptor["repository_path"] = "series/other/"
            write_json(root / "series/example/.repository/series-registry.json", descriptor)
            with self.assertRaisesRegex(DomainError, "repository_path must equal"):
                synchronize(root, "series/example")

    def test_branch_parser_rejects_cross_cutting_and_nested_names(self) -> None:
        with self.temporary() as temporary:
            root = self.root(temporary)
            for branch in ("main", "character-registry", "codex/test", "series/foo/extra", "series/Foo"):
                with self.subTest(branch=branch):
                    with self.assertRaisesRegex(DomainError, "branch must be exactly"):
                        synchronize(root, branch)


if __name__ == "__main__":
    unittest.main()
