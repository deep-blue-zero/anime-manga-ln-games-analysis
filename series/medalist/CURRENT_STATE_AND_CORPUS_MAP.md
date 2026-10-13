---
title: "Medalist — Current State and Corpus Map"
artifact_id: "MEDALIST_CURRENT_STATE_AND_CORPUS_MAP"
artifact_type: "current_state_corpus_map"
series: "Medalist / メダリスト"
series_id: "medalist"
generation: "MEDALIST_BOOTSTRAP_V1"
version: "1.2"
status: "canonical"
scope: "Single project entrypoint, initiation state, current authority and next permitted operation"
canonical_home: "series/medalist/CURRENT_STATE_AND_CORPUS_MAP.md"
source_boundary: "Japanese V01–V08 closed (Scores 1–32, Short Programs 1–4, one Exhibition, own-volume material); fanbooks and later sources unadmitted"
created: "2026-10-11"
updated: "2026-10-13"
review_status: "AUTHOR_REVIEWED_V08_UPDATE"
foundation_owner_approval: "I approve the revised foundation. Begin analysis/deep reading of Volume 1."
continuation_owner_authorization: "2026-10-12 owner continuous_sequential authorization: V02 through the verified as-of-start publication boundary (V15, Score 61), then provisional syntheses"
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
do_not_use_as_literary_evidence: true
recommended_reasoning_class: "DEEP_SYNTHESIS"
---

# Medalist — current state and corpus map

Start here for `series/medalist/`, the continuing Japanese manga project for メダリスト by つるまいかだ. Branch: `series/medalist`. The owner approved the revised version-0.2 foundation and authorized a single complete V01 reading. Current governing homes are canonical; lifecycle was INITIAL at activation and is now EVOLVING after the first evidence-driven V01 review. Approval of the method/schema does not pre-approve new character or interpretive conclusions.

**SEQUENTIAL_ANALYSIS_LOCK = OPEN**

**A `continuous_sequential` run is active: V02 through V15, one closed volume transaction at a time. Committed high-water mark: V08. Next candidate: V09.** The owner authorized this run on 2026-10-12; the [continuous-run receipt](07%20Audits%20and%20Handoffs/MEDALIST_CONTINUOUS_RUN_AUTHORIZATION_AND_SOURCE_RECEIPT.md) records the authorization, the dated publication ceiling (V15, ending at Score 61; no serial-only Score beyond it) and the structurally verified witnesses. [V01 deep reading and MD-FR-V01](02%20Sequential%20Readings/MEDALIST_V01_DEEP_READING.md) remain frozen and are not redone; the latest closed reading is [V08 / MD-FR-V08](02%20Sequential%20Readings/MEDALIST_V08_DEEP_READING.md), and the progress table below lists every closed unit. Fanbook coverage reconnaissance and audits are authorized only at a verified safe manga checkpoint; adaptation sources remain unauthorized. The historical single-operation V01 authorization is preserved in its own receipt.

## Recoverable project initialization

```yaml
project_initialization:
  status: canonical
  bootstrap_generation: MEDALIST_BOOTSTRAP_V1
  base_origin_main: "238fed779661f6a5a49d6a70034a6183d17ca175"
  architecture_lifecycle: EVOLVING
  governing_method: "00 Frameworks and Methods/MEDALIST_ANALYTICAL_METHOD.md"
  synthesis_architecture: "00 Frameworks and Methods/MEDALIST_SYNTHESIS_ARCHITECTURE.md"
  method_status: canonical
  architecture_status: canonical
  source_reconnaissance_complete: true
  source_reconnaissance_status: "METADATA_AND_PUBLICATION_RECONNAISSANCE_COMPLETE_WITH_EXPLICIT_GAPS"
  source_authentication_status: V01_DELIVERED_INTEGRITY_AND_COMPONENT_MAP_VERIFIED_PRINTING_UNVERIFIED
  required_ledgers_initialized: true
  required_day_one_infrastructure:
    - "03 Longitudinal Ledgers/MEDALIST_CHARACTER_DEVELOPMENT_AND_READINESS_LEDGER.md"
    - "03 Longitudinal Ledgers/MEDALIST_RELATIONSHIP_RIVALRY_AND_MENTORSHIP_LEDGER.md"
    - "03 Longitudinal Ledgers/MEDALIST_SKATING_TRAINING_AND_COMPETITION_LEDGER.md"
    - "03 Longitudinal Ledgers/MEDALIST_INSTITUTIONS_RESOURCES_AND_AUTHORITY_LEDGER.md"
    - "03 Longitudinal Ledgers/MEDALIST_CHRONOLOGY_INFORMATION_AND_RETROSPECTION_LEDGER.md"
    - "03 Longitudinal Ledgers/MEDALIST_VISUAL_FORM_AND_PERFORMANCE_LEDGER.md"
    - "03 Longitudinal Ledgers/MEDALIST_CLAIMS_PREDICTIONS_AND_REVISIONS_LEDGER.md"
  substantive_sequential_findings_at_bootstrap: false
  completed_sequential_readings: 8
  owner_review_state: APPROVED_REVISED_FOUNDATION_0_2
  sequential_analysis_lock: OPEN
  lock_reason: OWNER_APPROVED_FOUNDATION_AND_AUTHORIZED_V01
  lock_reason_current_run: OWNER_AUTHORIZED_CONTINUOUS_SEQUENTIAL_V02_TO_V15
  next_permitted_operation: "V09 complete volume transaction under the active continuous run"
sequential_execution:
  mode: continuous_sequential
  unit_type: japanese_tankobon_volume
  authorized_start: V02
  terminal_boundary: V15
  terminal_boundary_basis: "Verified publication ceiling at 2026-10-12: V15 collects through Score 61; no serial-only Score beyond it"
  committed_high_water_mark: V08
  next_candidate_operation: V09
  next_candidate_authorization: AUTHORIZED_WITHIN_ACTIVE_RUN
  confirmation_between_units: false
  run_state: active
  prior_run: "single_operation V01, COMPLETED"
supplemental_execution:
  scheduled_units: [FB01, FB02]
  admission_positions_status: HOLD_COVERAGE_UNVERIFIED
  authorized_start: "Coverage reconnaissance and conditional audit at a verified safe manga checkpoint"
  completed_paratext_audits: 0
  committed_high_water_mark: null
  run_state: AUTHORIZED_CONDITIONAL_NOT_STARTED
synthesis_execution:
  authorized_scope: "Provisional character, relationship, specialist and integrated syntheses at the locked boundary"
  run_state: NOT_STARTED
  series_state: ONGOING
```

Preliminary reconnaissance is sufficient for design; the true source gaps below remain unresolved. The seven day-one instruments were empty at activation. All seven now contain version-1 V01 records, including separate readiness decisions, and the real `02 Sequential Readings/` home contains one complete reading with `MD-FR-V01`. The authorization/source receipt preserves its zero-reading activation snapshot. The completed boundary is V01, including its own bonus fiction and attributed paratext; this is not whole-series or fanbook completion. Repository publication/audit evidence is recovered from the containing commits and exact-head GitHub statuses, not preclaimed in prose.

## Governing route

1. [Analytical method](00%20Frameworks%20and%20Methods/MEDALIST_ANALYTICAL_METHOD.md) — observe, interpret and preserve prospective state.
2. [Synthesis architecture](00%20Frameworks%20and%20Methods/MEDALIST_SYNTHESIS_ARCHITECTURE.md) — accumulation, responsibilities, promotion, convergence and completion.
3. [Source and scope map](00%20Frameworks%20and%20Methods/MEDALIST_SOURCE_AND_SCOPE_MAP.md) — exact visible witnesses, provenance stages, publication uncertainty and locators.
4. [Source-unit reading specification](00%20Frameworks%20and%20Methods/MEDALIST_SOURCE_UNIT_READING_SPEC.md) — atomic reading/freeze/closeout contract, exercised at V01.
5. [Character reconstruction specification](00%20Frameworks%20and%20Methods/MEDALIST_CHARACTER_RECONSTRUCTION_SPEC.md) — independent monograph/model/domain readiness gates.
6. [Bootstrap receipt](07%20Audits%20and%20Handoffs/MEDALIST_BOOTSTRAP_RECEIPT.md) — exact authored inventory, checks and recoverable publication/audit state.

## Current source boundaries

| Boundary | Current fact |
| --- | --- |
| Inventory | Drive snapshot: Japanese V13–V15 and English V01–V12; local addendum: Japanese V01–V15 containers plus Official Fanbook 01/02, filenames/sizes only |
| Structurally verified / admitted / narratively inspected / closed | 15 volume witnesses at container level / V01–V08 / all admitted images of V01–V08 / 8, latest MD-FR-V08 |
| Planned primary sequence | Japanese V01 onward, one authenticated volume per transaction; V02–V15 authorized as one continuous run with fourteen separately closed transactions |
| First-source route | V01 delivered CBZ integrity/component map verified, inspected and closed with original-image locators; printing unverified. V02–V15 delivered witnesses passed CRC, full image decode and hash checks at activation; none narratively inspected at that snapshot |
| Supplemental source positions | FB01/FB02 inventory-visible; each coverage boundary and admit_after null/unverified; zero completed fanbook audits |
| Public collected record | V15 latest identified by official publisher records at reconnaissance |
| Public serialized record | Score 61 (second installment, August 2026 issue, on sale 2026-06-25) is the last serialized installment; official September–November 2026 issue contents omit the series |
| V15 chapter range / hiatus | V15 witness navigation lists Scores 57–61, to be confirmed page by page when V15 is read; hiatus announced 2026-09-04 with no resumption found at the 2026-10-12 snapshot |
| Terminal boundary of the active run | V15 / Score 61, fixed at 2026-10-12; later publication needs a new authorization |
| Adaptation | S1/S2 planned distinct lane; no admitted episode/audio/video or manga crosswalk |

V01 is the sole completed narrative boundary. These facts do not establish later narrative coverage, an explanation beyond the notice's stated production circumstances, or a finished-series boundary. Later snippets returned by publication searches remain prior-exposure disclosures, not findings.

## Continuous-run progress

One row is appended when a volume transaction has closed locally: reading, seven-ledger reconciliation, freeze and source-map advancement in one commit. Publication and exact-head audit evidence is recovered from Git history and GitHub statuses, not asserted here.

| Unit | Scores | Reading / freeze | Ledger versions at freeze | State |
| --- | --- | --- | --- | --- |
| V01 | 1–3 | [V01](02%20Sequential%20Readings/MEDALIST_V01_DEEP_READING.md) / MD-FR-V01 | 1.0 | Closed under the earlier single-operation run |
| V02 | 4–7 | [V02](02%20Sequential%20Readings/MEDALIST_V02_DEEP_READING.md) / MD-FR-V02 | 1.1 | Closed 2026-10-13; first competition results; claims 0001–0013 at version 2, 0014–0018 new |
| V03 | 8–11 | [V03](02%20Sequential%20Readings/MEDALIST_V03_DEEP_READING.md) / MD-FR-V03 | 1.2 | Closed 2026-10-13; first defeat, an injury and a one-year elision; fourteen claims advanced a version, 0019–0021 new |
| V04 | 12–15 | [V04](02%20Sequential%20Readings/MEDALIST_V04_DEEP_READING.md) / MD-FR-V04 | 1.3 | Closed 2026-10-13; summer camp and grade-6 test, no competition; fifteen claims advanced a version, 0022 new |
| V05 | 16–19 | [V05](02%20Sequential%20Readings/MEDALIST_V05_DEEP_READING.md) / MD-FR-V05 | 1.4 | Closed 2026-10-13; block competition in progress, thirteen of fifteen skated, protagonist's skate pending; fourteen claims advanced a version, 0023–0024 new |
| V06 | 20–23 | [V06](02%20Sequential%20Readings/MEDALIST_V06_DEEP_READING.md) / MD-FR-V06 | 1.5 | Closed 2026-10-13; block competition won at 81.20, both coaches' creeds stated, about two weeks before the All-Japan Novice; twenty claims advanced a version, 0025 new |
| V07 | 24–28 | [V07](02%20Sequential%20Readings/MEDALIST_V07_DEEP_READING.md) / MD-FR-V07 | 1.6 | Closed 2026-10-13; preparation for the All-Japan Novice, a coach's injury, a lost jump and a first quadruple, ending at the opening ceremony; twenty-one claims advanced a version, none new |
| V08 | 29–32 | [V08](02%20Sequential%20Readings/MEDALIST_V08_DEEP_READING.md) / MD-FR-V08 | 1.7 | Closed 2026-10-13; All-Japan Novice in progress, eleven of thirty-six scored, leader 128.98, protagonist's skate pending; first EPUB witness; seventeen claims advanced a version, 0026 new |

## Supplemental checkpoint route

The [architecture fanbook checkpoint](00%20Frameworks%20and%20Methods/MEDALIST_SYNTHESIS_ARCHITECTURE.md#fanbook-admission-checkpoints), [source schedule](00%20Frameworks%20and%20Methods/MEDALIST_SOURCE_AND_SCOPE_MAP.md#local-inventory-addendum-and-supplemental-schedule-2026-10-12) and [paratext-audit contract](00%20Frameworks%20and%20Methods/MEDALIST_SOURCE_UNIT_READING_SPEC.md#fanbook-paratext-audit-transaction) now cover FB01/FB02. Each enters after its verified manga cutoff is closed and frozen, then contributes an independently frozen supplemental delta before combined boundary synthesis. The numeric cutoffs remain pending verification; neither V15 nor a book number supplies them. Mainline manga completion and supplemental completion are tracked separately. There are no fanbook findings or audit artifacts yet.

## Initialized longitudinal responsibilities

- [CHARACTER_DEVELOPMENT_AND_READINESS_LEDGER](03%20Longitudinal%20Ledgers/MEDALIST_CHARACTER_DEVELOPMENT_AND_READINESS_LEDGER.md)
- [RELATIONSHIP_RIVALRY_AND_MENTORSHIP_LEDGER](03%20Longitudinal%20Ledgers/MEDALIST_RELATIONSHIP_RIVALRY_AND_MENTORSHIP_LEDGER.md)
- [SKATING_TRAINING_AND_COMPETITION_LEDGER](03%20Longitudinal%20Ledgers/MEDALIST_SKATING_TRAINING_AND_COMPETITION_LEDGER.md)
- [INSTITUTIONS_RESOURCES_AND_AUTHORITY_LEDGER](03%20Longitudinal%20Ledgers/MEDALIST_INSTITUTIONS_RESOURCES_AND_AUTHORITY_LEDGER.md)
- [CHRONOLOGY_INFORMATION_AND_RETROSPECTION_LEDGER](03%20Longitudinal%20Ledgers/MEDALIST_CHRONOLOGY_INFORMATION_AND_RETROSPECTION_LEDGER.md)
- [VISUAL_FORM_AND_PERFORMANCE_LEDGER](03%20Longitudinal%20Ledgers/MEDALIST_VISUAL_FORM_AND_PERFORMANCE_LEDGER.md)
- [CLAIMS_PREDICTIONS_AND_REVISIONS_LEDGER](03%20Longitudinal%20Ledgers/MEDALIST_CLAIMS_PREDICTIONS_AND_REVISIONS_LEDGER.md)

Each home defines stable record IDs, trigger, evidence/confidence, links and historical versus mutable state. Read the architecture matrix before updating them; source observations remain in the frozen V01 reading, claims/revisions have one home, and readiness has no global curation effect. Global entity/subject IDs remain null in the local character register; no monograph, reconstruction model or specialist was promoted.

## Authority, execution and owner-review decisions

Current governing Markdown is canonical with complete authority metadata. Foundation version 0.2 retains owner approval; the V01 interpretation, ledger records and evidence-driven version-0.4 updates are AUTHOR_REVIEWED_V01_UPDATE, not pre-approved owner conclusions. The bootstrap receipt preserves its historical provisional snapshot; new source findings require their own evidence/confidence and author review. The local [.repository descriptor](.repository/series-registry.json) declares `project_initiation_gate: REQUIRED`, `PRESENT_VERIFIED` entrypoint structure and `PRESENT_REVIEWED` foundation materialization. Housekeeping owns global routing; the author does not edit global series/corpus or character outputs. Branch publication and main integration do not constitute owner architectural approval.

The owner has accepted those version-0.2 design choices: collected-volume transactions with bounded serial exceptions, seven cumulative homes, historical freezes, four-channel skating evidence, separate readiness gates, fanbook checkpoints and deferred adaptation. The [V01 authorization/source receipt](07%20Audits%20and%20Handoffs/MEDALIST_V01_AUTHORIZATION_AND_SOURCE_RECEIPT.md) records direct approval, delivered-witness checks, incidental exposure and V01-only activation. The [closed reading](02%20Sequential%20Readings/MEDALIST_V01_DEEP_READING.md) owns actual observations and frozen exit state. No later reading follows automatically from this approval.

Preferred future topology is staged: local primary reading/ledgers; fresh cloud substantial synthesis at a pinned boundary; local required evidence completion, reconciliation and authorized Git publication. Historical bootstrap capability state was metadata-only. V01 now verifies local bytes/container decoding and actual original-image/Japanese text inspection; audio/continuous AV remain unexercised. Source availability and actual perception must be checked per stage. No literal model/effort or account allowance is inferred.

## Architecture revision record

2026-10-12, version 0.2: incorporated the owner-selected COTE guidebook pattern into the method, architecture, source map, reading specification and reconstruction contract; recorded newly observed local source filenames. Kept the seven ledgers and historical bootstrap receipt unchanged. No source contents admitted/inspected, no readings completed and no owner approval inferred. The original bootstrap is now present on main through reviewed PR #155 (`4a3a9cb5422ff5e817fff1603ef61c5d428e6a23`); that publication does not open the analytical lock. This amendment's commit and exact-head audits remain externally recoverable through Git history/status.

2026-10-12, version 0.3: owner approved the revised foundation and authorized V01 only; current governing homes promoted, OPEN recorded after delivered-witness verification, seven ledger schemas retained empty at activation. Structural inspection exposed the opening prologue and jacket gags; that exposure is explicitly retained.

2026-10-12, version 0.4: complete V01 witness inspected and interpreted; seven ledgers reconciled and MD-FR-V01 frozen. Architecture moves to EVOLVING without adding infrastructure. Mainline ends before the competition; bonus fiction recontextualizes access/support. No later source or fanbook admitted. The single-operation run is COMPLETED; V02 is an unauthorized candidate.

2026-10-12, version 0.5: owner authorized `continuous_sequential` execution from V02 through the verified as-of-start publication boundary, conditional fanbook audits and provisional boundary syntheses. Publication ceiling fixed at V15 / Score 61 from official issue contents, the catalog listing and the V15 witness navigation; no serial-only unit exists. Fourteen target witnesses and both fanbook containers structurally verified without narrative inspection. A second locator version covers the fixed-layout EPUB witnesses. The four specification documents now state their source boundary by reference to this entrypoint instead of naming a volume, so they do not go stale at each closure; their analytical contracts are unchanged. No infrastructure added; lifecycle stays EVOLVING. Paragraphs above that describe V02 or the fanbooks as unauthorized are version-0.3/0.4 history.

2026-10-13, version 0.6: V02 closed. All 203 images inspected; Scores 4–7 and Short Programs 3–4 read; seven ledgers reconciled to version 1.1; thirteen V01 claims adjudicated to version 2 with recorded revisions and five new claims registered; MD-FR-V02 frozen. Mainline stands at the morning of the West Japan meet with no result. No infrastructure added. From this version the front-matter source boundary names the latest closed volume and the progress table carries per-unit detail. Statements in the sections below about seven version-1 ledgers and a single reading describe the V01 state.

2026-10-13, version 0.7: V03 closed. All 203 images inspected; Scores 8–11 read; seven ledgers reconciled to version 1.2; fourteen claims advanced with recorded revisions, four preserved and three registered; MD-FR-V03 frozen. The mainline passes through the West Japan meet (Inori second with 24.32), a jointly decided year without winter competitions that the manga elides, and a second 名港杯 at badge grade 5, and stands at Inori's vow to Rio. No infrastructure added; regional speech variety is noted as a recurring feature still served by observation rows.

2026-10-13, version 0.8: V04 closed. All 203 images inspected; Scores 12–15 read; seven ledgers reconciled to version 1.3; fifteen claims advanced with recorded revisions, six preserved and one registered; MD-FR-V04 frozen. The mainline passes through the Tsuruga summer camp and the grade-6 badge test, with no competition held, and stands at entry to the Chūbu block competition. No infrastructure added; practice and test attempts are carried in the skating ledger's performance table with explicit labels.

2026-10-13, version 0.9: V05 closed. All 187 images inspected; Scores 16–19 and one bonus Exhibition read; seven ledgers reconciled to version 1.4; fourteen claims advanced with recorded revisions, eight preserved and two registered; MD-FR-V05 frozen. The mainline stands inside the Chūbu block competition after the thirteenth of fifteen Novice A free skates, before the protagonist's. No infrastructure added; the first scored qualifier with printed protocols fitted the existing skating tables, and facing-page geometry was verified for two spreads.

2026-10-13, version 1.0: V06 closed. All 205 images inspected; Scores 20–23 read; seven ledgers reconciled to version 1.5; twenty claims advanced with recorded revisions, four preserved and one registered; MD-FR-V06 frozen. The mainline completes the Chūbu block competition, which the protagonist wins, and stands about two weeks before the All-Japan Novice. No infrastructure added; a volume of spoken disclosure was carried by the chronology ledger's knowledge and retrospection tables, and a verbal motif was registered in the visual ledger.

2026-10-13, version 1.1: V07 closed. All 203 images inspected; Scores 24–28 read; seven ledgers reconciled to version 1.6; twenty-one claims advanced with recorded revisions, four preserved and none registered; MD-FR-V07 frozen. The mainline stands at the opening ceremony of the All-Japan Novice. No infrastructure added; qualifiers reported at second hand were carried in the skating ledger's competition table with labels, and a coach's injury as a state event and a technical constraint.

2026-10-13, version 1.2: V08 closed. All 187 image occurrences of the first EPUB witness inspected; Scores 29–32 read; seven ledgers reconciled to version 1.7; seventeen claims advanced with recorded revisions, eight preserved and one registered; MD-FR-V08 frozen. The mainline stands inside the All-Japan Novice after its eleventh scored skater, before the protagonist's free skate. No infrastructure added; the EPUB locator version declared at activation was used unchanged, and two source-internal disagreements were recorded without resolution.

## Higher-level governing controls

- [Repository authority/routing](../../governance/CHATGPT_AUTHORITY_AND_ROUTING.md), [authority state](../../governance/AUTHORITY_STATE.yaml) and [scope](../../governance/AUTHORITY_SCOPE.json).
- [Initiation policy](../../governance/source-policies/MANGA_ANIME_PROJECT_INITIATION_AND_ARCHITECTURE_POLICY.md) and [authority/supersession](../../governance/source-policies/ARCHIVE_AUTHORITY_AND_SUPERSESSION_POLICY.md).
- [Reasoning routing](../../governance/source-policies/MANGA_ANIME_REASONING_AND_MODEL_ROUTING_POLICY.md), [capabilities](../../governance/source-policies/MANGA_ANIME_EXECUTION_TOPOLOGY_AND_CAPABILITY_ROUTING_POLICY.md), [long-series protocol](../../governance/source-policies/MANGA_ANIME_LONG_SERIES_HYBRID_EXECUTION_PROTOCOL.md).
- [Handoff contract](../../governance/source-policies/MANGA_ANIME_ANALYTICAL_HANDOFF_AND_INTEGRATION_CONTRACT.md), [continuation](../../governance/source-policies/MANGA_ANIME_SEQUENTIAL_EXECUTION_SCOPE_AND_CONTINUATION_POLICY.md) and [episode evidence](../../governance/source-policies/MANGA_ANIME_EPISODE_BUNDLE_SPECIFICATION.md).
- [Integration checklist](../../governance/policies/CHANGE_INTEGRATION_CHECKLIST.md), [branch lifecycle](../../governance/policies/BRANCH_LIFECYCLE.md), [housekeeping ownership](../../governance/policies/AUTOMATED_GLOBAL_INDEX_MAINTENANCE.md) and [change obligations](../../governance/repository-controls/change-obligations.json).
