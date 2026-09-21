---
title: "Rent-a-Girlfriend - Claims, predictions, and revisions ledger"
artifact_id: RAG_CLAIMS_PREDICTIONS_AND_REVISIONS_LEDGER
artifact_type: claims_predictions_revisions_ledger
series: Rent-a-Girlfriend
generation: V1
version: "1.32"
status: canonical
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
created: "2026-09-19"
source_boundary: "Japanese manga witnesses RAG-JP-EPUB-V001-V028; inspected and closed through V028; predictions frozen before V029 narrative inspection."
---

# Claims, predictions, and revisions ledger

## Responsibility

Preserve current claims, competing hypotheses, prospective predictions, adjudications, counterevidence, and historical revisions.

## Record schema

`claim_id | scope | formulation | epistemic_class | evidence_refs | counterevidence_or_gap | prediction_conditions | disconfirmation | adjudication | transition | prior_formulation`

Markdown tables and bounded prose may implement this semantic schema. Unknown values remain unknown; rows cite canonical volume evidence IDs rather than duplicating primary observations.

## Update and routing rule

Update after each eligible volume only when inspected evidence materially affects this responsibility. Preserve stable IDs and historical states. A reviewed domain may record no material change without manufacturing a row. Consequential claims route back to the owning volume reading and forward to the project artifacts named by the series architecture.

## Current coverage

```yaml
initialized: true
inspected_through_volume: V028
current_claim_count: 104
frozen_prediction_count: 4
state: CURRENT_THROUGH_V028__PREDICTIONS_FROZEN_FOR_V029
```

## Current claims

| Claim ID | Scope and formulation | Class | Evidence | Counterevidence or gap | Current adjudication |
|---|---|---|---|---|---|
| RAG-CLM-001 | Attempted endings recur as expansions that preserve new social or material constraints. | STRONG_INFERENCE | RAG-E-V001-004, RAG-E-V001-006, RAG-E-V001-007, RAG-E-V001-008, RAG-E-V001-009, RAG-E-V001-011, RAG-E-V002-008, RAG-E-V002-012, RAG-E-V002-014, RAG-E-V002-015, RAG-E-V003-006, RAG-E-V003-009, RAG-E-V003-010, RAG-E-V003-014, RAG-E-V004-003, RAG-E-V004-005, RAG-E-V004-017, RAG-E-V005-001, RAG-E-V005-006, RAG-E-V005-007, RAG-E-V006-006, RAG-E-V006-009, RAG-E-V006-017 | Six volumes support recurrence; long-series durability remains untested. | STRENGTHENED through V006. |
| RAG-CLM-002 | Transactional form sets duties and boundaries but does not by itself settle the authenticity of every act or feeling. | STRONG_INFERENCE | RAG-E-V001-002, RAG-E-V001-003, RAG-E-V001-005, RAG-E-V001-008, RAG-E-V001-009, RAG-E-V001-013, RAG-E-V002-002, RAG-E-V002-006, RAG-E-V002-013, RAG-E-V002-017, RAG-E-V003-003, RAG-E-V003-008, RAG-E-V003-009, RAG-E-V003-016, RAG-E-V004-001, RAG-E-V004-007, RAG-E-V004-014, RAG-E-V004-016, RAG-E-V004-018, RAG-E-V005-009, RAG-E-V005-010, RAG-E-V005-011, RAG-E-V005-012, RAG-E-V006-001, RAG-E-V006-008, RAG-E-V006-011, RAG-E-V006-013 | Chizuru's private motives receive little direct access; V005-V006 show informed cooperation and confrontation inside compensated labor without allocating a unique motive. | STRENGTHENED; motive allocation remains bounded. |
| RAG-CLM-003 | Kazuya's extreme self-account is diagnostically useful but incomplete; conduct must test both his flattering and unflattering interpretations. | STRONG_INFERENCE | RAG-E-V001-002, RAG-E-V001-008, RAG-E-V001-011, RAG-E-V001-014, RAG-E-V002-005, RAG-E-V002-010, RAG-E-V002-012, RAG-E-V002-017, RAG-E-V003-005, RAG-E-V003-015, RAG-E-V004-004, RAG-E-V004-011, RAG-E-V004-013, RAG-E-V004-015, RAG-E-V005-008, RAG-E-V005-011, RAG-E-V006-001, RAG-E-V006-002, RAG-E-V006-012, RAG-E-V006-016 | Completed employment-linked repair, adaptive care, and pursued responsibility is counterevidence to a uniformly helpless account; panic and concealment continue elsewhere. | STRENGTHENED through V006 with discriminating counterevidence. |
| RAG-CLM-004 | Chizuru's minimum warranted through-line is controlled responsibility, compartmentalization, and vocational purpose, not proven romance. | STRONG_INFERENCE | RAG-E-V001-005, RAG-E-V001-006, RAG-E-V001-007, RAG-E-V001-008, RAG-E-V001-009, RAG-E-V001-013, RAG-E-V002-002, RAG-E-V002-006, RAG-E-V002-013, RAG-E-V002-015, RAG-E-V003-001, RAG-E-V003-003, RAG-E-V003-008, RAG-E-V003-009, RAG-E-V003-010, RAG-E-V004-012, RAG-E-V004-014, RAG-E-V004-017, RAG-E-V005-010, RAG-E-V005-012, RAG-E-V005-014, RAG-E-V006-006, RAG-E-V006-013, RAG-E-V006-015 | Professional pride, fairness, family empathy, social obligation, and personal investment remain inseparable; acting purpose becomes practical in V006, while her romantic self-report remains absent. | STRENGTHENED through V006; vocational consequence now observed. |
| RAG-CLM-005 | V001 progress is strongest in shared infrastructure and social consequence; no mutual private romance is established. | STRONG_INFERENCE | RAG-E-V001-006, RAG-E-V001-007, RAG-E-V001-008, RAG-E-V001-009, RAG-E-V001-011, RAG-E-V001-013, RAG-E-V001-014 | Future volumes may recontextualize motive but cannot retroactively create a V001 joint acknowledgment. | PRESERVE at V001 boundary. |
| RAG-CLM-006 | Audience belief is causally active: Kibe's mistaken premise and the grandmothers' couple belief produce conflict, secrecy pressure, travel, and shared space. | STRONG_INFERENCE | RAG-E-V002-008, RAG-E-V002-012, RAG-E-V002-014, RAG-E-V002-015, RAG-E-V003-004, RAG-E-V003-006, RAG-E-V003-007 | Later correction may revise responses but cannot erase the observed chains. | STRENGTHENED through V003. |
| RAG-CLM-007 | Mami's operational goal in V002 is to destabilize or split the public couple, while the motive and desired final relationship remain unresolved. | STRONG_INFERENCE | RAG-E-V002-003, RAG-E-V002-005, RAG-E-V002-007, RAG-E-V002-009, RAG-E-V002-016, RAG-E-V003-002, RAG-E-V003-011 | The no-love statement adds a self-report but does not distinguish love, jealousy, status, control, or withdrawal. | OPEN; separate goal from motive. |
| RAG-CLM-008 | The unpriced rescue becomes a successful reciprocal rescue with public, medical, and scheduling consequences; it supports personal significance without proving mature love. | STRONG_INFERENCE | RAG-E-V002-016, RAG-E-V002-017, RAG-E-V003-001, RAG-E-V003-002, RAG-E-V003-003, RAG-E-V003-005 | Emergency action and CPR do not generalize to ordinary partnership or establish reciprocation. | REVISED and strengthened through V003. |
| RAG-CLM-009 | V003 uses intimacy-like images as boundary tests whose meaning depends on agency, necessity, consent, and material obstruction. | STRONG_INFERENCE | RAG-E-V003-001, RAG-E-V003-008, RAG-E-V003-013, RAG-E-V003-015 | The scenes differ sharply; formal similarity must not erase those differences. | OPEN; current through V003. |
| RAG-CLM-010 | Ruka's dual position as former rental provider and provisional girlfriend makes her both an informed observer of Chizuru and an active participant in a differently constrained relationship. | STRONG_INFERENCE | RAG-E-V003-012, RAG-E-V003-013, RAG-E-V003-014, RAG-E-V003-016, RAG-E-V004-001, RAG-E-V004-003, RAG-E-V004-005, RAG-E-V004-007, RAG-E-V005-004, RAG-E-V005-007, RAG-E-V005-013, RAG-E-V006-009, RAG-E-V006-010 | Kuribayashi's basic knowledge is now corrected; exact original terms and Ruka's broader professional history remain incomplete. | STRENGTHENED through V006. |
| RAG-CLM-011 | Ruka treats measurable bodily excitation as proof of emotional authenticity and Kazuya as its unique cause. | STRONG_INFERENCE | RAG-E-V004-002, RAG-E-V004-006, RAG-E-V004-007, RAG-E-V004-008, RAG-E-V005-001, RAG-E-V005-002 | The pulse criterion is Ruka's represented personal rule; V005 shows tactical inhibition but no revision of the uniqueness inference. | OPEN; current through V005. |
| RAG-CLM-012 | Personal gifts create unpriced reciprocity across the paid relationship without by themselves establishing mutual romance. | STRONG_INFERENCE | RAG-E-V004-014, RAG-E-V004-015, RAG-E-V004-016, RAG-E-V004-018, RAG-E-V005-008, RAG-E-V005-009 | Chizuru supplies gratitude and shared-secret reasons; the gift-motivated job later funds care for a friend rather than a couple transition. | STRENGTHENED through V005. |
| RAG-CLM-013 | Kazuya's newly acknowledged attachment produces both care and boundary failure; self-recognition is not equivalent to relational competence. | STRONG_INFERENCE | RAG-E-V003-005, RAG-E-V003-015, RAG-E-V004-004, RAG-E-V004-011, RAG-E-V004-013, RAG-E-V004-015, RAG-E-V005-001, RAG-E-V005-008, RAG-E-V005-011, RAG-E-V005-013, RAG-E-V006-009, RAG-E-V006-012, RAG-E-V006-016, RAG-E-V006-017 | Refusal and friendship repair add competence evidence; public humiliation and panic concealment preserve the mixed pattern. | STRENGTHENED through V006. |
| RAG-CLM-014 | Bounded self-disclosure can repair a deceived audience without dissolving the larger deception system. | STRONG_INFERENCE | RAG-E-V005-008, RAG-E-V005-009, RAG-E-V005-011 | Kuribayashi receives the truth and accepts the repair, while family, Kibe, and wider peers remain uninformed. | ADDED and supported in V005. |
| RAG-CLM-015 | Chizuru sometimes converts trust in a known client into off-platform coordination that produces a new paid encounter, expanding collaboration without settling romance. | STRONG_INFERENCE | RAG-E-V005-012, RAG-E-V005-014, RAG-E-V005-016, RAG-E-V006-001 through RAG-E-V006-004 | The Sumi referral produces an observable training effect; later repetition and generality remain unknown. | STRENGTHENED in V006 from working hypothesis. |
| RAG-CLM-016 | Mami converts observed relationship anomalies into researched and purchased access, using the service system to challenge the service-created public bond. | STRONG_INFERENCE | RAG-E-V005-017, RAG-E-V006-005, RAG-E-V006-008, RAG-E-V006-011, RAG-E-V006-014 | Her operational intervention is clear, but desired endpoint and deeper motive remain unresolved. | ADDED and supported in V006. |
| RAG-CLM-017 | Kazuya's clearest romantic self-knowledge emerges through moral admiration and cumulative care, while communication still fails or remains incomplete at direct address. | STRONG_INFERENCE | RAG-E-V006-007, RAG-E-V006-012, RAG-E-V006-015, RAG-E-V006-016, RAG-E-V006-017 | Chizuru's interpretation and response are withheld; clarity of preference does not establish relational competence or reciprocity. | ADDED and supported in V006. |
| RAG-CLM-018 | Chizuru can respond to vocational defeat while preserving professional classification and selectively granting a trusted client unpriced ordinary and family access. | STRONG_INFERENCE | RAG-E-V007-004 through RAG-E-V007-006, RAG-E-V007-011 through RAG-E-V007-013 | Acting persistence, professional fairness, trust, family need, and personal attachment remain compatible motives; no romantic self-report occurs. | ADDED and supported in V007. |
| RAG-CLM-019 | Sayuri's family account identifies Chizuru's visible strength as protective performance around vulnerability. | WORKING_HYPOTHESIS | RAG-E-V007-014 | The account is close-observer testimony rather than Chizuru's direct present-tense interior report. | ADDED in V007 with source limit retained. |
| RAG-CLM-020 | Chizuru can disclose core family and vocational history while reclassifying the closeness produced by that disclosure through rental-girlfriend language. | STRONG_INFERENCE | RAG-E-V008-004 through RAG-E-V008-008 | Disclosure and re-bounding coexist; neither proves romantic acknowledgment or emotional absence. | ADDED and supported in V008. |
| RAG-CLM-021 | Provisional girlfriend status does not settle consent or reciprocity: ordinary couple conduct and sexual pressure can coexist with refusal and nonreciprocal feeling. | STRONG_INFERENCE | RAG-E-V008-009 through RAG-E-V008-014 | Ruka's effort and Kazuya's attraction are represented, but no sex, reciprocal love, or completed official conversion follows. | ADDED and supported in V008. |
| RAG-CLM-022 | Kazuya can convert social-identity threat into costly protection, while Chizuru can answer the resulting burden with chosen care and still verbally constrain its meaning. | STRONG_INFERENCE | RAG-E-V009-005 through RAG-E-V009-011 | The protection method is reckless, the care motive remains plural, and no mutual status change follows. | ADDED and supported in V009. |
| RAG-CLM-023 | Mami converts both researched and incidental relationship anomalies into new investigative access or attention. | STRONG_INFERENCE | RAG-E-V005-017, RAG-E-V006-005, RAG-E-V006-008, RAG-E-V006-011, RAG-E-V009-012 through RAG-E-V009-015 | The operational pattern repeats, but her desired endpoint and the next action after the train sighting remain unknown. | ADDED and supported in V009; extends RAG-CLM-016. |
| RAG-CLM-024 | Paid relationship performance can contain scripted physical intimacy and genuine information, pride, or encouragement simultaneously; the service frame neither proves nor erases private feeling. | STRONG_INFERENCE | RAG-E-V010-004 through RAG-E-V010-010 | The evidence distinguishes observable conduct and stated work meaning from unreported romantic motive. | ADDED and supported in V010. |
| RAG-CLM-025 | Technical and family-mediated routes can convert contingent contact into chosen non-booking coordination, but each use remains bounded by context rather than creating general entitlement. | STRONG_INFERENCE | RAG-E-V009-010, RAG-E-V010-011 through RAG-E-V010-014, RAG-E-V010-016, RAG-E-V010-017, RAG-E-V011-001, RAG-E-V011-007 | Repeated crisis use strengthens the route but still does not establish unrestricted access. | STRENGTHENED through V011. |
| RAG-CLM-026 | Ruka's status strategy converts perceived competition into unilateral physical and public escalation, widening the gap between sincere claim and mutual agreement. | STRONG_INFERENCE | RAG-E-V008-012 through RAG-E-V008-014, RAG-E-V009-013, RAG-E-V009-014, RAG-E-V010-003, RAG-E-V010-014, RAG-E-V010-015, RAG-E-V011-002, RAG-E-V011-004, RAG-E-V011-013, RAG-E-V011-014 | Sympathy, apology, and sincere feeling are real counterweights but do not supply Kazuya's consent or reciprocation. | STRENGTHENED through V011. |
| RAG-CLM-027 | Family belief can become a material obligation: the heirloom ring carries care, emergency value, and coercive pressure through the same object. | STRONG_INFERENCE | RAG-E-V011-006, RAG-E-V011-011, RAG-E-V011-012 | Chizuru redirects custody to Kazuya, and no engagement or later use is established. | ADDED and supported in V011. |
| RAG-CLM-028 | Limited time converts the false relationship into an explicit ethical conflict between factual disclosure and protective comfort. | STRONG_INFERENCE | RAG-E-V011-007 through RAG-E-V011-012 | Neither strategy is completed in V011, and Sayuri's own informed preference is unavailable. | ADDED and supported in V011. |
| RAG-CLM-029 | Communication competence can grow through observation, writing, itinerary design, execution, listening, and shared affect even when spontaneous speech remains difficult. | STRONG_INFERENCE | RAG-E-V011-015 through RAG-E-V011-018, RAG-E-V012-001, RAG-E-V012-003, RAG-E-V012-004, RAG-E-V012-006, RAG-E-V012-007 | The completed aquarium sequence is consequential but does not establish broad independent provider competence or fluent speech. | STRENGTHENED through V012. |
| RAG-CLM-030 | Romantic recognition and disclosure access are separable: Sumi's love confession remains unheard while she becomes a consequential confidant. | STRONG_INFERENCE | RAG-E-V012-002, RAG-E-V012-004 through RAG-E-V012-007 | One relationship and one unheard utterance do not establish a universal pattern. | ADDED and supported in V012. |
| RAG-CLM-031 | When emotional concern acquires a concrete route, Kazuya can convert helplessness into researched, non-entitlement project support. | STRONG_INFERENCE | RAG-E-V012-005, RAG-E-V012-007, RAG-E-V012-016 through RAG-E-V012-020 | Research and commitment precede execution; competence, funds, personnel, and delivery remain untested. | ADDED and supported in V012. |
| RAG-CLM-032 | Chizuru's acting purpose is an intergenerational promise rooted in Sayuri's screen legacy and Katsuhito's encouragement and death, so vocational failure can reactivate grief and family obligation. | STRONG_INFERENCE | RAG-E-V012-008 through RAG-E-V012-015 | The history explains represented pressure without reducing every acting decision to one motive or guaranteeing success. | ADDED and supported in V012. |
| RAG-CLM-033 | The film agreement crosses from paid access and verbal support into a voluntary joint production commitment without itself establishing romantic reciprocity. | STRONG_INFERENCE | RAG-E-V012-016 through RAG-E-V012-022 | No campaign, contract, production result, or mutual romantic classification exists at the cutoff. | ADDED and supported in V012. |
| RAG-CLM-034 | The film project creates a distinct work relation with professional disclosure, financial parity, task division, and private access whose scope is repeatedly distinguished from girlfriend service and romance. | STRONG_INFERENCE | RAG-E-V013-001 through RAG-E-V013-004, RAG-E-V013-007 through RAG-E-V013-011 | Shared labor and domestic-looking care do not reveal a unique private motive. | ADDED and supported in V013. |
| RAG-CLM-035 | Kazuya can respond to external correction by revising a concrete plan rather than collapsing into self-description or abandoning it. | STRONG_INFERENCE | RAG-E-V013-005, RAG-E-V013-015, RAG-E-V013-020 through RAG-E-V013-022 | Platform approval precedes fundraising and production; general competence remains unproved. | ADDED and supported in V013. |
| RAG-CLM-036 | Third-party observers can interpret project intimacy romantically while also supplying real labor, so social reading and operational contribution must be tracked separately. | STRONG_INFERENCE | RAG-E-V013-012 through RAG-E-V013-016 | Mini's first task and reliability remain unobserved, and her reading is not the pair's self-report. | ADDED and supported in V013. |
| RAG-CLM-037 | Informed project consent can coexist with incomplete relationship information: Sayuri authorizes the film campaign and endorses Kazuya while still lacking the rental truth. | STRONG_INFERENCE | RAG-E-V013-017 through RAG-E-V013-019 | Her campaign consent is valid within its disclosed scope, but relational advice rests on a false premise. | ADDED and supported in V013. |
| RAG-CLM-038 | Public project infrastructure distributes causal agency: backers, platform metrics, specialists, rewards, and street outreach can each enable or block a private promise. | STRONG_INFERENCE | RAG-E-V014-002, RAG-E-V014-007 through RAG-E-V014-014, RAG-E-V014-018 | The project remains unfunded and unfinished, so no one mechanism is sufficient. | ADDED and supported in V014. |
| RAG-CLM-039 | Kazuya can operationalize attachment through sustained, correctable production labor across reading, rights outreach, director recruitment, and public rejection. | STRONG_INFERENCE | RAG-E-V014-007 through RAG-E-V014-010, RAG-E-V014-014 | The pattern remains tied to Chizuru and coexists with self-blame and financial strain. | ADDED and supported in V014. |
| RAG-CLM-040 | Mini's creator and crowdfunding literacy is consequential labor, while her romantic interpretations remain separate claims requiring independent evidence. | STRONG_INFERENCE | RAG-E-V014-004, RAG-E-V014-005, RAG-E-V014-011 through RAG-E-V014-013, RAG-E-V014-019 | Her campaign work is observed; her relationship claim is not yet tested by Chizuru's response. | ADDED and supported in V014; extends RAG-CLM-036. |
| RAG-CLM-041 | Chizuru governs project exposure by calibrated consent: she can offer image, story, labor, and personal property while preserving a distinct intimate boundary and withholding romantic reclassification. | STRONG_INFERENCE | RAG-E-V014-003, RAG-E-V014-007, RAG-E-V014-012, RAG-E-V014-013, RAG-E-V014-016, RAG-E-V014-017 | The later reward publication and response to Mini's disclosure are unknown. | ADDED and supported in V014. |
| RAG-CLM-042 | Ruka's rivalry can coexist with costly prosocial support when Kazuya's burden is concrete, without repairing the unresolved provisional relation or consent history. | STRONG_INFERENCE | RAG-E-V014-012, RAG-E-V014-013, RAG-E-V014-015, RAG-E-V014-020 | One flyer sequence does not establish durable subordination of rivalry or broader change. | ADDED and supported in V014. |
| RAG-CLM-043 | An unauthorized third-party disclosure can change information and interaction without making the discloser's romantic interpretation authoritative. | STRONG_INFERENCE | RAG-E-V015-001, RAG-E-V015-002 | Chizuru responds and conduct changes, but Mini's confidence remains her inference. | ADDED and supported in V015. |
| RAG-CLM-044 | Chizuru's direct classification shifts from separating gratitude and romance to a qualified non-negation, but the shift remains ambivalent and creates no mutual status. | STRONG_INFERENCE | RAG-E-V014-017, RAG-E-V015-005, RAG-E-V015-007 | The paired statements include explicit negation, no affirmative confession, and no response from Kazuya. | ADDED and supported in V015. |
| RAG-CLM-045 | Distributed promotional labor becomes financially consequential when it crosses an all-or-nothing threshold; gross support, net transfer, and total bank balance remain distinct quantities. | STRONG_INFERENCE | RAG-E-V015-003, RAG-E-V015-004, RAG-E-V015-008, RAG-E-V015-009 | The evidence cannot allocate marginal causal value among tactics or treat the account balance as campaign support. | ADDED and supported in V015. |
| RAG-CLM-046 | Umi's campaign help and romantic self-positioning coexist, so useful social capital does not require assigning either pure altruism or a proved quid pro quo. | STRONG_INFERENCE | RAG-E-V015-003, RAG-E-V015-006 through RAG-E-V015-008 | Timing and topic shift support mixed motives, but no explicit bargain or coercive condition is stated. | ADDED and supported in V015. |
| RAG-CLM-047 | The film converts Kazuya's attachment-driven preparation into an operational producer role inside specialist-led production, where his value lies largely in coordination, endurance, and bottleneck removal rather than artistic command. | STRONG_INFERENCE | RAG-E-V015-010 through RAG-E-V015-015 | Principal photography is incomplete, bodily risk complicates competence, and Tabuse and crew hold specialist authority. | ADDED and supported in V015. |
| RAG-CLM-048 | Ruka can repeat project-first cooperation when Sayuri's welfare and Kazuya's burden are concrete, while rivalry and the unresolved provisional relation remain intact. | STRONG_INFERENCE | RAG-E-V014-015, RAG-E-V015-004, RAG-E-V015-017 | Two campaign sequences do not establish generalized restraint or repair earlier consent failures. | ADDED and supported in V015; strengthens RAG-CLM-042. |
| RAG-CLM-049 | Chizuru directly rejects the hierarchy Kazuya builds from her acting success and validates his producer labor without changing their formal relationship. | STRONG_INFERENCE | RAG-E-V016-001, RAG-E-V016-002 | Her statements establish value and no regret, not romantic love or a new label. | ADDED and supported in V016. |
| RAG-CLM-050 | The film completes principal photography and enters editing, September-target planning, and theater arrangement, while completion, screening, and delivery remain open. | OBSERVATION | RAG-E-V016-012, RAG-E-V016-013 | No finished edit, booked exhibition, or delivery to Sayuri is observed. | ADDED and supported in V016. |
| RAG-CLM-051 | Chizuru identifies the film as a route for fulfilling a family promise after Katsuhito's death and thanks Kazuya for making that route possible. | STRONG_INFERENCE | RAG-E-V016-010 through RAG-E-V016-012 | Family purpose, happiness, and gratitude do not constitute romantic confession. | ADDED and supported in V016. |
| RAG-CLM-052 | Chizuru's private recall, chosen travel care, nighttime wakefulness, and return-trip response strengthen evidence of affective activation while stopping short of shared or affirmative romantic classification. | WORKING_HYPOTHESIS | RAG-E-V016-005, RAG-E-V016-006, RAG-E-V016-014 through RAG-E-V016-016 | Motives remain plural; the nighttime framing proves no contact, and Kazuya receives no direct answer. | ADDED in V016 with ambiguity preserved. |
| RAG-CLM-053 | Mini's unauthorized engineering creates two-person privacy and a conditional shared-room decision, then produces Ruka's confrontation; spatial access changes without sexual consent or couple status. | STRONG_INFERENCE | RAG-E-V016-004, RAG-E-V016-008, RAG-E-V016-014, RAG-E-V016-017 | Project necessity and financial choice constrain the access, and Ruka did not consent to the false absence story. | ADDED and supported in V016. |
| RAG-CLM-054 | Ruka turns a birthday wish and prior project labor into an explicit request for bodily contact, but V016 ends before Kazuya answers or any act occurs. | OBSERVATION | RAG-E-V016-018 | The request cannot be treated as consent, contact, or reciprocal intimacy. | ADDED and supported in V016. |
| RAG-CLM-055 | Explicit consent remains divisible by act: Kazuya accepts sunscreen application, blocks a later hug, and separately permits first-name address. | STRONG_INFERENCE | RAG-E-V017-001, RAG-E-V017-002, RAG-E-V017-004 | The naming permission changes social access but does not generalize to touch or relationship status. | ADDED and supported in V017. |
| RAG-CLM-056 | Ruka continues to interpret physiological response, deliberately extended time, and symbolic recognition as evidence for her chosen romantic persistence, while reciprocity remains absent. | STRONG_INFERENCE | RAG-E-V017-002 through RAG-E-V017-004, RAG-E-V017-007 | Her pulse and destiny language are her self-account; Kazuya's bounded answers and blocked hug contradict mutual-status inference. | ADDED and supported in V017. |
| RAG-CLM-057 | Film delivery advances from general postproduction to a September 30 screening plan in a 200-seat wheelchair-accessible cinema, while the edit and exhibition remain unfinished. | OBSERVATION | RAG-E-V017-005, RAG-E-V017-008 | A reserved and inspected venue is not evidence that the finished film screened. | ADDED and supported in V017. |
| RAG-CLM-058 | Sayuri is a consequential close observer and grateful project recipient, but her romantic inference about Chizuru and Kazuya is constrained by incomplete relationship information. | STRONG_INFERENCE | RAG-E-V017-006, RAG-E-V017-009, RAG-E-V017-010 | She lacks the rental truth, and neither principal supplies mutual romantic classification. | ADDED and supported in V017. |
| RAG-CLM-059 | Chizuru reaffirms acting as a chosen pursuit despite hardship and family obligation, while Sayuri's collapse threatens the intended film-delivery function. | STRONG_INFERENCE | RAG-E-V017-011 through RAG-E-V017-015 | Chosen vocation does not guarantee career success, medical recovery, or completed delivery. | ADDED and supported in V017. |
| RAG-CLM-060 | Sayuri's critical state reopens the truth-versus-comfort conflict: Chizuru defends a happy final belief, Kazuya prioritizes her feelings and initiates an alternative action, but no correction or outcome is yet shown. | STRONG_INFERENCE | RAG-E-V017-015 through RAG-E-V017-018 | Sayuri supplies no informed preference, Chizuru's full wish remains conflicted, and the LINE-and-running action is incomplete. | ADDED and supported in V017. |
| RAG-CLM-061 | Under terminal time pressure, incomplete creative work can still perform its core care function when Kazuya adapts available footage and equipment to Sayuri's bedside. | STRONG_INFERENCE | RAG-E-V018-001, RAG-E-V018-007 | Private access does not equal finished editing, public screening, or full fulfillment of every production promise. | ADDED and supported in V018. |
| RAG-CLM-062 | Chizuru's comfort-first ethic is not simple refusal of truth: she attempts the central correction, while Sayuri responds by entrusting the answer rather than demanding exhaustive fact. | STRONG_INFERENCE | RAG-E-V018-002, RAG-E-V018-005, RAG-E-V018-006 | Rental details and Sayuri's final factual belief remain unknown. | ADDED and supported in V018. |
| RAG-CLM-063 | The final grandmother-granddaughter exchange achieves direct relational closure through film acknowledgment, touch, and reciprocal love even though factual relationship knowledge remains incomplete. | STRONG_INFERENCE | RAG-E-V018-004 through RAG-E-V018-008 | Emotional closure does not retroactively make the deception informed or establish Kazuya-Chizuru couple status. | ADDED and supported in V018. |
| RAG-CLM-064 | Chizuru's polished `fine` presentation persists through bereavement and funeral labor, while Sumi, Nagomi, and Kazuya supply independent evidence that composure is not equivalent to absent support need. | STRONG_INFERENCE | RAG-E-V018-009 through RAG-E-V018-013 | Observers cannot identify her complete interior state or preferred helper. | ADDED and supported in V018. |
| RAG-CLM-065 | Sumi's support competence includes converting empathy into an experiential method of low-demand enjoyment and direct encouragement. | STRONG_INFERENCE | RAG-E-V018-012 through RAG-E-V018-015 | The method's effect on Chizuru and Sumi's broader competence remain untested. | ADDED and supported in V018. |
| RAG-CLM-066 | Kazuya can operationalize care through consultation, earned resources, planning, and an answerable rental request rather than claiming informal lover access. | STRONG_INFERENCE | RAG-E-V018-014 through RAG-E-V018-020 | The booking is prospective; acceptance, helpfulness, and reciprocity remain unknown. | ADDED and supported in V018. |
| RAG-CLM-067 | A paid all-day route can contain sincere enjoyment and effective support while payment remains insufficient to buy grief disclosure, bodily reliance, or romantic status. | STRONG_INFERENCE | RAG-E-V019-001 through RAG-E-V019-008, RAG-E-V019-015, RAG-E-V019-020 | The mixture is established for one unusually long booking and should not be generalized to every rental interaction. | ADDED and supported in V019. |
| RAG-CLM-068 | Chizuru's controlled strength can break when precise recognition permits rather than demands grief; her later reset does not negate the release. | STRONG_INFERENCE | RAG-E-V019-009 through RAG-E-V019-016, RAG-E-V019-020 | One acute episode does not establish a stable support rule or completed bereavement. | ADDED and supported in V019. |
| RAG-CLM-069 | Kazuya shows improved support competence by combining tailored activity, cost-bearing action, recognition of concealment, and non-demanding presence. | STRONG_INFERENCE | RAG-E-V019-001 through RAG-E-V019-017 | His method is expensive, context-specific, and validated by one later self-report rather than a general test. | ADDED and supported in V019. |
| RAG-CLM-070 | Chizuru directly reports that crying before Kazuya relieved severe loneliness while explicitly retaining the rental-girlfriend and non-boyfriend classification. | OBSERVATION | RAG-E-V019-020 | Relief does not reveal durable recovery, romantic motive, or future relationship choice. | ADDED and supported in V019. |
| RAG-CLM-071 | The crowdfunded film reaches public exhibition and receives local applause, completing the delivery sequence without establishing wider distribution or career breakthrough. | OBSERVATION | RAG-E-V020-001 | One screening and audience response do not establish commercial or professional success. | ADDED and supported in V020. |
| RAG-CLM-072 | Chizuru's acting commitment survives Sayuri's death as an explicitly self-endorsed vocation: she says production was enjoyable, acting is something she likes, and she expects to continue. | STRONG_INFERENCE | RAG-E-V020-002 | Intention and enjoyment do not guarantee a next role or stable career. | ADDED and supported in V020. |
| RAG-CLM-073 | Unbooked ordinary access, professional reaccounting, gratitude, direct romantic inquiry, and renewed rental classification can coexist in one interaction without reducing to either pure service or established couplehood. | STRONG_INFERENCE | RAG-E-V020-009 through RAG-E-V020-018 | The sequence is shaped by bereavement aftermath, alcohol, and an unresolved question. | ADDED and supported in V020. |
| RAG-CLM-074 | Mini's unauthorized romantic disclosure has a direct causal consequence when Chizuru cites it while asking Kazuya whether he likes her. | OBSERVATION | RAG-E-V020-015, RAG-E-V020-016 | Causal use does not validate Mini's interpretation or authorize the disclosure. | ADDED and supported in V020. |
| RAG-CLM-075 | Kazuya converts internal love into personally identifying speech by naming Chizuru as his ideal girlfriend and beginning a direct declaration, but interruption prevents a completed mutual confession. | OBSERVATION | RAG-E-V020-019 through RAG-E-V020-021 | Chizuru's affected replay supplies no affirmative answer or final classification. | ADDED and supported in V020. |
| RAG-CLM-076 | Mami can turn accumulated social information into legitimate-looking family access through Kibe and a business proposal while her desired endpoint remains opaque. | STRONG_INFERENCE | RAG-E-V020-022, RAG-E-V020-023 | Genuine work interest and instrumental access can coexist; sabotage or renewed romance is not established. | ADDED and supported in V020. |
| RAG-CLM-077 | Sexualized or couple-coded staging does not determine consent: activity terms, a specific offer, and an explicit answer govern each act separately. | STRONG_INFERENCE | RAG-E-V023-001 through RAG-E-V023-005 | One pool sequence does not establish all future boundary conduct or broader romantic agreement. | ADDED and supported in V023. |
| RAG-CLM-078 | Mami's concern language can coexist with platform research, selective warning, trust testing, and disclosure leverage, so presentation does not by itself settle protective or adversarial motive. | STRONG_INFERENCE | RAG-E-V023-004, RAG-E-V023-006, RAG-E-V023-008 through RAG-E-V023-016 | Mixed methods support motive pluralism but do not prove that concern is false or identify a final endpoint. | ADDED and supported in V023. |
| RAG-CLM-079 | After Kazuya's withdrawal, Ruka expands unilateral status performance through public declaration, deceptive isolation, bodily pressure, and repeated fabricated sexual evidence. | STRONG_INFERENCE | RAG-E-V023-012, RAG-E-V023-013, RAG-E-V023-016, RAG-E-V023-017 | Kazuya's objections and denial remain explicit; Ruka's sincere feeling does not create consent or truth. | ADDED and supported in V023; strengthens the V021-V022 separation finding. |
| RAG-CLM-080 | Kazuya can initiate selective truth correction under exposure pressure, but he still sequences public correction behind an unresolved confession and thereby preserves the larger deception. | STRONG_INFERENCE | RAG-E-V023-008 through RAG-E-V023-010, RAG-E-V023-019 | One candid conversation with Mami does not establish durable honesty or completed family correction. | ADDED and supported in V023. |
| RAG-CLM-081 | Chizuru can move consequential rival information from private uncertainty into direct source checking without that act itself revealing a romantic or final trust judgment. | STRONG_INFERENCE | RAG-E-V023-016 through RAG-E-V023-018 | The brief question lacks a full debrief, explicit belief update, or relationship answer. | ADDED and supported in V023. |
| RAG-CLM-082 | Chosen-family inclusion can become directly valuable to Chizuru through Sayuri's remembered teaching while remaining ethically entangled with the false couple premise. | STRONG_INFERENCE | RAG-E-V023-008, RAG-E-V023-020 through RAG-E-V023-022 | Gratitude, belonging, and a best-day appraisal do not validate deception, complete ring return, or establish romance. | ADDED and supported in V023. |
| RAG-CLM-083 | Mami can combine accurate facts, selective omission, rescue language, and coercive verification into one public exposure performance; factual components do not make her framing neutral. | STRONG_INFERENCE | RAG-E-V026-001, RAG-E-V026-004, RAG-E-V026-009, RAG-E-V026-015 | Her full motive, exact pre-drop screen preparation, and next response remain unresolved. | ADDED and supported in V026. |
| RAG-CLM-084 | Kazuya's sincere public love declaration coexists with a knowingly false mutual-dating timeline, so affective truth and status truth must be adjudicated separately. | OBSERVATION | RAG-E-V026-007, RAG-E-V026-008 | His feeling supplies no evidence that Chizuru agreed to date him before or during the scene. | ADDED and supported in V026. |
| RAG-CLM-085 | Chizuru's two deliberate kisses, real-name disclosure, and statement that Kazuya became important are strong evidence of personal investment, while coercive public conditions and the explicit residual lie prevent promotion to a private mutual dating classification. | STRONG_INFERENCE | RAG-E-V026-012 through RAG-E-V026-016 | A later private debrief or direct self-classification could alter the prospective state but cannot retroactively make the V026 public claim true. | ADDED and supported in V026. |
| RAG-CLM-086 | Near-total correction can preserve a structurally central deception: the room account removes almost every falsehood while retaining genuine dating as the sole lie that determines family interpretation. | OBSERVATION | RAG-E-V026-016 | The summarized account does not enumerate every disclosed detail, and later correction remains possible. | ADDED and supported in V026. |
| RAG-CLM-087 | Ruka can reject an exposure method and protect the principals at personal cost without relinquishing her own attachment, disputed status claim, or prior deceptive conduct. | STRONG_INFERENCE | RAG-E-V026-009, RAG-E-V026-010, RAG-E-V026-016 | V026 ends before her next action and supplies no withdrawal or repair of the fabricated sex claim. | ADDED and supported in V026. |
| RAG-CLM-088 | Immediate family acceptance after disclosure is evidence-responsive but not fully informed when it rests on the residual dating lie; Kibe's and Kazuo's violence remains a separate trust and boundary failure. | STRONG_INFERENCE | RAG-E-V026-006, RAG-E-V026-016 | Later family treatment, apology, scrutiny, or renewed rejection remains open. | ADDED and supported in V026. |
| RAG-CLM-089 | Ordinary treatment can resume while the residual dating claim remains under direct peer scrutiny. | OBSERVATION | RAG-E-V027-001, RAG-E-V027-005 | Nagomi's normalization and Kuribayashi's challenge do not establish every observer's final belief or durable trust repair. | ADDED and supported in V027. |
| RAG-CLM-090 | Ruka converts her V026 conflict into direct professional and access pressure against Chizuru without relinquishing her own disputed claim. | OBSERVATION | RAG-E-V027-002, RAG-E-V027-007 | Her grievance does not authorize grabbing, emotional compulsion, or control over Chizuru's employment and access. | ADDED and supported in V027. |
| RAG-CLM-091 | Chizuru can admit professional wrongdoing and share responsibility while rejecting both Ruka's totalizing accusation and Kazuya's unilateral heroic blame. | STRONG_INFERENCE | RAG-E-V027-002, RAG-E-V027-004 | More balanced accountability does not correct the residual dating lie or settle romantic status. | ADDED and supported in V027. |
| RAG-CLM-092 | Chizuru's private thought that she cannot like a customer supplies direct evidence of personally salient attraction or attachment constrained by the professional category. | STRONG_INFERENCE | RAG-E-V027-006 | The thought does not establish a final love label, intention to date, or reciprocal agreement. | ADDED and supported in V027. |
| RAG-CLM-093 | Prolonged silence is an observable Chizuru choice rather than evidence that she is absent or hates Kazuya. | OBSERVATION | RAG-E-V027-008, RAG-E-V027-009 | Her full motive is withheld, and chosen avoidance can still cause substantial harm. | ADDED and supported in V027. |
| RAG-CLM-094 | Mini can interrupt self-confirming rejection and prompt useful inquiry while her confident love label remains an interested interpretation rather than narrator authority. | STRONG_INFERENCE | RAG-E-V027-010 through RAG-E-V027-012 | Helpful consequence does not establish permission, omniscience, or the correctness of every romantic inference. | ADDED and supported in V027. |
| RAG-CLM-095 | Roughly three months without contact end through a system-mediated rental booking, so restored access and continued professional distance arise from the same act. | OBSERVATION | RAG-E-V027-009, RAG-E-V027-013 through RAG-E-V027-015 | Platform acceptance and paid attendance do not establish personal acceptance or resolved feeling. | ADDED and supported in V027. |
| RAG-CLM-096 | The paid date makes client status both a communication route and a barrier: it creates bounded contact, cost, performance ambiguity, and a clock for direct speech. | STRONG_INFERENCE | RAG-E-V027-013 through RAG-E-V027-015 | Chizuru's initiated statement and the wrapper's eventual disposition remain beyond the volume cut. | ADDED and supported in V027. |
| RAG-CLM-097 | Direct apology and first-person explanation can end prolonged silence without retroactively making avoidance harmless. | STRONG_INFERENCE | RAG-E-V028-001 through RAG-E-V028-004 | Chizuru explains Ruka-linked concern and responsibility, but the complete motive and accumulated cost remain partly unresolved. | ADDED and supported in V028. |
| RAG-CLM-098 | Chizuru converts uncertainty into a structured investigation and promised answer while refusing both a convenient love label and a false rejection. | OBSERVATION | RAG-E-V028-003, RAG-E-V028-004, RAG-E-V028-006 | The method is improvised and V028 supplies no result or mutual status. | ADDED and supported in V028. |
| RAG-CLM-099 | Rental work is simultaneously a professional rule system, valued practice, and material support for tuition and expenses; a rule breach does not reduce it to disguise or disposable obstacle. | OBSERVATION | RAG-E-V028-003, RAG-E-V028-004 | Continued employment does not settle whether the kisses had romantic meaning or how future bookings will be governed. | ADDED and supported in V028. |
| RAG-CLM-100 | The professional “Mizuhara” presentation and Chizuru's whole person are analytically distinguishable roles without constituting separate selves. | STRONG_INFERENCE | RAG-E-V028-004 | Kazuya's answer does not establish how accurately he knows every private domain, and Chizuru's worry remains consequential. | ADDED and supported in V028. |
| RAG-CLM-101 | Chizuru operationalizes the investigation through direct status inquiry, bounded private observation, ordinary messaging, vocational access, and family-house labor. | STRONG_INFERENCE | RAG-E-V028-004 through RAG-E-V028-010, RAG-E-V028-013 through RAG-E-V028-015 | Access expansion has multiple practical causes and does not establish a favorable answer. | ADDED and supported in V028. |
| RAG-CLM-102 | Concern for Ruka becomes an explicit constraint on Chizuru's choices without granting Ruka authority over Chizuru's work, access, or final feeling. | STRONG_INFERENCE | RAG-E-V028-001, RAG-E-V028-006, RAG-E-V028-009 | No workable separation, corrected fabrication, or mutually accepted boundary is observed. | ADDED and supported in V028. |
| RAG-CLM-103 | Ordinary communication can resume beyond paid time while romantic classification, the residual dating lie, and rival status all remain unresolved. | OBSERVATION | RAG-E-V028-004 through RAG-E-V028-010 | Message warmth, privacy, and duration do not themselves create a relationship agreement. | ADDED and supported in V028. |
| RAG-CLM-104 | Practical labor at Chizuru's childhood home turns post-bereavement property transition and family memory into shared access without making the task romantic by default. | STRONG_INFERENCE | RAG-E-V028-013 through RAG-E-V028-015 | Sale, retained objects, the photograph explanation, and later access remain open. | ADDED and supported in V028. |

## Competing hypotheses

| Hypothesis ID | Formulation | Supporting evidence | Limitation / discriminator |
|---|---|---|---|
| RAG-HYP-001 | Chizuru's exceptional help and defense are entirely professional. | Pride in satisfaction, payment rules, girlfriend register. | Weakened if she repeatedly chooses costly help outside role incentives; V001 family/fairness motives already prevent “mechanical compliance.” |
| RAG-HYP-002 | Chizuru's exceptional help already proves romantic attachment. | Beauty framing, repeated chosen continuation, direct defense. | Not discriminated from family empathy, fairness, or professional investment in V001. |
| RAG-HYP-003 | Mami's separation goal is motivated by jealousy, residual attachment, status threat, control, or a mixture. | Reaction to the girlfriend claim, explicit breakup goal, identity appropriation, deliberate kiss, and private meeting. | Operational goal is now observed, but no decisive evidence ranks its deeper causes or desired endpoint. |

## Adjudicated predictions from the V001 boundary

| Prediction ID | Adjudication | V002 basis | Limit |
|---|---|---|---|
| RAG-PRED-001 | SUPPORTED | Extension invoice and discharge-week booking; RAG-E-V002-002, RAG-E-V002-011. | Later durability of the weekly rule remains open. |
| RAG-PRED-002 | SUPPORTED | Identity repair, intimacy pressure, breakup reaction, fight, tickets, and planned disclosure; RAG-E-V002-007, RAG-E-V002-008, RAG-E-V002-012, RAG-E-V002-014, RAG-E-V002-015. | Does not predict every friend's later response. |
| RAG-PRED-003 | SUPPORTED | Separation goal, probe, identity appropriation, kiss, and scheduled meeting; RAG-E-V002-003, RAG-E-V002-005, RAG-E-V002-007, RAG-E-V002-009, RAG-E-V002-016. | Underlying motive remains unresolved. |
| RAG-PRED-004 | SUPPORTED | Reunion search and memory inflation coexist with service-based discounting and contrary action; RAG-E-V002-005, RAG-E-V002-006, RAG-E-V002-010, RAG-E-V002-017. | Support is bounded to the observed relationships and pressure contexts. |

## Adjudicated predictions from the V002 boundary

| Prediction ID | Adjudication | V003 basis | Limit |
|---|---|---|---|
| RAG-PRED-005 | SUPPORTED | Reciprocal rescue, hospital care, Kibe's interpretation, renewed booking, and narrow extension; RAG-E-V003-001, RAG-E-V003-003, RAG-E-V003-004, RAG-E-V003-005, RAG-E-V003-009. | Does not prove romance or indefinite continuation. |
| RAG-PRED-006 | SUPPORTED | The rescue cancels the pool meeting and intended confession; RAG-E-V003-002. | Mami's later response remains open. |
| RAG-PRED-007 | SUPPORTED | Kibe directs secrecy and interprets the rescue through the couple premise; the grandmothers create further pressure; RAG-E-V003-004, RAG-E-V003-006. | Does not predict every audience response. |
| RAG-PRED-008 | SUPPORTED | Chizuru invokes girlfriend, customer, touch-boundary, and rental frames after the rescue; RAG-E-V003-003, RAG-E-V003-008, RAG-E-V003-009, RAG-E-V003-010. | Role language does not settle private motive. |

## Adjudicated predictions from the V003 boundary

| Prediction ID | Adjudication | V004 basis | Limit |
|---|---|---|---|
| RAG-PRED-009 | SUPPORTED | Ruka explains that Kuribayashi was a rental client and supplies her work motive; RAG-E-V004-001, RAG-E-V004-006, RAG-E-V004-007. | Exact terms and his full knowledge remain incomplete. |
| RAG-PRED-010 | SUPPORTED | Kazuya refuses ordinary dating without mutual feeling, then accepts a trial for Chizuru; the Mami plan does not resume; RAG-E-V004-004, RAG-E-V004-005, RAG-E-V004-010. | Does not establish mature treatment of either woman. |
| RAG-PRED-011 | SUPPORTED | Ruka conditions secrecy on dating; RAG-E-V004-003. | Her later reassurance limits a purely destructive reading. |
| RAG-PRED-012 | SUPPORTED | Chizuru applies the real-girlfriend exit rule and encourages the trial; RAG-E-V004-005. | The status is provisional and coerced by the surrounding secret. |

## Adjudicated predictions from the V004 boundary

| Prediction ID | Adjudication | V005 basis | Limit |
|---|---|---|---|
| RAG-PRED-013 | SUPPORTED | Ruka presses sexual and relational availability and family recognition in the private room; RAG-E-V005-001. | Kazuya retreats, Ruka stops, and no sexual act occurs. |
| RAG-PRED-014 | SUPPORTED | Gift-motivated employment produces first wages and funds the Kuribayashi repair booking; RAG-E-V005-008, RAG-E-V005-009. | The gifts are not directly revisited in dialogue, and no couple transition follows. |
| RAG-PRED-015 | DISCONFIRMED | Chizuru's acting ambition has no practical consequence in V005. | Absence at this horizon does not show abandonment or invalidate V004 evidence. |
| RAG-PRED-016 | SUPPORTED | Karaoke work becomes routine, workplace collision, first pay, and friendship-repair infrastructure; RAG-E-V005-007, RAG-E-V005-008, RAG-E-V005-009. | Long-term job durability remains untested. |

## Adjudicated predictions from the V005 boundary

| Prediction ID | Adjudication | V006 basis | Limit |
|---|---|---|---|
| RAG-PRED-017 | SUPPORTED | Kazuya changes activities, reassures Sumi, averts his gaze after accidental exposure, and supplies an exit from unwanted attention; RAG-E-V006-001 through RAG-E-V006-003. | One date does not establish stable communication or broad maturity. |
| RAG-PRED-018 | SUPPORTED | Mami identifies Sumi's profile, books Chizuru, and attacks the continuing girlfriend performance; RAG-E-V006-005, RAG-E-V006-008, RAG-E-V006-011. | Her desired endpoint remains unknown. |
| RAG-PRED-019 | SUPPORTED | The shared workplace gives Ruka private access for a status discussion and lets her detect Kazuya's collision with Mami and Chizuru; RAG-E-V006-009, RAG-E-V006-010. | Ruka does not learn the complete confrontation. |
| RAG-PRED-020 | SUPPORTED | Kazuya acts as an entrusted training participant, and Sumi reaches a small expressive breakthrough; RAG-E-V006-001 through RAG-E-V006-004. | Training success remains bounded to one encounter. |

## Adjudicated predictions from the V006 boundary

| Prediction ID | Adjudication | V007 basis | Limit |
|---|---|---|---|
| RAG-PRED-021 | SUPPORTED | Chizuru immediately asks for clarification; Kazuya retreats into rental language and she reacts privately; RAG-E-V007-001, RAG-E-V007-002. | No mutual transition follows. |
| RAG-PRED-022 | DISCONFIRMED at V007 horizon | Mami does not appear and no consequence is observed. | Absence at this horizon does not show permanent abandonment. |
| RAG-PRED-023 | SUPPORTED | Casting loss postpones retirement and produces new bookings, income support, and continuing access; RAG-E-V007-004 through RAG-E-V007-006. | Long-term employment and acting outcome remain unknown. |
| RAG-PRED-024 | INCONCLUSIVE | Ruka does not appear. | V007 neither revisits the proposal nor treats her status as settled. |

## Adjudicated predictions from the V007 boundary

| Prediction ID | Adjudication | V008 basis | Limit |
|---|---|---|---|
| RAG-PRED-025 | SUPPORTED | The lost key immediately produces temporary apartment access and practical help; RAG-E-V008-001. | The access remains temporary and does not establish cohabitation. |
| RAG-PRED-026 | SUPPORTED | Kazuya asks Chizuru to move after accidental closeness, refuses Ruka's sexual escalation, and states non-entitled support; RAG-E-V008-002, RAG-E-V008-006, RAG-E-V008-012. | These bounded acts do not establish generalized maturity. |
| RAG-PRED-027 | SUPPORTED | Chizuru's family-linked acting dream reorganizes Kazuya's support purpose, while platform access also supplies the birthday and Sumi booking; RAG-E-V008-005, RAG-E-V008-006, RAG-E-V008-015. | Long-term acting and financial outcomes remain unknown. |
| RAG-PRED-028 | SUPPORTED | Kazuya answers private need with temporary help and restraint, then listens to Chizuru's family account and offers support; RAG-E-V008-001, RAG-E-V008-002, RAG-E-V008-004 through RAG-E-V008-008. | Chizuru re-bounds the exchange through rental service. |

## Adjudicated predictions from the V008 boundary

| Prediction ID | Adjudication | V009 basis | Limit |
|---|---|---|---|
| RAG-PRED-029 | SUPPORTED | Sumi's guidance produces a 2,500-yen practical gift that Kazuya delivers and Chizuru accepts; RAG-E-V009-001 through RAG-E-V009-004. | The gift creates no reciprocal status and required a 17,000-yen consultation. |
| RAG-PRED-030 | SUPPORTED | Kazuya reassures Chizuru that no sex occurred, and Ruka later claims current status and sex before Mami; RAG-E-V009-004, RAG-E-V009-013. | Kazuya does not disclose the kiss, and Ruka's sexual claim is false. |
| RAG-PRED-031 | SUPPORTED | Kazuya chooses the gift for usefulness against Chizuru's acting fatigue; RAG-E-V009-003. | One gift does not establish durable vocational support. |
| RAG-PRED-032 | SUPPORTED | Sumi persists through performance, written advice, a direct birthday question, and calendar entry; RAG-E-V009-001, RAG-E-V009-002. | Communication remains visibly effortful. |

## Adjudicated predictions from the V009 boundary

| Prediction ID | Adjudication | V010 basis | Limit |
|---|---|---|---|
| RAG-PRED-033 | SUPPORTED | Mami directly questions Chizuru and follows the Kinoshita family liquor-store account; RAG-E-V010-001, RAG-E-V010-002. | Her final goal and use of the family route remain unknown. |
| RAG-PRED-034 | SUPPORTED | Ruka apologizes for the Mami confrontation, then family competition and a unilateral kiss extend the same status pressure; RAG-E-V010-003, RAG-E-V010-014, RAG-E-V010-015. | The later escalation occurs before the family rather than in another direct Mami exchange. |
| RAG-PRED-035 | SUPPORTED | Chizuru accepts an unbooked family visit and uses direct LINE for a hospital crisis; RAG-E-V010-012, RAG-E-V010-016, RAG-E-V010-017. | Each access event remains context-bounded. |
| RAG-PRED-036 | DISCONFIRMED | June 1 and its family celebration pass without an observed Sumi message, gift, meeting, or other follow-up; RAG-E-V010-018. | The result is horizon-bounded and does not establish motive or any later conduct. |

## Adjudicated predictions from the V010 boundary

| Prediction ID | Adjudication | V011 basis | Limit |
|---|---|---|---|
| RAG-PRED-037 | SUPPORTED | Sayuri's hospitalization produces direct calling, Chizuru's return and later departure from the party, hospital coordination, and a truth crisis; RAG-E-V011-001, RAG-E-V011-007 through RAG-E-V011-012. | Diagnosis and longer prognosis remain unknown. |
| RAG-PRED-038 | DISCONFIRMED | No attendance, planning, spending, or practical-help action concerning the new stage opportunity occurs; RAG-E-V011-019. | The horizon-bounded result does not revoke Kazuya's earlier promise. |
| RAG-PRED-039 | DISCONFIRMED | Mami does not appear and her family-account route has no observed consequence; RAG-E-V011-020. | Later use remains possible. |
| RAG-PRED-040 | SUPPORTED | Ruka informs Chizuru, repeats unilateral kissing, then changes timing through a truce while preserving pursuit through a gift, cheek kiss, and declared rule change; RAG-E-V011-002, RAG-E-V011-004, RAG-E-V011-013, RAG-E-V011-014. | Tactical change does not resolve consent or status. |

## Adjudicated predictions from the V011 boundary

| Prediction ID | Adjudication | V012 basis | Limit |
|---|---|---|---|
| RAG-PRED-041 | SUPPORTED | Sumi invites and receives a substantive disclosure, shares Kazuya's grief, reduces his distress, and helps create the coping frame from which he identifies possible action; RAG-E-V012-004 through RAG-E-V012-007. | She does not explicitly suggest crowdfunding or a film. |
| RAG-PRED-042 | DISCONFIRMED | The truth disagreement and false relationship account are neither revisited nor acted on; RAG-E-V012-023. | The film project does not itself correct or renew the lie. |
| RAG-PRED-043 | DISCONFIRMED | The ring has no handling, disclosure, attempted return, concealment, or support use; RAG-E-V012-023. | Later material consequence remains possible. |
| RAG-PRED-044 | DISCONFIRMED | Ruka is absent, and her truce and declared kiss rule produce no observed conduct consequence; RAG-E-V012-024. | Later use remains possible. |

## Adjudications and revisions

At the V020 horizon, RAG-PRED-073 through RAG-PRED-076 are supported. Public screening completes the film's exhibition route; Chizuru reopens the grief episode through refund, self-description, gratitude, and ordinary access; Mini's disclosure directly prompts Chizuru's question; and Kazuya turns internal love into personally identifying but interrupted speech. V020 adds public completion, continuing vocation, mixed ordinary and professional access, a Mini-triggered question, an incomplete direct confession, and Mami's active family-business route as RAG-CLM-071 through RAG-CLM-076.

The V020 checkpoint and local reconstruction audit are the latest block-level synthesis and recovery boundary. The cumulative prediction record through V020 contains seventy-six adjudications: sixty-six supported, eight disconfirmed, one inconclusive, and one no-diagnostic. The V011-V020 block contributes forty adjudications: thirty-four supported and six disconfirmed. No V021 prediction set is frozen because V021 lies outside the authorized narrative run.

## Adjudicated predictions from the V012 boundary

| Prediction ID | Adjudication | V013 basis | Limit |
|---|---|---|---|
| RAG-PRED-045 | SUPPORTED | Task allocation, expert review, budgeting, revision, approval, and publication; RAG-E-V013-001 through RAG-E-V013-010, RAG-E-V013-020 through RAG-E-V013-022. | Launch begins at zero support and does not establish completion. |
| RAG-PRED-046 | SUPPORTED | Chizuru initiates and shapes non-booked work, contributions, and publication; RAG-E-V013-006 through RAG-E-V013-011, RAG-E-V013-021. | Project agency does not establish romance. |
| RAG-PRED-047 | SUPPORTED | Sayuri's time drives initial withholding, later permission, and rapid publication; RAG-E-V013-003, RAG-E-V013-017 through RAG-E-V013-022. | Exact prognosis remains unknown. |
| RAG-PRED-048 | SUPPORTED | Kazuya consults a CAMPFIRE planner and Mini joins as volunteer labor; RAG-E-V013-005, RAG-E-V013-014. | Their later contributions and production outcome remain unknown. |

## Adjudicated predictions from the V013 boundary

| Prediction ID | Adjudication | V014 basis | Limit |
|---|---|---|---|
| RAG-PRED-049 | SUPPORTED | The campaign reaches at least 150,000 yen on day one and later roughly 837,000 yen from 328 supporters; RAG-E-V014-002, RAG-E-V014-010. | Support remains below the all-or-nothing target. |
| RAG-PRED-050 | SUPPORTED | Mini analyzes the stall, convenes the team, designs recovery tactics, assigns labor, and coordinates reward selection; RAG-E-V014-004, RAG-E-V014-011 through RAG-E-V014-013, RAG-E-V014-016. | Final campaign impact remains unknown. |
| RAG-PRED-051 | SUPPORTED | Story search, adaptation outreach, repeated director contact, permission, and crew recruitment occur; RAG-E-V014-007 through RAG-E-V014-009. | Agreements precede actual preproduction and filming. |
| RAG-PRED-052 | SUPPORTED | Publication creates a stalled-audience problem, analytics review, reward redesign, flyer distribution, and conditional platform-recommendation work; RAG-E-V014-010 through RAG-E-V014-014, RAG-E-V014-018. | No privacy breach or reputational harm is established. |

## Adjudicated predictions from the V014 boundary

| Prediction ID | Adjudication | V015 basis | Limit |
|---|---|---|---|
| RAG-PRED-053 | SUPPORTED | Chizuru responds defensively and acts more coldly; Mini and Kazuya discuss the disclosure, and Chizuru later supplies a qualified non-negation; RAG-E-V015-001, RAG-E-V015-002, RAG-E-V015-007. | Response does not validate Mini's interpretation or establish reciprocity. |
| RAG-PRED-054 | SUPPORTED | Umi's post produces visible audience response, and the campaign closes at 1,850,000 yen against a 1,820,000-yen target; RAG-E-V015-008, RAG-E-V015-009. | Marginal attribution among simultaneous tactics remains unknown. |
| RAG-PRED-055 | SUPPORTED | The project advances beyond preproduction into a scheduled, staffed shoot under Tabuse; RAG-E-V015-011 through RAG-E-V015-015. | Principal photography, postproduction, and delivery remain incomplete. |
| RAG-PRED-056 | SUPPORTED | Ruka endorses the Umi route, checks Kazuya's rivalry response, and performs final-day flyer labor; RAG-E-V015-004. | Cooperation remains local and the provisional relation persists. |

## Frozen predictions for V016

| Prediction ID | Observable expectation | Source basis | Disconfirmation |
|---|---|---|---|
| RAG-PRED-057 | Active principal photography will produce at least one concrete completion, pickup, travel, postproduction, scheduling, or resource consequence. | RAG-E-V015-011 through RAG-E-V015-015 | V016 shows no further production consequence. |
| RAG-PRED-058 | Chizuru's demonstrated on-camera work will produce an explicit evaluation, opportunity, visibility, rehearsal choice, or production decision. | RAG-E-V015-013, RAG-E-V015-015 | Her acting has no observable V016 consequence. |
| RAG-PRED-059 | Kazuya's producer labor and unsafe bottleneck response will produce a direct interpersonal, crew, health, or role consequence beyond his private self-appraisal. | RAG-E-V015-012, RAG-E-V015-014 | No one responds and his conduct changes nothing beyond the completed take. |
| RAG-PRED-060 | The widening film-and-career relation will produce an observable question, negotiation, or pressure concerning Kazuya's future role, access, or distance from Chizuru. | RAG-E-V015-005, RAG-E-V015-007, RAG-E-V015-016 | V016 contains no such status or access consequence. |

## Adjudicated predictions from the V015 boundary

| Prediction ID | Adjudication | V016 basis | Limit |
|---|---|---|---|
| RAG-PRED-057 | SUPPORTED | The final location trip completes principal photography; footage then enters editing with a September target while Kazuya begins theater arrangements; RAG-E-V016-003, RAG-E-V016-009, RAG-E-V016-012, RAG-E-V016-013. | The finished edit, screening, and delivery remain unobserved. |
| RAG-PRED-058 | SUPPORTED | Chizuru performs the final scene, and Kazuya evaluates it as her brightest performance before the take closes shooting; RAG-E-V016-012. | His response is local evaluation, not a public or professional opportunity. |
| RAG-PRED-059 | SUPPORTED | Chizuru rejects Kazuya's self-demotion, identifies his work as being for her, calls his life wonderful, and says she never regretted meeting him; RAG-E-V016-001, RAG-E-V016-002. | Validation does not make the earlier unsafe method prudent. |
| RAG-PRED-060 | SUPPORTED | Chizuru rejects the different-world hierarchy; the trip forces two-person travel and room-access decisions; Kazuya names expected post-film estrangement, and Ruka challenges the overnight access; RAG-E-V016-001, RAG-E-V016-003, RAG-E-V016-008, RAG-E-V016-016, RAG-E-V016-017. | Access and distance change without mutual romantic classification. |

## Frozen predictions for V017

| Prediction ID | Observable expectation | Source basis | Disconfirmation |
|---|---|---|---|
| RAG-PRED-061 | Ruka's explicit request for bodily touch will receive an observable answer, boundary, contact, withdrawal, or conflict consequence. | RAG-E-V016-018 | V017 supplies no consequence to the request. |
| RAG-PRED-062 | Editing and theater planning will produce a concrete completion, technical, scheduling, screening, delivery, or Sayuri-access consequence. | RAG-E-V016-012, RAG-E-V016-013 | V017 shows no film or postproduction consequence. |
| RAG-PRED-063 | Sayuri's health and the family promise attached to the film will produce a direct visit, disclosure, urgency, access, or medical-state consequence. | RAG-E-V016-010 through RAG-E-V016-013 | V017 shows no such consequence. |
| RAG-PRED-064 | The post-shoot Kazuya-Chizuru relation will produce an observable access, distance, role, or status discussion or a changed non-rental interaction. | RAG-E-V016-001, RAG-E-V016-002, RAG-E-V016-005, RAG-E-V016-008, RAG-E-V016-016 | V017 shows no such relationship consequence. |

## Adjudicated predictions from the V016 boundary

| Prediction ID | Adjudication | V017 basis | Limit |
|---|---|---|---|
| RAG-PRED-061 | SUPPORTED | Kazuya requires Ruka to specify sunscreen, performs that bounded act, later blocks a hug, and separately permits first-name address; RAG-E-V017-001, RAG-E-V017-002, RAG-E-V017-004. | The trial and status conflict remain unresolved. |
| RAG-PRED-062 | SUPPORTED | Editing continues, a September 30 screening is scheduled, and a 200-seat wheelchair-accessible cinema is arranged and visited; RAG-E-V017-005, RAG-E-V017-008. | The finished edit and screening are not shown. |
| RAG-PRED-063 | SUPPORTED | Sayuri visits the cinema, speaks with Chizuru and Kazuya, collapses, is taken by ambulance, and receives a critical prognosis; RAG-E-V017-008 through RAG-E-V017-015. | Diagnosis and final medical outcome remain unknown. |
| RAG-PRED-064 | SUPPORTED | Chizuru publicly coordinates the screening, waits for and thanks Kazuya, and hears his status-independent support commitment; RAG-E-V017-005, RAG-E-V017-010, RAG-E-V017-013. | No mutual romantic classification follows. |

## Frozen predictions for V018

| Prediction ID | Observable expectation | Source basis | Disconfirmation |
|---|---|---|---|
| RAG-PRED-065 | Kazuya's LINE-and-running action will produce an observable film-delivery, projection, technical-access, transport, coordination, or failure consequence. | RAG-E-V017-018 | V018 supplies no consequence to the initiated action. |
| RAG-PRED-066 | The renewed truth-versus-comfort conflict will produce a disclosure attempt, refusal, interruption, audience-knowledge change, or explicit renewed decision. | RAG-E-V017-016, RAG-E-V017-017 | V018 supplies no consequence to the dispute. |
| RAG-PRED-067 | Sayuri's critical state will produce a medical update, consciousness change, family response, death, or stabilization. | RAG-E-V017-014, RAG-E-V017-015 | V018 supplies no medical or family-state consequence. |
| RAG-PRED-068 | Kazuya's instruction to prioritize Chizuru's feelings will produce an observable support, access, comfort, boundary, or role consequence between them. | RAG-E-V017-016 through RAG-E-V017-018 | V018 supplies no interpersonal consequence. |

## Adjudicated predictions from the V017 boundary

| Prediction ID | Adjudication | V018 basis | Limit |
|---|---|---|---|
| RAG-PRED-065 | SUPPORTED | Kazuya's action produces laptop-and-projector delivery of unfinished footage at Sayuri's bedside; RAG-E-V018-001. | The edit and public screening remain incomplete. |
| RAG-PRED-066 | SUPPORTED | Chizuru says that she and Kazuya are not dating and apologizes; Sayuri responds by entrusting the answer to her; RAG-E-V018-005, RAG-E-V018-006. | Rental details and Sayuri's final factual belief remain ambiguous. |
| RAG-PRED-067 | SUPPORTED | Sayuri regains limited responsiveness, exchanges touch and final love with Chizuru, and dies before the funeral; RAG-E-V018-004, RAG-E-V018-008. | Exact diagnosis and medical mechanism remain unknown. |
| RAG-PRED-068 | SUPPORTED | Kazuya urges self-directed speech, offers help, respects refusal, consults Sumi, and constructs a funded rental-support plan; RAG-E-V018-003, RAG-E-V018-010, RAG-E-V018-012 through RAG-E-V018-020. | Chizuru has not accepted or experienced the planned date. |

## Frozen predictions for V019

| Prediction ID | Observable expectation | Source basis | Disconfirmation |
|---|---|---|---|
| RAG-PRED-069 | Kazuya's rental request will receive an observable acceptance, refusal, modification, scheduling, or platform consequence. | RAG-E-V018-019, RAG-E-V018-020 | V019 supplies no consequence to the submitted booking. |
| RAG-PRED-070 | The funded best-date plan will produce a concrete activity, spending, support, comfort, boundary, or failure consequence. | RAG-E-V018-015, RAG-E-V018-017 through RAG-E-V018-020 | V019 supplies no observable consequence to the planned intervention. |
| RAG-PRED-071 | Chizuru's controlled bereavement presentation will produce an observable continuation, crack, self-report, refusal, crying episode, or accepted support. | RAG-E-V018-008 through RAG-E-V018-011 | V019 supplies no grief-presentation or support-reception consequence. |
| RAG-PRED-072 | Ruka's truce and amusement-park request will produce a scheduling, cooperation, conflict, status, or access consequence. | RAG-E-V018-016 | V019 supplies no consequence to the request or truce. |

## Adjudicated predictions from the V018 boundary

| Prediction ID | Adjudication | V019 basis | Limit |
|---|---|---|---|
| RAG-PRED-069 | SUPPORTED | Chizuru accepts the request and appears for a ten-hour September 24 booking; RAG-E-V019-001. | Acceptance does not determine every activity or emotional outcome. |
| RAG-PRED-070 | SUPPORTED | The itinerary produces clothing, film, restaurant, bouldering, crab dinner, sparklers, and a consequential support exchange; RAG-E-V019-002 through RAG-E-V019-017. | Expense and activity alone do not prove recovery or romance. |
| RAG-PRED-071 | SUPPORTED | Chizuru's composure visibly cracks, she cries against Kazuya, and later reports severe loneliness and relief; RAG-E-V019-009 through RAG-E-V019-020. | The episode does not establish durable bereavement resolution. |
| RAG-PRED-072 | DISCONFIRMED | Ruka is absent and the request and truce receive no scheduling, cooperation, conflict, status, or access consequence; RAG-E-V019-021. | A later consequence remains possible. |

## Adjudicated predictions from the V019 boundary

| Prediction ID | Adjudication | V020 basis | Limit |
|---|---|---|---|
| RAG-PRED-073 | SUPPORTED | The scheduled film screens before an applauding audience, and Chizuru reaffirms acting as a continuing vocation; RAG-E-V020-001, RAG-E-V020-002. | Local reception does not establish wider career success. |
| RAG-PRED-074 | SUPPORTED | Chizuru initiates an unbooked meeting, returns money, admits possible weakness, accepts an ordinary meal, and says the support helped; RAG-E-V020-009, RAG-E-V020-011 through RAG-E-V020-018. | The sequence does not establish durable bereavement recovery or couple status. |
| RAG-PRED-075 | SUPPORTED | Chizuru explicitly cites Mini's disclosure while asking Kazuya whether he likes her; RAG-E-V020-015, RAG-E-V020-016. | The outcome does not validate Mini's theory or authorization. |
| RAG-PRED-076 | SUPPORTED | Kazuya initiates ordinary food access, names Mizuhara as his ideal girlfriend, and begins a confession before interruption; RAG-E-V020-013, RAG-E-V020-019, RAG-E-V020-020. | The final proposition is incomplete and unanswered. |

## V020 terminal prediction disposition

At the V020 close, no predictions were frozen for V021 because the then-authorized sequential run ended at V020. The later V021-V030 authorization opens a new transaction and supplies the prospective freeze below without altering that historical boundary.

## Frozen predictions for V021

| Prediction ID | Observable expectation | Source basis | Disconfirmation |
|---|---|---|---|
| RAG-PRED-077 | Chizuru's replay and public denial of Kazuya's partly delivered declaration will produce a private answer, renewed confession attempt, evasion, boundary, access change, or explicit classification pressure. | RAG-E-V020-019 through RAG-E-V020-021, RAG-E-V020-024, RAG-E-V020-025 | V021 supplies no consequence to the partly heard declaration or Chizuru's avoidance. |
| RAG-PRED-078 | Mami's scheduled app follow-up and request to conceal her past with Kazuya will produce a business step, family contact, information request, disclosure pressure, conflict, or other observable use of the Kibe-Nagomi route. | RAG-E-V020-022, RAG-E-V020-023 | V021 supplies no consequence to the scheduled proposal or newly active family route. |
| RAG-PRED-079 | Kazuya's continued preference for Chizuru and Ruka's unresolved provisional status will produce an observable breakup attempt, status negotiation, jealousy response, access demand, consent boundary, or tactical change. | RAG-E-V020-005 through RAG-E-V020-008 | V021 supplies no consequence to the unresolved trial or the unequal romantic positions. |
| RAG-PRED-080 | Chizuru's stated intention to continue acting and her new capacity for direct unbooked contact will produce an observable acting, professional-network, ordinary-contact, invitation, or boundary consequence. | RAG-E-V020-002, RAG-E-V020-009, RAG-E-V020-013, RAG-E-V020-014 | V021 supplies no acting/career consequence and no consequence to the new ordinary-access route. |

## Adjudicated predictions from the V020 boundary

| Prediction ID | Adjudication | V021 basis | Limit |
|---|---|---|---|
| RAG-PRED-077 | SUPPORTED | The interrupted declaration produces renewed confession planning, Umi-mediated interpretation of Chizuru's qualified phrase, Chizuru's conditional partner account, and repeated but incomplete confession attempts; RAG-E-V021-006 through RAG-E-V021-010, RAG-E-V021-013, RAG-E-V021-022. | Chizuru gives no current romantic self-classification and Kazuya completes no proposition. |
| RAG-PRED-078 | SUPPORTED | Repeated Nagomi contact, the bag-based leakage inference, crowdfunding research, Mami's direct Chizuru intervention, and her final call to Nagomi make the family route operational; RAG-E-V021-001, RAG-E-V021-014, RAG-E-V021-018 through RAG-E-V021-024. | The app's independent viability, call content, and Mami's final endpoint remain unknown. |
| RAG-PRED-079 | SUPPORTED | Kazuya explicitly requests breakup and states nonreciprocity; Ruka refuses, asserts continued pursuit, and increases message pressure; RAG-E-V021-011, RAG-E-V021-012, RAG-E-V021-022. | Her refusal does not create his consent or establish how later conduct will be labeled. |
| RAG-PRED-080 | SUPPORTED | Chizuru invites Kazuya into an acting-network party and affirms his producer role; Umi adds public promotion, a romantic-information probe, and direct contact; RAG-E-V021-002 through RAG-E-V021-007. | One party and post do not establish durable career conversion or couple status. |

## Frozen predictions for V022

| Prediction ID | Observable expectation | Source basis | Disconfirmation |
|---|---|---|---|
| RAG-PRED-081 | Mami's direct call to Nagomi will produce a concrete family, app-project, invitation, disclosure, scheduling, or conflict consequence. | RAG-E-V021-001, RAG-E-V021-018 through RAG-E-V021-024 | V022 supplies no consequence to the direct call or active family route. |
| RAG-PRED-082 | Chizuru's question about how many nights Kazuya can go, following Nagomi's call, will produce a travel, lodging, family-event, scheduling, refusal, or changed-access consequence. | RAG-E-V021-023 | V022 supplies no consequence to the overnight question or linked contact. |
| RAG-PRED-083 | Ruka's rejected breakup and increased messaging will produce another status claim, access demand, monitoring act, tactical change, boundary, or response to the attempted ending. | RAG-E-V021-011, RAG-E-V021-012, RAG-E-V021-022 | V022 supplies no consequence to the breakup attempt or intensified contact. |
| RAG-PRED-084 | Kazuya's renewed confession plan and Chizuru's decision to help under Mami's intervention will produce a confession attempt, truth-correction attempt, explicit classification pressure, coordinated response, or observable deferral. | RAG-E-V021-013 through RAG-E-V021-017, RAG-E-V021-021 through RAG-E-V021-024 | V022 supplies no consequence to either person's stated intention or to Mami's proposed ending. |

## Adjudicated predictions from the V021 boundary

| Prediction ID | Adjudication | V022 basis | Limit |
|---|---|---|---|
| RAG-PRED-081 | SUPPORTED | Mami's Nagomi route culminates in her inclusion in the Kinoshita family trip, where she brings project knowledge and intervention pressure into the shared setting; RAG-E-V022-014 through RAG-E-V022-019. | The exact content and full causal contribution of the V021 call remain withheld; prior lodging and the manager connection also enable the encounter. |
| RAG-PRED-082 | SUPPORTED | The overnight question becomes a two-night, three-day Hawaiians trip with lodging, family care, rental-rule negotiation, the ring problem, and changed access; RAG-E-V022-003, RAG-E-V022-004, RAG-E-V022-008 through RAG-E-V022-013. | The trip does not resolve the relationship or family deception. |
| RAG-PRED-083 | SUPPORTED | Ruka answers the rejected breakup with an overnight attempt, a forced kiss, continued status pressure, monitoring, and the deliberate condom-wrapper fabrication; RAG-E-V022-001 through RAG-E-V022-007. | Escalation supplies no reciprocal status and does not establish Chizuru's lasting belief. |
| RAG-PRED-084 | SUPPORTED | Kazuya sets and attempts a confession deadline; Chizuru and Kazuya coordinate around the trip and ring; Mami's presence and Chizuru's avoidance keep completion deferred; RAG-E-V022-010 through RAG-E-V022-022. | No confession, truth correction, ring return, or alliance with Mami is completed. |

## Frozen predictions for V023

| Prediction ID | Observable expectation | Source basis | Disconfirmation |
|---|---|---|---|
| RAG-PRED-085 | Kazuya's renewed on-trip deadline will produce another confession or truth-correction attempt, a completed proposition, an answer, an interruption, or an explicit deferral. | RAG-E-V022-013, RAG-E-V022-019, RAG-E-V022-021 through RAG-E-V022-024 | V023 supplies no consequence to the renewed deadline or the interrupted room attempt. |
| RAG-PRED-086 | Mami's embedded trip presence and stated intention to end the situation will produce a direct probe, disclosure threat, information move, alliance test, or family-facing intervention. | RAG-E-V022-014 through RAG-E-V022-020 | V023 supplies no observable use of Mami's trip access or intervention stance. |
| RAG-PRED-087 | Ruka's condom-wrapper fabrication and active monitoring will produce a Chizuru reaction, confrontation, changed status judgment, further rivalry pressure, or discovery or correction of the lie. | RAG-E-V022-004 through RAG-E-V022-007, RAG-E-V022-016 | V023 supplies no consequence to the fabricated evidence or its intended wedge. |
| RAG-PRED-088 | The ring-return plan, shared agreement to get through the trip, and mixed family/peer audience will produce coordination about the ring or cover story, an exposure event, a revised arrangement, or another explicit truth-management action. | RAG-E-V022-008 through RAG-E-V022-011, RAG-E-V022-018 through RAG-E-V022-020 | V023 supplies no consequence to the ring obligation, operational alliance, or split-audience problem. |

## Adjudicated predictions from the V022 boundary

| Prediction ID | Adjudication | V023 basis | Limit |
|---|---|---|---|
| RAG-PRED-085 | SUPPORTED | Kazuya tells Mami that he will correct the family lie after confessing and later vows again to end the situation during the trip; RAG-E-V023-009, RAG-E-V023-010, RAG-E-V023-019. | The consequence is renewed sequencing and explicit deferral; no confession, answer, or public correction completes. |
| RAG-PRED-086 | SUPPORTED | Mami probes Ruka, researches Chizuru's profile, warns Chizuru of disclosure capacity, tests Kazuya's correction plan, and asks whether Ruka will tell Nagomi; RAG-E-V023-004, RAG-E-V023-006, RAG-E-V023-008 through RAG-E-V023-016. | These moves do not reveal her final motive or produce full family disclosure. |
| RAG-PRED-087 | SUPPORTED | The wrapper reappears, Ruka repeats the sex claim, Kazuya directly denies it, and Chizuru asks him whether he lied; RAG-E-V023-016 through RAG-E-V023-018. | The volume does not supply a full factual debrief or Chizuru's final belief. |
| RAG-PRED-088 | SUPPORTED | Kazuya admits the cover lie to Mami and explicitly asks her to act unaware while he sequences correction after confession; RAG-E-V023-008 through RAG-E-V023-010. | The ring does not reappear, and the requested concealment does not complete a revised shared arrangement with Chizuru or the family. |

## Frozen predictions for V024

| Prediction ID | Observable expectation | Source basis | Disconfirmation |
|---|---|---|---|
| RAG-PRED-089 | Kazuya's renewed promise to end the situation during the trip and confession-contingent correction plan will produce another confession or truth-correction attempt, a completed proposition, an answer, an interruption, or another explicit deferral. | RAG-E-V023-009, RAG-E-V023-010, RAG-E-V023-019 | V024 supplies no consequence to the renewed trip deadline or stated correction sequence. |
| RAG-PRED-090 | Mami's parallel probes, independent profile research, disclosure warning, and Nagomi test will produce another information move, alliance test, disclosure threat, family-facing intervention, or observable tactical delay. | RAG-E-V023-004, RAG-E-V023-006, RAG-E-V023-008 through RAG-E-V023-016 | V024 supplies no consequence to Mami's active intervention routes. |
| RAG-PRED-091 | Chizuru's direct wrapper question and Kazuya's denial will produce a clarification, trust judgment, confrontation, changed status inference, or further verification of Ruka's claim. | RAG-E-V023-016 through RAG-E-V023-018 | V024 supplies no consequence to the direct source check or contradictory accounts. |
| RAG-PRED-092 | Chizuru's explicit best-day appraisal and chosen-family recognition inside a still-false family account will produce further family participation, care, guilt, boundary, ring, cover-story, or exposure consequence. | RAG-E-V023-020 through RAG-E-V023-022 | V024 supplies no consequence to the strengthened family belonging or its conflict with the uncorrected premise. |

## Adjudicated predictions from the V023 boundary

| Prediction ID | Adjudication | V024 basis | Limit |
|---|---|---|---|
| RAG-PRED-089 | SUPPORTED | Kazuya fixes a same-day deadline, searches for Chizuru, reaches the chapel, and initiates direct speech; RAG-E-V024-010, RAG-E-V024-020 through RAG-E-V024-022. | The proposition, wider truth correction, and answer remain beyond the volume boundary. |
| RAG-PRED-090 | SUPPORTED | Mami judges the souvenir-ring scene, a locked account in her sequence frames withheld action as help, same-day answer pressure remains active, and Nagomi requests a private talk; RAG-E-V024-009, RAG-E-V024-015, RAG-E-V024-019. | No public disclosure or completed Nagomi-Mami conversation occurs. |
| RAG-PRED-091 | SUPPORTED | Ruka repeats the wrapper claim and demands emotional classification; Chizuru then directly asks whether Kazuya still cares for Mami, and he denies wanting her while offering limited interpretive help; RAG-E-V024-012 through RAG-E-V024-015. | The wrapper receives no full factual debrief, and Chizuru's final trust judgment remains unstated. |
| RAG-PRED-092 | SUPPORTED | Nagomi explicitly names Chizuru as family; Harumi offers care and releases her from compulsory ring retention; Ruka demands return and truth; and wedding and mortality history intensify the same obligation; RAG-E-V024-002, RAG-E-V024-007 through RAG-E-V024-009, RAG-E-V024-011 through RAG-E-V024-013, RAG-E-V024-016, RAG-E-V024-017. | Family care continues under the false premise, and neither ring return nor exposure completes. |

## Frozen predictions for V025

| Prediction ID | Observable expectation | Source basis | Disconfirmation |
|---|---|---|---|
| RAG-PRED-093 | Kazuya's direct chapel approach and request that Chizuru listen will produce a completed romantic proposition or truth statement, an answer, an interruption, a flight, or another explicit deferral. | RAG-E-V024-020 through RAG-E-V024-022 | V025 supplies no consequence to the initiated chapel speech. |
| RAG-PRED-094 | Mami's ring-scene judgment, intervention self-framing, same-day pressure, and Nagomi's request to talk will produce a family-facing conversation, disclosure threat or action, tactical delay, alliance test, or material information change. | RAG-E-V024-009, RAG-E-V024-015, RAG-E-V024-019 | V025 supplies no consequence to Nagomi's message or Mami's active intervention stance. |
| RAG-PRED-095 | Kuribayashi's direct statement that he came to see Ruka will produce a relationship-history discussion, support attempt, status response, rejection, or changed access between them. | RAG-E-V024-018 | V025 supplies no consequence to the initiated Kuribayashi-Ruka contact. |
| RAG-PRED-096 | Harumi's permission to return the ring, Nagomi's family and wedding framing, and Ruka's disclosure pressure will produce a return attempt, explanation, continued concealment, family boundary, cover story, or exposure consequence. | RAG-E-V024-002, RAG-E-V024-007 through RAG-E-V024-009, RAG-E-V024-011 through RAG-E-V024-013, RAG-E-V024-016, RAG-E-V024-017 | V025 supplies no consequence to the ring-release and family-obligation conflict. |

## Adjudicated predictions from the V024 boundary

| Prediction ID | Adjudication | V025 basis | Limit |
|---|---|---|---|
| RAG-PRED-093 | SUPPORTED | Kazuya continues the chapel attempt, but Mami's arrival message prompts Chizuru to apologize and run before a proposition or answer; RAG-E-V025-003, RAG-E-V025-004. | The consequence is interruption, flight, and explicit deferral rather than a completed confession. |
| RAG-PRED-094 | SUPPORTED | Mami creates an immediate room-and-ring disclosure plan, Chizuru refuses and obtains a tactical delay, and the volume ends with the rental profile exposed on the fallen phone; RAG-E-V025-005, RAG-E-V025-006, RAG-E-V025-010, RAG-E-V025-014, RAG-E-V025-018, RAG-E-V025-021. | V026 identifies the device as Ruka's and records Mami saying that she dropped it; the exact pre-drop screen preparation remains unshown. |
| RAG-PRED-095 | SUPPORTED | Kuribayashi tells Ruka that he is glad to see her, worried after she left the service, and ashamed of his own status display rather than angry at her; RAG-E-V025-011. | The clarification does not establish romance, reconciliation, or continuing access. |
| RAG-PRED-096 | SUPPORTED | Mami makes the inherited ring part of the planned disclosure, Chizuru refuses the method and supplies a cover story, and the false family account reaches profile exposure without a completed ring return; RAG-E-V025-005, RAG-E-V025-012 through RAG-E-V025-014, RAG-E-V025-018, RAG-E-V025-021. | The ring remains unreturned and is not itself displayed to the group at the cliffhanger. |

## Frozen predictions for V026

| Prediction ID | Observable expectation | Source basis | Disconfirmation |
|---|---|---|---|
| RAG-PRED-097 | The visible Diamond profile on Nagomi's fallen phone will produce an identification, question, denial, explanation, interruption, removal attempt, or other immediate exposure consequence. | RAG-E-V025-021, RAG-E-V025-022 | V026 supplies no consequence to the displayed profile. |
| RAG-PRED-098 | Kazuya and Chizuru's shared exposure crisis will produce coordination, divergent accounts, a protective action, blame allocation, status clarification, or an observable failure to coordinate. | RAG-E-V025-017, RAG-E-V025-018, RAG-E-V025-021, RAG-E-V025-022 | V026 supplies no joint or contrasting response from the two principals. |
| RAG-PRED-099 | Mami's prior disclosure plan, conditional truce, and smile at the profile reveal will produce an intervention, explanation, denial, rescue framing, accountability test, or further information move. | RAG-E-V025-005, RAG-E-V025-006, RAG-E-V025-010, RAG-E-V025-018, RAG-E-V025-021 | V026 supplies no consequence to Mami's position at the exposure. |
| RAG-PRED-100 | Nagomi's explicit chosen-family commitment, the unresolved inherited ring, and the rental-profile display will produce a family judgment, care response, anger, boundary, factual question, ring consequence, or changed relationship belief. | RAG-E-V024-002, RAG-E-V024-008, RAG-E-V025-005, RAG-E-V025-012 through RAG-E-V025-014, RAG-E-V025-021 | V026 supplies no family or ring consequence to the corrected-information threat. |

## Material claim revision at the V026 boundary

| Revision ID | Prior formulation | Revised formulation | Evidence and impact |
|---|---|---|---|
| RAG-REV-006 | V025 close artifacts described the displayed device as Nagomi's phone or said that Nagomi dropped it. | The phone belongs to Ruka, and Mami says that she dropped it; Nagomi is an observer who then asks the direct relationship question. | Reinspection of RAG-E-V025-021 and the explicit continuation at RAG-E-V026-001 correct current factual artifacts. The frozen RAG-PRED-097 wording above remains preserved as the historical prospective record. The exact pre-drop screen preparation remains unknown. |

## Adjudicated predictions from the V025 boundary

| Prediction ID | Adjudication | V026 basis | Limit |
|---|---|---|---|
| RAG-PRED-097 | SUPPORTED | The profile produces immediate identification, a failed joke-image cover, Kazuya's removal attempt, Kazuo's money question, and Nagomi's direct status question; RAG-E-V026-001 through RAG-E-V026-003. | The frozen wording misidentified the device as Nagomi's; V026 corrects it as Ruka's phone dropped by Mami. |
| RAG-PRED-098 | SUPPORTED | Kazuya constructs a protective dating timeline, accepts blame, and confesses love; Chizuru initiates two kisses, discloses her identity, makes a public status claim, and joins the near-complete private explanation; RAG-E-V026-007 through RAG-E-V026-016. | Coordination preserves one explicit lie, and no private mutual romantic classification completes. |
| RAG-PRED-099 | SUPPORTED | Mami acknowledges dropping the phone, performs a whistleblower accusation, and twice turns kissing into a public proof demand; RAG-E-V026-001, RAG-E-V026-004, RAG-E-V026-009, RAG-E-V026-015. | The exact pre-drop screen preparation and a single exhaustive motive remain unshown. |
| RAG-PRED-100 | SUPPORTED | Kazuo raises the money exchange, Kibe uses the ring as evidence, Nagomi requests explanation and later accepts the near-complete account, and family trust changes; RAG-E-V026-002, RAG-E-V026-006, RAG-E-V026-016. | No completed ring return is visible, and family acceptance still rests on the residual dating lie. |

## Frozen predictions for V027

| Prediction ID | Observable expectation | Source basis | Disconfirmation |
|---|---|---|---|
| RAG-PRED-101 | Ruka's intervention against Mami, continued attachment, and hard endpoint stare will produce a confrontation, withdrawal, status demand, emotional disclosure, changed access, or other observable response to the kisses and retained couple cover. | RAG-E-V026-009, RAG-E-V026-010, RAG-E-V026-016 | V027 supplies no consequence to Ruka's V026 position. |
| RAG-PRED-102 | Kazuya and Chizuru's public kisses, real-name disclosure, and retained dating lie will produce a private debrief, avoidance, interpretation, boundary, gratitude, status discussion, or observable failure to communicate. | RAG-E-V026-012 through RAG-E-V026-016 | V027 supplies no consequence between the two principals. |
| RAG-PRED-103 | Mami's staged exposure, failed accusation endpoint, and repeated proof demands will produce withdrawal, renewed pressure, reframing, emotional reaction, access change, or another information move. | RAG-E-V026-001, RAG-E-V026-004, RAG-E-V026-009, RAG-E-V026-015 | V027 supplies no consequence to her failed public intervention. |
| RAG-PRED-104 | Nagomi's conditional acceptance, Kibe's trust rupture, Kazuo's anger, and the near-complete explanation will produce changed treatment, apology, boundary, continued scrutiny, family integration, or another trust consequence. | RAG-E-V026-006, RAG-E-V026-016 | V027 supplies no family or peer consequence to the V026 disclosure. |

## Adjudicated predictions from the V026 boundary

| Prediction ID | Adjudication | V027 basis | Limit |
|---|---|---|---|
| RAG-PRED-101 | SUPPORTED | Ruka confronts Chizuru, attempts an agency complaint, demands professional and access boundaries, and later calls the kisses a necessary evil while preserving her own claim; RAG-E-V027-002, RAG-E-V027-007. | Her attachment, fabricated sexual claim, and workable separation remain unresolved. |
| RAG-PRED-102 | SUPPORTED | The principals privately debrief the kisses and responsibility, then undergo deliberate silence for roughly three months before a paid rental recontact; RAG-E-V027-003 through RAG-E-V027-009, RAG-E-V027-013 through RAG-E-V027-015. | The debrief supplies no mutual classification, and the endpoint cuts before Chizuru's direct statement. |
| RAG-PRED-103 | DISCONFIRMED | V027 supplies no canonical Mami withdrawal, renewed pressure, reframing, emotional reaction, access change, or information move. | Creator-labeled cut pages at `0188.jpg`-`0193.jpg` cannot rescue the prediction because they are non-continuity; RAG-E-V027-016. |
| RAG-PRED-104 | SUPPORTED | Nagomi supports continued ordinary treatment, and Kuribayashi directly challenges whether the couple claim is real by invoking the kisses; RAG-E-V027-001, RAG-E-V027-005. | Both consequences occur under the residual dating lie and do not establish durable trust repair for every family or peer. |

## Frozen predictions for V028

| Prediction ID | Observable expectation | Source basis | Disconfirmation |
|---|---|---|---|
| RAG-PRED-105 | Chizuru's serious “hey” and Kazuya's resolve at the paid-date endpoint will produce substantive speech about the silence, kisses, feelings, apology, or relationship boundary. | RAG-E-V027-013 through RAG-E-V027-015 | V028 supplies no substantive consequence to the conversational threshold. |
| RAG-PRED-106 | Chizuru's resolve to face and examine her unnamed feeling will produce a concrete inquiry, test, disclosure, observation, or explicit limit. | RAG-E-V027-011, RAG-E-V027-012, RAG-E-V027-015 | V028 supplies no behavior that advances or bounds the investigation. |
| RAG-PRED-107 | Chizuru's guilt toward Ruka and Ruka's demand for professional and access limits will produce renewed status or boundary negotiation, confrontation, changed access, or disclosure. | RAG-E-V027-002, RAG-E-V027-007, RAG-E-V027-011 | V028 supplies no consequence to the Ruka boundary conflict. |
| RAG-PRED-108 | Recontact through a paid date will create a payment, professional-role, booking, refund, extension, or client-versus-person distinction with observable consequence. | RAG-E-V027-013 through RAG-E-V027-015 | The rental wrapper produces no consequence beyond background setting. |

## Adjudicated predictions from the V027 boundary

| Prediction ID | Adjudication | V028 basis | Limit |
|---|---|---|---|
| RAG-PRED-105 | SUPPORTED | The paid-date endpoint produces Chizuru's apology for silence, explanation of Ruka concern, and direct discussion of the kisses, feeling, responsibility, and future answer; RAG-E-V028-001 through RAG-E-V028-004. | The conversation defines uncertainty and process rather than a final romantic classification. |
| RAG-PRED-106 | SUPPORTED | Chizuru explicitly commits to investigation, asks Ruka's current status, names a private-access concern, promises an answer, sustains ordinary observation time, and later invites Kazuya into family-house labor; RAG-E-V028-004 through RAG-E-V028-007, RAG-E-V028-013 through RAG-E-V028-015. | The method remains partly improvised, and the volume supplies no final answer. |
| RAG-PRED-107 | SUPPORTED | Chizuru says Ruka concern caused the silence, directly asks Kazuya about Ruka, treats Ruka's feeling as real, and questions private-room access; Ruka later appears at work still claiming girlfriend status and caring for him; RAG-E-V028-001, RAG-E-V028-006, RAG-E-V028-009. | No workable separation, corrected fabricated evidence, or mutually accepted access rule follows. |
| RAG-PRED-108 | SUPPORTED | Chizuru treats the kisses as a professional violation serious enough to consider resignation, questions whether Kazuya loves the provider presentation, and moves from a paid date into ordinary LINE, apartment, vocational, and family-home access; RAG-E-V028-002 through RAG-E-V028-005, RAG-E-V028-007 through RAG-E-V028-015. | The booking is not explicitly extended or refunded, and movement beyond it does not by itself create dating status. |

## Frozen predictions for V029

| Prediction ID | Observable expectation | Source basis | Disconfirmation |
|---|---|---|---|
| RAG-PRED-109 | The unidentified photograph at the family altar will produce a kinship identification, family-history disclosure, emotionally material response, or explicit refusal to explain. | RAG-E-V028-015 | V029 supplies no substantive consequence to Kazuya's photograph question. |
| RAG-PRED-110 | The cleanup and contemplated sale will produce a concrete decision or constraint involving property, storage, keys, continued labor, residence, disposal, or retained objects. | RAG-E-V028-013 through RAG-E-V028-015 | V029 supplies no practical consequence to the house transition. |
| RAG-PRED-111 | Chizuru's inquiry will produce another explicit question, observation, test, disclosure, answer promise, or access limit tied to how she evaluates Kazuya or her own feeling. | RAG-E-V028-004 through RAG-E-V028-007, RAG-E-V028-013 through RAG-E-V028-015 | V029 supplies no observable continuation of the investigation. |
| RAG-PRED-112 | The expansion from paid contact to private rooms, sustained LINE, theater access, and family-house labor will produce a Ruka status or boundary response, explicit accounting for her claim, changed access, confrontation, or disclosure. | RAG-E-V028-006 through RAG-E-V028-010, RAG-E-V028-013 through RAG-E-V028-015 | V029 supplies no consequence to the still-active Ruka conflict. |

## Open evidence questions

- What exact terms governed Ruka's original rental relationship with Kuribayashi beyond the now-shared basic truth?
- Will Chizuru's family-linked acting purpose and selective unpriced access alter her longer-term career or relationship classification?
- What relationship or family outcome does Mami seek through the senior-smartphone business route?
- Can Kazuya convert the near-complete family explanation into full correction of the residual dating lie across audiences?
- Can Kazuya and Ruka establish workable separation terms after his explicit withdrawal and her refusal to recognize the breakup?
- How will Chizuru continue and bound the investigation after direct inquiry, ordinary observation, and family-house access?
- Will the transition from paid recontact to unpriced private access alter future use of the rental wrapper?
- What boundary or escalation follows Ruka's still-disputed claim as Chizuru and Kazuya expand ordinary access?
- Can Chizuru and Kazuya complete the planned return or correction around Nagomi's family ring?
- Will Chizuru's acting career and family-linked vocational purpose develop after the public screening?
- Does Chizuru's accepted support produce durable bereavement recovery or only a bounded release?
- Can Sumi's consequential emotional support coexist with an unheard confession without distorting the practice relationship?
- What final outcome does Mami seek after Chizuru rejects her claimed alliance and the public separation attempt fails?
- Will Kazuya's direct denial and Chizuru's source check produce a complete correction of Ruka's fabricated sex evidence?
- How will Chizuru balance newly explicit chosen-family value against the ring and false couple premise?
- Can the principals sustain the renewed direct communication beyond the first LINE, apartment, theater, and family-house sequence?
- How will Mami respond after her staged disclosure and proof demands fail to separate the principals immediately, given no canonical V027 action?
- Will Nagomi's expectation and Kibe's partial repair remain stable if the residual dating lie is corrected?
- Who is shown in the second altar photograph, and how does that identification revise the known Ichinose family history?
- What practical disposition follows for Sayuri's house, the collected stones, and other retained family objects?
