---
series: GBC
artifact_type: synthesis_architecture
scope: E01-E13
media: TV_anime
language_priority: Japanese
analysis_generation: V2
status: canonical
source_boundary: "Girls Band Cry TV anime Episodes 1-13, episode audiovisual bundles, official episode audio/subtitles/frames available in the primary-source corpus, and V1 analysis used only as revision-target provenance"
supersedes: null
superseded_by: null
do_not_use_as_current_authority: false
created: 2026-08-17
updated: 2026-08-17
---

# Girls Band Cry — V2 Synthesis Architecture

## 1. Purpose

This document defines the canonical analytical architecture for a second-pass, primary-source-grounded reading of *Girls Band Cry*.

V2 has two simultaneous goals:

1. produce a stronger literary, thematic, audiovisual, musical, social, and character analysis of the thirteen-episode television series; and
2. produce enough structured evidence to reconstruct the major characters with high fidelity: their personalities, behavioral tendencies, interpersonal habits, manner of speaking, emotional regulation, worldviews, practical judgment, performance identities, and context-dependent changes in voice and conduct.

The second goal is not an optional appendix to the literary analysis. It changes what the sequential reread must record. A character monograph is successful only if a later reader can use it to predict how the character is likely to speak, react, decide, escalate, apologize, evade, comfort, perform, or misunderstand in a new but canon-compatible situation—and can identify the uncertainty boundaries of those predictions.

V2 therefore treats character reconstruction as an evidence problem rather than a freeform personality summary.

---

## 2. Governing question

The principal adversarial question for V2 is:

> Does the primary audiovisual text actually sustain the mature V1 interpretation when every episode is reread prospectively, with full-series hindsight available but not allowed to erase local ambiguity?

A second governing question applies specifically to character work:

> Can the corpus distinguish what a character believes, what she says she believes, what she habitually does, what she does only under stress, what she does for a particular person, and what later viewers merely project onto her?

This distinction is essential for Nina, Momoka, Subaru, Tomo, Rupa, Hina, and the surrounding ensemble because *Girls Band Cry* repeatedly stages conflict between declared principle, practical behavior, self-concept, social performance, and emotional need.

---

## 3. Canonical root and authority model

The existing Girls Band Cry analytical Drive folder remains the single canonical root. V2 does not create a parallel project root.

The legacy V1 corpus remains preserved in place until an explicit migration is justified. V1 episode files and the V1 full-series synthesis are `historical_legacy` revision targets, not current V2 authority.

The active first-read file for the project is:

`CURRENT_STATE_AND_CORPUS_MAP.md`

Authority precedence during V2 is:

1. current V2 corpus map and governing method;
2. current V2 specialist/full-series synthesis within its declared source boundary;
3. current V2 sequential readings and checkpoints;
4. current V2 evidence, locator, and revision ledgers;
5. original Japanese audiovisual primary source;
6. V1 analytical material as historical provenance or revision target.

When exact dialogue, acting, musical, visual, or scene claims matter, the original source overrides any synthesis.

---

## 4. Planned directory architecture

Directories should be created when they acquire actual contents. Empty folders should not be created merely for symmetry.

```text
Girls Band Cry/
|
|-- CURRENT_STATE_AND_CORPUS_MAP.md
|
|-- 00 Frameworks and Methods/
|   |-- GBC_ANALYTICAL_METHOD_V2.md
|   `-- GBC_SYNTHESIS_ARCHITECTURE_V2.md
|
|-- 01 Source Lock and Inventory/
|   |-- GBC_SOURCE_INVENTORY.md
|   |-- GBC_SOURCE_LOCK.md
|   `-- GBC_V1_BASELINE_AND_REVISION_TARGETS.md
|
|-- 02 Sequential Readings/
|   |-- GBC_E01_DEEP_READING.md
|   |-- GBC_E02_DEEP_READING.md
|   |-- ...
|   |-- GBC_E13_DEEP_READING.md
|   |-- GBC_E01-E04_CHECKPOINT.md
|   |-- GBC_E05-E08_CHECKPOINT.md
|   |-- GBC_E09-E11_CHECKPOINT.md
|   `-- GBC_E12-E13_CHECKPOINT.md
|
|-- 03 Longitudinal Ledgers/
|   |-- GBC_CHARACTER_STATE_AND_VOICE_LEDGER.md
|   |-- GBC_BEHAVIORAL_RECONSTRUCTION_LEDGER.md
|   |-- GBC_RELATIONSHIP_LEDGER.md
|   |-- GBC_MUSIC_PERFORMANCE_AND_AUTHORSHIP_LEDGER.md
|   |-- GBC_VISUAL_FORM_AND_DIRECTION_LEDGER.md
|   |-- GBC_INDUSTRY_LABOR_AND_AUTONOMY_LEDGER.md
|   `-- GBC_V1_TO_V2_CLAIM_REVISION_LEDGER.md
|
|-- 04 Specialist Synthesis/
|   |-- GBC_NINA_CHARACTER_MONOGRAPH.md
|   |-- GBC_MOMOKA_CHARACTER_MONOGRAPH.md
|   |-- GBC_SUBARU_CHARACTER_MONOGRAPH.md
|   |-- GBC_TOMO_CHARACTER_MONOGRAPH.md
|   |-- GBC_RUPA_CHARACTER_MONOGRAPH.md
|   |-- GBC_HINA_CHARACTER_MONOGRAPH.md
|   |-- GBC_TOGENASHI_TOGEARI_ENSEMBLE_SYNTHESIS.md
|   |-- GBC_DIAMOND_DUST_ENSEMBLE_SYNTHESIS.md
|   |-- GBC_NINA_MOMOKA_RELATIONSHIP_SYNTHESIS.md
|   |-- GBC_NINA_HINA_RELATIONSHIP_SYNTHESIS.md
|   |-- GBC_JAPANESE_VOICE_SPEECH_AND_VOCAL_PERFORMANCE.md
|   |-- GBC_MUSIC_PERFORMANCE_AND_COLLECTIVE_AUTHORSHIP.md
|   |-- GBC_VISUAL_DIRECTION_CG_ACTING_AND_PERFORMANCE_FORM.md
|   `-- GBC_INDUSTRY_LABOR_ARTISTIC_AUTONOMY_AND_FAILURE.md
|
|-- 05 Full-Series Synthesis/
|   `-- GBC_FULL_SERIES_SYNTHESIS_V2.md
|
|-- 06 Evidence and Indexes/
|   |-- GBC_PRIMARY_SOURCE_LOCATOR_INDEX.md
|   |-- GBC_JAPANESE_KEY_LINE_AND_TERMINOLOGY_INDEX.md
|   |-- GBC_CHARACTER_RECONSTRUCTION_EVIDENCE_MATRIX.md
|   |-- GBC_V1_V2_CROSSWALK.md
|   `-- GBC_ENDING_EPILOGUE_AV_ANALYSIS.md
|
|-- 08 Audits and Manifests/
|   |-- GBC_CHARACTER_MODEL_VALIDATION_AUDIT.md
|   |-- GBC_V2_FINAL_AUDIT.md
|   `-- GBC_V2_MANIFEST.md
|
`-- 90 Legacy and Superseded/
    `-- V1/    # create only if/when an explicit legacy migration is performed
```

The architecture is intentionally proportional to a thirteen-episode anime. It is more structured than V1 because audiovisual form and character reconstruction require cumulative evidence, but it does not import the scale of much larger novel or game projects.

---

## 5. Phase structure

### Phase 0 — Source lock, V1 baseline, and method stabilization

Required outputs:

- `GBC_SOURCE_INVENTORY.md`
- `GBC_SOURCE_LOCK.md`
- `GBC_V1_BASELINE_AND_REVISION_TARGETS.md`

Tasks:

- verify exactly which episode bundles, audio tracks, subtitle tracks, screenshots, contact sheets, clips, songs, and other primary-source assets are accessible;
- define the primary Japanese text/audio track and locator scheme;
- enumerate important V1 theses as claim IDs;
- flag the known Episode 13 V1 archival gap;
- establish which supplemental materials are inside or outside the V2 source boundary.

V1 is not reread as authority. It is converted into hypotheses to test.

### Phase 1 — Sequential reread

Analyze Episodes 1–13 in order using `GBC_ANALYTICAL_METHOD_V2.md`.

Each reading must generate both literary analysis and cumulative character-model evidence. Later knowledge may be used only in a separately marked retrospective layer.

Episode analyses should normally be created in the following sequence:

- E01
- E02
- E03
- E04
- checkpoint E01–E04
- E05
- E06
- E07
- E08
- checkpoint E05–E08
- E09
- E10
- E11
- checkpoint E09–E11
- E12
- E13
- checkpoint E12–E13

The Episode 13 V2 reading is especially important because there is no recoverable main V1 episode deep-dive response in the available transcript export. It should be treated as a fresh primary-source analysis rather than an attempt to reverse-engineer missing V1 prose.

### Phase 2 — Longitudinal ledgers

Ledgers are updated throughout Phase 1 rather than written only at the end.

They separate recurring evidence from the prose argument of any one episode.

### Phase 3 — Character monographs and specialist syntheses

After sequential reading and checkpoints stabilize, produce individual reconstructive monographs for:

- Iseri Nina;
- Kawaragi Momoka;
- Awa Subaru;
- Ebizuka Tomo;
- Rupa;
- Hina.

The core five must not be collapsed into an ensemble-only treatment. The ensemble synthesis asks how the band functions as a system; the monographs ask what each person is like and how reliably that person can be reconstructed.

Hina receives her own monograph because V2 must resist treating her solely as an instrument of Nina's psychology. Diamond Dust also receives a group synthesis so Hina's individual psychology can be distinguished from institutional and band-level pressures.

### Phase 4 — Cross-domain specialist synthesis

Produce the relationship, voice, music, visual-form, and industry/labor syntheses after the monographs can constrain them.

### Phase 5 — Full-series synthesis

`GBC_FULL_SERIES_SYNTHESIS_V2.md` integrates the mature findings without replacing the specialist artifacts.

### Phase 6 — Validation, audit, and release

The final audit tests whether mature claims can be routed to evidence and whether character reconstruction has overfit memorable scenes.

---

## 6. Longitudinal evidence architecture

### 6.1 `GBC_CHARACTER_STATE_AND_VOICE_LEDGER.md`

Tracks observable state and speech changes by episode.

Minimum dimensions:

- character;
- scene locator;
- interlocutor;
- immediate objective;
- emotional state;
- Japanese wording;
- pronouns and address forms;
- politeness/register;
- sentence endings and characteristic constructions;
- dialect/regional features;
- lexical preferences;
- ellipsis, hesitation, interruption, repetition;
- profanity/insult/teasing/affection style;
- audio delivery;
- embodied behavior;
- context-specific voice change;
- interpretation confidence;
- cumulative significance.

This ledger records what happens. It should not prematurely turn every observation into a personality law.

### 6.2 `GBC_BEHAVIORAL_RECONSTRUCTION_LEDGER.md`

This is the principal bridge from episode evidence to later character-modeling.

Each row should represent a candidate behavioral rule or decision tendency, for example:

> When Nina experiences accommodation as a demand to invalidate a prior injury, she tends to escalate from issue-specific disagreement to a broader moral or identity claim.

Each candidate rule must record:

- rule ID;
- character;
- trigger/context;
- observed behavior;
- apparent goal;
- apparent fear or avoided state;
- relationship dependency;
- supporting episodes/scenes;
- counterexamples;
- exception conditions;
- confidence;
- current formulation;
- status: provisional / stabilized / rejected.

The ledger must preserve counterexamples. A rule with no recorded falsification conditions is not yet a useful reconstruction rule.

### 6.3 `GBC_RELATIONSHIP_LEDGER.md`

Tracks how behavior changes by partner rather than assuming a character has one universal social style.

Important pairs include at minimum:

- Nina ↔ Momoka;
- Nina ↔ Subaru;
- Nina ↔ Tomo;
- Nina ↔ Rupa;
- Nina ↔ Hina;
- Momoka ↔ Subaru;
- Momoka ↔ Tomo;
- Momoka ↔ Rupa;
- Tomo ↔ Rupa;
- Subaru ↔ Tomo;
- core five ↔ family members;
- core five ↔ Miura / industry personnel;
- Hina ↔ Diamond Dust.

The ledger should track trust, fear, authority, teasing, dependence, conflict, repair, disclosure, concealment, physical comfort, role expectations, and speech/register changes.

### 6.4 `GBC_MUSIC_PERFORMANCE_AND_AUTHORSHIP_LEDGER.md`

Tracks how personal conflict becomes musical form.

Dimensions:

- composition/arrangement decisions;
- instrumental role;
- lyrical authorship;
- rehearsal conflict;
- performance behavior;
- song reuse/recontextualization;
- vocal interpretation;
- musical response between members;
- professional vs independent constraints;
- whether music resolves, translates, amplifies, or preserves conflict.

### 6.5 `GBC_VISUAL_FORM_AND_DIRECTION_LEDGER.md`

Tracks recurring formal grammar:

- blocking;
- gaze;
- proximity;
- thresholds;
- screens/phones;
- body language;
- camera motion;
- cutting rhythm;
- lighting/color;
- transitions between ordinary and performance space;
- CG acting specificity;
- abstract or subjective visual passages;
- recurrent objects and spatial motifs.

### 6.6 `GBC_INDUSTRY_LABOR_AND_AUTONOMY_LEDGER.md`

Tracks ticket quotas, rent, school, jobs, labels, venues, recording, promotion, agencies, professionalization, travel, equipment, logistics, and the material price of artistic choices.

This ledger prevents the autonomy theme from becoming purely psychological.

### 6.7 `GBC_V1_TO_V2_CLAIM_REVISION_LEDGER.md`

Every important V1 claim should transition through one of:

**PRESERVE · STRENGTHEN · REVISE · DOWNGRADE · REJECT · OPEN**

Preferred schema:

| Claim ID | V1 formulation | Status | V2 formulation | Evidence route | Notes |
|---|---|---|---|---|---|

---

## 7. Character monograph standard

Every individual character monograph must be capable of functioning as both a literary study and a constrained reconstruction model.

The monograph is not complete if it only explains the character's arc, themes, trauma, or philosophy.

### 7.1 Required section: identity and narrative function

Establish:

- social and narrative role;
- material circumstances;
- history relevant to present behavior;
- self-concept;
- how other characters perceive the person;
- difference between public image and private behavior.

### 7.2 Required section: core motivational system

Distinguish:

- primary wants;
- primary fears;
- wounds or unresolved losses;
- desired forms of recognition;
- shame triggers;
- attachment needs;
- autonomy needs;
- competence needs;
- identity-protective commitments.

Avoid reducing every action to trauma. A motivation is useful only when supported across contexts.

### 7.3 Required section: worldview and practical philosophy

Map what the character appears to believe about:

- truth and lying;
- fairness and wrongdoing;
- victory and defeat;
- regret;
- responsibility;
- compromise;
- artistic integrity;
- work and professionalism;
- family obligation;
- friendship;
- love/intimacy;
- dependence;
- forgiveness;
- success and failure;
- whether people can change;
- what makes a life choice worth defending.

For each proposition, distinguish:

- explicitly stated belief;
- repeated behavior consistent with belief;
- behavior contradicting stated belief;
- belief inferred only from one scene;
- unresolved contradiction.

### 7.4 Required section: cognitive and interpretive style

Record recurring tendencies such as:

- literal vs contextual interpretation;
- tendency to moralize practical disputes;
- sensitivity to hypocrisy;
- tendency to infer abandonment;
- strategic foresight;
- capacity to hold ambiguity;
- use of humor;
- suspicion of authority;
- self-blame;
- externalization;
- projection;
- reading of social atmosphere;
- comfort with indirectness;
- capacity for perspective-taking.

This section must include failure modes and not merely strengths.

### 7.5 Required section: affective regulation and escalation model

Describe:

- baseline affect;
- early signs of discomfort;
- anger escalation;
- shame response;
- grief response;
- fear response;
- embarrassment;
- jealousy or possessiveness when supported;
- intoxication effects where relevant;
- crying patterns;
- withdrawal vs confrontation;
- repair after conflict;
- how quickly the character returns to baseline;
- whether behavior changes when alone.

The monograph should identify a likely escalation sequence when evidence permits.

### 7.6 Required section: behavioral policy by context

Model probable behavior in contexts such as:

- being criticized;
- receiving praise;
- being wrong;
- believing someone else is wrong;
- being excluded;
- being asked for help;
- asking for help;
- financial pressure;
- authority pressure;
- family pressure;
- romantic/intimate ambiguity;
- band disagreement;
- performance stress;
- public failure;
- private failure;
- success;
- apology;
- reconciliation;
- encountering a stranger;
- protecting a friend;
- having to choose between principle and practicality.

Every behavioral policy should cite evidence and exception conditions.

### 7.7 Required section: interpersonal models

A character's behavior must be reconstructed relationally.

For each important partner, record:

- default register;
- power/authority assumptions;
- trust level;
- what the character wants from the partner;
- what the character fears from the partner;
- teasing and affection style;
- conflict triggers;
- physical-distance/touch norms;
- disclosure thresholds;
- repair behavior;
- ways the partner uniquely changes the character's voice or behavior.

A Nina-to-Momoka model, for example, cannot be assumed to generalize to Nina-to-Subaru or Nina-to-family.

### 7.8 Required section: Japanese speech model

The speech section must be detailed enough to support plausible line generation without flattening the character into catchphrases.

Track:

- first-person pronouns;
- second-person/reference strategies;
- names, surnames, given names, honorifics, nicknames;
- politeness level;
- plain/polite switching;
- sentence-final particles;
- gendered or regionally marked language where actually present;
- Kyushu/Kumamoto leakage where relevant;
- contractions;
- clipped vs expanded syntax;
- preferred intensifiers;
- recurring evaluative vocabulary;
- repetition;
- ellipsis;
- false starts;
- rhetorical questions;
- imperatives;
- apology forms;
- gratitude forms;
- insults;
- teasing;
- affectionate softness;
- professional vocabulary;
- music vocabulary;
- intoxicated speech where relevant;
- listener-specific register change;
- stress-specific register change.

Japanese quotations should be accompanied by locators and concise explanation of why the wording matters.

### 7.9 Required section: vocal-performance model

Speech text alone is insufficient for an audiovisual work.

Record qualitative vocal behaviors such as:

- pitch range and pitch shifts;
- loudness;
- tempo;
- rhythm;
- breathiness;
- tension/compression;
- hesitation;
- laughter;
- crying;
- muttering;
- shouting;
- swallowed words;
- overlap/interruption;
- changes under embarrassment, anger, grief, alcohol, intimacy, or performance.

Descriptions should remain qualitative unless reliable acoustic measurements are actually available.

### 7.10 Required section: embodied behavior

Track recurring physical signatures:

- posture;
- gaze;
- use of hands;
- pacing;
- flinching;
- stillness;
- touch initiation/avoidance;
- personal-space behavior;
- eating/drinking habits where relevant;
- instrument handling;
- rehearsal conduct;
- performance stance;
- body-language differences across partners.

### 7.11 Required section: music/performance identity

For band members, characterize:

- relationship to instrument/voice;
- rehearsal habits;
- response to criticism;
- live-performance state;
- authorship preferences;
- aesthetic values;
- how musical behavior differs from ordinary conversation;
- what the character can express in music that she cannot express directly.

### 7.12 Required section: contradiction map

A high-fidelity character model should preserve contradictions rather than smoothing them away.

Examples of useful contradiction forms:

- values honesty but uses performance strategically;
- rejects compromise but learns tactical compromise;
- protects others by making unilateral decisions;
- demands recognition while resisting dependence;
- seeks closeness but experiences closeness as vulnerability or control.

For each contradiction, specify whether it is:

- stable personality structure;
- developmental tension;
- context-specific exception;
- unresolved ambiguity;
- apparent contradiction produced by different relationship contexts.

### 7.13 Required section: negative model / boundary conditions

Record what the character is unlikely to do.

This is critical for reconstruction fidelity.

Examples:

- forms of cruelty not supported by the text;
- levels of emotional transparency that would be out of character;
- speech registers the character does not use;
- kinds of authority the character would normally accept or reject;
- behaviors requiring circumstances absent from canon.

### 7.14 Required section: scenario prediction tests

Each monograph should conclude with several hypothetical but canon-compatible situations designed to test the model.

For each scenario:

1. predict likely first reaction;
2. predict likely wording/register;
3. predict likely embodied behavior;
4. identify what would make the reaction escalate or de-escalate;
5. give confidence;
6. cite the canonical patterns supporting the prediction;
7. identify plausible alternative reactions.

These are validation exercises, not new canon.

### 7.15 Required section: reconstruction confidence

Assign confidence separately for domains:

- personality structure;
- everyday behavior;
- stress behavior;
- worldview;
- speech/register;
- vocal performance;
- physical mannerisms;
- intimate/relationship behavior;
- professional behavior;
- unseen-situation prediction.

A sparse character like Rupa may have high confidence in observed speech style but lower confidence in private behavior outside the contexts shown. The monograph must state that asymmetry explicitly rather than filling it with plausible invention.

---

## 8. Character-model evidence classes

Every reconstructive assertion should be tagged mentally or explicitly as one of the following:

### A — Direct recurrent evidence

Observed repeatedly across multiple scenes or episodes.

### B — Direct local evidence

Clearly observed, but only in a narrow context.

### C — Strong relational inference

Not stated directly, but supported by recurring behavior toward a particular person or situation.

### D — Interpretive hypothesis

Plausible and analytically useful, but underdetermined.

### E — Unsupported / do not model

An attractive inference for which the corpus does not provide enough warrant.

The final monographs should lean heavily on A–C and label D explicitly. E should be excluded from the model except as a warning about a common overreading.

---

## 9. Episode checkpoint responsibilities

### `GBC_E01-E04_CHECKPOINT.md`

Focus:

- Nina/Momoka formation;
- refusal and correctness;
- Nina's politeness/anger/dialect shifts;
- Momoka's roughness/care/avoidance;
- Subaru's performed social competence;
- early reconstruction rules and their counterexamples.

### `GBC_E05-E08_CHECKPOINT.md`

Focus:

- Diamond Dust and compromise;
- Hina's arrival as independent subject, not only Nina's trigger;
- professional vs independent models;
- five-member formation;
- Nina/Momoka projection rupture;
- confession/intimacy coding with evidentiary restraint;
- Rupa/Tomo initial reconstruction confidence limits.

### `GBC_E09-E11_CHECKPOINT.md`

Focus:

- Tomo criticism and family material;
- Nina family recontextualization;
- Rupa's grief, racism, maturity, and sparse-speech caution;
- Subaru's affirmative musicianship;
- collective authorship;
- the degree to which “conflict becomes composition” is formally and musically demonstrated.

### `GBC_E12-E13_CHECKPOINT.md`

Focus:

- professionalization and market response;
- Miura;
- Hina and Diamond Dust as competing but legitimate survival strategies;
- failure;
- independent continuation;
- ED/epilogue literal vs symbolic status;
- final character-model deltas.

---

## 10. Principal V1 claims to test

V2 should begin by formalizing, not automatically accepting, claims including:

- conflict becomes composition;
- Nina's worth does not depend on being correct in every judgment;
- correctness and non-regret are distinct;
- Diamond Dust's alternative is not morally illegitimate merely because Nina rejects it;
- Momoka's protection of others is partly entangled with fear, guilt, and self-erasure;
- Subaru's social performance is often intelligence and mediation rather than simple falseness;
- Tomo's psychology was under-modeled before later family evidence was recognized;
- Rupa is vulnerable to over-inference because her speech is sparse and her composure is easy to romanticize;
- the Nina/Momoka relationship is strongly yuri/romance-coded but must be analyzed with greater precision than a binary “canon couple/not couple” frame;
- Hina requires independent psychology;
- the show's industry analysis is more complex than authenticity versus sellout;
- Episode 11 marks the strongest emergence of five-person authorship;
- the ending/ED contains both likely literal epilogue information and symbolic visual narration.

---

## 11. Specialist synthesis responsibilities

### Individual character monographs

These own mature reconstruction of personality, behavior, voice, worldview, relationship-specific conduct, and uncertainty boundaries.

### `GBC_TOGENASHI_TOGEARI_ENSEMBLE_SYNTHESIS.md`

Owns the band as a system:

- role differentiation;
- conflict ecology;
- decision structure;
- informal leadership;
- care labor;
- criticism;
- dependency;
- authorship;
- how five incompatible temperaments become productive without becoming homogeneous.

It must not replace individual monographs.

### `GBC_DIAMOND_DUST_ENSEMBLE_SYNTHESIS.md`

Owns Diamond Dust as artistic institution, peer group, and competing survival strategy.

### `GBC_NINA_MOMOKA_RELATIONSHIP_SYNTHESIS.md`

Owns the dyad's projection, admiration, dependence, anger, intimacy, asymmetry, mutual rescue, recognition, and romance/yuri coding.

### `GBC_NINA_HINA_RELATIONSHIP_SYNTHESIS.md`

Owns their shared history, competing interpretations of injury and compromise, recognition, rivalry, and the limits of Nina's perspective on Hina.

### `GBC_JAPANESE_VOICE_SPEECH_AND_VOCAL_PERFORMANCE.md`

Owns cross-character comparison of linguistic and acoustic characterization.

### `GBC_MUSIC_PERFORMANCE_AND_COLLECTIVE_AUTHORSHIP.md`

Owns the musical proof for claims about conflict, authorship, artistic identity, performance, song reuse, and band formation.

### `GBC_VISUAL_DIRECTION_CG_ACTING_AND_PERFORMANCE_FORM.md`

Owns formal analysis of CG acting, camera, blocking, editing, space, color, performance visualization, and embodied characterization.

### `GBC_INDUSTRY_LABOR_ARTISTIC_AUTONOMY_AND_FAILURE.md`

Owns material conditions and competing models of professional survival.

---

## 12. Full-series synthesis constraints

The V2 full-series synthesis should answer:

- What is *Girls Band Cry* ultimately about?
- How do its central themes develop rather than merely recur?
- What does it believe about correctness, injury, regret, compromise, recognition, friendship, art, labor, and failure?
- How does the band become an artistic collective?
- What does each major character contribute that no other member could substitute?
- What does the audiovisual form do that a plot summary cannot capture?
- Which V1 conclusions survived, changed, weakened, or failed?

The full-series synthesis should point outward to monographs and ledgers rather than duplicate them wholesale.

---

## 13. Character reconstruction validation audit

`GBC_CHARACTER_MODEL_VALIDATION_AUDIT.md` should test the monographs before final release.

Required checks:

1. **Scene holdout test** — reserve several scenes from direct monograph construction and ask whether the mature model predicts the observed response.
2. **Relationship transfer test** — verify that behavior toward one partner was not incorrectly generalized to another.
3. **Stress-state test** — distinguish ordinary behavior from crisis behavior.
4. **Speech test** — compare generated paraphrase-level likely lines against actual Japanese register without copying canon dialogue.
5. **Negative-boundary test** — identify plausible fanon behaviors the model should reject.
6. **Counterexample test** — require each strong behavioral rule to survive known exceptions or be narrowed.
7. **Sparse-evidence test** — especially for Rupa, Hina, and secondary Diamond Dust members, ensure missing evidence remains missing rather than being filled with genre archetype.
8. **Literary-model consistency test** — confirm that the reconstruction model does not contradict the character's documented development.

The audit should grade model confidence by domain rather than issue one global “accurate/inaccurate” judgment.

---

## 14. Retrieval model after V2 completion

For future questions, preferred routing should be:

- character personality / speech / worldview / likely behavior → individual character monograph;
- relationship-specific behavior → relationship synthesis + relationship ledger;
- exact Japanese wording → key-line index → primary subtitle/audio source;
- exact physical acting → visual ledger → frame/video source;
- musical authorship or performance claim → music ledger/synthesis → audio/video source;
- episode-local truth → episode deep reading;
- changed interpretation → V1-to-V2 revision ledger;
- overall thematic conclusion → full-series synthesis.

This enables later use of the corpus for comparative analysis and character modeling without forcing every question back through the entire raw audiovisual source.

---

## 15. Governing architectural principle

The V2 corpus should preserve a distinction between four things that V1 sometimes allowed to bleed into one another:

1. what the character says;
2. what the character does;
3. what the work structurally implies about the character;
4. what an analyst predicts the character would do next.

The first three can establish a model. The fourth must always remain a model output, not retroactively become evidence.

That boundary is what makes a reconstructive monograph analytically useful rather than merely persuasive fan characterization.
