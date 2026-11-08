---
title: "Domestic Girlfriend — character reconstruction contract"
series: domestic-girlfriend
artifact_id: DG_RECONSTRUCTION_SPECIFICATION
artifact_type: character_reconstruction_specification
generation: DG-G1
version: "1.0"
status: canonical
authority_scope: "Derived-use methodology and coverage controls; no model, simulation, or capability assessment"
source_boundary: "Metadata reconnaissance of Japanese manga volumes 01-03 only; no narrative units admitted or inspected"
canonical_home: series/domestic-girlfriend/DG_RECONSTRUCTION_SPECIFICATION.md
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
recommended_reasoning_class: DEEP_SYNTHESIS
---

# Character reconstruction contract

## Purpose and present boundary

Character reconstruction is an intended downstream responsibility because the project is designed to preserve changing behavior, motives, relationships and Japanese expression. Its present status is **NOT_READY**: no person has been established from inspected evidence, no source unit admitted, no model built and no evaluation performed. Three inventoried volumes cannot certify either the source's full developmental range or a whole-series character.

This contract adapts the [generic reconstruction method](../../governance/analytical-methods/GENERIC_CHARACTER_RECONSTRUCTION_METHOD.md) to an opening-only manga acquisition. Reconstruction is derived use of the literary corpus, never a parallel canon or its master interpretation. A literary monograph explains a character's meaning and development; a model makes bounded conditional behavioral claims. Neither substitutes for the other.

## Evidence capture begins with authorized reading

The character, directed-relationship, expression/everyday and claim ledgers are day-one evidence routes. They must preserve ordinary-life situations as well as crises, relationship-specific responses, self-report versus shown conduct, Japanese wording, state transitions and contradicting cases. No reconstruction dossier may be filled from a familiar name, title, plot summary or generic personality taxonomy.

For a later proposed subject/state, first create a distinct evidence map with `evidence_id | subject_key | state/horizon | continuity | situation/stakes | interlocutor/audience | evidence_class | locator | reading_anchor/claim_ids | source_language_status | counterevidence | limitation`. Evidence classes are DS direct speech, DB shown behavior, NI presented interiority, RB reported behavior, OS observer/role statement and INF inference. PF performance is unavailable in the current manga scope. Apparent interiority without secure attribution remains unresolved.

The map is not a duplicate reading. It links the reasoning and exact witness support needed to reconstruct decisions. Evidence of absence requires an opportunity to act; untested contexts remain gaps. A crisis-only sample cannot establish ordinary behavior. A new revelation about an earlier period is labeled REVEALED_NOT_NEW rather than mistaken for new development.

## Distinct artifacts, created only when earned

For each eligible subject and defined state, use separate future homes:

- `reconstruction/DG_<SUBJECT>_<STATE>_EVIDENCE_LEDGER.md`: scoped retrieval map and exclusions.
- `reconstruction/DG_<SUBJECT>_<STATE>_MODEL_VNN.md`: operational model and limits.
- `reconstruction/DG_<SUBJECT>_<STATE>_VALIDATION_VNN.md`: independent test specification, frozen predictions, adjudications and fidelity review.
- `studies/DG_<SUBJECT>_CHARACTER_MONOGRAPH.md`, only when a distinct literary question earns it: interpretation, not model certification.

No such artifacts exist now. Resolve established names and any curated subject ID at creation; do not seed global discovery or capability rows. A model version later assessed by an evaluator stays identifiable and is superseded explicitly rather than silently rewritten.

## Operational-model contract

A future model header binds subject, source-established identity, continuity/witness, `Character@Unit` state, earliest/latest evidence, excluded evidence, exact evidence-base commit, model version and actual inspection lanes. It includes no later-volume knowledge outside its state.

The body must distinguish stable dispositions, developmental state with validity interval and change cause, situational deltas, values/appraisal, directed relationship conditioning, ordinary behavior and explicit unknowns. Decision rules take the form “trigger + perceived stakes + current state → plausible response family,” with inhibitors, overrides, evidence, counterexamples, rival explanations and a disconfirming case. Rules move from OBSERVED to CANDIDATE_POLICY to PROMOTED_POLICY only with actual support and validation.

Written-register modeling follows appraisal → objective → speech act → interlocutor filter → register → wording. Preserve private thought versus public speech: inner access is not permission to make a model speak its thoughts aloud. Record source-attested self-reference, address, endings and pragmatic contrasts across ordinary and conflict contexts, with “would sound wrong if” traps supported by Japanese evidence. This is not a voice-actor or acoustic model.

Confidence is qualitative: HIGH, MODERATE, LOW or OPEN. Prediction distance is D0 attested case, D1 close variant, D2 novel situation within the admitted story world/state, or D3 cross-scenario. A D3 use specifies chronology, relationship and setting assumptions and defaults to strong limits. Fluency cannot raise confidence.

The opening frontier makes abstention especially important. A model may predict only within the situations and states its evidence supports. Later acquisition triggers state separation and possible revision, not a retroactive claim that an early model already knew the outcome.

## Independent held-out validation

A separate evaluator/reviewer must assess the model against a declared frozen evidence set; author confidence is not evaluation. Before model authorship or exposure to test material, the operator identifies held-out situations or units and their access boundary. Model author records all prior exposure. Where a clean held-out set cannot be established because the author has read everything, label the test RETROSPECTIVE_CONSISTENCY_TEST and do not report it as prospective success. Genuine held-out evaluation requires evidence withheld from the model author, not merely a delayed adjudication of known material.

For a prospective test, commit/freeze `prediction_id | model_version | rule_ids | test_scope | predicted_response_family | confidence | distance | assumptions | falsifier | exposure_disclosure` before releasing held-out evidence. A later authorized source unit is not automatically available as test material. With only V01–03 presently acquired, the project may defer testing rather than manufacture an unseen future.

The independent adjudication records diagnostic opportunity, observed response, evidence/locators, outcome and reasoning. Outcomes are SUPPORTED, PARTLY_SUPPORTED, CONTRADICTED, NO_DIAGNOSTIC_OPPORTUNITY, CONFOUNDED and UNRESOLVED. Separate decision fidelity from surface-language fidelity. Test plausible decoys, negative controls requiring abstention, changed-interlocutor perturbations and ordinary-life cases; compare with a generic-personality baseline. Record exclusions and test counts without unsupported accuracy percentages.

Fidelity findings are PASS, PASS_WITH_BOUND, NEEDS_TARGETED_SOURCE_REVIEW or INSUFFICIENT_EVIDENCE. A failure revises the source-grounded rule and affected interpretations through the claim system. It does not alter the frozen forecast to improve apparent performance.

## Synthetic-output firewall

Generated dialogue, invented scenes, role-play and predictions are synthetic test outputs. They are never observations about the character, source quotations, evidence rows or grounds for new canonical claims. If separately authorized later, keep them clearly labeled beside the test, with the model/version and assumptions. The source can test a model; a model cannot manufacture missing source evidence. No simulation is authorized or generated by this bootstrap.

## Coverage/readiness controls and schema

| Control ID | Scope | Current evidence coverage | Limit | Next acceptance condition |
|---|---|---|---|---|
| DG-RC-001 | All potential subjects | NONE | No narrative inspection or established subjects | Source-grounded capture during an authorized reading |
| DG-RC-002 | Longitudinal behavior | NONE | V01–03 acquisition is partial; no developmental findings | Distinct time-indexed states and counterexamples within the declared horizon |
| DG-RC-003 | Ordinary life and written register | NONE | No samples; Japanese inspection unperformed | Diagnostic ordinary contexts and source-verified Japanese examples |
| DG-RC-004 | Models / held-out tests | NOT_CREATED / NOT_RUN | No clean test set or model currently exists | Frozen model/predictions plus independent adjudication |
| DG-RC-005 | Capability grades | NOT_ASSESSED | Reserved to repository evaluator | Evaluator examines eligible exact evidence; series author never self-grades |

At each accepted unit, amend controls only for actual evidence changes and append `event_id | date | control_or_subject | previous_coverage | new_coverage | evidence_routes | residual_gap | responsible_role`. Preserve history. Per-subject coverage rows, when earned, use `subject/state | evidence_boundary | dimension | supporting_ids | counterevidence | gap_or_evidence_backed_limit | prospective_test_status | next_action`.

Make all twelve evaluator dimensions assessable: psychological model, longitudinal state, voice/register, mundane behavior, relationship conditioning, interiority, conflict behavior, ethical deliberation, humor/play, source completeness, negative evidence and temporal specificity. State evidence and limits for dialogue, cross-scenario, mundane-social, ethical, relationship and professional scenarios without assigning grades. The designated evaluator alone owns capability partitions; the discovery agent alone curates discovery metadata.
