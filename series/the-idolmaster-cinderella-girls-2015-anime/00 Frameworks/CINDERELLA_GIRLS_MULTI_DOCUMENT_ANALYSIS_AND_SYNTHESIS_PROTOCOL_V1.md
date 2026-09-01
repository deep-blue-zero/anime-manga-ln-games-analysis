---
title: "THE IDOLM@STER CINDERELLA GIRLS (2015) — Multi-Document Analysis and Synthesis Protocol"
short_title: "Cinderella Girls Multi-Document Protocol"
version: "1.0"
status: "governing"
series: "THE IDOLM@STER CINDERELLA GIRLS"
primary_scope: "2015 TV anime Episodes 1–25"
supplementary_scope: "Episode 26 / Extra treated separately as epilogue or paratext"
primary_language: "Japanese"
derived_from:
  - "CinderellaGirlsAnalyticalMethod.txt"
  - "Episode-by-episode analyses through Episode 13"
  - "Cour 1 provisional synthesis through Episode 13"
purpose: "Govern ongoing episode analysis, retrospective migration, multi-document synthesis, evidence auditing, and final archival packaging."
---

# THE IDOLM@STER CINDERELLA GIRLS (2015)
## Multi-Document Analysis and Synthesis Protocol v1.0

> **Governing principle:**  
> **Allow the girls to become who they become at the same speed the anime allows them to become it.**

This document governs the continuing and retrospective analysis of the 2015 television anime **THE IDOLM@STER CINDERELLA GIRLS**.

It is intended to operate **in addition to**, not in replacement of, `CinderellaGirlsAnalyticalMethod.txt`.

The original analytical method defines **how an individual episode should be read**.

This protocol defines:

- how each episode analysis becomes a canonical archival artifact;
- how longitudinal character, relationship, production, institutional, performance, motif, and vocal evidence is accumulated;
- how provisional interpretations are preserved without being silently overwritten by hindsight;
- how mature claims are routed back to exact Japanese audiovisual evidence;
- how the first-cour analysis is retroactively migrated;
- how Episodes 14–25 should be analyzed as they are added;
- how Episode 26 should be treated separately;
- how specialist synthesis documents should be written without duplicating one another;
- and how the final full-series synthesis should be assembled and archived.

The objective is a traceable chain:

> **full-series claim → specialist synthesis → episode evidence ledger → source locator → original Japanese episode bundle**

The finished corpus should make it possible to answer both:

> **What did Episode 6 mean when Episode 6 was the latest evidence available?**

and:

> **What can the completed series later teach us about Episode 6?**

Those are not the same question. The architecture must preserve both.

---

# 1. Core analytical commitments

## 1.1 Anime-only primary evidentiary boundary

For the primary analysis, treat the 2015 anime as a self-contained authored work.

Do **not** allow the following to determine an episode's meaning before the anime itself establishes it:

- game characterization;
- card stories;
- later franchise material;
- later anime spin-offs;
- seiyuu commentary;
- staff commentary;
- fan reputation;
- popular fandom interpretations;
- wiki summaries;
- retrospective knowledge of later episodes;
- comparative knowledge from `U149`, 2011 `THE IDOLM@STER`, `Gakuen Idolmaster`, `IDOLY PRIDE`, `SHINE POST`, or other idol works.

These may later be used in specifically labeled comparative or external-production appendices.

The primary evidentiary hierarchy is:

1. **Japanese dialogue and program audio**
2. **Complete visual staging**
3. **Episode chronology and causal structure**
4. **Recurring patterns already established by earlier reviewed episodes**
5. **Later episodes, only during explicitly retrospective synthesis**
6. **Official production interviews, storyboards, fanbooks, and production notes**
7. **Franchise/game context**
8. **Reception history, criticism, and fandom interpretation**

Always distinguish:

> **"What this character is in the Cinderella Girls franchise"**

from:

> **"What the 2015 anime has presently established this character to be."**

The second is the governing object of the primary deep reading.

---

# 2. Chronological epistemic discipline

Chronological discipline is mandatory.

When analyzing Episode N:

- use Episodes 1 through N as semantic evidence;
- do not use Episodes N+1 onward;
- do not interpret an early image through a later payoff unless the analysis is explicitly labeled **Retrospective**;
- do not turn a later-established arc into an assumed early motivation;
- do not assume later relationships were already emotionally complete;
- do not treat a later institutional conflict as though it had already been revealed.

This applies even when later episode bundles already exist in storage.

## 2.1 Staging is not semantic access

A future episode may be:

- file-validated;
- counted;
- checksum-verified;
- confirmed to contain audio/subtitles/contact sheets;
- staged for later work.

That does **not** authorize reading its:

- Japanese dialogue;
- scene summaries;
- contact sheets;
- screenshots;
- audio;
- dialogue indices;
- scene indices;
- performance content;
- character actions.

A future bundle can be structurally validated without being semantically inspected.

> **Unreviewed material remains sealed until it is the active sequential target.**

This rule exists to prevent accidental hindsight contamination.

---

# 3. Source package requirements

For each reviewed episode, prefer a bundle containing:

- Japanese ASS or equivalent subtitle track;
- complete main Japanese program audio;
- dense subtitle-linked screenshots;
- shot-change or representative frames;
- all contact sheets;
- manifest;
- dialogue index;
- scene index;
- extraction statistics;
- optional CSV/JSON timing or visual metadata.

The analytical corpus should record source identity exactly.

For Episodes 1–25, the working Japanese subtitles are retimed Hulu Japanese subtitles matched to the Blu-ray main program audio.

Known timing policy:

- Episodes 01–11 and 13–25: approximately **+0.98 s fixed correction**
- Episode 12: approximately **+0.82 s fixed correction**
- no progressive drift was found in the validated source alignment

The analysis should use the main audio stream and exclude commentary audio unless commentary is being studied in a separate external-production appendix.

Episode 26 currently occupies a different source state and must be treated separately under the paratext protocol below.

---

# 4. Canonical corpus directory structure

Use the following conceptual corpus structure:

```text
CINDERELLA_GIRLS_2015_DEFINITIVE_ANALYSIS/
│
├── GOVERNING/
│   ├── CinderellaGirlsAnalyticalMethod.txt
│   └── CINDERELLA_GIRLS_MULTI_DOCUMENT_ANALYSIS_AND_SYNTHESIS_PROTOCOL_V1.md
│
├── SOURCE_INVENTORY/
│   ├── SOURCE_INVENTORY.md
│   ├── SOURCE_MANIFEST.json
│   └── SOURCE_CHECKSUMS.sha256
│
├── EPISODE_READINGS/
│   ├── CG2015_EP01_DEEP_READING.md
│   ├── CG2015_EP02_DEEP_READING.md
│   ├── ...
│   ├── CG2015_EP25_DEEP_READING.md
│   └── CG2015_EP26_EXTRA_DEEP_READING.md
│
├── CHECKPOINTS/
│   ├── CG2015_EP01-03_INITIAL_FORMATION_CHECKPOINT.md
│   ├── CG2015_EP04-06_EARLY_GROUP_CHECKPOINT.md
│   ├── optional local arc checkpoints
│   └── CG2015_COUR1_PROVISIONAL_SYNTHESIS.md
│
├── SYNTHESIS/
│   ├── 00_README_AND_CORPUS_MAP.md
│   ├── 01_SERIES_ARCHITECTURE_AND_EPISODE_PROGRESSION.md
│   ├── 02_NEW_GENERATIONS_CHARACTERS_AND_RELATIONAL_SYSTEM.md
│   ├── 03_TAKEP_PRODUCER_DEVELOPMENTAL_AUTHORSHIP_AND_RESPONSIBILITY.md
│   ├── 04_CINDERELLA_PROJECT_CHARACTERS_UNITS_AND_UNIT_ECOLOGIES.md
│   ├── 05_CINDERELLA_PROJECT_COLLECTIVE_FORMATION_LEADERSHIP_AND_BELONGING.md
│   ├── 06_346_PRODUCTION_INSTITUTIONS_AND_PHILOSOPHIES_OF_PRODUCTION.md
│   ├── 07_PERFORMANCE_SONGS_AUDIENCE_SUCCESS_AND_RECOGNITION.md
│   ├── 08_PERSONA_IMAGE_MEDIA_AND_SELF_AUTHORSHIP.md
│   ├── 09_FAILURE_CARE_AUTONOMY_AND_DEVELOPMENTAL_RISK.md
│   ├── 10_CINDERELLA_METAPHOR_VISUAL_ARCHITECTURE_TIME_SPACE_AND_MOTIFS.md
│   ├── 11_JAPANESE_VOICE_PERFORMED_VOCAL_STATES_AND_RELATIONAL_REGISTER.md
│   ├── 12_COMPARATIVE_REFERENCE_MATRICES_AND_OPEN_QUESTIONS.md
│   ├── 13_EPISODE_BY_EPISODE_EVIDENCE_LEDGER.md
│   ├── 14_PRIMARY_SOURCE_LOCATOR_AND_CLAIM_REVISION_LEDGER.md
│   ├── 15_EP26_EXTRA_EPILOGUE_AND_PARATEXT.md
│   └── CINDERELLA_GIRLS_FULL_SERIES_SYNTHESIS.md
│
└── AUDIT/
    ├── CORPUS_MANIFEST.md
    ├── CLAIM_INDEX.json
    ├── LOCATOR_INDEX.json
    ├── ARTIFACT_CHECKSUMS.sha256
    ├── DUPLICATION_AUDIT.md
    └── DELIVERY_AUDIT.md
```

The exact physical directory names may change if storage constraints require it. The **logical architecture and naming responsibilities should not**.

---

# 5. Canonical episode artifact naming

Each mainline episode receives one canonical Markdown artifact:

```text
CG2015_EPXX_DEEP_READING.md
```

Examples:

```text
CG2015_EP01_DEEP_READING.md
CG2015_EP13_DEEP_READING.md
CG2015_EP25_DEEP_READING.md
```

Episode 26 should be:

```text
CG2015_EP26_EXTRA_DEEP_READING.md
```

Do not label chat-response text itself as canonical merely because it was previously detailed.

For Episodes 1–13, create **source-audited reconstructions** of the prior work.

The prior episode analyses are:

> **claims and interpretive history to preserve**

but the source bundles are:

> **the evidentiary authority.**

If the source audit changes an earlier conclusion, record that change.

Do not silently rewrite history.

---

# 6. Canonical YAML metadata for episode artifacts

Each canonical episode file should begin with standardized YAML such as:

```yaml
---
series: "THE IDOLM@STER CINDERELLA GIRLS"
year: 2015
episode: 13
artifact_id: "CG2015_EP13_DEEP_READING"
artifact_type: "episode_deep_reading"
source_bundle: "ep13_screenshots(1).zip"
source_language: "Japanese"
spoiler_boundary: "E01-E13"
analysis_method: "CinderellaGirlsAnalyticalMethod.txt"
architecture_protocol: "CINDERELLA_GIRLS_MULTI_DOCUMENT_ANALYSIS_AND_SYNTHESIS_PROTOCOL_V1.md"
source_audit_status: "complete"
audio_reviewed: true
contact_sheets_reviewed: true
performance_analysis_required: true
performed_vocal_state_ledger: true
status: "canonical"
prospective_reading_preserved: true
retrospective_notes_allowed: false
---
```

When an episode is later revisited retrospectively, do not mutate the original prospective reading into a retrospective document.

Instead either:

- append a clearly separated `Retrospective Addendum`, or
- place the retrospective revision in Documents 01, 13, and 14.

The reader should always be able to reconstruct what was supportable at the original spoiler horizon.

---

# 7. Required episode-analysis workflow

Every episode receives three distinct analytical passes before synthesis.

## 7.1 Pass A — Narrative and dialogue reconstruction

Read the Japanese subtitle track chronologically.

Establish:

- scene progression;
- causal structure;
- who initiates decisions;
- what information each person presently possesses;
- explicit motivations;
- conflicts;
- resolutions or non-resolutions;
- relationship changes;
- jokes that double as characterization;
- repetitions;
- unusual lexical choices;
- incomplete statements;
- evasions;
- address terms;
- pronouns;
- politeness shifts;
- register shifts.

Always distinguish:

1. **what a character says**
2. **what the character appears to believe**
3. **what the episode demonstrates**

These are separate evidence categories.

Do not collapse them.

---

## 7.2 Pass B — Visual and sonic close reading

Inspect:

- **all contact sheets** supplied for the episode;
- representative full-resolution frames;
- shot-change frames;
- subtitle-linked images;
- silent passages;
- staging;
- blocking;
- camera distance;
- visual hierarchy;
- architecture;
- stairs/elevators;
- doors/windows/glass;
- costume;
- ordinary clothing;
- props;
- background activity;
- lighting;
- color;
- reflections;
- stage/backstage transitions;
- movement;
- audience framing;
- program audio;
- silence;
- music;
- vocal delivery;
- laughter, sighs, gasps, huffs, hesitations, crying, breath, and other minor vocalizations where they materially affect characterization.

Pay special attention to spatial relationships.

Ask:

- Who is above or below whom?
- Who is separated by glass, walls, doors, screens, or distance?
- Who occupies the center?
- Who is pushed toward the edge?
- Who moves while someone else remains still?
- Who looks toward a stage?
- Who is already standing on one?
- Who is isolated in an oversized room?
- Who is compressed into a group frame?
- When does institutional geography become emotional geography?

Contact sheets are reconnaissance, not substitutes for full-resolution evidence when a conclusion depends on composition or expression.

---

## 7.3 Pass C — Interpretive synthesis

Only after Passes A and B ask:

> **What is this episode actually doing?**

The synthesis should consider, when materially relevant:

- character development;
- relationship development;
- New Generations;
- unit ecology;
- Producer;
- production philosophy;
- 346 institutional structure;
- agency and developmental authorship;
- identity and self-image;
- persona and media;
- performance;
- four success axes;
- audience/recognition;
- visual motifs;
- Japanese voice;
- performed vocal state;
- thematic implications;
- unresolved questions;
- hypotheses that future episodes must test.

Do not force every category into every episode if the evidence is weak.

---

# 8. Required canonical episode output structure

The exact prose length may vary, but use the following default structure.

## 8.1 Header

- source and spoiler boundary;
- technical source note if relevant;
- episode-level thesis.

## 8.2 Pass A — Narrative and dialogue reconstruction

Chronological causal analysis, not plot recap.

## 8.3 Pass B — Visual and sonic close reading

Formal analysis grounded in actual staging and audio.

## 8.4 Dedicated performance analysis

Required whenever an important live, song, media performance, recording sequence, MC sequence, or staged promotional act carries dramatic meaning.

## 8.5 Pass C — Interpretive synthesis

Episode-level meaning derived from A and B.

## 8.6 Japanese voice analysis

Relevant speech patterns and longitudinal changes.

## 8.7 Performed-vocal-state ledger

Required from the point it became part of the project's standard method and recommended retroactively for earlier episodes when source auditing supports it.

## 8.8 Cumulative character ledgers

Update only characters materially affected.

## 8.9 New Generations relational ledger

When applicable.

## 8.10 Unit/Project relational ledger

When applicable.

## 8.11 Producer track

When applicable.

## 8.12 Philosophies-of-production ledger

When applicable.

## 8.13 Four forms of success

When the episode involves work, evaluation, performance, media exposure, audience response, or institutional advancement.

## 8.14 Motif ledger

Only record literal occurrence plus provisional meaning.

## 8.15 Hypothesis ledger

- Established
- Developing
- Speculative
- Revised

## 8.16 Cumulative delta

A compact final section stating:

> **What changed in the series model because this episode exists?**

This should prevent the long analysis from obscuring the actual longitudinal update.

---

# 9. Cumulative character ledger

For every principal or materially developing character, maintain:

### Current self-conception
How does the character presently understand herself?

### Desire
What does she presently want?

### Fear / vulnerability
What threatens that self-understanding or desire?

### Relationship to idolhood
Why is she doing this?

### Relationship to performance
What does the stage mean to her?

### Relationship to recognition
What does she want audiences, peers, professionals, friends, or family to see?

### Speech / voice markers
Track:

- first-person pronouns;
- second-person/address forms;
- sentence endings;
- politeness;
- contractions;
- dialect;
- tempo;
- hesitation;
- self-correction;
- catchphrases;
- private/professional differences;
- senior/junior differences;
- unit-specific speech;
- onstage speech.

### Performed vocal states
Track changes under:

- ordinary conversation;
- professional presentation;
- private intimacy;
- anxiety;
- anger;
- shame;
- exhaustion;
- illness;
- performance;
- MC;
- recording;
- crisis;
- reconciliation.

### Relational position
Who does she presently:

- trust;
- admire;
- depend upon;
- resent;
- compete with;
- protect;
- misunderstand;
- imitate;
- challenge?

### Agency
Is development being:

- self-initiated;
- peer-elicited;
- Producer-elicited;
- institutionally assigned;
- collaboratively authored;
- externally imposed?

### Open questions
What remains unresolved at the present spoiler horizon?

Do not convert open questions into promises of future arcs.

---

# 10. New Generations relational ledger

Uzuki, Rin, and Mio require independent character analysis **and** a dedicated relational ledger.

For every major change ask:

- Who currently needs the group most?
- Who is carrying whom?
- Who currently provides momentum?
- Who provides stabilization?
- Who supplies continuity?
- Who questions the group?
- Who currently leads, if anyone?
- Is leadership fixed or mobile?
- Who feels ahead?
- Who fears being left behind?
- What does New Generations mean to each member now?
- Is the group currently functioning as:
  - friendship;
  - professional unit;
  - emotional refuge;
  - identity;
  - shared ambition;
  - public brand;
  - some combination?
- Does individual ambition threaten the group, deepen it, or expose asymmetry?
- Does the anime present difference as betrayal, maturation, necessary tension, or something else?

Never assume the three arcs run in parallel.

**Asynchronous development is a feature to measure, not an imbalance to correct.**

---

# 11. Producer / TakeP analytical track

Treat Producer as a principal developing character.

For each relevant episode track:

- how he identifies potential;
- what evidence he uses;
- how he communicates judgments;
- what he withholds;
- what he explains;
- when he intervenes;
- when he deliberately does not intervene;
- when he avoids;
- what he misunderstands;
- how he defines success;
- how he reacts to failure;
- how he treats uncertainty;
- whether he sees idols as:
  - talent;
  - employees;
  - developing persons;
  - collaborators;
  - children;
  - clients;
  - organizational resources;
- how his speech acts change;
- how the girls alter his professional philosophy;
- how his bodily/staging presence changes;
- how his very low vocal identity changes pragmatically even when timbre remains stable.

Preserve the distinction:

> **supporting a person's existing desire**

versus:

> **authoring a desire for that person.**

Also distinguish:

> **giving autonomy**

from:

> **withdrawing responsibility.**

And:

> **protective authority**

from:

> **controlling authorship.**

---

# 12. Philosophies-of-production ledger

Whenever any adult, idol, trainer, executive, senior performer, unit, or staff member articulates or embodies an assumption about production, record it.

Questions include:

- Is an idol discovered or created?
- Can potential be seen before the person sees it?
- When does recognition become projection?
- Does a producer serve an identity or construct it?
- What should be disclosed to a developing performer?
- How much uncertainty is acceptable?
- How much discomfort is legitimate?
- When is experience worth risk?
- When does freedom require supervision?
- Who is responsible when an experiment fails?
- Should units preserve emotional bonds?
- Should units maximize artistic/commercial opportunity?
- Is specialization liberation, confinement, or both?
- Can a persona be professionally designed and still be sincere?
- What does a corporation owe a performer after selecting her?
- What does a performer owe the opportunity she receives?
- Is success:
  - commercial;
  - technical;
  - social;
  - personal;
  - institutional;
  - artistic?
- Which success categories can conflict?

Do not begin with moral labels such as:

> Producer good / executive bad.

First identify what an approach **achieves**, **damages**, **assumes**, and **fails to see**.

---

# 13. Performance analysis protocol

Every major performance should be read as a dramatic scene, not a music video.

Track:

- why it occurs;
- how the opportunity was allocated;
- who selected the song;
- who authored lyrics or staging where known;
- whose emotional problem the performance answers;
- what it does not answer;
- center position;
- line distribution;
- choreography;
- physical coordination;
- facial expression;
- MC;
- audience depiction;
- venue scale;
- crowd density;
- lighting;
- costume;
- backstage preparation;
- professional infrastructure;
- technical disruption;
- cutaways;
- whether another character watches;
- whether the performer sees the audience;
- whether the audience is presented as:
  - mass;
  - faces;
  - friends;
  - strangers;
  - consumers;
  - correspondents;
- whether the performance resolves, reframes, masks, or merely postpones a conflict.

Always ask:

> **What can this character communicate through performance that she cannot communicate through ordinary dialogue?**

Do not interpret lyrics as direct interior monologue automatically.

Lyrics may function as:

- character expression;
- unit philosophy;
- formal commentary;
- dramatic irony;
- audience-facing text;
- franchise song language;
- multiple layers simultaneously.

State the confidence level.

---

# 14. Four forms of success

Never collapse all professional outcomes into "success" or "failure."

Track at least:

## Commercial success

- attendance;
- sales;
- visibility;
- rankings;
- corporate value;
- media attention;
- market reach.

## Technical success

- singing;
- dancing;
- staging;
- execution;
- timing;
- MC;
- recovery from mistakes;
- professional reliability.

## Social success

- unit cohesion;
- peer recognition;
- audience relationship;
- professional trust;
- group resilience;
- collaborative development.

## Personal success

- whether the experience means what the performer wanted it to mean;
- whether she recognizes herself in the result;
- whether the experience produces fulfillment, shame, alienation, curiosity, fear, or a revised desire.

One event can succeed on one axis and fail on another.

This distinction is mandatory whenever evaluation matters.

---

# 15. Japanese voice and performed-vocal-state protocol

Japanese voice is character evidence.

Do not reduce voice analysis to pitch or catchphrases.

Track:

- grammar;
- pronouns;
- address;
- politeness;
- sentence endings;
- lexical habits;
- rhythm;
- tempo;
- pausing;
- hesitation;
- breath;
- laughter;
- crying;
- huffs;
- sighs;
- volume;
- attack;
- projection;
- register;
- code-switching;
- relational changes by interlocutor.

## 15.1 Performed-vocal-state ledger template

For relevant characters:

| Character | Baseline | Stress/private state | Performance/public state | Integrated/recovered state | Dramatic meaning |
|---|---|---|---|---|---|

Where helpful, acoustic measurements may be used as **supplementary evidence**.

Do not treat pitch-tracking from mixed program audio as publication-grade source-isolated measurement.

Prefer:

> audible relational change + cautious quantitative support

over:

> false precision.

The central question is:

> **How does this character construct herself through sound, and what new emotional or social functions can the established voice carry over time?**

Character maturity does not necessarily mean:

- lower pitch;
- calmer voice;
- less stylization;
- more adult speech.

Often development means:

> **the same voice becomes capable of carrying more truth.**

---

# 16. Visual motif ledger

Track motifs from first occurrence without assigning final meaning prematurely.

Potential categories include:

- stairs;
- elevators;
- doors;
- windows;
- glass;
- thresholds;
- clocks;
- shoes;
- feet;
- flowers;
- rain;
- sunlight;
- artificial light;
- shadows;
- mirrors;
- reflections;
- photographs;
- cameras;
- screens;
- empty rooms;
- offices;
- stages;
- backstage;
- corridors;
- costumes;
- ordinary clothing;
- city/castle imagery;
- stars;
- hands/touch;
- paperwork;
- movement upward/downward;
- stopping/following;
- crowd density;
- dream/reality vocabulary.

Each motif entry should record:

```text
episode
timestamp/scene
character(s)
literal visual fact
formal function
provisional interpretation
confidence
later recurrence
revision status
```

Only at major checkpoints should motifs be upgraded from:

> incidental object

to:

> recurring image

to:

> strong motif

to:

> governing visual structure.

Avoid universal codes such as:

> light = good  
> darkness = bad

unless the complete evidence truly supports them.

---

# 17. Background-character restraint

The anime exists inside a franchise with a huge cast.

Do not allow recognition of a cameo to manufacture narrative importance.

If an idol appears only in the background:

> record the cameo if analytically useful.

Do not import:

- game personality;
- later stories;
- fandom status;
- famous songs;
- future franchise importance.

If the anime later gives the character narrative weight, revisit the earlier appearance retrospectively.

This preserves the distinction between:

> world density

and:

> active characterization.

---

# 18. Hypothesis ledger

Every episode should finish with explicit epistemic classification.

## Established

Claims strongly supported by present evidence.

## Developing

Patterns supported by multiple pieces of evidence but not settled.

## Speculative

Interesting possibilities requiring later confirmation.

## Revised

Earlier hypotheses materially complicated, narrowed, or disproved.

When a claim changes status, record:

- old status;
- new status;
- triggering episode;
- reason.

Do not convert a clever interpretation into fact because it is elegant.

---

# 19. Checkpoint architecture

Do not constantly rewrite the full series model.

Use frozen checkpoints.

## 19.1 Episodes 1–3

```text
CG2015_EP01-03_INITIAL_FORMATION_CHECKPOINT.md
```

Question:

> Who are these people before the ensemble stabilizes?

## 19.2 Episodes 4–6

```text
CG2015_EP04-06_EARLY_GROUP_CHECKPOINT.md
```

Question:

> What relational, institutional, and production patterns have emerged without assuming permanence?

## 19.3 Local arc checkpoints

Create only when the narrative itself produces a meaningful boundary.

Do not impose arbitrary three-episode blocks.

## 19.4 End of Cour 1 / Episode 13

```text
CG2015_COUR1_PROVISIONAL_SYNTHESIS.md
```

This document must be **frozen** after migration/audit.

It should preserve the Episode-13 horizon:

- ensemble formation;
- New Generations;
- Producer;
- unit ecology;
- Cinderella Project identity;
- production philosophies;
- audience/recognition;
- visual motif inventory;
- Japanese voice;
- performed-vocal architecture;
- open questions entering Cour 2.

Later episodes may revise its conclusions elsewhere.

Do not silently update the Cour 1 synthesis into end-of-series knowledge.

---

# 20. Second-cour continuation rules

When Episodes 14–25 are added:

1. treat Episode 14 as the next sequential target;
2. preserve the Episode-13 model as the starting epistemic state;
3. do not retrospectively rewrite Cour 1 before Episode 14 has been analyzed;
4. produce the canonical episode artifact immediately;
5. update Documents 13 and 14 immediately;
6. add **deltas** to specialist documents rather than fully rewriting them after every episode;
7. create local checkpoints only where the narrative warrants them;
8. reserve complete arc claims for Episode 25.

For every second-cour episode explicitly ask:

> **What does this episode preserve, complicate, overturn, or newly expose about the frozen Cour 1 model?**

Do not assume that a first-cour open question necessarily becomes a second-cour storyline.

Let the anime decide.

---

# 21. Episode 26 / Extra protocol

Episode 26 should not be allowed to silently redefine the mainline Episode 1–25 structure.

Treat it as:

> **supplementary animated material / epilogue / paratext**

unless close reading demonstrates a stronger canonical structural function.

Use:

```text
15_EP26_EXTRA_EPILOGUE_AND_PARATEXT.md
```

Questions:

- What does it extend?
- What does it merely play with?
- Does it provide post-series ordinary-life texture?
- Does it deepen performance or character knowledge?
- Does it alter any mainline claim?
- Is that alteration strong enough to require a revision ledger entry?

If the currently available Episode 26 subtitle source is English-only while Japanese audio is present:

- treat Japanese audio as primary;
- use English subtitle text as navigation/secondary support;
- do not build fine Japanese linguistic claims from English subtitles;
- where exact Japanese wording materially matters, reconstruct only when the audio is clear enough to support it;
- mark uncertain Japanese transcription explicitly;
- do not pretend Episode 26 has the same linguistic evidentiary status as Episodes 1–25.

---

# 22. Retroactive migration of Episodes 1–13

The existing analyses through Episode 13 are valuable but should be migrated carefully.

## Phase R1 — source inventory

For each episode:

- confirm source bundle filename;
- record SHA-256 if available;
- confirm audio;
- confirm Japanese ASS;
- record screenshot count;
- record contact-sheet count;
- confirm indices;
- record known subtitle timing correction.

## Phase R2 — source audit

Re-open the primary evidence.

At minimum:

- read/recheck the Japanese ASS;
- inspect all contact sheets;
- inspect full-resolution evidence for major visual claims;
- use audio for vocal/performance claims.

## Phase R3 — claim migration

Convert the prior analysis into a canonical episode artifact.

Every major earlier conclusion becomes:

- VERIFIED;
- QUALIFIED;
- REVISED;
- RETIRED;
- or UNRESOLVED.

## Phase R4 — locator backfill

Add exact or near-exact audiovisual locators for load-bearing claims.

## Phase R5 — ledger population

Populate:

- Document 13 episode evidence ledger;
- Document 14 source locator / claim revision ledger.

Do not claim a historic chat analysis had exact locators if it did not.

The canonical migration may preserve the interpretation while adding evidence precision.

---

# 23. Primary-source locator syntax

Audiovisual analysis requires multiple locator types.

Use a consistent syntax.

Examples:

```text
E05-T18:42-20:11
E05-ASS0412-0447
E05-CS29-31
E05-FRAME_000521
E05-AUDIO18:53-19:21
E05-SCENE09
```

Definitions:

- `E05-T...` — episode timestamp span
- `E05-ASS...` — subtitle cue range
- `E05-CS...` — contact-sheet range
- `E05-FRAME...` — exact retained frame/screenshot identifier
- `E05-AUDIO...` — audio interval
- `E05-SCENE...` — scene-index identifier

A mature claim should use the locator types appropriate to its evidence.

### Linguistic claim

Prefer:

```text
timestamp + ASS cue
```

### Vocal-performance claim

Prefer:

```text
timestamp + audio interval + ASS cue where relevant
```

### Visual-composition claim

Prefer:

```text
timestamp + full-resolution frame + contact-sheet context
```

### Performance-sequence claim

Prefer:

```text
timestamp span + audio + visual sequence + relevant lyrics/dialogue cues
```

Never cite a contact sheet alone when the claim depends on subtle expression, composition, or text that requires the original frame.

---

# 24. Document 13 — Episode-by-episode evidence ledger

`13_EPISODE_BY_EPISODE_EVIDENCE_LEDGER.md` is the canonical chronological spine.

It should be comparatively compact.

For every episode record:

- source status;
- spoiler horizon;
- episode thesis;
- governing dramatic question;
- decisive chronology;
- key Japanese evidence;
- key visual evidence;
- key sonic evidence;
- character deltas;
- relationship deltas;
- Producer delta;
- production-philosophy delta;
- performance delta;
- four success axes;
- motif entries;
- vocal-state entries;
- Established;
- Developing;
- Speculative;
- Revised;
- open questions.

Its function is not to replace the episode essay.

Its function is to answer:

> **What did this episode add to the cumulative model?**

---

# 25. Document 14 — Primary source locator and claim-revision ledger

`14_PRIMARY_SOURCE_LOCATOR_AND_CLAIM_REVISION_LEDGER.md` is the corpus's provenance engine.

Each important longitudinal claim should receive an ID.

Recommended namespaces:

```text
CG-CHAR-
CG-NG-
CG-PROD-
CG-INST-
CG-PERF-
CG-VOICE-
CG-MOTIF-
CG-REL-
CG-ETHICS-
CG-CIND-
```

Example:

```text
Claim ID:
CG-PROD-0057

Claim:
Episode 5 establishes that Producer has a plan for all members
but fails to communicate enough provisional information for Miku
to understand her waiting as meaningful.

Original analytical status:
Strong interpretive conclusion.

Primary evidence:
E05-T18:42-20:11
E05-ASS0412-0447
E05-CS29-31

Key Japanese:
「皆さん全員分考えています」
「まだ決定ではないので話せませんでしたが」
「早く言ってニャ」

Audit result:
VERIFIED

Primary home:
03_TAKEP_PRODUCER_DEVELOPMENTAL_AUTHORSHIP_AND_RESPONSIBILITY.md

Secondary homes:
06_346_PRODUCTION_INSTITUTIONS_AND_PHILOSOPHIES_OF_PRODUCTION.md
09_FAILURE_CARE_AUTONOMY_AND_DEVELOPMENTAL_RISK.md

Revision history:
None.
```

Permitted audit states:

- `VERIFIED`
- `VERIFIED_STRENGTHENED`
- `QUALIFIED`
- `REVISED`
- `RETIRED`
- `UNSUPPORTED`
- `OPEN`

This ledger should make interpretive change visible.

---

# 26. Specialist synthesis architecture

The specialist documents divide the completed work by governing question.

They should not become independent mini-series summaries.

---

## 26.1 `01_SERIES_ARCHITECTURE_AND_EPISODE_PROGRESSION.md`

Primary responsibility:

> **How does the dramatic problem change from Episode 1 through Episode 25?**

Include:

- major movements;
- local arc boundaries;
- causal progression;
- cour architecture;
- how later phases revise earlier ones;
- where the anime changes governing questions.

Do not duplicate full character biographies.

This is the chronological synthesis.

---

## 26.2 `02_NEW_GENERATIONS_CHARACTERS_AND_RELATIONAL_SYSTEM.md`

Primary responsibility:

> **What do Uzuki, Rin, and Mio become individually, and what kind of relational system is New Generations?**

Recommended structure:

1. Shimamura Uzuki deep dive
2. Shibuya Rin deep dive
3. Honda Mio deep dive
4. New Generations formation
5. asynchronous development
6. role mobility
7. leadership
8. private relational culture
9. professional identity
10. audience/recognition
11. conflict and repair
12. final unit status
13. prospective versus retrospective corrections

Do not create three completely independent documents unless later corpus scale proves necessary.

Their scenes are too relationally intertwined for full duplication to be efficient.

---

## 26.3 `03_TAKEP_PRODUCER_DEVELOPMENTAL_AUTHORSHIP_AND_RESPONSIBILITY.md`

Primary responsibility:

> **What does Producer learn production is?**

Include:

- recruitment/recognition;
- smile criterion;
- professional opacity;
- institutional knowledge;
- communication failures;
- intervention/non-intervention;
- fear of over-authorship;
- relational avoidance;
- repair;
- translation;
- autonomy;
- accountability;
- delegation;
- safeguarding;
- expectation management;
- speech-act development;
- vocal continuity;
- supporting versus authoring desire;
- final production philosophy.

Do not turn this into a generic "best Producer" comparison.

Comparative material belongs primarily in Document 12.

---

## 26.4 `04_CINDERELLA_PROJECT_CHARACTERS_UNITS_AND_UNIT_ECOLOGIES.md`

Primary responsibility:

> **What kind of person does each non-NG principal idol become, and what kind of social structure allows her to function professionally?**

Cover:

- Minami;
- Anastasia;
- Miku;
- Riina;
- Ranko;
- Chieri;
- Kanako;
- Anzu;
- Kirari;
- Rika;
- Miria;
- other materially developed Project idols;
- LOVE LAIKA;
- Candy Island;
- Dekoration;
- Asterisk;
- solo artistic structures.

For each unit ask:

- formation path;
- relational mechanism;
- conflict style;
- care style;
- performance philosophy;
- relation to Producer;
- relation to Project;
- vulnerability;
- what the unit makes possible that the individual alone could not do.

---

## 26.5 `05_CINDERELLA_PROJECT_COLLECTIVE_FORMATION_LEADERSHIP_AND_BELONGING.md`

Primary responsibility:

> **How does a corporate roster become a social/professional collective?**

Track stages such as:

- roster;
- cohort;
- staggered trajectories;
- unit network;
- community of practice;
- mutual interpretive literacy;
- shared rhythm;
- recoverability;
- leadership;
- belonging;
- conflict;
- differentiation.

Do not call the Project a **family** automatically.

Ask whether the evidence supports:

- family;
- cohort;
- workplace;
- network;
- team;
- community;
- professional collective;
- hybrid structure.

Name the form the anime actually builds.

---

## 26.6 `06_346_PRODUCTION_INSTITUTIONS_AND_PHILOSOPHIES_OF_PRODUCTION.md`

Primary responsibility:

> **What does the institution do to make idolhood possible, and what forms of power does that give it?**

Analyze:

- selection;
- training;
- resources;
- timing;
- unit allocation;
- staffing;
- creators;
- songs;
- costumes;
- media access;
- schedules;
- professional evaluation;
- corporate expectation;
- visibility;
- risk;
- safety;
- bureaucracy;
- communication;
- unequal opportunity;
- path dependence;
- institutional promises.

Separate:

- individual Producer;
- department staff;
- senior idols;
- executives;
- larger 346 logic.

Do not reduce the institution to either benevolent home or oppressive machine without sufficient evidence.

---

## 26.7 `07_PERFORMANCE_SONGS_AUDIENCE_SUCCESS_AND_RECOGNITION.md`

Primary responsibility:

> **What does public performance do that ordinary interaction cannot?**

Include:

- all major live sequences;
- important recorded performances;
- media performance;
- MC;
- crowd representation;
- applause;
- audience scale;
- fan response;
- fan letters;
- spectatorship;
- performer seeing audience;
- audience seeing performer;
- four success categories;
- stage as experiment;
- stage as confirmation;
- stage as crisis;
- stage as interpretation.

This is also the primary home for the longitudinal **smile/recognition** argument.

---

## 26.8 `08_PERSONA_IMAGE_MEDIA_AND_SELF_AUTHORSHIP.md`

Primary responsibility:

> **What is the relation between person, public image, aspiration, camera, costume, and authored identity?**

Analyze:

- PR video;
- promotional photography;
- camera behavior;
- personas;
- Miku;
- Riina;
- Ranko;
- Anzu;
- character branding;
- professional self-presentation;
- private/public register;
- self-caricature;
- costume;
- image selection;
- mediated identity.

Reject the simplistic binary:

> persona = fake  
> spontaneity = true.

Ask instead:

- who authored the form;
- whether the performer recognizes herself in it;
- what the form communicates;
- what the form hides;
- whether the institution reduces the person to it.

---

## 26.9 `09_FAILURE_CARE_AUTONOMY_AND_DEVELOPMENTAL_RISK.md`

Primary responsibility:

> **Who is permitted to fail, who carries the consequences, and what distinguishes ethical developmental challenge from abandonment or control?**

Analyze:

- failed auditions;
- readiness;
- first live;
- Miku protest;
- Mio crisis;
- Producer failure;
- Chieri anxiety;
- Minami over-responsibility;
- substitutions;
- illness;
- experimentation;
- freedom;
- safeguarding;
- peer care;
- recovery;
- retries;
- accountability.

Core distinctions:

- autonomy vs withdrawal;
- protection vs control;
- challenge vs negligence;
- support vs authorship;
- failure vs disposability;
- recoverability vs perfection.

---

## 26.10 `10_CINDERELLA_METAPHOR_VISUAL_ARCHITECTURE_TIME_SPACE_AND_MOTIFS.md`

Primary responsibility:

> **How does the anime think visually?**

Analyze:

- Cinderella fairy-tale vocabulary;
- castle;
- stairs;
- clock/time;
- doors;
- thresholds;
- stage/backstage;
- verticality;
- offices;
- corridors;
- home;
- public city space;
- light/darkness;
- rain;
- flowers;
- hands;
- photographs;
- paperwork;
- ordinary clothing/costume;
- feet/shoes;
- movement/stillness;
- crowd density;
- dream/reality.

Do not finalize exact motif meanings until the full mainline has been reviewed.

---

## 26.11 `11_JAPANESE_VOICE_PERFORMED_VOCAL_STATES_AND_RELATIONAL_REGISTER.md`

Primary responsibility:

> **How does voice construct identity, and how does the same voice change function across development?**

Include:

- principal cast speech profiles;
- Producer;
- New Generations;
- units;
- relational register;
- professional/private shifts;
- stress states;
- performance states;
- catchphrase use;
- catchphrase suspension;
- vocal recovery;
- meaningful pauses;
- delivery under conflict;
- performance diction;
- MC;
- private family speech where relevant.

The final argument should be built from longitudinal evidence, not from isolated impressions.

---

## 26.12 `12_COMPARATIVE_REFERENCE_MATRICES_AND_OPEN_QUESTIONS.md`

Primary responsibility:

> **Make the completed Cinderella Girls analysis reusable without allowing comparison to contaminate the primary reading.**

Only after the independent series model stabilizes, compare when useful with:

- `THE IDOLM@STER CINDERELLA GIRLS U149`
- 2011 `THE IDOLM@STER`
- `SHINE POST`
- `Love Live! Superstar!!`
- `Gakuen Idolmaster`
- `IDOLY PRIDE`
- other relevant performance narratives.

Possible dimensions:

- Producer philosophy;
- adult/performer relationship;
- institutional structure;
- group formation;
- performance philosophy;
- persona;
- public image;
- failure;
- audience;
- leadership;
- recognition;
- voice;
- dream/realism.

Keep comparison subordinate to the Cinderella Girls evidence.

---

# 27. Primary-home anti-duplication rules

Every major argument gets one **primary home**.

Other documents may summarize and cross-reference it, but should not rebuild the full argument.

Examples:

| Question | Primary home |
|---|---|
| Final meaning of smile/recognition | `07` |
| Producer's use of 「笑顔です」 | `03` |
| Uzuki's personal relationship to smile | `02` |
| Vocal smile/performed delivery | `11` |
| Episode-by-episode smile evidence | `13` |
| Exact source locators | `14` |
| Miku as character/persona | `04` |
| Persona as general theory | `08` |
| Institutional unit formation | `06` |
| Asterisk stage as performance | `07` |
| Cat/rock visual opposition | `10` |
| Minami as character/unit member | `04` |
| Minami as Project leader | `05` |
| Producer delegating to Minami | `03` |
| Leadership as production philosophy | `06` / `09`, summarized from `05` |

Before adding a long section, ask:

> **Does this argument already have a primary home?**

If yes, summarize rather than duplicate.

---

# 28. Recommended production sequence

Do not draft the numbered synthesis documents in numerical order.

## Phase 0 — Architecture and source lock

Create/finalize:

- this protocol;
- source inventory;
- source manifest;
- checksums where practical;
- governing method preservation.

No narrative analysis of unreviewed episodes.

---

## Phase 1 — Retroactive Episodes 1–13 migration

Audit sequentially.

Recommended small batches:

- E01–E03
- E04–E06
- E07–E09
- E10–E11
- E12–E13

For each:

1. source audit;
2. canonical episode artifact;
3. Document 13 update;
4. Document 14 update;
5. checkpoint preservation where relevant.

Do not wait until all thirteen are complete before beginning provenance work.

---

## Phase 2 — Cour 1 specialist scaffolding

After E01–E13 migration:

- freeze the canonical Cour 1 synthesis;
- create **provisional Cour-1-only sections** for Documents 01–12;
- label them provisional;
- preserve open questions.

Do not turn them into final-series documents.

---

## Phase 3 — Sequential Episodes 14–25

For every new episode:

1. validate source package;
2. analyze only the active episode;
3. create canonical episode artifact;
4. update Document 13;
5. update Document 14;
6. append specialist **deltas**;
7. create local checkpoint only if narratively warranted.

Do not perform a full rewrite of every specialist document after every episode.

---

## Phase 4 — Episode 25 full-mainline audit

After Episode 25:

1. freeze the prospective E25 endpoint;
2. audit every major first-cour thesis;
3. stress-test major interpretations with counterevidence;
4. revisit unresolved hypotheses;
5. finalize motif recurrence;
6. finalize character arcs;
7. finalize production philosophy;
8. finalize institutional analysis;
9. finalize Project identity;
10. explicitly record what Cour 1:
   - got right;
   - underweighted;
   - overclaimed;
   - could not yet know.

---

## Phase 5 — Episode 26 paratext

Analyze Episode 26 separately.

Do not allow supplementary tone or comedy to overwrite the mainline by default.

---

## Phase 6 — Mature specialist synthesis

Finalize Documents 01–12.

Recommended order:

1. `13_EPISODE_BY_EPISODE_EVIDENCE_LEDGER.md`
2. `14_PRIMARY_SOURCE_LOCATOR_AND_CLAIM_REVISION_LEDGER.md`
3. `01_SERIES_ARCHITECTURE_AND_EPISODE_PROGRESSION.md`
4. `02_NEW_GENERATIONS_CHARACTERS_AND_RELATIONAL_SYSTEM.md`
5. `03_TAKEP_PRODUCER_DEVELOPMENTAL_AUTHORSHIP_AND_RESPONSIBILITY.md`
6. `04_CINDERELLA_PROJECT_CHARACTERS_UNITS_AND_UNIT_ECOLOGIES.md`
7. `05_CINDERELLA_PROJECT_COLLECTIVE_FORMATION_LEADERSHIP_AND_BELONGING.md`
8. `06_346_PRODUCTION_INSTITUTIONS_AND_PHILOSOPHIES_OF_PRODUCTION.md`
9. `08_PERSONA_IMAGE_MEDIA_AND_SELF_AUTHORSHIP.md`
10. `09_FAILURE_CARE_AUTONOMY_AND_DEVELOPMENTAL_RISK.md`
11. `07_PERFORMANCE_SONGS_AUDIENCE_SUCCESS_AND_RECOGNITION.md`
12. `10_CINDERELLA_METAPHOR_VISUAL_ARCHITECTURE_TIME_SPACE_AND_MOTIFS.md`
13. `11_JAPANESE_VOICE_PERFORMED_VOCAL_STATES_AND_RELATIONAL_REGISTER.md`
14. `15_EP26_EXTRA_EPILOGUE_AND_PARATEXT.md`
15. `12_COMPARATIVE_REFERENCE_MATRICES_AND_OPEN_QUESTIONS.md`

This order may be adjusted if later evidence reveals a more efficient dependency chain.

---

## Phase 7 — Continuous full-series synthesis

Write:

```text
CINDERELLA_GIRLS_FULL_SERIES_SYNTHESIS.md
```

only after the specialist corpus is stable.

This should be a continuous literary argument.

It should **not** reproduce Documents 01–15 section by section.

Its role is to answer:

> **What kind of work is THE IDOLM@STER CINDERELLA GIRLS, and what does the complete anime ultimately argue through its characters, institutions, performances, relationships, images, and fairy-tale structure?**

Use the specialist documents as evidentiary substrate.

---

## Phase 8 — External production and reception appendix

Only after the independent reading is committed:

research and classify, if desired:

- director interviews;
- writer interviews;
- official fanbook material;
- storyboards;
- production notes;
- Japanese contemporary criticism;
- English criticism;
- contemporary fan response.

Classify external material as:

- **Confirmation**
- **Production Evidence**
- **Alternative Reading**
- **Correction**
- **Reception History**

Do not let external criticism become invisible scaffolding for the independent analysis.

---

## Phase 9 — README, archive, and immutable release

Write `00_README_AND_CORPUS_MAP.md` last.

Then:

- create corpus manifest;
- verify YAML;
- verify internal links;
- verify locator syntax;
- verify source inventory;
- run duplicate-prose audit;
- run claim-provenance audit;
- calculate artifact checksums;
- ensure no copyrighted audiovisual source bundles are accidentally packaged;
- package only analytical artifacts and permitted metadata;
- create release checksum;
- mark the final release immutable.

Future corrections become a new release version.

Do not silently mutate the frozen release.

---

# 29. Final continuous synthesis requirements

The final full-series synthesis should address at minimum:

## The work as a whole
What kind of idol story is this?

## Cinderella as governing metaphor
What does transformation actually mean?

## New Generations
What is the group's complete relational architecture?

## Uzuki
Effort, smile, ordinariness, selfhood, performance, desire.

## Rin
Discovery, skepticism, desire, differentiation, trust, belonging.

## Mio
Recognition, narrative, shame, leadership, emotional labor, resilience.

## Producer
Developmental authorship, communication, responsibility, growth.

## Cinderella Project
Roster, cohort, unit network, collective, belonging, resilience.

## 346 Production
Institution, resources, allocation, promises, power.

## Competing production philosophies
What different people believe idols need.

## Persona
Constructed image, selective truth, authorship, aspiration.

## Performance
What the stage allows that ordinary language does not.

## Audience
Recognition, scale, reciprocity, correspondence.

## Failure
Who is allowed to fail, what happens afterward.

## Care and autonomy
Support, intervention, freedom, responsibility.

## Individualization versus belonging
How distinct people remain distinct inside larger structures.

## Visual architecture
Castle, stairs, time, thresholds, stage/backstage, images, movement.

## Japanese voice
Longitudinal speech and vocal-state development.

## Dream and reality
What the final work does with the fairy-tale promise.

Strong claims about complete arcs or final motif meanings should be made **only here or in final specialist documents after Episode 25 has been fully audited**.

---

# 30. Claim-quality rules

Before allowing a claim into a mature synthesis, ask:

### Is it directly evidenced?
If yes, identify the locator.

### Is it interpretive?
If yes, identify what evidence makes the interpretation stronger than alternatives.

### Is there counterevidence?
If yes, include it or narrow the claim.

### Is it actually longitudinal?
If yes, cite multiple episodes.

### Is it merely a trope assumption?
If yes, remove it unless the anime independently establishes it.

### Is it imported from franchise knowledge?
If yes, quarantine it from the primary analysis.

### Is it a motif claim?
If yes, show recurrence.

### Is it a complete-arc claim?
If yes, verify Episode 25 boundary.

### Is it a vocal claim?
If yes, use program audio.

### Is it a visual claim?
If yes, inspect full-resolution evidence.

### Is it a performance claim?
If yes, analyze performance as scene, not isolated song.

---

# 31. Counterevidence and adversarial rereading

After Episode 25, every major thesis should receive an adversarial pass.

For each strong claim ask:

> **What would I cite if I wanted to argue the opposite?**

Examples:

- If claiming Producer increasingly supports autonomy, identify moments where he still imposes.
- If claiming the Project becomes a family, identify evidence that it remains workplace/institution.
- If claiming a persona is self-authored, identify where external branding constrains it.
- If claiming a relationship is mutually supportive, identify asymmetry.
- If claiming a performance resolves a conflict, identify evidence of residual distress.
- If claiming a motif has stable meaning, identify contradictory uses.

Strong synthesis should survive contradiction rather than omit it.

---

# 32. Prospective versus retrospective reading

This corpus must preserve two modes.

## Prospective reading

What the anime permitted us to know at that point.

Example:

```text
Episode 1 prospective:
Producer's smile criterion is perceptive but underexplained; whether it is true recognition or projection remains open.
```

## Retrospective reading

What later episodes allow us to reconsider.

Example form:

```text
Full-series retrospective:
Later evidence may show that the Episode 1 criterion participates in a broader philosophy of potential, image, or recognition.
```

Do not erase the first statement with the second.

The difference between them is analytically valuable.

---

# 33. Provisional word-length guidance

Do not target length for its own sake.

Approximate planning ranges:

### Episode canonical readings
Enough to preserve the actual evidence and causal analysis. Some episodes may require substantially more than others.

### Specialist synthesis corpus
Likely **90,000–140,000+ words** if the second cour sustains the first cour's density.

### Continuous final synthesis
Likely **30,000–50,000 words**, depending on how much argument can be delegated to specialist documents without becoming skeletal.

These are planning ranges, not quotas.

> **Added length from duplicated summary is not added depth.**

---

# 34. Comparative-analysis quarantine

Comparisons with other idol works can be valuable, but only after the internal Cinderella Girls argument is stable.

When comparisons are introduced:

1. state the Cinderella Girls finding first;
2. state the comparison dimension;
3. use the comparison to sharpen distinction;
4. do not use another work as proof of what Cinderella Girls means.

Especially useful comparison axes may include:

- Producer ethics;
- adult/performer authority;
- school versus corporate production;
- persona;
- group formation;
- child/adult agency;
- audience;
- public image;
- performance;
- voice;
- failure;
- institutional legitimacy;
- self-authorship.

Comparative analysis is a **reuse layer**, not primary evidence.

---

# 35. Immediate next-step workflow when new episodes arrive

When Episodes 14 onward are uploaded:

### Step 1
Validate the episode bundle structurally.

### Step 2
Do not inspect later bundles beyond the active episode.

### Step 3
Analyze the active episode using Pass A / B / C.

### Step 4
Include performed-vocal-state ledger.

### Step 5
Create/update the canonical episode artifact.

### Step 6
Update:

```text
13_EPISODE_BY_EPISODE_EVIDENCE_LEDGER.md
14_PRIMARY_SOURCE_LOCATOR_AND_CLAIM_REVISION_LEDGER.md
```

### Step 7
Record specialist-document deltas.

### Step 8
State explicitly:

> what this episode changes about the frozen Episode-13 midpoint model.

### Step 9
Proceed to the next episode only after the current one is analytically closed.

---

# 36. Definition of analytical completion

The project is not complete merely when Episode 25 has been summarized.

It is complete when:

- Episodes 1–25 have canonical source-audited readings;
- Episode 26 has separately bounded treatment;
- all major character arcs have traceable evidence;
- New Generations has a complete relational model;
- Producer has a complete developmental model;
- units have distinct final ecologies;
- Cinderella Project has a defensible social/institutional definition;
- performance claims are separated by success axis;
- audience/recognition development is traced;
- major motifs have recurrence evidence;
- Japanese voice has longitudinal evidence;
- performed-vocal states have been synthesized;
- major first-cour hypotheses have been audited;
- external commentary is clearly separated;
- every mature load-bearing claim can route back to original episode evidence;
- specialist documents do not substantially duplicate one another;
- the full-series synthesis reads as an argument rather than an encyclopedia;
- archival validation passes.

---

# 37. Compact execution checklist

For every episode:

```text
[ ] Correct sequential episode only
[ ] No later semantic leakage
[ ] Japanese ASS read
[ ] Complete audio used where relevant
[ ] All contact sheets inspected
[ ] Targeted full-resolution frames inspected
[ ] Pass A completed
[ ] Pass B completed
[ ] Pass C completed
[ ] Performance analyzed if relevant
[ ] Japanese voice updated
[ ] Performed-vocal-state ledger updated
[ ] Character ledgers updated
[ ] New Generations ledger updated if relevant
[ ] Unit/Project ledger updated if relevant
[ ] Producer track updated if relevant
[ ] Production-philosophy ledger updated if relevant
[ ] Four success axes separated where relevant
[ ] Motif entries remain provisional unless recurrence supports more
[ ] Established / Developing / Speculative / Revised classified
[ ] Episode evidence ledger updated
[ ] Primary-source locators backfilled
[ ] Claim revisions recorded
[ ] Cumulative delta stated
```

For the completed mainline:

```text
[ ] Episode 25 prospective endpoint frozen
[ ] Cour 1 synthesis preserved unchanged as E13 artifact
[ ] Major first-half claims adversarially audited
[ ] Motif recurrence audited
[ ] Character arcs audited
[ ] Producer arc audited
[ ] Unit ecologies audited
[ ] Project identity audited
[ ] Institutional analysis audited
[ ] Performance/audience success axes audited
[ ] Japanese voice synthesis completed
[ ] Episode 26 treated separately
[ ] Specialist documents finalized
[ ] Continuous synthesis written afterward
[ ] README written last
[ ] Provenance and duplication audits passed
[ ] Analytical-only delivery package generated
[ ] Checksums locked
```

---

# 38. Final governing rule

If every instruction above is compressed into one rule, retain this:

> **Allow the girls to become who they become at the same speed the anime allows them to become it.**

That means:

- no retrospective Uzuki imposed upon early Uzuki;
- no predetermined Mio arc;
- no franchise-default Rin;
- no automatically saintly Producer;
- no automatically villainous institutional figure;
- no fixed symbolism before recurrence establishes it;
- no success assumed from applause alone;
- no failure assumed from personal distress alone;
- no persona dismissed as fake because it is deliberately made;
- no collective identity presumed to erase individuality;
- no final conclusion allowed to erase the genuine uncertainty that made an earlier episode meaningful.

Episode 1 should first remain what Episode 1 could support.

Episode 13 should remain what the first half could support.

Episode 25 may teach us something new about both.

The finished corpus must preserve the difference.

That difference is not archival bureaucracy.

It is one of the central analytical advantages of the project.
