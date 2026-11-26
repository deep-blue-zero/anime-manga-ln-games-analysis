---
title: "Psycho-Pass — Current state and corpus map"
artifact_id: PP_CURRENT_STATE_AND_CORPUS_MAP
artifact_type: current_state_and_corpus_map
series: psycho-pass
version: "1.12"
status: canonical
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
do_not_use_as_literary_evidence: true
authority_generation: PP-INITIAL
source_boundary: "Run PP-S01NE-RUN-20261123-E01-E11 complete: PP-S01NE-E01–E11 admitted and accepted (11/11 = 100%)"
canonical_home: series/psycho-pass/CURRENT_STATE_AND_CORPUS_MAP.md
created: 2026-11-18
last_updated: 2026-11-26
recommended_reasoning_class: BOUNDED_STANDARD
project_initialization:
  status: canonical
  architecture_lifecycle: INITIAL
  governing_method: framework/PP_ANALYTICAL_METHOD.md
  synthesis_architecture: framework/PP_SYNTHESIS_ARCHITECTURE.md
  method_status: canonical
  architecture_status: canonical
  source_reconnaissance_complete: true
  required_day_one_infrastructure_initialized: true
  required_ledgers_initialized: true
  required_day_one_infrastructure:
    - source-inventory/PP_SOURCE_REGISTER.md
    - installments/s01-new-edit/PP_S01NE_EVIDENCE_AND_STATE_LEDGER.md
    - installments/s01-new-edit/PP_S01NE_CLAIM_AND_DISCLOSURE_LEDGER.md
    - franchise/ledgers/PP_FRANCHISE_STATE_LEDGER.md
    - franchise/ledgers/PP_CONTINUITY_AND_CLAIM_LEDGER.md
    - integration/PP_RECONCILIATION_PROTOCOL.md
  sequential_analysis_lock: OPEN
  next_permitted_operation: NONE
sequential_execution:
  run_id: PP-S01NE-RUN-20261123-E01-E11
  mode: continuous_sequential
  unit_type: episode
  authorized_start: PP-S01NE-E01
  terminal_boundary: PP-S01NE-E11
  committed_high_water_mark: PP-S01NE-E11
  next_candidate_operation: NONE
  confirmation_between_units: false
  run_state: completed
source_admission: "PP-S01NE-E01–E11 Season 1 New Edit complete (11/11 admitted and accepted); no further narrative admission authorized"
run_authorization: PP-S01NE-RUN-20261123-E01-E11
execution_profile:
  role_configuration_status: VERIFIED_ACTIVE_MULTIAGENT_NATIVE
  method_family: ANIME_WITH_CONTINUOUS_AV_COMPANION
  project_reconciliation_profile: PP_AV_PRIMARY_CHARACTER_AND_FORM
  continuous_video: VERIFIED_1FPS_WITH_LOSSLESS_CLIPS_AND_1080P_STILLS
  direct_listening: VERIFIED_48KHZ_JAPANESE_AND_50MS_AM
  source_language_inspection: VERIFIED_JAPANESE_ASS_SRT_AND_AUDIO
  complete_episode_bundles: VERIFIED_AVAILABLE_E01_TO_E11
  source_filesystem_metadata: VERIFIED_BOUNDED_INVENTORY
---

# Psycho-Pass — Current state and corpus map

The canonical root and sole continuing analytical branch are `series/psycho-pass`. This is one franchise project with installment-local source work and a distinct franchise reconciliation layer. The first intended installment is **Season 1 New Edit / Extended Edition, eleven episodes**. The original twenty-two-episode version is a separate possible comparison witness of the same underlying continuity, with its own identifiers, disclosure order and clocks.

**SEQUENTIAL_ANALYSIS_LOCK = OPEN (Run `PP-S01NE-RUN-20261123-E01-E11` COMPLETED — `next_permitted_operation = NONE`, `next_candidate_operation = NONE`).** Owner authorization (`PP-S01NE-RUN-20261123-E01-E11`, 2026-11-23; reaffirmed 2026-11-24 post-recovery) authorized one `continuous_sequential` run across Season 1 New Edit (`PP-S01NE-E01` through `PP-S01NE-E11`). **All eleven episodes (`PP-S01NE-E01` through `PP-S01NE-E11`, `11/11 = 100%`) have been content-authenticated, independently analyzed, reconciled, validated, and accepted on branch `series/psycho-pass`** (Tranche 1 `E03–E04`, Tranche 2 `E06–E08`, and Tranche 3 `E09–E11` complete; **Final Season 1 Monograph Qualification Gate adjudicated cleanly in [`PP_FRANCHISE_STATE_LEDGER.md`](franchise/ledgers/PP_FRANCHISE_STATE_LEDGER.md): `9` individual `QUALIFIED_PENDING` portrait obligations + `1` separate institutional/vessel study candidate, `0` completed portraits** — counting qualification obligations separately from production without starting a portrait run). `committed_high_water_mark` stands at **`PP-S01NE-E11`** with `run_state: completed`, `next_permitted_operation: NONE`, and `next_candidate_operation: NONE`; publication to `main` remains governed by owner review of PR #717, and no later installment or menu witness has been admitted.

Metadata reconnaissance verified eleven numbered New Edit MKVs, one excluded menu, two BD-labelled ASS witnesses, ten TV-labelled SRT witnesses, eleven standalone lossless FLAC tracks, and eleven structurally validated episode bundles. All 24 archival source hashes remain unchanged. Full audiovisual playback, direct Japanese listening (including direct lossless `AO` Japanese certification of `E11`'s untagged `audio_language=null/und` stream), lossless stream-copy/WAV reinspection, native 1080p still inspection, and 50 ms `AM` calibration have been verified empirically across all eleven episodes **`PP-S01NE-E01` through `PP-S01NE-E11`** (enforcing bounded `≤ 28 MiB` single-clip and per-episode isolated subagent payload budgets from `E03` onward). Original supplier Blu-ray/disc provenance remains explicitly unauthenticated (content authentication establishes Season 1 New Edit E01–E11, not physical disc derivation).

## Accepted units (`PP-S01NE`)

| Unit | Status | Deep Reading | Transaction Checkpoint |
| --- | --- | --- | --- |
| `PP-S01NE-E01` | `ACCEPTED` (`14/14` QC PASS) | [`PP_S01NE_E01_DEEP_READING.md`](installments/s01-new-edit/readings/PP_S01NE_E01_DEEP_READING.md) | [`PP_S01NE_E01_CHECKPOINT.md`](installments/s01-new-edit/checkpoints/PP_S01NE_E01_CHECKPOINT.md) |
| `PP-S01NE-E02` | `ACCEPTED` (`14/14` QC PASS) | [`PP_S01NE_E02_DEEP_READING.md`](installments/s01-new-edit/readings/PP_S01NE_E02_DEEP_READING.md) | [`PP_S01NE_E02_CHECKPOINT.md`](installments/s01-new-edit/checkpoints/PP_S01NE_E02_CHECKPOINT.md) |
| `PP-S01NE-E03` | `ACCEPTED` (`14/14` QC PASS) | [`PP_S01NE_E03_DEEP_READING.md`](installments/s01-new-edit/readings/PP_S01NE_E03_DEEP_READING.md) | [`PP_S01NE_E03_CHECKPOINT.md`](installments/s01-new-edit/checkpoints/PP_S01NE_E03_CHECKPOINT.md) |
| `PP-S01NE-E04` | `ACCEPTED` (`14/14` QC PASS) | [`PP_S01NE_E04_DEEP_READING.md`](installments/s01-new-edit/readings/PP_S01NE_E04_DEEP_READING.md) | [`PP_S01NE_E04_CHECKPOINT.md`](installments/s01-new-edit/checkpoints/PP_S01NE_E04_CHECKPOINT.md) |
| `PP-S01NE-E05` | `ACCEPTED` (`14/14` QC PASS) | [`PP_S01NE_E05_DEEP_READING.md`](installments/s01-new-edit/readings/PP_S01NE_E05_DEEP_READING.md) | [`PP_S01NE_E05_CHECKPOINT.md`](installments/s01-new-edit/checkpoints/PP_S01NE_E05_CHECKPOINT.md) |
| `PP-S01NE-E06` | `ACCEPTED` (`14/14` QC PASS) | [`PP_S01NE_E06_DEEP_READING.md`](installments/s01-new-edit/readings/PP_S01NE_E06_DEEP_READING.md) | [`PP_S01NE_E06_CHECKPOINT.md`](installments/s01-new-edit/checkpoints/PP_S01NE_E06_CHECKPOINT.md) |
| `PP-S01NE-E07` | `ACCEPTED` (`14/14` QC PASS) | [`PP_S01NE_E07_DEEP_READING.md`](installments/s01-new-edit/readings/PP_S01NE_E07_DEEP_READING.md) | [`PP_S01NE_E07_CHECKPOINT.md`](installments/s01-new-edit/checkpoints/PP_S01NE_E07_CHECKPOINT.md) |
| `PP-S01NE-E08` | `ACCEPTED` (`14/14` QC PASS; Tranche 2 Close) | [`PP_S01NE_E08_DEEP_READING.md`](installments/s01-new-edit/readings/PP_S01NE_E08_DEEP_READING.md) | [`PP_S01NE_E08_CHECKPOINT.md`](installments/s01-new-edit/checkpoints/PP_S01NE_E08_CHECKPOINT.md) |
| `PP-S01NE-E09` | `ACCEPTED` (`14/14` QC PASS; Tranche 3 Open) | [`PP_S01NE_E09_DEEP_READING.md`](installments/s01-new-edit/readings/PP_S01NE_E09_DEEP_READING.md) | [`PP_S01NE_E09_CHECKPOINT.md`](installments/s01-new-edit/checkpoints/PP_S01NE_E09_CHECKPOINT.md) |
| `PP-S01NE-E10` | `ACCEPTED` (`14/14` QC PASS; Penultimate) | [`PP_S01NE_E10_DEEP_READING.md`](installments/s01-new-edit/readings/PP_S01NE_E10_DEEP_READING.md) | [`PP_S01NE_E10_CHECKPOINT.md`](installments/s01-new-edit/checkpoints/PP_S01NE_E10_CHECKPOINT.md) |
| `PP-S01NE-E11` | `ACCEPTED` (`14/14` QC PASS; Season Finale & Run Closure) | [`PP_S01NE_E11_DEEP_READING.md`](installments/s01-new-edit/readings/PP_S01NE_E11_DEEP_READING.md) | [`PP_S01NE_E11_CHECKPOINT.md`](installments/s01-new-edit/checkpoints/PP_S01NE_E11_CHECKPOINT.md) |

| Need | Canonical home |
| --- | --- |
| Governing source-facing practice and adopted AV-primary scope | [Analytical method](framework/PP_ANALYTICAL_METHOD.md) |
| Local/master authority, specialist synthesis and monographs | [Synthesis architecture](framework/PP_SYNTHESIS_ARCHITECTURE.md) |
| Exact available bytes, edition uncertainty, clocks and missing routes | [Source register](source-inventory/PP_SOURCE_REGISTER.md) |
| S1 New Edit observations, source locators and local state | [Local evidence and state ledger](installments/s01-new-edit/PP_S01NE_EVIDENCE_AND_STATE_LEDGER.md) |
| S1 New Edit materialized scene reconstructions (`222` scenes) | [Scene reconstruction ledger](installments/s01-new-edit/PP_S01NE_SCENE_RECONSTRUCTION_LEDGER.md) |
| S1 New Edit hypotheses, disclosure freezes and claim changes | [Local claim and disclosure ledger](installments/s01-new-edit/PP_S01NE_CLAIM_AND_DISCLOSURE_LEDGER.md) |
| S1 New Edit byte-exact original prospective freezes (`PRE-0001`–`0011`) | [Freeze provenance index](installments/s01-new-edit/freezes/FREEZE_PROVENANCE_INDEX.md) |
| Canonical errata and clarifications for frozen E01–E11 readings | [Reading errata and clarifications](installments/s01-new-edit/PP_S01NE_READING_ERRATA_AND_CLARIFICATIONS.md) |
| Reconciled character, directed relationship and institution state; portrait obligations | [Franchise state ledger](franchise/ledgers/PP_FRANCHISE_STATE_LEDGER.md) |
| Three chronologies, cross-installment claims and audiovisual recurrence | [Franchise continuity and claim ledger](franchise/ledgers/PP_CONTINUITY_AND_CLAIM_LEDGER.md) |
| Independent source review, AV calibration, incremental integration and handoff | [Reconciliation protocol](integration/PP_RECONCILIATION_PROTOCOL.md) |
| Housekeeping's project-local routing input | [Series descriptor](.repository/series-registry.json) |

## Completion gate summary & historical bootstrap note

- **Current Series Gate Status (through `PP-S01NE-E11`, `11/11 = 100%` on branch `series/psycho-pass`):**
  - *Sequential-source completion (`PP-S01NE`):* **REACHED** (`E01`–`E11` accepted; all 11 deep-reading artifacts preserved byte-sealed under `.repository/completed-run-publication.json`, accompanied by [`PP_S01NE_READING_ERRATA_AND_CLARIFICATIONS.md`](installments/s01-new-edit/PP_S01NE_READING_ERRATA_AND_CLARIFICATIONS.md) and byte-exact [`freezes/`](installments/s01-new-edit/freezes/FREEZE_PROVENANCE_INDEX.md)).
  - *Longitudinal reconciliation (`PP-S01NE`):* **REACHED** (local evidence/scene/claim ledgers and both franchise ledgers reconciled through `E11`, including PR #717 review corrections).
  - *Specialist-synthesis & monograph readiness:* **READY FOR AUTHORIZATION (`9` individual `QUALIFIED_PENDING` portrait obligations + `1` separate institutional/vessel candidate; `0` completed portraits — character layer explicitly incomplete until standalone portraits are separately authorized and reviewed)**.
  - *Full-series synthesis / Validation / Release to `main`:* **PENDING** (awaiting owner PR #717 release decision and any future authorized portrait/synthesis runs).
- **Historical Bootstrap Record (2026-11-18 — Superseded by `PP-S01NE-RUN-20261123-E01-E11`):** At initial repository bootstrap on `2026-11-18`, the franchise ledgers held zero accepted narrative records, runtime capabilities were unverified, TV subtitle clocks and E04/E11 source gaps were unresolved, and `SEQUENTIAL_ANALYSIS_LOCK` was `CLOSED` awaiting first-start prerequisites. Those bootstrap prerequisites were satisfied per episode during `2026-11-23`–`2026-11-24` under `PP-S01NE-RUN-20261123-E01-E11` (including full `E04` BD07/08 + `45/45` lossless `AO` audit and `E11` direct lossless `AO` Japanese spoken-language verification). Only `installments/s01-new-edit/` has a local reading home; all other catalogue families (`PP-S01OB`, Season 2, The Movie, *Sinners of the System*, Season 3, *First Inspector*, *Providence*) remain unadmitted inventory entries. Any new sequential run, portrait production run, or original-broadcast comparison requires fresh owner authorization under the [initiation](../../governance/source-policies/MANGA_ANIME_PROJECT_INITIATION_AND_ARCHITECTURE_POLICY.md) and [continuation](../../governance/source-policies/MANGA_ANIME_SEQUENTIAL_EXECUTION_SCOPE_AND_CONTINUATION_POLICY.md) policies.
