#!/usr/bin/env python3
"""Fail-closed validation for the migration repository and G3 bootstrap."""

from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
import unicodedata
from pathlib import Path, PurePosixPath


WINDOWS_RESERVED = {
    "CON", "PRN", "AUX", "NUL",
    *(f"COM{i}" for i in range(1, 10)),
    *(f"LPT{i}" for i in range(1, 10)),
}
SECRET_PATTERNS = {
    "GitHub token": re.compile(rb"\b(?:ghp|gho|ghu|ghs|ghr)_[A-Za-z0-9]{20,}\b"),
    "private key": re.compile(rb"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
    "AWS access key": re.compile(rb"\bAKIA[0-9A-Z]{16}\b"),
    "Google API key": re.compile(rb"\bAIza[0-9A-Za-z_-]{30,}\b"),
}


class ValidationError(Exception):
    pass


def git(root: Path, *args: str) -> bytes:
    return subprocess.check_output(["git", "-C", str(root), *args])


def staged_paths(root: Path) -> list[str]:
    raw = git(root, "ls-files", "--cached", "-z")
    return [item.decode("utf-8", "strict") for item in raw.split(b"\0") if item]


def staged_modes(root: Path) -> dict[str, str]:
    raw = git(root, "ls-files", "--stage", "-z")
    result: dict[str, str] = {}
    for item in raw.split(b"\0"):
        if not item:
            continue
        metadata, path = item.split(b"\t", 1)
        result[path.decode("utf-8", "strict")] = metadata.split(b" ", 1)[0].decode("ascii")
    return result


def read_policy(root: Path) -> dict:
    path = root / "governance" / "repository-controls" / "tracked-file-policy.json"
    return json.loads(path.read_text(encoding="utf-8"))


def validate_paths(root: Path, paths: list[str], modes: dict[str, str], policy: dict) -> list[str]:
    errors: list[str] = []
    normalized: dict[str, str] = {}
    casefolded: dict[str, str] = {}
    allowed_roots = tuple(policy["allowed_roots"])
    allowed_root_files = set(policy["allowed_root_files"])
    forbidden = tuple(policy["forbidden_paths"])
    external_extensions = set(policy["default_external_extensions"])

    for path in paths:
        posix = PurePosixPath(path)
        if path.startswith("/") or ".." in posix.parts or "\\" in path:
            errors.append(f"unsafe path: {path}")
        if any(ord(char) < 32 or ord(char) == 127 for char in path):
            errors.append(f"control character in path: {path!r}")
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
            errors.append(f"forbidden tracked path: {path}")
        if Path(path).suffix.casefold() in external_extensions:
            errors.append(f"default-external artifact tracked without exception: {path}")
        if modes.get(path) != "100644":
            errors.append(f"non-regular or executable Git mode {modes.get(path)!r}: {path}")
        disk_path = root / Path(*posix.parts)
        if os.path.islink(disk_path):
            errors.append(f"symlink prohibited: {path}")
    return errors


def validate_bytes(root: Path, paths: list[str], policy: dict) -> list[str]:
    errors: list[str] = []
    threshold = int(policy["review_threshold_bytes"])
    text_extensions = set(policy["allowed_text_extensions"])
    special_text = {".gitattributes", ".gitignore", "CODEOWNERS"}
    for path in paths:
        data = (root / Path(*PurePosixPath(path).parts)).read_bytes()
        if len(data) > threshold:
            errors.append(f"G3 file exceeds 1 MiB review threshold: {path} ({len(data)} bytes)")
        for label, pattern in SECRET_PATTERNS.items():
            if pattern.search(data):
                errors.append(f"possible {label} in {path}")
        suffix = Path(path).suffix.casefold()
        if suffix in text_extensions or Path(path).name in special_text:
            if data.startswith(b"\xef\xbb\xbf"):
                errors.append(f"UTF-8 BOM prohibited in generated text: {path}")
            if b"\r" in data:
                errors.append(f"non-LF line ending in generated text: {path}")
            if b"\0" in data:
                errors.append(f"NUL byte in text file: {path}")
            try:
                data.decode("utf-8", "strict")
            except UnicodeDecodeError as exc:
                errors.append(f"invalid UTF-8 in {path}: {exc}")
        if suffix == ".json":
            try:
                json.loads(data)
            except (json.JSONDecodeError, UnicodeDecodeError) as exc:
                errors.append(f"invalid JSON in {path}: {exc}")
        if suffix == ".jsonl":
            for line_number, line in enumerate(data.decode("utf-8").splitlines(), 1):
                if not line.strip():
                    continue
                try:
                    json.loads(line)
                except json.JSONDecodeError as exc:
                    errors.append(f"invalid JSONL in {path}:{line_number}: {exc}")
    return errors


def validate_g3_exact_set(root: Path, paths: list[str]) -> list[str]:
    manifest = root / "governance" / "repository-controls" / "G3_BOOTSTRAP_TRACKED_PATHS.txt"
    expected = [line for line in manifest.read_text(encoding="utf-8").splitlines() if line]
    errors: list[str] = []
    if expected != sorted(expected):
        errors.append("G3 bootstrap path manifest is not sorted")
    if len(expected) != len(set(expected)):
        errors.append("G3 bootstrap path manifest contains duplicates")
    if sorted(paths) != expected:
        missing = sorted(set(expected) - set(paths))
        extra = sorted(set(paths) - set(expected))
        errors.append(f"G3 staged set mismatch; missing={missing}, extra={extra}")
    return errors


def validate_generated_index(root: Path) -> list[str]:
    result = subprocess.run(
        [sys.executable, str(root / "tools" / "generate_character_index.py"), "--check"],
        cwd=root,
        capture_output=True,
        text=True,
    )
    if result.returncode:
        return [result.stderr.strip() or result.stdout.strip() or "character index drift"]
    return []


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--phase", choices=["g3"], default="g3")
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[1]
    paths = staged_paths(root)
    if not paths:
        raise SystemExit("no staged/tracked paths to validate")
    policy = read_policy(root)
    errors = []
    errors.extend(validate_g3_exact_set(root, paths))
    errors.extend(validate_paths(root, paths, staged_modes(root), policy))
    errors.extend(validate_bytes(root, paths, policy))
    errors.extend(validate_generated_index(root))
    if errors:
        for error in errors:
            print(f"FAIL: {error}")
        return 1
    print(f"PASS: {len(paths)} G3 bootstrap paths validated")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
