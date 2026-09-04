from __future__ import annotations

import sys
import unittest
from pathlib import Path


TOOLS = Path(__file__).resolve().parents[1]
ROOT = TOOLS.parent
sys.path.insert(0, str(TOOLS))

from character_index_core import GitSnapshot, SnapshotEntry  # noqa: E402
from prepare_commit import active_rules  # noqa: E402
from update_repository_indexes import _snapshot, expected_outputs  # noqa: E402
from validate_repository import (  # noqa: E402
    validate_change_obligations,
    validate_registered_root_topology,
    validate_study_registry,
)


class RepositoryIndexTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.base_snapshot = _snapshot(ROOT, "index", None)

    def snapshot(self) -> GitSnapshot:
        return self.base_snapshot

    def test_generated_repository_indexes_match_index(self) -> None:
        snapshot = self.snapshot()
        for path, expected in expected_outputs(snapshot).items():
            self.assertEqual(snapshot.entries[path].data, expected, path)

    def test_registered_root_topology_is_bidirectional(self) -> None:
        snapshot = self.snapshot()
        self.assertEqual(validate_registered_root_topology(snapshot), [])
        entries = dict(snapshot.entries)
        path = "studies/unregistered-test/README.md"
        entries[path] = SnapshotEntry(path, "100644", b"# Unregistered\n")
        changed = GitSnapshot(ROOT, "UNREGISTERED_TEST", entries)
        self.assertIn(
            "unregistered studies root: studies/unregistered-test/",
            validate_registered_root_topology(changed),
        )

    def test_study_registry_and_obligation_map_are_valid(self) -> None:
        snapshot = self.snapshot()
        self.assertEqual(validate_study_registry(snapshot), [])
        self.assertEqual(validate_change_obligations(snapshot), [])

    def test_obligation_rules_detect_topology_and_registry_changes(self) -> None:
        obligations = {
            "rules": [
                {
                    "id": "paths",
                    "trigger": {"kind": "tracked_path_set_changed"},
                },
                {
                    "id": "series",
                    "trigger": {
                        "kind": "top_level_roots_changed",
                        "root": "series/",
                    },
                },
                {
                    "id": "registry",
                    "trigger": {
                        "kind": "path_changed",
                        "path": "series/registry.json",
                    },
                },
            ]
        }
        base = {"series/existing/README.md", "series/registry.json"}
        index = base | {"series/new-series/README.md"}
        active = active_rules(obligations, {"series/registry.json"}, base, index)
        self.assertEqual([rule["id"] for rule in active], ["paths", "series", "registry"])


if __name__ == "__main__":
    unittest.main()
