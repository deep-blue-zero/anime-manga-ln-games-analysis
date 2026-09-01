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
    "characters/registry.jsonl": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
    G3_MANIFEST: "75c6fe48adc719090828a2da02f3dc69e2334b8b20ee5f1c89e0f4c33ee6d191",
    "governance/repository-controls/bootstrap-bindings.json": "7ebb26e4cff22acbabe72905847f6efbbb6885c4a6be0b9e5297db22d654ae17",
}
RESERVED_ABSENT = {
    "characters/reconstruction_capabilities.jsonl",
    "characters/CHARACTER_RECONSTRUCTION_INDEX.md",
}


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
        if entry.mode != "100644":
            errors.append(f"non-regular or executable Git mode {entry.mode!r}: {path}")
    return errors


def validate_bytes(snapshot: GitSnapshot, policy: Mapping[str, Any], phase: str) -> list[str]:
    errors: list[str] = []
    threshold = int(policy["review_threshold_bytes"])
    text_extensions = set(policy["allowed_text_extensions"])
    special_text = {".gitattributes", ".gitignore", "CODEOWNERS"}
    for path, entry in snapshot.entries.items():
        data = entry.data
        if len(data) > threshold:
            errors.append(f"{phase} file exceeds 1 MiB review threshold: {path} ({len(data)} bytes)")
        for label, pattern in SECRET_PATTERNS.items():
            if pattern.search(data):
                errors.append(f"possible {label} in {path}")
        for label, pattern in PUBLICATION_PATTERNS.items():
            if pattern.search(data):
                errors.append(f"publication hazard ({label}) in {path}")
        suffix = Path(path).suffix.casefold()
        if suffix in text_extensions or Path(path).name in special_text:
            if data.startswith(b"\xef\xbb\xbf"):
                errors.append(f"UTF-8 BOM prohibited: {path}")
            if b"\r" in data:
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
    return errors


def validate_markdown_links(snapshot: GitSnapshot) -> list[str]:
    errors: list[str] = []
    paths = set(snapshot.entries)
    folded = {path.casefold(): path for path in paths}
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
            if unsafe or resolved not in paths:
                case_match = folded.get(resolved.casefold())
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
