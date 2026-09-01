---
title: AoButa Phase 9 Final Archival Lock Report
series: 青春ブタ野郎シリーズ / Rascal Does Not Dream
artifact_type: final_archival_lock_report
version: '1.0'
date: '2026-08-12'
status: final_immutable_release
release_version: '1.0'
immutable_delivery_lock: true
---

# Phase 9 — Final Archival Cleanup, Checksum Lock, and Immutable Delivery

Phase 9 converts the Japanese-verified Phase-8 working corpus into the definitive **v1.0 immutable analytical release**.

## 1. Archival cleanup

The final release keeps the mature analytical corpus, source-navigation infrastructure, Phase-8 verification evidence, governing method/architecture, and final administrative controls. It removes superseded working-state material from the delivery tree, including historical phase READMEs, superseded manifests/checksum inventories, provisional delivery audits, earlier corpus-index snapshots, draft-only QC reports, and `PHASE8_WORKING_STATE.md`.

The Phase0-8 working directory is left untouched outside the release package, so project history is not destroyed; it is simply not mixed into the immutable reader/research release.

Historical/admin files excluded by cleanup pattern: **60**.

## 2. Source lock

- Japanese EPUB sources: **17**.
- SHA-256 identities matched: **17/17**.
- Byte sizes matched: **17/17**.
- ZIP/CRC integrity passed: **17/17**.
- Copyrighted EPUB payloads included in release: **0**.

See `SOURCE_INVENTORY.md`, `SOURCE_CHECKSUMS.sha256`, and `support/FINAL_SOURCE_REVALIDATION.json`.

## 3. Analytical lock

The release retains:

- 17 immutable sequential volume/bonus readings;
- 18 final specialist documents;
- Documents 19–21;
- the selectively expanded continuous full-series synthesis;
- 8 longitudinal ledgers;
- 3 V1–V7 provenance/backfill documents;
- the final reader README;
- Phase-8 source-language verification artifacts.

No analytical thesis was reopened in Phase 9. Changes at this stage are archival, metadata, navigation, and release-control operations.

## 4. Final audits

The final release performs and records:

- internal Markdown link validation;
- exact substantive-prose duplication screening;
- UTF-8 decoding and YAML front-matter validation for every Markdown artifact;
- source-exclusion scan;
- machine-readable corpus-index regeneration;
- final artifact checksum generation and verification;
- deterministic ZIP integrity testing.

## 5. Immutability rule

This package is versioned as **v1.0**. Any future correction, locator improvement, or interpretive amendment should be published as a new release version with a new artifact checksum set and new external ZIP digest. The v1.0 package should not be silently edited in place.

The external ZIP SHA-256 is issued beside the archive rather than embedded inside it, avoiding a self-referential checksum cycle.
