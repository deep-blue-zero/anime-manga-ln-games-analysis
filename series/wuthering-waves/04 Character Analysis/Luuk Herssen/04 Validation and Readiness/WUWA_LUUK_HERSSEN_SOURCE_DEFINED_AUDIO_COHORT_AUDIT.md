---
series: WUWA
character: Luuk Herssen
artifact_type: source_defined_audio_cohort_audit
scope: LUUK_HERSSEN_PINNED_3_6_0_TEXT_AUDIO_PRE_AV
analysis_generation: LUUK_HERSSEN_PRE_AV_V0_1
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

# Luuk Herssen — exact-action sound cohorts and performance limits

Luuk's source invites an appealing vocal story: a careful physician becomes a piercing opponent, then relaxes into food, a cat and mutual support. The written changes are real; whether their *performed* delivery follows that trajectory is a different question. This audit joins exact accepted source occurrences to the existing official-client-derived decoded-object measurements. It is metadata-only: no audio is embedded here, no four-dub human listening was performed, and no runtime option was observed being selected. Read with the [speech profile](../03%20Audiovisual%20and%20Voice/WUWA_LUUK_HERSSEN_SPEECH_AND_MACHINE_VOICE_PROFILE_PRE_AV.md), [audio QC audit](WUWA_LUUK_HERSSEN_AUDIO_QC_AND_COMPARABILITY_AUDIT.md) and [evidence matrix](../01%20Evidence%20and%20Source-Facing/WUWA_LUUK_HERSSEN_EVIDENCE_AND_FALSIFICATION_MATRIX.md).

## Eleven disjoint selections

The eleven selectors below cover **127 distinct semantic lines**, or 17.7% of the selected 719, and **512 render associations with 512 distinct canonical PCM hashes**. Every object is present in the existing 2,855-object integrity-valid measurement table. Selected lines include route alternatives, not a claim that all 127 played in one traversal. These are purposive contrasts across different source situations, not a random or complete voice sample.

| Cohort | Exact selector | Lines / render associations | Question kept open |
|---|---|---:|---|
| Clinic uncertainty | `10719/5@1-12` | 12 / 50 | Does a careful, non-omniscient first appointment have a distinct delivery? The two hidden-ID opening turns are only contextually accepted as Luuk. |
| Sigrika counseling | `12313/3@0+2-3+5-6+8-9+11` | 8 / 32 | Does he give conjectural support without making the student disclose? |
| Rover counseling and disclosure | `12313/3@13+15-17+19-20+25-26+28+30-32+34-36+39-41+43+45+47` | 21 / 86 | The same action moves from slowing Rover down to covert-role and factional-risk information; it is not one undifferentiated therapeutic register. |
| After-shock care | `12330/4` | 6 / 24 | He tends Nivora, allows recovery time, then investigates; care is not evidence of perfect psychological diagnosis. |
| Architect challenge | `12331/4` | 7 / 28 | A forensic, personal confrontation need not be acoustically reducible to loud anger. |
| Architect inference | `12332/3` | 9 / 36 | He calls earlier conclusions hypotheses until the opponent acts; certainty has a source-timed threshold. |
| Waffle praise route | `15461/5@6-8` | 3 / 12 | Rover's approving option leads to one three-line response, including a food-making invitation. |
| Waffle critique route | `15461/5@9-11` | 3 / 12 | Rover's critical option leads to a different three-line response and revision offer. |
| Ordinary Academy labor | `15461/5@14-29+31-32` | 18 / 72 | Students, clinic load, N.A.N.A. repairs, a joke and future cooking sit in one action with another option later; “domestic” is not free of work. |
| Cat-care planning | `15473/2` | 19 / 76 | Food, space, toys, checkup, Rover's help and Luuk's limits appear together. |
| Cat freedom and leave | `15475/5` | 21 / 84 | Real local paid leave, the semi-free cat and a grave/witness reflection share a later action; it is not one unbroken relaxation speech. |

The raw `ShowTalk` in `15461/5` makes the waffle comparison a **branch control**: the item-5 Rover option jumps to TalkId 7 or 10. Luuk's source TalkItems 6–8 (`Side_LHSCP_2_9–11`) are the approving route; 9–11 (`Side_LHSCP_2_12–14`) are the critical route. Each final line jumps to TalkId 13. The two three-line sets are acoustically comparable *alternatives*, not six consecutive things Luuk says to one response. Item 5 itself is the player option and is not a Luuk voiced line [LUK-E26].

Source/render identity is not one line per language in every case. Two clinic occurrences (`10719/5/2` and `/9`) each have two distinct Japanese PCM variants; two Rover/disclosure occurrences (`12313/3/43` and `/47`) each have two English variants. Thus 127 lines would have 508 one-per-dub associations, but there are 512. The auditor excludes ambiguous multi-object occurrences from its one-object-per-language paired-level statistic rather than silently selecting a friendly filename. The exact render ID and hash remain necessary for future listening.

## What the measured signal can and cannot say

The pre-existing analyzer uses a −45 dBFS active-frame gate and a conservative qualified-F0 filter. Median active levels in the clinic cohort are ZH −24.03, EN −23.53, JA −24.41 and KO −24.00 dBFS; the Architect-challenge medians are ZH −23.56, EN −23.44, JA −24.85 and KO −23.34. The challenge is slightly higher in ZH/EN/KO but lower in JA. These different scripts, durations, mixes and sound scenes do not support a universal “forensic anger is louder” rule or an inference that he is emotionally cool in Japanese. Compared with the clinic, the later cat-care cohort is also mixed by dub (ZH −23.28, EN −23.87, JA −21.31, KO −26.33). Raw median levels are descriptive file properties, not volume-matched perceptual judgments.

Pitch is less comparable still. In the twelve-line clinic selection, only **1/12 ZH and 0/12 KO** objects pass the conservative F0 gate, versus 11/12 EN and 12/14 JA renders. All six ZH and KO after-shock-care objects fail that gate; cat-care planning qualifies only 1/19 ZH and 5/19 KO. The whole-corpus [QC audit](WUWA_LUUK_HERSSEN_AUDIO_QC_AND_COMPARABILITY_AUDIT.md) already found 21.3% and 25.9% qualification shares for ZH and KO against 96.1% EN. These source-matched subsets show the disparity persists where a character claim might otherwise be tested. Neither a cross-dub F0 ranking nor a within-dub physician→opponent→care arc is warranted from such selected remainders. An independent tracker, acoustic segmentation and actual listening may clarify the cause; this report does not guess it.

Even the same-action waffle routes resist an easy warmth-versus-disappointment shortcut. At −45 dBFS the praise/critique medians are ZH −24.85/−24.54, EN −23.00/−22.57, JA −19.84/−21.10 and KO −24.83/−24.59 dBFS. The direction differs in JA, each route has only three lines per dub, and the text itself differs. One could listen for a delivery distinction while preserving the branch and text; the signal numbers alone neither prove nor disprove one. Luuk's written willingness to revise a recipe after criticism remains a source fact [LUK-E16, E26].

Two character-relevant actions are **accepted but source-unvoiced in this selection**. `15474/1` has eleven accepted Luuk message turns, including leave plans and a revised waffle invitation; `15914/1` has nine accepted message turns, including the cat-safe waffle-lure warning. All twenty are `play_voice: false` in the pinned occurrence crosswalk and absent from selected voice-line analysis. Their text belongs in a behavior model and medium-aware relationship history, but not in a claim about how he sounded when sending them. An unavailable selected render is not proof no related client recording exists in any later build [LUK-E24, E27].

## Reproduction and next evidence gate

The private audit is `_research/character_packets/Luuk Herssen/audio_work/LUUK_SOURCE_COHORT_AUDIT.json`, SHA-256 `00199988c6959545f6249eb61e62d19f7a4961a73bdbb0d8b9e05f8f25dcd95e`. It binds the pinned line-analysis and measurement-table hashes and stores each member's source locator, semantic occurrence, text key, dub, render-analysis ID, PCM/FLAC hashes and QC flags. Recreate it with `scripts/audit_character_audio_cohorts.py 'Luuk Herssen'` and the eleven literal `--cohort NAME=selector` values above, then `--output` to that private path; the second run produced the same SHA-256. A selector for unvoiced `15474/1` and an overlapping within-cohort waffle selector both failed nonzero without writing their intended output files. The auditor permits overlap *between* named cohorts, so the reported 127 distinct occurrence IDs and 512 distinct render IDs were separately checked for disjointness. The selected object table says all 512 are integrity-valid; it is not a fresh re-decode of all source WEMs.

Next, listen line by line in four languages with exact variant IDs, including both waffle routes as separate hypothetical traversals, and inspect runtime choice/staging before asserting what a player hears. Review clip boundaries and the KO/ZH pitch failures with an independent tracker or manual pitch inspection before estimating sustained cross-context vocal changes. **PRESERVE** the written role and branch distinctions; **DOWNGRADE** a simple acoustic physician→opponent→domestic-personality arc; **OPEN** the acted delivery, message-medium sound availability outside this selected generation, and the source of the pitch-gate skew. No draft authority is promoted by these measurements.
