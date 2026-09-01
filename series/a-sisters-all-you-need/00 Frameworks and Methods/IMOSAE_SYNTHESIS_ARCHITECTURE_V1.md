---
series: IMOSAE
artifact_type: synthesis_architecture
scope: V01-V14_main_series_plus_labeled_supplements
generation: V1
status: canonical
source_boundary: Complete numbered Japanese light-novel main series; supplements separately tiered
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
version: '1.0'
date: '2026-08-18'
paired_with: IMOSAE_ANALYTICAL_METHOD_V1.md
---

# 妹さえいればいい。 / A Sister's All You Need
## Synthesis Architecture V1

## 0. Purpose

The analytical method answers:

> **How should the novels be read?**

This architecture answers:

> **Where does each kind of knowledge live, in what order is it produced, and how do later findings revise earlier ones without destroying provenance?**

Governing architectural principles:

1. **One canonical project root.** A new chat or later pass does not create a new corpus.
2. **One current entrypoint.** `CURRENT_STATE_AND_CORPUS_MAP.md` is the first-read file during active work.
3. **Sequential reading and retrospective synthesis are different products.**
4. **Every recurring analytical problem receives one primary topical home.**
5. **Later evidence revises earlier claims by delta, not silent retrofit.**
6. **Mainline and supplemental authority remain visibly distinct.**
7. **Architecture remains proportional.** Do not create a specialist document until enough evidence exists to justify independent retrieval.

Stable project identifier:

`IMOSAE`

Stable scope forms:

- `V01` … `V14`
- `V01-V03`
- `SUPP_DRAMA_V04`
- `SUPP_ARTBOOK`
- `ANIME_S1E01` if adaptation work is later added.

---

# I. Canonical project tree

```text
IMOSAE/
├── CURRENT_STATE_AND_CORPUS_MAP.md
│
├── 00 Frameworks and Methods/
│   ├── IMOSAE_ANALYTICAL_METHOD_V1.md
│   └── IMOSAE_SYNTHESIS_ARCHITECTURE_V1.md
│
├── 01 Source Lock and Inventory/
│   ├── IMOSAE_SOURCE_INVENTORY.md
│   ├── IMOSAE_SOURCE_LOCK.md
│   ├── IMOSAE_GAIJI_AND_TEXT_NORMALIZATION_REGISTER.md
│   ├── IMOSAE_ILLUSTRATION_AND_PARATEXT_INVENTORY.md
│   ├── IMOSAE_SUPPLEMENTAL_SOURCE_INVENTORY_AND_ACQUISITION_PLAN.md
│   └── machine_readable/
│       ├── source_manifest.json
│       ├── locator_index.jsonl
│       └── checksums.sha256
│
├── 02 Sequential Readings/
│   ├── IMOSAE_V01_DEEP_READING.md
│   ├── ...
│   ├── IMOSAE_V14_DEEP_READING.md
│   └── Checkpoints/
│       ├── IMOSAE_V01-V03_CHECKPOINT.md
│       ├── IMOSAE_V04-V06_CHECKPOINT.md
│       ├── IMOSAE_V07-V09_CHECKPOINT.md
│       ├── IMOSAE_V10-V12_CHECKPOINT.md
│       └── IMOSAE_V13-V14_END_STATE_CHECKPOINT.md
│
├── 03 Longitudinal Ledgers/
│   ├── IMOSAE_CHARACTER_AND_RELATIONSHIP_STATE_LEDGER.md
│   ├── IMOSAE_CREATIVE_LABOR_CAREER_AND_INDUSTRY_LEDGER.md
│   ├── IMOSAE_FAMILY_IDENTITY_AND_SIBLINGHOOD_LEDGER.md
│   ├── IMOSAE_JAPANESE_VOICE_STYLE_AND_TERMINOLOGY_LEDGER.md
│   ├── IMOSAE_FICTION_WITHIN_FICTION_GAMES_AND_INTERTEXT_LEDGER.md
│   ├── IMOSAE_VISUAL_PARATEXT_AND_ILLUSTRATION_LEDGER.md
│   ├── IMOSAE_OPEN_QUESTIONS_LEDGER.md
│   └── IMOSAE_CLAIM_REVISION_LEDGER.md
│
├── 04 Specialist Synthesis/
│   ├── IMOSAE_CREATIVE_LABOR_AUTHORSHIP_AND_LN_INDUSTRY_SPECIALIST_SYNTHESIS.md
│   ├── IMOSAE_TALENT_EFFORT_SUCCESS_FAILURE_AND_SELF_WORTH_SPECIALIST_SYNTHESIS.md
│   ├── IMOSAE_RELATIONSHIPS_INTIMACY_FRIENDSHIP_AND_ADULT_LIFE_SPECIALIST_SYNTHESIS.md
│   ├── IMOSAE_FAMILY_SIBLINGHOOD_AND_IDENTITY_SPECIALIST_SYNTHESIS.md
│   ├── IMOSAE_COMEDY_SEXUALITY_VULGARITY_AND_BOUNDARIES_SPECIALIST_SYNTHESIS.md
│   ├── IMOSAE_GAMES_TRPG_ALCOHOL_AND_SOCIAL_RITUAL_SPECIALIST_SYNTHESIS.md
│   ├── IMOSAE_NARRATION_JAPANESE_VOICE_AND_INTERTEXT_SPECIALIST_SYNTHESIS.md
│   ├── IMOSAE_ILLUSTRATION_PARATEXT_AND_MEDIA_REFLEXIVITY_SPECIALIST_SYNTHESIS.md
│   └── character_monographs/          # create only when justified
│
├── 05 Full-Series Synthesis/
│   ├── IMOSAE_FULL_SERIES_SYNTHESIS.md
│   ├── IMOSAE_CORE_CHARACTER_REFERENCE.md
│   └── IMOSAE_COMPARATIVE_REFERENCE_AND_OPEN_QUESTIONS.md
│
├── 06 Evidence and Indexes/
│   ├── IMOSAE_PRIMARY_SOURCE_LOCATOR_INDEX.md
│   ├── IMOSAE_VOLUME_BY_VOLUME_EVIDENCE_LEDGER.md
│   ├── IMOSAE_JAPANESE_PASSAGE_AND_TERMINOLOGY_INDEX.md
│   ├── IMOSAE_ILLUSTRATION_LOCATOR_INDEX.md
│   ├── IMOSAE_SUPPLEMENT_CROSSWALK.md
│   └── machine_readable/
│
├── 07 Current Release/
│   └── latest_frozen_or_review_candidate/
│
├── 08 Audits and Manifests/
│   ├── source_audits/
│   ├── locator_validation/
│   ├── contradiction_audits/
│   ├── duplication_audits/
│   ├── authority_audits/
│   ├── corpus_manifest/
│   └── release_checksums/
│
└── 90 Legacy and Superseded/
    └── Conversation Archives/
```

Do not create every empty directory immediately. The tree defines semantic homes; instantiate only what active work requires.

---

# II. Production phases

## Phase 0 — Source lock and normalized reading layer

### Required outputs

- `IMOSAE_SOURCE_INVENTORY.md`
- `IMOSAE_SOURCE_LOCK.md`
- `IMOSAE_GAIJI_AND_TEXT_NORMALIZATION_REGISTER.md`
- `IMOSAE_ILLUSTRATION_AND_PARATEXT_INVENTORY.md`
- machine-readable locator/checksum assets
- Phase-0 audit report under `08 Audits and Manifests/source_audits/`

### Completion criteria

Phase 0 is complete only when:

- 14/14 EPUB hashes are frozen;
- archive integrity is validated;
- colophon records are extracted;
- every spine item has a content class;
- ruby is preserved without duplicated reading text;
- gaiji are resolved or explicitly tokenized;
- typography relevant to analysis is retained;
- paragraph-level locators are stable;
- illustrations have anchors to prose;
- sampled round-trip validation passes.

No literary deep reading is canonical before this state.

---

## Phase 1 — Sequential volume deep readings

Produce:

`IMOSAE_V01_DEEP_READING.md` through `IMOSAE_V14_DEEP_READING.md`.

### Production order

1. V01
2. V02
3. V03
4. freeze V01–V03 checkpoint
5. V04
6. V05
7. V06
8. freeze V04–V06 checkpoint
9. V07
10. V08
11. V09
12. freeze V07–V09 checkpoint
13. V10
14. V11
15. V12
16. freeze V10–V12 checkpoint
17. V13
18. V14
19. freeze V13–V14 end-state checkpoint

### Why five checkpoints?

Fourteen volumes are long enough that a single end-of-series retrospective would lose the history of interpretation, but short enough that per-volume checkpoints would be redundant. Three-volume tranches preserve meaningful state transitions while keeping the corpus navigable.

### Sequential immutability rule

After canonicalization, a volume reading is immutable except for:

- factual correction;
- broken locator repair;
- metadata correction.

Later interpretive changes belong in:

- the next checkpoint;
- the claim revision ledger;
- specialist synthesis.

---

## Phase 2 — Longitudinal stabilization

This phase runs throughout Phase 1 but receives a formal consolidation after V14.

### Mandatory ledgers

#### `IMOSAE_CHARACTER_AND_RELATIONSHIP_STATE_LEDGER.md`

Owns:

- character state by volume;
- relationship state;
- trust/intimacy/conflict changes;
- who occupies central versus peripheral social roles;
- trajectory endpoints.

#### `IMOSAE_CREATIVE_LABOR_CAREER_AND_INDUSTRY_LEDGER.md`

Owns:

- publications/projects;
- editors;
- awards;
- adaptations;
- sales/career movement when textually established;
- deadlines and work process;
- professional successes/failures;
- institutional constraints.

#### `IMOSAE_FAMILY_IDENTITY_AND_SIBLINGHOOD_LEDGER.md`

Owns:

- literal family relations;
- disclosure/reclassification;
- sibling language;
- protagonist's sister fixation;
- family-versus-chosen-social-system pressures.

#### `IMOSAE_JAPANESE_VOICE_STYLE_AND_TERMINOLOGY_LEDGER.md`

Owns:

- character idiolect;
- names and address;
- professional jargon;
- recurrent lexical targets;
- difficult translation points;
- ruby-dependent meaning.

#### `IMOSAE_FICTION_WITHIN_FICTION_GAMES_AND_INTERTEXT_LEDGER.md`

Owns:

- internal fictional works;
- games/TRPGs;
- repeated references;
- professional analogies;
- transformed callbacks.

#### `IMOSAE_VISUAL_PARATEXT_AND_ILLUSTRATION_LEDGER.md`

Owns:

- covers;
- illustrations;
- publication emphasis;
- recurring visual framing;
- bonus/retailer visuals.

#### `IMOSAE_CLAIM_REVISION_LEDGER.md`

Owns every major thesis transition using:

- PRESERVE
- STRENGTHEN
- REVISE
- DOWNGRADE
- REJECT
- OPEN

### Evidence IDs

Recommended:

```text
IM-V01-E001
IM-V01-E002
...
IM-SUPP-ARTBOOK-E001
```

Evidence IDs are immutable once frozen.

---

## Phase 3 — Supplemental-source acquisition and source-facing readings

Begin semantic use only after the numbered-series end-state checkpoint is frozen.

### Objectives

- acquire high-value authorial supplements;
- distinguish additions from alternate-route/adaptation material;
- test mature mainline claims against supplemental evidence;
- recover creator commentary and visual material unavailable in the EPUBs.

### Outputs as needed

Examples:

- `IMOSAE_SUPP_ARTBOOK_SOURCE_READING.md`
- `IMOSAE_SUPP_V04_DRAMA_CD_SOURCE_READING.md`
- `IMOSAE_SUPP_V07_DRAMA_CD_SOURCE_READING.md`
- `IMOSAE_SUPP_V13_DRAMA_CD_SOURCE_READING.md`
- `IMOSAE_SUPP_ANIME_AUDIO_DRAMAS_SOURCE_READING.md`
- `IMOSAE_SUPP_SPINOFF_MANGA_SOURCE_READING.md`
- `IMOSAE_SUPPLEMENT_CROSSWALK.md`

A source-reading artifact should be created only when the supplement is analytically substantial. Minor promotional illustrations belong in the paratext inventory instead.

---

## Phase 4 — Specialist synthesis

Specialist synthesis begins only after:

- V14 sequential completion;
- longitudinal ledgers are reconciled;
- high-priority supplements are either read or explicitly deferred.

Every specialist document owns one major analytical responsibility.

### 1. `IMOSAE_CREATIVE_LABOR_AUTHORSHIP_AND_LN_INDUSTRY_SPECIALIST_SYNTHESIS.md`

Primary home for:

- writing as work;
- publishing institutions;
- editor-author relations;
- deadlines;
- adaptations;
- awards;
- market pressure;
- creator community;
- media-mix production;
- the series' reflexive view of its own industry.

### 2. `IMOSAE_TALENT_EFFORT_SUCCESS_FAILURE_AND_SELF_WORTH_SPECIALIST_SYNTHESIS.md`

Primary home for:

- prodigy discourse;
- effort;
- envy;
- comparison;
- luck;
- success/failure;
- artistic judgment;
- psychological consequences of professional hierarchy.

### 3. `IMOSAE_RELATIONSHIPS_INTIMACY_FRIENDSHIP_AND_ADULT_LIFE_SPECIALIST_SYNTHESIS.md`

Primary home for:

- ensemble social architecture;
- friendship;
- romance;
- sex;
- jealousy;
- mutual care;
- professional friendship;
- ordinary adulthood outside work.

This document must not turn every relationship into a route around Itsuki.

### 4. `IMOSAE_FAMILY_SIBLINGHOOD_AND_IDENTITY_SPECIALIST_SYNTHESIS.md`

Primary home for:

- literal siblinghood;
- family revelation and belonging;
- inherited/chosen family;
- the protagonist's sister aesthetic/fixation;
- title-level meaning across the complete series.

### 5. `IMOSAE_COMEDY_SEXUALITY_VULGARITY_AND_BOUNDARIES_SPECIALIST_SYNTHESIS.md`

Primary home for:

- sexual comedy;
- explicitness;
- embarrassment;
- consent/refusal;
- voyeurism/objectification;
- comic framing versus ethical consequence;
- how vulgarity functions formally.

### 6. `IMOSAE_GAMES_TRPG_ALCOHOL_AND_SOCIAL_RITUAL_SPECIALIST_SYNTHESIS.md`

Primary home for:

- tabletop games;
- drinking;
- meals;
- travel;
- group rituals;
- competition and role-play as relationship mechanisms.

### 7. `IMOSAE_NARRATION_JAPANESE_VOICE_AND_INTERTEXT_SPECIALIST_SYNTHESIS.md`

Primary home for:

- focalization;
- prose voice;
- idiolect;
- naming/address;
- wordplay;
- industry vocabulary;
- fiction-within-fiction language;
- literary and genre reference.

### 8. `IMOSAE_ILLUSTRATION_PARATEXT_AND_MEDIA_REFLEXIVITY_SPECIALIST_SYNTHESIS.md`

Primary home for:

- Kantoku illustration corpus;
- cover evolution;
- visual erotic/comic/dramatic framing;
- author/illustrator interplay where documentary evidence exists;
- adaptation/media-mix self-consciousness.

### Character monographs

Do **not** pre-create one for every cast member.

Create a monograph only if:

- the character accumulates evidence across many volumes;
- several specialist documents otherwise repeat a long character thesis;
- the character has distinctive voice and developmental complexity that benefits independent retrieval.

Likely candidates can be decided after the longitudinal ledger is mature.

---

## Phase 5 — Full-series synthesis

### `IMOSAE_FULL_SERIES_SYNTHESIS.md`

This is the continuous reader-facing argument.

It should not be fourteen volume recaps stitched together.

Required functions:

- define what kind of literary work the series becomes in full;
- explain the complete developmental architecture;
- integrate character, relationship, work, family, sexuality, comedy, and metatext;
- show how early theses were revised;
- explain the ending without treating closure as total resolution;
- distinguish the series' strongest achievements from unresolved or ethically unstable elements.

### `IMOSAE_CORE_CHARACTER_REFERENCE.md`

Compact but detailed reference for:

- personality;
- wound/desire;
- voice;
- professional identity;
- key relationships;
- development;
- end state;
- comparative usefulness.

### `IMOSAE_COMPARATIVE_REFERENCE_AND_OPEN_QUESTIONS.md`

Owns:

- comparison matrices;
- exportable formulations for other creator/industry anime and novels;
- unresolved questions;
- limits of the corpus;
- future adaptation/reception research routes.

---

## Phase 6 — Evidence lock and quality-control audits

Before final release, perform all of the following.

### 6.1 Locator validation

Randomly and deliberately sample claims across all fourteen volumes and verify that locators route to the correct source passage.

### 6.2 Japanese quotation audit

For every load-bearing Japanese phrase used in synthesis:

- verify source;
- verify ruby/gaiji;
- verify speaker/focal context;
- verify translation gloss.

### 6.3 Contradiction audit

Search for:

- incompatible chronology;
- inconsistent character-state claims;
- claims that a later volume explicitly disproves;
- supplement/mainline contamination.

### 6.4 Anti-thesis audit

For each major synthesis thesis, identify the strongest contrary evidence and either:

- incorporate it;
- narrow the thesis;
- or leave the issue unresolved.

### 6.5 Duplication audit

Detect specialist documents that repeat the same analysis at length.

Primary-home rule:

> The same evidence may recur when answering different questions; the same argument should not be reproduced wholesale.

### 6.6 Authority audit

Confirm every Markdown artifact has correct:

- series;
- artifact type;
- scope;
- generation;
- status;
- source boundary;
- supersession fields.

### 6.7 Supplemental-authority audit

Verify that:

- author-written supplements are labeled as such only when credits support the claim;
- adaptation-only events are not cited as mainline facts;
- counterfactual route material stays counterfactual;
- marketing copy is not treated as literary evidence.

### 6.8 Coverage audit

Check whether the final corpus can answer:

- each core character's arc;
- each major relationship;
- the creative-labor/industry argument;
- title/siblinghood interpretation;
- sexuality/comedy/boundaries;
- games/social rituals;
- Japanese voice;
- illustration/paratext;
- ending/end states;
- important counterarguments.

---

## Phase 7 — Release and archival freeze

When the corpus is complete:

1. Replace the active entrypoint with `00_README_AND_CORPUS_MAP.md` or convert `CURRENT_STATE_AND_CORPUS_MAP.md` into the frozen final entrypoint.
2. Mark canonical artifacts.
3. Move materially distinct superseded work to `90 Legacy and Superseded/`.
4. Archive conversation transcripts under `Conversation Archives/` when structured analysis supersedes them.
5. Generate:
   - corpus manifest;
   - SHA-256 inventory;
   - release audit;
   - optional ZIP package.
6. Freeze the release.
7. Later corrections become a new version rather than silently mutating the frozen package.

---

# III. Cross-document responsibility rules

## 1. Volume readings own local interpretation

A deep reading explains what a scene/volume means at its evidence boundary.

## 2. Ledgers own longitudinal state

Do not reconstruct entire trajectories repeatedly inside every volume artifact.

## 3. Specialist documents own mature topical arguments

Examples:

- industry theory → creative-labor specialist;
- sibling/title theory → family/sibling specialist;
- consent/vulgarity theory → sexuality/comedy specialist;
- voice → narration/Japanese specialist.

## 4. Full-series synthesis owns integration

It may summarize specialist findings, but should not duplicate their full evidentiary apparatus.

## 5. Evidence indexes own retrieval, not interpretation

Keep locators concise. The index tells the reader where; the analytical artifact tells the reader why.

---

# IV. Recommended mature reader order

1. `00_README_AND_CORPUS_MAP.md` / active `CURRENT_STATE_AND_CORPUS_MAP.md`
2. `IMOSAE_FULL_SERIES_SYNTHESIS.md`
3. `IMOSAE_CORE_CHARACTER_REFERENCE.md`
4. specialist syntheses according to interest
5. checkpoint documents for historical development
6. individual volume readings
7. evidence/terminology/illustration indexes
8. supplemental source readings
9. audits/manifests when provenance verification is needed.

Production order and reader order are intentionally different.

---

# V. Release criteria

The first definitive release should not occur until:

- all fourteen canonical volume readings exist;
- five checkpoints are frozen;
- all mandatory longitudinal ledgers are reconciled;
- high-priority supplements are either integrated or explicitly deferred;
- load-bearing claims have primary-source locators;
- Japanese language claims have been source-verified;
- supplement/mainline authority boundaries are clean;
- specialist syntheses have clear topical homes;
- the full-series synthesis is continuous rather than recap-driven;
- contradiction, anti-thesis, duplication, locator, and authority audits pass;
- final manifests/checksums exist.

The intended result is a reusable literary-analysis corpus that can be searched from a character, relationship, theme, Japanese phrase, visual image, creative-industry problem, or source locator without having to reconstruct the whole project from conversation history.
