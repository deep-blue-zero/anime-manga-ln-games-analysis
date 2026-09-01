# Artifact Exclusion Report

## Scope

This report covers the integrated U149 first tranche and the settled spreadsheet-format decision relevant to the successor G4 run. It is not the final archive-wide exclusion review.

## U149 tranche

The P01 U149 source slice contains 15 Markdown artifacts and no binary artifact. All 15 were materialized as prospective Git content after deterministic authority-front-matter normalization. The conversation transcript remains present for provenance but is marked `historical_legacy` and barred from current authority.

| Class | Count | Disposition | Reason |
|---|---:|---|---|
| Markdown analytical artifacts | 14 | `MIGRATE_TEXT` | Human- and LLM-readable analysis |
| Markdown historical transcript | 1 | `MIGRATE_TEXT_HISTORICAL_ONLY` | Provenance retained; current-authority veto applied |
| Binary artifacts in P01 U149 slice | 0 | Not applicable | None were present in the approved source slice |

## Controlled reference-only artifact

| Artifact | Drive file ID | Bytes | SHA-256 | Disposition |
|---|---|---:|---|---|
| DJFW project-control workbook (`.xlsx`) | `1fDfRSY9oHovjAcO-YPItDfZlirPjlc3yL8IZQZMRRXg` | 56,153 | `45af93158093209fd43c451f800322808e5b5ef184e949af690089f65e46d57a` | `REFERENCE_DRIVE`; future Git representation is TSV plus a structure manifest |

The validated TSV and structure-manifest derivatives are outside this U149 tranche and must pass a later tranche gate before admission. The original XLSX is not tracked.

## Default exclusions retained

CBZ, ZIP, RAR, 7z, audio, video, scans, source media, large images, binary evidence, databases, model/cache files, executables, generated extraction outputs, superseded Office/PDF originals, large generated corpora, and duplicate release bundles remain `REFERENCE_DRIVE` or `VERIFIED_EXCLUDED` by default. A named owner-approved exception is required before any such object can enter Git; Git LFS does not itself make an out-of-scope artifact eligible.
