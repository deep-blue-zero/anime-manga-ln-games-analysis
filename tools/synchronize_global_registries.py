#!/usr/bin/env python3
"""Apply series-local declarative inputs to global machine registries.

The tool never writes analytical content. It supports additive or replacement
upserts only; automated registry deletion is deliberately outside its contract.
"""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Any, Mapping

from character_index_core import (
    DomainError,
    atomic_write_text,
    decode_json,
    decode_jsonl_with_lines,
)


BRANCH_RE = re.compile(r"^(series|studies)/([a-z0-9][a-z0-9-]*)$")
SERIES_REGISTRY = "series/registry.json"
STUDY_REGISTRY = "studies/registry.json"
CHARACTER_REGISTRY = "characters/registry.jsonl"


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


def _render_jsonl(rows: list[Mapping[str, Any]]) -> str:
    return "".join(
        json.dumps(row, ensure_ascii=False, separators=(",", ":")) + "\n"
        for row in rows
    )


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


def _upsert_characters(
    current: list[dict[str, Any]], source: list[dict[str, Any]], slug: str
) -> None:
    positions: dict[str, int] = {}
    for index, row in enumerate(current):
        subject_id = row.get("analysis_subject_id")
        if not isinstance(subject_id, str) or subject_id in positions:
            raise DomainError("global character registry has a missing or duplicate analysis_subject_id")
        positions[subject_id] = index

    source_ids: set[str] = set()
    expected_prefix = f"series/{slug}/"
    for row in source:
        subject_id = row.get("analysis_subject_id")
        if not isinstance(subject_id, str) or not subject_id:
            raise DomainError("character upsert lacks analysis_subject_id")
        if subject_id in source_ids:
            raise DomainError(f"duplicate character upsert: {subject_id}")
        source_ids.add(subject_id)
        if row.get("series_id") != slug:
            raise DomainError(f"{subject_id}: series_id must equal branch slug {slug!r}")
        evidence = row.get("evidence")
        if not isinstance(evidence, list):
            raise DomainError(f"{subject_id}: evidence must be an array")
        for evidence_row in evidence:
            path = evidence_row.get("repository_path") if isinstance(evidence_row, Mapping) else None
            if not isinstance(path, str) or not path.startswith(expected_prefix):
                raise DomainError(
                    f"{subject_id}: automated evidence must remain under {expected_prefix}"
                )
        if subject_id in positions:
            existing = current[positions[subject_id]]
            if existing.get("series_id") != slug:
                raise DomainError(f"{subject_id}: upsert would cross a series ownership boundary")
            current[positions[subject_id]] = dict(row)
        else:
            positions[subject_id] = len(current)
            current.append(dict(row))


def synchronize(root: Path, branch: str) -> dict[str, str]:
    namespace, slug = parse_branch(branch)
    root_registry_path = root / (SERIES_REGISTRY if namespace == "series" else STUDY_REGISTRY)
    root_document = _read_object(root_registry_path, root_registry_path.as_posix())
    collection = "series" if namespace == "series" else "studies"
    id_key = "series_id" if namespace == "series" else "study_id"
    rows = root_document.get(collection)
    if not isinstance(rows, list):
        raise DomainError(f"{root_registry_path.as_posix()}: missing {collection} array")

    input_name = "series-registry.json" if namespace == "series" else "study-registry.json"
    input_path = root / namespace / slug / ".repository" / input_name
    registered = any(
        isinstance(row, Mapping)
        and row.get("stable_slug") == slug
        and row.get(id_key) == slug
        for row in rows
    )
    if input_path.is_file():
        source = _read_object(input_path, input_path.as_posix())
        _upsert_root_row(
            root_document,
            collection=collection,
            id_key=id_key,
            slug=slug,
            namespace=namespace,
            source=source,
        )
    elif not registered:
        raise DomainError(
            f"new {namespace} root requires declarative input {input_path.relative_to(root).as_posix()}"
        )

    outputs = {root_registry_path.relative_to(root).as_posix(): _render_json(root_document)}
    if namespace == "series":
        character_path = root / CHARACTER_REGISTRY
        current = [
            row
            for _line, row in decode_jsonl_with_lines(
                character_path.read_bytes(), CHARACTER_REGISTRY
            )
        ]
        character_input = root / "series" / slug / ".repository" / "character-registry-upserts.jsonl"
        if character_input.is_file():
            source = [
                row
                for _line, row in decode_jsonl_with_lines(
                    character_input.read_bytes(), character_input.as_posix()
                )
            ]
            _upsert_characters(current, source, slug)
        outputs[CHARACTER_REGISTRY] = _render_jsonl(current)
    return outputs


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
        print("UPDATED: " + ", ".join(outputs))
    else:
        print(f"PASS: global registries match declarative inputs for {args.branch}")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (DomainError, OSError, ValueError) as exc:
        raise SystemExit(f"FAIL: {exc}") from exc
