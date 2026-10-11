---
series: WUWA
character: Brant
artifact_type: speech_and_machine_voice_profile_pre_av
scope: BRANT_PINNED_3_6_0_TEXT_AUDIO_PRE_AV
analysis_generation: BRANT_PRE_AV_V0_1
status: draft_noncurrent
release_state: author_working_draft_pending_owner_review
source_commit: 353f2eaed119bc9f680eab92807d20ac75a79b40
source_generation: arikatsu-3.6.0-353f2eae-expanded-v0.3.0-ko
source_generation_frozen: true
source_freeze_metadata: conflicting_collection_and_embedded_lock_fields
text_authority: zh-Hans
localization_witnesses: [en, ja, ko]
supersedes: []
superseded_by: []
do_not_use_as_current_authority: true
---

# Brant — speech and machine voice, before listening

This is a text-register analysis and a native-audio integrity/signal census. **No human four-dub listening, actor-performance annotation or runtime audiovisual review has occurred.** The Chinese text is the semantic anchor; localization witnesses can choose different metaphors, lengths and idioms. Do not compare raw written-unit rates across scripts as if they were phonetic syllables.

## Textual registers and switches

| Situation | Supported construction | Evidence and limit |
|---|---|---|
| Stage or public welcome | Hails the audience, offers a role, applauds and frames episodes as scenes; he readily uses captain/sea/stage imagery. | `FavorStory_120601_Content`; `FavorWord_120603`, `_120621`; `flow#/4220/3`. Lines that dramatize a tale are not factual testimony. |
| Emergency command | Shorter navigation/danger imperatives interrupt the flourish; a credible commander takes over when fog or storm threatens. | `flow#/4220/3`; `FavorStory_120604_Content`; Benir's in-world storm note. Text alone does not prove audible tempo or volume. |
| Rehearsal direction | Explains theme, movement, rapport and audience-responsive improvisation; gives other artists room. | `flow#/4385/1`; `11366–11367`. “No scripts” cannot be reduced to zero preparation. |
| Protected private memory | Slows conceptually to names, losses, box, family home and unfinished piano; explicitly distinguishes a captain's composed face from fear/sorrow. | `FavorStory_120603`, `_120605`; `flow#/4381/2`. Describing text as soft-spoken would require listening. |
| Ethical disagreement | Names concrete crew obligations and choice, rather than merely repeating “freedom”; can condemn the person who makes others pay. | `flow#/5248/5/7–9`; `5357/3/2–10`. EN adds a *tricking* accusation to the broader ZH/JA/KO cost-transfer line. Do not normalize his and Aldric's stances into identical treasure-hunting or derive Aldric's reported end from one spoken dub; the quest synopsis is a separate textual source. |
| Playful wager versus treasure warning | Accepts a fish-bet chore burden and leaves the day helm optional; later interprets a scale painting and quotes a curse/exchange inscription with conditional cost language. | `flow#/5236/3`; `6281/6–6283/2`. The first has two choice forks, the painting three; the inscription is a local quotation, not a verified magic law. ZH/JA/KO `Character_Brant_65_10` counsel currents and winds while EN requires an offering to the sea. The later honorary title is not permanent operational command. |
| Personal appraisal | Cartethyia is person-not-label; Zani is herself; Roccia has professional authority; Rover earns leadership respect. | `FavorWord_120613–120616_Content`; `flow#/5357/3`. Each addressee has a different information state. |
| Public civic challenge | Conditional questions about a god and punishment culminate in a commitment to freely chosen lives; this is an argument, not a direct metaphysical report. | `flow#/4384/2/34–37`; `Main_Linaxita_2_3_39_57` has a Laurel/miracle test in ZH/KO, compressed EN wording and a different unpunished-evil premise in JA. The four voiced turns are in a shared final graph unit, but delivery remains unheard. |
| Rank-up rally | Stage opening, sails, port turn, wave-as-show and friend invitation compress progress into nautical spectacle. | `FavorWord_120626–120630_Content`. EN II makes the unwarranted stronger “storm-proof and unstoppable” assertion; JA IV changes a prospective wave challenge into one already crossed. These are menu addresses, not dated voyages. |

Brant's frequent hails, invitations, second-person friendship language and theatrical metaphors can be adapted as *register resources*, not pasted into every line. A private scene may still have humor. A crisis may still have a turn of phrase. Stage narration about Rover and Carlotta (`flow#/4386–4387`) must be labeled as play-within-story. Unresolved anonymous quotation at `8842/4` cannot become evidence of Brant's personal diction just because it sounds theatrical.

The additional 42-line wager/exchange/honorary-title cohort has 168 language-labeled associations and 168 distinct PCM-valid objects within the 606-line selected total. Those exact joins support future line-level listening, but their numeric event/media fields are paired null under the external-source binding. They do not establish an event→bank chain, performance of every optional reply on one route, or an audible distinction between Brant's teasing and warning. A text-level difference such as EN's sea-offering line should first be aligned to exact localized subtitles and sound objects; a whole-object pitch or duration average cannot decide which exchange theory Brant believes [BRA-E41–E43; C37–C39].

## Whole selected audio census

The private `AUDIO_MEASUREMENT_SUMMARY.json` records 2,324 distinct native FLAC/PCM objects from 2,328 runtime rows and 2,432 semantic render associations, tied to 606 semantic lines. All 2,324 passed local integrity/decoding and waveform measurement; zero failed. Four repeated PCM manifest rows are reuse/duplication, not new performances. These numbers describe the *selected corpus*, not all installed game versions or every possible Brant line. Ninety-two accepted direct occurrences are source-unvoiced.

| Dub | Unique measured objects | Median object duration | Qualified F0 median | Median active-frame energy |
|---|---:|---:|---:|---:|
| EN | 604 | 5.097 s | 169.75 Hz | -23.67 dBFS |
| JA | 604 | 5.546 s | 188.51 Hz | -22.68 dBFS |
| KO | 600 | 4.697 s | 178.06 Hz | -23.74 dBFS |
| ZH | 600 | 4.578 s | 177.52 Hz | -23.23 dBFS |

The analyzer used native FLAC/PCM hashes, a 16 kHz analysis copy, 20 ms energy windows, Praat autocorrelation via Parselmouth and sensitivity checks; it did not downmix all channels into an asserted isolated voice. The local summary flags 70 objects with frequent pitch-edge estimates, five pitch-parameter-sensitive objects, one with fewer than ten voiced frames, four multichannel objects, two long objects needing subtitle-extent checks, two with full-scale samples (not proof of audible clipping), and one very short object. Those are QC prompts, not defect counts or emotional labels. F0 and dBFS are recording/estimator quantities shaped by language, performance, signal chain and mixtures; no cross-dub vocal timbre ranking follows from the table.

The language columns are *memberships*, not disjoint object partitions. EN and JA each have 604 unique measured objects; ZH and KO each have 600. Their sum is 2,408 memberships but only 2,324 unique PCM objects: 28 objects occur in all four language collections, adding 84 memberships. The measurement result is therefore not a claim of 2,408 independent recordings. The four multichannel and other flagged objects require separate perceptual/source checks before a voice-only comparison.

## Source-defined scene-cohort audit and a failed simple stage/offstage inference

A private metadata-only audit at `_research/character_packets/Brant/audio_work/BRANT_SOURCE_COHORT_AUDIT.json` was derived from the pinned `COMPLETE_VOICE_LINE_ANALYSIS.jsonl` and `AUDIO_OBJECT_MEASUREMENTS.jsonl`. It joins each exact semantic occurrence to all four language render identities and the canonical PCM hash, checks the existing native PCM/FLAC integrity result, deduplicates objects within each language/cohort, and excludes ambiguous distinct takes from line-paired comparisons. It does not read, duplicate or publish media. The three primary groups below are disjoint; the seven groups stored in the private JSON also include action-level splits, so their counts must not be summed together.

| Source-defined group | Exact actions | Semantic lines / four-dub render associations | Qualified F0 median, ZH / EN / JA / KO (Hz) | Paired JA minus ZH median active-frame level at −45 dBFS |
|---|---|---:|---|---:|
| Opening and rehearsal | `flow#/4220/3`, `4385/1` | 35 / 140 | 170.1 / 173.8 / 204.9 / 168.2 | +2.25 dB; JA lower on 1/35 pairs |
| Island history | `flow#/4381/2` | 24 / 96 | 136.6 / 146.3 / 153.7 / 149.5 | −0.21 dB; JA lower on 14/24 pairs |
| Later cost discussions | `flow#/5248/5`, `5357/3` | 45 / 180 | 139.7 / 141.8 / 160.4 / 153.6 | +0.68 dB; JA lower on 18/45 pairs |

These groups cover 104 distinct selected semantic lines and 416 render associations, all with measured, integrity-valid mono objects and no missing render. For the later-cost group, F0 eligibility is 43/45 ZH, 43/45 EN, 45/45 JA and 44/45 KO; pitch-edge flags account for the exclusions. In the other two groups all objects pass the stated F0 gate. The auditor uses the existing analyzer's 16 kHz highest-RMS-channel copy, 20 ms energy windows and Praat autocorrelation. Its paired level comparison requires exactly one distinct PCM per semantic occurrence per language; a repeated association to the *same* PCM is not a new take. It reports no distinct-variant exclusions for these groups. It tests three silence thresholds (−50/−45/−40 dBFS); changing −50 to −40 reduces median active duration by roughly 0.30–0.63 seconds across these source/language slices. Neither threshold is a forced subtitle alignment.

The opening group's higher median F0 in each dub is a **candidate for listening**, not proof of a theatrical persona that switches off in private. `4220/3` contains sea-fog danger and short helm commands as well as flamboyant introduction; `4385/1` is a rehearsal explanation. `4381/2` combines reassurance to Morrias with past crew/island history. The later-cost composite also hides heterogeneity: its `5248/5` Aldric-chase action has ZH median qualified F0 164.9 Hz, while `5357/3` Drake-aftermath has 131.7 Hz. Sentence lengths, phonetic content, narrative period, stress, recording and mixing can all move an object-level median. The JA–ZH level offset is stronger in the opening (median +2.99 dB on 27 line pairs) than in island history (−0.21 dB on 24); this is a scene/locale-associated signal difference, not a demonstrated actor decision, emotional state or stable dub quality ranking. A hypothesis that Brant always has a single loud/high “stage voice” and low “true voice” does not survive these mixed source actions without within-language, text-aware, human-audited contrasts.

The private report pins line, measurement, summary and analyzer SHA-256 hashes. A byte-for-byte rerun gave the same report hash (`51AD37CA6742A12C89E8946D8A114DA64947F664A4D29985FCA400424361D607`); a deliberately nonexistent action address was rejected before an output artifact was written. This establishes reproducibility of the *selected audit*, not representative performance across all 606 lines. Next useful evidence would be matched four-dub listening of the exact opening/helm, Morrias/history and Aldric/Drake turns, checking channel content and subtitle extent before attributing a delivery change to the character.

The [23 exact matched cases](AUDIO_MATCHED_SEMANTIC_CASES.json) each retain occurrence ID, text witness hashes, render variant ID, event/media identity, source virtual path and WEM/PCM/FLAC hashes. They sample stage/offstage self, money, character judgments, rescue, duty, Aldric, religious freedom and all five rank-up addresses. Earlier added four-dub cases isolate transferred cost, Aldric's textual aftermath, Drake's earlier coin-bearer and Brant's uncertain map bargain. Forty-eight of 92 selected renders lack event and numeric-media IDs, so their exact external-source identities do not establish an event/bank chain; all twenty new ascension renders retain both IDs, without independently supplying bank proof. These cases are metadata-only; neither a friendly filename nor aggregate pitch is used to identify a line. A human performance pass should listen to all four dubs in at least matched stage, emergency, grief, private/home, disagreement and rank-up cases, then expand by claim rather than declaring twenty-three lines representative of 606.
