#!/usr/bin/env python3
"""Mechanical integration; candidate Git objects are never checked out or executed."""
from __future__ import annotations

import argparse
import base64
import json
import os
import re
import subprocess
import tempfile
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

REPOSITORY = "deep-blue-zero/anime-manga-ln-games-analysis"
OWNER = "deep-blue-zero"
AUDIT = "Repository integration audit"
AUDIT_WORKFLOW = ".github/workflows/repository-audit.yml"
BRANCH = re.compile(r"^(series|studies)/[a-z0-9][a-z0-9-]*$")
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


def protection_method(protection: dict, repository: dict) -> str:
    checks = protection.get("required_status_checks") or {}
    contexts = set(checks.get("contexts", [])) | {item.get("context") for item in checks.get("checks", [])}
    if AUDIT not in contexts or checks.get("strict") is not True:
        raise Halt("main must require the integration audit and up-to-date branches")
    if protection.get("enforce_admins", {}).get("enabled") is not True:
        raise Halt("main protection must also apply to the owner/admin credential")
    method = "squash" if protection.get("required_linear_history", {}).get("enabled", False) else "merge"
    setting = "allow_merge_commit" if method == "merge" else "allow_squash_merge"
    if not repository.get(setting, False):
        raise Halt(f"The protection-compatible {method} method is not enabled")
    return method


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

    def status(self, sha: str) -> dict | None:
        # Newest first: an older success cannot override a later failure/pending.
        return next((row for row in self.pages(f"commits/{exact_sha(sha)}/statuses") if row["context"] == AUDIT), None)

    def audit_run(self, sha: str, status: dict | None) -> dict | None:
        if not status or status.get("creator", {}).get("login") != "github-actions[bot]":
            return None
        match = re.fullmatch(r"https://github\.com/" + re.escape(REPOSITORY) + r"/actions/runs/([0-9]+)", status.get("target_url", ""))
        if not match:
            return None
        run = self.request("GET", "actions/runs/" + match[1])
        if run.get("path", "").split("@", 1)[0] != AUDIT_WORKFLOW or run.get("conclusion") != "success":
            return None
        if run.get("event") in {"push", "workflow_dispatch", "schedule"} and run.get("head_sha") != sha:
            return None
        return run


class Graph:
    def __init__(self, directory: Path):
        self.directory = directory
        self.git("init", "--bare", ".")
        self.git("remote", "add", "origin", f"https://github.com/{REPOSITORY}.git")
        self.git("config", "core.hooksPath", str(directory / "disabled-hooks"))

    def git(self, *args: str, input_text: str | None = None, extra_env: dict | None = None) -> str:
        environment = {key: value for key, value in os.environ.items() if key not in {"OWNER_TOKEN", "READ_TOKEN", "GH_TOKEN", "GITHUB_TOKEN"}}
        environment.update(extra_env or {})
        result = subprocess.run(["git", *args], cwd=self.directory, env=environment,
                                input=None if input_text is None else input_text.encode("utf-8"),
                                capture_output=True, check=False)
        if result.returncode:
            raise GitError(args[0], result.returncode, result.stdout)
        return result.stdout.decode("utf-8", "strict").strip("\r\n")

    def fetch(self, sha: str) -> None:
        self.git("fetch", "--no-tags", "origin", exact_sha(sha))

    def paths(self, base: str, head: str, *, triple: bool = False) -> set[str]:
        delta = exact_sha(base) + ("..." if triple else "..") + exact_sha(head)
        return set(filter(None, self.git("diff", "--name-only", "--no-renames", "-z", delta, "--").split("\0")))

    def ancestor(self, base: str, head: str) -> bool:
        return self.git("merge-base", exact_sha(base), exact_sha(head)) == base

    def tree(self, sha: str) -> str:
        return self.git("rev-parse", exact_sha(sha) + "^{tree}")

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
                 budget: int = 9900, wait_seconds: int = 4200):
        self.api, self.graph, self.preview = api, graph, preview
        self.controller_sha = exact_sha(controller_sha)
        self.deadline = time.monotonic() + budget
        self.wait_seconds = wait_seconds
        self.rows: list[dict] = []
        self.method = "merge"

    def check_time(self) -> None:
        if time.monotonic() >= self.deadline:
            raise Halt("Run deadline reached; remaining candidates are deferred")

    def same_heads(self, branch: str, source: str, base: str) -> None:
        if self.api.head("main") != base:
            raise Halt("main advanced outside this controller; restart from a newly audited base")
        if self.api.head(branch) != source:
            raise Blocked("Source advanced; preserve the newer work for a later run")

    def candidate_pr(self, branch: str) -> dict | None:
        query = urllib.parse.urlencode({"state": "open", "base": "main", "head": OWNER + ":" + branch})
        prs = self.api.pages("pulls?" + query)
        if len(prs) > 1:
            raise Blocked("Multiple matching PRs require reconciliation")
        if not prs:
            return None
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

    def wait_final(self, branch: str, source: str, base: str) -> str:
        end = min(self.deadline, time.monotonic() + self.wait_seconds)
        final = source
        while time.monotonic() < end:
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
            if (status and status["state"] == "success" and run
                    and run.get("event") == "repository_dispatch"
                    and run.get("actor", {}).get("login") == "github-actions[bot]"):
                return final
            time.sleep(15)
        raise Blocked("Timed out awaiting housekeeping and its exact-commit full audit")

    def wait_post_merge(self, sha: str, previous_status_id: int) -> None:
        end = min(self.deadline, time.monotonic() + 1800)
        while time.monotonic() < end:
            status = self.api.status(sha)
            if status and status["id"] > previous_status_id:
                if status["state"] in {"failure", "error"}:
                    raise Halt("Already integrated, but post-merge audit failed; further merges stopped")
                run = self.api.audit_run(sha, status)
                if (status["state"] == "success" and run and run.get("event") == "repository_dispatch"
                        and run.get("actor", {}).get("login") == OWNER):
                    return
            time.sleep(15)
        raise Halt("Already integrated, but explicit post-merge audit did not finish; further merges stopped")

    def preflight(self) -> str:
        base = self.api.head("main")
        self.graph.fetch(base)
        self.graph.fetch(self.controller_sha)
        changed = self.graph.paths(self.controller_sha, base)
        if any(path == root or path.startswith(root + "/") for path in changed for root in CONTROL_PATHS):
            raise Halt("Repository controls changed since this workflow started; run the current workflow")
        if not self.preview:
            if self.api.request("GET", "/user").get("login") != OWNER:
                raise Halt("NIGHTLY_INTEGRATION_TOKEN must authenticate the repository owner")
            self.method = protection_method(self.api.request("GET", "branches/main/protection"), self.api.request("GET", ""))
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
        if not scoped_paths(branch, self.graph.paths(base, source, triple=True)):
            raise Blocked("Branch delta exceeds its analytical root and seven allowed shared files")
        self.candidate_pr(branch)
        status = self.api.status(source)
        if not status or status["state"] not in {"success", "pending"} or not self.api.audit_run(source, status):
            raise Blocked("Source has no successful authored-content or full audit run")
        tree = self.graph.merge_tree(source, base)
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
            self.same_heads(branch, source, base)
            try:
                self.graph.push(branch, reconciled, self.api.token)
            except GitError:
                observed = self.api.head(branch)
                if observed != reconciled and not self.generated_child(reconciled, observed):
                    raise
            row["reconciled_sha"] = reconciled
            source = reconciled
        final = self.wait_final(branch, source, base)
        self.graph.fetch(final)
        if not self.graph.ancestor(base, final) or not scoped_paths(branch, self.graph.paths(base, final)):
            raise Blocked("Final branch no longer incorporates main within the allowed path boundary")
        self.same_heads(branch, final, base)
        pr = self.candidate_pr(branch)
        if pr is None:
            pr = self.api.request("POST", "pulls", {
                "title": "Integrate " + branch, "head": branch, "base": "main",
                "body": "Nightly integration of an audited analytical branch. The controller rechecks the exact head, preserves branch protections, and explicitly audits the resulting main commit.",
            })
        row.update(pr=pr["number"], final_source_sha=final)
        pr = self.api.request("GET", f"pulls/{pr['number']}")
        self.allowed_pr(pr)
        if pr["head"]["sha"] != final:
            raise Blocked("PR head changed before merge")
        self.same_heads(branch, final, base)
        # Strict admin-enforced protection closes the base race the REST SHA cannot.
        method = protection_method(self.api.request("GET", "branches/main/protection"), self.api.request("GET", ""))
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
        try:
            result = self.api.request("PUT", f"pulls/{pr['number']}/merge", {"sha": final, "merge_method": self.method})
        except (ApiError, OSError):
            observed_pr = self.api.request("GET", f"pulls/{pr['number']}")
            if not observed_pr.get("merged"):
                raise Blocked("Merge was not confirmed; no mutation retry was issued") from None
            result = {"merged": True, "sha": observed_pr["merge_commit_sha"]}
        if not result.get("merged"):
            raise Blocked("GitHub did not confirm a protected merge")
        merged = exact_sha(result["sha"])
        row.update(outcome="integrated_unverified", integration_sha=merged)
        self.save()
        self.graph.fetch(merged)
        if self.graph.tree(merged) != self.graph.tree(final):
            raise Halt("Already integrated, but the resulting tree differs from the audited source")
        previous = self.api.status(merged)
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
        report = json.dumps({"preview": self.preview, "branches": self.rows}, indent=2) + "\n"
        Path("nightly-integration-report.json").write_text(report, encoding="utf-8")
        summary = os.environ.get("GITHUB_STEP_SUMMARY")
        if summary:
            Path(summary).write_text("Nightly analytical integration - " + ("preview" if self.preview else "apply") + "\n\n```json\n" + report + "```\n", encoding="utf-8")
        if self.rows:
            print(json.dumps(self.rows[-1]), flush=True)

    def run(self, selected: str = "") -> None:
        if selected and not BRANCH.fullmatch(selected):
            raise Halt("The selected branch must be an exact stable series/study branch")
        base = self.preflight()
        branches = sorted((item["name"], item["commit"]["sha"]) for item in self.api.pages("branches")
                          if BRANCH.fullmatch(item["name"]) and (not selected or item["name"] == selected))
        if selected and not branches:
            raise Halt("The selected branch does not exist")
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


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--mode", choices=("preview", "apply"), default="preview")
    parser.add_argument("--branch", default="")
    args = parser.parse_args()
    preview = args.mode == "preview"
    if os.environ.get("GITHUB_REPOSITORY", REPOSITORY) != REPOSITORY:
        parser.error("Unexpected repository")
    if not preview and (os.environ.get("GITHUB_REF") != "refs/heads/main" or os.environ.get("GITHUB_ACTIONS") != "true"):
        parser.error("Apply is only supported by the trusted default-branch Actions workflow")
    token = os.environ.get("READ_TOKEN", "") if preview else os.environ.get("OWNER_TOKEN", "")
    if not preview and not token:
        parser.error("Configure NIGHTLY_INTEGRATION_TOKEN before enabling integration")
    controller_sha = os.environ.get("GITHUB_SHA") or subprocess.check_output(["git", "rev-parse", "HEAD"], text=True).strip()
    result = 0
    with tempfile.TemporaryDirectory(prefix="nightly-integration-") as temporary:
        worker = Integrator(GitHub(token, preview=preview), Graph(Path(temporary)), preview=preview, controller_sha=controller_sha)
        try:
            worker.run(args.branch)
            if not preview and any(row["outcome"] == "blocked" for row in worker.rows):
                result = 1
        except (Halt, Blocked, ApiError, OSError, ValueError, KeyError) as exc:
            worker.rows.append({"branch": "run", "outcome": "halted", "detail": str(exc)})
            result = 1
        finally:
            worker.save()
            report = Path("nightly-integration-report.json").read_text(encoding="utf-8")
            print(report)

    return result


if __name__ == "__main__":
    raise SystemExit(main())
