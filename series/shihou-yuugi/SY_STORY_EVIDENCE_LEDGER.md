---
title: "Shihou Yuugi — story-local evidence ledger"
series: shihou-yuugi
artifact_id: SY_STORY_EVIDENCE_LEDGER
artifact_type: story_evidence_ledger
generation: SY-G1
version: "1.0"
status: canonical
authority_scope: "Typed story-scoped retrieval and coverage controls; no narrative findings"
source_boundary: "One Japanese four-story anthology EPUB, metadata verified; all story narratives unadmitted and uninspected"
canonical_home: series/shihou-yuugi/SY_STORY_EVIDENCE_LEDGER.md
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
---

# Story-local evidence ledger

## Scope controls

Every analytical key begins with its work key. A collection-wide cast/state ledger would collapse unrelated subjects, so this compact file holds independently scoped typed records.

| Work | Admitted / inspected | Subjects / states / directed edges / expression samples | Reconstruction |
|---|---|---|---|
| SY-W01 | 0 / 0 | 0 / 0 / 0 / 0 | NOT_READY |
| SY-W02 | 0 / 0 | 0 / 0 / 0 / 0 | NOT_READY |
| SY-W03 | 0 / 0 | 0 / 0 / 0 / 0 | NOT_READY |
| SY-W04 | 0 / 0 | 0 / 0 / 0 / 0 | NOT_READY |

These are bibliographic control rows, not character evidence. No narrative records exist.

## Scene and identity schemas

Scene: `work/scene_id | source_span | actual_presentation_order | event_time_or_UNKNOWN | frame/confidence | active_subject_keys | entering_state_refs | causal_change_claims | exit_state_refs | disclosure_horizon | reading_anchor | inspection_limits`.

Identity: `work/subject_key | source_name | preferred_name | aliases/disclosure_points | continuity/frame | first_locator | identity_confidence`.

Use immutable work-qualified suffixes S0001 and P0001. Similar names across stories remain different identities. Concealed identities retain source-faithful labels until resolved at their actual disclosure frontier. These are project keys, not global discovery IDs.

## State and knowledge schema

`work/state_event_id | subject_key | scene/horizon | event_time | validity_from/until | prior_event | state_proposition | disposition/development/situation | trigger/stakes/constraint | source_layer | change_cause | evidence/confidence | counterevidence/alternative | claim_ids/reading_anchor/locators`.

Source layer distinguishes direct behavior, self-report, inner presentation and another's report. Change cause is DISPOSITION, KNOWLEDGE, RELATIONSHIP, CONTEXT, ROLE, RESOURCE, REVEALED_NOT_NEW or UNRESOLVED. Knowledge records additionally name knower, proposition, KNOWS/BELIEVES/SUSPECTS/UNAWARE/UNKNOWN and acquisition evidence; UNAWARE requires diagnostic support.

## Directed relationships

`work/edge_event_id | from_subject | to_subject | scene/horizon | expressed_position | shown_conduct | recipient_response | inferred_state/confidence | knowledge/power/constraint_asymmetry | prior_edge_event | counterevidence/alternative | claim_ids/reading_anchor/locators`.

Use R0001 onward within each work. The reverse direction requires independent evidence. Cross-story comparison of a relationship pattern cites separately supported local edges and never becomes a cross-story relationship.

## Japanese and ordinary-context samples

`work/sample_id | subject | interlocutor/audience | scene/state/horizon | stakes(ORDINARY/CRISIS/MIXED) | opportunity | behavior/inaction | speech/thought/narration/effect_layer | attribution_confidence | brief_Japanese_form/labeled_gloss_if_needed | pragmatic/register_feature | baseline/exception | reading_anchor/locators/claims`.

Use X0001 onward. A silent behavioral sample need not contain quoted text. Missing opportunity is a gap, not negative evidence. Private thought is not spoken register. A model cannot infer an ordinary baseline from crisis samples alone.

## Update/history and readiness

Append material records within the accepted story transaction. Never renumber IDs or rewrite earlier state to match an ending or collection comparison. Current-view indexes route latest event IDs by work/person/horizon without replacing history. Corrections append `correction_id | prior_record | date | old/new | source_basis | affected_claims`; interpretive changes enter the claim ledger.

Control updates append `control_event | work | date | old_coverage | new_coverage | evidence_routes | remaining_gap | role`. Per-subject reconstruction coverage, only when earned, uses `work/subject@state | dimension | evidence_ids | counterevidence | evidence_backed_limit_or_gap | test_status | next_action`. No grades or simulation outputs enter this ledger.

Coverage checks include psychological/behavioral model, temporal state, Japanese register, mundane behavior, directed relationships, interiority, conflict, ethical deliberation, humor, source completeness, negative evidence and temporal specificity, plus scenario support/limits. The architecture owns independent evaluation. The full reading remains the explanatory home; rows provide exact retrieval.
