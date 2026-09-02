---
title: Classroom of the Elite — Year 1 Source Inventory
series: Classroom of the Elite
artifact_type: source_inventory
version: '1.7'
status: rolling_through_Y1V10_reconciled_cp03_reconciled_cp03
source_boundary: 'complete Year 1 source set: Y1V01–Y1V11.5 plus Y1FF'
analytical_completion_boundary: Y1V10
method: COTE_Y1_ANALYTICAL_METHOD_V2.md
created_at: '2026-08-11'
updated_at: '2026-08-12'
reconciliation_checkpoint: Y1-CP03 through Y1V10
---
# 『ようこそ実力至上主義の教室へ』
## Year 1 Source Inventory

This inventory records the complete Japanese Year 1 source set used by the second-pass corpus. All fourteen novels and *First File* are present as local EPUBs, open successfully as ZIP archives, and contain Japanese-language material. The source EPUBs are **not** included in the analytical delivery ZIP.

The exact EPUB SHA-256 is the governing source identity. A normalized-text fingerprint is added to the canonical inventory when each volume receives its deterministic second-pass extraction. Volumes 1–10 have completed deterministic extraction and canonical analysis. Checkpoint 01 freezes V01–V04.5; Checkpoint 02 freezes V05–V07.5; Checkpoint 03 freezes V08–V10. Volume 11 is the next sequential source.

| Code | Work | Status | Bytes | EPUB SHA-256 | Spine | Images | Analysis |
|---|---|---:|---:|---|---:|---:|---|
| `Y1V01` | 1 | `PASS` | 1,208,178 | `963cfa952f132284e6404a7e1cc41576cdb8ae90261d074cefbccbce493faa7a` | 44 | 25 | `complete` |
| `Y1V02` | 2 | `PASS` | 2,505,107 | `05c73d21b069e7b0bb65f683045148de9bf8501fae3578831727d05f2510e08a` | 46 | 25 | `complete` |
| `Y1V03` | 3 | `PASS` | 1,587,919 | `e47a65d4ccdbd170d9af9825960362bc47642479458b1893a6db582a4c40dcce` | 48 | 27 | `complete` |
| `Y1V04` | 4 | `PASS` | 1,750,747 | `2c5878c16c43024b2f88f93abe83813098e7d48e1834a389863b1b7f913da472` | 46 | 25 | `complete` |
| `Y1V04.5` | 4.5 | `PASS` | 1,162,326 | `172cfc8f46060668846fa6786cd83833a4b272f7504c36d08934e84331d96501` | 39 | 18 | `complete` |
| `Y1V05` | 5 | `PASS` | 1,575,532 | `083a6151a29c3efb6fdfe9de9a4e133975dd1d7aa6460e17510171db17b67abe` | 52 | 27 | `complete` |
| `Y1V06` | 6 | `PASS` | 2,617,264 | `fed319353078c3790fbe0348550642599e7003258b257b79a4f8354ab9ea5c12` | 22 | 35 | `complete` |
| `Y1V07` | 7 | `PASS` | 1,591,733 | `f36da0aafdef2e6f7789750754a65ff5bcf61c5479e48a1d07ca51b1a6eae097` | 47 | 29 | `complete` |
| `Y1V07.5` | 7.5 | `PASS` | 2,681,985 | `809b78ada556e4c1885d3ea3f856e784bebf6ad762491a0cd4f741e0f20d925a` | 21 | 23 | `complete` |
| `Y1V08` | 8 | `PASS` | 2,547,746 | `70fe11cf8145e97fcf17ea817f326d43ac0fe213b6ffeec7ee532acbd83ebb8e` | 24 | 23 | `complete` |
| `Y1V09` | 9 | `PASS` | 2,093,540 | `0f615a16f03db32930f0a24ba41778fff30d5b1d8a4d21df625757fae576eaca` | 24 | 24 | `complete` |
| `Y1V10` | 10 | `PASS` | 2,374,182 | `2b3b83b5281ef7bdeb320bb9d0c24f58b67be044fda02724c3683b32fdc4d1e5` | 23 | 23 | `complete` |
| `Y1V11` | 11 | `PASS` | 2,605,011 | `a067284074b9209c4712b41d05ce01da17c971bc6d7993afb07cd548524a0a9f` | 26 | 24 | `planned` |
| `Y1V11.5` | 11.5 | `PASS` | 2,537,841 | `c5078e3770b0a74b161070920d65a91c681d8d54905477d15434bb05f5848fde` | 23 | 23 | `planned` |
| `Y1FF` | First File | `PASS` | 121,638,502 | `b0b95aea1a832f6492c6e6b40faf19a277a3c4435fef3fe0859947e6fe8a45b1` | 253 | 247 | `planned` |

## Audit notes

- The fourteen numbered/decimal novels were previously subjected to ZIP/CRC, OPF/manifest, spine, navigation, XHTML, image, language-identity, and internal-reference checks; all passed.
- *First File* is structurally unusual because it is image-heavy: 253 spine items and 247 image resources. Its extracted text is Japanese, and its archive passes CRC validation.
- Some EPUBs do not expose a conventional NCX table of contents. That is a packaging/navigation difference, not evidence of missing narrative text; chapter mapping will be reconstructed from the spine and internal headings during each canonical reread.
- The normalized-text hash is optional under the governing method. It becomes canonical only after the volume-specific deterministic extraction is frozen.

## Current source-processing state

| Code | Normalized-text SHA-256 | Locator status |
|---|---|---|
| `Y1V01` | `b7790d5814009e62c824bd1cfe0b594a54b61028f9ceb75dde6cc425c3de35e1` | canonical `epub-spine-xhtml-paragraph-anchor-v1` |
| `Y1V02` | `6f03469cadda251d81b47b2c03f010cdf2097fc81f126ec2e34a1a1253de0d7c` | canonical `epub-spine-xhtml-paragraph-anchor-v1`; 3,967 normalized paragraphs / 144,825 Japanese characters |
| `Y1V03` | `457e373660a3e3b72d0c268dedf86d288085ad690800799129c126bc70d62dfb` | canonical `epub-spine-xhtml-paragraph-anchor-v1`; 3,790 normalized paragraphs / 157,261 Japanese characters |
| `Y1V04` | `a4d3164c8f08bf1c331c4fee9eafffbdf14bb8b135a4bdb2b5477ea27b9fbf55` | canonical `epub-spine-xhtml-paragraph-anchor-v1`; 3,409 normalized paragraphs / 161,157 Japanese characters |
| `Y1V04.5` | `709cdc0b3d40a9a6a9a901b4422c6eb955fb26e4e2596123474f642628655820` | canonical `epub-spine-xhtml-paragraph-anchor-v1`; 3,681 normalized paragraphs / 140,842 Japanese characters |
| `Y1V05` | `a1af41937668e9a78541426dedabd4e5b1308d9acdc80e6860db8fbb9dbd6d3a` | canonical `epub-spine-xhtml-paragraph-anchor-v1`; 3,603 normalized paragraphs / 145,015 Japanese characters |
| `Y1V06` | `684c46f94745ab37881e3f62034e9b29307e5f2b4291376376e3eb18581078dc` | canonical `epub-spine-xhtml-paragraph-anchor-v1`; 3,620 normalized paragraphs / 150,989 Japanese characters |
| `Y1V07` | `82247b695ae062dcb154d75330c4bf93a2a3c6f2b1fa69bdb26b23ef5e020d1a` | canonical `epub-spine-xhtml-paragraph-anchor-v1`; 4,031 normalized paragraphs / 133,528 Japanese characters |
| `Y1V07.5` | `61246a54758030821a292588fbbc71a54e5d062dbfdaefb0fa69f9b6fc286e3d` | canonical `epub-spine-xhtml-paragraph-anchor-v1`; 3,820 normalized paragraphs / 124,881 Japanese characters |
| `Y1V08` | `a67725eb41238b1878ef4a2795fd91fc93fa2367d9374bae3af9bccc5f98df8a` | canonical `epub-spine-xhtml-paragraph-anchor-v1`; 3,683 normalized paragraphs / 145,448 Japanese characters |
| `Y1V09` | `1fe037048c9cf5869dd7c387fe81ef7ba0f26dedb4b5579dd6e38bd22317b42c` | canonical `epub-spine-xhtml-paragraph-anchor-v1`; 3,554 normalized paragraphs / 111,176 Japanese characters |
| `Y1V10–Y1FF` | pending canonical volume extraction | source identity verified; locators pending |

## Detailed source map

The metadata-only source map, including detailed deterministic maps where frozen and canonical normalized fingerprints through Volume 9, is stored at [`support/COTE_Y1_SOURCE_MAP.json`](../04%20Source%20Maps%20and%20Support/COTE_Y1_SOURCE_MAP.json).


## Locator-index convention through Checkpoint 01

The frozen volume artifacts do not all share the same historical spine-number base. `Y1V01–Y1V04` use zero-based spine locators; `Y1V04.5` uses one-based spine locators. `support/COTE_Y1_SOURCE_MAP.json` uses one-based `spine_index` values and records the required per-source offset, allowing all 275 evidence locators to validate without rewriting immutable earlier artifacts.

The explicit Volume 4.5 artifact recovery record is stored at [`support/COTE_Y1_V04_5_RECOVERY_NOTE.md`](../04%20Source%20Maps%20and%20Support/COTE_Y1_V04_5_RECOVERY_NOTE.md).

## Volume 3 source-specific notes

- Internal title: `ようこそ実力至上主義の教室へ 3 <ようこそ実力至上主義の教室へ> (MF文庫J)`.
- Original EPUB SHA-256: `e47a65d4ccdbd170d9af9825960362bc47642479458b1893a6db582a4c40dcce`.
- Frozen normalized-text SHA-256: `457e373660a3e3b72d0c268dedf86d288085ad690800799129c126bc70d62dfb`.
- Deterministic extraction: **3,790 substantive paragraphs / 157,261 normalized Japanese characters** across 48 spine items.
- The archive exposes 27 image-like resources in the broad source audit; the volume-specific raster inventory contains 26 raster resources, including four color front-matter illustrations, ten narrative illustrations, six dossier/database inserts, title/TOC/branding material, and a gaiji resource.
- One inline gaiji supplies the rare initial kanji in `葛城`; normalized extraction may visually reduce the name to `城` at that location. Raw XHTML/ruby verifies `葛城康平`. The canonical prose analysis therefore uses the verified full name and records the extraction caveat rather than treating it as a textual variant.


## Volume 4 source-specific notes

- Internal title: `ようこそ実力至上主義の教室へ 4 <ようこそ実力至上主義の教室へ> (MF文庫J)`.
- Original EPUB SHA-256: `2c5878c16c43024b2f88f93abe83813098e7d48e1834a389863b1b7f913da472`.
- Frozen normalized-text SHA-256: `a4d3164c8f08bf1c331c4fee9eafffbdf14bb8b135a4bdb2b5477ea27b9fbf55`.
- Deterministic extraction: **3,409 substantive paragraphs / 161,157 normalized Japanese characters** across 46 spine items.
- The volume-specific visual inventory contains 25 raster resources: four color front-matter illustrations, four student-database inserts, ten monochrome narrative illustrations, two bonus manga pages, and title/contents/branding resources.
- The canonical artifact preserves a strict Volume 4 endpoint and records Hirata's report of Kei's history as local character testimony rather than silently correcting it with later-year information.

## Volume 4.5 source-specific notes

- Internal title: `ようこそ実力至上主義の教室へ 4.5 <ようこそ実力至上主義の教室へ> (MF文庫J)`.
- Original EPUB SHA-256: `172cfc8f46060668846fa6786cd83833a4b272f7504c36d08934e84331d96501`.
- Frozen normalized-text SHA-256: `709cdc0b3d40a9a6a9a901b4422c6eb955fb26e4e2596123474f642628655820`.
- Deterministic extraction: **3,681 substantive paragraphs / 140,842 normalized Japanese characters** across 39 spine items.
- Broad source audit records 18 image resources; the volume-specific raster working inventory contains 17 raster resources after excluding non-raster/packaging distinctions.
- The volume is treated as core narrative evidence, not optional side material. Its vignette architecture is especially important for ordinary life, social voice, privacy, friendship, interdependence, and the ethical comparison between low-coercion support and covert control.




## Checkpoint 01 provenance repair

The reconciliation audit detected that the active `Y1V04.5` Markdown path had been replaced accidentally by a compatibility pointer after its original delivery. The analytical source layer—Japanese EPUB, frozen normalized text, 68 evidence entries, terminology index, revision audit, and cumulative delta—remained intact. A versioned v1.1 canonical artifact was reconstructed explicitly from those verified materials. Its recovery status and the original v1.0 SHA-256 are recorded in the artifact front matter; no primary-source identity changed.


## Volume 5 source-specific notes

- Internal title: `ようこそ実力至上主義の教室へ 5 <ようこそ実力至上主義の教室へ> (MF文庫J)`.
- Original EPUB SHA-256: `083a6151a29c3efb6fdfe9de9a4e133975dd1d7aa6460e17510171db17b67abe`.
- Frozen normalized-text SHA-256: `a1af41937668e9a78541426dedabd4e5b1308d9acdc80e6860db8fbb9dbd6d3a`.
- Deterministic extraction: **3,603 substantive paragraphs / 145,015 normalized Japanese characters** across 52 spine items.
- The broad source audit records 27 image-like resources. The volume-specific raster working inventory contains 26 extracted raster files; the difference is a packaging/resource-classification distinction and does not indicate missing narrative content.
- Volume 5 uses one-based artifact spine locators, matching the one-based source-map spine index; locator offset is therefore `0`.


## Volume 7 source-specific notes

- Internal title: `ようこそ実力至上主義の教室へ 7 <ようこそ実力至上主義の教室へ> (MF文庫J)`.
- Original EPUB SHA-256: `f36da0aafdef2e6f7789750754a65ff5bcf61c5479e48a1d07ca51b1a6eae097`.
- Frozen normalized-text SHA-256: `82247b695ae062dcb154d75330c4bf93a2a3c6f2b1fa69bdb26b23ef5e020d1a`.
- Deterministic extraction: **4,031 substantive paragraphs / 133,528 normalized Japanese characters** across 47 spine items.
- Broad source audit records 29 raster resources. The narrative inventory includes the Hiyori library scene, Atsuomi, Chabashira, Sakayanagi/Kamuro, Kōenji, Kei's rooftop ordeal, Ryūen's fear, and Ayanokōji's procedural violence.
- Volume 7 uses zero-based artifact spine locators, matching the frozen extraction in `work/Y1V07/source_info.json`; locator offset is `0`.


## Volume 7.5 source-specific notes

- Internal title: `ようこそ実力至上主義の教室へ 7.5 (MF文庫J)`.
- Original EPUB SHA-256: `809b78ada556e4c1885d3ea3f856e784bebf6ad762491a0cd4f741e0f20d925a`.
- Frozen normalized-text SHA-256: `61246a54758030821a292588fbbc71a54e5d062dbfdaefb0fa69f9b6fc286e3d`.
- Deterministic extraction: **3,820 substantive paragraphs / 124,881 normalized Japanese characters** across 21 spine items.
- The volume contains 23 raster resources. Narrative and editorial images foreground Kei, Satō, Ibuki, Horikita/Kushida, Airi, Ryūen, and Ayanokōji's winter isolation.
- The artifact uses zero-based spine indices matching the frozen extraction.


## Volume 8 source-specific notes

- Original EPUB SHA-256: `70fe11cf8145e97fcf17ea817f326d43ac0fe213b6ffeec7ee532acbd83ebb8e`.
- Frozen normalized-text SHA-256: `a67725eb41238b1878ef4a2795fd91fc93fa2367d9374bae3af9bccc5f98df8a`.
- Deterministic extraction: **3,683 substantive paragraphs / 145,448 normalized Japanese characters** across 24 spine items.
- Canonical analysis: `volumes/COTE_Y1_V08_DEEP_READING.md`.

## Volume 9 source-specific notes

- Original EPUB SHA-256: `0f615a16f03db32930f0a24ba41778fff30d5b1d8a4d21df625757fae576eaca`.
- Frozen normalized-text SHA-256: `1fe037048c9cf5869dd7c387fe81ef7ba0f26dedb4b5579dd6e38bd22317b42c`.
- Deterministic extraction: **3,554 substantive paragraphs / 111,176 normalized Japanese characters** across 24 spine items.
- Canonical analysis: `volumes/COTE_Y1_V09_DEEP_READING.md`.
- The EPUB uses raster gaiji for several rare kanji. The deterministic normalized layer records those positions explicitly as `[GAIJI:...]` rather than guessing characters from context; exact-name verification can therefore return to the raw XHTML/ruby when necessary.


## Volume 10 source-specific notes

- Internal title: `ようこそ実力至上主義の教室へ 10 (MF文庫J)`.
- Original EPUB SHA-256: `2b3b83b5281ef7bdeb320bb9d0c24f58b67be044fda02724c3683b32fdc4d1e5`.
- Frozen normalized-text SHA-256: `8c1d43dde96ffa772361b7d9c399ddda9321ff2019c8a379caa4ceed8c751d8c`.
- Deterministic extraction: **4,606 substantive paragraphs / 140,731 normalized Japanese characters** across 23 spine items.
- The EPUB contains 23 raster resources.
- The canonical artifact and source audit use one-based spine indices; no locator offset is required.
- Canonical analysis: `volumes/COTE_Y1_V10_DEEP_READING.md`.
