---
title: Yuru Camp Current Source Quality and Locator Notes
artifact_id: YURUCAMP_CURRENT_SOURCE_QUALITY_AND_LOCATOR_NOTES
artifact_type: source_quality_audit
series: YURUCAMP
status: canonical
source_boundary: Source identities through V19 acquisition; literary analysis remains V15
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
created: '2026-10-17'
updated: '2026-10-22'
---

# Yuru Camp Current Source Quality and Locator Notes

## Historical October 17 audit scope and results

Fresh checks on 2026-10-17: exact live Drive ID/name/size/parent readback, independent SHA-256, ZIP CRC on every member, full Pillow image decoding, and EPUB container/OPF/manifest/spine parsing. Every referenced reading-spine XHTML resolves to exactly one existing image. This corroborates the independently reported October 16 technical audit, but makes no claim of EPUBCheck validation, complete visual editorial quality review or narrative analysis.

| Source | Drive ID | SHA-256 | Images / dimensions | CRC / decode / spine |
| --- | --- | --- | --- | --- |
| V16 | 1U_krzsI0k5fQkE4H8mAmNPBZD1ueWNKS | 3a6665014f96cc6c7245ec54989bce651fcb42659b2838e6525c9fc96bd2f584 | 168 / 1125×1600 | PASS / PASS / N/A (CBZ) |
| V17 | 1sAvxxFVzSOtobfs2HTjPTK1QqNjxyu96 | 4c0e269486348e18ebd35a584347f06a1c5928775a752e7a6366d6c911a9ac3c | 166 / 1350×1920 | PASS / PASS / 166 complete |
| V18 | 1QEgPUH9Sr-3jVH2C5vr-3ZRJ7xKK4uH4 | 2bea54a3bdefb97905910bd0038d3066e662bfb770ddf446164f8d7e99053395 | 166 / 1350×1920 | PASS / PASS / 166 complete |

## V16 — retained CBZ quality flag and raw locators (historical October 17 audit)

For the retained historical CBZ, preserve `LOCKED_WITH_QUALITY_FLAG` / `USABLE_WATERMARKED_WITH_EXTRANEOUS_INSERTS`. These flags no longer describe the preferred V16 source. The archive contains **168 JPEG images, all 1125×1600**. Persistent third-party corner watermarks remain a limitation. Bottom-strip inspection of raw `0016.jpg`, `0042.jpg`, `0081.jpg`, `0120.jpg` and `0167.jpg` corroborates that flag without beginning story reading. This sampling does not claim every panel is unobscured.

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

### Independent structural concordance follow-up

A subsequent October 17 acceptance pass retrieved the same hashed old and preferred objects and compared all 166 reading-spine images. Grayscale raster correlation at 96×128 initially returned the same-ordinal best match in 129 cases. Visual thumbnail checks of the twelve lowest correlations identified margin/scale differences; the initial result was not treated as reordered narrative. Repeating after an ink bounding-box crop (gray threshold below 220) returned the same-ordinal best match for all **165 nonblank images**. Ordinal 2 is blank in both. Four remaining low-correlation same-position cases (11, 12, 13 and 163) were also visually compared; borders, scaling and end-matter presentation limit pixel equivalence.

This follow-up corroborates the bounded structural crosswalk **old 1-based spine N → preferred 1-based spine N, N=1–166**. It does not certify exhaustive Japanese wording equality, identical crops, printed pagination or publisher-edition equivalence. Keep both object hashes with any migrated locator, resolve the preferred wrapper/image from the manifest, and verify any disputed quotation or composition at full resolution. The earlier paragraph describes the initial source batch; this follow-up supplies additional independent structural comparison without admitting V17 narrative claims.

## V18 — admitted source

The new Kobo object has 166 distinct reading-spine images/assets at 1350×1920; Japanese metadata and pre-paginated fixed layout; all CRC, decoding and mapping checks pass. Its full mapping is in the current manifest and uses the same **structure** as preferred V17; this is not a claim that their content is the same. The Phase 0 missing-source statement remains historically intact. V18 is available but has not been analyzed here.

## October 22 local integrity recheck and source upgrades

Fresh verification used the exact accessible local bytes for preferred V16–V19. All four passed independent SHA-256, every-member ZIP CRC, full in-memory Pillow decoding of all images, EPUB container/OPF/resource checks and all 166 spine→XHTML→image resolutions. Each ZIP has 340 members, an uncompressed first `mimetype` member containing `application/epub+zip`, `item/standard.opf`, right-to-left spine direction and no encryption descriptor. This is not full EPUBCheck validation, exhaustive visual editorial review, a fresh Drive download or narrative reading.

| Preferred source | Drive ID | Bytes | Independently recomputed local SHA-256 | Images / dimensions / spine |
| --- | --- | ---: | --- | --- |
| V16 | 1S6wIlhB--XXMdja34Y-uzrdcR6xOMXNv | 93,334,575 | 89a0c141bcffc614f08c470be93782e9358845eca59ed8f901e9861138214aa3 | 166 / 1350×1920 / 166 complete |
| V17 | 1sAvxxFVzSOtobfs2HTjPTK1QqNjxyu96 | 108,379,583 | 4c0e269486348e18ebd35a584347f06a1c5928775a752e7a6366d6c911a9ac3c | 166 / 1350×1920 / 166 complete |
| V18 | 1QEgPUH9Sr-3jVH2C5vr-3ZRJ7xKK4uH4 | 115,153,335 | 2bea54a3bdefb97905910bd0038d3066e662bfb770ddf446164f8d7e99053395 | 166 / 1350×1920 / 166 complete |
| V19 | 1SUFejNLxWBLfvvfY2xCwyhhvYX8ud3bN | 118,272,724 | b77d071322e1321e52b6d68b254843becedc339b807c982865d99b0d5e32a043 | 166 / 1350×1920 / 166 complete |

### V16 preferred-source replacement and archive crosswalk

Use the Japanese publisher EPUB as `LOCKED_PRIMARY` / `PREFERRED_JAPANESE_PUBLISHER_FIXED_LAYOUT`. The October 22 acquisition review reports no watermark in its sampled new pages; this reconciliation independently confirms dimensions, structural order and integrity, not an exhaustive absence-of-watermarks judgment. The old CBZ remains preserved under Drive ID `1U_krzsI0k5fQkE4H8mAmNPBZD1ueWNKS` in archive folder `19Yo7DYiZdhsxT3GnEBRSX-fH6abgBjIk`. Its independently rechecked SHA-256 remains `3a6665014f96cc6c7245ec54989bce651fcb42659b2838e6525c9fc96bd2f584`, with all 168 images intact. Keep the preceding historical quality flags and printed-page anchors attributable to that CBZ.

An independent non-displayed raster comparison reproduced every row of the acquisition crosswalk: RGB 48×48 Lanczos resampling, mean absolute difference against all 168 old images, 166 unique nearest matches, no ties and strictly increasing old positions. Maximum matched MAE was 1.4327256944/255, mean 0.8848135598/255. The comparison verifies correspondence, not identical image bytes, exhaustive Japanese wording equality or printed pagination.

| Preferred one-based spine position | Retained CBZ one-based raw image position |
| --- | --- |
| 1–78 | Same position |
| 79–129 | Preferred position + 1 |
| 130–166 | Preferred position + 2 |

Old raw79 (`0079.jpg`) and raw131 (`0131.jpg`) have no preferred counterpart; their non-story-advertisement classification remains supported by the preserved October 17 visual check and October 22 acquisition review. They are retained in the old object. The acquisition comparison's initial same-index page comparisons are not the crosswalk after the first insertion; the ordered nearest-page alignment is the appropriate mapping.

### Exact preferred EPUB locator scheme and V19 admission

The current machine manifest records all 166 structural rows for each preferred V16–V19 EPUB, independently checked in full. Their shared wrapper scheme is: spine1 → `p-cover` → `item/xhtml/p-cover.xhtml` → `item/image/cover_omo.jpg`; spine2–164 → id `p-{spine-1:03}` and matching XHTML → image `item/image/i-{spine-2:03}.jpg`; spine165 → `p-164.xhtml` → `cover.jpg`; spine166 → `p-165.xhtml` → `hyoushi.jpg` (the latter two under `item/xhtml/` and `item/image/`). Sharing a structure does not imply sharing content. Use the exact recorded row, object hash, chapter and scene; printed pages require visual verification. Source-order chapter/scene maps belong to the authorized sequential reading, not this structural reconciliation.

V19 is now acquired and technically mapped; the earlier published-but-unacquired observation remains historical. No V19 narrative claim is admitted here. The accepted October 17 V17 old-spine-N→preferred-spine-N concordance and its wording/crop/pagination limits remain unchanged above.

October 22 propagation metadata provides recorded Drive identities, names, sizes, MIME types and parents. Local byte hashes have been independently verified; no remote content hash has been independently verified by this reconciliation. Preserve older live-readback dates rather than treating metadata readback or a matching size as remote byte equality.

## Limits and preservation

Technical integrity does not verify literary claims. The current manifest preserves older audit dates and labels supplement hashes as reported. No binaries, extracted pages, contact sheets or source images are in Git. No manga narrative from V16–V19 or supplementary continuity has been admitted into the retrospective V01–V15 ledgers.
