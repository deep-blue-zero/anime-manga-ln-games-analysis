---
series: MHA
artifact_type: synthesis_architecture
scope: FULL_SERIES_V01-V42
generation: V2
status: canonical
source_boundary: Japanese manga Volumes 1-42; V2 sequential reread in progress
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
---

# My Hero Academia V2 — Series Architecture, Roadmap, and Character-Modeling Structure

## 1. Purpose

This document is the governing architecture for the Japanese-primary second-pass reread of 『僕のヒーローアカデミア』. It converts the existing volume-level analytical method into a cumulative series system capable of supporting both literary synthesis and evidence-grounded character reconstruction.

The architecture is designed around two simultaneous goals:

1. produce a definitive volume-by-volume reread and full-series synthesis; and
2. preserve enough longitudinal character evidence to reconstruct plausible speech, judgment, relationships, and behavior in novel situations without confusing simulation with canon.

The architecture does **not** treat character simulation as a replacement for literary analysis. Modeling is a downstream use of the same primary-source evidence.

## 2. Canonical roots

### Analytical root

Google Drive: `My Hero Academia` under the project analytical-artifact root.

Current V2 subtree: `V2 Analysis`.

### Primary-source root

Google Drive: `My Hero Academia` primary sources.

Current visible subfolders:

- `Main volumes`
- `Supplemental material`

The source inventory remains `active_provisional` while uploads are still in progress.

## 3. Authority precedence

Within MHA, use the following order:

1. this V2 architecture and the current V2 corpus map;
2. the amended V2 analytical method;
3. canonical V2 sequential volume readings and cumulative ledgers;
4. V2 specialist and full-series syntheses once created;
5. primary Japanese manga for direct verification;
6. V1 analysis only as `historical_legacy` and revision-comparison material.

V1 findings do not remain authoritative merely because they are earlier or more complete. They must survive V2 re-adjudication.

## 4. V2 Drive structure

```text
V2 Analysis/
├── 00 Frameworks and Methods/
│   ├── CURRENT_STATE_AND_CORPUS_MAP.md
│   ├── MHA_SP2_ANALYTICAL_METHOD_V2_1.md
│   ├── MHA_SP2_SYNTHESIS_ARCHITECTURE.md
│   └── MHA_SP2_CHARACTER_MODELING_SCHEMA.md
│
├── 01 Source Lock and Inventory/
│   └── MHA_SP2_SOURCE_INVENTORY.md
│
├── 02 Sequential Readings/
│   ├── MHA_SP2_V01_DEEP_READING.md
│   ├── MHA_SP2_V02_DEEP_READING.md
│   └── ... through V42
│
├── 03 Longitudinal Ledgers/
│   ├── Character Group Ledgers/
│   │   ├── MHA_SP2_CLASS_1A_CHARACTER_STATE_LEDGER.md
│   │   ├── MHA_SP2_UA_STUDENTS_STAFF_CHARACTER_STATE_LEDGER.md
│   │   ├── MHA_SP2_PRO_HERO_CHARACTER_STATE_LEDGER.md
│   │   ├── MHA_SP2_VILLAIN_ANTAGONIST_CHARACTER_STATE_LEDGER.md
│   │   └── MHA_SP2_FAMILY_CIVILIAN_SOCIAL_ACTOR_LEDGER.md
│   ├── MHA_SP2_RELATIONSHIP_STATE_LEDGER.md
│   ├── MHA_SP2_POWER_PHILOSOPHY_LEDGER.md
│   ├── MHA_SP2_HERO_SOCIETY_LEDGER.md
│   ├── MHA_SP2_RECOGNITION_FAILED_RESCUE_LEDGER.md
│   ├── MHA_SP2_VILLAIN_FORMATION_LEDGER.md
│   ├── MHA_SP2_JAPANESE_VOCABULARY_LEDGER.md
│   ├── MHA_SP2_VISUAL_MOTIF_LEDGER.md
│   ├── MHA_SP2_CALLBACK_PAYOFF_LEDGER.md
│   └── MHA_SP2_FIRST_PASS_CORRECTION_LEDGER.md
│
├── 04 Character Modeling and Reconstruction/
│   ├── MHA_SP2_CHARACTER_MODEL_READINESS_INDEX.md
│   └── future character model dossiers / scenario validation reports
│
├── 05 Specialist Synthesis/
│   └── subject-specific canonical syntheses after sufficient evidence accrues
│
├── 06 Full-Series Synthesis/
│   └── definitive post-V42 synthesis corpus
│
├── 07 Evidence and Indexes/
│   └── MHA_SP2_PRIMARY_SOURCE_LOCATOR.md and future crosswalks
│
└── 08 Audits and Manifests/
    └── source locks, corpus audits, manifests, checksums, handoffs
```

No empty categories should be created merely for symmetry. The folders above exist because each already has a planned analytical responsibility.

## 5. Why group-specific character ledgers are necessary

The existing method has a generic character trajectory ledger. That is adequate for thematic synthesis but insufficient for modeling a cast as large as MHA because it encourages only the most salient characters to be updated.

The group ledgers solve three problems:

- **coverage:** minor and secondary characters remain visible even when not central to the current volume;
- **retrieval:** a later model-building pass can retrieve all relevant characters from a social/institutional cohort without searching forty-two volume essays;
- **state continuity:** small behavioral or relational changes can accumulate without needing a standalone monograph.

The ledgers are organized by durable social role rather than moral importance.

### Class 1-A

All Class 1-A students. This is the densest and most frequently recurring cohort and warrants its own ledger.

### Other U.A. students and staff

Class 1-B, Big Three, General Studies, Support Course, teachers, administration, and other U.A.-embedded actors.

### Professional heroes and hero-system actors

Pro heroes, sidekicks, agency personnel, HPSC-linked actors, police when functioning within the hero system, and other adult professional hero infrastructure.

### Villains and antagonists

League of Villains, Meta Liberation Army, organized villain actors, vigilante/criminal antagonists, and other recurring hostile figures. This ledger records behavior without assuming villainy explains the whole person.

### Family, civilians, and other social actors

Parents, siblings, civilians, media figures, doctors, ordinary bystanders, and other non-hero/non-villain actors whose behavior materially shapes characters or the social system.

Characters may migrate in social role over time, but their canonical entry should remain in the ledger that best preserves longitudinal identity. Cross-links should record role changes rather than duplicating the full model.

## 6. Character-state record

Every materially updated character entry should preserve the following fields when evidence exists:

### Identity and role
- current public/social role;
- institutional memberships;
- hero/villain/student status;
- known aliases and naming preferences.

### Psychological state
- dominant desires;
- active fears;
- self-conception;
- shame/pride vulnerabilities;
- unresolved contradictions;
- current sources of confidence and insecurity.

### Values and power philosophy
- what power means to the character;
- what power permits;
- what power obligates;
- moral priorities;
- legitimacy beliefs;
- personhood/autonomy assumptions where textually supported.

### Perception and cognition
- what the character habitually notices;
- blind spots;
- analytical style;
- attribution habits;
- epistemic limits;
- common misreadings of other people.

### Decision behavior
- default decision heuristics;
- risk tolerance;
- action threshold;
- response to uncertainty;
- response to authority;
- response to helplessness;
- response to insult, fear, shame, praise, defeat, and responsibility.

### Social and relational behavior
- baseline sociability;
- hierarchy sensitivity;
- dominance/submission patterns;
- care/help behavior;
- conflict style;
- reconciliation style;
- relationship-specific exceptions.

### Stress and escalation
- low-stakes baseline;
- competitive stress;
- acute danger;
- injury/exhaustion;
- shame/humiliation;
- moral crisis;
- grief/loss;
- group-pressure behavior.

### Japanese voice and speech behavior
- pronouns;
- address terms;
- sentence endings;
- formality;
- contractions/slang;
- recurring phrases;
- insults/praise patterns;
- hesitation and silence;
- emotional register changes;
- relationship-specific speech differences.

### Embodiment and action
- habitual posture/gesture where textually meaningful;
- relationship to injury and bodily cost;
- quirk-specific bodily habits;
- fighting or rescue style;
- noncombat habits relevant to personality.

### Behavioral evidence
For every material modeling claim preserve:
- observed context;
- behavior or wording;
- source locator;
- evidence class;
- whether repeated or one-off;
- current confidence.

### Predictive note
Only after the above, optionally record:
- likely response in analogous situations;
- conditions that would change the prediction;
- confidence level;
- evidence used.

Predictive notes are never canon and must not be fed back into the observational fields as evidence.

## 7. Relationship state ledger

Character models cannot be reconstructed independently of relationships. The relationship ledger records directed pairs or small-group relations where behavior changes significantly by partner.

For each relation track:

- current relational definition;
- trust;
- affection;
- rivalry;
- fear;
- dependency;
- authority;
- resentment;
- idealization;
- protectiveness;
- communication style;
- recurring conflict;
- repair behavior;
- speech/register differences;
- major state transitions;
- asymmetries in how each person understands the relationship.

Examples from Volume 1 already requiring longitudinal tracking include:

- Midoriya → Bakugo;
- Bakugo → Midoriya;
- Midoriya ↔ All Might;
- Midoriya ↔ Uraraka;
- Midoriya ↔ Iida;
- Midoriya ↔ Inko;
- Midoriya ↔ Aizawa.

## 8. Model-readiness states

A character's reconstruction readiness must be explicit.

### `insufficient`
Too little direct evidence or too narrow a context range.

### `emerging`
Several consistent traits are visible, but behavior remains underdetermined outside observed contexts.

### `moderate`
Repeated evidence exists across multiple contexts and relationships; cautious novel-situation reconstruction is possible.

### `strong`
Extensive longitudinal behavior, speech, stress, and relationship evidence supports high-confidence reconstruction across ordinary and high-stakes contexts.

### `specialist_ready`
Strong model plus sufficiently rich language/relationship evidence for a standalone character dossier and formal scenario-validation tests.

Readiness is evidence coverage, not character importance.

## 9. Volume workflow amendment

After every future volume reading:

1. write the canonical volume deep reading;
2. update every group ledger for characters whose state materially changed;
3. add newly observed behavioral evidence even if the character did not undergo thematic development;
4. update relationship states;
5. update model-readiness ratings only when evidence breadth materially changes;
6. update thematic ledgers;
7. update source locators;
8. record first-pass claim transitions;
9. update `CURRENT_STATE_AND_CORPUS_MAP.md` only when project state materially changes.

A character appearing without new usable evidence does not require a synthetic update.

## 10. Phased roadmap

### Phase 0 — Framework and source lock
- establish V2 architecture;
- amend analytical method;
- establish modeling schema;
- create source inventory;
- initialize ledgers;
- seed Volume 1 evidence.

### Phase 1 — Sequential reread, Volumes 1–42
- one Japanese volume per pass;
- canonical deep-reading artifact per volume;
- cumulative character/model and thematic ledgers updated continuously.

### Phase 2 — Mid-series modeling checkpoints
At major structural boundaries, audit whether character models have enough context diversity. Suggested checkpoints:
- post-Sports Festival;
- post-Kamino;
- post-Overhaul;
- post-My Villain Academia;
- post-Paranormal Liberation War;
- post-Dark Deku;
- post-Final War / Volume 42.

These checkpoints should identify what kinds of situations remain missing for each important character rather than merely summarizing them.

### Phase 3 — Character reconstruction dossiers
After enough evidence accumulates, produce specialist dossiers for characters that reach `specialist_ready`.

Likely eventual candidates include Midoriya, Bakugo, All Might, Todoroki, Endeavor, Shigaraki/Tenko, AFO, Ochako, Toga, Iida, Aizawa, Hawks, Twice, Spinner, Dabi, and others as evidence warrants.

### Phase 4 — Validation probes
Test reconstruction quality using held-out canonical scenes or deliberately withheld later-volume material:

- predict likely behavior from the model using only evidence available before the held-out scene;
- compare prediction to canonical behavior;
- classify mismatch as missing state, wrong inference, context sensitivity, or genuine surprise;
- revise the model rather than rationalizing the miss.

This is the preferred method for measuring simulation rigor.

### Phase 5 — Specialist synthesis
Draft subject-specific documents from the mature ledgers and sequential readings.

### Phase 6 — Full-series synthesis
After Volume 42, produce the definitive multi-document synthesis with direct primary-source re-verification of load-bearing claims.

## 11. Separation of responsibilities

### Sequential volume readings answer
What does this volume do, and what evidence does it add?

### Group character ledgers answer
What do we currently know about each character as a changing person?

### Relationship ledger answers
How does behavior change by social partner and relational state?

### Thematic ledgers answer
How do recurring philosophical, social, visual, and linguistic structures evolve?

### Modeling dossiers answer
Given the accumulated evidence, what behavior/speech can be reconstructed, with what confidence and limits?

### Specialist syntheses answer
What is the strongest mature interpretation of a subject across the complete corpus?

These responsibilities should not be collapsed into near-duplicate documents.

## 12. Governing rule for simulation

The project should model **conditional behavioral tendencies**, not deterministic personalities.

A valid reconstruction states:

> Given this character state, relationship, knowledge, stakes, and social context, the best-supported response is X, with Y plausible alternatives and Z confidence.

An invalid reconstruction states:

> This character is the kind of person who always does X.

MHA repeatedly depicts growth, role conflict, hidden information, situational stress, and relationship-specific exceptions. A rigorous model must preserve that conditionality.

## 13. End-state deliverable

At the completion of Volume 42, the MHA V2 corpus should be able to support both:

- a source-grounded definitive literary/thematic synthesis; and
- evidence-auditable character reconstruction in novel scenarios.

The two outputs should share evidence infrastructure but remain epistemically distinct.
