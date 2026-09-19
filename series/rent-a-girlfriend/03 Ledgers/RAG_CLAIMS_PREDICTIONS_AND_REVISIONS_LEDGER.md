---
title: "Rent-a-Girlfriend - Claims, predictions, and revisions ledger"
artifact_id: RAG_CLAIMS_PREDICTIONS_AND_REVISIONS_LEDGER
artifact_type: claims_predictions_revisions_ledger
series: Rent-a-Girlfriend
generation: V1
version: "1.1"
status: canonical
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
created: "2026-09-19"
source_boundary: "Japanese manga witness RAG-JP-EPUB-V001; inspected and closed through V001; predictions frozen before V002."
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
inspected_through_volume: V001
current_claim_count: 5
frozen_prediction_count: 4
state: CURRENT_THROUGH_V001__PREDICTIONS_FROZEN_FOR_V002
```

## Current claims

| Claim ID | Scope and formulation | Class | Evidence | Counterevidence or gap | Current adjudication |
|---|---|---|---|---|---|
| RAG-CLM-001 | V001 narrative engine: attempted endings recur as expansions that preserve new social or material constraints. | STRONG_INFERENCE | RAG-E-V001-004, RAG-E-V001-006, RAG-E-V001-007, RAG-E-V001-008, RAG-E-V001-009, RAG-E-V001-011 | One volume cannot establish the long-series durability of the mechanism. | OPEN; current through V001. |
| RAG-CLM-002 | Transactional form sets duties and boundaries but does not by itself settle the authenticity of every act or feeling. | STRONG_INFERENCE | RAG-E-V001-002, RAG-E-V001-003, RAG-E-V001-005, RAG-E-V001-008, RAG-E-V001-009, RAG-E-V001-013 | Chizuru's private motives receive little direct access. | OPEN; motive allocation remains bounded. |
| RAG-CLM-003 | Kazuya's extreme self-account is diagnostically useful but incomplete; conduct must test both his flattering and unflattering interpretations. | STRONG_INFERENCE | RAG-E-V001-002, RAG-E-V001-008, RAG-E-V001-011, RAG-E-V001-014 | Limited ordinary-life evidence and no later persistence test. | OPEN; routed to Kazuya model. |
| RAG-CLM-004 | Chizuru's minimum warranted V001 through-line is controlled responsibility plus compartmentalization, not proven romance. | WORKING_HYPOTHESIS | RAG-E-V001-005, RAG-E-V001-006, RAG-E-V001-007, RAG-E-V001-008, RAG-E-V001-009, RAG-E-V001-013 | Professional pride, fairness, family empathy, and personal investment are not separable. | OPEN; routed to Chizuru model. |
| RAG-CLM-005 | V001 progress is strongest in shared infrastructure and social consequence; no mutual private romance is established. | STRONG_INFERENCE | RAG-E-V001-006, RAG-E-V001-007, RAG-E-V001-008, RAG-E-V001-009, RAG-E-V001-011, RAG-E-V001-013, RAG-E-V001-014 | Future volumes may recontextualize motive but cannot retroactively create a V001 joint acknowledgment. | PRESERVE at V001 boundary. |

## Competing hypotheses

| Hypothesis ID | Formulation | Supporting evidence | Limitation / discriminator |
|---|---|---|---|
| RAG-HYP-001 | Chizuru's exceptional help and defense are entirely professional. | Pride in satisfaction, payment rules, girlfriend register. | Weakened if she repeatedly chooses costly help outside role incentives; V001 family/fairness motives already prevent “mechanical compliance.” |
| RAG-HYP-002 | Chizuru's exceptional help already proves romantic attachment. | Beauty framing, repeated chosen continuation, direct defense. | Not discriminated from family empathy, fairness, or professional investment in V001. |
| RAG-HYP-003 | Mami's renewed attention is motivated by jealousy or status threat. | Reaction to the girlfriend claim, public diminishment, later approach. | No decisive interior evidence; intoxication, residual attachment, control, or mixed motive remain viable. |

## Frozen predictions for V002

| Prediction ID | Observable expectation | Source basis | Disconfirmation |
|---|---|---|---|
| RAG-PRED-001 | The Wednesday arrangement will recur or materially constrain a choice. | RAG-E-V001-009 | V002 treats it as nonexistent without explanation. |
| RAG-PRED-002 | The friend-group girlfriend claim will increase disclosure cost or require further performance. | RAG-E-V001-011, RAG-E-V001-013 | The informed audience has no causal relevance where correction is available. |
| RAG-PRED-003 | Mami's renewed attention will produce another initiative testing Kazuya's attachment or the public couple claim. | RAG-E-V001-012, RAG-E-V001-015 | Her V001 approach has no subsequent behavioral consequence within V002. |
| RAG-PRED-004 | Kazuya will continue alternating inflated romantic projection with defensive discounting of positive evidence. | RAG-E-V001-002, RAG-E-V001-010, RAG-E-V001-014 | His appraisals become consistently calibrated across comparable pressure. |

## Adjudications and revisions

No entering prediction existed for V001. No historical claim has yet required revision.

## Open evidence questions

- What practical or personal reason makes the rental job necessary for Chizuru?
- What does Mami seek from renewed contact with Kazuya?
- Can Kazuya complete a disclosure after recognizing its necessity?
- Will the Wednesday rule function as a durable boundary, a recurring pressure point, or both?
