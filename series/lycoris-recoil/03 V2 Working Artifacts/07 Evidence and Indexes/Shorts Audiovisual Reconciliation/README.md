---
series: LYCORIS_RECOIL
artifact_type: evidence_index
generation: V2
scope: friends_shorts_01_to_06
status: canonical
source_boundary: TV E01-E13 and Friends Shorts 01-06 only
---

# Friends shorts · audiovisual reconciliation

The six shorts repeatedly set up a familiar musical ending and then find a different place for it to land. Short 02 starts it twice. Short 04 introduces it while the scare is still unfolding. Short 06 finally lets it carry Mika’s reveal into the sung passage and the rolling credits. This is the strongest new cross-short finding. The character evidence is more local. Takina can originate a civilian project and veto its cost, privately try the role she publicly polices, and nearly disclose the truth to fans who take her for a cosplayer. Those scenes do not establish a single travel chronology or private romantic motives.

Read the [53-proposition claim matrix](CLAIM_MATRIX.md) for the decisions and [corrections, disputes and verifier referrals](COVERAGE_AND_OPEN_ITEMS.md) for their effects on the earlier readings and Gemini’s retrospective. The separate [TV record](../TV%20Audiovisual%20Reconciliation/README.md) remains the authority for TV returns. This comparison supplies an attributable overlay. The six source readings retain their original language and release-order horizon.

The [source-reading participation and CP4 correction](SOURCE_READING_PARTICIPATION_AND_CP4_CORRECTION.md) identifies each independent execution context and its unit-specific contribution before and after the source seals. It also governs the terminal prediction count used at CP5.

## What was compared

The local series source inventory identifies the prepared Japanese masters under `00_prepared_japanese_mkv/friends/`, Gemini’s analysis masters under `02_media/hardsub_mkv/s00eNN.analysis-hardsub.mkv`, and the reading bundles and `audio/s00eNN.complete-audio.flac` under `03_ai_analysis/`. All six prepared-master and hardsub first audio streams reproduce the corresponding FLAC when decoded to native 44,100 Hz stereo signed 16-bit PCM. This tests audio identity at that precision. The hardsub and prepared video pictures differ by the burned lettering. Corrected and styled Japanese ASS files match the six source-manifest digests. The written dialogue records also match the corresponding bundle selection. All measurements use local elapsed media time. Captions supply their own cue bounds. They are not a clock for the exact instant a syllable is heard.

The independent run is `_analysis_work/gemini_independent_continuous_av_v1/`. Its `06_handoff/FROZEN_HANDOFF_MANIFEST.json` has SHA-256 `a8624af20d42f82038c154c00056dbe220e60d5c1d77840d7e3f1653b0bc25fb`. All 152 listed files match their byte lengths and hashes. This checks the frozen inventory, including its existing TV portion. No external source was admitted. Each short has a unit reading in `01_unit_readings/friends/` and six files in `02_specialist_and_review_records/S00ENN/` covering visuals, audio, character, dialogue, blind review and adjudication. All six Agent F byte-prefix hashes reproduce at the marked Stage 1 freeze. The original run reports its viewing order. The hashes authenticate the saved text. They cannot replay the producer’s actual viewing session.

| Short | Bundle or master coverage | Japanese cues | Gemini clips | Sealed claims | Blind F2 decisions | Quarantined source-draft errata |
|---|---|---:|---:|---:|---:|---:|
| 01 | 135.070 s, existing frozen reading rechecked | 50 | 1 | 8 | 5 | 16 |
| 02 | 195.048 s, 105 retained images, 6 sheets | 80 | 1 | 9 | 6 | 21 |
| 03 | 210.071 s, 132 images, 7 sheets | 90 | 2 | 9 | 8 | 23 |
| 04 | 245.063 s, 123 images, 7 sheets | 105 | 2 | 9 | 7 | 25 |
| 05 | 195.048 s, 104 images, 6 sheets | 84 | 2 | 9 | 9 | 18 |
| 06 | 315.048 s, 180 images, 9 sheets | 93 | 2 | 9 | 9 | 20 |

Short 06’s errata section reports nineteen in its heading and enumerates twenty distinct IDs (6 + 3 + 6 + 3 + 2). The table uses the enumerated count.

Ten available proxy clips cover all six units, including the endings. Divided clips overlap. The S05 and S06 clip directories lack the per-unit clip-ledger JSON present for S01–04. For those two last units the clip files and their overlapping bounds supply coverage. The six adjudications contain 44 F2 decisions. Adding the TV count of 121 gives 165 for the entire independent run. The aggregate coverage prose gives 164. The machine manifest and individual adjudications govern. The seven ledger files total 612,989 bytes and the four synthesis files 86,352 bytes. Differences from the written audit’s aggregate counts do not invalidate their individually verified digests.

### Source identities

SHA-256 of the local hardsub input and Gemini’s final unit reading. The frozen native Short 02–06 readings and per-bundle digests are in the [series map](../../../CURRENT_STATE_AND_CORPUS_MAP.md) and each reading’s opening inventory.

| Short | Analysis master SHA-256 | Gemini reading SHA-256 |
|---|---|---|
| S00E01 | `12ac4f7ab327b02dd8c376cedab96a718f1f7e855a2b34ec18f3282887bd0db1` | `57ed2f37525fbfc8dfefcf411932824aacf6941d9529425b0e97260aa9b98646` |
| S00E02 | `07d0fe81f45d473797382bf883b787d4f81355627e571143061a620769a3985f` | `928e16933ee8409fa0cc9f1d6b019fa3635b6f5c5ec12bd871e91fec1b6ecc59` |
| S00E03 | `8c519738e7184527acef3d95a7a1b81d21d596c3ad4043e36534dd96adb0dfb0` | `2eb6f25887ac2d91e6400022b29fdd5c5af058b350da5f7f5a57612c31c48145` |
| S00E04 | `8a7047a91d8db6c03714ff5978db7185d09aa44906fbe03b0c1a97915eaf9453` | `1d41fe5af00c7698c84fbaaf62507b8ade8c719a1b3ed1e307d4ac4184397f0f` |
| S00E05 | `16ffb2acb56457fbd479b77ac31f51ea0dbe76c5d446c7a7a79af74c59744217` | `e310dac0820e7f9d6a21f740dfd06c89667ffd5c3f65857ee9a98bb408ed0d08` |
| S00E06 | `e8a59afd474e9ef946259c5ee4d9a09658c1c31bd629c8cca4a49af447fefea0` | `72ee29c8d46407f257844f6c7b751c85c36e06872e9189031a33cd3576c58788` |

## How decisions were made

Shorts 02–06 were opened one at a time. The source reader used Japanese cues, every retained bundle sheet, selected diagnostic frames and measurements from the complete FLAC. Each short received an outbound freeze before admitting the next one. Separate specialists tested image/text and sound/source identity. An independent critic reviewed the resulting freeze and the bounded V1 comparison. Only the principal integrator wrote shared records. The six source readings and ledger state preceded the opening of Gemini’s short reports. Git tree `9064e0d5fd0f9a5335150cb76aec015fcce030f8` preserves that boundary. Short 02’s published text standardizes trailing Markdown hard-break spaces from its initial freeze. No words or forecasts changed in that normalization.

For the retrospective pass, two range specialists independently compared S01–03 and S04–06 with the earlier readings. A third reviewer audited provenance, cross-short assertions, primary controls and negative evidence. The principal tested music alignments and adjudicated competing readings. The review included all six unit reports, all 36 specialist/adjudication files, the short contributions in seven cumulative ledgers and the four full-corpus retrospective documents. These records share the same underlying pictures and audio. Agreement between their authors is weaker than an independently reproduced source check.

The producer’s capability report describes an initial multimodal pass with audio and approximately one visual sample per second, followed by targeted native-frame inspection, short-sequence and PCM tests. Here the receiver could inspect individual decoded pictures, frame sequences, crop detail, sample peaks, channel width, exact-zero intervals and TV reference correlations. It did not perform a native continuous perceptual AV audition. Relative vocal color, masked words, intentionally mixed simultaneity and what characters perceived retain the provenance stated in each row. The [open-item register](COVERAGE_AND_OPEN_ITEMS.md) routes consequential auditory questions to an independent Japanese-speaking listener with synchronized playback.

## Outcome and authority

The 53 primary dispositions are 32 STRENGTHEN, 12 REVISE, 4 DOWNGRADE, 4 PRESERVE and 1 OPEN. Additional rejected subclaims, such as the all-hiragana notebook and exact 14.35-second Short 04 music duration, are documented separately so one compound source ID is counted only once. CP4’s corrected twelve comprise seven supported, four partially supported and one not tested across Shorts 01–06. The earlier five-partial total credited PRED-CP4-004 for group planning. The shorts finish the 19-unit A1 reading horizon. The ensuing Phase D baseline is frozen at CP5, subject to the attributable prediction-count correction above. The independent retrospective’s monograph recommendations do not substitute for that operation. Supplementary narrative evidence remains outside this record.
