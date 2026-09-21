---
title: "Rent-a-Girlfriend - Ruka Sarashina Reconstruction Model"
artifact_id: RAG_RUKA_RECONSTRUCTION_MODEL
artifact_type: character_reconstruction_model
series: Rent-a-Girlfriend
generation: V1
version: "1.23"
status: canonical
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
created: "2026-09-19"
source_boundary: "Operational model based on Japanese manga witnesses RAG-JP-EPUB-V003-V025, with V012-V013 and V019 negative-evidence review."
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
    - RAG-JP-EPUB-V017
    - RAG-JP-EPUB-V018
    - RAG-JP-EPUB-V019
    - RAG-JP-EPUB-V020
    - RAG-JP-EPUB-V021
    - RAG-JP-EPUB-V022
    - RAG-JP-EPUB-V023
    - RAG-JP-EPUB-V024
    - RAG-JP-EPUB-V025
  admitted_through_volume: V025
  narrative_time_boundary: "after Ruka receives Kuribayashi's direct clarification that he is concerned rather than angry, expresses affection toward Kazuya without reciprocal reclassification, and stands in the group when Chizuru's Diamond profile appears on Nagomi's phone"
  basis_checkpoint: RAG_CP_V010
  basis_commit: 18fe1738f18a66a91e6a3a340f845f3d7c3d4efe
  model_revision: "1.22"
  prior_knowledge_limitations:
    - "No post-V025 narrative evidence is admitted."
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

This model supports tightly bounded reconstruction of Ruka at the V025 endpoint when bodily self-monitoring, romantic certainty, rivalry, disputed termination, family exposure, former-client contact, and status challenge are salient. It can model her direct speech, high initiative, ordinary-date effort, local apology, sexual pressure, unilateral intimacy, categorical overstatement, evidence fabrication, selective nondisclosure, and alliance testing. It must abstain on a precise diagnosis, family life, workable separation, a romantic meaning for Kuribayashi's clarification, her response after the profile display, knowledge she does not receive, and any assumption that pulse, a former provisional label, gifts, or physical initiative prove mutual love or consent.

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
valid_until_source: "V017 0004"
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

### RUK-S014 — bounded-request pursuer with first-name privilege

~~~yaml
state_id: RUK-S014
valid_from_source: "V017 0005"
valid_until_source: "V018 0170"
entry_conditions:
  - "Kazuya must answer the birthday bodily-contact request made after Ruka's exclusion from the final-location trip."
active_goals:
  - obtain chosen physical and symbolic recognition from Kazuya
  - preserve and publicly display the provisional-girlfriend claim
  - extend access through time together and domestic performance
known_propositions:
  - "Kazuya consents to applying sunscreen but limits the act to that task."
  - "Her pulse reaches ninety-four, which she interprets within her established love model."
  - "Kazuya blocks an attempted hug but permits her to call him Kazuya without an honorific."
  - "Chizuru and Mini can observe the first-name address and her girlfriend claim."
relationship_conditions:
  - "Ruka treats the narrow naming privilege as meaningful recognition while Kazuya does not formalize the trial."
  - "She describes her pursuit as chosen and uses route selection to maximize time with him."
  - "Apartment access and domestic labor expand her performed status, but a shared-bath proposal is not accepted."
changed_from_previous:
  - SUNSCREEN_CONTACT_GRANTED_WITH_BOUNDED_SCOPE
  - PULSE_NINETY_FOUR_SELF_INTERPRETED
  - DELIBERATE_EXTENDED_PROXIMITY_EXPLAINED
  - HUG_BLOCKED
  - FIRST_NAME_PERMISSION_GRANTED
  - FIRST_NAME_USED_PUBLICLY
  - DOMESTIC_STATUS_PRESSURE_CONTINUED
evidence_refs:
  - RAG-E-V017-001
  - RAG-E-V017-002
  - RAG-E-V017-003
  - RAG-E-V017-004
  - RAG-E-V017-007
uncertainties:
  - "Whether she preserves request specificity across later intimacy pressure."
  - "Whether first-name permission changes the trial or only its public appearance."
  - "How she responds to a definitive relationship decision."
~~~

### RUK-S015 — truce-bound rival allowing bereavement support while preserving future access

~~~yaml
state_id: RUK-S015
valid_from_source: "V018 0171"
valid_until_source: "V020 0045"
entry_conditions:
  - "Sayuri has died, Kazuya wants to encourage Chizuru, and Ruka's earlier crisis truce remains relevant."
active_goals:
  - allow an immediate bereavement-support action without surrendering her own claim
  - retain a future date and visible relationship access with Kazuya
known_propositions:
  - "Chizuru is bereaved and Kazuya wants to encourage her."
  - "Direct encouragement may help or may become excessive depending on delivery."
  - "Kazuya is preparing action centered on Chizuru during the truce."
relationship_conditions:
  - "Ruka shows sympathy and does not block the immediate plan."
  - "She asks Kazuya to take her to an amusement park, preserving future access."
changed_from_previous:
  - CHIZURU_BEREAVEMENT_ACKNOWLEDGED
  - IMMEDIATE_SUPPORT_ROUTE_ALLOWED
  - ENCOURAGEMENT_ADVICE_OFFERED
  - FUTURE_AMUSEMENT_DATE_REQUESTED
evidence_refs:
  - RAG-E-V018-016
uncertainties:
  - "Whether the amusement-park request is scheduled or fulfilled."
  - "Whether the truce survives Kazuya's planned rental date."
  - "How she responds to a definitive relationship decision."
~~~

### RUK-S016 — post-truce pursuer obtaining negotiated local access

~~~yaml
state_id: RUK-S016
valid_from_source: "V020 0046"
valid_until_source: "V021 0084"
entry_conditions:
  - "Ruka's crisis accommodation has received no V019 consequence, and Kazuya has completed the Chizuru-focused support date."
active_goals:
  - obtain reciprocal attention after allowing Kazuya's crisis support route
  - secure ordinary access and physical recognition without abandoning the trial claim
known_propositions:
  - "Kazuya completed the support date and says Chizuru is doing acceptably."
  - "He refuses an overnight hot-spring trip but will accept a nearby day outing."
  - "He gives verbal permission for a five-second hug."
relationship_conditions:
  - "Ruka invokes prior accommodation as a reason he should consider her feelings."
  - "The hug has explicit duration and assent, unlike earlier unilateral kisses."
  - "Kazuya remains internally in love with Chizuru and supplies no official conversion."
changed_from_previous:
  - POST_TRUCE_RECIPROCITY_REQUESTED
  - OVERNIGHT_TRAVEL_REFUSED
  - LOCAL_OUTING_SUBSTITUTED
  - FIVE_SECOND_HUG_REQUESTED_AND_PERMITTED
  - ORDINARY_RECOGNITION_SOUGHT
evidence_refs:
  - RAG-E-V020-005
  - RAG-E-V020-006
  - RAG-E-V020-007
  - RAG-E-V020-008
uncertainties:
  - "Whether specific request-and-answer conduct persists under stronger rivalry threat."
  - "Whether she recognizes Kazuya's direct declaration to Chizuru."
  - "How she responds to a definitive end of the trial."
~~~

### RUK-S017 — rejected-trial terminus resister

~~~yaml
state_id: RUK-S017
valid_from_source: "V021 0085"
valid_until_source: "V022 0004"
entry_conditions:
  - "Ruka has obtained one negotiated outing and hug, while Kazuya remains in love with Chizuru and now seeks to end the trial explicitly."
active_goals:
  - prevent the provisional relation from being treated as ended
  - preserve access to Kazuya despite acknowledged nonreciprocity
  - outlast Chizuru's priority through persistence
known_propositions:
  - "Kazuya loves Chizuru from the bottom of his heart."
  - "He says he has no romantic feeling for Ruka and apologizes for continuing the trial."
  - "He asks her directly to break up."
relationship_conditions:
  - "Ruka refuses the requested shared ending and continues to claim the relation."
  - "Kazuya's withdrawal means her label does not establish his ongoing consent."
changed_from_previous:
  - BREAKUP_REQUEST_RECEIVED
  - NONRECIPROCITY_EXPLICITLY_ACKNOWLEDGED
  - TERMINATION_REFUSED
  - FATE_AND_UNILATERAL_LOVE_ASSERTED
  - RULE_VIOLATION_DECLARED
  - MESSAGE_PRESSURE_INCREASED
evidence_refs:
  - RAG-E-V021-011
  - RAG-E-V021-012
  - RAG-E-V021-022
uncertainties:
  - "Whether she will negotiate practical distance or intensify contact further."
  - "How she responds to a completed Kazuya-Chizuru classification or family disclosure."
  - "Whether increased messages include threats, ordinary contact, or both."
~~~

### RUK-S018 — coercive rival using fabricated evidence after termination

~~~yaml
state_id: RUK-S018
valid_from_source: "V022 0005"
valid_until_source: "V023 0004"
entry_conditions:
  - "Kazuya has explicitly withdrawn, denied romantic reciprocity, and plans to confess to Chizuru while Ruka refuses to recognize the ending."
active_goals:
  - preserve immediate bodily and spatial access to Kazuya
  - prevent Chizuru from accepting or encouraging Kazuya's confession
  - maintain visible status inside Nagomi's family trip
known_propositions:
  - "Kazuya continues to say he loves Chizuru rather than Ruka."
  - "Chizuru accepts Nagomi's family trip despite intending to refuse."
  - "Ruka suspects Chizuru may like Kazuya and can be affected by apparent sexual evidence."
  - "Mami, Kazuya's former girlfriend, is also embedded in the trip."
relationship_conditions:
  - "Ruka's claim remains unilateral after Kazuya's withdrawal."
  - "Nagomi treats Ruka as Chizuru's close friend rather than as Kazuya's partner."
  - "Ruka and Chizuru share direct rivalry knowledge that the family audience lacks."
changed_from_previous:
  - OVERNIGHT_ACCESS_ATTEMPTED_AFTER_WITHDRAWAL
  - FORCED_KISS_REPEATED
  - FAMILY_TRIP_ACCESS_ACCEPTED
  - CHIZURU_DIRECTLY_MONITORED
  - SEXUAL_EVENT_FABRICATED
  - MATERIAL_EVIDENCE_USED_AS_WEDGE
  - MAMI_TRIP_PRESENCE_RECOGNIZED
evidence_refs:
  - RAG-E-V022-001
  - RAG-E-V022-002
  - RAG-E-V022-003
  - RAG-E-V022-004
  - RAG-E-V022-005
  - RAG-E-V022-006
  - RAG-E-V022-008
  - RAG-E-V022-016
  - RAG-E-V022-025
uncertainties:
  - "How long Chizuru believes the fabricated sex claim and whether it is corrected."
  - "Whether Ruka escalates, narrows, or changes tactics after seeing Kazuya attempt confession."
  - "How Mami's presence alters Ruka's rivalry priorities."
~~~

### RUK-S019 — public claimant repeating fabricated evidence under coalition and correction pressure

~~~yaml
state_id: RUK-S019
valid_from_source: "V023 0005"
valid_until_source: null
entry_conditions:
  - "Ruka is inside the Hawaiians trip after Kazuya's withdrawal, with Chizuru holding the fabricated wrapper and Mami embedded as another informed former partner."
active_goals:
  - preserve visible girlfriend status before peers and family
  - obtain private bodily and emotional access despite Kazuya's withdrawal
  - keep the fabricated sexual claim credible enough to deter Chizuru
  - evaluate whether Mami's intervention can advance Ruka's own goal without surrendering control
known_propositions:
  - "Mami knows Chizuru is a rental girlfriend and questions whether Chizuru genuinely likes Kazuya."
  - "Mami is willing to raise possible disclosure to Nagomi and tests what Ruka would do."
  - "Kazuya objects to Ruka's public girlfriend claim and removes her after the false lost-key isolation."
  - "Kazuya directly denies the asserted sexual relation in Chizuru's presence."
  - "Chizuru begins checking Kazuya's credibility rather than accepting the wrapper without question."
relationship_conditions:
  - "Ruka's status remains unilateral after explicit withdrawal."
  - "Mami is a possible tactical interlocutor, not an established ally."
  - "Chizuru and Kazuya now have a direct verification route that threatens the wrapper wedge."
changed_from_previous:
  - MAMI_SUPPORT_PROBE_RECEIVED
  - PUBLIC_GIRLFRIEND_STATUS_DECLARED
  - FALSE_KEY_ISOLATION_USED
  - BODILY_PRESSURE_REJECTED
  - REAL_STATUS_TEST_RECEIVED
  - CHIZURU_FEELING_HYPOTHESIS_PRESSED
  - NAGOMI_DISCLOSURE_ROLE_TESTED
  - WRAPPER_CLAIM_REPEATED_PUBLICLY
  - KAZUYA_DENIAL_RECEIVED
  - CHIZURU_VERIFICATION_OBSERVED
evidence_refs:
  - RAG-E-V023-004
  - RAG-E-V023-012
  - RAG-E-V023-013
  - RAG-E-V023-014
  - RAG-E-V023-015
  - RAG-E-V023-016
  - RAG-E-V023-017
  - RAG-E-V023-018
uncertainties:
  - "Whether Ruka accepts, rejects, or exploits Mami's possible coalition route."
  - "Whether the fabricated sex claim survives Kazuya's denial and Chizuru's source check."
  - "Whether she can establish any noncoercive separation or contact arrangement."
~~~

### RUK-S020 — selective cover preserver under ring and classification pressure

~~~yaml
state_id: RUK-S020
valid_from_source: "V024 0005"
valid_until_source: null
entry_conditions:
  - "Ruka remains inside the Hawaiians trip after Kazuya denies her fabricated claim and Chizuru begins direct verification."
active_goals:
  - test whether Nagomi could accept Kazuya choosing someone other than Chizuru
  - force Chizuru to confront the ring, family lie, and her own emotional classification
  - preserve the fabricated sexual wedge despite direct contradiction
  - retain control over whether and when the family audience receives the rental truth
known_propositions:
  - "Nagomi says she would support the person Kazuya chooses because his happiness governs her answer."
  - "Chizuru denies a marriage plan, treats the ring as held rather than accepted, and acknowledges responsibility for the deception."
  - "Chizuru does not answer whether Kazuya is her favorite person or only a customer."
  - "Nagomi can enter the private conflict without warning, making immediate disclosure a live option."
  - "Kuribayashi seeks Ruka directly and says that he came to see her."
relationship_conditions:
  - "Ruka's claim remains unilateral after Kazuya's withdrawal and denial of the asserted sexual event."
  - "Nagomi continues to understand Ruka as Chizuru's younger-sister-like friend."
  - "Ruka and Chizuru share moral pressure and rivalry knowledge while preserving the cover before family."
changed_from_previous:
  - NAGOMI_ACCEPTANCE_TESTED_HYPOTHETICALLY
  - SELF_DISCLOSURE_APPROACHED_AND_WITHHELD
  - RING_RETURN_DEMANDED
  - CHIZURU_RESPONSIBILITY_PRESSED
  - FAVORITE_PERSON_CUSTOMER_BINARY_DEMANDED
  - FABRICATED_SEX_CLAIM_REPEATED
  - NAGOMI_INTERRUPTION_COVERED_TWICE
  - KURIBAYASHI_DIRECT_APPROACH_RECEIVED
evidence_refs:
  - RAG-E-V024-003
  - RAG-E-V024-004
  - RAG-E-V024-010
  - RAG-E-V024-011
  - RAG-E-V024-012
  - RAG-E-V024-013
  - RAG-E-V024-018
uncertainties:
  - "Whether she later discloses, continues cover, or changes tactics after the chapel event."
  - "Whether Chizuru's inability to answer alters Ruka's belief or only intensifies rivalry."
  - "Why Kuribayashi seeks her and how she responds."
~~~

### RUK-S021 — former-provider recipient of bounded clarification at an exposure threshold

~~~yaml
state_id: RUK-S021
valid_from_source: "V025 0005"
valid_until_source: null
entry_conditions:
  - "Ruka has received Kuribayashi's direct approach while her unilateral Kazuya claim, fabricated sexual evidence, and selective family cover remain active."
active_goals:
  - understand or contain the former client's reason for approaching
  - continue expressing her own affection toward Kazuya despite his withdrawal
  - respond to any family or peer consequence of Chizuru's exposed rental profile
  - preserve her claimed status without treating Kuribayashi's concern as romantic proof
known_propositions:
  - "Kuribayashi is glad to see Ruka, worried after she left the service, and blames his own status performance rather than her."
  - "Kazuya is visibly distressed at the pool, but he gives Ruka no reciprocal status answer."
  - "Chizuru's Diamond profile is visible on Nagomi's fallen phone before the group."
relationship_conditions:
  - "The former client-provider grievance Ruka anticipated is reduced, but no new personal relation is agreed."
  - "Kazuya's withdrawal remains explicit despite Ruka's affection and physical proximity."
  - "Ruka is a partly informed witness inside a public exposure that may change Nagomi and Kibe's knowledge."
changed_from_previous:
  - KURIBAYASHI_NONANGER_CLARIFICATION_RECEIVED
  - FORMER_CLIENT_CONCERN_RECEIVED
  - FORMER_CLIENT_SELF_CRITIQUE_RECEIVED
  - POOL_AFFECTION_RENEWED_WITHOUT_STATUS_ANSWER
  - DIAMOND_PROFILE_EXPOSURE_WITNESSED
evidence_refs:
  - RAG-E-V025-002
  - RAG-E-V025-011
  - RAG-E-V025-015
  - RAG-E-V025-016
  - RAG-E-V025-021
uncertainties:
  - "Whether she answers Kuribayashi with gratitude, distance, support, or another status interpretation."
  - "Whether the exposure causes her to correct, repeat, or strategically use prior claims."
  - "How she behaves when Nagomi and Kibe can directly question Chizuru's service identity."
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

### RAG-RUK-R008 — resistance to a higher-intimacy request can redirect pursuit toward narrower symbolic recognition

- Scope: RUK-S014.
- Trigger: Kazuya blocks or hesitates at a requested intimacy act while Ruka still seeks visible birthday recognition.
- Likely appraisal: the larger romantic goal remains valid, but a smaller mutually acknowledged change can still count as progress.
- Likely action range: stop the resisted act, request naming or another bounded privilege, practice it, and later display it before rivals.
- Inhibitors/escalators: immediate bodily resistance redirects the tactic; rivalry audiences and status insecurity escalate public use of the narrower permission.
- Support: RAG-E-V017-004, RAG-E-V017-007.
- Counterevidence/gap: one sequence; later domestic and status pressure shows that tactical narrowing is not general goal revision.
- Disconfirming observation: repeated resisted requests produce no narrower negotiation and only unchanged physical escalation.
- Class/confidence: WORKING_HYPOTHESIS; low and sequence-specific.

### RAG-RUK-R009 — explicit refusal can narrow travel and touch demands into negotiated finite access

- Scope: RUK-S016.
- Trigger: Kazuya rejects an overnight proposal while Ruka seeks recognition after accommodating his support for Chizuru.
- Likely appraisal: the larger access goal can be preserved through a nearby outing and a short, answerable contact request.
- Likely action range: invoke desired reciprocity, propose broad access, accept refusal, substitute a local plan, state a timed hug request, and wait for verbal permission.
- Inhibitors/escalators: explicit refusal narrows scope; accumulated rivalry and perceived sacrifice escalate the demand for recognition.
- Support: RAG-E-V020-005 through RAG-E-V020-008.
- Counterevidence/gap: one sequence and one hug; earlier kisses through resistance remain strong contrary history against generalized consent sensitivity.
- Disconfirming observation: under another clear refusal, she treats the bounded permission as authority for broader contact or resumes unilateral physical escalation without a new request.
- Class/confidence: WORKING_HYPOTHESIS; low and provisional.

### RAG-RUK-R010 — definitive breakup pressure can intensify nonseverability claims and access persistence

- Scope: RUK-S017.
- Trigger: Kazuya names Chizuru as his preferred person, denies romantic feeling for Ruka, apologizes, and asks to end the trial.
- Likely appraisal: her own love and destiny claim make the relation worth preserving even without his reciprocal classification.
- Likely action range: reject termination, cry, use physical pressure, invoke fate, promise continued rule violations, and increase messaging.
- Inhibitors/escalators: acknowledged rivalry and loss of status escalate persistence; no successful durable inhibitor is observed in V021.
- Support: RAG-E-V021-011, RAG-E-V021-012, RAG-E-V021-022.
- Counterevidence/gap: one breakup sequence; earlier episodes show local narrowing after refusal but not acceptance of a durable relationship ending.
- Disconfirming observation: after another explicit withdrawal, she promptly accepts distance and ceases status or access pressure without an external crisis forcing delay.
- Class/confidence: WORKING_HYPOTHESIS; low and termination-specific.

### RAG-RUK-R011 — feared rival acceptance can shift status pressure into targeted evidence fabrication

- Scope: RUK-S018, with antecedent support in RUK-S005 and RUK-S008.
- Trigger: Kazuya explicitly chooses Chizuru, Chizuru accepts unusual family access, and direct persistence appears insufficient to prevent a confession.
- Likely appraisal: changing the rival's belief about existing sexual intimacy may deter her more effectively than another unilateral status claim.
- Likely action range: monitor the rival's decision, select a plausible sexual prop, state a false event, leave the prop as continuing evidence, and preserve public closeness to Kazuya.
- Inhibitors/escalators: visible family harm has previously delayed disclosure; explicit termination and suspected rival feeling escalate fabrication.
- Support: RAG-E-V005-007, RAG-E-V009-012 through RAG-E-V009-014, RAG-E-V022-003 through RAG-E-V022-008.
- Counterevidence/gap: one fully explicit planned fabrication and earlier false or implied intimacy claims; its durability and later correction are unknown.
- Disconfirming observation: under another comparable termination and rival-access threat, she accurately represents the relationship and accepts the rival's informed decision without manufactured evidence.
- Class/confidence: WORKING_HYPOTHESIS; low and high-threat rivalry-specific.

### RAG-RUK-R012 — when a fabricated wedge loses exclusivity, she may repeat it through direct status pressure

- Scope: RUK-S019.
- Trigger: the target sees the material evidence in a shared setting where Kazuya can contradict the claim.
- Likely appraisal: the lie must be reinforced as proof of a broader relationship before the rival can verify independently.
- Likely action range: frame the object as a keepsake, repeat the sexual account, demand that Kazuya affirm status, and continue public girlfriend presentation.
- Support: RAG-E-V023-012, RAG-E-V023-016, RAG-E-V023-017.
- Counterevidence/gap: one escalation sequence; Kazuya's denial and Chizuru's question show immediate loss of control rather than success.
- Disconfirming observation: comparable exposure of a fabricated claim produces prompt correction, withdrawal, and no attempt to preserve status through repetition.
- Class/confidence: WORKING_HYPOTHESIS; low and fabrication-specific.

### RAG-RUK-R013 — family-harm proximity can preserve selective cover while private status pressure intensifies

- Scope: RUK-S020, with antecedent support in RUK-S005 and RUK-S010.
- Trigger: Ruka can expose the central deception before an emotionally invested family member while still seeking advantage over Chizuru.
- Likely appraisal: immediate disclosure may impose unacceptable family cost, but withholding it need not reduce the legitimacy of her private claim or demands.
- Likely action range: test acceptance hypothetically, approach disclosure, stop, invent a local cover story, and resume direct moral or emotional-classification pressure in private.
- Inhibitors/escalators: Nagomi's attachment and physical presence inhibit disclosure; Chizuru's ring retention and inability to classify Kazuya escalate private pressure.
- Support: RAG-E-V024-003, RAG-E-V024-004, RAG-E-V024-011 through RAG-E-V024-013.
- Counterevidence/gap: one resort interval; selective cover coexists with fabrication, so it does not establish broad truthfulness or altruism.
- Disconfirming observation: repeated comparable access to an invested family audience produces either automatic exposure or complete withdrawal from private pressure rather than the observed split.
- Class/confidence: WORKING_HYPOTHESIS; low and family-exposure-specific.

## Directed relationship conditioning

### Toward Kazuya

Ruka regards Kazuya as the first person who made her pulse exceed ninety and therefore as proof that she is capable of love and excitement. She knows he does not reciprocate and is attached to Chizuru, yet accepts a trial rather than leave. V008 shows sexual pressure and a morning kiss after refusal; V009-V011 show status overstatement, local apology, repeated kissing through resistance, and a crisis truce that preserves pursuit. V016 adds investigation and confrontation after Mini uses her name to exclude her. V017 answers the resulting request with bounded sunscreen contact, records a pulse of ninety-four, and shows her redirect a blocked hug into first-name permission before using that permission publicly and continuing domestic status pressure. V018-V020 move crisis accommodation into later reciprocity pressure, but also add a clear overnight refusal, local-plan substitution, and five-second hug after verbal permission. V021 shows a qualitatively stronger boundary: Kazuya withdraws from the trial, and Ruka refuses the ending and increases pressure. V022 answers that boundary with an overnight attempt, forced kiss, and fabricated wrapper. V023 adds public girlfriend declaration, false-pretext isolation, and repetition of the sex claim under direct denial. V024 does not restore access or status; it shifts her pressure toward Chizuru and Nagomi while Kazuya prepares direct speech elsewhere. Predict direct pursuit, monitoring, rivalry, and tactical change, but do not treat her claim as Kazuya's consent or infer mutual love from any label, labor, contact, request, or pulse.

### Toward Chizuru

Chizuru is both a recognized fellow rental provider and the person Ruka correctly identifies as Kazuya's emotional priority. Ruka asks her directly to yield, preserves her family relation after hearing Nagomi, plants underwear to imply intimacy, and in V011 tells her directly about kissing Kazuya before declaring a temporary truce during Sayuri's crisis. V022 adds an explicit planned lie: Ruka uses a torn condom wrapper and a false sex claim because she suspects Chizuru may like Kazuya. V023 shows her repeat that claim after the wrapper reappears, while Kazuya denies it and Chizuru checks him directly. V024 adds ring-return and favorite-person/customer pressure, another repetition of the false account, and two cover stories before Nagomi. Do not flatten this mixture of sympathy, restraint, moral argument, and manipulation into friendship or treat suspicion as knowledge of Chizuru's feeling.

### Toward Kuribayashi

Kuribayashi is a former rental client whose public couple display Ruka performed. V005 shows that he was hurt and later learned the shared rental context through Kazuya and Chizuru. V024 has him seek Ruka directly. V025 clarifies that he was glad to see her, worried after she left the service, is not angry, and criticizes his own status performance. Ruka is surprised, but her developed response remains unavailable; do not convert his concern into romance, friendship, continuing access, or broad reconciliation.

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

Require extra assumptions: her own family reaction, school routine, precise medical prognosis, mature reciprocal partnership, workable conduct after Kazuya's withdrawal, long-term workplace conduct, durable correction after the fabrication, romantic meaning in Kuribayashi's concern, her response after the profile display, or any post-V025 conduct.

Abstain whenever the outcome depends on diagnosing Ruka, treating pulse as objective love proof, or assuming consent from the provisional label. Generated scenarios can test the behavioral rules but cannot become canon evidence.

## Validation status

V020 validates one stronger request-and-answer case: Ruka accepts refusal of an overnight trip, narrows the outing, states a five-second hug request, and waits for permission. V022-V023 sharply bound that success because definitive withdrawal and rival threat produce a forced kiss, deliberate sexual-evidence fabrication, deceptive isolation, and repeated falsehood under challenge. V024 validates a narrower family-exposure inhibitor. V025 resolves Kuribayashi's purpose into concern and self-critique but gives too little Ruka response for a new rule, then places her at the profile exposure without follow-through. Local readiness remains PARTIAL_MODEL because family life, school routine, response after correction, and long-term conduct are sparse.

The V010 local reconstruction audit retains `PARTIAL_MODEL` overall while recognizing conditional operational use in rivalry, access-pressure, and tactical-redirection scenarios. It assigns no global capability grade.
