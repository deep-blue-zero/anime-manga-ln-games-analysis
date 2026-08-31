# Anime, Manga, Light-Novel, and Games Analysis

Owner-maintained repository for human- and LLM-readable analytical work about anime, manga, light novels, and games.

## Current state

This is the G3 repository bootstrap. It contains governance, schemas, validation tooling, and repository controls only. No analytical corpus has been migrated yet.

Google Drive remains authoritative until a separately approved G8 activation changes the authority state. The Git tree is currently a nonauthoritative candidate representation.

The GitHub repository is still private while the publication candidate is audited. Its approved target is public visibility after a separately hash-approved activation. Public readers may make independent forks, but the upstream repository is a personal project: `deep-blue-zero` is its sole writer and contributor, and external pull requests or patches are not accepted. See `CONTRIBUTING.md` and `governance/policies/PUBLICATION_AND_CONTRIBUTION_POLICY.md`.

## First read

1. `governance/AUTHORITY_STATE.yaml`
2. `governance/AUTHORITY_SCOPE.json`
3. `governance/MANGA_ANIME_CORPUS_INDEX.md`
4. `governance/CHATGPT_AUTHORITY_AND_ROUTING.md`
5. `CHARACTER_ANALYSIS_INDEX.md`

## Intended topology

- `series/<stable-slug>/` — one canonical analysis tree per series
- `studies/<stable-slug>/` — comparative, taxonomy, and other non-series studies
- `characters/` — curated character registry source
- `governance/` — authority, policies, schemas, and navigation
- `tools/` — deterministic repository validation and generators

## Publication and license state

Every public push must pass the repository's publication-safety controls before it leaves the contained migration workspace. Raw acquisition evidence, primary-source media, excluded binaries, credentials, personal data, local paths, and non-migrated Drive references stay outside Git.

No content license has been selected. A separate owner decision is required before the first substantive analytical corpus batch is published.
