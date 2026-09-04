#!/usr/bin/env python3
"""Prepare or validate one exact staged repository change."""

from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
from pathlib import Path
from typing import Any


OBLIGATIONS_PATH = "governance/repository-controls/change-obligations.json"
EXPECTED_SCHEMA = "anime-manga-ln-games-analysis/change-obligations/v1"


def git(root: Path, *args: str) -> bytes:
    return subprocess.check_output(
        ["git", "-C", str(root), *args], stderr=subprocess.PIPE
    )


def nul_paths(raw: bytes) -> set[str]:
    return {
        item.decode("utf-8", "strict") for item in raw.split(b"\0") if item
    }


def staged_changes(root: Path, base: str) -> tuple[set[str], set[str]]:
    raw = git(root, "diff", "--cached", "--name-status", "-z", base, "--")
    fields = [item for item in raw.split(b"\0") if item]
    changed: set[str] = set()
    statuses: set[str] = set()
    index = 0
    while index < len(fields):
        status = fields[index].decode("ascii", "strict")
        index += 1
        statuses.add(status[0])
        path_count = 2 if status[0] in {"R", "C"} else 1
        if index + path_count > len(fields):
            raise RuntimeError("unable to parse staged name-status output")
        for raw_path in fields[index : index + path_count]:
            changed.add(raw_path.decode("utf-8", "strict"))
        index += path_count
    return changed, statuses


def top_level_roots(paths: set[str], root: str) -> set[str]:
    result = set()
    for path in paths:
        if not path.startswith(root):
            continue
        remainder = path[len(root) :]
        if "/" in remainder:
            result.add(remainder.split("/", 1)[0])
    return result


def load_obligations_from_index(root: Path) -> dict[str, Any]:
    raw = git(root, "show", f":{OBLIGATIONS_PATH}")
    value = json.loads(raw.decode("utf-8", "strict"))
    if not isinstance(value, dict) or value.get("schema") != EXPECTED_SCHEMA:
        raise RuntimeError(f"invalid staged obligation map: {OBLIGATIONS_PATH}")
    return value


def active_rules(
    obligations: dict[str, Any],
    changed: set[str],
    base_paths: set[str],
    index_paths: set[str],
) -> list[dict[str, Any]]:
    active = []
    for rule in obligations.get("rules", []):
        trigger = rule.get("trigger", {})
        kind = trigger.get("kind")
        matched = False
        if kind == "tracked_path_set_changed":
            matched = base_paths != index_paths
        elif kind == "path_changed":
            matched = trigger.get("path") in changed
        elif kind == "top_level_roots_changed":
            root = trigger.get("root")
            if isinstance(root, str):
                matched = top_level_roots(base_paths, root) != top_level_roots(
                    index_paths, root
                )
        else:
            raise RuntimeError(f"unsupported obligation trigger kind: {kind!r}")
        if matched:
            active.append(rule)
    return active


def run_python(root: Path, *args: str) -> None:
    environment = os.environ.copy()
    environment["PYTHONDONTWRITEBYTECODE"] = "1"
    subprocess.run([sys.executable, *args], cwd=root, env=environment, check=True)


def main() -> int:
    parser = argparse.ArgumentParser()
    operation = parser.add_mutually_exclusive_group(required=True)
    operation.add_argument("--write-generated", action="store_true")
    operation.add_argument("--check", action="store_true")
    parser.add_argument("--base", default="origin/main")
    parser.add_argument("--repo", type=Path)
    args = parser.parse_args()
    root = args.repo.resolve() if args.repo else Path(__file__).resolve().parents[1]
    base = git(root, "rev-parse", "--verify", f"{args.base}^{{commit}}").decode("ascii").strip()
    changed, _statuses = staged_changes(root, base)
    if not changed:
        raise RuntimeError("the Git index contains no change relative to the selected base")

    base_paths = nul_paths(git(root, "ls-tree", "-r", "--name-only", "-z", base))
    index_paths = nul_paths(git(root, "ls-files", "--cached", "-z"))
    obligations = load_obligations_from_index(root)
    rules = active_rules(obligations, changed, base_paths, index_paths)
    print("ACTIVE OBLIGATIONS:")
    if not rules:
        print("- none beyond invariant validation")
    for rule in rules:
        print(f"- {rule['id']}: {rule['description']}")

    if args.write_generated:
        run_python(root, "tools/update_repository_indexes.py", "--snapshot", "index", "--write")
        if any(rule.get("id") == "character-discovery" for rule in rules):
            run_python(root, "tools/generate_character_index.py", "--snapshot", "index")
        print("Generated files were written to the worktree and were not staged.")
        print("Review and stage the reported outputs by exact path, then run --check.")
        return 0

    unstaged = git(root, "diff", "--name-only", "-z")
    if unstaged:
        paths = sorted(nul_paths(unstaged), key=lambda value: value.encode("utf-8"))
        raise RuntimeError(f"tracked worktree changes are not staged: {paths}")

    missing_outputs = sorted(
        {
            path
            for rule in rules
            for path in rule.get("required_outputs", [])
            if path not in changed
        },
        key=lambda value: value.encode("utf-8"),
    )
    if missing_outputs:
        raise RuntimeError(
            f"staged change omits required synchronized outputs: {missing_outputs}"
        )

    run_python(
        root,
        "tools/validate_repository.py",
        "--phase",
        "current",
        "--snapshot",
        "index",
        "--repo",
        str(root),
    )
    run_python(root, "-m", "unittest", "discover", "-s", "tools/tests", "-p", "test_*.py")
    print(f"PASS: staged pre-commit gate against {base}")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (OSError, RuntimeError, subprocess.CalledProcessError, ValueError) as exc:
        raise SystemExit(f"FAIL: {exc}") from exc
