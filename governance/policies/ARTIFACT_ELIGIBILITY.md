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

A reviewed text artifact over 1 MiB is admissible only when `named_text_exceptions` in `governance/repository-controls/tracked-file-policy.json`, the only binding copy, records its exact path, byte length and SHA-256 with its purpose, rights basis and review decision. The exception is never path-wide: a one-byte change revokes it. Secret, publication-hazard, NUL and strict UTF-8 checks are never waived.

The six current exceptions keep directly queryable provenance in Git, where an external pointer would make the analyses materially harder to interpret and audit:

- the three aggregate migration ledgers under `crosswalk/` (strict UTF-8/LF);
- the IDOLY PRIDE source-to-bundle provenance CSV, the only one allowed its existing UTF-8 BOM and carriage returns;
- the Blue Archive Cycle007 character analytical coverage index and supplemental source-to-analysis crosswalk, size-only exceptions recorded in the [exact review record](../reports/storage-decisions/BLUE_ARCHIVE_CYCLE007_EXACT_TWO_TEXT_DERIVATIVE_SIZE_CONTENT_REVIEW_V1.json) (strict UTF-8/LF).

None of these is a general CSV, BOM, CRLF, directory or size-threshold exception, and none grants upstream source rights.

## Native Google Sheet representation contract

Native Google Sheets remain controlled Drive authoring surfaces. A reviewed revision may be represented in Git by UTF-8/LF TSV projections plus a machine-readable structure manifest after its source revision, workbook structure, tab dimensions and exact committed bytes are verified. The proprietary XLSX export, render previews and conversion evidence remain `REFERENCE_DRIVE`; Git LFS is not used for them. A later Sheet revision becomes a Git candidate only through a new verified export and the ordinary publication lifecycle.
