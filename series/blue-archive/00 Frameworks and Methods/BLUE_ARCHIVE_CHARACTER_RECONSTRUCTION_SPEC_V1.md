---
series: BLUE_ARCHIVE
artifact_type: character_reconstruction_specification
scope: PROJECT_LOCAL_RECONSTRUCTION_DESIGN_AT_MAIN_V001_C002
generation: V1
version: "1.1"
status: canonical
source_boundary: "Method/specification only; no character capability is certified. Design basis: canonical Prologue plus MAIN_V001_C001 and MAIN_V001_C002 through BA:main:001:002:020; BA:main:002:001:001 and later main-story narrative remain unopened"
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
do_not_use_as_literary_evidence: true
created: 2026-09-25
updated: 2026-09-25
canonical_home: "series/blue-archive/00 Frameworks and Methods/BLUE_ARCHIVE_CHARACTER_RECONSTRUCTION_SPEC_V1.md"
governing_method: BLUE_ARCHIVE_ANALYTICAL_METHOD_V1.md
governing_architecture: BLUE_ARCHIVE_SYNTHESIS_ARCHITECTURE_V1.md
current_checkpoint: MAIN_V001_C002
next_unopened_main_unit: BA:main:002:001:001
recommended_reasoning_class: DEEP_SYNTHESIS
---

# BLUE ARCHIVE CHARACTER RECONSTRUCTION SPECIFICATION V1
## Source-bounded behavioral models, validation, and hypothetical-use controls

## 0. Purpose and present disposition

This specification defines how the Blue Archive project may later reconstruct a character's perception, appraisal, motive conflict, choice, action, speech, and relationship-conditioned behavior at an explicit story state.

The target is not a personality summary and not unrestricted role-play. It is a **source-bounded, time-indexed, domain-specific model** that can answer:

> Given this version of the character, with this knowledge, role, relationship, audience, pressure, and material constraint, which response families are well supported, which alternatives remain plausible, and where must the model abstain?

This document creates the project-local contract only. It does not create a character reconstruction model, freeze a prospective prediction, assign a global capability grade, or inspect the next unopened story unit. The current evidence boundary is the canonical Prologue plus Chapters 1–2 of Volume 1 through `BA:main:001:002:020` and the canonical `MAIN_V001_C002` checkpoint. The recovered analytical basis is Git commit `533a7c7253f6cbea8616518abdc37076f604d3c5`; the audit records reconciliation with the previously published C001 design.

## 1. Responsibility and authority boundary

The reconstruction layer has one responsibility: compile already admitted evidence and accepted analysis into conditional operational rules for bounded extrapolation.

It does not replace any of the following:

| Layer | Owning responsibility |
|---|---|
| Canonical Japanese source | What the represented text/data actually contains. |
| Sequential deep reading | What becomes legible at one local source boundary without later hindsight. |
| Longitudinal ledger | How evidence, claims, states, relationships, institutions, and wording accumulate and change. |
| Checkpoint or literary specialist | What the work means, how character and narrative causality operate, and which interpretation currently governs. |
| Reconstruction model | Which conditional behavioral and speech inferences the admitted evidence supports. |
| Validation record | How a frozen rule or prediction performed under a fair later or withheld test. |
| Hypothetical application | A downstream scenario output that can illustrate model use but never becomes evidence. |

Evidence flows downward. Correction flows back by reopening canonical evidence and revising the appropriate analytical owner. A generated scene, invented line, crossover interaction, or model-consistent answer can never flow upward into a deep reading, ledger, monograph, or source claim.

The global discovery and capability layers remain separate. This project must not edit or populate:

```text
characters/registry.jsonl
CHARACTER_ANALYSIS_INDEX.md
characters/CHARACTER_ANALYSIS_INDEX.md  # Also prohibited if this alias is ever introduced.
characters/reconstruction_capabilities.jsonl
characters/CHARACTER_RECONSTRUCTION_INDEX.md
```

Project-local readiness uses the vocabulary in section 15 and does not mint repository-wide A–E grades.

## 2. Model identity and source state

Every model must identify the represented person, continuity, source witnesses, story-time boundary, analytical checkpoint, and excluded knowledge. A playable variant, costume, mood, or ordinary developmental phase does not automatically create a separate person.

Use an existing reviewed global entity or subject ID only when one already exists. Otherwise use a visibly project-local key; do not invent global registry enrollment.

```yaml
model_identity:
  artifact_id: null
  local_character_key: null
  preferred_name: null
  character_entity_id: null
  analysis_subject_id: null
  continuity: BLUE_ARCHIVE_JP_GAME
model_basis:
  admitted_source_classes: []
  admitted_main_units: []
  pinned_source_witnesses: []
  narrative_time_boundary: null
  chronology_confidence_and_basis: null
  excluded_evidence: []
  known_prior_exposure_limitations: []
  basis_checkpoint: null
  basis_commit: null
  model_revision: null
  excluded_later_knowledge: []
  unresolved_source_anomalies: []
coverage:
  observed_contexts: []
  missing_contexts: []
  ordinary_life: null
  written_japanese: null
  performed_voice: NOT_ADMITTED
local_readiness: UNMODELED
```

`basis_commit` names an existing input snapshot. It is never a fabricated hash of the model itself. The model must route load-bearing claims through the current literary/checkpoint authority and then to stable Blue Archive evidence IDs.

## 3. Temporal and contextual state

A source-unit boundary is not automatically a new character state. Create a distinct state only when a changed configuration materially alters the response rules.

Every state difference must be classified using one or more of:

- `DISPOSITION_CHANGE` — a durable behavioral or value tendency changed;
- `KNOWLEDGE_CHANGE` — the character learned, forgot, or revised a proposition;
- `RELATIONSHIP_CHANGE` — trust, standing, obligation, intimacy, rivalry, or permission changed;
- `CONTEXT_CHANGE` — the same disposition operates differently because the setting, audience, stakes, or task changed;
- `ROLE_CHANGE` — institutional, team, professional, or command position changed;
- `RESOURCE_CHANGE` — money, equipment, information access, health, time, or other practical capacity changed;
- `REVEALED_NOT_NEW` — later access reveals a feature already present rather than causing it;
- `UNRESOLVED` — current evidence cannot distinguish change from revelation or context.

```yaml
state_id: null
label: null
valid_from_source: null
valid_until_source: null
change_types: []
entry_conditions: []
self_model: null
active_goals: []
known_propositions: []
false_or_uncertain_beliefs: []
relationship_conditions: []
role_conditions: []
resource_conditions: []
persisting_features: []
changed_from_previous: []
evidence_refs: []
uncertainties: []
```

Later knowledge must not leak backward. Earlier uncertainty also must not be rewritten as though the audience or character always knew the later answer.

## 4. Required model domains

A substantial model addresses each domain with evidence, bounded inference, or an explicit gap. The sections need not be equally long.

| Domain | Required content |
|---|---|
| Core self-model | Explicit self-conception, desired and feared self, public identity, evidenced private identity, self-report/conduct gaps, performed personas, and the costs of maintaining them. |
| Motivational architecture | Immediate wants, recurring needs, commitments, loyalties, protected values, fears, status concerns, institutional duties, relationship obligations, and what tends to win when these conflict. |
| Attention and appraisal | What becomes salient first; what is missed; how evidence, threat, status, care, shame, opportunity, and uncertainty are interpreted. |
| Decision policy | How perception becomes options, inhibition/escalation, choice, action, and later self-account. |
| Emotional regulation | Triggers, expression, concealment, displacement, escalation, avoidance, rumination, embarrassment, anger, fear, recovery, and disclosure, with audience/relationship/state differences. |
| Directed relationship conditioning | A-to-B trust, knowledge, standing, obligations, vulnerabilities, expectations, deference, rivalry, care, boundaries, refusal, misunderstanding, public/private differences, and updating conditions. |
| Institutional conditioning | School/club/committee office, command hierarchy, public duty, jurisdiction, factional pressure, scarcity, inter-academy politics, and Schale/Sensei standing; role is not private preference. |
| Agency and competence | Initiative, practical capacity, delegation, help-seeking, refusal, correction, persistence, and domain-specific failure modes. |
| Ordinary-life repertoire | Mundane conversation, food, hobbies, leisure, work, shopping, study, small favors, compliments, teasing, awkward introductions, routine disagreement, rest, humor, and play where evidenced. |
| Crisis repertoire | Distinguish ordinary disagreement, embarrassment, institutional conflict, physical danger, coercion, perceived betrayal, and existential threat. Slapstick and combat are not universal interpersonal baselines. |
| Japanese written speech | Self-reference, address/honorifics, politeness and plain/polite shifts, sentence-final forms, stylization/dialect, hesitation, self-correction, interruption, directness and speech acts. Distinguish represented spoken dialogue from written messages and preserve context/relationship shifts. |
| Contradictions and negative constraints | Strong counterexamples, caricature traps, evidence-backed non-rules, and hypotheses the source does not support. |
| Qualitative thresholds | Conditions under which the response family changes, without invented numeric cutoffs. |
| Development | What changed, what persisted, what was newly revealed, and why the distinction matters. |
| Counterfactual envelope | Supported scenario domains, required assumptions, scenario distance, plausible alternatives, and abstention zones. |
| Limits and confidence | Source gaps, access asymmetry, mapping anomalies, chronology uncertainty, localization limits, and demonstrated model failures. |

## 5. Decision-path contract

A behavioral explanation should normally expose the following path when evidence permits:

```text
perception
  -> attention
  -> appraisal
  -> affective response
  -> motives in conflict
  -> inhibitors / escalators
  -> perceived options
  -> choice and observable action
  -> immediate aftermath
  -> later self-account or repair
```

The path is diagnostic, not a demand to invent invisible interiority. If the source supplies observable action but not appraisal, mark the appraisal `OPEN` or present competing hypotheses. If the source supplies represented thought, do not assume the character would verbalize it.

## 6. Behavioral rule schema

Use stable project-local rule IDs such as `BA-ARU-R001`. An ID provides retrieval stability, not global enrollment.

```yaml
rule_id: null
rule_label: null
scope_state_ids: []
trigger_or_situation: null
source_domains: []
relationship_conditions: []
audience_conditions: []
role_conditions: []
character_knowledge_required: []
salient_attention: []
likely_appraisal: null
likely_affect: []
motives_in_conflict: []
inhibitors: []
escalators: []
perceived_options: []
likely_internal_response: null
likely_external_action_range: []
aftermath_and_self_account: []
written_speech_constraints: []
alternatives: []
supporting_evidence: []
counterevidence: []
evidence_gaps: []
disconfirming_observation: null
claim_class: WORKING_HYPOTHESIS
confidence: null
validation_refs: []
last_material_revision: null
```

Allowed `claim_class` values are:

- `DIRECT_BOUNDED_PATTERN` — the source directly demonstrates the conditional pattern in its stated scope;
- `REPEATED_BEHAVIORAL_PATTERN` — materially different occasions support a recurrence;
- `RELATIONSHIP_CONDITIONED_PATTERN` — recurrence belongs to a named directed relation or relation class;
- `STATE_DELTA` — the rule is a bounded departure from baseline under a known state;
- `STRONG_INFERENCE` — several independent evidence routes converge without direct statement;
- `WORKING_HYPOTHESIS` — plausible and useful but underdetermined;
- `OPEN` — retained for inquiry and not usable as a prediction rule;
- `NEGATIVE_CONSTRAINT` — evidence constrains a caricature or overgeneralization.

A useful rule excludes something. A rule broad enough to explain every possible response is descriptive padding. One distinctive scene may support a narrow rule; it does not license unrestricted transfer.

## 7. Attention, appraisal, and motive conflict

Trait labels are insufficient. `impulsive`, `kind`, `lazy`, `loyal`, `professional`, or `villainous` must be unpacked into a conditional mechanism.

For each material rule ask:

1. What did the character notice first?
2. What relevant information did they ignore, lack, or distrust?
3. What did the situation mean to them?
4. Which identity, relationship, institutional, ethical, or material motives competed?
5. Which inhibition failed or succeeded?
6. Which options were genuinely available from the character's perspective?
7. What did the character do, and how did they later interpret or repair it?
8. What did the character assume about another person's intent and knowledge, and what evidence would make that social reading update?

Where the answer is only inferential, record alternatives. A later consequence does not prove a prior motive.

## 8. Directed relationships and institutional conditioning

Relationship evidence is directional. `A -> B` and `B -> A` are separate records. A model must not assume that care, trust, knowledge, or permission is symmetric.

For major relations record:

```text
character -> interlocutor | state | public/private | institutional relation |
knowledge asymmetry | expected reciprocity | dominant speech acts |
behavioral deltas | permissions/taboos | exceptions | evidence | confidence
```

Blue Archive also requires an institutional condition for many rules. A character's school, club, office, mission, debt, territorial standing, or chain of command may alter attention and available choices without exhausting personal motivation. Institutional role is neither proof of sincere agreement nor a disposable costume.

## 9. Ordinary life as a control sample

Ordinary-life evidence is a first-class validation control. Seek, where the admitted source supplies it:

- one low-stakes group interaction;
- one low-stakes dyadic interaction;
- one work, study, food, travel, leisure, or household routine;
- one minor disagreement, refusal, joke, embarrassment, irritation, or act of care;
- one transition into or out of crisis for comparison.

Missing ordinary evidence narrows readiness. Do not invent favorite foods, hobbies, domestic competence, money habits, romantic fluency, or relaxed conversation from costume, metadata, archetype, or one contextual line.

At the current Chapter 2 boundary, Serika's work/ramen/money routine and the Problem Solver 68 restaurant/scarcity material are especially valuable but remain narrow samples. They do not make any subject whole-person ready.

## 10. Written Japanese and performed voice

The current corpus supports a **written-Japanese speech model**. It may use canonical dialogue and choice records to study:

- self-reference, address, honorifics, sentence-final forms, stylization, and evidenced dialect;
- honorific accommodation and role titles;
- directness, hedging, qualification, interruption, and repair;
- command, request, refusal, apology, gratitude, teasing, complaint, and reassurance;
- sentence/turn length and represented typographic emphasis;
- public/private, relationship, institutional, and stress deltas.

Do not infer performed delivery—pitch, timbre, pace, breath, pause, loudness, or acting—from the transcript. If voice audio or a performed adaptation is later admitted, it requires a separate performance layer with its own source lock, identity mapping, inspection method, and divergence notes. Performed voice may enrich delivery; it may not overwrite canonical wording or literary ambiguity.

The [Japanese voice/address ledger](../03%20Longitudinal%20Ledgers/BLUE_ARCHIVE_JAPANESE_VOICE_AND_ADDRESS_LEDGER.md) owns attested textual examples and their source cautions. Written-message rhythm is not performed prosody, and a disputed speaker cannot supply a secure idiolect example.

Generated Japanese must be labeled illustrative. It is never a recovered line and must not be stored as a canonical voice example.

## 11. Source-class admission rules

### 11.1 Main story

Main story remains the sequential literary spine. New main units enter prospectively under the no-hindsight gate. Reconstruction deltas are recorded only after the literary reading has established source meaning.

### 11.2 Group and event stories

Use complete stories, not extracted quotes alone. Record publication/source order, story-local chronology, event-specific roles, audience, and continuity uncertainty. An event costume or temporary office does not automatically define baseline behavior. Release order is not a complete in-universe chronology. Record chronology confidence and its basis: an uncertainly placed event can establish contextual repertoire without proving when it was acquired. Do not create a state-transition edge until the ordering is supported.

### 11.3 Bond stories and MomoTalk

These are high-value for private presentation, ordinary life, messaging rhythm, dyadic repair, and Sensei-conditioned behavior. They are also structurally player-facing and relationship-specific. Do not generalize a Sensei dyad to peers, public institutions, or romantic certainty without independent support. Preserve the source-class label; private material does not automatically overwrite main-story institutional state, public knowledge, chronology, or other relationships.

### 11.4 Sensei choices

Preserve the full choice space and the shared structural action. Do not treat mutually exclusive options as simultaneously spoken. Distinguish:

- invariant action across choices;
- required narrative participation even when the interface presents a choice;
- optional tone or persona expression;
- branch-conditioned response;
- normalized choice metadata;
- malformed or choice-like text not represented as a formal choice group.

### 11.5 Sensei model

The [Sensei role/ethics ledger](../03%20Longitudinal%20Ledgers/BLUE_ARCHIVE_SENSEI_ROLE_AND_ETHICS_LEDGER.md) remains authoritative for institutional and ethical analysis. Keep invariant narrative agency, bounded selectable persona, structural capacity, and player-variable characterization distinct.

Sensei is a player-variable protagonist with represented structural commitments. A reconstruction may model invariants, choice families, role obligations, and observed effects. It must not average every option into one fully specified private personality or use another character's interpretation as direct Sensei interiority.

### 11.6 Playable variants

Consolidate the person unless the continuity evidence requires separation. Preserve variant-specific setting, role, outfit, event, skill, and dialogue conditions. Variant evidence can demonstrate a contextual repertoire without proving a timeless trait. Gameplay metadata has no automatic narrative force; alternate/special continuity requires positive source evidence, not a costume name.

### 11.7 Generated bundles and chunks

Character, relationship, institution, Sensei, and LLM bundles are retrieval projections. They can improve recall but cannot establish scene order, context, speaker identity, or a behavioral pattern independently of the canonical source object. Machine co-occurrence measures retrieval adjacency, not relationship strength. Consequential behavioral inference must return to the complete canonical source unit and its provenance; bundle excerpts alone cannot certify a rule.

### 11.8 Source anomalies

Quarantined speaker mappings, missing titles, unresolved IDs, truncated convenience renderings, and chronology gaps stay visible. A model may omit a corrupted line, lower confidence, or route to a stronger promoted record. It may not repair the source from memory, localization, wiki, or character stereotype.

## 12. Contradictions, limitations, and abstention

Every limitation uses one of two support kinds:

- `EVIDENCE_GAP` — the source does not supply enough evidence; it requires no supporting evidence reference and must not be rewritten as a negative trait.
- `EVIDENCE_BACKED_LIMITATION` — affirmative evidence constrains a rule, contradicts a caricature, or shows a failure mode; it requires evidence references.

```yaml
limit_id: null
statement: null
support_kind: EVIDENCE_GAP
scope_state_ids: []
evidence_refs: []
effect_on_use: null
```

Examples of invalid reasoning:

- no ordinary-life scene therefore the character has no hobbies;
- sparse speech therefore the character lacks emotion;
- one crisis outburst therefore the character always speaks that way;
- formal office therefore the character personally endorses every institutional act;
- affection toward Sensei therefore identical behavior toward peers;
- a generated scenario sounds plausible therefore the model is validated.

Abstain, or give explicitly conditional alternatives, when the requested state cannot be selected, required character knowledge is missing, chronology changes the answer, no comparable relationship/context is evidenced, a decisive speaker mapping is unresolved, or rival explanations cannot be discriminated. Name the missing evidence or assumption. A requested definite answer does not eliminate these limits.

## 13. Qualitative thresholds and counterfactual distance

Do not invent numerical psychological thresholds. State the conditions that alter the likely response:

- public versus private audience;
- trusted, subordinate, peer, stranger, rival, or authority relation;
- routine, pressured, dangerous, or catastrophic stakes;
- time, money, injury, equipment, and information constraints;
- institutional permission and jurisdiction;
- identity threat, shame, care, reciprocity, or perceived betrayal;
- whether refusal, clarification, or repair remains available.

Use scenario distance:

- `D0_CANON_NEAR` — nearly the same situation class, state, and relation;
- `D1_ANALOGOUS_TRANSFER` — novel event with close canonical pressures and roles;
- `D2_MODERATE_TRANSFER` — important unfamiliar features but relevant mechanisms remain;
- `D3_FAR_TRANSFER` — institutions, technology, intimacy, culture, age, or life experience absent from the evidence.

Confidence normally falls with distance. A strong crisis model can still be unready for a quiet meal, and a strong Sensei dyad can still be unready for a peer romance.

## 14. Scenario-use contract

Every hypothetical application begins with:

```yaml
scenario_id: null
scenario_type: null
character_state_id: null
source_boundary: null
scenario_distance: null
participants_and_relationships: []
setting_and_audience: null
stakes_and_time_pressure: null
role_and_institutional_constraints: []
material_and_bodily_constraints: []
what_each_person_knows: []
canon_changes_introduced: []
unknown_assumptions: []
applicable_rule_ids: []
unsupported_domains: []
```

Output distinguishes:

1. likely attention and appraisal;
2. plausible internal response, where warranted;
3. likely observable action range;
4. likely written-speech/register constraints;
5. meaningful alternative branches;
6. conditions that flip the choice;
7. uncertainty and abstention.

Exact invented dialogue is illustrative, not uniquely predicted. A crossover or transformed-age scenario must state the introduced assumptions; it does not supply the missing developmental history automatically.

## 15. Project-local readiness

Use only:

- `UNMODELED` — evidence is routed, but no operational mechanism is yet asserted for scenario use;
- `PARTIAL_MODEL` — some source-backed mechanisms or rules exist, with substantial unmodeled domains;
- `OPERATIONAL_CANDIDATE` — rule-based scenario work is supportable under named state/domain conditions, but validation remains incomplete;
- `BOUNDED_VALIDATED` — named rules have survived specified prospective or adversarial checks inside an explicit tested envelope. Retrospective consistency alone does not establish this state.

Readiness is domain-specific. Record it alongside the model-artifact state so a distributed partial account is not mistaken for a completed standalone model. No character receives `OPERATIONAL_CANDIDATE` merely for having many appearances, a source bundle, a checkpoint paragraph, or fluent generated dialogue.

Promotion requires, as applicable:

1. traceable load-bearing evidence;
2. explicit source/time state;
3. more than one context or a clearly narrow domain claim;
4. directed relationship conditioning;
5. written-Japanese evidence beyond a slogan;
6. ordinary-life control or an explicit limitation;
7. counterevidence and negative constraints;
8. a stated counterfactual envelope;
9. preserved fair prospective or adversarial results for the named rules/envelope before `BOUNDED_VALIDATED`, with opportunity, exposure, rivals, and remaining failures visible. An inapplicable or unresolved test does not count as support.

Every readiness record includes a domain, state, supporting mechanism/rule routes, model-artifact status, constraints, validation references, and promotion/demotion reason. Assess mundane social interaction, unfamiliar groups, institutional/professional conduct, conflict, ethical decisions, friendship, romance/dating, public performance, crossover, and high-stakes crisis separately when requested. Unsupported domains remain `UNMODELED`; strength in one cannot raise another.

```yaml
domain_readiness:
  - domain: null
    scope_state_ids: []
    readiness: UNMODELED
    mechanism_or_rule_refs: []
    model_artifact: null
    required_assumptions: []
    excluded_transfers: []
    validation_refs: []
    last_change_and_reason: null
```

Readiness can decrease. New counterevidence must narrow or suspend affected rules before further scenario use; preserve the previous decision and failed test instead of averaging them away.

## 16. Validation

### 16.1 Prospective freeze

Before opening a later diagnostic source unit, freeze only a small set of material, discriminating rules. Record:

- exact source and Git basis;
- character state and knowledge boundary;
- triggering conditions;
- expected response family;
- plausible alternatives;
- a response the rule does not predict;
- disconfirming observation;
- which later observation would be a fair test.

Do not rewrite the frozen wording after source exposure. Freeze an actual committed register under `08 Audits and Manifests/BLUE_ARCHIVE_CHARACTER_MODEL_PROSPECTIVE_REGISTER_<BOUNDARY>.md`; a timestamp in mutable prose is insufficient. Identify the register commit/blob, model revision, basis checkpoint, admitted/excluded source IDs, rule IDs, and known prior exposure. Known outcome exposure makes that test retrospective even if later put in a register.

A separate `BLUE_ARCHIVE_CHARACTER_MODEL_ADJUDICATION_<BOUNDARY>.md` links each frozen entry and records the actual observation, canonical locator, opportunity match, outcome, rival explanation, error category, and resulting rule revision. Do not repair the frozen record to match a later model.

### 16.2 Adjudication vocabulary

Use:

- `SUPPORTED_IN_THIS_TEST`;
- `PARTLY_SUPPORTED`;
- `CONTRADICTED`;
- `NO_DIAGNOSTIC_OPPORTUNITY`;
- `CONFOUNDED`;
- `UNRESOLVED`.

Then apply a separate model transition where warranted:

`PRESERVE · STRENGTHEN · REVISE · DOWNGRADE · REJECT · OPEN`

### 16.3 Retrospective and withheld-context checks

A previously read scene can test internal consistency only when labeled retrospective. A bounded evidence packet may withhold a scene or context, but the audit must state exactly what was withheld and whether the analyst had prior exposure. Never call a hindsight-informed test blind.

Useful checks include:

- state contrast;
- relationship switch;
- ordinary versus crisis behavior;
- public versus private register;
- institution/role change;
- choice-space invariance for Sensei;
- leave-one-context-out rule construction;
- cross-model interaction consistency.

### 16.4 Adversarial and negative tests

Test whether the model:

- leaks later knowledge backward;
- gives both sides of a relation the same knowledge;
- treats narrative consequence as proof of motive;
- converts absence into prohibition;
- applies a relationship-specific behavior universally;
- uses crisis register as baseline;
- confuses official role with personal endorsement;
- uses a generated output as evidence;
- can explain every outcome and therefore predicts nothing;
- survives a rival explanation after removing the favored motive, changing the relationship or knowledge condition, or reinstating an omitted inhibitor;
- mistakes narrative function, comedic necessity, or another actor's testimony for demonstrated interiority.

### 16.5 Error analysis

Preserve failures under recoverable categories:

- wrong knowledge state;
- wrong temporal state;
- wrong relationship condition;
- missed institutional or resource constraint;
- attention/appraisal error;
- motive-weighting error;
- omitted inhibitor/escalator;
- action-family mismatch;
- written-register mismatch;
- ordinary/crisis overgeneralization;
- source/mapping error;
- genuine underdetermination.

Revise the affected rule and dependent artifacts while retaining the failed test.

### 16.6 No fake accuracy

Do not publish an accuracy percentage from a small, selected, heterogeneous set of scenes. Report test counts and dispositions descriptively, with source selection, exposure, and domain limits. A model that abstains on everything is not operational; a model that never abstains is not bounded.

## 17. Model construction and lifecycle

The construction sequence is:

1. select person, continuity, and story-time state;
2. read the coverage index and current checkpoint;
3. retrieve affected character, relationship, institution, Sensei, voice, motif, and claim ledgers;
4. retrieve the strongest source-facing readings and stable IDs;
5. return to the complete canonical Japanese source units for consequential rules, using the existing reading/provenance routes; prioritize anomalies, disputed wording, and thin support for direct reinspection and record any unresolved source-access limit;
6. separate baseline, state, relation, role, resource, and crisis conditions;
7. draft a small rule set with alternatives, counterevidence, and disconfirmers;
8. define ordinary-life and speech limits;
9. define the counterfactual envelope and abstention zones;
10. freeze fair tests before eligible new source exposure;
11. adjudicate without changing the freeze;
12. revise through explicit transitions.

A model is updated in place when the responsibility and identity remain stable. Historical states and failed predictions stay recoverable through Git and validation records. A materially different continuity or approved global subject requires a separately scoped artifact rather than silent blending.

## 18. Model artifact contract and canonical home

When evidence warrants a standalone model, place it under:

```text
series/blue-archive/04 Specialist Synthesis/Character Reconstruction/
  BLUE_ARCHIVE_<STABLE_CHARACTER_KEY>_RECONSTRUCTION_MODEL.md
```

Do not create the directory or model merely to complete a roster. Every model must contain:

1. authority/source boundary;
2. identity and basis block;
3. intended use and abstention summary;
4. central mechanism;
5. temporal/contextual states;
6. behavioral rules;
7. directed relationship conditions;
8. institutional and resource conditions;
9. ordinary-life and crisis contrast;
10. Japanese written-speech profile;
11. negative constraints and explicit unknowns;
12. counterfactual envelope;
13. validation status and preserved failures;
14. evidence routes.

A mature literary monograph must explain the character's development, causal/narrative function, contradictions, relationships, language, and interpretive disputes. It may summarize an accepted operational mechanism and link rule IDs, but it must not maintain a competing rule set. The reconstruction model may consume accepted literary authority; it may not dictate literary conclusions through hypothetical output.

## 19. Current Chapter 2 bootstrap gate

At the current boundary:

- the Prologue, `MAIN_V001_C001`, and `MAIN_V001_C002` checkpoints are the complete admitted main-story basis;
- all seven ledgers are current through `BA:main:001:002:020` and the C002 checkpoint; read their checkpoint reconciliation and cumulative deltas rather than treating older opening tables as the latest state;
- contextual backfill remains `DEFER` under the checkpoint decision;
- no bond, MomoTalk, group, event, or performed-voice material has been analytically admitted for a reconstruction model in this tranche;
- no character is promoted to `OPERATIONAL_CANDIDATE` or `BOUNDED_VALIDATED` by this specification;
- the coverage index and bootstrap audit govern any later pilot selection;
- `BA:main:002:001:001` remains unopened; a new story instruction is required, and any intended prospective test must be committed before its diagnostic source is opened;
- the forthcoming Chapters 3–8 run uses the analytical method's checkpoint reconstruction-delta contract; chapter labels are workflow planning, not an invented chronological remapping of the crosswalk.

The correct present outcome is architecture and evidence triage, not a premature prototype.

## 20. Governing references and adopted precedents

This design is Blue Archive-specific but adopts tested methods from:

- `characters/README.md` — discovery identity and the distinction between substantial analysis and reconstruction readiness;
- `characters/RECONSTRUCTION_CAPABILITY_SPEC.md` — exact-scope capability discipline, evidence-backed limits versus gaps, and nonpopulation of global capability files;
- `series/rent-a-girlfriend/00 Frameworks and Methods/RAG_CHARACTER_RECONSTRUCTION_SPEC.md` — state/rule schemas, scenario contracts, local readiness, and monograph/model responsibility separation;
- Attack on Titan's character modeling and validation architecture — state vectors, ordinary-life control samples, source-to-model authority direction, scenario distance, and prospective freezes;
- My Hero Academia's modeling schema and representative models — evidence atoms, attention/decision dimensions, chronology locks, qualitative holdout comparison, and source-specific uncertainty;
- Tomozaki's synthesis architecture — derived-use placement after literary authority and targeted primary-source escalation;
- Oregairu's reconstruction models — explicit era selection, attention-to-action pipelines, anti-caricature rules, ordinary-life texture, and compact scenario engines.

The project does not import those projects' filenames, tiers, source assumptions, or artifact volume wholesale. One artifact retains one responsibility, and the Japanese Blue Archive source remains the evidentiary authority.

## 21. Revision and architecture review

Version 1.1 reconciles the recovered C002 boundary with the published C001 design in place. Revise this architecture if recurring evidence lacks a canonical owner; event/variant chronology cannot be represented without leakage; direction or choice conditions are repeatedly lost; models need competing live rules; validation cannot recover its freeze; or the current coverage router disguises domain failures. First repair the existing owner, schema, or routing contract. Add a separate ledger or specialist only for an independent recurring responsibility. Record the reason, version, affected dependencies, and required revalidation in the bootstrap or later scoped audit and current map. Source-admission decisions remain separate from architecture revision.
