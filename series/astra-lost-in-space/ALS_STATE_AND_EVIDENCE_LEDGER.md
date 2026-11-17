---
title: "Astra Lost in Space — longitudinal state and evidence"
series: astra-lost-in-space
artifact_id: ALS_STATE_AND_EVIDENCE_LEDGER
artifact_type: longitudinal_state_ledger
generation: ALS-G1
version: "1.0"
status: canonical
authority_scope: "Typed unit/state/evidence schemas and controls; zero narrative findings"
source_boundary: "One Japanese 彼方のアストラ 全巻合本版 omnibus EPUB; internal units unverified; no narrative admission or inspection"
canonical_home: series/astra-lost-in-space/ALS_STATE_AND_EVIDENCE_LEDGER.md
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
---

# Longitudinal state and evidence

## Current controls

| Control | State |
|---|---|
| Verified internal units | 0 |
| Admitted / inspected units | 0 / 0 |
| Established subjects / state / knowledge / directed-edge events | 0 / 0 / 0 / 0 |
| Ordinary/Japanese expression samples | 0 |
| Reconstruction | NOT_READY; no model or test |

All analytical records require a verified unit key from the source map. An omnibus-wide file label cannot substitute for a local knowledge horizon.

## Exact typed schemas

**Identity:** `subject_key | source_name | preferred_name | aliases/first_disclosure | continuity/frame | first_unit/locator | confidence`, using immutable ALS-P0001 onward. Preserve concealment and unresolved identity rather than importing a cast.

**Scene:** `unit/scene_id | global_start/end_image | actual_chapter_label_or_UNKNOWN | presentation_order | event_time | frame/confidence | active_subjects | entering_state_refs | causal_claims | exit_state_refs | disclosure_horizon | full_reading_anchor`. Event time may be UNKNOWN; global image ordinals never reset.

**State:** `state_event_id | subject | unit/scene/horizon | valid_from/until | prior_event | proposition | disposition/development/temporary_condition | trigger/stakes/constraints | evidence_layer/confidence | change_cause | support | counterexample/alternative | claims/reading/locators`. Change causes: DISPOSITION, KNOWLEDGE, RELATIONSHIP, CONTEXT, ROLE, RESOURCE, REVEALED_NOT_NEW, UNRESOLVED.

**Knowledge:** `knowledge_event_id | subject | proposition | KNOWS/BELIEVES/SUSPECTS/UNAWARE/UNKNOWN | how_acquired | event_time | disclosure_unit | reader_horizon | evidence/confidence | predecessor | claims/locators`. UNAWARE needs source support; unshown is UNKNOWN. A later reader disclosure is not automatically a character-state change.

**Directed relationship:** `edge_event_id | from_subject | to_subject | unit/scene/horizon | expressed_position | shown_conduct | recipient_response | inferred_state/confidence | knowledge/power/constraint_asymmetry | prior_edge | counterevidence/alternative | claims/reading/locators`. Reverse edges require independent support.

**Contextual sample:** `sample_id | subject | interlocutor/audience | unit/state/horizon | situation/stakes(ORDINARY/CRISIS/MIXED) | diagnostic_opportunity | behavior/inaction | text_layer/attribution_confidence | brief_Japanese_form/labeled_gloss_if_needed | register/pragmatic_feature | baseline/exception_links | claims/reading/locators`. Private thought is not speaking style; missing opportunity is GAP.

No analytical records exist.

## Update/history contract

Append material events/samples with each accepted mapped-unit reading. Stable IDs and global source coordinates remain fixed. Current indexes route latest state/knowledge/edge IDs by subject and horizon without replacing historical records.

Corrections append `id | prior_record | date | old/new | source_basis | affected_claims`. Meaning changes enter claim history; frozen entering/exit states remain intact. A source-map correction triggers crosswalk and locator review rather than renumbering facts silently.

Coverage controls change only with `control_event | date | old/new | verified_unit_scope | evidence_routes | remaining_gap | role`. No-change is a reasoned reading-manifest statement, not filler rows. Full causal prose remains the interpretive home.

When a model is earned, coverage rows use `subject@state | dimension | evidence_ids | counterevidence | evidence_backed_limit_or_gap | test_status | next_action`. Address psychological model, longitudinal state, Japanese register, mundane behavior, directed relationships, interiority, conflict, ethics, humor, source completeness, negative evidence and temporal specificity, with scenario limits but no capability grades.
