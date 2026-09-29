---
series: WUWA
character: Augusta
artifact_type: speech_and_machine_voice_profile
scope: AUGUSTA_PINNED_3_6_0_TEXT_AUDIO_PRE_AV
analysis_generation: AUGUSTA_PRE_AV_V0_1
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

# Augusta — textual speech and measured audio, pre-AV

The pinned scripts support speech *acts and registers*; the local client-derived FLACs support source/render identity and signal measurements. Human four-dub listening and runtime gesture inspection have **not** been done for this packet, so no claim about enacted tenderness, authority, accent, actor intention or emotional pitch is made here. Some central reflective scenes are source-unvoiced.

## Textual registers

| Register | Anchors | Action and limit |
|---|---|---|
| Ephor's ceremonial challenge | `FavorWord_130622–130624_Content`; `flow#/8363/3/0–7` | Uses title, honor, direct contest and martial respect. This is public/first-encounter framing, not every private sentence. |
| Political confrontation | `flow#/8797/4/5–12`; `FavorWord_130630_Content` | Addresses senators' use of tradition and rank, with forceful invitation to accountability; later concedes governance requires learning balance. Do not write all policy as a duel. |
| Comradely trust | `FavorWord_130601–130605_Content`; `flow#/8363/3/34–36`; `8422/2/26–31` | Explicit friendship, trust, apology, thanks, and a non-totalizing view of titles. Optional responses can change immediate sequence. |
| Prophecy argument | `flow#/7804/4/3–22`; `8797/4/37–51` | Differentiates foresight as aid from passive submission to fate; presses Iuno with concrete existential questions. This is not blanket anti-priestess speech. |
| Memory conflict | `flow#/7741/5/3–37` | Reports a lack of Iuno-memory while seeking physical traces and naming possible distortion. Do not treat her doubts as stable contempt. |
| Quiet private reflection | `FavorStory_130605_Content`; `FavorWord_130631_Content`; `flow#/11364/2` | Wonders about a future beyond the hero climax, can share a walk, reminisce or spar. `11364` is textually present but source-unvoiced in this selected corpus. |
| Ascension-menu reflection | `FavorWord_130627–130631_Content` | Sword purpose, homeland roots, solar vigilance, institutional reform and imagined old age; five progression addresses are not a dated policy meeting or completed retirement. |
| Combat, damage and traversal dispatch | Raw `favorword#/2506–2539`, `#/2620–2622`; actual keys in the [combat crosswalk](WUWA_AUGUSTA_COMBAT_TRIGGER_AND_ARCHIVE_KEY_IDENTITY_PROFILE.md) | Short boasts, commands, ally address, pain/fallen cries and reward remarks are trigger-conditioned. They are not interchangeable with a considered civic position or a fixed addressee. |

Translation needs line-specific alignment. Chinese `英雄王` is the semantic title anchor, while EN “Hero of Heroes” conveys a different surface rhythm; neither should be mechanically back-projected into every language's prosody. The arena choice in `FavorStory_130602_Content` explicitly distinguishes last standing from killing. In `FavorStory_130604_Content`, the poisoned death is reported through competing voices, not a single narrated culprit. A role model that carries a confident English paraphrase but loses these Chinese distinctions would not be faithful.

At `flow#/7804/4/6`, ZH `鬣狗`, JA `ハイエナ` and KO `하이에나` name a **hyena** being tamed into a rabbit; EN substitutes a **wolf**. The supported source concept is fate eroding untamed agency, not a stable wolf emblem for Augusta. This fork matters when using the line to construct her own metaphorical speech. The same action begins with technical speaker `178` at item 0, contextually accepted as Augusta because the address to Iuno immediately continues as her first-person recollection; the technical ID alone is not the attribution proof.

Three ascension contrasts materially affect interpretation. The sun line (`FavorWord_130629_Content`) is more exclusive/necessary in ZH/EN/KO, while JA makes darkness's retreat conditional on the sun continuing to shine. In `FavorWord_130630_Content`, ZH/EN/JA warn about destructive power *under* corrupt rules, whereas KO calls it a weapon *against* those rules; all still say reform and balance require learning. Ascension V (`FavorWord_130631_Content`) makes an arena return a stronger conditional preference in EN than the more speculative or attached ZH/JA/KO forms. None of these written differences establishes how an actor delivered the line, a settled political platform, or a chosen retirement [AUG-E28–E29, C26–C28].

The separate combat-dispatch family has a stronger provenance issue than those five ascension addresses. Thirty-seven raw favor IDs at `favorword#/2506–2539` and `#/2620–2622` do **not** match their actual Content-key suffixes. They have 148 complete four-dub local PCM/FLAC renders, but these objects are not a 148-line dramatic speech or an acoustic counterpart to the 189-line *story-action* cohort below. A raw ID can generate another existing, wrong key: Liberation VII raw `130645` is `_130632_Content`, whereas `_130645_Content` is Intro Skill II. Within the correct lines, EN Liberation I's ruler/winner tautology is not a universal policy claim, and KO Fallen III uses stronger deathward wording than the other witnesses. A future voice study must select by pinned row locator, actual key and trigger, then listen; the complete technical join itself supplies no delivery adjective or canonical failure event [AUG-E33–E34, C29–C30].

## Full selected-scope machine pass

The local pass used Sigrika `audio_tools/analyze_audio.py` version `sigrika-waveform-analysis-0.2.0` (`SHA-256 73c2904c38d06440a86a572d05fa3fe200e23055e68f0aeaec3be75313d3c4a2`) through `scripts/analyze_character_audio.py`. It verified FLAC bytes and canonical native PCM, retained native channel structure, selected the highest-RMS channel for analysis rather than claiming an isolated voice stem, resampled to 16 kHz, applied three 20 ms energy gates, and ran Praat autocorrelation pitch plus sensitivity/quality flags. The full parameters and per-object data remain private at `_research/character_packets/Augusta/audio_work/`.

| Dub | Unique measured PCM/FLAC objects | Median object duration | Qualified F0 objects / median estimate | Median −45 dBFS active-frame energy |
|---|---:|---:|---:|---:|
| EN | 600 | 5.828 s | 586 / 188.6 Hz | −25.13 dBFS |
| JA | 600 | 6.124 s | 587 / 216.6 Hz | −21.67 dBFS |
| KO | 600 | 5.356 s | 585 / 204.0 Hz | −23.91 dBFS |
| ZH | 599 | 5.213 s | 576 / 201.8 Hz | −24.41 dBFS |

All 2,399 distinct objects measured with zero failures. Flags include 18 pitch-parameter-sensitive, 39 edge-band-frequent, 18 with fewer than ten voiced frames, 21 long-object/subtitle-extent checks, and two multichannel-not-isolated-speaker objects. These counts are *not* a ranking of four performances. Written-unit rates are source-text units over object or active duration, not syllable timing or forced alignment. The 2,420 render associations and 2,400 runtime rows are not equal to unique PCM objects. Archive and main-story registers may be recorded under different production conditions, and four-language scripts differ in length and syntax; aggregate F0 or energy cannot substantiate personality.

## Source-defined story-action audit

The [nine-cohort audit](WUWA_AUGUSTA_SOURCE_DEFINED_AUDIO_COHORT_AUDIT.md) selects 189 accepted story occurrences (756 four-dub associations) from exact pinned action/TalkItem addresses. All 756 selected PCM/FLAC objects are distinct and integrity-valid; 751 have pitch estimates that pass the declared quality gates. This is 31.2% of the 605 selected semantic lines and excludes the archive; it is purposive, not a statistical portrait of her voice. The private machine-readable artifact preserves line/render IDs, source locators, hashes, per-object flags and input hashes. A second run was byte-identical, and absent/overlapping exact TalkItem selections failed before output. Neither repeatability nor integrity means a person listened.

The long `8797/4` action must not be treated as one emotional block: its seven voiced Senate-rebuke lines, thirteen friend/logistics lines and sixteen fate/friend-exchange lines have different addressees and purposes. Median qualified F0 in the Senate subset is above the friend subset in ZH (221.4 versus 190.4 Hz), EN (206.4 versus 197.6) and JA (228.5 versus 199.8), but **below** it in KO (208.3 versus 212.0). The Senate subset is not uniformly louder in the four dubs, and its −50-to−40 dBFS gate change in median active duration is 1.10–1.92 seconds, compared with 0.24–0.62 in the friend subset. Seven against thirteen different sentences without listening, within-dub normalization, matched phonetic content or pause alignment cannot establish a public/private acting rule. The contrast instead identifies exact lines for a controlled human comparison.

The item-level exclusion matters too. `flow#/8797/4/46` is a *spoken* claim that she will sever a disastrous fate; item 47 is a separate laugh, whose JA and KO pitch measurements fail the ten-voiced-frame gate. The short refusal `8408/3/19` fails that gate in ZH; item 20 carries the longer bodily-risk objection. The measured Angel report at `8402/4/29–30` proves four-dub audio objects for her *textually bounded testimony*, not the unknown inside-hollow events or Angel's later outcome. The measured `7741/5/12` question asks for an external trace of Iuno; it is not a recording-based proof of illusion. In all these cases, actual performance and scene meaning remain separate evidence channels. The JA-minus-ZH matched-line median active level varies from +0.66 dB for the Senate subset to +4.18 dB for post-victory sharing, a production/text confound rather than a personality scale.

## Eighteen matched retrieval cases

The [metadata case file](AUDIO_MATCHED_SEMANTIC_CASES.json) has 18 semantic occurrences and 72 exact four-language render rows. Ten archive cases cover honesty, non-totalizing titles, the defeated-blade sword, Iuno, Angel and the five ascension addresses; eight voiced story cases sample first martial esteem, prejudice about Forte, credit shared after victory, resistance to a puppet-fate account, the Iuno memory conflict, a declaration against fixed fate, and Augusta's two-line Angel testimony. For each, the artifact preserves source locator, semantic voice ID, runtime variant, event/media IDs where resolved, source virtual path, WEM hash, canonical PCM SHA-256, FLAC SHA-256, duration and QC flags. The four new Ascension I–IV cases add sixteen clean-QC renders with explicit IDs; their durations differ across languages and do not themselves establish political conviction or performance warmth. This is a claim-driven sample, not a statistical stand-in for all 605 lines. A friendly text key alone is insufficient to choose audio. In this sample 32/72 render rows lack explicit event/numeric-media IDs; exact external-source audio identity must not be mislabeled as a proven event→bank chain.

An important negative control is `flow#/11364/2`: its friendly, quiet exchange is present in text, but it is not in the selected voice corpus. An audio profile must not say “she sounds softer in that scene” or map another nearby file to it. Likewise the accepted anonymous entrance at `9509/2/7` is source-unvoiced. Performance annotations should begin with the exact voiced cases above and a separate runtime/source check for any scene audio not in the current semantic mapping.

## Listening and scene review needed

The first four-dub comparison should contrast public `Main_Linaxita_2_9_25_7` with archive friendship `FavorWord_130604_Content`, prophecy resistance `Main_Linaxita_2_10_38_16`, memory conflict `Main_Linaxita_2_10_5_8`, post-victory shared credit `Main_Linaxita_2_9_565_17`, and the paired `Main_Linaxita_2_9_470_35`/`_36` report against `FavorWord_130617_Content`. It should also hear `8797/4/6–11`, `13–23` and `46–47` *as different contexts inside one action*. Annotate pauses, articulation, dynamic arc, overlap and source-text differences *within* each dub before cross-language comparison; record time offsets and uncertainty. The textual distinction between witnessed change and hoped-for later survival does not depend on hearing an emotional delivery. Video should test whether direct visual observations of crown/weapon/pose persist at runtime and whether Iuno/Rover interactions alter physical distance or gesture. Do not infer a single acoustic “royal voice” from group medians.
