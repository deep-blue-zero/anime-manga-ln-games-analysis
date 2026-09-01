---
series: IMOSAE
artifact_type: source_inventory
scope: V01-V14_Japanese_numbered_light_novels
generation: V1
status: canonical
source_boundary: "Japanese numbered light novel EPUBs V01-V14 staged 2026-08-18; supplemental sources excluded"
supersedes: null
superseded_by: null
do_not_use_as_current_authority: false
source_set_id: IMOSAE-JP-LN-RAW-1.0
version: "1.0"
date: "2026-08-18"
---

# IMOSAE Source Inventory
## 『妹さえいればいい。』 / *A Sister's All You Need* — Japanese Main-Series Corpus

## 1. Inventory purpose

This document is the canonical human-readable inventory for the raw Japanese numbered light-novel corpus. It establishes exactly which files belong to the project, records their bibliographic and package properties, and separates raw-source facts from later normalized-reading artifacts.

The locked raw source-set identifier is **`IMOSAE-JP-LN-RAW-1.0`**. This identifier refers only to the fourteen original uploaded EPUB files listed below. It does **not** include extracted text, converted EPUBs, translations, adaptations, drama CDs, retailer short stories, or later supplemental material.

The accompanying machine-readable record is `machine_readable/source_manifest.json`; exact source hashes are also emitted as `machine_readable/checksums.sha256`.

## 2. Corpus-level findings

- **Numbered main-series coverage:** 14/14 volumes, V01–V14.
- **Total raw size:** 222,679,906 bytes (212.36 MiB).
- **Exact duplicate files:** 0.
- **Archive integrity:** 14/14 PASS under the supplied audit and independently revalidated by ZIP CRC testing.
- **Hash verification:** SHA-256 independently recalculated for all fourteen files; all values match `epub_audit.json`.
- **Language:** Japanese throughout the substantive reading corpus; package metadata and sampled body text agree.
- **Extracted body-text scale:** approximately 1,397,830 characters across 340 substantive spine documents.
- **Package structure:** 10 EPUB 3 packages and 4 EPUB 2 packages.
- **Spine items:** 981 total.
- **Ruby:** 29,083 `<ruby>` constructions detected directly in XHTML.
- **Inline gaiji/special-symbol images:** 651 occurrences, representing **65 distinct image hashes across the full set**. This direct census supersedes the earlier preliminary estimate of 57 distinct assets.
- **Raster-image assets:** 666 total; 552 meet the project's provisional large-page-image threshold (long edge ≥900 px and short edge ≥500 px). All raster assets in this pass decoded successfully.

These findings make the corpus suitable for Japanese prose, dialogue/idiolect, typography, illustration/paratext, and longitudinal full-series analysis. The remaining Phase-0 work concerns **normalization and stable locators**, not replacement of defective primary sources.

## 3. Volume inventory

| Vol. | Base edition | Ebook edition | ISBN | EPUB / nav | Spine | Text chars | Ruby | Gaiji occ. / distinct | Raster / large | Raw MiB | Result |
|---:|---|---|---|---|---:|---:|---:|---:|---:|---:|---|
| V01 | 2015-03-23 | 2015-03-27 | `978-4-09-451507-7` | 3.0 / EPUB3 nav | 68 | 108,233 | 2,081 | 76 / 14 | 51 / 37 | 16.73 | PASS |
| V02 | 2015-07-22 | 2015-07-31 | `978-4-09-451560-2` | 3.0 / EPUB3 nav | 59 | 103,484 | 1,949 | 58 / 23 | 53 / 29 | 12.54 | PASS |
| V03 | 2015-11-23 | 2015-11-27 | `978-4-09-451580-0` | 3.0 / EPUB3 nav | 56 | 89,404 | 1,811 | 30 / 2 | 31 / 29 | 11.55 | PASS |
| V04 | 2016-03-23 | 2016-03-25 | `978-4-09-451598-5` | 2.0 / EPUB2 NCX | 62 | 110,648 | 2,781 | 42 / 12 | 43 / 31 | 3.65 | PASS |
| V05 | 2016-07-25 | 2016-07-29 | `978-4-09-451618-0` | 3.0 / EPUB3 nav | 59 | 94,075 | 2,231 | 28 / 8 | 38 / 30 | 8.64 | PASS |
| V06 | 2016-12-25 | 2016-12-28 | `978-4-09-451646-3` | 3.0 / EPUB3 nav | 67 | 96,666 | 2,157 | 70 / 8 | 44 / 36 | 14.67 | PASS |
| V07 | 2017-05-23 | 2017-05-26 | `978-4-09-451677-7` | 3.0 / EPUB3 nav | 68 | 101,599 | 2,172 | 31 / 5 | 44 / 39 | 18.39 | PASS |
| V08 | 2017-09-25 | 2017-09-29 | `978-4-09-451697-5` | 3.0 / EPUB3 nav | 93 | 89,807 | 1,677 | 32 / 2 | 62 / 59 | 33.81 | PASS |
| V09 | 2018-02-25 | 2018-02-23 | `978-4-09-451719-4` | 3.0 / EPUB3 nav | 100 | 98,175 | 2,005 | 118 / 8 | 67 / 59 | 29.96 | PASS |
| V10 | 2018-07-23 | 2018-07-27 | `978-4-09-451742-2` | 3.0 / EPUB3 nav | 67 | 91,670 | 1,750 | 23 / 1 | 40 / 39 | 19.97 | PASS |
| V11 | 2018-12-23 | 2018-12-28 | `978-4-09-451765-1` | 3.0 / EPUB3 nav | 75 | 88,866 | 1,826 | 19 / 3 | 57 / 50 | 27.10 | PASS |
| V12 | 2019-04-23 | 2019-04-18 | `978-4-09-451782-8` | 2.0 / EPUB2 NCX | 73 | 99,194 | 2,140 | 34 / 7 | 46 / 38 | 5.08 | PASS |
| V13 | 2019-09-23 | 2019-09-18 | `978-4-09-451808-5` | 2.0 / EPUB2 NCX | 73 | 120,697 | 2,320 | 44 / 4 | 48 / 43 | 5.48 | PASS |
| V14 | 2020-02-23 | 2020-02-18 | `978-4-09-451828-3` | 2.0 / EPUB2 NCX | 61 | 105,312 | 2,183 | 46 / 7 | 42 / 33 | 4.80 | PASS |

### Bibliographic authority rule

The **colophon is authoritative for project bibliography** when it conflicts with embedded OPF metadata. Package metadata is retained as provenance but is not used to establish original publication sequence.

This matters because the packages are heterogeneous conversions. For example, V03's embedded `dc:date` reports `2017-05-19`, while its colophon identifies the base edition as **2015-11-23** and the ebook edition as **2015-11-27**. V05, V07, and V08 omit `dc:date` entirely. The colophons recover coherent edition dates and ISBNs for all fourteen volumes.

## 4. Exact raw-file identities

| Vol. | Filename | Bytes | SHA-256 | OPF path |
|---:|---|---:|---|---|
| V01 | `A Sister's All You Need - Volume 01 [Japanese].epub` | 17,543,612 | `73d79276ea950d82d3338ab93b023473676855b9cc3759b32899d88f87cdca9b` | `OEBPS/content.opf` |
| V02 | `A Sister's All You Need - Volume 02 [Japanese].epub` | 13,148,865 | `5f942c7d2e1c14bbb0a55b81257e95dc776b70c28f872633084a93693a2488ff` | `OEBPS/content.opf` |
| V03 | `A Sister's All You Need - Volume 03 [Japanese].epub` | 12,108,933 | `edc655a6b440f7ee927cfc8ef09d72c5a8b950800dacf5d2ddff6e2e54c3b9d3` | `OEBPS/content.opf` |
| V04 | `A Sister's All You Need - Volume 04 [Japanese].epub` | 3,829,274 | `e753b87bd220f78575e43a89a1b9646c0cf2985d740805e9fe4822d9ef52e674` | `content.opf` |
| V05 | `A Sister's All You Need - Volume 05 [Japanese].epub` | 9,055,624 | `7f46b0c0f96dfed933fa46cbd1f4bab9d80b74808bdf566f0416f7a7b1c3af53` | `OEBPS/content.opf` |
| V06 | `A Sister's All You Need - Volume 06 [Japanese].epub` | 15,384,271 | `3c7e5338586227512ed16f9f9af7d31f3076403f3962b3e4f8945909c6dc5e9a` | `OEBPS/content.opf` |
| V07 | `A Sister's All You Need - Volume 07 [Japanese].epub` | 19,282,376 | `75f8f9f8cf6ba3bb58f395506280aeb0e5c54593c4bbe9248b3ecf6e115c8566` | `OEBPS/content.opf` |
| V08 | `A Sister's All You Need - Volume 08 [Japanese].epub` | 35,450,423 | `caec6062f4a5649762edbf3f2eb2265c99a8be7e4d54f03b6c0aae1cd19569f9` | `OEBPS/content.opf` |
| V09 | `A Sister's All You Need - Volume 09 [Japanese].epub` | 31,412,256 | `25661b4807c64202f6febc1c69646d09900b25e3281f8928b75d2d070a378cfd` | `OEBPS/content.opf` |
| V10 | `A Sister's All You Need - Volume 10 [Japanese].epub` | 20,944,508 | `69440a509c1aee946857b52994b1eab96a59bf7ecbb18a7da6bbf02253f5c06a` | `OEBPS/content.opf` |
| V11 | `A Sister's All You Need - Volume 11 [Japanese].epub` | 28,415,419 | `ae1f5cba5fca191e8d27a17658e7679567bc4018cde347001c84ef5a43f5f5d7` | `OEBPS/content.opf` |
| V12 | `A Sister's All You Need - Volume 12 [Japanese].epub` | 5,327,450 | `fbf988f8620b09d476a3d993ab6f931f6dc2db6fabb1cec8afd985c98c635e7f` | `content.opf` |
| V13 | `A Sister's All You Need - Volume 13 [Japanese].epub` | 5,741,368 | `70c62c02d882a8f7ada21657a03c0521ca1092bbbdc6e5e5d23e317419224737` | `content.opf` |
| V14 | `A Sister's All You Need - Volume 14 [Japanese].epub` | 5,035,527 | `86dd3d6ae2196f1255b9266003e0b6337ee5011e0d11d0a4d2afe25791d31fd5` | `content.opf` |

## 5. Packaging heterogeneity

The corpus contains multiple retail/conversion generations. This is not an analytical defect, but the normalization pipeline must not assume identical internal paths or navigation technology.

- **EPUB 3 / nav:** V01–V03 and V05–V11.
- **EPUB 2 / NCX:** V04 and V12–V14.
- OPF locations vary between `OEBPS/content.opf` and root-level `content.opf`.
- XHTML naming varies (`p-XXXX.xhtml[.xhtml]` versus `text/partXXXX.html`).

Therefore locators must be generated from each volume's actual package/spine rather than from a hard-coded path template.

## 6. Native-text quality and linguistic value

The body prose is native Unicode Japanese rather than OCR-derived text. Direct XHTML inspection found no UTF-8 replacement-character corruption in the literary text. The sources preserve dialogue punctuation, paragraph boundaries, ruby, and presentational markup well enough for close Japanese reading.

Ruby must be preserved as structured annotation rather than flattened into duplicated text. The canonical normalized reading stream should retain the base orthography while exposing the reading in a sidecar field or inline structured representation when analytically needed.

The volume-by-volume ruby counts above are not themselves literary measurements; they are ingestion facts that demonstrate why a ruby-aware extraction layer is required.

## 7. Gaiji and special-symbol findings

The EPUBs use inline image glyphs (`gaiji`) inside otherwise textual prose. A generic HTML-to-text conversion can silently delete them. The current direct corpus census finds **651 inline gaiji occurrences and 65 distinct underlying image hashes**.

The earlier readiness note estimated 632 occurrences / 57 unique assets from a narrower preliminary scan. The present inventory uses a complete package-level census and **supersedes that preliminary count** for Phase 0.

No literary normalization should replace these glyphs by guess. The next dedicated artifact, `IMOSAE_GAIJI_AND_TEXT_NORMALIZATION_REGISTER.md`, must assign stable IDs, resolve high-confidence glyphs, preserve uncertain symbols explicitly, and record context/evidence for every distinct asset.

## 8. Illustration and paratext findings

The source set contains **666 raster-image assets**, of which **552** meet the provisional large-page-image threshold used in this audit. This total includes covers, illustrations, gaiji, promotional graphics, and other package images; it is not equivalent to a count of unique story illustrations.

Illustrations are preserved at sufficient resolution for later visual/paratext analysis. A dedicated `IMOSAE_ILLUSTRATION_AND_PARATEXT_INVENTORY.md` should classify each image by role and anchor narrative illustrations to the surrounding prose before sequential deep reading begins.

## 9. Content-boundary policy

Every spine item must be classified before the normalized reading layer is frozen. Required content classes from the governing analytical method are:

- `MAIN_NARRATIVE`
- `BONUS_FICTION`
- `AUTHOR_AFTERWORD`
- `ILLUSTRATION`
- `TITLE_FRONTMATTER`
- `COLOPHON`
- `PROMOTIONAL`
- `RETAILER_EBOOK_BONUS`
- `OTHER_PARATEXT`

This is essential because the EPUBs include publication material such as afterwords, colophons, digital bonuses, promotional pages, and in some cases material such as `ガガガ文庫PR`. None of those should silently become main-narrative evidence.

## 10. Provenance inputs

This inventory was built from three evidence layers:

1. the supplied `epub_audit.json`;
2. the supplied `MANIFEST(20260818-040407).md`;
3. direct re-reading of the fourteen uploaded EPUB packages on 2026-08-18, including fresh SHA-256 calculation, ZIP CRC validation, OPF/package inspection, colophon extraction, ruby/gaiji census, and image decoding/dimension inspection.

Where the preliminary manifest and fresh direct inspection differ, this document records the fresh direct inspection and calls out the difference explicitly.

## 11. Source-readiness conclusion

**Raw-source readiness: PASS.** The fourteen Japanese EPUBs are complete for the numbered main series, internally readable, hash-stable, unencrypted, structurally navigable, and suitable for archival literary analysis.

**Normalized-reading readiness: NOT YET FROZEN.** Before `IMOSAE_V01_DEEP_READING.md` becomes canonical, Phase 0 must still complete gaiji normalization, spine-item classification, typography-aware extraction, stable paragraph locators, illustration anchors, and round-trip validation.

## 12. Next artifact

The next authority artifact is `IMOSAE_SOURCE_LOCK.md`, which freezes the raw set defined here and specifies what may and may not be changed without creating a new source-set generation.
