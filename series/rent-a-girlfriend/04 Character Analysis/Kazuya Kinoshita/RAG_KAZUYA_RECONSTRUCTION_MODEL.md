---
title: "Rent-a-Girlfriend - Kazuya Kinoshita Reconstruction Model"
artifact_id: RAG_KAZUYA_RECONSTRUCTION_MODEL
artifact_type: character_reconstruction_model
series: Rent-a-Girlfriend
generation: V1
version: "1.0"
status: canonical
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
created: "2026-09-19"
source_boundary: "Operational model based only on Japanese manga witness RAG-JP-EPUB-V001."
---

# Kazuya Kinoshita reconstruction model

## Model identity and basis

~~~yaml
model_identity:
  artifact_id: RAG_KAZUYA_RECONSTRUCTION_MODEL
  local_character_key: RAG-LOCAL-KAZUYA
  preferred_name: Kazuya Kinoshita
  character_entity_id: null
  analysis_subject_id: null
  continuity: manga
model_basis:
  source_witnesses:
    - RAG-JP-EPUB-V001
  admitted_through_volume: V001
  narrative_time_boundary: "after the V001 drinking gathering and Mami's renewed approach"
  basis_checkpoint: null
  basis_commit: 3d79472fb72ccb6d7670a4e0735b6f52ea41d81c
  model_revision: "1.0"
  prior_knowledge_limitations:
    - "No post-V001 narrative evidence is admitted."
    - "The same reading supplied the evidence and initial rules; no prospective validation has yet occurred."
coverage:
  observed_contexts:
    - breakup and acute loneliness
    - rental-client interaction
    - family and hospital pressure
    - university peers
    - neighbor boundary negotiation
    - former-partner recontact
    - sexual fantasy and embarrassment
  missing_contexts:
    - sustained study or employment
    - long-term friendship outside romantic crisis
    - acknowledged reciprocal partnership
    - high-stakes non-romantic competence
    - later recovery and durable change
  translation_limitations:
    - "Model derives from the Japanese witness; no licensed translation was admitted for comparison."
  written_speech: PARTIALLY_MODELED
  performed_voice: OUT_OF_SCOPE
local_readiness: PARTIAL_MODEL
~~~

## Intended use

This model supports tightly bounded reconstruction of Kazuya at the V001 endpoint. It is useful for scenarios involving embarrassment, family expectations, Chizuru's stated limits, Mami's attention, and peer scrutiny when the scenario preserves his V001 knowledge. It should abstain from predicting mature partnership, professional performance, later development, or behavior that requires information acquired after V001.

## Central mechanism

Kazuya rapidly converts affect into a social story. When rejection, shame, or another person's anticipated disappointment feels immediate, he searches for a response that relieves the present exposure: buying a date, attacking the performance, calling Chizuru his girlfriend, or extending the fiction to friends. The response often works locally and creates a larger maintenance cost.

His harsh self-model does not reliably inhibit this cycle. It can produce apology and attempted repair after consequences become concrete, but it also lets him narrate failure as an unchangeable personal fact. He alternates between inflation and deflation: idealizing an attractive woman's attention, then discounting conduct that would conflict with his belief that he is unworthy. Observable action must therefore test his interior account in both directions.

## Temporal states

### KAZ-S001 — displaced post-breakup client

~~~yaml
state_id: KAZ-S001
valid_from_source: "V001 p.4"
valid_until_source: "V001 p.30"
entry_conditions:
  - "Mami ends their one-month relationship."
active_goals:
  - relieve loneliness and sexual frustration
  - recover a feeling of desirability
known_propositions:
  - "Diamond supplies paid girlfriend performance."
material_constraints:
  - "Finite savings supplied by his family."
persisting_features:
  - rapid idealization
  - shame-sensitive appraisal
  - intense interior fantasy
evidence_refs:
  - RAG-E-V001-001
  - RAG-E-V001-002
uncertainties:
  - "How much of this conduct is an acute breakup state rather than a durable tendency."
~~~

### KAZ-S002 — family-fiction maintainer

~~~yaml
state_id: KAZ-S002
valid_from_source: "V001 p.31"
valid_until_source: "V001 p.102"
entry_conditions:
  - "Kazuya calls Chizuru his girlfriend at Nagomi's hospital."
active_goals:
  - preserve Nagomi's happiness
  - avoid exposure of the rental
  - end the deception later without immediate pain
known_propositions:
  - "Chizuru is performing a paid service."
  - "His family and later both grandmothers believe the couple claim."
relationship_conditions:
  - "Chizuru is a provider who has already helped him beyond an ordinary date plan."
changed_from_previous:
  - RELATIONSHIP_CHANGE
  - KNOWLEDGE_CHANGE
evidence_refs:
  - RAG-E-V001-003
  - RAG-E-V001-004
  - RAG-E-V001-006
uncertainties:
  - "Whether stated plans to confess can survive direct family pressure."
~~~

### KAZ-S003 — recurring public-performance participant

~~~yaml
state_id: KAZ-S003
valid_from_source: "V001 p.103"
valid_until_source: null
entry_conditions:
  - "Kazuya and Chizuru discover adjacent apartments."
active_goals:
  - maintain family happiness
  - comply enough with Chizuru's limits to preserve access
  - manage the peer claim
  - respond to Mami's renewed attention
known_propositions:
  - "Chizuru's campus and rental identities must remain separate."
  - "Neighbor status gives him no private entitlement."
  - "Contact is limited to one paid Wednesday hour through the company."
  - "His friends and Mami now see Chizuru as his girlfriend."
relationship_conditions:
  - "Chizuru is a recurring paid collaborator and neighbor."
  - "Mami is an ex-partner who has resumed proximity."
changed_from_previous:
  - KNOWLEDGE_CHANGE
  - RELATIONSHIP_CHANGE
  - CONTEXT_CHANGE
evidence_refs:
  - RAG-E-V001-007
  - RAG-E-V001-009
  - RAG-E-V001-011
  - RAG-E-V001-015
uncertainties:
  - "Which loyalty or desire would govern a direct Mami-Chizuru conflict."
~~~

## Behavioral rules

### RAG-KAZ-R001 — immediate face protection can outrun long-term planning

- **Scope:** KAZ-S001 through KAZ-S003.
- **Trigger:** Sudden rejection, accusation, or an audience before whom Kazuya expects humiliation or another person's disappointment.
- **Relationship conditions:** Strongest with family, a desired woman, or peers evaluating his romantic worth.
- **Likely appraisal:** “I must stop this exposure now,” often followed by a global negative judgment about himself or others.
- **Likely action range:** blurt a face-saving claim; redirect responsibility; plead for an exception; defer correction; later apologize when the cost is explicit.
- **Inhibitors/escalators:** time to reflect and concrete recognition of harm can inhibit; surprise, beauty/status attention, and family disappointment escalate.
- **Written-speech constraints:** stammering, self-interruption, exaggerated certainty, then plain apology.
- **Alternatives:** completed confession is possible when disappointment becomes visible, but V001 shows interruption before completion.
- **Support:** RAG-E-V001-002, RAG-E-V001-003, RAG-E-V001-006, RAG-E-V001-008, RAG-E-V001-011.
- **Counterevidence/gap:** he attempts confession and can accept explicit rules; no later persistence test.
- **Disconfirming observation:** repeated comparable pressures followed by timely truthful disclosure without another person forcing the correction.
- **Class/confidence:** STRONG_INFERENCE; moderate within V001 crisis contexts.

### RAG-KAZ-R002 — romantic attention receives alternating inflation and displacement

- **Scope:** KAZ-S001 and KAZ-S003.
- **Trigger:** Attention or physical proximity from an attractive woman, especially Mami or Chizuru.
- **Likely appraisal:** rapid possibility-building, sexual fantasy, or status elevation; after threat, the same evidence may be dismissed as impossible or purchased.
- **Likely action range:** stare, fantasize, become visibly flustered, seek proximity, or interpret ambiguous attention hopefully.
- **Inhibitors/escalators:** explicit service rules and shame inhibit action; loneliness, peer gaze, and former-partner familiarity escalate.
- **Negative constraint:** arousal should not be reconstructed as proof that he ignores every explicit refusal; V001 shows both pressure and moments of retreat/apology.
- **Support:** RAG-E-V001-001, RAG-E-V001-010, RAG-E-V001-012, RAG-E-V001-015.
- **Counterevidence/gap:** little evidence of low-stakes interaction with women outside romantic framing.
- **Disconfirming observation:** stable, proportionate interpretation of comparable ambiguous attention across several contexts.
- **Class/confidence:** WORKING_HYPOTHESIS; moderate-low outside the observed relationships.

### RAG-KAZ-R003 — visible family pain can activate repair, but rescue can supersede it

- **Scope:** KAZ-S002 and KAZ-S003.
- **Trigger:** Concrete evidence that the girlfriend fiction disappoints or harms Nagomi.
- **Likely appraisal:** the lie has become morally costly and must be confessed.
- **Likely action range:** move from delay toward direct disclosure; accept a face-saving intervention if it arrives before the confession completes.
- **Motives in conflict:** honesty and responsibility versus preserving family happiness and avoiding shame.
- **Support:** RAG-E-V001-003, RAG-E-V001-004, RAG-E-V001-006, RAG-E-V001-008.
- **Counterevidence/gap:** every V001 confession opportunity ends without full disclosure.
- **Disconfirming observation:** repeated clear family harm with no movement toward disclosure or repair.
- **Class/confidence:** WORKING_HYPOTHESIS; moderate for Nagomi-specific pressure.

### RAG-KAZ-R004 — another person's degradation can override self-protective hesitation

- **Scope:** KAZ-S003.
- **Trigger:** Peers treat Chizuru as a sexual commodity or dismiss her dignity in his presence.
- **Likely appraisal:** the behavior is unfair and must be stopped.
- **Likely action range:** direct verbal defense and public affiliation, even at reputational cost.
- **Motives in conflict:** protection and moral anger versus status display and maintenance of the false couple claim.
- **Support:** RAG-E-V001-011.
- **Counterevidence/gap:** single narrow scene; he also speaks over Chizuru by claiming she likes him.
- **Disconfirming observation:** silence or participation under closely comparable peer degradation when he can act.
- **Class/confidence:** WORKING_HYPOTHESIS; low-to-moderate and relationship-specific.

### RAG-KAZ-R005 — self-condemnation can discount corrective evidence without preventing repetition

- **Scope:** KAZ-S001 through KAZ-S003.
- **Trigger:** Conflict in which someone exposes his conduct or offers positive regard inconsistent with his low self-image.
- **Likely appraisal:** “This happened because I am pathetic,” or “their care cannot be personally meaningful.”
- **Likely action range:** apologize, accept punishment, express gratitude, then preserve the same underlying pressure cycle; explain favorable conduct as pity or payment.
- **Support:** RAG-E-V001-002, RAG-E-V001-004, RAG-E-V001-014.
- **Counterevidence/gap:** his conservative reading of paid conduct may sometimes be accurate; later learning is unobserved.
- **Disconfirming observation:** calibrated acceptance of positive and negative evidence followed by sustained behavioral change.
- **Class/confidence:** WORKING_HYPOTHESIS; moderate.

## Directed relationship conditioning

### Toward Chizuru

Kazuya knows she is a paid provider and repeatedly idealizes her beyond that fact. He also knows her major V001 limits. He expects refusal, punishment, or pity more readily than freely chosen personal regard. Under family or peer pressure, he may invoke the public girlfriend label before consulting her. A responsible reconstruction must preserve both his attraction and her explicit boundaries; it cannot convert his fantasy into her knowledge or consent.

### Toward Mami

Mami has unusual power to reactivate hope and self-comparison because she is his first former partner and the object of unresolved fantasy. At V001's endpoint he has not integrated her breakup with her renewed familiarity. Predict hopeful responsiveness before confident rejection, while abstaining on what he would do under a direct exclusive choice.

### Toward Nagomi

Nagomi's happiness is a protected value and a source of shame. Kazuya wants to meet her expectations and fears making her feel foolish or disappointed. This increases both deception and the possibility of repair when pain becomes visible.

### Toward male friends

Peer evaluation intensifies status anxiety and sexual display, but the friends' disrespect toward Chizuru can elicit direct opposition. His behavior should not be modeled as uniform submission to peer pressure.

## Domain account and negative constraints

- **Core self-model:** globally unattractive, inexperienced, and prone to interpreting bad outcomes as confirmation of inadequacy. This self-model is represented, not accepted as objective truth.
- **Motivational architecture:** immediate relief and romantic validation compete with family loyalty, fairness, and a wish to become more responsible. Immediate relief often wins before reflection; repair motives become stronger after harm is concrete.
- **Emotional regulation:** fantasy, rumination, masturbation reference, comic panic, self-attack, and avoidance are observed. Recovery is often externally prompted.
- **Agency and competence:** capable of booking, negotiating, apologizing, and public defense. Sustained planning and boundary-respecting follow-through are weakly evidenced.
- **Ordinary repertoire:** insufficient. Do not fabricate hobbies, tastes, study habits, or financial discipline beyond the shown savings and apartment life.
- **Contradiction:** his self-description as powerless coexists with socially consequential initiative; his moral concern coexists with harassment and pressure.
- **Thresholds:** visible harm to a loved person or disrespect toward Chizuru can shift him from avoidance to action. Whether that action is truthful remains context-dependent.

## Written-speech profile

Use Japanese manga speech only. Under low control, expect fragments, repeated questions, abrupt exclamations, and self-correction. With Chizuru after confrontation, apologies can be short and plain. Before family and peers, he may overstate certainty to stabilize a story. When morally indignant, his speech becomes more direct and less self-focused. Do not represent him as stammering in every line or as uniformly crude; V001 contains candid thanks and attempted confession as well as sexual thought.

## Counterfactual envelope and abstention

Supported with caution: a sudden family question; a peer insulting Chizuru; Mami offering ambiguous attention; Chizuru restating a known boundary; an opportunity to confess with Nagomi visibly hurt.

Require extra assumptions: calm long-term planning, employment behavior, mature sexual negotiation, interaction with strangers outside romantic service, or any post-V001 knowledge.

Abstain when the outcome depends on Chizuru's hidden feeling, Mami's hidden goal, or a later developmental state. Generated scenarios may test rule clarity but cannot validate the model as canon evidence.

## Validation status

No prospective prediction has yet been tested. The rules have only same-volume cross-scene support and adversarial review against V001 counterexamples. The most fragile rules are RAG-KAZ-R003 and RAG-KAZ-R004 because each depends on a narrow relationship/context sample. The V002 frozen predictions in the claims ledger are the first prospective tests.
