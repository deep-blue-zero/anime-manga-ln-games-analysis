---
title: "『86―エイティシックス―』 Multi-Document Synthesis Architecture V2"
subtitle: "Document map, primary-home rules, production phases, evidence routing, and archival delivery standard"
version: "2.2"
date: "2026-08-13"
last_amended: "2026-08-20"
status: "Canonical V2 architecture through V14 + Alter.1; CMR-0 through CMR-10 complete; release 86-V2-V01-V14-1.0 frozen"
primary_corpus: "All supplied and verified original-Japanese 86 light novels and canonical prose supplements"
current_entrypoint: "00_README_AND_CORPUS_MAP.md"
release_id: "86-V2-V01-V14-1.0"
release_state: "frozen_boundary_release"
---

# 『86―エイティシックス―』
## Multi-Document Synthesis Architecture V2
### Document map, primary-home rules, production phases, evidence routing, and archival delivery standard

## 0. Purpose

This file defines **where the analysis goes**.

Its paired analytical method defines **how the evidence is read**:

> `86_FULL_SERIES_ANALYTICAL_METHOD_V2.md`

The multi-document model is necessary because *86* operates at several scales that distort one another when compressed into one large response:

- Shin and Lena each sustain full independent character studies;
- Spearhead functions as both intimate found family and military formation;
- the Republic requires legal, administrative, racial, political, and memorial analysis;
- the Federacy complicates rather than simply reverses the Republic;
- battles require tactical and operational reading;
- war aims and state behavior require strategic and political reading;
- the Legion is simultaneously literal military system, memory technology, and philosophical challenge to personhood;
- romance and home are not separable from survival and future imagination;
- childhood, bodily injury, disability, military usefulness, and postwar identity require their own longitudinal evidence;
- Japanese voice and forms of address carry relational information that disappears in thematic summary;
- and the legacy Volume 1–12 synthesis must be audited rather than merely expanded.

The governing architectural principle is:

> **Separate documents by governing question, not simply by topic pile.**

A second principle is:

> **Every major subject receives one primary analytical home. Other documents may summarize it briefly and cross-reference, but should not reproduce the same deep dive.**

A third principle is:

> **The final human-readable synthesis layer must remain connected to the chronological evidence layer.**

---

# I. Corpus layers

The frozen V01–V14 boundary release contains six core layers plus one supplemental reference/reconstruction layer. The supplemental layer extends the mature corpus without renumbering or relocating the established Documents 01–18.

## Layer A — Governing frameworks

1. `86_FULL_SERIES_ANALYTICAL_METHOD_V2.md`
2. `86_MULTI_DOCUMENT_SYNTHESIS_ARCHITECTURE_V2.md`

These remain stable unless the method itself changes.

---

## Layer B — Source and chronological evidence layer

### Required administrative source file

`86_SOURCE_INVENTORY.md`

For every supplied source:

- exact filename;
- volume / supplement identity;
- publication position;
- format;
- checksum where available;
- internal chapter/spine map;
- illustration inventory;
- afterword / paratext status;
- known extraction issues.

### Canonical volume artifacts

`86_V01_DEEP_READING.md`  
`86_V02_DEEP_READING.md`  
...  
`86_VNN_DEEP_READING.md`

Every supplied numbered volume receives one.

If canonical side stories or supplements are added, use stable IDs such as:

`86_SS01_DEEP_READING.md`

The evidence layer should be complete enough that later thematic writing does not require reconstruction from chat memory.

---

## Layer C — Longitudinal ledger layer

Recommended files:

1. `L01_CHARACTER_DEVELOPMENT_LEDGER.md`
2. `L02_RELATIONSHIP_STATE_LEDGER.md`
3. `L03_INSTITUTIONS_CITIZENSHIP_AND_POLITICAL_CHANGE_LEDGER.md`
4. `L04_MILITARY_DOCTRINE_OPERATIONS_AND_IRREPLACEABILITY_LEDGER.md`
5. `L05_RACE_PERSONHOOD_AND_DEHUMANIZATION_LEDGER.md`
6. `L06_BODY_INJURY_DISABILITY_AND_MEDICAL_LEDGER.md`
7. `L07_DEATH_MEMORY_GRIEF_AND_INHERITANCE_LEDGER.md`
8. `L08_CHILDHOOD_ORDINARY_LIFE_AND_FUTURE_LEDGER.md`
9. `L09_JAPANESE_VOICE_ADDRESS_AND_TERMINOLOGY_LEDGER.md`
10. `L10_MOTIF_OBJECT_AND_SYMBOL_LEDGER.md`
11. `L11_LEGACY_V1_TO_V2_REVISION_LEDGER.md`

These are analytical infrastructure, not reader-facing essays.

---

## Layer D — Human-readable specialist synthesis

This is the core multi-document corpus.

Recommended numbered documents:

- `00_README_AND_CORPUS_MAP.md`
- `01_SERIES_ARCHITECTURE_VOLUME_PROGRESSION_AND_MASTER_THESIS.md`
- `02_SHINEI_NOUZEN_DEATH_MEMORY_VIOLENCE_AND_FUTURE.md`
- `03_VLADILENA_MILIZE_COMMAND_RESPONSIBILITY_AND_POLITICAL_CONSCIENCE.md`
- `04_SPEARHEAD_RELATIONSHIPS_BELONGING_AND_THE_RIGHT_TO_CHANGE.md`
- `05_SAN_MAGNOLIA_RACISM_GENOCIDE_COMPLICITY_AND_MEMORY.md`
- `06_GIAD_AND_COMPARATIVE_INSTITUTIONS_CITIZENSHIP_FREEDOM_AND_PATERNALISM.md`
- `07_WAR_STRATEGY_LOGISTICS_TECHNOLOGY_AND_HEROISM.md`
- `08_PERSONHOOD_BODY_DISABILITY_AI_AND_THE_DEAD.md`
- `09_CHILDHOOD_PRIDE_TRAUMA_GRIEF_RECOVERY_AND_ORDINARY_LIFE.md`
- `10_SHIN_LENA_LOVE_DEPENDENCE_HOME_AND_THE_RIGHT_TO_RETURN.md`
- `11_LEGION_MEMORY_IDENTITY_AND_POSTHUMAN_CONTINUITY.md`
- `12_JAPANESE_VOICE_NARRATION_TERMINOLOGY_AND_TRANSLATION_SENSITIVE_FINDINGS.md`
- `13_SYMBOLS_MOTIFS_LANDSCAPES_OBJECTS_AND_LIGHT_NOVEL_FORM.md`
- `14_COMPARATIVE_REFERENCE_MATRICES_CONTRADICTIONS_AND_OPEN_QUESTIONS.md`
- `15_VOLUME_BY_VOLUME_EVIDENCE_LEDGER.md`
- `16_JAPANESE_PASSAGE_AND_TERMINOLOGY_INDEX.md`
- `17_LEGACY_SYNTHESIS_REVISION_REPORT.md`
- `18_FULL_SERIES_CONTINUOUS_SYNTHESIS.md`

Documents 15–17 are audit/reference documents rather than ordinary essays.

Document 18 is written last.

---

## Layer E — Machine retrieval layer

Recommended:

- `86_CORPUS_INDEX.json`
- `86_CLAIM_INDEX.json`

These are optional but valuable.

The corpus index can store:

- document ID;
- title;
- scope;
- major characters;
- major themes;
- source volumes;
- word count;
- checksum.

The claim index can store:

- claim ID;
- concise formulation;
- primary home;
- supporting volume artifacts;
- evidence locators;
- confidence;
- contradiction status.

This allows later comparative work to retrieve conclusions without treating summary prose as primary evidence.

---

## Layer F — Delivery and integrity layer

Required for archival release:

- `CORPUS_MANIFEST.md`
- `FILE_CHECKSUMS.sha256`
- `DELIVERY_AUDIT.md`
- optional ZIP checksum sidecar
- final ZIP package

The copyrighted source novels are not included in the analytical delivery package.

---

## Supplemental Reference Layer — Character Modeling Reference

**Status:** canonical and release-integrated after CMR-10 on 2026-08-20.

**Canonical Drive home:** `04 Evidence and Indexes/Character Modeling Reference/` — Drive folder ID `1qASOnAB4uSiB-nTsbDiCyAjHU7bs0xno`

This is an **additive reader/model-facing reconstruction layer**, not a new thematic synthesis phase and not a replacement for Documents 01–18. Its governing question is:

> **What information is necessary to recognize, predict, compare, or reconstruct a character as a person—including Japanese voice, behavior, emotional-state changes, ordinary-life texture, relationship-conditioned register, and likely response patterns—without inventing characterization the sources do not support?**

Its primary purpose is reconstructability and descriptive fidelity. It supports:

- character recognition and comparison;
- Japanese dialogue/register analysis;
- ordinary-life and emotional-state retrieval;
- directed relationship/register modeling;
- behavioral prediction with explicit uncertainty;
- hypothetical-interaction work whose synthetic output is kept separate from evidence.

### Authority hierarchy

The Character Modeling Reference layer never becomes an independent source of canon. Use this precedence:

1. original Japanese primary source;
2. Phase-5 locked locator/source authority and Phase-8 source verification;
3. canonical V2 deep readings and longitudinal ledgers;
4. canonical specialist Documents 01–14 and source-sensitive Documents 16–17;
5. canonical continuous synthesis, Document 18;
6. Character Modeling Reference layer;
7. V1 legacy analysis as discovery aid only;
8. synthetic/generated examples, which are never evidence.

When precision matters, the narrower primary or canonical analytical home prevails over a profile summary.

### Required artifacts

The layer is governed by:

- `86_CHARACTER_MODELING_REFERENCE_METHOD.md`

Its initial profile roster is:

- `86_SHINEI_NOUZEN_CHARACTER_REFERENCE_PROFILE.md`
- `86_VLADILENA_MILIZE_CHARACTER_REFERENCE_PROFILE.md`
- `86_RAIDEN_SHUGA_CHARACTER_REFERENCE_PROFILE.md`
- `86_THEOTO_RIKKA_CHARACTER_REFERENCE_PROFILE.md`
- `86_KURENA_KUKUMILA_CHARACTER_REFERENCE_PROFILE.md`
- `86_ANJU_EMMA_CHARACTER_REFERENCE_PROFILE.md`
- `86_FREDERICA_ROSENFORT_CHARACTER_REFERENCE_PROFILE.md`
- `86_SHIDEN_IIDA_CHARACTER_REFERENCE_PROFILE.md`
- `86_ERNST_ZIMMERMANN_CHARACTER_REFERENCE_PROFILE.md`
- `86_GRETHE_WENZEL_CHARACTER_REFERENCE_PROFILE.md`
- `86_ANNETTE_PENROSE_CHARACTER_REFERENCE_PROFILE.md`
- `86_VIKA_CHARACTER_REFERENCE_PROFILE.md`
- `86_LERCHE_CHARACTER_REFERENCE_PROFILE.md`
- `86_RITO_CHARACTER_REFERENCE_PROFILE.md`
- `86_MARCEL_CHARACTER_REFERENCE_PROFILE.md`
- `86_FIDO_CHARACTER_REFERENCE_PROFILE.md`

Retrieval/reference infrastructure:

- `86_CHARACTER_RELATIONSHIP_REGISTER_MATRIX.md`
- `86_CHARACTER_DIALOGUE_AND_BEHAVIOR_LOCATOR_INDEX.tsv`
- `86_CHARACTER_MODELING_CROSSWALK.md`

CMR-0 also records the identity of the chat-local working EPUB set in `86_CHARACTER_MODELING_ATTACHED_SOURCE_VERIFICATION.tsv`. This support audit does **not** supersede the Phase-5 source lock or the canonical Phase-8 source-verification audit.

### Locator and source rules

`86_PHASE5_LOCKED_LOCATOR_INDEX.tsv` remains the locator-coordinate authority. If a diagnostically useful character passage already has a locked locator, the Character Modeling Reference index reuses it. If a useful passage lacks one, the layer must preserve the precise source route and mark a controlled `LOCATOR_GAP`; it must not invent a canonical locator or silently reopen Phase 5.

The source boundary remains original-Japanese V01–V14 plus Alter.1 in its audited supplemental role. Alter.1 should be used actively for ordinary-life characterization where useful, but never promoted above mainline evidence. Alter.2 remains excluded from mainline characterization unless explicitly invoked for counterfactual/AU comparison.

### Architectural anti-duplication rule

Profiles reorganize evidence for reconstruction. They do not become parallel thematic monographs. Major claims must route back to Documents 02–12, L01/L02/L09 and other relevant ledgers, deep readings, the diagnostic locator index, and locked Phase-5 coordinates where available. The crosswalk exists specifically to preserve this routing.

---

# II. Primary-home map

The most important anti-duplication rule is that every large question has one primary home.

## `01_SERIES_ARCHITECTURE_VOLUME_PROGRESSION_AND_MASTER_THESIS.md`

### Governing question

> **What does the complete supplied sequence become when read as one developing argument, and how does each volume modify the problem inherited from the previous one?**

### Primary responsibilities

- narrative architecture;
- volume-to-volume progression;
- arc segmentation;
- scale shifts;
- master thesis and competing thesis;
- how later volumes revise early formulations;
- series-wide endpoint at the supplied corpus boundary.

### Do not duplicate here

- full Shin psychology;
- full Lena psychology;
- detailed battle doctrine;
- full race/genocide analysis;
- full romance analysis.

Those receive cross-references.

---

## `02_SHINEI_NOUZEN_DEATH_MEMORY_VIOLENCE_AND_FUTURE.md`

### Governing question

> **How does Shin move from being organized around death, usefulness, and inherited responsibility toward a self capable of desire and future without repudiating the dead?**

### Primary responsibilities

- Shin's childhood and family;
- Rei;
- Undertaker identity;
- hearing the Legion;
- execution of comrades;
- violence and ethical burden;
- leadership;
- names and memory;
- dependence;
- loneliness;
- future imagination;
- body and injury insofar as specific to Shin;
- relation to Spearhead;
- relation to Lena as part of Shin's development.

### Secondary homes

- romance-specific bilateral analysis → Document 10;
- tactical use of Shin's ability → Document 07;
- Legion ontology → Document 11.

---

## `03_VLADILENA_MILIZE_COMMAND_RESPONSIBILITY_AND_POLITICAL_CONSCIENCE.md`

### Governing question

> **How does Lena move from morally correct witness inside an evil institution toward command, political agency, coercive responsibility, and a more bounded understanding of what care can legitimately demand?**

### Primary responsibilities

- Alba privilege;
- childhood and father;
- Handler role;
- political education;
- command;
- institutional dissent;
- guilt;
- Republic collapse;
- Bloody Reina;
- responsibility for subordinates;
- use of force;
- care versus paternalism;
- desire and future;
- post-Republic political consciousness.

### Secondary homes

- Republic system → Document 05;
- military command mechanics → Document 07;
- Shin relationship → Document 10.

---

## `04_SPEARHEAD_RELATIONSHIPS_BELONGING_AND_THE_RIGHT_TO_CHANGE.md`

### Governing question

> **What kind of social world do the Eighty-Six build among themselves, and can belonging survive when members change, stop fighting, fall in love, become disabled, or want different futures?**

### Primary responsibilities

- Raiden;
- Anju;
- Theo;
- Kurena;
- Frederica where she functions as household/family member;
- group culture;
- jokes and daily life;
- mutual care;
- conflict;
- pride;
- internal difference;
- found family;
- living with the dead;
- belonging after function;
- relationship to later Eighty-Six groups.

### Important rule

Do not let “Spearhead” become a homogeneous trauma subject.

Each member must retain independent motive and trajectory.

---

## `05_SAN_MAGNOLIA_RACISM_GENOCIDE_COMPLICITY_AND_MEMORY.md`

### Governing question

> **How does the Republic turn racial ideology into administrative reality, and what remains after the state that denied the Eighty-Six's humanity collapses?**

### Primary responsibilities

- racial classification;
- law;
- camps / Sector system;
- military euphemism;
- unmanned-war fiction;
- propaganda;
- bureaucracy;
- ordinary civilian complicity;
- dissent;
- resistance;
- economic and political incentives;
- historical memory;
- collapse;
- survivor return;
- revenge / nonrevenge / nonforgiveness;
- post-collapse responsibility.

### Key distinction

Genocide is not only hatred.

Analyze the machinery that makes destruction administratively ordinary.

---

## `06_GIAD_AND_COMPARATIVE_INSTITUTIONS_CITIZENSHIP_FREEDOM_AND_PATERNALISM.md`

### Governing question

> **What changes when a state recognizes the Eighty-Six as citizens, and why is legal recognition still insufficient to produce a livable freedom?**

### Primary responsibilities

- Giad political order;
- Ernst and civilian leadership;
- military institutions;
- education and welfare;
- child protection;
- treatment of the Eighty-Six;
- treatment of Frederica;
- imperial inheritance;
- rights;
- benevolent paternalism;
- political legitimacy;
- exceptional-unit dependence;
- comparison with other states/polities encountered later.

### Comparative axis

Distinguish:

- legal recognition;
- material provision;
- social belonging;
- political agency;
- usable freedom.

---

## `07_WAR_STRATEGY_LOGISTICS_TECHNOLOGY_AND_HEROISM.md`

### Governing question

> **How does *86* imagine war as an organizational system, and what does it reveal when survival repeatedly depends on exceptional people or morally intolerable necessities?**

### Primary responsibilities

- tactical analysis;
- operational analysis;
- strategy;
- war aims;
- logistics;
- reconnaissance;
- command;
- industrial capacity;
- force preservation;
- casualty systems;
- Juggernaut / Reginleif as military platforms;
- Para-RAID as command technology;
- Legion force structure;
- heroic dependency;
- irreplaceability;
- distributed competence;
- military professionalism;
- war termination.

### Normative rule

Do not confuse:

- courage with good strategy;
- good strategy with moral legitimacy;
- necessity with innocence;
- victory with peace.

---

## `08_PERSONHOOD_BODY_DISABILITY_AI_AND_THE_DEAD.md`

### Governing question

> **What counts as a person when bodies, memories, military functions, machines, copied minds, scars, and disabilities all challenge simple biological or utilitarian definitions?**

### Primary responsibilities

- racialized body;
- military body;
- scars;
- bodily autonomy;
- injury;
- disability;
- prosthetics;
- medical treatment;
- loss of combat function;
- Sirins;
- Fido;
- artificial minds;
- copied/preserved cognition;
- body as political territory;
- continuity of self;
- instrumentalization.

### Caution

This is not only a “technology ethics” document.

Human bodies and artificial continuities belong in the same analysis because the series repeatedly asks who is allowed to remain more than a function.

---

## `09_CHILDHOOD_PRIDE_TRAUMA_GRIEF_RECOVERY_AND_ORDINARY_LIFE.md`

### Governing question

> **What does recovery mean for young people who became competent at war before they had ordinary opportunities to develop outside it?**

### Primary responsibilities

- child soldierhood;
- emergency competence;
- interrupted development;
- pride as survival strategy;
- pride as constraint;
- survivor guilt;
- grief;
- ordinary adolescence;
- school;
- play;
- hobbies;
- art;
- fashion;
- rest;
- food;
- festivals;
- embarrassment;
- sexuality and romance insofar as developmental;
- recovery without pretending the past can be undone.

### Diagnostic caution

Use clinical language only where the text or reliable external framework justifies it.

Prefer precise descriptions of behavior and experience.

---

## `10_SHIN_LENA_LOVE_DEPENDENCE_HOME_AND_THE_RIGHT_TO_RETURN.md`

### Governing question

> **How does the central relationship transform from disembodied military communication into reciprocal dependence, embodied intimacy, chosen home, and a future neither person is allowed to own alone?**

### Primary responsibilities

- voice before body;
- names;
- memory;
- pursuit;
- reunion;
- conflict after reunion;
- mutual idealization;
- correction of idealization;
- dependence;
- desire;
- jealousy where present;
- confession;
- touch / physical presence;
- communication failures;
- future promises;
- home;
- return;
- responsibility boundaries.

### Key ethical distinction

Healthy interdependence is not total self-sufficiency.

Nor is it savior dependence.

The document should test exactly where the relationship moves between those poles.

---

## `11_LEGION_MEMORY_IDENTITY_AND_POSTHUMAN_CONTINUITY.md`

### Governing question

> **What does the Legion make literal about memory, death, copied consciousness, final desire, and the danger of a self that can no longer revise its command?**

### Primary responsibilities

- Legion origin and mechanics as supplied;
- Black Sheep;
- Shepherds;
- copied minds;
- identity continuity;
- final mental states;
- human command converted into machinery;
- dead/living boundary;
- immortality versus imprisonment;
- technological persistence;
- metaphysical implications.

### Rule

Maintain two columns of analysis:

1. **literal mechanics**
2. **philosophical implications**

Never substitute one for the other.

---

## `12_JAPANESE_VOICE_NARRATION_TERMINOLOGY_AND_TRANSLATION_SENSITIVE_FINDINGS.md`

### Governing question

> **What becomes visible only when the novels are read in Japanese?**

### Primary responsibilities

- narrator / focalization;
- free indirect style;
- Shin's voice;
- Lena's voice;
- Spearhead voices;
- Frederica;
- institutional registers;
- military terminology;
- racial terminology;
- forms of address;
- honorifics;
- pronouns;
- intimacy shifts;
- official euphemisms;
- recurring conceptual vocabulary;
- translation-sensitive findings.

### Output style

Prefer:

- short Japanese anchors;
- compact glosses;
- locator tables;
- voice profiles.

Avoid turning this into a second general thematic synthesis.

---

## `13_SYMBOLS_MOTIFS_LANDSCAPES_OBJECTS_AND_LIGHT_NOVEL_FORM.md`

### Governing question

> **How does the series use recurring objects, landscapes, visual paratext, and structural juxtapositions to connect war-scale abstraction to embodied life?**

### Primary responsibilities

Potential systems to test:

- names;
- tags / records;
- graves;
- flowers;
- voices;
- headless imagery;
- machines;
- borders;
- roads;
- sea;
- sky;
- fields;
- food;
- clothing;
- drawings;
- medals;
- hands;
- ruins;
- home;
- thresholds.

Also:

- cover / insert illustration patterns;
- maps;
- afterword placement;
- volume title structure;
- chapter rhythm;
- action / quiet-scene alternation.

Do not include a motif merely because it appears twice.

Require recurrence plus changing or structurally meaningful function.

---

## `14_COMPARATIVE_REFERENCE_MATRICES_CONTRADICTIONS_AND_OPEN_QUESTIONS.md`

### Governing question

> **What are the strongest reusable conclusions, strongest counterarguments, unresolved tensions, and comparative formulations produced by the V2 corpus?**

### Primary responsibilities

- character matrices;
- institution matrices;
- ethical matrices;
- military matrices;
- personhood matrices;
- relationship matrices;
- legacy-vs-V2 change matrix;
- contradictions;
- unresolved questions;
- comparative hooks for other project works.

### Do not place here

New major interpretations that have not already been argued in Documents 01–13.

This is a compression and retrieval layer.

---

## `15_VOLUME_BY_VOLUME_EVIDENCE_LEDGER.md`

### Function

This is the common chronological spine.

For every volume record:

1. volume ID and title;
2. chapter list;
3. volume thesis;
4. decisive events;
5. character changes;
6. relationship changes;
7. institution changes;
8. military developments;
9. personhood / technology developments;
10. ethical cases;
11. Japanese terms;
12. motifs;
13. later revisions;
14. unresolved questions;
15. which synthesis documents use the evidence.

Recommended table:

| Locator | Event / wording | Evidence class | Immediate meaning | Later revision | Primary home |
|---|---|---|---|---|---|

This document is required.

---

## `16_JAPANESE_PASSAGE_AND_TERMINOLOGY_INDEX.md`

### Function

Create a compact retrieval layer for exact Japanese language.

Sections:

- names / ranks / titles;
- forms of address;
- racial and political terminology;
- military terms;
- personhood / machine vocabulary;
- death / memory vocabulary;
- freedom / choice vocabulary;
- home / return vocabulary;
- high-value verified passages.

This document should be table-heavy and quotation-light.

---

## `17_LEGACY_SYNTHESIS_REVISION_REPORT.md`

### Governing question

> **What did the first synthesis get right, underweight, overstate, miss, or misclassify?**

### Required structure

For each major legacy thesis:

- legacy formulation;
- V2 evidence base;
- confirming evidence;
- counterevidence;
- revised formulation;
- disposition.

Suggested dispositions:

- survives substantially intact;
- survives but narrowed;
- strengthened;
- materially complicated;
- partially overturned;
- fully overturned;
- unresolved.

This is one of the most important V2 deliverables because it demonstrates analytical gain.

---

## `18_FULL_SERIES_CONTINUOUS_SYNTHESIS.md`

### Function

Write a final continuous literary argument after all specialist documents are stable.

It should answer:

> **What is *86* ultimately doing across the complete supplied corpus?**

It should not reproduce the specialist documents section by section.

Instead it should synthesize their results into a coherent argument about:

- personhood;
- war;
- memory;
- institutions;
- freedom;
- love;
- future;
- and the right of living people to remain revisable.

### Recommended scale

Approximately 15,000–30,000 words depending on final corpus length.

This document is a reader-facing capstone, not the evidentiary substrate.

---

# III. Human-readable core versus archival substrate

The corpus should make a distinction similar to a scholarly edition.

## Reader-facing core

Primarily:

- `00`
- `01` through `14`
- `18`

These should be readable without consulting the ledgers constantly.

## Evidence / audit substrate

- per-volume deep readings;
- L01–L11;
- `15`;
- `16`;
- `17`;
- source inventory;
- claim index.

These preserve traceability and revision history.

## Model-facing reconstruction infrastructure

The Character Modeling Reference layer sits beside the evidence/audit substrate rather than inside the numbered specialist sequence. It is optimized for reconstructing how a character sounds, behaves, varies by emotional state, and changes register by interlocutor. It must remain source-routed and subordinate to the Japanese source, Phase-5/8 controls, ledgers, and canonical specialist homes.

This division lets the project achieve both:

- readable criticism;
- and evidentiary recoverability.

---

# IV. Recommended word-budget philosophy

Do not impose uniform document lengths.

The subject should determine length.

Approximate expectations for the currently known scale of the series:

- per-volume deep reading: **6,000–12,000 words**
- major character documents: **8,000–15,000**
- ensemble/institution documents: **7,000–14,000**
- military/ethics/personhood documents: **8,000–16,000**
- language/motif documents: **5,000–10,000**
- evidence ledger: **15,000–30,000**
- final continuous synthesis: **15,000–30,000**

A mature core synthesis across Documents 01–14 may reasonably exceed 100,000 words.

That is not a target.

It is permission not to compress major questions merely to fit a single response.

The primary quality criterion is:

> **Does each paragraph add a distinct analytical function?**

---

# V. Production phases

## Phase 0 — Corpus audit and source lock

Before rereading:

1. verify every Japanese source;
2. record checksum, title, spine, chapter list;
3. inventory illustrations/maps;
4. identify supplements and paratext;
5. establish publication order;
6. create `86_SOURCE_INVENTORY.md`.

No major synthesis drafting yet.

---

## Phase 1 — Legacy V1 audit

Before Volume 1 rereading, inventory the legacy analysis.

Create a preliminary table of:

- major theses;
- character claims;
- institutional claims;
- military claims;
- ethical claims;
- Japanese-language claims;
- areas that were compressed;
- claims lacking direct locator support.

This creates questions for V2 without granting V1 authority.

---

## Phase 2 — Sequential volume reread

Read the numbered novels in publication order.

For each volume:

1. produce `86_VXX_DEEP_READING.md`;
2. update L01–L11;
3. add locators;
4. update the prospective state;
5. add retrospective revision only in its labeled section;
6. record legacy corrections.

Do not draft final specialist documents yet except short working notes.

---

## Phase 3 — Narrative checkpoint syntheses

At major arc transitions, produce provisional checkpoint summaries.

The earlier corpus suggests natural movements such as:

- opening Republic / first survival movement;
- post-rescue / Federacy reintegration;
- pride-and-wounds movement;
- later political / technological expansions.

But V2 should let the actual reread determine exact boundaries.

Each checkpoint asks:

- what has the series become so far?
- what earlier thesis changed?
- which characters moved?
- which institutions changed?
- which hypotheses remain live?

---

## Phase 4 — Thematic retrieval pass

After the sequential reread reaches the current corpus endpoint, run targeted source retrieval across all novels.

Priority searches:

- names / forms of address;
- human / person terminology;
- race / blood / color language;
- freedom / choice / command;
- pride / dignity;
- home / return;
- dead / memory / name / grave;
- hero / replaceability;
- child / adult / school;
- weapon / machine / body;
- responsibility / guilt / forgiveness;
- recurring military doctrine;
- repeated motifs.

Search hits are then reread in context.

---

## Phase 5 — Evidence and locator lock

Before the specialist synthesis:

- ensure every volume is represented in Document 15;
- ensure every major character has ordinary-scene evidence as well as climactic evidence;
- ensure every ethical conclusion has counterevidence;
- ensure military claims identify their level;
- ensure major Japanese claims have verified anchors;
- mark unresolved contradictions.

Only after this phase should the thematic documents become authoritative.

---

## Phase 6 — Draft specialist documents

Recommended drafting order:

1. `15_VOLUME_BY_VOLUME_EVIDENCE_LEDGER.md`
2. `01_SERIES_ARCHITECTURE_VOLUME_PROGRESSION_AND_MASTER_THESIS.md`
3. `02_SHINEI_NOUZEN...`
4. `03_VLADILENA_MILIZE...`
5. `04_SPEARHEAD_RELATIONSHIPS...`
6. `05_SAN_MAGNOLIA...`
7. `06_GIAD_AND_COMPARATIVE_INSTITUTIONS...`
8. `07_WAR_STRATEGY...`
9. `08_PERSONHOOD_BODY...`
10. `09_CHILDHOOD_PRIDE...`
11. `10_SHIN_LENA_LOVE...`
12. `11_LEGION_MEMORY...`
13. `12_JAPANESE_VOICE...`
14. `13_SYMBOLS_MOTIFS...`
15. `17_LEGACY_SYNTHESIS_REVISION_REPORT.md`
16. `14_COMPARATIVE_REFERENCE...`
17. `16_JAPANESE_PASSAGE_AND_TERMINOLOGY_INDEX.md`

This order moves from chronological substrate toward higher synthesis.

---

## Phase 7 — Contradiction and adversarial audit

Before the final capstone, test the corpus against its most tempting simplifications.

Required stress tests include:

### “The Republic is evil; Giad is good.”
Test institutional nuance without creating false equivalence.

### “The Eighty-Six simply need to stop fighting.”
Test agency, military necessity, pride, competence, and lack of alternatives.

### “Pride is purely pathological.”
Test its role in resisting extermination and pity.

### “Lena saves the Eighty-Six.”
Test the limits of her authority and the Eighty-Six's own agency.

### “Shin's problem is simply depression / trauma.”
Reject unsupported clinical flattening; reconstruct the specific text.

### “The romance heals both protagonists.”
Test what it changes, what it cannot change, and where dependence remains risky.

### “The Legion are only a metaphor for the dead.”
Reassert literal military and technological ontology.

### “The series is pacifist.”
Test admiration for military virtue alongside structural anti-war critique.

### “A humane institution solves dehumanization.”
Test citizenship, paternalism, material conditions, and institutional dependency.

### “Personhood equals biological humanity.”
Test Fido, Sirins, copied minds, Legion persistence, and shared history.

Every final thesis should survive these challenges or be reformulated.

---

## Phase 8 — Japanese verification pass

Recheck:

- every direct quotation;
- every translation-sensitive term;
- every claimed address shift;
- every recurring lexical motif;
- disputed narrator wording;
- political vocabulary;
- military vocabulary;
- terms used to distinguish human / machine / citizen / Eighty-Six.

Update Documents 12 and 16.

No unverified quotation should remain load-bearing.

---

## Phase 9 — Write the continuous synthesis

Draft `18_FULL_SERIES_CONTINUOUS_SYNTHESIS.md`.

The capstone should be written from Documents 01–17, not from memory.

It should avoid an encyclopedic structure.

Preferred movement:

1. the first denial of personhood;
2. the survival systems built under extermination;
3. rescue and the inadequacy of benevolence;
4. pride as dignity and enclosure;
5. bodies, machines, and the problem of function;
6. the dead and the living;
7. institutions and usable freedom;
8. love, home, and future time;
9. the unresolved question of what life after weaponhood can become.

This sequence is provisional and may change if the completed V2 evidence demands a different architecture.

---

## Supplemental production sequence — Character Modeling Reference (CMR-0 through CMR-10)

This sequence was executed **after the canonical Phase-9 continuous synthesis and before Phase 10 README finalization**. It does not renumber Documents 01–18 or replace the Phase 0–11 analytical/release architecture.

- **CMR-0 — Architecture amendment:** amend this architecture in place; create `04 Evidence and Indexes/Character Modeling Reference/`; verify the active working source set against the Phase-8 identities; update `CURRENT_STATE_AND_CORPUS_MAP.md`; do not freeze the README.
- **CMR-1 — Method:** create `86_CHARACTER_MODELING_REFERENCE_METHOD.md`, cross-checked against the governing method, L01/L02/L09, T12, Document 12, and Phase-5/8 source rules.
- **CMR-2 — Frederica pilot:** create `86_FREDERICA_ROSENFORT_CHARACTER_REFERENCE_PROFILE.md` as the stress test for marked idiolect, child/adult asymmetry, relationship-conditioned register, ordinary life, humor, political role, and source-language reconstruction. Revise the method if the pilot exposes missing fields.
- **CMR-3 — Retrieval spine:** create and seed `86_CHARACTER_DIALOGUE_AND_BEHAVIOR_LOCATOR_INDEX.tsv` and `86_CHARACTER_RELATIONSHIP_REGISTER_MATRIX.md`.
- **CMR-4 — Core Spearhead/protagonists:** Shin, Lena, Raiden, Theo, Kurena, Anju, Shiden.
- **CMR-5 — Adult/institutional and artificial-person profiles:** Ernst, Grethe, Annette, Vika, Lerche.
- **CMR-6 — Wider ensemble:** Rito, Marcel, Fido.
- **CMR-7 — Matrix completion:** audit directed `A → B` and `B → A` relationship/register routes against all profiles.
- **CMR-8 — Crosswalk:** create `86_CHARACTER_MODELING_CROSSWALK.md` routing profile sections back into the existing V2 authority structure.
- **CMR-9 — QA and canonical promotion:** run source-grounding, state-versus-trait, relationship-specificity, V1-regrounding, synthetic-example firewall, thematic-flattening, reconstruction, and retrieval audits; promote profiles only after passing.
- **CMR-10 — Final architecture/release integration: COMPLETE.** Updated the architecture, archived `CURRENT_STATE_AND_CORPUS_MAP.md`, created the final README, manifest, delivery audit, checksum inventory, machine index, release notes, package, and archival lock for `86-V2-V01-V14-1.0`.

Phase 10 was unblocked after CMR-9 canonical promotion; CMR-10 completed README, manifest, delivery, checksum, package, and archival integration.

---

## Phase 10 — README and corpus map

`00_README_AND_CORPUS_MAP.md` was written last for frozen boundary release `86-V2-V01-V14-1.0`.

It should reflect the finished corpus, not the plan.

Include:

- scope;
- spoiler boundary;
- source hierarchy;
- evidence codes;
- locator conventions;
- document map;
- recommended reading paths;
- glossary;
- summary of major V1 → V2 changes;
- master thesis;
- unresolved questions.

---

## Phase 11 — Archival package

CMR-10 generated:

- corpus manifest;
- word counts;
- byte counts;
- checksums;
- internal link audit;
- duplicate prose audit;
- unresolved-placeholder audit;
- source-payload exclusion audit;
- ZIP CRC test;
- final ZIP.

Frozen release `86-V2-V01-V14-1.0` is v1.0 of the V2 V01–V14 + Alter.1 corpus.

Future corrections or boundary expansions become v1.1 or later rather than silent mutation.

---

# VI. Cross-document citation rules

Each specialist document should use stable internal references.

Examples:

- `See 05_SAN_MAGNOLIA..., §VII`
- `Evidence: V03 deep reading, locator L-0312`
- `See L07 Death/Memory Ledger`
- `Terminology: 16_JAPANESE_PASSAGE..., entry JP-FREEDOM-004`

Avoid embedding sandbox URLs or transient chat citations inside the archival corpus.

The corpus should remain portable.

---

# VII. Claim-routing standard

Every mature load-bearing claim should be routable.

Example:

> **Claim:** the series distinguishes a person's emotional irreplaceability from a military institution's dangerous dependence on an exceptional capability.

Route:

1. `14_COMPARATIVE_REFERENCE...` — compact formulation
2. `07_WAR_STRATEGY...` — full military/institutional argument
3. `02_SHINEI_NOUZEN...` — Shin-specific psychological dimension
4. relevant `86_VXX_DEEP_READING.md`
5. `15_VOLUME_BY_VOLUME_EVIDENCE_LEDGER.md`
6. original Japanese locator

This is the standard the corpus should satisfy.

---

# VIII. Anti-duplication rules

## Rule 1 — One deep home

A topic receives one full treatment.

Other documents receive only what they need to advance their own governing question.

## Rule 2 — No repeated scene retelling

If a major scene has already been reconstructed in a volume deep reading, specialist documents should summarize only the necessary causal elements and focus on interpretation.

## Rule 3 — No identical thematic introductions

Documents should not each begin with “86 is about personhood.”

Each file should establish its specific problem.

## Rule 4 — Cross-reference instead of re-explaining

If Document 10 needs the full Republic context, point to Document 05.

## Rule 5 — The final synthesis is not a concatenation

Document 18 must create a new continuous argument rather than paste condensed versions of Documents 01–14.

---

# IX. Retrieval-oriented metadata

Every Markdown artifact should contain YAML front matter.

Recommended fields:

```yaml
title:
document_id:
version:
date:
status:
corpus_scope:
spoiler_boundary:
source_volumes:
primary_characters:
primary_domains:
evidence_status:
supersedes:
related_documents:
```

Per-volume artifacts additionally include:

```yaml
volume:
publication_position:
source_filename:
source_sha256:
chapters:
prospective_boundary:
retrospective_scope:
```

This supports Library search and future automated corpus indexing.

---

# X. Comparative reuse

The final corpus should make *86* usable in cross-series analysis without flattening it.

Document 14 should support comparisons involving:

- *Legend of the Galactic Heroes* — legitimacy, military command, institutions, history;
- *Youjo Senki* — war systems, professionalism, state survival, authorship;
- *Attack on Titan* — racialization, dehumanization, memory, inherited violence, freedom;
- *Lycoris Recoil* — institutionalized child combatants and ordinary-life counterspaces;
- *Sound! Euphonium* — institutional belonging and identity beyond a role, at a radically different scale;
- *One Punch Man* — heroism, irreplaceability, institutional recognition;
- *To Be Hero X* — public image, legitimacy, personhood under imposed roles;
- Paragon Shepard — command responsibility, proportionality, coalition duty.

Comparative formulations should be derived from the 86 corpus after the source-grounded reading, not imported as interpretive templates.

---

# XI. Expected analytical gains over the legacy synthesis

The V2 architecture should improve the earlier analysis in at least nine ways.

## 1. Better chronology
The old full-series synthesis necessarily compressed twelve books into one mature endpoint.

V2 preserves what each volume knew at the time.

## 2. Better evidence recoverability
Claims route back to Japanese locators.

## 3. Better secondary-character resolution
Raiden, Anju, Theo, Kurena, Frederica, Annette, and others no longer disappear inside Shin/Lena/thematic compression.

## 4. Better institutional analysis
Republic, Giad, military organizations, and later polities receive independent treatment.

## 5. Better military analysis
Tactical spectacle is separated from operational, strategic, and political consequences.

## 6. Better Japanese-language analysis
Voice, title, address, and conceptual vocabulary become cumulative evidence rather than occasional observations.

## 7. Better normative rigor
Each strong ethical thesis is forced through counterargument.

## 8. Better V1 correction
The new project records what actually changed rather than simply replacing the old prose.

## 9. Better long-term reuse
Future questions about a character, institution, military concept, relationship, or philosophical issue can retrieve the relevant specialist document instead of reopening one massive chat synthesis.

---

# XII. Definition of completion

The V2 analysis is not complete merely when every volume has been summarized.

It is complete when:

1. every supplied Japanese volume has a canonical deep reading;
2. the cumulative ledgers are current;
3. every specialist document has been drafted and cross-audited;
4. the Japanese-language and locator layers are verified;
5. the legacy revision report is complete;
6. the contradiction audit is complete;
7. the final continuous synthesis is written and canonically promoted after its audit gates;
8. the Character Modeling Reference layer is complete, source-grounded, crosswalked, and QA-promoted without becoming a parallel thematic corpus;
9. the README accurately maps the finished corpus, including the Character Modeling Reference retrieval route;
10. the package passes integrity and duplication audits;
11. every major final claim can be traced back to primary-source evidence.

---

# XIII. Final architectural principle

The legacy analysis was strong enough to identify the broad question:

> **What does it mean to recognize someone as human after a state has tried to turn that person into a weapon?**

The new architecture is designed to prevent that insight from becoming too clean.

The V2 corpus should be able to show, separately and then together:

- what law does;
- what war does;
- what memory does;
- what love does;
- what institutions do;
- what bodies remember;
- what machines preserve;
- what children lose;
- what pride saves;
- what pride imprisons;
- what command requires;
- what responsibility cannot accomplish;
- and what conditions allow a living person to revise the story that violence wrote for them.

The Character Modeling Reference layer extends that resolution one step further: the corpus should preserve enough ordinary, relational, emotional-state, behavioral, and Japanese-voice evidence that a character can be reconstructed as a person without being reduced to the thesis they help prove.

That is the level of resolution the multi-document model is meant to preserve.

# XIV. CMR-10 completion and frozen release state

CMR-10 completed on 2026-08-20 with verdict `CMR10_PASS_RELEASE_INTEGRATION`.

The canonical first-read entrypoint is now `00_README_AND_CORPUS_MAP.md`. `CURRENT_STATE_AND_CORPUS_MAP.md` is retained as a historical transition record and no longer determines current authority. The released corpus preserves the established Drive architecture and the authority hierarchy established by the method, Phase-5/8 controls, specialist corpus, Document 18, and CMR-9.

Release `86-V2-V01-V14-1.0` is frozen at the original-Japanese V01–V14 boundary with Alter.1 in its audited supplemental role. It is **not** labeled a completed analysis of the still-continuing novel series. Alter.2 remains excluded from mainline characterization. All 32 T14 open questions and all final-arc uncertainty controls remain active.

The final portable package excludes copyrighted source novels and redundant intermediate ZIP/sidecar copies. It contains the analytical and audit artifacts necessary to reconstruct authority, evidence, revision history, specialist conclusions, source routing, and character-modeling infrastructure. Any future correction or V15+ expansion must create a versioned successor release rather than silently mutating this frozen release.
