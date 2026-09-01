---
series: LYCORIS_RECOIL
artifact_type: analytical_method
scope: "V2 character behavioral reconstruction, state modeling, validation, and simulation constraints"
generation: V2
status: canonical
source_boundary: "Anime-native reconstruction first; later integrated reconstruction follows multi-source promotion rules"
supersedes: null
superseded_by: null
do_not_use_as_current_authority: false
architecture: LYCORIS_RECOIL_V2_SYNTHESIS_ARCHITECTURE.md
governing_method: LYCORIS_RECOIL_V2_ANALYTICAL_METHOD.md
integration_method: LYCORIS_RECOIL_MULTI_SOURCE_AUTHORITY_AND_INTEGRATION_METHOD.md
---

# Lycoris Recoil Character Reconstruction Method

## 1. Purpose

This method governs the conversion of source evidence into auditable character models capable of constrained behavioral reconstruction.

A literary monograph asks:

> **Who is this character and what does the work do with them?**

A behavioral reconstruction asks:

> **Given a particular state, stimulus, relationship, stakes, and setting, what is this character likely to perceive, want, say, do, and revise—and how certain are we?**

The reconstruction system must remain downstream of source interpretation.

It must never turn generated behavior into evidence about the character.

---

# 2. Governing pipeline

Use the following direction of inference:

> **source evidence → atomic observations → state/context tagging → repeated patterns → conditional policies → relationship modifiers → state transitions → coverage/confidence → validation → reconstruction**

Do not jump directly from:

> “Takina is literal”

to:

> “Takina would misunderstand this hypothetical statement.”

The model must explain **under what conditions**, **with whom**, **at what developmental state**, and **with what competing cues** the behavior is likely.

---

# 3. Character identifiers

Use stable short identifiers where useful:

- `CHI` — Nishikigi Chisato
- `TAK` — Inoue Takina
- `FUK` — Harukawa Fuki
- `KUR` — Kurumi
- `MIK` — Mika
- `MIZ` — Nakahara Mizuki
- `KUS` — Kusunoki
- `SAK` — Otome Sakura
- `MAJ` — Majima
- `YOS` — Shinji Yoshimatsu

Additional identifiers may be added as evidence warrants.

Observation IDs should remain unique and sortable, e.g.:

`CHI-MB-E04-017`

Relationship observations may use:

`REL-CHI-TAK-E04-009`

Policy IDs should be semantic and stable after promotion, e.g.:

`CHI-SOC-INIT-01`

---

# 4. Atomic observation standard

An atomic observation records one diagnostically useful behavioral event or non-event without overgeneralizing it.

Recommended fields:

```text
Observation ID
Source / scope
Timestamp / locator
Character
Interlocutor(s)
Setting / role
Relationship state
Stakes
Character affect/state
Trigger / stimulus
Initiator
Observed appraisal or strong inference
Immediate objective
Action/tactic
Speech act
Textual register
Performance register
Physical/body behavior
Partner response
Character recalibration
Outcome
Candidate policy/trait
Negative evidence if applicable
Epistemic state
Source class
Confidence
```

Do not force every field when the source cannot support it.

---

# 5. Context/state dimensions

Character behavior should be tagged across enough dimensions to distinguish apparently contradictory responses.

## Familiarity

- `STRANGER`
- `CUSTOMER`
- `ACQUAINTANCE`
- `COWORKER`
- `FRIEND`
- `INTIMATE`
- `AUTHORITY`
- `RIVAL`
- `ENEMY`
- `VULNERABLE_OTHER`

Named relationships override coarse categories when needed.

## Stakes

- `TRIVIAL`
- `LOW`
- `MODERATE`
- `HIGH`
- `EXISTENTIAL`

## Affect/state

Examples:

- baseline;
- excited;
- bored;
- irritated;
- embarrassed;
- frightened;
- grieving;
- protective;
- angry;
- physically compromised;
- mission-focused;
- socially playful.

Do not create a fixed taxonomy so large that tagging becomes performative rather than useful.

## Interaction function

Examples:

- greeting;
- information exchange;
- request;
- refusal;
- teasing;
- reassurance;
- persuasion;
- conflict;
- repair;
- teaching;
- service;
- affection;
- boundary test;
- task coordination;
- competition.

## Power/role

Track where material:

- lower-status;
- peer;
- higher-status;
- role-authority;
- non-hierarchical;
- operational command.

---

# 6. Stable traits, strategies, and constraints

Do not collapse different causal layers.

A mature model should distinguish:

## Temperament

Relatively stable baseline tendencies.

## Values / moral constraints

Rules about what the character regards as acceptable or owed.

## Social strategies

How the character attempts to influence interpersonal situations.

## Defensive strategies

How the character manages shame, fear, grief, vulnerability, or loss of control.

## Competence effects

Behavior produced because the character can reliably do something others cannot.

## Relationship modifiers

Behavior available only or especially with particular people.

## Developmental state

Capabilities or permissions that change over the sequence.

A single surface behavior may arise from several layers.

---

# 7. Conditional behavioral policies

A promoted policy should answer:

> **When condition X obtains, what does this character usually attempt, through what means, with what modifiers and failure behavior?**

Recommended policy schema:

```text
Policy ID:
Name:
Current authority:
Source boundary:
Condition:
Likely appraisal:
Immediate objective:
Baseline response:
Preferred tactics:
Speech/register profile:
Embodied behavior:
Relationship modifiers:
State/stakes modifiers:
Escalation behavior:
Failure/repair behavior:
Known exceptions:
Negative constraints:
Supporting observation IDs:
Counterevidence:
Coverage gaps:
Confidence:
```

A policy is more useful than a trait label because it can fail conditionally.

---

# 8. Promotion threshold for policies

Use three states before mature promotion:

## `OBSERVED`

A behavior occurred.

## `CANDIDATE_POLICY`

The behavior appears reusable, repeated, or unusually diagnostic, but conditions are not fully constrained.

## `PROMOTED_POLICY`

Multiple observations or strong converging evidence establish a conditional rule with known scope.

Do not promote a policy solely because it matches the analyst's intuitive picture of the character.

A single observation may justify a candidate when it is especially diagnostic, but should normally not establish a base rate.

---

# 9. State-transition modeling

Some characters are better modeled by transition paths than by static traits.

Represent transitions as:

> **state A + stimulus + relationship → state B → probable response**

For example, a future Takina model might eventually distinguish pathways such as:

- professional containment → irritation → explicit confrontation;
- practical engagement → playful opportunity → literal participation → competitive investment;
- concern for Chisato → information seeking → pressure → loss of procedural composure.

These examples are hypotheses inherited from prior work and must be independently rebuilt by V2 evidence before promotion.

Track:

- transition trigger;
- latency if observable;
- intermediate state;
- recovery/repair;
- whether transition differs by interlocutor.

---

# 10. Relationship modifiers

A character model is incomplete without named relationship conditioning.

For major relationships, track:

- baseline distance;
- initiative balance;
- tolerated teasing;
- permitted physical proximity;
- forms of care;
- authority/yielding patterns;
- vulnerability topics;
- conflict style;
- repair style;
- reading/misreading tendencies;
- address/register;
- future orientation;
- longitudinal development.

The same stimulus may produce different behavior with:

- stranger;
- customer;
- Mika;
- Takina;
- Fuki;
- Yoshimatsu;
- Majima.

Do not infer a global disposition from one privileged relationship.

---

# 11. Voice model: text versus performance

For anime-native reconstruction, maintain two related generators.

## Textual/linguistic layer

Track:

- sentence completeness;
- politeness;
- pronouns;
- address terms;
- fillers;
- contractions;
- endings;
- imperatives;
- rhetorical questions;
- teasing structures;
- semantic reframing;
- characteristic vocabulary.

## Performance layer

Track:

- tempo;
- pitch movement;
- loudness;
- vowel length;
- breath;
- laughter;
- pause;
- overlap;
- clippedness;
- state-conditioned elasticity.

A convincing reconstruction asks both:

> What would Chisato say?

and:

> How would anime Chisato likely deliver it in this state?

Textual dialogue alone cannot reproduce performed characterization.

---

# 12. Humor, play, and repair

Humor requires explicit behavioral modeling because it is highly conditional.

Track mechanisms such as:

- imitation;
- mock aggression;
- exaggerated politeness;
- register mismatch;
- wordplay;
- physical comedy;
- absurd framing;
- deadpan;
- literal misunderstanding;
- competitiveness;
- embarrassment;
- prank;
- shared reference;
- escalation;
- failed joke;
- repair.

Ask:

- who may tease whom;
- who initiates;
- what happens when the joke fails;
- when the character stops joking;
- whether humor is affective play, social testing, avoidance, or repair.

Do not assume every Chisato joke is consciously therapeutic.

---

# 13. Preferences and affordances

Maintain only source-supported preferences.

Useful domains include:

- food;
- clothing;
- media;
- travel;
- money;
- sleep;
- cooking;
- household labor;
- work;
- technology;
- competition;
- novelty;
- risk;
- modesty;
- status;
- fandom.

Use states such as:

- `DEMONSTRATED`
- `STRONGLY_INFERRED`
- `UNKNOWN`

Do not fill an `UNKNOWN` cell with genre convention or fan assumption.

---

# 14. Meaningful negative evidence

Negative evidence can constrain reconstruction when:

1. the character had a real opportunity to act;
2. the action would plausibly be expected under a proposed rule;
3. the source makes the non-action observable.

Examples:

- does not retaliate;
- does not tease;
- does not disclose;
- does not correct;
- lets the other person lead;
- accepts a boundary;
- ignores status;
- declines to pursue a topic.

Do not use absence when the scene simply never tests the behavior.

---

# 15. Negative constraints

Every mature reconstruction should include explicit “do not flatten into” constraints.

These are especially important because simulation systems tend to amplify salient surface traits.

Examples to test prospectively rather than assume:

## Chisato

- not a generic abstract pacifist;
- not a generic anti-DA dissident;
- not endlessly high-energy;
- not perfectly boundary-respecting;
- not incapable of deception;
- not automatically impressed by celebrity/status;
- not consciously using every joke as therapy;
- nonlethality does not equal unwillingness to inflict pain.

## Takina

- not robotic;
- literalism does not imply stupidity;
- emotional compression does not imply absence of affect;
- growth does not mean becoming Chisato;
- intimacy does not erase professional competence or lethal willingness.

These inherited candidate constraints remain provisional until V2 independently supports them.

---

# 16. Confidence architecture

Use separate dimensions.

## Evidence confidence

How strongly does source evidence establish the observation/policy?

Suggested qualitative states:

- `HIGH`
- `MODERATE`
- `LOW`
- `OPEN`

## Source authority

Where does evidence originate?

Use the source classes from the multi-source method.

## Reconstruction distance

### `R1_DIRECT_RECONSTRUCTION`

Near-equivalent source situation exists.

### `R2_CONSTRAINED_INTERPOLATION`

No identical scene, but multiple policies strongly constrain likely behavior.

### `R3_WEAK_EXTRAPOLATION`

At least one major variable is weakly evidenced.

### `R4_OPEN_SIMULATION`

The source scarcely constrains the answer.

A polished R4 response must still be labeled R4.

---

# 17. State-space coverage

For major characters, track whether evidence covers combinations of:

- familiarity;
- stakes;
- affect;
- power;
- interaction function;
- setting/role;
- relationship state.

The goal is not to assign a fake completeness percentage.

The goal is to identify holes such as:

> Chisato is well evidenced with strangers in service contexts but poorly evidenced with same-age celebrity peers.

or:

> Takina is well evidenced under operational pressure but weakly evidenced in low-stakes interpersonal disagreement after the main arc.

Side material should be used coverage-directively, not merely accumulated.

---

# 18. Prospective validation

Validation is mandatory for major models.

Recommended anime-native checkpoints:

- E01-E03 → predict E04-E06 behavior classes;
- E01-E06 → predict E07-E10;
- E01-E10 → predict E11-E13;
- E01-E13 → predict Shorts 01-06.

Predictions should target:

- action class;
- social initiative;
- emotional direction;
- register;
- moral choice;
- humor/play;
- relationship response;
- recalibration.

Do not predict plot merely to generate an easy score.

Prediction outcomes:

- `SUPPORTED`
- `PARTIALLY_SUPPORTED`
- `NOT_TESTED`
- `DISCONFIRMED`
- `DEVELOPMENTAL_INVALIDATION`
- `NEW_MODIFIER_REQUIRED`

A failure may indicate character development or an unmodeled state, not only analytical error.

---

# 19. Adversarial reconstruction tests

After a character has enough evidence, test situations designed to distinguish deep rules from surface imitation.

Potential Chisato tests:

- friendly stranger;
- shy stranger;
- irritating but harmless stranger;
- hostile non-dangerous stranger;
- grieving person;
- joke-averse person;
- someone praising her excessively;
- someone insulting Takina;
- harmless authority rule;
- trivial bureaucratic task;
- losing a game;
- being refused help.

Potential Takina tests:

- ambiguous instruction;
- inefficient coworker;
- indirect request;
- teasing;
- praise;
- unfair trivial competition;
- being wrong;
- accidental harm to Chisato;
- gift reception;
- irrational child question;
- secretly pleased state.

Tests should include decoy responses that match shallow stereotypes.

The model should justify why the selected response fits the evidence better.

---

# 20. Supplementary-source integration

After the anime-native baseline freezes, supplementary observations enter reconstruction only through the multi-source authority method.

Maintain conceptual layers:

1. `CORE_INVARIANT`
2. `SUPPLEMENTARY_EXTENSION`
3. `CHARACTERIZATION_ENVELOPE`
4. `SOURCE_LOCAL_VARIANT`

Default simulation uses layers 1 + 2.

A `SOURCE_LOCAL_VARIANT` may be selected explicitly for tasks such as:

> “Write Chisato specifically in Abe Kanari’s *Recollect* comedic realization.”

---

# 21. Character reconstruction artifact contract

A mature character reconstruction should normally contain:

1. source boundary;
2. authority state;
3. developmental scope;
4. invariant temperament;
5. values/moral constraints;
6. social initiative policies;
7. conflict/refusal policies;
8. care/reassurance policies;
9. humor/play policies;
10. stress/fear/grief transitions;
11. relationship modifiers;
12. language/register model;
13. performance model;
14. embodied behavior;
15. preferences/affordances;
16. competence effects;
17. negative constraints;
18. source-local variants;
19. coverage gaps;
20. validation history;
21. reconstruction confidence guidance;
22. evidence matrix route.

Do not force secondary characters into general-purpose models when the source only supports domain-limited reconstruction.

---

# 22. E01 operational contract

Before E01:

- PRE-E01 character state contains no V2 behavioral evidence;
- CP0 contains no behavioral predictions by design;
- V1 claims remain quarantined;
- supplementary material remains locked.

During E01:

- create atomic observations only when diagnostically useful;
- do not promote mature policies prematurely;
- initialize relationship state only from what E01 actually shows;
- create candidate policies with explicit low/initial coverage;
- record unknowns rather than importing V1 expectations;
- freeze outgoing E01→E02 predictions after E01 closes.

---

# 23. Failure modes

Do not:

- model from adjectives alone;
- confuse capability with frequency;
- confuse state with trait;
- globalize behavior from one relationship;
- use generated scenarios as evidence;
- turn literalism into stupidity;
- turn energy into emotional transparency;
- overfit comedy;
- erase developmental stage;
- let later sources leak into earlier model snapshots;
- claim confidence without coverage.

---

# 24. Governing rule

> **A character reconstruction is valid only to the extent that its response policies, state transitions, relationship modifiers, and uncertainties remain traceable to source evidence and become less confident as the hypothetical moves farther from observed state space.**
