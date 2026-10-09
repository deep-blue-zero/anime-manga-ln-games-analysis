---
series: BLUE_ARCHIVE
artifact_type: analytical_method
scope: 'Japanese Blue Archive game narrative corpus: main, group, event, bond, mini, MomoTalk, character/profile/contextual dialogue'
generation: V1
version: "1.10"
status: canonical
source_boundary: "Current promoted Japanese main-story snapshot: electricgoat/ba-data@jp a038020f1f5ac02dcfe76962426d38f86414cdd8, generation BA_REFRESH_20260928T032248159554Z, all 480 main units read; historical V1 witness cbe3fd623c2aab9e781ba0ce0483bc77c68bff86 remains attached to its readings; HePudding/ba-storybook@main 6c4091603ca76d7d8c3cdb9104933f52cd8cab8e remains the independent reference; 3940 supplemental objects admitted with limits in Phase2 cycles001–008; contextual content PASS_WITH_LIMITS, publication pending"
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
created: 2026-08-15
updated: 2026-10-09
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

For the current promoted corpus generation, the primary raw witness is the pinned Japanese branch of `electricgoat/ba-data`:

- branch: `jp`
- commit: `a038020f1f5ac02dcfe76962426d38f86414cdd8`
- recorded game-data version: `v1.73.459696-r96_3cpn8ebtdjiqi6y9qtn1`
- generation: `BA_REFRESH_20260928T032248159554Z`

The historical V1 lock remains `cbe3fd623c2aab9e781ba0ce0483bc77c68bff86`, game-data version `v1.71.447596-r94_y2ha6vgythtil9ja597o`. Completed readings retain their recorded witness; the current snapshot does not silently replace it. The [2026-09-28 source reconciliation](../01%20Source%20Lock%20and%20Inventory/BLUE_ARCHIVE_SOURCE_RECONCILIATION_20260928.md) records the change from 310 to 480 main units, the release cutoff, and the completed V001 C003 backfill. All 480 main units have been read; no main unit remains unopened in that snapshot. Side-source availability remains separate from analytical admission.

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

The historical promoted V1 source corpus provided reversible analytical projections in addition to its 2,716 canonical story/data objects. Its source-side projections included 128 character packages, 2,718 measured relationship candidates with 40 selected relationship bundles, 47 club packages, 15 school packages, 128 Sensei relationship packages, seven main-arc maps, and LLM-oriented context chunks.

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

The historical V1 event corpus contained 490 promoted canonical event stories; nine rerun aliases were consolidated without losing contexts. Current inventory and admission state are routed through the [coverage index](../06%20Evidence%20and%20Indexes/BLUE_ARCHIVE_CHARACTER_ANALYTICAL_COVERAGE_INDEX.md). Analytical event triage should target the canonical story object and preserve alias/release context where relevant.

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

The historical V1 source corpus measured 2,718 person-pairs and emitted 40 selected scene bundles. These are valuable for recall, but the metrics cannot decide which relationships deserve analytical priority.

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

The historical promoted V1 school layer contained 15 master-data-backed school packages, including crossover/external-school labels and an `ETC` category. **Source affiliation is not the same thing as core Kivotos institutional importance.** Before using a school package in worldbuilding synthesis, classify whether it is:

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

## 10.4 Behavioral and reconstruction delta

The literary reading remains primary. When a source unit supplies diagnostically useful character evidence, add a concise behavioral/reconstruction delta after the ordinary character and relationship interpretation. Do not replace scene meaning with a psychology template.

Use one or more change types:

`DISPOSITION_CHANGE · KNOWLEDGE_CHANGE · RELATIONSHIP_CHANGE · CONTEXT_CHANGE · ROLE_CHANGE · RESOURCE_CHANGE · REVEALED_NOT_NEW · UNRESOLVED`

For each material event record, where the source permits:

```yaml
character: null
change_types: []
reconstruction_effect: []
related_rule_or_candidate_refs: []
perceived_problem: null
knowledge_and_uncertainty: []
salient_attention: []
appraisal_hypotheses: []
affective_response: []
motives_in_conflict: []
inhibitors: []
escalators: []
perceived_options: []
choice_and_observable_action: null
immediate_aftermath: null
later_self_account_or_repair: null
relationship_role_resource_conditions: []
written_speech_delta: null
supporting_locators: []
counterevidence: []
uncertainties: []
```

`reconstruction_effect` distinguishes `CREATES_CANDIDATE_RULE`, `STRENGTHENS_RULE`, `NARROWS_RULE`, `CONTRADICTS_RULE`, `CHANGES_STATE`, and `CONTEXTUAL_REPERTOIRE_ONLY`; several may apply. Link an existing rule ID when one exists, otherwise the source-facing observation/candidate route. Do not fabricate a model or rule ID merely to fill this field.

Do not invent unrepresented interiority to complete the fields. Separate observable conduct from appraisal hypotheses, preserve alternatives, and distinguish a state or context delta from durable disposition change. If the unit supplies no discriminating evidence, record `NO_MATERIAL_RECONSTRUCTION_DELTA` rather than manufacturing a row.

The detailed rule, state, readiness, scenario, and validation contracts are governed by `BLUE_ARCHIVE_CHARACTER_RECONSTRUCTION_SPEC_V1.md`. Sequential deltas are evidence-routing inputs to later modeling; they are not themselves permission for hypothetical generation.

## 10.5 Reconstruction responsibility at every future chapter checkpoint

Each natural chapter checkpoint must answer: **What changed about our ability to reconstruct these characters, beyond what changed in our literary interpretation?** This capture contract was introduced at the historical C002 design boundary for the then-planned Chapters 3–8 run. That planning label did not replace canonical crosswalk IDs or establish narrative time. V001 C003 was absent from the historical V1 lock and has since been admitted and fully read as a 43-unit backfill in the current snapshot. Future extensions follow the reconciled crosswalk and declared exposure boundary.

Use a compact table or connected prose covering:

- newly observed contexts and what remains unsampled;
- material state transitions versus contextual repertoire or newly revealed history;
- candidate/rule mechanisms created, strengthened, narrowed, or contradicted, with evidence and counterevidence routes;
- directed relationship, institutional, and public/private conditions;
- ordinary-life controls, written-register variation, and new evidence-backed negative constraints;
- outcomes of previously frozen expectations, including `NO_DIAGNOSTIC_OPPORTUNITY` and failures, linked to the unchanged freeze;
- readiness by domain before and after, with explicit increases, decreases, or `NO MATERIAL READINESS CHANGE`;
- the next missing evidence and whether contextual backfill remains `DEFER`.

Update only affected cumulative ledger entries and coverage rows. The character ledger owns state/mechanism observations, relationship ledger owns directed conditions, institution ledger owns mandate/material constraints, Sensei ledger owns invariants/ethics, voice ledger owns attested speech, motif ledger owns literary recurrence, and claim ledger owns interpretive revisions. The coverage index owns readiness; validation records own frozen tests and outcomes. No new model is required at a checkpoint. Historical C001/C002 readings and checkpoints remain unchanged by this prospective capture contract.

If an expectation was not frozen before exposure, label any later comparison retrospective. If a chapter supplies no fair opportunity, do not manufacture a validation result. A detected failure can lower readiness without making the literary reading unsuccessful.

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

**Historical V1 promotion status:** Phase 0 closed for bulk analysis. The canonical build (`BA_FULL_20260816T002743Z`) and derived build (`BA_DERIVED_20260816T010224Z`) both report `PASS`. Stable-ID uniqueness, 8,774/8,774 choice preservation, sampled provenance round-trip, coverage regression, required derived bundle classes, deterministic sharding, and sampled derived provenance all passed. That audit opened Phase 1. The [current source reconciliation](../01%20Source%20Lock%20and%20Inventory/BLUE_ARCHIVE_SOURCE_RECONCILIATION_20260928.md) records the later promoted DB generation; all 480 main units in that snapshot are now read. The synthesis architecture's §12 owns the current production sequence.

The historical V1 audit retained non-blocking but analytically visible source ambiguities: seven unknown timing/control records, unresolved overarching Japanese event titles in the raw localization tables, some generic group-label resolution, unresolved person/speaker mappings from the source lock, and unresolved in-universe chronology.

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
15. behavioral/reconstruction delta when diagnostic, or `NO_MATERIAL_RECONSTRUCTION_DELTA`;
16. open questions;
17. evidence locators.

The goal is not maximum length. The goal is enough structure that later synthesis can recover **what changed, why we believed it, how confident we were, and where the source evidence lives**.

---

# 17. Governing analytical principle

*Blue Archive* should be analyzed as a **multi-layered social world**, not as a pile of character quotes and not as a single linear visual novel.

The strongest method is therefore:

> **Sequential story first; contextual projection second; longitudinal comparison third; specialist synthesis only after source-class triangulation.**

That order preserves literary causality while exploiting the unusual richness of the extracted corpus: public crises, institutional routines, private bond scenes, messaging behavior, voice/register data, and a reversible path back to the exact Japanese source record.

## Current Phase 2 admission boundary — 2026-10-09

Architecture **Phase2 — Arc contextualization** follows its own phase labels; older numbered method phases remain historical organization. [Cycle008](../02%20Sequential%20Readings/BLUE_ARCHIVE_PHASE2_CONTEXTUALIZATION_CYCLE_008_CHECKPOINT.md) accepts3674 new complete objects, cumulative3940:65 GROUP/1010 EVENT/1161 BOND/1161 whole MomoTalk/511 written/32 MINI. All12 sustained contextual accounts and seven cumulative domains have current content/admission/control acceptance with limits. Scope extension002 and six current class crosswalks own exact responsibilities and states. R09 publication gates remain pending before whole-phase closure. Ordinary repertoire and contrary endpoints have intrinsic value; written language is distinct from performed voice, source dates from global chronology, and textual breadth from model readiness. Later Phase3 packages and pilots require separate claim/state/domain adjudication; no models are certified here.

Current supplemental character coverage is maintained in the [contextual companion](../06%20Evidence%20and%20Indexes/BLUE_ARCHIVE_CONTEXTUAL_CHARACTER_COVERAGE_INDEX.md), read together with the inherited 480-main coverage/history.

## Phase2 cycle003 production boundary — 2026-10-01

[31 group objects](../02%20Sequential%20Readings/BLUE_ARCHIVE_PHASE2_CONTEXTUALIZATION_CYCLE_003_CHECKPOINT.md) bring scoped supplemental admission to100 while every whole-arc row remains incomplete. Ordinary enjoyment, personal wishes, fallible care, recipient objections and routine work enter the seven ledgers with exact evidence modes. Readiness remains23 partial/394 unmodeled/417, standalone NONE. The next major architectural phase is **Phase3 — Character / relationship / institution packages**, after Phase2 obligations are fulfilled; this tranche does not certify that transition.

## Phase2 cycle004 production boundary — 2026-10-01

[The remaining22 group objects](../02%20Sequential%20Readings/BLUE_ARCHIVE_PHASE2_CONTEXTUALIZATION_CYCLE_004_CHECKPOINT.md) close complete group-content intake at65/65 and bring supplemental admission to122. All seven ledgers and coverage/control effects retain ordinary value, actual recipients, source modes and contrary cases. [Fourteen group-grounded families](../08%20Audits%20and%20Manifests/BLUE_ARCHIVE_PHASE2_PRINCIPAL_SCOPE_EXTENSION_001.md) add227 required private objects and three mini relevance leads; current wholePhase2 scope is3631 mandatory/3682 tracked, with3560 still unaccepted. Readiness remains23 partial/432 unmodeled/455, standalone NONE. All12 arc rows and9 wholePhase2 requirements remain incomplete. Phase3 — Character / relationship / institution packages follows sufficient contextualization and its distinct evidence/readiness gates; no package/model is manufactured by this tranche.

## Phase2 cycle005 production boundary — 2026-10-01

[The58-object acceptance](../02%20Sequential%20Readings/BLUE_ARCHIVE_PHASE2_CONTEXTUALIZATION_CYCLE_005_CHECKPOINT.md) brings admitted contextual evidence to180:65 group/43 event/30 bond/30 MomoTalk/12 written-data. Reijo and Ayane complete their available required pools; baseballRei completes ten secure own objects, while four full Tsukuyo/Junko inquiry objects are accepted in their actual contexts without false appearance credit. EVENT807/814 are complete, with ordinary wishes, play, rest, giving and counterevidence retained. All seven ledgers and the five current coverage tables reconcile the accepted effects. Existing readiness stays fixed:23 partial/482 unmodeled/505 analytical subjects, every standaloneNONE.

The full scope remains3631 mandatory/3682 tracked, with3451 mandatory/3502 tracked objects unaccepted. Required private remainders1031B/1031M/422D;57 event packages/967 objects remain. All12 arc rows remain incomplete. Phase3 — Character / relationship / institution packages follows the architecture evidence gates; full-pool intake is distinct from broad transfer or a finished model. Chronology, actual recipients, raw actors, consent conditions and unprinted outcomes retain their limits. No stakes threshold excludes quiet character evidence.

The [complete65-group/12-arc relevance audit](../08%20Audits%20and%20Manifests/BLUE_ARCHIVE_PHASE2_GROUP_ARC_RELEVANCE_AUDIT.md) is parent-accepted as P2-R01 PASS_WITH_LIMITS with no additional source admission. Direct person/community core, bounded comparisons and inspected absence are grounded in the full accepted arguments. P2-R02–R09 and all12 full-arc rows remain incomplete; each source retains intrinsic ordinary value and its original knowledge/identity/chronology limits.

## Phase2 cycle006 production boundary — 2026-10-02

[The33-object acceptance](../02%20Sequential%20Readings/BLUE_ARCHIVE_PHASE2_CONTEXTUALIZATION_CYCLE_006_CHECKPOINT.md) admits Serina’s complete17-source private/written pool and all16 independent EVENT80001 encounters. Cumulative admission is213:65 group/59 event/37 bond/37 full MomoTalk/15 written-data. Ordinary preferences, receiving care, making, gifts, desired time, work and disappointment retain intrinsic literary value. Fake adult summons, refusal pressure, painful care, failed reception and explicit objections remain contrary evidence; a pleasant ending does not authorize an earlier objection. Exact source modes and mutually exclusive alternatives survive integration.

All seven ledgers and five current coverage tables reconcile those accepted effects. The companion has262 rows:98 main-row overrides and164 added analytical subjects;254 main-only rows inherit unchanged. Combined readiness is23 PARTIAL_MODEL /493 UNMODELED /516 subjects, all standaloneNONE. The eleven new routes comprise eight joined named people, one unresolved event-local Kei actor and two local animal/voice buckets, not eleven certified human biographies. Existing baseball Rei receives the E126 addition; diving Rei, Nozomi/Nonomi and the unresolved main-Key/event-Kei identity boundaries remain separate.

Full Phase2 scope remains3631 mandatory/3682 tracked. There are3418 mandatory/3469 tracked objects unaccepted:951 events in56 packages,1024 bond/1024 full MomoTalk/419 written-data. P2-R01 remains PASS_WITH_LIMITS; P2-R02–R09 and all12 arc rows remain incomplete. EVENT801 is the next independent rotation candidate, without an unread literary priority judgment. Later Phase3 — Character / relationship / institution packages and any reconstruction pilot retain their separate source/state/domain gates. Written Japanese does not admit performed voice or unprinted clinical, technical, legal, financial or institutional outcomes.

## Phase2 cycle007 production boundary — 2026-10-07

[The53-object acceptance](../02%20Sequential%20Readings/BLUE_ARCHIVE_PHASE2_CONTEXTUALIZATION_CYCLE_007_CHECKPOINT.md) admits Hanae’s complete21-source and Mine’s complete19-source private/written pools and all13 EVENT801 objects. Cumulative admission is266:65 group/72 event/54 bond/54 full MomoTalk/21 written-data. Gardening, exercise, holiday rest, knitting, giving, collecting, tea, clothing, food, wanted company, festival work, dreams and shared beauty retain intrinsic value. Explicit refusal, failed search, pressure, property costs and unfinished protection retain their contrary force. Source-scoped reports, inward forms, actor commands and alternatives remain distinct from actions and shared knowledge.

The seven ledgers and five current companion tables reconcile these accepted effects. The companion has287 rows:99 main-row overrides and188 added analytical subjects;253 main-only subjects inherit unchanged. Combined readiness is540 subjects:23 PARTIAL_MODEL/517 UNMODELED, allstandaloneNONE. Twenty-four additional source-local routes comprise two Hanae retail opponents, nine Mine people/voice or role buckets and thirteen EVENT801 routes; they are not twenty-four certified named biographies. EVENT801’s chairman/employer alias bridge is explicit, while recurring staff labels do not certify one staff person and separate passer encounters are not automatically joined. Mine and Hanae remain UNMODELED.

Full Phase2 scope remains3631 mandatory/3682 tracked, with3365 mandatory/3416 tracked objects unaccepted:938 events in55 packages,1007 principal bond/1007 full MomoTalk/413 written-data. P2-R01 remains PASS_WITH_LIMITS; P2-R02–R09 and all12 arc rows remain incomplete. Receiving review and shared reconciliation of existing complete unadmitted event packets remain the rotation lane. Existing complete-declared EVENT812 all15 saved arguments now have COMPLETE_PROVISIONAL_RECEIVING_ADOPTION_WITH_MANDATORY_QUALIFICATIONS through ROOT's completed provisional receiving decision. All eight required qualifications below govern affected downstream use; original contributor, prior distinct independent-review allocation and publication rights remain UNKNOWN. EVENT812 remains UNADMITTED and outside cycle007 full53; this disposition supplies no FIRST, SECOND, certified distinct original-author independence, new global source completion or original-body refinement. Resolve EVENT861 all13 owner/private-allocation state before any FIRST assignment; allocation is UNKNOWN and FIRST is false. Preserve EVENT806 as the closed/delivered Yuuka/C&C inquiry awaiting its actual receiving disposition, and EVENT802 as existing completed unadmitted work. These responsibilities are separate from literary priority and retain every required quiet episode. Priority orders complete review and never discards quiet evidence. Later Phase3 — Character / relationship / institution packages and any reconstruction pilot retain their separate gates. Written Japanese admits no performed voice or unprinted clinical, technical, legal, financial or institutional result.


### Current cycle007 authority qualification — 2026-10-07

The earlier dated acceptance and conditional appendices retain their exact input boundaries, including213 admitted objects/516 subjects where recorded. The current cycle007 checkpoint and current boundary above govern266 admitted objects/540 subjects after this coherent transaction; those historical numbers are not competing live censuses. Later mini/G01,20-family,G06/G26,D02 and CF08/CF10 observations retain their existing conditional admission, actor/mode/locale, ordinary-value and contrary-case limits. All twelve full-arc rows and all five architectural duties as a complete Phase2 responsibility remain incomplete; P2-R01 is PASS_WITH_LIMITS only for its group-relevance scope, and P2-R02–R09 remain IN_PROGRESS. No standalone/operational/validated model, monograph, forecast or performed-voice admission is created.


### Receiving review and allocation queue — 2026-10-07

Receiving review and shared reconciliation of existing complete unadmitted event packets remain the rotation lane. Existing complete-declared EVENT812 all15 saved arguments now have COMPLETE_PROVISIONAL_RECEIVING_ADOPTION_WITH_MANDATORY_QUALIFICATIONS through ROOT's completed provisional receiving decision. All eight required qualifications below govern affected downstream use; original contributor, prior distinct independent-review allocation and publication rights remain UNKNOWN. EVENT812 remains UNADMITTED and outside cycle007 full53; this disposition supplies no FIRST, SECOND, certified distinct original-author independence, new global source completion or original-body refinement. Resolve EVENT861 all13 owner/private-allocation state before any FIRST assignment; allocation is UNKNOWN and FIRST is false. Preserve EVENT806 as the closed/delivered Yuuka/C&C inquiry awaiting its actual receiving disposition, and EVENT802 as existing completed unadmitted work. These responsibilities are separate from literary priority and retain every required quiet episode.


### Event812 completed provisional receiving — successor qualification,2026-10-07

Current receiving state: **COMPLETE_PROVISIONAL_RECEIVING_ADOPTION_WITH_MANDATORY_QUALIFICATIONS**. ROOT completed its qualified receiving judgment for all15 saved Event812 arguments and their union checkpoint. The complete14,734-byte ROOT judgment is bound by SHA256 `03fafb6c72984ff3dc03848522ae6e62192ba34db23ad79dabbb0b69a149e2e0`; its2,583-byte decision is bound by SHA256 `122379c75b1597f1412681e8cca2238b78ff0a24e5a4c83d4562e408c23df7a4`. This control qualification carries that decision; it applies no original-body precision operation or analytical admission.

The following eight requirements govern any affected downstream claim:

1. **001 inward alternative:** the relic-like adult thought belongs to designed `[ns3]/[ns4]` alternatives, not a securely observed single selected inward line. ROOT001 Q01 remains an unapplied exact guard.
2. **001 causal condition:** possible prior fragility remains unresolved at001. Gentle-handling testimony, sincere preparation and actual failure establish no cause, blame or innocence proof. ROOT001 Q02 remains unapplied.
3. **014 collective attribution:** retain the Kazusa-and-Natsu collective reply as one named collective unit, not Kazusa-exclusive agency. Exclusive individual subtotal868 plus one collective; Kazusa-exclusive routing21 total/4 in014; eleven named people and1019 total units unchanged; actor-bearing partition868+1+107+17=993. Do not count two units or silently call869 an exclusive subtotal.
4. **Preference revision:**003's cake demand and008's gratitude retain value beside011's mischief and015's actual taste. Neither cake nor lemon smoothie is Ui's established favorite; iced Americano is self-chosen. Future coffee delivery remains unobserved.
5. **007 offer and recipient situation:** no wages, possible shelter/food and conditional later recommendation remain distinct; Japanese supplies no fixed one-month term. Constrained recipients' cinema/café/arcade desires are their ends. Offer and B's acceptance establish no universal trust, unpressured consent, adequate provision or fulfilled paid job.
6. **Accomplished local benefits:** retain009's narrated medicine discovery/bright return,012's expressed enjoyable fatigue,013's completion report/handoff and014's strong immediate replacement inference/resumed ceremony. Broader treatment, authority, technical equivalence, consent, costs and covert steps stay open without erasing achieved local benefits.
7. **Documentary boundaries:** preserve actual actors, `#na`, silence, inward/narration/system modes, Japanese wording, guards, encountered alternatives/order, generic local contexts and internal chronology. The collective is not a74th dialogue seam. Closing text does not repair null event-title metadata; performed voice, animation and runtime remain uninspected.
8. **Provisional origins and rights:** original contributor, prior distinct independent-review allocation and publication rights remain UNKNOWN. This completed receiving work certifies no distinct origins, retroactive source-work authorization or publication entitlement. Event812 all15 remain UNADMITTED outside cycle007 full53; no FIRST, SECOND or new global source-completion credit is created.

**Retained planning history:** the original sealed current58 proposal recorded the following earlier state accurately before this completed ROOT decision:

> Existing complete-declared EVENT812 all15 saved arguments now have provisional receiving review IN_PROGRESS; original contributor and prior distinct independent-review allocation remain UNKNOWN. This current receiving allocation certifies neither distinct original-author independence nor publication rights, and EVENT812 remains outside the cycle007 full53 admission.

The current completed qualified receiving decision qualifies the earlier queue state as dated planning history. It preserves the sealed snapshot, the53-source admission union, all earlier source/owner/closure/model limits and other receiving duties. Formal intake/admission states do not assert that no historical COMPLETE declaration or qualified provisional receiving assessment exists. All12 whole arcs and all five Phase2 duties remain incomplete; merge approval remains RESERVED.
