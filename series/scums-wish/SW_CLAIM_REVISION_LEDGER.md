---
title: "Scum’s Wish — claims, revisions and horizon comparison"
series: scums-wish
artifact_id: SW_CLAIM_REVISION_LEDGER
artifact_type: claim_revision_ledger
generation: SW-G1
version: "1.0"
status: canonical
authority_scope: "Claim/forecast/horizon schema and controls; no literary findings"
source_boundary: "Metadata reconnaissance of Japanese main manga volumes 01-08 and decor volume 09; no narrative units admitted or inspected"
canonical_home: series/scums-wish/SW_CLAIM_REVISION_LEDGER.md
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
---

# Claims, revisions and horizon comparison

## Present controls

| Control | State |
|---|---|
| Literary claims / questions / predictions | 0 / 0 / 0 |
| MAIN source horizon | NONE_ADMITTED |
| DECOR source horizon | NONE_ADMITTED |
| Main-only interpretive checkpoint | NOT_CREATED |
| Source gaps | SW-SRC-001 through SW-SRC-007 in source inventory |

Architectural expectations are not literary claim rows. No plot, character or ethical conclusion is seeded here.

## Stable claims and evidence

Use SW-C0001 onward. The exact claim schema is:

`claim_id | domain | proposition | source_track_and_horizon | scene_knowledge_boundary | evidence_label/confidence | inferential_warrant_summary | supporting_locators | counterevidence | strongest_alternative | disconfirming_observation | reading_anchor | claim_status | latest_revision_id`.

Domains include PERSON, PERSPECTIVE, RELATIONSHIP, REGISTER, FORM, CONTEXT, ETHICS, ENSEMBLE and HORIZON. Claim status is SUPPORTED, CONTESTABLE, PROVISIONAL, OPEN or CONTRADICTED. A summary routes to full causal prose; it cannot replace the warrant, alternative or evidence. Locators name the witness and source track, with no invented chapter/page data.

## Append-only revisions

`revision_id | claim_id | date | prior_revision_id | earlier_formulation | transition | new_formulation | new_horizon | support_and_counterevidence | reason | dependent_claims_and_paths | unresolved_alternative`.

Use PRESERVE, STRENGTHEN, REVISE, DOWNGRADE, REJECT or OPEN. Keep old formulations and frozen readings. A mutable current index may point to the latest event for each horizon; MAIN-only and DECOR-aware states remain distinguishable. A new source does not mechanically promote a claim or erase a live rival reading.

A load-bearing revised premise requires review of dependent specialist arguments. It cannot be closed solely by appending a note while leaving the dependent conclusion intact.

## Questions, forecasts and adjudication

Questions use `question_id | opened_at_horizon | question | alternatives | diagnostic_requirement | affected_claims | present_disposition | adjudications`, with SW-Q0001 onward.

Predictions use `prediction_id | frozen_horizon | forecast | grounding_claims | confidence | falsifier | test_boundary | prior_exposure | freeze_reference`. Freeze before the test material is exposed. Test outcomes are SUPPORTED, PARTLY_SUPPORTED, CONTRADICTED, NO_DIAGNOSTIC_OPPORTUNITY, CONFOUNDED or UNRESOLVED. Adjudication records retain test scope, locators, observed response, reasoning and uncertainty. No retrospective fit may be called a prior prediction.

## Main/decor cross-horizon schema

Only after separate authorized supplement inspection, add:

`comparison_id | main_checkpoint_anchor | main_claim_or_question | supplementary_evidence | effect(CONFIRMATION/DEVELOPMENT/RETROSPECTIVE_EXPLANATION/REVEALED_NOT_NEW/DIVERGENCE/UNRESOLVED) | actual_event_time | disclosure_horizon | revised_claim_ids | counterreading | affected_studies`.

A main-only interpretation can remain sound within its boundary even when later evidence changes the mature synthesis. Conversely, changed scope is not a reason to preserve a demonstrated error unqualified in current supplementary analysis. Maintain both historical and current responsibilities through explicit revision.

## Update and acceptance

Append claims, material transitions and question/prediction adjudications atomically with each accepted volume. Do not generate automatic PRESERVE rows or placeholder questions. Record a justified no-update statement in the reading's ledger manifest where needed.

At checkpoints test exact retrieval, source-layer distinctions, subject attribution, competing explanations and horizon consistency. Keep unresolved uncertainty with its practical effect. Full synthesis readiness requires role-gap and convergence review; a tidy claim table cannot supply missing interpretation.
