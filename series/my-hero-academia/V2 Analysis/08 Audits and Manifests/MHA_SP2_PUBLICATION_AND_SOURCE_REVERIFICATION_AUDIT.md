---
series: MHA
corpus: MHA_SP2
artifact_type: audit
scope: PUBLICATION_EQUIVALENCE_AND_PRIMARY_REVERIFICATION
generation: V2
status: canonical
source_boundary: Published V42 source lock and Japanese main-volume CBZs; inspected pages are enumerated separately
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
---

# MHA SP2 — Publication equivalence and primary-source reverification audit

This audit preserves retrieval and admissibility. It does not replace the readiness index, frozen source blobs, sequential readings or per-model validation transactions. The continuation reviewed exact published head `a225d537cfacd07a485d3167e1cd8bc4cd7b5586` (tree `de1a1e9a64133697036555fe46313a5527e97c25`) and locked complete beforeimages before bounded edits.

## Publication equivalence

The preceding session lacked terminal write credentials and appended equivalent reviewed trees through the connected Git Data API with `force=false`. Commit metadata/parent identity produced different commit IDs; the handoff and [PR #40](https://github.com/deep-blue-zero/anime-manga-ln-games-analysis/pull/40) recorded the following mapping. In this continuation, every published tree below was retrieved and matched exactly. Original local IDs are reported provenance; this audit does not claim those unavailable local objects were independently fetched.

| Original unpublished local commit | Accessible published equivalent | Exact shared tree reported in handoff and verified at published commit |
|---|---|---|
| `c999a3d82b618fa022ec97993211d99116aa28a3` | `cbabd47d81a56f4bd6123f764f599c8bc86fa823` | `aef1bfec20d9bd8f5bbbe271a09b0e7f4301d28d` |
| `fd795d3f842136e147537fc13b2efae87b5636df` | `3706083801094428a5742aa71e80f0daf5fce658` | `5326369586c6a4f66adfafff42966571f8d53804` |
| `2a5a604cd592bdce0d6d77cca34ac04122a5484b` | `7089f586ce3114e54a2c4954018f809b7c2cab09` | `1c462d5df59271b47b4fadd60d8e68615e2e2017` |
| `5a6fa0ada27c651fd43d3c5975bd5bd9e61293fe` | `416ce8fe682f40606242e223ddbf2e66893aee7c` | `444ccf3f88eab949f711b9fed4bd7ad561cf908e` |
| `c10db26ba4ba8701345a8a36a74ebfc8cd74abd1` | `a3481bd9fa3308a6617ad7c000c0064416220236` | `095c7757aed08501dc176d85a22583a5e46104c1` |
| `1fedf0bff7c5d34998733db9960b1eba9e41d285` | `b51f39c412d4e05510f1158cba9071c01822e73a` | `c9724a0dee4f4c6914e1329c84de9ac1e51a9dfd` |
| `e3a1ecc0ae3bd6d65c514be1f6cd62f8b8e4b037` | `b1b7bf1d6ec493a683100e61d935bf86e2ecb2cd` | `d862fd173fcbf40536dca452753ac6d09a80074d` |
| `8a0606303ff7c5a5b35a11dd59ac574984206179` | `acd1fd70eaf1648791c7d69abe5866f05efc082b` | `2e7d0df388151805aef30d1bffdece214dfe243d` |
| `62a63ed1db783465f85add0d5d247e6f3dbeb01b` | `2f0090d0953f44c9f1c2f64765dfc91045d950c5` | `2389ce4a5986a227e4755ad02cb71b85e098a902` |
| `0b9c1211df5f5f41000823acc77359f141d226fe` | `751f759e23a60d175e4788e55d8e00613d7996ef` | `0039f85b2b3c697c25d7897de085b6ac650fa6a0` |
| `ef8707e8246ba615b0cf784682ef655071db5320` | `d928e9a777b2c32ae140acb927ca6c8d12d7d3d2` | `cdcce6626b214dd6f396be8e6fccfc4ff9c2ee60` |
| `cc7a3404ff54b4f1ce4e9698c54935fffd659d6d` | `9d3204e446f1cb2a6753f243672da9c10602855c` | `bd3327310f75b19fb16bb94dcdc7112325faf06d` |
| `0807940cba0009f160d698ec202c4b7fa5faaefb` | `12aa3df94e6e66c5e141b56c5f1c30559232878c` | `85ca2ed3b19de89be00ffa289948038c918dbe3c` |
| `0335630d22db9282ccba493943fd31475b3131ba` | `00a3e81878173217f16b39bf906d0dbfa439e4f0` | `5dbb8e506322f178fca1c4d35738e41aba0011d9` |
| `bad28651037c92e57081b64941f0e14e89041c9e` | `a225d537cfacd07a485d3167e1cd8bc4cd7b5586` | `de1a1e9a64133697036555fe46313a5527e97c25` |

The models’ original local lock `2a5a604cd592bdce0d6d77cca34ac04122a5484b` resolves for retrieval through published equivalent `7089f586ce3114e54a2c4954018f809b7c2cab09`. At that published commit, **182/182 declared frozen-source references in all 30 models** matched their recorded Git blobs, covering **40 distinct source files**. These counts describe identity checks, not interpretive validation success. Retrieve the path at that commit, rather than a subsequently corrected current file. The selected earlier evidence and explicit exclusions in each probe still control admissibility.

## Frozen source identity register

The model tables retain individual attribution of these sources. One row per distinct source avoids reproducing 182 dossier references here.

| Frozen sequential source | Git blob at published source lock |
|---|---|
| [MHA_SP2_V01_DEEP_READING](https://github.com/deep-blue-zero/anime-manga-ln-games-analysis/blob/7089f586ce3114e54a2c4954018f809b7c2cab09/series/my-hero-academia/V2%20Analysis/02%20Sequential%20Readings/MHA_SP2_V01_DEEP_READING.md) | `223f10b50076224de81f1804b9a996749a987841` |
| [MHA_SP2_V02_DEEP_READING](https://github.com/deep-blue-zero/anime-manga-ln-games-analysis/blob/7089f586ce3114e54a2c4954018f809b7c2cab09/series/my-hero-academia/V2%20Analysis/02%20Sequential%20Readings/MHA_SP2_V02_DEEP_READING.md) | `6952dcfc4414a0ac811393179f5004d1b27eccba` |
| [MHA_SP2_V03_DEEP_READING](https://github.com/deep-blue-zero/anime-manga-ln-games-analysis/blob/7089f586ce3114e54a2c4954018f809b7c2cab09/series/my-hero-academia/V2%20Analysis/02%20Sequential%20Readings/MHA_SP2_V03_DEEP_READING.md) | `1a2530adf9feea21a44a705c68c86bbb18f79818` |
| [MHA_SP2_V04_DEEP_READING](https://github.com/deep-blue-zero/anime-manga-ln-games-analysis/blob/7089f586ce3114e54a2c4954018f809b7c2cab09/series/my-hero-academia/V2%20Analysis/02%20Sequential%20Readings/MHA_SP2_V04_DEEP_READING.md) | `418f60e6762ddb7aa1d839a791320109de7385ff` |
| [MHA_SP2_V05_DEEP_READING](https://github.com/deep-blue-zero/anime-manga-ln-games-analysis/blob/7089f586ce3114e54a2c4954018f809b7c2cab09/series/my-hero-academia/V2%20Analysis/02%20Sequential%20Readings/MHA_SP2_V05_DEEP_READING.md) | `52c30c6edf2fb60673ff0815a78ab1d7406043a4` |
| [MHA_SP2_V06_DEEP_READING](https://github.com/deep-blue-zero/anime-manga-ln-games-analysis/blob/7089f586ce3114e54a2c4954018f809b7c2cab09/series/my-hero-academia/V2%20Analysis/02%20Sequential%20Readings/MHA_SP2_V06_DEEP_READING.md) | `623eab5e390a8288ed626f05f43fb5d3819dfaff` |
| [MHA_SP2_V07_DEEP_READING](https://github.com/deep-blue-zero/anime-manga-ln-games-analysis/blob/7089f586ce3114e54a2c4954018f809b7c2cab09/series/my-hero-academia/V2%20Analysis/02%20Sequential%20Readings/MHA_SP2_V07_DEEP_READING.md) | `d7fb50444f8a12ffbfe379feec381d6535083083` |
| [MHA_SP2_V08_DEEP_READING](https://github.com/deep-blue-zero/anime-manga-ln-games-analysis/blob/7089f586ce3114e54a2c4954018f809b7c2cab09/series/my-hero-academia/V2%20Analysis/02%20Sequential%20Readings/MHA_SP2_V08_DEEP_READING.md) | `889992563e79083262f4a58d6843b55b5ebc01d8` |
| [MHA_SP2_V09_DEEP_READING](https://github.com/deep-blue-zero/anime-manga-ln-games-analysis/blob/7089f586ce3114e54a2c4954018f809b7c2cab09/series/my-hero-academia/V2%20Analysis/02%20Sequential%20Readings/MHA_SP2_V09_DEEP_READING.md) | `03b891e11cad7a4d72e6c3d63681058276cbc800` |
| [MHA_SP2_V10_DEEP_READING](https://github.com/deep-blue-zero/anime-manga-ln-games-analysis/blob/7089f586ce3114e54a2c4954018f809b7c2cab09/series/my-hero-academia/V2%20Analysis/02%20Sequential%20Readings/MHA_SP2_V10_DEEP_READING.md) | `fb3d558ff7386c55d42ef69315b80a1e0d9e7a84` |
| [MHA_SP2_V11_DEEP_READING](https://github.com/deep-blue-zero/anime-manga-ln-games-analysis/blob/7089f586ce3114e54a2c4954018f809b7c2cab09/series/my-hero-academia/V2%20Analysis/02%20Sequential%20Readings/MHA_SP2_V11_DEEP_READING.md) | `212e588a99f614a67df5f21e7baa73732bf55b86` |
| [MHA_SP2_V12_DEEP_READING](https://github.com/deep-blue-zero/anime-manga-ln-games-analysis/blob/7089f586ce3114e54a2c4954018f809b7c2cab09/series/my-hero-academia/V2%20Analysis/02%20Sequential%20Readings/MHA_SP2_V12_DEEP_READING.md) | `26210faac76c877c864d59a98749449a6b295b47` |
| [MHA_SP2_V13_DEEP_READING](https://github.com/deep-blue-zero/anime-manga-ln-games-analysis/blob/7089f586ce3114e54a2c4954018f809b7c2cab09/series/my-hero-academia/V2%20Analysis/02%20Sequential%20Readings/MHA_SP2_V13_DEEP_READING.md) | `27e75f3ad9e2b134a05aca00741f3a1441291880` |
| [MHA_SP2_V14_DEEP_READING](https://github.com/deep-blue-zero/anime-manga-ln-games-analysis/blob/7089f586ce3114e54a2c4954018f809b7c2cab09/series/my-hero-academia/V2%20Analysis/02%20Sequential%20Readings/MHA_SP2_V14_DEEP_READING.md) | `b89730844cb2ddbb2c8c4791e4006082187a016c` |
| [MHA_SP2_V15_DEEP_READING](https://github.com/deep-blue-zero/anime-manga-ln-games-analysis/blob/7089f586ce3114e54a2c4954018f809b7c2cab09/series/my-hero-academia/V2%20Analysis/02%20Sequential%20Readings/MHA_SP2_V15_DEEP_READING.md) | `a85c6588194c1698329379b552ba938ece9cedc1` |
| [MHA_SP2_V16_DEEP_READING](https://github.com/deep-blue-zero/anime-manga-ln-games-analysis/blob/7089f586ce3114e54a2c4954018f809b7c2cab09/series/my-hero-academia/V2%20Analysis/02%20Sequential%20Readings/MHA_SP2_V16_DEEP_READING.md) | `9c72525e6e26fe6b9c8ddbdbc09b84df027a53f9` |
| [MHA_SP2_V17_DEEP_READING](https://github.com/deep-blue-zero/anime-manga-ln-games-analysis/blob/7089f586ce3114e54a2c4954018f809b7c2cab09/series/my-hero-academia/V2%20Analysis/02%20Sequential%20Readings/MHA_SP2_V17_DEEP_READING.md) | `9773321f00dd2f9b7cfa4cb9ff7584d7ad11d818` |
| [MHA_SP2_V18_DEEP_READING](https://github.com/deep-blue-zero/anime-manga-ln-games-analysis/blob/7089f586ce3114e54a2c4954018f809b7c2cab09/series/my-hero-academia/V2%20Analysis/02%20Sequential%20Readings/MHA_SP2_V18_DEEP_READING.md) | `5190f206219a89733eef6fa4bb1b88377565d327` |
| [MHA_SP2_V19_DEEP_READING](https://github.com/deep-blue-zero/anime-manga-ln-games-analysis/blob/7089f586ce3114e54a2c4954018f809b7c2cab09/series/my-hero-academia/V2%20Analysis/02%20Sequential%20Readings/MHA_SP2_V19_DEEP_READING.md) | `d5a1748e07a6407eed8641a04f4af4733f1df1d4` |
| [MHA_SP2_V20_DEEP_READING](https://github.com/deep-blue-zero/anime-manga-ln-games-analysis/blob/7089f586ce3114e54a2c4954018f809b7c2cab09/series/my-hero-academia/V2%20Analysis/02%20Sequential%20Readings/MHA_SP2_V20_DEEP_READING.md) | `3036aa393affe559d862ad97081a77e77e41ba36` |
| [MHA_SP2_V21_DEEP_READING](https://github.com/deep-blue-zero/anime-manga-ln-games-analysis/blob/7089f586ce3114e54a2c4954018f809b7c2cab09/series/my-hero-academia/V2%20Analysis/02%20Sequential%20Readings/MHA_SP2_V21_DEEP_READING.md) | `ceb7f9b9dda03442ae9b8927ecdd2e07a65ffefa` |
| [MHA_SP2_V22_DEEP_READING](https://github.com/deep-blue-zero/anime-manga-ln-games-analysis/blob/7089f586ce3114e54a2c4954018f809b7c2cab09/series/my-hero-academia/V2%20Analysis/02%20Sequential%20Readings/MHA_SP2_V22_DEEP_READING.md) | `c8ca1ec7f1ae2cad84e3e55353354e2865d55983` |
| [MHA_SP2_V23_DEEP_READING](https://github.com/deep-blue-zero/anime-manga-ln-games-analysis/blob/7089f586ce3114e54a2c4954018f809b7c2cab09/series/my-hero-academia/V2%20Analysis/02%20Sequential%20Readings/MHA_SP2_V23_DEEP_READING.md) | `ef303e196f253a004423c6bcc285969cc25e7788` |
| [MHA_SP2_V24_DEEP_READING](https://github.com/deep-blue-zero/anime-manga-ln-games-analysis/blob/7089f586ce3114e54a2c4954018f809b7c2cab09/series/my-hero-academia/V2%20Analysis/02%20Sequential%20Readings/MHA_SP2_V24_DEEP_READING.md) | `ff68ace5e3e524597a6402fa0bd3da1da255c267` |
| [MHA_SP2_V25_DEEP_READING](https://github.com/deep-blue-zero/anime-manga-ln-games-analysis/blob/7089f586ce3114e54a2c4954018f809b7c2cab09/series/my-hero-academia/V2%20Analysis/02%20Sequential%20Readings/MHA_SP2_V25_DEEP_READING.md) | `338453c007cd2cb8317959c0859ae37c30a5c474` |
| [MHA_SP2_V26_DEEP_READING](https://github.com/deep-blue-zero/anime-manga-ln-games-analysis/blob/7089f586ce3114e54a2c4954018f809b7c2cab09/series/my-hero-academia/V2%20Analysis/02%20Sequential%20Readings/MHA_SP2_V26_DEEP_READING.md) | `ae9f01e67db14903dd685cf19b6b4991f5fc2d75` |
| [MHA_SP2_V27_DEEP_READING](https://github.com/deep-blue-zero/anime-manga-ln-games-analysis/blob/7089f586ce3114e54a2c4954018f809b7c2cab09/series/my-hero-academia/V2%20Analysis/02%20Sequential%20Readings/MHA_SP2_V27_DEEP_READING.md) | `8ce15b4cc2ca01b19bcb1bc3e1994e0cf5a0132a` |
| [MHA_SP2_V28_DEEP_READING](https://github.com/deep-blue-zero/anime-manga-ln-games-analysis/blob/7089f586ce3114e54a2c4954018f809b7c2cab09/series/my-hero-academia/V2%20Analysis/02%20Sequential%20Readings/MHA_SP2_V28_DEEP_READING.md) | `a7b302b5bbe5b34ed6c49f337912612bbc1c91fe` |
| [MHA_SP2_V30_DEEP_READING](https://github.com/deep-blue-zero/anime-manga-ln-games-analysis/blob/7089f586ce3114e54a2c4954018f809b7c2cab09/series/my-hero-academia/V2%20Analysis/02%20Sequential%20Readings/MHA_SP2_V30_DEEP_READING.md) | `b5014dee356ad84b98d6cd9154c2c75badbb9f0c` |
| [MHA_SP2_V31_DEEP_READING](https://github.com/deep-blue-zero/anime-manga-ln-games-analysis/blob/7089f586ce3114e54a2c4954018f809b7c2cab09/series/my-hero-academia/V2%20Analysis/02%20Sequential%20Readings/MHA_SP2_V31_DEEP_READING.md) | `85d667dcf3b39e6930cebadd381823e56d307994` |
| [MHA_SP2_V32_DEEP_READING](https://github.com/deep-blue-zero/anime-manga-ln-games-analysis/blob/7089f586ce3114e54a2c4954018f809b7c2cab09/series/my-hero-academia/V2%20Analysis/02%20Sequential%20Readings/MHA_SP2_V32_DEEP_READING.md) | `b04863c066bce6e5d3e6b8b65a9aa3542a516c79` |
| [MHA_SP2_V33_DEEP_READING](https://github.com/deep-blue-zero/anime-manga-ln-games-analysis/blob/7089f586ce3114e54a2c4954018f809b7c2cab09/series/my-hero-academia/V2%20Analysis/02%20Sequential%20Readings/MHA_SP2_V33_DEEP_READING.md) | `ad875b86ee779e8b67edccaac69a252b7d63d9de` |
| [MHA_SP2_V34_DEEP_READING](https://github.com/deep-blue-zero/anime-manga-ln-games-analysis/blob/7089f586ce3114e54a2c4954018f809b7c2cab09/series/my-hero-academia/V2%20Analysis/02%20Sequential%20Readings/MHA_SP2_V34_DEEP_READING.md) | `1cb72979205e7c54a9c6a445c385d340d0cd6f6c` |
| [MHA_SP2_V35_DEEP_READING](https://github.com/deep-blue-zero/anime-manga-ln-games-analysis/blob/7089f586ce3114e54a2c4954018f809b7c2cab09/series/my-hero-academia/V2%20Analysis/02%20Sequential%20Readings/MHA_SP2_V35_DEEP_READING.md) | `8ca13103cd19ed74f849997e18655ea358a70349` |
| [MHA_SP2_V36_DEEP_READING](https://github.com/deep-blue-zero/anime-manga-ln-games-analysis/blob/7089f586ce3114e54a2c4954018f809b7c2cab09/series/my-hero-academia/V2%20Analysis/02%20Sequential%20Readings/MHA_SP2_V36_DEEP_READING.md) | `b60603cf13a9068b4e246e4936ba1a2434286c96` |
| [MHA_SP2_V37_DEEP_READING](https://github.com/deep-blue-zero/anime-manga-ln-games-analysis/blob/7089f586ce3114e54a2c4954018f809b7c2cab09/series/my-hero-academia/V2%20Analysis/02%20Sequential%20Readings/MHA_SP2_V37_DEEP_READING.md) | `d6ad83b397cd8cba16fdf2927dc9d3a0a6392f6c` |
| [MHA_SP2_V38_DEEP_READING](https://github.com/deep-blue-zero/anime-manga-ln-games-analysis/blob/7089f586ce3114e54a2c4954018f809b7c2cab09/series/my-hero-academia/V2%20Analysis/02%20Sequential%20Readings/MHA_SP2_V38_DEEP_READING.md) | `215b5c0fe5a7ac6581582a82c658228f1f2bd0c8` |
| [MHA_SP2_V39_DEEP_READING](https://github.com/deep-blue-zero/anime-manga-ln-games-analysis/blob/7089f586ce3114e54a2c4954018f809b7c2cab09/series/my-hero-academia/V2%20Analysis/02%20Sequential%20Readings/MHA_SP2_V39_DEEP_READING.md) | `81dffc0898e73a19855d5e2dff989de71148f01f` |
| [MHA_SP2_V40_DEEP_READING](https://github.com/deep-blue-zero/anime-manga-ln-games-analysis/blob/7089f586ce3114e54a2c4954018f809b7c2cab09/series/my-hero-academia/V2%20Analysis/02%20Sequential%20Readings/MHA_SP2_V40_DEEP_READING.md) | `888b9d6cd5753de469e658d5d1ef343db5571194` |
| [MHA_SP2_V41_DEEP_READING](https://github.com/deep-blue-zero/anime-manga-ln-games-analysis/blob/7089f586ce3114e54a2c4954018f809b7c2cab09/series/my-hero-academia/V2%20Analysis/02%20Sequential%20Readings/MHA_SP2_V41_DEEP_READING.md) | `3f2a810dd36593160af413e4fff35ee648391ccd` |

## Primary-source byte locks

The user supplied a read-only local main-series source after the connected Drive folder confirmed all 42 volumes but its binary download reference could not be materialized by the desktop toolset. Local file names are `My Hero Academia - Vol. NN [Japanese].cbz`. All 42 archives were hashed; **all 12 handoff-locked archives match the recorded byte count, image count and SHA-256 exactly**. Hashing establishes byte identity, not complete rereading. All extraction and working notes remain outside Git within the authorized MHA workspace. No manga images or archives are repository artifacts. Supplements remain provisionally inventoried and outside this main-volume completion boundary.

| Volume | Bytes | Image entries | SHA-256 | Handoff comparison |
|---|---:|---:|---|---|
| V01 | 157078028 | 193 | `df8f229cc354c67556f9d0ab642863d7a32f349724fa5de273051a066f745504` | New byte inventory only |
| V02 | 123746101 | 207 | `4f9fc1d0bba8a13f4c5d275d93d7c9129572ad2998f1090c86c8749ef5fa8ece` | New byte inventory only |
| V03 | 121065222 | 194 | `9260d968e8dff84637667e76b91020d17068a7a8dcabafe18f93ba43fdc5afe3` | New byte inventory only |
| V04 | 129278993 | 199 | `ef472390d4112392d23171c044ab52b4e38c3e08b6408d8b55f0b904fc7601b8` | New byte inventory only |
| V05 | 82256073 | 197 | `3edcf0928f04f6e4db8c6e186c7c1a35a795f8596eace8b3793b5cbc75646626` | New byte inventory only |
| V06 | 82482507 | 197 | `628be5a5c415c241f1d8beb9ba16b954c9c864f4e078caa04c7722dc9ab2f8fd` | New byte inventory only |
| V07 | 45675959 | 198 | `5218355ec7dfc73bf6dae1a2f43033fe5e823dcf89551eea9cd577eda7ff36a3` | New byte inventory only |
| V08 | 46393575 | 198 | `bd55920b45ae5a3ea0e0e474f0a67d62b4912f53d3fe14f23ed55b69a35bac9e` | New byte inventory only |
| V09 | 67270236 | 197 | `2b4ef329c34948037c6567c8229c210aa858e7b3027237c5b9c96f2ac1da81eb` | New byte inventory only |
| V10 | 61083922 | 197 | `cbc3867b756d5b9d611d32ae232a99267e5dfc7f21a4f353dda26101a51b996d` | Exact match |
| V11 | 66006162 | 213 | `7d8e71415b16c5098f14e6d774375c605b6d8ae31916486f76e8fdb9b2d4e1b0` | New byte inventory only |
| V12 | 60278774 | 197 | `72985b18e4550cd7596471811b013f2ac467ecdb8fc2724dc2ffa3dcd9edaa6d` | New byte inventory only |
| V13 | 44474264 | 190 | `ea56aca599a74dc6c8bc616c5aac309e14d884cce06197982c952b3ca3b2fa8c` | New byte inventory only |
| V14 | 46728808 | 214 | `8640f02343e87265021ee6e000166139380e3bb616d7060797be4b57e1e4b16a` | New byte inventory only |
| V15 | 91682977 | 199 | `3e9867d48636aafc7cf7731d5a5ac17c5068b019114f8f173d22c47deb1f3645` | New byte inventory only |
| V16 | 48970977 | 199 | `df11b1a65be7464702c2e5c036cbf6fb9f9da0d60ca616a8aacbe01ff0aa450c` | New byte inventory only |
| V17 | 122999614 | 197 | `81f8358fc40eabab0b85984ef727d476ce2ab2ecc4b92693d9fb763f56b0231b` | New byte inventory only |
| V18 | 108140909 | 186 | `cb0a91c634f886244b9bbf60ad2b7f33c99ebc5067552d09a06efff9e2f52ae2` | Exact match |
| V19 | 89583284 | 199 | `52719329e28ea573796ef2cb9881ebc93572ef936019d2187c6b2d6c1b2af2b5` | New byte inventory only |
| V20 | 103545443 | 207 | `8f63d4f6115d6108bda4c3d8508b0543b764ab851454dcac55066562d2f55bf1` | New byte inventory only |
| V21 | 101396898 | 207 | `880d226aab23a3fe25b89e0855ff2a3ab02094649a9b9a23d43153abd1f6193a` | New byte inventory only |
| V22 | 98315191 | 199 | `f6a0b73d597e59215e2e6594c333ad97161512c0f21ba14c71a0924d56948e7e` | New byte inventory only |
| V23 | 99853030 | 207 | `98018ffb3ec3129580f3a95461ed9fea4f54b81121f79a394375cf63ec1f8453` | New byte inventory only |
| V24 | 99701551 | 199 | `72aca3bb2fb4de56acd4219fb15bbb3e0bfe2d5af06a3e5e92c4bec300722d61` | New byte inventory only |
| V25 | 77196427 | 202 | `6ac9dd14f73b2938a288d865d0ffde8932b62cb9713bf09efa6d00cedf4bd0d7` | New byte inventory only |
| V26 | 76673164 | 206 | `a2b319b15f86b99e53eb7564b13867ab92c788abe210fa64c96101da11d93c71` | New byte inventory only |
| V27 | 77689548 | 190 | `6b584784f60af885845ddbec40c1630f09f0a63991c7062266366c75d0748abd` | Exact match |
| V28 | 79422767 | 190 | `5fff3f9e0beac4ceacf9dbc81f717817a2406fa6df411f5e4e1cfbe022a6a7ef` | Exact match |
| V29 | 80172013 | 194 | `6b62549b48d28ffdec1b727239b00a365e8b91fb2cf27240cef7661629a5d381` | New byte inventory only |
| V30 | 86061552 | 210 | `51045856a48b05035044699ab2b238e02361e7eb17939a597fc5b73e44213714` | New byte inventory only |
| V31 | 80948005 | 226 | `e33112db5532725b59e67e6fe2d68a5407a8016f77f8ee5314463bc275842f2b` | Exact match |
| V32 | 108387656 | 113 | `96e8e37981e4eb9d6ce434f07f6860120e9c3bcef4e22177aa11671a13e24156` | New byte inventory only |
| V33 | 71754987 | 102 | `e2648a9a97cb884a34bdcd0eaf3b7bb8c3e5b66852e666163d6fbdd53e43351d` | New byte inventory only |
| V34 | 44463417 | 202 | `3294854c05a375a790cb1898014d3ece4e0b3ba33fd460e28103114a03e4a8fe` | New byte inventory only |
| V35 | 60711475 | 202 | `57f160938005ef542af03a568edbe181959ff32785d18e4304d1a74d9b27e767` | New byte inventory only |
| V36 | 74084458 | 105 | `0fd06c75bb1386361a3b6b5747ee9faf00d02573e037137a54175c9f72ab01c3` | Exact match |
| V37 | 130985719 | 209 | `d21cb6179686d2095fe6536fedf5bbb697efdf559ca4846567da2e2cf240e9b0` | Exact match |
| V38 | 148791443 | 217 | `4d78463dde1833168ba8272a5b48c91ab6e19fa65b044011c28f224cb8545ebc` | Exact match |
| V39 | 143178554 | 193 | `57c3133999ee380b35b029eecf29d6ca0b8c5a2302af18b9ec515124d97f65ac` | Exact match |
| V40 | 108580700 | 209 | `d6273762bb04c30680f60b025cba573e6468f070bea276b81ab18bce10799011` | Exact match |
| V41 | 104293245 | 209 | `236c8ee8546dcc4c2007a9ffedced6e3489f1d0a2f721cea0d89b5dc75220700` | Exact match |
| V42 | 89885814 | 193 | `969bd3ca1df7cea2f2e6e2aae16eae77c4717d82c09f7ee372f22a5d195b86c3` | Exact match |

## Direct page inspection in this continuation

The following pages were opened and visually inspected in Japanese in this continuation. They are separate from the inherited handoff’s earlier observations; no unlisted page is claimed to have been re-inspected here. Scene ranges can include excluded chapter/author matter and do not make every image narrative evidence.

| Check | Pages actually inspected | Observation and use limit |
|---|---|---|
| SR01 — Hawks/Tokoyami boundary | V27:p149, p179–182; V28:p059–077 | V27:p149 locates the lethal strike. V27:p179 is Tokoyami’s arrival, p180 Mirko’s narrative endpoint, p181 author equipment note, p182 assistant material. V28:p060–061 approaches; p062 is a chapter portrait; p063–070 retrieves Hawks under fire and records unconsciousness; p071–076 includes renewed danger, Geten’s interruption and escape; p077 voices Tokoyami’s belief. Neither that belief nor physical rescue exonerates the killing. V28:p059 is author matter. |
| SR02 — Hawks later comparison and page offset | V31:p067, p079–081, p083, p085 | Raw numeric filename = logical page + 1, confirmed against printed p079–081, p083 and p085. p067 is narrative biography, not the adjacent author page. p081 removes institutional command; p083 invokes Twice as a positive helping example; p085 chooses continued work/Endeavor support. These are comparison evidence, not V27 frozen inputs. |

## Hawks validation defect and its disposition

HK-V01 originally declared “received rescue” inside a V27 freeze. V27:p179 supplies arrival only. The full historical V27 reading additionally imports V28 extraction, accusation and trust-response material into several sections and its outgoing lock; V28’s opening inherits that mistake. The correction notices preserve all historical body text while excluding those claims from earlier freezes. The Hawks evidence atom HK05 now names V28; its freeze remains V27→V31 and explicitly separates later survival/extraction conditions from predicted behavior.

The original prediction is retained verbatim in its substantive wording. It grounds continued helping in public rescue, mentorship and Endeavor trust, all independent of extraction. That rationale survives removing the invalid input; **the original exercise nevertheless remains contaminated**. Its five qualitative comparisons retain partials for motive, emotional trajectory and relationships. Correction is not retroactive preregistration, proof of no hindsight influence, a new blind experiment, or a survival forecast. The aggregate report must carry this limitation forward.

The historical extraction wording also occurs in the source inventory, current-state map and Pro Hero ledger. Local correction notices supersede those clauses; the Pro Hero ledger locates the lethal strike at V27:p149 and extraction in V28. Subsequent corpus-wide correction propagation and synthesis do not alter the frozen identities recorded above.

## Recovery integration observation

At the continuation’s first live check, PR #40 was already merged (2026-09-09T17:30:12Z); the handoff’s draft/open description had become historical. Fetched main `2a9d39efe4bfd0ca0c54f910ff9dce27f0186f40` had the same tree as the published analytical head but different squash ancestry. A clean non-rewriting merge reconciled the histories with zero content delta: `5a698297888ef25e465cd364ac8448580050f72f`. Its staged routing preflight returned `PASS: phase=current snapshot=INDEX paths=3515`. This is a local recovery receipt, not a final-head remote audit or completion claim for the remaining synthesis work.
