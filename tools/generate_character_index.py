#!/usr/bin/env python3
"""Generate the root character-analysis discovery index deterministically."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


HEADER = """# Character Analysis Index

> Status: G3 bootstrap; no corpus or reviewed character records are present.

This generated discovery surface answers: “Where is the substantive analysis of this character?” It is not the migration ledger or authority registry.

Inclusion requires curated evidence of either a dedicated character analysis or distributed substantial analysis. Mention counts, cast lists, transcripts, source text, and incidental references do not qualify by themselves.

## Reviewed entries

"""


def load_records(path: Path) -> list[dict]:
    records: list[dict] = []
    seen: set[str] = set()
    for line_number, raw in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if not raw.strip():
            continue
        record = json.loads(raw)
        character_id = record.get("character_id")
        if not isinstance(character_id, str) or not character_id:
            raise ValueError(f"line {line_number}: missing character_id")
        if character_id in seen:
            raise ValueError(f"line {line_number}: duplicate character_id {character_id}")
        seen.add(character_id)
        records.append(record)
    return records


def render(records: list[dict]) -> str:
    included = sorted(
        (record for record in records if record.get("curation_status") == "INCLUDED"),
        key=lambda record: (record["preferred_name"].casefold(), record["character_id"]),
    )
    if not included:
        return HEADER + "_No reviewed entries have been migrated._\n"

    lines = [HEADER.rstrip(), ""]
    for record in included:
        lines.append(f"### {record['preferred_name']}")
        lines.append("")
        lines.append(f"- ID: `{record['character_id']}`")
        lines.append(f"- Series: `{record['series_id']}`")
        lines.append(f"- Inclusion: `{record['inclusion_basis']}`")
        lines.append("- Evidence:")
        for evidence in sorted(record["evidence"], key=lambda item: (item["repository_path"], item["semantic_locator"])):
            lines.append(f"  - [{evidence['semantic_locator']}]({evidence['repository_path']})")
        lines.append("")
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[1]
    registry = root / "characters" / "registry.jsonl"
    output = root / "CHARACTER_ANALYSIS_INDEX.md"
    rendered = render(load_records(registry))
    if args.check:
        if output.read_text(encoding="utf-8") != rendered:
            raise SystemExit("CHARACTER_ANALYSIS_INDEX.md is out of date")
        return 0
    output.write_text(rendered, encoding="utf-8", newline="\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
