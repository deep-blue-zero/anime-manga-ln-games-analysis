---
corpus: AOBUTA_JP_DEEP_READING
work: "青春ブタ野郎シリーズ"
work_en: "Seishun Buta Yarou / Rascal Does Not Dream"
author: "鴨志田一"
document: analytical_method
version: "2.0"
date: "2026-08-11"
primary_language: ja
source_type: light_novel
source_format: epub
primary_scope: "Japanese light novels Volumes 1-15 plus canon extras when supplied"
analysis_mode: sequential_first_pass
spoiler_policy: strict_publication_order
canonical_volume_filename: "AOBUTA_VXX_DEEP_READING.md"
artifact_prefix: "AOBUTA_"
---

# 青春ブタ野郎シリーズ
## Volume-by-Volume Analytical Method v2
### Original-Japanese close reading with provenance, source tracking, and synthesis traceability

## 1. Purpose

This document supersedes *AoButa Volume-by-Volume Analytical Method v1.0* while preserving its interpretive commitments.

The project remains a sequential close reading of 鴨志田一's *青春ブタ野郎シリーズ* in original Japanese. Each volume must still be understood simultaneously as a self-contained literary unit and as one movement in a cumulative series whose later books repeatedly revise what earlier books appeared to establish.

The governing interpretive principle remains:

> **Read each phenomenon simultaneously as an event with literal rules, an embodied experience, an interpersonal crisis, and a social or psychological expression—without collapsing any one layer into another.**

Version 2 adds a second governing principle:

> **Every load-bearing analytical claim should be recoverable from synthesis → canonical volume artifact → evidence entry → primary-source locator → original Japanese EPUB passage or illustration.**

The method therefore aims to produce two durable outputs at once:

1. a substantial literary and character analysis of every volume; and
2. an auditable evidence architecture from which later checkpoint and full-series syntheses can be written without reconstructing the source trail from memory.

The archival layer does not replace interpretation. It exists so that sophisticated claims about identity, memory, recognition, care, time, romance, institutional failure, and Adolescence Syndrome remain inspectable months or years later.

## 2. What v2 changes

Version 2 retains the entire v1 close-reading framework and adds:

- canonical per-volume Markdown artifacts named `AOBUTA_VXX_DEEP_READING.md`;
- standardized YAML metadata for Library retrieval and corpus management;
- source filename, SHA-256 checksum, EPUB spine count, illustration count, and integrity status where verifiable;
- a source/structure audit at the beginning of every volume;
- an expanded Evidence Classification Ledger;
- a dedicated Primary-Source Locator Ledger;
- stable evidence IDs;
- a second epistemic axis distinguishing direct establishment from speculation;
- explicit prospective-versus-retrospective reading status;
- a provenance audit pass before the cumulative delta;
- standardized cumulative-ledger updates;
- Library search and retrieval conventions;
- raw-source cold-storage and selective reintroduction rules;
- a migration rule for pre-v2 Volumes 1–7;
- and a final synthesis traceability chain.

The principal adaptation from `NANA_ANALYTICAL_METHOD_V2.md` is archival rather than interpretive. AoButa retains its series-specific priorities: non-reductive treatment of Adolescence Syndrome, Sakuta-aligned focalization, Mai as continuing co-protagonist, ensemble continuity, Japanese voice, literal-versus-metaphorical distinction, and the ethics of intervention.

The default mode remains **strict publication-order first-pass reading**. Later revelations may revise earlier interpretations only after the later source has actually been analyzed, and the correction must remain visibly labeled rather than silently rewriting the historical reading.

## 3. Governing disciplines

Every volume analysis must satisfy the following requirements.

### 3.1 Read the complete primary source

Read the complete Japanese EPUB in spine order, including:

- title and opening pages;
- table of contents;
- prologue, numbered sections, chapters, interludes, and epilogue;
- every embedded illustration in its intended position;
- afterword and other relevant paratext;
- any included bonus story or retailer-specific material whose provenance can be established.

Search, remembered plot knowledge, adaptations, summaries, and fan discussion are not substitutes for reading the full novel.

### 3.2 Preserve the sequential epistemic boundary

The first analysis of Volume *N* may use:

- Volumes 1 through *N* already analyzed in publication order;
- earlier canon extras already analyzed at their proper release position;
- the current volume’s own afterword, treated as paratext.

It must not use later novels to settle present ambiguity. Later revelations must not be silently imported into an earlier character’s motives, the operation of a phenomenon, or the reader’s expectations.

This creates two legitimate but separate modes:

- **First-pass historical reading:** What the text and reader can know at this point in publication order.
- **Retrospective rereading:** How later material revises, confirms, or destabilizes the earlier interpretation.

Do not mix these modes within the first-pass analysis. Retrospective notes belong in later checkpoint or full-series synthesis documents and must be labeled as such.

### 3.3 Keep fact, belief, inference, interpretation, ambiguity, and judgment distinct

Use the v2 evidence classes defined formally in §18. In compact form, these distinguish **TF** textual fact, **SI** strong inference, **TI** thematic/tentative interpretation, **CB** character belief, **UA** unresolved ambiguity, **FP** prospective signal, **RC** retrospective correction, and **VJ** explicit value judgment.

A second optional confidence axis (**A–E**) distinguishes how strongly the source establishes the proposition. This matters especially when a statement is directly attested as a character's theory but only weakly established as literal world mechanics.

These labels need not clutter every paragraph of the finished essay. They must, however, appear in the evidence and open-question ledgers whenever confidence or ontological status materially affects the claim.

### 3.4 Preserve contradictions

Do not force a character, relationship, or phenomenon into a single clean explanation when the novel sustains multiple truths. In *AoButa*, a joke can be affectionate and invasive; a rescue can be loving and self-destructive; a character can desire recognition and fear exposure; a phenomenon can embody a conflict without being reducible to allegory.

Contradiction is often characterization, not noise.

## 4. Source hierarchy and corpus control

### 4.1 Source hierarchy

Use sources in this order:

1. **The original Japanese novel currently under analysis**
2. **Earlier original Japanese novels and canon extras already analyzed**
3. **Illustrations and paratext belonging to the same edition**
4. **Official supplementary material**, evaluated according to its date, authorship, and narrative status
5. **Official translations**, used only for comparison or efficient retrieval
6. **Anime, manga, film, event, drama-CD, or game adaptations**, used only in a separately requested adaptation analysis
7. **Interviews and reliable external scholarship**, used for reception or authorial context, never to override the text
8. **Fan wikis, summaries, and general online discussion**, used only to map reception or identify claims to test against primary evidence

Authorial statements may clarify intention or production history, but they do not automatically settle the literary effect of the published text.

### 4.2 Edition record

At the start of each analysis, record:

- Japanese title;
- volume number and publication position;
- source filename and edition when recoverable;
- chapter and section structure;
- EPUB spine order;
- illustration inventory;
- included extras;
- any missing, duplicated, corrupt, or apparently out-of-order item;
- current spoiler boundary.

### 4.3 Extras: two-order rule

For short stories, drama CDs, booklets, event material, or retailer bonuses, record both:

- **release position** — when the audience received it; and
- **story position** — when its events appear to occur.

First analysis should normally follow release position. A late-written story set during an early novel may reflect later characterization and should not be silently inserted into the earlier historical reading.

## 5. Canonical corpus naming and durable artifacts

Every per-volume analysis is emitted as a stable Markdown artifact:

```text
AOBUTA_V01_DEEP_READING.md
AOBUTA_V02_DEEP_READING.md
...
AOBUTA_V15_DEEP_READING.md
```

Recommended global artifacts are:

```text
AOBUTA_ANALYTICAL_METHOD_V2.md
AOBUTA_MASTER_SOURCE_INVENTORY.md
AOBUTA_EVIDENCE_INDEX.md
AOBUTA_PRIMARY_SOURCE_LOCATOR_INDEX.md
AOBUTA_MASTER_CHRONOLOGY.md
AOBUTA_PHENOMENON_AND_RULE_LEDGER.md
AOBUTA_STATE_WORLD_MEMORY_LEDGER.md
AOBUTA_SAKUTA_INTERVENTION_LEDGER.md
AOBUTA_MAI_AND_CENTRAL_ROMANCE_LEDGER.md
AOBUTA_ENSEMBLE_CHARACTER_LEDGER.md
AOBUTA_RELATIONSHIP_STATE_LEDGER.md
AOBUTA_JAPANESE_VOICE_AND_ADDRESS_LEDGER.md
AOBUTA_INSTITUTION_AND_ADULT_RESPONSIBILITY_LEDGER.md
AOBUTA_PLACE_OBJECT_MOTIF_INDEX.md
AOBUTA_ILLUSTRATION_LEDGER.md
AOBUTA_OPEN_QUESTIONS_AND_HYPOTHESES.md
AOBUTA_RETROSPECTIVE_CORRECTION_LOG.md
```

The canonical per-volume artifact is the durable analytical source. The global ledgers may be compiled later from those artifacts rather than rewritten after every turn.

### 5.1 Stable evidence IDs

Use:

```text
AOBUTA_V01_E001
AOBUTA_V01_E002
...
AOBUTA_V07_E116
```

Once an ID has been published in a canonical artifact, do not silently renumber it. If an entry is withdrawn or reclassified, preserve the ID and record the change.

### 5.2 Bonus and side material

Use clear prefixes that preserve both release position and story position. Do not force late-written theater bonuses into the historical knowledge state of an earlier novel merely because their events occur there chronologically.

## 6. Standard YAML metadata and source/structure audit

Every canonical volume artifact begins with YAML front matter. Minimum schema:

```yaml
---
corpus: AOBUTA_JP_DEEP_READING
work: "青春ブタ野郎シリーズ"
author: "鴨志田一"
volume: 01
japanese_title: "青春ブタ野郎はバニーガール先輩の夢を見ない"
analysis_pass: 1
primary_language: ja
source_type: light_novel
source_format: epub
source_file: "01 青春ブタ野郎はバニーガール先輩の夢を見ない.epub"
source_sha256: "..."
source_spine_items: 29
source_images: 24
primary_source_verified: true
spoiler_scope: "through Volume 01 only"
method: "AOBUTA_ANALYTICAL_METHOD_V2"
provenance_status: full
locator_status: complete
major_characters:
  - 梓川咲太
  - 桜島麻衣
major_relationships:
  - "咲太 / 麻衣"
major_topics:
  - recognition
  - social ontology
major_lexical_targets:
  - 空気
cumulative_status:
  - established
---
```

Do not invent a hash, edition date, spine count, chapter title, or locator. If a field is unverified, use `null`, omit it, or mark it `pending_backfill`.

### 6.1 Source and structure audit

Before literary analysis, establish the source object. Record:

- exact filename;
- file format;
- SHA-256 checksum when available;
- EPUB validity / ZIP integrity;
- language identity of the narrative text;
- OPF metadata when useful;
- spine count and spine order;
- chapter and section map;
- front matter and afterword;
- illustration inventory;
- included extras;
- duplicated, blank, corrupt, missing, or out-of-order resources;
- and the current spoiler boundary.

For text EPUBs, device pagination is not a stable locator. The governing structural locator is normally **chapter + numbered subsection when present + spine index/internal XHTML filename + short Japanese anchor phrase**.

### 6.2 Source integrity versus literary confidence

A structurally valid EPUB can still be unsuitable for Japanese-language analysis if its narrative is another language, OCR-corrupted, or incomplete. Record source fitness separately for:

- plot and event order;
- Japanese wording and voice;
- illustration analysis;
- paratext;
- quotation-grade verification.

## 7. Central research questions

Each volume should answer the questions that its evidence makes relevant rather than forcing identical conclusions. Across the series, the cumulative project should repeatedly test the following.

1. What form of recognition does a character want, and what makes being seen dangerous?
2. How does the pressure to read or obey the social atmosphere—**空気を読む**—shape perception, speech, memory, and conduct?
3. When does adaptation to others become empathy, and when does it become self-erasure?
4. What makes a self continuous across memory loss, bodily change, role performance, duplicated possibilities, or altered histories?
5. Is adolescence represented as a clinical stage, a social position, a metaphysical instability, or some combination?
6. How do private pain and public legibility interact? What suffering becomes visible, credible, dismissible, sensational, or exploitable?
7. What does care demand: attention, belief, intervention, sacrifice, restraint, or permission?
8. When Sakuta intervenes, does he restore another person’s agency, substitute his judgment for theirs, or do both at once?
9. How does Mai and Sakuta’s continuing relationship change the structure of later arcs? Do they operate as lovers, witnesses, co-investigators, protectors, critics, or competing claimants over risk?
10. How do family, school, entertainment, medicine, friendship groups, social media, and public opinion produce or intensify the crisis?
11. What distinguishes an emotionally satisfying resolution from a causally or ethically adequate one?
12. What remains after an apparent resolution: memory traces, bodily residues, changed habits, grief, obligations, new dependencies, or altered possibilities?
13. How does movement from high school toward university and adult work change the series’ conception of “adolescence”?
14. What does the volume add to the series’ account of choosing a future under uncertainty?

## 8. The Adolescence Syndrome analysis matrix

For every apparent case of **思春期症候群**, build a phenomenon dossier. Do not begin by assuming that Futaba Rio’s first explanation is complete, that the apparent sufferer is the only causal participant, or that the phenomenon has one-to-one symbolic meaning.

### 8.1 Observable phenomenology

Record what actually occurs before explaining it:

- who can perceive the phenomenon;
- who cannot;
- what changes in body, memory, time, space, identity, or probability;
- onset, escalation, variation, and cessation;
- physical and emotional sensations;
- public versus private manifestations;
- whether witnesses share the same experience;
- objects, marks, records, or memories that persist;
- counterexamples to the proposed rule.

### 8.2 Precipitating conflict

Identify the conflict temporally associated with onset, while avoiding the easy formula “emotion X caused magic Y.” Ask:

- What desire cannot be admitted?
- What decision is being deferred?
- What social role has become intolerable?
- What contradiction cannot coexist in ordinary life?
- Is the apparent trigger a cause, catalyst, interpretation, or coincidence?
- Does the volume distinguish the first onset from later escalation?

### 8.3 Social substrate

Map the collective conditions that make the conflict consequential:

- peer surveillance and classroom atmosphere;
- rumor and network effects;
- fame, audience attention, and commercial image;
- bullying, exclusion, and institutional disbelief;
- family comparison or expectation;
- gendered and age-coded expectations;
- entrance exams, careers, graduation, and future planning;
- the difference between being ignored, unseen, forgotten, or deliberately excluded.

### 8.4 Literal mechanics

Construct the narrowest model that accounts for the evidence. Specify:

- necessary and sufficient conditions, if known;
- whether the event is local, contagious, relational, or world-level;
- whether memory follows the person, the observer, the body, the timeline, or something else;
- whether multiple states coexist or replace one another;
- what action changes the system;
- what the model fails to explain.

The model should remain revisable. A later contradiction is evidence against the model, not an inconvenience to be explained away.

### 8.5 Diegetic explanation versus scientific validity

Track every explanation offered by Rio, Sakuta, a clinician, a rumor, or another character. For each, distinguish:

1. **Explanatory role in the story** — what the analogy helps the characters notice or attempt.
2. **Diegetic status** — whether the novel confirms it, merely entertains it, or later complicates it.
3. **Real-world scientific status** — whether it is a rigorous claim, a loose analogy, speculative language, or pseudoscientific ornament.

Quantum-mechanical language should not be accepted as proof merely because the characters use it. It also should not be dismissed as “bad science” without asking what narrative work the analogy performs. The proper question is often: *Where does this model illuminate the phenomenon, and where does the mapping break?*

### 8.6 Embodied and metaphorical meaning

Analyze how the literal event gives form to an otherwise difficult experience. Use non-reductive phrasing:

- “The phenomenon externalizes…”
- “The event makes socially visible…”
- “The mechanics create an analogue for…”
- “This reading explains X but not Y…”

Avoid “the syndrome is merely a metaphor for…” unless the text decisively eliminates literal operation, which *AoButa* generally does not.

### 8.7 Intervention and causal chain

For every attempted solution, reconstruct:

1. what the interveners believe;
2. what action they take;
3. what immediate change follows;
4. what evidence links the action to the change;
5. what alternative causes remain possible;
6. what interpersonal acknowledgment, decision, or sacrifice accompanies the action;
7. who bears the cost.

Do not confuse chronological proximity with demonstrated causation.

### 8.8 Resolution, residue, and recurrence

An apparent cure is not the end of the analysis. Record:

- what changed internally;
- what changed socially;
- what changed literally;
- what did not change;
- whether the person chose a future or merely escaped a crisis;
- whether others remember;
- whether the body, environment, dreams, or habits retain traces;
- whether the resolution creates a new obligation or unresolved grief.

## 9. Time, worlds, dreams, and memory bookkeeping

Whenever a volume alters sequence, causality, possibility, or recollection, maintain a formal event ledger.

### 9.1 Separate four orders

| Order | Question |
| --- | --- |
| **Narrated order** | In what sequence does the novel disclose events? |
| **Experienced order** | In what sequence does each character live or remember them? |
| **Causal order** | Which events appear to produce which later states? |
| **Publication order** | What could the reader know when this volume appeared? |

### 9.2 State/world notation

When needed, assign neutral working labels such as **State A**, **State B**, or **Possibility 1** rather than prematurely declaring “the real timeline.” For each state, track:

- living persons and bodily conditions;
- possessed memories;
- public records;
- relationships and promises;
- physical residues;
- dreams or anticipatory knowledge;
- transition conditions;
- evidence of persistence across transitions.

### 9.3 Dream taxonomy

Do not treat every dream alike. Classify it provisionally as one or more of:

- ordinary psychological dream;
- memory replay;
- displaced or residual memory;
- anticipatory experience;
- communication across states;
- imagined counterfactual;
- framing device whose status remains unresolved.

Then cite the sensory, temporal, and narrative evidence for that classification.

### 9.4 Identity continuity test

When memory, personality, body, or history changes, ask separately:

- Who experiences continuity?
- Who is recognized by others as continuous?
- Which memories are autobiographically available?
- Which commitments persist?
- Does the narration treat loss as recovery, replacement, integration, death, or something deliberately harder to name?
- Whose preferred description controls the scene?

Do not import a clinical or philosophical answer when the novel itself sustains grief and ambiguity.

## 10. Narration and focalization

### 10.1 Sakuta-aligned third person

The default narration is close third person centered on Sakuta. It frequently absorbs his diction, comic timing, attention, judgments, and omissions. Therefore distinguish:

- what the narrator directly reports;
- what Sakuta notices;
- what Sakuta infers;
- what free-indirect phrasing makes feel narratively endorsed;
- what the scene shows despite Sakuta’s interpretation.

Close access to Sakuta does not make him omniscient or wholly reliable. His jokes can reveal desire, deflect fear, protect another person, evade embarrassment, or control the emotional tempo. Determine which function applies in the specific exchange.

### 10.2 Sakuta perception ledger

For important scenes, record:

- first noticed detail;
- detail noticed late or not at all;
- stated interpretation;
- likely unspoken motive;
- action taken;
- discrepancy between his self-description and conduct;
- later correction by Mai or another character.

### 10.3 Information distribution

Ask who knows what, when, and with what confidence. *AoButa* often creates drama from asymmetric memory, private experience, concealed plans, or one person believing an event that nobody else can verify. Track:

- private knowledge;
- shared knowledge;
- credible evidence;
- public story;
- mistaken belief;
- deliberately withheld information;
- knowledge destroyed or altered by the phenomenon.

### 10.4 Opening and closing architecture

Analyze:

- the title’s “does not dream of” construction;
- who is grammatically or thematically dreaming of whom;
- opening promises, recurring lines, and apparent flash-forwards;
- chapter-title irony;
- echoes between the first and final scenes;
- how the ending changes the meaning of the opening.

Repeated formulas such as “that day Sakuta met…” should be examined for variation rather than treated as neutral boilerplate.

## 11. Character analysis

### 11.1 No “heroine-of-the-volume” reduction

The title character must be analyzed as a person embedded in continuing relationships, institutions, and future choices—not merely as the carrier of a supernatural problem or a temporary romantic possibility.

For every central character, record:

- publicly performed identity;
- private self-description;
- desire and fear;
- strategy for managing attention;
- what they can and cannot say directly;
- agency before, during, and after Sakuta’s involvement;
- acts of care toward others;
- boundaries asserted or surrendered;
- material and institutional constraints;
- change achieved, refused, or left incomplete.

### 11.2 Sakuta intervention audit

For every major intervention by Sakuta, ask:

1. Did the other person request help?
2. What did Sakuta know, and what did he assume?
3. Did he disclose his plan and its risks?
4. Could the affected person meaningfully refuse?
5. Did the act restore voice and choice, or replace them with his judgment?
6. Was self-sacrifice necessary, impulsive, theatrical, avoidable, or some mixture?
7. Who performs the decisive act in the resolution?
8. What would have happened if the plan failed?
9. Does Sakuta learn, or merely survive?
10. Does the series reward behavior that the analysis should still question ethically?

Effectiveness, courage, love, consent, and proportionality are separate judgments.

### 11.3 Mai as continuing protagonist and ethical counterweight

Do not let later volumes demote Mai to “the girlfriend at home” merely because another character supplies the title. Track:

- her independent career and family pressures;
- her reading of Sakuta’s evasions;
- her role as witness, collaborator, boundary-setter, and rescuer;
- what she knows and when she knows it;
- the costs she accepts voluntarily versus those imposed on her;
- jealousy as comedy, information, intimacy, or genuine conflict;
- how public celebrity and private partnership collide;
- whether Sakuta grants her equal authority over risks that affect them both.

### 11.4 Ensemble continuity

Maintain a living ensemble ledger. A previously centered character remains relevant through:

- ordinary friendship;
- advice and practical assistance;
- changed speech or behavior;
- independent ambitions;
- reciprocal care;
- memory of an earlier arc;
- new relationships that do not pass through Sakuta.

Small scenes may supply more durable evidence of recovery or maturation than climactic declarations.

### 11.5 Adults and institutions

Analyze parents, teachers, managers, clinicians, producers, schools, hospitals, and other institutions as actors rather than scenery. Ask:

- Who notices distress?
- Who has a duty to act?
- Who believes, disbelieves, commercializes, medicalizes, or ignores it?
- What resources are available?
- What burden falls on adolescents because adults or institutions are absent?
- Is institutional failure actually shown, or merely inferred because the narrative focalizes the young cast?

## 12. Relationship analysis

### 12.1 Relationship-state ledger

For every materially changed pair or group, record:

| Field | Question |
| --- | --- |
| **State entering volume** | What trust, knowledge, obligation, and conflict already exist? |
| **Pressure event** | What tests or destabilizes the relationship? |
| **Speech act** | What promise, confession, lie, refusal, joke, or silence matters? |
| **Embodied act** | What touch, distance, movement, waiting, or risk changes the meaning? |
| **Agency distribution** | Who chooses, initiates, consents, withholds, or sacrifices? |
| **State leaving volume** | What is now possible or impossible that was not before? |
| **Unresolved tension** | What has been deferred rather than solved? |

### 12.2 Mai and Sakuta

Analyze the central romance as an ongoing practice rather than a binary “together/not together” state. Track:

- teasing and the right to interpret it;
- repair after concealment;
- mutual belief under impossible conditions;
- negotiations over danger and self-sacrifice;
- career, schedule, publicity, and physical distance;
- trust versus unilateral protection;
- sexual language versus enacted boundaries;
- domestic routine and ordinary companionship;
- their movement toward adult partnership.

### 12.3 Care network, not harem scoreboard

Do not organize the ensemble primarily by which girl “likes Sakuta.” Distinguish:

- romantic desire;
- admiration;
- gratitude;
- dependency;
- sibling attachment;
- friendship;
- identification;
- shared secrecy;
- ethical debt;
- comic flirtation.

Also track relationships among the girls and women themselves. The series’ social world becomes richer as knowledge, care, and accountability cease to run only through Sakuta.

## 13. Japanese language and character voice

Japanese-language analysis is not an ornamental section. It should be used where wording materially affects characterization, social position, emotional force, or interpretation.

### 13.1 Voice ledger

For each important speaker, track:

- self-reference and pronouns;
- names, surnames, kinship terms, and honorifics used for others;
- plain versus polite form;
- sentence-final particles and characteristic constructions;
- contractions, dialect, slang, and code-switching;
- commands, questions, hedges, and indirectness;
- ellipsis and unfinished statements;
- characteristic teasing or insult patterns;
- shifts under anger, fear, intimacy, exhaustion, or public performance.

The analytically important unit is often the **change** in voice, not the baseline trait.

### 13.2 Address-term matrix

Update a matrix of who calls whom what. A changed name, suffix, kinship term, or level of formality may indicate:

- greater intimacy;
- deliberate distance;
- performance for an audience;
- assertion of hierarchy;
- restored or disrupted identity;
- emotional leakage.

### 13.3 Social atmosphere vocabulary

Track recurring words and constructions concerning:

- **空気** and **空気を読む**;
- visibility, recognition, memory, and forgetting;
- normality and abnormality;
- dreams, futures, and possibility;
- pain, scars, bodies, and hearts;
- choice, waiting, going, returning, and home;
- adulthood, graduation, work, and responsibility.

Do not count words mechanically and call the result a theme. Use recurrence only when syntax, placement, or narrative function develops across scenes.

### 13.4 Translation-sensitive passages

Flag passages where an English rendering is likely to flatten:

- ambiguous subjects;
- gendered or age-coded speech;
- honorific relations;
- politeness used aggressively or tenderly;
- puns and title echoes;
- dialect as sincerity or self-concealment;
- the difference between “seeing,” “recognizing,” and “remembering” someone;
- the distinction between **かえで** and **花楓** or any comparable orthographic identity marker.

Provide concise translations only where needed and explain the interpretive consequence. Avoid long blocks of quotation.

## 14. Body, comedy, sexuality, and genre framing

*AoButa* uses romantic comedy, male focalization, fanservice, and sexual banter alongside serious material. Neither moral dismissal nor genre-excuse is sufficient.

For each consequential instance, ask:

- Who looks, describes, jokes, or touches?
- Is the description narrator-neutral or Sakuta-focalized?
- What is the target’s response?
- Is there reciprocal license, established intimacy, discomfort, coercion, or a status difference?
- Does the joke reveal trust, deflect vulnerability, establish control, objectify, or interrupt the scene’s emotional force?
- Does an illustration intensify, complicate, or contradict the prose framing?
- Would the same act be judged differently if performed by another character?
- Does the volume invite criticism, normalize the conduct, or leave its ethics unstable?

Keep separate judgments for comic effectiveness, character truth, erotic appeal, relational consent, and ethical legitimacy.

## 15. Place, season, objects, and ordinary life

The series’ coastal geography and everyday routines are part of its emotional architecture. Track locations and movement through them, including where relevant:

- Fujisawa, Enoshima, Shichirigahama, Kamakura, and transit routes;
- beaches, train platforms, classrooms, libraries, hospitals, homes, studios, and commercial spaces;
- weather, sea color, snow, daylight, and seasonal transitions;
- phones, messages, notebooks, photographs, clothing, food, gifts, and school materials.

Ask what a location permits that another forbids. A public platform, private apartment, empty beach, hospital room, or performance venue changes who may speak, witness, leave, or intervene.

Ordinary-life scenes require full analytical weight. Cooking, commuting, studying, shopping, caring for a cat, waiting for a call, or sharing a meal can demonstrate restored function, attachment, and chosen continuity more convincingly than an explicit thematic speech.

## 16. Thematic and philosophical modules

Select only modules materially activated by the current volume. Empty coverage is worse than focused analysis.

### 16.1 Recognition and social ontology

- What makes a person socially real?
- Can one witness preserve another’s existence?
- Is being seen the same as being known, believed, remembered, or valued?
- When does collective inattention become active harm?

### 16.2 Identity, memory, and personhood

- Is identity grounded in memory, body, name, relationships, commitments, or narrative continuity?
- Can restoration of one continuity constitute loss of another?
- Who has authority to name what has happened?

### 16.3 Care, sacrifice, and moral injury

- Is sacrifice freely chosen with adequate knowledge?
- Does one person’s life or future become an instrument for another?
- Does love create a right to intervene or a duty to refrain?
- How does survival produce guilt, debt, or responsibility?

### 16.4 Performance and authenticity

- Which selves are roles, and which roles become genuine through repetition?
- Does refusing the social atmosphere express authenticity or simply another performance?
- Can public and private selves coexist without one being declared false?

### 16.5 Adolescence and adulthood

- Is adulthood freedom, responsibility, compromise, economic dependence, or the loss of protected possibility?
- Do university, career, and public work resolve adolescent conflicts or relocate them?
- Does the category of “adolescence syndrome” expand, weaken, or become ironic as the cast ages?

### 16.6 Knowledge and belief

- What evidence justifies belief in another person’s impossible testimony?
- When is trust rational without public proof?
- How do altered memory and records affect responsibility?

### 16.7 Gender, fame, and legibility

- How do girls and young women experience appearance, comparison, sexualization, public ownership, and replaceability?
- How does male focalization reveal or obscure those experiences?
- Does celebrity intensify the same recognition problem ordinary students face, or create a categorically different one?

## 17. Illustration protocol

Inspect every illustration in context. For each materially important image, record:

- image filename or stable internal locator;
- adjacent scene and its position in the spine;
- characters, gaze, posture, distance, touch, costume, and setting;
- whose viewpoint the composition approximates;
- whether the image anticipates, repeats, or selectively freezes a moment;
- information added, omitted, eroticized, softened, or made ambiguous;
- whether the image aligns with Sakuta’s focalization or grants another character greater subjectivity.

Do not treat an illustration as proof of a thought or motive that the prose does not support. Do not ignore it merely because the prose can be read without it.

## 18. Evidence Classification Ledger

Every canonical volume artifact contains a compact evidence ledger for load-bearing claims.

Use the following evidence classes:

| Label | Meaning | Standard |
|---|---|---|
| **TF — Textual fact** | Directly stated or unambiguously shown | Recoverable from a precise source location |
| **SI — Strong inference** | Best explanation of converging evidence | Alternatives considered and materially weaker |
| **TI — Thematic / tentative interpretation** | Literary, psychological, ethical, or formal synthesis | Supported but not uniquely entailed |
| **CB — Character belief** | A proposition held or asserted by a character | Must not be promoted to objective fact without support |
| **UA — Unresolved ambiguity** | Evidence remains incomplete or incompatible | Must remain open within the current boundary |
| **FP — Prospective / foreshadowing signal** | Suggests a later development without establishing it | Cannot be converted into later certainty early |
| **RC — Retrospective correction** | Later analyzed evidence changes an earlier reading | Used only after the later source is analyzed |
| **VJ — Value judgment** | Explicit normative or critical evaluation by the analysis | Kept separate from descriptive fact |

Retain a second, optional epistemic-confidence axis when useful:

- **A — directly established**
- **B — strongly established**
- **C — strongly implied**
- **D — plausible inference**
- **E — speculation / theory**

This two-axis system is particularly useful in AoButa because a directly quoted Rio explanation may be **A-level evidence that Rio said it** while remaining only **C/D-level evidence that the proposed physical model is literally correct**.

Recommended row:

| ID | Location | Japanese anchor | Evidence/function | Class | Confidence | Tags |
|---|---|---|---|---|---|---|

Quotes should remain short and proportionate. The objective is retrievability, not reproduction of the novel.

## 19. Primary-Source Locator Ledger

Every load-bearing evidence entry should have a retrievable source locator.

For AoButa text EPUBs, record as many of the following as the edition permits:

1. volume and Japanese title;
2. chapter;
3. numbered subsection or scene marker when present;
4. EPUB spine index;
5. internal XHTML filename;
6. short exact Japanese anchor phrase;
7. illustration filename when applicable;
8. optional surrounding locator range;
9. verification note.

Recommended row:

| Evidence ID | Chapter/section | Spine item | XHTML | Japanese anchor | Illustration | Verification note |
|---|---|---:|---|---|---|---|

Never guess a locator from memory. If an older analysis contains a valid quotation but the exact spine item has not been reopened, record:

```yaml
locator_status: pending_backfill
```

A missing locator is an auditable gap. A fabricated locator corrupts the corpus.

### 19.1 Locator granularity

Not every observation needs line-level precision. Use the strongest practical locator for the claim:

- **exact dialogue/lexical claim:** exact Japanese anchor + chapter + XHTML/spine;
- **scene-level relational claim:** scene or subsection + one or more anchors;
- **illustration claim:** image filename + adjacent spine item;
- **chapter-architecture claim:** chapter boundaries and opening/closing spine items;
- **afterword claim:** afterword spine item + short anchor.

### 19.2 Multiple-source support

A major synthesis claim should ideally be supported by more than one evidence entry when the claim spans:

- several volumes;
- competing states/worlds;
- a character's long-term development;
- a translation-sensitive lexical pattern;
- or a contested ethical interpretation.

## 20. Multi-pass workflow for each volume

### Pass 0 — Integrity and structure audit

1. Confirm the EPUB opens and the spine is readable.
2. Map contents, chapters, subsections, illustrations, afterword, and extras.
3. Record edition and spoiler boundary.
4. Note formatting or extraction anomalies.

### Pass 1 — Spoiler-bound linear reading

Read in spine order without consulting later volumes. Capture:

- scene sequence;
- dates and locations;
- entrances and exits;
- promises, lies, confessions, refusals, and decisions;
- first manifestations of the phenomenon;
- emotional and linguistic shifts;
- provisional questions rather than premature answers.

### Pass 2 — Causal and formal reconstruction

Build:

- a concise causal synopsis;
- phenomenon dossier;
- time/state map if required;
- information-distribution map;
- opening/closing and chapter-architecture analysis;
- illustration notes.

### Pass 3 — Character, relationship, and voice reading

Update:

- central-character trajectories;
- Sakuta intervention audit;
- Mai continuity audit;
- relationship-state ledger;
- voice and address-term ledger;
- ensemble and institutional changes.

### Pass 4 — Thematic and ethical interpretation

Select the relevant modules from Sections 11–13. Test how the literal mechanism, social situation, and interpersonal choices interact. Separate:

- causal success;
- emotional success;
- ethical legitimacy;
- psychological plausibility;
- thematic force.

### Pass 5 — Adversarial rereading

Challenge the preferred thesis.

1. What evidence does it fail to explain?
2. Is a phenomenon being over-symbolized?
3. Is Sakuta’s view being mistaken for the novel’s whole view?
4. Is a character’s agency being minimized to preserve a rescue narrative?
5. Is scientific language being treated too literally or too dismissively?
6. Is romantic comedy obscuring a boundary problem?
7. Is later knowledge leaking backward?
8. Is an emotionally moving resolution being mistaken for a fully coherent one?
9. Is absence of adult action really established by the text?
10. Which alternative reading deserves to remain live?

### Pass 6 — Provenance audit

Before finalizing, verify that each load-bearing claim has an evidence classification and that every native-v2 evidence entry has a recoverable locator. Confirm source hashes and spine metadata, identify quotation-sensitive claims requiring primary-source reinspection, and mark unresolved locator gaps rather than guessing.

### Pass 7 — Cumulative delta

Conclude by stating exactly what the volume changes in the series-so-far model:

- new textual facts;
- revised character or relationship states;
- phenomenon rules confirmed, contradicted, or left open;
- new motifs and returned motifs;
- earlier claims strengthened or weakened without violating the spoiler boundary;
- open questions carried forward;
- evidence entries reserved for final synthesis.

## 21. Required cumulative ledgers

Maintain these across the entire reading project.

1. **Master chronology and calendar**
2. **Phenomenon case and rule ledger**
3. **State/world/memory ledger**
4. **Sakuta character and intervention ledger**
5. **Mai character and central-romance ledger**
6. **Ensemble character trajectory ledger**
7. **Relationship-state matrix**
8. **Japanese voice and address-term matrix**
9. **Institution and adult-responsibility ledger**
10. **Place, season, object, and motif index**
11. **Illustration ledger**
12. **Evidence ledger**
13. **Open-question and competing-hypothesis register**
14. **Strengths, limitations, and unresolved-tensions ledger**
15. **Primary-source locator index**
16. **Retrospective correction log**, activated only when later analyzed material warrants it

## 22. Required per-volume artifact structure

The default canonical artifact uses 21 analytical functions. Headings may merge when a novel's form makes that clearer, but the functions must remain recoverable.

```markdown
---
[YAML metadata]
---

# 『Japanese Volume Title』
## Volume N Deep Reading
### [Volume-specific interpretive subtitle]

## 1. Central thesis and volume role
## 2. Source integrity, edition, structure, and narrated sequence
## 3. Causal synopsis: what changes and why
## 4. Adolescence Syndrome / phenomenon dossier
## 5. Central character deep dive
## 6. Sakuta: focalization, intervention, cost, and development
## 7. Mai and the continuing central relationship
## 8. Ensemble and relationship-state changes
## 9. Japanese voice, address, and translation-sensitive language
## 10. Time, memory, dreams, worlds, and identity [when activated]
## 11. Institutions, adults, social atmosphere, and material conditions
## 12. Place, season, objects, ordinary life, and formal motifs
## 13. Illustrations and visual paratext
## 14. Ethics and philosophical implications
## 15. Counterreadings, limitations, and hypothesis stress-test
## 16. What this volume changes in the series-so-far model
## 17. Evidence Classification Ledger
## 18. Primary-Source Locator Ledger
## 19. Cumulative-ledger updates
## 20. Retrospective-correction status
## 21. Volume thesis and questions carried forward
```

Do not pad a quiet volume with artificial subsections. If functions are merged, note the merge explicitly. Complex volumes involving branch states, memory replacement, or nested future possibilities should expand beyond this template rather than compressing the evidence to fit it.

## 23. Library retrieval strategy

Canonical artifacts should be findable without exact filename recall. Each volume document should include:

- canonical filename;
- volume number and Japanese title;
- chapter titles;
- source filename;
- major character names in Japanese and common romanization;
- major relationship pairings;
- phenomenon type;
- key Japanese lexical anchors;
- important places and motifs;
- evidence IDs.

Useful retrieval queries should therefore work conceptually, for example:

```text
AOBUTA V01 空気 Mai recognition
AOBUTA V03 双葉 理央 自傷行為 花火
AOBUTA V05 かえで 今年の目標 学校
AOBUTA V06 翔子 心臓 将来スケジュール
AOBUTA V07 ふたりで幸せになる Tomoe observer
```

Metadata exists to make later synthesis and targeted primary-source reinspection cheap.

## 24. Raw-source cold storage and selective reintroduction

Once a volume has:

- a complete canonical deep-reading artifact;
- verified source metadata and checksum;
- a sufficiently populated Evidence Classification Ledger;
- a Primary-Source Locator Ledger;
- and short Japanese anchors for load-bearing findings,

the raw EPUB need not remain simultaneously active for every later synthesis task.

The raw Japanese novel remains the final authority. When a synthesis claim is contested, quotation-sensitive, mechanically complex, visually dependent, or unusually important:

1. retrieve the canonical analytical artifact;
2. identify the relevant evidence ID(s);
3. follow the locator(s);
4. selectively reintroduce the original EPUB;
5. verify the passage or illustration;
6. then write or revise the synthesis claim.

This permits the full fifteen-volume corpus and extras to remain auditable without requiring every raw file to be loaded at once.

## 25. Migration rule for Volumes 1–7

Volumes 1–7 were analyzed before the v2 provenance architecture became the governing output standard.

Their analytical conclusions should be preserved as historical first-pass artifacts rather than silently rewritten using later knowledge.

Migration procedure:

1. emit a canonical `AOBUTA_VXX_DEEP_READING.md` artifact for each existing analysis;
2. add YAML metadata and verified source-object information;
3. record the source SHA-256, spine count, and illustration count where available;
4. preserve the original spoiler boundary and first-pass conclusions;
5. do **not** fabricate exact evidence IDs, XHTML locators, or section locators from memory;
6. add a provenance note distinguishing a verbatim legacy export from a reconstructed archival migration;
7. mark locator backfill as `pending_backfill` or `partial` unless the original EPUB is deliberately reopened and audited;
8. if exact traceability later becomes necessary, backfill locators against the raw source without importing post-boundary knowledge into the historical interpretation.

Recommended metadata for a faithful but non-verbatim reconstruction:

```yaml
provenance_status: migrated_legacy_analysis_reconstructed
locator_status: pending_backfill
retrospective_material_imported: false
```

If an exact prior response is available verbatim, use instead:

```yaml
provenance_status: migrated_legacy_analysis_verbatim
```

Beginning with **Volume 8**, full v2 provenance should be native rather than retrofitted.

## 26. Quality-control checklist

Before finalizing each volume analysis, verify:

- [ ] The complete Japanese EPUB was read in spine order.
- [ ] Every illustration was inspected in context.
- [ ] The spoiler boundary is explicit and intact.
- [ ] The analysis distinguishes textual fact, inference, interpretation, and ambiguity.
- [ ] The plot section explains causal development rather than merely summarizing chapters.
- [ ] Literal phenomenon mechanics and metaphorical meaning remain distinct.
- [ ] Competing explanations and counterexamples are recorded.
- [ ] Sakuta’s focalization is not treated as omniscient narration.
- [ ] The title character retains agency beyond being rescued.
- [ ] Mai and the central romance are tracked even when another character supplies the title.
- [ ] Ensemble continuity and ordinary-life evidence are included.
- [ ] Japanese-language observations have an interpretive payoff.
- [ ] Scientific and clinical language is handled with appropriate caution.
- [ ] Sexual comedy and male gaze are assessed rather than ignored or mechanically condemned.
- [ ] Ethical judgment is separated from narrative effectiveness and emotional force.
- [ ] Time, memory, and state changes are internally consistent or explicitly unresolved.
- [ ] Major claims have retrievable EPUB locations and short Japanese anchors. For migrated pre-v2 artifacts, unresolved locator backfill is explicitly marked rather than fabricated.
- [ ] The volume’s weaknesses and resistant evidence receive serious treatment.
- [ ] The cumulative ledgers and open questions are updated.

## 27. Prohibited shortcuts and recurring failure modes

Avoid the following:

- reducing the series to “mental health problems visualized as supernatural events”;
- accepting quantum terminology as a complete scientific mechanism;
- dismissing all quantum terminology as meaningless without analyzing its narrative function;
- treating explicit clinical diagnoses and Adolescence Syndrome as interchangeable;
- equating memory restoration with an uncomplicated happy ending;
- treating each title character as disposable after her featured volume;
- converting every female relationship with Sakuta into romance or harem competition;
- assuming Sakuta’s sacrifice is justified because it succeeds;
- using Mai only as a jealous-girlfriend reaction function;
- overlooking scenes of women helping, correcting, or knowing one another independently of Sakuta;
- treating banter as transparent confession rather than a speech act with context;
- using adaptation imagery to fill gaps in the novel;
- overvaluing climactic speeches and undervaluing routine, silence, and aftermath;
- importing later world mechanics into an earlier volume;
- resolving contradictions through franchise memory;
- producing a long plot recap with thematic labels attached afterward.

## 28. Checkpoints and later full-series synthesis

At natural structural thresholds, produce a provisional synthesis that does not replace the volume analyses. A checkpoint should:

1. restate the strongest series-so-far thesis;
2. map character and relationship movement;
3. compare phenomenon cases without assuming one universal law;
4. audit Sakuta’s changing intervention ethic;
5. assess Mai and Sakuta’s movement toward adult partnership;
6. track how “adolescence” changes as the cast ages;
7. review recurring language, places, objects, and title patterns;
8. identify claims later evidence may overturn;
9. preserve a compact evidence map for the final multi-document synthesis.

After the full corpus is analyzed, conduct a distinct retrospective pass. Only then may later revelations be used systematically to reinterpret earlier volumes. Every revision should retain the earlier reading as historical evidence of how the series controlled information at the time.

Likely final synthesis domains include:

- series architecture and the transition from adolescence toward adulthood;
- Sakuta as focalizer, caregiver, rescuer, and risk-bearer;
- Mai as co-protagonist and the central romance as an ethical partnership;
- the ensemble and distributed networks of care;
- Adolescence Syndrome: phenomenology, metaphysics, explanatory models, and limits;
- identity, memory, counterfactual lives, and personal continuity;
- recognition, social atmosphere, media, school, medicine, family, and work;
- Japanese narration, character voice, titles, imagery, and recurring motifs;
- strengths, limitations, contradictions, and unresolved questions;
- volume-by-volume evidence ledger and retrospective correction log.

## 29. Final synthesis traceability

The eventual full-series synthesis should use a three-layer evidence architecture.

### Layer 1 — Reader-facing synthesis claim

Example:

> The series gradually shifts Sakuta from heroic substitution toward collaborative responsibility.

### Layer 2 — Canonical analytical artifacts

Example:

```text
AOBUTA_V03_DEEP_READING.md
AOBUTA_V06_DEEP_READING.md
AOBUTA_V07_DEEP_READING.md
```

### Layer 3 — Primary evidence

Example:

```text
AOBUTA_V07_E0XX
→ Chapter 3
→ spine item / XHTML locator
→ short Japanese anchor
→ original Japanese EPUB
```

For every load-bearing thesis, preserve at least one such chain. For disputed, translation-sensitive, or mechanically complex claims, preserve multiple independent chains.

The final corpus should permit movement:

> **synthesis → analysis → evidence ID → locator → Japanese primary source**

without reconstructing the path from memory.

## 30. Periodic synthesis and retrospective correction

Use natural structural thresholds rather than arbitrary fixed counts. Checkpoints should summarize:

- current series architecture;
- Sakuta's intervention ethic;
- Mai/Sakuta partnership state;
- ensemble-care network;
- current phenomenon models and counterexamples;
- state/world/memory bookkeeping;
- Japanese voice and address findings;
- institutions and adult responsibility;
- motifs, places, objects, and illustrations;
- strongest hypotheses and their counterevidence;
- open questions;
- and any RC entries activated by newly analyzed material.

A checkpoint never replaces the canonical volume artifacts. It is a synthesis layer above them.

## 31. Compact invocation prompt

Use the following prompt with this document and the next Japanese EPUB:

> Following *青春ブタ野郎シリーズ — Volume-by-Volume Analytical Method v2.0*, read the complete original-Japanese EPUB in spine order and produce the canonical `AOBUTA_VXX_DEEP_READING.md` artifact with YAML metadata, evidence classifications, primary-source locators, and the full literary deep dive. Preserve a strict spoiler boundary through the current volume; inspect all illustrations and paratext; distinguish textual fact, strong inference, tentative interpretation, and unresolved ambiguity; update every materially relevant cumulative ledger; and give special attention to Adolescence Syndrome phenomenology, Sakuta’s focalization and intervention ethics, Mai and the continuing central relationship, ensemble continuity, Japanese character voice, time/memory/state mechanics, social atmosphere, ordinary life, and evidence that resists the preferred thesis.

---

**Method status:** Governing protocol from Volume 8 forward. Volumes 1–7 are migrated under Section 25. Revise the version number only when the workflow itself changes; volume-specific discoveries belong in canonical volume artifacts, cumulative ledgers, retrospective corrections, and checkpoint syntheses rather than being silently folded into this base protocol.
