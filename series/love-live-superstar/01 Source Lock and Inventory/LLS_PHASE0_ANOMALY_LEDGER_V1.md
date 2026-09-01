---
series: "Love Live! Superstar!!"
artifact_id: "LLS_PHASE0_ANOMALY_LEDGER_V1"
artifact_type: "phase0_anomaly_ledger"
status: "phase0_complete"
---

# Love Live! Superstar!! — Phase 0 Anomaly Ledger

## Classification key

- **BLOCKER** — prevents canonical semantic analysis until repaired.
- **WARNING** — usable source with a material caveat that must be carried into analysis.
- **SCHEMA VARIATION** — generation/packaging difference that does not compromise required primary evidence.
- **INFORMATIONAL** — noteworthy but analytically non-limiting.

## AV-001 — Season 1 bundle schema evolves during the season

**Classification:** SCHEMA VARIATION

- `S01E01-S01E03`: schema v1; no `op_ed_deduplication` metadata block.
- `S01E04-S01E06`: schema v1; OP/ED dedup metadata present.
- `S01E07-S01E12`: schema v2; OP/ED dedup metadata present.
- Seasons 2-3: schema v2 throughout.

All required primary evidence remains present. No remediation required.

## AV-002 — Selected corrected Japanese subtitle format changes in Season 3

**Classification:** WARNING / METADATA INCONSISTENCY

Corrected Japanese subtitles are retained as `.srt` rather than `.ass` in:

- `S03E04`
- `S03E06`
- `S03E07`
- `S03E08`
- `S03E09`
- `S03E10`
- `S03E11`

The actual SRT files are present, timed, UTF-8 Japanese dialogue sources and are the files named by `selected_subtitle`. However, `subtitle_info.json` in those bundles still declares an `.ass` filename under `language_tracks.japanese_corrected` and `comparison_pairing.primary`.

**Analytical consequence:** Japanese wording and timing remain available. ASS-specific style metadata must not be claimed for those episodes unless independently reconstructed. Episode provenance should name the actual SRT source rather than the stale declared ASS name.

## AV-003 — Episode bundles are analytical derivatives, not continuous video containers

**Classification:** INFORMATIONAL

Bundles contain complete episode audio plus dense timestamped retained frames, contact sheets and indexes, but not the continuous MKV. Exact continuous-motion claims should be limited to retained visual evidence unless a future video source lane is added.


## AV-004 — S01E11-S01E12 English spoken-dialogue derivative filters the wrong active story-dialogue style

**Classification:** WARNING / DERIVATIVE-GENERATION ANOMALY

First discovered during the S1E11 V2.2 local audit and independently reproduced in S1E12, the late-Season-1 bundles' declared paired-English derivatives are structurally present but semantically mis-filtered because generation assumes `Style=Default` is the principal story-dialogue style.

### S01E11

- bundle derivative: `subtitles/S01E11.en.spoken-dialogue.ass`;
- generator filter: `Style=Default`;
- dialogue-index result: **1 / 397** Japanese rows paired (**0.002519** coverage);
- unmodified full embedded English ASS: **341 `Style=newDefault`** events carrying principal spoken story dialogue;
- `Style=Default` is used heavily for signs/title-animation and other non-story events.

### S01E12 recurrence

- bundle derivative: `subtitles/S01E12.en.spoken-dialogue.ass`;
- generator filter: `Style=Default`;
- dialogue-index result: **4 / 403** Japanese rows paired (**0.009926** coverage);
- unmodified full embedded English ASS: **331 `Style=newDefault`** events carrying principal spoken story dialogue;
- corrected Japanese contains **351** spoken-dialogue cues; a conservative local timing reconstruction against the `newDefault` lane yields **307 / 351** pairs (**0.874644** coverage).

**Root cause:** the derivative generator uses a fixed style assumption that is not episode-aware. The affected episodes encode principal English story dialogue as `newDefault` rather than `Default`.

**Analytical consequence:** corrected Japanese remains fully usable and authoritative. The full English ASS can be used as a comparison/navigation source by reconstructing a temporary `Style=newDefault` speech lane. Original bundle pairing statistics remain preserved as source provenance and must not be silently rewritten.

**Remediation for V2 analysis:** reconstruct English comparison locally from the full ASS when needed; do not mutate the canonical source ZIP. Any future bundle-regeneration pipeline should make spoken-dialogue style selection episode-aware rather than assuming `Default`.

This does **not** block S1E11 or S1E12 canonical semantic analysis because the governing corrected Japanese, complete Japanese audio, retained visuals, full English ASS and indexes remain intact.

## Blocking anomalies

**None.**
