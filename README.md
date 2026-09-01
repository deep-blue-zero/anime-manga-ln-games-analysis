# Anime, Manga, Light-Novel, and Games Analysis

Owner-maintained repository for human- and LLM-readable analytical work about anime, manga, light novels, and games.

## Current state

The repository is public, the G3 public bootstrap is closed, and all five G4 representative archetypes have passed their independent completion audit. G4 is closed and G5 progressive bounded migration is active. The first G5 tranche adds the complete reviewed Maebashi Witches V1 analysis tree and seven Character Index v2 discovery records. The second adds the complete compact Mass Effect comparative corpus and two reviewed Commander Shepard player-archetype records under the intentionally cross-root study binding. The third adds the bounded reviewed Genshin Impact Furina V1 analytical corpus and one Character Index v2 discovery record. The fourth adds 23 reviewed Cinderella Girls mobile-game analytical artifacts and nine Character Index v2 discovery records. The fifth adds 36 reviewed Blue Archive analytical artifacts and eleven Character Index v2 discovery records grounded in the canonical Chapter 1 checkpoint and current-eligible longitudinal ledgers. The sixth adds the 16-file reviewed Youjo Senki V2 light-novel analytical corpus; Tanya remains a non-materialized Character Index candidate because her legacy monograph lacks the recognized authority quartet. Character Index v2 hardening is complete. The materialized candidates are the U149 tranche under `series/the-idolmaster-cinderella-girls-u149/`, one partial IDOLY PRIDE provenance-ledger slice under `series/idoly-pride/`, and one partial DJFW control-state slice under `studies/doujinshi-fanwork-comparative-taxonomy/`. The DJFW slice contains one corpus map plus 17 TSV worksheet projections and their structure manifest; it is not a complete study migration, and names of sibling artifacts inside the corpus map are not claims that those artifacts are present in Git. The P04 reference control records six hash-verified Gakuen Idolmaster ZIP identities as destination-free `REFERENCE_DRIVE` metadata. It adds no archive bytes, Gakuen Idolmaster analysis tree, or Drive URL to Git. The prior unapproved P05/YonaiP v1 tuple remains withdrawn and was not imported; the current YonaiP discovery record is an independently authored schema-v2 record.

Google Drive remains authoritative until a separately approved and verified G8 analytical-authority activation changes the authority state. Public visibility did not activate Git as the analytical master: the Git tree remains a nonauthoritative candidate representation.

The verified G3 public-visibility evidence is bound in `governance/repository-controls/public-activation-bindings.json`. Public readers may make independent forks, but the upstream repository is a personal project: `deep-blue-zero` is its sole human writer and contributor, and external pull requests, commits, or patches are not accepted upstream. See `CONTRIBUTING.md` and `governance/policies/PUBLICATION_AND_CONTRIBUTION_POLICY.md`.

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
