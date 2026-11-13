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
source_boundary: "Japanese publisher EPUBs V01–V07. Bibliography, bytes and package structure reconciled. Narrative admission and inspection are pending."
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
  source_admission: NONE
  required_day_one_infrastructure_initialized: true
  required_day_one_infrastructure:
    - KSOA_SOURCE_AND_WITNESS_MAP.md
    - KSOA_CASE_EVIDENCE_LEDGER.md
    - KSOA_DISCLOSURE_AND_HYPOTHESIS_LEDGER.md
    - KSOA_CHARACTER_AND_RELATIONSHIP_LEDGER.md
    - KSOA_CLAIM_REVISION_LEDGER.md
  substantive_sequential_findings_at_bootstrap: false
  sequential_analysis_lock: closed
  next_permitted_operation: NONE_AWAITING_RUN_AUTHORIZATION
  run_authorization: NONE
  committed_high_water_mark: NONE
  sequential_units_admitted: 0
  sequential_units_completed: 0
---

# Kamakura Police Station — current state and corpus map

**SEQUENTIAL_ANALYSIS_LOCK = CLOSED.** Next permitted narrative operation is **NONE_AWAITING_RUN_AUTHORIZATION**. The architecture is `INITIAL`. No sequential run exists. All seven volumes are unadmitted, and the analytical ledgers have zero rows.

`series/kamakura-sho/` is the canonical root for *Kamakura Police Station: The Case Files of Asumi Ogasawara* / 鎌倉署・小笠原亜澄の事件簿 by 鳴神響一 (Kyōichi Narukami), 文藝春秋 / 文春文庫. The planned corpus is V01 稲村ヶ崎の落日, V02 由比ヶ浜協奏曲, V03 極楽寺逍遙, V04 竹寺の雪, V05 西御門の館, V06 佐助ヶ谷の銀雫 and V07 長谷の花舞, the publisher-identified finale.

The primary sources are the seven Japanese EPUBs in the owner's local `Main Series` collection and matching copies in the canonical Google Drive evidence folder. The [witness map](KSOA_SOURCE_AND_WITNESS_MAP.md) identifies that folder, the existing import records, the exact editions and hashes, and the chapter-to-member mapping. All seven local/Drive copies and all three provenance records matched byte for byte. ZIP, package and navigation checks passed within the scope recorded there. Full EPUBCheck, reading-route fidelity, the two chapter images and narrative coverage remain unverified.

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

## Before V01

1. Review the full foundation against the live [initiation policy](../../governance/source-policies/MANGA_ANIME_PROJECT_INITIATION_AND_ARCHITECTURE_POLICY.md) and [continuation policy](../../governance/source-policies/MANGA_ANIME_SEQUENTIAL_EXECUTION_SCOPE_AND_CONTINUATION_POLICY.md). Resolve any material receiving findings and recover explicit owner authorization for the first unit and terminal boundary. A V01 request covers one volume unless the owner authorizes continuation.
2. Bind V01 to its exact witness, confirm the prologue-to-epilogue span and provisional paratext dispositions, and verify that the next authorized portion can be read faithfully in Japanese with its layout and ruby. Record any prior exposure and the entering reader and character knowledge boundaries.
3. Record a consistent OPEN transition and active run with its authorized start, terminal boundary and matching next-operation fields before staging a sequential reading. Use the method's chapter freezes inside the V01 transaction. The [execution and acceptance gates](KSOA_SYNTHESIS_ARCHITECTURE.md#execution-and-acceptance-gates) govern advance, reconciliation and later synthesis.
