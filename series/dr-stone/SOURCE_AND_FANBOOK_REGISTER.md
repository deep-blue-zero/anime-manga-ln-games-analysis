---
title: "Dr. STONE — Source and Fanbook Register"
artifact_id: DS_SOURCE_REGISTER
artifact_type: source_fanbook_register
version: "1.0"
status: canonical
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
authority_generation: DS-INITIAL
authority_scope: "INITIAL bootstrap rules and attributed source metadata only; no literary or technical findings"
source_boundary: "Metadata only: Japanese main manga V01–27 plus separate 科学王国事典 fanbook; no narrative admitted"
created: 2026-11-07
last_updated: 2026-11-07
---

# Source and fanbook register

## Metadata boundary

The 2026-11-04 import metadata, reconciled on 2026-11-07, reports Japanese main V01–27 and the separate 科学王国事典 fanbook, 28 EPUBs. Credits contain 稲垣理一郎 and Boichi; publisher metadata is 集英社. No numeric gaps are reported within supplied 1–27. Specific creative-decision attribution, official completeness and ending/continuation scope are not established.

No narrative pages, diagrams, spine, chapter/page order, spread pairing, legibility or completeness were independently inspected. Prior import technical checks were not rerun. Japanese is metadata-reported. Every row is METADATA_REPORTED_PRESENT, current-byte NOT_VERIFIED, NOT_ADMITTED, NOT_INSPECTED and analytical NOT_STARTED.

Public keys resolve through the governed *Dr. STONE* source collection/custodian. Private identifiers, acquisition paths, primary pages and raw extractions remain outside Git.

| Public local key | Reported unit | Lane |
|---|---|---|
| DS-JP-V01 | Japanese main V01 | Main candidate |
| DS-JP-V02 | Japanese main V02 | Main candidate |
| DS-JP-V03 | Japanese main V03 | Main candidate |
| DS-JP-V04 | Japanese main V04 | Main candidate |
| DS-JP-V05 | Japanese main V05 | Main candidate |
| DS-JP-V06 | Japanese main V06 | Main candidate |
| DS-JP-V07 | Japanese main V07 | Main candidate |
| DS-JP-V08 | Japanese main V08 | Main candidate |
| DS-JP-V09 | Japanese main V09 | Main candidate |
| DS-JP-V10 | Japanese main V10 | Main candidate |
| DS-JP-V11 | Japanese main V11 | Main candidate |
| DS-JP-V12 | Japanese main V12 | Main candidate |
| DS-JP-V13 | Japanese main V13 | Main candidate |
| DS-JP-V14 | Japanese main V14 | Main candidate |
| DS-JP-V15 | Japanese main V15 | Main candidate |
| DS-JP-V16 | Japanese main V16 | Main candidate |
| DS-JP-V17 | Japanese main V17 | Main candidate |
| DS-JP-V18 | Japanese main V18 | Main candidate |
| DS-JP-V19 | Japanese main V19 | Main candidate |
| DS-JP-V20 | Japanese main V20 | Main candidate |
| DS-JP-V21 | Japanese main V21 | Main candidate |
| DS-JP-V22 | Japanese main V22 | Main candidate |
| DS-JP-V23 | Japanese main V23 | Main candidate |
| DS-JP-V24 | Japanese main V24 | Main candidate |
| DS-JP-V25 | Japanese main V25 | Main candidate |
| DS-JP-V26 | Japanese main V26 | Main candidate |
| DS-JP-V27 | Japanese main V27 | Main candidate |
| DS-SCIENCE-FANBOOK | Dr.STONE 公式ファンブック 科学王国事典 | Separate companion |

## Operational schemas

| Record | Required fields |
|---|---|
| Witness/version `DS-WV-nnnn` | Key/version; exact title/edition/language/credits/publisher or UNKNOWN; immutable digest/byte count; governed receipt; original/derivative relation; spine/image-map version; verifier/date; equivalence/limits |
| Page occurrence `DS-PG-nnnn` | Witness/version; one-based image including covers; spine/member; verified chapter; visible printed label; facing/spread basis; component; readability; authorization/frontier; review state; full reading/evidence |
| Fanbook component `DS-FB-nnnn` | Exact pages/section; data/editorial/technical explanation/creator statement/interview/commentary/art/narrative/unresolved type; speaker/author as established; publication/disclosure boundary; admission scope; main comparison and limits |
| Source discrepancy `DS-SD-nnnn` | Conflicting source/metadata statements; exact boundaries/routes; provisional decision; missing verification; affected claims; preserved resolution history |

Identity states: NOT_VERIFIED / VERIFIED / CHANGED_UNRESOLVED. Admission: NOT_ADMITTED / AUTHORIZED_NOT_ADMITTED / ADMITTED. Mapped page states: REVIEWED_MATERIAL / NO_MATERIAL_ADDITION / DUPLICATE / EXCLUDED / UNRESOLVED_READABILITY. Closure: NOT_STARTED / IN_PROGRESS / ACCEPTED_AT_BOUNDARY. These are independent dimensions.

No chapter/page/diagram/component mapping is invented now. The fanbook is not V28; “official” does not confer uniform source authority. Technical-looking text is an assertion to inspect, not scientific validation.

## Source gaps

| ID | Limitation | Effect | Closure evidence |
|---|---|---|---|
| DS-SG-001 | Current immutable bytes/spine/image map unverified | All deterministic routes/admission pending | Exact source receipts and page-order mapping |
| DS-SG-002 | Chapter/spread/component/diagram readability and completeness uninspected | No coverage, diagram or source-complete certification | Actual STILL_IMAGE inspection of selected scope |
| DS-SG-003 | Fanbook components, publication boundary and bonus extent unknown | No fanbook fill in main prospective reasoning | Exact classification and separate authorization |
| DS-SG-004 | Supplied numeric range/order is not official completeness or ending evidence | No assumed terminal work scope | Verify selected order and separately support expanded publication claims |
| DS-SG-005 | Credit allocation, edition/adaptation equivalence and all-content language not verified | No specific creative attribution or cross-source replacement | Source-specific verification if relevant and authorized |

The custodian proposes source corrections; one integrator owns this register. Append versions and retain earlier routes. Changed bytes require equivalence/remapping and downstream review. Advance page/closure states only after actual inspection and accepted transaction. Derivative repairs keep provenance.

| History ID | Date | Operation | Result |
|---|---|---|---|
| DS-SH-001 | 2026-11-07 | Initialized reported inventory and source/component schemas | 28 reported witnesses; five gaps; no literary or technical source inspection |
