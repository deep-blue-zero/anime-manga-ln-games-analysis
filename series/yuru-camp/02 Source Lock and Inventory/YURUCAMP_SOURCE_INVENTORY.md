---
title: "Yuru Camp Source Inventory — Phase 0"
series: "ゆるキャン△ / Yuru Camp△"
document_type: "source_inventory"
phase: 0
status: "locked_with_known_gaps"
audit_date: "2026-08-14"
source_folder_drive_id: "1KlblbCFMPiR1WSwMLD2icnDT7Dhjzm-j"
---

# Yuru Camp△ Source Inventory — Phase 0

## Corpus state

The reviewed Drive source directory contains **19 files**:

- **17 main-manga volumes, V01–V17**;
- **2 Japanese Rurubu travel-guide volumes**.

The official Houbunsha catalogue was checked on 2026-08-14 and lists **Volume 18** as the latest tankōbon, released 2025-11-12. The present main-manga corpus is therefore **17/18 volumes complete by current tankōbon count**. V18 is not present in the reviewed directory.

All present archives passed ZIP/EPUB CRC testing. Every present manga image in V01–V16 decoded successfully. A dedicated corrected verification pass confirmed that **167/167 V17 image assets decode successfully**; its reading spine contains 166 page wrappers plus a separate cover asset.

**Important provenance limit:** V01–V16 and both Rurubu guides are derivative containers assembled from Japanese page images. Their embedded `ComicInfo.xml` explicitly identifies them as non-destructive derivatives and names DLRAW.TO-derived source paths. They are appropriate as high-fidelity Japanese textual/visual evidence for this project, but they are **not publisher-native archival masters**. Internal completeness is verified; publisher-native byte/page identity is not.

## Main manga

| Vol. | File | Container | Size MiB | Reading/page images | Dominant dimensions | CRC | Image decode | Lock status | Quality note |
|---:|---|---|---:|---:|---|---|---|---|---|

| 01 | `Laid-Back Camp - Vol. 01 [Japanese].cbz` | CBZ | 97.7 | 182 | 1125×1600 | PASS | PASS | `LOCKED_CURRENT_PREFERRED` | Good derivative |
| 02 | `Laid-Back Camp - Vol. 02 [Japanese].cbz` | CBZ | 136.7 | 182 | 1350×1920 | PASS | PASS | `LOCKED_CURRENT_PREFERRED` | Good derivative |
| 03 | `Laid-Back Camp - Vol. 03 [Japanese].cbz` | CBZ | 120.5 | 182 | 1350×1920 | PASS | PASS | `LOCKED_CURRENT_PREFERRED` | Good derivative |
| 04 | `Laid-Back Camp - Vol. 04 [Japanese].cbz` | CBZ | 119.2 | 182 | 1350×1920 | PASS | PASS | `LOCKED_CURRENT_PREFERRED` | Good derivative |
| 05 | `Laid-Back Camp - Vol. 05 [Japanese].cbz` | CBZ | 119.8 | 182 | 1350×1920 | PASS | PASS | `LOCKED_CURRENT_PREFERRED` | Good derivative |
| 06 | `Laid-Back Camp - Vol. 06 [Japanese].cbz` | CBZ | 105.0 | 184 | 1350×1920 | PASS | PASS | `LOCKED_CURRENT_PREFERRED` | Good derivative |
| 07 | `Laid-Back Camp - Vol. 07 [Japanese].cbz` | CBZ | 109.9 | 183 | 1350×1920 | PASS | PASS | `LOCKED_CURRENT_PREFERRED` | Good derivative |
| 08 | `Laid-Back Camp - Vol. 08 [Japanese].cbz` | CBZ | 116.8 | 184 | 1350×1920 | PASS | PASS | `LOCKED_CURRENT_PREFERRED` | Good derivative |
| 09 | `Laid-Back Camp - Vol. 09 [Japanese].cbz` | CBZ | 104.1 | 183 | 1350×1920 | PASS | PASS | `LOCKED_CURRENT_PREFERRED` | Good derivative |
| 10 | `Laid-Back Camp - Vol. 10 [Japanese].cbz` | CBZ | 100.2 | 183 | 1350×1920 | PASS | PASS | `LOCKED_CURRENT_PREFERRED` | Good derivative |
| 11 | `Laid-Back Camp - Vol. 11 [Japanese].cbz` | CBZ | 104.7 | 182 | 1350×1920 | PASS | PASS | `LOCKED_CURRENT_PREFERRED` | Good derivative |
| 12 | `Laid-Back Camp - Vol. 12 [Japanese].cbz` | CBZ | 92.2 | 182 | 1350×1920 | PASS | PASS | `LOCKED_CURRENT_PREFERRED` | Good derivative |
| 13 | `Laid-Back Camp - Vol. 13 [Japanese].cbz` | CBZ | 58.9 | 182 | 1350×1920 (+1 minor variant[s]) | PASS | PASS | `LOCKED_CURRENT_PREFERRED` | Good derivative |
| 14 | `Laid-Back Camp - Vol. 14 [Japanese].cbz` | CBZ | 82.9 | 183 | 1350×1920 (+1 minor variant[s]) | PASS | PASS | `LOCKED_CURRENT_PREFERRED` | Good derivative |
| 15 | `Laid-Back Camp - Vol. 15 [Japanese].cbz` | CBZ | 78.4 | 166 | 1350×1920 (+1 minor variant[s]) | PASS | PASS | `LOCKED_CURRENT_PREFERRED` | Good derivative |
| 16 | `Laid-Back Camp - Vol. 16 [Japanese].cbz` | CBZ | 51.2 | 168 | 1125×1600 | PASS | PASS | `LOCKED_WITH_QUALITY_FLAG` | Readable; 1125×1600; RawLazy/DL-Raw watermarks; two extraneous repeated ad inserts |
| 17 | `Laid-Back Camp - Vol. 17 [Japanese].epub` | EPUB | 70.7 | 166 spine / 167 assets | 584×754 | PASS | PASS | `PROVISIONAL_LOCK` | Readable fixed-layout image EPUB; 584×754; incorrect `language=en` metadata; replacement preferred |
| 18 | **MISSING** | — | — | — | — | — | — | `PENDING` | Current known corpus gap |

## Supplementary paratext

| File | Role | Size MiB | Images | Dimensions | Internal format | CRC | Lock status |
|---|---|---:|---:|---|---|---|---|

| `Laid-Back Camp - Rurubu Travel Guide - Season 2 [Japanese].cbz` | Travel/geography franchise paratext | 47.6 | 98 | 1569×1920 | .avif:98 | PASS | `LOCKED_SUPPLEMENTARY` |
| `Laid-Back Camp - Rurubu Travel Guide [Japanese].cbz` | Travel/geography franchise paratext | 45.2 | 102 | 1569×1920 | .avif:102 | PASS | `LOCKED_SUPPLEMENTARY` |

## Exact source hashes

The authoritative hashes are stored in `YURUCAMP_SOURCE_CHECKSUMS.sha256`. They lock the exact source objects used for any future analysis and make later controlled replacement of V16/V17 possible without erasing provenance.

## Source-role policy

### Governing primary evidence

The Japanese manga page images govern claims about:

- dialogue and wording;
- character behavior;
- relationship development;
- panel composition;
- pacing;
- visual detail;
- page order;
- practical camping depiction.

### Supplementary evidence

The Rurubu guides are not permitted to override the manga. They may later be used to distinguish:

1. manga-internal geographic representation;
2. real-world travel/camping information;
3. franchise tourism framing.

Those layers must remain separate in the Place / Geography / Travel ledger.

## Phase-0 lock decision

- **V01–V15:** locked as current preferred working sources.
- **V16:** locked with a quality flag; analysis may proceed, but a clean replacement would be welcome.
- **V17:** provisionally locked; analysis may proceed if necessary, but a higher-resolution source should supersede it when obtained.
- **V18:** pending and absent.
- **Rurubu guides:** locked as supplementary paratext.

This lock records what the project used; it is not an immutable final-release lock.
