---
title: ROAD TO THE TOP Race and Competition Ledger
artifact_id: UM_RTTT_RACE_COMPETITION_LEDGER
artifact_type: race_competition_ledger
series: uma-musume
installment: road-to-the-top
generation: V1
status: canonical
scope: Depicted competition, audiovisual staging and separately sourced historical comparison
source_boundary: "2023 original four-episode anime; no narrative sources admitted at bootstrap"
created: 2026-11-22
last_updated: 2026-11-22
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
do_not_use_as_literary_evidence: true
---

# Race and competition ledger

This ledger asks how a competition is staged and experienced, and how it affects particular characters. **Depicted races allocated: 0. Historical context facts allocated: 0.** Satsuki Sho, Tokyo Yushun / Japanese Derby and Kikuka Sho are investigation targets, not an entered anime chronology or a preloaded result. Read alongside the [AV ledger](UM_RTTT_AV_MOTIF_PERFORMANCE_LEDGER.md) and [method](../00_Method/UM_RTTT_ANALYTICAL_METHOD.md).

## Depicted-race schema

Allocate `RTTT-E01-RACE01` for an actual inspected depiction; do not allocate an ID from an external race list. A repeated or remembered depiction links the original race ID and retains its own observed source interval. The following is an **unallocated template**.

```yaml
race_id: TEMPLATE_UNALLOCATED
episode: TEMPLATE
source_id: TEMPLATE_MANIFEST_ID
edition: TEMPLATE
source_interval: {start: TEMPLATE, end: TEMPLATE}
diegetic_race_name_and_text_witness: TEMPLATE_OR_UNNAMED
depiction_mode: TEMPLATE_PRESENT_MEMORY_REPORT_MONTAGE_UNCERTAIN
participants_identified_in_source: []
participant_identity_uncertainties: []
pre_race_stakes_by_character: TEMPLATE_WITH_CS_AND_CLM_REFS
scene_and_observation_ids: []
staging_phase_refs: []
depicted_result_and_witness: TEMPLATE_OR_NOT_ESTABLISHED
aftermath_and_character_state_refs: []
historical_context_ids: []
adaptation_claim_ids: []
independent_contribution_and_review_refs: []
record_state: DRAFT
```

## Phase capture

Within each race, add a phase row for analytically consequential changes. Phases follow observed action rather than a predetermined start/middle/finish formula. Source intervals and observation IDs are mandatory; every interpretation uses a claim ID.

| Field | Capture responsibility |
|---|---|
| Spatial staging | Runner positions, depth, lateral relations, visibility and what establishes identity; leave unseen positions unknown |
| Pace and movement | Perceived acceleration/deceleration, gait and camera trajectory only through an adequate continuous route; separate an editorial impression from physical measurement |
| Camera and composition | Angle, framing, scale, objective/subjective viewpoint cues and their uncertainty |
| Shot/edit timing | Shot IDs, boundaries, measured durations, cuts and transitions; distinguish measured time from perceived rhythm |
| Body and expression | Animation, gaze, effort, strain or other visible details; emotional meaning remains an interpretation |
| Audio layers | Breathing/exertion, voice, footsteps/environment, crowd and commentary, with track/channel and inspected-route references |
| Music and silence | Cue entry/exit, development, energy change, relative silence and relation to image or dialogue, with timing evidence |
| Emotional and competitive stakes | Which character's stakes are expressed, inferred or withheld; rivalry/support/disclosure changes linked to CS/RS/CLM IDs |
| Perceptual effect | The argued viewer experience and why, including an alternative explanation and limits |

A finishing position alone does not explain the dramatic construction of a race. Do not infer unseen athletic mechanics from a cut, treat simulated camera movement as physical camera metadata, or treat commentary as omniscient narration without examining its status. A crowd reaction must be observed before its meaning is inferred.

## Historical-context schema

Allocate installment-wide `RTTT-CTX0001` only for an externally verified fact. Prefer JRA records and other authoritative race archives, with original Japanese naming and date. Store history separately from fictional characterization. The template below contains no race result.

```yaml
context_id: TEMPLATE_UNALLOCATED
epistemic_state: EXTERNAL_CONTEXTUAL_FACT
historical_subject_and_date: TEMPLATE
fact: TEMPLATE_PRECISE_BOUNDED
authoritative_reference: TEMPLATE_URL_RECORD_IDENTIFIER
retrieval_date: TEMPLATE
reference_locator: TEMPLATE_TABLE_RACE_OR_SECTION
translation_or_name_variants: []
uncertainty_or_conflicting_records: []
related_depicted_race_ids: []
anime_observation_ids: []
adaptation_claim_ids: []
```

For a later historical-adaptation claim, compare the external fact with separately observed anime evidence: what is preserved, omitted, rearranged, personified or transformed, and what remains uncertain. An apparent parallel does not prove authorial intention. Never backfill an anime winner, participant, date, emotion or relationship from a historical result.

## Revision and acceptance

Keep depicted-race facts, performance observations and adaptation interpretations distinct. A new source edition receives a new source binding; theatrical additions never overwrite the episodic account. Correct a misidentified runner or mistaken locator with a dated revision preserving the old record and review affected state and claim links. Record `DRAFT`, `ACCEPTED`, `DISPUTED`, `CORRECTED` or `WITHDRAWN`, with independent reviewer and integrator dispositions in the episode transaction record. All accepted race interpretations require the actual inspected channel; no sampled still set certifies motion, performance or musical timing.

## Race and context records

None. Original episode footage and authoritative historical records must be examined independently before either record class is populated.
