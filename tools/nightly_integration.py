#!/usr/bin/env python3
"""Deterministic merge gate; candidate Git objects are never checked out or executed.

The CI agent runs it for open owner PRs (``--candidates open-prs``). The owner's
bulk-merge workflow runs it for every series/study branch
(``--candidates analysis-branches``). Merges use GitHub's protected PR endpoint,
the exact audited head and an ordinary merge commit.
"""
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

REPOSITORY = "deep-blue-zero/anime-manga-ln-games-analysis"
OWNER = "deep-blue-zero"
AUDIT = "Repository integration audit"
AUDIT_INTEGRATION_ID = 15368
MAIN_RULESET_ID = 25199066
AUDIT_WORKFLOW_ID = 347147204
AUDIT_REPORTER_ID = 41898282
AUDIT_WORKFLOW = ".github/workflows/repository-audit.yml"
CONTROLLER = "tools/nightly_integration.py"
BRANCH = re.compile(r"^(series|studies)/[a-z0-9][a-z0-9-]*$")
SHA = re.compile(r"^[0-9a-f]{40}$")
CANDIDATES = ("open-prs", "analysis-branches")
GENERATED = frozenset({
    "governance/MANGA_ANIME_CORPUS_INDEX.md", "series/README.md",
    "series/registry.json", "studies/README.md", "studies/registry.json",
})
CHARACTER = frozenset({"CHARACTER_ANALYSIS_INDEX.md", "characters/registry.jsonl"})
AUTHOR = {"name": OWNER, "email": "50891441+peipw@users.noreply.github.com"}
COMMITTER = {"name": "GitHub", "email": "noreply@github.com"}
# Guardrails: the owner merges changes to workflows, this gate, the CI agent's
# own rules, owner authorization records (publication grants, sealed-reading
# releases, phase gates), the archived migration records, frozen provenance
# and legal files. Everything else may integrate.
GUARDRAIL_ROOTS = (".github/", "crosswalk/", "provenance/", "governance/repository-controls/", "governance/archive/")
GUARDRAIL_FILES = frozenset({"AGENTS.md", "LICENSE.md", "THIRD_PARTY_NOTICES.md", CONTROLLER,
                             "governance/policies/NIGHTLY_ANALYTICAL_INTEGRATION.md"})
RECONSTRUCTION = frozenset({"characters/reconstruction_capabilities.jsonl", "characters/CHARACTER_RECONSTRUCTION_INDEX.md"})
RECONSTRUCTION_BRANCH = "character-reconstruction"
RECONSTRUCTION_POLICY = "governance/repository-controls/reconstruction-capability-policy.json"
LOADED_SHA256 = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()


class Blocked(RuntimeError):
    """A candidate cannot be integrated under the current contract."""


class Deferred(RuntimeError):
    """Stop cleanly; remaining candidates wait for the next run."""


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


def eligible_paths(branch: str, paths: set[str]) -> bool:
    if any(path in GUARDRAIL_FILES or path.startswith(GUARDRAIL_ROOTS) for path in paths):
        return False
    # Reconstruction outputs come only from the evaluator's branch, which carries nothing else.
    if branch == RECONSTRUCTION_BRANCH or paths & RECONSTRUCTION:
        return branch == RECONSTRUCTION_BRANCH and paths <= RECONSTRUCTION
    # An analysis branch stays inside its own root; cross-cutting work uses another branch.
    return scoped_paths(branch, paths) if BRANCH.fullmatch(branch) else True


def protection_method(ruleset: dict, repository: dict) -> str:
    # Without Administration access GitHub may omit bypass_actors; the
    # token's own inability to bypass is what protects this gate's merges.
    if (not isinstance(ruleset, dict) or ruleset.get("id") != MAIN_RULESET_ID
            or ruleset.get("target") != "branch" or ruleset.get("enforcement") != "active"
            or ruleset.get("conditions") != {"ref_name": {"include": ["refs/heads/main"], "exclude": []}}
            or ruleset.get("bypass_actors", []) != [] or ruleset.get("current_user_can_bypass") != "never"):
        raise Halt("The main ruleset must be active, target only main, and permit no owner/admin bypass")
    entries = ruleset.get("rules")
    if (not isinstance(entries, list) or any(not isinstance(rule, dict)
            or not isinstance(rule.get("type"), str) for rule in entries)):
        raise Halt("The main ruleset rules are unreadable")
    rules = {rule["type"]: rule for rule in entries}
    if len(rules) != len(entries) or not {"deletion", "non_fast_forward", "required_status_checks"} <= set(rules):
        raise Halt("The main ruleset must preserve deletion, non-fast-forward and audit gates")
    if "required_linear_history" in rules:
        raise Halt("Turn off required linear history on main; integration uses merge commits")
    parameters = rules["required_status_checks"].get("parameters")
    if not isinstance(parameters, dict) or parameters.get("strict_required_status_checks_policy") is not True:
        raise Halt("The main ruleset must require up-to-date branches")
    checks = parameters.get("required_status_checks")
    if not isinstance(checks, list) or not any(
        isinstance(check, dict) and check.get("context") == AUDIT
        and check.get("integration_id") == AUDIT_INTEGRATION_ID for check in checks
    ):
        raise Halt("The main ruleset must require the trusted integration audit")
    if not isinstance(repository, dict) or repository.get("allow_merge_commit") is not True:
        raise Halt("Merge commits are not enabled for this repository")
    return "merge"


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

    def verify_runtime(self, base: str) -> None:
        # Apply runs only the reviewed gate on current main, never a local edit.
        content = self.git("show", f"{exact_sha(base)}:{CONTROLLER}", raw=True)
        if hashlib.sha256(content).hexdigest() != LOADED_SHA256:
            raise Halt("Run the merge script from a fresh checkout of current main")

    def reconstruction_phase(self, base: str) -> str | None:
        return json.loads(self.git("show", f"{exact_sha(base)}:{RECONSTRUCTION_POLICY}")).get("publication_phase")

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
                raise Blocked("Git merge-tree found conflicts; the CI agent or author must reconcile") from exc
            raise
        return exact_sha(output.splitlines()[0])

    def reconcile_commit(self, source: str, base: str, tree: str) -> str:
        identities = {"GIT_AUTHOR_NAME": AUTHOR["name"], "GIT_AUTHOR_EMAIL": AUTHOR["email"],
                      "GIT_COMMITTER_NAME": COMMITTER["name"], "GIT_COMMITTER_EMAIL": COMMITTER["email"]}
        return exact_sha(self.git("commit-tree", tree, "-p", source, "-p", base,
                                  input_text="chore: reconcile main for integration\n", extra_env=identities))

    def push(self, branch: str, sha: str, token: str) -> None:
        if not branch or branch == "main":
            raise Halt("Only a candidate branch may receive a reconciliation")
        auth = base64.b64encode(("x-access-token:" + token).encode()).decode()
        self.git("push", "origin", f"{exact_sha(sha)}:refs/heads/{branch}", extra_env={
            "GIT_CONFIG_COUNT": "1", "GIT_CONFIG_KEY_0": "http.https://github.com/.extraheader",
            "GIT_CONFIG_VALUE_0": "AUTHORIZATION: basic " + auth,
        })


class Integrator:
    def __init__(self, api: GitHub, graph: Graph, *, preview: bool, candidates: str = "open-prs",
                 budget: int = 9900, wait_seconds: int = 4200, report_path: Path | None = None):
        if candidates not in CANDIDATES:
            raise ValueError("Unknown candidate selection: " + candidates)
        self.api, self.graph, self.preview = api, graph, preview
        self.candidates = candidates
        self.deadline = time.monotonic() + budget
        self.wait_seconds = wait_seconds
        self.rows: list[dict] = []
        self.held_branches: set[str] = set()
        self.report_path = report_path or Path("nightly-integration-report.json")

    def guard_mutation(self, branch: str, source: str, base: str) -> None:
        if self.preview:
            raise Halt("Preview prohibits every remote mutation")
        self.check_time()
        self.same_heads(branch, source, base)
        self.candidate_pr(branch)

    def observe_hold(self, branch: str, pr: dict) -> None:
        if pr.get("draft") or "nightly-hold" in {row["name"] for row in pr.get("labels", [])}:
            self.held_branches.add(branch)
        if branch in self.held_branches:
            raise Blocked("PR was held during this cycle; only a later owner-released cycle may apply")

    def check_time(self) -> None:
        if time.monotonic() >= self.deadline:
            raise Deferred("Run deadline reached; remaining candidates wait for the next run")

    def same_heads(self, branch: str, source: str, base: str) -> None:
        if self.api.head("main") != base:
            raise Deferred("main advanced during this run; remaining candidates wait for the next run")
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
        # Branches squash-merged before merge commits were adopted sit outside
        # main's ancestry. A merged PR for this exact tip plus whole-tree
        # equality proves the content was preserved.
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
                raise Deferred("main advanced while awaiting the final audit; remaining candidates wait for the next run")
            observed = self.api.head(branch)
            if observed != final:
                if final != source or not self.generated_child(source, observed):
                    raise Blocked("Unexpected source update while awaiting housekeeping")
                final = observed
            status = self.api.status(final)
            if status and status["state"] in {"failure", "error"}:
                raise Blocked("Final repository audit failed")
            # The reporter marks an analysis push pending only while housekeeping
            # must regenerate routing, so a trusted success means the exact head is ready.
            if status and status["state"] == "success" and self.api.audit_run(final, status):
                return final
            time.sleep(max(0, min(15, end - time.monotonic())))
        raise Blocked("Timed out awaiting housekeeping and the final exact-head audit")

    def wait_post_merge(self, sha: str) -> None:
        # The owner-token merge starts main's push audit on the merge commit.
        end = min(self.deadline, time.monotonic() + 1800)
        while time.monotonic() < end:
            status = self.api.status(sha)
            if status and status["state"] in {"failure", "error"}:
                raise Halt("Already integrated, but main's audit failed; further merges stopped")
            if status and status["state"] == "success" and self.api.audit_run(sha, status):
                return
            time.sleep(15)
        raise Halt("Already integrated, but main's audit did not finish; further merges stopped")

    def access_check(self) -> None:
        # Owner-only write access: no other collaborator, no pending invitation, no write-enabled deploy key.
        try:
            collaborators = self.api.pages("collaborators?affiliation=all")
            invitations = self.api.pages("invitations")
            keys = self.api.pages("keys")
        except ApiError:
            raise Halt("Collaborators, invitations or deploy keys are unreadable; owner-only access is unverified") from None
        others = sum(1 for row in collaborators if not isinstance(row, dict) or row.get("login") != OWNER)
        writable_keys = sum(1 for row in keys if not isinstance(row, dict) or row.get("read_only") is not True)
        if others or invitations or writable_keys:
            raise Halt(f"Repository access is not owner-only: {others} other collaborator(s), "
                       f"{len(invitations)} pending invitation(s) and {writable_keys} write-enabled deploy key(s)")

    def preflight(self) -> str:
        base = self.api.head("main")
        self.graph.fetch(base)
        if not self.preview:
            self.graph.verify_runtime(base)
            if self.api.request("GET", "/user").get("login") != OWNER:
                raise Halt("OWNER_TOKEN must authenticate the repository owner")
            # The CI agent's cloud GitHub proxy refuses these reads; the owner confirms
            # owner-only access when changing settings, and the bulk merge checks it here.
            if self.candidates == "analysis-branches":
                self.access_check()
            protection_method(self.api.request("GET", f"rulesets/{MAIN_RULESET_ID}"), self.api.request("GET", ""))
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
        delta = self.graph.paths(base, source, triple=True)
        if not eligible_paths(branch, delta):
            raise Blocked("Branch touches guardrail paths or files outside its allowed scope; the owner merges it")
        # Until the owner accepts calibration, every reconstruction PR is owner-merged.
        if delta & RECONSTRUCTION and self.graph.reconstruction_phase(base) != "ROUTINE":
            raise Blocked("Reconstruction assessments are owner-merged until calibration is accepted")
        self.graph.verify_identities(base, source)
        if delta & CHARACTER:
            self.graph.verify_curation_commits(base, source)
        self.candidate_pr(branch)
        # Initial audit and final housekeeping share one source budget.
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
        if not self.graph.ancestor(base, final) or not eligible_paths(branch, self.graph.paths(base, final)):
            raise Blocked("Final branch no longer incorporates main within its allowed paths")
        self.same_heads(branch, final, base)
        self.graph.verify_identities(base, final)
        pr = self.candidate_pr(branch)
        if pr is None:
            if not BRANCH.fullmatch(branch):
                raise Blocked("Only analysis branches receive an automatic PR")
            self.guard_mutation(branch, final, base)
            pr = self.api.request("POST", "pulls", {
                "title": "Integrate " + branch, "head": branch, "base": "main",
                "body": "Automated integration of an audited analysis branch. The merge gate rechecks the exact head, merges it with a merge commit, and verifies main's audit of the result.",
            })
        row.update(pr=pr["number"], final_source_sha=final)
        self.check_time()
        if self.deadline - time.monotonic() < 1800:
            raise Deferred("Too little time remains to verify main after a merge; remaining candidates wait for the next run")
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
        if not latest or latest["state"] != "success" or not self.api.audit_run(final, latest):
            raise Blocked("Final exact-head audit is no longer successful")
        # The strict up-to-date rule closes the base race the expected SHA cannot,
        # so confirm it still holds after any wait.
        protection_method(self.api.request("GET", f"rulesets/{MAIN_RULESET_ID}"), self.api.request("GET", ""))
        self.same_heads(branch, final, base)
        try:
            result = self.api.request("PUT", f"pulls/{pr['number']}/merge", {"sha": final, "merge_method": "merge"})
        except (ApiError, OSError) as exc:
            observed_pr = self.api.request("GET", f"pulls/{pr['number']}")
            if not observed_pr.get("merged"):
                if not isinstance(exc, ApiError) or exc.status not in {403, 405, 409, 422}:
                    raise Halt("Merge outcome is uncertain; inspect the PR before the next run") from None
                raise Blocked("Merge was not confirmed; no mutation retry was issued") from None
            result = {"merged": True, "sha": observed_pr["merge_commit_sha"]}
        if result.get("merged") is False:
            raise Blocked("GitHub did not confirm a protected merge")
        if result.get("merged") is not True:
            raise Halt("Merge acknowledgement is unreadable; inspect the PR before the next run")
        row["outcome"] = "integrated_unverified"
        try:
            merged = exact_sha(result.get("sha"))
        except Blocked:
            raise Halt("GitHub reported integration without a valid commit SHA; inspect main before the next run") from None
        row["integration_sha"] = merged
        self.save()
        self.graph.fetch(merged)
        if self.graph.tree(merged) != self.graph.tree(final):
            raise Halt("Already integrated, but the resulting tree differs from the audited source")
        self.wait_post_merge(merged)
        row["outcome"] = "merged_verified"
        self.save()
        return merged

    def save(self) -> None:
        report = json.dumps({"preview": self.preview, "candidates": self.candidates,
                             "branches": self.rows}, indent=2) + "\n"
        self.report_path.parent.mkdir(parents=True, exist_ok=True)
        temporary = self.report_path.with_suffix(".tmp")
        with temporary.open("w", encoding="utf-8", newline="\n") as stream:
            stream.write(report)
            stream.flush()
            os.fsync(stream.fileno())
        os.replace(temporary, self.report_path)
        summary = os.environ.get("GITHUB_STEP_SUMMARY")
        if summary:
            Path(summary).write_text("Analytical integration - " + ("preview" if self.preview else "apply") + "\n\n```json\n" + report + "```\n", encoding="utf-8")
        if self.rows:
            print(json.dumps(self.rows[-1]), flush=True)

    def inventory(self) -> list[tuple[str, str]]:
        opened = [pr for pr in self.api.pages("pulls?state=open&base=main")
                  if pr.get("user", {}).get("login") == OWNER
                  and pr.get("head", {}).get("repo", {}).get("full_name") == REPOSITORY]
        for pr in opened:
            if pr.get("draft") or "nightly-hold" in {label["name"] for label in pr.get("labels", [])}:
                self.held_branches.add(pr["head"]["ref"])
        if self.candidates == "analysis-branches":
            return sorted((item["name"], item["commit"]["sha"]) for item in self.api.pages("branches")
                          if BRANCH.fullmatch(item["name"]))
        return sorted((pr["head"]["ref"], pr["head"]["sha"]) for pr in opened)

    def run(self, selected: str = "", expected_head: str = "") -> None:
        base = self.preflight()
        branches = [row for row in self.inventory() if not selected or row[0] == selected]
        if selected and not branches:
            self.rows.append({"branch": selected, "base_sha": base, "outcome": "blocked",
                              "detail": "The selected branch does not exist or has no eligible PR"})
            self.save()
        for branch, source in branches:
            row = {"branch": branch, "source_sha": exact_sha(source), "base_sha": base, "outcome": "pending"}
            self.rows.append(row)
            try:
                # The CI agent names the head it reviewed; a newer head waits for its review.
                if expected_head and source != expected_head:
                    raise Blocked("The PR head moved since it was reviewed; review the new commits first")
                base = self.process(branch, source, base, row)
            except (Blocked, Deferred) as exc:
                if row["outcome"] == "integrated_unverified":
                    row["detail"] = str(exc)
                    raise Halt("Already integrated, but verification failed; further merges stopped") from exc
                if isinstance(exc, Deferred):
                    row.update(outcome="deferred", detail=str(exc))
                    break
                row.update(outcome="blocked", detail=str(exc))
                if self.preview:
                    message = f"{branch}: {exc}".replace("%", "%25").replace("\r", "%0D").replace("\n", "%0A")
                    print("::warning::" + message, flush=True)
            except Exception as exc:
                row["detail"] = str(exc)
                raise
            finally:
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
    parser.add_argument("--candidates", choices=CANDIDATES, default="open-prs",
                        help="open-prs: every open owner PR (CI agent); analysis-branches: every series/study branch (bulk merge)")
    parser.add_argument("--branch", default="")
    parser.add_argument("--expect-head", default="",
                        help="with --branch: integrate only if the PR head is still this reviewed commit")
    parser.add_argument("--report", type=Path, default=Path("nightly-integration-report.json"),
                        help="JSON receipt path; keep it outside disposable checkouts")
    args = parser.parse_args()
    if args.expect_head and (not args.branch or not SHA.fullmatch(args.expect_head)):
        parser.error("--expect-head needs --branch and a full commit SHA")
    if args.mode == "apply" and args.candidates == "open-prs" and not args.expect_head:
        parser.error("Apply over open PRs needs --branch and --expect-head with the reviewed head")
    preview = args.mode == "preview"
    if os.environ.get("GITHUB_REPOSITORY", REPOSITORY) != REPOSITORY:
        parser.error("Unexpected repository")
    if not preview and os.environ.get("GITHUB_ACTIONS") == "true" and (
            os.environ.get("GITHUB_REF") != "refs/heads/main"
            or os.environ.get("GITHUB_EVENT_NAME") != "workflow_dispatch" or os.environ.get("GITHUB_ACTOR") != OWNER):
        parser.error("In GitHub Actions, apply requires an explicit owner dispatch of the workflow on main")
    token = os.environ.get("READ_TOKEN", "") if preview else os.environ.get("OWNER_TOKEN", "")
    if not preview and not token:
        parser.error("Set OWNER_TOKEN to the owner's integration token before apply")
    result = 0
    with temporary_graph_directory() as temporary:
        worker = Integrator(GitHub(token, preview=preview), Graph(Path(temporary)), preview=preview,
                            candidates=args.candidates, report_path=args.report)
        try:
            worker.run(args.branch, args.expect_head)
            if not preview and any(row["outcome"] == "blocked" for row in worker.rows):
                result = 1
        except (Halt, Blocked, ApiError, OSError, ValueError, KeyError) as exc:
            worker.rows.append({"branch": "run", "outcome": "halted", "detail": str(exc)})
            result = 1
        finally:
            worker.save()
            report = worker.report_path.read_text(encoding="utf-8")
            print(report)

    return result


if __name__ == "__main__":
    raise SystemExit(main())
