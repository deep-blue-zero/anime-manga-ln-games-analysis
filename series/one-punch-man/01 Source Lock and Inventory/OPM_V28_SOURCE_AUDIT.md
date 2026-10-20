---
series: OPM
artifact_type: source_audit
scope: V28 mechanical integrity, complete sequential review and semantic source lock
generation: V2
status: canonical
source_boundary: Japanese tankobon V28; mechanical integrity and complete semantic source lock PASS
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
created: 2026-09-12
workspace_state: local_staged_unintegrated
archive_integrity: PASS
semantic_source_lock: PASS
sequential_reading: COMPLETE
---

# One Punch Man — V28 Source Audit

## Current sequential reading status — 2026-09-12

**PASS — all 216 images directly reviewed in order, mechanically verified and semantically mapped.** Six numbered chapters (138–143), attached illustrations, the four-page `嗅覚` extra and digital end matter are covered. The [V28 reading](../02%20Sequential%20Readings/OPM_V28_DEEP_READING.md) and [Japanese/register audit](../08%20Audits%20and%20Manifests/OPM_V28_JAPANESE_DIALOGUE_AND_REGISTER_AUDIT.md) are complete. The final map below and the current metadata supersede the explicitly historical step-5 inspection limits retained here. The [update manifest](../08%20Audits%20and%20Manifests/OPM_V28_UPDATE_MANIFEST.md) owns closeout readback and the V29 gate.

## Bootstrap disposition — historical step 5

**PASS for mechanical archive integrity and front-matter identity. Semantic source lock remains PENDING.** This audit completes bootstrap step 5. It does not establish chapter-to-image boundaries, review all story panels, or begin the V28 deep reading.

## Exact source object

| Field | Verified value |
|---|---|
| Filename | `One Punch Man - Volume 28 [Japanese].cbz` |
| Immutable local path | `OPM_SOURCE_ROOT\One Punch Man - Volume 28 [Japanese].cbz` |
| Bytes | 126,817,320 |
| SHA-256 | `62d76b41823c35eb49e18229a4e28a89194088e496dc33db5140f00588605a28` |
| Archive entries | 217 |
| Image entries | 216 JPEG files, including front/end matter |
| Metadata | `ComicInfo.xml`, 311 bytes |
| Deterministic image order | `0001.jpg` through `0216.jpg`; archive, numeric and lexicographic orders agree |
| Dimensions | 215 images at 1221 × 1920; one at 884 × 1200 |

`ComicInfo.xml` identifies Volume 28, ONE, Yusuke Murata, Japanese, right-to-left manga and 216 pages. Its `Count=34` belongs to the historical archive build; it is not the present acquisition boundary or a claim about the current published total. Metadata SHA-256: `48c722d3885fe7540de86b66de6f875e4c15e66818f2f456125758f8ca8da757`.

## Integrity checks

- Every archive entry was read with ZIP CRC validation. Every image passed Pillow verification and complete pixel decoding.
- Every image byte hash and dimension pair matches `manifests/volume_28.json` in the source root. That supplied manifest's SHA-256 is `55a912648238de4621db8b551f5142384a2c11e5c24074d5f8d941e0f81dbb5f`.
- No missing numeric index, duplicate entry name, unsafe path, encrypted member, exact duplicate image bytes or identical decoded RGB image was found in the retained archive.
- The supplied historical build records 217 input images and one exact duplicate removal, leaving 216 retained images. The CBZ was not rebuilt or altered. Near-duplicate visual similarity was not reassessed; byte/pixel identity checks do not substitute for semantic review.

The per-image receipt records CRC, byte hash, decoded RGB hash, dimensions and manifest comparison. Full decoding establishes file usability, not human review of every image.

## Bootstrap front-matter inspection and printed contents — historical step 5

Only images **0001, 0007 and 0008** were visually inspected: cover, cast page, and contents/prior-story recap. The cover visibly identifies Japanese Volume 28, `深淵へ`, with ONE/Murata and Jump Comics branding. Eight front-matter candidates were extracted as unchanged source bytes under the staging cache; extraction is not counted as visual reading. **Zero sequential narrative images were reviewed.**

The contents page at `image:0008` supplies these printed starts:

| Collected label | Japanese title | Printed page | Archive-image boundary |
|---|---|---:|---|
| 138撃目 | ねじれ | 7 | PENDING |
| 139撃目 | 巨大バリア | 35 | PENDING |
| 140撃目 | 醜態と基本 | 73 | PENDING |
| 141撃目 | 不屈 | 87 | PENDING |
| 142撃目 | 共鳴 | 123 | PENDING |
| 143撃目 | 深淵へ | 159 | PENDING |
| 番外編 | 嗅覚 | 204 | PENDING |

Do not convert printed starts to archive indices using an assumed offset. Chapter ends, any attached omake, bonus-manga limits and remaining edition/end matter require the next sequential visual pass. No semantic range is promoted into the crosswalk here.

## Evidence routes and historical bootstrap next gate

- Machine receipt: `_staging/verification/V28_integrity.json` beneath the analytical staging root.
- Source inventory receipt: `_staging/verification/source_inventory.json`.
- Temporary raw front matter: `_staging/cache/V28/front_matter/`.
- Canonical routing: [current corpus map](../CURRENT_STATE_AND_CORPUS_MAP.md), [source inventory](OPM_SOURCE_INVENTORY.md), [chapter/extra crosswalk](OPM_TANKOBON_CHAPTER_AND_EXTRA_CROSSWALK.md).

The next operation is the V28 prospective reading and semantic mapping from the frozen V27 observational boundary. Japanese/register audit, prospective freeze, legitimate V1 comparison, checkpoint scoring and administrative closure follow in the established order. V29 remains unopened until V28 closes. The [bootstrap audit](../08%20Audits%20and%20Manifests/OPM_V28_BOOTSTRAP_AUDIT.md) records prior checkpoint exposure and the user's steps 1–5 stopping boundary.


## Final semantic source lock — V28 closeout

The contents page is `0008`. Printed starts below are transcribed from that page. All archive boundaries are now directly verified; titles, attached illustrations, the extra and digital packaging are distinguished.

| Surface | Printed start | Directly verified archive range | Status |
|---|---:|---|---|
| Front matter / author notes / title / cast / contents | — | `0001–0008` | reviewed |
| `138撃目 ねじれ` | 7 | `0009–0035` title/narrative; `0036` attached laundry vignette | reviewed; next start verified |
| `139撃目 巨大バリア` | 35 | `0037–0073` title/narrative; `0074` attached Atomic Samurai/Iaian illustration | reviewed; next start verified |
| `140撃目 醜態と基本` | 73 | `0075–0087` title/narrative; `0088` attached Amai Mask portrait | reviewed; next start verified |
| `141撃目 不屈` | 87 | `0089–0123` title/narrative; `0124` attached Child Emperor illustration | reviewed; next start verified |
| `142撃目 共鳴` | 123 | `0125–0159` title/narrative; `0160` attached fused Psykos illustration | reviewed; next start verified |
| `143撃目 深淵へ` | 159 | `0161–0205` title/narrative; final spread `0204–0205` | reviewed; main narrative ends here |
| `番外編 嗅覚` | 204 | `0206–0209` | reviewed; four-page Watchdog Man extra; volume end mark at `0209` |
| Credits / digital colophon / imprint | — | `0210–0212` | reviewed; non-narrative |
| Digital extra cover reproductions | — | `0213–0215` | reviewed; back/spine/flap, body back and body front |
| Terminal digital cover | — | `0216` | reviewed; 884 × 1200 image, not a new narrative page |

Printed pages 10 and 11 are directly visible at images `0012` and `0013`, and 170 and 171 at `0172` and `0173`; the narrative uses printed page = archive image − 2. Archive ordinals remain the primary exact locator. The title, author credits and digital-edition fiction notice appear in front matter. Author comments and chapter illustrations are paratext, not diegetic episodes: the recreational vehicle group at `0009` does not establish an actual outing. The colophon at `0211` identifies Volume 28, ONE, Yusuke Murata, Shueisha and 2023 for both first and digital editions; it does not print an exact day. The end covers do not constitute a separate collected chapter.

Mechanical integrity and semantic review have separate receipts: `_staging/verification/V28_integrity.json` records the earlier mechanical check, while `V28_review_progress.json` records all 216 direct image reviews. The old zero-review count in the mechanical receipt is its bootstrap-time observation and is not overwritten. `V28_prospective_freeze.json` fixes the corrected prospective region. No duplicate, gap, chapter-start mismatch or end-matter intrusion into the narrative was found in the complete visual pass. The title/edition identifies 2023 without an exact printed publication day.
