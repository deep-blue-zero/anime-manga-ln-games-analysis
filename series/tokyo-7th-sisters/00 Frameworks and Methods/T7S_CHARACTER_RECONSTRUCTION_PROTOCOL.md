---
title: "Tokyo 7th Sisters — Character Reconstruction Protocol"
artifact_id: T7S_CHARACTER_RECONSTRUCTION_PROTOCOL
artifact_type: character_reconstruction_protocol
series: Tokyo 7th Sisters
generation: V1
version: "1.0"
status: canonical
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
do_not_use_as_literary_evidence: true
source_boundary: "c20260909-r484; preserved offline Japanese game; no sequential analysis consumed"
architecture_lifecycle: INITIAL
created: 2026-09-09
last_updated: 2026-09-09
---

# Tokyo 7th Sisters character reconstruction protocol

Current route: [CURRENT_STATE_AND_CORPUS_MAP.md](../CURRENT_STATE_AND_CORPUS_MAP.md). Governing pair: [T7S_ANALYTICAL_METHOD.md](T7S_ANALYTICAL_METHOD.md) and [T7S_SYNTHESIS_ARCHITECTURE.md](T7S_SYNTHESIS_ARCHITECTURE.md). Source recovery: [T7S_EVIDENCE_SUBSTRATE_AND_LOCATOR_PROTOCOL.md](T7S_EVIDENCE_SUBSTRATE_AND_LOCATOR_PROTOCOL.md).

Section letters retained from the approved design are cross-document references: E/P = [source and locator protocol](T7S_EVIDENCE_SUBSTRATE_AND_LOCATOR_PROTOCOL.md); F = [topology](../01%20Sources%20and%20Chronology/T7S_TOPOLOGY_AND_CHRONOLOGY.md); G/H/I/N/O = [reading method](T7S_ANALYTICAL_METHOD.md); J/K/M/R/S/U/X/Y/Z = [synthesis architecture](T7S_SYNTHESIS_ARCHITECTURE.md); L = [reconstruction protocol](T7S_CHARACTER_RECONSTRUCTION_PROTOCOL.md) (monograph promotion is owned by the synthesis architecture); V/T = [bootstrap and gate record](../09%20Audits%20and%20Manifests/T7S_BOOTSTRAP_AND_GATE_RECORD.md). B01–B13 identify the architecture’s bootstrap inventory, not source IDs.

## L. Character reconstruction architecture

`T7S_CHARACTER_RECONSTRUCTION_PROTOCOL.md` is a day-one governing method because later source selection must gather ordinary-life and counterexample evidence deliberately.

**Interface:** `(analytical subject, witness, developmental state, known/remembered history, recipient and relationship state, role/resources, public/private/stage mode, stakes/pressure)` → `noticed features → active goals/value conflict → decision → conduct → speech`, with confidence, evidence routes, alternatives, and abstention conditions.

| Component | Required constraint |
| --- | --- |
| Invariants and variables | Candidate invariant needs contrasting contexts; record developmental and relationship-specific exceptions |
| State selection | Explicit default state and allowed alternatives; no unmarked “all-era” personality |
| Knowledge | Event-indexed acquisition and beliefs; later revelations do not become earlier knowledge |
| Social context | Private familiarity, fan-facing persona, management, peers, stage, and creative/professional roles may activate different policies |
| Behavioral repertoire | Ordinary/low stakes, social conflict/medium stakes, crisis/high stakes, initiative, refusal, coping, repair, and mundane competence |
| Speech | Native Japanese register, address, turn-taking, lexical habits, situational changes; translation remains an attributed aid |
| Performance | Linguistic model may mature before performed/embodied voice; capability boundaries remain explicit |
| Rules | Trigger + state → perception/priority/action, with support, rival explanation, counterexample, and failure conditions |
| Output | Source-supported reconstruction versus extrapolation; uncertain or unsupported inputs prompt abstention or a bounded alternative |

**Local readiness states** (not global registry scores):

| State | Entry/exit criterion |
| --- | --- |
| `R0_UNRESOLVED` | Identity or witness/state assignment insufficient |
| `R1_INDEXED` | Evidence routes exist; no behavioral adequacy claim |
| `R2_STATE_BOUNDED` | At least one grounded state and relevant scene/context coverage; substantial gaps explicit |
| `R3_RULE_CANDIDATE` | Conditional rules, ordinary-life evidence, contrasting recipients/stakes, rivals, and negative controls are present |
| `R4_VALIDATED_WITH_BOUNDS` | Fidelity/counterexample tests pass for named states and domains, with explicit unsupported domains |
| `R5_MAINTAINED` | R4 model has undergone later-source revision, regression checks, and current-horizon reconciliation |

Store the R0–R5 state in `reconstruction_readiness`: it describes source-grounded conditional behavioral reconstruction. Store `monograph_maturity` separately: it describes the completeness of the integrated interpretive monograph. Neither is a sum of modality scores, and neither changes repository authority metadata or the sequential-analysis lock.

Track separate capability fields: `textual_characterization`, `japanese_linguistic_voice`, `performed_voice`, `visual_identity`, `embodied_presentation`, `stage_identity`, `relationship_coverage`, `ordinary_life_coverage`, and `chronology_coverage`. Each records scope, review/coverage status, exact evidence routes and limits; unreviewed, insufficient-source, and justified non-applicable cases remain explicit. Do not make AV a universal ordinal veto on R0–R5 or claim that high text readiness implies vocal fidelity. The mandatory visual/voice review for monograph maturity is a separate promotion rule.

For example, an `R4_VALIDATED_WITH_BOUNDS` behavioral model may coexist with `MONOGRAPH_READY_TEXTUAL` because performed voice remains unreviewed. Conversely, `MONOGRAPH_MATURE` may coexist with `R3_RULE_CANDIDATE` for extreme-domain behavioral prediction. No automatic promotion occurs between these dimensions.

A **monograph** may be created at `MONOGRAPH_READY_TEXTUAL` under the separate promotion rules in the synthesis architecture; it must not be labeled fully mature until `MONOGRAPH_MATURE`. A **reconstruction model** is earned at R3 when an independently reusable behavioral interface and falsifiable rules exist; usable validated status requires R4 tests. A bounded model may cover one era/state rather than wait for all franchise material.

Ordinary-life evidence is mandatory for general behavior readiness. Build an eligible pool from complete Sub/Event envelopes and condition-bearing card/character messages. Include teasing, annoyance, help, leisure, casual address, low-stakes conflict, and conversational initiative where available. Preserve examples that resist the preferred characterization. Missing ordinary-life evidence limits the model to its evidenced domains; it is not repaired with generic idol archetypes.

Evidence distance: `D0` direct observed action/wording; `D1` close same-state contextual generalization; `D2` tested cross-context rule; `D3` bounded novel situation or incomplete state; `D4` substantial unsupported extrapolation. D3 requires conspicuous uncertainty; D4 normally abstains. No numerical probability is required without calibration data.

First mature model and material revisions require adversarial fidelity review: recipient swaps, era/knowledge swaps, public/private/stage swaps, stakes changes, ordinary-life tasks, anti-archetype cases, and unknown-input tests. Keep held-out cases from rule fitting; report retrospective testing honestly when a case was already seen. Outcomes: `PASS`, `PASS_WITH_BOUND`, `NEEDS_TARGETED_SOURCE_REVIEW`, or `INSUFFICIENT_EVIDENCE`.



## Model artifact and revision contract

A candidate model at R3 records subject identity and witness, default developmental/epistemic state, allowed state alternatives, evidence coverage, input contract, conditional rules, counterexamples, unsupported domains, and output/abstention behavior. Each rule has a stable ID, trigger, state guard, perception/priority/action/speech prediction, supporting and contrary locators, evidence distance, rival explanation and falsifying observation. Output separates directly supported reconstruction from extrapolation.

Validation fixes the model version and fit/held-out memberships before running tests. Record each scenario, input-state provenance, expected source constraints, produced behavior, failure type, claim repair and scope change. No test fabricated from the fitted rule is independent confirmation. Do not claim held-out testing for already seen cases. Retest every affected rule after new evidence or broader scope; retain earlier bounded releases and failed cases.

The entity ledger owns identity and the current readiness decision until a documented responsibility transfer. Promotion to an independent reconstruction model does not create a global character registry row or assign a repository-wide score. Monograph maturity follows the synthesis architecture and is never inferred from R0–R5.
