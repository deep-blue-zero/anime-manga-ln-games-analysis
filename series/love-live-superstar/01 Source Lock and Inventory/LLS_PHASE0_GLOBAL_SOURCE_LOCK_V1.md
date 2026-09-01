---
series: "Love Live! Superstar!!"
artifact_id: "LLS_PHASE0_GLOBAL_SOURCE_LOCK_V1"
artifact_type: "phase0_global_source_lock"
status: "complete"
scope: "36 TV episodes"
---

# Love Live! Superstar!! — Phase 0 Global Source Lock

## Completion statement

Phase 0 source validation is complete for the 36-episode primary-source corpus.

The lock establishes:

- exact Drive identity and compressed byte size for every bundle;
- local downloaded-size equality with Drive metadata;
- SHA-256 for every bundle;
- clean ZIP CRC for every bundle;
- required internal primary-evidence components;
- Japanese subtitle format and selection state;
- complete audio presence;
- retained-frame/contact-sheet/index availability;
- bundle schema/version differences;
- explicit non-blocking anomaly/provenance notes.

## Corpus QA summary
- Bundles: **36/36**
- Bytes: **6,148,386,809**
- SHA-256 hashes: **36/36**, with **36 unique hashes**
- ZIP CRC: **36/36 PASS**
- Component contract: **36/36 PASS**
- Downloaded size = Drive-listed size: **36/36**
- Retained frames: **28,801**
- Japanese subtitle cues: **15,571**
- Contact sheets: **1,586**

## Semantic release gate

Phase 0 completion does **not** authorize retrospective use of all 36 episodes during the sequential pass. It only proves the source corpus is available and valid.

Phase 1 begins at `S01E01`, with the semantic boundary sealed to `S01E01`. Later episode bundles remain technically validated but semantically sealed until reached in sequence.
