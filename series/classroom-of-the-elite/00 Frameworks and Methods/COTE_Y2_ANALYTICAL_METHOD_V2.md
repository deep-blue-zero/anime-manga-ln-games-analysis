---
title: "ようこそ実力至上主義の教室へ / Classroom of the Elite — Year 2 Second-Pass Analytical Method"
subtitle: "Japanese-primary deep-reading, inherited-baseline revision, retrospective prequel control, provenance, and retrieval protocol"
version: "2.0"
date: "2026-08-11"
status: "Governing protocol for the Year 2 second-pass corpus"
project: "Manga and anime discussions"
series: "ようこそ実力至上主義の教室へ / Classroom of the Elite"
analysis_scope: "Year 2 Volumes 1–12.5, Volume 0 in its agreed retrospective position, and Year 2 Official Guidebook — Second List"
source_language: "Japanese"
source_priority: "Original Japanese Year 2 novels and Volume 0 > Second List fiction/data > Year 1 audited corpus > prior Year 2 analysis > later-year material > adaptations/external material"
canonical_prefix: "COTE_Y2_"
parent_method: "COTE_Y1_ANALYTICAL_METHOD_V2.md"
paired_architecture: "COTE_Multi_Document_Synthesis_Architecture_v1.md"
---

# 『ようこそ実力至上主義の教室へ』
## Year 2 Second-Pass Analytical Method v2.0
### Japanese-primary deep reading, inherited-baseline revision, retrospective prequel control, provenance, and Library retrieval protocol

## 0. Status and purpose

This document governs the second analytical pass over **Year 2** of 『ようこそ実力至上主義の教室へ』 / *Classroom of the Elite*.

It is a derived companion to `COTE_Y1_ANALYTICAL_METHOD_V2.md`. The following Year 1 standards remain unchanged unless this document explicitly modifies them:

- Japanese-primary source hierarchy;
- source-byte and normalized-text fingerprinting;
- deterministic EPUB spine/XHTML/paragraph locators;
- illustration locators;
- evidence and claim classification;
- explicit confidence grading;
- local versus retrospective reading;
- correction of prior analysis rather than silent replacement;
- canonical Markdown/YAML output;
- controlled retrieval vocabulary;
- primary-home and anti-duplication rules;
- and traceability from synthesis claim back to the original Japanese source.

Year 2 requires additional controls because it changes the scale of the story. The first year largely asks how students discover, survive, and manipulate an institution whose rules are incompletely visible. The second year increasingly introduces:

- OAA and more explicit institutional legibility;
- first-year entrants and inter-year politics;
- Nagumo's school-wide political project;
- White Room-linked identities, agents, and competing allegiances;
- Tsukishiro's use of administrative power;
- Ayanokōji's increasing authorship of other people's developmental environments;
- class succession and separation;
- and Volume 0, whose story chronology predates the series while its analytical function is retrospective.

The governing traceability rule remains:

> **year synthesis → specialist document → volume artifact → evidence entry → source locator → original Japanese passage or illustration.**

The additional Year 2 governing rule is:

> **Every apparent change must be tested as development, revelation of a prior hidden state, retrospective recontextualization, or some combination of the three.**

---

# I. Core Year 2 theses to test, not assume

The completed first-pass Year 2 synthesis suggested a broad movement from **surviving another person's experiment toward designing one's own**. This is a working hypothesis, not a required conclusion.

Every volume should test at least the following questions.

1. Does Ayanokōji become more autonomous, or does autonomy increasingly take the form of control over other people?
2. When he develops a person, class, or rival, who selected the goal and who is permitted to redefine it?
3. Does Year 2 show actual emotional development in Ayanokōji, or merely reveal capacities and attachments that existed earlier but had not become legible?
4. Does OAA make ability more transparent, or merely create a more sophisticated target for strategic performance?
5. Does greater measurement produce greater fairness?
6. How does inter-year competition change the class as the primary community of fate?
7. What distinguishes a White Room student, a Tsukishiro agent, an Atsuomi-aligned actor, an independently exceptional student, and a student who merely knows unusual information?
8. Does Nagumo's individualist meritocracy liberate strong students from collective failure or replace class dependence with dependence on a central patron?
9. Can Horikita's class develop without Ayanokōji becoming more publicly indispensable?
10. Does Kei's romantic relationship produce greater autonomy, deeper dependency, or both simultaneously?
11. Can Ichinose's solidaristic political constitution survive adversarial pressure without becoming self-destructive?
12. Does Ryūen become ethically better, politically more legitimate, or simply tactically safer?
13. Can Sakayanagi subordinate personal rivalry to institutional responsibility?
14. What happens when a leader, protector, or strategist deliberately withdraws from a structure that has grown around them?
15. Does development survive the developer?

The second pass should actively search for counterevidence to these formulations.

---

# II. Corpus boundary and binding analytical reading order

## 1. Primary Year 2 sequence

Use the following canonical source codes:

1. `Y2V01`
2. `Y2V02`
3. `Y2V03`
4. `Y2V04`
5. `Y2V04.5`
6. `Y2V05`
7. `Y2V06`
8. `Y2V07`
9. `Y2V08`
10. `V00` — Volume 0
11. `Y2V09`
12. `Y2V09.5`
13. `Y2V10`
14. `Y2V11`
15. `Y2V12`
16. `Y2V12.5`
17. `Y2SL` — Year 2 Official Guidebook — *Second List*

The decimal volumes are core narrative material.

## 2. Binding reading position of Volume 0

Volume 0 must be read **after Year 2 Volume 8 and before Year 2 Volume 9** unless the user explicitly requests another analytical experiment.

This rule is not based on in-universe chronology. It preserves the series' publication-era management of information.

Volume 0 therefore receives four temporal coordinates:

```yaml
story_chronology: "pre-ANHS / White Room and political prehistory"
publication_chronology: "later retrospective publication"
analytical_reading_position: "after Y2V08"
character_knowledge_position: "varies by actor and scene"
```

Do not relocate Volume 0 to the beginning merely because its events occur earlier.

## 3. Binding position of *Second List*

`Y2SL` comes after `Y2V12.5`.

Treat it as a retrospective audit of the completed second school year, not as advance reference material.

## 4. Spoiler discipline during the second pass

During a local analysis of `Y2VXX`, do not use:

- later Year 2 volumes;
- Volume 0 before its agreed analytical position;
- *Second List* before `Y2V12.5`;
- Year 3;
- adaptations or external summaries.

Year 1 is inherited background and may be used normally because the characters and reader already possess that history.

---

# III. Source hierarchy

## Tier 1A — Original Japanese Year 2 light novels

Governing evidence for Year 2 narrative, dialogue, narration, examinations, relationships, and institutional facts.

## Tier 1B — Volume 0

Primary fictional evidence, not paratext.

Its special rule is **retrospective position**, not lower authority.

Volume 0 may establish facts about:

- White Room history;
- Atsuomi;
- Ayanokōji's childhood;
- political sponsorship;
- generational design;
- prior relationships;
- and institutional origins.

It must not be used to pretend those facts were already available to readers or characters in earlier volumes.

## Tier 1C — Novel illustrations

Primary visual paratext under the same restrictions as Year 1.

## Tier 1D — *Second List* exclusive fiction

Canonical fictional supplement within its publication position.

## Tier 2A — *Second List* factual data

Strong official reference evidence for explicit biography, chronology, ratings, or school data.

## Tier 2B — *Second List* ratings and measurements

Institutional snapshots, not omniscient truth.

## Tier 2C — *Second List* editorial framing

Useful evidence for official franchise emphasis. Do not allow compressed editorial labels to override richer novel evidence.

## Tier 3 — Audited Year 1 corpus

Year 1 volume artifacts, ledgers, *First File* audit, and Year 1 synthesis are inherited interpretive context.

They do not override the Year 2 Japanese primary text.

## Tier 4 — Prior Year 2 analyses

Use as hypotheses and revision targets.

## Tier 5 — Year 3 and later material

Permitted only in separately labeled retrospective revision fields after the Year 2-local artifact is complete.

---

# IV. Source identity, integrity, and locator protocol

Year 2 inherits the Year 1 protocol without reduction.

For every primary EPUB record:

- canonical source code;
- exact filename;
- byte size;
- SHA-256 of original file;
- EPUB spine order;
- XHTML manifest;
- image inventory;
- normalized text representation when generated;
- normalized-text SHA-256;
- extraction date;
- extraction tool/version if relevant;
- structural anomalies.

Recommended locator:

```text
COTE:Y2V03:spine07:para0142
```

Volume 0:

```text
COTE:V00:spine05:para0088
```

Second List:

```text
COTE:Y2SL:section-character_profiles:para0064
```

Illustrations:

```text
COTE:Y2V05:ill-07
```

Do not invent page numbers when the EPUB does not provide stable print pagination.

---

# V. Evidence and claim classification

Year 2 retains the Year 1 codes:

### Source layers

`LN-TEXT`, `LN-ILL`, `SL-FICTION`, `SL-DATA`, `SL-RATING`, `SL-EDITORIAL`, `PRIOR`, `LATER`.

For Volume 0 use:

`V00-TEXT`, `V00-ILL`.

### Claim types

- `TF` — textual fact
- `CI` — character interior/self-report
- `IR` — institutional rule/record
- `VF` — visual fact
- `SI` — strong inference
- `IT` — interpretive thesis
- `UA` — unresolved ambiguity
- `VJ` — value judgment
- `RC` — retrospective correction
- `RR` — retrospective recontextualization

### Confidence

Use `A`, `B`, `C` or the equivalent confidence system established by Year 1.

Negative evidence must remain explicitly identified as such.

---

# VI. Inherited-baseline and year-delta protocol

Year 2 adds a formal inherited-baseline layer.

Every volume artifact should identify the relevant Year 1 snapshot:

```yaml
prior_snapshot:
  governing_synthesis: "COTE_Y1_FULL_SYNTHESIS.md"
  source_boundary: "end of Y1 / First File"
  inherited_character_ledgers:
    - "COTE_CHAR_LEDGER_AYANOKOJI_THROUGH_Y1.md"
    - "COTE_CHAR_LEDGER_HORIKITA_THROUGH_Y1.md"
```

Every significant Year 2 development should, where relevant, receive one of the following delta labels:

### `CONTINUITY`
The Year 1 characterization remains operative without meaningful change.

### `DEVELOPMENT`
The character, relationship, or institution genuinely changes in Year 2.

### `REVELATION_OF_PRIOR_STATE`
Year 2 newly reveals something that was already true earlier.

### `RETROSPECTIVE_RECONTEXTUALIZATION`
New evidence changes the meaning of earlier evidence without making the earlier reading irrational.

### `CORRECTION`
Primary evidence demonstrates that a prior interpretation was materially wrong.

### `REVERSAL`
A prior trajectory genuinely changes direction.

### `RELATIONSHIP_SPECIFIC_EXPRESSION`
A trait appears differently because of a specific relationship or setting rather than general development.

### `UNRESOLVED`
Evidence does not justify a stable classification.

The required question is:

> **Did the person change, or did our access to the person change?**

---

# VII. Standard per-volume workflow

## Phase 1 — Audit source identity

Verify source file, hash, spine, chapter map, images, and extraction integrity.

## Phase 2 — Read complete volume in spine order

Do not build the analysis from keyword retrieval alone.

## Phase 3 — Create chapter/narrative map

Record:

- viewpoint and temporal changes;
- examinations;
- public and private meetings;
- class transitions;
- relationship scenes;
- institutional interventions;
- unresolved anomalies.

## Phase 4 — Targeted retrieval

Search for:

- names and address-term changes;
- repeated philosophical vocabulary;
- OAA and ability language;
- White Room references;
- student-council and administrative terminology;
- protection/ownership language;
- class-transfer and expulsion terms;
- ordinary-life counterpoints.

## Phase 5 — Audit prior analysis

Classify prior claims as:

`CONFIRMED`, `STRENGTHENED`, `WEAKENED`, `CORRECTED`, `REJECTED`, `NEWLY_FOUND`, `UNRESOLVED`.

## Phase 6 — Build evidence and locator ledgers

No major thesis should depend only on memory of the first pass.

## Phase 7 — Draft canonical artifact

Follow the structure in Section X.

## Phase 8 — Perform local/retrospective separation audit

Especially check that Volume 0 or later-year information has not leaked backward.

## Phase 9 — Update cumulative ledgers

Update the Year 2 working snapshots and longitudinal thread links.

---

# VIII. Canonical filenames

```text
COTE_Y2_V01_DEEP_READING.md
COTE_Y2_V02_DEEP_READING.md
COTE_Y2_V03_DEEP_READING.md
COTE_Y2_V04_DEEP_READING.md
COTE_Y2_V04_5_DEEP_READING.md
COTE_Y2_V05_DEEP_READING.md
COTE_Y2_V06_DEEP_READING.md
COTE_Y2_V07_DEEP_READING.md
COTE_Y2_V08_DEEP_READING.md
COTE_V00_RETROSPECTIVE_DEEP_READING.md
COTE_Y2_V09_DEEP_READING.md
COTE_Y2_V09_5_DEEP_READING.md
COTE_Y2_V10_DEEP_READING.md
COTE_Y2_V11_DEEP_READING.md
COTE_Y2_V12_DEEP_READING.md
COTE_Y2_V12_5_DEEP_READING.md
COTE_Y2_SECOND_LIST_PARATEXT_AUDIT.md
```

Do not rename historical canonical artifacts casually. Searchability depends on stable prefixes.

---

# IX. Standard YAML metadata

Minimum example:

```yaml
---
title: "Classroom of the Elite — Year 2 Volume 3 Deep Reading"
series: "ようこそ実力至上主義の教室へ / Classroom of the Elite"
year: 2
volume: "3"
source_code: "Y2V03"
artifact_type: "volume_deep_reading"
method: "COTE_Y2_ANALYTICAL_METHOD_V2"
method_version: "2.0"
source_language: "Japanese"
spoiler_boundary: "through Y2V03"
source_filename: "...epub"
source_sha256: "..."
normalized_text_sha256: "..."
provenance_status: "verified_primary_source"
prior_snapshot: "end_of_year_1"
local_reading_complete: true
retrospective_annotations_present: false
characters:
  - "綾小路清隆 / Ayanokōji Kiyotaka"
  - "堀北鈴音 / Horikita Suzune"
themes:
  - "実力 / jitsuryoku"
  - "OAA / institutional legibility"
longitudinal_threads:
  - "AYANOKOJI_AUTHORSHIP"
  - "HORIKITA_INDEPENDENCE"
related_artifacts: []
---
```

For Volume 0 add the four temporal coordinates explicitly.

---

# X. Required per-volume analytical structure

Use this as a default, not an inflexible essay template.

1. **Scope, source, provenance, and inherited baseline**
2. **Executive thesis**
3. **Position in Year 2 architecture**
4. **Chapter and narrative architecture**
5. **Examination/institutional mechanism**
6. **Ayanokōji: ordinary, relational, strategic, and authorial layers**
7. **Horikita and class leadership**
8. **New first-year / inter-year characters**
9. **Major returning-character developments**
10. **Relationship architecture**
11. **Class-polity and inter-year politics**
12. **Student council / administration / adult power**
13. **White Room identity and allegiance evidence**
14. **Ability, OAA, legibility, and generative capacity**
15. **Ethics, consent, protection, control, and expulsion**
16. **Japanese narration, voice, and register**
17. **Illustration and embodied characterization**
18. **Motifs, repeated vocabulary, and ordinary-life counterpoints**
19. **Formal/literary strengths**
20. **Critical reservations**
21. **Prior-analysis revision audit**
22. **Inherited Year 1 delta**
23. **Evidence classification ledger**
24. **Primary-source locator ledger**
25. **Cumulative Year 2 delta**
26. **Open questions at this exact endpoint**
27. **Final synthesis**
28. **Related artifacts**

---

# XI. Year 2 Ayanokōji protocol

Continue the Year 1 three-layer distinction:

1. **ordinary adolescent layer**;
2. **relational layer**;
3. **White Room / strategic conditioning layer**.

Add a fourth Year 2 layer:

4. **environmental author / developmental director**.

For every major intervention, ask:

- Did Ayanokōji merely solve the immediate problem?
- Did he intentionally create conditions for another person's later growth?
- Did he choose the person's goal for them?
- Did he preserve refusal?
- Did he allow the person to generate an answer outside his model?
- Did he become more necessary after helping?
- Did he create a successor or a dependent?

Do not infer that becoming more interested in human development is necessarily becoming more humane.

---

# XII. OAA, ability, meritocracy, and legibility protocol

Year 2 expands the ability taxonomy to seven dimensions.

1. **possessed ability** — what the person can potentially do;
2. **displayed ability** — what the person actually reveals;
3. **measured ability** — what institutional categories record;
4. **socially usable ability** — what a group can reliably convert into performance;
5. **developmental ability** — capacity to grow or help others grow;
6. **political ability** — capacity to alter rules, coalitions, incentives, or institutional outcomes;
7. **generative ability** — capacity to produce an answer not already contained in another person's model.

For OAA specifically distinguish:

- measurement accuracy;
- strategic underperformance;
- context dependence;
- disability effects;
- reputation feedback;
- recruitment/targeting consequences;
- market legibility;
- and concealment cost.

The key question is not merely whether a score is correct.

> **What becomes politically possible once a score is visible?**

---

# XIII. White Room identity and allegiance protocol

Year 2 must never infer White Room origin from exceptional ability alone.

Maintain:

`COTE_ACTOR_IDENTITY_ALLEGIANCE_LEDGER.md`

Recommended fields:

| Actor | Public identity | Claimed motive | Observed knowledge | White Room evidence | Tsukishiro link | Atsuomi link | Independent hypothesis | Resolution status |
|---|---|---|---|---|---|---|---|---|

For each candidate or operative distinguish:

- White Room origin;
- White Room knowledge;
- Tsukishiro operational allegiance;
- Atsuomi allegiance;
- personal motive;
- temporary cooperation;
- fabricated identity;
- and unresolved status.

The appearance of privileged information is evidence, not proof of institutional origin.

---

# XIV. Political-scale protocol

Every major operation may be tagged by scale:

```text
individual
relationship
small_group
class
inter_class
year_group
inter_year
student_council
school_wide
administration
white_room
national
```

A single intervention may operate at several scales.

Ask whether an actor controls:

- people;
- information;
- money;
- rules;
- access;
- reputation;
- or the official record.

This prevents class politics from swallowing the increasingly important school-wide and adult political layers.

---

# XV. Class constitutions and the shadow constitution

Continue tracking the four visible class models:

- `POLITY-HORIKITA` — developmental pluralism;
- `POLITY-RYUEN` — authoritarian mobilization and evolving voluntary legitimacy;
- `POLITY-ICHINOSE` — solidaristic institutionalism;
- `POLITY-SAKAYANAGI-ORIGIN` — aristocratic selection.

Add a fifth model:

> **Ayanokōji's shadow constitution — developmental environmental sovereignty.**

He may not hold formal class office, yet he can shape:

- survival;
- incentives;
- leadership trajectories;
- information flows;
- alliances;
- and who remains available for later development.

Track whether this shadow constitution becomes more or less accountable over Year 2.

---

# XVI. Relationship, intimacy, dependency, and consent

Retain the Year 1 relationship dimensions:

- information symmetry;
- leverage;
- exit capacity;
- reciprocity;
- dependency;
- privacy;
- protection;
- ownership;
- ordinary shared life;
- and conflict tolerance.

Add two Year 2 questions:

### Developmental independence

Is the relationship making the other person more able to act without Ayanokōji?

### Disclosure sufficiency

Does the other person possess enough information about Ayanokōji's relevant motives and conduct to make meaningful relational choices?

For romance, do not equate:

- jealousy with love;
- protection with equality;
- sexual attraction with commitment;
- dependency with intimacy;
- or continued relationship with informed consent to its origin.

---

# XVII. Succession and separation protocol

Maintain:

`COTE_SUCCESSION_SEPARATION_LEDGER.md`

Fields:

- central actor;
- dependent structure;
- functions supplied;
- centralization level;
- substitutes;
- planned withdrawal;
- actual departure;
- short-term collapse;
- independent adaptation;
- long-term survival;
- ethical assessment.

The governing question is:

> **Does development survive the developer?**

Apply this not only to Ayanokōji but also to:

- class leaders;
- romantic relationships;
- student-council systems;
- Sakayanagi's class;
- Ryūen's followers;
- Ichinose's class;
- and any institution centralized around one exceptional actor.

---

# XVIII. Volume 0 retrospective-revelation protocol

Volume 0 requires its own artifact and audit layer.

For every load-bearing revelation create:

| Volume 0 fact | Earlier source evidence | Earlier reasonable inference | New status | Development or revelation? | Affected artifact |
|---|---|---|---|---|---|

Use status labels:

- `CONFIRMS`
- `SHARPENS`
- `CORRECTS`
- `RECONTEXTUALIZES`
- `OVERTURNS`
- `ADDS_PREHISTORY_WITHOUT_REVISING`

Volume 0 must not rewrite earlier local artifacts.

Instead, create a separate:

`COTE_RETROSPECTIVE_REVELATION_LEDGER_VOLUME0.md`

and link affected Year 1/early-Year-2 claims to it.

This preserves both:

- historical reading state;
- mature canonical knowledge.

---

# XIX. *Second List* protocol

Audit *Second List* through four categories:

### A. Direct canonical facts

Biographical, institutional, chronological, and explicit data.

### B. Institutional measurement

OAA or other ratings. Treat as observed/constructed measurement, not total personhood.

### C. Official editorial framing

Useful for identifying franchise emphasis but not for overruling novel nuance.

### D. New fiction

Treat as canonical fictional evidence in its publication position.

Required output:

`COTE_Y2_SECOND_LIST_PARATEXT_AUDIT.md`

Include an explicit table of which Year 2 conclusions are:

- confirmed;
- sharpened;
- complicated;
- or left unresolved by the guidebook.

---

# XX. Japanese narration, voice, and address-term protocol

Continue all Year 1 rules.

Pay particular attention to whether increased intimacy or political scale produces changes in:

- first-person self-reference;
- given-name use;
- surnames versus first names;
- honorific reduction;
- politeness shifts;
- private/public speech;
- insult register;
- strategic euphemism;
- Ayanokōji's internal comic register versus cold declarative register.

Voice claims require repeated evidence.

Do not reduce unusual speech to archetype labels without describing actual linguistic features.

---

# XXI. Longitudinal thread registry

Year 2 artifacts should use the stable controlled IDs defined by the architecture, including where relevant:

```text
AYANOKOJI_FREEDOM
AYANOKOJI_AUTHORSHIP
AYANOKOJI_ORDINARY_LIFE
AYANOKOJI_NARRATION
AYANOKOJI_IRREPLACEABILITY
HORIKITA_INDEPENDENCE
HORIKITA_LEADERSHIP
KEI_DEPENDENCY_AUTONOMY
ICHINOSE_SOLIDARITY
ICHINOSE_SELF_WORTH
RYUEN_FEAR_LEGITIMACY
SAKAYANAGI_RIVALRY_GENIUS
KUSHIDA_INTEGRATION
HIRATA_CARE_LEADERSHIP
SUDO_DEVELOPMENT
HIYORI_QUIET_AGENCY
KOENJI_AUTONOMY
JITSURYOKU
OAA_LEGIBILITY
GENERATIVE_ABILITY
CLASS_CONSTITUTIONS
POINTS_POLITICAL_ECONOMY
EXPULSION_DISPOSABILITY
WHITE_ROOM
ANHS_EXPERIMENT
ENVIRONMENTAL_AUTHORSHIP
RELATIONSHIP_RECIPROCITY
PROTECTION_OWNERSHIP
TRUTH_PROOF_RECORD
SURVEILLANCE
STUDENT_COUNCIL
NATIONAL_POLITICS
SUCCESSION_SEPARATION
ORDINARY_LIFE_COUNTER_CURRICULUM
```

Use only materially relevant threads.

---

# XXII. Year 2 cumulative ledgers and supersession

Recommended Year 2 snapshots:

```text
COTE_CHAR_LEDGER_AYANOKOJI_THROUGH_Y2.md
COTE_CHAR_LEDGER_HORIKITA_THROUGH_Y2.md
COTE_CHAR_LEDGER_CLASS_CORE_THROUGH_Y2.md
COTE_CHAR_LEDGER_RIVALS_LEADERS_THROUGH_Y2.md
COTE_CHAR_LEDGER_WHITE_ROOM_ADULTS_THROUGH_Y2.md
COTE_RELATIONSHIP_LEDGER_THROUGH_Y2.md
COTE_INSTITUTION_EXAM_LEDGER_THROUGH_Y2.md
COTE_THEME_TERMINOLOGY_LEDGER_THROUGH_Y2.md
COTE_CLASS_POLITY_LEDGER_THROUGH_Y2.md
COTE_ACTOR_IDENTITY_ALLEGIANCE_LEDGER_THROUGH_Y2.md
COTE_SUCCESSION_SEPARATION_LEDGER_THROUGH_Y2.md
```

Each must include:

> **SUPERSESSION NOTICE — This Year 2 snapshot supersedes the corresponding Year 1 ledger for current-state reference only. The Year 1 artifact remains authoritative for what had been established at the Year 1 boundary.**

Every ledger must contain a **Changes since Year 1** section using the delta categories in Section VI.

---

# XXIII. Searchability and Library retrieval

Use stable prefixes:

- `COTE_Y2_`
- `COTE_V00_`
- `COTE_CHAR_LEDGER_`
- `COTE_RELATIONSHIP_LEDGER_`
- `COTE_CLASS_POLITY_`

Every artifact should include:

- Japanese and romanized character names;
- source code;
- volume number;
- canonical title;
- major examination name;
- longitudinal thread IDs;
- major relationship names;
- key Japanese terminology;
- concise retrieval-oriented abstract near the top.

Do not create idiosyncratic abbreviations that are unlikely to be searched later.

---

# XXIV. Recommended Year 2 specialist corpus

Use the parallel architecture defined by `COTE_Multi_Document_Synthesis_Architecture_v1.md`:

```text
COTE_Y2_00_README_AND_CORPUS_MAP.md
COTE_Y2_01_YEAR_ARCHITECTURE_AND_VOLUME_PROGRESSION.md
COTE_Y2_02_AYANOKOJI_CHARACTER_PSYCHOLOGY_ETHICS_AND_VOICE.md
COTE_Y2_03_HORIKITA_LEADERSHIP_SELF_AUTHORSHIP_AND_CLASS_FORMATION.md
COTE_Y2_04_RELATIONSHIPS_DEPENDENCY_FRIENDSHIP_ROMANCE_AND_RECOGNITION.md
COTE_Y2_05_CLASS_POLITICS_LEADERSHIP_AND_CONSTITUTIONAL_DEVELOPMENT.md
COTE_Y2_06_ABILITY_MERITOCRACY_MEASUREMENT_POINTS_AND_EXAMS.md
COTE_Y2_07_INSTITUTIONS_SURVEILLANCE_ADULT_POWER_AND_WHITE_ROOM.md
COTE_Y2_08_ETHICS_AUTONOMY_PROTECTION_EXPULSION_AND_VIOLENCE.md
COTE_Y2_09_JAPANESE_NARRATION_VOICE_GENRE_HUMOR_AND_VISUAL_PARATEXT.md
COTE_Y2_10_RETROSPECTIVE_PARATEXT_AND_REVISION.md
COTE_Y2_11_COMPARATIVE_MATRICES_OPEN_QUESTIONS_AND_NEXT_YEAR_HANDOFF.md
COTE_Y2_12_VOLUME_BY_VOLUME_EVIDENCE_LEDGER.md
COTE_Y2_13_JAPANESE_TERMINOLOGY_AND_PASSAGE_INDEX.md
COTE_Y2_FULL_SYNTHESIS.md
```

`Y2_10` has a special Year 2 function: **Volume 0 + Second List + revelation/development audit**.

---

# XXV. Production order

## Phase 0 — Corpus audit

Verify all Year 2 EPUBs, Volume 0, and *Second List*.

## Phase 1 — Sequential reread through Y2V08

Produce immutable per-volume artifacts.

## Phase 2 — Volume 0

Produce `COTE_V00_RETROSPECTIVE_DEEP_READING.md` and the retrospective-revelation ledger.

## Phase 3 — Continue Y2V09 through Y2V12.5

Volume 0 may now inform reader-level interpretation, but continue separating what each character knows.

## Phase 4 — *Second List*

Produce paratext audit.

## Phase 5 — Lock Year 2 ledgers

Complete superseding character, relationship, institution, polity, identity/allegiance, and succession snapshots.

## Phase 6 — Draft Year 2 specialist documents

Evidence-first order is preferred:

1. volume evidence ledger;
2. chronology/year progression;
3. Volume 0/paratext/revision;
4. character and relationship documents;
5. class/institution/ability/ethics documents;
6. Japanese-language index;
7. comparative matrices;
8. full synthesis;
9. README last.

## Phase 7 — Cross-document audit

Check duplication, citations, locator validity, spoiler boundaries, and supersession notices.

## Phase 8 — Delivery package

Include manifest, source checksums, artifact checksums, corpus index, method, architecture reference, and delivery audit. Do not redistribute copyrighted source EPUBs.

---

# XXVI. Quality-assurance checklist

Before finalizing any Year 2 artifact verify:

### Source
- primary Japanese EPUB read completely;
- source hash recorded;
- locators deterministic;
- no invented pagination.

### Epistemic discipline
- no later Year 2 leakage;
- no Volume 0 leakage before Y2V08;
- no Year 3 leakage into local reading;
- development distinguished from revelation.

### Character analysis
- Ayanokōji not flattened into emotionlessness;
- ordinary, relational, strategic, and authorial layers separated;
- new students not reduced immediately to White Room candidates;
- characters treated as people and political actors before functional labels.

### Ability
- OAA not treated as omniscient truth;
- measured ability separated from possessed and socially usable ability;
- generative ability considered where relevant.

### Ethics
- beneficial outcomes not treated as proof of legitimate authority;
- consent, leverage, exit, and disclosure examined;
- protection distinguished from ownership.

### Revision
- prior Year 2 claims explicitly audited;
- inherited Year 1 claims explicitly delta-classified;
- Volume 0 retrospective changes linked rather than silently backfilled.

### Retrieval
- canonical filename;
- YAML valid;
- Japanese and romanized names present;
- longitudinal threads controlled;
- related artifacts linked.

---

# XXVII. Governing Year 2 question

The Year 2 second pass should remain open to multiple answers, but its most productive governing question is:

> **What happens when a person who escaped being another institution's curriculum becomes capable of designing the environments in which other people develop—and can that new authorship remain compatible with the freedom he originally sought for himself?**

The method should not presume that Year 2 answers this question positively or negatively. Its purpose is to produce enough source-grounded evidence that the later all-years synthesis can answer it responsibly.
