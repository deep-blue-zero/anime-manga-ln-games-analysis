---
title: "Rent-a-Girlfriend - Claims, predictions, and revisions ledger"
artifact_id: RAG_CLAIMS_PREDICTIONS_AND_REVISIONS_LEDGER
artifact_type: claims_predictions_revisions_ledger
series: Rent-a-Girlfriend
generation: V1
version: "1.5"
status: canonical
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
created: "2026-09-19"
source_boundary: "Japanese manga witnesses RAG-JP-EPUB-V001-V005; inspected and closed through V005; predictions frozen before V006."
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
inspected_through_volume: V005
current_claim_count: 15
frozen_prediction_count: 4
state: CURRENT_THROUGH_V005__PREDICTIONS_FROZEN_FOR_V006
```

## Current claims

| Claim ID | Scope and formulation | Class | Evidence | Counterevidence or gap | Current adjudication |
|---|---|---|---|---|---|
| RAG-CLM-001 | Attempted endings recur as expansions that preserve new social or material constraints. | STRONG_INFERENCE | RAG-E-V001-004, RAG-E-V001-006, RAG-E-V001-007, RAG-E-V001-008, RAG-E-V001-009, RAG-E-V001-011, RAG-E-V002-008, RAG-E-V002-012, RAG-E-V002-014, RAG-E-V002-015, RAG-E-V003-006, RAG-E-V003-009, RAG-E-V003-010, RAG-E-V003-014, RAG-E-V004-003, RAG-E-V004-005, RAG-E-V004-017, RAG-E-V005-001, RAG-E-V005-006, RAG-E-V005-007 | Five volumes support recurrence; long-series durability remains untested. | STRENGTHENED through V005. |
| RAG-CLM-002 | Transactional form sets duties and boundaries but does not by itself settle the authenticity of every act or feeling. | STRONG_INFERENCE | RAG-E-V001-002, RAG-E-V001-003, RAG-E-V001-005, RAG-E-V001-008, RAG-E-V001-009, RAG-E-V001-013, RAG-E-V002-002, RAG-E-V002-006, RAG-E-V002-013, RAG-E-V002-017, RAG-E-V003-003, RAG-E-V003-008, RAG-E-V003-009, RAG-E-V003-016, RAG-E-V004-001, RAG-E-V004-007, RAG-E-V004-014, RAG-E-V004-016, RAG-E-V004-018, RAG-E-V005-009, RAG-E-V005-010, RAG-E-V005-011, RAG-E-V005-012 | Chizuru's private motives receive little direct access; V005 shows informed cooperation inside compensated labor without allocating a unique motive. | STRENGTHENED; motive allocation remains bounded. |
| RAG-CLM-003 | Kazuya's extreme self-account is diagnostically useful but incomplete; conduct must test both his flattering and unflattering interpretations. | STRONG_INFERENCE | RAG-E-V001-002, RAG-E-V001-008, RAG-E-V001-011, RAG-E-V001-014, RAG-E-V002-005, RAG-E-V002-010, RAG-E-V002-012, RAG-E-V002-017, RAG-E-V003-005, RAG-E-V003-015, RAG-E-V004-004, RAG-E-V004-011, RAG-E-V004-013, RAG-E-V004-015, RAG-E-V005-008, RAG-E-V005-011 | Completed employment-linked repair is counterevidence to a uniformly helpless account; panic and concealment continue elsewhere. | STRENGTHENED through V005 with discriminating counterevidence. |
| RAG-CLM-004 | Chizuru's minimum warranted through-line is controlled responsibility, compartmentalization, and vocational purpose, not proven romance. | WORKING_HYPOTHESIS | RAG-E-V001-005, RAG-E-V001-006, RAG-E-V001-007, RAG-E-V001-008, RAG-E-V001-009, RAG-E-V001-013, RAG-E-V002-002, RAG-E-V002-006, RAG-E-V002-013, RAG-E-V002-015, RAG-E-V003-001, RAG-E-V003-003, RAG-E-V003-008, RAG-E-V003-009, RAG-E-V003-010, RAG-E-V004-012, RAG-E-V004-014, RAG-E-V004-017, RAG-E-V005-010, RAG-E-V005-012, RAG-E-V005-014 | Professional pride, fairness, family empathy, social obligation, and personal investment remain inseparable; acting purpose receives no V005 consequence. | PRESERVED through V005; acting forecast disconfirmed for this horizon. |
| RAG-CLM-005 | V001 progress is strongest in shared infrastructure and social consequence; no mutual private romance is established. | STRONG_INFERENCE | RAG-E-V001-006, RAG-E-V001-007, RAG-E-V001-008, RAG-E-V001-009, RAG-E-V001-011, RAG-E-V001-013, RAG-E-V001-014 | Future volumes may recontextualize motive but cannot retroactively create a V001 joint acknowledgment. | PRESERVE at V001 boundary. |
| RAG-CLM-006 | Audience belief is causally active: Kibe's mistaken premise and the grandmothers' couple belief produce conflict, secrecy pressure, travel, and shared space. | STRONG_INFERENCE | RAG-E-V002-008, RAG-E-V002-012, RAG-E-V002-014, RAG-E-V002-015, RAG-E-V003-004, RAG-E-V003-006, RAG-E-V003-007 | Later correction may revise responses but cannot erase the observed chains. | STRENGTHENED through V003. |
| RAG-CLM-007 | Mami's operational goal in V002 is to destabilize or split the public couple, while the motive and desired final relationship remain unresolved. | STRONG_INFERENCE | RAG-E-V002-003, RAG-E-V002-005, RAG-E-V002-007, RAG-E-V002-009, RAG-E-V002-016, RAG-E-V003-002, RAG-E-V003-011 | The no-love statement adds a self-report but does not distinguish love, jealousy, status, control, or withdrawal. | OPEN; separate goal from motive. |
| RAG-CLM-008 | The unpriced rescue becomes a successful reciprocal rescue with public, medical, and scheduling consequences; it supports personal significance without proving mature love. | STRONG_INFERENCE | RAG-E-V002-016, RAG-E-V002-017, RAG-E-V003-001, RAG-E-V003-002, RAG-E-V003-003, RAG-E-V003-005 | Emergency action and CPR do not generalize to ordinary partnership or establish reciprocation. | REVISED and strengthened through V003. |
| RAG-CLM-009 | V003 uses intimacy-like images as boundary tests whose meaning depends on agency, necessity, consent, and material obstruction. | STRONG_INFERENCE | RAG-E-V003-001, RAG-E-V003-008, RAG-E-V003-013, RAG-E-V003-015 | The scenes differ sharply; formal similarity must not erase those differences. | OPEN; current through V003. |
| RAG-CLM-010 | Ruka's dual position as former rental provider and provisional girlfriend makes her both an informed observer of Chizuru and an active participant in a differently constrained relationship. | STRONG_INFERENCE | RAG-E-V003-012, RAG-E-V003-013, RAG-E-V003-014, RAG-E-V003-016, RAG-E-V004-001, RAG-E-V004-003, RAG-E-V004-005, RAG-E-V004-007, RAG-E-V005-004, RAG-E-V005-007, RAG-E-V005-013 | Kuribayashi's basic knowledge is now corrected; exact original terms and Ruka's broader professional history remain incomplete. | STRENGTHENED through V005. |
| RAG-CLM-011 | Ruka treats measurable bodily excitation as proof of emotional authenticity and Kazuya as its unique cause. | STRONG_INFERENCE | RAG-E-V004-002, RAG-E-V004-006, RAG-E-V004-007, RAG-E-V004-008, RAG-E-V005-001, RAG-E-V005-002 | The pulse criterion is Ruka's represented personal rule; V005 shows tactical inhibition but no revision of the uniqueness inference. | OPEN; current through V005. |
| RAG-CLM-012 | Personal gifts create unpriced reciprocity across the paid relationship without by themselves establishing mutual romance. | STRONG_INFERENCE | RAG-E-V004-014, RAG-E-V004-015, RAG-E-V004-016, RAG-E-V004-018, RAG-E-V005-008, RAG-E-V005-009 | Chizuru supplies gratitude and shared-secret reasons; the gift-motivated job later funds care for a friend rather than a couple transition. | STRENGTHENED through V005. |
| RAG-CLM-013 | Kazuya's newly acknowledged attachment produces both care and boundary failure; self-recognition is not equivalent to relational competence. | STRONG_INFERENCE | RAG-E-V003-005, RAG-E-V003-015, RAG-E-V004-004, RAG-E-V004-011, RAG-E-V004-013, RAG-E-V004-015, RAG-E-V005-001, RAG-E-V005-008, RAG-E-V005-011, RAG-E-V005-013 | Refusal and friendship repair add competence evidence; public humiliation and panic concealment preserve the mixed pattern. | STRENGTHENED through V005. |
| RAG-CLM-014 | Bounded self-disclosure can repair a deceived audience without dissolving the larger deception system. | STRONG_INFERENCE | RAG-E-V005-008, RAG-E-V005-009, RAG-E-V005-011 | Kuribayashi receives the truth and accepts the repair, while family, Kibe, and wider peers remain uninformed. | ADDED and supported in V005. |
| RAG-CLM-015 | Chizuru sometimes converts trust in a known client into off-platform coordination that produces a new paid encounter, expanding collaboration without settling romance. | WORKING_HYPOTHESIS | RAG-E-V005-012, RAG-E-V005-014, RAG-E-V005-016 | One referral sequence; Sumi's date outcome and any later repetition remain unknown. | ADDED in V005; low-confidence and domain-specific. |

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

## Frozen predictions for V006

| Prediction ID | Observable expectation | Source basis | Disconfirmation |
|---|---|---|---|
| RAG-PRED-017 | Sumi's practice date will require Kazuya to lead, adapt, or protect the interaction because her communication difficulty prevents an ordinary self-directed provider performance. | RAG-E-V005-014, RAG-E-V005-016 | Sumi conducts the date without material communication difficulty or need for Kazuya's adaptation. |
| RAG-PRED-018 | Mami's observation of Kazuya with Sumi will reactivate investigation, intervention, or pressure around his publicly presented relationship with Chizuru. | RAG-E-V002-003, RAG-E-V002-007, RAG-E-V005-017 | The observation has no informational or behavioral consequence in V006. |
| RAG-PRED-019 | Ruka's coworker position will create a collision, monitoring opportunity, or access claim beyond ordinary weekly dating. | RAG-E-V005-007, RAG-E-V005-013 | Workplace proximity produces no relationship or secrecy consequence in V006. |
| RAG-PRED-020 | Chizuru's private referral will make Kazuya a consequential participant in Sumi's training or evaluation rather than merely an interchangeable platform client. | RAG-E-V005-014, RAG-E-V005-016 | The encounter is treated as an ordinary commercial booking with no training, feedback, or trust consequence. |

## Adjudications and revisions

Three V005 predictions were supported and one was disconfirmed. The private-room and employment expectations occurred, and the gift-motivated job produced a downstream behavioral consequence. Chizuru's acting goal did not condition any V005 event, so RAG-PRED-015 failed at its declared horizon while the underlying V004 fact remains preserved. RAG-CLM-014 records Kazuya's bounded disclosure to Kuribayashi; RAG-CLM-015 records Chizuru's private coordination of Sumi's paid practice encounter. Predictions RAG-PRED-017 through RAG-PRED-020 are frozen before V006.

## Open evidence questions

- What exact terms governed Ruka's original rental relationship with Kuribayashi beyond the now-shared basic truth?
- When will Chizuru's acting goal next alter her schedule, money needs, identity management, or opportunities after the failed V005 forecast?
- What final relationship state does Mami seek through separation?
- Can Kazuya generalize the completed Kuribayashi disclosure to Kibe, family, or another audience?
- Can Kazuya treat Ruka's sincere feeling responsibly while he remains attached to Chizuru?
- How will Sumi's communication difficulty change the practice date, and what will Mami do with her observation?
