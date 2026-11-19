---
title: "Psycho-Pass S1 New Edit — Evidence and local state"
artifact_id: PP_S01NE_EVIDENCE_AND_STATE_LEDGER
artifact_type: evidence_and_state_ledger
series: psycho-pass
version: "1.0"
status: canonical
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
do_not_use_as_literary_evidence: true
authority_generation: PP-INITIAL
source_boundary: "NONE; metadata-only foundation, no admitted narrative"
canonical_home: series/psycho-pass/installments/s01-new-edit/PP_S01NE_EVIDENCE_AND_STATE_LEDGER.md
created: 2026-11-18
last_updated: 2026-11-18
---

# S1 New Edit — Evidence and local state

This is the current canonical source-observation and installment-state home for the intended eleven New Edit units. **Initialized records: 0 observations, 0 scene reconstructions, 0 character states, 0 relationship states, 0 institution states.** None is missing from an admitted reading: no source unit is admitted and no reading exists. The contract below establishes a recurring responsibility without fabricating analytical rows.

## Identity and source-facing records

An observation uses `PP-S01NE-E##-OBS-####`; IDs never recycle or change with interpretation. Its mandatory payload is unit ID, exact witness ID and SHA-256 reference from the [source register](../../source-inventory/PP_SOURCE_REGISTER.md), source edition, clock convention, start/end locator, scene ID, observation type, inspectable description, inspector/date, actual modality and any sampling or access limit. Exact dialogue adds text-witness ID, cue/line locator, language, aligned audiovisual interval and whether original wording, subtitle transcription or analytical translation.

Observation types separate directly viewed action/image, directly heard performance/sound, inspected text, character/institution assertion and analyst inference. An inference links the observations from which it follows and its local claim ID; it does not overwrite the observed event. `REPORTED` AV locators are retrieval candidates until reinspected and `ANCHORED` under the [protocol](../../integration/PP_RECONCILIATION_PROTOCOL.md). A timestamp precise to milliseconds does not establish perceptual timing accuracy.

Source coverage is recorded by meaningful scene/segment, including ordinary connective action, OP/ED, credits and post-credit material within the admitted source. List inspected versus missing intervals, continuity breaks, text route, audio route and visual route. Requirement (`REQUIRED`, `OPTIONAL`, `OUT_OF_SCOPE`) and inspection (`COMPLETE_FOR_DECLARED_SCOPE`, `PARTIAL`, `PENDING`, `UNAVAILABLE`, `NOT_APPLICABLE`) are independent. No checksum, extracted frame count or transcript cue count certifies perceptual completion.

Each scene reconstruction preserves presented order, relevant event-time constraint, persons and their information, action/choice, immediate consequence and changed state. It links the reading's narrative prose rather than replacing it. Unknown event dates and inferred offscreen actions remain marked.

## Local state and changes

A local state ID is `PP-S01NE-STATE-####` with versions tied to accepted unit boundaries. Record entity ID, state domain, entering state, source-supported change, resulting state, evidence and local claim IDs, counterevidence, uncertainty and review disposition. Preserve prior states and the transition mechanism. A later-looking summary without transition evidence is insufficient.

Character state separates goals, knowledge, affect, competencies/limits, public role, self-report and supported disposition. Directed relationship state carries subject → object, trust/dependence/obligation/authority/intimacy dimensions as supported, asymmetric information and the concrete exchange behind change. Institution state separates claimed norm, actual process, displayed measurement, enforcement, exception and affected person's consequence. These are installment-scoped records, never rival full biographies or automatically current franchise conclusions.

Known persons use a stable entity ID from the franchise state ledger, a proper name known at this boundary and any purposeful role/alias. If identity is not established, a local provisional ID is used and later linked without backfilling the earlier knowledge boundary. Do not replace recurring named subjects with generic role labels that make their actions hard to retrieve.

## Per-unit maintenance and dependencies

The principal proposes source and state updates with the completed reading. Independent specialists supply their actual source observations; the critical reviewer checks load-bearing source spans, significant omitted persons/scenes and disputed transitions. The integrator alone accepts shared changes. Every material state transition has a route into the [local claim/disclosure ledger](PP_S01NE_CLAIM_AND_DISCLOSURE_LEDGER.md).

At each accepted unit, identify potential franchise implications and existing portrait dependencies. A change that is merely new local detail stays local. A materially changed disposition, directed bond, institutional rule or contradiction becomes a numbered delta under the [reconciliation protocol](../../integration/PP_RECONCILIATION_PROTOCOL.md). If master integration is batched, record the pending delta and the master's earlier boundary; never imply that the master already reflects it.

Corrections retain the original observation identity, describe corrected versus earlier content and link the claim revision. Changed source bytes create another witness. Frozen readings and independent logs remain intact; current ledger entries retain their lineage. The [franchise state ledger](../../franchise/ledgers/PP_FRANCHISE_STATE_LEDGER.md) owns current reconciled conclusions and monograph qualification, not this document.
