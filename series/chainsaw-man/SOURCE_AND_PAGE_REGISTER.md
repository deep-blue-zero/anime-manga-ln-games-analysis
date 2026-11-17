---
title: "Chainsaw Man — Source and Page Register"
artifact_id: CM_SOURCE_REGISTER
artifact_type: source_page_register
version: "1.0"
status: canonical
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
authority_generation: CM-INITIAL
authority_scope: "INITIAL bootstrap rules and attributed source metadata only; no literary findings"
source_boundary: "Metadata only: Japanese main manga V01–24; no narrative admitted"
created: 2026-11-07
last_updated: 2026-11-07
---

# Source and page register

## Administrative evidence and inventory

The 2026-11-04 import metadata, reconciled in the campaign on 2026-11-07, reports 24 Japanese main EPUBs, V01–24, creator 藤本タツキ and publisher 集英社. No numeric gaps are reported within this supplied range. No official collection-completeness, ending or continuation claim follows.

No source pages, spine, chapters, image order, legibility or completeness were independently inspected. Prior technical import checks were not rerun. All rows have current-byte identity NOT_VERIFIED, admission NOT_ADMITTED, project inspection NOT_INSPECTED and analytical closure NOT_STARTED. Language is metadata-reported.

The governed *Chainsaw Man* evidence collection/custodian resolves public local keys to private receipts. No private source ID or acquisition path belongs here.

| Local key | Reported source unit | Presence |
|---|---|---|
| CM-JP-V01 | Japanese main V01 | METADATA_REPORTED_PRESENT |
| CM-JP-V02 | Japanese main V02 | METADATA_REPORTED_PRESENT |
| CM-JP-V03 | Japanese main V03 | METADATA_REPORTED_PRESENT |
| CM-JP-V04 | Japanese main V04 | METADATA_REPORTED_PRESENT |
| CM-JP-V05 | Japanese main V05 | METADATA_REPORTED_PRESENT |
| CM-JP-V06 | Japanese main V06 | METADATA_REPORTED_PRESENT |
| CM-JP-V07 | Japanese main V07 | METADATA_REPORTED_PRESENT |
| CM-JP-V08 | Japanese main V08 | METADATA_REPORTED_PRESENT |
| CM-JP-V09 | Japanese main V09 | METADATA_REPORTED_PRESENT |
| CM-JP-V10 | Japanese main V10 | METADATA_REPORTED_PRESENT |
| CM-JP-V11 | Japanese main V11 | METADATA_REPORTED_PRESENT |
| CM-JP-V12 | Japanese main V12 | METADATA_REPORTED_PRESENT |
| CM-JP-V13 | Japanese main V13 | METADATA_REPORTED_PRESENT |
| CM-JP-V14 | Japanese main V14 | METADATA_REPORTED_PRESENT |
| CM-JP-V15 | Japanese main V15 | METADATA_REPORTED_PRESENT |
| CM-JP-V16 | Japanese main V16 | METADATA_REPORTED_PRESENT |
| CM-JP-V17 | Japanese main V17 | METADATA_REPORTED_PRESENT |
| CM-JP-V18 | Japanese main V18 | METADATA_REPORTED_PRESENT |
| CM-JP-V19 | Japanese main V19 | METADATA_REPORTED_PRESENT |
| CM-JP-V20 | Japanese main V20 | METADATA_REPORTED_PRESENT |
| CM-JP-V21 | Japanese main V21 | METADATA_REPORTED_PRESENT |
| CM-JP-V22 | Japanese main V22 | METADATA_REPORTED_PRESENT |
| CM-JP-V23 | Japanese main V23 | METADATA_REPORTED_PRESENT |
| CM-JP-V24 | Japanese main V24 | METADATA_REPORTED_PRESENT |

## Operational schemas

| Record | Required fields |
|---|---|
| Witness version `CM-WV-nnnn` | Key/version; edition/language/publisher/creator or UNKNOWN; immutable digest/byte count; governed receipt; original/derivative relation; spine/image-map version; verifier/date; equivalence and limits |
| Page occurrence `CM-PG-nnnn` | Witness/version; one-based reading-order image including covers; spine/member identity; verified chapter; visible printed label if any; spread/facing relation and basis; component type; readability; authorized frontier; review state; full reading/evidence |
| Component boundary `CM-COMP-nnnn` | Narrative/cover/front matter/bonus/author note/preview/other/unresolved type; exact mapped extent; admission/exclusion reason; spoiler boundary; inspection lane; outstanding debt |
| Source discrepancy `CM-SD-nnnn` | Conflicting metadata/page/edition statements; evidence and scope; provisional route; needed verification; affected locators; preserved resolution history |

Identity: NOT_VERIFIED / VERIFIED / CHANGED_UNRESOLVED. Admission: NOT_ADMITTED / AUTHORIZED_NOT_ADMITTED / ADMITTED. Page review: REVIEWED_MATERIAL / NO_MATERIAL_ADDITION / DUPLICATE / EXCLUDED / UNRESOLVED_READABILITY. Closure: NOT_STARTED / IN_PROGRESS / ACCEPTED_AT_BOUNDARY. These dimensions do not advance each other automatically.

Deterministic locators bind exact bytes, mapping version and image/member/panel/balloon coordinates. No pages or chapters are invented now. A verified container does not prove readable or complete narrative pages.

## Source gaps

| ID | Limitation | Effect | Closure evidence |
|---|---|---|---|
| CM-SG-001 | Current immutable bytes and spine/image map unbound | All evidence routes/admission pending | Exact receipts and deterministic image ordering |
| CM-SG-002 | Chapters, spread pairing, components, readability/completeness uninspected | No page-turn, coverage or source-complete claims | Actual mapped STILL_IMAGE inspection of selected scope |
| CM-SG-003 | Publication/order/edition relation and supplied-range completeness unverified | No assumed arc/ending or exhaustive collection | Verify selected order and separately support any broader scope |
| CM-SG-004 | No adaptation/other-edition equivalence or actual all-component language check | Excluded source lanes cannot fill gaps | Explicit separate admission and comparison if needed |

Reconnaissance notes a publisher grouping of V01–11; it is bibliographic context only, not verified Japanese chapter/arc segmentation and not a reading boundary. Do not elevate it into narrative evidence.

The source custodian proposes corrections and one integrator updates this register. Append witness versions and preserve former routes; changed bytes trigger locator/equivalence and dependency review. Advance page/closure state only after actual inspection and accepted full-reading transaction. A repair derivative retains its provenance.

| History ID | Date | Operation | Result |
|---|---|---|---|
| CM-SH-001 | 2026-11-07 | Initialized supplied inventory, page schemas and gaps | 24 reported witnesses, no source admission or page inspection |
