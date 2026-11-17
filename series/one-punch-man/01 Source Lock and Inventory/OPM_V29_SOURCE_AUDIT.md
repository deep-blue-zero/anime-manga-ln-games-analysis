---
series: OPM
artifact_type: source_audit
scope: V29 mechanical integrity, complete sequential review and semantic source lock
generation: V2
status: canonical
source_boundary: Japanese tankobon V29; mechanical integrity and complete semantic source lock PASS
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
created: 2026-09-12
workspace_state: local_staged_unintegrated
archive_integrity: PASS
semantic_source_lock: PASS
sequential_reading: COMPLETE
---

# One Punch Man — V29 Source Audit

## Current disposition

**PASS — all 199 images directly reviewed in sequence and semantically locked.** Seven numbered chapters (144–150), their attached illustrations and all editorial/cover matter are mapped. No narrative omake follows chapter 150. The [V29 reading](../02%20Sequential%20Readings/OPM_V29_DEEP_READING.md) and [Japanese/register audit](../08%20Audits%20and%20Manifests/OPM_V29_JAPANESE_DIALOGUE_AND_REGISTER_AUDIT.md) are complete. The [update manifest](../08%20Audits%20and%20Manifests/OPM_V29_UPDATE_MANIFEST.md) owns final readback and the V30 gate. The initial inspection state below remains a historical receipt, not the present review count.

## Initial disposition — historical opening check

**Mechanical integrity PASS; complete semantic lock PENDING.** V28 closeout passed before V29 opened. Images 0001–0008 have been directly reviewed; current progress and chapter boundaries belong in the [V29 draft](../02%20Sequential%20Readings/OPM_V29_DEEP_READING.md). No full-volume narrative conclusion is implied by this mechanical audit.

## Exact source object

| Field | Value |
|---|---|
| Immutable input | `OPM_SOURCE_ROOT\One Punch Man - Volume 29 [Japanese].cbz` |
| Bytes | 132,639,923 |
| SHA-256 | `7b31cb0fda3641ad926735233d18e93eb28d5f1f06e848866dfe9b07e980c02d` |
| Entries | 200: 199 JPEG images plus `ComicInfo.xml` |
| Image order | `0001.jpg`–`0199.jpg`; archive, numeric and lexicographic order agree |
| Dimensions | All 199 images at 1303 × 2048 |
| ComicInfo metadata | 311 bytes; Japanese Volume 29, ONE / Yusuke Murata, right-to-left, 199 pages |
| Metadata SHA-256 | `a9fb0b59ee51b0dccab32c45b31abd858a0c8123b1dba9df5f1fefc6ea4dea84` |
| Supplied build manifest | `manifests/volume_29.json` |
| Build-manifest SHA-256 | `e26ca247109dd641e53481627e423a505b84eb7a747a9940fd28d0f3f8088b55` |

The metadata's `Count=34` is a historical build field, not the current collection or publication boundary. The source hash matches the earlier immutable-object inventory. Every retained image passed CRC, full pixel decoding and supplied-manifest byte/dimension comparison. No unsafe or encrypted member, duplicate member name, missing numeric index, exact byte duplicate or identical decoded RGB image was found. This does not substitute for semantic review or assert a new near-duplicate similarity audit.

The exact machine receipt is `_staging/verification/V29_integrity.json`. All extracted bytes remain unchanged beneath `_staging/cache/V29/images/`, outside the source and repository. The volume contains a visible `DL-Raw.Se` mark in the supplied images; source-byte fidelity preserves it, and it is not treated as publisher story text.

## Initial front identity and next gate — historical opening check

Cover 0001 and title 0005 identify `捲土重来`. Contents 0008 lists chapters 144–150, with printed starts recorded in the draft. No archive boundary is inferred solely from the printed offset. Complete chapter ends, attached art, unlisted extras if any, and edition/cover matter must be verified in order. Japanese/register audit, prospective freeze, V1 comparison, checkpoint and cumulative closeout follow the source-first pass. V30 remains unopened; Git remains closed until the V37 and corpus-audit gates.


## Final semantic source lock

Cover 0001, title 0005, contents 0008, the closing mark at 0193 and the colophon at 0195 directly identify Japanese Volume 29, `捲土重来`. The complete ordered inspection establishes the following map.

| Surface / collected label | Printed start on contents 0008 | Direct archive boundaries |
|---|---:|---|
| Cover, author notes, fiction notice, title, cast, recap, contents | — | 0001–0008 |
| 144撃目 `ABYSS` | 7 | 0009–0035 title/narrative; 0036 attached Tatsumaki illustration |
| 145撃目 `石とダイヤ` | 35 | 0037–0055 title/narrative; 0056 attached Metal Bat portrait |
| 146撃目 `捲土重来` | 55 | 0057–0088 title/narrative; no separate attached art |
| 147撃目 `とるべき態度` | 87 | 0089–0101 title/narrative; 0102 attached Fubuki illustration |
| 148撃目 `木星` / `Jupiter, the Bringer of Jollity` | 101 | 0103–0139 title/narrative; 0140 attached Fuhrer Ugly illustration |
| 149撃目 `シルバーファング` | 139 | 0141–0165 title/narrative; 0166 attached Bang illustration |
| 150撃目 `THE BLACK SHINE` | 165 | 0167–0193 title/narrative; volume narrative end mark at 0193 |
| Editorial/design credits, digital colophon, digital end mark | — | 0194–0196 |
| `EXTRA PAGES`: spine/back/flap, inner back cover, inner front cover | — | 0197–0199; cover reproductions, no additional narrative omake |

Printed page 7 at 0009, 162–163 at 0164–0165 and 174–177 at 0176–0179 corroborate printed page = archive image − 2 in the narrative. Archive ordinals remain the exact reference. The colophon identifies ONE, 村田雄介, 集英社 and 2023 for both first and digital editions, without a month/day. The digital re-editing and fiction notices are edition evidence; the supplied `DL-Raw.Se` mark is preserved as part of the local source, not attributed to a character or publisher. Mechanical source integrity and semantic identification are distinct checks.

The mechanical receipt remains `_staging/verification/V29_integrity.json`; complete direct review is recorded in `V29_review_progress.json`, and corrected prospective text is locked by `V29_prospective_freeze.json`. Archive and cached image bytes were reverified at freeze. Initial review counts are historical and are not rewritten. No missing image, exact retained duplicate, chapter-start mismatch or narrative/cover intrusion was found. Source, metadata and build-manifest hashes remain unchanged.
