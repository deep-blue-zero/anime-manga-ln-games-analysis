from __future__ import annotations

import json
import os
import re
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
        branch = os.environ.get("AUDIT_BRANCH", "")
        if os.environ.get("AUDIT_EVENT") == "push" and re.fullmatch(
            r"(series|studies)/[a-z0-9][a-z0-9-]*", branch
        ):
            # Author preflight validates projected routing without writing it.
            # Housekeeping, dispatch, main, and ordinary local tests stay strict.
            from analytical_preflight import routing_preflight

            cls.base_snapshot, _ = routing_preflight(cls.base_snapshot, branch)

    def snapshot(self) -> GitSnapshot:
        return self.base_snapshot

    def test_generated_repository_indexes_match_index(self) -> None:
        snapshot = self.snapshot()
        outputs = expected_outputs(snapshot)
        self.assertEqual(
            set(outputs),
            {
                "series/README.md",
                "studies/README.md",
                "governance/MANGA_ANIME_CORPUS_INDEX.md",
            },
        )
        for path, expected in outputs.items():
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
        snapshot = self.snapshot()
        obligations = json.loads(
            snapshot.entries[
                "governance/repository-controls/change-obligations.json"
            ].data
        )
        base = {"series/existing/README.md", "series/registry.json"}
        ordinary = base | {"series/existing/V42/new-analysis.md"}
        active = active_rules(obligations, {"series/existing/V42/new-analysis.md"}, base, ordinary)
        self.assertEqual(active, [])

        index = base | {"series/new-series/README.md"}
        active = active_rules(obligations, {"series/registry.json"}, base, index)
        self.assertEqual(
            [rule["id"] for rule in active],
            ["series-root-topology", "series-registry-routing"],
        )


if __name__ == "__main__":
    unittest.main()
