# Artifact eligibility policy

The repository is optimized for text that a human or LLM can interpret directly.

## Size gates

1. Any artifact over 1 MiB requires an explicit review record.
2. Generated or extracted structured data over 10 MiB is `REFERENCE_DRIVE` by default.
3. No tracked object may exceed 25 MiB without a named binary or large-text exception.
4. Git LFS does not make out-of-scope content eligible.

## Default external or excluded classes

CBZ, ZIP, RAR, 7z, audio, video, scans, source media, large images, binary evidence, databases, model/cache files, executables, generated extraction outputs, superseded Office/PDF originals, large generated corpora, and duplicate release bundles are `REFERENCE_DRIVE` or `VERIFIED_EXCLUDED` by default.

A named exception must identify the artifact, purpose, rights basis, size, content hash, review decision, and why a text derivative or external reference is insufficient. Future publication remains a separate audit regardless of migration eligibility.

## Named text exception contract

A reviewed text artifact over 1 MiB is admissible only when `governance/repository-controls/tracked-file-policy.json` binds its exact repository path, byte length, and SHA-256 digest. The validator does not treat the exception as a path-wide allowance: a one-byte or one-bit change invalidates the tuple and restores the normal size and text-normalization failures. Secret, publication-hazard, NUL, and strict UTF-8 checks are never waived.

The following single exception is approved for the G4 P02 large-structured boundary:

| Repository path | Bytes | SHA-256 | Review decision | Encoding allowance |
|---|---:|---|---|---|
| `series/idoly-pride/V2 Analysis/02 Source Audits and Longitudinal Ledgers/02.01 Corpus Coverage and Priority Ledger/IDOLY_PRIDE_V2_SOURCE_TO_BUNDLE_PROVENANCE.csv` | 1,377,633 | `7dde60c452627a694307dda68abfb0d4d434ec1c2ce934bf85a0b81db483c366` | `OWNER_APPROVED_G4_P02_LARGE_STRUCTURED_BOUNDARY` | Existing UTF-8 BOM and carriage returns are accepted only while the complete tuple matches. |

The ledger is retained because its source-to-bundle relationships are directly queryable analytical provenance; an external-only pointer would make the migrated analyses materially harder to interpret and audit. This is not a general CSV, Idoly Pride, BOM, CRLF, or size-threshold exception.

## Native Google Sheet representation contract

Native Google Sheets remain controlled Drive authoring surfaces. Under the approved X1 disposition, a reviewed revision may be represented in Git by UTF-8/LF TSV projections plus a machine-readable structure manifest after source revision, workbook structure, tab dimensions, and exact committed bytes are verified. The proprietary XLSX export remains `REFERENCE_DRIVE`; Git LFS is not used for it.

The partial DJFW P03 pilot applies this contract to revision 18 of `DJFW_PROJECT_CONTROL_SHEET`: 17 TSV projections and one structure manifest are tracked. This is a structured-text representation, not a binary-artifact exception and not authority cutover. A later native-Sheet revision becomes a Git candidate only after a new verified export and ordinary Git publication lifecycle.
