---
title: "Cornered Mouse — Character Reconstruction Protocol"
artifact_id: CORNERED_MOUSE_CHARACTER_RECONSTRUCTION_PROTOCOL
artifact_type: character_reconstruction_protocol
series: "The Cornered Mouse Dreams of Cheese / 窮鼠はチーズの夢を見る"
series_id: cornered-mouse
generation: CORNERED_MOUSE_BOOTSTRAP_V1
version: "0.2"
status: active_provisional
scope: "Future source-bounded behavioral rules, portability and separate validation"
source_boundary: "Japanese manga continuity; AIO2020 structurally checked; no narrative admission or reading"
canonical_home: series/cornered-mouse/00 Frameworks and Methods/CORNERED_MOUSE_CHARACTER_RECONSTRUCTION_PROTOCOL.md
created: "2026-10-24"
review_status: OWNER_BOOTSTRAP_ARCHITECTURE_APPROVED
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
do_not_use_as_literary_evidence: true
recommended_reasoning_class: DEEP_SYNTHESIS
---

# Character reconstruction protocol

This is a protocol, **not a character model or readiness certification**. No subject has been source-enrolled or assessed. Kyoichi and Imagase are bibliographically identified candidate subjects only; secondary subjects require their own independent evidence. The [character ledger](../03%20Longitudinal%20Ledgers/CORNERED_MOUSE_CHARACTER_DEVELOPMENT_AND_READINESS_LEDGER.md) owns local readiness and gaps. The [method](CORNERED_MOUSE_ANALYTICAL_METHOD.md) owns observations; the [architecture](CORNERED_MOUSE_SYNTHESIS_ARCHITECTURE.md) owns promotion and literary integration.

The live [capability specification](../../../characters/RECONSTRUCTION_CAPABILITY_SPEC.md), [schema](../../../governance/schemas/character-reconstruction-capability.schema.json), and [maintenance policy](../../../governance/policies/CHARACTER_RECONSTRUCTION_MAINTENANCE.md) govern any later global evaluation. This project neither assigns global tiers nor writes their registry. A literary monograph is not an operational behavioral model, and a full-series synthesis cannot certify prediction readiness.

## Target and model dimensions

The target is a source-grounded, time-bounded account of plausible behavior beyond directly depicted scenes, with explicit uncertainty and abstention. Preserve an individual's choices and contradictions rather than a universal personality portrait.

| Dimension | Required evidence and limit |
|---|---|
| Stable dispositions | Repeated preferences, values, habits, vulnerabilities, communication and decision patterns across materially different situations; separate from one scene or assertion |
| Temporal state | Exact source boundary; knowledge/belief, desire, fear, expectations, commitments, recent events and options then available |
| Relational conditioning | Interlocutor identity, history, intimacy, obligations, expectations and perceived power; compare behavior across relationships before transferring it |
| Conflict response | Evidenced avoidance, pursuit, confrontation, capitulation, retaliation, repair and withdrawal, including alternatives, failures and counterexamples |
| Agency and choice | Perceived available actions and costs, intended gains/avoided losses, practical exit options, information leverage and uncertainty |
| Written dialogue | Vocabulary, register, self-reference, forms of address, initiative, directness/evasion and interaction pattern with Japanese locators; no inferred acoustic voice or physical performance |
| Contradictions and limits | Competing explanations, context-dependent inconsistency, evidenced change, negative constraints and genuine gaps |

A stable preference, temporary fear, intimate dependency and response under coercive leverage are distinct explanatory variables. Strong attachment cannot stand in for consent; avoidance cannot be labeled a stable trait without comparing alternatives and counterexamples. These are methodological tests, not findings about either candidate.

## Future rule contract

Each eventual `CM-RULE-<subject>-NNN@vN` record must specify:

1. Rule identity/version, source-state version and admissible temporal interval.
2. Preconditions, situational triggers and available/perceived choices.
3. Applicable social/relationship contexts and interlocutor knowledge.
4. Predicted response or bounded response range; distinguish action, language and inferred motive.
5. Supporting observation IDs, source witnesses and exact page/panel/balloon locators.
6. Material counterexamples and known failures, not only confirming scenes.
7. Plausible alternative explanations and what distinguishes them.
8. Confidence, evidence coverage and applicability limits.
9. Falsification conditions and a discriminating test where feasible.
10. Explicit abstention/nonprediction conditions.

Rules must explain characteristic poor decisions and failed repairs as well as successful behavior. Unsupported precision, absolute always/never claims and confident motive attribution are defects even when a generated scene sounds persuasive. Version revisions through claim history; preserve prior rule/test identities.

## Unfamiliar scenarios and cross-series transfer

A scenario declaration must fix the source-state version, what the subject knows, commitments/attachments, familiar versus unfamiliar interlocutor and relationship history, retained setting constraints, whether original leverage/information asymmetries exist, and assumptions introduced solely for the hypothetical. Mark introduced facts separately from canon. Generated scenarios remain noncanonical and never become evidence for a rule.

Do not transfer intimate-partner conduct automatically to strangers. Manipulation evidenced under a particular unequal relationship cannot establish a universal disposition to manipulate. Test transfer separately for ordinary conversation, mundane social interaction, romance, conflict, ethical deliberation, professional/native-setting conduct and other evidenced domains. Humor/play and interiority require their own basis if claimed. Record evidence-backed limitations separately from missing evidence: lack of a professional scene is a gap, not proof of inability.

## Readiness and validation

Local stages distinguish `NOT_ASSESSED`, evidence gathering, a proposed model, and validated-for-a-declared-domain. These are project workflow descriptions, not global capability grades. Monograph and model readiness have separate ledger columns; neither inherits the other's state.

Before a model proposal, audit repeated decisions, temporal snapshots, relationship contrasts, written-register evidence, contradictory choices and missing contexts. Candidate subjects need no predetermined scene count; evidence must discriminate the claimed response range. A single rich scene cannot establish broad portability. Record unsupported dimensions as gaps and abstain.

Future validation proceeds as follows:

1. Freeze exact rule versions and test protocol with the source/knowledge boundary and evidence set. Distinguish observed test material from genuine uninspected holdouts. Declare prior exposure.
2. Build source-derived cases with preconditions and permissible knowledge. Reserve later units as prospective holdouts when possible and record predictions before access. Reread tests of already known scenes are retrospective consistency tests.
3. Evaluate actual response against the originally specified range and discriminators. Log support, failure, mixed result, non-discriminating outcome, unobserved outcome and abstention separately; record temporal/context mismatch.
4. Preserve every failure and material counterexample. Revise rules and affected claims through versioned history; a revised rule cannot inherit a predecessor's success count without a new test.
5. Review transferred analytical work independently under the handoff contract: verify full outputs, hashes/base, actual source access, knowledge restrictions and representative high-impact claims. Agreement between sessions is not independent source evidence.
6. Report literary understanding and behavioral prediction separately, by domain and source boundary. No fabricated holdout results, accuracy figures or blanket simulation-ready status. Any metric must name the tested set, denominator, scoring rule and limitations.

Global discovery, evidence curation, capability assessment and currentness checks remain with their authorized processes. If a future assessment is requested, use their exact discovery-subject binding, reviewed evidence union, immutable basis commit, evidence-set hash and staleness rules; project-local labels cannot bypass calibration or owner promotion. At bootstrap all domains remain **NOT_ASSESSED**, with no model or test result.
