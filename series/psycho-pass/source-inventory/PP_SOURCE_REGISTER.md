---
title: "Psycho-Pass — Source register and admission boundary"
artifact_id: PP_SOURCE_REGISTER
artifact_type: source_register
series: psycho-pass
version: "1.2"
status: canonical
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
do_not_use_as_literary_evidence: true
authority_generation: PP-INITIAL
source_boundary: "PP-S01NE-E01–E02 admitted and verified; E03–E11 metadata-only candidates"
canonical_home: series/psycho-pass/source-inventory/PP_SOURCE_REGISTER.md
created: 2026-11-18
last_updated: 2026-11-23
source_admission: "PP-S01NE-E01–E11 Season 1 New Edit authorized; admitted through PP-S01NE-E02"
---

# Source register and admission boundary

This register distinguishes official edition/catalogue metadata, verified local file availability and narrative admission. **As of 2026-11-23 under run `PP-S01NE-RUN-20261123-E01-E11`, `PP-S01NE-E01` and `PP-S01NE-E02` are content-authenticated, bundle-verified, alignment-calibrated, and admitted; `PP-S01NE-E03`–`E11` remain metadata-only candidates pending sequential admission at their own frontiers.** On 2026-11-18 a bounded inventory found eleven numbered New Edit/Extended-labelled MKVs, one menu MKV, two BD-labelled ASS files and ten TV-labelled SRT files. All twenty-four files were byte-hashed. Container/stream metadata and subtitle timing/script metadata were inspected. Subsequent verification on 2026-11-23 confirmed all 24 original hashes unchanged, verified eleven complete episode bundles (`PP-S01NE-E01-BUNDLE-V1`..`E11-BUNDLE-V1`) and eleven standalone canonical FLAC streams bit-exact with embedded MKV audio, and performed full audiovisual/Japanese-text inspection through `PP-S01NE-E02` only.

Private acquisition paths and supplier filenames remain outside Git. Stable witness IDs below bind public-safe technical metadata to the exact private bytes. An authorized operator retrieves the private source inventory through the owner's source environment and matches by SHA-256; filename resemblance is insufficient. Copy/move without byte change preserves witness identity; new bytes require a new witness/version record. A hash proves identity of the inspected file, not authenticity, completeness or successful decoding.

## Edition relationship and available scope

Fuji Television identifies Season 1 New Edit as the original twenty-two episodes reedited into eleven hour-slot episodes with added cuts. The hour-slot description includes broadcast scheduling and is compatible with the roughly forty-six-minute candidate files; it does not prove their edition or completeness. The page's 2014 back-number entries support the original New Edit broadcast year. Its displayed 2023 broadcast date is a later airing, not first release. [Official Fuji programme metadata](https://www.fujitv.co.jp/b_hp/psycho-pass_new/)

The eleven local filename labels and counts are consistent with that official New Edit relationship. Their asserted BD/Extended provenance is **supplier-labelled, content match pending**. The original disc/edition, cuts, completeness, Japanese audio and subtitle fidelity have not been authenticated by direct inspection. These are eleven verified available media candidates, not eleven admitted episodes or eleven verified complete episode bundles.

| Family / reserved analytical identity | Metadata basis | Available in inspected root | Admission and local-home state |
| --- | --- | --- | --- |
| Season 1 New Edit / Extended, `PP-S01NE` | Official eleven-unit reedit relationship; local numbered labels/probes | Eleven MKV candidates E01–E11; subtitle witnesses below | NONE; first intended installment, local contracts initialized |
| Season 1 original broadcast, `PP-S01OB` | Official twenty-two-unit source edition for New Edit | No original-version witness located in this inventory | NONE; possible same-continuity comparison only, no local reading home |
| Season 2, prospective `s02` | Official franchise archive | No source verified here | NONE; inventory candidate only |
| The Movie | Official franchise archive names The Movie | No source verified here | NONE; exact release/edition and stable installment slug to verify at admission |
| Sinners of the System | Official franchise archive identifies the collection | No source verified here | NONE; case boundaries, exact titles and source editions must be verified before creating case homes |
| Season 3, prospective `s03` | Official franchise archive | No source verified here | NONE; inventory candidate only |
| FIRST INSPECTOR | Official franchise archive | No source verified here | NONE; release/streaming segmentation versus film witness unresolved |
| PROVIDENCE | Official franchise archive | No source verified here | NONE; inventory candidate only |

The [official franchise archive](https://psycho-pass.com/archive/) distinguishes these families, including original Season 1 and New Edit. Listing them establishes a candidate franchise scope, not automatic canon admission, complete franchise coverage, release dates, in-universe ordering or availability elsewhere. Exact later unit counts, editions, language assets and first-release provenance remain unverified. A later source sweep may extend this inventory without narrative admission. No later installment placeholders are created.

New Edit is not a new fictional continuity merely because it edits the original. Reserve original broadcast IDs E01–E22 separately; no automatic E01↔E01/E02 pairing, duplicated coverage credit or common timestamp namespace. Added/reordered segments and disclosure differences require authorized comparison of both exact witnesses.

## Exact media candidates

All eleven candidate episode files are MKV containers with stream 0 H.264, 1920×1080, 10-bit `yuv420p10le`, declared frame rate `24000/1001`, time base `1/1000`; stream 1 is FLAC, 48 kHz stereo, time base `1/1000`. No embedded subtitle streams were found. Container and video origins report 0.000 seconds. The video language tag is `eng`; that tag does not identify spoken language. Audio is tagged `jpn` for E01–E10, while E11 has no audio language tag. Direct language/listening verification remains pending for every file.

Use source-relative `HH:MM:SS.mmm` with the registered origin, retaining stream-specific offsets below. Duration is a container report, not a perceptually verified ending. Frame rate is source metadata, not evidence of an inspecting model's sampling rate. All rows have availability `VERIFIED_METADATA_ONLY`, narrative admission `NONE` and content/edition verification `PENDING`.

| Unit / media witness | Bytes | Duration (s) | Audio start (s) | SHA-256 |
| --- | ---: | ---: | ---: | --- |
| PP-S01NE-E01 / PP-S01NE-E01-AV01 | 2098155274 | 2753.194 | 0.000 | `1603b8b0872d4f616a317739dfac060997729b188f62e656123ef271df939f9b` |
| PP-S01NE-E02 / PP-S01NE-E02-AV01 | 2630810452 | 2752.171 | 0.111 | `77d1ee150780edcefb905573dfc3c68995b98ee41f11db8c80ab671d659ba151` |
| PP-S01NE-E03 / PP-S01NE-E03-AV01 | 2461643956 | 2753.109 | 0.000 | `d76993e5cff4d4424f0ff84b0ee290629e730e3da415c236f94519282d1f97a9` |
| PP-S01NE-E04 / PP-S01NE-E04-AV01 | 2035181254 | 2752.048 | 0.067 | `ee38a468dacfc260b4a17126c5591a6054bfa9284ceca53b8e59f135895b3cbd` |
| PP-S01NE-E05 / PP-S01NE-E05-AV01 | 2228054484 | 2752.597 | 0.000 | `9403b95ca44051b023693da162119703b0e659a0249f74c6c684b26030304063` |
| PP-S01NE-E06 / PP-S01NE-E06-AV01 | 2289411589 | 2739.409 | 0.056 | `a1544c22bf8654ef798e35a402cd097c2babc82c18cffa2162ac18072c22897a` |
| PP-S01NE-E07 / PP-S01NE-E07-AV01 | 1715381250 | 2753.194 | 0.000 | `e035170d12b767767beea0fd28a23e168bf8b2e3b96ef459c56ddf9d9bee1f84` |
| PP-S01NE-E08 / PP-S01NE-E08-AV01 | 2061834286 | 2752.126 | 0.111 | `844a9842de4d208b713bff15d46c31708a215a4c3fe2face21e75e187854b95f` |
| PP-S01NE-E09 / PP-S01NE-E09-AV01 | 1720941211 | 2753.194 | 0.000 | `5b7bfaf7a83745d11981d381bced15841e3ef854e6217efff1b168ea96ed2d64` |
| PP-S01NE-E10 / PP-S01NE-E10-AV01 | 1709900885 | 2752.005 | 0.070 | `415f232ea2e21cbd3a184ab9887df3c5a3294ce4aba119117ef6883667f3537b` |
| PP-S01NE-E11 / PP-S01NE-E11-AV01 | 1970103346 | 2753.130 | 0.000 | `8beb0d594ef014dd73478672318c53e188deeaf3c330cbfe1fbc17878f7c93c2` |

The separate menu witness `PP-S01NE-MENU-AV01` is 148875590 bytes, reported duration 43.045 seconds, SHA-256 `fb340024765e43d25ee7a263b40f81ee2a66e0f8c0c23a7b45e5e91f21b1441a`. It is 1080p H.264 8-bit `yuv420p`, `24000/1001`, with Japanese-tagged 48 kHz stereo FLAC. **Excluded from the eleven episode units and from narrative admission.** Its content and potential supplementary role are uninspected.

## Exact external text witnesses

All twelve text files decoded as UTF-8 with optional BOM and contain Japanese-script codepoints. Script presence is not proof of sole language, official authorship, complete dialogue, speaker attribution or textual accuracy. ASS event counts and SRT cue counts are technical counts, not verified spoken-line counts. BD/TV are supplier labels. BD-labelled text filenames reference a different encoding/resolution than the current 1080p MKVs; matching edition and synchronization must be demonstrated.

| Witness ID | Format / claimed timing witness | Bytes | Events/cues | First start → last end | SHA-256 |
| --- | --- | ---: | ---: | --- | --- |
| PP-S01NE-E01-TXT-BD01 | ASS / BD-labelled | 64679 | 624 | 0:00:07.53 → 0:44:31.45 | `e940679bad8022dcfc1214e40eef5ae38c02f767074b647bb9e8fa74fa578358` |
| PP-S01NE-E02-TXT-BD01 | ASS / BD-labelled | 74221 | 683 | 0:00:01.85 → 0:44:30.40 | `c4630c23b2b2dbf5938bb5ecca95134a793a0643ace4498fe9dbeddde4bd6786` |
| PP-S01NE-E01-TXT-TV01 | SRT / TV-labelled | 54765 | 625 | 00:01:07,436 → 00:56:06,355 | `ca77a4ea226f50ac3d1e4816522aa2906eef136cbd56a0796b18cec5d4adf59a` |
| PP-S01NE-E02-TXT-TV01 | SRT / TV-labelled | 63443 | 683 | 00:01:02,950 → 00:56:05,906 | `a7ab9ecddf4a09e7df73de58b1a14a15a06b47015ee106a5c848f9d498a41c8a` |
| PP-S01NE-E03-TXT-TV01 | SRT / TV-labelled | 66881 | 725 | 00:01:03,125 → 00:56:06,181 | `da13d0198173e4e4b8b511ceeb9d4c119e45351e0b7558b7eb56132ffc92c3fe` |
| PP-S01NE-E05-TXT-TV01 | SRT / TV-labelled | 61299 | 686 | 00:01:02,875 → 00:56:22,748 | `8f79859c3e9f945d192138d0ce69d40a1c7d14c9322efb2b14b6c465bc766964` |
| PP-S01NE-E06-TXT-TV01 | SRT / TV-labelled | 56102 | 659 | 00:01:07,125 → 00:56:25,833 | `92bdaa74c2ca8234300273912ef2c7856e8b10b15bcf01f2831a2927395f5b6c` |
| PP-S01NE-E07-TXT-TV01 | SRT / TV-labelled | 61477 | 680 | 00:01:02,872 → 00:56:05,928 | `ee3e5bfb45f55c5a0593586ec238845995e7b3c1405729c6ac405682bcf049c7` |
| PP-S01NE-E08-TXT-TV01 | SRT / TV-labelled | 58581 | 652 | 00:01:03,231 → 00:56:06,220 | `5adbe6e2fd59223e7777221d0085799403d1ccc96cc1ad1bdd291ec4c09a88ad` |
| PP-S01NE-E09-TXT-TV01 | SRT / TV-labelled | 59080 | 641 | 00:01:02,865 → 00:56:58,274 | `b6c0db6ebb1695222c311cfc7f1d9cd803dfaf94f4cfeaa5a12cadc7b15eba63` |
| PP-S01NE-E10-TXT-TV01 | SRT / TV-labelled | 66437 | 719 | 00:01:03,059 → 00:57:22,966 | `a3fa53ce51a4369df15ac9e426e841b880c30d64a10d1c3171d05debd71ee524` |
| PP-S01NE-E11-TXT-TV01 | SRT / TV-labelled | 48898 | 568 | 00:01:06,043 → 00:57:22,913 | `555d18875707f956697bf8ae7e5712bf4342b5550af806615de6473ab55fc61f` |

**E04 has no external subtitle file in the inspected inventory.** E01 and E02 have both BD- and TV-labelled witnesses. E03 and E05–E11 have TV-labelled witnesses only.

Every TV-labelled SRT ends around 56–57 minutes, beyond the roughly 45–46-minute video duration. Those clocks are **UNALIGNED** and must not be used as direct video timestamps. Differences may involve commercial breaks, cuts, edition changes or incorrect labelling; no cause was established by metadata. Do not assume one constant offset. A verified piecewise segment crosswalk or another accurate source-language route is required. The BD ASS endpoints lie inside E01/E02 duration, which is necessary but insufficient for synchronization; content matching, opening/middle/end anchors, residual error and text fidelity remain pending.

## Evidence routes and bounded gaps

| Responsibility | Verified now | Missing before a required future claim can be accepted |
| --- | --- | --- |
| Continuous video | Eleven file identities and technical probes | Actual access in chosen runtime, edition/completeness, successful playback, coverage and sampling disclosure; faithful derivatives if needed |
| Direct audio/listening | FLAC stream metadata and language tags except E11 | Actual listening, language/content verification, stream/time calibration and adequate delivery to each required analyst |
| Japanese dialogue/text | Twelve external candidates with script/timing metadata | Accuracy, speaker/line identity and edition alignment; an adequate E04 route; no official or production-script status established |
| Visual frame evidence/index | Source video exists | No extracted frame set, scene index or reviewed visual witness prepared in this bootstrap |
| Audio analysis assets | Embedded audio exists | No separate calibrated listening/clip set or analyzed waveform prepared |
| Transcript and cross-modal linkage | External text candidates only | No verified continuous transcript, cue-to-scene map or full bundle linkage |
| Complete episode bundle | None | All semantic responsibilities, coverage and QA under the live bundle specification |
| Supplementary material | Menu candidate identified | Its content/relevance uninspected; no admitted scripts, commentary, interviews, novels, manga or later films/episodes |

The large MKVs require actual runtime transport verification and possibly faithful derivatives, not a presumption that a provider can inspect the original files. Any derivative must retain source hash/interval, stream mapping, time transform, encoding/sampling limits and quality assurance. Keep restricted source media, extracted frames, transcripts and full subtitles in authorized private environments. The repository stores analytical outputs and safe witness metadata only.

Before the first run, recover owner authorization, verify the selected edition/witness and complete required bundle/text/AV routes, record role/capability and independence receipts, fix the admitted boundary and run stop, then update the [entrypoint](../CURRENT_STATE_AND_CORPUS_MAP.md) under the initiation contract. The admitted-source table remains empty until that actual transaction. Preparing a source, finding a folder or confirming a hash does not open admission.

## Inventory changes

The integrator owns attributed additions and corrections. Preserve original hashes and labels, record changed bytes as new witnesses, distinguish unavailable from not searched, and never infer later corpus completeness from this bounded directory. Metadata evidence can refine candidate identity without changing narrative coverage. Subsequent edition/content verification records exactly what was inspected and by whom, with any remaining uncertainty.

Current summary: 11 available numbered media candidates (2 admitted: `PP-S01NE-E01`–`E02`; 9 metadata-only pending sequential frontier: `E03–E11`); 1 excluded menu; 12 external text candidates; 11 structurally validated episode bundles (2 content-authenticated: `E01–E02`); 2 accepted canonical deep readings (`PP-S01NE-E01`–`E02`).

### 2026-11-23 Attributed Inventory & Admission Updates (`PP-S01NE-E01` – `E02`)

| Admitted Unit | Primary AV Witness | Canonical Lossless Audio | Primary Japanese Text & Calibration | Bundle & Runtime Verification |
| --- | --- | --- | --- | --- |
| `PP-S01NE-E01` | `PP-S01NE-E01-AV01` (`1603b8b0...`, `2753.194s`, `audio_start=0.000s`, content-authenticated Season 1 New Edit Episode 01, 100% watched) | `PP-S01NE-E01-AUD-FLAC01` (`225,075,213` B, `4005a1e3e83f46f8a48656845edd779c90f472b1f16538532692259b3b604f2f`, decoded 16-bit PCM `fdaaf145...` bit-exact with MKV FLAC) | `PP-S01NE-E01-TXT-BD01` (`e940679b...`, `624` cues): calibrated linearly across opening, Block 3 (`00:13:34–00:16:45`), and closing (`0.000s` global offset, `|error| ≤ ±0.4–0.5s`); `TXT-TV01` (`ca77a4ea...`) wording diffed (1 omitted breathing cue `ハァ…ハァ…！`). | `PP-S01NE-E01-BUNDLE-V1`: 9/9 semantic layers (`1,350` kept 1080p frames, `68` contact sheets, `541` shots, `0` broken links; `paired_subtitle_file: null` metadata caveat disclosed). Runtime: overlapping 720p MP4 segments + 11 zero-recompression lossless MKV clips + 25+ 1080p `FRM` stills + 50 ms `AM` RMS checks (`1.0 fps` model video sampling disclosed). |
| `PP-S01NE-E02` | `PP-S01NE-E02-AV01` (`77d1ee15...`, `2752.171s`, `audio_start=0.111s`, content-authenticated Season 1 New Edit Episode 02, 100% watched) | `PP-S01NE-E02-AUD-FLAC01` (`215,444,913` B, `bd9d3d759410f74dec0952f79426e96ca8f405961a8c3218bdf6e883e98761bb`, decoded 16-bit PCM `f203fea8...` bit-exact with MKV FLAC) | `PP-S01NE-E02-TXT-BD01` (`c4630c23...`, `683` cues `00:00:01.85–00:44:30.40`): calibrated across 6 opening/middle/closing 50 ms `AM` RMS anchors incorporating `+0.111s` audio start (`|error| ≤ ±0.5s`, fractional-second act-boundary phase shifts noted); `TXT-TV01` (`a7ab9ecd...`) wording diffed (`0` diff blocks, 100% identical text). | `PP-S01NE-E02-BUNDLE-V1`: validated (`1,478` kept clean 1080p frames, `74` contact sheets, `620` shots, `10` scenes, `valid: true`, `offset_applied_seconds: 0`). Runtime: 8 overlapping 720p MP4 segments + 15 zero-recompression lossless MKV clips + 23 native 1080p `FRM` stills (incl. 4x zoomed crops) + 50 ms `AM` checks (`1.0 fps` sampling disclosed). |

- **Unadmitted Corpus Metadata Watchpoints (`E03–E11`, no narrative inspection):** All remaining episode bundles pass structural validation (`0` errors) and standalone FLACs match bundle copies bit-exact; preserve non-zero MKV audio stream start offsets for `E04` (`0.067s`), `E06` (`0.056s`), `E08` (`0.111s`), and `E10` (`0.070s`), E04's missing archival external subtitle witness (`45` `ASR_UNVERIFIED` bundle cues flagged in metadata), E10 Block 1 anchor sparsity note, and E11's untagged audio language field for verification when each unit reaches its authorized frontier.
