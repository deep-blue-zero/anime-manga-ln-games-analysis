---
title: "Rent-a-Girlfriend - Progress and regression ledger"
artifact_id: RAG_PROGRESS_AND_REGRESSION_LEDGER
artifact_type: progress_regression_ledger
series: Rent-a-Girlfriend
generation: V1
version: "1.1"
status: canonical
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
created: "2026-09-19"
source_boundary: "Japanese manga witness RAG-JP-EPUB-V001; inspected and closed through V001."
---

# Progress and regression ledger

## Responsibility

Preserve domain-specific changes against named baselines without collapsing them into one romance score.

## Record schema

`change_id | domain | prior_state | classification | observed_delta | agents_who_know | consequence | durability_boundary | reversal_or_reconfiguration | evidence_refs`

Markdown tables and bounded prose may implement this semantic schema. Unknown values remain unknown; rows cite canonical volume evidence IDs rather than duplicating primary observations.

## Update and routing rule

Update after each eligible volume only when inspected evidence materially affects this responsibility. Preserve stable IDs and historical states. A reviewed domain may record no material change without manufacturing a row. Consequential claims route back to the owning volume reading and forward to the project artifacts named by the series architecture.

## Current coverage

```yaml
initialized: true
inspected_through_volume: V001
row_count: 6
state: CURRENT_THROUGH_V001
```

## Records

| Change ID | Domain / prior state | Classification and observed delta | Knowledge / consequence | Durability boundary and reconfiguration | Evidence refs |
|---|---|---|---|---|---|
| RAG-PRG-001 | Information: strangers after first rental | GAIN — Kazuya and Chizuru learn each other's university identity, family linkage, hospital context, and neighboring residence. | Both know; creates practical access and risk. | Durable through V001; no knowledge erasure. | RAG-E-V001-005, RAG-E-V001-006, RAG-E-V001-007 |
| RAG-PRG-002 | Public status: no shared social identity | RECONFIGURATION — a private service becomes a girlfriend claim believed by family and peers. | Several audiences know a false version; correction cost rises. | Durable through V001; new audiences accumulate. | RAG-E-V001-003, RAG-E-V001-006, RAG-E-V001-011 |
| RAG-PRG-003 | Access: one-off bookings | GAIN — one paid Wednesday hour becomes recurring until both grandmothers leave hospital. | Jointly acknowledged by Kazuya and Chizuru. | Active at V001 boundary; conditional and untested for long durability. | RAG-E-V001-009 |
| RAG-PRG-004 | Honesty: Kazuya intends to end the lie | LOSS — he repeatedly defers or interrupts disclosure under immediate social pressure. | He recognizes the lie and its cost; family and peers remain uninformed. | Pattern persists through V001; attempted confession is counterevidence to total unwillingness. | RAG-E-V001-004, RAG-E-V001-006, RAG-E-V001-008, RAG-E-V001-011 |
| RAG-PRG-005 | Boundary understanding: Kazuya initially treats performance as personal fraud | GAIN — he admits fault and learns explicit rules around campus, residence, time, payment, and routing. | Knowledge changes; compliance remains inconsistent. | Durable knowledge through V001, with repeated behavioral pressure. | RAG-E-V001-002, RAG-E-V001-005, RAG-E-V001-007, RAG-E-V001-008, RAG-E-V001-009 |
| RAG-PRG-006 | Romance: no mutually acknowledged attraction | NO_DEMONSTRATED_CHANGE — Kazuya's attraction is explicit, while Chizuru's romantic state and any joint status remain unestablished. | Kazuya alternates idealization and discounting; Chizuru maintains limits. | No private romantic transition through V001 despite material/social closeness. | RAG-E-V001-009, RAG-E-V001-010, RAG-E-V001-013, RAG-E-V001-014 |
