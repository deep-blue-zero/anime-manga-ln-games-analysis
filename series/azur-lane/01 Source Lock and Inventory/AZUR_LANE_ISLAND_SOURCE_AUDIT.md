# Azur Lane Island Source Audit

- Parser: `island-non-relationship-1.0.0`.
- Identity/behavior graph tables: `island_chara_template`, `island_unit_character`, `island_strollnpc`, `island_skin_template`, `island_skin_colordiff_template`, and action/task/story joins where linked.
- Scene source: regional `GameCfg/story*.json` objects with `ISLAND*` IDs; task conditions are joined from `island_task` without forcing unrelated flat dialogue/interaction groups onto a ship identity.
- Raw Lua is a semantic and conversion witness. Takao records present in raw Lua but absent from structured JSON are preserved as `raw_lua_witness_fallback` with explicit JSON/Lua divergence metadata.
- Raw archival strategy: `GIT_PIN_SUFFICIENT` at AzurLaneData `4cca5c2437007b62d30a6235fcfc0c0203231378` and AzurLaneLuaScripts `cc8e9fdf6a1a2e5d20c9a8ff6c0369832bb33336`.
- Current target batch: **85** regional identity/behavior/scene records.
