---
title: "Shuukura V2 — character state and reconstruction readiness"
artifact_id: SHUUKURA_V2_CHARACTER_LEDGER
artifact_type: longitudinal_ledger
series: "Shuukura / 週に一度クラスメイトを買う話"
series_id: shuukura
generation: SHUUKURA_V2
version: "0.1"
status: active_provisional
scope: "Time-indexed individual state, developmental change and domain-specific readiness"
source_boundary: "Bootstrap metadata and architecture only; zero V2 narrative units admitted or read"
canonical_home: series/shuukura/04 Longitudinal Ledgers/SHUUKURA_CHARACTER_STATE_AND_READINESS_LEDGER.md
created: "2026-10-17"
planning_date: "2026-10-16"
review_status: OWNER_BOOTSTRAP_REVIEW_PENDING
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
do_not_use_as_literary_evidence: true
---

# Character state and reconstruction readiness

Schema initialized; **zero evidence-derived character records and zero models**. Principal subject identifiers are reserved as `MIYAGI_SHIORI` (宮城志緒理) and `SENDAI_HAZUKI` (仙台葉月); these are administrative identities, not findings. Supporting subjects are admitted only from inspected source evidence. Global character discovery remains the curation agent's responsibility.

## Responsibility and boundaries

This ledger owns individual state transitions, stable-versus-acquired tendency candidates, changes across social/domestic contexts, and reconstruction readiness by domain. It references the disclosure ledger for the character's information and the relationship ledger for directional commitments; it does not copy either history. The claims ledger owns adjudication of explanations. Immutable reading observations own the underlying passages. Model specifications and validation cases eventually belong to the character's justified specialist artifact, not this index.

At each atomic unit, append evidenced events, reconcile current state with the entering snapshot, and explicitly record no material change where appropriate in the unit receipt. Every current row carries the event/version IDs needed to reconstruct earlier states. Never replace an earlier state with later understanding without preserving its valid reading interval and revision event.

## Append-only state event schema

`CHR-<witness>-<unit>-<subject>-NNN` is stable. Record source order separately from narrated event time; uncertain chronology stays uncertain. `valid_from`/`valid_to` refer to source-observable states, not invented dates. A superseding event closes a prior projection without deleting its historical basis.

| Event ID / revision | Subject / witness / unit | Event time and uncertainty | Prior state ID → new state ID | Disposition or acquired tendency; domain | Stated intention / inferred motive / competing explanation | Context and observed action / consequence | Evidence observation IDs and exact locators | Countercase / confidence / claim ID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |

## Current state projection schema

| Subject / witness / as-of boundary | State version and event lineage | Stable / acquired / unresolved tendencies | Priorities and conflicting motives | Context-sensitive decision patterns | Information-state IDs | Relationship-state IDs | Japanese voice/disclosure evidence IDs | Limitations and negative constraints |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |

The projection is an index into evidence and events, not a personality summary detached from time. Do not equate narration with self-knowledge or outward behavior with a single motive. Contradictory tendencies may remain live.

## Readiness and supporting-character role-gap schema

Domains include everyday choices, conflict and refusal, intimacy/boundaries, peer/family/institutional contexts, Japanese dialogue, and stress/repair. Evaluate separately; missing domains remain UNASSESSED or INSUFFICIENT. Use the [reconstruction contract](../00%20Frameworks%20and%20Methods/SHUUKURA_CHARACTER_RECONSTRUCTION_CONTRACT.md) for the meaning of the readiness labels and validation prerequisites.

| Subject / witness / time range | Domain | Grade / evidence strength | Coverage and independent situation families | Countercases / rival explanations | Fit cases / genuinely held-out cases / contamination status | Abstention conditions | Monograph or bounded dossier decision and rationale | Review boundary / model artifact |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |

A supporting subject warrants an individual monograph only when recurring evidence, independent agency, explanatory importance and cross-context coverage justify it. Otherwise record a bounded dyadic/social dossier or explicit deferral. A protagonist is not automatically SPECIALIST_READY. No character registration or simulation capability is asserted at bootstrap.

## Transaction acceptance

Require recoverable entering and endpoint states, no unexplained retroactive changes, exact observation links, cross-ledger consistency, confidence proportional to evidence, and readiness that distinguishes literary interpretation from tested behavior. All substantive additions await separate sequential authorization. Revision 0.1: schema only.
