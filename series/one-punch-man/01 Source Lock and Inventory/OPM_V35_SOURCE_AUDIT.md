---
series: OPM
artifact_type: source_audit
scope: V35 complete mechanical and semantic source lock
generation: V2
status: canonical
source_boundary: Japanese tankobon V35; mechanical and semantic PASS
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
created: 2026-09-13
workspace_state: local_staged_unintegrated
archive_integrity: PASS
semantic_source_lock: PASS
sequential_reading: COMPLETE
---

# One Punch Man — V35 Source Audit

## Current disposition

**Mechanical and semantic PASS; complete sequential review and Japanese/register audit.** V34's 41-check closeout passed before V35 opened. All 207 images were directly inspected in strict order, including a fresh reconciliation of the previously exposed but unsaved 0009–0024 interval before the advance through 0207. All 178 planned audit targets were then directly reinspected in strict order. Original detail was requested; the viewer transport reported display resizing from 1303 × 2048 to 1248 × 1961, while source/cache bytes remain unchanged. The [canonical reading](../02%20Sequential%20Readings/OPM_V35_DEEP_READING.md) owns observations and the [Japanese dialogue/register audit](../08%20Audits%20and%20Manifests/OPM_V35_JAPANESE_DIALOGUE_AND_REGISTER_AUDIT.md) returns PASS. Prospective freeze, V1 comparison, checkpoint adjudication and propagation are complete; the [V35 update manifest](../08%20Audits%20and%20Manifests/OPM_V35_UPDATE_MANIFEST.md) owns final readback and the V36 gate.

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

## Identity and semantic map

Cover 0001 and title 0005 identify V35 `会っちゃいけない奴`. ONE/Murata notes are 0002–0003, fiction art 0004, cast/recap 0006–0007 and contents 0008. Contents records the following printed starts, not yet certified archive offsets:

| Contents label | Printed start | Archive confirmation |
|---|---:|---|
| 176撃目 `会っちゃいけない奴` | 7 | 0009 title; narrative 0010–0037; terminal gag 0038 |
| 177撃目 `新居` | 37 | 0039 title; narrative 0040–0075; terminal gag 0076 |
| 178撃目 `秘匿情報` | 75 | 0077 title; narrative 0078–0110 |
| 179撃目 `華` | 109 | 0111 title; narrative 0112–0136; attached terminal gags 0137–0138 |
| 180撃目 `訪問者` | 137 | 0139 title; narrative 0140–0167; attached terminal gag 0168 |
| 181撃目 `震源` | 167 | 0169 title; narrative 0170–0195 |
| 番外編 `怖くないよ` | 194 | 0196 title and narrative opening; narrative through 0201 |

Endmatter is 0202–0207: update/publication credits, digital imprint and copyright matter, branding, and reproduced cover-package images.

Narrative, attached-gag, bonus and endmatter boundaries are now certified by complete sequential inspection. A title such as `新居` is not itself a completed move or proof of every exposed legacy claim.

Prospective freeze precedes V35 legacy search/comparison and current checkpoint reopening. Prior prediction/heading and V34 V1 housing/monster-companion exposure are disclosed, not admitted as narrative evidence. The completed audit corrects 0180's `重要参考人` to an important witness/person of interest, confirms Psykos's death-row list status, preserves the unlabeled 0189 communication mechanism and verifies symmetric `到達者` usage through Fubuki's inference. V36 and web narrative remain outside scope. The owner-authorized branch publication checkpoint remains current Git authority; this V35 closeout performs no repository mutation.


## Final semantic source lock

Cover 0001 and title 0005 identify V35 `会っちゃいけない奴`. ONE/Murata notes are 0002–0003, fiction art 0004, cast/recap 0006–0007 and contents 0008. Contents records the following printed starts, not yet certified archive offsets:

| Contents label | Printed start | Archive confirmation |
|---|---:|---|
| 176撃目 `会っちゃいけない奴` | 7 | 0009 title; narrative 0010–0037; terminal gag page 0038 |
| 177撃目 `新居` | 37 | 0039 title; narrative 0040–0075; terminal gag page 0076 |
| 178撃目 `秘匿情報` | 75 | 0077 title; narrative 0078–0110 |
| 179撃目 `華` | 109 | 0111 title; narrative 0112–0136; attached terminal gags 0137–0138 |
| 180撃目 `訪問者` | 137 | 0139 title; narrative 0140–0167; attached terminal gag 0168 |
| 181撃目 `震源` | 167 | 0169 title; narrative 0170–0195 |
| 番外編 `怖くないよ` | 194 | 0196 title and narrative opening; narrative through 0201 |

Endmatter occupies 0202–0207: publication/update note, digital imprint and copyright matter, reproduced cover-package images and extra-page labels. These pages supply publication framing, not timed narrative evidence.

Narrative, attached-gag, bonus and endmatter boundaries are certified by complete sequential inspection. A title such as `新居` is not itself proof of every exposed legacy claim; the narrative evidence above establishes the move and its limits independently.

Exact map copied from frozen sections 0–15. Disjoint spans: front 0001–0008; chapter-plus-art 0009–0038, 0039–0076, 0077–0110, 0111–0138, 0139–0168 and 0169–0195; bonus 0196–0201; endmatter 0202–0207. Every image is accounted for once. All 207 source images retain their original `.jpg` filenames and bytes.
