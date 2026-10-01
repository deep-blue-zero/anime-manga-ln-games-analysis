---
series: WUWA
character: Cantarella
artifact_type: speech_and_machine_voice_profile_pre_av
scope: CANTARELLA_PINNED_3_6_0_TEXT_AUDIO_PRE_AV
analysis_generation: CANTARELLA_PRE_AV_V0_1
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

# Cantarella — textual speech and measured voice, pre-AV

## Written registers, not actor-performance labels

Cantarella often folds a concrete proposal into sea, poison or dream metaphor, then tests whether the addressee will approach. That pattern has multiple functions. A favor line offering relief for fatigue is caring; a character-quest warning names lethal plants with almost instructional precision; the Sea of Ghosts invitation asks Rover to judge her; the political account of Sentinel/Leviathan is structured explanation; after the crisis she describes ordinary tea plainly. The same lexical motif can therefore signal temptation, medical caution, memory, affection or artifice depending on scene. [CAN-E08–E13, E20–E22]

The five favor stories are prose with distinct nested viewpoints, not five samples of a single continuous speaking register. The older-looking dream voice confidently pushes dream control; the notebook figure's procedural certainty becomes a self-harming trap; the child uses birds and ground underfoot to think about freedom. The final waking Cantarella adopts none wholesale. Scenario text should be able to switch from playful ellipses and teasing questions to explicit moral disagreement and quiet gratitude without declaring a wholly new personality. Her first-person claim of certainty is also undercut by the inherited-record discussion in which she checks her thoughts against whispers. [CAN-E03–E07, E21]

Combat barks are task-specific and often lethal; they are not examples of how she addresses a guest at tea. Favor intimacy, optional gondola lines and branch-specific Rover choices are similarly not a universal speech script. The `FavorWord_160765_Content` source key is archive-listed as greeting despite its nonsequential key number; text key, not display row position, is the reproducible join. Anonymous nearby speakers are excluded according to the exact identity crosswalk. [CAN-E08–E10, E24–E25]

The combat/archive block is large enough to test that boundary rather than merely assert it. Raw favor-word IDs **160732–160765** comprise 34 attack, skill, intro, injury, fallen and traversal/chest trigger rows. Their actual `Content` keys run `FavorWord_160731–160764_Content`, not the raw-ID numbers; the greeting's raw ID 160723 instead points to `FavorWord_160765_Content`. Exact raw-row locators join all 34 combat/system records to **34 semantic voice occurrences, 34 distinct event IDs with populated bank fields and 136 distinct, mono, four-dub PCM/FLAC objects**, with all render round trips marked identical. This verifies the retained mapping records and retrievable performance set, not an independent reparse of every bank or when a trigger fired in a story scene. The archive's trigger titles are a source-class boundary, not a chronological chapter. [CAN-E36]

There is a particularly revealing *Chinese textual echo* across that boundary. The blink instruction in `FavorWord_160733_Content` (raw ID 160734, Resonance Skill I) recurs within the jellyfish/dream invitation in `FavorWord_160702_Content` (raw ID 160702, Thoughts II). The latter speaks to a prospective guest who is told not to fear the jellyfish; the former is an attack trigger. English preserves the blink command in the skill but not the longer Thought II text, while Japanese changes the skill into a challenge about catching her and Korean asks the hearer to look closely. The repeated Chinese wording gives her repertoire a recognizable texture; it does **not** turn an apparent opponent into a consenting dream guest or prove a single emotional intention in every dub. Likewise, `FavorWord_160735_Content` invites swimming together in ZH/JA/KO, whereas EN emphasizes the tide's pull. It cannot be lifted from a skill trigger as evidence that a social invitation has already been accepted. [CAN-E08, E36]

Soft and harmful marine words coexist *within* the triggered set. `FavorWord_160737_Content` gives the sea's caress in ZH/EN, mercy in JA and touch in KO; nearby `FavorWord_160741–160743_Content` commands choking/suffering, struggle and another distress state with nonidentical physical wording across witnesses. Intro keys `FavorWord_160747–160748_Content` reassure or offer company, but they are entry-to-combat cues, not proof of a standing intimate relationship. The Liberation at `FavorWord_160746_Content` is a sharper translation trap: ZH/JA offer the sea's whisper and KO its blessing, while EN adds sleep and sirens. A model may exploit the shared sea imagery as an aesthetic resource while keeping the target, action and localization separate. It may not export EN's siren-induced sleep into all four source witnesses, read combat caress as assured safe touch, or turn the damaged-opponent lexicon into her default bedside manner. [CAN-E36]

Two self-directed triggers also have strict evidentiary limits. `FavorWord_160753_Content` says a sensation is familiar when she is injured, but does not identify the sensation, date a particular trial replay or diagnose a lasting condition. `FavorWord_160754_Content` invokes a return to water on a fallen trigger; it is not a canonical death scene. These lines are useful as questions for four-dub listening, including whether the verbal contrast is matched or resisted in delivery. No listening was performed here, and no machine energy or F0 value resolves those questions. [CAN-E02, E36]

The five Ascension addresses form another distinct *menu* register: sunlight, storm, vortex, the unknowable sea's offered secrets and slow companionship amid danger (`FavorWord_160726–160730_Content`; CAN-E33–E35). IV's Japanese treasure-location image is less intimate than the Chinese/English/Korean secret language; V's Japanese eventual light is not identical to a pure place reserved amid poison. Their metaphors should not be pasted onto an actual survivor-record request or treated as proof of toxin-safe hospitality. The source keys are one lower than raw row IDs 160727–160731.

## Full selected local audio measurement

The private selected voice corpus joins **845** semantic voice-line records to **3,389** render associations, 3,240 runtime object rows and **3,237** distinct native PCM/FLAC objects. All 3,237 passed local hash/integrity and waveform measurement; three manifest rows reused a PCM identity. This is four-dub *source availability*, not four-dub interpretation. The 105 accepted source-unvoiced direct occurrences remain text-only even if near voiced speech in a scene. The [23 matched cases](AUDIO_MATCHED_SEMANTIC_CASES.json) retain semantic occurrence ID, exact source locator and text hashes separately from each runtime render variant, event/media/path and WEM/PCM/FLAC hash. No recordings are checked into Git.

| Dub | Distinct measured objects | Sum duration | Median object duration | Qualified F0 median | Median energy-active level |
|---|---:|---:|---:|---:|---:|
| EN | 835 | 5,775.72 s | 6.188 s | 184.68 Hz (807 qualified) | −22.55 dBFS |
| JA | 834 | 5,733.28 s | 6.105 s | 239.72 Hz (831 qualified) | −23.08 dBFS |
| KO | 832 | 5,981.12 s | 6.374 s | 219.93 Hz (823 qualified) | −23.00 dBFS |
| ZH | 833 | 5,268.98 s | 5.569 s | 189.93 Hz (830 qualified) | −23.48 dBFS |

These are measurements of **selected media objects**, not intrinsic actor pitch, speed, emotionality or dub quality. Written-unit/text-duration ratios are language- and translation-dependent, not forced alignment. Different recording chains, line content, music/effects and channel layout can move summary values. The analyzer used the highest-RMS native channel, not source separation or a guaranteed clean speech channel. QC flags across the full set include 28 multichannel-not-isolated-speaker objects, 32 frequent pitch-edge-band objects, five pitch-parameter-sensitive objects, eight with fewer than ten voiced frames and one long-object subtitle-extent warning. The flags are not additive unique-object counts. The parameters and analyzer hash are retained in the private `AUDIO_MEASUREMENT_SUMMARY.json`.

The whole-set per-language object counts are **memberships**, not four disjoint sets: 3,204 measured PCM objects belong to one language, one to two and 32 to all four. This yields 97 extra language memberships above the 3,237 unique hashes. It is not 3,334 separate recordings. A shared hash can be a reused/silent/generic object; it should not be assigned a dub-specific performance merely because it appears under several language rows.

## Source-action cohort audit: the limits of a single vocal arc

A private metadata-only audit (`_research/character_packets/Cantarella/audio_work/CANTARELLA_SOURCE_COHORT_AUDIT.json`, SHA-256 `474420975796e9bb746c72f10735f91f7a1d305bd9fda1ef69039ba6461dbe56`) joins exact selected source actions to the existing line, render and measured-object tables. The seven disjoint cohorts below contain **175/845** selected semantic lines and **700** four-dub render associations, with 700 distinct PCM hashes in this selected subset. All 700 objects passed FLAC/native-PCM integrity and waveform measurement and are mono; 693 meet the declared pitch qualification gate. This is purposive coverage of contrasting situations, not a random sample or the full 845-line perceptual analysis.

| Source-action cohort | Selected lines | Why it is separate |
|---|---:|---|
| Garden encounter, `flow#/6596/3` | 31 | Lethal-plant warnings and hospitality occur in one action; even this cohort is not a pure “temptation” class. |
| Sonoro caveat, `flow#/6862/4` and `6863/1` | 9 | She explicitly warns that the represented past is selective. |
| Current crisis exposition, `flow#/6801/3` and `6811/2` | 64 | Strategic appeal, threat and technical explanation are not survivor testimony. |
| Trial recollections, `flow#/6909/3` and `6915/2` | 18 | Hebenon/Mandragora accounts are Cantarella's retrospectively told memories inside a mediated sequence, not transparent recordings of the trials. |
| Immediate poison handling, `flow#/6916/1` | 8 | A present handling instruction must not be pooled with historical pain or household policy. |
| Escape hint, `flow#/6924/1` | 11 | Her later, partly evasive suggestion that the girls left is a different evidentiary step from the trial recollections or postquest report. |
| Headship/accountability, `flow#/6607/6` and `6620/3` | 34 | Her reply to Cheri and later private explanation/offer have different audiences; Cheri's own objection is not Cantarella-owned audio. |

The qualified *within-dub, object-level* F0 medians are lower in the trial-recollection and headship cohorts than the garden cohort: ZH **190.2 → 173.2 / 175.8 Hz**, EN **187.0 → 179.8 / 168.9**, JA **238.1 → 232.2 / 213.4**, KO **216.0 → 207.1 / 204.8** (garden → trial / headship). This repeated direction is a reason to listen to matched context; it is **not** a proven change from seductive mask to remorse, nor a chronology score. The cohorts contain different words, phonetic distributions, line lengths, narrative states and addressees; none pairs the same sentence across those situations. EN pitch qualification excludes three flagged objects in the main-crisis cohort, one in trial recollections and two in the escape-hint cohort; KO excludes one flagged headship object. No F0 value is promoted to a psychological label.

Exact occurrence-paired median active-frame energy differences versus ZH likewise depend on action. EN ranges from **+0.42 dB** in headship to **+1.74 dB** in main-crisis exposition; JA ranges from **−0.24 dB** in the eight-line poison-handling set to **+1.76 dB** in the eighteen-line trial-recollection set. Every reported comparison has one unique PCM per language/semantic occurrence; no alternative take was silently chosen. These are digital levels, not perceived closeness, dominance or moral seriousness. Changing the silence gate from −50 to −40 dBFS shifts median active duration by **0.16–0.64 seconds** across the cohort/language cells, so a rate or pause claim needs threshold sensitivity and direct listening. The whole corpus still contains flagged multichannel objects outside this clean subset. The seven-cohort report reproduced byte-identically on rerun; the same auditor rejected a nonexistent action before producing an output artifact.

There is an especially important *negative* performance boundary. The accepted Cantarella turns at `flow#/7472/6` (nine mixed-frequency/anti-appropriation items), `7344/6` (six city-tea items) and `7345/5` (seven estate-hospitality items) all have `play_voice: false` in the pinned occurrence crosswalk. They can ground text/choice analysis and future runtime visual questions, but cannot be assigned a heard tone from this selected voice corpus. Nor can the adjacent voiced headship cohort stand in as their performance. The most defensible present conclusion is that a source-defined listening plan is ready, not that Cantarella's four-dub performed persona has been adjudicated.

## Claim-driven four-dub retrieval set

The 23 cases sample caregiving, dream invitation, selfhood beyond the Bane title, desire for air/plain taste, Cartethyia appraisal, trial truth, Hebenon/Mandragora memories, anti-sacrifice judgment, thought/whisper discrimination, Fisalia stigma, the disputed headship/inquiry line, reported return of the girls, the common secrets offer with two alternative replies, and all five rank-up sea images. Each has one resolved EN/JA/KO/ZH text witness and four measured render records; 48/92 render rows have paired null event/numeric-media IDs, while all twenty new ascension renders have both IDs. Cheri's independent objection is contextual text by another speaker, not a Cantarella-owned sound case. The [crosswalk](WUWA_CANTARELLA_AV_HUMAN_RETRIEVAL_CROSSWALK.md) separately nominates seven source-joined trigger lines with explicit event/media IDs and ten story lines with paired-null IDs and 44 PCM-valid renders outside this 23-case JSON; none has human listening. This is a **retrieval index**, not a representative acoustic sample of all 845 lines. Source-witness and rendered-audio language should be checked together; an English subtitle's implication cannot be imposed on the Chinese voice performance.

## Required human layer

A future performed-voice analysis should listen to the full 845-line selected corpus across four dubs if a completeness claim is intended, prioritizing matched high-stakes cases for calibration and revisiting flagged mixtures. Annotators should capture language, line ID, render ID, acoustic context/channel, independently perceived delivery, disagreement and uncertainty. Compare the same semantic occurrence across dubs rather than averaging away script/localization differences. A performed “seductive,” “cold,” “afraid,” “protective” or “playfully dangerous” label is currently **open**. If an object has multiple speakers/effects, abstain or isolate only with a disclosed method. The local files are restricted; the public packet keeps locators and hashes, not voice media.
