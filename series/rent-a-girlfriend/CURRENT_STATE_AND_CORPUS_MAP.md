---
title: "Rent-a-Girlfriend - Current State and Corpus Map"
artifact_id: RAG_CURRENT_STATE_AND_CORPUS_MAP
artifact_type: corpus_map
series: Rent-a-Girlfriend
generation: V1
version: "1.65"
status: canonical
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
created: "2026-09-19"
source_boundary: "Japanese manga EPUB inventory V001-V047; V001-V040 inspected and closed; V041+ inventory only."
---

# Rent-a-Girlfriend — current state and corpus map

This is the canonical first-read surface for the Git analytical corpus. Primary manga files and extraction products remain outside Git in the owner-authorized evidence and working planes.

## Project initialization

```yaml
project_initialization:
  status: canonical
  architecture_lifecycle: INITIAL
  analytical_phase: V040_CHECKPOINT_AND_AUDITS_COMPLETE
  source_reconnaissance_complete: true
  governing_method: "00 Frameworks and Methods/RAG_ANALYTICAL_METHOD.md"
  method_status: canonical
  synthesis_architecture: "00 Frameworks and Methods/RAG_SERIES_ARCHITECTURE.md"
  architecture_status: canonical
  reconstruction_specification: "00 Frameworks and Methods/RAG_CHARACTER_RECONSTRUCTION_SPEC.md"
  reconstruction_specification_status: canonical
  required_day_one_infrastructure_initialized: true
  required_day_one_infrastructure:
    - "03 Ledgers/RAG_CHRONOLOGY_LEDGER.md"
    - "03 Ledgers/RAG_RELATIONSHIP_STATE_LEDGER.md"
    - "03 Ledgers/RAG_INFORMATION_AND_DECEPTION_LEDGER.md"
    - "03 Ledgers/RAG_AGENCY_AND_INITIATIVE_LEDGER.md"
    - "03 Ledgers/RAG_TRANSACTION_AND_INTIMACY_LEDGER.md"
    - "03 Ledgers/RAG_PROGRESS_AND_REGRESSION_LEDGER.md"
    - "03 Ledgers/RAG_REPETITION_AND_VISUAL_FORM_LEDGER.md"
    - "03 Ledgers/RAG_CLAIMS_PREDICTIONS_AND_REVISIONS_LEDGER.md"
    - "03 Ledgers/RAG_CAST_AND_RECONSTRUCTION_READINESS.md"
  sequential_analysis_lock: OPEN
```

The V031-V040 sequential run, V040 checkpoint, local reconstruction audit and character-promotion audit are complete. All 204 ordered spine images in each of V031-V040 were directly inspected; readings, longitudinal ledgers and affected character homes are synchronized. V040 predictions were frozen at the V039 boundary and adjudicated after V040 inspection. V041+ remain inventory only.

## Active sequential authorization

```yaml
sequential_execution:
  mode: continuous_sequential
  unit_type: volume
  authorized_start: V001
  terminal_boundary: V040
  committed_high_water_mark: V040
  next_candidate_operation: AWAIT_SEPARATE_V041_AUTHORIZATION
  confirmation_between_units: false
  run_state: V031_to_V040_complete
```

V001-V040 were admitted and inspected in order. The requested ten-volume block and its checkpoint and audits are closed. No V041 narrative has been admitted.

## Source boundary

- Available inventory: 47 Japanese collected-volume EPUB witnesses, numbered V001-V047 without gaps.
- Active admitted boundary: V001-V040; all inspected and closed in order.
- Primary continuity: main manga.
- Excluded unless separately admitted: anime, spin-offs, alternate translations, interviews, reception, fan material, and future releases.
- Exact hashes, package metadata, page-spine counts, anomaly notes, and inspection state live in [RAG_SOURCE_AND_SCOPE_MAP.md](00%20Frameworks%20and%20Methods/RAG_SOURCE_AND_SCOPE_MAP.md).

## Governing read order

1. This file.
2. [RAG_ANALYTICAL_METHOD.md](00%20Frameworks%20and%20Methods/RAG_ANALYTICAL_METHOD.md).
3. [RAG_SERIES_ARCHITECTURE.md](00%20Frameworks%20and%20Methods/RAG_SERIES_ARCHITECTURE.md).
4. [RAG_CHARACTER_RECONSTRUCTION_SPEC.md](00%20Frameworks%20and%20Methods/RAG_CHARACTER_RECONSTRUCTION_SPEC.md).
5. [RAG_SOURCE_AND_SCOPE_MAP.md](00%20Frameworks%20and%20Methods/RAG_SOURCE_AND_SCOPE_MAP.md).
6. The latest closed volume, affected ledgers, and active character models needed for the next transaction.

## Current artifact state

| Responsibility | State |
|---|---|
| Foundation method, architecture, reconstruction specification | Canonical and adopted |
| Source map and next inspection route | V001-V040 inspected and closed; V041+ inventory only |
| Longitudinal ledgers | Synchronized through V040; predictions through V040 adjudicated |
| Character evidence ledgers | Thirteen homes are routed; Kazuya, Chizuru, Ruka, and Mini updated at V040, other unaffected homes retain their last material boundary |
| Reconstruction models | Kazuya and Chizuru `OPERATIONAL_CANDIDATE`; Ruka, Mami, Mini, and Sumi `PARTIAL_MODEL`; all other cast rows remain `UNMODELED` |
| Sequential deep readings | V001-V040 closed |
| Latest checkpoint | `02 Block Syntheses/RAG_CP_V040.md` complete for V031-V040, cumulative through V040 |
| Reconstruction audit | `07 Audits and Handoffs/RAG_RECONSTRUCTION_AUDIT_V040.md` complete for six models at the frozen V040 closing commit |
| Character-home promotion audit | `07 Audits and Handoffs/RAG_CHARACTER_ANALYSIS_PROMOTION_AUDIT_V040.md` complete for fourteen rows; thirteen evidence homes, six models, no new promotion or monograph |
| Repository publication | Stable branch `series/rent-a-girlfriend`; V030 block previously published; V031-V040 block committed locally |

## Execution profile

```yaml
execution_profile:
  product_surface: Codex desktop
  tool_runtime_location: owner-controlled local runtime
  observation_date: "2026-09-27"
  capability_scope: "Japanese image-based EPUB manga; V001-V040 direct page inspection"
  source_transport: owner-authorized local evidence path
  filesystem_read: VERIFIED
  filesystem_write: VERIFIED
  image_inspection: VERIFIED
  audio_content_inspection: NOT_APPLICABLE
  continuous_av_inspection: NOT_APPLICABLE
  git_write: VERIFIED
  inspection_method: "EPUB structural parsing plus direct original-resolution page inspection"
```

## Next operation

The V040 analytical block is complete. Any V041 narrative inspection requires a separate authorized run and a new entering freeze.

## Current analytical routes

- Latest closed reading: [RAG_V040_DEEP_READING.md](01%20Sequential%20Readings/Volumes%20031-040/RAG_V040_DEEP_READING.md)
- Current claims and adjudicated predictions through V040: [RAG_CLAIMS_PREDICTIONS_AND_REVISIONS_LEDGER.md](03%20Ledgers/RAG_CLAIMS_PREDICTIONS_AND_REVISIONS_LEDGER.md)
- Latest checkpoint: [RAG_CP_V040.md](02%20Block%20Syntheses/RAG_CP_V040.md)
- V040 local reconstruction audit: [RAG_RECONSTRUCTION_AUDIT_V040.md](07%20Audits%20and%20Handoffs/RAG_RECONSTRUCTION_AUDIT_V040.md)
- V040 character-analysis promotion audit: [RAG_CHARACTER_ANALYSIS_PROMOTION_AUDIT_V040.md](07%20Audits%20and%20Handoffs/RAG_CHARACTER_ANALYSIS_PROMOTION_AUDIT_V040.md)
- Current cast, artifact, and readiness router: [RAG_CAST_AND_RECONSTRUCTION_READINESS.md](03%20Ledgers/RAG_CAST_AND_RECONSTRUCTION_READINESS.md)
- Kazuya evidence/model: [evidence ledger](04%20Character%20Analysis/Kazuya%20Kinoshita/RAG_KAZUYA_EVIDENCE_LEDGER.md), [reconstruction model](04%20Character%20Analysis/Kazuya%20Kinoshita/RAG_KAZUYA_RECONSTRUCTION_MODEL.md)
- Chizuru evidence/model: [evidence ledger](04%20Character%20Analysis/Chizuru%20Ichinose/RAG_CHIZURU_EVIDENCE_LEDGER.md), [reconstruction model](04%20Character%20Analysis/Chizuru%20Ichinose/RAG_CHIZURU_RECONSTRUCTION_MODEL.md)
- Ruka evidence/model: [evidence ledger](04%20Character%20Analysis/Ruka%20Sarashina/RAG_RUKA_EVIDENCE_LEDGER.md), [reconstruction model](04%20Character%20Analysis/Ruka%20Sarashina/RAG_RUKA_RECONSTRUCTION_MODEL.md)
- Partial models initially promoted at V020: [Mami](04%20Character%20Analysis/Mami%20Nanami/RAG_MAMI_RECONSTRUCTION_MODEL.md), [Mini](04%20Character%20Analysis/Mini%20Yaemori/RAG_MINI_RECONSTRUCTION_MODEL.md), and [Sumi](04%20Character%20Analysis/Sumi%20Sakurasawa/RAG_SUMI_RECONSTRUCTION_MODEL.md)
- Evidence-only homes: [Nagomi](04%20Character%20Analysis/Nagomi%20Kinoshita/RAG_NAGOMI_EVIDENCE_LEDGER.md), [Sayuri](04%20Character%20Analysis/Sayuri%20Ichinose/RAG_SAYURI_EVIDENCE_LEDGER.md), [Katsuhito](04%20Character%20Analysis/Katsuhito%20Ichinose/RAG_KATSUHITO_EVIDENCE_LEDGER.md), [Harumi](04%20Character%20Analysis/Harumi%20Kinoshita/RAG_HARUMI_EVIDENCE_LEDGER.md), [Kibe](04%20Character%20Analysis/Kibe/RAG_KIBE_EVIDENCE_LEDGER.md), [Kuribayashi](04%20Character%20Analysis/Kuribayashi/RAG_KURIBAYASHI_EVIDENCE_LEDGER.md), and [Umi](04%20Character%20Analysis/Umi/RAG_UMI_EVIDENCE_LEDGER.md)
- The V031-V040 sequence, checkpoint and local audits are closed; V041+ remain outside this run and are inventory only.
