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
