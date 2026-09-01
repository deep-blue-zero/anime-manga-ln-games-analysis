# Anime, Manga, Light-Novel, and Games Analysis

Owner-maintained repository for human- and LLM-readable analytical work about anime, manga, light novels, and games.

## Current state

The repository is public and the G3 public bootstrap is closed. Work is in the G4 representative-pilot phase. Character Index v2 hardening is complete, and the first integrated substantive candidate is the U149 tranche under `series/the-idolmaster-cinderella-girls-u149/`. The prior unapproved P05/YonaiP v1 tuple remains withdrawn and was not imported; the current YonaiP discovery record is an independently authored schema-v2 record.

Google Drive remains authoritative until a separately approved and verified G8 analytical-authority activation changes the authority state. Public visibility did not activate Git as the analytical master: the Git tree remains a nonauthoritative candidate representation.

The verified G3 public-visibility evidence is bound in `governance/repository-controls/public-activation-bindings.json`. Public readers may make independent forks, but the upstream repository is a personal project: `deep-blue-zero` is its sole human writer and contributor, and external pull requests, commits, or patches are not accepted upstream. See `CONTRIBUTING.md` and `governance/policies/PUBLICATION_AND_CONTRIBUTION_POLICY.md`.

## First read

1. `governance/AUTHORITY_STATE.yaml`
2. `governance/AUTHORITY_SCOPE.json`
3. `governance/repository-controls/public-activation-bindings.json`
4. `governance/MANGA_ANIME_CORPUS_INDEX.md`
5. `governance/CHATGPT_AUTHORITY_AND_ROUTING.md`
6. `CHARACTER_ANALYSIS_INDEX.md`
7. `LICENSE.md` and `THIRD_PARTY_NOTICES.md`

## Intended topology

- `series/<stable-slug>/` — one canonical analysis tree per series
- `studies/<stable-slug>/` — comparative, taxonomy, and other non-series studies
- `characters/` — curated character registry source
- `governance/` — authority, policies, schemas, and navigation
- `tools/` — deterministic repository validation and generators
- `crosswalk/` — sanitized source-to-Git path and materialization records
- `provenance/` — public-safe reference metadata for artifacts retained outside Git

## Publication and license state

Every public push must pass the repository's publication-safety controls before it leaves the contained migration workspace. Raw acquisition evidence, primary-source media, excluded binaries, credentials, personal data, local paths, and non-migrated Drive references stay outside Git. The sole repository workflow is a non-mutating, read-only integrity and publication audit; it cannot write to the repository.

Covered original content is licensed under CC BY-NC 4.0 within the narrow scope stated in `LICENSE.md`. Third-party material and repository software/tooling are excluded as described in `THIRD_PARTY_NOTICES.md` and the license file.
