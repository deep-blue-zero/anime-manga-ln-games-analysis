---
title: "Revue Starlight — V2 Audiovisual Witness Supplement"
artifact_id: REVUE_STARLIGHT_V2_AV_WITNESS_SUPPLEMENT
artifact_type: source_inventory
series_id: revue-starlight
version: "1.0"
status: canonical
authority_scope: v2_witness_identity_and_clock
source_boundary: "TV01–TV12, OVA01–OVA03, and the complete 2021 sequel film, including credits and post-credit material"
canonical_home: "series/revue-starlight/01 Source Lock and Inventory/SOURCE_WITNESS_SUPPLEMENT_V2.md"
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
---

# Revue Starlight — V2 Audiovisual Witness Supplement

The [V1 source inventory](SOURCE_INVENTORY.md) defines the animated corpus. This supplement identifies the witnesses used for the [retrospective V2 claims](../06%20Evidence%20and%20Indexes/16_ANIME_AV_RECONCILIATION_V2.md). The two runs used different derivatives of the same admitted works. Match the unit and the digest before reusing a timestamp or comparing measurements.

## Verified audiovisual containers

All sixteen rows were rehashed from local bytes and matched to Gemini's frozen CP16 inventory. Durations are `ffprobe` container durations in seconds. Source aliases below also name the clocks used for V2 scene locators. Times are container elapsed time from the beginning of the named object.

| Unit | Witness basename | Container duration (s) | SHA-256 |
| --- | --- | ---: | --- |
| `TV01` | `Shoujo Kageki Revue Starlight - S01E01.mkv` | 1446.784 | `a6a97c09edc8e69c1d283822afff560a50609775893e3e429e7d310c01852250` |
| `TV02` | `Shoujo Kageki Revue Starlight - S01E02.mkv` | 1445.615 | `899a91f16b01ffcd00f91ded0cb5e27cd9254c0225afa3920270820a6ad36eda` |
| `TV03` | `Shoujo Kageki Revue Starlight - S01E03.mkv` | 1445.780 | `f8ebfcb4a48f3ca32ce2e303e77c58c8a4eea3e066aca985e1274736faf20aa1` |
| `TV04` | `Shoujo Kageki Revue Starlight - S01E04.mkv` | 1445.655 | `b2d2bcf99d7111e3436d49df21383e330402366d35522122b4335c6e9be97d9d` |
| `TV05` | `Shoujo Kageki Revue Starlight - S01E05.mkv` | 1446.784 | `7168a34c9920d88fc019354999167b9685cdc106e1cb7ecaa723e07703a994c1` |
| `TV06` | `Shoujo Kageki Revue Starlight - S01E06.mkv` | 1445.780 | `84abc1e3e49868adbbd6adb77f5a6bfc63fa681f055a11eaf0434517ea30679d` |
| `TV07` | `Shoujo Kageki Revue Starlight - S01E07.mkv` | 1445.630 | `6bf41ce89db359ef18a6bc88ad0799363e96565bf7a92dd9ac584cc4620c6e46` |
| `TV08` | `Shoujo Kageki Revue Starlight - S01E08.mkv` | 1445.670 | `a8dce7414bd1e09d1e56f2f25f088c739e2fce48b0fefc7bab5cdd7496245ce3` |
| `TV09` | `Shoujo Kageki Revue Starlight - S01E09.mkv` | 1447.110 | `ff53750e4d26305afabd06af8c752166d4289cf7d32c7d48abc2989a417bc375` |
| `TV10` | `Shoujo Kageki Revue Starlight - S01E10.mkv` | 1447.400 | `78d4c66f73ccb1d51dd24a2058bf42d8005dab8d207ba634b5b65e66ecd0c8b4` |
| `TV11` | `Shoujo Kageki Revue Starlight - S01E11.mkv` | 1445.780 | `7b279ba1efb60a9d63cf43f88940a1e0c31d49cf77f6d4076af72bc002d996df` |
| `TV12` | `Shoujo Kageki Revue Starlight - S01E12.mkv` | 1430.805 | `887501ca140a02c40da82faebd09ee9795d2de9e9dfb0864af8da1ef23261b85` |
| `OVA01` | `ep01.analysis-softsub.mkv` | 419.420 | `14bcfd93131d1cfeea41b52c3370ca877e48cfbe69e4fae8434f1e7d48d8c6c1` |
| `OVA02` | `ep02.analysis-softsub.mkv` | 428.430 | `04b35dd4b04f6932eece9d5292d2973612c7157989268ed92feb2162f8c6e1bc` |
| `OVA03` | `ep03.analysis-softsub.mkv` | 433.435 | `c2152663a82472b0a618c5ca09f7e826b82706d5a07647253c221603ff70a38f` |
| `MOVIE` | `[Veggie_Sub]_Shoujo☆Kageki_Revue_Starlight_Movie.analysis-softsub.mkv` | 7222.770 | `dd3c3858effe78bfdc4f67b588ec23f274460a33fc3968c8c83a745e71a41099` |
| `MOVIE-MIX` | `[Veggie Sub] Shoujo☆Kageki Revue Starlight Movie.mkv` | 7222.236 | `8674bf5ec2192fe0ff77e7b8d9644231da6e9444964a09cdda17d9182492685a` |

- **TV01–TV12** use clean HEVC video and Japanese 48 kHz stereo FLAC in stream `0:1` (`0:a:0`). TV01, TV05, and TV10 also carry Japanese cast commentary in stream `0:2`. Use the primary program stream for narrative analysis.
- **OVA01–OVA03** use HEVC video and Japanese 48 kHz stereo FLAC in `0:1` (`0:a:0`). Their English ASS is an auxiliary locator. For exact Japanese wording, use the program audio or legible on-screen Japanese. English cues can help locate a contribution, with speaker or action confirmed by synchronized image and performance.
- **MOVIE** uses unburned H.264 video and Japanese 48 kHz stereo AAC in `0:1` (`0:a:0`). Its video begins at `+0.021 s`, with a stream end tag of `7222.235 s`. Audio starts at `0.000 s` and ends at `7222.228 s`. The embedded subtitle stream extends the container to `7222.770 s`. CP16's reviewed scope uses the video endpoint, yielding a combined TV, OVA, and film span of `25,842.313 s`.
- **MOVIE-MIX** is a parallel container for the same film, with Japanese stereo AAC in `0:1` and discrete Japanese 48 kHz AAC 5.1 in `0:2` (`0:a:1`). Cite this alias for discrete channel measurements. The stereo analysis container has one audio stream. Scope conclusions about framing or soundtrack to measured intervals and identify the mix. Surround routing can corroborate a production observation, and dramatic meaning requires evidence from the scene.

## Auxiliary Japanese ASS witnesses

The thirteen files below were rehashed and match CP16. Counts are literal `Dialogue:` records in each file, which can include multiple voices, effects, or other annotations in one event. They can differ from counts in earlier analysis bundles.

| Unit | ASS basename | Dialogue records | SHA-256 |
| --- | --- | ---: | --- |
| `TV01` | `s01e01.analysis.ass` | 344 | `06c35606770414ff4e4bde6225c6d853ba5f27c8eed992d0208cb6f9e78a8e4e` |
| `TV02` | `s01e02.analysis.ass` | 318 | `9fdd1039588b5ef6675482ee7711a992e14e7951c8b46759ab33b73e2f82a1fb` |
| `TV03` | `s01e03.analysis.ass` | 279 | `236353e6bc06bca90ef4c9e2eb2271c4816ddaaff3c48f48f9386b1aab511396` |
| `TV04` | `s01e04.analysis.ass` | 317 | `2e5b611a95e14a6e6cd98ae5e8bbed614beebf21b4378956904d2e0ecbe8d263` |
| `TV05` | `s01e05.analysis.ass` | 346 | `740e3e1c08b95b9a56c6a2ee7be9acdacdbc8144c467006145b89f946b23eb35` |
| `TV06` | `s01e06.analysis.ass` | 318 | `f13bdbd8c8e2de51e09b45a70ce65b6e55738a0ea06c35f422f77d771264da38` |
| `TV07` | `s01e07.analysis.ass` | 331 | `67903a213ff2e89095031f0ece062517f7b51ded9363b3da51234cf0e200e9b8` |
| `TV08` | `s01e08.analysis.ass` | 273 | `8ec6c7a6b907748cc609d6d4c86206b57070f6ab29a3a2066d4aa9ce92409187` |
| `TV09` | `s01e09.analysis.ass` | 333 | `5c2962acaa09211abd614525ee76b285bd0d3652cffd055c7853ee51ad1f2008` |
| `TV10` | `s01e10.analysis.ass` | 288 | `631304ff21efeec341b4627fab3854372836029c98fdeff0db8106a4daf487fe` |
| `TV11` | `s01e11.analysis.ass` | 306 | `9c394734966462d16f5a4a9b39b8e5eef3ae23c659ded7980e3589c46e5b8ec3` |
| `TV12` | `s01e12.analysis.ass` | 281 | `6e25d70372949508d19462bbff44f349d783b2fd237596396cf9e1770f8f810b` |
| `MOVIE` | `[Veggie_Sub]_Shoujo☆Kageki_Revue_Starlight_Movie.analysis.ass` | 1691 | `5992b2b769783b558886e024cf119769af7403d668ac85483bb4a2f555341783` |

The TV copies are time-corrected Japanese broadcast captions and may condense or omit sung lines. The film ASS is a community Japanese text layer. Its 1,691 records and style labels aid retrieval. Use the audio for contested wording and the shot, cues, and credits for their respective attribution questions.

## Inspection and provenance

| Record | Frozen identity |
| --- | --- |
| Original OpenAI project tree used for comparison | `0bae19f328c3fdef82047e5753568fbb8478daed` |
| Gemini run `RS-AV-R2-GEMINI-CARBON` analytical freeze (CP16) | `224c52786b9b5a1d5edd6ce203bfb0714305627e`, tree `e45cae165d93b70b00dba20c690f97b094e3157d` |
| Gemini comparative audit (CP17A) | `724f8fb0fd79705fa3f1c558851d29b12dd2de1a` |
| Gemini Track C handoff (CP18) | `98115bee1a9ce0a7e50bd83c0f38ced130cea4b8` |

The comparison tree and the receiving `main` at `73caf927b4ffe1c4a2ad1590d4d24b9a4a755e77` agree for this project. The `00_inventory` Markdown and JSON at CP16 identify the source objects and document Gemini's calibration. CP18's suggested inventory differed from the verified bytes at ten TV container digests, both film container digests, and twelve Japanese ASS digests. The physical witnesses and the matching CP16 identities govern this supplement. A separate TV01 reading-header discrepancy is recorded in the [erratum](../07%20Audits%20and%20Manifests/V1_STRUCTURAL_AND_CHECKSUM_ERRATUM.md#gemini-packet-corrections).

Gemini reported synchronized Japanese audio and an effective native visual sampling rate of 1 fps, supplemented by targeted higher-rate frames, dedicated listening, and measurements. The local review checked digests and stream metadata, sought directly on the identified container clocks, and inspected selected frames and caption intervals. For example, TV05's scene cues, the ending chapter at `22:30.891`, and the `22:31` picture change supply distinct anchors on the same clock. The film's video offset and end tags distinguish frame positions from the subtitle tail. V2 uses those object clocks directly. Applying them to a different V1 derivative requires calibration on that derivative.

The private CP16 and CP17A records retain the original scope and sequence. Their separation establishes the reported freeze order, while Gemini's disclosed pretraining knowledge of the TV07 reveal qualifies the TV06 interpretation. See the [TV06 decision](../06%20Evidence%20and%20Indexes/16_ANIME_AV_RECONCILIATION_V2.md#tv06--the-damaged-clasp-and-the-replay-stinger).
