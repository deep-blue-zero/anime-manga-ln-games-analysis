---
title: "SPY x FAMILY — Source and Fanbook Register"
artifact_id: SXF_SOURCE_REGISTER
artifact_type: source_fanbook_register
version: "1.0"
status: canonical
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
authority_generation: SXF-INITIAL
authority_scope: "INITIAL bootstrap rules and attributed metadata only; no literary findings"
source_boundary: "Metadata only: Japanese main manga V01–18 plus separate EYES ONLY fanbook; no narrative admitted"
created: 2026-11-07
last_updated: 2026-11-07
---

# Source and fanbook register

## Evidence boundary and inventory

The 2026-11-04 import metadata, reconciled on 2026-11-07, reports Japanese main V01–18 and EYES ONLY, nineteen EPUBs, creator 遠藤達哉 and publisher 集英社. No numeric gap is reported within the supplied main range. Official completeness and story/continuation boundaries are not established.

No pages, spine, chapters, spread pairing, image order/completeness or readable rendering were inspected here; prior import technical checks were not rerun. Japanese is metadata-reported. All rows are METADATA_REPORTED_PRESENT, current-byte NOT_VERIFIED, NOT_ADMITTED, NOT_INSPECTED and analytical NOT_STARTED.

Public local keys resolve through the governed *SPY x FAMILY* evidence collection/custodian. Private source IDs, acquisition details and raw pages remain outside Git.

| Public local key | Reported unit | Lane |
|---|---|---|
| SXF-JP-V01 | Japanese main V01 | Main candidate |
| SXF-JP-V02 | Japanese main V02 | Main candidate |
| SXF-JP-V03 | Japanese main V03 | Main candidate |
| SXF-JP-V04 | Japanese main V04 | Main candidate |
| SXF-JP-V05 | Japanese main V05 | Main candidate |
| SXF-JP-V06 | Japanese main V06 | Main candidate |
| SXF-JP-V07 | Japanese main V07 | Main candidate |
| SXF-JP-V08 | Japanese main V08 | Main candidate |
| SXF-JP-V09 | Japanese main V09 | Main candidate |
| SXF-JP-V10 | Japanese main V10 | Main candidate |
| SXF-JP-V11 | Japanese main V11 | Main candidate |
| SXF-JP-V12 | Japanese main V12 | Main candidate |
| SXF-JP-V13 | Japanese main V13 | Main candidate |
| SXF-JP-V14 | Japanese main V14 | Main candidate |
| SXF-JP-V15 | Japanese main V15 | Main candidate |
| SXF-JP-V16 | Japanese main V16 | Main candidate |
| SXF-JP-V17 | Japanese main V17 | Main candidate |
| SXF-JP-V18 | Japanese main V18 | Main candidate |
| SXF-EYES-ONLY | SPY×FAMILY 公式ファンブック EYES ONLY | Separate companion |

## Operational schemas

| Record / prefix | Required fields |
|---|---|
| Witness version `SXF-WV-nnnn` | Local key/version; exact title/edition/language/creator/publisher or UNKNOWN; immutable digest/bytes; governed receipt; source/derivative relation; spine/image-map version; verifier/date; equivalence/limits |
| Page occurrence `SXF-PG-nnnn` | Witness/version; one-based image occurrence including covers; spine/member; verified chapter; visible printed label; spread/facing basis; component type; readability; authorization/frontier; actual inspection state; full reading/evidence |
| Fanbook component `SXF-FB-nnnn` | Exact pages/section; profile/data/editorial/creator statement/interview/commentary/art/narrative/other/unresolved; source-established speaker/author; publication/disclosure boundary; admission scope; assertion and authority limits; main comparison if authorized |
| Source relation/discrepancy `SXF-SD-nnnn` | Exact paired witnesses/statements; compatible/conflicting scope; evidence; unresolved cause; needed verification; affected claims; preserved resolution history |

Identity states are NOT_VERIFIED / VERIFIED / CHANGED_UNRESOLVED. Admission states are NOT_ADMITTED / AUTHORIZED_NOT_ADMITTED / ADMITTED. Mapped page states are REVIEWED_MATERIAL / NO_MATERIAL_ADDITION / DUPLICATE / EXCLUDED / UNRESOLVED_READABILITY. Closure states are NOT_STARTED / IN_PROGRESS / ACCEPTED_AT_BOUNDARY. No state automatically proves another.

“Official fanbook” is a publication label, not one evidence grade. Data, intention statements, commentary and narrative content have different warrants. A fanbook profile is not automatically a fact known by a main-narrative subject or early reader. Component mapping is not yet available and must not be invented.

## Source gaps

| ID | Limitation | Consequence | Closure evidence |
|---|---|---|---|
| SXF-SG-001 | Current bytes/spine/image mapping unverified | Every locator/admission pending | Exact source receipt and deterministic page map |
| SXF-SG-002 | Readability, page completeness, chapter and spread structure uninspected | No coverage/page-turn/source-complete claims | Actual STILL_IMAGE inspection at selected boundary |
| SXF-SG-003 | EYES ONLY component/source authority and spoiler boundary unknown | Companion facts cannot enter main prospective readings | Exact component classification and separate authorization |
| SXF-SG-004 | Supplied range/order is not official completeness or ending evidence | No automatic terminal-work scope | Verify run order and separately support broader publication claims |
| SXF-SG-005 | Adaptation/other-work equivalence and all-content language unverified | No cross-source fill or creator-based continuity | Explicit separate source verification/admission if needed |

The source custodian proposes identity/component evidence and one integrator updates the register. Append versions; retain earlier routes and disagreement. Changed bytes trigger equivalence/remapping and dependency review. Advance actual coverage only after inspection and accepted transaction. Repaired derivatives preserve provenance.

| History ID | Date | Operation | Result |
|---|---|---|---|
| SXF-SH-001 | 2026-11-07 | Initialized reported inventory, component schemas and five gaps | Nineteen distinct reported witnesses; no main or fanbook content admitted |
