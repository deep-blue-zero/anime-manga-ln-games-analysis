---
series: WUWA
character: Yinlin
artifact_type: source_defined_audio_cohort_audit
scope: YINLIN_PINNED_3_6_0_TEXT_AUDIO_PRE_AV
analysis_generation: YINLIN_PRE_AV_V0_1
status: draft_noncurrent
release_state: author_working_draft_pending_owner_review
source_commit: 353f2eaed119bc9f680eab92807d20ac75a79b40
source_generation_frozen: true
source_freeze_metadata: conflicting_collection_and_embedded_lock_fields
text_authority: zh-Hans
localization_witnesses: [en, ja, ko]
supersedes: []
superseded_by: []
do_not_use_as_current_authority: true
---

# Yinlin — source-defined voice cohorts, route variants and unvoiced festival controls

Yinlin's written record crosses undercover explanation, unconsented tracking, a dangerous performed defection, resistance to the Dollmaker, retrospective confession, and a later chosen mixture of covert duty and holiday time. It is tempting to call these one acoustic journey from manipulation to “true voice.” This audit asks what the existing exact source/render/PCM mapping actually permits. It is a metadata and machine-signal analysis, **not** four-dub listening, runtime branch observation, an actor-intent finding, or full voice-line interpretation. The [speech profile](WUWA_YINLIN_SPEECH_AND_MACHINE_VOICE_PROFILE_PRE_AV.md) supplies the written-language hinges; the [matrix](WUWA_YINLIN_EVIDENCE_AND_FALSIFICATION_MATRIX.md) owns claim scope and counterreadings.

## Selected action/TalkItem strata

Sixteen deliberately disjoint selections cover **181 semantic story lines**, 41.2% of the selected 439-line voice corpus, and **728 render associations but only 725 distinct canonical PCM objects**. All 725 have prior local measurement and integrity validation; the whole selected corpus remains 439 lines/1,776 associations/1,725 distinct objects. These 181 source lines include alternative replies and cover-state utterances, not a transcript of one executed playthrough. A grouped action would hide important audience and knowledge changes, so `1004/6`, `1006/7`, `353/6`, and `15092/6` are partitioned explicitly.

| Source-defined cohort | Exact selector | Lines / render associations | Distinction tested |
|---|---|---:|---|
| Puppet explanation | `997/7` | 15 / 60 | Replica account and risk language are neither a proof of resurrection nor one covert seduction. |
| Private case exposition | `1004/6@0-21` | 22 / 88 | Limited access, Li Rong's grief and suspected links; the organization claim remains investigative. |
| Rover risk and offer | `1004/6@22-34+42-43` | 15 / 60 | A request to help follows risk disclosure but has optional answers; later tracking still complicates consent. |
| Yuanyuan care under cover | `1004/6@36+38+40-41` | 4 / 16 | Her child-facing reassurance is not the same addressee or operational purpose as Rover recruitment. |
| Postfight social approach | `1006/7@0-9` | 10 / 40 | Teasing and injury concern precede the tracking admission; player answers vary. |
| Tracking admission | `1006/7@10-15` | 6 / 24 | She identifies an eavesdropping/location device and prior distrust rather than hiding it behind a friendly register. |
| Posttracker tactics | `1006/7@16-23` | 8 / 32 | The same action then returns to Li Rong, Yuanyuan and moving the bodies/puppets safely. |
| Guardian reveal under cover | `349/5` | 21 / 84 | Her orphan/guardian account occurs while Society allegiance is being tested, not in an uncontested private confession. |
| Hostage performance | `350/4` | 5 / 20 | Threatening public role and a brief trust request coexist; text alone does not remove Rover's imposed risk. |
| Living-people objection | `673/3` | 6 / 24 | She contests instrumental harm to the Society's own people. |
| Vocation without file | `1092/1` | 11 / 44 | Refusal of parent-revival at others' expense is a source action, not mere restored badge authority. |
| Postcase account | `353/6@0-13` | 14 / 56 | She admits using Rover and describes the Dollmaker's attempted access and remaining uncertainty. |
| Grief and complicity | `353/6@14-28` | 15 / 64 | Shared loneliness and an attractive reunion fantasy do not excuse delayed resistance. |
| Future and tentative trust | `353/6@29-37` | 9 / 36 | Continuing threat, a marked joke, gratitude and ZH's *possible* trust must not become guaranteed romance. |
| Party as herself | `15092/6@1-3+5-7` | 6 / 24 | A later event names her off-duty presence as Yinlin while still checking who can overhear. |
| Renewed covert duty | `15092/6@10-18+20-24` | 14 / 56 | Rebuilt dossier, declined public return and costly chosen work are later developments, not permanent exile. |

Raw `ShowTalk` confirms route restrictions inside these selections. For example, `1004/6` contains multiple Rover options and `1006/7` begins with three different responses; the two sets of accepted lines need not all occur in one run. `15092/6` also opens with alternate replies before the later dossier account. Exact selected membership provides retrieval targets, not a played branch history [YIN-E11–E12, E24].

One occurrence makes render identity especially important. `353/6/28` (`Character_YinLin_58_36`) has **two render associations in each language**. English's two canonical PCM hashes are distinct. In JA, KO and ZH the two runtime render IDs alias the *same* PCM hash within each dub. This adds four associations above the one-per-dub 724 baseline but only one extra unique PCM, yielding 728 associations/725 PCM. Counting every render as an independent heard take would inflate evidence in JA/KO/ZH; collapsing the English pair by text key would erase a real sound variant. The paired-level auditor excludes the distinct-variant occurrence where a single language value would be arbitrary.

## Scene-linked signal contrast is not sincerity detection

The stored −45 dBFS active-frame measure shows a substantial **scene-dependent EN-minus-ZH level offset**, with medians formed only from unambiguous one-object-per-language occurrence pairs. Early puppet explanation is −0.02 dB across 15 pairs, private case exposition +0.88 across 22, Rover risk/offer −0.07 across 15, and tracker admission +0.91 across six. The later guardian reveal and hostage actions are +2.68 dB (21 pairs) and +2.80 (five); living-people objection, vocation, grief/complicity and tentative-trust selections reach +4.08, +4.71, +4.30 and +4.41 respectively. The later *party as herself* selection reverses to −2.14 dB (six), while renewed covert duty is −0.81 (fourteen). This nonconstant pattern is reproducible file-level evidence, not a localization ranking or proof that her English actor becomes louder when she is “honest.” Different text, action mix, recording gain, scene treatment, encoding and performance all remain possible contributors. A listener would need level-aware matched playback, phrase alignment, scene context and contrary readings before attributing any portion to acting.

Within the same `1006/7` action, postfight social approach, tracker admission and subsequent tactics have median active levels ZH −22.63/−23.35/−22.37, EN −22.78/−22.75/−22.80, JA −22.22/−24.81/−22.94 and KO −20.86/−21.52/−21.52 dBFS. The confession is **not a universal loudness spike**; JA is lower-level and EN almost flat. This split holds audience and broad recording context closer than the cross-action comparison, but the individual words and lengths still differ. It supports an exact listening design rather than a psychometric trait. The two `15092/6` subdivisions likewise mix off-duty presence with continued work in one source action, so a later “mask off” persona cannot be defined by a single whole-action median [YIN-E11–E12, E24].

The conservative pitch gate accepts 723 of the 728 selected render associations, far more than in some other packets, but qualified F0 still cannot resolve deception, intimacy, ethical conviction or vocal age across dubs. A high qualification rate means the estimator returned usable signal under its declared gates, not that different scripts, actors and mixes form controlled comparisons. The source-selected lines and the quoted Chinese/EN/Japanese/Korean semantic differences have priority when specifying a model. No observed theatrical pause, softness, laugh or threat is claimed here.

Four earlier festival/free-show actions are important **negative controls**: `3987/6` has ten accepted Yinlin turns, `3991/6` four, `3992/7` twenty-three and `4231/1` eleven. All **48** are `play_voice: false` in the pinned crosswalk and absent from selected playable line analysis. Their apology, subsequent performed-mistake admission, invitation and freely chosen public craft remain textual evidence; none is a measured or heard festival line in this generation. This does **not** make the later `15092/6` party dialogue unvoiced—it contributes twenty selected semantic lines above. Medium, episode and time must be kept separate, and absence from this selection does not prove universal client-asset absence [YIN-E21–E24].

## Reproduction and revision gate

The private artifact `_research/character_packets/Yinlin/audio_work/YINLIN_SOURCE_COHORT_AUDIT.json` has SHA-256 `b1dd590084042d3e29036067ca60f12bf6bcc6ad0eb626cdbd84aea5525743d1`. It binds pinned line-analysis and object-measurement hashes and lists every member's semantic occurrence, text key, exact source locator, dub, render-analysis ID, PCM/FLAC hashes and flags. Re-run `scripts/audit_character_audio_cohorts.py Yinlin` with the sixteen literal `--cohort NAME=selector` values above and that private `--output`; a second run was byte-identical. A selector for unvoiced `3992/7` and an overlapping within-cohort `1006/7` selector both failed nonzero without writing their intended files. The utility allows overlaps *between* named cohorts; the reported 181 unique semantic IDs and 728 unique render IDs were therefore checked separately.

**PRESERVE** cover-, audience-, choice- and time-indexed text readings. **DOWNGRADE** any acoustic “true self” or seduction-to-sincerity curve derived solely from active level/F0. **REVISE** any selected-audio claim about the earlier festival/free-show lines, and distinguish their absence from the voiced later party. **OPEN** variant-aware four-dub listening, runtime branch/staging observation, full JA/KO semantic adjudication and independent gain/segmentation checks. No audio was copied into Git, no human performed-voice review is asserted, and this packet remains noncurrent.
