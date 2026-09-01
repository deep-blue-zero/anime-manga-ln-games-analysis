# Azur Lane Pipeline Hardening Audit

Audit date: 2026-08-20  
Pipeline generation: 0.1.0, pre-hardening baseline  
Pinned sources:

- AzurLaneTools/AzurLaneData `4cca5c2437007b62d30a6235fcfc0c0203231378`
- AzurLaneTools/AzurLaneLuaScripts `cc8e9fdf6a1a2e5d20c9a8ff6c0369832bb33336`

This audit freezes current behavior before H1?H7 implementation. It is descriptive, not a literary analysis.

## Stable behavior that must not regress

- CN remains the originating textual witness for `origin`; CN, JP, EN, TW, and KR remain independently recoverable.
- Canonical identity is based on encoded group and skin IDs, never display-name merging.
- META, child, muse, collaboration, and same-name incarnations remain separate.
- Story records preserve sequence, narration, other speakers, choices, title cards, presentation metadata, inherited background/BGM, raw rows, and memory linkage.
- Raw strings and normalized strings remain separate; translation remains null/none by default.
- Every normalized record retains repository, commit, locale, file, table, record ID, parser/pipeline versions, timestamp, and content hash.
- Cross-locale structural alignment remains deterministic and independent of semantic review.
- Community text is not primary evidence.

## Five frozen regression fixtures

| Character | ID | CN direct lines | CN scenes | Dedicated chapters | Dialogue records | Social threads | Current grade |
|---|---:|---:|---:|---:|---:|---:|---|
| Taihou | 30707 | 257 | 28 | 7 | 108 | 25 | B |
| Enterprise | 10706 | 1,101 | 178 | 0 | 145 | 12 | A |
| Baltimore | 10316 | 355 | 81 | 4 | 98 | 9 | B |
| Atago | 30312 | 128 | 31 | 7 | 85 | 5 | C |
| St. Louis | 10213 | 67 | 18 | 0 | 72 | 5 | C |

The exact snapshot is stored in `tests/fixtures/hardening_baseline_v1.json`. H7 tests use the pinned commits and bounded minimums so valid additions remain possible.

## Successfully extracted systems

- canonical ship/group identity, locale names, aliases, skins, variants, nation IDs, ship instances, and story actor mappings;
- aggregate narrative scripts with full ordered context;
- character memories through `memory_group` and `memory_template`;
- base and skin dialogue from `ship_skin_words`, `ship_skin_words_extra`, and `ship_skin_words_add`;
- affinity, oath, profile, combat, relationship-specific, and special-secretary text;
- Juustagram posts/comments, Fleet Chat, Dorm3D chat, and Island relationship triggers;
- evidence-only relationship records;
- five-locale structural alignment;
- per-character JSONL, narrative Markdown, coverage, and SHA-256 manifests;
- SQLite/FTS5 search.

## Character-specific absence versus capability gaps

- Enterprise and St. Louis have no complete dedicated character-memory group under the current strict detector. This is `NOT_FOUND`, not confirmed absence.
- St. Louis emits no Fleet Chat thread in the supported activity-chat tables. This is `NOT_FOUND`, not a parser failure.
- Dorm3D chat parsing is implemented. A character without emitted Dorm3D chat must not be labeled parser-unsupported merely because Taihou has content.
- Non-chat Dorm3D interaction graphs and broader Island unit/action graphs are parser capability gaps.
- Child-memory and sound-story specialist exporters remain unaudited/unsupported.

## Machine-strong but analyst-weak outputs

- JSONL provenance, raw records, ordering, hashes, and stable IDs are strong.
- `CHARACTER_SOURCE_MAP.md` is only a few lines and does not inventory evidence.
- Human-readable output contains narrative scenes only but is named `PRIMARY_SOURCE_CORPUS`, implying broader coverage.
- Dialogue, social, relationships, and regional alignment have no substantive analyst-readable editions.
- Raw name-code and presentation markup is preserved correctly but no deterministic analyst rendering exists.
- Identity joins are machine-readable but lack per-character diagnostics explaining inclusion and rejected ambiguity.

## Potentially misleading current metrics

- `distinct_conversation_partners` includes scene co-occurrence and can exceed actual interlocutors substantially.
- One aggregate `regional_alignment_records` count mixes narrative and static dialogue.
- Readiness scoring rewards raw volume heavily and does not expose component scores.
- No corpus-composition warnings identify Commander-heavy, skin-heavy, socially sparse, or regionally sparse evidence.

## Source-layer anomaly: St. Louis

St. Louis has one base skin and four non-base skins. All four non-base skins contain dialogue. Current extraction marks every non-base dialogue record as `interactive_skin` when either `ship_l2d_id` or `l2d_animations` is populated. Because `skin` and `interactive_skin` are mutually exclusive labels, St. Louis reports:

- `skin: NOT_FOUND`
- `interactive_skin: PRESENT`

This does not mean ordinary skin dialogue is absent. It means `interactive_skin` is currently an exclusive source-layer label although interactivity is a capability of a skin and should be modeled as an overlapping facet. H1 must make all non-base records part of `skin`, with interactivity represented separately.

## Current `other` category

For St. Louis, one record per locale maps to `other`: raw slot `vote`, skin 102134, table `ship_skin_words`, source text `????`. This is a placeholder/campaign-vote field, not a hidden large characterization system. H1 should assign a documented `vote_or_campaign` category and retain the raw slot.

## Regional comparison limits

Structural alignment is reliable at story ID/sequence and table/skin/slot/index level. Nearly every translated string currently becomes `REQUIRES_HUMAN_REVIEW`; there is no useful semantic triage. No current output makes a censorship determination, and hardening must preserve that restraint.

## Naming, token, and export issues

- `{namecode:N}` and markup are correct raw evidence but awkward for first reading.
- The current narrative Markdown uses unresolved tokens and presentational tags.
- Per-character folders are canonical and coherent under `derived/characters/`; no competing root should be introduced.
- The code repository has method documents, but there is no single corpus entrypoint that routes an analyst through current releases and manifests.

## Hardening decision

Preserve extraction architecture. Refactor semantic labels and exporters, not source acquisition. Add explicit status reasons, relationship types, Commander entity, analyst rendering, separated alignment metrics, deterministic semantic triage, versioned scoring, archival entrypoints, source-surface discovery, and bounded regressions.
