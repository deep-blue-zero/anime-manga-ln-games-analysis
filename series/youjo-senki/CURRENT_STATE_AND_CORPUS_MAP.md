---
series: YOUJO_SENKI
artifact_type: corpus_map
scope: "V01-V14 mature V2 synthesis + active Character Modeling and Reconstruction layer"
generation: V2_CMR
version: "2.7"
status: active_provisional
source_boundary: "Original Japanese light novels Volumes 01-14"
current_entrypoint: CURRENT_STATE_AND_CORPUS_MAP.md
analysis_root: "17UvtZCM9QBQdFtqKjDsebZfQXsuB2idH"
v2_analysis_root: "1q1xEv83Ld8KGENT_cZTN3OhAzjoFqzzs"
primary_source_root: "1s8Ido1uUbAyR-lXstTyOVfoeHaUDop-g"
cmr_root: "1z-U_tluPeOwMuRIVzEbQOOxrI1cYlMK4"
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
updated: "2026-08-23T20:45:00-04:00"
---

# YOUJO SENKI — CURRENT STATE AND CORPUS MAP

## 1. Current state

*Youjo Senki* has one canonical analytical Drive root with three distinct responsibility layers:

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
- `YOUJO_SENKI_CHARACTER_RECONSTRUCTION_READINESS_AUDIT.md` - Drive `1LYRzJS4AL6jHAmIAjkaOC-HIWQQdBp51`; qualitative readiness authority and CMR-2 handoff.
- `YOUJO_SENKI_TANYA_CMR2_CANDIDATE_SCENE_POOL.tsv` - Drive `1LRcSX-k739E4O4xQ2ImZnawzx6IylARo`; 1,200 broad-recall Tanya candidate centers across V01-V14; SHA-256 `8344b6196565645cfe373d3468fa4f3c618d1c4d3afb363667c64a073a5c469a`.
- `YOUJO_SENKI_TANYA_CMR2_CANDIDATE_RETRIEVAL_SCRIPT.py` - Drive `1GZMXU-ulPFfKFKGrjl6GjXUYtqnorwg5`; reproducible CMR-2A retrieval support.
- `YOUJO_SENKI_TANYA_CMR2_CANDIDATE_RETRIEVAL_MANIFEST.md` - Drive `1v3oLyOSuwD9WgZX_TvAPekRo20g4m_Rh`; CMR-2A completion/limitations and CMR-2B handoff.
- `YOUJO_SENKI_TANYA_CMR2_ADJUDICATION_LEDGER.tsv` - Drive `1Eoz8hpJMoeksACmQgvJXntTEcYM-w20g`; cumulative candidate disposition ledger; V01-V12 currently **1,045/1,045** adjudicated; SHA-256 `4391f1042668cdc2148f6e09b975317cb5ab9d20c9e0e1679d491c450a8e6fa0`.
- `YOUJO_SENKI_TANYA_CMR2_DIAGNOSTIC_EVIDENCE_INDEX.tsv` - Drive `1i1Ov7u5yGciH55j-04LxIR4CWck61-KH`; cumulative source-adjudicated evidence index; V01-V12 currently **676 diagnostics**; SHA-256 `1240953f6174375e64ddf1eb44af83954984a438c4b2fbc5d8869dabcf42ce68`.
- `YOUJO_SENKI_TANYA_CMR2B_ADJUDICATION_SCRIPT.py` - Drive `1whdImFw-vUblagWfpiqEmY58hT1vd3LZ`; reproducible cumulative V01-V12 build with frozen V01-V11-prefix preservation guards and validation; SHA-256 `23078662fed83e7aa8ba7c5e59fe9e0946a58ab75abab61a7de0a326e5e6909f`.
- `YOUJO_SENKI_TANYA_CMR2B_ADJUDICATION_MANIFEST.md` - Drive `1JxHeRuCRltCmQsyIs2nQruzewx1U8Bmd`; v2.1 cumulative V01-V12 authority, preservation controls, limitations, and V13 handoff.

Current active evidence work:

- cumulative Tanya candidate-adjudication ledger and diagnostic evidence index, with V01-V12 complete and V13-V14 pending;
- future speech-act/interaction matrix;
- future everyday-life/preferences/material-habits ledger.

#### `02 Character Models`
Drive: `1AMNfngVWTSm_4O0XadlJjHWjR8hMw21X`

First required pilot:

- `YOUJO_SENKI_TANYA_DEGURECHAFF_CHARACTER_RECONSTRUCTION_MODEL.md`.

Other character models are gated by source-coverage audit.

#### `03 Relationship Registers`
Drive: `1TomsYaw1BmQMRp-JuMils2PeHzl375uo`

Future home for the directional character relationship/register matrix.

#### `04 QA and Simulation`
Drive: `1dPqF3RjqawccCi8LA59QVMXsp2KDvH63`

Future home for held-out validation, perturbation tests, adversarial caricature tests, cross-model consistency checks, and promotion audits.

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

Current readiness classes:

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

The first modeling roster is now frozen for this generation: Tanya first; Lergen/Visha/Zettour as transfer priorities after Tanya QA; bounded specialists only within audited domains.

### Tanya evidence pilot - CMR-2 active

- **CMR-2A candidate retrieval: COMPLETE.** The deterministic broad-recall pass reduced the 63,812-row CMR-0 source index to **1,200** Tanya candidate centers distributed across V01-V14.
- Candidate-pool SHA-256: `8344b6196565645cfe373d3468fa4f3c618d1c4d3afb363667c64a073a5c469a`.
- Candidate priorities: 388 `HIGH`, 762 `MEDIUM`, 50 `LOW`. Priority means adjudication usefulness, not evidentiary confidence.
- Heuristic category/speech/relationship tags are retrieval cues only; they must not be promoted directly into claims.
- **CMR-2B candidate adjudication: ACTIVE.** Volumes 01-12 are complete: **1,045/1,045** cumulative candidates adjudicated. V12 added 44 `RETAIN`, 12 `MERGE`, and 5 `REJECT` dispositions while preserving every V01-V11 row and identifier unchanged.
- The cumulative V01-V12 diagnostic index contains **676** source-adjudicated states. V12 added **60 states: 53 `HIGH`, 7 `MODERATE`**. V12 materially strengthens historical-glory versus civilian-legacy preferences, patriotism modeled without projection, unfamiliar-institution fallibility, career ambition under order constraints, context override of combat habits, familiar-unit humor and material reciprocity, enemy competence/aesthetic appreciation, developmental mentorship, audience-conditioned violent rhetoric, bounded tactical enjoyment, body/age observer effects, Tanya-Zettour modeling, Grantz advocacy and recorded dissent, retreat/casualty-reduction command logic, dynamic enemy learning, Uger peer-professional interaction, civilian-normalcy aspirations, subordinate-welfare advocacy, resource bargaining, and veteran intuition under uncertainty.
- V13-V14 remain pending. The evidence pack remains `active_provisional`; the raw 676-state count exceeds the eventual 250-350 target by design, and all-volume deduplication/counterevidence review must wait until V14. V01 IDs `YS-TAN-CMR2-V01-001` through `055`, V02 IDs `YS-TAN-CMR2-V02-001` through `054`, V03 IDs `YS-TAN-CMR2-V03-001` through `046`, V04 IDs `YS-TAN-CMR2-V04-001` through `055`, V05 IDs `YS-TAN-CMR2-V05-001` through `059`, V06 IDs `YS-TAN-CMR2-V06-001` through `041`, V07 IDs `YS-TAN-CMR2-V07-001` through `053`, V08 IDs `YS-TAN-CMR2-V08-001` through `045`, V09 IDs `YS-TAN-CMR2-V09-001` through `069`, V10 IDs `YS-TAN-CMR2-V10-001` through `071`, V11 IDs `YS-TAN-CMR2-V11-001` through `068`, and V12 IDs `YS-TAN-CMR2-V12-001` through `060` are stable provenance identifiers. V12 does not close the attraction/orientation question; the V05 former-male-psyche/current-female-body dilemma remains OPEN / underdetermined and does not license a modern categorical gender-identity label.

### Character models

- Tanya: **CMR-2 evidence pilot active; model not yet emitted**;
- Lergen/Visha/Zettour: **approved transfer priorities after Tanya QA, subject to their audited ceilings**;
- other audited characters: **modeling allowed only within the CMR-1 readiness class/domain boundary**.

### Relationship matrix

- not yet emitted.

### QA

- held-out validation suite not yet emitted.

## 8. Binding next steps

1. **CMR-0 - COMPLETE:** deterministic source extraction and exact-locator build across V01-V14.
2. **CMR-1 - COMPLETE:** controlled alias map + first production reconstruction-readiness audit for the recurring cast.
3. **CMR-2A - COMPLETE:** 1,200-candidate broad-recall Tanya scene pool across V01-V14.
4. **CMR-2B - ACTIVE:** V01-V12 adjudication complete; V13 next. Continue the same cumulative ledger/index through V14 while preserving earlier identifiers, then run cross-volume deduplication and counterevidence audit toward roughly 250-350 source-verified diagnostic states.
5. **CMR-3 — Tanya reconstruction model** after CMR-2 evidence closure.
6. **CMR-4 — Tanya held-out and adversarial QA**.
7. **CMR-5 — transfer pilots** for Visha, Lergen, and Zettour if readiness supports them.
8. **CMR-6 — directional relationship matrix and cross-model QA** after multiple models exist.

## 9. Recommended retrieval routes

For a mature literary/theme question:

> `CURRENT_STATE_AND_CORPUS_MAP.md` → `V2 Analysis` relevant specialist document → Document 11 if chronology/evidence trail is needed → Japanese source for exact verification

For a compact mature comparison:

> `CURRENT_STATE_AND_CORPUS_MAP.md` → `V2 Analysis/10_COMPARATIVE_REFERENCE_AND_OPEN_QUESTIONS.md` → relevant specialist document when compression needs expansion

For a character-reconstruction question:

> `CURRENT_STATE_AND_CORPUS_MAP.md` → CMR-0 source locator/member index → mature V2 character/relationship context → CMR diagnostic/model layer → exact Japanese source

For generated hypothetical scenarios:

> scenario state → retrieve canonical analogues → infer attention/appraisal → infer action → select relationship/state-appropriate register → generate dialogue → label inference boundaries

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
