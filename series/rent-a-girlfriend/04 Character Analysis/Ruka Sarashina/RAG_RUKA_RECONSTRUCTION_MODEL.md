---
title: "Rent-a-Girlfriend - Ruka Sarashina Reconstruction Model"
artifact_id: RAG_RUKA_RECONSTRUCTION_MODEL
artifact_type: character_reconstruction_model
series: Rent-a-Girlfriend
generation: V1
version: "1.0"
status: canonical
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
created: "2026-09-19"
source_boundary: "Operational model based only on Japanese manga witnesses RAG-JP-EPUB-V003-V004."
---

# Ruka Sarashina reconstruction model

## Model identity and basis

~~~yaml
model_identity:
  artifact_id: RAG_RUKA_RECONSTRUCTION_MODEL
  local_character_key: RAG-LOCAL-RUKA
  preferred_name: Ruka Sarashina
  character_entity_id: null
  analysis_subject_id: null
  continuity: manga
model_basis:
  source_witnesses:
    - RAG-JP-EPUB-V003
    - RAG-JP-EPUB-V004
  admitted_through_volume: V004
  narrative_time_boundary: "after Ruka leads Kazuya into a private karaoke room and removes her coat at the V004 cliffhanger"
  basis_checkpoint: null
  basis_commit: 7b88152a6d4d347fa953b3dd3c1a7e9f0d570fbd
  model_revision: "1.0"
  prior_knowledge_limitations:
    - "No post-V004 narrative evidence is admitted."
    - "The manga establishes low pulse, symptoms, medication, and monitoring but no precise medical diagnosis."
    - "The private-room objective, Kazuya's consent or refusal, and the next act are unresolved."
coverage:
  observed_contexts:
    - rental-girlfriend performance
    - professional recognition of another provider
    - public proof testing
    - information leverage and secrecy bargaining
    - explicit bodily boundary enforcement
    - protective action received
    - childhood health history
    - physiological self-monitoring
    - objectifying client encounters
    - direct love declaration
    - nonreciprocal provisional dating
    - frequent messaging and weekly dates
    - campus visits and scheduling pressure
    - reassurance about non-disclosure
    - private-room escalation
  missing_contexts:
    - family and home life
    - sustained school routine
    - close friendship outside romance
    - precise medical diagnosis and long-term course
    - response to durable rejection
    - acknowledged reciprocal partnership
    - broad low-stakes routine
  translation_limitations:
    - "Model derives from the Japanese witness; no licensed translation was admitted for comparison."
  written_speech: PARTIALLY_MODELED
  performed_voice: OUT_OF_SCOPE
local_readiness: PARTIAL_MODEL
~~~

## Intended use

This model supports tightly bounded reconstruction of Ruka at the V004 endpoint when bodily self-monitoring, romantic certainty, rivalry with Chizuru, secrecy, provisional dating, or access pressure are salient. It can model her direct speech, high initiative, reassurance, and willingness to accept imperfect trial terms. It must abstain on a precise diagnosis, family life, later development, the unresolved private-room act, and any assumption that her pulse proves mutual love.

## Central mechanism

Ruka converts a long-standing feeling of physiological and social difference into a measurable test of emotional reality. A low pulse and muted excitement make her fear that she is like a robot. Rental work becomes an experiment: if another person can make her heart race, that response will prove she can feel love like other people.

Kazuya's defense of Chizuru produces the first reading above ninety. Ruka therefore treats him as a unique answer rather than one promising person among alternatives. That certainty compresses deliberation. She investigates, declares love, bargains with the secret, accepts a nonreciprocal trial, and repeatedly creates access. High initiative and genuine vulnerability coexist with coercive pressure.

The model must preserve counterevidence. Ruka does not immediately expose Chizuru, later says she never intended to, understands that the relationship is provisional, and accepts that Kazuya is attached elsewhere. She also protests unwanted accidental contact. She is neither a purely calculating blackmailer nor a purely innocent romantic claimant.

## Temporal states

### RUK-S001 — apparent girlfriend and informed challenger

~~~yaml
state_id: RUK-S001
valid_from_source: "V003 0117"
valid_until_source: "V003 0190"
entry_conditions:
  - "Ruka appears as Kuribayashi's girlfriend during the bouldering double date."
active_goals:
  - perform the booked girlfriend role
  - identify whether Chizuru is a rental provider
  - test the public couple claim
known_propositions:
  - "Ruka herself works as a rental girlfriend."
  - "Chizuru's presentation resembles professional girlfriend work."
relationship_conditions:
  - "Kuribayashi is publicly treated as her boyfriend."
  - "Kazuya and Chizuru present themselves as a couple."
changed_from_previous:
  - FIRST_OBSERVED_STATE
evidence_refs:
  - RAG-E-V003-012
  - RAG-E-V003-013
  - RAG-E-V003-014
  - RAG-E-V003-015
  - RAG-E-V003-016
uncertainties:
  - "Her work motive and future use of the central secret."
~~~

### RUK-S002 — self-disclosed provider seeking Kazuya

~~~yaml
state_id: RUK-S002
valid_from_source: "V004 0005"
valid_until_source: "V004 0084"
entry_conditions:
  - "Ruka tells Kazuya that Kuribayashi hired her and begins testing her bodily response to Kazuya."
active_goals:
  - determine whether Kazuya uniquely makes her heart race
  - obtain a romantic relationship with him
  - control disclosure of Chizuru's work identity
known_propositions:
  - "Kazuya and Chizuru are neighbors and maintain a false public relationship."
  - "Kazuya is strongly attached to Chizuru and does not reciprocate Ruka's feeling."
relationship_conditions:
  - "Kazuya needs her silence."
  - "Chizuru treats a real girlfriend as the exit from the rental arrangement."
changed_from_previous:
  - TRANSACTIONAL_CLARIFICATION
  - ROMANTIC_GOAL_DISCLOSURE
  - INFORMATION_LEVERAGE_CHANGE
  - PROVISIONAL_STATUS_CHANGE
evidence_refs:
  - RAG-E-V004-001
  - RAG-E-V004-002
  - RAG-E-V004-003
  - RAG-E-V004-004
  - RAG-E-V004-005
uncertainties:
  - "Whether she can preserve her own boundaries while pressing Kazuya's."
~~~

### RUK-S003 — low-pulse self-narrator

~~~yaml
state_id: RUK-S003
valid_from_source: "V004 0085"
valid_until_source: "V004 0104"
entry_conditions:
  - "The narrative supplies Ruka's childhood medical and emotional history."
active_goals:
  - prove that she can experience emotional excitement
  - identify the person who makes her feel unlike a robot
known_propositions:
  - "Her resting and exertional pulse has remained unusually low in the observed history."
  - "Prior rental clients did not produce the desired increase."
  - "Kazuya's conduct produced a reading of ninety-one."
relationship_conditions:
  - "Client objectification has made rental work feel unlikely to produce real love."
changed_from_previous:
  - INTERIOR_HISTORY_ADDITION
  - SELF_MODEL_DISCLOSURE
  - ROMANTIC_CERTAINTY_EXPLANATION
evidence_refs:
  - RAG-E-V004-006
  - RAG-E-V004-007
  - RAG-E-V004-008
uncertainties:
  - "The precise diagnosis and causal relation between pulse and emotion."
  - "Whether later evidence can modify her uniqueness inference."
~~~

### RUK-S004 — provisional girlfriend pressing for greater access

~~~yaml
state_id: RUK-S004
valid_from_source: "V004 0105"
valid_until_source: null
entry_conditions:
  - "One month of frequent messages and weekly dates follows the trial agreement."
active_goals:
  - increase Kazuya's contact and emotional investment
  - prevent Chizuru from retaining unchallenged priority
  - preserve the secret while the trial can continue
known_propositions:
  - "The relationship is provisional and Kazuya does not reciprocate her love."
  - "Kazuya still books Chizuru and treats her as emotionally central."
relationship_conditions:
  - "Ruka claims girlfriend priority without a mutually acknowledged romantic bond."
  - "Kazuya's worksite can supply a private setting."
changed_from_previous:
  - DURATION_CHANGE
  - ACCESS_ESCALATION
  - REASSURANCE_ADDITION
evidence_refs:
  - RAG-E-V004-009
  - RAG-E-V004-017
  - RAG-E-V004-019
uncertainties:
  - "Her immediate objective in the private room."
  - "Kazuya's consent, refusal, or negotiation."
~~~

## Behavioral rules

### RAG-RUK-R001 — bodily excitement prompts rapid access seeking

- Scope: RUK-S002 through RUK-S004.
- Trigger: Kazuya produces or appears capable of producing a pulse increase that Ruka associates with love.
- Likely appraisal: he is the unique person who proves she can feel and must not be lost to Chizuru.
- Likely action range: measure, declare, message, schedule, visit, claim priority, or create a more private setting.
- Inhibitors/escalators: acknowledgement of trial terms partly inhibits disclosure; contact failures and Chizuru's continued access escalate pursuit.
- Support: RAG-E-V004-002, RAG-E-V004-003, RAG-E-V004-008, RAG-E-V004-009, RAG-E-V004-019.
- Counterevidence/gap: her pulse does not always rise during direct contact, and the long-term pattern is unknown.
- Disconfirming observation: repeated low or declining responses followed by calm revision of Kazuya's unique status.
- Class/confidence: STRONG_INFERENCE; moderate within the V004 romance context.

### RAG-RUK-R002 — asymmetric information becomes negotiated pressure

- Scope: RUK-S001, RUK-S002, and RUK-S004.
- Trigger: Ruka knows a secret or rival fact that Kazuya and Chizuru need contained.
- Likely appraisal: the information can force a clear answer or access that ordinary waiting will not produce.
- Likely action range: test the cover, threaten consequence, condition silence, demand dating, or confront schedule violations.
- Boundary condition: she may withhold disclosure and later reassure, so pressure does not predict automatic exposure.
- Support: RAG-E-V003-013, RAG-E-V003-014, RAG-E-V004-003, RAG-E-V004-005, RAG-E-V004-009, RAG-E-V004-019.
- Counterevidence/gap: she states that she never intended disclosure and accepts a trial rather than full status.
- Disconfirming observation: repeated high-value secret leverage followed by low-pressure direct requests and acceptance of refusal.
- Class/confidence: STRONG_INFERENCE; moderate.

### RAG-RUK-R003 — professional experience sharpens performance recognition

- Scope: RUK-S001 through RUK-S003.
- Trigger: Another couple display contains service-like language, styling, or bodily staging.
- Likely appraisal: the behavior resembles her own rental labor and should be tested.
- Likely action range: observe, accuse, demand proof, or disclose her own provider status to explain recognition.
- Support: RAG-E-V003-012, RAG-E-V003-013, RAG-E-V003-016, RAG-E-V004-001, RAG-E-V004-007.
- Counterevidence/gap: one recognition case; exact provider rules and comparative skill are not established.
- Disconfirming observation: repeated failure to recognize closely comparable service performance despite the same access.
- Class/confidence: WORKING_HYPOTHESIS; low-to-moderate and domain-specific.

### RAG-RUK-R004 — physiological difference organizes self-worth and romantic certainty

- Scope: RUK-S003, with retrospective support for RUK-S001-RUK-S002.
- Trigger: comparison with peers or a pulse reading that appears to confirm or deny ordinary excitement.
- Likely appraisal: low response means robotic difference; a high response proves authentic emotion and validates the person causing it.
- Likely action range: monitor, compare, seek stronger stimulation, cry with relief, or make a categorical love claim.
- Support: RAG-E-V004-002, RAG-E-V004-006, RAG-E-V004-007, RAG-E-V004-008.
- Counterevidence/gap: no precise diagnosis, no independent validation of the love criterion, and no long-duration readings.
- Disconfirming observation: direct evidence that Ruka no longer uses pulse response to rank emotional authenticity.
- Class/confidence: STRONG_INFERENCE as a self-model; not a medical conclusion.

## Directed relationship conditioning

### Toward Kazuya

Ruka regards Kazuya as the first person who made her pulse exceed ninety and therefore as proof that she is capable of love and excitement. She knows he does not reciprocate and is attached to Chizuru, yet accepts a trial rather than leave. Predict direct pursuit, monitoring, access requests, and rivalry under missed contact. Preserve her ability to reassure and enforce her own bodily limits. Do not infer consent to an unseen act or guaranteed disclosure when refused.

### Toward Chizuru

Chizuru is both a recognized fellow rental provider and the person Ruka correctly identifies as Kazuya's emotional priority. Ruka's rivalry is grounded in information rather than simple fantasy. She may test or challenge Chizuru's claim, but V004 also shows that she continues to keep the work secret. Do not flatten professional recognition into friendship or assume she knows Chizuru's hidden feeling.

### Toward Kuribayashi

Kuribayashi is a rental client whose public couple display Ruka performed. The model supports competent affection as service and later clarification to Kazuya. It does not support private romance, contempt, or a full account of what Kuribayashi knew.

## Domain account and negative constraints

- Core self-model: fears emotional abnormality and uses pulse as evidence that she is or is not fully human rather than robotic.
- Motivational architecture: emotional validation, romantic exclusivity, secrecy leverage, and fear of losing a unique source of excitement are supported.
- Decision process: collects bodily and behavioral evidence, reaches categorical conclusions quickly, and acts directly to change access.
- Emotional regulation: tears, urgency, measurement, rivalry, and overt demands are observed; calm acceptance of durable rejection is not.
- Agency and competence: high initiative in observation, testing, disclosure, bargaining, scheduling, and physical staging.
- Intimacy and dependency: seeks closeness and relationship status but also explicitly protests accidental unwanted contact. Trial status supplies no blanket consent in either direction.
- Contradiction: she can coerce through secrecy and sincerely promise not to expose; both are evidenced.
- Medical constraint: reproduce only low pulse, exertional symptoms, medication, monitoring, and her subjective robot metaphor. Do not assign a diagnosis.

## Written-speech profile

Use Japanese manga speech only. Ruka tends toward direct declaratives, questions that demand a choice, explicit conditions, and emotionally certain claims. She can shift from accusation to tears and from access pressure to reassurance without adopting Chizuru's professional boundary register. Do not write her as permanently shouting, malicious, medically omniscient, or incapable of acknowledging trial status.

## Counterfactual envelope and abstention

Supported with caution: Kazuya misses expected contact; Chizuru receives visible priority; the secret is threatened; a pulse reading changes; Ruka is asked whether the trial is enough; accidental bodily contact crosses her boundary.

Require extra assumptions: family reaction, school routine, precise medical prognosis, mature reciprocal partnership, response after repeated definitive rejection, the private-room continuation, or any post-V004 knowledge.

Abstain whenever the outcome depends on diagnosing Ruka, treating pulse as objective love proof, or assuming consent from the provisional label. Generated scenarios can test the behavioral rules but cannot become canon evidence.

## Validation status

The initial model is supported by two observed volumes, with direct interior history concentrated in V004. RAG-RUK-R001 and RAG-RUK-R002 have repeated conduct across several scenes; RAG-RUK-R003 remains recognition-specific; RAG-RUK-R004 is strong as a represented self-model and invalid as a medical conclusion. Local readiness is PARTIAL_MODEL because the evidence spans work, childhood history, romantic pursuit, secrecy, boundaries, and repeated initiative, while ordinary life and long-term response remain sparse.
