---
series: RE_ZERO
artifact_type: analytical_method
scope: JAPANESE_LIGHT_NOVEL_PRIMARY_PROSPECTIVE_AND_LONGITUDINAL_ANALYSIS
generation: V0.1
status: canonical
release_state: mutable_active
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
---

# Re:Zero — analytical method

## 1. Responsibility

This document governs source-facing analysis of Re:Zero once exact witnesses are admitted by the source lock. It defines how evidence becomes claims, how a long serial reading remains prospective, how repeated or branching event-states are handled, how later evidence may revise the current model without rewriting historical analytical state, and when recurring questions deserve independent artifacts.

It is not a plot summary, character profile, lore encyclopedia, adaptation verdict, or whole-series thesis. Those responsibilities are downstream and must be earned by source evidence.

## 2. Source hierarchy and semantic anchor

The intended primary semantic anchor is the **Japanese published light novel**, but this becomes operative only for exact volumes actually admitted by `REZERO_SOURCE_LOCK_AND_INVENTORY.md`.

Use this hierarchy by default:

1. locked Japanese main light novel for main-route claims;
2. locked Japanese mainline supplemental light-novel/short-story material for claims within its verified scope and insertion horizon;
3. translations as convenience/comparison witnesses, not silent semantic replacements;
4. alternate-route/IF material as separately bounded counterfactual witnesses;
5. web-novel material as a separately labeled developmental/version witness;
6. anime or other adaptations as adaptation witnesses;
7. interviews, reference books, games, promotional material, and other sources only after explicit admission and role assignment.

A lower item is not necessarily less valuable. The hierarchy identifies **which witness answers which question**. Anime performance may be the primary evidence for anime acting choices while remaining unable to establish a light-novel wording claim.

## 3. Evidence classes

Every durable claim should be recoverable to source-bearing observations. Use these working classes:

- **DIRECT** — explicitly stated or unambiguously shown by the admitted witness.
- **CORROBORATED INFERENCE** — not stated verbatim, but supported by multiple observations, states, or perspectives with weak counterevidence.
- **INTERPRETIVE HYPOTHESIS** — a plausible model that organizes evidence but remains materially contestable.
- **OPEN / UNRESOLVED** — evidence is insufficient, contradictory, route-bound, viewpoint-bound, or dependent on unread/unadmitted material.

Direct evidence that a character believes something is not automatically direct evidence that the belief is true. Repetition across event-states can strengthen a behavioral inference, but only when the relevant conditions are comparable.

## 4. Prospective freeze and anti-hindsight rule

The numbered main light novels use a prospective freeze.

For each locked `VNN`:

1. begin from the frozen state after `VNN-1`;
2. record important expectations, rival hypotheses, unresolved questions, and confidence before reading `VNN`;
3. read `VNN` as the new source increment;
4. classify changes to earlier claims;
5. write the deep reading;
6. freeze the bounded state before advancing.

Later knowledge may revise the **current** model. It may not silently rewrite what an earlier reader reasonably knew. Preserve wrong predictions when they were reasonable, and state why later evidence changed them.

This rule applies equally to lore, character motives, faction models, relationship expectations, ability/mechanics theories, and thematic hypotheses.

## 5. Revision vocabulary

When later evidence tests a prior claim, use:

- **PRESERVE** — materially unchanged;
- **STRENGTHEN** — same claim, stronger evidence or broader support;
- **REVISE** — core model survives but wording, scope, mechanism, or causal account changes;
- **DOWNGRADE** — claim remains possible but confidence or scope falls;
- **REJECT** — evidence materially contradicts the claim;
- **OPEN** — adjudication remains insufficient.

Do not convert every new detail into a revision. A claim changes only when its meaning, confidence, scope, or causal account changes.

## 6. Global volume identity and arc identity

Preserve global volume numbering in repository filenames. When the admitted sources establish an arc structure, record arc identity as metadata rather than restarting filenames inside each arc.

A deep reading should therefore be addressable by stable global volume identity while retaining the work's own macrostructure.

Create an arc checkpoint only after the boundary is source-verified and its final contributing main volume is frozen. A checkpoint summarizes the reached state; it never replaces the underlying volume freezes.

## 7. Focalization and epistemic discipline

For every material claim ask:

- Who perceives, remembers, narrates, asserts, or infers this?
- What does that person know in this exact event-state?
- What relevant facts does the reader know that the focalizer does not?
- Is the speaker positioned to know?
- Is the account distorted by fear, hope, shame, loyalty, status, ideology, trauma, self-interest, incomplete memory, deception, or ordinary ignorance?
- Does another independent viewpoint or event-state corroborate it?

Do not flatten multiple viewpoints into an omniscient composite voice.

## 8. Repeated and branching event-state discipline

Whenever the source presents materially repeated, reset, superseded, branching, failed, or counterfactual sequences, identify the **event-state** before drawing longitudinal conclusions.

Keep separate:

- event-state-local facts;
- current active-world facts;
- retained character knowledge, if any;
- non-retained character knowledge;
- reader-only knowledge;
- causal changes introduced by earlier information;
- behaviors that recur under comparable conditions;
- behaviors that differ because conditions changed.

An event can be narratively and psychologically consequential without remaining an active-world historical fact. A behavior can be directly observed in a superseded state without proving that the same behavior would occur in a later state whose information, trust, incentives, or stressors differ.

## 9. Failed-state evidence transfer rule

Evidence from a failed or superseded event-state may transfer into a broader character model only after asking:

1. Was the relevant character in a comparable internal state?
2. Did they possess comparable information?
3. Were the relationship and power conditions comparable?
4. Did the triggering circumstances materially differ?
5. Does the behavior recur elsewhere?
6. Is the inference about a stable tendency, a conditional tendency, or merely one observed possibility?

Prefer conditional formulations when transfer is uncertain: `under condition X, character Y did Z`, not `character Y always does Z`.

## 10. Information asymmetry and knowledge provenance

Track important knowledge by **holder, source, confidence, and event-state**.

Distinguish:

- personally witnessed knowledge;
- remembered prior-state knowledge;
- testimony received from another character;
- inference;
- rumor or institutional doctrine;
- deliberate deception;
- hidden information known to the reader but not the focal character;
- information lost or no longer mutually shared across states.

This is essential for interpreting trust, apparent irrationality, persuasion, consent, secrecy, accusation, alliance, and conflict.

Do not judge a character's decision against information they did not possess.

## 11. Relationship continuity under asymmetric experience

Relationship analysis must be dyadic and state-aware.

Track:

- what each participant remembers of the relationship;
- current trust and disclosure;
- affection, duty, fear, dependency, obligation, rivalry, patronage, coercion, or alliance;
- information asymmetry;
- recipient-conditioned behavior;
- changes in address, register, intimacy, and practical reliance;
- whether one party's sense of continuity exceeds the other's.

Do not describe a relationship as mutually developed merely because one participant carries cumulative experience.

## 12. Character continuity, stress, and genuine development

Distinguish:

- **stable tendency** — recurs across materially different states or recipients;
- **developmental state** — characteristic of a bounded period;
- **information effect** — changed because the character knows more or less;
- **relationship effect** — recipient-specific;
- **role/status effect** — produced by office, faction, class, duty, or public position;
- **situational/stress effect** — crisis, injury, exhaustion, grief, fear, shame, urgency, public performance, etc.;
- **genuine revision** — earlier character model no longer predicts later behavior adequately.

Do not medicalize ordinary distress or infer diagnoses from narrative behavior. When trauma or psychological strain is analytically relevant, describe source-supported phenomena first: intrusive memory, avoidance, panic, dissociation-like presentation, self-blame, impaired judgment, altered risk tolerance, emotional numbing, dependency, or other observable patterns only when the text supports them.

## 13. Agency and constrained choice

Reconstruct the actual choice set before making ethical or political judgments.

Track:

- information available;
- time pressure;
- physical capacity;
- status and legal position;
- threats and coercion;
- social obligations;
- material resources;
- dependence on allies;
- credible alternatives;
- expected costs of refusal;
- whether prior-state knowledge changes the apparent option set.

Nominal ability to choose is not the same as practical autonomy.

## 14. Institutions, factions, status, and power

Separate:

- stated rules;
- customary practice;
- enforcement capacity;
- faction incentives;
- patronage and personal discretion;
- class/status barriers;
- coercive leverage;
- material and military capacity;
- information networks;
- exceptions and informal workarounds.

Do not infer a faction's unified intention from one member's account. Do not mistake legal authority for actual capacity or actual capacity for legitimacy.

## 15. Mechanics, abilities, and world-model inference

For supernatural, technical, historical, religious, or political mechanisms, classify evidence as:

- character belief/explanation;
- institutional doctrine;
- observed regularity;
- demonstrated cost;
- demonstrated exception;
- independent corroboration;
- reader-only pattern;
- unresolved contradiction.

Operational reliability does not prove the characters' theory of why a mechanism works. A later explanation may revise the current world model without retroactively making earlier characters knowledgeable.

## 16. Japanese-language audit

Japanese is the semantic anchor for admitted light-novel claims. Return to exact Japanese when interpretation depends on:

- first/second-person choice or omitted subject;
- honorifics and forms of address;
- titles, ranks, factional or institutional terminology;
- politeness/register shifts;
- insults, threats, affection, self-deprecation, or performative bravado;
- recurring slogans or emotionally charged lexical choices;
- modal or evidential ambiguity;
- who is grammatically or pragmatically presented as agent;
- terms with inconsistent or lossy English renderings.

A translation disagreement should be documented as a witness issue, not silently resolved by preference.

## 17. Ordinary life as character evidence

Record mundane evidence when it changes the model: food, clothing, hygiene, comfort, study, work rhythm, shopping, gifts, leisure, humor, games, etiquette, domestic routines, habits, taste, annoyance, avoidance, sleep, recovery, and treatment of people in low-stakes interactions.

Ordinary-life evidence is useful because crisis behavior alone can overfit a character to extreme conditions. Do not accumulate trivia without analytical responsibility.

## 18. Supplemental and alternate material

Follow `REZERO_ROUTE_AND_WITNESS_PROTOCOL.md` before integrating any non-spine witness.

A mainline supplement may update the main-route model only within its verified temporal/route scope and only after the prospective horizon permits reading it.

An IF/alternate-route witness can support statements about that route and carefully bounded counterfactual claims. It cannot silently add events, relationships, motives, or developmental history to the main route.

A web-novel witness is not a draft footnote to be mined for light-novel facts. Treat version differences as evidence about textual development only when the comparison itself is the analytical task.

## 19. Adaptation discipline

Anime analysis is a separate witness layer. Track:

- scene retention, omission, compression, expansion, and reordering;
- focalization changes;
- acting and vocal delivery;
- music, silence, sound design, timing, editing, framing, color, blocking, and visual symbolism;
- changes in ambiguity or information disclosure;
- whether adaptation choices materially alter character, relationship, mechanics, or thematic interpretation.

Never attribute anime-only audiovisual evidence to the light novel.

## 20. Minimum main-volume deep-reading responsibilities

Each numbered deep reading should cover, as evidence warrants:

- exact witness identity and global volume identity;
- arc metadata if source-verified;
- pre-reading analytical horizon and open questions;
- event/scene structure and focalization;
- route/event-state distinctions;
- information-state changes;
- character-state changes and contradictions;
- relationship/network changes;
- institutions, factions, status, and constrained agency;
- mechanics/world-model changes;
- ordinary-life evidence;
- distinctive Japanese wording when interpretation depends on it;
- direct facts versus inference;
- counterevidence and rival readings;
- revision status of prior claims;
- bounded expectations/open questions for the next unread main volume.

## 21. Promotion thresholds for canonical artifacts

Create a new canonical artifact only when it owns a recurring retrieval/revision responsibility that existing files no longer serve reliably.

Examples:

- a route/event-state ledger after repeated sequences become costly to reconstruct across volume files;
- an information-asymmetry ledger after knowledge provenance repeatedly drives interpretation;
- a character monograph after enough longitudinal evidence exists to distinguish stable and conditional behavior;
- a faction/institution or mechanics synthesis after the question spans enough volumes to require its own maintained state;
- an adaptation synthesis only after the relevant audiovisual corpus is actually reviewed;
- an arc or full-series synthesis only after its source boundary is covered.

Do not create placeholder monographs or empty ledgers merely to advertise future scope.

## 22. Comparative and ethical frameworks

PACTRIH, cross-series simulation, shipping analysis, genre comparison, moral evaluation, and other higher-order frameworks are downstream.

Before applying them:

- reconstruct the relevant Re:Zero source state first;
- separate description from normative judgment;
- preserve route and temporal dependence;
- include counterevidence;
- do not use protagonist/antagonist status, popularity, suffering, narrative reward, or fandom reputation as moral evidence.

## 23. Falsification rule

For any recurring thesis, be able to name:

- supporting evidence;
- counterevidence;
- alternate causal explanations;
- route/state conditions under which the claim may fail;
- missing source evidence;
- unread or unadmitted witnesses that could change the result.

Precision about uncertainty is preferable to premature closure.

## 24. Bootstrap prohibition

This method establishes how Re:Zero will be analyzed. It does not establish substantive conclusions about any character, faction, mechanism, relationship, or theme.

The first canonical interpretive artifact should be the first source-locked main light-novel deep reading, not a retrospective whole-series model assembled from remembered canon.
