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
source_boundary: "Japanese publisher EPUBs V01–V07. Sequential reading and producer synthesis are complete through V07."
canonical_home: series/kamakura-sho/CURRENT_STATE_AND_CORPUS_MAP.md
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
do_not_use_as_literary_evidence: true
project_initialization:
  status: canonical
  architecture_lifecycle: STABILIZED
  bootstrap_generation: KSOA-G1
  governing_method: KSOA_ANALYTICAL_METHOD.md
  method_status: canonical
  synthesis_architecture: KSOA_SYNTHESIS_ARCHITECTURE.md
  architecture_status: canonical
  source_reconnaissance_complete: true
  source_reconnaissance_scope: "All seven Japanese EPUBs. Local and Drive bytes, import provenance, package structure and navigation."
  source_admission: V01_THROUGH_V07
  required_day_one_infrastructure_initialized: true
  required_day_one_infrastructure:
    - KSOA_SOURCE_AND_WITNESS_MAP.md
    - KSOA_CASE_EVIDENCE_LEDGER.md
    - KSOA_DISCLOSURE_AND_HYPOTHESIS_LEDGER.md
    - KSOA_CHARACTER_AND_RELATIONSHIP_LEDGER.md
    - KSOA_CLAIM_REVISION_LEDGER.md
  substantive_sequential_findings_at_bootstrap: false
  sequential_analysis_lock: open
  next_permitted_operation: NONE
  run_authorization: "Owner instruction in the current Codex task to analyze all seven local Japanese novels and generate the artifacts required by the architecture."
  committed_high_water_mark: V07
  sequential_units_admitted: 7
  sequential_units_completed: 7
sequential_execution:
  mode: continuous_sequential
  unit_type: volume
  authorized_start: V01
  terminal_boundary: V07
  committed_high_water_mark: V07
  next_candidate_operation: NONE
  confirmation_between_units: false
  run_state: completed
---

# Kamakura Police Station — current state and corpus map

**SEQUENTIAL_ANALYSIS_LOCK = OPEN.** The owner authorized continuous sequential analysis of V01–V07 from the local Japanese witnesses. The committed high-water mark is **V07**, through [KSOA-V07-H-0015](readings/KSOA_V07_DEEP_READING.md#ksoa-v07-h-0015). The authorized run reached its terminal boundary. No next source operation is permitted.

`series/kamakura-sho/` is the canonical root for *Kamakura Police Station: The Case Files of Asumi Ogasawara* / 鎌倉署・小笠原亜澄の事件簿 by 鳴神響一 (Kyōichi Narukami), 文藝春秋 / 文春文庫. The seven-work corpus is V01 稲村ヶ崎の落日, V02 由比ヶ浜協奏曲, V03 極楽寺逍遙, V04 竹寺の雪, V05 西御門の館, V06 佐助ヶ谷の銀雫 and V07 長谷の花舞, the publisher-identified finale.

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
| V04 | [竹寺の雪](readings/KSOA_V04_DEEP_READING.md) |
| V05 | [西御門の館](readings/KSOA_V05_DEEP_READING.md) |
| V06 | [佐助ヶ谷の銀雫](readings/KSOA_V06_DEEP_READING.md) |
| V07 | [長谷の花舞](readings/KSOA_V07_DEEP_READING.md) |

## Synthesis and reconciliation

The [terminal source completion and reconciliation](audits/KSOA_SOURCE_COMPLETION_AND_LONGITUDINAL_RECONCILIATION.md) binds all seven EPUBs, 36 narrative sections, 104 frozen horizons and 459 volume-level ledger records. Earlier reconciliation remains available at the [V01 closeout](readings/KSOA_V01_DEEP_READING.md#closeout-and-limits) and [V04 midpoint](audits/KSOA_V04_LONGITUDINAL_RECONCILIATION.md). The [late event chronologies](audits/KSOA_SOURCE_COMPLETION_AND_LONGITUDINAL_RECONCILIATION.md#v06-and-v07-event-chronologies) route through the case ledger. The case, disclosure and character ledgers preserve the exact terminal blobs, including their historical initialization headers. Their volume sections and the coverage table above give the current frontier. The [role-gap audit](audits/KSOA_ARCHITECTURE_ROLE_GAP_AUDIT.md) accounts for all sixteen required responsibilities. The [convergence review](audits/KSOA_SPECIALIST_CONVERGENCE.md) adjudicates the studies’ scope and disagreements.

| Study | Question |
|---|---|
| [Integrated series synthesis](studies/KSOA_INTEGRATED_SERIES_SYNTHESIS.md) | How the mysteries make the work of knowing, protecting and disclosing visible across the series |
| [Mystery form and causal attribution](studies/KSOA_MYSTERY_FORM_AND_CAUSALITY.md) | Which roles and clues a reader can establish, and when |
| [Asumi Ogasawara](studies/KSOA_ASUMI_OGASAWARA.md) | How observation, register, authority and vulnerability shape her work |
| [Motoya Kitsukawa](studies/KSOA_MOTOYA_KITSUKAWA.md) | How his independent work, focalization and discretion bear on his self-assessment |
| [Asumi and Motoya’s partnership](studies/KSOA_PARTNERSHIP.md) | How directed professional and personal commitments change under unequal knowledge |
| [Policing, place and narration](studies/KSOA_POLICING_PLACE_AND_NARRATION.md) | How institutions, geography and prose give access to evidence and set its limits |
| [Character reconstruction readiness](audits/KSOA_CHARACTER_RECONSTRUCTION_READINESS.md) | Where the literary evidence supports a bounded candidate and what independent validation requires |

The current cross-volume formulations and source routes are in the [series claim history](KSOA_CLAIM_REVISION_LEDGER.md#series-claim-history). The studies and this table contain solutions. For a bounded reading, use the [disclosure ledger](KSOA_DISCLOSURE_AND_HYPOTHESIS_LEDGER.md) and the [checkpoint locator addendum](audits/KSOA_CHECKPOINT_LOCATOR_ADDENDUM.md) to extract the applicable freeze.

## Completed run and review status

The terminal reading is pinned at `9fee95813a8df8c19621001ae7cb1c9bc02f76bc`. The [completion proof](.repository/completed-run-publication.json) binds that state and its active first parent. The [continuation policy](../../governance/source-policies/MANGA_ANIME_SEQUENTIAL_EXECUTION_SCOPE_AND_CONTINUATION_POLICY.md) governs the recorded completed state. Any new source operation requires a new authority decision.

Producer authoring and semantic review are complete. The architecture is `STABILIZED`. [PR #551](https://github.com/deep-blue-zero/anime-manga-ln-games-analysis/pull/551) holds the candidate for receiving acceptance. Its audit is tied to the PR head. The [producer review and handoff](audits/KSOA_PRODUCER_REVIEW_AND_RECEIVING_HANDOFF.md) records verification, residual limits and the conditions for a frozen release.
