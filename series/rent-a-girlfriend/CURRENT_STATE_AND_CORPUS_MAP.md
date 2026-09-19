---
title: "Rent-a-Girlfriend - Current State and Corpus Map"
artifact_id: RAG_CURRENT_STATE_AND_CORPUS_MAP
artifact_type: corpus_map
series: Rent-a-Girlfriend
generation: V1
version: "1.4"
status: canonical
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
created: "2026-09-19"
source_boundary: "Japanese manga EPUB inventory V001-V047; V001-V004 inspected and closed; active prospective analysis authorized through V010 with V005 next."
---

# Rent-a-Girlfriend — current state and corpus map

This is the canonical first-read surface for the Git analytical corpus. Primary manga files and extraction products remain outside Git in the owner-authorized evidence and working planes.

## Project initialization

```yaml
project_initialization:
  status: canonical
  architecture_lifecycle: INITIAL
  analytical_phase: READY_FOR_V005
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

The gate remains open because the stable root and identity were resolved against current Git authority; the Japanese V001-V047 inventory is continuous and hash-locked; V001-V004 received complete sequential visual inspection and atomic analytical closes; the three governing foundations remain current-eligible; and the cumulative ledgers and active character models are synchronized through V004.

## Active sequential authorization

```yaml
sequential_execution:
  mode: continuous_sequential
  unit_type: volume
  authorized_start: V001
  terminal_boundary: V010
  committed_high_water_mark: V004
  next_candidate_operation: V005
  confirmation_between_units: false
  run_state: active
```

V011 is inventory-visible but narratively inadmissible in this run. Each volume must close as an independent transaction before the next begins.

## Source boundary

- Available inventory: 47 Japanese collected-volume EPUB witnesses, numbered V001-V047 without gaps.
- Active admitted run: V001-V010, in order.
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
| Source map and next inspection route | V001-V004 closed; V005 is next |
| Longitudinal ledgers | Synchronized through V004 |
| Character evidence ledgers and models | Kazuya, Chizuru, and Ruka at project-local `PARTIAL_MODEL` through V004 |
| Sequential deep readings | V001-V004 closed |
| Latest checkpoint | None |
| Reconstruction audit | None |
| Repository publication | Stable branch `series/rent-a-girlfriend`; V004 transaction included in the current branch state |

## Execution profile

```yaml
execution_profile:
  product_surface: Codex desktop
  tool_runtime_location: owner-controlled local runtime
  observation_date: "2026-09-19"
  capability_scope: "Japanese image-based EPUB manga; V001-V004 metadata, spine mapping, and original-resolution page inspection"
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

Before inspecting V005 narrative pages, recover the V004 exiting freeze, current claims, frozen predictions `RAG-PRED-013` through `RAG-PRED-016`, and the Kazuya, Chizuru, and Ruka V004 models. Verify witness `RAG-JP-EPUB-V005`, create the V005 entering freeze, and close V005 as its own transaction before opening V006.

## Current analytical routes

- Latest closed reading: [RAG_V004_DEEP_READING.md](01%20Sequential%20Readings/Volumes%20001-010/RAG_V004_DEEP_READING.md)
- Current claims and V005 predictions: [RAG_CLAIMS_PREDICTIONS_AND_REVISIONS_LEDGER.md](03%20Ledgers/RAG_CLAIMS_PREDICTIONS_AND_REVISIONS_LEDGER.md)
- Kazuya evidence/model: [evidence ledger](04%20Character%20Analysis/Kazuya%20Kinoshita/RAG_KAZUYA_EVIDENCE_LEDGER.md), [reconstruction model](04%20Character%20Analysis/Kazuya%20Kinoshita/RAG_KAZUYA_RECONSTRUCTION_MODEL.md)
- Chizuru evidence/model: [evidence ledger](04%20Character%20Analysis/Chizuru%20Ichinose/RAG_CHIZURU_EVIDENCE_LEDGER.md), [reconstruction model](04%20Character%20Analysis/Chizuru%20Ichinose/RAG_CHIZURU_RECONSTRUCTION_MODEL.md)
- Ruka evidence/model: [evidence ledger](04%20Character%20Analysis/Ruka%20Sarashina/RAG_RUKA_EVIDENCE_LEDGER.md), [reconstruction model](04%20Character%20Analysis/Ruka%20Sarashina/RAG_RUKA_RECONSTRUCTION_MODEL.md)
- No block checkpoint or reconstruction audit is due until V010 closes.
