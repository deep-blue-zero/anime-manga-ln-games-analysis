---
title: "Rent-a-Girlfriend - Chizuru Ichinose Reconstruction Model"
artifact_id: RAG_CHIZURU_RECONSTRUCTION_MODEL
artifact_type: character_reconstruction_model
series: Rent-a-Girlfriend
generation: V1
version: "1.1"
status: canonical
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
created: "2026-09-19"
source_boundary: "Operational model based only on Japanese manga witnesses RAG-JP-EPUB-V001-V002."
---

# Chizuru Ichinose reconstruction model

## Model identity and basis

~~~yaml
model_identity:
  artifact_id: RAG_CHIZURU_RECONSTRUCTION_MODEL
  local_character_key: RAG-LOCAL-CHIZURU
  preferred_name: Chizuru Ichinose
  character_entity_id: null
  analysis_subject_id: null
  continuity: manga
model_basis:
  source_witnesses:
    - RAG-JP-EPUB-V001
    - RAG-JP-EPUB-V002
  admitted_through_volume: V002
  narrative_time_boundary: "after Chizuru falls overboard and is shown unconscious at the unresolved V002 ferry cliffhanger"
  basis_checkpoint: null
  basis_commit: 3d79472fb72ccb6d7670a4e0735b6f52ea41d81c
  model_revision: "1.1"
  prior_knowledge_limitations:
    - "No post-V002 narrative evidence is admitted."
    - "Interiority is sparse; motives are modeled at minimum warranted strength."
    - "Chizuru is not shown knowing about Kazuya's dive; rescue outcome is unknown."
coverage:
  observed_contexts:
    - rental-girlfriend work
    - dissatisfied-client conflict
    - campus identity protection
    - family and hospital interaction
    - neighbor boundary negotiation
    - public peer conflict
    - limited private apartment conduct
    - university-friend travel and identity collision
    - transaction settlement and announced closure
    - illness and acute physical vulnerability
  missing_contexts:
    - sustained study and friendships
    - reason for needing the job
    - explicit romantic self-report
    - long-term professional practice
    - acknowledged reciprocal partnership
    - broad private routine
  translation_limitations:
    - "Model derives from the Japanese witness; no licensed translation was admitted for comparison."
  written_speech: PARTIALLY_MODELED
  performed_voice: OUT_OF_SCOPE
local_readiness: PARTIAL_MODEL
~~~

## Intended use

This model supports narrow reconstruction of Chizuru at the V002 endpoint when professional rules, family welfare, privacy, audience management, public unfairness, or a socially requested exception are salient. Because the manga rarely supplies her interior narration, the model predicts action ranges from conduct and speech rather than inventing a hidden monologue. It must abstain on rescue knowledge, romantic feeling, career goals, intimate partnership, and unseen ordinary preferences.

## Central mechanism

Chizuru manages competing obligations through compartmentalization and bounded exceptions. She can perform warmth as skilled labor, protect a separate campus identity, and speak bluntly when a client threatens those boundaries. When new information reveals a concrete family or dignity cost, she may revise an earlier refusal. She then tends to specify a rule, payment frame, audience story, or exit that limits what the exception means.

The minimum supported motive is responsive responsibility. Professional pride, empathy for the grandmothers, fairness toward Kazuya, social obligation to Kibe, protection of her own work, and possible personal investment can all contribute. V002 prospectively supports her tendency to restore a role or endpoint after suggestive conduct. Neither volume justifies selecting romance as the hidden master explanation or treating professional conduct as emotionally unreal.

## Temporal states

### CHI-S001 — professional provider with a dissatisfied client

~~~yaml
state_id: CHI-S001
valid_from_source: "V001 p.9"
valid_until_source: "V001 p.56"
entry_conditions:
  - "Kazuya books Chizuru through Diamond."
active_goals:
  - deliver a satisfying girlfriend experience
  - protect professional boundaries and reputation
known_propositions:
  - "Kazuya purchased a role and later left a hostile review."
relationship_conditions:
  - "Kazuya is a client, not a private partner."
persisting_features:
  - rapid social calibration
  - direct correction when the service frame is abused
evidence_refs:
  - RAG-E-V001-002
  - RAG-E-V001-003
  - RAG-E-V001-004
uncertainties:
  - "How representative this difficult client encounter is of her ordinary work."
~~~

### CHI-S002 — dual-identity provider under family exposure

~~~yaml
state_id: CHI-S002
valid_from_source: "V001 p.57"
valid_until_source: "V001 p.106"
entry_conditions:
  - "Kazuya recognizes her at their university."
active_goals:
  - protect her campus identity and employment
  - limit contact
  - prevent immediate harm to both grandmothers
known_propositions:
  - "Kazuya's family believes the girlfriend claim."
  - "Sayuri and Nagomi now know each other."
relationship_conditions:
  - "Kazuya is a client carrying a family deception that now affects her family."
changed_from_previous:
  - KNOWLEDGE_CHANGE
  - RELATIONSHIP_CHANGE
  - CONTEXT_CHANGE
evidence_refs:
  - RAG-E-V001-005
  - RAG-E-V001-006
uncertainties:
  - "Her reason for needing to continue the job."
~~~

### CHI-S003 — bounded recurring collaborator

~~~yaml
state_id: CHI-S003
valid_from_source: "V001 p.107"
valid_until_source: "V002 i_0041"
entry_conditions:
  - "Adjacent apartments create an unplanned private-space overlap."
active_goals:
  - preserve identity and residential privacy
  - manage both grandmothers' welfare
  - keep recurring contact bounded and compensated
  - maintain dignity within the public role
known_propositions:
  - "Nagomi's belief gives the fiction emotional weight."
  - "Kazuya's friends and Mami now see her as his girlfriend."
relationship_conditions:
  - "Kazuya is a client, neighbor, and co-maintainer of a family and peer deception."
changed_from_previous:
  - RELATIONSHIP_CHANGE
  - CONTEXT_CHANGE
evidence_refs:
  - RAG-E-V001-007
  - RAG-E-V001-008
  - RAG-E-V001-009
  - RAG-E-V001-011
  - RAG-E-V001-013
uncertainties:
  - "Whether chosen defense and care contain a romantic component."
~~~

### CHI-S004 — identity-collision participant under announced closure

~~~yaml
state_id: CHI-S004
valid_from_source: "V002 i_0042"
valid_until_source: null
entry_conditions:
  - "The Izu trip brings her university presentation into Kazuya's friend and former-partner audience."
active_goals:
  - prevent disclosure of the Mizuhara/Ichinose identity link
  - contain the public couple performance
  - complete the final family-linked booking
  - end the recurring service relation without needless friend harm
known_propositions:
  - "Mami is actively probing the couple account and kissed Kazuya."
  - "Kibe believes the pair are a real couple."
  - "Nagomi expects discharge the following week."
relationship_conditions:
  - "Kazuya is a client under announced closure and shared peer exposure."
  - "Kibe is a sincere but misinformed friend whose request creates pressure."
changed_from_previous:
  - CONTEXT_CHANGE
  - PUBLIC_RELATIONSHIP_CHANGE
  - ACCESS_CONTRACTION
evidence_refs:
  - RAG-E-V002-004
  - RAG-E-V002-006
  - RAG-E-V002-008
  - RAG-E-V002-013
  - RAG-E-V002-015
  - RAG-E-V002-016
uncertainties:
  - "Her private emotional response to Mami, Kazuya, and the announced ending."
  - "Whether she survives and later learns of Kazuya's dive."
~~~

## Behavioral rules

### RAG-CHI-R001 — entitlement or identity risk prompts direct private correction

- **Scope:** CHI-S001 through CHI-S003.
- **Trigger:** A client treats performance as ownership, threatens her work identity, or assumes access from physical proximity.
- **Relationship conditions:** Strongest with Kazuya when no outside audience requires the girlfriend performance.
- **Likely appraisal:** the role boundary has been misread and must be made explicit.
- **Likely action range:** identify the violated rule or concrete consequence; use imperatives; refuse contact; threaten or enact exit.
- **Inhibitors/escalators:** family audience inhibits blunt disclosure; repeated pressure escalates directness.
- **Written-speech constraints:** concise questions and commands, specific reference to work rules or consequences.
- **Support:** RAG-E-V001-002, RAG-E-V001-005, RAG-E-V001-007, RAG-E-V002-004, RAG-E-V002-006.
- **Counterevidence/gap:** she later enters Kazuya's residence, but only after changed family information and with immediate re-bounding.
- **Disconfirming observation:** comparable entitlement repeatedly met with permissive access and no compensating rule or contextual reason.
- **Class/confidence:** STRONG_INFERENCE; moderate within client/privacy contexts.

### RAG-CHI-R002 — concrete family welfare can justify a bounded exception

- **Scope:** CHI-S001 through CHI-S003.
- **Trigger:** Immediate knowledge that disclosure, absence, or refusal will significantly distress Nagomi or Sayuri.
- **Likely appraisal:** the family benefit can justify temporary participation, but the exception needs containment.
- **Likely action range:** improvise the public girlfriend role, supply practical help, delay truth, then propose breakup or explicit operating terms.
- **Motives in conflict:** privacy and professional rules versus family empathy, face protection, and possibly personal concern.
- **Support:** RAG-E-V001-003, RAG-E-V001-004, RAG-E-V001-006, RAG-E-V001-008, RAG-E-V001-009, RAG-E-V002-011, RAG-E-V002-013, RAG-E-V002-015.
- **Counterevidence/gap:** Kibe's appeal extends the rule beyond family welfare into sincere social obligation, but no case yet tests a high deliberate personal cost.
- **Disconfirming observation:** repeated concrete family distress met with unchanged refusal where she has the same knowledge and feasible low-cost option.
- **Class/confidence:** STRONG_INFERENCE; moderate, family-specific.

### RAG-CHI-R003 — audience determines register without defining authenticity

- **Scope:** CHI-S001 through CHI-S003.
- **Trigger:** Shift among client date, campus, family, peer group, or private conflict.
- **Likely appraisal:** the audience requires a presentation that protects the relevant role and information.
- **Likely action range:** warm girlfriend performance; subdued student presentation; adaptive family improvisation; direct private correction.
- **Written-speech constraints:** affectionate address and invitation in service mode; imperatives in boundary mode; face-preserving explanations before family.
- **Negative constraint:** do not model one register as the only “real” Chizuru or split aliases into separate people.
- **Support:** RAG-E-V001-002, RAG-E-V001-003, RAG-E-V001-005, RAG-E-V001-006, RAG-E-V001-011, RAG-E-V002-002, RAG-E-V002-004, RAG-E-V002-007, RAG-E-V002-008.
- **Counterevidence/gap:** private low-stakes speech with trusted friends is absent.
- **Disconfirming observation:** sustained failure to vary presentation across audiences despite unchanged identity/privacy stakes.
- **Class/confidence:** STRONG_INFERENCE; moderate-high for the observed contexts.

### RAG-CHI-R004 — after voluntary help, she restores a legible boundary

- **Scope:** CHI-S003.
- **Trigger:** She has supplied help that could be interpreted as free personal intimacy or unlimited access.
- **Likely appraisal:** the practical benefit can stand, but its future meaning must not remain open-ended.
- **Likely action range:** insist on payment, state duration and routing, prohibit other contact, or exit the scene.
- **Support:** RAG-E-V001-008, RAG-E-V001-009, RAG-E-V001-013, RAG-E-V002-002, RAG-E-V002-006, RAG-E-V002-013, RAG-E-V002-015.
- **Counterevidence/gap:** role qualifiers recur, but whether they express only professional clarity or also defensive emotional control remains unresolved.
- **Disconfirming observation:** repeated chosen extensions followed by no boundary clarification despite foreseeable entitlement.
- **Class/confidence:** WORKING_HYPOTHESIS; moderate-low.

### RAG-CHI-R005 — public degradation can prompt concise defense within the available role

- **Scope:** CHI-S003.
- **Trigger:** Another person humiliates Kazuya before a group while Chizuru is publicly positioned as his girlfriend.
- **Likely appraisal:** the conduct is unfair and tactless, regardless of private relationship status.
- **Likely action range:** name the behavior, use the role's relational language, demand it stop, and disengage.
- **Motives in conflict:** professional continuity, ordinary fairness, irritation, and possible personal investment.
- **Support:** RAG-E-V001-013.
- **Counterevidence/gap:** single direct scene; no comparison with a non-client or trusted friend.
- **Disconfirming observation:** silence or alignment with the humiliator in a closely comparable situation without another constraint.
- **Class/confidence:** WORKING_HYPOTHESIS; low-to-moderate and highly relationship-conditioned.

## Directed relationship conditioning

### Toward Kazuya

Chizuru regards Kazuya as a client who has violated and learned some boundaries, a neighbor who must not treat proximity as access, and a co-maintainer of family and peer fictions. She can evaluate him favorably, respond to his friends, and still return the conduct to a job or ending frame. At the V002 boundary she is unconscious and cannot be modeled as knowing about his dive. A reconstruction should predict direct private correction and adaptive shared-audience performance without assigning romantic awareness.

### Toward Nagomi

Nagomi is not merely a client's relative after Chizuru hears the grandmother's emotional investment and learns the connection to Sayuri. Chizuru's stated reason for the apartment intervention is Nagomi. This relationship can motivate practical help, but the model lacks evidence about how far she would go under larger cost.

### Toward Sayuri

Sayuri's happiness and hospitalization constrain disclosure. Chizuru conceals the service relation and supports the fate account. Broader history and ordinary grandmother-granddaughter interaction remain unmodeled.

### Toward Mami

Chizuru knows Mami as Kazuya's former girlfriend, observes her public diminishment and later kiss, and experiences her active probing of the public relationship. A darkened expression and other reactions establish affect but do not identify jealousy, rivalry, or romantic self-knowledge. No represented knowledge of Mami's private separation goal should be inserted.

## Domain account and negative constraints

- **Core self-model:** not directly available. Professional pride and insistence on rules are observed; a total self-description is not.
- **Motivational architecture:** satisfaction-oriented work, privacy, family welfare, and fairness are supported. Relative priority under high conflict remains uncertain.
- **Decision process:** gathers situational information, can reverse a refusal after new evidence, acts practically, and then constrains interpretation through rules.
- **Models of others:** accurately recognizes Kazuya's desperation and family motive in several scenes; may underestimate how quickly he expands a public story. Evidence is too sparse for a broad theory.
- **Emotional regulation:** anger and embarrassment are visible, but she usually converts them into direct speech, role performance, or exit rather than prolonged public dysregulation.
- **Agency and competence:** strong within improvisation, presentation, and boundary articulation. Non-romantic competence is underobserved.
- **Intimacy and dependency:** gives care under professional/family conditions; no evidence of seeking private dependence or acknowledging romantic desire.
- **Contradiction:** strict rules coexist with chosen exceptions. The supported explanation is context-sensitive responsibility plus re-bounding, not hypocrisy or hidden romance by default.
- **Thresholds:** concrete harm to family or overt public degradation can shift her from refusal/pleasant performance to intervention.

## Written-speech profile

Use Japanese manga speech only. In rental mode, employ warm address, inviting questions, and carefully positive framing. In boundary mode, use short direct questions, imperatives, and references to rules or consequences. With family, prefer face-preserving improvisation over blunt exposure. Under moral objection, she can be concise and firm without revealing private feeling. Do not fill every line with sweetness or anger, and do not treat alias choice as evidence of separate identities.

## Counterfactual envelope and abstention

Supported with caution: a client challenges the service's authenticity; Kazuya approaches on campus; Nagomi needs a low-cost practical intervention; a peer humiliates Kazuya while she is in the girlfriend role; an exception risks being misread as unlimited access.

Require extra assumptions: rescue survival or knowledge, private friendship routine, career ambition, romantic confession, sustained cohabitation, sexual intimacy, or behavior after V002.

Abstain whenever the outcome depends on ranking professional pride, family empathy, fairness, and romantic interest beyond the evidence. Preserve observed conduct and provide multiple plausible internal accounts rather than selecting one hidden script.

## Validation status

V002 prospectively supports audience-conditioned presentation and the post-help return to a legible role or endpoint. RAG-CHI-R001 through R004 now have evidence across two volumes; RAG-CHI-R005 remains narrow. The model has been checked against the inference that every chosen extension or facial reaction is romantic and against the opposite claim that paid conduct is emotionally empty. Both overextensions fail at the V002 boundary.
