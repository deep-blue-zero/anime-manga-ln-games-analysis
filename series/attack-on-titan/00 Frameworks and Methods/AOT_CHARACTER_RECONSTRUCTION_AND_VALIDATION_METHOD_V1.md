---
series: AOT
artifact_type: character_reconstruction_validation_method
scope: V01-V34_design
status: canonical
generation: V2
version: "1.0"
date: "2026-08-23"
source_boundary: "Methodological extension; current analytical corpus V01-V18, complete manga source corpus V01-V34"
supersedes: null
superseded_by: null
do_not_use_as_current_authority: false
parent_method: AOT_ANALYTICAL_METHOD_V2.md
architecture: AOT_CHARACTER_MODELING_AND_SIMULATION_ARCHITECTURE_V1.md
---

# Attack on Titan — Character Reconstruction and Validation Method v1.0

## 1. Purpose

This method tells a later analyst how to transform the V2 deep-reading corpus into a character model and how to test that model without confusing plausibility with truth.

A character model is a **constrained reconstruction surface**. It should predict ranges and tendencies under specified conditions while preserving contradiction, development, and uncertainty.

## 2. Evidence classes

Use the following modeling evidence classes.

`DIRECT_SOURCE_FACT (DSF)` — directly observed action, line, stated preference, relationship fact, bodily fact, or role fact.

`REPEATED_BEHAVIORAL_PATTERN (RBP)` — recurs across materially distinct situations.

`RELATIONSHIP_CONDITIONED_PATTERN (RCP)` — recurs with a specific person or relationship class and should not be generalized without support.

`EMOTIONAL_OR_BODILY_STATE_DELTA (ESD)` — a bounded departure from resting behavior under a defined state.

`DEVELOPMENTAL_TRANSITION (DT)` — evidence that a repertoire, belief, or threshold changes across time.

`HIGH_CONFIDENCE_INFERENCE (HCI)` — no single source statement establishes the rule, but multiple independent evidence channels converge.

`OPEN_INFERENCE (OI)` — plausible but underdetermined.

`NEGATIVE_CONSTRAINT (NC)` — evidence against a caricature, overgeneralization, or predicted behavior.

No synthetic output receives an evidence class.

## 3. Claim-strength rubric

Assess each model claim across:

- directness;
- recurrence;
- cross-context stability;
- relationship specificity;
- temporal stability;
- counterevidence;
- source/locator quality;
- scenario-domain coverage.

Use confidence bands:

`HIGH` — repeated or directly anchored, survives counterexamples, and has clear boundary conditions.

`MODERATE` — meaningful evidence but limited recurrence, narrow relationship scope, or unresolved counterevidence.

`LOW` — weakly supported, single-scene, or distant transfer.

`OPEN` — should not currently be used as a predictive rule.

## 4. Stable baseline versus state

Never write "Character X is Y" when the evidence actually says "Character X behaves Y under state Z."

For each pattern decide whether it is:

- stable baseline;
- developmental state;
- emotional delta;
- bodily delta;
- relationship-conditioned;
- role-conditioned;
- information-conditioned;
- one-off exception;
- uncertain.

The same outward behavior may have different causes at different boundaries.

## 5. Behavioral grammar extraction

For each major scene, extract only diagnostically useful behavior.

Required questions:

1. What problem did the character perceive?
2. What did they know and not know?
3. What options were materially available?
4. What role or relationship constrained them?
5. What did they attend to first?
6. What action threshold was crossed?
7. Which alternatives did they reject or fail to consider?
8. What did they do?
9. How did they interpret the result?
10. Did later behavior preserve, revise, or contradict the pattern?

Prefer conditional rules over adjectives.

## 6. Core predictive domains

A substantial model should cover, when evidence permits:

- uncertainty and information seeking;
- threat response;
- intervention threshold;
- obedience and authority;
- command and delegation;
- failure and regret;
- anger and punitive impulse;
- fear and avoidance;
- sacrifice/self-sacrifice;
- help-seeking and help refusal;
- care giving and care receiving;
- apology/repair after harm;
- persuasion and disagreement;
- deception/secrecy;
- public versus private role;
- ordinary companionship;
- humor and teasing;
- embarrassment and social discomfort;
- boredom/rest/routine;
- value conflict and override conditions.

A model may explicitly mark a domain `INSUFFICIENT_EVIDENCE`.

## 7. Japanese voice extraction

For each character track:

- self-reference;
- addressee naming;
- politeness and honorific accommodation;
- command versus request form;
- sentence/turn length;
- lexical abstraction;
- blunt negation;
- hedging/qualification;
- rhetorical questions;
- repetition;
- ellipsis;
- apology/praise/complaint/teasing strategies;
- role vocabulary;
- emotionally altered speech;
- relationship-specific register.

Do not infer a complete voice from famous lines. Do not infer anime prosody from manga text. English translations are comparison surfaces, not voice authority.

## 8. Ordinary-life control sample

Every model should seek at least:

- one low-stakes group interaction;
- one low-stakes dyadic interaction where available;
- one disagreement not immediately governed by mortal danger;
- one routine/work/training interaction;
- one humor, embarrassment, irritation, or rest sample if canon supplies it;
- one crisis state for contrast.

If a character lacks these samples, record the gap and narrow simulation confidence accordingly.

## 9. Relationship-conditioned register matrix

For each major relation, use directed rows:

`character -> interlocutor | time boundary | public/private | role relation | trust | dominant speech acts | behavioral tendencies | exceptions | evidence IDs | confidence`

A relation should receive multiple rows when it materially changes across time or state.

## 10. Mischaracterization-trap protocol

Before promotion, identify at least three tempting but reductive caricatures for a major character.

Examples of trap classes:

- famous slogan becomes every conversation;
- protective attachment becomes total personality;
- terse command language becomes emotional emptiness;
- strategic intelligence becomes constant calm;
- trauma becomes every motive;
- ideology becomes a mechanically applied algorithm;
- later revelation erases genuine earlier attachment;
- high-stakes courage becomes social confidence;
- high-stakes ruthlessness becomes ordinary cruelty.

For each trap cite contrary or qualifying evidence.

## 11. "Would sound wrong if..." constraints

The model should include negative linguistic and behavioral constraints. These are especially useful in hypothetical scenes.

A constraint should be evidence-backed and scoped, for example:

- wrong if the character becomes much more verbose than their attested conversational range without a state reason;
- wrong if a relationship-specific tenderness is generalized to strangers;
- wrong if a crisis-state nihilism is used as resting baseline;
- wrong if a character knows facts unavailable at the selected boundary.

## 12. Construction protocol

For each character:

1. choose the source/time boundary;
2. read the readiness ledger;
3. retrieve all relevant behavioral/relationship/voice/ordinary-life entries;
4. retrieve character-specific thematic/state ledgers;
5. retrieve the strongest canonical volume artifacts;
6. escalate disputed or wording-sensitive claims to Japanese pages;
7. draft stable versus state-conditioned patterns;
8. write conditional behavior rules;
9. map relationship-conditioned variation;
10. write speech fingerprint and state deltas;
11. write negative constraints;
12. identify uncovered domains;
13. create validation predictions before consulting reserved test material;
14. run validation;
15. preserve failures and revise claims through explicit transitions.

## 13. Prospective V01-V19 prediction freeze

The current corpus design permits genuine prospective testing.

After V19 and the 50% checkpoint, but **before V20 analysis**, create `AOT_CHARACTER_MODEL_PROSPECTIVE_PREDICTION_REGISTER_V01-V19.md`.

For each sufficiently evidenced character, freeze a compact set of predictions across several classes:

- decision under uncertainty;
- response to guilt/failure;
- relationship-specific behavior;
- response to authority;
- likely speech/register behavior;
- predicted exception or failure mode;
- ordinary-life prediction only where V01-V19 evidence supports one.

Predictions should be conditional and falsifiable. Avoid trivialities such as "Eren will care about freedom."

## 14. Holdout adjudication

When later canon supplies a relevant test, use:

`PASS` — the predicted response family and boundary conditions are materially supported.

`PARTIAL` — direction is broadly right but mechanism, state condition, or register requires revision.

`FAIL` — canon materially contradicts the prediction under a genuinely comparable condition.

`NOT_TESTED` — later source has not supplied a fair test.

`CONFOUNDED` — the apparent test changes too many relevant variables to score cleanly.

Never edit the original frozen prediction after seeing the test. Record a new adjudication and, if needed, a `PRESERVE`, `STRENGTHEN`, `REVISE`, `DOWNGRADE`, `REJECT`, or `OPEN` transition.

## 15. Retrospective validation after V34

After full-series completion, prospective predictions remain the strongest evidence of earlier predictive warrant. Final models may additionally use:

- scene withholding during final drafting;
- leave-arc-out reconstruction tests;
- relationship contrast tests;
- state contrast tests;
- anti-stereotype adversarial probes;
- cross-model dialogue/interaction consistency tests.

Because the analyst will have encountered the whole manga by then, retrospective tests must not be mislabeled as fully blind holdouts.

## 16. Simulation QA

A hypothetical probe should specify:

- character boundary;
- scenario distance `D0-D3`;
- known/unknown information;
- relationship state;
- public/private context;
- stakes and time pressure;
- physical/emotional state;
- closest canonical analogues;
- unmatched features;
- predicted response family;
- confidence.

Generate at least one alternative response when uncertainty is material.

## 17. Synthetic-content firewall

Generated scenes, generated Japanese, crossover dialogue, and hypothetical reasoning are never evidence.

They must not be copied into:

- evidence ledgers;
- voice ledgers as examples of canon;
- preference ledgers;
- model validation as if observed;
- primary-source locator indexes.

If a reconstruction test exposes a weakness, return to canonical evidence.

## 18. Cross-character interaction validation

Pairwise or group simulations should be checked against both models. A scene fails QA if one character is made accurate by forcing another into an unsupported role.

Audit:

- directional relationship assumptions;
- rank and authority;
- information asymmetry;
- interruption and turn-taking tendencies;
- likely alliance/conflict points;
- who initiates repair;
- who tolerates ambiguity;
- who dominates topic or action;
- whether one character is reduced to a foil.

## 19. Model promotion gates

A model cannot become `canonical` unless it passes:

**Gate A — source grounding:** load-bearing claims route to canonical evidence.

**Gate B — temporal discipline:** no later knowledge leaks into earlier states.

**Gate C — state/trait separation:** crisis and bodily deltas are quarantined.

**Gate D — relationship specificity:** directional differences are preserved.

**Gate E — ordinary-life control:** low-stakes evidence is used or the gap is explicit.

**Gate F — Japanese voice:** idiolect is evidence-based and not translation-derived.

**Gate G — negative constraints:** caricature traps are tested.

**Gate H — validation:** prospective/retrospective test results are preserved, including failures.

**Gate I — retrieval:** a reader can move model -> ledger -> volume -> evidence ID -> source page.

**Gate J — synthetic firewall:** generated material has not contaminated evidence.

## 20. Predictive warrant language

Prefer:

- "strongly predicts";
- "makes X more likely";
- "canon repeatedly supports";
- "plausible under this relationship state";
- "weakly evidenced";
- "outside current coverage".

Avoid:

- "would definitely";
- "always";
- "never";
- "this is what the character secretly thinks";

unless the source directly warrants the categorical form.

## 21. Completion standard

A character model is complete when a competent reader can recover:

- what is stable;
- what changed and when;
- what varies by interlocutor;
- what varies by emotional/physical state;
- how the character tends to decide;
- how they tend to speak in written Japanese;
- what ordinary-life evidence exists;
- what would be a caricature;
- which scenario domains remain weak;
- how the claims were validated;
- where the underlying Japanese evidence lives.
