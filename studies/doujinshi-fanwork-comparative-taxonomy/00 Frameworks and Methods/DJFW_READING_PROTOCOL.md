---
project: DJFW
artifact_type: reading_protocol
scope: new_case_intake_and_analysis
generation: V1
status: active_provisional
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
---

# DJFW_READING_PROTOCOL.md

## New-work workflow

Every new work follows this pipeline:

1. **Register case** in `DJFW_PROJECT_CONTROL_SHEET` before filing source material.
2. **Add primary source** under the DJFW source root.
3. **Record source metadata** and source-boundary status.
4. **Extract reading copy** where needed: page images, contact sheet, OCR/translation notes, or non-graphic locator notes.
5. **Create analytical case folder** under `02 Case Readings`.
6. **Resolve baseline readiness** for characters and pairings.
7. **Perform case reading** using the four voice components and source-relation categories.
8. **Update Sheets ledgers** for case, source, baseline, voice, subjecthood, pressure, canon relation, audience orientation, value, and revision state.
9. **Update Markdown synthesis/current-state surfaces** only when project state materially changes.
10. **Close out** with a case update manifest.

## Case states

- `0_candidate`
- `1_registered`
- `2_source_added`
- `3_extracted`
- `4_baseline_resolved`
- `5_case_reading_started`
- `6_case_reading_complete`
- `7_ledgers_updated`
- `8_synthesis_reviewed`
- `9_closed`

Blocked states:

- `blocked_needs_reupload`
- `blocked_baseline_missing`
- `blocked_translation_unclear`
- `superseded_duplicate`
- `metadata_only`

## Case reading structure

Each case reading should include:

- identification and source boundary;
- R18/all-ages/unclear status;
- work type and audience orientation;
- baseline readiness;
- transformation pressure;
- surface voice;
- behavioral grammar;
- relational grammar;
- subjecthood/interiority;
- canon relationship;
- taxonomy placement;
- value assessment;
- confidence and gaps;
- ledger-update notes.

## Analysis guardrails

The reading should be rigorous but non-graphic. Explicit works are analyzed through narrative, symbolic, relational, and genre functions rather than graphic description.

## Anthology rule

An anthology may receive one parent source package but multiple analytical case IDs when individual contributions represent distinct character, pairing, genre, or authorial transformations.
