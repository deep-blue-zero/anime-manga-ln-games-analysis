---
title: "Rent-a-Girlfriend - Ruka Sarashina Reconstruction Model"
artifact_id: RAG_RUKA_RECONSTRUCTION_MODEL
artifact_type: character_reconstruction_model
series: Rent-a-Girlfriend
generation: V1
version: "1.15"
status: canonical
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
created: "2026-09-19"
source_boundary: "Operational model based on Japanese manga witnesses RAG-JP-EPUB-V003-V016, with V012-V013 negative-evidence review."
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
  admitted_through_volume: V016
  narrative_time_boundary: "after Mini uses Ruka's name without consent, Ruka confronts the final-location trip, and her birthday request for bodily touch remains unanswered"
  basis_checkpoint: RAG_CP_V010
  basis_commit: 18fe1738f18a66a91e6a3a340f845f3d7c3d4efe
  model_revision: "1.14"
  prior_knowledge_limitations:
    - "No post-V016 narrative evidence is admitted."
    - "The manga establishes low pulse, symptoms, medication, and monitoring but no precise medical diagnosis."
    - "Kazuya refuses sex during the V008 overnight; Ruka's contrary V009 sexual claim is immediately denied."
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
    - immediate refusal and self-inhibition
    - family recognition contest
    - disclosure reconsideration under concrete human cost
    - coworker access
    - fabricated rival evidence
    - ordinary date effort and interrupted status conversion
    - workplace monitoring under incomplete information
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

This model supports tightly bounded reconstruction of Ruka at the V014 endpoint when bodily self-monitoring, romantic certainty, rivalry, provisional dating, family crisis, status challenge, and shared project work are salient. It can model her direct speech, high initiative, ordinary-date effort, local apology, sexual pressure, unilateral intimacy, crisis-triggered tactical delay, categorical overstatement, and burden-triggered support. It must abstain on a precise diagnosis, family life, later development, durable rejection, knowledge she does not receive, and any assumption that her pulse, provisional label, gift, or physical initiative proves mutual love or consent.

## Central mechanism

Ruka converts a long-standing feeling of physiological and social difference into a measurable test of emotional reality. A low pulse and muted excitement make her fear that she is like a robot. Rental work becomes an experiment: if another person can make her heart race, that response will prove she can feel love like other people.

Kazuya's defense of Chizuru produces the first reading above ninety. Ruka therefore treats him as a unique answer rather than one promising person among alternatives. That certainty compresses deliberation. She investigates, declares love, bargains with the secret, accepts a nonreciprocal trial, and repeatedly creates access. High initiative and genuine vulnerability coexist with coercive pressure.

The model must preserve counterevidence. Ruka does not immediately expose Chizuru, later says she never intended to, understands that the relationship is provisional, and accepts that Kazuya is attached elsewhere. In V005 she stops after Kazuya retreats, abandons a prepared disclosure when Nagomi's attachment becomes concrete, joins Kazuya's workplace, and plants underwear to mislead Chizuru. V008 shows sincere ordinary-date effort and cooking alongside intrusion, sexual pressure, and a unilateral kiss after refusal. V009 shows sincere tears and love language alongside a false claim of completed sexual intimacy. V010 shows an apology followed by family pursuit and another unilateral kiss. V011 weakens a broad refusal-sensitive model because she continues kissing through objection, while the later temporary truce shows that third-party crisis can redirect timing. V014 adds costly cooperation on Chizuru's film when Kazuya's burden is visible. She is neither a purely calculating blackmailer nor a purely innocent romantic claimant.

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
valid_until_source: "V005 0004"
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

### RUK-S005 — strategic rival under family and workplace expansion

~~~yaml
state_id: RUK-S005
valid_from_source: "V005 0005"
valid_until_source: "V006 0090"
entry_conditions:
  - "Ruka uses the private karaoke room to press for sexual and family recognition beyond weekly dating."
active_goals:
  - obtain Kazuya's freely enacted girlfriend recognition
  - replace Chizuru in Nagomi's family understanding without destroying Nagomi's attachment
  - increase routine access through the karaoke workplace
  - make her closeness to Kazuya visible to Chizuru
known_propositions:
  - "Kazuya retreats from immediate sexual escalation and still prioritizes Chizuru."
  - "Nagomi wants to love Chizuru like a daughter."
  - "Public declaration alone is recast as lying under the family fiction."
relationship_conditions:
  - "Ruka remains a provisional girlfriend without family recognition or reciprocal love."
  - "Chizuru is both rival and beneficiary of a family bond Ruka chooses not to destroy."
  - "The workplace supplies recurring contact but also secrecy risks around Kuribayashi."
changed_from_previous:
  - CONSENT_RESPONSE_EVIDENCE
  - FAMILY_STRATEGY_CHANGE
  - WORKPLACE_ACCESS_CHANGE
  - RIVAL_SIGNALING_CHANGE
evidence_refs:
  - RAG-E-V005-001
  - RAG-E-V005-002
  - RAG-E-V005-003
  - RAG-E-V005-004
  - RAG-E-V005-006
  - RAG-E-V005-007
  - RAG-E-V005-013
uncertainties:
  - "Whether immediate self-inhibition persists under repeated refusal."
  - "Whether workplace access produces competent routine or escalating collision."
~~~

### RUK-S006 — provisional girlfriend receiving an interrupted conversion attempt at work

~~~yaml
state_id: RUK-S006
valid_from_source: "V006 0091"
valid_until_source: "V008 0004"
entry_conditions:
  - "An ordinary date leads Kazuya to begin proposing that the provisional relationship become official."
active_goals:
  - obtain freely enacted official recognition from Kazuya
  - use workplace access to understand unexplained contact involving Chizuru
  - preserve her position against Chizuru without yet exposing the central secret
known_propositions:
  - "Kazuya begins but does not complete a status-change proposal."
  - "Kazuya leaves the karaoke room after Chizuru and an unidentified client."
  - "The manager can interrupt her pursuit and restore workplace duty."
relationship_conditions:
  - "Ruka remains a provisional girlfriend without completed official status or reciprocal love."
  - "She lacks the content of Mami's booking and Kazuya's later direct preference statement to Chizuru."
changed_from_previous:
  - STATUS_PROPOSAL_CHANGE
  - WORKPLACE_INFORMATION_GAP_CHANGE
  - MONITORING_CONTEXT_CHANGE
evidence_refs:
  - RAG-E-V006-009
  - RAG-E-V006-010
uncertainties:
  - "Whether Kazuya revisits the proposal after the interruption."
  - "How Ruka responds if she learns the booking's content or Kazuya's direct preference."
~~~

### RUK-S007 — domestic and overnight escalator under explicit nonreciprocity

~~~yaml
state_id: RUK-S007
valid_from_source: "V008 0005"
valid_until_source: "V009 0004"
entry_conditions:
  - "Ruka discovers Chizuru's temporary private access and judges that roughly two months of provisional dating have not produced recognition."
active_goals:
  - make Kazuya experience her as an ordinary girlfriend
  - convert private and domestic access into reciprocal intimacy
  - preserve advantage over Chizuru while avoiding immediate exposure of the central secret
known_propositions:
  - "Chizuru can enter Kazuya's apartment under practical need."
  - "Kazuya accepts shopping, cooking, and storm lodging but refuses sex."
  - "The provisional label has not produced reciprocal love or spontaneous physical initiative."
relationship_conditions:
  - "Ruka and Kazuya remain provisional and nonreciprocal after the overnight."
  - "Chizuru does not know about the overnight stay or morning kiss."
changed_from_previous:
  - RIVAL_PRIVATE_ACCESS_DISCOVERY
  - UNIVERSITY_INTRUSION
  - ORDINARY_DATE_AND_DOMESTIC_EFFORT
  - STORM_OVERNIGHT
  - SEXUAL_REFUSAL_RECEIVED
  - UNILATERAL_KISS
evidence_refs:
  - RAG-E-V008-003
  - RAG-E-V008-009
  - RAG-E-V008-010
  - RAG-E-V008-011
  - RAG-E-V008-012
  - RAG-E-V008-013
  - RAG-E-V008-014
uncertainties:
  - "What secrecy or status consequence follows the overnight and kiss."
  - "Whether repeated explicit nonreciprocity changes her larger pursuit."
  - "How she responds if Chizuru learns the event."
~~~

### RUK-S008 — public status claimant under former-partner challenge

~~~yaml
state_id: RUK-S008
valid_from_source: "V009 0005"
valid_until_source: "V010 0004"
entry_conditions:
  - "The overnight becomes a written reassurance issue between Kazuya and Chizuru before Mami visits the karaoke workplace."
active_goals:
  - establish present priority over Mami and Chizuru
  - have the provisional relation recognized as an ordinary current relationship
  - defend the sincerity and exclusivity of her love claim
known_propositions:
  - "Mami is Kazuya's former girlfriend and her rejection contributed to his rental-girlfriend use."
  - "Kazuya corrects the relation as provisional and denies that sex occurred."
  - "Mami knows about rental girlfriends and doubts the coherence of Ruka's account."
relationship_conditions:
  - "Ruka's public status claim exceeds the mutually agreed trial."
  - "Her stated love remains sincere within the represented self-model and unreciprocated by Kazuya."
  - "Mami leaves with unresolved suspicion rather than accepting the claim."
changed_from_previous:
  - MAMI_IDENTITY_ACQUIRED
  - CURRENT_GIRLFRIEND_PUBLIC_CLAIM
  - FALSE_SEXUAL_COMPLETION_CLAIM
  - KAZUYA_CORRECTION_RECEIVED
  - RIVAL_CHALLENGE_AND_TEARS
  - LOVE_DECLARATION_REITERATED
evidence_refs:
  - RAG-E-V009-004
  - RAG-E-V009-012
  - RAG-E-V009-013
  - RAG-E-V009-014
uncertainties:
  - "How Mami uses the contradictory account."
  - "Whether Kazuya's public correction changes Ruka's later tactics."
  - "Whether she learns that Mami has seen Chizuru working."
~~~

### RUK-S009 — locally apologetic but family-space escalator

~~~yaml
state_id: RUK-S009
valid_from_source: "V010 0005"
valid_until_source: "V011 0002"
entry_conditions:
  - "The Mami confrontation has ended with Kazuya's factual correction but without resolution of the provisional relation."
active_goals:
  - repair the immediate conflict with Kazuya
  - maintain direct girlfriend-like access
  - gain recognition inside the Kinoshita family
  - displace Chizuru's family priority through visible affection and service
known_propositions:
  - "Her conduct before Mami upset Kazuya and requires an apology."
  - "Chizuru is attending Kazuya's family birthday under the recognized girlfriend role."
  - "The family knows Ruka only through a friend classification."
  - "Kazuya recoils from her party kiss rather than reciprocating it."
relationship_conditions:
  - "Local remorse coexists with an unchanged conversion goal."
  - "Family approval is pursued as indirect leverage on status."
  - "Physical and public escalation remain unilateral."
changed_from_previous:
  - MAMI_CONFRONTATION_APOLOGY
  - BIRTHDAY_VIDEO_ACCESS
  - FAMILY_PARTY_PURSUIT
  - APPROVAL_COMPETITION
  - SECOND_UNILATERAL_KISS
  - PUBLIC_PRIORITY_CLAIM
evidence_refs:
  - RAG-E-V010-003
  - RAG-E-V010-013
  - RAG-E-V010-014
  - RAG-E-V010-015
uncertainties:
  - "Whether she revises tactics after Kazuya's recoil."
  - "Whether the Kinoshita family learns the provisional or rental truths."
  - "How she responds to Chizuru's hospital crisis and Kazuya's stage support."
~~~

### RUK-S010 — crisis-aware but consent-blind pursuer

~~~yaml
state_id: RUK-S010
valid_from_source: "V011 0003"
valid_until_source: "V014 0125"
entry_conditions:
  - "The family-party kiss has become a direct rivalry fact while Sayuri's hospitalization raises a concrete third-party cost."
active_goals:
  - make Chizuru recognize her claimed progress
  - convert the provisional relation through decisive physical and ordinary-date acts
  - avoid appearing indifferent to Sayuri's crisis
  - retain direct birthday and intimacy access during the truce
known_propositions:
  - "Kazuya recoils and tells her to stop during repeated kissing."
  - "Chizuru's grandmother has suffered a serious collapse."
  - "Kazuya remains emotionally focused on Chizuru and Sayuri."
relationship_conditions:
  - "Tactical sympathy coexists with unchanged status certainty."
  - "Repeated physical escalation now continues through explicit resistance."
  - "Gift giving and a cheek kiss preserve pursuit under a declared truce."
changed_from_previous:
  - KISS_DISCLOSED_TO_CHIZURU
  - REPEATED_KISSING_AFTER_RESISTANCE
  - NO_REGRET_POSITION
  - SAYURI_CRISIS_TRUCE
  - DELAYED_BIRTHDAY_GIFT
  - KISS_BAN_UNILATERALLY_LIFTED
evidence_refs:
  - RAG-E-V011-002
  - RAG-E-V011-004
  - RAG-E-V011-005
  - RAG-E-V011-013
  - RAG-E-V011-014
uncertainties:
  - "Whether the truce constrains later conduct."
  - "Whether she distinguishes Kazuya's guilt from consent."
  - "How she would respond to a definitive end of the trial."
~~~

### RUK-S011 — rival acting as project supporter

~~~yaml
state_id: RUK-S011
valid_from_source: "V014 0126"
valid_until_source: "V015 0046"
entry_conditions:
  - "The film campaign is stalled, Mini convenes a recovery team, and Kazuya's burden is directly visible."
active_goals:
  - help Kazuya prevent the campaign from failing
  - remain involved while Chizuru is the film's heroine
  - preserve her romantic claim despite temporary cooperative labor
known_propositions:
  - "The campaign needs roughly one million yen more and fails completely if the target is missed."
  - "Kazuya is exhausting his money and effort on promotion for Chizuru."
  - "Mini has assigned a broad publicity and reward strategy."
relationship_conditions:
  - "Rivalry with Chizuru coexists with membership in the same project team."
  - "Concern for Kazuya can produce unpriced work that materially benefits Chizuru."
  - "The provisional relationship and prior consent conflict remain unresolved."
changed_from_previous:
  - FILM_TEAM_JOINED
  - CAMPAIGN_TASK_ACCEPTED
  - PUBLIC_FLYER_LABOR_PERFORMED
  - COLLECTIVE_PROJECT_LANGUAGE_USED
evidence_refs:
  - RAG-E-V014-012
  - RAG-E-V014-013
  - RAG-E-V014-015
  - RAG-E-V014-020
uncertainties:
  - "Whether project cooperation persists when rivalry becomes immediate again."
  - "Whether helping the film changes her treatment of Kazuya's refusal or Chizuru's priority."
~~~

### RUK-S012 — rival regulating an immediate threat for project welfare

~~~yaml
state_id: RUK-S012
valid_from_source: "V015 0047"
valid_until_source: "V016 0046"
entry_conditions:
  - "Chizuru proposes using Umi's large audience on the campaign's final day, creating both a project opportunity and an immediate rivalry cue."
active_goals:
  - help the campaign reach its target for Sayuri
  - keep Kazuya focused on useful final-day work
  - preserve her romantic claim while tolerating Chizuru's contact with Umi
known_propositions:
  - "Umi's audience can materially expand campaign reach."
  - "Kazuya is reacting jealously and the final day leaves little time."
  - "Chizuru says Umi is an acting colleague, while the project still needs outreach."
relationship_conditions:
  - "Ruka remains Chizuru's rival but accepts a tactic that benefits Chizuru and requires trust in her professional contact."
  - "Ruka can correct Kazuya's rivalry response while continuing to seek him romantically."
  - "The provisional relation and prior consent failures remain unresolved."
changed_from_previous:
  - IMMEDIATE_RIVALRY_CUE_CONTAINED
  - UMI_ROUTE_ENDORSED
  - KAZUYA_JEALOUSY_CHECKED
  - SAYURI_WELFARE_INVOKED
  - FINAL_DAY_LABOR_REPEATED
evidence_refs:
  - RAG-E-V015-004
  - RAG-E-V015-017
uncertainties:
  - "Whether project-first regulation persists after the funding emergency."
  - "Whether similar restraint applies when no third-party welfare goal is available."
  - "Whether she will address status and consent directly."
~~~

### RUK-S013 — excluded project supporter renewing status and intimacy pressure

~~~yaml
state_id: RUK-S013
valid_from_source: "V016 0047"
valid_until_source: null
entry_conditions:
  - "Mini has used Ruka's name without consent to exclude her from a two-person final-location trip involving Kazuya and Chizuru."
active_goals:
  - recover accurate information and challenge access granted to Chizuru
  - preserve the provisional-girlfriend claim after project cooperation
  - obtain visible birthday recognition and physical intimacy from Kazuya
known_propositions:
  - "Mini engineered the trip and confessed after Ruka questioned her."
  - "Kazuya and Chizuru shared overnight lodging but both deny the anticipated intimacy."
  - "Ruka contributed campaign labor and missed the final-location trip."
relationship_conditions:
  - "Project-first cooperation gives way to direct rivalry after exclusion and unauthorized identity use."
  - "Ruka continues to call herself Kazuya's girlfriend despite the unresolved trial and his rejection of her trip forecast."
  - "Her birthday request for bodily touch awaits Kazuya's answer."
changed_from_previous:
  - NAME_USED_WITHOUT_CONSENT
  - MINI_QUESTIONED_AND_CONFESSION_OBTAINED
  - OVERNIGHT_TRIP_CONFRONTED
  - GIRLFRIEND_STATUS_REASSERTED
  - PROJECT_LABOR_INVOKED_AS_BIRTHDAY_CONTEXT
  - BODILY_CONTACT_REQUEST_MADE
evidence_refs:
  - RAG-E-V016-004
  - RAG-E-V016-017
  - RAG-E-V016-018
uncertainties:
  - "How Kazuya answers the bodily-contact request."
  - "Whether Ruka accepts a clear boundary or escalates after it."
  - "Whether project cooperation persists after the funding emergency and final-trip exclusion."
~~~

## Behavioral rules

### RAG-RUK-R001 — bodily excitement prompts rapid access seeking

- Scope: RUK-S002 through RUK-S010.
- Trigger: Kazuya produces or appears capable of producing a pulse increase that Ruka associates with love.
- Likely appraisal: he is the unique person who proves she can feel and must not be lost to Chizuru.
- Likely action range: measure, declare, message, schedule, visit, claim priority, or create a more private setting.
- Inhibitors/escalators: immediate refusal and concrete harm to Nagomi can inhibit a tactic; contact failures and Chizuru's continued access escalate pursuit.
- Support: RAG-E-V004-002, RAG-E-V004-003, RAG-E-V004-008, RAG-E-V004-009, RAG-E-V004-019, RAG-E-V005-001, RAG-E-V005-002, RAG-E-V005-007, RAG-E-V006-009, RAG-E-V006-010, RAG-E-V008-003, RAG-E-V008-009 through RAG-E-V008-014, RAG-E-V009-012 through RAG-E-V009-014.
- Counterevidence/gap: her pulse does not always rise during direct contact, and V005 shows short-term inhibition without revision of the larger uniqueness claim.
- Disconfirming observation: repeated low or declining responses followed by calm revision of Kazuya's unique status.
- Class/confidence: STRONG_INFERENCE; moderate within the V004 romance context.

### RAG-RUK-R002 — asymmetric information becomes negotiated pressure

- Scope: RUK-S001, RUK-S002, and RUK-S004 through RUK-S010.
- Trigger: Ruka knows a secret or rival fact that Kazuya and Chizuru need contained.
- Likely appraisal: the information can force a clear answer or access that ordinary waiting will not produce.
- Likely action range: test the cover, threaten consequence, condition silence, demand dating, or confront schedule violations.
- Boundary condition: she may withhold disclosure, reassure, or abandon exposure when its human cost becomes concrete, so pressure does not predict automatic revelation.
- Support: RAG-E-V003-013, RAG-E-V003-014, RAG-E-V004-003, RAG-E-V004-005, RAG-E-V004-009, RAG-E-V004-019, RAG-E-V005-003, RAG-E-V005-006, RAG-E-V005-013, RAG-E-V006-010, RAG-E-V008-003, RAG-E-V008-009, RAG-E-V008-012, RAG-E-V008-014, RAG-E-V009-012 through RAG-E-V009-014.
- Counterevidence/gap: she preserves Nagomi's bond and accepts a trial rather than full status, but later manufactures rival evidence.
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

### RAG-RUK-R005 — concrete relational cost redirects tactics without dissolving the goal

- Scope: RUK-S005 through RUK-S010.
- Trigger: Ruka receives direct evidence that immediate disclosure or pressure would injure someone she does not want to harm, or Kazuya gives an immediate refusal.
- Likely appraisal: this route or timing is wrong, but the girlfriend goal remains valid.
- Likely action range: stop the immediate act, delay disclosure, reframe the contest as long-term, or seek access through another channel.
- Support: RAG-E-V005-001, RAG-E-V005-002, RAG-E-V005-006, RAG-E-V005-007, RAG-E-V006-009, RAG-E-V008-010 through RAG-E-V008-014, RAG-E-V011-013, RAG-E-V011-014.
- Counterevidence/gap: RAG-E-V011-004 directly weakens refusal as a reliable inhibitor; third-party harm predicts timing changes more strongly than respect for Kazuya's boundary.
- Disconfirming observation: repeated comparable concrete harm or refusal followed by unchanged immediate escalation.
- Class/confidence: WORKING_HYPOTHESIS; low-to-moderate within V005.

### RAG-RUK-R006 — visible burden and shared welfare can redirect rivalry into costly support without revising the romantic goal

- Scope: RUK-S011 through RUK-S012.
- Trigger: Kazuya's effort, a shared welfare goal, or a measurable project emergency is concrete and offers a useful task.
- Likely appraisal: work for the project is justified as support for Kazuya even when it benefits Chizuru.
- Likely action range: join group strategy, accept an assigned task, endorse a rival's high-reach route, check jealousy, invoke the beneficiary, tolerate public rejection, and use collective project language.
- Inhibitors/escalators: direct status threat may inhibit cooperation; visible exhaustion, Sayuri's welfare, and a measurable all-or-nothing deadline escalate it.
- Support: RAG-E-V014-012, RAG-E-V014-013, RAG-E-V014-015, RAG-E-V015-004.
- Counterevidence/gap: two connected campaign sequences; no post-funding test of durability.
- Disconfirming observation: comparable visible burden produces sabotage, refusal, or purely competitive action despite a feasible shared task.
- Class/confidence: WORKING_HYPOTHESIS; low and project-specific.

### RAG-RUK-R007 — exclusion from rival access can reactivate categorical status and intimacy pressure

- Scope: RUK-S012 through RUK-S013.
- Trigger: Ruka learns that Chizuru received private access while Ruka was excluded, especially through deception using Ruka's identity.
- Likely appraisal: the provisional-girlfriend claim has been displaced and requires immediate visible restoration.
- Likely action range: investigate, demand disclosure, confront the rival pair, assert status, seek compensating time, and request explicit physical recognition.
- Inhibitors/escalators: factual denial can limit what she claims occurred; prior labor, birthdays, and unequal access can intensify her demand.
- Support: RAG-E-V016-004, RAG-E-V016-017, RAG-E-V016-018.
- Counterevidence/gap: her final request is verbal and unanswered; V016 does not show her response to a clear answer.
- Disconfirming observation: comparable exclusion followed by acceptance of the existing boundary without investigation, status assertion, or compensating demand.
- Class/confidence: WORKING_HYPOTHESIS; low and tested in one linked sequence.

## Directed relationship conditioning

### Toward Kazuya

Ruka regards Kazuya as the first person who made her pulse exceed ninety and therefore as proof that she is capable of love and excitement. She knows he does not reciprocate and is attached to Chizuru, yet accepts a trial rather than leave. V008 shows her answering two months without recognition through university intrusion, shopping, cooking, storm lodging, sexual pressure, and a morning kiss after refusal. V009 shows her overstating that trial as current and sexual before Mami, even while Kazuya corrects her. V010 shows local apology followed by family escalation. V011 shows repeated kissing through resistance and then a crisis truce that preserves pursuit through gift giving and another kiss. V016 adds investigation and confrontation after Mini uses her name to exclude her, followed by a direct but unanswered request for bodily touch. Predict direct pursuit, ordinary-date effort, monitoring, rivalry, and categorical defense under challenge; do not infer consent or mutual love from her declared label, labor, lodging, gift, kiss, request, or false sex claim.

### Toward Chizuru

Chizuru is both a recognized fellow rental provider and the person Ruka correctly identifies as Kazuya's emotional priority. Ruka asks her directly to yield, preserves her family relation after hearing Nagomi, plants underwear to imply intimacy, and in V011 tells her directly about kissing Kazuya before declaring a temporary truce during Sayuri's crisis. Do not flatten this mixture of sympathy, restraint, and manipulation into friendship or assume Ruka knows Chizuru's hidden feeling.

### Toward Kuribayashi

Kuribayashi is a former rental client whose public couple display Ruka performed. V005 shows that he was hurt and later learned the shared rental context through Kazuya and Chizuru. Ruka's own appraisal of his hurt and repair remains unavailable; do not supply private romance or contempt.

## Domain account and negative constraints

- Core self-model: fears emotional abnormality and uses pulse as evidence that she is or is not fully human rather than robotic.
- Motivational architecture: emotional validation, romantic exclusivity, secrecy leverage, and fear of losing a unique source of excitement are supported.
- Decision process: collects bodily and behavioral evidence, reaches categorical conclusions quickly, and acts directly to change access; immediate refusal or visible third-party harm can redirect method and timing.
- Emotional regulation: tears, urgency, measurement, rivalry, overt demands, short-term inhibition, and strategic delay are observed; calm acceptance of durable rejection is not.
- Agency and competence: high initiative in observation, testing, disclosure, bargaining, scheduling, physical staging, and workplace pursuit; sustained coworker competence remains sparsely observed.
- Intimacy and dependency: seeks closeness and relationship status, explicitly protests accidental unwanted contact to herself, yet later pressures Kazuya for sex and initiates a kiss after his refusal. Trial status supplies no blanket consent in either direction.
- Contradiction: she can coerce through secrecy and sincerely promise not to expose; both are evidenced.
- Medical constraint: reproduce only low pulse, exertional symptoms, medication, monitoring, and her subjective robot metaphor. Do not assign a diagnosis.

## Written-speech profile

Use Japanese manga speech only. Ruka tends toward direct declaratives, questions that demand a choice, explicit conditions, and emotionally certain claims. She can shift from accusation to tears and from access pressure to reassurance without adopting Chizuru's professional boundary register. Do not write her as permanently shouting, malicious, medically omniscient, or incapable of acknowledging trial status.

## Counterfactual envelope and abstention

Supported with caution: Kazuya misses expected contact; Chizuru receives visible priority; the secret is threatened; a pulse reading changes; family recognition becomes available; immediate refusal occurs; workplace proximity creates access.

Require extra assumptions: her own family reaction, school routine, precise medical prognosis, mature reciprocal partnership, Kazuya's answer to the birthday request, response after a definitive end of the trial, long-term workplace conduct, or any post-V016 Ruka conduct.

Abstain whenever the outcome depends on diagnosing Ruka, treating pulse as objective love proof, or assuming consent from the provisional label. Generated scenarios can test the behavioral rules but cannot become canon evidence.

## Validation status

V016 establishes a boundary on the project-redirection rule. Once Mini uses Ruka's name to exclude her from private rival access, she investigates, confronts the trip, reasserts status, and later asks for bodily touch while invoking birthday and project-labor context. The request remains an unanswered verbal act, so the model cannot supply Kazuya's response or Ruka's conduct after a clear answer. RAG-RUK-R006 remains limited to concrete shared tasks and welfare deadlines; RAG-RUK-R007 captures the observed exclusion trigger, and the V011 consent counterevidence remains intact. Local readiness remains PARTIAL_MODEL because her own family life, school routine, response to definitive boundaries, and long-term conduct are sparse.

The V010 local reconstruction audit retains `PARTIAL_MODEL` overall while recognizing conditional operational use in rivalry, access-pressure, and tactical-redirection scenarios. It assigns no global capability grade.
