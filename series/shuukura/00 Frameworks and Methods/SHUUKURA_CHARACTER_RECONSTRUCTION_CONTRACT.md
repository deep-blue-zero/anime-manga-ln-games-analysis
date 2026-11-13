---
title: "Shuukura V2 — Character Reconstruction Contract"
artifact_id: SHUUKURA_CHARACTER_RECONSTRUCTION_CONTRACT
artifact_type: character_reconstruction_specification
series: "Shuukura / 週に一度クラスメイトを買う話"
series_id: shuukura
generation: SHUUKURA_V2
version: "0.2"
status: active_provisional
scope: "Time-indexed behavioral models, readiness, tests and abstention"
source_boundary: "Specification for frozen inventory SHUUKURA-V2-20261017-I1; no constructed or tested character model"
canonical_home: series/shuukura/00 Frameworks and Methods/SHUUKURA_CHARACTER_RECONSTRUCTION_CONTRACT.md
created: "2026-10-17"
planning_date: "2026-10-16"
review_status: OWNER_ADOPTED_FOR_AUTHORIZED_V2_EXECUTION
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
do_not_use_as_literary_evidence: true
---

# Character reconstruction contract

## Responsibility and present state

This contract defines an executable reasoning specification for future source-tested models. It is not a model. No character trait, reconstruction result or validation score is populated at bootstrap. The primary intended subjects are **宮城志緒理 / Miyagi Shiori** and **仙台葉月 / Sendai Hazuki**. Supporting characters are assessed from independently accumulated V2 evidence; a name in a source inventory or V1 filename does not confer readiness.

A monograph explains a person's literary development, psychology, relationships, language and formal role. A reconstruction maps a specified person's state and information at a specified time to a bounded repertoire of plausible responses. The two may cross-reference one another but neither substitutes for the other. A model must explain where it fails or abstains, not just produce plausible dialogue.

## Model identity and input contract

Each model declares subject ID/name; witness/edition; model version and authority; admitted source boundary; reconstruction-time interval; training evidence; excluded/test evidence; actual reviewer; applicable domains; dependencies; and unresolved uncertainty. Cross-witness identity correspondence does not authorize mixing LN and web observations into a single undifferentiated person-state. State explicitly whether a model is LN-only, web-only, or a justified comparison.

Every query must supply `subject`, `witness_revision`, `time_state_id`, `situation`, `interlocutor_ids`, `public_private_context`, `available_options`, and an information packet. Unknown options, motive or social context stay unknown. The information packet is restricted to what that subject has encountered by the selected time: `known`, `believed`, `suspected`, `concealed_by_subject`, `misbelieved`, `unavailable`, each with provenance and confidence. Analyst-known truth is kept in a separate evaluation record and cannot enter the simulation prompt as character knowledge.

The model rejects an invalid witness/time combination, leaked future knowledge, a nonexistent demonstrated skill or an ungrounded claim about another person's private thoughts. An analyst's retrospective interpretation may describe a mechanism, but the simulated person must not articulate it as conscious self-knowledge without evidence.

## State representation

| Component | Required representation and control |
| --- | --- |
| Temporal state | Stable state ID, entering/exiting source boundary, event-time uncertainty, reason for transition and prior-state link |
| Dispositions | Repeated context-supported tendencies, exceptions and strength; distinguish stable tendencies from temporary stress and recent learning |
| Motivation | Desires, fears, priorities, incompatible intentions, trade-offs, anticipated consequences and self-justifications; explicit versus inferred |
| Self-model | Claimed identity, ideal/feared self where supported, self-presentation and discrepancies with action; do not add a diagnostic label |
| Information | Subject-specific proposition states and acquisition times; what is unavailable, mistaken, hidden or uncertain |
| Decision policy | Conditions, salient cues, available choices, ranked/plausible response families, inhibitions and fallback/avoidance behavior |
| Interpersonal conditioning | Separate policy toward each evidenced interlocutor; asymmetry, disclosure, trust, boundaries and public/private differences |
| Regulation and stress | Triggers, coping/avoidance, escalation, recovery and failure conditions, all time- and context-bounded |
| Japanese expression | Address forms, omissions, register, refusal/request strategies, hedges and disclosure habits; dialogue distinct from private narration |
| Contradictions/errors | Characteristic misreadings or inconsistent choices supported by multiple routes; distinguish model error and source ambiguity |
| Limits | Competing explanations, weak domains, negative constraints, abstention and unsupported behaviors |

Each material policy rule must cite at least one exact observation and an assessed countercase or state that no countercase has yet been inspected. A single scene may support a narrow local response; it cannot alone establish a general disposition. Do not manufacture probabilities from prose evidence. If likelihoods are used for a test, disclose their subjective elicitation and compare calibration separately from fit.

## Output contract

A responsible output contains: applicable state/domain; allowed information; cues attended to; plausible options; preferred response family with grounds; alternatives that remain credible; expected language/disclosure tendencies; confidence/abstention; and linked evidence/rule IDs. Distinguish a predicted action from a generated illustrative line of dialogue. No exact invented Japanese line is treated as a quotation or as unique inevitable behavior.

Negative constraints are first-class: no future revelation; no access to the other person's internal monologue; no assumption that behavior generalizes across public/private contexts or across relationships; no diagnosis from literary traits; no inference that a single consent or refusal governs all later interactions; no voice/performance imitation claim from prose alone; no assertion that an unsourced supporting character has a fully known private psychology.

## Domain readiness

Readiness is assessed per `(subject, witness, time regime, domain)`, not awarded once to an entire person. The [character ledger](../04%20Longitudinal%20Ledgers/SHUUKURA_CHARACTER_STATE_AND_READINESS_LEDGER.md) is the only cumulative readiness home.

| State | Meaning and permissible output |
| --- | --- |
| UNASSESSED | No V2 assessment; bootstrap state for all subjects |
| INSUFFICIENT | Evidence cannot constrain a useful response; abstain |
| EMERGING | Local observations permit explicitly narrow hypotheses, no general behavioral model |
| MODERATE | Multiple situations support a provisional domain policy; material alternatives remain |
| STRONG | Context variation, temporal changes, countercases and Japanese interaction evidence are traceable; candidate reconstruction may be drafted |
| SPECIALIST_READY | Strong domain evidence plus reconciled claims, explicit gaps, sealed test design and independent acceptance plan; modeling/validation work may be assigned within separate authorization |

No count of scenes alone promotes readiness. A STRONG speech domain does not imply STRONG motivation or unfamiliar-interlocutor prediction. A supporting character may warrant a substantial monograph while reconstruction remains INSUFFICIENT. Dedicated treatment is justified by a recoverable development question or distinctive recurring behavior across contexts, sufficient direct evidence and independent explanatory value; otherwise retain the subject in the dyadic/ensemble synthesis and record why.

## Validation design

1. **Retrospective fit:** trace a rule through already inspected passages, including disconfirming examples and state changes. Label this fit, not held-out success.
2. **Prospective held-out test:** before a later eligible passage is inspected by the model author, freeze model version, information cutoff, scenario framing, predictions, alternatives, discriminating outcomes and scoring rubric. Prefer naturally subsequent source situations. A reviewer prepares a scenario from pre-outcome evidence without giving away the outcome or a later narrator's explanation.
3. **Exposure audit:** list precisely which outcomes the author, evaluator and prompt have seen. If prior familiarity, a V1 discussion or a summary reveals the answer, mark the item contaminated and downgrade it to retrospective fit. Fresh sessions reduce context contamination; they cannot prove that a pretrained model has never encountered the work.
4. **Reveal and adjudicate:** compare against the source situation after predictions are frozen. Score action class, motivation explanation, interlocutor conditioning, language/register, epistemic fidelity and calibrated abstention separately. A semantically similar action for an unsupported motive is only partial support. Multiple source-compatible responses may remain plausible.
5. **Challenge:** inspect an ordinary situation, a boundary/refusal or negotiation, a public/private contrast, a conflicting motive, an information-asymmetry case and a temporal transition when the admitted source supplies them. If a class is absent, record limited validation rather than inventing a source test.
6. **Revise and retest:** preserve failed predictions, classify the failure as evidence gap, wrong state, wrong knowledge, wrong conditional rule, ambiguity or unsupported extrapolation, revise the model with linked claims, then test only on a new untouched case. Reusing a revealed test is training/fit.

Freeze the rubric before seeing outcomes. A practical rubric uses `SUPPORTED`, `PARTIAL`, `CONTRADICTED`, `NONDISCRIMINATING`, `ABSTAINED` for each dimension, with a source-grounded rationale. Report denominators, exclusions and contamination, not a context-free accuracy percentage. Compare the candidate against a simple prior-state or coarse descriptive baseline: a sophisticated model should explain more than a generic relationship stereotype. Negative controls include a deliberately future-contaminated prompt, an impossible knowledge attribution and an unsupported interlocutor; the expected behavior is rejection or abstention.

## Acceptance, use and retirement

Model acceptance requires an auditable state/information contract, strong support in the claimed domains, meaningful countercases, correctly labeled fit versus held-out evidence, failure retention, explicit negative constraints, and a semantic review independent of the authoring claims. An unavailable required test blocks validated status for that domain, not the separate literary synthesis. Zero tested domains cannot yield a validated overall model.

Future model home: `05 Character Studies/SHUUKURA_<SUBJECT>_RECONSTRUCTION.md`; companion monograph: `05 Character Studies/SHUUKURA_<SUBJECT>_MONOGRAPH.md`. These are reserved naming patterns, not existing files or bootstrap deliverables. Use source-established identity and the repository's curation conventions; do not create global registry entries here. Validation records live with the model so its tested scope remains attached, while readiness summaries point back to those records.

Hypothetical and crossover simulations are downstream, noncanonical applications. Their outputs are not observations, evidence, validation cases or new story facts. A model update invalidates affected downstream applications by version; preserve older model/test versions and do not silently claim a new boundary for them.

Revision 0.2: owner adoption recorded for continuous execution. Model state remains UNASSESSED; no construction, predictive test or validation has occurred.
