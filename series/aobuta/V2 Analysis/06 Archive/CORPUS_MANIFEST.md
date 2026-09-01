---
title: AoButa Definitive Full-Series Synthesis — Final Corpus Manifest
series: 青春ブタ野郎シリーズ / Rascal Does Not Dream
artifact_type: final_corpus_manifest
version: '1.0'
date: '2026-08-12'
status: immutable_release
source_count: 17
source_payloads_redistributed: false
---

# AoButa Definitive Full-Series Synthesis — Final Corpus Manifest

**Release:** v1.0  
**Lock date:** 2026-08-12  
**State:** immutable analytical release  
**Primary source payloads included:** no

## Substantive analytical scale

| Layer | Words |
|---|---:|
| 17 sequential volume/bonus readings | 209,651 |
| Specialist Documents 01–18 | 87,190 |
| Evidence/navigation Documents 19–21 | 17,827 |
| Continuous full-series synthesis | 35,196 |
| 00 README and corpus map | 9,827 |
| 8 longitudinal ledgers | 16,087 |
| V1–V7 provenance/backfill documents | 4,653 |
| **Total substantive corpus** | **380,431** |

The substantive count excludes verification reports, manifests, checksums, machine-readable QC files, and governing-method/reference documents. Word counting uses the project convention of whitespace-delimited tokens; contiguous Japanese strings therefore count as phrase units.

## Canonical analytical inventory

- `00_README_AND_CORPUS_MAP.md` — reader orientation and navigation.
- `01`–`18` — specialist full-series synthesis corpus.
- `19`–`21` — revision, evidence-routing, and exact-Japanese navigation layer.
- `AOBUTA_FULL_SERIES_SYNTHESIS.md` — continuous book-like synthesis.
- `volumes/` — 17 immutable local readings.
- `ledgers/` — 8 longitudinal control ledgers.
- three V1–V7 locator/backfill documents — provenance normalization without hindsight rewriting.
- `reference/` — frozen governing analytical method and synthesis architecture.
- `support/` — final index, link/duplication/encoding audits, Phase-8 verification records, locator map, and thread registry.

## Source and checksum controls

- `SOURCE_INVENTORY.md` — 17 revalidated Japanese source identities.
- `SOURCE_CHECKSUMS.sha256` — external source-object digest set.
- `ARTIFACT_CHECKSUMS.sha256` — checksum lock for every packaged file except itself.
- `DELIVERY_AUDIT.md` — final release audit.
- `PHASE9_FINAL_ARCHIVAL_LOCK_REPORT.md` — cleanup and lock policy.

## File inventory

The authoritative per-file machine-readable inventory, including path, category, byte size, word count, SHA-256, and parsed front matter, is `support/CORPUS_INDEX.json`; the index omits its own record and the artifact-checksum file to avoid self/circular hash semantics. The checksum authority is `ARTIFACT_CHECKSUMS.sha256`.

## Release policy

This v1.0 archive is immutable. Corrections should produce a new version rather than silently mutating this package.
