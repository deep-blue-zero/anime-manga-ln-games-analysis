---
title: "Rent-a-Girlfriend - Claims, predictions, and revisions ledger"
artifact_id: RAG_CLAIMS_PREDICTIONS_AND_REVISIONS_LEDGER
artifact_type: claims_predictions_revisions_ledger
series: Rent-a-Girlfriend
generation: V1
version: "1.11"
status: canonical
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
created: "2026-09-19"
source_boundary: "Japanese manga witnesses RAG-JP-EPUB-V001-V010; inspected, closed, and checkpointed through V010; no V011 prediction frozen."
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
inspected_through_volume: V010
current_claim_count: 26
frozen_prediction_count: 0
state: CHECKPOINTED_THROUGH_V010__NO_NEXT_VOLUME_AUTHORITY
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
| RAG-CLM-025 | Technical and family-mediated routes can convert contingent contact into chosen non-booking coordination, but each use remains bounded by context rather than creating general entitlement. | STRONG_INFERENCE | RAG-E-V009-010, RAG-E-V010-011 through RAG-E-V010-014, RAG-E-V010-016, RAG-E-V010-017 | One family visit and one crisis message do not establish unrestricted future access. | ADDED and supported in V010. |
| RAG-CLM-026 | Ruka's status strategy converts perceived competition into unilateral physical and public escalation, widening the gap between sincere claim and mutual agreement. | STRONG_INFERENCE | RAG-E-V008-012 through RAG-E-V008-014, RAG-E-V009-013, RAG-E-V009-014, RAG-E-V010-003, RAG-E-V010-014, RAG-E-V010-015 | Her apology and sincere feeling are real counterweights but do not supply Kazuya's consent or reciprocation. | ADDED and supported in V010. |

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

## Adjudications and revisions

At the V010 horizon, RAG-PRED-033 through RAG-PRED-035 are supported and RAG-PRED-036 is disconfirmed. The disconfirming case is retained because recorded information and prior initiative did not produce the predicted birthday action within the declared test window. V010 strengthens the commercial-boundary, vocational-support, Mami-investigation, family-access, and provisional-status claims. RAG-CLM-024 records the coexistence of scripted intimacy and genuine vocational exchange; RAG-CLM-025 limits non-booking access by context; RAG-CLM-026 records the growing gap between Ruka's sincere claim and mutual agreement. No V011 prediction is frozen because V011 inspection is outside the authorized block.

The V010 checkpoint preserves the current twenty-six claims, rejects physical or visual intimacy as sufficient proof of mutual consent or relationship status, and revises any simple stagnation account toward domain-specific durable change inside repeated public structures. It downgrades the expectation that newly recorded personal knowledge reliably produces prompt follow-up. Exact checkpoint reasoning is frozen in `02 Block Syntheses/RAG_CP_V010.md`; model-level tests are frozen in `07 Audits and Handoffs/RAG_RECONSTRUCTION_AUDIT_V010.md`.

## Open evidence questions

- What exact terms governed Ruka's original rental relationship with Kuribayashi beyond the now-shared basic truth?
- Will Chizuru's family-linked acting purpose and selective unpriced access alter her longer-term career or relationship classification?
- What final relationship state does Mami seek through separation?
- Can Kazuya generalize the completed Kuribayashi disclosure to Kibe, family, or another audience?
- Can Kazuya treat Ruka's sincere feeling responsibly after nearly formalizing from duty while explicitly preferring Chizuru?
- What use will Mami make of the Kinoshita family account after Chizuru's denial?
- Will direct LINE access remain crisis-bounded or become routine communication?
- How will Kazuya address Ruka's unilateral kiss and widening family-status conflict?
- What diagnosis, prognosis, and family response follow Sayuri's hospitalization?
- Can Kazuya convert stated support for Chizuru's new stage opportunity into durable practical help?
