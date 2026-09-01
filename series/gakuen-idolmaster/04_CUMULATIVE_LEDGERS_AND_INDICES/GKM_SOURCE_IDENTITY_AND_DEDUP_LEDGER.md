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
