---
title: "Tatsuki Fujimoto Before Chainsaw Man — story states and samples"
series: tatsuki-fujimoto-before-chainsaw-man
artifact_id: TF_STORY_STATE_LEDGER
artifact_type: story_evidence_ledger
generation: TF-G1
version: "1.0"
status: canonical
authority_scope: "Work-qualified retrieval/coverage schemas only; no narrative findings"
source_boundary: "Japanese 藤本タツキ短編集 22-26 only; 17-21 absent; no narrative admission or inspection"
canonical_home: series/tatsuki-fujimoto-before-chainsaw-man/TF_STORY_STATE_LEDGER.md
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
---

# Story states and samples

## Controls

| Control | Actual state | Limit |
|---|---|---|
| Available source volume | 22–26 only | 17–21 absent |
| Mapped story spans | 0 | Four-story bibliographic count is not mapping |
| Admitted / inspected stories | 0 / 0 | No narrative facts |
| Subjects / state events / edges / expression samples | 0 / 0 / 0 / 0 | No character model |
| Reconstruction tests / capability | NOT_RUN / NOT_ASSESSED | No self-certification |

All narrative records require a verified collection/story key. No collective “Fujimoto character” identity exists.

## Typed record schemas

**Scene:** `collection/story/scene_id | witness/start/end_locators | actual_presentation_order | event_time_or_UNKNOWN | frame/confidence | active_subjects | entering_state_refs | causal_claims | exit_state_refs | disclosure_horizon | full_reading_anchor | coverage_limit`.

**Identity:** `collection/story/subject_key | source_name | preferred_name | aliases/disclosure_points | continuity/frame | first_locator | confidence`. Assign immutable P0001-style suffixes only after inspection; similar names in another work remain different subjects.

**State:** `work/state_event_id | subject | scene/horizon | event_time | valid_from/until | prior_event | proposition | disposition/development/temporary_condition | trigger/stakes/constraints | evidence_layer/confidence | change_cause | supporting_locators | counterexample/alternative | claims/reading_anchor`. Change cause: DISPOSITION, KNOWLEDGE, RELATIONSHIP, CONTEXT, ROLE, RESOURCE, REVEALED_NOT_NEW or UNRESOLVED.

**Knowledge:** `work/knowledge_event_id | subject | proposition | KNOWS/BELIEVES/SUSPECTS/UNAWARE/UNKNOWN | how_acquired | event_time | disclosure_horizon | reader_horizon | support/confidence | prior_event`. UNAWARE requires diagnostic evidence; lack of inspection is UNKNOWN.

**Directed edge:** `work/edge_event_id | from | to | scene/horizon | expressed_position | shown_conduct | recipient_response | inferred_state/confidence | knowledge/power/constraint_asymmetry | prior_edge | counterevidence/alternative | claims/reading/locators`. Reverse edges require their own evidence.

**Situated expression/behavior:** `work/sample_id | subject | interlocutor/audience | scene/state/horizon | ORDINARY/CRISIS/MIXED | diagnostic_opportunity | shown_behavior/inaction | speech/thought/narration/effect_layer | attribution_confidence | brief_Japanese_form/labeled_gloss_if_needed | register/pragmatic_feature | baseline/exception | claims/reading/locators`. A silent sample need not contain text. Missing opportunity is GAP, not negative evidence. Keep private thought distinct from public speaking habits.

All record sets contain zero rows. IDs are assigned only when evidence exists, never from marketing summaries.

## Updates and historical preservation

Append material records in the same accepted story transaction. Never renumber, overwrite original states or import another story's knowledge. A current index routes latest event IDs by work/person/horizon; it does not replace events. Corrections append `id | prior_record | date | old/new | source_basis | affected_claims`; interpretive changes also enter claim history.

Coverage changes append `control_event | date | work/subject | old/new | evidence_routes | remaining_gap | role`. A later 17–21 source receives separate collection-qualified records, never silently extends an old 22–26 view.

When reconstruction is earned, coverage rows use `subject@state | dimension | evidence_ids | counterevidence | evidence_backed_limit_or_gap | test_status | next_action`. Check psychological/behavioral model, temporal state, Japanese register, mundane behavior, directed relationships, interiority, conflict, ethics, humor, source completeness, negative evidence and temporal specificity, plus scenario limits. Describe coverage without capability grades. Full prose remains the explanatory home.
