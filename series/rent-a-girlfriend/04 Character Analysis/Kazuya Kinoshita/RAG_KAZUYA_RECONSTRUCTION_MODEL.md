---
title: "Rent-a-Girlfriend - Kazuya Kinoshita Reconstruction Model"
artifact_id: RAG_KAZUYA_RECONSTRUCTION_MODEL
artifact_type: character_reconstruction_model
series: Rent-a-Girlfriend
generation: V1
version: "1.2"
status: canonical
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
created: "2026-09-19"
source_boundary: "Operational model based only on Japanese manga witnesses RAG-JP-EPUB-V001-V003."
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
    - RAG-JP-EPUB-V002
    - RAG-JP-EPUB-V003
  admitted_through_volume: V003
  narrative_time_boundary: "after Ruka tells Kazuya that she too is a rental girlfriend at the V003 cliffhanger"
  basis_checkpoint: null
  basis_commit: 3d79472fb72ccb6d7670a4e0735b6f52ea41d81c
  model_revision: "1.2"
  prior_knowledge_limitations:
    - "No post-V003 narrative evidence is admitted."
    - "Ruka's contract, motive, secrecy terms, and relationship with Kuribayashi are unknown."
coverage:
  observed_contexts:
    - breakup and acute loneliness
    - rental-client interaction
    - family and hospital pressure
    - university peers
    - neighbor boundary negotiation
    - former-partner recontact
    - sexual fantasy and embarrassment
    - overnight peer travel and identity collision
    - partial public correction and friend conflict
    - acute physical emergency
    - reciprocal rescue and recovery
    - family-engineered hot-spring travel
    - bounded shared lodging
    - conscious attachment recognition
    - third-party rental-secret exposure
  missing_contexts:
    - sustained study or employment
    - long-term friendship outside romantic crisis
    - acknowledged reciprocal partnership
    - high-stakes non-romantic competence
    - durable honesty and later development
  translation_limitations:
    - "Model derives from the Japanese witness; no licensed translation was admitted for comparison."
  written_speech: PARTIALLY_MODELED
  performed_voice: OUT_OF_SCOPE
local_readiness: PARTIAL_MODEL
~~~

## Intended use

This model supports tightly bounded reconstruction of Kazuya at the V003 endpoint. It is useful for scenarios involving embarrassment, family expectations, Chizuru's stated limits, Mami's attention, peer scrutiny, partial truth correction, protective action, and Ruka's knowledge when the scenario preserves his V003 knowledge. It should abstain from predicting Ruka's terms, mature partnership, professional performance, later development, or behavior that requires information acquired after V003.

## Central mechanism

Kazuya rapidly converts affect into a social story. When rejection, shame, or another person's anticipated disappointment feels immediate, he searches for a response that relieves the present exposure: buying a date, attacking the performance, calling Chizuru his girlfriend, or extending the fiction to friends. The response often works locally and creates a larger maintenance cost.

His harsh self-model does not reliably inhibit this cycle. It can produce apology and attempted repair after consequences become concrete, but it also lets him narrate failure as an unchangeable personal fact. He alternates between inflation and deflation: idealizing an attractive woman's attention, then discounting conduct that would conflict with his belief that he is unworthy. V003 adds a limited change in self-knowledge: he recognizes serious feeling for Chizuru and explains the deception to Ruka through family consequence, yet still chooses paid access over disclosure and pursues Ruka past a stated distance boundary. Observable action must test his interior account in both directions.

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
valid_until_source: "V002 i_0118"
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

### KAZ-S004 — attempted closer under divided attachment and emergency

~~~yaml
state_id: KAZ-S004
valid_from_source: "V002 i_0119"
valid_until_source: "V003 0001"
entry_conditions:
  - "Nagomi's discharge schedule and the Izu audience make an endpoint immediately actionable."
active_goals:
  - complete the final family-linked booking
  - tell friends that the public couple is ending
  - confess to Mami after disembarkation
  - eventually disclose the rental truth to Kibe
known_propositions:
  - "Mami deliberately kissed him and wants a private meeting."
  - "Kibe believes Chizuru is a real partner being discarded."
  - "Chizuru considers the upcoming booking the final hospital-linked use."
  - "Chizuru is missing overboard at the volume endpoint."
relationship_conditions:
  - "Chizuru is an announced former/final rental partner whose rescue he attempts."
  - "Mami is a desired former partner awaiting a meeting."
  - "Kibe is a caring but deceived friend."
changed_from_previous:
  - GOAL_CHANGE
  - PUBLIC_RELATIONSHIP_CHANGE
  - EMERGENCY_CONTEXT_CHANGE
evidence_refs:
  - RAG-E-V002-011
  - RAG-E-V002-012
  - RAG-E-V002-015
  - RAG-E-V002-016
  - RAG-E-V002-017
uncertainties:
  - "Rescue outcome and whether the planned breakup, meeting, or disclosures survive it."
~~~

### KAZ-S005 — consciously attached client under renewed terms and third-party exposure

~~~yaml
state_id: KAZ-S005
valid_from_source: "V003 0001"
valid_until_source: null
entry_conditions:
  - "Chizuru revives Kazuya and the rescue gains public and private consequences."
active_goals:
  - understand and preserve contact with Chizuru
  - protect Chizuru from disclosure of the rental secret
  - avoid harming Nagomi, Sayuri, and Kuribayashi through the existing fictions
  - respond to Ruka's informed challenge
known_propositions:
  - "Chizuru consciously saved him through CPR."
  - "His serious feeling for Chizuru is no longer only an unformulated action tendency."
  - "Chizuru permits continued rental until a real girlfriend triggers the exit rule."
  - "Ruka knows the central secret and says she is also a rental girlfriend."
relationship_conditions:
  - "Chizuru is a valued provider and deception partner whose continued access remains paid."
  - "Ruka is an informed third party with explicit boundaries and unresolved leverage."
changed_from_previous:
  - KNOWLEDGE_CHANGE
  - SELF_REPORT_CHANGE
  - ACCESS_RECONFIGURATION
  - INFORMATION_RISK_CHANGE
evidence_refs:
  - RAG-E-V003-001
  - RAG-E-V003-005
  - RAG-E-V003-009
  - RAG-E-V003-010
  - RAG-E-V003-014
  - RAG-E-V003-015
  - RAG-E-V003-016
uncertainties:
  - "Whether recognized feeling produces honest, sustained, boundary-respecting conduct."
  - "How Ruka will use the secret and whether she becomes a real-girlfriend candidate."
~~~

## Behavioral rules

### RAG-KAZ-R001 — immediate face protection can outrun long-term planning

- **Scope:** KAZ-S001 through KAZ-S005.
- **Trigger:** Sudden rejection, accusation, or an audience before whom Kazuya expects humiliation or another person's disappointment.
- **Relationship conditions:** Strongest with family, a desired woman, or peers evaluating his romantic worth.
- **Likely appraisal:** “I must stop this exposure now,” often followed by a global negative judgment about himself or others.
- **Likely action range:** blurt a face-saving claim; redirect responsibility; plead for an exception; defer correction; later apologize when the cost is explicit.
- **Inhibitors/escalators:** time to reflect and concrete recognition of harm can inhibit; surprise, beauty/status attention, and family disappointment escalate.
- **Written-speech constraints:** stammering, self-interruption, exaggerated certainty, then plain apology.
- **Alternatives:** completed confession is possible when disappointment becomes visible, but V001 shows interruption before completion.
- **Support:** RAG-E-V001-002, RAG-E-V001-003, RAG-E-V001-006, RAG-E-V001-008, RAG-E-V001-011, RAG-E-V002-005, RAG-E-V002-008, RAG-E-V002-012, RAG-E-V003-006, RAG-E-V003-014.
- **Counterevidence/gap:** he makes a costly partial public correction and plans fuller disclosure, so avoidance is neither total nor immutable.
- **Disconfirming observation:** repeated comparable pressures followed by timely truthful disclosure without another person forcing the correction.
- **Class/confidence:** STRONG_INFERENCE; moderate within V001 crisis contexts.

### RAG-KAZ-R002 — romantic attention receives alternating inflation and displacement

- **Scope:** KAZ-S001, KAZ-S003, and KAZ-S005.
- **Trigger:** Attention or physical proximity from an attractive woman, especially Mami or Chizuru.
- **Likely appraisal:** rapid possibility-building, sexual fantasy, or status elevation; after threat, the same evidence may be dismissed as impossible or purchased.
- **Likely action range:** stare, fantasize, become visibly flustered, seek proximity, or interpret ambiguous attention hopefully.
- **Inhibitors/escalators:** explicit service rules and shame inhibit action; loneliness, peer gaze, and former-partner familiarity escalate.
- **Negative constraint:** arousal should not be reconstructed as proof that he ignores every explicit refusal; V001 shows both pressure and moments of retreat/apology.
- **Support:** RAG-E-V001-001, RAG-E-V001-010, RAG-E-V001-012, RAG-E-V001-015, RAG-E-V002-005, RAG-E-V002-006, RAG-E-V002-009, RAG-E-V002-010, RAG-E-V003-005, RAG-E-V003-012.
- **Counterevidence/gap:** he refuses the Pocky kiss and acts for Chizuru under emergency; little low-stakes interaction with women exists outside romantic framing.
- **Disconfirming observation:** stable, proportionate interpretation of comparable ambiguous attention across several contexts.
- **Class/confidence:** WORKING_HYPOTHESIS; moderate-low outside the observed relationships.

### RAG-KAZ-R003 — visible family pain can activate repair, but rescue can supersede it

- **Scope:** KAZ-S002 through KAZ-S005.
- **Trigger:** Concrete evidence that the girlfriend fiction disappoints or harms Nagomi.
- **Likely appraisal:** the lie has become morally costly and must be confessed.
- **Likely action range:** move from delay toward direct disclosure; accept a face-saving intervention if it arrives before the confession completes.
- **Motives in conflict:** honesty and responsibility versus preserving family happiness and avoiding shame.
- **Support:** RAG-E-V001-003, RAG-E-V001-004, RAG-E-V001-006, RAG-E-V001-008, RAG-E-V002-011, RAG-E-V002-012, RAG-E-V002-015, RAG-E-V002-016, RAG-E-V003-006, RAG-E-V003-007, RAG-E-V003-015.
- **Counterevidence/gap:** V003 supplies direct explanation to Ruka and another planned breakup, but still no completed truth disclosure to family or friends.
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

- **Scope:** KAZ-S001 through KAZ-S005.
- **Trigger:** Conflict in which someone exposes his conduct or offers positive regard inconsistent with his low self-image.
- **Likely appraisal:** “This happened because I am pathetic,” or “their care cannot be personally meaningful.”
- **Likely action range:** apologize, accept punishment, express gratitude, then preserve the same underlying pressure cycle; explain favorable conduct as pity or payment.
- **Support:** RAG-E-V001-002, RAG-E-V001-004, RAG-E-V001-014, RAG-E-V002-006, RAG-E-V002-013, RAG-E-V002-017, RAG-E-V003-003, RAG-E-V003-005, RAG-E-V003-015.
- **Counterevidence/gap:** his conservative reading of paid conduct may sometimes be accurate; V003 adds conscious feeling without sustained follow-through.
- **Disconfirming observation:** calibrated acceptance of positive and negative evidence followed by sustained behavioral change.
- **Class/confidence:** WORKING_HYPOTHESIS; moderate.

### RAG-KAZ-R006 — acute threat can compress rumination into direct protective action

- **Scope:** KAZ-S004 and KAZ-S005.
- **Trigger:** Concrete evidence that Chizuru is in immediate physical danger and delay may be fatal.
- **Likely appraisal:** the missing passenger is Chizuru and action cannot wait for certainty or social permission.
- **Likely action range:** infer rapidly from available evidence and accept personal risk before narrating a complete motive.
- **Inhibitors/escalators:** acute time pressure escalates action; no comparable non-romantic emergency is available.
- **Support:** RAG-E-V002-017, RAG-E-V003-001, RAG-E-V003-015.
- **Counterevidence/gap:** the Ruka catch extends the pattern beyond Chizuru, but both cases concern attractive women inside relationship crises; broad generality remains unknown.
- **Disconfirming observation:** repeated comparable immediate danger to a valued person followed by self-protective delay despite feasible action.
- **Class/confidence:** WORKING_HYPOTHESIS; low and emergency-specific.

## Directed relationship conditioning

### Toward Chizuru

Kazuya knows she is a paid provider and privately recognizes serious feeling for her. He knows she revived him and that she permits continued rental only under a temporary, nonexclusive rule. He expects role duty more readily than freely chosen personal regard and has not disclosed his feeling to her. Reciprocal rescue demonstrates significance and care without establishing her romantic reciprocation.

### Toward Mami

Mami has unusual power to reactivate hope and self-comparison because she is his first former partner and the object of unresolved fantasy. V002 shows hopeful responsiveness to her kiss and a plan to confess, alongside refusal of a second game-induced kiss. V003 cancels the meeting and shifts his conscious attention toward Chizuru; do not erase the earlier attachment or assume the confession remains his active priority.

### Toward Nagomi

Nagomi's happiness is a protected value and a source of shame. Kazuya wants to meet her expectations and fears making her feel foolish or disappointed. This increases both deception and the possibility of repair when pain becomes visible.

### Toward male friends

Peer evaluation intensifies status anxiety and sexual display, but the friends' disrespect toward Chizuru can elicit direct opposition. His behavior should not be modeled as uniform submission to peer pressure.

### Toward Ruka

Ruka is an attractive third party who knows the rental truth and states explicit distance boundaries. Kazuya's protective goal leads him to pursue and plead past one boundary, including accidental protested contact; later he catches her fall and speaks directly about family consequence and Chizuru's value. Predict urgency and overpursuit under exposure risk, not entitlement to intimacy or knowledge of Ruka's motive.

## Domain account and negative constraints

- **Core self-model:** globally unattractive, inexperienced, and prone to interpreting bad outcomes as confirmation of inadequacy. This self-model is represented, not accepted as objective truth.
- **Motivational architecture:** immediate relief and romantic validation compete with family loyalty, fairness, and a wish to become more responsible. Immediate relief often wins before reflection; repair motives become stronger after harm is concrete.
- **Emotional regulation:** fantasy, rumination, masturbation reference, comic panic, self-attack, and avoidance are observed. Recovery is often externally prompted.
- **Agency and competence:** capable of booking, negotiating, apologizing, and public defense. Sustained planning and boundary-respecting follow-through are weakly evidenced.
- **Ordinary repertoire:** insufficient. Do not fabricate hobbies, tastes, study habits, or financial discipline beyond the shown savings, apartment life, bouldering date, and travel contexts.
- **Contradiction:** his self-description as powerless coexists with socially consequential initiative; his moral concern coexists with harassment and pressure.
- **Thresholds:** visible harm to a loved person or disrespect toward Chizuru can shift him from avoidance to action. Whether that action is truthful remains context-dependent.

## Written-speech profile

Use Japanese manga speech only. Under low control, expect fragments, repeated questions, abrupt exclamations, and self-correction. With Chizuru after confrontation, apologies can be short and plain. Before family and peers, he may overstate certainty to stabilize a story. When morally indignant, his speech becomes more direct and less self-focused. Do not represent him as stammering in every line or as uniformly crude; V001 contains candid thanks and attempted confession as well as sexual thought.

## Counterfactual envelope and abstention

Supported with caution: a sudden family question; a peer insulting Chizuru; Mami offering ambiguous attention; Chizuru restating a known boundary; Ruka threatening the secret; an opportunity to confess with Nagomi visibly hurt.

Require extra assumptions: calm long-term planning, employment behavior, mature sexual negotiation, Ruka's contract or motive, interaction with strangers outside romantic service, or any post-V003 knowledge.

Abstain when the outcome depends on Chizuru's hidden feeling, Mami's hidden goal, or a later developmental state. Generated scenarios may test rule clarity but cannot validate the model as canon evidence.

## Validation status

V003 supports the rescue-consequence predictions and supplies further evidence for RAG-KAZ-R001, RAG-KAZ-R002, RAG-KAZ-R003, RAG-KAZ-R005, and RAG-KAZ-R006. RAG-KAZ-R004 remains narrow. The model now includes conscious attachment and a second protective catch while withholding mature partnership, durable honesty, and broad competence.
