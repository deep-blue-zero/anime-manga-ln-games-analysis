---
corpus: NANA_JP_DEEP_READING
artifact: DELIVERY_AUDIT
release_version: "v1.0"
status: release_tree_validated
generated: "2026-08-14"
---

# NANA v1.0 — Delivery Audit

This file records the release-tree validation performed after the literary and evidentiary audit but before the external ZIP checksum is calculated. ZIP CRC validation and the archive SHA-256 are therefore external release checks rather than self-referential data stored inside the archive.

## Release composition

The package is organized into four analytical layers:

- **Documents 00–16** at archive root: final reader-facing synthesis plus archival/reference layer;
- **`frameworks/`**: governing analytical method and synthesis architecture;
- **`sequential_deep_readings/`**: Volume 1–21 analyses plus canonical Chapters 81–84 continuation analysis;
- **`historical_audits/`**: the Phase-2 evidence-stabilization audit retained for provenance.

Root-level release-control files additionally include:

- `SOURCE_INVENTORY.md`;
- `PHASE8_FINAL_ARCHIVAL_AUDIT.md`;
- `CORPUS_MANIFEST.md`;
- `ARTIFACT_CHECKSUMS.sha256`;
- this `DELIVERY_AUDIT.md`.

## Package hygiene

The release intentionally contains **no copyrighted primary-source payloads**. In particular, it excludes:

- `.epub` manga source files;
- `.cbz` continuation scans;
- `.pdf` paratext source files;
- image extracts;
- OCR working data;
- temporary build scripts;
- superseded/in-progress analysis drafts;
- stale Drive-replication notes.

The source corpus remains identifiable through `SOURCE_INVENTORY.md` and the per-volume analytical YAML without redistributing the source media.

## Text and structure validation

The canonical analytical tree passed:

- UTF-8 decoding checks;
- YAML/front-matter parsing for files that require front matter;
- numbered-document presence checks;
- README document-map target checks;
- evidence-reference and locator audits;
- long-form duplication checks;
- terminology/romanization variant checks;
- removal of chat UI markup, sandbox paths, and draft placeholders.

The only deliberately retained historical irregularity is that Volumes 20–21 do not carry the same `locator_status` YAML field used by several earlier volumes. Their locator ledgers are present and verified, so mutating the frozen files solely for metadata symmetry was rejected because it would invalidate the Phase-2 artifact hash lock.

## Version policy

The release directory is frozen as **v1.0**. After packaging, its files are made read-only. Any later source backfill or substantive correction should create a new version rather than overwrite this tree.
