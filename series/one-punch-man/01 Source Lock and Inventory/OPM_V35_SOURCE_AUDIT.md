---
series: OPM
artifact_type: source_audit
scope: V35 mechanical integrity and incremental semantic review
generation: V2
status: active_provisional
source_boundary: Japanese tankobon V35; mechanical PASS; semantic review in progress
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
created: 2026-09-13
workspace_state: local_staged_unintegrated
archive_integrity: PASS
semantic_source_lock: PENDING
sequential_reading: IN_PROGRESS
---

# One Punch Man — V35 Source Audit

## Current disposition

**Mechanical PASS; semantic review in progress.** V34's 41-check closeout passed before V35 opened. Images 0001–0008 were directly inspected at original detail with 1303 × 2048 displayed and no resize notice. The [live prospective reading](../02%20Sequential%20Readings/OPM_V35_DEEP_READING.md) owns observations; cumulative authority remains V34.

## Exact source object

| Field | Value |
|---|---|
| Input | `OPM_SOURCE_ROOT\One Punch Man - Volume 35 [Japanese].cbz` |
| Bytes | 87,519,794 |
| SHA-256 | `160d07bd53253d99b32e168e5b388c608327c0c6c9aa974ec291da8f54e74c9d` |
| Entries / images | 208 / 207 JPEGs plus `ComicInfo.xml` |
| Order / dimensions | 0001.jpg–0207.jpg; archive/numeric/lexicographic agreement; all 1303 × 2048 |
| Metadata | 340 bytes; Japanese V35, ONE / Yusuke Murata, RTL, 207 pages, historical Count=36 |
| Metadata SHA-256 | `505a279b4a13675b2f20f2c8875b4e3a68cceb4ab2573abd79ff90797b7dc290` |
| Build manifest | `manifests/volume_35.json` |
| Build-manifest SHA-256 | `800d577ac8041b6ec6863e5b051dd7d0fc6af4d5faa63a46b0b295d0d9900ab9` |

Fresh CRC/full decode, supplied-manifest byte hashes and exact-byte/decoded-RGB duplicate checks passed with no issues. The manifest uses `sha256` and omits dimensions; direct decode measures dimensions, and missing comparisons remain null. The first preparation attempt stopped before any image write at the old hash-field expectation. Tool compatibility was corrected and the same immutable source then passed; `_staging/verification/V35_preparation_compatibility_note.md` records this tooling issue. Source/archive/manifest bytes were not altered. Receipt `_staging/verification/V35_integrity.json`, checked `2026-09-13T05:54:45.167658+00:00`. Cache and tools are noncanonical and excluded from Git. V35–V36 resolve the earlier acquisition gap; historical metadata Count does not override V37 holdings.

## Identity and remaining gate

Cover 0001 and title 0005 identify V35 `会っちゃいけない奴`. ONE/Murata notes are 0002–0003, fiction art 0004, cast/recap 0006–0007 and contents 0008. Contents records the following printed starts, not yet certified archive offsets:

| Contents label | Printed start | Archive confirmation |
|---|---:|---|
| 176撃目 `会っちゃいけない奴` | 7 | pending direct title inspection |
| 177撃目 `新居` | 37 | pending |
| 178撃目 `秘匿情報` | 75 | pending |
| 179撃目 `華` | 109 | pending |
| 180撃目 `訪問者` | 137 | pending |
| 181撃目 `震源` | 167 | pending |
| 番外編 `怖くないよ` | 194 | pending |

Exact narrative, attached art, extra and endmatter boundaries remain subject to complete sequential inspection. A title such as `新居` is not itself a completed move or proof of every exposed legacy claim.

Complete sequential reading, Japanese/register audit and prospective freeze precede V35 legacy search/comparison and current checkpoint reopening. Prior prediction/heading and V34 V1 housing/monster-companion exposure are disclosed, not admitted as narrative evidence. V36 and web narrative remain outside scope. Git remains gated until V37 and corpus-wide audit.
