---
title: "Scum’s Wish — reconstruction and independent evaluation contract"
series: scums-wish
artifact_id: SW_RECONSTRUCTION_SPECIFICATION
artifact_type: character_reconstruction_specification
generation: SW-G1
version: "1.0"
status: canonical
authority_scope: "Derived-use methodology/coverage controls only; no models, synthetic scenes or capability grades"
source_boundary: "Metadata reconnaissance of Japanese main manga volumes 01-08 and decor volume 09; no narrative units admitted or inspected"
canonical_home: series/scums-wish/SW_RECONSTRUCTION_SPECIFICATION.md
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
recommended_reasoning_class: DEEP_SYNTHESIS
---

# Reconstruction and independent evaluation contract

## Placement and current state

Reconstruction is an intended derived use of the source-grounded literary corpus. It is distinct from a monograph, relationship interpretation or moral assessment. Its current state is NOT_READY: no source unit admitted, no character established, no model, simulation or evaluation produced.

The [generic reconstruction method](../../governance/analytical-methods/GENERIC_CHARACTER_RECONSTRUCTION_METHOD.md) is adapted here to manga with a MAIN V01–08 horizon and a separately gated DECOR09 horizon. A main-state model and a later supplement-aware model must not become one timeless personality description. Their relationship is an evidence question, not something the supplementary label settles.

## Source-grounded evidence pathway

Capture during authorized sequential reading preserves shown conduct, direct speech, private thought, narrated presentation and reports about others as different evidence routes. A person's explicit self-description does not automatically become a validated behavioral rule. If interior access is uncertain, inferential status and attribution confidence stay visible.

A future evidence map uses `evidence_id | subject/state | MAIN_or_DECOR_horizon | witness/continuity | situation/stakes | interlocutor/audience | evidence_class | source_locator | reading_anchor/claim_ids | Japanese_status | competing_account | limitation`. Evidence classes are DS direct speech, DB directly shown behavior, NI presented interiority, RB reported behavior, OS observer/role statement and INF inference. PF performance is outside this source boundary.

Preserve ordinary-life and humor evidence where the source offers it, alongside conflict or intimacy. Do not generalize from one interlocutor to all others. Absence counts as negative evidence only with a real opportunity to behave otherwise; an unrepresented situation is a gap. A thought–speech gap is evidence about communication, not permission for a model to speak private thoughts aloud.

## Separate future artifacts

Create only when the evidence supports a defined subject/state:

- `reconstruction/SW_<SUBJECT>_<STATE>_EVIDENCE_LEDGER.md`: bounded retrieval and exclusions.
- `reconstruction/SW_<SUBJECT>_<STATE>_MODEL_VNN.md`: operational structure, counterexamples and abstentions.
- `reconstruction/SW_<SUBJECT>_<STATE>_VALIDATION_VNN.md`: independent test record and fidelity audit.
- An earned `studies/SW_<SUBJECT>_CHARACTER_MONOGRAPH.md`: literary interpretation, separately scoped and accepted.

No such artifacts exist at bootstrap. Source-derived project keys may later map to curated subject IDs; the series author does not create discovery or capability registry records. Each assessed version retains its exact identity and evidence-base commit.

## Model requirements

Bind subject, state `Character@MAIN-VNN` or another source-supported state, continuity/frame, source witnesses, temporal and disclosure limits, excluded evidence, evidence-base commit, version and actual inspection lanes.

The body distinguishes stable dispositions from developmental state and transient conditions. Every state has a validity interval and a change cause: DISPOSITION, KNOWLEDGE, RELATIONSHIP, CONTEXT, ROLE, RESOURCE, REVEALED_NOT_NEW or UNRESOLVED. The analyst learning a fact is not necessarily the character changing.

A decision rule states trigger, perceived stakes and current state → likely response family, with inhibitors, overrides, alternative explanations, counterexamples and a disconfirming condition. It must exclude plausible responses rather than accommodate everything. Rule status is OBSERVED, CANDIDATE_POLICY or PROMOTED_POLICY, based on evidence and actual testing.

Directed relationship conditioning names the interlocutor and evidenced mode. Speech generation follows appraisal → objective → speech act → relationship filter → register → wording. Model Japanese expression from attested address, self-reference, politeness, endings and contextual contrasts; score decision fidelity separately from surface wording. Private thought, irony, silence and reported speech retain their source layers. No acoustic performance is modeled.

Use HIGH, MODERATE, LOW or OPEN confidence. Distance D0 is attested, D1 a close variant, D2 a novel situation within admitted world/state and D3 a cross-scenario case. D3 requires explicit chronology, relationship and setting assumptions, and abstention where evidence cannot constrain it. A morally flattering, condemning or fluent response is not evidence of fidelity.

## Genuine held-out testing and retrospective checks

An independent reviewer/evaluator tests a frozen model. Before exposure, identify the withheld evidence and record the model author's knowledge boundary. Genuine held-out evidence has not been seen by that author or included through summaries, monographs or remembered adaptation events. If exposure already occurred, label the exercise RETROSPECTIVE_CONSISTENCY_TEST; delaying adjudication does not restore a clean test.

DECOR09 is not automatically a valid held-out test just because it is separate in the inventory. It may concern a later state, changed setting or newly disclosed premise, and the analyst may already know it. Its admission requires owner scope. A test must distinguish changed character state from a prediction failure at the earlier modeled state. When no diagnostic unexposed material is available, leave prospective validation pending.

Before release of the test material, freeze `prediction_id | model/version | rule_ids | modeled_state | assumptions | response_family | confidence/distance | falsifier | test_scope | exposure_disclosure`. Independent adjudication records opportunity, source response, locators, outcome, reasoning and any state mismatch. Outcomes are SUPPORTED, PARTLY_SUPPORTED, CONTRADICTED, NO_DIAGNOSTIC_OPPORTUNITY, CONFOUNDED and UNRESOLVED.

Tests include ordinary situations, changed-interlocutor perturbations, plausible decoys, abstention controls and Japanese expression checks where supported. Compare with a generic personality baseline and keep content fidelity separate from linguistic naturalness. Report qualitative findings with counts/exclusions, not unsupported accuracy percentages. Fidelity results are PASS, PASS_WITH_BOUND, NEEDS_TARGETED_SOURCE_REVIEW or INSUFFICIENT_EVIDENCE.

## Synthetic-output firewall

Generated dialogue, imagined scenes, simulated reactions and predictions are synthetic outputs, never literary evidence, source quotations or new observations. If separately authorized later, preserve them as labeled test artifacts with model/state/assumptions. They cannot populate the source evidence ledgers or repair an unobserved motive. The source tests the model; the model does not establish what the source contains. This bootstrap authorizes no simulation.

## Coverage controls

| Control ID | Scope | Current state | Limit / next acceptance condition |
|---|---|---|---|
| SW-RC-001 | All subjects | NO_EVIDENCE | Establish identities and scoped evidence only during authorized reading |
| SW-RC-002 | MAIN temporal/perspective states | NO_EVIDENCE | Distinguish action, self-report, inner presentation and observer beliefs |
| SW-RC-003 | Directed relationships and ordinary behavior | NO_EVIDENCE | Preserve contextual/directional contrast and diagnostic opportunity |
| SW-RC-004 | Japanese register | NO_EVIDENCE | Source-verified expression; private thought not public voice |
| SW-RC-005 | DECOR-derived model changes | NOT_AUTHORIZED | Separate source/state horizon and main-only freeze required |
| SW-RC-006 | Independent held-out validation | NOT_RUN | Clean withheld evidence and frozen predictions, or explicit retrospective label |
| SW-RC-007 | Capability assessment | NOT_ASSESSED | Designated evaluator alone grades eligible exact evidence |

Coverage updates append `event_id | date | control_or_subject | old_state | new_state | evidence_routes | remaining_gap | responsible_role`; current cells may change only with that history. When a subject earns evaluation, add `subject/state | horizon | dimension | evidence_ids | counterevidence | gap_or_evidence_backed_limit | test_status | next_action`.

Expose evidence and limits for all twelve evaluator dimensions: psychological model, longitudinal state, voice/register, mundane behavior, relationship conditioning, interiority, conflict, ethical deliberation, humor/play, source completeness, negative evidence and temporal specificity. Likewise describe support for dialogue, cross-scenario, mundane-social, ethical, relationship and professional scenarios. Do not self-assign grades or readiness tiers; those belong to the reconstruction evaluator.
