---
title: "Rent-a-Girlfriend - Claims, predictions, and revisions ledger"
artifact_id: RAG_CLAIMS_PREDICTIONS_AND_REVISIONS_LEDGER
artifact_type: claims_predictions_revisions_ledger
series: Rent-a-Girlfriend
generation: V1
version: "1.2"
status: canonical
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
created: "2026-09-19"
source_boundary: "Japanese manga witnesses RAG-JP-EPUB-V001-V002; inspected and closed through V002; predictions frozen before V003."
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
inspected_through_volume: V002
current_claim_count: 8
frozen_prediction_count: 4
state: CURRENT_THROUGH_V002__PREDICTIONS_FROZEN_FOR_V003
```

## Current claims

| Claim ID | Scope and formulation | Class | Evidence | Counterevidence or gap | Current adjudication |
|---|---|---|---|---|---|
| RAG-CLM-001 | Attempted endings recur as expansions that preserve new social or material constraints. | STRONG_INFERENCE | RAG-E-V001-004, RAG-E-V001-006, RAG-E-V001-007, RAG-E-V001-008, RAG-E-V001-009, RAG-E-V001-011, RAG-E-V002-008, RAG-E-V002-012, RAG-E-V002-014, RAG-E-V002-015 | Two volumes support recurrence; long-series durability remains untested. | STRENGTHENED through V002. |
| RAG-CLM-002 | Transactional form sets duties and boundaries but does not by itself settle the authenticity of every act or feeling. | STRONG_INFERENCE | RAG-E-V001-002, RAG-E-V001-003, RAG-E-V001-005, RAG-E-V001-008, RAG-E-V001-009, RAG-E-V001-013, RAG-E-V002-002, RAG-E-V002-006, RAG-E-V002-013, RAG-E-V002-017 | Chizuru's private motives receive little direct access. | STRENGTHENED; motive allocation remains bounded. |
| RAG-CLM-003 | Kazuya's extreme self-account is diagnostically useful but incomplete; conduct must test both his flattering and unflattering interpretations. | STRONG_INFERENCE | RAG-E-V001-002, RAG-E-V001-008, RAG-E-V001-011, RAG-E-V001-014, RAG-E-V002-005, RAG-E-V002-010, RAG-E-V002-012, RAG-E-V002-017 | Ordinary-life evidence remains limited; emergency action is not a full trait test. | PROSPECTIVELY_SUPPORTED through V002. |
| RAG-CLM-004 | Chizuru's minimum warranted through-line is controlled responsibility plus compartmentalization, not proven romance. | WORKING_HYPOTHESIS | RAG-E-V001-005, RAG-E-V001-006, RAG-E-V001-007, RAG-E-V001-008, RAG-E-V001-009, RAG-E-V001-013, RAG-E-V002-002, RAG-E-V002-006, RAG-E-V002-013, RAG-E-V002-015 | Professional pride, fairness, family empathy, social obligation, and personal investment are not separable. | PROSPECTIVELY_SUPPORTED through V002. |
| RAG-CLM-005 | V001 progress is strongest in shared infrastructure and social consequence; no mutual private romance is established. | STRONG_INFERENCE | RAG-E-V001-006, RAG-E-V001-007, RAG-E-V001-008, RAG-E-V001-009, RAG-E-V001-011, RAG-E-V001-013, RAG-E-V001-014 | Future volumes may recontextualize motive but cannot retroactively create a V001 joint acknowledgment. | PRESERVE at V001 boundary. |
| RAG-CLM-006 | V002 converts passive audience belief into causal intervention: Kibe's mistaken premise produces conflict, moral pressure, tickets, and a final shared ride. | STRONG_INFERENCE | RAG-E-V002-008, RAG-E-V002-012, RAG-E-V002-014, RAG-E-V002-015 | Later correction may revise Kibe's response but not erase the V002 causal chain. | OPEN; current through V002. |
| RAG-CLM-007 | Mami's operational goal in V002 is to destabilize or split the public couple, while the motive and desired final relationship remain unresolved. | STRONG_INFERENCE | RAG-E-V002-003, RAG-E-V002-005, RAG-E-V002-007, RAG-E-V002-009, RAG-E-V002-016 | Her “lost control” statement supports affect but does not distinguish love, jealousy, status, or control. | OPEN; separate goal from motive. |
| RAG-CLM-008 | Kazuya's rescue dive is unpriced, self-initiated evidence of Chizuru's personal significance, but does not establish successful rescue, mature love, or reciprocity. | STRONG_INFERENCE | RAG-E-V002-016, RAG-E-V002-017 | Emergency action may not generalize to ordinary relationship competence; Chizuru is not shown knowing it. | PRESERVE at V002 boundary. |

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

## Frozen predictions for V003

| Prediction ID | Observable expectation | Source basis | Disconfirmation |
|---|---|---|---|
| RAG-PRED-005 | The overboard rescue attempt will create a private or public consequence that disrupts the planned clean breakup. | RAG-E-V002-016, RAG-E-V002-017 | V003 erases the cliffhanger with no relational, informational, physical, or scheduling effect. |
| RAG-PRED-006 | Mami's scheduled pool meeting and Kazuya's confession plan will be delayed, canceled, or materially reconfigured by the rescue. | RAG-E-V002-015, RAG-E-V002-016, RAG-E-V002-017 | Meeting and confession proceed unchanged and without reference to the emergency. |
| RAG-PRED-007 | Kibe's intervention or the friend-group belief will continue to constrain disclosure, the breakup account, or the public label. | RAG-E-V002-012, RAG-E-V002-014, RAG-E-V002-015 | The deceived audience has no causal relevance when the event becomes discussable. |
| RAG-PRED-008 | After direct care or rescue consequences become available, Chizuru will reassert a role, boundary, or transactional explanation. | RAG-E-V002-002, RAG-E-V002-006, RAG-E-V002-013 | She accepts an unbounded personal meaning without qualification at the first viable interpretive exchange. |

## Adjudications and revisions

All four V002 predictions were supported within their declared window. Claims RAG-CLM-001 through RAG-CLM-004 are strengthened or prospectively supported, not universalized. RAG-HYP-003 is revised to separate Mami's now-observed separation goal from her still-unresolved motive.

## Open evidence questions

- What is the survival and immediate relational outcome of the rescue attempt?
- What practical or personal reason makes the rental job necessary for Chizuru?
- What final relationship state does Mami seek through separation?
- Can Kazuya complete disclosure to Kibe or another audience after the emergency?
- Does Nagomi's discharge actually terminate the weekly booking rule?
