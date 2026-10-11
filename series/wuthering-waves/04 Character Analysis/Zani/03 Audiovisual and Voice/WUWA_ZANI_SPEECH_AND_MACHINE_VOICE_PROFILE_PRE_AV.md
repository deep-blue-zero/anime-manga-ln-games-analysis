---
series: WUWA
character: Zani
artifact_type: speech_and_machine_voice_profile
scope: ZANI_PINNED_3_6_0_TEXT_AUDIO_PRE_AV
analysis_generation: ZANI_PRE_AV_V0_1
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

# Zani — textual speech and measured audio, pre-AV

This separates two different claims. The pinned text can support *what she says and how her wording changes by situation*. The official-client FLACs and Sigrika-derived signal pass can support *exact render identity and reproducible acoustic measurements*. No one has yet listened across four dubs for this packet; no emotion, actor intention, dialect or relationship conclusion is inferred from pitch or loudness.

## Textual registers and speaking acts

| Context | Source keys / flow targets | Supported speech behavior | Constraint |
|---|---|---|---|
| Client-facing | `Main_Linaxita_2_1_16_1`, `_4`, `_11`, `_16`, `_18` | Full service formulas, deference to a Montelli guest, structured offer of help, concern about unknown preferences. | First contact should not begin with private-nightwalker intimacy. |
| Staff operations | `4204/2/19–21`; `4577/7`; `11780/2` | Short task assignment, specific insured objects, evidence/reporting and logistical constraints. | “Efficient” does not mean rude to all colleagues. |
| Relaxed with Rover | `Main_Linaxita_2_1_16_41–42`; `FavorWord_150705_Content`; `8586/10` | Relief from formal mode, food invitation, wry acknowledgment of changed routine, invitation to share a view. | Warmth is context-earned, not universal flirtation. |
| Moral challenge | `Character_Zani_29_4`, `_8`; `Character_Zani_59_2`; `Character_Zani_63_23` | Reciprocal-trust demand, responsibility despite coercion, admitted fabricated rule, terse serious threat. | These acts have different targets and stakes. Do not use Talos register on a minor mistake. |
| Missing-person pressure and survivor participation | `Character_Zani_51_1`, `_7–8`, `_10`, `_12–18`, `_20`, `_26`, `_31`, `_33–34`; `flow#/7552/2` | Repeated short demands to a gang member, a firm stay-behind instruction to Colleen, an unequal-risk objection, an overburden warning and eventual concession. | Different addressees and Rover/Colleen turns divide the sequence; do not infer a heard tone, a Zani-inflicted injury or a completed rescue. |
| Anti-legend self-report | `Character_Zani_17_25`, `_37–38`; `Character_Zani_67_3`, `_16`, `_35–38` | Dismisses a grand nickname, admits a past error and reframes success as civic stability and rest. | Her self-account may understate risk; it is not a narrator's exhaustive biography. |
| Private routine / holiday | `FavorWord_150703–150711_Content`; `Event_WWPDJSBF_1_16`, `_23` | Work-value distinctions, food, alarm, fatigue, difficulty using a real paid holiday. | Avoid a one-note “coffee and overtime” parody; she actually prefers sweetness. |
| Ascension-menu addresses | `FavorWord_150727–150731_Content` | Honing/work, a deadpan productivity trap, civic light, protection and a sword/shield offer. | Menu progression is not a dated five-scene conversation or a literal combat capability certificate. |

The Chinese anchor and EN/JA/KO witnesses may choose different forms of address, sentence segmentation, idioms and markup. For example, the welcome `Main_Linaxita_2_1_16_1` carries gender/player-name substitutions and **seven** render variants across four languages, not a simple one-text/one-file assumption. The EN `FavorWord_150703_Content` explicit “purpose” distinction and the Chinese counterpart's meaningful-work condition align semantically, but exact joke timing or register strength across the four performances is not established by text alone. `FavorWord_150714_Content` supports her human-agency position and respect for Phoebe; a line-length comparison cannot establish contempt or tenderness. Translation should preserve *the action of the line* before mirroring any one dub's cadence.

Two targeted four-language hinges now matter for interpretation, not just translation style. At `7297/7/17` (`Character_Zani_10_25`), Chinese, Japanese and Korean explicitly name torture as difficult to use against minor offenders because opponents could exploit the situation; English says “more extreme methods.” Neither wording proves action or desire, but an English-only clean ethical prohibition would be false precision. `FavorWord_150718_Content` plans a traditional birthday party through dawn in Chinese, Japanese and Korean; English changes this to nobody leaving before midnight. The source records a prearranged invitation, not Rover's response or a human-heard party scene. These checks do not amount to exhaustive JA/KO review and cannot certify how any actor delivered the lines [ZAN-E27, E29, C24, C26].

The rest advice in `FavorWord_150704_Content` is another consequential hinge. In ZH/JA/KO she addresses a tired Rover, recommends rest when possible, and compares world-saving to overtime that can expand without end; EN ends with the stronger “saving the world can wait.” This is a textual scope difference, not an observed softer or harsher dub. It supports care and a warning against chronic self-expenditure, but does not record Zani choosing to defer a known immediate rescue. Her evacuation report and offer to work longer for Carlotta complicate a universal retreat rule without proving a specific rest-versus-danger choice or completed extra shift [ZAN-E08, E23–E24, E35, C33]. A later matched listening note should annotate the actually heard advice separately from that ethical inference.

At `7552/2`, the short source lines “tell me” and “stay here” are addressed in different circumstances: the former presses a gang member who refuses missing-person information, the latter initially excludes Colleen from a dangerous search. The later warning about carrying everything alone follows Rover's one-option protection assurance, but its exact addressee is not marked. ZH/EN state an unequal-risk comparison, JA more directly questions taking the danger for that purpose, and KO is less specific. Text supports distinct speaking acts, not a claim that one dub sounds harsher or that her eventual concession was reluctant in performance. The fifteen Zani voice lines in that action join sixty distinct four-dub PCM objects outside the frozen matched-case sample and eight measured action cohorts; this packet has not listened to them [ZAN-E42–E43; C41–C42].

Three ascension addresses add another language-sensitive speaking-act contrast. `FavorWord_150728_Content` frames improved efficiency as threatened loafing in ZH/KO, difficulty acting busy in EN and likely extra work in JA; it does not document an actual missed duty. `FavorWord_150730_Content` makes protection the purpose of greater power in all four witnesses, but only EN names a shield at this point. In `FavorWord_150731_Content`, ZH/KO imagine a sword that can cut anything, EN an unbreakable sword, and JA a powerful one. These are textual differences, not evidence that one dub is more protective in performance or that the menu question received an answer [ZAN-E31–E32, C28–C30].

## Reproducible signal pass

The private run used the published Sigrika `audio_tools/analyze_audio.py` (`sha256:73c2904c38d06440a86a572d05fa3fe200e23055e68f0aeaec3be75313d3c4a2`, version `sigrika-waveform-analysis-0.2.0`) through local `scripts/analyze_character_audio.py`. It verified the FLAC SHA-256 and native interleaved 16-bit PCM payload, analyzed the highest-RMS native channel without a semantic downmix, resampled to 16 kHz with `scipy.signal.resample_poly`, used 20 ms energy gates at −50/−45/−40 dBFS, Praat autocorrelation pitch with a sensitivity comparison, and measured harmonic/spectral descriptors. The exact parameters, Python/platform, source manifest hashes and 3,517 per-object results are restricted locally in `_research/character_packets/Zani/audio_work/`.

| Dub | Distinct measured PCM objects | Median object duration | Qualified F0 objects / median estimate | Median −45 dBFS active-frame energy |
|---|---:|---:|---:|---:|
| EN | 902 | 4.470 s | 897 / 181.9 Hz | −23.22 dBFS |
| JA | 900 | 5.177 s | 891 / 176.4 Hz | −20.99 dBFS |
| KO | 899 | 4.651 s | 898 / 194.6 Hz | −23.36 dBFS |
| ZH | 900 | 4.213 s | 893 / 188.7 Hz | −22.76 dBFS |

All 3,517 unique objects passed local measurement; seven were `pitch_parameter_sensitive`, sixteen `pitch_edge_band_frequent`, and two had fewer than ten voiced frames. This is not four actors' emotional ranking. Dubs differ in scripts, segmentation, performance, mix and recording; object aggregates are not matched utterance controls. F0 qualification only suppresses known unstable estimates, not every source of error. Written-unit rates use language-specific orthographic units per total/active object duration, not syllables or forced word alignment. The two voiced lines `Main_Linaxita_2_2_91_1` and `_91_2` have absent normalized text in all four languages. The adapter marks their source-linked rate proxies `missing_source_text_witness`, with `units`, rates and text hash null; verified audio is not silently treated as a zero-word script.

## Exact-action contrast and source-unvoiced controls

The [source-defined cohort audit](../04%20Validation%20and%20Readiness/WUWA_ZANI_SOURCE_DEFINED_AUDIO_COHORT_AUDIT.md) joins eight disjoint action/TalkItem selections to 142 semantic lines, 571 render associations and 571 distinct integrity-valid PCM objects. It intentionally tests, rather than presupposes, a vocal transformation from client-facing bank employee through Nightwalker confrontation to a person attempting rest. The front-desk action itself contains both formal welcome and terser staff talk; the `7297/7` action contains guest sweets and minor-offender inquiry; `7301/4` includes retrospective error and a safer-city wish. Optional branches are present, so action membership is not a playback order. The bank's hidden-speaker first line is accepted only by contextual identity adjudication and has seven render associations—two different PCM objects each in ZH/EN/JA, one in KO. A paired one-object-per-dub comparison excludes it [ZAN-E11, E14, E17–E18, E33].

At the −45 dBFS active-frame gate, front-desk median levels are ZH −22.4, EN −23.6, JA −19.7 and KO −23.7 dBFS; Talos-confrontation medians are ZH −24.3, EN −23.9, JA −20.3 and KO −25.8. The threat set is lower-level in three dubs and nearly equal in EN, not a universal “vigilante is louder” pattern. Qualified F0 medians rise from front desk to Talos in ZH and EN but fall in JA and KO. The five sweets lines versus fourteen minor-offender lines likewise do not yield a shared F0 direction. Script, duration, gain, delivery and scene treatment are confounded; these are descriptive values, not human-heard timbre or intent. The source's ethically different speech acts remain different even though this acoustic shortcut fails [ZAN-E14, E20, E33, C26, C31].

The accepted `8585/5` restitution turns (ten) and `8586/10` night-city turns (thirteen) are all `play_voice: false` in the pinned crosswalk and absent from the selected playable voice analysis. They support her *written* differentiated justice, breeze/bread pleasure and insomnia, but no claim that a listener heard warmth, guilt or recovery in these scenes. Missing selected voice is not proof that no asset exists in every client build. Human four-dub listening must use the actually voiced cohorts and preserve each exact occurrence/variant; direct runtime review is needed to separate mutually exclusive replies [ZAN-E21–E22, E34, C32].

## Fifteen retrieval cases, 63 renders

The metadata-only [matched-case artifact](AUDIO_MATCHED_SEMANTIC_CASES.json) selects seven archive lines, two bank-reception lines, three character-quest self-account lines, a rule-fiction line, a Talos confrontation line and a later-holiday line. Every case has EN/JA/KO/ZH render identities, WEM and FLAC hashes, canonical PCM SHA-256, virtual source path and source locator; event/media IDs are retained where resolved and explicitly null where not. `Main_Linaxita_2_1_16_1` has multiple runtime variants; do not choose a file only by friendly text-key stem. The cases are *not* the whole 912-line corpus and were chosen to test competing interpretive claims, not to fabricate statistical representativeness.

Some selected durations illustrate why signal-only inferences are unsafe. `FavorWord_150714_Content` takes about 15.3 s in EN but 30.1 s in JA; both are verified renders of a semantically aligned archive entry, not evidence that the Japanese Zani is twice as reverent. The compact `Character_Zani_63_23` threat spans about 1.6 s in ZH and 3.6 s in EN; silence, phrasing and acting need listening before calling either “harsher.” The bank greeting has variant-dependent durations even within a dub. More useful than these comparisons is the deterministic chain they enable: choose the exact occurrence and variant, retrieve local restricted FLAC, inspect four performances blind to the intended trait hypothesis, and then record human observations separately from measurements.

The three added ascension cases contribute twelve explicit event/media-ID render rows: Ascension II is about 7.04/6.55/7.22/7.21 s and IV about 8.27/7.07/11.00/11.08 s in EN/JA/KO/ZH order; V spans about 9.28/16.23/14.53/14.16 s. These timings reflect different localized text lengths and performances, not measured resolve, affection or fatigue. Across all fifteen cases, 35/63 render rows still have paired null event/numeric-media IDs, so media retrieval does not equal a fully demonstrated event-to-bank graph.

## Archive trigger and localization audit beyond the fifteen-case sample

All 72 favor-word rows join exact source locators and actual `Content` keys to 72 complete four-dub voice records and 288 distinct PCM-valid objects. Forty-one combat/system/traversal/reward rows at `favorword#/2193–2233` supply 41 explicit events and 164 of those objects. They are already inside the selected 912-line/3,517-object denominator; they are **not** one of the eight source-defined story-action acoustic cohorts above. Seventeen skill/liberation/intro raw IDs rotate to different valid `Content` keys, so the raw ID cannot stand in for text or event identity. The [row crosswalk and source-class profile](../01%20Evidence%20and%20Source-Facing/WUWA_ZANI_ARCHIVE_SKILL_KEY_AND_COMBAT_LABOR_PROFILE.md) gives the exact map.

This source class adds a battle register without settling ordinary conduct. EN Liberation III says “I don't do overtime,” whereas ZH/JA/KO express the approaching end of a shift; the pinned civil evidence permits meaningful overtime and separately records later real leave. EN/ZH Dash sound maxim-like about efficiency, but JA/KO are less absolute. Echo Transform is a temporary switch, not that paid leave. Skill IX's dust command, Injured I's shield reaction and Fallen III's justice phrase do not prove a hit, invulnerability, canonical death or completed judgment. Four-language text and valid PCM establish *what can be retrieved*; human delivery, exact runtime trigger and target consequence remain unobserved. The additional exact-event nominations in the [AV crosswalk](WUWA_ZANI_AV_HUMAN_RETRIEVAL_CROSSWALK.md) are outside the unchanged fifteen-case JSON, whose 35/63 paired-null count therefore stays the same.

## Pending human and multimodal review

Listen to each chosen four-dub case at matched playback level without normalizing away dynamics in the evidence copy. Annotate audible pauses, vocal attack, breath, laugh, stress, addressee, line boundaries and background contamination, with time offsets and uncertainty. Compare each performance to its *own* localized wording before cross-language conclusions. Also retrieve runtime scenes around the bank reception, Nightwalker disclosure, Talos confrontation and holiday; observe pose, gaze and timing without assuming the UI portrait is the enacted model. A revised AV packet may promote specific performance claims, but this pre-AV document intentionally makes none.
