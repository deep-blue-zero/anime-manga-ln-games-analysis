#!/usr/bin/env python3
"""Derive reconstruction currentness and evaluator work from exact Git state.

``currentness`` is the consumer verification route: it reports whether each
recorded assessment still applies to one exact snapshot. ``work-queue`` is the
evaluator's Git-derived work discovery, including the advisory analysis
frontier: current analysis that has grown around an assessed subject since the
assessment's basis without touching its evidence. Neither mode writes files,
and neither depends on another agent's private checkpoint or on advisory
referrals.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from pathlib import Path
from typing import Any, Mapping, Sequence

from character_index_core import (
    CURRENT_CLAIM_STATUSES,
    RECONSTRUCTION_REGISTRY_PATH,
    AuthorityGraph,
    DomainError,
    GitSnapshot,
    ReconstructionEvaluation,
    coverage_projection,
    decode_reconstruction_registry,
    discovery_commit_snapshot,
    evaluate_reconstruction_assessments,
    is_ancestor_commit,
    load_discovery_snapshot_records,
    read_blob_objects,
    read_discovery_registry,
    reviewed_evidence_membership,
    run_git,
    subject_scope_projection,
)


WORK_TIERS = {
    "EFFECTIVELY_STALE_ASSESSMENT": 1,
    "REASSESSMENT_NEEDED": 2,
    "NEWLY_ELIGIBLE": 3,
    "BACKFILL_UNASSESSED": 4,
    "DEFERRED_EVIDENCE_CHANGED": 5,
    "ANALYSIS_FRONTIER_ADVANCED": 6,
}

# One file must gain this many mentions of a subject before the frontier counts
# it. Mention growth only finds work; it is never evidence or readiness.
DEFAULT_FRONTIER_MIN_MENTIONS = 10
# Kana and Han names are written without word spacing, so they match anywhere.
_UNSPACED_SCRIPT = re.compile("[\u3040-\u30ff\u3400-\u4dbf\u4e00-\u9fff\uf900-\ufaff\uff66-\uff9f]")
_NAME_SEPARATORS = re.compile(r"[\s\u30fb\uff65(),]+")


def _snapshot(root: Path, mode: str, commit: str | None) -> GitSnapshot:
    if mode == "commit":
        if commit is None:
            raise DomainError("--commit is required with --snapshot commit")
        return GitSnapshot.from_commit(root, commit)
    if commit is not None:
        raise DomainError("--commit is valid only with --snapshot commit")
    return GitSnapshot.from_index(root)


def load_state(
    snapshot: GitSnapshot, repository: Path
) -> tuple[list[dict[str, Any]], list[dict[str, Any]], ReconstructionEvaluation]:
    registry = snapshot.get(RECONSTRUCTION_REGISTRY_PATH)
    if registry is None or not registry.qualifies_as_evidence:
        raise DomainError(f"snapshot lacks the production registry: {RECONSTRUCTION_REGISTRY_PATH}")
    assessments = [
        record
        for _line, record in decode_reconstruction_registry(
            registry.data, f"{snapshot.identity}:{RECONSTRUCTION_REGISTRY_PATH}"
        )
    ]
    discovery = load_discovery_snapshot_records(snapshot)
    evaluation = evaluate_reconstruction_assessments(
        assessments, repository, comparison=snapshot, comparison_records=discovery
    )
    return assessments, discovery, evaluation


def currentness_report(
    assessments: Sequence[Mapping[str, Any]], evaluation: ReconstructionEvaluation
) -> list[dict[str, Any]]:
    rows = [evaluation.currentness[index].as_json() for index in sorted(evaluation.currentness)]
    return sorted(rows, key=lambda row: row["assessment_id"].encode("ascii"))


def _discovery_at(repository: Path, commit: str) -> dict[str, Mapping[str, Any]]:
    return _records_by_subject(discovery_commit_snapshot(repository, commit))


def _material_discovery_change(before: Mapping[str, Any], after: Mapping[str, Any]) -> bool:
    return (
        subject_scope_projection(before) != subject_scope_projection(after)
        or before.get("curation_status") != after.get("curation_status")
        or coverage_projection(before) != coverage_projection(after)
        or reviewed_evidence_membership(before) != reviewed_evidence_membership(after)
    )


def _records_by_subject(snapshot: GitSnapshot) -> dict[str, Mapping[str, Any]]:
    """Discovery rows by subject in either storage layout; empty before the registry existed."""

    return {
        record["analysis_subject_id"]: record
        for record in read_discovery_registry(snapshot).records
        if isinstance(record.get("analysis_subject_id"), str)
    }


def _blob_fingerprint(snapshot: GitSnapshot, path: str) -> tuple[str, str] | None:
    entry = snapshot.get(path)
    if entry is None:
        return None
    return (entry.mode, hashlib.sha256(entry.data).hexdigest())


def deferred_evidence_changes(
    deferred: Sequence[str],
    discovery: Sequence[Mapping[str, Any]],
    since_records: Mapping[str, Mapping[str, Any]],
    since_snapshot: GitSnapshot,
    since_authority: AuthorityGraph,
    snapshot: GitSnapshot,
    authority: AuthorityGraph,
) -> dict[str, list[str]]:
    """Detect evidence changes that discovery metadata does not record.

    Only the reviewed evidence paths named on each deferred subject's discovery
    row, at the checkpoint or now, are compared. A changed blob or a changed
    authority classification (including one caused by another artifact's
    supersession edge) returns the subject to the queue; unrelated files never do.
    """

    now = {
        record["analysis_subject_id"]: record
        for record in discovery
        if isinstance(record.get("analysis_subject_id"), str)
    }
    result: dict[str, list[str]] = {}
    for subject in sorted(set(deferred), key=lambda value: value.encode("utf-8")):
        current, before = now.get(subject), since_records.get(subject)
        if current is None or before is None:
            continue
        paths = {
            item["repository_path"]
            for record in (current, before)
            for item in record.get("evidence", [])
            if isinstance(item, Mapping)
            and item.get("review_state") == "REVIEWED"
            and isinstance(item.get("repository_path"), str)
        }
        reasons: set[str] = set()
        for path in sorted(paths):
            if _blob_fingerprint(since_snapshot, path) != _blob_fingerprint(snapshot, path):
                reasons.add("EVIDENCE_BYTES_CHANGED_SINCE_CHECKPOINT")
            if since_authority.classification(path) != authority.classification(path):
                reasons.add("EVIDENCE_AUTHORITY_CHANGED_SINCE_CHECKPOINT")
        if reasons:
            result[subject] = sorted(reasons)
    return result


def subject_mention_pattern(record: Mapping[str, Any]) -> re.Pattern[str] | None:
    """Match a subject's registered names, or their distinctive parts, in analysis.

    Analysis usually names a character by one part of the registered name
    ("Julius" for "Julius Juukulius"), so the preferred name and each
    unambiguous alias contribute themselves and every part of at least three
    characters that is not a number and does not start in lower case (dropping
    particles such as "van"). Longer names win at the same position.
    """

    aliases = [*record.get("entity_aliases", []), *record.get("subject_aliases", [])]
    names = [record.get("preferred_name")] + [
        alias.get("value") for alias in aliases if isinstance(alias, Mapping) and alias.get("ambiguous") is False
    ]
    terms: set[str] = set()
    for name in names:
        if not isinstance(name, str) or not name.strip():
            continue
        terms.add(name)
        terms.update(
            part
            for part in _NAME_SEPARATORS.split(name)
            if len(part) >= 3 and not part[0].islower() and not part.isdigit()
        )
    if not terms:
        return None
    alternatives = [
        re.escape(term) if _UNSPACED_SCRIPT.search(term) else rf"(?<!\w){re.escape(term)}(?!\w)"
        for term in sorted(terms, key=lambda value: (-len(value), value))
    ]
    return re.compile("|".join(alternatives))


def _mention_count(pattern: re.Pattern[str], data: bytes) -> int:
    return sum(1 for _match in pattern.finditer(data.decode("utf-8", "replace")))


def _git_blob_id(data: bytes, length: int) -> str:
    digest = hashlib.new("sha1" if length == 40 else "sha256")
    digest.update(b"blob " + str(len(data)).encode("ascii") + b"\0")
    digest.update(data)
    return digest.hexdigest()


def _tree_blobs(root: Path, commit: str, roots: Sequence[str]) -> dict[str, tuple[str, str]]:
    """Mode and object ID of every blob under ``roots`` at ``commit``, without reading content."""

    raw = run_git(root, "--literal-pathspecs", "ls-tree", "-r", "-z", "--full-tree", commit, "--", *roots)
    blobs: dict[str, tuple[str, str]] = {}
    for item in raw.split(b"\0"):
        if not item:
            continue
        metadata, raw_path = item.split(b"\t", 1)
        mode, kind, oid = metadata.decode("ascii").split(" ")
        if kind == "blob":
            blobs[raw_path.decode("utf-8", "strict")] = (mode, oid)
    return blobs


def analysis_frontier(
    root: Path,
    snapshot: GitSnapshot,
    authority: AuthorityGraph,
    assessments: Sequence[Mapping[str, Any]],
    discovery: Sequence[Mapping[str, Any]],
    evaluation: ReconstructionEvaluation,
    *,
    since: str | None = None,
    deferred: Sequence[str] = (),
    min_mentions: int = DEFAULT_FRONTIER_MIN_MENTIONS,
) -> dict[str, list[dict[str, Any]]]:
    """Find current analysis that has grown around an effectively current claim.

    Currentness compares only a claim's discovery row and cited evidence, so a
    later volume reading or ledger entry about the subject leaves the claim
    current. For each effectively current claim this compares the files under
    the subject's reviewed evidence roots (``series/<slug>`` or
    ``studies/<slug>``) between the claim's ``basis_commit`` and the snapshot.
    A file counts when it is current authority and gained at least
    ``min_mentions`` matches of the subject's registered names; a changed cited
    file already makes its claim stale, so it never reaches this check. For a
    deferred subject the checkpoint replaces the basis when it is later, so a
    reviewed frontier returns only after further growth. The result never
    affects currentness; it is work discovery only.
    """

    if min_mentions < 1:
        raise DomainError("frontier mention threshold must be at least 1")
    records = {
        record["analysis_subject_id"]: record
        for record in discovery
        if isinstance(record.get("analysis_subject_id"), str)
    }
    deferred_set = set(deferred)
    trees: dict[tuple[str, tuple[str, ...]], dict[str, tuple[str, str]]] = {}
    blob_cache: dict[str, bytes] = {}
    patterns: dict[str, re.Pattern[str] | None] = {}
    result: dict[str, list[dict[str, Any]]] = {}
    for index in sorted(evaluation.currentness):
        state = evaluation.currentness[index]
        record = records.get(state.analysis_subject_id)
        if not state.effectively_current or record is None:
            continue
        subject = state.analysis_subject_id
        if subject not in patterns:
            patterns[subject] = subject_mention_pattern(record)
        pattern = patterns[subject]
        roots = tuple(
            sorted(
                {
                    "/".join(item["repository_path"].split("/")[:2])
                    for item in record.get("evidence", [])
                    if isinstance(item, Mapping)
                    and item.get("review_state") == "REVIEWED"
                    and isinstance(item.get("repository_path"), str)
                    and item["repository_path"].startswith(("series/", "studies/"))
                    and item["repository_path"].count("/") >= 2
                }
            )
        )
        if pattern is None or not roots:
            continue
        basis = assessments[index]["assessment_scope"]["basis_commit"]
        base, base_kind = basis, "BASIS"
        if subject in deferred_set and since is not None and since != basis and is_ancestor_commit(root, basis, since):
            base, base_kind = since, "CHECKPOINT"
        if (base, roots) not in trees:
            trees[(base, roots)] = _tree_blobs(root, base, roots)
        before = trees[(base, roots)]
        # A path new since the base may be a moved file. Its baseline is the
        # departed content: identical bytes are no growth, and a departed file
        # of the same unique name is compared as the earlier version.
        departed = {path: oid for path, (_mode, oid) in before.items() if path not in snapshot.entries}
        departed_ids = set(departed.values())
        departed_names: dict[str, str | None] = {}
        for path, oid in departed.items():
            name = path.rsplit("/", 1)[-1]
            departed_names[name] = None if name in departed_names else oid
        prefixes = tuple(item + "/" for item in roots)
        grown: list[tuple[str, int, str | None]] = []
        for path in sorted(snapshot.entries):
            if not path.startswith(prefixes) or not authority.current_eligible(path):
                continue
            entry = snapshot.entries[path]
            blob_id = _git_blob_id(entry.data, len(base))
            previous = before.get(path)
            if previous == (entry.mode, blob_id):
                continue
            if previous is not None:
                baseline: str | None = previous[1]
            elif blob_id in departed_ids:
                continue
            else:
                baseline = departed_names.get(path.rsplit("/", 1)[-1])
            mentions = _mention_count(pattern, entry.data)
            if mentions >= min_mentions:
                grown.append((path, mentions, baseline))
        earlier = read_blob_objects(root, (oid for _path, _count, oid in grown if oid is not None), cache=blob_cache)
        paths = []
        for path, mentions, oid in grown:
            growth = mentions - (0 if oid is None else _mention_count(pattern, earlier[oid]))
            if growth >= min_mentions:
                paths.append({"mention_growth": growth, "repository_path": path})
        if paths:
            paths.sort(key=lambda item: (-item["mention_growth"], item["repository_path"].encode("utf-8")))
            result.setdefault(subject, []).append(
                {
                    "assessment_id": state.assessment_id,
                    "base": base_kind,
                    "base_commit": base,
                    "paths": paths,
                }
            )
    return result


def work_queue(
    assessments: Sequence[Mapping[str, Any]],
    discovery: Sequence[Mapping[str, Any]],
    evaluation: ReconstructionEvaluation,
    *,
    since_records: Mapping[str, Mapping[str, Any]] | None = None,
    deferred: Sequence[str] = (),
    deferred_changes: Mapping[str, Sequence[str]] | None = None,
    hints: Sequence[str] = (),
    frontier: Mapping[str, Sequence[Mapping[str, Any]]] | None = None,
) -> dict[str, Any]:
    """Prioritize evaluator work by exact subject from Git-derived state only.

    Work is keyed by ``analysis_subject_id``; each subject appears at most once
    with every applicable reason merged. Advisory hints only annotate existing
    work and never create it. ``deferred`` is the evaluator's own checkpoint
    list; a deferred subject returns to the queue after a material discovery
    change since ``since_records`` or an evidence change in ``deferred_changes``
    (see ``deferred_evidence_changes``). ``frontier`` (see
    ``analysis_frontier``) queues a subject whose claims all still apply at the
    lowest tier, without changing its state.
    """

    by_subject: dict[str, list[int]] = {}
    for index, assessment in enumerate(assessments):
        subject = assessment.get("analysis_subject_id")
        if isinstance(subject, str):
            by_subject.setdefault(subject, []).append(index)
    discovery_by_subject = {
        record["analysis_subject_id"]: record
        for record in discovery
        if isinstance(record.get("analysis_subject_id"), str)
    }
    hint_set = set(hints)
    deferred_set = set(deferred)
    items: dict[str, dict[str, Any]] = {}
    states: dict[str, str] = {}

    def add(subject: str, kind: str, reasons: Sequence[str] = ()) -> None:
        item = items.get(subject)
        if item is None or WORK_TIERS[kind] < item["tier"]:
            previous = item["reasons"] if item else []
            items[subject] = {
                "advisory_hint": subject in hint_set,
                "analysis_subject_id": subject,
                "kind": kind,
                "reasons": sorted(set(previous) | set(reasons)),
                "tier": WORK_TIERS[kind],
            }
        else:
            item["reasons"] = sorted(set(item["reasons"]) | set(reasons))

    for subject in sorted(set(by_subject) | set(discovery_by_subject), key=lambda s: s.encode("ascii")):
        record = discovery_by_subject.get(subject)
        indexes = by_subject.get(subject, [])
        claims = [index for index in indexes if assessments[index].get("assessment_status") in CURRENT_CLAIM_STATUSES]
        stale_claims = [
            index for index in claims
            if index in evaluation.currentness and not evaluation.currentness[index].effectively_current
        ]
        changed_since = bool(
            since_records is not None
            and record is not None
            and subject in since_records
            and _material_discovery_change(since_records[subject], record)
        )
        if stale_claims:
            reasons = sorted({reason for index in stale_claims for reason in evaluation.currentness[index].reasons})
            add(subject, "EFFECTIVELY_STALE_ASSESSMENT", reasons)
            states[subject] = "EFFECTIVELY_STALE"
        elif claims:
            reviewed = any(assessments[index].get("assessment_status") == "REVIEWED" for index in claims)
            states[subject] = "HUMAN_REVIEWED_CURRENT" if reviewed else "PENDING_PROVISIONAL"
            advanced = (frontier or {}).get(subject)
            if advanced:
                add(
                    subject,
                    "ANALYSIS_FRONTIER_ADVANCED",
                    sorted({f"SUBJECT_ANALYSIS_GREW_SINCE_{claim['base']}" for claim in advanced}),
                )
                items[subject]["frontier"] = [dict(claim) for claim in advanced]
        elif indexes:
            if record is not None and record.get("curation_status") == "INCLUDED":
                add(subject, "REASSESSMENT_NEEDED", ["NO_CURRENT_CLAIM_AFTER_HISTORICAL_ASSESSMENT"])
            states[subject] = "HISTORICAL_ONLY"
        elif record is not None and record.get("curation_status") == "INCLUDED":
            if subject in deferred_set:
                states[subject] = "DEFERRED"
                reasons = list((deferred_changes or {}).get(subject, ()))
                if changed_since:
                    reasons.append("DISCOVERY_CHANGED_SINCE_CHECKPOINT")
                if reasons:
                    add(subject, "DEFERRED_EVIDENCE_CHANGED", reasons)
            elif since_records is not None and subject not in since_records:
                add(subject, "NEWLY_ELIGIBLE", ["ENROLLED_SINCE_CHECKPOINT"])
                states[subject] = "ELIGIBLE_UNASSESSED"
            else:
                add(subject, "BACKFILL_UNASSESSED")
                states[subject] = "ELIGIBLE_UNASSESSED"
    ordered = sorted(items.values(), key=lambda item: (item["tier"], item["analysis_subject_id"].encode("ascii")))
    counts: dict[str, int] = {}
    for state in states.values():
        counts[state] = counts.get(state, 0) + 1
    return {
        "items": ordered,
        "subject_state_counts": dict(sorted(counts.items())),
        "unenrolled_hints": sorted(
            (hint for hint in hint_set if hint not in discovery_by_subject),
            key=lambda value: value.encode("utf-8"),
        ),
    }


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("mode", choices=["currentness", "work-queue"])
    parser.add_argument("--repo", type=Path)
    parser.add_argument("--snapshot", choices=["index", "commit"], default="commit")
    parser.add_argument("--commit")
    parser.add_argument("--assessment", action="append", default=[], help="limit currentness to these IDs")
    parser.add_argument(
        "--require-current-reviewed",
        action="store_true",
        help=(
            "exit 1 unless the selection is nonempty and every selected assessment "
            "is CURRENT_REVIEWED; an empty selection never certifies readiness"
        ),
    )
    parser.add_argument("--since", help="full commit of the last verified evaluator checkpoint")
    parser.add_argument("--deferred", action="append", default=[], help="subject deferred in the evaluator checkpoint")
    parser.add_argument("--hint", action="append", default=[], help="advisory referral subject; annotates only")
    parser.add_argument(
        "--frontier-min-mentions",
        type=int,
        default=DEFAULT_FRONTIER_MIN_MENTIONS,
        help="mentions of a subject one file must gain before the analysis frontier counts it",
    )
    args = parser.parse_args(argv)
    if args.deferred and not args.since:
        parser.error("--deferred requires --since, the checkpoint the deferral was recorded at")
    if args.frontier_min_mentions < 1:
        parser.error("--frontier-min-mentions must be at least 1")
    root = args.repo.resolve() if args.repo else Path(__file__).resolve().parents[1]
    snapshot = _snapshot(root, args.snapshot, args.commit)
    assessments, discovery, evaluation = load_state(snapshot, root)
    if evaluation.errors:
        for error in evaluation.errors:
            print(f"FAIL: {error}", file=sys.stderr)
        return 2
    output: dict[str, Any] = {"comparison": snapshot.identity}
    if args.mode == "currentness":
        rows = currentness_report(assessments, evaluation)
        if args.assessment:
            selected = set(args.assessment)
            missing = sorted(selected - {row["assessment_id"] for row in rows})
            if missing:
                print(f"FAIL: unknown assessment IDs: {missing}", file=sys.stderr)
                return 2
            rows = [row for row in rows if row["assessment_id"] in selected]
        output["assessments"] = rows
        certified = bool(rows) and all(row["effective_state"] == "CURRENT_REVIEWED" for row in rows)
        if args.require_current_reviewed:
            output["current_reviewed_certified"] = certified
        print(json.dumps(output, ensure_ascii=False, sort_keys=True, indent=2))
        if args.require_current_reviewed and not certified:
            if not rows:
                print(
                    "FAIL: no assessment was selected; an empty selection never certifies readiness",
                    file=sys.stderr,
                )
            return 1
        return 0
    since_records = None
    deferred_changes: dict[str, list[str]] = {}
    authority = AuthorityGraph(snapshot)
    if args.since and args.deferred:
        # One full checkpoint snapshot, only when deferred subjects need it.
        since_snapshot = GitSnapshot.from_commit(root, args.since)
        since_records = _records_by_subject(since_snapshot)
        deferred_changes = deferred_evidence_changes(
            args.deferred,
            discovery,
            since_records,
            since_snapshot,
            AuthorityGraph(since_snapshot),
            snapshot,
            authority,
        )
    elif args.since:
        since_records = _discovery_at(root, args.since)
    output["since"] = args.since
    output.update(
        work_queue(
            assessments,
            discovery,
            evaluation,
            since_records=since_records,
            deferred=args.deferred,
            deferred_changes=deferred_changes,
            hints=args.hint,
            frontier=analysis_frontier(
                root,
                snapshot,
                authority,
                assessments,
                discovery,
                evaluation,
                since=args.since,
                deferred=args.deferred,
                min_mentions=args.frontier_min_mentions,
            ),
        )
    )
    print(json.dumps(output, ensure_ascii=False, sort_keys=True, indent=2))
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except DomainError as exc:
        raise SystemExit(f"FAIL: {exc}") from exc
