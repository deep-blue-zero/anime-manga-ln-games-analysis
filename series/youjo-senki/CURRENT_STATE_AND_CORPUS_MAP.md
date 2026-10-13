---
series: YOUJO_SENKI
artifact_type: corpus_map
scope: V01-V14 mature V2 synthesis + active Character Modeling and Reconstruction layer
generation: V2_CMR
version: '2.9'
status: active_provisional
source_boundary: Original Japanese light novels Volumes 01-14
current_entrypoint: CURRENT_STATE_AND_CORPUS_MAP.md
analysis_root: 17UvtZCM9QBQdFtqKjDsebZfQXsuB2idH
v2_analysis_root: 1q1xEv83Ld8KGENT_cZTN3OhAzjoFqzzs
primary_source_root: 1s8Ido1uUbAyR-lXstTyOVfoeHaUDop-g
cmr_root: 1z-U_tluPeOwMuRIVzEbQOOxrI1cYlMK4
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
updated: '2026-10-13'
---

# YOUJO SENKI — CURRENT STATE AND CORPUS MAP

## 1. Current state

*Youjo Senki* uses this Git series root as its current analytical entrypoint. The preserved Drive routes below identify the original analytical provenance, primary sources, and bulk CMR evidence:

- **Analytical root:** `17UvtZCM9QBQdFtqKjDsebZfQXsuB2idH`
- **Mature V2 analysis:** `V2 Analysis` — `1q1xEv83Ld8KGENT_cZTN3OhAzjoFqzzs`
- **Primary-source root:** `1s8Ido1uUbAyR-lXstTyOVfoeHaUDop-g`
- **Character Modeling and Reconstruction root:** `1z-U_tluPeOwMuRIVzEbQOOxrI1cYlMK4`

The primary-source boundary is the original Japanese light novels **Volumes 01-14**. The source folder contains all fourteen EPUBs plus `audit_manifest.json`; thirteen are conformant EPUB containers and V02 has a known mimetype-order/compression irregularity while otherwise passing archive/container integrity checks.

The mature V2 literary/full-series synthesis was completed on 2026-08-11 and is the current series-level analytical authority. Documents 00-12 are now present in the canonical `V2 Analysis` folder; Documents 00-11 were migrated with exact byte/hash verification and the user subsequently supplied the missing original `12_JAPANESE_ENGLISH_TRANSLATION_AUDIT_LEDGER.md`, now synced as Drive `1mQno_ayho-R3jacL374LrNamAe_Sbkf0`. The post-synthesis CMR layer remains `active_provisional` derived infrastructure and does **not** supersede, rename, renumber, or silently mutate V2.

## 2. Authority state

### Mature literary/full-series authority — `V2 Analysis`

The V2 core is canonical for mature interpretation through Volume 14.

Exact migrated files:

- `00_README_AND_CORPUS_MAP.md` — frozen core-corpus snapshot / original V2 guide;
- `01_SERIES_ARCHITECTURE_AND_VOLUME_PROGRESSION.md` — chronology and developmental architecture;
- `02_TANYA_DEGURECHAFF_CHARACTER_DEEP_DIVE.md` — primary mature Tanya character authority;
- `03_IMPERIAL_PROFESSIONALS_RELATIONSHIPS_AND_COMMAND_CULTURE.md`;
- `04_COUNTERPERSPECTIVES_ENEMIES_ALLIES_AND_PARALLEL_PROFESSIONALS.md`;
- `05_POLITICS_INSTITUTIONS_STATECRAFT_AND_WAR_TERMINATION.md`;
- `06_STRATEGY_DOCTRINE_LOGISTICS_AND_ORGANIZATIONAL_LEARNING.md`;
- `07_ETHICS_LAW_AUTONOMY_AND_VIOLENCE.md`;
- `08_FAITH_BEING_X_MAGIC_TECHNOLOGY_AND_BODILY_AUTHORSHIP.md`;
- `09_NARRATION_LANGUAGE_HISTORIOGRAPHY_GENRE_AND_MOTIFS.md`;
- `10_COMPARATIVE_REFERENCE_AND_OPEN_QUESTIONS.md` — principal compact mature cross-series/comparative reference;
- `11_VOLUME_BY_VOLUME_EVIDENCE_LEDGER.md` — chronological evidentiary spine.

Also present:

- `FRAMEWORK_MANIFEST.md` — recovered provenance for the original analytical method and synthesis architecture hashes;
- `V2_MIGRATION_AUDIT.md` — exact migration inventory, Drive IDs, original hashes, and unresolved byte-recovery gaps.

### Restored final translation-audit artifact

The user supplied the missing original:

- `12_JAPANESE_ENGLISH_TRANSLATION_AUDIT_LEDGER.md` — Drive `1mQno_ayho-R3jacL374LrNamAe_Sbkf0`, covering official English comparison through Volume 13 while retaining Volume 14 as Japanese-primary only.

This closes the principal analytical-document migration gap. The final package's updated README/manifest copies, governing framework documents, delivery manifest, and checksum files remain provenance items whose exact final byte streams have not all been separately restored; do not recreate them from summaries merely for symmetry. See `V2_MIGRATION_AUDIT.md`.

The translation-audit corrections remain part of V2 provenance:

- V9 `低血圧` = **low blood pressure**;
- V10 deadline = about **six months**, not one year;
- V11 Chapter I begins **September 10, 1927**, not September 25;
- no official English Volume 14 comparison was included in that appendix.

Do not read the exact migrated `V2 Analysis/00_README_AND_CORPUS_MAP.md` statement that Document 12 was still optional/unproduced as the final project state. That file is intentionally preserved byte-exact from the core-corpus snapshot immediately before the appendix was produced. This root `CURRENT_STATE_AND_CORPUS_MAP.md` controls current state.

## 3. Authority order by question type

### Mature literary, thematic, political, military, ethical, or character interpretation

1. `CURRENT_STATE_AND_CORPUS_MAP.md` for authority/current-state resolution;
2. relevant `V2 Analysis` specialist document;
3. `10_COMPARATIVE_REFERENCE_AND_OPEN_QUESTIONS.md` for compact mature cross-series reference where appropriate;
4. `11_VOLUME_BY_VOLUME_EVIDENCE_LEDGER.md` for chronological/source-trail support;
5. original Japanese V01-V14 source for exact verification.

### Translation or exact Japanese wording

1. original Japanese V01-V14 primary source;
2. official English counterpart when present;
3. V2 translation-audit provenance / Document 09 where relevant;
4. do not invent missing Document-12 text from its summary.

### Character reconstruction / simulation

1. original Japanese V01-V14 primary source;
2. CMR-0 exact locator / source-member infrastructure;
3. mature V2 analytical corpus;
4. CMR character models and relationship registers;
5. generated simulations.

Generated simulations are never canonical evidence.

## 4. Mature V2 architecture

The V2 corpus intentionally uses a flat numbered multi-document architecture rather than being reorganized into a new generic folder tree. Each document has one primary analytical responsibility and cross-references the others.

Key retrieval homes:

- **series development / volume progression:** Document 01;
- **Tanya:** Document 02;
- **Imperial professional network / command culture:** Document 03;
- **non-Imperial counterperspectives:** Document 04;
- **politics / institutions / war termination:** Document 05;
- **strategy / doctrine / logistics / organizational learning:** Document 06;
- **ethics / law / autonomy / violence:** Document 07;
- **faith / Being X / magic / technology / embodiment:** Document 08;
- **narration / Japanese voice / historiography / genre / motifs:** Document 09;
- **comparative matrices / contradiction audit / open questions:** Document 10;
- **volume-level evidence spine:** Document 11;
- **JP/EN translation audit:** Document 12, restored and canonical in `V2 Analysis` as Drive `1mQno_ayho-R3jacL374LrNamAe_Sbkf0`.

## 5. Active CMR architecture

The Git-readable operational entrypoint is [CMR/README.md](CMR/README.md), with a [29-package model/readiness/source index](CMR/YOUJO_SENKI_MODEL_AND_SOURCE_NAVIGATION.md). All 1,200 Tanya candidates through V14 are closed, yielding 814 textual diagnostics and 44 conditional rule families without changing the frozen V12 prefixes. All 29 models or recognition profiles and their original independent QA are present. Source support and new-scene prediction remain separate: seven actual held-out continuations are partial, synthetic applications are nonempirical, and repairs retain original judgments. Current bounded successor regressions and the separate ensemble release are complete with limits; original failures and partials remain versioned. The CMR layer remains `active_provisional`; it preserves the mature V2 corpus. Method promotion and former-Drive authority pointers await verified main integration.

The Drive folder architecture below is historical analytical provenance and the current primary/bulk evidence map. Git `CMR/Models`, `CMR/Relations` and `CMR/QA` own the emitted interpretive derivatives.

### `06 Character Modeling and Reconstruction`
Drive: `1z-U_tluPeOwMuRIVzEbQOOxrI1cYlMK4`

This is a post-synthesis, source-grounded character reconstruction layer.

#### `00 Frameworks and Methods`
Drive: `1Ul_BbZkw9UkSOrDik3hmWVfcK84WWGvW`

Governing home for:

- `YOUJO_SENKI_CHARACTER_MODELING_REFERENCE_METHOD.md` — Drive `16tMcTb0rZZ7U3gjidf6bzJ-TravNQcCh`.

#### `01 Evidence and Locators`
Drive: `1aDiFqWjWHZ53xX-lBvjMLfA6eN89Z7SZ`

Current canonical CMR source/evidence infrastructure:

- `YOUJO_SENKI_CMR_SOURCE_EXTRACTION_MANIFEST.md` - Drive `1zWogK3vzZ0Tj1_92r3NaESIj1NzV1Biv`;
- `YOUJO_SENKI_CMR_SOURCE_LOCATOR_INDEX.tsv` - Drive `140ow12czVj4J8Q_JR44MSWI98LUxj3uk`; 63,812 deterministic source-textual-block locators;
- `YOUJO_SENKI_CMR_SOURCE_MEMBER_INDEX.tsv` - Drive `1GlDNvT5spgIQk5VaUU5S2Qsk5dF174hR`; 608 OPF-spine-member routes;
- `YOUJO_SENKI_CMR_SOURCE_EXTRACTION_SCRIPT.py` - Drive `1l8ok-FT2RMmDl-qeXJnVaj8hrS7pzKeu`; reproducible CMR-0 extractor;
- `YOUJO_SENKI_CHARACTER_ALIAS_MAP.tsv` - Drive `1C95SxSuba7Fr9diTMyc1N8q58TbzxsLs`; canonical CMR-1 controlled retrieval aliases;
- `YOUJO_SENKI_CHARACTER_RECONSTRUCTION_READINESS_METRICS.tsv` - Drive `13pEqvLZiv8Pc0SjvbsWSYpk_G4VMKZ0b`; quantitative CMR-1 retrieval proxies;
- `YOUJO_SENKI_CMR1_READINESS_AUDIT_SCRIPT.py` - Drive `1keRBa1MAecQmFefKgmnUMroSeOarf1B1`; reproducible CMR-1 support;
- `YOUJO_SENKI_CHARACTER_RECONSTRUCTION_READINESS_AUDIT.md` - Drive `1LYRzJS4AL6jHAmIAjkaOC-HIWQQdBp51`; original first-audit readiness and CMR-2 handoff; current coverage is the separately versioned Git re-audit/supplement above.
- `YOUJO_SENKI_TANYA_CMR2_CANDIDATE_SCENE_POOL.tsv` - Drive `1LRcSX-k739E4O4xQ2ImZnawzx6IylARo`; 1,200 broad-recall Tanya candidate centers across V01-V14; SHA-256 `8344b6196565645cfe373d3468fa4f3c618d1c4d3afb363667c64a073a5c469a`.
- `YOUJO_SENKI_TANYA_CMR2_CANDIDATE_RETRIEVAL_SCRIPT.py` - Drive `1GZMXU-ulPFfKFKGrjl6GjXUYtqnorwg5`; reproducible CMR-2A retrieval support.
- `YOUJO_SENKI_TANYA_CMR2_CANDIDATE_RETRIEVAL_MANIFEST.md` - Drive `1v3oLyOSuwD9WgZX_TvAPekRo20g4m_Rh`; CMR-2A completion/limitations and CMR-2B handoff.
- `YOUJO_SENKI_TANYA_CMR2_ADJUDICATION_LEDGER.tsv` - Drive `1Eoz8hpJMoeksACmQgvJXntTEcYM-w20g`; current V01-V14 **1,200/1,200** closed candidate ledger; SHA-256 `47614760d6b14118bb507a086270d316af8c8a881ec10955ca362ebbccb526eb`. Exact frozen V12 copy: Drive `1aU4ZarOXLUnOV082bk4BEIxAe7NwwkyA`, original SHA-256 `4391f1042668cdc2148f6e09b975317cb5ab9d20c9e0e1679d491c450a8e6fa0`.
- `YOUJO_SENKI_TANYA_CMR2_DIAGNOSTIC_EVIDENCE_INDEX.tsv` - Drive `1i1Ov7u5yGciH55j-04LxIR4CWck61-KH`; current V01-V14 **814 textual diagnostics**; SHA-256 `2b5fbc8caa711ee2c71a028a093b877df8b1335207352528cf9043d2349dc387`. Exact frozen V12 copy: Drive `1v67_7wmkiYnXE1LJ_okzpR9tNk8ANws9`, original SHA-256 `1240953f6174375e64ddf1eb44af83954984a438c4b2fbc5d8869dabcf42ce68`.
- `YOUJO_SENKI_TANYA_CMR2B_ADJUDICATION_SCRIPT.py` - Drive `1whdImFw-vUblagWfpiqEmY58hT1vd3LZ`; reproducible cumulative V01-V12 build with frozen V01-V11-prefix preservation guards and validation; SHA-256 `23078662fed83e7aa8ba7c5e59fe9e0946a58ab75abab61a7de0a326e5e6909f`.
- `YOUJO_SENKI_TANYA_CMR2B_ADJUDICATION_MANIFEST.md` - Drive `1JxHeRuCRltCmQsyIs2nQruzewx1U8Bmd`; v2.1 cumulative V01-V12 authority, preservation controls, limitations, and V13 handoff.

Completed evidence-facing continuation:

- current cumulative Tanya ledger/index close V01-V14 with immutable V12 copies and exact prefix guards;
- current successor script: Drive `1p4PpUbQc80YJZLk2uXme_68cuSsEpIiA`; the original V12 script and manifest above remain historical;
- [source append disposition](CMR/Provenance/YOUJO_SENKI_CMR_SOURCE_APPEND_DISPOSITION.jsonl) records twelve preserved/new/advanced evidence objects and complete readbacks;
- [44-family rule register](CMR/Diagnostics/TANYA_OPERATIONAL_RULE_REGISTER.md) includes speech acts, everyday/material contrasts, counterevidence and inference ceilings.

#### `02 Character Models`
Drive: `1AMNfngVWTSm_4O0XadlJjHWjR8hMw21X`

Historical Drive scaffold. Current [29 completed Git packages](CMR/YOUJO_SENKI_MODEL_AND_SOURCE_NAVIGATION.md) include the Tanya pilot, three transfer priorities and all further subjects admitted by focused readiness audits.

#### `03 Relationship Registers`
Drive: `1TomsYaw1BmQMRp-JuMils2PeHzl375uo`

Historical Drive scaffold. Current [Git directional register](CMR/Relations/YOUJO_SENKI_DIRECTED_RELATIONSHIP_REGISTER.md) contains 77 separately sourced directed episodes and explicit unknown core cells.

#### `04 QA and Simulation`
Drive: `1dPqF3RjqawccCi8LA59QVMXsp2KDvH63`

Historical Drive scaffold. Current Git QA routes are linked from the [model index](CMR/YOUJO_SENKI_MODEL_AND_SOURCE_NAVIGATION.md#current-qa-qualifications); original partials, failures and nonblind regressions are preserved separately.

## 6. CMR governing principle

The CMR layer separates:

1. private cognition;
2. observable behavior;
3. public speech/presentation;
4. external interpretation;
5. institutional consequence.

This is mandatory for Tanya because her private self-preservation and institutional reasoning frequently produce outward behavior that other characters misread as zeal, courage, ideological devotion, or extraordinary ambition.

The simulator must therefore model the causal chain rather than a single flattened personality label.

## 7. Current modeling status

### Method

- Controlled Git method candidate: [YOUJO_SENKI_CHARACTER_MODELING_REFERENCE_METHOD.md](CMR/Methods/YOUJO_SENKI_CHARACTER_MODELING_REFERENCE_METHOD.md); its complete v1.1 substantive body is preserved from verified Drive bytes. The Git preface declares responsibilities and the pending promotion boundary. The former Drive object remains an explicitly identified predecessor rather than an unlabeled competing current copy.
- CMR method: **v1.1 established, active provisional**. The v1.1 refinement formalizes speech reconstruction as `private appraisal -> communicative objective -> speech act -> relationship/role constraint -> register -> surface wording`, adds speech-specific diagnostic fields, mandatory low-stakes speech oversampling, no-shared-hierarchy professional-peer handling, character-specific speech hazards, and Document 12 as the translation-sensitive lexical warning layer.

### Source extraction

- Japanese V01-V14 source set: **present**;
- audit manifest: **present**;
- deterministic source-member / paragraph-style locator layer: **CMR-0 complete and canonical**;
- source hash verification: **14/14 canonical EPUB hashes matched `audit_manifest.json`**;
- OPF spine members indexed: **608**;
- text-bearing spine members: **222**;
- deterministic source textual-block locators: **63,812**;
- normalized Japanese characters indexed: **2,974,249**;
- member extraction errors: **0**;
- full rerun determinism: locator/member index hashes reproduced byte-identically.

CMR-0 canonical artifacts are routed through `YOUJO_SENKI_CMR_SOURCE_EXTRACTION_MANIFEST.md` (`1zWogK3vzZ0Tj1_92r3NaESIj1NzV1Biv`). The 52.9 MB locator index is Drive `140ow12czVj4J8Q_JR44MSWI98LUxj3uk`; its SHA-256 is `c84fa4c8e0251730887b51913a8f32ea68c39be68ff4adae8d995d49292f5cfe`.

### Readiness audit - CMR-1 complete

CMR-1 completed a first production reconstruction-readiness pass over 20 recurring characters using the deterministic CMR-0 locator layer, a controlled alias map, reproducible retrieval metrics, contextual source review, and the mature V2 character/relationship syntheses.

Historical initial twenty-subject readiness classes:

- `FULL_SPECTRUM`: **Tanya Degurechaff** (`HIGH`); **Erich von Lergen** (`MODERATE_HIGH`).
- high-confidence `DOMAIN_BOUNDED`: **Visha, Hans von Zettour, Matheus Johann Weiss, Grantz, Uger, Kurt von Rudersdorf, Drake, Mary Sue, Calandro, Loria**.
- narrower `DOMAIN_BOUNDED`: **Romel, Conrad, de Lugo, Anson Sioux, Schugel**.
- `RECOGNITION_PROFILE`: **Meybert, Tospan, Josef**.

No selected CMR-1 audit candidate was assigned `INSUFFICIENT`. Characters not included in this first audit remain **not yet audited**, not automatically insufficient.

Important scope controls:

- quantitative alias/window metrics are retrieval proxies, not direct speaker counts;
- `FULL_SPECTRUM` does not authorize invention in unsupported private/domestic domains;
- Mary Sue requires a developmental/state-conditioned model rather than one timeless voice;
- Josef remains recognition-only because the available source presentation is heavily mediated by satire, propaganda diction, reports, and other observers;
- Visha is a promotion candidate if later targeted low-stakes/non-Tanya sampling broadens her support.

The initial roster is historical. The [current re-audit](CMR/Provenance/YOUJO_SENKI_CHARACTER_READINESS_REAUDIT.md) and [supplement](CMR/Provenance/YOUJO_SENKI_SUPPLEMENTARY_CHARACTER_READINESS.md) admit 29 packages: 2 full-spectrum with limits, 23 domain-bounded and 4 recognition profiles. Meybert is narrowly promoted; nine additional supported subjects are included. Unexamined figures remain not yet audited. Tanya was constructed first and independently repaired/accepted before transfer authoring.

### Tanya evidence pilot - CMR-2 closed through V14

The [interpretive navigation](CMR/Diagnostics/YOUJO_SENKI_TANYA_DIAGNOSTIC_NAVIGATION.md) exposes all **814 textual diagnostics in five Git JSONL slices**. V13 adds 82 and V14 adds 56, including 26 missed high-salience cases. All 1,200 candidates close as 711 RETAIN, 433 MERGE and 56 REJECT. The [closure audit](CMR/Provenance/YOUJO_SENKI_TANYA_CMR2_V14_CLOSURE_AUDIT.md) records coverage, source certainty and preservation; the 44-family non-destructive consolidation preserves 815 typed crosswalk rows including a separate collective image witness. Historical confidence is not silently converted to speaker/focalizer certainty. The inherited V01-V12 route validation is not a claim to newly reread every legacy scene.

- **CMR-2A candidate retrieval: COMPLETE.** The deterministic broad-recall pass reduced the 63,812-row CMR-0 source index to **1,200** Tanya candidate centers distributed across V01-V14.
- Candidate-pool SHA-256: `8344b6196565645cfe373d3468fa4f3c618d1c4d3afb363667c64a073a5c469a`.
- Candidate priorities: 388 `HIGH`, 762 `MEDIUM`, 50 `LOW`. Priority means adjudication usefulness, not evidentiary confidence.
- Heuristic category/speech/relationship tags are retrieval cues only; they must not be promoted directly into claims.
- **Historical V12 CMR-2B checkpoint (preserved provenance):** Volumes 01-12 are complete: **1,045/1,045** cumulative candidates adjudicated. V12 added 44 `RETAIN`, 12 `MERGE`, and 5 `REJECT` dispositions while preserving every V01-V11 row and identifier unchanged.
- The cumulative V01-V12 diagnostic index contains **676** source-adjudicated states. V12 added **60 states: 53 `HIGH`, 7 `MODERATE`**. V12 materially strengthens historical-glory versus civilian-legacy preferences, patriotism modeled without projection, unfamiliar-institution fallibility, career ambition under order constraints, context override of combat habits, familiar-unit humor and material reciprocity, enemy competence/aesthetic appreciation, developmental mentorship, audience-conditioned violent rhetoric, bounded tactical enjoyment, body/age observer effects, Tanya-Zettour modeling, Grantz advocacy and recorded dissent, retreat/casualty-reduction command logic, dynamic enemy learning, Uger peer-professional interaction, civilian-normalcy aspirations, subordinate-welfare advocacy, resource bargaining, and veteran intuition under uncertainty.
- **Historical planning snapshot, superseded by the V14 closure above:** V13-V14 remain pending. The evidence pack remains `active_provisional`; the raw 676-state count exceeds the eventual 250-350 target by design, and all-volume deduplication/counterevidence review must wait until V14. V01 IDs `YS-TAN-CMR2-V01-001` through `055`, V02 IDs `YS-TAN-CMR2-V02-001` through `054`, V03 IDs `YS-TAN-CMR2-V03-001` through `046`, V04 IDs `YS-TAN-CMR2-V04-001` through `055`, V05 IDs `YS-TAN-CMR2-V05-001` through `059`, V06 IDs `YS-TAN-CMR2-V06-001` through `041`, V07 IDs `YS-TAN-CMR2-V07-001` through `053`, V08 IDs `YS-TAN-CMR2-V08-001` through `045`, V09 IDs `YS-TAN-CMR2-V09-001` through `069`, V10 IDs `YS-TAN-CMR2-V10-001` through `071`, V11 IDs `YS-TAN-CMR2-V11-001` through `068`, and V12 IDs `YS-TAN-CMR2-V12-001` through `060` are stable provenance identifiers. V12 does not close the attraction/orientation question; the V05 former-male-psyche/current-female-body dilemma remains OPEN / underdetermined and does not license a modern categorical gender-identity label.

### Character models

All **29** admitted source-limited models/profiles are authored with **418 anchored claims**: [current package and source navigation](CMR/YOUJO_SENKI_MODEL_AND_SOURCE_NAVIGATION.md). Full-spectrum does not authorize unsupported domestic or private domains; recognition is not full simulation.

### Relationship matrix

The [77 directed episodes/register](CMR/Relations/YOUJO_SENKI_DIRECTED_RELATIONSHIP_REGISTER.md) include the core Tanya/Visha/Weiss/Grantz/Lergen/Zettour/Uger network and supported external counterparts. The 42 ordered core cells contain 24 direct, 3 partial and 15 not yet audited in this packet; absence of a witness is not an absent relationship.

### QA

All 29 original independent assessments are sealed. Seven actual frozen-before-revelation continuations remain partial; no novel-wide blindness or calibrated forecast accuracy is claimed. Tanya's first failure and all metadata/pipeline issues remain versioned alongside nonblind successor checks. The [four-pipeline regression](CMR/QA/FOUR_SPEECH_ACT_PIPELINE_REGRESSION_QA.md), [six-specialist process regression](CMR/QA/SIX_SPECIALIST_PIPELINE_REGRESSION_QA.md) and [separately qualified current ensemble release](CMR/QA/YOUJO_SENKI_ENSEMBLE_CONSISTENCY_QA.md) are complete with limits. The [current ensemble ledger](CMR/QA/YOUJO_SENKI_ENSEMBLE_CONSISTENCY_QA_CASES.jsonl) and [application repair trace](CMR/QA/YOUJO_SENKI_ENSEMBLE_APPLICATION_REPAIR_TRACE.json) retain the original failed 76-application suite and 17 separate application repairs; no original failure or source partial is rescored. Generated wording never enters the evidence corpus. Model and original-QA promotion fields remain construction/evaluation snapshots; separately verified release/promotion receipts govern actual publication/main/native-Drive authority, which remains pending.

## 8. Binding next steps

1. **CMR-0 - COMPLETE:** deterministic source extraction and exact-locator build across V01-V14.
2. **CMR-1 - COMPLETE:** controlled alias map + first production reconstruction-readiness audit for the recurring cast.
3. **CMR-2A - COMPLETE:** 1,200-candidate broad-recall Tanya scene pool across V01-V14.
4. **CMR-2B - COMPLETE:** all 1,200 candidates through V14; 814 textual diagnostics; frozen V12 prefixes and append provenance preserved; 44 conditional families with full non-destructive crosswalk.
5. **CMR-3 - COMPLETE:** Tanya source-limited reconstruction model, 44 claims, separate written-voice controls.
6. **CMR-4 - COMPLETE WITH LIMITS:** original independent failure/two partial continuations retained; repaired successor accepted by nonblind regression.
7. **CMR-5 - COMPLETE WITH LIMITS:** Visha, Lergen, Zettour and all further admitted subjects; bounded successors are tracked separately.
8. **CMR-6 - RELATIONSHIPS / CURRENT ENSEMBLE COMPLETE WITH LIMITS:** directed register and source-backed episode controls; exact-head publication, owner-governed main integration and former-Drive authority pointer cutover remain pending.

## 9. Recommended retrieval routes

For a mature literary/theme question:

> `CURRENT_STATE_AND_CORPUS_MAP.md` → `V2 Analysis` relevant specialist document → Document 11 if chronology/evidence trail is needed → Japanese source for exact verification

For a compact mature comparison:

> `CURRENT_STATE_AND_CORPUS_MAP.md` → `V2 Analysis/10_COMPARATIVE_REFERENCE_AND_OPEN_QUESTIONS.md` → relevant specialist document when compression needs expansion

For a character-reconstruction question:

> `CURRENT_STATE_AND_CORPUS_MAP.md` → CMR-0 source locator/member index → mature V2 character/relationship context → CMR diagnostic/model layer → exact Japanese source

For generated hypothetical scenarios:

> scenario state → retrieve canonical analogues → attention/private appraisal with explicit access limits → communicative objective → likely decision/action → speech act → relationship/role constraint → register → surface wording → label inference boundaries

## 10. Do not do

- Do not treat CMR as a new full-series reread.
- Do not create a parallel V3 corpus because a new chat or modeling phase exists.
- Do not reorganize or rewrite the migrated V2 core merely to conform to a newer global folder skeleton.
- Do not silently reconstruct missing final-package artifacts from summaries.
- Do not use generated dialogue as evidence.
- Do not globalize relationship-specific register.
- Do not infer ordinary preferences from isolated wartime necessities.
- Do not project later Tanya backward into early career states.
- Do not fill gaps in domain-bounded characters with generic military-fiction behavior.
