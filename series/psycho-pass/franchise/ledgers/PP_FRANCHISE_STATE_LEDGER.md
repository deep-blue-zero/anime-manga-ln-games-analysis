---
title: "Psycho-Pass — Franchise state and portrait qualification"
artifact_id: PP_FRANCHISE_STATE_LEDGER
artifact_type: franchise_state_ledger
series: psycho-pass
version: "1.0"
status: canonical
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
do_not_use_as_literary_evidence: true
authority_generation: PP-INITIAL
source_boundary: "NONE; metadata-only foundation, no admitted narrative"
canonical_home: series/psycho-pass/franchise/ledgers/PP_FRANCHISE_STATE_LEDGER.md
created: 2026-11-18
last_updated: 2026-11-18
---

# Franchise state and portrait qualification

This is the single current canonical home for reconciled character, directed relationship and institution/world state across admitted installments. It also owns individual portrait qualification and the route to each current full portrait. **Initialized records: 0 entities, 0 reconciled states, 0 qualification decisions, 0 monograph obligations or completed portraits.** These zero counts mean no narrative has been admitted; they are not a finding that no character qualifies.

## Materialized state contract

Give each person/institution a stable `PP-ENT-####` ID once evidence supports identity. Preserve source-language name, transliteration and meaningful aliases with their legitimate knowledge boundaries. Unknown/provisional identities remain distinct until evidenced equivalence. Record continuity and any source-scoped identity uncertainty.

A state record `PP-FSTATE-####` includes subject and domain, current reconciled conclusion in explanatory prose, boundary through which it is current, contributing installment/edition/unit/local state and claim IDs, decisive locators, contrary cases, confidence and transition history. Explain the mechanism behind a claimed change; a stack of trait labels or links is insufficient. Local observations remain in their source ledger. The master stores only material synthesis and its lineage.

For a person, preserve stable tendencies, changing circumstances, goals, beliefs/knowledge, competencies/limits, self-presentation and meaningful ordinary behavior separately. Do not merge a later identity revelation with what another character knew earlier. For relationships, the canonical key includes A → B and dimension; reciprocity requires separate evidence. For institutions, distinguish professed authority, implemented behavior, constraints, exceptions and consequences. A measurement output remains different from a validated description of a person.

## Qualification register contract

At the first accepted episode, each new differentiated individual is considered; reassess on substantive new evidence and at every declared tranche/installment synthesis boundary. The qualification record carries subject ID/name, continuity, assessed boundary, evidence distribution, rationale, gaps, next review trigger and the actual canonical portrait path once it exists. No name-only roster or fixed lead-character quota controls this decision.

Use `QUALIFIED_PENDING` when sufficient differentiated evidence creates a portrait production obligation, `DEFERRED_EVIDENCE` with a concrete gap/review trigger, `COMPLETE_AT_BOUNDARY` only after both required reviews, and `REASSESS_AFTER_REVISION` when material evidence or correction changes the portrait's basis. An unavailable portrait path is stated as absent rather than linked as if it exists. Counts of pending obligations remain visible in the current handoff.

The [architecture](../../framework/PP_SYNTHESIS_ARCHITECTURE.md#individuals-and-one-canonical-full-portrait) defines the full portrait standard and intended home `franchise/characters/PP_<SUBJECT>_CHARACTER_MONOGRAPH.md`. There is one current full portrait per person/continuity/boundary. Installment states and historical snapshots are scoped evidence, not competing current portraits.

A completion decision names the exact portrait bytes and declared boundary, independent self-containment review and independent source-fidelity review, actual source sample/coverage, required revisions and their disposition, and residual limits. Both reviews must pass for the declared scope; a complete checklist with missing causal/ordinary-life/relationship substance fails. Unknown domains remain stated, not fabricated. Portrait completion does not certify operational reconstruction or simulation readiness.

## Incremental integration and dependencies

The integrator applies accepted local deltas to affected state and qualification records, preserving the previous conclusion and reason for change. A new state with cross-installment consequences also links the [continuity/claim ledger](PP_CONTINUITY_AND_CLAIM_LEDGER.md). If not yet reconciled, keep the older materialized boundary visible with the pending delta ID; do not silently borrow the latest local wording.

A changed psychological, relationship or institutional conclusion identifies dependent portraits, specialist studies and syntheses. Update affected living portraits through dated sourced additions or mark them for reassessment. Frozen prior versions retain their authority boundary and supersession route. At a synthesis boundary, reconcile pending changes and qualification obligations or accurately state that the affected layer is incomplete.

The master never adjudicates a fact solely by citing itself. Reopen decisive source evidence through installment/edition/unit locators under the [integration protocol](../../integration/PP_RECONCILIATION_PROTOCOL.md).
