---
series: OPM
artifact_type: source_audit
scope: V36 mechanical integrity and incremental semantic review
generation: V2
status: canonical
source_boundary: Japanese tankobon V36; mechanical and semantic PASS; local closeout complete
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
created: 2026-09-15
workspace_state: local_staged_unintegrated
archive_integrity: PASS
semantic_source_lock: PASS
sequential_reading: COMPLETE_0247_OF_0247
---

# One Punch Man — V36 Source Audit

## Current disposition

**Mechanical and semantic PASS; local closeout complete subject to final readback.** V35's 43-check closeout passed before V36 opened. All images 0001–0247 were directly inspected in strict order, and all 226 locked narrative targets then passed direct Japanese/register reinspection. Original detail was requested; viewer transport reported display resizing from 1303 × 2048 to 1248 × 1961, while source/cache bytes remain unchanged. The [canonical reading](../02%20Sequential%20Readings/OPM_V36_DEEP_READING.md) owns observations, the [register audit](../08%20Audits%20and%20Manifests/OPM_V36_JAPANESE_DIALOGUE_AND_REGISTER_AUDIT.md) owns exact wording/modality limits, and the [V36 update manifest](../08%20Audits%20and%20Manifests/OPM_V36_UPDATE_MANIFEST.md) owns final readback and the V37 gate.

## Exact source object

| Field | Value |
|---|---|
| Input | `OPM_SOURCE_ROOT\One Punch Man - Volume 36 [Japanese].cbz` |
| Bytes | 198,284,447 |
| SHA-256 | `4798a23e92395acbff507b63dd11bdd624a8c507c5143a6f45eca79eed454cdb` |
| Entries / images | 248 / 247 JPEGs plus `ComicInfo.xml` |
| Order / dimensions | 0001.jpg–0247.jpg; archive/numeric/lexicographic agreement; all 1303 × 2048 |
| Metadata | 340 bytes; Japanese V36, ONE / Yusuke Murata, RTL, 247 pages, historical Count=36 |
| Metadata SHA-256 | `c5d0767356e8be7e35a2bd46a6b26135e80e67607af142772186fb134c4dd0cd` |
| Build manifest | `manifests/volume_36.json` |
| Build-manifest SHA-256 | `eb42adb5aca804daca3be8b4c41b61e8575ceb3a1a6260b54df1b93e08a5baba` |

Fresh CRC/full decode, supplied-manifest byte hashes and exact-byte/decoded-RGB duplicate checks passed with no issues. The supplied manifest uses `sha256` and omits dimensions; direct decode measures dimensions, and absent dimension comparisons remain null. Receipt: `_staging/verification/V36_integrity.json`, checked `2026-09-16T02:48:23.201828+00:00`. Original bytes are cached under `_staging/cache/V36/images/`; cache and receipts are noncanonical and excluded from Git.

## Identity and semantic lock

Cover 0001 and title 0005 identify V36 `未知数`. ONE/Murata notes occupy 0002–0003, fiction art 0004, cast/recap 0006–0007 and contents 0008. Contents records printed starts for 182撃目 `超常とリスク`, 183撃目 `外でやれ！`, 184撃目 `目撃`, 185撃目 `取り込み中`, 186撃目 `頭皮と摩擦`, 187撃目 `未知数`, 188撃目 `取引` and 番外編 `最初の勇気`. Direct boundary crossings certify frontmatter 0001–0008; chapter starts 0009, 0045, 0073, 0109, 0143, 0173 and 0211; bonus start 0237; and publication/endmatter 0242–0247.

The complete combined V35–V36 V1 reading was exposed after V35's prospective freeze. Its V36 claims remained non-evidence throughout the primary pass and targeted audit; no fresh blindness is claimed. The audit receipt records 226/226 targets, no post-synthesis V1 reopen and no checkpoint reopen. Exact reinspection confirms the acquaintance/friend distinction, self-assessment versus narrator authority, unknown-limit modality, voluntary group return, institutional bargain/concealment and first-courage scope without a load-bearing correction. Semantic source lock therefore passes. Prospective freeze, V1 comparison, checkpoint adjudication and propagation are complete. V37 narrative and official-web narrative remain outside scope until final V36 readback passes.


## Final semantic source map

| Segment | Exact archive span | Certified function |
|---|---|---|
| Frontmatter | 0001–0008 | cover, creator notes, fiction art, title, cast/recap and contents |
| 182撃目 `超常とリスク` | 0009–0044 | title 0009; narrative 0010–0044 |
| 183撃目 `外でやれ！` | 0045–0072 | title 0045; narrative 0046–0072 |
| 184撃目 `目撃` | 0073–0108 | title 0073; narrative 0074–0108 |
| 185撃目 `取り込み中` | 0109–0142 | title 0109; narrative 0110–0142 |
| 186撃目 `頭皮と摩擦` | 0143–0172 | title 0143; narrative 0144–0172 |
| 187撃目 `未知数` | 0173–0210 | title 0173; narrative 0174–0210 |
| 188撃目 `取引` | 0211–0236 | title 0211; narrative 0212–0236 |
| 番外編 `最初の勇気` | 0237–0241 | title and narrative 0237; narrative through 0241 |
| Publication/endmatter | 0242–0247 | creator/publication pages, digital colophon and package material |

Disjoint spans: front 0001–0008; chapters 0009–0044, 0045–0072, 0073–0108, 0109–0142, 0143–0172, 0173–0210 and 0211–0236; bonus 0237–0241; endmatter 0242–0247. Every image is accounted for once. All 247 source images retain their original `.jpg` filenames and bytes. This exact post-freeze map supersedes only the provisional-ending wording in frozen prospective section 1; no prospective observation or claim changes.
