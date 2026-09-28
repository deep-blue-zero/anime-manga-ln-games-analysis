---
series: WUWA
character: Iuno
artifact_type: speech_and_machine_voice_profile_pre_av
scope: IUNO_PINNED_3_6_0_TEXT_AUDIO_PRE_AV
analysis_generation: IUNO_PRE_AV_V0_1
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

# Iuno — textual speech and measured voice, pre-AV

## A voice with state, not one permanent pose

Public Iuno enjoys self-advertisement, direct challenge, mock-grand titles and turning a tactical maneuver into a game. That register is not merely false armor; she says she likes surprises and applause, and her field instructions are genuinely confident. It is nevertheless incomplete. With Augusta she can quarrel and worry; with an injured companion she gives brief practical directions; before vanishing she asks about rest and admits the fear of forgetting; the 350026 remnant speaks in broken searches for her own name; after return she can admit an unknown future. The textual shift is a source-state constraint, **not yet an observed acting interpretation**. [IUN-E09–E18, E20–E23]

Her signature conceptual antithesis is *seeing versus facing*. The line about an unknowable void changes significance across time: at first Rover's future defeats her divination, then their open possibility helps her choose beyond a fixed final answer. “Moon,” “arrow” and “anchor” can be tactical objects, metaphors for causality, a family/Temple inheritance, or an intimate bracelet. A model should identify which function applies instead of inserting grand fate rhetoric into every meal. Past/Chaos recollections and stylized third-person `10155/0` narration should not be treated as casual present-day banter. [IUN-E04, E07–E09, E14, E17–E21]

The five ascension-menu addresses add a distinct address register, not a dated after-return dialogue. I–II join growing power to feeling, memory, ties and lunar change; III asks whether the addressee is sure about a possible shared unknown; IV asks for something desired besides power and cautions before an answer; V gathers seeing images around Chaos and the moon (`FavorWord_141027–141031_Content`; `favorword#/2566–2570`). Japanese IV adds not letting go of the addressee's hand and Korean is forceful about pursuit, while English and Chinese leave the desired object unspecified. Japanese/Korean V use past/perfective seeing, unlike the present-like Chinese/English. Textual contrast does not establish whether the warning is fearful, flirtatious or ironic in any dub, nor does it restore the clear fate-peering she says she traded away [IUN-E34–E36, C28–C31].

The [archive-key and trigger profile](WUWA_IUNO_ARCHIVE_KEY_FATE_AND_FALLEN_VOICE_PROFILE.md) separates 49 combat/system entries from the 31 earlier archive/menu entries. All 80 raw favor IDs are one greater than their actual Content-key suffixes; the exact row, not that observed offset, controls retrieval. The 49 trigger rows have 196 PCM-valid four-dub objects already in the 2,155-object corpus, but they are not the 170 **story-action** lines in the eight-cohort study below. Skill X–XII's causality/future/fate language is a battle register, not demonstrated restored clear vision. Fallen II varies materially: ZH/KO are past-oriented, JA present-oriented, EN leaves a “mark”; no version turns the defeat bark into a dated story death. Human hearing may sharpen emotion; only runtime observation can verify the fired trigger and recipient [IUN-E38–E40; C33–C35].

An earlier archive address has its own translation-sensitive intimacy. `FavorWord_141004_Content` first acknowledges the burden placed on whoever remembers her, then names her wish as selfish. ZH/EN/KO condition the hoped-for exceptional rememberer on whether anyone retains her trace; JA more emphatically singles out the addressee and her whole self. The exact four-dub case IUN-AV-03 is decoded and measured, but not yet listened to. No textual witness provides Rover's reciprocal answer or a stable breath/tempo signature for this request [IUN-E37, C32].

## Measured selected corpus

The private complete selected voice corpus contains 540 semantic line records, 2,162 render associations, 2,158 runtime object rows and **2,155** distinct measured native PCM/FLAC objects. All objects passed local integrity and signal measurement; three manifest rows reuse a PCM. The [24 matched cases](AUDIO_MATCHED_SEMANTIC_CASES.json) preserve semantic occurrence ID and text/source hashes separately from four render IDs, Wwise/media identity and WEM/PCM/FLAC hashes. Forty-four of their 96 renders have null event and numeric-media IDs, so those chains stop at exact external-source object identity rather than proving an event/bank mapping. There is no voice media in this Git packet.

| Dub | Distinct measured objects | Sum duration | Median object duration | Qualified F0 median | Median energy-active level |
|---|---:|---:|---:|---:|---:|
| EN | 539 | 3,312.98 s | 4.632 s | 227.31 Hz (528 qualified) | −23.70 dBFS |
| JA | 539 | 4,080.59 s | 5.712 s | 279.92 Hz (531 qualified) | −23.92 dBFS |
| KO | 539 | 4,169.36 s | 5.667 s | 295.38 Hz (518 qualified) | −22.72 dBFS |
| ZH | 538 | 3,863.42 s | 5.730 s | 277.02 Hz (504 qualified) | −23.31 dBFS |

These statistics are for media objects, not a biological trait, one actor's natural voice, acting quality, emotional intensity or language-specific speech rate. Cross-dub duration differences include different writing and performance, and text-unit ratios are **not** forced syllable alignment. The analyzer selected the highest-RMS native channel rather than isolating a guaranteed speech stem. Full-set QC counts include 45 frequent pitch-edge-band flags, 25 pitch-parameter-sensitive flags, 14 with fewer than ten voiced frames, 23 long-object subtitle-extent flags and one full-scale-samples warning that does not prove audible clipping. Flag counts can overlap. Analyzer version/hash and exact parameters are recorded in the private `AUDIO_MEASUREMENT_SUMMARY.json`; human listening and video review flags remain false.

Unlike some other character corpora, the four Iuno language object sets are disjoint by canonical PCM hash in this pinned selection: their 539+539+539+538 memberships sum to exactly 2,155 unique objects. This prevents double-counting the whole-set object denominator, but it does not make cross-dub F0, duration or energy directly comparable as actor traits.

## Source-defined audit of disappearance and return

A restricted metadata-only report (`_research/character_packets/Iuno/audio_work/IUNO_SOURCE_COHORT_AUDIT.json`, SHA-256 `e43b288b47de62e88d2f3e8854dd5e3e47e5b893792a12f11ef828455a0e3514`) joins pinned source actions to existing semantic-line, render and measured-object records. The eight disjoint cohorts below cover **170/540** selected semantic lines, **680** render associations and 680 distinct PCM hashes. All 680 are mono, integrity-valid and measured; 663 meet the declared pitch qualification gate. The report reproduced byte-identically on rerun. A requested nonexistent TalkItem and overlapping source selectors each failed without writing a report. These are selected contrasts, not a random sample of the whole corpus or a listening study.

| Cohort and exact source address | Lines | Scope and negative control |
|---|---:|---|
| Fate-peering trade, `flow#/8386/4` | 42 | Preplan explanation of what she traded and what she still remembers; not proof that later vision is clear. |
| Joint intervention, `flow#/8408/3` | 32 | Tactical claims to Augusta/Rover; her hidden personal cost is a separate information question. |
| Farewell, `flow#/7741/5` | 13 | Sleep comforts and bracelet preparations before disappearance; rest is not a demonstrated cure. |
| Fragment, `flow#/7747/5` | 8 | Technical speaker 350026 with incomplete self-access; not a second person. |
| Present re-anchoring speech, `flow#/7764/3` indices `/0`, `/2–3`, `/5–6`, `/20–22` | 8 | Technical speaker 350026; this action also contains other voices and remembered quotations. |
| Quoted earlier-self speech, `flow#/7764/3/7–17` | 11 | Generic technical speaker 178 is contextually resolved as Iuno's remembered words, not the remnant's present narration. |
| Returned disclosure, `flow#/7759/3` | 35 | Cost admission, conditional future promise, friendship hope and route-sensitive privacy request. |
| Later evacuation, `flow#/8878/7` | 21 | Competent civic action after return, without regained augury being assumed. |

The `7764/3` split is an analytical necessity, not a finer label for the same utterances. Raw TalkItem indices `/0,2–3,5–6,20–22` use technical speaker **350026**, while `/7–17` use **178** for quoted memories; the exact occurrence crosswalk accepts both for Iuno for *different reasons*. Pooling the action would hide that distinction. The qualified within-dub object-level F0 medians for present re-anchoring versus remembered-self quotation are **264.3/337.5 Hz ZH, 197.1/301.0 EN, 269.6/421.3 JA, and 239.5/381.5 KO**. This repeated numerical separation warrants targeted listening, but it does not prove one actor deliberately changed persona, that the memory is a second embodied Iuno, or that pitch alone conveys restored identity. The quotation cohort has different words, phonetics and source presentation, and some objects are excluded from F0 qualification. The earlier `7747/5` fragment is kept separate so even two technical-350026 scenes are not silently made one state.

Level and gate sensitivity further narrow performance claims. The exact-occurrence paired EN-minus-ZH active-frame median is **−2.47 dB** in the farewell cohort, **+3.19 dB** in the eight-line Chaos fragment and **−1.39 dB** after return; JA-minus-ZH is **−2.78**, **+1.45** and **−1.51 dB** for those same groups. These are digital signal-level differences in different texts and production contexts, not a reliable scale of confidence, fear or intimacy. Moving the low-energy gate from −50 to −40 dBFS shifts median active duration by **0.15–0.64 seconds** across cohort/language cells. Rate, pause or fragility judgments therefore require disclosed gate choice, source context and hearing, not a single whole-corpus median.

Three *accepted* but source-unvoiced surfaces are essential negative controls: six Iuno turns at `flow#/7742/1`, including her unfinished fear of being forgotten, plus 17 and 22 at the optional `10491/6` and `11529/6` encounters, all have `play_voice: false` in the pinned crosswalk. Their Chinese/English text can inform the model; the neighboring voiced farewell or return cannot be used to invent how those particular lines sound. The twenty `LIANBO_TEST_3.4` placeholders are separately unvoiced and nonliterary. No human four-dub performance or runtime gesture conclusion is added by this audit.

## Four-dub retrieval priorities

The 24-case metadata index covers Rover's void; cumulative existence loss; the burden of memory; a future not yet chosen; prepared surprise and ripe fruit; Augusta and Lillibet relationships; the ability trade; hidden self-cost; fragmented “Iuno” self-recognition; and her insistence on deciding her own path. Seven return-scene cases isolate a conditional full-account promise to Rover, old friends' nonrecognition, hope of renewed friendship, and the common privacy request versus the teasing response route. Five further exact ascension cases preserve archive identity, four-language witnesses and explicit event/media IDs; none is a dated quest conversation. The new Ascension V renders last roughly 15.8/20.0/17.8/21.6 s in EN/JA/KO/ZH order. That spread does not identify actor intention. All selected cases have resolved text witnesses and measured renders. They are **claim-driven** rather than statistically representative. Match a case's exact render to its text witness before comparing performance; the remnant case must retain source state 350026, and long/mixed-channel cases need separate QC judgment. The Japanese “friendship from the beginning,” desire phrasing and V's seeing aspect require textual comparison before any actor-intent claim.

A completed performed-voice claim would require listening to all 540 selected semantic cases across available four-dub renders, with statuses for unavailable, mixed, unreviewed and uncertain observations. The 125 source-unvoiced accepted direct occurrences are not heard speech; 20 of those are identified `LIANBO_TEST_3.4` placeholders, not interpretable dialogue. A human review should annotate source/render/timecode/channel, dub, audible delivery and independent interpretation with counterexamples. Machine F0 or dBFS may direct attention to unusual objects but cannot label Iuno “arrogant,” “fragile,” “flirtatious” or “frightened.”
