---
title: "Peach Girl — Character Development and Readiness"
artifact_id: PEACH_GIRL_CHARACTER_DEVELOPMENT_AND_READINESS_LEDGER
artifact_type: character_development_readiness_ledger
series: "Peach Girl / ピーチガール"
series_id: peach-girl
generation: PEACH_GIRL_BOOTSTRAP_V1
version: "0.1"
status: active_provisional
scope: "Character Development and Readiness; schema initialized with zero source-derived records"
source_boundary: "Original manga candidate corpus; no narrative source admitted or inspected"
canonical_home: series/peach-girl/03 Longitudinal Ledgers/PEACH_GIRL_CHARACTER_DEVELOPMENT_AND_READINESS_LEDGER.md
created: "2026-10-16"
review_status: OWNER_BOOTSTRAP_AUDIT_PENDING
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
do_not_use_as_literary_evidence: true
---

# Character Development and Readiness

This instrument owns verified local subject identity, character-level developmental/decision state and readiness derived from that evidence. The [architecture](../00%20Frameworks%20and%20Methods/PEACH_GIRL_SYNTHESIS_ARCHITECTURE.md#character-reconstruction-contract) owns the reconstruction contract. Pair feelings/commitments belong in the relationship ledger; proposition knowledge and public reputation belong in the information ledger; arguments and revisions belong in the claims ledger.

Development and readiness share a home because promotion depends on this same subject's state coverage and gaps. They are distinct record types. No character name, trait, psychological conclusion or readiness assessment is prepopulated.

## Records and allocation

| Type / stable identifier | Required fields |
| --- | --- |
| Subject `PG-CHAR-####` | Source-spelled name or bounded unnamed identity; alias/language/basis if inspected; continuity; first observation; identity uncertainty; any actually curated global IDs, otherwise null |
| Development event `PG-CS-####` | Subject; represented time/range and certainty; learned-after source frontier; previous state; event kind; observed action; attributed intention/self-report; options and constraints; recipient/response/consequence where relevant; observation refs; claim/version; interpretation and alternative; support strength/basis; correction link |
| Current subject view | Subject + temporal/disclosure boundary; active event IDs/versions; scoped formulation; unresolved contradictions and unobserved contexts |
| Readiness decision `PG-RD-####` | Subject + target artifact/domain; source and Git evidence cutoff; context diversity; supporting/counterevidence; written-language/form coverage; missing domains; validation status; assessment/reviewer/date; prior decision; governing claim versions |

Event kinds: `DISPOSITION_CHANGE / KNOWLEDGE_CHANGE / RELATIONSHIP_CHANGE / CONTEXT_CHANGE / REVEALED_NOT_NEW / UNRESOLVED`. Link the authoritative knowledge or relationship row; do not restate its entire proposition. Actor-level agency records actual choice processes; the relationship ledger owns their pair-state consequences. A new disclosure of an old habit does not establish newly developed behavior.

Readiness states: `UNASSESSED / INSUFFICIENT_EVIDENCE / BOUNDED_PROVISIONAL / DOMAIN_READY`. These are local scoped assessments, not artifact authority or global capability grades. No row is needed merely to assign every mentioned subject UNASSESSED.

## Evidence, update and history

Allocate an ID only on actual admitted evidence, monotonically within its prefix; never recycle it. Distinguish identity uncertainty, source legibility, timing and interpretation uncertainty. Every state event requires a reading's `PG-EV-VNN-####` with exact locator and disclosure frontier. A self-report can be recorded without being endorsed as a stable trait. A consequential interpretation also points to a `PG-CL-####@version`, supporting evidence, strongest available counterevidence and plausible alternative.

A future VNN transaction appends events for material goal/choice/development changes, newly disclosed state or a consequential contradiction. Ordinary momentary mood stays local unless it changes the model. Update readiness only when an actual proposal is assessed or evidence materially changes an existing assessment. Independent contexts and failures matter; repeated shots of one encounter are not independent tests.

Preserve original names/identity allocation, event formulations, source frontiers and assessment history. Amend the current view through targeted edits with an appended event/revision; retain old versions. Later retrospective explanation has its actual learned-after frontier. A frozen `PG-FR-VNN` cites the versions then active and contains enough state to recover them after this ledger advances. Errata append a reason and replacement link.

The sequential closeout certifies this instrument updated or records no material change without a dummy row. Bootstrap source-derived subject, event, current-state and readiness rows: **0**.

## Subject register

| Subject | Source identity / aliases and basis | Continuity / first observation | Identity uncertainty / global IDs |
| --- | --- | --- | --- |

## Developmental events

| Event / version | Subject / prior | Story time / learned after | Kind / action / intention / options / consequences | Evidence / claim version | Uncertainty / counterreading / correction |
| --- | --- | --- | --- | --- | --- |

## Current subject state

| Subject / boundary | Active event versions | Scoped state | Unresolved evidence / contexts |
| --- | --- | --- | --- |

## Readiness assessments

| Assessment / prior | Subject / target / domain / cutoff | Evidence diversity / counterevidence | Gaps / validation | Assessment / reviewer / date / claim versions |
| --- | --- | --- | --- | --- |
