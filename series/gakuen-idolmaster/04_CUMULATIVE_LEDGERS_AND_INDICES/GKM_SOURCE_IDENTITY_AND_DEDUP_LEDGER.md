---
title: "Gakuen Idolmaster V2 - Source Identity and Dedup Ledger"
project: "Gakuen Idolmaster"
document_type: "persistent ledger"
version: "2.1"
source_lock: "GAKUMAS V2 Source Lock 1.0"
initialized: "2026-08-13"
last_updated: "2026-11-15 — source-to-analysis audit source-anomaly table"
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

## Source-to-analysis audit corrections — 2026-11-15

Source anomalies and conventions surfaced by the source-to-analysis audit (GKM-SAA-291, with GKM-SAA-241, 213 and 270). Each was re-read in A1 on this date. None changes a source identity or count; each changes how an object may be cited. Locators resolve in the [locator ledger](GKM_PRIMARY_SOURCE_LOCATOR_LEDGER.md#source-to-analysis-audit-corrections--2026-11-15).

| anomaly | A1 object and lines | observation | handling | audit ID |
| --- | --- | --- | --- | --- |
| (a) duplicated title card | `adv_unit_01-01_05.txt` L13 (cf. `01-01_04` L75, `01-01_06` L21) | part 05 carries the title card `6話`, as does part 06; part 04 carries `4話` | chronology follows archive part order; the title card is not a sequence locator (`LOC-SAA-291A`) | GKM-SAA-291(a) |
| (b) name field on Misuzu-voiced lines | `adv_live_hmsz_001_start-03-01.txt` L1, L21–L24 | `name=佑芽` on two lines whose actor is `hmsz` and whose voice assets are `hmsz-01` and `hmsz-02`; the other Misuzu live lines read `name=美鈴` | probable copy error; attribute the murmur to Misuzu; AV-D confirmation pending (`LOC-SAA-241A`) | GKM-SAA-241, GKM-SAA-291(b) |
| (c) `hkne` voice stems in China's narration | `adv_pstory_003_kcna_selection-failure-01.txt` L92–L99 | the three `ナレーション` lines carry voice assets `hkne-001`..`003` under `actorId=kcna`, in a Source Lock 1.0 object | the asset stem is recorded; whether the voice is Kanae's is an AV question (Carbon candidate) (`LOC-SAA-291C`) | GKM-SAA-291(c), GKM-SAA-213 |
| (d) parenthesised Producer lines | corpus-wide, current A1 | 841 of 842 parenthesised `{user}` messages lack `isInner=true` | Producer interiority is marked typographically; parsers keyed on `isInner` miss it | GKM-SAA-291(d) |
| (e) festival dating tension | `adv_event_024_main-02.txt` L4; `adv_event_028_main-01.txt` L9, `-02` L155, `-03` L452 | E024 dates festival planning to late September (`――9月下旬。`); SL1.1 E028 places the culture festival "next week" while the September 100 Pro exam is still ahead | OPEN; recorded here as a source-level tension; the continuity disposition belongs to the continuity ledger (`LOC-SAA-291E`) | GKM-SAA-291(e), GKM-SAA-270 |
