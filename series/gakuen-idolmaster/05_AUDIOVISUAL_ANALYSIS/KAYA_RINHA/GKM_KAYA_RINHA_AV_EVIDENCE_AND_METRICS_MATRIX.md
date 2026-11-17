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

# Kaya Rinha — AV evidence and metrics matrix

All 18 rows have matched Japanese source scenes, actual still inspection and a computed audio excerpt. **Every row remains unreviewed by direct listening and continuous motion.** The [baseline](GKM_KAYA_RINHA_COMPLETE_AUDIOVISUAL_BASELINE.md) owns the observation, interpretation, confidence limit and next discrimination for each matching ID. The [point index](SUPPORTING_DATA/observed_anchors.json) contains source SHA, stream, integer PTS/time base and image SHA for the cited anchors.

## Selected recorded-mix measurements

LUFS is integrated loudness, LRA is loudness range in LU, and dBTP is estimated true peak. These values describe stereo final mixes containing other speakers, music and effects. They are neither Rinha loudness measurements nor emotion classifiers. All selected decoded samples were preserved in the extracted WAV and then measured without a normalization write to the source.

| Target | Physical asset | Conservative scene envelope | Measured source window | LUFS | LRA | dBTP | Affected claims |
| --- | --- | --- | --- | ---: | ---: | ---: | --- |
| P0-001 / Temari Dear 015 | `RINHA-PKT-TEMARI-11-20` | 00:26:18.000–00:30:51.000 | 00:28:42.000–00:30:47.000 | -17.75 | 6.0 | -1.80 | C034, C035, C067, C068, C069, C070 |
| P0-002 / Temari Dear 016 | `RINHA-PKT-TEMARI-11-20` | 00:30:47.000–00:37:03.000 | 00:30:49.000–00:37:01.000 | -17.71 | 6.0 | -4.81 | C009, C012, C013, C014, C020, C057, C070 |
| P0-003 / Temari Dear 020 | `RINHA-PKT-TEMARI-11-20` | 00:50:53.000–00:55:55.000 | 00:50:57.000–00:52:08.000 | -17.92 | 4.5 | -3.70 | C030, C073 |
| P0-004 / Misuzu Dear 016 | `RINHA-PKT-MISUZU-11-20` | 00:20:24.000–00:27:16.000 | 00:20:26.000–00:27:14.000 | -22.21 | 5.7 | -8.79 | C009, C012, C013, C014, C031, C057, C058 |
| P0-005 / Misuzu Dear 024 | `RINHA-PKT-MISUZU-21-27` | 00:15:41.000–00:23:14.000 | 00:15:43.000–00:23:13.000 | -21.65 | 5.6 | -8.54 | C011, C018, C054, C066, C067, C068, C069, C070, C071, C072, C073 |
| P0-006 / Saki Dear 026 | `RINHA-PKT-SAKI-21-27` | 00:32:47.000–00:38:25.000 | 00:33:40.000–00:36:23.000 | -21.58 | 6.7 | -8.53 | C005, C006, C007, C008, C033, C059, C070 |
| P0-007 / Ume Dear 024 | `RINHA-PKT-UME-21-27` | 00:15:12.000–00:23:07.000 | 00:15:14.000–00:18:55.000 | -21.23 | 4.6 | -8.65 | C020, C044, C046, C047, C060 |
| P0-008 / Support 0097 part 01 | `RINHA-PKT-SUPPORT-0097` | 00:00:00.000–00:01:38.000 | 00:00:00.000–00:01:37.000 | -20.71 | 12.2 | -8.64 | C015, C021, C070, C073 |
| P0-009 / Support 0097 part 02 | `RINHA-PKT-SUPPORT-0097` | 00:01:36.000–00:03:17.000 | 00:01:37.000–00:03:16.000 | -21.95 | 7.6 | -8.65 | C037, C038, C039, C040, C041, C055 |
| P0-010 / Support 0097 part 03 | `RINHA-PKT-SUPPORT-0097` | 00:03:15.000–00:04:40.950 | 00:03:16.000–00:04:40.950 | -20.31 | 6.0 | -8.46 | C019, C060, C070 |
| P0-011 / EVENT_016 main-03 | `RINHA-PKT-EVENT-016` | 00:10:12.000–00:14:04.000 | 00:11:16.000–00:11:56.000 | -24.71 | 6.0 | -7.47 | C042, C043, C066, C067, C068 |
| P1-001 / Saki Dear 016 | `RINHA-PKT-SAKI-11-20` | 00:17:10.000–00:20:12.000 | 00:18:15.000–00:20:08.000 | -18.05 | 5.7 | -3.15 | C007, C059, C062, C063, C069, C071 |
| P1-002 / Saki Dear 034 | `RINHA-PKT-SAKI-28-37` | 00:35:40.000–00:39:58.000 | 00:36:05.000–00:39:05.000 | -21.31 | 3.7 | -8.71 | C019, C048, C055, C059, C062, C069, C070, C071 |
| P1-003 / Ume Dear 016 | `RINHA-PKT-UME-11-20` | 00:20:43.000–00:24:54.000 | 00:22:30.000–00:24:50.000 | -17.70 | 6.2 | -5.14 | C007, C014, C020, C060, C062, C063, C070 |
| P1-004 / Ume Dear 029 | `RINHA-PKT-UME-28-37` | 00:04:59.000–00:09:48.000 | 00:06:25.000–00:09:35.000 | -21.47 | 4.7 | -8.58 | C019, C046, C047, C048, C060, C069 |
| P1-005 / Temari Dear 024 | `RINHA-PKT-TEMARI-21-27` | 00:15:39.000–00:22:27.000 | 00:16:07.000–00:22:24.000 | -21.39 | 6.0 | -8.23 | C037, C039, C042, C048, C056, C057, C067, C068, C069, C070, C073 |
| P1-006 / Misuzu Dear 023 | `RINHA-PKT-MISUZU-21-27` | 00:10:30.000–00:15:45.000 | 00:10:32.000–00:13:30.000 | -21.57 | 4.5 | -8.80 | C048, C054, C055, C058, C067, C068, C069, C071, C073 |
| P1-007 / Ume Dear 015 | `RINHA-PKT-UME-11-20` | 00:16:15.000–00:20:50.000 | 00:18:00.000–00:20:45.000 | -17.67 | 5.3 | -4.98 | C042, C043, C048, C052, C060, C067, C068 |

The 18 measured windows total **3473.95 seconds of selected-mix computation. This is not direct-listening coverage, total compilation duration or an exhaustive Rinha-voice duration. The excerpts are disjoint within each physical source. Saki026 excludes the later stage performance; Ume024 and Misuzu023 have later visual anchors outside their selected audio windows. Source overlap in conservative navigation envelopes is not counted as independent evidence.

## Interpretation of the measurements

The early Temari11–20 excerpts sit near −17.7 to −17.9 LUFS, while later host/support excerpts commonly sit near −21 to −22 LUFS. Recording/mix differences and dialogue composition are sufficient confounds; these values do not establish that Rinha becomes quieter, more vulnerable or less severe. The support01 LRA of 12.2 LU spans reflection, recalled characters and the fan encounter. It cannot be assigned to Rinha’s vocal dynamics alone. No sample of isolated Rinha speech was certified, so no F0, jitter, shimmer, timbre or imitation-fidelity result is claimed.

The WAV-to-metrics parent SHA, decoded-PCM SHA and original-source interval were checked for all 18 excerpts. A derivative-relative zero maps back to its recorded source start, not to zero on the compilation. Technical audio equivalence does not prove audiovisual synchronization, performer identity or perceptual equivalence between different editions. [Machine-readable measurements](SUPPORTING_DATA/mix_measurements.json) retain these distinctions.

## Evidence confidence and gate accounting

| Responsibility | Result | Confidence / ceiling |
| --- | --- | --- |
| Media inventory | 12/12 physical files identified; video stream 0 and stereo audio stream 1 present | Byte identity/probe result verified; embedded uploader provenance labeled |
| Target-to-source mapping | 18/18 matched by Japanese scene/caption anchors | High for scene identity; no full word alignment or exact edit boundaries |
| Japanese text | 18/18 fetched A1 objects match retained Source Lock archive bytes | High; A1 wording authority preserved |
| Corpus speaker recount | 43 exact-name A1 files = 620 A2 entries | High; one fan-prefix false positive corrected |
| Visual evidence | 538 distinct inspected frame points, including controls | High for observable objects/poses at those points; bounded inference for affect |
| Acoustic computation | 18/18 selected final mixes; decoded-sample preservation verified | High for the stated measurement method; no actor isolation |
| Direct listening / continuous motion | 0 seconds / 0 seconds | Unperformed; all tone/motion-dependent ceilings remain open |
| Dossier and Phase 6 | Not finalized / IN PROGRESS | Required perceptual discrimination has not been satisfied |
