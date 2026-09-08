---
series: PJSK
artifact_type: source_lock
scope: ANALYTICAL_LAYER
generation: V1
status: canonical
source_boundary: "Sibling Project SEKAI Japanese corpus pipeline"
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
---


# Project SEKAI Analytical Source Lock


## Authority


The analytical layer does not maintain an independent transcript corpus. Source identity, repository pins, canonical stories, chronology metadata, generated projections, and provenance are governed by the sibling pjsk-corpus-pipeline and its CURRENT_STATE_AND_CORPUS_MAP.md plus manifests.


Before a new analytical campaign, read the source current-state map and record the source/pipeline generation used by the resulting artifact in its source boundary or analysis cutoff.


## Rules


- Canonical story records outrank retrieval projections for textual interpretation.
- Character, relationship, unit, and LLM bundles are retrieval aids with stable locators, not separate narrative authorities.
- Do not silently merge secondary transcript wording into the preferred Japanese source.
- Preserve chronology uncertainty, conditioned ordering, special contexts, and My SEKAI separation where the source corpus does.
- Important verbatim claims should remain traceable to canonical source locators.
- If the source corpus advances while an analysis is underway, the analytical artifact retains the source boundary it actually used; newer source material enters later through the live-service integration method.


## Current lock state


`SOURCE_COMPLETION_CUTOFF = PJSK_SOURCE_20260822T184634Z_EVENT_0213`.

The continuous completion campaign freezes the certified inventory observed at execution start and reverified during recovery on 2026-09-08. This replaces the initialization-era dynamic-lock statement; it does not change any earlier reading's prospective boundary.

| Lock field | Verified value |
|---|---|
| Source pipeline run | `20260822T184634Z` |
| Certification generated | `2026-08-22T18:46:34.036268Z` |
| Pipeline / parser | `0.2.7` / `0.1.0` |
| Preferred Japanese transcript pin | `22b4d19e982feaece6cd42c074e86e2cefac5cdd` |
| Separate secondary witness pin | `b25ce86ec43a6c9e819e9106549f75a50edf1357` |
| Master-data pin | `475d81169f2a00f07195d766eb936b8168a5c72c` |
| Master asset version / platform | `1.9.0.30` / `ios` |
| Logical stories / scenes / ordered records | `15,292 / 20,833 / 435,615` |
| Terminal event | `EVENT_0213 — Leap Beyond The Limits！` |
| Terminal event core | `PJSK:event:0213:01–08` |
| Terminal initial-availability bucket | `RB_20260809T060000Z` |
| Terminal event envelope | 8 core chapters + cards `1440–1444` (10 halves) + archive-publication area `areatalk_ev_idol_27_001–004` (4): 22 surfaces |
| Event inventory | 211 distinct event IDs; `0166` and `0186` are absent from the locked manifest and are not invented missing operations |
| Temporal partitions | 5,872 dated; 743 condition-ordered; 8,677 undated |

The source map's newest-dated-story label `PJSK:event:0213:01 — 始まりの時` names the first chapter of the terminal event, not its complete envelope or parent title. The full manifest and event-review group establish the eight-chapter boundary above. Associated cards and archive-publication areas are envelope members, not assertions of co-release or identical narrative time.

### Integrity and certification

The following downloaded source files were checked against `00_MANIFESTS/ARTIFACT_CHECKSUMS.sha256`; all six matched. The release manifest contains 15,292 unique logical-story rows, and its counts, source pins, and terminal event agree with the live source current-state map, release certification, audit snapshot, and event-review groups.

| Source artifact | SHA-256 |
|---|---|
| `00_MANIFESTS/RELEASE_ORDER_MANIFEST.jsonl` | `c09ff420f4dd92a397e6aeadd4c399f0597e34a67c3238273df102a6438d5223` |
| `00_MANIFESTS/RELEASE_ORDER_MANIFEST_SCHEMA.md` | `36461bbc303bd7c012a7887a0fa816b319a782e35badb6cc76279fb227ab0ecb` |
| `00_MANIFESTS/CHRONOLOGY.csv` | `f15f394b910aa914159311cbe65e092c72b6e048dc0f92b2bcc452abdce9563d` |
| `00_MANIFESTS/SOURCE_MANIFEST.json` | `b4064e11d56df3d932a0109c4dcfbd21a401a2bea7ca7688b642f707a6c8e17c` |
| `09_AUDITS/RELEASE_ORDER_AUDIT.json` | `abf651cc31da05ed615021c5135723ab2f8ad4aa4d78d96873db719edfd55518` |
| `00_MANIFESTS/PIPELINE_RUN.json` | `43f1fe175502b766ff60a772ae09291bf9d21facf37424e009263fcc8bd0a18d` |

The source certification reports passing provenance, area-context, release-order, audio, and incremental-update audits and zero parse failures. This verifies the supplied snapshot's certification and the six files above; it does not claim that every primary story or audio file has already been independently downloaded and inspected by the analytical campaign. Each source transaction must still verify its actual canonical evidence.

### Scope and continuation

The frozen inventory includes main, event, card, area, self, special, and My SEKAI source classes. Undated, condition-ordered, alternate, special, and My SEKAI evidence retains its source context; no total narrative chronology is manufactured. Generated character packages remain retrieval infrastructure, not completed analytical monographs or reconstruction models.

The authorized run is `continuous_sequential` through this inventory, including the remaining foundations, deferred-route interpretation, reconstruction, synthesis, audits, and protected integration. Later source ingestion belongs to a subsequent cycle. Current analytical progress and the next operation remain owned by the [corpus map](../PJSK_ANALYTICAL_CORPUS_MAP.md) and [coverage ledger](PJSK_ANALYSIS_COVERAGE_LEDGER.md).