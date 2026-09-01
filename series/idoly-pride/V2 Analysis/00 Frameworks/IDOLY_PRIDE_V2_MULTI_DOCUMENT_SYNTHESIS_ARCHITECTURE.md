---
title: "IDOLY PRIDE V2 Multi-Document Synthesis Architecture"
project: "IDOLY PRIDE"
document_id: "IDOLY_PRIDE_V2_MULTI_DOCUMENT_SYNTHESIS_ARCHITECTURE"
version: "2.5"
status: "governing-framework"
created: "2026-08-13"
updated: "2026-08-19"
live_corpus_model: "mutable rolling workspace plus immutable dated releases"
target_substantive_documents: "approximately 20 reader-facing documents plus a per-character modeling/simulation profile family, expandable when analytical scale requires"
release_model: "rolling source deltas -> ledgers -> specialist synthesis -> evidence routing -> continuous synthesis -> immutable dated package"
---

# IDOLY PRIDE V2 MULTI-DOCUMENT SYNTHESIS ARCHITECTURE

## 1. Purpose

This architecture replaces conversational sprawl with a stable analytical corpus.

It separates:

- framework;
- source lock;
- working ledgers;
- unit/character synthesis;
- holistic character modeling, experiential reconstruction, and simulation profiles;
- cross-unit thematic synthesis;
- audiovisual/formal analysis;
- continuous full-series synthesis;
- evidence routing;
- audit/manifests;
- final release.

No single document is expected to hold everything.

The corpus should support both human reading and reliable machine retrieval.

---

# 2. Canonical directory model

```text
V2 Analysis/
|-- 00 Frameworks/
|-- 01 Source Lock and Inventory/
|-- 02 Source Audits and Longitudinal Ledgers/
|   |-- 02.01 Corpus Coverage and Priority Ledger/
|   |-- 02.02 Character Longitudinal Ledgers/
|   |-- 02.03 Relationship and Unit Ledgers/
|   `-- 02.04 Theme Motif and Institution Ledgers/
|-- 03 Unit and Character Syntheses/
|   |-- 03.01 Foundational Characters and Inheritance/
|   |-- 03.02 SUNNY PEACE/
|   |-- 03.03 Tsuki no Tempest/
|   |-- 03.04 LizNoir/
|   |-- 03.05 TRINITYAiLE/
|   |-- 03.06 IIIX/
|   |-- 03.07 DoriKyun BIG4 and External Units/
|   `-- 03.08 Character Modeling and Simulation Profiles/
|-- 04 Relationships and Thematic Syntheses/
|   |-- 04.01 Relationships Intimacy Rivalry and Care/
|   |-- 04.02 Grief Memory Survival and Inheritance/
|   |-- 04.03 Idolhood Audience and Performance/
|   |-- 04.04 Professional Labor Industry and Institutions/
|   `-- 04.05 Manager Production and Guidance/
|-- 05 Audiovisual Music and Performance Analysis/
|   |-- 05.01 Anime Formal Audit/
|   |-- 05.02 Game Music 3DMV and Live Performance/
|   |-- 05.03 Voice Register and Telephone Audio/
|   `-- 05.04 Visual Design Card Art and 4koma/
|-- 06 Full-Series Synthesis/
|-- 07 Evidence Indexes and Claim Routing/
|-- 08 Audits and Manifests/
`-- 09 Final Release/
```

Primary-source files remain outside this analysis tree.

---

# 3. Governing framework documents

`00 Frameworks` should contain at minimum:

- `IDOLY_PRIDE_V2_ANALYTICAL_METHOD.md`
- `IDOLY_PRIDE_V2_MULTI_DOCUMENT_SYNTHESIS_ARCHITECTURE.md`
- `IDOLY_PRIDE_V2_SOURCE_EVIDENCE_AND_LEDGER_PROTOCOL.md`

Optional later additions:

- `IDOLY_PRIDE_V2_NAMING_AND_ROMANIZATION_POLICY.md`
- `IDOLY_PRIDE_V2_AUDIOVISUAL_AUDIT_PROTOCOL.md`

The framework directory defines how work is done, not the findings themselves.

---

# 4. Source-lock artifacts

`01 Source Lock and Inventory` should ultimately contain:

## `SOURCE_MANIFEST.md`

Human-readable inventory of source roots, source classes, corpus snapshot date, analysis-bundle version, ingest version, anime bundles, songs/3DMVs, visuals, 4koma, telephone status, and known gaps.

## `SOURCE_MANIFEST.json`

Machine-readable equivalent where practical.

## `SOURCE_CUTOFF_AND_PROJECT_DECISIONS.md`

Record:

- canonical cutoff date;
- treatment of the player-facing game manager as continuing Makino Kouhei, with custom naming treated as interface parameterization and selectable dialogue handled through branch-canon semantics;
- source hierarchy;
- ASR treatment;
- 4koma treatment;
- prior-analysis treatment;
- continuity exceptions;
- known missing assets;
- unresolved source questions.

## `CORPUS_INTEGRITY_AUDIT.md`

Record technical validation relevant to analysis.

## 4.1 Live-corpus maintenance artifacts

Because the game remains live, `01 Source Lock and Inventory` and `02 Source Audits and Longitudinal Ledgers` also maintain the rolling update frontier.

Recommended files:

- `SOURCE_DELTA_LEDGER.md` - additions, modifications, removals/replacements, and newly available assets between source snapshots;
- `SOURCE_SNAPSHOT_HISTORY.md` - dated snapshot identifiers and their relation to frozen analytical releases;
- `CHARACTER_UNIT_UPDATE_STATUS.md` - freshness frontier for each major character/unit;
- `PENDING_REANALYSIS_QUEUE.md` - new material whose semantic impact has been classified but not yet incorporated into every affected synthesis;
- `RELEASE_CHANGELOG.md` - analytical changes between frozen releases.

These are rolling administrative artifacts. They should not be mistaken for reader-facing synthesis documents.

A new source snapshot does not create a new analytical release automatically. Release creation is driven by semantic impact and coherence.

---

# 5. Working ledgers

Working ledgers are the project's epistemic machinery. They do not all belong in the final reader package.

## 5.1 Corpus coverage and priority ledger

Canonical filename:

`IDOLY_PRIDE_V2_CORPUS_COVERAGE_AND_PRIORITY_LEDGER.md`

This supersedes historical event-priority lists.

It answers:

- what has been read;
- what matters and why;
- what remains unread;
- which V1 conclusions are vulnerable;
- which items require audiovisual review.

## 5.2 Character longitudinal ledgers

Create one per major character when scale warrants it.

Example:

`IDOLY_PRIDE_V2_CHAR_MIHO_LONGITUDINAL_LEDGER.md`

The ledger is evidence-bearing reconstruction, not polished biography.

Makino additionally requires:

`IDOLY_PRIDE_V2_MAKINO_PLAYER_BRANCH_CANON_LEDGER.md`

This is **not** an identity-equivalence ledger. The governing project decision already treats the customizable game manager as Makino Kouhei. The ledger distinguishes fixed Makino facts/actions from mutually exclusive player-selected expressions and records the authored range of Makino-compatible responses without falsely making every branch co-occur.

Phase 1 also maintains a Hoshimi cross-media expansion matrix mapping `st-original-cmn` blocks to anime episodes and recording added Makino POV, explicitated motive/professional reasoning, added context, branch parameterization, reframing, anime-only audiovisual form, and genuine continuity tensions.

### Phase 1B ordered dependency architecture

Phase 1B uses the **main story as the present-tense longitudinal spine** while inserting unit-origin material at controlled disclosure boundaries. Each origin ledger/audit records both where its events occur in-world and when its information becomes analytically available. Required routing fields are:

- `diegetic_position`;
- `disclosure_position`;
- `prerequisite_main_story_state`;
- `retrospective_targets`;
- `forward_inheritance_point`.

Canonical execution order after the completed Hoshimi anime/game expansion audit:

1. SUNNY PEACE origins: `origin_sun_001`-`origin_sun_005`;
2. Tsuki no Tempest origins: `origin_moon_001`-`origin_moon_005`;
3. LizNoir origins: `origin_liz_001`-`origin_liz_010`;
4. TRINITYAiLE origins: `origin_tri_001`-`origin_tri_006`;
5. conditional Hoshimi cross-media audit addendum;
6. IIIX origins: `origin_thrx_001`-`origin_thrx_004` - **mandatory before Tokyo**;
7. Tokyo main story `001`-`014`;
8. BIG4 main story `001`-`014`;
9. Stellar main story `001`-`011`;
10. remaining source classes according to disclosure dependencies;
11. full event reranking against the stabilized Tier-A reference state.

The SUNNY PEACE/Tsuki/LizNoir/TRINITYAiLE origin tranche is allowed to revise the Hoshimi expansion audit because those stories may establish that an apparent game-main-story addition originates in a dedicated unit history, or may add prequel/concurrent/post-Hoshimi information relevant to anime-era characterization. Such changes must be emitted as explicit addenda or claim revisions.

The IIIX origin tranche is a **hard interpretive dependency** for Tokyo rather than optional background: its frozen output defines IIIX's pre-Tokyo character, relationship, unit, and professional-philosophy baseline.

## 5.3 Relationship ledgers

Create for relationships that materially exceed ordinary character-note scale.

Examples include:

- Kotono/Nagisa;
- Mana/Kotono;
- Mana/Makino;
- Sakura/Kotono;
- Rio/Aoi;
- miho/Yo;
- kana/Kokoro;
- the IIIX internal triad.

## 5.4 Unit ledgers

Track unit development rather than merely member summaries.

## 5.5 Theme and institution ledgers

Track series-level recurrences before thematic prose is written.

---

# 6. Reader-facing synthesis corpus

The mature corpus should target approximately twenty substantive documents. Numbering may be refined during drafting.

## `00_README_AND_CORPUS_MAP.md`

Written last.

Contains the mature executive thesis, source/spoiler boundaries, version, document map, reading paths, evidence labels, naming conventions, known limitations, and release pointers.

## `01_SERIES_ARCHITECTURE_CHRONOLOGY_AND_NARRATIVE_PROGRESSION.md`

Distinguish release chronology, in-universe chronology, and character-development chronology. Map major game-era arcs and the expansion beyond the anime.

Draft relatively late.

## `02_MANA_MAKINO_MEMORY_MIRACLE_AND_INHERITANCE.md`

Foundational structural document covering Mana as person, sister, idol, public myth, professional standard, ghost/absence, and inheritance problem; plus Makino and Hoshimi as living continuation rather than shrine.

## `03_SUNNY_PEACE_UNIT_AND_CHARACTER_SYNTHESIS.md`

Unit formation, Sakura, Rei, Haruko, Chisa, Shizuku, reciprocal support, performance philosophy, fandom/audience relation, mature unit identity.

If above approximately 25-30k words, split into unit synthesis and character profiles.

## `04_TSUKI_NO_TEMPEST_UNIT_AND_CHARACTER_SYNTHESIS.md`

Kotono, Nagisa, Saki, Suzu, Mei; grief/inheritance; disciplined illumination; rivalry; relationship structure; performance language; mature post-defeat identity.

## `05_LIZNOIR_UNIT_AND_CHARACTER_SYNTHESIS.md`

Rio, Aoi, Ai, Kokoro; adult/professional idolhood; career longevity; perfection and warmth; rivalry; youth sacrificed to career; domestic/professional unit rhythm.

## `06_TRINITYAILE_UNIT_AND_CHARACTER_SYNTHESIS.md`

Rui, Yu, Sumire; elite idolhood; professionalism; gratitude; fandom; perfection and emotional accessibility; creative process.

## `07_IIIX_UNIT_AND_CHARACTER_SYNTHESIS.md`

Expected to be one of the largest documents.

Covers fran, miho, kana, unit origin, beauty/authorship, grief/control, abandonment/visibility, money/material production, media strategy, hostile intimacy, American arc, dissolution/re-foundation, Hoshimi integration, mature IIIX, and adversarial public authenticity.

Prefer splitting if above 25-30k words.

## `08_DORIKYUN_BIG4_EXTERNAL_UNITS_AND_COMPETITIVE_ECOSYSTEM.md`

DoriKyun, BIG4, major external rivals, antagonistic mentorship, global ambition, industry disruption, tournament ecology, competitive legitimacy, and external pressure on Hoshimi.

## `09_RELATIONSHIPS_INTIMACY_DEPENDENCE_RIVALRY_AND_CARE.md`

Organize by relationship form rather than one mini-biography per pair.

Major axes: sisters, best friends, rivals, hostile intimacy, senior/junior bonds, caretaking, dependency, memory bonds, cross-unit friendship, producer/idol relations, chosen professional family.

## `10_GRIEF_DEATH_MEMORY_SURVIVAL_AND_CONTINUITY.md`

Mana, Yo, Sakura's survival, Kotono, Makino, Haruko, Rio, miho, memorial objects, bodily memory, public myth, private grief, song as memorialization, performance as continuity, survival guilt, inheritance vs replacement.

## `11_PROFESSIONAL_IDOLHOOD_LABOR_MONEY_AND_INDUSTRY.md`

Management, training, scheduling, contracts where evidenced, money, competition, brand/image labor, adult idolhood, career sustainability, burnout, overseas work, media, professional discipline, agency structure.

This document prevents the corpus from reducing *IDOLY PRIDE* to interpersonal psychology.

## `12_IDOLHOOD_AUDIENCE_RECOGNITION_AND_PERFORMANCE.md`

Compare how characters and units answer "what is an idol?" Candidate answers include miracle, memory, hope, proof, gratitude, fun, professionalism, competition, self-authorship, public survival, and mutual illumination.

Shizuku is especially important to the fan/performer boundary.

## `13_MANAGER_PRODUCTION_AUTONOMY_AND_THE_ETHICS_OF_GUIDANCE.md`

Treat Makino as producer and character, not merely player infrastructure. The player-facing game manager is the continuing Makino Kouhei; custom naming is interface parameterization, while selectable dialogue defines branch-specific authored possibilities rather than multiple simultaneously canonical utterances. Cover intervention, autonomy, emotional labor, talent judgment, boundaries, career steering, relationship to Mana, individualization, and the ethics of producing people rather than merely performances.

## `14_JAPANESE_VOICE_REGISTER_AND_RELATIONAL_GRAMMAR.md`

Pronouns, sentence endings, politeness, vocatives, nicknames, ojou-sama register, stage names, teasing, commands, apology, aggression, affection, register shifts, public/private voice, message voice, relationship-specific changes.

## `15_ORDINARY_LIFE_MESSAGES_CARDS_BONDS_AND_SOCIAL_TEXTURE.md`

Show what low-pressure material contributes: social rhythm, indirect care, everyday professionalism, unit culture, and post-event continuity.

Messages should not be dismissed as filler simply because they are low-stakes.

## `16_VISUAL_DESIGN_COSTUME_STAGECRAFT_AND_PERFORMANCE_LANGUAGE.md`

Card illustration, costume, color, silhouette, stage blocking, choreography, camera, lighting, audience, recurring objects, body language, 3DMV, anime performance form, visual echoes.

Do not invent visual claims from prose-only sources.

## `17_COMPARATIVE_REFERENCE_MATRICES_AND_OPEN_QUESTIONS.md`

Matrices for wound/pressure, desire, defense, idol philosophy, relation to Mana, audience, failure, labor, performance, speech, relationship form, maturity, and source confidence. Preserve unresolved continuity questions.

## `18_EVIDENCE_LOCATOR_AND_CLAIM_REVISION_LEDGER.md`

For every load-bearing synthesis claim record claim ID, summary, target document, epistemic class, supporting ledger entries, source IDs, exact story IDs, audiovisual evidence, counterevidence, V1 status, V2 revision, confidence, and unresolved issues.

This is the accountability document.

## `19_IDOLY_PRIDE_FULL_SERIES_SYNTHESIS.md`

The continuous literary argument.

It should not recap Documents 01-18. It should explain the work as a whole.

A provisional organizing thesis is:

> *IDOLY PRIDE* is a story about what living people do after a miracle becomes memory: how they inherit without copying, compete without erasing, remember without becoming mausoleums, and turn private wounds into performances that can reach other people.

That formulation remains provisional until V2 is complete.

## 6.1 Holistic Character Modeling and Experiential Profile framework

The architecture additionally defines a **derived holistic character-modeling layer** under:

`03 Unit and Character Syntheses/03.08 Character Modeling and Simulation Profiles/`

Do **not** create the directory merely for symmetry while it is empty. Create it when the first profile is emitted.

### Governing division of analytical labor

The modeling-profile family has a deliberately different responsibility from the longitudinal and synthesis corpus.

The upstream character ledgers and literary syntheses principally answer:

> **Who is this person across time? What formed them, what drives them, what wounds or contradictions organize them, what do they learn, how do their relationships change, and what thematic or structural role do they play in the work?**

The modeling profile principally answers:

> **What is it actually like to know this person at conversational distance? What would it be like to spend a day with them, talk with them, watch them choose what to do, and notice what they enjoy, avoid, buy, eat, listen to, collect, joke about, get embarrassed by, become excited about, or do when nothing dramatic is happening?**

This distinction is architectural, not merely stylistic. The longitudinal/synthesis layer explains the character **from the outside and across time**. The modeling profile reconstructs the character **as a lived social person from conversational distance**.

Character-specific ordinary-life information therefore has its canonical mature home in the modeling profile when it is useful for lived-person reconstruction. A longitudinal ledger should still preserve a hobby, preference, fandom, domestic habit, or mundane weakness when it materially explains development, contradiction, relationship state, or a literary claim, but it should not become an exhaustive lifestyle catalogue merely to prevent data loss.

### Canonical profile granularity

Prefer one profile per character at this corpus scale.

Canonical naming grammar:

`IDOLY_PRIDE_V2_CHAR_<CHARACTER>_MODELING_PROFILE.md`

Examples:

- `IDOLY_PRIDE_V2_CHAR_MEI_MODELING_PROFILE.md`
- `IDOLY_PRIDE_V2_CHAR_KOTONO_MODELING_PROFILE.md`
- `IDOLY_PRIDE_V2_CHAR_RIO_MODELING_PROFILE.md`
- `IDOLY_PRIDE_V2_CHAR_SAKI_MODELING_PROFILE.md`

A single omnibus `IDOLY_PRIDE_V2_CHARACTER_MODELING_AND_SIMULATION_PROFILES.md` may later serve as a compact index/cross-character routing surface, but it should **not** replace the per-character canonical profiles when character scale warrants separate artifacts.

Do **not** create a permanent per-character preference or hobby document parallel to the modeling profile. That would split one semantic responsibility across near-duplicate homes. If systematic extraction needs a granular audit surface, an optional cumulative `IDOLY_PRIDE_V2_CHARACTER_TEXTURE_EVIDENCE_LEDGER.md` may be created later under `07 Evidence Indexes and Claim Routing`; it is evidence infrastructure, not the canonical human-facing characterization surface.

### Analytical responsibility

A modeling profile is **not** a new literary synthesis, a replacement for a character longitudinal ledger, or a source of new canon. Its distinct responsibility is to translate stabilized evidence into a holistic lived-person model that can support:

- character-consistent dialogue generation;
- realistic low-stakes conversation;
- behavioral and decision simulation;
- relationship-conditioned interaction;
- ordinary-life and day-in-the-life reconstruction;
- preferences, hobbies, fandoms, tastes, aversions, material habits, and domestic behavior;
- practical competencies and mundane weaknesses;
- humor, teasing, boredom, embarrassment, excitement, and recovery;
- counterfactual scenario analysis;
- cross-character ensemble simulation;
- reconstruction of likely speech, action, attention, and emotional response under explicitly stated uncertainty.

The profile should answer at least five different questions without conflating them:

1. **What does this character tend to notice, want, fear, value, and protect?**
2. **How does this character tend to choose and behave under different pressures?**
3. **What do they actually like doing, consuming, collecting, discussing, practicing, avoiding, or seeking out in ordinary life?**
4. **How does behavior change by interlocutor, relationship, public/private setting, activity, and developmental state?**
5. **How would the character characteristically express the resulting thought or action in Japanese?**

### Phase placement and sequencing

The default production home for these profiles is **Phase 8.5**, after the core longitudinal and synthesis program has substantially stabilized and after the continuous full-series synthesis exists.

The reason is methodological: exhaustive ordinary-life, preference, fandom, and conversational mining is valuable for reconstruction but should not block the higher-priority work of establishing longitudinal character causality, relationships, units, themes, institutions, and the literary argument of the series.

During Phases 1-8, preserve high-value texture when encountered and route it forward, but do **not** require every character ledger to exhaustively mine every card, message, event, bond, 4koma, or telephone scene for lifestyle facts.

Phase 8.5 then performs a targeted character-by-character re-sweep of already covered source regions for experiential evidence that literary compression may have underweighted.

A profile may be emitted earlier as `active_provisional` only for an explicit operational need. Earlier emission does not change the default sequence and must state missing upstream dependencies. Canonical profile promotion normally belongs to Phase 8.5.

### Required upstream dependencies

A canonical modeling profile should normally be drafted only after the relevant inputs have stabilized. At minimum, consult:

1. the current character longitudinal ledger;
2. the relevant unit/character synthesis in Documents `03`-`07`;
3. any P2-C relationship ledger materially affecting the simulated interaction;
4. the relevant P2-D unit ledger for group-role behavior;
5. P2-F textual Japanese voice/register evidence;
6. `14_JAPANESE_VOICE_REGISTER_AND_RELATIONAL_GRAMMAR.md`;
7. `15_ORDINARY_LIFE_MESSAGES_CARDS_BONDS_AND_SOCIAL_TEXTURE.md`;
8. `09_RELATIONSHIPS_INTIMACY_DEPENDENCE_RIVALRY_AND_CARE.md` where relational behavior is load-bearing;
9. `05.03 Voice Register and Telephone Audio` and other performed-voice evidence where delivery matters;
10. `16_VISUAL_DESIGN_COSTUME_STAGECRAFT_AND_PERFORMANCE_LANGUAGE.md` where body language or embodied performance matters;
11. `18_EVIDENCE_LOCATOR_AND_CLAIM_REVISION_LEDGER.md` and exact primary-source descent when a modeled trait is disputed or load-bearing;
12. `19_IDOLY_PRIDE_FULL_SERIES_SYNTHESIS.md` as the mature series-level interpretive boundary, so the experiential profile does not silently contradict the final literary model.

Document `15` remains a **series-level synthesis of what ordinary-life material does**. It is not required to become an encyclopedia of every person's favorite food, mascot, hobby, playlist, shopping habit, or fear. Those character-specific particulars belong in the modeling profile when they are sufficiently evidenced and behaviorally useful.

### Phase-8.5 experiential evidence sweep

For each character, Phase 8.5 should deliberately revisit source classes where low-stakes characterization is concentrated:

- events, including seasonal, travel, collaboration, leisure, cooking, shopping, competition, and work-comedy events;
- card stories;
- bond stories;
- messages/group chats;
- official 4koma;
- telephone audio where relevant;
- anime/game audiovisual scenes that establish body language, leisure behavior, or performed conversational affect;
- lower-stakes main/origin scenes where ordinary behavior is unusually revealing.

The sweep should preserve concrete particulars that literary synthesis may compress away: fandoms, mascots, favorite media, food/drink, shopping, collecting, fashion, games, books, music, sports, domestic habits, sleep, organization, money behavior, practical skills, fears, pet peeves, embarrassment triggers, leisure preferences, digital habits, and context-dependent enthusiasm.

Do not promote every isolated observation into a stable trait. Distinguish:

- **one-off fact** - directly observed once, little predictive force;
- **repeated preference** - recurring choice or explicit liking across sources;
- **stable disposition** - preference/habit generalized across contexts with meaningful recurrence;
- **behaviorally predictive trait** - evidence strong enough to constrain likely future behavior or conversation.

The profile may preserve all four categories, but it must label their evidentiary strength rather than converting trivia into personality by accumulation.

### Required profile contents

Each profile should operationalize, where evidence permits:

1. **identity and temporal state** - source snapshot, developmental endpoint, and earlier-state variants needed to prevent endpoint leakage;
2. **core lived impression** - what being around the character generally feels like in ordinary conditions, without reducing them to archetype shorthand;
3. **baseline temperament** - stable affective and interpersonal tendencies;
4. **motivation and value hierarchy** - what outcomes matter most and what values constrain action;
5. **attention and salience model** - what the character tends to notice first in people, environments, performances, conflict, work, leisure, or risk;
6. **daily-life rhythm** - planning, punctuality, sleep, work habits, preparation, organization, cleanliness, downtime, recovery, and ordinary routines;
7. **interests, fandoms, hobbies, and obsessions** - what the character voluntarily spends attention, time, money, or enthusiasm on;
8. **taste and material preferences** - food, drink, clothing, shopping, decor, gifts, media, music, preferred environments, possessions, mascots, and aesthetics where evidenced;
9. **likes, dislikes, fears, aversions, and pet peeves** - with one-off versus stable status clearly separated;
10. **competencies and mundane weaknesses** - cooking, technology, academics, athletics, navigation, money, household tasks, practical judgment, and other non-idol capabilities;
11. **decision heuristics** - recurring ways the character evaluates ordinary and serious choices, including known exceptions;
12. **emotional regulation and stress transitions** - what produces embarrassment, anger, withdrawal, overwork, impulsivity, defensiveness, openness, repair, or recovery;
13. **behavioral signatures** - initiative, avoidance, planning, improvisation, caretaking, competitiveness, novelty seeking, persistence, play, and work habits;
14. **humor and play model** - what the character finds funny, how they tease, what makes them flustered, how they react to bits/nonsense, and when comedy stops being socially safe;
15. **conversation model** - topics they initiate, questions they ask, how much they speak/listen, how they handle silence, enthusiasm/infodump triggers, avoided subjects, conversational repair, and topic-dependent changes in energy;
16. **digital communication model** - message length, timing, punctuation, stickers/emoji where evidenced, group-chat behavior, telephone behavior, and differences from face-to-face speech;
17. **conflict and repair behavior** - how the character disagrees, escalates, apologizes, forgives, re-engages, or preserves boundaries;
18. **failure and recovery model** - how defeat, criticism, exclusion, uncertainty, fatigue, grief, or public pressure alter behavior;
19. **relationship-conditioned state changes** - how speech, expectations, vulnerability, teasing, aggression, care, deference, and initiative change around specific people;
20. **group-role behavior** - center/leader/support/mediator/instigator/observer/organizer functions where evidenced, while avoiding permanent role captivity;
21. **care and affection model** - direct versus indirect care, physical/verbal affection, practical help, gift behavior, concern, jealousy, protectiveness, and limits;
22. **textual speech grammar** - pronouns, forms of address, politeness, sentence endings, lexical preferences, fillers, hesitation, commands, apologies, intensifiers, teasing, aggression, softness, and code/register shifts;
23. **public/private/message/stage register** - explicit separation where the source supports different voices;
24. **performed-voice layer** - prosody, pitch/register, breathiness, laughter/crying texture, vocal tension, and delivery only when audiovisual evidence exists;
25. **body-language and embodied-behavior layer** - gesture, posture, proximity, kinetic style, facial control, and stage/offstage physicality only when visual evidence exists;
26. **day-in-the-life reconstruction** - an evidence-constrained description of an ordinary day or outing, clearly marked as derived reconstruction rather than an unseen canonical event;
27. **scenario behavior ranges** - restaurant, shopping, travel, party, work crisis, argument, hobby event, unexpected gift, quiet evening, and comparable contexts where the profile has enough evidence to generalize;
28. **out-of-character constraints** - reactions, attitudes, vocabulary, or behavioral shortcuts that the evidence makes unlikely;
29. **uncertainty and alternative-response ranges** - plausible multiple reactions where canon does not justify deterministic prediction;
30. **evidence-backed preference inventory** - concise character-specific facts with source locator, recurrence class, temporal scope, confidence, and behavioral relevance;
31. **open dependencies** - missing relationship, telephone, audiovisual, branch, chronology, or later-snapshot evidence that would materially alter profile confidence.

### Preference-inventory evidence fields

A mature preference/texture entry should ideally preserve:

```yaml
category:
item_or_behavior:
epistemic_class:
recurrence_class: one_off | repeated_preference | stable_disposition | behaviorally_predictive
source_ids:
temporal_scope:
relationship_or_context:
confidence:
behavioral_relevance:
notes:
```

The goal is not trivia accumulation. The goal is to preserve the concrete details that make the person socially recognizable and behaviorally reconstructable.

### Relationship-conditioned simulation rule

Character behavior must not be modeled as context-free. For a simulated interaction between known characters, the retrieval path should include both character profiles plus the relevant relationship/unit evidence.

For example, simulating Nagisa speaking to Kotono should use:

> Nagisa modeling profile -> Kotono modeling profile -> Kotono/Nagisa relationship ledger/synthesis -> Tsuki unit state -> Japanese relational grammar -> ordinary-life/experiential profile evidence -> exact source when needed.

This prevents a superficially accurate "Nagisa voice" from being paired with behavior she would use only with a different interlocutor.

### Temporal-state rule

Do not project a mature endpoint backward into an earlier simulation. Each profile should identify the state being modeled, such as:

- origin/pre-Hoshimi;
- anime/Hoshimi era;
- post-Tokyo;
- post-BIG4;
- post-Stellar;
- locked-snapshot mature endpoint.

If a requested scenario occurs earlier, use only knowledge, habits, relationships, and developmental capacities available at that point. Later understanding may be used analytically to explain the difference, but not silently inserted into the character's earlier mind.

### Speech-generation rule

Do not reduce voice to catchphrases or copied source sentences. Model **distributions and transformations**:

- what level of politeness is likely here;
- which pronoun/vocative is likely with this interlocutor;
- whether the character tends toward direct assertion, hedging, teasing, silence, rhetorical exaggeration, practical phrasing, or enthusiastic over-explanation;
- how emotional pressure or favored topics change syntax/register;
- how text-message voice differs from face-to-face voice;
- how public idol speech differs from private speech.

Source quotations remain evidence, not reusable canned dialogue. Generated dialogue should be novel reconstruction constrained by the source model.

### Behavioral simulation rule

Treat behavior as a **probabilistic evidence-constrained range**, not a deterministic script. A profile may identify:

- high-likelihood response;
- plausible alternate response;
- trigger conditions that shift the response;
- evidence that would make a reaction unlikely or out of character.

This is especially important for characters whose growth consists of gaining multiple available strategies rather than replacing an old personality with a new one.

### Canon and epistemic guardrail

A generated simulation is **not canonical evidence**. The authority chain is:

> primary source -> ledger/synthesis/evidence routing -> holistic modeling profile -> generated simulation

Never reverse that chain. A simulation may test whether the model is coherent, reveal missing evidence, or suggest a source question, but generated material must never be cited as proof of characterization.

For Makino, branch-canon semantics remain mandatory: mutually exclusive player-selected expressions must not be merged into one simultaneously canonical history. For all characters, `OPEN`, ambiguity, formal gaps, and source-snapshot boundaries remain active constraints rather than being "filled in" by the simulation layer.

### Machine-readable companion

A later profile may optionally emit a machine-readable companion, for example:

`IDOLY_PRIDE_V2_CHAR_MEI_MODELING_PROFILE.json`

The Markdown profile remains the human-auditable authority. The structured companion should contain pointers/normalized fields rather than silently introducing claims absent from the Markdown profile.

---

# 7. Working vs final vs archival layers

## Working layer

- source audits;
- character ledgers;
- relationship ledgers;
- theme ledgers;
- routing tables;
- duplicate checks;
- source-gap reports.

## Final human-readable layer

Primarily Documents `00-19`, plus selected evidence indexes.

## Derived holistic character-modeling layer

- per-character `IDOLY_PRIDE_V2_CHAR_<CHARACTER>_MODELING_PROFILE.md` artifacts;
- holistic human-readable experiential profiles designed for both direct reading and machine retrieval;
- optional machine-readable companions after the Markdown authority exists;
- derived from current ledgers/syntheses and never a substitute for primary evidence;
- may be included in a release without being counted as additional numbered reader-facing Documents `00-19`.

## Archival layer

- manifests;
- checksums;
- release audit;
- machine-readable indexes;
- framework documents.

---

# 8. Metadata standard

Every canonical Markdown artifact should use YAML front matter.

Recommended fields:

```yaml
title:
project: "IDOLY PRIDE"
document_id:
version:
status:
source_cutoff:
source_classes:
characters:
units:
themes:
evidence_classes:
supersedes:
related_documents:
created:
updated:
```

Working ledgers may add:

```yaml
ledger_type:
coverage_status:
open_questions:
requires_audiovisual_review:
source_snapshot_id:
validated_through:
last_retested:
update_status:
```

For live-corpus documents, `update_status` should use a compact vocabulary such as `current`, `new-material-pending`, `reanalysis-required`, or `provisional`.

Modeling profiles may additionally use:

```yaml
artifact_type: character_modeling_profile
artifact_role: MODELING_PROFILE
character:
character_code:
simulation_scope:
experiential_profile_scope:
profile_readiness:
ordinary_life_status:
preference_inventory_status:
conversation_model_status:
linguistic_model_status:
performed_voice_status:
relationship_dependencies:
required_upstream:
open_dependencies:
validated_through:
```

`profile_readiness` should distinguish at minimum `active_provisional` from `canonical`. A profile is not canonical merely because its character ledger is complete if material relationship, voice/register, unit, or audiovisual dependencies remain unstabilized.

---

# 9. Naming standard

Use stable uppercase identifiers.

Examples:

- `IDOLY_PRIDE_V2_CORPUS_COVERAGE_AND_PRIORITY_LEDGER.md`
- `IDOLY_PRIDE_V2_CHAR_MIHO_LONGITUDINAL_LEDGER.md`
- `IDOLY_PRIDE_V2_REL_KOTONO_NAGISA_LEDGER.md`
- `IDOLY_PRIDE_V2_07A_IIIX_UNIT_SYNTHESIS.md`
- `IDOLY_PRIDE_V2_CHAR_MEI_MODELING_PROFILE.md`

Do not use filenames like `final_final_v2_revised.md` or `notes2.md`.

Version belongs in metadata and release package naming.

---

# 10. Cross-document duplication policy

Each major idea should have one canonical home.

Example: "miho's hair care as bodily memory of Yo."

Canonical home: miho character/IIIX material.

Cross-references: grief/memory document, visual/body-memory discussion, evidence ledger.

The other documents may summarize the point but should not reproduce the full argument.

A character modeling profile should likewise **operationalize and route** existing characterization rather than duplicate the full literary argument. Character-specific ordinary-life preferences, fandoms, habits, mundane competencies, aversions, and conversational triggers have their canonical mature home in the modeling profile unless they are independently load-bearing for a literary/longitudinal claim. Document `15` synthesizes what ordinary-life material does across the series; it is not the per-character fact repository. If a modeling-relevant literary claim changes upstream, revise the canonical topical home first and then propagate the resulting model delta into the profile.

---

# 11. Release architecture

The final release should contain:

- final synthesis documents `00-19`;
- governing frameworks;
- source manifest;
- evidence/claim ledger;
- per-character modeling/simulation profiles whose declared dependencies have reached release readiness;
- corpus manifest;
- delivery audit;
- checksums;
- optional machine-readable indexes.

Do not redistribute copyrighted primary-source payloads in the analytical release.

The release becomes immutable after audit. Future source additions are incorporated in the rolling workspace first and create a new frozen version only after impact review.

## Rolling workspace versus release history

The active folders `01-08` are mutable analytical workspace. `09 Final Release` stores immutable dated snapshots. A frozen release should never be overwritten merely because the game continues.

Recommended pattern:

```text
09 Final Release/
|-- IDOLY_PRIDE_V2_v1.0_YYYY-MM-DD/
|-- IDOLY_PRIDE_V2_v1.1_YYYY-MM-DD/
`-- ...
```

Each release should include a changelog identifying which new source deltas caused which claim/document revisions.

---

# 12. Recommended drafting order

1. Source lock and inventory.
2. Corpus coverage/priority ledger.
3. Character longitudinal ledgers.
4. Relationship/unit ledgers.
5. Theme/institution ledgers.
6. Unit/character syntheses.
7. Relationship and thematic syntheses.
8. Textual voice/register and audiovisual/formal audits needed to stabilize the literary/specialist corpus; preserve ordinary-life texture encountered here without requiring exhaustive lifestyle mining.
9. Series architecture.
10. Comparative matrices/open questions.
11. Evidence locator and revision ledger.
12. Continuous full-series synthesis.
13. **Phase 8.5 holistic character modeling profiles**: perform the targeted ordinary-life/preference/conversation re-sweep, compile each `IDOLY_PRIDE_V2_CHAR_<CHARACTER>_MODELING_PROFILE.md`, and optionally maintain a cumulative texture-evidence audit ledger.
14. README/corpus map.
15. Duplication/provenance/model-consistency audit.
16. Immutable release package.
17. After release, return to source-delta audit when a new corpus snapshot arrives; update affected ledgers/syntheses first, then propagate model and texture deltas into the relevant character profiles before freezing the next coherent release.

The architecture intentionally delays the mature full-series thesis until the evidence-bearing specialist layer exists. The holistic modeling profiles are delayed one step further: they are **post-synthesis experiential reconstruction**, not a prerequisite for completing core literary analysis. This prevents hundreds of low-stakes facts from interrupting the higher-priority task of stabilizing character causality, relationships, units, themes, institutions, and the series-level argument, while still preserving a deliberate later stage where those details become first-class characterization evidence.

---

# 13. Architectural rule

The project should always permit reverse navigation:

> **full-series synthesis -> specialist document -> ledger -> source locator -> extracted story or audiovisual evidence**

For character simulation, the additional chain is:

> **generated simulation -> holistic character modeling profile -> character/relationship/unit/voice/ordinary-life specialist evidence -> ledger or evidence route -> source locator -> extracted story or audiovisual evidence**

The first arrow is one-way for authority purposes: a generated simulation can be audited against the profile and sources, but it can never become evidence merely because it sounds convincing.

If a document cannot participate in the appropriate chain, it is either insufficiently sourced or stored at the wrong layer.
