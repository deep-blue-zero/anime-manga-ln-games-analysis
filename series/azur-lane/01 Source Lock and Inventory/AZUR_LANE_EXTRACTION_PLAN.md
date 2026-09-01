# Azur Lane Extraction Plan

## Implemented phases

1. Targeted sparse acquisition of the two governing upstream repositories.
2. Five-locale identity, skin, alias, ship-instance, nation, and actor crosswalk.
3. Ordered narrative normalization with full raw records, choices, presentation, memory links, direct presence, and mention candidates.
4. Skin/base/affinity/oath/combat/relationship/special-secretary dialogue normalization.
5. Juustagram, Fleet Chat, Dorm3D chat, and Island relationship-trigger topology.
6. Stable-ID locale alignment and candidate-only difference ledger.
7. Per-character JSONL and Markdown source editions, coverage, relationship evidence, and SHA-256 manifest.
8. Reconstructible SQLite and FTS5 index.

## Next engineering work

- Parse all Dorm3D interaction, subtitle, telephone, touch, favor, and animation graphs.
- Parse broader Island unit/action/dialogue graphs and distinguish character speech from generic barks.
- Add child-memory and sound-story specialized exporters.
- Add direct raw-Lua fallback for table families that fail equivalence checks.
- Add release-version chronology from upstream version history without claiming in-universe order.
- Replace mention substring matching with locale-aware token boundaries and reviewed name-code resolution.
- Add changed-file dependency tracking so `azl sync` can rebuild only affected layers.
- Expand fixture and regression coverage to the ten-character roster.

No downstream literary labels are part of acquisition.
