---
title: "Rent-a-Girlfriend - Chronology ledger"
artifact_id: RAG_CHRONOLOGY_LEDGER
artifact_type: chronology_ledger
series: Rent-a-Girlfriend
generation: V1
version: "1.2"
status: canonical
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
created: "2026-09-19"
source_boundary: "Japanese manga witnesses RAG-JP-EPUB-V001-V002; inspected and closed through V002."
---

# Chronology ledger

## Responsibility

Preserve event order, temporal expressions, interval bounds, calendar anchors, conflicts, and revisions.

## Record schema

`chronology_id | evidence_refs | event | temporal_expression | anchor_type | earliest | latest | ordering_constraints | uncertainty | contradiction | revision_refs`

Markdown tables and bounded prose may implement this semantic schema. Unknown values remain unknown; rows cite canonical volume evidence IDs rather than duplicating primary observations.

## Update and routing rule

Update after each eligible volume only when inspected evidence materially affects this responsibility. Preserve stable IDs and historical states. A reviewed domain may record no material change without manufacturing a row. Consequential claims route back to the owning volume reading and forward to the project artifacts named by the series architecture.

## Current coverage

```yaml
initialized: true
inspected_through_volume: V002
row_count: 9
state: CURRENT_THROUGH_V002
```

## Records

| Chronology ID | Evidence refs | Event and temporal expression | Anchor and bounds | Ordering constraints, uncertainty, contradiction |
|---|---|---|---|---|
| RAG-CHR-001 | RAG-E-V001-001 | Kazuya is 20 and a first-year university student; Mami ends their first relationship after one month. | Explicit age, academic status, and elapsed relationship duration; exact date unknown. | Precedes the first Diamond booking. No V001 contradiction. |
| RAG-CHR-002 | RAG-E-V001-002, RAG-E-V001-003 | The first rental is followed by Kazuya's one-star review, a second booking, and Nagomi's hospital call during that second session. | Event-order anchor; elapsed days between rentals unknown. | Second booking must follow the posted review; hospital introduction occurs before campus recognition. |
| RAG-CHR-003 | RAG-E-V001-005, RAG-E-V001-009 | Nagomi's established hospital visits are weekly on Wednesday; Kazuya and Chizuru agree to one paid hour each Wednesday until both grandmothers are discharged. | Explicit weekday and termination condition; start date and discharge dates unknown. | Agreement follows the home visit and governs the later scheduled visit in Satisfaction 4. |
| RAG-CHR-004 | RAG-E-V001-011, RAG-E-V001-012, RAG-E-V001-015, RAG-E-V001-016 | During a scheduled rental, the friend encounter produces an extended drinking gathering; later that night Mami approaches Kazuya. The volume closes on a mundane one-week DVD extension. | Same-evening ordering is explicit for the gathering and approach; the DVD-counter transition's exact story time is not stated. | Do not treat publication date or clothing as a calendar anchor. The “one more week” coda formally echoes the weekly arrangement but is not a precise new date. |
| RAG-CHR-005 | RAG-E-V002-001, RAG-E-V002-002 | Mami's post-gathering test and Chizuru's consolation precede an elapsed-time caption placing the story around one hundred days after university entry. | Explicit approximate elapsed time; exact calendar date unknown. | The 17,000-yen invoice settles the earlier extension after this transition. |
| RAG-CHR-006 | RAG-E-V002-003, RAG-E-V002-004, RAG-E-V002-005 | The Izu overnight trip follows Mami's stated separation goal and brings the campus and girlfriend audiences together. | Trip sequence and same-location ordering are explicit; travel date is unstated. | Mami's probe precedes her appropriation of the Mizuhara identity. |
| RAG-CHR-007 | RAG-E-V002-007, RAG-E-V002-009, RAG-E-V002-012 | During the Izu gathering, Mami's identity intervention precedes the pool kiss; the Pocky game and Kazuya's breakup announcement follow. | Same-trip ordering is explicit. | Do not collapse Mami's first kiss, Pocky refusal, and Kazuya's later confession plan into one choice. |
| RAG-CHR-008 | RAG-E-V002-011, RAG-E-V002-013, RAG-E-V002-014, RAG-E-V002-015 | Nagomi expects discharge the following week; Chizuru calls for a final booking. Kibe's fight and appeal then produce a ferry ride on the trip. | “Next week” anchors the booking relative to the Izu trip; exact date unknown. | The ferry ride occurs before the planned post-disembarkation disclosures. |
| RAG-CHR-009 | RAG-E-V002-016, RAG-E-V002-017 | Mami schedules a pool meeting for after disembarkation; before arrival Chizuru falls overboard and Kazuya dives after her. | Immediate sequence explicit; V002 ends underwater. | Rescue outcome, elapsed time, and whether the meeting occurs are unknown at the boundary. |
