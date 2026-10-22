#!/usr/bin/env python3
"""Fail-closed validation for historical G3 and the Character Index v2 candidate."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import shlex
import unicodedata
from pathlib import Path, PurePosixPath
from typing import Any, Mapping
from urllib.parse import unquote_to_bytes

from character_index_core import (
    RECONSTRUCTION_INDEX_PATH,
    RECONSTRUCTION_POLICY_PATH,
    RECONSTRUCTION_REGISTRY_PATH,
    RECONSTRUCTION_SCHEMA_PATH,
    AuthorityGraph,
    DomainError,
    _restricted_yaml_load,
    GitSnapshot,
    decode_json,
    decode_jsonl_with_lines,
    decode_reconstruction_registry,
    evaluate_reconstruction_assessments,
    is_ancestor_commit,
    load_reconstruction_policy,
    reconstruction_registry_changes,
    render_schema_diagnostics,
    run_git,
    schema_diagnostics,
    validate_discovery_records,
    validate_repository_path,
    validate_schema_document,
)
from generate_character_index import render as render_character_index
from generate_reconstruction_index import render as render_reconstruction_index
from completed_run_publication import CompletionProof, PROOF_NAME
from audit_timing import AuditTimer, report_path, write_report
from frozen_publication import frozen_publication_paths, publication_grants
from update_repository_indexes import ROUTING_OUTPUTS, expected_outputs


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
# Exact prefilters for the hazard patterns above: every match of a pattern
# contains at least one of its literal needles (in ASCII-lowercased bytes when
# the second field is true, which is how bytes IGNORECASE matching folds case).
# A file without any needle cannot match, so its regex search is skipped. A
# pattern without an entry is always searched.
HAZARD_PREFILTERS: dict[str, tuple[tuple[bytes, ...], bool]] = {
    "GitHub token": ((b"ghp_", b"gho_", b"ghu_", b"ghs_", b"ghr_"), False),
    "AWS access key": ((b"AKIA",), False),
    "Google API key": ((b"AIza",), False),
    # Split literals keep this table from matching the pattern it filters.
    "Google Drive URL": ((b"https://drive" b".google.com", b"https://docs" b".google.com"), True),
    "local absolute path": ((b":/", b":\\"), False),
    "personal email address": (
        (b"@gmail.", b"@googlemail.", b"@outlook.", b"@hotmail.", b"@yahoo."),
        True,
    ),
}
MARKDOWN_LINK = re.compile(r"\[[^\]]*\]\(([^)]+)\)")
G3_MANIFEST = "governance/repository-controls/G3_BOOTSTRAP_TRACKED_PATHS.txt"
G3_BOUND_COMMIT = "e934c0a6f92ad16ba3305bd99f938aa6b3d97a1f"
G3_BOUND_TREE = "d0bb00fa5d7a8735892921ba3c0023b4855ac52e"
PROTECTED_HASHES = {
    G3_MANIFEST: "75c6fe48adc719090828a2da02f3dc69e2334b8b20ee5f1c89e0f4c33ee6d191",
    "governance/repository-controls/bootstrap-bindings.json": "7ebb26e4cff22acbabe72905847f6efbbb6885c4a6be0b9e5297db22d654ae17",
}
# The evaluator's ordinary production delta. Any other path changed beside
# these requires a reviewed amendment that also changes the publication gate.
RECONSTRUCTION_OUTPUTS = frozenset({RECONSTRUCTION_REGISTRY_PATH, RECONSTRUCTION_INDEX_PATH})
# The curation agent's ordinary delta on its continuing branch.
DISCOVERY_BRANCH_REF = "refs/remotes/origin/character-registry"
DISCOVERY_OUTPUTS = frozenset({"characters/registry.jsonl", "CHARACTER_ANALYSIS_INDEX.md"})
NATIVE_SHEET_SCHEMA = "governance/schemas/native-sheet-structure.schema.json"
NATIVE_SHEET_SCHEMA_ID = "manga-anime-git-migration/native-sheet-structure/v1"
NATIVE_SHEET_TRANSFORMATION = (
    "GOOGLE_SHEET_VERIFIED_XLSX_TO_TSV_PACKAGE_V2_BLANK_PRESERVING"
)
NATIVE_SHEET_REFERENCE_TRANSFORMATION = "GOOGLE_SHEET_NATIVE_XLSX_REFERENCE_V1"
CROSSWALK_FILES = {
    "mapping": "crosswalk/drive-to-git.jsonl",
    "results": "crosswalk/materialization-results.jsonl",
    "plan": "crosswalk/path-plan.jsonl",
}
SHA256_RE = re.compile(r"^[0-9a-f]{64}$")
REPRESENTATION_ID_RE = re.compile(r"^repr-[0-9a-f]{24}$")
POSITIVE_DECIMAL_RE = re.compile(r"^[1-9][0-9]*$")
EXCEL_RANGE_RE = re.compile(r"^A1:([A-Z]+)([1-9][0-9]*)$")
SERIES_REGISTRY_PATH = "series/registry.json"
SERIES_REGISTRY_SCHEMA = "anime-manga-ln-games-analysis/series-registry/v2"
SERIES_ENTRYPOINT_STATUSES = {"PRESENT_VERIFIED", "MISSING"}
STUDY_REGISTRY_PATH = "studies/registry.json"
STUDY_REGISTRY_SCHEMA = "anime-manga-ln-games-analysis/study-registry/v1"
CHANGE_OBLIGATIONS_PATH = "governance/repository-controls/change-obligations.json"
CHANGE_OBLIGATIONS_SCHEMA = "anime-manga-ln-games-analysis/change-obligations/v1"
PROJECT_INITIATION_GATE_PATH = (
    "governance/repository-controls/project-initiation-gate.json"
)
PROJECT_INITIATION_GATE_SCHEMA = (
    "anime-manga-ln-games-analysis/project-initiation-gate/v1"
)
PROJECT_INITIATION_BASELINE = "2eec12ae1200d3aaaff3f754fd535808161226f8"
AUDIT_WORKFLOW_PATH = ".github/workflows/repository-audit.yml"
AUDIT_COMMIT_EXPRESSION = (
    "${{ github.event_name == 'repository_dispatch' && github.event.client_payload.commit_sha || github.sha }}"
)
HOUSEKEEPING_WORKFLOW_PATH = ".github/workflows/global-index-housekeeping.yml"
NIGHTLY_WORKFLOW_PATH = ".github/workflows/nightly-integration.yml"
GLOBAL_AUTOMATION_WRITE_PATHS = set(ROUTING_OUTPUTS)
DJFW_TSV_WHITESPACE_ATTRIBUTE_RULE = (
    '"studies/doujinshi-fanwork-comparative-taxonomy/01 Project Registry and '
    'Source Lock/DJFW_PROJECT_CONTROL_SHEET.tabs/*.tsv" whitespace=-blank-at-eol'
)
WHITESPACE_ATTRIBUTE_TOKEN_RE = re.compile(
    r"(?:^|[ \t])(?:whitespace(?:=[^ \t]+)?|-whitespace|!whitespace)(?=$|[ \t])"
)


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
    allowed_workflows = set(policy.get("allowed_workflows", []))
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
        if path.startswith(".github/workflows/") and path not in allowed_workflows:
            errors.append(f"workflow is outside the exact allowlist: {path}")
        if entry.mode != "100644":
            errors.append(f"non-regular or executable Git mode {entry.mode!r}: {path}")
    for path in sorted(allowed_workflows):
        if snapshot.get(path) is None:
            errors.append(f"allowlisted workflow is missing: {path}")
    return errors


def validate_audit_workflow(
    snapshot: GitSnapshot, policy: Mapping[str, Any]
) -> list[str]:
    """Enforce content-read-only validation and an isolated exact-status reporter."""

    expected = {AUDIT_WORKFLOW_PATH, HOUSEKEEPING_WORKFLOW_PATH, NIGHTLY_WORKFLOW_PATH}
    declared = set(policy.get("allowed_workflows", []))
    errors: list[str] = []
    if declared != expected:
        errors.append(
            "allowed_workflows must contain only the repository audit, global index housekeeper, and nightly integrator"
        )
    entry = snapshot.get(AUDIT_WORKFLOW_PATH)
    if entry is None:
        return ["approved repository-audit workflow is missing"]
    try:
        text = entry.data.decode("utf-8", "strict")
    except UnicodeDecodeError as exc:
        return [f"repository-audit workflow is not UTF-8: {exc}"]

    required_fragments = (
        "name: Repository audit",
        "  push:",
        "      - main",
        "      - character-registry",
        "      - character-reconstruction",
        '      - "codex/**"',
        '      - "chatgpt/**"',
        '      - "claude/**"',
        '      - "agent/**"',
        '      - "series/**"',
        '      - "studies/**"',
        "  repository_dispatch:",
        "      - audit-generated-commit",
        '    - cron: "17 6 * * 0"',
        "  workflow_dispatch:",
        "permissions:\n  contents: read",
        "runs-on: ubuntu-24.04",
        'MANGA_ANIME_TEST_TMP: "${{ runner.temp }}/manga-anime-tests"',
        'AUDIT_COMMIT: ${{ github.event_name == \'repository_dispatch\' && github.event.client_payload.commit_sha || github.sha }}',
        'git fetch --no-tags origin "${AUDIT_COMMIT}"',
        "if git ls-remote --exit-code --heads origin character-registry > /dev/null; then",
        "git fetch --no-tags origin refs/heads/character-registry:refs/remotes/origin/character-registry",
        'test "${status}" -eq 2',
        'test "$(git rev-parse --is-shallow-repository)" = "false"',
        "--require-hashes",
        "tools/validate_repository.py",
        'audit_args+=(--routing-preflight "${AUDIT_BRANCH}")',
        'if [[ "${AUDIT_BRANCH}" = "character-registry" && "${AUDIT_EVENT}" != "repository_dispatch" ]]; then',
        "audit_args+=(--discovery-branch-confinement)",
        'steps.validate.outputs.integration_state',
        'mkdir -p "${MANGA_ANIME_TEST_TMP}"',
        'python tools/audit_execution.py --snapshot commit --commit "${AUDIT_COMMIT}" --report-json "${RUNNER_TEMP}/test-timings.json"',
        '--timings-json "${RUNNER_TEMP}/audit-timings.json"',
    )
    for fragment in required_fragments:
        if fragment not in text:
            errors.append(f"repository-audit workflow missing required contract: {fragment}")

    # Only the isolated reporter receives write permission. It has no checkout
    # or candidate-code execution and publishes one exact audit-status context.
    try:
        workflow = _restricted_yaml_load(
            re.sub(r"(?m)^on:", '"on":', text), AUDIT_WORKFLOW_PATH
        )
        if not isinstance(workflow, Mapping) or workflow.get("permissions") != {"contents": "read"}:
            errors.append("audit validation must retain read-only contents permission")
        jobs = workflow.get("jobs", {}) if isinstance(workflow, Mapping) else {}
        if not isinstance(jobs, Mapping) or set(jobs) != {"audit", "report"}:
            errors.append("audit jobs must be exactly validation and isolated status reporting")
            jobs = {}
        audit_job = jobs.get("audit", {})
        if not isinstance(audit_job, Mapping) or audit_job.get(
            "permissions", {"contents": "read"}
        ) != {"contents": "read"}:
            errors.append("audit validation job must not receive write permissions")
        if isinstance(audit_job, Mapping) and (
            "uses" in audit_job or any(
                isinstance(step, Mapping) and "uses" in step
                for step in audit_job.get("steps", [])
            )
        ):
            errors.append("repository-audit workflow contains prohibited capability: uses:")
        report = jobs.get("report", {})
        steps = report.get("steps", []) if isinstance(report, Mapping) else []
        step = steps[0] if isinstance(steps, list) and len(steps) == 1 else None
        if (
            not isinstance(report, Mapping)
            or report.get("needs") != "audit"
            or report.get("permissions") != {"statuses": "write"}
            or "uses" in report
            or not isinstance(step, Mapping)
            or "uses" in step
            or step.get("env", {}).get("AUDIT_COMMIT") != AUDIT_COMMIT_EXPRESSION
            or "/statuses/{sha}" not in str(step.get("run", ""))
        ):
            errors.append(
                "audit status reporter must be one step with statuses: write only, "
                "reporting the exact audited commit"
            )
    except (DomainError, AttributeError, TypeError, ValueError) as exc:
        errors.append(f"invalid audit permission/reporting contract: {exc}")

    whitespace_command = 'git show --check --format= "${AUDIT_COMMIT}" -- . \\'
    markdown_whitespace_exclusion = "':(top,glob,exclude)**/*.md'"
    idoly_whitespace_exclusion = (
        "':(top,literal,exclude)series/idoly-pride/V2 Analysis/02 Source Audits and "
        "Longitudinal Ledgers/02.01 Corpus Coverage and Priority Ledger/"
        "IDOLY_PRIDE_V2_SOURCE_TO_BUNDLE_PROVENANCE.csv'"
    )
    workflow_lines = text.splitlines()
    command_lines = [
        index
        for index, line in enumerate(workflow_lines)
        if line.strip().startswith("git show --check")
    ]
    exclusion_lines = [
        line.strip()
        for line in workflow_lines
        if ":(" in line and "exclude" in line
    ]
    exact_whitespace_shape = bool(
        len(command_lines) == 1
        and workflow_lines[command_lines[0]].strip() == whitespace_command
        and command_lines[0] + 2 < len(workflow_lines)
        and workflow_lines[command_lines[0] + 1].strip()
        == markdown_whitespace_exclusion + " \\"
        and workflow_lines[command_lines[0] + 2].strip() == idoly_whitespace_exclusion
        and exclusion_lines
        == [markdown_whitespace_exclusion + " \\", idoly_whitespace_exclusion]
    )
    if not exact_whitespace_shape:
        errors.append(
            "repository-audit workflow whitespace check must use only the exact approved "
            "Markdown glob and IDOLY PRIDE provenance CSV exclusions"
        )

    forbidden_fragments = (
        "pull_request",
        "secrets.",
        "contents: write",
        "permissions: write",
        "git push",
        "git commit",
        "git tag",
        "actions/upload-artifact",
        "GITHUB_TOKEN",
        "gh ",
        "--depth",
        "--deepen",
        "--shallow-exclude",
        "--shallow-since",
    )
    for fragment in forbidden_fragments:
        if fragment in text:
            errors.append(f"repository-audit workflow contains prohibited capability: {fragment}")
    return errors


def validate_global_index_automation(
    snapshot: GitSnapshot, policy: Mapping[str, Any]
) -> list[str]:
    """Keep housekeeping to owner audits of analysis branches and the five routing outputs."""

    errors: list[str] = []
    workflow_entry = snapshot.get(HOUSEKEEPING_WORKFLOW_PATH)
    if workflow_entry is None or workflow_entry.mode != "100644":
        return ["approved global index housekeeping workflow is missing"]
    try:
        text = workflow_entry.data.decode("utf-8", "strict")
        workflow = _restricted_yaml_load(
            re.sub(r"(?m)^on:", '"on":', text), HOUSEKEEPING_WORKFLOW_PATH
        )
    except (UnicodeDecodeError, DomainError, TypeError, ValueError) as exc:
        return [f"invalid global index housekeeping workflow: {exc}"]
    if not isinstance(workflow, Mapping):
        return ["global index housekeeping workflow must be a mapping"]
    if workflow.get("on") != {"workflow_run": {
        "workflows": ["Repository audit"], "types": ["completed"],
        "branches": ["series/**", "studies/**"],
    }}:
        errors.append("housekeeping must run only after Repository audit completes on series/study branches")
    if workflow.get("permissions") != {"contents": "write"}:
        errors.append("housekeeping token must have contents: write only")
    jobs = workflow.get("jobs", {})
    if not isinstance(jobs, Mapping) or any(
        not isinstance(job, Mapping) or "permissions" in job or "uses" in job
        for job in jobs.values()
    ):
        errors.append("housekeeping jobs may not widen permissions or call reusable workflows")
    for fragment in (
        "github.event.workflow_run.event == 'push'",
        "github.event.workflow_run.conclusion == 'success'",
        "github.event.workflow_run.actor.login == github.repository_owner",
        "git merge-base --is-ancestor origin/main HEAD",
    ):
        if fragment not in text:
            errors.append(f"global index housekeeping workflow missing contract: {fragment}")
    # Branches may carry coordinated character repairs, but the generated and
    # staged output set must remain the five routing paths.
    output_blocks = re.findall(
        r"readonly generated_paths=\((.*?)\)", text, flags=re.DOTALL
    )
    try:
        generated_paths = shlex.split(output_blocks[0]) if len(output_blocks) == 1 else []
        staged_paths: list[str] = []
        for line in text.splitlines():
            if line.strip().startswith("git add"):
                command = shlex.split(line.strip())
                if command[:3] != ["git", "add", "--"]:
                    raise ValueError("staging must use exact paths after git add --")
                staged_paths.extend(command[3:])
        if (
            len(generated_paths) != len(GLOBAL_AUTOMATION_WRITE_PATHS)
            or set(generated_paths) != GLOBAL_AUTOMATION_WRITE_PATHS
        ):
            errors.append("housekeeping generated paths must be exactly the five routing outputs")
        if set(staged_paths) != GLOBAL_AUTOMATION_WRITE_PATHS:
            errors.append("housekeeping staging must contain only the five routing outputs")
    except ValueError as exc:
        errors.append(f"invalid housekeeping output/staging contract: {exc}")
    forbidden_fragments = (
        "tools/generate_character_index.py",
        "uses:",
        "secrets.",
        "pull_request",
        "issues: write",
        "pull-requests: write",
        "actions: write",
        "git push --force",
        "--force-with-lease",
        "git reset",
        "git clean",
        "git tag",
        "git branch -D",
        "refs/heads/main\"",
        "actions/upload-artifact",
    )
    for fragment in forbidden_fragments:
        if fragment in text:
            errors.append(f"global index housekeeping workflow contains prohibited capability: {fragment}")
    declared = set(policy.get("allowed_workflows", []))
    if declared != {AUDIT_WORKFLOW_PATH, HOUSEKEEPING_WORKFLOW_PATH, NIGHTLY_WORKFLOW_PATH}:
        errors.append("global index automation workflow inventory is not exact")
    return errors


def validate_nightly_integration(snapshot: GitSnapshot) -> list[str]:
    """Keep the bulk-merge workflow manual-only, read-only and limited to the merge script."""
    errors: list[str] = []
    for path in (NIGHTLY_WORKFLOW_PATH, "tools/nightly_integration.py"):
        candidate = snapshot.get(path)
        if candidate is None or candidate.mode != "100644":
            errors.append(f"nightly integration file is missing or not a regular file: {path}")
    try:
        candidate = snapshot.get(NIGHTLY_WORKFLOW_PATH)
        if candidate is None:
            return errors
        text = candidate.data.decode("utf-8", "strict")
        workflow = _restricted_yaml_load(text.replace("\non:", '\n"on":'), NIGHTLY_WORKFLOW_PATH)
        if set(workflow) != {"name", "on", "permissions", "concurrency", "jobs"}:
            errors.append("nightly integration workflow envelope is not exact")
        if set(workflow.get("on", {})) != {"workflow_dispatch"}:
            errors.append("bulk-merge workflow must be manual-only; scheduled apply is prohibited")
        if workflow.get("permissions") != {"contents": "read", "actions": "read", "statuses": "read", "pull-requests": "read"}:
            errors.append("nightly integration repository token must remain read-only")
        if workflow.get("concurrency") != {"group": "nightly-analytical-integration", "cancel-in-progress": False}:
            errors.append("nightly integration must be serialized without cancellation")
        jobs = workflow.get("jobs", {})
        if set(jobs) != {"integrate"}:
            errors.append("nightly integration may contain only its trusted controller job")
        job = jobs.get("integrate", {})
        expected_if = "github.repository == 'deep-blue-zero/anime-manga-ln-games-analysis' && github.ref == 'refs/heads/main' && github.event_name == 'workflow_dispatch' && github.actor == 'deep-blue-zero'"
        if job.get("if") != expected_if or job.get("runs-on") != "ubuntu-24.04" or job.get("timeout-minutes") != 180:
            errors.append("nightly integration repository, branch, runner, or timeout guard differs")
        if "permissions" in job or "uses" in job or "environment" in job:
            errors.append("nightly integration job may not widen its execution envelope")
        steps = job.get("steps", [])
        if len(steps) != 2 or any("uses" in step or step.get("shell") != "bash" for step in steps):
            errors.append("nightly integration may only acquire and run the bound controller")
    except (ValueError, TypeError, AttributeError, UnicodeError, DomainError) as exc:
        errors.append(f"invalid nightly integration contract: {exc}")
    return errors


def load_named_text_exceptions(
    policy: Mapping[str, Any], text_extensions: set[str], threshold: int
) -> tuple[dict[str, Mapping[str, Any]], list[str]]:
    """Parse the exact reviewed-text tuples without granting a path-wide capability."""

    raw = policy.get("named_text_exceptions", [])
    if not isinstance(raw, list):
        return {}, ["named_text_exceptions must be a list"]

    required_fields = {
        "path",
        "bytes",
        "sha256",
        "exception_id",
        "allow_utf8_bom",
        "allow_carriage_returns",
        "purpose",
        "rights_basis",
        "review_decision",
        "external_reference_insufficient",
    }
    hard_limit = int(policy["hard_exception_threshold_bytes"])
    exceptions: dict[str, Mapping[str, Any]] = {}
    errors: list[str] = []
    for index, item in enumerate(raw):
        label = f"named_text_exceptions[{index}]"
        if not isinstance(item, Mapping):
            errors.append(f"{label} must be an object")
            continue
        fields = set(item)
        if fields != required_fields:
            errors.append(
                f"{label} field-set mismatch; missing={sorted(required_fields - fields)}, "
                f"extra={sorted(fields - required_fields)}"
            )
            continue

        path = item["path"]
        if not isinstance(path, str):
            errors.append(f"{label}.path must be a string")
            continue
        try:
            validate_repository_path(path)
        except DomainError as exc:
            errors.append(f"{label}.path is invalid: {exc}")
            continue
        if Path(path).suffix.casefold() not in text_extensions:
            errors.append(f"{label}.path is not an allowed text extension: {path}")
        if path in exceptions:
            errors.append(f"duplicate named text exception path: {path}")
            continue

        byte_length = item["bytes"]
        if (
            isinstance(byte_length, bool)
            or not isinstance(byte_length, int)
            or byte_length <= threshold
            or byte_length > hard_limit
        ):
            errors.append(
                f"{label}.bytes must be an integer above the review threshold "
                f"and at or below the hard exception threshold"
            )
        sha256 = item["sha256"]
        if not isinstance(sha256, str) or re.fullmatch(r"[0-9a-f]{64}", sha256) is None:
            errors.append(f"{label}.sha256 must be exactly 64 lowercase hexadecimal characters")
        exception_id = item["exception_id"]
        if (
            not isinstance(exception_id, str)
            or re.fullmatch(r"[A-Z][A-Z0-9_]*", exception_id) is None
        ):
            errors.append(
                f"{label}.exception_id must be an uppercase ASCII identifier"
            )
        for flag in ("allow_utf8_bom", "allow_carriage_returns"):
            if not isinstance(item[flag], bool):
                errors.append(f"{label}.{flag} must be a boolean")
        for field in (
            "purpose",
            "rights_basis",
            "review_decision",
            "external_reference_insufficient",
        ):
            value = item[field]
            if (
                not isinstance(value, str)
                or not value
                or value != value.strip()
                or "\n" in value
                or "\r" in value
            ):
                errors.append(f"{label}.{field} must be a nonempty single-line string")

        # Invalid entries stay non-capable: validation reports their defects and the
        # corresponding artifact receives the ordinary size/normalization checks.
        if not any(error.startswith(label) for error in errors):
            exceptions[path] = item
    return exceptions, errors


def load_named_whitespace_exceptions(
    policy: Mapping[str, Any],
) -> tuple[dict[str, Mapping[str, Any]], list[str]]:
    """Parse exact, byte-bound waivers for intentional Markdown hard breaks."""

    raw = policy.get("named_whitespace_exceptions", [])
    if not isinstance(raw, list):
        return {}, ["named_whitespace_exceptions must be a list"]

    required_fields = {
        "path",
        "bytes",
        "sha256",
        "exception_id",
        "attribute",
        "trailing_ascii_spaces",
        "line_numbers",
        "purpose",
        "review_decision",
    }
    exceptions: dict[str, Mapping[str, Any]] = {}
    errors: list[str] = []
    for index, item in enumerate(raw):
        label = f"named_whitespace_exceptions[{index}]"
        if not isinstance(item, Mapping):
            errors.append(f"{label} must be an object")
            continue
        fields = set(item)
        if fields != required_fields:
            errors.append(
                f"{label} field-set mismatch; missing={sorted(required_fields - fields)}, "
                f"extra={sorted(fields - required_fields)}"
            )
            continue

        path = item["path"]
        if not isinstance(path, str):
            errors.append(f"{label}.path must be a string")
            continue
        try:
            validate_repository_path(path)
        except DomainError as exc:
            errors.append(f"{label}.path is invalid: {exc}")
            continue
        if Path(path).suffix.casefold() != ".md":
            errors.append(f"{label}.path must identify a Markdown artifact")
        if '"' in path:
            errors.append(f"{label}.path cannot contain a double quote")
        if path in exceptions:
            errors.append(f"duplicate named whitespace exception path: {path}")
            continue

        byte_length = item["bytes"]
        if isinstance(byte_length, bool) or not isinstance(byte_length, int) or byte_length <= 0:
            errors.append(f"{label}.bytes must be a positive integer")
        sha256 = item["sha256"]
        if not isinstance(sha256, str) or SHA256_RE.fullmatch(sha256) is None:
            errors.append(f"{label}.sha256 must be exactly 64 lowercase hexadecimal characters")
        exception_id = item["exception_id"]
        if (
            not isinstance(exception_id, str)
            or re.fullmatch(r"[A-Z][A-Z0-9_]*", exception_id) is None
        ):
            errors.append(f"{label}.exception_id must be an uppercase ASCII identifier")
        if item["attribute"] != "whitespace=-blank-at-eol":
            errors.append(
                f"{label}.attribute must equal whitespace=-blank-at-eol"
            )
        if item["trailing_ascii_spaces"] != 2:
            errors.append(f"{label}.trailing_ascii_spaces must equal 2")
        line_numbers = item["line_numbers"]
        if (
            not isinstance(line_numbers, list)
            or not line_numbers
            or any(
                isinstance(value, bool) or not isinstance(value, int) or value <= 0
                for value in line_numbers
            )
            or line_numbers != sorted(set(line_numbers))
        ):
            errors.append(
                f"{label}.line_numbers must be a nonempty sorted unique list of positive integers"
            )
        for field in ("purpose", "review_decision"):
            value = item[field]
            if (
                not isinstance(value, str)
                or not value
                or value != value.strip()
                or "\n" in value
                or "\r" in value
            ):
                errors.append(f"{label}.{field} must be a nonempty single-line string")

        if not any(error.startswith(label) for error in errors):
            exceptions[path] = item
    return exceptions, errors


def validate_named_whitespace_exceptions(
    snapshot: GitSnapshot, policy: Mapping[str, Any]
) -> list[str]:
    """Bind each whitespace waiver to exact bytes, lines, and one Git attribute."""

    exceptions, errors = load_named_whitespace_exceptions(policy)
    attributes_entry = snapshot.get(".gitattributes")
    if attributes_entry is None or attributes_entry.mode != "100644":
        return errors + ["missing regular .gitattributes for whitespace controls"]
    try:
        attributes_text = attributes_entry.data.decode("utf-8", "strict")
    except UnicodeDecodeError as exc:
        return errors + [f".gitattributes is not UTF-8: {exc}"]

    nested_attributes = sorted(
        path
        for path in snapshot.entries
        if path != ".gitattributes" and PurePosixPath(path).name == ".gitattributes"
    )
    if nested_attributes:
        errors.append(
            f"nested .gitattributes files are prohibited: {nested_attributes}"
        )

    active_rules = [
        line
        for line in attributes_text.splitlines()
        if line
        and not line.lstrip().startswith("#")
        and WHITESPACE_ATTRIBUTE_TOKEN_RE.search(line) is not None
    ]
    expected_rules = [DJFW_TSV_WHITESPACE_ATTRIBUTE_RULE]
    expected_rules.extend(
        f'"{path}" {item["attribute"]}'
        for path, item in sorted(exceptions.items(), key=lambda pair: pair[0].encode("utf-8"))
    )
    if active_rules != expected_rules:
        errors.append(
            ".gitattributes whitespace rules must equal the exact approved TSV and "
            "named byte-bound exception set"
        )

    for path, item in sorted(exceptions.items(), key=lambda pair: pair[0].encode("utf-8")):
        entry = snapshot.get(path)
        if entry is None or entry.mode != "100644":
            errors.append(f"unused named whitespace exception: {path}")
            continue
        actual_hash = hashlib.sha256(entry.data).hexdigest()
        if len(entry.data) != item["bytes"] or actual_hash != item["sha256"]:
            errors.append(f"named whitespace exception tuple mismatch: {path}")

        actual_trailing: dict[int, bytes] = {}
        for line_number, line in enumerate(entry.data.split(b"\n"), 1):
            match = re.search(rb"[ \t]+$", line)
            if match is not None:
                actual_trailing[line_number] = match.group(0)
        expected_trailing = {
            line_number: b" " * item["trailing_ascii_spaces"]
            for line_number in item["line_numbers"]
        }
        if actual_trailing != expected_trailing:
            errors.append(
                f"named whitespace exception line-shape mismatch: {path}; "
                f"expected_lines={sorted(expected_trailing)}, "
                f"actual_lines={sorted(actual_trailing)}"
            )
    return errors


def hazard_matches(data: bytes, patterns: Mapping[str, re.Pattern[bytes]]) -> list[str]:
    """Return the labels of hazard patterns found in data, skipping exact non-candidates."""

    found: list[str] = []
    lowered: bytes | None = None
    for label, pattern in patterns.items():
        prefilter = HAZARD_PREFILTERS.get(label)
        if prefilter is not None:
            needles, fold_case = prefilter
            haystack = data
            if fold_case:
                if lowered is None:
                    lowered = data.lower()
                haystack = lowered
            if not any(needle in haystack for needle in needles):
                continue
        if pattern.search(data):
            found.append(label)
    return found


def validate_bytes(snapshot: GitSnapshot, policy: Mapping[str, Any], phase: str) -> list[str]:
    errors: list[str] = []
    threshold = int(policy["review_threshold_bytes"])
    text_extensions = set(policy["allowed_text_extensions"])
    named_exceptions, exception_errors = load_named_text_exceptions(
        policy, text_extensions, threshold
    )
    errors.extend(exception_errors)
    special_text = {".gitattributes", ".gitignore", "CODEOWNERS"}
    for path, entry in snapshot.entries.items():
        data = entry.data
        exception = named_exceptions.get(path)
        exception_matches = bool(
            exception
            and len(data) == exception["bytes"]
            and hashlib.sha256(data).hexdigest() == exception["sha256"]
        )
        if exception is not None and not exception_matches:
            errors.append(f"named text exception tuple mismatch: {path}")
        if len(data) > threshold and not exception_matches:
            errors.append(f"{phase} file exceeds 1 MiB review threshold: {path} ({len(data)} bytes)")
        for label in hazard_matches(data, SECRET_PATTERNS):
            errors.append(f"possible {label} in {path}")
        for label in hazard_matches(data, PUBLICATION_PATTERNS):
            errors.append(f"publication hazard ({label}) in {path}")
        suffix = Path(path).suffix.casefold()
        if suffix in text_extensions or Path(path).name in special_text:
            allow_bom = bool(exception_matches and exception["allow_utf8_bom"])
            allow_carriage_returns = bool(
                exception_matches and exception["allow_carriage_returns"]
            )
            if data.startswith(b"\xef\xbb\xbf") and not allow_bom:
                errors.append(f"UTF-8 BOM prohibited: {path}")
            if b"\r" in data and not allow_carriage_returns:
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
    for path in sorted(named_exceptions, key=lambda item: item.encode("utf-8")):
        if path not in snapshot.entries:
            errors.append(f"unused named text exception: {path}")
    return errors


def validate_markdown_links(snapshot: GitSnapshot) -> list[str]:
    errors: list[str] = []
    paths = set(snapshot.entries)
    folded = {path.casefold(): path for path in paths}
    directories = {
        parent.as_posix()
        for path in paths
        for parent in PurePosixPath(path).parents
        if parent.as_posix() != "."
    }
    folded_directories = {path.casefold(): path for path in directories}
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
            if unsafe or (resolved not in paths and resolved not in directories):
                case_match = folded.get(resolved.casefold()) or folded_directories.get(
                    resolved.casefold()
                )
                if case_match:
                    errors.append(f"case-mismatched Markdown link in {path}: {target} -> {case_match}")
                else:
                    errors.append(f"unresolved Markdown link in {path}: {target}")
    return errors


GITHUB_SERVER_IDENTITY = ("GitHub", "noreply@github.com")


def _identity_set(policy: Mapping[str, Any], field: str, errors: list[str]) -> set[tuple[str, str]]:
    rows = policy.get(field)
    if not isinstance(rows, list) or not rows:
        errors.append(f"{field} must be a nonempty list")
        return set()
    parsed: set[tuple[str, str]] = set()
    valid_rows = 0
    for row in rows:
        if (
            not isinstance(row, Mapping)
            or set(row) != {"name", "email"}
            or not all(isinstance(row[key], str) and row[key] for key in ("name", "email"))
        ):
            errors.append(f"malformed {field} entry: {row!r}")
            continue
        valid_rows += 1
        parsed.add((row["name"], row["email"]))
    if len(parsed) != valid_rows:
        errors.append(f"duplicate identity in {field}")
    return parsed


def commit_identity_policy(
    policy: Mapping[str, Any],
) -> tuple[set[tuple[str, str]], set[tuple[str, str]], list[str]]:
    """Return the allowed author and committer sets and any policy-shape errors.

    Authors and committers are separate roles: the GitHub server identity may
    commit (squash merges) but never author. allowed_commit_identities is kept
    as the compatibility union of the two lists.
    """

    errors: list[str] = []
    authors = _identity_set(policy, "allowed_author_identities", errors)
    committers = _identity_set(policy, "allowed_committer_identities", errors)
    compatibility = _identity_set(policy, "allowed_commit_identities", errors)
    if GITHUB_SERVER_IDENTITY in authors:
        errors.append("GitHub server identity must never be an allowed author")
    if GITHUB_SERVER_IDENTITY not in committers:
        errors.append("GitHub server identity must be an allowed committer")
    if compatibility != authors | committers:
        errors.append(
            "allowed_commit_identities must equal the compatibility union of "
            "allowed_author_identities and allowed_committer_identities"
        )
    return authors, committers, errors


def validate_commit_identities(
    root: Path, policy: Mapping[str, Any], revision: str, *, role_split: bool = True
) -> list[str]:
    """Check every reachable author and committer against the policy.

    The historical G3 policy predates the role split and lists only the
    compatibility set, so G3 validation passes role_split=False.
    """

    if role_split:
        allowed_authors, allowed_committers, errors = commit_identity_policy(policy)
    else:
        errors = []
        allowed_authors = allowed_committers = _identity_set(
            policy, "allowed_commit_identities", errors
        )
    raw = run_git(root, "log", revision, "--format=%an%x1f%ae%x1f%cn%x1f%ce%x1e")
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
        if author not in allowed_authors:
            errors.append(f"disallowed Git author identity: {author[0]} <{author[1]}>")
        if committer not in allowed_committers:
            errors.append(f"disallowed Git committer identity: {committer[0]} <{committer[1]}>")
    return errors


def validate_missing_entrypoint_allowlist(
    snapshot: GitSnapshot, policy: Mapping[str, Any]
) -> list[str]:
    """Bind MISSING series entrypoints to the reviewed allowlist, in both directions."""

    allowed = policy.get("allowed_missing_canonical_entrypoints")
    if (
        not isinstance(allowed, list)
        or any(not isinstance(value, str) or not value for value in allowed)
        or len(allowed) != len(set(allowed))
    ):
        return ["allowed_missing_canonical_entrypoints must be a unique string list"]
    entry = snapshot.get("series/registry.json")
    if entry is None:
        return ["series/registry.json is absent; MISSING entrypoints cannot be checked"]
    try:
        registry = decode_json(entry.data, "series/registry.json")
    except (DomainError, json.JSONDecodeError, UnicodeDecodeError) as exc:
        return [str(exc)]
    rows = registry.get("series", []) if isinstance(registry, Mapping) else []
    errors: list[str] = []
    actual: set[str] = set()
    for row in rows if isinstance(rows, list) else []:
        if not isinstance(row, Mapping) or row.get("canonical_entrypoint_status") != "MISSING":
            continue
        series_id = row.get("series_id")
        if not isinstance(series_id, str) or not series_id:
            errors.append("MISSING series route without series_id")
            continue
        actual.add(series_id)
    if actual != set(allowed):
        errors.append(
            "canonical-entrypoint MISSING set differs from reviewed allowlist; "
            f"allowed={sorted(allowed)}, actual={sorted(actual)}"
        )
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
    return errors


def validate_generated_index(
    snapshot: GitSnapshot, snapshot_kind: str, authority: AuthorityGraph | None = None
) -> list[str]:
    registry = snapshot.get("characters/registry.jsonl")
    output = snapshot.get("CHARACTER_ANALYSIS_INDEX.md")
    if registry is None or output is None:
        return ["character registry or generated index is missing"]
    try:
        records = [
            record
            for _line_number, record in decode_jsonl_with_lines(
                registry.data, f"{snapshot.identity}:characters/registry.jsonl"
            )
        ]
        if snapshot_kind == "worktree" and records:
            return [
                "worktree bytes cannot establish materialization; use an exact Git index or commit snapshot"
            ]
        graph = authority if authority is not None else AuthorityGraph(snapshot)
        rendered = render_character_index(records, graph).encode("utf-8")
    except (DomainError, UnicodeDecodeError, ValueError) as exc:
        return [f"unable to render character index: {exc}"]
    if output.data != rendered:
        return ["CHARACTER_ANALYSIS_INDEX.md is out of date"]
    return []


def validate_generated_repository_indexes(snapshot: GitSnapshot) -> list[str]:
    try:
        stale = [
            path for path, expected in expected_outputs(snapshot).items()
            if snapshot.get(path) is None
            or snapshot.entries[path].mode != "100644"
            or snapshot.entries[path].data != expected
        ]
        return [f"generated repository indexes are out of date: {stale}"] if stale else []
    except (DomainError, OSError, ValueError) as exc:
        return [str(exc)]


def _policy_from_snapshot(snapshot: GitSnapshot) -> Mapping[str, Any]:
    path = "governance/repository-controls/tracked-file-policy.json"
    entry = snapshot.get(path)
    if entry is None:
        raise DomainError(f"missing policy: {path}")
    value = decode_json(entry.data, path)
    if not isinstance(value, dict):
        raise DomainError(f"policy is not an object: {path}")
    return value


def _snapshot_jsonl(snapshot: GitSnapshot, path: str) -> list[dict[str, Any]]:
    entry = snapshot.get(path)
    if entry is None:
        raise DomainError(f"missing crosswalk path: {path}")
    if not entry.qualifies_as_evidence:
        raise DomainError(
            f"crosswalk must be a tracked regular non-LFS Git blob: {path}"
        )
    return [
        record
        for _line_number, record in decode_jsonl_with_lines(
            entry.data, f"{snapshot.identity}:{path}"
        )
    ]


def _valid_nonempty_string(value: Any) -> bool:
    return (
        isinstance(value, str)
        and bool(value)
        and value == value.strip()
        and "\r" not in value
        and "\n" not in value
    )


def _yaml_front_matter(data: bytes, path: str) -> Mapping[str, Any] | None:
    """Return generic restricted YAML front matter without classifying authority."""

    if not data.startswith(b"---\n"):
        return None
    if b"\r" in data:
        raise DomainError(f"{path}: recognized YAML artifact must be LF-only")
    try:
        text = data.decode("utf-8", "strict")
    except UnicodeDecodeError as exc:
        raise DomainError(f"{path}: invalid UTF-8 front matter") from exc
    lines = text.split("\n")
    closing = next(
        (index for index in range(1, len(lines)) if lines[index] == "---"), None
    )
    if closing is None:
        raise DomainError(f"{path}: unterminated YAML front matter")
    loaded = _restricted_yaml_load("\n".join(lines[1:closing]) + "\n", path)
    if not isinstance(loaded, Mapping):
        raise DomainError(f"{path}: front matter must be one mapping")
    return loaded


def _load_project_initiation_gate(
    snapshot: GitSnapshot,
) -> tuple[Mapping[str, Any] | None, list[str]]:
    entry = snapshot.get(PROJECT_INITIATION_GATE_PATH)
    if entry is None or not entry.qualifies_as_evidence:
        return None, [
            f"missing tracked regular project-initiation control: "
            f"{PROJECT_INITIATION_GATE_PATH}"
        ]
    try:
        control = decode_json(entry.data, PROJECT_INITIATION_GATE_PATH)
    except (DomainError, json.JSONDecodeError, UnicodeDecodeError) as exc:
        return None, [str(exc)]
    if not isinstance(control, Mapping):
        return None, [f"{PROJECT_INITIATION_GATE_PATH} must be a JSON object"]

    errors: list[str] = []
    if control.get("schema") != PROJECT_INITIATION_GATE_SCHEMA:
        errors.append(
            f"{PROJECT_INITIATION_GATE_PATH}.schema must equal "
            f"{PROJECT_INITIATION_GATE_SCHEMA!r}"
        )
    policy = control.get("governing_policy")
    if not _valid_nonempty_string(policy):
        errors.append(
            f"{PROJECT_INITIATION_GATE_PATH}.governing_policy must be a nonempty path"
        )
    else:
        try:
            validate_repository_path(policy)
        except DomainError as exc:
            errors.append(
                f"{PROJECT_INITIATION_GATE_PATH}.governing_policy is invalid: {exc}"
            )
        target = snapshot.get(policy)
        if target is None or not target.qualifies_as_evidence:
            errors.append(
                f"project-initiation governing policy is not tracked regular: {policy}"
            )
    baseline = control.get("activation_baseline_commit")
    if not isinstance(baseline, str) or re.fullmatch(r"[0-9a-f]{40}", baseline) is None:
        errors.append(
            f"{PROJECT_INITIATION_GATE_PATH}.activation_baseline_commit must be a "
            "full lowercase SHA-1 commit ID"
        )
    elif baseline != PROJECT_INITIATION_BASELINE:
        errors.append("project-initiation immutable activation baseline changed")

    marker = control.get("prospective_registry_marker")
    if not isinstance(marker, Mapping):
        errors.append(
            f"{PROJECT_INITIATION_GATE_PATH}.prospective_registry_marker must be an object"
        )
    elif marker.get("field") != "project_initiation_gate" or marker.get(
        "required_value"
    ) != "REQUIRED":
        errors.append("project-initiation registry marker contract is invalid")

    compatibility = control.get("legacy_compatibility")
    if not isinstance(compatibility, Mapping):
        errors.append(
            f"{PROJECT_INITIATION_GATE_PATH}.legacy_compatibility must be an object"
        )
    else:
        if compatibility.get("baseline_rule") != "ROOT_PRESENT_AT_ACTIVATION":
            errors.append("project-initiation legacy baseline rule is invalid")
        if not _valid_nonempty_string(
            compatibility.get("git_native_migration_scope_prefix")
        ):
            errors.append("project-initiation Git-native migration prefix is invalid")
        if (
            compatibility.get("new_sequential_work_requires_current_architecture")
            is not True
        ):
            errors.append(
                "project-initiation legacy continuation architecture rule must be true"
            )

    classification = control.get("sequential_artifact_classification")
    if not isinstance(classification, Mapping):
        errors.append(
            f"{PROJECT_INITIATION_GATE_PATH}.sequential_artifact_classification "
            "must be an object"
        )
    else:
        if classification.get("front_matter_field") != "artifact_type":
            errors.append("project-initiation artifact classifier field is invalid")
        for field in (
            "exact_types",
            "suffixes",
            "untyped_fallback_directory_keywords",
        ):
            values = classification.get(field)
            if (
                not isinstance(values, list)
                or not values
                or any(not _valid_nonempty_string(value) for value in values)
                or len(values) != len(set(values))
                or values != sorted(values)
            ):
                errors.append(
                    f"project-initiation artifact classifier {field} must be a "
                    "nonempty sorted unique string array"
                )
    closures = control.get("terminal_closures", {})
    if not isinstance(closures, Mapping):
        errors.append("project-initiation terminal_closures must be an object")
    else:
        for prefix, closure in closures.items():
            label = f"project-initiation terminal_closures[{prefix!r}]"
            if not isinstance(prefix, str) or re.fullmatch(
                r"(?:series|studies)/[a-z0-9][a-z0-9-]*/", prefix
            ) is None:
                errors.append(f"{label}: invalid project root")
                continue
            errors.extend(_closure_record_errors(label, prefix, closure))
    errors.extend(_run_closure_amendments(control)[1])
    errors.extend(publication_grants(control)[1])
    return (None if errors else control), errors


def _run_closure_amendments(
    control: Mapping[str, Any],
) -> tuple[dict[str, dict[str, str]], list[str]]:
    """Owner-merged releases of run-stop seals, keyed by registered project root.

    Each entry is {"authorization": text, "record_sha256": SHA-256 of main's
    run-closure.json bytes, "release": {path: sealed SHA-256}}. The gate reads
    releases from main's control, and a release applies only while main's
    record has exactly those bytes, so it lapses as soon as that record changes.
    """

    label = f"{PROJECT_INITIATION_GATE_PATH}.run_closure_amendments"
    raw = control.get("run_closure_amendments", {})
    if not isinstance(raw, Mapping):
        return {}, [f"{label} must be an object"]
    releases: dict[str, tuple[str, dict[str, str]]] = {}
    errors: list[str] = []
    for prefix, entry in raw.items():
        item = f"{label}[{prefix!r}]"
        try:
            if (
                not isinstance(prefix, str)
                or not prefix.endswith("/")
                or not prefix.startswith(("series/", "studies/"))
            ):
                raise DomainError("not a project root")
            validate_repository_path(prefix[:-1])
        except DomainError:
            errors.append(f"{item}: invalid project root")
            continue
        if (
            not isinstance(entry, Mapping)
            or set(entry) != {"authorization", "record_sha256", "release"}
            or not _valid_nonempty_string(entry["authorization"])
            or not isinstance(entry["record_sha256"], str)
            or SHA256_RE.fullmatch(entry["record_sha256"]) is None
            or not isinstance(entry["release"], Mapping)
            or not entry["release"]
        ):
            errors.append(
                f"{item}: needs a nonempty authorization, the record_sha256 of main's "
                "run-closure.json, and a nonempty release object"
            )
            continue
        released: dict[str, str] = {}
        for sealed_path, digest in entry["release"].items():
            if (
                not isinstance(sealed_path, str)
                or not sealed_path.startswith(prefix)
                or not sealed_path.endswith(".md")
            ):
                errors.append(f"{item}: released path must be Markdown inside its project: {sealed_path!r}")
            elif not isinstance(digest, str) or SHA256_RE.fullmatch(digest) is None:
                errors.append(f"{item}: release must name the sealed SHA-256 of {sealed_path}")
            else:
                released[sealed_path] = digest
        releases[prefix] = (entry["record_sha256"], released)
    return releases, errors


CLOSURE_RECORD_FIELDS = frozenset({
    "canonical_entrypoint", "completion_commit", "frozen_sequential_artifacts",
    "supplemental_execution_required",
})
# A project's own stop at the end of an authorized run. It seals the readings
# like a global terminal closure, lives on the project's branch, and is
# reopened there (state REOPENED keeps the seals) when the owner authorizes
# the next run. The global record is reserved for the final source boundary.
PROJECT_RUN_CLOSURE_NAME = ".repository/run-closure.json"
PROJECT_RUN_CLOSURE_SCHEMA = "anime-manga-ln-games-analysis/project-run-closure/v1"
PROJECT_RUN_CLOSURE_STATES = frozenset({"CLOSED", "REOPENED"})


def _closure_record_errors(label: str, prefix: str, closure: Any) -> list[str]:
    """Shape checks shared by global terminal closures and project run closures."""

    if not isinstance(closure, Mapping) or set(closure) != CLOSURE_RECORD_FIELDS:
        return [f"{label}: invalid terminal closure fields"]
    errors: list[str] = []
    commit = closure["completion_commit"]
    if not isinstance(commit, str) or re.fullmatch(r"[0-9a-f]{40}", commit) is None:
        errors.append(f"{label}: completion_commit must be a full commit ID")
    if not isinstance(closure["supplemental_execution_required"], bool):
        errors.append(f"{label}: supplemental_execution_required must be a boolean")
    frozen = closure["frozen_sequential_artifacts"]
    if not isinstance(frozen, Mapping) or not frozen:
        errors.append(f"{label}: frozen_sequential_artifacts must be a nonempty object")
        return errors
    for path in [closure["canonical_entrypoint"], *frozen]:
        if not isinstance(path, str):
            errors.append(f"{label}: artifact path must be a string")
            continue
        try:
            validate_repository_path(path)
        except DomainError as exc:
            errors.append(f"{label}: invalid artifact path: {exc}")
            continue
        if not path.startswith(prefix) or not path.endswith(".md"):
            errors.append(f"{label}: artifact must be Markdown inside its project: {path}")
    for path, digest in frozen.items():
        if not isinstance(digest, str) or SHA256_RE.fullmatch(digest) is None:
            errors.append(f"{label}: invalid frozen SHA-256 for {path}")
    return errors


# A run stop is written on a project's own branch, so the validator binds it to
# main: the completion commit must already be on main (its readings passed the
# OPEN gate there, and a squash merge keeps it reachable), and every seal in
# main's record must survive unless the owner-merged control amends it.
RUN_CLOSURE_BASE_REF = "refs/remotes/origin/main"
def _run_closure_base_commit(root: Path) -> str | None:
    try:
        return run_git(
            root, "rev-parse", "--verify", "-q", RUN_CLOSURE_BASE_REF + "^{commit}"
        ).decode("ascii").strip()
    except DomainError:
        return None


def _base_run_closure_seals(
    root: Path, base_commit: str
) -> dict[str, tuple[str, dict[str, str]]]:
    """Return {registered root on main: (record SHA-256, {path: digest})} for main's run stops."""

    prefixes: set[str] = set()
    for registry_path, collection in (
        (SERIES_REGISTRY_PATH, "series"),
        (STUDY_REGISTRY_PATH, "studies"),
    ):
        try:
            registry = json.loads(run_git(root, "show", f"{base_commit}:{registry_path}"))
        except (DomainError, json.JSONDecodeError, UnicodeDecodeError):
            continue
        rows = registry.get(collection) if isinstance(registry, Mapping) else None
        for row in rows if isinstance(rows, list) else []:
            prefix = row.get("repository_path") if isinstance(row, Mapping) else None
            if _valid_nonempty_string(prefix) and prefix.endswith("/"):
                prefixes.add(prefix)
    listed = set(
        _git_paths(root, "ls-tree", "-r", "-z", "--name-only", base_commit, "--", "series", "studies")
    )
    seals: dict[str, tuple[str, dict[str, str]]] = {}
    for prefix in sorted(prefixes):
        record_path = prefix + PROJECT_RUN_CLOSURE_NAME
        if record_path not in listed:
            continue
        try:
            data = run_git(root, "show", f"{base_commit}:{record_path}")
            record = json.loads(data)
        except (DomainError, json.JSONDecodeError, UnicodeDecodeError):
            continue  # main failed its own audit; there is nothing valid to carry
        frozen = record.get("frozen_sequential_artifacts") if isinstance(record, Mapping) else None
        if isinstance(frozen, Mapping):
            seals[prefix] = (hashlib.sha256(data).hexdigest(), {
                key: value for key, value in frozen.items()
                if isinstance(key, str) and isinstance(value, str)
            })
    return seals


def _base_run_closure_releases(root: Path, base_commit: str) -> dict[str, tuple[str, dict[str, str]]]:
    """Releases recorded in main's gate control; a candidate's own entries never count."""

    try:
        control = json.loads(run_git(root, "show", f"{base_commit}:{PROJECT_INITIATION_GATE_PATH}"))
    except (DomainError, json.JSONDecodeError, UnicodeDecodeError):
        return {}
    return _run_closure_amendments(control)[0] if isinstance(control, Mapping) else {}


def _run_closure_on_main(
    snapshot: GitSnapshot, prefix: str, record: Mapping[str, Any], base_commit: str | None
) -> list[str]:
    path = prefix + PROJECT_RUN_CLOSURE_NAME
    commit = record["completion_commit"]
    if base_commit is None:
        return [
            f"{path}: verifying completion_commit needs {RUN_CLOSURE_BASE_REF}; fetch main first"
        ]
    try:
        merge_base = run_git(snapshot.root, "merge-base", commit, base_commit).decode("ascii").strip()
    except DomainError as exc:
        return [f"{path}: completion_commit cannot be compared with main: {exc}"]
    if merge_base != commit:
        return [
            f"{path}: completion_commit {commit} is not on main ({RUN_CLOSURE_BASE_REF}); "
            "name the commit on main that integrated the sealed readings"
        ]
    return []


def _load_project_run_closure(
    snapshot: GitSnapshot, prefix: str
) -> tuple[Mapping[str, Any] | None, str | None, list[str]]:
    """Return a project's own run closure record, its state, and any errors."""

    path = prefix + PROJECT_RUN_CLOSURE_NAME
    entry = snapshot.get(path)
    if entry is None:
        return None, None, []
    if not entry.qualifies_as_evidence:
        return None, None, [f"{path}: run closure must be a tracked regular non-LFS blob"]
    try:
        record = decode_json(entry.data, path)
    except (DomainError, json.JSONDecodeError, UnicodeDecodeError) as exc:
        return None, None, [str(exc)]
    if not isinstance(record, Mapping):
        return None, None, [f"{path}: run closure must be a JSON object"]
    errors: list[str] = []
    if record.get("schema") != PROJECT_RUN_CLOSURE_SCHEMA:
        errors.append(f"{path}: run closure schema is not recognized")
    state = record.get("state")
    if state not in PROJECT_RUN_CLOSURE_STATES:
        errors.append(f"{path}: run closure state must be CLOSED or REOPENED")
    body = {key: value for key, value in record.items() if key not in {"schema", "state"}}
    errors.extend(_closure_record_errors(path, prefix, body))
    return (None if errors else body), state, errors


def project_initiation_baseline_paths(
    root: Path, control: Mapping[str, Any]
) -> set[str]:
    baseline = control.get("activation_baseline_commit")
    if baseline != PROJECT_INITIATION_BASELINE:
        raise DomainError("project-initiation immutable activation baseline changed or is unavailable")
    if run_git(root, "cat-file", "-t", baseline).decode("ascii").strip() != "commit":
        raise DomainError("project-initiation activation baseline is not a commit")
    return set(
        _git_paths(root, "ls-tree", "-r", "--name-only", "-z", baseline)
    )


def _is_substantive_sequential_artifact(
    path: str,
    entry: Any,
    classification: Mapping[str, Any],
) -> tuple[bool, bool, list[str]]:
    """Return (classified, used_untyped_fallback, parse_errors)."""

    errors: list[str] = []
    try:
        front = _yaml_front_matter(entry.data, path)
    except DomainError as exc:
        return False, False, [str(exc)]
    artifact_type = front.get("artifact_type") if front is not None else None
    if isinstance(artifact_type, str):
        normalized = artifact_type.casefold()
        exact = classification.get("exact_types", [])
        suffixes = classification.get("suffixes", [])
        return (
            normalized in exact
            or any(normalized.endswith(suffix) for suffix in suffixes),
            False,
            errors,
        )
    if artifact_type is not None:
        errors.append(f"{path}: artifact_type must be a string")
        return False, False, errors
    if PurePosixPath(path).name.casefold() == "readme.md":
        return False, False, errors
    normalized_parts = [
        re.sub(r"[^a-z0-9]+", " ", part.casefold()).strip()
        for part in PurePosixPath(path).parts[:-1]
    ]
    fallback = any(
        keyword in part
        for keyword in classification.get("untyped_fallback_directory_keywords", [])
        for part in normalized_parts
    )
    return fallback, fallback, errors


PROJECT_INITIALIZATION_ALIASES = {
    "method": ("governing_method", "analytical_method", "deep_reading_method"),
    "architecture": (
        "synthesis_architecture",
        "governing_synthesis_architecture",
        "corpus_architecture",
    ),
    "method_status": ("method_status", "governing_method_status"),
    "architecture_status": (
        "architecture_status",
        "synthesis_architecture_status",
    ),
    "infrastructure_initialized": (
        "required_day_one_infrastructure_initialized",
        "required_day_one_ledgers_initialized",
        "required_ledgers_initialized",
    ),
    "infrastructure": (
        "required_day_one_infrastructure",
        "required_day_one_artifacts",
    ),
    "lock": ("sequential_analysis_lock",),
}


def _initialization_yaml_blocks(
    text: str, path: str, *, sections: tuple[str, ...] = ("project_initialization",)
) -> list[tuple[int, Any, str | None]]:
    """Return recognized fenced initialization blocks as (index, value, error).

    A fenced YAML block is an initialization surface only when its top level
    declares ``project_initialization``. The lock reader and the terminal
    closure reader share this recognition so that one entrypoint cannot be
    read differently by two parts of the same gate.
    """

    blocks: list[tuple[int, Any, str | None]] = []
    for index, match in enumerate(
        re.finditer(r"(?ms)^```ya?ml[ \t]*\n(.*?)^```[ \t]*$", text), start=1
    ):
        body = match.group(1)
        if not re.search(r"(?m)^(?:" + "|".join(map(re.escape, sections)) + r")\s*:", body):
            continue
        try:
            loaded = _restricted_yaml_load(
                body if body.endswith("\n") else body + "\n",
                f"{path}:project_initialization_block[{index}]",
            )
        except DomainError as exc:
            blocks.append((index, None, str(exc)))
            continue
        blocks.append((index, loaded, None))
    return blocks


def _project_initialization_state(
    data: bytes, path: str
) -> tuple[dict[str, Any], list[str]]:
    errors: list[str] = []
    mappings: list[Mapping[str, Any]] = []
    try:
        front = _yaml_front_matter(data, path)
    except DomainError as exc:
        return {}, [str(exc)]
    if front is not None:
        nested = front.get("project_initialization")
        if nested is not None:
            if isinstance(nested, Mapping):
                mappings.append(nested)
            else:
                errors.append(f"{path}: project_initialization must be a mapping")
        if any(
            alias in front
            for aliases in PROJECT_INITIALIZATION_ALIASES.values()
            for alias in aliases
        ):
            mappings.append(front)

    try:
        text = data.decode("utf-8", "strict")
    except UnicodeDecodeError as exc:
        return {}, [f"{path}: invalid UTF-8 initialization state: {exc}"]
    for index, loaded, block_error in _initialization_yaml_blocks(text, path):
        if block_error is not None:
            errors.append(block_error)
            continue
        nested = (
            loaded.get("project_initialization")
            if isinstance(loaded, Mapping)
            else None
        )
        if not isinstance(nested, Mapping):
            errors.append(
                f"{path}:project_initialization_block[{index}] must contain one mapping"
            )
        else:
            mappings.append(nested)

    state: dict[str, Any] = {}
    for semantic, aliases in PROJECT_INITIALIZATION_ALIASES.items():
        observed = [
            mapping[alias]
            for mapping in mappings
            for alias in aliases
            if alias in mapping
        ]
        if not observed:
            continue
        if any(value != observed[0] for value in observed[1:]):
            errors.append(
                f"{path}: contradictory project-initialization declarations for {semantic}"
            )
            continue
        state[semantic] = observed[0]
    return state, errors


def _resolve_project_reference(
    snapshot: GitSnapshot,
    project_prefix: str,
    entrypoint_path: str,
    value: Any,
    label: str,
) -> tuple[str | None, list[str]]:
    if not _valid_nonempty_string(value):
        return None, [f"{entrypoint_path}: {label} must be a nonempty path"]
    if "\\" in value or value.startswith(("/", "http://", "https://")):
        return None, [f"{entrypoint_path}: {label} is not a repository-relative path"]

    raw_candidates = []
    if value.startswith(project_prefix):
        raw_candidates.append(value)
    else:
        raw_candidates.extend(
            [
                project_prefix + value,
                (PurePosixPath(entrypoint_path).parent / value).as_posix(),
            ]
        )
    candidates: list[str] = []
    for candidate in raw_candidates:
        try:
            validate_repository_path(candidate)
        except DomainError:
            continue
        if candidate.startswith(project_prefix) and candidate not in candidates:
            candidates.append(candidate)
    direct = [
        candidate
        for candidate in candidates
        if (target := snapshot.get(candidate)) is not None and target.qualifies_as_evidence
    ]
    if not direct and "/" not in value:
        direct = [
            path
            for path, target in snapshot.entries.items()
            if path.startswith(project_prefix)
            and PurePosixPath(path).name == value
            and target.qualifies_as_evidence
        ]
    direct = sorted(set(direct), key=lambda item: item.encode("utf-8"))
    if not direct:
        return None, [
            f"{entrypoint_path}: referenced {label} is missing or not a tracked regular "
            f"Git artifact: {value}"
        ]
    if len(direct) != 1:
        return None, [
            f"{entrypoint_path}: referenced {label} is ambiguous: {value} -> {direct}"
        ]
    return direct[0], []


def _validate_current_reference(
    snapshot: GitSnapshot,
    authority: AuthorityGraph,
    project_prefix: str,
    entrypoint_path: str,
    value: Any,
    label: str,
) -> list[str]:
    resolved, errors = _resolve_project_reference(
        snapshot, project_prefix, entrypoint_path, value, label
    )
    if resolved is not None and not authority.current_eligible(resolved):
        errors.append(
            f"{entrypoint_path}: referenced {label} is not current-eligible: {resolved} "
            f"(classification={authority.classification(resolved)})"
        )
    return errors


def _validate_initialization_contract(
    snapshot: GitSnapshot,
    authority: AuthorityGraph,
    project_prefix: str,
    entrypoint_path: Any,
    *,
    require_open: bool,
    terminal: bool = False,
) -> list[str]:
    if not _valid_nonempty_string(entrypoint_path):
        return [
            f"{project_prefix} project-initiation gate requires a canonical entrypoint"
        ]
    entry = snapshot.get(entrypoint_path)
    if entry is None or not entry.qualifies_as_evidence:
        return [
            f"{project_prefix} project-initiation entrypoint is missing or not tracked "
            f"regular: {entrypoint_path}"
        ]
    errors: list[str] = []
    if not entrypoint_path.startswith(project_prefix):
        errors.append(
            f"{project_prefix} project-initiation entrypoint is outside the project root: "
            f"{entrypoint_path}"
        )
    if not authority.current_eligible(entrypoint_path):
        errors.append(
            f"{entrypoint_path}: project-initiation entrypoint is not current-eligible "
            f"(classification={authority.classification(entrypoint_path)})"
        )
    state, state_errors = _project_initialization_state(entry.data, entrypoint_path)
    errors.extend(state_errors)
    lock = state.get("lock")
    normalized_lock = lock.casefold() if isinstance(lock, str) else None
    if normalized_lock not in {"open", "closed"}:
        errors.append(
            f"{entrypoint_path}: sequential_analysis_lock must be explicitly OPEN or CLOSED"
        )
    if require_open and normalized_lock != "open":
        errors.append(
            f"{entrypoint_path}: substantive sequential analysis requires "
            "sequential_analysis_lock OPEN"
        )
    if terminal and normalized_lock != "closed":
        errors.append(f"{entrypoint_path}: terminal closure requires sequential_analysis_lock CLOSED")

    full_gate_claimed = require_open or normalized_lock == "open" or terminal
    if full_gate_claimed:
        for semantic, label in (
            ("method", "governing analytical method"),
            ("architecture", "governing synthesis architecture"),
        ):
            if semantic not in state:
                errors.append(
                    f"{entrypoint_path}: project_initialization does not identify {label}"
                )
            else:
                errors.extend(
                    _validate_current_reference(
                        snapshot,
                        authority,
                        project_prefix,
                        entrypoint_path,
                        state[semantic],
                        label,
                    )
                )
        current_statuses = {
            "canonical",
            "active_provisional",
            "current",
            "current_eligible",
        }
        for semantic, label in (
            ("method_status", "method status"),
            ("architecture_status", "synthesis-architecture status"),
        ):
            if semantic in state and (
                not isinstance(state[semantic], str)
                or state[semantic].casefold() not in current_statuses
            ):
                errors.append(f"{entrypoint_path}: {label} contradicts the initialized gate")
        if state.get("infrastructure_initialized") is not True:
            errors.append(
                f"{entrypoint_path}: required day-one infrastructure must be explicitly "
                "initialized before sequential analysis"
            )

    infrastructure = state.get("infrastructure")
    if infrastructure is not None:
        if (
            not isinstance(infrastructure, list)
            or any(not _valid_nonempty_string(value) for value in infrastructure)
            or len(infrastructure) != len(set(infrastructure))
        ):
            errors.append(
                f"{entrypoint_path}: required_day_one_infrastructure must be a "
                "unique path list"
            )
        elif state.get("infrastructure_initialized") is True:
            for value in infrastructure:
                _resolved, reference_errors = _resolve_project_reference(
                    snapshot,
                    project_prefix,
                    entrypoint_path,
                    value,
                    "required day-one infrastructure",
                )
                errors.extend(reference_errors)
    return errors


# `complete` is the established closure token; `completed` is the run-state
# vocabulary of the sequential execution scope and continuation policy.
TERMINAL_RUN_STATES = frozenset({"complete", "completed"})
TERMINAL_STATE_SECTIONS = (
    "project_initialization",
    "sequential_execution",
    "supplemental_execution",
)


def _execution_state(data: bytes, path: str) -> tuple[dict[str, Any], list[str]]:
    """Read existing run fields from front matter and independent YAML fences."""
    state, errors = _project_initialization_state(data, path)
    result = {"lock": state["lock"]} if "lock" in state else {}
    try:
        surfaces = [_yaml_front_matter(data, path) or {}]
        for _index, value, error in _initialization_yaml_blocks(
            data.decode("utf-8", "strict"), path,
            sections=("project_initialization", "sequential_execution"),
        ):
            if error:
                errors.append(error)
            elif isinstance(value, Mapping):
                surfaces.append(value)
    except (DomainError, UnicodeDecodeError) as exc:
        return result, errors + [f"{path}: invalid execution state: {exc}"]
    for section, fields in (
        ("project_initialization", ("next_permitted_operation",)),
        ("sequential_execution", ("run_state", "mode", "authorized_start", "terminal_boundary",
                                  "committed_high_water_mark", "next_candidate_operation")),
    ):
        declarations = [s[section] for s in surfaces if section in s]
        if section == "sequential_execution" and declarations:
            result["run_state"] = None  # A partial declaration is not legacy absence.
        if any(not isinstance(s, Mapping) for s in declarations):
            errors.append(f"{path}: {section} must be a mapping wherever declared")
            continue
        for field in fields:
            values = [s[field] for s in declarations if field in s]
            if values:
                result[field] = values[0]
                if any(v != values[0] for v in values[1:]):
                    errors.append(f"{path}: contradictory execution declarations for {field}")
    return result, errors


def _validate_run_admission(
    snapshot: GitSnapshot, entrypoint: str, previous: Any, *, admission: bool, strict: bool
) -> list[str]:
    """Check state consistency, never purport to authenticate owner permission."""
    entry = snapshot.get(entrypoint)
    if entry is None or not entry.qualifies_as_evidence:
        return []  # The architecture gate reports this independently.
    current, errors = _execution_state(entry.data, entrypoint)
    prior, prior_errors = _execution_state(previous.data, entrypoint) if previous else ({}, [])
    lock = current.get("lock")
    lock = lock.casefold() if isinstance(lock, str) else None
    none = lambda v: isinstance(v, str) and re.fullmatch(r"NONE(?:_[A-Z0-9]+)*", v) is not None
    prose_closed = re.search(r"SEQUENTIAL_ANALYSIS_LOCK\s*=\s*CLOSED\b", entry.data.decode("utf-8", "replace"), re.I)
    # Preserve accepted legacy inconsistencies until the operational fields
    # change or a new reading is admitted. Retrospective prose edits are safe.
    if not admission and current == prior and errors == prior_errors:
        return []
    if (not admission and "run_state" not in current and "run_state" not in prior
            and not errors and not prior_errors):
        return []
    if (admission and not strict and "run_state" not in current and "run_state" not in prior
            and not errors and not prior_errors and not prose_closed
            and ("lock" not in current or lock == "open")
            and not none(current.get("next_permitted_operation"))):
        return []  # Mature legacy projects retain their existing architecture route.
    run = current.get("run_state")
    run = run if isinstance(run, str) else None
    candidates = [current.get(k) for k in ("next_permitted_operation", "next_candidate_operation")]
    if run not in {"active", "blocked", "interrupted_pending_recovery", *TERMINAL_RUN_STATES}:
        errors.append(f"{entrypoint}: missing or unrecognized sequential_execution.run_state")
    if run in TERMINAL_RUN_STATES and not all(none(v) for v in candidates):
        errors.append(f"{entrypoint}: completed run requires both next operations NONE")
    if run == "active":
        if lock != "open" or any(not _valid_nonempty_string(v) or none(v) for v in candidates):
            errors.append(f"{entrypoint}: active run requires OPEN lock and both next operations")
        if candidates[0] != candidates[1]:
            errors.append(f"{entrypoint}: active next permitted and candidate operations disagree")
        if current.get("mode") not in ("single_operation", "continuous_sequential") or any(
            not _valid_nonempty_string(current.get(k)) or none(current.get(k))
            for k in ("authorized_start", "terminal_boundary")
        ):
            errors.append(f"{entrypoint}: active run requires mode and recoverable authorized bounds")
        if current.get("mode") == "single_operation" and current.get("authorized_start") != current.get("terminal_boundary"):
            errors.append(f"{entrypoint}: single_operation must have one authorized source unit")
        if current.get("mode") == "single_operation" and candidates[1] != current.get("authorized_start"):
            errors.append(f"{entrypoint}: single_operation next candidate exceeds its authorized unit")
    if admission:
        # The final transaction may close a run already recorded active on main.
        # Its original bounds survive, and the high-water mark reaches the end.
        closing = (
            run in TERMINAL_RUN_STATES and not prior_errors and prior.get("run_state") == "active"
            and isinstance(prior.get("lock"), str) and prior["lock"].casefold() == "open"
            and previous is not None and not re.search(
                r"SEQUENTIAL_ANALYSIS_LOCK\s*=\s*CLOSED\b", previous.data.decode("utf-8", "replace"), re.I
            )
            and prior.get("mode") in ("single_operation", "continuous_sequential")
            and prior.get("next_permitted_operation") == prior.get("next_candidate_operation")
            and _valid_nonempty_string(prior.get("next_candidate_operation"))
            and not none(prior.get("next_candidate_operation"))
            and (prior.get("mode") != "single_operation" or
                 prior.get("authorized_start") == prior.get("terminal_boundary") == prior.get("next_candidate_operation"))
            and all(_valid_nonempty_string(prior.get(k)) and not none(prior[k]) and current.get(k) == prior[k]
                    for k in ("mode", "authorized_start", "terminal_boundary"))
            and current.get("committed_high_water_mark") == current.get("terminal_boundary")
        )
        if run != "active" and not closing:
            errors.append(f"{entrypoint}: new sequential admission requires an active authorized run; OPEN alone is insufficient")
        if lock != "open":
            errors.append(f"{entrypoint}: new sequential admission requires sequential_analysis_lock OPEN")
        if prose_closed:
            errors.append(f"{entrypoint}: new sequential admission contradicts prose lock CLOSED")
    return errors


def _completed_publication_previous(
    snapshot: GitSnapshot, prefix: str, entrypoint: str, classification: Mapping[str, Any]
) -> tuple[Any, list[str]]:
    """Recover an exact historical completion without trusting a mutable label."""
    path = prefix + PROOF_NAME
    proof_entry = snapshot.get(path)
    if proof_entry is None:
        return None, []
    try:
        if not proof_entry.qualifies_as_evidence:
            raise DomainError("completion proof must be a regular tracked text blob")
        proof = CompletionProof(decode_json(proof_entry.data, path), prefix, entrypoint)
        completed, active = proof.markdown_snapshot(snapshot, prefix, entrypoint)
        historical = completed.get(entrypoint)
        current = snapshot.get(entrypoint)
        if historical is None or current is None or not historical.qualifies_as_evidence:
            raise DomainError("completion proof has no regular completed entrypoint")
        old_state, old_errors = _execution_state(historical.data, entrypoint)
        new_state, new_errors = _execution_state(current.data, entrypoint)
        if (old_errors or new_errors or old_state != new_state
                or old_state.get("run_state") not in TERMINAL_RUN_STATES):
            raise DomainError("completion proof and current operational state disagree")
        transition = _validate_run_admission(
            completed, entrypoint, active, admission=True, strict=True,
        )
        if transition:
            raise DomainError("completion proof has no valid active-to-completed transition: " + "; ".join(transition))

        def readings(view: GitSnapshot) -> dict[str, bytes]:
            result = {}
            for name, entry in view.entries.items():
                if name.startswith(prefix) and name.endswith(".md"):
                    classified, fallback, failures = _is_substantive_sequential_artifact(
                        name, entry, classification,
                    )
                    if failures or fallback:
                        raise DomainError("completion proof cannot classify historical/current Markdown: " + name)
                    if classified:
                        if not entry.qualifies_as_evidence:
                            raise DomainError("completion proof reading is not a regular blob: " + name)
                        result[name] = entry.data
            return result

        frozen, candidate = readings(completed), readings(snapshot)
        if not frozen or frozen != candidate:
            raise DomainError("completion proof reading set or bytes differ from the completed snapshot")
        return active, []
    except (DomainError, UnicodeError, ValueError, TypeError) as exc:
        return None, [f"{path}: invalid completed-run publication proof: {exc}"]


def _validate_sealed_readings(
    snapshot: GitSnapshot,
    entrypoint_path: str,
    closure: Mapping[str, Any],
    sequential_paths: set[str],
    *,
    exact: bool,
) -> list[str]:
    """Check sealed reading bytes against the completion commit and the candidate.

    exact=True (a closed lock) also requires the sealed set to be the whole
    sequential corpus; a reopened run may add readings but keeps every seal.
    """

    errors: list[str] = []
    if entrypoint_path != closure["canonical_entrypoint"]:
        errors.append(f"{entrypoint_path}: terminal closure canonical entrypoint changed")
    frozen = closure["frozen_sequential_artifacts"]
    # Use immutable local Git objects, independent of HEAD and the candidate
    # index/worktree. Missing history is a failure, never a network lookup or
    # permission to substitute the candidate bytes for the historical seal.
    try:
        completion = GitSnapshot.from_commit(
            snapshot.root, closure["completion_commit"], paths=frozen
        )
    except DomainError as exc:
        errors.append(f"{entrypoint_path}: terminal completion_commit cannot be resolved: {exc}")
    else:
        for path, digest in frozen.items():
            historical = completion.get(path)
            if (
                historical is None
                or not historical.qualifies_as_evidence
                or hashlib.sha256(historical.data).hexdigest() != digest
            ):
                errors.append(
                    f"{path}: terminal frozen seal does not match completion_commit tree"
                )
    if exact and set(frozen) != sequential_paths:
        errors.append(
            f"{entrypoint_path}: terminal sequential corpus differs from reviewed closure "
            f"(added={sorted(sequential_paths - set(frozen))}, "
            f"missing={sorted(set(frozen) - sequential_paths)})"
        )
    elif not exact and set(frozen) - sequential_paths:
        errors.append(
            f"{entrypoint_path}: reopened run closure no longer finds sealed readings "
            f"(missing={sorted(set(frozen) - sequential_paths)})"
        )
    for path, digest in frozen.items():
        entry = snapshot.get(path)
        if (
            entry is None
            or not entry.qualifies_as_evidence
            or hashlib.sha256(entry.data).hexdigest() != digest
        ):
            errors.append(f"{path}: terminal frozen reading bytes changed or are missing")
    return errors


def _validate_terminal_corpus(
    snapshot: GitSnapshot,
    entrypoint_path: str,
    closure: Mapping[str, Any],
    sequential_paths: set[str],
) -> list[str]:
    """Retain only reviewed reading bytes; closure never admits another source."""

    errors = _validate_sealed_readings(
        snapshot, entrypoint_path, closure, sequential_paths, exact=True
    )
    entry = snapshot.get(entrypoint_path)
    if entry is None or not entry.qualifies_as_evidence:
        return errors  # The initialization contract reports the missing entrypoint.
    try:
        front = _yaml_front_matter(entry.data, entrypoint_path) or {}
        text = entry.data.decode("utf-8", "strict")
    except DomainError as exc:
        return errors + [str(exc)]
    except UnicodeDecodeError as exc:
        return errors + [f"{entrypoint_path}: invalid UTF-8 terminal state: {exc}"]
    # Terminal state is read from the same surfaces as the lock: front matter
    # and recognized fenced initialization blocks. Every statement of a field
    # must agree; a non-mapping section or a contradiction fails closed.
    surfaces: list[Mapping[str, Any]] = [front]
    for _index, loaded, block_error in _initialization_yaml_blocks(
        text, entrypoint_path, sections=TERMINAL_STATE_SECTIONS
    ):
        if block_error is not None:
            errors.append(block_error)
        elif isinstance(loaded, Mapping):
            surfaces.append(loaded)
    sections = {
        name: [surface[name] for surface in surfaces if name in surface]
        for name in TERMINAL_STATE_SECTIONS
    }
    problems: list[str] = []

    def declared(section: str, field: str) -> Any:
        values = sections[section]
        if any(not isinstance(value, Mapping) for value in values):
            problems.append(f"terminal {section} must be a mapping wherever declared")
            return None
        stated = [value[field] for value in values if field in value]
        if any(value != stated[0] for value in stated[1:]):
            problems.append(f"contradictory terminal declarations for {section}.{field}")
            return None
        return stated[0] if stated else None

    for section, field in (
        ("project_initialization", "next_permitted_operation"),
        ("sequential_execution", "next_candidate_operation"),
    ):
        value = declared(section, field)
        if not isinstance(value, str) or re.fullmatch(r"NONE(?:_[A-Z0-9]+)*", value) is None:
            errors.append(f"{entrypoint_path}: terminal closure requires {field} NONE")
    run_state = declared("sequential_execution", "run_state")
    if not isinstance(run_state, str) or run_state not in TERMINAL_RUN_STATES:
        errors.append(f"{entrypoint_path}: terminal closure requires run_state complete")
    if closure["supplemental_execution_required"] or sections["supplemental_execution"]:
        current = declared("supplemental_execution", "current_state")
        admission = declared("supplemental_execution", "other_narrative_admission")
        if (
            not sections["supplemental_execution"]
            or not isinstance(current, str)
            or re.fullmatch(r"CLOSED(?:_[A-Z0-9]+)*", current) is None
            or admission != "NOT_AUTHORIZED"
        ):
            errors.append(
                f"{entrypoint_path}: terminal supplemental execution must be CLOSED "
                "with no other admission"
            )
    for problem in dict.fromkeys(problems):
        errors.append(f"{entrypoint_path}: {problem}")
    if re.search(r"SEQUENTIAL_ANALYSIS_LOCK\s*=\s*OPEN\b", text, re.I):
        errors.append(f"{entrypoint_path}: terminal closure contradicts prose lock OPEN")
    return errors


def _entrypoint_mentions(
    entrypoint_text: str, path: str, project_prefix: str
) -> bool:
    relative = path[len(project_prefix) :] if path.startswith(project_prefix) else path
    candidates = {path, relative, PurePosixPath(path).name}
    candidates.update(value.replace(" ", "%20") for value in tuple(candidates))
    return any(value in entrypoint_text for value in candidates)


def _validate_legacy_architecture_route(
    snapshot: GitSnapshot,
    authority: AuthorityGraph,
    project_prefix: str,
    entrypoint_path: Any,
) -> list[str]:
    if not _valid_nonempty_string(entrypoint_path):
        return [
            f"{project_prefix} legacy continuation cannot publish new sequential analysis "
            "without a canonical entrypoint"
        ]
    entry = snapshot.get(entrypoint_path)
    if entry is None or not entry.qualifies_as_evidence:
        return [
            f"{project_prefix} legacy continuation entrypoint is missing or not tracked "
            f"regular: {entrypoint_path}"
        ]
    errors: list[str] = []
    if not authority.current_eligible(entrypoint_path):
        errors.append(
            f"{entrypoint_path}: legacy continuation entrypoint is not current-eligible"
        )
    try:
        text = entry.data.decode("utf-8", "strict")
    except UnicodeDecodeError as exc:
        return errors + [f"{entrypoint_path}: invalid UTF-8: {exc}"]
    method_paths: list[str] = []
    architecture_paths: list[str] = []
    for path, candidate in snapshot.entries.items():
        if (
            not path.startswith(project_prefix)
            or not path.endswith(".md")
            or not candidate.qualifies_as_evidence
            or not authority.current_eligible(path)
            or not _entrypoint_mentions(text, path, project_prefix)
        ):
            continue
        try:
            front = _yaml_front_matter(candidate.data, path)
        except DomainError as exc:
            errors.append(str(exc))
            continue
        artifact_type = front.get("artifact_type") if front is not None else None
        if not isinstance(artifact_type, str):
            continue
        normalized = artifact_type.casefold()
        if normalized.endswith(("_method", "_methodology")) or normalized in {
            "analytical_method",
            "comparative_methodology",
            "governing_method",
            "reading_protocol",
        }:
            method_paths.append(path)
        if normalized.endswith("_architecture") or normalized in {
            "project_architecture",
            "synthesis_architecture",
        }:
            architecture_paths.append(path)
    if not method_paths:
        errors.append(
            f"{entrypoint_path}: legacy continuation does not identify a current-eligible "
            "governing analytical method"
        )
    if not architecture_paths:
        errors.append(
            f"{entrypoint_path}: legacy continuation does not identify a current-eligible "
            "governing synthesis/corpus architecture"
        )
    return errors


def validate_project_initiation_gate(
    snapshot: GitSnapshot,
    baseline_paths: set[str],
    control: Mapping[str, Any] | None = None,
    authority: AuthorityGraph | None = None,
) -> list[str]:
    """Enforce the prospective project-initiation gate without rewriting legacy roots."""

    errors: list[str] = []
    if control is None:
        control, control_errors = _load_project_initiation_gate(snapshot)
        errors.extend(control_errors)
        if control is None:
            return errors
    classification = control.get("sequential_artifact_classification")
    marker = control.get("prospective_registry_marker")
    compatibility = control.get("legacy_compatibility")
    if not all(
        isinstance(value, Mapping)
        for value in (classification, marker, compatibility)
    ):
        return errors + ["project-initiation control is incomplete"]
    marker_field = marker["field"]
    marker_value = marker["required_value"]
    git_native_prefix = compatibility["git_native_migration_scope_prefix"]
    if authority is None:
        authority = AuthorityGraph(snapshot)
    closures = control.get("terminal_closures", {})
    registered_prefixes: set[str] = set()
    base_commit = _run_closure_base_commit(snapshot.root)
    if base_commit is None:
        errors.append(
            f"project-initiation gate needs {RUN_CLOSURE_BASE_REF} to check run-stop "
            "continuity; fetch main first"
        )
        base_seals: dict[str, tuple[str, dict[str, str]]] = {}
        releases: dict[str, tuple[str, dict[str, str]]] = {}
    else:
        base_seals = _base_run_closure_seals(snapshot.root, base_commit)
        releases = _base_run_closure_releases(snapshot.root, base_commit)
    current_seals_by_prefix: dict[str, Mapping[str, Any]] = {}

    rows: list[tuple[str, Mapping[str, Any]]] = []
    for registry_path, collection in (
        (SERIES_REGISTRY_PATH, "series"),
        (STUDY_REGISTRY_PATH, "studies"),
    ):
        entry = snapshot.get(registry_path)
        if entry is None or not entry.qualifies_as_evidence:
            continue
        try:
            registry = decode_json(entry.data, registry_path)
        except (DomainError, json.JSONDecodeError, UnicodeDecodeError):
            continue
        registry_rows = registry.get(collection) if isinstance(registry, Mapping) else None
        if not isinstance(registry_rows, list):
            continue
        rows.extend(
            (f"{registry_path}:{collection}[{index}]", row)
            for index, row in enumerate(registry_rows)
            if isinstance(row, Mapping)
        )

    # The activation tree still owns architecture adoption. Admission is a
    # separate delta against fetched main, pinned once per validation, never
    # prepare_commit's caller-selected --base. A post-integration commit audit
    # replays the main transaction against its first parent rather than self.
    admission_tree: dict[str, tuple[str, str]] = {}
    prior_rows: dict[str, list[Mapping[str, Any]]] = {}
    history = None
    comparison = None
    if base_commit is not None:
        try:
            comparison = (
                run_git(snapshot.root, "rev-parse", base_commit + "^1").decode().strip()
                if snapshot.identity == base_commit else base_commit
            )
            raw = run_git(snapshot.root, "ls-tree", "-r", "-z", "--full-tree", comparison)
            for item in raw.split(b"\0"):
                if item:
                    metadata, path = item.split(b"\t", 1)
                    mode, kind, oid = metadata.decode("ascii").split()
                    if kind == "blob":
                        admission_tree[path.decode("utf-8")] = (mode, oid)
            history_paths = {row["canonical_entrypoint"] for _, row in rows
                             if _valid_nonempty_string(row.get("canonical_entrypoint"))}
            registries = GitSnapshot.from_commit(
                snapshot.root, comparison, paths=(SERIES_REGISTRY_PATH, STUDY_REGISTRY_PATH)
            )
            for registry_path, collection in (
                (SERIES_REGISTRY_PATH, "series"), (STUDY_REGISTRY_PATH, "studies"),
            ):
                entry = registries.get(registry_path)
                if entry is None:
                    continue
                if not entry.qualifies_as_evidence:
                    raise DomainError(f"{registry_path}: admission history registry is not regular")
                registry = decode_json(entry.data, registry_path)
                values = registry.get(collection) if isinstance(registry, Mapping) else None
                if not isinstance(values, list):
                    raise DomainError(f"{registry_path}: admission history registry has no {collection} list")
                prior_rows[registry_path] = [value for value in values if isinstance(value, Mapping)]
                history_paths.update(value["canonical_entrypoint"] for value in prior_rows[registry_path]
                                     if _valid_nonempty_string(value.get("canonical_entrypoint")))
            history = GitSnapshot.from_commit(snapshot.root, comparison, paths=history_paths)
        except DomainError as exc:
            errors.append(f"project-initiation admission history is unavailable: {exc}")

    def unchanged_on_main(path: str, entry: Any) -> bool:
        previous = admission_tree.get(path)
        if previous is None or entry.mode != previous[0]:
            return False
        digest = hashlib.new("sha1" if len(previous[1]) == 40 else "sha256")
        digest.update(b"blob " + str(len(entry.data)).encode("ascii") + b"\0")
        digest.update(entry.data)
        return digest.hexdigest() == previous[1]

    # Publication grants bind from main before this transaction too: the
    # self-audit judges publication by the first parent, never the commit.
    publications: dict[str, set[str]] = {}
    if comparison is not None:
        publications, publication_errors = frozen_publication_paths(
            snapshot, comparison, control,
            {row["repository_path"]: row.get("canonical_entrypoint") for _, row in rows
             if _valid_nonempty_string(row.get("repository_path"))},
        )
        errors.extend(publication_errors)

    for label, row in rows:
        project_prefix = row.get("repository_path")
        if not _valid_nonempty_string(
            project_prefix
        ) or not project_prefix.endswith("/"):
            continue
        registered_prefixes.add(project_prefix)
        closure = closures.get(project_prefix)
        local, local_state, local_errors = _load_project_run_closure(snapshot, project_prefix)
        errors.extend(local_errors)
        if local is not None and closure is not None:
            errors.append(
                f"{project_prefix}: a project run closure and a global terminal closure cannot "
                "both be present; the global closure replaces the project record"
            )
            local = None
        if local is not None:
            errors.extend(_run_closure_on_main(snapshot, project_prefix, local, base_commit))
        if local is not None and local_state == "CLOSED":
            closure = local
        reopened = local if local is not None and local_state == "REOPENED" else None
        current_seals = (closure or reopened or {}).get("frozen_sequential_artifacts", {})
        current_seals_by_prefix[project_prefix] = current_seals
        baseline_present = any(path.startswith(project_prefix) for path in baseline_paths)
        explicit_marker = row.get(marker_field)
        if explicit_marker is not None and explicit_marker != marker_value:
            errors.append(
                f"{label}.{marker_field} must equal {marker_value!r} when present"
            )
        if not baseline_present and explicit_marker != marker_value:
            errors.append(
                f"{label}.{marker_field} must equal {marker_value!r} for a project root "
                "created after the initiation-gate activation baseline"
            )

        new_sequential: list[str] = []
        admissions: list[str] = []
        terminal_sequential: set[str] = set()
        for path, candidate in snapshot.entries.items():
            if (
                not path.startswith(project_prefix)
                or not path.endswith(".md")
                or not candidate.qualifies_as_evidence
                or (path in baseline_paths and closure is None and reopened is None
                    and unchanged_on_main(path, candidate))
            ):
                continue
            classified, fallback, artifact_errors = _is_substantive_sequential_artifact(
                path, candidate, classification
            )
            errors.extend(artifact_errors)
            if classified:
                if (not unchanged_on_main(path, candidate)
                        and path not in publications.get(project_prefix, set())):
                    admissions.append(path)
                if path not in baseline_paths:
                    new_sequential.append(path)
                terminal_sequential.add(path)
                if fallback:
                    errors.append(
                        f"{path}: sequential-reading directory artifact requires a structured "
                        "artifact_type"
                    )

        git_native = isinstance(row.get("migration_scope"), str) and row[
            "migration_scope"
        ].startswith(git_native_prefix)
        strict = (
            not baseline_present or explicit_marker == marker_value
            or git_native or closure is not None or reopened is not None
        )
        entrypoint = row.get("canonical_entrypoint")
        if closure is None and _valid_nonempty_string(entrypoint) and history is not None:
            # A moved/repointed entrypoint cannot erase a root's recorded run.
            # Match its prior registry identity or root, never just its new path.
            registry_path = label.split(":", 1)[0]
            identity_field = "series_id" if registry_path == SERIES_REGISTRY_PATH else "study_id"
            identity = row.get(identity_field)
            previous_rows = [value for value in prior_rows.get(registry_path, [])
                             if value.get("repository_path") == project_prefix or
                             (_valid_nonempty_string(identity) and value.get(identity_field) == identity)]
            previous = history.get(entrypoint)
            if len(previous_rows) > 1:
                errors.append(f"{entrypoint}: admission history has ambiguous prior project routes")
            elif previous_rows:
                previous_path = previous_rows[0].get("canonical_entrypoint")
                previous = history.get(previous_path) if _valid_nonempty_string(previous_path) else None
                if admissions and (previous is None or not previous.qualifies_as_evidence):
                    errors.append(f"{entrypoint}: admission history prior canonical entrypoint is unavailable")
            # A first publication may batch an actually completed local run.
            # A self-contained proof survives squash integration and requires
            # the exact completed reading set, never merely an active ancestor.
            # It replaces only main with no recorded run or a consistently
            # completed one: main's active run keeps the ordinary closing route
            # without consulting a stale proof, and its blocked, interrupted or
            # malformed state is never bypassed.
            current_entry = snapshot.get(entrypoint)
            state, _ = _execution_state(current_entry.data, entrypoint) if current_entry else ({}, [])
            run_state = state.get("run_state")
            prior_state, prior_errors = (
                _execution_state(previous.data, entrypoint) if previous else ({}, [])
            )
            prior_run = prior_state.get("run_state")
            # Main's completion must itself pass the ordinary consistency rules
            # (for example, both next operations NONE) before a proof replaces it.
            prior_inconsistent = _validate_run_admission(
                GitSnapshot(snapshot.root, "MAIN_RUN_STATE", {entrypoint: previous}),
                entrypoint, None, admission=False, strict=True,
            ) if previous else []
            if (admissions and isinstance(run_state, str) and run_state in TERMINAL_RUN_STATES
                    and not prior_errors and not prior_inconsistent
                    and ("run_state" not in prior_state or (
                        isinstance(prior_run, str) and prior_run in TERMINAL_RUN_STATES))):
                proved_previous, proof_errors = _completed_publication_previous(
                    snapshot, project_prefix, entrypoint, classification,
                )
                errors.extend(proof_errors)
                if proved_previous is not None:
                    previous = proved_previous
            errors.extend(_validate_run_admission(
                snapshot, entrypoint, previous,
                admission=bool(admissions), strict=strict,
            ))
        # A closure covers every reading under its root, including readings of
        # nested registered roots, exactly as the OPEN gate scan does.
        if closure is not None:
            errors.extend(
                _validate_terminal_corpus(snapshot, entrypoint, closure, terminal_sequential)
            )
        if reopened is not None:
            errors.extend(
                _validate_sealed_readings(
                    snapshot, entrypoint, reopened, terminal_sequential, exact=False
                )
            )
        if strict and (
            not baseline_present or explicit_marker == marker_value or new_sequential
            or closure is not None or reopened is not None
        ):
            errors.extend(
                _validate_initialization_contract(
                    snapshot,
                    authority,
                    project_prefix,
                    entrypoint,
                    require_open=bool(new_sequential) and closure is None,
                    terminal=closure is not None,
                )
            )
        elif new_sequential:
            errors.extend(
                _validate_legacy_architecture_route(
                    snapshot, authority, project_prefix, entrypoint
                )
            )
    for prefix in set(closures) - registered_prefixes:
        errors.append(f"project-initiation terminal closure has no registered project: {prefix}")
    for candidate in snapshot.entries:
        if candidate.endswith("/" + PROJECT_RUN_CLOSURE_NAME) and (
            candidate[: -len(PROJECT_RUN_CLOSURE_NAME)] not in registered_prefixes
        ):
            errors.append(f"project run closure has no registered project: {candidate}")
    # Every seal of a run stop on main survives, here or in a replacing terminal
    # closure, unless an owner-merged release names that exact sealed digest.
    for prefix, (record_sha256, sealed) in sorted(base_seals.items()):
        bound_record, release = releases.get(prefix, ("", {}))
        released = (
            {path for path, digest in release.items() if sealed.get(path) == digest}
            if bound_record == record_sha256 else set()
        )
        current = current_seals_by_prefix.get(prefix, {})
        for sealed_path, digest in sorted(sealed.items()):
            if sealed_path in released or current.get(sealed_path) == digest:
                continue
            where = "" if prefix in registered_prefixes else " (its root is no longer registered)"
            errors.append(
                f"{prefix}: sealed reading {sealed_path} was dropped or re-sealed relative to "
                f"main's run closure{where}; that needs an owner-merged release in "
                f"{PROJECT_INITIATION_GATE_PATH} run_closure_amendments"
            )
    return errors


def validate_series_registry(
    snapshot: GitSnapshot, authority: AuthorityGraph | None = None
) -> list[str]:
    """Validate deterministic first-read routing for every registered series."""

    entry = snapshot.get(SERIES_REGISTRY_PATH)
    if entry is None or not entry.qualifies_as_evidence:
        return [f"missing tracked regular series registry: {SERIES_REGISTRY_PATH}"]
    try:
        registry = decode_json(entry.data, SERIES_REGISTRY_PATH)
    except (DomainError, json.JSONDecodeError, UnicodeDecodeError) as exc:
        return [str(exc)]
    if not isinstance(registry, Mapping):
        return [f"{SERIES_REGISTRY_PATH} must be a JSON object"]

    errors: list[str] = []
    if registry.get("schema") != SERIES_REGISTRY_SCHEMA:
        errors.append(
            f"{SERIES_REGISTRY_PATH}.schema must equal {SERIES_REGISTRY_SCHEMA!r}"
        )
    rows = registry.get("series")
    if not isinstance(rows, list):
        errors.append(f"{SERIES_REGISTRY_PATH}.series must be an array")
        return errors
    if authority is None:
        authority = AuthorityGraph(snapshot)

    required = {
        "series_id",
        "stable_slug",
        "canonical_title",
        "repository_path",
        "canonical_entrypoint",
        "canonical_entrypoint_status",
    }
    seen_ids: dict[str, str] = {}
    seen_slugs: dict[str, str] = {}
    seen_entrypoints: dict[str, str] = {}
    for index, row in enumerate(rows):
        label = f"{SERIES_REGISTRY_PATH}:series[{index}]"
        if not isinstance(row, Mapping):
            errors.append(f"{label} must be an object")
            continue
        missing = required - set(row)
        if missing:
            errors.append(f"{label} missing required fields: {sorted(missing)}")

        series_id = row.get("series_id")
        stable_slug = row.get("stable_slug")
        repository_path = row.get("repository_path")
        for field, value in (
            ("series_id", series_id),
            ("stable_slug", stable_slug),
            ("canonical_title", row.get("canonical_title")),
            ("repository_path", repository_path),
        ):
            if not _valid_nonempty_string(value):
                errors.append(f"{label}.{field} must be a nonempty single-line string")

        if _valid_nonempty_string(series_id):
            prior = seen_ids.get(series_id)
            if prior is not None:
                errors.append(f"duplicate series_id {series_id!r}: {prior} / {label}")
            else:
                seen_ids[series_id] = label
        if _valid_nonempty_string(stable_slug):
            prior = seen_slugs.get(stable_slug)
            if prior is not None:
                errors.append(f"duplicate stable_slug {stable_slug!r}: {prior} / {label}")
            else:
                seen_slugs[stable_slug] = label

        catalog_note = row.get("catalog_note")
        if catalog_note is not None and not _valid_nonempty_string(catalog_note):
            errors.append(f"{label}.catalog_note must be a nonempty single-line string")

        repository_prefix: str | None = None
        if _valid_nonempty_string(repository_path):
            if not repository_path.endswith("/"):
                errors.append(f"{label}.repository_path must end with '/'")
            else:
                repository_prefix = repository_path
                try:
                    validate_repository_path(repository_path[:-1])
                except DomainError as exc:
                    errors.append(f"{label}.repository_path is invalid: {exc}")

        status = row.get("canonical_entrypoint_status")
        canonical_entrypoint = row.get("canonical_entrypoint")
        if not isinstance(status, str) or status not in SERIES_ENTRYPOINT_STATUSES:
            errors.append(
                f"{label}.canonical_entrypoint_status must be one of "
                f"{sorted(SERIES_ENTRYPOINT_STATUSES)}"
            )
            continue
        if status == "MISSING":
            if canonical_entrypoint is not None:
                errors.append(
                    f"{label}.canonical_entrypoint must be null when status is MISSING"
                )
            continue

        if not _valid_nonempty_string(canonical_entrypoint):
            errors.append(
                f"{label}.canonical_entrypoint must be a nonempty single-line string "
                "when status is PRESENT_VERIFIED"
            )
            continue
        try:
            validate_repository_path(canonical_entrypoint)
        except DomainError as exc:
            errors.append(f"{label}.canonical_entrypoint is invalid: {exc}")
            continue
        if PurePosixPath(canonical_entrypoint).suffix.casefold() != ".md":
            errors.append(f"{label}.canonical_entrypoint must identify a Markdown file")
        if repository_prefix is not None and not canonical_entrypoint.startswith(
            repository_prefix
        ):
            errors.append(
                f"{label}.canonical_entrypoint must remain under repository_path"
            )
        prior = seen_entrypoints.get(canonical_entrypoint)
        if prior is not None:
            errors.append(
                f"duplicate canonical_entrypoint {canonical_entrypoint!r}: "
                f"{prior} / {label}"
            )
        else:
            seen_entrypoints[canonical_entrypoint] = label
        target = snapshot.get(canonical_entrypoint)
        if target is None or not target.qualifies_as_evidence:
            errors.append(
                f"{label}.canonical_entrypoint is not a tracked regular Git blob: "
                f"{canonical_entrypoint}"
            )
        elif not authority.current_eligible(canonical_entrypoint):
            errors.append(
                f"{label}.canonical_entrypoint is not current-eligible: "
                f"{canonical_entrypoint} "
                f"(classification={authority.classification(canonical_entrypoint)})"
            )
    return errors


def _top_level_roots(snapshot: GitSnapshot, root: str) -> set[str]:
    roots = set()
    for path in snapshot.entries:
        parts = PurePosixPath(path).parts
        if len(parts) >= 3 and parts[0] == root:
            roots.add(parts[1])
    return roots


def _registry_root_slugs(
    snapshot: GitSnapshot, path: str, key: str, root: str
) -> tuple[set[str], list[str]]:
    entry = snapshot.get(path)
    if entry is None:
        return set(), [f"missing registry for {root} topology: {path}"]
    try:
        document = decode_json(entry.data, path)
    except (DomainError, json.JSONDecodeError, UnicodeDecodeError) as exc:
        return set(), [str(exc)]
    if not isinstance(document, Mapping) or not isinstance(document.get(key), list):
        return set(), [f"{path}.{key} must be an array"]
    slugs = set()
    for row in document[key]:
        if not isinstance(row, Mapping):
            continue
        slug = row.get("stable_slug")
        repository_path = row.get("repository_path")
        if isinstance(slug, str) and repository_path == f"{root}/{slug}/":
            slugs.add(slug)
    return slugs, []


def validate_registered_root_topology(snapshot: GitSnapshot) -> list[str]:
    """Require a one-to-one registry mapping for top-level series and study roots."""

    errors: list[str] = []
    for root, path, key in (
        ("series", SERIES_REGISTRY_PATH, "series"),
        ("studies", STUDY_REGISTRY_PATH, "studies"),
    ):
        registered, registry_errors = _registry_root_slugs(snapshot, path, key, root)
        errors.extend(registry_errors)
        actual = _top_level_roots(snapshot, root)
        for slug in sorted(actual - registered, key=lambda value: value.encode("utf-8")):
            errors.append(f"unregistered {root} root: {root}/{slug}/")
        for slug in sorted(registered - actual, key=lambda value: value.encode("utf-8")):
            errors.append(f"registered {root} root has no tracked content: {root}/{slug}/")
    return errors


def validate_study_registry(
    snapshot: GitSnapshot, authority: AuthorityGraph | None = None
) -> list[str]:
    entry = snapshot.get(STUDY_REGISTRY_PATH)
    if entry is None or not entry.qualifies_as_evidence:
        return [f"missing tracked regular study registry: {STUDY_REGISTRY_PATH}"]
    try:
        registry = decode_json(entry.data, STUDY_REGISTRY_PATH)
    except (DomainError, json.JSONDecodeError, UnicodeDecodeError) as exc:
        return [str(exc)]
    if not isinstance(registry, Mapping):
        return [f"{STUDY_REGISTRY_PATH} must be a JSON object"]
    errors: list[str] = []
    if registry.get("schema") != STUDY_REGISTRY_SCHEMA:
        errors.append(
            f"{STUDY_REGISTRY_PATH}.schema must equal {STUDY_REGISTRY_SCHEMA!r}"
        )
    rows = registry.get("studies")
    if not isinstance(rows, list):
        errors.append(f"{STUDY_REGISTRY_PATH}.studies must be an array")
        return errors
    if authority is None:
        authority = AuthorityGraph(snapshot)
    required = {
        "study_id",
        "stable_slug",
        "canonical_title",
        "repository_path",
        "canonical_entrypoint",
        "materialization_status",
        "authority_status",
    }
    seen_ids: set[str] = set()
    seen_slugs: set[str] = set()
    seen_entrypoints: set[str] = set()
    for index, row in enumerate(rows):
        label = f"{STUDY_REGISTRY_PATH}:studies[{index}]"
        if not isinstance(row, Mapping):
            errors.append(f"{label} must be an object")
            continue
        missing = required - set(row)
        if missing:
            errors.append(f"{label} missing required fields: {sorted(missing)}")
        for field in required:
            if not _valid_nonempty_string(row.get(field)):
                errors.append(f"{label}.{field} must be a nonempty single-line string")
        study_id = row.get("study_id")
        slug = row.get("stable_slug")
        entrypoint = row.get("canonical_entrypoint")
        if isinstance(study_id, str):
            if study_id in seen_ids:
                errors.append(f"duplicate study_id {study_id!r}")
            seen_ids.add(study_id)
        if isinstance(slug, str):
            if slug in seen_slugs:
                errors.append(f"duplicate study stable_slug {slug!r}")
            seen_slugs.add(slug)
            if row.get("repository_path") != f"studies/{slug}/":
                errors.append(f"{label}.repository_path must equal studies/{slug}/")
        if isinstance(entrypoint, str):
            if entrypoint in seen_entrypoints:
                errors.append(f"duplicate study canonical_entrypoint {entrypoint!r}")
            seen_entrypoints.add(entrypoint)
            try:
                validate_repository_path(entrypoint)
            except DomainError as exc:
                errors.append(f"{label}.canonical_entrypoint is invalid: {exc}")
            target = snapshot.get(entrypoint)
            if target is None or not target.qualifies_as_evidence:
                errors.append(
                    f"{label}.canonical_entrypoint is not a tracked regular Git blob: {entrypoint}"
                )
            elif not authority.current_eligible(entrypoint):
                errors.append(
                    f"{label}.canonical_entrypoint is not current-eligible: {entrypoint}"
                )
        if row.get("materialization_status") not in {
            "NOT_PRESENT",
            "PRESENT_UNREVIEWED",
            "PRESENT_REVIEWED",
        }:
            errors.append(f"{label}.materialization_status is not recognized")
        catalog_note = row.get("catalog_note")
        if catalog_note is not None and not _valid_nonempty_string(catalog_note):
            errors.append(f"{label}.catalog_note must be a nonempty single-line string")
    return errors


def validate_change_obligations(snapshot: GitSnapshot) -> list[str]:
    entry = snapshot.get(CHANGE_OBLIGATIONS_PATH)
    if entry is None or not entry.qualifies_as_evidence:
        return [f"missing tracked regular obligation map: {CHANGE_OBLIGATIONS_PATH}"]
    try:
        document = decode_json(entry.data, CHANGE_OBLIGATIONS_PATH)
    except (DomainError, json.JSONDecodeError, UnicodeDecodeError) as exc:
        return [str(exc)]
    if not isinstance(document, Mapping):
        return [f"{CHANGE_OBLIGATIONS_PATH} must be a JSON object"]
    errors: list[str] = []
    if document.get("schema") != CHANGE_OBLIGATIONS_SCHEMA:
        errors.append(
            f"{CHANGE_OBLIGATIONS_PATH}.schema must equal {CHANGE_OBLIGATIONS_SCHEMA!r}"
        )
    rules = document.get("rules")
    if not isinstance(rules, list) or not rules:
        errors.append(f"{CHANGE_OBLIGATIONS_PATH}.rules must be a nonempty array")
        return errors
    seen_ids: set[str] = set()
    allowed_kinds = {
        "path_changed",
        "top_level_roots_changed",
    }
    for index, rule in enumerate(rules):
        label = f"{CHANGE_OBLIGATIONS_PATH}:rules[{index}]"
        if not isinstance(rule, Mapping):
            errors.append(f"{label} must be an object")
            continue
        rule_id = rule.get("id")
        if not _valid_nonempty_string(rule_id):
            errors.append(f"{label}.id must be a nonempty single-line string")
        elif rule_id in seen_ids:
            errors.append(f"duplicate obligation rule id: {rule_id!r}")
        else:
            seen_ids.add(rule_id)
        trigger = rule.get("trigger")
        kind = trigger.get("kind") if isinstance(trigger, Mapping) else None
        if kind not in allowed_kinds:
            errors.append(f"{label}.trigger.kind is not recognized: {kind!r}")
        if kind == "path_changed" and not _valid_nonempty_string(trigger.get("path")):
            errors.append(f"{label}.trigger.path must be a nonempty string")
        if kind == "top_level_roots_changed" and trigger.get("root") not in {
            "series/",
            "studies/",
        }:
            errors.append(f"{label}.trigger.root must be series/ or studies/")
        outputs = rule.get("required_outputs")
        if not isinstance(outputs, list) or not outputs:
            errors.append(f"{label}.required_outputs must be a nonempty array")
            continue
        if len(outputs) != len(set(outputs)):
            errors.append(f"{label}.required_outputs contains duplicates")
        for path in outputs:
            if not _valid_nonempty_string(path):
                errors.append(f"{label}.required_outputs contains an invalid path")
                continue
            try:
                validate_repository_path(path)
            except DomainError as exc:
                errors.append(f"{label}.required_outputs path is invalid: {exc}")
                continue
            target = snapshot.get(path)
            if target is None or not target.qualifies_as_evidence:
                errors.append(f"{label}.required output is not tracked regular: {path}")
    return errors


def _validate_crosswalk_record_basics(
    row: Mapping[str, Any], label: str, required: set[str]
) -> list[str]:
    errors: list[str] = []
    missing = required - set(row)
    if missing:
        errors.append(f"{label} missing required fields: {sorted(missing)}")
    schema_version = row.get("schema_version")
    if (
        isinstance(schema_version, bool)
        or not isinstance(schema_version, int)
        or schema_version != 1
    ):
        errors.append(f"{label}.schema_version must equal 1")
    for field in required - {
        "schema_version",
        "destination_bytes",
        "git_bytes",
        "source_bytes",
    }:
        if field in row and not _valid_nonempty_string(row[field]):
            errors.append(f"{label}.{field} must be a nonempty single-line string")
    return errors


def _is_positive_integer(value: Any) -> bool:
    return isinstance(value, int) and not isinstance(value, bool) and value > 0


def _validate_crosswalk_source_group(
    row: Mapping[str, Any], label: str
) -> list[str]:
    """Validate optional one-to-many source provenance on a representation."""

    errors: list[str] = []
    source_ids = row.get("source_drive_ids")
    source_tuples = row.get("source_tuples")
    if source_ids is None and source_tuples is None:
        return errors
    if not isinstance(source_ids, list) or not source_ids:
        return [f"{label}.source_drive_ids must be a nonempty array"]
    if any(not _valid_nonempty_string(item) for item in source_ids):
        errors.append(f"{label}.source_drive_ids contains an invalid ID")
    if len(source_ids) != len(set(source_ids)):
        errors.append(f"{label}.source_drive_ids contains a duplicate ID")
    if source_ids and source_ids[0] != row.get("drive_id"):
        errors.append(f"{label}.source_drive_ids must begin with drive_id")
    if not isinstance(source_tuples, list) or len(source_tuples) != len(source_ids):
        errors.append(
            f"{label}.source_tuples must align one-for-one with source_drive_ids"
        )
        return errors

    tuple_ids: list[Any] = []
    required = {
        "drive_id",
        "source_path",
        "source_bytes",
        "source_revision",
        "source_sha256",
    }
    for index, item in enumerate(source_tuples):
        tuple_label = f"{label}.source_tuples[{index}]"
        if not isinstance(item, Mapping):
            errors.append(f"{tuple_label} must be an object")
            continue
        missing = required - set(item)
        if missing:
            errors.append(f"{tuple_label} missing fields: {sorted(missing)}")
            continue
        tuple_ids.append(item.get("drive_id"))
        for field in ("drive_id", "source_path"):
            if not _valid_nonempty_string(item.get(field)):
                errors.append(f"{tuple_label}.{field} is invalid")
        if not _is_positive_integer(item.get("source_bytes")):
            errors.append(f"{tuple_label}.source_bytes must be a positive integer")
        revision = item.get("source_revision")
        if not isinstance(revision, str) or POSITIVE_DECIMAL_RE.fullmatch(revision) is None:
            errors.append(
                f"{tuple_label}.source_revision must be a positive decimal string"
            )
        source_sha256 = item.get("source_sha256")
        if not isinstance(source_sha256, str) or SHA256_RE.fullmatch(source_sha256) is None:
            errors.append(f"{tuple_label}.source_sha256 is invalid")

    if tuple_ids != source_ids:
        errors.append(f"{label}.source_tuples IDs do not match source_drive_ids")
    if source_tuples and isinstance(source_tuples[0], Mapping):
        first = source_tuples[0]
        for field in (
            "drive_id",
            "source_path",
            "source_bytes",
            "source_revision",
            "source_sha256",
        ):
            if first.get(field) != row.get(field):
                errors.append(
                    f"{label}.{field} does not match the canonical source tuple"
                )
    if row.get("transformation") == "MERGE_IDENTICAL_BYTES_V1":
        byte_identities = {
            (item.get("source_bytes"), item.get("source_sha256"))
            for item in source_tuples
            if isinstance(item, Mapping)
        }
        if len(byte_identities) != 1:
            errors.append(
                f"{label} MERGE_IDENTICAL_BYTES_V1 sources are not byte-identical"
            )
    return errors


def _crosswalk_path_scope(row: Mapping[str, Any], path: str, label: str) -> list[str]:
    errors: list[str] = []
    scope_fields = [
        field for field in ("series_id", "study_id", "governance_id") if field in row
    ]
    if len(scope_fields) != 1:
        return [
            f"{label} must declare exactly one of series_id, study_id, or governance_id"
        ]
    field = scope_fields[0]
    value = row[field]
    if not _valid_nonempty_string(value):
        return [f"{label}.{field} must be a nonempty single-line string"]
    if field == "governance_id":
        if value != "repository":
            errors.append(f"{label}.governance_id must equal 'repository'")
        expected = "governance/"
    else:
        expected = f"{'series' if field == 'series_id' else 'studies'}/{value}/"
    if not path.startswith(expected):
        errors.append(
            f"{label} scope/path mismatch: {field}={value!r}, path={path!r}"
        )
    return errors


def _compare_crosswalk_field(
    errors: list[str],
    destination: str,
    left_label: str,
    left: Mapping[str, Any],
    left_field: str,
    right_label: str,
    right: Mapping[str, Any],
    right_field: str,
) -> None:
    if left.get(left_field) != right.get(right_field):
        errors.append(
            f"crosswalk {destination} {left_field}/{right_field} mismatch between "
            f"{left_label} and {right_label}"
        )


def active_migration_baseline_commit(snapshot: GitSnapshot) -> str | None:
    """Return the immutable migration baseline once Git authority is active."""

    entry = snapshot.get("governance/AUTHORITY_SCOPE.json")
    if entry is None:
        return None
    scope = decode_json(entry.data, "governance/AUTHORITY_SCOPE.json")
    if not isinstance(scope, Mapping):
        raise DomainError("authority scope must be an object")
    activation = scope.get("activation")
    if not isinstance(activation, Mapping):
        return None
    if activation.get("state") not in {"GIT_ACTIVE_STABILIZING", "GIT_ACTIVE_ACCEPTED"}:
        return None
    commit = activation.get("candidate_commit")
    if not isinstance(commit, str) or not re.fullmatch(r"[0-9a-f]{40}|[0-9a-f]{64}", commit):
        raise DomainError("active authority scope has an invalid candidate_commit")
    return commit


def validate_active_authority_scope(snapshot: GitSnapshot, baseline_commit: str | None) -> list[str]:
    """Bind the live authority scope to its cutover record and frozen ledgers."""

    if baseline_commit is None:
        return []
    errors: list[str] = []
    scope_entry = snapshot.get("governance/AUTHORITY_SCOPE.json")
    cutover_entry = snapshot.get("governance/cutovers/AUTHORITY_EPOCH_1.json")
    if scope_entry is None or cutover_entry is None:
        return ["active authority scope or epoch-1 cutover record is absent"]
    try:
        scope = decode_json(scope_entry.data, "governance/AUTHORITY_SCOPE.json")
        cutover = decode_json(cutover_entry.data, "governance/cutovers/AUTHORITY_EPOCH_1.json")
    except (DomainError, json.JSONDecodeError, UnicodeDecodeError) as exc:
        return [str(exc)]
    if not isinstance(scope, Mapping) or not isinstance(cutover, Mapping):
        return ["active authority scope and cutover record must be objects"]
    scope_hash = hashlib.sha256(scope_entry.data).hexdigest()
    if cutover.get("authority_scope_sha256") != scope_hash:
        errors.append("cutover authority-scope SHA-256 does not match committed bytes")
    if cutover.get("activation_commit") != baseline_commit:
        errors.append("cutover activation commit does not match authority scope")
    manifest = scope.get("scope_manifest")
    components = manifest.get("components") if isinstance(manifest, Mapping) else None
    if not isinstance(components, list):
        errors.append("active authority scope has no component list")
        return errors
    for component in components:
        if not isinstance(component, Mapping):
            errors.append("active authority component must be an object")
            continue
        path = component.get("path")
        expected_hash = component.get("sha256")
        expected_rows = component.get("rows")
        if not isinstance(path, str) or not isinstance(expected_hash, str):
            errors.append("active authority component path/hash is invalid")
            continue
        entry = snapshot.get(path)
        if entry is None or not entry.qualifies_as_evidence:
            errors.append(f"active authority component is absent or unsafe: {path}")
            continue
        if hashlib.sha256(entry.data).hexdigest() != expected_hash:
            errors.append(f"active authority component SHA-256 drift: {path}")
        rows = len([line for line in entry.data.split(b"\n") if line])
        if rows != expected_rows:
            errors.append(f"active authority component row-count drift: {path}")
    return errors


def validate_crosswalk_closure(
    snapshot: GitSnapshot, *, baseline_commit: str | None = None
) -> list[str]:
    """Validate migration provenance and current closure.

    Before cutover, declared destination bytes must match the selected snapshot. After
    cutover, those declarations remain immutable migration provenance bound to the
    activation commit; later authorized Git-primary edits are validated as current
    repository content without rewriting the historical crosswalk.
    """

    errors: list[str] = []
    try:
        mappings = _snapshot_jsonl(snapshot, CROSSWALK_FILES["mapping"])
        results = _snapshot_jsonl(snapshot, CROSSWALK_FILES["results"])
        plans = _snapshot_jsonl(snapshot, CROSSWALK_FILES["plan"])
    except (DomainError, json.JSONDecodeError, UnicodeDecodeError) as exc:
        return [str(exc)]

    baseline_cache: dict[str, bytes | None] = {}

    def baseline_bytes(path: str) -> bytes | None:
        if baseline_commit is None:
            return None
        if path not in baseline_cache:
            try:
                baseline_cache[path] = run_git(snapshot.root, "show", f"{baseline_commit}:{path}")
            except DomainError:
                baseline_cache[path] = None
        return baseline_cache[path]

    mapping_by_path: dict[str, Mapping[str, Any]] = {}
    representation_paths: dict[str, str] = {}
    for index, row in enumerate(mappings):
        label = f"{CROSSWALK_FILES['mapping']}:{index + 1}"
        required = {
            "schema_version",
            "drive_id",
            "source_path",
            "source_sha256",
            "git_path",
            "git_sha256",
            "transformation",
            "representation_id",
        }
        errors.extend(_validate_crosswalk_record_basics(row, label, required))
        errors.extend(_validate_crosswalk_source_group(row, label))
        if not required.issubset(row):
            continue
        path = row["git_path"]
        if not isinstance(path, str):
            continue
        try:
            validate_repository_path(path)
        except DomainError as exc:
            errors.append(f"{label}.git_path is invalid: {exc}")
            continue
        if not isinstance(row["source_sha256"], str) or not SHA256_RE.fullmatch(
            row["source_sha256"]
        ):
            errors.append(f"{label}.source_sha256 is not a lowercase SHA-256")
        if not isinstance(row["git_sha256"], str) or not SHA256_RE.fullmatch(
            row["git_sha256"]
        ):
            errors.append(f"{label}.git_sha256 is not a lowercase SHA-256")
        representation_id = row["representation_id"]
        if not isinstance(representation_id, str) or not REPRESENTATION_ID_RE.fullmatch(
            representation_id
        ):
            errors.append(f"{label}.representation_id is invalid")
            continue
        prior_representation = representation_paths.get(representation_id)
        if prior_representation is not None:
            errors.append(
                f"duplicate crosswalk representation_id {representation_id}: "
                f"{prior_representation} / {path}"
            )
        else:
            representation_paths[representation_id] = path
        if path in mapping_by_path:
            errors.append(f"duplicate drive-to-git destination path: {path}")
            continue
        mapping_by_path[path] = row
        errors.extend(_crosswalk_path_scope(row, path, label))
        entry = snapshot.get(path)
        if entry is None and baseline_commit is None:
            errors.append(f"drive-to-git destination is absent from snapshot: {path}")
        elif entry is not None and not entry.qualifies_as_evidence:
            errors.append(
                f"drive-to-git destination is not a tracked regular non-LFS blob: {path}"
            )
        else:
            provenance_data = entry.data if entry is not None else b""
            actual_hash = hashlib.sha256(provenance_data).hexdigest()
            if actual_hash != row["git_sha256"] and baseline_commit is not None:
                frozen = baseline_bytes(path)
                if frozen is not None:
                    provenance_data = frozen
                    actual_hash = hashlib.sha256(frozen).hexdigest()
            if actual_hash != row["git_sha256"]:
                errors.append(
                    f"drive-to-git committed-byte hash drift: {path}; "
                    f"declared={row['git_sha256']}, actual={actual_hash}"
                )
            if path.startswith("studies/"):
                if row.get("git_bytes") != len(provenance_data):
                    errors.append(f"drive-to-git committed-byte length drift: {path}")

    materialized_by_path: dict[str, Mapping[str, Any]] = {}
    reference_results: dict[tuple[str, str], Mapping[str, Any]] = {}
    for index, row in enumerate(results):
        label = f"{CROSSWALK_FILES['results']}:{index + 1}"
        result = row.get("result")
        if result == "MATERIALIZED_AND_HASH_VERIFIED":
            required = {
                "schema_version",
                "drive_id",
                "source_sha256",
                "destination_path",
                "destination_sha256",
                "destination_bytes",
                "transformation",
                "run_id",
            }
            errors.extend(_validate_crosswalk_record_basics(row, label, required))
            errors.extend(_validate_crosswalk_source_group(row, label))
            path = row.get("destination_path")
            if not isinstance(path, str):
                continue
            try:
                validate_repository_path(path)
            except DomainError as exc:
                errors.append(f"{label}.destination_path is invalid: {exc}")
                continue
            if path in materialized_by_path:
                errors.append(f"duplicate materialization destination path: {path}")
            else:
                materialized_by_path[path] = row
            if not isinstance(row.get("source_sha256"), str) or not SHA256_RE.fullmatch(
                row["source_sha256"]
            ):
                errors.append(f"{label}.source_sha256 is not a lowercase SHA-256")
            if not isinstance(row.get("destination_sha256"), str) or not SHA256_RE.fullmatch(
                row["destination_sha256"]
            ):
                errors.append(f"{label}.destination_sha256 is not a lowercase SHA-256")
            if not _is_positive_integer(row.get("destination_bytes")):
                errors.append(f"{label}.destination_bytes must be a positive integer")
            if "source_bytes" in row and not _is_positive_integer(row["source_bytes"]):
                errors.append(f"{label}.source_bytes must be a positive integer")
            if "body_preserved" in row and not isinstance(row["body_preserved"], bool):
                errors.append(f"{label}.body_preserved must be a boolean")
        elif result == "REFERENCE_VERIFIED_NOT_MATERIALIZED":
            required = {
                "schema_version",
                "drive_id",
                "source_path",
                "source_sha256",
                "transformation",
                "run_id",
                "terminal_action",
            }
            errors.extend(_validate_crosswalk_record_basics(row, label, required))
            key = (row.get("drive_id"), row.get("source_path"))
            if not all(isinstance(item, str) for item in key):
                continue
            if key in reference_results:
                errors.append(f"duplicate reference-only materialization result: {key}")
            else:
                reference_results[key] = row
            if row.get("terminal_action") != "REFERENCE_DRIVE":
                errors.append(f"{label}.terminal_action must equal REFERENCE_DRIVE")
            if not isinstance(row.get("source_sha256"), str) or not SHA256_RE.fullmatch(
                row["source_sha256"]
            ):
                errors.append(f"{label}.source_sha256 is not a lowercase SHA-256")
            if not _is_positive_integer(row.get("source_bytes")):
                errors.append(f"{label}.source_bytes must be a positive integer")
            prohibited = {
                "destination_path",
                "destination_sha256",
                "destination_bytes",
                "representation_id",
                "series_id",
                "study_id",
                "governance_id",
                "source_drive_ids",
                "source_tuples",
            }
            present = sorted(prohibited & set(row))
            if present:
                errors.append(
                    f"{label} reference-only row contains destination fields: {present}"
                )
        else:
            errors.append(f"{label}.result is not a recognized terminal result")

    planned_by_path: dict[str, Mapping[str, Any]] = {}
    reference_plans: dict[tuple[str, str], Mapping[str, Any]] = {}
    for index, row in enumerate(plans):
        label = f"{CROSSWALK_FILES['plan']}:{index + 1}"
        decision = row.get("decision")
        if isinstance(decision, str) and decision.startswith("MIGRATE_"):
            required = {
                "schema_version",
                "drive_id",
                "source_path",
                "destination_path",
                "path_status",
            }
            errors.extend(_validate_crosswalk_record_basics(row, label, required))
            errors.extend(_validate_crosswalk_source_group(row, label))
            path = row.get("destination_path")
            if not isinstance(path, str):
                continue
            try:
                validate_repository_path(path)
            except DomainError as exc:
                errors.append(f"{label}.destination_path is invalid: {exc}")
                continue
            if row.get("path_status") != "MATERIALIZED_PROSPECTIVE":
                errors.append(
                    f"{label}.path_status must equal MATERIALIZED_PROSPECTIVE"
                )
            if path in planned_by_path:
                errors.append(f"duplicate path-plan destination path: {path}")
            else:
                planned_by_path[path] = row
        elif decision == "REFERENCE_DRIVE":
            required = {
                "schema_version",
                "drive_id",
                "source_path",
                "path_status",
            }
            errors.extend(_validate_crosswalk_record_basics(row, label, required))
            key = (row.get("drive_id"), row.get("source_path"))
            if not all(isinstance(item, str) for item in key):
                continue
            if key in reference_plans:
                errors.append(f"duplicate reference-only path-plan row: {key}")
            else:
                reference_plans[key] = row
            if row.get("path_status") != "REFERENCE_VERIFIED_NOT_MATERIALIZED":
                errors.append(
                    f"{label}.path_status must equal REFERENCE_VERIFIED_NOT_MATERIALIZED"
                )
            prohibited = {
                "destination_path",
                "destination_sha256",
                "destination_bytes",
                "representation_id",
                "series_id",
                "study_id",
                "governance_id",
                "source_drive_ids",
                "source_tuples",
            }
            present = sorted(prohibited & set(row))
            if present:
                errors.append(
                    f"{label} reference-only row contains destination fields: {present}"
                )
        else:
            errors.append(f"{label}.decision is not a recognized migration decision")

    destination_sets = {
        "drive-to-git": set(mapping_by_path),
        "materialization-results": set(materialized_by_path),
        "path-plan": set(planned_by_path),
    }
    authoritative_destinations = destination_sets["drive-to-git"]
    for label, destinations in destination_sets.items():
        if destinations != authoritative_destinations:
            errors.append(
                f"crosswalk three-leg destination closure failure ({label}); "
                f"missing={sorted(authoritative_destinations - destinations)}, "
                f"extra={sorted(destinations - authoritative_destinations)}"
            )

    for path in sorted(
        authoritative_destinations
        & set(materialized_by_path)
        & set(planned_by_path),
        key=lambda item: item.encode("utf-8"),
    ):
        mapping = mapping_by_path[path]
        result = materialized_by_path[path]
        plan = planned_by_path[path]
        _compare_crosswalk_field(
            errors, path, "mapping", mapping, "drive_id", "result", result, "drive_id"
        )
        _compare_crosswalk_field(
            errors, path, "mapping", mapping, "drive_id", "plan", plan, "drive_id"
        )
        _compare_crosswalk_field(
            errors,
            path,
            "mapping",
            mapping,
            "source_path",
            "plan",
            plan,
            "source_path",
        )
        if "source_path" in result:
            _compare_crosswalk_field(
                errors,
                path,
                "mapping",
                mapping,
                "source_path",
                "result",
                result,
                "source_path",
            )
        _compare_crosswalk_field(
            errors,
            path,
            "mapping",
            mapping,
            "source_sha256",
            "result",
            result,
            "source_sha256",
        )
        _compare_crosswalk_field(
            errors,
            path,
            "mapping",
            mapping,
            "git_sha256",
            "result",
            result,
            "destination_sha256",
        )
        _compare_crosswalk_field(
            errors,
            path,
            "mapping",
            mapping,
            "transformation",
            "result",
            result,
            "transformation",
        )
        for field in (
            "governance_id",
            "source_drive_ids",
            "source_tuples",
        ):
            if any(field in leg for leg in (mapping, result, plan)):
                _compare_crosswalk_field(
                    errors, path, "mapping", mapping, field, "result", result, field
                )
                _compare_crosswalk_field(
                    errors, path, "mapping", mapping, field, "plan", plan, field
                )
        entry = snapshot.get(path)
        if (entry is not None and entry.qualifies_as_evidence) or baseline_commit is not None:
            provenance_data = entry.data if entry is not None else b""
            if (
                result.get("destination_sha256") != hashlib.sha256(provenance_data).hexdigest()
                and baseline_commit is not None
            ):
                frozen = baseline_bytes(path)
                if frozen is not None:
                    provenance_data = frozen
            if result.get("destination_bytes") != len(provenance_data):
                errors.append(f"materialization destination byte-length drift: {path}")
            if result.get("destination_sha256") != hashlib.sha256(provenance_data).hexdigest():
                errors.append(f"materialization destination SHA-256 drift: {path}")

        if path.startswith("studies/"):
            required_study_fields = {
                "mapping": {
                    "study_id",
                    "representation_id",
                    "source_path",
                    "source_bytes",
                    "source_revision",
                    "source_sha256",
                    "transformation",
                    "git_bytes",
                    "git_sha256",
                },
                "result": {
                    "study_id",
                    "representation_id",
                    "source_path",
                    "source_bytes",
                    "source_revision",
                    "source_sha256",
                    "transformation",
                    "destination_bytes",
                    "destination_sha256",
                },
                "plan": {
                    "study_id",
                    "representation_id",
                    "source_path",
                    "source_bytes",
                    "source_revision",
                    "source_sha256",
                    "transformation",
                    "destination_bytes",
                    "destination_sha256",
                },
            }
            for leg_label, leg in (
                ("mapping", mapping),
                ("result", result),
                ("plan", plan),
            ):
                missing = required_study_fields[leg_label] - set(leg)
                if missing:
                    errors.append(
                        f"study crosswalk {path} {leg_label} leg missing bindings: "
                        f"{sorted(missing)}"
                    )
                source_path = leg.get("source_path")
                source_bytes = leg.get("source_bytes")
                source_revision = leg.get("source_revision")
                source_sha256 = leg.get("source_sha256")
                if not _valid_nonempty_string(source_path):
                    errors.append(
                        f"study crosswalk {path} {leg_label}.source_path is invalid"
                    )
                if not _is_positive_integer(source_bytes):
                    errors.append(
                        f"study crosswalk {path} {leg_label}.source_bytes must be a "
                        "positive integer"
                    )
                if (
                    not isinstance(source_revision, str)
                    or POSITIVE_DECIMAL_RE.fullmatch(source_revision) is None
                ):
                    errors.append(
                        f"study crosswalk {path} {leg_label}.source_revision must be a "
                        "positive decimal string"
                    )
                if (
                    not isinstance(source_sha256, str)
                    or SHA256_RE.fullmatch(source_sha256) is None
                ):
                    errors.append(
                        f"study crosswalk {path} {leg_label}.source_sha256 is invalid"
                    )
            for field in (
                "study_id",
                "representation_id",
                "source_path",
                "source_bytes",
                "source_revision",
                "source_sha256",
                "transformation",
            ):
                _compare_crosswalk_field(
                    errors, path, "mapping", mapping, field, "result", result, field
                )
                _compare_crosswalk_field(
                    errors, path, "mapping", mapping, field, "plan", plan, field
                )
            for leg_label, leg in (("result", result), ("plan", plan)):
                _compare_crosswalk_field(
                    errors,
                    path,
                    "mapping",
                    mapping,
                    "git_sha256",
                    leg_label,
                    leg,
                    "destination_sha256",
                )
                _compare_crosswalk_field(
                    errors,
                    path,
                    "mapping",
                    mapping,
                    "git_bytes",
                    leg_label,
                    leg,
                    "destination_bytes",
                )

    if set(reference_results) != set(reference_plans):
        errors.append(
            "reference-only crosswalk closure failure; "
            f"missing_results={sorted(set(reference_plans) - set(reference_results))}, "
            f"missing_plans={sorted(set(reference_results) - set(reference_plans))}"
        )
    for key in set(reference_results) & set(reference_plans):
        result = reference_results[key]
        plan = reference_plans[key]
        if key[0] == "1fDfRSY9oHovjAcO-YPItDfZlirPjlc3yL8IZQZMRRXg":
            if result.get("transformation") != NATIVE_SHEET_REFERENCE_TRANSFORMATION:
                errors.append(
                    "P03 native XLSX reference result has an invalid transformation"
                )
            if (
                "transformation" in plan
                and plan["transformation"] != NATIVE_SHEET_REFERENCE_TRANSFORMATION
            ):
                errors.append(
                    "P03 native XLSX reference plan has an invalid transformation"
                )
    return errors


def _excel_column_number(label: str) -> int:
    result = 0
    for character in label:
        result = result * 26 + (ord(character) - ord("A") + 1)
    return result


def _validate_native_tsv(
    snapshot: GitSnapshot,
    path: str,
    expected_rows: int,
    expected_columns: int,
    expected_sha256: str,
) -> list[str]:
    errors: list[str] = []
    entry = snapshot.get(path)
    if entry is None:
        return [f"native-sheet TSV is missing: {path}"]
    if not entry.qualifies_as_evidence:
        return [f"native-sheet TSV is not a tracked regular non-LFS Git blob: {path}"]
    data = entry.data
    actual_sha256 = hashlib.sha256(data).hexdigest()
    if actual_sha256 != expected_sha256:
        errors.append(
            f"native-sheet TSV SHA-256 drift: {path}; "
            f"declared={expected_sha256}, actual={actual_sha256}"
        )
    if data.startswith(b"\xef\xbb\xbf"):
        errors.append(f"native-sheet TSV has a prohibited UTF-8 BOM: {path}")
    if b"\r" in data or b"\0" in data:
        errors.append(f"native-sheet TSV contains a prohibited control byte: {path}")
    if not data.endswith(b"\n"):
        errors.append(f"native-sheet TSV must end with exactly one LF-terminated row: {path}")
    try:
        text = data.decode("utf-8", "strict")
    except UnicodeDecodeError as exc:
        errors.append(f"native-sheet TSV is not strict UTF-8: {path}: {exc}")
        return errors
    if any(
        (ord(character) < 32 and character not in {"\t", "\n"})
        or 127 <= ord(character) <= 159
        for character in text
    ):
        errors.append(f"native-sheet TSV contains a prohibited text control: {path}")
    rows = text[:-1].split("\n") if text.endswith("\n") else text.split("\n")
    if len(rows) != expected_rows:
        errors.append(
            f"native-sheet TSV row-count drift: {path}; "
            f"declared={expected_rows}, actual={len(rows)}"
        )
    for row_number, row in enumerate(rows, 1):
        actual_columns = len(row.split("\t"))
        if actual_columns != expected_columns:
            errors.append(
                f"native-sheet TSV rectangularity failure: {path}:row={row_number}; "
                f"declared_columns={expected_columns}, actual_columns={actual_columns}"
            )
    return errors


def validate_native_sheets(snapshot: GitSnapshot, require_schema: bool) -> list[str]:
    """Validate native-sheet manifests and projections from exact snapshot blobs."""

    errors: list[str] = []
    schema_entry = snapshot.get(NATIVE_SHEET_SCHEMA)
    if schema_entry is None:
        return [f"native-sheet schema is missing: {NATIVE_SHEET_SCHEMA}"]
    if not schema_entry.qualifies_as_evidence:
        return [f"native-sheet schema is not a tracked regular Git blob: {NATIVE_SHEET_SCHEMA}"]
    try:
        schema = decode_json(schema_entry.data, NATIVE_SHEET_SCHEMA)
        if not isinstance(schema, Mapping):
            raise DomainError("native-sheet schema must be a JSON object")
        if require_schema:
            validate_schema_document(schema, "native-sheet structure schema")
    except (DomainError, json.JSONDecodeError, UnicodeDecodeError) as exc:
        return [str(exc)]

    try:
        mapping_rows = _snapshot_jsonl(snapshot, CROSSWALK_FILES["mapping"])
        result_rows = _snapshot_jsonl(snapshot, CROSSWALK_FILES["results"])
        plan_rows = _snapshot_jsonl(snapshot, CROSSWALK_FILES["plan"])
    except (DomainError, json.JSONDecodeError, UnicodeDecodeError) as exc:
        return [str(exc)]

    crosswalk_native_manifests = {
        row.get("git_path")
        for row in mapping_rows
        if row.get("transformation") == NATIVE_SHEET_TRANSFORMATION
        and isinstance(row.get("git_path"), str)
        and row["git_path"].endswith(".structure.json")
    }
    schema_id_native_manifests: set[str] = set()
    for path, entry in snapshot.entries.items():
        if not path.endswith(".structure.json"):
            continue
        try:
            candidate = decode_json(entry.data, path)
        except (DomainError, json.JSONDecodeError, UnicodeDecodeError):
            # Generic JSON validation reports malformed unrelated JSON. A path named
            # by the native crosswalk remains in the candidate set and fails below.
            continue
        if isinstance(candidate, Mapping) and candidate.get("schema") == NATIVE_SHEET_SCHEMA_ID:
            schema_id_native_manifests.add(path)
    manifest_paths = sorted(
        crosswalk_native_manifests | schema_id_native_manifests,
        key=lambda item: item.encode("utf-8"),
    )
    if not manifest_paths:
        return ["native-sheet schema is present but no structure manifest is tracked"]
    if not require_schema:
        return ["schema-engine deferral is prohibited for a native-sheet manifest"]

    represented_tsvs: set[str] = set()
    p03_manifest_count = 0
    for manifest_path in manifest_paths:
        entry = snapshot.get(manifest_path)
        if entry is None or not entry.qualifies_as_evidence:
            errors.append(
                f"native-sheet manifest is not a tracked regular non-LFS Git blob: "
                f"{manifest_path}"
            )
            continue
        try:
            manifest = decode_json(entry.data, manifest_path)
        except (DomainError, json.JSONDecodeError, UnicodeDecodeError) as exc:
            errors.append(str(exc))
            continue
        if not isinstance(manifest, Mapping):
            errors.append(f"native-sheet manifest is not an object: {manifest_path}")
            continue
        diagnostics = schema_diagnostics(manifest, schema, manifest_path)
        schema_failures = render_schema_diagnostics(diagnostics)
        if schema_failures:
            errors.append("\n".join(schema_failures))
            continue
        if manifest.get("schema") != NATIVE_SHEET_SCHEMA_ID:
            errors.append(f"unrecognized native-sheet manifest schema: {manifest_path}")
            continue
        source_drive_id = manifest["source_drive_id"]
        if source_drive_id == "1fDfRSY9oHovjAcO-YPItDfZlirPjlc3yL8IZQZMRRXg":
            p03_manifest_count += 1
            if manifest["worksheet_count"] != 17:
                errors.append("P03 native-sheet manifest must declare exactly 17 worksheets")
        worksheets = manifest["worksheets"]
        if manifest["worksheet_count"] != len(worksheets):
            errors.append(
                f"native-sheet worksheet_count mismatch: {manifest_path}; "
                f"declared={manifest['worksheet_count']}, actual={len(worksheets)}"
            )
        normalized_names: dict[str, str] = {}
        manifest_base = manifest_path[: -len(".structure.json")]
        tabs_prefix = f"{manifest_base}.tabs/"
        expected_tsvs: set[str] = set()
        for ordinal, worksheet in enumerate(worksheets):
            label = f"{manifest_path}:worksheets[{ordinal}]"
            if worksheet["index"] != ordinal:
                errors.append(
                    f"native-sheet worksheet indices are not contiguous and ordered: {label}"
                )
            name = worksheet["name"]
            folded = unicodedata.normalize("NFC", name).casefold()
            if folded in normalized_names:
                errors.append(
                    f"native-sheet worksheet name collision: "
                    f"{normalized_names[folded]!r} / {name!r}"
                )
            else:
                normalized_names[folded] = name
            match = EXCEL_RANGE_RE.fullmatch(worksheet["address"])
            if match is None:
                errors.append(f"native-sheet declared range is invalid: {label}")
            else:
                address_columns = _excel_column_number(match.group(1))
                address_rows = int(match.group(2))
                if address_columns != worksheet["columns"] or address_rows != worksheet["rows"]:
                    errors.append(
                        f"native-sheet declared range end/shape mismatch: {label}"
                    )
            if worksheet["formula_cells"] or worksheet["tables"] != 0:
                errors.append(f"native-sheet formulas and tables must both be zero: {label}")
            tsv_path = worksheet["tsv_destination_path"]
            try:
                validate_repository_path(tsv_path)
            except DomainError as exc:
                errors.append(f"{label}.tsv_destination_path is invalid: {exc}")
                continue
            expected_prefix = f"{ordinal + 1:02d}-"
            tsv_name = PurePosixPath(tsv_path).name
            if not tsv_path.startswith(tabs_prefix) or not tsv_name.startswith(expected_prefix):
                errors.append(
                    f"native-sheet TSV escapes exact .tabs/ containment or ordinal: {tsv_path}"
                )
            if tsv_path in expected_tsvs:
                errors.append(f"duplicate native-sheet TSV destination: {tsv_path}")
            expected_tsvs.add(tsv_path)
            represented_tsvs.add(tsv_path)
            errors.extend(
                _validate_native_tsv(
                    snapshot,
                    tsv_path,
                    worksheet["rows"],
                    worksheet["columns"],
                    worksheet["tsv_sha256"],
                )
            )
        sibling_tsvs = {
            path
            for path in snapshot.entries
            if path.startswith(tabs_prefix) and path.endswith(".tsv")
        }
        if sibling_tsvs != expected_tsvs:
            errors.append(
                f"native-sheet sibling TSV closure failure: {manifest_path}; "
                f"missing={sorted(expected_tsvs - sibling_tsvs)}, "
                f"orphan={sorted(sibling_tsvs - expected_tsvs)}"
            )

    unrepresented = sorted(
        (
            path
            for path in snapshot.entries
            if ".tabs/" in path and path.endswith(".tsv") and path not in represented_tsvs
        ),
        key=lambda item: item.encode("utf-8"),
    )
    if unrepresented:
        errors.append(f"orphan native-sheet TSV paths: {unrepresented}")
    tracked_xlsx = sorted(
        path
        for path, entry in snapshot.entries.items()
        if path.casefold().endswith(".xlsx") and entry.tracked
    )
    if tracked_xlsx:
        errors.append(f"native XLSX must remain REFERENCE_DRIVE: {tracked_xlsx}")
    if p03_manifest_count != 1:
        errors.append(
            f"P03 native-sheet manifest count must equal one; actual={p03_manifest_count}"
        )

    # Bind every manifest-derived Git object back to its exact three-leg records.
    for manifest_path in manifest_paths:
        entry = snapshot.get(manifest_path)
        if entry is None:
            continue
        try:
            manifest = decode_json(entry.data, manifest_path)
        except (DomainError, json.JSONDecodeError, UnicodeDecodeError):
            continue
        if not isinstance(manifest, Mapping) or manifest.get("schema") != NATIVE_SHEET_SCHEMA_ID:
            continue
        expected_paths = {manifest_path} | {
            item["tsv_destination_path"]
            for item in manifest.get("worksheets", [])
            if isinstance(item, Mapping) and isinstance(item.get("tsv_destination_path"), str)
        }
        source_drive_id = manifest.get("source_drive_id")
        source_sha256 = manifest.get("source_sha256")
        source_bytes = manifest.get("source_byte_length")
        study_id = PurePosixPath(manifest_path).parts[1]
        native_mappings = {
            row.get("git_path"): row
            for row in mapping_rows
            if row.get("drive_id") == source_drive_id
            and isinstance(row.get("transformation"), str)
            and (
                row["transformation"] == NATIVE_SHEET_TRANSFORMATION
                or row["transformation"].startswith(
                    NATIVE_SHEET_TRANSFORMATION + "_AND_"
                )
            )
        }
        if set(native_mappings) != expected_paths:
            errors.append(
                f"native-sheet drive-to-git closure failure: {manifest_path}; "
                f"missing={sorted(expected_paths - set(native_mappings))}, "
                f"extra={sorted(set(native_mappings) - expected_paths)}"
            )
        native_source_paths = {
            row.get("source_path")
            for row in native_mappings.values()
            if isinstance(row.get("source_path"), str)
        }
        native_source_path = (
            next(iter(native_source_paths)) if len(native_source_paths) == 1 else None
        )
        if native_source_path is None:
            errors.append(
                f"native-sheet mappings must bind one source_path: {manifest_path}"
            )
        for path, row in native_mappings.items():
            if row.get("source_sha256") != source_sha256:
                errors.append(f"native-sheet source SHA-256 crosswalk drift: {path}")
            if row.get("source_bytes") != source_bytes:
                errors.append(f"native-sheet source byte-length crosswalk drift: {path}")
            if row.get("source_revision") != manifest.get("source_drive_revision"):
                errors.append(f"native-sheet source revision crosswalk drift: {path}")
            if row.get("study_id") != study_id:
                errors.append(f"native-sheet study scope crosswalk drift: {path}")
        native_results = {
            row.get("destination_path"): row
            for row in result_rows
            if row.get("drive_id") == source_drive_id
            and row.get("result") == "MATERIALIZED_AND_HASH_VERIFIED"
            and isinstance(row.get("transformation"), str)
            and (
                row["transformation"] == NATIVE_SHEET_TRANSFORMATION
                or row["transformation"].startswith(
                    NATIVE_SHEET_TRANSFORMATION + "_AND_"
                )
            )
        }
        native_plans = {
            row.get("destination_path"): row
            for row in plan_rows
            if row.get("drive_id") == source_drive_id
            and isinstance(row.get("decision"), str)
            and row["decision"].startswith("MIGRATE_")
            and isinstance(row.get("transformation"), str)
            and (
                row["transformation"] == NATIVE_SHEET_TRANSFORMATION
                or row["transformation"].startswith(
                    NATIVE_SHEET_TRANSFORMATION + "_AND_"
                )
            )
        }
        if set(native_results) != expected_paths:
            errors.append(f"native-sheet materialization-result closure failure: {manifest_path}")
        if set(native_plans) != expected_paths:
            errors.append(f"native-sheet path-plan closure failure: {manifest_path}")
        for leg_label, records in (("result", native_results), ("plan", native_plans)):
            for path, row in records.items():
                if (
                    row.get("source_sha256") != source_sha256
                    or row.get("source_bytes") != source_bytes
                    or row.get("source_revision") != manifest.get("source_drive_revision")
                    or row.get("study_id") != study_id
                ):
                    errors.append(
                        f"native-sheet {leg_label} source/scope binding drift: {path}"
                    )
        references = [
            row
            for row in result_rows
            if row.get("drive_id") == source_drive_id
            and row.get("result") == "REFERENCE_VERIFIED_NOT_MATERIALIZED"
        ]
        if len(references) != 1:
            errors.append(f"native-sheet XLSX reference result count must equal one: {manifest_path}")
        elif (
            references[0].get("source_sha256") != source_sha256
            or references[0].get("source_bytes") != source_bytes
            or references[0].get("source_revision")
            != manifest.get("source_drive_revision")
            or references[0].get("source_path") != native_source_path
            or references[0].get("terminal_action") != "REFERENCE_DRIVE"
            or references[0].get("transformation") != NATIVE_SHEET_REFERENCE_TRANSFORMATION
        ):
            errors.append(f"native-sheet XLSX reference result binding drift: {manifest_path}")
        reference_plans_for_source = [
            row
            for row in plan_rows
            if row.get("drive_id") == source_drive_id and row.get("decision") == "REFERENCE_DRIVE"
        ]
        if len(reference_plans_for_source) != 1:
            errors.append(f"native-sheet XLSX reference plan count must equal one: {manifest_path}")
        elif (
            reference_plans_for_source[0].get("transformation")
            != NATIVE_SHEET_REFERENCE_TRANSFORMATION
            or reference_plans_for_source[0].get("source_sha256") != source_sha256
            or reference_plans_for_source[0].get("source_bytes") != source_bytes
            or reference_plans_for_source[0].get("source_revision")
            != manifest.get("source_drive_revision")
            or reference_plans_for_source[0].get("source_path") != native_source_path
        ):
            errors.append(f"native-sheet XLSX reference plan binding drift: {manifest_path}")
    return errors


def validate_current_domain(
    root: Path,
    snapshot: GitSnapshot,
    require_schema: bool,
    authority: AuthorityGraph | None = None,
) -> list[str]:
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
        if authority is None:
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


def _reconstruction_target_commit(root: Path, kind: str, commit: str | None) -> str | None:
    if kind == "commit":
        return commit
    try:
        return run_git(root, "rev-parse", "--verify", "-q", "HEAD^{commit}").decode("ascii").strip()
    except DomainError:
        return None


def _reconstruction_integration_base(root: Path, target: str | None, kind: str) -> str | None:
    """Return the published history the validated change is compared against.

    For a branch this is the merge base with current main. An exact commit that
    main already contains (the push audit of an integration, where the audit
    fetches the updated main) is compared with its first parent, the pre-merge
    main, so the integrated delta is still checked.
    """

    main_commit = _run_closure_base_commit(root)
    if main_commit is None or target is None:
        return None
    base = run_git(root, "merge-base", target, main_commit).decode("ascii").strip()
    if kind == "commit" and base == target:
        try:
            return run_git(root, "rev-parse", "--verify", "-q", f"{target}^1^{{commit}}").decode(
                "ascii"
            ).strip()
        except DomainError:
            return None
    return base


def _reconstruction_delta_paths(root: Path, kind: str, base: str, commit: str | None) -> set[str]:
    if kind == "commit":
        args = ["diff", "--name-only", "--no-renames", "-z", base, str(commit), "--"]
    elif kind == "index":
        args = ["diff", "--cached", "--name-only", "--no-renames", "-z", base, "--"]
    else:
        args = ["diff", "--name-only", "--no-renames", "-z", base, "--"]
    paths = set(_git_paths(root, *args))
    if kind == "worktree":
        paths.update(_git_paths(root, "ls-files", "--others", "--exclude-standard", "-z"))
    return paths


def validate_reconstruction_domain(
    root: Path,
    snapshot: GitSnapshot,
    kind: str,
    commit: str | None,
    authority: AuthorityGraph | None = None,
) -> tuple[list[str], list[str]]:
    """Validate the production capability registry; return errors and notices.

    Historical validity is always blocking. Effective currentness blocks only
    records this change adds or transitions; an untouched assessment made stale
    by later integrated evidence is reported for evaluator reconciliation and
    never obstructs unrelated analytical or discovery publication.
    """

    errors: list[str] = []
    notices: list[str] = []
    phase, policy_errors = load_reconstruction_policy(snapshot)
    errors.extend(policy_errors)
    registry = snapshot.get(RECONSTRUCTION_REGISTRY_PATH)
    output = snapshot.get(RECONSTRUCTION_INDEX_PATH)
    schema_entry = snapshot.get(RECONSTRUCTION_SCHEMA_PATH)
    if registry is None or not registry.qualifies_as_evidence:
        errors.append(f"production capability registry is missing: {RECONSTRUCTION_REGISTRY_PATH}")
    if output is None or not output.qualifies_as_evidence:
        errors.append(f"generated reconstruction index is missing: {RECONSTRUCTION_INDEX_PATH}")
    if schema_entry is None or not schema_entry.qualifies_as_evidence:
        errors.append(f"reconstruction capability schema is missing: {RECONSTRUCTION_SCHEMA_PATH}")
    if registry is None or schema_entry is None or not registry.qualifies_as_evidence:
        return errors, notices
    try:
        records_with_lines = decode_reconstruction_registry(
            registry.data, f"{snapshot.identity}:{RECONSTRUCTION_REGISTRY_PATH}"
        )
        schema = decode_json(schema_entry.data, RECONSTRUCTION_SCHEMA_PATH)
        if not isinstance(schema, dict):
            raise DomainError("reconstruction capability schema is not a JSON object")
        validate_schema_document(schema, "reconstruction capability schema")
    except DomainError as exc:
        return errors + [str(exc)], notices
    diagnostics = []
    for line_number, record in records_with_lines:
        diagnostics.extend(
            schema_diagnostics(record, schema, RECONSTRUCTION_REGISTRY_PATH, line_number=line_number)
        )
    schema_failures = render_schema_diagnostics(diagnostics)
    if schema_failures:
        return errors + schema_failures, notices
    assessments = [record for _line_number, record in records_with_lines]
    for record in assessments:
        status = record["assessment_status"]
        if status == "UNASSESSED":
            errors.append(
                f"{record['assessment_id']}: the production registry does not admit UNASSESSED "
                "placeholders; eligible-but-unassessed state is derived from discovery"
            )
        if status == "REVIEWED" and phase != "ROUTINE":
            errors.append(
                f"{record['assessment_id']}: REVIEWED publication requires the ROUTINE phase "
                "after owner-accepted calibration"
            )
    target = _reconstruction_target_commit(root, kind, commit)
    try:
        base = _reconstruction_integration_base(root, target, kind)
    except DomainError as exc:
        return errors + [f"unable to determine the reconstruction integration base: {exc}"], notices
    if base is None and assessments:
        errors.append(
            "reconstruction validation needs refs/remotes/origin/main to bind basis commits "
            "and published history; fetch main first"
        )
    current_records: list[dict[str, Any]] = []
    discovery_entry = snapshot.get("characters/registry.jsonl")
    if discovery_entry is not None:
        try:
            current_records = [
                record
                for _line_number, record in decode_jsonl_with_lines(
                    discovery_entry.data, f"{snapshot.identity}:characters/registry.jsonl"
                )
            ]
        except DomainError as exc:
            errors.append(str(exc))
    evaluation = evaluate_reconstruction_assessments(
        assessments,
        root,
        comparison=snapshot,
        comparison_records=current_records,
        comparison_authority=authority,
        basis_ancestor_of=base,
    )
    errors.extend(evaluation.errors)
    base_records: list[dict[str, Any]] = []
    if base is not None:
        try:
            base_snapshot = GitSnapshot.from_commit(root, base, paths={RECONSTRUCTION_REGISTRY_PATH})
            base_entry = base_snapshot.get(RECONSTRUCTION_REGISTRY_PATH)
            if base_entry is not None:
                base_records = [
                    record
                    for _line_number, record in decode_reconstruction_registry(
                        base_entry.data, f"{base}:{RECONSTRUCTION_REGISTRY_PATH}"
                    )
                ]
        except DomainError as exc:
            errors.append(f"unable to read the published capability registry at {base}: {exc}")
    touched, change_errors = reconstruction_registry_changes(base_records, assessments)
    errors.extend(change_errors)
    for index in sorted(evaluation.currentness):
        item = evaluation.currentness[index]
        if item.effectively_current or item.recorded_status not in {"CANDIDATE", "REVIEWED"}:
            continue
        detail = f"{item.assessment_id} ({item.recorded_status}): {', '.join(item.reasons)}"
        if item.assessment_id in touched:
            errors.append(
                f"newly published or transitioned assessment is not effectively current: {detail}"
            )
        else:
            notices.append(
                f"recorded assessment is effectively stale pending evaluator reconciliation: {detail}"
            )
    if base is not None:
        try:
            changed = _reconstruction_delta_paths(root, kind, base, commit)
        except DomainError as exc:
            errors.append(f"unable to determine the reconstruction delta: {exc}")
            changed = set()
        if (
            changed & RECONSTRUCTION_OUTPUTS
            and changed - RECONSTRUCTION_OUTPUTS
            and RECONSTRUCTION_POLICY_PATH not in changed
        ):
            errors.append(
                "reconstruction production outputs must change alone; other changed paths: "
                + str(sorted(changed - RECONSTRUCTION_OUTPUTS, key=lambda item: item.encode("utf-8")))
            )
    if output is not None and not evaluation.errors:
        try:
            rendered = render_reconstruction_index(assessments, evaluation.basis_entries)
            if output.data != rendered.encode("utf-8"):
                errors.append(f"{RECONSTRUCTION_INDEX_PATH} is out of date")
        except (DomainError, KeyError, ValueError) as exc:
            errors.append(f"unable to render the reconstruction index: {exc}")
    return errors, notices


def validate_discovery_branch_confinement(root: Path, kind: str, commit: str | None) -> list[str]:
    """Bound a `character-registry` delta to the two discovery outputs.

    Applied only to the curation agent's continuing branch: coordinated
    pre-merge repairs on analytical branches legitimately carry the same two
    files beside their analytical root and are confined by housekeeping and the
    integration controller instead.
    """

    target = _reconstruction_target_commit(root, kind, commit)
    try:
        base = _reconstruction_integration_base(root, target, kind)
    except DomainError as exc:
        return [f"unable to determine the discovery branch base: {exc}"]
    if base is None:
        return [
            "discovery branch confinement needs refs/remotes/origin/main; fetch main first"
        ]
    try:
        changed = _reconstruction_delta_paths(root, kind, base, commit)
    except DomainError as exc:
        return [f"unable to determine the discovery branch delta: {exc}"]
    extra = sorted(changed - DISCOVERY_OUTPUTS, key=lambda item: item.encode("utf-8"))
    if extra:
        return [
            "character-registry delta may contain only characters/registry.jsonl and "
            f"CHARACTER_ANALYSIS_INDEX.md; other changed paths: {extra}"
        ]
    return []


def discovery_branch_candidate(root: Path, kind: str, commit: str | None) -> bool:
    """Whether the audited commit is unmerged `character-registry` history.

    Identity comes from the fetched live branch ref, so every audit of such a
    commit is confined whichever event started it, including an exact-commit
    repository dispatch whose run context names `main`.
    """

    target = _reconstruction_target_commit(root, kind, commit)
    if target is None:
        return False
    try:
        tip = run_git(root, "rev-parse", "--verify", "-q", DISCOVERY_BRANCH_REF + "^{commit}").decode(
            "ascii"
        ).strip()
    except DomainError:
        return False
    if not is_ancestor_commit(root, target, tip):
        return False
    main_commit = _run_closure_base_commit(root)
    return not (main_commit is not None and is_ancestor_commit(root, target, main_commit))


def discovery_confinement_errors(
    root: Path, kind: str, commit: str | None, *, requested: bool
) -> list[str]:
    """Apply confinement when requested explicitly or the commit is curation history."""

    try:
        applies = requested or discovery_branch_candidate(root, kind, commit)
    except DomainError as exc:
        return [f"unable to determine whether the audited commit is curation history: {exc}"]
    return validate_discovery_branch_confinement(root, kind, commit) if applies else []


def validate_routing_branch_scope(root: Path, kind: str, commit: str | None, branch: str) -> list[str]:
    """Bound a series/study branch delta to its own root and the shared outputs.

    The routing preflight applies this so a passing analysis-branch audit is
    integration-ready without a separate housekeeping certification. A commit
    already contained in main has nothing left to integrate.
    """

    if not re.fullmatch(r"(series|studies)/[a-z0-9][a-z0-9-]*", branch):
        return [f"routing preflight requires a series/study branch: {branch}"]
    target = _reconstruction_target_commit(root, kind, commit)
    main_commit = _run_closure_base_commit(root)
    if target is None or main_commit is None:
        return ["analysis branch scope needs the audited commit and refs/remotes/origin/main"]
    try:
        base = run_git(root, "merge-base", target, main_commit).decode("ascii").strip()
        if kind == "commit" and base == target:
            return []
        changed = _reconstruction_delta_paths(root, kind, base, commit)
    except DomainError as exc:
        return [f"unable to determine the analysis branch delta: {exc}"]
    allowed = set(ROUTING_OUTPUTS) | set(DISCOVERY_OUTPUTS)
    extra = sorted(
        (path for path in changed if path not in allowed and not path.startswith(branch + "/")),
        key=lambda item: item.encode("utf-8"),
    )
    if extra:
        return [
            f"{branch} may change only its own root, the five routing outputs and the two "
            f"discovery outputs; other changed paths: {extra}"
        ]
    return []


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
    parser.add_argument("--routing-preflight", metavar="ANALYTICAL_BRANCH")
    parser.add_argument(
        "--discovery-branch-confinement",
        action="store_true",
        help="require the delta against main to contain only the two discovery outputs",
    )
    parser.add_argument("--result-json", type=Path)
    parser.add_argument("--timings-json", type=Path)
    parser.add_argument("--repo", type=Path)
    args = parser.parse_args()
    root = args.repo.resolve() if args.repo else Path(__file__).resolve().parents[1]
    kind = args.snapshot or ("commit" if args.phase == "g3" else "worktree")
    timer = AuditTimer()
    outcome = "failure"
    commit = args.commit
    timing_output = None
    try:
        if args.timings_json:
            timing_output = report_path(root, args.timings_json)
        if args.phase == "g3":
            commit = require_g3_selection(root, kind, commit, args.manifest is not None)
        elif kind == "commit" and commit is None:
            commit = run_git(root, "rev-parse", "HEAD").decode("ascii").strip()
        if args.routing_preflight and (
            args.phase != "current" or kind not in {"index", "commit"}
        ):
            raise DomainError("routing preflight requires a current Git index or exact commit")
        if args.discovery_branch_confinement and (
            args.phase != "current" or kind not in {"index", "commit"}
        ):
            raise DomainError("discovery branch confinement requires a current Git index or exact commit")
        snapshot, paths = timer.call("snapshot", choose_snapshot, root, kind, commit)
        deferred_routing: list[str] = []
        reconstruction_notices: list[str] = []
        policy = _policy_from_snapshot(snapshot)
        errors: list[str] = []
        if args.manifest:
            expected = read_external_manifest(args.manifest.resolve())
            errors.extend(validate_exact_set(paths, expected, args.phase))
        elif args.phase == "g3":
            expected = read_manifest_from_snapshot(snapshot, G3_MANIFEST)
            errors.extend(validate_exact_set(paths, expected, args.phase))
        errors.extend(timer.call("paths", validate_paths, snapshot, policy))
        errors.extend(timer.call("bytes", validate_bytes, snapshot, policy, args.phase))
        revision = identity_revision_for_snapshot(kind, commit)
        errors.extend(
            timer.call(
                "identities", validate_commit_identities, root, policy, revision,
                role_split=args.phase == "current",
            )
        )
        if args.routing_preflight:
            from analytical_preflight import routing_preflight

            snapshot, deferred_routing = timer.call("routing_preflight", routing_preflight, snapshot, args.routing_preflight)
            errors.extend(
                timer.call("routing_scope", validate_routing_branch_scope, root, kind, commit, args.routing_preflight)
            )
        if args.phase == "g3":
            errors.extend(timer.call("protected", validate_protected, snapshot))
        else:
            errors.extend(timer.call("protected", validate_protected, snapshot))
            errors.extend(timer.call("links", validate_markdown_links, snapshot))
            errors.extend(timer.call("audit_workflow", validate_audit_workflow, snapshot, policy))
            errors.extend(timer.call("housekeeping", validate_global_index_automation, snapshot, policy))
            errors.extend(timer.call("nightly_contract", validate_nightly_integration, snapshot))
            errors.extend(timer.call("whitespace_exceptions", validate_named_whitespace_exceptions, snapshot, policy))
            # One authority graph serves every consumer of this snapshot; each
            # builds its own only when called outside a validator run.
            authority = timer.call("authority_graph", AuthorityGraph, snapshot)
            baseline_commit = active_migration_baseline_commit(snapshot)
            errors.extend(timer.call("authority_scope", validate_active_authority_scope, snapshot, baseline_commit))
            errors.extend(
                timer.call("crosswalk", validate_crosswalk_closure, snapshot, baseline_commit=baseline_commit)
            )
            errors.extend(timer.call("native_sheets", validate_native_sheets, snapshot, True))
            errors.extend(timer.call("series_registry", validate_series_registry, snapshot, authority))
            errors.extend(timer.call("missing_entrypoints", validate_missing_entrypoint_allowlist, snapshot, policy))
            errors.extend(timer.call("study_registry", validate_study_registry, snapshot, authority))
            errors.extend(timer.call("root_topology", validate_registered_root_topology, snapshot))
            errors.extend(timer.call("obligations", validate_change_obligations, snapshot))
            project_gate_control, project_gate_control_errors = (
                _load_project_initiation_gate(snapshot)
            )
            errors.extend(project_gate_control_errors)
            if project_gate_control is not None:
                try:
                    errors.extend(
                        timer.call("project_initiation", validate_project_initiation_gate,
                            snapshot,
                            project_initiation_baseline_paths(
                                root, project_gate_control
                            ),
                            project_gate_control,
                            authority,
                        )
                    )
                except DomainError as exc:
                    errors.append(str(exc))
            errors.extend(timer.call("character_domain", validate_current_domain, root, snapshot, True, authority))
            generator_snapshot = "commit" if kind == "commit" else kind
            errors.extend(timer.call("character_render", validate_generated_index, snapshot, generator_snapshot, authority))
            reconstruction_errors, reconstruction_notices = timer.call(
                "reconstruction", validate_reconstruction_domain, root, snapshot, kind, commit, authority
            )
            errors.extend(reconstruction_errors)
            if args.phase == "current" and kind in {"index", "commit"}:
                errors.extend(
                    timer.call(
                        "discovery_confinement",
                        discovery_confinement_errors,
                        root,
                        kind,
                        commit,
                        requested=args.discovery_branch_confinement,
                    )
                )
            if not deferred_routing:
                errors.extend(
                    timer.call("catalog_render", validate_generated_repository_indexes, snapshot)
                )
        if errors:
            for error in sorted(set(errors), key=lambda item: item.encode("utf-8")):
                print(f"FAIL: {error}")
            return 1
        if args.result_json:
            args.result_json.write_text(
                json.dumps({
                    "audited_commit": commit,
                    "integration_state": "pending" if deferred_routing else "success",
                    "deferred_routing_paths": deferred_routing,
                    "reconstruction_currentness_notices": reconstruction_notices,
                }) + "\n",
                encoding="utf-8",
            )
        outcome = "pending" if deferred_routing else "success"
        for notice in reconstruction_notices:
            print(f"NOTICE: {notice}")
        if deferred_routing:
            print(
                f"AWAITING_SYNCHRONIZATION: source={snapshot.identity} paths={deferred_routing}; "
                "authored content passed; the projected routing bytes are not committed"
            )
            return 0
        print(
            f"PASS: phase={args.phase} snapshot={snapshot.identity} "
            f"paths={len(paths)}"
        )
        return 0
    except (DomainError, OSError, ValueError) as exc:
        print(f"FAIL: {exc}")
        return 1
    finally:
        if timing_output:
            write_report(root, timing_output, {
                "schema": "repository-audit-timing/v1", "audited_commit": commit,
                "snapshot": kind, "outcome": outcome, **timer.report(),
            })


if __name__ == "__main__":
    raise SystemExit(main())
