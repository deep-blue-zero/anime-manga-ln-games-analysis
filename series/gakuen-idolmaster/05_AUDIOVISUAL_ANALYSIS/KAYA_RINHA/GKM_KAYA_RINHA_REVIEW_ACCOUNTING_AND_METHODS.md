---
series: GKM
generation: V2
artifact_type: audiovisual_documentation
scope: KAYA_RINHA_DISTRIBUTED_CHARACTER
status: canonical
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
source_boundary: "RINHA-AV-20260911: Source Lock 1.0, 18 targeted scenes, sampled stills and computed final-mix audio only; direct listening and continuous-motion review unperformed"
last_updated: '2026-09-11'
---

# Kaya Rinha — actual review accounting and methods

Execution: 2026-09-10–11. Toolkit: **AV Evidence Toolkit 1.1.0rc2+retiming.1**, the locally tested repair of the retimed-video regression. Python 3.12.4; FFmpeg/FFprobe 8.1.1. The runner extended only the process timeout to 1,800 seconds for long recordings; evidence algorithms were not changed for this analysis. The earlier toolkit regression/wheel tests remain the software-validation record.

## What was actually reviewed

| Modality or operation | Amount | Meaning |
| --- | ---: | --- |
| Targeted scene bodies and their still samples | 18 | All 11 P0 and 7 P1 responsibilities have a bounded scene record |
| Inspected still point presentations | 540 | Recorded from actual displayed sheets, including initial/locator controls |
| Distinct source frame points | 538 | Deduplicated by source SHA + video stream + integer PTS + time base |
| Inspected sheets | 97 | Dense target sheets, 15 initial sheets, support overview and locator controls |
| Direct listening | 0 seconds | Audio input test was omitted by the environment |
| Continuous-motion review | 0 seconds | Still extraction and display do not supply continuous perception |
| Still-derived interval coverage | 0 seconds | Point observations receive no interval review credit |
| Selected-mix measurement windows | 18 | Computed, technically verified excerpts; not heard |

The [actual display ledger](SUPPORTING_DATA/actual_review_accounting.json) names every inspected sheet and point with its hash. Generated P0-008/009/010 initial sheets were not displayed and are excluded. A repeated display does not add a point. Full frame-index attempts that hit a timeout generated no accepted complete index. The dense sheets were inspected in their central viewport; full extracted images remain available locally, but their unexamined side regions do not silently gain review credit.

## Source and timing procedure

1. Probe each supplied file, hash it, check stability and select main video stream 0/audio stream 1. Ignore attached cover art as a video stream for analysis.
2. Retrieve the 18 A1 bodies, verify exact bytes against the recovered Source Lock archive, and parse message/voice/motion/BGM/SE commands as source metadata. Engine times and asset keys are not recorded performance timings.
3. Use chapter tags and engine clocks only to propose searches. Compare actual Japanese captions to the A1 scene. Keep conservative scene envelopes and accepted point anchors separate from unverified alignment proposals. A single offset fails with unvoiced/manual-advance sections; no fabricated subtitle timeline is published.
4. Extract original-source PTS stills with FFmpeg `-copyts`, input seek, selected video stream, `showinfo`, no interpolation and scaling to readable PNGs. Require the first accepted frame to fall at or shortly after the request and preserve integer PTS/time base and output hash. Derived central-viewport contact sheets have separate hashes and do not certify unseen motion.
5. Use toolkit `clip-audio` with explicit source stream 1 and interval. Retain native 44.1-kHz stereo decoded f64 samples; verify the decoded WAV against the selected samples and preserve the parent interval mapping.
6. Run toolkit `audio-metrics` on WAV stream 0. Verify its parent file SHA and PCM SHA against the clip receipt, then join the derivative-relative measurements back to the original-source interval. All 18 selections report complete coverage, zero missing selection seconds and zero timestamp adjustment in these runs.

Integrated LUFS/LRA/true peak are FFmpeg loudness-filter **input** measurements. `volumedetect` mean/sample peak uses its documented signed-16-bit conversion, retained in the JSON. The filter’s proposed output-normalization values are not source observations and are not interpreted. No source normalization, channel downmix or isolated-Rinha assumption was used. The original AAC recordings remain lossy; sample preservation refers to their decoded signal, not recovery of a studio master or container/packet identity.

The retiming fix makes an invalid timing certificate fail; it does not transform a computation into a perceptual review. No imported retimed video was admitted as watched in this pass. Audio derivative checks do not establish original audiovisual synchronization. Pitch, jitter, shimmer, timbre, crying acoustics, imitation fidelity, overlap and reaction latency remain unmeasured/unheard at the actor level.

## Reproduction and retained evidence

The companion local working directory is identified as `rinha-av-20260910` and remains outside Git. It retains the original per-frame receipts/logs, script-search proposals, toolkit inventory/clip/metrics runs and extracted WAVs. `SUPPORTING_DATA` in this Git packet contains portable source identities, accepted target mappings, measured values and actual inspection ledgers; raw source scripts, videos, audio, still-image derivatives and local execution tools stay outside Git under repository policy.

The companion local review ZIP contains the reviewed sheets, frame receipts and a scene navigator. Its navigator accepts user-selected local recordings and uses the source times above; it neither uploads files nor records playback as completed review. To close the perceptual gate, a reviewer must identify the exact source/hash/stream, record genuinely reviewed intervals, report observations and limitations, and reconcile each affected claim. Playing a file or running an algorithm alone must not mark that work complete.
