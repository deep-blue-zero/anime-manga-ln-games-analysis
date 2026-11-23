---
title: ROAD TO THE TOP Scene and Evidence Ledger
artifact_id: UM_RTTT_SCENE_EVIDENCE_LEDGER
artifact_type: scene_evidence_ledger
series: uma-musume
installment: road-to-the-top
generation: V1
status: canonical
scope: Scene chronology and recoverable primary-source observations
source_boundary: "2023 original four-episode anime; no narrative sources admitted at bootstrap"
created: 2026-11-22
last_updated: 2026-11-22
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
do_not_use_as_literary_evidence: true
---

# Scene and evidence ledger

This is the canonical locator and observation home under the [analytical method](../00_Method/UM_RTTT_ANALYTICAL_METHOD.md). **Accepted scene records: 0. Accepted observation records: 0.** The schemas below are operational instructions, not findings. The four episode templates carry no scene chronology yet.

## Identity and clocks

Allocate scenes as `RTTT-E01-SC001` and observations as `RTTT-E01-OBS0001`; substitute E02–E04 as appropriate. IDs are immutable and episode-local counters only increase. A scene is a coherent dramatic situation; an observation is one recoverable detail or bounded cluster with one locator. Do not equate scenes with shots or make an observation from every sampled frame. Split a record when its channel, source edition or confidence needs a different assessment.

Every locator binds `source_id`, edition and SHA-256 from the [source inventory](../01_Sources/UM_RTTT_SOURCE_INVENTORY.md). Use source presentation time `HH:MM:SS.mmm` from the first presentation timestamp under the documented clock mapping. Preserve original stream PTS and any offset when needed. An interval means `[start,end)`; label approximate boundaries. A cropped clip or subtitle time is a derivative clock, never silently the source clock. Cite the clip's source offset and the frame/shot/cue IDs that permit retrieval. Other editions need a distinct source ID and an explicit crosswalk; timestamps do not transfer by assumption.

## Scene schema

Copy this **unallocated template** only after source admission. Replace all `TEMPLATE` values; it does not reserve an ID.

```yaml
scene_id: TEMPLATE_UNALLOCATED
episode: TEMPLATE_E01_TO_E04
source_id: TEMPLATE_MANIFEST_ID
edition: TEMPLATE_EXACT_VERSION
interval: {start: TEMPLATE, end: TEMPLATE, precision: TEMPLATE}
dramatic_time: TEMPLATE_PRESENT_MEMORY_UNCERTAIN
setting_and_subjects: TEMPLATE_OBSERVED_ONLY
entry_situation: TEMPLATE
consequential_actions_and_turn: TEMPLATE
exit_situation: TEMPLATE
observation_ids: []
omissions_or_uncertain_boundaries: []
```

## Observation schema

Observation text describes recoverable image, sound or wording. Put explanations of motive and formal significance in a linked claim, even when the observer finds them convincing.

```yaml
observation_id: TEMPLATE_UNALLOCATED
scene_id: TEMPLATE
installment: road-to-the-top
episode: TEMPLATE
source_id: TEMPLATE_MANIFEST_ID
source_sha256: TEMPLATE
edition_and_language: TEMPLATE
source_interval: {start: TEMPLATE, end: TEMPLATE, precision: TEMPLATE}
derivative_refs: []
clock_mapping_ref: TEMPLATE
speaker_or_subjects: []
scene_description: TEMPLATE_CONCISE_CONTEXT
observation_kind: TEMPLATE_VISUAL_AUDIO_DIALOGUE_MEASUREMENT
inspection_lane: TEMPLATE_TEXT_STILL_IMAGE_BUNDLE_MEDIATED_CONTINUOUS_AV
capability_receipt_ref: TEMPLATE
observed_visual_details: TEMPLATE_OR_NOT_INSPECTED
observed_audio_details: TEMPLATE_OR_NOT_INSPECTED
brief_japanese_anchor: TEMPLATE_OR_NOT_NEEDED
translation: TEMPLATE_OR_NOT_NEEDED
text_witness_and_cue: TEMPLATE_OR_UNAVAILABLE
translation_issue: TEMPLATE_OR_NONE_IDENTIFIED
epistemic_state: PRIMARY_SOURCE_OBSERVATION
evidentiary_strength: TEMPLATE_HIGH_MODERATE_LOW_UNASSESSABLE
limits_and_missing_channels: []
related_character_state_ids: []
related_relationship_state_ids: []
related_claim_ids: []
independent_contribution_ref: TEMPLATE
critical_review_and_reconciliation_ref: TEMPLATE
record_state: DRAFT
```

`derivative_refs` contain portable artifact IDs, hashes, cue/frame/shot identifiers and retrieval references; raw artifacts remain outside Git. Keep quotations brief and limited to what the claim requires. If Japanese wording is unavailable, record `UNAVAILABLE`, leave wording-dependent claims open, and identify whether an English line is a subtitle translation, working translation or unverified gloss. Neither ASR nor an English subtitle is an authenticated Japanese text witness by default.

## Evidence categories and acceptance

| Epistemic state | Appropriate home and threshold |
|---|---|
| `VERIFIED_PRODUCTION_FACT` | Production-metadata record with authoritative reference; not an anime scene observation |
| `PRIMARY_SOURCE_OBSERVATION` | This ledger, directly recoverable in the identified source and inspected channel |
| `GROUNDED_INTERPRETATION` | Claim ledger, supported by observation IDs and material counterevidence |
| `TENTATIVE_HYPOTHESIS` | Research/claim register, with an explicit disconfirmation test |
| `EXTERNAL_CONTEXTUAL_FACT` | Context record, with an external source and no implied anime authority |
| `UNVERIFIED_UNAVAILABLE` | Explicit evidence gap; no positive finding |

`HIGH` means the relevant channel and locator clearly support the bounded observation; `MODERATE` marks a specific ambiguity; `LOW` marks a weak witness or incomplete route; `UNASSESSABLE` marks unavailable evidence. These are evidence-strength judgments, not a vote count. Multiple agents repeating the same claim create no independent corroboration.

Record states are `DRAFT`, `ACCEPTED`, `DISPUTED`, `CORRECTED` and `WITHDRAWN`. An integrator accepts a record only after checking its source identity, channel capability, timestamp, independence and critical-review disposition. Preserve disagreements and their evidence; an independent reviewer does not become independent by paraphrasing the principal's draft. An observation may remain accepted while a linked interpretation is rejected.

Sampled stills support visible endpoints, not the path between them. Shot measurements can support duration, but a single still cannot establish motion, editing rhythm, delivery or image–music synchronization. Audio presence is not proof that a model listened. Unsupported channel claims stay `DRAFT`/`DISPUTED` or are narrowed to the channel actually inspected.

## Record and correction procedure

Append new scene and observation records below after a real authorized reading. Each addition names its author role, source frontier and episode transaction record. Do not prefill outcomes from synopses, trailers, historical race results, later episodes or another installment.

Keep the original wording and locator recoverable when correcting a record. Add a dated correction with reason, prior/new values and affected claim/state IDs; use a successor observation ID for a materially different observation and link both. Retain withdrawn IDs as tombstones, never recycle them. A source replacement needs a new source binding and a checked crosswalk, not an overwritten hash. Frozen episode records are corrected through attributable errata under the governing method.

## Accepted records

None. Next permitted work is source-readiness verification; source-grounded records begin only under the canonical entrypoint's applicable gates.
