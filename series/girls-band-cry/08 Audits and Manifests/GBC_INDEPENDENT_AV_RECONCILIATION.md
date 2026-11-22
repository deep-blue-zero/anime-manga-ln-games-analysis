---
series: GBC
artifact_type: audiovisual_reconciliation_report
scope: E01-E13
analysis_generation: V2
status: active_provisional
source_boundary: "GBC-V2-SOURCE-LOCK-1.0 television series, frozen V2 sequential readings, and restricted retrospective AV observation evidence"
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
stage_state: READY_FOR_HANDOFF
created: 2026-11-22
updated: 2026-11-22
---

# Girls Band Cry · Independent audiovisual reconciliation

## What was completed

All thirteen V2 episode readings and four sequential checkpoints now exist. This report records the retrospective comparison and the remaining work needed for claims about performance, editing, attribution and timing. The accompanying question packet is the only document intended for the return observer before their log is frozen.

| Milestone | Git witness and result |
|---|---|
| Authority and base | Registered `girls-band-cry`, GIT_PRIMARY. Verified entrypoint `series/girls-band-cry/CURRENT_STATE_AND_CORPUS_MAP.md`. Initial main read `e3571eb717f06a2fbe17b02c4a3f508a79573ede`; preserved subsequent concurrent work by advancing to actual branch base `ceb4675196d22cfc291842328cfd5c42d867bc77`. |
| Archive and E11 ledgers | `486d1c9a611c374b2c9689a36a2a1752ae8c098a`. Sixteen R100 relocations to `90 Legacy and Superseded/V1/`, with all 16 current blobs verified identical. The archival checksum list covers 13 readings and the manifest. All 14 match original import `9957068cc942bdfbfb4f3fbd39c0c6aca13ed2ea`, and none matches the already-modified pre-move current bytes. The original checksum list, full-series document and E13 gap record were preserved. The map documents the complete crosswalk. [Exact-head audit](https://github.com/deep-blue-zero/anime-manga-ln-games-analysis/actions/runs/44994449756) |
| Cumulative infrastructure | All seven ledgers were first materialized from V2 E01–E11 following the E08 authorization and E11 reset. The revision ledger carries 84 baseline targets, with traceable prior transitions. The E12, E13 and checkpoint changes were written into the same seven files. |
| E12 | `df319357282053800d3647a1a52b37e523a682ad`. Atomic reading, seven ledger deltas and entrypoint. Three independent specialist/review contexts plus a principal. All 511 cues, 676 retained frames across 34 sheets and a full mixed-track decode were covered. [Exact-head audit](https://github.com/deep-blue-zero/anime-manga-ln-games-analysis/actions/runs/44995068064) |
| E13 | `85548af477932ee0475e4d2b83c00885ccd4ca6d` on the active E12 parent; publication proof `00920e758d2ddd2b77a12da6a51cc190036adf91`. Same role separation, 503 cues, 813 retained frames across 41 sheets, separate ending review and full mixed-track decode. The critic corrected the concert interruption and lyric endpoint. [Exact-head audit](https://github.com/deep-blue-zero/anime-manga-ln-games-analysis/actions/runs/44995917407) Source, prior-hypothesis exposure, rejected readings and disagreements about the credits are recorded in the episode. |
| Checkpoint 4 | `ba568fc0656158d1b46c8def2a96a8139e33b9d2`. All 27 prospective formulations match CP3 verbatim. The 54 events give 26 CONFIRM, 13 PARTIAL, 0 CONTRADICT and 15 NON-DIAGNOSTIC. Unique totals are 14 STRENGTHEN, 4 REVISE, 1 PRESERVE-FULFILLED and 8 OPEN. E09’s earlier falsification remains available. [Exact-head audit](https://github.com/deep-blue-zero/anime-manga-ln-games-analysis/actions/runs/44996612896) |

The two independent E12/E13 readings closed under the owner’s express authorization for text, frames and acoustic measurements, with qualitative delivery deferred. Bundle fingerprints are available in the observation packet. No primary media or transcripts were included in the analytical branch. The thirteen locked ZIPs agree with the published inventory wherever it gives names, sizes and extraction counts. The published inventory provides no ZIP digests; the SHA-256 values here identify the local copies. The only differing files between the E12/E13 archive and expanded copies carry historical absolute paths.

The publication branch is `series/girls-band-cry`. The PR body is the external receipt for the exact terminal branch commit, required checks and their URLs. A commit cannot carry its own hash in a tracked document. The last commit that changed this report and the current PR head are separately recoverable. A merge into main remains with the integration owner. [PR #698](https://github.com/deep-blue-zero/anime-manga-ln-games-analysis/pull/698) · [Report history](https://github.com/deep-blue-zero/anime-manga-ln-games-analysis/commits/series/girls-band-cry/series/girls-band-cry/08%20Audits%20and%20Manifests/GBC_INDEPENDENT_AV_RECONCILIATION.md)

## Which Gemini evidence entered the comparison

After the checkpoint commit a metadata-only traversal found **2,519 files** in `gemini_independent_continuous_av_v1`. The traversal recorded relative names, sizes and modification times. It did not index contents. The principal selected technical manifests, source-derived stills or strips, numerical measurements and standalone E1 observations. Each selection was written to an exact-path allowlist before copying or projection. Reviewers received private views restricted to their assigned episodes. The exposure register below identifies every selected file, source hash, the admitted material and its reader.

The technical method distinguishes the critic’s E1 blind observation pass from E2 adjudication after reading the other agents. Four independently named `critic_eNN_blind_notes.md` files for E08–E11 could therefore be admitted in part. A bounded extractor required an E1/Blind header, restricted output to question groups and source-channel or time-marked observational sentences, skipped interpretation/summary sections and stopped at an E2 or adjudication heading. Numerical JSON views retained structural keys and numeric values. No concluding prose from those metric files was passed to reviewers. Standalone E1 projections contain 74, 58, 54 and 62 records respectively; those are fragments of evidence, not 248 independent claims. The exposure register records exact source line numbers. Source materials and working copies remain private.

The 13 consolidated AV readings, 13 multi-agent checkpoints, principal/character/music/visual/critic analytical reports, cumulative interpretive ledgers, final audit, synthesized series files, run index, run checkpoint and freeze/handoff narrative were excluded. The remaining unselected technical working files and media were inventoried only. In particular, an E2 critic document was never opened to look for an E1 section, and a specialist filename was never treated as an observation log. No search, model summary or embedding of this excluded material was used.

**Independence and temporal resolution.** Gemini’s manifest reports isolation from V1/V2, title-repository history and published external analyses. The method documents a blind-first procedure *within* Gemini. The present comparison is retrospective. The specific order of an independent Gemini response to *this Codex verification packet* was never established (`blind_order_achieved: null`). An earlier independent source pass and a newly commissioned blind return are different evidentiary events.

Gemini’s reported six-second test recovered six images at one-second intervals, starting at +0.458 s, and three ascending tones. A Japanese speech test and five-minute chunk test supported synchronized continuous audio with **1 fps effective native video**. Each episode had five scaled 540p MP4 parts, nominally five minutes with ten-second overlap. The source-clock equation is source start of part plus part-relative time. A stream-copy MKV probe began roughly nine seconds early because of keyframe seeking; its offsets do not apply to the accurate-seek MP4s. Separate frame strips where available can support finer timing at their declared sampling rate. Neither a clip manifest nor the successful probe authenticates an unreported interpretation or individual delivery.

The principal reproduced all thirteen source MKV SHA-256 values, matched them to the source inventory and capability manifest, and checked the thirteen clip manifests. The coverage ledger reports zero nominal source offset across all thirteen and complete clip exposure per episode. Our 39 beginning/middle/late visual reference points agree closely on the matched encode or an adjacent frame at a cut. The hashes, runtimes, byte counts and per-episode calibration anchors are in the return packet. Record exact subsecond source/bundle uncertainty at a given cut. Gemini’s additional 4–24 fps diagnostics improve only their actual intervals. Japanese ASS is a source transcription, not a studio script. All clips were reported Japanese; six original MKVs lack a language tag.

The retrospective inspection scope is asymmetric. In E08–E11 a reader could evaluate separately documented verbal observations of selected diagnostics. In E01–E07 and E12–E13 the admissible comparison consists of Gemini-selected source specimens and, where available, numerical measurement records. A row based on an image says what the specimen shows. It does not purport to quote Gemini’s unseen conclusion, or certify a listening judgment from a picture. There is some meaningful comparison in each episode. No episode has an unrestricted claim-by-claim audit of its entire reading.

Two standalone E1 extracts included incidental reviewer grade language at E10 line 160 and E11 line 202. The reviewer saw those words and discarded the grading. The corresponding rows use only separately stated or primary-verified sounds and pictures. No consolidated manuscript was opened.

## Reconciliation counts and coverage

**53 existing claim components received a meaningful comparison.** 18 PRESERVE, 26 STRENGTHEN, 5 REVISE, 1 DOWNGRADE, 1 REJECT, 2 OPEN. There are also **11 new finding records** (10 accepted within their stated bounds, 1 disputed), and 3 explicitly unsuccessful matches. The latter have no claim transition. The separate neutral packet contains **49 open questions**, 35 required and 14 optional. The unit of count is a decision row; closely linked passages or observations can support one row. An accepted transition need not settle a harder claim about the same scene.

The unresolved observer disputes include E08’s exact low-instrument and unison-voice attribution (one grouped new-finding record), E09’s title-call voice, E11’s audible particle and the E07 correction split across a shot change. The latter is a downgrade in confidence; a rival turn attribution is plausible. The E10 parent identification is a resolved contradiction. Mismatched scenes and a misleading image filename are reported under unsuccessful matches.

| Episode | Meaningfully evaluated | New findings | Unsuccessful matches | Verbal blind observations admitted | Explicit V1 target IDs present in frozen reading | Return items |
|---|---:|---:|---:|---|---:|---:|
| E01 | 2 | 0 | 0 | No separately admissible verbal log | 18 | 2 |
| E02 | 1 | 0 | 1 | No separately admissible verbal log | 25 | 2 |
| E03 | 1 | 1 | 1 | No separately admissible verbal log | 20 | 2 |
| E04 | 2 | 1 | 0 | No separately admissible verbal log | 29 | 2 |
| E05 | 3 | 0 | 0 | No separately admissible verbal log | 33 | 3 |
| E06 | 3 | 0 | 0 | No separately admissible verbal log | 39 | 3 |
| E07 | 3 | 0 | 0 | No separately admissible verbal log | 44 | 3 |
| E08 | 5 | 5 | 1 | E1 diagnostic groups Q1–Q7 | 47 | 7 |
| E09 | 8 | 0 | 0 | E1 diagnostic groups Q1–Q7 | 16 | 3 |
| E10 | 6 | 3 | 0 | E1 diagnostic groups Q1–Q7 | 30 | 2 |
| E11 | 8 | 1 | 0 | E1 diagnostic groups Q1–Q7 | 40 | 4 |
| E12 | 5 | 0 | 0 | No separately admissible verbal log | 23 | 7 |
| E13 | 6 | 0 | 0 | No separately admissible verbal log | 22 | 9 |

The 386 explicit episode/target-ID occurrences are a reproducible census of historical target references, expanding explicit ranges. They are not an exhaustive count of propositions and are not the denominator for the decision rows. Claims without a matched observation receive no disposition. Nine episodes (E01–E07, E12–E13) lack adequate comparative listening coverage; those four with admitted E1 notes are also limited to the documented intervals.

## Corrections with consequences for later work

- **The E10 visitor is Nina’s mother.** Nina hides at work as her mother asks if she is there. Her father appears in a different Kawasaki exterior immediately afterward. The principal checked both the mother with Rupa and Tomo at 05:51.7 and the father outside at 06:06.3 and 06:11.7. Reject the workplace attribution in E10 §§4.7 and 4.25 and any derivative inference about how Nina responds to *him* in the shop. The subsequent paternal encounter and later listening scene remain evidence about father and daughter.
- **E07 cannot securely assign an entire correction to Tomo.** Nina breaks off, Rupa leans in, Tomo appears with her mouth open and a cut shows Rupa under the following cue. The group corrects Nina and keeps playing. Who delivers each clause remains worth hearing. An ensemble intervention cannot support a Tomo-specific behavioral rule until attribution is firmer.
- **E08 gives the music a place inside the cab.** A hand reaches the console and the mix level rises about 6.15 dB in the external measurement and 6.16 dB on the locked MP3. Read the music as available to the occupants as well as shaping the edit. Neither a level change nor Momoka’s tears supplies reciprocal speech. The Japanese register, title spelling and uncaptioned practice reports have separate word-level decisions below.
- **Two texts in E10 and E11 had been made to carry too much.** The E10 phone shows a titled draft and several stanzas. Final published wording and a line-by-line account of composing it remain unverified. E11’s incoming audition email and Subaru’s report that she wrote to her grandmother are separate acts of communication. The later sight of Tendo in the crowd demonstrates attendance. It does not supply her answer to the band disclosure.
- **The audience and the stage must be identified in the actual shot.** In E03 a file with “crowd” in its name pictures the guitarist. In E04 the time-labelled acting strip puts Subaru's raised head and smile before the written reveal cue. E12’s mixed energy cannot locate a speaker, but the photo and hand samples can locate a group gesture. E13’s stage carries a white logo before the red title appears on a pale field. Treat the transition as two observable steps.

## Existing claim decisions

Each heading is a stable erratum or verification locator. Items marked REVISE, DOWNGRADE or REJECT govern later use of their cited original passage. The completion proof preserves the original readings and checkpoints byte-for-byte. This report supplies the errata, the map points here, and the cumulative ledgers carry the accepted formulations. Source-file shorthand below resolves against the path register. “Observed” describes the admitted witness; “primary check” states the separate corroboration or limit.

### E01

#### GBC-AV-E01-01 · STRENGTHEN

**21:34.200–21:42.800; §4.9, cue 431.** Nina’s requested gesture gives the interrupted invitation a visible form.

**Observed.** The 21:34.2 and .7 images frame her mouth. At 21:35.5 she holds the microphone, raises the other arm and extends one digit. At 21:42.8 the free hand is down near her face. The request text identifies the intended sign; the image alone does not settle digit anatomy.

**Primary check.** Original ZIP frames 1119, 1120, 1122 and 1129; primary MKV seeks 1295.5 and 1302.8 s reproduce both poses.

Sampled stills plus Japanese text; no onset or acoustic inspection. · High for witnessed positions, open for continuous trajectory or precise delivery. Affected route — E01 §4.9; visual form and relationship ledgers. Return GBC-AV-Q01-01.

Witness — `episodes/work/E01/critic_hand_2134_2_full.jpg`, `episodes/work/E01/critic_hand_2134_7_full.jpg`, `episodes/work/E01/critic_hand_2135_5_full.jpg`, `episodes/work/E01/critic_hand_2142_8_full.jpg`.

#### GBC-AV-E01-02 · PRESERVE

**22:01–22:02; §§4.10, 9.2; cue 434.** The wider performance presents instruments and passersby alongside Nina’s vocal focus.

**Observed.** The guitar crop includes a guitar neck, part of its player and an occluding dark foreground figure. The object supports a guitar on stage; the crop does not securely identify this player or the audible source.

**Primary check.** Primary at 22:01.000 is a mouth close-up. By 22:01.500 the wider stage includes vocalist, drums, guitars and dark foreground figures. Nominal filename precision is insufficient to assign the cropped frame to 22:01.000.

Guitar crop and two independent timestamped MKV samples, no isolated audio. · High for shared public/instrumental staging; no crop-based player ID, no beat synchrony. Affected route — E01 §§4.10, 9.2; music and visual ledgers. Return GBC-AV-Q01-02.

Witness — `episodes/work/E01/critic_kyoko_2201_guitar.jpg`.

### E02

#### GBC-AV-E02-01 · STRENGTHEN

**12:15.0–12:16.8; 12:48.2–12:49.1; §4.5, cues 246–250, 255.** Nina proposes using a little finger as a private signal, and Momoka accepts.

**Observed.** Both characters are individually pictured with one small finger extended after the agreement. Later a black-sleeved arm outside the truck window changes from open hand at 12:48.2 to the little finger extended at 12:49.1, while the same sung line remains captioned. This adds concrete evidence of the sign being used.

**Primary check.** Exact primary seeks at 735.0, 736.8, 768.2 and 769.1 s reproduce those four states. The original bundle’s nearest frame to 769.1 is 12:49.394, already a cut to Nina. A coarse nearest-frame check alone would miss the response.

Four source-still checks; singer/audibility and exact trajectory remain separate. · High for bilateral use and two truck-window states; moderate attribution of arm to Momoka from continuity. Affected route — E02 §4.5, §9.1; relationship and visual ledgers. Return GBC-AV-Q02-01.

Witness — `episodes/work/E02/critic_e02_q3_momoka_735_0.png`, `episodes/work/E02/critic_e02_q3_nina_736_8.png`, `episodes/work/E02/critic_e02_q3_truck_768_2.png`, `episodes/work/E02/critic_e02_q3_truck_769_1.png`.

### E03

#### GBC-AV-E03-01 · STRENGTHEN

**13:55.500, 14:00.200, 22:06.000; §§4.7, 9.5.** The group explicitly plans to compensate for the missing bassist with a loop machine; the live remains technologically mediated.

**Observed.** Two rehearsal stills show a foot over a cabled, labeled multi-loop pedal with a lit indicator. The 22:06 live image instead shows a drum beater. These furnish instrument-specific visual referents, but do not identify which bass or rhythm layer was heard or when a pedal sounded.

**Primary check.** Primary at 835.5, 840.2 and 1326.0 s reproduces device, foot, indicator and drum beater. Cue 283 names the loop machine. The rehearsal pedal and live beater belong to different scenes.

Exact still correspondence plus indexed words; no per-instrument audio or beat alignment. · High for material design and the plan. Specific live layer attribution stays open. Affected route — E03 §9.5; music/performance and industry/material ledgers. Return GBC-AV-Q03-02.

Witness — `episodes/work/E03/critic_looper_1355_5.jpg`, `episodes/work/E03/critic_looper_1400_2.jpg`, `episodes/work/E03/diag_1080p_kickbeater_1326.0s.png`.

### E04

#### GBC-AV-E04-01 · PRESERVE

**08:48.500; §4.6, corridor encounter.** Subaru’s conduct changes across audiences; the corridor places friend and senior family witness in the same space.

**Observed.** The raw shot and independent crop show smiling Subaru holding a hand near the face of a bent-over companion; Nina is frowning beside them and Tendo is visible at the far end. The crop does not conclusively classify a private signal or identify what Tendo could see. These images precede the separate 09:02 posture instruction.

**Primary check.** Primary at 528.5 s matches the image; nearest ZIP frame 489 at 527.777 s establishes the wider group layout. Cue 169 at 09:02.120 is later.

Still and crop of the same instant count as one view, not independent witnesses. · High for spatial and audience configuration; low for assigning private meaning to the hand. Affected route — E04 §4.6; relationship/visual form ledgers. No separate return on this decision.

Witness — `episodes/work/E04/critic_q2_52850_raw.png`, `episodes/work/E04/critic_q2_52850_hand_2x.png`.

#### GBC-AV-E04-03 · STRENGTHEN

**21:47.000–21:56.833; §4.11/§7.3, cues 445–449.** The acting reveal follows the outburst. Its visual change can now be placed before the indexed reveal line.

**Observed.** The 1/6-second sequence shows Subaru bowed at 21:50.667; by about 21:50.833 she has risen, and by 21:51.000 her broad smile is visible over the drums. The indexed reveal line starts 21:53.480. The expression change therefore precedes its subtitle by roughly 2.5 seconds and does not wait for the reveal’s words in the index.

**Primary check.** Primary seeks at 1310.667, 1310.833, 1311.000 and 1313.480 s independently confirm posture, rise/smile and later close-up. Cue 447 ends 21:45.940, before the strip starts.

Timestamped 6-fps derivatives, direct MKV frames and subtitle timing. Fine timing is bounded at the sample interval; actual vocal onset/room sound not measured. · High for sampled ordering relative to cue. Visible smile is not proof that earlier anger was feigned. Affected route — E04 §4.11, §7.3, §9.4; character/voice and visual ledgers. Return GBC-AV-Q04-02.

Witness — `episodes/work/E04/critic_q5_climax_2147_2157.jpg`.

### E05

#### GBC-AV-E05-01 · STRENGTHEN

**09:09.910–10:59.520; image strip 09:26.000–09:30.833.** Nina’s response to Hina’s new stage position is personally charged and she subsequently withdraws before speaking harmfully.

**Observed.** Hina fronts the microphone. The crowd resolves into Nina, whose face aligns across a textured red field and a blue school setting. The construction of the memory is visible; how much of the venue sound travels across the edit remains unresolved.

**Primary check.** Cues 179–212; #594/10:12.320 shows Nina bent away while describing the risk of harsh words.

Independent targeted pictures and locked Japanese; no speech audition. · High on edit and spoken self-report; low on sonic continuity. Affected route — E05 §4.5; visual form/behavior Return GBC-AV-Q05-01.

Witness — `critic_e05_dd_stage_0916.png`, `highfps_02a_tdc_ink_dissolve.jpg`.

#### GBC-AV-E05-02 · PRESERVE

**14:54–15:01 versus 15:33–16:59.** The bar confrontation escalates physically before Nina acknowledges why she still chooses Momoka.

**Observed.** The short-interval strip shows a hand around a glass, Momoka’s mouth, Nina’s face taking the splash and Momoka’s arm extended across Subaru. It refines the preceding action. The later reconciliation’s Japanese delivery falls outside this strip.

**Primary check.** Cues 312–345 establish Nina’s words before and after the account. #931 frames all three from behind during her answer.

Targeted motion samples versus a later untargeted speech window. · High for visible splash; deferred for later delivery. Affected route — E05 §§4.7–4.8; relationship Return GBC-AV-Q05-02.

Witness — `highfps_03_izakaya_splash1.jpg`.

#### GBC-AV-E05-03 · STRENGTHEN

**21:17.390–21:53.** Chosen public exposure becomes a collective stage action.

**Observed.** Nina raises both hands by herself under blue light. Momoka and Subaru answer with raised hands; costume crop gives Nina’s 不登校. Distinct stills and matched text support adoption by the three; exact vocal sources across the transitional lines and audience response remain open.

**Primary check.** Cues 428–439, #1134 and #1136; #1159 shows Nina at the microphone under 全部を晒して 生きてやる.

Separate high-resolution stage stills, Japanese cues; no independent audio slice. · High for the visible public gesture and costume; moderate for the exact speech-song boundary. Affected route — E05 §4.11; music/performance and visual ledgers Return GBC-AV-Q05-03.

Witness — `frame_1080p_2124_nina_hands.png`, `frame_1080p_2128_momoka_subaru_hands.png`, `critic_e05_nina_front_2153.png`.

### E06

#### GBC-AV-E06-01 · PRESERVE

**00:23.680–00:54.790.** Tomo says vocal-synth composition makes the melody hard to sing; Rupa suggests finding a singer for it.

**Observed.** Independent images alternate Tomo’s open mouth, red illuminated bars and Rupa wearing headphones. A labeled demo window has −41.59 dBFS RMS over 11.8 seconds; two measured subwindows are −43.78 and −32.14 dBFS. Their labels and levels cannot establish whether a particular note is synthetic or sung live, or the nature of the melodic difficulty.

**Primary check.** Cues 4, 6–8; #66/00:58.684 shows Rupa at the workstation.

Targeted higher-rate frames and mixed-track metrics; Japanese authorship statements. · High on what Tomo and Rupa say; unresolved acoustically. Affected route — E06 §4.1; musical authorship Return GBC-AV-Q06-01.

Witness — `q1_strobe_strip_12fps.jpg`, `agent_b_e06_acoustics_results.json`, `critic_e06_metrics.json`.

#### GBC-AV-E06-02 · PRESERVE

**03:09.430–03:41.840.** Nina reports her throat is improving.

**Observed.** The bath strip keeps the people small, partially occluded by the pool edge and steam. Mixed bath and separate quieter-room windows differ in energy and stereo spread. Neither measures laryngeal quality or isolates Nina’s speech.

**Primary check.** Cues 46–47; #237/03:12.930 shows the bath during Nina’s reply.

Visual setting, character testimony and non-isolated numerical mix. · High for self-report; limited for audible rasp. Affected route — E06 §4.2; character/voice Return GBC-AV-Q06-02.

Witness — `q2_bath_strip_6fps.jpg`, `agent_b_e06_acoustics_results.json`.

#### GBC-AV-E06-03 · REVISE

**20:31.430–21:13.050.** Group performance precedes the proposal. The reading also characterizes separate bass and keyboard functions.

**Observed.** The 12-fps downbeat strip moves from raised drumsticks to the five in the room. A separate crop supports the keyboard and amplifier as stage equipment. Waveform transients cluster from 20:31.505 to 20:33.400; 36 s of ensemble mix measure −19.94 dBFS with substantial low-band energy. The locked MP3 independently measured −20.40 dBFS and −7.85 dB side/mid over 20:32.7–21:08.7. Visible ensemble action and spectral weight do not resolve doubling or individual parts.

**Primary check.** Count-in cue 432/#1071; bassist #1092 at 20:49.999; offer cue 440/#1119.

Targeted motion, indexed words and independently decoded mixed audio; no stems or qualified audition. · High for order and visible participation; low for specific independent lines. Affected route — E06 §§4.14–4.15; music/performance Return GBC-AV-Q06-03.

Witness — `e2_jam_downbeat_12fps.jpg`, `q3_keys_amp_macro2x2.jpg`, `agent_b_e06_acoustics_results.json`, `critic_e06_metrics.json`.

### E07

#### GBC-AV-E07-01 · PRESERVE

**12:45.600–12:53.640.** Different participants judge the rehearsal differently.

**Observed.** The reported 4.9-second rehearsal window has −23.2 dBFS RMS and 59.08% power in 20–90 Hz. The source MP3 measured −23.63 dBFS in the same interval. Chroma similarity with one late-song window is a possible lead; no measurement here grades ensemble timing.

**Primary check.** Cues 273–274 / #680–681. #681 shows stage equipment and an instrumentalist as the negative judgment is made.

Repeat measurement on locked downmix and primary dialogue; audible fault unresolved. · High for opposition of the verdicts; low for independent technical diagnosis. Affected route — E07 §4.8; music/performance Return GBC-AV-Q07-01.

Witness — `critic_e07_dsp_results.json`.

#### GBC-AV-E07-02 · DOWNGRADE

**21:17.0–21:33.7.** The E07 reading treats both corrective lines to Nina as Tomo’s speech.

**Observed.** Rupa leans in as Nina breaks off; Tomo’s mouth is open in the keyboard wide under the first corrective cue. Under the next cue the shot switches to Rupa smiling with mouth open. The rapid cut to all five continuing is clear. A single Tomo attribution, a divided turn and a reactive close-up are alternatives. The image strip ends just before the second cue and does not settle speaker identity.

**Primary check.** Directly re-viewed #1065/21:20.770, #1067/21:23.440, #1069/21:24.408; cue indexes 445–447 have empty speaker fields.

Competing implication of high-rate movement, cut and unlabelled dialogue. · High that public correction occurs; individual(s) OPEN. Affected route — E07 §4.16; character, relationship and behavioral ledgers; CP2 erratum route if attribution is propagated Return GBC-AV-Q07-02.

Witness — `highfps_c_15_rupa_stage_nudge.jpg`, `highfps_c_16_concert_opening_fireworks.jpg`.

#### GBC-AV-E07-03 · STRENGTHEN

**23:17.800–23:35.000.** Nina’s closing announcement is staged within collective listening; it establishes intent to leave preparatory school.

**Observed.** The coda strip moves through bass, keys, drums and Momoka towards Nina’s microphone as she names them. The wide stage holds after the written response, and the next-episode image is explicitly separated near 23:35. The admitted result has a 1.4202 s digital-zero interval beginning 23:34.5798. The public setting is secure; the last responder’s identity is not resolved.

**Primary check.** Cues 471–477, #1243 at 23:29.270; this does not show administrative withdrawal.

Image sequence, cue index, digits for the boundary; no performance audition. · High on setting and sequence; lower on last voice. Affected route — E07 §4.18; education/labor Return GBC-AV-Q07-03.

Witness — `critic_e07_q6_2317_coda_strip.jpg`, `highfps_c_21_pre_nep_exact_boundary.jpg`, `critic_e07_dsp_results.json`.

### E08

#### GBC-AV-E08-01 · STRENGTHEN

**05:24–05:57.** Nina invites Momoka to strike her and associates doing so with despised past aggressors.

**Observed.** The strips distinguish a real collar grab from raising a fist, Nina flinching, Momoka lowering her arm and leaving. They do not picture that threatened punch landing. This is a separate incident from the later real slap in the loading area.

**Primary check.** Cues 115–124 and #371/05:43.301; the earlier E07 preview boundary also displays the collar grab.

Higher-rate motion and Japanese utterance; cadence unresolved. · High gross action and setting; delivery ungraded. Affected route — E08 §4.6; relationship and behavior Return GBC-AV-Q08-01.

Witness — `highfps_c_04_foodcourt_collar_fist.jpg`, `highfps_c_05_foodcourt_flinch_drop.jpg`.

#### GBC-AV-E08-03 · STRENGTHEN

**18:42–19:22.8.** Nina steps into the truck’s path and Momoka reacts; the join between sound and motion matters.

**Observed.** The lighted roadway approaches Nina’s outstretched arms, then the kei-truck turns with exposed red tail lights and spray. The later horn is separately timed at 19:11.5–19:19.9 (8.4 s); its end overlaps the close view of hands at the wheel. Locked MP3 RMS there is −20.83 dBFS; the admitted horn window is roughly −20.33. This separates encounter, braking and the later sustained horn. The images do not supply speed, stopping distance or the speaker of every cry.

**Primary check.** Locked #1059/18:43.860 and cues 393–403; E1 Q2 lines 66–70, Q6 lines 206–208 and 220–224.

Higher-rate motion, blind continuous-audio observation and independently measured locked mix. · High for gross movement and continuous horn interval; calibrated speed unavailable. Affected route — E08 §4.18; behavior/visual form Return GBC-AV-Q08-03.

Witness — `highfps_c_12_keitruck_drift_stop.jpg`, `highfps_c_13_horn_hand_overlap.jpg`, `critic_e08_audio_cuts.json`, `critic_e08_blind_notes.md (restricted E1 slice)`.

#### GBC-AV-E08-04 · REVISE

**20:57.330–21:38.0.** Nina’s confession is explicit. The song helps frame the encounter and cannot stand in for a reciprocal answer from Momoka.

**Observed.** Q1 places Momoka at the wheel and Nina in the passenger seat. A hand reaches to the dashboard; Momoka cries after the turn. The immediate mix changes −24.44 to −18.29 dBFS; the locked MP3 gives −24.88 to −18.72 dBFS in the matching windows, a +6.16 dB change. Narrow low-frequency content persists into the louder cab portion before the later transition. The volume control provides a diegetic anchor for the song. Attributing the reach to Nina is strongly supported by seating/side; the emotions’ object and reciprocity remain open.

**Primary check.** #1196/20:57.330, #1200–1208 and #1213/21:22.190; E1 Q1 lines 27–28 and Q6 lines 196–197, 203, 222, 224.

Directly viewed locked frames, targeted sequence, numerical stereo mix and E1 timed observation. · High acoustic level change/visible control; moderate-to-high Nina agency, no reciprocal declaration. Affected route — E08 §§4.21,13.2; relationship and music/performance; C059–061 Return GBC-AV-Q08-04.

Witness — `highfps_c_15_stereo_knob_tears_star.jpg`, `critic_e08_audio_cuts.json`, `critic_e08_blind_notes.md (restricted E1 slice)`.

#### GBC-AV-E08-05 · STRENGTHEN

**16:02.420–16:45.080; 19:18–19:23; 20:17–20:26.** Gestures of holding, refusing and greeting need distinct actor, target and location.

**Observed.** Q1 and Q2 trace a single hand cupping Nina’s cheek, then the grab and Nina’s slap in the loading area; the cut to school is later. A separate hand arrives over Momoka’s at the wheel. At the exit Momoka uses the driver’s window, while Nina’s gesture is bilateral. Body-side specifications come from the continuous observer, with weaker verification from stills than the gross differentiation. No physical gesture supplies an agreement between them.

**Primary check.** Viewed #905, #919, #934, #936, #940, #1159 and #1165. Locked mix yields −16.55 dBFS RMS near the reported slap at 16:37.70. Q1 lines 42–45; Q2 lines 58–78; Q6 line 212.

Direct stills, mixed-track transient and E1 anatomical attribution. Impact source alone cannot identify laterality. · High for locations/contact and separate events; provisional for exact chirality where hands cross. Affected route — E08 §§4.15–4.19; visual and relationship ledgers No separate return on this decision.

Witness — `critic_e08_blind_notes.md (restricted E1 slice)`, `critic_e08_audio_cuts.json`, `highfps_c_13_horn_hand_overlap.jpg`.

#### GBC-AV-E08-10 · PRESERVE

**01:23.5–01:49.5; 06:05.5–07:20.5; 13:26.5–14:31.5; 21:38.5–22:09.5; 23:35.164–.205.** Visual boundaries need differentiation between hard cuts, moving light and fades.

**Observed.** Q7’s inspected hard-cut counts are 9, 17, 16 and 11 across the four named windows. The automated result reports 20, 58, 21 and 11 candidates, respectively. These quantities answer different questions; only the last pair has literal numerical agreement. E1 marks the headlight pass and stage flare as lighting, notes explicit credits do not assign instrumental roles, and observes no visible backstage pass check in the selected transition. The 23:35 cut takes place within a quiet audio interval (source MP3 is digitally silent 23:34.7–23:35.4). Prior authorization offscreen or the status of three unnamed credits cannot be inferred.

**Primary check.** Archive shots #905/16:06.674 display backstage access; #1225/21:42.343 lies within the coda. E1 Q6 lines 226–227, Q7 lines 234–237, 244,246; machine candidates in q7_shot_cuts.

1-fps survey supplemented by specific high-rate inspection; algorithmic candidates are not final hard cuts. · High distinction among event types; observer’s full manual counts separately attributed, not independently reproduced. Affected route — E08 §§4.1,4.7,4.14,4.22; visual form and credits No separate return on this decision.

Witness — `critic_e08_blind_notes.md (restricted E1 slice)`, `critic_e08_audio_cuts.json`.

### E09

#### GBC-AV-E09-01 · OPEN

**12:20.93–12:22.26.** No speaker is established for the title card.

**Observed.** E1 hears a single restrained voice. Two character voices remain close acoustic matches.

**Primary check.** The local card at 12:21.5 shows instruments. The 12:21.0–12:22.1 primary signal has identical stereo channels, −20.84 dBFS RMS and −6.38 dBFS peak. Mono does not identify a performer.

Visual, independent listening report and primary PCM · High for dry centered signal; low for attribution Affected route — E09 §4.11; character/voice Return GBC-AV-Q09-03.

Witness — `episodes/work/E09/critic_e09_blind_notes.md L25–42`.

#### GBC-AV-E09-02 · STRENGTHEN

**20:10.5, 20:12.71, 20:39–20:40.1.** Nina’s practice and finger pain are bodily evidence of continued technical work.

**Observed.** An early close view shows bare fingers. A medium shot immediately after the wince and a later close view show a beige wrap on the fretting hand.

**Primary check.** Direct primary frames show bare fingers at 20:10.5, Nina releasing the neck at 20:12.71, and a colored dressing at 20:40.1. An application of the dressing is not shown.

Selected full frame and crop, direct time-separated frames · High for pictured discontinuity; when applied remains unknown Affected route — E09 §4.19, §19; music/performance and visual form No separate return on this decision.

Witness — `episodes/work/E09/agent_a_crops/p3_nina_2012_712_full.png`, `episodes/work/E09/agent_a_crops/p3_nina_2012_712_hand_zoom.png`, `episodes/work/E09/critic_e09_blind_notes.md L54–60`.

#### GBC-AV-E09-03 · STRENGTHEN

**08:28.4–08:32.0.** The snake and damaged bathroom door have material effects within a comic group episode.

**Observed.** The six-samples-per-second strip places a foot raised behind a falling door. E1 distinguishes the larger movement from an edit.

**Primary check.** At 08:28.4 Rupa holds the beer; at 08:29.1 she turns, a foot is over Nina at 08:30.1, and the reverse at 08:31.5–08:32.0 reveals Rupa and the displaced door. The shot change and kick are separate observations.

Direct video stills plus selected high-rate strip · High for who kicked the door; soundtrack impact onset unchecked Affected route — E09 §4.6; visual and behavior No separate return on this decision.

Witness — `episodes/work/E09/agent_a_crops/rupa_kick_6fps_grid.png`, `episodes/work/E09/critic_e09_blind_notes.md L177`.

#### GBC-AV-E09-04 · PRESERVE

**00:55.7–00:57.5; 13:15.378.** The old band’s departing voices belong to a represented history. Current messages serve a different group.

**Observed.** E1 describes a former group’s phone chat with named exits. The selected current chat includes Nina’s name and a thank-you sticker.

**Primary check.** Primary 00:55.7 shows two grey chat-withdrawal notices and names. Locked bundle frame 000725 is the present group chat. Neither phone establishes the individual drummer/guitarist mapping.

Primary screens and selected crop · High for two distinct screens; former players’ instrument assignments open Affected route — E09 §§4.2, 4.12; relationship No separate return on this decision.

Witness — `episodes/work/E09/agent_a_crops/toge_chat_zoom.png`, `episodes/work/E09/critic_e09_blind_notes.md L85–89, L97, L201–202`.

#### GBC-AV-E09-05 · STRENGTHEN

**17:24.0–17:27.4.** Loss of contact with Tomo’s parents makes acquiring housing materially difficult.

**Observed.** The legal form uses 保証, while the dialogue transcription writes the homophone 保障. The paper is a rental guarantor consent form.

**Primary check.** Video 17:24.5–17:25.3 shows the upside-down form seen right-side up in the crop. Locked Japanese cue 355 at 17:26.030 reads 保障人？. E1’s 329 uses its own numbering. A signed guarantor identity or completed lease is not legible here.

Object text, Japanese cue, direct primary frame · High for depicted document category; no signature claim Affected route — E09 §§4.15, 17; industry/labor and character/voice No separate return on this decision.

Witness — `episodes/work/E09/agent_a_crops/guarantor_doc_rot180.png`, `episodes/work/E09/critic_e09_blind_notes.md L70, L122`.

#### GBC-AV-E09-06 · STRENGTHEN

**09:48–10:16.** Tuning is part of Nina’s practical work and the others can evaluate a particular result.

**Observed.** E1 tracks an upward tuning change with the last note slightly below equal-tempered B3.

**Primary check.** Local 48 kHz mixed-track spectral maxima near 245.18 and 245.73 Hz occur in the turning window; the final plucks give 245.91–246.28 Hz, below 246.94 Hz. One intermediate window has weak target-band signal, so the local checks cannot confirm every point on a monotonic curve.

Reported fine pitch and direct short-window spectral measurements · High for slightly flat final plucks; moderate for the detailed tuning trajectory Affected route — E09 §§4.7, 19; music/performance No separate return on this decision.

Witness — `episodes/work/E09/critic_e09_blind_notes.md L130–134`.

#### GBC-AV-E09-07 · STRENGTHEN

**12:03.4–12:09.** The severe rehearsal verdict disrupts the interaction.

**Observed.** E1 hears a marked drop after the shout, before insects and other background details come forward.

**Primary check.** Independent 12:04.1–12:08.9 integrated stereo RMS is −54.19 dBFS. This is not bit-zero silence. A reported mean of shorter dB windows need not equal the single interval’s energy-based RMS.

Independent auditory report and primary digital measurement · High for the low-level interval; source of each sound not isolated Affected route — E09 §§4.10–11; behavior and music/performance No separate return on this decision.

Witness — `episodes/work/E09/critic_e09_blind_notes.md L164`.

#### GBC-AV-E09-08 · PRESERVE

**05:50–06:24.** Tomo withdraws, then objects when Rupa leaves her alone.

**Observed.** E1 reports six cuts missing from the retained shot-change tags, including a transition between doorway geography and closer coverage.

**Primary check.** Direct 05:58.0 shows Rupa in the doorway across the room from Tomo. 06:02.0 isolates Tomo near the bed. These establish a changed framing. The exact count of eight cuts is reported by E1 and is not required to identify the separation.

Reported frame-accurate edit audit and sampled primary · High for spatial staging; count reported independently Affected route — E09 §4.5; visual form No separate return on this decision.

Witness — `episodes/work/E09/critic_e09_blind_notes.md L176`.

### E10

#### GBC-AV-E10-01 · STRENGTHEN

**00:42–00:46.5; 20:02.8–20:04.8.** Miura identifies herself professionally; Nina’s parting gesture makes a public departure distinct from the earlier avoidance.

**Observed.** The card names Miura Shiomi and Golden Archer. Nina later extends both little fingers toward her father.

**Primary check.** Local 00:45.4 bears the same card; 20:03.4 shows the two raised arms, both little fingers and the band on Nina’s left wrist. The image supports gesture and affiliation, without settling every origin or private meaning.

Selected crops and direct primary images · High for legible card and bilateral gesture Affected route — E10 §§4.1, 4.25; industry, visual and relationship No separate return on this decision.

Witness — `episodes/work/E10/a_pass1_checks/crop_bizcard_full_0045.png`, `episodes/work/E10/a_pass1_checks/pinky_2002/f07.png`, `episodes/work/E10/critic_e10_blind_notes.md L23–25, L39–42`.

#### GBC-AV-E10-02 · STRENGTHEN

**13:16; 15:14.3.** The school’s apology and Nina’s earlier pressure to apologize occupy different positions of authority.

**Observed.** Two paper objects carry distinct headings, a stamped, typed 謝罪文 and a ruled handwritten 反省文 page.

**Primary check.** At 13:16 the primary shows the typed school document addressed to the family. At 15:14.3 it shows a writing hand, pen and almost blank reflection sheet. These cannot be treated as two copies of one author’s apology.

Selected written-detail crops and direct primary images · High for two documents; distinct imagery does not establish completed submission by Nina Affected route — E10 §§4.15–18; character/voice, institutional material No separate return on this decision.

Witness — `episodes/work/E10/a_pass1_checks/crop_shazaibun_1316.png`, `episodes/work/E10/a_pass1_checks/crop_hanseibun_1513.png`.

#### GBC-AV-E10-03 · REVISE

**20:30.2–20:33.** The reading describes completion of the writing but says that completed lyric text or process is unavailable.

**Observed.** A phone in the carriage carries the song title and several stanzas; the subsequent close view clips some lines.

**Primary check.** At 20:30.2 the local primary shows the writing app on the tray. At 20:33 the closer view and selected crop allow the title 空白とカタルシス and several lines to be read. The 12:55 in E1 is a phone clock. This supplies text to compare without establishing precisely when each line was written or final-stage identity. Preserve the narrower caution that E10 supplies no authenticated complete final lyric version or line-by-line composition history.

Selected crop, wider direct primary and onscreen text · High for visible draft; final editorial identity and the source of each line unverified Affected route — E10 §§1, 4.25, 4.27, terminal claim 10; music/authorship No separate return on this decision.

Witness — `episodes/work/E10/a_pass1_checks/crop_lyrics_2033.png`, `episodes/work/E10/critic_e10_blind_notes.md L106–107`.

#### GBC-AV-E10-06 · STRENGTHEN

**18:03–18:36.5; 20:56.5–21:05.6; 23:12.2.** The father listens to Momoka’s old song and this changes what Nina can say to him.

**Observed.** E1 distinguishes a recorded Diamond Dust rendition in the house from an Iseri Nina rendition heard at Kawasaki. The credits use the same song title for two performers.

**Primary check.** The local video shows the father holding the player at 18:36.5, Nina at the plaza at 21:00.5, and separate Diamond Dust / Iseri Nina credits at 23:12.2. Primary 18:03.4–18:08.4 peaks at −11.21 dBFS; the plaza’s 20:57–20:59 is −39.85 dBFS RMS. Credits and scenes establish two uses. Exact humming and door-filter quality rely on the E1 listening report.

Credits, direct frames and mix; independent listening · High for the two credited versions and contexts; moderate for acoustic descriptions Affected route — E10 §§4.22, 4.26; music and relationship No separate return on this decision.

Witness — `episodes/work/E10/critic_e10_blind_notes.md L103, L154–156`.

#### GBC-AV-E10-07 · PRESERVE

**07:15–07:36; 21:28.94 and 21:32.91.** Suzune turns Nina’s anti-evasion language back toward her; Momoka’s rough address remains partner-conditioned.

**Observed.** E1 hears regional forms from Suzune, and distinguishes Momoka’s fragmented utterance from a single later shout.

**Primary check.** The Japanese text for the phone turn uses regional forms. The paired dialogue fragments are separated in the episode cue index; the primary 21:32.9 frame shows Momoka and the second syllable. Indexed spacing is firmer than a claim about exact intonation.

Japanese source cues, primary image, independent listening · High for text and segmentation; delivery remains reported Affected route — E10 §§4.9, 4.26, 5.7; character/voice No separate return on this decision.

Witness — `episodes/work/E10/critic_e10_blind_notes.md L204, L210`.

#### GBC-AV-E10-08 · REJECT

**05:35–05:57; 08:11–08:44.** E10 §4.7 identifies the parent visiting the workplace as the father and uses the scene to infer Nina’s response to paternal presence.

**Observed.** E1 identifies the shop visitor as Yasue, the mother, and places Tomo alongside Rupa during both the shop exchange and the later bereavement disclosure.

**Primary check.** Primary 05:45.5 and 05:51.7/05:57 place the mother across the counter from Rupa and Tomo. The father is seen in a separate Kawasaki exterior at 06:06.3–06:11.7; Nina’s speech opening お父… independently supports his identity. At 08:21 and 08:32 Tomo remains at work during Rupa’s disclosure. Nina’s fear of meeting her father can be grounded in the exterior and later encounters, while the shop scene concerns her mother.

Independent visual observation and directly matched multiple frames · High for identity, staging and removal of the paternal trigger as an inference from the shop Affected route — E10 §4.7 and character/relationship rules using it; mutable ledgers No separate return on this decision.

Witness — `episodes/work/E10/critic_e10_blind_notes.md L227–228`.

### E11

#### GBC-AV-E11-01 · STRENGTHEN

**15:39.8–15:44; 18:18.4.** The group adopts a raised-pinky practice and treats Hina as an active musical rival.

**Observed.** E1 identifies Hina’s raised right little finger, cyan nails and subsequent left-eye wink. It separately describes the five’s huddle.

**Primary check.** The 15:39.8 crop catches the curled hand, not the final endpoint. Local 15:40.5 establishes the extended outer finger and 15:44 the wink. At 18:18.4 the five meet with raised little fingers. These episodes of gesturing do not establish Hina’s motive or reconciliation.

Selected crop plus timed decodes of gesture endpoints · High for the pictured gesture and eye; rhetorical intent remains open Affected route — E11 §§4.12–13, 4.16; visual form/relationships No separate return on this decision.

Witness — `episodes/work/E11/agent_a_tmp/hina_finger_15398.png`, `episodes/work/E11/critic_e11_blind_notes.md L50–53, L57–61`.

#### GBC-AV-E11-02 · PRESERVE

**14:26.2; 16:31.8–16:45.5.** Rival and home performances are embodied technical tasks; soundcheck is practical work.

**Observed.** E1 identifies the rival singer’s guitar and separates Subaru’s kit and vocal boom from other equipment.

**Primary check.** Local 14:26.2 shows Hina performing on guitar at the microphone. 16:31.8 and 16:35 show kit and separate pedals; 16:45.5 shows Subaru at a microphone. The instrument context is seen directly. The precise brand/model and microphone signal paths need closer images for independent endorsement.

Primary instruments and stage fixtures, with independently reported detail · High for rigs and workstations; lower for model and assignment of isolated sound Affected route — E11 §§4.13–14; music/performance No separate return on this decision.

Witness — `episodes/work/E11/critic_e11_blind_notes.md L86–93`.

#### GBC-AV-E11-03 · REVISE

**06:13.5; 11:33.68; 23:04.2–23:04.42.** Subaru tells Nina she wrote to her grandmother; the grandmother’s settled response to the band remains open.

**Observed.** The visible inbox message runs from Tendo to Subaru and mentions an audition. A late crowd insert places Tendo by a sunglasses-wearing attendee identified as Miura.

**Primary check.** Primary 06:13.5 shows the actual incoming sender, addressee and audition wording. Cue 253 at 11:33.680 is Subaru’s separate report of her own outbound mail. The figures occur in source images at 23:04.2–23:04.42; no statement of approval is attached to that cut.

Written prop, spoken-text index and matching visual witnesses · High for mail directions and visible witness; attendance cannot settle family consent Affected route — E11 §§4.6, 4.10, 4.21; Subaru voice and relationships No separate return on this decision.

Witness — `episodes/work/E11/agent_a_tmp/crop_email_tendo.png`, `episodes/work/E11/agent_a_tmp/tendo_miura_23042.png`, `episodes/work/E11/critic_e11_blind_notes.md L109, L125`.

#### GBC-AV-E11-04 · STRENGTHEN

**22:08.5.** E11 treats the burning certificate as potentially relevant to Tomo’s musical history while withholding a total account of her family.

**Observed.** E1 identifies an award naming Tomo, a student category and a gold prize.

**Primary check.** Direct primary 22:08.5 and the enlargement show a burning certificate. Student division and gold prize are readable, with parts of the name hidden by flame in this specific frame. The shot cannot identify who set it on fire, the whole institution, or a causal family history.

Primary insert and cropped printed text · High for the depicted award; its destruction history remains open Affected route — E11 §§4.21, 14, character/relationship No separate return on this decision.

Witness — `episodes/work/E11/agent_a_tmp/tomo_cert_22085.png`, `episodes/work/E11/critic_e11_blind_notes.md L117`.

#### GBC-AV-E11-06 · OPEN

**07:04.37 and 07:16.72.** Rupa distinguishes a living estranged person from the irrevocable loss of the dead, then thanks Tomo.

**Observed.** E1 hears the particle は omitted in the first phrase and a plain ありがとう in the second before polite register resumes.

**Primary check.** Original dialogue-index cues 144 and 148 and matching frames show 今は生きてる and ありがとう. The plain thanks agrees in both accounts. Direct images and transcription cannot adjudicate an unvoiced particle; E1’s own cue ordinals differ from the locked index.

Japanese cue and primary caption; independent listening for the disputed particle · High for thanks and bounded scene meaning; exact audible particle remains unresolved Affected route — E11 §4.7; character/voice, Rupa–Tomo Return GBC-AV-Q11-04.

Witness — `episodes/work/E11/critic_e11_blind_notes.md L152–153`.

#### GBC-AV-E11-07 · STRENGTHEN

**16:31.8; 16:43.547; 20:23.6; 22:19.3.** E11 places technical soundcheck beside two high-impact festival performances.

**Observed.** E1 ranks a one-second Subaru soundcheck window above a full-band opening and a late vocal/performance passage by mixed stereo RMS.

**Primary check.** Identical primary windows give −13.79, −14.71 and −14.20 dBFS at 16:31.8, 20:23.6 and 22:19.3. A 0.1 s window around 16:43.547 peaks at −0.33 dBFS. This compares three exact windows; it does not identify isolated instrument or voice loudness.

Direct stereo PCM and source-aligned kit image · High for window values; exhaustive episode-wide rank is the observer’s Affected route — E11 §§2.2, 4.14, 4.21; music/performance No separate return on this decision.

Witness — `episodes/work/E11/critic_e11_blind_notes.md L187–194`.

#### GBC-AV-E11-08 · PRESERVE

**20:15.5.** Within the story Nina supplies lyrics, Momoka and colleagues make other decisions, and all perform the song.

**Observed.** The on-screen broadcast insert-song credit lists a performer and production writing/arranging credits in different fields.

**Primary check.** At 20:15.5 the primary wide includes the same credit; the crop reads Togenashi Togeari, 空白とカタルシス, with separate production lyricist/composer/arranger lines. These are production credits. Fictional authorship has its own dialogue and writing witnesses.

Direct paratext, with V2 source-dialogue and E10 writing evidence · High for credited categories; the production names cannot override story-level authorship Affected route — E11 §§4.17–4.21, C064; music/authorship No separate return on this decision.

Witness — `episodes/work/E11/agent_a_tmp/toge_song_cred_20155.png`.

#### GBC-AV-E11-09 · STRENGTHEN

**22:40.35–22:44.0.** E11 treats the concert as deliberately constructed and associates the live performance with other histories.

**Observed.** E1’s 24 fps audit finds a cut to the orbiting stage view at 22:40.526 and attributes five later automatic tags to strobes or a moving camera.

**Primary check.** Direct 22:40.35 shows a single performer and 22:40.60 shows the open stage. 22:41.0, 22:42.0 and 22:43.8 change angle around that same configuration. A smooth orbit is plausible. The exact number of subsequent cuts is E1’s sampled diagnostic and does not determine whose memory appears elsewhere.

Primary sampled frame progression and reported 106-frame audit · High for change into the stage view; moderate for all internal boundaries Affected route — E11 §4.21; visual form No separate return on this decision.

Witness — `episodes/work/E11/critic_e11_blind_notes.md L212–215`.

### E12

#### GBC-AV-E12-01 · PRESERVE

**03:32 · shop / #234.** The instrument displays a price of ¥79,200.

**Observed.** The separately selected price placard reads ¥79,200 and identifies the instrument as a Tribute ASAT Classic.

**Primary check.** The identical figure is legible in the locked price shot. Neither witness shows a completed purchase.

sign text / single crop · High for price. Affected route — E12 material world; industry ledger No separate return on this decision.

Witness — `crop_0332_guitar_price.jpg`.

#### GBC-AV-E12-02 · PRESERVE

**08:48–08:50 · studio sheet / #500–502.** The musicians are given a written song draft in the studio.

**Observed.** The sheet carries the title 運命の華 and lines of lyrics. A hand holds it before the reader.

**Primary check.** E12 retained #501 and cues 216–224 connect the tentative lyrics to Momoka. A cropped hand cannot independently supply the author credit.

written text / photographed prop · High for the sheet; process attribution remains text-dependent. Affected route — E12 authorship; music ledger No separate return on this decision.

Witness — `crop_0849_lyric_complete.jpg`.

#### GBC-AV-E12-03 · PRESERVE

**11:56 · event proposal.** The proposal identifies Club Citta and a 1,300-person figure.

**Observed.** The screen labels the rival acts, the location and 動員人数 1,300人.

**Primary check.** The phone is a proposal marked 仮. This number precedes the event, and measures a different quantity from the final 103-play screen.

sign text / still · High; no figure for eventual turnstile attendance. Affected route — E12 and CP4; industry ledger No separate return on this decision.

Witness — `crop_1156_proposal_screen.jpg`.

#### GBC-AV-E12-04 · STRENGTHEN

**19:28.750–19:31.500 · shrine / #1004, 1013–1014.** The two-person gesture becomes a five-person promise. Exact positions between retained frames had remained open.

**Observed.** Two independently extracted stills separate two approaching little fingers from a later group of hands.

**Primary check.** An 8-fps matched-encode check shows a gap at 19:30.375, tip contact by 19:30.500, another hand by 19:30.875 and the larger grouping by 19:31.375. The audible phrase boundary and speaker remain unverified.

sampled motion / still pair / primary frame series · High for order within 125 ms samples; no assertion of voiced sync. Affected route — E12 shrine, CP4 P07/P15; visual and relationship ledgers Return GBC-AV-Q12-06.

Witness — `crop_1930_two_pinkies_1080p.jpg`, `crop_1931_five_pinkies_1080p.jpg`.

#### GBC-AV-E12-05 · PRESERVE

**22:01 · Nina’s release check / #1132, 1136.** The phone reports 103 plays at one depicted check.

**Observed.** The crop reads 曲名 運命の華 and 再生回数 103.

**Primary check.** The locked phone image agrees on title, measure and count. It cannot identify distinct people, elapsed hours or eventual reception.

screen text / still · High for unit and value. Affected route — E12 closing counter; industry and revision ledgers Return GBC-AV-Q12-07.

Witness — `crop_2201_plays_103_1080p.jpg`.

### E13

#### GBC-AV-E13-01 · STRENGTHEN

**06:26 · meeting / cues 136–142.** The two meet over food they associate with earlier trips home from school.

**Observed.** A cup bearing the Hill Valley name is filled with pink popcorn.

**Primary check.** Cue 140 locates the habit in returning from school. The depicted snack is now identifiable. Sharing a food does not show reconciliation.

source crop, object and indexed speech · High for the pictured food. Affected route — E13 Hina meeting; relationship ledger No separate return on this decision.

Witness — `b3_hillvalley_cup_06260.png`.

#### GBC-AV-E13-02 · PRESERVE

**17:48–17:56 · dressing room.** A trail of provocations draws Nina through the dressing room.

**Observed.** Selected pictures show Nina looking ahead, looking upward and leaning forward while others remain in the room.

**Primary check.** Locked frames 1064, 1068 and 1076 supply the notes and arrows. The selected expressions alone neither identify their author nor explain Hina’s motives.

three discrete poses / written signs · High for sequence and addressee, motive remains inferential. Affected route — E13 backstage; relationship and behavioral ledgers Return GBC-AV-Q13-06.

Witness — `b3_prank_wb_17480.png`, `b3_prank_ceil_17510.png`, `b3_prank_door_17555.png`.

#### GBC-AV-E13-03 · PRESERVE

**19:55.5 and 21:52 · shared listening and balcony.** Nina realizes that Hina also heard the old song; Diamond Dust attends the show.

**Observed.** Two uniformed girls share earphones from one device. Four members of the rival band appear listening/watching from the balcony.

**Primary check.** Frames 1176–1178 and 1317–1325 corroborate the two distinct times. Hina does not affirm Nina’s account aloud in either image.

depicted listening and presence / stills · High for bodies and device; no reciprocal forgiveness or audible mic status established. Affected route — E13 MC; relationship and voice ledgers Return GBC-AV-Q13-07.

Witness — `b4_flashback_greenfloor_19555.png`, `b4_dd_balcony_21520.png`.

#### GBC-AV-E13-04 · REVISE

**22:10.250–22:15.250 · closing thanks to title.** E13 used the 22:15.084 title card to separate the performance from the illustrated ED.

**Observed.** The sampled strip already shows a white title over the colored stage by 22:11.250. The red-on-white title follows.

**Primary check.** A 4-fps primary recheck shows the logo entering over the stage around 22:10.250–22:10.500. The stage darkens under it. The change to the white field falls between 22:15.000 and 22:15.250, consistent with bundle #1346.

editing / time-labelled samples and matched source · High for the two distinct visual events; onset not timed to a single source frame. Affected route — E13 ED table and CP4 formal boundary, visual and revision ledgers Return GBC-AV-Q13-08.

Witness — `b4_title_transition_2211_2216_strip.jpg`.

#### GBC-AV-E13-05 · STRENGTHEN

**23:36–23:37 · final music player.** The ending shows the band’s own song on a player with a five-member portrait.

**Observed.** The selected closing image shows the five together on a handset with playback controls and a red cord.

**Primary check.** The full-size primary matched-encode sample at 23:36 reads 誰にもなれない私だから / トゲナシトゲアリ. The earlier player has 空の箱 / Diamond Dust. Neither interface establishes a commercial release date.

graphic design / still and matched title read · High for the visible player; actual future event OPEN. Affected route — E13 C084, music and visual ledgers Return GBC-AV-Q13-09.

Witness — `b5_cred_2337_prod_end.png`.

#### GBC-AV-E13-06 · STRENGTHEN

**19:53.35–20:01.61 and 21:44.00–22:12.00.** The Hina recollection includes low mixed-track levels; the collective close is louder than the preceding performance passage.

**Observed.** The numeric file contains 14,202 RMS samples at 0.1-second hops. Median reported levels for the recollection, 21:44–22:05.73 performance passage and 22:05.73–22:12 thanks are −35.29, −18.14 and −15.56 dB respectively.

**Primary check.** I independently decoded the locked MP3 at 8 kHz mono. Across jointly non-floor samples, 1-second forward-window levels correlate r=.995 with the external profile, compared with .611 for 0.1-second windows. A −2.30 dB median cross-pipeline offset prevents treating the absolute numeric scales as identical.

Program-mix acoustic measurement. Speaker, venue amplification and instruments are not isolated. · High for relative energy and time structure; underlying voice identity and sound perspective remain OPEN. Affected route — E13 MC and final set; character/voice and music ledgers. Return GBC-AV-Q13-07.

Witness — `ep13_rms_01hop.npz`.

## New observations proposed by the evidence review

#### GBC-AV-E03-03 · NEW (accepted)

**18:44.600; §4.10, cues 369–372.** New local observation of the hand motif at the food counter.

**Observed.** Nina holds both hands up with one outer finger extended on each while seated between her bandmates; Subaru’s open hand is lower in front. The pose appears in a comic exchange following commentary about Nina’s throat. It gives a visible comparison with E02; a shared private meaning with Subaru does not follow.

**Primary check.** Exact primary seek 1124.6 s confirms hand configuration. The nearest retained primary image, frame 874 at 1125.958 s, has already cut to Momoka; the index alone cannot recover the pose.

Matched stills on the episode clock, no inference about the voice from an image. · High for bilateral gesture; significance and whether it repeats an established private meaning remain inferential. Affected route — E03 §4.10; visual form ledger as a bounded additional pose. No separate return on this decision.

Witness — `episodes/work/E03/critic_yoshinoya_1124.6.png`.

#### GBC-AV-E04-02 · NEW (accepted)

**12:28–12:33; boundary §§4.7–4.8.** Additional visual observation at the transition after the acting exercise.

**Observed.** The selected strip follows Subaru’s tightened brow and lowered/closed eyes into a side-profile composition with a dark doubled face/reflection. Its interval is after the etude proper; it cannot establish that the earlier rough aside was publicly heard.

**Primary check.** Primary at 748.0, 751.5 and 753.0 s verifies frontal frown, closed eyes/profile and dark reflection respectively. The label etude describes a diagnostic topic; §4.8 begins at 12:21.

Sample sequence, source comparison. Transport/location or interior monologue alone cannot be inferred from the reflected face. · High for visible transition; no access here to the 11:25 phone/speech channel. Affected route — E04 §§4.7–4.8, visual ledger. Return GBC-AV-Q04-01.

Witness — `episodes/work/E04/critic_q3_etude_1228_1233.jpg`.

#### GBC-AV-E08-06 · NEW (accepted)

**12:10.969–12:12.277.** The eyecatch is a brief stylized vocal item with title and musical setup.

**Observed.** Q3/Q5 report the standard title pronunciation; the ZIP’s selected ASS reads カールズ while the pictured title begins ガールズ. E1 further reports a two-voice unison and assigns the voices to Nina and Momoka. The two pictured objects qualify as visual correspondences, insufficient by themselves to identify singers. The independent −22.25 and source MP3 −22.70 dBFS RMS and −39.0 dB side/mid substantiate the narrow 1.308-second item, not headcount.

**Primary check.** #669 at 12:10.970; cue 259 (blind note’s track-specific 233); Q3 lines 87, 90–96 and Q5 line 152.

Printed title plus captions and numeric audio; E1 auditory attribution is single-witness. · High written discrepancy and span; specific pair OPEN. Affected route — E08 source/text accuracy and music/performance No separate return on this decision.

Witness — `critic_e08_blind_notes.md (restricted E1 slice)`, `critic_e08_audio_cuts.json`.

#### GBC-AV-E08-07 · NEW (accepted)

**08:37.800; 09:34.616; 17:07.151; 21:42.343–21:46.** Institutional and interpersonal claims can use visible documents independently of dialogue.

**Observed.** Q4's social profile figures are directly readable at #487: 383 following and 27,851 followers. The bookstore, school broadcast room, group chat and phone case are distinct images; #1229 corroborates a bright lizard/foliage pattern. Exact book editions, the small room-indicator text and a recurring keyboard-decal interpretation need stronger close views. A profile counter locates an account, not tickets sold.

**Primary check.** #487, #536, #970, #1225 and #1229 re-viewed in original ZIP; E1 Q4 lines 113, 130, 132, 136, 138.

Legible locked prop versus separate E1 observation; careful resolution limits. · High social counts and visible chat; moderate identity/design echoes. Affected route — E08 §§4.8–4.9,4.22; industry and visual form No separate return on this decision.

Witness — `critic_e08_blind_notes.md (restricted E1 slice)`.

#### GBC-AV-E08-08 · NEW (accepted)

**00:53.920; 05:30.240; 08:37.800; 09:37.5–09:46; 16:15.960; 18:27.220–18:33.640; 21:52.720.** Japanese ASS is an indexed witness, and phonetic or omitted words require a separate audio basis.

**Observed.** Q5 reports sungoi rather than the normalized first line, presents the unusual apology form as a caption issue, distinguishes watashira, reports spoken A-minor/F/G and a groan in a cue gap, hears the group name correctly despite an ASS バスト spelling, and distinguishes Nina saying Hina from an offscreen Momokan. The late Rupa line is reported as spoken with a chuckle over music. The matching captions confirm the lexical mismatches and cue gap, not every sound, accent or offscreen attribution.

**Primary check.** ZIP cues 22,115,180,201–202 (no text for the proposed chord names), 259, #912 at 16:15.960, 386,391,451. Q5 lines 145–158,170,179. Line/cue IDs in the two indexes differ; aligned by time.

E1 continuous listening, structured Japanese and on-screen text; no direct independent listening by Codex. · High missing/variant caption material; medium E1’s positive heard reports, exact chord sequence not independently recovered. Affected route — E08 source accuracy, character/voice and music authorship Return GBC-AV-Q08-05.

Witness — `critic_e08_blind_notes.md (restricted E1 slice)`.

#### GBC-AV-E08-09 · NEW (accepted)

**16:53–17:15.** School flashback transitions from exposed voice to a broad instrumental presentation of 空の箱.

**Observed.** Q6 reports voice with a quieter office and louder corridor, abrupt full-band entry, then sustained stereo. Original MP3 confirms −34.94 dBFS/−25.00 dB side/mid (16:53–16:59), −25.11/−20.98 (16:59–17:04), then −20.42/−7.25 (17:06–17:09). The image places Nina in the broadcast room. The large stereo expansion cannot establish that every sounded instrument is available through the school’s on-screen loudspeaker. E1’s M2/M3 grades encode interpretation and are excluded.

**Primary check.** Cues 355–360, #952 and #970. E1 Q6 lines 190–193 and 201–203. Time-domain measurements independently agree after MP3 compression.

Indexed lyrics, direct frame, numeric measurement and admitted observer’s listening. · High acoustic shift and place; source assignment across the transition partly open. Affected route — E08 §13.2; visual/music performance Return GBC-AV-Q08-06.

Witness — `critic_e08_blind_notes.md (restricted E1 slice)`, `critic_e08_audio_cuts.json`.

#### GBC-AV-E08-11 · NEW (disputed)

**12:33–12:38; 12:10.969–12:12.277.** An instrumental timbre or specific pair of voices should only enter a motif or cast claim with appropriate support.

**Observed.** Q6 line 216 attributes five 42.2 Hz attacks to low piano. Q3 line 93 additionally claims the title-call unison is precisely Nina and Momoka. The admitted hearing is positive, but a low fundamental and pictured instruments do not independently classify a sound, count voices or identify singers. These proposed exact identifications remain separate from the accepted title spelling and measured timing.

**Primary check.** #669 shows the title over an instrument image; cue 259 locates the narrow title mix. The locked MP3 reproduces its low side/mid signal, which cannot count voices. No separate original stems or labeled speaker line exists in these sources.

Single-witness auditory source attribution; numerical measurements cannot separate contributing sources. · Moderate for the source observer’s hearing; inadequate corroboration for exact personnel or recurrence in synthesis. Affected route — E08 music/performance; keep provisional until a future claim depends on those identifications. Return GBC-AV-Q08-07.

Witness — `critic_e08_blind_notes.md (restricted E1 slice)`, `critic_e08_audio_cuts.json`.

#### GBC-AV-E10-04 · NEW (accepted)

**19:07–19:14.** At the railway-side farewell Nina begins to address her father again.

**Observed.** E1 hears two separated low thuds, resembling a heartbeat; it differentiates them from a continuous recurring musical pattern.

**Primary check.** Local 19:09.1 places both people in the railway-side space. A 30–130 Hz scan gives separated maxima at 19:08.425 and 19:08.900. Two sound events and their spacing are established. The physical or psychological source remains unshown.

Independent listening report, direct frame and PCM spectra · High for two impulses; moderate for the heartbeat likeness Affected route — E10 §§4.24–25; visual form/music No separate return on this decision.

Witness — `episodes/work/E10/critic_e10_blind_notes.md L133`.

#### GBC-AV-E10-05 · NEW (accepted)

**10:26–10:30.** The title-card transition interrupts the family section.

**Observed.** E1 reports exact silent intervals before and after the title call against the station platform.

**Primary check.** At 10:26.4 and 10:27.5 the primary shows the same platform and track number. Both channels are zero throughout the selected 10:26.3–10:27.0 and 10:28.42–10:29.02 windows. The intervening 10:27.13–10:28.13 has −23.48 dBFS RMS and equal channels. No performer identification follows.

Direct frames and exact stereo samples · High for sampled silent/non-silent contrast Affected route — E10 §§2, 4.13; visual/music No separate return on this decision.

Witness — `episodes/work/E10/critic_e10_blind_notes.md L140–146`.

#### GBC-AV-E10-09 · NEW (accepted)

**00:53.845–00:56.848.** The opening introduces an agency encounter beside unequal responses among the musicians.

**Observed.** E1 reports a half-second Tomo insert missed at 1 fps, followed by quick cuts among members.

**Primary check.** Direct calibrated frames at 00:54.05, 00:54.53, 00:54.95 and 00:55.8 show Tomo, Momoka’s eye, Rupa amid the crowds, and Nina. Individual timing supports the distribution of reactions but does not isolate internal motives.

Source-aligned subsecond primary stills and E1 edit report · High for frame sequence; exact first/last PTS from E1 Affected route — E10 §§4.1–2; visual form No separate return on this decision.

Witness — `episodes/work/E10/critic_e10_blind_notes.md L223`.

#### GBC-AV-E11-05 · NEW (accepted)

**07:48.0–07:50.2.** An episode that distributes answers to why the band sings also includes an ensemble instrument image.

**Observed.** E1 reports a title card with the five players’ instruments and a narrowly stereo voice/track.

**Primary check.** The 07:48 and 07:49.3 primary frames show the boardwalk lined with a kit, keys and stringed instruments. Independent 48 kHz stereo gives −29.82 dBFS RMS, −17.91 dBFS peak, max channel difference .027517. The mixed track is not bit-identical mono. Object count cannot identify a title-call performer.

Primary image and direct digital-channel comparison · High for card and non-identical channels; no voice identity proposed Affected route — E11 §§2, 4.8; visual and music No separate return on this decision.

Witness — `episodes/work/E11/critic_e11_blind_notes.md L134–137`.

## Attempted matches without meaningful comparative evidence

#### GBC-AV-E02-02 · UNREVIEWED

**15:52.300; near §4.6–4.7, after cue 303.** Subaru’s introduction is read as socially managed friendliness, with caution about equating effort with falseness.

**Observed.** A close-up shows Subaru’s settled face, slight cheek color and open eyes. The frame follows the introductions by about nine seconds; it does not test the speaking contour or duration at 15:37–43.

**Primary check.** Exact primary seek 952.3 s and ZIP frame 812 at 952.326 reproduce the close-up; cue 301 begins at 937.480 s.

Single facial still; speech delivery receives no AV review from this image. · High for identifying the later face; delivery and intention unresolved. Affected route — E02 §7 and character/voice ledger; limit disposition to attempted AV check. Return GBC-AV-Q02-02.

Witness — `episodes/work/E02/critic_e02_q4_subaru_952_3.png`.

#### GBC-AV-E03-02 · UNREVIEWED

**22:18.000; §4.12.** The free public show does not guarantee an attentive crowd; audience evidence must be specific to the image.

**Observed.** The file named for the crowd at 22:18 shows a light-haired guitarist at a microphone, eyes closed. It supplies no audience count or reaction. Do not use the diagnostic filename as an observational assertion.

**Primary check.** MKV 1338.0 s and ZIP frame 1085 both depict the guitarist; no audience member is identifiable in the shot.

Single frame; does not cover adjacent audience shots. · High for the file-content correction, no conclusion about the audience across the sequence. Affected route — E03 §4.12 and visual form; retain the broader reading’s independent evidence. No separate return on this decision.

Witness — `episodes/work/E03/critic_q6_crowd_2218.jpg`.

#### GBC-AV-E08-02 · UNREVIEWED

**10:51.970–11:20.710.** Rupa links a hostile workplace encounter to her own need for rock.

**Observed.** The selected blind records on Rupa at 21:51–21:55 concern a later car/coda exchange. No selected matched observation describes the workplace vocal turn. Maintain the primary claim; do not transfer the late delivery across settings.

**Primary check.** Cues 227–239 and #618/#622; later #1235/21:52.720 is a different scene.

Coverage gap; primary Japanese versus nonmatching admitted audio observation (Q5 line 158). · High for the spoken need; no comparison for the targeted register claim. Affected route — E08 §4.10; labor/character voice Return GBC-AV-Q08-02.

Witness — `critic_e08_blind_notes.md (restricted E1 slice)`.

## Two ending details independently checked in a local derivative

These two findings were verified from a locally matched hard-sub encode before the Gemini inventory. They supplement the E13 reading's C082–C083 qualifications and do not count as independent-comparator transitions. The encode SHA-256 is `54ade5c2a525f25219c0271c4026f858fd73f0d94ee87e9c187b22770a850a00`; seven picture anchors matched the bundle to within 0–2.67 mean RGB levels on a 0–255 scale. These are targeted image samples rather than an auditory or continuous-performance pass.

| ID | E13 elapsed time | Witness, interpretation and affected route |
|---|---|---|
| GBC-LOCAL-13-01 | 23:05.000–23:05.780, between bundle frames 1365 and 1366 | In three drawn panels a father figure holds a lighter to a cigarette, turns his head, and a cigarette and pack rest on a surface. This supports an interrupted or deferred act in the illustration. Nina had asked him to smoke less (E10 cue 356). The panel cannot establish permanent cessation, motivation, or the date. ED claim C082, visual and relationship ledgers. |
| GBC-LOCAL-13-02 | 23:09.900–23:10.150, between frames 1368 and 1369 | The smaller yellow vehicle in an inset has a white plume at its nose beside an X-armed figure. The larger graphic vehicle beneath the panels continues. A problem with the illustrated vehicle is strongly implied. Its mechanical cause, a repair bill and the economics of an actual tour remain open. ED claim C083, visual and industry ledgers. |

## Readiness and questions outside AV inspection

The exact source objects, on-screen documents, pictured people and reproduced timing/energy measurements above can already ground later work. A reported voice identification and an inference about what a performance means have different evidentiary standing. The required queue concerns genuine remaining observations, including Japanese attribution, changes in sound perspective, the sources of musical passages and movement relative to speech. Prepare a log from the neutral packet in a session with demonstrated Japanese listening and appropriately fine motion sampling. Freeze that log before giving its observer the adjudication context below.

Hina’s ultimate intention, whether school intervention was ethically right, whether Tomo’s judgment generalizes, a couple designation, and the band’s long-term economic viability cannot be decided by a finer frame interval. The promise of ten more years is conditional. Keep these analytical questions separate. Independent synthesis remains outside this authorization, and the required comparison obligations should be resolved or explicitly bounded by the owner before reliance on the affected claims.

[Neutral observation packet](GBC_GEMINI_REINSPECTION_QUEUE.md) · [Current entrypoint](../CURRENT_STATE_AND_CORPUS_MAP.md) · [Final sequential checkpoint](../02%20Sequential%20Readings/GBC_E12-E13_CHECKPOINT.md)

## Adjudication context for the integrator

Withhold this section and the readings from the return observer until their observation log is frozen. An item proposes a test and does not itself count as a reviewed claim.

| Return ID | Bounded claim / reading locator | What would change it |
|---|---|---|
| GBC-AV-Q01-01 | The reading connects Nina’s twice unfinished request to Momoka’s invitation to sing; the index establishes words and order, not how the interruption is performed. (§§4.9, 9.3; cues 429–433, frames 1113, 1117, 1138) | A new speaker overlaps, music or an independent cut fills the apparent gap, or Nina completes more of the clause audibly. |
| GBC-AV-Q01-02 | The reprise places Nina at the vocal center with Momoka on guitar and interleaves public performance with subjective images. (§§4.10, 9.2; cues 433–443, frames 1146 and 1188) | A passage uses an alternate vocal source or cuts away from the plaza independently of the vocal entrance. |
| GBC-AV-Q02-01 | The reading describes Nina singing to Momoka as part of an attempted parting. The cue-linked frames show Nina’s close-up, then spatial displacement under the lyric. (§9.1, cues 249–256, frames 606, 609, 635) | A recorded or nondiegetic continuation is distinguishable, the addressee is absent from the pertinent action, or no response is perceptible. |
| GBC-AV-Q02-02 | Subaru presents herself with elongated wording while Nina offers a compact surname response. Bright versus guarded delivery requires hearing. (§§2, 7 and Subaru introduction; cues 301–303, frames 800, 802) | The vocal contrast is slight, cue timing clips a turn, or the reported level contrast is driven by other sound. |
| GBC-AV-Q03-01 | The reading understands the post-rehearsal state as temporary hoarseness following overexertion. The group’s comments support a represented change; the texture is not established by the stills. (§§4.10, 9.4; cues 357–372, frames 849, 862, 865) | Listeners cannot reliably hear the change in comparable speech, or effects/other speakers account for the apparent difference. |
| GBC-AV-Q03-02 | The reading identifies technologically mediated performance and a plan to replace the missing bassist. The planning evidence is stronger than specific sound-source attribution. (§§4.12, 9.5; cues 420–424; compare planning cues 280–283, frames 634 and 637) | The device is never shown operating, or the mix cannot separate programmed from played bass or other parts. |
| GBC-AV-Q04-01 | The reading contrasts polished stage speech and a rough aside. The visual presence of a phone complicates audible register and audience attribution. (§§4.7, 9.3; cues 221–230, frames 600, 611, 632) | The aside is a represented message or voice-over addressed privately, or neither channel establishes a publicly spoken utterance. |
| GBC-AV-Q04-02 | The words frame the prior outburst retrospectively as a performance and report relief. The bowed head then smiling face establish endpoints only. (§§4.11, 7.3, 9.4; cues 445–449, frames 1134 and 1148) | The expressive switch begins before the intervening reply, or a cut prevents observing a continuous switch. |
| GBC-AV-Q05-01 | Nina identifies danger of saying something harmful and asks for a moment. (§4.5; cues 179–212; frame 594 at 10:12.320) | The voice, speaker or scene boundary differs, or evidence indicates no comparable modulation. |
| GBC-AV-Q05-02 | Nina can retain attachment after hearing Momoka’s account of the split. (§4.8; cues 319–345; frames 845, 931, 936) | Voice attribution, transition or apparent accommodation changes when actual turn-taking is inspected. |
| GBC-AV-Q05-03 | Spoken claw-mark image and prepared live performance are adjacent; it need not all be one public address. (§4.11; cues 424–439; frames 1127, 1134, 1136, 1159) | A discontinuity, different speaker or clearly nondiegetic layer changes the extent of the public address. |
| GBC-AV-Q06-01 | Tomo and Rupa present the melodic line as a constraint on recruitment. (§4.1; cue 6 near 00:42, cue 10 at 00:59.050; frames 13, 66, 83) | The excerpt lacks a comparable audible line or the proposed feature is contradicted by the sound. |
| GBC-AV-Q06-02 | Nina says her throat is improved following the live show. (§4.2; cues 46–56; frames 232, 237, 266) | No reliable audible difference, a different talker or masking weakens the attempted sonic description. |
| GBC-AV-Q06-03 | The playing arrangement supplies practical evidence before explicit group assent. (§§4.14–4.15; count-in cue 432/frame 1071, lyric 436/frame 1092, offer cue 440/frame 1119) | Mix does not resolve the claimed part, assumed doubling is heard, or the offer precedes the relevant event. |
| GBC-AV-Q07-01 | The opposed verdicts document disagreement over standards. (§4.8; cue 262/frame 643, cues 273–274/frames 680–681) | The mix or edit withholds the evaluated performance or contradicts a claimed technical defect. |
| GBC-AV-Q07-02 | The group can correct Nina publicly and proceed to performance. (§§4.16–4.17; cues 440–450; frames 1052, 1065, 1067, 1074) | A different speaker, added interruption, overlap or gesture changes the attribution or strength of assent. |
| GBC-AV-Q07-03 | Nina declares that she will quit preparatory school. (§4.18; cues 471–477; frame 1243 at 23:29.270) | Response attribution or the location of the address differs from the reading; no administrative completion can be heard. |
| GBC-AV-Q08-01 | Nina presents a way for Momoka to become someone she could despise. (§4.6; cues 116–124; frame 371 at 05:43.301) | Contradictory delivery, source attribution or timing weakens a precise characterization of her state. |
| GBC-AV-Q08-02 | Rupa supplies her own account of music’s relevance after the encounter. (§4.10; cues 227–239; frames 605, 608, 618, 622) | Utterance sequence, speaker or direction differs from the assumed proximity/contrast. |
| GBC-AV-Q08-03 | Nina places herself in the vehicle’s path during conflict. (§4.18; cues 384–403; #1029, #1058–1059, #1080 and wheel-contact sequence) | Different timing or sound source changes the reconstruction of the braking and turn-taking. |
| GBC-AV-Q08-04 | Nina gives the explicit confession; romantic coding is strong and reciprocal status remains open. (§§4.21, 13.2; cues 439–448; frames 1200, 1203, 1208, 1215) | An explicit reciprocal utterance would revise the limit; an absent or masked reply should remain unassigned. |
| GBC-AV-Q08-05 | Nina names and practices identifiable chord changes; the written band-name token may be a transcription error. (E08 §4.9; cues 201–202, #536–546; #912/16:15.960) | Different audible tokens or sounding shapes, masking, or inability to separate speech from playing would restrict the claim. |
| GBC-AV-Q08-06 | Nina’s school performance and the editorial presentation of 空の箱 overlap without guaranteeing every heard source exists in the school. (E08 §13.2, cues 355–360; #952, #970, school PA) | A continuous source-matched shift in room reverb, PA filtering or explicitly located performance could instead assign the contested layer. |
| GBC-AV-Q08-07 | One E1 witness proposes two identifiable singers and a low piano; the reports exceed what the available measurements alone establish. (title cue 259 and subsequent low attacks) | Separately identifiable voice, instrument, matching source cue or stems could change the attribution. |
| GBC-AV-Q09-01 | Tomo’s permanent forecast about Nina’s skill differs from a local practice correction. (§§4.9–4.10) | A different speaker or clause grouping would change how the judgment is assigned. |
| GBC-AV-Q09-02 | The ending recapitulates the opening with Tomo now speaking in rehearsal. (§4.21) | An unrelated playback or cutaway would narrow the claim about immediate application. |
| GBC-AV-Q10-01 | Rupa uses finite opportunity to motivate a choice, leaving Nina’s answer open. (§4.11) | An extra imperative, overlap or attribution error could change the scope of pressure. |
| GBC-AV-Q10-02 | The father’s listening and Nina’s subsequent apology occupy distinct turns in family repair. (§§4.22–4.23) | A different order or source would narrow any inference about the effect of hearing the song. |
| GBC-AV-Q11-01 | The declaration belongs to Subaru; the following exchange uses Rupa’s experience with loss. (§§4.6–4.7) | A different source of the line would reassign it in the voice and relationship ledgers. |
| GBC-AV-Q11-02 | Attributing the song and deferring guitar performance are separate actions. (§§4.17–4.18) | A different order would pressure any causal coupling of the actions. |
| GBC-AV-Q11-03 | The MC introduces an authored purpose before the ensemble performs. (§§4.20–4.21) | Sound bridging or a different entry may revise the formal boundary without changing the written introduction. |
| GBC-AV-Q12-01 | Nina’s repeated rival name and Momoka’s answer distinguish agitation from the explanation of draw. (festival exchange) | A different speaker or overlapping retort could change their assignment. |
| GBC-AV-Q12-02 | Nina bounds her competence in the kitchen. Momoka records the idea and supplies tentative lyrics. (kitchen, hot pot and first draft) | Incompatible voiced turns would require a narrower attribution than still positions indicate. |
| GBC-AV-Q12-03 | The instrumental and travel montage connects successive work stages; RMS does not identify the mix. (studio/practice, montage) | Separate nonbridging cues would narrow the interpretation of sonic continuity. |
| GBC-AV-Q12-04 | Nina qualifies her account of Hina; Rupa and Nina favor proceeding and three vote against. (cues 308–312 and vote) | An offscreen voice or missed response could force an attribution or vote correction. |
| GBC-AV-Q12-05 | The players discuss modulation and whether a change fits all five. Adoption remains open. (rehearsal, cues 351–372) | A direct match or clearly abandoned figure would resolve part of the arrangement claim. |
| GBC-AV-Q12-06 | The shrine moves from personal address to a five-person promise; the wish to win is provisionally Momoka’s. (shrine, frames 1004/1013/1014) | Contrary turn or contact order changes who asks, answers or joins. |
| GBC-AV-Q12-07 | Professional evaluations and Nina’s reaction to 103 plays are distinct; its emotional scale remains unsettled. (Nakata, Miura and release counter) | Different sound perspective or overlap may change the attributed reaction. |
| GBC-AV-Q13-01 | School testimony, dream framing and the later report have different evidentiary status. (cues 1–28, 258–282) | Different sound perspective or source could narrow the assignment of reported dialogue. |
| GBC-AV-Q13-02 | Miura describes a promotional problem, and Hina separately makes personal help conditional. (agency report and Hina, cues 57–116, 136–185) | Different attribution or clause boundary could change whose condition is being stated. |
| GBC-AV-Q13-03 | Tomo couples disagreement with attachment and qualifies her inference about the others. (rehearsal, cues 215–257, 284–300) | A change of speaker or addressee could revise that scope. |
| GBC-AV-Q13-04 | The band offers repayment; Miura undertakes to handle funds and contracts; Nakata offers a conditional future invitation. (agency bow and engineer, cues 309–357) | Different turn allocation would matter to an individual character claim. |
| GBC-AV-Q13-05 | The pledge is prospective and a later decision admits Nina to guitar performance. (restaurant and backstage, cues 364–417) | An alternative addressee or speaker could alter the distribution of authority. |
| GBC-AV-Q13-06 | A bandmate speculates about Hina’s intentions; no Hina confession is present. (backstage notes, cues 418–434) | Hina speaking or a different turn-taking pattern would change attribution. |
| GBC-AV-Q13-07 | Nina states no regret and recognizes another listener. The text does not establish that everyone hears every clause. (cues 435–468, frames 1176–1186) | A clear mic or interior contrast changes the public/private scope; the unusual indexed wording needs direct hearing. |
| GBC-AV-Q13-08 | The last insert lyric ends at 21:45.540, before the band’s literal shared ending and the credit title. (cues 468–485, frames 1341–1346) | Different voice allocation or music boundary could revise formal or performance claims. |
| GBC-AV-Q13-09 | Collective travel is strongly implied, individual chronology remains open, and the phone graphic links two songs. (frames 1346–1377) | A dated in-world event or an independently identifiable continuity link could promote a particular claim. |
| GBC-AV-Q09-03 | A centrally mixed call is audible; the character voicing it remains open. (§4.11, title card) | An identifiable onscreen or independent source cue would narrow the alternatives. |
| GBC-AV-Q11-04 | The first written phrase includes は. One independent listener hears it omitted; the plain thanks agrees. (§4.7, cues 144 and 148) | An audible particle or clear elision resolves the wording locally. |

## Exact exposure register

All paths below are relative to the private Gemini v1 run root. Each byte length and SHA-256 identifies the source file. For E1 the admitted source lines appear below; metric JSON and NPZ exposure was confined to structural keys and numeric values. For the two technical methodological Markdown files only source, capability, method and stage sections were consulted, and only coverage/provenance fields and anchors from the coverage ledger. Diagnostic images are separately selected source specimens, not quoted verbal claims.

| Relative input path | Bytes | SHA-256 | Reader and admitted view |
|---|---:|---|---|
| `METHOD_AND_AGENT_TOPOLOGY.md` | 10837 | 610d800973c7c2d8d766ec3bcc56a5fc9246326e969e56dffa741f58104bd273 | principal · technical records |
| `SOURCE_AND_CAPABILITY_MANIFEST.md` | 10671 | 687fa07caa8e925abf412b899b7be9f6ac16fb7ea79e5aeb2481ced0c8e29c68 | principal · technical records |
| `ledgers/EPISODE_COVERAGE_AND_PROVENANCE_LEDGER.md` | 11014 | 11b4cd09bd5b2052a19be0dbef0d9d1c9c424d3dca0b8a4f4e33c2a97313dcdb | principal · technical records |
| `provenance/source_inventory.json` | 66233 | b3dfc01d3d561b58164ccb7aaecf04fd1824375833038f390d3c6d42da28e79d | principal · technical records |
| `clips/E01/E01_clip_manifest.json` | 4180 | 4f38545b4f9ca3103200801a305e5e6586995839265c84dc9e74af29a4409e28 | principal · technical records |
| `clips/E02/E02_clip_manifest.json` | 4184 | a82a1facf1ab64453b708a37e91f463f24305e57f0327f3197745eb5a46d6c1e | principal · technical records |
| `clips/E03/E03_clip_manifest.json` | 4180 | 9374184283b4e12e1f5dc96783724f315e4b4a28974b02f0c64070d617a0da0e | principal · technical records |
| `clips/E04/E04_clip_manifest.json` | 4184 | 4847fc4952840cf56408aec1d9fd1ef13e304a8fd184852bb6b076d53e61f1f7 | principal · technical records |
| `clips/E05/E05_clip_manifest.json` | 4183 | 640c60ce8816d162ecd9547021d45c0149d34ec70112c5382e3db2a39271c738 | principal · technical records |
| `clips/E06/E06_clip_manifest.json` | 4186 | 7a5421961b461c585297eb2ba8d95a20575717ede7268dc8529d4095438ca796 | principal · technical records |
| `clips/E07/E07_clip_manifest.json` | 4180 | dec5ee2ce19285cde9e3ecf32c91f1d91b9a8cfd63877180e9a593293f0a67fb | principal · technical records |
| `clips/E08/E08_clip_manifest.json` | 4185 | 8d92b2ae6a7459d31aff535ffcefd055f879ce61c3df30370b0e9c0607f07918 | principal · technical records |
| `clips/E09/E09_clip_manifest.json` | 4184 | 1927f6546b8885773416bf36ffd71f2b46eaa04b0ca507a53bdea1c6d8af14b6 | principal · technical records |
| `clips/E10/E10_clip_manifest.json` | 4185 | 4d76fddf45c90308b9dac806172ea9cd8862f7ec7a39f253580f5e47af5cc005 | principal · technical records |
| `clips/E11/E11_clip_manifest.json` | 4185 | 5ce783a2d71b2ca744c769664c3a6efe7e0a621968c1bcdc804a748ace01a753 | principal · technical records |
| `clips/E12/E12_clip_manifest.json` | 4184 | b51ac93d54890350903ed89dbe79e773bff4fbb1098f9abb7e250c23c7d0d40e | principal · technical records |
| `clips/E13/E13_clip_manifest.json` | 4183 | 3754efc18a5ac4ebd3c1053b17d3c5e5fcf8da5e00dd7a6e7ec99d384c51bc6c | principal · technical records |
| `episodes/work/E01/critic_hand_2134_2_full.jpg` | 77655 | 3e9b22d3f708d6a210b68e070a1fb8c37c8bed38b276f2f24af2ec3fd804e82c | E01–E04 reviewer · image |
| `episodes/work/E01/critic_hand_2134_7_full.jpg` | 44562 | fcba4e3cd23eb557d12f2a1c80c3afd9745e4c1ee7824580e79eaea5de931546 | E01–E04 reviewer · image |
| `episodes/work/E01/critic_hand_2135_5_full.jpg` | 170530 | 7e08263ddbc2654b85edb29a737ae84eaa49f0c2084374530d6ffc2599b3484e | E01–E04 reviewer · image |
| `episodes/work/E01/critic_hand_2142_8_full.jpg` | 234560 | 9d2c7189e3f0de5f55678620144385505822a8c35146eb6e1583537f4147ba8e | E01–E04 reviewer · image |
| `episodes/work/E01/critic_kyoko_2201_guitar.jpg` | 36171 | 8122ceae28ecb4ee3fad7636777bfa7adb12a8a0574c0a1d1a132cab863b49c4 | E01–E04 reviewer · image |
| `episodes/work/E02/critic_e02_q3_momoka_735_0.png` | 8625853 | 0aa8cbc5591ebdbcb410d280aaa46cbff05c2a9e9bea38e60c25aa76ab755099 | E01–E04 reviewer · image |
| `episodes/work/E02/critic_e02_q3_nina_736_8.png` | 8639796 | 0d1364691720bf1223d7f729bca95bf5b8c539b3c93c7cd053d5ec01adf9aaab | E01–E04 reviewer · image |
| `episodes/work/E02/critic_e02_q3_truck_768_2.png` | 5773184 | 1d6181a3ed5e2445a1843911f4b12d5b7e59b2b9a17c2b5c9b8e735bf9ef03f8 | E01–E04 reviewer · image |
| `episodes/work/E02/critic_e02_q3_truck_769_1.png` | 6275284 | 0dec55063bce24ca2ff435e8e338834550aa045120720fc15d84c4673752c2e4 | E01–E04 reviewer · image |
| `episodes/work/E02/critic_e02_q4_subaru_952_3.png` | 4518963 | 9a66932093319aa7ad1dff5dd6de04d0a340f7e7952ba2e6b8138ec8946d8276 | E01–E04 reviewer · image |
| `episodes/work/E03/critic_looper_1355_5.jpg` | 263263 | 03891c71ba6151486e5379955be8057f5fbebe5b731292ee76aeda8bf27f77bf | E01–E04 reviewer · image |
| `episodes/work/E03/critic_looper_1400_2.jpg` | 258216 | 418c9b43b722a905c152c7287e272a936e7a10b2bd64dd25683401472f215100 | E01–E04 reviewer · image |
| `episodes/work/E03/diag_1080p_kickbeater_1326.0s.png` | 7723612 | 677dacd4e4441ba5ade15db3ff0c9f94d1bda3a85566dfc1d997b1e43812732d | E01–E04 reviewer · image |
| `episodes/work/E03/critic_q6_crowd_2218.jpg` | 186502 | c6e257874cef5f939ef3bb9a7592801b0f8a24d6e59ea91b863003de9966cc84 | E01–E04 reviewer · image |
| `episodes/work/E03/critic_yoshinoya_1124.6.png` | 7569565 | df43b3a11776699d67f723e84f066e985c08cd7c3234fc280f17dbce7e85f319 | E01–E04 reviewer · image |
| `episodes/work/E04/critic_q2_52850_raw.png` | 6919420 | 79422fcbe9b4b553adccdcb67a844adcdfd2c88b5bafc136ac37be9844f5a459 | E01–E04 reviewer · image |
| `episodes/work/E04/critic_q2_52850_hand_2x.png` | 343500 | ca8eef7088c2f4fa9363a54fd5b49605178f8007c3dbb17269606929885235ba | E01–E04 reviewer · image |
| `episodes/work/E04/critic_q3_etude_1228_1233.jpg` | 216651 | 485232aa6c1d7a8928a523b4a000dc5ce373a192a731c349d730f135e871cf63 | E01–E04 reviewer · image |
| `episodes/work/E04/critic_q5_climax_2147_2157.jpg` | 419592 | 3de403186bb64f83112fcfb93c0f435301b4a51dd458df8e3a2d1c388a0fcefd | E01–E04 reviewer · image |
| `episodes/work/E05/critic_e05_dd_stage_0916.png` | 5635893 | 0dfb5117c370d0180ec5793423fb0b0b52ac6ab556d5b11d23f6f50b9d7e87db | E05–E08 reviewer · image or numeric projection |
| `episodes/work/E05/highfps_02a_tdc_ink_dissolve.jpg` | 243101 | e8ca30a4b7b1e3eff5db1d43adb919414f4ad9b58187e0d99c7bb88c08badb04 | E05–E08 reviewer · image or numeric projection |
| `episodes/work/E05/highfps_03_izakaya_splash1.jpg` | 363711 | 1c543dd070007ef58b16a7f634421cfd7fe009aef96ecf66956dbe128584f423 | E05–E08 reviewer · image or numeric projection |
| `episodes/work/E05/frame_1080p_2124_nina_hands.png` | 5137627 | 2c37a4c435bdf5b4cc0c8acd07d064106386711c4b97f4a6cf4fdc7b0bba3c04 | E05–E08 reviewer · image or numeric projection |
| `episodes/work/E05/frame_1080p_2128_momoka_subaru_hands.png` | 7189917 | 06fb7e62c92f4ca9bb70cc18d4c0cd85428d04318c1dcf5327631ce6afb9fb0d | E05–E08 reviewer · image or numeric projection |
| `episodes/work/E05/critic_e05_nina_front_2153.png` | 1944550 | 8978a67c3561a64c5c9eb1120f4c8c770adc27e223ccab23cee6d723c358da65 | E05–E08 reviewer · image or numeric projection |
| `episodes/work/E06/agent_b_e06_acoustics_results.json` | 51756 | cd119d2b384520798a3124ec1b433808da4114fe24144db1e1b414d4cf4d86ae | E05–E08 reviewer · image or numeric projection |
| `episodes/work/E06/critic_e06_metrics.json` | 40843 | d01f369a99786d471440296ea9176b6c48188e4c53919e887a581375ec015daf | E05–E08 reviewer · image or numeric projection |
| `episodes/work/E06/critic_e06_visual/q1_strobe_strip_12fps.jpg` | 326912 | 1dc093755e0554f502cf92185f8ced837da7c07f4d1c6580fc36791e78e0c4eb | E05–E08 reviewer · image or numeric projection |
| `episodes/work/E06/critic_e06_visual/q2_bath_strip_6fps.jpg` | 307623 | a10b24d83bfa4e2af365d69535b4df71e2ef7376375d26de2ec201f226bf9475 | E05–E08 reviewer · image or numeric projection |
| `episodes/work/E06/critic_e06_visual/e2_jam_downbeat_12fps.jpg` | 343207 | 1a993f8b2309eea594e45dc0708efcd9a2749e6af336d56df16f607dade46c66 | E05–E08 reviewer · image or numeric projection |
| `episodes/work/E06/critic_e06_visual/q3_keys_amp_macro2x2.jpg` | 172681 | 714944073621a1a387f1fcb2246a338bd71e12e81d70588cdcff1fa9da95de8b | E05–E08 reviewer · image or numeric projection |
| `episodes/work/E07/critic_e07_dsp_results.json` | 39289 | 1359f8f5320fa647df3a42dcec5e9a7dd4871faebfa3aefc060fbb0819b2fa82 | E05–E08 reviewer · image or numeric projection |
| `episodes/work/E07/highfps_c_15_rupa_stage_nudge.jpg` | 278769 | d7c5193f03c861960ff571dd7fe7379e267ab4636c3dcf8e418232f6c8d79585 | E05–E08 reviewer · image or numeric projection |
| `episodes/work/E07/highfps_c_16_concert_opening_fireworks.jpg` | 256292 | d1b4cb6739658b638c9473fb7b7f3be3116c32d05c54d47d82da022dd03fec61 | E05–E08 reviewer · image or numeric projection |
| `episodes/work/E07/highfps_c_21_pre_nep_exact_boundary.jpg` | 175125 | 48eec9ae3724bd925b915bc5040d416bad11888a07db976c5853e51344f622cc | E05–E08 reviewer · image or numeric projection |
| `episodes/work/E07/critic_e07_q6_2317_coda_strip.jpg` | 255194 | 4f8b06c0e9a4d724b07c6df971399003bec96d9e5a0434db94eefc5ae4cb9fa4 | E05–E08 reviewer · image or numeric projection |
| `episodes/work/E08/critic_e08_media/critic_e08_audio_cuts.json` | 112462 | befec9abce2135c8f747921b8ec06f91c5c830bb2c40d10e07cf1d63ce3232b2 | E05–E08 reviewer · image or numeric projection |
| `episodes/work/E08/highfps_c_04_foodcourt_collar_fist.jpg` | 453667 | 9f7f89314562e19c644f2157207ce02894825161b3b0f54208caaaa990c0a7a2 | E05–E08 reviewer · image or numeric projection |
| `episodes/work/E08/highfps_c_05_foodcourt_flinch_drop.jpg` | 526546 | a8d0cd3f5a4d24e1466dcea11f0ff4a5936f0ac6b78ab96e6a39abbe581615c5 | E05–E08 reviewer · image or numeric projection |
| `episodes/work/E08/highfps_c_12_keitruck_drift_stop.jpg` | 411361 | 935c22a34454b52d7e7e0a01fc2396cf88336245cb3020c1b99da7c9518ba401 | E05–E08 reviewer · image or numeric projection |
| `episodes/work/E08/highfps_c_13_horn_hand_overlap.jpg` | 289974 | 2b354af78341776afc20363d1f994cbfa0dab801d96139a1dd2cf1d9495d8b54 | E05–E08 reviewer · image or numeric projection |
| `episodes/work/E08/highfps_c_15_stereo_knob_tears_star.jpg` | 415002 | f3ccaef15ef851686f4ad2a04eba0ca2ea4abb4da02341167cc39308cd6b6063 | E05–E08 reviewer · image or numeric projection |
| `episodes/work/E09/agent_a_crops/guarantor_doc_rot180.png` | 265817 | c3ac76a350498a5e5d27100e155cf5b195916f976c30358c6027723e40792014 | E09–E11 reviewer · image |
| `episodes/work/E09/agent_a_crops/p3_nina_2012_712_full.png` | 8938022 | 3408dc9fda92805ea43b0f4706b9e1fad04205ad0368692b32c05379ca13f8e1 | E09–E11 reviewer · image |
| `episodes/work/E09/agent_a_crops/p3_nina_2012_712_hand_zoom.png` | 227521 | 2d36ad6e7fb3d8c9ad2a82f353d012455012db4283bb2d8c2ff3abb16225c5f8 | E09–E11 reviewer · image |
| `episodes/work/E09/agent_a_crops/rupa_kick_6fps_grid.png` | 786661 | 147b66a79702fa0a774681c576da97588cc34aef1937bc32e773bbb09d91bd04 | E09–E11 reviewer · image |
| `episodes/work/E09/agent_a_crops/toge_chat_zoom.png` | 488094 | 17e1ca37c4e5f7eecf512dd9e5dbf2924ab79c6fa3bebf7d1517aa33d940fe79 | E09–E11 reviewer · image |
| `episodes/work/E10/a_pass1_checks/crop_bizcard_full_0045.png` | 990343 | 06a5ecd5ad6d131c7ca73ed28d644ecf6b52e6283af0c9614b110b4888c87512 | E09–E11 reviewer · image |
| `episodes/work/E10/a_pass1_checks/crop_shazaibun_1316.png` | 1139676 | 1f788c46aa17ec7b2540807af7c00f895fb6e2beaa768398ba60dd9358afbce5 | E09–E11 reviewer · image |
| `episodes/work/E10/a_pass1_checks/crop_hanseibun_1513.png` | 1298372 | a38276dd458d9fe3e4874fce398c022950cdd2203ca3c0e4fefa745300e0605d | E09–E11 reviewer · image |
| `episodes/work/E10/a_pass1_checks/crop_lyrics_2033.png` | 898354 | e0a2d6b315fe4efc0b4525a2fa899db2402bde314e9099da6d893f8b3612045f | E09–E11 reviewer · image |
| `episodes/work/E10/a_pass1_checks/pinky_2002/f07.png` | 5381598 | 5b81388c7aafada175b87a43154d729aa6acdea1b54dc49071b2b5179aec9dc5 | E09–E11 reviewer · image |
| `episodes/work/E11/agent_a_tmp/crop_email_tendo.png` | 819031 | 66bc774124fbea5f55bab39e21b2b7b832c9083720b862614e14d68bbf7b878e | E09–E11 reviewer · image |
| `episodes/work/E11/agent_a_tmp/toge_song_cred_20155.png` | 306110 | 41b68d4ca67e747cfe201c5ed5ef4979c4e7c55d7e5c3db2931560c060c6ec5e | E09–E11 reviewer · image |
| `episodes/work/E11/agent_a_tmp/tomo_cert_22085.png` | 978557 | 5149882e4e0f961083db38f6de9b971f9e369789c8bef4b31827894083016f01 | E09–E11 reviewer · image |
| `episodes/work/E11/agent_a_tmp/tendo_miura_23042.png` | 1167051 | b11fe3130fb3cbee2c32c6b573d5a1d22e12d83b929b1b8dbfa1cc4a5f0c4ab2 | E09–E11 reviewer · image |
| `episodes/work/E11/agent_a_tmp/hina_finger_15398.png` | 787087 | f0713bb9f8cc412abce2ba56f157a06af6bca7ef70d562c220f172158f335e95 | E09–E11 reviewer · image |
| `episodes/work/E12/diag/crop_0332_guitar_price.jpg` | 253879 | 1bed64569ff80c032b1a449ad46e474f3aeeabebe00f18534485f1dc1a22c15a | principal · image |
| `episodes/work/E12/diag/crop_0849_lyric_complete.jpg` | 276421 | cad95929399f20b8fb679e657182d0eb93ddfdccb357f37f79fe7ca572fa78a8 | principal · image |
| `episodes/work/E12/diag/crop_1156_proposal_screen.jpg` | 208159 | e7608e71534321d1c3ea16e329c8e60fc9c53584525ea1acc508f236bc715c69 | principal · image |
| `episodes/work/E12/diag/crop_1930_two_pinkies_1080p.jpg` | 215192 | 5bd485f53919d2c2b269d2af5744f28d651ecfa86f8b4e4f978ba25635b9053f | principal · image |
| `episodes/work/E12/diag/crop_1931_five_pinkies_1080p.jpg` | 241210 | f2b102184fa67aadbd10edbf6b5b7adf58cb649541d7fccebc92f1cec4c3a487 | principal · image |
| `episodes/work/E12/diag/crop_2201_plays_103_1080p.jpg` | 195190 | 9649e6e16ee349897e75097d239a987c1e29f879da84ad4a1790cfca9591395b | principal · image |
| `episodes/work/E13/diag/b3_hillvalley_cup_06260.png` | 6935950 | d6c70dd281016342f078d66e3cba1eef1fd254ac8915d2c6451a568de792b536 | principal · image |
| `episodes/work/E13/diag/b3_prank_wb_17480.png` | 5735351 | 9878e8bae96ba5ee21c716b4b179231a6316397b90ab60b2ee25ee5365114c37 | principal · image |
| `episodes/work/E13/diag/b3_prank_ceil_17510.png` | 5685651 | e2a378b58fcdeb9849786bd2d336ff91655eaff7407c6aff0eb830177ede5914 | principal · image |
| `episodes/work/E13/diag/b3_prank_door_17555.png` | 7521630 | aae2e130499d0c69a529573bd39157404a3b51ce33f68c5c95f2d2480516cba8 | principal · image |
| `episodes/work/E13/diag/b4_dd_balcony_21520.png` | 5833265 | dd9cab89192db12cc263bed1c230325b8a69de315d9fe55bd18a0566164a172f | principal · image |
| `episodes/work/E13/diag/b4_flashback_greenfloor_19555.png` | 8370408 | 860041254ba0c1d2433b42f8e8465d33f52b4c046dad6febd92e89344161fd5c | principal · image |
| `episodes/work/E13/diag/b4_title_transition_2211_2216_strip.jpg` | 224340 | 5c7b5f6a488dd4d0ca580af93df2da3dfe4a6ab4f8cb80941e8255621ecce696 | principal · image |
| `episodes/work/E13/diag/b5_cred_2337_prod_end.png` | 6062942 | 383d2e52a337d4e32562c7e0b46df9caec3c5f0ad111496562241c48ee5355bf | principal · image |
| `episodes/work/E13/diag/ep13_rms_01hop.npz` | 227740 | d9a55f5eabf9a3ce5abd0e4b4c62637e3c2e0e7cdb702718bdc172bf9656c339 | principal · numeric arrays |
| `episodes/work/E08/critic_e08_blind_notes.md` | 35696 | ce5f5e2423acc9a5b094015d94734f179f47fd825e9039012f3290b8d8e21495 | episode reviewer · E1 projection |
| `episodes/work/E09/critic_e09_blind_notes.md` | 31942 | 37ef9565764d55a9b3a7b49f72e819ddd75b2d35582a85940332119e99c7aa7a | episode reviewer · E1 projection |
| `episodes/work/E10/critic_e10_blind_notes.md` | 37351 | 2de2b2b32ed2f2be99942048016172afe2d71828b2684b8f092d79c9df4a9c32 | episode reviewer · E1 projection |
| `episodes/work/E11/critic_e11_blind_notes.md` | 32525 | 18cf7b5d85af82b7c5ed5941667c1d5c04c920f053e9d7d0c5ed73d58e6e5340 | episode reviewer · E1 projection |

93 exact source files admitted; 2,426 other files had filename/size/mtime metadata only.

- `episodes/work/E08/critic_e08_blind_notes.md` — 74 projected statements from lines 27–28, 42–45, 58, 60–61, 63–64, 66, 68–70, 72–73, 77–78, 87, 90–91, 93, 95–96, 113, 130, 132, 136, 138, 145–153, 155–156, 158, 170, 179, 190–193, 196–197, 201–203, 206–208, 212, 216, 220–224, 226–227, 234–237, 244, 246. View SHA-256 `387829feb615f03e3a69f694577d1bc73347267121273b9df63c3f80a88be973`.

- `episodes/work/E09/critic_e09_blind_notes.md` — 58 projected statements from lines 25, 28, 39, 41–42, 54, 57, 59–60, 63–66, 70–72, 84–85, 89, 92, 97, 101, 107–108, 119–120, 122–123, 125, 130, 133–135, 147–148, 151–153, 162, 164, 169–170, 176–181, 188, 197, 201–202. View SHA-256 `28fe62721b1331dd05d19691d1c757f7a3804b966ed27fc6d8536b75f4f634c0`.

- `episodes/work/E10/critic_e10_blind_notes.md` — 54 projected statements from lines 23–26, 28–31, 33, 35–39, 42, 45, 101–103, 105–107, 122, 133, 140, 143, 146, 154–156, 159–160, 162, 164–168, 171, 174–176, 204, 210, 212, 223–225, 227–228. View SHA-256 `c4a2f935d4ed4c6ab76cf3fe62e0d24a416672c8c30d75e8d782de735676283a`.

- `episodes/work/E11/critic_e11_blind_notes.md` — 62 projected statements from lines 19, 26–27, 29, 35–37, 44, 48, 50, 52–53, 57–61, 65, 69–72, 86–87, 89–90, 93, 105, 109–111, 113, 117–119, 121, 124–125, 134–135, 137, 141, 152–153, 186–194, 197–198, 202, 206, 212, 215. View SHA-256 `16a763f7a04bba02ff3691ea761343e897367eca5a2464d3bc5e2d98a78ecbc3`.

**Reading hashes at the independent freeze.** SHA-256 values identify the exact prior Codex files used for comparison.

| Episode | SHA-256 |
|---|---|
| E01 | 2aa7370d2c06b5519b5489ae7af3623d90380a4c4e7cb9c5978559c088941e65 |
| E02 | a284282de3eed5e859a479c7ef5b187f70565d7113a9e0d71e56a46d5460ead7 |
| E03 | 626a3e02dcb39e9dbb4e4767f814d9d10146cbd908dbb6ee4c28d2a9b2b5191c |
| E04 | 92adc4b60f2885767945282f8e4df7fea65ba87eb7a7c7d92e3c266ce53fc9b8 |
| E05 | 429c95e61b50471842829f3c6ca70445b7fe56950049ed30f36202215b811461 |
| E06 | 97ed8fd61ece02101e0e9b56fd64a17a062dd7693a63fa05513ba104a7d57482 |
| E07 | 04174da449acd717eb9af6e7a0bf7deaaa6ea0fd1f037eef891ebf5aba4dcb33 |
| E08 | e8acd68cf5c5ec75bd6835a5b54f8cc7ab4f2688e959bec85162022735f0bf75 |
| E09 | e150c1ab2e8af2e6ea7511e5018090786a3cd56eca83ea47f3d4f9f1cdd5d844 |
| E10 | 9e2178a0993ec4b68e0575facfe22c89bb165f1be1e5a894afbb99e401fd8c0e |
| E11 | aa77d88e2bb3f9dd0353394261c2816386f497e8a0f56d89ec2f64cc5f590ea4 |
| E12 | 7e06c0bd57c76c6565a7c5b288a48971671243ec17a2e20f6efffa98b54c315f |
| E13 | a7164b9a736d2d69d3b1e58b302f96d46329d98664dedc2c53da60d4fe2d5057 |
