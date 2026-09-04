from __future__ import annotations

import json
import os
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
        write_json(
            root / "series/registry.json",
            {
                "schema": "anime-manga-ln-games-analysis/series-registry/v2",
                "status": "TEST",
                "series": [],
            },
        )
        write_json(
            root / "studies/registry.json",
            {
                "schema": "anime-manga-ln-games-analysis/study-registry/v1",
                "status": "TEST",
                "studies": [],
            },
        )
        (root / "characters").mkdir(parents=True)
        (root / "characters/registry.jsonl").write_text("", encoding="utf-8")
        return root

    def test_series_inputs_upsert_only_global_registry_outputs(self) -> None:
        with self.temporary() as temporary:
            root = self.root(temporary)
            descriptor = {
                "series_id": "example-series",
                "stable_slug": "example-series",
                "canonical_title": "Example Series",
                "media": ["ANIME"],
                "repository_path": "series/example-series/",
                "canonical_entrypoint": "series/example-series/CURRENT_STATE_AND_CORPUS_MAP.md",
                "canonical_entrypoint_status": "PRESENT_VERIFIED",
                "materialization_status": "PRESENT_REVIEWED",
                "migration_scope": "GIT_NATIVE_POST_CUTOVER_TEST",
                "authority_status": "GIT_PRIMARY",
            }
            write_json(
                root / "series/example-series/.repository/series-registry.json",
                descriptor,
            )
            character = {
                "analysis_subject_id": "example-series:alice@anime",
                "series_id": "example-series",
                "evidence": [
                    {
                        "repository_path": "series/example-series/Characters/ALICE.md"
                    }
                ],
            }
            source = root / "series/example-series/.repository/character-registry-upserts.jsonl"
            source.write_bytes(
                (json.dumps(character, separators=(",", ":")) + "\n").encode("utf-8")
            )

            outputs = synchronize(root, "series/example-series")
            self.assertEqual(set(outputs), {"series/registry.json", "characters/registry.jsonl"})
            rendered_series = json.loads(outputs["series/registry.json"])
            self.assertEqual(rendered_series["series"], [descriptor])
            rendered_characters = [
                json.loads(line)
                for line in outputs["characters/registry.jsonl"].splitlines()
                if line
            ]
            self.assertEqual(rendered_characters, [character])

    def test_new_root_without_descriptor_fails_closed(self) -> None:
        with self.temporary() as temporary:
            root = self.root(temporary)
            with self.assertRaisesRegex(DomainError, "requires declarative input"):
                synchronize(root, "series/unregistered")

    def test_character_upsert_cannot_cross_series_boundary(self) -> None:
        with self.temporary() as temporary:
            root = self.root(temporary)
            descriptor = {
                "series_id": "example-series",
                "stable_slug": "example-series",
                "repository_path": "series/example-series/",
            }
            write_json(
                root / "series/example-series/.repository/series-registry.json",
                descriptor,
            )
            source = root / "series/example-series/.repository/character-registry-upserts.jsonl"
            source.write_bytes(
                (
                    json.dumps(
                    {
                        "analysis_subject_id": "example-series:alice@anime",
                        "series_id": "example-series",
                        "evidence": [
                            {"repository_path": "series/another-series/ALICE.md"}
                        ],
                    },
                        separators=(",", ":"),
                    )
                    + "\n"
                ).encode("utf-8")
            )
            with self.assertRaisesRegex(DomainError, "automated evidence must remain"):
                synchronize(root, "series/example-series")

    def test_branch_parser_rejects_cross_cutting_and_nested_names(self) -> None:
        with self.temporary() as temporary:
            root = self.root(temporary)
            for branch in ("main", "codex/test", "series/foo/extra", "series/Foo"):
                with self.subTest(branch=branch):
                    with self.assertRaisesRegex(DomainError, "branch must be exactly"):
                        synchronize(root, branch)


if __name__ == "__main__":
    unittest.main()
