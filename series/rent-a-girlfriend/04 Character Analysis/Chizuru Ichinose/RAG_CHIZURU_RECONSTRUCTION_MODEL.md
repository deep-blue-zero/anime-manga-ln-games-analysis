---
title: "Rent-a-Girlfriend - Chizuru Ichinose Reconstruction Model"
artifact_id: RAG_CHIZURU_RECONSTRUCTION_MODEL
artifact_type: character_reconstruction_model
series: Rent-a-Girlfriend
generation: V1
version: "1.29"
status: canonical
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
created: "2026-09-19"
source_boundary: "Operational model based only on Japanese manga witnesses RAG-JP-EPUB-V001-V028."
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
    - RAG-JP-EPUB-V026
    - RAG-JP-EPUB-V027
    - RAG-JP-EPUB-V028
  admitted_through_volume: V028
  narrative_time_boundary: "after Chizuru apologizes for the silence, states unresolved feeling and work stakes, commits to investigation and a later answer, asks about Ruka, sustains ordinary and vocational contact, and invites Kazuya into task-bound childhood-house labor"
  basis_checkpoint: RAG_CP_V010
  basis_commit: 18fe1738f18a66a91e6a3a340f845f3d7c3d4efe
  model_revision: "1.28"
  prior_knowledge_limitations:
    - "No post-V028 narrative evidence is admitted."
    - "Interiority is sparse; motives are modeled at minimum warranted strength."
    - "Chizuru has directly explained the silence and operationalized inquiry, but its result and any final mutual classification remain unavailable."
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
    - emergency CPR and recovery
    - family-engineered hot-spring travel
    - bounded shared lodging
    - explicit short-term contract renewal
    - recognition by another rental provider
    - acting-school colleague interaction
    - explicit acting ambition and work funding
    - personalized off-contract gift
    - provisional-rival advice
    - rival dialogue before family
    - informed participation in friendship repair
    - private referral and novice-provider coordination
    - acting opportunity with possible rental-work exit
    - hostile booking by a known former partner
    - moral advocacy for Kazuya's prior romantic feeling
    - receipt of direct personal preference
    - dense acting, rental-work, study, and hospital-care routine
    - extended family origin of the acting vocation
    - grief-linked persistence after another rejection
    - project-risk assessment and explicit film request
    - direct rival confrontation over professional rule violation
    - prolonged deliberate neighbor avoidance
    - confidant-prompted self-investigation and paid recontact
    - direct apology and uncertainty conversation
    - unpriced private-room and multi-hour messaging contact
    - theater invitation and childhood-house cleanup
  missing_contexts:
    - sustained study and friendships
    - affirmative romantic self-classification or mutual status agreement
    - long-term acting and rental-work practice
    - acknowledged reciprocal partnership
    - broad private routine
    - repeat post-film professional outcome
  translation_limitations:
    - "Model derives from the Japanese witness; no licensed translation was admitted for comparison."
  written_speech: PARTIALLY_MODELED
  performed_voice: OUT_OF_SCOPE
local_readiness: PARTIAL_MODEL
~~~

## Intended use

This model supports narrow reconstruction of Chizuru at the V028 endpoint when professional rules, family welfare, privacy, audience management, protective deception, bodily initiative, avoidance, emotional self-inquiry, rival-harm accounting, inherited obligation, or task-bound family access are salient. The manga supplies one direct customer-love prohibition, an explicit unnamed-feeling account, and a stated investigation, but interior access remains sparse; the model must not turn those moments into a completed hidden monologue. It must abstain on the investigation result, final romantic classification, intimate partnership, completed ring return, and unseen ordinary preferences.

## Central mechanism

Chizuru manages competing obligations through compartmentalization and bounded exceptions. She can perform warmth as skilled labor, protect a separate campus identity, and speak bluntly when a client threatens those boundaries. When new information reveals a concrete family or dignity cost, she may revise an earlier refusal. She then tends to specify a rule, payment frame, audience story, or exit that limits what the exception means.

The minimum supported motive is responsive responsibility organized around work, privacy, family, and a named vocational project. Professional pride, acting practice, income, the wish to show Sayuri her success, fairness toward Kazuya and Ruka, protection of her own work, and possible personal investment can all contribute. V005-V010 establish informed performance, vocational persistence, selective private access, care, and crisis contact. V011 adds a direct rule for family crisis. V012-V016 show the vocation's family legacy, project consent, campaign governance, completed principal photography, and bounded post-shoot proximity. V017 reaffirms acting as her own choice, moves Sayuri into the planned cinema, and tests comfort-first ethics against terminal risk and visible regret. The admitted evidence does not justify selecting romance as the hidden master explanation or treating professional conduct as emotionally unreal.

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
valid_until_source: "V003 0001"
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

### CHI-S005 — reciprocal rescuer under renewed terms and provider exposure

~~~yaml
state_id: CHI-S005
valid_from_source: "V003 0001"
valid_until_source: "V004 0004"
entry_conditions:
  - "Chizuru wakes after the ferry fall and finds Kazuya unconscious beside her."
active_goals:
  - save Kazuya and contain the rescue's public meaning
  - navigate both grandmothers' shared expectations
  - preserve consent, work, and identity boundaries
  - permit only a legible, temporary continuation
  - prevent Ruka from exposing the rental identity
known_propositions:
  - "Kazuya entered the sea after her and required CPR."
  - "Sayuri says her love would survive ordinary human deception."
  - "Kazuya wants to keep renting her."
  - "Ruka recognizes her as a rental girlfriend."
relationship_conditions:
  - "Kazuya remains a client and deception partner under a renewed nonexclusive rule."
  - "Ruka is an informed outsider whose terms are not known to Chizuru."
changed_from_previous:
  - KNOWLEDGE_CHANGE
  - ACCESS_RECONFIGURATION
  - FAMILY_CONTEXT_CHANGE
  - INFORMATION_RISK_CHANGE
evidence_refs:
  - RAG-E-V003-001
  - RAG-E-V003-003
  - RAG-E-V003-006
  - RAG-E-V003-007
  - RAG-E-V003-008
  - RAG-E-V003-009
  - RAG-E-V003-010
  - RAG-E-V003-013
uncertainties:
  - "How she privately interprets Kazuya's rescue and her own CPR response."
  - "Whether the real-girlfriend rule survives a concrete rival or candidate."
~~~

### CHI-S006 — acting student under personal reciprocity and a provisional triangle

~~~yaml
state_id: CHI-S006
valid_from_source: "V004 0005"
valid_until_source: "V005 0004"
entry_conditions:
  - "Ruka makes secrecy contingent on Kazuya dating her and presents herself as a real-girlfriend candidate."
active_goals:
  - protect her work identity and the grandmothers from abrupt disclosure
  - move Kazuya toward a viable real relationship without careless treatment of Ruka
  - fund and practice for an acting career
  - acknowledge Kazuya's help without erasing provider-client boundaries
known_propositions:
  - "Ruka sincerely wants Kazuya and accepts only a provisional relationship."
  - "Kazuya says he does not reciprocate Ruka's feeling."
  - "Kazuya followed her Christmas outing and falsely inferred that Umi was her boyfriend."
  - "Kazuya values her personalized phone-case gift and returns a gift through a booking."
relationship_conditions:
  - "Kazuya remains a client and deception partner who now has a provisional girlfriend."
  - "Ruka is both a secrecy risk and a person whose sincere feeling should not be treated lightly."
  - "Umi is an acting-school colleague, not a partner."
changed_from_previous:
  - EXIT_POLICY_ACTIVATION
  - VOCATIONAL_DISCLOSURE
  - RECIPROCITY_CHANGE
  - TRIANGULAR_RELATIONSHIP_CHANGE
evidence_refs:
  - RAG-E-V004-003
  - RAG-E-V004-005
  - RAG-E-V004-012
  - RAG-E-V004-014
  - RAG-E-V004-016
  - RAG-E-V004-017
  - RAG-E-V004-018
uncertainties:
  - "How she privately interprets Kazuya's surveillance, gift response, and attachment."
  - "How acting opportunities will change her schedule or identity management."
~~~

### CHI-S007 — informed professional coordinator inside an enlarged network

~~~yaml
state_id: CHI-S007
valid_from_source: "V005 0005"
valid_until_source: "V006 0004"
entry_conditions:
  - "New Year places Chizuru's family role and Ruka's provisional claim before the same audience."
active_goals:
  - protect the family and work secret while responding to Ruka's ethical challenge
  - perform the Kuribayashi booking while supporting Kazuya's reparative purpose
  - help Sumi practice rental-girlfriend work through a known client
  - press Kazuya to clarify unresolved attachment to Mami
known_propositions:
  - "Ruka wants family recognition and asks Chizuru to yield if she does not love Kazuya."
  - "Kuribayashi is Kazuya's friend and the Asakusa booking is intended to encourage him."
  - "Kazuya can be recruited as a practice client for Sumi."
  - "Kazuya remains uncertain about Mami."
relationship_conditions:
  - "Kazuya is a client, neighbor, deception partner, and increasingly trusted collaborator."
  - "Ruka is a sincere rival who preserves the secret while manufacturing intimacy cues."
  - "Sumi is a novice provider whose practice Chizuru is coordinating."
changed_from_previous:
  - FAMILY_RIVAL_CONTEXT_CHANGE
  - INFORMED_WORK_CHANGE
  - COORDINATOR_ROLE_CHANGE
  - FORMER_PARTNER_INQUIRY_CHANGE
evidence_refs:
  - RAG-E-V005-003
  - RAG-E-V005-004
  - RAG-E-V005-010
  - RAG-E-V005-012
  - RAG-E-V005-014
  - RAG-E-V005-015
uncertainties:
  - "Her private response to Ruka's direct question about love."
  - "Whether the acting project re-enters practical scheduling or opportunity after its V005 absence."
  - "How Sumi's practice date changes her trust in Kazuya."
~~~

### CHI-S008 — acting-linked exit planner and advocate under direct address

~~~yaml
state_id: CHI-S008
valid_from_source: "V006 0005"
valid_until_source: "V007 0004"
entry_conditions:
  - "Sumi's practice date continues under the referral Chizuru arranged."
active_goals:
  - support Sumi's development through controlled professional coordination
  - pursue acting opportunities and evaluate leaving rental-girlfriend work
  - answer Mami's client challenge without erasing Kazuya's responsibility or feeling
  - preserve a legible account of why she intervened
known_propositions:
  - "Kazuya completed the Sumi practice date with adaptive support."
  - "An acting opportunity may produce further work and conflict with rental availability."
  - "Mami knows enough about the rental system to book and interrogate her."
  - "Kazuya says directly that Chizuru is the person he wants."
relationship_conditions:
  - "Kazuya is a client, neighbor, collaborator, and now a direct romantic addresser whose answer is pending."
  - "Mami is both a client and former partner whose challenge crosses professional and private domains."
  - "Sumi is a novice provider whose referral has produced a successful practice outcome."
changed_from_previous:
  - REFERRAL_OUTCOME_CHANGE
  - VOCATIONAL_EXIT_RISK_CHANGE
  - FORMER_PARTNER_CONFRONTATION_CHANGE
  - DIRECT_ADDRESS_CHANGE
evidence_refs:
  - RAG-E-V006-001
  - RAG-E-V006-004
  - RAG-E-V006-006
  - RAG-E-V006-007
  - RAG-E-V006-008
  - RAG-E-V006-011
  - RAG-E-V006-013
  - RAG-E-V006-014
  - RAG-E-V006-015
  - RAG-E-V006-017
uncertainties:
  - "Her private interpretation and response to Kazuya's statement."
  - "Whether acting work produces actual rental retirement."
  - "Whether her defense of Kazuya is best explained by fairness, professional self-defense, personal concern, or a combination."
~~~

### CHI-S009 — defeated but recommitting actor granting selective private access

~~~yaml
state_id: CHI-S009
valid_from_source: "V007 0005"
valid_until_source: "V008 0004"
entry_conditions:
  - "Chizuru asks Kazuya to clarify his direct V006 statement."
active_goals:
  - preserve a legible professional relation while processing its affective disturbance
  - continue acting after losing the next role
  - regulate Kazuya's repeated paid support
  - meet Sayuri's family need through controlled access
known_propositions:
  - "Kazuya reclassifies his statement as rental preference."
  - "Her stage performance affected the audience, but she did not receive the next lead."
  - "Kazuya will work and book her to support acting and protected her work secret from Kazuo."
  - "Sayuri wants to see Kazuya during hospitalization."
relationship_conditions:
  - "Kazuya remains a client and neighbor but now receives unpriced ordinary and family access."
  - "Sayuri accepts the public couple premise and privately tests Kazuya."
  - "Sumi remains a junior provider whose V007 supplemental account shows continued effort."
changed_from_previous:
  - PRIVATE_AFFECT_AFTER_CLARIFICATION
  - CASTING_LOSS_AND_RECOMMITMENT
  - PAID_SUPPORT_REGULATION
  - UNPRICED_ACCESS_EXPANSION
evidence_refs:
  - RAG-E-V007-001
  - RAG-E-V007-002
  - RAG-E-V007-003
  - RAG-E-V007-004
  - RAG-E-V007-006
  - RAG-E-V007-010
  - RAG-E-V007-011
  - RAG-E-V007-012
  - RAG-E-V007-013
  - RAG-E-V007-017
uncertainties:
  - "Her romantic self-classification."
  - "Whether acting work later succeeds or again changes rental availability."
  - "How the lost-key request is resolved."
~~~

### CHI-S010 — self-disclosing actor who re-bounds private support

~~~yaml
state_id: CHI-S010
valid_from_source: "V008 0005"
valid_until_source: "V009 0004"
entry_conditions:
  - "The lost key requires temporary practical help inside Kazuya's apartment."
active_goals:
  - resolve immediate access without granting standing private permission
  - explain the family purpose behind acting
  - preserve a legible rental classification after receiving personal support language
  - continue acting for Sayuri and for the promise associated with her grandparents
known_propositions:
  - "Kazuya responds to accidental closeness with restraint."
  - "Ruka discovers the temporary apartment access and remains a rival claimant."
  - "Kazuya wants her dream fulfilled and wants to become her support."
relationship_conditions:
  - "Kazuya is a client, neighbor, collaborator, and recipient of first-person family history."
  - "Ruka knows about the private access but not every detail of the encounter."
  - "Sayuri remains the intended audience for Chizuru's hoped-for screen success."
changed_from_previous:
  - LOST_KEY_HELP_RESOLUTION
  - RIVAL_INFORMATION_EXPOSURE
  - FIRST_PERSON_FAMILY_DISCLOSURE
  - ACTING_PURPOSE_CLARIFICATION
  - SUPPORT_RECEIVED_AND_REBOUNDED
evidence_refs:
  - RAG-E-V008-001
  - RAG-E-V008-002
  - RAG-E-V008-003
  - RAG-E-V008-004
  - RAG-E-V008-005
  - RAG-E-V008-006
  - RAG-E-V008-007
  - RAG-E-V008-008
uncertainties:
  - "Her romantic self-classification."
  - "How she would respond to explicit knowledge of Ruka's overnight stay and kiss."
  - "Whether and when the acting dream produces visible success."
~~~

### CHI-S011 — grateful gift recipient and bounded crisis carer under campus exposure

~~~yaml
state_id: CHI-S011
valid_from_source: "V009 0005"
valid_until_source: "V010 0004"
entry_conditions:
  - "Kazuya completes the Sumi-assisted birthday plan and sends a practical gift with a partial Ruka reassurance."
active_goals:
  - preserve the Ichinose-Mizuhara separation before university friends
  - respond responsibly to Kazuya's intoxication without granting a new status
  - regulate direct digital access and interpretation of unpaid care
  - continue rental work while Mami again gains direct observational access
known_propositions:
  - "Kazuya chose the pickled plums for acting-related fatigue and says he and Ruka have not had sex."
  - "He deliberately overdrank to protect Ichinose from identity scrutiny."
  - "The new university group gives him direct access to the Ichinose LINE profile."
  - "Mami sees and recognizes her during a rental date on the train."
relationship_conditions:
  - "Kazuya receives escort, apartment care, and follow-up medicine outside a booking."
  - "Chizuru objects to unsolicited contact and verbally minimizes romantic interpretation."
  - "Mami is again an informed observer of her rental work."
changed_from_previous:
  - PRACTICAL_GIFT_ACCEPTED
  - PARTIAL_RUKA_REASSURANCE_RECEIVED
  - UNIVERSITY_IDENTITY_COLLISION
  - CRISIS_ESCORT_AND_BODILY_CARE
  - DIRECT_CONTACT_BOUNDARY
  - FOLLOW_UP_MEDICINE
  - MAMI_RECOGNITION
evidence_refs:
  - RAG-E-V009-003
  - RAG-E-V009-004
  - RAG-E-V009-005
  - RAG-E-V009-006
  - RAG-E-V009-007
  - RAG-E-V009-008
  - RAG-E-V009-009
  - RAG-E-V009-010
  - RAG-E-V009-011
  - RAG-E-V009-015
uncertainties:
  - "Her romantic self-classification."
  - "What she says or does after recognizing Mami on the train."
  - "Whether direct LINE access becomes routine or remains tightly bounded."
~~~

### CHI-S012 — professionally self-defining actor under family and hospital pressure

~~~yaml
state_id: CHI-S012
valid_from_source: "V010 0005"
valid_until_source: "V011 0002"
entry_conditions:
  - "Mami questions her after the train sighting, and the May 20 booking tests work identity, intimacy performance, and acting disclosure together."
active_goals:
  - contain Mami's inquiry and protect the cross-audience secret
  - deliver the booked dream-date scenario competently
  - continue acting after securing another stage opportunity
  - honor a family promise while responding to Sayuri's hospital condition
known_propositions:
  - "Mami doubts that her repeated contact with Kazuya is ordinary rental distance."
  - "Kazuya responds enthusiastically to her stage news and promises support."
  - "Nagomi expects her at the joint birthday, and Ruka is also competing in the family space."
  - "The direct LINE route can reach Kazuya during Sayuri's hospital crisis."
relationship_conditions:
  - "Paid girlfriend performance and genuine vocational exchange coexist without a romantic self-report."
  - "Family access is chosen but still rests on the false girlfriend premise."
  - "Direct contact becomes useful by her initiative and remains crisis-bounded."
changed_from_previous:
  - MAMI_DENIAL_AND_CONTAINMENT
  - DREAM_DATE_LEADERSHIP
  - SCRIPTED_INTIMACY_WITH_BOUNDARY
  - RENTAL_WORK_PRIDE_ARTICULATED
  - NEW_STAGE_OPPORTUNITY_DISCLOSED
  - UNBOOKED_FAMILY_ATTENDANCE
  - DIRECT_HOSPITAL_CONTACT
evidence_refs:
  - RAG-E-V010-001
  - RAG-E-V010-004
  - RAG-E-V010-005
  - RAG-E-V010-007
  - RAG-E-V010-008
  - RAG-E-V010-009
  - RAG-E-V010-010
  - RAG-E-V010-011
  - RAG-E-V010-012
  - RAG-E-V010-014
  - RAG-E-V010-016
  - RAG-E-V010-017
uncertainties:
  - "Sayuri's diagnosis, prognosis, and immediate care need."
  - "Whether the new stage work changes rental availability."
  - "Her private evaluation of Kazuya's support and the family-party rivalry."
~~~

### CHI-S013 — protective-deception advocate under inherited burden

~~~yaml
state_id: CHI-S013
valid_from_source: "V011 0003"
valid_until_source: "V012 0004"
entry_conditions:
  - "Sayuri's hospital crisis continues into the Kinoshita birthday, where Ruka's claim and Nagomi's ring make the false relationship immediately consequential."
active_goals:
  - protect Sayuri from distress while her time may be limited
  - manage the Kinoshita family's mistaken future expectations
  - continue functioning despite private family strain
  - coordinate a Sumi practice date around Kazuya
known_propositions:
  - "Ruka says she kissed Kazuya and treats that act as ownership evidence."
  - "Kazuya wants to tell both grandmothers that the relationship is false."
  - "Nagomi gives the ring as both family heirloom and emergency support."
  - "Sayuri has suffered a serious collapse but is conscious after stabilization."
relationship_conditions:
  - "Chizuru and Kazuya now hold incompatible disclosure strategies."
  - "Family care and false prospective-marriage pressure share one material object."
  - "Visible strain coexists with outward coordination and attention to others."
changed_from_previous:
  - HOSPITAL_TO_PARTY_RETURN
  - RUKA_KISS_DISCLOSURE_RECEIVED
  - FAMILY_RING_REFUSED_AND_REDIRECTED
  - PROTECTIVE_DECEPTION_POSITION_STATED
  - PRIVATE_STRAIN_SHOWN
  - SUMI_ROUTE_REOPENED
evidence_refs:
  - RAG-E-V011-001
  - RAG-E-V011-002
  - RAG-E-V011-006
  - RAG-E-V011-008
  - RAG-E-V011-010
  - RAG-E-V011-011
  - RAG-E-V011-012
  - RAG-E-V011-015
uncertainties:
  - "Whether she revisits or executes the truth decision."
  - "Sayuri's prognosis and informed preference."
  - "Her complete purpose in arranging the Sumi practice date."
~~~

### CHI-S014 — grieving actor and voluntary film principal under deadline

~~~yaml
state_id: CHI-S014
valid_from_source: "V012 0005"
valid_until_source: "V013 0004"
entry_conditions:
  - "Sayuri remains hospitalized while Chizuru sustains acting, rental work, study, care, and repeated auditions under a shrinking time horizon."
active_goals:
  - appear on screen for Sayuri
  - continue acting effort after rejection without wasting Sayuri's remaining time
  - evaluate whether Kazuya's independent-film route is feasible enough to accept
  - participate in the film as a project principal rather than a passive beneficiary
known_propositions:
  - "Sayuri performed successfully under the screen name Sayuri Otori."
  - "Katsuhito promised support, expected to see Chizuru on film, and died after briefly repeating his assurance."
  - "Kazuya has researched crowdfunding, personnel, budget ranges, timing, editing, and exhibition."
  - "Kazuya says he will try and will not quit midway."
relationship_conditions:
  - "Sayuri's legacy and Katsuhito's death bind vocation to care, imitation, grief, and obligation."
  - "Chizuru and Kazuya become voluntary film collaborators without settling their truth dispute or romantic status."
  - "Her consent is conditional on project persistence and protection of limited time."
changed_from_previous:
  - WORK_AND_CARE_SYSTEM_MAPPED
  - NEW_FILM_REJECTION_RECEIVED
  - ACTING_ORIGIN_HISTORY_EXPANDED
  - KATSUHITO_LOSS_REACTIVATED
  - FILM_FEASIBILITY_CHALLENGED
  - FILM_PROJECT_EXPLICITLY_REQUESTED
evidence_refs:
  - RAG-E-V012-008
  - RAG-E-V012-009
  - RAG-E-V012-010
  - RAG-E-V012-011
  - RAG-E-V012-012
  - RAG-E-V012-013
  - RAG-E-V012-014
  - RAG-E-V012-015
  - RAG-E-V012-016
  - RAG-E-V012-017
  - RAG-E-V012-018
  - RAG-E-V012-019
  - RAG-E-V012-020
  - RAG-E-V012-021
  - RAG-E-V012-022
uncertainties:
  - "Whether the campaign and film can be completed before Sayuri's condition worsens."
  - "How Chizuru divides project agency, acting labor, and existing work obligations."
  - "Whether the dormant truth, ring, and relationship routes re-enter the production effort."
~~~

### CHI-S015 — publicly exposed film principal in governed collaboration

~~~yaml
state_id: CHI-S015
valid_from_source: "V013 0005"
valid_until_source: "V014 0004"
entry_conditions:
  - "Chizuru has requested the film but professional terms, money, disclosure, collaborators, and campaign approval remain unresolved."
active_goals:
  - make the film for Sayuri without wasting her remaining time
  - preserve acting professionalism and controlled identity disclosure
  - contribute materially without bearing every project cost
  - expand project capacity while keeping work access correctly classified
known_propositions:
  - "Her manager approves the film and Sayuri permits campaign use of the family story."
  - "The budget target is 1.82 million yen and the campaign window is forty-five days."
  - "Mini knows a bounded account and has offered help."
  - "Sayuri calls Kazuya suitable for her, but Chizuru has not adopted that romantic classification."
relationship_conditions:
  - "Kazuya is the named producer and a sustained non-booked collaborator."
  - "Mini is a recruited volunteer and active audience whose inference requires correction."
  - "Sayuri is informed about the film but not the rental truth."
changed_from_previous:
  - AGENCY_APPROVAL_REPORTED
  - PRIVATE_WORK_ACCESS_INITIATED
  - BUDGET_AND_CAMPAIGN_AGENCY_EXERCISED
  - MINI_RECRUITED
  - SAYURI_PERMISSION_SECURED
  - CAMPAIGN_PUBLISHED
evidence_refs:
  - RAG-E-V013-001
  - RAG-E-V013-003
  - RAG-E-V013-004
  - RAG-E-V013-006
  - RAG-E-V013-007
  - RAG-E-V013-008
  - RAG-E-V013-010
  - RAG-E-V013-011
  - RAG-E-V013-013
  - RAG-E-V013-014
  - RAG-E-V013-015
  - RAG-E-V013-017
  - RAG-E-V013-018
  - RAG-E-V013-019
  - RAG-E-V013-021
  - RAG-E-V013-022
uncertainties:
  - "Whether funding and production can finish in time."
  - "How public exposure affects university and acting work."
  - "Whether Sayuri's suitability judgment changes Chizuru's private appraisal."
~~~

### CHI-S016 — campaign principal under calibrated exposure and direct preference information

~~~yaml
state_id: CHI-S016
valid_from_source: "V014 0005"
valid_until_source: "V015 0004"
entry_conditions:
  - "The published campaign begins to attract support while script, director, and remaining finance are unresolved."
active_goals:
  - help convert the live campaign into a funded and executable film
  - participate in source, staffing, reward, and publicity decisions
  - retain control over professional identity, personal property, intimate access, and relationship classification
known_propositions:
  - "The campaign has hundreds of supporters but later stalls below its target."
  - "The selected source is acceptable, permission has been obtained, and Tabuse agrees to direct."
  - "Mini has concrete campaign competence and believes Kazuya likes Chizuru."
  - "Kazuya is kind and his film work produces deep gratitude, while romance remains separately classified in Chizuru's statement."
relationship_conditions:
  - "Kazuya is a consequential producer and collaborator without mutual romantic status."
  - "Mini is a useful strategist who presses beyond project work into relationship interpretation."
  - "Ruka can join team labor while retaining rivalry."
changed_from_previous:
  - CAMPAIGN_TRACTION_AND_STALL_OBSERVED
  - SOURCE_APPROVED
  - DIRECTOR_MEETING_COMPLETED
  - RECOVERY_STRATEGY_JOINED
  - PERSONAL_PROPERTY_REWARDS_OFFERED
  - INTIMATE_DRESSER_BOUNDARY_ENFORCED
  - KAZUYA_PREFERENCE_CLAIM_RECEIVED
evidence_refs:
  - RAG-E-V014-002
  - RAG-E-V014-003
  - RAG-E-V014-007
  - RAG-E-V014-009
  - RAG-E-V014-010
  - RAG-E-V014-012
  - RAG-E-V014-013
  - RAG-E-V014-016
  - RAG-E-V014-017
  - RAG-E-V014-019
uncertainties:
  - "How she responds to Mini's direct statement about Kazuya."
  - "Whether reward exposure and campaign publicity create later professional or privacy costs."
  - "Whether the project is funded and completed before Sayuri's deadline."
~~~

### CHI-S017 — filming lead under qualified romantic ambiguity

~~~yaml
state_id: CHI-S017
valid_from_source: "V015 0005"
valid_until_source: "V016 0004"
entry_conditions:
  - "Mini's direct preference disclosure requires a response while the campaign and film remain under deadline."
active_goals:
  - complete the campaign and film for Sayuri
  - use acting and social networks without surrendering decision authority
  - perform the lead role under professional production conditions
  - preserve control over romantic classification and access
known_propositions:
  - "Mini believes Kazuya likes her, and Kazuya's film effort has materially restored her ability to act for Sayuri."
  - "Umi recently ended his relationship, is romantically probing, and can expose the campaign to a large audience."
  - "The campaign is funded and principal photography operates under Tabuse."
relationship_conditions:
  - "Her self-report to Umi moves from direct negation to a qualified non-negation about Kazuya."
  - "Kazuya remains producer and accepts a concentration boundary on set."
  - "No direct mutual romantic discussion or status change occurs."
changed_from_previous:
  - DIRECT_PREFERENCE_DISCLOSURE_ANSWERED
  - KAZUYA_SUPPORT_EXPLICITLY_CREDITED
  - UMI_DINNER_REFUSED
  - QUALIFIED_NON_NEGATION_STATED
  - CAMPAIGN_FUNDED
  - LEAD_PERFORMANCE_FILMED
  - LOCAL_CREW_RECEPTION_OBSERVED
evidence_refs:
  - RAG-E-V015-001
  - RAG-E-V015-003
  - RAG-E-V015-005
  - RAG-E-V015-006
  - RAG-E-V015-007
  - RAG-E-V015-008
  - RAG-E-V015-009
  - RAG-E-V015-011
  - RAG-E-V015-012
  - RAG-E-V015-013
  - RAG-E-V015-015
uncertainties:
  - "Whether she will communicate the qualified appraisal to Kazuya."
  - "Whether filmed performance produces a career opportunity or reaches Sayuri in time."
  - "How professional distance and personal reliance interact after production."
~~~

### CHI-S018 — final-scene lead under direct gratitude and private affective activation

~~~yaml
state_id: CHI-S018
valid_from_source: "V016 0005"
valid_until_source: "V017 0067"
entry_conditions:
  - "Principal photography nears its final scene while Kazuya interprets her acting success as evidence that they belong to different worlds."
active_goals:
  - complete the final performance and move the film toward Sayuri
  - correct Kazuya's self-demotion while retaining authority over relationship classification
  - govern project travel, room access, and rivalry pressure under explicit limits
known_propositions:
  - "Kazuya expects career distance and regards his own life as inferior to hers."
  - "Mini engineered the two-person trip and used Ruka's name without her consent."
  - "The film can preserve the family promise after Katsuhito's death and may reach Sayuri when auditions cannot."
  - "Ruka's trial remains unresolved, and Kazuya says a future family introduction should concern someone he truly loves."
relationship_conditions:
  - "She rejects the status hierarchy, calls Kazuya's life wonderful, and says she has never regretted meeting him."
  - "She privately recalls her qualified non-negation and shows wakeful affective activation without affirmative disclosure or proved nighttime contact."
  - "She permits bounded travel and room access, then gives Ruka a factual denial of kissing."
changed_from_previous:
  - DIFFERENT_WORLD_HIERARCHY_REJECTED
  - NO_REGRET_STATEMENT_GIVEN
  - ENGINEERED_TRIP_IDENTIFIED
  - BOUNDED_SHARED_ROOM_ACCEPTED
  - FAMILY_PURPOSE_AND_GRATITUDE_DISCLOSED
  - FINAL_PERFORMANCE_COMPLETED
  - QUALIFIED_NON_NEGATION_PRIVATELY_RECALLED
  - RUKA_TRIAL_DIRECTLY_QUERIED
evidence_refs:
  - RAG-E-V016-001
  - RAG-E-V016-002
  - RAG-E-V016-003
  - RAG-E-V016-004
  - RAG-E-V016-005
  - RAG-E-V016-006
  - RAG-E-V016-008
  - RAG-E-V016-010
  - RAG-E-V016-011
  - RAG-E-V016-012
  - RAG-E-V016-014
  - RAG-E-V016-015
  - RAG-E-V016-016
  - RAG-E-V016-017
uncertainties:
  - "Whether the edited film reaches Sayuri and produces any public career consequence."
  - "Whether she communicates an affirmative or negative romantic classification to Kazuya."
  - "Whether post-shoot access continues when project necessity no longer governs it."
~~~

### CHI-S019 — family-purpose actor under terminal-risk truth conflict

~~~yaml
state_id: CHI-S019
valid_from_source: "V017 0068"
valid_until_source: "V018 0004"
entry_conditions:
  - "The film is in editing with a September 30 accessible-cinema plan while Sayuri remains its intended family recipient."
active_goals:
  - finish and deliver the film to Sayuri
  - continue acting as a chosen pursuit rather than only an inherited obligation
  - protect Sayuri's happiness while governing whether the rental-and-family account is corrected
known_propositions:
  - "The edit remains incomplete, but Kazuya has arranged a 200-seat wheelchair-accessible cinema for September 30."
  - "Sayuri thanks Kazuya, interprets Chizuru's happy project account as possible love, and asks whether acting is truly Chizuru's choice."
  - "Sayuri collapses after the cinema visit, and the physician says recovery is difficult and the night may be critical."
  - "Kazuya challenges comfort-first silence and tells Chizuru to prioritize her own feelings."
relationship_conditions:
  - "She waits for and thanks Kazuya again after his private conversation with Sayuri."
  - "Her no-regret account coexists with visible tears and bodily strain that Kazuya notices."
  - "She rejects a sad final truth for Sayuri but gives Kazuya no mutual romantic classification."
changed_from_previous:
  - SCREENING_DATE_AND_ACCESSIBLE_VENUE_COORDINATED
  - ACTING_REAFFIRMED_AS_CHOSEN_PURSUIT
  - KAZUYA_THANKED_AGAIN_AFTER_FAMILY_CONVERSATION
  - SAYURI_COLLAPSE_AND_CRITICAL_PROGNOSIS_RECEIVED
  - NO_REGRET_ACCOUNT_VISUALLY_COMPLICATED
  - COMFORT_FIRST_TRUTH_RULE_REASSERTED
evidence_refs:
  - RAG-E-V017-005
  - RAG-E-V017-006
  - RAG-E-V017-008
  - RAG-E-V017-011
  - RAG-E-V017-012
  - RAG-E-V017-013
  - RAG-E-V017-014
  - RAG-E-V017-015
  - RAG-E-V017-016
  - RAG-E-V017-017
  - RAG-E-V017-018
uncertainties:
  - "Whether Sayuri survives and receives the completed film."
  - "Whether Chizuru discloses the rental truth or maintains the comforting belief."
  - "What Kazuya's LINE-and-running action changes."
  - "Whether she communicates a romantic classification to Kazuya."
~~~

### CHI-S020 — bereaved granddaughter after partial truth and final recognition

~~~yaml
state_id: CHI-S020
valid_from_source: "V018 0005"
valid_until_source: "V019 0004"
entry_conditions:
  - "Sayuri remains critically ill while the promised film is unfinished and Kazuya has initiated an unknown action."
active_goals:
  - give Sayuri the most honest and loving final exchange she can manage
  - handle death and funeral obligations under controlled public presentation
  - preserve agency over what help and professional access she accepts
known_propositions:
  - "Kazuya can project unfinished footage at the bedside, allowing Sayuri to see her act."
  - "She states that she and Kazuya are not dating, but Sayuri entrusts the answer to her rather than demand rental details."
  - "Sayuri praises the film, asks that Kazuya be thanked, calls Chizuru her treasure, and dies after reciprocal declarations of love."
  - "Sumi, Nagomi, and Kazuya treat continued composure as compatible with grief and support need."
relationship_conditions:
  - "Her family relation with Sayuri closes through touch, embrace, film acknowledgment, and reciprocal love."
  - "She says she is fine and does not accept Kazuya's immediate offer of help."
  - "Kazuya remains a neighbor, collaborator, and prospective paying client rather than an acknowledged partner."
changed_from_previous:
  - UNFINISHED_FILM_RECEIVED_AT_BEDSIDE
  - CENTRAL_RELATIONSHIP_FACT_DISCLOSED
  - SAYURI_ENTRUSTS_CHIZURUS_ANSWER
  - FINAL_FAMILY_LOVE_RECIPROCATED
  - SAYURI_DEATH_AND_FUNERAL_COMPLETED
  - GRIEF_CARRIED_THROUGH_CONTROLLED_PRESENTATION
  - IMMEDIATE_HELP_DECLINED
evidence_refs:
  - RAG-E-V018-001
  - RAG-E-V018-002
  - RAG-E-V018-003
  - RAG-E-V018-004
  - RAG-E-V018-005
  - RAG-E-V018-006
  - RAG-E-V018-007
  - RAG-E-V018-008
  - RAG-E-V018-009
  - RAG-E-V018-010
  - RAG-E-V018-011
  - RAG-E-V018-019
  - RAG-E-V018-020
uncertainties:
  - "Whether she accepts Kazuya's rental request and what support she permits during it."
  - "Whether controlled presentation breaks into direct grief expression before Kazuya."
  - "Whether the film is finished and publicly screened after Sayuri's death."
  - "Whether she communicates any romantic classification to Kazuya."
~~~

### CHI-S021 — bereaved provider after accepted grief release

~~~yaml
state_id: CHI-S021
valid_from_source: "V019 0005"
valid_until_source: "V020 0004"
entry_conditions:
  - "Sayuri has died, Chizuru has maintained controlled funeral conduct, and Kazuya's unusually long rental request is available for acceptance."
active_goals:
  - complete the coming public film screening and continue acting-related obligations
  - retain agency over grief disclosure, bodily support, and relationship classification
  - resume ordinary functioning without denying the relief she received
known_propositions:
  - "Kazuya planned the elaborate date because of Sayuri and had already delivered the bedside projection she values."
  - "She can enjoy clothing, film, climbing, and food while grief remains active and family cues still breach composure."
  - "Kazuya's ideal-girlfriend speech recognizes sadness without requiring a direct reply."
  - "Before crying she felt so lonely she thought she might die, and crying before someone left her refreshed."
relationship_conditions:
  - "She initiates role-framed handholding and later initiates unpriced bodily reliance during grief."
  - "She restores public control after crying and does not discuss the episode with Kazuya in the observed follow-up."
  - "She tells Mini that Kazuya is not her boyfriend and that she remains his rental girlfriend."
changed_from_previous:
  - TEN_HOUR_BOOKING_ACCEPTED
  - CARE_PURPOSE_RECOGNIZED_AND_QUESTIONED
  - ACTIVITY_ENJOYMENT_OBSERVED
  - FAMILY_MEMORY_TRIGGERS_BREACH_CONTROL
  - GRIEF_WALL_BROKEN
  - SELF_INITIATED_BODILY_SUPPORT_ACCEPTED
  - DIRECT_LONELINESS_AND_RELIEF_REPORT
  - NON_BOYFRIEND_CLASSIFICATION_RETAINED
evidence_refs:
  - RAG-E-V019-001
  - RAG-E-V019-002
  - RAG-E-V019-003
  - RAG-E-V019-004
  - RAG-E-V019-005
  - RAG-E-V019-006
  - RAG-E-V019-007
  - RAG-E-V019-008
  - RAG-E-V019-009
  - RAG-E-V019-010
  - RAG-E-V019-011
  - RAG-E-V019-013
  - RAG-E-V019-014
  - RAG-E-V019-015
  - RAG-E-V019-016
  - RAG-E-V019-019
  - RAG-E-V019-020
uncertainties:
  - "Whether relief changes her later willingness to seek or discuss support with Kazuya."
  - "Whether the public screening is completed and how bereavement affects it."
  - "How she interprets Kazuya romantically beyond the explicit non-boyfriend classification."
  - "Whether one acute release changes her longer-term controlled presentation."
~~~

### CHI-S022 — continuing actor and direct questioner under incomplete romantic information

~~~yaml
state_id: CHI-S022
valid_from_source: "V020 0005"
valid_until_source: "V021 0004"
entry_conditions:
  - "The film is ready for public exhibition, grief release has been reported to Mini, and Chizuru still classifies Kazuya as a customer rather than a boyfriend."
active_goals:
  - continue acting as a chosen vocation after the family promise is publicly completed
  - reaccount for the ten-hour date without surrendering professional standards
  - determine whether Kazuya's ideal-girlfriend speech and Mini's claim describe his actual feeling
  - control the audience and timing of any response
known_propositions:
  - "The film receives applause and she enjoyed making it enough to intend continued acting."
  - "Kazuya regards her crying as real and valuable rather than failed service."
  - "Mini told her that Kazuya likes her, and the ideal-girlfriend speech plausibly described her."
  - "Kazuya says the speech was sincere, identifies Mizuhara as his ideal girlfriend, and begins a longer declaration."
relationship_conditions:
  - "She initiates an unbooked café meeting and accepts an ordinary meal extension."
  - "She restores the rental-girlfriend frame before Kazuya's direct declaration."
  - "She privately replays the interrupted answer but later blocks public discussion before friends."
changed_from_previous:
  - PUBLIC_FILM_EXHIBITION_RECEIVED
  - ACTING_REAFFIRMED_AS_PERSONAL_CHOICE
  - UNBOOKED_DIRECT_INVITATION_INITIATED
  - GRIEF_DATE_REACCOUNTED_THROUGH_REFUND
  - POSSIBLE_WEAKNESS_SELF_DESCRIBED
  - ORDINARY_MEAL_ACCESS_ACCEPTED
  - DIRECT_ROMANTIC_QUESTION_ASKED
  - PARTIAL_DECLARATION_HEARD_AND_REPLAYED
  - PUBLIC_RESPONSE_DEFERRED
evidence_refs:
  - RAG-E-V020-001
  - RAG-E-V020-002
  - RAG-E-V020-009
  - RAG-E-V020-011
  - RAG-E-V020-012
  - RAG-E-V020-013
  - RAG-E-V020-014
  - RAG-E-V020-015
  - RAG-E-V020-016
  - RAG-E-V020-017
  - RAG-E-V020-018
  - RAG-E-V020-019
  - RAG-E-V020-020
  - RAG-E-V020-021
  - RAG-E-V020-024
  - RAG-E-V020-025
uncertainties:
  - "Whether she accepts, rejects, or continues to defer Kazuya's romantic intent."
  - "Whether asking directly reflects curiosity, practical classification need, romantic interest, or a mixture."
  - "Whether her public avoidance persists in private and low-pressure conditions."
  - "Whether acting continuity produces a professional opportunity."
~~~

### CHI-S023 — professional-world host and deception monitor under direct Mami pressure

~~~yaml
state_id: CHI-S023
valid_from_source: "V021 0005"
valid_until_source: "V022 0004"
entry_conditions:
  - "Kazuya's romantic intent is partly heard but unanswered, her acting vocation continues, and Mami has recurring family access under an app-work account."
active_goals:
  - maintain acting-network and project relations without surrendering classification control
  - determine the practical threat created by Mami's knowledge
  - coordinate with Kazuya while avoiding premature provocation
  - decide how to help Kazuya under family and former-partner pressure
known_propositions:
  - "Kazuya is accepted as the film's producer inside her acting-network party."
  - "Umi and Kazuya have discussed her earlier qualified answer."
  - "A person she came to like would be someone she thinks she would want to date and stay beside."
  - "Mami saw her bag in Kazuya's room and found the public crowdfunding page."
  - "Mami reports a negative former-partner experience, claims ally status, and proposes ending everything together."
  - "Nagomi remains in direct contact with both Chizuru and Mami."
relationship_conditions:
  - "She voluntarily brings Kazuya into her professional network but gives no present romantic classification."
  - "She and Kazuya share a monitoring problem and an intended response without a completed plan."
  - "Mami possesses real evidence but supplies an interested interpretation and withheld endpoint."
changed_from_previous:
  - ACTING_NETWORK_GUEST_ACCESS_GRANTED
  - PRODUCER_ROLE_PUBLICLY_AFFIRMED
  - CONDITIONAL_PARTNER_PREFERENCE_STATED
  - INFORMATION_LEAK_RECONSTRUCTED
  - MUTUAL_MONITORING_PROPOSED
  - MAMI_TESTIMONY_AND_ALLIANCE_OFFER_RECEIVED
  - FAMILY_LINKED_OVERNIGHT_QUESTION_OPENED
  - HELP_INTENTION_FORMED
evidence_refs:
  - RAG-E-V021-002
  - RAG-E-V021-003
  - RAG-E-V021-004
  - RAG-E-V021-006
  - RAG-E-V021-007
  - RAG-E-V021-008
  - RAG-E-V021-009
  - RAG-E-V021-014
  - RAG-E-V021-015
  - RAG-E-V021-018
  - RAG-E-V021-019
  - RAG-E-V021-020
  - RAG-E-V021-021
  - RAG-E-V021-023
  - RAG-E-V021-024
uncertainties:
  - "How she evaluates Mami's testimony and claimed alliance."
  - "What action she intends by helping Kazuya and asking about overnight availability."
  - "Whether her conditional partner account has any current identified referent."
~~~

### CHI-S024 — family-trip participant under fabricated rivalry evidence and immediate confession pressure

~~~yaml
state_id: CHI-S024
valid_from_source: "V022 0005"
valid_until_source: "V023 0004"
entry_conditions:
  - "Chizuru has decided to help Kazuya under Mami's pressure and receives Nagomi's invitation to a bereavement-care family trip."
active_goals:
  - accept or limit family care without pretending the ring and public couple premise are ethically settled
  - evaluate Ruka's sexual claim and Mami's embedded presence without surrendering response control
  - coordinate the trip and eventual explanation with Kazuya
  - govern when and under what conditions Kazuya's romantic answer can be heard
known_propositions:
  - "She sees Ruka kissing Kazuya but does not hear his preceding refusal."
  - "Ruka claims sex with Kazuya and leaves a torn wrapper; Chizuru has no verification, while the manga directly establishes that Ruka fabricated the event."
  - "Nagomi organizes the trip to comfort her after Sayuri's death."
  - "She still has Nagomi's ring, intends to return it, and has Kazuya's cooperation in getting through the trip."
  - "Mami is embedded in the group, and Nagomi knows the public acting, crowdfunding, and producer facts."
  - "Kazuya begins answering her earlier question about whether he likes her."
relationship_conditions:
  - "Nagomi's care is personally valuable but remains structured by the false girlfriend premise."
  - "Chizuru and Kazuya form a reciprocal operational alliance without mutual romantic status."
  - "Ruka and Mami each apply different information pressure, while Chizuru controls neither source fully."
changed_from_previous:
  - FAMILY_TRIP_ACCEPTED
  - RUKA_KISS_OBSERVED_WITH_PARTIAL_CONTEXT
  - FABRICATED_SEX_CLAIM_RECEIVED
  - RING_RETURN_INTENT_REASSERTED
  - GET_THROUGH_ALLIANCE_FORMED
  - MISSING_FAMILY_TRIP_EXPERIENCE_DISCLOSED
  - MAMI_TRIP_PRESENCE_RECEIVED
  - IMMEDIATE_CONFESSION_RECOGNIZED_AND_AVOIDED
evidence_refs:
  - RAG-E-V022-001
  - RAG-E-V022-003
  - RAG-E-V022-004
  - RAG-E-V022-005
  - RAG-E-V022-006
  - RAG-E-V022-007
  - RAG-E-V022-010
  - RAG-E-V022-011
  - RAG-E-V022-012
  - RAG-E-V022-014
  - RAG-E-V022-016
  - RAG-E-V022-018
  - RAG-E-V022-021
  - RAG-E-V022-022
  - RAG-E-V022-025
uncertainties:
  - "Whether and how she verifies or corrects Ruka's fabricated claim."
  - "Whether she returns the ring or participates in a full family correction."
  - "Whether leaving the confession reflects timing, pressure, fear, rejection, or a mixture."
~~~

### CHI-S025 — chosen-family participant and direct verifier under contested evidence

~~~yaml
state_id: CHI-S025
valid_from_source: "V023 0005"
valid_until_source: null
entry_conditions:
  - "Chizuru is inside Nagomi's family trip with a deferred confession, the ring obligation, Ruka's false wrapper claim, and Mami embedded in the group."
active_goals:
  - govern vulnerable bodily access through specific answers and practical scope
  - verify consequential claims without surrendering response timing or audience control
  - receive family care while preserving awareness of the false premise and ring obligation
  - evaluate Mami and Ruka without assigning certainty beyond their observable acts
known_propositions:
  - "Kazuya follows the agreed swimsuit-fastening task and does not expand it."
  - "Mami says she will not expose the rental arrangement without warning and continues information activity inside the trip."
  - "Ruka repeats the sex claim in Kazuya's presence, and Kazuya directly denies it."
  - "Kazuya still intends to end the lie during the trip, although Chizuru does not receive every part of his Mami conversation."
  - "Sayuri taught her to recognize available happiness, and the gathered group now makes that teaching personally legible."
relationship_conditions:
  - "Kazuya is an operational ally and direct credibility source, not an acknowledged partner."
  - "Nagomi's care is emotionally valuable while remaining structured by false couple information."
  - "Ruka and Mami apply different disclosure and status pressure, neither of which Chizuru accepts as complete truth."
changed_from_previous:
  - RAFT_ACTIVITY_ACCEPTED
  - SWIMSUIT_HELP_SPECIFICALLY_AUTHORIZED
  - ROLE_FRAMED_COMPLIMENT_REQUESTED
  - RUKA_RELATIONSHIP_UPDATE_REQUESTED
  - MAMI_WARNING_RECEIVED
  - WRAPPER_REAPPEARANCE_OBSERVED
  - RUKA_CLAIM_HEARD_UNDER_KAZUYA_DENIAL
  - DIRECT_CREDIBILITY_QUESTION_ASKED
  - SAYURI_HAPPINESS_TEACHING_RECALLED
  - GROUP_RECOGNIZED_AS_CHOSEN_FAMILY
  - DAY_APPRAISED_AS_BEST
evidence_refs:
  - RAG-E-V023-002
  - RAG-E-V023-003
  - RAG-E-V023-005
  - RAG-E-V023-007
  - RAG-E-V023-008
  - RAG-E-V023-016
  - RAG-E-V023-017
  - RAG-E-V023-018
  - RAG-E-V023-020
  - RAG-E-V023-021
  - RAG-E-V023-022
uncertainties:
  - "Whether she accepts Kazuya's denial and how she classifies Ruka's fabrication."
  - "Whether chosen-family value changes the timing of ring return or public correction."
  - "Whether she permits, answers, or further defers Kazuya's confession."
~~~

### CHI-S026 — explicitly included family participant under released ring obligation and direct answer pressure

~~~yaml
state_id: CHI-S026
valid_from_source: "V024 0005"
valid_until_source: null
entry_conditions:
  - "Chizuru remains inside Nagomi's family trip after identifying it as her best day, with the inherited ring, Ruka's fabricated claim, Mami's intervention, and Kazuya's confession deadline unresolved."
active_goals:
  - receive family care without treating it as compulsory marriage or indefinite deception
  - preserve professional accounting for access the agency cannot formally process
  - clarify consequential former-partner information while retaining control of her own classification
  - address the ring and family premise without accepting Ruka's false evidence or unilateral status
known_propositions:
  - "Nagomi explicitly says that Chizuru's family is present and wants her happiness."
  - "Harumi regards Chizuru with maternal care and says the inherited ring may be returned without resentment."
  - "Ruka demands truth and ring return, repeats the false sex claim, and still covers the situation before Nagomi."
  - "Kazuya says that he does not want Mami and regards her as dangerous, while offering limited help interpreting her."
  - "Kazuya has reached the chapel and directly asks Chizuru to listen."
relationship_conditions:
  - "Kazuya remains an operational ally and direct information source whose initiated proposition is not yet available."
  - "Nagomi and Harumi extend real care through an inaccurate partner premise, while Harumi removes one presumed object obligation."
  - "Ruka and Mami continue distinct pressure routes without controlling Chizuru's answer."
changed_from_previous:
  - EXPLICIT_FAMILY_ASSURANCE_RECEIVED
  - UNREPORTABLE_TRIP_ACCOUNTING_PROPOSED
  - TRIP_ENJOYMENT_STATED_DIRECTLY
  - MATERNAL_CONSULTATION_OFFER_RECEIVED
  - RING_RETURN_PERMISSION_RECEIVED
  - MARRIAGE_PLAN_DENIED
  - FAVORITE_PERSON_CUSTOMER_BINARY_WITHHELD
  - PRESENT_MAMI_PREFERENCE_CHECKED_DIRECTLY
  - KAZUYA_MAMI_DENIAL_RECEIVED
  - CHAPEL_LISTEN_REQUEST_RECEIVED
evidence_refs:
  - RAG-E-V024-002
  - RAG-E-V024-005
  - RAG-E-V024-006
  - RAG-E-V024-007
  - RAG-E-V024-008
  - RAG-E-V024-009
  - RAG-E-V024-011
  - RAG-E-V024-012
  - RAG-E-V024-013
  - RAG-E-V024-014
  - RAG-E-V024-015
  - RAG-E-V024-019
  - RAG-E-V024-022
uncertainties:
  - "How she receives and answers the initiated chapel speech."
  - "Whether Harumi's release changes the timing or method of ring return."
  - "How she finally classifies Kazuya, Ruka's fabrication, and Mami's intervention."
~~~

### CHI-S027 — method-refusing participant under conditional secrecy and identity exposure

~~~yaml
state_id: CHI-S027
valid_from_source: "V025 0005"
valid_until_source: null
entry_conditions:
  - "Chizuru is at the chapel under simultaneous Kazuya confession pressure and Mami's family-disclosure intervention."
active_goals:
  - prevent Mami from controlling the timing and method of family correction
  - preserve Kazuya's agency and Nagomi's welfare while admitting her own role in the lie
  - keep the inherited ring and rental identity from being used without context
  - maintain immediate safety through a conditional cover without surrendering final response control
known_propositions:
  - "Mami overheard the morning account, regards Chizuru as a victim, and planned to use the ring and room 8504 for immediate disclosure."
  - "Kazuya tried to continue the chapel speech but does not know why Chizuru left."
  - "Mami agrees to defer only if Chizuru aligns a financial-dispute cover and hides the exchange from Kazuya."
  - "Kazuya still promises to protect Chizuru and wants Nagomi to keep dreaming."
  - "Chizuru's Diamond profile is visible on Ruka's fallen phone before the mixed group; V026 records Mami saying that she dropped it."
relationship_conditions:
  - "Chizuru defends Kazuya's decisional agency and accepts his care without giving a romantic answer or full information."
  - "Nagomi's real care and smile coexist with an inaccurate relationship premise now under direct profile exposure."
  - "Mami's claimed alliance has become coercive and conditional, while Ruka's status and fabrication remain unresolved."
changed_from_previous:
  - LIMIT_MESSAGE_SENT
  - CHAPEL_ATTEMPT_LEFT_UNANSWERED_UNDER_MAMI_PRESSURE
  - ROOM_AND_RING_PLAN_RECEIVED
  - PRACTICAL_OBJECTIONS_RAISED
  - NAGOMI_INSULT_RETRACTION_DEMANDED
  - KAZUYA_CORRECTION_AGENCY_DEFENDED
  - COERCIVE_DISCLOSURE_METHOD_REFUSED
  - CONDITIONAL_COVER_BARGAIN_ACCEPTED
  - KAZUYA_PROTECTION_PROMISE_ACCEPTED
  - DIAMOND_PROFILE_EXPOSURE_WITNESSED
evidence_refs:
  - RAG-E-V025-001
  - RAG-E-V025-002
  - RAG-E-V025-003
  - RAG-E-V025-004
  - RAG-E-V025-005
  - RAG-E-V025-006
  - RAG-E-V025-010
  - RAG-E-V025-012
  - RAG-E-V025-013
  - RAG-E-V025-014
  - RAG-E-V025-017
  - RAG-E-V025-018
  - RAG-E-V025-020
  - RAG-E-V025-021
  - RAG-E-V025-022
uncertainties:
  - "How she explains or contests the profile display before the mixed audience."
  - "Whether she discloses Mami's pressure and conditional bargain to Kazuya."
  - "Whether the inherited ring, family bond, and unfinished confession can be addressed together or remain compartmented."
~~~

### CHI-S028 — publicly acting protector inside near-complete correction

~~~yaml
state_id: CHI-S028
valid_from_source: "V026 0005"
valid_until_source: "V027 0005"
entry_conditions:
  - "Chizuru's Diamond profile is visible on Ruka's phone before a mixed family and peer audience, and Mami says that she dropped the device."
active_goals:
  - prevent Kazuya from carrying the exposure alone
  - correct identity and service facts while preserving immediate family access
  - resist Mami's reduction of the relationship to money and deception
  - retain control over private relationship meaning after public bodily proof
known_propositions:
  - "Mami selectively combines money, ring, heir, and Sayuri facts while omitting her own bargain and drop role from the accusation."
  - "Kazuya publicly says that he loves Chizuru but knowingly fabricates an earlier mutual dating timeline."
  - "Chizuru initiates two real kisses, discloses her real name and role, and says that Kazuya became important."
  - "The later room account preserves genuine dating as the sole remaining lie."
relationship_conditions:
  - "Chizuru and Kazuya have major public intimacy evidence but no private mutual status agreement."
  - "Nagomi accepts and apologizes under a near-complete account, while the ring remains unreturned on-page."
  - "Ruka resists Mami's method but leaves visibly unsettled and without withdrawing her claim."
changed_from_previous:
  - PHONE_ATTRIBUTION_CORRECTED_TO_RUKA
  - MAMI_DROP_ACKNOWLEDGMENT_RECEIVED
  - PUBLIC_ACCUSATION_ENDURED
  - FIRST_KISS_INITIATED_AND_SUSTAINED
  - REAL_NAME_AND_RENTAL_ROLE_DISCLOSED
  - KAZUYA_PERSONAL_IMPORTANCE_STATED
  - PUBLIC_GIRLFRIEND_CLAIM_MADE
  - SECOND_KISS_INITIATED
  - FAMILY_ACCOUNT_NARROWED_TO_ONE_RESIDUAL_LIE
evidence_refs:
  - RAG-E-V026-001
  - RAG-E-V026-002
  - RAG-E-V026-003
  - RAG-E-V026-004
  - RAG-E-V026-005
  - RAG-E-V026-006
  - RAG-E-V026-011
  - RAG-E-V026-012
  - RAG-E-V026-013
  - RAG-E-V026-014
  - RAG-E-V026-015
  - RAG-E-V026-016
uncertainties:
  - "How Chizuru privately interprets and bounds the two kisses and Kazuya's love declaration."
  - "Whether she corrects the residual dating lie or returns the inherited ring."
  - "How she responds to Ruka's unresolved claim and Mami's failed intervention."
~~~

### CHI-S029 — professionally conflicted avoider entering explicit self-investigation

~~~yaml
state_id: CHI-S029
valid_from_source: "V027 0005"
valid_until_source: "V028 0005"
entry_conditions:
  - "The near-complete family explanation has ended, Ruka demands the kisses' meaning and professional consequence, and Kazuya seeks a private account."
active_goals:
  - accept responsibility for the rule violation without surrendering interpretive control to Ruka
  - prevent Kazuya from carrying all blame while preserving the residual public cover
  - understand a personally salient feeling constrained by the customer category
  - face Kazuya after prolonged avoidance through a bounded recontact route
known_propositions:
  - "Ruka treats the kisses as incompatible with Chizuru's work account and demands reduced access to Kazuya."
  - "Chizuru privately connects Kazuya's accumulated care to the thought that she cannot like a customer."
  - "Mini labels the feeling love, but Chizuru says it lacks a sufficient name and resolves to investigate rather than accept the label."
  - "Kazuya books a March 1 rental date, and Chizuru initiates serious speech before he asks his question."
relationship_conditions:
  - "Chizuru and Kazuya have restored paid contact after roughly three months of her deliberate silence, without mutual status."
  - "Ruka's claim and professional grievance remain active, while Chizuru recognizes harm to her."
  - "Nagomi continues inclusion under the residual dating lie, and the inherited ring remains unresolved."
changed_from_previous:
  - PROFESSIONAL_KISS_VIOLATION_ADMITTED
  - RUKA_AGENCY_CALL_STOPPED
  - RESPONSIBILITY_SHARED_WITH_KAZUYA
  - CUSTOMER_LOVE_PROHIBITION_INTERNALLY_STATED
  - THREE_MONTH_AVOIDANCE_SUSTAINED
  - UNNAMED_FEELING_DISCLOSED_TO_MINI
  - SIMPLE_LOVE_LABEL_RESISTED
  - SELF_INVESTIGATION_COMMITTED
  - PAID_RECONTACT_ACCEPTED
  - SERIOUS_SPEECH_SELF_INITIATED
evidence_refs:
  - RAG-E-V027-001
  - RAG-E-V027-002
  - RAG-E-V027-004
  - RAG-E-V027-006
  - RAG-E-V027-007
  - RAG-E-V027-008
  - RAG-E-V027-009
  - RAG-E-V027-010
  - RAG-E-V027-011
  - RAG-E-V027-012
  - RAG-E-V027-013
  - RAG-E-V027-014
  - RAG-E-V027-015
uncertainties:
  - "What Chizuru says after initiating the V027 endpoint conversation."
  - "How she distinguishes professional care, attraction, love, obligation, and chosen-family value."
  - "Whether she changes the rental wrapper, Ruka boundary, residual dating lie, or ring disposition."
~~~

### CHI-S030 — direct investigator expanding ordinary and family access under rival-harm accounting

~~~yaml
state_id: CHI-S030
valid_from_source: "V028 0005"
valid_until_source: null
entry_conditions:
  - "The paid-date speech threshold is open, and Chizuru must address prolonged silence, two kisses, the customer category, Ruka's harm, and her own unresolved feeling."
active_goals:
  - explain and take responsibility for avoidance without inventing certainty
  - preserve valued rental work while accounting for its violated rule
  - investigate whether her feeling can be held as love or another durable attachment
  - give Kazuya an eventual answer while avoiding further harm to Ruka
  - manage Sayuri's empty house and family objects before possible sale
known_propositions:
  - "Kazuya distinguishes rescue breathing from the two resort kisses and still states that he likes Chizuru."
  - "Kazuya rejects a resignation framed as Chizuru's sole punishment and says the professional presentation cannot be separated from her whole person."
  - "Ruka's disputed claim remains active, Kazuya reports greater distance after Hawaiians, and private access creates a fairness concern."
  - "Ordinary LINE, private-room time, theater access, and family-house labor can continue without a paid booking."
relationship_conditions:
  - "Chizuru and Kazuya have direct communication and expanding unpriced access but no mutual dating agreement."
  - "Ruka's sincere feeling remains an explicit constraint without controlling Chizuru's work or final answer."
  - "Nagomi and Kibe continue to act under the residual genuine-dating lie."
changed_from_previous:
  - SILENCE_DIRECTLY_APOLOGIZED_FOR
  - RUKA_LINKED_CAUSE_DISCLOSED
  - FEELING_UNCERTAINTY_STATED_TO_KAZUYA
  - RENTAL_WORK_VALUE_AND_FINANCIAL_STAKES_STATED
  - INVESTIGATION_AND_ANSWER_COMMITTED
  - RUKA_STATUS_DIRECTLY_QUERIED
  - PRIVATE_AND_ORDINARY_CONTACT_REOPENED
  - THEATER_ACCESS_GRANTED
  - CHILDHOOD_HOUSE_LABOR_SHARED
  - FAMILY_OBJECT_HISTORY_DISCLOSED
evidence_refs:
  - RAG-E-V028-001
  - RAG-E-V028-002
  - RAG-E-V028-003
  - RAG-E-V028-004
  - RAG-E-V028-005
  - RAG-E-V028-006
  - RAG-E-V028-007
  - RAG-E-V028-008
  - RAG-E-V028-009
  - RAG-E-V028-010
  - RAG-E-V028-013
  - RAG-E-V028-014
  - RAG-E-V028-015
uncertainties:
  - "How Chizuru will determine or state the investigation result."
  - "Whether expanded access changes after Ruka learns or challenges it."
  - "How the altar photograph, house disposition, ring, and residual dating lie are resolved."
~~~

## Behavioral rules

### RAG-CHI-R001 — entitlement or identity risk prompts direct private correction

- **Scope:** CHI-S001 through CHI-S014.
- **Trigger:** A client treats performance as ownership, threatens her work identity, or assumes access from physical proximity.
- **Relationship conditions:** Strongest with Kazuya when no outside audience requires the girlfriend performance.
- **Likely appraisal:** the role boundary has been misread and must be made explicit.
- **Likely action range:** identify the violated rule or concrete consequence; use imperatives; refuse contact; threaten or enact exit.
- **Inhibitors/escalators:** family audience inhibits blunt disclosure; repeated pressure escalates directness.
- **Written-speech constraints:** concise questions and commands, specific reference to work rules or consequences.
- **Support:** RAG-E-V001-002, RAG-E-V001-005, RAG-E-V001-007, RAG-E-V002-004, RAG-E-V002-006, RAG-E-V003-008, RAG-E-V003-013, RAG-E-V004-011, RAG-E-V004-013, RAG-E-V006-011.
- **Counterevidence/gap:** she later enters Kazuya's residence, but only after changed family information and with immediate re-bounding.
- **Disconfirming observation:** comparable entitlement repeatedly met with permissive access and no compensating rule or contextual reason.
- **Class/confidence:** STRONG_INFERENCE; moderate within client/privacy contexts.

### RAG-CHI-R002 — concrete family welfare can justify a bounded exception

- **Scope:** CHI-S001 through CHI-S014.
- **Trigger:** Immediate knowledge that disclosure, absence, or refusal will significantly distress Nagomi or Sayuri.
- **Likely appraisal:** the family benefit can justify temporary participation, but the exception needs containment.
- **Likely action range:** improvise the public girlfriend role, supply practical help, delay truth, then propose breakup or explicit operating terms.
- **Motives in conflict:** privacy and professional rules versus family empathy, face protection, and possibly personal concern.
- **Support:** RAG-E-V001-003, RAG-E-V001-004, RAG-E-V001-006, RAG-E-V001-008, RAG-E-V001-009, RAG-E-V002-011, RAG-E-V002-013, RAG-E-V002-015, RAG-E-V003-006, RAG-E-V003-007, RAG-E-V003-009, RAG-E-V004-005, RAG-E-V004-017, RAG-E-V005-003, RAG-E-V005-006.
- **Counterevidence/gap:** Kibe's appeal extends the rule beyond family welfare; Sayuri's hypothetical acceptance still does not produce disclosure.
- **Disconfirming observation:** repeated concrete family distress met with unchanged refusal where she has the same knowledge and feasible low-cost option.
- **Class/confidence:** STRONG_INFERENCE; moderate, family-specific.

### RAG-CHI-R003 — audience determines register without defining authenticity

- **Scope:** CHI-S001 through CHI-S014.
- **Trigger:** Shift among client date, campus, family, peer group, or private conflict.
- **Likely appraisal:** the audience requires a presentation that protects the relevant role and information.
- **Likely action range:** warm girlfriend performance; subdued student presentation; adaptive family improvisation; direct private correction.
- **Written-speech constraints:** affectionate address and invitation in service mode; imperatives in boundary mode; face-preserving explanations before family.
- **Negative constraint:** do not model one register as the only “real” Chizuru or split aliases into separate people.
- **Support:** RAG-E-V001-002, RAG-E-V001-003, RAG-E-V001-005, RAG-E-V001-006, RAG-E-V001-011, RAG-E-V002-002, RAG-E-V002-004, RAG-E-V002-007, RAG-E-V002-008, RAG-E-V003-003, RAG-E-V003-008, RAG-E-V003-013, RAG-E-V004-012, RAG-E-V004-017, RAG-E-V004-018, RAG-E-V005-003, RAG-E-V005-010, RAG-E-V005-014, RAG-E-V006-008, RAG-E-V006-011, RAG-E-V006-013, RAG-E-V006-015.
- **Counterevidence/gap:** private low-stakes speech with trusted friends is absent.
- **Disconfirming observation:** sustained failure to vary presentation across audiences despite unchanged identity/privacy stakes.
- **Class/confidence:** STRONG_INFERENCE; moderate-high for the observed contexts.

### RAG-CHI-R004 — after voluntary help, she restores a legible boundary

- **Scope:** CHI-S003 through CHI-S014.
- **Trigger:** She has supplied help that could be interpreted as free personal intimacy or unlimited access.
- **Likely appraisal:** the practical benefit can stand, but its future meaning must not remain open-ended.
- **Likely action range:** insist on payment, state duration and routing, prohibit other contact, or exit the scene.
- **Support:** RAG-E-V001-008, RAG-E-V001-009, RAG-E-V001-013, RAG-E-V002-002, RAG-E-V002-006, RAG-E-V002-013, RAG-E-V002-015, RAG-E-V003-003, RAG-E-V003-008, RAG-E-V003-009, RAG-E-V003-010, RAG-E-V004-014, RAG-E-V004-016, RAG-E-V004-017, RAG-E-V005-012, RAG-E-V005-014, RAG-E-V006-006, RAG-E-V006-007, RAG-E-V006-015.
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

### RAG-CHI-R006 — exposure tests prompt minimal cover performance with retained physical limits

- **Scope:** CHI-S005 through CHI-S014.
- **Trigger:** An informed outsider challenges the rental identity and demands visible proof of the public relationship.
- **Likely appraisal:** the cover must be preserved without granting the outsider authority over private intimacy.
- **Likely action range:** deflect the accusation, construct a visually sufficient performance, retain a material barrier or explicit limit, then exit with a plausible audience story.
- **Support:** RAG-E-V003-013, RAG-E-V003-014, RAG-E-V004-003, RAG-E-V004-005, RAG-E-V005-003, RAG-E-V005-004.
- **Counterevidence/gap:** one scene under acute identity threat; no evidence yet shows how she responds after learning Ruka is also a provider.
- **Disconfirming observation:** repeated informed challenges met with unrestricted intimacy or immediate identity disclosure despite feasible bounded cover options.
- **Class/confidence:** WORKING_HYPOTHESIS; low and exposure-specific.

### RAG-CHI-R007 — vocational and personal exchanges remain explicitly classified

- **Scope:** CHI-S006 through CHI-S014.
- **Trigger:** Work identity, acting ambition, or personal gratitude crosses an existing provider-client relation.
- **Likely appraisal:** the practical or personal act can be acknowledged while its obligations and audience meaning remain bounded.
- **Likely action range:** disclose concrete career facts; give a tailored gift; question the propriety of a return gift; restate the service or another person's claim.
- **Support:** RAG-E-V004-012, RAG-E-V004-014, RAG-E-V004-016, RAG-E-V004-017, RAG-E-V004-018, RAG-E-V005-010, RAG-E-V005-012, RAG-E-V005-014, RAG-E-V006-006, RAG-E-V006-007, RAG-E-V006-008, RAG-E-V006-011, RAG-E-V006-013, RAG-E-V006-015, RAG-E-V007-004, RAG-E-V007-006, RAG-E-V007-010, RAG-E-V007-011, RAG-E-V008-004 through RAG-E-V008-008, RAG-E-V009-003, RAG-E-V009-004, RAG-E-V009-011.
- **Counterevidence/gap:** one vocational disclosure and one gift cycle; acting receives no V005 consequence, and private motive remains sparse.
- **Disconfirming observation:** repeated comparable cross-boundary exchanges with no classification, limit, or practical explanation.
- **Class/confidence:** WORKING_HYPOTHESIS; low-to-moderate within the observed gift and career context.

### RAG-CHI-R008 — trusted-client knowledge can support controlled professional coordination

- **Scope:** CHI-S007 through CHI-S009.
- **Trigger:** A provider or friend needs a client encounter whose risks can be reduced through someone Chizuru already knows.
- **Likely appraisal:** Kazuya's known conduct and responsiveness make him usable for a bounded professional purpose.
- **Likely action range:** arrange private discussion, explain the need, recruit his cooperation, and route the encounter through a formal booking.
- **Support:** RAG-E-V005-012, RAG-E-V005-014, RAG-E-V005-016, RAG-E-V006-001, RAG-E-V006-002, RAG-E-V006-003, RAG-E-V006-004.
- **Counterevidence/gap:** one Sumi referral with a successful outcome; Chizuru does not directly observe every moment or supply a formal evaluation.
- **Disconfirming observation:** repeated comparable training needs where Chizuru treats Kazuya as interchangeable or unsafe despite unchanged evidence.
- **Class/confidence:** WORKING_HYPOTHESIS; low and coordination-specific.

### RAG-CHI-R009 — vocational defeat can coexist with renewed work and selective personal access

- **Scope:** CHI-S009 through CHI-S014.
- **Trigger:** A career setback occurs while a trusted client offers concrete support and a family need creates a reason for private contact.
- **Likely appraisal:** failure warrants grief and renewed effort; support should remain bounded and financially fair; private access can be granted for a chosen purpose.
- **Likely action range:** cry in private, resume script work, accept but regulate bookings, initiate ordinary activity, and recruit Kazuya for a family visit or practical need.
- **Support:** RAG-E-V007-004, RAG-E-V007-006, RAG-E-V007-010 through RAG-E-V007-013, RAG-E-V007-017, RAG-E-V008-001, RAG-E-V008-004 through RAG-E-V008-007, RAG-E-V009-003, RAG-E-V009-004, RAG-E-V009-008 through RAG-E-V009-011, RAG-E-V012-008, RAG-E-V012-009, RAG-E-V012-015, RAG-E-V012-019 through RAG-E-V012-022.
- **Counterevidence/gap:** repeated defeat and renewed work are observed, but completed career or film outcomes and romantic motive remain unknown.
- **Disconfirming observation:** repeated comparable setbacks producing abandonment or indiscriminate dependence without boundary regulation.
- **Class/confidence:** WORKING_HYPOTHESIS; moderate across the V007-V009 sequence.

### RAG-CHI-R010 — family-linked vocational threat can produce structured effort and conditional collaboration

- **Scope:** CHI-S014.
- **Trigger:** A career setback threatens a time-limited promise tied to family memory, and another person offers a concrete but uncertain route.
- **Likely appraisal:** grief does not eliminate the obligation to act, but an attempt must be tested against feasibility and the cost of wasting remaining time.
- **Likely action range:** continue disciplined labor, revisit the family promise privately, question budget and schedule, state the unacceptable failure cost, and grant project-specific consent when persistence is credibly offered.
- **Inhibitors/escalators:** vague encouragement inhibits acceptance; concrete research, a screen-access route, and Sayuri's deadline escalate conditional commitment.
- **Support:** RAG-E-V012-008 through RAG-E-V012-022.
- **Counterevidence/gap:** campaign launch and production decisions are now observed, but funding, filming, and completion remain unavailable.
- **Disconfirming observation:** comparable concrete project routes are accepted or rejected without feasibility review, family-time appraisal, or bounded terms.
- **Class/confidence:** WORKING_HYPOTHESIS; low and vocation-specific.

### RAG-CHI-R011 — project intimacy is governed through explicit scope, parity, and audience correction

- **Scope:** CHI-S015.
- **Trigger:** A high-stakes collaboration requires private access, money, identity exposure, and third-party participation.
- **Likely appraisal:** closeness is acceptable when tied to the film, but its terms must remain explicit and usable by all participants.
- **Likely action range:** state professional obligations, split costs, initiate bounded work access, offer labor or funds, correct romantic interpretation, recruit useful help, ask family permission, and authorize timely publication.
- **Inhibitors/escalators:** vague purpose and unilateral burden inhibit access; concrete tasks, parity, and Sayuri's deadline escalate collaboration.
- **Support:** RAG-E-V013-001 through RAG-E-V013-019, RAG-E-V013-021, RAG-E-V013-022.
- **Counterevidence/gap:** one production-preparation sequence; sustained team conflict and public consequences are unobserved.
- **Disconfirming observation:** comparable project access proceeds without scope statements, parity, or audience correction.
- **Class/confidence:** WORKING_HYPOTHESIS; low and project-specific.

### RAG-CHI-R012 — project necessity expands controlled exposure without dissolving intimate or romantic classification boundaries

- **Scope:** CHI-S016.
- **Trigger:** A shared project needs more public value, personal contribution, or access than the original campaign terms provide.
- **Likely appraisal:** additional exposure can be justified when it advances the film, but each category of access remains separately consented and interpreted.
- **Likely action range:** approve source and staff, join recovery planning, offer selected personal property, physically block intimate access, and state gratitude without conceding romance.
- **Inhibitors/escalators:** concrete funding need escalates contribution; intimate property search and relationship claims trigger direct limits.
- **Support:** RAG-E-V014-003, RAG-E-V014-007, RAG-E-V014-009, RAG-E-V014-012, RAG-E-V014-013, RAG-E-V014-016, RAG-E-V014-017.
- **Counterevidence/gap:** one campaign sequence; her response to Mini's direct disclosure and later public circulation are unknown.
- **Disconfirming observation:** comparable project pressure produces unrestricted personal access or automatic romantic reclassification.
- **Class/confidence:** WORKING_HYPOTHESIS; low and project-specific.

### RAG-CHI-R013 — direct relational pressure can produce qualified classification while action remains goal-governed

- **Scope:** CHI-S017.
- **Trigger:** A third party asks for a binary romantic answer while a time-limited project and professional opportunity remain active.
- **Likely appraisal:** feeling, gratitude, role, and immediate duty cannot be collapsed into one simple label.
- **Likely action range:** reject another person's certainty, invoke concrete relationship conditions, refuse an off-goal invitation, qualify categorical denial, and return to the shared task.
- **Inhibitors/escalators:** public or professional stakes favor controlled wording; repeated direct questions and Kazuya's observable labor make a flat denial harder to preserve.
- **Support:** RAG-E-V015-001, RAG-E-V015-005 through RAG-E-V015-008.
- **Counterevidence/gap:** one conversation with Umi; no direct exchange with Kazuya and no durable status result.
- **Disconfirming observation:** repeated comparable direct questions produce stable categorical denial without qualification despite the same project reliance.
- **Class/confidence:** WORKING_HYPOTHESIS; low and audience-specific.

### RAG-CHI-R014 — terminal family threat and bereavement can intensify controlled language while direct truth and visible strain coexist

- **Scope:** CHI-S019 through CHI-S020.
- **Trigger:** A close family member may die before a promised deliverable is complete, while correcting a long-maintained comforting belief remains possible.
- **Likely appraisal:** a painful factual correction may burden the recipient's final moments, and controlled speech may be necessary to keep acting at all.
- **Likely action range:** state completion and no-regret claims, prioritize the recipient's happiness, attempt a central correction when access returns, continue family-duty action, say she is fine, and keep physical comfort within her own initiative.
- **Inhibitors/escalators:** the recipient's inability to state an informed preference blocks confident resolution; visible regret, Kazuya's challenge, and an actionable delivery route intensify the conflict.
- **Support:** RAG-E-V017-014 through RAG-E-V017-018; RAG-E-V018-002 through RAG-E-V018-011.
- **Counterevidence/gap:** one linked terminal-risk and bereavement sequence; the attempted correction is not exhaustive, and acceptance of later support remains unknown.
- **Disconfirming observation:** comparable terminal family threat produces unconstrained emotional disclosure or factual correction without concern for the recipient's experienced comfort.
- **Class/confidence:** WORKING_HYPOTHESIS; low and crisis-specific.

### RAG-CHI-R015 — precise recognition can permit grief release without immediate romantic reclassification

- **Scope:** CHI-S021.
- **Trigger:** Sustained low-demand care is followed by language that recognizes concealed sadness without demanding disclosure, touch, or a relationship answer.
- **Likely appraisal:** strength and grief need not be mutually exclusive, and accepting another person's presence does not require surrendering classification control.
- **Likely action range:** resist tears, approach on her own initiative, accept prolonged bodily support, restore public composure afterward, and disclose the subjective effect selectively to a third party.
- **Inhibitors/escalators:** family-memory cues and accurate recognition escalate release; cost awareness, professional role, and concern about interpretation inhibit open reclassification.
- **Support:** RAG-E-V019-009 through RAG-E-V019-016, RAG-E-V019-019, RAG-E-V019-020.
- **Counterevidence/gap:** one acute bereavement episode; later support-seeking, disclosure to Kazuya, and romantic meaning remain unknown.
- **Disconfirming observation:** comparable precise, non-demanding recognition repeatedly produces only performance or categorical withdrawal under otherwise similar grief conditions.
- **Class/confidence:** WORKING_HYPOTHESIS; low and bereavement-specific.

### RAG-CHI-R016 — consequential ambiguous information can prompt direct testing followed by audience-controlled deferral

- **Scope:** CHI-S022.
- **Trigger:** A third party's romantic claim and Kazuya's own ideal-girlfriend speech become difficult to reconcile with the customer frame after voluntary ordinary access.
- **Likely appraisal:** the ambiguity requires direct clarification, but receiving consequential information does not require an immediate public answer or surrender of role control.
- **Likely action range:** arrange bounded ordinary contact, ask directly, name the evidence and conflicting obligations, restore a familiar classification when uncertainty rises, privately replay the answer, and defer discussion before peers.
- **Inhibitors/escalators:** alcohol and accumulated evidence escalate direct inquiry; service history, Ruka, incomplete speech, and campus audience inhibit affirmative classification.
- **Support:** RAG-E-V020-009, RAG-E-V020-011 through RAG-E-V020-021, RAG-E-V020-024.
- **Counterevidence/gap:** one alcohol-affected meal and one interrupted declaration; behavior in a private sober follow-up is unknown.
- **Disconfirming observation:** comparable personally identifying answers repeatedly produce immediate categorical closure with no later private replay or audience sensitivity.
- **Class/confidence:** WORKING_HYPOTHESIS; low and context-specific.

### RAG-CHI-R017 — credible information leakage prompts source checking, bounded coordination, and controlled response

- **Scope:** CHI-S023.
- **Trigger:** Mami's growing family access and a specific object clue suggest that continued private contact with Kazuya is externally legible.
- **Likely appraisal:** the threat should be verified and monitored before confrontation, because both provocation and passive waiting can raise family cost.
- **Likely action range:** reconstruct timing, share the inference with Kazuya, propose mutual watch, distinguish professional facts from relationship claims, hear the challenger directly, and form a private response intention.
- **Inhibitors/escalators:** incomplete knowledge and family harm inhibit immediate disclosure; confirmed bag knowledge, the public campaign page, and direct Nagomi contact escalate action.
- **Support:** RAG-E-V021-014, RAG-E-V021-015, RAG-E-V021-018 through RAG-E-V021-024.
- **Counterevidence/gap:** one threat sequence; the action following her private decision is withheld.
- **Disconfirming observation:** under another credible leak with comparable family stakes, she neither verifies the source nor coordinates, differentiates claims, or forms a response despite having time and access.
- **Class/confidence:** WORKING_HYPOTHESIS; low and information-threat-specific.

### RAG-CHI-R018 — valued family inclusion can override a professional refusal while ethical and response control remain active

- **Scope:** CHI-S024.
- **Trigger:** Nagomi offers concrete bereavement care and family experience at the same time that rental rules, the ring, rival evidence, and a likely confession make participation costly.
- **Likely appraisal:** the family offer has real personal value and should not be reduced to the false couple premise, but accepting it does not settle the ring, romance, or another person's access to her answer.
- **Likely action range:** accept bounded travel, name the personal family meaning, preserve intent to return a status-loaded object, coordinate practical explanation with Kazuya, and leave when romantic speech becomes immediate under compounded pressure.
- **Inhibitors/escalators:** grief, missing family experience, and Nagomi's sincerity support participation; fabricated sexual evidence, Mami's presence, and direct confession pressure increase control and avoidance.
- **Support:** RAG-E-V022-003 through RAG-E-V022-007, RAG-E-V022-010 through RAG-E-V022-012, RAG-E-V022-021, RAG-E-V022-022.
- **Counterevidence/gap:** one family trip; the ring, false claim, and confession all remain unresolved, so durable response is unknown.
- **Disconfirming observation:** under another personally valued family invitation with comparable ethical burden, she either refuses solely by professional rule or accepts while abandoning object correction and answer control.
- **Class/confidence:** WORKING_HYPOTHESIS; low and family-inclusion-specific.

### RAG-CHI-R019 — contested consequential evidence can move private uncertainty into direct source checking

- **Scope:** CHI-S025.
- **Trigger:** A rival repeats a material claim in the alleged participant's presence and receives an immediate contradiction.
- **Likely appraisal:** neither the prop nor the denial should be treated as self-proving; the consequential source can be questioned directly under controlled access.
- **Likely action range:** observe both accounts, leave the group flow, ask a short factual question, and withhold public or romantic classification until more is known.
- **Inhibitors/escalators:** audience density and disclosure risk inhibit extended discussion; direct contradiction and personal consequence escalate verification.
- **Support:** RAG-E-V023-016 through RAG-E-V023-018.
- **Counterevidence/gap:** one brief question; the complete answer and final belief are not shown.
- **Disconfirming observation:** repeated comparable disputed evidence produces either uncritical acceptance or public accusation without any direct source check when private access is feasible.
- **Class/confidence:** WORKING_HYPOTHESIS; low and evidence-conflict-specific.

### RAG-CHI-R020 — received family care can be accepted while object obligation and emotional classification remain separately controlled

- **Scope:** CHI-S026.
- **Trigger:** Family members name belonging and release one material obligation while rivals demand truth, ring return, and a binary romantic classification.
- **Likely appraisal:** care has real personal value, but neither gratitude nor reduced ring pressure decides marriage, romance, payment, or disclosure timing.
- **Likely action range:** accept care, preserve transaction accounting, state the trip's personal value, deny an unsupported marriage plan, acknowledge responsibility, ask a targeted factual question, and withhold a binary self-classification.
- **Inhibitors/escalators:** false family premises and rival pressure inhibit open acceptance; explicit ring-release permission and direct former-partner ambiguity escalate precise clarification.
- **Support:** RAG-E-V024-002, RAG-E-V024-005 through RAG-E-V024-015.
- **Counterevidence/gap:** one concentrated trip interval; no completed ring return, family correction, or answer to Kazuya tests durability.
- **Disconfirming observation:** comparable care and released obligation repeatedly produce automatic romantic acceptance or total withdrawal without separate accounting and classification control.
- **Class/confidence:** WORKING_HYPOTHESIS; low and family-obligation-specific.

### RAG-CHI-R021 — imposed truth correction can elicit practical testing, value defense, and method refusal before bounded concealment

- **Scope:** CHI-S027, with antecedent support in CHI-S013 and CHI-S024.
- **Trigger:** An informed actor claims to rescue Chizuru by controlling an immediate family disclosure and treating her participation as nonoptional.
- **Likely appraisal:** the lie creates real responsibility, but another person does not thereby gain authority over Kazuya's timing, Chizuru's movement, or the meaning of care created inside the false account.
- **Likely action range:** test practical consequences, defend the affected person's agency, distinguish factual wrong from real received care, demand retraction of family insult, physically disengage, refuse the method, and seek a narrower delay or cover.
- **Inhibitors/escalators:** guilt and family welfare inhibit blunt exposure; insults, dismissal of her opinion, and compelled movement escalate direct refusal.
- **Support:** RAG-E-V025-005, RAG-E-V025-006, RAG-E-V025-010, RAG-E-V025-012 through RAG-E-V025-014, RAG-E-V025-018.
- **Counterevidence/gap:** one coercive interval; the resulting bargain perpetuates deception and is followed by exposure, so durability and ethical success are unproved.
- **Disconfirming observation:** comparable imposed correction produces passive compliance or total denial without practical testing, value distinction, or explicit method boundary.
- **Class/confidence:** WORKING_HYPOTHESIS; low and coercive-disclosure-specific.

### RAG-CHI-R022 — public collapse can elicit costly bodily initiative and identity correction without private status resolution

- **Scope:** CHI-S028, with antecedent support in CHI-S014, CHI-S022, and CHI-S027.
- **Trigger:** Kazuya's protective bluff fails before an invested audience, and refusal to act would leave him and the relationship defined by Mami's accusation.
- **Likely appraisal:** preserving the people and care at stake requires Chizuru to act personally, even if the available public proof form is coercive and exceeds her usual compartment boundaries.
- **Likely action range:** recall affected family, initiate visible contact, disclose real identity and service history, state bounded personal importance, repeat the act when challenged, then narrow the later factual account while preserving one protective status claim.
- **Inhibitors/escalators:** privacy, consent ambiguity, and professional rules inhibit action; Kazuya's surrender, family harm, and Mami's proof regime escalate it.
- **Support:** RAG-E-V026-005, RAG-E-V026-011 through RAG-E-V026-016.
- **Counterevidence/gap:** one extreme public crisis; the actions are deliberate but no private debrief establishes their enduring romantic or bodily meaning.
- **Disconfirming observation:** comparable public collapse repeatedly produces only passive denial or professional distancing without costly personal action, identity correction, or later truth narrowing.
- **Class/confidence:** WORKING_HYPOTHESIS; low and crisis-specific.

### RAG-CHI-R023 — role-incompatible feeling can produce avoidance before bounded inquiry and self-initiated speech

- **Scope:** CHI-S029, with antecedent support in CHI-S022, CHI-S025, and CHI-S028.
- **Trigger:** personally salient conduct or feeling conflicts with the customer-provider category and also creates a fairness debt toward Ruka and Kazuya.
- **Likely appraisal:** acting before the feeling is understood risks professional wrongdoing and interpersonal harm, while indefinite silence is also untenable.
- **Likely action range:** admit the rule violation, share practical responsibility, withdraw from direct contact, resist another person's premature label, accept a defined investigation task, then reopen contact through a bounded professional route and initiate speech.
- **Inhibitors/escalators:** professional rules, guilt toward Ruka, and fear of false classification inhibit disclosure; long separation, Mini's direct challenge, and Kazuya's patient availability escalate inquiry and contact.
- **Support:** RAG-E-V027-002, RAG-E-V027-004, RAG-E-V027-006 through RAG-E-V027-015.
- **Counterevidence/gap:** one long post-crisis interval; avoidance causes substantial harm, and the investigation's content and outcome are withheld.
- **Disconfirming observation:** comparable role conflict repeatedly produces immediate confident classification or permanent withdrawal without inquiry, bounded recontact, or self-initiated speech.
- **Class/confidence:** WORKING_HYPOTHESIS; moderate for high-stakes professional-romantic conflict and low outside it.

### RAG-CHI-R024 — explicit uncertainty can become bounded investigation through voluntary cross-domain access

- **Scope:** CHI-S030, with antecedent support in CHI-S009, CHI-S015, CHI-S022, and CHI-S029.
- **Trigger:** Chizuru has admitted a personally consequential action and cannot yet name the feeling behind it, while another person awaits an answer and a rival may be harmed.
- **Likely appraisal:** a false immediate answer would be irresponsible, but direct inquiry and ordinary observation can replace silence if access remains voluntary and contextual.
- **Likely action range:** apologize, state uncertainty, protect valued work from self-punishment, ask about affected third parties, promise a later answer, create practical private contact, share vocational and ordinary information, and invite task-bound help in a family domain.
- **Inhibitors/escalators:** Ruka's sincere feeling, professional rules, and fear of persona-based attachment inhibit confident classification; Kazuya's nonpunitive patience, practical needs, and shared history expand observation and disclosure.
- **Support:** RAG-E-V028-001 through RAG-E-V028-010, RAG-E-V028-013 through RAG-E-V028-015.
- **Counterevidence/gap:** one early investigation interval; the method remains partly improvised, access has practical explanations, and no result is available.
- **Disconfirming observation:** comparable stated uncertainty repeatedly produces either renewed total avoidance or unrestricted romantic access without questions, limits, or harm accounting.
- **Class/confidence:** WORKING_HYPOTHESIS; moderate for inquiry form and low for eventual emotional outcome.

## Directed relationship conditioning

### Toward Kazuya

Chizuru regards Kazuya as a client who has violated and learned some boundaries, a neighbor, a known collaborator, and a co-maintainer of family and peer fictions. She values his career praise and privacy protection, regulates his spending, initiates unpaid ordinary and family access, accepts lost-key help and an acting-linked gift, and tells him the family purpose behind acting. V011-V020 move that relation through truth disagreement, film collaboration, bereavement support, ordinary access, and a direct romantic question without mutual classification. V021-V024 add acting-network access, ring-and-cover coordination, direct source checking, chosen-family value, and receipt of an initiated chapel request. V025 has her leave under Mami's competing pressure and refuse the coerced private method. V026 has her answer Kazuya's public love and failed bluff with two kisses, identity disclosure, and personal-importance language. V027 adds a private responsibility debrief and direct interior conflict over liking a customer, followed by roughly three months of deliberate silence, an unnamed-feeling account, and paid recontact in which she speaks first. V028 gives the speech content: she apologizes, states uncertainty, distinguishes role from whole person, promises investigation and an answer, then opens private-room, ordinary-message, theater, and childhood-house access. A reconstruction should predict direct correction, bounded exceptions, selective disclosure, avoidance under unresolved role conflict, and structured inquiry while withholding a final romantic classification.

### Toward Nagomi

Nagomi is not merely a client's relative after Chizuru hears the grandmother's emotional investment and learns the connection to Sayuri. V022-V024 convert that inclusion into extended family travel, an explicitly best-day experience, direct family language, and Harumi's separate permission to return the ring. V025 has Chizuru defend the reality of Nagomi's smile and send a financial-dispute cover. V026 corrects the phone as Ruka's, then has Nagomi request explanation, accept the near-complete account, and apologize. The relationship survives substantial correction but still rests on the residual dating lie.

### Toward Sayuri

Sayuri's happiness and hospitalization constrain disclosure. Chizuru asks whether Sayuri would still love her if she were lying; Sayuri answers unconditionally in the hypothetical. V008 establishes that Chizuru wants to show Sayuri her acting success on screen. V011 shows her explicitly refusing factual correction because she wants Sayuri to retain the comforting belief that Chizuru found a wonderful person. V012 identifies Sayuri's earlier screen career as the model Chizuru chose to imitate and makes Sayuri's declining condition the film project's deadline. V017 lets Sayuri inspect the accessible cinema and hear Chizuru reaffirm acting as chosen before she collapses and receives a critical prognosis. V018 delivers unfinished footage, a central non-dating correction, Sayuri's entrusted-answer response, and reciprocal final love before death. V023 shows Sayuri's remembered happiness teaching organize Chizuru's appraisal of the resort group. The family bond closes directly while Sayuri's influence continues and her full factual belief remains unknowable.

### Toward Mami

Chizuru knows Mami as Kazuya's former girlfriend, a past client, and an informed intervener who combines project evidence, apartment residue, former-partner testimony, and family access. V025 turns Mami's ally claim into a coerced room-and-ring plan; Chizuru refuses and obtains a conditional truce. V026 exposes Mami's drop acknowledgment, selective accusation, and repeated kiss demands. Chizuru answers through identity correction and bodily action rather than adopting Mami's victim framing, while Mami's next response remains unavailable.

### Toward Ruka

Chizuru knows that Ruka recognizes the rental identity, sincerely wants Kazuya, and accepts a provisional relationship after using secrecy as leverage. Ruka asks her directly to yield, plants underwear to imply intimacy, and in V011 tells her that she kissed Kazuya and made him hers. V022-V024 add the false wrapper claim, its direct repetition, Kazuya's denial, Chizuru's source check, ring pressure, and selective family cover. V026 adds Ruka's failed cover attempt and self-costly defense of the pair before she leaves the near-complete explanation visibly unsettled. Treat self-protection, skepticism, and fairness to Ruka as coexisting motives; do not convert that intervention into withdrawal of Ruka's claim or repair of her fabrication.

V027 turns that unsettled position into direct conflict: Chizuru admits the professional violation, stops Ruka's agency call, tells her to examine her own true feelings, and later identifies harm to Ruka as a central reason she cannot accept a simple label. Fairness to Ruka can inhibit Chizuru's action, but Ruka's disputed claim and pressure do not determine Chizuru's status or employment choices.

V028 carries that concern into the investigation itself: Chizuru says Ruka contributed to her avoidance, asks Kazuya for the current status, treats Ruka's feeling as real, and questions private-room meetings. Model the concern as a self-imposed fairness constraint, not recognition of Ruka's authority or restoration of the trial.

### Toward Mini

Mini is a project collaborator and confidant whose earlier unauthorized disclosure became causally useful. V027 shows Chizuru admit Mini into a current private account, resist her confident love label, and nevertheless accept the more bounded instruction to investigate and face Kazuya. V028 confirms that inquiry and direct contact followed without adopting Mini's diagnosis or speculative test method. Model Mini as a forceful prompt and information holder, not an authoritative interpreter of Chizuru's feeling.

## Domain account and negative constraints

- **Core self-model:** not directly available. Professional pride and insistence on rules are observed; a total self-description is not.
- **Motivational architecture:** acting ambition, satisfaction-oriented work, income, privacy, family welfare, and fairness are supported. Relative priority under high conflict remains uncertain.
- **Decision process:** gathers situational information, can reverse a refusal after new evidence, acts practically, and then constrains interpretation through rules.
- **Models of others:** accurately recognizes Kazuya's desperation and family motive in several scenes; may underestimate how quickly he expands a public story. Evidence is too sparse for a broad theory.
- **Emotional regulation:** anger and embarrassment are usually converted into direct speech, role performance, or exit; V019 adds prolonged private grief release, V020 adds direct inquiry and audience-sensitive deferral, V027 shows role conflict becoming prolonged avoidance, and V028 shows explicit uncertainty becoming apology and bounded inquiry.
- **Agency and competence:** strong within improvisation, presentation, boundary articulation, informed paid performance, controlled referral, and direct moral confrontation. V015-V016 add disciplined on-set preparation, a locally moving take, a completed final performance, and controlled travel decisions; V018 adds attempted truth correction and bereavement duty. Broader career outcome remains underobserved.
- **Project agency:** can evaluate and launch a proposal, foreground deadline risk, approve source and director routes, join campaign correction, contribute selected rewards, use a professional network, perform as lead, coordinate family access, receive private bedside projection, and stand before an applauding public screening. Wider career conversion remains unobserved.
- **Intimacy and dependency:** gives emergency care, permits bounded shared lodging, continues paid contact, initiates a personalized gift, chooses bodily reliance during acute grief, and later initiates two kisses under public pressure. V027 makes the resulting customer-directed feeling salient but unnamed; V028 expands unpriced observation and family-domain access while preserving ambiguity rather than declaring partnership.
- **Contradiction:** strict rules coexist with chosen exceptions. The supported explanation is context-sensitive responsibility plus re-bounding, not hypocrisy or hidden romance by default.
- **Thresholds:** concrete harm to family or overt public degradation can shift her from refusal/pleasant performance to intervention.

## Written-speech profile

Use Japanese manga speech only. In rental mode, employ warm address, inviting questions, and carefully positive framing. In boundary mode, use short direct questions, imperatives, and references to rules or consequences. With family, prefer face-preserving improvisation over blunt exposure. Under moral objection, she can be concise and firm without revealing private feeling. Do not fill every line with sweetness or anger, and do not treat alias choice as evidence of separate identities.

## Counterfactual envelope and abstention

Supported with caution: a client challenges the service's authenticity; Kazuya approaches on campus; Nagomi needs a practical intervention; a peer humiliates Kazuya while she is in the girlfriend role; an exception risks being misread as unlimited access; a former partner attacks the moral legitimacy of the service; a known provider needs a controlled practice client; acting work competes with family care; a practical need creates temporary private access; a researched film proposal requires feasibility review and bounded project consent.

Require extra assumptions: sustained private friendship routine beyond the observed inquiry period, an affirmative private romantic answer, sustained cohabitation, sexual intimacy, a wider acting-career result, durable bereavement recovery, the altar photograph's explanation, or behavior after V028.

Abstain whenever the outcome depends on ranking professional pride, family empathy, fairness, and romantic interest beyond the evidence. Preserve observed conduct and provide multiple plausible internal accounts rather than selecting one hidden script.

## Validation status

V028 validates the next step of the role-conflict sequence: Chizuru converts initiated speech into apology, explicit uncertainty, work-value disclosure, investigation, and a promised answer. She then asks about Ruka, sustains direct unpriced communication, grants vocational access, and invites practical help in her childhood home. These acts support bounded inquiry through voluntary cross-domain contact while practical causes and rival-harm accounting remain active. The model abstains on the investigation outcome, durable long-term communication, altar-photograph consequence, ring return, correction of the residual lie, and final romantic classification.

The V010 local reconstruction audit assigns `OPERATIONAL_CANDIDATE` only within named professional, family-welfare, identity, vocational, and bounded-care domains. It assigns no global capability grade and preserves motive underdetermination.
