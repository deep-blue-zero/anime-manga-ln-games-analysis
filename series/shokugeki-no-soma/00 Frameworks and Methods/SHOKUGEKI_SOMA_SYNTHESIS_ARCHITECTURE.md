---
series: SHOKUGEKI
artifact_type: synthesis_architecture
scope: SOMA_CHARACTER_MODEL_SAMPLE
generation: V1
status: canonical
source_boundary: "Japanese manga sample: V01, V03, V08, V13, V19, V25, V30, V36"
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
created: 2026-08-17
---

# SHOKUGEKI_SOMA_SYNTHESIS_ARCHITECTURE

## Architectural purpose

This architecture defines the canonical analytical home for the initial Yukihira Soma character-modeling project.

It follows the shared Manga / Anime archive language while remaining proportional to the task. This is not initially a full-series *Shokugeki no Soma* synthesis. The architecture therefore emphasizes source control, sequential character readings, longitudinal linguistic and behavioral ledgers, a final character model, and adversarial validation.

The same root is intentionally extensible if a complete 36-volume literary reread is commissioned later.

## Stable identifier

Series identifier:

`SHOKUGEKI`

Primary character scope:

`SOMA`

## Canonical roots

### Analytical root

`Manga / Anime analytical hierarchy / Shokugeki no Soma`

### Primary-source root

`Manga / Anime primary-source hierarchy / Shokugeki no Soma`

The source and analytical roots are separate but cross-referenced. Do not create an additional project root merely because the project later expands.

# 1. Current directory structure

```text
Shokugeki no Soma/
|
|-- CURRENT_STATE_AND_CORPUS_MAP.md
|
|-- 00 Frameworks and Methods/
|   |-- SHOKUGEKI_SOMA_ANALYTICAL_METHOD.md
|   `-- SHOKUGEKI_SOMA_SYNTHESIS_ARCHITECTURE.md
|
|-- 01 Source Lock and Inventory/
|   `-- SHOKUGEKI_SOURCE_INVENTORY.md
|
|-- 02 Sequential Character Readings/
|   |-- SHOKUGEKI_V01_SOMA_CHARACTER_READING.md
|   |-- SHOKUGEKI_V03_SOMA_CHARACTER_READING.md
|   |-- SHOKUGEKI_V08_SOMA_CHARACTER_READING.md
|   |-- SHOKUGEKI_V13_SOMA_CHARACTER_READING.md
|   |-- SHOKUGEKI_V19_SOMA_CHARACTER_READING.md
|   |-- SHOKUGEKI_V25_SOMA_CHARACTER_READING.md
|   |-- SHOKUGEKI_V30_SOMA_CHARACTER_READING.md
|   `-- SHOKUGEKI_V36_SOMA_CHARACTER_READING.md
|
|-- 03 Longitudinal Ledgers/
|   |-- SHOKUGEKI_SOMA_JAPANESE_VOICE_LEDGER.md
|   |-- SHOKUGEKI_SOMA_BEHAVIORAL_MODEL_LEDGER.md
|   `-- SHOKUGEKI_SOMA_RELATIONSHIP_REGISTER_MATRIX.md
|
|-- 04 Final Character Model/
|   `-- SHOKUGEKI_SOMA_FINAL_CHARACTER_MODEL.md
|
`-- 05 Validation and Audit/
    `-- SHOKUGEKI_SOMA_MODEL_VALIDATION_AUDIT.md
```

Only governing and inventory artifacts exist at project initialization. Sequential readings and ledgers become populated as analysis begins.

# 2. Artifact responsibilities

## CURRENT_STATE_AND_CORPUS_MAP.md

This is the first-read document while the project is active.

It must identify:

- current analytical authority;
- source boundary;
- completed readings;
- current model-construction stage;
- whether V30 or V36 remains held out;
- live ledgers;
- next action;
- source and analysis root links;
- any future expansion of scope.

Update it in place as project state changes.

## 00 Frameworks and Methods

Contains only governing protocol and architecture.

### SHOKUGEKI_SOMA_ANALYTICAL_METHOD.md

Defines how the manga is read, how evidence is classified, how Japanese voice is analyzed, how personality claims are formed, and how holdout validation works.

### SHOKUGEKI_SOMA_SYNTHESIS_ARCHITECTURE.md

Defines artifact roles, folder responsibilities, naming, authority, project phases, and full-series expansion rules.

These two documents are canonical unless formally superseded.

## 01 Source Lock and Inventory

### SHOKUGEKI_SOURCE_INVENTORY.md

Records:

- source folder;
- each staged Japanese CBZ;
- Drive ID;
- volume role;
- source-lock status;
- later checksum/integrity fields when established.

Do not claim cryptographic verification until the binary has actually been hashed and archive integrity tested.

## 02 Sequential Character Readings

One artifact per sampled volume.

These are not general volume deep readings. Their semantic responsibility is narrower:

> reconstruct Soma's linguistic, behavioral, relational, emotional, and cognitive state from this volume.

Use filenames:

`SHOKUGEKI_VXX_SOMA_CHARACTER_READING.md`

This naming is deliberate. If a later full-series literary reread creates `SHOKUGEKI_VXX_DEEP_READING.md`, both artifacts can coexist because they answer different questions.

## 03 Longitudinal Ledgers

Mutable active infrastructure during the sampled reread.

### SHOKUGEKI_SOMA_JAPANESE_VOICE_LEDGER.md

Canonical home for recurring linguistic patterns and longitudinal register changes.

### SHOKUGEKI_SOMA_BEHAVIORAL_MODEL_LEDGER.md

Canonical home for conditional personality rules, counterevidence, confidence, claim transitions, and predictions.

### SHOKUGEKI_SOMA_RELATIONSHIP_REGISTER_MATRIX.md

Canonical home for interlocutor-specific differences.

Do not duplicate the same cumulative tables inside every sequential reading. Sequential readings should state deltas and route cumulative material to the ledgers.

## 04 Final Character Model

### SHOKUGEKI_SOMA_FINAL_CHARACTER_MODEL.md

The mature reconstruction surface after V36 validation.

It should be optimized for later comparative analysis and hypothetical behavior reconstruction, not written merely as a chronological biography.

## 05 Validation and Audit

### SHOKUGEKI_SOMA_MODEL_VALIDATION_AUDIT.md

Records how well the pre-V30 and pre-V36 models predicted held-out behavior and voice functions.

This prevents the final model from appearing more predictive than it actually was.

# 3. Project phases

## Phase 0 - setup and source staging

Artifacts:

- `../CURRENT_STATE_AND_CORPUS_MAP.md`
- `SHOKUGEKI_SOMA_ANALYTICAL_METHOD.md`
- `SHOKUGEKI_SOMA_SYNTHESIS_ARCHITECTURE.md`
- `../01 Source Lock and Inventory/SHOKUGEKI_SOURCE_INVENTORY.md`

Exit condition:

The eight-volume sample is identified and the governing method is frozen for the start of V01.

## Phase 1 - baseline and early calibration

Read:

- V01
- V03

Initialize all three ledgers.

Goal:

Separate baseline Soma from immediate Totsuki-context behavior.

## Phase 2 - competition and limits

Read:

- V08
- V13

Goal:

Test competitive language, response to strong opponents, evaluation pressure, success, defeat, and limits.

## Phase 3 - institutional and collective calibration

Read:

- V19
- V25

Goal:

Test whether earlier rules survive institutional conflict, ideological pressure, collective stakes, teamwork, and later relationship development.

At the end of V25, freeze a provisional model snapshot.

## Phase 4 - first holdout

Read V30 only after predictions have been recorded from the V01-V25 model.

Goal:

Measure genuine longitudinal predictive performance.

After V30:

- audit predictions;
- assign claim transitions;
- freeze a revised pre-V36 model.

## Phase 5 - final holdout

Read V36.

Goal:

Test endpoint stability and identify genuine late-series development.

## Phase 6 - final synthesis and audit

Complete:

- [`SHOKUGEKI_SOMA_FINAL_CHARACTER_MODEL.md`](../../../provenance/drive-artifacts/DRIVE_ARTIFACT_REFERENCE_INDEX.md)
- [`SHOKUGEKI_SOMA_MODEL_VALIDATION_AUDIT.md`](../../../provenance/drive-artifacts/DRIVE_ARTIFACT_REFERENCE_INDEX.md)

Update corpus map to mark the sampled character-model pass complete.

# 4. Authority states

Use:

- `canonical`
- `active_provisional`
- `superseded`
- `historical_legacy`

Recommended states during this project:

- analytical method: `canonical`;
- synthesis architecture: `canonical`;
- current-state map: `active_provisional` until completion;
- sequential readings: `canonical` once each source reading is completed and checked;
- ledgers: `active_provisional` while the sample remains unfinished;
- final character model: `canonical` after V36 validation;
- validation audit: `canonical` after completion.

# 5. Revision behavior

Sequential character readings are historical snapshots of what the sampled volume supports at that point.

Do not silently rewrite an early reading to make it agree with V30 or V36.

Instead:

- preserve the early reading;
- update the cumulative ledger;
- mark the earlier claim `REVISE`, `DOWNGRADE`, or `REJECT` as needed;
- state the mature formulation in the final model.

This preserves intellectual provenance.

# 6. Model snapshots

Two model snapshots are architecturally important even if represented inside the behavioral ledger rather than separate files.

## Snapshot A - after V25

Training/model-construction boundary.

V30 remains unread for detailed evidence extraction at the moment of freeze.

## Snapshot B - after V30

First holdout revision boundary.

V36 remains unread for detailed evidence extraction at the moment of freeze.

The validation audit should be able to reconstruct what each snapshot actually predicted.

# 7. Minimal context rule

Sequential character readings may explain plot, but context should be proportional to its analytical value.

Preferred standard:

> enough context that a reader can understand why Soma's behavior matters, but not a substitute synopsis of the entire volume.

If a non-Soma scene materially changes the interpretation of his later conduct, summarize it. Otherwise, do not expand it merely for completeness.

# 8. Full-series expansion path

If a complete V01-V36 reread is later commissioned, preserve this architecture and extend it rather than migrating to a parallel root.

Recommended changes at that point:

1. Expand `../01 Source Lock and Inventory/SHOKUGEKI_SOURCE_INVENTORY.md` to all 36 volumes.
2. Add general literary volume artifacts as:
   - `../02 Full-Series Deep Readings/SHOKUGEKI_V01_DEEP_READING.md`
   - through `SHOKUGEKI_V36_DEEP_READING.md`.
3. Keep existing `SOMA_CHARACTER_READING` artifacts unchanged except for metadata corrections or explicit new versions.
4. Add only the longitudinal ledgers justified by recurring evidence.
5. Add specialist syntheses only after the full read demonstrates a persistent analytical responsibility.
6. Create a full-series synthesis only after sequential evidence and ledgers stabilize.
7. Move to `00_README_AND_CORPUS_MAP.md` only when the corpus becomes completed or frozen.

Possible future layers may include:

- ensemble/relationship synthesis;
- institutions, hierarchy, and culinary legitimacy;
- food, craft, experimentation, and pedagogy;
- visual/formal manga analysis;
- fanservice/body/comedy grammar;
- Erina or Joichiro character monographs;
- full-series synthesis;
- evidence and locator indexes.

Do not create these categories now merely for symmetry.

# 9. Naming and metadata

Stable filename grammar:

`SHOKUGEKI_<SCOPE>_<ARTIFACT_ROLE>.md`

Examples:

- `../02 Sequential Character Readings/SHOKUGEKI_V08_SOMA_CHARACTER_READING.md`
- `../03 Longitudinal Ledgers/SHOKUGEKI_SOMA_JAPANESE_VOICE_LEDGER.md`
- [`SHOKUGEKI_SOMA_FINAL_CHARACTER_MODEL.md`](../../../provenance/drive-artifacts/DRIVE_ARTIFACT_REFERENCE_INDEX.md)

Every new Markdown analytical artifact should normally include YAML fields for:

- `series`;
- `artifact_type`;
- `scope`;
- `generation`;
- `status`;
- `source_boundary`;
- `supersedes`;
- `superseded_by`;
- `do_not_use_as_current_authority`.

# 10. Canonical retrieval route

While active:

1. `../CURRENT_STATE_AND_CORPUS_MAP.md`
2. governing method/architecture when protocol is relevant;
3. final character model when available;
4. longitudinal ledger for current claim state;
5. sampled volume character reading;
6. original Japanese CBZ for exact verification.

Before the final character model exists, the behavioral ledger is the preferred current cumulative authority for Soma-model claims.

# 11. Governing architectural rule

Every artifact in this project must answer one clear question.

The sampled character readings answer:

> What does this volume establish or challenge about Soma?

The ledgers answer:

> What is the current cumulative model across sampled volumes?

The final model answers:

> What version of Soma can the evidence reliably reconstruct?

The validation audit answers:

> How well did that model actually predict held-out late-series behavior?

A later general deep reading would answer a different question:

> What is this volume doing as a complete part of *Shokugeki no Soma*?

Keeping those responsibilities distinct is what allows a future full-series project to grow from this root without erasing the current work.
