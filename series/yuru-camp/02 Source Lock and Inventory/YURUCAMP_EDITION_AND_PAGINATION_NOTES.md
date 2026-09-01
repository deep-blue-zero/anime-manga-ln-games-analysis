---
title: "Yuru Camp Edition and Pagination Notes — Phase 0"
series: "ゆるキャン△ / Yuru Camp△"
document_type: "edition_pagination_notes"
phase: 0
status: "active"
---

# Yuru Camp△ Edition and Pagination Notes — Phase 0

## 1. Governing locator principle

The project must cite the **actual archived page object**, not an inferred prose-page number.

Preferred locator form for V01–V16:

> `V05 / 0083.jpg / panel or region`

When a printed manga page number is visible and analytically useful:

> `V05 / 0083.jpg / printed p.XX / lower-right panel`

For V17, use **EPUB spine order plus image asset**:

> `V17 / spine page 083 / 82_0.png / panel or region`

This preserves stable traceability even if a later clean derivative is generated.

## 2. CBZ source structure, V01–V16

All sixteen CBZ manga volumes:

- are valid ZIP containers;
- pass CRC integrity testing;
- contain numerically continuous image filenames with no numeric gaps;
- contain a `ComicInfo.xml` metadata file;
- identify Japanese (`ja`) and right-to-left manga reading;
- have `ComicInfo` page counts matching the archived image count;
- mark image 0 as `FrontCover`;
- preserve front matter and end matter rather than extracting story pages only.

Visual edge-page inspection confirms consistent retention of:

- front covers;
- inside/front matter;
- early color illustration/title/contents material;
- normal black-and-white manga pages;
- colophon/publication matter;
- end-of-volume promotional/back matter.

Exact semantic classification of every omake, map, diagram, author note, and advertisement is intentionally deferred to the volume deep reading, where it can be read rather than guessed from image position.

## 3. Dimensions and source families

- V01: predominantly **1125×1600**.
- V02–V12: predominantly **1350×1920**.
- V13: 181 pages at 1350×1920; one page at 1351×1920.
- V14: 181 pages at 1350×1920; two pages at 1348×1920.
- V15: 165 pages at 1350×1920; one page at 1349×1920.
- V16: **1125×1600** throughout.

The small one- to two-pixel width variants in V13–V15 are not treated as corruption. All affected images decode and the numeric sequence remains continuous.

## 4. Provenance of V01–V16

Embedded `ComicInfo.xml` identifies each volume as a **non-destructive derivative** and records DLRAW.TO-derived source paths. This metadata appears to have been added during derivative packaging and must not be treated as publisher-authored bibliographic metadata.

The analysis therefore distinguishes:

- **primary textual/visual content:** Afro's Japanese manga pages;
- **digital-container provenance:** unofficial derivative CBZ;
- **publication authority:** Houbunsha, as identified by the work and metadata but not by a publisher-native downloaded container.

## 5. V16 special handling

V16 is internally intact but visually contaminated by third-party source material.

Observed facts:

- all 168 images decode;
- numeric sequence 0001.jpg–0168.jpg is continuous;
- visible `RawLazy.Si` / `DL-Raw.Se` marks appear on sampled manga pages;
- `0079.jpg` and `0131.jpg` are byte-identical copies of the same third-party interstitial advertisement;
- surrounding pages show that these are inserted between manga pages, not duplicated manga content.

Therefore:

- retain the raw V16 source unchanged for provenance;
- classify 0079.jpg and 0131.jpg as `EXTRANEOUS_SOURCE_INSERT`;
- do not use those pages as manga evidence;
- do not renumber the archive destructively;
- when citing later pages, use the immutable archive filename and, when available, the printed page number;
- accept a cleaner V16 source later as a controlled replacement if one becomes available.

## 6. V17 EPUB structure

V17 is a fixed-layout/image-based EPUB rather than reflowable prose.

Verified structure:

- ZIP/EPUB CRC passes;
- 167 image assets total;
- 166 XHTML reading-spine entries;
- the 166 spine pages map to `0_0.png` through `165_0.png`;
- `cover.jpg` is a separate cover asset and is visually near-identical to the spine cover image, differing primarily by encoding/compression;
- all 167 image assets pass a dedicated image-verification pass;
- dominant dimensions are **584×754**;
- OPF title: `ゆるキャン△ １７巻`;
- creator: `あｆろ`;
- publisher: `芳文社`;
- ISBN identifier present: `9784832296213`;
- calibre series metadata identifies volume index `17.0`;
- OPF language is incorrectly recorded as `en` despite the pages being Japanese.

The low resolution is sufficient for normal dialogue and panel reading in sampled pages, but it is materially weaker for:

- tiny furigana;
- handwritten marginal reactions;
- fine environmental text;
- very small signage;
- subtle line/detail inspection.

V17 is therefore a **provisional analysis source**, not the desired final archival source.

## 7. V17 replacement policy

When a higher-resolution V17 arrives:

1. preserve the present EPUB hash and inventory entry;
2. audit the replacement independently;
3. compare page order, front/end matter, and content continuity;
4. designate the better source as preferred;
5. if V17 has already been analyzed, revalidate only claims sensitive to resolution or page identity unless the replacement reveals substantive differences.

No previous source record should be deleted.

## 8. V18 insertion policy

When V18 arrives:

- add it as a new source; do not rewrite the earlier source lock;
- hash and CRC-test it;
- verify page/image continuity;
- record edition/container notes;
- update current-corpus completeness from 17/18 to 18/18;
- maintain the publication-order reading boundary.

## 9. Chapter mapping

The present CBZ containers do not encode authoritative chapter boundaries in `ComicInfo.xml`; V17's EPUB spine is page-based rather than chapter-semantic.

Phase 0 therefore does **not** manufacture a chapter map through OCR or filename inference. Chapter boundaries and exact title-page locators will be frozen during each volume's Pass-A reconstruction from the visible table of contents and chapter pages.

This is deliberately more conservative than guessing structure from page position.
