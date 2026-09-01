# Azur Lane Source Inventory

Audit date: 2026-08-19.

## Primary upstream snapshots

- AzurLaneTools/AzurLaneData: `4cca5c2437007b62d30a6235fcfc0c0203231378`
- AzurLaneTools/AzurLaneLuaScripts: `cc8e9fdf6a1a2e5d20c9a8ff6c0369832bb33336`

The checkouts are partial-clone sparse working trees under `upstream/`. They contain only the five locale ShareCfg/sharecfgdata trees, aggregate/per-file story trees, versions, and the CN nation constant. Upstream is gitignored; build manifests retain SHAs.

## Locale story inventory

| Locale | JSON aggregate | Raw Lua directory | Lua files | Lua size |
|---|---|---|---:|---:|
| CN | `CN/GameCfg/story.json` (65.0 MiB) | `CN/gamecfg/story/` | 7,290 | 53.2 MiB |
| JP | `JP/GameCfg/storyjp.json` (67.8 MiB) | `JP/gamecfg/storyjp/` | audited separately | about 55 MiB |
| EN | `EN/GameCfg/story.json` (65.8 MiB) | `EN/gamecfg/story/` | 7,323 | 54.1 MiB |
| TW | `TW/GameCfg/story.json` (64.9 MiB) | `TW/gamecfg/story/` | 7,194 | 52.0 MiB |
| KR | `KR/GameCfg/story.json` (67.0 MiB) | `KR/gamecfg/story/` | 7,197 | 54.3 MiB |

CN JSON contains 6,879 top-level objects. Narrative objects use `scripts`; battle-stage objects use `stages` and are intentionally excluded from the literary story normalizer while remaining in upstream.

## Identity and character-text authorities

The non-empty large tables are in lowercase `sharecfgdata/`; same-named `ShareCfg/` stubs can be empty.

- `ship_data_statistics`: names, nationality, base skin, historical/English reference.
- `ship_data_template`: stable `group_type` join and ship-instance rows.
- `ship_skin_template`: skin ID ? `ship_group`, painting, presentation, Live2D metadata.
- `ship_skin_words`: base and skin dialogue slots.
- `ship_skin_words_extra`: newer/extended slot records.
- `ship_skin_words_add`: collaboration/special supplemental slots.
- `name_code`: locale-specific token expansion witnesses.
- `CN/model/const/nation.lua`: numeric nation constants and i18n keys.
- `character_voice`, `character_voice_special`, `voice_actor_CN`, and `voice_bgm`: voice metadata surfaces.

## Narrative and social families found

- `memory_group`, `memory_template`, `memory_storyline`, `story_group`, `story_template`
- `activity_ins_*`: Juustagram posts, comments, profiles, and chat
- `dorm3d_ins_*`: Dorm3D posts, direct-chat groups, messages, telephone groups
- `dorm3d_dialogue_group` + regional `GameCfg/story*.json`: non-chat Dorm3D groups and full conditional scene scripts
- `dorm3d_rooms`, `dorm3d_resource`: room, character, model, and skin/resource joins
- `island_chara_template`, `island_unit_character`, `island_strollnpc`, `island_skin_template`: Island identity, profile, appearance, placement, and behavior graph
- `island_task` + regional `ISLAND*` story records: task conditions and full linked Island scenes
- JP client asset archive/catalog: performed-voice bytes and source identity; external client acquisition is required and remains separate from Analysis
- `dorm3d_dialogue_group`, `dorm3d_subtitle`, `dorm3d_touch_*`, `dorm3d_favor*`
- `secretary_special_ship*`
- `island_chara_template`, `island_dialogue`, `island_couple_word`, `island_interaction`, `island_strollnpc`
- `child_memory`, `child2_memory`, `child2_chat`
- `soundstory_template`
- `activity_event_memorybook`, `activity_sp_story`, `activity_series_enemy_story`

This inventory is primary-source discovery. No community text was copied.
