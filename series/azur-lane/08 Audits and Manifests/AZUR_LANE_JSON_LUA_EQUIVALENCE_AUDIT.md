# Azur Lane JSON/Lua Equivalence Audit

## Sampled findings

CN `GameCfg/story.json["dafeng1"]` preserves the same top-level fields, 19-script order, dialogue, title sequence, actor IDs, choices, background, BGM, transition, painting, and typewriter metadata found in `CN/gamecfg/story/dafeng1.lua`.

CN split `ship_skin_words` JSON preserves the Lua record fields and nested `couple_encourage` topology sampled in base records. JSON numbers, booleans, arrays, objects, and UTF-8 strings are adequate for the implemented normalizers.

The aggregate JSON contains both narrative `scripts` and battle `stages`; the distinction is semantic, not conversion loss. JP uses `storyjp` naming in both JSON and Lua.

## Current decision

JSON is the operational authority for identity, story, character text, and implemented social layers. Raw Lua is retained as a schema and sample cross-check. The audit is not a proof of global losslessness.

## Known audit gap

A general Lua table parser and automated value-by-value sample comparator are not yet implemented. Therefore ordering/metadata equivalence outside sampled story and skin-word families is `UNKNOWN`, not presumed lossless. Any JSON table found empty while its split-data or Lua counterpart is populated is treated as a routing issue; this already changed identity/dialogue routing from empty `ShareCfg` stubs to `sharecfgdata`.
