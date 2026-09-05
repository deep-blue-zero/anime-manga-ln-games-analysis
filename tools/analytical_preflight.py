#!/usr/bin/env python3
"""Read-only routing projection for analytical author preflight.

Only housekeeping's five outputs can differ from the source snapshot. Character
discovery, analytical prose, and authority fields are never generated here.
"""
from __future__ import annotations

from character_index_core import DomainError, GitSnapshot, SnapshotEntry
from synchronize_global_registries import synchronize_snapshot
from update_repository_indexes import expected_outputs

ROUTING_OUTPUTS = frozenset({
    "series/registry.json", "studies/registry.json", "series/README.md",
    "studies/README.md", "governance/MANGA_ANIME_CORPUS_INDEX.md",
})


def routing_preflight(snapshot: GitSnapshot, branch: str) -> tuple[GitSnapshot, list[str]]:
    entries = dict(snapshot.entries)
    outputs = {
        path: text.encode("utf-8")
        for path, text in synchronize_snapshot(snapshot, branch).items()
    }

    def apply(values: dict[str, bytes]) -> None:
        for path, data in values.items():
            if path not in ROUTING_OUTPUTS:
                raise DomainError(f"preflight attempted a prohibited output: {path}")
            original = snapshot.get(path)
            if original is None or not original.qualifies_as_evidence:
                raise DomainError(f"preflight cannot replace missing or nonregular output: {path}")
            entries[path] = SnapshotEntry(path, original.mode, data, original.tracked)

    apply(outputs)
    projected = GitSnapshot(snapshot.root, snapshot.identity, entries)
    catalogs = expected_outputs(projected)
    apply(catalogs)
    deferred = sorted(
        path for path in ROUTING_OUTPUTS
        if entries[path].data != snapshot.entries[path].data
    )
    return GitSnapshot(snapshot.root, snapshot.identity, entries), deferred
