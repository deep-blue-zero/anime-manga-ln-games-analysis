---
title: "IDOLY PRIDE V2 Analytical Method"
project: "IDOLY PRIDE"
document_id: "IDOLY_PRIDE_V2_ANALYTICAL_METHOD"
version: "2.5"
status: "governing-framework"
created: "2026-08-13"
updated: "2026-08-19"
live_corpus_model: "rolling workspace plus immutable dated releases"
primary_reading_layer: "analysis_bundles"
provenance_layer: "idoly-ingest and underlying extracted game corpus"
historical_analysis_role: "hypothesis and provenance only"
anime_phase_execution: "one episode per analytical turn with five-step prospective/adversarial audit"
historical_stress_test_order: "primary source -> prospective freeze -> historical comparison"
---

# IDOLY PRIDE V2 ANALYTICAL METHOD

## 1. Purpose

This document governs the second-pass deep analysis of *IDOLY PRIDE*.

V2 is not an expansion of the earlier scattered writeups. It is a source-led reconstruction of the work from the game-extracted Japanese corpus, supplemented by anime and other audiovisual material. Earlier analyses remain useful as historical hypotheses and provenance, but they never override source evidence.

The method is designed to solve five problems from the first-pass workflow:

1. characterization is dispersed across thousands of story fragments;
2. earlier analyses were sometimes written before later or less obvious evidence had been surveyed;
3. event-level insight accumulated faster than it could be reconciled longitudinally;
4. textual and audiovisual claims were sometimes mixed together;
5. conversational sprawl weakened retrieval, correction, and source traceability.

The governing traceability chain is:

> **claim -> synthesis document -> working ledger -> source bundle -> granular story ID -> extracted game material or audiovisual source**

No conclusion becomes canonical merely because it appeared in V1.

---

# 2. Governing source model

## 2.1 `analysis_bundles`: default analytical reading layer

Use `analysis_bundles` for:

- complete and chronological character reconstruction;
- source-class slices;
- unit reading;
- event/card/bond/message reconnaissance;
- relationship discovery;
- lexical and speech-pattern analysis;
- contradiction detection;
- identifying passages for closer inspection.

These bundles are an LLM-oriented edition of the extracted game corpus, not a prior interpretive summary.

## 2.2 `idoly-ingest`: provenance and exact-context layer

Descend to `idoly-ingest` when:

- a major claim depends on one specific scene;
- exact surrounding dialogue matters;
- scene boundaries must be reconstructed;
- speaker attribution or source metadata needs verification;
- a contradiction in a higher-level omnibus must be resolved;
- a canonical source locator is being created.

The project should not waste context by reading raw records when a source-preserving analytical bundle is sufficient.

## 2.3 Underlying extracted corpus

The raw/normalized extraction is archival. It exists to keep the transformation chain inspectable and to resolve unusual technical questions.

## 2.4 Game-manager identity and branch semantics

**Governing identity decision:** the customizable game manager is treated as the continuing **Makino Kouhei (牧野航平)** from the television anime. This is the default character identity, not an open equivalence hypothesis. The editable player name and `{user}` placeholder are interface-level customization layered onto a character whose Hoshimi narrative role, continuity history, appearance, and voiced presentation overwhelmingly identify him with Makino. Only explicit primary-source contradiction may reopen the identity question.

This identity decision must be separated from the canon status of individual selectable responses. Classify manager material as follows:

1. **IDENTITY-INVARIANT MAKINO FACT** - history, relationships, role, appearance/voice continuity, and other facts independent of player selection.
2. **BRANCH-INVARIANT MAKINO ACTION/DIALOGUE** - events or lines the game presents regardless of selectable response; ordinary canonical characterization.
3. **PLAYER-SELECTED MAKINO EXPRESSION** - mutually exclusive authored options. Each option defines a plausible Makino response within the game's characterization envelope, but all options must not be treated as having literally co-occurred.
4. **INTERFACE PARAMETERIZATION** - custom name, `{user}`, and comparable player-facing affordances. These do not by themselves create a separate protagonist or continuity break.

Phase 2 therefore maintains a **Makino Player-Branch Canon Ledger**, not an identity-continuity ledger. Its purpose is to distinguish fixed characterization from branch possibility space and to preserve any genuine contradiction if one appears.

---

# 3. Supplementary and audiovisual sources

The franchise is multimedia. Text alone cannot establish every claim.

## Anime audiovisual evidence

Use for:

- vocal delivery, pause, breath, silence, affect;
- blocking and camera placement;
- editing and recurring visual motifs;
- Mana's ghostly presence;
- Sakura/Mana visual or vocal rhyme;
- stage and audience relations;
- music and scene transition;
- character embodiment.

Subtitles establish words. Audio establishes delivery. Frames establish visible form.

## Game music, 3DMVs, and live sequences

Use for:

- performance identity;
- choreography;
- costume language;
- center/member hierarchy;
- arrangement and sonic character;
- lyrics;
- audience orientation;
- formal contrast among units.

## Card art, key visuals, photos, and official 4koma

Use for visual design, recurring objects, body language, public persona, visual motifs, and editorial emphasis.

Treat official 4koma as supplementary characterization/social texture rather than automatically equivalent in dramatic weight to main story or major event narratives.

## Telephone audio

Telephone audio is source evidence. Machine-generated ASR is a provisional transcription layer.

For quotation-sensitive or linguistically subtle claims, verify against audio.

---

# 4. Historical analytical corpus

Existing chats and prior synthesis documents form a historical analytical layer.

Use them to:

- recover hypotheses worth retesting;
- find source stories that earlier work identified as important;
- locate prior interpretive disagreements;
- preserve development history;
- identify what V2 confirms or revises.

They must never silently substitute for source rereading.

V1 claims may be confirmed, strengthened, qualified, split, weakened, overturned, recontextualized, or left unresolved.

---

# 5. Epistemic evidence classes

Every consequential analytical claim should be classifiable as one of the following.

## TEXTUAL FACT

Directly established by dialogue, narration, metadata, or explicit story events.

## AUDIOVISUAL FACT

Directly established by visible or audible presentation rather than inferred from text.

## STRONG INFERENCE

Not directly stated, but supported by multiple converging signals with little meaningful counterevidence.

## INTERPRETATION

A defensible explanatory model that organizes evidence but is not uniquely compelled by it.

## SPECULATION / OPEN HYPOTHESIS

Plausible but insufficiently stabilized. Preserve only when analytically useful.

## CONFLICT / AMBIGUITY

Evidence materially supports more than one reading, or continuity/source tension remains unresolved.

These labels are epistemic, not quality judgments.

---

# 6. Narrative-weight hierarchy

The following hierarchy is a default, not an automatic rule.

## Tier A: governing narrative

- main game story;
- unit-origin stories;
- anime narrative.

## Tier B: major developmental narrative

- major events;
- substantial card stories;
- bond stories.

## Tier C: relational/social texture

- messages;
- group chats;
- ordinary-life scenes;
- routine communications.

## Tier D: formal/performance evidence

- songs and lyrics;
- 3DMVs/live sequences;
- anime audiovisual form;
- key visuals and card art;
- official 4koma.

## Tier E: provisional derived evidence

- unverified telephone ASR;
- technically incomplete assets.

## Tier H: historical analysis

- earlier project chats;
- prior synthesis documents;
- old event-priority lists.

A lower-tier source may be decisive for a narrow question. The hierarchy governs expected narrative weight, not universal supremacy.

---

# 7. Corpus reconnaissance before prose synthesis

V2 must not begin by rewriting character profiles.

First construct a Corpus Coverage and Priority Ledger.

For each significant source item record:

- source ID;
- title;
- source class;
- original story ID(s);
- corpus path;
- characters and units;
- relationship axes;
- approximate order/release position;
- narrative function;
- motifs/themes;
- priority;
- priority reason;
- relevance to V1 claims;
- contradiction/revision potential;
- audiovisual dependency;
- source locator;
- notes.

Priority vocabulary:

- **FOUNDATIONAL**
- **CORE**
- **IMPORTANT**
- **TEXTURE**
- **REDUNDANT**
- **CONFLICTING**
- **FORMAL-DEPENDENT**
- **UNRESOLVED**

The historical `idoly-ingest-selected-events-core-important` layer may be used for orientation, but it is not authoritative. V2 priority is determined by the new ledger after broad corpus review.

---

# 8. Longitudinal character method

Before writing a definitive character synthesis, reconstruct the character across source classes.

For each major character track:

1. **Initial condition** - role, unit, prior career/history, public image.
2. **Core desire** - stated, enacted, concealed, socially acceptable.
3. **Core fear/wound/contradiction** - without reducing every character to trauma.
4. **Defensive strategy** - control, glamour, cuteness, overwork, hostility, caretaking, humor, restraint, withdrawal, etc.
5. **Public/private selves** - not as fake/real binaries, but as different functional registers.
6. **Professional philosophy** - idolhood, audience, competition, labor, money, talent, teamwork, publicity, failure, career.
7. **Relational architecture** - unit peers, rivals, family, manager, fans, seniors/juniors, former partners, absent/dead figures.
8. **Performance identity** - what becomes expressible onstage that ordinary life cannot fully hold.
9. **Japanese voice/register** - pronouns, sentence endings, politeness, address terms, nicknames, teasing, commands, aggression, apology, message vs spoken voice.
10. **Turning points** - only count events that alter a stable dimension of self or relationship.
11. **Mature state** - what the character can now do, admit, share, refuse, or choose.
12. **Contradictory evidence/open questions** - evidence that pressures the preferred model.

### 8.1 Longitudinal scope boundary versus holistic experiential modeling

The Phase-2 character ledger is a **change-through-time instrument**, not an exhaustive inventory of everything the person likes, buys, eats, watches, collects, fears, texts, or does on a day off.

Ordinary-life material should enter the longitudinal ledger when it materially clarifies:

- a stable disposition or contradiction;
- a relationship state;
- a developmental transition;
- a public/private split;
- a recurring behavioral defense or care pattern;
- a literary/theme claim;
- a voice/register finding needed for current interpretation.

Do not force every card, message, bond, event, 4koma, or telephone scene into the ledger merely to avoid losing lifestyle detail. The complete coverage/routing layer already preserves source discoverability.

A later **Phase 8.5 holistic character-modeling pass** deliberately returns to these source classes after the core longitudinal and synthesis corpus is stable. That pass asks a different question: what is it like to actually know this person, spend ordinary time with them, talk with them, and observe their preferences, habits, fandoms, domestic behavior, mundane competencies, conversational triggers, humor, embarrassment, leisure, and daily routines?

The canonical mature home for those character-specific experiential details is `IDOLY_PRIDE_V2_CHAR_<CHARACTER>_MODELING_PROFILE.md`, not a separate permanent per-character preference document.

Do not retroactively pretend later clarifications were already available in early arcs.

---

# 9. Relationship analysis

Relationships receive their own ledgers when they materially exceed ordinary character-note scale.

Track:

- initial asymmetry;
- explicit self-definition;
- actual behavior;
- conflict grammar;
- care grammar;
- speech/address changes;
- intimacy markers;
- professional consequences;
- reversals of dependence;
- mature equilibrium;
- unresolved tension.

Distinguish:

- siblinghood;
- best friendship;
- rivalry;
- hostile intimacy;
- professional partnership;
- caretaking;
- dependency;
- mentorship;
- fan/performer relation;
- memory bond;
- producer/idol relation.

For romance or yuri-coded readings, separate:

- textual romantic fact;
- culturally legible romantic coding;
- unusually intimate friendship;
- interpretive possibility;
- unsupported shipping inference.

---

# 10. Unit analysis

A unit is more than the sum of its members.

Track:

- origin;
- founding contradiction;
- member differentiation;
- center logic;
- division of emotional/professional labor;
- performance aesthetic;
- speech/social rhythm;
- relationship to competition;
- relationship to audience;
- relationship to management;
- crisis/re-foundation;
- mature philosophy;
- relation to other units;
- the unit's distinctive answer to "what is an idol?"

Every unit-level generalization should be tested against members who resist it.

---

# 11. Theme and institution analysis

Maintain cross-series ledgers for recurring structures before writing thematic prose.

Priority axes include:

- Mana and inheritance;
- grief and public memory;
- miracle vs reproducible labor;
- professional idolhood;
- money and career;
- audience and recognition;
- rivalry and care;
- ordinary life;
- bodily memory;
- performance as memorialization;
- management, autonomy, and intervention;
- media visibility and branding;
- adulthood and longevity;
- failure and competition;
- overseas/global ambition;
- institutional legitimacy.

A theme does not become series-wide simply because it is vivid in one unit.

---

# 12. Prospective and retrospective reading

For major arcs distinguish:

## Prospective reading

What could a reader/player reasonably infer at the time?

## Retrospective reading

What does later information recontextualize?

The later reading may strengthen, weaken, or overturn the earlier one, but the early ambiguity should remain historically intelligible.

## 12.1 Phase 0.5 anime execution unit

The default Phase 0.5 execution unit is **one anime episode per analytical turn**. All five stages below should normally be resolved inside that same turn so that the independently formed episode model remains immediately available for adversarial comparison without requiring a second reconstruction.

Do not batch multiple previously unread episodes into one prospective pass unless source access or another technical constraint makes the default workflow impossible. Episode N may inherit the frozen prospective state of Episodes 1 through N-1, but it must not silently use knowledge from Episodes N+1 onward or later game material.

The five-stage transaction is:

### Step 1 - Independent prospective deep reading

Read the locked episode bundle **before consulting the prior anime-analysis transcript or other historical analytical prose about that episode**.

The evidence pass should integrate, where available:

- original Japanese dialogue and subtitle wording;
- voice acting, pitch/timbre tendency, pacing, pauses, breath, laughter, hesitation, vocal strain, softness, and relational register;
- score, insert-song placement, silence, sound design, transition cues, and musical build/release;
- composition, blocking, character acting, gesture, eye line, bodily distance, color/light, recurring spaces and objects;
- editing, shot duration, juxtaposition, visual rhyme, audience position, and performance staging;
- character state, relationship state, narrative function, thematic propositions, and unresolved ambiguity.

The purpose is not to reproduce the episode plot. It is to reconstruct what the episode itself establishes under the information conditions available at that point in the anime.

If later-canon knowledge is already known to the analyst, it must be actively bracketed during this step rather than used as invisible support.

### Step 2 - Freeze the prospective finding set

Before retrieving historical analysis, record a **Prospective Finding Set** for the episode. At minimum it should contain:

- episode-level dramatic function;
- character-state deltas;
- relationship-state deltas;
- Japanese-language findings;
- voice/performance findings;
- music/sound findings;
- visual/formal findings;
- major claims with epistemic labels;
- counterevidence and simpler alternative explanations;
- open questions;
- primary-source locators.

"Freeze" means that these findings remain identifiable as the pre-comparison V2 reading. Historical analysis discovered in Step 3 may cause a later claim revision, but it must not be allowed to rewrite the record so that the earlier independent finding appears never to have existed.

This separation is necessary to measure convergence and anchoring rather than merely produce a polished retrospective synthesis.

### Step 3 - Retrieve the corresponding historical analysis

Only after Step 2 is frozen, retrieve the relevant episode section from prior IDOLY PRIDE anime-analysis transcripts and related historical analytical material.

Historical analysis remains **Tier H** evidence. Its purpose is to supply:

- earlier hypotheses;
- prior interpretive disagreements;
- claims generated under different source access or reading order;
- documented overreads and corrections;
- observations V2 may have independently missed.

Do not treat eloquence, prior confidence, or earlier repetition as evidence that a legacy claim is correct.

### Step 4 - Adversarial V1/V2 stress test

Compare the frozen V2 finding set against the historical episode analysis claim by claim.

For each meaningful legacy claim, assign the existing revision vocabulary where appropriate:

- **CONFIRMED**
- **STRENGTHENED**
- **QUALIFIED**
- **SPLIT**
- **WEAKENED**
- **OVERTURNED**
- **RECONTEXTUALIZED**
- **UNRESOLVED**

The stress test is bidirectional. It must ask both:

1. What did the prior analysis claim that the fresh V2 pass does not independently recover?
2. What did the fresh V2 pass recover that the prior analysis never noticed?

When useful, record likely causes of disagreement using diagnostic flags such as:

- `source_order`;
- `retrospective_knowledge`;
- `transcript_reduction`;
- `audiovisual_overread`;
- `later_canon_projection`;
- `insufficient_counterevidence`;
- `simpler_explanation_available`;
- `historical_source_gap`.

A legacy thesis that survives a different reading order, stricter evidence separation, stronger audiovisual inspection, and explicit counterevidence search becomes more credible. A thesis that does not survive should not be restored merely because it was central to V1.

Recommended stress-test record:

```yaml
legacy_claim_id:
legacy_source:
legacy_turn_or_locator:
legacy_claim:
original_evidence_basis:

v2_status:
v2_evidence:
v2_source_locator:

bias_flags: []
what_v1_got_right:
what_v1_missed:
what_v1_overstated:
what_v2_changes:
confidence:
```

### Step 5 - Emit the episode delta and update cumulative anime state

Conclude the turn by emitting or updating the canonical episode-level analytical record. It should preserve the prospective V2 reading while also recording the historical stress test.

The preferred episode output contains:

- prospective episode deep reading;
- character and relationship state deltas;
- audiovisual/formal findings;
- Japanese-language findings;
- voice/performance findings;
- music/sound findings;
- V1-to-V2 revision table;
- genuinely new V2 claims;
- unresolved questions;
- primary-source locator section;
- cumulative anime-state changes that become valid prior knowledge for the next episode.

The output should be selective rather than exhaustive. Inspect as much primary evidence as needed, but surface the observations that materially affect characterization, relationship structure, theme, formal design, or later synthesis.

After Episode 12, the cumulative prospective state is frozen as the **anime-endpoint ledger**. Later game material may recontextualize that baseline during the retrospective audiovisual/cross-media phase, but must not silently rewrite what the anime itself had established prospectively.

## 12.2 Historical-analysis contamination rule

The governing order for Phase 0.5 is:

> **primary source -> independent prospective interpretation -> frozen finding set -> historical-analysis retrieval -> adversarial comparison**

Never invert this into:

> **historical interpretation -> primary source -> search for confirmation**

The historical transcript is therefore a stress-test corpus, not a reading guide.

---

# 13. Adversarial reading protocol

Before stabilizing a major thesis, ask:

1. What source most strongly contradicts this?
2. Is the pattern longitudinal or event-specific?
3. Is comedy being mistaken for deep psychology?
4. Is later information being projected backward?
5. Is the character's self-description reliable?
6. Does another source class change the claim?
7. Is Japanese nuance being lost in paraphrase?
8. Is the claim textual, formal, inferential, or interpretive?
9. Are we mistaking narrative convenience for thematic structure?
10. Would a simpler explanation fit equally well?

Record material counterevidence rather than silently explaining it away.

---

# 14. Duplication control

Each major idea should have one canonical analytical home.

Preferred routing:

- character-specific detail -> character/unit document;
- relationship mechanics -> relationship document;
- series-wide implication -> thematic document;
- exact proof -> evidence ledger;
- concise cross-reference -> later synthesis.

A mature document may summarize another document's conclusion but should not reproduce its full analysis unless the context materially changes it.

---

# 15. Writing standard

Final synthesis prose should:

- privilege original Japanese evidence;
- quote sparingly and purposefully;
- preserve source IDs for load-bearing claims;
- distinguish fact from interpretation;
- avoid invented themes;
- address counterevidence;
- treat characters as subjects rather than archetype checklists;
- avoid reducing every conflict to trauma;
- preserve humor, ordinary life, labor, and professional material;
- treat *IDOLY PRIDE* as a multimedia idol drama rather than a transcript database.

The goal is a corpus that is both human-readable and machine-retrievable.

---

# 16. Live-service corpus maintenance, cutoffs, and versioning

*IDOLY PRIDE* is a continuing live-service work. The analytical corpus therefore has two simultaneous states: a mutable **rolling workspace** and immutable **dated releases**.

## 16.1 Rolling workspace and frozen releases

The rolling workspace absorbs new game material, source corrections, new audiovisual assets, and revised ledgers. It is explicitly mutable.

A frozen release records a coherent interpretation of the corpus through an exact source cutoff. After final audit, that release is immutable. Later material must never be silently folded backward into it.

A frozen release should record at minimum:

- release version;
- source cutoff date/time;
- source snapshot or manifest identifier;
- exact source classes included;
- known gaps;
- claim-validation frontier;
- package checksum.

This preserves the historical fact that a reading may have been the strongest interpretation available at one point in an ongoing serialization even if later material recontextualizes it.

## 16.2 Source-delta audit

When a newer extraction snapshot becomes available, do not reread the entire corpus from zero. Compare it against the prior frozen source manifest and create a delta audit identifying:

- newly added stories;
- modified stories;
- removed/replaced stories;
- newly available audio or visual assets;
- new main-story chapters;
- new unit stories;
- new events, cards, bonds, messages, and telephone material;
- new characters or units;
- upstream extraction corrections.

Every changed source should receive a delta-ledger entry and be routed to the characters, units, relationships, themes, and claims it may affect.

## 16.3 Semantic impact classes

New material should be classified by analytical impact rather than merely by source count.

### UPDATE CLASS 1 - ADDITIVE TEXTURE

Examples: ordinary messages, minor card scenes, birthday material, comedy, routine interactions, hobbies, fandoms, preferences, domestic habits, and conversational texture. Class-1 material may leave the literary synthesis unchanged while still creating a later Phase-8.5 modeling-profile delta.

Default action: update source/character/relationship ledgers; revise polished synthesis only when accumulation becomes meaningful.

### UPDATE CLASS 2 - SIGNIFICANT DEVELOPMENT

Examples: substantial events, important bond/card stories, meaningful relationship development, new professional information, or a significant unit development.

Default action: update ledgers and re-audit affected specialist synthesis documents.

### UPDATE CLASS 3 - ARCHITECTURAL MATERIAL

Examples: new main-story arcs, new units, major character revelations, unit dissolution/re-formation, major Mana/Makino information, important industry changes, or material that changes the full-series model.

Default action: broad claim audit, revision of all affected specialist documents, and reassessment of the continuous full-series synthesis.

The update class is an impact judgment, not a prestige judgment. A small message can still become Class 2 if it resolves a major ambiguity.

## 16.4 Temporal claim provenance

Every consequential claim record should contain:

```yaml
validated_through:
last_retested:
source_snapshot_id:
```

`validated_through` records the newest narrative/source frontier against which the claim has been tested. `last_retested` records when the analytical review occurred.

This allows a claim to remain historically valid without pretending it has been checked against material that did not yet exist.

## 16.5 Character and unit freshness frontier

Maintain a small update-status registry for major characters and units containing:

- last corpus review date;
- latest included source;
- current source snapshot;
- whether new material is pending;
- whether specialist synthesis requires reanalysis.

A character whose ledger is six months behind the live corpus must not appear equally current merely because the document still exists.

## 16.6 New characters and units

Newly introduced figures should first receive provisional ledgers. Do not produce a definitive synthesis from an introductory scene alone. Promote a provisional ledger to canonical character/unit synthesis only when the source base is sufficient for longitudinal analysis.

## 16.7 Main-story trigger

A substantial new main-story tranche automatically triggers review of:

- series architecture;
- affected character and unit ledgers;
- relationship changes;
- Mana/Makino inheritance where relevant;
- institution/industry ledgers;
- every relevant claim marked `OPEN`, `UNRESOLVED`, or `CONFLICTING`.

Smaller source classes normally use narrower impact routing.

## 16.8 Release versioning

Recommended version semantics:

- **patch (`v1.0.1`)** - technical correction, locator repair, or non-substantive metadata fix;
- **minor (`v1.1`)** - meaningful new source material that revises a bounded portion of the corpus without changing the governing architecture;
- **major (`v2.0`)** - large new narrative era, broad reinterpretation, or methodological/architectural break.

A project may use simpler `v1.0`, `v1.1`, `v1.2` numbering if preferred, but the release manifest must state why the version changed.

Frozen releases should be stored separately from the rolling workspace, for example:

```text
09 Final Release/
|-- IDOLY_PRIDE_V2_v1.0_2026-08-13/
|-- IDOLY_PRIDE_V2_v1.1_2026-10-02/
`-- IDOLY_PRIDE_V2_v1.2_2027-01-15/
```

Newly released stories must never silently alter an older frozen synthesis.

---

# 17. Recommended phase sequence

## Phase 0 - Source lock and corpus audit

Freeze the initial source snapshot, record manifests, gaps, evidence classes, and cutoff. After the first release, this becomes a recurring delta-audit step rather than a full restart of the project.

## Phase 0.5 - Prospective complete anime deep reading

Review all twelve TV episodes sequentially as a bounded audiovisual work. Use the five-step episode transaction in Section 12.1: independent prospective reading, prospective freeze, historical-analysis retrieval, adversarial V1/V2 stress test, and episode delta/ledger update.

Default cadence: **one episode per analytical turn**. Do not use later episodes or the later game corpus to erase uncertainty that was genuinely present at the episode's original information frontier.

At Episode 12, freeze the anime-endpoint character, relationship, unit, music/performance, and formal baseline.

## Phase 1 - Corpus priority, coverage, and anime-era expansion audit

Survey `analysis_bundles`, build the authoritative priority ledger, reassess historical selections, and flag game sources that require selective audiovisual escalation.

After the Phase 0.5 anime endpoint is frozen, Phase 1 must also perform a dedicated **Hoshimi anime/game expansion audit** across all `st-original-cmn` blocks. Map each game block to the relevant anime episode(s) and classify the relation using explicit categories such as:

- `DIRECT_RETELLING`;
- `EXPANDED_MAKINO_POV`;
- `EXPLICITATED_MOTIVE_OR_PROFESSIONAL_REASONING`;
- `ADDED_SCENE_OR_CONTEXT`;
- `BRANCH_PARAMETERIZED_MAKINO_EXPRESSION`;
- `REFRAMING_OR_EMPHASIS_SHIFT`;
- `ANIME_ONLY_AUDIOVISUAL_FORM`;
- `CONTINUITY_TENSION`.

The purpose is not to collapse the two tellings into one composite transcript. It is to establish exactly **how the game's Hoshimi telling expands, specifies, or reframes the anime while preserving the anime's frozen prospective information boundary**.

### Phase 1B - ordered origin/main-story dependency sequence

Phase 1B must preserve **both diegetic chronology and disclosure chronology**. Unit-origin stories are not dumped into a detached background appendix and are not automatically read before every present-tense main-story arc merely because they depict earlier events. For each origin bundle record:

- `diegetic_position`;
- `disclosure_position`;
- `prerequisite_main_story_state`;
- `retrospective_targets`;
- `forward_inheritance_point`.

The main story remains the governing present-tense spine. Origin material enters the inherited analytical state at a controlled reveal boundary so that later explanations do not erase the uncertainty or first-impression state created by earlier material.

The canonical Phase-1B sequence after completion of the Hoshimi anime/game expansion audit is:

1. **SUNNY PEACE origin audit** - `origin_sun_001` through `origin_sun_005`;
2. **Tsuki no Tempest origin audit** - `origin_moon_001` through `origin_moon_005`;
3. **LizNoir origin audit** - `origin_liz_001` through `origin_liz_010`;
4. **TRINITYAiLE origin audit** - `origin_tri_001` through `origin_tri_006`;
5. **Hoshimi anime/game expansion-audit addendum**, only where those origin stories materially revise source attribution, chronology, motive, relationship state, or expansion findings;
6. **IIIX origin audit - mandatory pre-Tokyo baseline** - `origin_thrx_001` through `origin_thrx_004`;
7. **Tokyo main story** - `tokyo_001_new_wind` through `tokyo_014_with_beyond_the_miracle`;
8. **BIG4 main story** - `big4_001_dark_of_the_moon` through `big4_014_epilogue`;
9. **Stellar main story** - `stellar_001_to_soar_high` through `stellar_011_all_my_youth`;
10. remaining origin/special source classes as required by disclosure dependencies;
11. independent reranking of all event bundles against the stabilized Tier-A model.

The first four origin audits are deliberately placed before Tokyo because they can contain prequel, concurrent, and post-Hoshimi information that changes how the anime-era game retelling should be sourced or interpreted. **IIIX is a hard prerequisite for Tokyo** because IIIX is a major actor in that arc; Tokyo must not be used to infer IIIX's baseline retroactively when the game provides a dedicated origin sequence first.

When an origin story reveals later information about an already-read source, revise the relevant ledger through an explicit retrospective delta or addendum. Do not silently rewrite the earlier state.

## Phase 2 - Longitudinal ledgers

Characters, relationships, units, themes/institutions, linguistic voice/register evidence, performed-voice requirements, formal dependencies, and the **Makino Player-Branch Canon Ledger**. Phase 2 stabilizes change-through-time and interpretive voice evidence; it does **not** require exhaustive preference, hobby, ordinary-life, or conversational-persona mining. P2-F is linguistic scaffolding for later synthesis and modeling, not the final lived-person conversational reconstruction.

## Phase 3 - Unit and character syntheses

Draft only after ledgers stabilize.

## Phase 4 - Relationship and thematic syntheses

Integrate across units.

## Phase 5 - Retrospective audiovisual and cross-media audit

Return selectively to anime scenes whose meaning is materially changed or strengthened by later game evidence, while also reviewing prioritized game voice scenes, music, 3DMVs, live performance, card art, 4koma, and telephone audio under the dedicated audiovisual-selection protocol.

This phase may recontextualize the frozen anime baseline but must not silently overwrite it.

## Phase 6 - Series architecture and comparative matrices

Define mature full-series structure only after specialist work exists.

## Phase 7 - Evidence locator and claim revision audit

Trace load-bearing conclusions backward.

## Phase 8 - Continuous full-series synthesis

Write the literary argument rather than an encyclopedia.

## Phase 8.5 - Holistic character modeling and experiential reconstruction

After the core longitudinal, specialist, thematic, audiovisual, evidence-routing, and full-series synthesis work is substantially stable, build the per-character modeling profiles.

The governing question is:

> **What is it actually like to spend time with this person as a lived social individual?**

For each major character, perform a targeted re-sweep of events, cards, bonds, messages, 4koma, telephone audio, and relevant audiovisual material for characterization that earlier literary compression may have underweighted. Integrate:

- ordinary routines and daily rhythm;
- interests, fandoms, hobbies, mascots, collections, and enthusiasm triggers;
- food, shopping, money, fashion, media, leisure, and material preferences;
- practical skills and mundane weaknesses;
- fears, aversions, pet peeves, boredom, embarrassment, humor, and play;
- conversation initiation, listening, silence, infodump behavior, topic-specific energy, digital communication, and relationship-conditioned register;
- body language and performed conversational affect where audiovisual evidence permits;
- day-in-the-life and scenario-behavior ranges, clearly labeled as derived reconstruction rather than unseen canonical events.

Distinguish `one_off`, `repeated_preference`, `stable_disposition`, and `behaviorally_predictive` evidence so that isolated trivia does not become a false personality law.

The canonical human-readable home is `IDOLY_PRIDE_V2_CHAR_<CHARACTER>_MODELING_PROFILE.md`. An optional cumulative `IDOLY_PRIDE_V2_CHARACTER_TEXTURE_EVIDENCE_LEDGER.md` may support source routing, but it is evidence infrastructure rather than a competing per-character profile family.

Generated dialogue or simulated behavior remains derived output and never becomes canonical evidence.

## Phase 9 - README, manifests, duplication audit, immutable release

---

# 18. Governing rule

When the method and a prior interpretation disagree, the method governs.

When the method and primary evidence disagree, the evidence governs.

When evidence remains ambiguous, the ambiguity must survive into the synthesis.
