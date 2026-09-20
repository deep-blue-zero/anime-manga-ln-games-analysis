---
title: "Rent-a-Girlfriend - Kazuya Kinoshita Reconstruction Model"
artifact_id: RAG_KAZUYA_RECONSTRUCTION_MODEL
artifact_type: character_reconstruction_model
series: Rent-a-Girlfriend
generation: V1
version: "1.19"
status: canonical
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
created: "2026-09-19"
source_boundary: "Operational model based only on Japanese manga witnesses RAG-JP-EPUB-V001-V018."
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
  admitted_through_volume: V018
  narrative_time_boundary: "after improvised bedside film delivery, Sayuri's death, Chizuru's immediate refusal of help, Sumi's experiential support lesson, a wage advance, and Kazuya's submitted rental request for a planned best date"
  basis_checkpoint: RAG_CP_V010
  basis_commit: 18fe1738f18a66a91e6a3a340f845f3d7c3d4efe
  model_revision: "1.18"
  prior_knowledge_limitations:
    - "No post-V018 narrative evidence is admitted."
    - "Chizuru privately revisits her qualified non-negation and directly values Kazuya's life and work, but she supplies him no affirmative romantic answer or mutual status."
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
    - provisional relationship negotiation
    - jealousy-driven surveillance and correction
    - personal gift exchange
    - entry into paid karaoke employment
    - routine work and first wages
    - bounded truth disclosure and friendship repair
    - practice-client adaptation
    - protection of a shy practice provider under public harassment
    - acting-linked threat to continued rental access
    - interrupted attempt to formalize the Ruka relationship
    - responsibility-taking during a former-partner confrontation
    - direct preference statement to Chizuru
    - partial crisis disclosure and emotional support received from Sumi
    - crowdfunding and film-production research
    - direct non-booking project proposal
    - joint film commitment under family deadline
  missing_contexts:
    - sustained study or long-term employment performance
    - broad friendship life outside crisis
    - acknowledged reciprocal partnership
    - high-stakes non-romantic competence
    - executed film production or fundraising
    - durable honesty and later development
  translation_limitations:
    - "Model derives from the Japanese witness; no licensed translation was admitted for comparison."
  written_speech: PARTIALLY_MODELED
  performed_voice: OUT_OF_SCOPE
local_readiness: PARTIAL_MODEL
~~~

## Intended use

This model supports tightly bounded reconstruction of Kazuya at the V012 endpoint. It is useful for scenarios involving embarrassment, family expectations, bounded truth correction, protective action, adaptive support for and reception from Sumi, inherited obligation, direct disagreement with Chizuru, researched project support, and the asymmetric trial relationship when the scenario preserves his V012 knowledge. It should abstain from predicting Chizuru's romantic self-classification, mature partnership, successful fundraising or production, Mami's later use of the family account, Sayuri's prognosis, or behavior that requires information acquired after V012.

## Central mechanism

Kazuya rapidly converts affect into a social story. When rejection, shame, or another person's anticipated disappointment feels immediate, he searches for a response that relieves the present exposure: buying a date, attacking the performance, calling Chizuru his girlfriend, or extending the fiction to friends. The response often works locally and creates a larger maintenance cost.

His harsh self-model does not reliably inhibit this cycle. It can produce apology and attempted repair after consequences become concrete, but it also lets him narrate failure as an unchangeable personal fact. He alternates between inflation and deflation: idealizing an attractive woman's attention, then discounting conduct that would conflict with his belief that he is unworthy. V004 shows that conscious attachment does not cure the mechanism. V005 supplies a stronger counterexample to helplessness through friendship repair. V006 adds adaptive low-pressure support for Sumi and a direct statement of preference for Chizuru. V007-V010 add career support, privacy cost, restraint during accidental closeness, refusal of Ruka's sexual pressure, completed gift planning, a reckless drinking strategy under identity threat, and direct encouragement after new stage work. V011 supplies a stronger honesty counterexample: he begins a family confession and argues for truth before time runs out, although interruption and disagreement stop execution. V012-V016 supply a different competence path: after accepting Sumi's support, he researches and funds a concrete film route, revises under expert and metric feedback, recruits specialists, sustains public outreach, works inside a real production hierarchy, completes the final-location camera task, and initiates postproduction and theater planning. Observable action must still test safe judgment, delivery, and his interior account.

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
valid_until_source: "V004 0004"
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

### KAZ-S006 — provisional boyfriend under vocational, financial, and reciprocity pressure

~~~yaml
state_id: KAZ-S006
valid_from_source: "V004 0005"
valid_until_source: "V005 0004"
entry_conditions:
  - "Ruka clarifies the rental relation with Kuribayashi and makes secrecy contingent on dating."
active_goals:
  - protect Chizuru's job and the central secret
  - preserve contact with Chizuru while managing Ruka's trial status
  - reciprocate Chizuru's Christmas gift
  - earn money through the karaoke job
known_propositions:
  - "He does not reciprocate Ruka's love, and she recognizes his feeling for Chizuru."
  - "Chizuru wants to become an actress and uses rental work for income and practice."
  - "Chizuru selected a personal Christmas gift from their shared history."
  - "The handholding on the return-gift date remains part of paid service."
relationship_conditions:
  - "Ruka is a provisional girlfriend whose sincere attachment began under secrecy leverage."
  - "Chizuru is a paid provider who has also initiated an unpriced personalized exchange."
changed_from_previous:
  - RELATIONSHIP_STATUS_CHANGE
  - VOCATIONAL_KNOWLEDGE_CHANGE
  - FINANCIAL_ROUTINE_CHANGE
  - RECIPROCITY_CHANGE
evidence_refs:
  - RAG-E-V004-003
  - RAG-E-V004-005
  - RAG-E-V004-011
  - RAG-E-V004-012
  - RAG-E-V004-013
  - RAG-E-V004-014
  - RAG-E-V004-015
  - RAG-E-V004-016
  - RAG-E-V004-017
  - RAG-E-V004-019
uncertainties:
  - "Whether correction after surveillance becomes prospective restraint."
  - "How he responds to Ruka's private-room escalation."
  - "Whether employment produces durable competence or financial independence."
~~~

### KAZ-S007 — employed repair agent and recruited practice client

~~~yaml
state_id: KAZ-S007
valid_from_source: "V005 0005"
valid_until_source: "V006 0004"
entry_conditions:
  - "Ruka presses the private-room trial beyond weekly dating and Kazuya retreats."
active_goals:
  - manage Ruka's demand for recognition without exposing Chizuru
  - use work and money to repair Kuribayashi's injury
  - cooperate with Chizuru's request to practice-date Sumi
  - understand unresolved feeling toward Mami without abandoning his attachment to Chizuru
known_propositions:
  - "Ruka can stop after immediate refusal but continues a long contest for family and workplace access."
  - "Kuribayashi was sincerely hurt and now knows Kazuya's own rental-girlfriend deception."
  - "Chizuru understood and supported the Kuribayashi repair plan."
  - "Sumi is a new rental girlfriend whose communication difficulty motivates the practice date."
relationship_conditions:
  - "Ruka remains a provisional girlfriend denied recognition before Nagomi."
  - "Kuribayashi is a repaired but newly informed friend."
  - "Chizuru is a paid provider and off-platform coordinator who trusts him with Sumi's practice."
  - "Mami has seen him with Sumi, but her interpretation is unknown."
changed_from_previous:
  - CONSENT_EVIDENCE_CHANGE
  - EMPLOYMENT_DURABILITY_CHANGE
  - FRIEND_DISCLOSURE_CHANGE
  - COLLABORATOR_ROLE_CHANGE
evidence_refs:
  - RAG-E-V005-001
  - RAG-E-V005-003
  - RAG-E-V005-008
  - RAG-E-V005-009
  - RAG-E-V005-011
  - RAG-E-V005-014
  - RAG-E-V005-016
  - RAG-E-V005-017
uncertainties:
  - "Whether bounded honesty generalizes to family, Kibe, or later crises."
  - "How the Sumi date and Mami's observation change the relationship system."
~~~

### KAZ-S008 — adaptive helper and explicit but unresolved chooser

~~~yaml
state_id: KAZ-S008
valid_from_source: "V006 0005"
valid_until_source: "V007 0004"
entry_conditions:
  - "Sumi's practice date continues and requires Kazuya to replace ordinary conversation with responsive support."
active_goals:
  - help Sumi complete a safe and useful practice date
  - support Chizuru's acting opportunity despite fearing the loss of rental access
  - resolve the provisional Ruka relationship responsibly
  - answer Mami's intervention without leaving Chizuru to carry his responsibility
  - state his preference to Chizuru directly
known_propositions:
  - "Sumi can act under pressure and protects the public cover when Mami appears."
  - "Chizuru may leave rental work if acting opportunities expand."
  - "Mami researched Sumi and booked Chizuru to challenge the rental relation."
  - "Chizuru believes his earlier feeling for Mami deserved serious recognition."
relationship_conditions:
  - "Chizuru is a valued provider, collaborator, and the person Kazuya directly says he wants."
  - "Ruka remains a provisional girlfriend after an interrupted duty-based attempt at formalization."
  - "Mami is an active former partner who has investigated and challenged the rental system."
changed_from_previous:
  - PRACTICE_OUTCOME_CHANGE
  - VOCATIONAL_EXIT_RISK_CHANGE
  - FORMER_PARTNER_CONFRONTATION_CHANGE
  - DIRECT_PREFERENCE_DISCLOSURE
evidence_refs:
  - RAG-E-V006-001
  - RAG-E-V006-004
  - RAG-E-V006-006
  - RAG-E-V006-009
  - RAG-E-V006-010
  - RAG-E-V006-013
  - RAG-E-V006-015
  - RAG-E-V006-017
uncertainties:
  - "How Chizuru interprets or answers the direct preference statement."
  - "Whether Kazuya revisits or abandons the interrupted Ruka formalization."
  - "Whether acting work changes Chizuru's rental availability."
~~~

### KAZ-S009 — practical supporter under private access

~~~yaml
state_id: KAZ-S009
valid_from_source: "V007 0005"
valid_until_source: "V008 0004"
entry_conditions:
  - "Chizuru immediately asks Kazuya to classify his V006 preference statement."
active_goals:
  - preserve the relation after retreating into rental language
  - support Chizuru's acting effort through labor and bookings
  - protect her occupational privacy
  - become a supporter without requiring boyfriend status
known_propositions:
  - "Chizuru lost the next acting role but continues rehearsing and accepting bookings."
  - "Chizuru values his judgment that she has talent and worries about excessive spending."
  - "Sayuri interprets Chizuru's strength as armor around vulnerability."
  - "Chizuru has lost her key and seeks immediate help at his apartment."
relationship_conditions:
  - "Chizuru grants unpriced ordinary and family access but has not acknowledged romance."
  - "Sayuri knows Kazuya says he loves Chizuru."
  - "Ruka remains provisional and absent from V007."
changed_from_previous:
  - CLARIFICATION_RETREAT
  - PRACTICAL_CAREER_SUPPORT
  - PRIVACY_COST
  - UNPRICED_ACCESS_GAIN
  - LOVE_DISCLOSURE_TO_FAMILY_WITNESS
evidence_refs:
  - RAG-E-V007-001
  - RAG-E-V007-003
  - RAG-E-V007-005
  - RAG-E-V007-009
  - RAG-E-V007-012
  - RAG-E-V007-014
  - RAG-E-V007-015
  - RAG-E-V007-016
  - RAG-E-V007-017
uncertainties:
  - "How he handles the lost-key request and private-space pressure."
  - "Whether support remains non-entitled over time."
  - "Whether the interrupted Ruka formalization is revisited."
~~~

### KAZ-S010 — status-independent supporter under consent and planning tests

~~~yaml
state_id: KAZ-S010
valid_from_source: "V008 0005"
valid_until_source: "V009 0004"
entry_conditions:
  - "Chizuru's lost-key request creates immediate private-space access."
active_goals:
  - help Chizuru without exploiting practical dependence
  - support her family-linked acting dream independent of relationship label
  - manage the unresolved provisional relationship with Ruka
  - choose an appropriate birthday gift despite limited ordinary knowledge
known_propositions:
  - "Chizuru's grandparents raised her and her acting dream is tied to showing Sayuri success on screen."
  - "Chizuru classifies being beside someone as a service a rental girlfriend can provide."
  - "Ruka wants ordinary and sexual recognition that he does not reciprocate."
  - "Chizuru's profile lists an April 19 birthday, and Sumi knows at least one of her preferences."
relationship_conditions:
  - "Chizuru grants disclosure and temporary access but no romantic status."
  - "Ruka remains provisional after his refusal of sex and her morning kiss."
  - "Sumi is a paid provider actively helping with the gift search."
changed_from_previous:
  - LOST_KEY_HELP_AND_RESTRAINT
  - FAMILY_AND_VOCATIONAL_KNOWLEDGE_GAIN
  - DIRECT_SUPPORT_SPEECH
  - SEXUAL_REFUSAL_UNDER_STATUS_PRESSURE
  - BIRTHDAY_PLANNING
evidence_refs:
  - RAG-E-V008-001
  - RAG-E-V008-002
  - RAG-E-V008-004
  - RAG-E-V008-005
  - RAG-E-V008-006
  - RAG-E-V008-008
  - RAG-E-V008-012
  - RAG-E-V008-014
  - RAG-E-V008-015
  - RAG-E-V008-016
uncertainties:
  - "How Chizuru receives the eventual birthday gift."
  - "What consequence follows Ruka's overnight stay and kiss."
  - "Whether acting support remains sustainable and non-entitled."
~~~

### KAZ-S011 — practical giver and reckless identity protector under widening observation

~~~yaml
state_id: KAZ-S011
valid_from_source: "V009 0005"
valid_until_source: "V010 0004"
entry_conditions:
  - "The Sumi booking continues into an actionable gift choice and personal-information exchange."
active_goals:
  - give Chizuru useful support without imposing a heavy obligation
  - protect her campus and rental identities during an accidental audience collision
  - preserve accurate limits on the provisional Ruka relation
  - manage Mami's renewed access to the relationship system
known_propositions:
  - "Chizuru accepts the fatigue-oriented gift and believes that he and Ruka have not had sex."
  - "Chizuru observed his deliberate drinking, escorted him home, tended him, and later left medicine."
  - "Direct LINE access to Ichinose exists, but she objects to being added without permission."
  - "Mami heard Ruka claim current status and sex, received his correction, and then saw Chizuru on a rental date."
relationship_conditions:
  - "Chizuru provides substantial unpriced care while verbally limiting its meaning."
  - "Ruka remains provisional and nonreciprocal despite her public completed-status claim."
  - "Sumi has recorded his June 1 birthday after completing the paid gift consultation."
changed_from_previous:
  - BIRTHDAY_GIFT_COMPLETED
  - PARTIAL_RUKA_REASSURANCE_DELIVERED
  - CAMPUS_IDENTITY_COLLISION
  - RECKLESS_PROTECTIVE_DRINKING
  - UNPRICED_CARE_RECEIVED
  - DIRECT_LINE_ACCESS
  - PUBLIC_RUKA_CORRECTION
  - MAMI_OBSERVATION_ESCALATION
evidence_refs:
  - RAG-E-V009-001
  - RAG-E-V009-002
  - RAG-E-V009-003
  - RAG-E-V009-004
  - RAG-E-V009-005
  - RAG-E-V009-007
  - RAG-E-V009-008
  - RAG-E-V009-009
  - RAG-E-V009-010
  - RAG-E-V009-011
  - RAG-E-V009-013
  - RAG-E-V009-015
uncertainties:
  - "What action Mami takes after seeing Chizuru's rental date."
  - "Whether direct LINE access produces stable non-booking communication."
  - "How he repairs or resolves the widening gap between Ruka's claimed and agreed status."
~~~

### KAZ-S012 — paid dream-date client and vocational supporter under family crisis

~~~yaml
state_id: KAZ-S012
valid_from_source: "V010 0005"
valid_until_source: "V011 0002"
entry_conditions:
  - "Mami acts on the train sighting while Kazuya and Chizuru retain paid, neighbor, family, and direct-contact routes."
active_goals:
  - experience a missed-youth scenario through a bounded booking
  - support Chizuru's new stage opportunity
  - preserve Nagomi's girlfriend belief during the joint birthday
  - manage Ruka's renewed status escalation and Chizuru's hospital crisis
known_propositions:
  - "Chizuru takes pride in rental work and has another stage opportunity."
  - "Chizuru voluntarily attends the family party outside a booking after a hospital appointment."
  - "Ruka follows them, competes for family approval, and initiates another kiss."
  - "Chizuru chooses the direct LINE route to contact him from Sayuri's hospital setting."
relationship_conditions:
  - "Chizuru and Kazuya coordinate scripted intimacy professionally and vocational support sincerely without acknowledged private status."
  - "Ruka remains provisional and nonreciprocal despite family-space pressure."
  - "Nagomi still believes the public girlfriend account."
changed_from_previous:
  - UPGRADED_DREAM_DATE_BOOKED
  - SCRIPTED_INTIMACY_WITH_BOUNDARY
  - RENTAL_WORK_PRIDE_DISCLOSED
  - NEW_STAGE_SUPPORT_COMMITMENT
  - UNBOOKED_FAMILY_ATTENDANCE
  - RUKA_PARTY_KISS_RECEIVED
  - DIRECT_HOSPITAL_CONTACT
evidence_refs:
  - RAG-E-V010-004
  - RAG-E-V010-005
  - RAG-E-V010-007
  - RAG-E-V010-008
  - RAG-E-V010-009
  - RAG-E-V010-010
  - RAG-E-V010-011
  - RAG-E-V010-012
  - RAG-E-V010-014
  - RAG-E-V010-015
  - RAG-E-V010-016
  - RAG-E-V010-017
uncertainties:
  - "How he responds to Sayuri's hospitalization."
  - "Whether he converts stage support into durable practical action."
  - "Whether he directly addresses Ruka's kiss and the unresolved trial."
~~~

### KAZ-S013 — truth advocate under crisis, coercion, and inherited obligation

~~~yaml
state_id: KAZ-S013
valid_from_source: "V011 0003"
valid_until_source: "V012 0004"
entry_conditions:
  - "Chizuru's hospital call returns the unresolved family fiction, Ruka's kiss, and Sayuri's limited time to one active decision problem."
active_goals:
  - tell Nagomi and Sayuri that the relationship is false
  - respond to Sayuri's medical crisis without abandoning Chizuru
  - recognize responsibility for the unresolved Ruka trial without treating resistance as consent
  - determine what practical support remains possible
known_propositions:
  - "Ruka tells Chizuru about the kiss and continues kissing after his resistance."
  - "Chizuru does not want Sayuri told that the relation ended or was false."
  - "Nagomi has transferred the family ring, and Chizuru has placed it in his bag."
  - "Sumi can plan and execute substantial care even with limited spontaneous speech."
relationship_conditions:
  - "Kazuya and Chizuru cooperate in crisis but disagree about truth."
  - "Ruka remains nonreciprocal and continues unilateral physical escalation."
  - "Sumi's care can be received and evaluated without a private status claim."
changed_from_previous:
  - FAMILY_CONFESSION_ATTEMPTED
  - REPEATED_KISS_RESISTED
  - TRIAL_CAUSAL_RESPONSIBILITY_ACCEPTED
  - LIMITED_TIME_TRUTH_POSITION_STATED
  - FAMILY_RING_RECEIVED
  - SUMI_PRACTICAL_CARE_RECOGNIZED
evidence_refs:
  - RAG-E-V011-003
  - RAG-E-V011-004
  - RAG-E-V011-005
  - RAG-E-V011-007
  - RAG-E-V011-009
  - RAG-E-V011-010
  - RAG-E-V011-012
  - RAG-E-V011-015
  - RAG-E-V011-018
uncertainties:
  - "Whether he executes the disclosure against Chizuru's objection."
  - "How he separates guilt about the trial from responsibility for Ruka's conduct."
  - "Whether the ring or aquarium exchange changes his next action."
~~~

### KAZ-S014 — prospective producer under time-limited vocational commitment

~~~yaml
state_id: KAZ-S014
valid_from_source: "V012 0005"
valid_until_source: "V013 0004"
entry_conditions:
  - "Sumi's completed care itinerary and invitation to speak give Kazuya a bounded route for disclosing distress before a film-rental advertisement makes an actionable association available."
active_goals:
  - make a film starring Chizuru for Sayuri
  - turn preliminary crowdfunding research into an executable production route
  - protect Sayuri's remaining time from an abandoned or purely symbolic effort
  - preserve responsibility for unresolved truth, ring, and Ruka routes without inventing a V012 resolution
known_propositions:
  - "Sumi can receive a partial account of the crisis and provide support that reduces his distress."
  - "Chizuru's screen goal remains urgent under repeated rejection and Sayuri's declining condition."
  - "Crowdfunding may finance a modest independent film, but personnel, editing, schedule, and exhibition remain unresolved."
  - "Chizuru wants the film if Kazuya will not quit midway."
relationship_conditions:
  - "Kazuya and Sumi now share a consequential confidant exchange, but he did not hear her love confession."
  - "Kazuya and Chizuru become voluntary film collaborators without a romantic reclassification."
  - "The family-deception dispute, ring custody, Ruka trial, and Mami route remain dormant rather than resolved."
changed_from_previous:
  - SUMI_SUPPORT_RECEIVED
  - PARTIAL_CRISIS_DISCLOSURE_COMPLETED
  - FILM_ROUTE_RESEARCHED
  - CROWDFUNDING_PROPOSAL_PRESENTED
  - CHIZURU_PROJECT_REQUEST_RECEIVED
  - COMPLETION_COMMITMENT_ACCEPTED
evidence_refs:
  - RAG-E-V012-004
  - RAG-E-V012-005
  - RAG-E-V012-006
  - RAG-E-V012-007
  - RAG-E-V012-016
  - RAG-E-V012-017
  - RAG-E-V012-018
  - RAG-E-V012-019
  - RAG-E-V012-020
  - RAG-E-V012-021
  - RAG-E-V012-022
uncertainties:
  - "Whether research becomes a launched and funded campaign."
  - "Whether he can recruit production competence and sustain execution."
  - "How the project interacts with the dormant truth, ring, and Ruka obligations."
~~~

### KAZ-S015 — named producer with a live unfunded campaign

~~~yaml
state_id: KAZ-S015
valid_from_source: "V013 0005"
valid_until_source: "V014 0004"
entry_conditions:
  - "Kazuya and Chizuru have promised the film but lack an approved campaign, budget, team, and production route."
active_goals:
  - launch and fund the 1.82-million-yen campaign within forty-five days
  - obtain missing script and production competence
  - coordinate Chizuru and Mini without converting project access into romantic entitlement
known_propositions:
  - "CAMPFIRE rejected the first draft and later approved the revision."
  - "Chizuru's manager and Sayuri permit the campaign's controlled identity disclosure."
  - "Chizuru identifies him as producer and Mini has offered labor."
  - "The campaign begins at zero yen and zero supporters."
relationship_conditions:
  - "Chizuru is an active project principal who shares work, cost decisions, private space, and a public outcome test."
  - "Mini is an informed volunteer whose romantic interpretation is not authoritative."
  - "Sayuri endorses the project and Kazuya's suitability while lacking the rental truth."
changed_from_previous:
  - EXPERT_CORRECTION_RECEIVED
  - PROJECT_BUDGET_FIXED
  - CHIZURU_COLLABORATION_DEEPENED
  - MINI_RECRUITED
  - PRODUCER_ROLE_NAMED
  - CAMPAIGN_APPROVED_AND_PUBLISHED
evidence_refs:
  - RAG-E-V013-001
  - RAG-E-V013-002
  - RAG-E-V013-005
  - RAG-E-V013-007
  - RAG-E-V013-008
  - RAG-E-V013-009
  - RAG-E-V013-010
  - RAG-E-V013-014
  - RAG-E-V013-015
  - RAG-E-V013-020
  - RAG-E-V013-021
  - RAG-E-V013-022
uncertainties:
  - "Whether public support arrives and reaches the target."
  - "Whether Mini completes useful work and further specialists join."
  - "Whether Kazuya can move from campaign preparation to production management."
~~~

### KAZ-S016 — cross-functional producer under funding stall

~~~yaml
state_id: KAZ-S016
valid_from_source: "V014 0005"
valid_until_source: "V015 0122"
entry_conditions:
  - "The live campaign begins attracting support while script, director, remaining finance, and production execution are unresolved."
active_goals:
  - reach the 1.82-million-yen all-or-nothing target
  - secure source permission, director, crew, and preproduction capacity
  - sustain public outreach despite rejection and limited personal funds
known_propositions:
  - "Early campaign support is real but later stalls below target with roughly two weeks left."
  - "Chizuru approves the selected source, and adaptation permission and Tabuse's direction are secured."
  - "Mini has campaign experience and has converted analytics into a distributed recovery plan."
  - "Ruka is willing to perform public labor for the film despite rivalry."
relationship_conditions:
  - "Chizuru remains an active project principal and has not romantically reclassified him."
  - "Mini is both a useful strategist and an unauthorized interpreter of his preference."
  - "Ruka's support coexists with an unresolved provisional relation and consent history."
changed_from_previous:
  - INITIAL_BACKING_RECEIVED
  - SOURCE_SELECTED_AND_PERMISSIONED
  - DIRECTOR_AND_CREW_ROUTE_SECURED
  - CAMPAIGN_STALL_DIAGNOSED
  - TEAM_STRATEGY_ACCEPTED
  - PUBLIC_FLYER_LABOR_PERFORMED
evidence_refs:
  - RAG-E-V014-002
  - RAG-E-V014-003
  - RAG-E-V014-007
  - RAG-E-V014-008
  - RAG-E-V014-009
  - RAG-E-V014-010
  - RAG-E-V014-011
  - RAG-E-V014-012
  - RAG-E-V014-013
  - RAG-E-V014-014
  - RAG-E-V014-015
uncertainties:
  - "Whether the revised tactics close the funding gap."
  - "Whether specialist agreements become an executable screenplay, schedule, and shoot."
  - "How Chizuru responds after Mini discloses Kazuya's preference."
~~~

### KAZ-S017 — operational producer under specialist authority and future-distance anxiety

~~~yaml
state_id: KAZ-S017
valid_from_source: "V015 0123"
valid_until_source: "V016 0004"
entry_conditions:
  - "The campaign crosses its all-or-nothing target, usable funds transfer, and principal photography becomes active under Tabuse."
active_goals:
  - carry the funded film through production for Chizuru and Sayuri
  - perform useful producer work despite limited specialist expertise
  - support Chizuru's acting without claiming personal status from the project
known_propositions:
  - "Gross campaign support is 1,850,000 yen and the transfer after fees is 1,535,500 yen."
  - "Tabuse directs a functioning cast and crew, while Kazuya's producer work includes logistics and bottleneck removal."
  - "Mini disclosed his preference to Chizuru, but Chizuru has given him no direct answer."
relationship_conditions:
  - "Chizuru enforces on-set concentration distance while accepting him as producer."
  - "Ruka has repeated project-first labor without ending the provisional relation."
  - "Kazuya imagines Chizuru's future fame and remains uncertain about his place in it."
changed_from_previous:
  - CAMPAIGN_TARGET_REACHED
  - USABLE_FUNDS_TRANSFERRED
  - PRINCIPAL_PHOTOGRAPHY_ACTIVE
  - PRODUCER_ROLE_OPERATIONALIZED
  - SPECIALIST_AUTHORITY_ACCEPTED
  - UNSAFE_BOTTLENECK_RESPONSE_PERFORMED
  - FUTURE_DISTANCE_ANXIETY_EXPLICIT
evidence_refs:
  - RAG-E-V015-002
  - RAG-E-V015-009
  - RAG-E-V015-010
  - RAG-E-V015-011
  - RAG-E-V015-012
  - RAG-E-V015-013
  - RAG-E-V015-014
  - RAG-E-V015-015
  - RAG-E-V015-016
  - RAG-E-V015-017
uncertainties:
  - "Whether principal photography, editing, exhibition, and delivery are completed."
  - "Whether unsafe effort produces correction or becomes a repeated production method."
  - "How he responds if future career access and personal access diverge."
~~~

### KAZ-S018 — post-shoot producer under value recognition and consent pressure

~~~yaml
state_id: KAZ-S018
valid_from_source: "V016 0005"
valid_until_source: "V017 0004"
entry_conditions:
  - "Principal photography is nearing its final scene while Kazuya treats Chizuru's acting success as evidence of status distance."
active_goals:
  - complete editing, exhibition planning, and delivery of the film for Chizuru and Sayuri
  - remain useful without converting project labor into romantic entitlement
  - move family relationships toward truth and handle Ruka's trial and bodily requests responsibly
known_propositions:
  - "Chizuru rejects his different-world inference, calls his life wonderful, and says she has never regretted meeting him."
  - "The final take is complete; footage is in editing with a September target, and a theater is being sought."
  - "Chizuru made the film for the promise involving Katsuhito and Sayuri and directly thanks him for proposing it."
  - "Ruka did not authorize Mini's false absence story and has asked Kazuya for bodily touch on her birthday."
relationship_conditions:
  - "Chizuru permits bounded ordinary and spatial access during the final trip but gives no mutual romantic classification."
  - "Kazuya states a true-love standard and his post-film loneliness, yet his shouted preference has no proved reception."
  - "The unresolved Ruka trial has returned as direct status conflict and an unanswered consent threshold."
changed_from_previous:
  - SELF_DEMOTION_DIRECTLY_CORRECTED
  - FINAL_LOCATION_WORK_COMPLETED
  - FAMILY_PURPOSE_AND_GRATITUDE_RECEIVED
  - PRINCIPAL_PHOTOGRAPHY_COMPLETED
  - POSTPRODUCTION_HANDOFF_INITIATED
  - POST_FILM_DISTANCE_NAMED
  - BODILY_CONTACT_REQUEST_RECEIVED
evidence_refs:
  - RAG-E-V016-001
  - RAG-E-V016-002
  - RAG-E-V016-003
  - RAG-E-V016-007
  - RAG-E-V016-008
  - RAG-E-V016-009
  - RAG-E-V016-010
  - RAG-E-V016-011
  - RAG-E-V016-012
  - RAG-E-V016-013
  - RAG-E-V016-015
  - RAG-E-V016-016
  - RAG-E-V016-017
  - RAG-E-V016-018
uncertainties:
  - "Whether the edit, screening, and delivery to Sayuri are completed."
  - "Whether Chizuru hears or later responds to his preference."
  - "How he answers Ruka's explicit request and whether he resolves the trial fairly."
~~~

### KAZ-S019 — boundary-setting supporter under terminal family crisis

~~~yaml
state_id: KAZ-S019
valid_from_source: "V017 0005"
valid_until_source: "V018 0004"
entry_conditions:
  - "Ruka's birthday request requires an answer while film postproduction and Sayuri delivery remain incomplete."
active_goals:
  - answer Ruka's requests without converting trial status into blanket consent
  - finish and deliver the film through a concrete accessible screening route
  - support Chizuru and Sayuri without requiring romantic status or uninvited bodily access
  - identify a feasible final action under Sayuri's critical prognosis
known_propositions:
  - "Ruka accepts sunscreen scope, later receives first-name permission, and continues to assert girlfriend status."
  - "A 200-seat wheelchair-accessible cinema is available for September 30, but the edit and screening are incomplete."
  - "Sayuri credits him with making the film route possible and then collapses after visiting the cinema."
  - "The physician says recovery is difficult and the night may be critical."
  - "Chizuru defends a happy final belief and says she hates sad truths while showing visible strain."
relationship_conditions:
  - "He tells Sayuri that he wants to support Chizuru even if they are no longer lovers."
  - "He blocks Ruka's hug after accepting sunscreen and separately permits first-name address."
  - "He imagines embracing Chizuru but does not touch her, then asks her to prioritize her own feelings."
changed_from_previous:
  - RUKA_REQUESTS_ANSWERED_BY_SCOPE
  - ACCESSIBLE_SCREENING_VENUE_ARRANGED
  - STATUS_INDEPENDENT_SUPPORT_DECLARED
  - SAYURI_COLLAPSE_AND_CRITICAL_PROGNOSIS_RECEIVED
  - UNINVITED_CRISIS_TOUCH_WITHHELD
  - TRUTH_CONFLICT_REOPENED
  - LINE_AND_RUNNING_ACTION_INITIATED
evidence_refs:
  - RAG-E-V017-001
  - RAG-E-V017-004
  - RAG-E-V017-005
  - RAG-E-V017-008
  - RAG-E-V017-009
  - RAG-E-V017-010
  - RAG-E-V017-014
  - RAG-E-V017-015
  - RAG-E-V017-016
  - RAG-E-V017-017
  - RAG-E-V017-018
uncertainties:
  - "Whether his final action delivers the film or changes Sayuri's condition or access."
  - "Whether the rental-and-family truth is disclosed."
  - "Whether Chizuru accepts comfort, access, or a changed support role."
  - "Whether he fairly resolves the Ruka trial."
~~~

### KAZ-S020 — bereavement-support planner after adaptive delivery

~~~yaml
state_id: KAZ-S020
valid_from_source: "V018 0005"
valid_until_source: null
entry_conditions:
  - "Sayuri is critically ill, the film is unfinished, Chizuru has entered her room, and Kazuya has begun an unidentified coordination action."
active_goals:
  - deliver available film material before Sayuri dies
  - help Chizuru speak and grieve without claiming family or lover authority
  - learn a support method that Chizuru may accept
  - fund and schedule an answerable professional-access date
known_propositions:
  - "Unfinished footage can be projected at Sayuri's bedside and receives her praise."
  - "Chizuru attempts the non-dating correction, Sayuri entrusts the answer to her, and Sayuri dies after reciprocal love."
  - "Chizuru says she is fine and does not accept his immediate help, while Sumi rejects the claim that a strong person can live alone."
  - "Sumi models play and direct encouragement; Ruka gives bounded advice; the karaoke manager grants a wage advance."
relationship_conditions:
  - "He identifies himself as neighbor and outsider, urges Chizuru to speak as herself, and does not enter the final family embrace."
  - "He accepts Chizuru's immediate refusal, then seeks Sumi's help instead of forcing access."
  - "He submits a rental request rather than presuming informal lover privileges."
changed_from_previous:
  - LINE_ACTION_COMPLETED_AS_BEDSIDE_PROJECTION
  - PARTIAL_TRUTH_DISCLOSURE_OBSERVED
  - SAYURI_DEATH_RECEIVED
  - SOLITARY_STRENGTH_APPRAISAL_CORRECTED
  - IMMEDIATE_HELP_REFUSAL_RESPECTED
  - SUMI_SUPPORT_METHOD_LEARNED
  - WAGE_ADVANCE_OBTAINED
  - FUNDED_RENTAL_SUPPORT_PLAN_SUBMITTED
evidence_refs:
  - RAG-E-V018-001
  - RAG-E-V018-003
  - RAG-E-V018-005
  - RAG-E-V018-006
  - RAG-E-V018-007
  - RAG-E-V018-008
  - RAG-E-V018-009
  - RAG-E-V018-010
  - RAG-E-V018-011
  - RAG-E-V018-012
  - RAG-E-V018-013
  - RAG-E-V018-014
  - RAG-E-V018-015
  - RAG-E-V018-016
  - RAG-E-V018-017
  - RAG-E-V018-018
  - RAG-E-V018-019
  - RAG-E-V018-020
uncertainties:
  - "Whether Chizuru accepts the booking and what date boundaries she sets."
  - "Whether the planned enjoyment and encouragement help or burden her."
  - "Whether she shows grief directly before him."
  - "Whether he resolves the Ruka trial fairly or completes public film exhibition."
~~~

## Behavioral rules

### RAG-KAZ-R001 — immediate face protection can outrun long-term planning

- **Scope:** KAZ-S001 through KAZ-S014.
- **Trigger:** Sudden rejection, accusation, or an audience before whom Kazuya expects humiliation or another person's disappointment.
- **Relationship conditions:** Strongest with family, a desired woman, or peers evaluating his romantic worth.
- **Likely appraisal:** “I must stop this exposure now,” often followed by a global negative judgment about himself or others.
- **Likely action range:** blurt a face-saving claim; redirect responsibility; plead for an exception; defer correction; later apologize when the cost is explicit.
- **Inhibitors/escalators:** time to reflect and concrete recognition of harm can inhibit; surprise, beauty/status attention, and family disappointment escalate.
- **Written-speech constraints:** stammering, self-interruption, exaggerated certainty, then plain apology.
- **Alternatives:** completed confession is possible when disappointment becomes visible, but V001 shows interruption before completion.
- **Support:** RAG-E-V001-002, RAG-E-V001-003, RAG-E-V001-006, RAG-E-V001-008, RAG-E-V001-011, RAG-E-V002-005, RAG-E-V002-008, RAG-E-V002-012, RAG-E-V003-006, RAG-E-V003-014, RAG-E-V004-003, RAG-E-V004-005, RAG-E-V004-011, RAG-E-V005-003, RAG-E-V005-013, RAG-E-V006-009, RAG-E-V006-012, RAG-E-V008-003, RAG-E-V009-005, RAG-E-V009-010, RAG-E-V009-012, RAG-E-V009-013.
- **Counterevidence/gap:** he makes a costly partial public correction and plans fuller disclosure, so avoidance is neither total nor immutable.
- **Disconfirming observation:** repeated comparable pressures followed by timely truthful disclosure without another person forcing the correction.
- **Class/confidence:** STRONG_INFERENCE; moderate within V001 crisis contexts.

### RAG-KAZ-R002 — romantic attention receives alternating inflation and displacement

- **Scope:** KAZ-S001, KAZ-S003, KAZ-S005 through KAZ-S014.
- **Trigger:** Attention or physical proximity from an attractive woman, especially Mami or Chizuru.
- **Likely appraisal:** rapid possibility-building, sexual fantasy, or status elevation; after threat, the same evidence may be dismissed as impossible or purchased.
- **Likely action range:** stare, fantasize, become visibly flustered, seek proximity, or interpret ambiguous attention hopefully.
- **Inhibitors/escalators:** explicit service rules and shame inhibit action; loneliness, peer gaze, and former-partner familiarity escalate.
- **Negative constraint:** arousal should not be reconstructed as proof that he ignores every explicit refusal; V001 shows both pressure and moments of retreat/apology.
- **Support:** RAG-E-V001-001, RAG-E-V001-010, RAG-E-V001-012, RAG-E-V001-015, RAG-E-V002-005, RAG-E-V002-006, RAG-E-V002-009, RAG-E-V002-010, RAG-E-V003-005, RAG-E-V003-012, RAG-E-V004-011, RAG-E-V004-014, RAG-E-V005-013, RAG-E-V005-015, RAG-E-V006-006, RAG-E-V006-016, RAG-E-V006-017, RAG-E-V008-002, RAG-E-V008-012.
- **Counterevidence/gap:** he refuses the Pocky kiss and acts for Chizuru under emergency; little low-stakes interaction with women exists outside romantic framing.
- **Disconfirming observation:** stable, proportionate interpretation of comparable ambiguous attention across several contexts.
- **Class/confidence:** WORKING_HYPOTHESIS; moderate-low outside the observed relationships.

### RAG-KAZ-R003 — visible family pain can activate repair, but rescue can supersede it

- **Scope:** KAZ-S002 through KAZ-S008.
- **Trigger:** Concrete evidence that the girlfriend fiction disappoints or harms Nagomi.
- **Likely appraisal:** the lie has become morally costly and must be confessed.
- **Likely action range:** move from delay toward direct disclosure; accept a face-saving intervention if it arrives before the confession completes.
- **Motives in conflict:** honesty and responsibility versus preserving family happiness and avoiding shame.
- **Support:** RAG-E-V001-003, RAG-E-V001-004, RAG-E-V001-006, RAG-E-V001-008, RAG-E-V002-011, RAG-E-V002-012, RAG-E-V002-015, RAG-E-V002-016, RAG-E-V003-006, RAG-E-V003-007, RAG-E-V003-015, RAG-E-V004-005, RAG-E-V004-017, RAG-E-V005-003, RAG-E-V005-006, RAG-E-V006-009, RAG-E-V006-013, RAG-E-V006-015, RAG-E-V006-017.
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

- **Scope:** KAZ-S001 through KAZ-S014.
- **Trigger:** Conflict in which someone exposes his conduct or offers positive regard inconsistent with his low self-image.
- **Likely appraisal:** “This happened because I am pathetic,” or “their care cannot be personally meaningful.”
- **Likely action range:** apologize, accept punishment, express gratitude, then preserve the same underlying pressure cycle; explain favorable conduct as pity or payment.
- **Support:** RAG-E-V001-002, RAG-E-V001-004, RAG-E-V001-014, RAG-E-V002-006, RAG-E-V002-013, RAG-E-V002-017, RAG-E-V003-003, RAG-E-V003-005, RAG-E-V003-015, RAG-E-V004-011, RAG-E-V004-013, RAG-E-V004-014, RAG-E-V005-011, RAG-E-V005-013, RAG-E-V006-006, RAG-E-V006-009, RAG-E-V006-015, RAG-E-V006-016.
- **Counterevidence/gap:** his conservative reading of paid conduct may sometimes be accurate; V003 adds conscious feeling without sustained follow-through.
- **Disconfirming observation:** calibrated acceptance of positive and negative evidence followed by sustained behavioral change.
- **Class/confidence:** WORKING_HYPOTHESIS; moderate.

### RAG-KAZ-R006 — acute threat can compress rumination into direct protective action

- **Scope:** KAZ-S004 through KAZ-S007.
- **Trigger:** Concrete evidence that Chizuru is in immediate physical danger and delay may be fatal.
- **Likely appraisal:** the missing passenger is Chizuru and action cannot wait for certainty or social permission.
- **Likely action range:** infer rapidly from available evidence and accept personal risk before narrating a complete motive.
- **Inhibitors/escalators:** acute time pressure escalates action; no comparable non-romantic emergency is available.
- **Support:** RAG-E-V002-017, RAG-E-V003-001, RAG-E-V003-015.
- **Counterevidence/gap:** the Ruka catch extends the pattern beyond Chizuru, but both cases concern attractive women inside relationship crises; broad generality remains unknown.
- **Disconfirming observation:** repeated comparable immediate danger to a valued person followed by self-protective delay despite feasible action.
- **Class/confidence:** WORKING_HYPOTHESIS; low and emergency-specific.

### RAG-KAZ-R007 — personalized reciprocity can mobilize practical effort

- **Scope:** KAZ-S006 through KAZ-S014.
- **Trigger:** A valued person gives Kazuya an unpriced, personalized object that he cannot reduce to a standard booking.
- **Likely appraisal:** he has received singular attention and should return it materially.
- **Likely action range:** cry, preserve and inspect the object, seek income, choose a return gift, and arrange delivery.
- **Inhibitors/escalators:** service ambiguity complicates interpretation; concrete financial limits redirect fantasy into work.
- **Support:** RAG-E-V004-014, RAG-E-V004-015, RAG-E-V004-016, RAG-E-V005-008, RAG-E-V005-009.
- **Counterevidence/gap:** one gift cycle; V005 confirms downstream job consequence but not long-term stability.
- **Disconfirming observation:** repeated comparable personalized care followed only by fantasy or entitlement and no feasible reciprocal effort.
- **Class/confidence:** WORKING_HYPOTHESIS; low and gift-specific.

### RAG-KAZ-R008 — concrete guilt can become planned reparative disclosure

- **Scope:** KAZ-S007.
- **Trigger:** Kazuya sees that a friend has been materially hurt by the same deception system he maintains.
- **Likely appraisal:** apology alone is insufficient; he must supply context while sharing the humiliation himself.
- **Likely action range:** earn or allocate money, arrange a controlled encounter, disclose his own comparable secret, and accept anger.
- **Inhibitors/escalators:** direct evidence of the friend's hurt escalates action; exposure risk and shame inhibit broader disclosure.
- **Support:** RAG-E-V005-008, RAG-E-V005-009, RAG-E-V005-011.
- **Counterevidence/gap:** one friendship repair; he still withholds the truth from family, Kibe, and most peers.
- **Disconfirming observation:** repeated comparable injury followed by apology theater without feasible material repair or self-exposure.
- **Class/confidence:** WORKING_HYPOTHESIS; low and friendship-specific.

### RAG-KAZ-R009 — relationship labels do not override observed consent limits

- **Scope:** KAZ-S007 through KAZ-S014.
- **Trigger:** A partner or provider creates sexualized proximity while the governing relationship remains asymmetric or transactional.
- **Likely appraisal:** attraction and affection do not require acting on the opportunity.
- **Likely action range:** retreat, avert gaze, ask for physical separation, or refuse sex.
- **Support:** RAG-E-V005-001, RAG-E-V006-002, RAG-E-V008-002, RAG-E-V008-012, RAG-E-V008-013.
- **Counterevidence/gap:** the contexts are narrow, and earlier pursuit and privacy violations prevent a global mature-boundary claim.
- **Disconfirming observation:** repeated comparable explicit pressure followed by participation because a label or private setting is treated as sufficient consent.
- **Class/confidence:** WORKING_HYPOTHESIS; moderate within the observed refusal contexts.

### RAG-KAZ-R010 — shareable distress plus a concrete route can convert helplessness into organized support

- **Scope:** KAZ-S014.
- **Trigger:** Kazuya receives nonjudgmental emotional support while facing a valued person's time-limited goal, then encounters a feasible external mechanism.
- **Likely appraisal:** feeling unable to help is not the same as having no available action; uncertainty should be reduced through research and proposal.
- **Likely action range:** disclose enough distress to become less dysregulated, investigate costs and timing, present an actionable route, accept scrutiny, and commit to sustained work without demanding relationship status.
- **Inhibitors/escalators:** lack of a concrete mechanism inhibits action; visible deadline, personalized support, and Chizuru's explicit request escalate commitment.
- **Support:** RAG-E-V012-004 through RAG-E-V012-007, RAG-E-V012-016 through RAG-E-V012-022.
- **Counterevidence/gap:** V013-V016 supply campaign launch, funding, specialist recruitment, completed principal photography, and postproduction handoff, but no finished film or general competence proof.
- **Disconfirming observation:** the plan remains rhetorical or is abandoned once execution requires ordinary coordination and sustained labor.
- **Class/confidence:** WORKING_HYPOTHESIS; low and project-specific.

### RAG-KAZ-R011 — concrete criticism can elicit revision when a valued external goal is measurable

- **Scope:** KAZ-S015.
- **Trigger:** An expert rejects an inadequate plan whose failure would harm a time-limited goal.
- **Likely appraisal:** personal inexperience is a problem to research and revise rather than proof that action is impossible.
- **Likely action range:** solicit criticism, endure discouragement, return to joint planning, quantify costs, recruit help, revise the campaign, and publish once approved.
- **Inhibitors/escalators:** global self-condemnation inhibits action; Chizuru's explicit reliance, a public deadline, and concrete reviewer demands escalate revision.
- **Support:** RAG-E-V013-001 through RAG-E-V013-010, RAG-E-V013-014, RAG-E-V013-015, RAG-E-V013-020 through RAG-E-V013-022.
- **Counterevidence/gap:** V015-V016 supply funding, staffing, completed shooting, editing handoff, and theater search; safe judgment, finished postproduction, and delivery remain unproved.
- **Disconfirming observation:** comparable external correction produces abandonment or unchanged resubmission rather than revision.
- **Class/confidence:** WORKING_HYPOTHESIS; low and project-specific.

### RAG-KAZ-R012 — a measurable external goal can sustain effort across rejection and distribute responsibility

- **Scope:** KAZ-S016.
- **Trigger:** A valued project has a public deficit that cannot be solved by private feeling or one person's cash.
- **Likely appraisal:** failure remains personally painful, but the next useful act is to find missing expertise, accept diagnostic correction, and keep performing concrete tasks.
- **Likely action range:** search large candidate sets, approach rights holders and specialists repeatedly, share analytics with a team, spend bounded personal money, and tolerate public rejection.
- **Inhibitors/escalators:** self-blame and weak finances inhibit judgment; Chizuru's participation, visible metrics, specialist response, and assigned tasks escalate persistence.
- **Support:** RAG-E-V014-007 through RAG-E-V014-015.
- **Counterevidence/gap:** one time-limited project; completion, sustainable budgeting, and general management competence remain unobserved.
- **Disconfirming observation:** comparable measurable failure produces solitary panic or abandonment despite available collaborative correction.
- **Class/confidence:** WORKING_HYPOTHESIS; low and project-specific.

### RAG-KAZ-R013 — concrete production responsibility can elicit subordinate labor and unsafe bottleneck removal

- **Scope:** KAZ-S017.
- **Trigger:** A time-sensitive production obstacle threatens a shared deliverable and specialist staff identify ordinary tasks or an immediate bottleneck.
- **Likely appraisal:** usefulness matters more than title prestige, and delay could cost Chizuru and Sayuri the scene.
- **Likely action range:** accept errands, setup, carrying, and direction; maintain performer distance; intervene physically when time or continuity appears endangered.
- **Inhibitors/escalators:** explicit specialist guidance can channel effort; countdown pressure, visible crew dependence, and personal attachment escalate self-risk.
- **Support:** RAG-E-V015-011 through RAG-E-V015-015.
- **Counterevidence/gap:** one shoot sequence; the bridge climb nearly causes injury and does not prove repeatable production judgment.
- **Disconfirming observation:** comparable production pressure produces status-seeking, refusal of ordinary work, or avoidable paralysis despite clear feasible tasks.
- **Class/confidence:** WORKING_HYPOTHESIS; low and production-specific.

### RAG-KAZ-R014 — visible concealed regret plus a concrete route can shift status fantasy into noncontact challenge, updating, and logistical action

- **Scope:** KAZ-S019 through KAZ-S020.
- **Trigger:** Chizuru's controlled crisis statement conflicts with visible strain while time is critically limited and a practical route may remain.
- **Likely appraisal:** imagined boyfriend privileges are unavailable and unnecessary; useful support requires asking what she wants and acting on a feasible task.
- **Likely action range:** withhold uninvited touch, challenge a total no-regret account, separate support from formal status, improvise technical delivery, accept an immediate refusal, seek advice, and fund an answerable service route.
- **Inhibitors/escalators:** uncertainty about Chizuru's wishes inhibits physical comfort; critical prognosis, unfinished film delivery, and visible regret escalate action.
- **Support:** RAG-E-V017-010, RAG-E-V017-015 through RAG-E-V017-018; RAG-E-V018-001, RAG-E-V018-009 through RAG-E-V018-020.
- **Counterevidence/gap:** one linked acute crisis and planning sequence; he initially misreads strength as possible self-sufficiency, and the date plan's acceptance and result remain unknown.
- **Disconfirming observation:** comparable visible crisis with a concrete feasible route produces only status rumination or uninvited intimacy without practical action.
- **Class/confidence:** WORKING_HYPOTHESIS; low and crisis-specific.

## Directed relationship conditioning

### Toward Chizuru

Kazuya knows she is a paid provider and actor whose family-linked dream is to show Sayuri her success on screen. Her casting loss elicits wages-and-bookings support, and V011 makes their ethical difference explicit: he argues that limited time requires truth while she chooses Sayuri's comforting belief. V012-V015 move support into an agreed, funded film project and operational producer role. V016 gives him direct correction of his status self-demotion, Chizuru's family-purpose disclosure and thanks, final-scene camera responsibility, and postproduction follow-through. V017 has him arrange accessible cinema access, tell Sayuri that support survives the lover label, recognize Chizuru's concealed strain, withhold imagined boyfriend touch, and initiate a practical response. V018 completes that response through bedside projection, then shows him respect her immediate refusal, seek Sumi's method, and submit a paid support booking. This establishes consequential collaboration and updating, not reciprocated romance or a shared disclosure plan.

### Toward Mami

Mami has unusual power to reactivate hope and self-comparison because she is his first former partner and the object of unresolved fantasy. V006 shows her researching Sumi and booking Chizuru; Kazuya overhears her accusation and accepts responsibility for the deception. Chizuru's confrontation helps him separate his past attachment to Mami from his present preference, but Mami's next response remains unknown.

### Toward Nagomi

Nagomi's happiness is a protected value and a source of shame. Kazuya wants to meet her expectations and fears making her feel foolish or disappointed. This increases both deception and the possibility of repair when pain becomes visible.

### Toward male friends

Peer evaluation intensifies status anxiety and sexual display, but the friends' disrespect toward Chizuru can elicit direct opposition. His behavior should not be modeled as uniform submission to peer pressure.

### Toward Ruka

Ruka is his provisional girlfriend, knows the rental truth, sincerely loves him by her own account, and understands that he is attached to Chizuru. Kazuya does not reciprocate her feeling. V008 shows him accepting ordinary-date activity and storm lodging while refusing sex; Ruka then initiates a morning kiss. Predict guilt, urgency, attraction, and inconsistent boundary management under her demands, while preserving the evidenced capacity for direct refusal. Do not infer intimacy consent or mutual love from the label, lodging, or kiss.
V009 adds public correction: when Ruka tells Mami that the relation is current and sexual, Kazuya identifies it as provisional and denies sex. This supports factual resistance under explicit overstatement without showing that he can end or fairly resolve the trial.
V010 adds another unilateral kiss in a family setting. V011 adds repeated kissing through objection and recoil, followed by Kazuya's recognition that sustaining the trial helped create the situation. V017 shows improved differentiation: he accepts sunscreen, blocks a hug, and separately permits first-name address. Preserve all facts: he remains responsible for leaving the asymmetric relation unresolved, Ruka remains responsible for unilateral contact and status overstatement, and a narrow permission must stay narrow.

## Domain account and negative constraints

- **Core self-model:** globally unattractive, inexperienced, and prone to interpreting bad outcomes as confirmation of inadequacy. This self-model is represented, not accepted as objective truth.
- **Motivational architecture:** immediate relief and romantic validation compete with family loyalty, fairness, and a wish to become more responsible. Immediate relief often wins before reflection; repair motives become stronger after harm is concrete.
- **Emotional regulation:** fantasy, rumination, masturbation reference, comic panic, self-attack, and avoidance are observed. Recovery is often externally prompted.
- **Agency and competence:** capable of booking, negotiating, apologizing, public defense, gift selection, routine paid work, first-wage allocation, controlled disclosure, adapting to a practice-client role, and giving low-pressure practical protection. Long-term planning and generalized honesty remain weakly evidenced.
- **Project competence:** can launch and revise a campaign, recruit specialists, coordinate production, complete camera work, hand footage to editing, arrange a dated accessible venue, and improvise private projection of unfinished footage. Finished editing and public exhibition remain untested.
- **Ordinary repertoire:** insufficient. Do not fabricate hobbies, tastes, study habits, or financial discipline beyond the shown savings, apartment life, bouldering date, travel contexts, and initial karaoke employment.
- **Contradiction:** his self-description as powerless coexists with socially consequential initiative; his moral concern coexists with harassment and pressure.
- **Thresholds:** visible harm to a loved person or disrespect toward Chizuru can shift him from avoidance to action. Whether that action is truthful remains context-dependent.

## Written-speech profile

Use Japanese manga speech only. Under low control, expect fragments, repeated questions, abrupt exclamations, and self-correction. With Chizuru after confrontation, apologies can be short and plain. Before family and peers, he may overstate certainty to stabilize a story. When morally indignant, his speech becomes more direct and less self-focused. Do not represent him as stammering in every line or as uniformly crude; V001 contains candid thanks and attempted confession as well as sexual thought.

## Counterfactual envelope and abstention

Supported with caution: a sudden family question; a peer insulting Chizuru; Mami challenging the rental system; Chizuru restating a known boundary; Ruka claiming priority; an opportunity for bounded friend repair; a shy provider needing a cooperative client; emotional support offered through a constrained communication style; a concrete film task requiring research or coordination.

Require extra assumptions: successful long-term production management, mature reciprocal sexual negotiation, mutual romantic classification, Mami's later use of the family account, resolution of the Ruka status, acceptance or success of the planned rental date, finished public exhibition, or any post-V018 knowledge.

Abstain when the outcome depends on Chizuru's hidden feeling, Mami's hidden goal, or a later developmental state. Generated scenarios may test rule clarity but cannot validate the model as canon evidence.

## Validation status

V018 validates that Kazuya can finish the prior action through improvised bedside projection, use outsider framing without entering Chizuru's final family exchange, and revise his support approach after Sumi challenges solitary-strength reasoning. He respects Chizuru's immediate refusal, then uses consultation, earned resources, itinerary work, and a rental request to create a bounded care plan. The model still withholds mature partnership, generalized disclosure, finished public exhibition, date acceptance or success, fair resolution of the Ruka trial, and Mami's later use of the family account.

The V010 local reconstruction audit assigns `OPERATIONAL_CANDIDATE` only within named family-pressure, support, embarrassment, repair, and consent-boundary domains. It assigns no global capability grade and no whole-person validation.
