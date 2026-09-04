#!/usr/bin/env python3
"""Deterministically render global repository catalogs and the tracked-path manifest."""

from __future__ import annotations

import argparse
import re
from pathlib import Path
from typing import Any, Mapping

from character_index_core import (
    DomainError,
    GitSnapshot,
    SnapshotEntry,
    atomic_write_text,
    decode_json,
    run_git,
)


CURRENT_MANIFEST = "governance/repository-controls/CURRENT_TRACKED_PATHS.txt"
SERIES_REGISTRY = "series/registry.json"
STUDY_REGISTRY = "studies/registry.json"
CHANGE_OBLIGATIONS = "governance/repository-controls/change-obligations.json"
SERIES_README = "series/README.md"
STUDIES_README = "studies/README.md"
CORPUS_INDEX = "governance/MANGA_ANIME_CORPUS_INDEX.md"
SERIES_SCHEMA = "anime-manga-ln-games-analysis/series-registry/v2"
STUDY_SCHEMA = "anime-manga-ln-games-analysis/study-registry/v1"

SERIES_README_MARKERS = (
    "<!-- BEGIN GENERATED SERIES CATALOG -->",
    "<!-- END GENERATED SERIES CATALOG -->",
)
STUDIES_README_MARKERS = (
    "<!-- BEGIN GENERATED STUDY CATALOG -->",
    "<!-- END GENERATED STUDY CATALOG -->",
)
CORPUS_SERIES_MARKERS = (
    "<!-- BEGIN GENERATED CORPUS SERIES CATALOG -->",
    "<!-- END GENERATED CORPUS SERIES CATALOG -->",
)
CORPUS_STUDY_MARKERS = (
    "<!-- BEGIN GENERATED CORPUS STUDY CATALOG -->",
    "<!-- END GENERATED CORPUS STUDY CATALOG -->",
)
CONTENT_PATHS = {
    CURRENT_MANIFEST,
    SERIES_REGISTRY,
    STUDY_REGISTRY,
    SERIES_README,
    STUDIES_README,
    CORPUS_INDEX,
    CHANGE_OBLIGATIONS,
}


def _registry_entrypoints(entries: Mapping[str, SnapshotEntry]) -> set[str]:
    paths = set()
    for registry_path, key in (
        (SERIES_REGISTRY, "series"),
        (STUDY_REGISTRY, "studies"),
    ):
        entry = entries.get(registry_path)
        if entry is None or not entry.data:
            continue
        document = decode_json(entry.data, registry_path)
        if not isinstance(document, Mapping) or not isinstance(document.get(key), list):
            continue
        for row in document[key]:
            if isinstance(row, Mapping) and isinstance(row.get("canonical_entrypoint"), str):
                paths.add(row["canonical_entrypoint"])
    return paths


def _entries_from_index(root: Path) -> dict[str, SnapshotEntry]:
    entries: dict[str, SnapshotEntry] = {}
    raw = run_git(root, "ls-files", "--stage", "-z")
    for item in raw.split(b"\0"):
        if not item:
            continue
        metadata, raw_path = item.split(b"\t", 1)
        mode, _oid, stage = metadata.decode("ascii").split(" ")
        path = raw_path.decode("utf-8", "strict")
        if stage != "0":
            raise DomainError(f"unmerged index entry: {path}")
        data = run_git(root, "show", f":{path}") if path in CONTENT_PATHS else b""
        entries[path] = SnapshotEntry(path, mode, data)
    for path in _registry_entrypoints(entries):
        if path in entries:
            entry = entries[path]
            entries[path] = SnapshotEntry(path, entry.mode, run_git(root, "show", f":{path}"))
    return entries


def _entries_from_commit(root: Path, commit: str) -> dict[str, SnapshotEntry]:
    object_format = run_git(root, "rev-parse", "--show-object-format").decode().strip()
    length = 40 if object_format == "sha1" else 64 if object_format == "sha256" else 0
    if not re.fullmatch(rf"[0-9a-f]{{{length}}}", commit):
        raise DomainError("basis commit must be a full lower-case object ID")
    if run_git(root, "cat-file", "-t", commit).decode().strip() != "commit":
        raise DomainError("basis object is not a commit")
    entries: dict[str, SnapshotEntry] = {}
    raw = run_git(root, "ls-tree", "-r", "-z", "--full-tree", commit)
    for item in raw.split(b"\0"):
        if not item:
            continue
        metadata, raw_path = item.split(b"\t", 1)
        mode, kind, _oid = metadata.decode("ascii").split(" ")
        path = raw_path.decode("utf-8", "strict")
        data = run_git(root, "show", f"{commit}:{path}") if path in CONTENT_PATHS else b""
        entries[path] = SnapshotEntry(path, mode, data, tracked=kind == "blob")
    for path in _registry_entrypoints(entries):
        if path in entries:
            entry = entries[path]
            entries[path] = SnapshotEntry(
                path,
                entry.mode,
                run_git(root, "show", f"{commit}:{path}"),
                tracked=entry.tracked,
            )
    return entries


def _snapshot(root: Path, mode: str, commit: str | None) -> GitSnapshot:
    if mode == "commit":
        if commit is None:
            raise DomainError("--commit is required with --snapshot commit")
        return GitSnapshot(root, commit, _entries_from_commit(root, commit))
    if commit is not None:
        raise DomainError("--commit is valid only with --snapshot commit")
    if mode == "index":
        return GitSnapshot(root, "INDEX", _entries_from_index(root))
    manifest = root / CURRENT_MANIFEST
    paths = [line for line in manifest.read_text(encoding="utf-8").splitlines() if line]
    modes: dict[str, str] = {}
    raw = run_git(root, "ls-files", "--stage", "-z")
    for item in raw.split(b"\0"):
        if not item:
            continue
        metadata, raw_path = item.split(b"\t", 1)
        git_mode, _oid, stage = metadata.decode("ascii").split(" ")
        if stage == "0":
            modes[raw_path.decode("utf-8", "strict")] = git_mode
    entries = {}
    for path in paths:
        full = root.joinpath(*path.split("/"))
        data = full.read_bytes() if path in CONTENT_PATHS and full.is_file() else b""
        entries[path] = SnapshotEntry(path, modes.get(path, "100644"), data, path in modes)
    for path in _registry_entrypoints(entries):
        if path in entries:
            entry = entries[path]
            full = root.joinpath(*path.split("/"))
            entries[path] = SnapshotEntry(
                path,
                entry.mode,
                full.read_bytes() if full.is_file() else b"",
                tracked=entry.tracked,
            )
    return GitSnapshot(root, "WORKTREE", entries)


def _registry_rows(
    snapshot: GitSnapshot, path: str, key: str, schema: str
) -> list[Mapping[str, Any]]:
    entry = snapshot.get(path)
    if entry is None or not entry.qualifies_as_evidence:
        raise DomainError(f"snapshot lacks required regular registry: {path}")
    document = decode_json(entry.data, f"{snapshot.identity}:{path}")
    if not isinstance(document, Mapping):
        raise DomainError(f"{path} must be a JSON object")
    if document.get("schema") != schema:
        raise DomainError(f"{path}.schema must equal {schema!r}")
    raw_rows = document.get(key)
    if not isinstance(raw_rows, list):
        raise DomainError(f"{path}.{key} must be an array")

    rows: list[Mapping[str, Any]] = []
    seen_slugs: set[str] = set()
    for index, row in enumerate(raw_rows):
        label = f"{path}:{key}[{index}]"
        if not isinstance(row, Mapping):
            raise DomainError(f"{label} must be an object")
        for field in ("stable_slug", "canonical_title", "repository_path"):
            value = row.get(field)
            if not isinstance(value, str) or not value or value != value.strip():
                raise DomainError(f"{label}.{field} must be a nonempty trimmed string")
        slug = str(row["stable_slug"])
        if slug in seen_slugs:
            raise DomainError(f"duplicate stable_slug in {path}: {slug!r}")
        seen_slugs.add(slug)
        note = row.get("catalog_note")
        if note is not None and (
            not isinstance(note, str) or not note or note != note.strip()
        ):
            raise DomainError(f"{label}.catalog_note must be a nonempty trimmed string")
        rows.append(row)
    return rows


def _root_rows(rows: list[Mapping[str, Any]], root: str) -> list[Mapping[str, Any]]:
    selected = []
    for row in rows:
        slug = str(row["stable_slug"])
        if row["repository_path"] == f"{root}{slug}/":
            selected.append(row)
    return sorted(
        selected,
        key=lambda row: (
            str(row["canonical_title"]).casefold().encode("utf-8"),
            str(row["canonical_title"]).encode("utf-8"),
            str(row["stable_slug"]).encode("utf-8"),
        ),
    )


def _label(value: str) -> str:
    return value.replace("\\", "\\\\").replace("[", "\\[").replace("]", "\\]")


def _note(row: Mapping[str, Any]) -> str:
    note = row.get("catalog_note")
    return f" — {note}" if isinstance(note, str) else ""


def render_series_readme(rows: list[Mapping[str, Any]]) -> str:
    migrated = [
        row
        for row in rows
        if not str(row.get("migration_scope", "")).startswith(
            "GIT_NATIVE_POST_CUTOVER_"
        )
    ]
    post_cutover = [row for row in rows if row not in migrated]
    lines = [
        "The final G7 materialization and sealed epoch-1 migration scope contain these series roots:",
        "",
    ]
    for row in migrated:
        slug = str(row["stable_slug"])
        lines.append(
            f"- [`{slug}/`]({slug}/) — {_label(str(row['canonical_title']))}{_note(row)}"
        )
    lines.extend(
        [
            "",
            "All G7 roots are `PRESENT_REVIEWED` and `GIT_PRIMARY` within authority epoch 1. Completeness refers to the approved Drive-to-Git migration boundary, not to every possible future analysis for a title. Excluded and reference-only source artifacts are recorded in the provenance and exclusion controls rather than copied into these trees.",
            "",
            "## Post-cutover Git-native series roots",
            "",
        ]
    )
    if post_cutover:
        for row in post_cutover:
            slug = str(row["stable_slug"])
            lines.append(
                f"- [`{slug}/`]({slug}/) — {_label(str(row['canonical_title']))}{_note(row)}"
            )
    else:
        lines.append("_None._")
    return "\n".join(lines)


def render_studies_readme(rows: list[Mapping[str, Any]]) -> str:
    return "\n".join(
        f"- [`{row['stable_slug']}/`]({row['stable_slug']}/) — "
        f"{_label(str(row['canonical_title']))}{_note(row)}"
        for row in rows
    )


def render_corpus_series(rows: list[Mapping[str, Any]]) -> str:
    return "\n".join(
        f"- [{_label(str(row['canonical_title']))}]"
        f"(../series/{row['stable_slug']}/) — `series/{row['stable_slug']}/`{_note(row)}"
        for row in rows
    )


def render_corpus_studies(rows: list[Mapping[str, Any]]) -> str:
    return "\n".join(
        f"- [{_label(str(row['canonical_title']))}]"
        f"(../studies/{row['stable_slug']}/) — `studies/{row['stable_slug']}/`{_note(row)}"
        for row in rows
    )


def _replace_generated_block(
    data: bytes, path: str, markers: tuple[str, str], rendered: str
) -> bytes:
    try:
        text = data.decode("utf-8", "strict")
    except UnicodeDecodeError as exc:
        raise DomainError(f"{path} is not UTF-8: {exc}") from exc
    if "\r" in text:
        raise DomainError(f"{path} must use LF line endings")
    start, end = markers
    if text.count(start) != 1 or text.count(end) != 1:
        raise DomainError(f"{path} must contain exactly one {start!r} / {end!r} pair")
    before, remainder = text.split(start, 1)
    _old, after = remainder.split(end, 1)
    replacement = f"{start}\n\n{rendered.rstrip()}\n\n{end}"
    return f"{before}{replacement}{after}".encode("utf-8")


def expected_outputs(snapshot: GitSnapshot) -> dict[str, bytes]:
    series_rows = _root_rows(
        _registry_rows(snapshot, SERIES_REGISTRY, "series", SERIES_SCHEMA), "series/"
    )
    study_rows = _root_rows(
        _registry_rows(snapshot, STUDY_REGISTRY, "studies", STUDY_SCHEMA), "studies/"
    )
    required_documents = (SERIES_README, STUDIES_README, CORPUS_INDEX)
    missing = [path for path in required_documents if snapshot.get(path) is None]
    if missing:
        raise DomainError(f"snapshot lacks generated catalog documents: {missing}")

    series_readme = _replace_generated_block(
        snapshot.entries[SERIES_README].data,
        SERIES_README,
        SERIES_README_MARKERS,
        render_series_readme(series_rows),
    )
    studies_readme = _replace_generated_block(
        snapshot.entries[STUDIES_README].data,
        STUDIES_README,
        STUDIES_README_MARKERS,
        render_studies_readme(study_rows),
    )
    corpus_index = _replace_generated_block(
        snapshot.entries[CORPUS_INDEX].data,
        CORPUS_INDEX,
        CORPUS_SERIES_MARKERS,
        render_corpus_series(series_rows),
    )
    corpus_index = _replace_generated_block(
        corpus_index,
        CORPUS_INDEX,
        CORPUS_STUDY_MARKERS,
        render_corpus_studies(study_rows),
    )
    tracked_paths = sorted(snapshot.entries, key=lambda path: path.encode("utf-8"))
    manifest = ("\n".join(tracked_paths) + "\n").encode("utf-8")
    return {
        SERIES_README: series_readme,
        STUDIES_README: studies_readme,
        CORPUS_INDEX: corpus_index,
        CURRENT_MANIFEST: manifest,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    operation = parser.add_mutually_exclusive_group()
    operation.add_argument("--check", action="store_true")
    operation.add_argument("--write", action="store_true")
    parser.add_argument("--snapshot", choices=["worktree", "index", "commit"], default="index")
    parser.add_argument("--commit")
    parser.add_argument("--repo", type=Path)
    args = parser.parse_args()
    root = args.repo.resolve() if args.repo else Path(__file__).resolve().parents[1]
    mode = "write" if args.write else "check"
    if mode == "write" and args.snapshot == "commit":
        raise DomainError("commit-snapshot generation is check-only")

    snapshot = _snapshot(root, args.snapshot, args.commit)
    outputs = expected_outputs(snapshot)
    stale = []
    for path, expected in outputs.items():
        entry = snapshot.get(path)
        if entry is None or entry.mode != "100644" or entry.data != expected:
            stale.append(path)
        if mode == "write":
            atomic_write_text(root / path, expected.decode("utf-8"))
    if mode == "check" and stale:
        raise DomainError(f"generated repository indexes are out of date: {stale}")
    if mode == "write":
        print("UPDATED: " + ", ".join(outputs))
    else:
        print(f"PASS: generated repository indexes match {snapshot.identity}")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (DomainError, OSError, ValueError) as exc:
        raise SystemExit(f"FAIL: {exc}") from exc
