---
series: OPM
artifact_type: source_audit
scope: V30 mechanical integrity and complete semantic source lock
generation: V2
status: canonical
source_boundary: Japanese tankobon V30; mechanical integrity and complete semantic review PASS
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
created: 2026-09-12
workspace_state: local_staged_unintegrated
archive_integrity: PASS
semantic_source_lock: PASS
sequential_reading: COMPLETE
---

# One Punch Man — V30 Source Audit

## Current disposition

**Mechanical integrity and semantic source lock PASS.** V29 closeout passed before this volume opened. All 207 images were directly reviewed in order and recorded in `_staging/verification/V30_review_progress.json`. The [V30 canonical reading](../02%20Sequential%20Readings/OPM_V30_DEEP_READING.md) records the exact map and observations. Japanese/register PASS, prospective freeze, V1 comparison, checkpoint and propagation are complete; final readback owns the next-volume gate.

## Exact source object

| Field | Value |
|---|---|
| Immutable input | `OPM_SOURCE_ROOT\One Punch Man - Volume 30 [Japanese].cbz` |
| Bytes | 130,364,472 |
| SHA-256 | `59135310fd0cd775a14a51f8885e8206f9348536b45cd6eb80cc3b8a3636cfd8` |
| Entries | 208: 207 JPEG images plus `ComicInfo.xml` |
| Image order | `0001.jpg`–`0207.jpg`; archive, numeric and lexicographic order agree |
| Dimensions | All 207 images at 1221 × 1920 |
| ComicInfo metadata | 311 bytes; Japanese Volume 30, ONE / Yusuke Murata, right-to-left, 207 pages |
| Metadata SHA-256 | `4b8e1513a1b607f7aaa373971b1a47c016963fb8a1fa430a35570fedf68817fb` |
| Build manifest | `manifests/volume_30.json` |
| Build-manifest SHA-256 | `dbaab9af423e5682ed5b359b647a677cbf8195461ce13bb71ebb760281e5656d` |

The metadata's `Count=34` remains a historical build field. Every image passed CRC/full decode and supplied-manifest byte/dimension comparison. No duplicate member, unsafe/encrypted path, missing index, exact-byte duplicate or identical decoded RGB image was found. No near-duplicate semantic conclusion is claimed. The immutable source hash matches the prior collection inventory.

Receipt: `_staging/verification/V30_integrity.json`, checked `2026-09-12T23:42:18.483007+00:00`. Unchanged extracted bytes live only under `_staging/cache/V30/images/`. This cache is not a canonical image archive or Git payload.

## Verified identity, boundaries and next gate

Cover 0001/title 0005 identify `最大の壁`; contents 0008 lists chapters 151–156 and `王の風格` extra (`王` read `キング`). Directly verified spans are: front matter 0001–0008; 151 title/narrative 0009–0037 plus art 0038; 152 0039–0071 plus art 0072; 153 0073–0101 plus art 0102; 154 0103–0130; 155 0131–0167 plus art 0168; 156 0169–0195; extra 0196–0201; credits/colophon/publisher mark 0202–0204; physical cover/spine/flap reproductions 0205–0207. No narrative gap or duplicate narrative sequence was identified; repeated Genos/King intervention staging is an intentional intercut, not a duplicated archive member.

The colophon identifies Volume 30, ONE, 村田雄介 and 集英社, gives 2024 for first and digital publication, and states digital re-editing. No month/day is supplied by this source page. Metadata and filename identity agree with visual identity. The publication extra is undated within story chronology.

The prospective reading discloses incidental later-heading/summary-line exposure during the prior combined V1 comparison. The full combined V29–V30 legacy reading was subsequently reopened only after the V30 prospective freeze and Japanese/register PASS. The [V30 update manifest](../08%20Audits%20and%20Manifests/OPM_V30_UPDATE_MANIFEST.md) owns final readback before V31. Git remains gated until V37 plus corpus-wide audit.


## Final semantic source lock

Cover 0001 and title 0005 identify Volume 30 `最大の壁`. Images 0001–0008 are front matter: cover; Murata note/digital-fiction notice; ONE note; Garou/fiction illustration; Saitama/King game title image; cast; cast/recap; cast/contents.

| Contents label on 0008 | Printed start | Directly verified archive span |
|---|---:|---|
| 151撃目 `助太刀` | 7 | 0009–0037 title/narrative; 0038 attached Bang/Atomic meal art |
| 152撃目 `劇物` | 37 | 0039–0071 title/narrative; 0072 attached Tatsumaki art |
| 153撃目 `一線` | 71 | 0073–0101 title/narrative; 0102 attached Golden Sperm art |
| 154撃目 `伏兵` | 101 | 0103–0130 title/narrative; no separate attached art |
| 155撃目 `師と弟子` | 129 | 0131–0167 title/narrative; 0168 attached Genos portrait |
| 156撃目 `最大の壁` | 167 | 0169–0195 title/narrative; no separate attached art |
| 番外編 `王の風格` (`王` with `キング` reading) | 194 | 0196–0201; title integrated into opening narrative |

End matter: 0202 design credits; 0203 digital colophon; 0204 publisher mark; 0205 physical spine/back/flap reproduction; 0206 inner back-cover King art; 0207 inner front-cover Saitama art. The colophon gives 2024 for first and digital publication, without month/day. Printed starts are contents references; archive ordinals above are the stable local citation system. The digital extra reproductions are not additional numbered chapters or later narrative. All spans were established from images before this map was finalized.

The exact map above is copied from the frozen prospective reading. Source and cache hashes are reverified by the freeze and closeout receipts. All 207 images are covered exactly once by the disjoint front/chapter-plus-art/extra/end spans. No new edition or web material is used.
