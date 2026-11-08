---
title: "Look Back — claims and revisions"
series: look-back
artifact_id: LB_CLAIM_REVISION_LEDGER
artifact_type: claim_revision_ledger
generation: LB-G1
version: "1.0"
status: canonical
authority_scope: "Claim/history schemas and current controls; no literary conclusions"
source_boundary: "One Japanese standalone manga EPUB, metadata verified; narrative admission and inspection NONE"
canonical_home: series/look-back/LB_CLAIM_REVISION_LEDGER.md
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
---

# Claims and revisions

| Control | Present state |
|---|---|
| Literary claims / open questions / forecasts | 0 / 0 / 0 |
| Admitted horizon | NONE |
| Full-work prospective freeze | NOT_CREATED |
| Reconstruction predictions | NOT_CREATED |

## Claim and revision schemas

A claim uses immutable LB-C0001-style ID and fields `claim_id | domain | bounded_proposition | scene/disclosure_horizon | evidence_label/confidence | inferential_warrant_summary | support_locators | counterevidence | strongest_alternative | falsifier | reading_anchor | status | latest_revision`. Domains include CHARACTER, RELATIONSHIP, TEMPORAL, FORM, REGISTER, CONTEXT or ETHICS. Status is SUPPORTED, CONTESTABLE, PROVISIONAL, OPEN or CONTRADICTED. Summaries index full reasoning; they do not replace it.

A revision uses `revision_id | claim_id | date | previous_revision | earlier_formulation | transition | revised_formulation | revised_horizon | evidence/counterevidence | reason | dependent_claims/artifacts | remaining_alternative`. Transitions are PRESERVE, STRENGTHEN, REVISE, DOWNGRADE, REJECT or OPEN. Preserve original claims, prospective freezes and full earlier formulations. Current indexes may route to latest events.

No literary rows exist. Metadata facts stay in the source inventory rather than masquerading as narrative claims.

## Questions and forecasts

Question schema: `question_id | opened_horizon | issue | competing_answers | diagnostic_evidence_needed | related_claims | disposition | adjudication_ids`, using LB-Q0001 onward.

Forecast schema: `prediction_id | frozen_horizon | forecast | grounding_claims | confidence | possible_falsifier | test_scope | exposure_disclosure | freeze_reference`. Freeze before test exposure. Adjudication records test evidence, diagnostic opportunity, outcome, reason and limits. Outcomes: SUPPORTED, PARTLY_SUPPORTED, CONTRADICTED, NO_DIAGNOSTIC_OPPORTUNITY, CONFOUNDED, UNRESOLVED.

The work may be fully exposed by the time a model is created; such evaluation is RETROSPECTIVE_CONSISTENCY_TEST, not a clean prediction. Neither a reordered reading nor a withheld written summary erases source exposure.

## Transaction and preservation

Append material claims and events with the accepted reading, adjudicating only what was tested. OPEN is a valid result. Do not create automatic confirmations or filler questions. Every mature claim must route to stable reading headings and exact witness/image/panel support; unit-only references are navigation, not adequate support for disputed wording or form.

Before synthesis, reconcile scene chronology, speaker/thinker identity, evidence layers and alternatives. If a central premise changes, identify every dependent argument and require bounded revision. Keep the main causal prose intact until an evidence-backed correction justifies changing it.
