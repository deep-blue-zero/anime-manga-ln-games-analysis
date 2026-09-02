---
series: SHOKUGEKI
artifact_type: analytical_method
scope: FULL_SERIES_V01-V36
generation: V2
status: canonical
source_boundary: Original Japanese manga tankobon V01-V36 in the canonical Shokugeki primary-source root; per-volume publication boundaries preserved
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
created: 2026-08-26
---

# SHOKUGEKI_V2_ANALYTICAL_METHOD

## Purpose

This document governs the complete V01-V36 original-Japanese manga reread of *Shokugeki no Soma / 食戟のソーマ*.

The V2 project has three equally important responsibilities:

1. **full-series literary analysis** — what each volume and the series as a whole are doing thematically, formally, institutionally, emotionally, and structurally;
2. **ensemble character analysis** — how characters change, relate, compete, teach, fail, protect identities, and respond to institutions over time;
3. **character reconstruction** — for characters with sufficient evidence, construct source-grounded models of Japanese voice, behavioral rules, relationship-specific register, emotional activation, ordinary-state behavior, decision-making, and exception conditions that can support later hypothetical simulation.

The project is not a replacement for the completed V1 Yukihira Soma sampled-character experiment. V1 remains frozen provenance and a bounded reconstruction authority. V2 expands the semantic responsibility from one strategically sampled protagonist model to a complete literary and ensemble corpus.

## 1. Governing principles

1. The original Japanese manga is primary evidence.
2. Read V01-V36 sequentially. A volume's local-state claims may use only that volume and earlier V2 evidence.
3. Separate **observed fact**, **inference**, **interpretation**, and **retrospective significance**.
4. Preserve manga form: panel sequence, page turns, spreads, framing, reaction timing, typography, visual metaphor, body comedy, and food presentation are evidence.
5. Japanese dialogue is analyzed pragmatically and relationally, not reduced to catchphrases or isolated lexical frequency.
6. Character claims are conditional models with counterevidence and exception conditions, not adjective lists.
7. A character's cooking is evidence about cognition and values only when the source supports that connection; do not assume every dish is a personality allegory.
8. Competition is analyzed as psychology, pedagogy, social ordering, spectacle, and institutional procedure, not merely as a win/loss ledger.
9. Institutional claims distinguish Totsuki's formal rules, prestige systems, coercive power, educational functions, meritocratic rhetoric, family capital, commercial authority, and culinary competence.
10. Existing V1 Soma conclusions may be compared only after the fresh V2 reading of the corresponding volume is stable. They may not silently pre-fill the new reading.
11. Counterevidence and unresolved ambiguity remain visible.
12. Major claim changes use `PRESERVE`, `STRENGTHEN`, `REVISE`, `DOWNGRADE`, `REJECT`, or `OPEN`.
13. Exact wording and visual claims must remain recoverable through deterministic source locators.
14. External culinary history, science, interviews, anime material, translations, wikis, and fandom interpretation are supplementary unless a later artifact explicitly expands the source boundary.

## 2. The dual-horizon rule

The analyst cannot become literally ignorant of the completed V1 Soma sample or general series familiarity. V2 therefore uses procedural controls rather than pretending to be epistemically blind.

Each volume has two interpretive horizons.

### Horizon A — local publication boundary

This is the governing sequential layer.

Ask:

- What has the manga established **by the end of this volume**?
- What can a character reasonably know now?
- What relationship state exists now?
- Which themes or institutional claims are actually supported now?
- Which predictions follow from the evidence available now?

Do not import later outcomes to make early ambiguity look resolved.

### Horizon B — retrospective significance

After Horizon A is stable, a tightly separated retrospective section may identify later resonance, foreshadowing, reversal, structural irony, or endpoint significance.

Retrospective knowledge may sharpen literary interpretation but **must not**:

- change the local character-state ledger as though the character already possessed later knowledge;
- be scored as a prospective prediction;
- repair an early claim without a recorded revision transition;
- or be used to claim that the early volume made a later outcome inevitable.

Existing V1 Soma sample documents are consulted only in this Horizon-B/comparison stage for corresponding volumes.

## 3. Evidence classes

Use these labels when they improve precision:

- `JT` — Japanese textual evidence: dialogue, narration, captions, in-world text.
- `VB` — visual-behavioral evidence: expression, gaze, posture, gesture, spatial relation, silent reaction.
- `AC` — action/choice evidence.
- `RS` — relationship/register evidence.
- `OC` — other-character evidence about a target character.
- `CC` — cooking-cognition/craft evidence.
- `FM` — formal manga evidence: paneling, page turn, spread, typography, visual rhythm, compositional contrast.
- `VD` — visual food dramaturgy: food reveal, sensory metaphor, transformation/reaction grammar, body/comedy/eroticization used to stage tasting.
- `IN` — institution/power evidence: rules, hierarchy, legitimacy, coercion, evaluation, economic or status structure.
- `CP` — competition/pedagogy evidence: judging, rivalry, loss, learning, teaching, collaboration, performance pressure.
- `TH` — thematic/motif evidence.
- `PT` — paratext: omake, recipes, author pages, publication matter, alternate one-shots, promotional material.
- `CX` — context needed to interpret another evidence class.

Evidence classes are descriptors, not confidence scores.

## 4. Source locators and volume lock

Preferred locator grammar:

`VXX / chapter number or title / CBZ image index / panel or page region`

When printed page numbers are reliable, record them in addition to CBZ image index.

Every volume begins with a Phase-0 lock:

1. retrieve the canonical CBZ temporarily from Drive;
2. verify filename and Drive ID against `../01 Source Lock and Inventory/SHOKUGEKI_SOURCE_INVENTORY.md`;
3. compute SHA-256;
4. run archive/CRC integrity testing;
5. record image-member count and representative dimensions;
6. identify mainline chapter boundaries, spreads, bonuses, recipes, one-shots, alternate-author material, and publication backmatter;
7. classify non-mainline material as canonical supplementary, low-weight comedy, prototype/alternate continuity, bibliographic, or excluded;
8. note any legibility or resolution limitation before analysis;
9. clean the temporary source payload after the analytical artifacts are safely written and verified.

The collection-level audit has already established a contiguous V01-V36 Japanese CBZ spine. Per-volume cryptographic locks are still performed when each volume enters active V2 reading.

## 5. Per-volume deep-reading protocol

Each `SHOKUGEKI_VXX_DEEP_READING.md` receives six passes.

### Pass A — whole-volume contextual read

Read the complete volume before detailed extraction.

Establish:

- starting social/institutional state;
- major conflicts and stakes;
- important relationship movements;
- competition or service context;
- dominant culinary problem(s);
- structural role in the current arc;
- endpoint state and unresolved questions.

Avoid turning this into a chapter synopsis.

### Pass B — literary/formal reread

Track what the volume does as manga:

- page and chapter architecture;
- page-turn reveals;
- panel density and rhythm;
- reaction sequencing;
- visual parallelism;
- food reveal grammar;
- sensory metaphor;
- comedy and eroticization;
- body transformation or fantasy imagery;
- silence and negative space;
- how competition is staged as spectacle;
- how ordinary service scenes differ visually from elite contest scenes.

Ask what the form contributes that a prose transcript would lose.

### Pass C — character and relationship extraction

For every character with genuinely diagnostic material, record:

- current goals and pressures;
- self-conception and identity claims;
- behavioral decisions;
- emotional departures from baseline;
- response to success, failure, humiliation, praise, uncertainty, authority, and vulnerability;
- learning and teaching behavior;
- relationship-specific conduct;
- changes from prior V2 state;
- counterevidence to current models.

Do not force equal coverage. Character importance is evidence-driven and may remain highly uneven.

### Pass D — Japanese voice/register extraction

For high-information dialogue, track:

- first-person and second-person forms;
- surname/given-name/title/honorific choices;
- plain/polite/mixed register;
- sentence endings and contractions;
- imperatives, requests, hedges, admissions, challenges, praise, apology, refusal, reassurance, criticism, joking, and teasing;
- serious-speech changes;
- textual prosody: fragments, pauses, ellipses, repetition, emphatic typography, delayed response;
- relationship-specific and pressure-specific shifts.

The goal is functional reconstruction, not exhaustive transcription.

### Pass E — adversarial reread

Challenge the strongest emerging claims.

For each important literary or character proposition, ask:

- What is the strongest counterexample in this volume?
- Is a supposed trait actually relationship-specific?
- Is a theme being inferred from a single dramatic scene?
- Does the manga complicate its own institution or competition rhetoric?
- Does visual comedy undermine, intensify, or simply coexist with serious characterization?
- Are we confusing competence with virtue, prestige with legitimacy, confidence with certainty, reserve with lack of feeling, or fanservice with absence of narrative function?
- Is the apparent development genuine change, new context, or merely new evidence of an older rule?

### Pass F — integration and prospective freeze

After the deep reading is stable:

1. state the volume's principal literary thesis;
2. state major character deltas;
3. update only the ledgers actually affected;
4. route V1 Soma claims through the crosswalk if this is a previously sampled volume;
5. assign claim transitions;
6. record unresolved questions;
7. freeze concise, falsifiable predictions for later volumes where the current evidence warrants them;
8. update `../CURRENT_STATE_AND_CORPUS_MAP.md` and the source inventory lock state.

## 6. Literary-analysis lenses

These are recurring lenses, not mandatory headings when a volume supplies no evidence.

### 6.1 Culinary authorship and originality

Track what the series means by a cook having "their own" food or style.

Distinguish:

- imitation;
- influence;
- inheritance;
- adaptation;
- technical mastery;
- self-authorship;
- service to a specific eater;
- prestige claims about originality.

### 6.2 Craft, labor, service, and expertise

Track the relationship among:

- restaurant labor;
- repetition and accumulated practice;
- elite schooling;
- specialist traditions;
- customer feedback;
- convenience/industrial food knowledge;
- professional kitchen workflow;
- embodied skill versus declarative explanation.

### 6.3 Education and pedagogy

Ask how Totsuki and individual mentors teach:

- challenge versus instruction;
- humiliation versus productive failure;
- competition versus collaboration;
- apprenticeship;
- peer correction;
- feedback quality;
- selection/elimination;
- whether the institution creates growth, wastes talent, or both.

### 6.4 Institutions, hierarchy, legitimacy, and class

Track formal and informal power separately:

- Totsuki administration;
- Elite Ten authority;
- shokugeki rules;
- Central;
- family lineages;
- economic/social prestige;
- WGO authority;
- restaurant/industry reputation;
- technical competence;
- coercive capacity;
- legitimacy in the eyes of characters.

Do not treat "meritocracy" as a neutral descriptive fact merely because characters use competitive rhetoric.

### 6.5 Competition, judgment, failure, and growth

Track what competitive structures actually do to people.

Questions include:

- What kinds of loss produce learning, shame, resentment, exclusion, or renewed agency?
- Who is allowed to judge, and why is that judgment accepted?
- Does victory establish superiority in a narrow task or a total hierarchy?
- When is rivalry reciprocal and when is it domination?
- How do spectacle and audience alter behavior?
- How does the series distinguish fair adversity from arbitrary or ideological coercion?

### 6.6 Family, inheritance, lineage, and chosen affiliation

Track biological family, culinary lineage, mentorship, Polar Star, rival networks, and self-selected communities.

Ask how characters inherit techniques, burdens, expectations, status, and unfinished conflicts without assuming inheritance determines identity.

### 6.7 Food, body, desire, comedy, and sensory excess

The series' tasting reactions and fanservice are not analytically disposable.

Track:

- whose bodies are used and how;
- gendered asymmetries;
- eroticization versus absurdist body comedy;
- loss of clothing as evaluation grammar;
- fantasy transformations and symbolic environments;
- whether reactions externalize pleasure, prestige, domination, vulnerability, memory, or social recognition;
- how the manga modulates or changes this device across the run.

Describe before judging. Distinguish formal function from value judgment.

### 6.8 Ordinary life versus tournament life

A reconstruction project needs low-stakes evidence.

Track kitchens, dorm life, meals, travel, errands, service work, conversation after contests, jokes, and unguarded downtime whenever available. High-stakes competition alone produces distorted character models.

## 7. Character-reconstruction protocol

A character becomes reconstructable through **coverage**, not popularity or chapter count alone.

### 7.1 Required modeling dimensions

For each serious target, attempt to establish:

1. Japanese baseline voice and address system.
2. Pragmatic acts: challenge, praise, refusal, apology, reassurance, criticism, teaching, admission of ignorance, response to praise/contempt.
3. Behavioral rules under ordinary and high-stakes conditions.
4. Goals, values, identity claims, and protected vulnerabilities.
5. Emotional activation and recovery patterns.
6. Response to winning, losing, correction, and uncertainty.
7. Authority and status behavior.
8. Learning/teaching/craft cognition.
9. Relationship-specific deltas.
10. Ordinary-state calibration.
11. Negative constraints — behavior that would be surprising without intervening development.
12. Counterevidence and unresolved conditions.

### 7.2 Readiness states

The readiness ledger uses:

- `background` — identifiable but insufficiently diagnostic.
- `tracked` — recurring evidence exists; no stable conditional model yet.
- `emerging` — several model dimensions recur across contexts.
- `substantial` — enough breadth for a serious analytical profile, but important reconstruction gaps remain.
- `monograph_ready` — voice, behavior, relationships, ordinary/high-stakes contrast, and counterevidence are broad enough for a dedicated model.
- `validated_model` — a monograph/model has survived an explicit later-source or adversarial validation gate.

Do not promote by volume count alone.

### 7.3 Prediction and validation

At checkpoints, freeze only predictions that are genuinely diagnostic.

A prediction should specify:

- condition;
- expected behavioral/linguistic direction;
- known exception clauses;
- target character or relationship;
- confidence.

Later evidence is scored as `CONFIRM`, `PARTIAL`, `CONTRADICT`, or `NON-DIAGNOSTIC/UNTESTED` before model revision.

Because the analyst may possess latent prior knowledge, V2 validation is **procedurally prospective, not claimed to be epistemically blind**. The V1 Soma holdout audit retains its own stronger, separately documented provenance.

## 8. Longitudinal checkpoint cadence

Default checkpoints occur after:

- V01-V06;
- V07-V12;
- V13-V18;
- V19-V24;
- V25-V30;
- V31-V36.

An additional arc checkpoint may be created only when a major transition would otherwise be analytically lost. Do not create redundant checkpoints for symmetry.

Each checkpoint should:

- synthesize literary development without erasing volume-local ambiguity;
- reconcile live ledgers;
- promote/demote character reconstruction readiness;
- adjudicate frozen predictions;
- freeze new prospective claims;
- identify specialist-synthesis candidates;
- record V1-to-V2 transitions when applicable.

Checkpoint documents are frozen once closed. Later corrections route through claim-revision infrastructure rather than silent rewriting.

## 9. Longitudinal ledgers

The V2 corpus maintains these distinct responsibilities:

- `../03 Longitudinal Ledgers/SHOKUGEKI_CHARACTER_STATE_AND_RECONSTRUCTION_LEDGER.md`
- `../03 Longitudinal Ledgers/SHOKUGEKI_CHARACTER_RECONSTRUCTION_READINESS_LEDGER.md`
- `../03 Longitudinal Ledgers/SHOKUGEKI_ENSEMBLE_JAPANESE_VOICE_LEDGER.md`
- `../03 Longitudinal Ledgers/SHOKUGEKI_RELATIONSHIP_DYNAMICS_LEDGER.md`
- `../03 Longitudinal Ledgers/SHOKUGEKI_CULINARY_IDEOLOGY_CRAFT_AND_PEDAGOGY_LEDGER.md`
- `../03 Longitudinal Ledgers/SHOKUGEKI_INSTITUTION_POWER_AND_LEGITIMACY_LEDGER.md`
- `../03 Longitudinal Ledgers/SHOKUGEKI_COMPETITION_EVALUATION_AND_GROWTH_LEDGER.md`
- `../03 Longitudinal Ledgers/SHOKUGEKI_VISUAL_FOOD_DRAMATURGY_AND_BODY_COMEDY_LEDGER.md`

Do not duplicate entire cumulative tables in sequential readings. The volume artifact records the delta; the ledger records the current longitudinal state.

The V1 Soma voice/behavior/relationship ledgers are frozen bounded artifacts and are not reused as mutable V2 ensemble ledgers.

## 10. Treatment of V1 Soma artifacts

The completed V1 project is a methodological asset and a contamination risk if used carelessly.

Rules:

1. Do not edit the V1 sequential readings, final model, validation audit, or three V1 ledgers for V2 findings.
2. [`SHOKUGEKI_SOMA_FINAL_CHARACTER_MODEL.md`](../04%20Final%20Character%20Model/SHOKUGEKI_SOMA_FINAL_CHARACTER_MODEL.md) remains the best completed Soma reconstruction until a full-series V2 Soma model is ready.
3. At V01, V03, V08, V13, V19, V25, V30, and V36, perform the V2 deep reading first. Only afterward compare the corresponding V1 character reading.
4. Route differences through `../06 Evidence and Indexes/SHOKUGEKI_V1_TO_V2_CROSSWALK.md` and later claim-revision infrastructure.
5. Preserve the V25/V30/V36 prediction freezes and validation audit exactly; V2 cannot retroactively improve the old experiment.
6. A later V2 Soma monograph may supersede the V1 final model for **full-series reconstruction authority**, while the V1 audit remains permanently authoritative about what the sampled holdout experiment demonstrated.

## 11. Specialist synthesis and final synthesis gates

Do not predeclare every supporting character or theme worthy of a standalone document.

Create a specialist synthesis when a dimension:

- recurs across many volumes;
- has accumulated enough evidence that the ledger is becoming a retrieval burden;
- supports a distinct thesis not reducible to the master synthesis;
- or needs independent character-reconstruction access.

Likely candidates include culinary authorship, Totsuki/institutional legitimacy, competition and pedagogy, food/body dramaturgy, family/inheritance, ensemble relationship systems, and character monographs for sufficiently ready characters. These are hypotheses about future artifact needs, not guaranteed outputs.

The full-series synthesis is written only after V36, the final checkpoint, ledgers, claim revisions, and major character/specialist syntheses are stable.

## 12. Per-volume output contract

A strong `SHOKUGEKI_VXX_DEEP_READING.md` should normally contain:

1. YAML authority metadata.
2. Phase-0 source lock and content boundary.
3. Local-state starting context.
4. Volume thesis.
5. Chapter/structural map proportional to analysis.
6. Literary and thematic analysis.
7. Manga-form / visual analysis.
8. Character deltas for diagnostically important characters.
9. Japanese voice/register findings.
10. Relationship changes.
11. Culinary ideology/craft/pedagogy findings.
12. Institution/competition findings when present.
13. Visual food dramaturgy/body-comedy findings when present.
14. Strongest counterevidence / alternative readings.
15. V1 Soma comparison only after the fresh reading, when applicable.
16. Claim transitions and ledger updates.
17. Open questions.
18. Frozen prospective predictions, limited to genuinely diagnostic claims.
19. Exact source locators for major claims.
20. Administrative verification and next volume.

## 13. Governing success criterion

The V2 project succeeds if, at the end of V36, it can answer both kinds of question without collapsing one into the other:

> **What is *Shokugeki no Soma* doing as a complete manga — aesthetically, thematically, institutionally, relationally, and philosophically?**

and

> **Given a new but well-specified situation, what can the original Japanese manga reliably predict about how a sufficiently evidenced character would think, speak, decide, compete, cooperate, teach, support, fail, and relate to other people?**

Literary richness and reconstructive precision are complementary outputs, not substitutes.
