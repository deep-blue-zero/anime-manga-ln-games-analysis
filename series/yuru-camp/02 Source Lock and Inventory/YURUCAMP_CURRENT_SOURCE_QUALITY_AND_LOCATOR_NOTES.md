---
title: Yuru Camp Current Source Quality and Locator Notes
artifact_id: YURUCAMP_CURRENT_SOURCE_QUALITY_AND_LOCATOR_NOTES
artifact_type: source_quality_audit
series: YURUCAMP
status: canonical
source_boundary: Source metadata through V19 publication; literary analysis remains V15
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
created: '2026-10-17'
---

# Yuru Camp Current Source Quality and Locator Notes

## Audit scope and results

Fresh checks on 2026-10-17: exact live Drive ID/name/size/parent readback, independent SHA-256, ZIP CRC on every member, full Pillow image decoding, and EPUB container/OPF/manifest/spine parsing. Every referenced reading-spine XHTML resolves to exactly one existing image. This corroborates the independently reported October 16 technical audit, but makes no claim of EPUBCheck validation, complete visual editorial quality review or narrative analysis.

| Source | Drive ID | SHA-256 | Images / dimensions | CRC / decode / spine |
| --- | --- | --- | --- | --- |
| V16 | 1U_krzsI0k5fQkE4H8mAmNPBZD1ueWNKS | 3a6665014f96cc6c7245ec54989bce651fcb42659b2838e6525c9fc96bd2f584 | 168 / 1125×1600 | PASS / PASS / N/A (CBZ) |
| V17 | 1sAvxxFVzSOtobfs2HTjPTK1QqNjxyu96 | 4c0e269486348e18ebd35a584347f06a1c5928775a752e7a6366d6c911a9ac3c | 166 / 1350×1920 | PASS / PASS / 166 complete |
| V18 | 1QEgPUH9Sr-3jVH2C5vr-3ZRJ7xKK4uH4 | 2bea54a3bdefb97905910bd0038d3066e662bfb770ddf446164f8d7e99053395 | 166 / 1350×1920 | PASS / PASS / 166 complete |

## V16 — quality flag and raw locators

Retain `LOCKED_WITH_QUALITY_FLAG` / `USABLE_WATERMARKED_WITH_EXTRANEOUS_INSERTS`. The archive contains **168 JPEG images, all 1125×1600**. Persistent third-party corner watermarks remain a limitation. Bottom-strip inspection of raw `0016.jpg`, `0042.jpg`, `0081.jpg`, `0120.jpg` and `0167.jpg` corroborates that flag without beginning story reading. This sampling does not claim every panel is unobscured.

Raw `0079.jpg` and `0131.jpg` are **byte-identical non-story advertisements**, SHA-256 `2a9e7083c99b24cf06ee65e61dd7dd1427cfeacaa304f9d2a75a1f203f887fad`. One was visually checked after byte equality established the identity. They are excluded from narrative interpretation but retained in archive indexing. Do not remove them and silently renumber later pages. Nor should the remaining 166 images be called 166 story pages: covers, contents and other matter require their own source-unit map when V16 is authorized.

Cite `V16 / archive SHA-256 / exact raw member / printed page if visibly verified / chapter / scene`. Sample bottom-strip anchors are raw0016→printed14, raw0042→40, raw0081→78, raw0120→117. The changing offset demonstrates why a single arithmetic raw-to-print conversion is unsafe. Do not extrapolate a full chapter map from these technical anchors.

A future reader must lock chapter boundaries from the source, retain ad slots in the manifest, distinguish mark-induced ambiguity from intentional art, and abstain or seek a better source if dialogue/expressions/panel edges are obscured. No blanket “clean source” claim is permitted. V16 has not been analyzed in this repair.

## V17 — replacement chain

| Role | Drive ID / location | SHA-256 | Technical state |
| --- | --- | --- | --- |
| Historical Phase 0 / retained archive | 1itEg_5CH3XR138EBsbTxYeZyiUk9uOT1 / folder 19Yo7DYiZdhsxT3GnEBRSX-fH6abgBjIk | 922280f5c2735bc024d25861a0eaf62e1f0486ffcb47634cc39098eb2a14fb4e | 166 spine pages; 167 image assets at 584×754; OPF language en; CRC/decode/mapping pass |
| Current preferred September Kobo | 1sAvxxFVzSOtobfs2HTjPTK1QqNjxyu96 / primary root | 4c0e269486348e18ebd35a584347f06a1c5928775a752e7a6366d6c911a9ac3c | 166 spine images/assets at 1350×1920; Japanese ja; pre-paginated fixed layout; CRC/decode/mapping pass |

The September comparison reports cropped content in sampled older pages. That is **ingestion-report evidence**, not a fresh visual comparison performed here. Fresh dimensions, metadata, object hashes and the preserved replacement chain independently support routing to the higher-resolution source. The old object is historical evidence and fallback comparison material, not an interchangeable preferred edition. Same spine count does not prove identical page contents, crops or page numbering.

Current preferred locators: OPF `item/standard.opf`; 1-based spine1 → `item/xhtml/p-cover.xhtml` → `item/image/cover_omo.jpg`; spine2 → `item/xhtml/p-001.xhtml` → `item/image/i-000.jpg`; spine166 → `item/xhtml/p-165.xhtml` → `item/image/hyoushi.jpg`. Use the manifest’s full 166-row mapping, not an inferred filename offset. Old locators use `content.opf` and `page_1.xhtml`→`0_0.png` through `page_166.xhtml`→`165_0.png`; never carry those filenames into a new-source citation without an explicit concordance.

## V18 — admitted source

The new Kobo object has 166 distinct reading-spine images/assets at 1350×1920; Japanese metadata and pre-paginated fixed layout; all CRC, decoding and mapping checks pass. Its full mapping is in the current manifest and uses the same **structure** as preferred V17; this is not a claim that their content is the same. The Phase 0 missing-source statement remains historically intact. V18 is available but has not been analyzed here.

## Limits and preservation

Technical integrity does not verify literary claims. The current manifest preserves older audit dates and labels supplement hashes as reported. No binaries, extracted pages, contact sheets or source images are in Git. No manga narrative from V16–V19 or supplementary continuity has been admitted into the retrospective V01–V15 ledgers.
