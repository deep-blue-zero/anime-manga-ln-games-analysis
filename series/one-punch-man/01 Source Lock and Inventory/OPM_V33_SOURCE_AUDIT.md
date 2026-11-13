---
series: OPM
artifact_type: source_audit
scope: V33 complete mechanical and semantic source lock
generation: V2
status: canonical
source_boundary: Japanese tankobon V33; mechanical and semantic PASS
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
created: 2026-09-12
workspace_state: local_staged_unintegrated
archive_integrity: PASS
semantic_source_lock: PASS
sequential_reading: COMPLETE
---

# One Punch Man — V33 Source Audit

## Current disposition

**Mechanical and semantic PASS; complete sequential reading and post-freeze stages.** V32 closed before V33 opened. All 223 images were directly viewed in order, with 112 distinct targeted reinspections. Original detail was requested; the tool transported 1303 × 2048 images at 1248 × 1961, while source/cache bytes remained unchanged. The [canonical reading](../02%20Sequential%20Readings/OPM_V33_DEEP_READING.md) and [update manifest](../08%20Audits%20and%20Manifests/OPM_V33_UPDATE_MANIFEST.md) own interpretation and final readback. V34 remains gated until PASS.

## Exact source object

| Field | Value |
|---|---|
| Input | `OPM_SOURCE_ROOT\One Punch Man - Volume 33 [Japanese].cbz` |
| Bytes | 107,999,277 |
| SHA-256 | `121d8b45e1c0be7fbd4fe4c0121161656ecaaa693e3b63786cc5d6596e8b76fd` |
| Entries / images | 224 / 223 JPEGs plus `ComicInfo.xml` |
| Order | 0001.jpg–0223.jpg; archive/numeric/lexicographic agreement |
| Dimensions | all 1303 × 2048 |
| Metadata | 311 bytes; Japanese V33, ONE / Yusuke Murata, RTL, 223 pages |
| Metadata SHA-256 | `1ee74d42af7a3113742a8227f7784413a2677c2b0c6db434c75ff95043651702` |
| Build manifest | `manifests/volume_33.json` |
| Build-manifest SHA-256 | `72973f71d9064e60b7c45ee637938b3531c2e5319c2b801624fac5bf5586d0d6` |

Fresh CRC/full decode, supplied-manifest byte/dimension match and exact-byte/decoded-RGB duplicate checks passed. No duplicate entry, unsafe/encrypted member or missing index was found. Historical metadata Count=34 does not limit current holdings. Receipt `_staging/verification/V33_integrity.json`, checked `2026-09-13T03:24:37.860077+00:00`. Cache remains noncanonical and excluded from Git.

## Identity and remaining gate

Cover/title/contents confirm Volume 33 `二乗`. Contents at 0008 lists chapters 168–171 and bonus `駆動騎士の噂`, with printed starts 7/49/105/159/211. Actual starts are 0009/0051/0107/**0160** and bonus 0213; the single color chapter-171 title makes a uniform plus-two mapping unreliable. Main narrative ends 0212, bonus 0217; credits/logo/extra covers occupy 0218–0222, followed by the 2025 year-only digital colophon at 0223. Black/typography pages are directly accounted for. V33 legacy/checkpoint reopening followed Japanese/register PASS and prospective freeze. Prior prediction/heading exposure and unverified later claims misplaced in the V32 legacy account are disclosed; no V34 primary or web narrative is admitted. The later-event assertions encountered in V33/mixed legacy prose are separately rejected and quarantined after freeze. Git remains gated until V37 and corpus audit.


## Final semantic source lock

Cover 0001 and title 0005 identify Volume 33, `二乗`. Front 0001–0008 contains cover, ONE note/fiction and color-reproduction notice, Murata note, chibi fiction notice, title illustration, cast/recap montage and contents. Contents 0008 lists four numbered chapters and one bonus:

| Contents label at 0008 | Printed start | Archive boundary status |
|---|---:|---|
| 168撃目 `神魔よりも` (ruby `やま` over `神魔`) | 7 | 0009 title; 0010–0049 narrative; 0050 attached King joke |
| 169撃目 `神に仇なす忌むべき拳` | 49 | 0051 title; 0052–0105 narrative; 0106 dark transitional art |
| 170撃目 `絶対悪` | 105 | 0107 title; 0108–0159 narrative |
| 171撃目 `二乗` | 159 | 0160 single color title; 0161–0212 narrative, main-volume ending at 0212 |
| 番外編 `駆動騎士の噂` | 211 | 0213–0217, explicit bonus ending at 0217 |

0218 contains original-publication/design credits; 0219 the digital logo; 0220–0222 extra cover/spine/flap/board reproductions; 0223 the digital colophon (2025, year only). The whole archive order is accounted for. The chapter-171 color title is **0160**, one image before the position that an untested printed-start-plus-two rule would imply. Main-story image 0210 visibly carries printed 208, and the bonus starts at 0213. Keep the observed single color title and actual endpoints; do not force all positions into one offset formula. The black page at 0194 and typography pages at 0204–0205 are intentional source content.

Exact map copied from frozen sections 0–15. Disjoint spans: front 0001–0008; chapter-plus-art 0009–0050,0051–0106,0107–0159,0160–0212; bonus 0213–0217; endmatter 0218–0223. Every image is accounted for once.
