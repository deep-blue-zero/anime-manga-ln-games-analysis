---
title: "Rent-a-Girlfriend - Mini Yaemori Reconstruction Model"
artifact_id: RAG_MINI_RECONSTRUCTION_MODEL
artifact_type: character_reconstruction_model
series: Rent-a-Girlfriend
generation: V1
version: "1.0"
status: canonical
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
created: "2026-09-20"
source_boundary: "Operational model based only on Japanese manga witnesses RAG-JP-EPUB-V013-V020."
---

# Mini Yaemori reconstruction model

## Model identity and basis

~~~yaml
model_identity:
  artifact_id: RAG_MINI_RECONSTRUCTION_MODEL
  local_character_key: RAG-LOCAL-MINI
  preferred_name: Mini Yaemori
  character_entity_id: null
  analysis_subject_id: null
  continuity: manga
model_basis:
  source_witnesses:
    - RAG-JP-EPUB-V013
    - RAG-JP-EPUB-V014
    - RAG-JP-EPUB-V015
    - RAG-JP-EPUB-V016
    - RAG-JP-EPUB-V017
    - RAG-JP-EPUB-V018
    - RAG-JP-EPUB-V019
    - RAG-JP-EPUB-V020
  admitted_through_volume: V020
  narrative_time_boundary: "after Mini's earlier disclosure becomes an explicit premise in Chizuru's direct question to Kazuya, while Kazuya's answer remains interrupted"
  basis_checkpoint: RAG_CP_V020
  basis_commit: 940f1b3050e41ff0fac8a79fcdbb8260b0f0ca06
  model_revision: "1.0"
  prior_knowledge_limitations:
    - "No post-V020 narrative evidence is admitted."
    - "Mini does not witness the V020 interrupted declaration and cannot be assigned its missing completion."
    - "Her romantic readings are interested interpretations rather than privileged narrative truth."
coverage:
  observed_contexts:
    - accidental discovery of a concealed collaboration
    - voluntary entry into a family-purpose film project
    - creator and streamer self-description
    - crowdfunding analytics
    - stalled-campaign diagnosis
    - group convening and task distribution
    - explicit personal privacy boundary
    - direct relationship questioning
    - unauthorized romantic disclosure
    - disclosure accountability to Kazuya
    - deceptive trip logistics
    - admission after direct questioning
    - remote project contact
    - observation of Ruka's rival status pressure
    - post-support-event questioning
    - grief-confidant conversation with Chizuru
    - public peer-network address
  missing_contexts:
    - family and home history
    - sustained university routine
    - independent close friendships
    - creator workflow and long-term results
    - finances and material constraints
    - goals unrelated to creator work or Kazuya and Chizuru
    - response to a firm no-intervention boundary
    - durable confidentiality practice
  translation_limitations:
    - "Model derives from the Japanese witness; no licensed translation was admitted for comparison."
  written_speech: PARTIALLY_MODELED
  performed_voice: OUT_OF_SCOPE
local_readiness: PARTIAL_MODEL
~~~

## Intended use

This model supports bounded reconstruction of Mini when a measurable group problem invites coordination, when she interprets relational inertia as solvable, or when she moves information between Kazuya and Chizuru. It can estimate direct questions, rapid labeling, volunteer labor, analytics-based planning, access engineering, and interested mediation. It must abstain on private facts she has not received, broad creator competence, independent life goals, confidentiality under a clear prohibition, and any completion of V020's interrupted exchange.

## Central mechanism

Mini tends to convert ambiguity into a working theory and a next action. When she discovers the film collaboration, she rapidly interprets the pair, volunteers, and adopts a supporter role. When the campaign stalls, creator experience gives her a measurable problem: she analyzes the platform, convenes the group, and distributes tasks. When the relationship appears stalled, she treats information and access in a similar operational way, directly telling Chizuru that Kazuya likes her and later engineering a two-person trip through false absence information.

The same mechanism produces both competence and overreach. Mini is effective when the goal is shared, externally measurable, and within her creator knowledge. Her romantic interventions operate under weaker authorization and less reliable ground truth. She asks both principals, but she also privileges a mutual-romance interpretation even when Kazuya limits what a paid date proves and Chizuru denies boyfriend status. A useful reconstruction must preserve that distinction rather than treating every intervention as either benevolent insight or manipulation.

## Temporal states

### MIN-S001 — accidental discoverer turned volunteer

~~~yaml
state_id: MIN-S001
valid_from_source: "V013 0108"
valid_until_source: "V013 endpoint"
entry_conditions:
  - "Mini discovers Chizuru in Kazuya's room during private film planning."
active_goals:
  - understand the concealed collaboration
  - join the film effort
  - test her romantic interpretation of Kazuya and Chizuru
known_propositions:
  - "Kazuya and Chizuru are privately collaborating on a film for Sayuri."
  - "Their public relationship account does not explain the whole collaboration."
relationship_conditions:
  - "Mini is a nearby university junior without prior project authority."
changed_from_previous:
  - FIRST_OBSERVED_STATE
evidence_refs:
  - RAG-E-V013-012
  - RAG-E-V013-014
  - RAG-E-V013-016
uncertainties:
  - "Exact creator competence and the accuracy of her romantic reading."
~~~

### MIN-S002 — campaign analyst and direct intermediary

~~~yaml
state_id: MIN-S002
valid_from_source: "V014 0027"
valid_until_source: "V015 endpoint"
entry_conditions:
  - "Mini is accepted into the active film campaign."
active_goals:
  - help the all-or-nothing campaign succeed
  - support Kazuya
  - move Kazuya and Chizuru toward her preferred romantic clarification
known_propositions:
  - "The campaign has stalled and needs coordinated recovery."
  - "Chizuru describes gratitude and project trust without affirming romance."
  - "Kazuya likes Chizuru, based on Mini's conversations and inference."
relationship_conditions:
  - "Mini is a project teammate and self-designated supporter, not an authorized relationship representative."
changed_from_previous:
  - RELATIONSHIP_CHANGE
  - REVEALED_NOT_NEW
evidence_refs:
  - RAG-E-V014-004
  - RAG-E-V014-005
  - RAG-E-V014-011
  - RAG-E-V014-012
  - RAG-E-V014-013
  - RAG-E-V014-016
  - RAG-E-V014-017
  - RAG-E-V014-019
  - RAG-E-V015-001
  - RAG-E-V015-002
uncertainties:
  - "How much of the campaign outcome is attributable to her plan and whether either principal wants her continued mediation."
~~~

### MIN-S003 — access engineer under accountability pressure

~~~yaml
state_id: MIN-S003
valid_from_source: "V016 0034"
valid_until_source: "V018 endpoint"
entry_conditions:
  - "The filming trip offers a chance to create private access between Kazuya and Chizuru."
active_goals:
  - produce a two-person trip
  - preserve film logistics
  - advance her romantic interpretation through opportunity
known_propositions:
  - "Ruka would object to exclusion and has a competing status claim."
  - "Kazuya and Chizuru will travel together if the other participants appear unavailable."
relationship_conditions:
  - "Mini can alter logistics but lacks Ruka's consent to use her identity."
changed_from_previous:
  - CONTEXT_CHANGE
evidence_refs:
  - RAG-E-V016-004
  - RAG-E-V016-007
  - RAG-E-V017-007
uncertainties:
  - "Whether Mini changes her intervention threshold after the deception is exposed."
  - "V018 supplies no material new Mini conduct."
~~~

### MIN-S004 — aftermath interpreter and grief confidant

~~~yaml
state_id: MIN-S004
valid_from_source: "V019 0187"
valid_until_source: "V020 endpoint"
entry_conditions:
  - "Kazuya has completed a paid support date and Chizuru has privately accepted grief support."
active_goals:
  - determine what changed between the pair
  - encourage an ordinary relationship step
  - maintain separate information access to both principals
known_propositions:
  - "Kazuya refuses to treat the paid date as proof of romance."
  - "Chizuru experienced severe loneliness and relief but says Kazuya is not her boyfriend."
  - "Chizuru remembers Mini's earlier claim that Kazuya likes her."
relationship_conditions:
  - "Mini is a confidant and visible supporter but is not present for every central exchange."
changed_from_previous:
  - KNOWLEDGE_CHANGE
  - CONTEXT_CHANGE
evidence_refs:
  - RAG-E-V019-018
  - RAG-E-V019-020
  - RAG-E-V020-004
  - RAG-E-V020-016
uncertainties:
  - "Whether she will preserve Chizuru's confidence or relay it."
  - "What she would do after an explicit request to stop intervening."
~~~

## Behavioral rules

### RAG-MIN-R001 — a measurable shared problem activates volunteered expertise and coordination

- Scope: MIN-S001 through MIN-S003.
- Trigger: a group goal is concrete, time-bounded, and visibly lacks labor or platform knowledge.
- Relationship conditions: Mini has access to the team and can identify a useful contribution.
- Character knowledge required: the project's purpose, deadline, platform condition, and available participants.
- Likely appraisal: the problem can be decomposed into tasks rather than endured as vague worry.
- Likely action range: volunteer, explain relevant creator experience, inspect metrics, convene participants, distribute tasks, or remain reachable during execution.
- Support: RAG-E-V013-014, RAG-E-V014-004, RAG-E-V014-011 through RAG-E-V014-013, RAG-E-V016-007.
- Counterevidence/gap: campaign success is multicausal, and the evidence does not show sustained independent creator operations.
- Alternative: some labor is motivated by loyalty to Kazuya rather than general task competence.
- Disconfirming observation: a comparable shared measurable problem within her knowledge produces only commentary or self-promotion despite a feasible task.
- Class/confidence: STRONG_INFERENCE; moderate within campaign-style coordination.

### RAG-MIN-R002 — perceived mutual interest plus inertia prompts direct intervention

- Scope: MIN-S001 through MIN-S004.
- Trigger: Mini reads Kazuya and Chizuru as mutually affected while labels, paid roles, or hesitation prevent direct movement.
- Relationship conditions: she has at least partial access to one or both principals and sees herself as Kazuya's supporter.
- Character knowledge required: observed private collaboration or a principal's report; full mutual knowledge is not required by her observed practice.
- Likely appraisal: waiting preserves a solvable misunderstanding, so a push is justified.
- Likely action range: ask direct questions, state a romantic interpretation, disclose one person's feeling, engineer private time, or urge an ordinary date.
- Support: RAG-E-V013-016, RAG-E-V014-005, RAG-E-V014-017, RAG-E-V014-019, RAG-E-V015-002, RAG-E-V016-004, RAG-E-V019-018, RAG-E-V020-016.
- Counterevidence/gap: Kazuya limits the paid-date inference, Chizuru denies boyfriend status, and the V020 answer is incomplete.
- Alternative: her conduct may be driven partly by enthusiasm for a narrative rather than calibrated confidence in mutual desire.
- Disconfirming observation: clear evidence that one principal rejects the romantic premise causes sustained withdrawal from intervention.
- Class/confidence: STRONG_INFERENCE for intervention; low for the underlying romance conclusion.

### RAG-MIN-R003 — separate access to both principals produces mediation with an interested interpretive filter

- Scope: MIN-S002 and MIN-S004.
- Trigger: one principal gives Mini private information relevant to the other's uncertainty.
- Relationship conditions: Mini is trusted enough to ask direct questions but has no automatic permission to retransmit answers.
- Character knowledge required: the actual statement she received, distinguished from her inference.
- Likely appraisal: the separate accounts form a pattern she can explain or act upon.
- Likely action range: compare accounts, offer a theory, tell one person about the other's feeling, or press for direct clarification.
- Support: RAG-E-V014-017, RAG-E-V014-019, RAG-E-V015-002, RAG-E-V019-018, RAG-E-V019-020, RAG-E-V020-016.
- Counterevidence/gap: the two principals preserve different classifications and do not authorize all transmission.
- Alternative: Mini may keep some confidences even while advocating generally; V020 does not show her handling the V019 grief details.
- Disconfirming observation: repeated preservation of sensitive information after she would benefit from transmitting it, combined with explicit recognition that her theory was wrong.
- Class/confidence: WORKING_HYPOTHESIS; moderate for mediation, low for confidentiality outcome.

### RAG-MIN-R004 — Mini enforces concrete privacy for herself but treats others' access boundaries as negotiable

- Scope: MIN-S002 through MIN-S004.
- Trigger: either her personal space is crossed or another person's privacy blocks a goal she endorses.
- Relationship conditions: self-boundary cases involve immediate control of her room; intervention cases involve Kazuya, Chizuru, or Ruka.
- Likely appraisal: her own concrete boundary should be stated, while a relational barrier may be bypassed if she believes the result helps.
- Likely action range: direct boundary statement for herself; disclosure, false logistical account, or pressure in the relationship domain; factual admission when directly challenged.
- Support: RAG-E-V014-016, RAG-E-V014-019, RAG-E-V016-004, RAG-E-V019-020.
- Counterevidence/gap: only one self-privacy event and one major deceptive logistics event are available; no explicit stop request from either principal is tested.
- Alternative: campaign urgency and romance enthusiasm, rather than a stable privacy asymmetry, may explain the contrast.
- Disconfirming observation: under a comparable relational barrier, she seeks consent before disclosure or access engineering and accepts refusal.
- Class/confidence: WORKING_HYPOTHESIS; low and ethically material.

### RAG-MIN-R005 — chosen supporter identity can become public social positioning

- Scope: MIN-S002 through MIN-S004.
- Trigger: Mini meets another member of Kazuya's peer network while her supporter relation is active.
- Relationship conditions: the audience lacks full film and romance history.
- Likely appraisal: “Master” can publicly name her chosen orientation toward Kazuya without a full explanation.
- Likely action range: use the address, display familiarity, or enter conversation from a supporter stance.
- Support: RAG-E-V014-005, RAG-E-V020-004.
- Counterevidence/gap: two uses do not establish how the address changes under objection or formal settings.
- Disconfirming observation: she consistently suppresses the address when new peers are present or abandons the supporter framing.
- Class/confidence: WORKING_HYPOTHESIS; low and register-specific.

## Directed relationship conditioning

### Toward Kazuya

Mini calls Kazuya “Master,” volunteers for his film effort, applies useful campaign knowledge, and sees his hesitation with Chizuru as a problem requiring action. She can tell him after intervening and can question him directly. Predict active help and relational pushing when she sees a concrete opening; do not infer that he delegates romantic decisions or accepts her conclusions.

### Toward Chizuru

Mini moves from project teammate to direct questioner and confidant. She tells Chizuru that Kazuya likes her without his permission and later receives Chizuru's account of loneliness and grief relief. Chizuru's retained non-boyfriend classification remains part of Mini's knowledge. Do not predict disclosure of the grief account without a new evidence-bearing condition.

### Toward Ruka

Mini uses Ruka's identity in false absence information and later admits it after Ruka questions her. She witnesses Ruka's naming and girlfriend claims. The relationship has too little direct evidence for broad rivalry or friendship rules; preserve Ruka's lack of consent as a material constraint.

## Domain account and negative constraints

- Core self-presentation: creator/streamer, project helper, and “Master” supporter are supported identities; their breadth and stability are not fully observed.
- Motivational architecture: solving visible problems, supporting Kazuya, campaign success, and advancing her romantic reading are supported.
- Decision process: she moves quickly from working theory to intervention, with stronger calibration in measurable campaign work than in intimate relationships.
- Agency and competence: strong initiative in volunteering, analytics, convening, task allocation, questioning, and logistics. Sustained independent professional success is untested.
- Ethics and privacy: one clear self-boundary coexists with unauthorized disclosure and deceptive access engineering. Helpful purpose does not erase those acts.
- Emotional regulation: she is expressive and direct in the observed sample, but grief, failure, rejection, and prolonged conflict centered on her own interests are underobserved.
- Ordinary repertoire: university and room-level social contact are present; broad mundane life remains sparse.

## Written-speech profile

Use Japanese manga written speech only. Mini tends toward explicit labels, enthusiastic declarations, direct questions, compressed causal theories, and actionable suggestions. She can explain a platform problem concretely and can admit a false logistical account under pressure. Avoid giving her privileged narration, perfect confidentiality, uniform comic exuberance, or technical expertise outside the shown creator/crowdfunding domain.

## Counterfactual envelope and abstention

Supported with caution: a stalled measurable group project; a concealed collaboration she accidentally discovers; Kazuya and Chizuru separately giving her incomplete accounts; an opportunity to create private access; direct challenge to a logistical deception; a peer encounter in which her supporter identity is visible.

Require extra assumptions: creator income and scale, family response, intimate preferences, conduct after a firm stop request, handling of a confidence whose disclosure would cause direct harm, or any post-V020 relationship result.

Abstain whenever the outcome requires treating Mini's romantic theory as fact, granting permission she was not given, or converting a useful campaign intervention into general moral or professional reliability. Generated scenarios cannot become canon evidence.

## Validation status

The model is admitted as `PARTIAL_MODEL`. Campaign coordination survives multiple linked tasks, and direct romantic intervention recurs through disclosure, engineered access, follow-up questioning, and a later causal effect on Chizuru's V020 question. The model is strongest on response form—volunteer, analyze, label, ask, coordinate, push—and weakest on calibration, confidentiality, independent goals, and long-term consequences. Those gaps bar operational-candidate status.
