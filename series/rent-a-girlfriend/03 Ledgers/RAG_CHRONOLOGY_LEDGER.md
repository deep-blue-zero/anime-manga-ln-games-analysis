---
title: "Rent-a-Girlfriend - Chronology ledger"
artifact_id: RAG_CHRONOLOGY_LEDGER
artifact_type: chronology_ledger
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

# Chronology ledger

## Responsibility

Preserve event order, temporal expressions, interval bounds, calendar anchors, conflicts, and revisions.

## Record schema

`chronology_id | evidence_refs | event | temporal_expression | anchor_type | earliest | latest | ordering_constraints | uncertainty | contradiction | revision_refs`

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
