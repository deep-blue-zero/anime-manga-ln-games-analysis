# Azur Lane Dorm3D Source Audit

- Parser: `dorm3d-non-chat-1.0.0`.
- Primary group table: `ShareCfg/dorm3d_dialogue_group.json`.
- Regional scene scripts: `CN/GameCfg/story.json`, `JP/GameCfg/storyjp.json`, and corresponding EN/TW/KR aggregates.
- Supporting joins audited: `dorm3d_rooms`, `dorm3d_resource`, group room/character/unlock/trigger fields.
- Preserved topology: source order, mutually exclusive option flags, branch edges, merge edges, conditions, full scene nodes, dispatcher animation/timeline operations, camera/background references, and direct `voice` references.
- Raw archival strategy: `GIT_PIN_SUFFICIENT` at AzurLaneData `4cca5c2437007b62d30a6235fcfc0c0203231378` and AzurLaneLuaScripts `cc8e9fdf6a1a2e5d20c9a8ff6c0369832bb33336`.
- Current target batch: **625** regional character-linked scenes.
