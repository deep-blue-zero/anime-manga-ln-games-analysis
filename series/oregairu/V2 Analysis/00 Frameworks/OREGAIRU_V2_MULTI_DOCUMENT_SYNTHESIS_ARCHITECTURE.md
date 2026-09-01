---
title: "Oregairu V2 Multi-Document Synthesis Architecture and Execution Phases"
project: "Yahari Ore no Seishun Love Comedy wa Machigatteiru. / Oregairu"
version: "2.2"
status: "governing architecture"
companion_method: "OREGAIRU_V2_ANALYTICAL_METHOD.md"
artifact_prefix: "OREGAIRU_V2_"
last_updated: "2026-08-19T16:20:00-04:00"
architecture_amendment: "Phase 8.5 reconstruction models + shared everyday-life/preferences evidence infrastructure"
---

# OREGAIRU V2 MULTI-DOCUMENT SYNTHESIS ARCHITECTURE AND EXECUTION PHASES

## Purpose

This document defines the production architecture for the Oregairu V2 project.

Its job is different from the analytical method.

The companion method answers:

> **How should each volume, scene, claim, character, relationship, and piece of evidence be read?**

This architecture answers:

> **What artifacts will the project produce, in what order, with what dependencies, and how will the finished corpus be validated and packaged?**

The V2 project is designed as a second-pass reconstruction rather than an unstructured rewrite.

The intended outcome is a durable analytical corpus consisting of:

- verified source inventory;
- canonical per-volume deep readings;
- longitudinal ledgers;
- V1 revision history;
- specialist synthesis documents;
- one continuous full-series synthesis;
- character reconstruction and simulation models for evidence-sufficient cast members;
- reader-facing corpus map;
- provenance and audit artifacts.

The earlier Oregairu analysis remains valuable, but it enters this project as a **revision corpus**. It is evidence about what the first analytical pass concluded, not evidence about what the novels say.

---

# 1. Corpus boundary

## 1.1 Mainline literary core

The central governing corpus is the original Japanese light-novel sequence:

- Volumes 1–14;
- canonical bonus/interstitial volumes available for the project, including 6.5, 7.5, 10.5, and 14.5;
- 6.75 is retained only as publication genealogy/source-history under the current source lock and is **not** a standalone canonical V2 source unless a separately admissible source is later established.

The final source inventory should determine exact bibliographic order and edition identity.

---

## 1.2 Supplementary material

Drama CDs, bonus stories, and other canonical supplementary material may enter where they provide:

- ordinary-life characterization;
- alternate viewpoints;
- relational continuity;
- voice/performance evidence;
- chronological bridge material.

Their authority must be labeled rather than silently equated with numbered mainline prose.

---

## 1.3 Out-of-core continuations and alternatives

### Shin

Treat as a possible **post-ending continuation annex** after the V2 mainline corpus has stabilized.

It may test whether the mainline synthesis survives later ordinary-life continuation.

### Ketsu

Treat as **alternate-continuity comparative material**.

It must not be used to retroactively change what the canonical mainline establishes.

---

# 2. Preferred source configuration

The ideal V2 working source is:

> **Japanese EPUB + existing Japanese PDF**

### EPUB role

Use as:

- primary text layer;
- search layer;
- lexical analysis layer;
- quotation layer;
- chapter extraction layer;
- source-locator layer.

### PDF role

Use as:

- fixed-page verification;
- illustration/typography source;
- printed-pagination locator;
- fallback when EPUB extraction is suspicious.

The project should not require duplicate re-upload of PDFs already securely retrievable.

Volume 14.5 should be reintroduced in a directly retrievable form before the relevant phase if it is not available in the active source set.

---

# 3. Artifact classes

The project produces six major artifact classes.

## 3.1 Governing documents

- `OREGAIRU_V2_ANALYTICAL_METHOD.md`
- `OREGAIRU_V2_MULTI_DOCUMENT_SYNTHESIS_ARCHITECTURE.md`

These define how all later work is performed.

---

## 3.2 Source and provenance documents

Recommended:

- `OREGAIRU_V2_SOURCE_INVENTORY.md`
- `OREGAIRU_V2_CORPUS_MANIFEST.md`
- `OREGAIRU_V2_V1_CLAIM_AUDIT.md`
- `OREGAIRU_V2_PROJECT_DECISIONS.md`

Optional machine-readable mirrors may be added later.

---

## 3.3 Canonical volume deep readings

Every numbered and included bonus volume receives a permanent Markdown artifact.

Examples:

- `OREGAIRU_V2_V01_DEEP_READING.md`
- `OREGAIRU_V2_V02_DEEP_READING.md`
- ...
- `OREGAIRU_V2_V06_5_DEEP_READING.md`
- `OREGAIRU_V2_V07_5_DEEP_READING.md`
- ...
- `OREGAIRU_V2_V10_5_DEEP_READING.md`
- ...
- `OREGAIRU_V2_V14_DEEP_READING.md`
- `OREGAIRU_V2_V14_5_DEEP_READING.md`

These are the evidentiary middle layer between the original sources and the final synthesis.

---

## 3.4 Longitudinal ledgers

Recommended final ledgers:

1. `LEDGER_HACHIMAN_EPISTEMIC_AND_NARRATORIAL.md`
2. `LEDGER_CHARACTER_STATE.md`
3. `LEDGER_RELATIONSHIP_STATE.md`
4. `LEDGER_REQUEST_INTERVENTION_ETHICS.md`
5. `LEDGER_AUTHENTICITY_HONMONO.md`
6. `LEDGER_DEPENDENCY_AUTONOMY.md`
7. `LEDGER_SOCIAL_ROLE_AND_PERFORMANCE.md`
8. `LEDGER_JAPANESE_VOICE.md`
9. `LEDGER_PRIMARY_SOURCE_LOCATORS.md`
10. `LEDGER_V1_TO_V2_REVISION.md`

Working forms may be updated during the reread; final forms are stabilized after the complete source pass.

---

## 3.5 Specialist synthesis documents

These form the mature human-readable analytical layer.

The recommended architecture is `00–14`, with an optional `15` only if the evidence requires a dedicated Hachiman/Yukino document.

---

## 3.6 Delivery and audit artifacts

Recommended:

- `CORPUS_MANIFEST.md`
- `SOURCE_CHECKSUMS.sha256`
- `ARTIFACT_CHECKSUMS.sha256`
- `DELIVERY_AUDIT.md`
- `README.md` or the numbered `00_README_AND_CORPUS_MAP.md`
- final ZIP archive

The original copyrighted source novels should not be redistributed inside the analytical delivery package.

---

# 4. Final multi-document synthesis architecture

## 00 — `00_README_AND_CORPUS_MAP.md`

### Function

Reader-facing guide written near the end of the project.

### Contents

- scope;
- source hierarchy;
- spoiler boundaries;
- evidence labels;
- naming conventions;
- mainline versus supplementary distinction;
- document map;
- recommended reading paths;
- mature executive thesis;
- glossary of recurring concepts;
- provenance notes;
- how to trace claims back to Japanese sources.

### Dependency

Written only after specialist documents have stabilized terminology.

---

## 01 — `01_SERIES_ARCHITECTURE_AND_VOLUME_PROGRESSION.md`

### Function

Explain how the complete sequence develops rather than summarize every plot.

### Core questions

- What problem is each major movement solving?
- Which apparent solutions create later problems?
- How does the series change its own question over time?
- How does the Service Club move from institution to relationship?
- How does "helping" become inseparable from desire?
- How does the ending answer earlier structures without purifying them?

### Inputs

All volume readings, checkpoint freezes, character and relationship ledgers.

---

## 02 — `02_HIKIGAYA_HACHIMAN_NARRATION_SELF_DECEPTION_AND_GROWTH.md`

### Function

Definitive Hachiman character/narrator study.

### Required domains

- narration;
- social intelligence;
- cynicism;
- comedy;
- self-deprecation;
- self-sacrifice;
- desire to be needed;
- fear of rejection;
- moral seriousness;
- control through self-destruction;
- development after 「本物」;
- romantic desire;
- final self-authorship.

### Special requirement

Must distinguish:

- what Hachiman sees accurately;
- what he explains badly;
- what he refuses to name;
- what later behavior reveals.

---

## 03 — `03_YUKINOSHITA_YUKINO_SELFHOOD_COMPETENCE_FAMILY_AND_DESIRE.md`

### Function

Definitive Yukino character study.

### Required domains

- competence;
- isolation;
- imitation and differentiation;
- helping as identity;
- Haruno;
- mother/family expectations;
- independence;
- dependence;
- vulnerability;
- desire;
- relationship to Hachiman;
- relationship to Yui;
- final choice and future.

### Guardrail

Do not define Yukino primarily through Hachiman's interpretation of her.

---

## 04 — `04_YUIGAHAMA_YUI_ATMOSPHERE_ACCOMMODATION_DESIRE_AND_LOSS.md`

### Function

Definitive Yui character study.

### Required domains

- social intelligence;
- atmosphere management;
- kindness;
- accommodation;
- self-suppression;
- desire;
- jealousy;
- moral agency;
- willingness to preserve the triangle;
- willingness to ask for more;
- relationship to Yukino;
- relationship to Hachiman;
- loss and continuation.

### Guardrail

Do not reduce Yui to "nice girl who loses the romance."

---

## 05 — `05_THE_SERVICE_CLUB_TRIAD_RELATIONSHIP_AND_ROMANTIC_CHOICE.md`

### Function

Analyze the Service Club as a dynamic three-person system.

### Required domains

- formation;
- requests;
- mutual recognition;
- triangulation;
- romantic asymmetry;
- friendship and rivalry;
- silence;
- obligation;
- jealousy;
- ordinary presence;
- the "genuine" request;
- final choice;
- what survives the choice.

### Central principle

> The romantic resolution does not erase the triad's prior reality.

---

## 06 — `06_THE_GENUINE_AUTHENTICITY_PERFORMANCE_AND_MIXED_MOTIVES.md`

### Function

Trace authenticity without treating sincerity as purity.

### Required domains

- 「本物」;
- social performance;
- lies;
- role behavior;
- politeness;
- hidden desire;
- mixed motives;
- conflict;
- mutual recognition;
- the difference between "not fake" and "genuine."

### Strong test

The final thesis should explain why a relationship can contain:

- desire;
- selfishness;
- duty;
- fear;
- performance;
- care;

and still be more genuine than one built around avoiding those contradictions.

---

## 07 — `07_HELPING_SELF_SACRIFICE_DEPENDENCY_AND_AUTONOMY.md`

### Function

Ethical analysis of the Service Club's intervention model.

### Required domains

- request ownership;
- Hachiman methods;
- Yukino methods;
- Yui's mediating role;
- immediate success versus long-term cost;
- self-sacrifice;
- humiliation;
- reputation;
- autonomy;
- dependence;
- alleged codependency;
- chosen interdependence.

### Central test

Do not assume that either:

- effective outcomes justify methods, or
- emotional cost proves methods never worked.

---

## 08 — `08_SOCIAL_SYSTEMS_REPUTATION_GROUPS_AND_SCHOOL_POLITICS.md`

### Function

Treat Oregairu as social-system fiction.

### Required domains

- Hayama's group;
- Miura;
- Ebina;
- Sagami;
- Rumi;
- Iroha;
- councils;
- festivals;
- elections;
- prom;
- face-saving;
- hierarchy;
- reputation;
- belonging;
- leadership;
- institutional constraints.

### Comparative role

This document should make clear where Hachiman's social analysis is insightful and where it becomes reductive.

---

## 09 — `09_HARUNO_HAYAMA_HIRATSUKA_KOMACHI_AND_COUNTER_GAZES.md`

### Function

Analyze major counter-gazes that diagnose or redirect the protagonists.

### Core figures

- Haruno;
- Hayama;
- Hiratsuka;
- Komachi.

Additional figures may enter as needed.

### Central questions

- Who sees Hachiman most clearly?
- Who sees Yukino most clearly?
- Who weaponizes insight?
- Who provides adult ethical language?
- Who represents alternative models of care or social competence?

---

## 10 — `10_FAMILY_ADULTHOOD_FUTURITY_AND_THE_PROBLEM_OF_CHOICE.md`

### Function

Analyze movement from school problems toward adult consequence.

### Required domains

- Yukinoshita family;
- family role;
- social class;
- career;
- future;
- graduation;
- adulthood;
- institutional inheritance;
- choosing versus being chosen for;
- responsibility after romantic resolution.

---

## 11 — `11_JAPANESE_VOICE_NARRATIVE_STYLE_COMEDY_AND_INTERTEXTUALITY.md`

### Function

Dedicated language/form study.

### Required domains

- Hachiman prose voice;
- spoken versus narrated self;
- Yukino register;
- Yui register;
- Iroha persona;
- Haruno ambiguity;
- address terms;
- politeness shifts;
- modality;
- ellipsis;
- recurring lexical clusters;
- jokes;
- anime/manga/game/literary references;
- genre self-consciousness.

### Purpose

Prevent linguistic evidence from being scattered so widely that it becomes difficult to use comparatively.

---

## 12 — `12_SUPPLEMENTARY_VOLUMES_DRAMA_CDS_AND_ORDINARY_LIFE.md`

### Function

Evaluate what material outside the numbered mainline contributes.

### Required domains

- 6.5;
- 6.75 publication genealogy/source-history only; do not treat it as a standalone canonical source under the current lock;
- 7.5;
- 10.5;
- 14.5;
- drama/audio material in scope.

### Analytical emphasis

Ordinary-life material is especially valuable for determining what relationships look like when they are not being tested by a crisis.

---

## 13 — `13_EVIDENCE_LOCATOR_AND_FIRST_PASS_REVISION_LEDGER.md`

### Function

Bridge mature synthesis claims back to source and document V1→V2 revision.

### Contents

- high-value claim inventory;
- source locators;
- relevant volume analyses;
- confidence status;
- counterevidence;
- V1 claim status;
- reason for revision.

### Traceability target

> synthesis claim → specialist doc → volume analysis → locator → Japanese source

---

## 14 — `14_OREGAIRU_FULL_SERIES_SYNTHESIS.md`

### Function

Continuous literary argument written last.

### It should not be

- a pasted summary of Documents 01–13;
- a giant encyclopedia;
- a character-by-character report.

### It should be

A sustained argument explaining what *Oregairu* becomes across the entire run.

A provisional orientation to test rather than assume is:

> Oregairu begins with a boy who believes social falsehood can be escaped through cynical clarity and ends by asking whether a relationship can become genuine not by purifying itself of selfishness, performance, dependence, and pain, but by becoming capable of naming, negotiating, and continuing through them.

The final synthesis is free to reject or revise that formulation.

---

## Phase 8.5 reconstruction suite - `OREGAIRU_V2_CHAR_*_RECONSTRUCTION_MODEL.md`

### Function

Compile the completed literary-analysis corpus into operational character models optimized for:

- behavioral reconstruction;
- relationship-conditioned decision inference;
- Japanese speech/register reconstruction;
- dialogue and interaction simulation in novel scenarios;
- explicit uncertainty and out-of-distribution control.

These are **derived-use artifacts**, not a new literary-authority layer. They translate already-audited evidence into a form that is easier to use for simulation.

### Initial eligible characters

The current V2 corpus supports eight architecture-defined models:

1. `OREGAIRU_V2_CHAR_HACHIMAN_RECONSTRUCTION_MODEL.md`
2. `OREGAIRU_V2_CHAR_YUKINO_RECONSTRUCTION_MODEL.md`
3. `OREGAIRU_V2_CHAR_YUI_RECONSTRUCTION_MODEL.md`
4. `OREGAIRU_V2_CHAR_IROHA_RECONSTRUCTION_MODEL.md`
5. `OREGAIRU_V2_CHAR_KOMACHI_RECONSTRUCTION_MODEL.md`
6. `OREGAIRU_V2_CHAR_HARUNO_RECONSTRUCTION_MODEL.md`
7. `OREGAIRU_V2_CHAR_HIRATSUKA_RECONSTRUCTION_MODEL.md`
8. `OREGAIRU_V2_CHAR_HAYAMA_RECONSTRUCTION_MODEL.md`

Do not create additional character models for symmetry. A later character becomes eligible only when the corpus contains enough longitudinal behavioral evidence and relationship-conditioned linguistic evidence to support a distinct reconstruction responsibility.

### Authority boundary

Reconstruction models must obey the following precedence:

1. Japanese primary sources control exact wording and source fact.
2. Document 13 controls publication-safe mature claim wording and post-Phase-6 dispositions.
3. Phase-4 character, relationship, voice, social-role, epistemic, and intervention ledgers control longitudinal derived state within their domains.
4. Phase-5 specialist documents and Document 14 supply mature interpretive context.
5. Sequential deep readings and checkpoints supply chronology and scene-level development.
6. Reconstruction-model heuristics are operational extrapolations and may not override any higher layer.

A reconstruction model may say **"high-confidence simulation rule"** without claiming **"the novel explicitly theorizes this rule."**

### Derived-first, source-verified workflow

Do **not** reread the complete novel corpus for each model.

For each character:

1. compile the model from the existing derived V2 corpus;
2. build the behavioral and relationship-conditioned speech matrices;
3. mark thin, contradictory, or over-generalized cells;
4. reopen only the Japanese primary scenes needed to verify representative exemplars or resolve those cells;
5. record the targeted source escalation and its result;
6. freeze the model only after the gaps that materially affect simulation are resolved or explicitly left OPEN.

### Shared everyday-life / preferences evidence infrastructure

Phase 8.5 additionally maintains one mutable cumulative ledger:

`OREGAIRU_V2_EVERYDAY_LIFE_PREFERENCES_AND_MATERIAL_HABITS_LEDGER.md`

This ledger exists because the literary synthesis and Phase-4 claim-routing infrastructure intentionally compress much of the low-stakes texture needed to answer a different reconstruction question: **what is it actually like to spend ordinary time with this person?**

For this evidence class, the normal derived-first workflow is intentionally reversed:

> **Japanese primary source -> contextual everyday-life observation -> evidence-typed ledger row -> reconstruction-model everyday-life profile -> scenario inference**

The existing `OREGAIRU_V2_PRIMARY_SOURCE_LOCATOR_LEDGER.md` remains frozen. Do not mutate it to absorb Phase-8.5 preference evidence. The new ledger may cite an existing locator when useful, but it owns the distinct semantic responsibility of accumulating mundane choices, routines, tastes, habits, material practices, and their inference limits.

The ledger is **shared across the eligible cast**, not duplicated per character. It is updated incrementally as each reconstruction model is built or revised. A completed character slice may be treated as canonical for that character while the cumulative ledger remains mutable for later characters.

#### Everyday-life evidence classes

Use controlled evidence labels including, as applicable:

- `EXPLICIT_PREFERENCE`;
- `EXPLICIT_AVERSION`;
- `SELF_DESCRIPTION`;
- `VOLUNTARY_SELECTION`;
- `REPEATED_SELECTION`;
- `HABITUAL_PRACTICE`;
- `OBSERVED_ENJOYMENT`;
- `COMPETENCE`;
- `SOCIAL_ACCOMMODATION`;
- `CONSTRAINT_DRIVEN`;
- `STATE_DEPENDENT`;
- `OTHER_REPORT`;
- `NARRATOR_INFERENCE`;
- `ANALYTICAL_INFERENCE`.

A row may carry multiple labels when the scene supports multiple evidentiary functions.

#### Required row fields

Each material row should identify at least:

- stable row ID;
- character;
- era/state;
- everyday-life domain;
- observed choice, habit, preference, or material practice;
- evidence class;
- relationship/social setting and relevant constraints;
- deterministic Japanese source locator;
- confidence;
- **inference ceiling / what the evidence does not entitle us to conclude**.

The last field is mandatory. Examples: competence does not prove enjoyment; eating something once does not prove preference; accepting another person's invitation does not prove activity preference; ownership does not prove sentimental attachment; narrator inference about another person's taste is not first-person confirmation; a state-dependent crisis behavior is not a baseline routine.

#### Everyday-life domains

Mine proportionally for evidence concerning food/drink, cooking, reading, manga/anime/games/radio/TV/online media, music, animals, hobbies/collections, sports/exercise, study/work habits, sleep and day rhythm, household behavior, shopping/spending, clothing/fashion, preferred environments, cafes/restaurants, leisure, transport/travel, phone/text habits, gift selection, sentimental objects, preferred social-group size, crowd/noise tolerance, boredom behavior, small irritants, and recurring ways of doing nothing.

Absence is also information. If the corpus does not establish a music genre, favorite food beyond a narrower demonstrated preference, adult routine, or similar field, the reconstruction model should say **unknown** rather than synthesize plausible trivia.

### Mandatory primary-source escalation triggers

Reopen the Japanese source when any of the following applies:

- a relationship-conditioned register cell rests on too few examples;
- the model needs an exact Japanese exemplar not already verified in the V2 evidence chain;
- a behavioral claim depends mainly on Hachiman's narration rather than directly observed speech/action;
- early/middle/late character-state differences remain ambiguous;
- an iconic lexical or comic marker risks being overused because absence/frequency is under-modeled;
- two derived artifacts disagree about motive, register, or behavioral state;
- a proposed simulation rule extrapolates beyond situations represented in the corpus;
- a supporting character's dialogue corpus is substantially thinner than the core trio's.

Targeted source reopening is a verification instrument, not permission to restart the sequential reread.

### Required model schema

Every reconstruction model should contain, at minimum:

1. **identity, scope, and use boundary**;
2. **era/state variants** - early, middle, late, post-V14.5 where materially distinct;
3. **baseline attentional model** - what the character notices, prioritizes, and systematically underweights;
4. **motivational hierarchy and decision heuristics**;
5. **emotional defenses, self-deceptions, and failure modes**;
6. **behavioral-state model** - common triggers, transitions, and likely actions;
7. **relationship-conditioned behavior matrix**;
8. **Japanese speech/register matrix** - self-reference, address, politeness, sentence endings, modality, hedging, ellipsis, requests, refusals, teasing, apology, and escalation shifts;
9. **narrated thought versus spoken output**, where relevant, especially for Hachiman;
10. **conversational moves and turn-taking habits**;
11. **humor, affection, irritation, embarrassment, and conflict expression**;
12. **stress escalation and de-escalation behavior**;
13. **negative constraints and caricature traps** - what the character is often generated doing incorrectly, what markers must not be spammed, and what the character would rarely say/do;
14. **scenario-transfer rules** and out-of-distribution boundaries;
15. **diagnostic Japanese exemplars** with deterministic source routes;
16. **confidence matrix and evidentiary gaps**;
17. **simulation checklist** for future novel-scenario use;
18. **provenance and source-escalation log**;
19. **Everyday Life, Preferences, and Material Habits** - a compiled character-facing profile derived primarily from the shared Phase-8.5 everyday-life ledger, including demonstrated tastes/routines, relationship-conditioned ordinary behavior, material habits, mundane unknowns, and explicit anti-hallucination limits.

### Relationship-conditioning requirement

A character model must not treat voice as one invariant register.

Where evidence permits, it should distinguish behavior and speech by counterpart and setting. Examples include:

- Hachiman -> Yukino / Yui / Komachi / Iroha / Hayama / Hiratsuka / unfamiliar peers;
- Yukino -> Hachiman / Yui / Haruno / mother / Iroha / Service Club clients / formal institutional settings;
- Yui -> Hachiman / Yukino / Miura-group peers / family / Iroha / mixed public settings.

Equivalent relationship matrices should be built for the supporting models at the granularity the evidence can actually sustain.

### Negative-constraint principle

Reconstruction quality depends on modeling **absence** as well as presence.

The suite must explicitly guard against transformations such as:

- Hachiman -> endless cynical pseudo-philosophical monologue;
- Yukino -> permanently icy insult machine;
- Yui -> permanent hesitation/filler register;
- Iroha -> rejection-gag repetition;
- Komachi -> constant "Komachi points" performance;
- Haruno -> omniscient cryptic oracle;
- Hiratsuka -> aphorism dispenser;
- Hayama -> generic pleasant popular boy.

Salient markers are diagnostic only when their frequency, audience, and emotional conditions are also modeled.

### Simulation confidence classes

Each model should distinguish:

- **HIGH - behavior**: strong longitudinal support for likely action/decision;
- **HIGH - register**: strong relationship-conditioned Japanese evidence;
- **SUPPORTED EXTRAPOLATION**: novel situation inferred from stable rules but not directly represented;
- **UNDERDETERMINED**: multiple outcomes remain comparably plausible;
- **SOURCE ESCALATION REQUIRED**: prediction should not be made without reopening source evidence.

### Cross-model consistency audit

Before Phase 8.5 closes, test the models in shared novel scenarios that force different characters to respond to the same stimulus.

The goal is not to choose a single "correct" improvised scene. The audit should confirm that:

- each character attends to different features where the corpus supports that difference;
- relationship history changes behavior and register;
- iconic markers are not over-produced;
- era-specific models do not leak later growth backward;
- generated behavior remains compatible with Document 13's audited claim boundaries;
- disagreement and uncertainty remain possible rather than being optimized into thematic harmony.

### Canonical home

Store the suite under:

`06 Continuous Synthesis/Character Reconstruction Models/`

The folder is a retrieval convenience inside the existing canonical analytical root, not a new top-level corpus.

---

## Optional 15 — `15_HACHIMAN_AND_YUKINO_RELATIONSHIP_DEEP_DIVE.md`

Create only if Document 05 becomes overloaded.

### Trigger condition

Use only if the reread shows that Hachiman/Yukino requires substantially more dedicated space than can be accommodated without crowding:

- Yukino/Yui;
- Hachiman/Yui;
- triadic dynamics;
- final-choice analysis.

Do not create this document merely to increase corpus size.

---

# 5. Execution phases

## Phase 0 — Corpus lock and source inventory

### Objective

Establish exactly what primary material exists before analysis begins.

### Actions

- verify each Japanese EPUB/PDF;
- record filenames;
- record byte sizes;
- compute SHA-256 where possible;
- map volumes and bonus volumes;
- identify duplicates or alternate editions;
- map chapter structures;
- confirm publication order;
- confirm 14.5 availability;
- inventory drama/audio supplements;
- create stable source IDs.

### Outputs

- `OREGAIRU_V2_SOURCE_INVENTORY.md`
- `OREGAIRU_V2_PROJECT_DECISIONS.md`
- initial source checksum file

### Exit criterion

No ambiguity remains about what source file corresponds to each analyzed work.

---

## Phase 1 — V1 audit and hypothesis extraction

### Objective

Recover the value of the earlier project without importing its conclusions as truth.

### Actions

Extract major V1 claims concerning:

- Hachiman;
- Yukino;
- Yui;
- Haruno;
- Hayama;
- Hiratsuka;
- Komachi;
- Iroha;
- Service Club dynamics;
- self-sacrifice;
- authenticity;
- dependency;
- social performance;
- ending interpretation.

Classify each as:

- high-confidence;
- plausible;
- weakly sourced;
- overcompressed;
- potentially overclaimed;
- unresolved.

### Output

`OREGAIRU_V2_V1_CLAIM_AUDIT.md`

### Exit criterion

The earlier analysis has been converted into a testable hypothesis ledger.

---

## Phase 2 — Sequential Japanese reread

### Objective

Rebuild the corpus volume by volume under the V2 method.

### Actions for each volume

1. verify source;
2. read in publication order;
3. freeze prospective interpretation;
4. perform narratorial audit;
5. update character/relationship/request ledgers;
6. audit Japanese language;
7. conduct adversarial reading;
8. perform retrospective pass;
9. compare against V1;
10. record source locators;
11. update cumulative hypotheses.

### Outputs

One canonical deep reading per volume.

### Critical rule

Do not draft mature full-series synthesis prose during this phase.

The project must remain capable of surprise.

---

## Phase 3 — Controlled checkpoint freezes

### Objective

Preserve what the series looked like at major developmental stages.

### Suggested checkpoints

### A — Early Service Club formation

Focus:

- Hachiman's initial worldview;
- Yukino's competence ethic;
- Yui's social mediation;
- first request structures.

### B — Cultural-festival / self-sacrifice consolidation

Focus:

- reputation;
- social damage;
- "effective" ugly solutions;
- emerging concern with method.

### C — Kyoto / election / Christmas crisis

Focus:

- Service Club fracture;
- avoidance;
- social role;
- Hachiman's request for something genuine.

### D — Post-「本物」 restructuring

Focus:

- desire becoming harder to avoid;
- changing dependence;
- shifting Yukino/Yui/Hachiman permissions.

### E — Prom / final-choice movement

Focus:

- autonomy;
- family;
- future;
- romantic choice;
- what the Service Club becomes afterward.

### Final — post-14.5

Focus:

- ordinary-life stabilization;
- whether the ending thesis survives non-crisis material.

### Outputs

Checkpoint notes or frozen ledger snapshots.

### Exit criterion

The later synthesis can reconstruct the evolution of interpretation rather than only its endpoint.

---

## Phase 4 — Longitudinal ledger consolidation

### Objective

Turn cumulative working notes into complete series-level evidence structures.

### Actions

For each ledger:

- remove duplicates;
- reconcile terminology;
- preserve contradictions;
- assign confidence;
- attach source locators;
- mark retrospective revisions.

### Outputs

Final versions of the ten longitudinal ledgers.

### Exit criterion

Every major character/theme/relationship claim has a longitudinal evidence trail.

---

## Phase 5 — Specialist synthesis production

### Objective

Write Documents 01–12 from evidence rather than conversation memory.

### Recommended drafting order

1. `01_SERIES_ARCHITECTURE_AND_VOLUME_PROGRESSION.md`
2. `02_HIKIGAYA_HACHIMAN_NARRATION_SELF_DECEPTION_AND_GROWTH.md`
3. `03_YUKINOSHITA_YUKINO_SELFHOOD_COMPETENCE_FAMILY_AND_DESIRE.md`
4. `04_YUIGAHAMA_YUI_ATMOSPHERE_ACCOMMODATION_DESIRE_AND_LOSS.md`
5. `05_THE_SERVICE_CLUB_TRIAD_RELATIONSHIP_AND_ROMANTIC_CHOICE.md`
6. `06_THE_GENUINE_AUTHENTICITY_PERFORMANCE_AND_MIXED_MOTIVES.md`
7. `07_HELPING_SELF_SACRIFICE_DEPENDENCY_AND_AUTONOMY.md`
8. `08_SOCIAL_SYSTEMS_REPUTATION_GROUPS_AND_SCHOOL_POLITICS.md`
9. `09_HARUNO_HAYAMA_HIRATSUKA_KOMACHI_AND_COUNTER_GAZES.md`
10. `10_FAMILY_ADULTHOOD_FUTURITY_AND_THE_PROBLEM_OF_CHOICE.md`
11. `11_JAPANESE_VOICE_NARRATIVE_STYLE_COMEDY_AND_INTERTEXTUALITY.md`
12. `12_SUPPLEMENTARY_VOLUMES_DRAMA_CDS_AND_ORDINARY_LIFE.md`

### Why this order

Character and relational interpretations depend on a stable volume architecture.

Conceptual documents depend on stable character/relationship conclusions.

Language and supplementary documents should be written after the primary dramatic architecture is mature so they can refine rather than prematurely dictate it.

---

## Phase 6 — Adversarial Japanese-source audit

### Objective

Stress-test the strongest mature claims.

### Actions

Select the most consequential claims from Documents 01–12.

For each:

1. identify the source chain;
2. reopen relevant Japanese passages;
3. search for counterexamples;
4. inspect passages that appear to contradict the claim;
5. verify Japanese wording;
6. verify whether narrator inference has been mistaken for fact;
7. downgrade, narrow, or rewrite where necessary.

### Required attitude

The goal is not to defend the synthesis.

The goal is to break weak parts before publication.

### Output

Revision notes feeding Document 13.

---

## Phase 7 — Evidence locator and V1 revision document

### Objective

Create the explicit bridge between V2's mature conclusions, the Japanese sources, and the earlier project.

### Actions

Build a curated ledger of:

- major claim;
- relevant specialist document;
- source volume;
- Japanese locator;
- confidence;
- counterevidence;
- V1 status;
- V2 revision reason.

### Output

`13_EVIDENCE_LOCATOR_AND_FIRST_PASS_REVISION_LEDGER.md`

### Exit criterion

The project can explain not only what it concludes, but why V2 differs from V1.

---

## Phase 8 — Full-series synthesis

### Objective

Write the continuous reader-facing literary argument.

### Source basis

Documents 01–13 plus the canonical volume readings and ledgers.

### Rules

- do not reproduce specialist-document section structure;
- do not force every character into equal space;
- privilege the series' strongest explanatory through-lines;
- distinguish interpretation from fact;
- retain unresolved tensions;
- include only enough plot to support argument.

### Output

`14_OREGAIRU_FULL_SERIES_SYNTHESIS.md`

### Exit criterion

A reader unfamiliar with the project infrastructure can understand the mature V2 interpretation without reading every evidence artifact.

---

## Phase 8.5 - Character reconstruction and simulation models

### Objective

Transform the audited literary corpus into reusable character-inference specifications without creating a second full reread or a parallel authority hierarchy.

### Evidence basis

For psychology, longitudinal state, relationship behavior, and Japanese register, begin with the Phase-4 ledgers, Phase-5 character/form specialists, Phase-6 audit, Document 13, Document 14, checkpoints, and sequential readings. Reopen Japanese primary scenes only when the reconstruction matrix exposes a material evidentiary gap or when a diagnostic exemplar requires exact verification.

For **Everyday Life, Preferences, and Material Habits**, use the opposite evidence direction: mine the Japanese novels and admitted supplements directly into `OREGAIRU_V2_EVERYDAY_LIFE_PREFERENCES_AND_MATERIAL_HABITS_LEDGER.md`, then compile the reconstruction-model section from that ledger. Earlier derived artifacts may guide discovery but do not substitute for the primary-source observation.

### Initial output order

1. `OREGAIRU_V2_CHAR_HACHIMAN_RECONSTRUCTION_MODEL.md`
2. `OREGAIRU_V2_CHAR_YUKINO_RECONSTRUCTION_MODEL.md`
3. `OREGAIRU_V2_CHAR_YUI_RECONSTRUCTION_MODEL.md`
4. `OREGAIRU_V2_CHAR_IROHA_RECONSTRUCTION_MODEL.md`
5. `OREGAIRU_V2_CHAR_KOMACHI_RECONSTRUCTION_MODEL.md`
6. `OREGAIRU_V2_CHAR_HARUNO_RECONSTRUCTION_MODEL.md`
7. `OREGAIRU_V2_CHAR_HIRATSUKA_RECONSTRUCTION_MODEL.md`
8. `OREGAIRU_V2_CHAR_HAYAMA_RECONSTRUCTION_MODEL.md`

The order reflects evidence density and simulation utility, not character importance.

### Working state

Models are `active_provisional` while being compiled and source-verified. They become `canonical` only after their individual negative-constraint, relationship-register, confidence, and provenance checks pass.

### Phase-level QA

Before closure:

- verify every model's source-routing table;
- verify exact Japanese exemplars against primary evidence where used;
- confirm early/middle/late state separation;
- run cross-character novel-scenario discrimination tests;
- inspect for iconic-marker overuse and genericized speech;
- confirm that reconstruction heuristics do not override Phase-6/Document-13 claim dispositions;
- verify that each model's **Everyday Life, Preferences, and Material Habits** section routes to a completed character slice in the shared primary-source-first ledger;
- inspect mundane-life claims for competence/preference, participation/selection, and baseline/state-dependent conflation;
- document any model whose evidence remains insufficient rather than padding it with inference.

### Exit criterion

Phase 8.5 closes when the eight architecture-defined models are canonical **or** a model has been explicitly downgraded/deferred with an evidence-insufficiency finding; every canonical model has a completed everyday-life/preferences slice in the shared ledger; targeted source escalations are recorded; cross-model consistency QA passes; and the release README can route simulation/reconstruction tasks deterministically.

Phase 9 may not begin while an architecture-defined Phase-8.5 model remains silently incomplete.

---

## Phase 9 — Archival release and immutable packaging

### Objective

Turn the working corpus into a durable release.

### Actions

- write `00_README_AND_CORPUS_MAP.md`;
- update corpus manifest;
- validate internal links;
- validate YAML/front matter;
- check filename consistency;
- check source locators;
- run duplicate-prose audit;
- separate working notes from release artifacts;
- compute artifact checksums;
- verify source checksums;
- confirm no copyrighted primary-source payloads are redistributed;
- package final archive;
- freeze as v1.0 of the V2 project.

### Recommended release name

`Oregairu_Definitive_V2_Multi_Document_Synthesis_v1.0.zip`

### Future corrections

Corrections should become:

- v1.1;
- v1.2;
- or a later major release,

rather than silently mutating the frozen package.

---

# 6. Recommended directory structure

```text
Oregairu_V2/
├── 00_GOVERNING/
│   ├── OREGAIRU_V2_ANALYTICAL_METHOD.md
│   ├── OREGAIRU_V2_MULTI_DOCUMENT_SYNTHESIS_ARCHITECTURE.md
│   └── OREGAIRU_V2_PROJECT_DECISIONS.md
├── 01_SOURCE_CONTROL/
│   ├── OREGAIRU_V2_SOURCE_INVENTORY.md
│   ├── SOURCE_CHECKSUMS.sha256
│   └── OREGAIRU_V2_CORPUS_MANIFEST.md
├── 02_V1_AUDIT/
│   └── OREGAIRU_V2_V1_CLAIM_AUDIT.md
├── 03_VOLUME_DEEP_READINGS/
│   ├── OREGAIRU_V2_V01_DEEP_READING.md
│   ├── ...
│   └── OREGAIRU_V2_V14_5_DEEP_READING.md
├── 04_CHECKPOINTS/
│   ├── CHECKPOINT_A.md
│   ├── CHECKPOINT_B.md
│   ├── CHECKPOINT_C.md
│   ├── CHECKPOINT_D.md
│   ├── CHECKPOINT_E.md
│   └── CHECKPOINT_FINAL.md
├── 05_LEDGERS/
│   ├── LEDGER_HACHIMAN_EPISTEMIC_AND_NARRATORIAL.md
│   ├── LEDGER_CHARACTER_STATE.md
│   ├── LEDGER_RELATIONSHIP_STATE.md
│   ├── LEDGER_REQUEST_INTERVENTION_ETHICS.md
│   ├── LEDGER_AUTHENTICITY_HONMONO.md
│   ├── LEDGER_DEPENDENCY_AUTONOMY.md
│   ├── LEDGER_SOCIAL_ROLE_AND_PERFORMANCE.md
│   ├── LEDGER_JAPANESE_VOICE.md
│   ├── LEDGER_PRIMARY_SOURCE_LOCATORS.md
│   └── LEDGER_V1_TO_V2_REVISION.md
├── 06_SYNTHESIS/
│   ├── 00_README_AND_CORPUS_MAP.md
│   ├── 01_SERIES_ARCHITECTURE_AND_VOLUME_PROGRESSION.md
│   ├── 02_HIKIGAYA_HACHIMAN_NARRATION_SELF_DECEPTION_AND_GROWTH.md
│   ├── 03_YUKINOSHITA_YUKINO_SELFHOOD_COMPETENCE_FAMILY_AND_DESIRE.md
│   ├── 04_YUIGAHAMA_YUI_ATMOSPHERE_ACCOMMODATION_DESIRE_AND_LOSS.md
│   ├── 05_THE_SERVICE_CLUB_TRIAD_RELATIONSHIP_AND_ROMANTIC_CHOICE.md
│   ├── 06_THE_GENUINE_AUTHENTICITY_PERFORMANCE_AND_MIXED_MOTIVES.md
│   ├── 07_HELPING_SELF_SACRIFICE_DEPENDENCY_AND_AUTONOMY.md
│   ├── 08_SOCIAL_SYSTEMS_REPUTATION_GROUPS_AND_SCHOOL_POLITICS.md
│   ├── 09_HARUNO_HAYAMA_HIRATSUKA_KOMACHI_AND_COUNTER_GAZES.md
│   ├── 10_FAMILY_ADULTHOOD_FUTURITY_AND_THE_PROBLEM_OF_CHOICE.md
│   ├── 11_JAPANESE_VOICE_NARRATIVE_STYLE_COMEDY_AND_INTERTEXTUALITY.md
│   ├── 12_SUPPLEMENTARY_VOLUMES_DRAMA_CDS_AND_ORDINARY_LIFE.md
│   ├── 13_EVIDENCE_LOCATOR_AND_FIRST_PASS_REVISION_LEDGER.md
│   ├── 14_OREGAIRU_FULL_SERIES_SYNTHESIS.md
│   └── CHARACTER_RECONSTRUCTION_MODELS/
│       ├── OREGAIRU_V2_CHAR_HACHIMAN_RECONSTRUCTION_MODEL.md
│       ├── OREGAIRU_V2_CHAR_YUKINO_RECONSTRUCTION_MODEL.md
│       ├── OREGAIRU_V2_CHAR_YUI_RECONSTRUCTION_MODEL.md
│       ├── OREGAIRU_V2_CHAR_IROHA_RECONSTRUCTION_MODEL.md
│       ├── OREGAIRU_V2_CHAR_KOMACHI_RECONSTRUCTION_MODEL.md
│       ├── OREGAIRU_V2_CHAR_HARUNO_RECONSTRUCTION_MODEL.md
│       ├── OREGAIRU_V2_CHAR_HIRATSUKA_RECONSTRUCTION_MODEL.md
│       └── OREGAIRU_V2_CHAR_HAYAMA_RECONSTRUCTION_MODEL.md
└── 07_DELIVERY/
    ├── CORPUS_MANIFEST.md
    ├── ARTIFACT_CHECKSUMS.sha256
    └── DELIVERY_AUDIT.md
```

---

# 7. Dependency rules

The architecture should enforce these dependencies.

## Rule 1

No final specialist synthesis before the relevant volume readings exist.

## Rule 2

No full-series synthesis before the adversarial Japanese audit.

## Rule 3

No release README/corpus map until the specialist corpus, full-series synthesis, and architecture-defined reconstruction-model suite are structurally stable.

## Rule 4

No V1 correction should be recorded without identifying the new evidence or methodological reason.

## Rule 5

No theme should enter the mature synthesis merely because it was prominent in V1.

## Rule 6

No later continuation should alter the mainline V2 synthesis unless it is explicitly incorporated as a separately labeled scope expansion.

## Rule 7

No reconstruction model may override primary-source fact, Document-13 audited wording, or a Phase-6 disposition. Simulation heuristics remain subordinate derived artifacts.

---

# 8. Word-count philosophy

The project should not target a predetermined total word count.

Expansion is justified where Oregairu is structurally dense:

- Hachiman narration;
- Service Club triad;
- Yukino/Yui individual subjectivity;
- authenticity;
- helping/self-sacrifice;
- Japanese voice;
- social systems.

Compression is preferable where the evidence is repetitive.

A document should become longer because it has more distinctions to preserve, not because other project corpora happened to reach a certain size.

---

# 9. Definition of "done"

The V2 project is complete when:

1. all in-scope Japanese sources are inventoried;
2. all in-scope volumes have canonical deep readings;
3. prospective and retrospective readings are preserved separately;
4. longitudinal ledgers are reconciled;
5. V1 claims have explicit revision status;
6. Documents 01–13 are complete;
7. the strongest claims survive adversarial Japanese-source audit;
8. the continuous full-series synthesis is written;
9. every major synthesis claim is traceable to primary-source evidence;
10. the architecture-defined Phase-8.5 reconstruction models are complete or explicitly deferred for documented evidence insufficiency;
11. the reconstruction suite passes relationship-register, negative-constraint, source-routing, and cross-model simulation QA;
12. the final corpus passes archival QA and is frozen as a versioned release.

The final corpus should support both:

- **human reading**, through Documents 00–14;
- **future analytical retrieval**, through volume artifacts, ledgers, locators, and provenance;
- **future character reconstruction and novel-scenario simulation**, through the Phase-8.5 models while retaining deterministic escalation to Japanese source.

---

# 10. Final architectural principle

The project should move in one direction during analysis:

> **source → volume reading → ledger → specialist synthesis → full-series argument**

And it should remain navigable in the opposite direction during verification:

> **full-series argument → specialist claim → volume artifact → locator → Japanese source**

For simulation, the corpus also supports a derived operational route:

> **audited character state + voice evidence -> reconstruction model -> scenario inference**

For ordinary-life texture, the parallel route is:

> **Japanese source -> everyday-life/preferences ledger -> reconstruction model -> mundane scenario inference**

with verification in the opposite direction:

> **scenario inference -> reconstruction rule -> derived/everyday ledger evidence -> locator -> Japanese source**

That bidirectional traceability, plus explicit separation between literary authority and simulation heuristics, is the main structural advantage of V2 over the earlier Oregairu deep dive.
