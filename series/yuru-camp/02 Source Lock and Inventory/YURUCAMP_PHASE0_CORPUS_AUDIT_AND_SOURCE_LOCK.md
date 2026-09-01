---
title: "Yuru Camp Phase 0 — Corpus Audit and Source Lock"
series: "ゆるキャン△ / Yuru Camp△"
document_type: "phase_report"
phase: 0
method_version: "YURUCAMP_ANALYTICAL_METHOD_V1"
architecture_version: "YURUCAMP_MULTI_DOCUMENT_SYNTHESIS_ARCHITECTURE_V1"
status: "complete_with_known_gaps"
audit_date: "2026-08-14"
---

# Yuru Camp△ — Phase 0: Corpus Audit and Source Lock

## Executive result

**Phase 0 is complete for the corpus currently available.**

The source set is sufficiently stable to begin the sequential deep reading with Volume 1.

Current state:

- V01–V15: **locked current preferred sources**;
- V16: **locked with quality flag**;
- V17: **provisional lock**;
- V18: **pending / absent**;
- two Rurubu volumes: **locked supplementary paratext**.

The lock is deliberately mutable at the source-preference layer. It records exact hashes and provenance so that a later clean V16, higher-resolution V17, or newly supplied V18 can be introduced without contaminating prior analysis or destroying reproducibility.

## 1. Audit scope

Reviewed Drive source folder:

`1KlblbCFMPiR1WSwMLD2icnDT7Dhjzm-j`

Audited objects:

- 17 main manga volumes;
- 2 Rurubu travel-guide volumes;
- 19 total archive files.

Machine and visual checks performed:

- raw-file download from Drive;
- file-size confirmation;
- SHA-256 hashing;
- ZIP/EPUB CRC test;
- archive-member enumeration;
- image-count enumeration;
- image-decoding/verification;
- dominant image-dimension analysis;
- filename-sequence continuity;
- exact duplicate-image detection;
- `ComicInfo.xml` inspection for CBZs;
- EPUB container/OPF/manifest/spine inspection for V17;
- representative visual sampling across early, middle, and late pages;
- edge-page contact inspection for front/end matter preservation;
- targeted investigation of the V16 duplicate-image anomaly.

No OCR was used to manufacture missing metadata or chapter structure.

## 2. Integrity findings

### Archive integrity

**19/19 present archive files pass CRC testing.**

### Image integrity

- V01–V16: all archived images decode successfully.
- V17: dedicated second-pass verification confirms 167/167 image assets decode successfully.
- Both Rurubu guides: all archived AVIF images decode successfully.

### Numeric continuity

V01–V16 use continuous numeric image filenames with no missing numbers.

### Duplicate detection

V01–V15 and both Rurubu guides contain no exact duplicate image groups.

V16 contains one duplicate group:

- `0079.jpg`
- `0131.jpg`

Visual inspection establishes that both are the same third-party DL-Raw/RawLazy advertisement inserted at two separate boundaries. They are **not duplicated manga pages**.

## 3. Resolution/quality tiers

### Tier A — preferred working derivative

V02–V15 are predominantly 1350×1920 and structurally clean.

V01 is 1125×1600 but visually clean and sufficiently detailed.

### Tier B — usable with source contamination

V16 is 1125×1600 and readable, but sampled pages visibly carry `RawLazy.Si` / `DL-Raw.Se` marks, and two third-party advertisement pages are embedded in the sequence.

### Tier C — usable provisional source

V17 is a fixed-layout, image-based EPUB with 584×754 page images. It is fully readable in normal sampled dialogue but materially weaker for microtext and fine visual analysis.

## 4. V17 metadata findings

V17's OPF metadata identifies:

- title: `ゆるキャン△ １７巻`;
- creator: `あｆろ`;
- publisher: `芳文社`;
- ISBN identifier: `9784832296213`;
- calibre series index: 17.0.

The OPF incorrectly records `language=en`. This is a metadata defect only; the page images are Japanese.

The EPUB has:

- 166 reading-spine XHTML pages;
- 166 corresponding PNG page images;
- one additional `cover.jpg` asset.

## 5. Publication-completeness finding

External verification against Houbunsha's current catalogue on 2026-08-14 shows:

- latest tankōbon: **Volume 18**;
- V18 release date: **2025-11-12**.

Therefore:

> Present current-mainline completeness = **17/18 volumes**.

This is a known and explicitly documented gap, not an accidental omission.

## 6. Source-provenance finding

V01–V16 and the Rurubu guides contain derivative metadata stating that Japanese source images were assembled losslessly into CBZs and naming DLRAW.TO-derived source paths.

Accordingly, the project must say:

> **The Japanese manga pages are governing primary textual/visual evidence; the digital containers are unofficial derivatives.**

We have verified the integrity of the derivatives we possess, not their byte identity to a publisher-native Houbunsha digital edition.

This distinction applies to claims of archival completeness.

## 7. Publication-object preservation

Visual inspection of first/last page groups across V01–V17 confirms that the sources preserve more than story panels. They retain, in varying combinations:

- front covers;
- inside/front matter;
- color illustration/title/contents pages;
- manga body pages;
- end matter;
- colophon/publication pages;
- promotional/back-cover material.

This is suitable for the project's formal and paratextual method.

The analysis should not strip these materials out of the canonical archive.

## 8. Locator freeze

### V01–V16

Canonical raw-source locator:

> `VXX / NNNN.jpg / panel-region`

When visible, add printed page number as a secondary locator.

### V17

Canonical raw-source locator:

> `V17 / spine page NNN / NN_0.png / panel-region`

### V16 extraneous pages

`0079.jpg` and `0131.jpg` remain in raw-source numbering but are tagged:

> `EXTRANEOUS_SOURCE_INSERT`

They do not count as manga evidence.

## 9. Chapter-boundary policy

The containers do not provide authoritative chapter metadata.

Phase 0 therefore refuses to infer chapter boundaries by OCR, file-size change, or page-position heuristics.

Each volume's Pass-A reconstruction will identify:

- table-of-contents entries;
- chapter title pages;
- stable chapter-to-image ranges;
- omake/bonus boundaries;

from the visible source itself.

This becomes the chapter map used by later locators.

## 10. Rurubu lock and geography amendment

The two Rurubu volumes are suitable supplementary paratext and will be held outside the primary manga chain.

Future place analysis should explicitly classify evidence as:

- `MANGA_INTERNAL`
- `REAL_WORLD_GUIDE_CONTEXT`
- `FRANCHISE_TOURISM_FRAMING`

A real-world fact or franchise travel recommendation cannot be used to claim that the manga symbolically or thematically means the same thing.

## 11. What Phase 0 does not claim

Phase 0 does **not** establish:

- any character thesis;
- any relationship trajectory;
- any thematic thesis;
- any symbolic meaning of camping, landscape, food, or solitude;
- chapter-level interpretation;
- publisher-native completeness of derivative files;
- V18 coverage.

Its purpose is source control.

## 12. Gate decision

**Phase 1 may begin with Volume 1.**

No current source issue threatens V01–V15 analysis. V16 and V17 have explicit quality states that can be handled when reached. V18 can be added later without changing the prospective reading of earlier volumes.

The next architecture-defined artifact is:

> `YURUCAMP_V01_DEEP_READING.md`

using the governing rule:

> **Description first. Pattern second. Interpretation third. Theme last.**
