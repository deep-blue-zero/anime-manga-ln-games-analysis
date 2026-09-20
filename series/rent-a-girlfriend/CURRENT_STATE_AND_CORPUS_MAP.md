---
title: "Rent-a-Girlfriend - Current State and Corpus Map"
artifact_id: RAG_CURRENT_STATE_AND_CORPUS_MAP
artifact_type: corpus_map
series: Rent-a-Girlfriend
generation: V1
version: "1.21"
status: canonical
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
created: "2026-09-19"
source_boundary: "Japanese manga EPUB inventory V001-V047; V001-V016 inspected and closed; V010 checkpoint and local audit remain the latest block boundary; V017 is next for entering freeze."
---

# Rent-a-Girlfriend — current state and corpus map

This is the canonical first-read surface for the Git analytical corpus. Primary manga files and extraction products remain outside Git in the owner-authorized evidence and working planes.

## Project initialization

```yaml
project_initialization:
  status: canonical
  architecture_lifecycle: INITIAL
  analytical_phase: V016_CLOSED__V017_ENTRY_NEXT
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

The first block gate is closed and the V010 checkpoint is the committed recovery boundary. V011-V016 are inspected and closed in the authorized V011-V020 block. Sequential analysis remains locked to unit order: V017 must receive its entering freeze before inspection, and no V021 narrative evidence is admitted.

## Active sequential authorization

```yaml
sequential_execution:
  mode: continuous_sequential
  unit_type: volume
  authorized_start: V001
  terminal_boundary: V020
  committed_high_water_mark: V016
  next_candidate_operation: V017_ENTRY_FREEZE
  confirmation_between_units: false
  run_state: active
```

V016 is closed; V017-V020 remain admitted in order for this run. V021 is inventory-visible but narratively inadmissible. Each volume must close as an independent transaction before the next begins.

## Source boundary

- Available inventory: 47 Japanese collected-volume EPUB witnesses, numbered V001-V047 without gaps.
- Active admitted run: V001-V020, with V001-V016 closed and V017-V020 remaining in order.
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
| Source map and next inspection route | V001-V016 closed; V017 entering freeze next |
| Longitudinal ledgers | Synchronized through V016 |
| Character evidence ledgers and models | Kazuya, Chizuru, and Ruka updated through V016; Mini role expanded in readiness |
| Sequential deep readings | V001-V016 closed; V017 not yet opened |
| Latest checkpoint | `02 Block Syntheses/RAG_CP_V010.md` complete |
| Reconstruction audit | `07 Audits and Handoffs/RAG_RECONSTRUCTION_AUDIT_V010.md` complete |
| Repository publication | Stable branch `series/rent-a-girlfriend`; V016 close prepared for publication |

## Execution profile

```yaml
execution_profile:
  product_surface: Codex desktop
  tool_runtime_location: owner-controlled local runtime
  observation_date: "2026-09-19"
  capability_scope: "Japanese image-based EPUB manga; V001-V016 original-resolution page inspection"
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

Prepare and publish the entering freeze for witness RAG-JP-EPUB-V017 under predictions RAG-PRED-061 through RAG-PRED-064 before inspecting any V017 narrative image.

## Current analytical routes

- Latest closed reading: [RAG_V016_DEEP_READING.md](01%20Sequential%20Readings/Volumes%20011-020/RAG_V016_DEEP_READING.md)
- Current claims, adjudicated V016 predictions, and frozen V017 predictions: [RAG_CLAIMS_PREDICTIONS_AND_REVISIONS_LEDGER.md](03%20Ledgers/RAG_CLAIMS_PREDICTIONS_AND_REVISIONS_LEDGER.md)
- V010 checkpoint: [RAG_CP_V010.md](02%20Block%20Syntheses/RAG_CP_V010.md)
- V010 local reconstruction audit: [RAG_RECONSTRUCTION_AUDIT_V010.md](07%20Audits%20and%20Handoffs/RAG_RECONSTRUCTION_AUDIT_V010.md)
- Kazuya evidence/model: [evidence ledger](04%20Character%20Analysis/Kazuya%20Kinoshita/RAG_KAZUYA_EVIDENCE_LEDGER.md), [reconstruction model](04%20Character%20Analysis/Kazuya%20Kinoshita/RAG_KAZUYA_RECONSTRUCTION_MODEL.md)
- Chizuru evidence/model: [evidence ledger](04%20Character%20Analysis/Chizuru%20Ichinose/RAG_CHIZURU_EVIDENCE_LEDGER.md), [reconstruction model](04%20Character%20Analysis/Chizuru%20Ichinose/RAG_CHIZURU_RECONSTRUCTION_MODEL.md)
- Ruka evidence/model: [evidence ledger](04%20Character%20Analysis/Ruka%20Sarashina/RAG_RUKA_EVIDENCE_LEDGER.md), [reconstruction model](04%20Character%20Analysis/Ruka%20Sarashina/RAG_RUKA_RECONSTRUCTION_MODEL.md)
- The first block checkpoint and reconstruction audit are closed; V017 entry is the next authorized unit operation.
