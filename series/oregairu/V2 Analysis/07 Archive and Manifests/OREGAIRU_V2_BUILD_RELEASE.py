#!/usr/bin/env python3
"""Build and fully reopen a deterministic, Git-bound Oregairu analytical ZIP.

Scratch packaging helper; this does not authorize a release, integrate a branch,
fetch a remote, promote authority, or claim a curator action. The caller supplies
the exact source SHA and a fresh factual publication receipt. No worktree file is
read into the archive. Copyrighted primary-source payloads are outside selection.

Receipt required keys:
  repository_url, source_commit, release_state, source_boundary,
  main_verification: {verified: true, verified_commit: FULL_SHA,
                      contains_source_content: BOOL, ...actual evidence},
  full_integration_audit: {verified_commit: SOURCE_SHA, conclusion: "success", ...},
  character_discovery: {state: NONEMPTY_STRING, ...actual evidence}

main_verification records a caller-observed remote head; it need not equal the
candidate SHA. No integration or final-freeze conclusion is inferred from it.
Input receipt bytes are preserved unchanged as PUBLICATION_RECEIPT.json.
"""

from __future__ import annotations

import argparse
import hashlib
import io
import json
import posixpath
import re
import stat
import subprocess
import sys
from pathlib import Path, PurePosixPath
from urllib.parse import unquote, urlsplit
from zipfile import ZIP_STORED, ZipFile, ZipInfo


ROOT = "series/oregairu/V2 Analysis"
PREFIX = "Oregairu_V2"
ENTRYPOINT = "07 Archive and Manifests/OREGAIRU_V2_DRIVE_CORPUS_MAP.md"
READER_GUIDE = "06 Continuous Synthesis/00_README_AND_CORPUS_MAP.md"
BUILD_HELPER = "07 Archive and Manifests/OREGAIRU_V2_BUILD_RELEASE.py"
EXCLUSIONS = {
    "01 Legacy V1 and Source Control/Manga and anime discussions - Oregairu Deep-dive - Full Transcript.md":
        "Cold V1 dialogue transcript; recoverable from the exact source Git tree, outside reader analytical package.",
    "07 Archive and Manifests/OREGAIRU_V2_HANDOFF_PHASE4_AFTER_REQUEST_INTERVENTION_ETHICS_LEDGER.md":
        "Historical working handoff with obsolete local paths; recoverable from the exact source Git tree.",
}
TOP_DIRS = {
    "00 Frameworks", "01 Legacy V1 and Source Control", "02 V1 Claim Audit",
    "03 Volume Deep Readings", "04 Checkpoints and Longitudinal Ledgers",
    "05 Specialist Synthesis", "06 Continuous Synthesis", "07 Archive and Manifests",
}
LEGAL = ("LICENSE.md", "THIRD_PARTY_NOTICES.md")
GENERATED = ("START_HERE.md", "RELEASE_PROVENANCE.json", "PUBLICATION_RECEIPT.json", "PACKAGE_CHECKSUMS.json")
FIXED_TIME = (2026, 10, 17, 0, 0, 0)
SHA = re.compile(r"(?:[0-9a-f]{40}|[0-9a-f]{64})\Z")
ESCAPE = re.compile(r"\\([!\"#$%&'()*+,\-./:;<=>?@\[\\\]^_`{|}~])")


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def json_bytes(value: object) -> bytes:
    return (json.dumps(value, ensure_ascii=False, sort_keys=True, indent=2) + "\n").encode("utf-8")


def git(repo: Path, *args: str) -> bytes:
    # A local replacement ref must never change the objects bound to --commit.
    return subprocess.check_output(["git", "--no-replace-objects", "-C", str(repo), *args], stderr=subprocess.PIPE)


def replacement_ref_regression() -> dict:
    """Exercise real commit/blob replacements in an isolated, disposable repo."""
    import os
    import tempfile
    from unittest.mock import patch

    env = {key: value for key, value in os.environ.items() if not key.startswith("GIT_")}
    env.update(GIT_CONFIG_NOSYSTEM="1", GIT_CONFIG_GLOBAL=os.devnull)
    with tempfile.TemporaryDirectory(prefix="oregairu-release-regression-") as directory, patch.dict(os.environ, env, clear=True):
        repo = Path(directory)

        def fixture_git(*args: str) -> bytes:
            return subprocess.check_output(["git", "-C", str(repo), *args], stderr=subprocess.PIPE)

        fixture_git("init", "-q")
        fixture_git("config", "user.name", "Release regression fixture")
        fixture_git("config", "user.email", "fixture@example.invalid")
        files = {"series/registry.json": json_bytes({"series": [{"series_id": "oregairu", "canonical_entrypoint": ROOT + "/" + ENTRYPOINT}]}),
                 **{name: b"Fixture legal text.\n" for name in LEGAL},
                 **{ROOT + "/" + name: b"Fixture historical exclusion.\n" for name in EXCLUSIONS},
                 ROOT + "/" + ENTRYPOINT: b"# Fixture corpus map\n",
                 ROOT + "/" + READER_GUIDE: b"# Original fixture guide\n",
                 ROOT + "/" + BUILD_HELPER: Path(__file__).read_bytes(),
                 ROOT + "/03 Volume Deep Readings/FIXTURE.md": b"# Fixture analytical reading\n"}
        for name, data in files.items():
            path = repo / name
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes(data)
        fixture_git("add", "--", *files)
        fixture_git("commit", "-q", "-m", "Original fixture")
        original = fixture_git("rev-parse", "HEAD").decode().strip()
        baseline = select_git_blobs(repo, original)
        baseline_zip = zip_bytes(baseline[0])
        guide = ROOT + "/" + READER_GUIDE
        original_blob = fixture_git("rev-parse", original + ":" + guide).decode().strip()
        (repo / guide).write_bytes(b"# Substituted fixture guide\n")
        fixture_git("add", "--", guide)
        fixture_git("commit", "-q", "-m", "Replacement fixture")
        substitute = fixture_git("rev-parse", "HEAD").decode().strip()
        substitute_blob = fixture_git("rev-parse", substitute + ":" + guide).decode().strip()
        fixture_git("replace", original, substitute)
        require(fixture_git("rev-parse", original + "^{commit}").decode().strip() == original,
                "Fixture must preserve the apparent requested commit identity.")
        require(fixture_git("show", original + ":" + guide) != files[guide],
                "Fixture commit replacement must affect unprotected Git reads.")

        def unchanged(label: str) -> None:
            selected = select_git_blobs(repo, original)
            require(selected == baseline and zip_bytes(selected[0]) == baseline_zip,
                    label + " changed protected source tree, inventory or archive bytes.")

        unchanged("Commit replacement")
        fixture_git("replace", original_blob, substitute_blob)
        require(fixture_git("cat-file", "blob", original_blob) != files[guide],
                "Fixture blob replacement must affect unprotected Git reads.")
        require(git(repo, "cat-file", "blob", original_blob) == files[guide],
                "Protected blob read returned substituted content.")
        unchanged("Combined commit/blob replacements")
        fixture_git("replace", "-d", original)
        unchanged("Blob replacement")
    return {"commit_replacement": "PASS", "blob_replacement": "PASS", "combined_replacements": "PASS",
            "original_tree_inventory_and_archive_byte_identity": "PASS", "isolated_fixture_only": True}


def validate_text(name: str, data: bytes) -> str:
    suffix = PurePosixPath(name).suffix.lower()
    require(suffix in {".md", ".json"} or (suffix == ".py" and name.endswith("/" + BUILD_HELPER)), f"Unapproved file type: {name}")
    require(b"\x00" not in data, f"NUL/binary content: {name}")
    text = data.decode("utf-8", "strict")
    require(not any(ord(c) < 32 and c not in "\t\r\n" for c in text), f"Binary control character: {name}")
    require(not data.startswith((b"PK\x03\x04", b"%PDF", b"ID3", b"\x89PNG", b"\xff\xd8\xff")), f"Source/binary signature: {name}")
    if suffix != ".py":
        require(not re.search(r"/(?:workspace|mnt/data)/|[?&](?:sig|token|se|sp)=", text), f"Private local path or signed URL: {name}")
    if suffix == ".json":
        obj = json.loads(text)
        forbidden = {"raw_source_text", "primary_source_text", "ocr_text", "full_text", "page_text", "paragraph_text", "transcript_text", "transcription", "image_base64", "audio_base64", "epub_base64", "pdf_base64", "data_base64", "binary_payload"}
        def walk(value: object) -> None:
            if isinstance(value, dict):
                require(not (set(value) & forbidden), f"Potential primary-source payload JSON field in {name}: {sorted(set(value) & forbidden)}")
                for child in value.values(): walk(child)
            elif isinstance(value, list):
                for child in value: walk(child)
            elif isinstance(value, str):
                require("\x00" not in value, f"Decoded NUL in JSON string: {name}")
        walk(obj)
        if name.endswith("OREGAIRU_ANTHOLOGY_02_OCR_FINDINGS.json"):
            require(set(obj) == {"schema_version", "generated_at", "scope", "totals", "pages"}, "Unexpected OCR-findings JSON schema; inspect for source payload.")
            page_fields = {"reading_order", "source_id", "book_page", "content_type", "review_status", "selected_tesseract_confidence", "tesseract_pass_agreement", "audit_flags", "raw_machine_characters", "final_machine_readable_characters", "machine_to_final_compact_similarity", "paddle_audited_lines", "flagged_or_disputed_lines"}
            require(isinstance(obj["pages"], list) and all(isinstance(row, dict) and set(row) == page_fields for row in obj["pages"]), "OCR-findings page records are no longer metadata-only.")
        if name.endswith("OREGAIRU_ANTHOLOGY_02_INVENTORY_SUMMARY.json"):
            require(set(obj) == {"schema_version", "created_at", "source_root", "source_images", "body_pages", "jacket_pages", "total_bytes", "hash_algorithm", "source_mutation", "reading_order_policy"}, "Unexpected inventory-summary schema; inspect for source payload.")
    return text


def read_receipt(path: Path, source_commit: str) -> tuple[bytes, dict]:
    raw = path.read_bytes()
    text = validate_text("PUBLICATION_RECEIPT.json", raw)
    receipt = json.loads(text)
    require(isinstance(receipt, dict), "Receipt must be a JSON object.")
    for key in ("repository_url", "source_commit", "release_state", "source_boundary", "main_verification", "full_integration_audit", "character_discovery"):
        require(key in receipt, f"Receipt missing required key: {key}")
    require(receipt["source_commit"] == source_commit, "Receipt source_commit must exactly match --commit.")
    require(receipt["repository_url"] == "https://github.com/deep-blue-zero/anime-manga-ln-games-analysis", "Unexpected receipt repository_url.")
    require(isinstance(receipt["release_state"], str) and receipt["release_state"].strip(), "Receipt release_state must be explicit.")
    require(isinstance(receipt["source_boundary"], (str, dict)) and bool(receipt["source_boundary"]), "Receipt source_boundary must be explicit.")
    main = receipt["main_verification"]
    require(isinstance(main, dict) and main.get("verified") is True, "Receipt must record an actual main observation (verified:true).")
    require(isinstance(main.get("verified_commit"), str) and bool(SHA.fullmatch(main["verified_commit"])), "Receipt main verified_commit must be a full SHA.")
    require(type(main.get("contains_source_content")) is bool, "Receipt must explicitly state main contains_source_content true/false.")
    audit = receipt["full_integration_audit"]
    require(isinstance(audit, dict) and audit.get("verified_commit") == source_commit and audit.get("conclusion") == "success", "Receipt requires successful full integration audit of exact source SHA.")
    discovery = receipt["character_discovery"]
    require(isinstance(discovery, dict) and isinstance(discovery.get("state"), str) and bool(discovery["state"].strip()), "Receipt must explicitly record character discovery state.")
    return raw, receipt


def select_git_blobs(repo: Path, commit: str) -> tuple[dict[str, bytes], list[dict], str]:
    require(bool(SHA.fullmatch(commit)), "--commit must be a full lowercase commit SHA.")
    actual = git(repo, "rev-parse", "--verify", commit + "^{commit}").decode().strip()
    require(actual == commit, "Supply an exact full commit SHA, not a tag, branch or abbreviation.")
    tree = git(repo, "rev-parse", commit + "^{tree}").decode().strip()
    registry = json.loads(git(repo, "show", commit + ":series/registry.json"))
    registered = [entry for entry in registry["series"] if entry.get("series_id") == "oregairu"]
    require(len(registered) == 1 and registered[0].get("canonical_entrypoint") == ROOT + "/" + ENTRYPOINT, "Exact source commit no longer registers the expected single canonical entrypoint; inspect routing before packaging.")
    entries = git(repo, "ls-tree", "-r", "-z", "--full-tree", commit, "--", ROOT, *LEGAL).split(b"\0")
    members: dict[str, bytes] = {}
    inventory: list[dict] = []
    excluded_seen: set[str] = set()
    for entry in entries:
        if not entry:
            continue
        header, raw_path = entry.split(b"\t", 1)
        mode, kind, oid = header.decode("ascii").split()
        path = raw_path.decode("utf-8", "strict")
        require(kind == "blob" and mode in {"100644", "100755"}, f"Nonregular Git member rejected: {path}")
        require("\\" not in path and not path.startswith("/") and ".." not in PurePosixPath(path).parts, f"Unsafe Git path: {path}")
        if path in LEGAL:
            relative = path
            role = "repository_license_or_notice"
        else:
            require(path.startswith(ROOT + "/"), f"Outside canonical scope: {path}")
            relative = path[len(ROOT) + 1:]
            if relative in EXCLUSIONS:
                excluded_seen.add(relative)
                continue
            require(PurePosixPath(relative).parts[0] in TOP_DIRS, f"Unrecognized analytical home requires explicit review: {path}")
            role = "canonical_root_analytical_or_provenance_text"
        require(relative not in GENERATED, f"Generated package-name collision: {relative}")
        archive_path = PREFIX + "/" + relative
        require(archive_path not in members, f"Duplicate archive path: {archive_path}")
        data = git(repo, "cat-file", "blob", oid)
        validate_text(path, data)
        hash_name = "sha1" if len(oid) == 40 else "sha256"
        exact_oid = hashlib.new(hash_name, b"blob " + str(len(data)).encode("ascii") + b"\0" + data).hexdigest()
        require(exact_oid == oid, f"Git blob identity mismatch: {path}")
        members[archive_path] = data
        inventory.append({"git_path": path, "archive_path": archive_path, "git_blob_oid": oid,
                          "git_mode": mode, "bytes": len(data), "sha256": sha256(data), "role": role})
    require(excluded_seen == set(EXCLUSIONS), "Expected both historical exclusions in source commit; inspect changed scope.")
    for required in (*LEGAL, ENTRYPOINT, READER_GUIDE, BUILD_HELPER):
        require(PREFIX + "/" + required in members, f"Required source-commit member absent: {required}")
    require(any("/03 Volume Deep Readings/" in p for p in members), "No source-facing analytical readings selected.")
    return members, sorted(inventory, key=lambda x: x["archive_path"]), tree


def mask_nonprose(text: str) -> str:
    """Mask code/front matter/comments without the quadratic link regex trap."""
    lines = text.splitlines(keepends=True)
    result: list[str] = []
    fence_char = ""
    fence_len = 0
    yaml = bool(lines and lines[0].strip() == "---")
    for index, line in enumerate(lines):
        if yaml:
            result.append("\n" if line.endswith("\n") else "")
            if index and line.strip() in {"---", "..."}:
                yaml = False
            continue
        fence = re.match(r"^ {0,3}(`{3,}|~{3,})", line)
        if fence_char:
            result.append("\n" if line.endswith("\n") else "")
            if fence and fence[1][0] == fence_char and len(fence[1]) >= fence_len and not line[fence.end():].strip():
                fence_char = ""
            continue
        if fence:
            fence_char, fence_len = fence[1][0], len(fence[1])
            result.append("\n" if line.endswith("\n") else "")
            continue
        result.append(line)
    visible = "".join(result)
    visible = re.sub(r"<!--[\s\S]*?-->", "", visible)
    out: list[str] = []
    i = 0
    while i < len(visible):
        if visible[i] != "`" or (i and visible[i-1] == "\\"):
            out.append(visible[i]); i += 1; continue
        j = i
        while j < len(visible) and visible[j] == "`":
            j += 1
        marker = visible[i:j]
        end = visible.find(marker, j)
        if end < 0:
            out.append(marker); i = j
        else:
            out.append(" " * (end + len(marker) - i)); i = end + len(marker)
    return "".join(out)


def destination(text: str, start: int, inline: bool) -> tuple[str, int] | None:
    """Parse a Markdown destination plus optional title; return URL/end offset."""
    n = len(text); i = start
    while i < n and text[i].isspace(): i += 1
    begin = i
    if i < n and text[i] == "<":
        i += 1; begin = i
        while i < n and text[i] != ">":
            if text[i] in "\r\n<": return None
            i += 2 if text[i] == "\\" and i + 1 < n else 1
        if i == n: return None
        url = text[begin:i]; i += 1
    else:
        depth = 0
        while i < n:
            c = text[i]
            if c == "\\" and i + 1 < n: i += 2; continue
            if c.isspace(): break
            if c == "(": depth += 1
            elif c == ")":
                if depth == 0: break
                depth -= 1
            i += 1
        if depth: return None
        url = text[begin:i]
    if not inline:
        return ESCAPE.sub(r"\1", url), i
    while i < n and text[i].isspace(): i += 1
    if i < n and text[i] == ")":
        return ESCAPE.sub(r"\1", url), i + 1
    if i < n and text[i] in "\"'(":
        end_marker = ")" if text[i] == "(" else text[i]
        i += 1
        while i < n and text[i] != end_marker:
            i += 2 if text[i] == "\\" and i + 1 < n else 1
        if i == n: return None
        i += 1
        while i < n and text[i].isspace(): i += 1
        if i < n and text[i] == ")":
            return ESCAPE.sub(r"\1", url), i + 1
    return None


def markdown_destinations(text: str) -> list[str]:
    """Inline/image and defined reference links, ignoring literal code text.

    Covers package Markdown link forms, balanced labels/parentheses, angle
    destinations, escaped punctuation and optional titles. HTML hrefs/fragment
    existence are outside the Markdown-relative-file validation contract.
    """
    text = mask_nonprose(text)
    definitions: dict[str, str] = {}
    def label_key(s: str) -> str: return " ".join(s.split()).casefold()
    for line in text.splitlines():
        m = re.match(r"^ {0,3}\[([^\]\r\n]+)\]:[ \t]*(.*)$", line)
        if m:
            parsed = destination(m[2], 0, False)
            if parsed: definitions.setdefault(label_key(m[1]), parsed[0])
    # Match labels once so unmatched openers never rescan the same suffix.
    closers: dict[int, int] = {}
    openers: list[int] = []
    i = 0; n = len(text)
    while i < n:
        char = text[i]
        if char == "\\": i += 2; continue
        if char == "[": openers.append(i)
        elif char == "]" and openers:
            closers[openers.pop()] = i + 1
        i += 1
    urls: list[str] = []
    i = 0
    while i < n:
        if text[i] == "\\": i += 2; continue
        if text[i] != "[": i += 1; continue
        begin = i + 1; j = closers.get(i)
        if j is None:
            # An unmatched opener is literal text; later links still count.
            i = begin
            continue
        label = text[begin:j-1]
        if j < n and text[j] == "(":
            parsed = destination(text, j + 1, True)
            if parsed: urls.append(parsed[0]); i = parsed[1]; continue
        elif j < n and text[j] == "[":
            end = text.find("]", j + 1)
            if end >= 0:
                key = label_key(text[j+1:end] or label)
                if key in definitions: urls.append(definitions[key])
                i = end + 1; continue
        else:
            key = label_key(label)
            if key in definitions: urls.append(definitions[key])
        i = j
    return urls


def check_relative_links(members: dict[str, bytes]) -> dict:
    count = 0; external = 0; fragments = 0; failures: list[dict] = []
    for name, data in sorted(members.items()):
        if not name.endswith(".md"): continue
        for target in markdown_destinations(data.decode("utf-8", "strict")):
            parsed = urlsplit(target)
            if parsed.scheme or parsed.netloc:
                require(parsed.scheme.casefold() not in {"file", "sandbox"}, f"Private local URL in {name}: {target}")
                external += 1; continue
            if not parsed.path:
                fragments += 1; continue
            raw_path = unquote(parsed.path)
            require("\\" not in raw_path and "\x00" not in raw_path and not raw_path.startswith("/"), f"Unsafe local link in {name}: {target}")
            resolved = posixpath.normpath(posixpath.join(posixpath.dirname(name), raw_path))
            count += 1
            if not resolved.startswith(PREFIX + "/") or not (resolved in members or any(p.startswith(resolved.rstrip("/") + "/") for p in members)):
                failures.append({"member": name, "target": target, "resolved": resolved})
    require(not failures, "Unresolved archive-relative Markdown links:\n" + json.dumps(failures, ensure_ascii=False, indent=2))
    return {"relative_file_or_directory_links_checked": count, "external_links_not_fetched": external,
            "fragment_only_links_not_anchor_validated": fragments, "result": "PASS",
            "scope": "Markdown inline/image/defined-reference destinations; file existence only; no HTML href or heading-anchor claim"}


def markdown_link_regression() -> dict:
    """Check scanner recovery and actual missing-member rejection in memory."""
    from unittest.mock import patch

    prefixes = ("", "[unmatched ", "[unmatched\n", "[first [second\n")
    labels = ("link", "outer [nested] label", r"escaped \[brackets\] label", r"escaped closer \] label")
    cases = [
        ("[normal](valid.md)", ["valid.md"]),
        ("[one](valid.md) [two](other.md)", ["valid.md", "other.md"]),
        ("[outer [nested] label](valid.md)", ["valid.md"]),
        (r"[escaped \[brackets\] label](valid.md)", ["valid.md"]),
        (r"\[literal\] [normal](valid.md)", ["valid.md"]),
        (r"\[literal](missing.md) [normal](valid.md)", ["valid.md"]),
        (r"[escaped closer \] label](valid.md)", ["valid.md"]),
        ("![image](valid.md)", ["valid.md"]),
        (r"\\[even escape](valid.md)", ["valid.md"]),
        (r"\\\[odd escape](missing.md) [normal](valid.md)", ["valid.md"]),
        (r"[outer [nested \] bracket] label](valid.md)", ["valid.md"]),
        ("] ] [normal](valid.md)", ["valid.md"]),
        ("[ unmatched opener\n[broken](missing.md)", ["missing.md"]),
    ]
    for prefix in prefixes:
        for target in ("missing.md", "valid.md"):
            for label in labels:
                cases.append((prefix + f"[{label}]({target})", [target]))
    for text, expected in cases:
        require(markdown_destinations(text) == expected,
                f"Markdown destination regression: {text!r}; expected {expected!r}")
    for prefix in prefixes:
        for target in ("missing.md", "valid.md"):
            for label in labels:
                members = {PREFIX + "/start.md": (prefix + f"[{label}]({target})").encode("utf-8"),
                           PREFIX + "/valid.md": b"# Valid fixture member\n"}
                try:
                    result = check_relative_links(members)
                except ValueError as exc:
                    require(target == "missing.md" and "Unresolved archive-relative Markdown links:" in str(exc)
                            and '"target": "missing.md"' in str(exc),
                            f"Unexpected Markdown link rejection: {exc}")
                else:
                    require(target == "valid.md" and result["result"] == "PASS"
                            and result["relative_file_or_directory_links_checked"] == 1,
                            f"Missing or uncounted Markdown link: {prefix!r} {target}")

    class CountedText(str):
        def __new__(cls, value: str):
            result = super().__new__(cls, value)
            result.reads = 0
            return result

        def __getitem__(self, key):
            self.reads += len(range(*key.indices(len(self)))) if isinstance(key, slice) else 1
            return super().__getitem__(key)

    scaling: list[dict] = []
    for size in (64, 128, 256):
        for name, text, expected in (
            ("unmatched", "[" * size, []),
            ("unmatched_then_link", "[" * size + "[link](valid.md)", ["valid.md"]),
            ("nested_label", "[" * size + "label" + "]" * size + "(valid.md)", ["valid.md"]),
        ):
            counted = CountedText(text)
            # Observe the visible scanner, charging slices for every copied character.
            with patch.dict(globals(), {"mask_nonprose": lambda _: counted}):
                actual = markdown_destinations(text)
            require(actual == expected, f"Scaling fixture lost destinations: {name} {size}")
            budget = 8 * len(text) + 64
            require(counted.reads <= budget,
                    f"Nonlinear bracket scan: {name} {size}: {counted.reads} reads > {budget}")
            scaling.append({"case": name, "size": size, "character_reads": counted.reads, "budget": budget})
    return {"destination_cases": len(cases), "member_validation_cases": len(prefixes) * 2 * len(labels),
            "linear_scan_cases": scaling,
            "unmatched_openers_missing_and_valid_links": "PASS", "result": "PASS"}


def add_generated(members: dict[str, bytes], inventory: list[dict], tree: str, commit: str,
                  receipt_raw: bytes, receipt: dict, script_hash: str) -> dict:
    state = receipt["release_state"]
    start = ("# Oregairu V2 analytical package\n\n"
             "[Start at the registered canonical corpus map](07%20Archive%20and%20Manifests/OREGAIRU_V2_DRIVE_CORPUS_MAP.md).\n\n"
             "[Reader navigation](06%20Continuous%20Synthesis/00_README_AND_CORPUS_MAP.md) is subordinate to that map.\n\n"
             f"Source commit: `{commit}`.\n\nReceipt release state: `{state}`.\n\n"
             "[Publication receipt](PUBLICATION_RECEIPT.json) records actual main, audit, and discovery state. "
             "This package does not itself integrate or freeze the source branch.\n\n"
             "[License](LICENSE.md) · [Third-party notices](THIRD_PARTY_NOTICES.md). "
             "No primary-source payloads are included.\n")
    members[PREFIX + "/START_HERE.md"] = start.encode("utf-8")
    members[PREFIX + "/PUBLICATION_RECEIPT.json"] = receipt_raw
    pre_links = check_relative_links(members)
    provenance = {
        "schema_version": "1.0", "package_type": "text_only_analytical_release_candidate_or_release_as_receipted",
        "repository_url": receipt["repository_url"], "source_commit": commit, "source_tree": tree,
        "source_selection": ROOT, "package_prefix": PREFIX, "release_state": state,
        "registered_entrypoint": PREFIX + "/" + ENTRYPOINT,
        "subordinate_reader_guide": PREFIX + "/" + READER_GUIDE,
        "authority_note": "The existing registered corpus map remains the sole current-state entrypoint. Packaging confers no integration, final freeze, global discovery enrollment or capability qualification.",
        "publication_receipt": {"member": PREFIX + "/PUBLICATION_RECEIPT.json", "bytes": len(receipt_raw),
                                "sha256": sha256(receipt_raw), "preservation": "Exact supplied input bytes; external assertions are caller-provided, not independently inferred by this helper."},
        "provided_publication_state": receipt,
        "packaging_helper_sha256": script_hash, "packaging_helper_git_path": ROOT + "/" + BUILD_HELPER,
        "format": {"zip_compression": "ZIP_STORED", "member_timestamp": "2026-10-17T00:00:00", "unix_file_mode": "0644", "member_order": "lexicographic", "dynamic_timestamp": False},
        "source_payload_policy": "Only Git-tracked .md/.json analytical and metadata files in the exact canonical root, its one exact .py reproducibility helper, and two legal texts; no EPUB/PDF/audio/image/source-transcription file copied from source storage. No worktree or source-storage file is selected. Text/type/schema checks supplement the caller's substantive source-payload review; they do not automatically determine copyright or classify every possible prose quotation.",
        "excluded_git_paths": [{"git_path": ROOT + "/" + p, "reason": reason} for p, reason in sorted(EXCLUSIONS.items())],
        "git_blob_inventory": inventory, "archive_relative_link_validation": pre_links,
        "reproducibility": "Use this exact helper SHA, source commit and receipt bytes; builder constructs twice, compares complete ZIP bytes, and reopens every written member with CRC and SHA verification.",
    }
    members[PREFIX + "/RELEASE_PROVENANCE.json"] = json_bytes(provenance)
    checksums = {"schema_version": "1.0", "algorithm": "SHA-256", "path_base": "archive_root",
                 "self_exclusion": PREFIX + "/PACKAGE_CHECKSUMS.json intentionally excludes itself; ZIP SHA-256 is reported outside the archive to avoid self-reference.",
                 "members": [{"path": p, "bytes": len(data), "sha256": sha256(data)} for p, data in sorted(members.items())]}
    members[PREFIX + "/PACKAGE_CHECKSUMS.json"] = json_bytes(checksums)
    for name, data in members.items(): validate_text(name, data)
    check_relative_links(members)
    return provenance


def zip_bytes(members: dict[str, bytes]) -> bytes:
    stream = io.BytesIO()
    with ZipFile(stream, "w", compression=ZIP_STORED, allowZip64=True) as archive:
        archive.comment = b""
        for name, data in sorted(members.items()):
            info = ZipInfo(name, date_time=FIXED_TIME)
            info.compress_type = ZIP_STORED
            info.create_system = 3
            info.create_version = 20
            info.extract_version = 20
            info.external_attr = (stat.S_IFREG | 0o644) << 16
            info.internal_attr = 0
            info.extra = b""
            info.comment = b""
            archive.writestr(info, data)
    return stream.getvalue()


def verify_archive(source: io.BytesIO | Path, expected: dict[str, bytes], inventory: list[dict]) -> None:
    with ZipFile(source, "r") as archive:
        names = archive.namelist()
        require(names == sorted(expected) and len(names) == len(set(names)), "Duplicate/unexpected archive member or ordering.")
        require(archive.testzip() is None, "ZIP CRC verification failed.")
        require(archive.comment == b"", "Unexpected ZIP archive comment.")
        reopened: dict[str, bytes] = {}
        for info in archive.infolist():
            require(info.date_time == FIXED_TIME and info.compress_type == ZIP_STORED, f"ZIP metadata mismatch: {info.filename}")
            require(info.create_system == 3 and stat.S_IMODE(info.external_attr >> 16) == 0o644 and stat.S_ISREG(info.external_attr >> 16), f"ZIP mode mismatch: {info.filename}")
            require(info.extra == b"" and info.comment == b"", f"Unexpected member metadata: {info.filename}")
            data = archive.read(info.filename)
            validate_text(info.filename, data)
            require(data == expected[info.filename], f"ZIP byte readback mismatch: {info.filename}")
            reopened[info.filename] = data
        checks = json.loads(reopened[PREFIX + "/PACKAGE_CHECKSUMS.json"])
        listed = checks["members"]
        require([x["path"] for x in listed] == sorted(set(expected) - {PREFIX + "/PACKAGE_CHECKSUMS.json"}), "Package checksum inventory mismatch.")
        for row in listed:
            data = reopened[row["path"]]
            require(row["bytes"] == len(data) and row["sha256"] == sha256(data), f"Package checksum mismatch: {row['path']}")
        for row in inventory:
            data = reopened[row["archive_path"]]
            oid = row["git_blob_oid"]
            algo = "sha1" if len(oid) == 40 else "sha256"
            require(hashlib.new(algo, b"blob " + str(len(data)).encode("ascii") + b"\0" + data).hexdigest() == oid, f"Reopened Git blob mismatch: {row['git_path']}")
        check_relative_links(reopened)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--self-test", action="store_true", help="Run isolated Git replacement-ref and Markdown-link regressions; no packaging inputs required.")
    parser.add_argument("--repo", type=Path)
    parser.add_argument("--commit")
    parser.add_argument("--output", type=Path)
    parser.add_argument("--receipt", type=Path)
    args = parser.parse_args()
    if args.self_test:
        require(not any((args.repo, args.commit, args.output, args.receipt)), "--self-test takes no packaging inputs.")
        print(json.dumps({**replacement_ref_regression(), "markdown_links": markdown_link_regression()}, indent=2))
        return
    if any(value is None for value in (args.repo, args.commit, args.output, args.receipt)):
        parser.error("packaging requires --repo, --commit, --output and --receipt")
    repo = args.repo.resolve(); output = args.output.resolve(); receipt_path = args.receipt.resolve()
    require(repo.is_dir(), "Repository does not exist.")
    require(output.suffix.lower() == ".zip", "Output must have .zip suffix.")
    require(not output.is_relative_to(repo) and not receipt_path.is_relative_to(repo), "Output and factual receipt must stay outside repository.")
    require(output != receipt_path, "Output must not replace receipt.")
    receipt_raw, receipt = read_receipt(receipt_path, args.commit)
    members, inventory, tree = select_git_blobs(repo, args.commit)
    helper_hash = sha256(Path(__file__).read_bytes())
    require(members[PREFIX + "/" + BUILD_HELPER] == Path(__file__).read_bytes(), "Executed helper bytes must match the helper blob included in exact source commit.")
    provenance = add_generated(members, inventory, tree, args.commit, receipt_raw, receipt, helper_hash)
    first = zip_bytes(members); second = zip_bytes(members)
    require(first == second and sha256(first) == sha256(second), "Deterministic double-build failed.")
    verify_archive(io.BytesIO(first), members, inventory)
    output.parent.mkdir(parents=True, exist_ok=True)
    if output.exists():
        require(output.is_file() and output.read_bytes() == first, "Output exists with different bytes; choose a new output path.")
    else:
        with output.open("xb") as handle: handle.write(first)
    verify_archive(output, members, inventory)
    require(output.read_bytes() == first, "Final ZIP bytes differ from deterministic construction.")
    print(json.dumps({"output": str(output), "bytes": len(first), "sha256": sha256(first),
                      "source_commit": args.commit, "source_tree": tree, "git_blob_members": len(inventory),
                      "archive_members": len(members), "receipt_raw_sha256": sha256(receipt_raw),
                      "release_state": receipt["release_state"], "main_verification": receipt["main_verification"],
                      "character_discovery_state": receipt["character_discovery"]["state"],
                      "packaging_helper_sha256": helper_hash,
                      "double_build_byte_identity": "PASS", "all_member_crc_sha_git_blob_readback": "PASS",
                      "relative_markdown_file_links": provenance["archive_relative_link_validation"]}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    try:
        main()
    except (ValueError, UnicodeError, OSError, subprocess.CalledProcessError) as exc:
        print("PACKAGING FAILED: " + str(exc), file=sys.stderr)
        sys.exit(1)
