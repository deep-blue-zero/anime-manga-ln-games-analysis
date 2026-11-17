#!/usr/bin/env python3
"""Prepare or validate one exact staged repository change."""

from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
import tempfile
from contextlib import contextmanager
from pathlib import Path
from typing import Any, Iterator, Mapping


sys.path.insert(0, str(Path(__file__).resolve().parent))
from character_index_core import DomainError, GitSnapshot  # noqa: E402
from validate_repository import (  # noqa: E402
    TRACKED_FILE_POLICY_PATH,
    _policy_from_snapshot,
    commit_identity_policy,
    review_threshold_errors,
    validate_commit_identities,
)

OBLIGATIONS_PATH = "governance/repository-controls/change-obligations.json"
EXPECTED_SCHEMA = "anime-manga-ln-games-analysis/change-obligations/v1"
IDENTITY_ENVIRONMENT = (
    "GIT_AUTHOR_NAME",
    "GIT_AUTHOR_EMAIL",
    "GIT_COMMITTER_NAME",
    "GIT_COMMITTER_EMAIL",
)
IDENTITY_SETTINGS = r"^(user|author|committer)\.(name|email)$"
GIT_IDENT = re.compile(r"(?P<name>.*) <(?P<email>[^<>]*)> \d+ [+-]\d{4}")
IDENTITY_REMEDY = (
    "Set an approved identity from allowed_author_identities and "
    f"allowed_committer_identities in {TRACKED_FILE_POLICY_PATH}"
)


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
        if kind == "path_changed":
            matched = trigger.get("path") in changed
        elif kind == "path_prefix_changed":
            prefix = trigger.get("prefix")
            matched = isinstance(prefix, str) and any(
                path.startswith(prefix) for path in changed
            )
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


def missing_required_output_paths(
    rules: list[dict[str, Any]], index_paths: set[str]
) -> list[str]:
    """Return required output paths that are absent from the staged snapshot.

    A required deterministic output can already contain the expected bytes and
    therefore have no diff to stage.  The generator-specific checks below prove
    content synchronization; this boundary check only proves that each required
    output exists in the candidate index.
    """
    return sorted(
        {
            path
            for rule in rules
            for path in rule.get("required_outputs", [])
            if path not in index_paths
        },
        key=lambda value: value.encode("utf-8"),
    )


def staged_size_errors(root: Path, changed: set[str], index_paths: set[str]) -> list[str]:
    """Apply the validator's review threshold to the staged blobs of the changed paths.

    The repository audit fails any tracked file over the threshold, so the local
    gate reads exactly the same rule from the staged policy and reports it
    before a commit is made. Only the changed paths are read: unchanged files
    were already audited on the base.
    """

    staged = {path for path in changed if path in index_paths}
    if not staged:
        return []
    snapshot = GitSnapshot.from_index(root, paths=staged | {TRACKED_FILE_POLICY_PATH})
    policy = _policy_from_snapshot(snapshot)
    checked = GitSnapshot(root, "INDEX", {path: snapshot.entries[path] for path in staged})
    return review_threshold_errors(checked, policy, "staged")


def identity_configured(root: Path) -> bool:
    """Report whether Git config or the environment names a commit identity.

    Without one Git falls back to a host-derived identity. The housekeeping
    workflow runs this gate before it exports its identity, so an unconfigured
    identity is skipped here; the repository audit still checks every commit.
    """

    if any(os.environ.get(name) for name in IDENTITY_ENVIRONMENT):
        return True
    result = subprocess.run(
        ["git", "-C", str(root), "config", "--get-regexp", IDENTITY_SETTINGS],
        capture_output=True,
    )
    if result.returncode not in {0, 1}:
        raise RuntimeError(f"git config failed: {result.stderr.decode(errors='replace').strip()}")
    return result.returncode == 0


def commit_identity_errors(root: Path, policy: Mapping[str, Any]) -> list[str]:
    """Check the author and committer Git would record for the next commit.

    A cloud sandbox can be recreated between turns with the platform's default
    identity, so the gate reads what Git resolves now rather than trusting an
    identity set earlier in the session.
    """

    allowed_authors, allowed_committers, errors = commit_identity_policy(policy)
    if errors:
        return errors
    for variable, role, allowed in (
        ("GIT_AUTHOR_IDENT", "author", allowed_authors),
        ("GIT_COMMITTER_IDENT", "committer", allowed_committers),
    ):
        raw = git(root, "var", variable).decode("utf-8", "strict").strip()
        match = GIT_IDENT.fullmatch(raw)
        if match is None:
            errors.append(f"unable to parse the Git {role} identity: {raw!r}")
        elif (match["name"], match["email"]) not in allowed:
            errors.append(f"disallowed Git {role} identity: {match['name']} <{match['email']}>")
    return errors


def push_identity_errors(root: Path, revisions: str) -> list[str]:
    """Check every commit in a revision range against HEAD's identity policy."""

    if not revisions or revisions.startswith("-"):
        raise ValueError(f"invalid revision range: {revisions!r}")
    head = git(root, "rev-parse", "--verify", "HEAD^{commit}").decode("ascii").strip()
    snapshot = GitSnapshot.from_commit(root, head, paths={TRACKED_FILE_POLICY_PATH})
    return validate_commit_identities(root, _policy_from_snapshot(snapshot), revisions)


def run_python(root: Path, *args: str, overrides: dict[str, str] | None = None) -> None:
    environment = os.environ.copy()
    environment["PYTHONDONTWRITEBYTECODE"] = "1"
    environment.update(overrides or {})
    subprocess.run([sys.executable, *args], cwd=root, env=environment, check=True)


@contextmanager
def test_temporary_root() -> Iterator[str]:
    """Give the full suite a scratch root so no test skips for want of one.

    CI sets MANGA_ANIME_TEST_TMP; a local gate gets a disposable directory.
    """

    existing = os.environ.get("MANGA_ANIME_TEST_TMP")
    if existing:
        Path(existing).mkdir(parents=True, exist_ok=True)
        yield existing
        return
    with tempfile.TemporaryDirectory(
        prefix="manga-anime-tests-", ignore_cleanup_errors=True
    ) as directory:
        yield directory


def run_full_checks(root: Path, test_tmp: str) -> None:
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
    run_python(
        root,
        "tools/audit_execution.py",
        "--snapshot",
        "index",
        overrides={"MANGA_ANIME_TEST_TMP": test_tmp},
    )


def main() -> int:
    parser = argparse.ArgumentParser()
    operation = parser.add_mutually_exclusive_group(required=True)
    operation.add_argument("--write-generated", action="store_true")
    operation.add_argument("--check", action="store_true")
    operation.add_argument(
        "--check-push",
        metavar="RANGE",
        help="check the author and committer of every commit in RANGE, such as "
        "origin/<branch>..HEAD, before pushing it",
    )
    parser.add_argument(
        "--full",
        action="store_true",
        help="also run the full repository validator and complete unit-test suite",
    )
    parser.add_argument("--base", default="origin/main")
    parser.add_argument("--repo", type=Path)
    args = parser.parse_args()
    root = args.repo.resolve() if args.repo else Path(__file__).resolve().parents[1]
    if args.check_push is not None:
        if args.full:
            raise RuntimeError("--full is valid only with --check")
        unapproved = push_identity_errors(root, args.check_push)
        if unapproved:
            raise RuntimeError(
                f"commits in {args.check_push} would fail the repository audit: "
                + "; ".join(dict.fromkeys(unapproved))
                + f". Do not push. {IDENTITY_REMEDY}, "
                "then rewrite only these unpushed commits with --reset-author; a commit "
                "already on a continuing branch can be removed only by the owner"
            )
        print(f"PASS: every commit in {args.check_push} has an approved author and committer")
        return 0
    base = git(root, "rev-parse", "--verify", f"{args.base}^{{commit}}").decode("ascii").strip()
    changed, _statuses = staged_changes(root, base)
    if not changed:
        raise RuntimeError("the Git index contains no change relative to the selected base")

    # Git owns the complete live path inventory. These sets detect semantic
    # root-topology changes; no checked-in path-list projection is maintained.
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
        if args.full:
            raise RuntimeError("--full is valid only with --check")
        run_python(root, "tools/update_repository_indexes.py", "--snapshot", "index", "--write")
        if any(rule.get("id") == "character-discovery" for rule in rules):
            run_python(root, "tools/generate_character_index.py", "--snapshot", "index")
        if any(rule.get("id") == "character-reconstruction" for rule in rules):
            run_python(root, "tools/generate_reconstruction_index.py", "--snapshot", "index")
        print("Generated files were written to the worktree and were not staged.")
        print("Review and stage the reported outputs by exact path, then run --check.")
        return 0

    unstaged = git(root, "diff", "--name-only", "-z")
    if unstaged:
        paths = sorted(nul_paths(unstaged), key=lambda value: value.encode("utf-8"))
        raise RuntimeError(f"tracked worktree changes are not staged: {paths}")

    missing_outputs = missing_required_output_paths(rules, index_paths)
    if missing_outputs:
        raise RuntimeError(
            f"staged snapshot omits required output paths: {missing_outputs}"
        )
    if identity_configured(root):
        policy = _policy_from_snapshot(
            GitSnapshot.from_index(root, paths={TRACKED_FILE_POLICY_PATH})
        )
        unapproved = commit_identity_errors(root, policy)
        if unapproved:
            raise RuntimeError(
                "the next commit would fail the repository audit: "
                + "; ".join(unapproved)
                + f". Do not commit. {IDENTITY_REMEDY} and rerun this check"
            )
    else:
        print("Commit identity: none configured, so not checked; the audit checks every commit")
    oversized = staged_size_errors(root, changed, index_paths)
    if oversized:
        raise RuntimeError(
            "staged files fail the repository audit's size rule: "
            + "; ".join(sorted(oversized, key=lambda value: value.encode("utf-8")))
        )

    subprocess.run(["git", "-C", str(root), "diff", "--cached", "--check"], check=True)
    run_python(root, "tools/update_repository_indexes.py", "--snapshot", "index", "--check")
    if any(rule.get("id") == "character-discovery" for rule in rules):
        run_python(
            root,
            "tools/generate_character_index.py",
            "--snapshot",
            "index",
            "--check",
        )
    if any(rule.get("id") == "character-reconstruction" for rule in rules):
        run_python(
            root,
            "tools/generate_reconstruction_index.py",
            "--snapshot",
            "index",
            "--check",
        )
    if args.full:
        with test_temporary_root() as test_tmp:
            run_full_checks(root, test_tmp)
        level = "full"
    else:
        run_python(root, "-m", "unittest", "tools.tests.test_repository_indexes")
        level = "targeted"
    print(f"PASS: {level} staged pre-commit gate against {base}")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (DomainError, OSError, RuntimeError, subprocess.CalledProcessError, ValueError) as exc:
        raise SystemExit(f"FAIL: {exc}") from exc
