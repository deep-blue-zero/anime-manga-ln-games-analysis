#!/usr/bin/env python3
"""Place, replay and export records of the partitioned capability registry.

The reconstruction capability registry is one logical registry stored as one
JSONL file per analysis subject, ``characters/reconstruction_capabilities/
<namespace>/<subject>.jsonl``, each ordered by ASCII ``assessment_id``.

``normalize`` moves every worktree record, byte for byte, into the file its
``analysis_subject_id`` names and orders each file. It also migrates the
retired single-file registry, collapsing byte-identical copies of a record and
refusing differing ones.

``replay`` carries a branch's pending assessments across the partition
migration: it applies to the worktree partitions exactly the records that
changed between two commits, in either layout, and stops on any record that
also changed in the worktree since the first commit.

``export`` prints the logical registry of a snapshot in either layout as one
JSONL stream in ASCII ``assessment_id`` order, the order the retired single file
kept. The output is a view for consumers and comparisons, never a second
tracked copy.

After ``normalize`` or ``replay`` the command lists every registry path whose
worktree differs from the Git index, which is the complete list to stage.

None of these edits a record; the repository validator decides whether records
are valid.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path, PurePosixPath

from character_index_core import (
    LEGACY_RECONSTRUCTION_REGISTRY_PATH,
    RECONSTRUCTION_REGISTRY_PREFIX,
    SUBJECT_ID_RE,
    DomainError,
    GitSnapshot,
    atomic_write_text,
    decode_jsonl_with_lines,
    managed_worktree_directory,
    reconstruction_commit_snapshot,
    reconstruction_partition_path,
    run_git,
)


def _records(data: bytes, label: str) -> list[tuple[str, str, bytes]]:
    """Return (assessment_id, analysis_subject_id, exact line bytes) for each nonblank row."""

    lines = data.split(b"\n")
    records: list[tuple[str, str, bytes]] = []
    for line_number, record in decode_jsonl_with_lines(data, label):
        assessment_id = record.get("assessment_id")
        if not isinstance(assessment_id, str) or not assessment_id:
            raise DomainError(f"{label}:{line_number}: record has no assessment_id")
        subject_id = record.get("analysis_subject_id")
        if not isinstance(subject_id, str) or not SUBJECT_ID_RE.fullmatch(subject_id):
            raise DomainError(f"{label}:{line_number}: record has no valid analysis_subject_id")
        records.append((assessment_id, subject_id, lines[line_number - 1]))
    return records


def _record_map(
    sources: dict[str, bytes], label: str, *, collapse: bool
) -> dict[str, tuple[str, bytes]]:
    """Map each assessment_id to (subject, row); identical copies collapse only when asked."""

    records: dict[str, tuple[str, bytes]] = {}
    for path in sorted(sources, key=lambda item: item.encode("utf-8")):
        for assessment_id, subject_id, raw in _records(sources[path], f"{label}:{path}"):
            if assessment_id in records and not (collapse and records[assessment_id][1] == raw):
                if collapse:
                    raise DomainError(
                        f"{label}:{path}: conflicting records for assessment_id "
                        f"{assessment_id}; reconcile them by hand"
                    )
                raise DomainError(f"{label}:{path}: duplicate assessment_id {assessment_id}")
            records[assessment_id] = (subject_id, raw)
    return records


def _snapshot_sources(snapshot: GitSnapshot) -> dict[str, bytes]:
    paths = [
        path
        for path in snapshot.entries
        if path == LEGACY_RECONSTRUCTION_REGISTRY_PATH
        or path.startswith(RECONSTRUCTION_REGISTRY_PREFIX)
    ]
    if LEGACY_RECONSTRUCTION_REGISTRY_PATH in paths and len(paths) > 1:
        raise DomainError(
            f"{snapshot.identity}: the retired {LEGACY_RECONSTRUCTION_REGISTRY_PATH} and "
            f"{RECONSTRUCTION_REGISTRY_PREFIX} partitions cannot coexist"
        )
    return {path: snapshot.entries[path].data for path in paths}


def _worktree_sources(root: Path) -> dict[str, bytes]:
    sources: dict[str, bytes] = {}
    directory = managed_worktree_directory(root, RECONSTRUCTION_REGISTRY_PREFIX)
    legacy = root.joinpath(*PurePosixPath(LEGACY_RECONSTRUCTION_REGISTRY_PATH).parts)
    if legacy.is_symlink():
        raise DomainError(
            f"refusing to read or remove a symlinked {LEGACY_RECONSTRUCTION_REGISTRY_PATH}"
        )
    if legacy.is_file():
        sources[LEGACY_RECONSTRUCTION_REGISTRY_PATH] = legacy.read_bytes()
    if directory.is_dir():
        for namespace_directory in sorted(directory.iterdir()):
            namespace_path = RECONSTRUCTION_REGISTRY_PREFIX + namespace_directory.name
            if namespace_directory.is_symlink() or not namespace_directory.is_dir():
                raise DomainError(f"unexpected entry in the capability registry: {namespace_path}")
            for item in sorted(namespace_directory.iterdir()):
                path = f"{namespace_path}/{item.name}"
                if not item.is_file() or item.is_symlink() or not item.name.endswith(".jsonl"):
                    raise DomainError(f"unexpected entry in the capability registry: {path}")
                sources[path] = item.read_bytes()
    return sources


def _write(root: Path, sources: dict[str, bytes], records: dict[str, tuple[str, bytes]]) -> list[str]:
    """Write records as canonical partitions; remove every other source; return paths to stage."""

    placed: dict[str, list[str]] = {}
    for assessment_id, (subject_id, _raw) in records.items():
        placed.setdefault(reconstruction_partition_path(subject_id), []).append(assessment_id)
    rendered = {
        path: b"".join(
            records[assessment_id][1] + b"\n"
            for assessment_id in sorted(identifiers, key=lambda item: item.encode("utf-8"))
        )
        for path, identifiers in placed.items()
    }
    changed: list[str] = []
    for path in sorted(rendered, key=lambda item: item.encode("utf-8")):
        if sources.get(path) == rendered[path]:
            continue
        target = root.joinpath(*PurePosixPath(path).parts)
        target.parent.mkdir(parents=True, exist_ok=True)
        atomic_write_text(target, rendered[path].decode("utf-8"))
        changed.append(path)
    # Emptied partitions and the retired single file are removed, then any
    # namespace directory left empty.
    for path in sorted(set(sources) - set(rendered), key=lambda item: item.encode("utf-8")):
        target = root.joinpath(*PurePosixPath(path).parts)
        target.unlink()
        changed.append(path)
        parent = target.parent
        if path.startswith(RECONSTRUCTION_REGISTRY_PREFIX) and parent.is_dir() and not any(parent.iterdir()):
            parent.rmdir()
    return sorted(changed, key=lambda item: item.encode("utf-8"))


def normalize(root: Path) -> list[str]:
    """Rewrite worktree partitions into canonical placement; return the paths to stage."""

    sources = _worktree_sources(root)
    return _write(root, sources, _record_map(sources, "worktree", collapse=True))


def replay(root: Path, base: str, head: str) -> list[str]:
    """Apply the records changed from ``base`` to ``head`` to the worktree partitions.

    A record added, revised or removed between the commits is applied unless the
    worktree's record also changed since ``base``; any such conflict stops the
    run before anything is written.
    """

    sources = _worktree_sources(root)
    if LEGACY_RECONSTRUCTION_REGISTRY_PATH in sources:
        raise DomainError(
            f"replay needs the partitioned layout; remove {LEGACY_RECONSTRUCTION_REGISTRY_PATH} first"
        )
    current = _record_map(sources, "worktree", collapse=False)
    before = _record_map(
        _snapshot_sources(reconstruction_commit_snapshot(root, base)), base, collapse=False
    )
    after = _record_map(
        _snapshot_sources(reconstruction_commit_snapshot(root, head)), head, collapse=False
    )
    conflicts: list[str] = []
    for assessment_id in sorted(set(before) | set(after), key=lambda item: item.encode("utf-8")):
        old, new, now = before.get(assessment_id), after.get(assessment_id), current.get(assessment_id)
        if old == new or now == new:
            continue
        if now != old:
            conflicts.append(assessment_id)
        elif new is None:
            del current[assessment_id]
        else:
            current[assessment_id] = new
    if conflicts:
        raise DomainError(
            "records changed both on the replayed branch and in the worktree; reconcile them by hand: "
            + ", ".join(conflicts)
        )
    return _write(root, sources, current)


def unstaged_registry_paths(root: Path) -> list[str]:
    """Registry paths whose worktree state differs from the Git index.

    This is the staging list after ``normalize`` or ``replay``: it includes a
    record revised in place and a new partition written already sorted, which
    the normalization report alone omits, and the retired single file once
    removed.
    """

    pathspecs = [
        "--",
        LEGACY_RECONSTRUCTION_REGISTRY_PATH,
        RECONSTRUCTION_REGISTRY_PREFIX.rstrip("/"),
    ]
    modified = run_git(root, "--literal-pathspecs", "diff", "--name-only", "-z", *pathspecs)
    untracked = run_git(
        root, "--literal-pathspecs", "ls-files", "--others", "--exclude-standard", "-z", *pathspecs
    )
    paths = {
        item.decode("utf-8", "strict")
        for raw in (modified, untracked)
        for item in raw.split(b"\0")
        if item
    }
    return sorted(paths, key=lambda item: item.encode("utf-8"))


def export(snapshot: GitSnapshot) -> bytes:
    records = _record_map(_snapshot_sources(snapshot), snapshot.identity, collapse=False)
    return b"".join(
        records[assessment_id][1] + b"\n"
        for assessment_id in sorted(records, key=lambda item: item.encode("utf-8"))
    )


def _commit(root: Path, revision: str) -> str:
    return run_git(root, "rev-parse", "--verify", "-q", f"{revision}^{{commit}}").decode("ascii").strip()


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--repo", type=Path)
    commands = parser.add_subparsers(dest="command", required=True)
    commands.add_parser("normalize", help="place worktree records in canonical partitions")
    replayer = commands.add_parser("replay", help="apply the records changed between two commits")
    replayer.add_argument("--base", required=True, help="commit before the branch's assessments")
    replayer.add_argument("--head", required=True, help="commit holding the branch's assessments")
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
            print(f"rewritten: {path}")
        for path in unstaged_registry_paths(root):
            print(f"registry path to stage: {path}")
        return 0
    if args.snapshot == "commit":
        if args.commit is None:
            raise DomainError("--commit is required with --snapshot commit")
        snapshot = reconstruction_commit_snapshot(root, _commit(root, args.commit))
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
