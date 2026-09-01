---
series: AZUR_LANE
artifact_type: source_augmentation_report
scope: JP_AUDIO_DORM3D_ISLAND
generation: V1
status: complete_with_documented_limitations
---

# Azur Lane Source Augmentation Report

## Source boundary

- AzurLaneData: `4cca5c2437007b62d30a6235fcfc0c0203231378`
- AzurLaneLuaScripts: `cc8e9fdf6a1a2e5d20c9a8ff6c0369832bb33336`
- Build identity: `AZL-2026-08-22-4cca5c24-cc8e9fdf`; it remains on the existing pinned boundary because no upstream revision was changed.
- Primary Sources Azur Lane folder ID: `1BoL0xYtws249v800vv3FWRpKW1jdwUDl`

## Implementation result

- Generic CLI: `augment-character` and `augment-characters --from-current-corpus`.
- JP acquisition/catalog ingestion, SHA-256 deduplication, technical probe, deterministic mapping, explicit ambiguity/absence states, Primary Sources manifests, and Analysis alignments are implemented.
- Original JP assets archived: **344**; mapped slots: **1630**.
- Direct JP acquisition: `ACQUIRED`; catalog `RESOLVED`; integrity `PASS`. No EN mirror or guessed bytes were substituted.
- Dorm3D parser: **supported**, preserving full conditional topology and direct audio references; target regional scenes: **625**.
- Island parser: **supported**, with system-specific identity/behavior/task/scene graphs and raw-Lua fallback provenance; target regional records: **170**.
- Dorm3D/Island voice references feed the same JP acquisition and alignment layer; no second binary archive was created.
- New Analysis evidence consists of per-character audio alignments/coverage, complete Dorm3D scenes and target ledgers where present, and Island identity/behavior/scene graphs where present.
- Existing character readiness scores were not changed. `JP_VOICE_PERFORMANCE_READINESS` is separate.

## Per-character status

| Character | JP audio | Audio mapping | Dorm3D non-chat | Island non-relationship | Analysis corpus updated | Blocking issue |
|---|---|---|---|---|---|---|
| Akagi | AUDIO_PARTIAL | 101 mapped / 1 unresolved | SUPPORTED_NOT_FOUND | SUPPORTED_NOT_FOUND | YES | VOICE_MAPPING_UNRESOLVED |
| Atago | AUDIO_PARTIAL | 71 mapped / 14 unresolved | SUPPORTED_NOT_FOUND | SUPPORTED_PRESENT | YES | VOICE_MAPPING_UNRESOLVED |
| Ayanami | AUDIO_PARTIAL | 109 mapped / 96 unresolved | SUPPORTED_NOT_FOUND | SUPPORTED_NOT_FOUND | YES | VOICE_MAPPING_UNRESOLVED |
| Baltimore | AUDIO_READY | 100 mapped / 0 unresolved | SUPPORTED_NOT_FOUND | SUPPORTED_NOT_FOUND | YES | VOICE_MAPPING_UNRESOLVED |
| Bremerton | AUDIO_READY | 101 mapped / 0 unresolved | SUPPORTED_NOT_FOUND | SUPPORTED_NOT_FOUND | YES | DRIVE_PUBLICATION_PENDING |
| Cheshire | AUDIO_PARTIAL | 99 mapped / 2 unresolved | SUPPORTED_NOT_FOUND | SUPPORTED_PRESENT | YES | VOICE_MAPPING_UNRESOLVED |
| Enterprise | AUDIO_PARTIAL | 120 mapped / 25 unresolved | SUPPORTED_NOT_FOUND | SUPPORTED_NOT_FOUND | YES | VOICE_MAPPING_UNRESOLVED |
| Formidable | AUDIO_PARTIAL | 101 mapped / 12 unresolved | SUPPORTED_NOT_FOUND | SUPPORTED_NOT_FOUND | YES | VOICE_MAPPING_UNRESOLVED |
| Kaga | AUDIO_PARTIAL | 71 mapped / 40 unresolved | SUPPORTED_NOT_FOUND | SUPPORTED_NOT_FOUND | YES | VOICE_MAPPING_UNRESOLVED |
| Kirishima | AUDIO_PARTIAL | 65 mapped / 1 unresolved | SUPPORTED_NOT_FOUND | SUPPORTED_NOT_FOUND | YES | VOICE_MAPPING_UNRESOLVED |
| Le Malin | AUDIO_PARTIAL | 70 mapped / 1 unresolved | SUPPORTED_NOT_FOUND | SUPPORTED_PRESENT | YES | VOICE_MAPPING_UNRESOLVED |
| Nagato | AUDIO_READY | 106 mapped / 0 unresolved | SUPPORTED_NOT_FOUND | SUPPORTED_NOT_FOUND | YES | VOICE_MAPPING_UNRESOLVED |
| Owari | AUDIO_PARTIAL | 65 mapped / 1 unresolved | SUPPORTED_NOT_FOUND | SUPPORTED_NOT_FOUND | YES | VOICE_MAPPING_UNRESOLVED |
| Prinz Eugen | AUDIO_PARTIAL | 114 mapped / 1 unresolved | SUPPORTED_NOT_FOUND | SUPPORTED_PRESENT | YES | — |
| St. Louis | AUDIO_READY | 71 mapped / 0 unresolved spoken; 1 non-dialogue placeholder | SUPPORTED_NOT_FOUND | SUPPORTED_NOT_FOUND | YES | — |
| Taihou | AUDIO_PARTIAL | 152 mapped / 57 unresolved | SUPPORTED_PRESENT | SUPPORTED_PRESENT | YES | VOICE_MAPPING_UNRESOLVED |
| Takao | AUDIO_READY | 114 mapped / 0 unresolved | SUPPORTED_NOT_FOUND | SUPPORTED_PRESENT | YES | — |

## Validation and remaining gaps

- Automated tests: **PASS_WITH_DRIVE_PUBLICATION_PENDING** (100 run; 0 failures; 0 errors).
- Provenance validation: **PASS** (237755 records checked).
- Character artifact hashes: **PASS** (1629 hashes checked).

Regression coverage tests the audio catalog join/dedup/storage boundary, Dorm3D conditional topology/localization/voice preservation, Island identity and condition joins, JSON/Lua fallback, explicit absence states, and absence of audio binaries under Analysis. Original JP bundles are byte-hash verified; technical stream metadata comes from the read-only `vgmstream` parser.


## St. Louis spoken-audio closure appendix

- JP performed-voice spoken readiness: `AUDIO_READY`.
- Final mapped spoken utterances: `71`.
- Unresolved spoken text records: `0`.
- Known-unvoiced `drop_descrip`: `5`.
- `102130:couple_encourage:0/1` deterministically route to client `link1/link2`.
- `102134:vote:0` is the generic source placeholder `拉票描述`; it is preserved as `NON_DIALOGUE_PLACEHOLDER` rather than counted as missing spoken dialogue.
- Canonical adjudication: `AZUR_LANE_ST_LOUIS_JP_AUDIO_RECONCILIATION_AUDIT.md`.

## Takao source-gap closure appendix

- JP performed-voice source readiness: `AUDIO_READY`.
- Dorm3D non-chat: `SUPPORTED_NOT_FOUND`.
- Island non-relationship: `SUPPORTED_PRESENT`; raw-Lua-only identity/behavior evidence is preserved rather than erased by the JSON conversion gap.
- New text records: Island unit profile and skin-description records where published; no monograph was edited.
- New mapped voiced records: `114`.
- New contexts: Island profile, appearance/skin, stroll placement, and behavior-feedback linkage.
- Regional implications: JSON/Lua extraction divergence is a source-layer issue, not evidence of censorship or a textual-authority change.
- Existing monograph claims potentially affected: performed-voice discussion and source-limitations/method sections only; no claim disposition was assigned.

The corpus is ready for Dorm3D/Island textual analysis and objective performed-voice source work **when the character-specific source bytes are actually published/retrievable**. Any character marked `AUDIO_PARTIAL` still requires explicit resolution of remaining text/audio joins; Bremerton is a distinct `AUDIO_READY`-mapping / `PUBLICATION_BLOCKED`-waveform case.

## Bremerton late-publication appendix

- Text/audio alignment readiness: `AUDIO_READY` — 101 mapped spoken utterances / 0 unresolved spoken; seven profile/drop-description fields are explicitly known unvoiced.
- Acquisition timestamp for the Bremerton bundle family: approximately `2026-08-23T18:58:22Z`, later than the earlier 311-bundle Drive publication/audit generated around `2026-08-23T04:36Z`.
- Required mapped source bundles: `cv-10324.b` SHA-256 `cc507128546ac676c142b171b8919104d3672f62910f9e3e4218cd39d4b3e75e` (92 mapped utterances) and `cv-10324-battle.b` SHA-256 `7cb946f5962bfe920b0111e093a70a04391309fad0110aeacd287fbe50c99161` (9 mapped utterances).
- The bundle catalog/technical probe proves those bytes existed in the late acquisition, but neither bundle is present in the currently published content-addressed Drive source-bundle tree and the mapped WAV derivative directory lacks published mapped children.
- Consequence: mapping readiness remains `AUDIO_READY`; performed-voice analytical readiness is separately `PUBLICATION_BLOCKED`. Do not infer acoustic/timing/pitch state from metadata alone.
- Canonical Bremerton publication-gap audit: `AZUR_LANE_BREMERTON_JP_AUDIO_PUBLICATION_GAP_AUDIT.md` (`1C56nvsyl8BRiJuZzelHRKGzNieiQ32m1`).

## Final verdict

`SOURCE_AUGMENTATION_COMPLETE_WITH_DOCUMENTED_LIMITATIONS`
