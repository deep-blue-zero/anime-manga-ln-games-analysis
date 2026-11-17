#!/usr/bin/env python3
"""Portable, hash-checked Git evidence for a completed source-branch run.

This is an integrity proof, never an owner-authorization mechanism. It contains
textual Git objects, not source media, and never installs objects or fetches refs.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
from pathlib import Path, PurePosixPath
from typing import Any, Mapping

from character_index_core import (
    DomainError, GitSnapshot, SnapshotEntry, run_git,
    validate_repository_path,
)

PROOF_NAME = ".repository/completed-run-publication.json"
PROOF_SCHEMA = "anime-manga-ln-games-analysis/completed-run-publication/v1"
OID = re.compile(r"(?:[0-9a-f]{40}|[0-9a-f]{64})\Z")


def object_id(kind: str, data: bytes, width: int) -> str:
    if width not in (40, 64):
        raise DomainError("invalid Git object format")
    return hashlib.new(
        "sha1" if width == 40 else "sha256",
        kind.encode("ascii") + b" " + str(len(data)).encode("ascii") + b"\0" + data,
    ).hexdigest()


def _oid(value: Any, width: int | None = None) -> str:
    if not isinstance(value, str) or not OID.fullmatch(value) or (
        width is not None and len(value) != width
    ):
        raise DomainError("invalid Git object identity")
    return value


def commit_headers(text: str) -> tuple[str, list[str]]:
    """Read a commit's tree and first parent lines exactly as Git does.

    Git separates headers only by LF and takes parents solely from the lines
    immediately after the tree, so no other line break or header can add one.
    """
    headers = text.split("\n\n", 1)[0].split("\n")
    if not headers[0].startswith("tree ") or any(
        line.startswith("tree ") for line in headers[1:]
    ):
        raise DomainError("completion proof commit has invalid tree header")
    parents = []
    for line in headers[1:]:
        if not line.startswith("parent "):
            break
        parents.append(line[7:])
    return headers[0][5:], parents


class CompletionProof:
    """Verify a bounded textual object graph independently of the object DB."""

    def __init__(self, record: Any, prefix: str, entrypoint: str):
        keys = {"schema", "project_root", "canonical_entrypoint", "active_commit",
                "completion_commit", "commits", "trees", "blobs"}
        if not isinstance(record, Mapping) or set(record) != keys:
            raise DomainError("completion proof has missing or unknown fields")
        if (record["schema"] != PROOF_SCHEMA or record["project_root"] != prefix
                or record["canonical_entrypoint"] != entrypoint):
            raise DomainError("completion proof schema or project route disagrees")
        validate_repository_path(prefix.rstrip("/"))
        validate_repository_path(entrypoint)
        if not prefix.endswith("/") or not entrypoint.startswith(prefix):
            raise DomainError("completion proof entrypoint is outside its root")
        self.active = _oid(record["active_commit"])
        self.completion = _oid(record["completion_commit"], len(self.active))
        self.width = len(self.active)
        self.record = record
        for field in ("commits", "trees", "blobs"):
            if not isinstance(record[field], Mapping):
                raise DomainError(f"completion proof {field} must be an object")
        if set(record["commits"]) != {self.active, self.completion}:
            raise DomainError("completion proof must contain exactly its two commits")
        self.commit_trees = {}
        parents = {}
        for oid, text in record["commits"].items():
            _oid(oid, self.width)
            if (not isinstance(text, str) or "\0" in text
                    or object_id("commit", text.encode("utf-8"), self.width) != oid):
                raise DomainError("completion proof commit hash mismatch")
            tree, commit_parents = commit_headers(text)
            self.commit_trees[oid] = _oid(tree, self.width)
            parents[oid] = [_oid(parent, self.width) for parent in commit_parents]
        if not parents[self.completion] or parents[self.completion][0] != self.active:
            raise DomainError("completion commit must directly follow its active first parent")
        self.trees: dict[str, list[tuple[str, str, str]]] = {}
        for oid, rows in record["trees"].items():
            _oid(oid, self.width)
            if not isinstance(rows, list):
                raise DomainError("completion proof tree must be a list")
            raw = bytearray()
            entries = []
            names = set()
            order = []
            for row in rows:
                if not isinstance(row, list) or len(row) != 3:
                    raise DomainError("completion proof tree row is invalid")
                mode, name, child = row
                if not isinstance(mode, str) or mode not in {"40000", "100644", "100755", "120000", "160000"}:
                    raise DomainError("completion proof tree mode is invalid")
                if (not isinstance(name, str) or not name or name in {".", ".."}
                        or "/" in name or "\0" in name or name in names):
                    raise DomainError("completion proof tree name is invalid")
                _oid(child, self.width)
                names.add(name)
                encoded = name.encode("utf-8")
                order.append(encoded + (b"/" if mode == "40000" else b""))
                raw.extend(mode.encode("ascii") + b" " + encoded + b"\0" + bytes.fromhex(child))
                entries.append((mode, name, child))
            if order != sorted(order) or object_id("tree", bytes(raw), self.width) != oid:
                raise DomainError("completion proof tree hash or ordering mismatch")
            self.trees[oid] = entries
        for oid, text in record["blobs"].items():
            _oid(oid, self.width)
            if (not isinstance(text, str) or "\0" in text
                    or object_id("blob", text.encode("utf-8"), self.width) != oid):
                raise DomainError("completion proof blob hash mismatch")

    def tree(self, oid: str) -> list[tuple[str, str, str]]:
        if oid not in self.trees:
            raise DomainError("completion proof is missing a historical tree")
        return self.trees[oid]

    def resolve(self, commit: str, path: str) -> tuple[str, str]:
        oid = self.commit_trees[commit]
        parts = PurePosixPath(path).parts
        for index, part in enumerate(parts):
            matches = [(mode, child) for mode, name, child in self.tree(oid) if name == part]
            if len(matches) != 1:
                raise DomainError(f"completion proof is missing historical path {path}")
            mode, oid = matches[0]
            if index < len(parts) - 1 and mode != "40000":
                raise DomainError("completion proof path crosses a non-tree")
        return mode, oid

    def blob(self, oid: str, path: str, candidate: GitSnapshot) -> bytes:
        current = candidate.get(path)
        if current is not None and object_id("blob", current.data, self.width) == oid:
            return current.data
        text = self.record["blobs"].get(oid)
        if not isinstance(text, str):
            raise DomainError(f"completion proof is missing historical blob {path}")
        return text.encode("utf-8")

    def markdown_snapshot(self, candidate: GitSnapshot, prefix: str, entrypoint: str
                          ) -> tuple[GitSnapshot, SnapshotEntry]:
        entries = {}
        mode, root = self.resolve(self.completion, prefix.rstrip("/"))
        if mode != "40000":
            raise DomainError("completion proof project root is not a tree")

        def walk(oid: str, base: str) -> None:
            for mode, name, child in self.tree(oid):
                path = base + name
                validate_repository_path(path)
                if mode == "40000":
                    walk(child, path + "/")
                elif path.endswith(".md"):
                    entries[path] = SnapshotEntry(path, mode, self.blob(child, path, candidate))

        walk(root, prefix)
        mode, oid = self.resolve(self.active, entrypoint)
        if mode != "100644":
            raise DomainError("completion proof active entrypoint is not a regular blob")
        active = SnapshotEntry(entrypoint, mode, self.blob(oid, entrypoint, candidate))
        return GitSnapshot(candidate.root, self.completion, entries), active


def build_proof(candidate: GitSnapshot, prefix: str, entrypoint: str,
                completion: str) -> dict[str, Any]:
    """Export only relevant trees and unavailable historical Markdown blobs."""
    _oid(completion)
    root = candidate.root
    raw_completion = run_git(root, "cat-file", "commit", completion).decode("utf-8")
    _tree, parents = commit_headers(raw_completion)
    if not parents:
        raise DomainError("completion commit has no active first parent")
    active = parents[0]
    record: dict[str, Any] = dict(
        schema=PROOF_SCHEMA, project_root=prefix, canonical_entrypoint=entrypoint,
        active_commit=active, completion_commit=completion,
        commits={}, trees={}, blobs={},
    )
    width = len(completion)

    def tree(oid: str) -> list[list[str]]:
        if oid not in record["trees"]:
            rows = []
            for item in run_git(root, "ls-tree", "-z", oid).split(b"\0"):
                if not item:
                    continue
                metadata, name = item.split(b"\t", 1)
                mode, _kind, child = metadata.decode("ascii").split()
                rows.append([mode.lstrip("0"), name.decode("utf-8"), child])
            record["trees"][oid] = rows
        return record["trees"][oid]

    def resolve(commit: str, path: str) -> tuple[str, str]:
        oid = commit_headers(record["commits"][commit])[0]
        for part in PurePosixPath(path).parts:
            rows = [(mode, child) for mode, name, child in tree(oid) if name == part]
            if len(rows) != 1:
                raise DomainError(f"missing historical path {path}")
            mode, oid = rows[0]
        return mode, oid

    def blob(oid: str, path: str) -> None:
        entry = candidate.get(path)
        if entry is None or object_id("blob", entry.data, width) != oid:
            record["blobs"][oid] = run_git(root, "cat-file", "blob", oid).decode("utf-8")

    def walk(oid: str, base: str) -> None:
        for mode, name, child in tree(oid):
            path = base + name
            if mode == "40000":
                walk(child, path + "/")
            elif path.endswith(".md"):
                blob(child, path)

    for commit in (active, completion):
        record["commits"][commit] = run_git(root, "cat-file", "commit", commit).decode("utf-8")
    _mode, active_oid = resolve(active, entrypoint)
    blob(active_oid, entrypoint)
    mode, project_oid = resolve(completion, prefix.rstrip("/"))
    if mode != "40000":
        raise DomainError("historical project root is not a tree")
    walk(project_oid, prefix)
    # Validate the export before returning it; never install missing objects.
    CompletionProof(record, prefix, entrypoint).markdown_snapshot(candidate, prefix, entrypoint)
    return record


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", type=Path, default=Path("."))
    parser.add_argument("--project-root", required=True)
    parser.add_argument("--entrypoint", required=True)
    parser.add_argument("--completion", required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    record = build_proof(GitSnapshot.from_worktree(args.repo), args.project_root,
                         args.entrypoint, args.completion)
    # Exclusive creation prevents silently replacing a reviewed proof.
    with args.output.open("x", encoding="utf-8", newline="\n") as output:
        output.write(json.dumps(record, ensure_ascii=False, indent=2) + "\n")


if __name__ == "__main__":
    main()
