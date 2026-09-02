---
title: "ようこそ実力至上主義の教室へ / Classroom of the Elite — Multi-Document Synthesis Architecture"
subtitle: "Year-layered corpus design, primary-home rules, superseding ledgers, longitudinal synthesis, and delivery standard"
version: "1.1"
date: "2026-08-11"
amended: "2026-08-25"
amendment_note: "Adds the boundary-specific behavioral reconstruction and simulation protocol layer."
status: "Governing architecture for the Year 1–3 second-pass and eventual full-series synthesis corpus"
project: "Manga and anime discussions"
series: "ようこそ実力至上主義の教室へ / Classroom of the Elite"
source_language: "Japanese"
paired_methods:
  - "COTE_Y1_ANALYTICAL_METHOD_V2.md"
  - "future COTE_Y2_ANALYTICAL_METHOD_V2.md"
  - "future COTE_Y3_ANALYTICAL_METHOD_V2.md"
  - "future COTE_FULL_SERIES_ANALYTICAL_METHOD_V1.md"
current_primary_corpus: "Year 1 complete; Year 2 complete; Volume 0; First File; Second List; Year 3 through Volume 4"
completion_state: "series ongoing; Year 3 provisional"
canonical_prefix: "COTE_"
---

# 『ようこそ実力至上主義の教室へ』
## Multi-Document Synthesis Architecture v1.1
### Year-layered corpus design, primary-home rules, superseding ledgers, longitudinal synthesis, and delivery standard

# 0. Purpose

This file defines the **document architecture** for the next source-grounded synthesis of 『ようこそ実力至上主義の教室へ』 / *Classroom of the Elite* across Years 1, 2, and 3.

It is an architectural companion to the analytical methods used for the sequential second pass.

The distinction is fundamental:

> **The analytical method determines how evidence is read, classified, verified, and interpreted.**
>
> **The architecture determines where each question receives its full treatment, how documents relate across school years, how longitudinal change is preserved, and how duplication is prevented.**

A multi-document structure is necessary not merely because the series is long. It is necessary because *Classroom of the Elite* operates simultaneously at several analytical scales:

- Ayanokōji's first-person psychology and strategic narration;
- Horikita's longitudinal formation as a leader capable of independent judgment;
- friendship, romance, dependency, recognition, and irreplaceability;
- four class cultures whose political constitutions change under pressure;
- special examinations functioning as institutional thought experiments;
- private points, class points, OAA, protection points, tokens, and other systems that translate people into measurable value;
- expulsion as both strategic mechanism and philosophy of disposability;
- the White Room and Advanced Nurturing High School as competing or overlapping models of development;
- student-council politics, administrative power, and national political intervention;
- truth, secrecy, rumor, evidence, reputation, surveillance, and manipulation of the official record;
- ordinary adolescence as a counter-curriculum to institutional optimization;
- Japanese character voice and Ayanokōji's unusually important first-person register;
- Volume 0 as retrospective prehistory encountered late rather than opening exposition;
- official guidebooks that mix factual data, institutional measurement, editorial framing, and new fiction;
- and a series whose major characters and class structures continue to change from year to year.

The architecture must therefore preserve **three distinct forms of truth** at once:

1. **local truth** — what a particular volume establishes at its endpoint;
2. **year-boundary truth** — what the project can responsibly say at the end of a school year;
3. **retrospective full-series truth** — what later evidence eventually confirms, corrects, or recontextualizes.

These must remain connected without being collapsed.

The governing architectural principle is:

> **Separate documents by governing question, not merely by character name, school year, or plot topic.**

A second principle is:

> **Every major subject receives one primary analytical home. Other documents may invoke the same evidence when answering a different question, but should cross-reference rather than reproduce the same deep dive.**

A third principle is:

> **Year-boundary artifacts are immutable historical snapshots. Later documents may supersede them for current-state reference, but they must not erase what the text had established at the earlier boundary.**

A fourth principle is especially important for this series:

> **Development must be distinguished from revelation.**
>
> A character may genuinely change, or the reader may merely learn something that was already true. The final corpus must be able to tell the difference.

A fifth principle is:

> **Class letters are not stable political identities.**
>
> Because classes change rank, leaders, and eventually membership, the architecture must track stable class-polity identifiers separately from the current A/B/C/D designation.

---

# I. Corpus boundary and analytical reading order

## 1. Current primary narrative corpus

The currently available Japanese corpus contains:

### Year 1

- `Y1V01`
- `Y1V02`
- `Y1V03`
- `Y1V04`
- `Y1V04.5`
- `Y1V05`
- `Y1V06`
- `Y1V07`
- `Y1V07.5`
- `Y1V08`
- `Y1V09`
- `Y1V10`
- `Y1V11`
- `Y1V11.5`
- `Y1FF` — Year 1 Official Guidebook — *First File*

### Year 2

- `Y2V01`
- `Y2V02`
- `Y2V03`
- `Y2V04`
- `Y2V04.5`
- `Y2V05`
- `Y2V06`
- `Y2V07`
- `Y2V08`
- `V00` — Volume 0, read in the analytical position specified below
- `Y2V09`
- `Y2V09.5`
- `Y2V10`
- `Y2V11`
- `Y2V12`
- `Y2V12.5`
- `Y2SL` — Year 2 Official Guidebook — *Second List*

### Year 3 — current rolling corpus

- `Y3V01`
- `Y3V02`
- `Y3V03`
- `Y3V04`

Future Year 3 volumes should be appended without changing the stable source-code convention.

## 2. Governing analytical reading order

Unless the user explicitly directs otherwise, use:

1. Year 1 Volumes 1–11.5;
2. *First File*;
3. Year 2 Volumes 1–8;
4. Volume 0;
5. Year 2 Volumes 9–12.5;
6. *Second List*;
7. Year 3 in publication order.

This order is analytically binding because it preserves the series' management of information.

Volume 0 occurs earlier in story chronology but later in analytical chronology. The guidebooks summarize and supplement completed years. Neither should be allowed to flatten the uncertainty through which the preceding books were originally constructed.

## 3. Four temporal coordinates

The full-series corpus should distinguish four temporal fields wherever they diverge:

```yaml
story_chronology: "when the event occurred in-universe"
publication_chronology: "when the material was published"
analytical_reading_position: "when this project encounters the material"
character_knowledge_position: "when the relevant character learns it"
```

This is especially important for:

- Volume 0;
- White Room history;
- Atsuomi Ayanokōji;
- Sakayanagi's childhood knowledge;
- concealed identities and allegiances;
- retrospective explanations of earlier examinations;
- guidebook bonus fiction;
- and any later reveal concerning a character's prior motivation.

## 4. Non-governing material

Unless a later project explicitly expands the scope, the following should not govern novel analysis:

- anime adaptations;
- manga adaptations;
- remembered adaptation dialogue;
- fan wikis;
- secondary plot summaries;
- unverified social-media claims;
- external criticism.

They may be useful in a later adaptation/reception project, but they should remain visibly separate from the Japanese-novel corpus.

---

# II. The architecture has four layers

The complete project should not be understood as one folder containing essays of equal status.

It has four analytical layers.

# Layer A — Immutable per-volume deep readings

Every numbered or decimal volume receives a canonical Markdown artifact created under the governing year method.

Examples:

```text
COTE_Y1_V01_DEEP_READING.md
COTE_Y1_V07_5_DEEP_READING.md
COTE_Y2_V04_5_DEEP_READING.md
COTE_Y2_V12_5_DEEP_READING.md
COTE_Y3_V04_DEEP_READING.md
```

Volume 0 receives:

```text
COTE_V00_RETROSPECTIVE_DEEP_READING.md
```

Guidebooks receive paratext-audit artifacts rather than ordinary volume numbers:

```text
COTE_Y1_FIRST_FILE_PARATEXT_AUDIT.md
COTE_Y2_SECOND_LIST_PARATEXT_AUDIT.md
```

These files are the **canonical scene-level analytical record**.

Their jobs are to preserve:

- volume-local interpretation;
- chapter architecture;
- examination rules;
- character turns;
- relationship changes;
- Japanese voice;
- illustrations;
- ethics;
- evidence classifications;
- source locators;
- and open questions at that precise endpoint.

Once audited, they should not be silently rewritten by later-series conclusions.

# Layer B — Superseding year-boundary snapshots

At the end of each school year, produce:

- a year-specific specialist corpus;
- a full-year synthesis;
- character ledgers;
- relationship and institution ledgers;
- and an explicit handoff to the next year.

These files answer:

> **What can responsibly be said at the end of this year?**

The Year 1 snapshot remains useful after Year 2 because it preserves what changed.

The Year 2 snapshot supersedes it only for **current-state reference**, not historical interpretation.

# Layer C — Longitudinal all-years specialist corpus

After the sequential year-level corpus is sufficiently mature—and definitively after the main series is complete—produce the full-series documents specified later in this architecture.

These answer questions such as:

- what did `実力` come to mean across all years?
- did Horikita become independent of Ayanokōji's authorship?
- did Kei's relationship produce autonomy, deeper dependency, or both?
- how did Ichinose's class constitution change under failure?
- did Ryūen's fear-based rule acquire genuine legitimacy?
- what became of Sakayanagi's aristocratic theory of excellence?
- what is Ayanokōji finally trying to create by moving among classes?
- did ANHS become an alternative to the White Room or another expression of developmental control?
- and can Ayanokōji ultimately accept outcomes he did not design?

# Layer D — Administrative and retrieval artifacts

These include:

- source inventory;
- source checksums;
- artifact checksums;
- corpus manifest;
- machine-readable corpus index;
- locator map;
- longitudinal thread registry;
- class-polity ledger;
- and final delivery audit.

These files do not replace literary analysis. They make the literary analysis recoverable and auditable.

---

# III. Recommended year-level architecture

The year-level corpora should use **parallel document slots whenever possible**. Stable slots improve retrieval and make cross-year comparison straightforward.

The recommended year-level template is:

```text
COTE_YX_00_README_AND_CORPUS_MAP.md
COTE_YX_01_YEAR_ARCHITECTURE_AND_VOLUME_PROGRESSION.md
COTE_YX_02_AYANOKOJI_CHARACTER_PSYCHOLOGY_ETHICS_AND_VOICE.md
COTE_YX_03_HORIKITA_LEADERSHIP_SELF_AUTHORSHIP_AND_CLASS_FORMATION.md
COTE_YX_04_RELATIONSHIPS_DEPENDENCY_FRIENDSHIP_ROMANCE_AND_RECOGNITION.md
COTE_YX_05_CLASS_POLITICS_LEADERSHIP_AND_CONSTITUTIONAL_DEVELOPMENT.md
COTE_YX_06_ABILITY_MERITOCRACY_MEASUREMENT_POINTS_AND_EXAMS.md
COTE_YX_07_INSTITUTIONS_SURVEILLANCE_ADULT_POWER_AND_WHITE_ROOM.md
COTE_YX_08_ETHICS_AUTONOMY_PROTECTION_EXPULSION_AND_VIOLENCE.md
COTE_YX_09_JAPANESE_NARRATION_VOICE_GENRE_HUMOR_AND_VISUAL_PARATEXT.md
COTE_YX_10_RETROSPECTIVE_PARATEXT_AND_REVISION.md
COTE_YX_11_COMPARATIVE_MATRICES_OPEN_QUESTIONS_AND_NEXT_YEAR_HANDOFF.md
COTE_YX_12_VOLUME_BY_VOLUME_EVIDENCE_LEDGER.md
COTE_YX_13_JAPANESE_TERMINOLOGY_AND_PASSAGE_INDEX.md
COTE_YX_FULL_SYNTHESIS.md
```

The slot meaning should remain stable even when emphasis changes.

## Year 1 specializations

`Y1_10` should primarily treat:

- *First File*;
- guidebook institutional legibility;
- ratings;
- official character framing;
- and bonus fiction.

## Year 2 specializations

`Y2_10` should treat:

- Volume 0 as retrospective primary fiction;
- *Second List* as paratext;
- the difference between revelation and development;
- and which Year 1/early-Year-2 interpretations Volume 0 genuinely revises.

Year 2 documents should also expand:

- OAA;
- inter-year politics;
- White Room identity/allegiance problems;
- Nagumo's institutional project;
- class succession and separation;
- and Ayanokōji's transition from target of another person's experiment to designer of other people's developmental environments.

## Year 3 specializations

Year 3 remains incomplete.

Therefore use rolling artifacts such as:

```text
COTE_Y3_PROVISIONAL_SYNTHESIS_THROUGH_V04.md
COTE_CHAR_LEDGER_AYANOKOJI_THROUGH_Y3V04.md
```

rather than falsely final artifacts such as:

```text
COTE_Y3_FULL_SYNTHESIS.md
COTE_CHAR_LEDGER_AYANOKOJI_THROUGH_Y3.md
```

until the year is complete.

Year 3 should add explicit tracking for:

- visible/public versus hidden sovereignty;
- class transfer;
- environmental authorship;
- preference engineering;
- sincere choice under manufactured scarcity;
- separation from prior dependents;
- whether development survives the developer;
- irreplaceability;
- reciprocal authorship;
- and ordinary life as counter-curriculum.

---

# IV. Superseding character-ledger architecture

The series requires longitudinal character ledgers because the meaning of a character at the end of Year 1 may differ substantially from the meaning of the same character after Year 2 or Year 3.

The ledgers should be **structured reference artifacts**, not miniature essays.

## 1. Recommended ledger families

### A. Ayanokōji

```text
COTE_CHAR_LEDGER_AYANOKOJI_THROUGH_Y1.md
COTE_CHAR_LEDGER_AYANOKOJI_THROUGH_Y2.md
COTE_CHAR_LEDGER_AYANOKOJI_THROUGH_Y3V04.md
...
COTE_CHAR_LEDGER_AYANOKOJI_FINAL.md
```

### B. Horikita

```text
COTE_CHAR_LEDGER_HORIKITA_THROUGH_Y1.md
COTE_CHAR_LEDGER_HORIKITA_THROUGH_Y2.md
COTE_CHAR_LEDGER_HORIKITA_THROUGH_Y3V04.md
```

### C. Rival leaders and alternative elite models

Recommended recurring membership:

- Ryūen Kakeru;
- Ichinose Honami;
- Sakayanagi Arisu;
- Kōenji Rokusuke;
- Nagumo Miyabi where relevant;
- later actors who become independent theories of leadership or ability.

Files:

```text
COTE_CHAR_LEDGER_RIVALS_LEADERS_THROUGH_Y1.md
COTE_CHAR_LEDGER_RIVALS_LEADERS_THROUGH_Y2.md
COTE_CHAR_LEDGER_RIVALS_LEADERS_THROUGH_Y3V04.md
```

### D. Relational and class-infrastructure core

Recommended recurring membership:

- Karuizawa Kei;
- Kushida Kikyō;
- Hirata Yōsuke;
- Sudō Ken;
- Shiina Hiyori;
- Kanzaki Ryūji;
- Hashimoto Masayoshi;
- major Ayanokōji Group members;
- and other students whose social function becomes longitudinally important.

```text
COTE_CHAR_LEDGER_CLASS_RELATIONAL_CORE_THROUGH_Y1.md
COTE_CHAR_LEDGER_CLASS_RELATIONAL_CORE_THROUGH_Y2.md
COTE_CHAR_LEDGER_CLASS_RELATIONAL_CORE_THROUGH_Y3V04.md
```

### E. White Room, younger cohorts, seniors, and adults

Recommended contents change by year but should preserve continuity among:

- Amasawa;
- Yagami;
- Nanase;
- Ishigami and later younger students where relevant;
- Manabu;
- Nagumo;
- Chabashira;
- Mashima;
- Hoshinomiya;
- Chairman Sakayanagi;
- Tsukishiro;
- Atsuomi;
- and other adult political actors.

```text
COTE_CHAR_LEDGER_INSTITUTIONAL_ACTORS_THROUGH_Y1.md
COTE_CHAR_LEDGER_INSTITUTIONAL_ACTORS_THROUGH_Y2.md
COTE_CHAR_LEDGER_INSTITUTIONAL_ACTORS_THROUGH_Y3V04.md
```

## 2. Mandatory supersession notice

Every superseding ledger begins with a visible notice:

> **SUPERSESSION NOTICE**
>
> This file supersedes the previous snapshot **for current-state character reference only**. Earlier snapshots remain authoritative for what had been established at their own spoiler boundary and must be preserved for developmental comparison. Do not delete or silently overwrite them.

YAML should include:

```yaml
artifact_type: "character_ledger"
snapshot_boundary: "Y2"
supersedes_current_state:
  - "COTE_CHAR_LEDGER_AYANOKOJI_THROUGH_Y1.md"
historical_predecessor_remains_authoritative: true
```

## 3. Required delta block

Every later snapshot must contain:

## Changes since prior snapshot

with categories:

- `CONFIRMED_CONTINUITY`
- `GENUINE_DEVELOPMENT`
- `REVELATION_OF_PRIOR_HIDDEN_STATE`
- `RETROSPECTIVE_RECONTEXTUALIZATION`
- `CORRECTION_OF_PRIOR_INFERENCE`
- `RELATIONSHIP_SPECIFIC_EXPRESSION`
- `UNRESOLVED_CONTRADICTION`

This protects the corpus from a common failure:

> treating newly revealed information as newly created personality.

---

# V. Required non-character longitudinal ledgers

Character ledgers alone are insufficient because the series' major transformations often occur at the level of institutions and relationships.

## 1. Relationship ledger

```text
COTE_RELATIONSHIP_LEDGER_THROUGH_Y1.md
COTE_RELATIONSHIP_LEDGER_THROUGH_Y2.md
COTE_RELATIONSHIP_LEDGER_THROUGH_Y3V04.md
```

For every major relationship, record:

- start condition;
- information asymmetry;
- leverage;
- dependency;
- protection;
- exit capacity;
- reciprocity;
- emotional disclosure;
- strategic use;
- current trust;
- current fungibility/irreplaceability status;
- and major turning points with volume locators.

Suggested `fungibility_status` values:

- `INTERCHANGEABLE`
- `HIGH_VALUE_BUT_REPLACEABLE`
- `FUNCTIONALLY_IRREPLACEABLE`
- `PERSONALLY_IRREPLACEABLE`
- `UNRESOLVED`

## 2. Institution and examination ledger

```text
COTE_INSTITUTION_EXAM_LEDGER_THROUGH_Y1.md
COTE_INSTITUTION_EXAM_LEDGER_THROUGH_Y2.md
COTE_INSTITUTION_EXAM_LEDGER_THROUGH_Y3V04.md
```

Track:

- special examination;
- formal rules;
- hidden incentives;
- reward and punishment structure;
- what form of ability becomes legible;
- what behavior the mechanism encourages;
- loopholes;
- points/expulsion consequences;
- political effects;
- adult intervention;
- and ethical concerns.

## 3. Class-polity ledger

Because class letters change, use stable political identifiers.

Recommended stable IDs:

```text
POLITY-HORIKITA
POLITY-RYUEN
POLITY-ICHINOSE
POLITY-SAKAYANAGI-ORIGIN
```

The stable ID does **not** imply permanent leadership. It preserves continuity of the student community.

For each volume record:

| Volume | Stable polity | Official class letter | Formal/visible leader | Hidden influence | Major membership change | Constitutional change |
|---|---|---|---|---|---|---|

Recommended file:

```text
COTE_CLASS_POLITY_LEDGER.md
```

This ledger should be updated cumulatively rather than duplicated by year because its main function is to prevent class-letter confusion.

## 4. White Room / identity / allegiance ledger

Year 2 makes apparent identity, sponsor, knowledge, and allegiance difficult to distinguish.

Create:

```text
COTE_ACTOR_IDENTITY_ALLEGIANCE_LEDGER.md
```

Suggested columns:

| Actor | Claimed identity | Observed behavior | Knowledge of White Room | Link to Tsukishiro | Link to Atsuomi | Independent motive | Competing hypothesis | Resolution status |
|---|---|---|---|---|---|---|---|---|

Do not infer White Room origin from exceptional ability or knowledge alone.

## 5. Succession and separation ledger

Create:

```text
COTE_SUCCESSION_SEPARATION_LEDGER.md
```

Track cases where a person, relationship, or institution has become dependent upon a central actor.

Fields:

- central actor;
- structure dependent upon them;
- functions supplied;
- degree of centralization;
- available substitutes;
- departure/separation event;
- survival after departure;
- independent adaptation;
- retrospective assessment.

The governing question is:

> **Does development survive the developer?**

## 6. Longitudinal theme/claim ledger

Create:

```text
COTE_LONGITUDINAL_CLAIM_AND_REVISION_LEDGER.md
```

For every major thesis:

| Claim ID | Claim | First evidence | Stronger evidence | Counterevidence | Later revision | Current status | Primary home |
|---|---|---|---|---|---|---|---|

Examples:

- Ayanokōji sincerely wants ordinary life.
- Ayanokōji understands people primarily through developmental utility.
- Horikita can lead independently of Ayanokōji.
- Kei's dependency decreases over time.
- Ichinose's solidarity is politically sustainable.
- Ryūen's coercive leadership develops voluntary legitimacy.
- Kōenji's autonomy is compatible or incompatible with collective obligation.
- ANHS differs meaningfully from the White Room.
- `実力` cannot be reduced to OAA measurement.
- Ayanokōji becomes capable of treating particular people as personally irreplaceable.

This is the principal bridge between year-level analyses and the final full-series corpus.

---

# VI. Controlled longitudinal thread registry

Important per-volume evidence should optionally carry one or more stable thread IDs.

A compact controlled vocabulary is preferable to hundreds of ad hoc tags.

Recommended initial registry:

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

Thread IDs should appear in YAML or evidence ledgers only when materially relevant.

They are intended to support retrieval such as:

> find every scene across all years relevant to `ENVIRONMENTAL_AUTHORSHIP` or `HORIKITA_INDEPENDENCE`.

---

# VII. Recommended full-series reader-facing corpus

The eventual all-years corpus should be reorganized by **longitudinal governing question**, not merely by school year.

Recommended structure:

```text
COTE_Definitive_Full_Series_Synthesis/
├── 00_README_AND_CORPUS_MAP.md
├── 01_SERIES_ARCHITECTURE_CHRONOLOGY_AND_YEAR_PROGRESSION.md
├── 02_AYANOKOJI_PSYCHOLOGY_FREEDOM_AUTHORSHIP_AND_HUMAN_DEVELOPMENT.md
├── 03_HORIKITA_LEADERSHIP_INDEPENDENCE_AND_CLASS_FORMATION.md
├── 04_RELATIONSHIPS_FRIENDSHIP_ROMANCE_DEPENDENCY_RECOGNITION_AND_IRREPLACEABILITY.md
├── 05_CLASS_LEADERS_RIVALS_AND_COMPETING_THEORIES_OF_ELITE_POWER.md
├── 06_SOCIAL_ENSEMBLE_CLASS_INFRASTRUCTURE_AND_DISTRIBUTED_ABILITY.md
├── 07_CLASS_CONSTITUTIONS_LEADERSHIP_SUCCESSION_TRANSFER_AND_COLLECTIVE_DEVELOPMENT.md
├── 08_ABILITY_JITSURYOKU_OAA_MERITOCRACY_LEGIBILITY_AND_GENERATIVE_CAPACITY.md
├── 09_POINTS_EXAMS_EXPULSION_AND_THE_POLITICAL_ECONOMY_OF_HUMAN_VALUE.md
├── 10_WHITE_ROOM_ANHS_EDUCATION_DEVELOPMENTAL_AUTHORSHIP_AND_ATSUOMI.md
├── 11_STUDENT_COUNCIL_TEACHERS_ADMINISTRATION_AND_NATIONAL_POLITICS.md
├── 12_ETHICS_AUTONOMY_CONSENT_PROTECTION_CONTROL_AND_VIOLENCE.md
├── 13_TRUTH_PROOF_REPUTATION_SURVEILLANCE_AND_THE_AUTHORED_RECORD.md
├── 14_ORDINARY_LIFE_FREEDOM_BODY_LEISURE_AND_COUNTER_CURRICULUM.md
├── 15_JAPANESE_NARRATION_CHARACTER_VOICE_HUMOR_GENRE_AND_VISUAL_PARATEXT.md
├── 16_VOLUME0_GUIDEBOOKS_PREHISTORY_AND_RETROSPECTIVE_REVELATION.md
├── 17_SPECIAL_EXAMINATION_TYPOLOGY_AND_INSTITUTIONAL_DESIGN.md
├── 18_COMPARATIVE_MATRICES_COUNTERARGUMENTS_AND_OPEN_QUESTIONS.md
├── 19_LONGITUDINAL_CLAIM_REVISION_AND_YEAR_DELTA_LEDGER.md
├── 20_VOLUME_ARTIFACT_AND_EVIDENCE_INDEX.md
├── 21_JAPANESE_TERMINOLOGY_DIALOGUE_AND_PASSAGE_INDEX.md
├── COTE_FULL_SERIES_SYNTHESIS.md
├── ledgers/
├── years/
├── volumes/
├── support/
├── CORPUS_MANIFEST.md
├── SOURCE_INVENTORY.md
├── SOURCE_CHECKSUMS.sha256
├── ARTIFACT_CHECKSUMS.sha256
├── CORPUS_INDEX.json
├── DELIVERY_AUDIT.md
├── REFERENCE_COTE_FULL_SERIES_ANALYTICAL_METHOD.md
└── REFERENCE_COTE_MULTI_DOCUMENT_SYNTHESIS_ARCHITECTURE.md
```

The numbered corpus is the **specialist reference layer**.

`COTE_FULL_SERIES_SYNTHESIS.md` is the continuous reader-facing synthesis written only after the specialist documents stabilize.

---

# VIII. Full-series document specifications

# `00_README_AND_CORPUS_MAP.md`
## Corpus guide and executive orientation

### Function

Provide navigation, source boundaries, spoiler state, terminology, and document responsibility.

It should be written **last**, after the specialist documents determine the mature conclusions.

### Required contents

1. Corpus scope and completion state.
2. Publication and analytical reading order.
3. Source hierarchy.
4. Four-temporal-coordinate rule.
5. Local/year/retrospective distinction.
6. Evidence and confidence labels.
7. Naming and romanization conventions.
8. Stable class-polity identifiers.
9. Guidebook/Volume 0 handling.
10. One concise mature series thesis.
11. Full document map.
12. Suggested reading paths:
    - chronological;
    - character-focused;
    - institutional/political;
    - ethical;
    - Japanese-language;
    - comparative.
13. Supersession policy.
14. Retrieval guidance.

### Primary home

- orientation;
- navigation;
- source caveats;
- conventions.

### Do not place here

- full character arguments;
- long exam summaries;
- full White Room history;
- complete ethical theory.

---

# `01_SERIES_ARCHITECTURE_CHRONOLOGY_AND_YEAR_PROGRESSION.md`
## From hidden tests to authored environments

### Governing question

> **How does the series change its central problem as Ayanokōji moves from hidden observer, to covert architect, to increasingly visible political actor—and as the class system itself becomes the object of his experiment?**

### Function

Reconstruct the complete narrative as changing problems rather than one long chain of examinations.

### Required sections

1. Executive architecture thesis.
2. Year 1 movement:
   - discovering the hidden system;
   - integration of fragmented ability;
   - hidden authorship;
   - first institutional corruption;
   - Manabu's departure and Year 1 self-authorship.
3. Year 2 movement:
   - inter-year scale;
   - OAA legibility;
   - White Room infiltration problem;
   - island/unanimity politics;
   - Ayanokōji as developmental designer;
   - succession and deliberate separation.
4. Volume 0 retrospective insertion.
5. Year 3 movement, marked provisional until complete:
   - public sovereignty;
   - class transfer;
   - preference engineering;
   - whether developed systems survive separation;
   - reciprocal authorship.
6. Chronology table for every volume.
7. Main class-point trajectory.
8. Major expulsion/transfer/leadership hinges.
9. Major relationship hinges.
10. Institutional scale expansion:
    - individual;
    - class;
    - year;
    - school;
    - administration;
    - national politics.
11. What changes versus what is merely revealed later.
12. Final architectural synthesis.

### Primary home

- chronological structure;
- year progression;
- changing genre/problem scale.

---

# `02_AYANOKOJI_PSYCHOLOGY_FREEDOM_AUTHORSHIP_AND_HUMAN_DEVELOPMENT.md`
## The masterpiece who becomes an author—and may learn to be authored

### Governing question

> **Can a person whose development was almost entirely authored by others learn to value people without reproducing that authorship over them?**

### Required sections

1. Childhood and White Room formation, preserving Volume 0's retrospective position.
2. Ordinary adolescent voice versus strategic conditioning.
3. Freedom and resistance to ownership.
4. Desire for ordinary school life.
5. Concealment as protection and self-limitation.
6. `tools` doctrine and consequentialist control.
7. Developmental interventions across all years.
8. Protection versus possession.
9. Friendship and low-pressure belonging.
10. Romance, desire, sexuality, attachment, and experimentation.
11. Relation to Horikita.
12. Relation to Kei.
13. Relation to Ichinose.
14. Relation to Hiyori.
15. Relation to Ryūen.
16. Relation to Sakayanagi.
17. Relation to White Room peers/agents.
18. Relation to teachers and adults.
19. Environmental authorship and preference engineering.
20. Generative ability and desire for unpredictable results.
21. Irreplaceability.
22. Reciprocal authorship: people changing Ayanokōji in ways he did not design.
23. Japanese first-person narration and self-interpretation.
24. Ethics.
25. Strongest counterarguments.
26. Final character thesis.

### Primary home

- Ayanokōji's complete psychology;
- philosophy;
- voice;
- development;
- moral trajectory.

### Cross-reference

- relationship mechanics → Document 04;
- class transfer/system design → Document 07;
- White Room history → Document 10;
- normative cases → Document 12.

---

# `03_HORIKITA_LEADERSHIP_INDEPENDENCE_AND_CLASS_FORMATION.md`
## From imitative excellence to autonomous political leadership

### Governing question

> **Can Horikita become a leader whose judgment remains genuinely hers when her development was repeatedly accelerated by someone capable of engineering her environment?**

### Required sections

1. Initial isolation and narrow meritocracy.
2. Manabu imitation and identity construction.
3. Pedagogy and study-group failure.
4. Island/sports-festival/Paper Shuffle leadership development.
5. Kushida as the central rehabilitation gamble.
6. Class Poll and responsibility for sacrifice.
7. Chess and willingness to ask for help.
8. Haircut, Manabu, and self-authorship.
9. Student council and political expansion.
10. Year 2 independent examination design.
11. Relationship to Sudō, Hirata, Kei, Kushida, Kōenji, and the class.
12. Academic competition with Ayanokōji.
13. Leadership after greater public knowledge of his ability.
14. Year 2 end-state and the separation problem.
15. Year 3 class autonomy after transfer.
16. Ability to produce answers Ayanokōji did not specify.
17. Strength and kindness.
18. Japanese voice and register development.
19. Appearance and embodied self-authorship.
20. Ethical strengths and failures.
21. Counterargument: how much of her success remains scaffolded?
22. Final leadership thesis.

### Primary home

- Horikita's psychology;
- Manabu inheritance;
- leadership development;
- independent judgment.

---

# `04_RELATIONSHIPS_FRIENDSHIP_ROMANCE_DEPENDENCY_RECOGNITION_AND_IRREPLACEABILITY.md`
## Can intimacy remain reciprocal inside asymmetric power?

### Governing question

> **What makes a relationship reciprocal in a world where knowledge, protection, points, reputation, emotional vulnerability, and institutional survival can all become leverage?**

### Required relational studies

- Ayanokōji / Kei;
- Ayanokōji / Horikita;
- Ayanokōji / Ichinose;
- Ayanokōji / Hiyori;
- Ayanokōji / Hirata;
- Ayanokōji Group;
- Horikita / Manabu;
- Horikita / Kushida;
- Horikita / Sudō;
- Ryūen / Hiyori / Ishizaki / Ibuki / Albert;
- Ichinose / Kanzaki;
- Sakayanagi / Ayanokōji;
- later relationships materially affecting the same questions.

### Required dimensions

For each major relationship:

- origin;
- information symmetry;
- power symmetry;
- leverage;
- refusal capacity;
- dependency;
- protection;
- strategic utility;
- emotional disclosure;
- ability to contradict;
- reciprocity;
- fungibility/irreplaceability;
- separation;
- capacity to survive a change in role.

### Special distinctions

Do not conflate:

- affection with consent;
- protection with ownership;
- usefulness with intimacy;
- jealousy with love;
- dependence with closeness;
- strategic investment with emotional attachment;
- or sincere choice with fully autonomous choice.

### Primary home

- complete relationship architecture;
- intimacy;
- dependency;
- recognition;
- friendship/romance as longitudinal structures.

---

# `05_CLASS_LEADERS_RIVALS_AND_COMPETING_THEORIES_OF_ELITE_POWER.md`
## Ryūen, Sakayanagi, Ichinose, Kōenji, Nagumo, and alternative answers to `実力`

### Governing question

> **What do the series' major rivals believe exceptional ability entitles a person to do—and what happens when those philosophies become institutions around other people?**

### Principal figures

## Ryūen Kakeru

- fear;
- authoritarian mobilization;
- ownership;
- follower loyalty;
- defeat and reconstruction;
- increasingly trusted authority;
- whether tactical maturation becomes moral maturation.

## Sakayanagi Arisu

- natural genius;
- aristocratic selection;
- White Room observation;
- rivalry;
- worthy contest;
- selective ethics;
- leadership and succession vulnerability.

## Ichinose Honami

- solidaristic leadership;
- no-expulsion constitution;
- guilt and self-worth;
- points as pooled trust;
- Kanzaki's opposition;
- political and romantic conflict;
- later reinvention.

## Kōenji Rokusuke

- radical autonomy;
- extraordinary ability without collective obligation;
- cooperation under coercive institutional conditions;
- value of ungovernable power.

## Nagumo Miyabi

- individual mobility;
- patronage;
- student-council sovereignty;
- transparent ranking versus community of fate;
- relationship to Manabu's legacy.

## Later elite models

Add later figures only when they develop a sufficiently independent philosophy of ability, leadership, or institutional power.

### Primary home

- independent deep dives for major non-Ayanokōji/non-Horikita elite actors;
- their philosophy of ability and authority.

### Cross-reference

- class-wide systems → Document 07;
- relationship with Ayanokōji → Document 04;
- `実力` theory → Document 08.

---

# `06_SOCIAL_ENSEMBLE_CLASS_INFRASTRUCTURE_AND_DISTRIBUTED_ABILITY.md`
## The people who make the classes function

### Governing question

> **Which abilities remain invisible when the story is reduced to mastermind-versus-mastermind competition, and how do ordinary or secondary students create the social infrastructure through which exceptional actors can succeed?**

### Required character groups

- Karuizawa Kei as social network and independent actor;
- Kushida Kikyō as cooperation, information, approval, and threat;
- Hirata Yōsuke as social legitimacy and care;
- Sudō Ken as developmental ability and embodied contribution;
- Shiina Hiyori as perception and moral-strategic mediation;
- Kanzaki Ryūji as loyal opposition;
- Hashimoto Masayoshi as opportunistic information brokerage;
- Keisei, Haruka, Akito, Airi and the Ayanokōji Group;
- Ishizaki, Ibuki, Albert;
- class members whose hidden skills become strategically important;
- Matsushita;
- Yamamura, Morishita, Shiraishi and later socially diagnostic students;
- younger cohorts whose significance is social rather than principally White Room/political.

### Analytical dimensions

- visible versus hidden ability;
- social capital;
- information networks;
- teaching;
- emotional labor;
- practical knowledge;
- friendship-group function;
- dissent;
- ordinary courage;
- class memory;
- and what exceptional leaders fail to see.

### Primary home

- ensemble depth;
- independent supporting-character function;
- distributed and socially usable ability.

---

# `07_CLASS_CONSTITUTIONS_LEADERSHIP_SUCCESSION_TRANSFER_AND_COLLECTIVE_DEVELOPMENT.md`
## The four polities and the shadow constitution

### Governing question

> **How do the four student communities organize unequal people, and can their political cultures survive leader failure, expulsion, transfer, or deliberate separation?**

### Required class studies

Use stable polity IDs rather than letters.

## `POLITY-HORIKITA`

Track:

- fragmented Class D;
- developmental pluralism;
- Horikita/Hirata/Kei/Ayanokōji distribution;
- Kushida crisis;
- Kōenji problem;
- ascent;
- separation from Ayanokōji;
- independent Year 3 survival.

## `POLITY-RYUEN`

Track:

- fear-based centralization;
- ruler defeat;
- voluntary preservation;
- increased trust;
- distributed competence;
- whether the system can survive without Ryūen.

## `POLITY-ICHINOSE`

Track:

- solidarity;
- pooled points;
- no expulsion;
- leader centrality;
- Kanzaki opposition;
- decline/reconstruction;
- whether solidarity becomes resilient or dependent upon one moral center.

## `POLITY-SAKAYANAGI-ORIGIN`

Track:

- aristocratic selection;
- faction destruction;
- leader-centered intelligence;
- Hashimoto/Kamuro/Yamamura dynamics;
- succession after Sakayanagi;
- construction of a new center.

## The shadow constitution: Ayanokōji

Ayanokōji is not initially formal class ruler.

He nonetheless governs:

- information;
- survival;
- development;
- rival preservation;
- reputation;
- and eventually class-level competitive ecology.

Analyze this as **environmental sovereignty** rather than ordinary leadership.

### Required longitudinal questions

- Does development survive the developer?
- Does a class possess a constitution or merely a charismatic leader?
- Can followers contradict leadership without political destruction?
- How is weakness treated?
- Who is considered disposable?
- What happens when class membership changes?

### Primary home

- class political history;
- leadership systems;
- succession;
- transfer;
- collective development.

---

# `08_ABILITY_JITSURYOKU_OAA_MERITOCRACY_LEGIBILITY_AND_GENERATIVE_CAPACITY.md`
## Who controls the meaning of ability?

### Governing question

> **What is `実力` when possessed ability, displayed performance, institutional measurement, social usability, development, political influence, and generative originality diverge?**

### Required taxonomy

Track separately:

1. possessed ability;
2. displayed ability;
3. measured ability;
4. socially usable ability;
5. developmental ability;
6. political ability;
7. generative ability.

### Required topics

- entrance selection;
- early class placement;
- academic ability;
- physical ability;
- social contribution;
- hidden talents;
- OAA;
- deliberate suppression;
- institutional legibility;
- market/recruitment effects of visible scores;
- ability that refuses collective use;
- disability and aggregate scoring;
- development over static ranking;
- natural versus manufactured genius;
- Ayanokōji/Sakayanagi;
- Kōenji;
- Horikita;
- Sudō;
- Kei;
- Kushida;
- Hiyori;
- and later evidence concerning generative unpredictability.

### Required distinction

> **Measurement is an institutional theory of ability, not an omniscient description of the human being.**

### Primary home

- `実力`;
- meritocracy;
- OAA;
- legibility;
- ability taxonomy.

---

# `09_POINTS_EXAMS_EXPULSION_AND_THE_POLITICAL_ECONOMY_OF_HUMAN_VALUE.md`
## When people become numerically exchangeable

### Governing question

> **What happens to human relationships when survival, status, rescue, silence, mobility, and expulsion can be translated into points or examination outcomes?**

### Required topics

- private points;
- class points;
- protection points;
- class transfer prices;
- later tokens/alternative currencies;
- pooling;
- contracts;
- point markets;
- bribery and rescue;
- blackmail;
- buying examination advantage;
- class-point trajectories;
- economic inequality between classes;
- price of refusing sacrifice;
- expulsion;
- forced unanimity;
- leader protection;
- external financing;
- and whether numerical exchange normalizes disposability.

### Required analysis

For every major economic mechanism ask:

- What becomes commensurable?
- Who has liquidity?
- Who controls pooled resources?
- Who can purchase mercy?
- Which relationships become contractual?
- Which values resist translation into points?

### Primary home

- political economy;
- points;
- expulsion as priced institutional outcome.

---

# `10_WHITE_ROOM_ANHS_EDUCATION_DEVELOPMENTAL_AUTHORSHIP_AND_ATSUOMI.md`
## Who has the right to decide what another person should become?

### Governing question

> **Are the White Room and Advanced Nurturing High School genuine alternatives—or different technologies for turning adolescent development into institutional evidence?**

### Required sections

1. White Room political origin.
2. Atsuomi's ambitions.
3. generational structure and epistemic limits.
4. Ayanokōji's fourth generation.
5. failure, casualties, and the language of sampling/masterpiece.
6. White Room education versus ordinary social development.
7. ANHS admission and curated student population.
8. examinations as environmental pedagogy.
9. teacher manipulation.
10. Tsukishiro's administrative intrusion.
11. White Room students/agents and identity-allegiance distinctions.
12. Volume 0 retrospective revision.
13. Ayanokōji reproducing or rejecting White Room methods.
14. Horikita and other students as developmental subjects.
15. consent, refusal, and self-authorship.
16. family, property, and parental jurisdiction.
17. whether ANHS produces freedom or merely adaptive subjects.

### Primary home

- White Room;
- Atsuomi;
- educational theory;
- developmental authorship;
- White Room-linked actors.

---

# `11_STUDENT_COUNCIL_TEACHERS_ADMINISTRATION_AND_NATIONAL_POLITICS.md`
## Formal authority above the class level

### Governing question

> **How does authority change when competition moves from students adapting to rules toward actors capable of designing, suspending, or politically repurposing the rules themselves?**

### Required sections

- Manabu's student council;
- Nagumo's reforms;
- student-council patronage and school-wide power;
- Horikita's council development;
- teachers as former students;
- Chabashira's Class A fixation;
- Hoshinomiya rivalry;
- Mashima's professional ethics;
- Chairman Sakayanagi;
- Tsukishiro;
- school governance;
- external political control;
- Atsuomi and national actors;
- whether the school can maintain institutional autonomy;
- formal versus informal authority.

### Primary home

- student council;
- teachers;
- administration;
- school governance;
- national politics outside detailed White Room pedagogy.

---

# `12_ETHICS_AUTONOMY_CONSENT_PROTECTION_CONTROL_AND_VIOLENCE.md`
## Beneficial outcomes do not settle moral authority

### Governing question

> **When does producing a beneficial outcome cease to justify control over the person whose life is being improved?**

### Required distinctions

- explanation ≠ justification;
- effectiveness ≠ legitimacy;
- sincere choice ≠ fully autonomous choice;
- protection ≠ ownership;
- dependency ≠ love;
- forgiveness ≠ innocence;
- developmental improvement ≠ consent to the method;
- rule compliance ≠ justice;
- survival value ≠ human worth.

### Required cases

At minimum:

- Sudō's disciplinary case;
- Sakura/stalker surveillance and rescue;
- Kei's Volume 4 coercion and rooftop rescue;
- Chabashira's fabricated father threat;
- Ryūen's violence and later poisoning;
- Kushida's confidential truths;
- Ichinose rumor campaign and Ayanokōji's induced fracture;
- Class Poll;
- Nagumo/Tachibana;
- Tsukishiro's interference;
- Year 2 expulsion and forced-choice examinations;
- White Room student operations;
- relationship engineering;
- Year 3 preference engineering and manufactured scarcity.

### Environmental-authorship audit

For major interventions record:

| Intervention | Desired outcome | Information manipulated | Alternatives constrained | Scarcity manufactured | Refusal capacity | Subject sincerely chooses? | Ethical status |
|---|---|---|---|---|---|---|---|

### Primary home

- normative analysis;
- consent;
- coercion;
- protection;
- violence;
- developmental ethics.

---

# `13_TRUTH_PROOF_REPUTATION_SURVEILLANCE_AND_THE_AUTHORED_RECORD.md`
## What happened, what can be proven, and what the institution records

### Governing question

> **Who controls social reality when truth, evidence, credibility, reputation, secrecy, and the official record can diverge?**

### Required topics

- Sudō's case;
- Sakura's testimony;
- cameras and fake cameras;
- Kushida's confidential knowledge;
- Ryūen's real injuries/false causation;
- rumors;
- Ichinose;
- Sakayanagi's one-true-core strategy;
- Ayanokōji's rumor saturation;
- Hashimoto's observation;
- surveillance;
- OAA/publicly visible metrics;
- Tsukishiro's chess falsification;
- hidden identities;
- testimony;
- private recordings;
- strategic framing;
- institutional records.

### Required categories

Always distinguish:

1. event truth;
2. available evidence;
3. credibility;
4. public belief;
5. institutionally enforceable record;
6. retrospective reader knowledge.

### Primary home

- epistemology;
- rumor;
- surveillance;
- reputation;
- authored record.

---

# `14_ORDINARY_LIFE_FREEDOM_BODY_LEISURE_AND_COUNTER_CURRICULUM.md`
## The experiences that matter because nobody assigned their purpose

### Governing question

> **What forms of human development emerge only when an experience is not already organized around ranking, survival, or another person's developmental objective?**

### Required topics

- food;
- shopping;
- birthdays;
- holidays;
- movies;
- pools;
- snow;
- books;
- private phone calls;
- friendship-group leisure;
- gifts;
- romantic dates;
- dormitory privacy;
- appearance and hair;
- bodily embarrassment;
- illness;
- touch;
- sexuality;
- ordinary school attendance;
- graduation;
- future imagination.

### Assigned versus emergent experience

Track whether an experience is:

- institutionally assigned;
- strategically engineered;
- socially invited;
- mutually chosen;
- or spontaneously emergent.

The distinction is especially important for Ayanokōji.

### Primary home

- ordinary life;
- embodied adolescence;
- leisure;
- privacy;
- freedom as lived experience;
- counter-curriculum.

---

# `15_JAPANESE_NARRATION_CHARACTER_VOICE_HUMOR_GENRE_AND_VISUAL_PARATEXT.md`
## How the novels make hidden interiors audible

### Governing question

> **How does the Japanese text use first-person narration, register, address, humor, and visual design to keep public performance and private structure simultaneously visible?**

### Required sections

## Ayanokōji narration

- `オレ`;
- comic internal monologue;
- ordinary adolescent desire;
- strategic declarative mode;
- minimization;
- self-misinterpretation;
- emotional uncertainty;
- later shifts.

## Major voice studies

At minimum:

- Horikita;
- Kei;
- Kushida;
- Hirata;
- Sudō;
- Ryūen;
- Ichinose;
- Sakayanagi;
- Hiyori;
- Kōenji;
- Manabu;
- Nagumo;
- Tsukishiro;
- important Year 2/3 entrants.

## Address-term development

Track:

- family names;
- given names;
- nicknames;
- honorifics;
- private versus public address;
- register changes after relational shifts.

## Humor and genre

- school comedy;
- psychological thriller;
- examination puzzle;
- romance;
- political/institutional fiction;
- White Room conspiracy;
- ordinary-life .5 volumes.

## Visual paratext

- character design;
- posture;
- body language;
- clothing;
- hair;
- distance;
- editorial emphasis;
- guidebook dossier aesthetics.

### Primary home

- Japanese language;
- narration;
- character voice;
- visual/illustrative form;
- formal construction.

---

# `16_VOLUME0_GUIDEBOOKS_PREHISTORY_AND_RETROSPECTIVE_REVELATION.md`
## What later material changes—and what it does not

### Governing question

> **How does retrospective evidence refine the series without erasing the uncertainty through which earlier volumes were originally understood?**

### Required sections

## *First File*

Distinguish:

- factual data;
- institutional measurements;
- editorial framing;
- bonus fiction.

## Volume 0

For every major revelation record:

1. what Volume 0 establishes;
2. what prior volumes allowed the reader to infer;
3. whether Volume 0 confirms, corrects, or recontextualizes;
4. what characters in later chronology actually know.

## *Second List*

Use the same paratext categories as *First File*.

## Future guidebooks/bonus primary fiction

Add later material only after its correct analytical reading position is established.

### Required retrospective table

| Later source | Earlier claim | Earlier best inference | New evidence | Status | Documents affected |
|---|---|---|---|---|---|

### Primary home

- prehistory;
- paratext;
- retrospective revision;
- guidebook epistemology.

---

# `17_SPECIAL_EXAMINATION_TYPOLOGY_AND_INSTITUTIONAL_DESIGN.md`
## The school as laboratory, market, polity, and adversarial game designer

### Governing question

> **What does the school believe students should learn, and how does that belief change as examinations move from hidden incentives toward increasingly explicit political and social engineering?**

### Function

This is not a chronological recap of every examination. It is a comparative typology.

### Required examination categories

Possible categories include:

- hidden-rule/basic institutional socialization;
- truth/credibility;
- scarcity/resource management;
- leader identification;
- asymmetric information;
- betrayal/trust;
- athletic/public performance;
- paired academic dependency;
- conformity and collective responsibility;
- reputation/information warfare;
- compulsory sacrifice;
- indirect command;
- individual market/measurement;
- inter-year competition;
- survival/endurance;
- forced unanimity;
- class mobility;
- tokens/alternative currency;
- ordinary-life observation;
- examinations modified by external political actors.

### Required matrix

For each major examination:

| Exam | Formal mechanism | Hidden incentive | Ability made visible | Strategic exploit | Social effect | Ethical concern | Longitudinal family |
|---|---|---|---|---|---|---|---|

### Longitudinal questions

- Do rules become more transparent?
- Does transparency reduce manipulation or create new markets?
- Does the institution measure students or deliberately transform them?
- When do exams become instruments of adults outside the school?
- How often does institutional design reward the behavior it later condemns?

### Primary home

- comparative examination design;
- institutional pedagogy;
- typology of tests.

---

# `18_COMPARATIVE_MATRICES_COUNTERARGUMENTS_AND_OPEN_QUESTIONS.md`
## Compact reference for future cross-series analysis

### Function

Preserve the full synthesis in reusable structured form.

It must not become a place for new unsupported theses.

### Required matrices

## Character matrix

Axes should include:

- relation to power;
- relation to freedom;
- relation to control;
- relation to truth;
- relation to violence;
- relation to institutions;
- relation to ordinary life;
- relationship style;
- primary virtue;
- characteristic danger;
- capacity for revision;
- final/most-current function.

## Class constitution matrix

- source of authority;
- treatment of weak members;
- decision method;
- information system;
- approach to expulsion;
- ability to distribute leadership;
- succession resilience;
- characteristic failure.

## Ability matrix

- possessed;
- displayed;
- measured;
- usable;
- developmental;
- political;
- generative.

## Relationship matrix

- information symmetry;
- leverage;
- exit capacity;
- reciprocity;
- protection;
- dependency;
- irreplaceability;
- ability to survive disagreement/separation.

## Ethics matrix

- intervention;
- strategic rationale;
- harm;
- consent;
- refusal capacity;
- benefit;
- moral remainder;
- strongest defense;
- strongest criticism.

## Institution matrix

- White Room;
- ANHS;
- student council;
- class polity;
- teacher authority;
- administration;
- national political actors.

### Open questions

Preserve genuine uncertainty rather than forcing closure.

Examples:

- Can Ayanokōji accept a result he did not author?
- Can Horikita's class remain self-sustaining after separation?
- Is Ichinose's eventual political answer genuinely hers?
- Can Ryūen's authority produce independent followers?
- Can Kōenji's autonomy coexist with collective obligation?
- Does ANHS ultimately create freedom or merely more adaptable subjects?
- Is Ayanokōji's recognition of irreplaceability compatible with his willingness to prune others?
- Does he become an educator, ruler, experimenter, ordinary graduate, or some unresolved combination?

### Primary home

- matrices;
- reusable identifiers;
- open questions;
- cross-franchise portability.

---

# `19_LONGITUDINAL_CLAIM_REVISION_AND_YEAR_DELTA_LEDGER.md`
## Required audit layer

### Function

Provide the definitive record of how major interpretations changed across years.

This file is required.

### Required entry format

| Claim ID | Initial formulation | First support | Year 1 status | Year 2 delta | Volume 0 effect | Year 3 delta | Counterevidence | Current status | Primary home |
|---|---|---|---|---|---|---|---|---|---|

### Why it matters

Without this ledger, later insight will tend to rewrite earlier characterization unconsciously.

It is the principal defense against:

- treating revelation as development;
- treating development as proof the earlier self never existed;
- back-projecting Volume 0;
- and turning the final Ayanokōji into the explanation for every early scene.

### Primary home

- interpretive revision history;
- year-to-year delta;
- current claim status.

---

# `20_VOLUME_ARTIFACT_AND_EVIDENCE_INDEX.md`
## Navigation from synthesis claim back to the primary volume analysis

### Function

This is not another prose volume-by-volume synthesis.

The individual volume deep readings already perform that function.

Instead, this file provides a consolidated index:

| Source code | Canonical volume artifact | Volume thesis | Major thread IDs | Key evidence IDs | Major unresolved questions | Later revision links |
|---|---|---|---|---|---|---|

It should also include:

- source filename;
- SHA-256;
- normalized text fingerprint;
- spine map;
- guidebook/Volume 0 classification;
- and relative links to the canonical artifact.

### Primary home

- navigation;
- evidence routing;
- volume-artifact map.

---

# `21_JAPANESE_TERMINOLOGY_DIALOGUE_AND_PASSAGE_INDEX.md`
## Exact-language retrieval layer

### Function

Provide verified Japanese-language access without turning specialist documents into quotation anthologies.

### Required categories

## Ability and evaluation

- 実力;
- 能力;
- 評価;
- 優秀;
- 欠陥/不良品 language where applicable;
- 天才;
- 最高傑作;
- OAA terminology.

## Freedom and control

- 自由;
- 支配;
- 所有;
- 操作;
- 保護;
- 依存;
- 寄生虫;
- 自立;
- 選択.

## Relationship and trust

- 信頼;
- 仲間;
- 友達;
- パートナー;
- 恋人;
- かけがえのない;
- 必要不可欠;
- names and address changes.

## Institutions

- class/exam terminology;
- 退学;
- プロテクトポイント;
- 生徒会;
- White Room vocabulary;
- school-government vocabulary.

## Narration and selfhood

- tool/piece vocabulary;
- education/development metaphors;
- experiment/sample language;
- ordinary-life vocabulary;
- recurring statements concerning winning and losing.

## Passage entries

For each load-bearing passage:

- source code;
- deterministic locator;
- speaker/narrator;
- concise Japanese excerpt only where necessary;
- working translation;
- ambiguity note;
- thread IDs;
- specialist documents using it.

### Primary home

- exact Japanese retrieval;
- voice verification;
- translation-sensitive concepts.

---

# IX. The full-series synthesis

`COTE_FULL_SERIES_SYNTHESIS.md` should be written only after the specialist corpus is substantially complete.

It is not a replacement for the numbered documents.

Its purpose is continuous reading.

It should integrate:

- complete narrative architecture;
- Ayanokōji;
- Horikita;
- the major rival leaders;
- the social ensemble;
- relationships;
- class constitutions;
- `実力`;
- points and expulsion;
- White Room/ANHS;
- institutions;
- ethics;
- truth/record;
- ordinary life;
- Japanese voice;
- retrospective material;
- and the final state of the series' major questions.

Every major synthesis claim should be traceable through:

> `COTE_FULL_SERIES_SYNTHESIS.md`
> → specialist document
> → longitudinal claim/evidence index
> → per-volume artifact
> → evidence ID
> → primary-source locator
> → original Japanese text/illustration.

---

# X. Primary-home and anti-duplication map

The following map is binding for the full-series corpus.

| Subject | Primary home | Permitted elsewhere |
|---|---|---|
| Chronology and year progression | 01 | brief orientation |
| Ayanokōji psychology/philosophy | 02 | relation/class/ethics-specific summaries |
| Horikita psychology/leadership | 03 | relation/class-specific summaries |
| Intimacy, friendship, romance, dependency | 04 | character-specific reference elsewhere |
| Ryūen/Sakayanagi/Ichinose/Kōenji/Nagumo independent philosophies | 05 | class or `実力` summaries elsewhere |
| Supporting ensemble and distributed ability | 06 | concise references in class/exam docs |
| Four class constitutions, succession, transfer | 07 | leader summaries elsewhere |
| `実力`, OAA, meritocracy, generative ability | 08 | exam-specific measurement elsewhere |
| Points, expulsion, political economy | 09 | individual cases elsewhere |
| White Room, Atsuomi, developmental authorship | 10 | adult-politics summary in 11 |
| Student council, teachers, administration, national politics | 11 | actor-specific references elsewhere |
| Ethics, consent, control, violence | 12 | descriptive event summaries elsewhere |
| Truth, proof, rumor, surveillance, record | 13 | case-specific references elsewhere |
| Ordinary life, body, privacy, leisure | 14 | character-specific examples elsewhere |
| Japanese narration, voice, humor, visual form | 15 | concise language notes elsewhere |
| Volume 0 and guidebook retrospective revision | 16 | evidence integrated elsewhere with source labels |
| Examination typology | 17 | individual exam details in volume artifacts |
| Matrices/open questions | 18 | no new unsupported theses |
| Claim revision history | 19 | cited, not duplicated as prose |
| Volume/evidence navigation | 20 | cited throughout |
| Exact Japanese/passages | 21 | short glosses elsewhere |

## 1. Repetition threshold

A non-primary document may normally contain:

- one compact paragraph establishing the relevant background;
- a second paragraph when the evidence changes meaning under that document's question;
- then a relative link to the primary home.

## 2. Repeated evidence is allowed; repeated analysis is not

The same scene may legitimately appear in several documents.

Example: Kei's Volume 4–7 arc.

- Document 02: Ayanokōji's developmental/control logic.
- Document 04: dependency, protection, reciprocity, romance.
- Document 06: Kei as social infrastructure and independent actor.
- Document 12: coercion, retraumatization, consent, responsibility.
- Document 15: public/private voice and naming.

What should not be reproduced is the same multi-page scene summary and identical verdict.

## 3. Required Related Documents block

Every numbered specialist document ends with:

### Related documents

- exact document and topic;
- Document 19 claim/revision entries;
- Document 20 volume evidence routing;
- Document 21 language/passages where applicable.

---

# XI. Cross-reference standard

## 1. Relative Markdown links

Preferred:

```markdown
See [Year 1 ethics synthesis](../02%20Year%201%20Definitive%20Second%20Pass/05%20Year-Level%20Synthesis/COTE_Y1_08_ETHICS_AUTONOMY_PROTECTION_EXPULSION_AND_VIOLENCE.md) for the normative analysis.
```

## 2. Cross-reference by question

Preferred:

> This section concerns Kei's class-political function; the coercive origin of her relationship with Ayanokōji is evaluated in Document 12.

Avoid vague language such as:

> This was discussed elsewhere.

## 3. No circular deferral

Every substantive issue must have one document that actually answers it.

Cross-references must not create a loop of documents each refusing responsibility.

---

# XII. Minimum evidence standard for every full-series specialist document

Documents `01`–`18` should contain:

1. scope statement;
2. executive thesis;
3. governing question;
4. evidence across multiple years where the subject spans multiple years;
5. explicit Year 1/Year 2/Year 3 developmental comparison where relevant;
6. Volume 0 or guidebook source labels when retrospective evidence is used;
7. at least one substantial counterargument;
8. explicit unresolved ambiguity where the text does not settle the issue;
9. evidence from quiet/ordinary scenes, not only climactic examinations;
10. final synthesis that advances beyond the opening thesis;
11. Related Documents block;
12. route to source locators through Documents 19–21 and per-volume artifacts.

Character documents should not be built solely from famous strategic victories.

Institutional documents should include ordinary operation as well as crisis.

Relationship documents should include mundane interaction, not only confessions and betrayals.

Ethical documents should state the strongest defense of actions they criticize.

---

# XIII. Counterargument protocol

Every major specialist document must contain one section titled one of:

- `Strongest counterargument`;
- `Competing interpretation`;
- `What this reading may understate`;
- `Unresolved tension`.

Examples:

## Ayanokōji

> The “developmental authorship” model may overstate control because many of the people around Ayanokōji repeatedly produce decisions he did not predict, obey only selectively, or convert his intervention into outcomes he did not intend.

## Horikita

> Her independence may be overstated if her largest structural successes still depend upon capacities, information, or rival selection that Ayanokōji supplied.

## Ichinose

> Solidaristic politics may be more viable than the competitive system makes it appear; many of her worst defeats occur under adversarial cheating or institutional conditions specifically designed to force sacrifice.

## Ryūen

> Increased follower loyalty may represent genuine legitimacy—or simply a more durable authoritarian system in which attachment intensifies rather than limits centralized power.

## ANHS versus White Room

> Comparing the institutions may exaggerate similarity: ANHS contains peer life, choice, failure recovery, romance, leisure, and voluntary association to degrees fundamentally unavailable in the White Room.

The corpus must answer these arguments rather than merely acknowledge them.

---

# XIV. Production order

Reader order and drafting order should differ.

# Phase 0 — Freeze governing methods and source registry

Before the second-pass corpus expands:

- finalize Year 1 method v2;
- derive Year 2 method v2;
- derive rolling Year 3 method v2;
- establish source codes;
- establish longitudinal thread registry;
- establish class-polity IDs.

# Phase 1 — Complete Year 1 second-pass volume artifacts

Read and emit:

- fourteen volume artifacts;
- *First File* audit;
- Year 1 evidence ledger;
- Year 1 ledgers.

Then draft the Year 1 specialist corpus and synthesis.

# Phase 2 — Migrate Year 2 into the same archival standard

Repeat the process for:

- Year 2 Volumes 1–8;
- Volume 0 in the agreed analytical position;
- Year 2 Volumes 9–12.5;
- *Second List*.

Special requirements:

- Volume 0 retrospective-revision ledger;
- OAA/legibility expansion;
- White Room identity/allegiance ledger;
- succession/separation ledger.

Then draft the Year 2 specialist corpus and synthesis.

# Phase 3 — Year 3 rolling corpus

For each released Year 3 volume:

- emit canonical per-volume artifact;
- update rolling ledgers;
- update provisional Year 3 synthesis only at useful checkpoints;
- do not create final Year 3 or full-series conclusions prematurely.

# Phase 4 — Longitudinal evidence lock after series completion

Before final specialist drafting:

- ensure every volume has canonical artifact;
- lock final year snapshots;
- complete class-polity history;
- complete relationship ledger;
- complete longitudinal claim ledger;
- verify all retrospective revisions;
- audit major Japanese passages.

# Phase 5 — Draft full-series corpus in analytical order

Recommended order:

1. `19_LONGITUDINAL_CLAIM_REVISION_AND_YEAR_DELTA_LEDGER.md`;
2. `20_VOLUME_ARTIFACT_AND_EVIDENCE_INDEX.md`;
3. `01_SERIES_ARCHITECTURE...`;
4. `16_VOLUME0_GUIDEBOOKS...`;
5. `02_AYANOKOJI...`;
6. `03_HORIKITA...`;
7. `04_RELATIONSHIPS...`;
8. `05_CLASS_LEADERS_RIVALS...`;
9. `06_SOCIAL_ENSEMBLE...`;
10. `07_CLASS_CONSTITUTIONS...`;
11. `08_ABILITY...`;
12. `09_POINTS_EXAMS_EXPULSION...`;
13. `10_WHITE_ROOM_ANHS...`;
14. `11_STUDENT_COUNCIL...`;
15. `12_ETHICS...`;
16. `13_TRUTH_PROOF...`;
17. `14_ORDINARY_LIFE...`;
18. `15_JAPANESE_NARRATION...`;
19. `17_SPECIAL_EXAMINATION_TYPOLOGY...`;
20. `18_COMPARATIVE_MATRICES...`;
21. `COTE_FULL_SERIES_SYNTHESIS.md`;
22. `00_README_AND_CORPUS_MAP.md`;
23. finalize `21_JAPANESE_TERMINOLOGY_DIALOGUE_AND_PASSAGE_INDEX.md` from the verified corpus.

The rationale is:

> **revision history first → chronology second → retrospective evidence third → protagonists → relationships and rival systems → class constitutions → ability/economy/institutions → ethics and epistemology → ordinary life and formal language → exam typology → reusable matrices → continuous synthesis → final reader orientation.**

# Phase 6 — Cross-document audit

Check:

- duplicated paragraphs;
- contradictory character claims;
- inconsistent class labels;
- later-knowledge leakage;
- Volume 0 back-projection;
- guidebook ratings treated as omniscient;
- missing evidence locators;
- unsupported romance claims;
- ethical conclusions hidden inside strategic description;
- Ayanokōji flattened into emotional absence;
- ability collapsed into one power-ranking axis;
- social/supporting characters reduced to protagonist functions.

# Phase 7 — Final Japanese verification

Recheck every:

- direct quotation;
- translation-sensitive term;
- pronoun/register claim;
- form-of-address transition;
- examination rule;
- point value;
- chronology-sensitive assertion;
- and disputed motive.

# Phase 8 — Delivery audit

Generate:

- corpus manifest;
- source inventory;
- source checksums;
- artifact checksums;
- corpus JSON index;
- link audit;
- duplicate-text audit;
- UTF-8/front-matter audit;
- clean ZIP package.

Primary copyrighted EPUBs are not redistributed with the analytical corpus.

---

# XV. Searchability and metadata standard

The architecture assumes every Markdown artifact begins with structured YAML.

At minimum:

```yaml
title:
series: "Classroom of the Elite"
artifact_type:
version:
status:
source_boundary:
spoiler_boundary:
analytical_reading_position:
source_codes: []
primary_characters: []
relationships: []
class_polities: []
longitudinal_threads: []
themes: []
locators_verified: true
supersedes_current_state: []
historical_predecessor_remains_authoritative: true
```

## Search aliases

Include common forms in metadata where useful:

- Ayanokōji / 綾小路 / Ayanokoji;
- Horikita / 堀北;
- Kei / 軽井沢恵 / Karuizawa;
- Ichinose / 一之瀬;
- Ryūen / 龍園 / Ryuuen;
- Sakayanagi / 坂柳;
- Kōenji / 高円寺;
- Youjitsu / よう実;
- White Room / ホワイトルーム.

Do not artificially stuff prose with search synonyms.

Metadata and controlled indexes should carry most retrieval redundancy.

---

# XVI. Class-polity naming policy

Do not use a bare class letter as a stable identity in analytical filenames or longitudinal claims.

Bad:

> “Class B believes...”

without a volume anchor.

Better:

> `POLITY-ICHINOSE`, officially Class B in the relevant volume.

This is necessary because:

- class ranks change;
- leadership changes;
- students transfer;
- and later analysis may otherwise attribute the wrong history to a letter rather than a community.

The reader-facing prose may still use the contemporary class letter when it is clearly anchored to time.

---

# XVII. Development-versus-revelation protocol

Every apparent longitudinal change should be classified as one or more of:

- `DEVELOPMENT` — the person actually changes;
- `REVELATION` — the reader learns something previously true;
- `RETROSPECTIVE_REFRAMING` — later evidence changes the meaning of prior evidence;
- `PERFORMANCE_CHANGE` — public presentation changes more than underlying state;
- `RELATIONSHIP_SPECIFIC_EXPRESSION` — a trait becomes visible only with a particular person;
- `UNCERTAIN_MIXTURE`.

Example questions:

- Did Ayanokōji become more emotionally attached, or did the narration become more willing to admit attachment?
- Did Horikita become kinder, or did existing care acquire more socially usable form?
- Did Ryūen become less authoritarian, or did attachment simply become another source of authority?
- Did Kei become less dependent, or did dependency become less visible because the relationship was normalized?

The full-series corpus should avoid declaring one answer without evidence.

---

# XVIII. Environmental-authorship and consent protocol

Year 3 makes this sufficiently important to require an architectural standard.

For any major decision environment created by a powerful actor, especially Ayanokōji, record:

1. desired outcome;
2. information asymmetry;
3. alternatives available before intervention;
4. alternatives removed or made costly;
5. scarcity or urgency manufactured;
6. threats or incentives;
7. emotional leverage;
8. institutional leverage;
9. whether the subject knows the designer's objective;
10. whether the final choice is sincerely preferred;
11. whether the subject can later exit or reverse it;
12. whether the result increases independent agency.

This permits precise distinctions among:

- persuasion;
- bargaining;
- teaching;
- mentoring;
- legitimate command;
- manipulation;
- coercion;
- preference engineering;
- manufactured necessity.

---

# XIX. Ordinary-life counter-curriculum protocol

The full-series architecture should treat ordinary life as a substantive analytical category rather than leftover slice-of-life material.

Track scenes involving:

- food;
- books;
- films;
- phone calls;
- shopping;
- weather;
- travel;
- gifts;
- birthdays;
- dorm rooms;
- clothes;
- hair;
- exercise outside exams;
- sex/romance as lived experience;
- future careers;
- graduation;
- purposeless conversation.

For Ayanokōji especially, ask:

> **Does this experience matter because of what it accomplishes, or because of who is present?**

The answer may provide better evidence of human development than strategic victory does.

---

# XX. Quality-assurance checklist

The final corpus should pass all of the following tests.

## Source and provenance

- [ ] Every volume has a canonical artifact.
- [ ] Every governing EPUB/source has an identity record and checksum.
- [ ] Load-bearing claims have retrievable locators.
- [ ] Guidebook evidence is classified by type.
- [ ] Volume 0 is never silently treated as opening exposition.
- [ ] Adaptation material does not contaminate novel claims.

## Chronology and epistemology

- [ ] Local, year-boundary, and retrospective interpretations are distinguishable.
- [ ] Development is distinguished from revelation.
- [ ] Character knowledge is not confused with reader knowledge.
- [ ] Class letters are time-anchored.
- [ ] Unresolved ambiguity remains marked.

## Character depth

- [ ] Ayanokōji is not reduced to an emotionless mastermind.
- [ ] Ordinary adolescent, relational, and strategic layers remain simultaneously visible.
- [ ] Horikita is treated as an independent developing political subject.
- [ ] Rival leaders receive independent philosophies rather than existing only as Ayanokōji tests.
- [ ] Supporting characters are treated as social infrastructure and independent people.

## Ability and institutions

- [ ] `実力` is not reduced to raw power or OAA score.
- [ ] possessed/displayed/measured/usable/developmental/political/generative ability remain separable.
- [ ] ANHS and White Room similarities do not erase differences.
- [ ] examination mechanics are connected to the behavior they incentivize.

## Relationships and ethics

- [ ] protectiveness is not automatically interpreted as love.
- [ ] genuine affection does not erase coercive origins.
- [ ] successful manipulation is not automatically legitimate.
- [ ] consent includes information, alternatives, and exit capacity.
- [ ] character improvement does not retroactively justify harmful method.
- [ ] dependency and reciprocity are analyzed separately.

## Language and form

- [ ] Japanese voice claims are supported by repeated evidence.
- [ ] forms of address are verified.
- [ ] humor and ordinary life remain visible.
- [ ] illustrations are treated as evidence without overriding prose.

## Architecture

- [ ] every major subject has one primary home.
- [ ] cross-references resolve rather than defer.
- [ ] no specialist document becomes a disguised full-series summary.
- [ ] matrices introduce no new unsupported thesis.
- [ ] older year snapshots remain preserved after supersession.
- [ ] no accidental full-paragraph duplication remains.

---

# XXI. Delivery package and audit standard

The eventual definitive package should contain:

- all numbered specialist documents;
- `COTE_FULL_SERIES_SYNTHESIS.md`;
- year-level packages or relative links to them;
- per-volume canonical artifacts;
- character/relationship/institution ledgers;
- full-series analytical method;
- this architecture document;
- corpus manifest;
- source inventory;
- checksums;
- machine-readable index;
- delivery audit.

## Manifest fields

For every artifact:

- filename;
- artifact type;
- source boundary;
- status;
- word count;
- byte count;
- SHA-256;
- supersession relation;
- primary-home subject;
- relative path.

## Delivery audit should confirm

- all expected documents exist;
- filenames are canonical;
- UTF-8 decoding succeeds;
- YAML front matter is valid;
- internal Markdown links resolve;
- no placeholders remain;
- no chat-wrapper syntax remains;
- no `sandbox:` links remain inside the archival Markdown files;
- no accidental long duplication remains;
- checksums match;
- copyrighted source EPUBs are excluded from the redistribution package.

---

# XXII. Recommended planning scale

The final size should be determined by evidence rather than quota.

For planning purposes, a series of this scale can reasonably support:

- **18–22 substantial full-series specialist documents**;
- approximately **140,000–220,000 words** across the reader-facing specialist corpus;
- a substantial additional body of per-volume analyses and year snapshots;
- 30,000–70,000+ words of ledgers/indexes depending on how much source locator detail is retained.

These are planning ranges only.

Depth produced by repeating plot summaries is not useful depth.

The specialist corpus should become longer only when the governing questions require more evidence.

---

# XXIII. Reader order versus research order

The final reader should encounter:

> README → chronology → protagonists → relationships/rivals/ensemble → class systems → ability/economy → institutions → ethics/epistemology → ordinary life/form → retrospective material → exam typology → matrices → evidence/indexes → full synthesis as an optional continuous reading path.

The researcher should work in almost the opposite direction:

> source audit → volume artifacts → year snapshots → longitudinal ledgers → chronology → retrospective revisions → specialist arguments → matrices → synthesis → README.

This inversion is intentional.

A reader needs orientation first.

An analyst needs evidence first.

---

# XXIV. Final architectural rationale

A weaker *Classroom of the Elite* synthesis could become one enormous Ayanokōji essay with shorter subsections for everyone he manipulates.

This architecture is designed to prevent that failure.

Ayanokōji requires his own document because he is the narrative center and because the series' central problem of developmental authorship is concentrated in him.

Horikita requires her own document because her development tests whether another person can begin inside Ayanokōji's environment and nevertheless become an independent author of political judgment.

Relationships require their own document because friendship, romance, dependency, trust, and irreplaceability cannot be reduced to Ayanokōji's internal state.

The major rival leaders require independent treatment because Ryūen, Sakayanagi, Ichinose, Kōenji, and Nagumo embody competing theories of what exceptional ability authorizes.

The social ensemble requires its own document because the school is not actually run only by masterminds. Information networks, teaching, emotional labor, practical knowledge, friendship, courage, and ordinary reliability repeatedly determine what exceptional actors can accomplish.

The four class polities require their own longitudinal history because a class is more than its current letter or leader. Each develops a political constitution whose survival can be tested by expulsion, failure, transfer, and succession.

`実力` requires a dedicated document because the Japanese title itself makes ability ideological, while the narrative continually separates possessed ability from what institutions can measure or communities can use.

Points and expulsion require their own political-economy document because the school literally gives prices to safety, information, mobility, and survival.

The White Room and ANHS require their own developmental-institution document because the deepest argument of the series concerns who has the authority to determine what another human being should become.

Formal school authority requires a separate political document because student councils, teachers, administrators, and national actors increasingly become capable of altering the game itself rather than merely playing it.

Ethics requires its own normative home because admiration of strategic brilliance can otherwise slide too easily into justification of coercion.

Truth and surveillance require their own epistemic home because the series repeatedly distinguishes what happened, what can be proven, what people believe, and what the institution records.

Ordinary life requires a dedicated home because some of Ayanokōji's most significant development occurs precisely in experiences whose value is not reducible to victory.

Japanese narration and voice require a dedicated home because the protagonist's internal language is one of the strongest pieces of evidence against simplistic readings of him as emotionally blank.

Volume 0 and the guidebooks require a retrospective-revision document because later knowledge should sharpen rather than colonize the earlier books.

Special examinations require a typology because, across dozens of volumes, the tests become a history of the institution's changing theory of human development.

Finally, the claim ledger, evidence index, and Japanese passage index are required because a synthesis this large cannot remain trustworthy if its source trail survives only in conversational memory.

The architecture's governing full-series question is therefore:

> **When a person becomes exceptionally capable of understanding, developing, and controlling other human beings, what would it mean for that person to become genuinely free—and can freedom exist unless the people around him remain capable of producing choices, relationships, institutions, and futures that he did not author?**

That question should remain visible across the corpus without becoming a predetermined answer.

---

# XXV. Behavioral reconstruction and simulation protocol layer

## 1. Architectural status

Behavioral reconstruction is a **downstream operational application layer** of the analytical corpus.

It is not:

- a new source authority;
- a substitute for character ledgers;
- a substitute for relationship ledgers;
- a substitute for Japanese voice analysis;
- a new specialist synthesis slot;
- a license to convert plausible fanfiction into canonical characterization;
- or an excuse to collapse contradictory evidence into one deterministic personality model.

Its purpose is narrower and more demanding:

> **Given a clearly specified novel situation at a frozen analytical boundary, combine the corpus's existing character, relationship, institutional, ethical, ordinary-life, and Japanese-voice evidence into a bounded prediction of what a character is likely to notice, want, infer, do, refuse, conceal, and say.**

The first canonical implementation is:

```text
COTE_BEHAVIORAL_RECONSTRUCTION_PROTOCOL_THROUGH_Y2.md
```

The protocol is boundary-specific because a reconstruction model may be valid at the end of Year 2 and later require revision after Year 3.

Future boundary extensions should use explicit scope:

```text
COTE_BEHAVIORAL_RECONSTRUCTION_PROTOCOL_THROUGH_Y3VXX.md
COTE_BEHAVIORAL_RECONSTRUCTION_PROTOCOL_FINAL.md
```

A later protocol supersedes an earlier one for **current reconstruction practice only**. Earlier protocols remain historical records of what could responsibly be predicted from the evidence available at that boundary.

## 2. Authority rule

The reconstruction protocol may **route, constrain, combine, and rank** canonical evidence.

It may not originate new canonical character facts.

When a reconstruction rule conflicts with a canonical source-local reading, completed-year ledger, or specialist synthesis, the analytical authority wins and the protocol must be revised.

The protocol therefore has the following authority relation:

```text
Japanese primary source
    -> immutable source-local reading
    -> completed-boundary ledgers / specialist synthesis
    -> reconstruction protocol
    -> scenario-specific reconstruction output
```

Scenario outputs are never promoted upward merely because they are coherent or convincing.

## 3. Required reconstruction inputs

A high-confidence reconstruction should retrieve only the inputs relevant to the scenario, but the architecture recognizes the following canonical input families:

1. **character state** — current motives, fears, values, abilities, contradictions, developmental boundary;
2. **relationship state** — information asymmetry, power, dependence, reciprocity, refusal, nonfungibility, counter-authorship;
3. **knowledge state** — what the character actually knows at the frozen boundary and within the scenario;
4. **role / jurisdiction state** — class position, institutional authority, strategic responsibility, social role;
5. **ability / measurement state** — demonstrated capacities, hidden capacities, measurement distortions, withholding;
6. **ethical repertoire** — tools the character has used, rejected, tolerated, regretted, or bounded;
7. **ordinary-life distribution** — low-stakes preferences, hobbies, embarrassment, boredom, domestic routine, ordinary refusal, inefficient desire, horizontal friendship;
8. **stress state** — acute threat, grief, humiliation, loss of control, public exposure, leadership crisis, intimacy pressure;
9. **Japanese written voice** — self-reference, address, politeness, register, lexical/rhetorical habits, state-conditioned deformation;
10. **institutional environment** — rules, incentives, surveillance, scoring, expulsion risk, resource constraints;
11. **source-boundary restrictions** — later evidence that must not leak backward.

The protocol should prefer a small number of causally relevant inputs over indiscriminate retrieval of every document.

## 4. Separation of behavior selection and utterance realization

The architecture requires two distinct stages.

### Stage A — behavioral reconstruction

Determine:

- what the character notices;
- what the character wants;
- what the character fears or protects;
- which constraints matter;
- which actions are available;
- what the character is likely to attempt;
- what the character is likely to withhold;
- and what remains underdetermined.

### Stage B — speech realization

Only after the behavioral state is stable should the model determine:

- whether the character speaks at all;
- public/private/intimate/stress register;
- self-reference and address behavior;
- sentence density;
- directness versus euphemism;
- teasing, humor, threat, apology, or explanation style;
- and the final Japanese or translated utterance.

This prevents verbal tics from driving behavior backward.

A character does not choose an action because the simulator wants to use a catchphrase.

## 5. Epistemic reconstruction classes

Every nontrivial reconstruction should distinguish at least four support states:

### `DEMONSTRATED`

A close canonical analogue exists and the relevant state conditions materially match.

### `STRONG_GENERALIZATION`

Repeated evidence supports a stable behavioral rule across multiple situations, and the present scenario does not activate known counterconditions.

### `BOUNDED_EXTRAPOLATION`

The situation is novel, but multiple independent constraints converge on a limited response family.

### `SPECULATIVE`

The corpus does not strongly determine the response, multiple materially different outcomes remain live, or the scenario depends on unobserved capacities/preferences.

The protocol must never convert `SPECULATIVE` into false precision through arbitrary percentages.

## 6. Underdetermination rule

The reconstruction system should not force one answer when the corpus supports several.

Where two or more responses remain compatible, output a ranked or conditional response set and state the discriminator.

For example:

```text
If the interaction remains private and low-stakes -> response family A is better supported.
If public status or class authority becomes implicated -> response family B becomes more likely.
```

This is preferable to inventing numerical probabilities not grounded in source frequency or a validated model.

## 7. Perspective and model-ownership rule

No character's internal model of another character is automatically canonical truth about the modeled person.

This rule is especially important for Ayanokōji.

His predictions, classifications, developmental plans, and claims of understanding are evidence about:

- his epistemic model;
- his strategic confidence;
- his causal intervention;
- and sometimes the target.

They become stronger evidence about the target only when independently supported by the target's behavior, narration, speech, relationships, or later outcomes.

A reconstruction protocol that simply executes Ayanokōji's model of another person would reproduce one of the series' central epistemic problems rather than analyze it.

## 8. Ordinary-life correction against crisis overfitting

The completed through-Year-2 ordinary-life / counter-curriculum ledger is a required corrective whenever a scenario is not dominated by formal examination, survival, expulsion, or direct strategic conflict.

The protocol must explicitly ask:

> **Would this reconstruction look different if the character were not being selected from their most dramatic scenes?**

This protects against systematic distortions such as:

- Ayanokōji becoming permanently strategic;
- Horikita becoming permanently formal;
- Kei becoming permanently reactive;
- Sudō becoming permanently aggressive;
- Hiyori becoming permanently passive;
- Ryūen becoming permanently domineering;
- Ichinose becoming permanently political;
- Sakayanagi becoming permanently sovereign.

## 9. Relationship-conditioned behavior rule

Global personality is insufficient.

The same person may behave differently with:

- a stranger;
- a peer friend;
- a rival;
- a subordinate;
- a romantic partner;
- an institutional authority;
- an opponent they respect;
- or someone whose refusal matters.

Reconstruction therefore requires the specific dyad or social topology whenever the scenario is relationally meaningful.

Relationship-specific expression must not be promoted into a global trait without evidence.

## 10. Validation and backtesting

The preferred validation method is prospective and boundary-frozen.

Once later primary material is admissible:

1. freeze the reconstruction protocol and relevant ledgers at boundary `B`;
2. hide source material after `B`;
3. specify a diagnostic future situation without outcome leakage;
4. record predicted action families, speech constraints, and uncertainty class;
5. read the later Japanese primary source normally;
6. compare prediction against observed behavior;
7. classify the result.

Recommended result classes:

```text
HIT_CORE_BEHAVIOR
HIT_WITHIN_RESPONSE_FAMILY
UNDERDETERMINED_BUT_COMPATIBLE
MISS_CHARACTER_MODEL
MISS_RELATIONSHIP_MODEL
MISS_KNOWLEDGE_STATE
MISS_CONTEXT_OR_INSTITUTION
GENUINE_LATER_DEVELOPMENT
NEW_REVELATION_OF_PRIOR_STATE
SOURCE_INSUFFICIENT
```

A dedicated validation ledger should be created only after real prospective prediction/observation pairs exist. Do not create an empty validation artifact merely for symmetry.

## 11. Scenario-output status

Scenario reconstructions are derivative artifacts.

Unless the project later establishes a dedicated simulation archive, they should not be treated as canonical corpus members merely because they were generated from canonical inputs.

If retained, they should state:

```yaml
source_boundary: Y2SL
reconstruction_protocol: COTE_BEHAVIORAL_RECONSTRUCTION_PROTOCOL_THROUGH_Y2.md
canon_status: derivative_simulation
not_primary_evidence: true
```

## 12. Retrieval and directory placement

Behavioral reconstruction protocols belong with analytical methods / support infrastructure rather than with character ledgers or specialist syntheses.

The final directory architecture should therefore permit:

```text
methods/
  COTE_BEHAVIORAL_RECONSTRUCTION_PROTOCOL_THROUGH_Y2.md
  future boundary updates
```

This placement encodes the document's responsibility correctly: it governs **how to use** canonical analysis, not **what the canonical character analysis is**.

## 13. Year-2 completion relationship

`COTE_BEHAVIORAL_RECONSTRUCTION_PROTOCOL_THROUGH_Y2.md` is an optional but architecturally recognized operational artifact at the completed Year-2 boundary.

It does not replace the architecture-mandated Year-2 specialist synthesis, full synthesis, evidence/index consolidation, or Year-1 -> Year-2 handoff tracker.

It may be developed before those syntheses are complete because the required ledger substrate now exists, but any later specialist synthesis that materially changes a governing character claim should trigger protocol review before Year-2 archival lock.

## 14. Governing principle

> **Reconstruction should preserve constraint without pretending to determinism.**
>
> A strong model narrows the space of plausible behavior, identifies which responses would violate established characterization, and explains why one response family is better supported than another. It does not claim that a literary person is an algorithm whose next line can always be uniquely solved.

---

# Appendix A — Recommended final directory tree

```text
COTE_Definitive_Full_Series_Synthesis/
│
├── 00_README_AND_CORPUS_MAP.md
├── 01_SERIES_ARCHITECTURE_CHRONOLOGY_AND_YEAR_PROGRESSION.md
├── 02_AYANOKOJI_PSYCHOLOGY_FREEDOM_AUTHORSHIP_AND_HUMAN_DEVELOPMENT.md
├── 03_HORIKITA_LEADERSHIP_INDEPENDENCE_AND_CLASS_FORMATION.md
├── 04_RELATIONSHIPS_FRIENDSHIP_ROMANCE_DEPENDENCY_RECOGNITION_AND_IRREPLACEABILITY.md
├── 05_CLASS_LEADERS_RIVALS_AND_COMPETING_THEORIES_OF_ELITE_POWER.md
├── 06_SOCIAL_ENSEMBLE_CLASS_INFRASTRUCTURE_AND_DISTRIBUTED_ABILITY.md
├── 07_CLASS_CONSTITUTIONS_LEADERSHIP_SUCCESSION_TRANSFER_AND_COLLECTIVE_DEVELOPMENT.md
├── 08_ABILITY_JITSURYOKU_OAA_MERITOCRACY_LEGIBILITY_AND_GENERATIVE_CAPACITY.md
├── 09_POINTS_EXAMS_EXPULSION_AND_THE_POLITICAL_ECONOMY_OF_HUMAN_VALUE.md
├── 10_WHITE_ROOM_ANHS_EDUCATION_DEVELOPMENTAL_AUTHORSHIP_AND_ATSUOMI.md
├── 11_STUDENT_COUNCIL_TEACHERS_ADMINISTRATION_AND_NATIONAL_POLITICS.md
├── 12_ETHICS_AUTONOMY_CONSENT_PROTECTION_CONTROL_AND_VIOLENCE.md
├── 13_TRUTH_PROOF_REPUTATION_SURVEILLANCE_AND_THE_AUTHORED_RECORD.md
├── 14_ORDINARY_LIFE_FREEDOM_BODY_LEISURE_AND_COUNTER_CURRICULUM.md
├── 15_JAPANESE_NARRATION_CHARACTER_VOICE_HUMOR_GENRE_AND_VISUAL_PARATEXT.md
├── 16_VOLUME0_GUIDEBOOKS_PREHISTORY_AND_RETROSPECTIVE_REVELATION.md
├── 17_SPECIAL_EXAMINATION_TYPOLOGY_AND_INSTITUTIONAL_DESIGN.md
├── 18_COMPARATIVE_MATRICES_COUNTERARGUMENTS_AND_OPEN_QUESTIONS.md
├── 19_LONGITUDINAL_CLAIM_REVISION_AND_YEAR_DELTA_LEDGER.md
├── 20_VOLUME_ARTIFACT_AND_EVIDENCE_INDEX.md
├── 21_JAPANESE_TERMINOLOGY_DIALOGUE_AND_PASSAGE_INDEX.md
├── COTE_FULL_SERIES_SYNTHESIS.md
│
├── years/
│   ├── year_1/
│   │   ├── specialist/
│   │   ├── ledgers/
│   │   └── COTE_Y1_FULL_SYNTHESIS.md
│   ├── year_2/
│   │   ├── specialist/
│   │   ├── ledgers/
│   │   └── COTE_Y2_FULL_SYNTHESIS.md
│   └── year_3/
│       ├── specialist/
│       ├── ledgers/
│       └── provisional_or_final_synthesis.md
│
├── volumes/
│   ├── year_1/
│   ├── year_2/
│   ├── volume_0/
│   └── year_3/
│
├── ledgers/
│   ├── COTE_CHAR_LEDGER_AYANOKOJI_FINAL.md
│   ├── COTE_CHAR_LEDGER_HORIKITA_FINAL.md
│   ├── COTE_CHAR_LEDGER_RIVALS_LEADERS_FINAL.md
│   ├── COTE_CHAR_LEDGER_CLASS_RELATIONAL_CORE_FINAL.md
│   ├── COTE_CHAR_LEDGER_INSTITUTIONAL_ACTORS_FINAL.md
│   ├── COTE_RELATIONSHIP_LEDGER_FINAL.md
│   ├── COTE_CLASS_POLITY_LEDGER.md
│   ├── COTE_ACTOR_IDENTITY_ALLEGIANCE_LEDGER.md
│   ├── COTE_SUCCESSION_SEPARATION_LEDGER.md
│   └── COTE_LONGITUDINAL_CLAIM_AND_REVISION_LEDGER.md
│
├── methods/
│   ├── COTE_BEHAVIORAL_RECONSTRUCTION_PROTOCOL_THROUGH_Y2.md
│   └── future_boundary_specific_reconstruction_protocols/
│
├── support/
│   ├── CORPUS_INDEX.json
│   ├── LONGITUDINAL_THREAD_REGISTRY.md
│   ├── LOCATOR_MAP.md
│   └── optional_csv_json_indexes/
│
├── CORPUS_MANIFEST.md
├── SOURCE_INVENTORY.md
├── SOURCE_CHECKSUMS.sha256
├── ARTIFACT_CHECKSUMS.sha256
├── DELIVERY_AUDIT.md
├── REFERENCE_COTE_FULL_SERIES_ANALYTICAL_METHOD.md
└── REFERENCE_COTE_MULTI_DOCUMENT_SYNTHESIS_ARCHITECTURE.md
```

---

# Appendix B — Minimum year-boundary ledger set

At each complete year boundary, preserve at minimum:

```text
COTE_CHAR_LEDGER_AYANOKOJI_THROUGH_YX.md
COTE_CHAR_LEDGER_HORIKITA_THROUGH_YX.md
COTE_CHAR_LEDGER_RIVALS_LEADERS_THROUGH_YX.md
COTE_CHAR_LEDGER_CLASS_RELATIONAL_CORE_THROUGH_YX.md
COTE_CHAR_LEDGER_INSTITUTIONAL_ACTORS_THROUGH_YX.md
COTE_RELATIONSHIP_LEDGER_THROUGH_YX.md
COTE_INSTITUTION_EXAM_LEDGER_THROUGH_YX.md
COTE_THEME_TERMINOLOGY_LEDGER_THROUGH_YX.md
```

For incomplete Year 3, use the exact volume boundary:

```text
...THROUGH_Y3V04.md
```

---

# Appendix C — Success criteria

The architecture has succeeded if a later analyst can answer all of the following without relying on conversational memory:

1. What did Year 1 Volume 4 itself establish about Kei and Ayanokōji?
2. What did the Year 1 synthesis infer from that evidence?
3. What did Year 2 later change about that relationship?
4. Did the relationship itself develop, or did the reader merely gain new information?
5. Which Japanese passages support the current interpretation?
6. Which specialist document owns the ethical judgment?
7. Which class polity was Kei part of at the time, regardless of its letter?
8. What did the school measure, and what ability remained invisible?
9. Which later source retrospectively recontextualized the scene?
10. What remains genuinely unresolved?
11. At a frozen boundary, which canonical artifacts constrain a novel-situation behavioral reconstruction?
12. Which parts of a reconstruction are demonstrated, strongly generalized, bounded extrapolation, or speculative?
13. Has relationship-specific or stress-specific behavior been incorrectly promoted into a global personality rule?
14. Has ordinary-life evidence been consulted when the scenario is low-stakes rather than exam-centered?
15. Can a later source be used to backtest the frozen reconstruction without leaking that later evidence into the prediction?

If those questions can be answered through the artifact chain, the project has become an auditable literary corpus rather than a collection of good but isolated chat analyses.
