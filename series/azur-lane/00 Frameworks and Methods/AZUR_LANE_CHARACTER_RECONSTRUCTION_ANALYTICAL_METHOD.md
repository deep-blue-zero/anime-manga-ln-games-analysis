---
series: AZUR_LANE
artifact_type: analytical_method
scope: CHARACTER_RECONSTRUCTION
generation: V1
method_version: "1.0.0"
status: canonical
source_boundary: "Azur Lane extracted multilingual primary-source character corpus (CN originating textual authority; JP/EN/TW/KR regional witnesses)"
supersedes: null
superseded_by: null
do_not_use_as_current_authority: false
governing_dependencies:
  - CURRENT_STATE_AND_CORPUS_MAP.md
  - AZUR_LANE_PIPELINE_METHOD.md
  - AZUR_LANE_READINESS_SCORING_METHOD.md
---

# Azur Lane Character Reconstruction Analytical Method

## 0. Purpose

This document governs the construction of **character reconstruction models** for *Azur Lane*.

Its purpose is to ensure that future character monographs and simulation guides use a consistent analytical process when reconstructing:

- speech;
- behavior;
- cognition and decision-making;
- motivations and values;
- emotional regulation;
- stress and failure responses;
- social behavior;
- relationship-conditioned behavior;
- professional and combat conduct;
- deception, leadership, care, humor, leisure, and other recurring behavioral domains;
- locale-specific linguistic register;
- plausible behavior and speech in novel situations.

The desired product is **not** a list of personality adjectives and is **not** a roleplay prompt assembled from memorable quotations.

The desired product is a source-grounded model capable of answering:

> Given this character's established goals, self-concept, relationships, habits, constraints, and context-sensitive decision rules, what would she most plausibly think, do, and say in a situation not directly depicted in the source?

This method governs the analytical transformation:

```text
PRIMARY-SOURCE CORPUS
        ↓
EVIDENCE SELECTION AND CONTEXT SEPARATION
        ↓
OBSERVED BEHAVIOR
        ↓
RECURRING PATTERNS
        ↓
COGNITIVE / BEHAVIORAL RULES
        ↓
ADVERSARIAL TESTING
        ↓
REVISED CHARACTER MODEL
        ↓
LOCALE-SPECIFIC SPEECH REALIZATION
        ↓
CONSTRAINED NOVEL-SITUATION SIMULATION
```

It does **not** govern game-client extraction, source normalization, corpus provenance, or corpus-readiness scoring. Those responsibilities remain with the existing Azur Lane corpus infrastructure.

---

# 1. Governing precedence

Before reconstructing any character, consult in this order:

1. `CURRENT_STATE_AND_CORPUS_MAP.md`
2. the current character's `CHARACTER_SOURCE_MAP.md`
3. the current character's `SOURCE_COVERAGE.md`
4. `AZUR_LANE_PIPELINE_METHOD.md`
5. `AZUR_LANE_READINESS_SCORING_METHOD.md`
6. this document
7. any character-specific active monograph, revision ledger, or speech/performance specialist artifact

This document assumes the corpus's existing source policy:

- CN is the originating textual authority in `origin` mode.
- JP, EN, TW, and KR are independently published regional witnesses.
- Regional witnesses must not be silently harmonized into a synthetic master text.
- Raw client text and provenance remain recoverable.
- Community sources do not silently replace extracted primary text.
- Known parser/source limitations remain explicit.

If the corpus map or source policy changes, this analytical method must be reviewed for compatibility.

---

# 2. Analytical responsibilities and non-goals

## 2.1 This method is responsible for

- distinguishing observed behavior from inferred disposition;
- identifying repeated decision patterns;
- separating stable traits from state-dependent behavior;
- separating context-specific registers;
- correcting for evidence-composition bias;
- constructing predictive cognitive rules;
- testing those rules against counterexamples;
- reconstructing relationship-conditioned behavior;
- reconstructing locale-specific speech styles;
- assigning confidence to extrapolations;
- preventing trope collapse;
- defining a consistent monograph structure;
- preserving uncertainty and contradiction.

## 2.2 This method is not responsible for

- determining gameplay strength;
- producing a ship-history article;
- ranking character popularity;
- judging whether a character is "well written";
- diagnosing psychiatric conditions without explicit textual basis;
- flattening regional localizations into one synthetic voice;
- deciding that textual divergence is censorship without separate evidence;
- treating every costume/skin context as literal continuous chronology;
- assuming affinity/oath behavior is the universal baseline state;
- treating every event gimmick or crossover as equally authoritative for baseline personality;
- inventing unsupported internal monologue.

---

# 3. Core distinction: semantic character vs. locale realization

Every reconstruction must distinguish two related but separate analytical objects.

## 3.1 Semantic character model

The semantic model answers:

> What does this character plausibly believe, notice, value, fear, want, infer, decide, and do?

This model is principally governed by the originating CN textual branch, interpreted through complete context and cross-checked against repeated behavior.

The semantic model includes:

- motivations;
- priorities;
- self-concept;
- decision rules;
- relationship models;
- emotional triggers;
- stress responses;
- habits;
- behavioral constraints;
- stable vulnerabilities;
- context-conditioned behavior.

## 3.2 Locale-specific speech model

The locale model answers:

> How does the independently published CN / JP / EN / TW / KR version of this character express that semantic content?

Locale realization may differ in:

- pronouns;
- honorifics;
- address forms;
- archaism;
- sentence endings;
- politeness;
- slang;
- idioms;
- martial or technical vocabulary;
- intensity;
- explicitness;
- intimacy;
- humor;
- profanity;
- verbal tics;
- sentence length;
- hesitation patterns;
- rhetorical framing.

The required architecture is:

```text
SEMANTIC INTENT / CHARACTER STATE
                ↓
       LOCALE REALIZATION
       CN  JP  EN  TW  KR
```

Do not construct a single synthetic "Takao voice," "Taihou voice," etc. and then mechanically translate it.

A behavior may be semantically stable across regions while being expressed through substantially different linguistic machinery.

---

# 4. Reconstruction readiness

The corpus readiness score measures **amount and contextual diversity of evidence**, not the truth of any particular interpretation.

Use the current `SOURCE_COVERAGE.md` and `AZUR_LANE_READINESS_SCORING_METHOD.md` before analysis.

## 4.1 Recommended reconstruction posture by readiness grade

### Grade A — unusually rich multi-context corpus

Suitable for:

- full character monograph;
- detailed cognitive model;
- contextual behavior rules;
- relationship-conditioned simulation;
- multilingual speech profiles;
- adversarial validation;
- C1–C3 novel-situation extrapolation.

### Grade B — substantial corpus

Usually suitable for:

- strong monograph;
- major behavioral domains;
- speech reconstruction;
- moderate novel-situation extrapolation.

Require stronger uncertainty labeling where dedicated stories, peer contexts, or social systems are sparse.

### Grade C — moderate usable corpus

Suitable for:

- constrained character profile;
- high-confidence observed patterns;
- limited decision rules;
- speech tendencies where evidence is sufficient.

Avoid broad claims about low-evidence domains.

### Grade D — sparse corpus

Suitable for:

- evidence ledger;
- narrow speech/style profile;
- explicit observed behavior.

Do not present a robust behavioral simulator as established.

### Grade E — insufficient corpus

Do not produce a full reconstruction monograph.

Produce a coverage/gap assessment instead.

## 4.2 Readiness is not authority

A Grade A character can still have a biased evidence distribution.

A Grade C character can still have a few exceptionally strong, direct observations.

Use composition warnings such as:

- `COMMANDER_HEAVY`
- `SKIN_HEAVY`
- low peer-social evidence;
- low sustained narrative evidence;
- regional gaps;
- identity ambiguity

as **sampling-bias diagnostics**, not as automatic disqualifiers.

---

# 5. Evidence hierarchy

Evidence weight is based on **context, recurrence, causal clarity, and source responsibility**, not raw line count.

A hundred repetitive secretary lines must not automatically outweigh one sustained narrative sequence that clearly shows a character making decisions under pressure.

## 5.1 Tier E1 — sustained high-context behavioral evidence

Highest default weight.

Includes:

- dedicated character-memory stories;
- sustained narrative scenes with clear cause → decision → consequence;
- repeated behavior across independent major narrative contexts;
- scenes where the character must choose between competing goals;
- scenes that expose failure, conflict, stress, care, leadership, or vulnerability.

Use E1 evidence to anchor:

- cognitive architecture;
- motivational hierarchy;
- failure response;
- relationship behavior;
- stable dispositions.

## 5.2 Tier E2 — independent peer/professional/social evidence

High weight.

Includes:

- substantive peer conversations;
- Fleet Chat and Juustagram interactions with meaningful character participation;
- relationship-specific sortie lines;
- mentoring scenes;
- professional coordination;
- combat decision-making;
- repeated interactions with named peers.

E2 is particularly important for correcting Commander-heavy sampling bias.

## 5.3 Tier E3 — baseline character-text evidence

Moderate-to-high weight when context is clear.

Includes:

- base-skin dialogue;
- profile text;
- login/home/mission lines;
- affinity progression;
- oath;
- combat lines;
- special secretary material.

These are valuable for:

- self-presentation;
- speech register;
- recurring preferences;
- intimacy progression;
- repeated values;
- short-form behavioral cues.

Do not treat affinity/oath content as baseline behavior toward everyone.

## 5.4 Tier E4 — skin/costume/context-specific evidence

Context-dependent weight.

Skin material can be highly diagnostic, but it must be tagged by:

- skin/context;
- relationship state;
- event framing;
- situational premise;
- degree of continuity certainty.

Use it strongly for:

- local register;
- embarrassment;
- leisure;
- clothing/presentation reactions;
- specific hobbies;
- intimacy states;
- repeated behavior that independently recurs elsewhere.

Do not let skin volume dominate the global model.

## 5.5 Tier E5 — crossover, alternate, gimmick, or structurally unusual evidence

Use cautiously.

Includes:

- collaboration/crossover events;
- random-word-generator or simulation premises;
- explicitly alternate-world material;
- transformed/possessed/controlled variants;
- obviously comedic or game-mechanical scenarios.

These can still reveal stable tendencies, especially when the character behaves consistently with ordinary material, but they require explicit context labels.

## 5.6 Secondary or external sources

Wikis, community summaries, fan interpretations, and external commentary may assist navigation or source discovery.

They are not primary evidence for reconstruction unless the governing corpus map explicitly elevates them.

---

# 6. Evidence independence

Repeated wording is not necessarily repeated evidence.

Before calling something a stable pattern, ask whether examples are genuinely independent.

Examples are less independent when they are:

- the same line repeated across skins;
- translation variants of one source record;
- multiple records from one single narrative beat;
- one joke repeated within one event;
- mechanical duplicates.

Examples are more independent when they occur across:

- different stories;
- different relationship contexts;
- different time periods/releases;
- different social groups;
- different stakes;
- different source systems.

Prefer **cross-context recurrence** over sheer frequency.

---

# 7. Context decomposition

Every character must be analyzed in separate behavioral/register contexts before global synthesis.

At minimum consider:

```text
PROFESSIONAL / DUTY
COMBAT
FACTIONAL
PEER_SOCIAL
MENTORING / INSTRUCTIONAL
COMPETITIVE
LOW_STAKES_LEISURE
COMMANDER_BASELINE
COMMANDER_AFFECTION
COMMANDER_OATH / INTIMATE
EMBARRASSED / SELF-EXPOSED
INJURED / FATIGUED
FAILURE / DEFEAT
ANGER / CONFLICT
SKIN_SPECIFIC
CROSSOVER / ALTERNATE
```

Add character-specific contexts when evidence warrants them.

Do not force empty categories.

## 7.1 Why context decomposition is mandatory

Without it, a reconstruction can easily mistake:

- Commander intimacy for universal social behavior;
- combat bravado for baseline conversation;
- skin flirtation for ordinary professional speech;
- embarrassment for generalized shyness;
- event comedy for a stable cognitive rule;
- faction rhetoric for private belief.

Global traits may only be inferred after examining whether they survive context changes.

---

# 8. Claim ontology

Every major monograph claim should be identifiable as one of the following.

## OBSERVED

Directly represented in primary-source behavior or speech.

Example form:

> In scene X, the character conceals an injury and attempts to continue working.

## RECURRING_PATTERN

A behavior or response appears across multiple sufficiently independent contexts.

Example form:

> Across several independent contexts, the character tends to subordinate personal discomfort to task completion.

## INFERRED_DISPOSITION

A stable tendency inferred from recurring patterns.

Example form:

> The character is prone to self-neglect when discomfort is interpreted as a personal obstacle to duty.

## DECISION_RULE

A predictive conditional derived from source-grounded patterns.

Example form:

> When a clear duty answer exists, the character tends to act directly rather than dwell on emotional uncertainty.

## RELATIONSHIP_RULE

Behavior that depends on a particular person or relationship class.

## SPEECH_RULE

A recurring linguistic realization tied to locale and context.

## NEGATIVE_CONSTRAINT

A behavior or interpretation the evidence argues against.

Example:

> Do not model the character as generally socially incompetent; awkwardness is concentrated in romantic self-exposure.

## LOCALE_VARIANT

A meaningful difference between independently published regional versions.

## OPEN

A question for which current evidence is inadequate, contradictory, parser-limited, or unresolved.

---

# 9. Evidence-to-model ladder

Do not jump from one scene directly to a personality label.

Use:

```text
OBSERVATION
   ↓
PATTERN
   ↓
DISPOSITION
   ↓
CONDITIONAL RULE
   ↓
NOVEL-SITUATION PREDICTION
```

Example:

```text
OBSERVATION:
Character hides a minor injury and continues a task.

PATTERN:
Character repeatedly minimizes personal discomfort during obligations.

DISPOSITION:
High tolerance for self-imposed strain; tendency toward duty-linked self-neglect.

CONDITIONAL RULE:
If the character believes discomfort does not materially prevent task completion,
she is likely to continue unless a trusted person reframes treatment as part of
responsible performance.

PREDICTION:
In a new but analogous work setting, she may underreport fatigue while still
maintaining others' safety.
```

Each step increases inferential distance and therefore requires stronger evidence or lower confidence.

---

# 10. Trait vs. state test

Before calling a behavior a stable trait, ask:

1. Does it recur?
2. Does it recur across independent contexts?
3. Does it persist across different relationship states?
4. Does it appear outside Commander-facing material?
5. Does it survive changes in stakes?
6. Are there clear counterexamples?
7. Could the behavior be explained by the immediate premise instead?
8. Could it be a skin/event/crossover-specific role?
9. Is it a localization artifact?
10. Does the proposed trait predict unseen examples better than a narrower rule?

Prefer the **narrowest rule that explains the evidence**.

If:

> "The character interprets every aspect of life through training"

fails but:

> "The character uses training as a preferred framework for self-development and personal uncertainty"

survives,

use the narrower rule.

---

# 11. Required cognitive reconstruction domains

A full monograph should attempt to model the following when evidence permits.

## 11.1 Motivational hierarchy

What does the character prioritize when goals conflict?

Possible categories include:

- duty;
- safety;
- loyalty;
- autonomy;
- affection;
- recognition;
- status;
- competence;
- curiosity;
- pleasure;
- ideology;
- revenge;
- harmony;
- self-preservation.

Do not assume ordering without conflict evidence.

## 11.2 Self-concept

How does the character define:

- competence;
- worth;
- identity;
- responsibility;
- femininity/masculinity where relevant;
- faction membership;
- role;
- strength;
- failure;
- intimacy.

## 11.3 Uncertainty response

When the character does not know what to do, do they:

- seek procedure;
- ask advice;
- experiment;
- withdraw;
- bluff;
- observe;
- imitate;
- become controlling;
- become playful;
- become anxious.

## 11.4 Failure attribution

Does failure produce:

- self-blame;
- external blame;
- strategic recalibration;
- shame;
- anger;
- renewed effort;
- avoidance;
- humor;
- denial.

Distinguish ordinary failure from moral, relational, or identity-threatening failure.

## 11.5 Stress and threat response

Model changes in:

- decisiveness;
- speech length;
- politeness;
- aggression;
- risk tolerance;
- self-preservation;
- protection of others;
- emotional display.

## 11.6 Emotional regulation

How does the character manage:

- embarrassment;
- fear;
- anger;
- jealousy;
- affection;
- grief;
- excitement;
- shame.

## 11.7 Norm enforcement

Separate:

- standards applied to self;
- standards applied to peers;
- safety rules;
- professional rules;
- etiquette;
- harmless informality.

Self-discipline must not automatically be interpreted as authoritarianism.

## 11.8 Care-giving

How does the character show concern?

Possible forms:

- direct reassurance;
- practical assistance;
- food;
- protection;
- planning;
- companionship;
- teasing;
- instruction;
- gifts;
- physical contact;
- silent presence.

## 11.9 Care-receiving

How readily does the character accept:

- help;
- concern;
- physical care;
- emotional support;
- protection;
- gifts;
- advice.

What framing makes acceptance easier or harder?

## 11.10 Leadership and delegation

Model:

- comfort with authority;
- delegation;
- trust;
- supervision;
- intervention threshold;
- handling of weaker subordinates;
- handling of competent peers;
- response to hierarchy.

## 11.11 Deception and concealment

Separate:

- omission;
- euphemism;
- face-saving;
- weak pretext;
- tactical deception;
- manipulative deception;
- sustained lying.

Do not infer broad manipulativeness from embarrassment-driven concealment.

## 11.12 Humor

Determine whether humor is:

- deliberate;
- dry;
- teasing;
- absurd;
- self-deprecating;
- accidental straight-man comedy;
- context-specific.

## 11.13 Leisure and low-stakes behavior

This domain is essential for avoiding high-stakes overfitting.

Ask how the character behaves when:

- nothing is wrong;
- nobody needs rescue;
- no duty is urgent;
- there is no romantic crisis.

---

# 12. Relationship reconstruction

Do not define relationships solely through labels such as:

- friend;
- sister;
- rival;
- lover.

Model **functional dynamics**.

For each important relationship, assess:

- trust;
- authority;
- dependence;
- mutual regulation;
- rivalry;
- teasing;
- protection;
- admiration;
- irritation;
- emotional disclosure;
- physical comfort;
- conflict style;
- role complementarity;
- what the other person can successfully persuade the character to do;
- which behaviors appear only in this relationship.

A relationship model should be able to explain:

> Why does this person change the character's behavior when another person making the same request might fail?

---

# 13. Relationship-state separation

Commander-facing behavior must be separated by relationship state.

At minimum:

```text
COMMANDER_BASELINE
COMMANDER_AFFECTION
COMMANDER_OATH / ESTABLISHED_INTIMACY
```

Do not use oath-level declarations to simulate a baseline stranger relationship.

Likewise, if a simulation assumes an established relationship, do not artificially reset the character to early-affinity emotional distance.

Every simulation should specify the target relationship state.

---

# 14. Skin and alternate-context policy

Skins are evidence, but context must remain explicit.

For every skin-derived claim ask:

1. Is this a stable personality tendency?
2. Is it triggered by the costume/situation?
3. Does it recur in base or narrative material?
4. Does it imply chronology, or only an alternate presentation context?
5. Does it alter relationship state?
6. Is the behavior intensified for fanservice?

Use skin evidence confidently for its local context.

Promote it to a global rule only when corroborated.

Do not treat all skins as literal points in one continuous chronology unless the text establishes that.

---

# 15. Crossover and alternate-scenario policy

Crossover or structurally unusual material may be used in three ways:

## CONFIRMATORY

The character behaves in a way already established elsewhere.

## BOUNDARY-TESTING

The unusual premise reveals how a stable trait operates under novel conditions.

## LOCAL-ONLY

The behavior depends too strongly on the special premise to generalize.

Do not allow crossover gimmicks to redefine baseline psychology without independent support.

---

# 16. Provisional model construction

After anchor readings, construct a provisional model.

Prefer **mechanisms** over adjectives.

Weak:

> serious, disciplined, competitive, shy

Stronger:

```text
clear duty → direct action
perceived personal deficiency → seek a trainable method
ordinary failure → internal attribution → recalibrate and retry
trusted principled correction → rapid incorporation
romantic self-exposure → composure disruption
```

The provisional model should identify:

- activation conditions;
- behavioral response;
- likely emotional state;
- likely speech change;
- exceptions;
- confidence.

---

# 17. Adversarial validation

Adversarial validation is mandatory before a full monograph becomes canonical.

After constructing the provisional model, actively search for scenes likely to falsify it.

Do **not** merely collect confirming examples.

## 17.1 Standard adversarial test menu

Search for:

- behavior that contradicts the proposed core trait;
- low-stakes peer-only scenes;
- situations with no Commander;
- failure without the predicted response;
- successful deception;
- failed deception;
- delegation;
- receiving care;
- rejecting care;
- harmless indiscipline;
- serious norm violations;
- leisure;
- humor;
- unfamiliar outsiders;
- authority conflict;
- being subordinate;
- being leader;
- injury;
- embarrassment;
- fear;
- anger;
- romantic exposure;
- situations where the character changes their mind.

Not every character will have evidence for every test.

## 17.2 Revision vocabulary

After adversarial testing, classify major provisional claims as:

- `PRESERVE`
- `STRENGTHEN`
- `REVISE`
- `DOWNGRADE`
- `REJECT`
- `OPEN`

A model that never changes during adversarial validation should be treated with suspicion.

---

# 18. Contradictions

Contradiction is not automatically noise.

When two scenes disagree, test:

1. different context?
2. different relationship state?
3. different chronology?
4. skin-specific behavior?
5. deliberate character development?
6. regional rewrite?
7. comedy/gimmick?
8. genuine inconsistency?
9. identity-resolution error?
10. extraction/alignment error?

Preserve unresolved contradictions rather than forcing false coherence.

---

# 19. Multilingual speech reconstruction

Speech modeling must be locale-specific.

## 19.1 Required dimensions

For each locale with sufficient evidence, model:

- self-reference;
- addressee terms;
- honorifics;
- politeness;
- formality;
- archaism;
- sentence endings;
- sentence length;
- clause density;
- contractions;
- slang;
- idioms;
- rhetorical questions;
- imperative style;
- hesitation/disfluency;
- laughter;
- interjections;
- profanity;
- metaphor families;
- technical/martial vocabulary;
- intimacy markers;
- embarrassment markers;
- combat register;
- peer register;
- professional register.

## 19.2 Stable alignment priority

For language comparison, prefer:

1. identical ship/skin/slot character-text records;
2. dedicated story scenes manually verified in local context;
3. event scenes with stable story/sequence structure;
4. social-thread alignments only after local neighborhood verification.

A nominally aligned social message can be displaced by regional insertion/reordering.

Do not infer a characterization shift from sequence-number alignment alone when the surrounding thread does not match.

---

# 20. Regional authority policy

Use:

## Originating semantic question

> What is the originating characterization?

CN normally governs.

## Regional-publication question

> How is this character presented in the Japanese / English / Korean / Taiwanese release?

That locale is independently authoritative for that question.

## Performed Japanese voice question

JP text plus Japanese audio performance governs.

Do not silently use JP wording to rewrite CN semantic claims.

Do not silently use EN wording as if it were a neutral translation.

---

# 21. Regional divergence classification

Where relevant, distinguish:

- equivalent meaning;
- lexical variation;
- register shift;
- formality shift;
- intimacy shift;
- expansion;
- compression;
- omission;
- addition;
- relationship framing shift;
- characterization shift candidate;
- lore shift candidate;
- political/historical shift candidate;
- structural rewrite;
- unresolved.

Do not call a difference censorship without separate evidence.

---

# 22. Performed voice layer

Textual speech reconstruction and performed voice reconstruction are separate responsibilities.

If audio has not been systematically analyzed, mark:

```text
PERFORMED_VOICE_MODEL: OPEN
```

A later performance pass may analyze:

- pitch range;
- baseline timbre;
- tempo;
- pause structure;
- breathiness;
- clipped vs. flowing delivery;
- emphasis;
- laughter;
- sighs;
- vocal fry;
- hesitations;
- emotional compression;
- shouted combat register;
- intimate register;
- changes under embarrassment, anger, fear, fatigue, or grief.

Do not fabricate performance traits from text alone.

---

# 23. Simulation confidence classes

Every extrapolative claim should be assignable to one of these classes.

## C1 — DIRECT CANON

The behavior/speech is directly observed.

## C2 — STRONG RECONSTRUCTION

The rule is supported by multiple independent contexts and survives adversarial testing.

## C3 — CONSTRAINED EXTRAPOLATION

The exact situation is novel, but established rules strongly constrain the likely response.

## C4 — PLAUSIBLE SPECULATION

Compatible with the model but not strongly predicted.

## C5 — UNSUPPORTED

Current evidence does not meaningfully constrain the answer.

Simulation should preferentially operate in C1–C3.

C4 must be labeled as speculative when analytically relevant.

Do not present C5 as character fact.

---

# 24. Novel-situation simulation protocol

When predicting behavior in a novel situation:

## Step 1 — define state

Specify:

- locale;
- relationship state;
- chronology/continuity assumptions;
- whether skin/event context applies;
- stakes;
- current emotional state.

## Step 2 — identify active goals

List the character's likely competing objectives.

## Step 3 — identify the highest-priority known rule

Examples:

- protect others;
- fulfill duty;
- preserve autonomy;
- maintain harmony;
- seek competence;
- avoid exposure;
- remain beside attachment figure.

## Step 4 — apply context modifiers

Ask:

- public or private?
- peer or superior?
- Commander or stranger?
- danger or leisure?
- injured or healthy?
- embarrassed or composed?

## Step 5 — generate semantic response

Determine likely:

- perception;
- interpretation;
- decision;
- action;
- emotional response.

## Step 6 — realize speech in target locale

Apply the locale-specific speech model.

## Step 7 — anti-caricature check

Remove unsupported repetitions of signature vocabulary, tropes, or gimmicks.

## Step 8 — confidence label

Classify the simulation as C1–C5 if the output is being used analytically.

---

# 25. Thought reconstruction

Internal thoughts are often less directly observable than speech and action.

Therefore thought modeling requires special caution.

Use direct internal narration where available.

Otherwise infer thought through:

- explicit statements;
- observable choices;
- repeated causal behavior;
- stable self-concept;
- consistent emotional triggers.

Do not convert every behavior into a detailed hidden monologue.

Prefer:

> "She would likely interpret this as a failure of preparation."

over:

> "She thinks exactly: 'I have dishonored my path and must train twice as hard tomorrow.'"

unless the text supports that wording.

---

# 26. Anti-caricature constraints

Every monograph must contain explicit negative constraints.

Common errors include:

- turning a recurring metaphor into every sentence;
- turning one embarrassment trigger into generalized shyness;
- turning discipline into universal authoritarianism;
- turning affection into constant flirtation;
- turning tactical intelligence into omniscience;
- turning competence into emotional invulnerability;
- turning one relationship dynamic into behavior toward everyone;
- turning skin fanservice into baseline sexuality;
- turning oath intimacy into baseline Commander behavior;
- turning a regional speech feature into universal semantic characterization.

A good simulator should often be recognizable **without** using the character's most famous verbal tic.

---

# 27. Sampling-bias correction

For every monograph, explicitly state corpus composition.

At minimum inspect:

- proportion Commander-facing;
- proportion skin-specific;
- narrative depth;
- peer-social coverage;
- dedicated story coverage;
- relationship diversity;
- regional coverage.

If `COMMANDER_HEAVY`, actively prioritize peer and narrative evidence when constructing global traits.

If `SKIN_HEAVY`, do not allow costume-context behavior to dominate baseline psychology.

If peer evidence is sparse, mark peer extrapolations lower confidence.

---

# 28. Source disagreement and locale bias

Regional texts can intensify or soften:

- intimacy;
- aggression;
- archaic register;
- military framing;
- family framing;
- flirtation;
- politeness;
- emotional explicitness.

Therefore:

> linguistic intensity is not automatically psychological intensity.

A JP character may sound more archaic than CN without being semantically more traditional.

An EN character may use more explicit genre vocabulary while having less marked grammar.

Separate **surface realization** from **underlying claim**.

---

# 29. Required monograph structure

Future full character monographs should normally use:

```text
<SERIES>_<CHARACTER>_CHARACTER_MONOGRAPH.md
```

For example:

```text
AZUR_LANE_TAKAO_CHARACTER_MONOGRAPH.md
```

Recommended front matter:

```yaml
---
series: AZUR_LANE
artifact_type: character_monograph
scope: TAKAO
generation: V1
status: active_provisional
source_boundary: "Pinned Azur Lane multilingual primary-source corpus"
governing_method: AZUR_LANE_CHARACTER_RECONSTRUCTION_ANALYTICAL_METHOD.md
method_version: "1.0.0"
source_build_id: "<build id>"
semantic_authority: CN
regional_witnesses: [JP, EN, TW, KR]
performed_voice_status: open
supersedes: null
superseded_by: null
do_not_use_as_current_authority: false
---
```

## Required sections

1. **Authority, scope, and corpus condition**
2. **Executive character model**
3. **Evidence composition and bias warnings**
4. **Core psychological architecture**
5. **Motivational hierarchy**
6. **Self-concept and identity**
7. **Decision-making under ordinary conditions**
8. **Uncertainty and learning**
9. **Failure and recovery**
10. **Stress, danger, and combat**
11. **Emotional regulation**
12. **Care-giving and care-receiving**
13. **Leadership, delegation, and authority**
14. **Deception, concealment, and honesty**
15. **Norm enforcement and tolerance**
16. **Humor, leisure, and low-stakes behavior**
17. **Relationship models**
18. **Commander relationship-state progression**
19. **Context/register matrix**
20. **CN speech model**
21. **JP speech model**
22. **EN speech model**
23. **TW speech model**
24. **KR speech model**
25. **Cross-locale characterization differences**
26. **Performed voice model or OPEN status**
27. **Simulation decision rules**
28. **Negative constraints / anti-caricature rules**
29. **Novel-situation extrapolation guide**
30. **Adversarial validation results**
31. **Confidence matrix**
32. **Open questions and unsupported domains**
33. **Evidence locator index**
34. **Revision state**

Do not create empty sections merely for symmetry. If a locale or domain lacks evidence, state that succinctly.

---

# 30. Context/register matrix

Every monograph should include a table approximately like:

| Context | Cognition | Behavior | Speech/Register | Confidence |
|---|---|---|---|---|
| Professional | ... | ... | ... | ... |
| Combat | ... | ... | ... | ... |
| Peer casual | ... | ... | ... | ... |
| Commander baseline | ... | ... | ... | ... |
| Commander intimate | ... | ... | ... | ... |
| Embarrassed | ... | ... | ... | ... |
| Failure | ... | ... | ... | ... |
| Leisure | ... | ... | ... | ... |

This is a simulation-facing summary, not a substitute for the analysis supporting it.

---

# 31. Decision-rule format

Where practical, express predictive rules as:

```text
TRIGGER
    ↓
APPRAISAL
    ↓
PRIORITY
    ↓
LIKELY ACTION
    ↓
SPEECH CHANGE
    ↓
EXCEPTIONS
```

Example:

```text
TRIGGER:
Unexpected personal failure.

APPRAISAL:
"I was insufficiently prepared."

PRIORITY:
Restore competence.

LIKELY ACTION:
Reassess technique and retry.

SPEECH CHANGE:
More self-critical and concise.

EXCEPTIONS:
If failure threatens relational worth rather than competence alone,
shame may become much stronger.

CONFIDENCE:
C2.
```

This is preferable to vague labels such as "perfectionist."

---

# 32. Adversarial-validation record

Every canonical monograph should preserve a concise revision table:

| Provisional claim | Test | Result | Transition | Current formulation |
|---|---|---|---|---|
| ... | ... | ... | PRESERVE/STRENGTHEN/REVISE/DOWNGRADE/REJECT/OPEN | ... |

This provides provenance for **interpretive evolution**, not just source extraction.

---

# 33. Confidence matrix

For major domains, record confidence separately.

Example:

| Domain | Confidence | Basis | Limitation |
|---|---|---|---|
| Duty behavior | High | many independent narrative scenes | — |
| Peer leisure | Medium | few social scenes | sparse long-form evidence |
| Romantic behavior | High | affinity + dedicated story | Commander-specific |
| Deception | Medium | several concealment examples | no high-stakes manipulation evidence |
| JP performance | Open | text only | no systematic audio audit |

Do not collapse all confidence into one number.

---

# 34. When to stop analysis and write the monograph

A character is ready for a full monograph when:

1. the corpus is sufficiently ready for the desired scope;
2. anchor narrative/dedicated stories have been read;
3. peer/non-Commander evidence has been inspected where available;
4. Commander relationship stages have been separated;
5. a provisional cognitive model exists;
6. adversarial testing has been performed;
7. major claims have revision statuses;
8. locale-specific speech evidence has been inspected;
9. unsupported domains are explicit;
10. the model predicts source behavior better than a trope/adjective summary.

Do not delay indefinitely in pursuit of perfect completeness.

A monograph may be `active_provisional` and later strengthened.

---

# 35. When not to write a full monograph

Prefer a smaller artifact when:

- source coverage is too sparse;
- all evidence comes from one relationship context;
- identity resolution is uncertain;
- major source systems remain missing for that character;
- regional alignment is too weak for the requested language model;
- the character has too little dialogue for speech reconstruction.

Possible alternatives:

- `CHARACTER_EVIDENCE_PROFILE`
- `SPEECH_PROFILE`
- `BEHAVIORAL_CHECKPOINT`
- `RECONSTRUCTION_READINESS_AUDIT`

---

# 36. Methodological lessons from the pilot reconstruction

The first pilot reconstruction demonstrated several general lessons that now become method requirements.

## 36.1 Prefer mechanisms to tropes

A trope label can be descriptively useful but is not a predictive model.

## 36.2 Adversarial testing materially improves accuracy

An initially broad rule may survive only in a narrower activation domain.

## 36.3 High-stakes behavior does not automatically describe leisure behavior

Peer and ordinary-life scenes are analytically necessary.

## 36.4 Commander-heavy evidence can distort global characterization

Separate relationship-conditioned behavior before synthesis.

## 36.5 Locale-specific grammar can carry characterization independently of semantic content

Speech reconstruction must therefore be multilingual and layered.

## 36.6 A character can be self-disciplined without imposing equal discipline on others

Model norm enforcement explicitly rather than inferring it from self-control.

## 36.7 Deception must be decomposed by function and sophistication

Embarrassment-driven concealment is not equivalent to strategic manipulation.

## 36.8 Care may have an entry condition that later disappears with trust

Relationship development can alter decision rules rather than merely increase emotional intensity.

These are methodological principles, not Takao-specific traits.

---

# 37. Revision and supersession

Major reinterpretations should use:

- `PRESERVE`
- `STRENGTHEN`
- `REVISE`
- `DOWNGRADE`
- `REJECT`
- `OPEN`

If a later corpus build materially changes a monograph:

- preserve the earlier monograph if it is a frozen release;
- produce a later generation;
- create or update a claim revision ledger when changes are substantial;
- identify source-build changes;
- update `supersedes` / `superseded_by`.

Do not silently rewrite frozen analytical releases.

---

# 38. Method versioning

This document is `method_version: 1.0.0`.

Use semantic-style method revisions:

## Patch

Clarification that does not change analytical conclusions or required workflow.

Example:

```text
1.0.0 → 1.0.1
```

## Minor

Adds a new analytical domain or validation procedure while remaining compatible.

Example:

```text
1.0.x → 1.1.0
```

## Major

Changes evidence authority, confidence ontology, required workflow, or monograph architecture in a way that can alter existing results.

Example:

```text
1.x → 2.0.0
```

Existing monographs should record the governing method version.

---

# 39. Pre-generation checklist for every character

Before writing or updating a monograph:

- [ ] resolve canonical Azur Lane root;
- [ ] consult `MANGA_ANIME_DRIVE_INDEX.md`;
- [ ] read `CURRENT_STATE_AND_CORPUS_MAP.md`;
- [ ] confirm build ID;
- [ ] read character `CHARACTER_SOURCE_MAP.md`;
- [ ] read `SOURCE_COVERAGE.md`;
- [ ] inspect composition warnings;
- [ ] identify dedicated stories;
- [ ] identify sustained narrative scenes;
- [ ] identify peer/non-Commander evidence;
- [ ] identify Commander relationship stages;
- [ ] identify skin/context-specific evidence;
- [ ] inspect relationship evidence;
- [ ] inspect regional crosswalk;
- [ ] verify suspicious social alignments locally;
- [ ] note parser-unsupported systems;
- [ ] check for existing monograph/topical home;
- [ ] check authority/supersession state.

---

# 40. Reconstruction workflow

## Phase R0 — Corpus and readiness audit

Establish:

- build;
- authority;
- coverage;
- bias warnings;
- unsupported systems.

## Phase R1 — Evidence map

Identify:

- anchor stories;
- peer scenes;
- relationship evidence;
- dialogue layers;
- regional witnesses.

## Phase R2 — Anchor reading

Read sustained narrative and dedicated character material in complete scene context.

Record observations without premature synthesis.

## Phase R3 — Context ledgers

Separate:

- professional;
- combat;
- peer;
- leisure;
- Commander states;
- skin contexts;
- stress states.

## Phase R4 — Provisional cognitive model

Construct:

- motivations;
- self-concept;
- decision rules;
- failure model;
- care model;
- leadership model;
- deception model;
- emotional triggers.

## Phase R5 — Adversarial validation

Seek counterexamples.

Apply claim transitions.

## Phase R6 — Relationship synthesis

Model major relationships as functional dynamics.

## Phase R7 — Multilingual speech reconstruction

Build CN / JP / EN / TW / KR register profiles using stable alignments and verified scenes.

## Phase R8 — Simulation extrapolation

Create decision rules and C1–C5 prediction boundaries.

## Phase R9 — Monograph

Write the character monograph under this method.

## Phase R10 — Optional performance pass

If audio exists and analytical value warrants it, add a performed-voice specialist layer and revise the monograph.

---

# 41. Quality-control questions

Before declaring a reconstruction usable, ask:

### Evidence

- Can every major claim be routed back to primary evidence?
- Are repeated examples actually independent?
- Are context-specific examples mislabeled as global?

### Cognition

- Does the model explain decisions, not just describe traits?
- Does it contain activation conditions?
- Does it explain counterexamples?

### Relationships

- Are Commander states separated?
- Are peer relationships represented independently?
- Does the model explain why different people can influence the character differently?

### Speech

- Are locale-specific forms modeled independently?
- Have address terms and intimacy gradients been captured?
- Have social-thread alignments been manually checked where structure differs?
- Is performed voice clearly separated from textual register?

### Simulation

- Can the model generate a plausible low-stakes response?
- Can it generate a failure response?
- Can it generate behavior without relying on signature catchphrases?
- Are C4/C5 areas clearly bounded?

### Anti-caricature

- Would removing the character's most famous trope still leave a recognizable decision process?

If not, the reconstruction is too shallow.

---

# 42. Canonical analytical principle

The governing principle of Azur Lane character reconstruction is:

> **Reconstruct the character as a conditional decision system before reconstructing her as a style of dialogue.**

Speech, behavior, and thought should emerge from:

- goals;
- context;
- relationship state;
- self-concept;
- uncertainty;
- emotional state;
- learned habits;
- cultural/locale realization.

The final simulator should not merely reproduce recognizable phrases.

It should produce responses that remain recognizably in-character even when:

- the situation is new;
- the Commander is absent;
- the character is not fighting;
- the character is not flirting;
- the character's signature motif is irrelevant;
- the target language changes.

That is the standard by which future Azur Lane character monographs and simulation models should be judged.
