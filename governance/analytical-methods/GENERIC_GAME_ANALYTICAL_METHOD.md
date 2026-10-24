---
title: Generic Source-Bounded Game Analytical Method
artifact_id: GENERIC_GAME_ANALYTICAL_METHOD
artifact_type: generic_game_analytical_method_reference
artifact_role: reusable_corpus_level_analytical_reference_method
version: "1.0"
status: canonical
scope: source-bounded analysis of game narratives, including live-service intake, branching and variant state, and extracted game data, and new-project method bootstrap
authority_scope: this_reusable_reference_only
adoption: opt_in
project_local_authority: false
created: 2026-10-24
maintainer: Claude + user
source_boundary: "Methodological reference only; no series findings or primary-source evidence"
do_not_use_as_current_authority: false
do_not_use_as_literary_evidence: true
canonical_home: governance/analytical-methods/GENERIC_GAME_ANALYTICAL_METHOD.md
drafted_against_commit: 6a3afaaf1bb61e0993db379ab4074c46e9ea98dd
supersedes: []
superseded_by: []
---

# Generic Source-Bounded Game Analytical Method

## Adoption and authority boundary

This artifact is a reusable, corpus-level analytical reference for source-bounded reading of game narratives: live-service games, gacha and idol games, visual novels, and offline or preserved games. It also supports new-project method design. It is canonical only for this reference responsibility, and adoption is opt-in. It is not a repository policy, a project-local governing method, a synthesis architecture, a current-state entrypoint, or literary evidence.

1. It does not govern an existing series merely by residing in Git.
2. It does not by itself satisfy a project's governing-method requirement or open a `SEQUENTIAL_ANALYSIS_LOCK`.
3. A new project adapts it after source reconnaissance, pairs it with a synthesis architecture (see the [architecture template](GENERIC_MULTI_DOCUMENT_SYNTHESIS_ARCHITECTURE_TEMPLATE.md)), and exposes both through its entrypoint.
4. Mature projects remain governed by their current methods.
5. Optional modules are activated only when the source earns them.

Game text is read in the `TEXT` lane; cards, CGs, sprites, and UI in `STILL_IMAGE`; cutscenes, music videos, voiced runtime scenes, and live footage in `CONTINUOUS_AV`, under the [routing policy](../source-policies/MANGA_ANIME_MEDIUM_AND_INSPECTION_LANE_ROUTING_POLICY.md) and the [generic continuous-AV method](GENERIC_CONTINUOUS_AUDIOVISUAL_ANALYTICAL_METHOD.md). Prose-reading discipline (narration, focalization, register) follows the [generic novel method](GENERIC_NOVEL_ANALYTICAL_METHOD.md); this method adds what games require on top of it.

## 0. Purpose

A game distributes its narrative across story modes, supplemental systems, data tables, presentation assets, voice, and time. What a player sees depends on the build, the route, the choices made, what has been unlocked, and when they played. A live-service game keeps adding to all of this.

The governing principle is:

> **Read a game as a versioned, state-dependent corpus. Every claim names the build it was read from, the state in which the content occurs, and the route by which the evidence was extracted.**

Three problems recur and organize this method:

- **Extracted data** (Part III): scripts, master tables, and asset dumps are powerful evidence that is easy to over-read.
- **Branching and variant state** (Part IV): content true in one state is not true in all.
- **Live-service intake** (Part V): new content must enter existing analysis without erasing what was true before.

---

# I. Epistemic boundary

## 1. Admitted horizon

The semantic evidence boundary is the **admitted horizon**: the exact inventory the project has admitted, up to its current frontier. For a prospective reading, it is the material up to and including the unit being read.

A live-service boundary is an exact, locked inventory, never "all current content" (handoff contract Section 4). A later release is a separate scope decision.

## 2. Separate orders

Keep these orders distinct and say which a claim depends on:

- **release chronology**: when content shipped (version, patch, event window);
- **diegetic chronology**: when events occur in the story world;
- **player epistemic order**: what a player could know at a given release;
- **character knowledge**: what each character knows at a given point;
- **unlock order**: when profile, archive, or bond material becomes visible;
- **retellings**: summaries, recaps, and retrospective framings, which are later sources about earlier events.

Undated, condition-ordered, and uncertainly placed content keeps that status. Do not flatten it into a tidy timeline. Event numbers and release order are metadata, not proof of in-world chronology. An unlock rank is not a calendar date.

**Cross-media sequencing.** Where a game sits beside an anime, manga, or live events, decide which medium is read prospectively first, freeze its findings, and only then let the other recontextualize them. Record each piece's disclosure position separately from its diegetic position, and mark hard prerequisites. When media disagree, each governs questions about itself: the anime governs the anime's audiovisual meaning; the game governs later game development. A later or longer source is not automatically privileged.

## 3. Reconnaissance limits and exposure

Game data exposes the future easily: titles, file names, table rows, and asset lists can reveal later content. Before a foundation is read, limit corpus-wide reconnaissance to schema, counts, hashes, IDs, native hierarchy, source sizes, and capability metadata. Do not search the future corpus for dialogue, revelations, or relationship outcomes.

Record unavoidable exposure, such as revealing titles, and prior knowledge of the game. Once a foundation is established, global retrieval **within the admitted horizon** is encouraged; out-of-horizon matches remain quarantined until a retrospective operation authorizes their use.

---

# II. Source model

## 4. Source classes

Admit sources by class, and state what each can support:

| Class | Supports | Boundary |
|---|---|---|
| Main story | Foundational events, causality, development | Dreams, performances, recollections, and unreliable statements keep that mode |
| Events | Longitudinal development; time-limited narrative | Window, reruns, and revisions recorded (Section 26) |
| Character, card, and bond stories | Fine-grained characterization, private behavior, relationships | Often unlock-gated or variant-specific (Part IV) |
| Supplemental lines: home, idle, area, messages | Ordinary behavior, speech, tastes, address | A repeatable interface line is not a dated, unique event or a relationship milestone |
| Profiles, archives, item and flavor text | Stated facts and framing | Often written in a narrator's or the game's voice; classify who is speaking |
| Choices and the player character | The designed option space; responses to the player | Not evidence of a player's personality (Section 19) |
| Presentation assets: sprites, CGs, cards, UI, movies | Presentation, iconography, staging | An asset's existence does not prove it was shown (Section 9) |
| Voice assets | Performed delivery, once resolved and actually listened to | Resolution to a speaker and scene must be shown, not assumed |
| Lyrics tables, recordings, music videos | Wording as stored; performed music | Not complete studio lyrics, sung alignment, or character testimony |
| Live performances | Performer embodiment and public presentation | Actor behavior is not evidence of a fictional character's private behavior |
| Cross-media adaptations | That adaptation's own story | Never automatically overwrite game events or character knowledge |
| Official paratext | Release anchors, official framing | Intention and publicity do not overrule what the story presents |
| Secondary references: wikis, fan transcripts, fan chronologies | Leads and retrieval | Research proxies; verify load-bearing claims; fan orderings are recommendations |

Source class and **narrative function** are separate axes. Classify each source's function as well (for example: spine, character core, ensemble, relational, texture, system). Function sets expected analytical weight; it does not rank authenticity. Texture material carries lower expected weight, not lower canonical reality, and a minor source can be decisive for a narrow question. Set priority from a corpus-wide relevance record, not from a curated list of what seemed important when someone first played.

## 5. Witness identity and the source lock

Every witness records: build or version, region, language, platform, acquisition and verification references (including any upstream extraction repository and commit), immutable source hashes, capabilities, limitations, admission scope, and analysis horizon. Bind them in a source lock under a corpus alias. Once published, an alias never changes its target; a changed corpus receives a new alias with an explicit crosswalk. Keep local paths out of Git.

The source lock freezes source identity and provenance, not interpretation. Version it: a minor increment for bounded additions, a major increment for a new era or a changed extraction method. Each increment records added, removed, and changed identities, count deltas, affected claims, and artifacts needing revision. Record the delta before moving any locator. No document calls itself current without naming its source lock. A re-upload, a copy, or a file rename is not a source delta.

## 6. Language witnesses

Name the semantic anchor, normally the original-language script. Official localizations and dubs are separate witnesses. Agreement among them can strengthen a semantic claim; divergence can reveal localization or performance choices. No localization replaces the anchor, and no dub defines the character universally.

---

# III. Extracted data

## 7. Native evidence and retrieval projections

Distinguish:

- **native evidence**: client assets, decrypted scripts, master data, and audio and video as the build stores them;
- **retrieval projections**: normalized JSON, databases, transcripts, search indexes, generated character or event bundles, and browsers built from native evidence.

Native evidence grounds claims. Projections make it findable. Correct a projection by returning to native evidence; a convenient derivative never overrules it. Runtime capture (recorded gameplay) governs runtime observations within its recorded build, route, and settings.

## 8. What a table row establishes

A master-data row establishes that the build stores that value under that key. It does **not** by itself establish:

- that players ever saw it, when, or under which conditions;
- that it is part of the story rather than a placeholder, test row, cut content, or unreleased future content;
- the speaker, when the row carries only a display label or technical ID;
- that two rows refer to the same scene, unless a key or pointer joins them.

Treat machine tables as **measurement evidence**, not interpretation. Retain deleted or inactive flags, conditions, and ordering fields with every cited row.

Likewise, script metadata establishes occurrence, not rendered effect: a camera or effect command is not what the player saw, a voice or music cue ID is not how it sounded, and an asset's file name is not its mood. Use cue and asset IDs to trace recurrence only after inspecting the actual asset.

**Counting and absence.** The evidence object is the unique source script or record, not each bundle or view that contains it. Deduplicate before counting, define what a count counts, and keep a deduplication record; duplicated appearances inflate frequency claims. An extract with no dialogue is not a lost scene: the raw file may still carry staging or system content. Phrase absence as "no instance found in the locked corpus", never as "never happens". A source not present in the lock is not evidence that something did not occur.

**Missing assets.** List assets that should exist but could not be extracted or processed. A textual claim survives an unrelated missing asset; a vocal, staging, or music claim that depends on it does not. Folder presence is not completeness; check at item level.

**Documented transformations.** Every extraction or normalization step records what it changed: wrapping, punctuation, encoding, placeholder handling. Keep player-name placeholders (such as `{user}`) raw rather than filling them in.

## 9. Assets are not playback

That an image, voice file, or movie exists in the build, or is referenced by a script, does not prove it was shown or played in a particular scene, in a particular order, or with a particular mix. Byte identity between two assets does not prove the same scene used them. Claim playback only from a resolved script reference with its conditions, or from runtime capture.

## 10. Joins

Extracted data is relational, and joins fail quietly. Rules:

- Never infer ownership or membership from a name or ID prefix.
- Native page, line, or index numbers are often unique only within one script or document. Qualify them.
- A null or missing link stays unbound until evidence binds it. Never coalesce a missing document reference to a default.
- Where a join yields zero, one, or many candidates, keep them all with a resolution confidence.
- Import ordinals of a database are not stable citations; cite the origin artifact and its row.
- Never silently substitute a near-matching ID, document, hash, or edition.

## 11. Identity adjudication

A display name, technical speaker ID, role ID, alternate form, compound speaker ("A and B"), hidden or generic ID ("???", "Student"), message ID, or voice object is not automatically one analytical person. Resolve identity through an explicit crosswalk with recorded decisions. Keep ambiguous and compound occurrences typed as such. Never globally map a generic ID unless the source proves it. Never silently upgrade a display label into a resolved character ID.

## 12. Unreleased, unused, and datamined content

Content present in data but not released (future events, cut scenes, unused lines, test text) belongs to a quarantined class. It is not inside the admitted horizon and may not support a narrative claim. If it is later released, it enters through intake (Part V) under its release identity, not as the earlier dump. Its earlier presence may be recorded as production evidence, never as foreshadowing.

## 13. Transcripts and machine outputs

Fan transcripts and mirrors are research proxies, not official publications. OCR, ASR, and machine translation are derivatives; record their method and confidence. Verify load-bearing verbatim claims against native data or rendered game assets.

Where speech exists only as audio (for example, voiced calls without a script), an ASR transcript is a provisional layer. Mark each passage as verified against the audio, ASR-supported, or a gap. ASR alone never supports claims about particles, register, pronouns, or exact quotation.

## 14. Locators

Use a versioned citation convention bound to the source lock, for example:

```text
<scheme>://<corpus-alias>/v1/script/<script-id>?doc=<document>#<field-pointer>
<scheme>://<corpus-alias>/v1/master/<table>?row=<n>&<native-key>=<value>#/<field>
<scheme>://<corpus-alias>/v1/asset/<asset-id>?kind=<kind>
```

State whether indexes are zero- or one-based. Percent-encode path and query values. For each claim, also record what applies:

- the language witness;
- the speaker identity status (resolved, ambiguous, compound, unresolved);
- the voice asset identity, for voice claims;
- the bounded AV witness and timestamp, for visual or performance claims;
- the state scope (Section 18).

A missing locator is better than a false one.

## 15. Packets and coverage

A **packet** is a bounded extract given to an analyst. It records the lock digest, exact membership and ranges, query and parameters, tool version, horizon and state filters, ordering basis, exclusions, unresolved joins, and an output hash. It includes complete page context, pages without dialogue, embedded documents, and every choice branch. A packet is disposable if it can be regenerated identically.

Keep a **coverage record** per source unit, with independent fields:

```text
inventoried | admitted_horizon | screened | narratively_reconstructed |
closely_analyzed | integrated_into_state | av_review_state | remaining_obligation
```

`NOT_SCREENED` and `DEFERRED` are not completion. Keep gaps as explicit sets, not just a highest-number frontier. Metadata discovery and machine equality checks do not mark a story as read. Completing a script requires every native page, embedded document, and choice branch to be accounted for.

## 16. Public-repository boundary

Scripts, master tables, transcripts, databases, and media stay in the evidence plane, outside Git. Git carries analysis, bounded paraphrase, brief quotations where necessary, locators, digests, typed state, and coverage decisions. No local path is part of a public citation.

---

# IV. Branching and variant state

## 17. State dimensions

Content in a game can be conditional on many dimensions. Identify those the source has:

| Dimension | Examples |
|---|---|
| Route or branch | Character routes, story branches, endings |
| Choice outcome | Dialogue choices and their responses |
| Progression and unlock | Bond or affection rank, chapter clears, item or level gates |
| Variant | Cards, costumes, alternate versions, seasonal or collaboration editions of one character |
| Context class | Ordinary continuity, alternate-world or special events, April Fools, collaborations |
| Parallel continuity or era | Separate story structures, timelines, or game generations |
| Manifestation or persona | One entity appearing in several forms, or under several public identities |
| Operational context | Disguise, mission role, combat condition, tactical secrecy |

## 18. State scope on every claim

Scope each claim to the states it was observed in, for example:

```yaml
state_scope:
  continuity: <stack or era>
  route: <route or common>
  variant: <base or variant ID>
  unlock: <condition, or none>
  context_class: ORDINARY | CONDITIONED | ALTERNATE | SPECIAL | UNDATED | UNRESOLVED_PLACEMENT
  release: <version or event>
```

Score each source's **continuity placement** separately from its internal order. A useful scale:

| Class | Placement |
|---|---|
| C0 | Fixed anchor: placed in one continuity at a known point |
| C1 | Strong longitudinal: ordered within a line of development |
| C2 | Floating: in continuity, but its position is uncertain |
| C3 | Branch variant: true only within a branch or result state |
| C4 | Flexible side continuity: coherent internally, loosely attached globally |

A card story can be C1 internally and C4 globally; that is a placement judgment, not a lesser canon.

Rules:

- What is true on one route is not true on another until shown.
- Never infer a branch's meaning from a label or file-name suffix such as "true", "normal", "bad", or a number; it may mark a result grade, a terminal failure, a world-state branch (one that changes shared facts), or a runtime composition fragment. Establish which from the source.
- A "true"-labeled route is a labeled branch, not the sole canon, unless the source says so.
- Results from mutually exclusive branches are each valid only inside their branch. Never average them.
- A trait that recurs across mutually exclusive branches is an invariant and earns higher confidence than a trait found on one branch only.
- Branch-conditioned possibility is not biography. For each branch record whether its content is safe to use in a character's biography: yes, conditionally, invariants only, or no. Write branch-scoped prose explicitly ("in the failure branch…").
- A variant's behavior does not define the base character. A seasonal card's story is evidence about that variant in that context.
- Unlock-gated material does not define every state of a relationship; a high-rank bond line describes that rank.
- Alternate, special, and collaboration contexts stay separate from ordinary continuity unless the source establishes continuity.
- Operational context is not development. A disguise or mission role is not a personality change without evidence.
- A manifestation's appearance is not generalized across all manifestations of the entity.

## 19. Choices and the player character

Record every branch of a consequential choice, and the responses to each, with a choice-group ID, an option ID, and any fixed consequence shared by all options. A choice's options show the designed option space; they are not evidence of a player's personality or of which option is canonical. A trait shown in only one exclusive option is labeled as such.

Treat the player character's material (producer, teacher, commander, protagonist proxy) as its own evidence class, and classify each part:

| Class | Meaning |
|---|---|
| Identity-invariant | Fixed facts about the player character across all play |
| Branch-invariant | The same in every option of a choice |
| Player-selected | Present only in the option chosen |
| Interface parameter | Custom names and placeholders; not characterization |

The player character is a designed position, often deliberately underdetermined; do not collapse selectable responses into one personality. Characters' responses to the player character are conditional evidence: "if addressed this way, responds this way".

Where the game marks a canonical path, or later content presupposes one choice, record that as a source fact, with its locator.

## 20. Parallel continuities

Keep an independent source frontier, semantic horizon, state horizon, and completion state for each continuity or era. A later continuity may open only through a transition decision recorded in the entrypoint. A connection found later between continuities is retrospective evidence, recorded as a typed bridge; it does not alter a completed continuity's frozen account.

---

# V. Live-service intake

## 21. Three current boundaries

Record in the project entrypoint:

| Boundary | Meaning |
|---|---|
| `SOURCE_CURRENT` | Newest material ingested into the evidence corpus |
| `ANALYSIS_CURRENT` | Newest material read, interpreted, and integrated into the canonical analysis |
| `RECONSTRUCTION_CURRENT` | Newest state considered safe as the default for character modeling |

These boundaries may differ, per scope. Source-current material must not silently change analysis-current or reconstruction-current authority. Make the lag visible: integrated, partially integrated, and pending material, per scope.

## 22. Intake lifecycle

```text
new release
  -> source lock update (new alias or explicit increment, with crosswalk)
  -> staging (an analytical holding area, not a second archive)
  -> one-time relevance screen of the complete release
  -> impact triage per scope with a mature baseline
  -> required reading
  -> claim revision
  -> character, relationship, and epistemic state updates
  -> reconstruction delta
  -> promotion; analysis-current advances only for the scope integrated
```

## 23. Relevance screen and impact triage

Keep two responsibilities apart:

- **Relevance routing** records what a release contains and where later analysis should look: represented characters, relationships, and groups; relevance (`PRIMARY`, `SECONDARY`, `CROSS_GROUP`, `INCIDENTAL`, `NONE`, `UNRESOLVED`); evidence domains; exact locators. Screen each release once, at the scope of the whole game, so later work reuses the screen instead of repeating it.
- **Impact triage** records what the release changes relative to an established baseline:

| Class | Meaning | Treatment |
|---|---|---|
| `I0 RECORD_ONLY` | No meaningful change | Keep retrievable |
| `I1 CHARACTERIZATION_INCREMENT` | More evidence for an established trait, preference, or tendency | Index; possibly `STRENGTHEN` |
| `I2 INTERPRETIVE_REFINEMENT` | Changes how established behavior or a relationship should be understood | Claim-revision review; targeted updates |
| `I3 STATE_CHANGING` | Durable psychological, relationship, epistemic, or group transition | Full reading, ledger updates, reconstruction review |

Impact is analytical consequence, not marketing prominence or rarity. Where a scope has no mature baseline, record relevance and set impact to `DEFERRED_PENDING_FOUNDATION`.

## 24. Historical state preservation

States are append-only. When a character moves from state M4 to M5, M4 remains authoritative for scenarios set during its validity period. Never rewrite an earlier state to resemble the current one. Relationship and epistemic states follow the same rule: later disclosure does not erase earlier ignorance, and later intimacy is not projected backward.

Character, relationship, and epistemic state change independently. A character may stay psychologically stable while one relationship changes, or while learning something that changes behavior immediately.

## 25. Selective updates and synthesis generations

A new release involving a character does not justify rewriting a monograph or model. Update only the responsibilities that changed: self-concept, a specific relationship, knowledge, ordinary behavior, stress response, speech, values, or group role. Mutable ledgers and models absorb incremental change.

Create a new synthesis generation only at a meaningful milestone (completion of an arc, a major state transition, accumulated change that makes the previous synthesis materially obsolete), never for calendar time alone. A full reread generation is justified when the method improves, not merely because new content exists.

**Retesting claims.** Give claims a `validated_through` boundary, a `last_retested` date, and the source lock they were tested against. A new release retests affected claims rather than appending another citation. `validated_through` advances only when the claim was actually retested against the new material, never because a snapshot exists or an unrelated story shipped. A substantial main-story release triggers review of every `OPEN`, unresolved, or conflicting claim it could bear on. A release record may not claim coverage through a cutoff while `I2` or `I3` work for that cutoff is pending. New characters and groups start provisional and are promoted when they have enough independent appearances. Keep a freshness record so that syntheses made stale by later releases are visible.

## 26. Content lifecycle

| Event | Rule |
|---|---|
| Time-limited content | Record its availability window. Analysis uses a preserved witness, not memory of the event |
| Rerun | The same content in a new window adds no evidence unless the content changed |
| Addition of new sources or assets | Admit through intake with the release's identity |
| Revision or patch, including an upstream extraction correction | Revised text or presentation is a new dated witness; record the variant and keep both |
| Replacement | The replaced source remains evidence for its builds; record the successor link |
| Removal | Removed content remains evidence for the builds that contained it; flag its status |
| Rework or retcon | Classify as revision, retcon, or clarification. Preserve the earlier state as true for its period |
| Service end or offline preservation | The corpus becomes fixed; record the final build and preservation route |

## 27. Current-state modeling

Default character modeling uses the reconstruction-current state. A scenario that needs newer material requires a provisional current-release reading, labeled provisional and not promoted silently.

---

# VI. Reading

## 28. Unit of analysis

Do not default to equal-length essays per episode or per file. The unit is a **bounded causal block**: a coherent chapter, phase, event, or sub-arc with a recoverable entering and exiting state. Main stories are read exhaustively and interpreted in causal phases. Events are read whole unless a distinct sub-arc warrants separation. Compact ordinary-life material may share a portfolio reading of separate mini-cases.

A boundary is justified by a durable psychological or relationship transition, an epistemic revelation, a causal turning point, or a new equilibrium. Do not split a continuous crisis to equalize block size.

## 29. Reading strategy

Read the narrative spine first, in order, within the admitted horizon. Route supplemental material (events, card and bond stories, interface lines) through the relevance screen, with mandatory coverage accounting so that ordinary-life evidence is not dropped because it is unprominent. Character-first mining of popular characters is a later retrieval operation, not a sequential foundation.

## 30. Lenses

Address these as the block earns them:

1. **Narrative and causality**: what happens, what causes what, who initiates, chooses, resists, or bears consequences.
2. **Psychological state**: goals, fears, beliefs, self-concept, coping, presentation versus internal state.
3. **Relationship state**: directional; trust, dependence, rivalry, authority, repair.
4. **Epistemic state**: who knows, believes, suspects, or misunderstands what, by which route. Knowledge change is not personality change.
5. **Behavior and speech**: decisions, avoidance, repair, recipient-conditioned register.
6. **Ordinary life**: initiative, humor, tastes, practical habits, irritation, downtime.
7. **Institutions and work**: groups, roles, public persona, professional labor, incentives.
8. **Form and presentation**: framing, staging, voice, music, performance as action, where actually inspected.
9. **Continuity and revision**: state scope, counterexamples, and transitions on earlier claims.

## 31. Facts, inference, and interpretation

Keep factual reconstruction usable on its own:

| Class | Meaning |
|---|---|
| `SOURCE_FACT` | Source-established event, wording, or attributed report |
| `BOUNDED_INFERENCE` | Supported interpretation within declared evidence and state |
| `THEMATIC_INTERPRETATION` | An argument about meaning or form |
| `WORKING_HYPOTHESIS` | A live explanation awaiting discrimination from rivals |
| `OPEN` / `UNKNOWN` | Unresolved / presently unavailable; neither means false |

A reported belief is a fact about the report, not necessarily about the world. Give load-bearing events stable IDs, independent of diegetic time.

## 32. Game systems and story

Gameplay systems are not narrative facts by default. Stats, rarity, gacha tiers, skill descriptions, tutorial text, and interface copy are classified separately. A card's rarity is not a character's importance; combat numbers are not story capability unless the story frames them so. Where the game deliberately makes a mechanic diegetic, record that as a source fact with its locator.

## 33. Ordinary life and high stakes

Every serious character account needs ordinary-life evidence: crisis scenes show value priority under pressure but not daily personality. Equally, identify which values survive conflict: loyalty against self-preservation, honesty against harmony, autonomy against obligation. A favorite food does not decide every choice; one memory does not prove identical adult conduct.

## 34. End-of-block handoff

Every block closes with "what is now true that was not true before":

| Field | Content |
|---|---|
| World and situation | New constraints, opportunities, institutional changes |
| Character | State transitions and unchanged bounds |
| Relationship | A toward B and B toward A changes |
| Epistemic | Who learned or misunderstood what, by which route |
| Group | Membership, roles, leadership, public and private changes |
| Threads | Opened, advanced, closed, unresolved, with event IDs |
| State scope | Routes, variants, and contexts the block covered |
| Revisions and uncertainty | Claim transitions, rival explanations, required AV checks |
| Closeout | Exact coverage, updated ledgers, verified endpoint |

"No supported change" is a valid value. A blank field is not negative evidence.

## 35. Counterevidence and revision

Every major claim records supporting evidence, counterevidence or a falsifying condition, state and relationship scope, confidence, an alternative reading, and its extrapolation limit. A contradiction is often the most useful fact about a character; do not resolve it by deleting one side. Use `PRESERVE`, `STRENGTHEN`, `REVISE`, `DOWNGRADE`, `REJECT`, and `OPEN` for transitions.

---

# VII. Voice, presentation, and music

## 36. Channels

- Text claims rest on resolved script evidence.
- Presentation claims rest on inspected assets bound to a scene (Section 9); dialogue does not show camera, gaze, blocking, or lighting.
- Performed-voice claims rest on a correctly resolved voice asset that was actually listened to, under a lane that supports it; runtime capture is needed where delivery depends on scene timing or the mix.
- Machine acoustic measurement can find distributions and outliers across a voice corpus; it does not establish emotion or acting intent by itself.
- Music videos and live performances follow the generic continuous-AV method. Review a music video or live footage only when its staging adds evidence. Lyrics are not autobiographical testimony by every singer.
- Keep text, voice, visual, and music evidence entries separate, and account honestly for what was actually inspected. "Direct listening: none" is a valid and useful record.
- Route AV needs found during text reading into a prioritized queue tied to a scene, a state, and an exact line or cue. A new event does not automatically require its whole video; add only the AV evidence its claims need.

---

# VIII. Outputs

## 37. Block reading structure

- **A. Receipt**: witness, lock alias, packet identity, coverage.
- **B. Entering state** and state scope.
- **C. Factual reconstruction** with event IDs.
- **D. Interpretation**, with rivals.
- **E. Character, relationship, and epistemic changes.**
- **F. Ordinary-life evidence.**
- **G. Presentation, voice, and music**, as inspected.
- **H. Counterevidence and alternatives.** Mandatory.
- **I. Claim transitions.**
- **J. Handoff** (Section 34).
- **K. Ledger manifest**, with explicit "no material change".
- **L. Limitations and remaining obligations**, including AV queue.

## 38. Infrastructure games commonly need

Name these in the architecture where the game earns them:

- a source lock and witness registry, with a source-delta ledger for each lock increment;
- a coverage record and a deduplication record;
- an identity crosswalk;
- a relevance-routing ledger and a release-impact ledger (live service), with a freshness record for syntheses;
- character, relationship, and epistemic state ledgers;
- a claim-revision ledger with retest fields;
- a branch-divergence ledger (branching games): shared pre-branch state, condition, outcome, invariants, branch-only traits, and biography safety;
- an AV queue for evidence the text lane cannot inspect.

---

# IX. Blind and benchmark use

## 39. Identity minimization

Blind analysis of a game is limited: names, titles, and IDs pervade the data. Give the analyst only an admitted packet; strip file names, build metadata, and series titles from it where practical; withhold wikis, prior analyses, and later content. Record what the analyst recognized. Blind mode is procedurally prospective, not a guarantee of epistemic blindness.

## 40. Modality and extraction ablation

Useful comparisons:

- **Pass A**: script text only, from extracted data.
- **Pass B**: script with presentation assets bound to scenes.
- **Pass C**: with resolved, listened-to voice.
- **Pass D**: runtime capture of the same scenes under the continuous-AV method.

Also compare a reading from a fan transcript with one from native data for the same scenes. Record new claims, revised claims, false claims (especially from bad joins or misattributed speakers), and claims correctly left open.

---

# X. Governing rules

1. **Every claim names its build, its state scope, and its extraction route.**
2. **Native evidence grounds claims; projections only find them.**
3. **A table row is stored data, not a shown event.**
4. **An asset's existence is not its playback.**
5. **A display name is not a resolved identity.**
6. **Unreleased content is outside the horizon.**
7. **What is true on one route, variant, or context is not true on all.**
8. **A choice shows the option space, not the player.**
9. **States are append-only; later releases do not rewrite earlier truth.**
10. **Source-current is not analysis-current.**
11. **Impact is consequence, not prominence.**
12. **Game mechanics are not story facts unless the story makes them so.**
13. **Coverage is recorded; search and screening are not reading.**
14. **Count unique sources, not appearances.**
15. **Never average mutually exclusive branches.**
16. **A file name or label is not a meaning.**
17. **Contradictions are recorded, not harmonized.**
18. **Counterevidence belongs inside the analysis.**

---

# Repository context

- [Medium and inspection-lane routing policy](../source-policies/MANGA_ANIME_MEDIUM_AND_INSPECTION_LANE_ROUTING_POLICY.md): lanes and reference methods by medium.
- [Project initiation and architecture policy](../source-policies/MANGA_ANIME_PROJECT_INITIATION_AND_ARCHITECTURE_POLICY.md): Section 12.4 on games and branching narratives.
- [Analytical handoff contract](../source-policies/MANGA_ANIME_ANALYTICAL_HANDOFF_AND_INTEGRATION_CONTRACT.md): Section 4 on live-service boundaries.
- [Generic novel method](GENERIC_NOVEL_ANALYTICAL_METHOD.md): prose-reading discipline for game text.
- [Generic continuous-AV method](GENERIC_CONTINUOUS_AUDIOVISUAL_ANALYTICAL_METHOD.md): cutscenes, music videos, runtime capture, and live footage.
- [Generic character reconstruction method](GENERIC_CHARACTER_RECONSTRUCTION_METHOD.md): Section 22, game and live-service sources.
- [Generic multi-document synthesis architecture template](GENERIC_MULTI_DOCUMENT_SYNTHESIS_ARCHITECTURE_TEMPLATE.md): the paired architecture.
- [Change-integration checklist](../policies/CHANGE_INTEGRATION_CHECKLIST.md): authorized paths, validation, and publication.
