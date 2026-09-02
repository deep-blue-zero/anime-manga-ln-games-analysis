---
series: MHA
artifact_type: analytical_method
scope: CHARACTER_MODELING
generation: V2
status: canonical
source_boundary: Japanese manga evidence accumulated through the MHA_SP2 sequential reread
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
---

# MHA SP2 — Character Modeling and Reconstruction Schema

## Purpose

This schema defines how character evidence should be recorded so that the V2 corpus can later reconstruct plausible character speech, judgment, interaction, and behavior without presenting inference as canon.

It is a specialized extension of the main second-pass analytical method.

## 1. Epistemic hierarchy

For modeling purposes, use this order:

1. directly observed Japanese dialogue/action/panel evidence;
2. repeated behavioral pattern across contexts;
3. relationship-specific pattern;
4. strongly supported inferred disposition or heuristic;
5. conditional prediction;
6. speculative alternative.

Predicted behavior never becomes source evidence unless a later canonical scene independently supports it.

## 2. Evidence atom

The smallest modeling unit is a behavioral evidence atom:

| Field | Meaning |
|---|---|
| Character | Actor being modeled |
| Scope | Volume/chapter/page |
| Context | Low stakes, competition, danger, shame, authority, care, etc. |
| Partner(s) | Relevant social target |
| Knowledge state | What the character knows at this moment |
| Trigger | Immediate precipitating event |
| Observable behavior | What the character actually says/does |
| Japanese voice | Exact or summarized speech marker if important |
| Interpretation | What the behavior may reveal |
| Evidence class | Explicit / strong inference / plausible / unresolved |
| Repetition status | one-off / repeated / contradicted / revised |
| Confidence | low / medium / high |

Do not store a trait label without at least one evidence atom.

## 3. Model dimensions

### A. Goals and motivational hierarchy
- immediate wants;
- persistent long-term desires;
- obligations;
- status goals;
- relationship goals;
- avoidance goals;
- conditions under which one goal overrides another.

### B. Self-model
- claimed identity;
- private self-conception;
- ideal self;
- feared self;
- shame triggers;
- pride anchors;
- discrepancy between self-description and behavior.

### C. Moral and normative model
- what counts as right/wrong;
- power philosophy;
- rescue/protection assumptions;
- legitimacy beliefs;
- responsibility boundaries;
- treatment of opponents;
- treatment of weaker people;
- tolerance for coercion, deception, sacrifice, and risk.

### D. Perception and attention
- what the character notices first;
- expertise-specific attention;
- emotional cues noticed or missed;
- tendency toward concrete vs abstract reasoning;
- threat detection;
- hierarchy/status sensitivity;
- common attribution errors.

### E. Decision policy
- speed of decision;
- preference for action vs deliberation;
- acceptable uncertainty;
- risk tolerance;
- willingness to delegate;
- use of rules;
- willingness to violate rules;
- escalation threshold;
- retreat threshold;
- help-seeking threshold.

### F. Emotional regulation
- baseline affect;
- suppression/expression style;
- anger pattern;
- fear pattern;
- embarrassment pattern;
- grief pattern;
- recovery pattern;
- displacement or masking behavior.

### G. Social behavior
- default politeness;
- dominance behavior;
- deference behavior;
- teasing/humor;
- affection display;
- care behavior;
- praise acceptance;
- criticism response;
- apology/repair style;
- conflict persistence.

### H. Relationship-conditioned behavior
For important partners record deltas from baseline:
- trust;
- openness;
- aggression;
- protectiveness;
- rivalry;
- embarrassment;
- speech/register;
- physical distance/touch;
- expected reciprocity;
- special permissions or taboos.

### I. Stress regimes
At minimum distinguish:
- ordinary daily life;
- training/competition;
- public evaluation;
- interpersonal conflict;
- acute danger;
- injury/exhaustion;
- moral dilemma;
- humiliation/shame;
- grief/loss;
- command responsibility.

A character who is well-modeled in battle may still be poorly modeled in ordinary social life, and vice versa.

### J. Japanese speech model
Record:
- pronouns;
- address terms;
- honorifics;
- sentence endings;
- politeness;
- contractions;
- lexical preferences;
- insults;
- praise;
- swearing/aggression;
- fillers;
- hesitation;
- ellipsis;
- rhetorical questions;
- volume/emphasis represented typographically;
- changes by relationship and stress.

A simulation should not imitate surface catchphrases while missing register logic.

### K. Embodied action model
- quirk use habits;
- bodily self-preservation or disregard;
- rescue/fight style;
- movement tendencies;
- habitual gestures if recurrent;
- pain tolerance;
- body-image issues;
- relationship to costume/support equipment.

### L. Knowledge and epistemic boundary
Before predicting behavior, specify:
- what facts the character knows;
- what facts they believe incorrectly;
- what future information they cannot use;
- what secrets they possess;
- what social context they misread.

This prevents full-series analyst knowledge from leaking into simulated character knowledge.

## 4. State versus trait

Every modeling claim should be labeled implicitly or explicitly as one of:

- **stable tendency** — repeated across substantial contexts;
- **current state** — true at the present point in the story but expected to change;
- **relationship-specific tendency**;
- **role-specific behavior** — e.g. teacher, student, hero, child, rival;
- **stress-specific behavior**;
- **one-off exceptional behavior**.

Do not promote a state into a trait merely because it is memorable.

## 5. Revision vocabulary

Use the project-wide claim-transition vocabulary when later evidence changes a model:

- `PRESERVE`
- `STRENGTHEN`
- `REVISE`
- `DOWNGRADE`
- `REJECT`
- `OPEN`

For behavior models, also record whether the change is caused by:

- character growth;
- earlier misread;
- newly revealed context;
- relationship specificity;
- stress specificity;
- contradiction not yet resolved.

## 6. Reconstruction output contract

When asked to simulate or reconstruct a character in a novel situation, generate internally from:

1. current character state at the requested chronology;
2. relationship state with present characters;
3. knowledge available to the character;
4. stakes and stress regime;
5. relevant decision heuristics;
6. Japanese speech/register evidence if dialogue is requested.

The resulting answer should distinguish:

- **high-confidence likely behavior**;
- **plausible alternatives**;
- **conditions that would flip the choice**;
- **areas where the corpus is insufficient**.

## 7. Chronology lock

Every model use must state a chronology boundary when later development would materially change behavior.

Examples:
- Bakugo at V01 is not Bakugo at V29 or the epilogue.
- Endeavor before the Pro Hero arc is not later Endeavor.
- Shigaraki/Tenko changes radically across revelation and bodily transformation.

A model may expose multiple snapshots, but must never silently merge them.

## 8. Validation protocol

The preferred validation method is held-out prediction.

1. freeze a character model at Volume N;
2. identify a later canonical scene not used in model construction;
3. describe the scene's initial conditions without revealing the outcome;
4. predict likely behavior, speech, and decision path;
5. compare with the actual scene;
6. score:
   - action choice;
   - motive;
   - speech/register;
   - emotional trajectory;
   - relationship handling;
7. diagnose mismatch;
8. revise model only from canonical evidence.

This tests whether the model predicts rather than merely explains after the fact.

## 9. Model readiness index

Use:

- `insufficient`
- `emerging`
- `moderate`
- `strong`
- `specialist_ready`

Readiness should consider five independent coverage dimensions:

| Dimension | Question |
|---|---|
| Context breadth | Have we seen the character in multiple stakes/regimes? |
| Relationship breadth | Have we seen behavior toward different kinds of people? |
| Language breadth | Is speech/register sufficiently sampled? |
| Longitudinal depth | Have we observed change over time? |
| Contradiction resolution | Do apparent inconsistencies have contextual explanations? |

A famous character with many battle scenes can still be only `moderate` if ordinary speech and relational behavior are undersampled.

## 10. Volume-level update rule

After each volume:

- update state only when evidence changes or clarifies it;
- add behavioral evidence even without a state change if it expands context breadth;
- record negative evidence when an expected behavior fails to occur;
- preserve contradictions rather than immediately harmonizing them;
- update readiness only when a coverage dimension materially changes.

## 11. Anti-hallucination rules

Never infer from:
- fandom archetype labels alone;
- hero/villain alignment;
- quirk type;
- costume design without behavioral support;
- later behavior when modeling an earlier chronology;
- one memorable quote treated as total personality;
- anime-only delivery when the current source boundary is manga, unless explicitly added as a supplementary performance layer.

## 12. End goal

The model should be capable of answering not merely:

> What would this character say?

but:

> What would this version of the character notice, believe, want, fear, decide, say, and do in this situation, toward these people, given what they know—and how confident are we?
