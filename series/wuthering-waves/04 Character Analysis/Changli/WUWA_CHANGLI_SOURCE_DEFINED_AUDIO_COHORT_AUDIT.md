---
series: WUWA
character: Changli
artifact_type: source_defined_audio_cohort_audit
scope: CHANGLI_PINNED_3_6_0_TEXT_AUDIO_PRE_AV
analysis_generation: CHANGLI_PRE_AV_V0_1
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

# Changli — source-defined audio, route multiplicity and the silent poem

This audit asks two narrower questions than “what does Changli sound like?” First, how many *distinct measured objects* are actually represented by source-selected text occurrences and player-conditioned render associations? Second, can the written strategist, private invitation, medical care and later Weiqi scenes be compared without inventing a continuous route or performing an unheard poem? No one listened to or viewed the selected scenes for this audit. The [speech profile](WUWA_CHANGLI_SPEECH_AND_MACHINE_VOICE_PROFILE_PRE_AV.md) retains the whole-corpus method, and the [Weiqi specialist](WUWA_CHANGLI_WEIQI_INVITATION_BRANCH_AND_DISCLOSURE_PROFILE.md) retains the graph interpretation.

## Exact cohorts

The eleven cohorts were specified by pinned source action and, where needed, exact zero-based TalkItem index *before* reading signal summaries. They select 242 semantic occurrences from the 610-line selected corpus: 224 have playable render associations and **18** `3688/0` text lines have unsupported dispatch. The 224 resolved occurrences produce 964 render associations but only 902 globally distinct canonical native-PCM objects in this subset, all with stored FLAC-hash and native-PCM-payload integrity passes and machine measurements. This selection is purposive; it is not 242 independent heard lines, 964 recordings, or the whole character voice.

| Cohort | Source selection | Semantic lines | Render associations | Source question |
|---|---|---:|---:|---|
| Hidden counsel | `flow#/2516/3` | 14 | 64 | Contextually attributed strategist turns, teacher–student agency and a promised supporting role. |
| Wayfinder risk | `flow#/3123/5` | 33 | 132 | Conditional time-risk explanation and Rover's decision. |
| Jinhsi strategy | `flow#/3209/3` | 28 | 164 | Sharp survival objection, Jinhsi's choice and subsequent route planning; several runtime variants. |
| Weiqi opening/apology | `flow#/3296/4@0-3+5+7-13` | 12 | 48 | Alternate opening, common token apology, optional EN “adorable.” |
| Weiqi uncertainty/request | `flow#/3296/4@14-36` | 23 | 92 | Legend versus record, slim healing theory, personal request. Some lines are branch alternatives. |
| Weiqi response routes | `flow#/3296/4@37-46` | 10 | 40 | Immediate-yes, why-me and reward replies, then shared departure; not one speech. |
| Explorer treatment | `flow#/3305/3` | 12 | 48 | Suspicious history but care before questioning an injured explorer. |
| Fuling investigation | `flow#/3310/3`, `3311/6` | 41 | 164 | Temporal-disruption hypothesis and the couple's distinct desires. |
| Care and rest | `flow#/3320/4` | 15 | 60 | Doctors, Fuling's art and postcrisis work/rest. |
| Later Weiqi | `flow#/3323/6` | 36 | 152 | Mature-fire reassurance, limited-life reflection and a later invitation; runtime variants remain. |
| Poetic no-dispatch | `flow#/3688/0` | 18 | **0** | Text and installed-member evidence without supported runtime dispatch/decoded line audio. |

The three `3296/4` groups are disjoint and total its 45 accepted semantic occurrences, but they contain *mutually exclusive route lines*. They describe the selected source surface, not a reachable 45-line playthrough. `2516/3` includes the contextually accepted hidden strategist; generic technical speaker IDs must not be globally equated with Changli. The poetic group is not a missing language pack: `ANALYSIS/Characters/Changli/UNRESOLVED_VOICE_MEDIA.json` retains installed-member rows and explicitly records `runtime_dispatch_unsupported` for 72 language-render possibilities. It does not establish which WEM would have played those 18 texts, much less a decoded performance. In the machine audit they remain 18 semantic IDs with `semantic_lines_without_renders`, not zero-length PCM objects.

The private no-media artifact `_research/character_packets/Changli/audio_work/CHANGLI_SOURCE_COHORT_AUDIT.json` has SHA-256 `1336d0cc9009f65ea9d1981ffafcf9db027a3df045c2b0b8177b9fc975d408bd`. Its members preserve source locators, semantic occurrence IDs, render IDs, language, PCM/FLAC hashes and flags alongside input hashes. Recreate it with `scripts/audit_character_audio_cohorts.py Changli`, the exact eleven `--cohort` selections above (drop `flow#/`), and `--output` to that private path. A rerun was byte-identical. The invalid `3296/4@999` selection and overlapping `3296/4@0-3,3296/4@2` each failed nonzero before writing a negative-test file.

## Render arithmetic is not optional

The 224 resolved semantic occurrences imply 896 occurrence–language cells. Their 964 render associations add 68 associations from runtime variants. Counting distinct PCM within *each* occurrence–language cell gives 910: just 14 extra distinct variants beyond one PCM per cell, while 54 associations repeat a PCM already in their own cell. A further eight PCM reuses across different occurrence–language cells yield 902 globally distinct PCM objects. There is **no cross-language PCM overlap in this selected subset**; the whole corpus's 23 objects shared across four language collections remain a separate full-scope fact. In `3296/4` the two opening alternatives can reuse the same recorded thanks/apology even while their source occurrence IDs remain distinct. One friendly filename, one semantic line and one playable object are not interchangeable keys.

The auditor's matched-level comparison admits an occurrence only if ZH and the target language each have exactly one *distinct* PCM. It does not choose one variant arbitrarily or average alternate recordings. Thus `3209/3` has 28 selected semantic lines but 164 associations; for its EN-versus-ZH level comparison, 22 pairs are admitted and **six** EN distinct-variant occurrences excluded. JA admits 25 and excludes three; KO admits all 28. `2516/3` similarly excludes two EN and one JA occurrence. The later `3323/6` comparison excludes two EN variants. A claim based on one supposedly universal Jinhsi-strategy or later-Weiqi sound would hide those runtime decisions.

## Bounded signal observations and their non-result

All 902 selected distinct objects are within the previously integrity-valid measured universe. None of these eleven selected cohorts contains a multichannel object, although the *full* Changli corpus contains 73 multichannel flags; this is another reason not to generalize from the cohorts. Their qualified-pitch denominators are stored by language and cohort. The −50 to −40 dBFS gate changes median active duration by 0.18–0.54 seconds in the three first-Weiqi groups and 0.26–0.63 seconds in the later-Weiqi group, depending on language. Neither a detected low-energy interval nor its length is a phrase-aligned intentional pause.

The matched JA-minus-ZH median active-frame level ranges from about +0.06 dB in hidden counsel to −2.31 in Wayfinder risk, −2.92/−3.57/−3.88 across the three first-Weiqi groups, −5.31 in Fuling investigation, −5.74 in care/rest and −5.38 in later Weiqi. Those are real object-level differences under the declared gate, but neither within-language loudness normalization nor identical wording/recording-chain control has been done. The progression is a useful mixing/provenance question for later listening, **not** evidence that Changli becomes quieter with increasing intimacy, that one actor grieves more, or that the writing has a measured emotional arc. The full-set 23 cross-language shared objects also warn against treating every dub-aggregate row as an independent actor sample, even though this particular selection contains none.

The older two-line F0 contrast between `3323/6/32` and route-only `3296/4/39` remains a negative control. It did not establish a four-dub warmth rule. The larger source cohorts reveal additional state and render multiplicity, not a license to promote that two-line impression. Similarly, a recorded `3320/4/32` doctor offer can corroborate that audio exists for *that* source line, but acoustic metrics cannot certify Fuling's cure or Changli's medical prognosis. The poem's source text may be analyzed as text only. Human review should first traverse the three Weiqi response routes and the two opening variants; then listen to exact render IDs and timestamps for the risk, care and later-game lines, checking voice versus background and localization phrase match. An observation can revise a delivery claim only within the route, language and signal object actually inspected.

## Additive Chronosorter source cohorts, not a replacement for the eleven

A separate reproducible metadata audit selects `physical_clue=3175/5`, `first_record=3176/5`, and `exceptional_device=3177/5` to match the [Chronosorter source study](WUWA_CHANGLI_CHRONOSORTER_HYPOTHESIS_EVIDENCE_AND_RISK_PROFILE.md). It is deliberately **additive**, so the frozen eleven-cohort artifact and its 242/964/902 accounting above remain unchanged. The three actions contribute 9, 13 and 21 accepted source-voiced Changli semantic occurrences, respectively: **43** lines, **172** four-dub render associations and **172** distinct native-PCM objects across this supplemental selection. Each of the 172 objects passed stored FLAC and PCM integrity checks; all are one-channel, no render variant or cross-action PCM reuse occurs in this particular selection. The first record has one ZH object with a `pitch_edge_band_frequent` flag, leaving 12/13 ZH pitch-qualified rather than 13/13. The other language/cohort pitch-qualified counts equal their measured-object counts. No human listening, dialogue timing or visual viewing occurred.

| Exact action | Lines / associations / distinct PCM | Matched JA-minus-ZH median active-frame level at −45 dBFS | Interpretation limit |
|---|---:|---:|---|
| `flow#/3175/5` | 9 / 36 / 36 | −2.00 dB, 9 line pairs | A lower JA object level cannot diagnose Changli's alarm from the blood/scales clue. |
| `flow#/3176/5` | 13 / 52 / 52 | −2.20 dB, 13 line pairs | The archive's bleak verdict is textual and qualified; level is not her certainty. |
| `flow#/3177/5` | 21 / 84 / 84 | −2.32 dB, 21 line pairs | A measured file cannot validate the machine experiment, safe Overclocking or visitor-transfer causality. |

The three JA–ZH medians are close to the earlier Wayfinder-risk group's −2.31 dB, yet sentence content, durations, recording chains and exact game mix are not controlled. This is a useful *negative* result for any simple machine-level “she grows more frightened as the evidence worsens” law. The −50 to −40 dBFS gate changes median active duration by 0.16–0.44 s in ZH and 0.26–0.40 s in JA across these three groups; those changes are threshold sensitivity, not heard hesitation. Likewise the one pitch flag is a measurement eligibility decision, not evidence of a vocal condition.

The restricted no-media artifact is `_research/character_packets/Changli/audio_work/CHANGLI_CHRONOSORTER_SOURCE_COHORT_AUDIT.json`, SHA-256 `2f18f33d51af2891057892d195fe1e13b094651d432fac3e4262572231e725ae`. Recreate it with `python scripts/audit_character_audio_cohorts.py Changli --cohort physical_clue=3175/5 --cohort first_record=3176/5 --cohort exceptional_device=3177/5 --output _research/character_packets/Changli/audio_work/CHANGLI_CHRONOSORTER_SOURCE_COHORT_AUDIT.json`. A second run reproduced the same hash. Its members retain exact source locators, occurrence IDs, render IDs, languages and PCM/FLAC hashes. The three supplemental actions are disjoint from one another and from the prior eleven selections; still, do not add counts to a whole-corpus denominator without deduplicating selected semantic IDs and objects first.
