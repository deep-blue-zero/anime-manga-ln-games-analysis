---
series: BLUE_ARCHIVE
artifact_type: source_reconciliation
scope: Japanese main-story source and release snapshot for continued sequential analysis
status: current_snapshot
source_boundary: electricgoat/ba-data@jp a038020f1f5ac02dcfe76962426d38f86414cdd8; active audited generation BA_REFRESH_20260928T032248159554Z
created: 2026-09-28
---

# Blue Archive source reconciliation — 2026-09-28

## Frozen session cutoff

This continuation uses the source/release state observed at 2026-09-28 03:53 UTC (2026-09-27 23:53 America/New_York), before opening `BA:main:004:002:001`. The Japanese `electricgoat/ba-data` `jp` remote head was `a038020f1f5ac02dcfe76962426d38f86414cdd8`, matching the active corpus generation. Its recorded game-data version is `v1.73.459696-r96_3cpn8ebtdjiqi6y9qtn1`; the independent `HePudding/ba-storybook` `main` head remains `6c4091603ca76d7d8c3cdb9104933f52cd8cab8e`. These mirrors supply text/provenance, not independent authority that an episode is publicly released.

The publisher's [2026-08-26 maintenance notice](https://bluearchive.jp/news/newsJump/688/) announces official Part 2 Vol.2 Odyssey Chapter 1 episodes 01–08. The publisher's [2026-09-09 release announcement as carried by GameWith](https://gamewith.jp/gamedb/6253/articles/63064) specifies episodes 09–14. The 2026-09-23 update [announced by Yostar as carried by GameWith](https://gamewith.jp/gamedb/6253/articles/63625) concerns a new event and students, not an announced later main chapter. At this cutoff, the last source-backed released canonical main unit is `BA:main:series2:003:001:014` (official Part 2 Vol.2 Chapter 1 episode 14). Recheck release and remote heads at the end of the continuation.

## Corpus layout and audit

`corpus/CURRENT.json` selects immutable `GENERATIONS/BA_REFRESH_20260928T032248159554Z`; `ACTIVE_CORPUS.md` is its human entry point. Raw Git snapshots live under `01_RAW_UPSTREAM/`, rejected candidates under `.staging/`, and the former root corpus under `ARCHIVE/LEGACY_CORPUS/BA_DERIVED_20260816T010224Z`. The selected generation has `00_MANIFESTS`, complete `02_CANONICAL_STORIES`, row-level `03_STRUCTURED_DATA`, derived bundles, `08_LLM_INGEST`, `09_AUDITS`, and link-only `10_READING_INDEXES`. Its `REFRESH_AUDIT.json`, `ID_AUDIT.json`, and `READING_INDEX_AUDIT.json` report pass, including 4,864 canonical objects checked, 18,067 links checked, and no ID changes or failures. The latest rebuild preserved the already-pinned source heads and added reading indexes; it did not add fresh raw records.

The V1 historical lock remains `BLUE_ARCHIVE_SOURCE_LOCK_V1.md`: `cbe3fd623c2aab9e781ba0ce0483bc77c68bff86`, Excel-backed build `BA_FULL_20260816T002743Z`, and **310** main units. The new DB-backed generation contains **480** main units: all 310 V1 main story IDs remain and 170 additional IDs are present, with none removed. The additions fill old missing chapters and extend later Part 1/Part 2 material; they do not imply that all 170 episodes were released between the two Git commits. Historical `source_commit` values in completed readings and crosswalk rows therefore identify the V1 witness, while new readings cite the new witness. The 310-unit denominator is historical; current main-story coverage uses 480.

The refreshed order also inserts **43 V001 C003 units** (`BA:main:001:003:001`–`:043`, crosswalk orders 43–85) before previously completed chapters. They remain `pending` analytical backfill, not readings silently inherited from V1. Thus current deep-read totals count inspected units, not a contiguous prefix of the 480-row inventory. Continue from the authorized V004 C002 handoff through later canonical units and close this earlier inserted-chapter gap as a separate sequential 43-unit tranche before claiming full 480-unit coverage.

For the 310 shared main IDs, title, group ID, scene count, and episode ID metadata are unchanged. Three story record counts, two utterance counts, and one choice-group count differ: `BA:main:000:001:002`, `BA:main:005:001:023`, `BA:main:005:001:024`, and `BA:main:005:001:026` are the distinct affected IDs. All 310 generated Markdown files differ bytewise because the source/provenance/build representation changed, so byte difference alone is not evidence of plot revision. None of the four metadata-affected IDs is the next unopened `BA:main:004:002:001` or in V004 Chapter 2. Completed analysis remains attached to its V1 witness; any material textual disagreement found later requires a located correction rather than silent retroactive substitution.

## ID and order reconciliation

The corpus story ID is the stable analytical locator. `BA:main:004:002:001` is present at `02_CANONICAL_STORIES/MAIN/VOLUME_004/CHAPTER_002/EPISODE_001.md`, title `第1話;キツネの見る夢`, raw group `42010`, one scene and 131 utterances. The 24 Chapter 2 units are already present in both V1 and the current generation; the new generation's ID/metadata continuity permits sequential analysis to resume there.

`series2` in corpus IDs marks Part 2. Its internal raw volume numbers are offset from official display names: for example `BA:main:series2:003:001:014` is official Part 2 **Vol.2** Odyssey Chapter 1 episode 14, and corpus `series2:002` is official Part 2 **Vol.1** Gehenna. Keep both labels explicit; do not renumber stable IDs. Canonical reading order continues through the remaining Part 1 main arcs, the Final volume, then Part 2. Episode titles and IDs can be inventoried ahead; future dialogue remains closed until the sequential reading reaches it.

The source classes `group`, `event`, `bond`, `mini`, `MomoTalk`, `character_data`, `special_operation`, and `unclassified_scenario` remain outside the admitted main-story reading boundary. Source availability is not analytical admission. The mirror's raw main `release_date` fields are empty, so public release is checked independently against publisher announcements.

## End-of-run release and source-head recheck

At 2026-09-28 19:24 UTC, `git ls-remote https://github.com/electricgoat/ba-data.git refs/heads/jp` still returned `a038020f1f5ac02dcfe76962426d38f86414cdd8`. A fresh review of the [publisher's news listing](https://bluearchive.jp/news/) and main-story search found no announcement after the September Odyssey Chapter 1 release that would extend the cutoff. The September 22 listing concerns the September 23 event/update. Thus the documented session cutoff remains official Part 2 Vol.2 Odyssey Chapter 1 episode 14 / `BA:main:series2:003:001:014`; no unacquired later released main dialogue is inferred from an ending card. All 480 canonical main units in this pinned generation have now been deep-read, including the 43-unit V001 C003 backfill. This completion note does not revise the frozen initial observation or the historical 310-unit lock.
