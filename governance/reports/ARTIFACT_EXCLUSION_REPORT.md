# Artifact Exclusion Report

## Scope

This report covers the integrated U149 first tranche, the P02 large-structured-text boundary tranche, and the partial P03 native-document/native-sheet tranche. It is not the final archive-wide exclusion review.

## U149 tranche

The P01 U149 source slice contains 15 Markdown artifacts and no binary artifact. All 15 were materialized as prospective Git content after deterministic authority-front-matter normalization. The conversation transcript remains present for provenance but is marked `historical_legacy` and barred from current authority.

| Class | Count | Disposition | Reason |
|---|---:|---|---|
| Markdown analytical artifacts | 14 | `MIGRATE_TEXT` | Human- and LLM-readable analysis |
| Markdown historical transcript | 1 | `MIGRATE_TEXT_HISTORICAL_ONLY` | Provenance retained; current-authority veto applied |
| Binary artifacts in P01 U149 slice | 0 | Not applicable | None were present in the approved source slice |

## P02 large-structured-text boundary

The P02 slice contains exactly two artifacts. The IDOLY PRIDE source-to-bundle provenance ledger is the archive's named large-text exception: it exceeds 1 MiB, remains below 25 MiB, passed content-safety review, and is admitted as an exact byte-preserved CSV. The much larger Azur Lane structural-alignment JSONL is generated extraction output over the 10 MiB default-external threshold and remains outside Git.

| Artifact | Drive file ID | Bytes | SHA-256 | Disposition |
|---|---|---:|---|---|
| IDOLY PRIDE source-to-bundle provenance CSV | `1EySpUScZKZ2irfYamER1e8FCrnjniGjk` | 1,377,633 | `7dde60c452627a694307dda68abfb0d4d434ec1c2ce934bf85a0b81db483c366` | `MIGRATE_EXACT`; named large-text exception; content-safety postreview passed |
| Azur Lane `structural_alignment.jsonl` | `1US_aDBA1ttPuUx-WlMfr7559PB8vq6we` | 86,490,198 | `ce3d0b9a6df171fdb5d52e7c509d08c35f49ddbc3cbb03e27ca12a079b247a37` | `REFERENCE_DRIVE`; generated/extracted corpus over 10 MiB; no Git destination |

The P02 frozen source slice has SHA-256 `c3e42495cf2a80d93e29245a494ab29533fd30113ceb418ba8f2caa2920c4f19`; its representation slice has SHA-256 `28ec52b8524a49484071cab3660b548ee2c83b24f6402079ace1a19ccebdb005`; and its validated local materialization receipt has SHA-256 `3207c68b9c9b1a51c0e368d50ad8009176db1a1ce926e7b03bd1e0fb03e88de2`.

## P03 native document and sheet

| Artifact | Drive file ID | Bytes | SHA-256 | Disposition |
|---|---|---:|---|---|
| DJFW current-state/corpus-map DOCX export | `10hQeZP3j1AUQ00YsOmt4xYIJmUOant0NsdXXkbmfs3Y` | 13,427 | `76600ca58154f45a2e597d1d34d09f5dacb60ec9235cde1c9a93fbca74439228` | Private conversion evidence; a normalized Markdown derivative is tracked |
| DJFW project-control workbook (`.xlsx`) | `1fDfRSY9oHovjAcO-YPItDfZlirPjlc3yL8IZQZMRRXg` | 56,138 | `5cebbd385b260e349ac54befbc22b5edc80bb8e9e96b4997eac507f123eb72af` | `REFERENCE_DRIVE`; 17 TSV projections plus a structure manifest are tracked |

The tracked derivatives contain one Markdown corpus map, 17 UTF-8/LF TSV worksheet projections, and one structure manifest. This is a partial control-state pilot, not a complete DJFW study migration. The source XLSX and DOCX are not tracked. Six DOCX render PNGs, one DOCX render PDF, seventeen worksheet preview PNGs, the earlier equivalent DOCX/XLSX export envelopes, and the superseded faulty TSV derivatives remain private validation evidence outside Git. The frozen representation slice's earlier XLSX `MIGRATE_TRANSFORMED` row is superseded by the approved X1 disposition and is not current policy. The P03 frozen source slice has SHA-256 `4de71ba55b23bc6e429dd6e4ac942efb47d6370f3cd6e589cc3970f9087d0c54`; its representation slice has SHA-256 `9f116606266962dfc869513ee6b984108bab56ed6af1301b9ea93ffd6a89a193`.

## Default exclusions retained

CBZ, ZIP, RAR, 7z, audio, video, scans, source media, large images, binary evidence, databases, model/cache files, executables, generated extraction outputs, superseded Office/PDF originals, large generated corpora, and duplicate release bundles remain `REFERENCE_DRIVE` or `VERIFIED_EXCLUDED` by default. A named owner-approved exception is required before any such object can enter Git; Git LFS does not itself make an out-of-scope artifact eligible.
