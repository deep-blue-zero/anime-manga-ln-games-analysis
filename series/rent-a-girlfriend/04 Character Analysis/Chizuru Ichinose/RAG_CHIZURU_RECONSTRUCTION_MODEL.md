---
title: "Rent-a-Girlfriend - Chizuru Ichinose Reconstruction Model"
artifact_id: RAG_CHIZURU_RECONSTRUCTION_MODEL
artifact_type: character_reconstruction_model
series: Rent-a-Girlfriend
generation: V1
version: "1.8"
status: canonical
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
created: "2026-09-19"
source_boundary: "Operational model based only on Japanese manga witnesses RAG-JP-EPUB-V001-V009."
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
  admitted_through_volume: V009
  narrative_time_boundary: "after Chizuru accepts an acting-linked gift, provides bounded hangover care, and recognizes Mami during a rental date on the train"
  basis_checkpoint: null
  basis_commit: 202e88180ffa41f2e6c238e7baf2902e48676998
  model_revision: "1.7"
  prior_knowledge_limitations:
    - "No post-V009 narrative evidence is admitted."
    - "Interiority is sparse; motives are modeled at minimum warranted strength."
    - "Chizuru's response to Kazuya's direct preference statement is not shown."
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
  missing_contexts:
    - sustained study and friendships
    - explicit romantic self-report
    - long-term acting and rental-work practice
    - acknowledged reciprocal partnership
    - broad private routine
  translation_limitations:
    - "Model derives from the Japanese witness; no licensed translation was admitted for comparison."
  written_speech: PARTIALLY_MODELED
  performed_voice: OUT_OF_SCOPE
local_readiness: PARTIAL_MODEL
~~~

## Intended use

This model supports narrow reconstruction of Chizuru at the V009 endpoint when professional rules, family welfare, privacy, audience management, public unfairness, informed paid work, family-linked acting purpose, practical gifts, or bounded unpaid care are salient. Because the manga rarely supplies her interior narration, the model predicts action ranges from conduct and speech rather than inventing a hidden monologue. It must abstain on romantic feeling, later career outcomes, intimate partnership, Mami's next action, and unseen ordinary preferences.

## Central mechanism

Chizuru manages competing obligations through compartmentalization and bounded exceptions. She can perform warmth as skilled labor, protect a separate campus identity, and speak bluntly when a client threatens those boundaries. When new information reveals a concrete family or dignity cost, she may revise an earlier refusal. She then tends to specify a rule, payment frame, audience story, or exit that limits what the exception means.

The minimum supported motive is responsive responsibility organized around work, privacy, family, and a named vocational project. Professional pride, acting practice, income, the wish to show Sayuri her success, fairness toward Kazuya and Ruka, protection of her own work, and possible personal investment can all contribute. V005 shows informed performance and professional coordination. V006 validates the Sumi referral and makes acting a possible reason to leave rental work. V007-V009 add career defeat, renewed work, selective private access, a first-person family account, an accepted practical gift, and substantial care followed by verbal rebounding. None of the nine volumes justifies selecting romance as the hidden master explanation or treating professional conduct as emotionally unreal.

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
valid_until_source: null
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

## Behavioral rules

### RAG-CHI-R001 — entitlement or identity risk prompts direct private correction

- **Scope:** CHI-S001 through CHI-S011.
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

- **Scope:** CHI-S001 through CHI-S008.
- **Trigger:** Immediate knowledge that disclosure, absence, or refusal will significantly distress Nagomi or Sayuri.
- **Likely appraisal:** the family benefit can justify temporary participation, but the exception needs containment.
- **Likely action range:** improvise the public girlfriend role, supply practical help, delay truth, then propose breakup or explicit operating terms.
- **Motives in conflict:** privacy and professional rules versus family empathy, face protection, and possibly personal concern.
- **Support:** RAG-E-V001-003, RAG-E-V001-004, RAG-E-V001-006, RAG-E-V001-008, RAG-E-V001-009, RAG-E-V002-011, RAG-E-V002-013, RAG-E-V002-015, RAG-E-V003-006, RAG-E-V003-007, RAG-E-V003-009, RAG-E-V004-005, RAG-E-V004-017, RAG-E-V005-003, RAG-E-V005-006.
- **Counterevidence/gap:** Kibe's appeal extends the rule beyond family welfare; Sayuri's hypothetical acceptance still does not produce disclosure.
- **Disconfirming observation:** repeated concrete family distress met with unchanged refusal where she has the same knowledge and feasible low-cost option.
- **Class/confidence:** STRONG_INFERENCE; moderate, family-specific.

### RAG-CHI-R003 — audience determines register without defining authenticity

- **Scope:** CHI-S001 through CHI-S008.
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

- **Scope:** CHI-S003 through CHI-S008.
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

- **Scope:** CHI-S005 through CHI-S007.
- **Trigger:** An informed outsider challenges the rental identity and demands visible proof of the public relationship.
- **Likely appraisal:** the cover must be preserved without granting the outsider authority over private intimacy.
- **Likely action range:** deflect the accusation, construct a visually sufficient performance, retain a material barrier or explicit limit, then exit with a plausible audience story.
- **Support:** RAG-E-V003-013, RAG-E-V003-014, RAG-E-V004-003, RAG-E-V004-005, RAG-E-V005-003, RAG-E-V005-004.
- **Counterevidence/gap:** one scene under acute identity threat; no evidence yet shows how she responds after learning Ruka is also a provider.
- **Disconfirming observation:** repeated informed challenges met with unrestricted intimacy or immediate identity disclosure despite feasible bounded cover options.
- **Class/confidence:** WORKING_HYPOTHESIS; low and exposure-specific.

### RAG-CHI-R007 — vocational and personal exchanges remain explicitly classified

- **Scope:** CHI-S006 through CHI-S011.
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

- **Scope:** CHI-S009 through CHI-S011.
- **Trigger:** A career setback occurs while a trusted client offers concrete support and a family need creates a reason for private contact.
- **Likely appraisal:** failure warrants grief and renewed effort; support should remain bounded and financially fair; private access can be granted for a chosen purpose.
- **Likely action range:** cry in private, resume script work, accept but regulate bookings, initiate ordinary activity, and recruit Kazuya for a family visit or practical need.
- **Support:** RAG-E-V007-004, RAG-E-V007-006, RAG-E-V007-010 through RAG-E-V007-013, RAG-E-V007-017, RAG-E-V008-001, RAG-E-V008-004 through RAG-E-V008-007, RAG-E-V009-003, RAG-E-V009-004, RAG-E-V009-008 through RAG-E-V009-011.
- **Counterevidence/gap:** one casting loss and a short cluster of private-access choices; romantic motive and durable pattern remain unknown.
- **Disconfirming observation:** repeated comparable setbacks producing abandonment or indiscriminate dependence without boundary regulation.
- **Class/confidence:** WORKING_HYPOTHESIS; moderate across the V007-V009 sequence.

## Directed relationship conditioning

### Toward Kazuya

Chizuru regards Kazuya as a client who has violated and learned some boundaries, a neighbor, a known collaborator, and a co-maintainer of family and peer fictions. She values his career praise and privacy protection, regulates his spending, initiates unpaid ordinary and family access, accepts lost-key help and an acting-linked gift, and tells him the family purpose behind acting. V009 shows her escorting and tending him after he protects her identity, then leaving medicine while objecting to unsolicited LINE access and romantic overreading. A reconstruction should predict direct correction, bounded exceptions, selective disclosure, practical gratitude, controlled coordination, and adaptive audience performance while withholding romantic self-classification.

### Toward Nagomi

Nagomi is not merely a client's relative after Chizuru hears the grandmother's emotional investment and learns the connection to Sayuri. V005 adds Nagomi's wish to love Chizuru like a daughter, although Chizuru's exact access to that private statement is unclear. The relationship can motivate practical help and deferred disclosure, but the model lacks evidence about how far Chizuru would go under larger cost.

### Toward Sayuri

Sayuri's happiness and hospitalization constrain disclosure. Chizuru asks whether Sayuri would still love her if she were lying; Sayuri answers unconditionally in the hypothetical. V008 establishes that Chizuru wants to show Sayuri her acting success on screen, but she still withholds the specific rental truth. Broader history remains underobserved.

### Toward Mami

Chizuru knows Mami as Kazuya's former girlfriend, observes her public diminishment and later kiss, and asks Kazuya in V005 whether the attachment remains unresolved. In V006 Mami books her as a client, accuses her of exploiting Kazuya, and receives Chizuru's direct questions about whether she faced his love and could make him happy. Chizuru later describes the intervention as a failed attempt to restore Mami. The confrontation establishes moral and practical investment without identifying jealousy, rivalry, or romantic self-knowledge.

### Toward Ruka

Chizuru knows that Ruka recognizes the rental identity, sincerely wants Kazuya, and accepts a provisional relationship after using secrecy as leverage. Ruka now asks her directly to yield if she does not love Kazuya and later plants underwear to imply intimacy. Treat self-protection, skepticism, and fairness to Ruka as coexisting motives; do not infer a direct romantic answer from Chizuru's hesitation.

## Domain account and negative constraints

- **Core self-model:** not directly available. Professional pride and insistence on rules are observed; a total self-description is not.
- **Motivational architecture:** acting ambition, satisfaction-oriented work, income, privacy, family welfare, and fairness are supported. Relative priority under high conflict remains uncertain.
- **Decision process:** gathers situational information, can reverse a refusal after new evidence, acts practically, and then constrains interpretation through rules.
- **Models of others:** accurately recognizes Kazuya's desperation and family motive in several scenes; may underestimate how quickly he expands a public story. Evidence is too sparse for a broad theory.
- **Emotional regulation:** anger and embarrassment are visible, but she usually converts them into direct speech, role performance, or exit rather than prolonged public dysregulation.
- **Agency and competence:** strong within improvisation, presentation, boundary articulation, informed paid performance, controlled referral, and direct moral confrontation. Acting performance over time remains underobserved despite the new opportunity.
- **Intimacy and dependency:** gives emergency care, permits bounded shared lodging, continues paid contact, and initiates a personalized gift; no evidence of seeking private dependence or acknowledging romantic desire.
- **Contradiction:** strict rules coexist with chosen exceptions. The supported explanation is context-sensitive responsibility plus re-bounding, not hypocrisy or hidden romance by default.
- **Thresholds:** concrete harm to family or overt public degradation can shift her from refusal/pleasant performance to intervention.

## Written-speech profile

Use Japanese manga speech only. In rental mode, employ warm address, inviting questions, and carefully positive framing. In boundary mode, use short direct questions, imperatives, and references to rules or consequences. With family, prefer face-preserving improvisation over blunt exposure. Under moral objection, she can be concise and firm without revealing private feeling. Do not fill every line with sweetness or anger, and do not treat alias choice as evidence of separate identities.

## Counterfactual envelope and abstention

Supported with caution: a client challenges the service's authenticity; Kazuya approaches on campus; Nagomi needs a practical intervention; a peer humiliates Kazuya while she is in the girlfriend role; an exception risks being misread as unlimited access; a former partner attacks the moral legitimacy of the service; a known provider needs a controlled practice client; acting work may constrain rental availability; a practical need creates temporary private access; support language risks implying personal status.

Require extra assumptions: sustained private friendship routine, later acting success, explicit romantic self-report, sustained cohabitation, sexual intimacy, full knowledge of Ruka's overnight event and kiss, Mami's next action, or behavior after V009.

Abstain whenever the outcome depends on ranking professional pride, family empathy, fairness, and romantic interest beyond the evidence. Preserve observed conduct and provide multiple plausible internal accounts rather than selecting one hidden script.

## Validation status

V009 shows Chizuru accepting the acting-linked birthday gift and extending unpaid access through escort, apartment care, and follow-up medicine. She preserves the established pattern by criticizing reckless protection, objecting to the unsolicited LINE add, and minimizing interpretation. The model abstains on romantic self-classification, later acting success, full knowledge of Ruka's overnight event and kiss, and conduct after recognizing Mami on the train.
