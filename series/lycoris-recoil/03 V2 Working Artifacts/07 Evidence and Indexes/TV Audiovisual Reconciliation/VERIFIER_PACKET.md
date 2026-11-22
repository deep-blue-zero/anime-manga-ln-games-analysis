---
series: LYCORIS_RECOIL
generation: V2
artifact_type: verification_handoff
source_boundary: TV E01-E13 only
analytical_base: b84f1da3812dadf64e62491f5e64bca4f3ea6500
---

# Observation packet for a Japanese-speaking audiovisual verifier

**READY_FOR_HANDOFF · TV only · VIDEO_TARGETED_ESCALATION.** For picture-and-sound work use the Japanese hardsub master in the table below. For by-ear transcription use its audio stream with the picture hidden, or the prepared Japanese companion in `00_prepared_japanese_mkv/tv/Lycoris Recoil - NN.mkv` with subtitle display disabled. Freeze the transcription before comparing picture or written cues. Inspect synchronized sound and moving picture on a surface that has demonstrated this capability. For a frame-scale question, document native-rate stepping or an independent deterministic measurement. For a listening question, state the exact audio stream and playback route.

Work from this packet first. Record interval, calibration anchors, sample rate or effective visual sampling, observed event order, what is obscured and confidence. Use the full displayed image and a little context on each side. For each episode, align beginning, middle and end against the neutral clock anchors below. Record any new offset. Freeze the observations before opening the [adjudication register](DISPUTES.md) or the originating claims. An observer who has already read the expected answers should disclose that as part of their return.

| Queue | Episode | MKV window | Channel | Neutral question |
|---|---|---|---|---|
| TV-Q01 | E01 | 19:12–19:44, 20:04–20:09 | Motion / cuts | At each cut, describe Chisato’s first visible posture and the next change that can actually be followed. |
| TV-Q02 | E01 | 22:17–22:46 | Music / dialogue | Locate the first recognizable ending-song material, the first line after its entry, and the first credit image. Describe what changes in the mix. |
| TV-Q03 | E02 | 14:11–14:16, 22:16–22:45 | Gaze / response | Which objects and faces are visible before and after each cut? In the closing scene, place each turn relative to the movement of the hair tie. |
| TV-Q04 | E03 | 02:30–02:38, 09:02–09:10 | Visible information | Which details can be read in each interface or photograph, and which details repeat across displays? |
| TV-Q05 | E03 | 22:15–22:45 | Voice / music | Locate the end of Takina’s last audible answer and the first recognizable musical phrase relative to the credit cut. |
| TV-Q06 | E06 | 11:42–11:50, 18:46–18:56, 22:05–22:15 | Space / disclosure | What can the shots disclose about the camera feed, Majima’s recognition and Chisato's visit? Record any event omitted by the edit. |
| TV-Q07 | E07 | 21:28–21:56, 23:10–23:15 | Music / cut | Mark the first musical material, change of image, last musical material and return to the story. Distinguish a mix change from a new cue. |
| TV-Q08 | E09 | 21:37–22:09 | Music / response | Place the first snow, final vocal response, first ending-song material and first credit image in order. |
| TV-Q09 | E10 | 19:50–20:16 | Action / sound-image | Describe what is visible at each report, the order of body movements, and the last visible state of each participant. |
| TV-Q10 | E10 | 17:03–17:38, 20:52–20:59 | Music / voice | Identify the audible bed between the lines and at the announcement. Record the point at which a sound can no longer be identified. |
| TV-Q11 | E11 | 00:06–00:12, 22:18–22:30 | Voice / masking | Transcribe as much of the opening broadcast as audible. At the closing exchange distinguish voices, discrete sounds and visible contacts. |
| TV-Q12 | E13 | 00:00–01:17, 09:02–09:12 | Music | Describe which vocal and instrumental material is identifiable during the opening credits and during the later entrance. |
| TV-Q13 | E13 | 07:18–07:34, 08:05–08:12 | Performed voice / audiovisual synchronization | Transcribe Yoshimatsu’s pronouns without consulting subtitles first. At the exterior cut, separately log light, audible transients and their timing. |
| TV-Q14 | E13 | 16:05–16:24 | Spatial choreography | Log initiative, reactions and visible effects in order. Flag events whose source is outside the shot. |
| TV-Q15 | E01 | 14:33–14:47, 20:40–20:44 | Japanese voice / latency | Locate the actual end of the question and start of the reply. Transcribe the shopkeeper’s greeting and the later reported phrase by ear before comparing their captions. |
| TV-Q16 | E02/E03/E04/E05 | E02 09:20–09:25, 11:26–11:29 / E03 16:29–16:37 / E04 20:17–20:22, 20:40–20:43, 21:39–21:42 / E05 06:37–06:42 | Japanese voice / overlap | Write the audible words and interjections, identify the speaker where possible and mark masked syllables. Compare with the written witness only after freezing the log. |
| TV-Q17 | E12 | 08:07–08:21 | Editing / sound synchronization | Describe the image at the report, the states of Chisato and Yoshimatsu on either side, and any intervening shot that depicts the action itself. |
| TV-Q18 | E08/E13 | E08 21:28.2–21:38.5 / E13 04:32–04:39 | Sonic recurrence | Identify the salient pitch and timbre among background sounds. Describe changes in relation to the visible action. Preserve the possibility of independent sound effects. |
| TV-Q19 | E13 | 03:53–04:10 | Prop continuity | Identify any visible continuity that establishes what Chisato is carrying or using in this interval. Record what the edits omit. |
| TV-Q20 | E01 | 02:49–02:54, 13:58–14:03, 21:11–21:17 | Cut / mix / perspective | Describe what remains perceptible before and after each low-level interval and what changes with interior and exterior perspectives. |

Q01–03, Q05 and Q07–14 are required before the corresponding disputed perceptual detail can be promoted. Q17 and Q19 are required only for stronger claims about visible contact and identifiable equipment. Their independent text, image and measurement decisions are already complete. Q04, Q06, Q15–16, Q18 and Q20 are optional follow-ups unless a later claim depends on their specific detail. Even a capable viewer may be unable to resolve information deliberately withheld by an edit. Return an explicit OPEN for that case. The integrator will retain the frozen return, apply the contradiction and verification criteria, and record one disposition per item.

## Source clocks for the verifier

Source root `Lycoris_Recoil/02_media/hardsub_mkv/`. Times below are Japanese ASS cue onsets on the source MKV clock. The picture is native 24000/1001 fps and the Japanese audio is 48 kHz stereo. In E01 use the ASS ID where two events overlap at 00:21.17.

| File | SHA-256 | Beginning, middle and end |
|---|---|---|
| ep01.analysis-hardsub.mkv | `495b91dba248e32200e500daed6bddce66473252d9c6c181aebbfd6c250e5950` | C0001 @ 00:01.69, C0276 @ 11:01.52, C0550 @ 23:58.29 |
| ep02.analysis-hardsub.mkv | `8010992a7795c47a29fb86a467e9852e9cabf70800f216e2d0fc5c9e220615b2` | C0001 @ 00:02.44, C0233 @ 12:30.94, C0464 @ 23:58.33 |
| ep03.analysis-hardsub.mkv | `0cb2dd474c7ba8a8fa1d702e3f0e8172381f78a4b59c93b7305b7636bd860df4` | C0001 @ 00:02.40, C0238 @ 11:53.32, C0475 @ 23:58.38 |
| ep04.analysis-hardsub.mkv | `4742a4ad6918c9a1065b50da7d78af98c0eb79469c6e5f29f660e1e892bb3877` | C0001 @ 00:01.44, C0227 @ 11:43.06, C0452 @ 23:56.04 |
| ep05.analysis-hardsub.mkv | `edd8ba3f87a5b0e94a836635d5a462a2538e0d6325f9096ff34087ec292830e7` | C0001 @ 00:01.65, C0215 @ 12:17.05, C0429 @ 23:58.46 |
| ep06.analysis-hardsub.mkv | `e998e2409da245fd03bd0b94fbe1f62f3f87de0b9f69becb409fdabc13fba5e2` | C0001 @ 00:07.65, C0246 @ 12:35.65, C0491 @ 23:58.29 |
| ep07.analysis-hardsub.mkv | `24212b2375856a728c62ad643e83f12b04878e06d3f840db47fb5818f8213358` | C0001 @ 00:01.57, C0238 @ 11:25.50, C0475 @ 23:46.32 |
| ep08.analysis-hardsub.mkv | `707e1ba464fd1b3af9878290b3c13ed163cd7ba71aa66a2c7d7fedf38fff5d20` | C0001 @ 00:08.84, C0236 @ 11:29.90, C0470 @ 23:58.35 |
| ep09.analysis-hardsub.mkv | `91f1d9e8b6f9a07f056beceb6a138599b3f1a095e4143bed6db3e0b28e583d83` | C0001 @ 00:03.90, C0199 @ 11:50.23, C0396 @ 23:58.67 |
| ep10.analysis-hardsub.mkv | `077339d1d447cede6f4e41d03e0e21e04030d74a8b886c20627fb5260f00d295` | C0001 @ 00:02.06, C0223 @ 11:41.34, C0445 @ 23:58.41 |
| ep11.analysis-hardsub.mkv | `29c5532e9abe8699c073432cc0f609aa88bc49c682570ee20b56c3745bffeda5` | C0001 @ 00:05.99, C0220 @ 12:04.08, C0439 @ 23:58.38 |
| ep12.analysis-hardsub.mkv | `ff47f4b4c36ca70c05355efc0c6f9c67d583efce79c231de2ba95386df19197f` | C0001 @ 00:01.61, C0242 @ 12:43.91, C0482 @ 23:58.50 |
| ep13.analysis-hardsub.mkv | `4b5a4052bba4afae6c7aa1bf1507532975d66de62be70f15900a936222a42933` | C0001 @ 00:03.53, C0244 @ 11:06.52, C0486 @ 23:59.17 |
