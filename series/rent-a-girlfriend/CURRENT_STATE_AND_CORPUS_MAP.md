---
title: "Rent-a-Girlfriend - Current State and Corpus Map"
artifact_id: RAG_CURRENT_STATE_AND_CORPUS_MAP
artifact_type: corpus_map
series: Rent-a-Girlfriend
generation: V1
version: "1.49"
status: canonical
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
created: "2026-09-19"
source_boundary: "Japanese manga EPUB inventory V001-V047; V001-V028 inspected and closed; V029 structurally verified and open under frozen predictions; V001-V020 checkpointed, locally audited, and character-home promotion audited; V021-V030 authorized in order."
---

# Rent-a-Girlfriend — current state and corpus map

This is the canonical first-read surface for the Git analytical corpus. Primary manga files and extraction products remain outside Git in the owner-authorized evidence and working planes.

## Project initialization

```yaml
project_initialization:
  status: canonical
  architecture_lifecycle: INITIAL
  analytical_phase: V029_ENTERING_FREEZE__INSPECTION_PENDING
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

The second block gate is closed. V001-V028 are inspected and closed, while the V020 checkpoint, local reconstruction audit, and character-home promotion audit remain the latest full recovery boundary. The owner has authorized V021-V030 as one continuous block. V029 is structurally verified and open under predictions frozen at the V028 close; no V029 or V031 narrative image has been inspected.

## Active sequential authorization

```yaml
sequential_execution:
  mode: continuous_sequential
  unit_type: volume
  authorized_start: V001
  terminal_boundary: V030
  committed_high_water_mark: V028
  next_candidate_operation: INSPECT_V029_SEQUENTIALLY
  confirmation_between_units: false
  run_state: active
```

V021-V030 are admitted in order for this run. V028 is closed and V029 is the active open unit. V031 is inventory-visible but narratively inadmissible.

## Source boundary

- Available inventory: 47 Japanese collected-volume EPUB witnesses, numbered V001-V047 without gaps.
- Active admitted run: V001-V030, with V001-V028 closed and V029 open under its entering freeze predictions.
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
| Source map and next inspection route | V001-V028 closed; V029 structurally verified and open |
| Longitudinal ledgers | Synchronized through V028; V029 predictions frozen |
| Character evidence ledgers | Thirteen homes are routed; Kazuya, Chizuru, Ruka, Mini, Kibe, Nagomi, Sumi, Sayuri, and Katsuhito updated or negative-evidence reviewed through V028; other unaffected homes retain their last material boundary |
| Reconstruction models | Kazuya and Chizuru `OPERATIONAL_CANDIDATE`; Ruka, Mami, Mini, and Sumi `PARTIAL_MODEL`; all other cast rows remain `UNMODELED` |
| Sequential deep readings | V001-V028 closed; V029 open under frozen predictions |
| Latest checkpoint | `02 Block Syntheses/RAG_CP_V020.md` complete |
| Reconstruction audit | `07 Audits and Handoffs/RAG_RECONSTRUCTION_AUDIT_V020.md` complete |
| Character-home promotion audit | `07 Audits and Handoffs/RAG_CHARACTER_ANALYSIS_PROMOTION_AUDIT_V020.md` complete; nine ledgers and three bounded models promoted without a monograph or architecture amendment |
| Repository publication | Stable branch `series/rent-a-girlfriend`; V029 opening is the current authored transaction |

## Execution profile

```yaml
execution_profile:
  product_surface: Codex desktop
  tool_runtime_location: owner-controlled local runtime
  observation_date: "2026-09-21"
  capability_scope: "Japanese image-based EPUB manga; V001-V028 original-resolution page inspection; V029 structural verification"
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

Inspect witness RAG-JP-EPUB-V029 completely under frozen predictions RAG-PRED-109 through RAG-PRED-112, then synchronize and close the atomic volume transaction. Do not inspect or admit V031 narrative evidence.

## Current analytical routes

- Latest closed reading: [RAG_V028_DEEP_READING.md](01%20Sequential%20Readings/Volumes%20021-030/RAG_V028_DEEP_READING.md)
- Active entering freeze: [RAG_V029_DEEP_READING.md](01%20Sequential%20Readings/Volumes%20021-030/RAG_V029_DEEP_READING.md), with no narrative image inspected at open.
- Current claims, adjudicated predictions through V028, and frozen V029 predictions: [RAG_CLAIMS_PREDICTIONS_AND_REVISIONS_LEDGER.md](03%20Ledgers/RAG_CLAIMS_PREDICTIONS_AND_REVISIONS_LEDGER.md)
- V020 checkpoint: [RAG_CP_V020.md](02%20Block%20Syntheses/RAG_CP_V020.md)
- V020 local reconstruction audit: [RAG_RECONSTRUCTION_AUDIT_V020.md](07%20Audits%20and%20Handoffs/RAG_RECONSTRUCTION_AUDIT_V020.md)
- V020 character-analysis promotion audit: [RAG_CHARACTER_ANALYSIS_PROMOTION_AUDIT_V020.md](07%20Audits%20and%20Handoffs/RAG_CHARACTER_ANALYSIS_PROMOTION_AUDIT_V020.md)
- Current cast, artifact, and readiness router: [RAG_CAST_AND_RECONSTRUCTION_READINESS.md](03%20Ledgers/RAG_CAST_AND_RECONSTRUCTION_READINESS.md)
- Kazuya evidence/model: [evidence ledger](04%20Character%20Analysis/Kazuya%20Kinoshita/RAG_KAZUYA_EVIDENCE_LEDGER.md), [reconstruction model](04%20Character%20Analysis/Kazuya%20Kinoshita/RAG_KAZUYA_RECONSTRUCTION_MODEL.md)
- Chizuru evidence/model: [evidence ledger](04%20Character%20Analysis/Chizuru%20Ichinose/RAG_CHIZURU_EVIDENCE_LEDGER.md), [reconstruction model](04%20Character%20Analysis/Chizuru%20Ichinose/RAG_CHIZURU_RECONSTRUCTION_MODEL.md)
- Ruka evidence/model: [evidence ledger](04%20Character%20Analysis/Ruka%20Sarashina/RAG_RUKA_EVIDENCE_LEDGER.md), [reconstruction model](04%20Character%20Analysis/Ruka%20Sarashina/RAG_RUKA_RECONSTRUCTION_MODEL.md)
- Partial models initially promoted at V020: [Mami](04%20Character%20Analysis/Mami%20Nanami/RAG_MAMI_RECONSTRUCTION_MODEL.md), [Mini](04%20Character%20Analysis/Mini%20Yaemori/RAG_MINI_RECONSTRUCTION_MODEL.md), and [Sumi](04%20Character%20Analysis/Sumi%20Sakurasawa/RAG_SUMI_RECONSTRUCTION_MODEL.md)
- Evidence-only homes: [Nagomi](04%20Character%20Analysis/Nagomi%20Kinoshita/RAG_NAGOMI_EVIDENCE_LEDGER.md), [Sayuri](04%20Character%20Analysis/Sayuri%20Ichinose/RAG_SAYURI_EVIDENCE_LEDGER.md), [Katsuhito](04%20Character%20Analysis/Katsuhito%20Ichinose/RAG_KATSUHITO_EVIDENCE_LEDGER.md), [Harumi](04%20Character%20Analysis/Harumi%20Kinoshita/RAG_HARUMI_EVIDENCE_LEDGER.md), [Kibe](04%20Character%20Analysis/Kibe/RAG_KIBE_EVIDENCE_LEDGER.md), [Kuribayashi](04%20Character%20Analysis/Kuribayashi/RAG_KURIBAYASHI_EVIDENCE_LEDGER.md), and [Umi](04%20Character%20Analysis/Umi/RAG_UMI_EVIDENCE_LEDGER.md)
- The second block checkpoint and reconstruction audit are closed at V020; V028 is closed and V029 is the active open unit in the V021-V030 block.
