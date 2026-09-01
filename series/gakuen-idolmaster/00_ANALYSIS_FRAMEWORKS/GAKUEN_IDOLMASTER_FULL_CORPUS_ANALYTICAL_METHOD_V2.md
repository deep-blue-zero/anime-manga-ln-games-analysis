---
title: "Gakuen Idolmaster Full-Corpus Analytical Method V2"
project: "Gakuen Idolmaster / 学園アイドルマスター"
document_type: "governing analytical protocol"
version: "2.2"
status: "canonical working method"
last_updated: "2026-08-14"
revision_note: "adds validated public-commu nomenclature, search-term construction, whole-video acquisition, and grouped AV retrieval packets"
source_lock: "GAKUMAS V2 Source Lock 1.0"
source_snapshot_date: "2026-08-02"
source_commit: "00d150a069a3ffa723a1ff264752ba242024caad"
source_revision: "32"
corpus_files: 3777
extracted_dialogue_lines: 93924
language_of_primary_evidence: "Japanese"
created: "2026-08-13"
---

# GAKUEN IDOLMASTER FULL-CORPUS ANALYTICAL METHOD V2

## 0. Purpose and governing principle

This document defines the canonical method for the second-pass, full-corpus analysis of **学園アイドルマスター / Gakuen Idolmaster** (hereafter **Gakumas**). It is designed for a live-service, character-centered narrative game whose characterization and thematic argument are distributed across branching Produce Stories, Dear Idol material, idol communications, event stories, support-card stories, unit stories, system/world-exposition scenes, voice performance, image songs, music videos, background music, and other audiovisual materials.

The project does **not** assume that Gakumas can be read as a single linear novel. Its governing task is to reconstruct, as rigorously as the source permits:

1. what the game actually contains;
2. which story states and branches can legitimately be related to one another;
3. what stable and conditional claims can be made about characters and relationships;
4. how Hatsuboshi Academy and the wider idol-production system structure development;
5. what themes emerge from the complete corpus rather than from selective quotation;
6. how language, voice acting, singing, composition, arrangement, choreography, camera, staging, and audiovisual performance contribute to characterization;
7. how prior Gakumas analyses should be confirmed, narrowed, revised, rejected, or left unresolved after systematic rereading.

The method is deliberately conservative about claims of chronology, canon, psychology, symbolism, and thematic design. It rewards **traceability over elegance**, **counterevidence over confirmation bias**, and **specificity over generalization**.

The intended evidentiary chain is:

> **raw primary source -> canonical source identity -> story-state classification -> source-facing reading -> cumulative ledger -> character/relationship synthesis -> thematic/institutional synthesis -> adversarial audit -> final series synthesis**

A conclusion is strongest when a reader can move backward through that chain to the exact Japanese source and, where relevant, the inspected audiovisual evidence.

---

# 1. Corpus definition and source lock

## 1.1 Frozen textual corpus

The initial V2 source lock is the archived Gakumas ADV corpus generated on **2026-08-02**, tied to upstream source commit:

`00d150a069a3ffa723a1ff264752ba242024caad`

with source revision value:

`32`

The archive contains:

- **3,777 source transcript files**;
- **93,924 extracted dialogue message lines**;
- raw ADV scripts;
- dialogue-only mirrors where message extraction is possible;
- analysis-friendly bundles;
- manifests, category counts, provenance records, and validation reports.

This corpus is formally designated:

> **GAKUMAS V2 SOURCE LOCK 1.0**

All definitive claims in the initial V2 synthesis refer to this source state unless explicitly labeled as later material.

## 1.2 Live-service versioning

Gakumas is an evolving live-service work. The project therefore treats source completeness as **versioned**, not absolute.

Later additions should be incorporated using explicit source-lock updates, for example:

- `SOURCE_LOCK_1.0` — frozen 2026-08-02 textual corpus;
- `SOURCE_LOCK_1.1` — minor post-lock additions;
- `SOURCE_LOCK_2.0` — substantial new story era or major ingestion rebuild.

A later update should not silently rewrite the evidentiary basis of older documents. Instead it should record:

- new source identity;
- date and provenance;
- affected characters/relationships/themes;
- claims strengthened, weakened, or overturned;
- documents requiring revision.

## 1.3 Scope claim

The finished V2 project may accurately describe itself as:

> **a source-grounded literary, character, relational, linguistic, and selectively audiovisual analysis of the frozen Gakuen Idolmaster corpus**.

It must **not** claim exhaustive audiovisual coverage of the entire multimedia franchise unless that material is separately ingested and audited.

---

# 2. Source hierarchy: authority and function

Two independent hierarchies are required. One concerns **textual authority**; the other concerns **narrative function**. They must not be conflated.

## 2.1 Textual authority hierarchy

### A1 — Raw Japanese ADV scripts

Directory role:

`transcripts_raw/`

These are the governing textual primary sources for:

- exact Japanese wording;
- ruby/furigana markup;
- line breaks where meaningful;
- speaker labels;
- voice asset IDs;
- BGM cues;
- camera settings;
- actor layout;
- motion/facial-motion instructions;
- background settings;
- timing;
- route labels and internal filenames.

If a derived representation conflicts with raw ADV, **raw ADV governs**.

### A2 — Dialogue-only transcript layer

Directory role:

`transcripts_dialogue_only/`

Use for:

- fast reading;
- phrase search;
- speaker-oriented retrieval;
- linguistic analysis where staging is not in question.

It is a convenience layer, not the final authority. If punctuation, markup, speaker attribution, omission, or staging matters, return to A1.

### A3 — Analysis bundles

Directory role:

`analysis_bundles/`

This is the **primary ingestion and reading layer** because it groups material into usable analytical units and preserves source envelopes/locators.

It may contain overlapping views of the same source. Therefore bundled occurrences must never be treated as separate evidence objects without deduplication.

### A4 — External official metadata

Examples:

- official Gakumas site;
- official YouTube channels;
- official music-release pages;
- Bandai Namco / ASOBINOTES / related official publishing metadata.

Use for:

- song titles;
- performer attribution;
- release chronology;
- credits;
- official video identification;
- public-facing nomenclature.

This is primary or near-primary metadata, but not a substitute for inspecting requested raw audiovisual evidence.

### A5 — Reliable indexing/reference sources

Example:

- Project-imas.

Use as a **discovery and crosswalk layer** for:

- song catalogs;
- image-song associations;
- credits;
- release relationships;
- alternate romanizations;
- live or CD associations;
- identifying likely official videos.

Do not allow a fan/reference index to override official metadata or raw evidence where they conflict.

### A6 — Legacy Gakumas analyses and prior chats

Prior deep dives, transcripts, relationship essays, and thematic syntheses are **historical analytical hypotheses**, not evidence.

They are preserved because they can reveal:

- earlier intuitions;
- useful candidate themes;
- prior blind spots;
- interpretive drift;
- claims worth testing.

They must remain capable of being disproved.

## 2.1.1 External evidence extension: S1-S5

The frozen ADV hierarchy above remains the governing textual hierarchy, but the project also uses a second source-class vocabulary for **paratext and external evidence**. This extension exists because dramatic scripts should not be forced to carry formal taxonomy, production history, or creator-stated design rationale that they have no reason to exposit.

| class | source type | proper use | prohibition |
| --- | --- | --- | --- |
| `S1` | narrative primary source | enacted story reality, dialogue, behavior, relationships, institutional practice, track chronology | never overridden by interview intent |
| `S2` | official canonical paratext | formal names, profiles, course/institution terminology, first-party setting metadata | do not turn promotional shorthand into unstated narrative consequences |
| `S3` | credited creator/staff commentary | production history, rejected concepts, design rationale, intended distance or theme | do not silently convert intention into in-world fact |
| `S4` | reliable external secondary source | reporting, preservation, historical/industry context | trace high-load claims upstream when possible |
| `S5` | fan reference/discovery source | search, cataloging, terminology discovery, crosswalks | never use as final authority where S1-S4 are available |

Mapping to the older A-hierarchy is contextual rather than one-to-one: A1-A3 are `S1`; A4 setting metadata is normally `S2`; A4 creator interviews are `S3`; A5 is normally `S5` unless the particular source qualifies as edited secondary reporting (`S4`). A6 remains historical analysis rather than evidence.

Every externally informed analytical proposition should also carry a **claim type**:

- `A` — TEXTUAL FACT (`S1`)
- `B` — OFFICIAL SETTING FACT (`S2`)
- `C` — CREATOR-STATED RATIONALE (`S3`)
- `D` — SECONDARY-SOURCE REPORT (`S4`)
- `E` — ANALYTICAL INFERENCE
- `F` — OPEN / UNRESOLVED

Source class and claim type answer different questions. `S3/C` can strongly establish why a design choice was made while remaining incapable of proving how every scene must be interpreted.

### Governing conflict rule

For enacted narrative reality, `S1` governs. If an interview states an intention that the game contradicts, record the tension rather than repairing the game toward the interview. For formal terminology not naturally exposited in dialogue, `S2` may fill the gap. `S3` may explain design rationale but never erase textual ambiguity.

### External-source register

Durable S2-S5 claims must be entered in `GKM_OFFICIAL_PARATEXT_AND_CREATOR_COMMENTARY_REGISTER.md` with title, publisher/host, author/speaker where known, publication date, URL, access date, exact bounded proposition, source class, claim type, and affected artifacts.

---

## 2.2 Narrative-function hierarchy

Narrative function describes what a source is useful for. It does **not** rank its authenticity.

### SPINE

Material that establishes major progression, world rules, or explicit longitudinal transitions.

Examples:

- Produce Story main progression;
- shared world-explanation scenes;
- unit story where it anchors ensemble chronology;
- N.I.A. and H.I.F. structural material.

### CHAR-CORE

Material centrally concerned with a character's internal development or Producer relationship.

Examples:

- Dear Idol;
- character communications;
- major character-route material.

### ENSEMBLE

Material designed around multiple characters, class dynamics, units, school culture, events, or collective conflict.

Examples:

- numbered story events;
- unit stories.

### RELATIONAL

Material especially valuable for recurring interpersonal behavior, ordinary-life interaction, or pair/group dynamics.

Examples:

- support-card stories;
- cross-character communications;
- routine peer interactions.

### TEXTURE

Material that enriches everyday practice, tone, habits, professional work, seasonal rhythms, performance context, or social ecology.

Examples:

- selected Produce Events;
- seasonal/startup scenes;
- live-related dialogue;
- low-stakes daily interactions.

### SYSTEM

Material mostly concerned with gameplay mechanics, result states, growth loops, or low-dialogue infrastructure.

Examples:

- many pstep/pweek/growth/result scripts;
- non-dialogue gacha or system sequences.

SYSTEM material should not be ignored automatically. It may contain worldbuilding or institutional information. It simply receives lower default interpretive priority until evidence shows otherwise.

---

# 3. Canonical source identity and deduplication

## 3.1 Evidence objects are scripts, not bundle appearances

The same original script may appear in more than one analysis bundle. Therefore evidence frequency must never be calculated by counting bundle appearances.

The default canonical source identity is:

> `original_name + sorted_relative_path`

where available.

If those are insufficient, use a stable fallback combining:

- corpus category;
- original filename;
- source path;
- checksum when generated.

## 3.2 Required dedup ledger

Maintain:

`GKM_SOURCE_IDENTITY_AND_DEDUP_LEDGER`

Minimum fields:

- canonical source ID;
- original filename;
- source path;
- category;
- bundle appearances;
- dialogue-line count;
- characters/speakers detected;
- source-family classification;
- continuity classification;
- duplicate aliases;
- checksum if available.

## 3.3 No frequency inflation

Statements such as “this motif appears repeatedly” must be based on **unique source objects**, not repeated bundle exposure.

---

# 4. Continuity and story-state ontology

Gakumas cannot be analyzed responsibly without separating longitudinal progression from outcome variants.

Every relevant source should eventually receive a continuity class.

## C0 — Fixed anchor

A source establishes a world rule, institutional fact, explicitly shared progression point, or non-branch-dependent premise.

Use for firm chronology/worldbuilding.

## C1 — Strong longitudinal state

Internal evidence clearly places the material before or after another story state.

Use for developmental claims when placement is secure.

## C2 — Compatible floating state

The material appears compatible with the broader progression, but exact placement is uncertain or unnecessary.

Use for characterization without overclaiming chronology.

## C3 — Branch variant

The scene depends on a mutually exclusive result, route outcome, choice, failure, normal ending, true-labeled ending, or equivalent branch state.

Use for:

- conditional psychology;
- response-to-failure analysis;
- possibility-space characterization;
- comparative branch analysis.

Do **not** automatically integrate all C3 events into one biography.

## C4 — Flexible side continuity

A scene supplies useful character/relationship information but its exact literal placement or compatibility with every main-route state should remain cautious.

This often applies to:

- some support stories;
- some seasonal/event material;
- highly modular character interactions.

## 4.1 True-labeled routes

The filename or game label `true` does not by itself authorize the analyst to declare an ontologically singular “true canon.” Use the formulation:

> **true-labeled branch/state**

unless stronger in-game evidence establishes unique canonical status.

## 4.2 Character possibility-space

Branch variants are not discarded. They are analytically powerful.

A C3 failure scene may show:

- how a character interprets defeat;
- what she fears;
- whom she seeks out;
- whether she externalizes or internalizes blame;
- what the Producer does under stress;
- what remains invariant across outcomes.

The project therefore distinguishes:

> **biographical sequence**

from

> **branch-conditioned possibility-space**.

## 4.3 Invariants across branches

When multiple routes independently reproduce the same trait, belief, relationship grammar, or coping strategy, confidence in that characterization rises.

Record this explicitly in the Branch Divergence Ledger.

---

# 5. Longitudinal macro-spine

The exact chronology must be reconstructed from source evidence rather than presumed from filenames alone. Nevertheless, the corpus supports a macro-spine with at least three major Produce Story eras.

## Series 1

Treat as the initial Produce framework with multiple result variants, including failure/normal/true-labeled states.

Primary analytical task:

- establish each idol's early self-concept;
- identify initial Producer pedagogy;
- map branch divergence;
- isolate traits invariant across outcomes.

## Series 2 — N.I.A.

Shared world-exposition explicitly identifies **N.I.A. / NEXT IDOL AUDITION** as a multi-school competition involving fan-vote ranking, eligibility thresholds, FINALE participation, and Producer/idol co-responsibility.

Primary analytical task:

- map the transition from internal school development to wider competitive visibility;
- analyze popularity, fan support, public judgment, and producer strategy;
- distinguish character growth from game-result variance.

## Series 3 — H.I.F.

The corpus explicitly includes selection and final-stage material tied to **H.I.F.**

Primary analytical task:

- establish H.I.F.'s institutional meaning;
- map which characters participate and under what states;
- analyze late-stage development, succession, visibility, ambition, and institutional culmination.

The final chronology document must remain willing to revise this spine if direct source evidence demands it.

---

# 6. Evidence classes and confidence labels

Every major analytical claim should be classifiable by both **evidence type** and **confidence**.

## 6.1 Textual evidence classes

### T-A — Direct explicit statement

The source states the relevant fact or belief directly.

### T-B — Strong behavioral pattern

Repeated actions/dialogue support the claim across multiple unique sources.

### T-C — Relational inference

The claim is not stated outright but follows strongly from consistent interaction patterns.

### T-D — Interpretive hypothesis

Plausible literary/psychological reading requiring caution and counterevidence.

### T-E — Speculation

Interesting possibility with insufficient support for synthesis-level assertion.

T-E material belongs in notes/open questions, not authoritative prose unless clearly labeled.

## 6.2 Audiovisual evidence classes

### AV-A — Directly observed audiovisual evidence

The actual supplied audio/video has been inspected.

### AV-B — Observed work plus script-traced recurrence

A BGM/song/performance device has been directly inspected in at least one source and its reuse is traced through the scripts.

### AV-C — Script metadata only

The script proves the presence of a cue, voice asset, motion, camera operation, etc., but the rendered performance has not been inspected.

### AV-D — Audiovisual inference requiring verification

The script suggests performative significance, but actual audiovisual evidence is needed.

## 6.3 Confidence vocabulary

Use:

- **high confidence**;
- **moderate confidence**;
- **tentative**;
- **open question**.

Avoid artificial numerical precision unless a ledger genuinely quantifies something meaningful.

---

# 7. Japanese-language close-reading method

Original Japanese is the governing linguistic evidence.

## 7.1 Required attention areas

Where relevant, analyze:

- pronouns and self-reference;
- forms of address;
- honorifics and omission of honorifics;
- sentence-final particles;
- politeness shifts;
- contractions;
- feminine/masculine/neutral register where analytically justified;
- dialect or stylized speech;
- lexical repetition;
- hedging;
- command forms;
- apology and gratitude formulas;
- metaphor;
- wordplay;
- ruby/furigana substitutions;
- written emphasis;
- line-break effects;
- deliberate mismatch between orthography and reading.

## 7.2 Translation discipline

Translations should be reader-oriented but must not erase relevant ambiguity.

When a claim depends on wording:

1. quote or cite the Japanese phrase in the analytical artifact;
2. provide a concise English rendering;
3. explain the relevant semantic/register issue;
4. avoid presenting one English equivalent as exhaustive if the Japanese carries multiple shades.

## 7.3 Voice/register ledger

Maintain:

`GKM_JAPANESE_VOICE_AND_REGISTER_LEDGER`

Fields may include:

- character;
- source ID;
- interlocutor;
- story state;
- linguistic feature;
- example phrase;
- interpretation;
- whether stable, relationship-conditioned, or state-conditioned.

---

# 8. Character analysis protocol

Character analysis occurs in **two passes**: a source-facing core reading and a later definitive monograph.

## 8.1 Phase-3 core reading

For each major idol, read source families separately before collapsing them into one model:

1. Produce Story;
2. Dear Idol;
3. idol communications;
4. Produce Events;
5. live/system-growth/startup dialogue where meaningful;
6. relevant shared/unit material.

The complete-character bundle is a retrieval convenience, not a linear novel.

## 8.2 Core questions

For each character identify:

- initial self-concept;
- central desire;
- fears and avoidance patterns;
- contradiction between self-image and behavior;
- talent/aptitude;
- physical or material constraints;
- relationship to effort;
- relationship to evaluation;
- relationship to failure;
- relationship to popularity/visibility;
- conception of idolhood;
- relationship with Producer;
- peer relationship grammar;
- family/material context;
- public persona versus private behavior;
- linguistic identity;
- branch-conditioned variation;
- changes across story states;
- unresolved contradictions.

## 8.3 No premature totalization

The Phase-3 character reading is explicitly provisional. It must end with:

- confirmed observations;
- working hypotheses;
- contradictions;
- missing relational evidence;
- support/event verification needs;
- audiovisual requests;
- legacy claims requiring audit.

## 8.4 Definitive monograph

The final character document is written only after:

- events are processed;
- support cards are processed;
- major relationship systems are reconstructed;
- side-character evidence is searched;
- high-priority audiovisual requests are resolved;
- musical identity baseline is mature.

The final character monograph should address:

1. core thesis;
2. story-state chronology;
3. initial self-concept;
4. central contradiction;
5. desire/fear/wound;
6. talent, weakness, embodiment;
7. idolhood and performance;
8. competition/evaluation;
9. Producer relationship;
10. peer relationships;
11. family/material context;
12. money, labor, food, health where relevant;
13. public/private self;
14. Japanese linguistic identity;
15. voice-acting profile;
16. singing voice and musical identity;
17. failure/recovery behavior;
18. branch divergence;
19. event/support corrections;
20. later-state development;
21. ethics/philosophy;
22. institutional function;
23. unresolved tensions;
24. legacy-analysis reconciliation;
25. primary-source locator table.

---

# 9. Relationship analysis protocol

Relationships are not reducible to two isolated character profiles.

## 9.1 Relationship object

A relationship is treated as its own evolving analytical object with:

- origin/history;
- mutual perception;
- asymmetry;
- dependency/autonomy balance;
- rivalry/support structure;
- linguistic register;
- physical/social proximity;
- conflict style;
- repair style;
- role in self-concept;
- changes across story states;
- external institutional pressures;
- audiovisual performance cues where relevant.

## 9.2 Relationship state ledger

Maintain:

`GKM_RELATIONSHIP_STATE_LEDGER`

Suggested fields:

- participants;
- source ID;
- story state;
- continuity class;
- interaction type;
- initiating party;
- explicit claims;
- inferred dynamic;
- change from previous state;
- contradiction/counterevidence;
- confidence.

## 9.3 Major relational systems

The method must allow some relationships/groups to receive dedicated synthesis when their interaction produces an arc larger than either individual character.

Likely high-priority systems include:

- Hanami Saki / Hanami Ume;
- Lilja / Sumika / REVERSI;
- Temari / Misuzu / Rinha / SyngUp!;
- Saki / Temari / Kotone;
- China / Ume / Hiro;
- Sena / Tsubame;
- senior/junior succession structures;
- class and unit friendship networks.

These are hypotheses to be confirmed by the full reread, not predetermined final conclusions.

---

# 10. Producer analysis protocol

The Producer requires special treatment because the player-facing structure can blur characterization and function.

Distinguish:

## P0 — Stable Producer trait

Behavior or belief recurring across multiple routes/characters.

## P1 — Character-specific pedagogy

The Producer adapts method to a specific idol.

## P2 — Branch-conditioned Producer behavior

Response depends on route/result state.

## P3 — Player-functional dialogue

Dialogue primarily serves choice, tutorial, exposition, or gameplay function.

## P4 — Uncertain personalization

Material may represent player projection more than stable protagonist characterization.

The analysis must not automatically combine all selectable responses into one psychologically coherent biography.

A final Producer synthesis should focus on:

- stable professional ethics;
- pedagogy;
- reading of talent;
- motivational strategies;
- use of competition;
- boundaries;
- mistakes and misreadings;
- co-authorship of idol identity;
- power asymmetry;
- institutional role.

---

# 11. Institution and worldbuilding method

Hatsuboshi Academy must be treated as more than scenery.

Maintain:

`GKM_INSTITUTION_AND_IDOL_SYSTEM_LEDGER`

Track:

- school structure;
- idol/professional training;
- student council;
- evaluations;
- rankings;
- auditions;
- jobs and paid requests;
- fan support;
- N.I.A.;
- H.I.F.;
- production responsibilities;
- teachers/trainers;
- clubs/units/classes where relevant;
- external industry pressures;
- school philosophy as enacted rather than merely stated.

The method should repeatedly ask:

> What kind of person does this institution try to produce?

and

> Where does the institution succeed, fail, distort, or overburden its students?

Do not romanticize Hatsuboshi merely because it often enables growth.

---

# 12. Event-story method

Read numbered story events in source order where possible.

For each event, record:

- participants;
- continuity confidence;
- setting and institutional context;
- main conflict;
- character-state deltas;
- relationship-state deltas;
- new side characters;
- theme/motif evidence;
- legacy claims affected;
- audiovisual requests.

The primary question is not merely “what happens?” but:

> **Which existing models does this event confirm, complicate, or break?**

---

# 13. Support-card method

Support-card stories are not presumed to be trivial or secondary characterization.

They are especially valuable for:

- ordinary relational behavior;
- low-stakes habits;
- social comfort/discomfort;
- food/body/training routines;
- money/material context;
- jokes and teasing;
- peer assumptions;
- daily school ecology;
- recurring linguistic habits.

## 13.1 Participant indexing

Because support files may be numerically named, construct:

`GKM_SUPPORT_AND_EVENT_PARTICIPANT_INDEX`

Fields:

- canonical source ID;
- support/event story ID;
- speakers;
- mentioned characters;
- relationship pairs;
- source family;
- continuity confidence;
- themes/concepts;
- story-state estimate;
- analytical notes.

## 13.2 No cherry-picking rule

Comedy, mundane scenes, and low-drama interactions still count as evidence. They may be more reliable for stable behavior than climactic scenes.

---

# 14. Side-character and NPC method

Do not equate “no dedicated character bundle” with “minor analytical importance.”

Maintain:

`GKM_NPC_AND_SIDE_CHARACTER_LEDGER`

Search by:

- speaker name;
- internal actor code;
- mentions in other characters' material;
- relationship clusters;
- event/support participation.

High-priority figures may include:

- Asari;
- Rinha;
- Kunio;
- trainers/teachers;
- family members;
- Gokugetsu-related figures;
- other recurring school/industry actors.

For Rinha in particular, use cross-character bundle retrieval because no dedicated playable-character bundle exists in the current structure.

---

# 15. Theme and motif method

Themes must be **earned from cumulative evidence**.

Maintain:

`GKM_THEME_AND_MOTIF_LEDGER`

Candidate themes may include, without being limited to:

- rivalry and recognition;
- support and care;
- dependence and autonomy;
- ambition;
- failure and recovery;
- visibility and popularity;
- embodiment;
- training;
- food;
- money and labor;
- school/institutional pedagogy;
- inheritance and succession;
- senpai/kouhai structures;
- self-authorship;
- performance persona;
- talent versus effort;
- private contradiction becoming public expression.

These are **candidate hypotheses**, not predetermined themes.

## 15.1 Minimum standard for synthesis-level theme

A major thematic claim should ideally have:

- evidence across multiple characters;
- evidence across multiple source families;
- evidence from different story states;
- counterexamples considered;
- a clear distinction between recurring motif and governing thematic argument.

## 15.2 Anti-symbolism rule

Do not invent symbolic meaning solely because a visual, food item, color, phrase, or repeated activity appears more than once.

Ask:

1. Is repetition demonstrable?
2. Does context support a stable conceptual function?
3. Are characters or staging treating it as meaningful?
4. Does the interpretation explain more than coincidence would?
5. Is there counterevidence?

If not, keep it at motif or observation level.

---

# 16. Voice-acting analytical method

Voice acting is a first-class component of characterization but will be studied through **selective high-value audiovisual sampling**.

## 16.1 Spoken-performance dimensions

When actual audio/video is supplied, analyze where relevant:

- pitch/register;
- resonance;
- breathiness;
- vocal weight;
- brightness/darkness;
- tempo;
- articulation;
- amplitude;
- pause structure;
- hesitation;
- laughter;
- crying/voice break;
- shouting;
- ironic coloration;
- emotional suppression;
- intimacy distance;
- relational shifts;
- public versus private delivery.

Avoid pseudo-acoustic precision unless measured from audio. Descriptions should remain perceptual and comparative.

## 16.2 Voice-performance state ontology

Maintain:

`GKM_VOICE_PERFORMANCE_STATE_LEDGER`

Classify observed traits as:

### V0 — Baseline voice characteristic
Persistent across contexts.

### V1 — Relationship-conditioned
Changes with a particular interlocutor or relational role.

### V2 — Emotional-state-conditioned
Changes under anger, shame, fear, triumph, grief, etc.

### V3 — Developmental change
A later-state performance shift that appears systematic.

### V4 — Performance persona
Deliberately adopted public/stage/idol voice.

## 16.3 Dialogue audiovisual escalation

Do not pre-upload arbitrary quantities of story video.

During textual analysis, maintain:

`GKM_AUDIOVISUAL_VERIFICATION_QUEUE`

Each request should include:

- AVQ ID;
- character(s);
- internal source ID/path;
- story state;
- human-readable scene description;
- exact/distinctive Japanese search lines;
- reason for request;
- whether voice, BGM, staging, or visual acting matters;
- priority.

Priorities:

- **AV-P0 — interpretation blocking**;
- **AV-P1 — major analytical value**;
- **AV-P2 — corroborative**;
- **AV-P3 — archival curiosity**.

Only P0/P1 should normally create an active retrieval burden.

## 16.4 Public commu nomenclature and retrieval identity

Internal ADV identifiers are excellent provenance keys and poor human search terms. Public uploads are normally titled according to the **originating commu/story/card/song/event**, not according to identifiers such as `adv_dear_hski_027` or `adv_cidol-hski-3-018_01`.

Therefore every active dialogue-AV request must lead with a **human-facing retrieval identity** and keep the machine identifier as a secondary crosswalk field.

Use the following default public nomenclature unless the actual source proves a more specific label:

| Internal source family | Preferred Japanese retrieval nomenclature | Typical additional anchor |
| --- | --- | --- |
| `adv_dear_*` | `親愛度コミュ` | STEP number, chapter range, individual chapter number/title |
| `adv_cidol_*` | `アイドルコミュ`; when song-linked, prefer `楽曲コミュ` | song/P-idol title, part number |
| `adv_pstory_*` | `プロデュースコミュ` | `初`, `N.I.A`, `H.I.F`, audition/result/route state |
| `adv_pevent_*` | use the identifiable subtype, e.g. `育成コミュ`, `おでかけコミュ`, `営業コミュ` | scenario/subtype title and character |
| `adv_csprt_*` | `サポートコミュ` | support-card title and/or featured characters |
| `adv_event_*` | `イベントコミュ` | official event title |
| `adv_unit_*` / unit-story material | `初星コミュ` where that is the public-facing label | unit/story title and episode |
| live/performance material | song title + character + `MV` / `3DMV` / `ライブ` as appropriate | solo/unit/ensemble version |

These are retrieval conventions, not replacements for source taxonomy. Preserve both identities.

### 16.4.1 Search-term construction

The analyst owns the machine-ID-to-public-title resolution burden. Do **not** ask the user to reverse-engineer transcript filenames.

Construct searches in this order:

1. `学マス` or `学園アイドルマスター`;
2. Japanese character name;
3. public commu family (`親愛度コミュ`, `楽曲コミュ`, `サポートコミュ`, etc.);
4. originating song/card/event/story title;
5. STEP/chapter/episode range when known;
6. route/state label (`N.I.A`, `H.I.F`, etc.) when discriminating;
7. distinctive Japanese dialogue only as a **fallback discriminator**, not the default primary query.

Preferred query shapes include:

- `学マス [キャラ名] 親愛度コミュ21～27 STEP3`
- `学マス [楽曲名] [キャラ名] 楽曲コミュ`
- `学マス [キャラ名] 親愛度コミュ28～37 H.I.F STEP4`
- `学マス [サポートカード名] サポートコミュ`
- `学マス [イベント名] イベントコミュ`

Supply at least one copy-paste-ready Japanese query and, for difficult material, two or three fallback variants. Community uploader terminology may be slightly loose; optimize for retrieval rather than terminological purity.

### 16.4.2 Whole-commu acquisition rule

Prefer the **complete commu, complete chapter compilation, complete card/event story, or complete song commu** over manually clipped target scenes.

Reasons:

- surrounding dialogue may change interpretation;
- BGM entry/exit and scene transitions are preserved;
- pauses, reaction shots, camera resets, and post-scene affect remain visible;
- one compilation may satisfy several AV requests;
- the user does not need to spend time manually cutting video.

If several requested scenes occur inside one public compilation, collapse them into **one retrieval target** and record all covered AVQ IDs. The analyst is responsible for locating and timestamping the relevant portions after upload.

For dialogue commus, **720p is normally analytically sufficient** when audio is intact and facial animation, gestures, camera changes, and text remain legible. Higher resolution is preferred for detailed MV/costume/lighting analysis but should not create unnecessary retrieval burden.

### 16.4.3 Required retrieval packet

Every P0/P1 dialogue-video request should be emitted in this form:

- **Human-facing retrieval name** — e.g. `[character] — [song] 楽曲コミュ` or `[character] — 親愛度STEP3 21～27`;
- **Primary Japanese search** — copy-paste ready;
- **Fallback searches** — when useful;
- **Internal crosswalk** — one or more `adv_*` IDs;
- **Coverage** — all AVQ IDs/scenes satisfied by this whole video;
- **Story state / continuity track**;
- **Why requested** — voice, BGM, staging, facial acting, camera, etc.;
- **Acquisition preference** — whole commu/compilation; no clipping required;
- **Priority** — AV-P0/P1/P2/P3.

This packet is the user-facing acquisition interface. Machine identifiers remain provenance infrastructure, not retrieval instructions.

---

# 17. Music, image-song, and MV analytical method

Every major idol receives a **Musical Identity Core Corpus**.

## 17.1 Initial baseline

Target approximately **3 image songs per idol initially**, ideally with official or high-quality MVs where available.

Expand selectively to approximately **4–6 works** when needed.

Selection criteria:

1. foundational identity song;
2. contrasting image song;
3. later/developmental song;
4. narratively important song;
5. relational/unit song where relevant;
6. outlier work that complicates the obvious profile.

Do not simply select the most popular tracks.

## 17.2 Song discovery and metadata

Use:

- official Gakumas pages/channels for verification;
- official release pages/credits;
- Project-imas as a discovery/indexing crosswalk;
- other reliable public metadata only when necessary.

Raw audio/video supplied for the project governs close reading of the actual sonic/visual work.

## 17.3 Musical analysis dimensions

Where evidence supports it, analyze:

- melodic contour;
- tessitura;
- harmony;
- rhythm;
- tempo;
- instrumentation;
- arrangement density;
- acoustic/electronic balance;
- guitar/piano/string/synth usage;
- pre-chorus/chorus architecture;
- buildup/release;
- modulation/key change;
- recurring sonic motifs;
- genre vocabulary;
- vocal timbre;
- attack;
- sustain;
- breath;
- articulation;
- vibrato;
- rhythmic precision;
- contrast between speaking and singing self.

## 17.4 Lyric analysis

Lyrics are analyzed as character evidence only when:

- the song is explicitly an image/character song or narratively associated with the idol;
- the project's interpretation distinguishes lyrical persona from literal autobiography;
- the claim is cross-checked against story characterization where necessary.

Do not assume every first-person lyric is a documentary statement by the character.

## 17.5 MV analysis

Where MVs are available, analyze:

- framing;
- camera distance and movement;
- editing rhythm;
- choreography;
- posture;
- eye line;
- costume;
- lighting;
- color;
- spatial isolation/integration;
- recurring gestures;
- synchronization of lyric/music/choreography;
- stage/public persona;
- relation to character story state.

## 17.6 Musical dramaturgy

The highest-order question is:

> **Why this sound, for this character, at this point in her development?**

Compare songs longitudinally. Look for:

- continuity;
- contradiction;
- maturation;
- self-expansion;
- new emotional vocabulary;
- stage expression that ordinary dialogue cannot sustain.

---

# 18. BGM dramaturgy method

Raw ADV scripts expose BGM cue IDs. This permits large-scale dramaturgical tracing even without video for every scene.

Method:

1. identify recurring BGM cue ID;
2. obtain/inspect the actual track before describing its sonic character;
3. establish a conservative musical description;
4. search cue recurrence across unique source scripts;
5. classify scene functions;
6. test whether deployment is systematic;
7. examine cue changes inside important scenes;
8. request rendered audiovisual evidence when mixing/timing matters.

Do not infer mood from an asset filename alone.

---

# 19. Audiovisual source crosswalk

Maintain:

`GKM_AUDIOVISUAL_SOURCE_CROSSWALK.md`

and preferably:

`GKM_AUDIOVISUAL_SOURCE_CROSSWALK.json`

Each mapped object should preserve multiple identities:

- internal source ID;
- internal filename;
- character;
- source family;
- analytical story state;
- official Japanese UI/story title where known;
- community shorthand;
- public video title;
- distinctive Japanese dialogue;
- voice asset prefix;
- song title / performer / release where applicable;
- verified raw audiovisual artifact supplied to project;
- analytical documents using it.

Do not replace machine nomenclature with human nomenclature; preserve both.

## 19.1 Crosswalk identity layers

Treat these as distinct fields rather than synonyms:

1. **internal ADV identity** — machine/provenance key;
2. **source-family identity** — Dear Idol, Idol Communication, Produce Story, Support Story, Event Story, Unit Story, etc.;
3. **official/public UI identity** — official chapter/card/song/event title where recoverable;
4. **community/uploader identity** — the title form actually used in searchable uploads;
5. **analytical identity** — project-specific description of why the object matters;
6. **supplied artifact identity** — exact filename/checksum of the media inspected.

One whole public video may map to several internal source IDs, and one internal story object may be represented by multiple public media artifacts (for example, full commu, isolated chapter, 2D MV, and 3DMV). The crosswalk must support **many-to-many mapping**.

## 19.2 Searchability requirement

A dialogue AVQ entry is not retrieval-ready until it contains enough human-facing information that a user can plausibly locate the media without understanding the ADV repository. At minimum this normally means:

- Japanese character name;
- public commu category;
- song/card/event/story/STEP identity;
- one optimized Japanese search query.

Exact dialogue strings are useful for verification after discovery but should not be assumed to be indexed by YouTube or other upload surfaces.

---

# 20. Raw ADV staging method

Raw ADV commands are analytically meaningful when they show deliberate staging.

Potentially relevant features:

- camera focal length;
- camera position;
- depth of field;
- actor placement;
- entrances/exits;
- facial-motion changes;
- gesture/motion cues;
- background changes;
- fades;
- timing;
- BGM starts/stops;
- voice timing.

However, script commands do not always equal the perceptual effect of the rendered scene. If a claim depends on visual emphasis, rhythm, or performance nuance, escalate to audiovisual inspection.

---

# 21. Legacy-analysis reconciliation

Maintain:

`GKM_LEGACY_CLAIM_REVISION_LEDGER`

Every substantial inherited thesis may receive:

- **CONFIRMED**;
- **STRENGTHENED**;
- **NARROWED**;
- **REVISED**;
- **REJECTED**;
- **UNRESOLVED**.

Each entry should include:

- legacy claim;
- source of legacy claim;
- V2 evidence;
- counterevidence;
- revised formulation;
- affected final document.

Prior analyses should never be quoted as proof of the game itself.

---

# 22. Adversarial analysis protocol

The final synthesis must attempt to disprove its own strongest theses.

For every major claim ask:

1. What is the strongest counterexample?
2. Which character least fits the model?
3. Does the claim survive outside climactic scenes?
4. Does a support/event story contradict it?
5. Is the interpretation actually route-specific?
6. Does the institution ever produce the opposite effect?
7. Is the Producer ever wrong?
8. Does rivalry become harmful rather than productive?
9. Does support become dependency, coercion, or avoidance?
10. Does inheritance become burden rather than continuity?
11. Does popularity distort rather than reveal value?
12. Does the musical profile complicate the textual profile?

A thesis that survives this process receives substantially greater confidence.

---

# 23. Character-state ledger

Maintain:

`GKM_CHARACTER_STATE_LEDGER`

Recommended fields:

- character;
- canonical source ID;
- story state;
- continuity class;
- self-concept;
- desire;
- fear;
- goal;
- belief about idolhood;
- belief about competition;
- belief about Producer;
- physical/material condition;
- key relationship changes;
- observed behavior;
- branch-specific/invariant flag;
- evidence class;
- confidence;
- delta from prior state.

Do not force every row to contain every field.

---

# 24. Branch divergence ledger

Maintain:

`GKM_BRANCH_DIVERGENCE_LEDGER`

For each branch family record:

- shared pre-branch state;
- branch condition;
- outcome;
- character response;
- Producer response;
- relationship changes;
- invariant traits;
- branch-only traits;
- whether later sources presuppose any outcome;
- implications for continuity.

This ledger is essential for preventing branch variants from being misread as one biography.

---

# 25. Primary-source locator ledger

Maintain:

`GKM_PRIMARY_SOURCE_LOCATOR_LEDGER`

The goal is:

> synthesis claim -> analytical artifact -> evidence entry -> exact source locator -> original Japanese

Minimum locator fields:

- claim ID;
- canonical source ID;
- source path;
- internal filename;
- speaker(s);
- distinctive line(s);
- story state;
- raw/dialogue/bundle paths;
- audiovisual crosswalk ID if applicable.

Final documents should use compact locators while the ledger stores full traceability.

---

# 26. Evidence quotation discipline

Use Japanese quotations sparingly and purposefully.

A quotation should do at least one of the following:

- establish exact wording;
- demonstrate register;
- preserve ambiguity;
- show repeated phrase/motif;
- support a close reading impossible from paraphrase.

Do not inflate analytical documents with long transcript reproduction.

---

# 27. Quantitative claims

Counts may support analysis, but they must be methodologically sound.

Examples:

- number of unique scripts using a BGM cue;
- number of unique sources containing a form of address;
- number of scenes involving a relationship pair.

Rules:

- deduplicate first;
- define what is being counted;
- do not substitute frequency for significance;
- distinguish scripted occurrence from interpreted function.

---

# 28. Negative evidence

Absence can matter, but use cautiously.

Do not claim “character never does X” unless the relevant source coverage is sufficiently complete.

Safer formulations:

- “no instance was found in the frozen corpus”;
- “the examined source families do not show...”;
- “this behavior appears rare relative to...”

---

# 29. Comparative claims between characters

Comparisons should control for source imbalance.

If one character has more late-stage material, support stories, or audiovisual evidence, do not treat raw quantity of examples as equivalent characterization density.

Comparative claims should emphasize:

- matched story states where possible;
- comparable source families;
- clearly stated evidence asymmetry.

---

# 30. Full-series synthesis standard

The final series synthesis should be written only after the character, relationship, event, support, institutional, linguistic, and audiovisual layers are mature.

A synthesis-level claim should ideally satisfy:

- multi-source support;
- multi-character support where applicable;
- chronology awareness;
- branch awareness;
- counterevidence review;
- legacy-claim audit;
- primary-source traceability.

The final synthesis should distinguish:

- what the work **shows**;
- what characters **believe**;
- what institutions **claim**;
- what the analyst **infers**.

These are not interchangeable.

---

# 31. Required recurring ledgers and infrastructure

The V2 project should maintain at minimum:

1. `GKM_SOURCE_IDENTITY_AND_DEDUP_LEDGER`
2. `GKM_CONTINUITY_AND_STORY_STATE_LEDGER`
3. `GKM_BRANCH_DIVERGENCE_LEDGER`
4. `GKM_CHARACTER_STATE_LEDGER`
5. `GKM_RELATIONSHIP_STATE_LEDGER`
6. `GKM_INSTITUTION_AND_IDOL_SYSTEM_LEDGER`
7. `GKM_THEME_AND_MOTIF_LEDGER`
8. `GKM_JAPANESE_VOICE_AND_REGISTER_LEDGER`
9. `GKM_NPC_AND_SIDE_CHARACTER_LEDGER`
10. `GKM_SUPPORT_AND_EVENT_PARTICIPANT_INDEX`
11. `GKM_PRIMARY_SOURCE_LOCATOR_LEDGER`
12. `GKM_LEGACY_CLAIM_REVISION_LEDGER`
13. `GKM_VOICE_PERFORMANCE_STATE_LEDGER`
14. `GKM_SONG_AND_MUSICAL_IDENTITY_LEDGER`
15. `GKM_AUDIOVISUAL_VERIFICATION_QUEUE`
16. `GKM_AUDIOVISUAL_SOURCE_CROSSWALK`

These need not all be manually maintained as giant prose documents. Some may be structured Markdown/CSV/JSON artifacts. What matters is that the information persists across phases.

---

# 32. Stop conditions and revision triggers

A document should be revised when:

- new source evidence contradicts a central claim;
- continuity classification changes;
- an AV-P0/P1 request materially alters interpretation;
- a character's later state changes the meaning of earlier scenes;
- deduplication reveals false frequency;
- new source-lock material creates a major longitudinal extension.

Do not rewrite merely because wording can be polished. Revision should track analytical change.

---

# 33. Final methodological commitments

The Gakumas V2 project is governed by the following commitments:

1. **Original Japanese is primary.**
2. **Raw ADV is the final textual authority.**
3. **Analysis bundles are the main ingestion layer, not the authority layer.**
4. **Bundle duplication does not create duplicate evidence.**
5. **Branch variants are not automatically one biography.**
6. **True-labeled routes are not automatically declared sole canon.**
7. **Support cards and events are genuine characterization.**
8. **Chronological certainty is graded, not invented.**
9. **The Producer is analyzed with route/player-function caution.**
10. **Themes emerge from cumulative rereading rather than being imposed in advance.**
11. **Legacy analyses are hypotheses, not proof.**
12. **Voice acting and music are first-class evidence when directly inspected.**
13. **Script metadata can establish occurrence, not sonic quality.**
14. **Audiovisual retrieval is selective and interpretation-driven.**
15. **Every major thesis receives counterevidence testing.**
16. **Final claims should remain traceable to source.**
17. **The project is versioned because the work is live-service.**

The goal is not to produce the largest possible corpus of commentary. The goal is to produce the most **recoverable, falsifiable, source-grounded reconstruction of Gakumas's characters, relationships, institutional logic, musical identities, and thematic architecture that the available evidence can support**.
