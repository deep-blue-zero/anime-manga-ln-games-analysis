---
title: "The Apothecary Diaries — Source Witness and Coverage Map"
artifact_id: AP_SOURCE_MAP
artifact_type: source_witness_and_coverage_map
version: "1.0"
status: canonical
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
authority_generation: AP-INITIAL
authority_scope: "INITIAL bootstrap method, architecture, and administrative metadata only; no literary findings"
source_boundary: "Metadata reconnaissance: Japanese volumes 01–16 and separate simplified Chinese volume 15; no narrative admitted"
created: 2026-11-07
last_updated: 2026-11-07
---

# Source witness and coverage map

## Scope of evidence

This is an administrative map of **reported source witnesses**, not an inspection receipt. Campaign metadata reconciliation identified the supplied range on 2026-11-07. The source audit dated 2026-10-24 supplies the historical checks below. No narrative prose, chapter map, local source checksum or illustration was independently inspected for this foundation.

The authoritative external evidence collection is the governed *Apothecary Diaries* source collection. Private object resolution and receipts remain there or in the authorized campaign ledger. The public keys below are project-local references; none is a remote file ID. A future receipt must bind key → exact witness version → immutable digest → spine/section mapping before admission.

## Historical audit, accurately bounded

The audit reports seventeen EPUBs: Japanese V01–16 and simplified Chinese V15. The originally mislabeled V15 contained Chinese prose despite retained Japanese headings/navigation or image wrappers. The audit reports script screening and distributed checks, language-tag correction and a later replacement Japanese V15. Those are the audit's findings, not independent narrative work performed here.

It reports that the Chinese witness's OPF/text-bearing language metadata and packaging were corrected, Japanese navigation/image-only wrappers were preserved, no prose or images changed, and the original was retained outside Git. The Japanese witnesses were unchanged through their audit renaming. No byte-identical archives were found. Japanese V15 and Chinese V15 nevertheless share an embedded UUID; content identity must not be inferred from that field.

The reported historical checks include ZIP CRC, manifest/spine/resource presence, XHTML/reference checks, raster decoding and full extractable-spine script screening, with three distributed text excerpts manually checked. These support the provenance statement at the historical boundary, not present remote-byte verification or exhaustive literary inspection. Japanese V12–16 retain a warning that `mimetype` is not the first ZIP member. The audit is not a full EPUBCheck or Calibre-render certification. Small illustrations and incomplete exhaustive visual QA remain limitations. It also does not certify that every later upload replicated the inspected bytes.

## Witness inventory

All rows have presence state `METADATA_REPORTED_PRESENT`. “NOT_INSPECTED” refers to this analytical project, not a denial that the historical auditor ran the reported checks. Official publication completeness is unknown.

| Local witness key | Supplied unit | Language | Lane | Immutable current bytes | Narrative admission | Project inspection | Material qualifier |
|---|---|---|---|---|---|---|---|
| AP-JP-V01 | Japanese V01 | ja, reported | JP anchor candidate | NOT_VERIFIED | NOT_ADMITTED | NOT_INSPECTED | No unit-specific defect established here |
| AP-JP-V02 | Japanese V02 | ja, reported | JP anchor candidate | NOT_VERIFIED | NOT_ADMITTED | NOT_INSPECTED | No unit-specific defect established here |
| AP-JP-V03 | Japanese V03 | ja, reported | JP anchor candidate | NOT_VERIFIED | NOT_ADMITTED | NOT_INSPECTED | No unit-specific defect established here |
| AP-JP-V04 | Japanese V04 | ja, reported | JP anchor candidate | NOT_VERIFIED | NOT_ADMITTED | NOT_INSPECTED | No unit-specific defect established here |
| AP-JP-V05 | Japanese V05 | ja, reported | JP anchor candidate | NOT_VERIFIED | NOT_ADMITTED | NOT_INSPECTED | No unit-specific defect established here |
| AP-JP-V06 | Japanese V06 | ja, reported | JP anchor candidate | NOT_VERIFIED | NOT_ADMITTED | NOT_INSPECTED | No unit-specific defect established here |
| AP-JP-V07 | Japanese V07 | ja, reported | JP anchor candidate | NOT_VERIFIED | NOT_ADMITTED | NOT_INSPECTED | No unit-specific defect established here |
| AP-JP-V08 | Japanese V08 | ja, reported | JP anchor candidate | NOT_VERIFIED | NOT_ADMITTED | NOT_INSPECTED | No unit-specific defect established here |
| AP-JP-V09 | Japanese V09 | ja, reported | JP anchor candidate | NOT_VERIFIED | NOT_ADMITTED | NOT_INSPECTED | No unit-specific defect established here |
| AP-JP-V10 | Japanese V10 | ja, reported | JP anchor candidate | NOT_VERIFIED | NOT_ADMITTED | NOT_INSPECTED | No unit-specific defect established here |
| AP-JP-V11 | Japanese V11 | ja, reported | JP anchor candidate | NOT_VERIFIED | NOT_ADMITTED | NOT_INSPECTED | No unit-specific defect established here |
| AP-JP-V12 | Japanese V12 | ja, reported | JP anchor candidate | NOT_VERIFIED | NOT_ADMITTED | NOT_INSPECTED | Historical mimetype-order warning |
| AP-JP-V13 | Japanese V13 | ja, reported | JP anchor candidate | NOT_VERIFIED | NOT_ADMITTED | NOT_INSPECTED | Historical mimetype-order warning |
| AP-JP-V14 | Japanese V14 | ja, reported | JP anchor candidate | NOT_VERIFIED | NOT_ADMITTED | NOT_INSPECTED | Historical mimetype-order warning |
| AP-JP-V15 | Japanese V15 | ja, reported | JP anchor candidate | NOT_VERIFIED | NOT_ADMITTED | NOT_INSPECTED | Historical mimetype-order warning |
| AP-JP-V16 | Japanese V16 | ja, reported | JP anchor candidate | NOT_VERIFIED | NOT_ADMITTED | NOT_INSPECTED | Historical mimetype-order warning |
| AP-ZH-HANS-V15 | Separate Chinese V15 | zh-Hans, historical correction | Separate comparison witness | NOT_VERIFIED | NOT_ADMITTED | NOT_INSPECTED | Shares embedded UUID with Japanese V15; never deduplicate by UUID |

## Operational schemas

A witness-version record must contain: local witness key; version ID; title/creator/publisher/edition and language as established, or UNKNOWN; source receipt reference; immutable digest; observed byte count; container identity; spine-map/extraction version; source category; source/derivative relation; metadata-versus-visible-text disagreement; inspection capability; verifier/date; equivalence status and evidence; superseded-version relation. Keep private acquisition details in the governed receipt and publish only eligible references.

A component coverage record must contain: `coverage_id`; witness version; verified spine/member and human section; component type (`NARRATIVE / ILLUSTRATION / FRONT_MATTER / AFTERWORD / BONUS / PREVIEW / UNRESOLVED`); intended ordering; run authorization and frontier; inspection lane; inspected extent; excluded extent and reason; full-reading route; retrieval-test route/result; outstanding debt; closure reviewer.

States are independent: presence `METADATA_REPORTED_PRESENT / RECEIVED / MISSING / UNRESOLVED`; byte identity `NOT_VERIFIED / VERIFIED / CHANGED_UNRESOLVED`; admission `NOT_ADMITTED / AUTHORIZED_NOT_ADMITTED / ADMITTED`; inspection `NOT_INSPECTED / PARTIAL / COMPLETE_FOR_DECLARED_COMPONENTS`; analytical closure `NOT_STARTED / IN_PROGRESS / ACCEPTED_AT_BOUNDARY`. Historical integrity checks never advance a different state automatically.

Reserve `AP-COV-nnnn` for actual verified components. No fabricated chapters, locators or coverage records are created now. When components become known, retain non-narrative and excluded ones so a complete spine does not disappear behind a narrative-only table.

## Open source obligations

| Gap ID | Established limitation | Effect | Closure evidence / responsible future operation |
|---|---|---|---|
| AP-SG-001 | No immutable current witness receipt or source-unit map bound here | All seventeen remain unadmitted and uninspected | Source custodian verifies exact bytes, metadata, language and spine mapping; record public-safe key/digest route |
| AP-SG-002 | Japanese and Chinese V15 share embedded UUID; historical mislabel correction | Identity and language conflation risk | Verify separate byte/language identities and maintain separate keys; any comparison needs verified alignment and authorization |
| AP-SG-003 | Historical V12–16 ZIP mimetype-order warning; no full render certification | Transport/processing usability remains route-specific | Verify actual parsing/render route without altering originals; record derivative provenance if repair is necessary |
| AP-SG-004 | Historical audit does not certify current remote replication or exhaustive visual QA | Present bytes and illustration evidence remain uncertain | Replication receipt and actual needed image inspection; preserve partial coverage if incomplete |
| AP-SG-005 | Supplied V01–16 range is not official publication-completeness evidence; exact chapter/order map unverified | No full-work completion claim or invented terminal sequence | Verify selected run units/order; separately establish any expanded publication boundary before extending scope |

## Update and history rules

The source custodian proposes identity/component changes; the active series integrator owns this mutable map. Append new witness versions and retain prior identity evidence. Correct clerical metadata with a dated reason; never erase a language disagreement, packaging warning or earlier failed route. Bind coverage only after the actual inspection, and update analytical closure only with the accepted full-reading transaction. Source admission follows the entrypoint lock and authorized run, not this table.

A changed hash invalidates affected deterministic locators until equivalence and remapping are tested. A repaired ZIP is a derivative, not an invisible overwrite. Check dependency rows in the integration ledger and downgrade unsupported claim routes while unresolved.

| History ID | Date | Operation | Result and remaining limitation |
|---|---|---|---|
| AP-SH-001 | 2026-11-07 | Initialized from campaign metadata and attributed 2026-10-24 audit | Seventeen distinct reported witnesses, five explicit gaps; no narrative admitted and no live-byte verification claimed |
