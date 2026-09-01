---
title: "Gakuen Idolmaster Multi-Document Synthesis Architecture V2"
project: "Gakuen Idolmaster / 学園アイドルマスター"
document_type: "production architecture and phase plan"
version: "2.4"
status: "canonical working architecture"
last_updated: "2026-08-17"
revision_note: "adds mandatory Phase-6 distributed-character reconstruction for Kaya Rinha, with cross-character provenance, observer triangulation, and explicit dossier promotion rules; preserves the 13-character playable-core architecture"
governing_method: "GAKUEN_IDOLMASTER_FULL_CORPUS_ANALYTICAL_METHOD_V2.md"
source_lock: "GAKUMAS V2 Source Lock 1.0"
created: "2026-08-13"
---

# GAKUEN IDOLMASTER MULTI-DOCUMENT SYNTHESIS ARCHITECTURE V2

## 0. Purpose

This document defines the production architecture for turning the frozen Gakuen Idolmaster source corpus into a complete, durable, source-grounded analysis of story, characters, relationships, institutions, Japanese language, voice performance, image songs, music-video dramaturgy, and full-series themes.

It governs:

- directory structure;
- phase order;
- phase dependencies;
- source-facing analytical artifacts;
- cumulative ledgers;
- audiovisual requests;
- definitive character monographs;
- specialist synthesis documents;
- final reader-facing corpus;
- provenance and release packaging.

The architecture is designed to prevent three recurring failure modes:

1. **premature synthesis** — writing polished theses before the corpus has been systematically read;
2. **context loss** — scattering insights across chats without durable ledgers and source locators;
3. **continuity flattening** — treating branching game states as one linear biography.

The architecture therefore separates:

> **source-facing work** from **reader-facing synthesis**.

The first layer exists to make the second trustworthy.

---

# 1. Governing dependency graph

The project dependency chain is:

```text
PHASE 0  Corpus Audit / Source Lock
   |
   v
PHASE 1  Continuity + Story-State Reconstruction
   |
   +------------------+
   |                  |
   v                  v
PHASE 2             AV Baseline Infrastructure
Shared/Institution   Song Catalog + Crosswalk
   |                  |
   +---------+--------+
             |
             v
PHASE 3  Character-Core Readings (13)
             |
             v
PHASE 4  Story-Event Pass
             |
             v
PHASE 5  Support-Card Pass
             |
             v
PHASE 6  Relationship + Side-Character Synthesis
         + Kaya Rinha Distributed-Character Dossier
             |
             v
PHASE 7  Definitive Character Monographs (13)
             |
             v
PHASE 8  Specialist Thematic / Institutional / Language / Music Docs
             |
             v
PHASE 9  Full-Series Synthesis + Adversarial Audit
             |
             v
PHASE 10 Legacy Reconciliation + Indexing + Release Package
```

Key prohibition:

> **No definitive character monograph before Phases 4–6 are substantially complete.**

Key audiovisual rule:

> **Dialogue video is requested on demand during source reading; song/MV coverage begins early as a systematic baseline.**

---

# 2. Proposed Google Drive / archive directory tree

Recommended durable structure:

```text
GAKUEN_IDOLMASTER/
|
|-- 00_FRAMEWORKS_AND_SOURCE_CONTROL/
|   |-- GAKUEN_IDOLMASTER_FULL_CORPUS_ANALYTICAL_METHOD_V2.md
|   |-- GAKUEN_IDOLMASTER_MULTI_DOCUMENT_SYNTHESIS_ARCHITECTURE_V2.md
|   |-- GKM_SOURCE_INVENTORY.md
|   |-- GKM_SOURCE_LOCK.md
|   |-- GKM_DEDUP_AND_EXCEPTION_AUDIT.md
|   |-- GKM_LEGACY_ANALYSIS_INVENTORY.md
|   `-- GKM_CORPUS_CHANGELOG.md
|
|-- 01_PRIMARY_SOURCES/
|   |-- [existing source tree or link/reference to it]
|   |-- 00_context/
|   |-- transcripts_raw/
|   |-- transcripts_dialogue_only/
|   `-- analysis_bundles/
|
|-- 02_INFRASTRUCTURE_AND_LEDGERS/
|   |-- GKM_SOURCE_IDENTITY_AND_DEDUP_LEDGER.*
|   |-- GKM_CONTINUITY_AND_STORY_STATE_LEDGER.*
|   |-- GKM_BRANCH_DIVERGENCE_LEDGER.*
|   |-- GKM_CHARACTER_STATE_LEDGER.*
|   |-- GKM_RELATIONSHIP_STATE_LEDGER.*
|   |-- GKM_INSTITUTION_AND_IDOL_SYSTEM_LEDGER.*
|   |-- GKM_THEME_AND_MOTIF_LEDGER.*
|   |-- GKM_JAPANESE_VOICE_AND_REGISTER_LEDGER.*
|   |-- GKM_NPC_AND_SIDE_CHARACTER_LEDGER.*
|   |-- GKM_SUPPORT_AND_EVENT_PARTICIPANT_INDEX.*
|   |-- GKM_PRIMARY_SOURCE_LOCATOR_LEDGER.*
|   |-- GKM_LEGACY_CLAIM_REVISION_LEDGER.*
|   |-- GKM_VOICE_PERFORMANCE_STATE_LEDGER.*
|   |-- GKM_SONG_AND_MUSICAL_IDENTITY_LEDGER.*
|   |-- GKM_AUDIOVISUAL_VERIFICATION_QUEUE.*
|   `-- GKM_AUDIOVISUAL_SOURCE_CROSSWALK.*
|
|-- 03_SOURCE_FACING_READINGS/
|   |-- 00_SHARED_AND_INSTITUTIONAL/
|   |-- 01_CHARACTERS_CORE/
|   |-- 02_STORY_EVENTS/
|   |-- 03_SUPPORT_CARDS/
|   `-- 04_AV_READINGS/
|
|-- 04_RELATIONSHIP_AND_ENSEMBLE_SYNTHESIS/
|
|-- 05_DEFINITIVE_CHARACTER_MONOGRAPHS/
|
|-- 06_SPECIALIST_SYNTHESIS/
|
|-- 07_READER_FACING_FINAL_CORPUS/
|
|-- 08_PROVENANCE_INDEXES_AND_RELEASE/
|
`-- 90_LEGACY_V1_ANALYSIS/
```

The source tree itself should remain immutable under the formal source lock. Analysis should reference it rather than reorganize or rename primary files in ways that destroy provenance.

---

# 3. Phase 0 — Corpus audit and source lock

## Goal

Establish exactly what exists before interpretation begins.

## Inputs

- complete Drive source tree;
- `00_context` metadata;
- analysis-bundle reports;
- current prior-analysis corpus/transcripts;
- known public music metadata sources.

## Required outputs

### `GKM_SOURCE_INVENTORY.md`

Record:

- archive root;
- source commit/revision;
- generation date;
- categories;
- file counts;
- dialogue-line counts;
- character-bundle coverage;
- story-event coverage;
- support-card coverage;
- known omissions/limitations.

### `GKM_SOURCE_LOCK.md`

Define:

- Source Lock 1.0;
- what it includes;
- what it excludes;
- change-control rules;
- live-service update policy.

### `GKM_DEDUP_AND_EXCEPTION_AUDIT.md`

Resolve:

- duplicated bundle views;
- ambiguous/unassigned files;
- dialogue-bearing exceptions;
- files with zero extracted dialogue;
- manually promoted institutional/shared scenes.

### `GKM_OFFICIAL_PARATEXT_AND_CREATOR_COMMENTARY_REGISTER.md`

Maintain a separately versioned evidence register for non-S1 material:

- `S2` official canonical paratext;
- `S3` credited creator/staff commentary;
- `S4` reliable external secondary sources;
- `S5` fan/discovery references.

Record claim type (`A-F`), source URL, publication/access dates, bounded proposition, affected artifacts, and conflicts with S1. **Do not merge these sources into the frozen ADV Source Lock or its counts.**

### `GKM_LEGACY_ANALYSIS_INVENTORY.md`

Catalogue previous Gakumas work:

- full-series synthesis;
- Saki analysis;
- Hanami sisters;
- SyngUp!;
- REVERSI;
- Worst Three;
- other character/relationship/theme discussions.

Do not evaluate them fully yet; only preserve provenance and key claims.

## Infrastructure initialized

Create empty or minimally seeded versions of all persistent ledgers.

## Exit criteria

Phase 0 completes when:

- source identity is frozen;
- duplicate handling is defined;
- meaningful exceptions are known;
- legacy work is inventoried;
- no major unexplained source branch remains.

---

# 4. Phase 1 — Continuity and story-state reconstruction

## Goal

Build a chronology model strong enough to prevent false biographies.

## Primary tasks

### 4.1 Map Produce Story Series 1

For each playable idol:

- opening states;
- audition stages;
- failure variants;
- normal variants;
- true-labeled variants;
- shared/invariant scenes;
- endpoint relationships.

### 4.2 Map Series 2 / N.I.A.

Establish:

- shared N.I.A. world rules;
- character entry points;
- audition structure;
- rankings/fan-vote role;
- FINALE relation;
- branch variants;
- relationship to prior development.

### 4.3 Map Series 3 / H.I.F.

Establish:

- selection structure;
- H.I.F. main competition;
- shared world-exposition;
- participant-specific states;
- ending variants;
- late-development implications.

### 4.4 Map unit story

Read unit-story episodes for:

- ensemble anchors;
- relationship history;
- school-state placement;
- references to Produce progression.

### 4.5 Classify Dear Idol, events, support stories

Do not force exact dates when evidence is weak.

Assign C0–C4 continuity classes.

## Required outputs

### `GKM_CONTINUITY_AND_STORY_STATE_MAP.md`

Reader-oriented explanation of the reconstructed chronology and its uncertainties.

### `GKM_CONTINUITY_AND_STORY_STATE_LEDGER`

Structured source-level mapping.

### `GKM_BRANCH_DIVERGENCE_LEDGER`

Detailed alternate-state tracking.

## Exit criteria

- every Produce Story family has a provisional continuity model;
- branch variants are explicitly separated;
- shared anchors are identified;
- later phases can cite story states consistently.

---

# 5. Parallel Phase 1A — Audiovisual baseline and discovery infrastructure

This runs alongside Phases 1–3.

## Goal

Ensure voice/music analysis is integrated early without requiring exhaustive video ingestion.

## 5.1 Build complete song inventory

For each major idol, identify:

- known solo/image songs;
- unit songs;
- major ensemble songs;
- release date;
- composer;
- lyricist;
- arranger;
- official MV/video if available;
- Project-imas entry if useful;
- known story/release association.

Use official sources for final factual verification where possible; use Project-imas as a discovery/crosswalk layer.

## 5.2 Select initial Musical Identity Core Corpus

Target:

- **3 songs/MVs per idol initially**.

Prioritize:

- foundational identity;
- contrasting sound;
- later/developmental identity.

Do not require all 39 audiovisual files before textual analysis starts. Requests may be staggered by character.

## 5.3 Build crosswalk

Create:

`GKM_AUDIOVISUAL_SOURCE_CROSSWALK.md/.json`

Map machine-oriented transcript IDs to human-searchable names and public media identities. The crosswalk must explicitly preserve:

- internal `adv_*` source ID/path;
- source family;
- official/public UI title where recoverable;
- uploader/community title;
- character/card/song/event/STEP identity;
- optimized Japanese search query;
- supplied media filename/checksum once acquired.

Default public retrieval vocabulary should include `親愛度コミュ`, `楽曲コミュ`, `プロデュースコミュ`, `育成コミュ`, `おでかけコミュ`, `営業コミュ`, `サポートコミュ`, `イベントコミュ`, and `初星コミュ` where applicable.

## 5.4 Initialize AV queue

Create:

`GKM_AUDIOVISUAL_VERIFICATION_QUEUE`

Dialogue scenes are added only when the reread shows they matter.

## Exit criteria

This parallel phase never truly “closes”; it reaches minimum viability when:

- each idol has an initial song shortlist;
- naming crosswalk conventions are working;
- dialogue AV requests can be expressed in human-searchable terms.

---

# 6. Phase 2 — Shared narrative and institutional spine

## Goal

Understand the world before reducing it to individual character arcs.

## Read

- tutorial/shared material;
- `00_shared` bundles;
- unit story;
- common Produce Story exposition;
- N.I.A. world-explanation scenes;
- H.I.F. world-explanation scenes;
- institutional exceptions such as tower/request-system dialogue;
- shared startup/seasonal material when meaningful.

## Core questions

- What is Hatsuboshi Academy structurally?
- What does it believe idol development requires?
- How are Producer and idol responsibilities divided?
- How are competition, rankings, fans, jobs, and public performance organized?
- What does the school reward?
- What does it risk distorting?
- What changes between Series 1, N.I.A., and H.I.F.?

## Outputs

### `GKM_SHARED_AND_INSTITUTIONAL_SPINE_DEEP_READING.md`

### Updates to

- institution ledger;
- continuity ledger;
- theme/motif ledger;
- NPC ledger;
- source locator ledger.

## Exit criteria

The institutional vocabulary and macro-story progression are sufficiently stable to support character readings.

---

# 7. Phase 3 — Thirteen character-core readings

## Goal

Construct provisional character models from core source families before ensemble correction.

## Characters

Recommended order may be adjusted, but the corpus must cover all 13:

1. Hanami Saki / 花海咲季
2. Tsukimura Temari / 月村手毬
3. Fujita Kotone / 藤田ことね
4. Arimura Mao / 有村麻央
5. Katsuragi Lilja / 葛城リーリヤ
6. Kuramoto China / 倉本千奈
7. Shinosawa Hiro / 篠澤広
8. Himesaki Rinami / 姫崎莉波
9. Shiun Sumika / 紫雲清夏
10. Hanami Ume / 花海佑芽
11. Hataya Misuzu / 秦谷美鈴
12. Juo Sena / 十王星南
13. Amaya Tsubame / 雨夜燕

## Source order inside each character pass

Read separately:

1. Produce Story;
2. Dear Idol;
3. Idol Communications;
4. Produce Events;
5. live/system/startup dialogue where meaningful;
6. shared/unit material directly affecting the character.

Do not read `99_complete_character_bundle` as a single chronology.

## Audiovisual integration

For each character:

- inspect initial 3-song/MV baseline as available;
- create a provisional sonic identity profile;
- add P0/P1 dialogue scenes to AV queue;
- resolve each active request into uploader-facing Japanese nomenclature before asking the user to retrieve it;
- group multiple scene requests into one whole-commu/compilation target whenever possible;
- provide copy-paste-ready primary and fallback search terms;
- request raw files only where interpretation benefits substantially;
- never require the user to cut target scenes when a complete commu is available—the analyst timestamps the relevant material after upload.

## Output naming

```text
GKM_CORE_01_HANAMI_SAKI.md
GKM_CORE_02_TSUKIMURA_TEMARI.md
...
GKM_CORE_13_AMAYA_TSUBAME.md
```

## Required ending section in every core reading

- Stable observations
- Working hypotheses
- Branch divergences
- Contradictions
- Relationship questions
- Event/support verification targets
- AV requests
- Legacy claims to test
- Open questions

## Exit criteria

All 13 idols have provisional models, but none is labeled definitive.

---

# 8. Phase 4 — Numbered story-event pass

## Goal

Reconstruct ensemble behavior and test provisional character models against multi-character narrative.

## Tranches

Recommended source-facing outputs:

### `GKM_EVENTS_001_005_DEEP_READING.md`
### `GKM_EVENTS_006_012_DEEP_READING.md`
### `GKM_EVENTS_013_020_DEEP_READING.md`
### `GKM_EVENTS_021_PLUS_DEEP_READING.md`

The exact tranche boundary can be revised if narrative groupings make a better segmentation, but source coverage must remain complete.

## For every event track

- participant list;
- story-state estimate;
- conflict;
- institutional setting;
- character deltas;
- relationship deltas;
- new side characters;
- thematic implications;
- contradictions to Phase-3 models;
- AV requests;
- primary locators.

## Exit criteria

All event stories are processed and ledgers updated.

---

# 9. Phase 5 — Complete support-card pass

## Goal

Capture the ordinary social ecology and relationship evidence that main routes cannot provide alone.

## Tranches

Follow existing bundle segmentation unless source evidence suggests a more coherent alternative.

Example output family:

```text
GKM_SUPPORT_SERIES_01_DEEP_READING.md
GKM_SUPPORT_SERIES_02_PART_001_025_DEEP_READING.md
GKM_SUPPORT_SERIES_02_PART_026_050_DEEP_READING.md
GKM_SUPPORT_SERIES_02_PART_051_074_DEEP_READING.md
GKM_SUPPORT_SERIES_03_PART_001_025_DEEP_READING.md
GKM_SUPPORT_SERIES_03_PART_026_050_DEEP_READING.md
GKM_SUPPORT_SERIES_03_PART_051_075_DEEP_READING.md
GKM_SUPPORT_SERIES_03_PART_076_102_DEEP_READING.md
```

## Participant indexing

Update:

`GKM_SUPPORT_AND_EVENT_PARTICIPANT_INDEX`

for every support story.

## Special focus

Support material should actively test:

- stable personality versus crisis behavior;
- casual language/register;
- food/body/training habits;
- socioeconomic context;
- teasing and humor;
- peer trust;
- informal senpai/kouhai relations;
- low-stakes Producer behavior;
- social comfort and avoidance.

## Exit criteria

All support stories are read, indexed, and linked to character/relationship ledgers.

---

# 10. Phase 6 — Relationship, ensemble, and side-character synthesis

## Goal

Move from individual models to relational systems.

## 10.1 Major relationship synthesis I

Proposed document:

`GKM_RELATIONSHIP_SYSTEMS_I_HANAMI_REVERSI_AND_SYNGUP.md`

Likely focus:

- Saki / Ume;
- Lilja / Sumika / REVERSI;
- Temari / Misuzu / Rinha / SyngUp!.

These should remain subject to revision if the reread suggests better grouping.

## 10.2 Major relationship synthesis II

Proposed document:

`GKM_RELATIONSHIP_SYSTEMS_II_RIVALRY_FRIENDSHIP_CLASS_AND_SUCCESSION.md`

Likely focus:

- Saki / Temari / Kotone;
- China / Ume / Hiro;
- Sena / Tsubame;
- class networks;
- senior/junior structures;
- succession and inheritance;
- Producer as relational node.

## 10.3 Side-character synthesis

Proposed:

`GKM_SIDE_CHARACTERS_FAMILIES_STAFF_GOKUGETSU_AND_EXTERNAL_PRESSURES.md`

Use speaker/mention searches across the corpus rather than folder availability.

Specially ensure coverage of non-playable but structurally important figures such as Rinha.

## 10.4 Distributed-character reconstruction — Kaya Rinha / 賀陽燐羽

**Status:** PLANNED / mandatory Phase-6 specialist branch.

Rinha must **not** be treated as a fourteenth playable-character core. Her evidence is structurally different: there is no dedicated playable-character bundle, and her characterization is distributed across Temari, Misuzu, Saki, SyngUp!, Gokugetsu, event/support material, and other cross-character scenes. The project therefore reconstructs her from intersections among evidence surfaces rather than from one route-centered archive.

### Planned artifacts

1. `GKM_KAYA_RINHA_SOURCE_CROSSWALK.md`
   - one row per unique canonical source object;
   - source family and exact locator;
   - continuity class;
   - primary viewpoint / host-character bundle;
   - whether Rinha is present, speaks, acts, is remembered, or is only discussed;
   - relationship tags;
   - AV availability and public-facing retrieval nomenclature.

2. `GKM_KAYA_RINHA_EVIDENCE_MATRIX.md`
   - claim ID and bounded proposition;
   - direct Rinha evidence;
   - observer reports;
   - retrospective-memory evidence;
   - cross-context corroboration;
   - contradictions/counterevidence;
   - confidence and `PRESERVE / STRENGTHEN / REVISE / DOWNGRADE / REJECT / OPEN` status.

3. `GKM_KAYA_RINHA_CHARACTER_DOSSIER.md`
   - active-provisional specialist synthesis;
   - authority/source-boundary notice emphasizing distributed reconstruction;
   - chronology/institutional trajectory;
   - SyngUp! history;
   - Temari, Misuzu, Saki, and non-SyngUp! relationship models;
   - competitive/idol ethos;
   - personality and behavioral invariants;
   - vulnerability/attachment/avoidance with direct-vs-mediated separation;
   - Japanese speech/register model;
   - performed voice/AV layer when sufficient material is staged;
   - contradictions, competing interpretations, reconstruction guide, and open questions.

A separate `GKM_KAYA_RINHA_AUDIOVISUAL_BASELINE_AND_REQUESTS.md` should be created **only if** the source crosswalk identifies enough specific voiced scenes to justify a distinct acquisition responsibility. Do not create it merely for symmetry.

### Reconstruction method

Proceed in this order:

1. **Entity resolution and corpus mining** — search `賀陽燐羽`, `燐羽`, confirmed internal speaker/actor code, `SyngUp!`, Gokugetsu associations, event/support participation, and indirect references across all character bundles.
2. **Canonical deduplication** — count unique underlying scripts, never bundle appearances.
3. **Evidence-surface labeling** — distinguish `R-DIRECT`, `R-ACTION`, `R-LING`, `R-AV`, `OTHER-REPORT`, `MEMORY`, `REL-INFERENCE`, `META`, and `OPEN`.
4. **Observer matrix** — keep Rinha's own evidence separate from Temari's Rinha, Misuzu's Rinha, Saki's Rinha, and other observers. Disagreement is evidence, not noise to be averaged away.
5. **Conservative chronology** — place scenes using the project `C0-C4` ontology before psychological synthesis; do not concatenate incompatible route states into one biography.
6. **Behavioral invariants** — test traits across unrelated relationships and contexts before promoting them to personality-level claims.
7. **Relationship-specific models** — reconstruct Rinha/Temari, Rinha/Misuzu, Rinha/Saki, and other important dyads independently before generalizing.
8. **Japanese voice/register model** — concatenate Rinha lines only with their source envelopes preserved; map pronouns, address, politeness, teasing/provocation, commands, hedges, laughter, disfluency, and relation-specific shifts.
9. **Audiovisual backfill** — retrieve voiced versions by exact recovered scene rather than broad character-name search; use AV to adjudicate tone, gaze, timing, affect leakage, and the difference between playful, defensive, wounded, and hostile provocation.
10. **Adversarial audit** — actively search for direct affection, accepted care, noncompetitive behavior, ordinary teamwork, explicit ambition, and other evidence capable of falsifying an emerging model.
11. **Dossier synthesis** — write only after the crosswalk and evidence matrix make direct versus mediated claims traceable.

### Scheduling and dependency

- Do **not** begin the definitive Rinha dossier before the Phase-4 numbered-event and Phase-5 support-card passes are substantially complete; those layers may contain the ordinary-life and cross-relationship controls needed to correct SyngUp!-heavy sampling.
- The source crosswalk may begin opportunistically earlier if retrieval work is convenient, but it remains provisional until Phases 4-5 are incorporated.
- The Rinha dossier should be substantially complete before Phase-7 definitive Temari and Misuzu monographs, because both models depend on an independently adjudicated account of Rinha rather than only their perceptions of her.
- Rinha remains outside the numbered 13-character monograph set unless a later source expansion makes a separate definitive monograph analytically necessary. Promotion must be evidence-driven, not symmetry-driven.

### Governing principle

> **Reconstruct Rinha from intersections, not reflections. Temari's Rinha, Misuzu's Rinha, Saki's Rinha, remembered Rinha, and Rinha's own words/actions are distinct evidence surfaces. The dossier becomes trustworthy where those surfaces triangulate—or where their disagreement itself reveals something important.**

## Audiovisual focus

This phase is a major trigger for P0/P1 dialogue-video requests because relationship tone often depends on delivery.

## Exit criteria

Major relational systems are mature enough to correct the 13 provisional character models, and the Rinha distributed-character crosswalk/evidence matrix/dossier are sufficiently complete to prevent Temari/Misuzu/SyngUp! synthesis from relying only on host-character perception.

---

# 11. Phase 7 — Definitive character monographs

## Goal

Rewrite each character from scratch using the entire matured evidence base.

The Phase-3 core readings remain preserved as source-facing artifacts and are **not simply overwritten**.

## Canonical monograph set

```text
13_HANAMI_SAKI.md
14_TSUKIMURA_TEMARI.md
15_FUJITA_KOTONE.md
16_ARIMURA_MAO.md
17_KATSURAGI_LILJA.md
18_KURAMOTO_CHINA.md
19_SHINOSAWA_HIRO.md
20_HIMESAKI_RINAMI.md
21_SHIUN_SUMIKA.md
22_HANAMI_UME.md
23_HATAYA_MISUZU.md
24_JUO_SENA.md
25_AMAYA_TSUBAME.md
```

Numbers reflect the proposed final reader-facing corpus described below.

## Pre-monograph sonic coverage audit

Before finalizing each character:

- inspect whether 3-song baseline adequately represents musical development;
- add 1–3 additional songs/MVs if necessary;
- resolve outstanding AV-P0 requests;
- resolve most AV-P1 requests central to the character thesis.

## Required monograph sections

Use the template defined in the governing method, while allowing character-specific expansion.

## Exit criteria

All 13 characters have full-corpus monographs with source locators and mature audiovisual interpretation.

---

# 12. Phase 8 — Specialist synthesis documents

## Goal

Write thematic and structural documents only after the character/relationship corpus is mature.

## Proposed specialist documents

### `03_HATSUBOSHI_ACADEMY_EDUCATION_PRODUCTION_AND_INSTITUTIONAL_PHILOSOPHY.md`

Questions:

- What institution is Hatsuboshi?
- What model of development does it instantiate?
- Where does it help or harm?
- How do N.I.A./H.I.F. alter its logic?

### `04_IDOLHOOD_TALENT_POPULARITY_PERFORMANCE_VISIBILITY_AND_PRIMA_STELLA.md`

Questions:

- What counts as idol talent?
- What is popularity measuring?
- How do audience judgment and self-authorship interact?
- How many competing conceptions of idolhood exist?

### `05_RIVALRY_COMPETITION_AMBITION_FAILURE_AND_RECOGNITION.md`

Questions:

- When is rivalry intimacy?
- When is it destructive?
- How is failure metabolized?
- What is the relationship between being seen and being surpassed?

### `06_SUPPORT_CARE_DEPENDENCY_AUTONOMY_FRIENDSHIP_AND_LOVE.md`

Questions:

- What does support mean in Gakumas?
- When does care enable autonomy?
- When does care become dependency, avoidance, or control?

### `07_BODY_TRAINING_FOOD_HEALTH_MONEY_LABOR_AND_MATERIAL_LIFE.md`

Questions:

- How does bodily capacity structure aspiration?
- What role do food, health, money, work, and class play?
- How material is the series's concept of talent?

### `08_TRADITION_INHERITANCE_SENPAI_KOUHAI_GRADUATION_AND_SUCCESSION.md`

Questions:

- How are ideals inherited or resisted?
- What does it mean to follow, surpass, or replace someone?
- How does graduation reorganize identity?

### `09_PRODUCER_PEDAGOGY_READING_COAUTHORSHIP_POWER_AND_ETHICS.md`

Questions:

- What kind of authority does Producer exercise?
- How individualized is his pedagogy?
- What are the ethical risks of directing another person's self-construction?

### `10_JAPANESE_LANGUAGE_VOICE_ACTING_AND_CHARACTER_PERFORMANCE.md`

Questions:

- How does written register become performed character?
- Which relational shifts are linguistic, vocal, or both?
- How do public and private voices diverge?

### `11_MUSIC_SONG_VOCAL_IDENTITY_AND_DRAMATURGY.md`

Questions:

- What is each idol's sonic identity?
- How do songs change with story state?
- What does the singing self express that dialogue cannot?
- How do composition, arrangement, lyrics, vocals, choreography, and visual staging co-author character?

### `12_MAJOR_RELATIONSHIP_SYSTEMS_AND_ENSEMBLE_ECOLOGY.md`

This may either synthesize Phase-6 relationship documents into a reader-facing version or be split into two documents if density requires it.

## Exit criteria

Specialist documents are mutually cross-referenced and no longer depend on untested Phase-3 hypotheses.

---

# 13. Phase 9 — Full-series synthesis and adversarial audit

## Goal

Produce the reader-facing overview only after specialist layers stabilize.

## 13.1 Story architecture document

### `02_STORY_ARCHITECTURE_CONTINUITY_BRANCHES_AND_TIMELINE.md`

Explain:

- source families;
- Series 1 / N.I.A. / H.I.F. progression;
- branch logic;
- continuity classes;
- unit/event/support placement;
- limits of chronology.

This is the reader's guide to how the narrative actually works.

## 13.2 Full-series synthesis

### `01_FULL_SERIES_SYNTHESIS_STORY_THEMES_AND_ARGUMENT.md`

This should answer:

- What kind of story is Gakumas?
- What does it ultimately argue about becoming an idol/person?
- What is Hatsuboshi's role?
- How do competition, support, embodiment, public visibility, and self-authorship interact?
- What remains unresolved at Source Lock 1.0?

## 13.3 Adversarial audit

Before finalizing Documents 01–12 and character monographs:

- identify strongest counterexamples;
- locate characters who resist the thesis;
- inspect contradictory branches;
- test institution-negative cases;
- test Producer mistakes;
- inspect musical contradictions;
- audit legacy assumptions.

Output:

`GKM_FINAL_ADVERSARIAL_AUDIT.md`

This may remain apparatus rather than reader-facing final corpus.

## Exit criteria

No major thesis remains untested against counterevidence.

---

# 14. Phase 10 — Legacy reconciliation, reference matrices, and release

## Goal

Convert the analytical workspace into a durable research corpus.

## 14.1 Legacy reconciliation

Complete:

`GKM_LEGACY_CLAIM_REVISION_LEDGER`

Every important V1 claim becomes:

- confirmed;
- strengthened;
- narrowed;
- revised;
- rejected;
- unresolved.

## 14.2 Comparative matrices

Create reader-facing:

### `27_COMPARATIVE_REFERENCE_MATRICES_OPEN_QUESTIONS_AND_LIMITS.md`

Possible matrices:

- character central contradiction;
- conception of idolhood;
- relationship to competition;
- Producer pedagogy;
- failure response;
- support/dependency pattern;
- public/private self;
- musical identity;
- voice/register profile;
- material constraints;
- succession/inheritance role.

## 14.3 Current-state entrypoint and final README

While the corpus remains active, maintain **one mutable canonical first-read entrypoint** at the series root:

### `CURRENT_STATE_AND_CORPUS_MAP.md`

It must identify current authority, Source Lock, governing method/architecture, phase state, completed character/AV tranches, external-evidence register, cumulative ledgers, legacy status, immediate next step, and recommended retrieval route. A new chat does not create a new map or root.

When the corpus is frozen, write the final reader-facing map last:

### `00_README_AND_CORPUS_MAP.md`

Explain:

- project scope;
- source lock;
- how to read the corpus;
- distinction between reader-facing and apparatus layers;
- document map;
- provenance;
- known limitations;
- update policy.

## 14.4 Release package

Create:

- final Markdown corpus;
- manifests;
- checksums where practical;
- source locator index;
- optional ZIP archive;
- Google Drive mirror;
- Library copies where appropriate.

---

# 15. Proposed final reader-facing corpus

The target human-readable layer is approximately 28 documents.

```text
00_README_AND_CORPUS_MAP.md
01_FULL_SERIES_SYNTHESIS_STORY_THEMES_AND_ARGUMENT.md
02_STORY_ARCHITECTURE_CONTINUITY_BRANCHES_AND_TIMELINE.md
03_HATSUBOSHI_ACADEMY_EDUCATION_PRODUCTION_AND_INSTITUTIONAL_PHILOSOPHY.md
04_IDOLHOOD_TALENT_POPULARITY_PERFORMANCE_VISIBILITY_AND_PRIMA_STELLA.md
05_RIVALRY_COMPETITION_AMBITION_FAILURE_AND_RECOGNITION.md
06_SUPPORT_CARE_DEPENDENCY_AUTONOMY_FRIENDSHIP_AND_LOVE.md
07_BODY_TRAINING_FOOD_HEALTH_MONEY_LABOR_AND_MATERIAL_LIFE.md
08_TRADITION_INHERITANCE_SENPAI_KOUHAI_GRADUATION_AND_SUCCESSION.md
09_PRODUCER_PEDAGOGY_READING_COAUTHORSHIP_POWER_AND_ETHICS.md
10_JAPANESE_LANGUAGE_VOICE_ACTING_AND_CHARACTER_PERFORMANCE.md
11_MUSIC_SONG_VOCAL_IDENTITY_AND_DRAMATURGY.md
12_MAJOR_RELATIONSHIP_SYSTEMS_AND_ENSEMBLE_ECOLOGY.md
13_HANAMI_SAKI.md
14_TSUKIMURA_TEMARI.md
15_FUJITA_KOTONE.md
16_ARIMURA_MAO.md
17_KATSURAGI_LILJA.md
18_KURAMOTO_CHINA.md
19_SHINOSAWA_HIRO.md
20_HIMESAKI_RINAMI.md
21_SHIUN_SUMIKA.md
22_HANAMI_UME.md
23_HATAYA_MISUZU.md
24_JUO_SENA.md
25_AMAYA_TSUBAME.md
26_SIDE_CHARACTERS_FAMILIES_STAFF_GOKUGETSU_AND_EXTERNAL_PRESSURES.md
27_COMPARATIVE_REFERENCE_MATRICES_OPEN_QUESTIONS_AND_LIMITS.md
```

If relationship material exceeds a reasonable size, split Document 12 into two volumes and shift later numbering. The architecture is semantic, not numerologically fixed.

---

# 16. Source-facing artifact catalog

These are not necessarily intended for casual reading but are mandatory research infrastructure.

## Shared/institutional

- `GKM_SHARED_AND_INSTITUTIONAL_SPINE_DEEP_READING.md`
- `GKM_CONTINUITY_AND_STORY_STATE_MAP.md`

## Character-core

- 13 `GKM_CORE_XX_*` documents.

## Event tranches

- 4+ event deep-reading documents.

## Support tranches

- 8 support-card deep-reading documents following current bundle segmentation.

## Relationship synthesis

- 2+ relationship-system documents.

## AV close readings

Store only when substantial enough to justify durable artifacts, for example:

```text
GKM_AV_SAKI_FOUNDATIONAL_MV_ANALYSIS.md
GKM_AV_TEMARI_KEY_DIALOGUE_SCENE_01.md
GKM_AV_REVERSI_MUSICAL_DRAMATURGY.md
```

Minor AV observations can remain in ledgers and be absorbed into monographs.

---

# 17. Phase update protocol

After every source-facing tranche:

1. update character-state ledger;
2. update relationship-state ledger;
3. update continuity ledger;
4. update branch ledger where relevant;
5. update institution ledger;
6. update theme/motif ledger;
7. update NPC ledger;
8. update source locator ledger;
9. add AV requests;
10. update legacy-claim ledger if evidence materially changes an inherited interpretation.

Do not postpone ledger maintenance until the end of a phase; that recreates context-loss risk.

---

# 18. Character delta protocol

Every new source block should record whether it:

- **CONFIRMS** current model;
- **EXTENDS** current model;
- **COMPLICATES** current model;
- **CONTRADICTS** current model;
- **BRANCH-LIMITS** current model;
- **RESOLVES** prior ambiguity.

This delta vocabulary allows later reconstruction of how the interpretation developed.

---

# 19. Audiovisual request workflow

The analyst—not the user—owns the translation from repository nomenclature to publicly searchable media. Internal filenames are provenance keys; the user-facing acquisition layer must use the terminology by which Japanese uploaders actually title the material.

## 19.1 Default commu nomenclature crosswalk

| Internal family | User-facing retrieval vocabulary | Strong secondary anchor |
| --- | --- | --- |
| `adv_dear_*` | `親愛度コミュ` | STEP, chapter number/range/title |
| `adv_cidol_*` | `アイドルコミュ`; song-linked material should normally use `楽曲コミュ` | song/P-idol title, part |
| `adv_pstory_*` | `プロデュースコミュ` | `初`, `N.I.A`, `H.I.F`, result/route state |
| `adv_pevent_*` | subtype such as `育成コミュ`, `おでかけコミュ`, `営業コミュ` | scenario/title/character |
| `adv_csprt_*` | `サポートコミュ` | support-card title |
| `adv_event_*` | `イベントコミュ` | event title |
| unit-story material | `初星コミュ` when used publicly | unit/story title, episode |
| live/performance | song title + `MV` / `3DMV` / `ライブ` | character/version |

This table is a retrieval aid, not a rewrite of the source taxonomy.

## Step 1 — Identify transcript object

Record the internal source ID/path, story-state label, source family, and the exact analytical question.

## Step 2 — Resolve the human-facing identity

Determine, in order of usefulness:

- Japanese character name;
- public commu family;
- official chapter/card/song/event title;
- STEP/chapter/episode range;
- route/state label (`N.I.A`, `H.I.F`, etc.);
- community/uploader shorthand.

Do not lead with a machine filename such as `adv_dear_hski_027`.

## Step 3 — Generate optimized search terms

Create at least one copy-paste-ready Japanese query. Preferred forms include:

- `学マス [キャラ名] 親愛度コミュ21～27 STEP3`
- `学マス [楽曲名] [キャラ名] 楽曲コミュ`
- `学マス [キャラ名] 親愛度コミュ28～37 H.I.F STEP4`
- `学マス [サポートカード名] サポートコミュ`
- `学マス [イベント名] イベントコミュ`

For difficult objects provide two or three fallback queries. Distinctive dialogue strings are fallback discriminators, not the default search strategy, because public-video indexing is usually title-driven.

## Step 4 — Group requests by whole public artifact

Before asking the user for files, determine whether several AVQ entries are contained in one:

- whole commu;
- STEP/chapter compilation;
- support-card story;
- event-story compilation;
- complete song commu.

If so, collapse them into one retrieval target and list every AVQ ID it covers. This minimizes user retrieval work and preserves context.

## Step 5 — Emit the retrieval packet

For each requested whole artifact provide:

- **human-facing retrieval name**;
- **primary Japanese search term**;
- **fallback searches** if needed;
- **internal crosswalk ID(s)**;
- **covered AVQ scenes**;
- **story state**;
- **why the media matters**;
- **priority**;
- **instruction that the whole commu is preferred and clipping is unnecessary**.

Dialogue commus at 720p are normally sufficient if the audio is intact and expressions, gestures, camera changes, and on-screen text remain legible. Higher resolution is more valuable for detailed MV/costume/lighting analysis.

## Step 6 — Acquire raw media

The user locates/downloads/uploads the whole artifact. Do not ask the user to perform manual editing merely to isolate the requested scene.

## Step 7 — Inspect, timestamp, and record

The analyst is responsible for:

- finding the requested scene inside the supplied whole video;
- recording useful timestamps;
- aligning it to the exact raw ADV script;
- classifying AV evidence;
- documenting voice/BGM/staging/camera observations;
- recording changed interpretations;
- updating the crosswalk with the exact supplied artifact identity.

This workflow prevents machine transcript nomenclature from becoming a practical retrieval barrier while preserving full provenance.

# 20. Musical baseline workflow

For each character:

## Stage A — Inventory

Collect known image songs/solos/unit songs and metadata.

## Stage B — Initial selection

Choose approximately 3 works covering identity, contrast, development.

## Stage C — Raw AV inspection

User supplies requested audio/video.

## Stage D — Sonic identity profile

Record:

- composition;
- arrangement;
- vocal delivery;
- lyrical persona;
- MV/stage persona;
- relation to character model.

## Stage E — Expansion audit

Before definitive monograph, determine whether additional works are needed.

## Stage F — Full musical synthesis

Document 11 integrates cross-character comparison.

---

# 21. Reader-facing versus apparatus rule

The final corpus should not overwhelm the reader with every research operation.

Reader-facing documents should contain:

- mature argument;
- necessary evidence;
- Japanese examples where meaningful;
- concise source locators;
- uncertainty/counterevidence.

Apparatus stores:

- exhaustive source mapping;
- duplicate tracking;
- participant indexes;
- full claim revision history;
- AV request queue;
- raw metadata.

This separation makes the project both rigorous and readable.

---

# 22. Naming conventions

## Source-facing

Prefix with `GKM_`.

Examples:

- `GKM_CORE_01_HANAMI_SAKI.md`
- `GKM_EVENTS_001_005_DEEP_READING.md`
- `GKM_SUPPORT_SERIES_03_PART_026_050_DEEP_READING.md`

## Final reader-facing

Use stable two-digit numeric prefixes.

## Ledgers

Use descriptive uppercase names and structured formats where useful.

Avoid ambiguous versions such as `final_final_v3`.

Use explicit version metadata inside files.

---

# 23. Provenance requirements

Every emitted analytical artifact should record at minimum:

- project;
- document type;
- version;
- source lock;
- creation date;
- sources covered;
- continuity scope;
- whether AV evidence was used;
- relationship to governing method.

Major artifacts should also identify:

- prior document superseded, if any;
- downstream documents affected;
- unresolved AV requests.

---

# 24. Quality-control gates

## Gate A — Source control

Before Phase 1:

- inventory complete;
- source lock frozen;
- dedup rules fixed.

## Gate B — Continuity control

Before Phase 3:

- major story states mapped;
- branch ontology operational.

## Gate C — Character-core completeness

Before Phase 4:

- all 13 provisional core models exist.

## Gate D — Ensemble completeness

Before Phase 7:

- events complete;
- support cards complete;
- major relationships synthesized;
- side-character search performed.

## Gate E — Audiovisual sufficiency

Before each final character monograph:

- initial musical baseline inspected;
- required sonic expansion assessed;
- all active P0/P1 requests have human-facing commu identities and optimized Japanese search terms;
- multiple requested scenes are grouped into whole-commu retrieval targets where possible;
- acquired whole videos are timestamp-aligned to internal source IDs;
- P0 dialogue AV resolved;
- central P1 requests resolved where feasible.

## Gate F — Synthesis readiness

Before Documents 01–12:

- definitive character monographs substantially stable;
- major ledgers mature;
- adversarial questions identified.

## Gate G — Release

Before final package:

- legacy reconciliation complete;
- provenance checked;
- source locators functional;
- README written last;
- checksums/manifests generated where practical.

---

# 25. What not to do

The project must not:

- read every bundle as a single linear transcript;
- count duplicate bundle appearances as independent evidence;
- treat support cards as disposable filler;
- infer sound from filenames;
- infer vocal emotion from text when delivery is interpretation-critical;
- assume true-labeled branch means singular canon without evidence;
- collapse every Producer choice into one coherent personality;
- use prior chat analysis as primary evidence;
- finalize themes before counterevidence testing;
- produce definitive character monographs before ensemble evidence;
- bury source provenance inside prose only;
- silently incorporate post-lock live-service content.

---

# 26. Expected project scale

The project is intentionally larger than a conventional review but smaller and more disciplined than an exhaustive transcript commentary.

The final reader-facing layer should resemble a **book-length scholarly companion**, while the source-facing and ledger layers form a research apparatus underneath it.

The architecture optimizes for:

- recoverability;
- source traceability;
- long-term reuse;
- future hypothetical character-scenario reconstruction;
- reliable comparison with other works in the broader Manga and anime discussions corpus.

---

# 27. Final architectural principle

The project should always be able to answer two questions:

> **Why do we believe this about Gakumas?**

and

> **Where, exactly, can we go in the source to test it?**

Every phase, ledger, crosswalk, audiovisual request, character monograph, and thematic synthesis exists to preserve those two capabilities while allowing the final corpus to remain readable.

The architecture is therefore complete only when the final human-readable interpretation and the underlying evidentiary machinery remain connected.

# 20. Mandatory next-step and model/reasoning routing

Every phase-level or tranche-level completion report must end with a section titled:

`Next step and model/reasoning recommendation`

It must state:

1. the next architecture-defined textual or synthesis step;
2. any audiovisual, indexing, or retrieval work that can proceed in parallel;
3. the recommended model;
4. the recommended reasoning level where the selected model exposes one;
5. a concise explanation tied to the actual integration burden.

## 20.1 Default routing

| Work type | Default recommendation |
| --- | --- |
| manifest inspection, source extraction, title crosswalks, search-term construction, checksums, packaging, citation QA | GPT-5.6 Sol — Extra High |
| one bounded event/support tranche | GPT-5.6 Sol — Extra High |
| one isolated song, MV, or commu close reading | GPT-5.6 Sol — Extra High |
| provisional character-core reading with limited branch interaction | GPT-5.6 Sol — Extra High, with Pro review if the result feeds a major synthesis |
| character core spanning incompatible routes, distributed relationship history, or institutional/title-state conflicts | GPT-5.6 Pro |
| integrated audiovisual baseline combining several songs, MVs, dialogue performances, and the textual model | GPT-5.6 Pro |
| relationship-system synthesis, definitive character monograph, institutional/theme document, full-series synthesis, adversarial reconciliation | GPT-5.6 Pro |

Model choice follows **integration complexity**, not word count alone. A long but mechanically bounded inventory can remain a Sol Extra High task. A shorter judgment that reconciles several incompatible story states, relationship perspectives, or evidence modes may require Pro.

## 20.2 Character-pass footer

Each Phase-3 character report must separately identify:

- the next textual character;
- whether the completed character has an active AV acquisition packet;
- the model/reasoning recommendation for retrieval and isolated AV readings;
- the recommendation for the integrated AV baseline;
- whether later events/support cards must reopen the model.

## 20.3 No implication of evidentiary rank

The chosen model or reasoning level is workflow metadata, not evidence. A claim remains valid only through source support, continuity discipline, counterevidence, and traceable locators.

