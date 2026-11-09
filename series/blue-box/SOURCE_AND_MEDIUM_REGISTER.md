---
title: "Blue Box — Source and Medium Register"
artifact_id: BB_SOURCE_REGISTER
artifact_type: source_medium_register
version: "1.0"
status: canonical
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
authority_generation: BB-INITIAL
authority_scope: "INITIAL bootstrap rules and attributed metadata only; no literary findings"
source_boundary: "Metadata only: Japanese main manga V01–27 and separate prose Interlude/Prologue; no narrative admitted"
created: 2026-11-07
last_updated: 2026-11-07
---

# Source and medium register

## Metadata and inventory

The 2026-11-04 import metadata and 2026-11-07 reconciliation report 29 Japanese EPUBs: main manga V01–27 and prose Interlude/Prologue. Credits include 三浦糀 and 七緒; publisher fields include 集英社 and 株式会社 集英社. No numeric gaps are reported in supplied main1–27. Exact source/component creative roles and official completeness are unverified.

No primary page or prose passage, spine/chapter map, page order/legibility/completeness or illustration was inspected. Prior import checks were not rerun. Every row is METADATA_REPORTED_PRESENT, current-byte NOT_VERIFIED, NOT_ADMITTED, NOT_INSPECTED and analytical NOT_STARTED. Japanese is metadata-reported.

Public keys resolve through the governed *Blue Box* collection/custodian. Private IDs, acquisition paths, primary media and bulk text remain outside Git.

| Public key | Reported unit | Independent source/inspection lane |
|---|---|---|
| BB-MANGA-V01 | Japanese main V01 | MANGA / STILL_IMAGE |
| BB-MANGA-V02 | Japanese main V02 | MANGA / STILL_IMAGE |
| BB-MANGA-V03 | Japanese main V03 | MANGA / STILL_IMAGE |
| BB-MANGA-V04 | Japanese main V04 | MANGA / STILL_IMAGE |
| BB-MANGA-V05 | Japanese main V05 | MANGA / STILL_IMAGE |
| BB-MANGA-V06 | Japanese main V06 | MANGA / STILL_IMAGE |
| BB-MANGA-V07 | Japanese main V07 | MANGA / STILL_IMAGE |
| BB-MANGA-V08 | Japanese main V08 | MANGA / STILL_IMAGE |
| BB-MANGA-V09 | Japanese main V09 | MANGA / STILL_IMAGE |
| BB-MANGA-V10 | Japanese main V10 | MANGA / STILL_IMAGE |
| BB-MANGA-V11 | Japanese main V11 | MANGA / STILL_IMAGE |
| BB-MANGA-V12 | Japanese main V12 | MANGA / STILL_IMAGE |
| BB-MANGA-V13 | Japanese main V13 | MANGA / STILL_IMAGE |
| BB-MANGA-V14 | Japanese main V14 | MANGA / STILL_IMAGE |
| BB-MANGA-V15 | Japanese main V15 | MANGA / STILL_IMAGE |
| BB-MANGA-V16 | Japanese main V16 | MANGA / STILL_IMAGE |
| BB-MANGA-V17 | Japanese main V17 | MANGA / STILL_IMAGE |
| BB-MANGA-V18 | Japanese main V18 | MANGA / STILL_IMAGE |
| BB-MANGA-V19 | Japanese main V19 | MANGA / STILL_IMAGE |
| BB-MANGA-V20 | Japanese main V20 | MANGA / STILL_IMAGE |
| BB-MANGA-V21 | Japanese main V21 | MANGA / STILL_IMAGE |
| BB-MANGA-V22 | Japanese main V22 | MANGA / STILL_IMAGE |
| BB-MANGA-V23 | Japanese main V23 | MANGA / STILL_IMAGE |
| BB-MANGA-V24 | Japanese main V24 | MANGA / STILL_IMAGE |
| BB-MANGA-V25 | Japanese main V25 | MANGA / STILL_IMAGE |
| BB-MANGA-V26 | Japanese main V26 | MANGA / STILL_IMAGE |
| BB-MANGA-V27 | Japanese main V27 | MANGA / STILL_IMAGE |
| BB-PROSE-INTERLUDE | アオのハコ Interlude | PROSE / TEXT, illustrations separately |
| BB-PROSE-PROLOGUE | アオのハコ Prologue | PROSE / TEXT, illustrations separately |

## Operational schemas

| Record | Required fields |
|---|---|
| Witness/version `BB-WV-nnnn` | Key/version; medium; title/edition/language/credits or UNKNOWN; immutable digest/bytes; governed receipt; source/derivative relation; map version; verifier/date; equivalence/limits |
| Manga occurrence `BB-MP-nnnn` | Exact witness; one-based image including covers; spine/member; verified chapter; visible printed label; spread/facing basis; component/readability; authorized frontier; page review state; full reading/evidence |
| Prose component `BB-PC-nnnn` | Exact witness; spine/member/heading; narrative/image/front matter/afterword/bonus/preview/unresolved type; paragraph/block/extraction mapping; authorized/inspected extent; exclusion/debt; TEXT/STILL_IMAGE route; full reading |
| Source relation `BB-SR-nnnn` | Exact paired witnesses/components; proposed chronology/edition/continuity relation; verified alignment or unmatched material; evidence/alternatives; authorization; limits and history |

Identity NOT_VERIFIED/VERIFIED/CHANGED_UNRESOLVED, admission NOT_ADMITTED/AUTHORIZED_NOT_ADMITTED/ADMITTED and closure NOT_STARTED/IN_PROGRESS/ACCEPTED_AT_BOUNDARY are independent. Manga page states are REVIEWED_MATERIAL/NO_MATERIAL_ADDITION/DUPLICATE/EXCLUDED/UNRESOLVED_READABILITY. Prose coverage is NOT_INSPECTED/PARTIAL/COMPLETE_FOR_DECLARED_COMPONENTS. An illustration needs its own actual visual inspection.

Supplement titles do not establish chronological placement or equivalence. No chapters, pages, paragraphs or alignments are invented now.

## Gaps and maintenance

| ID | Limitation | Effect / closure evidence |
|---|---|---|
| BB-SG-001 | Current bytes and maps unbound | OPEN; exact receipts and distinct image/prose mapping before admission |
| BB-SG-002 | Page/prose/chapter/readability/completeness uninspected | OPEN; actual appropriate-lane inspection of selected scope |
| BB-SG-003 | Supplement chronology/continuity/correspondence unknown | OPEN; separately authorized independent readings and exact comparison |
| BB-SG-004 | Creative-role attribution and illustration/paratext contents unverified | OPEN; source-specific component/credit evidence, no inferred authorship |
| BB-SG-005 | Supplied range/order/language metadata not full official collection or all-content certification | OPEN; verify selected scope; separately support broader claims |

One integrator maintains this surface from custodian evidence. Append versions, retain earlier routes, and review dependencies after changed bytes. Advance coverage only after actual inspection/accepted transaction. Derivative repairs preserve provenance; neither lane automatically advances the other.

| History ID | Date | Operation | Result |
|---|---|---|---|
| BB-SH-001 | 2026-11-07 | Initialized 29 reported witnesses and separate medium schemas | Five explicit gaps; no narrative or comparison admission |
