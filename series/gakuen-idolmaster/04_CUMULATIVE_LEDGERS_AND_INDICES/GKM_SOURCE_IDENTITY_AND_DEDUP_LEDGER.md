---
title: "Gakuen Idolmaster V2 - Source Identity and Dedup Ledger"
project: "Gakuen Idolmaster"
document_type: "persistent ledger"
version: "2.0"
source_lock: "GAKUMAS V2 Source Lock 1.0"
initialized: "2026-08-13"
status: "seeded; cumulative"
---

# SOURCE IDENTITY AND DEDUP LEDGER

This is a cumulative V2 project ledger. It is initialized in Phase 0 and must be updated rather than recreated as later phases add evidence.

## Schema

| field | meaning |
| --- | --- |
| canonical_source_id |  |
| original_name |  |
| sorted_relative_path |  |
| category |  |
| bundle_aliases |  |
| message_count |  |
| checksum |  |
| dedup_status |  |
| notes |  |

## Seed entries

| seed_id | source_or_alias | Phase 0 action | status |
| --- | --- | --- | --- |
| EVENT001005-ALIAS | shared event 001-005 view | 25-source overlap with dedicated event bundle | DEDUP REQUIRED |
| PSTORY003-REVERSI-WORLD-FINAL | adv_pstory_003_reversi_world-explanation-final.txt | promote shared institutional alias; retain original path | UNIQUE SOURCE |
| TOWER001 | adv_tower-001.txt | promote institutional alias; retain original path | UNIQUE SOURCE |


## Source Lock 1.1 — transcript refresh, 2026-11-12

| canonical delta group | basis | identity disposition |
| --- | --- | --- |
| Source Lock 1.1 | [versioned source record](../01_CORPUS_AUDIT_AND_SOURCE_LOCK/GKM_SOURCE_REFRESH_20261112.md) and [195-row per-object delta](../01_CORPUS_AUDIT_AND_SOURCE_LOCK/GKM_SOURCE_DELTA_20261112.tsv) | 3,754 identical, 172 additions, 13 revised bytes, 10 moves and zero removals |
| Dear 010-01 aliases | same original name and SHA-256, versioned path changes in delta | one evidence object per original identity, with two valid archive locators |
| Dear 037-01 | [episode comparison](../03_SOURCE_FACING_READINGS/01_CHARACTER_CORE_READINGS/GKM_DEAR_EPILOGUES_AND_COMMON_ADV_REV86.md) | 13 distinct raw objects with shared structural template. Use each only in its D track and avoid treating template repeats as independent corroboration. |
| Kanae horizontal arc | 5 A1 rows under generic Dear location, all new unassigned bundle entries | [dedicated reading](../03_SOURCE_FACING_READINGS/01_CHARACTER_CORE_READINGS/06_KURAMOTO_CHINA/GKM_KANAE_CHINA_DEAR_000_READING.md) routes the 5 objects. Derivatives and bundle appearances add no identities. |
| `musics.txt` | pinned raw bytes in both revisions, 22,304 → 25,584 bytes | opaque resource, no musical claim inferred |

## Source Lock 1.2 — transcript refresh, 2026-11-15

| canonical delta group | basis | identity disposition |
| --- | --- | --- |
| Revision 88 | [Source Lock 1.2](../01_CORPUS_AUDIT_AND_SOURCE_LOCK/GKM_SOURCE_REFRESH_20261115.md) and [per-object delta](../01_CORPUS_AUDIT_AND_SOURCE_LOCK/GKM_SOURCE_DELTA_20261115.tsv) | 103 additional A1 objects, zero removed/modified/moved. 96 exact A2 derivations and seven message-free step files. All 3,949 earlier A1 and corresponding A2 objects retain identity and bytes. |
| Kanae A3 gap | 89 additions / 2,369 messages without a character-bundle assignment | A3 character map lacks `hkne`. Recover all objects from manifest and exact A1 paths. The seven support additions and seven common steps are separately bundled. |
| Horizontal and numbered Dear | H05 L630–650 → D001 L14–50, H03 L1038–1065 → D001 L211–256 and D008 L312–317 | Separate source objects that reprise one consultation and one speech. Interpret reuse and framing while counting each remembered event only once. The mirrored run and pinky-promise scenes are separate diegetic events with later repeated wording. |
| Produce and communicating variants | GKM-R88-02, GKM-R88-03 and GKM-R88-06 | Distinct source objects survive byte-based deduplication. Parallel examinations, opposite `Condition` outcomes, wrapper pairs and repeated opening/ending templates are related alternatives or modules. Distinct content hashes do not imply independent corroboration of one outcome. |
