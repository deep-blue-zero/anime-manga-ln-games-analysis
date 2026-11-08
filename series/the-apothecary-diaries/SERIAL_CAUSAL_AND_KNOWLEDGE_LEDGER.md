---
title: "The Apothecary Diaries — Serial Causal and Knowledge Ledger"
artifact_id: AP_SERIAL_LEDGER
artifact_type: serial_state_ledger
version: "1.0"
status: canonical
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
authority_generation: AP-INITIAL
authority_scope: "INITIAL bootstrap method, architecture, and administrative metadata only; no literary findings"
source_boundary: "Metadata reconnaissance: Japanese volumes 01–16 and separate simplified Chinese volume 15; no narrative admitted"
created: 2026-11-07
last_updated: 2026-11-07
---

# Serial causal and knowledge ledger

## Responsibility

This ledger keeps event ordering, explanations, access to information and institutional conditions separable across future Japanese volume readings. It avoids the common failure where a later explanation overwrites an earlier uncertainty. No event, institution or character state is established at INITIAL.

The registers share evidence IDs but have distinct responsibilities. Full arguments, including causal alternatives and linguistic evidence of uncertainty, remain in the cited readings. A table is not a substitute for them.

## Operational register schemas

| Register / ID | Required fields and distinctions |
|---|---|
| Event/time `AP-T-nnnn` | Witness/version; event identity as established; disclosure unit/section; story-time constraints and uncertainty; predecessor/successor evidence; publication/edition relation if relevant; admitted frontier; focalization; supporting evidence; alternative placement; full reading |
| Knowledge `AP-K-nnnn` | Named knower or reader/narrator position; proposition; belief/knowledge/rumor/misconception/unknown state; acquisition route/time; confidence; who lacks it; disclosure position; concealment/audience; supporting and contrary evidence; change relation; prospective/retrospective mode |
| Causal model `AP-M-nnnn` | Event/question; conditions; actor perception/appraisal; affect; options and constraints; choice/non-action; mechanism; consequence; asserted versus inferred links; rival model; discriminating evidence; missing link; current claim version; dependent findings |
| Institution/practice `AP-I-nnnn` | Source-established institution/practice; stated rule and speaker authority; observed procedure; resources/eligibility; exceptions; who is constrained; enforcement/consequence; change/continuity; rival description; evidence; full argument |
| Continuity/dispute `AP-SD-nnnn` | Conflicting event/knowledge/rule routes; witness/language; boundary; possible cause; alternative state models; needed evidence; dispute ID in claim ledger; affected outputs and unresolved status |

A knowledge row must never use a later source to fill an earlier person's mind. “Narrator knows,” “reader has been told” and “subject believes” are different row keys. Silence can mean absence of evidence; it does not itself prove ignorance or concealment.

Use explicit `UNKNOWN`, `UNRESOLVED`, `NOT_APPLICABLE_WITH_REASON` or bounded intervals rather than blank cells that resemble certainty. Narrative-date estimates are hypotheses with routes. Causal-state confidence attaches to the individual link, not merely the outcome.

## State and continuity rules

The common state key is `witness/version + source frontier + disclosure position + story-time constraint + epistemic mode`. Subject/role/resource and directed relationship conditions are linked to the character ledger. Edition comparison remains `EDITION_COMPARATIVE` and never overwrites the Japanese prospective state.

A new revelation creates a new knowledge/revision event. A genuine change in rules requires its mechanism or an explicit unresolved cause; different testimony alone does not establish institutional change. A successful explanation proposed inside the story is still testimony until the text supplies relevant corroboration.

Classify contradictions using the claim-ledger dispute enum. Preserve both models while unresolved. Record whether an apparent contradiction is in source bytes, character assertions, narrator presentation or analyst interpretation. Each requires a different correction path.

## Update, validation and history

After each future full reading, append newly established events/knowledge and changes, then update current-view pointers. A no-change finding names the inspected unit and dimensions checked. Never silently replace an earlier row with the final state. Changes to story ordering or mechanisms trigger all linked claim/subject/study dependency checks.

Review central chains against their primary routes: does each asserted causal link have the claimed evidence; can a rival explain the same sequence; did the agent confuse information availability with an actual inference? Check at least one low-stakes or routine counterexample where available before promoting a generalized decision tendency.

The active sequential owner maintains this surface; a checkpoint reviewer reconciles it at a frozen boundary. Later synthesis may propose reclassification, retaining original rows and full arguments through the claim-revision route.

| Administrative gap ID | Initial state | Consequence | Resolution requirement |
|---|---|---|---|
| AP-SA-001 | NO_NARRATIVE_ADMITTED | No event/knowledge/causal rows are warranted | Authorized primary inspection and accepted full reading |
| AP-SA-002 | Chapter, story-time and disclosure map unknown | No invented chronology or causal episode segmentation | Verified spine plus source-grounded mapping during an authorized operation |
| AP-SA-003 | Institutional/specialist responsibilities not evidence-established | No standalone domain study commissioned | Role-gap review after recurring evidence demonstrates an independent question |

| History ID | Date | Operation | Result |
|---|---|---|---|
| AP-SL-H001 | 2026-11-07 | Initialized distinct temporal, knowledge, causal and institution schemas | Administrative obligations retained; zero narrative state rows |
