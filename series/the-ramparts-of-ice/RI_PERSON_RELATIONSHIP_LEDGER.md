---
title: "The Ramparts of Ice — person, relationship and expression states"
series: the-ramparts-of-ice
artifact_id: RI_PERSON_RELATIONSHIP_LEDGER
artifact_type: longitudinal_state_ledger
generation: RI-G1
version: "1.0"
status: canonical
authority_scope: "Typed longitudinal retrieval/coverage controls only; no narrative findings"
source_boundary: "Japanese full-colour tankobon volumes 01-14 metadata verified; no narrative admission or inspection"
canonical_home: series/the-ramparts-of-ice/RI_PERSON_RELATIONSHIP_LEDGER.md
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
---

# Person, relationship and expression states

| Control | Present state |
|---|---|
| Admitted / inspected volumes | 0 / 0 |
| Established people / state / knowledge events | 0 / 0 / 0 |
| Directed edges / Japanese or ordinary samples | 0 / 0 |
| Reconstruction | NOT_READY; no model or test |

Each record links full causal prose and exact witness support. A broad theme or color association cannot substitute for person-level evidence.

## Exact typed schemas

**Identity:** `subject_key | source_name | preferred_name | aliases/disclosure_points | continuity/frame | first_locator | confidence`. Immutable RI-P0001-style project keys are assigned only after inspection, not global discovery IDs. Preserve concealed/uncertain identities.

**State:** `event_id | subject | unit/scene/horizon | event_time | valid_from/until | prior_event | proposition | disposition/development/temporary_condition | trigger/stakes/constraints | evidence_layer/confidence | change_cause | supporting_locators | counterevidence/alternative | claims/full_reading_anchor`. Change cause: DISPOSITION, KNOWLEDGE, RELATIONSHIP, CONTEXT, ROLE, RESOURCE, REVEALED_NOT_NEW, UNRESOLVED.

**Knowledge:** `event_id | subject | proposition | KNOWS/BELIEVES/SUSPECTS/UNAWARE/UNKNOWN | how_acquired | event_time | disclosure_unit | reader_horizon | source_layer/confidence | prior_event | locators/claims`. UNAWARE requires diagnostic evidence; silence is not proof.

**Directed relationship:** `event_id | from | to | unit/scene/horizon | expressed_position | shown_conduct | recipient_response | inferred_state/confidence | knowledge/power/constraint_asymmetry | prior_edge | counterevidence/alternative | claims/reading/locators`. Reverse edges require independent support; no reciprocal state is filled automatically.

**Ordinary/expression sample:** `sample_id | subject | interlocutor/audience | unit/state/horizon | situation/stakes(ORDINARY/CRISIS/MIXED) | opportunity | behavior/inaction | speech/thought/narration/effect_layer | attribution_confidence | brief_Japanese_form/labeled_gloss_if_needed | register/pragmatic_feature | baseline/exception | claims/reading/locators`. Missing opportunity is GAP. Private thought is not spoken register.

All analytical tables contain zero rows. Colour/pose alone cannot establish inner state; link observed form to a separately argued inference.

## Updates, corrections and coverage

Append material records with each accepted volume. Stable IDs and initial disclosure horizons survive. Current indexes route latest IDs by subject/direction/horizon without replacing history. Correct through `correction_id | prior_record | date | old/new | source_basis | affected_claims`; interpretive changes enter claim history.

Coverage controls change only with `event_id | date | old/new | unit_scope | evidence_routes | remaining_gap | role`. No-change belongs in the reading manifest unless the absence itself matters. At checkpoints check ordinary and crisis contexts, actual interlocutor variety, source layers and contradictory cases.

For an earned model, coverage uses `subject@state | dimension | support_ids | counterevidence | evidence_backed_limit_or_gap | test_status | next_action`. Address psychological model, longitudinal state, written register, mundane behavior, directed relationships, interiority, conflict, ethics, humor, source completeness, negative evidence and temporal specificity; describe scenario limits without grading capability.
