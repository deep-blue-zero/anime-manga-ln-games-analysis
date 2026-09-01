# Azur Lane Schema Discovery

## Canonical joins

`ship_data_template.group_type` is the canonical character/group ID. A leveled ship instance remains a distinct `ShipInstance`. `ship_skin_template.ship_group` maps every skin back to its group; skin IDs are not assumed to be arithmetically derivable because alternate skin ranges exist. Story actors map first by skin ID, then by ship/NPC statistic ID and its encoded base skin.

The current build recovered 1,233 character groups, 2,754 skins, 3,957 ship instances, 5,190 actor mappings, and 5,880 normalized alias keys.

Child, ?, META, collaboration, and same-display-name incarnations remain separate groups. Related-incarnation fields are candidates, never merge instructions. For example, USS Enterprise (10706) and HMS Enterprise (20232) collide by EN display name and remain distinct.

## Story semantics

Narrative objects have a `scripts` list. Each list item is preserved in source order and classified as dialogue, narration, title card, choice, or stage direction. Important fields include `actor`, `actorName`, `say`, `sequence`, `options`, `optionFlag`, `bgName`, `bgm`, `painting`, `expression`, `side`, `action`, transitions, and effects. The entire raw record is retained.

Top-level `stages` objects are battle configuration, not VN narrative. They are skipped by the narrative parser and counted in its summary.

## Character text semantics

Raw slots remain intact. `main` and `main_extra` use pipe-delimited lines. `couple_encourage` is structured data containing selector targets, selector type, line, and flag; it is preserved rather than flattened into an interpretive relationship label.

Normalized categories are profile, base_secretary, affinity, oath, combat, relationship_specific, special_secretary, skin, interactive_skin, and other. Exact source strings, container strings, raw values, name-code tokens, and provenance are retained.

## Social topology

`activity_ins_template` supplies posts and `activity_ins_npc_template` comments; `activity_ins_language` resolves message keys. `activity_ins_chat_group.content` orders messages from `activity_ins_chat_language`. Dorm3D chat mirrors this family. Output retains thread, participants, sequence, reply target, choices, flags, and raw rows.

Island character IDs directly match ship groups in `island_chara_template`. `island_couple_word` links participant selectors to story IDs. Broader Island and non-chat Dorm3D source systems are parser-supported as of `source-augmentation-1.0.0`; their distinct graph schemas and conversion-boundary findings are documented in the dedicated Dorm3D and Island source audits.

## Source augmentation schemas

`dorm3d_dialogue_group` joins a character and room to a regional story script. Story nodes preserve source order, `options[].flag`, `optionFlag`, conditional and merge edges, raw unlock/trigger gates, dispatcher animation/timeline operations, camera/background metadata, and direct `voice` event references.

Island uses a distinct graph: `island_chara_template → island_unit_character → island_strollnpc`, with skin variants, map/unlock/action-feedback conditions, task-to-`ISLAND*` story joins, and `characterId` scene actors. Flat `island_dialogue` and `island_interaction` group IDs are not forced onto ship identities without an encoded join. Raw Lua records are permitted as a provenance-labeled fallback when the structured JSON conversion omits a record; Takao is the regression case.

## Uncertainty rules

An explicit localized name or `{namecode:N}` token can create a mention candidate. Pronouns never do. Generic aliases such as CN ???? can overmatch ordinary prose, so mention-only rows remain candidates and are never treated as direct presence. Missing subsystem output is not confirmed absence.
