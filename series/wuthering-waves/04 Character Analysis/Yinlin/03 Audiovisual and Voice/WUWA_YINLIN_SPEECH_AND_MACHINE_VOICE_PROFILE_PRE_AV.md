---
series: WUWA
character: Yinlin
artifact_type: speech_machine_voice_profile
analytical_responsibility: "Textual register, multilingual semantic hinges, source-linked audio measurements, and listening limits"
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

# Yinlin — textual speech and measured voice, pre-AV

This profile separates utterance content, audience/reveal state, audio signal, and performance interpretation. The [fifteen-case join](AUDIO_MATCHED_SEMANTIC_CASES.json) stores semantic occurrence IDs, exact text keys and locators, four language-render IDs, WEM/PCM/FLAC hashes, durations, energy, pitch gate results, and QC flags without publishing recordings. The [source audit](../04%20Validation%20and%20Readiness/WUWA_YINLIN_SOURCE_CENSUS_CHRONOLOGY_AND_IDENTITY_AUDIT.md) and [claim matrix](../01%20Evidence%20and%20Source-Facing/WUWA_YINLIN_EVIDENCE_AND_FALSIFICATION_MATRIX.md) govern identity and chronology. Chinese is the selected semantic anchor; EN/JA/KO are localization witnesses. No dub has been human-listened for this packet.

## Textual speech modes are audience-sensitive

Her professional voice can be a direct tactical proposition. At 1004/6 she names a covert investigation and offers Rover a way to help. At 1006/7 the short disclosure represented by Character_YinLin_21_18 names the device as both eavesdropper and tracker; concision is not evidence of harmlessness. Character_YinLin_44_10 is a small request to trust her inside a staged hostage switch, not a timeless guarantee that trust is safe. Her words to Patrollers, Society members, Dollmaker, and Rover have different information costs. [YIN-E11–E16](../01%20Evidence%20and%20Source-Facing/WUWA_YINLIN_EVIDENCE_AND_FALSIFICATION_MATRIX.md#evidence-bundles)

Her more reflective speech links identity, work, grief, and responsibility. Character_YinLin_42_9 recounts being orphaned and taken in by the Dollmaker, but it occurs amid an unstable Society-facing reveal. Character_YinLin_48_25 objects that their own people remain in the factory. Character_YinLin_51_17 asserts that loss of a recognized official identity will not erase her chosen action. Character_YinLin_58_34 confesses that a reunion fantasy was hard to destroy despite its cost to others. Character_YinLin_58_45 tentatively entertains trusting Rover in the later explanation. A model should be able to speak with this moral specificity while also preserving the earlier tracking and shock; it should not give the final explanatory register to a state before the confrontation. [YIN-E14–E19](../01%20Evidence%20and%20Source-Facing/WUWA_YINLIN_EVIDENCE_AND_FALSIFICATION_MATRIX.md#evidence-bundles)

Archive speech permits a third register: social invitation, teasing, and craft talk. FavorWord_130205_Content contrasts replaceable work personae with the attraction of being remembered by her own name; _130206_Content explains how puppet theater is both tradition and camouflage; _130208_Content prizes the maker's skill in a simple rice dish (English also says “care”); _130213_Content turns an ordinary birthday into a request for a whole day together. She can say such things without every line being a surveillance maneuver, but the archive context does not prove they happened at a particular point in the quest. [YIN-E07–E09](../01%20Evidence%20and%20Source-Facing/WUWA_YINLIN_EVIDENCE_AND_FALSIFICATION_MATRIX.md#evidence-bundles)

The festival public apology, later admission of a performed mistake, and free show in 3987–3992 and 4231/1 are important to her speech model but are **source-unvoiced in the selected mapping**. Their absence from the matched audio cases is not absence from the character's text evidence. The apology cannot be isolated from the later reveal as proof of genuine investigative error. Conversely, four accepted Test/123 occurrences in rows 648–649 have no useful literary or vocal content and must never be learned as her vocabulary. [YIN-E21–E23](../01%20Evidence%20and%20Source-Facing/WUWA_YINLIN_EVIDENCE_AND_FALSIFICATION_MATRIX.md#evidence-bundles) [YIN-C23](../01%20Evidence%20and%20Source-Facing/WUWA_YINLIN_EVIDENCE_AND_FALSIFICATION_MATRIX.md#claims-counterreadings-and-revision-tests)

## Material localization hinges

The Chinese Character_YinLin_58_45 is modal: she says that with Rover she *perhaps* could trust without conditions. The English version sounds more assured, implying she can always trust Rover's words. The primary-grounded model should preserve the tentative nature of this step, and the wording in neither language cancels her established operational caution. In Character_YinLin_51_17 the Chinese emphasizes doing what she wants in her own way independently of official identity, while English explicitly frames this as doing what is right; the ethical reading is supported by the wider confrontation, not by assuming the two sentences have identical semantic focus. In Event_WWPDJSBF_4_29 Chinese describes painful responsibility that someone must bear for Jinzhou's safety, while English sharpens it to “dirty work.” The later choice is costly in both; English's phrase should not alone license a generalized self-concept of moral contamination.

Targeted four-language comparison adds further constraints. In FavorWord_130209_Content, Chinese explicitly permits repellent target food but emphasizes disliked dining companions; English says she truly dislikes no dishes, while Korean initially broadens the aversion to eating with others before excepting Rover. In FavorWord_130213_Content, Chinese, Japanese and Korean pledge no lie on the birthday; English substitutes “not playing any games” and intensifies the invitation as “all to myself.” At `3992/7/19` (`Event_THCQDYBF_20_29`), English adds “You are... the only one” to the scene's mask-free-with-Rover statement. Ascension V, `FavorWord_130253_Content`, asks whether a special power signals trust in her skill or a personal feeling; the second possibility ranges from JA goodwill/friendship to KO love, while ZH speaks of liking and EN affection. She welcomes direct emotion, but no recipient reply or relationship status is recorded. Ascension II's EN “unbreakable will” is stronger than the ZH/JA/KO resilient-spirit formulation. These witness differences do not establish an exclusive canon relationship, psychological invulnerability, a permanent truth pledge, or a stable hatred of all shared meals. They are selected semantic hinges, **not** a completed line-by-line Japanese/Korean audit or evidence about audible delivery. [YIN-E29–E32](../01%20Evidence%20and%20Source-Facing/WUWA_YINLIN_EVIDENCE_AND_FALSIFICATION_MATRIX.md#evidence-bundles)

## Full local signal pass

The selected collection contains **439 semantic voiced lines**: 374 story and 65 archive. It preserves **1,776 runtime render associations** across English, Japanese, Korean, and Chinese. The local manifest contains 1,729 object rows, including four repeated PCM rows; the run measured **1,725 distinct FLAC/native PCM objects**, with zero failures. The generic adapter to the Sigrika waveform analyzer (version sigrika-waveform-analysis-0.2.0; analyzer SHA-256 73c2904c38d06440a86a572d05fa3fe200e23055e68f0aeaec3be75313d3c4a2) verifies FLAC bytes and interleaved native s16le payload hashes, chooses the highest-native-RMS channel without interpreting it as an isolated speaker, resamples to 16 kHz, and records gated activity, energy, pitch/harmonicity, and spectral proxies. Full object-level results stay in the private local extraction workspace under _research/character_packets/Yinlin/audio_work/. This pass validates the already decoded collection; it does not independently re-decode every original WEM.

| Language | Distinct measured objects | Summed object duration | Median object duration | Qualified pitch objects |
|---|---:|---:|---:|---:|
| English | 435 | 2,270.56 s | 4.23 s | 430 |
| Japanese | 430 | 2,577.07 s | 5.27 s | 427 |
| Korean | 430 | 2,609.32 s | 5.19 s | 428 |
| Chinese | 430 | 2,563.02 s | 5.23 s | 424 |

The four object-count denominators differ because semantic lines, render associations, and PCM identities are separate. Durations sum selected object lengths, not story time or a comparable rate of speaking. QC flags, which overlap, include 60 multichannel-not-isolated objects, nine with too few voiced pitch frames, five pitch-parameter-sensitive objects, four frequent pitch-edge estimates, four full-scale-sample warnings that are not proof of audible clipping, and one very short object. The stated pitch gate qualifies 1,709/1,725 objects, but that does not make a cross-dub median an actor or emotion comparison. Different texts, mixing, direction, silence, and segmentation remain material confounders.

## Source-defined scene contrasts and render variants

The [sixteen-cohort audit](../04%20Validation%20and%20Readiness/WUWA_YINLIN_SOURCE_DEFINED_AUDIO_COHORT_AUDIT.md) makes a more discriminating test than a whole-corpus median. Exact source action and TalkItem selections divide `1004/6` into private case exposition, Rover's risk/offer, and child-facing care; `1006/7` into postfight approach, tracker admission, and subsequent tactics; `353/6` into postcase account, grief/complicity, and tentative future trust; and `15092/6` into later off-duty presence and chosen covert work. The cohort union has **181 unique semantic story lines** (41.2% of 439 selected voiced lines), **728 unique render associations**, and **725 distinct measured PCM objects**. These are purposefully selected contrasts, not a complete speech analysis or a played route. Several action segments include alternative replies that cannot all be heard in one run.

The EN-minus-ZH paired −45 dBFS active-level median is approximately flat at the puppet explanation (−0.02 dB, 15 pairs) and Rover risk/offer (−0.07 dB, 15), positive at guardian reveal (+2.68 dB, 21), living-people objection (+4.08 dB, six), vocation without an official file (+4.71 dB, eleven), and grief/complicity (+4.30 dB, fourteen unambiguous pairs), then negative at later party-as-self (−2.14 dB, six) and renewed covert duty (−0.81 dB, fourteen). The direction changes with selected action and source state. It does **not** establish that the English performance grows louder with honesty, that Chinese is quieter as a character trait, or that either dub has a singular mask-off register. Text differences, recording gain, scene treatment and segmentation are live alternatives. Within `1006/7`, the tracker-admission median is not a universal level spike: ZH's three action-subset medians are −22.63/−23.35/−22.37 dBFS, EN's −22.78/−22.75/−22.80, JA's −22.22/−24.81/−22.94, and KO's −20.86/−21.52/−21.52. Even this closer within-action contrast does not control wording or listener context. The pitch gate accepts 723/728 associations, but a qualified F0 number does not label sincerity, coercion, eroticism, fear or tenderness. [YIN-C32](../01%20Evidence%20and%20Source-Facing/WUWA_YINLIN_EVIDENCE_AND_FALSIFICATION_MATRIX.md#claims-counterreadings-and-revision-tests)

There is also a concrete identity trap at `353/6/28` (`Character_YinLin_58_36`). One semantic occurrence maps to two runtime render IDs in *each* language; EN's two associations contain distinct canonical PCM, while the two JA, KO and ZH render IDs in each language alias one PCM object. Thus 181 × four gives 724 baseline associations; that occurrence adds four associations but only one distinct PCM beyond the baseline, giving 728/725. Counting render IDs as independent takes inflates JA/KO/ZH; collapsing by text key erases the English sound variant. The paired-level audit excludes the EN-distinct occurrence where a single value would be arbitrary. Runtime dispatch and what a particular player heard remain unobserved. [YIN-C33](../01%20Evidence%20and%20Source-Facing/WUWA_YINLIN_EVIDENCE_AND_FALSIFICATION_MATRIX.md#claims-counterreadings-and-revision-tests)

The earlier festival/free-show material must be kept in another medium bucket. The pinned crosswalk marks 48 accepted Yinlin turns across `3987/6`, `3991/6`, `3992/7`, and `4231/1` as `play_voice: false`; none appears in the selected playable-line analysis. They remain textual evidence for her staged investigative mistake, chosen public craft and invitation, but there is no measured or listened earlier-festival delivery here. The *later* party/dossier action `15092/6` has twenty selected voiced lines; its PCM cannot be borrowed to describe the earlier festival. This is a selection-level statement, not proof that no client ever contains an earlier asset. [YIN-C34](../01%20Evidence%20and%20Source-Facing/WUWA_YINLIN_EVIDENCE_AND_FALSIFICATION_MATRIX.md#claims-counterreadings-and-revision-tests)

## Fifteen source-defined four-dub cases

These cases were chosen for contrasting speech situations, not because their durations prove delivery. Each has four mapped render associations; the table gives EN / JA / KO / ZH object durations in seconds. All 60 selected renders have no listed QC flag, but their full hashes and locators belong to the JSON join.

| Exact key | Speech situation | Durations EN / JA / KO / ZH |
|---|---|---|
| Character_YinLin_21_18 | Tracker admission | 4.77 / 6.96 / 7.61 / 6.65 |
| Character_YinLin_42_9 | Guardian/orphan account under cover | 6.73 / 3.51 / 12.28 / 5.75 |
| Character_YinLin_44_10 | Trust request in staged coercion | 2.16 / 2.64 / 2.04 / 2.89 |
| Character_YinLin_48_25 | Concern for workers still inside | 2.61 / 2.10 / 2.61 / 1.76 |
| Character_YinLin_51_17 | Vocation beyond official identity | 5.15 / 8.21 / 4.73 / 6.07 |
| Character_YinLin_58_34 | Confession of delayed resistance | 8.34 / 7.72 / 7.08 / 6.78 |
| Character_YinLin_58_45 | Tentative possibility of trust | 6.33 / 3.98 / 3.22 / 5.78 |
| Event_WWPDJSBF_4_29 | Later undercover duty's cost | 6.61 / 11.90 / 9.75 / 11.90 |
| FavorWord_130205_Content | Identity remembered without cover | 30.43 / 35.56 / 30.43 / 30.43 |
| FavorWord_130206_Content | Puppet craft and public camouflage | 28.08 / 28.08 / 28.08 / 28.08 |
| FavorWord_130208_Content | Rice and value of craft | 22.30 / 22.30 / 22.30 / 22.30 |
| FavorWord_130213_Content | Birthday/day invitation | 25.70 / 25.70 / 25.70 / 25.70 |
| FavorWord_130222_Content | Resilient spirit beyond raw strength | 8.69 / 8.69 / 8.69 / 8.69 |
| FavorWord_130224_Content | Shared purposeful use of power | 10.85 / 10.85 / 10.85 / 10.85 |
| FavorWord_130253_Content | Trust-in-skill versus personal liking | 22.08 / 22.08 / 22.08 / 22.08 |

Several long archive cases have exactly equal durations across otherwise distinct language PCM objects. That pattern is a **timing/packaging observation**, not evidence of identical delivery or speech rate. The next pass should hear the exact mapped render in each language and record audible facts, competing interpretations, context, and confidence; visual synchronization is needed wherever a gesture or frame could reverse a line's apparent pragmatic force.

## Current inference boundary

Text supports a flexible speech model: tactical withholding, controlled roleplay, risk-aware directives, explicit ethical confrontation, confession without total self-excusal, and later ordinary/social play. The audio supports source-linked retrieval, integrity, and quantitative signal selection. It does not yet support claims that any language actor sounds seductive, cruel, frightened, warm, exhausted, or newly sincere. Such labels can be used in a fictional performance brief only as creative choices, not as observed canon.
