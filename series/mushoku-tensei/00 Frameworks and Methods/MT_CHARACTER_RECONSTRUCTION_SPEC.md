---
title: "Mushoku Tensei - Character Reconstruction Specification"
artifact_id: "MT_CHARACTER_RECONSTRUCTION_SPEC"
artifact_type: "character_reconstruction_specification"
series: "Mushoku Tensei"
generation: "V1"
version: "1.0"
status: canonical
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
do_not_use_as_literary_evidence: true
created: "2026-09-25"
design_reference_commit: "a2a1ab9a5ecd0512a5ac460c1b79655af1bca0bd"
adopted_on: "2026-09-25"
adoption_basis_commit: "a2a1ab9a5ecd0512a5ac460c1b79655af1bca0bd"
canonical_home: "series/mushoku-tensei/00 Frameworks and Methods/MT_CHARACTER_RECONSTRUCTION_SPEC.md"
source_boundary: "Accepted bootstrap method or template; no sequential novel readings or validated character models as of adoption."
recommended_reasoning_class: "DEEP_SYNTHESIS"
---

# Character reconstruction specification

## 1. Objective

A usable reconstruction predicts a constrained range of responses at a specified story state. It is not a collection of catchphrases, a moral verdict, or a claim that a fictional person has a uniquely recoverable hidden mind.

Use:

`identity + continuity + state + knowledge + relationship + context + stakes -> appraisal -> competing goals -> decision -> behavior -> speech`

Start from psychology and constraints, not dialogue imitation. Every model must exclude some responses, acknowledge plausible alternatives, and show where evidence becomes thin.

## 2. Identity and version boundary

Resolve an already enrolled entity/analysis subject against the live global registry. Before enrollment, use explicitly project-local keys and leave global IDs null. Never invent a global subject or write the curation-owned files.

Model the Japanese LN subject first. A WN counterpart, adaptation incarnation, or hypothetical future self is not silently the same model. A temporary mood, ordinary developmental transition, or disguise does not automatically create a new global subject. Distinguish literary identity questions from metadata identity decisions.

Every model states source witnesses, actual admitted coverage, latest incorporated checkpoint/commit, story-time applicability, excluded witnesses, and prior-knowledge limitations. Evidence availability through V10 does not mean every state variable changed in V10.

## 3. Canonical character package

| Artifact | Responsibility |
|---|---|
| `CHARACTER_MONOGRAPH.md` | Substantial literary/psychological explanation of the person, development, relationships, contradictions, voice, and narrative function. |
| `RECONSTRUCTION_MODEL.md` | Current operational rules, applicable states, response ranges, negative constraints, and validation. |
| `EVIDENCE_INDEX.md` | Curated routes from claims/rules/context domains to canonical volume observations and ledger events. |
| `STATE_HISTORY.md` | Optional focused navigation through complex observed state history; links to the shared state ledger rather than owning a competing chronology. |

The monograph must explain the model's central mechanisms and important limits, not merely provide a link. The detailed rules remain owned by the reconstruction model. A monograph may challenge them; accepted changes propagate back to the model and claim ledger.

Do not create separate CLOUD, LOCAL, and FINAL models. Preserve artifact identities across sessions. A generated scenario is a test/output, never a new source about the character.

## 4. Required explanatory domains

A substantial model addresses the following through evidence or explicit uncertainty:

| Domain | What to reconstruct |
|---|---|
| Self-concept | Desired/feared self, explicit self-theory, and discrepancy from behavior. |
| Attention/appraisal | What the character notices, misreads, dismisses, or treats as threatening. |
| Motivation | Immediate wants, durable commitments, less-conscious needs, and competing priorities. |
| Emotion/regulation | Escalation, expression, avoidance, recovery, disclosure, shame, anger, humor, and control. |
| Knowledge | What is known, falsely believed, suspected, hidden, forgotten, or attributed to others. |
| Agency/competence | Initiative, refusal, help-seeking, skill, practical limits, and available resources. |
| Social roles | Differences across family, peers, strangers, authority, work, intimacy, care, and conflict. |
| Relationships | Person-specific trust, obligations, vulnerability, rivalry, dependency, and repair. |
| Ordinary life | Conversation, chores, food/leisure preferences when evidenced, boredom, courtesy, small frustrations. |
| Written speech | Register, address, directness, hedging, teasing, turn-taking, silence, repair, and internal/external differences. |
| Moral cognition | What is recognized as a reason, an excuse, a duty, a limit, or another person's claim. |
| Development | Mechanisms of change, retained tendencies, newly disclosed traits, and regression. |
| Contradictions | Counterexamples, ambivalence, failures of prediction, and unresolved competing accounts. |
| Extrapolation limits | Supported domains, weak analogies, necessary assumptions, and abstention conditions. |

Do not use a fixed list of psychological diagnoses. Traits are explanations to test, not labels that settle behavior. A source can support a narrow observation without supporting a broad personality mechanism.

## 5. State model

```yaml
model_identity:
  local_character_key: null
  character_entity_id: null
  analysis_subject_id: null
  continuity: LN_JP
model_basis:
  witness_ids: []
  admitted_through: null
  basis_commit: null
  model_revision: null
  prior_exposure_limits: []
state:
  state_id: null
  valid_from_observation: null
  valid_until_observation: null
  known_propositions: []
  active_goals_and_commitments: []
  relationship_conditions: []
  material_and_bodily_constraints: []
  persistent_tendencies: []
  changed_features: []
  change_explanation: null
  evidence_refs: []
  uncertainty: null
```

Use change labels such as `DISPOSITION_CHANGE`, `KNOWLEDGE_CHANGE`, `RELATIONSHIP_CHANGE`, `CONTEXT_CHANGE`, `REVEALED_NOT_NEW`, and `UNRESOLVED`; several may apply. A response that differs under a different threat is not necessarily a developmental change.

Chronology must be evidence-based. Preserve uncertain ages or conflicting anchors instead of forcing precision. Use a separate knowledge state for each participant; the analyst's knowledge is not automatically theirs.

## 6. Rudeus-specific controls

Keep physical age, elapsed second-life time, first-life remembered biography, self-attributed age, social treatment, and observed maturity distinct. Treat embodiment effects as claims to test, not predetermined excuses or proof of unchanged adult psychology.

Compare self-criticism with actual restraint, repair, persistence, and treatment of others. Do not model him only as a perpetrator, only as a victim of his earlier life, only as a successful adventurer, or only as a family member. The source must decide the relations among these dimensions.

Track sexual desire, conduct, consent recognition, entitlement, and moral understanding separately. Never generate sexualized scenarios involving minors as a model-validation task. Use non-graphic choice summaries and boundary/authority tests when investigating those dimensions.

The same separation of desire, action, social role, and self-account applies to other characters; Rudeus does not get a uniquely forgiving or uniquely hostile evidentiary standard.

## 7. Behavioral rules

```yaml
rule_id: null
applicable_state_ids: []
trigger_and_context: null
interlocutor_or_relationship_class: null
knowledge_required: []
likely_appraisal: null
motives_in_conflict: []
response_range: []
inhibitors_and_escalators: []
speech_constraints: []
negative_constraints: []
plausible_alternatives: []
supporting_evidence: []
counterevidence: []
discriminating_observation: null
evidence_distance: null
confidence_and_basis: null
validation_refs: []
```

A rule like 'cares about family but may act differently under stress' is too elastic by itself. Specify which perceived threat, which obligation, whose welfare, what tradeoff, and what evidence would contradict the proposed mechanism. Do not invent numerical thresholds.

One distinctive scene can justify a narrow rule. Broad invariants require support across genuinely different situations. Repeated quotations of one episode are not independent corroboration.

## 8. Relationship conditioning and autonomy

Model A->B and B->A separately. Distinguish affection, attraction, dependency, loyalty, obligation, idealization, instrumental reliance, and mutual understanding. A character's interpretation of another person may be wrong.

Record public/private differences, safe/unsafe subjects, forms of address, teasing boundaries, help offered/accepted, conflict and repair, and what the relationship activates in each participant. Do not make all interlocutors interchangeable.

For less-focalized people, write the minimum warranted interpretation before proposing hidden motives. Romance or caregiving can be a chosen commitment; neither is automatic evidence of passivity. Conversely, asserting that a choice is voluntary does not settle structural dependency or the range of available alternatives.

## 9. Speech and embodiment

Separate interior diction from spoken dialogue and polite self-presentation. Preserve language-specific evidence for pronouns, honorifics, forms of address, register, and turns of phrase. Translated examples must be labeled and cannot support unobserved Japanese constructions.

A novel-only model has written-speech evidence, not actor timbre or acoustic prosody. Later voice work needs a separately scoped audiovisual witness. Illustrations can inform visual presentation only to their inspected scope. Do not import canonical anime appearance or gestures from memory.

In invented dialogue, prioritize what the person would disclose and attempt over stereotyped verbal tics. Do not make ordinary interactions sound like an analytical monograph or a therapy session. A character is not aware of the discourse hypotheses used to study them.

## 10. Readiness by domain, not a single score

Use local operational states: `UNASSESSED`, `INSUFFICIENT_EVIDENCE`, `BOUNDED_PROVISIONAL`, and `DOMAIN_READY`. These are **not** global registry capabilities or artifact authority statuses.

A readiness record names the supported context and state, coverage, counterexamples, tests, and limits. For example, ordinary family interaction may be better supported than unfamiliar diplomacy; written Japanese speech may be better supported than contemporary English slang. No character should become generically 'fully simulated' because a monograph is long.

Before `DOMAIN_READY`, require a coherent rule set, relevant ordinary behavior, relationship conditioning, at least some diagnostic counterevidence review, and a validation route appropriate to the claimed scope. Keep unavailable contexts unknown.

## 11. Validation protocol

Use several distinct tests:

**Source reproduction:** Given only the preceding eligible state, can the model account for an observed decision without using the later event as an input? This is stronger when the target was actually withheld; otherwise label it retrospective fitting.

**Contrast tests:** Give comparable situations with different interlocutors or stakes. The model should explain both differences and continuities rather than emit one generic personality.

**Prospective tests:** Freeze a bounded expectation before opening the next eligible source. Specify the opportunity needed for a real test. No relevant opportunity means `UNTESTED`, not success.

**Negative constraints:** Identify plausible-looking but unsupported behaviors that the model should resist, including later-knowledge leakage, out-of-state maturity, and fashionable therapeutic vocabulary.

**Ordinary-life tests:** Use mundane conversation, an inconvenient request, mild embarrassment, disagreement, or practical coordination. Do not make every test a catastrophe.

**Out-of-domain tests:** State the counterfactual assumptions and tolerate multiple plausible responses. These assess coherence, not canonical truth.

Model pretraining/familiarity may contaminate nominal holdouts. Record this limitation; a fresh chat is not a guaranteed blinded test. Generated scenarios never feed back as evidence. A good fit to remembered canon is not proof of predictive accuracy.

## 12. Evidence distance and scenario contract

Use `D0 DIRECT`, `D1 NEAR_ANALOG`, `D2 STRUCTURAL_ANALOG`, `D3 EXTRAPOLATED`, and `D4 SPECULATIVE` as qualitative descriptions. Greater distance should yield less specificity and more explicit alternatives, not invented probabilities.

Every substantial scenario specifies character/state, continuity, participants and relationship knowledge, premise changes, stakes, relevant rules, negative constraints, evidence distance, and uncertainties. If the scenario moves someone into a modern setting, state how language, technology, institutions, and information are supplied. Do not casually grant knowledge that the source never gives them.

A user-requested adult counterfactual is a declared altered premise, not evidence that the source character has a demonstrated adult developmental history. Age changes do not silently rewrite every psychological variable.

## 13. Revision and acceptance

Update rules through targeted edits, preserving IDs, rejected alternatives, tests, and state history. A failure can expose missing knowledge, wrong relationship conditioning, an overly broad rule, or a genuine source contradiction. Do not rescue every rule by adding exceptions until nothing could falsify it.

A mature monograph is accepted only if it makes a sustained explanatory argument, includes material state transitions and counterreadings, gives source-bearing ordinary behavior, explains the operational model, and states evidence limitations. A model is accepted separately for the domains its rules and tests support.

The character curation agent decides discovery enrollment under the live repository policy. Local readiness does not create permission to edit the global registry or claim a new global capability.
