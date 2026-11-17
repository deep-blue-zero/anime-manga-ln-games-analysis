---
title: "Summer Time Rendering — person and relationship states"
series: summer-time-rendering
artifact_id: STR_PERSON_RELATIONSHIP_LEDGER
artifact_type: longitudinal_state_ledger
generation: STR-G1
version: "1.0"
status: canonical
authority_scope: "Typed person/edge/ordinary-register schemas and controls; no character findings"
source_boundary: "Japanese main manga volumes 01-13 and 2026 未然事故物件 supplement; metadata only, no narrative admission or inspection"
canonical_home: series/summer-time-rendering/STR_PERSON_RELATIONSHIP_LEDGER.md
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
---

# Person and relationship states

| Control | State |
|---|---|
| Source-established subjects | 0 |
| State events / directed relationships / contextual samples | 0 / 0 / 0 |
| Main/supplement models | NONE / NONE |
| Reconstruction | NOT_READY; tests NOT_RUN |

## Exact typed schemas

Identity: `subject_key | source_name | preferred_name | aliases/first_disclosure | continuity/frame_if_established | first_locator | confidence`, using STR-P0001 onward. Similar appearance or role cannot merge identities. Preserve concealment and uncertain relations.

State: `event_id | subject | source_track/unit/scene/horizon | event_or_occurrence_ref | valid_from/until | prior_state | proposition | disposition/development/temporary_condition | trigger/stakes/constraints | evidence_layer/confidence | change_cause | support | counterevidence/alternative | knowledge_refs | claims/full_reading_anchor/locators`.
Change cause DISPOSITION, KNOWLEDGE, RELATIONSHIP, CONTEXT, ROLE, RESOURCE, REVEALED_NOT_NEW, UNRESOLVED. A later reader explanation is not necessarily behavioral change.

Directed relationship: `edge_id | from | to | track/unit/scene/horizon | occurrence_ref_if_needed | expressed_position | shown_conduct | recipient_response | inferred_state/confidence | knowledge/power/constraint_asymmetry | prior_edge | counterevidence/alternative | claims/reading/locators`. Reverse evidence is independent; no shared feeling or group knowledge assumed.

Ordinary/Japanese sample: `sample_id | subject | interlocutor/audience | track/unit/state/horizon | situation/stakes(ORDINARY/CRISIS/MIXED) | diagnostic_opportunity | shown_behavior/inaction | speech/thought/narration/effect_layer | attribution_confidence | brief_Japanese_form/labeled_gloss_if_needed | register/pragmatic_feature | baseline/exception | claims/reading/locators`. Unrepresented situations are gaps; private thoughts are not spoken register.

All analytical rows are absent. No character dossier is inferred from title or familiarity.

## History and readiness

Append material records atomically with accepted reading. Current views route latest state/edge IDs by subject and horizon without replacing old states. Corrections use `id | prior_record | date | old/new | source_basis | affected_claims`; meaning changes enter claim history. Main-only and supplementary states remain distinct.

Coverage control events record `date | old/new | actual_scope | evidence_routes | residual_gap | role`. A justified no-change belongs in the reading manifest. Ordinary/contextual examples must remain visible even if causal mysteries or conflicts dominate the reading.

Future reconstruction coverage uses `subject@state | dimension | evidence_ids | counterevidence | evidence_backed_limit_or_gap | test_status | next_action`. Address psychological model, temporal state, Japanese register, mundane behavior, directed conditioning, interiority, conflict, ethics, humor, source completeness, negative evidence and temporal specificity, with scenario limits. No capability grade or synthetic output is source evidence.
