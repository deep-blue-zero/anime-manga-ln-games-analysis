\---  
series: KIMISHINU  
artifact\_type: synthesis\_architecture  
scope: longitudinal\_ledgers  
generation: V1  
revision: 1.1  
updated: 2026-08-26  
status: canonical  
source\_boundary: "Designed before V01; applies prospectively through current manga boundary"  
supersedes: null  
superseded\_by: null  
do\_not\_use\_as\_current\_authority: false  
\---

\# KIMISHINU\_LONGITUDINAL\_LEDGER\_ARCHITECTURE.md

\#\# Purpose

This document defines the mutable longitudinal state infrastructure for the KimiShinu deep-reading project. Ledgers are cumulative analytical state, not duplicate volume summaries. They exist to make character reconstruction, relationship tracking, claim revision, and later synthesis possible without rereading every prior volume from scratch.

The initial architecture uses five ledgers. This is deliberately compact. New ledgers should be added only when a recurring analytical responsibility becomes too dense or too important to remain inside these five homes.

\#\# Governing update rule

After each completed deep reading:  
1\. update only ledgers materially affected by the new source;  
2\. preserve earlier state and explicitly route changes;  
3\. identify source boundary and locators;  
4\. separate directly observed evidence from interpretation;  
5\. do not rewrite history as though the mature interpretation was always obvious.

Claim/state transitions use:  
\`PRESERVE\`, \`STRENGTHEN\`, \`REVISE\`, \`DOWNGRADE\`, \`REJECT\`, \`OPEN\`.

Each ledger entry should identify at minimum:  
\- character/relationship/system target;  
\- previous state or claim ID where applicable;  
\- new formulation;  
\- transition class;  
\- scope boundary;  
\- evidence locator(s);  
\- confidence;  
\- unresolved counterevidence or ambiguity.

\#\# Ledger 1 — KIMISHINU\_CHARACTER\_STATE\_LEDGER.md

\#\#\# Responsibility  
Maintain reconstructable models of individual characters across time.

\#\#\# Track  
\- baseline temperament;  
\- motives, desires, aversions;  
\- beliefs and misbeliefs;  
\- coping and defense patterns;  
\- emotional regulation;  
\- conflict behavior;  
\- attachment behavior;  
\- self-conception and identity language;  
\- agency and perceived options;  
\- moral intuitions;  
\- stable speech tendencies;  
\- context-dependent behavioral changes;  
\- contradictions that may indicate growth, masking, situational pressure, or an incomplete model.

\#\#\# Entry model  
Prefer stable IDs such as \`SHI-V01-01\` or another clearly documented character abbreviation established during V01. Do not invent a comprehensive cast taxonomy before names and roles are verified from source.

Each state change should distinguish:  
\`baseline\` / \`new evidence\` / \`current model\` / \`confidence\` / \`open test\`.

\#\#\# Character-modeling constraint  
Do not convert relationship-specific behavior into a global personality trait without cross-context evidence. Preserve differences between how a character behaves alone, with friends, with authority, under deployment pressure, and with a romantic attachment figure.

\#\#\# Conditional behavioral-policy extraction  
Once repeated or highly diagnostic cross-context evidence exists, the CHARACTER STATE ledger should also encode conditional response rules that can support prediction and simulation. These rules are not new personality labels; they are evidence-bounded mappings from perceived context to likely response.

Preferred policy schema:  
\`trigger/context\` / \`perceived state\` / \`active goals and aversions\` / \`relationship state\` / \`competing motives\` / \`likely action or speech tendency\` / \`modifiers or inhibitors\` / \`known exceptions\` / \`confidence\` / \`evidence\`.

Examples of the level of abstraction sought include whether concern for a particular person overrides ordinary compliance, whether emotional threat produces deflection before disclosure, or whether danger to self is appraised differently from danger to another person. Do not instantiate such rules from hypothetical examples; derive them only from the manga.

Distinguish:  
\- stable behavioral invariants;  
\- context-conditioned policies;  
\- relationship-conditioned policies;  
\- stress-induced departures from baseline;  
\- unresolved apparent contradictions.

A single striking response normally remains scene evidence. Promote it into a behavioral policy only when repetition, contrast, or strong diagnostic structure makes the rule falsifiable.

\#\# Ledger 2 — KIMISHINU\_RELATIONSHIP\_AND\_INTIMACY\_LEDGER.md

\#\#\# Responsibility  
Track dyadic and small-group relationship states, especially where intimacy materially changes agency, survival behavior, or self-conception.

\#\#\# Track  
\- trust;  
\- disclosure and concealment;  
\- reciprocity;  
\- dependency/interdependence;  
\- caretaking;  
\- jealousy/exclusivity;  
\- touch and bodily proximity;  
\- address-language changes;  
\- promises and future orientation;  
\- rupture and repair;  
\- asymmetry in knowledge, vulnerability, mortality, or power;  
\- whether attachment expands or constrains each person's available choices.

\#\#\# State principle  
A relationship transition requires evidence of changed expectations or behavior, not merely a visually intimate panel. Record ambiguous moments as OPEN rather than forcing progression.

\#\#\# Central analytical distinction  
Because explicit romance exists in the source, the ledger should not spend its energy proving romantic possibility. It should model what love does: how it reorganizes fear, duty, disclosure, return, self-worth, and imagined futurity.

\#\# Ledger 3 — KIMISHINU\_MORTALITY\_EXPENDABILITY\_AND\_PERSONHOOD\_LEDGER.md

\#\#\# Responsibility  
Track how the manga constructs death, survivability, injury, sacrifice, replaceability, and the treatment of children as usable military resources.

\#\#\# Track  
\- fear/acceptance of death;  
\- injury response;  
\- grief and mourning;  
\- normalization or dissociation;  
\- fatalism;  
\- survival motivation;  
\- return/homecoming expectations;  
\- institutional language of expendability;  
\- self-instrumentalization;  
\- treatment of others as replaceable or irreplaceable;  
\- immortality or anomalous survivability where source-established;  
\- personhood recognition versus weaponization;  
\- changes in the imagined possibility of a shared future.

\#\#\# Constraint  
Do not treat death-awareness as a single continuum. Differentiate terror, numbness, practical acceptance, ideological sacrifice, learned normalization, reckless self-use, and genuine indifference.

\#\# Ledger 4 — KIMISHINU\_INSTITUTION\_WAR\_CONSCIOUSNESS\_AND\_AGENCY\_LEDGER.md

\#\#\# Responsibility  
Track the school/military system as experienced and understood by the characters, and track individual agency inside that system.

\#\#\# Track  
\- what students know about the war;  
\- what remains hidden or taken for granted;  
\- training and deployment procedures;  
\- discipline and authority;  
\- peer normalization;  
\- duty language;  
\- rewards, sanctions, and expectations;  
\- child/orphan military utilization;  
\- resistance, refusal, negotiation, evasion, adaptation, normalization, endorsement;  
\- external options actually available to characters;  
\- differences between felt autonomy and structural autonomy;  
\- evidence of broader political/strategic context when the manga supplies it.

\#\#\# Political-analysis constraint  
Do not manufacture macro-politics from implication. If recurring evidence later establishes governments, ideologies, war aims, strategic factions, propaganda systems, or geopolitical history as major objects, this ledger may be split and a dedicated political-war ledger created. Until then, preserve the bottom-up institutional perspective.

\#\# Ledger 5 — KIMISHINU\_VISUAL\_AND\_DIALOGUE\_PATTERN\_LEDGER.md

\#\#\# Responsibility  
Preserve recurring formal evidence that supports character, relationship, and thematic reconstruction across volumes.

\#\#\# Japanese dialogue track  
Record recurring or diagnostic:  
\- pronouns;  
\- names/titles/address forms;  
\- politeness level;  
\- sentence endings;  
\- contractions;  
\- hesitation and ellipsis;  
\- repetition;  
\- blunt/softened commands;  
\- joking register;  
\- evasive phrasing;  
\- emotional departures from baseline.

The goal is usable speech modeling, not exhaustive transcription.


\#\#\# Generative voice constraints  
When evidence becomes sufficient, convert recurring dialogue observations into a compact generative voice model. Track:  
\- lexical preferences and recurrent wording;  
\- syntax and utterance shape, including fragments, sentence length, question frequency, and assertion strength;  
\- pragmatics: directness, request style, emotional explicitness, evasion, deflection, teasing, reassurance, and repair;  
\- relationship-conditioned register: how the same speaker changes with friends, authority, romantic attachment, strangers, or adversaries;  
\- stress transformations under fear, anger, jealousy, grief, shame, urgency, or combat pressure;  
\- negative constraints: formulations, registers, or kinds of self-disclosure the character strongly tends not to use;  
\- exceptions and uncertainty.

Negative constraints are especially valuable for simulation because an in-character response is defined partly by what the character would be unlikely to say even when the semantic content is correct. Preserve short Japanese examples only where they materially establish the rule; do not turn this ledger into an exhaustive transcript.

\#\#\# Visual track  
Record recurring or diagnostic:  
\- panel scale;  
\- page-turn reveals;  
\- gaze structures;  
\- bodily distance;  
\- touch motifs;  
\- framing/occlusion;  
\- negative space;  
\- repeated compositions;  
\- background suppression or environmental emphasis;  
\- screentone and visual silence;  
\- SFX integration;  
\- transitions between ordinary school/domestic life and warfare/death.

\#\#\# Pattern threshold  
A single striking image belongs in the volume deep reading. Promote it into this ledger only when it establishes a character-specific visual grammar, recurs, revises an earlier pattern, or is likely to matter for later synthesis.

\#\# Cross-ledger routing examples

A scene in which one character waits for another to return from deployment may update:  
\- CHARACTER STATE if it changes survival motivation or coping behavior;  
\- RELATIONSHIP if expectations of return or attachment are newly articulated;  
\- MORTALITY if death/return is reconceptualized;  
\- INSTITUTION if deployment rules or normalization are revealed;  
\- VISUAL/DIALOGUE if recurring language or composition becomes diagnostic.

Do not paste the same prose into all five. Each ledger receives only the state change relevant to its semantic responsibility.

\#\# Simulation causal model

For mature character reconstruction, preserve a causal distinction between latent state and observable output. The default modeling chain is:

\`beliefs + goals/aversions + emotional state + relationship state + perceived environment/options\`  
\`-> appraisal of the immediate situation\`  
\`-> decision / response selection\`  
\`-> observable speech and action\`  
\`-> post-action state update\`.

The ledgers contribute different parts of this chain: CHARACTER STATE supplies dispositions, motives, beliefs, coping, and dynamic internal state; RELATIONSHIP supplies target-specific expectations and attachment conditions; MORTALITY supplies survival/death valuation; INSTITUTION supplies perceived constraints and available options; VISUAL/DIALOGUE supplies observable expression and speech-form evidence.

Do not treat an observed action as transparent proof of one hidden motive. When several latent-state explanations remain compatible with the page, preserve competing hypotheses and identify what future evidence would discriminate among them.

Simulation-oriented synthesis should therefore distinguish at least:  
\- latent state variables;  
\- appraisal/decision rules;  
\- observable behavioral outputs;  
\- state-update consequences;  
\- uncertainty and alternative models.

\#\# Prospective character-model validation

The prospective-reading design should be used to test character models, not only thematic predictions. Once a character has enough repeated cross-context evidence to support falsifiable expectations, freeze a small set of diagnostic behavioral predictions before opening the next volume.

Possible prediction domains include:  
\- response to interpersonal conflict;  
\- disclosure versus concealment under emotional pressure;  
\- behavior toward authority when personal attachment conflicts with duty;  
\- response to danger, injury, deployment, or anticipated loss;  
\- likely changes in Japanese speech register under stress;  
\- whether an established relationship-conditioned behavior generalizes to a new but comparable circumstance.

At the next boundary, classify each prediction as \`supported\`, \`partially supported\`, \`not supported\`, or \`indeterminate\`, then route any model change through PRESERVE, STRENGTHEN, REVISE, DOWNGRADE, REJECT, or OPEN as appropriate.

Prediction failure is evidence about the adequacy of the model, not a defect in the source. Prefer a few discriminating predictions over numerous easy or plot-level guesses. Do not optimize for an accuracy percentage, and do not make a prediction merely because the architecture provides a slot for one.

The likely point at which this becomes useful may be around V03-V04 for central characters, but the trigger is evidentiary maturity rather than a fixed volume number. It may occur earlier, later, or not at all for secondary characters.

\#\# Simulation-ready character synthesis contract

When ledger density justifies a CHARACTER MONOGRAPH or specialist character synthesis, it should convert the accumulated evidence into a simulation-ready model rather than merely restating traits. When supported, include five layers:

1\. stable personality architecture — temperament, values, durable motives, recurrent defenses, moral intuitions, and strong invariants;  
2\. dynamic state variables — current fears, desires, beliefs, injuries, grief, attachment security, perceived options, and other mutable conditions;  
3\. relationship-conditioned behavior — target-specific expectations, trust, disclosure, dependency/interdependence, conflict, care, and register;  
4\. decision/response policies — conditional mappings from perceived situation and competing motives to likely action, including modifiers, exceptions, and confidence;  
5\. Japanese voice constraints — lexical, syntactic, pragmatic, relationship-conditioned, stress-conditioned, and negative speech rules.

Each simulation-ready synthesis should also state known failure modes, unresolved contradictions, low-evidence contexts, and out-of-distribution situations where confident prediction would be unwarranted. The objective is source-faithful conditional behavior, not a universal personality chatbot unconstrained by chronology or context.

\#\# No automatic sixth-ledger rule

Simulation hardening is initially embedded inside the five existing ledgers. Do not create a separate behavioral-policy or simulation ledger merely because these schemas exist. Split a new semantic responsibility only if accumulated evidence becomes dense enough that retrieval, maintenance, or independent synthesis materially benefits from it.

\#\# Confidence vocabulary

Use \`high\`, \`medium\`, or \`low\` confidence, supplemented by a short reason. Confidence measures evidentiary support, not emotional intensity or thematic importance.

\#\# Checkpoint triggers

A separate CHECKPOINT artifact is justified when:  
\- multiple ledgers undergo major revisions at one boundary;  
\- a major arc closes;  
\- a long sequence of volumes has accumulated enough state that retrieval becomes difficult;  
\- the project needs a prospective-model audit before continuing;  
\- accumulated character-policy predictions require calibration against observed outcomes.

Do not schedule checkpoints at arbitrary identical intervals merely for symmetry.

\#\# Specialist synthesis triggers

Potential specialist artifacts should emerge from ledger density. Likely but not guaranteed candidates include:  
\- simulation-ready character monographs for Sheena, Mimi, and other sufficiently evidenced characters;  
\- central relationship synthesis;  
\- institutional normalization / war-consciousness synthesis;  
\- mortality, expendability, and weaponized-personhood synthesis;  
\- manga visual grammar study.

No specialist title is pre-authorized merely by this list.

\#\# Initialization state

At project start all five ledgers are conceptually empty and the analytical boundary is PRE-V01. The actual Markdown ledger files should be instantiated during V01 integration so their first entries are source-grounded rather than template boilerplate.

\#\# Architecture evolution

If recurring evidence shows that one ledger has two analytically independent retrieval functions, split it deliberately and document the change in CURRENT\_STATE\_AND\_CORPUS\_MAP.md. Preserve old IDs/crosswalks where needed. Do not silently rename or move mature ledger responsibilities once later analysis depends on them.  
