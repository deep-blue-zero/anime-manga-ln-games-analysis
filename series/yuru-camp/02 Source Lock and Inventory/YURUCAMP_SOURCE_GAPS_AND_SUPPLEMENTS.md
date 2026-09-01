---
title: "Yuru Camp Source Gaps and Supplements — Phase 0"
series: "ゆるキャン△ / Yuru Camp△"
document_type: "source_gaps_supplements"
phase: 0
status: "active"
---

# Yuru Camp△ Source Gaps and Supplements — Phase 0

## 1. Current mainline gap: Volume 18

The reviewed source folder contains V01–V17. Houbunsha's current catalogue, checked 2026-08-14, lists **Volume 18** as the latest tankōbon and gives a release date of **2025-11-12**.

V18 is therefore a known corpus gap.

**Effect on project:**

- does not block Phase 0;
- does not block sequential analysis of earlier volumes;
- does block any claim that the current Japanese tankōbon corpus is complete;
- must be added before an immutable complete-current-corpus release.

## 2. Preferred future replacement: Volume 17

Current V17 is fully readable and structurally valid but only 584×754.

Priority: **high but non-blocking**.

A replacement is especially valuable for:

- Japanese microtext;
- signage;
- handwritten reactions;
- visual-form close reading;
- exact quotation verification where ruby/furigana matters.

## 3. Optional future replacement: Volume 16

Phase-0 visual QC found that V16 contains persistent third-party watermarks and two repeated scan-site advertisement inserts.

Priority: **moderate, non-blocking**.

A clean V16 would improve visual/formal analysis and simplify locator logic, but the current manga content is readable and internally continuous.

## 4. V01–V15 status

No present structural blocker was found.

All V01–V15 files:

- pass archive CRC;
- have continuous numeric image sequences;
- have image counts matching embedded `ComicInfo` page counts;
- have no exact duplicate image groups;
- decode successfully.

This means they are safe to use as the current preferred working set, while retaining the general provenance caveat that they are derivative containers rather than publisher-native masters.

## 5. Rurubu supplementary corpus

Two Japanese travel-guide volumes are present:

- `Laid-Back Camp - Rurubu Travel Guide [Japanese].cbz`
- `Laid-Back Camp - Rurubu Travel Guide - Season 2 [Japanese].cbz`

Both:

- pass archive CRC;
- contain decodable AVIF page images;
- are 1569×1920 throughout;
- retain covers, full-color travel layouts, maps/routes, photography, anime imagery, and publication/end matter in sampled inspection;
- identify JTB Publishing in embedded metadata.

### Evidentiary role

They are **supplementary paratext**, not primary manga evidence.

They may later support a three-layer geography model:

1. **Manga-internal representation** — what Afro's manga itself depicts or says.
2. **Real-world geographic/practical context** — what the travel guide says about routes, sites, campgrounds, food, transport, and local attractions.
3. **Franchise tourism framing** — how the media franchise presents real places to fans and travelers.

No inference may move silently from layer 2 or 3 back into layer 1.

## 6. Materials not currently required

The following would be useful later but are not Phase-1 prerequisites:

- official English manga editions for targeted translation comparison;
- magazine-serialization pages for publication variants/color/editorial context;
- additional official guidebooks or author interviews;
- anime audiovisual sources for an adaptation phase.

They should be added as distinct source classes rather than merged into the primary manga ledger.

## 7. Replacement / augmentation rule

A later source never erases the earlier source record.

Use the states:

- `LOCKED_CURRENT_PREFERRED`
- `PROVISIONAL_LOCK`
- `SUPERSEDED_RETAINED_FOR_PROVENANCE`
- `PENDING`
- `LOCKED_SUPPLEMENTARY`

When a better source arrives, record:

> old hash → comparison audit → new hash → reason for preference → affected analytical claims, if any

This keeps the project reproducible even after source upgrades.
