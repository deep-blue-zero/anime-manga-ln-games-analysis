# Audits

[source_manifest.json](source_manifest.json) records the imported CSV v12 / atlas v3 source versions, source and committed byte lengths, SHA-256 values, the reversible CSV encoding conversion, unit counts, embedding fingerprint, handoff provenance and reproducibility boundary. [IMPORT_RECEIPT.md](IMPORT_RECEIPT.md) records scoped transfer acceptance, base/drift, checks and remaining obligations.

The validator checks the manifest against independent frozen-source pins. Re-running validation prints observed results and never blesses or rewrites a baseline. Git history retains the original import; a future reviewed successor must carry its own versions and metadata. The full methodological transport document, transport ZIP and any questionnaire responses are not public study artifacts.
