---
title: Yuru Camp Current Source Quality and Locator Notes
artifact_id: YURUCAMP_CURRENT_SOURCE_QUALITY_AND_LOCATOR_NOTES
artifact_type: source_quality_audit
series: YURUCAMP
status: canonical
source_boundary: Source identities through V19 acquisition; literary analysis complete through V18
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
created: '2026-10-17'
updated: '2026-10-23'
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

Technical integrity does not verify literary claims. The current manifest preserves older audit dates and labels supplement hashes as reported. No binaries, extracted pages, contact sheets or source images are in Git. The October 17 V01–V15 retrospective backfill admitted no V16–V19 or supplementary-continuity narrative. The separately dated continuation below extends the current ledgers.

## V16 literary transaction — 2026-10-23

All 166 preferred EPUB spine images were visually read in order, then integrated under the method’s second pass. The [V16 reading](../03%20Volume%20Deep%20Readings/YURUCAMP_V16_DEEP_READING.md) owns the exact chapter/scene map: chapters 88–92 spine005–132, interstitials separately; earlier spring-break special 135–158; Heya 159–162; afterword/colophon/jackets 163–166. This is distinct from the dated technical checks above. Main Golden Week narrative ends before the Nozori overnight. Printed contents starts 3/29/55/81/107/133/157 are separately observed, not an asserted universal spine-to-print conversion. No V17+ literary finding or supplement continuity is admitted.

## V17 literary transaction and exact current locator lookup — 2026-10-23

All 166 preferred V17 original spine images were individually visually inspected in order, followed by a separate analytical Pass B. The [V17 reading](../03%20Volume%20Deep%20Readings/YURUCAMP_V17_DEEP_READING.md) owns chapter/scene claims; this table supplies the source-order lookup. It adds literary inspection to the current boundary without rewriting the dated October 17/22 structural checks or the V16 literary receipt. V18/V19 and supplementary-continuity narrative remain NOT ANALYZED/not admitted.

For each endpoint below, XHTML basenames are under `item/xhtml/` and image basenames under `item/image/`; both exact endpoints come from the existing manifest rows. A range retains all intermediate positions, whose exact row remains in `technical.spine_image_map`. The V17-only `literary_section_map` records these ranges and chapter-title anchors separately from technical data. Printed contents starts are separately identified: 3/29/55/81/107/135/159. In particular the first Ch95 image and first Heya image do not show those opening folios; contents entries do not silently become visual folio verification.

| Section | Preferred spine range | Exact start XHTML → image | Exact end XHTML → image | Printed locator / title anchor |
| --- | --- | --- | --- | --- |
| Opening cover, blank, color illustration and contents | 001–004 | `p-cover.xhtml` → `cover_omo.jpg` | `p-003.xhtml` → `i-002.jpg` | No printed-page conversion asserted |
| Ch93 焼きまんじゅう改造計画 | 005–028 | `p-004.xhtml` → `i-003.jpg` | `p-027.xhtml` → `i-026.jpg` | Contents start 3; visible start 3; visible end 26; title spine 006 `p-005.xhtml` → `i-004.jpg` |
| Ch93 transition vignettes | 029–030 | `p-028.xhtml` → `i-027.jpg` | `p-029.xhtml` → `i-028.jpg` | No printed-page conversion asserted |
| Ch94 タイムアップ寸前!? キャンプ場までどれくらい? | 031–054 | `p-030.xhtml` → `i-029.jpg` | `p-053.xhtml` → `i-052.jpg` | Contents start 29; visible start 29; visible end 52; title spine 032 `p-031.xhtml` → `i-030.jpg` |
| Ch94 transition vignettes | 055–056 | `p-054.xhtml` → `i-053.jpg` | `p-055.xhtml` → `i-054.jpg` | No printed-page conversion asserted |
| Ch95 キャンプの夜とgummmaのなぞ | 057–080 | `p-056.xhtml` → `i-055.jpg` | `p-079.xhtml` → `i-078.jpg` | Contents start 55; start folio not visible; visible end 78; title spine 059 `p-058.xhtml` → `i-057.jpg` |
| Ch95 transition vignettes | 081–082 | `p-080.xhtml` → `i-079.jpg` | `p-081.xhtml` → `i-080.jpg` | No printed-page conversion asserted |
| Ch96 群馬二日目ぶらり旅 | 083–106 | `p-082.xhtml` → `i-081.jpg` | `p-105.xhtml` → `i-104.jpg` | Contents start 81; visible start 81; visible end 104; title spine 085 `p-084.xhtml` → `i-083.jpg` |
| Ch96 transition vignettes | 107–108 | `p-106.xhtml` → `i-105.jpg` | `p-107.xhtml` → `i-106.jpg` | No printed-page conversion asserted |
| Ch97 初夏の野反湖冬景色 | 109–134 | `p-108.xhtml` → `i-107.jpg` | `p-133.xhtml` → `i-132.jpg` | Contents start 107; visible start 107; visible end 132; title spine 112 `p-111.xhtml` → `i-110.jpg` |
| Ch97 transition vignettes | 135–136 | `p-134.xhtml` → `i-133.jpg` | `p-135.xhtml` → `i-134.jpg` | No printed-page conversion asserted |
| Ch98 旅の終わりと野反湖の夜 | 137–160 | `p-136.xhtml` → `i-135.jpg` | `p-159.xhtml` → `i-158.jpg` | Contents start 135; visible start 135; visible end 158; title spine 138 `p-137.xhtml` → `i-136.jpg` |
| Heya Camp 放課後128 桜お姉ちゃんの料理教室 | 161–162 | `p-160.xhtml` → `i-159.jpg` | `p-161.xhtml` → `i-160.jpg` | Contents start 159; start folio not visible; visible end 160 |
| Author afterword and initial-publication list | 163–163 | `p-162.xhtml` → `i-161.jpg` | `p-162.xhtml` → `i-161.jpg` | No printed-page conversion asserted |
| Electronic-edition colophon | 164–164 | `p-163.xhtml` → `i-162.jpg` | `p-163.xhtml` → `i-162.jpg` | No printed-page conversion asserted |
| Full jacket | 165–165 | `p-164.xhtml` → `cover.jpg` | `p-164.xhtml` → `cover.jpg` | No printed-page conversion asserted |
| Tenth-anniversary metafiction comic | 166–166 | `p-165.xhtml` → `hyoushi.jpg` | `p-165.xhtml` → `hyoushi.jpg` | No printed-page conversion asserted |

Ch97 retains spine 113 as a full lake panorama and spine 114 as the original GO NEXT PAGE navigation image; spine 115 visibly resumes printed 113. Main narrative ends at spine 160 / printed 158, before the separate Heya and closing matter. Do not delete or renumber title, transition, navigation, blank or paratext images. A source locator identifies the page; a dream, reported scene or retrospective image within it still needs its correct narrative mode, as distinguished in the reading. None of this is a blanket raw/spine-to-printed offset or permission to reuse an archived V17 wrapper without its explicit concordance.

## V18 literary transaction and exact current locator lookup — 2026-10-23

All 166 preferred V18 original spine images were individually visually inspected in source order, followed by a separate analytical Pass B. The [V18 reading](../03%20Volume%20Deep%20Readings/YURUCAMP_V18_DEEP_READING.md) owns chapter/scene claims; this table supplies the source-order lookup. This dated literary inspection extends the current boundary beyond the earlier technical-admission paragraph without rewriting the October 17/22 checks or the V16/V17 literary receipts. V19 remains NOT ANALYZED; its narrative must await the independently accepted and committed V16–V18 checkpoint. Supplementary-continuity narrative remains separate and not admitted.

XHTML basenames below are under `item/xhtml/` and image basenames under `item/image/`. Every start, end and title anchor comes from the unchanged V18 `technical.spine_image_map`; all intermediate positions remain recorded there. The V18 `literary_section_map` records the inspected ranges separately. Contents starts 3/29/55/81/107/133/157 are distinct from visible folios. In particular the full-title images 031/109 and first Heya image 159 do not display their contents opening folios. There is no separately listed contents start for Heya 130.

| Section | Preferred spine range | Exact start XHTML → image | Exact end XHTML → image | Printed locator / title anchor |
| --- | --- | --- | --- | --- |
| Opening cover, blank, color illustration and contents | 001–004 | `p-cover.xhtml` → `cover_omo.jpg` | `p-003.xhtml` → `i-002.jpg` | No printed-page conversion asserted |
| Ch99 諏訪湖までどれくらい? | 005–028 | `p-004.xhtml` → `i-003.jpg` | `p-027.xhtml` → `i-026.jpg` | Contents start 3; visible start 3; visible end 26; title spine 006 `p-005.xhtml` → `i-004.jpg` |
| Ch99 transition vignettes | 029–030 | `p-028.xhtml` → `i-027.jpg` | `p-029.xhtml` → `i-028.jpg` | No printed-page conversion asserted |
| Ch100 フランクフルトには何が合うか問題 | 031–054 | `p-030.xhtml` → `i-029.jpg` | `p-053.xhtml` → `i-052.jpg` | Contents start 29; start folio not visible; visible end 52; title spine 031 `p-030.xhtml` → `i-029.jpg`; first story spine 032 visibly 30 |
| Ch100 transition vignettes | 055–056 | `p-054.xhtml` → `i-053.jpg` | `p-055.xhtml` → `i-054.jpg` | No printed-page conversion asserted |
| Ch101 行き当たりばったり奥三河ツーリング | 057–080 | `p-056.xhtml` → `i-055.jpg` | `p-079.xhtml` → `i-078.jpg` | Contents start 55; visible start 55; visible end 78; title spine 058 `p-057.xhtml` → `i-056.jpg` |
| Ch101 transition vignettes | 081–082 | `p-080.xhtml` → `i-079.jpg` | `p-081.xhtml` → `i-080.jpg` | No printed-page conversion asserted |
| Ch102 ツーリングは用法・用量を守り正しくお楽しみ下さい | 083–106 | `p-082.xhtml` → `i-081.jpg` | `p-105.xhtml` → `i-104.jpg` | Contents start 81; visible start 81; visible end 104; title spine 086 `p-085.xhtml` → `i-084.jpg` |
| Ch102 transition vignettes | 107–108 | `p-106.xhtml` → `i-105.jpg` | `p-107.xhtml` → `i-106.jpg` | No printed-page conversion asserted |
| Ch103 くうねるはしる | 109–132 | `p-108.xhtml` → `i-107.jpg` | `p-131.xhtml` → `i-130.jpg` | Contents start 107; start folio not visible; visible end 130; title spine 109 `p-108.xhtml` → `i-107.jpg`; first story spine 110 visibly 108 |
| Ch103 transition vignettes | 133–134 | `p-132.xhtml` → `i-131.jpg` | `p-133.xhtml` → `i-132.jpg` | No printed-page conversion asserted |
| Ch104 この先通り抜けできません | 135–158 | `p-134.xhtml` → `i-133.jpg` | `p-157.xhtml` → `i-156.jpg` | Contents start 133; visible start 133; visible end 156; title spine 136 `p-135.xhtml` → `i-134.jpg` |
| Heya Camp 放課後129 むじんのなぞ | 159–160 | `p-158.xhtml` → `i-157.jpg` | `p-159.xhtml` → `i-158.jpg` | Contents start 157; start folio not visible; visible end 158; title spine 159 `p-158.xhtml` → `i-157.jpg` |
| Heya Camp 放課後130 ほらかほんまか甲州弁講座 | 161–162 | `p-160.xhtml` → `i-159.jpg` | `p-161.xhtml` → `i-160.jpg` | No separate contents start; visible start 159; visible end 160; title spine 161 `p-160.xhtml` → `i-159.jpg` |
| Author afterword and initial-publication list | 163–163 | `p-162.xhtml` → `i-161.jpg` | `p-162.xhtml` → `i-161.jpg` | No printed-page conversion asserted |
| Electronic-edition colophon | 164–164 | `p-163.xhtml` → `i-162.jpg` | `p-163.xhtml` → `i-162.jpg` | No printed-page conversion asserted |
| Full jacket | 165–165 | `p-164.xhtml` → `cover.jpg` | `p-164.xhtml` → `cover.jpg` | No printed-page conversion asserted |
| Alternate-world/time-leap metafiction comic | 166–166 | `p-165.xhtml` → `hyoushi.jpg` | `p-165.xhtml` → `hyoushi.jpg` | No printed-page conversion asserted |

Chapter 102 has three story images before its title at spine 086. Chapter 103 ends at the first collapse barrier at 132, before transition images 133–134 and Chapter 104. Main narrative ends at 158 / visible 156 before the separate Heya strips; the author afterword at 163 calls this the first part of the 152 touring arc. The final proposed destination is not shown reached. Preserve all title, transition, blank and paratext positions; an alternate-world/time-leap underjacket at 166 is not a literal future outcome.

The permit at spine 018 visibly says 5月2日 while the next depicted day's livecamera at 096 shows 05/02. These marks are retained without resolving an exact starting calendar date or assuming what date the permit denotes. This bounded chronology uncertainty does not alter the spine map. None of this is a blanket raw/spine-to-printed offset, a fresh technical audit or remote content-hash verification.
