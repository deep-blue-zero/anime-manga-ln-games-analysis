---
title: "Rent-a-Girlfriend - Progress and regression ledger"
artifact_id: RAG_PROGRESS_AND_REGRESSION_LEDGER
artifact_type: progress_regression_ledger
series: Rent-a-Girlfriend
generation: V1
version: "1.0"
status: canonical
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
created: "2026-09-19"
source_boundary: "Initialized before V001; no substantive manga observations admitted at bootstrap."
---

# Progress and regression ledger

## Responsibility

Preserve domain-specific changes against named baselines without collapsing them into one romance score.

## Record schema

`change_id | domain | prior_state | classification | observed_delta | agents_who_know | consequence | durability_boundary | reversal_or_reconfiguration | evidence_refs`

Markdown tables and bounded prose may implement this semantic schema. Unknown values remain unknown; rows cite canonical volume evidence IDs rather than duplicating primary observations.

## Update and routing rule

Update after each eligible volume only when inspected evidence materially affects this responsibility. Preserve stable IDs and historical states. A reviewed domain may record no material change without manufacturing a row. Consequential claims route back to the owning volume reading and forward to the project artifacts named by the series architecture.

## Initial coverage

```yaml
initialized: true
inspected_through_volume: null
row_count: 0
state: READY_FOR_V001
```

The V001 bootstrap probe established page-inspection capability only. It created no analytical record.
