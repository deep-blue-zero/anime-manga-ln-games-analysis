#!/usr/bin/env python3
"""Fail-closed validation for historical G3 and the Character Index v2 candidate."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import subprocess
import sys
import unicodedata
from pathlib import Path, PurePosixPath
from typing import Any, Mapping
from urllib.parse import unquote_to_bytes

from character_index_core import (
    AuthorityGraph,
    DomainError,
    GitSnapshot,
    decode_json,
    decode_jsonl_with_lines,
    load_json,
    render_schema_diagnostics,
    run_git,
    schema_diagnostics,
    validate_discovery_records,
    validate_repository_path,
    validate_schema_document,
)


WINDOWS_RESERVED = {
    "CON",
    "PRN",
    "AUX",
    "NUL",
    *(f"COM{i}" for i in range(1, 10)),
    *(f"LPT{i}" for i in range(1, 10)),
}
SECRET_PATTERNS = {
    "GitHub token": re.compile(rb"\b(?:ghp|gho|ghu|ghs|ghr)_[A-Za-z0-9]{20,}\b"),
    "private key": re.compile(rb"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
    "AWS access key": re.compile(rb"\bAKIA[0-9A-Z]{16}\b"),
    "Google API key": re.compile(rb"\bAIza[0-9A-Za-z_-]{30,}\b"),
}
PUBLICATION_PATTERNS = {
    "Google Drive URL": re.compile(rb"https://(?:drive|docs)\.google\.com", re.IGNORECASE),
    "local absolute path": re.compile(
        rb"(?:\b[A-Z]" + rb":" + rb"[\\/]|file" + rb"://)", re.IGNORECASE
    ),
    "personal email address": re.compile(
        rb"\b[A-Z0-9._%+-]+@(?:gmail|googlemail|outlook|hotmail|yahoo)\.[A-Z]{2,}\b",
        re.IGNORECASE,
    ),
}
MARKDOWN_LINK = re.compile(r"\[[^\]]*\]\(([^)]+)\)")
G3_MANIFEST = "governance/repository-controls/G3_BOOTSTRAP_TRACKED_PATHS.txt"
CURRENT_MANIFEST = "governance/repository-controls/CURRENT_TRACKED_PATHS.txt"
G3_BOUND_COMMIT = "e934c0a6f92ad16ba3305bd99f938aa6b3d97a1f"
G3_BOUND_TREE = "d0bb00fa5d7a8735892921ba3c0023b4855ac52e"
PROTECTED_HASHES = {
    G3_MANIFEST: "75c6fe48adc719090828a2da02f3dc69e2334b8b20ee5f1c89e0f4c33ee6d191",
    "governance/repository-controls/bootstrap-bindings.json": "7ebb26e4cff22acbabe72905847f6efbbb6885c4a6be0b9e5297db22d654ae17",
}
RESERVED_ABSENT = {
    "characters/reconstruction_capabilities.jsonl",
    "characters/CHARACTER_RECONSTRUCTION_INDEX.md",
}
NATIVE_SHEET_SCHEMA = "governance/schemas/native-sheet-structure.schema.json"
NATIVE_SHEET_SCHEMA_ID = "manga-anime-git-migration/native-sheet-structure/v1"
NATIVE_SHEET_TRANSFORMATION = (
    "GOOGLE_SHEET_VERIFIED_XLSX_TO_TSV_PACKAGE_V2_BLANK_PRESERVING"
)
NATIVE_SHEET_REFERENCE_TRANSFORMATION = "GOOGLE_SHEET_NATIVE_XLSX_REFERENCE_V1"
CROSSWALK_FILES = {
    "mapping": "crosswalk/drive-to-git.jsonl",
    "results": "crosswalk/materialization-results.jsonl",
    "plan": "crosswalk/path-plan.jsonl",
}
SHA256_RE = re.compile(r"^[0-9a-f]{64}$")
REPRESENTATION_ID_RE = re.compile(r"^repr-[0-9a-f]{24}$")
POSITIVE_DECIMAL_RE = re.compile(r"^[1-9][0-9]*$")
EXCEL_RANGE_RE = re.compile(r"^A1:([A-Z]+)([1-9][0-9]*)$")
DJFW_TSV_WHITESPACE_ATTRIBUTE_RULE = (
    '"studies/doujinshi-fanwork-comparative-taxonomy/01 Project Registry and '
    'Source Lock/DJFW_PROJECT_CONTROL_SHEET.tabs/*.tsv" whitespace=-blank-at-eol'
)
WHITESPACE_ATTRIBUTE_TOKEN_RE = re.compile(
    r"(?:^|[ \t])(?:whitespace(?:=[^ \t]+)?|-whitespace|!whitespace)(?=$|[ \t])"
)


def _git_paths(root: Path, *args: str) -> list[str]:
    raw = run_git(root, *args)
    return [item.decode("utf-8", "strict") for item in raw.split(b"\0") if item]


def worktree_paths(root: Path) -> list[str]:
    return sorted(_git_paths(root, "ls-files", "--cached", "--others", "--exclude-standard", "-z"))


def worktree_snapshot(root: Path, paths: list[str]) -> GitSnapshot:
    index_modes: dict[str, str] = {}
    raw = run_git(root, "ls-files", "--stage", "-z")
    for item in raw.split(b"\0"):
        if not item:
            continue
        metadata, raw_path = item.split(b"\t", 1)
        mode, _oid, stage = metadata.decode("ascii").split(" ")
        if stage != "0":
            raise DomainError(f"unmerged index entry: {raw_path.decode('utf-8', 'strict')}")
        index_modes[raw_path.decode("utf-8", "strict")] = mode
    entries = {}
    from character_index_core import SnapshotEntry

    for path in paths:
        full = root.joinpath(*PurePosixPath(path).parts)
        if full.is_symlink():
            entries[path] = SnapshotEntry(
                path, "120000", os.readlink(full).encode("utf-8"), path in index_modes
            )
        elif full.is_file():
            entries[path] = SnapshotEntry(
                path, index_modes.get(path, "100644"), full.read_bytes(), path in index_modes
            )
        elif full.exists():
            entries[path] = SnapshotEntry(path, "040000", b"", path in index_modes)
    return GitSnapshot(root, "PROSPECTIVE_WORKTREE", entries)


def read_manifest_from_snapshot(snapshot: GitSnapshot, path: str) -> list[str]:
    entry = snapshot.get(path)
    if entry is None or entry.mode != "100644":
        raise DomainError(f"missing regular path manifest: {path}")
    if b"\r" in entry.data or entry.data.startswith(b"\xef\xbb\xbf"):
        raise DomainError(f"invalid encoding/line endings in path manifest: {path}")
    values = [line for line in entry.data.decode("utf-8", "strict").split("\n") if line]
    if values != sorted(values):
        raise DomainError(f"path manifest is not ASCII/Unicode-codepoint sorted: {path}")
    if len(values) != len(set(values)):
        raise DomainError(f"path manifest contains duplicates: {path}")
    for value in values:
        validate_repository_path(value)
    return values


def read_external_manifest(path: Path) -> list[str]:
    data = path.read_bytes()
    if b"\r" in data or data.startswith(b"\xef\xbb\xbf"):
        raise DomainError(f"invalid external manifest encoding: {path}")
    values = [line for line in data.decode("utf-8", "strict").split("\n") if line]
    if values != sorted(values) or len(values) != len(set(values)):
        raise DomainError(f"external manifest must be sorted and unique: {path}")
    return values


def validate_exact_set(paths: list[str], expected: list[str], label: str) -> list[str]:
    missing = sorted(set(expected) - set(paths))
    extra = sorted(set(paths) - set(expected))
    if missing or extra or len(paths) != len(set(paths)):
        return [f"{label} path-set mismatch; missing={missing}, extra={extra}"]
    return []


def validate_paths(snapshot: GitSnapshot, policy: Mapping[str, Any]) -> list[str]:
    errors: list[str] = []
    normalized: dict[str, str] = {}
    casefolded: dict[str, str] = {}
    allowed_roots = tuple(policy["allowed_roots"])
    allowed_root_files = set(policy["allowed_root_files"])
    forbidden = tuple(policy["forbidden_paths"])
    external_extensions = set(policy["default_external_extensions"])
    allowed_workflows = set(policy.get("allowed_workflows", []))
    for path, entry in snapshot.entries.items():
        try:
            validate_repository_path(path)
        except DomainError as exc:
            errors.append(str(exc))
        posix = PurePosixPath(path)
        for part in posix.parts:
            if part.endswith((" ", ".")):
                errors.append(f"Windows-unsafe trailing character: {path}")
            if part.split(".", 1)[0].upper() in WINDOWS_RESERVED:
                errors.append(f"Windows reserved component: {path}")
        nfc = unicodedata.normalize("NFC", path)
        folded = nfc.casefold()
        if nfc in normalized and normalized[nfc] != path:
            errors.append(f"Unicode normalization collision: {normalized[nfc]} / {path}")
        if folded in casefolded and casefolded[folded] != path:
            errors.append(f"case collision: {casefolded[folded]} / {path}")
        normalized[nfc] = path
        casefolded[folded] = path
        if path not in allowed_root_files and not path.startswith(allowed_roots):
            errors.append(f"path is outside allowlisted roots: {path}")
        if any(path == item or path.startswith(item) for item in forbidden):
            errors.append(f"forbidden path: {path}")
        if Path(path).suffix.casefold() in external_extensions:
            errors.append(f"default-external artifact tracked without exception: {path}")
        if path.startswith(".github/workflows/") and path not in allowed_workflows:
            errors.append(f"workflow is outside the exact allowlist: {path}")
        if entry.mode != "100644":
            errors.append(f"non-regular or executable Git mode {entry.mode!r}: {path}")
    for path in sorted(allowed_workflows):
        if snapshot.get(path) is None:
            errors.append(f"allowlisted workflow is missing: {path}")
    return errors


def validate_audit_workflow(
    snapshot: GitSnapshot, policy: Mapping[str, Any]
) -> list[str]:
    """Enforce the settled single, non-mutating repository-audit workflow."""

    expected = {".github/workflows/repository-audit.yml"}
    declared = set(policy.get("allowed_workflows", []))
    errors: list[str] = []
    if declared != expected:
        errors.append(
            "allowed_workflows must contain only .github/workflows/repository-audit.yml"
        )
        return errors
    entry = snapshot.get(".github/workflows/repository-audit.yml")
    if entry is None:
        return ["approved repository-audit workflow is missing"]
    try:
        text = entry.data.decode("utf-8", "strict")
    except UnicodeDecodeError as exc:
        return [f"repository-audit workflow is not UTF-8: {exc}"]

    required_fragments = (
        "name: Repository audit",
        "  push:",
        "      - main",
        '      - "codex/**"',
        '    - cron: "17 6 * * 0"',
        "  workflow_dispatch:",
        "permissions:\n  contents: read",
        "runs-on: ubuntu-24.04",
        'MANGA_ANIME_TEST_TMP: "${{ runner.temp }}/manga-anime-tests"',
        'git fetch --no-tags origin "${GITHUB_SHA}"',
        'test "$(git rev-parse --is-shallow-repository)" = "false"',
        "--require-hashes",
        "tools/validate_repository.py",
        "tools/generate_character_index.py --check",
        'mkdir -p "${MANGA_ANIME_TEST_TMP}"',
        "python -m unittest discover",
    )
    for fragment in required_fragments:
        if fragment not in text:
            errors.append(f"repository-audit workflow missing required contract: {fragment}")

    whitespace_command = 'git show --check --format= "${GITHUB_SHA}" -- . \\'
    markdown_whitespace_exclusion = "':(top,glob,exclude)**/*.md'"
    idoly_whitespace_exclusion = (
        "':(top,literal,exclude)series/idoly-pride/V2 Analysis/02 Source Audits and "
        "Longitudinal Ledgers/02.01 Corpus Coverage and Priority Ledger/"
        "IDOLY_PRIDE_V2_SOURCE_TO_BUNDLE_PROVENANCE.csv'"
    )
    workflow_lines = text.splitlines()
    command_lines = [
        index
        for index, line in enumerate(workflow_lines)
        if line.strip().startswith("git show --check")
    ]
    exclusion_lines = [
        line.strip()
        for line in workflow_lines
        if ":(" in line and "exclude" in line
    ]
    exact_whitespace_shape = bool(
        len(command_lines) == 1
        and workflow_lines[command_lines[0]].strip() == whitespace_command
        and command_lines[0] + 2 < len(workflow_lines)
        and workflow_lines[command_lines[0] + 1].strip()
        == markdown_whitespace_exclusion + " \\"
        and workflow_lines[command_lines[0] + 2].strip() == idoly_whitespace_exclusion
        and exclusion_lines
        == [markdown_whitespace_exclusion + " \\", idoly_whitespace_exclusion]
    )
    if not exact_whitespace_shape:
        errors.append(
            "repository-audit workflow whitespace check must use only the exact approved "
            "Markdown glob and IDOLY PRIDE provenance CSV exclusions"
        )

    forbidden_fragments = (
        "pull_request",
        "secrets.",
        "uses:",
        "contents: write",
        "permissions: write",
        "git push",
        "git commit",
        "git tag",
        "actions/upload-artifact",
        "GITHUB_TOKEN",
        "gh ",
        "--depth",
        "--deepen",
        "--shallow-exclude",
        "--shallow-since",
    )
    for fragment in forbidden_fragments:
        if fragment in text:
            errors.append(f"repository-audit workflow contains prohibited capability: {fragment}")
    return errors


def load_named_text_exceptions(
    policy: Mapping[str, Any], text_extensions: set[str], threshold: int
) -> tuple[dict[str, Mapping[str, Any]], list[str]]:
    """Parse the exact reviewed-text tuples without granting a path-wide capability."""

    raw = policy.get("named_text_exceptions", [])
    if not isinstance(raw, list):
        return {}, ["named_text_exceptions must be a list"]

    required_fields = {
        "path",
        "bytes",
        "sha256",
        "exception_id",
        "allow_utf8_bom",
        "allow_carriage_returns",
        "purpose",
        "rights_basis",
        "review_decision",
        "external_reference_insufficient",
    }
    hard_limit = int(policy["hard_exception_threshold_bytes"])
    exceptions: dict[str, Mapping[str, Any]] = {}
    errors: list[str] = []
    for index, item in enumerate(raw):
        label = f"named_text_exceptions[{index}]"
        if not isinstance(item, Mapping):
            errors.append(f"{label} must be an object")
            continue
        fields = set(item)
        if fields != required_fields:
            errors.append(
                f"{label} field-set mismatch; missing={sorted(required_fields - fields)}, "
                f"extra={sorted(fields - required_fields)}"
            )
            continue

        path = item["path"]
        if not isinstance(path, str):
            errors.append(f"{label}.path must be a string")
            continue
        try:
            validate_repository_path(path)
        except DomainError as exc:
            errors.append(f"{label}.path is invalid: {exc}")
            continue
        if Path(path).suffix.casefold() not in text_extensions:
            errors.append(f"{label}.path is not an allowed text extension: {path}")
        if path in exceptions:
            errors.append(f"duplicate named text exception path: {path}")
            continue

        byte_length = item["bytes"]
        if (
            isinstance(byte_length, bool)
            or not isinstance(byte_length, int)
            or byte_length <= threshold
            or byte_length > hard_limit
        ):
            errors.append(
                f"{label}.bytes must be an integer above the review threshold "
                f"and at or below the hard exception threshold"
            )
        sha256 = item["sha256"]
        if not isinstance(sha256, str) or re.fullmatch(r"[0-9a-f]{64}", sha256) is None:
            errors.append(f"{label}.sha256 must be exactly 64 lowercase hexadecimal characters")
        exception_id = item["exception_id"]
        if (
            not isinstance(exception_id, str)
            or re.fullmatch(r"[A-Z][A-Z0-9_]*", exception_id) is None
        ):
            errors.append(
                f"{label}.exception_id must be an uppercase ASCII identifier"
            )
        for flag in ("allow_utf8_bom", "allow_carriage_returns"):
            if not isinstance(item[flag], bool):
                errors.append(f"{label}.{flag} must be a boolean")
        for field in (
            "purpose",
            "rights_basis",
            "review_decision",
            "external_reference_insufficient",
        ):
            value = item[field]
            if (
                not isinstance(value, str)
                or not value
                or value != value.strip()
                or "\n" in value
                or "\r" in value
            ):
                errors.append(f"{label}.{field} must be a nonempty single-line string")

        # Invalid entries stay non-capable: validation reports their defects and the
        # corresponding artifact receives the ordinary size/normalization checks.
        if not any(error.startswith(label) for error in errors):
            exceptions[path] = item
    return exceptions, errors


def load_named_whitespace_exceptions(
    policy: Mapping[str, Any],
) -> tuple[dict[str, Mapping[str, Any]], list[str]]:
    """Parse exact, byte-bound waivers for intentional Markdown hard breaks."""

    raw = policy.get("named_whitespace_exceptions", [])
    if not isinstance(raw, list):
        return {}, ["named_whitespace_exceptions must be a list"]

    required_fields = {
        "path",
        "bytes",
        "sha256",
        "exception_id",
        "attribute",
        "trailing_ascii_spaces",
        "line_numbers",
        "purpose",
        "review_decision",
    }
    exceptions: dict[str, Mapping[str, Any]] = {}
    errors: list[str] = []
    for index, item in enumerate(raw):
        label = f"named_whitespace_exceptions[{index}]"
        if not isinstance(item, Mapping):
            errors.append(f"{label} must be an object")
            continue
        fields = set(item)
        if fields != required_fields:
            errors.append(
                f"{label} field-set mismatch; missing={sorted(required_fields - fields)}, "
                f"extra={sorted(fields - required_fields)}"
            )
            continue

        path = item["path"]
        if not isinstance(path, str):
            errors.append(f"{label}.path must be a string")
            continue
        try:
            validate_repository_path(path)
        except DomainError as exc:
            errors.append(f"{label}.path is invalid: {exc}")
            continue
        if Path(path).suffix.casefold() != ".md":
            errors.append(f"{label}.path must identify a Markdown artifact")
        if '"' in path:
            errors.append(f"{label}.path cannot contain a double quote")
        if path in exceptions:
            errors.append(f"duplicate named whitespace exception path: {path}")
            continue

        byte_length = item["bytes"]
        if isinstance(byte_length, bool) or not isinstance(byte_length, int) or byte_length <= 0:
            errors.append(f"{label}.bytes must be a positive integer")
        sha256 = item["sha256"]
        if not isinstance(sha256, str) or SHA256_RE.fullmatch(sha256) is None:
            errors.append(f"{label}.sha256 must be exactly 64 lowercase hexadecimal characters")
        exception_id = item["exception_id"]
        if (
            not isinstance(exception_id, str)
            or re.fullmatch(r"[A-Z][A-Z0-9_]*", exception_id) is None
        ):
            errors.append(f"{label}.exception_id must be an uppercase ASCII identifier")
        if item["attribute"] != "whitespace=-blank-at-eol":
            errors.append(
                f"{label}.attribute must equal whitespace=-blank-at-eol"
            )
        if item["trailing_ascii_spaces"] != 2:
            errors.append(f"{label}.trailing_ascii_spaces must equal 2")
        line_numbers = item["line_numbers"]
        if (
            not isinstance(line_numbers, list)
            or not line_numbers
            or any(
                isinstance(value, bool) or not isinstance(value, int) or value <= 0
                for value in line_numbers
            )
            or line_numbers != sorted(set(line_numbers))
        ):
            errors.append(
                f"{label}.line_numbers must be a nonempty sorted unique list of positive integers"
            )
        for field in ("purpose", "review_decision"):
            value = item[field]
            if (
                not isinstance(value, str)
                or not value
                or value != value.strip()
                or "\n" in value
                or "\r" in value
            ):
                errors.append(f"{label}.{field} must be a nonempty single-line string")

        if not any(error.startswith(label) for error in errors):
            exceptions[path] = item
    return exceptions, errors


def validate_named_whitespace_exceptions(
    snapshot: GitSnapshot, policy: Mapping[str, Any]
) -> list[str]:
    """Bind each whitespace waiver to exact bytes, lines, and one Git attribute."""

    exceptions, errors = load_named_whitespace_exceptions(policy)
    attributes_entry = snapshot.get(".gitattributes")
    if attributes_entry is None or attributes_entry.mode != "100644":
        return errors + ["missing regular .gitattributes for whitespace controls"]
    try:
        attributes_text = attributes_entry.data.decode("utf-8", "strict")
    except UnicodeDecodeError as exc:
        return errors + [f".gitattributes is not UTF-8: {exc}"]

    nested_attributes = sorted(
        path
        for path in snapshot.entries
        if path != ".gitattributes" and PurePosixPath(path).name == ".gitattributes"
    )
    if nested_attributes:
        errors.append(
            f"nested .gitattributes files are prohibited: {nested_attributes}"
        )

    active_rules = [
        line
        for line in attributes_text.splitlines()
        if line
        and not line.lstrip().startswith("#")
        and WHITESPACE_ATTRIBUTE_TOKEN_RE.search(line) is not None
    ]
    expected_rules = [DJFW_TSV_WHITESPACE_ATTRIBUTE_RULE]
    expected_rules.extend(
        f'"{path}" {item["attribute"]}'
        for path, item in sorted(exceptions.items(), key=lambda pair: pair[0].encode("utf-8"))
    )
    if active_rules != expected_rules:
        errors.append(
            ".gitattributes whitespace rules must equal the exact approved TSV and "
            "named byte-bound exception set"
        )

    for path, item in sorted(exceptions.items(), key=lambda pair: pair[0].encode("utf-8")):
        entry = snapshot.get(path)
        if entry is None or entry.mode != "100644":
            errors.append(f"unused named whitespace exception: {path}")
            continue
        actual_hash = hashlib.sha256(entry.data).hexdigest()
        if len(entry.data) != item["bytes"] or actual_hash != item["sha256"]:
            errors.append(f"named whitespace exception tuple mismatch: {path}")

        actual_trailing: dict[int, bytes] = {}
        for line_number, line in enumerate(entry.data.split(b"\n"), 1):
            match = re.search(rb"[ \t]+$", line)
            if match is not None:
                actual_trailing[line_number] = match.group(0)
        expected_trailing = {
            line_number: b" " * item["trailing_ascii_spaces"]
            for line_number in item["line_numbers"]
        }
        if actual_trailing != expected_trailing:
            errors.append(
                f"named whitespace exception line-shape mismatch: {path}; "
                f"expected_lines={sorted(expected_trailing)}, "
                f"actual_lines={sorted(actual_trailing)}"
            )
    return errors


def validate_bytes(snapshot: GitSnapshot, policy: Mapping[str, Any], phase: str) -> list[str]:
    errors: list[str] = []
    threshold = int(policy["review_threshold_bytes"])
    text_extensions = set(policy["allowed_text_extensions"])
    named_exceptions, exception_errors = load_named_text_exceptions(
        policy, text_extensions, threshold
    )
    errors.extend(exception_errors)
    special_text = {".gitattributes", ".gitignore", "CODEOWNERS"}
    for path, entry in snapshot.entries.items():
        data = entry.data
        exception = named_exceptions.get(path)
        exception_matches = bool(
            exception
            and len(data) == exception["bytes"]
            and hashlib.sha256(data).hexdigest() == exception["sha256"]
        )
        if exception is not None and not exception_matches:
            errors.append(f"named text exception tuple mismatch: {path}")
        if len(data) > threshold and not exception_matches:
            errors.append(f"{phase} file exceeds 1 MiB review threshold: {path} ({len(data)} bytes)")
        for label, pattern in SECRET_PATTERNS.items():
            if pattern.search(data):
                errors.append(f"possible {label} in {path}")
        for label, pattern in PUBLICATION_PATTERNS.items():
            if pattern.search(data):
                errors.append(f"publication hazard ({label}) in {path}")
        suffix = Path(path).suffix.casefold()
        if suffix in text_extensions or Path(path).name in special_text:
            allow_bom = bool(exception_matches and exception["allow_utf8_bom"])
            allow_carriage_returns = bool(
                exception_matches and exception["allow_carriage_returns"]
            )
            if data.startswith(b"\xef\xbb\xbf") and not allow_bom:
                errors.append(f"UTF-8 BOM prohibited: {path}")
            if b"\r" in data and not allow_carriage_returns:
                errors.append(f"non-LF line ending: {path}")
            if b"\0" in data:
                errors.append(f"NUL byte in text file: {path}")
            try:
                data.decode("utf-8", "strict")
            except UnicodeDecodeError as exc:
                errors.append(f"invalid UTF-8 in {path}: {exc}")
        if suffix == ".json":
            try:
                decode_json(data, path)
            except (DomainError, json.JSONDecodeError, UnicodeDecodeError) as exc:
                errors.append(f"invalid JSON in {path}: {exc}")
        if suffix == ".jsonl":
            try:
                text = data.decode("utf-8", "strict")
            except UnicodeDecodeError:
                continue
            for line_number, line in enumerate(text.splitlines(), 1):
                if not line.strip():
                    continue
                try:
                    decode_json(line.encode("utf-8"), f"{path}:{line_number}")
                except (DomainError, json.JSONDecodeError) as exc:
                    errors.append(f"invalid JSONL in {path}:{line_number}: {exc}")
    for path in sorted(named_exceptions, key=lambda item: item.encode("utf-8")):
        if path not in snapshot.entries:
            errors.append(f"unused named text exception: {path}")
    return errors


def validate_markdown_links(snapshot: GitSnapshot) -> list[str]:
    errors: list[str] = []
    paths = set(snapshot.entries)
    folded = {path.casefold(): path for path in paths}
    directories = {
        parent.as_posix()
        for path in paths
        for parent in PurePosixPath(path).parents
        if parent.as_posix() != "."
    }
    folded_directories = {path.casefold(): path for path in directories}
    for path, entry in snapshot.entries.items():
        if not path.endswith(".md") or entry.mode != "100644":
            continue
        try:
            text = entry.data.decode("utf-8", "strict")
        except UnicodeDecodeError:
            continue
        base = PurePosixPath(path).parent
        for raw_target in MARKDOWN_LINK.findall(text):
            target = raw_target.strip()
            if not target or target.startswith(("#", "https://", "http://", "mailto:")):
                continue
            encoded_path = target.split("#", 1)[0]
            if re.search(r"%(?![0-9A-Fa-f]{2})", encoded_path):
                errors.append(f"malformed percent escape in Markdown link in {path}: {target}")
                continue
            decoded_segments: list[str] = []
            decode_failed = False
            for segment in encoded_path.split("/"):
                try:
                    decoded = unquote_to_bytes(segment).decode("utf-8", "strict")
                except UnicodeDecodeError:
                    errors.append(f"invalid UTF-8 percent escape in Markdown link in {path}: {target}")
                    decode_failed = True
                    break
                if "/" in decoded or "\\" in decoded:
                    errors.append(f"encoded path separator in Markdown link in {path}: {target}")
                    decode_failed = True
                    break
                decoded_segments.append(decoded)
            if decode_failed:
                continue
            target_path = "/".join(decoded_segments)
            if not target_path:
                continue
            combined = base.joinpath(PurePosixPath(target_path))
            parts: list[str] = []
            unsafe = False
            for part in combined.parts:
                if part == "..":
                    if not parts:
                        unsafe = True
                        break
                    parts.pop()
                elif part not in {"", "."}:
                    parts.append(part)
            resolved = "/".join(parts)
            if unsafe or (resolved not in paths and resolved not in directories):
                case_match = folded.get(resolved.casefold()) or folded_directories.get(
                    resolved.casefold()
                )
                if case_match:
                    errors.append(f"case-mismatched Markdown link in {path}: {target} -> {case_match}")
                else:
                    errors.append(f"unresolved Markdown link in {path}: {target}")
    return errors


def validate_commit_identities(root: Path, policy: Mapping[str, Any], revision: str) -> list[str]:
    allowed = {(item["name"], item["email"]) for item in policy["allowed_commit_identities"]}
    raw = run_git(root, "log", revision, "--format=%an%x1f%ae%x1f%cn%x1f%ce%x1e")
    errors: list[str] = []
    for record in raw.decode("utf-8", "strict").split("\x1e"):
        record = record.strip("\r\n")
        if not record:
            continue
        fields = record.split("\x1f")
        if len(fields) != 4:
            errors.append("unable to parse a Git author/committer identity")
            continue
        author = (fields[0], fields[1])
        committer = (fields[2], fields[3])
        if author not in allowed:
            errors.append(f"non-owner Git author identity: {author[0]} <{author[1]}>")
        if committer not in allowed:
            errors.append(f"non-owner Git committer identity: {committer[0]} <{committer[1]}>")
    return errors


def identity_revision_for_snapshot(kind: str, commit: str | None) -> str:
    """Bind identity validation to the same history used by the selected snapshot."""

    if kind == "commit":
        if commit is None:
            raise DomainError("commit identity validation requires the selected commit")
        return commit
    return "HEAD"


def require_g3_selection(root: Path, kind: str, commit: str | None, has_manifest: bool) -> str:
    """Resolve and authenticate the immutable historical G3 object selection."""

    if kind != "commit":
        raise DomainError("G3 validation requires --snapshot commit")
    if has_manifest:
        raise DomainError("G3 validation prohibits an external manifest")
    selected = commit or G3_BOUND_COMMIT
    if selected != G3_BOUND_COMMIT:
        raise DomainError(
            f"G3 commit is not the immutable bound commit; expected={G3_BOUND_COMMIT}, "
            f"selected={selected}"
        )
    actual_tree = run_git(root, "rev-parse", f"{selected}^{{tree}}")
    decoded_tree = actual_tree.decode("ascii", "strict").strip()
    if decoded_tree != G3_BOUND_TREE:
        raise DomainError(
            f"G3 tree binding mismatch; expected={G3_BOUND_TREE}, actual={decoded_tree}"
        )
    return selected


def validate_protected(snapshot: GitSnapshot) -> list[str]:
    errors: list[str] = []
    for path, expected in PROTECTED_HASHES.items():
        entry = snapshot.get(path)
        actual = hashlib.sha256(entry.data).hexdigest() if entry is not None else "MISSING"
        if actual != expected:
            errors.append(f"protected path drift: {path}; expected={expected}, actual={actual}")
    for path in RESERVED_ABSENT:
        if snapshot.get(path) is not None:
            errors.append(f"reserved reconstruction production path must remain absent: {path}")
    return errors


def validate_generated_index(root: Path, snapshot_kind: str, commit: str | None) -> list[str]:
    command = [
        sys.executable,
        str(root / "tools" / "generate_character_index.py"),
        "--check",
        "--repo",
        str(root),
        "--snapshot",
        snapshot_kind,
    ]
    if commit is not None:
        command.extend(["--commit", commit])
    result = subprocess.run(command, cwd=root, capture_output=True, text=True)
    if result.returncode:
        return [result.stderr.strip() or result.stdout.strip() or "character index drift"]
    return []


def _policy_from_snapshot(snapshot: GitSnapshot) -> Mapping[str, Any]:
    path = "governance/repository-controls/tracked-file-policy.json"
    entry = snapshot.get(path)
    if entry is None:
        raise DomainError(f"missing policy: {path}")
    value = decode_json(entry.data, path)
    if not isinstance(value, dict):
        raise DomainError(f"policy is not an object: {path}")
    return value


def _snapshot_jsonl(snapshot: GitSnapshot, path: str) -> list[dict[str, Any]]:
    entry = snapshot.get(path)
    if entry is None:
        raise DomainError(f"missing crosswalk path: {path}")
    if not entry.qualifies_as_evidence:
        raise DomainError(
            f"crosswalk must be a tracked regular non-LFS Git blob: {path}"
        )
    return [
        record
        for _line_number, record in decode_jsonl_with_lines(
            entry.data, f"{snapshot.identity}:{path}"
        )
    ]


def _valid_nonempty_string(value: Any) -> bool:
    return (
        isinstance(value, str)
        and bool(value)
        and value == value.strip()
        and "\r" not in value
        and "\n" not in value
    )


def _validate_crosswalk_record_basics(
    row: Mapping[str, Any], label: str, required: set[str]
) -> list[str]:
    errors: list[str] = []
    missing = required - set(row)
    if missing:
        errors.append(f"{label} missing required fields: {sorted(missing)}")
    schema_version = row.get("schema_version")
    if (
        isinstance(schema_version, bool)
        or not isinstance(schema_version, int)
        or schema_version != 1
    ):
        errors.append(f"{label}.schema_version must equal 1")
    for field in required - {
        "schema_version",
        "destination_bytes",
        "git_bytes",
        "source_bytes",
    }:
        if field in row and not _valid_nonempty_string(row[field]):
            errors.append(f"{label}.{field} must be a nonempty single-line string")
    return errors


def _is_positive_integer(value: Any) -> bool:
    return isinstance(value, int) and not isinstance(value, bool) and value > 0


def _validate_crosswalk_source_group(
    row: Mapping[str, Any], label: str
) -> list[str]:
    """Validate optional one-to-many source provenance on a representation."""

    errors: list[str] = []
    source_ids = row.get("source_drive_ids")
    source_tuples = row.get("source_tuples")
    if source_ids is None and source_tuples is None:
        return errors
    if not isinstance(source_ids, list) or not source_ids:
        return [f"{label}.source_drive_ids must be a nonempty array"]
    if any(not _valid_nonempty_string(item) for item in source_ids):
        errors.append(f"{label}.source_drive_ids contains an invalid ID")
    if len(source_ids) != len(set(source_ids)):
        errors.append(f"{label}.source_drive_ids contains a duplicate ID")
    if source_ids and source_ids[0] != row.get("drive_id"):
        errors.append(f"{label}.source_drive_ids must begin with drive_id")
    if not isinstance(source_tuples, list) or len(source_tuples) != len(source_ids):
        errors.append(
            f"{label}.source_tuples must align one-for-one with source_drive_ids"
        )
        return errors

    tuple_ids: list[Any] = []
    required = {
        "drive_id",
        "source_path",
        "source_bytes",
        "source_revision",
        "source_sha256",
    }
    for index, item in enumerate(source_tuples):
        tuple_label = f"{label}.source_tuples[{index}]"
        if not isinstance(item, Mapping):
            errors.append(f"{tuple_label} must be an object")
            continue
        missing = required - set(item)
        if missing:
            errors.append(f"{tuple_label} missing fields: {sorted(missing)}")
            continue
        tuple_ids.append(item.get("drive_id"))
        for field in ("drive_id", "source_path"):
            if not _valid_nonempty_string(item.get(field)):
                errors.append(f"{tuple_label}.{field} is invalid")
        if not _is_positive_integer(item.get("source_bytes")):
            errors.append(f"{tuple_label}.source_bytes must be a positive integer")
        revision = item.get("source_revision")
        if not isinstance(revision, str) or POSITIVE_DECIMAL_RE.fullmatch(revision) is None:
            errors.append(
                f"{tuple_label}.source_revision must be a positive decimal string"
            )
        source_sha256 = item.get("source_sha256")
        if not isinstance(source_sha256, str) or SHA256_RE.fullmatch(source_sha256) is None:
            errors.append(f"{tuple_label}.source_sha256 is invalid")

    if tuple_ids != source_ids:
        errors.append(f"{label}.source_tuples IDs do not match source_drive_ids")
    if source_tuples and isinstance(source_tuples[0], Mapping):
        first = source_tuples[0]
        for field in (
            "drive_id",
            "source_path",
            "source_bytes",
            "source_revision",
            "source_sha256",
        ):
            if first.get(field) != row.get(field):
                errors.append(
                    f"{label}.{field} does not match the canonical source tuple"
                )
    if row.get("transformation") == "MERGE_IDENTICAL_BYTES_V1":
        byte_identities = {
            (item.get("source_bytes"), item.get("source_sha256"))
            for item in source_tuples
            if isinstance(item, Mapping)
        }
        if len(byte_identities) != 1:
            errors.append(
                f"{label} MERGE_IDENTICAL_BYTES_V1 sources are not byte-identical"
            )
    return errors


def _crosswalk_path_scope(row: Mapping[str, Any], path: str, label: str) -> list[str]:
    errors: list[str] = []
    scope_fields = [
        field for field in ("series_id", "study_id", "governance_id") if field in row
    ]
    if len(scope_fields) != 1:
        return [
            f"{label} must declare exactly one of series_id, study_id, or governance_id"
        ]
    field = scope_fields[0]
    value = row[field]
    if not _valid_nonempty_string(value):
        return [f"{label}.{field} must be a nonempty single-line string"]
    if field == "governance_id":
        if value != "repository":
            errors.append(f"{label}.governance_id must equal 'repository'")
        expected = "governance/"
    else:
        expected = f"{'series' if field == 'series_id' else 'studies'}/{value}/"
    if not path.startswith(expected):
        errors.append(
            f"{label} scope/path mismatch: {field}={value!r}, path={path!r}"
        )
    return errors


def _compare_crosswalk_field(
    errors: list[str],
    destination: str,
    left_label: str,
    left: Mapping[str, Any],
    left_field: str,
    right_label: str,
    right: Mapping[str, Any],
    right_field: str,
) -> None:
    if left.get(left_field) != right.get(right_field):
        errors.append(
            f"crosswalk {destination} {left_field}/{right_field} mismatch between "
            f"{left_label} and {right_label}"
        )


def active_migration_baseline_commit(snapshot: GitSnapshot) -> str | None:
    """Return the immutable migration baseline once Git authority is active."""

    entry = snapshot.get("governance/AUTHORITY_SCOPE.json")
    if entry is None:
        return None
    scope = decode_json(entry.data, "governance/AUTHORITY_SCOPE.json")
    if not isinstance(scope, Mapping):
        raise DomainError("authority scope must be an object")
    activation = scope.get("activation")
    if not isinstance(activation, Mapping):
        return None
    if activation.get("state") not in {"GIT_ACTIVE_STABILIZING", "GIT_ACTIVE_ACCEPTED"}:
        return None
    commit = activation.get("candidate_commit")
    if not isinstance(commit, str) or not re.fullmatch(r"[0-9a-f]{40}|[0-9a-f]{64}", commit):
        raise DomainError("active authority scope has an invalid candidate_commit")
    return commit


def validate_active_authority_scope(snapshot: GitSnapshot, baseline_commit: str | None) -> list[str]:
    """Bind the live authority scope to its cutover record and frozen ledgers."""

    if baseline_commit is None:
        return []
    errors: list[str] = []
    scope_entry = snapshot.get("governance/AUTHORITY_SCOPE.json")
    cutover_entry = snapshot.get("governance/cutovers/AUTHORITY_EPOCH_1.json")
    if scope_entry is None or cutover_entry is None:
        return ["active authority scope or epoch-1 cutover record is absent"]
    try:
        scope = decode_json(scope_entry.data, "governance/AUTHORITY_SCOPE.json")
        cutover = decode_json(cutover_entry.data, "governance/cutovers/AUTHORITY_EPOCH_1.json")
    except (DomainError, json.JSONDecodeError, UnicodeDecodeError) as exc:
        return [str(exc)]
    if not isinstance(scope, Mapping) or not isinstance(cutover, Mapping):
        return ["active authority scope and cutover record must be objects"]
    scope_hash = hashlib.sha256(scope_entry.data).hexdigest()
    if cutover.get("authority_scope_sha256") != scope_hash:
        errors.append("cutover authority-scope SHA-256 does not match committed bytes")
    if cutover.get("activation_commit") != baseline_commit:
        errors.append("cutover activation commit does not match authority scope")
    manifest = scope.get("scope_manifest")
    components = manifest.get("components") if isinstance(manifest, Mapping) else None
    if not isinstance(components, list):
        errors.append("active authority scope has no component list")
        return errors
    for component in components:
        if not isinstance(component, Mapping):
            errors.append("active authority component must be an object")
            continue
        path = component.get("path")
        expected_hash = component.get("sha256")
        expected_rows = component.get("rows")
        if not isinstance(path, str) or not isinstance(expected_hash, str):
            errors.append("active authority component path/hash is invalid")
            continue
        entry = snapshot.get(path)
        if entry is None or not entry.qualifies_as_evidence:
            errors.append(f"active authority component is absent or unsafe: {path}")
            continue
        if hashlib.sha256(entry.data).hexdigest() != expected_hash:
            errors.append(f"active authority component SHA-256 drift: {path}")
        rows = len([line for line in entry.data.split(b"\n") if line])
        if rows != expected_rows:
            errors.append(f"active authority component row-count drift: {path}")
    return errors


def validate_crosswalk_closure(
    snapshot: GitSnapshot, *, baseline_commit: str | None = None
) -> list[str]:
    """Validate migration provenance and current closure.

    Before cutover, declared destination bytes must match the selected snapshot. After
    cutover, those declarations remain immutable migration provenance bound to the
    activation commit; later authorized Git-primary edits are validated as current
    repository content without rewriting the historical crosswalk.
    """

    errors: list[str] = []
    try:
        mappings = _snapshot_jsonl(snapshot, CROSSWALK_FILES["mapping"])
        results = _snapshot_jsonl(snapshot, CROSSWALK_FILES["results"])
        plans = _snapshot_jsonl(snapshot, CROSSWALK_FILES["plan"])
    except (DomainError, json.JSONDecodeError, UnicodeDecodeError) as exc:
        return [str(exc)]

    baseline_cache: dict[str, bytes | None] = {}

    def baseline_bytes(path: str) -> bytes | None:
        if baseline_commit is None:
            return None
        if path not in baseline_cache:
            try:
                baseline_cache[path] = run_git(snapshot.root, "show", f"{baseline_commit}:{path}")
            except DomainError:
                baseline_cache[path] = None
        return baseline_cache[path]

    mapping_by_path: dict[str, Mapping[str, Any]] = {}
    representation_paths: dict[str, str] = {}
    for index, row in enumerate(mappings):
        label = f"{CROSSWALK_FILES['mapping']}:{index + 1}"
        required = {
            "schema_version",
            "drive_id",
            "source_path",
            "source_sha256",
            "git_path",
            "git_sha256",
            "transformation",
            "representation_id",
        }
        errors.extend(_validate_crosswalk_record_basics(row, label, required))
        errors.extend(_validate_crosswalk_source_group(row, label))
        if not required.issubset(row):
            continue
        path = row["git_path"]
        if not isinstance(path, str):
            continue
        try:
            validate_repository_path(path)
        except DomainError as exc:
            errors.append(f"{label}.git_path is invalid: {exc}")
            continue
        if not isinstance(row["source_sha256"], str) or not SHA256_RE.fullmatch(
            row["source_sha256"]
        ):
            errors.append(f"{label}.source_sha256 is not a lowercase SHA-256")
        if not isinstance(row["git_sha256"], str) or not SHA256_RE.fullmatch(
            row["git_sha256"]
        ):
            errors.append(f"{label}.git_sha256 is not a lowercase SHA-256")
        representation_id = row["representation_id"]
        if not isinstance(representation_id, str) or not REPRESENTATION_ID_RE.fullmatch(
            representation_id
        ):
            errors.append(f"{label}.representation_id is invalid")
            continue
        prior_representation = representation_paths.get(representation_id)
        if prior_representation is not None:
            errors.append(
                f"duplicate crosswalk representation_id {representation_id}: "
                f"{prior_representation} / {path}"
            )
        else:
            representation_paths[representation_id] = path
        if path in mapping_by_path:
            errors.append(f"duplicate drive-to-git destination path: {path}")
            continue
        mapping_by_path[path] = row
        errors.extend(_crosswalk_path_scope(row, path, label))
        entry = snapshot.get(path)
        if entry is None and baseline_commit is None:
            errors.append(f"drive-to-git destination is absent from snapshot: {path}")
        elif entry is not None and not entry.qualifies_as_evidence:
            errors.append(
                f"drive-to-git destination is not a tracked regular non-LFS blob: {path}"
            )
        else:
            provenance_data = entry.data if entry is not None else b""
            actual_hash = hashlib.sha256(provenance_data).hexdigest()
            if actual_hash != row["git_sha256"] and baseline_commit is not None:
                frozen = baseline_bytes(path)
                if frozen is not None:
                    provenance_data = frozen
                    actual_hash = hashlib.sha256(frozen).hexdigest()
            if actual_hash != row["git_sha256"]:
                errors.append(
                    f"drive-to-git committed-byte hash drift: {path}; "
                    f"declared={row['git_sha256']}, actual={actual_hash}"
                )
            if path.startswith("studies/"):
                if row.get("git_bytes") != len(provenance_data):
                    errors.append(f"drive-to-git committed-byte length drift: {path}")

    materialized_by_path: dict[str, Mapping[str, Any]] = {}
    reference_results: dict[tuple[str, str], Mapping[str, Any]] = {}
    for index, row in enumerate(results):
        label = f"{CROSSWALK_FILES['results']}:{index + 1}"
        result = row.get("result")
        if result == "MATERIALIZED_AND_HASH_VERIFIED":
            required = {
                "schema_version",
                "drive_id",
                "source_sha256",
                "destination_path",
                "destination_sha256",
                "destination_bytes",
                "transformation",
                "run_id",
            }
            errors.extend(_validate_crosswalk_record_basics(row, label, required))
            errors.extend(_validate_crosswalk_source_group(row, label))
            path = row.get("destination_path")
            if not isinstance(path, str):
                continue
            try:
                validate_repository_path(path)
            except DomainError as exc:
                errors.append(f"{label}.destination_path is invalid: {exc}")
                continue
            if path in materialized_by_path:
                errors.append(f"duplicate materialization destination path: {path}")
            else:
                materialized_by_path[path] = row
            if not isinstance(row.get("source_sha256"), str) or not SHA256_RE.fullmatch(
                row["source_sha256"]
            ):
                errors.append(f"{label}.source_sha256 is not a lowercase SHA-256")
            if not isinstance(row.get("destination_sha256"), str) or not SHA256_RE.fullmatch(
                row["destination_sha256"]
            ):
                errors.append(f"{label}.destination_sha256 is not a lowercase SHA-256")
            if not _is_positive_integer(row.get("destination_bytes")):
                errors.append(f"{label}.destination_bytes must be a positive integer")
            if "source_bytes" in row and not _is_positive_integer(row["source_bytes"]):
                errors.append(f"{label}.source_bytes must be a positive integer")
            if "body_preserved" in row and not isinstance(row["body_preserved"], bool):
                errors.append(f"{label}.body_preserved must be a boolean")
        elif result == "REFERENCE_VERIFIED_NOT_MATERIALIZED":
            required = {
                "schema_version",
                "drive_id",
                "source_path",
                "source_sha256",
                "transformation",
                "run_id",
                "terminal_action",
            }
            errors.extend(_validate_crosswalk_record_basics(row, label, required))
            key = (row.get("drive_id"), row.get("source_path"))
            if not all(isinstance(item, str) for item in key):
                continue
            if key in reference_results:
                errors.append(f"duplicate reference-only materialization result: {key}")
            else:
                reference_results[key] = row
            if row.get("terminal_action") != "REFERENCE_DRIVE":
                errors.append(f"{label}.terminal_action must equal REFERENCE_DRIVE")
            if not isinstance(row.get("source_sha256"), str) or not SHA256_RE.fullmatch(
                row["source_sha256"]
            ):
                errors.append(f"{label}.source_sha256 is not a lowercase SHA-256")
            if not _is_positive_integer(row.get("source_bytes")):
                errors.append(f"{label}.source_bytes must be a positive integer")
            prohibited = {
                "destination_path",
                "destination_sha256",
                "destination_bytes",
                "representation_id",
                "series_id",
                "study_id",
                "governance_id",
                "source_drive_ids",
                "source_tuples",
            }
            present = sorted(prohibited & set(row))
            if present:
                errors.append(
                    f"{label} reference-only row contains destination fields: {present}"
                )
        else:
            errors.append(f"{label}.result is not a recognized terminal result")

    planned_by_path: dict[str, Mapping[str, Any]] = {}
    reference_plans: dict[tuple[str, str], Mapping[str, Any]] = {}
    for index, row in enumerate(plans):
        label = f"{CROSSWALK_FILES['plan']}:{index + 1}"
        decision = row.get("decision")
        if isinstance(decision, str) and decision.startswith("MIGRATE_"):
            required = {
                "schema_version",
                "drive_id",
                "source_path",
                "destination_path",
                "path_status",
            }
            errors.extend(_validate_crosswalk_record_basics(row, label, required))
            errors.extend(_validate_crosswalk_source_group(row, label))
            path = row.get("destination_path")
            if not isinstance(path, str):
                continue
            try:
                validate_repository_path(path)
            except DomainError as exc:
                errors.append(f"{label}.destination_path is invalid: {exc}")
                continue
            if row.get("path_status") != "MATERIALIZED_PROSPECTIVE":
                errors.append(
                    f"{label}.path_status must equal MATERIALIZED_PROSPECTIVE"
                )
            if path in planned_by_path:
                errors.append(f"duplicate path-plan destination path: {path}")
            else:
                planned_by_path[path] = row
        elif decision == "REFERENCE_DRIVE":
            required = {
                "schema_version",
                "drive_id",
                "source_path",
                "path_status",
            }
            errors.extend(_validate_crosswalk_record_basics(row, label, required))
            key = (row.get("drive_id"), row.get("source_path"))
            if not all(isinstance(item, str) for item in key):
                continue
            if key in reference_plans:
                errors.append(f"duplicate reference-only path-plan row: {key}")
            else:
                reference_plans[key] = row
            if row.get("path_status") != "REFERENCE_VERIFIED_NOT_MATERIALIZED":
                errors.append(
                    f"{label}.path_status must equal REFERENCE_VERIFIED_NOT_MATERIALIZED"
                )
            prohibited = {
                "destination_path",
                "destination_sha256",
                "destination_bytes",
                "representation_id",
                "series_id",
                "study_id",
                "governance_id",
                "source_drive_ids",
                "source_tuples",
            }
            present = sorted(prohibited & set(row))
            if present:
                errors.append(
                    f"{label} reference-only row contains destination fields: {present}"
                )
        else:
            errors.append(f"{label}.decision is not a recognized migration decision")

    destination_sets = {
        "drive-to-git": set(mapping_by_path),
        "materialization-results": set(materialized_by_path),
        "path-plan": set(planned_by_path),
    }
    authoritative_destinations = destination_sets["drive-to-git"]
    for label, destinations in destination_sets.items():
        if destinations != authoritative_destinations:
            errors.append(
                f"crosswalk three-leg destination closure failure ({label}); "
                f"missing={sorted(authoritative_destinations - destinations)}, "
                f"extra={sorted(destinations - authoritative_destinations)}"
            )

    for path in sorted(
        authoritative_destinations
        & set(materialized_by_path)
        & set(planned_by_path),
        key=lambda item: item.encode("utf-8"),
    ):
        mapping = mapping_by_path[path]
        result = materialized_by_path[path]
        plan = planned_by_path[path]
        _compare_crosswalk_field(
            errors, path, "mapping", mapping, "drive_id", "result", result, "drive_id"
        )
        _compare_crosswalk_field(
            errors, path, "mapping", mapping, "drive_id", "plan", plan, "drive_id"
        )
        _compare_crosswalk_field(
            errors,
            path,
            "mapping",
            mapping,
            "source_path",
            "plan",
            plan,
            "source_path",
        )
        if "source_path" in result:
            _compare_crosswalk_field(
                errors,
                path,
                "mapping",
                mapping,
                "source_path",
                "result",
                result,
                "source_path",
            )
        _compare_crosswalk_field(
            errors,
            path,
            "mapping",
            mapping,
            "source_sha256",
            "result",
            result,
            "source_sha256",
        )
        _compare_crosswalk_field(
            errors,
            path,
            "mapping",
            mapping,
            "git_sha256",
            "result",
            result,
            "destination_sha256",
        )
        _compare_crosswalk_field(
            errors,
            path,
            "mapping",
            mapping,
            "transformation",
            "result",
            result,
            "transformation",
        )
        for field in (
            "governance_id",
            "source_drive_ids",
            "source_tuples",
        ):
            if any(field in leg for leg in (mapping, result, plan)):
                _compare_crosswalk_field(
                    errors, path, "mapping", mapping, field, "result", result, field
                )
                _compare_crosswalk_field(
                    errors, path, "mapping", mapping, field, "plan", plan, field
                )
        entry = snapshot.get(path)
        if (entry is not None and entry.qualifies_as_evidence) or baseline_commit is not None:
            provenance_data = entry.data if entry is not None else b""
            if (
                result.get("destination_sha256") != hashlib.sha256(provenance_data).hexdigest()
                and baseline_commit is not None
            ):
                frozen = baseline_bytes(path)
                if frozen is not None:
                    provenance_data = frozen
            if result.get("destination_bytes") != len(provenance_data):
                errors.append(f"materialization destination byte-length drift: {path}")
            if result.get("destination_sha256") != hashlib.sha256(provenance_data).hexdigest():
                errors.append(f"materialization destination SHA-256 drift: {path}")

        if path.startswith("studies/"):
            required_study_fields = {
                "mapping": {
                    "study_id",
                    "representation_id",
                    "source_path",
                    "source_bytes",
                    "source_revision",
                    "source_sha256",
                    "transformation",
                    "git_bytes",
                    "git_sha256",
                },
                "result": {
                    "study_id",
                    "representation_id",
                    "source_path",
                    "source_bytes",
                    "source_revision",
                    "source_sha256",
                    "transformation",
                    "destination_bytes",
                    "destination_sha256",
                },
                "plan": {
                    "study_id",
                    "representation_id",
                    "source_path",
                    "source_bytes",
                    "source_revision",
                    "source_sha256",
                    "transformation",
                    "destination_bytes",
                    "destination_sha256",
                },
            }
            for leg_label, leg in (
                ("mapping", mapping),
                ("result", result),
                ("plan", plan),
            ):
                missing = required_study_fields[leg_label] - set(leg)
                if missing:
                    errors.append(
                        f"study crosswalk {path} {leg_label} leg missing bindings: "
                        f"{sorted(missing)}"
                    )
                source_path = leg.get("source_path")
                source_bytes = leg.get("source_bytes")
                source_revision = leg.get("source_revision")
                source_sha256 = leg.get("source_sha256")
                if not _valid_nonempty_string(source_path):
                    errors.append(
                        f"study crosswalk {path} {leg_label}.source_path is invalid"
                    )
                if not _is_positive_integer(source_bytes):
                    errors.append(
                        f"study crosswalk {path} {leg_label}.source_bytes must be a "
                        "positive integer"
                    )
                if (
                    not isinstance(source_revision, str)
                    or POSITIVE_DECIMAL_RE.fullmatch(source_revision) is None
                ):
                    errors.append(
                        f"study crosswalk {path} {leg_label}.source_revision must be a "
                        "positive decimal string"
                    )
                if (
                    not isinstance(source_sha256, str)
                    or SHA256_RE.fullmatch(source_sha256) is None
                ):
                    errors.append(
                        f"study crosswalk {path} {leg_label}.source_sha256 is invalid"
                    )
            for field in (
                "study_id",
                "representation_id",
                "source_path",
                "source_bytes",
                "source_revision",
                "source_sha256",
                "transformation",
            ):
                _compare_crosswalk_field(
                    errors, path, "mapping", mapping, field, "result", result, field
                )
                _compare_crosswalk_field(
                    errors, path, "mapping", mapping, field, "plan", plan, field
                )
            for leg_label, leg in (("result", result), ("plan", plan)):
                _compare_crosswalk_field(
                    errors,
                    path,
                    "mapping",
                    mapping,
                    "git_sha256",
                    leg_label,
                    leg,
                    "destination_sha256",
                )
                _compare_crosswalk_field(
                    errors,
                    path,
                    "mapping",
                    mapping,
                    "git_bytes",
                    leg_label,
                    leg,
                    "destination_bytes",
                )

    if set(reference_results) != set(reference_plans):
        errors.append(
            "reference-only crosswalk closure failure; "
            f"missing_results={sorted(set(reference_plans) - set(reference_results))}, "
            f"missing_plans={sorted(set(reference_results) - set(reference_plans))}"
        )
    for key in set(reference_results) & set(reference_plans):
        result = reference_results[key]
        plan = reference_plans[key]
        if key[0] == "1fDfRSY9oHovjAcO-YPItDfZlirPjlc3yL8IZQZMRRXg":
            if result.get("transformation") != NATIVE_SHEET_REFERENCE_TRANSFORMATION:
                errors.append(
                    "P03 native XLSX reference result has an invalid transformation"
                )
            if (
                "transformation" in plan
                and plan["transformation"] != NATIVE_SHEET_REFERENCE_TRANSFORMATION
            ):
                errors.append(
                    "P03 native XLSX reference plan has an invalid transformation"
                )
    return errors


def _excel_column_number(label: str) -> int:
    result = 0
    for character in label:
        result = result * 26 + (ord(character) - ord("A") + 1)
    return result


def _validate_native_tsv(
    snapshot: GitSnapshot,
    path: str,
    expected_rows: int,
    expected_columns: int,
    expected_sha256: str,
) -> list[str]:
    errors: list[str] = []
    entry = snapshot.get(path)
    if entry is None:
        return [f"native-sheet TSV is missing: {path}"]
    if not entry.qualifies_as_evidence:
        return [f"native-sheet TSV is not a tracked regular non-LFS Git blob: {path}"]
    data = entry.data
    actual_sha256 = hashlib.sha256(data).hexdigest()
    if actual_sha256 != expected_sha256:
        errors.append(
            f"native-sheet TSV SHA-256 drift: {path}; "
            f"declared={expected_sha256}, actual={actual_sha256}"
        )
    if data.startswith(b"\xef\xbb\xbf"):
        errors.append(f"native-sheet TSV has a prohibited UTF-8 BOM: {path}")
    if b"\r" in data or b"\0" in data:
        errors.append(f"native-sheet TSV contains a prohibited control byte: {path}")
    if not data.endswith(b"\n"):
        errors.append(f"native-sheet TSV must end with exactly one LF-terminated row: {path}")
    try:
        text = data.decode("utf-8", "strict")
    except UnicodeDecodeError as exc:
        errors.append(f"native-sheet TSV is not strict UTF-8: {path}: {exc}")
        return errors
    if any(
        (ord(character) < 32 and character not in {"\t", "\n"})
        or 127 <= ord(character) <= 159
        for character in text
    ):
        errors.append(f"native-sheet TSV contains a prohibited text control: {path}")
    rows = text[:-1].split("\n") if text.endswith("\n") else text.split("\n")
    if len(rows) != expected_rows:
        errors.append(
            f"native-sheet TSV row-count drift: {path}; "
            f"declared={expected_rows}, actual={len(rows)}"
        )
    for row_number, row in enumerate(rows, 1):
        actual_columns = len(row.split("\t"))
        if actual_columns != expected_columns:
            errors.append(
                f"native-sheet TSV rectangularity failure: {path}:row={row_number}; "
                f"declared_columns={expected_columns}, actual_columns={actual_columns}"
            )
    return errors


def validate_native_sheets(snapshot: GitSnapshot, require_schema: bool) -> list[str]:
    """Validate native-sheet manifests and projections from exact snapshot blobs."""

    errors: list[str] = []
    schema_entry = snapshot.get(NATIVE_SHEET_SCHEMA)
    if schema_entry is None:
        return [f"native-sheet schema is missing: {NATIVE_SHEET_SCHEMA}"]
    if not schema_entry.qualifies_as_evidence:
        return [f"native-sheet schema is not a tracked regular Git blob: {NATIVE_SHEET_SCHEMA}"]
    try:
        schema = decode_json(schema_entry.data, NATIVE_SHEET_SCHEMA)
        if not isinstance(schema, Mapping):
            raise DomainError("native-sheet schema must be a JSON object")
        if require_schema:
            validate_schema_document(schema, "native-sheet structure schema")
    except (DomainError, json.JSONDecodeError, UnicodeDecodeError) as exc:
        return [str(exc)]

    try:
        mapping_rows = _snapshot_jsonl(snapshot, CROSSWALK_FILES["mapping"])
        result_rows = _snapshot_jsonl(snapshot, CROSSWALK_FILES["results"])
        plan_rows = _snapshot_jsonl(snapshot, CROSSWALK_FILES["plan"])
    except (DomainError, json.JSONDecodeError, UnicodeDecodeError) as exc:
        return [str(exc)]

    crosswalk_native_manifests = {
        row.get("git_path")
        for row in mapping_rows
        if row.get("transformation") == NATIVE_SHEET_TRANSFORMATION
        and isinstance(row.get("git_path"), str)
        and row["git_path"].endswith(".structure.json")
    }
    schema_id_native_manifests: set[str] = set()
    for path, entry in snapshot.entries.items():
        if not path.endswith(".structure.json"):
            continue
        try:
            candidate = decode_json(entry.data, path)
        except (DomainError, json.JSONDecodeError, UnicodeDecodeError):
            # Generic JSON validation reports malformed unrelated JSON. A path named
            # by the native crosswalk remains in the candidate set and fails below.
            continue
        if isinstance(candidate, Mapping) and candidate.get("schema") == NATIVE_SHEET_SCHEMA_ID:
            schema_id_native_manifests.add(path)
    manifest_paths = sorted(
        crosswalk_native_manifests | schema_id_native_manifests,
        key=lambda item: item.encode("utf-8"),
    )
    if not manifest_paths:
        return ["native-sheet schema is present but no structure manifest is tracked"]
    if not require_schema:
        return ["schema-engine deferral is prohibited for a native-sheet manifest"]

    represented_tsvs: set[str] = set()
    p03_manifest_count = 0
    for manifest_path in manifest_paths:
        entry = snapshot.get(manifest_path)
        if entry is None or not entry.qualifies_as_evidence:
            errors.append(
                f"native-sheet manifest is not a tracked regular non-LFS Git blob: "
                f"{manifest_path}"
            )
            continue
        try:
            manifest = decode_json(entry.data, manifest_path)
        except (DomainError, json.JSONDecodeError, UnicodeDecodeError) as exc:
            errors.append(str(exc))
            continue
        if not isinstance(manifest, Mapping):
            errors.append(f"native-sheet manifest is not an object: {manifest_path}")
            continue
        diagnostics = schema_diagnostics(manifest, schema, manifest_path)
        schema_failures = render_schema_diagnostics(diagnostics)
        if schema_failures:
            errors.append("\n".join(schema_failures))
            continue
        if manifest.get("schema") != NATIVE_SHEET_SCHEMA_ID:
            errors.append(f"unrecognized native-sheet manifest schema: {manifest_path}")
            continue
        source_drive_id = manifest["source_drive_id"]
        if source_drive_id == "1fDfRSY9oHovjAcO-YPItDfZlirPjlc3yL8IZQZMRRXg":
            p03_manifest_count += 1
            if manifest["worksheet_count"] != 17:
                errors.append("P03 native-sheet manifest must declare exactly 17 worksheets")
        worksheets = manifest["worksheets"]
        if manifest["worksheet_count"] != len(worksheets):
            errors.append(
                f"native-sheet worksheet_count mismatch: {manifest_path}; "
                f"declared={manifest['worksheet_count']}, actual={len(worksheets)}"
            )
        normalized_names: dict[str, str] = {}
        manifest_base = manifest_path[: -len(".structure.json")]
        tabs_prefix = f"{manifest_base}.tabs/"
        expected_tsvs: set[str] = set()
        for ordinal, worksheet in enumerate(worksheets):
            label = f"{manifest_path}:worksheets[{ordinal}]"
            if worksheet["index"] != ordinal:
                errors.append(
                    f"native-sheet worksheet indices are not contiguous and ordered: {label}"
                )
            name = worksheet["name"]
            folded = unicodedata.normalize("NFC", name).casefold()
            if folded in normalized_names:
                errors.append(
                    f"native-sheet worksheet name collision: "
                    f"{normalized_names[folded]!r} / {name!r}"
                )
            else:
                normalized_names[folded] = name
            match = EXCEL_RANGE_RE.fullmatch(worksheet["address"])
            if match is None:
                errors.append(f"native-sheet declared range is invalid: {label}")
            else:
                address_columns = _excel_column_number(match.group(1))
                address_rows = int(match.group(2))
                if address_columns != worksheet["columns"] or address_rows != worksheet["rows"]:
                    errors.append(
                        f"native-sheet declared range end/shape mismatch: {label}"
                    )
            if worksheet["formula_cells"] or worksheet["tables"] != 0:
                errors.append(f"native-sheet formulas and tables must both be zero: {label}")
            tsv_path = worksheet["tsv_destination_path"]
            try:
                validate_repository_path(tsv_path)
            except DomainError as exc:
                errors.append(f"{label}.tsv_destination_path is invalid: {exc}")
                continue
            expected_prefix = f"{ordinal + 1:02d}-"
            tsv_name = PurePosixPath(tsv_path).name
            if not tsv_path.startswith(tabs_prefix) or not tsv_name.startswith(expected_prefix):
                errors.append(
                    f"native-sheet TSV escapes exact .tabs/ containment or ordinal: {tsv_path}"
                )
            if tsv_path in expected_tsvs:
                errors.append(f"duplicate native-sheet TSV destination: {tsv_path}")
            expected_tsvs.add(tsv_path)
            represented_tsvs.add(tsv_path)
            errors.extend(
                _validate_native_tsv(
                    snapshot,
                    tsv_path,
                    worksheet["rows"],
                    worksheet["columns"],
                    worksheet["tsv_sha256"],
                )
            )
        sibling_tsvs = {
            path
            for path in snapshot.entries
            if path.startswith(tabs_prefix) and path.endswith(".tsv")
        }
        if sibling_tsvs != expected_tsvs:
            errors.append(
                f"native-sheet sibling TSV closure failure: {manifest_path}; "
                f"missing={sorted(expected_tsvs - sibling_tsvs)}, "
                f"orphan={sorted(sibling_tsvs - expected_tsvs)}"
            )

    unrepresented = sorted(
        (
            path
            for path in snapshot.entries
            if ".tabs/" in path and path.endswith(".tsv") and path not in represented_tsvs
        ),
        key=lambda item: item.encode("utf-8"),
    )
    if unrepresented:
        errors.append(f"orphan native-sheet TSV paths: {unrepresented}")
    tracked_xlsx = sorted(
        path
        for path, entry in snapshot.entries.items()
        if path.casefold().endswith(".xlsx") and entry.tracked
    )
    if tracked_xlsx:
        errors.append(f"native XLSX must remain REFERENCE_DRIVE: {tracked_xlsx}")
    if p03_manifest_count != 1:
        errors.append(
            f"P03 native-sheet manifest count must equal one; actual={p03_manifest_count}"
        )

    # Bind every manifest-derived Git object back to its exact three-leg records.
    for manifest_path in manifest_paths:
        entry = snapshot.get(manifest_path)
        if entry is None:
            continue
        try:
            manifest = decode_json(entry.data, manifest_path)
        except (DomainError, json.JSONDecodeError, UnicodeDecodeError):
            continue
        if not isinstance(manifest, Mapping) or manifest.get("schema") != NATIVE_SHEET_SCHEMA_ID:
            continue
        expected_paths = {manifest_path} | {
            item["tsv_destination_path"]
            for item in manifest.get("worksheets", [])
            if isinstance(item, Mapping) and isinstance(item.get("tsv_destination_path"), str)
        }
        source_drive_id = manifest.get("source_drive_id")
        source_sha256 = manifest.get("source_sha256")
        source_bytes = manifest.get("source_byte_length")
        study_id = PurePosixPath(manifest_path).parts[1]
        native_mappings = {
            row.get("git_path"): row
            for row in mapping_rows
            if row.get("drive_id") == source_drive_id
            and isinstance(row.get("transformation"), str)
            and (
                row["transformation"] == NATIVE_SHEET_TRANSFORMATION
                or row["transformation"].startswith(
                    NATIVE_SHEET_TRANSFORMATION + "_AND_"
                )
            )
        }
        if set(native_mappings) != expected_paths:
            errors.append(
                f"native-sheet drive-to-git closure failure: {manifest_path}; "
                f"missing={sorted(expected_paths - set(native_mappings))}, "
                f"extra={sorted(set(native_mappings) - expected_paths)}"
            )
        native_source_paths = {
            row.get("source_path")
            for row in native_mappings.values()
            if isinstance(row.get("source_path"), str)
        }
        native_source_path = (
            next(iter(native_source_paths)) if len(native_source_paths) == 1 else None
        )
        if native_source_path is None:
            errors.append(
                f"native-sheet mappings must bind one source_path: {manifest_path}"
            )
        for path, row in native_mappings.items():
            if row.get("source_sha256") != source_sha256:
                errors.append(f"native-sheet source SHA-256 crosswalk drift: {path}")
            if row.get("source_bytes") != source_bytes:
                errors.append(f"native-sheet source byte-length crosswalk drift: {path}")
            if row.get("source_revision") != manifest.get("source_drive_revision"):
                errors.append(f"native-sheet source revision crosswalk drift: {path}")
            if row.get("study_id") != study_id:
                errors.append(f"native-sheet study scope crosswalk drift: {path}")
        native_results = {
            row.get("destination_path"): row
            for row in result_rows
            if row.get("drive_id") == source_drive_id
            and row.get("result") == "MATERIALIZED_AND_HASH_VERIFIED"
            and isinstance(row.get("transformation"), str)
            and (
                row["transformation"] == NATIVE_SHEET_TRANSFORMATION
                or row["transformation"].startswith(
                    NATIVE_SHEET_TRANSFORMATION + "_AND_"
                )
            )
        }
        native_plans = {
            row.get("destination_path"): row
            for row in plan_rows
            if row.get("drive_id") == source_drive_id
            and isinstance(row.get("decision"), str)
            and row["decision"].startswith("MIGRATE_")
            and isinstance(row.get("transformation"), str)
            and (
                row["transformation"] == NATIVE_SHEET_TRANSFORMATION
                or row["transformation"].startswith(
                    NATIVE_SHEET_TRANSFORMATION + "_AND_"
                )
            )
        }
        if set(native_results) != expected_paths:
            errors.append(f"native-sheet materialization-result closure failure: {manifest_path}")
        if set(native_plans) != expected_paths:
            errors.append(f"native-sheet path-plan closure failure: {manifest_path}")
        for leg_label, records in (("result", native_results), ("plan", native_plans)):
            for path, row in records.items():
                if (
                    row.get("source_sha256") != source_sha256
                    or row.get("source_bytes") != source_bytes
                    or row.get("source_revision") != manifest.get("source_drive_revision")
                    or row.get("study_id") != study_id
                ):
                    errors.append(
                        f"native-sheet {leg_label} source/scope binding drift: {path}"
                    )
        references = [
            row
            for row in result_rows
            if row.get("drive_id") == source_drive_id
            and row.get("result") == "REFERENCE_VERIFIED_NOT_MATERIALIZED"
        ]
        if len(references) != 1:
            errors.append(f"native-sheet XLSX reference result count must equal one: {manifest_path}")
        elif (
            references[0].get("source_sha256") != source_sha256
            or references[0].get("source_bytes") != source_bytes
            or references[0].get("source_revision")
            != manifest.get("source_drive_revision")
            or references[0].get("source_path") != native_source_path
            or references[0].get("terminal_action") != "REFERENCE_DRIVE"
            or references[0].get("transformation") != NATIVE_SHEET_REFERENCE_TRANSFORMATION
        ):
            errors.append(f"native-sheet XLSX reference result binding drift: {manifest_path}")
        reference_plans_for_source = [
            row
            for row in plan_rows
            if row.get("drive_id") == source_drive_id and row.get("decision") == "REFERENCE_DRIVE"
        ]
        if len(reference_plans_for_source) != 1:
            errors.append(f"native-sheet XLSX reference plan count must equal one: {manifest_path}")
        elif (
            reference_plans_for_source[0].get("transformation")
            != NATIVE_SHEET_REFERENCE_TRANSFORMATION
            or reference_plans_for_source[0].get("source_sha256") != source_sha256
            or reference_plans_for_source[0].get("source_bytes") != source_bytes
            or reference_plans_for_source[0].get("source_revision")
            != manifest.get("source_drive_revision")
            or reference_plans_for_source[0].get("source_path") != native_source_path
        ):
            errors.append(f"native-sheet XLSX reference plan binding drift: {manifest_path}")
    return errors


def validate_current_domain(root: Path, snapshot: GitSnapshot, require_schema: bool) -> list[str]:
    errors: list[str] = []
    registry_entry = snapshot.get("characters/registry.jsonl")
    series_entry = snapshot.get("series/registry.json")
    discovery_schema_entry = snapshot.get("governance/schemas/character-analysis-index.schema.json")
    reconstruction_schema_entry = snapshot.get(
        "governance/schemas/character-reconstruction-capability.schema.json"
    )
    if not all((registry_entry, series_entry, discovery_schema_entry, reconstruction_schema_entry)):
        return ["current Character Index v2 inputs are incomplete"]
    try:
        records_with_lines = decode_jsonl_with_lines(
            registry_entry.data,
            f"{snapshot.identity}:characters/registry.jsonl",
        )
        records = [record for _line_number, record in records_with_lines]
        series_registry = decode_json(series_entry.data, "series/registry.json")
        discovery_schema = decode_json(
            discovery_schema_entry.data,
            "governance/schemas/character-analysis-index.schema.json",
        )
        reconstruction_schema = decode_json(
            reconstruction_schema_entry.data,
            "governance/schemas/character-reconstruction-capability.schema.json",
        )
        if require_schema:
            validate_schema_document(discovery_schema, "character discovery schema")
            validate_schema_document(reconstruction_schema, "reconstruction capability schema")
            diagnostics = []
            for line_number, record in records_with_lines:
                diagnostics.extend(
                    schema_diagnostics(
                        record,
                        discovery_schema,
                        "characters/registry.jsonl",
                        line_number=line_number,
                    )
                )
            schema_failures = render_schema_diagnostics(diagnostics)
            if schema_failures:
                errors.append("\n".join(schema_failures))
                return errors
        elif records:
            return [
                "schema-engine deferral is permitted only for an empty character registry"
            ]
        authority = AuthorityGraph(snapshot)
        errors.extend(authority.errors)
        errors.extend(
            validate_discovery_records(
                records,
                series_registry,
                snapshot=snapshot,
                authority=authority,
            )
        )
    except (DomainError, json.JSONDecodeError, UnicodeDecodeError) as exc:
        errors.append(str(exc))
    return errors


def choose_snapshot(root: Path, kind: str, commit: str | None) -> tuple[GitSnapshot, list[str]]:
    if kind == "commit":
        if commit is None:
            raise DomainError("--commit is required with --snapshot commit")
        snapshot = GitSnapshot.from_commit(root, commit)
        return snapshot, sorted(snapshot.entries)
    if commit is not None:
        raise DomainError("--commit is valid only with --snapshot commit")
    if kind == "index":
        snapshot = GitSnapshot.from_index(root)
        return snapshot, sorted(snapshot.entries)
    enumerated = worktree_paths(root)
    snapshot = worktree_snapshot(root, enumerated)
    return snapshot, sorted(snapshot.entries)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--phase", choices=["g3", "current"], default="current")
    parser.add_argument("--snapshot", choices=["worktree", "index", "commit"])
    parser.add_argument("--commit")
    parser.add_argument("--manifest", type=Path)
    parser.add_argument(
        "--defer-schema-engine",
        action="store_true",
        help="H0-H5 diagnostic only; never valid for a final H6 receipt",
    )
    parser.add_argument("--repo", type=Path)
    args = parser.parse_args()
    root = args.repo.resolve() if args.repo else Path(__file__).resolve().parents[1]
    kind = args.snapshot or ("commit" if args.phase == "g3" else "worktree")
    try:
        commit = args.commit
        if args.phase == "g3":
            commit = require_g3_selection(root, kind, commit, args.manifest is not None)
        elif kind == "commit" and commit is None:
            commit = run_git(root, "rev-parse", "HEAD").decode("ascii").strip()
        snapshot, paths = choose_snapshot(root, kind, commit)
        policy = _policy_from_snapshot(snapshot)
        if args.manifest:
            expected = read_external_manifest(args.manifest.resolve())
        else:
            manifest_name = G3_MANIFEST if args.phase == "g3" else CURRENT_MANIFEST
            expected = read_manifest_from_snapshot(snapshot, manifest_name)
        errors: list[str] = []
        errors.extend(validate_exact_set(paths, expected, args.phase))
        errors.extend(validate_paths(snapshot, policy))
        errors.extend(validate_bytes(snapshot, policy, args.phase))
        revision = identity_revision_for_snapshot(kind, commit)
        errors.extend(validate_commit_identities(root, policy, revision))
        if args.phase == "g3":
            errors.extend(validate_protected(snapshot))
        else:
            errors.extend(validate_protected(snapshot))
            errors.extend(validate_markdown_links(snapshot))
            errors.extend(validate_audit_workflow(snapshot, policy))
            errors.extend(validate_named_whitespace_exceptions(snapshot, policy))
            baseline_commit = active_migration_baseline_commit(snapshot)
            errors.extend(validate_active_authority_scope(snapshot, baseline_commit))
            errors.extend(
                validate_crosswalk_closure(snapshot, baseline_commit=baseline_commit)
            )
            errors.extend(validate_native_sheets(snapshot, not args.defer_schema_engine))
            errors.extend(validate_current_domain(root, snapshot, not args.defer_schema_engine))
            if not args.defer_schema_engine:
                generator_snapshot = "commit" if kind == "commit" else kind
                errors.extend(
                    validate_generated_index(
                        root,
                        generator_snapshot,
                        commit if kind == "commit" else None,
                    )
                )
        if errors:
            for error in sorted(set(errors), key=lambda item: item.encode("utf-8")):
                print(f"FAIL: {error}")
            return 1
        suffix = (
            " (schema engine explicitly deferred; generated-index CLI not independently invoked)"
            if args.defer_schema_engine
            else ""
        )
        print(
            f"PASS: phase={args.phase} snapshot={snapshot.identity} "
            f"paths={len(paths)}{suffix}"
        )
        return 0
    except (DomainError, OSError, ValueError) as exc:
        print(f"FAIL: {exc}")
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
