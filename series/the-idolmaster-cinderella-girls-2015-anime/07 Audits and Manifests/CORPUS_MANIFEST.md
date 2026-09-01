---
series: "THE IDOLM@STER CINDERELLA GIRLS"
year: 2015
artifact_id: "CORPUS_MANIFEST"
artifact_type: "final_corpus_manifest"
release: "CG2015_Definitive_Analytical_Corpus_v1.0"
status: "immutable_v1_0_manifest"
---

# CORPUS MANIFEST — CG2015 Definitive Analytical Corpus v1.0

## Release boundary

This release contains **analytical artifacts and permitted metadata only**. It does not redistribute episode video, program audio, subtitle payloads, frame archives, contact sheets, manga/novel source containers, or nested historical package ZIPs.

- **Mainline:** Episodes 1–25.
- **Episode 26:** supplementary animated epilogue/paratext.
- **Authoritative claim ledger:** 410 unique claim IDs / 0 duplicate headings.
- **External production/reception appendix:** not pursued in v1.0.

## Canonical reader layer

`00_README_AND_CORPUS_MAP.md` is the entry point. `CINDERELLA_GIRLS_FULL_SERIES_SYNTHESIS.md` is the continuous mature argument. Documents 01–12 own specialist domains. The post-final-sound Document 14 is the provenance engine. Document 15 treats E26. Logical Document 13 remains intentionally absent as a standalone artifact and is not fabricated for numbering symmetry.

## Retained provenance

- `support/episode_readings/` preserves the available E16–E25 prospective deep readings.
- `support/retrospective_audio/` preserves retained E08–E15 sound-backfill artifacts.
- `support/source_metadata/` preserves permitted source-lock metadata only.
- `support/machine/` preserves machine-readable specialist/QA sidecars.

The missing E01–E15 standalone prospective Markdown readings and unrecovered Cour-1 synthesis remain documented archival gaps.

## Machine-readable controls

- `CORPUS_MANIFEST.json` — complete release file inventory with sizes, hashes, and Markdown word counts.
- `CLAIM_INDEX.json` — 410-claim machine index derived from the authoritative ledger.
- `LOCATOR_INDEX.json` — reverse locator-to-claim index.
- `support/source_metadata/SOURCE_METADATA_MANIFEST.json` — only the source metadata explicitly recoverable from the source lock.
- `ARTIFACT_CHECKSUMS.sha256` — checksum lock for release members other than itself.

## Final audits

- `audits/CG2015_PHASE9_CLAIM_PROVENANCE_AND_LOCATOR_AUDIT.md`
- `audits/CG2015_PHASE9_DUPLICATION_AUDIT.md`
- `audits/CG2015_PHASE9_TERMINOLOGY_CONSISTENCY_AUDIT.md`
- `audits/CG2015_FULL_SERIES_SYNTHESIS_QA.md`
- `audits/CG2015_PHASE9_RELEASE_VALIDATION.json`
- `DELIVERY_AUDIT.md`

The definitive numeric inventory is `CORPUS_MANIFEST.json`.
