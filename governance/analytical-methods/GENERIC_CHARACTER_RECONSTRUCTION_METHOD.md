---
title: Generic Character Reconstruction Method
artifact_id: GENERIC_CHARACTER_RECONSTRUCTION_METHOD
artifact_type: generic_character_reconstruction_method_reference
artifact_role: reusable_corpus_level_analytical_reference_method
version: "1.0"
status: canonical
scope: source-bounded, time-indexed character modeling and validation in any medium, and new-project reconstruction bootstrap
authority_scope: this_reusable_reference_only
adoption: opt_in
project_local_authority: false
created: 2026-10-24
maintainer: Claude + user
source_boundary: "Methodological reference only; no series findings or primary-source evidence"
do_not_use_as_current_authority: false
do_not_use_as_literary_evidence: true
canonical_home: governance/analytical-methods/GENERIC_CHARACTER_RECONSTRUCTION_METHOD.md
drafted_against_commit: 6a3afaaf1bb61e0993db379ab4074c46e9ea98dd
supersedes: []
superseded_by: []
---

# Generic Character Reconstruction Method

## Adoption and authority boundary

This artifact is a reusable, corpus-level reference for building and validating character models from a project's source-grounded analysis. It is canonical only for this reference responsibility, and adoption is opt-in. It is not a repository policy, a project-local method, a capability assessment, or literary evidence.

1. A project adapts it into its own reconstruction method or specification, named in its synthesis architecture (initiation Section 5.5). Mature projects keep their existing reconstruction methods.
2. **It never grades capability.** Overall tiers, dimension grades, and scenario readiness are assigned only by the reconstruction evaluator, in `characters/reconstruction_capabilities.jsonl`, under [its maintenance policy](../policies/CHARACTER_RECONSTRUCTION_MAINTENANCE.md) and [specification](../../characters/RECONSTRUCTION_CAPABILITY_SPEC.md). A project's model may describe what its evidence covers and lacks; it must not self-assign an A–E tier.
3. It does not create discovery rows. The discovery agent curates which artifacts become evidence items (`characters/registry.jsonl`).
4. Modules for a medium apply only to projects in that medium.

## 0. Purpose

A character model reconstructs what a character is likely to perceive, value, say, avoid, or do under specified conditions, at a specified point in the story, from evidence that can be traced and tested.

The governing principle is:

> **A character model is an auditable, time-indexed, probabilistic reconstruction from source evidence: it predicts conditionally, names its exceptions, says where its evidence ends, and is never itself evidence.**

The goal is not deterministic role-play. A model that produces fluent, plausible output but cannot say which source behavior grounds a prediction has failed, however convincing it sounds.

---

# I. Boundaries

## 1. Reconstruction is derived use

Reconstruction routes to the project's literary corpus: its readings, ledgers, and monographs. It is not a parallel canon and not the master interpretive layer. Where the model and the literary analysis disagree, the disagreement is resolved in the literary corpus through claim revision, and the model follows.

**The synthetic-output firewall.** Generated dialogue, simulated scenes, and model predictions are never evidence about the character. They may be tested against the source; they may not be cited as source.

## 2. Subject and state scope

Every model binds:

- the analysis subject, matching a discovery subject where one exists (continuity, incarnation, state);
- the source boundary and the temporal boundary;
- the state the model represents, written `Character@Unit` (for example, `Character@V05` or `Character@S2E08`);
- the evidence excluded and why.

A character at the start of a work and the same character at its end are different models. Later knowledge may not explain an earlier state (sequential seal). A model of a late state may use earlier evidence as history, labeled as such.

## 3. Artifact split

Per subject and state, keep three artifacts separate:

| Artifact | Responsibility |
|---|---|
| **Evidence ledger** | Retrieval map of the observations that ground the model: locators, situation, interlocutor, state at the time, evidence class. Not a copy of the readings |
| **Operational model** | The structure in Part III: dispositions, states, rules, voice, conditioning, limits |
| **Monograph** (optional) | Literary interpretation of the character. A monograph does not certify a model |

Validation records (Part V) attach to the model they test.

---

# II. Evidence

## 4. Evidence classes

Projects may keep their own vocabularies. A generic set:

| Class | Meaning |
|---|---|
| `DS` | Direct speech by the character |
| `DB` | Directly presented behavior: an action shown or narrated as occurring |
| `NI` | Narrated interiority: thought, perception, or feeling given by a narrator or focalizing character |
| `RB` | Behavior or traits reported by another character |
| `OS` | Observer, institutional, or role statements about the character |
| `PF` | Performance evidence: voice and body in audiovisual sources, under the inspection-lane rules |
| `INF` | Inference from multiple observations |

Each observation in the evidence ledger records its locator, the situation type (ordinary or crisis), the interlocutor or audience, the character's state at the time, and the source-language status of any quoted speech.

## 5. Interiority access

State, per character and medium, how the source gives access to the inner life:

- what the character says;
- what the character does;
- what a narrator or focalizer says about the character;
- what other characters say about the character.

These are different evidence routes, not one. A first-person narrator's self-report is viewpoint-bound evidence. A character's report of another's motive is evidence of that belief. Where the source gives no interior access, the model reconstructs inner states only as labeled inference.

## 6. Ordinary-life control sample

Crisis scenes are over-represented in memorable evidence. Wherever the source shows ordinary life (meals, routine, idle talk, play, work), sample it deliberately. A model built only from crises predicts every situation as a crisis. Record when the source offers no ordinary-life evidence; that is a limit.

## 7. Source-language authority for voice

Voice and register are reconstructed from the source language. Translation is a navigation aid, not voice authority. A voice model built from translated summaries is a model of the translation.

## 8. Negative evidence requires opportunity

Absence of a behavior counts as evidence only where the situation gave the character a real opportunity to show it. Otherwise it is a gap. Keep the two apart:

- **evidence-backed limitation**: the source affirmatively shows the character does not, cannot, or would not;
- **evidence gap**: the source never tests it.

---

# III. Model structure

## 9. Header

```yaml
subject: <name and discovery subject ID if curated, else null>
state: <Character@Unit>
continuity: <continuity, witness, or route>
source_boundary: <units admitted>
temporal_boundary: <earliest and latest units used>
basis_commit: <full commit the evidence was read at>
model_version: <version>
inspection_lanes: [<lanes whose evidence was used>]
excluded_evidence: <what was left out and why>
```

## 10. Layers

**Stable disposition.** What persists across states and situations, each item with its recurrence evidence.

**Developmental state.** What is true at this state, with `valid_from` and `valid_until`, and a change-cause tag for each change from the prior state:

```text
DISPOSITION | KNOWLEDGE | RELATIONSHIP | CONTEXT | ROLE | RESOURCE | REVEALED_NOT_NEW | UNRESOLVED
```

`REVEALED_NOT_NEW` marks a trait the story discloses late but that was already operative. It must not be modeled as change.

**Situational delta.** Temporary emotional or bodily conditions that alter behavior without changing state.

**Values and appraisal.** What the character attends to and cares about, each with the conditions that override it.

**Decision rules.** The preferred form:

> **trigger + perceived stakes + current state → likely response family, with inhibitors, overrides, and named exceptions.**

Each rule records its evidence, its counterevidence, an alternative explanation, the observation that would disconfirm it, and its status:

```text
OBSERVED          seen once or in one context; not yet a rule
CANDIDATE_POLICY  recurs or is explicitly established; untested on held-out evidence
PROMOTED_POLICY   recurs and has survived validation
```

A useful rule excludes something. A rule compatible with every behavior predicts nothing.

**Voice model.** Treat speech as downstream of decision: appraisal, then objective, then speech act, then relationship filter, then register, then wording. Record:

- a register matrix by interlocutor and mode (casual, formal, family, conflict, embarrassment, support, monologue, as attested);
- self-reference, address terms, sentence endings, discourse markers, and nonverbal vocalizations, from the source language;
- what is directly attested, separately from what would merely sound plausible;
- "would sound wrong if" traps: wordings the character would not use, with evidence.

Evaluate voice on two separate axes: **decision fidelity** (the character would say this) and **surface fidelity** (the character would say it this way).

**Directed relationship conditioning.** How the character's behavior and speech change toward each significant other. A toward B is not B toward A. Do not globalize a behavior seen with one interlocutor.

**Domain sections**, as the evidence supports: conflict behavior; ethical deliberation; humor and play; mundane behavior; professional or role behavior; romance and intimacy.

**Counter-structure.** Counterexamples, rival readings, and abstention conditions: situations where the model should decline to predict.

**Known limits.** Each limit typed as evidence-backed or gap (Section 8).

## 11. Confidence and distance

Use qualitative confidence (`HIGH`, `MODERATE`, `LOW`, `OPEN`), never numeric probabilities. Grade how far a prediction travels from the evidence:

| Distance | Situation |
|---|---|
| D0 | Attested: the source shows this situation |
| D1 | Close variant: same situation type, a changed detail |
| D2 | Novel within the story world and the modeled state |
| D3 | Cross-scenario: counterfactual, crossover, or materially new setting |

Confidence falls with distance unless a promoted rule specifically covers the case. A D3 prediction states its assumed chronology, interlocutor relationship, and setting.

---

# IV. Evaluator-facing evidence

## 12. Dimension crosswalk

The evaluator grades twelve dimensions and six scenario-readiness types. A project makes its evidence assessable by showing, per model, where each is addressed. It does not grade them.

| Evaluator dimension | Where the model addresses it |
|---|---|
| `PSYCHOLOGICAL_MODEL` | Values and appraisal; decision rules |
| `LONGITUDINAL_STATE` | Developmental states and change causes |
| `VOICE_REGISTER` | Voice model and register matrix |
| `MUNDANE_BEHAVIOR` | Ordinary-life sample; mundane behavior |
| `RELATIONSHIP_CONDITIONING` | Directed relationship conditioning |
| `INTERIORITY` | Interiority access strategy (Section 5) |
| `CONFLICT_BEHAVIOR` | Conflict behavior section; relevant rules |
| `ETHICAL_DELIBERATION` | Ethical deliberation section |
| `HUMOR_PLAY` | Humor and play section |
| `SOURCE_COMPLETENESS` | Source boundary; excluded evidence; coverage |
| `NEGATIVE_EVIDENCE` | Evidence-backed limitations |
| `TEMPORAL_SPECIFICITY` | State binding and validity intervals |

For scenario readiness (`DIALOGUE`, `CROSS_SCENARIO`, `MUNDANE_SOCIAL`, `ETHICAL_DELIBERATION`, `ROMANCE_RELATIONSHIP`, `PROFESSIONAL_CONTEXT`), state what evidence exists and its limits. For cross-scenario use, write a scenario contract naming the assumed chronology, interlocutor relationship, and setting.

The evaluator also distinguishes literary from behavioral support, source-supported from merely fluent voice, historical from later state, ambiguity from contradiction, and counterfactual from extrapolation. Keep those distinctions visible in the model.

## 13. Stable, eligible artifacts

An assessment binds an exact evidence set at an exact commit; any change to a cited artifact makes the assessment stale. Therefore:

- keep one stable file per subject and state, or stable heading anchors within a file; never cite line numbers;
- carry the recognized authority front matter (`status`, `supersedes`, `superseded_by`, `do_not_use_as_current_authority`), with reciprocal supersession links; an unclassified file cannot support an assessment;
- revise a model by issuing a new version that supersedes the old one, rather than by rewriting a model that may already have been assessed;
- never promote a provisional model by editing its front matter.

---

# V. Validation

## 14. Prospective freeze

Freeze predictions before the analyst is exposed to the material that tests them:

1. record each prediction, its rule, its distance, and its confidence in a committed prediction register;
2. read the held-out material;
3. adjudicate in a separate record, without editing the frozen register.

Outcomes:

```text
SUPPORTED | PARTLY_SUPPORTED | CONTRADICTED | NO_DIAGNOSTIC_OPPORTUNITY | CONFOUNDED | UNRESOLVED
```

`NO_DIAGNOSTIC_OPPORTUNITY` is not failure: the material never tested the prediction.

## 15. Retrospective tests

A test against material the analyst has already read is retrospective. Label it so, record what the analyst had been exposed to, and weight it below a prospective test. Never present a retrospective fit as a prediction.

## 16. Adversarial tests

As the model's use requires:

- **perturbation**: change one condition of an attested situation and check that the prediction changes only where a rule says it should;
- **decoys**: present plausible responses that violate a named rule or trap, and check that the model rejects them;
- **negative controls**: situations where the model should abstain;
- **voice falsification**: score content and naturalness separately; fluent wording that the character would not choose fails;
- **baseline comparison**: check that the model does better than a generic personality sketch of the same character.

## 17. Fidelity audit

Before a model is offered as mature, audit it rule by rule:

```text
PASS | PASS_WITH_BOUND | NEEDS_TARGETED_SOURCE_REVIEW | INSUFFICIENT_EVIDENCE
```

## 18. Scoring and records

Score qualitatively, with denominators and exclusions stated. Do not report accuracy percentages; they imply a sampling frame the tests do not have. Keep the register, the adjudications, and any audit beside the model they test. When more than one model or provider has built a model of the same character, a consistency audit compares the models' rules and predictions, not their prose.

---

# VI. Medium modules

## 19. Prose: novels and light novels

Interiority is often directly given, which makes it the most tempting route to over-model. Distinguish focalized thought from speech, and both from narration. Treat a first-person narrator's account of others as that narrator's perception. Keep witnesses apart where multiple narrators describe the same character. Watch the thought–speech gap: what a character thinks and does not say is evidence about the gap, not license to make the model voice its private thoughts.

## 20. Manga

Evidence is written dialogue and drawn behavior. There is no timbre or delivery; voice models are written-register models. Balloon attribution, offscreen speakers, and wordless panels can be ambiguous; record attribution confidence. An anime adaptation's performances are a separate layer, admitted only if the source boundary includes it.

## 21. Anime and audiovisual sources

Keep the textual layer (subtitles in the primary language) and the performance layer apart. Performance claims about delivery, timing, and movement are admitted only from inspection routes that can support them, under the [inspection-lane routing policy](../source-policies/MANGA_ANIME_MEDIUM_AND_INSPECTION_LANE_ROUTING_POLICY.md). Cite the calibrated timestamp. Text cannot reproduce performance, and a model built from subtitles alone is a model of the script.

## 22. Games and live-service sources

Declare source-class admission: main story, events, bond or relationship content, player choices, variants, alternate costumes or versions. Generated retrieval bundles are projections, not evidence. State explicitly whether performed voice is admitted. A character spread across many sources may need to be reconstructed by intersection, with an observer matrix that records who sees which side of the character. Scope each state to its route, variant, and context class, and default to the reconstruction-current state, under the [generic game method](GENERIC_GAME_ANALYTICAL_METHOD.md) (Parts IV and V).

---

# VII. Failure modes

Each of these has recurred across several projects in this corpus. Treat them as prohibitions.

1. **Catchphrase overfitting**: reproducing signature lines without their pragmatic fit.
2. **Invented interiority**: giving the model thoughts the source never grants, or having it voice private thoughts aloud.
3. **State collapse**: a crisis response modeled as baseline, or a temporary state merged into a trait.
4. **Later-knowledge leakage**: explaining an earlier state with later revelations.
5. **Globalized relationship behavior**: a behavior seen with one interlocutor applied to all.
6. **Synthetic output treated as evidence.**
7. **Absence read as negative evidence** without an opportunity.
8. **Crisis-heavy sampling**: no ordinary-life control sample.
9. **Translation as voice authority.**
10. **Role mistaken for personality**: an institutional or performed role modeled as the character's disposition.

---

# VIII. Outputs

A reconstruction stage normally delivers, per subject and state:

- the evidence ledger;
- the operational model, with its dimension crosswalk and known limits;
- the prediction register and adjudication records, if validation was run;
- the fidelity audit, if the model is offered as mature;
- an update to the project's reconstruction readiness record, describing coverage and limits, not grades.

---

# IX. Blind and benchmark use

To test reconstruction itself:

- give the analyst only this method, the project's adapted method, and a bounded evidence package; withhold franchise knowledge, existing models, and monographs;
- hold out later units as test material and freeze predictions before release (Section 14);
- audit leakage: record when the analyst recognized the work or recalled events beyond the package;
- compare models built from different evidence conditions (text only; text and images; with performance evidence) on the same held-out tests.

---

# X. Governing rules

1. **A model is derived from the literary corpus and routes back to it.**
2. **Synthetic output is never evidence.**
3. **Every state is time-indexed.**
4. **Disposition, state, and situation are separate layers.**
5. **A rule must exclude something and carry its exceptions.**
6. **Speech follows decision.**
7. **Relationship conditioning is directional.**
8. **Absence is evidence only where opportunity existed.**
9. **Voice comes from the source language.**
10. **Confidence falls with distance from the evidence.**
11. **Predictions are frozen before the test.**
12. **The project describes coverage; the evaluator grades capability.**

---

# Repository context

- [Character reconstruction capability specification](../../characters/RECONSTRUCTION_CAPABILITY_SPEC.md): dimensions, scenario readiness, known limits, evidence eligibility, and artifact authority.
- [Character reconstruction maintenance policy](../policies/CHARACTER_RECONSTRUCTION_MAINTENANCE.md): the evaluator's role and process.
- [Character discovery maintenance policy](../policies/CHARACTER_DISCOVERY_MAINTENANCE.md): how artifacts become curated evidence items.
- [Generic multi-document synthesis architecture template](GENERIC_MULTI_DOCUMENT_SYNTHESIS_ARCHITECTURE_TEMPLATE.md): reconstruction placement, timing, and artifact split in a project's architecture.
- [Medium and inspection-lane routing policy](../source-policies/MANGA_ANIME_MEDIUM_AND_INSPECTION_LANE_ROUTING_POLICY.md): which inspection routes can support performance claims.
- [Project initiation and architecture policy](../source-policies/MANGA_ANIME_PROJECT_INITIATION_AND_ARCHITECTURE_POLICY.md): Section 5.5, character and reconstruction responsibilities.
