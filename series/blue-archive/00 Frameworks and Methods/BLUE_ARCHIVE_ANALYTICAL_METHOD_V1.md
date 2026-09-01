---
series: BLUE_ARCHIVE
artifact_type: analytical_method
scope: 'Japanese Blue Archive game narrative corpus: main, group, event, bond, mini, MomoTalk, character/profile/contextual dialogue'
generation: V1
status: canonical
source_boundary: Promoted Blue Archive V1 Japanese canonical corpus pinned to electricgoat/ba-data@jp cbe3fd623c2aab9e781ba0ce0483bc77c68bff86, with HePudding/ba-storybook@main 6c4091603ca76d7d8c3cdb9104933f52cd8cab8e as independent reference; canonical and derived builds passed blocking audits
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
created: 2026-08-15
updated: 2026-08-15
---

# BLUE ARCHIVE ANALYTICAL METHOD V1
## Japanese-primary literary, character, relational, institutional, and thematic analysis over the extracted game corpus

## 0. Purpose

This document governs analytical interpretation of **『ブルーアーカイブ -Blue Archive-』** using the Japanese transcript and narrative-data corpus produced by the Blue Archive extraction pipeline.

It is an **analysis protocol**, not an extraction protocol. The extraction specification governs how text is recovered, normalized, identified, audited, and projected. This method governs what an analyst may infer from those materials, how different source classes should be weighted, how chronological and relational claims should be constructed, and how later synthesis must preserve provenance.

The central methodological problem is that *Blue Archive* is not one continuous text. It is a live-service narrative distributed across multiple textual environments with different narrative functions:

- main story;
- group/club stories;
- event stories;
- bond stories;
- MomoTalk;
- mini stories;
- profile and contextual character dialogue;
- Sensei choices and internal narration;
- institutional and metadata tables that help resolve school, club, speaker, and playable-variant identity.

These materials are all useful, but they are **not interchangeable evidence**.

The governing rule is:

> **Read complete stories as stories. Read derived bundles as reversible analytical projections. Preserve the difference between public narrative, private relationship material, ordinary-life material, event-specific performance, and decontextualized character voice lines.**

A character should never be reconstructed from isolated lines when contextual scenes are available. A relationship should never be inferred from a MomoTalk line alone when the linked bond scene changes its meaning. An institution should never be defined only through profile metadata when the main story depicts how it actually operates. A Sensei choice should never be treated as simultaneously canonical with every alternative choice in the same branch group.

---

# 1. Source authority and evidentiary hierarchy

## 1.1 Primary technical authority

For the current corpus generation, the primary raw authority is the pinned Japanese branch of `electricgoat/ba-data`:

- branch: `jp`
- commit: `cbe3fd623c2aab9e781ba0ce0483bc77c68bff86`
- recorded game-data version: `v1.71.447596-r94_y2ha6vgythtil9ja597o`

The independent parser/reference snapshot is:

- `HePudding/ba-storybook@main`
- commit: `6c4091603ca76d7d8c3cdb9104933f52cd8cab8e`

The reference corpus is useful for cross-checking, structural comparison, and discrepancy detection. It is not automatically newer or more authoritative than the current pinned raw Japanese tables.

## 1.2 Analytical evidence ladder

When answering an interpretive question, use the narrowest sufficient layer while preserving authority:

1. **current analytical corpus map / authority state**;
2. **canonical complete story or sequential deep reading**;
3. **contextual scene bundle**;
4. **specialist character / relationship / institution synthesis**;
5. **derived indexes and ledgers**;
6. **structured utterance / choice / MomoTalk records**;
7. **raw source table record at pinned commit**.

For exact Japanese wording, ambiguity, speaker identity, choice structure, or disputed chronology, descend to the structured or raw layer.

## 1.3 Derived-projection authority rule

The promoted V1 source corpus now provides reversible analytical projections in addition to the 2,716 canonical story/data objects. Current source-side projections include 128 character packages, 2,718 measured relationship candidates with 40 selected relationship bundles, 47 club packages, 15 school packages, 128 Sensei relationship packages, seven main-arc maps, and LLM-oriented context chunks.

These are **retrieval accelerators, not literary authorities in themselves**.

Apply the following distinctions:

- `04_CHARACTER_BUNDLES` gathers a literary person's evidence; it does not constitute an interpreted character monograph.
- `05_RELATIONSHIP_BUNDLES` gathers complete scenes around measured co-occurrence; it does not prove intimacy, causality, importance, or a particular relationship thesis.
- `RELATIONSHIP_CANDIDATES.csv` measures features such as shared stories/scenes, adjacent turns, one-on-one scenes, school/club overlap, and Sensei presence. Its ordering is **evidence-density ranking**, not narrative-significance ranking.
- `06_CLUB_AND_SCHOOL_BUNDLES` provides membership and institutional context backed by master data; institutional meaning still requires story-level analysis.
- `07_SENSEI_RELATIONSHIP_BUNDLES` gathers student-Sensei evidence; it does not collapse choice-space Sensei, structural Sensei, and relational Sensei into one fully authored route.
- `08_LLM_INGEST` is a reversible chunking layer. When a chunk supports a claim, follow its stable IDs back to the complete canonical scene/story before treating the claim as settled.

A source-side filename such as `BA_RELATIONSHIP_HOSHINO__SHIROKO.md` must therefore never be confused with an analytical relationship synthesis. The former is an evidence projection; the latter is a human/LLM-adjudicated argument that must weigh chronology, source class, scene function, counterevidence, and longitudinal change.

## 1.4 Evidence classes

Every significant analytical claim should be classifiable as one of the following:

- **TEXTUAL FACT** — explicitly stated in recoverable Japanese text.
- **STRUCTURAL FACT** — established by source ordering, speaker/scene structure, source class, school/club metadata, or choice structure.
- **LINGUISTIC OBSERVATION** — grounded in pronouns, address terms, register, sentence endings, lexical habits, ellipsis, honorifics, speech rhythm, or repeated phrasing.
- **RELATIONAL INFERENCE** — a supported interpretation of attachment, dependence, rivalry, intimacy, distance, authority, trust, fear, or obligation.
- **INSTITUTIONAL INFERENCE** — an interpretation of school/club governance, legitimacy, power, norms, incentives, or political structure.
- **THEMATIC INTERPRETATION** — a higher-order claim about what an arc, character, relationship, or recurring motif means.
- **OPEN HYPOTHESIS** — plausible but not yet sufficiently established.
- **CONTRADICTED / REVISED CLAIM** — an earlier interpretation weakened or overturned by later evidence.

Do not present inference as textual fact.

---

# 2. Source-class hierarchy: what each layer is good for

## 2.1 Main story — primary sequential literary authority

The main story is the preferred source for:

- large-scale plot and chronology;
- Kivotos-wide political order;
- school conflicts and alliances;
- major character crises and transformations;
- Sensei's public role;
- institutional legitimacy and failure;
- recurring philosophical propositions;
- large-scale violence and ethical stakes;
- durable character developments that subsequent material presupposes.

Read main-story episodes sequentially. Do not reconstruct a main arc from character bundles alone.

A sequential deep reading should preserve the local information boundary at the point of first reading, while a later full-series synthesis may use hindsight. When hindsight changes the interpretation of an earlier scene, record the transition explicitly rather than pretending the earlier ambiguity never existed.

## 2.2 Group / club stories — institutional daily life

Group stories are especially valuable for:

- club identity;
- school culture;
- recurring routines;
- peer hierarchy;
- division of labor;
- ordinary conflict resolution;
- how members behave when the stakes are lower than a main-story crisis;
- institutional norms that main story may only imply.

Do not dismiss them as bonus comedy. In a setting where schools and clubs are political and social units, low-stakes institutional behavior is part of the world model.

## 2.3 Event stories — cross-sectional and continuity-bearing material

Events should be classified before interpretation:

- **core-continuity event** — materially changes a character, relationship, school, or recurring status quo;
- **important continuity-supporting event** — deepens established characterization or relationships without changing their central state;
- **situational / seasonal event** — valuable for voice and interaction but weak for longitudinal development;
- **primarily comic / promotional event** — useful selectively, not automatically discarded.

Event analysis must avoid two opposite errors:

1. treating every event as disposable;
2. treating every event premise as equally strong evidence for durable character state.

The analyst should ask whether later stories presuppose the event's consequences, whether relationships retain the change, and whether the event exposes a stable behavior pattern rather than a one-off gag.

### Event order and chronology

The promoted corpus preserves release/source ordering when upstream data exposes it, but the build audit explicitly leaves **in-universe chronology unresolved**. Therefore:

- do not equate file order, event ID, release order, or first/last co-occurrence fields with diegetic chronology unless the text establishes the sequence;
- distinguish **documentary order** (how the corpus or release history orders material) from **story-world chronology**;
- use later-state assumptions only when another source actually presupposes them;
- record chronology conflicts or uncertain placements as `OPEN` rather than forcing a total timeline.

The event corpus currently contains 490 promoted canonical event stories; nine rerun aliases were consolidated without losing contexts. Analytical event triage should target the canonical story object and preserve alias/release context where relevant.

## 2.4 Bond stories — private relational and self-presentational authority

Bond stories are disproportionately important for:

- private self-presentation;
- personal history;
- vulnerability;
- trust and affection toward Sensei;
- ordinary desires and insecurities;
- the difference between public role and private person;
- romantic or intimacy coding where present;
- how a student responds to adult attention, praise, teasing, reassurance, boundaries, and care.

They must not silently dominate the total character model. A student may reveal a private self with Sensei that is real but context-specific.

A mature profile should therefore distinguish:

> public/institutional self → peer-group self → crisis self → Sensei-private self → low-stakes ordinary self.

## 2.5 MomoTalk — low-pressure relational grammar

MomoTalk is not ordinary prose and should not be flattened into it.

It is particularly strong evidence for:

- who initiates contact;
- texting register;
- directness versus indirection;
- apology habits;
- concern and care language;
- scheduling and availability;
- comfort with requesting help;
- how students address Sensei outside formal scenes;
- the transition from message to bond-story encounter where established.

Message boundaries, alternative Sensei replies, and thread structure are analytically meaningful.

MomoTalk should often be read as the **relational preface** to a bond scene, not as a substitute for that scene.

## 2.6 Character/profile/contextual dialogue — linguistic and persona evidence

Profile and contextual lines are excellent for:

- first-person pronouns;
- address terms;
- recurring sentence endings;
- lobby register;
- battle/formation register;
- seasonal language;
- self-description;
- repeated motifs and catchphrases;
- differences between playable variants of the same literary person.

They are weaker for:

- chronological development;
- causal narrative claims;
- precise relationship progression;
- claims that require a fully staged interaction.

Treat profile blurbs as **official descriptive metadata**, not omniscient literary proof that overrides the character's behavior in stories.

## 2.7 Mini stories

Mini stories receive the same evidence discipline as event/group stories. Their short form does not make them unimportant, but compact premises should not carry disproportionate interpretive weight without corroboration.

---

# 3. Person identity, playable variants, and literary continuity

The extraction correctly distinguishes **literary persons** from **playable variants**. Analysis must preserve that distinction.

A swimsuit, dress, alternate equipment, seasonal, or other playable form is not automatically a separate literary character. Variant-specific dialogue may, however, preserve a specific narrative context or emotional register.

For each character analysis:

1. begin from the literary-person registry;
2. inspect the variant crosswalk;
3. retain variant IDs in evidence locators;
4. ask whether a line is variant-contextual or person-general;
5. never merge contradictory variant contexts without explanation.

When a variant represents a specific event or later state, treat it as evidence from that context rather than as timeless personality data.

Unresolved person mappings and unresolved speaker labels must remain visible. Do not repair them from memory.

---

# 4. Sensei as a special analytical problem

Sensei is simultaneously:

- player-facing viewpoint;
- named institutional officeholder;
- adult authority figure;
- relational partner to many students;
- participant in dialogue choices;
- sometimes narrator or internal thinker;
- ethical and political actor.

This requires unusual discipline.

## 4.1 Choice alternatives

If a choice object contains multiple replies, the analyst may say:

- the scene permits Sensei to respond within a certain behavioral range;
- both choices characterize the designed player/Sensei possibility space;
- the student's post-choice response may reveal what the script is prepared to absorb.

The analyst may **not** say that Sensei canonically spoke every alternative.

When different choices converge to the same next line, note that the game may be characterizing a bounded persona rather than meaningful branching causality.

## 4.2 Sensei characterization

Build Sensei's character from recurring invariants across choices and stories:

- willingness to intervene;
- adult responsibility;
- use of institutional authority;
- willingness to trust students;
- humor and teasing;
- ethical boundaries;
- readiness to accept danger or cost;
- how students themselves consistently describe Sensei.

Separate:

- **choice-space Sensei** — all responses the game allows;
- **structural Sensei** — actions and commitments the narrative requires;
- **relational Sensei** — how particular students experience and address the adult.

## 4.3 Adult/student relation

Because Sensei is an adult in authority and the students are adolescents, relationship analysis should distinguish:

- trust;
- dependency;
- mentorship;
- care;
- affection;
- flirtation or romantic coding;
- institutional responsibility;
- boundary negotiation.

Do not collapse all intimacy into romance, and do not erase romantic coding where the text clearly supplies it. Describe what the source supports and preserve the asymmetry of role and age as part of the interpretation.

---

# 5. Character deep-reading protocol

A mature character monograph should be produced only after a minimum evidence threshold is met.

## 5.1 Minimum source coverage

For a major character, inspect where available:

1. all main-story appearances;
2. relevant group/club stories;
3. continuity-bearing events;
4. bond stories;
5. MomoTalk;
6. character/profile/contextual dialogue;
7. major relationship bundles;
8. school/club institutional bundle;
9. source gaps and unresolved speaker mappings affecting that character.

## 5.2 Required analytical dimensions

A character analysis should address:

- core contradiction;
- explicit goals;
- implicit needs;
- fears, wounds, shame, or unresolved obligations;
- self-concept versus others' perception;
- public role versus private behavior;
- competence and failure modes;
- ethics and use of power;
- humor and ordinary life;
- relationship to school/club;
- relationship to Sensei;
- significant peer relationships;
- Japanese voice/register;
- longitudinal development;
- contradictions and counterevidence;
- source-class dependence of each claim.

## 5.3 Ordinary behavior before crisis interpretation

Before interpreting a crisis reaction as the character's essence, establish ordinary behavior where possible.

The corpus architecture deliberately supplies low-stakes MomoTalk, group, bond, and contextual lines for this reason.

A useful comparison is:

> baseline behavior → institutional behavior → pressured behavior → crisis behavior → post-crisis behavior.

This protects against defining a person only by their most dramatic scene.

---

# 6. Relationship analysis protocol

Relationship documents should be generated selectively, not combinatorially.

Create a dedicated relationship artifact when at least one is true:

- the relationship drives a main-story arc;
- it changes both characters materially;
- it accumulates evidence across several source classes;
- it is necessary to understand a school/club;
- it has a distinct ideological or emotional problem;
- it is repeatedly referenced after the initiating story.

For each relationship track:

- origin / first meaningful contact;
- initial asymmetry;
- recurring relational grammar;
- conflict pattern;
- care language;
- trust and disclosure;
- rivalry or hierarchy;
- major rupture;
- repair or redefinition;
- ordinary-life afterstate;
- linguistic markers such as address-term changes;
- Sensei's mediating role where applicable.

Do not treat co-occurrence as relationship evidence. Preserve scene context.

## 6.1 Machine-measured relationship candidates

The source corpus now measures 2,718 person-pairs and emits 40 selected scene bundles. These are valuable for recall, but the metrics cannot decide which relationships deserve analytical priority.

When using a candidate row or selected bundle:

1. treat `shared_stories`, `shared_scenes`, `direct_adjacent_turns`, and `one_on_one_scenes` as **descriptive corpus features**, not emotional-strength scores;
2. inspect the actual scenes, because ensemble scenes can create high co-occurrence without a strong dyadic relationship;
3. do not treat `first_cooccurrence` or `last_cooccurrence` as proven origin/end points when in-universe chronology is unresolved;
4. examine scenes without Sensei separately from Sensei-mediated scenes when the distinction matters;
5. promote a pair to the analytical relationship ledger only after narrative significance is adjudicated.

This means a low-ranked pair can be analytically central, while a high-ranked same-club pair can be mostly structural co-presence.

---

# 7. School, club, and institutional analysis

Kivotos is structurally unusual: schools are not mere campuses, and clubs can function as political, military, administrative, disciplinary, economic, or quasi-governmental institutions.

Institutional analysis should therefore track:

- formal authority;
- practical authority;
- legitimacy;
- resource control;
- armed capacity;
- internal factions;
- norms and rituals;
- member recruitment and belonging;
- conflict-resolution mechanisms;
- relationship to Sensei / Schale;
- relationship to other schools;
- treatment of dissent;
- institutional memory;
- crisis behavior;
- gap between stated purpose and actual function.

Avoid importing real-world political categories too mechanically. Use them comparatively, not as replacements for the fictional institution's own structure.

The promoted school layer currently contains 15 master-data-backed school packages, including crossover/external-school labels and an `ETC` category. **Source affiliation is not the same thing as core Kivotos institutional importance.** Before using a school package in worldbuilding synthesis, classify whether it is:

- a core Kivotos institution;
- a crossover/external institution;
- a miscellaneous/technical grouping; or
- unresolved.

Generic group labels also remain a non-blocking source ambiguity. Do not infer a club's canonical Japanese name from a generic script-group identifier when master data does not resolve it.

---

# 8. Violence, absurdity, and tonal duality

*Blue Archive* frequently combines lethal-looking weaponry, extreme violence, slapstick durability, school comedy, political crisis, grief, and intimate emotional drama.

The method must not resolve this tension prematurely by assuming either:

- "nothing matters because everyone is durable," or
- "every firearm scene should be interpreted exactly like real-world lethal violence."

Instead track:

- what characters themselves fear;
- what injuries or threats have durable consequences;
- when violence is framed comically versus traumatically;
- when institutions treat violence as routine;
- when the story invokes death, disappearance, sacrifice, or irreversible harm;
- whether the tonal register changes around the same action.

The question is not merely "how dangerous are guns in Kivotos?" but also:

> **What does the setting normalize, what does it still treat as morally exceptional, and what does that difference reveal about childhood, authority, institutional life, and protection?**

---

# 9. Japanese-language analysis

Japanese speech is a first-class evidentiary layer, not decorative flavor.

Track where useful:

- 私 / 私たち / 僕 / 俺 and other self-reference;
- 先生 and other address terms;
- honorifics;
- school/club titles;
- polite/plain shifts;
- sentence-final forms;
- contractions and slang;
- dialect or stylization;
- formality under stress;
- feminine/masculine/neutral fictional speech coding;
- repeated lexical fields;
- hesitation, ellipsis, stammering, and self-correction;
- written-message register versus spoken register.

Do not infer personality from one marker in isolation. Prefer repeated patterns and context shifts.

When translation would erase a meaningful distinction, preserve the Japanese form and explain it.

---

# 10. Sequential reading and hindsight discipline

## 10.1 First-pass local reading

For each major main-story unit, create a deep reading at the source boundary of that unit. It should record:

- what is known now;
- what remains ambiguous;
- current character states;
- institutional state;
- open hypotheses;
- motifs and callbacks visible at that point;
- claims to test later.

## 10.2 Later rereading

When later material changes an earlier interpretation, use the project-wide claim-transition vocabulary:

**PRESERVE · STRENGTHEN · REVISE · DOWNGRADE · REJECT · OPEN**

A later revelation should not erase the fact that the earlier text was designed to be ambiguous.

## 10.3 Checkpoints

At natural main-story arc boundaries, create checkpoints that summarize:

- character-state changes;
- school/club state changes;
- relationship changes;
- institutional/political developments;
- Sensei's role;
- unresolved questions;
- major claims revised since the previous checkpoint.

---

# 11. Evidence and locator requirements

Every analytical artifact should be traceable to the extraction corpus.

Preferred route:

> analysis claim → canonical story / contextual bundle → stable scene or utterance/choice ID → normalized structured record → raw table record → source path → pinned commit

When exact locators are available, use identifiers such as:

`BA:main:1:1:1:scene:001:u:0008`

or the corresponding bond, event, MomoTalk, or character-data ID.

Do not invent page numbers or prose-style quotations detached from the extracted locator system.

---

# 12. Contradiction and counterevidence protocol

Blue Archive's size makes confirmation bias particularly dangerous. Character bundles can make any desired thesis look true if contrary scenes are ignored.

For every major character or thematic synthesis:

1. state the strongest thesis;
2. identify at least one plausible competing reading;
3. search for counterexamples across other source classes;
4. distinguish contradiction from context-dependent behavior;
5. downgrade claims that rely on one exceptional scene;
6. leave unresolved tensions unresolved when the text does.

A good synthesis should explain why apparently inconsistent behavior belongs to one person rather than smoothing the person into a single adjective.

---

# 13. Live-service continuity and update behavior

The source corpus will change.

Analytical artifacts should therefore state a source boundary and generation. A later raw commit does not silently alter the authority of an earlier analysis.

When new material arrives:

- update current-state files in place;
- update mutable longitudinal ledgers;
- add new sequential readings;
- revise specialist syntheses only when their semantic responsibility changes;
- record claim transitions;
- preserve frozen releases;
- do not create duplicate `updated`, `new`, or `final-final` artifacts.

Major synthesis should be regenerated only when enough new story material has accumulated to change the work's state meaningfully.

---

# 14. Analytical phase sequence

## Phase 0 — Extraction review and source lock

Before literary analysis begins at scale:

- confirm the pinned source commits;
- read the extraction coverage report;
- inspect known gaps;
- inspect unresolved speakers/person mappings;
- verify that canonical bulk generation has actually been promoted beyond inspection samples;
- record source classes currently safe for analysis.

**Current status after the V1 promotion audit:** Phase 0 is closed for bulk analysis. The canonical build (`BA_FULL_20260816T002743Z`) and derived build (`BA_DERIVED_20260816T010224Z`) both report `PASS`. Stable-ID uniqueness, 8,774/8,774 choice preservation, sampled provenance round-trip, coverage regression, required derived bundle classes, deterministic sharding, and sampled derived provenance all passed. Phase 1 may begin.

The remaining source ambiguities are non-blocking but analytically visible: seven unknown timing/control records, unresolved overarching Japanese event titles in the raw localization tables, some generic group-label resolution, unresolved person/speaker mappings from the source lock, and unresolved in-universe chronology.

## Phase 1 — Main-story sequential reading

Read main story in canonical order and emit one deep-reading artifact per stable episode/chapter unit chosen by the synthesis architecture.

## Phase 2 — Arc checkpoints and longitudinal ledgers

Maintain cumulative character, relationship, institution, Sensei, language, motif, and claim-revision ledgers.

## Phase 3 — Contextual backfill

After a character or institution becomes materially important, incorporate relevant group, event, bond, MomoTalk, and character-data layers.

This prevents supplemental material from spoiling or predetermining the first sequential reading while still allowing mature character reconstruction later.

## Phase 4 — Specialist synthesis

Produce character monographs, relationship studies, institutional studies, Sensei analysis, language analysis, and thematic syntheses when evidence density justifies independent retrieval.

## Phase 5 — Full-series / current-era synthesis

Because the game remains live, prefer a **current-era synthesis** over pretending the work is complete. State the exact source boundary and unresolved future-facing questions.

## Phase 6 — Release and archival controls

When a synthesis generation is declared stable:

- freeze it;
- generate a manifest;
- preserve checksums;
- move superseded materially distinct artifacts to legacy;
- route future corrections through a new release generation.

---

# 15. Prohibited analytical shortcuts

Do not:

- treat the current extraction as bulk-complete while its own state map says otherwise;
- use the older human-readable reference as automatically current;
- flatten all source classes into one chronology;
- treat all Sensei choices as simultaneously spoken;
- treat every playable variant as a separate person;
- ignore variant context after person consolidation;
- infer missing Japanese text from another-language localization;
- invent event titles or school/club assignments;
- use isolated character lines as substitutes for contextual scenes;
- define a character only through bond material;
- define a school only through metadata;
- equate every affectionate Sensei interaction with romance;
- erase romantic coding merely because the source is structurally player-facing;
- treat comedic violence and irreversible violence as automatically identical;
- assume event stories are either all core or all disposable;
- silently harmonize contradictions;
- cite a derived bundle as though it were the original source when a stronger locator is available.

---

# 16. Standard deep-reading output contract

A canonical sequential reading should normally contain:

1. source boundary and provenance;
2. story placement and local chronology;
3. concise narrative reconstruction;
4. central thesis;
5. scene-by-scene analytical reading;
6. character-state updates;
7. relationship-state updates;
8. school/club/institutional state;
9. Sensei role and choice-space observations;
10. Japanese-language observations;
11. motifs, symbols, and recurring formulations;
12. violence/ethics/power analysis where relevant;
13. competing interpretations and counterevidence;
14. cumulative ledger deltas;
15. open questions;
16. evidence locators.

The goal is not maximum length. The goal is enough structure that later synthesis can recover **what changed, why we believed it, how confident we were, and where the source evidence lives**.

---

# 17. Governing analytical principle

*Blue Archive* should be analyzed as a **multi-layered social world**, not as a pile of character quotes and not as a single linear visual novel.

The strongest method is therefore:

> **Sequential story first; contextual projection second; longitudinal comparison third; specialist synthesis only after source-class triangulation.**

That order preserves literary causality while exploiting the unusual richness of the extracted corpus: public crises, institutional routines, private bond scenes, messaging behavior, voice/register data, and a reversible path back to the exact Japanese source record.
