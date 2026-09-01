---
series: AZUR_LANE
artifact_type: corpus_map
scope: PRINZ_EUGEN_40303_RECONSTRUCTION
generation: V1
status: active_provisional
scope_character: PRINZ_EUGEN_40303
semantic_authority: CN
source_boundary: Active Prinz Eugen reconstruction over pinned AZL-2026-08-22-4cca5c24-cc8e9fdf source build
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
---

# Prinz Eugen — Current State and Corpus Map

## Current authority

This is the first-read entrypoint for the active Prinz Eugen / group `40303` reconstruction.

Current reconstruction state:

- **R0 — complete:** `AZUR_LANE_PRINZ_EUGEN_RECONSTRUCTION_READINESS_AUDIT.md`
- **Derived publication audit — complete:** `AZUR_LANE_PRINZ_EUGEN_DERIVED_EVIDENCE_PUBLICATION_AUDIT.md`
- **R1 — structurally complete / interpretive anchors open:** `AZUR_LANE_PRINZ_EUGEN_RECONSTRUCTION_EVIDENCE_MAP.md`
- **R2 — blocked on direct textual evidence publication/readback**
- **R3–R10 — not started**
- **Character monograph — not yet created**

## Governing method

`AZUR_LANE_CHARACTER_RECONSTRUCTION_ANALYTICAL_METHOD.md` V1 / method version `1.0.0`.

Semantic authority remains CN. JP, EN, TW, and KR are independent regional witnesses. JP performed voice is a separate realization layer.

## Pinned source boundary

- Build ID: `AZL-2026-08-22-4cca5c24-cc8e9fdf`
- AzurLaneData: `4cca5c2437007b62d30a6235fcfc0c0203231378`
- AzurLaneLuaScripts: `cc8e9fdf6a1a2e5d20c9a8ff6c0369832bb33336`
- character build manifest: `character-build-2.1.0`
- readiness: **B / 76.18**
- warnings: `COMMANDER_HEAVY`, `MANY_UNALIGNED_RECORDS`

## Canonical evidence roots

### Analysis source package

`02 Extracted Character Corpora/PRINZ_EUGEN_40303/`

Current directly retrievable surface:

- `CHARACTER_MANIFEST.json`
- `CHARACTER_SOURCE_MAP.md`
- `SOURCE_COVERAGE.json`
- `SOURCE_COVERAGE.md`
- `audio/`

### JP primary/performed source package

`Primary Sources/02 Japanese Voice Audio/Characters/PRINZ_EUGEN_40303/`

Listening derivative state:

- 114 mapped spoken WAVs;
- 9 known-unvoiced text fields;
- 1 unresolved expected spoken field;
- 1 non-text/review asset;
- literal Drive WAV objects are published and directly retrievable.

## Intended derived evidence surface

The canonical manifest declares/hashes 95 outputs, including the following human-readable analytical inputs that are not currently exposed in the Drive Analysis folder:

- CN character dialogue ledger;
- CN narrative scene corpus/raw corpus/scene index;
- CN social reconstruction;
- relationship evidence index;
- regional crosswalk;
- CN/JP/EN/TW/KR Island evidence.

Their absence from the current Drive publication is the only present R2 blocker.

## Locked corpus summary

- 127 linked narrative scenes;
- 886 direct attributed narrative lines;
- 125 character-dialogue records;
- 94 non-base skin records;
- 25 interactive-skin records;
- 17 social threads;
- 114 direct interlocutor entities;
- 44 social interlocutor entities;
- 5 explicit relationship entities;
- 256 narrative co-occurring entities;
- 99 Commander-facing character records;
- 5,902 regional alignment candidates;
- 92.61% weighted regional coverage;
- 35 Island non-relationship records;
- no dedicated character-memory group;
- no Dorm3D chat/non-chat evidence;
- no Island relationship evidence.

## Authority rule

Counts/readiness establish what can be studied; they do **not** establish Prinz Eugen's personality. Until R2 reads the actual CN evidence in context, no claim about teasing, detachment, loyalty, fear, intimacy, manipulation, boredom, vulnerability, or moral priorities should be treated as reconstructed authority.

## Next operation

**Restore/directly publish the manifest-declared human-readable evidence pack, verify readback, then perform `AZUR_LANE_PRINZ_EUGEN_NARRATIVE_DEEP_READING.md` over all 127 linked CN scenes.**

The R2 reading should group scenes by analytical function, preserve scene context, weight independent high-context evidence over repetition, and explicitly test the ten open questions in the R1 evidence map.
