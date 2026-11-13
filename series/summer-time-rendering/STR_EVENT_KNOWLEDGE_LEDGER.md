---
title: "Summer Time Rendering — event and knowledge records"
series: summer-time-rendering
artifact_id: STR_EVENT_KNOWLEDGE_LEDGER
artifact_type: event_knowledge_ledger
generation: STR-G1
version: "1.0"
status: canonical
authority_scope: "Source-qualified temporal/epistemic schemas and controls; no event findings"
source_boundary: "Japanese main manga volumes 01-13 and 2026 未然事故物件 supplement; metadata only, no narrative admission or inspection"
canonical_home: series/summer-time-rendering/STR_EVENT_KNOWLEDGE_LEDGER.md
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
---

# Event and knowledge records

## Control state

| Control | Current state |
|---|---|
| Admitted / inspected units | 0 / 0 |
| Established events / knowledge records | 0 / 0 |
| Repeated occurrences / branches / mechanisms | NOT_ESTABLISHED |
| Main-only checkpoint | NOT_CREATED |
| Supplement chronology | UNKNOWN; uninspected |

This home separates presentation from event time and individual knowledge. It does not assert any special narrative mechanic. The full reading owns the causal explanation.

## Event schema

`event_id | source_track/witness | unit/scene | physical_locators | presentation_position | event_time_and_basis_or_UNKNOWN | narrative_frame/confidence | occurrence_discriminator_if_evidenced | actors/observers | entering_conditions | action/constraint | consequence | causal_claim_ids | full_reading_anchor | prior_related_event`.

Use STR-E0001 onward. Actual story time may be UNKNOWN. Occurrence discriminator is NOT_REQUIRED unless evidence makes ambiguity material; then use a supported identifier or UNRESOLVED. Similar images cannot alone prove the same or another event. A recollection/report records who presents it and its status.

## Knowledge schema

`knowledge_id | subject | proposition | KNOWS/BELIEVES/SUSPECTS/UNAWARE/UNKNOWN | acquisition_or_nonacquisition_basis | event/occurrence/frame | disclosure_unit | reader_horizon | evidence_layer/confidence | counterevidence | predecessor | claims/reading/locators`.

Use STR-K0001 onward. UNAWARE requires diagnostic support; unshown information is UNKNOWN. A report of another's knowledge is attributed evidence. Do not propagate information across an unestablished frame/occurrence relation.

## Event-relation schema

Only when actual evidence warrants it:
`relation_id | event_ids | proposed_relation(SAME_OCCURRENCE/DIFFERENT_OCCURRENCE/REPORT_OR_MEMORY/FORMAL_ECHO/CAUSAL_DEPENDENCY/UNRESOLVED) | supporting_source | counterevidence | assumptions | confidence | claim_id/full_argument_anchor`.

These are analytical alternatives, not preset story mechanics. Causal dependency requires a warrant beyond temporal adjacency. Unknown relationships stay OPEN.

All analytical record sets are empty.

## Update and preservation

Append material events/knowledge/relations with the accepted unit. Stable IDs and physical source locators remain fixed. Current timelines may route event IDs but never overwrite presentation order or the prior uncertainty. A retrospective chronology is labeled as such and cites the original evidence.

Corrections append `id | prior_record | date | old/new | source_basis | affected_claims`; meaning changes use claim transitions. Main-only and supplement-aware views stay separately retrievable. New supplemental disclosure may revise understanding without changing earlier character knowledge.

Coverage changes append `control_event | date | old/new | actual_scope | evidence_routes | remaining_gap | role`. No-change belongs in the reading manifest, not automatic rows. Before synthesis verify subject attribution, event identity, chronology basis and inference limits; a neat chart cannot replace causal prose.
