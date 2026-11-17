---
title: "Domestic Girlfriend — claims, questions and revisions"
series: domestic-girlfriend
artifact_id: DG_CLAIM_REVISION_LEDGER
artifact_type: claim_revision_ledger
generation: DG-G1
version: "1.0"
status: canonical
authority_scope: "Claim/revision schema and bootstrap controls; no literary claims"
source_boundary: "Metadata reconnaissance of Japanese manga volumes 01-03 only; no narrative units admitted or inspected"
canonical_home: series/domestic-girlfriend/DG_CLAIM_REVISION_LEDGER.md
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
---

# Claims, questions and revisions

## Current state

| Control | Value |
|---|---|
| Literary claims / questions / predictions | 0 / 0 / 0 |
| Revision events | 0 |
| Admitted source frontier | NONE |
| Interpretation status | No narrative findings; architectural expectations are not claim rows |
| Unresolved source controls | DG-SRC-001 through DG-SRC-006 in the source inventory |

## Claim schema and route

One immutable claim ID, DG-C0001 onward, has an original entry and an append-only transition history. Required fields:

`claim_id | domain | bounded_proposition | through_unit/scene_horizon | evidence_label | confidence | reasoning_summary | supporting_locators | counterevidence_locators | strongest_alternative | disconfirming_observation | reading_anchor | current_status | latest_revision_id`.

Domains include CHARACTER, RELATIONSHIP, KNOWLEDGE, FORM, REGISTER, CONTEXT and ETHICS; add one only for a real retrieval need. `reasoning_summary` indexes the inferential step but cannot replace the developed explanation at `reading_anchor`. Missing evidence is explicitly NONE_OBSERVED_WITHIN_BOUNDARY, UNKNOWN or PENDING_VERIFICATION as appropriate. Do not write dummy locators.

Claim status distinguishes SUPPORTED, CONTESTABLE, PROVISIONAL, OPEN and CONTRADICTED. Confidence uses the method vocabulary. A claim may be well-supported for one horizon and invalid outside it. Stable anchors and witness/image locators are required; links to whole volumes alone cannot support a consequential synthesis claim.

No literary claim entries exist.

## Revision event schema

`revision_id | claim_id | date | author_role | prior_revision_id | earlier_formulation | transition | new_formulation | new_horizon | supporting_and_counterevidence | rationale | affected_downstream_paths_or_claims | unresolved_alternative`.

Transitions are PRESERVE, STRENGTHEN, REVISE, DOWNGRADE, REJECT and OPEN. Append every material change; do not overwrite old formulations or frozen readings. A mutable current index may point to the latest revision. A claim disputed by substantial evidence remains visibly qualified until adjudicated. A table-format change cannot promote a provisional conclusion.

## Questions and prospective predictions

A question record is `question_id | opened_at_horizon | issue | competing_answers | diagnostic_evidence_needed | related_claims | present_disposition | adjudication_ids`, using DG-Q0001 onward. A prediction adds `prediction_id | frozen_at_horizon | forecast | grounding_claims | confidence | possible_falsifier | test_boundary | exposure_disclosure | freeze_reference`.

Freeze the prediction before exposure to its test material. Append adjudications with `adjudication_id | prediction_or_question_id | test_boundary | evidence | outcome | reasoning | residual_uncertainty`. Outcomes are SUPPORTED, PARTLY_SUPPORTED, CONTRADICTED, NO_DIAGNOSTIC_OPPORTUNITY, CONFOUNDED or UNRESOLVED. A retrospective interpretation is never backdated as a forecast. The present V03 acquisition frontier is not itself permission to inspect an additional test volume.

## Update and closure

During each volume transaction, add material claims and questions, adjudicate predictions actually tested, and review claims pressured by the new evidence. A PRESERVE event is warranted when a claim is genuinely re-examined; do not flood the ledger with automatic confirmations. Completion may retain OPEN claims with their impact and next diagnostic requirement.

At checkpoint, verify retrieval chains, alternatives, named agents, chronology and source-layer limits. At specialist dispatch, identify exactly which claims are inputs and which remain live disagreements. If a central premise changes, mark dependent studies for bounded revision rather than attach an isolated footnote to an unchanged argument.
