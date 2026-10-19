#!/usr/bin/env python3
"""Derive reconstruction currentness and evaluator work from exact Git state.

``currentness`` is the consumer verification route: it reports whether each
recorded assessment still applies to one exact snapshot. ``work-queue`` is the
evaluator's Git-derived work discovery. Neither mode writes files, and neither
depends on another agent's private checkpoint or on advisory referrals.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any, Mapping, Sequence

from character_index_core import (
    CURRENT_CLAIM_STATUSES,
    DISCOVERY_INPUT_PATHS,
    RECONSTRUCTION_REGISTRY_PATH,
    DomainError,
    GitSnapshot,
    ReconstructionEvaluation,
    coverage_projection,
    decode_jsonl_with_lines,
    decode_reconstruction_registry,
    evaluate_reconstruction_assessments,
    load_discovery_snapshot_records,
    reviewed_evidence_membership,
    subject_scope_projection,
)


WORK_TIERS = {
    "EFFECTIVELY_STALE_ASSESSMENT": 1,
    "REASSESSMENT_NEEDED": 2,
    "NEWLY_ELIGIBLE": 3,
    "BACKFILL_UNASSESSED": 4,
    "DEFERRED_EVIDENCE_CHANGED": 5,
}


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
    selected = GitSnapshot.from_commit(
        repository, commit, paths={DISCOVERY_INPUT_PATHS["registry"]}
    )
    entry = selected.get(DISCOVERY_INPUT_PATHS["registry"])
    if entry is None:
        return {}
    return {
        record["analysis_subject_id"]: record
        for _line, record in decode_jsonl_with_lines(entry.data, f"{commit}:characters/registry.jsonl")
        if isinstance(record.get("analysis_subject_id"), str)
    }


def _material_discovery_change(before: Mapping[str, Any], after: Mapping[str, Any]) -> bool:
    return (
        subject_scope_projection(before) != subject_scope_projection(after)
        or before.get("curation_status") != after.get("curation_status")
        or coverage_projection(before) != coverage_projection(after)
        or reviewed_evidence_membership(before) != reviewed_evidence_membership(after)
    )


def work_queue(
    assessments: Sequence[Mapping[str, Any]],
    discovery: Sequence[Mapping[str, Any]],
    evaluation: ReconstructionEvaluation,
    *,
    since_records: Mapping[str, Mapping[str, Any]] | None = None,
    deferred: Sequence[str] = (),
    hints: Sequence[str] = (),
) -> dict[str, Any]:
    """Prioritize evaluator work by exact subject from Git-derived state only.

    Work is keyed by ``analysis_subject_id``; each subject appears at most once
    with every applicable reason merged. Advisory hints only annotate existing
    work and never create it. ``deferred`` is the evaluator's own checkpoint
    list; a deferred subject returns to the queue only after a material
    discovery change since ``since_records``.
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
        elif indexes:
            if record is not None and record.get("curation_status") == "INCLUDED":
                add(subject, "REASSESSMENT_NEEDED", ["NO_CURRENT_CLAIM_AFTER_HISTORICAL_ASSESSMENT"])
            states[subject] = "HISTORICAL_ONLY"
        elif record is not None and record.get("curation_status") == "INCLUDED":
            if subject in deferred_set:
                states[subject] = "DEFERRED"
                if changed_since:
                    add(subject, "DEFERRED_EVIDENCE_CHANGED", ["DISCOVERY_CHANGED_SINCE_CHECKPOINT"])
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
        help="exit 1 unless every selected assessment is CURRENT_REVIEWED",
    )
    parser.add_argument("--since", help="full commit of the last verified evaluator checkpoint")
    parser.add_argument("--deferred", action="append", default=[], help="subject deferred in the evaluator checkpoint")
    parser.add_argument("--hint", action="append", default=[], help="advisory referral subject; annotates only")
    args = parser.parse_args(argv)
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
        print(json.dumps(output, ensure_ascii=False, sort_keys=True, indent=2))
        if args.require_current_reviewed and any(
            row["effective_state"] != "CURRENT_REVIEWED" for row in rows
        ):
            return 1
        return 0
    since_records = _discovery_at(root, args.since) if args.since else None
    output["since"] = args.since
    output.update(
        work_queue(
            assessments,
            discovery,
            evaluation,
            since_records=since_records,
            deferred=args.deferred,
            hints=args.hint,
        )
    )
    print(json.dumps(output, ensure_ascii=False, sort_keys=True, indent=2))
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except DomainError as exc:
        raise SystemExit(f"FAIL: {exc}") from exc
