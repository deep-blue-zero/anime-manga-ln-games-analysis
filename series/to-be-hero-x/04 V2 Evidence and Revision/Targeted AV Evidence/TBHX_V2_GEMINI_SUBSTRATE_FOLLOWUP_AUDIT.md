---
series: TBHX
artifact_type: targeted_av_evidence_audit
generation: V2
scope: E15-E18_E22_E24_bounded_post_freeze_static_text_followup
status: canonical
source_boundary: Existing Mandarin-primary Bilibili-derived supplied 1fps windows and one retained E24 native screenshot; no new episode admission, continuous playback or acoustic audition
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
last_updated: 2026-10-25
---

# Gemini substrate follow-up — bounded static and text corrections

## 1. Responsibility and acceptance boundary

This audit qualifies the current E15–E18, E21–E22 and E24 handoff audits after inspection of the additional evidence substrate. It corrects failed locators, wrong transcriptions and actor alternatives; it does not replace the original intake receipts. The integration basis is `12e6e328bd8ddffe9c59e3eefd5231131028e566` on `series/to-be-hero-x`. PR340's E09/E24 donor correction is already on that basis and is not repeated.

The separate substrate assessment inventoried 4,583 source files and targeted disputed candidates. All 1,121 previously delivered ZIP members matched their loose counterparts. That identity check does not extend the ZIP checksum scope to the extra windows, which are separately identified below. A file inventory is not a perceptual-coverage claim. Only the nine bounded findings here are promoted by this follow-up; other assessment findings, including E04's dense attack sequence and early-arc glyph/date issues, are outside this change.

Execution: `LOCAL_ONLY`; `TEXT`, `STILL_IMAGE` and `BUNDLE_MEDIATED`; filesystem and image inspection verified through actual reads/views. The author and parallel reviewers inspected selected individual decoded frames, with sheets for navigation. No continuous-AV perception or fresh auditory inspection is claimed. Static credit, UI and caption observations are `F-VIS/SRC`, not `F-AUD` or complete mechanisms. Ordinary windows are supplied 1fps derivatives, not native-rate source episodes. A visible caption is identified as displayed wording; it is not newly certified spoken quotation under method §5.4. Existing native checks and these derivative checks remain distinct.

## 2. Source objects and clocks

The following paths are relative to the supplied external **Arc Bundles** evidence root. All source hashes were rechecked before integration. Local PTS is the decoded-window coordinate. Nominal WEB time is declared start plus local PTS; it is not a newly measured native-frame exposure, shot boundary or BD offset. No source or producer script was modified or executed.

| Finding | Supplied MP4 | SHA-256 | Local PTS seconds / nominal WEB |
|---|---|---|---|
| SUB-01 | `S01E15-E16/windows_1fps/s01e15_w03_0250_0380.mp4` | `128600eca0f61c97bab00b0bbb99ca4521efde108b48b7e44e74b70dc9376680` | 36 / 04:46; MG caption at 40 / 04:50 |
| SUB-02 | `S01E15-E16/windows_1fps/s01e16_w12_1375_1505.mp4` | `834befa3248595169a8442f3f61e6eacdf7f6a33ff7b7afa539b837d3482f9f4` | 79 / 24:14 |
| SUB-03 | `S01E17-E18/windows_1fps/s01e17_w02_0125_0255.mp4` | `4bf88d1f5a9b198b5df0a16a4297e9ebb920335bc3aca4d9d9c94aed3fad3fe5` | 89 / 03:34 |
| SUB-04 | `S01E17-E18/windows_1fps/s01e17_w03_0250_0380.mp4` | `5761d5cc3b666b2a64ed7c9a41b49d2761257175f839f5733072c0de17a77c31` | 35 / 04:45 |
| SUB-05 | `S01E17-E18/windows_1fps/s01e18_w03_0250_0380.mp4` | `8ac87a092ef1d9df4c55a19b0eb65dada3379f086c96df393619ac7778812fc7` | 45 / 04:55 |
| SUB-06 | `S01E17-E18/windows_1fps/s01e18_w09_1000_1130.mp4` | `7880a9f9f17dcfd88fd578c01debcdb70dbd1643414fdd051f9b7e9735c32ee3` | 40 / 17:20 |
| SUB-07 | `S01E21-E22/windows_1fps/s01e22_w12_1375_1505.mp4` | `79d52789e92019101e8c8319763a8b0f8b5469d83c7f6fc15d046514e9386cf9` | 5–21 / 23:00–23:16; clauses at 14–21 |
| SUB-08 | `S01E24/windows_1fps/s01e24_w11_1250_1380.mp4` | `579b98dbda4b7ff84ef8c46b31e86e118d1235b73e23361a395a0da530690a57` | 96 / 22:26; native retained still below |
| SUB-09 | `S01E17-E18/windows_1fps/s01e17_w12_1375_1505.mp4` | `84f4cbeb2c0ea0d0775fe4643eb201920b2ffcd03d7011890555ad140ce18d59` | 77 / 24:12 |

For SUB-08, the decisive small-text witness is the existing 3840×1636 screenshot `03_ai_analysis/s01e24_screenshots/001345_shot-change_00-22-26.417.jpg`, retained under the title's external extraction root. It is 604,276 bytes, SHA-256 `3f29b3ae06510962b3434e2e3c8b1fbbc813b05a72d3c729a7d3bb91cd0fa4be`. Its original-pixel text crop (90,440 to 1090,690; no resizing) hashes to `42efc6ea11a0ac3826281ae0f0a13ec395aaced156880a5567e83a46ca8c9f22`. The native-retained filename/manifest timestamp is a retrieval anchor, not a new cut measurement. The initial low-resolution “seventh” reading was withdrawn; the full-resolution pixels read **第十**. No new full-episode extraction was performed.

## 3. Accepted transitions

### SUB-01

**E15 recruiter — REVISE M15-06.** The card displays `尚德 / SHAND / HERO MANAGER`; a nearby caption invites Wang Yi into MG. This settles the depicted recruitment as Shang De/MG and rejects Zac and Yan Mo/FOMO as equivalent identities for this scene. It does not rewrite the preceding FOMO circulation or later agency history. Specialist 11 §6 and the chronology's Year-20 entry already contain the correct recruitment; the correction belongs in the audit, not a new monograph revision.

### SUB-02

**E16 music credit — REVISE M15-17's title-source premise.** The credit reads `英雄默杀 主旋律 Because of you`: performer **Kris Roche**, lyrics **泽野弘之 / Kris Roche**, composition/arrangement **泽野弘之**. `KONTINUUM` is separately labeled the ending theme. The title and credited artists are resolved as written paratext; the old failure-to-locate remains earlier-pass history. Actual heard recording, scene allocation, mix, performance and the interpretive remainder of `C-V1-105` remain open. The form ledger carries this narrow source qualification; it does not close Document 19.

### SUB-03

**E17 printed year — REVISE M17-01/02; STRENGTHEN P2-CR-C04's anchor route.** The city/Hero Tower image displays `联合18年 / YEAR18 AFTER COMMISSION` at nominal WEB 03:34. The card exists; the previous 03:45/03:05 retrievals failed. Keep this printed city/hospital framing distinct from E18's Year-18 retrospective mission testimony. Do not automatically date retirement, discovery, Nuonuo's birth or every adjacent event from the card. The current calendar table therefore keeps Year19 as the FOMO platform anchor only; the earlier conditional retirement/discovery estimate remains historical rather than jointly dating distinct events.

The dispatch testimony is **Micky's**, already identified in the [frozen E18 §17](../../01%20V2%20Episode%20Deep%20Readings/TBHX_V2_E18_DEEP_READING.md#17-micky-already-knows-the-survey-will-matter), not Luo Tong's separate material-discovery report. This corrects M17-02's earlier actor assignment without a new acoustic-speaker claim. The supplied secondary `S01E17-E18/subtitles/s01e18.bd_en_full.ass` tags Micky for BD14:30.10–14:50.79; its SHA-256 is `2b039036751f45060c530d3c292e5b657de5bc5598d9d95614acdd4ec721af85`. The ASS is a secondary labeled witness, not newly certified DB SDH or Mandarin lexical authority, and its BD clock is not converted by a flat offset.

### SUB-04

**E17 hospital HUD — REVISE M17-03.** The real dashboard pairs organ icons with **heart 80%, lungs 30%, stomach 50%, kidneys 10%**. This corrects both the receiver's absence shorthand and the producer's different organ mapping. The sampled UI does not securely resolve the separate `0%`-viability assertion or establish clinical meaning, diagnosis or an actual recovery probability. The hospital scene is recovered; those stronger claims remain open.

### SUB-05

**E18 notification — REVISE M17-08.** The phone displays `未知联系人 / 别做多余的事` (unknown contact / “Don't do anything unnecessary”). This is a real anonymous warning, not the proposed named Vortex/Big Johnny order. Sender, intended intervention, acoustic reading and native onset remain unresolved. Textual presence does not identify its author.

### SUB-06

**E18 tank — REVISE M17-12's failed-locator verdict.** The supplied frame shows a humanoid in a purple tank and `FUSION IN PROGRESS`, `LOADING`, `EXPERIMENTAL DATA DETAILS` and completion-rate UI. This recovers the scene. Exact 30/78 values, production scale, operator/ownership and a complete clone-production chain remain unverified. Neither a tank image nor its label proves a universal ontology or a named mastermind.

### SUB-07

**E22 ending — REVISE E21E22-C08's quotation and locator.** The supplied ending window shows Yan Mo observing a monitor and then X looking back. At local PTS14–21 the displayed clauses are `原来是这样 / 这下 / 我可抓到你了`. The previous audit's `他发现我们了` and reported 20:45–21:20 locator are superseded for this scene. The diegetic surveillance/discovery reading survives. No new acoustic speaker certification, exact gaze/sound synchronization, all-observer knowledge or literal fourth-wall awareness follows. Existing chronology/language/institutions wording already preserves the correct clauses, so it is not rewritten.

### SUB-08

**E24 public replacement account — STRENGTHEN/REVISE E24-C11's evidence qualification.** The FOCUS post reports Nice replacing **tenth-ranked E-Soul** to qualify and Treeman arranging **Nice and Lin Ling's dual entry**. This supplies an attributed public account behind the already secure separate presentations. Its Fear explanation is explicitly marked `可能` and expert/media attribution; neither literal resurrection nor continuous Original Nice personhood is established. The full current roster/order remains open under E24-D02. The institutions and public-narrative ledgers carry this account as reporting, preserving its distance from private continuity; P2-CR-C08's latest-convergence/ordinal proposition is unchanged. Specialist 06 already preserves dual entry and the unresolved mechanism, so no monograph revision is required.

### SUB-09

**E17 music credit — REVISE M17-16's title-source premise.** The page reads `英雄大小强 主旋律 growL`: performer **J.Rio**, lyrics **cAnON.**, composition/arrangement **Misaki Umase**. Acceptance review corrected the preliminary 小小强 transcription to 大小强; the title and artist readings are unchanged. Resolve those written credits only. Audible scene allocation, delivery, synchronization and interpretation remain open; neither a title nor an audio stream is a listening receipt.

## 4. Propagation, preservation and remaining work

The existing permanent packets `TBHX-AV-E15-001`, `TBHX-AV-E17-001`, `TBHX-AV-E21-001` and `TBHX-AV-E24-001` retain their identities. Their four arc audits, current claim/evidence routes and appropriate chronology/form/institutions/public-narrative homes receive the bounded corrections above. No new master claim key or permanent packet is created. The receiver's original failed samples remain traceable as earlier-pass history; wrong retrieval is distinguished from an absent scene.

The source/clock, acoustic, motion, named-sender/operator, mechanism and complete-roster portions of the existing debts remain open. Static credit recovery narrows credit identity only. No fresh full-season AV coverage, Phase-5 closure, Documents 18–20 synthesis, new episode reading or later-phase execution is certified. Frozen E01–E24 bodies, Part-II histories, original checkpoints and all unselected assessment findings are preserved.

Bounded name/reference review covered all nine findings and their cumulative notes. Shang De, Wang Yi, Yan Mo, X, Nice, Lin Ling and E-Soul remain identifiable; phone-sender anonymity and Original Nice's private-continuity uncertainty are required rather than repaired by invented names. Written performer attribution is not character-voice attribution.

The [follow-up checkpoint](../../99%20V2%20Archive%20and%20Delivery/TBHX_V2_GEMINI_SUBSTRATE_FOLLOWUP_CHECKPOINT.md) records this tranche's exact change boundary. Raw media, screenshots, private working receipts and producer transcripts remain external to analytical Git.
