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
