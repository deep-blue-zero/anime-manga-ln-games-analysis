# Azur Lane Pipeline Method

## Installation

From this directory, run `python -m pip install -e .`. Python 3.11+ and Git are required; runtime extraction uses only the standard library.

## Commands

- `azl sync`
- `azl audit --characters taihou enterprise akagi`
- `azl normalize --characters taihou enterprise akagi`
- `azl character taihou --authority origin --locales CN,JP,EN,TW,KR`
- `azl search-character Taihou`
- `azl index`
- `azl search "???"`
- `azl coverage taihou`
- `azl relationships taihou`
- `azl sources taihou`
- `azl validate`
- `azl build-jp-audio-catalog --client-assets <ClientAssets/JP> --vgmstream-cli <vgmstream-cli> --integrity-status PASS --output <catalog.jsonl>`
- `azl augment-character --character TAKAO_30311 --jp-audio --dorm3d --island`
- `azl augment-characters --from-current-corpus --jp-audio --dorm3d --island`

`origin` renders CN. A locale authority renders that independently published witness. Translation is always null/none unless a future opt-in aid is added.

## Provenance

Every normalized record stores repository, SHA, locale, source file, table, record ID, extraction time, pipeline/parser versions, and content SHA-256. Character manifests hash every emitted file. Upstream checkouts are reproducible from their SHAs.

## Coverage formula

The `readiness-2.1.0` 100-point model allocates narrative depth 25, complete character-memory depth 15, dialogue-category breadth 15, social-system diversity 10, relationship-context diversity 10, importance-weighted regional coverage 15, and supported source-system diversity 10. Grades are A at 80+, B at 60+, C at 40+, D at 20+, and E below 20. It measures evidence amount/diversity only.

## Regional differences

Alignment uses table/skin/slot/index IDs, story ID/sequence, or social system/thread/message keys. Missing witnesses become structured `STRUCTURAL_GAP` candidates with source family, locale direction, importance, and a deterministic reason such as `REGIONAL_CONTENT_ABSENCE`, `STRUCTURAL_REWRITE`, `UNMATCHED_AUXILIARY_RECORD`, or `IDENTITY_MAPPING_GAP`. Release lag and censorship are never inferred without separate evidence. Semantic review remains a candidate-only layer.

## Update behavior

`azl sync` records pre/post SHAs and uses fast-forward pulls. Current normalization rewrites selected normalized layers deterministically; fine-grained changed-file dependency rebuilding remains planned.

## Source augmentation

Source augmentation is rerunnable and does not regenerate or reinterpret the mature text corpus. Dorm3D and Island parsers preserve system-specific topology and emit character folders only when linked records exist; explicit supported-not-found states remain in coverage for other characters. JP audio acquisition is pinned to `nobbyfix/AzurLane-AssetDownloader` `4.7.1` / tag `v4.7.1` / commit `0ccb1924c11d06888fa4d0f59a708586139234fe`. The current client cache is AZL `9.3.386`, CV `1243`; the post-download integrity check passed. `vgmstream` r2083 identifies each CRI UTF/ACB bundle and enumerates its CRI HCA subsongs read-only. The generated catalog preserves stream identity, skin-suffix semantics, source-relative path, versions, size, SHA-256, and technical metadata. Target-relevant original bundles are deduplicated globally by content hash under Primary Sources and linked from Analysis without binary duplication. Missing client/catalog inputs still emit concrete blockers rather than inferred audio coverage.
