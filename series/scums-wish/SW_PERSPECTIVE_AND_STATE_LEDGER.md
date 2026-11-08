---
title: "Scum’s Wish — perspective and character states"
series: scums-wish
artifact_id: SW_PERSPECTIVE_AND_STATE_LEDGER
artifact_type: character_state_ledger
generation: SW-G1
version: "1.0"
status: canonical
authority_scope: "Subject/perspective/state schemas and controls; no character findings"
source_boundary: "Metadata reconnaissance of Japanese main manga volumes 01-08 and decor volume 09; no narrative units admitted or inspected"
canonical_home: series/scums-wish/SW_PERSPECTIVE_AND_STATE_LEDGER.md
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
---

# Perspective and character states

## Responsibility and present control

This ledger preserves who acts, who describes the act, whose inner life is presented and what each person can know. It prevents an account of desire or motive from becoming an unattributed fact, and separates actual development from later disclosure. The full reading owns the causal explanation.

| Control | Current value |
|---|---|
| Admitted / inspected units | 0 / 0 |
| Established subjects | 0 |
| Perspective observations / state events | 0 / 0 |
| MAIN and DECOR horizons | Both unadmitted; kept distinct |
| Model readiness | NOT_READY |

## Subject identities

Required identity fields: `subject_key | preferred_name | Japanese_form | aliases_and_disclosure_points | continuity_or_frame | first_locator | identity_confidence | reading_anchor`. Assign immutable SW-P0001-style project keys only from inspected evidence. These do not create global discovery IDs. Preserve source-required anonymity and unresolved identity relations; later naming does not retroactively identify a person in a scene whose horizon concealed it.

No subject rows exist.

## Perspective observation schema

Each SW-PO0001-style observation records one consequential access or attribution distinction.

| Observation ID | Subject described | Observer / speaker / thinker | Source layer and attribution confidence | Proposition or presented behavior | Event time / disclosure position | Subject knowledge / reader horizon | Observation versus self-report/inference | Counterevidence / alternative | Claim IDs / reading anchor / exact locators |
|---|---|---|---|---|---|---|---|---|---|

Source layer is SPEECH, THOUGHT, NARRATION, REPORTED_ACCOUNT, DRAWN_ACTION, DIEGETIC_TEXT or UNKNOWN. Do not fold one into another. Person-knowledge values are KNOWS, BELIEVES, SUSPECTS, UNAWARE or UNKNOWN; UNAWARE needs evidence of an opportunity and its absence. Explicitly distinguish a person's belief about another's motives from evidence of those motives. An ambiguous balloon gets unresolved attribution, not a confident identity guessed from familiarity.

## State-event schema

Required event fields: `event_id | subject_key | MAIN_or_DECOR | presentation_unit | event_time | valid_from | valid_until | prior_event | current_state | trigger/stakes | observed_response | constraints | change_cause | supporting_perspective_ids | counterevidence | claim_ids | reading_anchor/locators`. Use SW-CS0001 onward. Event time may be UNKNOWN; validity cannot be fabricated from publication order.

Separate disposition candidate, developmental state and temporary condition. Change cause is DISPOSITION, KNOWLEDGE, RELATIONSHIP, CONTEXT, ROLE, RESOURCE, REVEALED_NOT_NEW or UNRESOLVED. A newly available decor explanation may change analyst knowledge without changing the person's earlier state. Record both coordinates.

No perspective or state events exist.

## Update and history contract

Append events at each material authorized reading transaction. Keep IDs, earlier propositions, exposure horizons and evidence routes stable. A later correction appends `correction_id | prior_record | date | old_formulation | new_formulation | reason/evidence | affected_claims`; meaning changes also enter the claim revision ledger. Do not erase earlier uncertainty.

A current-view index, when earned, contains `subject_key | horizon | latest_state_event_ids | unresolved_perspective_ids | knowledge_claim_ids`. MAIN-only and DECOR-aware views remain separately retrievable. This is an index, not a new character narrative.

Check each materially active person for state treatment or a reasoned scope exception. A narrator's presentation, a subject's self-description and another person's account must not collapse into one psychological profile. Link ordinary/contextual examples to the expression/situation ledger and relational changes to directed events. No-change statements belong in the reading's manifest unless absence itself is diagnostic.
