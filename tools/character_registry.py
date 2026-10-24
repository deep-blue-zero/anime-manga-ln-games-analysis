#!/usr/bin/env python3
"""Place, replay and export rows of the partitioned character discovery registry.

``normalize`` moves every worktree row, byte for byte, into the partition its
namespace names and orders each partition by ASCII ``analysis_subject_id``. It
also migrates the retired single-file registry, collapsing byte-identical
copies of a row and refusing differing ones.

``replay`` carries a branch's pending curation across the partition
migration: it applies to the worktree partitions exactly the rows that changed
between two commits, in either layout, and stops on any row that also changed
in the worktree since the first commit.

``export`` prints the logical registry of a snapshot in either layout as one
JSONL stream in ASCII ``analysis_subject_id`` order. The output is a view for
consumers and comparisons, never a second tracked copy.

None of these edits a row; the repository validator decides whether rows are
valid.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path, PurePosixPath

from character_index_core import (
    DISCOVERY_REGISTRY_PREFIX,
    LEGACY_DISCOVERY_REGISTRY_PATH,
    DomainError,
    GitSnapshot,
    atomic_write_text,
    decode_jsonl_with_lines,
    discovery_commit_snapshot,
    discovery_partition_path,
    managed_worktree_directory,
    record_namespace,
    run_git,
)


def _rows(data: bytes, label: str) -> list[tuple[str, bytes]]:
    """Return (analysis_subject_id, exact line bytes) for each nonblank row."""

    lines = data.split(b"\n")
    rows: list[tuple[str, bytes]] = []
    for line_number, record in decode_jsonl_with_lines(data, label):
        subject_id = record.get("analysis_subject_id")
        if not isinstance(subject_id, str):
            raise DomainError(f"{label}:{line_number}: row has no analysis_subject_id")
        namespace = record_namespace(record)
        if namespace is None:
            raise DomainError(f"{label}:{line_number}: row has no valid character_entity_id")
        if subject_id.split(":", 1)[0] != namespace:
            raise DomainError(
                f"{label}:{line_number}: analysis_subject_id and character_entity_id name different namespaces"
            )
        rows.append((subject_id, lines[line_number - 1]))
    return rows


def _row_map(sources: dict[str, bytes], label: str, *, collapse: bool) -> dict[str, bytes]:
    """Map each subject to its row; identical copies collapse only when asked."""

    rows: dict[str, bytes] = {}
    for path in sorted(sources, key=lambda item: item.encode("utf-8")):
        for subject_id, raw in _rows(sources[path], f"{label}:{path}"):
            if subject_id in rows and not (collapse and rows[subject_id] == raw):
                if collapse:
                    raise DomainError(
                        f"{label}:{path}: conflicting rows for analysis_subject_id "
                        f"{subject_id}; reconcile them by hand"
                    )
                raise DomainError(f"{label}:{path}: duplicate analysis_subject_id {subject_id}")
            rows[subject_id] = raw
    return rows


def _snapshot_sources(snapshot: GitSnapshot) -> dict[str, bytes]:
    paths = [
        path
        for path in snapshot.entries
        if path == LEGACY_DISCOVERY_REGISTRY_PATH or path.startswith(DISCOVERY_REGISTRY_PREFIX)
    ]
    if LEGACY_DISCOVERY_REGISTRY_PATH in paths and len(paths) > 1:
        raise DomainError(
            f"{snapshot.identity}: the retired {LEGACY_DISCOVERY_REGISTRY_PATH} and "
            f"{DISCOVERY_REGISTRY_PREFIX} partitions cannot coexist"
        )
    return {path: snapshot.entries[path].data for path in paths}


def _worktree_sources(root: Path) -> dict[str, bytes]:
    sources: dict[str, bytes] = {}
    directory = managed_worktree_directory(root, DISCOVERY_REGISTRY_PREFIX)
    legacy = root.joinpath(*PurePosixPath(LEGACY_DISCOVERY_REGISTRY_PATH).parts)
    if legacy.is_symlink():
        raise DomainError(f"refusing to read or remove a symlinked {LEGACY_DISCOVERY_REGISTRY_PATH}")
    if legacy.is_file():
        sources[LEGACY_DISCOVERY_REGISTRY_PATH] = legacy.read_bytes()
    if directory.is_dir():
        for item in sorted(directory.iterdir()):
            path = DISCOVERY_REGISTRY_PREFIX + item.name
            if not item.is_file() or item.is_symlink() or not item.name.endswith(".jsonl"):
                raise DomainError(f"unexpected entry in the discovery registry: {path}")
            sources[path] = item.read_bytes()
    return sources


def _write(root: Path, sources: dict[str, bytes], rows: dict[str, bytes]) -> list[str]:
    """Write rows as canonical partitions; remove every other source; return paths to stage."""

    placed: dict[str, list[str]] = {}
    for subject_id in rows:
        placed.setdefault(discovery_partition_path(subject_id.split(":", 1)[0]), []).append(subject_id)
    rendered = {
        path: b"".join(
            rows[subject_id] + b"\n"
            for subject_id in sorted(subjects, key=lambda item: item.encode("utf-8"))
        )
        for path, subjects in placed.items()
    }
    changed: list[str] = []
    for path in sorted(rendered, key=lambda item: item.encode("utf-8")):
        if sources.get(path) == rendered[path]:
            continue
        target = root.joinpath(*PurePosixPath(path).parts)
        target.parent.mkdir(parents=True, exist_ok=True)
        atomic_write_text(target, rendered[path].decode("utf-8"))
        changed.append(path)
    # Emptied partitions and the retired single file are removed.
    for path in sorted(set(sources) - set(rendered), key=lambda item: item.encode("utf-8")):
        root.joinpath(*PurePosixPath(path).parts).unlink()
        changed.append(path)
    return sorted(changed, key=lambda item: item.encode("utf-8"))


def normalize(root: Path) -> list[str]:
    """Rewrite worktree partitions into canonical placement; return the paths to stage."""

    sources = _worktree_sources(root)
    return _write(root, sources, _row_map(sources, "worktree", collapse=True))


def replay(root: Path, base: str, head: str) -> list[str]:
    """Apply the rows changed from ``base`` to ``head`` to the worktree partitions.

    A row added, revised or removed between the commits is applied unless the
    worktree's row also changed since ``base``; any such conflict stops the run
    before anything is written.
    """

    sources = _worktree_sources(root)
    if LEGACY_DISCOVERY_REGISTRY_PATH in sources:
        raise DomainError(
            f"replay needs the partitioned layout; remove {LEGACY_DISCOVERY_REGISTRY_PATH} first"
        )
    current = _row_map(sources, "worktree", collapse=False)
    before = _row_map(_snapshot_sources(discovery_commit_snapshot(root, base)), base, collapse=False)
    after = _row_map(_snapshot_sources(discovery_commit_snapshot(root, head)), head, collapse=False)
    conflicts: list[str] = []
    for subject_id in sorted(set(before) | set(after), key=lambda item: item.encode("utf-8")):
        old, new, now = before.get(subject_id), after.get(subject_id), current.get(subject_id)
        if old == new or now == new:
            continue
        if now != old:
            conflicts.append(subject_id)
        elif new is None:
            del current[subject_id]
        else:
            current[subject_id] = new
    if conflicts:
        raise DomainError(
            "rows changed both on the replayed branch and in the worktree; reconcile them by hand: "
            + ", ".join(conflicts)
        )
    return _write(root, sources, current)


def export(snapshot: GitSnapshot) -> bytes:
    rows = _row_map(_snapshot_sources(snapshot), snapshot.identity, collapse=False)
    return b"".join(
        rows[subject_id] + b"\n" for subject_id in sorted(rows, key=lambda item: item.encode("utf-8"))
    )


def _commit(root: Path, revision: str) -> str:
    return run_git(root, "rev-parse", "--verify", "-q", f"{revision}^{{commit}}").decode("ascii").strip()


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--repo", type=Path)
    commands = parser.add_subparsers(dest="command", required=True)
    commands.add_parser("normalize", help="place worktree rows in canonical partitions")
    replayer = commands.add_parser("replay", help="apply the rows changed between two commits")
    replayer.add_argument("--base", required=True, help="commit before the branch's curation")
    replayer.add_argument("--head", required=True, help="commit holding the branch's curation")
    exporter = commands.add_parser("export", help="print the logical registry as one JSONL stream")
    exporter.add_argument("--snapshot", choices=["worktree", "index", "commit"], default="index")
    exporter.add_argument("--commit")
    args = parser.parse_args()
    root = args.repo.resolve() if args.repo else Path(__file__).resolve().parents[1]
    if args.command in {"normalize", "replay"}:
        changed = (
            normalize(root)
            if args.command == "normalize"
            else replay(root, _commit(root, args.base), _commit(root, args.head))
        )
        for path in changed:
            print(f"registry path to stage: {path}")
        return 0
    if args.snapshot == "commit":
        if args.commit is None:
            raise DomainError("--commit is required with --snapshot commit")
        snapshot = discovery_commit_snapshot(root, _commit(root, args.commit))
    elif args.commit is not None:
        raise DomainError("--commit is valid only with --snapshot commit")
    elif args.snapshot == "index":
        snapshot = GitSnapshot.from_index(root)
    else:
        snapshot = GitSnapshot.from_worktree(root)
    sys.stdout.buffer.write(export(snapshot))
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except DomainError as exc:
        raise SystemExit(f"FAIL: {exc}") from exc
