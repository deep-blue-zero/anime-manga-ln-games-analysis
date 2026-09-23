---
series: OPM
artifact_type: source_audit
scope: V34 complete mechanical and semantic source lock
generation: V2
status: canonical
source_boundary: Japanese tankobon V34; mechanical and semantic PASS
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
created: 2026-09-13
workspace_state: local_staged_unintegrated
archive_integrity: PASS
semantic_source_lock: PASS
sequential_reading: COMPLETE
---

# One Punch Man — V34 Source Audit

## Current disposition

**Mechanical and semantic PASS; complete sequential reading and post-freeze stages.** V33's 41-check closeout passed before V34 opened. All 224 images were directly viewed in order and 139 distinct images reinspected for Japanese/register audit; target pages displayed at native 1222 × 1920. Source/cache bytes remain unchanged. The [canonical reading](../02%20Sequential%20Readings/OPM_V34_DEEP_READING.md) and [update manifest](../08%20Audits%20and%20Manifests/OPM_V34_UPDATE_MANIFEST.md) own analysis and final readback. V35 remains gated until PASS.

## Exact source object

| Field | Value |
|---|---|
| Input | `OPM_SOURCE_ROOT\One Punch Man - Volume 34 [Japanese].cbz` |
| Bytes | 97,684,009 |
| SHA-256 | `2d5952153d956079fb04fe7137eb04d4b7b8ffe9dcfce6db78ba3ff21fce6bc7` |
| Entries / images | 225 / 224 JPEG images plus `ComicInfo.xml` |
| Order | 0001.jpeg, then 0002.jpg–0224.jpg; archive/numeric-stem/lexicographic agreement |
| Dimensions | 0001.jpeg 884 × 1200; remaining images 1222 × 1920 |
| Metadata | 311 bytes; Japanese V34, ONE / Yusuke Murata, RTL, 224 pages |
| Metadata SHA-256 | `6485a6dbb6c961863cc9f5543a1b3212f0e84d4f2af6df672df2fe8aa80e84a3` |
| Build manifest | `manifests/volume_34.json` |
| Build-manifest SHA-256 | `65ac800b628e95b950e3a7ba03d2311d2435063fc0cd94ed3866344fc54816a0` |

Fresh CRC/full decode, supplied-manifest byte/dimension match and exact-byte/decoded-RGB duplicate checks passed. No duplicate entry, unsafe/encrypted member or missing index was found. Historical metadata Count=34 does not limit current holdings. Receipt `_staging/verification/V34_integrity.json`, checked `2026-09-13T04:37:40.635003+00:00`. Cache remains noncanonical and excluded from Git. The generic preparer initially rejected the valid `.jpeg` first extension before extraction; it was corrected to verify numeric stems and preserve original extensions, then preparation passed. `_staging/verification/V34_preparation_compatibility_note.md` records that tool correction, not a source anomaly.

## Identity and remaining gate

Cover/title confirm Volume 34 `夜明け`; 0001–0002 are different cover renditions, both preserved. Frontmatter is 0001–0009; 172 `I.O.` is 0010–0067; 173 `神々の目覚め` is 0068–0147; 174 `夜明け` is 0148–0193; 175 `得たもの` is 0194–0215. Attached art is distinguished in the reading. The unlisted sewing bonus is 0216–0217, attached palms 0218, credits/colophon/logo 0219–0221 and extra cover material 0222–0224. The year-only colophon identifies 2025; directly checked update dates are 2022-07-07, 2022-07-21, 2022-08-04 and 2022-08-18. V34 legacy/checkpoint reopening followed Japanese/register PASS and prospective freeze. Prior prediction/heading exposure and unverified later claims misplaced in earlier legacy accounts are disclosed in the reading. No V35 primary or web narrative is admitted. Git remains gated until V37 and corpus audit.


## Final semantic source lock

Cover renditions 0001–0002 and title 0006 identify Volume 34, `夜明け`. Images 0003–0004 are creator notes; 0005 is the fiction notice; 0007–0008 are the cast/recap montage; 0009 is contents. Its Fubuki beach/Saitama surfboard image is posed paratext, not a new outing or recovery. Contents lists:

| Contents label at 0009 | Printed start | Direct archive confirmation |
|---|---:|---|
| 172撃目 `I.O.` (title ruby イオ) | 7 | 0010 title; 0011–0066 narrative; 0067 attached illustration |
| 173撃目 `神々の目覚め` | 65 | 0068 color title; 0069–0146 narrative; 0147 attached speed-radar gag |
| 174撃目 `夜明け` | 145 | 0148 color title; 0149–0193 narrative |
| 175撃目 `得たもの` | 191 | 0194 color title; 0195–0214 narrative; 0215 attached actress note |

The unlisted bonus `おまけ「裁縫」` occupies 0216–0217, with attached scarred-palms art at 0218. Image 0219 records first-publication and design credits; 0220 is the JCDigital colophon; 0221 is the JCDigital logo. Extra cover/spine/back/flap renditions occupy 0222–0224. All 224 images are accounted for. Printed starts are not alone archive offsets. The 2025 digital colophon supplies a year, not a month/day; 0219 records first-publication updates on 2022-07-07, 2022-07-21, 2022-08-04 and 2022-08-18, as directly checked in the audit. These publication facts do not by themselves establish episode IDs or redraw correspondences.

Exact map copied from frozen sections 0–15. Disjoint spans: front 0001–0009; chapter-plus-art 0010–0067,0068–0147,0148–0193,0194–0215; bonus 0216–0217; attached/endmatter 0218–0224. Every image is accounted for once. The first image retains its original `.jpeg` extension; remaining images retain `.jpg`.
