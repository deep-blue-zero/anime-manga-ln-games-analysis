---
series: BLUE_ARCHIVE
artifact_type: attribution_audit
scope: Fourteen exact supplemental raw-command attribution receipts
version: "1.0"
status: canonical
source_boundary: "Pinned a038020f1f5ac02dcfe76962426d38f86414cdd8 raw and canonical witnesses; twelve already accepted locators plus two unadmitted EVENT818 parser-diagnostic samples; no source refresh or event admission"
do_not_use_as_current_authority: false
created: 2026-10-01
updated: 2026-10-01
---

# Supplemental attribution review — display actor and text-bearing command

## Finding and witness

The inspected scenario parser selects the first numbered command matching its three-or-four-field dialogue expression. It does not require a nonempty fourth text field before choosing the actor. In these exact rows, an earlier actor-only command therefore supplies the canonical label while a later command names a different actor beside the raw spoken string. This is positive evidence for a **derived attribution seam**, not evidence that the upstream author mislabeled the utterance. The Japanese TextJp wording and immutable canonical IDs/hashes are preserved.

The local pipeline has existing uncommitted changes and is not edited by this review. The observed current scenario.py SHA256 is `74a4d6e214ba130e0bd64e52bfdef25bd80e28391d7c644e7290526cc57be4b7`; the canonical generation declares parser0.2.0. The raw-to-derived receipts below independently demonstrate the behavior at the locked generation; the working parser hash is an inspected explanatory witness, not a new source lock. Raw Table1 SHA256 `aaa9e2e5d7e2551af2c7db3109b5132507a0df4596470e03e6945168b73e6303`, Table2 `b699658e131aa4c9abf591f9fd46bf2f2d5b91ce5e20e27f9a2b242a094e68d5`.

## Exact receipts

| Canonical locator | Raw record | Canonical label | Earlier actor-only command | Later text-bearing actor command | Admission boundary |
|---|---|---|---|---|---|
| BA:group:1203:scene:001:u:0035 | ScenarioScriptExcelTable1.json:DataList[109440] | アスナ | `5;아스나;03` | `1;카린;04` (fourth field contains the spoken string) | Already accepted; individual label-qualified |
| BA:group:1501:scene:001:u:0012 | ScenarioScriptExcelTable1.json:DataList[107131] | マキ | `1;마키;05` | `3;코타마;01` (fourth field contains the spoken string) | Already accepted; individual label-qualified |
| BA:group:1503:scene:001:u:0004 | ScenarioScriptExcelTable1.json:DataList[107303] | ハレ | `5;하레;01` | `1;마키;04` (fourth field contains the spoken string) | Already accepted; individual label-qualified |
| BA:group:1503:scene:001:u:0037 | ScenarioScriptExcelTable1.json:DataList[107357] | マキ | `1;마키;01` | `3;코타마;99` (fourth field contains the spoken string) | Already accepted; individual label-qualified |
| BA:group:1503:scene:001:u:0038 | ScenarioScriptExcelTable1.json:DataList[107358] | コタマ | `3;코타마;01` | `5;하레;03` (fourth field contains the spoken string) | Already accepted; individual label-qualified |
| BA:group:2102:scene:002:u:0014 | ScenarioScriptExcelTable1.json:DataList[105130] | セリカ | `4;세리카;05` | `2;시로코;06` (fourth field contains the spoken string) | Already accepted; individual label-qualified |
| BA:group:2102:scene:002:u:0015 | ScenarioScriptExcelTable1.json:DataList[105131] | シロコ | `2;시로코;05` | `4;세리카;06` (fourth field contains the spoken string) | Already accepted; individual label-qualified |
| BA:group:2102:scene:002:u:0053 | ScenarioScriptExcelTable1.json:DataList[105172] | アヤネ | `1;아야네;01` | `3;호시노;03` (fourth field contains the spoken string) | Already accepted; individual label-qualified |
| BA:group:1101:scene:001:u:0035 | ScenarioScriptExcelTable1.json:DataList[103433] | ハルナ | `5;하루나;01` | `1;준코;09` (fourth field contains the spoken string) | Already accepted; individual label-qualified |
| BA:group:1101:scene:001:u:0053 | ScenarioScriptExcelTable1.json:DataList[103452] | ハルナ | `3;하루나;06` | `5;준코;05` (fourth field contains the spoken string) | Already accepted; individual label-qualified |
| BA:group:1101:scene:001:u:0054 | ScenarioScriptExcelTable1.json:DataList[103453] | ハルナ | `3;하루나;06` | `1;아카리;03` (fourth field contains the spoken string) | Already accepted; individual label-qualified |
| BA:group:1102:scene:001:u:0023 | ScenarioScriptExcelTable1.json:DataList[103508] | ハルナ | `5;하루나;07` | `1;준코;10` (fourth field contains the spoken string) | Already accepted; individual label-qualified |
| BA:event:818:001:scene:001:u:0040 | ScenarioScriptExcelTable1.json:DataList[282707] | アヤネ | `3;아야네 학교 체육복;09` | `1;하나코 학교 체육복;01` (fourth field contains the spoken string) | Diagnostic only; EVENT818 remains unadmitted |
| BA:event:818:007:scene:001:u:0001 | ScenarioScriptExcelTable2.json:DataList[79] | ツクヨ | `2;츠쿠요 학교 체육복;01` | `4;이즈나 학교 체육복;00` (fourth field contains the spoken string) | Diagnostic only; EVENT818 remains unadmitted |

## Claim effects and exclusions

GROUP2102's completion promise, charge and return greeting cannot be counted as secure individual Serika/Shiroko/Ayane voices merely because of canonical labels; the raw text-bearing commands favor Shiroko, Serika and Hoshino respectively. GROUP1203 u0035 favors Karin rather than Asuna. GROUP1501 u0012 favors Kotama rather than Maki; GROUP1503 u0004/u0037/u0038 favor Maki/Kotama/Hare. Their scene-level arguments already retain attribution warnings, so ensemble findings survive; the causal attribution of those warnings is now narrowed to derivation. No model readiness or main-history state changes.

Newly accepted GROUP1101 u0035/u0053 favor Junko and u0054 favors Akari; GROUP1102 u0023 favors Junko. Those are raw-command-supported assignments, distinct from uninspected audiovisual performance. Do not infer a speaker from expected personality, silently overwrite canonical labels, or count the same text twice.

EVENT818 u0040 and E007 u0001 favor Hanako and Izuna in the raw text-bearing commands, despite canonical Ayane/Tsukuyo labels. They diagnose the attribution mechanism only. The two excerpts do not admit the event, establish its complete literary content or revise character coverage. Its complete packet awaits separate semantic acceptance.

G09 now requires comparison of canonical label, earlier actor-only command and text-bearing command where they disagree. Raw command evidence can improve a written attribution claim without proving performed voice or every similar-looking record. This audit does not promise a parser fix, rebuild, silent correction, or wholesale reread. Future refresh belongs to governed source reconciliation. Cycle002 and the seven ledgers own the accepted analytical effects.
