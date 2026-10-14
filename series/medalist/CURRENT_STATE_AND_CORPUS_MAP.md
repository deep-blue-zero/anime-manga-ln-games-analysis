---
title: "Medalist — Current State and Corpus Map"
artifact_id: "MEDALIST_CURRENT_STATE_AND_CORPUS_MAP"
artifact_type: "current_state_corpus_map"
series: "Medalist / メダリスト"
series_id: "medalist"
generation: "MEDALIST_BOOTSTRAP_V1"
version: "1.12"
status: "canonical"
scope: "Single project entrypoint, initiation state, current authority and next permitted operation"
canonical_home: "series/medalist/CURRENT_STATE_AND_CORPUS_MAP.md"
source_boundary: "Japanese V01–V15 closed (Scores 1–61, Short Programs 1–7, three Exhibitions, own-volume material); Official Fanbooks 01 and 02 audited (MD-FR-FB01, MD-FR-FB02); later sources unadmitted"
created: "2026-10-11"
updated: "2026-10-13"
review_status: "AUTHOR_REVIEWED_SYNTHESIS_RELEASE_UPDATE"
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

**The `continuous_sequential` run authorized on 2026-10-12 is complete: V02 through V15, one closed volume transaction at a time. Committed high-water mark: V15, the run's terminal boundary; all fourteen volume transactions are closed. Official Fanbooks 01 and 02 are audited at this checkpoint (MD-FR-FB01, MD-FR-FB02). The provisional syntheses are released as eight version-1 artifacts (see the section below). The series is ONGOING and every synthesis is provisional through this boundary. Nothing further is authorized: a later volume or instalment, a third fanbook, the adaptation or operational models each need a new owner authorization.** The owner authorized this run on 2026-10-12; the [continuous-run receipt](07%20Audits%20and%20Handoffs/MEDALIST_CONTINUOUS_RUN_AUTHORIZATION_AND_SOURCE_RECEIPT.md) records the authorization, the dated publication ceiling (V15, ending at Score 61; no serial-only Score beyond it) and the structurally verified witnesses. [V01 deep reading and MD-FR-V01](02%20Sequential%20Readings/MEDALIST_V01_DEEP_READING.md) remain frozen and are not redone; the latest closed reading is [V15 / MD-FR-V15](02%20Sequential%20Readings/MEDALIST_V15_DEEP_READING.md), and the progress table below lists every closed unit. Fanbook coverage reconnaissance and audits are authorized only at a verified safe manga checkpoint; adaptation sources remain unauthorized. The historical single-operation V01 authorization is preserved in its own receipt.

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
  completed_sequential_readings: 15
  owner_review_state: APPROVED_REVISED_FOUNDATION_0_2
  sequential_analysis_lock: OPEN
  lock_reason: OWNER_APPROVED_FOUNDATION_AND_AUTHORIZED_V01
  lock_reason_current_run: OWNER_AUTHORIZED_CONTINUOUS_SEQUENTIAL_V02_TO_V15
  next_permitted_operation: "None within the 2026-10-12 authorization; a later source unit, a third fanbook, the adaptation or operational models each need a new owner authorization"
sequential_execution:
  mode: continuous_sequential
  unit_type: japanese_tankobon_volume
  authorized_start: V02
  terminal_boundary: V15
  terminal_boundary_basis: "Verified publication ceiling at 2026-10-12: V15 collects through Score 61; no serial-only Score beyond it"
  committed_high_water_mark: V15
  next_candidate_operation: AWAIT_NEW_AUTHORIZATION
  next_candidate_authorization: REQUIRES_NEW_OWNER_AUTHORIZATION
  confirmation_between_units: false
  run_state: completed
  prior_run: "single_operation V01, COMPLETED"
supplemental_execution:
  scheduled_units: [FB01, FB02]
  admission_positions_status: "FB01 admit_after V12, audited; FB02 admit_after V13, audited"
  authorized_start: "Coverage reconnaissance and conditional audit at a verified safe manga checkpoint"
  completed_paratext_audits: 2
  committed_high_water_mark: FB02
  run_state: COMPLETED_BOTH_SCHEDULED_UNITS
synthesis_execution:
  authorized_scope: "Provisional character, relationship, specialist and integrated syntheses at the locked boundary"
  run_state: PROVISIONAL_V1_RELEASED
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
| Structurally verified / admitted / narratively inspected / closed | 15 volume witnesses at container level / V01–V15 / all admitted images of V01–V15 / 15, latest MD-FR-V15 |
| Planned primary sequence | Japanese V01 onward, one authenticated volume per transaction; V02–V15 authorized as one continuous run with fourteen separately closed transactions |
| First-source route | V01 delivered CBZ integrity/component map verified, inspected and closed with original-image locators; printing unverified. V02–V15 delivered witnesses passed CRC, full image decode and hash checks at activation; none narratively inspected at that snapshot |
| Supplemental source positions | FB01 admitted after V12 and audited in full (MD-FR-FB01); FB02 admitted after V13 and audited in full (MD-FR-FB02; story guide Volumes 5–9, latest material presupposed Volumes 10–11, creator interviews of September 2025); two completed fanbook audits; a third fanbook is anticipated by the second and is not in the delivered set |
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
| V09 | 33–36 | [V09](02%20Sequential%20Readings/MEDALIST_V09_DEEP_READING.md) / MD-FR-V09 | 1.8 | Closed 2026-10-13; All-Japan Novice completed, protagonist fourth at 109.88; an elision of about eight months into the junior class and a federation designation; the arc of Volumes 5–9 ends; twenty claims advanced a version, 0027 new |
| V10 | 37–40, SP 5 | [V10](02%20Sequential%20Readings/MEDALIST_V10_DEEP_READING.md) / MD-FR-V10 | 1.9 | Closed 2026-10-13; no competition for the protagonist; the elided months filled, a junior strengthening camp, her coach's teacher identified, a boys' national title in a side story; twenty-one claims advanced a version, 0028 new as a hypothesis |
| V11 | 41–45, SP 6 | [V11](02%20Sequential%20Readings/MEDALIST_V11_DEEP_READING.md) / MD-FR-V11 | 1.10 | Closed 2026-10-13; first Junior Grand Prix event, protagonist fourth after a short program of 65.28, her free skate reported only; a medical trainer joins; a rival club's offer deferred; the rival leaves her club; twenty-three claims changed version, 0028 downgraded, 0029 new |
| V12 | 46–48, Exhibition 2 | [V12](02%20Sequential%20Readings/MEDALIST_V12_DEEP_READING.md) / MD-FR-V12 | 1.11 | Closed 2026-10-13; the rival's transfer, contract and first fall; the protagonist's series win reported and her place in the final; the All-Japan Junior short program in progress at her opening pose; twenty claims advanced a version, none new |
| V13 | 49–53 | [V13](02%20Sequential%20Readings/MEDALIST_V13_DEEP_READING.md) / MD-FR-V13 | 1.12 | Closed 2026-10-13; All-Japan Junior completed, the protagonist eliminated after the short program at 47.96, the rival champion at 227.64 and left by her coach; the pair's central silence broken; departure for the series final; twenty-four claims advanced a version, none new |
| V14 | 54–56, Exhibition 3, Short Program 7 | [V14](02%20Sequential%20Readings/MEDALIST_V14_DEEP_READING.md) / MD-FR-V14 | 1.13 | Closed 2026-10-13; the Junior Grand Prix Final opened, the protagonist first in its short program at 71.26 with one skater to come; the component mark explained; her program's story told; a different series' sample in the witness excluded; eighteen claims advanced a version, one new |
| V15 | 57–61 | [V15](02%20Sequential%20Readings/MEDALIST_V15_DEEP_READING.md) / MD-FR-V15 | 1.14 | Closed 2026-10-13; terminal unit of the run; the short program completed with the protagonist second by 0.33; the coach's childhood and his faith in his own sacrifice; the pupil's belief said to him by her; a promise in a stairwell; the free skate unopened; twenty-two claims advanced a version, one new |
| FB01 | supplement; own coverage through V12 | [FB01 audit](02%20Sequential%20Readings/MEDALIST_FB01_PARATEXT_AUDIT.md) / MD-FR-FB01 | 1.15 | Audited 2026-10-13 at the V15 checkpoint; 171 image occurrences inspected, adaptation pages excluded; creator-reported back story for the heroine's sister and mother, a second adult's regret about the coach as a boy, the stated origin of the adult coach; one conflict of degree with V15 kept; seven claims advanced a version, none new; the mainline boundary unchanged |
| FB02 | supplement; story guide V05–V09, latest material presupposed V10–V11 | [FB02 audit](02%20Sequential%20Readings/MEDALIST_FB02_PARATEXT_AUDIT.md) / MD-FR-FB02 | 1.16 | Audited 2026-10-13 at the V15 checkpoint; 203 image occurrences inspected; third-party and adaptation material excluded; the author's stated intent for the coach and position on sacrifice, creator-reported regimes and homes, complete result tables, a relative chronology; one conflict of colour with V15 kept; nine claims advanced a version, none new; the mainline boundary unchanged |

## Provisional syntheses (version 1, through MD-FR-FB02)

Released 2026-10-13. The series is ONGOING; every artifact is provisional through the verified boundary and reopens when a claim it depends on changes. The [readiness and role-gap audit](07%20Audits%20and%20Handoffs/MEDALIST_V15_SYNTHESIS_READINESS_AND_ROLE_GAP_AUDIT.md) pins the inputs and records what was promoted and what was not; the [release audit](07%20Audits%20and%20Handoffs/MEDALIST_V15_PROVISIONAL_SYNTHESIS_RELEASE_AUDIT.md) records production, review, contradictions and errata. No operational reconstruction model is promoted for any character.

| Artifact | Home | Status |
| --- | --- | --- |
| Monograph of the heroine | [Inori Yuitsuka](04%20Character%20and%20Relationship%20Synthesis/inori-yuitsuka/MEDALIST_INORI_YUITSUKA_PROVISIONAL_MONOGRAPH.md) | BOUNDED_PROVISIONAL |
| Monograph of the coach | [Tsukasa Akeuraji](04%20Character%20and%20Relationship%20Synthesis/tsukasa-akeuraji/MEDALIST_TSUKASA_AKEURAJI_PROVISIONAL_MONOGRAPH.md) | BOUNDED_PROVISIONAL |
| Relationship study | [Coach and pupil](04%20Character%20and%20Relationship%20Synthesis/MEDALIST_COACH_AND_PUPIL_RELATIONSHIP_STUDY.md) | BOUNDED_PROVISIONAL |
| Supporting study | [Hikaru Kamisaki and Yodaka Jun](04%20Character%20and%20Relationship%20Synthesis/hikaru-kamisaki/MEDALIST_HIKARU_KAMISAKI_AND_YODAKA_JUN_SUPPORTING_STUDY.md) | BOUNDED_PROVISIONAL, through V13 with supplements |
| Specialist | [Skating, competition and expression](05%20Specialist%20Synthesis/MEDALIST_SKATING_COMPETITION_AND_EXPRESSION_SPECIALIST.md) | PROVISIONAL; in-story rules only |
| Specialist | [Manga form and performance](05%20Specialist%20Synthesis/MEDALIST_MANGA_FORM_AND_PERFORMANCE_SPECIALIST.md) | PROVISIONAL; facing-page geometry largely unverified |
| Specialist | [Adult doctrines, institutions and burden](05%20Specialist%20Synthesis/MEDALIST_ADULT_DOCTRINES_INSTITUTIONS_AND_BURDEN_SPECIALIST.md) | PROVISIONAL |
| Integrated | [Integrated provisional synthesis through Volume 15](05%20Specialist%20Synthesis/MEDALIST_INTEGRATED_PROVISIONAL_SYNTHESIS_THROUGH_V15.md) | PROVISIONAL checkpoint with a map of competing readings |

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

2026-10-13, version 1.3: V09 closed. All 203 image occurrences inspected; Scores 33–36 read; seven ledgers reconciled to version 1.8; twenty claims advanced with recorded revisions, six preserved and one registered; MD-FR-V09 frozen. The mainline stands about eight months after the All-Japan Novice, in which the protagonist placed fourth, with her entry into the junior class and her designation by the federation. No infrastructure added; the elision is carried as a chronology row with its unknowns listed, and one first-pass misidentification of a figure was corrected from captions and recorded in the reading.

2026-10-13, version 1.4: V10 closed. All 203 images inspected; Scores 37–40 and Short Program 5 read; seven ledgers reconciled to version 1.9; twenty-one claims advanced with recorded revisions, six preserved and one registered as a hypothesis; MD-FR-V10 frozen. The mainline stands after a junior strengthening camp and before the protagonist's first Junior Grand Prix event. No infrastructure added; adult readings of a child are carried as attributed appraisals and as a low-confidence hypothesis and are not written into character projections, and a misattributed testimony was corrected from a caption before closure.

2026-10-13, version 1.5: V11 closed. All 203 images inspected; Scores 41–45 and Short Program 6 read; seven ledgers reconciled to version 1.10, the next step of the per-volume sequence; twenty-three claims changed version with recorded revisions, one of them a downgrade, five preserved and one registered; MD-FR-V11 frozen. The mainline stands after the protagonist's first Junior Grand Prix event. No infrastructure added; a performance known only by a third party's report is carried in the skating ledger's performance table with that label, and one inference from juxtaposition is labelled as such wherever it is used.

2026-10-13, version 1.6: V12 closed. All 171 images inspected; Scores 46–48 and a second Exhibition read; seven ledgers reconciled to version 1.11; twenty claims advanced with recorded revisions, nine preserved and none registered; MD-FR-V12 frozen. The mainline stands inside the All-Japan Junior short program at the protagonist's opening pose. No infrastructure added; a contested self-account is carried as two attributed statements with a bounded projection, competitions known only by report are labelled, and a parody chapter is recorded in the visual ledger alone.

2026-10-13, version 1.7: V13 closed. All 203 image occurrences of the EPUB witness inspected; Scores 49–53 read; seven ledgers reconciled to version 1.12; twenty-four claims advanced with recorded revisions, five preserved and none registered; MD-FR-V13 frozen. The mainline stands a week before the Junior Grand Prix Final, after the All-Japan Junior. No infrastructure added; one conclusion was held until a page stated it, creator pages that state character histories are used as creator statements, and a verbal motif recurring since Volume 4 is registered in the visual ledger.

2026-10-13, version 1.8: V14 closed. Of 256 image occurrences in the EPUB witness, 171 admitted and inspected and 85 excluded as a different series' advertisement and sample; Scores 54–56, one parody Exhibition and Short Program 7 read; seven ledgers reconciled to version 1.13; eighteen claims advanced with recorded revisions, eleven preserved and one registered; MD-FR-V14 frozen. The mainline stands inside the short program of the Junior Grand Prix Final. No infrastructure added; a result stated only in a next-volume advertisement was held out of the evidence, a side chapter told in a frame is used at a side chapter's weight, and a figure of the double at the water's surface is registered as a motif.

2026-10-13, version 1.9: V15 closed, the terminal unit of the continuous run. All 221 image occurrences of the EPUB witness inspected; Scores 57–61 read; seven ledgers reconciled to version 1.14; twenty-two claims advanced with recorded revisions, eight preserved and one registered; MD-FR-V15 frozen. The mainline stands in the warm-up before the free skate of the Junior Grand Prix Final, at the publication ceiling fixed on 2026-10-12. Two judgements made at V13 and carried at V14 were withdrawn by recorded revision on this volume's evidence; a preview page in the V14 witness was found to be contradicted by story pages; no infrastructure was added, and the figure of sorting by black and white is registered as a motif. The sequential phase of the run is complete; fanbook coverage reconnaissance and the provisional syntheses remain.

2026-10-13, version 1.10: Official Fanbook 01 admitted and audited at the V15 checkpoint. Coverage bounded at Volume 12 by three statements on its own pages and by complete inspection of 171 image occurrences; every component assigned a source layer; animation pages excluded. Seven ledgers reconciled to version 1.15, two with no material change; seven claims advanced with recorded revisions; one erratum entered in the character ledger; MD-FR-FB01 frozen. The mainline boundary is unchanged at V15 and Score 61. Official Fanbook 02 is authenticated and its coverage verified; its audit is next.

2026-10-13, version 1.11: Official Fanbook 02 admitted and audited at the V15 checkpoint. Coverage bounded by its own headings and by complete inspection of 203 image occurrences; no event of Volume 14 or 15 found; every component assigned a source layer; a third-party collaboration, animation information and adaptation talk excluded. Seven ledgers reconciled to version 1.16, one with no material change; nine claims advanced with recorded revisions; MD-FR-FB02 frozen. An author's statement of intended direction for one character is recorded as intent and adopted as no prediction. Both scheduled supplements are closed; the mainline boundary is unchanged at V15 and Score 61. The synthesis-readiness and role-gap audit is next.

2026-10-13, version 1.12: provisional syntheses released at the combined boundary. A readiness and role-gap audit pinned the inputs and promoted eight artifacts: two monographs, a relationship study, one bounded supporting study, three specialist syntheses and an integrated synthesis with a map of competing readings. Operational reconstruction models were judged to have insufficient evidence and none is promoted. Cross-specialist review found no incompatible conclusions and exposed seven small errors or imprecisions in the ledgers, entered as appended errata in four ledgers (version 1.17) without altering any frozen reading, earlier row or claim version. The continuous run is complete. The series is ONGOING; the mainline boundary is unchanged at V15 and Score 61; all syntheses are provisional through it.

## Higher-level governing controls

- [Repository authority/routing](../../governance/CHATGPT_AUTHORITY_AND_ROUTING.md), [authority state](../../governance/AUTHORITY_STATE.yaml) and [scope](../../governance/AUTHORITY_SCOPE.json).
- [Initiation policy](../../governance/source-policies/MANGA_ANIME_PROJECT_INITIATION_AND_ARCHITECTURE_POLICY.md) and [authority/supersession](../../governance/source-policies/ARCHIVE_AUTHORITY_AND_SUPERSESSION_POLICY.md).
- [Reasoning routing](../../governance/source-policies/MANGA_ANIME_REASONING_AND_MODEL_ROUTING_POLICY.md), [capabilities](../../governance/source-policies/MANGA_ANIME_EXECUTION_TOPOLOGY_AND_CAPABILITY_ROUTING_POLICY.md), [long-series protocol](../../governance/source-policies/MANGA_ANIME_LONG_SERIES_HYBRID_EXECUTION_PROTOCOL.md).
- [Handoff contract](../../governance/source-policies/MANGA_ANIME_ANALYTICAL_HANDOFF_AND_INTEGRATION_CONTRACT.md), [continuation](../../governance/source-policies/MANGA_ANIME_SEQUENTIAL_EXECUTION_SCOPE_AND_CONTINUATION_POLICY.md) and [episode evidence](../../governance/source-policies/MANGA_ANIME_EPISODE_BUNDLE_SPECIFICATION.md).
- [Integration checklist](../../governance/policies/CHANGE_INTEGRATION_CHECKLIST.md), [branch lifecycle](../../governance/policies/BRANCH_LIFECYCLE.md), [housekeeping ownership](../../governance/policies/AUTOMATED_GLOBAL_INDEX_MAINTENANCE.md) and [change obligations](../../governance/repository-controls/change-obligations.json).
