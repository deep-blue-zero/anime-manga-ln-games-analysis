---
title: "Rent-a-Girlfriend - Information and deception ledger"
artifact_id: RAG_INFORMATION_AND_DECEPTION_LEDGER
artifact_type: information_deception_ledger
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

# Information and deception ledger

## Responsibility

Preserve what the manga establishes, who knows or believes each proposition, disclosure state, deception mechanism, cost, and alternatives.

## Record schema

`proposition_id | represented_truth | agent | knowledge_or_belief | basis | disclosure_event | audience | mechanism | maintenance_cost | alternatives | evidence_refs`

Markdown tables and bounded prose may implement this semantic schema. Unknown values remain unknown; rows cite canonical volume evidence IDs rather than duplicating primary observations.

## Update and routing rule

Update after each eligible volume only when inspected evidence materially affects this responsibility. Preserve stable IDs and historical states. A reviewed domain may record no material change without manufacturing a row. Consequential claims route back to the owning volume reading and forward to the project artifacts named by the series architecture.

## Current coverage

```yaml
initialized: true
inspected_through_volume: V001
row_count: 5
state: CURRENT_THROUGH_V001
```

## Records

| Proposition ID | Represented truth | Knowledge / belief and basis | Disclosure or mechanism | Audience and maintenance cost | Alternatives / evidence refs |
|---|---|---|---|---|---|
| RAG-INF-001 | Kazuya purchases Chizuru's time through Diamond; they are not privately acknowledged romantic partners. | Kazuya and Chizuru know this from the bookings, payment, and negotiated rules. | Truth is mutually explicit but withheld from family and friends. | Concealment requires repeated performance, money, scheduling, and mutually compatible stories. | RAG-E-V001-001, RAG-E-V001-002, RAG-E-V001-003, RAG-E-V001-006, RAG-E-V001-009 |
| RAG-INF-002 | Kazuya's family and both grandmothers believe Chizuru is his girlfriend. | Their belief rests on Kazuya's spontaneous claim and Chizuru's supporting performance. | Fabrication, then maintained omission and active reinforcement. | Kazuya's parents, Nagomi, and Sayuri; correction now threatens family happiness and Chizuru's work privacy. | RAG-E-V001-003, RAG-E-V001-006, RAG-E-V001-008, RAG-E-V001-009 |
| RAG-INF-003 | The campus student known as Ichinose and the rental provider Mizuhara are the same person. | Kazuya and Chizuru know after recognizing each other; Kazuya's university peers do not recognize her in the subdued presentation. | Concealment by styling, separate names/registers, and an explicit no-contact agreement. | Disclosure could expose Chizuru's job and impair her university life. | RAG-E-V001-005, RAG-E-V001-007 |
| RAG-INF-004 | Kazuya's friends and Mami are shown Chizuru as his current girlfriend. | Their belief is based on Kazuya's claim, Chizuru's presentation, handholding, and her public defense. | Fresh fabrication and uncorrected misunderstanding. | Adds a peer audience, creating new pressure to continue and risking later reputational harm. | RAG-E-V001-011, RAG-E-V001-012, RAG-E-V001-013 |
| RAG-INF-005 | Mami's aim in reapproaching Kazuya is not disclosed. | Kazuya reads her attention hopefully; Chizuru does not receive represented knowledge of the later approach. | Strategic ambiguity or genuine mixed motive; insufficient evidence to classify. | The audience sees renewed initiative without privileged interior access. | Jealousy, residual attachment, intoxicated dependence, control, and status repair remain live; RAG-E-V001-012, RAG-E-V001-015. |
