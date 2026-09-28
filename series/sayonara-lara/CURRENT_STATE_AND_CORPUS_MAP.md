---
title: "Sayonara Lara: Current State and Corpus Map"
artifact_id: SYL_CURRENT_STATE
artifact_type: corpus_map
series: Sayonara Lara
generation: V1_JP_AUDITED
version: "1.13"
status: canonical
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
do_not_use_as_literary_evidence: true
created: "2026-09-20"
source_boundary: "Japanese-language TV anime E01-E12 closed at Japanese-caption and complete static-visual scope; E04/E08/E12 checkpoints complete"
canonical_home: series/sayonara-lara/CURRENT_STATE_AND_CORPUS_MAP.md
project_initialization:
  status: canonical
  architecture_lifecycle: EVOLVING
  governing_method: 00_Method/SYL_ANALYTICAL_METHOD.md
  synthesis_architecture: 00_Method/SYL_SYNTHESIS_ARCHITECTURE.md
  method_status: canonical
  architecture_status: canonical
  source_reconnaissance_complete: true
  required_day_one_infrastructure_initialized: true
  required_day_one_infrastructure:
    - 01_Source_Control/SYL_SOURCE_REGISTER.md
    - 01_Source_Control/SYL_EXECUTION_AND_INSPECTION_RECORD.md
    - 01_Source_Control/SYL_EXTERNAL_SOURCE_REGISTER.md
    - 03_Ledgers/SYL_CLAIMS_AND_REVISIONS.md
    - 03_Ledgers/SYL_CHARACTER_STATE_AND_READINESS.md
    - 03_Ledgers/SYL_RELATIONSHIP_TRAJECTORIES.md
    - 03_Ledgers/SYL_WORLD_RULES_AND_CAUSALITY.md
    - 03_Ledgers/SYL_MOTIFS_COMEDY_AND_FORM.md
    - 03_Ledgers/SYL_LANGUAGE_AND_PERFORMANCE.md
    - 08_Validation/SYL_BLOCKERS_AND_EVIDENCE_DEBTS.md
  sequential_analysis_lock: OPEN
---

# Sayonara Lara: current state and corpus map

This is the single canonical first-read surface for the project. Primary media, screenshots, subtitles, audio, extraction metadata, and transport archives remain in the owner-authorized evidence/working plane outside Git.

## Operational state

- Canonical root: `series/sayonara-lara/`
- Continuing branch: `series/sayonara-lara`
- `SEQUENTIAL_ANALYSIS_LOCK = OPEN` for active analysis/revision; authorized E01-E12 sequential transactions are complete for declared text/static scope
- Planned and source-locked narrative boundary: E01-E12
- Verified narrative transaction boundary: E12
- Audiovisual closure: E01-E12 text/static transactions complete; no episode certified for auditory or continuous-video coverage
- Knowledge mode: source-bounded chronological reread with disclosed prior exposure to E01-E04 discussion and the ending
- Current operation: semantic and repository acceptance of the completed bounded literary synthesis
- Next sequential candidate: none within authorized E01-E12 corpus
- Publication state: local synthesis authored; validation, routing synchronization and branch push pending

## Authorized sequential execution

```yaml
sequential_execution:
  mode: continuous_sequential
  unit_type: episode
  authorized_start: E01
  terminal_boundary: E12
  committed_high_water_mark: E12
  next_candidate_operation: final_audit_and_routing
  confirmation_between_units: false
  run_state: synthesis_authored
```

Each episode closed with its deep reading, applicable ledger changes, evidence debts, knowledge freeze, current-state update, checks, and commit before the next opened. E04/E08 contradiction checkpoints and E12 sequential closeout are complete for the declared scope. The bounded literary synthesis now awaits final semantic and repository acceptance.

## Source and capability boundary

All twelve owner-supplied extracted episode directories satisfy the repository's semantic bundle contract for the declared static/text/audio-access workflow: each includes source identity metadata, an aligned Japanese caption derivative, paired English aid, timestamped clean frames, manifests, dialogue and scene indexes, contact sheets, extraction QA, and complete stereo FLAC audio. The twelve transport ZIPs and key derivatives have SHA-256 locks in [the source register](01_Source_Control/SYL_SOURCE_REGISTER.md).

This runtime can read text, inspect original-resolution still images, decode/probe audio, write files, and perform Git operations. It does not have a verified route that supplies local FLAC samples to the analytical model for auditory interpretation, and the authorized input does not include continuous video. Narrative/text/static-image transactions may proceed with those scope limits. Sound-dependent and motion-dependent conclusions remain explicitly pending or are narrowed to inspected channels.

## Governing read order

1. This entrypoint.
2. [Analytical method](00_Method/SYL_ANALYTICAL_METHOD.md).
3. [Synthesis architecture](00_Method/SYL_SYNTHESIS_ARCHITECTURE.md).
4. [Audio and AV protocol](00_Method/SYL_AUDIO_AND_AV_PROTOCOL.md).
5. [Source register](01_Source_Control/SYL_SOURCE_REGISTER.md) and [execution record](01_Source_Control/SYL_EXECUTION_AND_INSPECTION_RECORD.md).
6. The latest closed episode/checkpoint, relevant ledgers, and [blockers/debts](08_Validation/SYL_BLOCKERS_AND_EVIDENCE_DEBTS.md).
7. [Legacy hypotheses](90_Legacy_and_Superseded/SYL_LEGACY_AND_HYPOTHESIS_REGISTER.md) only after the source-based episode/checkpoint result is recorded.

## Adopted architecture amendment

The owner requested a dedicated Rowan monograph because the king represents a major ideological axis. [His substantive monograph](04_Characters/SYL_ROWAN_MONOGRAPH.md) tests paternal sacrifice, dynastic need and sovereign coercion against each other.

## Current artifact state

| Responsibility | State |
|---|---|
| Method, synthesis architecture, AV protocol, design sources | Canonical and adopted |
| Source register and execution record | E01-E12 text/static inspection recorded |
| Six longitudinal ledgers | Synchronized through E12 |
| Legacy register | Historical/legacy and non-evidentiary |
| Sequential readings | E01-E12 complete for declared Japanese-text/static-visual scope; [E04](02_Episode_Readings/SYL_E04_CHECKPOINT.md), [E08](02_Episode_Readings/SYL_E08_CHECKPOINT.md) and [E12 closeout](02_Episode_Readings/SYL_E12_SEQUENTIAL_CLOSEOUT.md) passed |
| Character monographs | [Lara](04_Characters/SYL_LARA_MONOGRAPH.md), [Mari](04_Characters/SYL_MARI_MONOGRAPH.md), [Grace](04_Characters/SYL_GRACE_MONOGRAPH.md), [Rowan](04_Characters/SYL_ROWAN_MONOGRAPH.md), [Lisa](04_Characters/SYL_LISA_MONOGRAPH.md) and [ensemble](04_Characters/SYL_SUPPORTING_ENSEMBLE.md) authored for bounded literary lane |
| Relationship and specialists | [Lara/Mari](05_Relationships/SYL_LARA_MARI_RELATIONSHIP.md); [alienation](06_Specialist_Studies/SYL_ALIENATION_EMBODIMENT_AND_SELF_AUTHORSHIP.md), [love](06_Specialist_Studies/SYL_LOVE_FAIRYTALE_AND_RELATIONSHIP_CLASSIFICATION.md), [comedy/form](06_Specialist_Studies/SYL_COMEDY_VOICE_AND_AUDIOVISUAL_FORM.md), [family/law](06_Specialist_Studies/SYL_FAMILY_LAW_LIGHT_AND_CAUSALITY.md), [ending](06_Specialist_Studies/SYL_ENDING_AND_DRAMATIC_CLOSURE.md), [creator/reception](06_Specialist_Studies/SYL_CREATOR_CONTEXT_AND_RECEPTION.md) authored with channel limits |
| Series convergence and retrieval | [Full synthesis](07_Series_Synthesis/SYL_FULL_SERIES_SYNTHESIS.md), [comparative guide](07_Series_Synthesis/SYL_COMPARATIVE_ANALYSIS_GUIDE.md), [final claim/coverage audit](08_Validation/SYL_FINAL_CLAIM_AND_COVERAGE_AUDIT.md) authored; repository gate pending |

## Active blockers and debts

- `SYL-D0001`: no verified direct auditory-interpretation route in this runtime; affects performance, music, vocal, and sound-image claims.
- `SYL-D0002`: continuous video is outside the supplied input boundary; motion, microperformance, editing-rhythm, and AV-synchrony claims may require targeted later escalation.
- `SYL-D0003`: the supplied bundle contains the aligned Japanese caption derivative and provenance metadata but not the untouched ABEMA caption witness; disputed exact-wording claims require recovery of that witness.

These debts do not authorize invented observations and do not block text/static literary synthesis where supplied evidence is adequate. They do block unqualified final claims in their affected channels. E01-E12 assign claim-linked intervals and actions to `SYL-D0001`-`SYL-D0003` in their readings and the debt register. `SYL-D0004` is narrowly satisfied for four directly retrieved pages, with wider reception comparison unperformed.

## Latest closed transaction

[Episode 12: The World I Want to Inhabit](02_Episode_Readings/SYL_EP12_DEEP_READING.md) has Lara reject Rowan's loved-one stabbing and her own erasure. Mari approaches without claiming magical sight, is reported to have died and revived, and Lara avows continuing life in Mari's world while rejecting the prescribed “true love” test. Six months later the family recovers gradually, the king's hatred remains a future problem, and Lara leaves for independent life on painful legs while Mari names loneliness. [The closeout](02_Episode_Readings/SYL_E12_SEQUENTIAL_CLOSEOUT.md) separates this supported literary ending from unresolved mechanisms and channels.

## Next operation

Run semantic and link/authority validation, correct material errors, commit the synthesis transaction, synchronize the three global routing indexes under housekeeping ownership, run final repository checks, then push the continuing branch. This is a bounded literary acceptance, not a frozen all-channel AV release.
