---
series: KONOSUBA
artifact_type: analytical_method
scope: PER_VOLUME
method_version: V1
status: canonical
source_boundary: "Japanese main-series light novels in canonical volume order"
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
---

# KONOSUBA - Volume Deep-Reading Method

## 1. Purpose

This method governs every canonical main-series volume reading. It is designed to preserve literary interpretation while producing the structured evidence required for longitudinal character modeling, humor analysis, Japanese-language analysis, and prospective validation.

The core principle is:

> Comedy is evidence, but it is noisy evidence. Recover the stable machinery underneath the exaggeration without sanding away the exaggeration that actually defines the character.

The method must not reduce a novel to a spreadsheet. Each volume deep reading remains a coherent literary analysis. Ledgers support the reading; they do not replace it.

## 2. Pre-reading controls

Before opening a new volume:

1. confirm the source against `KONOSUBA_SOURCE_LOCK.md`;
2. confirm canonical sequence and unresolved source gaps;
3. read the latest checkpoint and the exact prospective predictions frozen before this tranche;
4. do not read later-volume summaries, fandom recaps, or adaptation material for interpretive guidance;
5. preserve the distinction between information available at this point in sequence and information learned later;
6. create or update only ledgers already justified by recurring evidence.

If the volume follows a checkpoint, the analyst must record the checkpoint predictions before reading. They may not be reformulated after the volume reveals the outcome.

## 3. Pass 1 - Structural and literary reading

Read the volume first as a novel.

Capture:

- chapter and section architecture;
- central conflicts;
- major plot events;
- new characters and factions;
- setting/worldbuilding additions;
- emotional peaks;
- reversals;
- comic set pieces;
- serious interruptions;
- relationship developments;
- genre parody and fantasy/RPG conventions;
- major motifs or recurring images;
- how the volume positions Kazuma as narrator.

Do not begin by assigning every joke a code. The first pass establishes what the work is doing before it is decomposed.

## 4. Pass 2 - Causal character reconstruction

For every high-information behavior, reconstruct the chain:

```text
STIMULUS
  -> PERCEPTION
  -> APPRAISAL
  -> DESIRE / FEAR / GOAL
  -> STABLE DISPOSITION OR CURRENT STATE
  -> COGNITIVE / AFFECTIVE DISTORTION
  -> AVAILABLE OPTIONS AS THE CHARACTER SEES THEM
  -> DECISION
  -> BEHAVIOR
  -> OUTCOME
  -> LEARNING / NON-LEARNING
```

The governing question is not merely "What did the character do?" but:

> Why did this option become attractive, acceptable, or inevitable to this particular character in this particular context?

Distinguish what the character objectively could have done from the options they actually noticed or considered.

## 5. Pass 3 - Decision and error analysis

Do not collapse apparently foolish behavior into a single intelligence judgment.

Possible error generators include:

- knowledge deficit;
- incorrect inference;
- attentional failure;
- impulsivity;
- overconfidence;
- vanity;
- status threat;
- greed;
- lust;
- laziness;
- fear;
- resentment;
- motivated reasoning;
- wishful thinking;
- poor risk estimation;
- short time horizon;
- social misreading;
- identity-protective reasoning;
- rigid preference;
- fixation;
- failure to update from prior experience;
- deliberate trolling;
- performative escalation in front of an audience;
- knowingly accepted impracticality;
- behavior that is rational under the character's values even if others judge it foolish.

A scene may involve several mechanisms. Prefer the smallest causal set that explains the behavior.

### Recommended Decision/Error Ledger fields

```text
volume / chapter / locator
character
stimulus
perceived situation
immediate goal
relevant stable disposition
state variable
error or bias mechanism
options apparently considered
decision
expected payoff
actual outcome
learning or non-learning
recurrence link
comic evidence class
confidence
```

## 6. Pass 4 - Competence decomposition

Never use a single smart/stupid or competent/incompetent axis.

Track separately when evidence supports them:

- factual knowledge;
- inferential reasoning;
- planning;
- practical judgment;
- technical/domain ability;
- social perception;
- social strategy;
- emotional regulation;
- impulse control;
- risk assessment;
- adaptability;
- learning from failure;
- crisis performance;
- resource management;
- domain specificity.

The objective is to identify asymmetric competence. A character may be technically extraordinary while strategically foolish, socially perceptive while impulsive, or mediocre in raw capability while unusually good at practical improvisation.

Do not infer a general cognitive rank from one domain.

## 7. Pass 5 - Humor mechanics and comic-evidence classification

For each major gag or recurring comic pattern, answer two different questions.

### 7.1 Why is it funny?

Possible mechanisms include:

- expectation violation;
- genre expectation violation;
- escalation;
- repetition/callback;
- bathos;
- hypocrisy exposure;
- status reversal;
- misunderstanding;
- dramatic irony;
- failed competence;
- social impropriety;
- sexual embarrassment;
- verbal aggression;
- physical farce;
- absurd commitment;
- reader superiority;
- sudden sincerity after nonsense;
- collision between two characters' incompatible decision rules.

This tag is descriptive, not exclusive. Several mechanisms may cooperate.

### 7.2 How literally should the scene inform the model?

Use four evidence classes.

**H1 - Direct behavioral evidence**

The scene is comic, but the action, motive, and consequence can be treated substantially literally.

**H2 - Real disposition with comic amplification**

The underlying motive/trait is strong evidence; the exact intensity, duration, physical result, or extremity should not automatically transfer into a realistic simulation.

**H3 - Gag-contingent behavior**

The scene may contain weak evidence, but the behavior is too dependent on a local punchline to generalize without recurrence.

**H4 - Nonliteral comic license**

Useful for understanding tone and humor mechanics; poor evidence for realistic behavioral prediction.

The deep reading must state when an important character claim relies primarily on H2-H4 evidence.

## 8. Pass 6 - Seriousness override and boundary analysis

Comic characters become most legible when the normal script stops working.

Mark scenes where a character's usual pattern is suppressed or transformed. Ask:

- What genuinely frightens this person?
- What genuinely hurts them?
- When does ritualized insult become real hostility?
- When does selfishness disappear?
- When does laziness disappear?
- When does lust, vanity, greed, or fixation cease to dominate?
- Who can trigger that change?
- What value or duty outranks the ordinary comic motive?
- Is the override temporary, relationship-specific, or evidence of development?

Seriousness-override scenes receive high reconstruction weight because they reveal goal hierarchy and moral/relational limits.

## 9. Pass 7 - Relationship and ensemble scripts

Do not treat party members as context-free individuals.

For each high-information dyad or group interaction, track:

- default stance;
- trust;
- affection;
- dependence;
- irritation;
- rivalry;
- known vulnerabilities;
- permitted insults;
- forbidden/serious insults;
- conflict triggers;
- manipulation strategies;
- appeasement/repair strategies;
- public versus private behavior;
- seriousness thresholds;
- shared-history callbacks;
- who knows what about whom.

Also track dynamic comic role:

- instigator;
- boke/fool role;
- tsukkomi/corrective role;
- victim;
- opportunist;
- accomplice;
- audience;
- escalator;
- saboteur;
- rescuer;
- moral objector.

Do not assume a character occupies one comic role permanently. Role switching is itself evidence about ensemble structure.

## 10. Pass 8 - Japanese voice and linguistic humor

Apply `KONOSUBA_JAPANESE_HUMOR_AND_VOICE_PROTOCOL.md` during every volume.

Track only patterns supported by the text. Relevant dimensions include:

- first-person reference;
- second-person/address forms;
- names and honorifics;
- plain versus polite register;
- sudden register shifts;
- exaggerated/mock politeness;
- sentence-final stance;
- contractions and clipping;
- written elongation or emotional deformation;
- interjections;
- recurring lexical choices;
- complaint, boast, plea, denial, and excuse formulas;
- syntactic timing;
- delayed reveal;
- repetition;
- ellipsis;
- short corrective retorts;
- boke/tsukkomi exchanges;
- wordplay or grammar-dependent jokes;
- narrator-specific rhetorical patterns.

For notable humor, assign translation-sensitivity class L0-L3 as defined in the language protocol.

## 11. Pass 9 - Kazuma narrator audit

Because the main novels are first-person, separate evidence into:

1. directly observable action;
2. direct speech;
3. independently observable consequence;
4. another character's report;
5. Kazuma's description;
6. Kazuma's interpretation;
7. Kazuma's speculation about another mind.

Track recurring narrator tendencies only when repeated evidence supports them, including possible:

- self-exoneration;
- selective attention;
- sexualized attention;
- hostile framing;
- rhetorical self-pity;
- exaggeration;
- accurate but uncharitable description;
- motivated interpretation;
- retrospective justification.

Do not diagnose global unreliability merely because the narrator is comic or biased. The goal is to model **where and how perspective changes evidentiary weight**.

## 12. Pass 10 - Ordinary-life and preference extraction

Simulation requires evidence outside quests, crises, and punchlines.

Extract when available:

- food/drink preferences;
- spending;
- saving;
- sleep;
- hygiene;
- clothing;
- chores;
- domestic competence;
- possessions;
- leisure;
- hobbies;
- alcohol;
- comfort seeking;
- boredom behavior;
- mundane anxieties;
- pet peeves;
- reactions to inconvenience;
- preferred company;
- conversational habits when nothing important is happening;
- attitudes toward work, effort, luxury, and routine.

Record absence carefully. A single preference mention does not automatically define a durable preference hierarchy.

## 13. Pass 11 - Volume-level model update

At the end of the volume, update each tracked character under these headings:

### New evidence

What behavior or context genuinely expands the model?

### Replication

Which existing mechanisms recur?

### Contradictions

Which prior claims are challenged?

### Boundary refinements

Where was an earlier rule too broad or too narrow?

### State changes

What appears to be development rather than another sample of a stable trait?

### Negative evidence

What expected behavior failed to occur in a context where the model predicted it should?

### Confidence

How strongly can the updated claim generalize beyond this scene?

Use claim states when a prior canonical checkpoint claim changes:

`PRESERVE | STRENGTHEN | REVISE | DOWNGRADE | REJECT | OPEN`

## 14. Pass 12 - Prospective predictions

Before the next tranche is read, create a limited set of falsifiable behavioral predictions.

Predictions are **not plot guesses**. They specify what a character should do if a relevant situation occurs.

Each prediction should contain:

```text
prediction_id
character
trigger/context
predicted appraisal
predicted dominant motive
predicted behavior or decision tendency
relationship/stakes modifiers
confidence
evidence basis
what would count as disconfirmation
future outcome field (blank until observed)
```

Good prediction:

> If a public status threat occurs while the character believes they can immediately demonstrate superiority, the model predicts escalation rather than quiet withdrawal, unless a previously identified seriousness override is active.

Bad prediction:

> The character will fight a dragon in the next volume.

## 15. Required structure of each volume deep reading

Each `KONOSUBA_V##_DEEP_READING.md` should normally contain:

1. authority/source metadata;
2. volume overview and narrative architecture;
3. chapter-by-chapter analytical reading;
4. major character findings;
5. relationship/ensemble findings;
6. decision/error and competence findings;
7. humor-system findings;
8. Japanese-language/voice findings;
9. Kazuma narrator/perspective findings;
10. seriousness-override findings;
11. ordinary-life/preference evidence;
12. worldbuilding/genre parody findings;
13. longitudinal model implications;
14. prior-prediction adjudication when applicable;
15. new or revised hypotheses;
16. source locators;
17. confidence limits and open questions.

The document need not force equal length into every section. Emphasize what the volume actually contains.

## 16. Locator convention

EPUB page numbers may be unstable across readers. Prefer reproducible source locators such as:

- volume;
- chapter/section title;
- scene description;
- distinctive short Japanese phrase or quote anchor;
- EPUB spine/XHTML item when technically available.

Exact Japanese quotations should be short and used as evidence anchors, not as substitute for analysis.

## 17. Governing standard

A strong volume reading should make later simulation more constrained.

After reading a volume, the analyst should know more precisely:

- what the character is likely to do;
- why;
- when that expectation fails;
- how another character changes the response;
- how much of the behavior is comic amplification;
- how the character's Japanese voice expresses the underlying process;
- what evidence would force revision.

If the reading only produces more adjectives, it has not completed the modeling task.
