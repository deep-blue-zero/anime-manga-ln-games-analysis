---
series: SHOKUGEKI
artifact_type: synthesis_architecture
scope: FULL_SERIES_V01-V36
generation: V2
status: canonical
source_boundary: Original Japanese manga V01-V36 complete; activation history preserved; terminal reconstruction refinement
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
created: 2026-08-26
---

# SHOKUGEKI_V2_SYNTHESIS_ARCHITECTURE

## Architectural purpose

This document expands the existing *Shokugeki no Soma* analytical root from a completed, purpose-built Yukihira Soma sampled reconstruction into a complete V01-V36 literary, ensemble-character, and reconstruction corpus.

This is an **extension of the existing canonical root**, not a new project. The V1 Soma experiment remains intact because its sampled design and holdout audit are valuable provenance that a full retrospective reread cannot recreate.

Stable series identifier: `SHOKUGEKI`.

## 1. Canonical roots

### Analytical root

`Manga / Anime analytical hierarchy / Shokugeki no Soma`

Drive ID: `1eq8Omgx9tdCoqwj__MTdieR1QSb88a_8`

### Primary-source root

`Manga / Anime primary-source hierarchy / Shokugeki no Soma`

Drive ID: `1Cdo5Uhq936_I1Hw3nB1S5bgSJ-rBAAlO`

There must remain exactly one analytical root and one source root for the series.

## 2. Authority model after V2 activation

### V2 governing authority

- `../CURRENT_STATE_AND_CORPUS_MAP.md` — canonical first-read/current-state router.
- `SHOKUGEKI_V2_ANALYTICAL_METHOD.md` — canonical protocol for the full V01-V36 reread.
- `SHOKUGEKI_V2_SYNTHESIS_ARCHITECTURE.md` — canonical architecture for the expanded project.
- `../01 Source Lock and Inventory/SHOKUGEKI_SOURCE_INVENTORY.md` — mutable source-routing/lock authority, expanded in place to the complete 36-volume source spine.

### V1 bounded authority retained

The following remain canonical **within the scope of the completed V1 Soma sampled experiment**:

- `SHOKUGEKI_SOMA_ANALYTICAL_METHOD.md`;
- `SHOKUGEKI_SOMA_SYNTHESIS_ARCHITECTURE.md`;
- eight `SHOKUGEKI_VXX_SOMA_CHARACTER_READING.md` artifacts;
- three V1 Soma longitudinal ledgers;
- [`SHOKUGEKI_SOMA_FINAL_CHARACTER_MODEL.md`](../04%20Final%20Character%20Model/SHOKUGEKI_SOMA_FINAL_CHARACTER_MODEL.md);
- [`SHOKUGEKI_SOMA_MODEL_VALIDATION_AUDIT.md`](../05%20Validation%20and%20Audit/SHOKUGEKI_SOMA_MODEL_VALIDATION_AUDIT.md).

They do not govern how new V2 volumes are read.

At activation, the V1 final character model remained the preferred **completed Soma reconstruction** until a full-series V2 Soma model was explicitly promoted. That condition has now been fulfilled: current full-series behavior routes through the V2 model and the character-model README. The V1 validation audit remains permanently authoritative for the old holdout experiment.

## 3. Existing structure and additive V2 layers

Preserve the current folders and file IDs. Do not rename the completed V1 lanes merely to make the tree visually uniform.

```text
Shokugeki no Soma/
|
|-- CURRENT_STATE_AND_CORPUS_MAP.md
|
|-- 00 Frameworks and Methods/
|   |-- SHOKUGEKI_SOMA_ANALYTICAL_METHOD.md                  [V1 bounded]
|   |-- SHOKUGEKI_SOMA_SYNTHESIS_ARCHITECTURE.md             [V1 bounded]
|   |-- SHOKUGEKI_V2_ANALYTICAL_METHOD.md                    [V2 governing]
|   `-- SHOKUGEKI_V2_SYNTHESIS_ARCHITECTURE.md               [V2 governing]
|
|-- 01 Source Lock and Inventory/
|   `-- SHOKUGEKI_SOURCE_INVENTORY.md                        [shared, expanded in place]
|
|-- 02 Sequential Character Readings/                         [V1 frozen lane]
|   `-- eight sampled SOMA_CHARACTER_READING artifacts
|
|-- 02 Full-Series Deep Readings/                             [V2 active lane]
|   |-- SHOKUGEKI_V01_DEEP_READING.md ... V36
|   `-- six-volume CHECKPOINT artifacts when closed
|
|-- 03 Longitudinal Ledgers/
|   |-- three frozen V1 Soma ledgers
|   |-- SHOKUGEKI_CHARACTER_STATE_AND_RECONSTRUCTION_LEDGER.md
|   |-- SHOKUGEKI_CHARACTER_RECONSTRUCTION_READINESS_LEDGER.md
|   |-- SHOKUGEKI_ENSEMBLE_JAPANESE_VOICE_LEDGER.md
|   |-- SHOKUGEKI_RELATIONSHIP_DYNAMICS_LEDGER.md
|   |-- SHOKUGEKI_CULINARY_IDEOLOGY_CRAFT_AND_PEDAGOGY_LEDGER.md
|   |-- SHOKUGEKI_INSTITUTION_POWER_AND_LEGITIMACY_LEDGER.md
|   |-- SHOKUGEKI_COMPETITION_EVALUATION_AND_GROWTH_LEDGER.md
|   `-- SHOKUGEKI_VISUAL_FOOD_DRAMATURGY_AND_BODY_COMEDY_LEDGER.md
|
|-- 04 Final Character Model/                                 [existing V1 artifact retained]
|   `-- SHOKUGEKI_SOMA_FINAL_CHARACTER_MODEL.md
|
|-- 05 Validation and Audit/                                  [existing audit lane]
|   `-- SHOKUGEKI_SOMA_MODEL_VALIDATION_AUDIT.md
|
`-- 06 Evidence and Indexes/
    `-- SHOKUGEKI_V1_TO_V2_CROSSWALK.md
```

Future specialist character/literary syntheses and the final full-series synthesis should be created only when they have content. Do not create empty folders for symmetry.

## 4. V2 sequential lane

Canonical filename:

`SHOKUGEKI_VXX_DEEP_READING.md`

Its responsibility is:

> What is this volume doing as a complete part of *Shokugeki no Soma*, and what does it change in the current literary, character, relationship, voice, craft, institutional, competition, and visual-form models?

This is distinct from the V1 question:

> What does this strategically sampled volume establish or challenge specifically about Soma?

At the eight overlapping volumes, both artifacts may remain canonical for their respective scopes.

## 5. Checkpoint architecture

Default frozen checkpoints:

- `SHOKUGEKI_V01-V06_CHECKPOINT.md`
- `SHOKUGEKI_V07-V12_CHECKPOINT.md`
- `SHOKUGEKI_V13-V18_CHECKPOINT.md`
- `SHOKUGEKI_V19-V24_CHECKPOINT.md`
- `SHOKUGEKI_V25-V30_CHECKPOINT.md`
- `SHOKUGEKI_V31-V36_END_STATE_CHECKPOINT.md`

Each checkpoint is a frozen longitudinal synthesis, not another mutable ledger.

It should:

- consolidate major literary claims;
- adjudicate prospective predictions;
- reconcile character state and readiness;
- record relationship-state transitions;
- identify which voice models are stable enough for reconstruction;
- reconcile institution/competition/craft/visual ledgers;
- route V1 Soma claim transitions where relevant;
- define open questions for the next block.

If a major arc boundary makes an additional checkpoint analytically necessary, create it only with a distinct responsibility.

## 6. V2 longitudinal-ledger responsibilities

### Character state and reconstruction

`../03 Longitudinal Ledgers/SHOKUGEKI_CHARACTER_STATE_AND_RECONSTRUCTION_LEDGER.md`

Canonical home for character-state deltas, conditional behavior rules, emotional triggers, ordinary/high-stakes contrasts, counterevidence, and model revisions.

### Reconstruction readiness

`../03 Longitudinal Ledgers/SHOKUGEKI_CHARACTER_RECONSTRUCTION_READINESS_LEDGER.md`

Canonical home for coverage assessment and promotion through `background -> tracked -> emerging -> substantial -> monograph_ready -> validated_model`.

It answers **whether** a model is mature enough, not what the model itself says.

### Ensemble Japanese voice

`../03 Longitudinal Ledgers/SHOKUGEKI_ENSEMBLE_JAPANESE_VOICE_LEDGER.md`

Canonical home for voice/register patterns beyond the frozen V1 Soma-only voice ledger.

### Relationship dynamics

`../03 Longitudinal Ledgers/SHOKUGEKI_RELATIONSHIP_DYNAMICS_LEDGER.md`

Canonical home for dyadic/group state changes, reciprocity, address/register shifts, rivalry/alliance, mentorship, family, intimacy, care, and conflict repair.

### Culinary ideology, craft, and pedagogy

`../03 Longitudinal Ledgers/SHOKUGEKI_CULINARY_IDEOLOGY_CRAFT_AND_PEDAGOGY_LEDGER.md`

Canonical home for recurring claims about culinary authorship, originality, service, expertise, labor, experimentation, tradition, inheritance, learning, teaching, and the relation between elite and ordinary food knowledge.

### Institution, power, and legitimacy

`../03 Longitudinal Ledgers/SHOKUGEKI_INSTITUTION_POWER_AND_LEGITIMACY_LEDGER.md`

Canonical home for Totsuki, Elite Ten, shokugeki authority, Central, family capital, WGO, hierarchy, coercion, legitimacy, and meritocratic rhetoric.

### Competition, evaluation, and growth

`../03 Longitudinal Ledgers/SHOKUGEKI_COMPETITION_EVALUATION_AND_GROWTH_LEDGER.md`

Canonical home for rivalry, judging, loss, victory, humiliation, growth, teamwork, spectacle, audience, evaluation legitimacy, and the difference between competitive ranking and total social hierarchy.

### Visual food dramaturgy and body comedy

`../03 Longitudinal Ledgers/SHOKUGEKI_VISUAL_FOOD_DRAMATURGY_AND_BODY_COMEDY_LEDGER.md`

Canonical home for manga-specific sensory staging: food reveals, reaction imagery, clothing-loss/body transformation grammar, eroticization, absurdist comedy, symbolic spaces, visual metaphors, and their changes over the series.

## 7. Character monograph architecture

Do not decide the entire cast in advance. The original activation architecture reserved dedicated full-scale monographs for `monograph_ready` characters. The completed V01–V36 corpus now permits a **terminal refinement**, without rewriting what the earlier checkpoints authorized.

| Artifact level | Evidence and authority contract | Readiness consequence |
|---|---|---|
| Full-scale monograph / validated reconstruction | Broad longitudinal, adverse, ordinary, relational, and endpoint evidence; explicit exception testing | `monograph_ready` authorizes construction; the recorded audit authorizes `validated_model` |
| Bounded substantial reconstruction | Useful recurring character evidence, a clear default and state gates, conditional behavior/register, ordinary evidence or explicit absence, recipient modifiers, negative controls, probes and abstentions | Retain `substantial` or `substantial, provisional`; an artifact, filename, or self-audit does not promote it |

A bounded model may be the character's first-read reconstruction artifact while ledgers and specialist syntheses retain their separate authority. It must expose missing ordinary, interior, endpoint, or accountability conditions. Do not fill those gaps with prominence, generic behavior, or protagonist-centered interpretation. Depth should follow evidence; Mana and Senzaemon need tighter limits than Hisako's broader work and relationship record.

For a full-scale artifact at `monograph_ready`, use a stable name such as:

`SHOKUGEKI_ERINA_CHARACTER_MONOGRAPH.md`

or, when the primary responsibility is generative reconstruction:

`SHOKUGEKI_ERINA_CHARACTER_MODEL.md`

Use the role that best describes the artifact; do not create both unless they answer genuinely different questions.

Likely but not guaranteed candidates include Soma, Erina, Megumi, Joichiro, Takumi, Hayama, Alice, Ryo, Shinomiya, Tsukasa, Rindo, and other characters whose evidence proves substantial. Readiness, not fandom prominence, decides.

### Soma V2 end state

A full-series Soma reconstruction should not overwrite the V1 final model in place.

Create a new V2 artifact, then use explicit authority routing:

- V2 full-series model becomes current reconstruction authority if it passes its audit;
- V1 sampled model becomes bounded/historical provenance for mature Soma claims;
- V1 validation audit remains immutable evidence about the sampled prospective experiment.

## 8. Specialist literary synthesis architecture

After enough sequential evidence accumulates, likely semantic homes include:

- culinary authorship, originality, craft, service, and pedagogy;
- Totsuki, meritocracy, hierarchy, coercion, and institutional legitimacy;
- competition, judgment, failure, rivalry, and collaborative growth;
- food, body, desire, fanservice, comedy, and sensory dramaturgy;
- family, inheritance, mentorship, and self-authorship;
- ensemble relationships, reciprocity, and social ecology;
- ending/BLUE/`Le dessert` end-state analysis if the final volumes warrant a separate treatment.

These are **candidate responsibilities**, not pre-authorized files. Promote one only when the ledgers show enough recurring evidence that independent retrieval is valuable.

## 9. Full-series synthesis

Final master artifact:

`SHOKUGEKI_FULL_SERIES_SYNTHESIS.md`

It is produced only after:

1. V01-V36 deep readings are complete;
2. all six checkpoints are closed;
3. live ledgers are reconciled through V36;
4. V1-to-V2 claim transitions are explicit;
5. major character models/specialist syntheses required for retrieval are complete;
6. evidence/index infrastructure can route major claims back to source;
7. unresolved claims are identified rather than silently harmonized.

The master synthesis should not duplicate every character monograph. It should state the series-level thesis and route deeper questions to specialist homes.

## 10. Evidence and revision infrastructure

### V1-to-V2 crosswalk

`../06 Evidence and Indexes/SHOKUGEKI_V1_TO_V2_CROSSWALK.md` records how the old focused-pass artifacts relate to current authority.

### Claim revision ledger

Create `SHOKUGEKI_CLAIM_REVISION_LEDGER.md` once sequential V2 analysis begins generating material transitions worth tracking. Use `PRESERVE / STRENGTHEN / REVISE / DOWNGRADE / REJECT / OPEN`.

### Locator index

Create `SHOKUGEKI_LOCATOR_INDEX.md` when evidence density makes direct retrieval from deep readings burdensome. It should index major claims/characters/themes to deterministic VXX/chapter/CBZ-image locators.

### Character evidence matrix

Create `SHOKUGEKI_CHARACTER_EVIDENCE_MATRIX.md` when multiple monograph candidates reach substantial readiness and cross-character evidence routing becomes expensive.

Do not create these later artifacts until their retrieval function is real.

## 11. Source architecture

`../01 Source Lock and Inventory/SHOKUGEKI_SOURCE_INVENTORY.md` is shared V1/V2 infrastructure and is expanded **in place**.

It must distinguish:

- collection-level presence/readiness;
- per-volume cryptographic lock state;
- Japanese-language/legibility audit state;
- mainline chapters;
- official bonus/epilogue material;
- recipes and low-weight comedy;
- prototypes/alternate-author material;
- publication/promotional backmatter;
- resolution or legibility limitations.

V36 retains a tiered distinction between serialized endpoint material and official `Le dessert` post-finale evidence.

## 12. Authority-transition rules

A later artifact does not automatically invalidate an earlier one.

Examples:

- V01 deep reading stays canonical for the V01 local boundary even after V36.
- V01-V06 checkpoint can be superseded as a **current cumulative** model while remaining frozen historical authority for what the project believed at that boundary.
- a V2 Erina model may become current mature authority while individual volume readings remain evidence/provenance.
- a V2 Soma model may supersede the V1 model for complete-series reconstruction, but cannot change the scorecard in the V1 validation audit.

## 13. Recommended retrieval routes

### Full-series literary question

`CURRENT_STATE_AND_CORPUS_MAP -> SHOKUGEKI_FULL_SERIES_SYNTHESIS -> relevant specialist synthesis/ledger -> checkpoint -> volume deep reading -> Japanese CBZ`

### Mature character question

`CURRENT_STATE_AND_CORPUS_MAP -> 04 Final Character Model/README -> selected validated or bounded model -> character/voice/relationship ledgers -> checkpoint -> deep reading -> Japanese CBZ`

Use the separate reconstruction-fidelity audit for ordinary behavior, recipient differences, and abstentions. The original full-series audit and immutable V1 holdout audit retain their different validation responsibilities. Exact evidence retrieval escalates only where the existing record cannot resolve a material claim.

### V1 Soma holdout/predictive-warrant question

`SHOKUGEKI_SOMA_MODEL_VALIDATION_AUDIT -> frozen V1 model/ledger revision -> sampled SOMA_CHARACTER_READING -> Japanese CBZ`

### Publication-boundary question

`relevant SHOKUGEKI_VXX_DEEP_READING -> prior checkpoint/ledger state -> Japanese CBZ`

### Exact Japanese wording or visual evidence

`Japanese CBZ`, with the analytical artifact used only to find the deterministic locator.

## 14. Activation state

At V2 activation:

- collection-level V01-V36 source presence: PASS;
- representative language/legibility sampling: PASS with heterogeneous resolution noted;
- V1 Soma focused pass: COMPLETE / FROZEN;
- V2 method and architecture: CANONICAL;
- V2 live ledgers: INITIALIZED at V00;
- V2 sequential deep readings: none yet;
- next canonical operation: `../02 Full-Series Deep Readings/SHOKUGEKI_V01_DEEP_READING.md`.

## 15. Governing architectural rule

Every artifact must have one clear identity, scope, authority state, and canonical home.

V1 is preserved because it answers a narrower experimental question well. V2 is added because the user now wants a larger question answered. The architecture should allow both to remain intelligible without forcing the old corpus to masquerade as work it was never designed to be.

## 16. Original terminal reconstruction expansion

Six existing validated models are expanded in place and ten bounded models are available through [the character router](../04%20Final%20Character%20Model/README.md). The sixteen readiness states are unchanged. This refinement changes artifact availability and reconstructive depth, not the frozen sequential method, past promotion decisions, or the separate responsibilities of the seven specialist syntheses.

The repository schema search found no governing cross-title character-package schema. The reconstruction-capability specification concerns discovery governance and remains specification-only; it is not adopted as a Shokugeki JSON package. Markdown models remain the canonical deliverables.

## 17. Ikumi Mito reconstruction addition

The subsequent owner-requested [Ikumi Mito model](../04%20Final%20Character%20Model/SHOKUGEKI_MITO_CHARACTER_MODEL.md) brings the current router to seventeen artifacts: six validated and eleven bounded. The original sixteen-model expansion above remains its own historical decision. Ikumi carries her explicit V20/V21 `substantial, provisional` readiness; omission from the earlier terminal selector did not demote her.

The existing Markdown model contract accommodates a default drawn from the latest evidenced school state when the analytical record cannot responsibly supply an adult endpoint. Targeted V02/V06 primary observations are appended to mutable ledgers and recorded in the fidelity audit. No sequential restart, whole-volume reread, duplicate character package, manual global discovery update, or change to specialist authority follows from this addition.
