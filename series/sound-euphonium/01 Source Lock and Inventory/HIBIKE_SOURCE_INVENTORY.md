---
series: HIBIKE
artifact_type: source_inventory
scope: V2_PHASE0
media: Japanese prose and official paratext
generation: V2
status: canonical
source_boundary: "Verified Japanese EPUB core HIBIKE-V01 through HIBIKE-V14, V1 OCR provenance, acquired Kyoto Animation illustration paratext, and identified supplemental-source candidates as of 2026-08-19"
supersedes: null
superseded_by: null
do_not_use_as_current_authority: false
---

# Sound! Euphonium V2 — Source Inventory

## 1. Purpose and authority

This inventory records the source corpus available to the V2 *Sound! Euphonium* project at the close of Phase 0. It separates:

1. the **locked Japanese prose core** used as governing literary and linguistic evidence;
2. V1 OCR/source packs retained only for provenance and historical comparison;
3. acquired adaptation/visual paratext;
4. known but presently unacquired or future supplemental prose;
5. material explicitly outside the novel-primary authority layer.

The governing bibliographic baseline is the current official Takarajimasha fourteen-book series set. The project assigns stable source IDs `HIBIKE-V01` through `HIBIKE-V14` in **publication chronology**, including the two Rikka/Tachibana novels as V05–V06. This differs from V1's ten-unit analytical numbering and must not be conflated with it.

Official fourteen-book set reference:
`https://store.tkj.jp/shopdetail/000000022019/`

Canonical primary-source Drive route:
`Primary Sources/Sound Euphonium/Epub + PDF/`

Canonical OCR provenance route:
`Primary Sources/Sound Euphonium/OCR/`

---

## 2. Core Japanese prose EPUB inventory

All fourteen listed EPUBs have passed the V2 structural/readability audit: ZIP integrity, valid EPUB mimetype, valid container-to-OPF resolution, coherent spine, Japanese text availability, ruby preservation, no detected encrypted content, zero Unicode replacement characters in prose XHTML, and no observed NUL corruption. Package provenance varies; several are retail-ebook-derived/conversion packages rather than demonstrably untouched publisher-native EPUB archives. The **verified Japanese text is authoritative; package-generated romanization or incidental metadata is not**.

| ID | Japanese title | Publication | ISBN | V2 file | SHA-256 | Audit |
|---|---|---:|---|---|---|---|
| HIBIKE-V01 | 『響け！ ユーフォニアム　北宇治高校吹奏楽部へようこそ』 | 2013-12-05 | 978-4-8002-1747-9 | `Sound! Euphonium - Novel 01 - Kitauji High School Concert Band Welcome [Japanese].epub` | `8b03b3aad0555b22cbb0ebe2f19b1adf9f3919b60487395dae0ab7958488e288` | PASS |
| HIBIKE-V02 | 『響け！ ユーフォニアム 2　北宇治高校吹奏楽部のいちばん熱い夏』 | 2015-03-05 | 978-4-8002-3906-8 | `Sound! Euphonium - Novel 02 - Kitauji High School Concert Band The Hottest Summer [Japanese].epub` | `fda7b77e5028f8e50d55cbffe883b3b63b57cf35d0abc1618e620b40c504cf12` | PASS |
| HIBIKE-V03 | 『響け！ ユーフォニアム 3　北宇治高校吹奏楽部、最大の危機』 | 2015-04-04 | 978-4-8002-3982-2 | `Sound! Euphonium - Novel 03 - Kitauji High School Concert Band The Greatest Crisis [Japanese].epub` | `81a7ebcb03bda07cdb6b43efd1e1c50301d866cb883cee421a65086cea95b013` | PASS |
| HIBIKE-V04 | 『響け！ ユーフォニアム　北宇治高校吹奏楽部のヒミツの話』 | 2015-05-25 | 978-4-8002-4119-1 | `Sound! Euphonium - Novel 04 - Kitauji High School Concert Band Secret Story [Japanese].epub` | `999645e5f9f4405dc9d2e1d5a2938c9ffcb8f377f42e6c2a4a8265e302fa25b5` | PASS |
| HIBIKE-V05 | 『響け！ ユーフォニアムシリーズ　立華高校マーチングバンドへようこそ 前編』 | 2016-08-04 | 978-4-8002-5872-4 | `Sound! Euphonium - Novel 05 - Rikka High School Marching Band Welcome Part 1 [Japanese].epub` | `99623910c375268a3443920ca464c51cbf2fb3f86094948cc22d4f607bf6a780` | PASS |
| HIBIKE-V06 | 『響け！ ユーフォニアムシリーズ　立華高校マーチングバンドへようこそ 後編』 | 2016-09-06 | 978-4-8002-5874-8 | `Sound! Euphonium - Novel 06 - Rikka High School Marching Band Welcome Part 2 [Japanese].epub` | `e14b74c7829ed30ae2447587b5a1bbded5621d1faf571f3201fb639d673e16b2` | PASS |
| HIBIKE-V07 | 『響け！ ユーフォニアム　北宇治高校の吹奏楽部日誌』 | 2016-10-06 | 978-4-8002-6226-4 | `Sound! Euphonium - Novel 07 - Kitauji High School Concert Band Diary [Japanese].epub` | `18e15066adabd7875d85509a570ef70790862da2a4313c88861310dea749f077` | PASS |
| HIBIKE-V08 | 『響け！ ユーフォニアム　北宇治高校吹奏楽部、波乱の第二楽章 前編』 | 2017-08-26 | 978-4-8002-7489-2 | `Sound! Euphonium - Novel 08 - Kitauji High School Concert Band Turbulent Second Movement Part 1 [Japanese].epub` | `478652db40270358fa36bede8a835076abe22a86177c251851623850dfc4b8cb` | PASS |
| HIBIKE-V09 | 『響け！ ユーフォニアム　北宇治高校吹奏楽部、波乱の第二楽章 後編』 | 2017-10-05 | 978-4-8002-7491-5 | `Sound! Euphonium - Novel 09 - Kitauji High School Concert Band Turbulent Second Movement Part 2 [Japanese].epub` | `3a5249c76be8618cf386fab5a9b3ab307ab424be09d7517665c77305fdbd1fb2` | PASS |
| HIBIKE-V10 | 『響け！ ユーフォニアム　北宇治高校吹奏楽部のホントの話』 | 2018-04-05 | 978-4-8002-8301-6 | `Sound! Euphonium - Novel 10 - Kitauji High School Concert Band True Story [Japanese].epub` | `04ae787ac0b852b5b83cf2077d602a242b31dd9c39b4e0fc71fb5467e3c477c1` | PASS |
| HIBIKE-V11 | 『響け！ ユーフォニアム　北宇治高校吹奏楽部、決意の最終楽章 前編』 | 2019-04-17 | 978-4-8002-9399-2 | `Sound! Euphonium - Novel 11 - Kitauji High School Concert Band Decisive Final Movement Part 1 [Japanese].epub` | `56cc0592af7aff896dbffbb4f23444ee4e497e783a94f1338630bf6c82c0da45` | PASS |
| HIBIKE-V12 | 『響け！ ユーフォニアム　北宇治高校吹奏楽部、決意の最終楽章 後編』 | 2019-06-22 | 978-4-8002-9401-2 | `Sound! Euphonium - Novel 12 - Kitauji High School Concert Band Decisive Final Movement Part 2 [Japanese].epub` | `5e98951d0a5e7829d6cc99f37acedb3926a04664d032a17b231dee8242bbf46b` | PASS |
| HIBIKE-V13 | 『飛び立つ君の背を見上げる』文庫版 | 2023-08-04 | 978-4-299-04598-0 | `Sound! Euphonium - Novel 13 - Watching You Take Flight [Japanese].epub` | `0728962b4793b2b59911cb332a0db174d47237a6e95011ffa408e2a91a1b733e` | PASS |
| HIBIKE-V14 | 『響け！ ユーフォニアム 北宇治高校吹奏楽部のみんなの話』 | 2024-06-27 | 978-4-299-05621-4 | `Sound! Euphonium - Novel 14 - Kitauji High School Concert Band Everyone's Story [Japanese].epub` | `b80455a6106a0a3fd54ff59826363d6a7f698efc710c1521e838501dbdfe24e9` | PASS |

### 2.1 Official publisher references

- V01: `https://tkj.jp/book/?cd=72174701`
- V02: `https://tkj.jp/book/?cd=72390601`
- V03: `https://tkj.jp/book/?cd=72398201`
- V04: `https://tkj.jp/book/?cd=72411901`
- V05: `https://tkj.jp/book/?cd=72587201`
- V06: `https://tkj.jp/book/?cd=72587401`
- V07: `https://tkj.jp/book/?cd=72622601`
- V08: `https://tkj.jp/book/?cd=72748901`
- V09: `https://tkj.jp/book/?cd=72749101`
- V10: `https://tkj.jp/book/?cd=72830101`
- V11: `https://tkj.jp/book/?cd=TD293992`
- V12: `https://tkj.jp/book/?cd=TD294012`
- V13: `https://tkj.jp/book/?cd=TD045980`
- V14: `https://tkj.jp/book/?cd=TD056214`

### 2.2 Structural audit summary

| ID | Bytes | Spine items | XHTML files | Ruby elements | Extracted text chars | Replacement chars | Encryption manifest |
|---|---:|---:|---:|---:|---:|---:|---|
| V01 | 306,300 | 13 | 13 | 203 | 146,295 | 0 | none |
| V02 | 319,329 | 13 | 13 | 208 | 153,098 | 0 | none |
| V03 | 1,524,543 | 13 | 14 | 227 | 183,575 | 0 | none |
| V04 | 3,126,240 | 36 | 37 | 150 | 102,711 | 0 | none |
| V05 | 1,455,914 | 16 | 17 | 226 | 160,138 | 0 | none |
| V06 | 1,184,859 | 15 | 16 | 220 | 163,172 | 0 | none |
| V07 | 12,633,513 | 64 | 66 | 284 | 127,301 | 0 | none |
| V08 | 1,607,137 | 13 | 14 | 320 | 187,172 | 0 | none |
| V09 | 2,083,635 | 15 | 17 | 293 | 184,558 | 0 | none |
| V10 | 2,864,738 | 34 | 35 | 512 | 122,357 | 0 | none |
| V11 | 1,090,111 | 14 | 15 | 285 | 176,310 | 0 | none |
| V12 | 1,074,880 | 13 | 14 | 264 | 173,918 | 0 | none |
| V13 | 2,444,487 | 24 | 25 | 221 | 145,101 | 0 | none |
| V14 | 2,456,230 | 35 | 36 | 506 | 109,397 | 0 | none |

The counts are integrity diagnostics, not literary measures. Illustrated/guide/anthology structures naturally produce different spine and text counts.

### 2.3 Hybrid-volume evidence rules

- **V07 — 『北宇治高校の吹奏楽部日誌』** is a hybrid guide/prose publication. Takeda-authored fiction is primary literary evidence; interviews, reference material, and editorial guide matter are paratext unless specifically attributed otherwise.
- **V13 — 『飛び立つ君の背を見上げる』文庫版** contains the prose story `記憶のイルミネーション`, originally distributed as a first-edition bonus with the 2021 hardcover. The current locked EPUB therefore already supplies that text; no separate bonus booklet is required for textual completeness.
- Commentary, afterwords, publisher descriptions, covers, and illustration emphasis are paratext and must not be silently treated as narrative fact.

### 2.4 Metadata caveats

The source archive preserves original/provenance filenames even when those filenames contain bad bibliographic metadata. Two known examples must **not** be propagated into V2 authority:

- the archived source filename associated with V03 carries the wrong ISBN `9784800217479`; official V03 ISBN is `978-4-8002-3982-2`;
- the archived source filename associated with V09 carries the wrong ISBN `9784800274892`; official V09 ISBN is `978-4-8002-7491-5`.

Likewise, automated Calibre/Kobo romanizations are not bibliographic authority. Japanese title/author strings and publisher-verified metadata govern.

---

## 3. V1 OCR/source-pack inventory

The V1 project used ten OCR/source packs. They are retained intact under `Primary Sources/Sound Euphonium/OCR/` as **historical provenance and fallback evidence only**. They are not exact-wording authority once a locked EPUB is available.

| V1 OCR pack | Official V2 source correspondence | V2 disposition |
|---|---|---|
| `hibike_euphonium_volume_01_analysis_pack.zip` | HIBIKE-V01 | historical legacy; EPUB supersedes wording authority |
| `hibike_euphonium_volume_02_analysis_pack.zip` | HIBIKE-V02 | historical legacy; EPUB supersedes wording authority |
| `hibike_euphonium_volume_03_analysis_pack.zip` | HIBIKE-V03 | historical legacy; EPUB supersedes wording authority |
| `hibike_euphonium_volume_04_analysis_pack.zip` | HIBIKE-V04 | historical legacy; EPUB supersedes wording authority |
| `hibike_euphonium_volume_05_analysis_pack.zip` | **HIBIKE-V07** | historical legacy; V1 numbering hazard |
| `hibike_euphonium_volume_06_analysis_pack.zip` | **HIBIKE-V08** | historical legacy; V1 numbering hazard |
| `hibike_euphonium_volume_07_analysis_pack.zip` | **HIBIKE-V09** | historical legacy; V1 numbering hazard |
| `hibike_euphonium_volume_08_analysis_pack.zip` | **HIBIKE-V10** | historical legacy; V1 numbering hazard |
| `hibike_euphonium_volume_09_analysis_pack.zip` | **HIBIKE-V11** | historical legacy; V1 numbering hazard |
| `hibike_euphonium_volume_10_analysis_pack.zip` | **HIBIKE-V12** | historical legacy; V1 numbering hazard |

No V1 OCR packs cover HIBIKE-V05, V06, V13, or V14. Those four are genuine V2 source-boundary expansions, not merely clean-text replacements.

---

## 4. Acquired adaptation/visual paratext

### KyoAni Official Illustration Works

- File: `Sound! Euphonium - Reference - Official Illustration Works [Japanese].pdf`
- Type: official Kyoto Animation illustration/visual paratext
- Size: 182,072,237 bytes
- SHA-256: `5ab8c96ff4508031dca507a744bf4f6a9b1b4ba4add0508ae3cf8ade82e4616b`
- Evidence class: **adaptation/visual paratext**
- Admission: acquired, indexed, **excluded from governing novel-text authority**
- Appropriate use: embodiment/design history, visual relationship framing, adaptation comparison, recurring pose/expression/presentation choices
- Inappropriate use: settling Takeda-prose wording, novel-canonical internal states, or novel-only continuity disputes

---

## 5. Supplemental-source candidates

Detailed decisions are governed by `HIBIKE_SUPPLEMENTAL_SOURCE_AUDIT.md`. Summary:

| Candidate | Current status | Phase-1 blocker? | Proposed evidence class |
|---|---|---:|---|
| 2023 *Ensemble Contest* Takeda theatrical stories ×3 | identified; unacquired | No | official author-written adaptation-adjacent supplemental prose |
| 2026 *Final Chapter* Part I Takeda theatrical stories ×3 | identified; unacquired | No | official author-written adaptation-adjacent supplemental prose |
| 2021 *5th Anniversary Disc* 48P booklet Takeda short story | identified; title/content not yet inventoried | No | official author-written adaptation paratext / supplemental candidate |
| `記憶のイルミネーション` | **already contained in HIBIKE-V13** | No | locked core prose via V13 |
| 『北宇治高校の吹奏楽部日誌2』 | unreleased as of 2026-08-19; release 2026-09-10 | No | future canonical prose supplement candidate |
| Anime scripts/scenario books | optional future | No | adaptation evidence only |
| Animation setting/design books | optional future | No | adaptation/design paratext |
| Manga adaptations | optional future | No | adaptation evidence only |
| Audio dramas | optional future | No | adaptation/performance evidence unless they contain independently authored new prose |

---

## 6. Locator standard for Phase 1

The locked EPUBs will use the deterministic locator grammar:

`HIBIKE-VXX / SNN / P#### / <short exact Japanese cue>`

Where:

- `VXX` = the locked publication-sequence source ID;
- `SNN` = zero-padded OPF spine ordinal for the relevant content item;
- `P####` = normalized prose-paragraph ordinal within that content item;
- the short Japanese cue is a human-verification aid, not the sole locator.

When each volume enters deep reading, its locator map must preserve:

- original OPF spine position;
- source XHTML path/name;
- generated paragraph ordinal;
- exact Japanese punctuation/orthography for quoted evidence.

Search-only references such as “the scene where Kumiko talks to Reina” are insufficient for evidence-grade claims.

---

## 7. Phase 0 disposition

**Core acquisition and integrity gate: PASS.**

The fourteen-volume Japanese prose core is complete and suitable for V2 sequential reading. Supplemental gaps are explicitly known and do not prevent Phase 1 because they are either adaptation-adjacent, already absorbed into the locked core, or future/unreleased.

Authority now passes to `HIBIKE_SOURCE_LOCK.md` for the immutable Phase-1 source boundary.
