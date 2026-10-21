#!/usr/bin/env python3
"""Mechanical integration; candidate Git objects are never checked out or executed."""
from __future__ import annotations

import argparse
import base64
import errno
import hashlib
import json
import os
import re
import subprocess
import tempfile
import time
import urllib.error
import urllib.parse
import urllib.request
from contextlib import contextmanager
from pathlib import Path

import integration_lock
from integration_lock import IntegrationLock, LockError

REPOSITORY = "deep-blue-zero/anime-manga-ln-games-analysis"
OWNER = "deep-blue-zero"
AUDIT = "Repository integration audit"
AUDIT_INTEGRATION_ID = 15368
MAIN_RULESET_ID = 25199066
TAG_RULESET_ID = 21946617
AUDIT_WORKFLOW_ID = 347147204
AUDIT_REPORTER_ID = 41898282
AUDIT_WORKFLOW = ".github/workflows/repository-audit.yml"
BRANCH = re.compile(r"^(series|studies)/[a-z0-9][a-z0-9-]*$")
TEMP_BRANCH = re.compile(r"^(codex|chatgpt|claude)/[a-z0-9][a-z0-9-]*$")
SHA = re.compile(r"^[0-9a-f]{40}$")
GENERATED = frozenset({
    "governance/MANGA_ANIME_CORPUS_INDEX.md", "series/README.md",
    "series/registry.json", "studies/README.md", "studies/registry.json",
})
CHARACTER = frozenset({"CHARACTER_ANALYSIS_INDEX.md", "characters/registry.jsonl"})
CONTROL_PATHS = (
    "AGENTS.md", ".github", "tools", "governance/policies",
    "governance/repository-controls", "governance/AUTHORITY_STATE.yaml",
    "governance/AUTHORITY_SCOPE.json", "governance/schemas",
)
AUTHOR = {"name": OWNER, "email": "50891441+peipw@users.noreply.github.com"}
COMMITTER = {"name": "GitHub", "email": "noreply@github.com"}
RESERVED_ROOTS = (".github/", "tools/", "crosswalk/", "provenance/", "governance/")
RESERVED_FILES = frozenset({"AGENTS.md", "LICENSE.md", "THIRD_PARTY_NOTICES.md", "CONTRIBUTING.md",
                            ".gitattributes", ".gitignore", "characters/README.md",
                            "characters/RECONSTRUCTION_CAPABILITY_SPEC.md"})
LOADED_SHA256 = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()


class Blocked(RuntimeError):
    """A candidate cannot be integrated under the current contract."""


class Halt(RuntimeError):
    """Stop the run: main or shared controls require attention."""


class GitError(Halt):
    """A Git execution failure, distinct from a merge conflict."""

    def __init__(self, operation: str, returncode: int, output: bytes = b""):
        super().__init__(f"Git {operation} failed (exit {returncode})")
        self.returncode = returncode
        self.output = output


class ApiError(RuntimeError):
    def __init__(self, method: str, path: str, status: int):
        super().__init__(f"GitHub {method} {path}: HTTP {status}")
        self.status = status


def exact_sha(value: str) -> str:
    if not isinstance(value, str) or not SHA.fullmatch(value):
        raise Blocked("Expected a full commit SHA")
    return value


def scoped_paths(branch: str, paths: set[str]) -> bool:
    return bool(BRANCH.fullmatch(branch)) and all(
        path.startswith(branch + "/") or path in GENERATED | CHARACTER for path in paths
    )


def eligible_paths(branch: str, paths: set[str], role: str) -> bool:
    if any(path in RESERVED_FILES or (path.startswith(RESERVED_ROOTS)
            and path != "governance/MANGA_ANIME_CORPUS_INDEX.md") for path in paths):
        return False
    if BRANCH.fullmatch(branch):
        return scoped_paths(branch, paths)
    # Conservative routine cross-cutting envelope: root Markdown documentation
    # and deterministic routing only, never another analytical root or character output.
    return role == "primary" and bool(TEMP_BRANCH.fullmatch(branch)) and bool(paths) and all(
        path in GENERATED or ("/" not in path and path.endswith(".md") and path not in CHARACTER)
        for path in paths
    )


def tag_protection(ruleset: dict) -> None:
    if (not isinstance(ruleset, dict) or ruleset.get("id") != TAG_RULESET_ID
            or ruleset.get("target") != "tag" or ruleset.get("enforcement") != "active"
            or ruleset.get("conditions") != {"ref_name": {"include": ["refs/tags/activation/**"], "exclude": []}}
            or ruleset.get("bypass_actors") != [] or ruleset.get("current_user_can_bypass") != "never"):
        raise Halt("Activation-tag protection is absent, changed or permits bypass")
    rules = ruleset.get("rules")
    if (not isinstance(rules, list) or any(not isinstance(row, dict) for row in rules)
            or not {"deletion", "non_fast_forward"} <= {row.get("type") for row in rules}):
        raise Halt("Activation tags must prohibit deletion and non-fast-forward changes")


def protection_method(ruleset: dict, repository: dict) -> str:
    if (not isinstance(ruleset, dict) or ruleset.get("id") != MAIN_RULESET_ID
            or ruleset.get("target") != "branch" or ruleset.get("enforcement") != "active"
            or ruleset.get("conditions") != {"ref_name": {"include": ["refs/heads/main"], "exclude": []}}
            or ruleset.get("bypass_actors") != [] or ruleset.get("current_user_can_bypass") != "never"):
        raise Halt("The main ruleset must be active, target only main, and permit no owner/admin bypass")
    entries = ruleset.get("rules")
    if (not isinstance(entries, list) or any(not isinstance(rule, dict)
            or not isinstance(rule.get("type"), str) for rule in entries)):
        raise Halt("The main ruleset rules are unreadable")
    rules = {rule["type"]: rule for rule in entries}
    if len(rules) != len(entries) or not {
        "deletion", "non_fast_forward", "required_linear_history", "required_status_checks"
    } <= set(rules):
        raise Halt("The main ruleset must preserve deletion, non-fast-forward, linear-history and audit gates")
    parameters = rules["required_status_checks"].get("parameters")
    if not isinstance(parameters, dict) or parameters.get("strict_required_status_checks_policy") is not True:
        raise Halt("The main ruleset must require up-to-date branches")
    checks = parameters.get("required_status_checks")
    if not isinstance(checks, list) or not any(
        isinstance(check, dict) and check.get("context") == AUDIT
        and check.get("integration_id") == AUDIT_INTEGRATION_ID for check in checks
    ):
        raise Halt("The main ruleset must require the trusted integration audit")
    if not isinstance(repository, dict) or repository.get("allow_squash_merge") is not True:
        raise Halt("The ruleset-compatible squash method is not enabled")
    return "squash"


class GitHub:
    def __init__(self, token: str, *, preview: bool = False):
        self.token, self.preview = token, preview

    def request(self, method: str, path: str, payload: dict | None = None):
        if self.preview and method != "GET":
            raise Halt("Preview prohibits every remote mutation")
        endpoint = "/user" if path == "/user" else f"/repos/{REPOSITORY}" + ("/" + path if path else "")
        headers = {"Accept": "application/vnd.github+json", "X-GitHub-Api-Version": "2022-11-28"}
        if self.token:
            headers["Authorization"] = "Bearer " + self.token
        data = None if payload is None else json.dumps(payload).encode("utf-8")
        request = urllib.request.Request("https://api.github.com" + endpoint, data=data, headers=headers, method=method)
        try:
            with urllib.request.urlopen(request, timeout=30) as response:
                raw = response.read()
                return json.loads(raw) if raw else None
        except urllib.error.HTTPError as exc:
            # Never include response bodies, headers, or credentials in reports.
            raise ApiError(method, path, exc.code) from None

    def pages(self, path: str) -> list:
        rows = []
        separator = "&" if "?" in path else "?"
        for page in range(1, 101):
            batch = self.request("GET", f"{path}{separator}per_page=100&page={page}")
            if not isinstance(batch, list):
                raise Halt("Unexpected paginated GitHub response")
            rows.extend(batch)
            if len(batch) < 100:
                return rows
        raise Halt("Pagination limit reached; incomplete inventory is not usable")

    def head(self, branch: str) -> str:
        name = urllib.parse.quote(branch, safe="")
        return exact_sha(self.request("GET", f"git/ref/heads/{name}")["object"]["sha"])

    def audit_statuses(self, sha: str) -> list[dict]:
        return [row for row in self.pages(f"commits/{exact_sha(sha)}/statuses") if row["context"] == AUDIT]

    def status(self, sha: str) -> dict | None:
        # Newest first: an older success cannot override a later failure/pending.
        return next(iter(self.audit_statuses(sha)), None)

    def audit_run(self, sha: str, status: dict | None, *, require_success: bool = True) -> dict | None:
        if (not status or status.get("creator", {}).get("login") != "github-actions[bot]"
                or status.get("creator", {}).get("id") != AUDIT_REPORTER_ID):
            return None
        match = re.fullmatch(r"https://github\.com/" + re.escape(REPOSITORY) + r"/actions/runs/([0-9]+)", status.get("target_url", ""))
        if not match:
            return None
        run = self.request("GET", "actions/runs/" + match[1])
        if (run.get("path", "").split("@", 1)[0] != AUDIT_WORKFLOW
                or run.get("workflow_id") != AUDIT_WORKFLOW_ID
                or run.get("actor", {}).get("login") not in {OWNER, "github-actions[bot]"}
                or run.get("event") not in {"push", "workflow_dispatch", "schedule", "repository_dispatch"}
                or run.get("head_repository", {}).get("full_name") != REPOSITORY):
            return None
        if require_success and run.get("conclusion") != "success":
            return None
        if run.get("event") in {"push", "workflow_dispatch", "schedule"} and run.get("head_sha") != sha:
            return None
        return run

    def source_audit(self, branch: str, sha: str) -> dict | None:
        # The reporter publishes a commit status only at the end of the audit.
        # Discover the latest push run without filtering out terminal failures.
        query = urllib.parse.urlencode({"branch": branch, "head_sha": exact_sha(sha),
                                       "event": "push", "per_page": 1})
        runs = self.request("GET", "actions/workflows/repository-audit.yml/runs?" + query)["workflow_runs"]
        run = next(iter(runs), None)
        if (not run or run.get("path", "").split("@", 1)[0] != AUDIT_WORKFLOW
                or run.get("head_sha") != sha or run.get("head_branch") != branch
                or run.get("event") != "push" or run.get("actor", {}).get("login") != OWNER
                or run.get("triggering_actor", {}).get("login") != OWNER
                or run.get("head_repository", {}).get("full_name") != REPOSITORY):
            return None
        return run


class Graph:
    def __init__(self, directory: Path):
        self.directory = directory
        self.git("init", "--bare", ".")
        self.git("remote", "add", "origin", f"https://github.com/{REPOSITORY}.git")
        self.git("config", "core.hooksPath", str(directory / "disabled-hooks"))
        # This object store is disposable; no background writer should outlive it.
        self.git("config", "--local", "maintenance.auto", "false")
        self.git("config", "--local", "gc.auto", "0")

    def git(self, *args: str, input_text: str | None = None, extra_env: dict | None = None,
            raw: bool = False) -> str | bytes:
        environment = {key: value for key, value in os.environ.items() if key not in {"OWNER_TOKEN", "READ_TOKEN", "GH_TOKEN", "GITHUB_TOKEN"}}
        environment.update(extra_env or {})
        try:
            result = subprocess.run(["git", *args], cwd=self.directory, env=environment,
                                    input=None if input_text is None else input_text.encode("utf-8"),
                                    capture_output=True, check=False, timeout=120)
        except subprocess.TimeoutExpired:
            raise GitError(args[0], 124) from None
        if result.returncode:
            raise GitError(args[0], result.returncode, result.stdout)
        return result.stdout if raw else result.stdout.decode("utf-8", "strict").strip("\r\n")

    def fetch(self, sha: str) -> None:
        self.git("fetch", "--no-tags", "origin", exact_sha(sha))

    def paths(self, base: str, head: str, *, triple: bool = False) -> set[str]:
        delta = exact_sha(base) + ("..." if triple else "..") + exact_sha(head)
        return set(filter(None, self.git("diff", "--name-only", "--no-renames", "-z", delta, "--").split("\0")))

    def ancestor(self, base: str, head: str) -> bool:
        return self.git("merge-base", exact_sha(base), exact_sha(head)) == base

    def tree(self, sha: str) -> str:
        return self.git("rev-parse", exact_sha(sha) + "^{tree}")

    def verify_runtime(self, controller: str, base: str) -> None:
        if not self.ancestor(controller, base):
            raise Halt("Executor code must be an integrated ancestor of current main")
        binding = json.loads(self.git("show", f"{base}:governance/repository-controls/nightly-integration-policy.json"))
        for key, path, loaded in (
            ("controller", "tools/nightly_integration.py", LOADED_SHA256),
            ("lock", "tools/integration_lock.py", integration_lock.LOADED_SHA256),
        ):
            content = self.git("show", f"{base}:{path}", raw=True)
            if (binding.get(key) != path or binding.get(key + "_sha256") != loaded
                    or hashlib.sha256(content).hexdigest() != loaded):
                raise Halt("Loaded executor code differs from the reviewed main binding")

    def verify_identities(self, base: str, head: str) -> None:
        policy = json.loads(self.git("show", f"{base}:governance/repository-controls/tracked-file-policy.json"))
        authors = {(row["name"], row["email"]) for row in policy["allowed_author_identities"]}
        committers = {(row["name"], row["email"]) for row in policy["allowed_committer_identities"]}
        for line in self.git("log", "--format=%H%x09%an%x09%ae%x09%cn%x09%ce", f"{base}..{head}").splitlines():
            sha, author, email, committer, committer_email = line.split("\t")
            if (author, email) not in authors or (committer, committer_email) not in committers:
                raise Halt("Unapproved commit identity at " + sha)

    def verify_curation_commits(self, base: str, head: str) -> None:
        for line in self.git("rev-list", "--parents", f"{base}..{head}").splitlines():
            sha, *parents = line.split()
            if len(parents) > 1:
                if not any(self.paths(parent, sha) & CHARACTER for parent in parents):
                    continue
                if len(parents) != 2:
                    raise Blocked("Character imports require a verifiable two-parent merge")
                # First-parent or combined diffs alone can hide authored merge
                # resolutions. Recompute the merge without executing candidate
                # code, then require exact preservation of its character blobs.
                try:
                    output = self.git("merge-tree", "--write-tree", "--name-only", *parents)
                except GitError as exc:
                    first = exc.output.splitlines()[0] if exc.output else b""
                    if exc.returncode != 1 or not re.fullmatch(rb"[0-9a-f]{40}", first):
                        raise
                    output = exc.output.decode("utf-8", "strict")
                    lines = output.splitlines()
                    if "" not in lines[1:]:
                        raise Halt("Character merge conflict paths are unreadable") from exc
                    conflicts = set(lines[1:lines.index("", 1)])
                    if conflicts & CHARACTER:
                        raise Blocked("Character merge conflicts require a separate curation repair") from exc
                expected = exact_sha(output.splitlines()[0])
                if self.paths(expected, sha) & CHARACTER:
                    raise Blocked("Merge commit authors character changes outside a separate curation repair")
                continue
            paths = set(filter(None, self.git("diff-tree", "--root", "--no-commit-id", "--name-only", "-r", "--no-renames", "-z", sha).split("\0")))
            if paths & CHARACTER and not paths <= CHARACTER:
                raise Blocked("Curation repair must be a separately identifiable two-file commit")

    def merge_tree(self, source: str, base: str) -> str:
        try:
            output = self.git("merge-tree", "--write-tree", exact_sha(source), exact_sha(base))
        except GitError as exc:
            # Some Git versions also return 1 for invalid objects; a completed
            # conflicted merge must emit its resulting tree as the first line.
            first = exc.output.splitlines()[0] if exc.output else b""
            if exc.returncode == 1 and re.fullmatch(rb"[0-9a-f]{40}", first):
                raise Blocked("Git merge-tree found conflicts; no conflict resolution is authorized") from exc
            raise
        return exact_sha(output.splitlines()[0])

    def reconcile_commit(self, source: str, base: str, tree: str) -> str:
        identities = {"GIT_AUTHOR_NAME": AUTHOR["name"], "GIT_AUTHOR_EMAIL": AUTHOR["email"],
                      "GIT_COMMITTER_NAME": COMMITTER["name"], "GIT_COMMITTER_EMAIL": COMMITTER["email"]}
        return exact_sha(self.git("commit-tree", tree, "-p", source, "-p", base,
                                  input_text="chore: reconcile main for nightly integration\n", extra_env=identities))

    def push(self, branch: str, sha: str, token: str) -> None:
        if not BRANCH.fullmatch(branch):
            raise Halt("Only an existing stable analytical branch may receive a reconciliation")
        auth = base64.b64encode(("x-access-token:" + token).encode()).decode()
        self.git("push", "origin", f"{exact_sha(sha)}:refs/heads/{branch}", extra_env={
            "GIT_CONFIG_COUNT": "1", "GIT_CONFIG_KEY_0": "http.https://github.com/.extraheader",
            "GIT_CONFIG_VALUE_0": "AUTHORIZATION: basic " + auth,
        })


class Integrator:
    def __init__(self, api: GitHub, graph: Graph, *, preview: bool, controller_sha: str,
                 budget: int = 9900, wait_seconds: int = 4200, role: str = "fallback", report_path: Path | None = None):
        self.api, self.graph, self.preview = api, graph, preview
        self.controller_sha = exact_sha(controller_sha)
        self.deadline = time.monotonic() + budget
        self.wait_seconds = wait_seconds
        self.rows: list[dict] = []
        self.method = "squash"
        self.access = "NOT_CHECKED"
        self.role = role
        self.held_branches: set[str] = set()
        self.lock = IntegrationLock(api, role=role, controller_sha=self.controller_sha, author=AUTHOR, committer=COMMITTER)
        self.report_path = report_path or Path("nightly-integration-report.json")

    def enabled(self) -> None:
        mode = self.api.request("GET", "actions/variables/INTEGRATION_EXECUTOR_MODE")
        if mode.get("value") != self.role:
            raise Halt("Executor disabled or assigned to the other route; no apply permitted")
        if self.role == "fallback":
            flag = self.api.request("GET", "actions/variables/NIGHTLY_INTEGRATION_ENABLED")
            if flag.get("value") != "true":
                raise Halt("Manual fallback apply is disabled")

    def protections(self) -> str:
        method = protection_method(self.api.request("GET", f"rulesets/{MAIN_RULESET_ID}"), self.api.request("GET", ""))
        tag_protection(self.api.request("GET", f"rulesets/{TAG_RULESET_ID}"))
        return method

    def guard_mutation(self, branch: str | None = None, source: str | None = None, base: str | None = None) -> None:
        if self.preview:
            raise Halt("Preview prohibits every remote mutation")
        self.lock.assert_owned()
        self.check_time()
        self.enabled()
        self.access = self.access_check()
        if self.protections() != self.method:
            raise Halt("Protection changed during integration")
        if branch:
            self.same_heads(branch, source, base)
            self.candidate_pr(branch)
        elif base and self.api.head("main") != base:
            raise Halt("main advanced before post-merge dispatch")
        self.lock.assert_owned()

    def observe_hold(self, branch: str, pr: dict) -> None:
        if pr.get("draft") or "nightly-hold" in {row["name"] for row in pr.get("labels", [])}:
            self.held_branches.add(branch)
        if branch in self.held_branches:
            raise Blocked("PR was held during this cycle; only a later owner-released cycle may apply")

    def check_time(self) -> None:
        if time.monotonic() >= self.deadline:
            raise Halt("Run deadline reached; remaining candidates are deferred")

    def same_heads(self, branch: str, source: str, base: str) -> None:
        if self.api.head("main") != base:
            raise Halt("main advanced outside this controller; restart from a newly audited base")
        if self.api.head(branch) != source:
            raise Blocked("Source advanced; preserve the newer work for a later run")

    def candidate_pr(self, branch: str) -> dict | None:
        if branch in self.held_branches:
            raise Blocked("PR was held during this cycle")
        query = urllib.parse.urlencode({"state": "open", "base": "main", "head": OWNER + ":" + branch})
        prs = self.api.pages("pulls?" + query)
        if len(prs) > 1:
            raise Blocked("Multiple matching PRs require reconciliation")
        if not prs:
            return None
        self.observe_hold(branch, prs[0])
        self.allowed_pr(prs[0])
        return prs[0]

    @staticmethod
    def allowed_pr(pr: dict) -> None:
        if pr.get("draft") or "nightly-hold" in {row["name"] for row in pr.get("labels", [])}:
            raise Blocked("PR is a draft or carries nightly-hold")
        if pr.get("user", {}).get("login") != OWNER or pr.get("head", {}).get("repo", {}).get("full_name") != REPOSITORY:
            raise Blocked("Only owner-authored, same-repository PRs are eligible")
        if pr.get("state") != "open" or pr.get("base", {}).get("ref") != "main":
            raise Blocked("PR is no longer open against main")

    def generated_child(self, source: str, observed: str) -> bool:
        commit = self.api.request("GET", f"git/commits/{observed}")
        if [parent["sha"] for parent in commit["parents"]] != [source]:
            return False
        if "Generated-From: " + source not in commit["message"].splitlines():
            return False
        for field, identity in (("author", AUTHOR), ("committer", COMMITTER)):
            if any(commit[field].get(key) != value for key, value in identity.items()):
                return False
        self.graph.fetch(observed)
        changed = self.graph.paths(source, observed)
        return bool(changed) and changed <= GENERATED

    def prior_integration(self, branch: str, source: str, base: str) -> dict | None:
        # A squash leaves the source outside main's ancestry. Only a merged PR
        # for this exact tip plus whole-tree equality proves it was preserved.
        query = urllib.parse.urlencode({"state": "closed", "base": "main", "head": OWNER + ":" + branch})
        for pr in self.api.pages("pulls?" + query):
            self.check_time()
            head, target = pr.get("head") or {}, pr.get("base") or {}
            if (pr.get("state") != "closed" or not pr.get("merged_at")
                    or (pr.get("user") or {}).get("login") != OWNER
                    or head.get("ref") != branch or head.get("sha") != source
                    or (head.get("repo") or {}).get("full_name") != REPOSITORY
                    or target.get("ref") != "main"
                    or (target.get("repo") or {}).get("full_name") != REPOSITORY):
                continue
            merged = exact_sha(pr.get("merge_commit_sha"))
            self.graph.fetch(merged)
            if self.graph.ancestor(merged, base) and self.graph.tree(merged) == self.graph.tree(source):
                return pr
        return None

    def wait_source(self, branch: str, source: str, base: str, end: float) -> None:
        waiting = False
        while time.monotonic() < end:
            self.candidate_pr(branch)
            self.same_heads(branch, source, base)
            status = self.api.status(source)
            if status and status["state"] in {"failure", "error"}:
                raise Blocked("Source repository audit failed")
            if (status and status["state"] in {"success", "pending"}
                    and self.api.audit_run(source, status)):
                return
            if self.preview:
                raise Blocked("Source has no successful authored-content or full audit run")
            run = self.api.source_audit(branch, source)
            if not run:
                raise Blocked("Source has no successful audit or trusted push audit to await")
            if run.get("status") not in {"queued", "in_progress", "waiting", "pending", "requested"} or run.get("conclusion") is not None:
                # The reporter may finish between the status and run requests.
                if run.get("status") == "completed" and run.get("conclusion") == "success":
                    status = self.api.status(source)
                    if (status and status["state"] in {"success", "pending"}
                            and self.api.audit_run(source, status)):
                        return
                raise Blocked("Source push audit ended without a successful trusted audit status")
            if not waiting:
                print(f"Waiting for source audit {run['id']} on {branch} at {source}", flush=True)
                waiting = True
            time.sleep(max(0, min(15, end - time.monotonic())))
        raise Blocked("Timed out awaiting the source audit; no integration was attempted")

    def wait_final(self, branch: str, source: str, base: str, *, end: float | None = None) -> str:
        end = min(self.deadline, time.monotonic() + self.wait_seconds) if end is None else min(self.deadline, end)
        final = source
        while time.monotonic() < end:
            self.candidate_pr(branch)
            if self.api.head("main") != base:
                raise Halt("main advanced while housekeeping was running")
            observed = self.api.head(branch)
            if observed != final:
                if final != source or not self.generated_child(source, observed):
                    raise Blocked("Unexpected source update while waiting for housekeeping")
                final = observed
            status = self.api.status(final)
            if status and status["state"] in {"failure", "error"}:
                raise Blocked("Final repository audit failed")
            run = self.api.audit_run(final, status)
            # Only the full audit dispatched by the existing housekeeper certifies readiness.
            stable_final = (run and run.get("event") == "repository_dispatch"
                            and run.get("actor", {}).get("login") == "github-actions[bot]")
            routine_final = (not BRANCH.fullmatch(branch) and self.role == "primary"
                             and run and run.get("actor", {}).get("login") == OWNER)
            if status and status["state"] == "success" and (stable_final or routine_final):
                return final
            time.sleep(max(0, min(15, end - time.monotonic())))
        raise Blocked("Timed out awaiting housekeeping and its exact-commit full audit")

    def wait_post_merge(self, sha: str, previous_status_id: int) -> None:
        end = min(self.deadline, time.monotonic() + 1800)
        while time.monotonic() < end:
            statuses = self.api.audit_statuses(sha)
            latest = next(iter(statuses), None)
            if latest and latest["id"] > previous_status_id:
                if latest["state"] in {"failure", "error"}:
                    raise Halt("Already integrated, but post-merge audit failed; further merges stopped")
                if latest["state"] == "success" and self.api.audit_run(sha, latest):
                    # The owner-token merge also starts a push audit. Its newer
                    # success must not hide the explicitly dispatched full audit.
                    # Keep the latest overall failure/pending safeguards above,
                    # and use only the newest trusted dispatch result below.
                    for status in statuses:
                        if status["id"] <= previous_status_id:
                            break
                        run = self.api.audit_run(sha, status, require_success=False)
                        if (not run or run.get("event") != "repository_dispatch"
                                or run.get("actor", {}).get("login") != OWNER):
                            continue
                        if status["state"] in {"failure", "error"} or run.get("conclusion") in {
                            "failure", "cancelled", "timed_out", "action_required", "startup_failure",
                        }:
                            raise Halt("Already integrated, but post-merge audit failed; further merges stopped")
                        if status["state"] == "success" and run.get("conclusion") == "success":
                            return
                        break
            time.sleep(15)
        raise Halt("Already integrated, but explicit post-merge audit did not finish; further merges stopped")

    def access_check(self) -> str:
        """Confirm owner-only write access before any write.

        No other collaborator, no pending invitation and no write-enabled
        deploy key. Apply halts when access is wider or unreadable. Preview
        never mutates, so it records what it could read and continues.
        """
        try:
            collaborators = self.api.pages("collaborators?affiliation=all")
            invitations = self.api.pages("invitations")
            keys = self.api.pages("keys")
        except ApiError as exc:
            if self.preview:
                return f"UNVERIFIED: HTTP {exc.status}"
            raise Halt("Collaborators, invitations or deploy keys are unreadable; owner-only access is unverified") from None
        others = sum(1 for row in collaborators if not isinstance(row, dict) or row.get("login") != OWNER)
        writable_keys = sum(1 for row in keys if not isinstance(row, dict) or row.get("read_only") is not True)
        if others or invitations or writable_keys:
            detail = (
                f"{others} other collaborator(s), {len(invitations)} pending invitation(s) "
                f"and {writable_keys} write-enabled deploy key(s)"
            )
            if self.preview:
                return "NOT_OWNER_ONLY: " + detail
            raise Halt("Repository access is not owner-only: " + detail)
        return "VERIFIED_OWNER_ONLY"

    def preflight(self) -> str:
        base = self.api.head("main")
        self.graph.fetch(base)
        self.graph.fetch(self.controller_sha)
        changed = self.graph.paths(self.controller_sha, base)
        if any(path == root or path.startswith(root + "/") for path in changed for root in CONTROL_PATHS):
            raise Halt("Repository controls changed since this workflow started; run the current workflow")
        if not self.preview:
            self.enabled()
            self.graph.verify_runtime(self.controller_sha, base)
            if self.api.request("GET", "/user").get("login") != OWNER:
                raise Halt("NIGHTLY_INTEGRATION_TOKEN must authenticate the repository owner")
        self.access = self.access_check()
        if not self.preview:
            self.method = self.protections()
            status = self.api.status(base)
            if not status or status["state"] != "success" or not self.api.audit_run(base, status):
                raise Halt("The starting main commit does not have a successful independent audit")
        return base

    def process(self, branch: str, source: str, base: str, row: dict) -> str:
        self.check_time()
        self.same_heads(branch, source, base)
        self.graph.fetch(source)
        if self.graph.ancestor(source, base):
            row["outcome"] = "already_integrated"
            return base
        if not eligible_paths(branch, self.graph.paths(base, source, triple=True), self.role):
            raise Blocked("Branch delta exceeds its delegated path scope or includes reserved work")
        self.graph.verify_identities(base, source)
        if self.graph.paths(base, source, triple=True) & CHARACTER:
            self.graph.verify_curation_commits(base, source)
        self.candidate_pr(branch)
        # Initial audit and final housekeeping share the existing source budget.
        source_deadline = min(self.deadline, time.monotonic() + self.wait_seconds)
        self.wait_source(branch, source, base, source_deadline)
        try:
            tree = self.graph.merge_tree(source, base)
        except Blocked:
            preserved = self.prior_integration(branch, source, base)
            if preserved is None:
                raise
            self.same_heads(branch, source, base)
            row.update(outcome="already_integrated", pr=preserved["number"],
                       integration_sha=preserved["merge_commit_sha"],
                       detail="Exact source tree verified in a prior merged PR on main; no conflict resolution or write needed")
            return base
        if tree == self.graph.tree(base):
            row["outcome"] = "no_content_change"
            return base
        needs_reconciliation = not self.graph.ancestor(base, source)
        if self.preview:
            row.update(outcome="candidate", reconciliation_required=needs_reconciliation,
                       detail="Preview only; fresh final checks and live protections are required before merging")
            return base
        if needs_reconciliation:
            if not BRANCH.fullmatch(branch):
                raise Blocked("Routine temporary PR needs author reconciliation and a fresh full audit")
            reconciled = self.graph.reconcile_commit(source, base, tree)
            self.guard_mutation(branch, source, base)
            try:
                self.graph.push(branch, reconciled, self.api.token)
            except GitError:
                observed = self.api.head(branch)
                if observed != reconciled and not self.generated_child(reconciled, observed):
                    raise
            row["reconciled_sha"] = reconciled
            source = reconciled
        final = self.wait_final(branch, source, base, end=source_deadline)
        self.graph.fetch(final)
        if not self.graph.ancestor(base, final) or not eligible_paths(branch, self.graph.paths(base, final), self.role):
            raise Blocked("Final branch no longer incorporates main within the allowed path boundary")
        self.same_heads(branch, final, base)
        self.graph.verify_identities(base, final)
        pr = self.candidate_pr(branch)
        if pr is None:
            if not BRANCH.fullmatch(branch):
                raise Blocked("Routine temporary integration requires an existing owner-authored PR")
            self.guard_mutation(branch, final, base)
            pr = self.api.request("POST", "pulls", {
                "title": "Integrate " + branch, "head": branch, "base": "main",
                "body": "Nightly integration of an audited analytical branch. The controller rechecks the exact head, preserves branch protections, and explicitly audits the resulting main commit.",
            })
        row.update(pr=pr["number"], final_source_sha=final)
        pr = self.api.request("GET", f"pulls/{pr['number']}")
        self.observe_hold(branch, pr)
        self.allowed_pr(pr)
        if pr["head"]["sha"] != final:
            raise Blocked("PR head changed before merge")
        self.same_heads(branch, final, base)
        # The strict no-bypass main ruleset closes the base race the REST SHA cannot.
        method = self.protections()
        if method != self.method:
            raise Halt("Merge configuration changed during integration")
        latest = self.api.status(final)
        if not latest or latest["state"] != "success" or not self.api.audit_run(final, latest):
            raise Blocked("Final audit is no longer successful")
        self.check_time()
        if self.deadline - time.monotonic() < 1800:
            raise Halt("Insufficient time remains for post-merge validation; defer remaining candidates")
        row["outcome"] = "merge_requested"
        self.save()
        self.guard_mutation(branch, final, base)
        pr = self.api.request("GET", f"pulls/{pr['number']}")
        self.observe_hold(branch, pr)
        self.allowed_pr(pr)
        if (pr["head"]["sha"] != final or pr.get("mergeable") is not True
                or pr.get("mergeable_state") != "clean"):
            raise Blocked("Protected PR readiness or required reviews are not satisfied")
        latest = self.api.status(final)
        run = self.api.audit_run(final, latest)
        if (not latest or latest["state"] != "success" or not run
                or (BRANCH.fullmatch(branch) and (run.get("event") != "repository_dispatch"
                    or run.get("actor", {}).get("login") != "github-actions[bot]"))
                or (not BRANCH.fullmatch(branch) and run.get("actor", {}).get("login") != OWNER)):
            raise Blocked("Final exact-head certification changed before merge")
        self.same_heads(branch, final, base)
        self.lock.assert_owned()
        try:
            result = self.api.request("PUT", f"pulls/{pr['number']}/merge", {"sha": final, "merge_method": self.method})
        except (ApiError, OSError) as exc:
            observed_pr = self.api.request("GET", f"pulls/{pr['number']}")
            if not observed_pr.get("merged"):
                if not isinstance(exc, ApiError) or exc.status not in {403, 405, 409, 422}:
                    raise Halt("Merge outcome is uncertain; retain the lock for owner recovery") from None
                raise Blocked("Merge was not confirmed; no mutation retry was issued") from None
            result = {"merged": True, "sha": observed_pr["merge_commit_sha"]}
        if result.get("merged") is False:
            raise Blocked("GitHub did not confirm a protected merge")
        if result.get("merged") is not True:
            raise Halt("Merge acknowledgement is unreadable; retain the lock for owner recovery")
        row["outcome"] = "integrated_unverified"
        try:
            merged = exact_sha(result.get("sha"))
        except Blocked:
            raise Halt("GitHub reported integration without a valid commit SHA; retain the lock for owner recovery") from None
        row["integration_sha"] = merged
        self.save()
        self.graph.fetch(merged)
        if self.graph.tree(merged) != self.graph.tree(final):
            raise Halt("Already integrated, but the resulting tree differs from the audited source")
        previous = self.api.status(merged)
        self.guard_mutation(base=merged)
        self.api.request("POST", "dispatches", {
            "event_type": "audit-generated-commit",
            "client_payload": {"commit_sha": merged, "branch": "main"},
        })
        self.wait_post_merge(merged, previous["id"] if previous else 0)
        row["outcome"] = "merged_verified"
        self.save()
        if self.api.head("main") != merged:
            raise Halt("The integration passed, but main advanced externally; remaining candidates are deferred")
        return merged

    def save(self) -> None:
        report = json.dumps({"preview": self.preview, "role": self.role, "lock": self.lock.receipt(),
                             "access_check": self.access, "branches": self.rows}, indent=2) + "\n"
        self.report_path.parent.mkdir(parents=True, exist_ok=True)
        temporary = self.report_path.with_suffix(".tmp")
        with temporary.open("w", encoding="utf-8", newline="\n") as stream:
            stream.write(report)
            stream.flush()
            os.fsync(stream.fileno())
        os.replace(temporary, self.report_path)
        summary = os.environ.get("GITHUB_STEP_SUMMARY")
        if summary:
            Path(summary).write_text("Nightly analytical integration - " + ("preview" if self.preview else "apply") + "\n\n```json\n" + report + "```\n", encoding="utf-8")
        if self.rows:
            print(json.dumps(self.rows[-1]), flush=True)

    def run(self, selected: str = "") -> None:
        allowed_branch = lambda name: bool(BRANCH.fullmatch(name) or (self.role == "primary" and TEMP_BRANCH.fullmatch(name)))
        if selected and not allowed_branch(selected):
            raise Halt("The selected branch is outside this executor route")
        base = self.preflight()
        if not self.preview:
            self.lock.acquire(base)
            self.save()
            # Capture the operative inventory/base only under shared ownership.
            base = self.preflight()
        opened = self.api.pages("pulls?state=open&base=main")
        temporary_prs = set()
        for pr in opened:
            branch = pr.get("head", {}).get("ref", "")
            if (not allowed_branch(branch) or pr.get("user", {}).get("login") != OWNER
                    or pr.get("head", {}).get("repo", {}).get("full_name") != REPOSITORY):
                continue
            temporary_prs.add(branch)
            if pr.get("draft") or "nightly-hold" in {label["name"] for label in pr.get("labels", [])}:
                self.held_branches.add(branch)
        branches = sorted((item["name"], item["commit"]["sha"]) for item in self.api.pages("branches")
                          if allowed_branch(item["name"]) and (BRANCH.fullmatch(item["name"]) or item["name"] in temporary_prs)
                          and (not selected or item["name"] == selected))
        if selected and not branches:
            # Complete inventory proves absence before any candidate mutation.
            # Record an unsuccessful scan, then release through the normal path.
            self.rows.append({"branch": selected, "base_sha": base, "outcome": "blocked",
                              "detail": "The selected branch does not exist or has no eligible PR"})
            self.save()
        for branch, source in branches:
            row = {"branch": branch, "source_sha": exact_sha(source), "base_sha": base, "outcome": "pending"}
            self.rows.append(row)
            try:
                base = self.process(branch, source, base, row)
            except Blocked as exc:
                if row["outcome"] == "integrated_unverified":
                    row["detail"] = str(exc)
                    raise Halt("Already integrated, but verification failed; further merges stopped") from exc
                row.update(outcome="blocked", detail=str(exc))
                if self.preview:
                    message = f"{branch}: {exc}".replace("%", "%25").replace("\r", "%0D").replace("\n", "%0A")
                    print("::warning::" + message, flush=True)
            except Exception as exc:
                row["detail"] = str(exc)
                raise
            finally:
                self.save()
        if not self.preview:
            self.lock.release()
            self.save()


def cleanup_directory(temporary: tempfile.TemporaryDirectory) -> None:
    # Retry disposal only: replaying integration could repeat remote mutations.
    for attempt in range(3):
        try:
            temporary.cleanup()
            return
        except OSError as exc:
            if exc.errno != errno.ENOTEMPTY or attempt == 2:
                raise
            time.sleep(1)


@contextmanager
def temporary_graph_directory():
    temporary = tempfile.TemporaryDirectory(prefix="nightly-integration-")
    try:
        yield temporary.name
    except BaseException as original:
        try:
            cleanup_directory(temporary)
        except OSError as cleanup_error:
            # Keep both failures, including the original traceback and cause.
            raise BaseExceptionGroup("Integration and temporary Git cleanup failed",
                                     [original, cleanup_error]) from None
        raise
    else:
        cleanup_directory(temporary)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--mode", choices=("preview", "apply"), default="preview")
    parser.add_argument("--branch", default="")
    parser.add_argument("--role", choices=("primary", "fallback"), default="fallback")
    parser.add_argument("--state-dir", type=Path, help="Durable external receipt directory; required for primary apply")
    args = parser.parse_args()
    preview = args.mode == "preview"
    if os.environ.get("GITHUB_REPOSITORY", REPOSITORY) != REPOSITORY:
        parser.error("Unexpected repository")
    if not preview and args.role == "fallback" and (
            os.environ.get("GITHUB_REF") != "refs/heads/main" or os.environ.get("GITHUB_ACTIONS") != "true"
            or os.environ.get("GITHUB_EVENT_NAME") != "workflow_dispatch" or os.environ.get("GITHUB_ACTOR") != OWNER):
        parser.error("Fallback apply requires an explicit owner dispatch of the trusted main workflow")
    if not preview and args.role == "primary" and not args.state_dir:
        parser.error("Primary apply requires --state-dir outside disposable working directories")
    token = os.environ.get("READ_TOKEN", "") if preview else os.environ.get("OWNER_TOKEN", "")
    if not preview and not token:
        parser.error("Configure NIGHTLY_INTEGRATION_TOKEN before enabling integration")
    controller_sha = os.environ.get("GITHUB_SHA") or subprocess.check_output(["git", "rev-parse", "HEAD"], text=True).strip()
    result = 0
    with temporary_graph_directory() as temporary:
        worker = Integrator(GitHub(token, preview=preview), Graph(Path(temporary)), preview=preview,
                            controller_sha=controller_sha, role=args.role)
        if args.state_dir:
            worker.report_path = args.state_dir / ("integration-" + worker.lock.run_id + ".json")
        try:
            worker.run(args.branch)
            if not preview and any(row["outcome"] == "blocked" for row in worker.rows):
                result = 1
        except (Halt, Blocked, LockError, ApiError, OSError, ValueError, KeyError) as exc:
            worker.rows.append({"branch": "run", "outcome": "halted", "detail": str(exc)})
            result = 1
        finally:
            worker.save()
            report = worker.report_path.read_text(encoding="utf-8")
            print(report)

    return result


if __name__ == "__main__":
    raise SystemExit(main())
