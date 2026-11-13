---
title: "Kamakura Police Station — current state and corpus map"
series: "Kamakura Police Station: The Case Files of Asumi Ogasawara / 鎌倉署・小笠原亜澄の事件簿"
series_id: kamakura-sho
artifact_id: CURRENT_STATE_AND_CORPUS_MAP
artifact_type: current_state_and_corpus_map
generation: KSOA-G1
version: "1.0"
created: "2026-11-12"
status: canonical
scope: "Sole current project entrypoint and operational state."
source_boundary: "Japanese publisher EPUBs V01–V07. Sequential readings closed through V03 within the authorized run."
canonical_home: series/kamakura-sho/CURRENT_STATE_AND_CORPUS_MAP.md
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
do_not_use_as_literary_evidence: true
project_initialization:
  status: canonical
  architecture_lifecycle: INITIAL
  bootstrap_generation: KSOA-G1
  governing_method: KSOA_ANALYTICAL_METHOD.md
  method_status: canonical
  synthesis_architecture: KSOA_SYNTHESIS_ARCHITECTURE.md
  architecture_status: canonical
  source_reconnaissance_complete: true
  source_reconnaissance_scope: "All seven Japanese EPUBs. Local and Drive bytes, import provenance, package structure and navigation."
  source_admission: V01_THROUGH_V03
  required_day_one_infrastructure_initialized: true
  required_day_one_infrastructure:
    - KSOA_SOURCE_AND_WITNESS_MAP.md
    - KSOA_CASE_EVIDENCE_LEDGER.md
    - KSOA_DISCLOSURE_AND_HYPOTHESIS_LEDGER.md
    - KSOA_CHARACTER_AND_RELATIONSHIP_LEDGER.md
    - KSOA_CLAIM_REVISION_LEDGER.md
  substantive_sequential_findings_at_bootstrap: false
  sequential_analysis_lock: open
  next_permitted_operation: V04
  run_authorization: "Owner instruction in the current Codex task to analyze all seven local Japanese novels and generate the artifacts required by the architecture."
  committed_high_water_mark: V03
  sequential_units_admitted: 3
  sequential_units_completed: 3
sequential_execution:
  mode: continuous_sequential
  unit_type: volume
  authorized_start: V01
  terminal_boundary: V07
  committed_high_water_mark: V03
  next_candidate_operation: V04
  confirmation_between_units: false
  run_state: active
---

# Kamakura Police Station — current state and corpus map

**SEQUENTIAL_ANALYSIS_LOCK = OPEN.** The owner authorized continuous sequential analysis of V01–V07 from the local Japanese witnesses. The committed high-water mark is **V03**, through [KSOA-V03-H-0013](readings/KSOA_V03_DEEP_READING.md#ksoa-v03-h-0013). **V04** is the next permitted operation.

`series/kamakura-sho/` is the canonical root for *Kamakura Police Station: The Case Files of Asumi Ogasawara* / 鎌倉署・小笠原亜澄の事件簿 by 鳴神響一 (Kyōichi Narukami), 文藝春秋 / 文春文庫. The planned corpus is V01 稲村ヶ崎の落日, V02 由比ヶ浜協奏曲, V03 極楽寺逍遙, V04 竹寺の雪, V05 西御門の館, V06 佐助ヶ谷の銀雫 and V07 長谷の花舞, the publisher-identified finale.

The primary sources are the seven Japanese EPUBs in the owner's local `Main Series` collection and matching copies in the canonical Google Drive evidence folder. The [witness map](KSOA_SOURCE_AND_WITNESS_MAP.md) identifies that folder, the existing import records, the exact editions and hashes, and the chapter-to-member mapping. All seven local/Drive copies and all three provenance records matched byte for byte. ZIP, package and navigation checks passed within the scope recorded there. Full EPUBCheck remains unverified. The per-volume witness and coverage records state what has been read and which apparatus was inspected.

| Canonical home | Responsibility |
|---|---|
| [Analytical method](KSOA_ANALYTICAL_METHOD.md) | Governs primary-text reading, evidence judgments, spoiler control and volume closeout |
| [Synthesis architecture](KSOA_SYNTHESIS_ARCHITECTURE.md) | Defines cumulative homes, stage ownership, dependencies and completion gates |
| [Source and witness map](KSOA_SOURCE_AND_WITNESS_MAP.md) | Binds works and witnesses, defines locators and records source coverage |
| [Case evidence ledger](KSOA_CASE_EVIDENCE_LEDGER.md) | Owns fictional events, evidence objects, testimony, investigative actions and case reconstructions |
| [Disclosure and hypothesis ledger](KSOA_DISCLOSURE_AND_HYPOTHESIS_LEDGER.md) | Owns frozen knowledge horizons, prospective hypotheses and later adjudications |
| [Character and relationship ledger](KSOA_CHARACTER_AND_RELATIONSHIP_LEDGER.md) | Owns time-indexed actor states, directed relationships and portrayed institutional practice |
| [Claim revision ledger](KSOA_CLAIM_REVISION_LEDGER.md) | Owns material interpretive claims, counterevidence, revisions and dependent-study routing |
| [Character reconstruction specification](KSOA_CHARACTER_RECONSTRUCTION_SPEC.md) | Defines the evidence and independent testing needed for a bounded future reconstruction |
| [Bootstrap review](KSOA_BOOTSTRAP_REVIEW.md) | Records producer scope, unresolved questions and receiving review obligations |

## Accepted readings

| Unit | Accepted reading |
|---|---|
| V01 | [稲村ヶ崎の落日](readings/KSOA_V01_DEEP_READING.md) |
| V02 | [由比ヶ浜協奏曲](readings/KSOA_V02_DEEP_READING.md) |
| V03 | [極楽寺逍遙](readings/KSOA_V03_DEEP_READING.md) |

## Active run

The [initiation policy](../../governance/source-policies/MANGA_ANIME_PROJECT_INITIATION_AND_ARCHITECTURE_POLICY.md) and [continuation policy](../../governance/source-policies/MANGA_ANIME_SEQUENTIAL_EXECUTION_SCOPE_AND_CONTINUATION_POLICY.md) govern the active V01–V07 range. Recheck each local EPUB against the witness map at admission. Carry forward only the previous accepted freeze, and close and commit each volume before advancing. The [execution and acceptance gates](KSOA_SYNTHESIS_ARCHITECTURE.md#execution-and-acceptance-gates) govern checkpoints, reconciliation and synthesis.
