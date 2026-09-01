---
series: OPM
series_title: One Punch Man
series_title_jp: ワンパンマン
artifact_type: synthesis_architecture
scope: Manga V2; open-ended architecture beginning with Japanese tankobon V01 and extending through the latest reconciled collected boundary plus continuing serialization
generation: V2
status: active_provisional
source_boundary: Architecture is designed to extend beyond the current collected boundary without creating a parallel project
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
created: 2026-08-15
last_amended: 2026-08-24
---

# One Punch Man — V2 Multi-Document Synthesis Architecture
## Canonical architecture for a long, revision-prone, still-publishing manga

# 1. Architectural objective

The V2 corpus should solve a different problem from the existing One Punch Man analysis.

The earlier corpus contains strong broad synthesis and specialist character/thematic documents through Volume 34. Its weakness is not lack of insight. Its weakness is that it grew conversationally and comparatively rather than as a source-locked, sequential, revision-aware archival system.

V2 should therefore convert One Punch Man into a corpus with:

- one canonical root;
- one current entrypoint;
- Japanese tankobon as the stable primary spine;
- a distinct provisional current-release layer;
- sequential volume readings;
- longitudinal ledgers;
- specialist topical homes;
- evidence and revision infrastructure;
- a cumulative synthesis with an explicit boundary;
- legacy preservation;
- repeatable new-volume reconciliation.

The architecture must be able to continue beyond the currently available collected boundary without renaming the project or creating a V3 merely because new chapters or volumes appear.

---

# 2. Proposed canonical directory tree

```text
One Punch Man/
├── CURRENT_STATE_AND_CORPUS_MAP.md
│
├── 00 Frameworks and Methods/
│   ├── OPM_ANALYTICAL_METHOD_V2.md
│   ├── OPM_SYNTHESIS_ARCHITECTURE_V2.md
│   ├── OPM_CHARACTER_MODELING_SCHEMA.md
│   └── OPM_V1_TO_V2_AUTHORITY_AND_MIGRATION_POLICY.md        [emit in Phase 0 if needed]
│
├── 01 Source Lock and Inventory/
│   ├── OPM_SOURCE_INVENTORY_AND_LOCK.md
│   ├── OPM_TANKOBON_CHAPTER_CROSSWALK.md
│   ├── OPM_WEB_SERIALIZATION_AND_REVISION_CROSSWALK.md
│   ├── OPM_SOURCE_CHECKSUMS.sha256
│   └── OPM_SOURCE_PROVENANCE_NOTES.md
│
├── 02 Sequential Readings/
│   ├── OPM_V01_DEEP_READING.md
│   ├── OPM_V02_DEEP_READING.md
│   ├── ...
│   └── OPM_VXX_DEEP_READING.md                               [future volumes continue here]
│
├── 03 Longitudinal Ledgers and Checkpoints/
│   ├── Checkpoints/
│   │   ├── OPM_V01-VXX_CHECKPOINT.md
│   │   └── ...
│   ├── Character State/
│   │   ├── OPM_SAITAMA_CHARACTER_STATE_LEDGER.md
│   │   ├── OPM_HERO_CHARACTER_STATE_LEDGER.md
│   │   ├── OPM_MONSTER_ANTAGONIST_CHARACTER_STATE_LEDGER.md
│   │   └── OPM_INDEPENDENT_CIVILIAN_CHARACTER_STATE_LEDGER.md
│   ├── OPM_RELATIONSHIP_STATE_LEDGER.md
│   ├── OPM_CHARACTER_MODEL_READINESS_INDEX.md
│   ├── OPM_HEROISM_RECOGNITION_RANK_AND_INSTITUTION_LEDGER.md
│   ├── OPM_MONSTERHOOD_PERSONHOOD_BODY_AND_TRANSFORMATION_LEDGER.md
│   ├── OPM_POWER_TECHNIQUE_LIMITER_GOD_AND_COSMIC_LEDGER.md
│   ├── OPM_TECHNOLOGY_ORGANIZATION_AND_HIDDEN_ACTORS_LEDGER.md
│   ├── OPM_SATIRE_GENRE_AND_PUBLIC_NARRATIVE_LEDGER.md
│   ├── OPM_VISUAL_FORM_MOTIF_AND_REDRAW_LEDGER.md
│   └── OPM_OPEN_QUESTIONS_AND_MYSTERY_LEDGER.md
│
├── 04 Specialist Synthesis/
│   ├── Core/
│   │   ├── OPM_SAITAMA_CHARACTER_AND_PHILOSOPHY.md
│   │   ├── OPM_GENOS_CHARACTER_TECHNOLOGY_AND_DISCIPLESHIP.md
│   │   ├── OPM_HEROISM_RECOGNITION_REPUTATION_AND_PUBLIC_TRUTH.md
│   │   ├── OPM_HERO_ASSOCIATION_NEO_HEROES_AND_INSTITUTIONAL_LEGITIMACY.md
│   │   ├── OPM_MONSTERHOOD_PERSONHOOD_AND_TRANSFORMATION.md
│   │   ├── OPM_POWER_TECHNIQUE_LIMITER_GOD_BLAST_AND_COSMIC_ONTOLOGY.md
│   │   ├── OPM_SATIRE_COMEDY_BATTLE_MANGA_AND_SUPERHERO_GENRE.md
│   │   └── OPM_MURATA_VISUAL_GRAMMAR_SCALE_MOTION_BODY_AND_REDRAW.md
│   └── Conditional/
│       ├── OPM_GAROU_CHARACTER_IDEOLOGY_AND_MARTIAL_INHERITANCE.md
│       ├── OPM_KING_REPUTATION_COURAGE_AND_SOCIAL_POWER.md
│       ├── OPM_TATSUMAKI_FUBUKI_POWER_PROTECTION_AND_SISTERHOOD.md
│       ├── OPM_BANG_GAROU_AND_MARTIAL_LINEAGE.md
│       ├── OPM_SAITAMA_SOCIAL_ORBIT_RELATIONSHIPS_AND_ORDINARY_LIFE.md
│       ├── OPM_TECHNOLOGY_METAL_KNIGHT_DRIVE_KNIGHT_ORGANIZATION_AND_GENOS.md
│       └── ...                                               [only when distinct responsibility exists]
│
├── 05 Cumulative Series Synthesis/
│   └── OPM_CUMULATIVE_SERIES_SYNTHESIS_THROUGH_VXX.md         [future collected boundary]
│
├── 06 Evidence and Indexes/
│   ├── OPM_V1_TO_V2_CLAIM_REVISION_LEDGER.md
│   ├── OPM_EVIDENCE_MATRIX.md
│   ├── OPM_PRIMARY_SOURCE_LOCATOR_INDEX.md
│   ├── OPM_CHARACTER_AND_RELATIONSHIP_CROSSWALK.md
│   ├── OPM_JAPANESE_TERMINOLOGY_AND_VOICE_INDEX.md
│   ├── OPM_TANKOBON_WEB_CROSSWALK.md
│   └── OPM_SYNTHESIS_TO_EVIDENCE_CROSSWALK.md
│
├── 07 Current Release/
│   ├── OPM_CURRENT_RELEASE_SOURCE_LOCK.md
│   ├── OPM_UNCOLLECTED_RELEASE_LEDGER.md
│   ├── OPM_WEB_<RANGE>_DEEP_READING.md
│   ├── OPM_CURRENT_RELEASE_SYNTHESIS.md
│   └── Historical Web States/
│       └── ...
│
├── 08 Audits and Manifests/
│   ├── OPM_CORPUS_MANIFEST.md
│   ├── OPM_AUTHORITY_AND_SUPERSESSION_AUDIT.md
│   ├── OPM_DUPLICATION_AND_CROSS_REFERENCE_AUDIT.md
│   ├── OPM_ARTIFACT_CHECKSUMS.sha256
│   └── Frozen Boundary Releases/
│       ├── VXX_BOUNDARY/                  [latest explicitly frozen collected boundary]
│       └── VXX_BOUNDARY/
│
└── 90 Legacy and Superseded/
    ├── V1 Analysis/
    │   ├── One Punch Man Through Volume 34 ...
    │   ├── Saitama Deep Dive ...
    │   ├── Genos Deep Dive ...
    │   ├── Garou Deep Dive ...
    │   ├── King Deep Dive ...
    │   ├── Tatsumaki Deep Dive ...
    │   ├── Bang Deep Dive ...
    │   └── satire / relationships / other V1 documents
    └── Conversation Archives/
```

This tree is a starting architecture, not a requirement to create empty directories or empty files. A folder/document should exist only once it serves a real analytical role.

---

# 3. Canonical entrypoint

While the manga is active, the first-read file should be:

`CURRENT_STATE_AND_CORPUS_MAP.md`

It should answer, in one place:

- latest locked tankobon boundary;
- latest analyzed tankobon boundary;
- current uncollected web boundary;
- current authority generation;
- completed volume deep readings;
- current checkpoint;
- active ledgers;
- completed specialist syntheses;
- current cumulative synthesis;
- V1 legacy location;
- outstanding source/reconciliation gaps;
- next architecture-defined step.

Do not rename this file every time a chapter is published.

When the manga eventually ends and the final source boundary is reconciled, the project may transition to `00_README_AND_CORPUS_MAP.md` and a frozen full-series release.

---

# 4. Authority model

## 4.1 Collected manga

`canonical`

A tankobon deep reading becomes current authority for its collected material after source lock and QC.

## 4.2 Uncollected official web manga

`active_provisional`

It is current evidence, but subject to redraw, rewrite, reordering, or tankobon change.

## 4.3 Replaced web versions

`historical_legacy` or `superseded`

Preserve for revision analysis. Do not use as current continuity authority.

## 4.4 V1 analytical corpus

`historical_legacy`

Preserve its materially distinct reasoning. Route every reused claim through V2 claim revision.

---

# 5. Phase architecture

## Phase 0 — source audit, corpus map, and migration control

### Purpose

Establish the exact source state before rereading.

### Required outputs

- `CURRENT_STATE_AND_CORPUS_MAP.md`
- `OPM_SOURCE_INVENTORY_AND_LOCK.md`
- `OPM_TANKOBON_CHAPTER_CROSSWALK.md`
- `OPM_WEB_SERIALIZATION_AND_REVISION_CROSSWALK.md`
- `OPM_V1_TO_V2_CLAIM_REVISION_LEDGER.md`

### Phase 0 questions

- What is the current available Japanese tankobon boundary, and are all volumes through that audited boundary present and readable?
- Which extras/bonus chapters belong to each volume?
- What is the exact chapter numbering used inside each book?
- Which uncollected official web installments are currently authoritative?
- Which web installments have known replaced/redrawn versions?
- Which V1 documents contain claims worth explicitly migrating?
- Which claims depend on material only analyzed broadly rather than with page-level evidence?

Do not finalize checkpoint boundaries until this source map exists.

---

# 6. Sequential reading phase

The project should reread **every tankobon from V01 forward**.

Do not treat V01–V34 as “already done” merely because V1 produced a synthesis through Volume 34. The V2 objective is longitudinal source traceability.

Canonical filename:

`OPM_VXX_DEEP_READING.md`

The volume artifact is the primary analytical unit because tankobon is the stable canonical collection boundary.

Chapter-level analysis belongs inside the volume unless a specific chapter is so large or revision-complex that it requires a distinct evidence appendix.

---

# 7. Checkpoint architecture

Rather than forcing identical three-volume blocks, use **adaptive checkpoints**.

Create a checkpoint when either:

- 4–6 volumes have accumulated; or
- a major narrative boundary makes a different grouping analytically superior.

A plausible initial planning map is:

- **Checkpoint A:** early premise / institutional entry / Boros-era foundation;
- **Checkpoint B:** King–Fubuki–Garou emergence / Super Fight / Monster Association formation;
- **Checkpoint C:** Monster Association expansion and early raid state;
- **Checkpoint D:** raid escalation / psychic and institutional exposure;
- **Checkpoint E:** late Monster Association collapse;
- **Checkpoint F:** Cosmic Garou / zero-punch aftermath;
- **Checkpoint G:** post-Garou collected transition through the latest relevant reconciled boundary.

Exact volume boundaries should be set only after Phase 0 reconstructs the volume/chapter map.

Checkpoint filenames should encode actual scopes, for example:

`OPM_V01-V06_CHECKPOINT.md`

not vague names such as `Checkpoint 1 Final.md`.

---

# 8. Longitudinal ledgers as the project's memory

The ledgers are what keep a multi-dozen-volume project from becoming a pile of isolated readings.

They should be updated after each volume, but only with material state changes.

A ledger is not a second summary of the volume. It is a cumulative record of one analytical dimension.

The nine recommended ledgers are:

1. Saitama meaning/affect/relationships.
2. Heroism/recognition/rank/institution.
3. Monsterhood/personhood/body/transformation.
4. Power/technique/limiter/God/cosmic.
5. Ensemble character/relationship states.
6. Technology/Organization/hidden actors.
7. Satire/genre/public narrative.
8. Visual form/motifs/redraws.
9. Open questions/mystery state.

If two ledgers prove persistently redundant after several volumes, merge them deliberately and update the corpus map. Do not preserve unnecessary complexity for symmetry.

---

# 9. Specialist synthesis architecture

The specialist layer should be written after enough V2 evidence accumulates, not copied immediately from V1.

## 9.1 Core specialist documents

These are likely to justify independent canonical homes because they span the whole work.

### `OPM_SAITAMA_CHARACTER_AND_PHILOSOPHY.md`

Primary responsibility:

- post-growth protagonist structure;
- boredom and meaning;
- ordinary life;
- ethics;
- recognition;
- attachment;
- hero identity;
- how later relationships change the original premise.

### `OPM_GENOS_CHARACTER_TECHNOLOGY_AND_DISCIPLESHIP.md`

Primary responsibility:

- revenge and reconstruction;
- growth logic;
- mechanical body;
- Saitama relationship;
- recognition/witness function;
- technological mystery.

### `OPM_HEROISM_RECOGNITION_REPUTATION_AND_PUBLIC_TRUTH.md`

Primary responsibility:

- Saitama/King inversion;
- public judgment;
- celebrity heroism;
- moral versus sociological legitimacy;
- credit, rank, symbols, and misrecognition.

### `OPM_HERO_ASSOCIATION_NEO_HEROES_AND_INSTITUTIONAL_LEGITIMACY.md`

Primary responsibility:

- professionalization of heroism;
- classification;
- bureaucracy;
- donor/elite influence;
- organizational failure;
- successor/rival institutions;
- civil-military-like command and legitimacy questions.

### `OPM_MONSTERHOOD_PERSONHOOD_AND_TRANSFORMATION.md`

Primary responsibility:

- what “monster” means across bodies, actions, labels, desire, biology, technology, divine power, and social identity;
- cases that destabilize hero/monster binaries.

### `OPM_POWER_TECHNIQUE_LIMITER_GOD_BLAST_AND_COSMIC_ONTOLOGY.md`

Primary responsibility:

- competing explanations of strength;
- limiter discourse;
- copying/adaptation;
- God-granted power;
- Blast/cubes/dimensional layer;
- where the text remains deliberately unresolved.

### `OPM_SATIRE_COMEDY_BATTLE_MANGA_AND_SUPERHERO_GENRE.md`

Primary responsibility:

- satire targets;
- genre affection versus critique;
- anticlimax;
- battle escalation;
- power-scaling;
- bureaucratic comedy;
- public narrative;
- ordinary-life deflation.

### `OPM_MURATA_VISUAL_GRAMMAR_SCALE_MOTION_BODY_AND_REDRAW.md`

Primary responsibility:

- manga form;
- kinetic sequencing;
- scale;
- page architecture;
- body design;
- gag/spectacle switching;
- grotesquerie;
- revision/redraw aesthetics.

## 9.2 Conditional specialist documents

These should be created only if the V2 evidence load warrants independent retrieval.

Likely candidates:

- Garou;
- King;
- Tatsumaki/Fubuki;
- Bang/Garou and martial lineage;
- Saitama's social orbit;
- technology/Organization/Metal Knight/Drive Knight;
- Amai Mask and beauty/personhood/public image;
- Child Emperor and adult institutional use of children;
- Neo Heroes as a separate political/institutional synthesis if the arc grows large enough.

The mature corpus should aim for **one current artifact per semantic responsibility**.

---

# 10. Cumulative synthesis architecture

While the manga is ongoing, use a boundary-qualified cumulative synthesis.

At any explicitly reconciled collected boundary, use a boundary-qualified filename such as:

`OPM_CUMULATIVE_SERIES_SYNTHESIS_THROUGH_VXX.md`

It should synthesize V2 findings without pretending the work is complete.

Its likely sections include:

1. current collected-boundary thesis;
2. narrative architecture through the declared collected boundary;
3. Saitama and post-growth heroism;
4. ensemble inheritance of battle-manga drama;
5. heroism, recognition, reputation, and rank;
6. Hero Association and institutional legitimacy;
7. monsterhood and personhood;
8. power systems and explanatory failure;
9. God/Blast/cosmic layer;
10. technology and hidden actors;
11. relationship/social-orbit development;
12. comedy and satire;
13. visual form and Murata's manga grammar;
14. Japanese-language findings;
15. V1 claims preserved/revised/rejected;
16. open questions at the collected boundary.

Do not append uncollected web developments directly into this canonical collected synthesis.

Instead use:

`OPM_CURRENT_RELEASE_SYNTHESIS.md`

with `status: active_provisional`.

---

# 11. Current-release architecture

`07 Current Release` is not an afterthought. It is a permanent part of the project while serialization continues.

## Required living files

### `OPM_CURRENT_RELEASE_SOURCE_LOCK.md`

Lists the exact official installments currently beyond the tankobon boundary.

### `OPM_UNCOLLECTED_RELEASE_LEDGER.md`

Tracks:

- provider update ID;
- display label;
- date;
- category;
- narrative content scope;
- revision state;
- analysis artifact;
- likely but unconfirmed tankobon destination;
- current authority.

### `OPM_WEB_<RANGE>_DEEP_READING.md`

Used for coherent tranches of uncollected material.

### `OPM_CURRENT_RELEASE_SYNTHESIS.md`

A compact provisional synthesis of what the uncollected material changes relative to the latest tankobon boundary.

It should answer:

- which collected-boundary claims are strengthened or threatened;
- which character/institution states changed;
- which mysteries moved;
- what remains vulnerable to redraw/tankobon revision.

---

# 12. New-volume reconciliation architecture

Every new tankobon release is a controlled migration event.

Suppose Volume 38 releases.

The workflow is:

1. add V38 to the source inventory and checksum lock;
2. determine its precise chapter/extra contents;
3. crosswalk V38 against the web current-release layer;
4. record significant changes;
5. produce `OPM_V38_DEEP_READING.md` from the book;
6. update ledgers;
7. adjudicate provisional web claims;
8. archive superseded web-state artifacts without deleting provenance;
9. revise the current cumulative synthesis to `THROUGH_V38` only when the V38 reading and reconciliation are complete;
10. update `CURRENT_STATE_AND_CORPUS_MAP.md`;
11. optionally freeze a V38 boundary release under `08 Audits and Manifests/Frozen Boundary Releases/`.

This prevents the project from splintering into “V2 2026,” “V2.5,” “new chapters analysis,” or other parallel roots.

---

# 13. Evidence and revision infrastructure

## `OPM_V1_TO_V2_CLAIM_REVISION_LEDGER.md`

Routes legacy conclusions into current authority.

## `OPM_EVIDENCE_MATRIX.md`

Indexes load-bearing evidence by theme/character/institution.

## `OPM_PRIMARY_SOURCE_LOCATOR_INDEX.md`

Provides deterministic page/panel routing.

## `OPM_TANKOBON_WEB_CROSSWALK.md`

Critical OPM-specific artifact. It must keep provider update numbering separate from tankobon chapter numbering.

## `OPM_SYNTHESIS_TO_EVIDENCE_CROSSWALK.md`

For major synthesis claims, records:

- claim ID;
- synthesis home;
- ledger/specialist home;
- supporting deep readings;
- primary locators;
- current status;
- counterevidence.

---

# 14. Legacy migration

The existing V1 work should be preserved, not discarded.

The legacy layer likely includes:

- Volumes 1–15 broad synthesis;
- through-Volume-34 comprehensive synthesis;
- Saitama deep dive;
- Genos deep dive;
- Garou deep dive;
- King deep dive;
- Tatsumaki deep dive;
- Bang deep dive;
- Saitama relationship reference;
- satire reference;
- other comparative documents.

Their role after V2 begins is:

- provenance;
- claim seed bank;
- comparison of analytical generations;
- recovery of useful hypotheses;
- evidence of what the first pass noticed or missed.

They should carry a warning:

> Historical V1 analytical material. Preserve for provenance and claim comparison. Do not prefer over V2 canonical artifacts where V2 has adjudicated the same issue.

---

# 15. Suggested V2 production sequence

## Phase 0

Source lock, crosswalk, current-state map, V1 claim ledger.

## Phase 1A onward

Sequential `V01`, `V02`, `V03` ... readings.

Do not batch multiple volumes into one artifact unless a source defect makes separate volume treatment impossible.

## Rolling checkpoints

Every approximately 4–6 volumes or at strong arc boundaries.

## Ledger stabilization

Update throughout; audit after each checkpoint.

## Specialist synthesis

Begin once the relevant evidence base is mature enough that a topical home improves retrieval. Saitama and institutional recognition will likely mature earlier than some hidden-actor/cosmic documents.

## Collected-boundary synthesis

Write a boundary synthesis only after every volume through that declared boundary has been re-read under V2 and the cumulative ledgers have been reconciled.

## Current release

Then ingest the uncollected official web layer as `active_provisional`.

This ordering is preferable to analyzing current chapters first because the V2 project is intended to rebuild longitudinal meaning, not only catch up on plot.

---

# 16. Reasoning-strength recommendations

For GPT-5.6 Sol:

- **Phase 0 source inventory/crosswalk:** medium to high; use high when reconciling conflicting chapter/revision identities.
- **Individual volume deep reading:** high.
- **Checkpoint:** high.
- **Routine ledger maintenance:** medium, escalating to high when a claim materially changes.
- **Visual/redraw comparison:** high.
- **Specialist character/thematic synthesis:** high.
- **Cumulative series synthesis:** high.
- **Minor current-release update note:** medium.
- **Major current-release revelation or institutional/ontology shift:** high.
- **Tankobon reconciliation after redraws:** high.

The expensive reasoning should be concentrated on interpretation, revision, visual causality, and synthesis rather than simple source inventory.

---

# 17. Definition of a successful V2 corpus

The project is succeeding if a future reader can ask any of the following and get a deterministic answer:

- What did Volume 12 establish at the time?
- When did Garou's self-concept materially change?
- Which evidence supports the claim that Saitama's social attachments matter more over time?
- Is King actually brave, or only lucky?
- How has the manga's concept of “monster” changed?
- What does the latest tankobon say about the Hero Association versus Neo Heroes?
- Which current web claims are not yet stable?
- Was this scene redrawn before tankobon collection?
- Did V1 overstate or understate Tatsumaki's controlling protection?
- Where is the Japanese page supporting a specific claim?
- What is the latest canonical synthesis boundary?

If the answer requires searching old chats or guessing which of several “final” documents is newest, the architecture has failed.

---

# 18. Governing architectural rule

*One Punch Man* should have one continuing V2 corpus, not a new project every time publication advances.

Its durable architecture is:

> **source-locked tankobon sequence → adaptive checkpoints → longitudinal ledgers → specialist synthesis → boundary-qualified cumulative synthesis**
>
> plus
>
> **a separately governed active-provisional web layer that is reconciled at every new tankobon release.**

That is the structure most likely to remain coherent if the manga grows from 37 volumes to 45, 50, or beyond.


---

# 16. Character modeling and reconstruction architecture amendment

## 16.1 Architectural purpose

The V2 corpus has two coequal downstream uses of the same primary evidence:

1. literary/thematic synthesis; and
2. evidence-auditable conditional character reconstruction.

Character simulation is not a replacement for interpretation and is never itself canon. The architecture must preserve enough longitudinal behavioral evidence to model plausible perception, judgment, speech, relationships, and action without collapsing context into archetype.

## 16.2 Canonical character-modeling homes

Under `03 Longitudinal Ledgers and Checkpoints`, use the following character-centered surfaces:

```text
Character State/
├── OPM_SAITAMA_CHARACTER_STATE_LEDGER.md
├── OPM_HERO_CHARACTER_STATE_LEDGER.md
├── OPM_MONSTER_ANTAGONIST_CHARACTER_STATE_LEDGER.md
└── OPM_INDEPENDENT_CIVILIAN_CHARACTER_STATE_LEDGER.md
OPM_RELATIONSHIP_STATE_LEDGER.md
OPM_CHARACTER_MODEL_READINESS_INDEX.md
```

These coexist with the concept-centered heroism, monsterhood, power, technology, satire, visual-form, and mystery ledgers. Character ledgers answer `what is this person currently like and how do they behave?`; thematic ledgers answer `what is the work doing through these people and structures?`.

Do not duplicate full character models across thematic ledgers. Cross-reference the canonical home.

The cohort division is intentionally proportional. Add further splits only after recurring evidence load demonstrates a retrieval or maintenance need.

## 16.3 Dedicated framework artifact

`00 Frameworks and Methods/OPM_CHARACTER_MODELING_SCHEMA.md` is the canonical field/schema definition for character records, evidence atoms, state/trait classifications, relationship directionality, collected/provisional authority overlays, readiness, and validation.

The analytical method governs when evidence is collected; the schema governs how it is represented; the synthesis architecture governs where it lives.

## 16.4 Model-readiness layer

`OPM_CHARACTER_MODEL_READINESS_INDEX.md` must remain compact and auditable. Track breadth rather than popularity or thematic importance. A character may be thematically well understood yet remain unsuitable for broad novel-situation reconstruction.

## 16.5 Current-release overlay

Character state must preserve the existing OPM authority split:

- tankobon-derived model state = collected/canonical;
- uncollected official web evidence = `active_provisional` overlay;
- replaced/redrawn web evidence = superseded or historical revision evidence.

No provisional behavior claim should silently become part of the stable collected model.

## 16.6 Update manifests

Add `OPM_VXX_UPDATE_MANIFEST.md` to the per-volume archival workflow. The manifest records which cumulative ledgers/indexes changed, which readiness states changed, which source/claim/revision surfaces changed, and which expected surfaces legitimately received `NO CHANGE`.

This provides an auditable volume→ledger propagation path and prevents minor character evidence from being stranded inside sequential readings.

## 16.7 Character reconstruction dossiers

When a character reaches `specialist_ready`, a downstream dossier may be created under a distinct modeling/reconstruction home if the evidence load warrants it. Do not create empty dossiers in advance.

A mature dossier may synthesize:

- conditional behavior by context;
- relationship-conditioned variants;
- Japanese voice model;
- knowledge-state constraints;
- stress/failure regimes;
- predictive rules with alternatives and confidence;
- known counterexamples;
- held-out validation results.

Predictions remain epistemically separate from observational evidence.

## 16.8 Checkpoint validation

At major adaptive checkpoints, audit both literary state and model coverage. Where feasible, freeze a pre-scene model and validate against held-out later canon using only evidence available at the frozen chronology boundary. Retrospective `RR` knowledge must not leak into the prospective prediction.

## 16.9 Retrieval route for a character-modeling question

Use:

`CURRENT_STATE_AND_CORPUS_MAP.md` → `OPM_CHARACTER_MODEL_READINESS_INDEX.md` → owning character state ledger → `OPM_RELATIONSHIP_STATE_LEDGER.md` as needed → relevant volume deep reading/evidence atom → primary source locator → Japanese manga page/panel.

For uncollected material, insert the current-release overlay and web/revision crosswalk before treating the claim as usable.
