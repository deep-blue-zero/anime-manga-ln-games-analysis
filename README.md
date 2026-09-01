# Anime, Manga, Light-Novel, and Games Analysis

Owner-maintained repository for human- and LLM-readable analytical work about anime, manga, light novels, and games.

## Current state

The public, owner-maintained Git candidate now contains the complete approved G5 text materialization: 2,665 Drive-derived representations across 36 series roots and two study roots, plus the governed character-discovery, provenance, and repository-control layers. Binary archives, primary-source media, generated extraction corpora, native Office/PDF originals with sufficient text derivatives, and other excluded classes remain outside Git. Their final 2,752-row disposition inventory is summarized in `governance/reports/ARTIFACT_EXCLUSION_REPORT.md`.

This completes corpus materialization, not analytical-authority cutover. Google Drive remains authoritative until a separately approved and verified G8 activation. The Git tree is a nonauthoritative candidate during final aggregate validation and the approved 14-day stabilization lifecycle.

## First read

1. `governance/AUTHORITY_STATE.yaml`
2. `governance/AUTHORITY_SCOPE.json`
3. `governance/repository-controls/public-activation-bindings.json`
4. `governance/MANGA_ANIME_CORPUS_INDEX.md`
5. `governance/CHATGPT_AUTHORITY_AND_ROUTING.md`
6. `governance/policies/RECURRING_TRANCHE_PROCESS.md`
7. `CHARACTER_ANALYSIS_INDEX.md`
8. `LICENSE.md` and `THIRD_PARTY_NOTICES.md`

## Intended topology

- `series/<stable-slug>/` — one canonical analysis tree per series
- `studies/<stable-slug>/` — comparative, taxonomy, and other non-series studies
- `characters/` — curated character registry source
- `governance/` — authority, policies, schemas, and navigation
- `tools/` — deterministic repository validation and generators
- `crosswalk/` — sanitized source-to-Git path and materialization records
- `provenance/` — public-safe reference metadata for artifacts retained outside Git

## Publication and license state

Every public push must pass the repository's publication-safety controls before it leaves the contained migration workspace. Recurring tranches use one bounded owner-approved package from transformation through ordinary non-forced push and verification; this removes repeated intermediate approvals, not source hashes, exclusion review, validation, remote-drift checks, CI, or Drive/Git authority controls. Raw acquisition evidence, primary-source media, excluded binaries, credentials, personal data, local paths, and non-migrated Drive references stay outside Git. The sole repository workflow is a non-mutating, read-only integrity and publication audit; it cannot write to the repository.

Covered original content is licensed under CC BY-NC 4.0 within the narrow scope stated in `LICENSE.md`. Third-party material and repository software/tooling are excluded as described in `THIRD_PARTY_NOTICES.md` and the license file.
