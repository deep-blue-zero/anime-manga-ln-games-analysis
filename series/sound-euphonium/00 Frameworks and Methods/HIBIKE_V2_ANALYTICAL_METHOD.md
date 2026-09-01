---
series: HIBIKE
artifact_type: analytical_method
scope: FULL_V2
media: Japanese light novels
generation: V2
status: active_provisional
source_boundary: "Locked core Japanese prose corpus HIBIKE-V01 through HIBIKE-V14; supplements governed by HIBIKE_SOURCE_LOCK.md"
supersedes: null
superseded_by: null
do_not_use_as_current_authority: false
---

# Sound! Euphonium V2 — Analytical Method

## 1. Purpose

This document governs the second-pass literary analysis of Takeda Ayano's *Sound! Euphonium* prose corpus.

V2 is not a cleanup pass whose purpose is to reproduce the V1 conclusions against prettier text. V1 already established a substantial literary account of the series: private desire becoming audible inside collective life; merit as necessary but incomplete; Kitauji as an institution with memory; relational asymmetry; the ethical difficulty of wanting; and Kumiko's movement from perception toward speech, intervention, leadership, and transmission. V1 also recognized that speech register is character evidence, that the anthology volumes reveal truths inaccessible to Kumiko's focalization, and that musical merit arises from unequal material preconditions.

The V2 task is therefore different:

> **Verify, refine, revise, and extend the V1 literary model from clean Japanese primary text while building evidence infrastructure strong enough to support high-confidence character, relationship, linguistic, institutional, and predictive behavioral modeling.**

V2 has five simultaneous goals:

1. establish a clean Japanese-primary textual foundation suitable for close linguistic analysis;
2. repeat the sequential reading without allowing V1 to erase volume-local ambiguity;
3. test V1's major theses rather than assuming them;
4. systematically capture dimensions V1 treated only intermittently, especially voice, behavior, focalization, ordinary-life characterization, embodiment, regional language, material opportunity, and musical pedagogy;
5. produce source-traceable longitudinal evidence suitable for later character monographs and full-series synthesis.

---

## 2. Authority and source hierarchy

### 2.1 Governing primary source

The governing evidence is the **original Japanese prose** in verified digital editions admitted by the V2 source lock.

Clean EPUB text is preferred because the V1 corpus repeatedly classified its OCR as reading-grade rather than quotation-grade. V2 should therefore avoid OCR whenever a legitimate digital text exists.

For every admitted book, Phase 0 must preserve:

- exact Japanese title;
- edition/publication metadata;
- filename and stable corpus identifier;
- file hash;
- chapter/section structure;
- text completeness;
- illustration and paratext inventory where present;
- any known digital-edition differences;
- stable locator strategy.

### 2.2 Provisional source boundary

The V1 baseline covers ten numbered analytical units: the opening trilogy, two interstitial/short-story volumes, the two-volume second-year movement, the later short-story collection, and the two-volume final movement.

V2 must **not silently assume that this is the complete desirable prose corpus**. Before source lock, perform a bibliographic and corpus audit for official Japanese supplemental prose, side stories, retailer/bonus fiction, guide/interview material, or later material relevant to the literary and character-modeling objectives. Items should be admitted or excluded explicitly.

No supplemental item becomes governing evidence merely because it exists. Record why it is:

- core canonical prose;
- supplementary canonical prose;
- paratext;
- adaptation-only evidence;
- promotional evidence;
- or excluded/outside scope.

### 2.3 V1 status

The V1 volume analyses and full-series synthesis are **historical analytical evidence**, not V2 primary evidence.

Use V1 as:

- a hypothesis generator;
- an index of scenes worth rechecking;
- a record of prior interpretation;
- a revision target;
- and provenance for how the project evolved.

Do not use V1 to settle a disputed wording when the Japanese primary text is available.

### 2.4 Adaptation boundary

The novel project is prose-primary. Anime, films, performance audio, promotional art, or adaptation-specific staging must not be imported into the novel analysis without explicit labeling.

A later adaptation-comparison layer may be valuable, but novel character models must first be reconstructable from novel evidence alone.

---

## 3. Epistemic categories

Every consequential claim should be classifiable as one of the following.

### A. Direct textual fact

Explicitly stated action, dialogue, narration, chronology, physical fact, or institutional fact.

### B. Focalized observation

Something a viewpoint character perceives or reports. This is evidence of what the focalizer sees, not automatically objective truth.

### C. Character interpretation

A character's explanation of another person, herself, an event, or a relationship. It is evidence of the interpreter's model and may also be factually correct, partially correct, or wrong.

### D. Narrative-pattern inference

An inference strongly supported by repeated textual structure, contrast, motif, or longitudinal recurrence.

### E. Analytical inference

A defensible interpretation that goes beyond explicit statement. It must identify its evidentiary basis and should remain revisable.

### F. Paratextual support

Author interviews, guide material, editorial text, cover/illustration emphasis, or other paratext. Paratext may clarify design history but does not erase textual ambiguity.

### G. Open / underdetermined

The evidence does not justify choosing among live interpretations.

A mature V2 artifact should make the boundary between these categories legible, especially for character psychology and relationship claims.

---

## 4. Locator standard

Each quoted or high-leverage primary-source observation should be recoverable through a stable locator.

Preferred locator grammar:

`HIBIKE-VXX / chapter-or-story / EPUB section or XHTML file / paragraph-or-anchor / short Japanese cue`

If the EPUB provides stable internal anchors, retain them. If not, create deterministic paragraph numbering during corpus normalization and maintain a crosswalk to the source XHTML/spine order.

Do not rely on a search-only locator such as "the scene where Kumiko talks to Reina." The evidence layer should allow another reader to recover the passage without semantic guesswork.

For short quotations used to characterize voice, preserve exact Japanese punctuation and orthography from the locked text.

---

## 5. V2 reading philosophy

### 5.1 Full-series hindsight without hindsight contamination

V2 may use knowledge of later developments to recognize setup, recurrence, and revision. It must not rewrite an earlier character as though she already possessed later knowledge or maturity.

Each sequential reading should therefore distinguish:

- **local truth:** what can reasonably be concluded at this point in the series;
- **retrospective significance:** what later material allows us to notice;
- **do-not-backport:** later information that would distort the earlier state if treated as already known.

### 5.2 Preserve contradiction

V1 correctly observed that growth in this series does not purify personality. Reina can learn and remain severe. Kanade can reject self-sabotage and remain calculating. Asuka can become more available and remain theatrical. Kumiko can become more empathetic and more strategically capable of managing people.

V2 should record **stable tendencies plus changed regulation**, not replace an earlier trait with its opposite.

### 5.3 Relationship plurality

Two people may sincerely inhabit different versions of the same relationship. V2 should not collapse dyadic disagreement into a search for the one "real" interpretation unless the text resolves it.

For important dyads, record:

- A's understanding of the bond;
- B's understanding of the bond;
- observable behavior;
- asymmetries;
- contested meanings;
- and how those components change over time.

### 5.4 Institution as character environment

Kitauji is not background. Track institutional rules, leadership practice, audition logic, rehearsal culture, reputation, inherited narratives, distributed labor, faction formation, and how students interpret legitimacy.

Character behavior often cannot be understood outside this institutional field.

---

## 6. Phase 0 — source establishment

No sequential V2 volume reading begins until Phase 0 is sufficiently complete.

### 6.1 Source inventory

Create `HIBIKE_SOURCE_INVENTORY.md` containing:

- every candidate Japanese prose source;
- edition and publication data;
- source type;
- completeness status;
- text/illustration status;
- V1 correspondence;
- V2 admission recommendation;
- unresolved corpus questions.

### 6.2 EPUB integrity audit

For each clean EPUB:

- verify it opens and parses cleanly;
- inspect OPF/spine order;
- verify chapter titles and order;
- count/document XHTML content files;
- confirm front/back matter boundaries;
- confirm Japanese text is native text rather than embedded page images;
- spot-check ruby, punctuation, emphasis, vertical-writing markup, and unusual characters;
- detect obvious missing sections or duplicated chapters;
- inventory illustrations and their sequence;
- hash the original file;
- retain an immutable source copy.

### 6.3 V1-to-V2 text crosswalk

Build `HIBIKE_V1_OCR_TO_V2_TEXT_CROSSWALK.md` for the V1 material where useful.

The crosswalk should identify:

- corresponding V1 analytical unit;
- V1 source/OCR limitations;
- V2 edition correspondence;
- major pagination/section differences;
- passages whose exact wording materially affects an old claim.

### 6.4 Source lock

Create `HIBIKE_SOURCE_LOCK.md` only after the core corpus is stable enough to prevent accidental source drift.

The source lock should distinguish:

- locked core;
- locked supplements;
- deferred/unavailable items;
- excluded sources;
- optional adaptation-comparison sources.

---

## 7. Sequential volume workflow

Each volume reading uses the following passes.

### Pass 1 — structural orientation

Establish:

- title and publication role;
- chapter/story architecture;
- chronology;
- viewpoint/focalization structure;
- major setting shifts;
- public institutional movement;
- relation to the previous volume;
- obvious formal devices.

Do not begin by forcing the volume into the V1 thesis.

### Pass 2 — scene-level literary reading

For each major scene, record:

- external action;
- active desires;
- conflict structure;
- what each participant believes is happening;
- information asymmetry;
- shifts in power or intimacy;
- consequential wording;
- unresolved ambiguity.

### Pass 3 — character-state extraction

For every recurring character with material evidence, collect:

- goals and priorities;
- fears/shame triggers;
- attention biases;
- assumptions about others;
- default coping strategies;
- conflict behavior;
- care behavior;
- authority response;
- jealousy/competition behavior;
- humor/play behavior;
- self-description versus observed behavior;
- changes from prior state;
- negative evidence against an existing model.

This pass feeds the character-state ledger and later monographs.

### Pass 4 — Japanese voice and register

Capture exact language evidence for:

- first-person reference;
- second-person reference and forms of address;
- honorific choice;
- standard Japanese versus Kansai/regional features;
- sentence-final particles and endings;
- hedges;
- intensifiers;
- ellipsis and unfinished speech;
- repetition;
- exclamations/interjections;
- laughter and written vocal gestures;
- directness versus circumlocution;
- average turn length qualitatively;
- formal/casual switching;
- joking, sarcasm, teasing, and deadpan patterns;
- speech under anger, embarrassment, grief, excitement, authority, and intimacy.

For viewpoint characters, separately model **internal narrative language** and **spoken language**.

### Pass 5 — relationship-state extraction

Update important dyads and group relationships.

Record:

- closeness;
- trust;
- power;
- perceived obligation;
- address terms;
- permitted teasing;
- disclosure depth;
- characteristic conflict;
- repair behavior;
- physical/social proximity;
- exclusivity/jealousy where evidenced;
- mismatched interpretations.

### Pass 6 — music, embodiment, and pedagogy

V1 was strongest when treating music symbolically and institutionally. V2 should add more attention to music as embodied practice.

Track:

- instrument technique when textually described;
- breathing;
- posture;
- embouchure or physical strain where relevant;
- rehearsal language;
- listening behavior;
- section teaching;
- correction style;
- conductor/student communication;
- ensemble balance;
- practice routines;
- auditions as situated judgments rather than abstract rankings;
- how characters hear versus how they are heard.

### Pass 7 — ordinary life, humor, and embodiment

Low-stakes scenes are high-value character evidence.

Track:

- food and eating behavior;
- walking and commuting;
- phone/message habits;
- jokes;
- teasing;
- boredom;
- casual complaints;
- grooming/clothing awareness;
- personal-space behavior;
- gestures;
- eye contact;
- nervous habits;
- how characters behave when nothing dramatic is required of them.

A character model built only from crisis scenes will overproduce crisis behavior.

### Pass 8 — focalization and epistemic audit

Ask:

- Who knows this?
- Who merely thinks this?
- What does the focalizer miss?
- What becomes visible when another character narrates?
- Is the narration reporting behavior, interpreting behavior, or retrospectively framing it?

The anthology volumes receive especially close treatment because V1 already demonstrated that outside viewpoints materially revise how Kumiko and other central figures appear.

### Pass 9 — material, family, regional, and social conditions

Track without forcing a totalizing socioeconomic thesis:

- family expectations;
- money and access where the text supports it;
- private instruction;
- instrument ownership/access;
- practice space;
- university/career costs;
- geographic mobility;
- regional rootedness or rootlessness;
- dialect/register as social positioning;
- school prestige and prior training;
- unequal starting conditions beneath merit judgments.

The purpose is to explain conditions of agency, not to reduce every outcome to class.

### Pass 10 — V1 revision audit

At the end of the volume, compare the V2 reading with the corresponding V1 artifact.

Every material V1 claim should receive one of:

`PRESERVE`, `STRENGTHEN`, `REVISE`, `DOWNGRADE`, `REJECT`, `OPEN`.

Do not change a claim merely to make V2 look new.

### Pass 11 — volume synthesis and ledger update

Emit `HIBIKE_VXX_DEEP_READING.md` and update all relevant cumulative ledgers.

---

## 8. Standard sequential artifact structure

Each `HIBIKE_VXX_DEEP_READING.md` should normally contain:

1. YAML authority metadata
2. Source/edition note and locators
3. Executive local thesis
4. Structural/chapter map
5. Volume-local dramatic movement
6. Scene-level close reading
7. Character-state changes
8. Relationship-state changes
9. Japanese voice/register findings
10. Focalization and narration
11. Music/rehearsal/pedagogy
12. Institution and legitimacy
13. Ordinary-life/embodiment evidence
14. Family/material/regional conditions
15. Motifs/form/paratext where relevant
16. V1 claim revision table
17. Open questions / hypotheses
18. Cumulative delta
19. Evidence locator appendix or links to ledger entries
20. Next architecture-defined step

Do not create sections with no meaningful evidence simply to satisfy symmetry.

---

## 9. Longitudinal ledgers

V2 should maintain, at minimum:

### `HIBIKE_CHARACTER_STATE_LEDGER.md`
Longitudinal state changes, stable traits, contradictions, knowledge boundaries, and behavioral evidence.

### `HIBIKE_VOICE_REGISTER_LEDGER.md`
Japanese linguistic evidence by character, addressee, situation, and volume.

### `HIBIKE_RELATIONSHIP_STATE_LEDGER.md`
Dyadic and group relationship evolution with asymmetric interpretation preserved.

### `HIBIKE_BEHAVIOR_GESTURE_LEDGER.md`
Ordinary habits, embodiment, physical responses, stress behavior, humor, and nonverbal interaction.

### `HIBIKE_INSTITUTIONAL_STATE_LEDGER.md`
Leadership, rules, auditions, rehearsal culture, factional pressure, legitimacy, and institutional memory.

### `HIBIKE_MUSIC_PEDAGOGY_PERFORMANCE_LEDGER.md`
Musical practice, teaching, correction, listening, rehearsal, audition, and performance evidence.

### `HIBIKE_V1_CLAIM_REVISION_LEDGER.md`
Authoritative V1→V2 claim transitions.

These ledgers are mutable working infrastructure until the V2 release is frozen.

---

## 10. Natural checkpoint cadence

Checkpoint around the literary movements already visible in V1 rather than every arbitrary number of files.

Recommended cadence:

- `HIBIKE_V01-V03_CHECKPOINT.md` — desire, conflict, and claimed agency;
- `HIBIKE_V04-V05_CHECKPOINT.md` — countermelody, private lives, artistic authorship;
- `HIBIKE_V06-V07_CHECKPOINT.md` — second-year fairness, social legitimacy, asymmetry, defeat;
- `HIBIKE_V08_CHECKPOINT.md` — institutional memory, alternate viewpoints, post-mainline lives;
- `HIBIKE_V09-V10_CHECKPOINT.md` — leadership, legitimacy, plural motive, transmission.

A checkpoint should freeze the best current interpretation for its boundary while preserving open questions for later volumes.

---

## 11. Major V1 theses to test, not assume

V2 should deliberately test the following strong V1 claims:

- the series is fundamentally about private desire becoming audible inside collective life;
- Kumiko's development is `perception → judgment → speech → intervention → leadership → transmission`;
- meritocracy is necessary but socially incomplete;
- Kitauji evolves from charismatic dependence toward institutional reproduction;
- relationships are often asymmetric without one side being false;
- specialness shifts from hierarchical distinction toward relational irreplaceability;
- empathy is also a form of power;
- musical judgment is contextual rather than a ranking of total human worth;
- the anthology volumes pluralize the "true" history of Kitauji;
- adult Kumiko's teaching role is a mature extension of her relational listening.

For each, look for:

- confirming evidence;
- limiting evidence;
- counterexamples;
- earlier foreshadowing;
- wording that changes the strength of the thesis;
- characters whose experience does not fit it.

---

## 12. V2 expansion targets

### 12.1 Character voice

Upgrade V1's useful but compact observations into evidence-dense models of Japanese speech.

### 12.2 Behavioral predictability

Capture decision rules, not adjective lists.

### 12.3 Relationship-conditioned personality

A character does not speak or behave identically with every addressee.

### 12.4 Ordinary life

Use low-stakes scenes to prevent dramatic moments from monopolizing personality models.

### 12.5 Focalization

Systematically separate what Kumiko sees from what the work establishes.

### 12.6 Material opportunity

V1 noted that merit emerges from unequal conditions but did not build a full material ledger. V2 should track those conditions proportionally to the text.

### 12.7 Regional/social language

Clean Japanese text enables more reliable treatment of Kansai features, standard-language switching, geographic mobility, and social register.

### 12.8 Music as practice

Extend symbolic music analysis into rehearsal behavior, teaching, embodied technique, and listening practice when the prose supports it.

---

## 13. Evidence discipline for themes and relationships

Avoid converting recurrent motifs into universal rules.

For example:

- a character's willingness to withdraw may sometimes be self-erasure, but not every withdrawal is secretly a desire to compete;
- an intense same-sex relationship may be strongly yuri-coded without the prose formally defining a romantic partnership;
- a fair audition may be musically defensible while still producing legitimate social distrust;
- talent may be enabled by privilege without becoming unreal or undeserved.

State the strongest formulation supported by the source, not the strongest formulation that produces thematic symmetry.

---

## 14. Release standard

V2 should not become canonical merely because all volumes have been read.

Before full-series freeze:

- sequential readings complete for locked core;
- checkpoints complete;
- ledgers reconciled;
- major character monographs complete or explicitly scoped out;
- relationship/specialist syntheses complete where warranted;
- V1 revision ledger complete;
- locator index passes spot audit;
- unresolved source gaps documented;
- full-series synthesis distinguishes fact, inference, and open questions;
- current corpus map routes all authority correctly.

Only then may the V2 full-series release supersede V1 as current literary authority.

---

## 15. Immediate next step

Do **not** begin `HIBIKE_V01_DEEP_READING.md` yet.

The next architecture-defined phase is:

1. acquire/identify clean Japanese EPUB candidates;
2. create `HIBIKE_SOURCE_INVENTORY.md`;
3. perform EPUB integrity and completeness audit;
4. audit supplemental prose boundary;
5. create `HIBIKE_SOURCE_LOCK.md`;
6. create the V1↔V2 text crosswalk where necessary;
7. only then begin Volume 1.
