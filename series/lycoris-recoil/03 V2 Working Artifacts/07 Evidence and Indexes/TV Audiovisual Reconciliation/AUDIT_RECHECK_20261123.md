---
series: LYCORIS_RECOIL
artifact_type: evidence_index
generation: V2
status: canonical
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
scope: attributable speaker, addressee and object rechecks from the 2026-11-23 proportionality audit of TV E01–E13 and one Short 01 ledger row
source_boundary: TV E01–E13 and Friends Short 01 only
analytical_base: 016904e42d49db1f5d5877c5daf89bd0c9f0aeff
---

# TV audit recheck · speakers, addressees and one gift

On 23 November 2026 two independent auditors read the complete Japanese dialogue of all nineteen anime units against the frozen readings, the current ledgers and the three lead syntheses:
- `claude/av-auditor-tv1` covered E01–E07;
- `claude/av-auditor-tv2` covered E08–E13 and Shorts 01–06.

Both judged every unit's reading proportionate to its substrate. They also found speaker, addressee and object errors that had survived the earlier reconciliation.

A separate verifier, `claude/av-verifier`, formed its own view of thirteen items from the cues and frames before reading each audit entry. The integrator `claude/integrator` independently checked five decisive items:
- E05 C0169–0170;
- E06 C0318–0320;
- E10 C0440–0441;
- E11 C0430;
- E12 C0471–0473.

Nobody listened to the audio for this record. Where speaker identity depends on voice alone, the item stays OPEN.

## How to read the locators

- **Cue numbers** (`C####`) are the 1-based index of `Dialogue:` lines in `01_subtitles/source_japanese_corrected/tv/ep##.japanese.corrected.ass`, the same numbering [SOURCE_RECHECK_20261123](SOURCE_RECHECK_20261123.md) uses.
- **Frame numbers** (`#000000`) are the numbered episode bundle images in `03_ai_analysis/ep##_screenshots/`, whose filenames carry their master timecode.

## Dispositions

The frozen readings keep their historical text. The dispositions below govern current use of the affected claims, ledger rows and synthesis passages.

| Cue and interval | Line (short) | Earlier attribution | Disposition | Decisive evidence |
|---|---|---|---|---|
| E05 C0169–0170, 09:34.85–09:42 | つまり 命と引き換えに… / 千束の使命は なんだい？ | Mika | **REVISE**: Kurumi infers and asks; Mika answers only それは千束が決めることだ (C0171) | #000508 (09:34.850) shows Kurumi speaking under C0169. C0168 is the tagged Mika line. Verified by the auditor and the integrator. |
| E06 C0318–0320, 15:16.19–15:22 | そうですか！ … たきなはクビになりました | Takina | **REVISE**: Mizuki. Takina's first response is 映像は それで全部ですか？ (C0322) | #000789 (15:21.650) shows Mizuki speaking with hands raised while Takina's mouth is closed. Mika answers やめろ ミズキ (C0321). Verified by the auditor and the integrator. |
| E06 C0450, 21:03 | ああ… ごめん たきな | Chisato | **REVISE**: Kurumi | #001102 (21:00.843) and #001107 (21:06.000): Kurumi looks up, then bows in seiza. Auditor and verifier. |
| E10 C0440–0441, 22:20.73–22:30 | 延空木は… / あの２人も お前同様 私の優秀な教え子だからな | Chisato | **REVISE**: Mika, addressing Chisato. Chisato answers うん！ (C0442) | #001036 (22:27.115): Mika speaks with his hand on Chisato's head. The line calls Takina and Fuki his pupils. Auditor and integrator. |
| E11 C0430, 22:21.99 | ハッ お前には用がない って言ったろ | Takina | **REVISE**: Majima | #001185 (22:21.924) shows Majima aiming. The line repeats his earlier dismissal of Takina. Auditor and integrator. |
| E02 C0169, 09:08.40 | 日本で一番 警戒されない姿だってことですよ これ | Takina | **REVISE**: Chisato | #000534 (09:10.840): Chisato speaks while pinching her own sleeve, the これ of the line. Auditor and verifier. |
| E03 C0353, 17:11.39 | あいつは任務以外で 戦えるようなヤツじゃない | Chisato | **REVISE**: Fuki. Chisato's reply 人を見る目がないねえ predicts that Takina will come | The cut to Fuki (#000885) spans C0353, and the cut back to Chisato (#000888) spans C0354–0355. Auditor and verifier. |
| E04 C0247–0248, 12:28.06–12:30 | チンアナゴよりも？ / ちゃかすなら もういいです | C0247 to Takina; C0248 unquoted | **REVISE**: C0247 is Chisato's tease. **ADD**: C0248 is Takina refusing to be teased off a serious question | #000708 (12:29.650): Takina's mouth is open under C0248. Auditor and verifier. |
| E08 C0215–0222 | もしもし 山岸先生？ たきなです | Takina calls Yamagishi | **REVISE**: Takina answers Yamagishi's incoming call on Chisato's phone | #000638–#000642: incoming-call screen, then Takina at the phone. Auditor and verifier. |
| E08 C0447–0448 | the "foreign object in my body" explanation | said to Takina | **REVISE**: said to Himegama, disguised as the clinic nurse | C0446 and C0450 are tagged （姫蒲）. #001147 and #001151 show only the nurse and Chisato. Auditor and verifier. |
| E12 C0157, 08:46 | これじゃ 死なんぞ | merged into Chisato's check of the wound | **REVISE**: Yoshimatsu | #000592 (08:46.000) shows him speaking. Auditor and verifier. |
| E12 C0115, 06:47–06:49 | 狂ってる | Chisato | **OPEN**: withdraw the Chisato attribution | The cue falls inside a Takina close-up and is untagged. No frame shows lips. |
| E01 C0237, 09:28.92 | 新しいお友達の たきなおねえちゃんだよ | Chisato | **OPEN**: needs a synchronized listener | It plays over Chisato and Takina while the daycare worker is off-screen, and is untagged after the worker's tagged C0236. Do not use it for `CHI-SOC-INIT-01` until heard. |
| E10 C0268–0271 and C0341, 13:50–18:00 | the coming-of-age photograph | Chisato asks Mika to photograph her (E10-VIS-003) | **DOWNGRADE**: the shutter (C0268, #000641) precedes any request. Chisato asks for Mika's opinion (C0271, C0341) and asks him to send the photo to Yoshimatsu (C0281) | Auditor and verifier. |
| Short 01 C031–0032 | "ウチは居酒屋じゃない！" って / もう提案済みでしたか | `TAK-MB-SHORT01-002`: Mika proposed yakitori first | **REVISE**: someone had already proposed it and it was refused. Mika is at most the one who refused; no line names the first proposer | #000075. The Short 01 reading itself is correct. Auditor and verifier. |

## The E12 bag and the E08 charm

The repository owner asked whether Chisato's E12 retrieval concerns the bag, the charm or both.

**Ruling: both, with distinct roles.**
- At C0471 (22:09.10) Chisato exclaims 「あ～っ 私のバッグ！」 (#001291) and turns back for her own bag.
- At C0473 (22:15.31–22:17.77) she cradles it and says 「ほら これ！ たきなに もらったやつ」. The red-bandana pug charm hangs on its front panel (#001296–#001298).
- The satchel is the standard Lycoris bag. Takina's gift is the charm: E08 C0419–0424 (20:00.37–20:08.79), 「欲しかったんでしょ？」 / 「くれるの？」 / 「おお～ イッヌ！ かわいい！」, with the pug strap handed over at #001098.
- The gift answers Chisato's public request at E08 C0190, 「私も たきなのプレゼント欲しい～」, which Takina had rebuffed with 「子供ですか！」 (C0191).

**Current use.** E12-CLM-046, the E12 reading's §24 heading and the three syntheses call the satchel "the bag Takina gave her". Read instead: *Chisato turns back for her own bag and names the charm on it, Takina's E08 gift, as the reason.* The retrieval's exposure to Majima's renewed ambush (C0474–0476) stands as recorded.

## Evidence not previously routed

These beats were confirmed by the auditor, the verifier or both. They enter current use as additional evidence and alter no frozen judgment.

- **E09 C0075–0077 (05:50–05:58).** Chisato tells Mizuki 「たきな 意識しちゃってるね」 / 「だから言いたくなかったんだよな～」. This is her only stated reason for withholding her condition from Takina. Both lines are tagged （千束）, and Mizuki answers.
- **E03 C0272 and C0462.** Takina's last 千束さん is C0272 (13:21.95); her first bare 千束 is C0462 (22:08.64). No later 千束さん from Takina occurs in E03–E13 or the shorts.
- **E08 C0190 → C0419–0424 → E12 C0471–0473.** The charm arc above.

## Affected records

- **Readings.** The frozen E02, E03, E04, E05, E06, E08, E10, E11 and E12 readings keep their text.
- **Revision ledger.** Current-use notes in the [V1-to-V2 claim revision ledger](../../03%20Longitudinal%20Ledgers/LYCORIS_RECOIL_V1_TO_V2_CLAIM_REVISION_LEDGER.md) qualify:
  - `REV-E05-002`;
  - `REV-E06-002`;
  - `REV-E10-003` and `REV-E10-010`;
  - the `E11-AUD-014` evidence.
- **Character ledger.** The [character ledger](../../03%20Longitudinal%20Ledgers/LYCORIS_RECOIL_CHARACTER_STATE_AND_MICROBEHAVIOR_LEDGER.md) notes qualify:
  - `TAK-MB-E06-004`, and `E06-AUD-003`, which measures Mizuki's voice, not Takina's;
  - `CHI-MB-E10-004`, `CHI-DISTRIBUTE-HERO-01` and `NEG-E10-REL-001`;
  - `TAK-MB-E11-004`;
  - `TAK-MB-SHORT01-002`;
  - `CHI-SOC-INIT-01`'s E01 support.
- **Relationship ledger.** It routes the E10 snapshot, the E12 bag and charm, and the address-form change.
- **Locator index.** It points the E06-CLM-014/015 and E06-AUD-003 rows here.
- **Crosswalk and syntheses.** The crosswalk and the three lead syntheses take the corrected attributions in the same transaction as the monograph revision.

Frozen predictions, checkpoint counts and the 143 historical transitions are unchanged.
