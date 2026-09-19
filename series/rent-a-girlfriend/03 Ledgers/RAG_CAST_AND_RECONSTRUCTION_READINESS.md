---
title: "Rent-a-Girlfriend - Cast and reconstruction readiness"
artifact_id: RAG_CAST_AND_RECONSTRUCTION_READINESS
artifact_type: cast_reconstruction_readiness
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

# Cast and reconstruction readiness

## Responsibility

Route verified character identities, aliases, evidence/model homes, observed domains, gaps, and project-local readiness without creating global registry records.

## Record schema

`local_character_key | preferred_name | verified_aliases | first_evidence | evidence_ledger | model | monograph | observed_domains | missing_domains | local_readiness | last_review`

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

## Project-local cast router

No listed person has been enrolled or graded in the global character registry by this project.

| Local character key | Preferred name / verified aliases | First evidence | Evidence ledger / model / monograph | Observed and missing domains | Local readiness | Last review |
|---|---|---|---|---|---|---|
| RAG-LOCAL-KAZUYA | Kazuya Kinoshita; 木ノ下和也 | RAG-E-V001-001 | `04 Character Analysis/Kazuya Kinoshita/RAG_KAZUYA_EVIDENCE_LEDGER.md`; `RAG_KAZUYA_RECONSTRUCTION_MODEL.md`; no monograph | Observed: breakup response, family/friend pressure, transactional conflict, sexual fantasy, apology, partial public correction, emergency risk. Missing: sustained work, broad ordinary routine, rescue outcome, durable later change. | PARTIAL_MODEL | V002 |
| RAG-LOCAL-CHIZURU | Chizuru Ichinose; rental alias Chizuru Mizuhara / 水原千鶴; campus surname Ichinose / 一ノ瀬 | RAG-E-V001-002 | `04 Character Analysis/Chizuru Ichinose/RAG_CHIZURU_EVIDENCE_LEDGER.md`; `RAG_CHIZURU_RECONSTRUCTION_MODEL.md`; no monograph | Observed: professional, campus, family, neighbor, peer collision, conflict, payment, boundary, and illness conduct. Missing: sustained private routine, explicit career goals, broad interior access, rescue knowledge. | PARTIAL_MODEL | V002 |
| RAG-LOCAL-MAMI | Mami Nanami; 七海麻美 | RAG-E-V001-001 | none | Observed: breakup, public social performance, explicit separation goal, identity appropriation, deliberate kiss, private-meeting initiative. Missing: private motive, ordinary routine, desired endpoint, durable pattern outside Kazuya. | EVIDENCE_LEDGER_ELIGIBLE | V002 |
| RAG-LOCAL-NAGOMI | Nagomi Kinoshita; 和 | RAG-E-V001-003 | none | Observed: family expectations, hospital visits, emotional investment, discharge timing. Missing: broader history and independent contexts. | UNMODELED | V002 |
| RAG-LOCAL-SAYURI | Sayuri Ichinose; 一ノ瀬小百合 | RAG-E-V001-006 | none | Observed: hospital relation and acceptance of couple claim. Missing: independent goals, ordinary conduct, relationship history. | UNMODELED | V001 |
| RAG-LOCAL-KAZUO | Kazuo Kinoshita; 和男 | RAG-E-V001-003 | none | Observed only in family/hospital context. | UNMODELED | V001 |
| RAG-LOCAL-HARUMI | Harumi Kinoshita; 晴美 | RAG-E-V001-003 | none | Observed only in family/hospital context. | UNMODELED | V001 |
| RAG-LOCAL-KIBE | Kibe; 木部; given name not established through V002 | RAG-E-V001-011 | none | Observed as Kazuya's childhood friend in peer conflict, moral intervention, childhood report, and ferry-ticket initiative. Missing: ordinary independent conduct and calibration outside the false couple belief. | EVIDENCE_LEDGER_ELIGIBLE | V002 |
| RAG-LOCAL-KURIBAYASHI | Kuribayashi; 栗林; given name not established through V002 | RAG-E-V001-011 | none | Observed as a university friend in peer, drinking, and Izu contexts. Missing: independent motive and broader conduct. | UNMODELED | V002 |

The cast router records identity and artifact availability only. Character-state history for Kazuya and Chizuru remains in their evidence ledgers; operational rules remain in their models.
