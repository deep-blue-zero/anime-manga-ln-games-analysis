---
title: "Astra Lost in Space — claims and revisions"
series: astra-lost-in-space
artifact_id: ALS_CLAIM_REVISION_LEDGER
artifact_type: claim_revision_ledger
generation: ALS-G1
version: "1.0"
status: canonical
authority_scope: "Claim/forecast history schema and controls; no literary conclusions"
source_boundary: "One Japanese 彼方のアストラ 全巻合本版 omnibus EPUB; internal units unverified; no narrative admission or inspection"
canonical_home: series/astra-lost-in-space/ALS_CLAIM_REVISION_LEDGER.md
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
---

# Claims and revisions

| Control | Current state |
|---|---|
| Claims / questions / predictions | 0 / 0 / 0 |
| Admitted source horizon | NONE |
| Internal-unit map | PENDING |
| Full-source interpretation | NOT_CREATED |

## Schemas

Claim:
`claim_id | bounded_proposition | domain | verified_unit/scene/disclosure_horizon | evidence_label/confidence | warrant_summary | support_locators | counterevidence | strongest_alternative | falsifier | full_reading_anchor | status | latest_revision`.
Use ALS-C0001 onward. Domains include CHARACTER, KNOWLEDGE, RELATIONSHIP, FORM, REGISTER, CONTEXT and GROUP where evidenced. Status is SUPPORTED/CONTESTABLE/PROVISIONAL/OPEN/CONTRADICTED.

Revision:
`revision_id | claim_id | date | predecessor | earlier_formulation | transition | new_formulation | new_horizon | evidence/counterevidence | rationale | dependent_claims/artifacts | residual_alternative`.
Transitions are PRESERVE/STRENGTHEN/REVISE/DOWNGRADE/REJECT/OPEN. Retain original wording and prospective freezes; update current pointers only through events.

Question:
`question_id | opened_unit/horizon | issue | competing_answers | diagnostic_requirement | related_claims | disposition | adjudications`.

Prediction:
`prediction_id | frozen_unit/horizon | forecast | grounding_claims | confidence | falsifier | test_unit_scope | exposure_disclosure | freeze_reference`.
Adjudication carries exact evidence, diagnostic opportunity, reasoning and SUPPORTED/PARTLY_SUPPORTED/CONTRADICTED/NO_DIAGNOSTIC_OPPORTUNITY/CONFOUNDED/UNRESOLVED.

All analytical row sets are empty because no evidence has been admitted.

## Omnibus-specific preservation

A file already available in full is not a retrospectively open evidence pool. Preserve which internal units were unexposed when the prediction froze. If the author saw later sections or knew the outcome, mark RETROSPECTIVE_CONSISTENCY_TEST; re-splitting the file does not restore blindness.

Claim locators use the global image coordinate plus verified unit/chapter crosswalk. A printed-page reset cannot point to the wrong internal volume. A changed map requires locator reconciliation before a claim is current.

At every accepted unit append material claims/revisions and test adjudications; do not manufacture automatic confirmations. Keep OPEN conflicts and their consequences visible. A new revelation can revise current interpretation while the earlier knowledge boundary remains historical truth. Changed central premises trigger dependent specialist review.

A summary warrant routes to complete reasoning, not a substitute for it. Before synthesis inspect support, named subjects, temporal/source layers and strongest alternatives, then the separate architecture gates.
