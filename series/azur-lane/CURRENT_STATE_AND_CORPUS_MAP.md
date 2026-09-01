---
series: AZUR_LANE
artifact_type: corpus_map
scope: FULL_CORPUS
generation: FINAL_REMEDIATION_V1
status: canonical
source_boundary: "Derived analytical/evidence corpus over extracted Azur Lane game-client sources"
supersedes: null
superseded_by: null
do_not_use_as_current_authority: false
---

# Azur Lane Current State and Corpus Map

This is the single current first-read entrypoint for the active, reproducible Azur Lane derived analytical/evidence corpus. Analysis contains normalized/extracted evidence, mappings, methods, audits, and monographs; Primary Sources contains original JP audio/client-only source assets and minimal acquisition provenance. Pinned Git repositories remain source provenance.

## Corpus identity

- Stable series identifier: `AZUR_LANE`
- Build ID: `AZL-2026-08-22-4cca5c24-cc8e9fdf`
- Build timestamp: `2026-08-23T04:36:09.753394Z`
- Pipeline version: `0.3.0`
- Normalized schema: `normalized-2.1.0`
- Social entity schema: `social-entity-1.0.0`
- Alignment-gap schema: `alignment-gap-1.0.0`
- Source-status model: `source-status-2.0.0`
- Readiness model: `readiness-2.1.0`
- Semantic regional-review model: `regional-semantic-rules-1.0.0`
- Locales: `CN, JP, EN, TW, KR`
- Release recommendation: **READY_WITH_DOCUMENTED_LIMITATIONS**

## Governing source policy

`AzurLaneTools/AzurLaneData` is the primary structured extraction. `AzurLaneTools/AzurLaneLuaScripts` is the raw Lua semantic/conversion witness. In `origin` mode, CN is the originating textual authority; JP, EN, TW, and KR remain parallel regional witnesses. Records are never silently translated, harmonized, or filled from the Story Player, wiki, or other community databases.

## Current upstream source lock

| Repository | URL | Commit SHA | Build timestamp | Locales |
|---|---|---|---|---|
| AzurLaneData | https://github.com/AzurLaneTools/AzurLaneData.git | `4cca5c2437007b62d30a6235fcfc0c0203231378` | `2026-08-23T04:36:09.753394Z` | CN, JP, EN, TW, KR |
| AzurLaneLuaScripts | https://github.com/AzurLaneTools/AzurLaneLuaScripts.git | `cc8e9fdf6a1a2e5d20c9a8ff6c0369832bb33336` | `2026-08-23T04:36:09.753394Z` | CN, JP, EN, TW, KR |

## Current supported systems

| Source system | Status | Source families |
|---|---|---|
| story_scenario | SUPPORTED | GameCfg/story*.json, gamecfg/story* |
| memory_grouping | SUPPORTED | memory_group, memory_template |
| character_skin_dialogue | SUPPORTED | ship_skin_words, ship_skin_words_extra, ship_skin_words_add |
| identity | SUPPORTED | ship_data_statistics, ship_data_template, ship_skin_template, nation, name_code |
| special_secretary | SUPPORTED | secretary_special_ship |
| juustagram | SUPPORTED | activity_ins_template, activity_ins_npc_template, activity_ins_language |
| fleet_chat | SUPPORTED | activity_ins_chat_group, activity_ins_chat_language |
| dorm3d_chat | SUPPORTED | dorm3d_ins_chat_group, dorm3d_ins_chat_language |
| island_relationship_trigger | SUPPORTED | island_couple_word |
| dorm3d_non_chat | SUPPORTED | dorm3d_dialogue_group, GameCfg/story*.json |
| island_non_relationship | SUPPORTED | island_chara_template, island_unit_character, island_strollnpc, island_task, GameCfg/story*.json (ISLAND*), raw Lua witness |
| jp_performed_voice | SUPPORTED | direct JP client acquisition, Primary Sources content-addressed audio archive, per-character mappings/derivatives |

## Known unsupported systems

- None among the currently declared source systems; current JP performed-voice acquisition and mapping status is reported separately below.

## Generated character corpora

The build path and Drive archival home are distinct routing surfaces. The first is used by the reproducible local pipeline; the second is the published archive.

| Character | Group ID | Build/repository path | Drive archival home | Grade | Score | Major coverage warnings |
|---|---:|---|---|---:|---:|---|
| Akagi | 30701 | [`derived/characters/AKAGI_30701/`](derived/characters/AKAGI_30701/) | [`02 Extracted Character Corpora/AKAGI_30701/`](../../provenance/drive-artifacts/DRIVE_ARTIFACT_REFERENCE_INDEX.md#drive-ref-1ea4e02c950e61e8) | A | 87.39 | COMMANDER_HEAVY |
| Atago | 30312 | [`derived/characters/ATAGO_30312/`](derived/characters/ATAGO_30312/) | [`02 Extracted Character Corpora/ATAGO_30312/`](../../provenance/drive-artifacts/DRIVE_ARTIFACT_REFERENCE_INDEX.md#drive-ref-82dc87e927405711) | A | 83.83 | COMMANDER_HEAVY, MANY_UNALIGNED_RECORDS |
| Ayanami | 30105 | [`derived/characters/AYANAMI_30105/`](derived/characters/AYANAMI_30105/) | [`02 Extracted Character Corpora/AYANAMI_30105/`](../../provenance/drive-artifacts/DRIVE_ARTIFACT_REFERENCE_INDEX.md#drive-ref-ad449f249922c56d) | A | 86.94 | COMMANDER_HEAVY |
| Baltimore | 10316 | [`derived/characters/BALTIMORE_10316/`](derived/characters/BALTIMORE_10316/) | [`02 Extracted Character Corpora/BALTIMORE_10316/`](../../provenance/drive-artifacts/DRIVE_ARTIFACT_REFERENCE_INDEX.md#drive-ref-ece1e5967dc738e1) | A | 82.91 | COMMANDER_HEAVY |
| Bremerton | 10324 | [`derived/characters/BREMERTON_10324/`](derived/characters/BREMERTON_10324/) | [`02 Extracted Character Corpora/BREMERTON_10324/`](../../provenance/drive-artifacts/DRIVE_ARTIFACT_REFERENCE_INDEX.md#drive-ref-02ccc61fd01982d7) | A | 87.75 | COMMANDER_HEAVY |
| Cheshire | 29903 | [`derived/characters/CHESHIRE_29903/`](derived/characters/CHESHIRE_29903/) | [`02 Extracted Character Corpora/CHESHIRE_29903/`](../../provenance/drive-artifacts/DRIVE_ARTIFACT_REFERENCE_INDEX.md#drive-ref-635b6fa865316589) | B | 61.21 | COMMANDER_HEAVY, SKIN_HEAVY, MANY_UNALIGNED_RECORDS |
| Enterprise | 10706 | [`derived/characters/ENTERPRISE_10706/`](derived/characters/ENTERPRISE_10706/) | [`02 Extracted Character Corpora/ENTERPRISE_10706/`](../../provenance/drive-artifacts/DRIVE_ARTIFACT_REFERENCE_INDEX.md#drive-ref-c21f8413ad5dfe3d) | B | 72.48 | COMMANDER_HEAVY, IDENTITY_AMBIGUITY, MANY_UNALIGNED_RECORDS |
| Formidable | 20705 | [`derived/characters/FORMIDABLE_20705/`](derived/characters/FORMIDABLE_20705/) | [`02 Extracted Character Corpora/FORMIDABLE_20705/`](../../provenance/drive-artifacts/DRIVE_ARTIFACT_REFERENCE_INDEX.md#drive-ref-ad5afd75a5a8e7d0) | B | 73.87 | COMMANDER_HEAVY, MANY_UNALIGNED_RECORDS |
| Kaga | 30702 | [`derived/characters/KAGA_30702/`](derived/characters/KAGA_30702/) | [`02 Extracted Character Corpora/KAGA_30702/`](../../provenance/drive-artifacts/DRIVE_ARTIFACT_REFERENCE_INDEX.md#drive-ref-870d5e992bb80b23) | B | 70.93 | COMMANDER_HEAVY, MANY_UNALIGNED_RECORDS |
| Kirishima | 30404 | [`derived/characters/KIRISHIMA_30404/`](derived/characters/KIRISHIMA_30404/) | [`02 Extracted Character Corpora/KIRISHIMA_30404/`](../../provenance/drive-artifacts/DRIVE_ARTIFACT_REFERENCE_INDEX.md#drive-ref-535247ad88637dca) | C | 52.73 | COMMANDER_HEAVY |
| Le Malin | 90111 | [`derived/characters/LE_MALIN_90111/`](derived/characters/LE_MALIN_90111/) | [`02 Extracted Character Corpora/LE_MALIN_90111/`](../../provenance/drive-artifacts/DRIVE_ARTIFACT_REFERENCE_INDEX.md#drive-ref-463572ea7630475b) | A | 82.83 | COMMANDER_HEAVY |
| Nagato | 30505 | [`derived/characters/NAGATO_30505/`](derived/characters/NAGATO_30505/) | [`02 Extracted Character Corpora/NAGATO_30505/`](../../provenance/drive-artifacts/DRIVE_ARTIFACT_REFERENCE_INDEX.md#drive-ref-701b7f4582381169) | B | 71.92 | COMMANDER_HEAVY, MANY_UNALIGNED_RECORDS |
| Owari | 30513 | [`derived/characters/OWARI_30513/`](derived/characters/OWARI_30513/) | [`02 Extracted Character Corpora/OWARI_30513/`](../../provenance/drive-artifacts/DRIVE_ARTIFACT_REFERENCE_INDEX.md#drive-ref-1bbbffbf90d71184) | B | 62.05 | COMMANDER_HEAVY |
| Prinz Eugen | 40303 | [`derived/characters/PRINZ_EUGEN_40303/`](derived/characters/PRINZ_EUGEN_40303/) | [`02 Extracted Character Corpora/PRINZ_EUGEN_40303/`](../../provenance/drive-artifacts/DRIVE_ARTIFACT_REFERENCE_INDEX.md#drive-ref-dca8c7589eb914cf) | B | 76.18 | COMMANDER_HEAVY, MANY_UNALIGNED_RECORDS |
| St. Louis | 10213 | [`derived/characters/ST_LOUIS_10213/`](derived/characters/ST_LOUIS_10213/) | [`02 Extracted Character Corpora/ST_LOUIS_10213/`](../../provenance/drive-artifacts/DRIVE_ARTIFACT_REFERENCE_INDEX.md#drive-ref-78eab904fa582168) | C | 57.3 | COMMANDER_HEAVY, SKIN_HEAVY, MANY_UNALIGNED_RECORDS |
| Taihou | 30707 | [`derived/characters/TAIHOU_30707/`](derived/characters/TAIHOU_30707/) | [`02 Extracted Character Corpora/TAIHOU_30707/`](../../provenance/drive-artifacts/DRIVE_ARTIFACT_REFERENCE_INDEX.md#drive-ref-3ec08c38a7f93402) | A | 86.89 | COMMANDER_HEAVY, MANY_UNALIGNED_RECORDS |
| Takao | 30311 | [`derived/characters/TAKAO_30311/`](derived/characters/TAKAO_30311/) | [`02 Extracted Character Corpora/TAKAO_30311/`](../../provenance/drive-artifacts/DRIVE_ARTIFACT_REFERENCE_INDEX.md#drive-ref-17bc769270fe14bc) | A | 89.21 | COMMANDER_HEAVY |

> **Baltimore analytical identity quarantine:** the R2 full-scene reconstruction pass found that 9 of the 81 nominal Baltimore direct-presence scenes are false actor joins (7 contextually Musashi / 73 dialogue records; 2 contextually Honoka / 6 dialogue records). Current Baltimore analysis therefore uses 72 clean direct-presence scenes / 276 clean narrative dialogue records. The canonical frozen V1 monograph, canonical R5 adversarial validation, R6 relationship-state synthesis, R7 multilingual speech profile, R8 novel-situation simulation audit, JP quantitative performed-voice profile, claim-revision ledger, and final promotion audit all retain that quarantine. The published readiness score **82.91** remains the frozen pre-remediation pipeline score until the actor mapping and generated manifests are rebuilt; it is not manually recomputed here.

## Drive archival routing

- [Canonical global Drive index — `MANGA_ANIME_DRIVE_INDEX.md`](../../governance/MANGA_ANIME_CORPUS_INDEX.md)
- [Azur Lane archival root](.)
- [Azur Lane Primary Sources root](../../provenance/drive-artifacts/DRIVE_ARTIFACT_REFERENCE_INDEX.md#drive-ref-d9f9a608b7e23f8f)
- Local build paths begin at `derived/characters/`; published Drive evidence paths begin at `02 Extracted Character Corpora/`.
- Derived character models and monographs route through `03 Character Reconstruction/`.

## Current character reconstruction authorities

- [Prinz Eugen reconstruction folder](03%20Character%20Reconstruction/PRINZ_EUGEN_40303) — Drive `1K0vEjel5HUBHSkT8idbCilxkqTsMEPOY`; **active-provisional reconstruction initiated**. Grade B / 76.18. R0/R1 routing is complete, and the former derived-evidence publication gate is closed. The complete 127-scene CN R2 anchor reading may proceed; no character monograph exists yet.
- [Prinz Eugen character current-state map — `CURRENT_STATE_AND_CORPUS_MAP.md`](03%20Character%20Reconstruction/PRINZ_EUGEN_40303/CURRENT_STATE_AND_CORPUS_MAP.md) — Drive `1QfM9hy2HvTMAeAYLDSHKhnOq7GrSEyHI`; first-read authority for the active reconstruction.
- [Prinz Eugen R0 readiness audit — `AZUR_LANE_PRINZ_EUGEN_RECONSTRUCTION_READINESS_AUDIT.md`](03%20Character%20Reconstruction/PRINZ_EUGEN_40303/AZUR_LANE_PRINZ_EUGEN_RECONSTRUCTION_READINESS_AUDIT.md) — Drive `1awDgUksPTcEqNBRr7yTuWXRmAeWlhW7N`; verdict `PRINZ_EUGEN_R0_PASS_WITH_DERIVED_PUBLICATION_GAP`.
- [Prinz Eugen R1 structural evidence map — `AZUR_LANE_PRINZ_EUGEN_RECONSTRUCTION_EVIDENCE_MAP.md`](03%20Character%20Reconstruction/PRINZ_EUGEN_40303/AZUR_LANE_PRINZ_EUGEN_RECONSTRUCTION_EVIDENCE_MAP.md) — Drive `1dzlgquUJ67fg3NLEx52jdeGsxe3ANadw`; verdict `PRINZ_EUGEN_R1_STRUCTURAL_MAP_PASS_INTERPRETIVE_ANCHORS_OPEN`.
- [Prinz Eugen derived-evidence publication audit — `AZUR_LANE_PRINZ_EUGEN_DERIVED_EVIDENCE_PUBLICATION_AUDIT.md`](03%20Character%20Reconstruction/PRINZ_EUGEN_40303/AZUR_LANE_PRINZ_EUGEN_DERIVED_EVIDENCE_PUBLICATION_AUDIT.md) — Drive `1asdtto9Amn0gVBMlalz1htFBOhMDSgP2`; retained as historical provenance for the former partial-publication state. Current corpus-wide closure is recorded in the publication-completeness audit below.
- Prinz Eugen JP voice state: **114 mapped spoken WAVs / 9 known-unvoiced text slots / 1 expected spoken slot unresolved / 115 Drive-readback-verified WAVs including one non-text review asset**. Acoustic/performance interpretation remains separate from semantic reconstruction.

- [Takao — `03 Character Reconstruction/TAKAO_30311/AZUR_LANE_TAKAO_CHARACTER_MONOGRAPH.md`](03%20Character%20Reconstruction/TAKAO_30311/AZUR_LANE_TAKAO_CHARACTER_MONOGRAPH.md) — Drive `1tGmkZfD2xkjQiLyFT5OvxSgR2i4wNgG8`; **canonical frozen V1**.
- [Takao reconstruction folder](03%20Character%20Reconstruction/TAKAO_30311) — Drive `1JF4tqVQsmBEwtCyt5upjvMJ5PpmRC58q`.
- [Takao JP voice-performance specialist — `AZUR_LANE_TAKAO_JP_VOICE_PERFORMANCE_PROFILE.md`](03%20Character%20Reconstruction/TAKAO_30311/AZUR_LANE_TAKAO_JP_VOICE_PERFORMANCE_PROFILE.md) — Drive `1fBUniM0VmjuqBmMfAppb6hqrR-rg_p1m`; canonical for JP acoustic/timing/state-transition realization.
- [Takao JP voice → monograph impact ledger — `AZUR_LANE_TAKAO_JP_VOICE_MONOGRAPH_IMPACT_LEDGER.md`](03%20Character%20Reconstruction/TAKAO_30311/AZUR_LANE_TAKAO_JP_VOICE_MONOGRAPH_IMPACT_LEDGER.md) — Drive `1FioXzW6Pl7qUfr8oHW88NWox9FCreWJi`; canonical claim-transition record.
- [Takao V1 promotion audit — `AZUR_LANE_TAKAO_CHARACTER_MONOGRAPH_PROMOTION_AUDIT.md`](03%20Character%20Reconstruction/TAKAO_30311/AZUR_LANE_TAKAO_CHARACTER_MONOGRAPH_PROMOTION_AUDIT.md) — Drive `17zXXqowMXcFjB6x829xUeVsQRsVxsdWu`; verdict `PROMOTE_TO_CANONICAL_V1`.
- [Baltimore - `03 Character Reconstruction/BALTIMORE_10316/AZUR_LANE_BALTIMORE_CHARACTER_MONOGRAPH.md`](03%20Character%20Reconstruction/BALTIMORE_10316/AZUR_LANE_BALTIMORE_CHARACTER_MONOGRAPH.md) - Drive `149ZmLNb9ojnApRbBYfeoJfrKVtRHJ0OCWz5U2rSqSwE`; **canonical frozen V1 integrated reconstruction authority**. Final promotion verdict `BALTIMORE_CHARACTER_MONOGRAPH_V1_PROMOTION_PASS` / `PROMOTE_TO_CANONICAL_V1`; R5-R8, multilingual text, and the canonical quantitative JP performed-voice layer are integrated. C4-C5 abstention, ear-dependent timbre OPEN, the nine-scene identity quarantine, and frozen 82.91 pre-remediation score remain explicit boundaries.
- [Baltimore reconstruction folder](03%20Character%20Reconstruction/BALTIMORE_10316) - Drive `1ysfQEMeWC-FlxDKuPvytX8J5quaPRGw0`; canonical V1 reconstruction through claim integration and final promotion audit.
- [Baltimore character current-state map — `CURRENT_STATE_AND_CORPUS_MAP.md`](03%20Character%20Reconstruction/BALTIMORE_10316/CURRENT_STATE_AND_CORPUS_MAP.md) — Drive `17VpD77LfvmSa4BaY72d3859zVIwwP9dGd_ZhAGGVGj0`; first-read authority for Baltimore reconstruction state.
- [Baltimore R3 longitudinal behavioral synthesis — `AZUR_LANE_BALTIMORE_LONGITUDINAL_BEHAVIORAL_SYNTHESIS.md`](03%20Character%20Reconstruction/BALTIMORE_10316/AZUR_LANE_BALTIMORE_LONGITUDINAL_BEHAVIORAL_SYNTHESIS.md) — Drive `1Sq8Mw0oagktET9MjyWq5MtKc5nIsBSy33uTIax4ssOs`; canonical R3 conditional behavioral architecture, verdict `BALTIMORE_R3_LONGITUDINAL_SYNTHESIS_PASS_WITH_IDENTITY_QUARANTINE_RETAINED`.
- [Baltimore R5 adversarial validation — `AZUR_LANE_BALTIMORE_ADVERSARIAL_VALIDATION_AUDIT.md`](03%20Character%20Reconstruction/BALTIMORE_10316/AZUR_LANE_BALTIMORE_ADVERSARIAL_VALIDATION_AUDIT.md) — Drive `1Xv1jClIwjWrTugrH411EQ8O4FdsCzkNtPC9xVLQsP4A`; canonical R5 falsification/claim-transition authority, verdict `BALTIMORE_R5_PASS_WITH_BOUNDED_REVISIONS_AND_IDENTITY_QUARANTINE_RETAINED`.
- [Baltimore R6 relationship-state synthesis — `AZUR_LANE_BALTIMORE_RELATIONSHIP_STATE_SYNTHESIS.md`](03%20Character%20Reconstruction/BALTIMORE_10316/AZUR_LANE_BALTIMORE_RELATIONSHIP_STATE_SYNTHESIS.md) — Drive `1rvcYT1N0ObvJUdvaTnTez3ExamI6UjvjJamK2esFz6g`; canonical R6 relationship modifier authority, verdict `BALTIMORE_R6_RELATIONSHIP_STATE_SYNTHESIS_PASS_WITH_STAGE_AND_INTERLOCUTOR_MODIFIERS_AND_IDENTITY_QUARANTINE_RETAINED`.
- [Baltimore R7 multilingual speech profile — `AZUR_LANE_BALTIMORE_MULTILINGUAL_SPEECH_PROFILE.md`](03%20Character%20Reconstruction/BALTIMORE_10316/AZUR_LANE_BALTIMORE_MULTILINGUAL_SPEECH_PROFILE.md) — Drive `1YwEv48seLhvZ7fl9ilx6k9doWO-O4fpCzdVXsyJrU-I`; canonical CN/JP/EN/TW/KR textual speech authority over 392 clean five-locale aligned Baltimore speech records, verdict `BALTIMORE_R7_MULTILINGUAL_SPEECH_PROFILE_PASS_WITH_PARALLEL_LOCALE_MODELS_AND_JP_ACOUSTIC_BOUNDARY_RETAINED`; textual locale authority remains distinct from the separate canonical JP performed-voice specialist.
- [Baltimore R8 novel-situation simulation audit — `AZUR_LANE_BALTIMORE_NOVEL_SITUATION_SIMULATION_AUDIT.md`](03%20Character%20Reconstruction/BALTIMORE_10316/AZUR_LANE_BALTIMORE_NOVEL_SITUATION_SIMULATION_AUDIT.md) — Drive `1r2xSjyaDFTvhrjJseBYvDY2ntlnEd3XyyMDJgGsgO0I`; canonical adversarial C1–C3 simulation-validation authority, verdict `BALTIMORE_R8_TEXTUAL_SIMULATION_PASS_WITH_RELATIONSHIP_AND_LOCALE_BOUNDARIES_RETAINED`; weakest-link confidence and calibrated C4–C5 abstention are mandatory.
- [Baltimore JP voice-performance specialist — `AZUR_LANE_BALTIMORE_JP_VOICE_PERFORMANCE_PROFILE.md`](03%20Character%20Reconstruction/BALTIMORE_10316/AZUR_LANE_BALTIMORE_JP_VOICE_PERFORMANCE_PROFILE.md) — Drive `1Qz1uSTjHs1gl2gEa9Mk3Nm35KTty4laEF0zLfKVPfJs`; canonical quantitative JP performed authority over 100/100 SHA-256-verified mapped WAV derivatives; verdict `BALTIMORE_JP_VOICE_PERFORMANCE_PROFILE_PASS_WITH_TWO_AXIS_ACOUSTIC_MODEL_AND_EAR_DEPENDENT_TIMBRE_OPEN`; ear-dependent timbre remains OPEN.
- [Baltimore V1 claim-revision ledger - `AZUR_LANE_BALTIMORE_CLAIM_REVISION_LEDGER.md`](03%20Character%20Reconstruction/BALTIMORE_10316/AZUR_LANE_BALTIMORE_CLAIM_REVISION_LEDGER.md) - Drive `1GwCoNS4BbanIOHDyVrQMmAhD5K0VCpdeQd9IUQq5RDg`; canonical claim-history authority, verdict `BALTIMORE_V1_CLAIM_INTEGRATION_PASS_WITH_C4_C5_AND_TIMBRE_BOUNDARIES_RETAINED`.
- [Baltimore V1 promotion audit - `AZUR_LANE_BALTIMORE_CHARACTER_MONOGRAPH_PROMOTION_AUDIT.md`](03%20Character%20Reconstruction/BALTIMORE_10316/AZUR_LANE_BALTIMORE_CHARACTER_MONOGRAPH_PROMOTION_AUDIT.md) - Drive `19BQQcMprDNGM11urlpTBFW-0Yrnyr7StfhSssTKkQ7k`; verdict `BALTIMORE_CHARACTER_MONOGRAPH_V1_PROMOTION_PASS` / `PROMOTE_TO_CANONICAL_V1`.
- [Taihou reconstruction folder](03%20Character%20Reconstruction/TAIHOU_30707) - Drive `1xNpglxJ9PzdyILP3_Ut3Lnwc0xX9Qg76`; **canonical frozen V1 textual/behavioral reconstruction through R9 promotion**. The in-place monograph is the preferred integrated V1 authority; the R9 claim-revision ledger preserves release-level transitions; the R9 promotion audit records `PROMOTE_TO_CANONICAL_V1`; R5/R6/R7/R8 remain canonical specialist authorities beneath it; R3 remains canonical longitudinal authority. JP performed voice remains a separate `OPEN_PARTIAL_SOURCE_MAPPING` track and is not part of the frozen V1 acoustic scope. Future substantive monograph integration requires V2 or an explicit superseding release.
- [Taihou character current-state map — `CURRENT_STATE_AND_CORPUS_MAP.md`](03%20Character%20Reconstruction/TAIHOU_30707/CURRENT_STATE_AND_CORPUS_MAP.md) — Drive `1y6azXpFlgBcWYesqxXRcbFkDL-m7et4gdb08yQWbzeU`; first-read authority for Taihou reconstruction state.
- [Taihou R0 readiness audit — `AZUR_LANE_TAIHOU_RECONSTRUCTION_READINESS_AUDIT.md`](03%20Character%20Reconstruction/TAIHOU_30707/AZUR_LANE_TAIHOU_RECONSTRUCTION_READINESS_AUDIT.md) — Drive `13dAuvS1BS80vB1RistnrvmYuFXywkgyBYRyCNRn-0Q8`; Grade A / 86.89; verdict `TAIHOU_R0_PASS_WITH_COMMANDER_HEAVY_REGIONAL_GAPS_DORM3D_REFERENCE_BOUNDARIES_AND_JP_AUDIO_PARTIAL`.
- [Taihou R1 evidence map — `AZUR_LANE_TAIHOU_RECONSTRUCTION_EVIDENCE_MAP.md`](03%20Character%20Reconstruction/TAIHOU_30707/AZUR_LANE_TAIHOU_RECONSTRUCTION_EVIDENCE_MAP.md) — Drive `1iDCkCzMASeolJse5xV8NXRiUgTgFIPVoaMmV2a7PPe4`; verdict `TAIHOU_R1_EVIDENCE_MAP_PASS_WITH_DORM3D_SEPARATION_AND_AUDIO_GATE_RETAINED`.
- [Taihou R2 memory deep reading — `AZUR_LANE_TAIHOU_CHARACTER_MEMORY_DEEP_READING.md`](03%20Character%20Reconstruction/TAIHOU_30707/AZUR_LANE_TAIHOU_CHARACTER_MEMORY_DEEP_READING.md) — Drive `1pZ4Ua-4E8uEBs355WZT5Mjpfu7nW9w_oco4j_NuOVBM`; verdict `TAIHOU_MEMORY_R2_PASS_WITH_TESTABLE_ATTACHMENT_SERVICE_AND_REJECTION_HYPOTHESES`.
- [Taihou R2 full narrative deep reading — `AZUR_LANE_TAIHOU_NARRATIVE_DEEP_READING.md`](03%20Character%20Reconstruction/TAIHOU_30707/AZUR_LANE_TAIHOU_NARRATIVE_DEEP_READING.md) — Drive `1Bd7snzqXC1pE9TU2ewGWb3UCCREbT0GsRCXgv_5_y-w`; verdict `TAIHOU_R2_FULL_NARRATIVE_PASS_WITH_SELECTIVE_BOUNDARY_OVERRIDE_PEER_COMPETENCE_AND_DUAL_ATTACHMENT_THREAT_MODEL`. The 28-scene CN pass revises generalized boundary-blindness and mechanically absolute exclusivity, preserves Commander-centered territoriality, and routes R3 to character dialogue/social/relationship/Dorm3D longitudinal testing. JP performed voice remains `AUDIO_PARTIAL` (151/217 mapped voiced slots; exhaustive acoustic closure blocked).
- [Taihou R3 longitudinal behavioral synthesis — `AZUR_LANE_TAIHOU_LONGITUDINAL_BEHAVIORAL_SYNTHESIS.md`](03%20Character%20Reconstruction/TAIHOU_30707/AZUR_LANE_TAIHOU_LONGITUDINAL_BEHAVIORAL_SYNTHESIS.md) — Drive `1fkvydZl7B4jYdHNXpAaoy1RCWn-fd5Jr0yAd0b4c6Gc`; canonical cross-context behavioral authority; verdict `TAIHOU_R3_LONGITUDINAL_SYNTHESIS_PASS_WITH_MUTUAL_INDISPENSABILITY_STATE_DEPENDENT_CARE_RECIPROCITY_AND_PERSISTENT_ATTACHMENT_INTRUSION`. Integrates 116 character-dialogue records, 25 normalized social sections, safely resolved named relationship evidence, and 125 routed CN Dorm3D groups as a separate established-intimacy stratum. R3 opens mutual indispensability as active-provisional, revises care-receiving as state-dependent, strengthens reassurance regulation and peer/professional competence, and preserves persistent Commander-specific access/tracking intrusion. JP performed voice remains partial/open.
- [Taihou canonical V1 character monograph - `AZUR_LANE_TAIHOU_CHARACTER_MONOGRAPH.md`](03%20Character%20Reconstruction/TAIHOU_30707/AZUR_LANE_TAIHOU_CHARACTER_MONOGRAPH.md) - Drive `1gyZInAjWxJnoKqpE2jaUFKu3EvqG_-AoacwnI-qOpzk`; **canonical / `archival_state: frozen_v1` preferred integrated authority**; final verdict `TAIHOU_V1_CHARACTER_MONOGRAPH_CANONICAL_WITH_RECIPROCAL_CONSEQUENTIALITY_RELATIONSHIP_CONDITIONING_FIVE_LOCALE_TEXTUAL_REALIZATION_R8_C3_BOUNDARIES_AND_JP_PERFORMED_VOICE_OPEN`. R5 bounds the higher-order model as reciprocal consequentiality with selective dependency engineering; R6 supplies relationship conditioning; R7 supplies five independent textual locale realizations; R8 validates bounded C3 simulation, cross-locale semantic invariance, ensemble-level style ablation, and OPEN-edge abstention. JP performed voice remains separate/open.
- [Taihou R5 adversarial validation audit — `AZUR_LANE_TAIHOU_ADVERSARIAL_VALIDATION_AUDIT.md`](03%20Character%20Reconstruction/TAIHOU_30707/AZUR_LANE_TAIHOU_ADVERSARIAL_VALIDATION_AUDIT.md) — Drive `1mOxxXBsI3R3Lh9mdlIpstQ4XtBtNaoro5DDVKKBYAvE`; **canonical R5 validation authority**; verdict `TAIHOU_R5_PASS_WITH_N5_REVISED_TO_RECIPROCAL_CONSEQUENTIALITY_HARD_REFUSAL_AND_HIGH_STAKES_EDGES_OPEN`. Applies formal H1–H10/N1–N5 claim transitions, preserves the state-weighting architecture, bounds reciprocal care/shared rivalry/generalized manipulation claims, and leaves acute hard refusal plus other high-stakes edges OPEN.
- [Taihou R6 relationship-state synthesis - `AZUR_LANE_TAIHOU_RELATIONSHIP_STATE_SYNTHESIS.md`](03%20Character%20Reconstruction/TAIHOU_30707/AZUR_LANE_TAIHOU_RELATIONSHIP_STATE_SYNTHESIS.md) - Drive `14CtqiHBvzMpMACaefNbvr7Gu2xGld7m31LT_82MN1kU`; **canonical R6 relationship-condition authority**; verdict `TAIHOU_R6_RELATIONSHIP_STATE_SYNTHESIS_PASS_WITH_NONCHRONOLOGICAL_COMMANDER_REGIMES_DYNAMIC_INTERLOCUTOR_FUNCTIONS_AND_RECIPROCAL_CONSEQUENTIALITY_BOUNDARIES`. Formalizes stable relationship history + momentary interlocutor function, CMD0-CMD3 nonchronological Commander regimes, cross-regime overlays, named interlocutor modifiers, and RR1-RR10.
- [Taihou R7 multilingual textual speech profile - `AZUR_LANE_TAIHOU_MULTILINGUAL_SPEECH_PROFILE.md`](03%20Character%20Reconstruction/TAIHOU_30707/AZUR_LANE_TAIHOU_MULTILINGUAL_SPEECH_PROFILE.md) - Drive `1XwnRVyZpMugaPu9m7qohWgLBq7RDlj6n9K7mmibddDY`; **canonical R7 regional textual-realization authority**; verdict `TAIHOU_R7_MULTILINGUAL_TEXTUAL_SPEECH_PASS_WITH_FIVE_INDEPENDENT_LOCALE_REGISTERS_CN_SEMANTIC_AUTHORITY_RELATIONSHIP_STATE_PRESERVATION_AND_PERFORMED_VOICE_SEPARATION`. Uses 2,541 stable alignment candidates plus a 247-record high-stability authored core; reconstructs CN/JP/EN/TW/KR independently, records JP/KR `dafeng7` dependency-framing shifts, EN `my Commander`/bounded rewrite tendencies, TW conservation value, and structural false-difference controls. JP performed voice remains separate/open.
- [Taihou R8 novel-situation simulation audit - `AZUR_LANE_TAIHOU_NOVEL_SITUATION_SIMULATION_AUDIT.md`](03%20Character%20Reconstruction/TAIHOU_30707/AZUR_LANE_TAIHOU_NOVEL_SITUATION_SIMULATION_AUDIT.md) - Drive `1noOs7XmHEtpiPzdX4xFV6tJJPl12yZYysgBy8BI2Tu4`; **canonical R8 constrained-simulation authority**; verdict `TAIHOU_R8_NOVEL_SITUATION_SIMULATION_PASS_WITH_BEHAVIOR_FIRST_C3_VALIDATION_CROSS_LOCALE_SEMANTIC_INVARIANCE_STYLE_ABLATION_ROBUSTNESS_AND_OPEN_EDGE_ABSTENTION`. Fourteen supported probes pass with no semantic failures; three are deliberately bounded; twelve forced-abstention controls preserve OPEN/C5 limits; `STYLE_ABLATION: PASS_AT_ENSEMBLE_LEVEL`.
- [Taihou V1 claim-revision ledger - `AZUR_LANE_TAIHOU_CLAIM_REVISION_LEDGER.md`](03%20Character%20Reconstruction/TAIHOU_30707/AZUR_LANE_TAIHOU_CLAIM_REVISION_LEDGER.md) - Drive `1XyX7tHOg7nnvfmCVPDPW6YitA6RIGAeqOtRCcIhuRvA`; **canonical R9 release-provenance authority**; verdict `TAIHOU_V1_CLAIM_REVISION_LEDGER_COMPLETE_WITH_R5_R8_TRANSITIONS_AND_OPEN_BOUNDARIES_PRESERVED`.
- [Taihou V1 promotion audit - `AZUR_LANE_TAIHOU_CHARACTER_MONOGRAPH_PROMOTION_AUDIT.md`](03%20Character%20Reconstruction/TAIHOU_30707/AZUR_LANE_TAIHOU_CHARACTER_MONOGRAPH_PROMOTION_AUDIT.md) - Drive `1jU8gKOsOrl01lNSoDWd1-H2GVfs2scYl90THFwtdH1Y`; **canonical R9 promotion authority**; verdict `TAIHOU_CHARACTER_MONOGRAPH_V1_PROMOTION_PASS` / disposition `PROMOTE_TO_CANONICAL_V1`; JP performed voice assessed as `SEPARATE_OPEN_TRACK` and not falsely declared complete.
- [Bremerton — `03 Character Reconstruction/BREMERTON_10324/AZUR_LANE_BREMERTON_CHARACTER_MONOGRAPH.md`](03%20Character%20Reconstruction/BREMERTON_10324/AZUR_LANE_BREMERTON_CHARACTER_MONOGRAPH.md) — Drive `1m20-jd9qoZ6DpmHKCljtQAZYC2ID97Yi`; **active-provisional Grade-A integrated authority**, readiness A / 87.75. R0–R8 textual reconstruction is complete and the JP quantitative performed-state model is usable at 100/101 directly measured mapped WAVs; frozen-V1 promotion is blocked by one exact missing waveform under the pre-declared 101/101 gate.
- [Bremerton reconstruction folder](03%20Character%20Reconstruction/BREMERTON_10324) — Drive `122p2KT0Gnwy-_OWN7QsFtx2unQ7PWyjY`; character current-state map `1r65ln_44I6YHPapi3RVpPAXhXwnPsai8`.
- [Bremerton reconstruction readiness audit — `AZUR_LANE_BREMERTON_RECONSTRUCTION_READINESS_AUDIT.md`](03%20Character%20Reconstruction/BREMERTON_10324/AZUR_LANE_BREMERTON_RECONSTRUCTION_READINESS_AUDIT.md) — Drive `1-GXlZSJJ24HOvnuyl1Dblq5aEhThXYnz`; `BREMERTON_R0_PASS`.
- [Bremerton character-memory deep reading — `AZUR_LANE_BREMERTON_CHARACTER_MEMORY_DEEP_READING.md`](03%20Character%20Reconstruction/BREMERTON_10324/AZUR_LANE_BREMERTON_CHARACTER_MEMORY_DEEP_READING.md) — Drive `1GCYDnXAx7kit6-x8Y0UkeJ-_DAqq6K_y`; canonical R1 over memory group 601 / IDs 3721–3727.
- [Bremerton narrative deep reading — `AZUR_LANE_BREMERTON_NARRATIVE_DEEP_READING.md`](03%20Character%20Reconstruction/BREMERTON_10324/AZUR_LANE_BREMERTON_NARRATIVE_DEEP_READING.md) — Drive `1B1yXCWTbJCURUpWX3ftoaQA2w1ycXbco`; canonical R2 with exact 41-record accounting (7 memory + 34 additional scenes).
- [Bremerton R5 adversarial validation — `AZUR_LANE_BREMERTON_ADVERSARIAL_VALIDATION_AUDIT.md`](03%20Character%20Reconstruction/BREMERTON_10324/AZUR_LANE_BREMERTON_ADVERSARIAL_VALIDATION_AUDIT.md) — Drive `1dT9Casg7Ls0lrFtlEEipgb1zp7eA1D-b`; `BREMERTON_R5_PASS_WITH_BOUNDED_REVISIONS`.
- [Bremerton R6 relationship-state synthesis — `AZUR_LANE_BREMERTON_RELATIONSHIP_STATE_SYNTHESIS.md`](03%20Character%20Reconstruction/BREMERTON_10324/AZUR_LANE_BREMERTON_RELATIONSHIP_STATE_SYNTHESIS.md) — Drive `1iaclA3l7bEc6hP1dRLv34Lm95-2IJjBC`.
- [Bremerton R7 multilingual speech profile — `AZUR_LANE_BREMERTON_MULTILINGUAL_SPEECH_PROFILE.md`](03%20Character%20Reconstruction/BREMERTON_10324/AZUR_LANE_BREMERTON_MULTILINGUAL_SPEECH_PROFILE.md) — Drive `1flcoa6-YgRguxzsY8HwcqYoyG2MZ28-9`; CN semantic authority with JP locale-specific register reconstruction.
- [Bremerton JP voice-performance specialist — `AZUR_LANE_BREMERTON_JP_VOICE_PERFORMANCE_PROFILE.md`](03%20Character%20Reconstruction/BREMERTON_10324/AZUR_LANE_BREMERTON_JP_VOICE_PERFORMANCE_PROFILE.md) — Drive `1EJ81rtLs-bBP_k6kV4u3fsAhHZjCOLtt`; **active-provisional quantitative JP performed-state authority**, 100/101 mapped WAVs directly retrieved, SHA-256 verified, and measured; one `103245:login:0` waveform and ear-dependent timbre remain OPEN.
- [Bremerton JP acoustic measurement matrix — `AZUR_LANE_BREMERTON_JP_VOICE_ACOUSTIC_METRICS.csv`](03%20Character%20Reconstruction/BREMERTON_10324/AZUR_LANE_BREMERTON_JP_VOICE_ACOUSTIC_METRICS.csv) — Drive `1-7DbKSRe_arXF9KcQdue5dAp1Do-KeIT`; fixed-procedure 101-row matrix with 100 measured rows and one explicit unavailable row.
- [Bremerton JP audio publication-gap audit — `AZUR_LANE_BREMERTON_JP_AUDIO_PUBLICATION_GAP_AUDIT.md`](03%20Character%20Reconstruction/BREMERTON_10324/AZUR_LANE_BREMERTON_JP_AUDIO_PUBLICATION_GAP_AUDIT.md) — Drive `1C56nvsyl8BRiJuZzelHRKGzNieiQ32m1`; **historical provenance / superseded as current authority**; the former broad publication gap has narrowed to one mapped WAV.
- [Bremerton R8 novel-situation simulation audit — `AZUR_LANE_BREMERTON_NOVEL_SITUATION_SIMULATION_AUDIT.md`](03%20Character%20Reconstruction/BREMERTON_10324/AZUR_LANE_BREMERTON_NOVEL_SITUATION_SIMULATION_AUDIT.md) — Drive `1TQE-Nac0d7GFf9gb57aBxg2Tgz5yGz0V`; `BREMERTON_R8_TEXTUAL_SIMULATION_PASS`.
- [Bremerton claim-revision ledger — `AZUR_LANE_BREMERTON_CLAIM_REVISION_LEDGER.md`](03%20Character%20Reconstruction/BREMERTON_10324/AZUR_LANE_BREMERTON_CLAIM_REVISION_LEDGER.md) — Drive `1pcphqnei-MuE16IFXVx14qSk7h80xmvt`.
- [Bremerton promotion audit — `AZUR_LANE_BREMERTON_CHARACTER_MONOGRAPH_PROMOTION_AUDIT.md`](03%20Character%20Reconstruction/BREMERTON_10324/AZUR_LANE_BREMERTON_CHARACTER_MONOGRAPH_PROMOTION_AUDIT.md) — Drive `1hdGLJeIsmvAHSqeqF3jF4i-LAuJ_klFT`; verdict `BREMERTON_CHARACTER_MONOGRAPH_V1_PROMOTION_BLOCKED_ONE_WAVEFORM_SHORT_OF_FROZEN_GATE`.
- [St. Louis — `03 Character Reconstruction/ST_LOUIS_10213/AZUR_LANE_ST_LOUIS_CHARACTER_MONOGRAPH.md`](03%20Character%20Reconstruction/ST_LOUIS_10213/AZUR_LANE_ST_LOUIS_CHARACTER_MONOGRAPH.md) — Drive `1DaLYt7EKtwPb2tcwX3PsKMDbvTN4c8-j`; **canonical constrained frozen V1**, Grade C / 57.3; substantial constrained simulation authority with explicit high-stakes limits.
- [St. Louis reconstruction readiness audit — `AZUR_LANE_ST_LOUIS_RECONSTRUCTION_READINESS_AUDIT.md`](03%20Character%20Reconstruction/ST_LOUIS_10213/AZUR_LANE_ST_LOUIS_RECONSTRUCTION_READINESS_AUDIT.md) — Drive `1i7APiq5-Lbc8nTfuwp6bkJFzTwvOxsQD`; verdict `ST_LOUIS_MONOGRAPH_BUILD_APPROVED_CONSTRAINED_SCOPE`.
- [St. Louis R5 adversarial validation — `AZUR_LANE_ST_LOUIS_ADVERSARIAL_VALIDATION_AUDIT.md`](03%20Character%20Reconstruction/ST_LOUIS_10213/AZUR_LANE_ST_LOUIS_ADVERSARIAL_VALIDATION_AUDIT.md) — Drive `1kQD8RyunZJD49ULTfgaeZg_DBNZVAYoy`; verdict `ST_LOUIS_R5_PASS_WITH_BOUNDED_REVISIONS`.
- [St. Louis R6 relationship synthesis — `AZUR_LANE_ST_LOUIS_RELATIONSHIP_STATE_SYNTHESIS.md`](03%20Character%20Reconstruction/ST_LOUIS_10213/AZUR_LANE_ST_LOUIS_RELATIONSHIP_STATE_SYNTHESIS.md) — Drive `1FaEbzQnTxEt77ttRcH_b6GSo_uxACBCW`; canonical for Helena/Honolulu/Boise and Commander-state asymmetries.
- [St. Louis R7 multilingual speech profile — `AZUR_LANE_ST_LOUIS_MULTILINGUAL_SPEECH_PROFILE.md`](03%20Character%20Reconstruction/ST_LOUIS_10213/AZUR_LANE_ST_LOUIS_MULTILINGUAL_SPEECH_PROFILE.md) — Drive `1Na-rKs2MOTj12ZmhMej25w5s8LPDi3e-`; CN semantic authority with JP locale-specific register reconstruction.
- [St. Louis JP audio reconciliation — `AZUR_LANE_ST_LOUIS_JP_AUDIO_RECONCILIATION_AUDIT.md`](03%20Character%20Reconstruction/ST_LOUIS_10213/AZUR_LANE_ST_LOUIS_JP_AUDIO_RECONCILIATION_AUDIT.md) — Drive `1CqxvvliInUzWHf1VBbPh3yhk2r9spkN-`; `AUDIO_READY`, 71/71 spoken mappings, 0 unresolved spoken.
- [St. Louis JP voice-performance specialist — `AZUR_LANE_ST_LOUIS_JP_VOICE_PERFORMANCE_PROFILE.md`](03%20Character%20Reconstruction/ST_LOUIS_10213/AZUR_LANE_ST_LOUIS_JP_VOICE_PERFORMANCE_PROFILE.md) — Drive `11VBbFih9_TJSQIX6ySXcZSNRBv8rgjK-`; canonical for JP acoustic/timing/state-transition realization.
- [St. Louis monograph impact ledger — `AZUR_LANE_ST_LOUIS_MONOGRAPH_IMPACT_LEDGER.md`](03%20Character%20Reconstruction/ST_LOUIS_10213/AZUR_LANE_ST_LOUIS_MONOGRAPH_IMPACT_LEDGER.md) — Drive `17QrZv-WEfyt9DIM-HXz34P1TvuuyOqtM`; canonical claim-transition record.
- [St. Louis promotion audit — `AZUR_LANE_ST_LOUIS_CHARACTER_MONOGRAPH_PROMOTION_AUDIT.md`](03%20Character%20Reconstruction/ST_LOUIS_10213/AZUR_LANE_ST_LOUIS_CHARACTER_MONOGRAPH_PROMOTION_AUDIT.md) — Drive `1T9JEBI3qUunzC4Z6-fj327kqTsnJdTnT`; verdict `PROMOTE_TO_CANONICAL_CONSTRAINED_V1`.
- [St. Louis acoustic measurement matrix — `ST_LOUIS_JP_ACOUSTIC_MEASUREMENT_MATRIX.csv`](03%20Character%20Reconstruction/ST_LOUIS_10213/ST_LOUIS_JP_ACOUSTIC_MEASUREMENT_MATRIX.csv) — Drive `1O7ATkjdEX9CWo01-Opyn3nW0v6PlWNY9`; 71-line fixed-procedure evidence matrix.
- [St. Louis reconstruction folder](03%20Character%20Reconstruction/ST_LOUIS_10213) — Drive `18QiLSV6PhZbD1A95FBIEGG2Kk_7d9111`.
- The Takao, St. Louis, Baltimore, and **Taihou** monographs are frozen current reconstruction authorities for their declared scopes. Bremerton remains a Grade-A **active-provisional** reconstruction authority with R0-R8 textual/behavioral work complete and a usable 100/101 quantitative JP performed-state model; promotion is blocked only by the remaining `103245:login:0` waveform required by its 101/101 freeze protocol. Taihou is now **canonical frozen V1 / Grade A / 86.89** for textual/behavioral/relationship-conditioned/multilingual textual reconstruction and bounded C1-C3 simulation. Its R9 claim-revision ledger and promotion audit preserve release provenance; R5/R6/R7/R8 remain canonical specialists; high-stakes C4/C5 abstention remains explicit; Dorm3D remains a separate established-intimacy stratum; and JP performed voice remains `OPEN_PARTIAL_SOURCE_MAPPING` outside the frozen V1 acoustic scope. Baltimore V1 is canonical and supports adversarially validated textual/behavioral/relationship C1-C3 simulation with CN/JP/EN/TW/KR textual realization plus measured JP activation/projection x temporal-continuity constraints; C4-C5 abstention and ear-dependent timbre remain explicit boundaries. Their packages in `02 Extracted Character Corpora/` remain the source-verification layers.
- Exact wording and audio claims escalate to original source evidence. Promotion occurs only after source-gap closure appropriate to the character, performed-voice analysis where available, claim-impact adjudication, and adversarial consistency review; source acquisition alone is not treated as analytical promotion.

## Retrieval routes

### Character interpretation / simulation

`CURRENT_STATE_AND_CORPUS_MAP.md` -> character reconstruction current-state map / current monograph or synthesis in `03 Character Reconstruction/` when one exists -> the relevant package in `02 Extracted Character Corpora/` -> exact evidence record, regional crosswalk, or audio alignment -> original source when needed. A character without any reconstruction authority routes directly to the evidence package.

### Source / evidence verification

`CURRENT_STATE_AND_CORPUS_MAP.md` → `CHARACTER_SOURCE_MAP.md` → evidence layer → machine provenance → Primary Sources original audio or pinned upstream source.

## Methods, audits, and manifests

- [Source inventory — `01 Source Lock and Inventory/AZUR_LANE_SOURCE_INVENTORY.md`](01%20Source%20Lock%20and%20Inventory)
- [Schema discovery — `01 Source Lock and Inventory/AZUR_LANE_SCHEMA_DISCOVERY.md`](01%20Source%20Lock%20and%20Inventory)
- [Extraction plan — `00 Frameworks and Methods/AZUR_LANE_EXTRACTION_PLAN.md`](00%20Frameworks%20and%20Methods)
- [JSON/Lua equivalence audit — `08 Audits and Manifests/AZUR_LANE_JSON_LUA_EQUIVALENCE_AUDIT.md`](08%20Audits%20and%20Manifests)
- [Source-layer semantics audit — `08 Audits and Manifests/AZUR_LANE_SOURCE_LAYER_SEMANTICS_AUDIT.md`](08%20Audits%20and%20Manifests)
- [Pipeline method — `00 Frameworks and Methods/AZUR_LANE_PIPELINE_METHOD.md`](00%20Frameworks%20and%20Methods/AZUR_LANE_PIPELINE_METHOD.md)
- [Character reconstruction analytical method — `00 Frameworks and Methods/AZUR_LANE_CHARACTER_RECONSTRUCTION_ANALYTICAL_METHOD.md`](00%20Frameworks%20and%20Methods/AZUR_LANE_CHARACTER_RECONSTRUCTION_ANALYTICAL_METHOD.md)
- [Readiness scoring method — `00 Frameworks and Methods/AZUR_LANE_READINESS_SCORING_METHOD.md`](00%20Frameworks%20and%20Methods/AZUR_LANE_READINESS_SCORING_METHOD.md) (the existing canonical artifact serving the corpus-readiness method role)
- [Audio source inventory — `01 Source Lock and Inventory/AZUR_LANE_AUDIO_SOURCE_INVENTORY.md`](01%20Source%20Lock%20and%20Inventory/AZUR_LANE_AUDIO_SOURCE_INVENTORY.md)
- [Source augmentation report — `08 Audits and Manifests/AZUR_LANE_SOURCE_AUGMENTATION_REPORT.md`](08%20Audits%20and%20Manifests/AZUR_LANE_SOURCE_AUGMENTATION_REPORT.md)
- [Other audits — `08 Audits and Manifests/`](08%20Audits%20and%20Manifests)
- [Canonical build manifest — `08 Audits and Manifests/manifests/AZUR_LANE_BUILD_MANIFEST.json`](08%20Audits%20and%20Manifests)
- [Machine social resolution audit — `08 Audits and Manifests/audits/social_entity_resolution.json`](08%20Audits%20and%20Manifests)
- [Validation summary — `08 Audits and Manifests/manifests/validation_summary.json`](08%20Audits%20and%20Manifests)

## Provenance contract

Every normalized record carries upstream repository, commit SHA, regional client, source file/table/record ID, extraction timestamp, pipeline/parser version, and content SHA-256. Raw client text and raw social IDs remain preserved beside derived joins.

## Known limitations

Baltimore is `AUDIO_READY` at 100 mapped / 0 unresolved spoken and now has a canonical quantitative JP performed-voice profile over 100/100 manifest-verified WAV derivatives. Its integrated character monograph is now canonical frozen V1 after claim integration and final promotion audit. Ear-dependent timbre/aesthetic description remains OPEN because this analysis environment did not directly audition the clips. Dorm3D non-chat and Island non-relationship parsing are supported. JP performed-voice acquisition is supported and acquired; readiness remains per-character. Takao is `AUDIO_READY` with 114 mapped / 0 unresolved spoken and a canonical performed-voice profile. St. Louis is `AUDIO_READY` with 71 mapped / 0 unresolved spoken, five known-unvoiced fields, and one separately classified non-dialogue campaign placeholder; its acoustic/timing/state-transition profile is canonical. Bremerton is text-side `AUDIO_READY` at 101 mapped / 0 unresolved spoken plus seven known-unvoiced profile fields. The later WAV rollout has repaired the former broad performed-voice publication block: **100/101** mapped derivatives are directly retrievable, hash-verified, and quantitatively measured in `AZUR_LANE_BREMERTON_JP_VOICE_PERFORMANCE_PROFILE.md`. The only remaining acoustic-publication exception is `BREMERTON_103245_LOGIN_LOGIN_S042_cc507128.wav`; frozen V1 remains blocked because Bremerton's pre-declared gate requires 101/101 measurements. Ear-dependent timbre remains OPEN. Structural gaps do not automatically imply censorship or release lag. Enterprise's unmerged identity alternative remains explicit. Community sources remain validation-only.

<!-- SOURCE_AUGMENTATION_START -->
## Source augmentation boundary

- Source-status model: `source-status-2.0.0`.
- Dorm3D non-chat: parser supported; explicit `SUPPORTED_PRESENT` / `SUPPORTED_NOT_FOUND` per character and locale.
- Island non-relationship: parser supported; raw Lua fallback preserves structured-JSON conversion gaps.
- JP voice: direct JP acquisition is `ACQUIRED`; catalog `RESOLVED`; integrity `PASS`. Original bundles are globally deduplicated under Primary Sources and analytical alignments remain in Analysis.
- Primary Sources Azur Lane route: `1BoL0xYtws249v800vv3FWRpKW1jdwUDl` under parent `1tNJvglC-ri_AEGTkJupZ78WddyiCqQMy`.
- Analysis route remains: .
- Existing readiness scores are unchanged; JP performance readiness is a separate dimension.
- Takao performed-voice readiness: `AUDIO_READY` — 114 mapped text utterances / 0 text-side unresolved; canonical specialist `AZUR_LANE_TAKAO_JP_VOICE_PERFORMANCE_PROFILE.md`.
- Takao source-gap closure: Dorm3D non-chat `SUPPORTED_NOT_FOUND`; Island non-relationship `SUPPORTED_PRESENT`.
- Takao V1 character monograph promotion: **canonical frozen V1**, governed by promotion audit `17zXXqowMXcFjB6x829xUeVsQRsVxsdWu`.
- St. Louis reconstruction: **canonical constrained frozen V1** under Grade C / 57.3 evidence; R5 adversarial validation, R6 Helena/Honolulu/Boise relationship synthesis, R7 multilingual speech reconstruction, exhaustive JP performed-voice analysis, and promotion audit are complete. Full unrestricted simulator authority remains explicitly unestablished.
- St. Louis source boundaries: Dorm3D non-chat `SUPPORTED_NOT_FOUND`; Island non-relationship `SUPPORTED_NOT_FOUND`; JP performed voice `AUDIO_READY` at 71 mapped / 0 unresolved spoken, with five known-unvoiced `drop_descrip` fields and one `NON_DIALOGUE_PLACEHOLDER`. Promotion audit `1T9JEBI3qUunzC4Z6-fj327kqTsnJdTnT`; canonical voice specialist `11VBbFih9_TJSQIX6ySXcZSNRBv8rgjK-`.
- Baltimore performed-voice readiness: `AUDIO_READY` - 100 mapped / 0 unresolved spoken; 100/100 published WAV derivative hashes verified; canonical specialist `AZUR_LANE_BALTIMORE_JP_VOICE_PERFORMANCE_PROFILE.md` (`1Qz1uSTjHs1gl2gEa9Mk3Nm35KTty4laEF0zLfKVPfJs`); quantitative acoustic state model complete, ear-dependent timbre OPEN.
- Baltimore V1 reconstruction authority: **canonical frozen V1**; monograph `149ZmLNb9ojnApRbBYfeoJfrKVtRHJ0OCWz5U2rSqSwE`; claim ledger `1GwCoNS4BbanIOHDyVrQMmAhD5K0VCpdeQd9IUQq5RDg`; promotion audit `19BQQcMprDNGM11urlpTBFW-0Yrnyr7StfhSssTKkQ7k`; promotion verdict `BALTIMORE_CHARACTER_MONOGRAPH_V1_PROMOTION_PASS` / `PROMOTE_TO_CANONICAL_V1`.
- Bremerton reconstruction: **Grade-A / 87.75 active-provisional full model**. R0 source/readiness, seven-part memory R1, exact 41-record narrative R2, R3 longitudinal synthesis, R5 adversarial validation, R6 relationship synthesis, R7 multilingual speech reconstruction, and R8 textual simulation audit are complete; character reconstruction home `122p2KT0Gnwy-_OWN7QsFtx2unQ7PWyjY`.
- Bremerton JP text/audio mapping: text-side `AUDIO_READY` at 101 mapped / 0 unresolved spoken, with seven known-unvoiced profile fields.
- Bremerton performed voice: **100/101 quantitative acoustic pass complete**. Specialist `1EJ81rtLs-bBP_k6kV4u3fsAhHZjCOLtt`; fixed matrix `1-7DbKSRe_arXF9KcQdue5dAp1Do-KeIT`. All 100 retrieved WAVs match manifest SHA-256 and are 44.1 kHz mono PCM. The sole unmeasured mapped record is `103245:login:0` / `BREMERTON_103245_LOGIN_LOGIN_S042_cc507128.wav`; ear-dependent timbre remains OPEN. Promotion audit `1hdGLJeIsmvAHSqeqF3jF4i-LAuJ_klFT` now records `BREMERTON_CHARACTER_MONOGRAPH_V1_PROMOTION_BLOCKED_ONE_WAVEFORM_SHORT_OF_FROZEN_GATE`; old publication-gap audit `1C56nvsyl8BRiJuZzelHRKGzNieiQ32m1` is historical provenance.

See `08 Audits and Manifests/AZUR_LANE_SOURCE_AUGMENTATION_REPORT.md`, `01 Source Lock and Inventory/AZUR_LANE_AUDIO_SOURCE_INVENTORY.md`, and the Dorm3D/Island audits under `08 Audits and Manifests/`.
<!-- SOURCE_AUGMENTATION_END -->


## Prinz Eugen reconstruction initiation — 2026-08-25

- Created the canonical active reconstruction home `03 Character Reconstruction/PRINZ_EUGEN_40303/` (`1K0vEjel5HUBHSkT8idbCilxkqTsMEPOY`).
- R0 and R1 are complete at the structural/readiness level; no personality thesis has been promoted from metadata alone.
- Current next operation: execute the complete 127-scene CN R2 anchor reading from the now-published, readback-verified evidence pack.
- JP audio publication is independently usable at 114 mapped literal WAVs, but one expected spoken slot remains unresolved and no acoustic interpretation has yet been performed.

## Corpus-wide evidence publication completeness — 2026-08-26

- [Publication completeness audit — `AZUR_LANE_CHARACTER_EVIDENCE_PUBLICATION_COMPLETENESS_AUDIT.md`](08%20Audits%20and%20Manifests/AZUR_LANE_CHARACTER_EVIDENCE_PUBLICATION_COMPLETENESS_AUDIT.md) — Drive `1gzrTcBAH4eWMKdXtslltfttYOdHv5B0K`.
- All 17 requested character evidence trees are present in their canonical `02 Extracted Character Corpora/` homes: 1,629 manifest-declared outputs plus 17 character manifests, with zero missing or unreadable final objects.
- The remediation published 809 existing local artifacts without regeneration, refreshed 61 earlier-character generated metadata files, repaired five latent same-size content mismatches found by Drive readback, and parent-routed 105 already-readable nested social objects into their canonical character trees.
- New-character Analysis verification produced 871 SHA-256 matches plus one complete streamed-size match for an artifact above the connector's inline frame limit. The 61 earlier-character refreshed files, 27 listening metadata files, 33 newly ledgered source bundles, and the updated source publication manifest were also SHA-256 readback verified.
- The Primary Sources publication manifest now records 344/344 content-addressed JP source bundles (159,277,728 bytes); none remain pending.
- Final recursive topology result: 1,646/1,646 character objects, zero missing objects, and zero duplicate canonical relative paths. Final reconstruction-publication result: zero `PUBLICATION_BLOCKED`, `PIPELINE_BLOCKED`, or `SOURCE_IDENTITY_BLOCKED` characters. Semantic R0-R9 evidence is directly retrievable for every target. Performed-voice limitations remain explicit per character and do not alter CN semantic authority.
