---
title: "Rent-a-Girlfriend - Character Reconstruction Specification"
artifact_id: RAG_CHARACTER_RECONSTRUCTION_SPEC
artifact_type: character_reconstruction_specification
series: Rent-a-Girlfriend
generation: V1
version: "1.0"
status: canonical
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
do_not_use_as_literary_evidence: true
created: "2026-09-19"
canonical_home: "series/rent-a-girlfriend/00 Frameworks and Methods/RAG_CHARACTER_RECONSTRUCTION_SPEC.md"
design_reference_commit: "6d027e55f2eb38ec04ceed16bddc25015dc8a180"
adopted_at: "2026-09-19"
adopted_against_commit: "6d027e55f2eb38ec04ceed16bddc25015dc8a180"
source_boundary: "Specification only; no populated character model or capability assessment is delivered."
recommended_reasoning_class: DEEP_SYNTHESIS
---

# Character reconstruction: model schema, monographs, and validation

## 1. Required outcome

A substantial character study must support more than recollection of events or a list of personality traits. The target is a **source-bounded, time-indexed model of perception, motivation, choice, speech, and relationship-conditioned behavior**, with explicit limits on extrapolation.

The model should answer: under these circumstances, at this point in the manga, with these people and this knowledge, what responses are well supported, what alternatives remain plausible, and what would be inconsistent without additional assumptions?

It is not a claim of direct access to a fictional person's hidden mind. It is an interpretive model constrained by represented evidence. A coherent model can remain uncertain. Fluency in invented dialogue is not proof of reconstruction quality.

## 2. Three artifacts with different responsibilities

### 2.1 Character evidence/state ledger

`RAG_<CHARACTER>_EVIDENCE_LEDGER.md` owns the character-specific longitudinal evidence trace: relevant observations, source access, state changes, written-speech examples, ordinary conduct, contradictions, and gaps. It points to canonical volume evidence IDs rather than duplicating the full primary observations.

This is a curated analytical ledger, not a raw transcript. It answers **where and when the evidence for this person accumulated**.

### 2.2 Living reconstruction model

`RAG_<CHARACTER>_RECONSTRUCTION_MODEL.md` owns the current operational rules, temporal-state definitions, relationship conditions, plausible response ranges, prohibited inferences, and validation status. It answers **how to reconstruct behavior responsibly at a specified source state**.

The model is updated through targeted changes after material new evidence. Older states remain recoverable through its state history and exact checkpoint snapshots. Do not create separate permanent live models named CLOUD, LOCAL, and FINAL.

### 2.3 Mature character monograph

`RAG_<CHARACTER>_CHARACTER_MONOGRAPH.md` owns the substantial literary and psychological synthesis: development, causality, motives, self-report, relationships, speech, contradiction, narrative form, thematic role, and interpretive disputes.

Every mature monograph **must include a substantive reconstruction account**: explain the model's central mechanisms, state transitions, relationship conditioning, behavioral and speech repertoire, important negative constraints, tested examples, and limitations. It must name the exact model version or snapshot it incorporates and link the detailed rule IDs.

A monograph cannot satisfy reconstruction merely with a link. Equally, it must not maintain a competing set of operational rules. The detailed model is the operational home; the monograph explains and integrates it. The monograph can challenge a rule, but accepted revisions route back through the model and claim history.

The monograph's literary interpretation and the model's operational extrapolation have different responsibilities. Neither automatically supersedes the other. A later model update does not silently expand the monograph's declared scope.

## 3. Identity and source state

Resolve the character's identity against the live global registry where an enrolled subject exists. Preserve the distinction between underlying entity and continuity/state-specific analysis subject. Before enrollment, use visibly **project-local** identifiers and keep global fields null. Do not invent canonical registry IDs or write the global character files.

The initial planned priority is Kazuya Kinoshita and Chizuru Ichinose, with Chizuru's professional/display names tracked as aliases when verified. Mami Nanami, Ruka Sarashina, Sumi Sakurasawa, Mini Yaemori, and other substantive figures enter on their actual evidence schedule. These names are planning targets inherited from the discussion, not a claim that their sources have been inspected or that each warrants equal coverage.

Do not treat a professional persona, disguise, temporary mood, or ordinary developmental phase as a separate person or global analysis subject by default. Model its conditioning explicitly.

Every model identifies its manga witness, admitted volumes, relevant chronology, source access, and other excluded continuities. Volume numbers index evidence availability; they are not themselves proof that a personality phase changed at a block boundary.

## 4. Model header and required domains

Use readable prose supported by small structured records. The following is a **local documentation contract**, not a proposed replacement for any repository-wide JSON schema.

```yaml
model_identity:
  artifact_id: null
  local_character_key: null
  preferred_name: null
  character_entity_id: null       # Existing reviewed global ID only, when available.
  analysis_subject_id: null       # Existing reviewed global subject only.
  continuity: manga
model_basis:
  source_witnesses: []
  admitted_through_volume: null
  narrative_time_boundary: null
  basis_checkpoint: null
  basis_commit: null             # An existing input snapshot; never a fabricated/self hash.
  model_revision: null
  prior_knowledge_limitations: []
coverage:
  observed_contexts: []
  missing_contexts: []
  translation_limitations: []
  written_speech: null
  performed_voice: OUT_OF_SCOPE
```

Artifact authority remains in the complete top-level repository quartet. Coverage, confidence, model maturity, and authority are independent fields.

Each substantial model must address the following domains with evidence, bounded inference, or an explicit unassessed/gap statement:

| Domain | Required analytical content |
|---|---|
| Core self-model | Explicit and implicit self-description; desired and feared self; discrepancies from observed conduct. |
| Motivational architecture | Surface wants, recurring needs, commitments, protected values/fears, and what wins when they conflict. |
| Decision process | Perception, interpretation, affect, options, inhibition, action, and later self-account. |
| Models of other people | Accurate beliefs, errors, idealization, assumptions about others' knowledge, and updating conditions. |
| Emotional regulation | Triggers, escalation, expression, avoidance, rumination, recovery, disclosure, and contextual variation. |
| Intimacy and dependency | Giving/receiving care; desired proximity; vulnerability; public/private distinctions; refusal and reciprocation. |
| Agency and competence | Initiative, persistence, practical ability, help-seeking, intervention, refusal, cost-bearing, and domain-specific limits. |
| Social performance | Presentation to strangers, friends, family, clients, romantic targets, and perceived rivals. |
| Constraint structure | Shame, pride, uncertainty, professional duties, loyalties, habits, material conditions, and other evidenced inhibitions. |
| Ordinary repertoire | Small talk, listening, humor, leisure, work routines, everyday preferences, and low-stakes choices. |
| Written speech | Vocabulary, address, politeness, sentence structure, repair, interruption, humor, and differences by interlocutor. |
| Contradiction and negative constraints | Important claims/behavior conflicts, strong counterexamples, and responses the evidence makes implausible. |
| Thresholds | Conditions under which response changes; qualitative and contextual, not invented numerical cutoffs. |
| Development | What changes, what persists, what was newly revealed, and which mechanisms explain the transitions. |
| Counterfactual envelope | Supported scenario domains, required assumptions, alternatives, abstention conditions, and untested regions. |
| Limits and confidence | Interiority access, missing evidence, localization sensitivity, unresolved alternatives, and demonstrated failures. |

These domains need not become sixteen uniform essays. Give a central character a deep account where the evidence warrants it; leave unsupported domains explicitly sparse. Reject a filled template that has no explanatory mechanism.

## 5. State and rule schemas

### 5.1 State definition

A state is a materially distinct configuration, not simply a new volume. It may combine a stable disposition with changed knowledge, relationships, resources, or commitments.

```yaml
state_id: null
label: null
valid_from_source: null
valid_until_source: null
entry_conditions: []
self_model: null
active_goals: []
known_propositions: []
relationship_conditions: []
material_constraints: []
changed_from_previous: []
persisting_features: []
evidence_refs: []
uncertainties: []
```

Track the cause of a difference as `DISPOSITION_CHANGE`, `KNOWLEDGE_CHANGE`, `RELATIONSHIP_CHANGE`, `CONTEXT_CHANGE`, `REVEALED_NOT_NEW`, or `UNRESOLVED`. Several can apply. Do not call every changed response character growth or every recurrence regression.

### 5.2 Behavioral rule

Use stable local IDs such as `RAG-KAZ-R001`. They do not imply global registry enrollment.

```yaml
rule_id: null
scope_state_ids: []
trigger_or_situation: null
relationship_conditions: []
character_knowledge_required: []
likely_appraisal: null
motives_in_conflict: []
likely_internal_response: null
likely_external_action_range: []
inhibitors_and_escalators: []
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

Prefer a compact explanatory rule over a list of every imaginable response. It must exclude something or discriminate between conditions to have operational value. Very broad rules that can accommodate every outcome are descriptive padding, not successful models.

Repeated restatements of one scene are not independent evidence. Strong generalization normally needs evidence across genuinely different opportunities or contexts. A distinctive single scene can support a narrow rule; it cannot justify unrestricted cross-scenario confidence.

### 5.3 Directed relationship conditioning

For each major relationship, specify how A regards B; what A thinks B expects; public/private differences; obligations; vulnerabilities; misreadings; and updating conditions. Link the relational ledger rather than creating a competing chronology.

A rule valid with a trusted confidant may fail with a stranger. A model that predicts the same speech and choices for every interlocutor is inadequate even if its trait summary is recognizable.

## 6. Different access strategies for Kazuya and Chizuru

For Kazuya, explicitly compare represented cognition with observable conduct. Test when self-evaluation predicts avoidance, when it coexists with competent action, and when it is contradicted by consequences. These are candidate questions, not findings already established by this specification.

For Chizuru, distinguish behavior, statements, private scenes, formal emphasis, and others' interpretations. Write the **minimum warranted inference** before stronger motive hypotheses. For example, in a hypothetical source situation, voluntary contact could establish a chosen continuation of contact without establishing conscious acknowledgment of a particular romantic feeling. This example is methodological, not a claim about a specific chapter.

Do not turn his interior access into exhaustive transparency or her limited access into permission to invent a hidden script. Apply each strategy only where the inspected volume supports that access pattern; revise as narration changes.

For other characters, select the strategy their actual evidence warrants. Do not hard-code Mami as a single motive, Ruka as only an obstacle, Sumi as only a personality label, or Mini as only a plot facilitator. Narrative function and autonomous characterization are separate questions to investigate.

## 7. Written speech and ordinary behavior

### 7.1 Speech profile

A usable speech model identifies the language witness and how speech varies by audience, emotional state, and setting. Capture representative short examples with locators and their context: address forms, directness, hedging, intensity, self-correction, questions, apologies, teasing, silence, interruption, and turn-taking.

Separate quoted wording, analyst paraphrase, and generated demonstration. A localization can support a profile of its own rendered voice; it does not by itself establish Japanese pronoun choice or dialect. Translation limitations are recorded at rule level where they affect prediction.

Do not substitute catchphrase imitation, excessive stammering, or one highly dramatic register for a person's whole conversational range. An invented line should sound plausible for that situation without pretending to be recoverable canon dialogue.

### 7.2 Ordinary repertoire

Track how a character spends an uneventful afternoon, responds to a mundane request, handles an awkward introduction, receives a compliment, or negotiates a small disagreement **when the manga provides relevant evidence**. Small preferences are especially easy to fabricate; keep unsupported ones unknown.

Non-romantic behavior matters. A model fitted only to romantic crises cannot claim general social or professional readiness. Missing mundane coverage is a limitation even for an extensively discussed central character.

### 7.3 No performed-voice substitution

Manga supports written speech and drawn presentation. Performed voice, prosody, timbre, and acting remain outside this initial model. A later anime layer needs its own witness, state mapping, inspection method, and adaptation-divergence treatment. It must not silently rewrite manga-only behavior.

## 8. Model use in novel scenarios

Every counterfactual starts with an explicit scenario contract:

```yaml
scenario_id: null
scenario_type: null
source_state_or_checkpoint: null
participants_and_relationships: []
setting_and_audience: null
stakes_and_material_constraints: []
what_each_person_knows: []
canon_changes_introduced: []
unknown_assumptions: []
applicable_rule_ids: []
unsupported_domains: []
```

For a dating-show or dinner scenario, specify chronology, prior familiarity, audience exposure, participation incentives, and whether the setting is ordinary, pressured, or performative. Do not assume a character understands an unfamiliar show format, has new life experience, or knows another franchise's history.

Age-normalization or other owner-specified transformations are explicit changes; they do not automatically supply maturity, experience, preferences, or a new developmental history. Keep any resulting uncertainty visible.

The output should distinguish likely appraisal, plausible internal response, likely observable conduct, and alternative branches. Exact invented dialogue is an illustration, not a uniquely predicted line. Include a brief rationale linked to rules, not a hidden-thought transcript claim.

A crossover output stays a downstream application. It cannot feed back into manga evidence, become a new canonical biography, or certify readiness simply by being entertaining. Cross-series study artifacts belong under the appropriate study architecture when separately commissioned.

## 9. Validation design

### 9.1 Prospective checks

At a closed volume or block, freeze a small set of material, discriminating rules and predictions before opening the next relevant source. Record the source basis, conditions, expected response range, meaningful alternatives, and disconfirmation criterion. Preserve a verifiable prior snapshot.

When a diagnostic opportunity occurs, adjudicate the frozen expectation against the observed action and context. Do not edit the prediction after seeing the result. Use `SUPPORTED_IN_THIS_TEST`, `PARTLY_SUPPORTED`, `CONTRADICTED`, `NO_DIAGNOSTIC_OPPORTUNITY`, or `UNRESOLVED`.

A correct prediction of a trope is weaker evidence of character specificity than predicting a response that distinguishes this character from a plausible alternative model. Record what the test actually discriminated.

### 9.2 Retrospective and withheld-context checks

A previously read scene can test internal consistency, but label it retrospective. A reviewer can be given a bounded evidence packet with selected scenes omitted; describe exactly what was withheld and whether prior exposure is known. Do not describe such a test as genuinely blind when the analyst may already know the scene.

Include ordinary, conflict, professional, intimacy, embarrassment, humor, and relationship-switch tests when the available evidence can support them. Coverage follows the source; do not invent unseen canonical incidents to fill a test matrix.

### 9.3 Negative and adversarial tests

Ask where the rule fails, whether an alternate explanation fits better, and what observation would materially weaken it. Test whether it confuses thoughts with action, gives both sides of a relationship the same knowledge, imports a later state, overattributes hidden motives, or mistakes narrative necessity for a person's decision process.

Separate `EVIDENCE_GAP` from `EVIDENCE_BACKED_LIMITATION`. Silence in the dataset is not affirmative evidence that a character would never do something. Strong counterevidence is not erased merely because the preferred interpretation remains appealing.

### 9.4 Error analysis

Record failures under recoverable categories: wrong knowledge state, wrong relationship condition, motive weighting error, omitted inhibition, speech/register mismatch, overgeneralization, source/translation error, later-state leakage, or genuine underdetermination. Then revise the affected rule and downstream artifacts, preserving the failed test.

Do not publish a numerical accuracy percentage from a small handpicked sample. Test counts may be reported descriptively with selection and exposure limitations. A model that abstains on everything is not operationally useful; a model that never abstains is not appropriately bounded.

## 10. Checkpoint audit and local readiness

After each ten-volume checkpoint, create one project-local reconstruction audit covering active substantial characters. For each character, record the exact model/snapshot, observed domains, strong and weak rules, tests performed, failures, required assumptions, unsupported scenarios, and the next evidence needed.

Use descriptive local readiness, not global A-E grades. A practical local vocabulary is:

- `UNMODELED`: evidence is routed but no operational model is asserted.
- `PARTIAL_MODEL`: a bounded account exists, with substantial unmodeled domains.
- `OPERATIONAL_CANDIDATE`: rule-based scenario work is supportable under named conditions; validation is incomplete.
- `BOUNDED_VALIDATED`: named rules have survived specified checks within an explicit tested envelope.

These labels never mean whole-person certainty. Readiness is stated by scenario/domain, not just by character. A character can be useful for ordinary dialogue and insufficiently supported for professional or romantic extrapolation.

The global `characters/RECONSTRUCTION_CAPABILITY_SPEC.md` reserves production capability records and formal A-E assessment for a separately authorized owner-reviewed phase. This project does not create or populate global capability files, mint grades, or repurpose the discovery registry as a simulation ranking. Project-local audits support the requested analysis without claiming that separate registry assessment occurred.

## 11. Promotion to a mature monograph

Promotion is evidence-based, not determined by having reached V030 or V040. At each block boundary, decide whether the character warrants a bounded dossier, an operational candidate, a substantial monograph, or further evidence collection. A mature through-V010 monograph can be legitimate when sufficiently supported; a through-V040 monograph can still be premature for a sparsely depicted figure.

A mature monograph must:

1. Develop an integrated argument about the character across the declared source boundary, rather than concatenate volume summaries.
2. Explain change and persistence, self-report versus action, relationship conditioning, written speech, ordinary repertoire, and important contradictions at the depth the evidence supports.
3. Incorporate the operational reconstruction in substantive prose with rule/state links and representative applications.
4. Address the strongest competing interpretation and material counterevidence.
5. Distinguish literary/narrative function from inferred psychology and from counterfactual extrapolation.
6. Provide traceable source routes and disclose material gaps, scope, and validation limitations.

No fixed word limit defines maturity. Headings, length, confident prose, and registry inclusion are not substitutes for these obligations. A monograph can be mature as literary synthesis while operational capability remains conditional in named domains; it must say so rather than claiming universal simulation readiness.

## 12. Update and dependency discipline

When new evidence changes a rule, update its scope, basis, and revision reference. Check the related monograph, relationship specialist, progress interpretation, and active predictions for consequences. If a monograph's central mechanism is no longer supportable, mark the affected interpretation for substantive revision; a small appended caveat is not enough.

Preserve the evidence ledger's history. Freeze checkpoint versions through exact Git snapshots rather than maintaining multiple identically scoped live files. Historical time states are not discarded when the current model advances.

A noncurrent draft cannot supersede an accepted model through metadata alone. On acceptance, use the live authority/supersession contract. Routine in-place revision under one artifact ID normally uses version history rather than creating new file-level supersession edges for every update.

## 13. Governing references

This specification formalizes the owner's requested reconstruction layer. It was designed against relevant sections of:

- `characters/README.md` - discovery identity, authority, and maintenance ownership;
- `characters/RECONSTRUCTION_CAPABILITY_SPEC.md` - formal global capability boundary, evidence scope, and limitations;
- `governance/source-policies/MANGA_ANIME_REASONING_AND_MODEL_ROUTING_POLICY.md` - distinct responsibilities for monographs and operational reconstruction;
- `governance/source-policies/MANGA_ANIME_LONG_SERIES_HYBRID_EXECUTION_PROTOCOL.md` - substantive synthesis, frozen inputs, and convergence;
- `governance/source-policies/MANGA_ANIME_ANALYTICAL_HANDOFF_AND_INTEGRATION_CONTRACT.md` - scoped transfer and semantic acceptance.

Repository reference: https://github.com/deep-blue-zero/anime-manga-ln-games-analysis/tree/6d027e55f2eb38ec04ceed16bddc25015dc8a180

The locally defined fields, rule IDs, and readiness vocabulary above are proposed project instrumentation. They are not asserted to be existing repository-wide schema fields, validated global grades, or conclusions about characters already read.
