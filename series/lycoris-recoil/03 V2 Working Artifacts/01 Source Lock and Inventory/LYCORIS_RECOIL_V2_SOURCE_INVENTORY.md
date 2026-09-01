---
series: LYCORIS_RECOIL
artifact_type: source_inventory
scope: V2 primary-source and analytical-derivative corpus audit
generation: V2
status: canonical
source_boundary: TV E01-E13; Friends Shorts 01-06; three Asaura novels; Recollect V01-V02; seven official anthology volumes; main Bizen adaptation not currently admitted
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
audit_date: 2026-08-27
source_root_id: 17Lq1kooYOsD2kaXSu1v9_byFjyjgDxAZ
---

# Lycoris Recoil V2 Source Inventory

## 1. Audit result

**Current source-readiness verdict: PASS for V2 initialization, with explicit source-boundary notes below.**

The live Drive source root was audited after duplicate pruning. The corpus presently provides:

- complete anime analytical derivatives for TV E01-E13 and all six *Friends are thieves of time* shorts;
- complete exposed Japanese analysis audio for all 19 audiovisual objects;
- complete corrected Japanese subtitle/transcript derivatives for all 19 objects;
- complete analysis ASS and extracted ASS mirrors for all 19 objects;
- 19 extraction logs;
- three validated Japanese Asaura prose EPUBs;
- two validated Japanese *Recollect* EPUBs;
- seven validated Japanese official comic-anthology EPUBs;
- no permanently published full-video branch, by deliberate design under the corpus continuous-video escalation protocol.

The V2 sequential-analysis lock remains **CLOSED** until the companion analytical method and day-one longitudinal infrastructure are initialized. Source acquisition itself is sufficient to proceed with those initialization operations.

## 2. Canonical source root

Drive folder: `Lycoris Recoil`  
Drive ID: `17Lq1kooYOsD2kaXSu1v9_byFjyjgDxAZ`  
URL: ../../../../provenance/drive-artifacts/DRIVE_ARTIFACT_REFERENCE_INDEX.md#drive-ref-2d4462e17888382b

Current published top-level structure:

```text
00_metadata/
01_subtitles/
03_ai_analysis/
04_books/
99_logs/
README.md
```

`00_prepared_japanese_mkv` and `02_media` are intentionally not published to this Drive root because their aggregate size is approximately 20 GB. They remain escalation-only source material; see Section 6.

## 3. Anime build validation

The retained `00_metadata/final_japanese_build_validation_report.json` reports:

- result: `pass`;
- issue count: `0`;
- 19 prepared MKVs in the originating build;
- 19 corrected Japanese ASS files;
- 19 analysis ASS files;
- 19 softsub MKVs in the originating build;
- 19 hardsub MKVs in the originating build;
- 19 analysis-audio MP3s;
- 19 bundle directories;
- 19 bundle ZIPs;
- all 19 timing items stable;
- all 19 prepared-source / canonical-manifest matches confirmed.

The live Drive publication was separately checked and contains all 19 bundle ZIPs, all 19 exposed MP3s, 13 TV + 6 short corrected Japanese subtitle files, 19 analysis ASS files, 19 extracted ASS files, and 19 logs.

A representative post-upload raw check of `LR_ep01_screenshots.zip` also passed ZIP integrity; its SHA-256 in the downloaded Drive object was `c0610b002e6dd5bfd2858126e1bb3b6eda90bdee641a996a9fd11ca80cbdc5d5`.

### 3.1 Bundle inventory

| Scope | Bundle | Drive ID | Size MiB | Frames | Contact sheets | Validator ZIP status |
|---|---|---|---:|---:|---:|---|
| EP01 | `LR_ep01_screenshots.zip` | `14ituZs6J8XQaGmVI22KJEuo5uU-JVvBb` | 123.6 | 839 | 42 | pass |
| EP02 | `LR_ep02_screenshots.zip` | `1PVdwBErFQ6MKkOuqDdpk8GPdMojnkw5k` | 135.9 | 907 | 46 | pass |
| EP03 | `LR_ep03_screenshots.zip` | `1LK3q8ywVmO30C1YRpH4Rm-PGXCSosrbS` | 128.7 | 948 | 48 | pass |
| EP04 | `LR_ep04_screenshots.zip` | `1orDMY8o6BKrw20lrcuRYLn05n_gUiZC0` | 135.1 | 908 | 46 | pass |
| EP05 | `LR_ep05_screenshots.zip` | `1Esu3YtKsyLzSz6oov_CEZcK-QtnsyNr2` | 142.6 | 897 | 45 | pass |
| EP06 | `LR_ep06_screenshots.zip` | `1TM3YwUWWQrFO1_i5DC_dlrxXz8Zyy7Od` | 118.7 | 856 | 43 | pass |
| EP07 | `LR_ep07_screenshots.zip` | `1j9WdC6xDm6dVSiWEAjwOlVBw8h9-AzBY` | 120.2 | 843 | 43 | pass |
| EP08 | `LR_ep08_screenshots.zip` | `1N_bBeWAREwmo68rhIlXwAVIMwh-XlHEy` | 122.0 | 853 | 43 | pass |
| EP09 | `LR_ep09_screenshots.zip` | `1eOgIzi3lFWiD0O0yQGpNLiRxyd0tlAdq` | 111.0 | 829 | 42 | pass |
| EP10 | `LR_ep10_screenshots.zip` | `1v9nnEwhZeml7p2rc_d4zHNaYg4IDSxBk` | 109.8 | 699 | 35 | pass |
| EP11 | `LR_ep11_screenshots.zip` | `1JRekpcwbQqZQJOvWqj4kcUQqr5tsZZ0i` | 130.5 | 901 | 46 | pass |
| EP12 | `LR_ep12_screenshots.zip` | `1YDKCf_9Wz8VgCVnSfbfDLqNoztUDoe_a` | 132.4 | 975 | 49 | pass |
| EP13 | `LR_ep13_screenshots.zip` | `1zRFfjhEB1UUYZLBfkMKlwm3BAuHXIagM` | 116.8 | 810 | 41 | pass |
| SHORT01 | `LR_s00e01_screenshots.zip` | `14IJCh1X_CNu14g2UsiOwRKFclUadU5uq` | 11.2 | 67 | 4 | pass |
| SHORT02 | `LR_s00e02_screenshots.zip` | `1HupgOXpB3k9Q9Kr19OiLxwLPEOjfbHEn` | 19.2 | 105 | 6 | pass |
| SHORT03 | `LR_s00e03_screenshots.zip` | `17XE-MY1OlgQBnFNOiIkkeuTirntp1HuF` | 22.3 | 132 | 7 | pass |
| SHORT04 | `LR_s00e04_screenshots.zip` | `1bnhDkI-GkxB3Oh7y23rHXdRyZ04y5G65` | 20.3 | 123 | 7 | pass |
| SHORT05 | `LR_s00e05_screenshots.zip` | `1VeJOXM5Y1Yfng9fWz6IPHNEJOprn45Ho` | 15.6 | 104 | 6 | pass |
| SHORT06 | `LR_s00e06_screenshots.zip` | `1ZUZASSfkn-4AwYVaXXLslpQJZhWX6em6` | 35.1 | 180 | 9 | pass |

### 3.2 Exposed evidence mirrors

- Bundle folder: `03_ai_analysis/` (`1eUQmdfKVlVrZWW7PFOJQ3EifTM7DirJw`)
- Direct audio mirror: `03_ai_analysis/audio/` (`13qUDMXk3-bVSNxkvQA44FGdlRSYpODhq`) — 19 files verified.
- Corrected Japanese subtitle root: `01_subtitles/source_japanese_corrected/` (`1apDdcuu9QzkGfHiPKRwjxQg6DNp4_1my`) — TV 13 + shorts 6 verified.
- Analysis ASS root: `01_subtitles/analysis_ass/` (`1v38asQrlYf-0iFFARVUnVzZarkAGKDPc`) — 19 files verified.
- Extracted ASS root: `01_subtitles/extracted_ass/` (`1N9yGsS6kNzVrpPPIXLcfh-lKyI1QW-cM`) — 19 files verified.
- Logs: `99_logs/` (`1V42ymJlNIDw9H9-MZMzqthhd98SElbtQ`) — 19 files verified.

## 4. Validated prose and manga EPUBs

Every retained EPUB below was raw-downloaded from Drive and checked for:

- ZIP member integrity;
- EPUB `mimetype` first-entry / uncompressed contract;
- valid `META-INF/container.xml` → OPF package resolution;
- internal title;
- creator metadata;
- publisher metadata;
- declared language;
- SHA-256.

**All 12 unique EPUBs passed integrity and EPUB-container checks and declare `ja`.**

| Source | Class | Drive ID | Bytes | SHA-256 | Internal title | Internal creator metadata |
|---|---|---|---:|---|---|---|
| `Lycoris Recoil - Novel - Ordinary days.epub` | `A2_CREATOR_PROXIMATE_SUPPLEMENTARY` | `1RlbZEqj3xaeGMu-Po26GwltJ45jYHnEu` | 13567738 | `3f3543042a1c95f87d3b0b0191c2d70468a6974c5acbd3e69a75c91174facea0` | リコリス・リコイル　Ordinary days | アサウラ; いみぎむる; Spider Lily |
| `Lycoris Recoil - Novel - Recovery days.epub` | `A2_CREATOR_PROXIMATE_SUPPLEMENTARY` | `1deAImiwPdORptTtsxdqliFlHPM4wAbav` | 10262263 | `3bae32b86e946245edca1095f386e301be11d2a236368e7e95482284e7f81edf` | リコリス・リコイル　Recovery days | アサウラ; いみぎむる; Spider Lily |
| `Lycoris Recoil - Novel - Gluttony days.epub` | `A2_CREATOR_PROXIMATE_SUPPLEMENTARY` | `1dVgGlPdZBlBEILdoqyPdHeAkdH7xfKdR` | 12896024 | `a99274c76a06e396857d2169451966e764f7d0f31bb928dd8296adf3f7d6a496` | リコリス・リコイル　Gluttony days | アサウラ; いみぎむる; Spider Lily |
| `Lycoris Recoil Recollect - Volume 01.epub` | `B1_OFFICIAL_SINGLE_AUTHOR_DERIVATIVE` | `1a5RZc2N4Lq9mjweXjbl1lhOBSJJ2iQ1J` | 61143156 | `f80ac8e746efe48da6e45200bee2b01a2330bebb7d0a113e0e2fad57d5d95a5b` | リコリス・リコイル リコレクト １ | 阿部 かなり |
| `Lycoris Recoil Recollect - Volume 02.epub` | `B1_OFFICIAL_SINGLE_AUTHOR_DERIVATIVE` | `1EtC-4C9e19aq_y4gCOTURxz7COj0s2kc` | 56503018 | `6fa524a39781144a63341b15d2ca4f41122f4ce16dc8579cc9081158c28c1131` | リコリス・リコイル リコレクト ２ | 阿部 かなり; Spider Lily |
| `Lycoris Recoil - Official Comic Anthology - Reload.epub` | `C1_MULTI_AUTHOR_LICENSED_INTERPRETATION` | `1iz1TLjqBuNLGleyeYgLdSDxzdfa07shi` | 84765296 | `66a70b27bd24e3603862980f59dfeaea6dfd9a53047c4a7f7a9659c9e38258ba` | リコリス・リコイル 公式コミックアンソロジー リロード | いみぎむる; ikra; たもり　ただぢ; ヨコシマ　ペンギン; 苗川　采; 山村　うみ; 秋タカ; 幌田; ぺけ; タチ |
| `Lycoris Recoil - Official Comic Anthology - Reload 02.epub` | `C1_MULTI_AUTHOR_LICENSED_INTERPRETATION` | `1RXo71dZANCFqQeDRVh2clJy7kQL8-Ei8` | 86115536 | `9a276d4eaf291fd106a64c40be51acb5b5025516d99d63909067f80c8b22969e` | リコリス・リコイル 公式コミックアンソロジー リロード 2 | いみぎむる; 安房さとる; ヨコシマ　ペンギン; タチ; 如月　南極; ぶりすけ; 耳式; どま; match; すのはら風香 |
| `Lycoris Recoil - Official Comic Anthology - Reload 03.epub` | `C1_MULTI_AUTHOR_LICENSED_INTERPRETATION` | `1CmKsnv7fgpuJOrHJUTDLJh4qUKbvRC1N` | 88951360 | `fb7d2160197158704cd83e5176d047a26fc2bf5e5f14cf049067e048e0934685` | リコリス・リコイル 公式コミックアンソロジー リロード 3 | いみぎむる; ヨコシマ　ペンギン; タダノなつ; 幌田; 安房さとる; 梅原　うめ; fu-ta; ikra; しーめ; 犬裸 |
| `Lycoris Recoil - Official Comic Anthology - Repeat.epub` | `C1_MULTI_AUTHOR_LICENSED_INTERPRETATION` | `1c5fzbhWdtt87yoXnEM88nKl56WVm7Mnv` | 113850048 | `3735931f08d43714d1483add5b18d96909cb07b4cf788843edf90cdcb69b9b68` | リコリス・リコイル 公式コミックアンソロジー リピート | Spider Lily; あっと |
| `Lycoris Recoil - Official Comic Anthology - Repeat 02.epub` | `C1_MULTI_AUTHOR_LICENSED_INTERPRETATION` | `1VrPMT-ysH6Hoe4ODXhw6b263WFkbI1j7` | 85542656 | `bb8d094a5dee3de832e033e6626a6be3f094379d8bfd5c9973e990abaef46cea` | リコリス・リコイル 公式コミックアンソロジー リピート2 | Spider Lily |
| `Lycoris Recoil - Official Comic Anthology - Repeat 03.epub` | `C1_MULTI_AUTHOR_LICENSED_INTERPRETATION` | `1uozt-it-6OqgX8ZnHSLCCRuI3eRZZwDg` | 103584416 | `ffdadf45e6e0f5ad74390747cfbd897aa8601c6f4f0f0f495bfd6e4770d9cff8` | リコリス・リコイル 公式コミックアンソロジー リピート3 | Spider Lily |
| `Lycoris Recoil - Official Comic Anthology - React.epub` | `C1_MULTI_AUTHOR_LICENSED_INTERPRETATION` | `1ynVbUqVGgs_NtGdWzFduy7U6vsWQQG2f` | 64255632 | `0e2b007483d00ce847d2097e0814c3fb7c3809b567ef5d414caa7e1db5243113` | リコリス・リコイル 公式コミックアンソロジー リアクト | Spider Lily |

### 4.1 Prose bibliography status

Official KADOKAWA listings checked on 2026-08-27 identify the current prose series as:

1. `リコリス・リコイル Ordinary days` — present;
2. `リコリス・リコイル Recovery days` — present;
3. `リコリス・リコイル Gluttony days` — present.

The KADOKAWA descriptions for `Recovery days` and `Gluttony days` explicitly describe them as stories written by the original concept/story creator (`原案者自ら`). The EPUB package metadata identifies アサウラ, いみぎむる, and Spider Lily. For V2 these remain `A2_CREATOR_PROXIMATE_SUPPLEMENTARY`, distinct from the frozen anime-native baseline.

### 4.2 Recollect bibliography status

Official KADOKAWA listing for `リコリス・リコイル リコレクト ２` identifies:

- manga: 阿部かなり;
- original work: Spider Lily;
- same-series volumes: 1 and 2.

Both volumes are present. No official Volume 3 was located in the current KADOKAWA bibliography search. `Recollect` therefore currently appears complete at two volumes.

### 4.3 Official anthology bibliography status

Current official KADOKAWA product listings support the following seven-volume anthology corpus, all present:

- `Reload` 1;
- `Reload` 2;
- `Reload` 3;
- `Repeat` 1;
- `Repeat` 2;
- `Repeat` 3;
- `React`.

No official `Reload 4` or `Repeat 4` was located in the 2026-08-27 KADOKAWA search. Anthology contributor attribution must still be preserved story-by-story during sequential reading because some electronic OPF metadata exposes only Spider Lily rather than the complete contributor list.

## 5. Duplicate cleanup

The following redundant Drive uploads were permanently deleted with user authorization:

| Deleted Drive ID | File | Basis |
|---|---|---|
| `1DtXzLw7IQgXqiECzokuYSCD3YWYiw0GE` | `Lycoris Recoil Recollect - Volume 02.epub` | same filename, byte size, and source modified timestamp as retained copy |
| `1b6PMIQHg8Gy5vUxgwisPnA2WfMjRLEqG` | `Lycoris Recoil - Official Comic Anthology - Repeat 02.epub` | same filename, byte size, and source modified timestamp as retained copy |
| `1WGZdd1fekDSrJ0C_Nzk7qLGqlMgzEL2x` | `Lycoris Recoil - Official Comic Anthology - React.epub` | same filename, byte size, and source modified timestamp as retained copy |

Post-cleanup folder listings show unique filenames for all retained *Recollect* and anthology volumes.

## 6. Continuous-video retention and escalation

The full `00_prepared_japanese_mkv` and `02_media` branches are intentionally excluded from Drive because they collectively occupy approximately 20 GB. This is **not a missing-source defect**.

The corpus-wide `MANGA_ANIME_EPISODE_BUNDLE_SPECIFICATION.md` v1.1 governs escalation. V2 should use episode bundles by default and classify continuity needs as:

- `VIDEO_NOT_REQUIRED`;
- `VIDEO_TARGETED_ESCALATION`;
- `VIDEO_FULL_EPISODE_ESCALATION`.

When escalation is necessary, supply the smallest continuous object that preserves the diagnostic evidence. Current corpus transport guidance prefers ≤256 MB and permits ≤512 MB when necessary. Absence of uploaded continuous video limits temporal claims; it does not license reconstruction of unseen motion from sampled frames.

The Lycoris source inventory should therefore record full source video as **externally retained / escalation on demand**, not as absent.

## 7. Sources not currently admitted as mandatory V2 material

### Main Bizen Yasunori manga adaptation

The direct manga adaptation is not present in the source root. This is currently intentional rather than a blocking gap.

Its expected role is `B2_OFFICIAL_ADAPTATION`: adaptation comparison, dialogue retention/omission, panel pacing, added connective material, and alternative visual emphasis. Because V2 already possesses the originating audiovisual work at much higher temporal/performance resolution, the adaptation is optional unless later analytical questions justify acquisition.

It should not block the anime-native reconstruction, prose integration, *Recollect* analysis, anthology variance analysis, or V2 release unless explicitly admitted into the mandatory source boundary later.

## 8. Source authority / integration boundary

Current V2 source classes:

| Class | Sources | Integration role |
|---|---|---|
| `A1_ORIGINATING_AUDIOVISUAL` | TV E01-E13 + Shorts 01-06 | governing anime facts, performance, audiovisual characterization, anime-native model |
| `A2_CREATOR_PROXIMATE_SUPPLEMENTARY` | three Asaura prose volumes | strong supplementary extension; source-native reading before integration |
| `B1_OFFICIAL_SINGLE_AUTHOR_DERIVATIVE` | *Recollect* V01-V02 | source-local comedy/everyday characterization; cautious integration |
| `C1_MULTI_AUTHOR_LICENSED_INTERPRETATION` | seven official anthology volumes | contributor-level variance, characterization envelope, recurring attractors |
| `B2_OFFICIAL_ADAPTATION` | Bizen manga | optional; not currently acquired/admitted |

The anime-native baseline must be frozen before A2/B1/C1 material is allowed to revise the integrated character models.

## 9. Remaining audit actions

The primary-source corpus is sufficiently audited to proceed with V2 method/infrastructure initialization. Remaining non-blocking or downstream audit work:

1. during anthology reading, recover full contributor/story attribution from contents/colophons where OPF metadata is incomplete;
2. preserve exact source-local story/chapter locators during prose and manga deep readings;
3. if the Bizen adaptation is later acquired, run a separate B2 admission audit rather than silently adding it;
4. update this inventory if any new official Lycoris narrative source is acquired;
5. record any supplied continuous-video escalation clips/episodes in the evidence index rather than publishing the 20 GB media tree wholesale.

## 10. Initialization consequence

**SOURCE_RECONNAISSANCE_COMPLETE = true**  
**SOURCE_INVENTORY_INITIALIZED = true**  
**ANIME_SOURCE_COVERAGE = COMPLETE_13_PLUS_6**  
**PROSE_SOURCE_COVERAGE = COMPLETE_CURRENT_THREE_VOLUME_SERIES**  
**RECOLLECT_SOURCE_COVERAGE = COMPLETE_CURRENT_TWO_VOLUME_SERIES**  
**OFFICIAL_ANTHOLOGY_COVERAGE = COMPLETE_CURRENT_SEVEN_VOLUME_SET**  
**MAIN_ADAPTATION = OPTIONAL_NOT_ADMITTED**  
**CONTINUOUS_VIDEO = EXTERNALLY_RETAINED_ESCALATION_ONLY**  
**SEQUENTIAL_ANALYSIS_LOCK = CLOSED**

Next initialization responsibility: establish/update `CURRENT_STATE_AND_CORPUS_MAP.md` and create the canonical `LYCORIS_RECOIL_V2_ANALYTICAL_METHOD.md`, then initialize day-one ledgers before E01.
