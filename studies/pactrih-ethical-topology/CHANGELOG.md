# PACTRIH Study Changelog

## Unreleased

- No further data additions or rescoring are authorized by this import.

## 2026-10-24 — CSV v12 / Interactive Atlas v3 import

- Import the canonical 100-subject matrix (reversible UTF-8 BOM/CRLF to UTF-8/LF encoding conversion only) and standalone atlas (byte-for-byte) under stable `data/pactrih_scores.csv` and `interactive/atlas.html` paths.
- Verify all seven axes, descriptions, identities/order, derived ethics-map coordinates and analysis units (85 Character, 7 Faction, 8 Historical Agent). Preserve supplied PCA, Ward k=8/10/12 IDs, labels and interaction code.
- Add source/embedding hashes, a scoped import receipt, a read-only stale/frozen-atlas guard and mutation tests; document the missing exact PCA/Ward producer and required reviewed successor procedure.
- Verify the existing current-eligible entrypoint and declare study routing for housekeeping; retain provisional analytical status. PACTRIH-SR remains independently versioned and outside the import.

## Initial scaffold (merged 2026-09-03, PR #5)

- Establish the `studies/pactrih-ethical-topology/` project topology.
- Reserve methodology, data, interactive, scripts, and audits subtrees.
- Do not yet materialize CSV datasets or HTML interactive artifacts.
