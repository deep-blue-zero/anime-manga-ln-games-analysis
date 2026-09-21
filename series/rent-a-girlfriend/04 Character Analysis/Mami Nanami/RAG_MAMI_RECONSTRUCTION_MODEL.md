---
title: "Rent-a-Girlfriend - Mami Nanami Reconstruction Model"
artifact_id: RAG_MAMI_RECONSTRUCTION_MODEL
artifact_type: character_reconstruction_model
series: Rent-a-Girlfriend
generation: V1
version: "1.4"
status: canonical
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
created: "2026-09-20"
source_boundary: "Operational model based only on Japanese manga witnesses RAG-JP-EPUB-V001-V024, with V011-V019 treated as a negative-evidence interval."
---

# Mami Nanami reconstruction model

## Model identity and basis

~~~yaml
model_identity:
  artifact_id: RAG_MAMI_RECONSTRUCTION_MODEL
  local_character_key: RAG-LOCAL-MAMI
  preferred_name: Mami Nanami
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
  admitted_through_volume: V024
  narrative_time_boundary: "after Mami treats Chizuru's souvenir-ring participation as contradictory, appears in a locked-account sequence framing restraint as help while resenting likely blame, and receives Nagomi's direct request to talk"
  basis_checkpoint: RAG_CP_V020
  basis_commit: 940f1b3050e41ff0fac8a79fcdbb8260b0f0ca06
  model_revision: "1.4"
  prior_knowledge_limitations:
    - "No post-V024 narrative evidence is admitted."
    - "Mami's final motive and desired endpoint remain unknown."
    - "V011-V019 contain no material observed Mami conduct and cannot be filled with inferred hidden actions."
coverage:
  observed_contexts:
    - breakup and former-partner contact
    - university peer gathering
    - public ridicule under a pleasant social surface
    - private vulnerable presentation and physical proximity
    - direct relationship questioning
    - stated separation goal
    - identity appropriation and public status testing
    - private kiss and scheduled meeting
    - rental-platform research
    - alternate-name booking
    - provider confrontation
    - conflicting status claims at Kazuya's workplace
    - direct observation of Chizuru on a rental date
    - social-account research
    - Twitter contact through Kibe
    - business proposal to Nagomi
    - selective secrecy request and follow-up planning
  missing_contexts:
    - reason for the original breakup
    - stable private motive and desired endpoint
    - family and home life
    - sustained work or study routine
    - close friendship outside Kazuya's network
    - response to a complete truthful account
    - conduct after explicit rejection of the V020 access route
    - low-stakes ordinary routine
  translation_limitations:
    - "Model derives from the Japanese witness; no licensed translation was admitted for comparison."
  written_speech: PARTIALLY_MODELED
  performed_voice: OUT_OF_SCOPE
local_readiness: PARTIAL_MODEL
~~~

## Intended use

This model supports bounded reconstruction when Mami encounters inconsistent relationship accounts, possesses an information advantage, or can approach Kazuya's network through a socially legitimate route. It can estimate likely questioning, information collection, selective disclosure, audience-specific presentation, parallel target testing, contradiction judgment, and attempts to preserve or widen access. It must abstain on her final motive, family history, private routine, a definitive romantic endpoint, the result of Nagomi's requested talk, and any action that depends on post-V024 knowledge.

## Central mechanism

Mami repeatedly responds to unresolved access and contradictory accounts by testing what other people know and by building routes that do not require her to announce a full intention. Public sociability, private vulnerability, client status, online research, and a business proposal are different access forms rather than proof of one hidden master plan. Across those forms she tends to disclose less about her endpoint than she asks others to disclose about theirs.

This information asymmetry can support destabilizing conduct. In V002 she explicitly wants to separate Kazuya and Chizuru, uses identity knowledge in public, kisses Kazuya, and schedules a meeting. In V005-V006 a sighting of Sumi becomes a platform search and a booking of Chizuru. In V009-V010 conflicting status claims and a direct rental sighting become questioning and family-account research. In V020 the dormant family route becomes contact through Kibe and a plausible older-user smartphone proposal to Nagomi.

The model cannot convert this recurrence into a solved motive. Mami can be affected, jealous, concerned, controlling, resentful, professionally interested, or several at once. Her self-report that she decided not to fall in love again and her request for secrecy constrain interpretation but do not establish which motive governs. Predictions should therefore be about method and access, not final purpose.

## Temporal states

### MAM-S001 — former partner re-entering the peer field

~~~yaml
state_id: MAM-S001
valid_from_source: "V001 0001"
valid_until_source: "V001 endpoint"
entry_conditions:
  - "Mami has ended a one-month relationship with Kazuya."
active_goals:
  - manage renewed contact with Kazuya
  - test or disturb the public girlfriend account
known_propositions:
  - "Kazuya remains affected by their former relationship."
  - "He publicly presents Chizuru as his girlfriend."
relationship_conditions:
  - "Mami is Kazuya's former girlfriend and remains inside his university peer network."
changed_from_previous:
  - FIRST_OBSERVED_STATE
evidence_refs:
  - RAG-E-V001-001
  - RAG-E-V001-012
  - RAG-E-V001-015
uncertainties:
  - "Why she ended the relationship and what she wants from renewed access."
~~~

### MAM-S002 — active relationship disruptor

~~~yaml
state_id: MAM-S002
valid_from_source: "V002 0025"
valid_until_source: "V003 endpoint"
entry_conditions:
  - "Mami encounters Kazuya and Chizuru together during the Izu trip."
active_goals:
  - separate Kazuya and Chizuru
  - test the credibility and future of their relationship
  - create private access to Kazuya
known_propositions:
  - "The presented couple account contains vulnerable details and audience dependencies."
  - "Kazuya remains responsive to her attention."
relationship_conditions:
  - "Kazuya still hopes for reconciliation."
  - "Chizuru is publicly presented as Kazuya's girlfriend."
changed_from_previous:
  - CONTEXT_CHANGE
  - REVEALED_NOT_NEW
evidence_refs:
  - RAG-E-V002-003
  - RAG-E-V002-005
  - RAG-E-V002-007
  - RAG-E-V002-009
  - RAG-E-V002-016
  - RAG-E-V003-002
  - RAG-E-V003-011
uncertainties:
  - "Whether separation is meant to produce reunion, withdrawal, punishment, or another outcome."
~~~

### MAM-S003 — platform investigator and client

~~~yaml
state_id: MAM-S003
valid_from_source: "V005 0158"
valid_until_source: "V006 endpoint"
entry_conditions:
  - "Mami directly observes Kazuya on a practice date with Sumi."
active_goals:
  - explain the new apparent girlfriend encounter
  - verify the service connection
  - confront Chizuru about the continuing account
known_propositions:
  - "Sumi and Chizuru are accessible through a rental-girlfriend platform."
  - "Kazuya's public relationship presentation remains inconsistent with paid access."
relationship_conditions:
  - "Mami can use customer status to reach Chizuru privately."
changed_from_previous:
  - KNOWLEDGE_CHANGE
  - CONTEXT_CHANGE
evidence_refs:
  - RAG-E-V005-017
  - RAG-E-V006-005
  - RAG-E-V006-008
  - RAG-E-V006-011
  - RAG-E-V006-014
uncertainties:
  - "Whether concern for Kazuya, personal claim, hostility to the lie, or another motive dominates."
~~~

### MAM-S004 — contradiction integrator with a dormant family route

~~~yaml
state_id: MAM-S004
valid_from_source: "V009 0128"
valid_until_source: "V019 endpoint"
entry_conditions:
  - "Mami encounters Ruka and Kazuya at the karaoke workplace."
active_goals:
  - test contradictory girlfriend and rental accounts
  - preserve an information route into Kazuya's family network
known_propositions:
  - "Ruka claims girlfriend status and sex, but Kazuya corrects both claims."
  - "Chizuru continues to work rental dates."
  - "The Kinoshita family business has a public social account."
relationship_conditions:
  - "Mami has no openly stated family role but can follow the public account."
changed_from_previous:
  - KNOWLEDGE_CHANGE
  - CONTEXT_CHANGE
evidence_refs:
  - RAG-E-V009-012
  - RAG-E-V009-013
  - RAG-E-V009-014
  - RAG-E-V009-015
  - RAG-E-V010-001
  - RAG-E-V010-002
uncertainties:
  - "No material conduct is observed from V011 through V019."
~~~

### MAM-S005 — family-access operator under a professional account

~~~yaml
state_id: MAM-S005
valid_from_source: "V020 0019"
valid_until_source: "V021 0004"
entry_conditions:
  - "Mami has made contact with Kibe and reaches Nagomi through him."
active_goals:
  - present an older-user smartphone support service
  - preserve access to Kibe, Nagomi, and Kazuya
  - keep her prior relationship with Kazuya outside the current business audience
known_propositions:
  - "Kibe can introduce her to Nagomi."
  - "Nagomi is receptive enough to evaluate the proposal."
  - "Kazuya can reveal their past unless asked not to."
relationship_conditions:
  - "Mami approaches as a plausible professional contact rather than as Kazuya's former girlfriend."
changed_from_previous:
  - RELATIONSHIP_CHANGE
  - CONTEXT_CHANGE
evidence_refs:
  - RAG-E-V020-003
  - RAG-E-V020-022
  - RAG-E-V020-023
uncertainties:
  - "Whether the service is independently pursued, strategically instrumental, or both."
  - "How she would respond if Kazuya or Nagomi rejects the secrecy or access terms."
~~~

### MAM-S006 — evidence-consolidating direct intervener across Chizuru and family routes

~~~yaml
state_id: MAM-S006
valid_from_source: "V021 0005"
valid_until_source: "V022 0004"
entry_conditions:
  - "Mami has legitimate-looking access to Nagomi, knows Kazuya and Chizuru remain connected, and can research the public film record."
active_goals:
  - preserve credibility and access with Nagomi
  - test Chizuru's current relation to Kazuya through concrete evidence
  - persuade Chizuru to accept Mami's interpretation and proposed intervention
  - control disclosure of her former relationship across audiences
known_propositions:
  - "Nagomi accepts her incident account and has met her repeatedly."
  - "The crowdfunding page publicly links Chizuru's film and Kazuya's producer role."
  - "Chizuru's bag was present in Kazuya's room during Mami's prior visit."
  - "Chizuru distinguishes sincere project participation from rental-girlfriend work."
relationship_conditions:
  - "Mami presents herself to Nagomi through work and to Chizuru as an informed former partner and ally."
  - "Her negative account of Kazuya is first-person testimony rather than independently settled fact."
  - "The scope of ending everything and the content of her direct Nagomi call remain withheld."
changed_from_previous:
  - REPEAT_FAMILY_CREDIBILITY_ESTABLISHED
  - PUBLIC_PROJECT_EVIDENCE_ACQUIRED
  - APARTMENT_RESIDUE_CONFIRMED
  - CHIZURU_DIRECTLY_CONFRONTED
  - FORMER_PARTNER_ACCOUNT_DISCLOSED
  - ALLY_STATUS_CLAIMED
  - JOINT_ENDING_PROPOSED
  - NAGOMI_DIRECTLY_CALLED
evidence_refs:
  - RAG-E-V021-001
  - RAG-E-V021-018
  - RAG-E-V021-019
  - RAG-E-V021-020
  - RAG-E-V021-021
  - RAG-E-V021-024
uncertainties:
  - "Whether protection, control, punishment, truth correction, renewed attachment, or a mixture governs the intervention."
  - "What action she proposes by ending everything."
  - "What she tells Nagomi and whether the app work remains independently active."
~~~

### MAM-S007 — embedded trip observer with calibrated disclosure

~~~yaml
state_id: MAM-S007
valid_from_source: "V022 0005"
valid_until_source: "V023 0004"
entry_conditions:
  - "Mami has direct Nagomi access, has proposed ending the situation to Chizuru, and is already staying at Spa Resort Hawaiians through a family-manager connection."
active_goals:
  - remain inside the Kinoshita family setting without prematurely disclosing her full stake
  - observe and test the relation among Kazuya, Chizuru, Ruka, and their partly informed peers
  - preserve the capacity to end or expose the current arrangement by a method not yet disclosed
known_propositions:
  - "Nagomi knows that Mami is in Fukushima and willingly includes her in the travel group."
  - "Nagomi knows public facts about Chizuru's acting and Kazuya's crowdfunding-producer role."
  - "Ruka recognizes Mami as Kazuya's former girlfriend, and Chizuru recognizes the prior intervention."
  - "Kuribayashi knows that Chizuru has worked as a rental girlfriend and asks whether that work continues."
relationship_conditions:
  - "Mami has socially legitimate venue and family access but no disclosed intimate role in the group."
  - "Nagomi remains uninformed about the former relationship and rental history."
  - "The mixed audience makes uniform disclosure costly and calibrated answers useful."
changed_from_previous:
  - PRIOR_RESORT_LODGING_ESTABLISHED
  - FAMILY_MANAGER_CONNECTION_DISCLOSED
  - NAGOMI_TRIP_INCLUSION_OBTAINED
  - MIXED_AUDIENCE_ACCESS_GAINED
  - PROJECT_INFORMATION_REACHED_FAMILY_SETTING
  - ENDING_OBJECTIVE_RETAINED
  - KURIBAYASHI_QUERY_ANSWERED_SELECTIVELY
evidence_refs:
  - RAG-E-V022-014
  - RAG-E-V022-015
  - RAG-E-V022-016
  - RAG-E-V022-017
  - RAG-E-V022-018
  - RAG-E-V022-020
uncertainties:
  - "The exact content and causal role of the V021 Nagomi call."
  - "Whether the resort overlap was planned, opportunistic, or mixed beyond the stated lodging facts."
  - "What action Mami intends by ending the situation and which audience she will address first."
~~~

### MAM-S008 — embedded multi-target intervener using disclosure leverage

~~~yaml
state_id: MAM-S008
valid_from_source: "V023 0005"
valid_until_source: null
entry_conditions:
  - "Mami is inside the Hawaiians group with direct access to Kazuya, Chizuru, Ruka, Nagomi, and partly informed peers."
active_goals:
  - test which participant can be moved toward ending or exposing the current arrangement
  - preserve socially legitimate family access while controlling disclosure timing
  - verify relationship facts through platform evidence and direct questioning
  - retain motive and final method under her own control
known_propositions:
  - "Ruka says she loves Kazuya but lacks secure recognized status."
  - "Chizuru's rental profile remains visible, and the family still believes a future-bride account."
  - "Kazuya admits that he lied about Chizuru's presence and says he will correct the story after confessing."
  - "Ruka may be willing to consider disclosure to Nagomi when pressured about Chizuru's possible feeling."
  - "Chizuru remains wary but has received a promise of warning before sudden exposure."
relationship_conditions:
  - "Mami presents support differently to Ruka, Chizuru, and Kazuya while revealing no single final beneficiary."
  - "Nagomi remains a high-leverage audience whose trust and family care are still based on incomplete information."
  - "No alliance with Ruka or Chizuru is completed."
changed_from_previous:
  - RUKA_ATTACHMENT_PROBED
  - SUPPORT_CONTACT_OFFERED
  - CHIZURU_PROFILE_VERIFIED
  - DISCLOSURE_WARNING_GIVEN
  - KAZUYA_COVER_LIE_RECEIVED
  - KAZUYA_TRUST_AND_TIMING_TESTED
  - CARING_FORMER_PARTNER_REGISTER_USED
  - RUKA_REAL_STATUS_TESTED
  - CHIZURU_FEELING_HYPOTHESIS_RAISED
  - NAGOMI_DISCLOSURE_WILL_TESTED
evidence_refs:
  - RAG-E-V023-004
  - RAG-E-V023-006
  - RAG-E-V023-008
  - RAG-E-V023-009
  - RAG-E-V023-010
  - RAG-E-V023-011
  - RAG-E-V023-014
  - RAG-E-V023-015
  - RAG-E-V023-016
uncertainties:
  - "Whether concern, control, punishment, truth correction, renewed attachment, or a mixture governs the intervention."
  - "Which target or audience Mami will activate next."
  - "Whether her warning to Chizuru constrains later disclosure in practice."
~~~

### MAM-S009 — contradiction judge under family-initiated contact

~~~yaml
state_id: MAM-S009
valid_from_source: "V024 0005"
valid_until_source: null
entry_conditions:
  - "Mami remains embedded in the Hawaiians group after separately probing Ruka, Chizuru, and Kazuya and learning Kazuya's confession-first correction plan."
active_goals:
  - evaluate whether Chizuru's conduct matches her disclaimers about Kazuya and the family
  - preserve control over disclosure timing while construing delay as intervention
  - respond to Nagomi without prematurely revealing Mami's entire stake or endpoint
  - obtain a same-day consequence from Chizuru or the family route
known_propositions:
  - "Harumi has Chizuru try a souvenir ring inside an apparent future-family interaction."
  - "Chizuru's conduct can be interpreted as participating in family-bride imagery despite prior denials."
  - "A locked account presented within Mami's sequence frames silence as help and anticipates being cast as the bad person."
  - "Nagomi directly asks Mami to speak."
  - "Kazuya and Chizuru are converging at the chapel under an unresolved confession deadline."
relationship_conditions:
  - "Mami judges Chizuru from an interested former-partner and intervention position rather than a neutral adjudicator role."
  - "Nagomi trusts Mami enough to initiate private contact while lacking the former-partner and rental history."
  - "No public disclosure or stable alliance has completed."
changed_from_previous:
  - SOUVENIR_RING_SCENE_OBSERVED
  - CHIZURU_LIAR_JUDGMENT_FORMED
  - PRIVATE_RESTRAINT_AS_HELP_FRAMING_PRESENTED
  - ANTICIPATED_VILLAIN_STATUS_RESENTED
  - SAME_DAY_CONCLUSION_PRESSURE_RETAINED
  - NAGOMI_PRIVATE_TALK_REQUEST_RECEIVED
evidence_refs:
  - RAG-E-V024-009
  - RAG-E-V024-015
  - RAG-E-V024-019
uncertainties:
  - "The exact ownership and audience of the locked account beyond its sequence presentation."
  - "What Nagomi wants to discuss and what Mami discloses in response."
  - "Whether Mami's help framing reflects protection, control, punishment, truth correction, or a mixture."
~~~

## Behavioral rules

### RAG-MAM-R001 — contradictory relationship accounts prompt targeted coherence testing

- Scope: MAM-S001 through MAM-S004.
- Trigger: a public couple claim conflicts with observed conduct, service status, or another person's account.
- Relationship conditions: Mami has direct access to at least one participant or audience and possesses a fact that the others have not integrated.
- Likely appraisal: the stated relationship can be tested through specific questions or by making a hidden fact salient.
- Likely action range: ask about history or future, appropriate a known identity detail, challenge standing, compare accounts, or confront a person after direct observation.
- Support: RAG-E-V001-012, RAG-E-V002-005, RAG-E-V002-007, RAG-E-V006-011, RAG-E-V006-014, RAG-E-V009-012 through RAG-E-V009-015, RAG-E-V010-001.
- Counterevidence/gap: she does not immediately expose every contradiction and leaves a long V011-V019 interval without observed action.
- Alternative: some tests may be motivated by affective reaction rather than a stable truth-seeking preference.
- Disconfirming observation: repeated access to a consequential contradiction followed by unqualified acceptance without inquiry or strategic delay.
- Class/confidence: STRONG_INFERENCE; moderate within relationship-status conflicts.

### RAG-MAM-R002 — an ambiguous sighting can become institution-mediated information access

- Scope: MAM-S003 through MAM-S005.
- Trigger: direct observation or public data suggests a route into an otherwise protected relationship or family system.
- Relationship conditions: a platform, public account, or intermediary makes contact possible without initial private disclosure by the target.
- Likely appraisal: the route can verify facts and create legitimate-looking access more effectively than an unsupported accusation.
- Likely action range: search a service profile, book through the platform, follow a public account, contact an intermediary online, or present a business proposal.
- Support: RAG-E-V005-017, RAG-E-V006-005, RAG-E-V006-008, RAG-E-V010-002, RAG-E-V020-022.
- Counterevidence/gap: only the platform booking and V020 meeting show route conversion; the family-account follow has no observed consequence until the later, partly indirect access sequence.
- Alternative: the V020 service may also be a real work project rather than solely an access instrument.
- Disconfirming observation: comparable public routes are repeatedly ignored while she chooses unsupported direct exposure instead.
- Class/confidence: STRONG_INFERENCE for method; low for purpose.

### RAG-MAM-R003 — audience changes presentation more reliably than it reveals motive

- Scope: MAM-S001, MAM-S002, and MAM-S005.
- Trigger: movement between peer audience, private former-partner contact, and professional or family-facing contact.
- Relationship conditions: Mami can decide which part of her past or objective is legible to the current audience.
- Likely appraisal: a register fitted to the audience preserves access and keeps her endpoint under her control.
- Likely action range: sociable ridicule in a group, softer vulnerability in private, or future-oriented professional framing before Nagomi while requesting secrecy from Kazuya.
- Support: RAG-E-V001-012, RAG-E-V001-015, RAG-E-V002-009, RAG-E-V020-022, RAG-E-V020-023.
- Counterevidence/gap: vulnerability and professional interest may be sincere; register control cannot by itself classify them as deceptive.
- Alternative: shifts can reflect ordinary context sensitivity rather than manipulation.
- Disconfirming observation: the same full account and affective register persist across audiences despite clear access cost.
- Class/confidence: STRONG_INFERENCE for audience sensitivity; low for inferred sincerity.

### RAG-MAM-R004 — renewed romantic access can coexist with refusal to state a final relational claim

- Scope: MAM-S001 through MAM-S003.
- Trigger: Kazuya remains responsive while his current relation appears unstable or false.
- Relationship conditions: Mami is a former partner and Chizuru occupies the publicly presented girlfriend role.
- Likely appraisal: she can test attachment or disrupt the current account without declaring a durable future with Kazuya.
- Likely action range: approach, permit proximity, kiss, schedule a private meeting, challenge Chizuru's standing, or remain affected by an answer.
- Support: RAG-E-V001-015, RAG-E-V002-003, RAG-E-V002-009, RAG-E-V002-016, RAG-E-V003-011, RAG-E-V006-014.
- Counterevidence/gap: the scheduled meeting fails, no reunion attempt is completed, and she reports an earlier decision not to fall in love.
- Alternative: control, resentment, or opposition to the lie may better explain some acts than a desire for reunion.
- Disconfirming observation: a complete, stable declaration of a different endpoint followed by conduct consistently organized around it.
- Class/confidence: WORKING_HYPOTHESIS; low-to-moderate and motive-bounded.

### RAG-MAM-R005 — dormant information can be reactivated through a lower-friction social route

- Scope: transition from MAM-S004 to MAM-S005.
- Trigger: a known family connection becomes reachable through Kibe and an older café contact.
- Relationship conditions: Mami lacks a declared family role but can approach through a trusted person and a service with plausible relevance to Nagomi.
- Likely appraisal: indirect introduction lowers immediate resistance and avoids foregrounding the former relationship.
- Likely action range: contact Kibe, attend a Nagomi meeting, frame the route as work, request selective privacy, and schedule follow-up.
- Support: RAG-E-V010-002, RAG-E-V020-003, RAG-E-V020-022, RAG-E-V020-023.
- Counterevidence/gap: the text does not show that the earlier account follow directly caused the Kibe route, and nine volumes of activity are unknown.
- Alternative: the professional opportunity may have arisen independently and only incidentally intersects the family.
- Disconfirming observation: the proposal proceeds transparently as ordinary work with no use of relationship information or special access.
- Class/confidence: WORKING_HYPOTHESIS; low and specific to the V020 route.

### RAG-MAM-R006 — public documentation and private residue can be combined into audience-specific direct pressure

- Scope: MAM-S006.
- Trigger: the crowdfunding page and remembered apartment object jointly contradict a simple discontinued-customer account.
- Relationship conditions: Mami can reach Chizuru privately while preserving a different professional presentation with Nagomi and Kibe.
- Likely appraisal: specific evidence and personal testimony can make Chizuru question both Kazuya's account and her own role in maintaining the deception.
- Likely action range: present documentary links, reveal private observation, distinguish trusted family members from Kazuya, narrate the former relationship, claim ally status, and offer coordinated intervention.
- Support: RAG-E-V021-018 through RAG-E-V021-021, with direct family continuation at RAG-E-V021-024.
- Counterevidence/gap: one extended meeting; Chizuru's acceptance, Mami's proposed method, and independent verification of the former-partner account are unavailable.
- Alternative: sincere protective concern and strategic control may coexist rather than forming exclusive explanations.
- Disconfirming observation: when comparable public and private evidence is available, Mami discloses it uniformly to all audiences without tailoring, pressure, or an attempt to influence the target's response.
- Class/confidence: WORKING_HYPOTHESIS; low and motive-bounded.

### RAG-MAM-R007 — legitimate venue and family routes can be combined into mixed-audience access with selective disclosure

- Scope: MAM-S007.
- Trigger: Mami is already present at a destination reachable through family connections while Nagomi can include her in a shared event.
- Relationship conditions: different travelers know different parts of her history and Chizuru's rental status, so full disclosure would change access and audience alignment.
- Likely appraisal: ordinary lodging and Nagomi's invitation provide stronger sustained access than an immediate accusation, while limited answers preserve maneuvering room.
- Likely action range: disclose a plausible venue basis, accept family inclusion, observe guarded reactions, carry public facts across contexts, answer an informed peer minimally, and withhold the final intervention method.
- Support: RAG-E-V022-014 through RAG-E-V022-020.
- Counterevidence/gap: one destination sequence; the exact call, planning degree, and later use of access remain unknown.
- Alternative: some or all of the travel overlap may be ordinary family logistics rather than a long-planned intervention.
- Disconfirming observation: comparable legitimate embedded access is immediately abandoned or used for uniform full disclosure without regard to audience cost.
- Class/confidence: WORKING_HYPOTHESIS; low and route-specific.

### RAG-MAM-R008 — embedded mixed-audience access can support parallel target-specific probes before public exposure

- Scope: MAM-S008.
- Trigger: several partly informed actors occupy the same setting and each holds a different route to the desired change.
- Relationship conditions: public disclosure would alter access, while private questions can test attachment, trust, and willingness to act.
- Likely appraisal: compare the targets separately before choosing which audience or contradiction to activate.
- Likely action range: offer support to one rival, verify a platform profile, warn the principal conditionally, test the former partner's correction plan, and ask another rival about family disclosure.
- Support: RAG-E-V023-004, RAG-E-V023-006, RAG-E-V023-008 through RAG-E-V023-016.
- Counterevidence/gap: one resort interval; the probes do not yet reveal which route she will use or whether any concern statement is instrumental.
- Alternative: sincere concern for different participants may coexist with strategic comparison.
- Disconfirming observation: comparable embedded access produces one uniform full account to every target without private testing or audience calibration.
- Class/confidence: WORKING_HYPOTHESIS; low and mixed-audience-specific.

### RAG-MAM-R009 — observed contradiction can become moral judgment while delayed action is framed as help

- Scope: MAM-S009.
- Trigger: Chizuru participates in family-coded conduct that appears inconsistent with her prior denial or reluctance.
- Relationship conditions: Mami retains disclosure leverage, lacks a completed alliance, and can still reach Nagomi directly.
- Likely appraisal: Chizuru is benefiting from or sustaining a false position, while Mami's own restraint deserves recognition rather than blame.
- Likely action range: observe without immediate exposure, form a concise moral judgment, use private or restricted self-framing, preserve same-day pressure, and answer a family-initiated contact selectively.
- Support: RAG-E-V024-009, RAG-E-V024-015, RAG-E-V024-019.
- Counterevidence/gap: one short sequence; the locked account is not publicly authenticated, and no resulting conversation or action tests the framing.
- Alternative: resentment, sincere protection, strategic positioning, or several motives may coexist.
- Disconfirming observation: comparable apparent contradiction produces neither judgment nor controlled delay and instead leads to an unrelated transparent response.
- Class/confidence: WORKING_HYPOTHESIS; low and attribution-bounded.

## Directed relationship conditioning

### Toward Kazuya

Mami knows Kazuya as a former boyfriend who remained responsive after the breakup and later became entangled in contradictory relationship presentations. V021 adds her own negative account of his pursuit, but that testimony must remain attributed. V023 gives her his direct admission of the cover lie and his confession-first correction plan while she presents concern for his happiness. V024 does not give her his chapel speech or Chizuru's answer; it places her own route under Nagomi's direct request. She can pressure him publicly, approach privately, create physical or scheduled access, test trust, and withhold her own endpoint. Do not predict reunion, harm, protection, or confession from former-partner status alone.

### Toward Chizuru

Chizuru is first the publicly presented girlfriend, then a verified rental provider whose continued involvement Mami challenges. Mami uses identity details, client access, public project documentation, apartment residue, direct testimony, and V023 profile verification. She claims ally status, proposes a joint ending, and later promises warning rather than sudden exposure. V024 adds an explicit liar judgment after the souvenir-ring scene and a private sequence framing Mami's restraint as help. The model cannot determine whether protection, control, punishment, truth correction, or mixed motive governs the offer, warning, and delay.

### Toward Ruka

Ruka supplies a rival status claim and a false sex claim that Kazuya corrects. In V023 Mami asks whether Ruka loves Kazuya, tests real-girlfriend status, raises Chizuru's possible feeling, and asks whether Ruka will disclose to Nagomi. This supports a bounded information-and-coalition test, not friendship, stable alliance, or a shared endpoint.

### Toward Kibe and Nagomi

Kibe becomes an intermediary, and Nagomi becomes the audience for a smartphone-service proposal. Mami presents herself through future-oriented work, suppresses former-partner history, builds repeated credibility, calls Nagomi directly, and then joins Nagomi's Hawaiians group while already present through a family-manager lodging route. V023 makes Nagomi disclosure an explicit option in Mami's Ruka test without carrying it out. V024 reverses direction when Nagomi asks Mami to talk. Predict route maintenance and calibrated disclosure within this setting; abstain on the requested topic, resulting disclosure, trust, exploitation, and durability.

## Domain account and negative constraints

- Motivational architecture: access, information advantage, relationship-status challenge, and control of self-disclosure are supported. A final motive is not.
- Decision process: concrete contradictions and available routes often precede research, questioning, or contact; the evidence does not establish exhaustive long-range planning.
- Emotional regulation: she can maintain a pleasant or professional surface and also show visible affect. Surface control does not prove emotional absence.
- Agency and competence: initiative is observed in questioning, research, booking, network contact, proposal framing, and follow-up scheduling. Actual business execution remains untested.
- Intimacy: a kiss and renewed proximity are observed. They do not establish mutual relationship restoration or continuing consent.
- Ethics and deception: selective disclosure and public destabilization are material. Do not infer criminality, total fabrication, or malicious intent beyond the evidence.
- Ordinary repertoire: too sparse for broad social or professional generalization.

## Written-speech profile

Use Japanese manga written speech only. Mami can place pointed questions or status pressure inside socially smooth language, become direct when a contradiction is exposed, and give a professionally coherent account without revealing private stakes. Avoid writing her as omniscient, continuously hostile, uniformly seductive, or certain of facts she has only inferred.

## Counterfactual envelope and abstention

Supported with caution: a new inconsistency in a relationship account; public information that opens a contact route; an audience before whom former-partner history is costly; a target who denies an observed fact; a follow-up meeting after the V020 proposal.

Require extra assumptions: family life, workplace competence beyond the pitch, whether she still wants Kazuya romantically, response to full truth, response to firm exclusion, willingness to harm Nagomi, the result of Nagomi's requested talk, or any post-V024 conduct.

Abstain whenever the outcome depends on solving her motive, inventing V011-V019 conduct, treating research as omniscience, or assuming that professional plausibility proves either innocence or deception. Generated scenarios cannot become canon evidence.

## Validation status

The model is admitted as `PARTIAL_MODEL`. Repeated information acquisition, audience-sensitive presentation, contradiction testing, and access-building recur across peer, platform, workplace, online, business, venue, and family contexts. V023 validates parallel target-specific probes inside embedded mixed-audience access; V024 adds contradiction judgment, a restraint-as-help self-framing, and family-initiated contact. The method remains more generalizable than the motive, the long negative-evidence interval remains substantial, and ordinary routine is sparse. Operational use is therefore limited to named information-and-access pressures with explicit abstention on endpoint and intent.
