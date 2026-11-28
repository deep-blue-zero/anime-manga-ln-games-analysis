---
title: "The Witch from Mercury — Evidence locator index"
artifact_id: GWFM_EVIDENCE_LOCATOR_INDEX
artifact_type: evidence_locator_index
series: gundam-witch-from-mercury
version: "1.0"
status: canonical
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
do_not_use_as_literary_evidence: true
authority_generation: GWFM-INITIAL
source_boundary: "NONE; bootstrap architecture and metadata reconnaissance only"
canonical_home: series/gundam-witch-from-mercury/ledgers/GWFM_EVIDENCE_LOCATOR_INDEX.md
created: 2026-11-27
last_updated: 2026-11-27
recommended_reasoning_class: BOUNDED_STANDARD
---

# The Witch from Mercury — Evidence locator index

This is the canonical join from analytical claims to retained evidence. The source register owns witness identity and admission; this index owns stable observation identity and retrieval. Other ledgers cite its IDs rather than reproducing media or long transcripts.

## Shared record discipline

The principal/integrator is the single mutable owner. Add records only from an accepted or explicitly provisional source transaction inside its authorized horizon. Every record binds a stable ID, unit and witness, source frontier, evidence IDs, evidence class, confidence, current claim references and review disposition. Use exact source names with stable subject keys once verified; preserve uncertain attribution rather than guessing.

Append event/revision history. Update a clearly identified current-state projection only from that history; preserve earlier boundaries and frozen checkpoints. Never overwrite an old belief with later knowledge. One locator ID may support several dimensions without duplicating raw source material.

At bootstrap there are **zero narrative records**. Header definitions below are contracts, not synthetic examples or findings. This file is current authority for its schema only; no narrative claim is eligible as evidence.

## Observation record

| Field | Meaning |
| --- | --- |
| evidence_id | `GWFM-EV-P00-001` or `GWFM-EV-E##-NNN` pattern; allocate only for an actual observation |
| unit / scene_id / witness_id | Exact admitted logical unit, local causal scene and locked witness |
| source_object_ref | Opaque retained-source identity, independently resolvable through the governed evidence record |
| start / end / clock_ref | Calibrated interval and clock mapping; unknown values stay unknown |
| cue_ids / frame_ids / audio_ref | Actually verified derivative links; absent layers are explicit |
| inspection_lane / inspection_state | TEXT, STILL_IMAGE, BUNDLE_MEDIATED or CONTINUOUS_AV; inspected/partial/unavailable as actually established |
| observation | Bounded description of what was inspected, with subject and attribution |
| evidence_class / confidence | OBS, REPORT, INF, HYP, VALUE or OPEN and reasons; distinguish observation from inference |
| exposure_boundary | What was admitted and what the observer had actually seen |
| claim_refs / ledger_refs | Analytical consumers and current responsibility routes |
| review / limitations | Source check, sampling/text limits, unresolved attribution and reconciliation |

The example ID spelling above is a format, not an issued evidence record. IDs are never recycled after revision. If a derivative changes, keep the original mapping and append an explicit successor/crosswalk; do not point the same ID silently at new bytes.

## Retrieval and quality checks

A material claim must resolve to an observation, then a unit/witness and retrievable retained source. A web synopsis is not an episode locator. Source paths and media stay outside public Git; safe locators must remain enough for an authorized reader to recover them.

At every unit closeout, test representative high-impact locators and every contested locator; check cue/frame/audio clock consistency and that all named evidence IDs exist. For source-wide coverage, retain actual inspection intervals and gaps in the transaction receipt. A few valid locators do not prove complete coverage.

## Current records

None. No source locator has been minted or verified.
