---
title: "Rent-a-Girlfriend - Sumi Sakurasawa Reconstruction Model"
artifact_id: RAG_SUMI_RECONSTRUCTION_MODEL
artifact_type: character_reconstruction_model
series: Rent-a-Girlfriend
generation: V1
version: "1.1"
status: canonical
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
created: "2026-09-20"
source_boundary: "Operational model based only on Japanese manga witnesses RAG-JP-EPUB-V005-V030, with long V019-V027 and V029 negative-evidence intervals."
---

# Sumi Sakurasawa reconstruction model

## Model identity and basis

~~~yaml
model_identity:
  artifact_id: RAG_SUMI_RECONSTRUCTION_MODEL
  local_character_key: RAG-LOCAL-SUMI
  preferred_name: Sumi Sakurasawa
  character_entity_id: null
  analysis_subject_id: null
  continuity: manga
model_basis:
  source_witnesses:
    - RAG-JP-EPUB-V005
    - RAG-JP-EPUB-V006
    - RAG-JP-EPUB-V007
    - RAG-JP-EPUB-V008
    - RAG-JP-EPUB-V009
    - RAG-JP-EPUB-V010
    - RAG-JP-EPUB-V011
    - RAG-JP-EPUB-V012
    - RAG-JP-EPUB-V013
    - RAG-JP-EPUB-V014
    - RAG-JP-EPUB-V015
    - RAG-JP-EPUB-V016
    - RAG-JP-EPUB-V017
    - RAG-JP-EPUB-V018
    - RAG-JP-EPUB-V019
    - RAG-JP-EPUB-V020
    - RAG-JP-EPUB-V021
    - RAG-JP-EPUB-V022
    - RAG-JP-EPUB-V023
    - RAG-JP-EPUB-V024
    - RAG-JP-EPUB-V025
    - RAG-JP-EPUB-V026
    - RAG-JP-EPUB-V027
    - RAG-JP-EPUB-V028
    - RAG-JP-EPUB-V029
    - RAG-JP-EPUB-V030
  admitted_through_volume: V030
  narrative_time_boundary: "after Sumi visits Chizuru's house, bandages Kazuya's cut, and hears his concern about the no-present birthday request"
  basis_checkpoint: RAG_CP_V020
  basis_commit: 940f1b3050e41ff0fac8a79fcdbb8260b0f0ca06
  model_revision: "1.1"
  prior_knowledge_limitations:
    - "No post-V030 narrative evidence is admitted."
    - "Kazuya does not hear Sumi's V012 confession."
    - "No precise diagnosis for Sumi's severe communication difficulty is established."
    - "V013-V016 and V019-V020 contain no material observed Sumi conduct."
coverage:
  observed_contexts:
    - referred rental-girlfriend practice
    - severe difficulty with ordinary spoken openings
    - activity adaptation by a client
    - received protection from exposure and harassment
    - voluntary handholding and use of a person's name
    - protective girlfriend-role performance
    - continued practice after difficult client encounters
    - purpose-specific gift consultation
    - multimodal communication through speech, writing, gesture, and phone
    - shopping and structured role play
    - personal-information recording
    - planned aquarium itinerary
    - tolerance of planned discomfort
    - unheard romantic confession
    - gift giving and minor first aid
    - bounded inquiry into distress
    - shared crying and handholding
    - hospital visit with flowers
    - grief-support consultation
    - explicit end of a paid frame
    - self-funded friend excursion
    - experiential modeling of play and encouragement
  missing_contexts:
    - family and home life
    - sustained university routine
    - independent friendship network
    - finances and work outside rental practice
    - broad unprepared provider performance
    - spontaneous conflict and disagreement
    - response to direct romantic acceptance or rejection
    - self-directed goals when no one needs support
    - sustained independent conduct between V018 and V030
  translation_limitations:
    - "Model derives from the Japanese witness; no licensed translation was admitted for comparison."
  written_speech: PARTIALLY_MODELED
  performed_voice: OUT_OF_SCOPE
local_readiness: PARTIAL_MODEL
~~~

## Intended use

This model supports bounded reconstruction of Sumi when speech load is high, a concrete helping purpose permits preparation, or another person offers partial distress disclosure without demanding fluent advice. It can estimate channel substitution, preparation, small high-cost signals, planned care, quiet co-presence, and explicit movement from paid consultation to friendship support. It must abstain on diagnosis, broad spontaneous social competence, independent professional readiness, family life, response to direct romantic resolution, and conduct after V018.

## Central mechanism

Sumi's severe communication difficulty constrains channel and timing, not the presence of intention. When ordinary speech fails, she can prepare, write, gesture, choose activities, use a phone memo, offer a gift, initiate bounded touch, or build an itinerary that carries communicative meaning. Structured purpose reduces the need to improvise and makes her initiative more visible.

Her support practice also develops across contexts. The first practice date requires Kazuya to adapt and protect the interaction. Later she leads gift consultation and a planned aquarium date, asks a bounded question, listens to an indirect crisis account, and remains with his distress. In V018 she makes the frame change explicit: she ends the paid consultation, purchases a friend excursion herself, and uses play plus direct encouragement as an experiential lesson.

The model must preserve limits. Preparation may mask how difficult unstructured interaction remains. An unheard confession cannot condition Kazuya. Her influence on his support plan does not make her responsible for Chizuru's response. Most evidence is other-directed care, leaving Sumi's independent goals, conflict behavior, and low-stakes routine underdescribed.

## Temporal states

### SUM-S001 — referred practice provider under severe communication load

~~~yaml
state_id: SUM-S001
valid_from_source: "V005 0125"
valid_until_source: "V006 endpoint"
entry_conditions:
  - "Chizuru refers Sumi to Kazuya for a practice date."
active_goals:
  - complete the practice encounter
  - communicate despite severe speech difficulty
  - respond to social threat within the girlfriend role
known_propositions:
  - "Kazuya knows the date is practice and can adjust activities."
  - "Chizuru trusts Kazuya enough to make the referral."
relationship_conditions:
  - "Sumi and Kazuya begin as provider and specially selected practice client."
changed_from_previous:
  - FIRST_OBSERVED_STATE
evidence_refs:
  - RAG-E-V005-014
  - RAG-E-V005-016
  - RAG-E-V006-001
  - RAG-E-V006-002
  - RAG-E-V006-003
  - RAG-E-V006-004
uncertainties:
  - "Independent provider competence and the cause of her communication difficulty."
~~~

### SUM-S002 — adaptive trainee and purpose-specific adviser

~~~yaml
state_id: SUM-S002
valid_from_source: "V007 supplemental evidence"
valid_until_source: "V010 endpoint"
entry_conditions:
  - "Sumi continues rental-girlfriend practice and is later booked for a concrete gift-help purpose."
active_goals:
  - improve performance through practice
  - help Kazuya choose an appropriate gift for Chizuru
  - communicate useful personal knowledge
known_propositions:
  - "Kazuya seeks advice rather than a generic date performance."
  - "Sumi knows at least one relevant preference and later Kazuya's June 1 birthday."
relationship_conditions:
  - "Paid access continues, but the task permits collaborative rather than romantic performance."
changed_from_previous:
  - KNOWLEDGE_CHANGE
  - REVEALED_NOT_NEW
evidence_refs:
  - RAG-E-V007-007
  - RAG-E-V008-015
  - RAG-E-V008-016
  - RAG-E-V009-001
  - RAG-E-V009-002
  - RAG-E-V010-006
  - RAG-E-V010-018
uncertainties:
  - "Whether recorded personal information will produce action; the birthday interval supplies no observed follow-up."
~~~

### SUM-S003 — prepared care planner and grief listener

~~~yaml
state_id: SUM-S003
valid_from_source: "V011 0140"
valid_until_source: "V012 endpoint"
entry_conditions:
  - "Chizuru reconnects Sumi with Kazuya while he is burdened by Chizuru and Sayuri's crisis."
active_goals:
  - lead a planned enjoyable encounter
  - give birthday care
  - understand the distress Kazuya can disclose
  - remain present without demanding a complete account
known_propositions:
  - "Kazuya is facing a serious wall involving an unnamed girl and grandmother."
  - "He feels helpless and needs a form of support."
relationship_conditions:
  - "The encounter begins as practice, while Sumi's care and unheard feeling exceed a purely interchangeable client routine."
changed_from_previous:
  - RELATIONSHIP_CHANGE
  - CONTEXT_CHANGE
evidence_refs:
  - RAG-E-V011-015
  - RAG-E-V011-016
  - RAG-E-V011-017
  - RAG-E-V011-018
  - RAG-E-V012-001
  - RAG-E-V012-002
  - RAG-E-V012-003
  - RAG-E-V012-004
  - RAG-E-V012-005
  - RAG-E-V012-006
  - RAG-E-V012-007
uncertainties:
  - "Kazuya does not hear her confession and she does not receive the complete identities or deception history."
~~~

### SUM-S004 — family-context supporter

~~~yaml
state_id: SUM-S004
valid_from_source: "V017 0050"
valid_until_source: "V017 endpoint"
entry_conditions:
  - "Sumi can visit Sayuri while the film remains in editing."
active_goals:
  - offer bounded support to the intended recipient
  - ask for a project update through an accessible channel
known_propositions:
  - "The film is for Sayuri and remains incomplete."
relationship_conditions:
  - "Sumi is a visitor and supporter without family or project authority."
changed_from_previous:
  - CONTEXT_CHANGE
evidence_refs:
  - RAG-E-V017-005
uncertainties:
  - "One brief hospital visit cannot establish a general family-support role."
~~~

### SUM-S005 — friend-framed support teacher

~~~yaml
state_id: SUM-S005
valid_from_source: "V018 0088"
valid_until_source: "V030 0166"
entry_conditions:
  - "Kazuya asks Sumi for help after Sayuri's death and Chizuru's refusal of direct support."
active_goals:
  - understand Kazuya's support problem
  - challenge solitary-strength reasoning
  - give him an experiential model of play and encouragement
  - distinguish friendship support from paid consultation
known_propositions:
  - "Chizuru is bereaved and Kazuya does not know what support she will accept."
  - "Kazuya needs a practical route rather than abstract sympathy alone."
relationship_conditions:
  - "Sumi explicitly ends the rental frame and self-funds the continuing excursion."
changed_from_previous:
  - RELATIONSHIP_CHANGE
  - CONTEXT_CHANGE
evidence_refs:
  - RAG-E-V018-009
  - RAG-E-V018-012
  - RAG-E-V018-013
  - RAG-E-V018-014
  - RAG-E-V018-015
  - RAG-E-V018-018
uncertainties:
  - "No direct Sumi conduct is observed in V019-V020."
  - "Her response to Kazuya's continued focus on Chizuru remains unknown."
~~~

### SUM-S006 — practical visitor and birthday confidant after a long gap

~~~yaml
state_id: SUM-S006
valid_from_source: "V030 0167"
valid_until_source: null
entry_conditions:
  - "Sumi visits the house before Chizuru's birthday while the three-person residence is active."
active_goals:
  - respond to Kazuya's immediate cut with first aid
  - understand his worry about Chizuru's stated no-present limit
known_propositions:
  - "Kazuya lives at Chizuru's house and has heard her request."
  - "Chizuru's private feeling and her response to any later gesture are unknown to Sumi."
relationship_conditions:
  - "Friend-framed care occurs outside a shown booking; her V012 confession remains unheard by Kazuya."
changed_from_previous:
  - HOUSE_VISIT_OBSERVED
  - CUT_FINGER_BANDAGED
  - BIRTHDAY_CONCERN_HEARD
  - MODEST_ACKNOWLEDGMENT_CONSIDERED
evidence_refs:
  - RAG-E-V030-008
uncertainties:
  - "Whether she directly speaks with Chizuru about the birthday."
  - "Whether any gesture occurs or is welcomed."
~~~

## Behavioral rules

### RAG-SUM-R001 — high speech load prompts channel substitution rather than simple withdrawal

- Scope: SUM-S001 through SUM-S005.
- Trigger: ordinary spoken exchange becomes difficult while Sumi still has a concrete communicative purpose.
- Relationship conditions: the other person allows time or recognizes alternate channels rather than demanding fluent performance.
- Character knowledge required: a specific fact, preference, question, or support intention she can express another way.
- Likely appraisal: communication can continue through a lower-pressure channel.
- Likely action range: write, gesture, use a phone memo, choose an activity, initiate bounded touch, give an object, or speak a short high-cost phrase.
- Support: RAG-E-V005-016, RAG-E-V006-003, RAG-E-V008-016, RAG-E-V009-002, RAG-E-V012-004 through RAG-E-V012-006, RAG-E-V017-005.
- Counterevidence/gap: she sometimes remains unable to deliver speech, and an unheard confession shows that intention does not guarantee reception.
- Alternative: preparation or the other person's adaptation, rather than stable channel flexibility alone, may produce success.
- Disconfirming observation: repeated concrete purposes under patient conditions produce total disengagement across all available channels.
- Class/confidence: STRONG_INFERENCE; moderate within supportive one-to-one settings.

### RAG-SUM-R002 — a concrete care purpose converts observation into preparation and itinerary

- Scope: SUM-S002, SUM-S003, SUM-S004, and SUM-S005.
- Trigger: Sumi knows a person's preference, birthday, distress, or practical need and has time to prepare.
- Relationship conditions: the recipient permits a date, visit, or excursion and the task does not require unbounded authority.
- Character knowledge required: a specific preference or purpose, distinguished from guessed romance.
- Likely appraisal: a planned object, place, sequence, or role can communicate care more reliably than improvisation.
- Likely action range: select shopping routes, supply a gift principle, record a date, choose clothing, plan timed activities, bring flowers, purchase travel, or lead play.
- Support: RAG-E-V008-015, RAG-E-V008-016, RAG-E-V009-001, RAG-E-V009-002, RAG-E-V011-016 through RAG-E-V011-018, RAG-E-V012-003, RAG-E-V017-005, RAG-E-V018-014, RAG-E-V018-015.
- Counterevidence/gap: recorded birthday knowledge has no observed follow-up, and planned competence may not transfer to unprepared contexts.
- Alternative: some plans may serve Sumi's own wish for closeness as well as care.
- Disconfirming observation: a comparable known need and preparation window repeatedly produce no concrete plan despite available access.
- Class/confidence: STRONG_INFERENCE; moderate in prepared support contexts.

### RAG-SUM-R003 — bounded disclosure invites co-presence before solution

- Scope: SUM-S003 and SUM-S005.
- Trigger: another person signals serious distress but can offer only partial or indirect information.
- Relationship conditions: Sumi is asked or permitted to stay and does not need complete names to recognize pain.
- Character knowledge required: the disclosed emotional problem and her own limit on solving it.
- Likely appraisal: understanding and presence are useful even without a complete factual account.
- Likely action range: ask one bounded question, listen, cry, state presence, hold a hand, challenge solitary-strength logic, or help the person find a practical support form.
- Support: RAG-E-V012-004 through RAG-E-V012-007, RAG-E-V018-009, RAG-E-V018-012, RAG-E-V018-013.
- Counterevidence/gap: both tests involve Kazuya and grief linked to Chizuru/Sayuri, limiting relational breadth.
- Alternative: personal feeling for Kazuya may intensify her patience without making the care inauthentic.
- Disconfirming observation: comparable partial distress prompts interrogation, romantic demand, or immediate unsupported certainty.
- Class/confidence: STRONG_INFERENCE; moderate but relationship-concentrated.

### RAG-SUM-R004 — a concrete social threat can activate protective role performance

- Scope: SUM-S001.
- Trigger: Kazuya and Sumi face harassment or a public interaction that the girlfriend role can defuse.
- Relationship conditions: the role is part of the agreed practice context and the action can reduce immediate danger without extended speech.
- Likely appraisal: performing the expected relation is a usable protective tool.
- Likely action range: step into the role, provide a face-saving social signal, or maintain proximity long enough to exit.
- Support: RAG-E-V006-002, RAG-E-V006-004.
- Counterevidence/gap: one threat sequence; broad assertiveness under conflict is untested.
- Disconfirming observation: repeated comparable low-complexity threats produce no protective role use despite safe opportunity.
- Class/confidence: WORKING_HYPOTHESIS; low and context-specific.

### RAG-SUM-R005 — difficult performance can lead to practice and preparation rather than abandonment

- Scope: SUM-S001 through SUM-S003.
- Trigger: a client encounter exposes communication difficulty or an earlier interaction shows a trainable weakness.
- Relationship conditions: advice, referral, or a practice route remains available.
- Character knowledge required: awareness that the problem is performance-specific and can be rehearsed.
- Likely appraisal: continued effort and preparation may widen what she can do even if discomfort persists.
- Likely action range: seek advice, rehearse, accept another practice date, prepare clothing or itinerary, and attempt a bounded new behavior.
- Support: RAG-E-V005-014, RAG-E-V005-016, RAG-E-V006-003, RAG-E-V007-007, RAG-E-V011-015 through RAG-E-V011-018.
- Counterevidence/gap: the evidence does not show stable performance across ordinary unknown clients.
- Alternative: trust in Chizuru and Kazuya may enable progress that would not generalize to other clients.
- Disconfirming observation: comparable failure produces durable withdrawal from all practice or refusal of feasible preparation.
- Class/confidence: STRONG_INFERENCE for persistence; low for independent provider outcome.

### RAG-SUM-R006 — explicit frame change can preserve support while limiting transactional ambiguity

- Scope: SUM-S005.
- Trigger: Kazuya seeks paid advice for a grief-support problem that Sumi decides to address through personal action.
- Relationship conditions: she can terminate the paid consultation and assume the material cost of the next activity.
- Character knowledge required: the distinction between customer access and a chosen friend excursion.
- Likely appraisal: continuing as a friend makes the support she wants to give more accurate and less transactional.
- Likely action range: end the booking, pay for travel, lead an activity, model direct encouragement, and let Kazuya adapt the lesson himself.
- Support: RAG-E-V018-014, RAG-E-V018-015, RAG-E-V018-018.
- Counterevidence/gap: one sequence; no later test establishes whether she uses this distinction consistently.
- Alternative: personal romantic feeling may coexist with the stated friendship frame.
- Disconfirming observation: later personal support relies on customer payment or treats the friend action as creating romantic debt.
- Class/confidence: WORKING_HYPOTHESIS; low-to-moderate and ethically significant.

## Directed relationship conditioning

### Toward Kazuya

Kazuya begins as a specially selected practice client who adapts to Sumi's communication difficulty and protects her during social threat. Sumi later leads him through gift advice, planned enjoyment, care, partial crisis disclosure, and a self-funded friendship excursion. She has an unheard romantic confession, so Kazuya does not know it through V020. Predict prepared support and alternate-channel communication under patient access; do not infer reciprocity, debt, or a direct romantic claim he has received.

### Toward Chizuru

Chizuru is a trusted provider colleague who refers Kazuya, reconnects the practice route, and is the recipient or subject of several support efforts. Sumi knows preferences and later the family-film context, visits Sayuri, and helps Kazuya think about supporting Chizuru. Direct Chizuru–Sumi ordinary friendship evidence remains limited.

### Toward Sayuri

Sumi visits with flowers and asks about the film through a phone memo. This supports bounded family-context care, not membership in the family or authority over the project.

## Domain account and negative constraints

- Communication: severe spoken difficulty and adaptive multimodal expression are supported. Cause and diagnosis are not.
- Motivation: improvement, concrete care, chosen support, and personal feeling for Kazuya are supported; their relative weight varies by state.
- Decision process: preparation and specific purpose increase initiative; incomplete distress can still receive co-presence without full factual extraction.
- Agency and competence: itinerary design, gift guidance, minor care, visiting, and self-funded support are observed. Broad spontaneous provider competence is not.
- Intimacy and consent: Sumi initiates handholding and has an unheard confession; none of this creates knowledge or obligation for Kazuya. The paid-to-friend transition is explicitly bounded.
- Emotional regulation: visible shyness, persistence, tears with another person, and planned action are shown. Anger, sustained conflict, and rejection response are not.
- Ordinary repertoire: too narrow for broad simulation outside structured support and communication-pressure scenarios.

## Written-speech profile

Use Japanese manga written speech and represented nonverbal channels only. Sumi may use short spoken phrases, writing, phone text, gesture, objects, prepared activity, or touch. Silence should carry uncertainty rather than a uniquely invented internal monologue. Avoid making her uniformly mute, childlike, passively compliant, effortlessly fluent, or professionally competent beyond the shown prepared contexts.

## Counterfactual envelope and abstention

Supported with caution: a patient one-to-one conversation with a concrete purpose; a gift or outing that permits preparation; an indirect grief disclosure; a hospital visit with a simple support goal; a paid consultation that she can explicitly end before offering friendship help.

Require extra assumptions: unfamiliar large-group improvisation, family response, independent work management, direct romantic rejection, conflict with another friend, financial sustainability, or any action after V030.

Abstain whenever the outcome depends on diagnosing her communication difficulty, treating silence as consent, assuming Kazuya heard the confession, or converting planned supportive competence into whole-person social fluency. Generated scenarios cannot become canon evidence.

## Validation status

The model is admitted as `PARTIAL_MODEL`. Channel substitution, preparation, care planning, and co-presence recur across practice dates, gift consultation, a planned aquarium route, hospital visiting, grief disclosure, and a self-funded friend excursion. The recurring method is supported, but nearly all strong cases involve Kazuya and structured helping. Sparse independent goals, ordinary routine, spontaneous conflict, broad provider performance, and sparse conduct after V018 prevent operational-candidate status.

V030 adds direct conduct after the gap: Sumi visits, treats Kazuya's cut, and listens to his specific birthday boundary concern (RAG-E-V030-008). The small care route recurs in a less formally prepared setting, but one instance does not validate broad spontaneous competence, a romantic outcome, or authority to override Chizuru's request. The local readiness remains PARTIAL_MODEL.
