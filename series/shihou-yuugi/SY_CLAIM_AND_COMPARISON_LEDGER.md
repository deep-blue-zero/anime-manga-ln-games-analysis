---
title: "Shihou Yuugi — claims and collection comparison"
series: shihou-yuugi
artifact_id: SY_CLAIM_AND_COMPARISON_LEDGER
artifact_type: claim_revision_ledger
generation: SY-G1
version: "1.0"
status: canonical
authority_scope: "Story-qualified claims, comparison and revision schemas; no conclusions"
source_boundary: "One Japanese four-story anthology EPUB, metadata verified; all story narratives unadmitted and uninspected"
canonical_home: series/shihou-yuugi/SY_CLAIM_AND_COMPARISON_LEDGER.md
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
---

# Claims and collection comparison

| Control | Value |
|---|---|
| Story literary claims / forecasts | 0 / 0 |
| Accepted story readings | 0 |
| Collection comparisons | 0 |
| Source horizon | NONE_ADMITTED |
| Shared continuity established | NO |

## Local claims and revisions

Local claim IDs use `SY-W01-C0001` style. Required fields: `id | work | bounded_proposition | scene/disclosure_horizon | domain | evidence_label/confidence | warrant_summary | supporting_locators | counterevidence | strongest_alternative | falsifier | reading_anchor | status | latest_revision`. Status: SUPPORTED, CONTESTABLE, PROVISIONAL, OPEN or CONTRADICTED. Domains include CHARACTER, RELATIONSHIP, KNOWLEDGE, FORM, REGISTER, CONTEXT and ETHICS.

Revision: `revision_id | claim_id | date | predecessor | earlier_formulation | transition | new_formulation | horizon | evidence/counterevidence | reason | affected_paths/claims | residual_alternative`. Use PRESERVE, STRENGTHEN, REVISE, DOWNGRADE, REJECT or OPEN. Current indexes may update latest pointers; original wording and prospective freezes survive.

## Collection comparison schema

Comparison IDs use SY-COMP0001. Required fields: `id | compared_work_keys | exact_admitted_scope | comparison_question | common_axis | local_claim_ids_and_locators_per_work | substantive_similarity | substantive_difference | counterexamples/noncomparability | inference_limits | full_argument_anchor | status/revision`.

Evidence must exist for each compared work. A resemblance is not shared character identity, diegesis, causal influence or creator psychology. Preserve differences that limit the thesis. A collection claim cannot silently overwrite a story's interpretation. Resolve any pressure through that story's claim history and a visible comparison revision.

## Questions and forecasts

Question: `work/question_id | opened_horizon | alternatives | diagnostic_evidence_needed | related_claims | disposition | adjudications`.
Forecast: `work/prediction_id | frozen_horizon | forecast | grounding_claims | confidence | falsifier | test_scope | exposure_disclosure | freeze_reference`.

Freeze before exposure and adjudicate separately using SUPPORTED, PARTLY_SUPPORTED, CONTRADICTED, NO_DIAGNOSTIC_OPPORTUNITY, CONFOUNDED or UNRESOLVED, retaining source evidence and reasoning. Another story does not test a prediction about the same character unless actual identity/continuity was separately established. Previously seen material yields RETROSPECTIVE_CONSISTENCY_TEST, not prospective success.

## Transaction and acceptance

Append material claims, revisions and adjudications with the accepted story reading. No automatic confirmations or dummy questions. No literary rows exist now. Metadata controls remain in the source/work map.

Every claim routes through full prose and exact source locators; the warrant summary is not a replacement argument. Before comparison, reconcile story-local chronology, subjects, directed states, Japanese attribution and live alternatives. If a central comparison premise changes, review dependent synthesis and preserve the previous scope/formulation.
