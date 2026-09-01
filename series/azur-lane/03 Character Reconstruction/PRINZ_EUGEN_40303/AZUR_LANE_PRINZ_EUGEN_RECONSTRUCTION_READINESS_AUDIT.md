---
series: AZUR_LANE
artifact_type: audit
scope: PRINZ_EUGEN_40303_R0_SOURCE_READINESS
generation: V1
status: canonical
scope_character: PRINZ_EUGEN_40303
semantic_authority: CN
source_build_id: AZL-2026-08-22-4cca5c24-cc8e9fdf
readiness_grade: B
readiness_score: 76.18
source_boundary: Pinned Prinz Eugen character-build 2.1.0 over AzurLaneData 4cca5c2437007b62d30a6235fcfc0c0203231378 and AzurLaneLuaScripts cc8e9fdf6a1a2e5d20c9a8ff6c0369832bb33336; CN-origin semantic authority with JP/EN/TW/KR regional witnesses; current Drive publication state audited separately
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
---

# Azur Lane — Prinz Eugen R0 Reconstruction Readiness Audit

## Verdict

**`PRINZ_EUGEN_R0_PASS_WITH_DERIVED_PUBLICATION_GAP`**

Prinz Eugen / 欧根亲王 / group `40303` clears the governing Grade-B threshold for a strong character reconstruction. The pinned build contains enough narrative, dialogue, social, relationship, interactive-skin, regional, Island, and JP voice evidence to support a substantial monograph with bounded C1–C3 extrapolation.

The current blocker is not corpus poverty. It is **Drive publication completeness**: the canonical manifest declares and hashes the full derived evidence pack, but the current published Analysis character folder exposes only the manifest/source-map/coverage layer plus audio. The human-readable CN narrative/dialogue/social/relationship/regional/Island artifacts required for R2+ close reading are not currently retrievable from Drive.

R0 therefore passes the character as a reconstruction target while **forbidding interpretive advancement from summary counts alone**.

## Locked corpus state

| Dimension | Locked value | Analytical consequence |
|---|---:|---|
| Readiness | **76.18 / Grade B** | strong monograph permitted once evidence text is directly readable |
| Linked narrative scenes | **127** | substantial sustained-context surface |
| Direct attributed narrative dialogue lines | **886** | large scene-level behavioral surface |
| Direct narrative dialogue characters | **22,838** | substantial speech quantity in narrative context |
| Contextual scene characters | **106,069** | scenes are large enough that target-only extraction would be unsafe |
| Dedicated character-memory chapters | **0 / NOT_FOUND** | no dedicated-memory anchor; R2 must derive anchors from ordinary narrative clusters |
| Character dialogue records | **125** | broad short-form state coverage |
| Base-skin source layer | **31** | baseline self-presentation available |
| Non-base skin source layer | **94** | unusually broad context variation; strong skin/context controls required |
| Interactive-skin records | **25** | additional controlled interaction surface |
| Affinity | **7** | Commander relationship transition visible |
| Oath | **1** | explicit committed/intimate state visible |
| Combat | **11** | operational speech surface |
| Relationship-specific | **4** | named-peer relation evidence present |
| Social threads | **17** | 14 Juustagram + 1 Fleet Chat plus additional social records in the normalized build |
| Direct interlocutor entities | **114** | strong potential correction to Commander-only interpretation |
| Explicit relationship entities | **5** | targeted relationship modeling possible |
| Social interlocutor entities | **44** | useful low-stakes/social correction |
| Narrative co-occurring entities | **256** | broad ensemble exposure |
| Commander-facing character records | **99 / 125 = 79.2%** | major `COMMANDER_HEAVY` sampling warning |
| Regional alignment candidates | **5,902** | broad five-locale comparison surface |
| Regional complete records | **5,150** | strong structural cross-region coverage |
| Regional structural gaps | **752 / 12.74%** | material narrative-alignment caution |
| Weighted regional coverage | **92.61%** | multilingual speech analysis is well supported |
| Character-text alignment gaps | **1 / 125** | character-text crosswalk is nearly complete |
| Social alignment gaps | **0 / 99** | social crosswalk structurally complete |
| Island non-relationship evidence | **35 records / 7 per locale** | identity/behavior metadata available; no character-linked Island scenes |
| Dorm3D non-chat | **SUPPORTED_NOT_FOUND** | explicit searched absence |
| JP mapped spoken utterances | **114** | large performed-voice surface |
| JP known-unvoiced text slots | **9** | do not classify as missing audio |
| JP unresolved expected spoken slot | **1** | R10 cannot claim full text-side closure yet |
| Non-text/review audio asset | **1** | keep separate from spoken model |
| Literal Drive WAV publication | **PRESENT** | direct waveform work is technically possible later |

## Identity and source closure

Identity is clean:

- canonical ship group: `40303`;
- skins/story actors: `403030`–`403038`;
- rejected ambiguity set: empty.

No Enterprise-style identity quarantine is currently required.

The canonical upstream source lock remains:

- `AzurLaneTools/AzurLaneData` @ `4cca5c2437007b62d30a6235fcfc0c0203231378`;
- `AzurLaneTools/AzurLaneLuaScripts` @ `cc8e9fdf6a1a2e5d20c9a8ff6c0369832bb33336`.

CN is semantic authority in `origin` mode. JP, EN, TW, and KR remain independent regional witnesses and must not be silently harmonized into a synthetic master voice.

## Source-status closure

`PRESENT`:

- narrative story;
- base-skin dialogue;
- non-base skin dialogue;
- interactive-skin capability;
- affinity;
- oath;
- combat;
- relationship-specific dialogue;
- Juustagram;
- Fleet Chat;
- five-locale regional alignment;
- Island non-relationship identity/behavior records;
- mapped JP performed-voice derivatives.

`NOT_FOUND`:

- dedicated character memory;
- Dorm3D chat;
- Island relationship evidence.

`SUPPORTED_NOT_FOUND`:

- Dorm3D non-chat.

The absence of a dedicated character-memory sequence is analytically meaningful: Prinz Eugen's reconstruction must be triangulated from recurring ordinary narrative contexts rather than treating a character-focused side story as the privileged explanatory spine.

## Composition warnings

### `COMMANDER_HEAVY`

99 of 125 normalized character-dialogue records are Commander-facing. Commander intimacy therefore cannot define the global personality model. Global claims require disproportionate weighting from the 127 narrative scenes, named-peer dialogue, 17 social threads, relationship-specific records, combat/professional contexts, and Island evidence.

### `MANY_UNALIGNED_RECORDS`

752 of 5,902 regional alignment candidates contain structural gaps. These are concentrated in narrative; the character-text and social layers are much cleaner. Structural absence must not be reinterpreted as censorship or semantic contradiction without separate evidence.

### Skin volume

94 non-base skin records and 25 interactive-skin records create a large context-sensitive surface. This is analytically valuable but dangerous: costume/activity/intimacy states are probes, not a chronological developmental sequence by default.

## Current Drive publication audit

The canonical `CHARACTER_MANIFEST.json` declares **95 output files** and hashes the following human-readable analytical inputs:

- `PRINZ_EUGEN_CN_CHARACTER_DIALOGUE_LEDGER.md`
- `PRINZ_EUGEN_CN_NARRATIVE_SCENE_CORPUS.md`
- `PRINZ_EUGEN_CN_NARRATIVE_SCENE_CORPUS_RAW.md`
- `PRINZ_EUGEN_CN_SCENE_INDEX.md`
- `PRINZ_EUGEN_CN_SOCIAL_RECONSTRUCTION.md`
- `PRINZ_EUGEN_RELATIONSHIP_EVIDENCE_INDEX.md`
- `PRINZ_EUGEN_REGIONAL_CROSSWALK.md`
- `PRINZ_EUGEN_ISLAND_EVIDENCE_CN.md`
- corresponding JP/EN/TW/KR Island witnesses
- `PRINZ_EUGEN_JP_AUDIO_INDEX.md`

The current Drive Analysis folder does **not** expose the first nine textual/relationship/regional artifacts as retrievable file objects. The audio-index/manifest/listening-derivative layer is separately published under Primary Sources and literal WAV files are directly accessible.

This is recorded as a publication-state gap, not as evidence that the underlying derived build failed: the manifest hashes and coverage declarations prove those outputs existed at build time.

## Reconstruction gates

- [x] identity resolved unambiguously to group `40303`;
- [x] canonical source commits locked;
- [x] Grade-B readiness established;
- [x] narrative, dialogue, social, relationship, regional, Island, and audio systems audited structurally;
- [x] 127 linked narrative scenes declared by the canonical build;
- [x] 114 mapped JP spoken utterances and literal WAV publication verified;
- [x] dedicated reconstruction home created under `03 Character Reconstruction/PRINZ_EUGEN_40303/`;
- [ ] manifest-declared CN narrative/dialogue/social human-readable artifacts are directly retrievable from Drive;
- [ ] relationship evidence index is directly retrievable from Drive;
- [ ] regional crosswalk is directly retrievable from Drive;
- [ ] Island evidence text is directly retrievable from Drive;
- [ ] R2 anchor reading completed;
- [ ] R3+ behavioral synthesis completed;
- [ ] JP performed-voice interpretation completed.

The first four open items block source-grounded **interpretive** R2+ work but do not invalidate R0 readiness.

## R0 conclusion

> **Proceed with Prinz Eugen as a Grade-B full-reconstruction target, but do not infer her psychology from coverage metadata, filenames, fandom archetypes, or audio filenames. Restore/directly expose the manifest-declared derived evidence text, then begin R2 with sustained CN narrative context and use Commander-facing, skin, and regional material as controlled secondary layers.**
