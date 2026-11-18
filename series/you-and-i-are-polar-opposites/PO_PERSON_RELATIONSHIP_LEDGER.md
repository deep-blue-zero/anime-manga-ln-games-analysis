---
title: "You and I Are Polar Opposites — person and directed relationship states"
series: you-and-i-are-polar-opposites
artifact_id: PO_PERSON_RELATIONSHIP_LEDGER
artifact_type: longitudinal_state_ledger
generation: PO-G1
version: "1.1"
status: canonical
authority_scope: "Typed source-grounded state schemas and controls; no narrative findings"
source_boundary: "Japanese manga volumes 01-08 plus one unadmitted shared artbook; metadata only, no narrative admission or inspection"
canonical_home: series/you-and-i-are-polar-opposites/PO_PERSON_RELATIONSHIP_LEDGER.md
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
---

# Person and directed relationship states

| Control | State |
|---|---|
| Admitted / inspected main units | 0 / 0 |
| Established people / state / knowledge / directed events | 0 / 0 / 0 / 0 |
| Individual portrait assessments | 0 |
| Artbook narrative evidence | NONE; separately gated |
| Reconstruction | NOT_READY; no model or test |

## Exact schemas

Identity: `subject_key | source_name | preferred_name | aliases/disclosure_points | continuity/frame | first_locator | confidence`, immutable PO-P0001 onward. Project keys are not discovery IDs. Preserve source-required anonymity; no cast is seeded from familiarity.

State: `event_id | subject | volume/scene/horizon | event_time | valid_from/until | prior_event | proposition | disposition/development/temporary_condition | trigger/stakes/constraints | evidence_layer/confidence | change_cause | supporting_locators | counterevidence/alternative | claims/full_reading_anchor`.
Change cause: DISPOSITION, KNOWLEDGE, RELATIONSHIP, CONTEXT, ROLE, RESOURCE, REVEALED_NOT_NEW, UNRESOLVED. A self-description or other's impression remains attributed, not automatically a trait.

Knowledge: `event_id | subject | proposition | KNOWS/BELIEVES/SUSPECTS/UNAWARE/UNKNOWN | acquisition_evidence | event_time | disclosure_horizon | reader_horizon | confidence | predecessor | claims/locators`. UNAWARE needs evidence; unshown is UNKNOWN.

Directed edge: `event_id | from_subject | to_subject | volume/scene/horizon | expressed_position | shown_conduct | recipient_response | inferred_state/confidence | knowledge/power/constraint_asymmetry | prior_edge | counterevidence/alternative | claims/reading/locators`. Reverse state requires its own evidence. A group claim cites constituent edges and unknowns rather than supplies a group mind.

Portrait qualification ([architecture §5](PO_SYNTHESIS_ARCHITECTURE.md#5-studies-and-preservation-of-analytical-depth)): `assessment_id | subject_key | admitted_witness_and_assessment_horizon | prior_assessment_id | outcome | rationale_and_evidence_locators | largest_gaps_and_counterevidence | next_review_trigger | portrait_path_if_produced | portrait_only_self_containment_result_ref | source_fidelity_result_ref`.

Use one immutable assessment ID (`PO-PQ0001` onward) for each decision about a registered `PO-P` subject. Record `QUALIFIED_PENDING`, `COMPLETE_AT_BOUNDARY`, `DEFERRED_EVIDENCE` or `REASSESS_AFTER_REVISION` at the stated horizon. For `COMPLETE_AT_BOUNDARY`, link the portrait and both separate passing reviews at that boundary. On reassessment append a new decision referencing its predecessor so the earlier horizon and outcome remain retrievable. A person without an assessment row is unassessed.

No analytical records exist. Contrast, similarity and reciprocity require inspected support; the title cannot fill the table.

## Updating and history

Append material state/knowledge/edge events in the accepted volume transaction. Current indexes route latest IDs by subject/direction/horizon, preserving all prior events. Correct through `correction_id | prior_record | date | old/new | evidence_basis | affected_claims`; semantic changes also enter claim history.

Coverage updates require `control_event | date | old/new | admitted_scope | evidence_routes | remaining_gap | role`. No-change belongs in the reading manifest unless absence itself matters. Japanese/ordinary samples link to the separate sample ledger.

For an earned model, coverage rows use `subject@state | dimension | evidence_ids | counterevidence | evidence_backed_limit_or_gap | test_status | next_action`. Address the twelve evaluator dimensions and scenario support/limits from architecture §7 without grades. Shared-artbook/cross-title material cannot fill missing main-story character state.
