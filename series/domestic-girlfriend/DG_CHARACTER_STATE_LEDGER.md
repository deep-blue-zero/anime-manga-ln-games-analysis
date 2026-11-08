---
title: "Domestic Girlfriend — character and knowledge states"
series: domestic-girlfriend
artifact_id: DG_CHARACTER_STATE_LEDGER
artifact_type: character_state_ledger
generation: DG-G1
version: "1.0"
status: canonical
authority_scope: "Longitudinal schema and control state; zero character findings"
source_boundary: "Metadata reconnaissance of Japanese manga volumes 01-03 only; no narrative units admitted or inspected"
canonical_home: series/domestic-girlfriend/DG_CHARACTER_STATE_LEDGER.md
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
---

# Character and knowledge states

## Responsibility and current control

This is the retrieval home for named subjects and their changing states. It preserves the distinction between behavioral development, newly disclosed information and transient context. Causal explanation remains in the full reading. The opening acquisition cannot warrant a whole-life model.

| Control | Value | Consequence |
|---|---|---|
| Admitted / inspected narrative units | 0 / 0 | No cast or character rows may be inferred from metadata |
| Registered project-local subjects | 0 | Names and aliases await source-grounded establishment |
| Behavioral state events / knowledge events | 0 / 0 | No analytical high-water mark exists |
| Source frontier | Available V01–03; unadmitted | Later character knowledge is excluded |
| Reconstruction use | NOT_READY | Schema presence supplies no characterization |

## Identity table schema

One row per source-established person/continuity; columns: `subject_key | preferred_name | source_form | aliases_with_first_disclosure | continuity | first_locator | identity_confidence | reading_anchor`. Use immutable DG-P0001-style project-local keys; these are not global discovery IDs. Names remain exactly sourced; proposed romanization is labeled until verified. Never merge people because their roles coincide. If identity is concealed, use a stable source-faithful label with an unresolved identity relation; append the later resolution without rewriting the earlier horizon.

| Subject key | Preferred name | Source form | Aliases / first disclosure | Continuity | First locator | Identity confidence | Reading anchor |
|---|---|---|---|---|---|---|---|

No subject rows exist.

## State-event schema

One row per material change or diagnostic state confirmation, with immutable ID DG-CS0001 onward. Required columns are shown; longer reasoning belongs at the linked reading anchor.

| Event ID | Subject key | Presentation unit / event time | Valid from / until | State and change cause | Trigger / perceived stakes | Action and constraints | Evidence / confidence | Counterevidence / alternative | Claim IDs / reading / locators | Prior event |
|---|---|---|---|---|---|---|---|---|---|---|

`event time` is the source-established chronology or UNKNOWN, never invented dates. `valid_until` is OPEN until supported. `state` distinguishes disposition candidate, developmental state and temporary condition. Change cause uses DISPOSITION, KNOWLEDGE, RELATIONSHIP, CONTEXT, ROLE, RESOURCE, REVEALED_NOT_NEW or UNRESOLVED. An observed episode does not alone establish disposition. Evidence labels/confidence inherit the method; a textual self-report remains labeled even when the character appears sincere.

## Knowledge-event schema

One row per material acquisition, belief, ignorance or correction: `knowledge_id | subject_key | proposition | status(KNOWS/BELIEVES/SUSPECTS/UNAWARE/UNKNOWN) | disclosure_unit | event_time | how_available_to_subject | reader_horizon | evidence_label/confidence | source_locator | reading_anchor | predecessor_id`. UNAWARE requires evidence; silence is UNKNOWN without diagnostic opportunity. Record one person's belief about another as the first person's belief, not the other's mental state. No knowledge rows exist.

## Update, current view and history

During each accepted volume transaction, append state and knowledge events for material changes and justified confirmations. Use stable IDs, never renumber. A current-view table, when needed, contains only `subject_key | latest_state_event_ids | latest_knowledge_event_ids | through_unit | unresolved_claim_ids`; it routes to events rather than overwriting them.

Corrections append an event with predecessor, corrected proposition, basis and date, and a claim transition where meaning changes. Existing rows, first-disclosure facts and freezes remain intact. A new cutoff must not erase earlier state. If no material update is needed, record that in the reading's ledger manifest, not fictitious rows. Ordinary-life examples link to the register/everyday ledger. The character ledger owns state meaning; the expression ledger owns contextual sample retrieval.

Before unit acceptance, check every materially active person has either supported state treatment or an explicit scope reason in the reading. Check names, actor/observer attribution, episode versus disposition, knowledge asymmetry and the exact evidence frontier. Reconstruction consumers must retrieve the underlying prose and source support.
