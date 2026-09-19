---
title: "Rent-a-Girlfriend - Claims, predictions, and revisions ledger"
artifact_id: RAG_CLAIMS_PREDICTIONS_AND_REVISIONS_LEDGER
artifact_type: claims_predictions_revisions_ledger
series: Rent-a-Girlfriend
generation: V1
version: "1.4"
status: canonical
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
created: "2026-09-19"
source_boundary: "Japanese manga witnesses RAG-JP-EPUB-V001-V004; inspected and closed through V004; predictions frozen before V005."
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
inspected_through_volume: V004
current_claim_count: 13
frozen_prediction_count: 4
state: CURRENT_THROUGH_V004__PREDICTIONS_FROZEN_FOR_V005
```

## Current claims

| Claim ID | Scope and formulation | Class | Evidence | Counterevidence or gap | Current adjudication |
|---|---|---|---|---|---|
| RAG-CLM-001 | Attempted endings recur as expansions that preserve new social or material constraints. | STRONG_INFERENCE | RAG-E-V001-004, RAG-E-V001-006, RAG-E-V001-007, RAG-E-V001-008, RAG-E-V001-009, RAG-E-V001-011, RAG-E-V002-008, RAG-E-V002-012, RAG-E-V002-014, RAG-E-V002-015, RAG-E-V003-006, RAG-E-V003-009, RAG-E-V003-010, RAG-E-V003-014, RAG-E-V004-003, RAG-E-V004-005, RAG-E-V004-017 | Four volumes support recurrence; long-series durability remains untested. | STRENGTHENED through V004. |
| RAG-CLM-002 | Transactional form sets duties and boundaries but does not by itself settle the authenticity of every act or feeling. | STRONG_INFERENCE | RAG-E-V001-002, RAG-E-V001-003, RAG-E-V001-005, RAG-E-V001-008, RAG-E-V001-009, RAG-E-V001-013, RAG-E-V002-002, RAG-E-V002-006, RAG-E-V002-013, RAG-E-V002-017, RAG-E-V003-003, RAG-E-V003-008, RAG-E-V003-009, RAG-E-V003-016, RAG-E-V004-001, RAG-E-V004-007, RAG-E-V004-014, RAG-E-V004-016, RAG-E-V004-018 | Chizuru's private motives receive little direct access; Ruka's rental history is clearer but exact contractual detail remains limited. | STRENGTHENED; motive allocation remains bounded. |
| RAG-CLM-003 | Kazuya's extreme self-account is diagnostically useful but incomplete; conduct must test both his flattering and unflattering interpretations. | STRONG_INFERENCE | RAG-E-V001-002, RAG-E-V001-008, RAG-E-V001-011, RAG-E-V001-014, RAG-E-V002-005, RAG-E-V002-010, RAG-E-V002-012, RAG-E-V002-017, RAG-E-V003-005, RAG-E-V003-015, RAG-E-V004-004, RAG-E-V004-011, RAG-E-V004-013, RAG-E-V004-015 | Employment is newly observed but not sustained; correction follows rather than prevents surveillance. | PROSPECTIVELY_SUPPORTED through V004 with new counterevidence. |
| RAG-CLM-004 | Chizuru's minimum warranted through-line is controlled responsibility, compartmentalization, and vocational purpose, not proven romance. | WORKING_HYPOTHESIS | RAG-E-V001-005, RAG-E-V001-006, RAG-E-V001-007, RAG-E-V001-008, RAG-E-V001-009, RAG-E-V001-013, RAG-E-V002-002, RAG-E-V002-006, RAG-E-V002-013, RAG-E-V002-015, RAG-E-V003-001, RAG-E-V003-003, RAG-E-V003-008, RAG-E-V003-009, RAG-E-V003-010, RAG-E-V004-012, RAG-E-V004-014, RAG-E-V004-017 | Professional pride, career investment, fairness, family empathy, social obligation, and personal investment are not separable. | REVISED and prospectively supported through V004. |
| RAG-CLM-005 | V001 progress is strongest in shared infrastructure and social consequence; no mutual private romance is established. | STRONG_INFERENCE | RAG-E-V001-006, RAG-E-V001-007, RAG-E-V001-008, RAG-E-V001-009, RAG-E-V001-011, RAG-E-V001-013, RAG-E-V001-014 | Future volumes may recontextualize motive but cannot retroactively create a V001 joint acknowledgment. | PRESERVE at V001 boundary. |
| RAG-CLM-006 | Audience belief is causally active: Kibe's mistaken premise and the grandmothers' couple belief produce conflict, secrecy pressure, travel, and shared space. | STRONG_INFERENCE | RAG-E-V002-008, RAG-E-V002-012, RAG-E-V002-014, RAG-E-V002-015, RAG-E-V003-004, RAG-E-V003-006, RAG-E-V003-007 | Later correction may revise responses but cannot erase the observed chains. | STRENGTHENED through V003. |
| RAG-CLM-007 | Mami's operational goal in V002 is to destabilize or split the public couple, while the motive and desired final relationship remain unresolved. | STRONG_INFERENCE | RAG-E-V002-003, RAG-E-V002-005, RAG-E-V002-007, RAG-E-V002-009, RAG-E-V002-016, RAG-E-V003-002, RAG-E-V003-011 | The no-love statement adds a self-report but does not distinguish love, jealousy, status, control, or withdrawal. | OPEN; separate goal from motive. |
| RAG-CLM-008 | The unpriced rescue becomes a successful reciprocal rescue with public, medical, and scheduling consequences; it supports personal significance without proving mature love. | STRONG_INFERENCE | RAG-E-V002-016, RAG-E-V002-017, RAG-E-V003-001, RAG-E-V003-002, RAG-E-V003-003, RAG-E-V003-005 | Emergency action and CPR do not generalize to ordinary partnership or establish reciprocation. | REVISED and strengthened through V003. |
| RAG-CLM-009 | V003 uses intimacy-like images as boundary tests whose meaning depends on agency, necessity, consent, and material obstruction. | STRONG_INFERENCE | RAG-E-V003-001, RAG-E-V003-008, RAG-E-V003-013, RAG-E-V003-015 | The scenes differ sharply; formal similarity must not erase those differences. | OPEN; current through V003. |
| RAG-CLM-010 | Ruka's dual position as former rental provider and provisional girlfriend makes her both an informed observer of Chizuru and an active participant in a differently constrained relationship. | STRONG_INFERENCE | RAG-E-V003-012, RAG-E-V003-013, RAG-E-V003-014, RAG-E-V003-016, RAG-E-V004-001, RAG-E-V004-003, RAG-E-V004-005, RAG-E-V004-007 | Exact rental terms and Kuribayashi's full knowledge remain underobserved. | REVISED and strengthened through V004. |
| RAG-CLM-011 | Ruka treats measurable bodily excitation as proof of emotional authenticity and Kazuya as its unique cause. | STRONG_INFERENCE | RAG-E-V004-002, RAG-E-V004-006, RAG-E-V004-007, RAG-E-V004-008 | The pulse criterion is Ruka's represented personal rule; the manga does not validate it as a general measure of love or compatibility. | OPEN; current through V004. |
| RAG-CLM-012 | Personal gifts create unpriced reciprocity across the paid relationship without by themselves establishing mutual romance. | STRONG_INFERENCE | RAG-E-V004-014, RAG-E-V004-015, RAG-E-V004-016, RAG-E-V004-018 | Chizuru supplies gratitude and shared-secret reasons; Kazuya attaches stronger affective meaning. | OPEN; current through V004. |
| RAG-CLM-013 | Kazuya's newly acknowledged attachment produces both care and boundary failure; self-recognition is not equivalent to relational competence. | STRONG_INFERENCE | RAG-E-V003-005, RAG-E-V003-015, RAG-E-V004-004, RAG-E-V004-011, RAG-E-V004-013, RAG-E-V004-015 | His correction and employment provide counterevidence to a uniformly regressive account. | PROSPECTIVELY_SUPPORTED through V004. |

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

## Frozen predictions for V005

| Prediction ID | Observable expectation | Source basis | Disconfirmation |
|---|---|---|---|
| RAG-PRED-013 | Ruka will use the private karaoke setting to test or escalate physical or relational boundaries and press the trial arrangement beyond ordinary weekly dating. | RAG-E-V004-003, RAG-E-V004-008, RAG-E-V004-019 | The scene ends without an explicit escalation, test, or demand. |
| RAG-PRED-014 | Chizuru's personalized Christmas gift and Kazuya's return gift will remain a materially distinct reciprocal exchange from ordinary rental payment and reviews. | RAG-E-V004-014, RAG-E-V004-016 | V005 treats both entirely as routine service with no relational or behavioral consequence. |
| RAG-PRED-015 | Chizuru's acting ambition will materially condition scheduling, money, identity, or opportunity. | RAG-E-V004-012 | The revealed goal has no practical consequence when those domains become relevant. |
| RAG-PRED-016 | Kazuya's new karaoke job will materially change his money, routine, or relationship logistics. | RAG-E-V004-010, RAG-E-V004-015 | The employment disappears without practical effect. |

## Adjudications and revisions

All four V004 predictions were supported within their declared window. Claims RAG-CLM-001 through RAG-CLM-004 remain bounded but gain evidence from the provisional relationship, vocational disclosure, and gift exchange. RAG-CLM-010 is revised from an unspecified parallel transaction to Ruka's rental history and current trial relationship. RAG-CLM-011 through RAG-CLM-013 record the new pulse criterion, unpriced reciprocity, and gap between attachment recognition and competence. Predictions RAG-PRED-013 through RAG-PRED-016 are frozen before V005.

## Open evidence questions

- What exact terms governed Ruka's rental relationship with Kuribayashi, and what did he know?
- How will Chizuru's acting goal alter her schedule, money needs, identity management, or opportunities?
- What final relationship state does Mami seek through separation?
- Can Kazuya complete disclosure to Kibe or another audience after the emergency?
- Can Kazuya treat Ruka's sincere feeling responsibly while he remains attached to Chizuru?
- What does Ruka seek in the private karaoke room, and what consent or refusal evidence governs the encounter?
