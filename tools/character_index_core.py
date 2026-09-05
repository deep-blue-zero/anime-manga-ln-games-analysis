#!/usr/bin/env python3
"""Shared fail-closed primitives for Character Index v2.

This module deliberately keeps repository policy separate from presentation.  It
never normalizes stored data in place, never hashes worktree bytes as evidence,
and never treats prose as authority.
"""

from __future__ import annotations

import hashlib
import json
import os
import re
import subprocess
import unicodedata
from collections import Counter, defaultdict, deque
from dataclasses import dataclass
from pathlib import Path, PurePosixPath
from typing import Any, Iterable, Mapping, Sequence


UNICODE_VERSION = "15.0.0"
CANONICALIZATION_PROFILE = "CHARACTER_INDEX_V2_C14N_1"
EVIDENCE_SET_ALGORITHM = "CHARACTER_EVIDENCE_SET_V1"
ID_RE = re.compile(r"^[a-z0-9][a-z0-9-]*$")
ENTITY_ID_RE = re.compile(r"^[a-z0-9][a-z0-9-]*:[a-z0-9][a-z0-9-]*$")
SUBJECT_ID_RE = re.compile(
    r"^[a-z0-9][a-z0-9-]*:[a-z0-9][a-z0-9-]*@[a-z0-9][a-z0-9-]*$"
)
EVIDENCE_REF_RE = re.compile(
    r"^[a-z0-9][a-z0-9-]*:[a-z0-9][a-z0-9-]*@[a-z0-9][a-z0-9-]*#[a-z0-9][a-z0-9-]*$"
)
FULL_COMMIT_RE = re.compile(r"^(?:[0-9a-f]{40}|[0-9a-f]{64})$")
HEX64_RE = re.compile(r"^[0-9a-f]{64}$")
AUTHORITY_STATUSES = {
    "canonical",
    "active_provisional",
    "draft_noncurrent",
    "superseded",
    "historical_legacy",
}
AUTHORITY_KEYS = {
    "status",
    "supersedes",
    "superseded_by",
    "do_not_use_as_current_authority",
}
ANALYTICAL_DIMENSIONS = {
    "BEHAVIOR",
    "PSYCHOLOGY",
    "SPEECH",
    "ETHICS",
    "RELATIONSHIPS",
    "IDEOLOGY",
    "DECISION_MAKING",
}
RECONSTRUCTION_DIMENSIONS = {
    "PSYCHOLOGICAL_MODEL",
    "LONGITUDINAL_STATE",
    "VOICE_REGISTER",
    "MUNDANE_BEHAVIOR",
    "RELATIONSHIP_CONDITIONING",
    "INTERIORITY",
    "CONFLICT_BEHAVIOR",
    "ETHICAL_DELIBERATION",
    "HUMOR_PLAY",
    "SOURCE_COMPLETENESS",
    "NEGATIVE_EVIDENCE",
    "TEMPORAL_SPECIFICITY",
}
SCENARIO_CATEGORIES = {
    "DIALOGUE",
    "CROSS_SCENARIO",
    "MUNDANE_SOCIAL",
    "ETHICAL_DELIBERATION",
    "ROMANCE_RELATIONSHIP",
    "PROFESSIONAL_CONTEXT",
}
LFS_PREFIXES = (
    b"version https://git-lfs.github.com/spec/v1\n",
    b"version https://git-lfs.github.com/spec/v1\r\n",
)


class DomainError(ValueError):
    """A deterministic validation or resolution failure."""


def require_unicode_profile() -> None:
    if unicodedata.unidata_version != UNICODE_VERSION:
        raise DomainError(
            f"{CANONICALIZATION_PROFILE} requires Unicode {UNICODE_VERSION}; "
            f"runtime exposes {unicodedata.unidata_version}"
        )


def _reject_surrogates(value: str, label: str) -> None:
    try:
        value.encode("utf-8", "strict")
    except UnicodeEncodeError as exc:
        raise DomainError(f"{label}: lone surrogate is prohibited") from exc


def require_nfc(value: str, label: str) -> None:
    require_unicode_profile()
    _reject_surrogates(value, label)
    if unicodedata.normalize("NFC", value) != value:
        raise DomainError(f"{label}: stored string is not Unicode NFC")


def fold(value: str) -> str:
    require_nfc(value, "comparison value")
    return unicodedata.normalize("NFC", value.casefold())


def sort_key(value: str) -> tuple[bytes, bytes]:
    require_nfc(value, "sort value")
    return (fold(value).encode("utf-8"), value.encode("utf-8"))


def validate_nfc_tree(value: Any, label: str = "$") -> None:
    if isinstance(value, str):
        require_nfc(value, label)
    elif isinstance(value, list):
        for index, item in enumerate(value):
            validate_nfc_tree(item, f"{label}[{index}]")
    elif isinstance(value, dict):
        for key, item in value.items():
            if not isinstance(key, str):
                raise DomainError(f"{label}: JSON object key is not a string")
            require_nfc(key, f"{label}.<key>")
            validate_nfc_tree(item, f"{label}.{key}")


def _no_duplicate_object(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise DomainError(f"duplicate JSON object key: {key!r}")
        result[key] = value
    return result


def decode_json(data: bytes, label: str) -> Any:
    if data.startswith(b"\xef\xbb\xbf"):
        raise DomainError(f"{label}: UTF-8 BOM is prohibited")
    if b"\r" in data:
        raise DomainError(f"{label}: CR/CRLF is prohibited; use LF")
    try:
        text = data.decode("utf-8", "strict")
    except UnicodeDecodeError as exc:
        raise DomainError(f"{label}: invalid UTF-8: {exc}") from exc
    try:
        value = json.loads(text, object_pairs_hook=_no_duplicate_object)
    except (json.JSONDecodeError, DomainError) as exc:
        raise DomainError(f"{label}: invalid JSON: {exc}") from exc
    validate_nfc_tree(value, label)
    return value


def load_json(path: Path) -> Any:
    return decode_json(path.read_bytes(), str(path))


def decode_jsonl_with_lines(
    data: bytes, label: str
) -> list[tuple[int, dict[str, Any]]]:
    if data.startswith(b"\xef\xbb\xbf"):
        raise DomainError(f"{label}: UTF-8 BOM is prohibited")
    if b"\r" in data:
        raise DomainError(f"{label}: CR/CRLF is prohibited; use LF")
    try:
        text = data.decode("utf-8", "strict")
    except UnicodeDecodeError as exc:
        raise DomainError(f"{label}: invalid UTF-8: {exc}") from exc
    records: list[tuple[int, dict[str, Any]]] = []
    for line_number, raw in enumerate(text.split("\n"), 1):
        if not raw.strip():
            continue
        try:
            value = json.loads(raw, object_pairs_hook=_no_duplicate_object)
        except (json.JSONDecodeError, DomainError) as exc:
            raise DomainError(f"{label}:{line_number}: invalid JSON object: {exc}") from exc
        if not isinstance(value, dict):
            raise DomainError(f"{label}:{line_number}: each nonblank line must be one object")
        validate_nfc_tree(value, f"{label}:{line_number}")
        records.append((line_number, value))
    return records


def decode_jsonl(data: bytes, label: str) -> list[dict[str, Any]]:
    return [record for _line_number, record in decode_jsonl_with_lines(data, label)]


def load_jsonl(path: Path) -> list[dict[str, Any]]:
    return decode_jsonl(path.read_bytes(), str(path))


def canonical_json_bytes(value: Any) -> bytes:
    """RFC 8785 serialization for the frozen string/array/object/null profile.

    The evidence envelope deliberately contains no JSON numbers.  Rejecting
    numbers here avoids claiming a general-purpose JCS number implementation.
    Boolean values are also outside the frozen envelope profile.
    """

    def check(item: Any, label: str) -> None:
        if item is None or isinstance(item, str):
            if isinstance(item, str):
                require_nfc(item, label)
            return
        if isinstance(item, bool) or isinstance(item, (int, float)):
            raise DomainError(f"{label}: number/boolean is outside restricted RFC 8785 profile")
        if isinstance(item, list):
            for index, child in enumerate(item):
                check(child, f"{label}[{index}]")
            return
        if isinstance(item, dict):
            for key, child in item.items():
                if not isinstance(key, str):
                    raise DomainError(f"{label}: object key is not a string")
                require_nfc(key, f"{label}.<key>")
                check(child, f"{label}.{key}")
            return
        raise DomainError(f"{label}: unsupported JSON type {type(item).__name__}")

    check(value, "$")
    return json.dumps(
        value,
        ensure_ascii=False,
        sort_keys=True,
        separators=(",", ":"),
        allow_nan=False,
    ).encode("utf-8")


def evidence_set_digest(entries: Sequence[Mapping[str, Any]]) -> tuple[str, bytes]:
    normalized: list[dict[str, Any]] = []
    seen: set[tuple[str, str]] = set()
    required = {
        "analysis_subject_id",
        "anchor",
        "artifact_sha256",
        "evidence_id",
        "repository_path",
    }
    for index, raw in enumerate(entries):
        if set(raw) != required:
            raise DomainError(f"evidence entry {index}: fields must be exactly {sorted(required)}")
        subject = raw["analysis_subject_id"]
        evidence_id = raw["evidence_id"]
        artifact_hash = raw["artifact_sha256"]
        anchor = raw["anchor"]
        path = raw["repository_path"]
        if not isinstance(subject, str) or not SUBJECT_ID_RE.fullmatch(subject):
            raise DomainError(f"evidence entry {index}: invalid analysis_subject_id")
        if not isinstance(evidence_id, str) or not ID_RE.fullmatch(evidence_id):
            raise DomainError(f"evidence entry {index}: invalid evidence_id")
        if not isinstance(artifact_hash, str) or not HEX64_RE.fullmatch(artifact_hash):
            raise DomainError(f"evidence entry {index}: invalid artifact_sha256")
        if anchor is not None:
            if not isinstance(anchor, str):
                raise DomainError(f"evidence entry {index}: invalid anchor")
            validate_anchor(anchor)
        if not isinstance(path, str):
            raise DomainError(f"evidence entry {index}: repository_path is not a string")
        validate_evidence_path(path)
        key = (subject, evidence_id)
        if key in seen:
            raise DomainError(f"duplicate evidence identity: {subject}#{evidence_id}")
        seen.add(key)
        normalized.append(dict(raw))
    normalized.sort(
        key=lambda item: (
            sort_key(item["analysis_subject_id"]),
            sort_key(item["evidence_id"]),
            item["analysis_subject_id"].encode("ascii"),
            item["evidence_id"].encode("ascii"),
        )
    )
    envelope = {
        "canonicalization": EVIDENCE_SET_ALGORITHM,
        "evidence": normalized,
        "hash_algorithm": "SHA-256",
        "unicode_version": UNICODE_VERSION,
    }
    serialized = canonical_json_bytes(envelope)
    return hashlib.sha256(serialized).hexdigest(), serialized


def validate_repository_path(path: str, roots: tuple[str, ...] | None = None) -> None:
    require_nfc(path, "repository path")
    if (
        not path
        or path.startswith("/")
        or "\\" in path
        or "://" in path
        or "#" in path
    ):
        raise DomainError(f"unsafe repository path: {path!r}")
    if any(unicodedata.category(char) == "Cc" for char in path):
        raise DomainError(f"control character in repository path: {path!r}")
    raw_parts = path.split("/")
    if any(part in {"", ".", ".."} for part in raw_parts):
        raise DomainError(f"unsafe repository path: {path!r}")
    parts = PurePosixPath(path).parts
    if any(any(char in '<>:"\\|?*' for char in part) for part in parts):
        raise DomainError(f"Windows-unsafe character in repository path: {path!r}")
    if roots and not path.startswith(roots):
        raise DomainError(f"path is outside governed roots {roots}: {path!r}")


def validate_evidence_path(path: str) -> None:
    validate_repository_path(path, ("series/", "studies/"))


def validate_anchor(anchor: str) -> None:
    require_nfc(anchor, "anchor")
    if (
        not anchor
        or "#" in anchor
        or any(char.isspace() for char in anchor)
        or any(unicodedata.category(char) == "Cc" for char in anchor)
    ):
        raise DomainError("anchor must be nonempty NFC without '#', controls, or whitespace")


def parse_evidence_ref(value: str) -> tuple[str, str]:
    if not isinstance(value, str) or not EVIDENCE_REF_RE.fullmatch(value) or value.count("#") != 1:
        raise DomainError(f"invalid evidence reference: {value!r}")
    return tuple(value.split("#", 1))  # type: ignore[return-value]


def evidence_ref_sort_key(value: str) -> tuple[Any, ...]:
    subject, evidence_id = parse_evidence_ref(value)
    return (sort_key(subject), sort_key(evidence_id), value.encode("ascii"))


def run_git(root: Path, *args: str, input_bytes: bytes | None = None) -> bytes:
    try:
        return subprocess.check_output(
            ["git", "-C", str(root), *args],
            input=input_bytes,
            stderr=subprocess.PIPE,
        )
    except subprocess.CalledProcessError as exc:
        detail = exc.stderr.decode("utf-8", "replace").strip()
        raise DomainError(f"git {' '.join(args)} failed: {detail}") from exc


@dataclass(frozen=True)
class SnapshotEntry:
    path: str
    mode: str
    data: bytes
    tracked: bool = True

    @property
    def qualifies_as_evidence(self) -> bool:
        return (
            self.tracked
            and self.mode == "100644"
            and not self.data.startswith(LFS_PREFIXES)
        )


class GitSnapshot:
    """Exact entries from a commit/index, or a directly enumerated worktree view."""

    def __init__(self, root: Path, identity: str, entries: Mapping[str, SnapshotEntry]):
        self.root = root
        self.identity = identity
        self.entries = dict(entries)

    @classmethod
    def from_commit(cls, root: Path, commit: str) -> "GitSnapshot":
        if not FULL_COMMIT_RE.fullmatch(commit):
            raise DomainError("basis commit must be a full lower-case 40- or 64-hex object ID")
        object_format = run_git(root, "rev-parse", "--show-object-format").decode().strip()
        expected_length = 40 if object_format == "sha1" else 64 if object_format == "sha256" else 0
        if len(commit) != expected_length:
            raise DomainError(f"basis commit length does not match repository object format {object_format}")
        if run_git(root, "cat-file", "-t", commit).decode().strip() != "commit":
            raise DomainError("basis object is not a commit")
        raw = run_git(root, "ls-tree", "-r", "-z", "--full-tree", commit)
        entries: dict[str, SnapshotEntry] = {}
        for item in raw.split(b"\0"):
            if not item:
                continue
            metadata, raw_path = item.split(b"\t", 1)
            mode, kind, _oid = metadata.decode("ascii").split(" ")
            path = raw_path.decode("utf-8", "strict")
            if kind == "blob":
                data = run_git(root, "show", f"{commit}:{path}")
                entries[path] = SnapshotEntry(path, mode, data)
            else:
                entries[path] = SnapshotEntry(path, mode, b"")
        return cls(root, commit, entries)

    @classmethod
    def from_index(cls, root: Path) -> "GitSnapshot":
        raw = run_git(root, "ls-files", "--stage", "-z")
        entries: dict[str, SnapshotEntry] = {}
        for item in raw.split(b"\0"):
            if not item:
                continue
            metadata, raw_path = item.split(b"\t", 1)
            mode, _oid, stage = metadata.decode("ascii").split(" ")
            path = raw_path.decode("utf-8", "strict")
            if stage != "0":
                raise DomainError(f"unmerged index entry: {path}")
            data = run_git(root, "show", f":{path}") if mode in {"100644", "100755", "120000"} else b""
            entries[path] = SnapshotEntry(path, mode, data)
        return cls(root, "INDEX", entries)

    @classmethod
    def from_worktree(cls, root: Path) -> "GitSnapshot":
        """Read the prospective Git worktree without a redundant path manifest."""

        paths = {
            item.decode("utf-8", "strict")
            for item in run_git(
                root,
                "ls-files",
                "--cached",
                "--others",
                "--exclude-standard",
                "-z",
            ).split(b"\0")
            if item
        }
        index_modes: dict[str, str] = {}
        for item in run_git(root, "ls-files", "--stage", "-z").split(b"\0"):
            if not item:
                continue
            metadata, raw_path = item.split(b"\t", 1)
            mode, _oid, stage = metadata.decode("ascii").split(" ")
            path = raw_path.decode("utf-8", "strict")
            if stage != "0":
                raise DomainError(f"unmerged index entry: {path}")
            index_modes[path] = mode
        entries: dict[str, SnapshotEntry] = {}
        for path in sorted(paths):
            validate_repository_path(path)
            full = root.joinpath(*PurePosixPath(path).parts)
            if not full.exists() and not full.is_symlink():
                continue
            if full.is_symlink():
                entries[path] = SnapshotEntry(
                    path,
                    "120000",
                    os.readlink(full).encode("utf-8"),
                    path in index_modes,
                )
            elif full.is_file():
                entries[path] = SnapshotEntry(
                    path,
                    index_modes.get(path, "100644"),
                    full.read_bytes(),
                    path in index_modes,
                )
            else:
                entries[path] = SnapshotEntry(path, "040000", b"", path in index_modes)
        return cls(root, "PROSPECTIVE_WORKTREE", entries)

    def get(self, path: str) -> SnapshotEntry | None:
        return self.entries.get(path)

    def artifact_sha256(self, path: str) -> str:
        entry = self.get(path)
        if entry is None:
            raise DomainError(f"missing exact-case Git path: {path}")
        if not entry.qualifies_as_evidence:
            raise DomainError(f"evidence is not a regular non-LFS blob: {path} ({entry.mode})")
        return hashlib.sha256(entry.data).hexdigest()


@dataclass(frozen=True)
class AuthorityMetadata:
    status: str
    supersedes: tuple[str, ...]
    superseded_by: tuple[str, ...]
    do_not_use: bool


def _restricted_yaml_load(text: str, label: str) -> Any:
    try:
        import yaml
    except ImportError as exc:
        raise DomainError("PyYAML is required for authority front matter") from exc

    class Loader(yaml.SafeLoader):
        pass

    def mapping(loader: Any, node: Any, deep: bool = False) -> dict[Any, Any]:
        result: dict[Any, Any] = {}
        for key_node, value_node in node.value:
            key = loader.construct_object(key_node, deep=deep)
            if not isinstance(key, str):
                raise DomainError(f"{label}: YAML mapping keys must be strings")
            if key == "<<":
                raise DomainError(f"{label}: YAML merge keys are prohibited")
            if key in result:
                raise DomainError(f"{label}: duplicate YAML key {key!r}")
            result[key] = loader.construct_object(value_node, deep=deep)
        return result

    Loader.add_constructor(
        yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG,
        mapping,
    )
    try:
        events = list(yaml.parse(text, Loader=Loader))
        for event in events:
            if isinstance(event, yaml.events.AliasEvent) or getattr(event, "anchor", None):
                raise DomainError(f"{label}: YAML aliases and anchors are prohibited")
            if getattr(event, "tag", None) is not None:
                raise DomainError(f"{label}: explicit YAML tags are prohibited")
        documents = list(yaml.load_all(text, Loader=Loader))
    except DomainError:
        raise
    except (TypeError, ValueError, yaml.YAMLError) as exc:
        raise DomainError(f"{label}: invalid restricted YAML: {exc}") from exc
    if len(documents) != 1:
        raise DomainError(f"{label}: exactly one YAML document is required")
    return documents[0]


def parse_authority_front_matter(data: bytes, path: str) -> AuthorityMetadata | None:
    if not data.startswith(b"---\n"):
        return None
    if b"\r" in data:
        raise DomainError(f"{path}: recognized authority artifact must be LF-only")
    try:
        text = data.decode("utf-8", "strict")
    except UnicodeDecodeError as exc:
        raise DomainError(f"{path}: invalid UTF-8 front matter") from exc
    lines = text.split("\n")
    closing = next((index for index in range(1, len(lines)) if lines[index] == "---"), None)
    if closing is None:
        raise DomainError(f"{path}: unterminated YAML front matter")
    if closing == len(lines) - 1:
        raise DomainError(f"{path}: YAML front-matter closing fence must be LF-terminated")
    front_lines = lines[1:closing]
    front = "\n".join(front_lines) + "\n"
    loaded = _restricted_yaml_load(front, path)
    if not isinstance(loaded, dict):
        raise DomainError(f"{path}: front matter must be one mapping")
    present = AUTHORITY_KEYS.intersection(loaded)
    if not present:
        return None
    if present != AUTHORITY_KEYS:
        # Legacy documents frequently use a generic ``status`` field (and, in
        # a few cases, other similarly named fields) for workflow state rather
        # than repository authority.  A partial quartet is therefore not
        # recognized machine-readable authority.  Failing closed here means
        # the artifact remains legacy/non-current evidence unless and until a
        # complete quartet is supplied; it is never promoted by inference.
        return None
    status = loaded["status"]
    supersedes = loaded["supersedes"]
    superseded_by = loaded["superseded_by"]
    veto = loaded["do_not_use_as_current_authority"]
    if not isinstance(status, str):
        raise DomainError(f"{path}: authority status must be a string")
    if status not in AUTHORITY_STATUSES:
        raise DomainError(
            f"{path}: invalid authority status; "
            f"expected one of {sorted(AUTHORITY_STATUSES)}"
        )
    if type(veto) is not bool:
        raise DomainError(f"{path}: authority veto must be a real boolean")
    bool_lines = [line for line in front_lines if line.startswith("do_not_use_as_current_authority:")]
    if len(bool_lines) != 1 or not re.fullmatch(
        r"do_not_use_as_current_authority: (?:true|false)", bool_lines[0]
    ):
        raise DomainError(f"{path}: authority boolean must use exact true/false spelling")
    for field, values in (("supersedes", supersedes), ("superseded_by", superseded_by)):
        if not isinstance(values, list) or any(not isinstance(item, str) for item in values):
            raise DomainError(f"{path}: {field} must be an array of strings")
        if len(values) != len(set(values)):
            raise DomainError(f"{path}: {field} contains duplicates")
        for target in values:
            validate_evidence_path(target)
    if status in {"canonical", "active_provisional"}:
        if veto or superseded_by:
            raise DomainError(f"{path}: current status contradicts veto/superseded_by")
    elif status == "superseded":
        if not veto or not superseded_by:
            raise DomainError(f"{path}: superseded requires veto=true and nonempty superseded_by")
    elif status == "historical_legacy" and not veto:
        raise DomainError(f"{path}: historical_legacy requires veto=true")
    elif status == "draft_noncurrent":
        if not veto or supersedes or superseded_by:
            raise DomainError(
                f"{path}: draft_noncurrent requires veto=true and empty supersession arrays"
            )
    return AuthorityMetadata(status, tuple(supersedes), tuple(superseded_by), veto)


class AuthorityGraph:
    def __init__(self, snapshot: GitSnapshot):
        self.snapshot = snapshot
        self.metadata: dict[str, AuthorityMetadata | None] = {}
        self.edges: set[tuple[str, str]] = set()
        self.errors: list[str] = []
        self.invalid_paths: set[str] = set()
        self._build()

    def _error(self, message: str, *paths: str) -> None:
        self.errors.append(message)
        self.invalid_paths.update(paths)

    def _build(self) -> None:
        markdown = sorted(
            path
            for path, entry in self.snapshot.entries.items()
            if path.startswith(("series/", "studies/"))
            and path.endswith(".md")
            and entry.mode == "100644"
            and entry.tracked
        )
        for path in markdown:
            try:
                self.metadata[path] = parse_authority_front_matter(
                    self.snapshot.entries[path].data, path
                )
            except DomainError as exc:
                self.metadata[path] = None
                self._error(str(exc), path)
        for path, meta in self.metadata.items():
            if meta is None:
                continue
            for predecessor in meta.supersedes:
                self.edges.add((predecessor, path))
            for successor in meta.superseded_by:
                self.edges.add((path, successor))
        for predecessor, successor in sorted(self.edges):
            if predecessor == successor:
                self._error(f"self supersession edge: {predecessor}", predecessor)
                continue
            pred_entry = self.snapshot.get(predecessor)
            succ_entry = self.snapshot.get(successor)
            if pred_entry is None or pred_entry.mode != "100644" or not predecessor.endswith(".md"):
                self._error(f"dangling predecessor path: {predecessor}", predecessor, successor)
                continue
            if succ_entry is None or succ_entry.mode != "100644" or not successor.endswith(".md"):
                self._error(f"dangling successor path: {successor}", predecessor, successor)
                continue
            pred_meta = self.metadata.get(predecessor)
            succ_meta = self.metadata.get(successor)
            reciprocal = (
                pred_meta is not None
                and succ_meta is not None
                and successor in pred_meta.superseded_by
                and predecessor in succ_meta.supersedes
            )
            if not reciprocal:
                self._error(
                    f"nonreciprocal supersession edge: {predecessor} -> {successor}",
                    predecessor,
                    successor,
                )
        outgoing: dict[str, set[str]] = defaultdict(set)
        undirected: dict[str, set[str]] = defaultdict(set)
        for predecessor, successor in self.edges:
            outgoing[predecessor].add(successor)
            undirected[predecessor].add(successor)
            undirected[successor].add(predecessor)
        for path, meta in self.metadata.items():
            if meta and meta.status in {"canonical", "active_provisional"} and outgoing[path]:
                self._error(f"current authority has outgoing successor edge: {path}", path)
        visiting: set[str] = set()
        visited: set[str] = set()

        def visit(node: str) -> None:
            if node in visiting:
                self._error(f"supersession cycle includes {node}", node)
                return
            if node in visited:
                return
            visiting.add(node)
            for child in outgoing[node]:
                visit(child)
            visiting.remove(node)
            visited.add(node)

        for node in sorted(set(self.metadata) | set(outgoing)):
            visit(node)
        seen: set[str] = set()
        for seed in sorted(undirected):
            if seed in seen:
                continue
            component: set[str] = set()
            queue = deque([seed])
            while queue:
                node = queue.popleft()
                if node in component:
                    continue
                component.add(node)
                queue.extend(undirected[node])
            seen.update(component)
            contains_chain = any(
                self.metadata.get(node) is not None
                and self.metadata[node].status == "superseded"  # type: ignore[union-attr]
                for node in component
            )
            if contains_chain:
                sinks = [
                    node
                    for node in component
                    if self.metadata.get(node) is not None
                    and self.metadata[node].status in {"canonical", "active_provisional"}  # type: ignore[union-attr]
                    and not outgoing[node]
                ]
                if len(sinks) != 1:
                    self._error(
                        f"supersession component requires exactly one current sink; "
                        f"component={sorted(component)}, sinks={sorted(sinks)}",
                        *component,
                    )

    def classification(self, path: str) -> str:
        entry = self.snapshot.get(path)
        if entry is None or not entry.qualifies_as_evidence:
            return "MISSING"
        if path in self.invalid_paths:
            return "INVALID"
        meta = self.metadata.get(path)
        if meta is None:
            return "UNCLASSIFIED_LEGACY"
        outgoing = any(predecessor == path for predecessor, _ in self.edges)
        if meta.status == "canonical" and not outgoing:
            return "CANONICAL_CURRENT"
        if meta.status == "active_provisional" and not outgoing:
            return "ACTIVE_PROVISIONAL_CURRENT"
        if meta.status == "superseded":
            return "SUPERSEDED"
        if meta.status == "historical_legacy":
            return "HISTORICAL_LEGACY"
        if meta.status == "draft_noncurrent":
            return "DRAFT_NONCURRENT"
        return "INVALID"

    def current_eligible(self, path: str) -> bool:
        return self.classification(path) in {
            "CANONICAL_CURRENT",
            "ACTIVE_PROVISIONAL_CURRENT",
        }


def _alias_canonical(alias: Mapping[str, Any]) -> bytes:
    return json.dumps(
        dict(alias), ensure_ascii=False, sort_keys=True, separators=(",", ":")
    ).encode("utf-8")


def alias_sort_key(alias: Mapping[str, Any]) -> tuple[Any, ...]:
    return (
        str(alias.get("language", "")).encode("ascii", "strict"),
        str(alias.get("kind", "")).encode("ascii", "strict"),
        sort_key(str(alias.get("value", ""))),
        str(alias.get("value", "")).encode("utf-8"),
        _alias_canonical(alias),
    )


def _validate_aliases(record: Mapping[str, Any], label: str, errors: list[str]) -> None:
    scope_keys: dict[str, set[tuple[str, str, str]]] = {}
    for field in ("entity_aliases", "subject_aliases"):
        aliases = record.get(field, [])
        keys: set[tuple[str, str, str]] = set()
        for index, alias in enumerate(aliases):
            value = alias.get("value") if isinstance(alias, dict) else None
            language = alias.get("language") if isinstance(alias, dict) else None
            kind = alias.get("kind") if isinstance(alias, dict) else None
            note = alias.get("note") if isinstance(alias, dict) else None
            if not all(isinstance(item, str) for item in (value, language, kind)):
                errors.append(f"{label}.{field}[{index}]: malformed alias")
                continue
            try:
                require_nfc(value, f"{label}.{field}[{index}].value")
                if value != value.strip() or any(unicodedata.category(ch) == "Cc" for ch in value):
                    raise DomainError("alias has boundary whitespace or control characters")
                if language != language.lower() or not re.fullmatch(
                    r"[a-z]{2,8}(?:-[a-z0-9]{1,8})*", language
                ):
                    raise DomainError("language tag is not lower-case ASCII BCP47 form")
                if note is not None:
                    if not isinstance(note, str):
                        raise DomainError("alias note is not a string or null")
                    require_nfc(note, f"{label}.{field}[{index}].note")
                    if note != note.strip() or any(
                        unicodedata.category(char) == "Cc" for char in note
                    ):
                        raise DomainError(
                            "alias note has boundary whitespace or control characters"
                        )
                key = (fold(value), language, kind)
            except DomainError as exc:
                errors.append(f"{label}.{field}[{index}]: {exc}")
                continue
            if key in keys:
                errors.append(f"{label}.{field}: normalized duplicate alias {value!r}")
            keys.add(key)
        scope_keys[field] = keys
    overlap = scope_keys.get("entity_aliases", set()) & scope_keys.get("subject_aliases", set())
    if overlap:
        errors.append(f"{label}: normalized alias keys overlap entity and subject scopes")


def _series_ids(series_registry: Mapping[str, Any]) -> set[str]:
    raw = series_registry.get("series", [])
    if not isinstance(raw, list):
        return set()
    result: set[str] = set()
    for item in raw:
        if isinstance(item, dict) and isinstance(item.get("series_id"), str):
            result.add(item["series_id"])
    return result


def validate_discovery_records(
    records: Sequence[Mapping[str, Any]],
    series_registry: Mapping[str, Any],
    *,
    snapshot: GitSnapshot | None = None,
    authority: AuthorityGraph | None = None,
) -> list[str]:
    errors: list[str] = []
    by_subject: dict[str, Mapping[str, Any]] = {}
    entity_fingerprints: dict[str, tuple[Any, ...]] = {}
    known_series = _series_ids(series_registry)
    for index, record in enumerate(records):
        label = f"record[{index}]"
        subject_id = record.get("analysis_subject_id")
        entity_id = record.get("character_entity_id")
        if isinstance(subject_id, str):
            if subject_id in by_subject:
                errors.append(f"{label}: duplicate analysis_subject_id {subject_id}")
            by_subject[subject_id] = record
        if not isinstance(subject_id, str) or not SUBJECT_ID_RE.fullmatch(subject_id):
            errors.append(f"{label}: invalid analysis_subject_id")
        if not isinstance(entity_id, str) or not ENTITY_ID_RE.fullmatch(entity_id):
            errors.append(f"{label}: invalid character_entity_id")
        elif isinstance(subject_id, str) and subject_id.split("@", 1)[0] != entity_id:
            errors.append(f"{label}: subject ID entity prefix differs from character_entity_id")
        series_id = record.get("series_id")
        franchise_id = record.get("franchise_id")
        namespace = franchise_id if franchise_id is not None else series_id
        if isinstance(entity_id, str) and isinstance(namespace, str):
            if entity_id.split(":", 1)[0] != namespace:
                errors.append(f"{label}: ID namespace must equal franchise_id or series_id")
        if isinstance(series_id, str) and series_id not in known_series:
            errors.append(f"{label}: unresolved series_id {series_id!r}")
        _validate_aliases(record, label, errors)
        if isinstance(entity_id, str):
            aliases = record.get("entity_aliases", [])
            try:
                canonical_aliases = tuple(
                    _alias_canonical(alias) for alias in sorted(aliases, key=alias_sort_key)
                )
            except (DomainError, TypeError, UnicodeError) as exc:
                errors.append(f"{label}: cannot canonicalize entity aliases: {exc}")
                canonical_aliases = ()
            fingerprint = (record.get("preferred_name"), franchise_id, canonical_aliases)
            previous = entity_fingerprints.get(entity_id)
            if previous is not None and previous != fingerprint:
                errors.append(f"{label}: entity-level drift for {entity_id}")
            entity_fingerprints[entity_id] = fingerprint
        dimensions = record.get("analytical_dimensions", [])
        if not isinstance(dimensions, list) or not dimensions or set(dimensions) - ANALYTICAL_DIMENSIONS:
            errors.append(f"{label}: invalid analytical_dimensions")
        evidence = record.get("evidence", [])
        evidence_by_id: dict[str, Mapping[str, Any]] = {}
        present: list[bool] = []
        for evidence_index, item in enumerate(evidence if isinstance(evidence, list) else []):
            item_label = f"{label}.evidence[{evidence_index}]"
            if not isinstance(item, dict):
                errors.append(f"{item_label}: evidence is not an object")
                continue
            evidence_id = item.get("evidence_id")
            if not isinstance(evidence_id, str) or not ID_RE.fullmatch(evidence_id):
                errors.append(f"{item_label}: invalid evidence_id")
            elif evidence_id in evidence_by_id:
                errors.append(f"{item_label}: duplicate evidence_id {evidence_id}")
            else:
                evidence_by_id[evidence_id] = item
            path = item.get("repository_path")
            try:
                if not isinstance(path, str):
                    raise DomainError("repository_path is not a string")
                validate_evidence_path(path)
            except DomainError as exc:
                errors.append(f"{item_label}: {exc}")
                path = None
            item_dimensions = item.get("dimensions", [])
            if isinstance(item_dimensions, list) and isinstance(dimensions, list):
                if not set(item_dimensions).issubset(set(dimensions)):
                    errors.append(f"{item_label}: evidence dimensions exceed record dimensions")
            anchor = item.get("anchor")
            if anchor is not None:
                try:
                    if not isinstance(anchor, str):
                        raise DomainError("anchor is not a string")
                    validate_anchor(anchor)
                except DomainError as exc:
                    errors.append(f"{item_label}: {exc}")
            if snapshot is not None and path is not None:
                entry = snapshot.get(path)
                qualifies = entry is not None and entry.qualifies_as_evidence
                present.append(qualifies)
        if snapshot is not None:
            if not present or not any(present):
                derived = "NOT_PRESENT"
            elif not all(present):
                errors.append(f"{label}: mixed present/absent evidence is migration-ledger-only")
                derived = None
            else:
                review_states = {item.get("review_state") for item in evidence}
                if not review_states.issubset({"UNREVIEWED", "REVIEWED"}):
                    errors.append(f"{label}: unknown evidence review_state")
                    derived = None
                elif "UNREVIEWED" in review_states:
                    derived = "PRESENT_UNREVIEWED"
                else:
                    derived = "PRESENT_REVIEWED"
            if derived is not None and record.get("materialization_status") != derived:
                errors.append(
                    f"{label}: materialization_status {record.get('materialization_status')!r} "
                    f"does not match derived {derived}"
                )
        coverage_ids: set[str] = set()
        for coverage_index, coverage in enumerate(record.get("analytical_coverage", [])):
            coverage_label = f"{label}.analytical_coverage[{coverage_index}]"
            coverage_id = coverage.get("coverage_id") if isinstance(coverage, dict) else None
            if not isinstance(coverage_id, str) or not ID_RE.fullmatch(coverage_id):
                errors.append(f"{coverage_label}: invalid coverage_id")
                continue
            if coverage_id in coverage_ids:
                errors.append(f"{coverage_label}: duplicate coverage_id")
            coverage_ids.add(coverage_id)
            evidence_ids = coverage.get("evidence_ids", [])
            if any(item not in evidence_by_id for item in evidence_ids):
                errors.append(f"{coverage_label}: unresolved evidence_ids")
            if record.get("curation_status") == "INCLUDED" and any(
                evidence_by_id[item].get("review_state") != "REVIEWED"
                for item in evidence_ids
                if item in evidence_by_id
            ):
                errors.append(f"{coverage_label}: included coverage references unreviewed evidence")
            if coverage.get("scope_type") == "RANGE" and coverage.get("unit") in {
                "EPISODE",
                "CHAPTER",
                "VOLUME",
                "STORY_CHAPTER",
            }:
                start = coverage.get("start")
                through = coverage.get("through")
                numeric_locator = re.compile(r"^[0-9]+(?:\.[0-9]+)*$")
                if (
                    isinstance(start, str)
                    and isinstance(through, str)
                    and numeric_locator.fullmatch(start)
                    and numeric_locator.fullmatch(through)
                ):
                    start_key = tuple(int(part) for part in start.split("."))
                    through_key = tuple(int(part) for part in through.split("."))
                    if start_key > through_key:
                        errors.append(f"{coverage_label}: ordered range start exceeds through")
            if record.get("subject_kind") != "COMPOSITE_MODEL":
                if "component_subject_id" in coverage:
                    errors.append(f"{coverage_label}: component_subject_id is composite-only")
                if coverage.get("continuity_id") != record.get("continuity_id"):
                    errors.append(f"{coverage_label}: continuity differs from subject continuity")
        if record.get("curation_status") == "INCLUDED":
            if record.get("materialization_status") != "PRESENT_REVIEWED":
                errors.append(f"{label}: INCLUDED requires PRESENT_REVIEWED")
            if record.get("inclusion_basis") not in {"DEDICATED", "DISTRIBUTED_SUBSTANTIAL"}:
                errors.append(f"{label}: INCLUDED requires a qualifying inclusion_basis")
            if not evidence:
                errors.append(f"{label}: INCLUDED requires evidence")
            supported = {
                dimension
                for item in evidence
                if item.get("review_state") == "REVIEWED"
                for dimension in item.get("dimensions", [])
            }
            if isinstance(dimensions, list) and not set(dimensions).issubset(supported):
                errors.append(f"{label}: included dimensions lack reviewed evidence support")
            for item in evidence:
                if item.get("review_state") != "REVIEWED":
                    errors.append(f"{label}: INCLUDED contains unreviewed evidence")
                if authority is not None and not authority.current_eligible(item.get("repository_path", "")):
                    errors.append(
                        f"{label}: INCLUDED evidence is not current eligible: "
                        f"{item.get('repository_path')}"
                    )
        # Provisional display state is derived again by the generator from the
        # authority graph; it is intentionally never stored in the registry.

    leaf_cache: dict[str, set[str]] = {}
    stack: list[str] = []

    def leaves(subject_id: str) -> set[str]:
        if subject_id in leaf_cache:
            return leaf_cache[subject_id]
        if subject_id in stack:
            errors.append(f"composite dependency cycle: {' -> '.join(stack + [subject_id])}")
            return set()
        record = by_subject.get(subject_id)
        if record is None:
            errors.append(f"unresolved component subject: {subject_id}")
            return set()
        if record.get("subject_kind") != "COMPOSITE_MODEL":
            return {subject_id}
        stack.append(subject_id)
        combined: set[str] = set()
        branches: list[set[str]] = []
        for component in record.get("component_subject_ids", []):
            branch = leaves(component)
            if combined & branch:
                errors.append(f"{subject_id}: transitive component leaf occurs in multiple branches")
            combined.update(branch)
            branches.append(branch)
        stack.pop()
        if len(combined) < 2:
            errors.append(f"{subject_id}: composite must expand to at least two distinct leaves")
        leaf_cache[subject_id] = combined
        return combined

    for subject_id, record in by_subject.items():
        if record.get("subject_kind") != "COMPOSITE_MODEL":
            continue
        components = record.get("component_subject_ids", [])
        if len(components) != len(set(components)):
            errors.append(f"{subject_id}: duplicate component_subject_ids")
        for component_id in components:
            component = by_subject.get(component_id)
            if component_id == subject_id:
                errors.append(f"{subject_id}: composite may not reference itself")
            if component is not None:
                if component.get("character_entity_id") != record.get("character_entity_id"):
                    errors.append(f"{subject_id}: direct component entity mismatch at {component_id}")
                if component.get("series_id") != record.get("series_id"):
                    errors.append(f"{subject_id}: direct cross-series component is prohibited at {component_id}")
        leaf_ids = leaves(subject_id)
        continuities: set[str] = set()
        for leaf_id in leaf_ids:
            leaf = by_subject.get(leaf_id)
            if leaf is None:
                continue
            if leaf.get("character_entity_id") != record.get("character_entity_id"):
                errors.append(f"{subject_id}: component entity mismatch at {leaf_id}")
            if leaf.get("series_id") != record.get("series_id"):
                errors.append(f"{subject_id}: cross-series composite is prohibited at {leaf_id}")
            continuity = leaf.get("continuity_id")
            if isinstance(continuity, str):
                continuities.add(continuity)
        if not continuities:
            errors.append(f"{subject_id}: effective continuity scope is empty")
        for coverage in record.get("analytical_coverage", []):
            component = coverage.get("component_subject_id")
            if component not in leaf_ids:
                errors.append(f"{subject_id}: composite coverage must name a transitive leaf")
            elif coverage.get("continuity_id") != by_subject[component].get("continuity_id"):
                errors.append(f"{subject_id}: composite coverage continuity differs from leaf")
    return sorted(set(errors), key=lambda item: item.encode("utf-8"))


def resolve_evidence_entries(
    evidence_refs: Sequence[str],
    records: Sequence[Mapping[str, Any]],
    snapshot: GitSnapshot,
) -> list[dict[str, Any]]:
    by_subject: dict[str, Mapping[str, Any]] = {}
    for record_index, record in enumerate(records):
        subject_id = record.get("analysis_subject_id")
        if not isinstance(subject_id, str):
            raise DomainError(f"discovery record {record_index} has no valid analysis_subject_id")
        if subject_id in by_subject:
            raise DomainError(f"duplicate discovery analysis_subject_id: {subject_id}")
        seen_evidence: set[str] = set()
        evidence_items = record.get("evidence", [])
        if not isinstance(evidence_items, list):
            raise DomainError(f"{subject_id}: evidence is not an array")
        for evidence_index, item in enumerate(evidence_items):
            if not isinstance(item, Mapping):
                raise DomainError(f"{subject_id}: evidence[{evidence_index}] is not an object")
            evidence_id = item.get("evidence_id")
            if not isinstance(evidence_id, str):
                raise DomainError(f"{subject_id}: evidence[{evidence_index}] has no valid evidence_id")
            if evidence_id in seen_evidence:
                raise DomainError(f"{subject_id}: duplicate evidence_id: {evidence_id}")
            seen_evidence.add(evidence_id)
        by_subject[subject_id] = record
    if len(evidence_refs) != len(set(evidence_refs)):
        raise DomainError("duplicate top-level evidence_refs")
    if list(evidence_refs) != sorted(evidence_refs, key=evidence_ref_sort_key):
        raise DomainError("top-level evidence_refs are not in canonical order")
    entries: list[dict[str, Any]] = []
    for reference in evidence_refs:
        subject_id, evidence_id = parse_evidence_ref(reference)
        record = by_subject.get(subject_id)
        if record is None:
            raise DomainError(f"unresolved evidence subject: {subject_id}")
        evidence_by_id = {item["evidence_id"]: item for item in record.get("evidence", [])}
        evidence = evidence_by_id.get(evidence_id)
        if evidence is None:
            raise DomainError(f"unresolved evidence reference: {reference}")
        if evidence.get("review_state") != "REVIEWED":
            raise DomainError(f"evidence reference is not reviewed: {reference}")
        path = evidence["repository_path"]
        entries.append(
            {
                "analysis_subject_id": subject_id,
                "anchor": evidence.get("anchor"),
                "artifact_sha256": snapshot.artifact_sha256(path),
                "evidence_id": evidence_id,
                "repository_path": path,
            }
        )
    return entries


def validate_reconstruction_assessments(
    assessments: Sequence[Mapping[str, Any]],
    records: Sequence[Mapping[str, Any]],
    repository: Path,
    *,
    comparison_commit: str | None = None,
) -> list[str]:
    """Validate cross-file reconstruction semantics not expressible in JSON Schema."""

    errors: list[str] = []
    by_subject: dict[str, Mapping[str, Any]] = {}
    for record_index, record in enumerate(records):
        subject_id = record.get("analysis_subject_id")
        if not isinstance(subject_id, str):
            errors.append(f"comparison discovery record[{record_index}] has no valid analysis_subject_id")
            continue
        if subject_id in by_subject:
            errors.append(f"duplicate comparison discovery analysis_subject_id: {subject_id}")
        by_subject[subject_id] = record
    by_assessment: dict[str, Mapping[str, Any]] = {}
    snapshot_cache: dict[str, GitSnapshot] = {}

    def snapshot(commit: str) -> GitSnapshot:
        if commit not in snapshot_cache:
            snapshot_cache[commit] = GitSnapshot.from_commit(repository, commit)
        return snapshot_cache[commit]

    def snapshot_records(selected: GitSnapshot) -> list[dict[str, Any]]:
        required = {
            "registry": "characters/registry.jsonl",
            "schema": "governance/schemas/character-analysis-index.schema.json",
            "series": "series/registry.json",
        }
        entries = {name: selected.get(path) for name, path in required.items()}
        invalid = [
            path
            for name, path in required.items()
            if entries[name] is None
            or entries[name].mode != "100644"
            or not entries[name].tracked
        ]
        if invalid:
            raise DomainError(
                f"{selected.identity}: basis discovery inputs are unavailable as regular tracked blobs: {invalid}"
            )
        records_with_lines = decode_jsonl_with_lines(
            entries["registry"].data,  # type: ignore[union-attr]
            f"{selected.identity}:characters/registry.jsonl",
        )
        records_at_snapshot = [record for _line_number, record in records_with_lines]
        schema = decode_json(
            entries["schema"].data,  # type: ignore[union-attr]
            f"{selected.identity}:character-analysis-index.schema.json",
        )
        series_registry = decode_json(
            entries["series"].data,  # type: ignore[union-attr]
            f"{selected.identity}:series/registry.json",
        )
        if not isinstance(schema, dict) or not isinstance(series_registry, dict):
            raise DomainError(f"{selected.identity}: invalid basis discovery schema/series registry")
        validate_schema_document(schema, f"{selected.identity}: discovery schema")
        diagnostics: list[SchemaDiagnostic] = []
        for line_number, record_at_snapshot in records_with_lines:
            diagnostics.extend(
                schema_diagnostics(
                    record_at_snapshot,
                    schema,
                    "characters/registry.jsonl",
                    line_number=line_number,
                )
            )
        failures = render_schema_diagnostics(diagnostics)
        if failures:
            raise DomainError(
                f"{selected.identity}: invalid basis discovery registry schema: "
                + " | ".join(failures)
            )
        basis_authority = AuthorityGraph(selected)
        failures.extend(basis_authority.errors)
        failures.extend(
            validate_discovery_records(
                records_at_snapshot,
                series_registry,
                snapshot=selected,
                authority=basis_authority,
            )
        )
        if failures:
            raise DomainError(
                f"{selected.identity}: invalid basis discovery registry: "
                + " | ".join(sorted(set(failures), key=lambda item: item.encode("utf-8")))
            )
        return records_at_snapshot

    for index, assessment in enumerate(assessments):
        label = f"assessment[{index}]"
        assessment_id = assessment.get("assessment_id")
        if isinstance(assessment_id, str):
            if assessment_id in by_assessment:
                errors.append(f"{label}: duplicate assessment_id {assessment_id}")
            by_assessment[assessment_id] = assessment
        subject_id = assessment.get("analysis_subject_id")
        status = assessment.get("assessment_status")
        record = by_subject.get(subject_id) if isinstance(subject_id, str) else None
        if status not in {"STALE", "SUPERSEDED"}:
            if record is None:
                errors.append(f"{label}: unresolved current analysis_subject_id {subject_id!r}")
                continue
            if assessment.get("character_entity_id") != record.get("character_entity_id"):
                errors.append(f"{label}: character_entity_id differs from discovery record")
        scope = assessment.get("assessment_scope", {})
        if not isinstance(scope, dict):
            errors.append(f"{label}: assessment_scope is not an object")
            continue
        if status not in {"STALE", "SUPERSEDED"}:
            for field in ("continuity_id", "incarnation_id", "state_id"):
                if scope.get(field) != record.get(field):
                    errors.append(f"{label}: assessment_scope.{field} differs from discovery record")
            if record.get("subject_kind") == "COMPOSITE_MODEL":
                if sorted(scope.get("component_subject_ids", [])) != sorted(
                    record.get("component_subject_ids", [])
                ):
                    errors.append(
                        f"{label}: composite assessment component_subject_ids must exactly equal "
                        "the canonical component set"
                    )
            elif "component_subject_ids" in scope:
                errors.append(f"{label}: non-composite assessment stores component_subject_ids")

        claimed: set[str] = set()
        dimensions = assessment.get("dimensions", [])
        dimension_names = [
            item.get("dimension") for item in dimensions if isinstance(item, dict)
        ] if isinstance(dimensions, list) else []
        if Counter(dimension_names) != Counter({item: 1 for item in RECONSTRUCTION_DIMENSIONS}):
            errors.append(f"{label}: dimensions must contain every controlled dimension exactly once")
        scenarios = assessment.get("scenario_readiness", [])
        scenario_names = [
            item.get("scenario") for item in scenarios if isinstance(item, dict)
        ] if isinstance(scenarios, list) else []
        if Counter(scenario_names) != Counter({item: 1 for item in SCENARIO_CATEGORIES}):
            errors.append(f"{label}: scenario_readiness must contain every category exactly once")
        for field in ("dimensions", "scenario_readiness"):
            values = assessment.get(field, [])
            if isinstance(values, list):
                for claim in values:
                    if isinstance(claim, dict):
                        for reference in claim.get("evidence_refs", []):
                            if isinstance(reference, str):
                                claimed.add(reference)
        limits = assessment.get("known_limits", [])
        if isinstance(limits, list):
            limit_ids = [
                item.get("limit_id") for item in limits if isinstance(item, dict)
            ]
            if len(limit_ids) != len(set(limit_ids)):
                errors.append(f"{label}: duplicate known-limit limit_id")
            for limit in limits:
                if not isinstance(limit, dict):
                    continue
                references = limit.get("evidence_refs", [])
                if limit.get("support_kind") == "EVIDENCE_GAP" and references:
                    errors.append(f"{label}: EVIDENCE_GAP known limit must have no evidence_refs")
                if limit.get("support_kind") == "EVIDENCE_BACKED" and not references:
                    errors.append(f"{label}: EVIDENCE_BACKED known limit requires evidence_refs")
                if limit.get("support_kind") == "EVIDENCE_BACKED":
                    for reference in references:
                        if isinstance(reference, str):
                            claimed.add(reference)
        top_refs = assessment.get("evidence_refs", [])
        if not isinstance(top_refs, list):
            errors.append(f"{label}: top-level evidence_refs is not an array")
            continue
        try:
            canonical_claimed = sorted(claimed, key=evidence_ref_sort_key)
            for reference in top_refs:
                parsed_subject, _ = parse_evidence_ref(reference)
                if parsed_subject != subject_id:
                    errors.append(f"{label}: evidence reference belongs to another subject: {reference}")
            if top_refs != canonical_claimed:
                errors.append(
                    f"{label}: top-level evidence_refs must equal the canonical exact union of claim refs"
                )
        except DomainError as exc:
            errors.append(f"{label}: {exc}")
            continue
        if status in {"CANDIDATE", "REVIEWED"} and not top_refs:
            errors.append(f"{label}: {status} requires a nonempty evidence union")
        if status == "UNASSESSED" and top_refs:
            errors.append(f"{label}: UNASSESSED requires an empty evidence union")
        basis_commit = scope.get("basis_commit")
        if not isinstance(basis_commit, str):
            errors.append(f"{label}: basis_commit is missing")
            continue
        try:
            basis = snapshot(basis_commit)
            basis_records = snapshot_records(basis)
            basis_by_subject = {
                item["analysis_subject_id"]: item for item in basis_records
            }
            basis_record = basis_by_subject.get(subject_id)
            if basis_record is None:
                raise DomainError(
                    f"basis discovery registry does not contain subject {subject_id}"
                )
            if assessment.get("character_entity_id") != basis_record.get("character_entity_id"):
                errors.append(f"{label}: character_entity_id differs from basis discovery record")
            for field in ("continuity_id", "incarnation_id", "state_id"):
                if scope.get(field) != basis_record.get(field):
                    errors.append(
                        f"{label}: assessment_scope.{field} differs from basis discovery record"
                    )
            if basis_record.get("subject_kind") == "COMPOSITE_MODEL":
                if sorted(scope.get("component_subject_ids", [])) != sorted(
                    basis_record.get("component_subject_ids", [])
                ):
                    errors.append(
                        f"{label}: composite scope differs from basis discovery component set"
                    )
            elif "component_subject_ids" in scope:
                errors.append(
                    f"{label}: non-composite basis subject cannot have component_subject_ids"
                )
            entries = resolve_evidence_entries(top_refs, basis_records, basis)
            digest, _serialized = evidence_set_digest(entries)
            if scope.get("evidence_set_algorithm") != EVIDENCE_SET_ALGORITHM:
                errors.append(f"{label}: invalid evidence_set_algorithm")
            if scope.get("evidence_set_sha256") != digest:
                errors.append(
                    f"{label}: evidence_set_sha256 mismatch; declared="
                    f"{scope.get('evidence_set_sha256')}, derived={digest}"
                )
            basis_authority = AuthorityGraph(basis)
            errors.extend(f"{label}: basis authority: {item}" for item in basis_authority.errors)
            if status == "REVIEWED":
                for reference, entry in zip(top_refs, entries):
                    if not basis_authority.current_eligible(entry["repository_path"]):
                        errors.append(
                            f"{label}: REVIEWED basis evidence is not current eligible: {reference}"
                        )
            if comparison_commit is not None:
                comparison = snapshot(comparison_commit)
                current_authority = AuthorityGraph(comparison)
                comparison_stale = any(
                    not current_authority.current_eligible(entry["repository_path"])
                    for entry in entries
                )
                try:
                    comparison_records = snapshot_records(comparison)
                    comparison_entries = resolve_evidence_entries(
                        top_refs, comparison_records, comparison
                    )
                    comparison_digest, _ = evidence_set_digest(comparison_entries)
                    comparison_stale = comparison_stale or comparison_digest != digest
                    comparison_record = {
                        item["analysis_subject_id"]: item for item in comparison_records
                    }.get(subject_id)
                    if comparison_record is None:
                        comparison_stale = True
                    else:
                        comparison_stale = comparison_stale or any(
                            scope.get(field) != comparison_record.get(field)
                            for field in ("continuity_id", "incarnation_id", "state_id")
                        )
                        if comparison_record.get("subject_kind") == "COMPOSITE_MODEL":
                            comparison_stale = comparison_stale or sorted(
                                scope.get("component_subject_ids", [])
                            ) != sorted(comparison_record.get("component_subject_ids", []))
                except DomainError:
                    comparison_stale = True
                if comparison_stale and status == "REVIEWED":
                    errors.append(
                        f"{label}: assessment is REVIEWED but current comparison requires STALE"
                    )
        except DomainError as exc:
            errors.append(f"{label}: {exc}")

    outgoing: dict[str, str] = {}

    def compatibility_key(assessment: Mapping[str, Any]) -> tuple[Any, ...]:
        scope = assessment.get("assessment_scope")
        if not isinstance(scope, Mapping):
            return (None, None, None, None)
        components = scope.get("component_subject_ids", [])
        if not isinstance(components, list) or not all(isinstance(item, str) for item in components):
            canonical_components: tuple[str, ...] | None = None
        else:
            canonical_components = tuple(sorted(components, key=lambda item: item.encode("ascii")))
        return (
            scope.get("continuity_id"),
            scope.get("incarnation_id"),
            scope.get("state_id"),
            canonical_components,
        )

    for assessment_id, assessment in by_assessment.items():
        predecessor = assessment.get("supersedes_assessment_id")
        successor = assessment.get("superseded_by_assessment_id")
        if isinstance(predecessor, str):
            other = by_assessment.get(predecessor)
            if other is None or other.get("superseded_by_assessment_id") != assessment_id:
                errors.append(f"assessment supersession is unresolved/nonreciprocal: {predecessor} -> {assessment_id}")
            else:
                outgoing[predecessor] = assessment_id
                if other.get("character_entity_id") != assessment.get("character_entity_id"):
                    errors.append(f"assessment supersession crosses entities: {predecessor} -> {assessment_id}")
                if other.get("analysis_subject_id") != assessment.get("analysis_subject_id"):
                    errors.append(f"assessment supersession crosses subjects: {predecessor} -> {assessment_id}")
                if compatibility_key(other) != compatibility_key(assessment):
                    errors.append(
                        f"assessment supersession has incompatible subject scope: "
                        f"{predecessor} -> {assessment_id}"
                    )
        if isinstance(successor, str):
            other = by_assessment.get(successor)
            if other is None or other.get("supersedes_assessment_id") != assessment_id:
                errors.append(f"assessment supersession is unresolved/nonreciprocal: {assessment_id} -> {successor}")
            else:
                outgoing[assessment_id] = successor
    for seed in outgoing:
        seen: set[str] = set()
        node = seed
        while node in outgoing:
            if node in seen:
                errors.append(f"assessment supersession cycle includes {node}")
                break
            seen.add(node)
            node = outgoing[node]
    return sorted(set(errors), key=lambda item: item.encode("utf-8"))


def _schema_validator_class(schema: Mapping[str, Any], label: str) -> Any:
    try:
        import jsonschema
    except ImportError as exc:
        raise DomainError(
            "jsonschema is unavailable; the separately approved offline dependency "
            "environment is required for Draft 2020-12 validation"
        ) from exc

    def inspect_refs(value: Any) -> None:
        if isinstance(value, dict):
            for keyword in ("$ref", "$dynamicRef", "$recursiveRef"):
                ref = value.get(keyword)
                if ref is not None and (not isinstance(ref, str) or not ref.startswith("#")):
                    raise DomainError(
                        f"{label}: remote or nonlocal {keyword} is prohibited: {ref!r}"
                    )
            for child in value.values():
                inspect_refs(child)
        elif isinstance(value, list):
            for child in value:
                inspect_refs(child)

    inspect_refs(schema)
    validator_class = jsonschema.validators.Draft202012Validator
    validator_class.check_schema(schema)
    return validator_class


def validate_schema_document(schema: Mapping[str, Any], label: str) -> None:
    _schema_validator_class(schema, label)


_DIAGNOSTIC_SOURCE_RE = re.compile(r"^[A-Za-z0-9_./-]{1,240}$")
_DIAGNOSTIC_SEGMENT_RE = re.compile(r"^[A-Za-z0-9_$.-]{1,80}$")


@dataclass(frozen=True)
class SchemaDiagnostic:
    repository_path: str
    line_number: int
    analysis_subject_id: str
    instance_path: str
    schema_path: str
    validator_keyword: str
    text: str

    def sort_key(self) -> tuple[bytes, int, bytes, bytes, bytes, bytes]:
        return (
            self.repository_path.encode("utf-8"),
            self.line_number,
            self.instance_path.encode("utf-8"),
            self.schema_path.encode("utf-8"),
            self.validator_keyword.encode("ascii"),
            self.text.encode("utf-8"),
        )

    def render(self) -> str:
        return (
            f"{self.repository_path}:line={self.line_number}:"
            f"instance={self.instance_path}:schema={self.schema_path}:"
            f"subject={self.analysis_subject_id}:validator={self.validator_keyword}: "
            f"{self.text}"
        )


_SCHEMA_DIAGNOSTIC_TEXT = {
    "additionalProperties": "object contains a disallowed property",
    "allOf": "value does not satisfy every required schema branch",
    "anyOf": "value does not satisfy a permitted schema branch",
    "const": "value does not equal the required constant",
    "contains": "array lacks a required matching item",
    "enum": "value is not a permitted enum member",
    "maxItems": "array has too many items",
    "maxLength": "string exceeds the permitted length",
    "minItems": "array has too few items",
    "minLength": "string is shorter than permitted",
    "not": "value satisfies a prohibited schema",
    "oneOf": "value does not satisfy exactly one schema branch",
    "pattern": "string violates the required grammar",
    "required": "object lacks a required property",
    "type": "value has an invalid JSON type",
    "uniqueItems": "array items are not unique",
}


def _schema_property_names(value: Any) -> set[str]:
    result: set[str] = set()
    if isinstance(value, Mapping):
        properties = value.get("properties")
        if isinstance(properties, Mapping):
            result.update(key for key in properties if isinstance(key, str))
        for child in value.values():
            result.update(_schema_property_names(child))
    elif isinstance(value, list):
        for child in value:
            result.update(_schema_property_names(child))
    return result


def _diagnostic_path(
    parts: Iterable[Any], *, allowed_strings: set[str] | None = None
) -> str:
    rendered: list[str] = []
    for part in parts:
        if isinstance(part, int) and part >= 0:
            rendered.append(f"[{part:012d}]")
        elif (
            isinstance(part, str)
            and _DIAGNOSTIC_SEGMENT_RE.fullmatch(part)
            and (allowed_strings is None or part in allowed_strings)
        ):
            rendered.append(part)
        else:
            rendered.append("<redacted>")
    return "<root>" if not rendered else "/" + "/".join(rendered)


def schema_diagnostics(
    instance: Any,
    schema: Mapping[str, Any],
    repository_path: str,
    *,
    line_number: int | None = None,
) -> list[SchemaDiagnostic]:
    validator_class = _schema_validator_class(schema, repository_path)
    validator = validator_class(schema)
    source = (
        repository_path
        if _DIAGNOSTIC_SOURCE_RE.fullmatch(repository_path)
        else "<redacted-source>"
    )
    line = line_number if isinstance(line_number, int) and line_number > 0 else 0
    subject = "<unavailable>"
    if isinstance(instance, Mapping):
        candidate = instance.get("analysis_subject_id")
        if (
            isinstance(candidate, str)
            and len(candidate) <= 256
            and SUBJECT_ID_RE.fullmatch(candidate)
        ):
            subject = candidate
    instance_properties = _schema_property_names(schema)
    result: list[SchemaDiagnostic] = []
    for error in validator.iter_errors(instance):
        instance_path = _diagnostic_path(
            error.absolute_path, allowed_strings=instance_properties
        )
        schema_path = _diagnostic_path(error.absolute_schema_path)
        keyword = error.validator if isinstance(error.validator, str) else "unknown"
        if not _DIAGNOSTIC_SEGMENT_RE.fullmatch(keyword):
            keyword = "unknown"
        result.append(
            SchemaDiagnostic(
                repository_path=source,
                line_number=line,
                analysis_subject_id=subject,
                instance_path=instance_path,
                schema_path=schema_path,
                validator_keyword=keyword,
                text=_SCHEMA_DIAGNOSTIC_TEXT.get(
                    keyword, "value violates a schema constraint"
                ),
            )
        )
    return sorted(result, key=SchemaDiagnostic.sort_key)


def render_schema_diagnostics(diagnostics: Iterable[SchemaDiagnostic]) -> list[str]:
    unique = set(diagnostics)
    return [item.render() for item in sorted(unique, key=SchemaDiagnostic.sort_key)]


def schema_errors(
    instance: Any,
    schema: Mapping[str, Any],
    repository_path: str,
    *,
    line_number: int | None = None,
) -> list[str]:
    return render_schema_diagnostics(
        schema_diagnostics(
            instance,
            schema,
            repository_path,
            line_number=line_number,
        )
    )


def atomic_write_text(path: Path, text: str) -> None:
    data = text.encode("utf-8")
    if b"\r" in data or data.startswith(b"\xef\xbb\xbf"):
        raise DomainError("generated output must be UTF-8 without BOM and LF-only")
    temporary = path.with_name(f".{path.name}.tmp")
    if temporary.exists():
        raise DomainError(f"refusing to overwrite preexisting temporary file: {temporary}")
    try:
        temporary.write_bytes(data)
        os.replace(temporary, path)
    finally:
        if temporary.exists():
            temporary.unlink()
