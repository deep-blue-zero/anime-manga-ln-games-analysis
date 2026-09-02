---
series: HIBIKE
artifact_type: character_modeling_method
scope: FULL_V2
media: Japanese light novels
generation: V2
status: active_provisional
source_boundary: V2 locked Japanese prose corpus; exact lock pending Phase 0
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
---

# Sound! Euphonium V2 — Character Modeling Method

## 1. Objective

This document governs the V2 character-modeling layer.

The target is not a conventional character essay and not a roleplay prompt. The target is an **evidence-constrained generative character model** strong enough to answer questions such as:

- How would this character probably interpret a novel situation?
- What would she notice first?
- What would she think but not say?
- What register would she use with this specific person?
- What kinds of pressure change her normal behavior?
- How does her behavior differ at different points in the series?
- What actions or phrasings would be out of character without extraordinary explanation?

A high-quality model should make plausible predictions **outside the exact scenes observed in canon** while clearly labeling those predictions as inference rather than canon.

The governing unit is:

> **character state × relationship state × situation → probabilistic behavior and language**

This prevents three common failures:

1. treating personality as a bag of adjectives;
2. treating a character's mature endpoint as though it existed from Volume 1;
3. making the character speak identically to every addressee.

---

## 2. V1 baseline and why a new layer is needed

V1 already contains many good compressed insights. Examples include:

- Kumiko's spoken language is more cautious than her sharper internal narration;
- Reina uses compact declaratives and `アタシ / アンタ`, with Kansai features intensifying under emotion;
- Asuka controls register theatrically through brightness, repetition, coldness, and comic deflection;
- Kanade's polished honorific language can operate as both courtesy and pressure;
- Mayu's controlled standard Japanese fits a socially adaptive, geographically mobile character;
- Mizore's sparse literal speech gives unusual weight to extended statements;
- Nozomi's bright social fluency can both include people and prevent emotional gravity from settling.

V1 also recognizes that personality does not become purified by growth. That is essential for modeling: later Reina is still Reina; later Kanade remains calculating; later Asuka remains theatrical; later Kumiko becomes more capable of strategic social influence rather than simply more "honest."

V2 must convert these compact observations into evidence-rich predictive structures.

---

## 3. Modeling principles

### 3.1 Model mechanisms, not adjectives

Weak:

> Reina is ambitious, blunt, intense, loyal, and talented.

Stronger:

> When musical excellence conflicts with social comfort, Reina normally privileges excellence and may regard softened standards as disrespectful. With people she has personally selected, care may alter the emotional aftermath but usually does not cause her to falsify the musical judgment.

The second formulation predicts behavior because it contains:

- trigger;
- priority;
- default action;
- relational modifier;
- constraint.

### 3.2 Preserve competing drives

Characters should not be compressed into one motive.

Record simultaneously:

- what the character wants;
- what she fears;
- what she believes she ought to want;
- what she wants others to believe about her;
- what she avoids admitting;
- what she is willing to sacrifice;
- what she is unwilling to sacrifice.

### 3.3 Distinguish behavior from self-explanation

A character's stated reason is evidence, not automatic diagnosis.

For each major pattern, compare:

- self-description;
- observed behavior;
- other characters' interpretations;
- later retrospective evidence;
- analyst inference.

### 3.4 State-addressable modeling

Never use one timeless character profile when the series depicts substantial development.

Recommended state notation:

- `KUMIKO@V01`
- `KUMIKO@V03`
- `KUMIKO@V06`
- `KUMIKO@V09`
- `KUMIKO@V10_POST`

State boundaries need not be identical for every character. Create a new state when there is a meaningful change in:

- knowledge;
- role;
- relationship;
- self-concept;
- decision policy;
- speech behavior;
- stress response.

### 3.5 Relationship-conditioned modeling

Character identity is relationally expressed.

A model must know that:

`KUMIKO ↔ REINA` is not `KUMIKO ↔ KANADE`,

and that:

`ASUKA ↔ KUMIKO` is not `ASUKA ↔ KAORI`.

Dyadic conditioning is mandatory for major characters.

### 3.6 Negative constraints are first-class evidence

Record what a character is **unlikely** to do.

Examples of the form, not canonical conclusions:

- unlikely to disclose vulnerability before first reframing it as a joke;
- unlikely to accept a pity concession when direct competition remains possible;
- unlikely to challenge authority publicly unless a threshold is crossed;
- unlikely to use intimate address with an unfamiliar junior;
- unlikely to offer therapeutic reassurance in the register of a highly verbally nurturing character.

Negative constraints reduce generic "good-person" drift in simulations.

---

## 4. Character evidence record

Every meaningful character observation should be representable as a record with fields such as:

- `character`
- `state`
- `volume`
- `chapter/story`
- `source_locator`
- `scene_context`
- `addressee_or_group`
- `public_or_private`
- `stress_level`
- `behavior`
- `exact_language_cue`
- `nonverbal_cue`
- `stated_motive`
- `inferred_motive`
- `confidence`
- `contradicts_prior_model`
- `relationship_delta`
- `notes`

Not every entry requires every field. The schema exists to keep later synthesis auditable.

---

## 5. Core psychological model

Each simulation-grade monograph should reconstruct the following.

### 5.1 Primary wants

Separate:

- immediate wants;
- recurring wants;
- identity-level wants;
- socially acceptable wants;
- privately embarrassing wants.

### 5.2 Threat model

What does the character experience as dangerous?

Possible categories include:

- rejection;
- humiliation;
- being unnecessary;
- being controlled;
- losing status;
- being pitied;
- disappointing someone;
- being ordinary;
- being visible;
- being abandoned;
- being replaceable;
- being morally misread.

Use only source-supported categories for a given character.

### 5.3 Identity claims

What descriptions of herself does the character defend?

Track where behavior supports or destabilizes them.

### 5.4 Attention model

What does this person notice disproportionately?

Examples might include:

- talent;
- social atmosphere;
- physical detail;
- hierarchy;
- fairness;
- cuteness;
- awkwardness;
- technical error;
- other people's emotional discomfort.

Attention is highly predictive because two characters in the same room do not inhabit the same informational world.

### 5.5 Default social strategy

How does the character normally preserve social safety?

Possible strategies:

- hedging;
- joking;
- confrontation;
- competence;
- caretaking;
- silence;
- charm;
- deference;
- aggressive honesty;
- plausible innocence;
- withdrawal;
- overperformance.

### 5.6 Conflict policy

Record behavior when:

- challenged directly;
- accused unfairly;
- accused correctly;
- competing for scarce status;
- protecting someone;
- protecting herself;
- facing authority;
- facing a friend;
- facing a person she admires.

### 5.7 Repair policy

How does she repair damage?

- explicit apology;
- action rather than words;
- joke/reset;
- gift;
- physical presence;
- delayed message;
- denial followed by changed behavior;
- third-party mediation.

### 5.8 Care language

How does she show affection or concern?

Do not assume verbal tenderness. Care may appear as:

- practical help;
- musical attention;
- teasing;
- defense;
- invitation;
- memory;
- giving space;
- refusing a sacrifice;
- correcting someone seriously.

### 5.9 Moral and interpretive heuristics

What rough rules does the character seem to use when deciding what is fair, kind, deserved, or necessary?

These may change by state.

### 5.10 Self-deception and blind spots

Record recurring ways the character misreads:

- herself;
- other people;
- the institution;
- causality;
- her own power over others.

---

## 6. Voice model

Clean Japanese EPUBs are especially important here because particles, punctuation, small kana, orthography, ruby, and quotation boundaries matter.

Each full model should include the following linguistic dimensions.

### 6.1 Person reference

- first-person pronoun/self-reference;
- second-person pronouns;
- surname/given-name use;
- honorifics;
- nicknames;
- zero-pronoun preference where notable;
- changes by addressee or emotional state.

### 6.2 Register

- casual/polite baseline;
- politeness switching;
- senpai/kouhai behavior;
- teacher/adult behavior;
- public leadership voice;
- intimate/private voice;
- strategic politeness.

### 6.3 Regionality

Track Kansai/regional features carefully and comparatively:

- lexical choices;
- endings;
- contractions;
- phonological representation where written;
- emotional intensification;
- standard-Japanese switching;
- whether regionality differs by addressee.

Do not turn a few dialect tokens into a caricature.

### 6.4 Syntax and turn shape

Qualitatively track:

- short declaratives versus long explanatory turns;
- questions;
- fragments;
- ellipsis;
- repeated starts;
- self-correction;
- repetition;
- rhetorical questions;
- commands;
- softened requests.

### 6.5 Sentence-final behavior

Track recurrent endings and particles where materially characteristic.

The purpose is not mechanical frequency counting alone. Ask what the ending does socially:

- asserts;
- seeks alignment;
- softens;
- provokes;
- performs innocence;
- withholds commitment.

### 6.6 Lexical and rhetorical habits

Track:

- favorite evaluative vocabulary;
- metaphors;
- intensifiers;
- insults;
- praise language;
- musical vocabulary;
- academic vocabulary;
- romantic euphemism;
- comic exaggeration;
- repeated phrases.

### 6.7 Paralinguistic writing cues

Capture:

- pauses;
- sighs;
- laughter;
- breath;
- written hesitation;
- volume markers;
- stammering;
- abrupt interruption;
- elongated sounds where represented.

### 6.8 Thought–speech gap

For focalized characters, explicitly compare:

- what is thought;
- what is said;
- what is omitted;
- how the spoken version edits the internal one.

This is mandatory for Kumiko.

### 6.9 Emotional-state variants

A voice model should include at least:

- baseline;
- excited;
- embarrassed;
- angry;
- hurt;
- competitive;
- authoritative;
- intimate;
- exhausted/defeated,

but only where enough evidence exists.

---

## 7. Behavioral and embodied model

Dialogue alone is insufficient for novel-scenario simulation.

Track:

- posture;
- eye contact;
- physical distance;
- touch initiation/acceptance;
- fidgeting;
- instrument handling;
- food behavior;
- walking/commuting habits;
- phone/message behavior;
- clothing/self-presentation awareness;
- physical reactions to embarrassment or anger;
- where the character places herself in a room/group;
- whether she moves toward, away from, or around conflict.

Also distinguish:

- ordinary behavior;
- performance/rehearsal behavior;
- crisis behavior.

---

## 8. Relationship model

For each major dyad, maintain a compact state model containing:

- relationship label used by each person, if any;
- history known to each side;
- attachment intensity;
- trust domains;
- authority/power asymmetry;
- dependency;
- admiration;
- jealousy/exclusivity;
- obligations perceived by each side;
- forms of address;
- permitted humor;
- usual conflict channel;
- disclosure boundary;
- repair channel;
- physical proximity norms;
- topics that reliably destabilize the interaction;
- what each side systematically misreads about the other.

The relationship ledger should permit asymmetric values. Do not force reciprocity.

---

## 9. Temporal model and knowledge boundaries

A simulation must specify **when** the character is being simulated.

Each state should include:

- current school year/role;
- current institutional responsibilities;
- relationship status;
- major events already experienced;
- facts the character knows;
- facts the reader knows but the character does not;
- unresolved wounds active at that time;
- capabilities not yet developed.

A later monograph may summarize the complete arc, but scenario generation must not backport mature insight.

---

## 10. Simulation-grade monograph format

Recommended artifact name:

`HIBIKE_CHAR_<NAME>_MONOGRAPH.md`

Example:

`HIBIKE_CHAR_KUMIKO_MONOGRAPH.md`

Each full monograph should contain:

1. authority/source metadata
2. simulation scope and state boundaries
3. compact identity thesis
4. stable traits versus developmental traits
5. wants, fears, shame, and identity claims
6. attention/perception model
7. decision policies
8. conflict and repair policies
9. care/attachment behavior
10. moral/interpretive heuristics
11. self-deception and blind spots
12. Japanese voice model
13. relationship-conditioned voice table
14. ordinary-life behavior and humor
15. embodied/nonverbal behavior
16. musical behavior and listening style
17. authority and institutional behavior
18. state-by-state longitudinal model
19. relationship matrix
20. negative constraints / out-of-character warnings
21. uncertainty and conflicting evidence
22. evidence matrix and locators
23. scenario-simulation guidance
24. validation results

---

## 11. Modeling tiers

Not every character warrants equal granularity.

### Tier A — full simulation-grade monographs

Initial candidates, subject to evidence audit:

- Oumae Kumiko
- Kousaka Reina
- Tanaka Asuka
- Tsukamoto Shuuichi
- Kuroe Mayu
- Hisaishi Kanade
- Yoroizuka Mizore
- Kasaki Nozomi
- Yoshikawa Yuuko
- Nakagawa Natsuki
- Katou Hazuki
- Kawashima Midori
- Taki Noboru

Tier A requires enough evidence across multiple contexts to distinguish ordinary, stressed, intimate, competitive, and institutional behavior where applicable.

### Tier B — strong character descriptions with partial simulation capacity

Likely candidates include Haruka, Kaori, Aoi, Motomu, Sally, Mirei, Satsuki, Suzume, Tsubame, Ririka, Tomoe, and other recurring figures with meaningful but narrower evidence.

### Tier C — bounded reference profiles

For characters with insufficient evidence, produce a precise limited profile rather than inventing missing psychology.

---

## 12. Evidence-density and confidence labels

Use qualitative confidence rather than false psychometric precision.

### High confidence

Pattern appears across multiple independent scenes and contexts, preferably across more than one volume/state, with little contradictory evidence.

### Moderate confidence

Pattern is repeated but context-limited, or supported strongly in one relationship but not generalized.

### Low confidence / provisional

Plausible from limited evidence, heavily dependent on one scene, one narrator's interpretation, or extrapolation.

Simulation output should inherit the confidence of the underlying rule.

---

## 13. Out-of-sample validation

A monograph is not complete when it merely summarizes canon. It must be stress-tested.

### 13.1 Novel-scenario tests

Create situations not directly present in the novels but compatible with their world.

For each scenario, predict:

- first noticed feature;
- private interpretation;
- immediate emotional response;
- outward response;
- likely exact register/style;
- what remains unsaid;
- decision;
- later reconsideration;
- relationship-specific modifier;
- confidence.

### 13.2 Counterfactual perturbation

Change one variable:

- addressee;
- public/private setting;
- authority role;
- competitive stake;
- time/state;
- whether another person is watching.

The response should change in ways consistent with the model.

### 13.3 Voice falsification

Generate several candidate lines, including deliberately generic or subtly wrong ones, and test whether the model can explain why they are wrong.

### 13.4 Behavior falsification

Ask what conditions would be required for a normally out-of-character action to become plausible.

A strong model should not simply say "she would never do that." It should identify the threshold that would have to change.

### 13.5 Canon backtesting

Where useful, hide a later canonical scene from the model-building evidence, predict behavior from earlier state evidence, then compare the prediction with the actual later scene.

This is one of the strongest available tests of whether the model captures mechanism rather than hindsight summary.

---

## 14. Simulation output standard

When using a completed monograph to simulate a novel scenario, distinguish:

### Canonical facts
Established by the source.

### High-confidence character inference
Strongly predicted by the model but not canonically observed in that exact situation.

### Plausible alternative
A second path consistent with meaningful ambiguity.

### Speculative embellishment
Creative detail not strongly inferable from source evidence.

Never present a generated scene as lost canon.

---

## 15. Anti-patterns

Do not:

- turn characters into trope labels;
- use anime-only mannerisms in a novel-primary model without labeling them;
- give every caring character therapy-speak;
- make quiet characters uniformly laconic in every context;
- make blunt characters incapable of strategic restraint;
- make intelligent characters omniscient;
- make later maturity available to earlier states;
- treat romantic/yuri coding as permission to invent explicit relationship states;
- infer dialect by stereotype when the locked text can be checked;
- extrapolate one crisis reaction into everyday baseline behavior;
- smooth contradictions merely to improve model neatness.

---

## 16. Character-model dependency graph

Character monographs should be downstream of:

1. locked Japanese sources;
2. sequential readings;
3. character-state ledger;
4. voice/register ledger;
5. relationship-state ledger;
6. behavior/gesture ledger;
7. relevant checkpoints.

A monograph may be drafted before the full series is finished only if marked `active_provisional`. Final simulation-grade authority should wait until the relevant source boundary is complete.

---

## 17. Immediate implementation rule

During every V2 volume reading, extract character-model evidence **prospectively**.

Do not plan to reconstruct voice and behavior retrospectively from literary summaries after Volume 10. The entire point of this method is to prevent loss of the mundane, linguistic, relational, and embodied details that conventional synthesis tends to compress away.
