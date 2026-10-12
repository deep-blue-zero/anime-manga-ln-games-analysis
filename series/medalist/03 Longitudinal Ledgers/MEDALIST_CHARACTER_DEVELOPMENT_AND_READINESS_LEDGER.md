---
title: "Medalist — Character Development and Reconstruction Readiness"
artifact_id: "MEDALIST_CHARACTER_DEVELOPMENT_AND_READINESS_LEDGER"
artifact_type: "character_state_readiness_ledger"
series: "Medalist / メダリスト"
series_id: "medalist"
generation: "MEDALIST_BOOTSTRAP_V1"
version: "0.1"
status: "active_provisional"
scope: "Time-indexed character interpretation, identity resolution and evidence-specific promotion readiness"
canonical_home: "series/medalist/03 Longitudinal Ledgers/MEDALIST_CHARACTER_DEVELOPMENT_AND_READINESS_LEDGER.md"
source_boundary: "Architecture and metadata reconnaissance only; zero primary narrative units admitted or inspected"
created: "2026-10-11"
review_status: "OWNER_REVIEW_PENDING"
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
do_not_use_as_literary_evidence: true
recommended_reasoning_class: "SUBSTANTIVE_ANALYSIS"
---

# Character development and readiness

This ledger owns character-level developmental state and the readiness derived from that evidence. It does not own pair states, competition results or canonical observations. At bootstrap all tables have **zero rows**; no cast identity, psychological trait or readiness grade has been invented.

## Why development and readiness share this home

Readiness depends on the same character's state coverage, ordinary behavior, contradictions and gaps. Keeping the assessment alongside the transition history prevents an independent readiness list from losing its basis. They remain distinct record types and decisions; the [reconstruction specification](../00%20Frameworks%20and%20Methods/MEDALIST_CHARACTER_RECONSTRUCTION_SPEC.md) controls promotion.

## Schema and identifiers

The character register assigns `MD-CHAR-####` on first admitted evidence, preserving source-spelled name, short aliases with language/basis, continuity, first observation and unresolved identity. Global entity/subject IDs remain null unless actually curated. Never infer an unseen cast from publisher summaries.

An append-only state event `MD-CS-####` names character, represented time/range and certainty, revealed-after unit, state/change kind, self-report, observed action, inference/alternatives, evidence IDs, claim/version, confidence/basis, previous-state link and superseded/correction link. Change kinds: `DISPOSITION_CHANGE / KNOWLEDGE_CHANGE / RELATIONSHIP_CHANGE / CONTEXT_CHANGE / REVEALED_NOT_NEW / UNRESOLVED`. Proposed psychological mechanisms are claims; an attributed self-report is not a trait.

The current view names character, valid source/story boundary, active state-event references, scoped formulation and unresolved contradictions. It is a mutable projection of retained history, not the source of earlier freezes. Track capability/self-efficacy, goals/aspirations/fears, coping, decision-making and skating's significance only when consequential evidence exists.

Readiness `MD-RD-####` names character + artifact/domain + source endpoint, context diversity, supporting/counterevidence IDs, language/form coverage, missing domains, proposed scope, test status, assessment/reviewer/date and prerequisite claims. Use `UNASSESSED / INSUFFICIENT_EVIDENCE / BOUNDED_PROVISIONAL / DOMAIN_READY` locally; these are not artifact authority or global capability grades.

## Row triggers, evidence and revision

Add a state event when a new decision, persistent discrepancy, change or disclosure materially alters a character interpretation. A single mood may remain local in its reading; do not manufacture a stable disposition. Add readiness when an actual promotion is assessed or new evidence changes a prior assessment. Multiple observations of one scene are not independent contexts.

Every event requires a frozen reading's `MD-EV-…` locator, qualitative confidence and counterreading where interpretive. Link directional `MD-RL-…` relationship rows, `MD-SK-…` competence records and `MD-KN-…` knowledge records rather than duplicating their authoritative content. Japanese speech evidence is retained in original observation rows and linked here when it changes characterization/readiness.

Historical event identity, first source boundary and original formulation are immutable. Current formulation/readiness may advance through targeted edits with a new event or `MD-RV-…` revision; retain earlier readiness decisions and failed tests. Corrections append a reason and replacement, never erase a prior source-time state.

## Empty evidence tables

| Character key | Source-spelled identity / alias basis | Continuity | First observation | Global IDs / unresolved identity |
| --- | --- | --- | --- | --- |

| State event | Character | Story time / revealed after | Change kind | Action / self-report / inference | Evidence / claim version | Confidence / alternatives | Prior / correction |
| --- | --- | --- | --- | --- | --- | --- | --- |

| Character | Current source boundary | Active state references | Bounded current formulation | Open contradictions |
| --- | --- | --- | --- | --- |

| Readiness record | Character / target / domain | Boundary / scope | Context coverage / counterevidence | Gaps / tests | Assessment / reviewer / date | History / revision |
| --- | --- | --- | --- | --- | --- | --- |
