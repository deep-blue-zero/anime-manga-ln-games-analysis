---
series: LYCORIS_RECOIL
generation: V2
artifact_type: reconciliation_coverage
source_boundary: TV E01-E13 only
analytical_base: b84f1da3812dadf64e62491f5e64bca4f3ea6500
---

# Coverage, clock and provenance

The transfer is the local `_analysis_work/gemini_independent_continuous_av_v1` directory under the Lycoris_Recoil extraction root. The Japanese TV hardsubs, corrected ASS, screenshot bundles and extracted audio remain in the extraction workspace. The archive’s authority declaration is `DRAFT_NONCURRENT`. Main at `b84f1da3812dadf64e62491f5e64bca4f3ea6500` supplies the published V2 comparison.

## Complete delivery inventory

Boundary control used names, sizes and archive-directory metadata for the entire delivery. Only TV material was eligible for analytical intake. The mixed final retrospectives and six short readings were excluded. Scratch files are supporting derivatives. The principal analytical witnesses are the 13 TV readings, 78 specialist/adjudication files, seven recovered pre-Shorts ledgers and two TV-boundary documents.

| Delivery location | Files | Bytes |
|---|---:|---:|
| 00_governance_and_inventory | 3 | 113974 |
| 01_unit_readings | 19 | 966316 |
| 02_specialist_and_review_records | 114 | 5416444 |
| 03_cumulative_ledgers | 7 | 612989 |
| 04_tv_boundary_freeze | 3 | 50688 |
| 05_full_corpus_synthesis | 4 | 86352 |
| 06_handoff | 3 | 81201 |
| RUN_INDEX.md | 1 | 11538 |
| gemini_independent_continuous_av_v1.zip | 1 | 2980729 |
| scratch | 12038 | 61761715901 |

12,193 files. Reproducible metadata inventory SHA-256 `c1df3eb5d38a82c7da90da3bd5f1be313da845bfca03f83e0373f0c75ac3ea6d` (UTF-8, ordinal sort of relative forward-slash path, tab, decimal size and LF). The ZIP central directory has 181 entries including directories. ZIP SHA-256 `d4ece808d0432833e9eb604feada7d6c98aeaa2ad6a59d4bb2f59dfccbea6dd6`. The ZIP is a packaged handoff with its own scope. The directory retains scratch media separately.

## Integrity at the TV boundary

TV snapshot `04_tv_boundary_freeze/TV_BOUNDARY_SNAPSHOT_HASHES.json`, SHA-256 `ba9a2cc47e1c6a923fa105ce29f2b3e930b4683c08ef7d8db12380e791ee43c1`. The independent reviewer verified all 103 snapshot content identities. Ninety-four current files directly match. Later run bookkeeping altered the two source manifests and seven cumulative ledgers. All nine TV versions were reproduced in memory and matched the lengths and SHA-256 values in the pre-Shorts snapshot. The receiver used the TV prefixes only.

For a ledger, normalize CRLF to LF, restore the first YAML high-water mark from `S00E06_COMPLETE` to `E13_COMPLETE`, slice to the frozen byte count and require the frozen digest before decoding. For the JSON source manifest, restore the E13 high-water mark and initial inventory-only records for the six excluded units, including their pending inspection state. Preserve the TV records. Serializing with two-space indentation, UTF-8, CRLF and no final newline reproduces `abb95d117bea057b16e76441380ff0ad8e8a22c971e7e587b83704ddca31b97e`. Rendering its Markdown table with the supplied renderer and final CRLF reproduces `4a43e6e4681cbeaaa4be0ed13979d042d860d42e65be899253850170ff8ab724`.

| Recovered TV ledger | Bytes | Frozen SHA-256 |
|---|---:|---|
| CHARACTER_STATE_HISTORY | 98547 | `18c20d7bc10d8f60f655ba5cf6aa26f9ed69bddb212d81fa0ee3eaeba728cf9e` |
| CHRONOLOGY_DISCLOSURE_CAUSALITY | 59358 | `3efe43c0960314d1c1cea0de614d02312d55534674e7787da53d16e7b33f38f4` |
| CLAIM_AND_ADJUDICATION_LEDGER | 76594 | `e3cf6ffabb49e3d2f2e82ede70172be5108d7ab2962199b6875a7c0af2ddff87` |
| INSTITUTIONAL_AND_WORLD_STATE | 46724 | `bdad4fc37d17e0210e77af62bb04b8d3f8ab2a3e6ddad3d6afe2c67cf203f8f4` |
| RELATIONSHIP_STATE_HISTORY | 70002 | `32696e006c90cb9f12448695b376c8c654cd1ce01bea0b36828f1eb88172362d` |
| SPEECH_AND_MOTIF_LEDGER | 73271 | `da1d0d37328be298e2ee82da5e08208f742c2ec4ecf05f576633133c9f56989f` |
| UNRESOLVED_EVIDENCE_REGISTER | 91632 | `e690eb8588f3d1d343b94085c416b868b7fc29fa9ae5e5bab2475f7f5cd44da8` |

## Source and precision

The source clock is the zero-origin hardsub MKV. The manifest identifies 1920×1080 HEVC at 24000/1001 fps and Japanese stereo 48 kHz Opus. The hardsub carries burned text. The embedded ASS stream belongs to the prepared companion. Float32 and 16-bit PCM refer to decodes. The extracted ASS exists for every TV episode despite its null manifest field. Extracted, analysis and bundle-selected ASS bytes agree for all 13. Corrected ASS agrees after line-ending and BOM normalization. No local English subtitle witness was admitted.

Gemini reports eight overlapping MP4 derivatives per episode, 1 fps effective visual sampling and synchronized audio, with targeted higher-rate sheets and stills. A pass on a 45-second E01 probe is evidence about that route. It cannot certify that a particular later observation was correctly interpreted. Native-looking millisecond timestamps may denote a caption edge, sampled frame PTS, a tool window or the peak of a mix. Each bounds a different claim. Typical navigation tolerance is ±0.5 s. A 6/12 fps sheet samples about 167/83 ms apart. Native picture steps are about 41.7 ms. Acoustic sample indices can be much finer.

Codex inspection was bundle/text mediated with selected primary frames and deterministic measurements. No receiver watched or heard the TV series in continuous synchronized playback. All 104 clip byte counts and SHA-256 receipts match. Intervals start at zero, overlap by about 5.017–5.018 s, and have no internal gap. Final derivative containers end 6–7 ms short of the respective source-container durations. A claim of gapless perception would exceed this check.

| Episode | MKV bytes / duration (s) | MKV SHA-256 | Japanese cues / bundle rows | Bundle cue anchors at beginning, middle and end (Gemini → bundle @ clock) | Claims / F2 |
|---|---|---|---|---|---|
| E01 | 470297950 / 1442.04 | `495b91dba248e32200e500daed6bddce66473252d9c6c181aebbfd6c250e5950` | 550 / 549 | C0001→1 @ 00:01.69, C0276→275 @ 11:01.52, C0550→549 @ 23:58.29 | 8 / 14 |
| E02 | 532234712 / 1442.049 | `8010992a7795c47a29fb86a467e9852e9cabf70800f216e2d0fc5c9e220615b2` | 464 / 464 | C0001→1 @ 00:02.44, C0233→233 @ 12:30.94, C0464→464 @ 23:58.33 | 8 / 11 |
| E03 | 549193645 / 1442.032 | `0cb2dd474c7ba8a8fa1d702e3f0e8172381f78a4b59c93b7305b7636bd860df4` | 475 / 475 | C0001→1 @ 00:02.40, C0238→238 @ 11:53.32, C0475→475 @ 23:58.38 | 9 / 9 |
| E04 | 557679357 / 1442.073 | `4742a4ad6918c9a1065b50da7d78af98c0eb79469c6e5f29f660e1e892bb3877` | 452 / 452 | C0001→1 @ 00:01.44, C0227→227 @ 11:43.06, C0452→452 @ 23:56.04 | 9 / 8 |
| E05 | 616087010 / 1442.031 | `edd8ba3f87a5b0e94a836635d5a462a2538e0d6325f9096ff34087ec292830e7` | 429 / 429 | C0001→1 @ 00:01.65, C0215→215 @ 12:17.05, C0429→429 @ 23:58.46 | 9 / 9 |
| E06 | 525828484 / 1442.073 | `e998e2409da245fd03bd0b94fbe1f62f3f87de0b9f69becb409fdabc13fba5e2` | 491 / 491 | C0001→1 @ 00:07.65, C0246→246 @ 12:35.65, C0491→491 @ 23:58.29 | 9 / 8 |
| E07 | 499003330 / 1442.071 | `24212b2375856a728c62ad643e83f12b04878e06d3f840db47fb5818f8213358` | 475 / 475 | C0001→1 @ 00:01.57, C0238→238 @ 11:25.50, C0475→475 @ 23:46.32 | 9 / 8 |
| E08 | 430631454 / 1442.04 | `707e1ba464fd1b3af9878290b3c13ed163cd7ba71aa66a2c7d7fedf38fff5d20` | 470 / 470 | C0001→1 @ 00:08.84, C0236→236 @ 11:29.90, C0470→470 @ 23:58.35 | 9 / 9 |
| E09 | 426467390 / 1442.071 | `91f1d9e8b6f9a07f056beceb6a138599b3f1a095e4143bed6db3e0b28e583d83` | 396 / 396 | C0001→1 @ 00:03.90, C0199→199 @ 11:50.23, C0396→396 @ 23:58.67 | 9 / 7 |
| E10 | 440048681 / 1442.073 | `077339d1d447cede6f4e41d03e0e21e04030d74a8b886c20627fb5260f00d295` | 445 / 445 | C0001→1 @ 00:02.06, C0223→223 @ 11:41.34, C0445→445 @ 23:58.41 | 9 / 9 |
| E11 | 636370540 / 1442.031 | `29c5532e9abe8699c073432cc0f609aa88bc49c682570ee20b56c3745bffeda5` | 439 / 439 | C0001→1 @ 00:05.99, C0220→220 @ 12:04.08, C0439→439 @ 23:58.38 | 9 / 12 |
| E12 | 564373179 / 1442.04 | `ff47f4b4c36ca70c05355efc0c6f9c67d583efce79c231de2ba95386df19197f` | 482 / 482 | C0001→1 @ 00:01.61, C0242→242 @ 12:43.91, C0482→482 @ 23:58.50 | 10 / 8 |
| E13 | 534379463 / 1441.986 | `4b5a4052bba4afae6c7aa1bf1507532975d66de62be70f15900a936222a42933` | 486 / 486 | C0001→1 @ 00:03.53, C0244→244 @ 11:06.52, C0486→486 @ 23:59.17 | 10 / 9 |

The receiver matched start **and** end against the original bundle dialogue index for all 6,054 ASS events. Bundle-selected subtitles matched the analysis ASS byte-for-byte. E01 C0009 and C0010 occupy the same 00:21.17–00:21.96 interval. The bundle has 549 dialogue rows to the ASS’s 550 events. Bundle row 9 retains the news text (ASS C0009). Its paired-text field is empty. The ringtone and Chisato’s response (ASS C0010) remain in the selected ASS and have no independent dialogue-index row. C0001–0009 keep their numbers. For C0011–0550 subtract one to obtain the bundle cue number. Use timestamp and text for that overlap. Across the TV run there are 6,053 bundle rows. These are cross-object navigation anchors. They do not measure performer onset or response latency. Some E01 early derivative overlays have a reported five-second offset. Use the clip ledger’s source start plus elapsed time, or go directly to the MKV.

The manifest’s build-time subtitle corrections (including E03 −0.04 s and E08 +0.02 s), a per-unit observer’s zero-drift declaration and a receiver match between subtitle clocks are three different results. Nine TV manifest inventory records retain a pending direct-calibration field (E03–E10 and E13). The corresponding episode language reports give completed observer checks. Neither overrides the measured cue mapping or certifies audiovisual synchrony to a frame.

## Review record and coverage by channel

Gemini A integrated each unit, B covered image, movement and editing, C covered sound and voice, D covered character and ethics, E tested Japanese dialogue, and F supplied blind-first challenge and post-draft review. Specialist disagreement is retained. The critics shared source objects and methods, which limits their independence as witnesses. Gemini’s initial separation from published V2 is a producer attestation. Codex range reviewers knew the V2 and Gemini claims. They worked independently of each other and did not claim blind-first viewing.

| Channel | Producer coverage | Receiver inspection | Residual obligation |
|---|---|---|---|
| Motion, blocking and camera | Sequential 1 fps with targeted 4–12 fps or native stills as identified per unit | PARTIAL · specific source stills and shot changes | Fine trajectories, eye order, first initiative and intended action require the targeted packet where consequential. |
| Speech, response and microbehavior | Japanese audio plus subtitles and selected WAV reviews | COMPLETE for matching TV subtitle clocks, PARTIAL for specific phrasing and acoustic windows | Layer-C phonetics, private affect and voice onset remain open where requested. |
| Editing, sound-image and music | Unit reports, mix measurements, higher-rate cut checks and cue comparisons | PARTIAL · selected stereo, fade, transient and waveform tests | Preserve individual onset conventions and the production-convention rival. |
| Story, institution, character and relationship | Sealed readings, seven TV ledgers and TV synthesis | Reviewed against the frozen episodes, character, relationship and V1 revision ledgers, prediction horizon and locator index | Mainline changes use the bounded formulation in the matrix. Untested V2 claims accrue no confirmation. |

## Specialist challenge index

Each item gives the episode-local F2 number and the exact line in `02_specialist_and_review_records/E##/adjudication.md`. Its title identifies the issue checked. The cited row preserves the producer’s disposition, specialist alternatives and supporting witness. These are incoming review records. The project decisions appear separately in the matrix and disputes register. Minor illustration details, chapter-pointer repairs and paratext quarantines have no independent character-model consequence. The thirteen sets contain **121** distinct F2 challenges. The TV audit’s reported total of 120 is an arithmetic error. Its 117 sealed claims are all indexed. Earlier-stage errata and corrections remain retrievable from the six files per episode.

**E01** · 01 (L28) Hibana’s printed surname · 02 (L29) opening montage roles · 03 (L30) occluded spatial detail · 04 (L31) Takina's uniform accessories · 05 (L32) road sign · 06 (L33) shop lettering and visible contact · 07 (L34) Cleaner identity and paratext · 08 (L35) Erika’s request versus Saori’s exposure · 09 (L36) ending-song lead arithmetic · 10 (L37) score masking the impacts · 11 (L38) Walnut's apparent fate · 12 (L39) motion before versus after a cut · 13 (L40) multiple explanations for an exhale · 14 (L41) comfort and speech-register exceptions

**E02** · 01 (L35) music measurement during speech · 02 (L36) unanswered Russia question · 03 (L37) broken section references · 04 (L38) intent needs an inference label · 05 (L39) what Yoshimatsu newly learns · 06 (L40) exterior insert limits visible event count · 07 (L41) prop finish · 08 (L42) doorway arrivals separated by an eighth of a second · 09 (L43) glare on station clock · 10 (L44) testing versus teasing · 11 (L45) credit names outside narrative evidence

**E03** · 01 (L16) speech masks score dropout · 02 (L17) no exact comparison of blow loudness · 03 (L18) water and towel noise under voice · 04 (L19) body laterality · 05 (L20) Takina unwraps the sweet herself · 06 (L21) held versus holstered prop · 07 (L22) audio-specialist errata · 08 (L23) character-specialist errata · 09 (L24) spoken and displayed names

**E04** · 01 (L27) pendant remains in hand · 02 (L28) Saori’s photograph versus CCTV · 03 (L29) written and spoken forms of names · 04 (L30) discrepant public times · 05 (L31) short effects and threshold metrics · 06 (L32) occlusion and tower identity · 07 (L33) language and prop errata · 08 (L34) group count and source horizon

**E05** · 01 (L30) request-form heading · 02 (L31) wheelchair impact location · 03 (L32) quiet interval and piano entry · 04 (L33) confinement versus visible binding · 05 (L34) seasonal date inference · 06 (L35) placeholder screen text · 07 (L36) earlier spoken surname · 08 (L37) two chimes in the hold · 09 (L38) brief shots interrupting the news

**E06** · 01 (L29) clinic bandage side · 02 (L30) hand laterality · 03 (L31) missing bandage is a drawing inconsistency · 04 (L32) breath precedes music · 05 (L33) vehicle and monitor counts · 06 (L34) digital floor versus near-silence · 07 (L35) organizational chart lettering · 08 (L36) prospective limits

**E07** · 01 (L38) invented trend in credit-song timing · 02 (L39) earlier familiar forms of address · 03 (L40) apparent glass hand-switch · 04 (L41) overlapped whisper · 05 (L42) voice loudness under score and hum · 06 (L43) computer case orientation · 07 (L44) reused display text · 08 (L45) remaining continuity checks

**E08** · 01 (L38) whole-image fade · 02 (L39) doorway occlusion · 03 (L40) decay versus mathematical zero · 04 (L41) frequency of the eyecatch tone · 05 (L42) timer display units · 06 (L43) voice and stillness at the bench · 07 (L44) earlier ending-song durations · 08 (L45) pronunciation and visible skin · 09 (L46) timestamp correction and limited knowledge

**E09** · 01 (L43) first direct address versus first naming · 02 (L44) beep contaminated by speech · 03 (L45) metallic color and inferred composition · 04 (L46) status of earlier tower testimony · 05 (L47) spoken versus written sentence ending · 06 (L48) caption-only surname · 07 (L49) piano entry and sneeze setup

**E10** · 01 (L42) mistaken identification of background cadet · 02 (L43) occlusion limits inferred intention · 03 (L44) captioned exhale · 04 (L45) flinch versus visible wound · 05 (L46) score fade versus room-tone interval · 06 (L47) Abe’s visual identification · 07 (L48) phone-channel separation · 08 (L49) siren before PA speech · 09 (L50) case resemblance without contents

**E11** · 01 (L43) fabricated earlier ending-song timings · 02 (L44) reading a printed name · 03 (L45) overlapping action and impact counts · 04 (L46) already resolved medical-status question · 05 (L47) two impacts and door kick · 06 (L48) screen lettering · 07 (L49) masked broadcast predicate · 08 (L50) hair versus visible skin injury · 09 (L51) satchel impacts and concealed action · 10 (L52) corroboration versus origin of ability · 11 (L53) drone marking · 12 (L54) preceding daylight exchange and timing

**E12** · 01 (L45) vocal attribution before the wound · 02 (L46) laterality under occlusion · 03 (L47) decay ramp versus final trough · 04 (L48) missing open threads · 05 (L49) credit cut frame · 06 (L50) specialist attribution · 07 (L51) contact and coda chronology · 08 (L52) flashback cue and peak notation

**E13** · 01 (L44) duration of tower-window highlight · 02 (L45) social-photo location badge · 03 (L46) partially legible drink label · 04 (L47) phone display before and after touch · 05 (L48) can lettering · 06 (L49) fireworks stereo and transient levels · 07 (L50) first initiative in the island exchange · 08 (L51) closed box and inferred contents · 09 (L52) unresolved institutional knowledge
