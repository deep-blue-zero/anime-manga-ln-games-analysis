#!/usr/bin/env python3
"""Apply series/study routing inputs to their global machine registries.

Character discovery belongs exclusively to the curation agent. This tool does
not read character proposals or read, normalize, or write character outputs.
It never writes analytical content or deletes registry records.
"""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Any, Mapping

from character_index_core import (
    DomainError,
    GitSnapshot,
    atomic_write_text,
    decode_json,
)


BRANCH_RE = re.compile(r"^(series|studies)/([a-z0-9][a-z0-9-]*)$")
SERIES_REGISTRY = "series/registry.json"
STUDY_REGISTRY = "studies/registry.json"


def parse_branch(branch: str) -> tuple[str, str]:
    match = BRANCH_RE.fullmatch(branch)
    if match is None:
        raise DomainError("branch must be exactly series/<stable-slug> or studies/<stable-slug>")
    return match.group(1), match.group(2)


def _read_object(path: Path, label: str) -> dict[str, Any]:
    value = decode_json(path.read_bytes(), label)
    if not isinstance(value, dict):
        raise DomainError(f"{label}: expected one JSON object")
    return value


def _render_json(value: Mapping[str, Any]) -> str:
    return json.dumps(value, ensure_ascii=False, indent=2) + "\n"


def _upsert_root_row(
    document: dict[str, Any],
    *,
    collection: str,
    id_key: str,
    slug: str,
    namespace: str,
    source: Mapping[str, Any],
) -> None:
    rows = document.get(collection)
    if not isinstance(rows, list) or any(not isinstance(row, dict) for row in rows):
        raise DomainError(f"{namespace}/registry.json: invalid {collection} collection")
    expected_path = f"{namespace}/{slug}/"
    if source.get("stable_slug") != slug:
        raise DomainError(f"registry input stable_slug must equal branch slug {slug!r}")
    if source.get(id_key) != slug:
        raise DomainError(f"registry input {id_key} must equal branch slug {slug!r}")
    if source.get("repository_path") != expected_path:
        raise DomainError(f"registry input repository_path must equal {expected_path!r}")

    matches = [
        index
        for index, row in enumerate(rows)
        if row.get("stable_slug") == slug or row.get(id_key) == slug
    ]
    if len(matches) > 1:
        raise DomainError(f"global registry contains conflicting identities for {slug!r}")
    if matches:
        rows[matches[0]] = dict(source)
    else:
        rows.append(dict(source))
    rows.sort(key=lambda row: str(row.get("stable_slug", "")).encode("utf-8"))


def _synchronize_document(
    root_document: dict[str, Any],
    branch: str,
    source: Mapping[str, Any] | None,
    *,
    root_present: bool,
) -> dict[str, str]:
    namespace, slug = parse_branch(branch)
    registry_path = SERIES_REGISTRY if namespace == "series" else STUDY_REGISTRY
    collection = "series" if namespace == "series" else "studies"
    id_key = "series_id" if namespace == "series" else "study_id"
    rows = root_document.get(collection)
    if not isinstance(rows, list):
        raise DomainError(f"{registry_path}: missing {collection} array")
    registered = any(
        isinstance(row, Mapping)
        and row.get("stable_slug") == slug
        and row.get(id_key) == slug
        for row in rows
    )
    if source is not None:
        _upsert_root_row(
            root_document, collection=collection, id_key=id_key,
            slug=slug, namespace=namespace, source=source,
        )
    elif not registered:
        if not root_present:
            # A branch name alone does not create an analytical root.
            return {}
        input_name = "series-registry.json" if namespace == "series" else "study-registry.json"
        raise DomainError(
            f"new {namespace} root requires declarative input "
            f"{namespace}/{slug}/.repository/{input_name}"
        )
    return {registry_path: _render_json(root_document)}


def synchronize(root: Path, branch: str) -> dict[str, str]:
    namespace, slug = parse_branch(branch)
    registry_path = SERIES_REGISTRY if namespace == "series" else STUDY_REGISTRY
    document = _read_object(root / registry_path, registry_path)
    input_name = "series-registry.json" if namespace == "series" else "study-registry.json"
    input_path = root / namespace / slug / ".repository" / input_name
    source = _read_object(input_path, input_path.as_posix()) if input_path.is_file() else None
    return _synchronize_document(
        document, branch, source, root_present=(root / namespace / slug).exists(),
    )


def synchronize_snapshot(snapshot: GitSnapshot, branch: str) -> dict[str, str]:
    """Calculate the same routing update from complete tracked bytes, without writes."""
    namespace, slug = parse_branch(branch)
    registry_path = SERIES_REGISTRY if namespace == "series" else STUDY_REGISTRY
    input_name = "series-registry.json" if namespace == "series" else "study-registry.json"
    input_path = f"{namespace}/{slug}/.repository/{input_name}"

    def read_object(path: str, *, optional: bool = False) -> dict[str, Any] | None:
        entry = snapshot.get(path)
        if entry is None and optional:
            return None
        if entry is None or not entry.qualifies_as_evidence:
            raise DomainError(f"{path}: expected a tracked regular Git blob")
        value = decode_json(entry.data, path)
        if not isinstance(value, dict):
            raise DomainError(f"{path}: expected one JSON object")
        return value

    document = read_object(registry_path)
    assert document is not None
    return _synchronize_document(
        document, branch, read_object(input_path, optional=True),
        root_present=any(path.startswith(f"{namespace}/{slug}/") for path in snapshot.entries),
    )


def main() -> int:
    parser = argparse.ArgumentParser()
    operation = parser.add_mutually_exclusive_group(required=True)
    operation.add_argument("--write", action="store_true")
    operation.add_argument("--check", action="store_true")
    parser.add_argument("--branch", required=True)
    parser.add_argument("--repo", type=Path)
    args = parser.parse_args()
    root = args.repo.resolve() if args.repo else Path(__file__).resolve().parents[1]
    outputs = synchronize(root, args.branch)
    stale = [
        path
        for path, rendered in outputs.items()
        if not (root / path).is_file() or (root / path).read_text(encoding="utf-8") != rendered
    ]
    if args.check and stale:
        raise DomainError(f"global registries are stale: {stale}")
    if args.write:
        for path, rendered in outputs.items():
            atomic_write_text(root / path, rendered)
        print("UPDATED: " + ", ".join(outputs) if outputs else "NOOP: branch has no analytical root")
    else:
        print(f"PASS: global registries match declarative inputs for {args.branch}")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (DomainError, OSError, ValueError) as exc:
        raise SystemExit(f"FAIL: {exc}") from exc
