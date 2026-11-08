---
title: "Tokyo 7th Sisters — EPISODE.4U Prerequisite Audit"
artifact_id: T7S_EPISODE_4U_PREREQUISITE_AUDIT
artifact_type: bounded_prerequisite_audit
series: Tokyo 7th Sisters
generation: V1
version: "1.0"
status: canonical
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
do_not_use_as_literary_evidence: true
source_boundary: "Routing metadata and already-consumed EPISODE 1.0 state used prospectively to decide the next Main unit; no KARAKURI or other later story text"
decision: ADMIT_COMPLETE_MAIN_EPISODE_4U
created: 2026-09-12
last_updated: 2026-09-12
---

# Tokyo 7th Sisters — EPISODE.4U prerequisite audit

Current authority: [CURRENT_STATE_AND_CORPUS_MAP.md](../CURRENT_STATE_AND_CORPUS_MAP.md). Source binding: [T7S_SOURCE_LOCK.json](../01%20Sources%20and%20Chronology/T7S_SOURCE_LOCK.json). Prior boundary proof: [T7S_EPISODE_1_0_COMPLETION_AUDIT.md](T7S_EPISODE_1_0_COMPLETION_AUDIT.md).

## Decision

**Admit the complete category-qualified native Main `EPISODE.4U` family layer `200040` as the next story unit after EPISODE 1.0.** The decision is grounded in the preserved client's series-specific recommendation order, not in filename intuition, source-array proximity, layer priority alone, external synopsis, or the user's recollection by itself.

The admitted set is exactly 22 episode IDs:

`{203000701, 203000702, 203000801, 203000802, 203000901, 203000902, 203001101, 203001102, 203001201, 203001202, 203001301, 203001302, 203001401, 203001402, 203001501, 203001502, 203001601, 203001602, 203001701, 203001702, 203001801, 203001802}`.

## Routing evidence

The locked `m_scenario_recommend` table for series `100020` assigns:

| Rank interval | Main family | Decision relevance |
| ---: | --- | --- |
| 1–91 | EPISODE 1.0 / `200030` | already consumed and closed |
| 92–113 | EPISODE.4U / `200040` | exact next complete recommended unit |
| 114 onward | EPISODE.KARAKURI / `200050` begins with `204001001` | next metadata-visible boundary; story remains unopened |

The recommendation extract SHA-256 is `d4d90261fa085363ab0ac2bd190305f9d82d7f58952c70823134b3725e12cddb`. The native scenario-layer extract SHA-256 is `5fac27e3e6bea2381b29eaf95a72e5c5f1c78af502554b1b0cb62106dcefafdc`. The locked episode catalog SHA-256 is `cda29102ec76a4242bcbb194a37a12453510e7ca6ccffe5478e4f1358b18e625`. All were bound to witness `T7S_GAME_OFFLINE_JA_R484`, alias `c20260909-r484`, master revision 484.

The family priorities are EPISODE 1.0 `11`, EPISODE.4U `10`, and EPISODE.KARAKURI `9`. They are consistent with this local succession but do not independently establish a universal reading order. The recommendation axis is stronger because it enumerates episodes within the same series and places all 22 4U entries contiguously before the first KARAKURI entry.

## Collision and exposure control

Native source-array order interleaves the two opening KARAKURI records `204001001` and `204001002` among the physical vicinity of later 4U records. That layout is not treated as narrative order. The audit inspected only their identifiers, family membership, titles, source-order values, and recommendation position. It did not open their pages, dialogue, choices, presentation commands, synopsis, or media.

No Sub/Event family, additional script, supplemental record, adaptation, performance recording, or external synopsis was admitted. The EPISODE 0.0 and 0.7 packets remain outside this decision; the earlier opening audit already established that they were not prerequisites for the EPISODE 1.0 opening, and no new dependency evidence emerged from the routing metadata.

## Prospective dependency test

The entering state already contains the complete EPISODE 1.0 formation line, including the twelve current Nanasta performers and audience-level confirmation that presented Coney is Nicole. EPISODE.4U's metadata presents a named autonomous group rather than a chronological prequel marker. The recommendation service places it immediately after the closed unit. No metadata or already-admitted claim asserts that KARAKURI, EPISODE 0.0, EPISODE 0.7, a Sub/Event story, or a supplemental packet must be known first.

This supports `ADMIT`, not the stronger proposition that EPISODE.4U is narratively independent of every unconsumed source. If its text had required an unknown antecedent for a load-bearing reconstruction, the operation would have paused and opened a prospective boundary correction. No such dependency was needed.

## Execution boundary

The authorized operation therefore consumed all and only the 22 listed primary documents in recommendation order, preserving native order within the family and stopping before `204001001`. Its five analytical blocks are:

1. `T7S_B0012` — six short 4U prologues;
2. `T7S_B0013` — Identity, Supremacy, and Ultimatum;
3. `T7S_B0014` — Lost Idols origin;
4. `T7S_B0015` — public intrusion and twelve-member deliberation;
5. `T7S_B0016` — final confrontation, reconstitution, and postscript.

Block division follows causal and interpretive seams, not an assumption that every native episode needs its own document or that every menu label must become one oversized reading.

## Revision history

- 2026-09-12 — V1 / 1.0: verify current project/source state, separate recommendation order from physical source order and family priority, admit complete Main EPISODE.4U as the next unit, and retain KARAKURI as metadata-only boundary.
