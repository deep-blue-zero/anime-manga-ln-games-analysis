---
title: "Medalist — Claims, Predictions and Revisions"
artifact_id: "MEDALIST_CLAIMS_PREDICTIONS_AND_REVISIONS_LEDGER"
artifact_type: "claim_revision_ledger"
series: "Medalist / メダリスト"
series_id: "medalist"
generation: "MEDALIST_BOOTSTRAP_V1"
version: "0.1"
status: "active_provisional"
scope: "Material interpretive claim versions, competing hypotheses, genuine predictions and downstream amendments"
canonical_home: "series/medalist/03 Longitudinal Ledgers/MEDALIST_CLAIMS_PREDICTIONS_AND_REVISIONS_LEDGER.md"
source_boundary: "Architecture and metadata reconnaissance only; zero primary narrative units admitted or inspected"
created: "2026-10-11"
review_status: "OWNER_REVIEW_PENDING"
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
do_not_use_as_literary_evidence: true
recommended_reasoning_class: "DEEP_SYNTHESIS"
---

# Claims, predictions and revisions

This home owns material claim identity/version, epistemic status, prospective predictions and revision history. Frozen readings own canonical observations and what was knowable then; domain ledgers own accumulated state. Publication metadata belongs in the source map. **All claim, prediction and revision tables are empty.**

## Claim schema

`MD-CL-####` has a stable question/responsibility. Each version records formulation, class (`INFERENCE / HYPOTHESIS / EVALUATION / UNRESOLVED`), continuity/edition/source endpoint, first formulated unit, evidence IDs, counterevidence, live alternatives, confidence/basis, disconfirming test, current topical home and dependent paths/rows.

Register a claim when it recurs, changes consequential interpretation, supports a specialist/model, carries a material disagreement or creates downstream obligations. Minor descriptive facts can remain local observations. A thematic label without an evidence-bearing formulation is not a claim.

A mutable current view selects the latest accepted scoped version; append-only history retains each prior formulation and the exact boundary at which it was asserted. A domain ledger may summarize the scoped state but must cite its claim/version, not create a competing independent claim.

## Revision schema and supersession

`MD-RV-####` records prior claim/version, new formulation/version, transition `PRESERVE / STRENGTHEN / REVISE / DOWNGRADE / REJECT / OPEN`, triggering observation/known-after unit, competing explanation, counterevidence, confidence, impacted homes and closure state. Record whether the change is new evidence, later disclosure, edition difference, error correction or interpretation change.

Retain rejected/uncertain versions and failed expectations. Revision of a claim is not deletion of its reading. Whole-artifact replacement follows the authority/supersession policy with reciprocal exact paths and a clear current sink; ordinary claim changes stay in their established topical home.

## Prediction schema and genuine adjudication

`MD-PR-####` records creation timestamp (ISO timestamp with offset), containing Git commit recovered externally, originating freeze/claim, precise prediction, eligible future source window, required opportunity, observable support/disconfirmation rule, alternatives, confidence and prior-exposure limitation. The original text and rule are immutable before inspection of later eligible evidence.

Adjudication appends inspected boundary/observation IDs, actual opportunity, `SUPPORTED / DISCONFIRMED / MIXED / UNTESTED / UNRESOLVED`, explanation and any resulting revision. No opportunity is `UNTESTED`. Retrospective fitting or known later information is not a prospective prediction. There is no prediction quota: an honest open question may be more useful.

## Cross-source dispute and dependency behavior

Classify conflict first: chronology/knowledge, unreliable account/deception, edition revision, translation, adaptation, paratext scope or genuine inconsistency. Keep a manga claim separate from an adaptation claim; agreement is a comparison, not merged continuity. Escalate to a bounded audit when identity/locator is unreliable, a load-bearing contradiction survives, or downstream claims cannot be consistently revised.

Before closing a revision, review every named dependent ledger/model/specialist. Mark unchanged dependents as reviewed; revise only affected material through targeted edits. Required evidence debt blocks the affected claim/promotion. A bounded provisional claim may remain open when its limitations are explicit and do not contradict the artifact's accepted scope.

## Empty evidence tables

| Claim / version | Formulation / class / scope | First boundary | Evidence / counterevidence / alternatives | Confidence / test | Current home / dependencies |
| --- | --- | --- | --- | --- | --- |

| Revision | Prior → new version | Transition / reason / known after | Evidence / alternatives | Affected homes / disposition | Closure / unresolved debt |
| --- | --- | --- | --- | --- | --- |

| Prediction | Created / originating freeze / Git recovery | Original expectation / window / opportunity | Immutable adjudication rule / alternatives | Confidence / exposure limitation | Later observation / result / revision |
| --- | --- | --- | --- | --- | --- |
