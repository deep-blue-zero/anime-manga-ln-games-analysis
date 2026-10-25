#!/usr/bin/env python3
"""Read-only validation of the frozen PACTRIH CSV v12 / atlas v3 import.

Adapted from the supplied checks/verify_sources.py. This never generates PCA,
clusters, scores, or a new trusted manifest. A successor needs a reviewed update.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import io
import json
import math
import re
import subprocess
import sys
import tempfile
from collections import Counter
from decimal import Decimal, InvalidOperation
from html.parser import HTMLParser
from pathlib import Path

AXES = list("PACTRIH")
COLUMNS = ["Character", *AXES, "Type", "Humane Regard", "Moral Structure", "Unit"]
UNIT_CODES = {0: "Character", 1: "Faction", 2: "Historical Agent"}
COUNTS = {"Character": 85, "Faction": 7, "Historical Agent": 8}
# Pins are intentionally independent of the editable provenance manifest.
PINS = {
    "data/pactrih_scores.csv": (12554, "4687d3484e6014debacb6d87a852698a2fd198be95e44a4684fc401fd1df4837"),
    "interactive/atlas.html": (33741, "e2c491c34ee6f47e2dd0bebfec5f21eef09baf38236c5aacb3645c7ca38429d6"),
}
SOURCE_CSV_PIN = (12658, "32d23e61134df1336af482e976e2006bb7a1321415b8b01cd13fdcf785d73f59")
RAW_PATTERN = re.compile(r"const raw\s*=\s*(\[.*?\])\s*;\s*const data\s*=", re.S)
SCRIPT_PATTERN = re.compile(r"<script(?:\s[^>]*)?>(.*?)</script>", re.S | re.I)


class ValidationError(ValueError):
    """An input is invalid, stale, or outside the reviewed frozen baseline."""


def check(condition: bool, message: str) -> None:
    if not condition:
        raise ValidationError(message)


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def strict_text(data: bytes, label: str) -> str:
    check(not data.startswith(b"\xef\xbb\xbf"), f"{label}: UTF-8 BOM prohibited")
    check(b"\r" not in data and b"\0" not in data, f"{label}: expected LF text without NUL")
    return data.decode("utf-8", "strict")


def load_csv(data: bytes) -> list[dict[str, str]]:
    reader = csv.DictReader(io.StringIO(strict_text(data, "CSV"), newline=""), strict=True)
    check(reader.fieldnames == COLUMNS, f"CSV headers differ: {reader.fieldnames}")
    rows = list(reader)
    check(len(rows) == 100, f"Expected 100 CSV records, got {len(rows)}")
    check(all(set(row) == set(COLUMNS) and all(isinstance(v, str) and v for v in row.values())
              for row in rows), "CSV row has missing, extra, or empty fields")
    check(len({row["Character"] for row in rows}) == 100, "Duplicate subjects")
    check(Counter(row["Unit"] for row in rows) == COUNTS, "Unexpected unit counts")
    for row in rows:
        name = row["Character"]
        for axis in AXES:
            check(re.fullmatch(r"(?:[0-9]|10)", row[axis]) is not None,
                  f"{name}: {axis} must be an integer in 0..10")
        for field, left, right in (("Humane Regard", "P", "A"), ("Moral Structure", "C", "T")):
            try:
                value = Decimal(row[field])
            except InvalidOperation as exc:
                raise ValidationError(f"{name}: invalid {field}") from exc
            expected = (Decimal(row[left]) + Decimal(row[right])) / 2
            check(value.is_finite() and value == expected, f"{name}: {field} mismatch")
    return rows


class ResourceCheck(HTMLParser):
    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attrs = dict(attrs)
        if tag in {"script", "img", "iframe", "audio", "video", "source", "embed", "object"}:
            check(not any(key in attrs for key in ("src", "srcset", "data")),
                  f"Atlas must remain standalone: external {tag} resource")
        if tag == "link":
            check("href" not in attrs, "Atlas must remain standalone: external link resource")


def load_atlas(data: bytes) -> tuple[list[list], str]:
    html = strict_text(data, "HTML")
    ResourceCheck().feed(html)
    matches = list(RAW_PATTERN.finditer(html))
    check(len(matches) == 1, "Expected one embedded raw data array")
    records = json.loads(matches[0].group(1))
    scripts = SCRIPT_PATTERN.findall(html)
    check(len(scripts) == 1, "Expected one embedded JavaScript block")
    return records, scripts[0]


def validate_pair(csv_data: bytes, html_data: bytes) -> tuple[list[dict[str, str]], list[list], str]:
    """Check semantics before snapshot pins so drift failures name their cause."""
    rows = load_csv(csv_data)
    records, script = load_atlas(html_data)
    check(len(records) == len(rows), "Atlas entry count differs from CSV")
    for index, (record, row) in enumerate(zip(records, rows), 1):
        check(isinstance(record, list) and len(record) == 16, f"Atlas row {index}: expected 16 fields")
        check(record[0] == row["Character"], f"Atlas row {index}: identity/order mismatch")
        for offset, axis in enumerate(AXES, 1):
            check(type(record[offset]) is int and record[offset] == int(row[axis]),
                  f"Atlas row {index}: {axis} mismatch")
        check(record[8] == row["Type"], f"Atlas row {index}: description mismatch")
        check(type(record[14]) is int and UNIT_CODES.get(record[14]) == row["Unit"],
              f"Atlas row {index}: unit mismatch")
        for offset in (9, 10):
            check(type(record[offset]) in (int, float) and math.isfinite(record[offset]),
                  f"Atlas row {index}: invalid PCA coordinate")
        for offset, cap in ((11, 8), (12, 10), (13, 12)):
            check(type(record[offset]) is int and 1 <= record[offset] <= cap,
                  f"Atlas row {index}: invalid cluster ID")
        check(type(record[15]) is int and record[15] in (0, 1), f"Atlas row {index}: invalid priority flag")
    return rows, records, script


def check_javascript(script: str) -> None:
    with tempfile.TemporaryDirectory(prefix="pactrih-js-") as directory:
        path = Path(directory) / "atlas.js"
        path.write_text(script, encoding="utf-8", newline="\n")
        try:
            result = subprocess.run(["node", "--check", str(path)], capture_output=True, text=True, check=False)
        except FileNotFoundError as exc:
            raise ValidationError("Node.js is required for the JavaScript syntax check") from exc
        check(result.returncode == 0, f"JavaScript syntax check failed: {result.stderr.strip()}")


def validate_snapshot(root: Path, *, javascript: bool = True) -> dict:
    csv_data = (root / "data/pactrih_scores.csv").read_bytes()
    html_data = (root / "interactive/atlas.html").read_bytes()
    rows, records, script = validate_pair(csv_data, html_data)
    manifest = json.loads((root / "audits/source_manifest.json").read_text(encoding="utf-8"))
    check(manifest.get("schema") == "pactrih/frozen-import/v1", "Unexpected manifest schema")
    check(manifest.get("dataset_version") == "v12" and manifest.get("atlas_version") == "v3",
          "Manifest version differs from frozen import")
    check(manifest.get("subject_count") == len(rows) and manifest.get("unit_counts") == COUNTS,
          "Manifest counts differ from dataset")
    check(manifest.get("columns") == COLUMNS, "Manifest schema differs from CSV")
    # The only CSV transformation is reversible BOM removal and CRLF -> LF.
    reconstructed_source = b"\xef\xbb\xbf" + csv_data.replace(b"\n", b"\r\n")
    check((len(reconstructed_source), sha256(reconstructed_source)) == SOURCE_CSV_PIN,
          "CSV does not reconstruct the exact supplied v12 source bytes")
    csv_manifest = manifest.get("artifacts", {}).get("data/pactrih_scores.csv", {})
    check((csv_manifest.get("source_bytes"), csv_manifest.get("source_sha256")) == SOURCE_CSV_PIN,
          "Manifest original CSV source pin mismatch")
    fingerprints = {}
    for path, data in (("data/pactrih_scores.csv", csv_data), ("interactive/atlas.html", html_data)):
        size, digest = PINS[path]
        check((len(data), sha256(data)) == (size, digest),
              f"Frozen baseline changed: {path}; reviewed successor metadata and reproducibility are required")
        source = manifest.get("artifacts", {}).get(path, {})
        check(source.get("bytes") == size and source.get("sha256") == digest,
              f"Manifest pin mismatch: {path}")
        fingerprints[path] = {"bytes": size, "sha256": digest}
    embedding_digest = sha256(json.dumps(records, ensure_ascii=False, separators=(",", ":")).encode("utf-8"))
    check(manifest.get("embedding_sha256") == embedding_digest, "Manifest embedding fingerprint mismatch")
    if javascript:
        check_javascript(script)
    return {"result": "PASS", "subjects": len(rows), "unit_counts": COUNTS,
            "parity": "identity/order/PACTRIH/description/unit; derived coordinates exact",
            "frozen_pca_clusters_priority_and_ui": "unchanged (whole HTML SHA-256)",
            "original_csv_reconstruction": "exact source SHA-256 passed (UTF-8 BOM and CRLF restored)",
            "javascript": "node --check passed" if javascript else "not run",
            "embedding_sha256": embedding_digest, "artifacts": fingerprints}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()
    try:
        print(json.dumps(validate_snapshot(args.root.resolve()), ensure_ascii=False, indent=2))
    except (OSError, ValueError, csv.Error) as exc:
        print(f"FAIL: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
