---
title: "Look Back — scene and state evidence"
series: look-back
artifact_id: LB_SCENE_AND_STATE_LEDGER
artifact_type: scene_state_evidence_ledger
generation: LB-G1
version: "1.0"
status: canonical
authority_scope: "Typed retrieval schemas and coverage controls; zero narrative evidence"
source_boundary: "One Japanese standalone manga EPUB, metadata verified; narrative admission and inspection NONE"
canonical_home: series/look-back/LB_SCENE_AND_STATE_LEDGER.md
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
---

# Scene and state evidence

## Compact responsibility, explicit internal schemas

A standalone needs cumulative retrieval across its scenes, not empty per-volume trackers. This file is a set of separately typed records sharing one scene coordinate system. Each record links full causal prose and exact source evidence. It never replaces that prose.

| Control ID | Current state | Consequence |
|---|---|---|
| LB-COV-01 | 0 admitted/inspected narrative units | No mapped scenes or narrative facts |
| LB-COV-02 | 0 established subjects / state events | No character profile or model |
| LB-COV-03 | 0 directed relationship events | Reciprocity unassessed |
| LB-COV-04 | 0 ordinary/contextual or Japanese expression samples | No behavioral baseline or written voice |
| LB-COV-05 | Reconstruction NOT_READY; tests NOT_RUN | No capability assessment or simulation |

## Scene records

Required schema: `scene_id | witness | actual_start/end_locators | presentation_order | event_time_or_UNKNOWN | frame_and_confidence | active_subject_keys | entering_state_refs | causal_change_claim_ids | exit_state_refs | disclosure_frontier | reading_anchor | inspection_limit`.

Assign LB-S0001-style IDs only after actual source mapping. A scene's significance must be argued in the reading; a segment boundary is not an interpretation. Never invent calendar dates or story-time order from image order.

## Subject and state records

Identity schema: `subject_key | source_name | preferred_name | aliases/disclosure_points | continuity/frame | first_locator | confidence`. Use LB-P0001 onward; these project-local keys are not discovery IDs. Preserve anonymous labels until names are source-established.

State schema: `state_event_id | subject_key | scene_id | valid_from/until | disclosure_horizon | behavior/self_report/interiority/report_layer | state_proposition | disposition_vs_development_vs_situation | trigger/stakes/constraints | change_cause | evidence/confidence | counterexample_or_alternative | claim_ids | reading_anchor/locators | prior_event`.

Change cause is DISPOSITION, KNOWLEDGE, RELATIONSHIP, CONTEXT, ROLE, RESOURCE, REVEALED_NOT_NEW or UNRESOLVED. Knowledge assertions name knower, proposition, KNOWS/BELIEVES/SUSPECTS/UNAWARE/UNKNOWN, how acquired and reader horizon. UNAWARE needs evidence; an unshown possibility is UNKNOWN.

## Directed-edge records

`edge_event_id | from_subject | to_subject | scene/horizon | expressed_position | shown_conduct | recipient_response | inferred_state/confidence | knowledge/power/constraint_asymmetry | counterevidence | prior_edge_event | claim_ids/reading_anchor/locators`.

Use LB-R0001 onward; each direction needs its own support. Do not seed mutual states from a scene's emotional framing. A group claim must identify constituent supported edges and unknowns.

## Expression and ordinary-situation records

`sample_id | subject | interlocutor/audience | scene/state/horizon | stakes(ORDINARY/CRISIS/MIXED) | opportunity | shown_behavior | text_layer/attribution_confidence | brief_Japanese_form/labeled_gloss_if_needed | register_or_pragmatic_feature | baseline/exception_links | claim_ids/reading_anchor/locators`.

Use LB-X0001 onward. No quotation is required for a wordless behavioral sample. Japanese wording requires page verification. Mark private thought separately from speech. An absent behavior is negative evidence only when the scene supplies a diagnostic opportunity; otherwise record a gap.

All analytical record sets currently contain **zero rows**.

## History and update rules

Append material scene/state/edge/sample records during the authorized work transaction. Stable IDs never renumber. Current indexes may point to latest event IDs but do not replace historical rows. Corrections append `correction_id | prior_record | date | old/new | source_basis | affected_claims`; interpretive changes also enter the claim ledger.

Coverage controls update only with real evidence, alongside `control_event_id | date | old_state | new_state | basis | residual_gap | role`. No-change statements belong in the reading's update manifest unless the absence is meaningful evidence. An exact locator or inspection limitation cannot be dropped during stylistic revision.

At reconstruction review, map evidence/limits to psychological model, longitudinal state, written register, mundane behavior, directed relationships, interiority, conflict, ethical deliberation, humor, source completeness, negative evidence and temporal specificity. Describe scenario support/gaps without self-assigned grades. The architecture owns separate model and independent-test requirements.
