---
title: "Haikyu!! — Source and Paratext Register"
artifact_id: HQ_SOURCE_REGISTER
artifact_type: source_paratext_register
version: "1.0"
status: canonical
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
authority_generation: HQ-INITIAL
authority_scope: "INITIAL bootstrap rules and attributed metadata only; no narrative findings"
source_boundary: "Metadata only: Japanese colour-edition main V01–45 plus separate 10th Chronicle and Final Guidebook; no narrative admitted"
created: 2026-11-07
last_updated: 2026-11-07
---

# Source and paratext register

## Observed administrative boundary

The 2026-11-04 import metadata, reconciled in the campaign on 2026-11-07, reports 47 Japanese EPUBs: colour main V01–45 and two separately titled companions. Creator metadata is 古舘春一 and publisher metadata 集英社. No numeric gap is reported within the supplied 1–45 range. This is not an exhaustive official-publication or narrative-completeness claim.

No narrative page, EPUB spine, chapter boundary, readable rendering, spread pairing or page-completeness check was independently performed here. Prior import technical checks are attributed evidence, not rerun verification. The public keys below resolve through the governed *Haikyu!!* evidence collection/custodian; private IDs and acquisition paths remain outside Git.

All rows currently have presence METADATA_REPORTED_PRESENT, current-byte identity NOT_VERIFIED, admission NOT_ADMITTED, project inspection NOT_INSPECTED and analytical closure NOT_STARTED. Japanese is metadata-reported, not a fresh all-component language check.

| Local witness key | Reported unit | Source lane |
|---|---|---|
| HQ-COL-V01 | Main colour V01 | Main candidate |
| HQ-COL-V02 | Main colour V02 | Main candidate |
| HQ-COL-V03 | Main colour V03 | Main candidate |
| HQ-COL-V04 | Main colour V04 | Main candidate |
| HQ-COL-V05 | Main colour V05 | Main candidate |
| HQ-COL-V06 | Main colour V06 | Main candidate |
| HQ-COL-V07 | Main colour V07 | Main candidate |
| HQ-COL-V08 | Main colour V08 | Main candidate |
| HQ-COL-V09 | Main colour V09 | Main candidate |
| HQ-COL-V10 | Main colour V10 | Main candidate |
| HQ-COL-V11 | Main colour V11 | Main candidate |
| HQ-COL-V12 | Main colour V12 | Main candidate |
| HQ-COL-V13 | Main colour V13 | Main candidate |
| HQ-COL-V14 | Main colour V14 | Main candidate |
| HQ-COL-V15 | Main colour V15 | Main candidate |
| HQ-COL-V16 | Main colour V16 | Main candidate |
| HQ-COL-V17 | Main colour V17 | Main candidate |
| HQ-COL-V18 | Main colour V18 | Main candidate |
| HQ-COL-V19 | Main colour V19 | Main candidate |
| HQ-COL-V20 | Main colour V20 | Main candidate |
| HQ-COL-V21 | Main colour V21 | Main candidate |
| HQ-COL-V22 | Main colour V22 | Main candidate |
| HQ-COL-V23 | Main colour V23 | Main candidate |
| HQ-COL-V24 | Main colour V24 | Main candidate |
| HQ-COL-V25 | Main colour V25 | Main candidate |
| HQ-COL-V26 | Main colour V26 | Main candidate |
| HQ-COL-V27 | Main colour V27 | Main candidate |
| HQ-COL-V28 | Main colour V28 | Main candidate |
| HQ-COL-V29 | Main colour V29 | Main candidate |
| HQ-COL-V30 | Main colour V30 | Main candidate |
| HQ-COL-V31 | Main colour V31 | Main candidate |
| HQ-COL-V32 | Main colour V32 | Main candidate |
| HQ-COL-V33 | Main colour V33 | Main candidate |
| HQ-COL-V34 | Main colour V34 | Main candidate |
| HQ-COL-V35 | Main colour V35 | Main candidate |
| HQ-COL-V36 | Main colour V36 | Main candidate |
| HQ-COL-V37 | Main colour V37 | Main candidate |
| HQ-COL-V38 | Main colour V38 | Main candidate |
| HQ-COL-V39 | Main colour V39 | Main candidate |
| HQ-COL-V40 | Main colour V40 | Main candidate |
| HQ-COL-V41 | Main colour V41 | Main candidate |
| HQ-COL-V42 | Main colour V42 | Main candidate |
| HQ-COL-V43 | Main colour V43 | Main candidate |
| HQ-COL-V44 | Main colour V44 | Main candidate |
| HQ-COL-V45 | Main colour V45 | Main candidate |
| HQ-CHRONICLE | ハイキュー!! 10thクロニクル | Separate companion |
| HQ-FINAL-GUIDE | ハイキュー!! ファイナルガイドブック 排球極！ | Separate companion |

## Operational schemas

| Record | Required fields |
|---|---|
| Witness/version `HQ-WV-nnnn` | Key/version; exact title/edition/language/publisher/creator or UNKNOWN; immutable digest and byte count; governed receipt reference; original/derivative relation; container/spine and image-map version; verifier/date; equivalence evidence/limits |
| Image occurrence `HQ-PG-nnnn` | Witness/version; one-based image occurrence including covers; spine/member identity; visible printed label if any; chapter; facing-page/spread relation and verification basis; dimensions/readability; component type; authorized frontier; inspection state; full-reading/evidence route |
| Companion component `HQ-PC-nnnn` | Witness; exact component/page range; data/editorial/creator statement/retrospective/technical/art/narrative/unresolved class; author/speaker as established; publication/disclosure boundary; admission scope; interpretation limits; main-lane comparison if authorized |
| Witness relation `HQ-WR-nnnn` | Exact paired witnesses; colour/monochrome/serialization/derivative relation proposed; aligned/unmatched pages; text/art/colour differences; equivalence scope; verifier and evidence; affected claims |

Presence, identity, admission, inspection and analytical closure are independent. Identity states: NOT_VERIFIED / VERIFIED / CHANGED_UNRESOLVED. Admission: NOT_ADMITTED / AUTHORIZED_NOT_ADMITTED / ADMITTED. Page states: REVIEWED_MATERIAL / NO_MATERIAL_ADDITION / DUPLICATE / EXCLUDED / UNRESOLVED_READABILITY; initial pages are not yet mapped. Closure: NOT_STARTED / IN_PROGRESS / ACCEPTED_AT_BOUNDARY.

A page map cannot be guessed from file counts. A duplicated image occurrence and a duplicate publication are different things. Verify spreads and reading order in the actual edition; retain covers/extra pages with explicit classification rather than silently subtracting them.

## Source gaps

| ID | Known limitation | Consequence | Closure requirement |
|---|---|---|---|
| HQ-SG-001 | Current immutable bytes/spine/image order not bound | All future locators and source admission remain pending | Verified exact receipts and deterministic page map |
| HQ-SG-002 | Colour-to-monochrome/serialization relationship and colouring responsibility unknown | Colour claims limited to supplied witness | Separate authorized exact-page comparison and provenance evidence |
| HQ-SG-003 | Companion contents/publication-time spoiler boundaries unexamined | No fan data or retrospective facts in main prospective readings | Component classification, exact boundary and separate admission |
| HQ-SG-004 | Page legibility/completeness/spread mapping uninspected; Japanese metadata only | No source-complete or visual-coverage certification | Actual STILL_IMAGE inspection and language/readability review of selected scope |
| HQ-SG-005 | Supplied 1–45 inventory is not official complete collection/continuation evidence | No inferred terminal story or all-publication scope | Verify selected run/order; separately establish any expanded claim |

The source custodian proposes identity corrections; one series integrator owns the mutable register. Append new versions and preserve former mappings. Changed bytes require equivalence/remapping and dependency review; a repaired derivative never silently overwrites an original. Coverage advances only after actual inspection and accepted reading transaction. Preserve explicit gaps and exclusions.

| History ID | Date | Operation | Result |
|---|---|---|---|
| HQ-SH-001 | 2026-11-07 | Initialized metadata inventory and witness/component schemas | Forty-seven reported witnesses; five gaps; no narrative or companion content admitted |
