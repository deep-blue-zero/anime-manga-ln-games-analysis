---
title: "Rent-a-Girlfriend - Chronology ledger"
artifact_id: RAG_CHRONOLOGY_LEDGER
artifact_type: chronology_ledger
series: Rent-a-Girlfriend
generation: V1
version: "1.4"
status: canonical
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
created: "2026-09-19"
source_boundary: "Japanese manga witnesses RAG-JP-EPUB-V001-V004; inspected and closed through V004."
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
inspected_through_volume: V004
row_count: 18
state: CURRENT_THROUGH_V004
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
| RAG-CHR-010 | RAG-E-V003-001, RAG-E-V003-002 | Chizuru revives Kazuya on shore; rescue and hospital care follow, and Mami's pool meeting is missed. | Immediate continuation of the V002 cliffhanger; exact elapsed time unknown. | The rescue outcome precedes Kibe's discussion and all later V003 events. |
| RAG-CHR-011 | RAG-E-V003-004, RAG-E-V003-005 | After the hospital return, Kibe interprets the rescue, Kazuya makes another booking, and his attention shifts toward conscious feeling for Chizuru. | The new booking is for the following week; exact calendar date unknown. | Occurs before the weekend breakup plan. |
| RAG-CHR-012 | RAG-E-V003-006, RAG-E-V003-007, RAG-E-V003-009 | The pair plan a weekend breakup disclosure; the grandmothers' hot-spring trip displaces it, and the shared night ends in a narrow rental extension. | Same-weekend sequence explicit; the trip coincides with the anniversary of Sayuri's husband's death. | The disclosure is not completed before the extension. |
| RAG-CHR-013 | RAG-E-V003-010, RAG-E-V003-012 | After the trip, Chizuru states the real-girlfriend exit policy; Kuribayashi then arranges a double date for the following Saturday. | Relative sequence and weekday are explicit; absolute date unknown. | Ruka's first accidental encounter with Kazuya precedes her formal introduction. |
| RAG-CHR-014 | RAG-E-V003-013, RAG-E-V003-014, RAG-E-V003-015, RAG-E-V003-016 | During and after the double date, Ruka identifies the rental secret, tests the couple, confronts Kazuya, is caught during a fall, and discloses that she is also a rental girlfriend. | Same-day sequence explicit. | V003 ends before Ruka explains her arrangement or future action. |
| RAG-CHR-015 | RAG-E-V004-001, RAG-E-V004-003, RAG-E-V004-005 | Ruka explains the Kuribayashi rental, conditions secrecy on dating, and accepts a provisional relationship after Chizuru invokes the real-girlfriend rule. | The status change is explicitly dated 2017-10-31 at 17:29. | The preceding confrontation and request occur before that timestamp; the trial does not imply mutual love. |
| RAG-CHR-016 | RAG-E-V004-008, RAG-E-V004-009 | During the month after the trial begins, Ruka messages frequently and has weekly dates with Kazuya; by winter she visits his university and arranges a Saturday movie before Christmas. | Explicit one-month passage followed by seasonal and relative-date anchors. | Exact dates for intervening weekly meetings are not stated. |
| RAG-CHR-017 | RAG-E-V004-010, RAG-E-V004-011, RAG-E-V004-012, RAG-E-V004-014 | On December 24, Kazuya recognizes financial pressure, follows Chizuru and Umi, learns of her acting goal, apologizes, and receives a personalized Christmas gift. | Christmas Eve is explicit; same-day sequence is continuous. | The precise elapsed hours are not needed to establish order. |
| RAG-CHR-018 | RAG-E-V004-015, RAG-E-V004-016, RAG-E-V004-017, RAG-E-V004-019 | After Christmas, Kazuya begins karaoke work and later books Chizuru to return a gift; Ruka intercepts him after the date and takes him into a karaoke room. | Relative ordering is explicit; exact date unknown. | V004 ends before the private-room encounter resolves. |
