# Anime, Manga, Light-Novel, and Games Analysis

Private Git migration repository for human- and LLM-readable analytical work about anime, manga, light novels, and games.

## Current state

This is the G3 repository bootstrap. It contains governance, schemas, validation tooling, and repository controls only. No analytical corpus has been migrated in this commit.

Google Drive remains authoritative until a separately approved G8 activation changes the authority state. The Git tree is currently a nonauthoritative candidate representation.

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

The repository is private and owner-only during migration. Any future public release requires an independent publication audit and separate owner decision.
