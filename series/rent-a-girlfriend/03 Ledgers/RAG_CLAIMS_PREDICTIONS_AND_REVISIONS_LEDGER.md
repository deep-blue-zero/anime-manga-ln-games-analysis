---
title: "Rent-a-Girlfriend - Claims, predictions, and revisions ledger"
artifact_id: RAG_CLAIMS_PREDICTIONS_AND_REVISIONS_LEDGER
artifact_type: claims_predictions_revisions_ledger
series: Rent-a-Girlfriend
generation: V1
version: "1.16"
status: canonical
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
created: "2026-09-19"
source_boundary: "Japanese manga witnesses RAG-JP-EPUB-V001-V014; inspected and closed through V014; predictions frozen before V015."
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
inspected_through_volume: V014
current_claim_count: 42
frozen_prediction_count: 4
state: CURRENT_THROUGH_V014__PREDICTIONS_FROZEN_FOR_V015
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

At the V014 horizon, RAG-PRED-049 through RAG-PRED-052 are supported. The campaign gains hundreds of backers before stalling; Mini becomes an active strategist; Kazuya secures source permission and a director route; and public exposure creates analytics, reward, flyer, and platform-recommendation work. V014 adds distributed project agency, attachment converted into production labor, separation of Mini's expertise from her romantic interpretation, calibrated exposure, and rivalry-compatible support as RAG-CLM-038 through RAG-CLM-042.

The V010 checkpoint remains the latest block synthesis and local reconstruction audit. V014 continues the next block without revising that historical checkpoint. Its close raises the live claim count to forty-two and freezes four prospective tests for V015.

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

## Frozen predictions for V015

| Prediction ID | Observable expectation | Source basis | Disconfirmation |
|---|---|---|---|
| RAG-PRED-053 | Mini's direct statement that Kazuya likes Chizuru will produce an observable response, relationship discussion, or changed interaction. | RAG-E-V014-017, RAG-E-V014-019 | V015 supplies no response or consequence. |
| RAG-PRED-054 | The revised campaign strategy will produce a measurable support, reach, reward, or platform-promotion change. | RAG-E-V014-010 through RAG-E-V014-013, RAG-E-V014-018 | V015 shows no campaign consequence from the new tactics. |
| RAG-PRED-055 | The secured source and director route will produce at least one concrete preproduction step such as screenplay work, casting, location planning, test shooting, or scheduling. | RAG-E-V014-007 through RAG-E-V014-009 | Production capacity does not advance in V015. |
| RAG-PRED-056 | Ruka's participation in the film effort will produce at least one further project action or rivalry-shaped conflict. | RAG-E-V014-012, RAG-E-V014-013, RAG-E-V014-015 | Her project role has no V015 consequence. |

## Open evidence questions

- What exact terms governed Ruka's original rental relationship with Kuribayashi beyond the now-shared basic truth?
- Will Chizuru's family-linked acting purpose and selective unpriced access alter her longer-term career or relationship classification?
- What final relationship state does Mami seek through separation?
- Can Kazuya generalize the completed Kuribayashi disclosure to Kibe, family, or another audience?
- Can Kazuya treat Ruka's sincere feeling responsibly after nearly formalizing from duty while explicitly preferring Chizuru?
- What later use, if any, will Mami make of the Kinoshita family account after no V011 consequence?
- Will direct LINE access remain crisis-bounded or become routine communication?
- How will Kazuya address Ruka's repeated unilateral kisses and widening status conflict?
- What diagnosis, prognosis, and disclosure decision follow Sayuri's hospitalization?
- What consequence follows Kazuya's custody of the family ring after no V012 use?
- Can Kazuya and Chizuru convert a researched proposal and joint promise into a feasible campaign and completed film?
- How will Chizuru exercise agency inside the film project, and which third parties will supply missing production competence?
- Can Sumi's consequential emotional support coexist with an unheard confession without distorting the practice relationship?
