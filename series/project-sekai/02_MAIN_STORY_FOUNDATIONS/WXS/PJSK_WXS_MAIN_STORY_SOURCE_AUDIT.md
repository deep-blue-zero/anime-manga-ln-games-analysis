---
series: PJSK
artifact_type: source_coverage_audit
scope: WXS_MAIN_STORY
generation: V1
status: canonical
source_boundary: "PJSK_SOURCE_20260822T184634Z_EVENT_0213; Japanese WXS main story episodes 00–20 only"
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
---

# Wonderlands×Showtime — Main-story source coverage audit

## Boundary and provenance

Canonical lock: `PJSK_SOURCE_20260822T184634Z_EVENT_0213`. Actual analytical boundary: WXS main-story episodes 00–20 only. Independently verified: **21 files, 60 scenes, 1,704 ordered records**, including stage/cut/media cues. Every canonical file hash equals both the task's verified inventory and the source `00_MANIFESTS/ARTIFACT_CHECKSUMS.sha256` entry. All records were read in episode order. No source transcript cache is included or needed in the analytical repository.

Preferred transcript repository: `ci-ke/ProjectSekai-story`; source commit: `22b4d19e982feaece6cd42c074e86e2cefac5cdd`. Canonical representations were generated under the locked pipeline run `20260822T184634Z` (pipeline/parser `0.2.7` / `0.1.0`). The source remains a research primary-text proxy; neither publication-grade official-game verification nor performance/audio review is claimed. Pipeline source and analysis authority remain distinct under the [source lock](../../01_SOURCE_LOCK_AND_INVENTORY/PJSK_ANALYTICAL_SOURCE_LOCK.md).

The release manifest identifies master internal episodes 1–21, `main_story`, `condition_ordered`, `relative_unlock_condition`, and null release timestamps for these files. Its verified SHA-256 is `c09ff420f4dd92a397e6aeadd4c399f0597e34a67c3238273df102a6438d5223`. Suffixes 00–20 express the foundation order; they are not a claimed calendar timeline shared with other units.

## Canonical-file manifest

Each filename below is under source-corpus-relative `02_CANONICAL_STORIES/MAIN/`. Each story ID has the form `PJSK:main:wonder_01_NN:01`. A canonical hash identifies the actual analyzed Markdown bytes; the original transcript hash in the next table identifies different upstream bytes and must not replace it.

| Episode | Canonical filename | Ordered records | Scenes | Canonical SHA-256 |
|---|---|---|---|---|
| 00 | `wonder_01_00_01.md` | 112 | 5 | `043fe3c344fa3d1b59220604714f9e5bb251bbb8000789661b43b4daabb6cf30` |
| 01 | `wonder_01_01_01.md` | 92 | 4 | `db37f32a111ab645ca75abd54e0196cd4e36ee4199cafc11acaa05ac59974faa` |
| 02 | `wonder_01_02_01.md` | 75 | 3 | `78308cffb711c40cf0f0a27c7fe63089a3f2390fedcd99a71c35ae69d07c20d6` |
| 03 | `wonder_01_03_01.md` | 76 | 1 | `00a325a94d492c6d6a54f7f19c0d68d4309c04514f4433c391228da1baff7786` |
| 04 | `wonder_01_04_01.md` | 75 | 3 | `66f124b0ecbd3ae12642419d325e970493de008a01f5055cdfef08ccbce4b793` |
| 05 | `wonder_01_05_01.md` | 80 | 4 | `018560321450762fa41daa69c7ddaf0354bc582a3f7543e86e8e8dfffb7c9221` |
| 06 | `wonder_01_06_01.md` | 64 | 3 | `034f4b3aa8e69d263da1fc25a8a8af78d69a233f792254cf3b116e65af79aed6` |
| 07 | `wonder_01_07_01.md` | 81 | 1 | `f3bbde432e7420dc3c78e5822e0c3e8a7b0ba61d39f2f4e7483aa7bae1d192cd` |
| 08 | `wonder_01_08_01.md` | 71 | 3 | `b4091c421094c648470882fb4bc4e909da5e52f0729008757836aa8d55ef53f7` |
| 09 | `wonder_01_09_01.md` | 81 | 3 | `dff5585a0bd35b4ca7bda58aedf685b4791218008033e0f504d7e22da60cc917` |
| 10 | `wonder_01_10_01.md` | 82 | 3 | `e7d2b964b8efba2f57486de9eeaeb51140ed1b7f82e28b9b286f09b90f792574` |
| 11 | `wonder_01_11_01.md` | 90 | 3 | `388acb640089bf1f862153331778853846a39d116d9ba21f068dd4295094ea6e` |
| 12 | `wonder_01_12_01.md` | 65 | 1 | `f467e7b029b04d4ac38de0be456595ea8bd46b9b3627a466b10ab4ade6921779` |
| 13 | `wonder_01_13_01.md` | 93 | 3 | `e5d6451e065734fa2771933896f9d863ca76d695e104326b43b6f2e4fc8a2d64` |
| 14 | `wonder_01_14_01.md` | 106 | 4 | `277302e7dfeb5863baba43f748e1dab8d7ceddd12607696048a5eeeceadc8a3e` |
| 15 | `wonder_01_15_01.md` | 66 | 3 | `1d010b7e73dbd14c6af14fb8f2f309134c5f94bfabd2506a83f62cdbf0555c09` |
| 16 | `wonder_01_16_01.md` | 81 | 2 | `164aa8d764305aebab4272b21c635cb627517520abf779296506e2165c10e497` |
| 17 | `wonder_01_17_01.md` | 81 | 3 | `ba31e3c0761b4923f68f95ccd02543451db2f958ae20a1d00e602d1551d00fc4` |
| 18 | `wonder_01_18_01.md` | 88 | 3 | `a2ccf45585e56840a42c4ebcbb453fcd3a50ccc8655de17e3aa6570d93939003` |
| 19 | `wonder_01_19_01.md` | 78 | 2 | `ee2175e6eb162682f54bfbdf534a611eb0289a3c98cb85d76f217518c3ae6656` |
| 20 | `wonder_01_20_01.md` | 67 | 3 | `bf7e151039243aa9204fc4503cb5f6a33dc9ca93d074a625f6d8a49df1ae3df4` |

## Upstream provenance and locator endpoints

All source paths begin with `story_jp/main/5 ワンダーランズ×ショウタイム/`. Source line bounds include the upstream file range declared by its canonical front matter. Locator endpoints are inclusive, not substitutes for per-record reading.

| Episode | Upstream filename / lines | Upstream SHA-256 | First / last ordered-record locator |
|---|---|---|---|
| 00 | `wonder_01_00 オープニング.txt` / 1–125 | `177d1aa365d7d3306e03a8b893d8bcbce78d5baca2fa690f2372eef154d38142` | `PJSK:main:wonder_01_00:01:001:0001` / `PJSK:main:wonder_01_00:01:005:0007` |
| 01 | `wonder_01_01 ようこそワンダーステージへ！.txt` / 1–102 | `e80a26053959396c8c065c905e8df36d3ac2076d15434dd1deb9f483f5a767e4` | `PJSK:main:wonder_01_01:01:001:0001` / `PJSK:main:wonder_01_01:01:004:0057` |
| 02 | `wonder_01_02 未来のスターとわんだほい.txt` / 1–83 | `177e596d98c183d1d2638044ae918b2143b05abec0874a9ba344107325912b80` | `PJSK:main:wonder_01_02:01:001:0001` / `PJSK:main:wonder_01_02:01:003:0008` |
| 03 | `wonder_01_03 ワンダーランドのセカイ.txt` / 1–81 | `ad423021fc21392eff4c0419629956947ba01cbb026dd8320abc64dddc2a3799` | `PJSK:main:wonder_01_03:01:001:0001` / `PJSK:main:wonder_01_03:01:001:0076` |
| 04 | `wonder_01_04 メンバーを探そう！.txt` / 1–84 | `7a25f97711fe07f432b45baa45b663ba2c941af0007ff002357ef011d52c931c` | `PJSK:main:wonder_01_04:01:001:0001` / `PJSK:main:wonder_01_04:01:003:0008` |
| 05 | `wonder_01_05 奇妙な演出家.txt` / 1–91 | `c6d8705c32c6c73e7e69a1473f9d9acd070de20436a9ded2f557fff28ff0deb3` | `PJSK:main:wonder_01_05:01:001:0001` / `PJSK:main:wonder_01_05:01:004:0024` |
| 06 | `wonder_01_06 ４人目のメンバー？.txt` / 1–72 | `706b852dc34a62fc18d65ff2f979602cb6e5f2388fe2b44d3a7cadff1f0bbce7` | `PJSK:main:wonder_01_06:01:001:0001` / `PJSK:main:wonder_01_06:01:003:0025` |
| 07 | `wonder_01_07 ネネロボ・オンステージ！？.txt` / 1–86 | `aad678479ef9313eab89d3d99aa9d4108572ad100110dd0e27469b4abe6c4456` | `PJSK:main:wonder_01_07:01:001:0001` / `PJSK:main:wonder_01_07:01:001:0081` |
| 08 | `wonder_01_08 結成！ショーユニット！.txt` / 1–79 | `4bbb1de2ac7bef6aa9ae35e9743793afe7f19cf9f03d12a0dda4cdef492d4779` | `PJSK:main:wonder_01_08:01:001:0001` / `PJSK:main:wonder_01_08:01:003:0046` |
| 09 | `wonder_01_09 変人、本領発揮.txt` / 1–90 | `30b5a09a0d0408d63fa2581ff2c490afa0e2ca74edd65fe80f065ff6fa8c707f` | `PJSK:main:wonder_01_09:01:001:0001` / `PJSK:main:wonder_01_09:01:003:0019` |
| 10 | `wonder_01_10 KAITOのヒント.txt` / 1–90 | `361f29da558b6fc1f2de417564c3f5d5991405a8e2f03a3db4d8246232f129fb` | `PJSK:main:wonder_01_10:01:001:0001` / `PJSK:main:wonder_01_10:01:003:0007` |
| 11 | `wonder_01_11 えむの夢.txt` / 1–99 | `d4f46201370aff8e3a418762a316d328f5d8dba2327be3bea1e534e8dda1b2bf` | `PJSK:main:wonder_01_11:01:001:0001` / `PJSK:main:wonder_01_11:01:003:0017` |
| 12 | `wonder_01_12 公演スタート！.txt` / 1–70 | `39cfe6c7c3a40e771dbb52dac6f24c743f37dccebf3de4641e639c489305dc64` | `PJSK:main:wonder_01_12:01:001:0001` / `PJSK:main:wonder_01_12:01:001:0065` |
| 13 | `wonder_01_13 失った笑顔.txt` / 1–106 | `44d14a5819320174c79868b09b6ecf2349b6f99cfba8c6587502721e8be326a7` | `PJSK:main:wonder_01_13:01:001:0001` / `PJSK:main:wonder_01_13:01:003:0007` |
| 14 | `wonder_01_14 あの日の想い.txt` / 1–123 | `51a2a3ad3268cff10e2ba26fec29235d89b55de59515dab554d2ac618bcc7577` | `PJSK:main:wonder_01_14:01:001:0001` / `PJSK:main:wonder_01_14:01:004:0013` |
| 15 | `wonder_01_15 おじいちゃんのステージ.txt` / 1–74 | `833c7a3570b150ed4be944314b4c3c7a6373643f575a463d167a5e51a4e7d6ba` | `PJSK:main:wonder_01_15:01:001:0001` / `PJSK:main:wonder_01_15:01:003:0021` |
| 16 | `wonder_01_16 絶対に失敗しない方法.txt` / 1–91 | `897e6cd8cc96f0868757d318e9d5668bd18f9a32470baa51787a583fc4071abb` | `PJSK:main:wonder_01_16:01:001:0001` / `PJSK:main:wonder_01_16:01:002:0079` |
| 17 | `wonder_01_17 ひとりぼっちの錬金術師.txt` / 1–90 | `9bc02b1b9afa2d29885951ddfe69f9c29982fa128d3b56dba6a3da22e08737a7` | `PJSK:main:wonder_01_17:01:001:0001` / `PJSK:main:wonder_01_17:01:003:0004` |
| 18 | `wonder_01_18 “最高のショー＂の答え.txt` / 1–96 | `bef3f1463556db053d9d9bffa2cfe134406a557ae971f8df0d8aa59a484ccb65` | `PJSK:main:wonder_01_18:01:001:0001` / `PJSK:main:wonder_01_18:01:003:0067` |
| 19 | `wonder_01_19 セカイはまだ始まってすらいない.txt` / 1–85 | `6a68b4c46becf0f476199d0ec386bf57a1ee82b775523ad1754c06c3cab8bf4c` | `PJSK:main:wonder_01_19:01:001:0001` / `PJSK:main:wonder_01_19:01:002:0040` |
| 20 | `wonder_01_20 ワンダーランズ×ショウタイム.txt` / 1–75 | `27f9f77ebee9cd250e9e9d752e719cb06de84fc3438a7b268097da939aa172f6` | `PJSK:main:wonder_01_20:01:001:0001` / `PJSK:main:wonder_01_20:01:003:0014` |

## Analytical audit scope

The canonical foundation consists of one phase map, six phase readings, one main-story synthesis and this audit, with a foundation README as the entrypoint. Each substantial phase addresses causality, psychology, relationships, knowledge, behavior/speech, theme and continuity, and carries an end-state handoff. A machine audit checks the existence of every cited record and expanded range against the canonical source files; relative links are checked from this canonical directory. Root semantic review and serial ledger integration are complete.

No source discrepancy was detected in the 21 analyzed files. The opening's dream-like return and the subsequent first-meeting greeting are retained as a presentation uncertainty. Retrospective self-blame, hostile motive judgments, indirect family outcomes and the degree of embodied stage participation retain the qualifications discussed in the phase readings. The final source count is not itself a declaration of canonical analytical completion.
