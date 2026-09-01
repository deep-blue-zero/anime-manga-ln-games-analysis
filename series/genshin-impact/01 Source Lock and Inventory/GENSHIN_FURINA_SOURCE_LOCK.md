---
series: GENSHIN
artifact_type: source_lock
scope: FURINA
generation: V1
status: active_provisional
source_boundary: "Genshin Impact 7.0.0 Tier-A normalized corpus; Furina V1 layered source lock"
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
---

# GENSHIN_FURINA_SOURCE_LOCK

## Purpose

This document freezes the source boundary for the V1 Furina character-monograph project. It distinguishes raw source authority, normalized textual evidence, corrected structural authority, and analytical inference so that the monograph can be revised without losing provenance.

## Locked source state

| Layer | Locked authority | Use in this project |
|---|---|---|
| Raw reconstruction root | Tier-A Genshin snapshot `GENSHIN:26df1dfbdf05`, game version 7.0.0 | Ultimate reconstruction authority if a normalization defect is found |
| Canonical normalized text carrier | Furina evidence package bound to build `GENSHIN_2026-08-23_fe06a14ba6` | Supplies the 6,340 trilingual context/dialogue records and 2,364 Furina-attributed records used here |
| Corrected structural authority | Controlled-scale Genshin build `GENSHIN_2026-08-23_3f0cd906c8` and `CONTROLLED_SCALE_ITERATION_REPORT.md` | Governs path-qualified Talk scene identity, corrected StoryUnit partitioning, source-class counts, and corrected counterpart totals |
| Profile/self-description | 79 normalized profile, voice-line, and character-story records | Separate self-description/paratext layer; never silently substituted for observed behavior |
| Third-party candidate view | 870 explicit-name candidate records | Search surface only; each claim requires speaker-access and relevance review |

The two normalized Genshin builds use the same Tier-A source snapshot. The later controlled-scale build preserves the dialogue-node inventory while correcting Talk scene identity and increasing the full Genshin StoryUnit count from 50,621 to 58,103. For Furina, the current controlled-scale summary is 2,364 attributed lines, 213 units, 12 source classes, 79 profile records, 870 mention candidates, and 20 corrected counterparts.

The existing Drive Furina package remains useful as a text carrier because the corrected scale pass did not report loss or replacement of Furina's dialogue nodes. It is **not** treated as current authority for old aggregate scene membership, old counterpart counts, or `Quest/GlobalDialog.json` as one scene.

## Language hierarchy

1. **CHS** is the primary source text in the normalized corpus.
2. **JP** is a first-class parallel localization and an important speech/register witness, especially Furina's stable `僕` self-reference and register modulation.
3. **EN** is a first-class parallel localization and the principal readable quotation layer in this English analytical corpus.
4. When an interpretive distinction turns on wording, CHS controls; JP and EN are compared rather than silently harmonized.
5. Missing JP/EN cells remain missing. No localization is backfilled from another language.

## Included evidence surfaces

- Archon/main-narrative CodexQuest material;
- character-story and story-quest material;
- classified event and limited-event material;
- Talk families including Quest, Activity, Cutscene, Coop, FreeGroup, NPC, Gadget, environmental, ambient, repeatable, and root Furniture/teapot material where present in the current normalized source;
- Furina profile description, voice lines, and character stories;
- conservative counterpart and third-party candidate evidence;
- stable `hoyo://GENSHIN/7.0.0/...` source locators.

## Known evidence limitations

The current Genshin corpus remains `PARTIAL` for `character_deep_dive` and `behavioral_model`, while `speech_model_text` is `READY` and `performance_model` is `NOT_READY`.

Material limitations:

- main-story and character-story parent/index joins remain partial;
- cross-surface chronology is incomplete;
- some Talk records are intentionally independent or metadata-like rather than fully reconstructed scenes;
- 522 continuation gaps and large numbers of unresolved TextMap references remain at full-build level;
- some JP/EN cells are missing in the full corpus;
- no approved audio-locator layer currently supports a Furina performance model;
- the normalized package contains source-order and release-order evidence, not a universally complete diegetic chronology.

Consequences:

- this V1 monograph is `active_provisional`, not frozen definitive authority;
- strong claims about textual voice, recurring decision patterns, public/private adaptation, and represented relationships are permitted;
- claims of exhaustive appearance coverage or exact total chronology remain `OPEN`;
- new recovered source material must be routed through the claim-revision ledger rather than simply appended to conclusions.

## Duplication and branch policy

The package contains repeated text across CodexQuest and Talk representations and repeated readable branch renderings. This project applies the following rule:

- CodexQuest is preferred for sequential main/character-story reading where available;
- Talk duplicates corroborate text and supply finer source-surface structure but do not multiply behavioral evidence;
- unique Talk-only event, ambient, environmental, social, and low-stakes records are analyzed independently;
- convergent branch responses count once canonically even if rendered repeatedly for readability;
- `Quest/GlobalDialog.json` is an aggregate vocabulary partitioned by corrected continuation components, never one shared diegetic scene.

## Analytical authority states

- Source facts: direct normalized records with locators.
- Strong inference: repeated pattern across independent source units.
- Provisional inference: plausible pattern with incomplete source-class coverage.
- Speculation: excluded from monograph conclusions unless explicitly marked.
- Revision transitions: `PRESERVE`, `STRENGTHEN`, `REVISE`, `DOWNGRADE`, `REJECT`, `OPEN`.

## Anti-retrojection rule

Later revelations may explain earlier behavior, but they do not erase the epistemic conditions under which that behavior occurred. Each sequential tranche records:

- what Furina knows;
- what she may disclose;
- what others believe;
- what the reader/player can know at that point;
- which later evidence revises rather than replaces the prospective reading.

## Locked source routes

- HoYoverse normalized evidence root: `1_CPeMe9iXCWyRZ1KCBlDTyS25KOfSBvU`
- Current Furina source package: `GENSHIN/characters/furina/`
- Furina machine evidence: `evidence.jsonl`
- Furina readiness: `readiness.json`
- Current HoYoverse entrypoint: `CURRENT_STATE_AND_CORPUS_MAP.md`
- Current Genshin analytical root: `Genshin Impact` under the canonical analytical hierarchy

## Source-lock conclusion

The present corpus is sufficient for a substantial, source-grounded V1 Furina monograph. It is not sufficient for a claim of exhaustive finality. The correct authority state is therefore **active provisional with explicit open-evidence boundaries**.
