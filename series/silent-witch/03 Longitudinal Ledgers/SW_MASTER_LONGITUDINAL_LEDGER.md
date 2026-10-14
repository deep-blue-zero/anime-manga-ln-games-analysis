---
title: "Silent Witch — SW Master Longitudinal Ledger"
artifact_id: SW_MASTER_LONGITUDINAL_LEDGER
artifact_type: master_longitudinal_ledger
series: "Silent Witch: Secrets of the Silent Witch"
series_id: silent-witch
generation: V1
version: "1.11"
last_updated: "2026-10-14"
status: canonical
scope: "Exclusive pre-split cumulative state; Japanese LN V01 to V09 and the companions IV -after- and IX -extra- closed and reconciled into every typed section"
source_boundary: "Japanese LN V01 to V09, IV -after- and IX -extra-, witnesses SW-LNJP-V01 to SW-LNJP-V09, SW-LNJP-AFTER04 and SW-LNJP-EXTRA09, closed; no other source unit in any lane analyzed."
created: "2026-10-12"
canonical_home: "series/silent-witch/03 Longitudinal Ledgers/SW_MASTER_LONGITUDINAL_LEDGER.md"
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
do_not_use_as_literary_evidence: true
---

# Master longitudinal ledger

This is the single pre-split cumulative analytical home specified by [the architecture](../00%20Frameworks%20and%20Methods/SW_SYNTHESIS_ARCHITECTURE.md). The current entrypoint is [the corpus map](../CURRENT_STATE_AND_CORPUS_MAP.md). This file preserves cumulative meaning and revision history; volume readings own underlying diagnostic observations, and Drive owns raw source/locator derivatives.

## Actual initialization state

```yaml
longitudinal_state:
  state: EXTRA09_CLOSED
  committed_high_water_mark: EXTRA09
  analyzed_units: [SW-LNJP-V01, SW-LNJP-V02, SW-LNJP-V03, SW-LNJP-V04, SW-LNJP-AFTER04, SW-LNJP-V05, SW-LNJP-V06, SW-LNJP-V07, SW-LNJP-V08, SW-LNJP-V09, SW-LNJP-EXTRA09]
  frozen_units: [SW-LNJP-V01, SW-LNJP-V02, SW-LNJP-V03, SW-LNJP-V04, SW-LNJP-AFTER04, SW-LNJP-V05, SW-LNJP-V06, SW-LNJP-V07, SW-LNJP-V08, SW-LNJP-V09, SW-LNJP-EXTRA09]
  literary_observations: 1996  # V01 001..132; V02 001..120; V03 001..139; V04 001..128; AFTER04 001..166; V05 001..187; V06 001..219; V07 001..229; V08 001..300; V09 001..188; EXTRA09 reading SW-E-LNJP-EXTRA09-001..188
  local_character_identities: 117
  character_models: 0
  readiness_assessments: 41  # evidence reviews SW-RD-0001..0041; no tier awarded
  claim_records: 78
  revision_records: 472  # SW-CR-0001..0018 at V02; 0019..0044 at V03; 0045..0078 at V04, two of them corrections; 0079..0118 at AFTER04; 0119..0162 at V05; 0163..0212 at V06; 0213..0268 at V07; 0269..0330 at V08; 0331..0398 at V09; 0399..0472 at EXTRA09
  prediction_records: 58  # prospective questions SW-P-0001..0058; thirty-nine retired with reason; zero predictions registered
  split_ledger_paths: []
  sequential_analysis_lock: OPEN
  sequential_analysis_lock_scope: CONTINUOUS_RUN_AUTHORIZED_2026-10-14
```

The initialization state, preserved here as history, was NO_SOURCE_UNIT_ANALYZED at PRE_V01 with every count at zero. Those zero records were truthful absence of analysis, not findings about the novel. The records below were appended at V01 closure on 2026-10-14 from the [V01 deep reading](../02%20Sequential%20Readings/SW_V01_DEEP_READING.md). They contain no simulated dialogue and no material from any later unit. Records marked as V02 records were appended at V02 closure on 2026-10-14 from the [V02 deep reading](../02%20Sequential%20Readings/SW_V02_DEEP_READING.md) under the same rule, and records marked as V03 records at V03 closure on 2026-10-14 from the [V03 deep reading](../02%20Sequential%20Readings/SW_V03_DEEP_READING.md), and records marked as V04 records at V04 closure on 2026-10-14 from the [V04 deep reading](../02%20Sequential%20Readings/SW_V04_DEEP_READING.md), and records marked as AFTER04 records at the closure of the companion IV -after- on 2026-10-14 from the [IV -after- deep reading](../02%20Sequential%20Readings/SW_AFTER04_DEEP_READING.md), records marked as V05 records at V05 closure on 2026-10-14 from the [V05 deep reading](../02%20Sequential%20Readings/SW_V05_DEEP_READING.md), records marked as V06 records at V06 closure on 2026-10-14 from the [V06 deep reading](../02%20Sequential%20Readings/SW_V06_DEEP_READING.md), records marked as V07 records at V07 closure on 2026-10-14 from the [V07 deep reading](../02%20Sequential%20Readings/SW_V07_DEEP_READING.md), records marked as V08 records at V08 closure on 2026-10-14 from the [V08 deep reading](../02%20Sequential%20Readings/SW_V08_DEEP_READING.md), records marked as V09 records at V09 closure on 2026-10-14 from the [V09 deep reading](../02%20Sequential%20Readings/SW_V09_DEEP_READING.md), and records marked as EXTRA09 records at the closure of the companion IX -extra- on 2026-10-14 from the [IX -extra- deep reading](../02%20Sequential%20Readings/SW_EXTRA09_DEEP_READING.md).

## Common record contract

Every source-bearing record carries: stable typed ID; continuity/witness/source unit; applicable diegetic interval and disclosure boundary; evidence class; canonical observation reference; exact evidence route; formulation; support; material counterevidence/rival explanation; uncertainty; created/updated boundary; and supersession/revision references where relevant.

Stable IDs are never renumbered. Source observation grammar is `SW-E-LNJP-V<NN>-<sequence>` for numbered LN units; the volume reading owns those IDs. Supplement/web IDs are separate. A published Japanese companion uses `SW-E-LNJP-<unit>-<sequence>`, for IV -after- `SW-E-LNJP-AFTER04-<sequence>`, owned by its reading. Local entity keys resolve only inspected identity evidence and are not global character enrollments.

The common fields apply to all sections. The following field lists define each section's additional exclusive responsibility; they are schemas, not populated rows.

**V01 record defaults.** Unless a row says otherwise, every V01 record has: continuity Japanese LN main track; witness and source unit `SW-LNJP-V01`; diegetic interval from three months after the Worgan dragon to one week after Thornley’s arrest; disclosure boundary V01; created and last updated at V01 closure, 2026-10-14; no supersession. The canonical observation reference is the `obs.` number in the [V01 reading](../02%20Sequential%20Readings/SW_V01_DEEP_READING.md#614-observation-register), meaning `SW-E-LNJP-V01-<nnn>`. The evidence route is that observation, then its locator, then the locally retained sealed locator package. Evidence classes use the method’s grammar abbreviated as OTE, CRB, NP, SI, WH, SP, NE, CON and UQ. Romanized names are analyst conveniences.

**V02 record defaults.** Every V02 record has: continuity Japanese LN main track; witness and source unit `SW-LNJP-V02`; diegetic interval from about two weeks after Monica’s enrolment to about six weeks after it, the evening of the delivery day; disclosure boundary V02; created and last updated at V02 closure, 2026-10-14; no supersession unless stated. Its `obs.` numbers refer to the [V02 reading](../02%20Sequential%20Readings/SW_V02_DEEP_READING.md#618-observation-register), meaning `SW-E-LNJP-V02-<nnn>`, and its bare locators to `SW-LNJP-V02`. A V01 observation cited in a V02 record is written `V01 obs. nnn`.

**V03 record defaults.** Every V03 record has: continuity Japanese LN main track; witness and source unit `SW-LNJP-V03`; diegetic interval from about a week after Casey’s removal, some six weeks into the mission, to the morning after the Coalrapton bell-ringing festival, with a prologue set at Minerva some years earlier and a secret episode shortly after the festival; disclosure boundary V03; created and last updated at V03 closure, 2026-10-14; no supersession unless stated. Its `obs.` numbers refer to the [V03 reading](../02%20Sequential%20Readings/SW_V03_DEEP_READING.md#619-observation-register), meaning `SW-E-LNJP-V03-<nnn>`, and its bare locators to `SW-LNJP-V03`. Earlier observations are written `V01 obs. nnn` or `V02 obs. nnn`.

**V04 record defaults.** Every V04 record has: continuity Japanese LN main track; witness and source unit `SW-LNJP-V04`; diegetic interval from four days before the school festival to the night of the ball, with a prologue from Monica’s tenth year and a secret episode on the ball night and the following day; disclosure boundary V04; created and last updated at V04 closure, 2026-10-14; no supersession unless stated. Its `obs.` numbers refer to the [V04 reading](../02%20Sequential%20Readings/SW_V04_DEEP_READING.md#613-observation-register), meaning `SW-E-LNJP-V04-<nnn>`, and its bare locators to `SW-LNJP-V04`. Earlier observations are written with their volume prefix.

**AFTER04 record defaults.** Every AFTER04 record has: continuity Japanese LN supplemental companion, admitted after V04 under the placement audit; witness and source unit `SW-LNJP-AFTER04`; diegetic interval from two days after the school festival to a winter holiday about four weeks later, before the winter break, with retrospective scenes about a year before the mission (prologue and first interlude), in Byron’s fourteenth, Glen’s fifteenth and Elliott’s seventh years, and two months after the black dragon; disclosure boundary AFTER04; created and last updated at the companion’s closure, 2026-10-14; no supersession unless stated. Its `obs.` numbers refer to the [IV -after- reading](../02%20Sequential%20Readings/SW_AFTER04_DEEP_READING.md#613-observation-register), meaning `SW-E-LNJP-AFTER04-<nnn>`, and its bare locators to `SW-LNJP-AFTER04`. A record resting on a retrospective scene says so; earlier observations are written with their volume prefix.

**V05 record defaults.** Every V05 record has: continuity Japanese LN main track; witness and source unit `SW-LNJP-V05`; diegetic interval from a week before the winter break to New Year’s Day, with a prologue more than half a year before the mission and a retrospective of Nero’s taming about half a year before it; disclosure boundary V05; created and last updated at V05 closure, 2026-10-14; no supersession unless stated. Its `obs.` numbers refer to the [V05 reading](../02%20Sequential%20Readings/SW_V05_DEEP_READING.md#612-observation-register), meaning `SW-E-LNJP-V05-<nnn>`, and its bare locators to `SW-LNJP-V05`. Earlier observations are written with their unit prefix.

**V06 record defaults.** Every V06 record has: continuity Japanese LN main track; witness and source unit `SW-LNJP-V06`; diegetic interval from before the solstice to the morning after the duel, about two and a half weeks into the new term; disclosure boundary V06; created and last updated at V06 closure, 2026-10-14; no supersession unless stated. Its `obs.` numbers refer to the [V06 reading](../02%20Sequential%20Readings/SW_V06_DEEP_READING.md#612-observation-register), meaning `SW-E-LNJP-V06-<nnn>`, and its bare locators to `SW-LNJP-V06`. Earlier observations are written with their unit prefix.

**V07 record defaults.** Every V07 record has: continuity Japanese LN main track; witness and source unit `SW-LNJP-V07`; diegetic interval from the forest day after the duel to early spring after Sheffield’s holiday, about six weeks, with retrospective scenes of Bartholomeus’s youth, Bridget’s childhood and the gardener’s memory of about ten years ago; disclosure boundary V07; created and last updated at V07 closure, 2026-10-14; no supersession unless stated. Its `obs.` numbers refer to the [V07 reading](../02%20Sequential%20Readings/SW_V07_DEEP_READING.md#612-observation-register), meaning `SW-E-LNJP-V07-<nnn>`, and its bare locators to `SW-LNJP-V07`. Earlier observations are written with their unit prefix.

**V08 record defaults.** Every V08 record has: continuity Japanese LN main track; witness and source unit `SW-LNJP-V08`; diegetic interval from the student assembly in the fifth week of Widdle to about two weeks before the Supreme Council, with retrospective chapters on Isaac Walker’s childhood and the substitution about ten years ago, and a prologue on the night after Venedict Rain’s arrest; disclosure boundary V08; created and last updated at V08 closure, 2026-10-14; no supersession unless stated. Its `obs.` numbers refer to the [V08 reading](../02%20Sequential%20Readings/SW_V08_DEEP_READING.md#612-observation-register), meaning `SW-E-LNJP-V08-<nnn>`, and its bare locators to `SW-LNJP-V08`. Earlier observations are written with their unit prefix.

**V09 record defaults.** Every V09 record has: continuity Japanese LN main track; witness and source unit `SW-LNJP-V09`; diegetic interval from the reveal to the council, about two weeks, then graduation and a coda to the summer about a year after graduation; disclosure boundary V09; created and last updated at V09 closure, 2026-10-14; no supersession unless stated. Its `obs.` numbers refer to the [V09 reading](../02%20Sequential%20Readings/SW_V09_DEEP_READING.md#612-observation-register), meaning `SW-E-LNJP-V09-<nnn>`, and its bare locators to `SW-LNJP-V09`. Earlier observations are written with their unit prefix.

**EXTRA09 record defaults.** Every EXTRA09 record has: continuity Japanese LN supplemental companion; witness and source unit `SW-LNJP-EXTRA09`; diegetic interval story by story, from about a year after Monica’s appointment to the summer after her move to Southerndoor, each placed by its own markers and none after V09’s last scene; disclosure boundary EXTRA09; created and last updated at the companion’s closure, 2026-10-14; no supersession unless stated. Its `obs.` numbers refer to the [IX -extra- reading](../02%20Sequential%20Readings/SW_EXTRA09_DEEP_READING.md#610-observation-register), meaning `SW-E-LNJP-EXTRA09-<nnn>`, and its bare locators to `SW-LNJP-EXTRA09`. Earlier observations are written with their unit prefix.

**Local identities at V01.** These keys resolve inspected identity only and are not global enrollments.

| Local key | Japanese name and aliases in V01 | Identity notes |
|---|---|---|
| sw.monica | モニカ・エヴァレット; 〈沈黙の魔女〉; cover name モニカ・ノートン; 同期殿, 子リス, ノートン会計 | One person under two names; the cover is known to her confidants only. |
| sw.felix | フェリクス・アーク・リディル; 第二王子; 生徒会長; マスター to Wildianu | Prologue watcher identification was inference only at V01; established from his own viewpoint at V02, SW-C-0006. |
| sw.louis | ルイス・ミラー; 〈結界の魔術師〉 | — |
| sw.cyril | シリル・アシュリー; 生徒会副会長; adopted son of the ハイオーン marquisate | — |
| sw.nero | ネロ; human-form alias バーソロミュー・アレクサンダー | Nature undisclosed. |
| sw.lynn | リィンズベルフィード; リン | Wind upper spirit. |
| sw.wildianu | ウィルディアヌ; ウィル | Water upper spirit contracted to Felix. |
| sw.isabelle | イザベル・ノートン; ケルベック伯爵令嬢 | — |
| sw.lana | ラナ・コレット | — |
| sw.elliott | エリオット・ハワード | — |
| sw.bridget | ブリジット・グレイアム | — |
| sw.neil | ニール・クレイ・メイウッド | — |
| sw.thornley | ヴィクター・ソーンリー | Removed from the school at V01. |
| sw.selma | セルマ・カーシュ | Removed at V01. |
| sw.aaron | アーロン・オブライエン | Removed at V01. |
| sw.rosalie | ロザリー・ミラー | — |

**Local identities added at V02.**

| Local key | Japanese name and aliases in V02 | Identity notes |
|---|---|---|
| sw.glen | グレン・ダドリー; 肉屋の倅 | Transfer student; apprentice mage. Identification as Louis’s disciple is inference only, SW-P-0001. |
| sw.casey | ケイシー・グローヴ; ブライト伯爵令嬢 | Also the prologue’s unnamed conspirator, identified by object, SW-C-0019. Removed from the school. |
| sw.claudia | クローディア・アシュリー; 〈歩く図書館〉 | Cyril’s adoptive sister; Neil’s fiancée. |
| sw.caroline | カロライン・シモンズ; ノルン伯爵令嬢 | The V01 staircase girl, first named in V02. To be expelled. |
| sw.maclaggan | ウィリアム・マクレガン; 〈水咬の魔術師〉 | Monica’s and Louis’s former Minerva teacher. |
| sw.lindsay | リンジー・ペイル | Dance teacher; Monica’s homeroom teacher after Thornley. |
| sw.boyd | カール・ボイド | Chess teacher. |
| sw.mary | メアリー・ハーヴェイ; 〈星詠みの魔女〉 | A Sage. |
| sw.mabel | メイベル・ヘインズ | Stage-effects lead. |
| sw.agatha | アガサ | Isabelle’s maid; also present in V01’s prologue. |
| sw.eliane | エリアーヌ; エリアーヌ・ハイアット | Felix’s second cousin; house given variously, V02 reading section 8.8. Not on stage. |
| sw.lionel | ライオネル | First prince. Not on stage. |
| sw.count-bright | ブライト伯爵 | Casey’s father. Not on stage except in memory. |
| sw.monica-father | モニカの父; named ヴェネディクト・レイン at V03 | Unnamed until V03, where his book names him, SW-C-0032. Known otherwise from memory and delirium. |
| sw.monica-uncle | 叔父 | Unnamed; the man in the V01 dream, SW-C-0003. |

**Local identities added at V03.**

| Local key | Japanese name and aliases in V03 | Identity notes |
|---|---|---|
| sw.bernie | バーニー・ジョーンズ; アンバード伯爵家の次男 | Minerva student and chess captain; the Minerva friend of V01–V02, SW-C-0027. |
| sw.rutherford | ギディオン・ラザフォード | Minerva professor; Monica’s laboratory head. In memory only. |
| sw.robert | ロベルト・ヴィンケル | Randall exchange student at the temple-affiliated academy. |
| sw.benjamin | ベンジャミン・モールディング | Serendia third-year; chess team. |
| sw.redding | レディング | Teacher of the temple-affiliated academy. |
| sw.pittman | ユージン・ピットマン | Minerva teacher; dead; his body was used to stage the impostor’s suicide, SW-C-0031. |
| sw.yuan | ユアン | Imperial agent; impersonated Pittman by body magic. Assigned names only as given in the text. |
| sw.heidi | ハイディ | Yuan’s pupil and partner. |
| sw.duke-clockford | ダライアス・ナイトレイ; クロックフォード公爵 | Felix’s maternal grandfather; first on stage at V03. |
| sw.bartholomeus | バルトロメウス; バルトロメウス・バール | Imperial craftsman; forger of the V02 crest. |
| sw.porter | ポーター; pen name ダスティン・ギュンター | Bookseller and novelist; friend of Monica’s father. |
| sw.doris | ドリス | Prostitute at Madam Cassandra’s house. |
| sw.cassandra | マダム・カサンドラ | Proprietor of the house. |
| sw.irene | アイリーン | Named in Felix’s dream as the mother of the boy addressed as Felix. Not on stage. |
| sw.felix-page | 従者の少年 | Felix’s attendant in Elliott’s memory and the page in Felix’s dream; whether these are one person is not stated. Unnamed. |
| sw.felix-friend | 友人 | The friend whose wish Felix pursues; presumed dead by Monica. Unnamed; no identity with any other key is asserted, SW-C-0022. |

**Local identities added at V04.**

| Local key | Japanese name and aliases in V04 | Identity notes |
|---|---|---|
| sw.hilda | ヒルダ・エヴァレット | Venedict Rain’s former assistant; Royal Magic Research Institute; Monica’s adoptive mother. |
| sw.matilda | マティルダ | Hilda’s housemaid. |
| sw.conrad | コンラッド・アスカム | Head of the magic-history club. |
| sw.ray | レイ・オルブライト; 〈深淵の呪術師〉 | Third of the name; head of the Albright house; a Sage. |
| sw.sylvia | シルヴィア・ノートン | Isabelle’s mother; wife of Count Kerbeck. |
| sw.henry | ヘンリー・ノートン | Isabelle’s younger brother. |
| sw.count-kerbeck | アズール・ノートン; ケルベック伯爵 | Named at V04; not on stage. |
| sw.myra | マイラ・ウェイン | Cyril’s mother. |
| sw.highorn | ハイオーン侯爵 | Claudia’s father; Cyril’s adoptive father. |
| sw.baron-collette | コレット男爵 | Lana’s father. |
| sw.baron-maywood | メイウッド男爵 | Neil’s father; a mediator. In Claudia’s memory. |
| sw.duke-leinbourg | レーンブルグ公爵 | Eliane’s father. |
| sw.albright-traitor | 裏切りの呪術師 | Unnamed; fled the Albrights ten years ago; serves a patron called 閣下; knew Venedict Rain. No identity with any other key is asserted, SW-C-0039. |
| sw.arthur | アルトゥール | Named by Yuan as a traitor whose work left a trace on Felix. Not on stage; identity withheld. |

**Local identities added at AFTER04.**

| Local key | Japanese name and aliases in AFTER04 | Identity notes |
|---|---|---|
| sw.byron | バイロン・ギャレット | Third-year; head of the magic-battle club; Sheila’s fiancé. |
| sw.sheila | シーラ・アシュバートン | Third-year; vice-head of the embroidery club; Byron’s fiancée. |
| sw.cecily | セシリー・スタンレイ | Head of the embroidery club; Wanda’s cousin. |
| sw.wanda | ワンダ・ウィルモット | Third-year; tore the grimoire page. |
| sw.lucile | ルシール | MacLaggan’s granddaughter, three or four years old. |
| sw.istreia | 地霊イストレイア | Mid-level earth spirit in rabbit form, contracted in Lucile’s family. |
| sw.count-dazvie | ダーズヴィー伯爵 | Elliott’s father; in the retrospective interlude and Elliott’s memory. |

**Local identities added at V05.**

| Local key | Japanese name and aliases in V05 | Identity notes |
|---|---|---|
| sw.bradford | ブラッドフォード・ファイアストン; 〈砲弾の魔術師〉 | A Sage; multi-reinforcement specialist. |
| sw.emmanuel | エマニュエル・ダーウィン; 〈宝玉の魔術師〉 | A Sage; enchanter and tool-maker; second-prince faction. |
| sw.raul | ラウル・ローズバーグ; 五代目〈茨の魔女〉 | A Sage; named, not on stage. |
| sw.dolly | ドリー | Bridget’s maid. |
| sw.reston | レストン | Leinbourg butler. |
| sw.barrow, sw.malet | バロー伯爵; マレ伯爵 | Falfolia envoys. |
| sw.albert | アルバート | Third prince, fourteen. |
| sw.patrick | パトリック | Albert’s attendant. |
| sw.seraphina | セラフィーナ | Bridget’s younger sister. |
| sw.hubert-dee | ヒューバード・ディー | Former Minerva student who pursued the Silent Witch; transferring to Serendia. |

**Identity disclosed at V05.** The key sw.albright-traitor is identified in the text as Barry Oates, who served at Leinbourg as the footman Peter Sams (ピーター・サムズ) and died by his own curse (V05 obs. 142, 147, 148). The patron 閣下 remains unidentified, SW-C-0039.

**Local identities added at V06.**

| Local key | Japanese name and aliases in V06 | Identity notes |
|---|---|---|
| sw.sandy | サンディ | Carrot farmer’s daughter, twelve; Monica Norton’s winter stand-in in Kerbeck. |
| sw.kerbeck-detective | 探偵 | Hired by an unnamed young lady to check Monica Norton; unnamed. |
| sw.ambrose | アンブローズ・クレイドル・リディル | The king; ill. |
| sw.wilma | ヴィルマ妃 | First queen; Lionel’s mother; a Randall princess. |
| sw.phyllis | フィリス妃 | Albert’s mother; allied with Clockford. |
| sw.carla | カーラ・マクスウェル; 〈星槍の魔女〉 | Former Sage; Louis’s senior; Magic Geography Society. |
| sw.ice-spirit | 氷霊 | An upper spirit in boy form that has forgotten its name. |
| sw.sezdio | セズディオ | Middle-rank earth spirit in wolf form. |
| sw.relva | レルヴァ | Fire upper spirit under the whistle. |
| sw.bestion | ベスティオン | Earth upper spirit under the whistle; named only. |
| sw.galanis | 〈偽王の笛ガラニス〉 | A speaking ancient tool, thought lost; held by Emmanuel. |
| sw.emmanuel-patron | あの方 | Emmanuel’s patron, who wants war; unnamed; no identity with any other key is asserted, SW-C-0053. |

**Identity notes extended at V06.** sw.raul, sw.lionel, sw.emmanuel and sw.hubert-dee are now on stage; sw.irene is named in narration as Felix’s mother, the queen who died soon after his birth (V06 obs. 043); sw.duke-clockford is named in narration as Darius Knightley (V06 obs. 024). The red-haired figure of V06 chapters three and four is linked to sw.hubert-dee by narration at V06 obs. 125. The unnamed old man of V06 chapter eight is placed as Emmanuel by the narration of the secret episode (V06 reading section 8.1). The friend in Felix’s memory who called him Ike is recorded under sw.felix-friend’s scope note only as a further unnamed appearance; no identity with sw.felix-friend or sw.felix-page is asserted, SW-C-0022.

**Local identities added at V07.**

| Local key | Japanese name and aliases in V07 | Identity notes |
|---|---|---|
| sw.isaac-walker | アイザック・ウォーカー; 殿下の従者 | The page in Bridget’s memory and the gardener’s account; blond, scarred over the right eye, from the east; died in a fire at Duke Clockford’s house about ten years ago, by the gardener’s account. No identity with sw.felix-page, sw.felix-friend or any other key is asserted, SW-C-0058. |
| sw.dr-arthur | アーサー先生 | Physician at Duke Clockford’s house before Sams; died in the same fire, by the gardener’s account. No identity with sw.arthur is asserted, SW-C-0058. |
| sw.marcy | マーシー | Former head maid at Clockford’s house; entered a convent after the fire. |
| sw.clockford-gardener | 庭師の老人 | Gardener at Clockford’s house for forty years. |
| sw.clockford-butler | 執事 | Butler at Clockford’s house. |
| sw.yuan-master | 我が君; 余 | Yuan’s master, a dark-haired man in his late twenties; unnamed. |
| sw.dahmisch | ダーミッシュ | Head of the Imperial workshop where Bartholomeus and his sister trained. |
| sw.bart-sister | 妹 | Bartholomeus’s younger sister; arrested for forgery and, by hearsay, executed. |
| sw.raul-sister | 姉; 四代目〈茨の魔女〉 by context | Raul’s elder sister, a former Thorn Witch; named only as his sister. |

**Identities disclosed at V07.** The key sw.ice-spirit is named in narration as Romaria (ロマリア), one of the three winter spirits of the legend (V07 obs. 068). The key sw.emmanuel-patron is identified with sw.duke-clockford by Emmanuel’s own usage of あの方 in V06 and V07 (V07 obs. 058; SW-C-0057). Neither identification is extended to 閣下 or the great noble, SW-C-0039.

**Local identities added at V08.**

| Local key | Japanese name and aliases in V08 | Identity notes |
|---|---|---|
| sw.arc | フェリクス・アーク・リディル (the original prince); アーク | The real second prince, Queen Irene’s son; frail, earth affinity; died by a fall from the roof about ten years ago. Distinct from sw.felix, the person who has borne the name since, SW-C-0063. |
| sw.colin | コリン | Isaac Walker’s baby brother; died in the dragon attack on Lugaroa. |
| sw.walker-parents | 父; 母 | Isaac Walker’s parents, a doctor and his wife in Lugaroa; killed in the dragon attack. |
| sw.labiana | ラビアナ司教 | A wealthy bishop; killed at Clockford’s order. |
| sw.rendula | レンデュラ | Wind spirit in bird form serving the emperor. |
| sw.esperne | エスペルネ | Wind spirit in bird form serving the emperor. |
| sw.lorna | シスター・ローナ | Head of the northern convent where Casey and Marcy lived. |
| sw.leonora | レオノーラ | Louis and Rosalie’s newborn daughter. |
| sw.clockford-father | 先代クロックフォード公爵 | Darius Knightley’s father; proposed peace in the war about fifty years ago and was killed by Ridill’s war party. |

**Identities disclosed at V08.** The narration discloses, from the person’s own memory, that sw.felix, the person on stage under the name Felix Arc Ridill since V01, is sw.isaac-walker, the page remade by body manipulation (V08 obs. 097, 147–150, 176; SW-C-0063). sw.felix-page is sw.isaac-walker (V08 obs. 219). sw.felix-friend is sw.arc (V08 obs. 115, 220). sw.irene is the mother of sw.arc. sw.arthur, Yuan’s Artur, is sw.dr-arthur, killed by Clockford (V08 obs. 037, 121, 156). sw.yuan-master is the emperor Leonhardt Alois Maximilian Bernd Kreving (レオンハルト), called the Black Lion Emperor (V08 obs. 054). sw.wildianu was sw.irene’s contract spirit, given by sw.arc to sw.isaac-walker, who contracted it (V08 obs. 141, 160–165). sw.marcy left after the prince’s death, hid in the northern convent and died of pneumonia the year before (V08 obs. 238, 239). The patron 閣下 remains unidentified, SW-C-0039.

**Local identities added at V09.**

| Local key | Japanese name and aliases in V09 | Identity notes |
|---|---|---|
| sw.annie | アニー | Village girl who brought Monica food at the hut. |
| sw.barrel | バーレル伯爵 | A count at the Supreme Council whose blood was used in the chalice demonstration. |
| sw.barrel-son | 書記官 | Count Barrel’s son, a clerk. |
| sw.ana | アナ | Glen’s younger sister. |
| sw.betty | ベティ | Glen’s younger sister. |
| sw.clockford-wife | 妻 | Clockford’s wife, of an impoverished noble house; killed by an assassin sent by Ridill nobles, by Mary’s account. |

**Identity notes extended at V09.** sw.felix (Isaac Walker) is recognized by the king by his own name and is Duke of Erin under the prince’s name (V09 obs. 106, 164). The patron 閣下 is not named in V09; the narration states Clockford was behind Sams’s Leinbourg dragon (S18:E000522), SW-C-0039.

**Local identities added at EXTRA09.**

| Local key | Japanese name and aliases in EXTRA09 | Identity notes |
|---|---|---|
| sw.hilda-ally | 男 (unnamed) | A tired middle-aged authority of the physicians’ association, trusted by the Mage Guild; helped Hilda escape with the chalice design. Not named. |
| sw.samus-horaceson | 〈水鏡の魔術師〉サムス・ホレイソン | A dead upper mage whose mirror was donated to Serendia; his water spirit slept in a hidden contract stone. |
| sw.loom-spirit | 風の精霊 (in a puppy) | A weak wind spirit possessing a puppy; sent to Minerva. |

**Identity notes extended at EXTRA09.** The fiancé of Mary’s first prophecy is sw.duke-clockford by the joined record (EXTRA09 obs. 151, 152; V08 obs. 294). The design materials give sw.duke-clockford a personal name, ダライアス・ナイトレイ, as paratext only; 閣下 is not used and remains unidentified by name, SW-C-0039. The prequel figures on the design pages are not entered as identities.

The AFTER04 retrospective interlude also shows a 従者の少年 serving the child Felix at Duke Clockford’s house. It is recorded under sw.felix-page’s scope note only as a further appearance of an unnamed attendant; whether it is the same person is not stated, SW-C-0022.

## 1. Character state and speech — SW-S

Owns source-bearing character changes, role constraints, ordinary behavior, self-conception and written-speech conditioning.

Fields: local key; name/title/address alias and scope; state before; represented perception/appraisal/affect; options; action/speech; consequence; state after; change kind; persistent feature; persona/private distinction; audience/recipient; register/address/silence feature; diagnostic ordinary-life basis.

Change kinds: DISPOSITION_CHANGE, KNOWLEDGE_CHANGE, ROLE_CONTEXT_CHANGE, RELATIONSHIP_CHANGE, REVEALED_NOT_NEW, UNRESOLVED. A knowledge-change summary links to SW-K for proposition ownership. A relational effect links to SW-R.

Records at V01:

| ID | Key | State before → after | Kind | Process: perception → appraisal/affect → options → act/speech → consequence | Persona/private; recipient; register | Obs. | Class | Rival; uncertainty |
|---|---|---|---|---|---|---|---|---|
| SW-S-0001 | sw.monica | Baseline at entry: recluse by preference; underfed; numbers as work and comfort; believes herself a makeweight Sage. | REVEALED_NOT_NEW | Legend heard → stomach pain, sweat → hide → stammered evasions → secret kept by others’ assumptions. | Public legend vs private recluse; polite stammer to humans, plain to Nero. | 004, 005, 006, 013, 016 | NP, CRB | R: preference for solitude rather than fear. U: none material. |
| SW-S-0002 | sw.monica | Chantless casting understood as avoidance turned mastery; can only cast silently, so any magic exposes her. | REVEALED_NOT_NEW | Exam fear → cannot chant → remove the chant → mastery → title. | Constraint operates at school in every scene. | 007, 008, 033 | NP | R: talent independent of cause. U: deeper origin, see SW-S-0004. |
| SW-S-0003 | sw.monica | Pain, fear or exposure produce absorption in numbers. | REVEALED_NOT_NEW | Threat or pain → fear → numerical refuge → reduced awareness → comic or productive outcome. | Song series, lashes, ledgers; narrated in hiragana once. | 014, 037, 071, 072, 085 | NP | R: habit of mind only. U: none; narrator states it. Links SW-C-0002. |
| SW-S-0004 | sw.monica | Associative evidence of past harm: dream of a drinking man, a bottle and a silence rule; head-covering flinch; fear of an adult male form; rank makes truth; refusal to let others be falsely accused. | REVEALED_NOT_NEW; UNRESOLVED | Raised hand → expects a blow → covers head; injustice to another → forces speech. | Not narrated as memory, only as dream and reflex. | 037, 040, 057, 058, 059 | SI, UQ | R: dream distortion and startle. U: who, when, how often. Links SW-C-0003. |
| SW-S-0005 | sw.monica | From reflexive nod and failed greeting to thanks, requests, chosen tasks, a completed false-name introduction, an accusation, plain speech to a friend. | DISPOSITION_CHANGE, provisional | Repeated: fear → recalled duty or care → speech act forced out → recognized or rebuffed. | Fluent with non-humans, in proof, in anger at formulas, in writing; breaks on self-reference. | 041, 045, 053, 059, 087, 104, 112, 114, 115 | OTE | R: role pressure, not disposition. U: generalization to strangers untested; SW-P-0012. |
| SW-S-0006 | sw.monica | Hermit Sage → student Monica Norton under Kerbeck cover → council treasurer with public badge. | ROLE_CONTEXT_CHANGE | Coerced acceptance → cover lived → competence displayed → appointment she cannot refuse. | Cover known to confidants; badge as public marking. | 011, 012, 074, 075, 084, 114 | OTE | R: none. U: none. |
| SW-S-0007 | sw.monica | Learns that an authority can investigate instead of deferring to rank. | KNOWLEDGE_CHANGE | Expected rank to decide → Cyril’s inquiry → surprise. | — | 058, 091 | OTE, NP | R: Cyril is an exception. U: whether expectation generalizes. Links SW-K-0014. |
| SW-S-0008 | sw.monica | Self-worth unchanged: cannot be proud; talent is a curse that took father and friend; claims no attachment to people while acting on attachments. | UNRESOLVED | Praise or challenge → refusal of pride; others’ need → anonymous care. | Report reduces achievements to “various things happened”. | 026, 066, 089, 090, 093, 101, 115 | CRB, NP | R: accurate self-report about romance only. U: father’s case. Links SW-C-0014. |
| SW-S-0009 | sw.felix | Public persona of perfect courtesy and command; private 僕, game vocabulary, life as remainder; wish withheld. | REVEALED_NOT_NEW | — | 私 public, 僕 private; さて as dominance. | 020, 023, 062, 078 | OTE, NP | R: affectation. U: reason for the remainder. |
| SW-S-0010 | sw.felix | Strategic actor: year-long trap for Aaron; key test; lies to council and to Elliott; destroyed Louis’s brooch; hides magic literacy and spirit. | REVEALED_NOT_NEW | Threat or puzzle → test or trap → concealment. | Kindness and calculation coincide in act. | 069, 074, 077, 079, 121 | OTE | R: prudent ruler-in-training. U: aims. |
| SW-S-0011 | sw.felix | Model of Monica: not a civilian; purpose unknown; too incompetent to be the king’s; amusing because indifferent to him. | KNOWLEDGE_CHANGE | Observes oddities → tests → appoints to keep near. | Pet lexicon toward her. | 063, 069, 078 | OTE | R: interest beyond the game. U: open. Links SW-K-0004. |
| SW-S-0012 | sw.felix | Rapt devotion to the Silent Witch in the abstract. | REVEALED_NOT_NEW | — | Warms and flushes describing her. | 003, 024, 122 | OTE, SI | R: idealization only. U: watcher identity, SW-C-0006. |
| SW-S-0013 | sw.cyril | Loyal to Felix to the point of violence; scrupulous procedure; needs recognition; adopted, with an unsaid sentence to his mother. | REVEALED_NOT_NEW | Disrespect to Felix → rage; injury → care first; incident → inquiry. | 私; stiff archaic register; hyperbolic oaths. | 057, 080, 091, 095, 096 | NP, OTE | R: none. U: object of elided wish. |
| SW-S-0014 | sw.cyril | Memory altered after noticing the slant; constitution crisis from brooch malfunction; treated without knowing it; remembers a monster. | KNOWLEDGE_CHANGE (unaware) | Notices evidence → erased → crisis → exhausted by an unknown mage. | — | 081, 098, 099, 103 | OTE, NP | R: none. U: whether memory returns. |
| SW-S-0015 | sw.cyril | Toward Monica: hostility for disrespect → professional recognition; private unverified suspicion from her hand. | RELATIONSHIP_CHANGE | Work observed → judgment revised → introduces her by office. | Office title ノートン会計. | 080, 111, 114 | OTE, SI | R: curiosity only about the hand. U: what he concludes. Links SW-R-0011. |
| SW-S-0016 | sw.louis | Coercive politeness; mock-scriptural motto; ear-pinching; doting husband. | REVEALED_NOT_NEW | Need → coerce with charm and threat. | 私; 同期殿; imperatives under pressure. | 009, 010, 011, 094 | OTE | R: none. U: none. |
| SW-S-0017 | sw.louis | Beaten by Monica at selection; regards her as a monster in power; wants her confident; reads the order as surveillance; planted a disciple. | REVEALED_NOT_NEW | — | Private candour with Lynn. | 116, 117, 118, 119 | CRB | R: self-serving memory. U: examiners’ view. Links SW-C-0017. |
| SW-S-0018 | sw.nero | Talking familiar; reads novels; senses magic; shapeshifts; strong; dislikes cold; knows her fear responses; hides the kiss from her; vows to protect her. | REVEALED_NOT_NEW | — | オレ様; garbles human names. | 041, 072, 076, 102 | OTE, CRB | R: none. U: nature, SW-C-0013. |
| SW-S-0019 | sw.isabelle | Brave heir in the prologue; theatrical villainess; devoted collaborator; effective tactician. | REVEALED_NOT_NEW | — | わたくし; お姉様; persona switching. | 018, 019, 025, 128 | OTE | R: none. U: none. |
| SW-S-0020 | sw.lana | Brusque new-money baron’s daughter, herself mocked; becomes Monica’s first friend. | RELATIONSHIP_CHANGE | Scorn → grooming → shared wound → apology → pride. | わたし; 貴女 → モニカ. | 031, 046, 047, 083, 112 | OTE | R: uses Monica as audience. U: low. |
| SW-S-0021 | sw.thornley | Contemptuous elite teacher; wounded by Monica’s published work; organized embezzlement; used restricted magic; removed. | ROLE_CONTEXT_CHANGE | Exposure threat → erase witnesses → confronted → sealed in dream. | たまえ/かね register. | 029, 051, 104, 105, 107, 108, 109 | OTE, CRB | R: none. U: none material. |
| SW-S-0022 | sw.elliott | Vigilant guard of Felix; trap-setter; contempt for presumptuous commoners; unaccepting of Monica. | REVEALED_NOT_NEW | — | 俺; flippant over contempt. | 036, 061 | OTE | R: none. U: none. |
| SW-S-0023 | sw.bridget | Cold, exacting, strikes Monica with a fan; unaccepting. | REVEALED_NOT_NEW | — | あたくし; お前. | 070 | OTE | R: none. U: thin. |
| SW-S-0024 | sw.selma | Devotion without return; over-confession; manipulated on Monica’s inference; removed. | ROLE_CONTEXT_CHANGE | — | 私. | 064, 065 | OTE, CRB | R: own initiative. U: instigator identity rests on inference. |

Records at V02:

| ID | Key | State before → after | Kind | Process: perception → appraisal/affect → options → act/speech → consequence | Persona/private; recipient; register | Obs. | Class | Rival; uncertainty |
|---|---|---|---|---|---|---|---|---|
| SW-S-0025 | sw.monica | Father’s fate unknown → learned researcher of the body as number, reviled, stoned and burned as a heretic with his papers. | REVEALED_NOT_NEW | Felix’s demand for expectations → old wound → memory; poisoning → delirium of the execution. | Private memory; never spoken to anyone. | 034, 044 | CRB | R: drugged distortion; V02 section 8.1. U: research, place, date. |
| SW-S-0026 | sw.monica | Man in the V01 dream unidentified → her paternal uncle, who beat her for reciting numbers and forbade speaking of her father in public. | REVEALED_NOT_NEW | Numbers recited → bottle, poker threat → apology and promise of silence. | Child’s plea; promise to say nothing before people. | 045 | CRB | R: as above. U: duration; how it ended. |
| SW-S-0027 | sw.monica | Duties of imposed roles never considered → accepts duties as treasurer, then as Sage. | DISPOSITION_CHANGE | Elliott’s noblesse oblige → shame at avoiding duty → practice; at the climax, acts alone as the Silent Witch. | Private resolve, then public act before Casey. | 024, 033, 083 | CRB, SI | R: compliance with Felix’s pressure. U: persistence. |
| SW-S-0028 | sw.monica | Speech gains among trusted people → refusals and assertions to superiors and opponents. | DISPOSITION_CHANGE | Fact or another’s interest at stake → fear overridden → full sentences. | To Elliott, Caroline, Casey, Louis; still fails at a simple request in class. | 023, 043, 072, 095 | OTE | R: situational, not general. U: strangers. |
| SW-S-0029 | sw.monica | Terror of Nero’s human form → at ease with it. | DISPOSITION_CHANGE | Repeated contact → noticed only when Nero points it out. | Large strange men still frighten her. | 006 | CRB | R: specific to Nero. U: generalization. |
| SW-S-0030 | sw.monica | Self-exclusion as out of place → offers herself as the most out of place, as a gift. | DISPOSITION_CHANGE | Refuses Lana from imagined shame; later serves coffee from her father’s pot to friends. | Self-description in public. | 003, 031, 058 | OTE | R: none. U: none. |
| SW-S-0031 | sw.monica | Unable to say she expects nothing → says it: cannot expect anything of anyone; only numbers are safe. | REVEALED_NOT_NEW | Romance novel → incomprehension → resolution in numbers. | Private, to Nero. | 057 | CRB | R: contradicted by conduct. U: none. |
| SW-S-0032 | sw.monica | Political indifference → uses factional logic to save Casey. | ROLE_CONTEXT_CHANGE | Execution threatened → looks straight at Louis → bargains on his faction’s interest. | First negotiation she wins. | 095 | OTE | R: Louis chose to concede. U: none. |
| SW-S-0033 | sw.monica | Hides power from everyone at school → reveals herself to Casey by act and by name. | KNOWLEDGE_CHANGE | Lives at stake → ritual chant naming herself. | Before an enemy who is also a friend. | 084, 085 | OTE | R: none. U: consequences, SW-P-0019. |
| SW-S-0034 | sw.felix | Watcher inferred → watcher established; secret student of magic and fan of the Silent Witch; searching for her. | REVEALED_NOT_NEW | Isabelle’s account → memory; Louis overheard → joy and search. | Private 僕; public 私 and denial of magic. | 014, 064, 065, 087, 088 | CRB, OTE | R: none. U: none. |
| SW-S-0035 | sw.felix | Motive withheld → states he must become king without wanting anything prepared for his name; holds the role while he bears the name. | UNRESOLVED | Eliane mentioned → indifference → resolve. | Private thought; said aloud only to Elliott. | 062, 077 | CRB | R: rhetoric. U: meaning, SW-C-0022. |
| SW-S-0036 | sw.louis | Coercer with private respect → also a gift-giver, a user of an unknowing decoy, and a negotiator who spares Casey to keep Monica’s cooperation. | REVEALED_NOT_NEW | Mission interest → calculation → concession. | Courteous surface, violent reputation, private candour. | 009, 010, 096, 099 | CRB | R: pure self-interest. U: none. |
| SW-S-0037 | sw.cyril | Fair but hostile superior → concealed protector who asks to be called Cyril. | RELATIONSHIP_CHANGE | Her endangerment and illness → care disguised as duty. | Shouting register persists; gentle in dance and sickroom. | 037, 046, 059, 069, 098 | OTE | R: duty to the prince. U: none. |
| SW-S-0038 | sw.cyril | Suspicion of Monica’s hand → also links the forest mage to the Silent Witch. | KNOWLEDGE_CHANGE | Isabelle’s account of the wyverns → memory of the silent monster. | Private. | 054 | CRB | R: none. U: link to Monica. |
| SW-S-0039 | sw.elliott | Contempt → shame, a noble’s protective duty, and grudging respect for her eye. | DISPOSITION_CHANGE | Castling → self-loathing; carriage → trusts her; still calls her presumptuous. | Flippant surface over a strict code. | 020, 021, 023, 024, 063 | OTE, CRB | R: self-interest. U: future acceptance. |
| SW-S-0040 | sw.casey | — → a friend who was an assassin under orders, grieving her brothers and her land. | REVEALED_NOT_NEW | Father’s order → infiltration → staged accident → device → surrender. | Cheerful persona; resigned truth. | 027, 079, 080, 082, 097 | OTE, CRB | R: friendship partly real. U: V02 section 8.3. |
| SW-S-0041 | sw.lana | Brusque helper → public friend; her pride and loneliness as a parvenu’s daughter disclosed. | REVEALED_NOT_NEW | Out of place everywhere → wants to give the best → hurt → accepts Monica’s coffee. | Haughty manner over care. | 029, 032 | CRB | R: none. U: none. |
| SW-S-0042 | sw.claudia | — → learned, gloomy, sharp, devoted to Neil; saved Monica; refuses thanks. | REVEALED_NOT_NEW | Jealousy → surveillance; poisoning → competent first aid. | Deliberate unapproachability; changes air with Neil. | 047, 048, 050, 068 | OTE | R: none. U: SW-P-0020. |
| SW-S-0043 | sw.isabelle | Theatrical admirer → also a deliberate policy-maker for Monica’s protection. | REVEALED_NOT_NEW | Debt to the Silent Witch → villainess performance as deterrence → mirrored revenge. | Stage villainess in public, devotee in private. | 052, 055 | CRB | R: enjoyment of the role. U: none. |
| SW-S-0044 | sw.glen, sw.maclaggan, sw.bridget, sw.neil | Thin entries: Glen, generous, loud, powerful and imprecise, rule-bending; MacLaggan, fond teacher with poor eyesight and unstated knowledge; Bridget, clever and cold, unconvinced; Neil, kind, competent, sensitive about height and his engagement. | REVEALED_NOT_NEW | — | — | 015, 016, 018, 039, 041, 089 | OTE, CRB | Keep explicitly thin. |

Records at V03:

| ID | Key | State before → after | Kind | Process: perception → appraisal/affect → options → act/speech → consequence | Persona/private; recipient; register | Obs. | Class | Rival; uncertainty |
|---|---|---|---|---|---|---|---|---|
| SW-S-0045 | sw.monica | History before Minerva and at Minerva disclosed: a long silence; the friend Bernie who needed her dependence; the shortened-chant occasion; selection via Rutherford; an adoptive mother; father named Venedict Rain; repeated beatings by the uncle; scars. | REVEALED_NOT_NEW | Others’ memories and her own; the father’s book found. | Prologue in Bernie’s view; book scene private. | 003–009, 023, 105, 106, 121, 133 | OTE, CRB | R: Bernie’s retrospection is self-serving. U: passage from uncle to guardian. |
| SW-S-0046 | sw.monica | Wanted Bernie’s approval for years → renounces it after defending Lana. | DISPOSITION_CHANGE | Friend insulted → anger → full declaration → renunciation; eyes no longer reflect him. | To Bernie, before Lana; plain form. | 042–046 | OTE | R: momentary. U: durability, SW-P-0025. |
| SW-S-0047 | sw.monica | Asks nothing for herself → asks for a wish, names a selfish motive, reaches out first. | DISPOSITION_CHANGE | Wager → wish; theft → mourning motive; Felix hurt → offers her hand as a ghost. | To Felix as Ike; to the tool. | 025, 088, 097, 100 | OTE | R: festival exception. U: persistence. |
| SW-S-0048 | sw.monica | Cannot fly → flies by riding technique; computes combat; casts mind interference on a tool. | REVEALED_NOT_NEW; capacity extended | Necessity → fear → recalled lessons → improvised method. | Alone; Lynn by voice. | 095–099 | OTE, NP | R: none. U: none. |
| SW-S-0049 | sw.monica | Fear of people and touch unchanged; numbers used to bear people; secrecy toward friends continues. | UNRESOLVED | Touch → stiffening; crowds → memory; friends → partial accounts. | — | 013, 058, 076, 087, 117, 130 | OTE, CRB | R: none. U: none. |
| SW-S-0050 | sw.felix | Wish withheld → a ten-year vow to inscribe the name Felix Arc Ridill in history; must become king without wanting it; magic study forbidden to him; nights in the town gathering the duke’s malcontents. | REVEALED_NOT_NEW | Duke’s contempt → emptied obedience; special day → vow restated. | 私 to the duke and of kingship. | 061, 065, 082, 101, 103 | OTE | R: ordinary ambition. U: why the vow and the prohibition. |
| SW-S-0051 | sw.felix | Taming game → Ike: laughter, 僕, the ghost conceit, permission to value the book, mourning a friend; then the pendant as possession and farewell, and the prince’s smile restored. | RELATIONSHIP_CHANGE | Finds her → masks → kindness to her fear → morning test and gift. | 僕 as Ike; 私 resumes. | 078, 087, 100, 107, 109, 118–122 | OTE, CRB | R: performance. U: attachment’s object, SW-C-0029. |
| SW-S-0052 | sw.felix | Cluster extended: child in Elliott’s memory, dream of a boy called Felix and a page, dead friend, necessary scar, eye colours. | UNRESOLVED | — | Dream boy described from outside. | 018–020, 065, 070, 109, 112–114, 121 | OTE, CRB, UQ | No hypothesis, SW-C-0022. |
| SW-S-0053 | sw.bernie | Rescuer and helper who needed her dependence → envious rival → knows her identity and mission and covers for her, demanding gratitude. | REVEALED_NOT_NEW; KNOWLEDGE_CHANGE | Envy → accusation → defeat → impostor → protective lie. | 僕; distant 貴女 throughout. | 001–009, 035, 042, 046, 050–056 | OTE, CRB | R: repentance vs possession, V03 section 8.2. U: motive. |
| SW-S-0054 | sw.louis | Coercer and investor → also the source of the verdict that she is heartless and was chosen for it; investigator of the Empire’s role. | REVEALED_NOT_NEW | Memory of the dragon campaign → contempt and pity. | 私; candour with Casey. | 029, 072, 073, 123, 128, 130, 131 | CRB | R: his verdict is half right. U: none. |
| SW-S-0055 | sw.mary | Named Sage → eldest, comic and wilful; reads Felix’s unreadable star; permits the theft; tests Monica; sees a star of loss near hers. | REVEALED_NOT_NEW | Stars → test → silence when questioned. | あたくし; playful register. | 067–071, 093, 115, 116 | CRB | R: protective intent. U: aim, SW-P-0024. |
| SW-S-0056 | sw.elliott | Contempt for upstarts explained by his uncle’s ruin; warns Monica; remembers the child Felix. | REVEALED_NOT_NEW | Shame at castling → apology in effect → memory → warning. | 俺. | 017–022 | CRB | R: none. U: none. |
| SW-S-0057 | sw.lana | Friend → armourer and defender who names Bernie’s envy. | REVEALED_NOT_NEW | Prepares Monica; intervenes; proud. | わたし; sharp to Bernie. | 032, 044, 049 | OTE | R: none. U: none. |
| SW-S-0058 | sw.cyril, sw.claudia, sw.isabelle, sw.bridget | Thin: Cyril strongest duelist, self-blaming, protective; Claudia politically lucid, calls Felix a puppet; Isabelle explains the festival and gives up her wish; Bridget probes Monica’s education. | REVEALED_NOT_NEW | — | — | 015, 016, 038, 057, 059, 063, 066, 089 | OTE, CRB | Keep thin. |
| SW-S-0059 | sw.benjamin, sw.robert, sw.maclaggan, sw.boyd, sw.redding | Thin: Benjamin’s musical chess; Robert’s proposal; MacLaggan’s emphasized remark; Boyd’s apology; Redding’s sneer. | REVEALED_NOT_NEW | — | — | 027, 037, 040, 047 | OTE | Keep thin. |
| SW-S-0060 | sw.bartholomeus | Imperial craftsman exiled for striking his master; forger; victim of the tool; smitten with the “Silent Witch” he believes Lynn to be; takes the uniform commission. | REVEALED_NOT_NEW | — | 俺; rough. | 074, 077, 080, 090, 124 | OTE | R: none. U: none. |
| SW-S-0061 | sw.porter | Curt bookseller and novelist; father’s friend; prices the book at two gold coins. | REVEALED_NOT_NEW | — | 僕. | 102, 106, 126 | OTE | R: none. U: SW-P-0026. |
| SW-S-0062 | sw.yuan, sw.heidi | Imperial agent with an unstable face and his pupil; escape; intent to expose Felix’s and Monica’s secrets. | REVEALED_NOT_NEW | Defeat → analysis → identifies Monica as obstacle. | Yuan’s feminine register; Heidi stiff. | 051–053, 123, 125 | OTE | R: none. U: sponsor. |
| SW-S-0063 | sw.duke-clockford | Reported power → on stage: commands the school, despises Felix in private. | REVEALED_NOT_NEW | — | 私; imperative. | 060, 061, 113 | OTE | R: none. U: aims. |
| SW-S-0064 | sw.casey, sw.doris, sw.cassandra | Thin: Casey at the convent, concerned for Monica; Doris and Madam Cassandra as Felix’s night-town intermediaries. | REVEALED_NOT_NEW | — | — | 081–083, 127–131 | OTE | Keep thin. |

Records at V04:

| ID | Key | State before → after | Kind | Process: perception → appraisal/affect → options → act/speech → consequence | Persona/private; recipient; register | Obs. | Class | Rival; uncertainty |
|---|---|---|---|---|---|---|---|---|
| SW-S-0065 | sw.monica | Childhood after the execution completed: abuse, dissociation, loss of language, rescue and adoption by Hilda. | REVEALED_NOT_NEW | Uncle’s blows → formulas as refuge → numbers only → named by Hilda → speech returns. | Narrated soberly. | 001–008 | NP, OTE | R: none. U: none. |
| SW-S-0066 | sw.monica | Numerical dissociation as defence → as chosen combat stance → unusable against people she knows. | DISPOSITION_CHANGE | Threat to Cyril → calculation says bluff → fear prevails → defeat → renounces the refrain as an excuse. | Private; to Louis. | 085, 088, 090, 096, 097 | OTE, CRB | R: poison and fatigue. U: durability. |
| SW-S-0067 | sw.monica | Refuses help for her own problems; accepts offered help; helps a stranger unbidden. | DISPOSITION_CHANGE, partial | Own problem → no signal; offered hand → accepts; stranger lost → speaks first. | — | 031, 042, 043, 073, 107 | OTE | R: situational. U: none. |
| SW-S-0068 | sw.monica | Chooses to remain Monica Norton until the mission ends, knowing she deceives friends; expects to return to the hut; no wish to marry. | KNOWLEDGE_CHANGE | Drawer of gifts → apology to all → resolve. | Private. | 098, 110, 115 | CRB | R: none. U: none. |
| SW-S-0069 | sw.monica | Keeps Ike’s confidences from Louis. | RELATIONSHIP_CHANGE | Report → omission → loyalty to a friend. | Private. | 067 | CRB | R: none. U: consequence. |
| SW-S-0070 | sw.felix | Attachment to Monica stated in viewpoint: would give her a flower; jealous of Cyril; wants her to wear his pendant. | RELATIONSHIP_CHANGE | Sees the rose → resentment → cannot act (no freedom) → jealousy shown privately. | 僕 to Monica; 私 in public. | 057, 081, 082, 105, 114 | OTE | R: possessive play. U: nature. |
| SW-S-0071 | sw.felix | Wish to be remembered → a hero’s posthumous light, overriding his friend’s wish; Monica perceives obsession. | UNRESOLVED | Glen’s heroism → emptied gaze; stars → the constellation question. | Private to Monica. | 030, 064, 113, 116, 117 | OTE, CRB | R: rhetoric. U: meaning, SW-C-0038. |
| SW-S-0072 | sw.cyril | Background disclosed: untitled abusive father; withholding mother; adoption for Claudia’s engagement; magic as his own weapon; over-absorption. | REVEALED_NOT_NEW | — | Others’ accounts. | 015, 070, 077, 078 | OTE | R: none. U: none. |
| SW-S-0073 | sw.cyril | Concealed care → a disguised invitation, practical help, a private dance; attention to her hand. | RELATIONSHIP_CHANGE | Worry → flower as charm → covers others → notices ice and hand. | 貴様 and ノートン会計; 「レディ」 once. | 028, 029, 032, 103, 108–110 | OTE | R: duty. U: what he concludes. |
| SW-S-0074 | sw.bernie | Envious former friend → rival and future ally; leaving Minerva as heir. | DISPOSITION_CHANGE | Brother’s death → relief → confession of rivalry → offer. | 僕; エヴァレット魔法伯. | 034–038 | OTE | R: pride. U: none. |
| SW-S-0075 | sw.louis | Rutherford’s pupil, Glen’s master and decoy-maker; repeats his verdict; takes blame; withholds a hypothesis. | REVEALED_NOT_NEW | — | 私; ジジイ of his master. | 040, 049, 050, 065, 096, 120 | OTE, CRB | R: none. U: hypothesis. |
| SW-S-0076 | sw.ray | Introduced: curse-caster Sage; craves love; dreads brightness; protective once trusted; enjoys the festival. | REVEALED_NOT_NEW | Secret shared → loyalty; enemy → curse. | 俺; self-pitying litany. | 022–024, 047, 048, 094, 095 | OTE | R: none. U: none. |
| SW-S-0077 | sw.eliane | Entitled, competitive, proud; cursed fragment amplifies; final anger her own. | REVEALED_NOT_NEW | Envy → sabotage → near disaster → fury at Glen. | わたくし; sweet public manner. | 044, 054, 056, 061, 063 | OTE, NE | R: curse alone. U: none. |
| SW-S-0078 | sw.glen | Unknowing decoy → public hero and known disciple; frank charm. | ROLE_CONTEXT_CHANGE | Substitute → flight rescue → acclaim → punished for flying. | っす; 下町訛り. | 055, 062, 065, 100 | OTE | R: none. U: none. |
| SW-S-0079 | sw.isabelle, sw.sylvia, sw.henry | A family of villain performers in Monica’s service. | REVEALED_NOT_NEW | — | Hand signal; performed cruelty. | 019, 043, 046 | OTE | Keep thin. |
| SW-S-0080 | sw.claudia, sw.neil | Claudia’s love for Neil and history; Neil’s mediation and flower. | REVEALED_NOT_NEW | — | — | 010, 013, 015, 106 | OTE | Keep thin. |
| SW-S-0081 | sw.bridget | Has watched Monica fly; ten years of endurance; resolves to take back her prince. | UNRESOLVED | — | あたくし. | 027, 118 | OTE | R: none. U: SW-P-0030. |
| SW-S-0082 | sw.yuan, sw.heidi | Two aims revealed; a master; defeated, threaten, poison, escape; Yuan cursed. | REVEALED_NOT_NEW | — | アタシ; わたくし in pain. | 051, 083–094 | OTE | R: none. U: master. |
| SW-S-0083 | sw.hilda, sw.myra | Two guardians: Hilda rescued and praised; Myra withheld praise and now resolves to welcome. | REVEALED_NOT_NEW | — | — | 006–008, 074–078 | OTE | Keep thin. |
| SW-S-0084 | sw.nero, sw.albright-traitor, sw.bartholomeus, sw.maclaggan | Thin: Nero’s non-human traits; the traitor’s patron and hatred; Bartholomeus hired by Leinbourg; MacLaggan’s knowing remark. | REVEALED_NOT_NEW | — | — | 069, 092, 121–123 | OTE | Keep thin. |

Records at AFTER04:

| ID | Key | State before → after | Kind | Process: perception → appraisal/affect → options → act/speech → consequence | Persona/private; recipient; register | Obs. | Class | Rival; uncertainty |
|---|---|---|---|---|---|---|---|---|
| SW-S-0085 | sw.monica | Keeps nothing for its own sake → makes and keeps a charm; first birthday celebrations since Minerva; asks for a gift; first season’s card; thanks Nero. | DEVELOPMENT | Rose from Cyril → water, drying, jar → “a charm that makes me stronger” → drawer; Lana’s pouch → 「……欲しい」. | Private; to Lana, Nero, Hilda. | 039, 066, 067, 146, 147, 160, 162 | OTE | R: comic register. U: durability after departure. |
| SW-S-0086 | sw.monica | Drifted into magic → wishes to be proud of something; claims her place as a council officer. | DISPOSITION_CHANGE | Glen’s question → Cyril’s answer → recognition of her own drift → 「……誇れたら、いいな」. | Private. | 077, 079 | OTE, CRB | R: one scene. U: whether it holds. |
| SW-S-0087 | sw.monica | Reads hidden feelings; withholds, then helps when invited; thanks require courage. | DEVELOPMENT | Handkerchief reverse → silence → Sheila’s account → card decoded. | To Sheila. | 105, 118, 156–158 | OTE | R: none. U: none. |
| SW-S-0088 | sw.monica | Cover by small lies; power used only unseen; seventeen at the first day of Shelgria; retrospectively, a frightened new Sage. | REVEALED_NOT_NEW | Questioned → improvised account; threat → silent spell. | Persona to Felix, Cyril, Elliott; private power. | 004, 006, 044, 072, 083, 092, 114, 116, 119, 137 | OTE | R: none. U: none. Retrospective for 004, 006. |
| SW-S-0089 | sw.felix | Ike in daylight; denied reading by his grandfather’s surveillance; glad of a listener; attentive and teasing to Monica; marks her birthday. | DEVELOPMENT | Donation list → scheme → crowded room → disappointment → 「過ぎた贅沢だ」. | Ike persona to Monica; prince to others. | 035, 043, 059, 062, 064, 137, 138, 149 | OTE | R: performance. U: source of the birthday; addressee of 「ずるい」. |
| SW-S-0090 | sw.felix | Working prince: appraisal of officers, Neil’s succession, tolerance of Claudia, gentleness with a child. | REVEALED_NOT_NEW | — | Public. | 030, 032, 057, 086, 087 | OTE, CRB | R: none. U: none. |
| SW-S-0091 | sw.cyril | Defender of juniors; teacher of earned pride; once an isolated adopted heir hoping for a friend; sincere duellist. | REVEALED_NOT_NEW | Glen’s oath → defence → 「……頼む」; Byron’s request → duel → victory. | To Glen, Monica, Byron. | 069, 070, 071, 074, 079, 093, 097, 109, 154 | OTE | R: none. U: none. Retrospective for 069. |
| SW-S-0092 | sw.glen | Swept into apprenticeship; distrusts magic battles; takes Cyril’s lesson; good with children; MacLaggan’s unfinished question. | REVEALED_NOT_NEW | — | — | 078, 079, 081, 090, 094, 099 | OTE | R: none. U: Minerva link. Retrospective for 099. |
| SW-S-0093 | sw.byron | Duels to win back a fiancée he misread; trains dangerously; loses; vows to win before graduation. | REVEALED_NOT_NEW | — | — | 049, 068, 116, 117, 155 | OTE | Keep thin. |
| SW-S-0094 | sw.sheila | Hides a confession in blue thread; named Cyril from embarrassment; verbal tic from failed words. | REVEALED_NOT_NEW | — | — | 156 | OTE | Keep thin. |
| SW-S-0095 | sw.elliott | Creed of rank from an uncle’s suicide and a withheld earlier event; a father’s slap; friendship with Benjamin; Felix’s childhood playmate. | REVEALED_NOT_NEW | — | Private to Benjamin. | 082, 110–112, 121, 122 | OTE, CRB | R: none. U: the second event. Retrospective for 122. |
| SW-S-0096 | sw.benjamin | Loves women in love; slump cured by a new piece; turns to Bridget. | REVEALED_NOT_NEW | — | — | 101, 111, 121 | OTE | Keep thin. |
| SW-S-0097 | sw.claudia, sw.neil | Claudia ignores Felix and watches only Neil; Neil will accept a duel over her. | REVEALED_NOT_NEW | — | — | 055, 056, 061, 120, 153 | OTE | Keep thin. |
| SW-S-0098 | sw.isabelle | Villainy from a family misreading; now a method of social investigation and quiet rescue. | REVEALED_NOT_NEW | — | Performance; private devotion. | 128, 131, 140–143, 150–152 | OTE | R: none. U: none. Retrospective for 150–152. |
| SW-S-0099 | sw.lana | A handmade gift instead of a costly one; asks for coffee on her own birthday. | REVEALED_NOT_NEW | — | — | 146–148 | OTE | Keep thin. |
| SW-S-0100 | sw.hilda | Hopeless at housework; overjoyed at Monica’s first card. | REVEALED_NOT_NEW | — | — | 146, 161, 162 | OTE | Keep thin. |
| SW-S-0101 | sw.louis, sw.rosalie | Tyrant to colleagues, admirer of Monica’s ability, devoted to Rosalie, teacher of strength against unreason; Rosalie a doctor. | REVEALED_NOT_NEW | — | — | 003, 007, 010, 023–028, 099 | OTE | Retrospective throughout. |
| SW-S-0102 | sw.ray | First to speak to Monica; re-covered his primer in pink; curses for what cannot be said aloud; answers her call. | REVEALED_NOT_NEW | — | — | 011–013, 019, 139 | OTE | Retrospective for 011–019. |

Records at V05:

| ID | Key | State before → after | Kind | Process: perception → appraisal/affect → options → act/speech → consequence | Persona/private; recipient; register | Obs. | Class | Rival; uncertainty |
|---|---|---|---|---|---|---|---|---|
| SW-S-0103 | sw.monica | Hidden treasurer → acts openly as the Silent Witch without speech. | CONTEXT_CHANGE | Official order → veil, writing, an attendant spokesman → strain and farce. | Persona as the Witch. | 027, 028, 039, 049, 059 | OTE | R: none. U: none. |
| SW-S-0104 | sw.monica | Vow to do better among people → defeat at the table → recovery. | DEVELOPMENT | Market vow → lost negotiation → grief → Glen’s example → descends. | Private; before witnesses. | 021, 129, 130, 136, 137 | OTE | R: none. U: durability. |
| SW-S-0105 | sw.monica | Numbers as refuge → numbers as evidence; speaks as a Sage to accuse. | DISPOSITION_CHANGE | Dragon’s memory → body measurements → spoken accusation → father’s saying as declaration. | Public, to Sams. | 139, 142, 144 | OTE | R: one confrontation. U: none. |
| SW-S-0106 | sw.monica | Purpose: the mission → also her father’s innocence. | GOAL_CHANGE | Sams’s words → Hilda’s account → vow → hires help. | Private. | 147, 149, 150, 166, 170, 180 | OTE | R: none. U: none. |
| SW-S-0107 | sw.monica | Home and bonds: first visit to Hilda as a Sage; misses Nero; the taming retrospect. | REVEALED_NOT_NEW | — | Private. | 123, 124, 164, 168 | OTE | Retrospective for 123, 124. |
| SW-S-0108 | sw.felix | Admiration for the Witch stated at length; the paper; the wish to see her face. | DEVELOPMENT | Letter → joy → paper annotated → rescue → longing. | Private viewpoint. | 026, 034, 042, 053, 102, 133 | OTE | R: performance. U: nature of the feeling. |
| SW-S-0109 | sw.felix | Puppet performed → resistance planned. | DISPOSITION_CHANGE | Anonymous letter → empty face → near death → plan to act. | Private. | 096–100, 159 | OTE, CRB | R: his inference about Clockford. U: none. |
| SW-S-0110 | sw.felix | Knows the black dragon and the Witch’s school; withholds his own knowledge; vow ending in Arc. | REVEALED_NOT_NEW | — | Private. | 107, 128, 129, 135 | OTE | U: meaning of Arc. |
| SW-S-0111 | sw.glen | Vow kept; cursed protecting others; mana above 250 and a past runaway. | DEVELOPMENT | — | — | 058, 079, 080, 115 | OTE | R: none. U: none. |
| SW-S-0112 | sw.cyril | Reconciliation with his mother; accepted as heir; his own vow. | DEVELOPMENT | Fear at the door → welcome → praise → vow. | Private. | 152–155, 179 | OTE | R: none. U: none. |
| SW-S-0113 | sw.ray | Master of his art with an ethic; insecure. | REVEALED_NOT_NEW | — | — | 112–114, 134, 145 | OTE | Keep thin. |
| SW-S-0114 | sw.nero | Revealed as the Worgan black dragon; chose Monica as master. | REVEALED_NOT_NEW | — | — | 106, 122–124 | OTE | Retrospective for 123, 124. |
| SW-S-0115 | sw.bartholomeus | Misreads; bargains for Lynn; catches Sams; hired. | REVEALED_NOT_NEW | — | — | 035, 057, 065, 150 | OTE | Keep thin. |
| SW-S-0116 | sw.albright-traitor | As Peter Sams: envious; puppet-curse research; sold Venedict to 閣下; consumed by his own curse. | REVEALED_NOT_NEW | — | — | 036, 140, 141, 147, 148 | OTE | U: 閣下. |
| SW-S-0117 | sw.hilda | Withholds the noble’s name to protect Monica. | REVEALED_NOT_NEW | — | — | 166, 167 | OTE | Keep thin. |
| SW-S-0118 | sw.bridget | Hired the detective; grieves alone for Felix. | REVEALED_NOT_NEW | — | — | 030, 031, 183 | OTE | U: aim. |
| SW-S-0119 | sw.albert | Forced to Serendia; suspects Felix; trusts Lionel. | REVEALED_NOT_NEW | — | — | 161, 162 | OTE | Keep thin. |
| SW-S-0120 | sw.bernie, sw.bradford, sw.emmanuel, sw.louis | Thin: Bernie’s resolve and warning; Bradford and Emmanuel on stage; Louis’s card lesson and lie. | REVEALED_NOT_NEW | — | — | 001–008, 045, 174, 181 | OTE | Keep thin. |

Records at V06:

| ID | Key | State before → after | Kind | Process: perception → appraisal/affect → options → act/speech → consequence | Persona/private; recipient; register | Obs. | Class | Rival; uncertainty |
|---|---|---|---|---|---|---|---|---|
| SW-S-0121 | sw.monica | Unnamed rage → named anger with a cause, spoken and used. | DISPOSITION_CHANGE | Clockford’s words → butterflies → Glen kicked → “angry” → Louis’s licence. | Private; spoken to Hubert. | 064, 154, 155, 184, 185 | OTE | R: two episodes. U: durability. |
| SW-S-0122 | sw.monica | Two selves pressed together: the Witch among schoolmates; Monica Norton’s life missed and a future offered. | DEVELOPMENT | Cyril’s courtesy → flight → Lana’s offer → guilt. | Public as the Witch; private. | 047–049, 123, 124 | OTE | R: none. U: none. |
| SW-S-0123 | sw.monica | The father’s inquiry reaches Clockford by inference. | DEVELOPMENT | Ray’s report → Clockford’s offer → Bartholomeus’s report → inference. | Private. | 021–025, 058, 204–206 | CRB | R: her inference. U: 閣下; the noble. |
| SW-S-0124 | sw.monica | New high homing formula; rewrites another’s tools; frees and seals spirits. | DEVELOPMENT | — | — | 159, 160, 203 | OTE | R: none. U: none. |
| SW-S-0125 | sw.monica | Refuses help; cannot call for it; apologizes as habit. | REVEALED_NOT_NEW | — | Private. | 115, 130; S22:E000095 | OTE | U: change. |
| SW-S-0126 | sw.felix | The search for the Witch systematized; delight in her magic. | DEVELOPMENT | Staff checked → council asked → report. | Public and private. | 079, 080, 131 | OTE | R: none. U: none. |
| SW-S-0127 | sw.felix | Ruthless means: an order to kill; Emmanuel as an instrument; lure and concealment. | REVEALED_NOT_NEW | — | Private. | 147, 149, 183, 197 | OTE | U: motive. |
| SW-S-0128 | sw.felix | Wants to be relied on; overlays a remembered friend on Monica; private 僕. | REVEALED_NOT_NEW | — | Private viewpoint. | 114, 165–167 | OTE | U: the friend. |
| SW-S-0129 | sw.glen | Minerva past told to the runaway; pain hidden; homing learned; vow kept. | REVEALED_NOT_NEW | — | — | 086–091, 101, 144 | OTE | Retrospective for 086–090. |
| SW-S-0130 | sw.cyril | Heir at court; protective senior; watches the hand; hears the title; thanks spirits. | DEVELOPMENT | — | Public; private. | 018, 083, 127, 152, 182 | OTE | R: none. U: what he concludes. |
| SW-S-0131 | sw.ray | Inquiry results; protective curses; the three youngest. | REVEALED_NOT_NEW | — | — | 021–024, 046 | OTE | Keep thin. |
| SW-S-0132 | sw.raul | On stage: plant researcher, listener through flowers, seeker of friends. | REVEALED_NOT_NEW | — | — | 019, 038, 039, 200, 201 | OTE | Keep thin. |
| SW-S-0133 | sw.hubert-dee | Hunter of strong prey; false chantless tools; bargain; defeat. | REVEALED_NOT_NEW | — | — | 118, 133, 142, 156, 160 | OTE | Keep thin. |
| SW-S-0134 | sw.emmanuel | Signed fraud; spirit-powered tools; the whistle; a patron. | REVEALED_NOT_NEW | — | — | 194, 196, 210, 211 | OTE | U: the patron. |
| SW-S-0135 | sw.duke-clockford | Offers the Witch office; claims Felix; once employed Sams. | REVEALED_NOT_NEW | — | — | 061, 063, 204 | OTE | U: 閣下; the noble. |
| SW-S-0136 | sw.isabelle | Performance in Kerbeck; diary; threat to Hubert. | REVEALED_NOT_NEW | — | — | 005, 071, 175, 176 | OTE | Keep thin. |
| SW-S-0137 | sw.albert, sw.patrick | Half a hostage; plots against Felix; friendship on Glen’s terms. | REVEALED_NOT_NEW | — | — | 107, 108, 117 | OTE | Keep thin. |
| SW-S-0138 | sw.lionel, sw.robert, sw.lana, sw.bartholomeus, sw.maclaggan, sw.carla, sw.mary, sw.louis | Thin: Lionel’s judgement of Felix; Robert’s suit; Lana’s offer; Bartholomeus’s refusal of pay; MacLaggan’s warning; Carla named; Mary’s warning; Louis’s licence. | REVEALED_NOT_NEW | — | — | 034, 050, 098, 124, 174, 185, 207, 215 | OTE | Keep thin. |

Records at V07:

| ID | Key | State before → after | Kind | Process: perception → appraisal/affect → options → act/speech → consequence | Persona/private; recipient; register | Obs. | Class | Rival; uncertainty |
|---|---|---|---|---|---|---|---|---|
| SW-S-0139 | sw.monica | Asks for help for the first time and accepts a civilian’s plan. | DISPOSITION_CHANGE | Lynn’s attack → hesitation → request → success. | Spoken. | 005, 015 | OTE | R: one episode. U: durability. |
| SW-S-0140 | sw.monica | Calculates against an upper spirit and the Star Spear; destroys an ancient tool; laments a split formula. | DEVELOPMENT | — | — | 006, 101, 110, 111 | OTE | R: none. U: none. |
| SW-S-0141 | sw.monica | Saves Romaria from her own ego; does not want the Witch thanked. | REVEALED_NOT_NEW | — | Private. | 126, 127, 129 | OTE | U: none. |
| SW-S-0142 | sw.monica | Wants to know Felix; steps forward on her own; inquires into love. | GOAL_CHANGE | Bridget’s account → the wish to know → the infiltration. | Private. | 157, 179, 190 | OTE | R: none. U: what she concludes. |
| SW-S-0143 | sw.monica | Withholds four matters from Louis; an unspoken conclusion about Felix. | REVEALED_NOT_NEW | — | Private. | 143, 211, 213 | OTE, CRB | U: her conclusion. |
| SW-S-0144 | sw.felix | Seen through others: a sickly, shy child; changed after illness. | REVEALED_NOT_NEW | — | Others’ accounts. | 159, 165, 170, 171, 173 | CRB | U: identity cluster. |
| SW-S-0145 | sw.felix | Search stalls; passes the rose test; offers Emmanuel help. | REVEALED_NOT_NEW | — | Private and public. | 148–150, 168, 180 | OTE | U: motive. |
| SW-S-0146 | sw.cyril | Keeps his promise; carries Romaria; links the Witch’s cursed hand; apologizes. | DEVELOPMENT | — | — | 025, 062, 124, 166 | OTE | R: none. U: what he concludes. |
| SW-S-0147 | sw.glen | Wants to help; resents his helplessness. | REVEALED_NOT_NEW | — | — | 042, 144 | OTE | Keep thin. |
| SW-S-0148 | sw.raul | The cruel persona and the rose fortress; loneliness. | REVEALED_NOT_NEW | — | — | 035–039, 131 | OTE | U: persona or possession. |
| SW-S-0149 | sw.ray | Takes over the armour; argues against helping spirits. | REVEALED_NOT_NEW | — | — | 040, 092, 130 | OTE | Keep thin. |
| SW-S-0150 | sw.louis | Axe; former Magic Corps head; expects a daughter; withholds and tests. | REVEALED_NOT_NEW | — | — | 020, 022, 079, 136, 138 | OTE | Keep thin. |
| SW-S-0151 | sw.bartholomeus | His sister’s fate; pride lost and stubbornness kept; Mary’s patronage. | REVEALED_NOT_NEW | — | — | 008–014, 224 | OTE | Retrospective for 008–012. |
| SW-S-0152 | sw.emmanuel | Envy; the whistle; possession; flight. | REVEALED_NOT_NEW | — | — | 055–059, 103, 133 | OTE | Keep thin. |
| SW-S-0153 | sw.bridget | Her memory, belief and disguise; resolve after disappointment. | REVEALED_NOT_NEW | — | — | 158–165, 176, 194, 212 | OTE, CRB | Retrospective for 158–165. |
| SW-S-0154 | sw.mary, sw.carla, sw.lynn | Mary closes the affair and funds a helper; Carla’s Star Spear; Lynn freed. | REVEALED_NOT_NEW | — | — | 098, 117, 141, 224 | OTE | Keep thin. |
| SW-S-0155 | sw.ice-spirit, sw.sezdio | Romaria’s history; Sezdio’s plan and restraint. | REVEALED_NOT_NEW | — | — | 046, 068, 120, 140 | OTE | Retrospective for 120. |
| SW-S-0156 | sw.yuan, sw.yuan-master | Yuan’s single face for his master; the master’s resolve. | REVEALED_NOT_NEW | — | — | 220–223 | OTE | U: the master’s identity. |

Records at V08:

| ID | Key | State before → after | Kind | Process: perception → appraisal/affect → options → act/speech → consequence | Persona/private; recipient; register | Obs. | Class | Rival; uncertainty |
|---|---|---|---|---|---|---|---|---|
| SW-S-0157 | sw.monica | From bystander to actor: the report aloud, the threat, the bargain. | DISPOSITION_CHANGE | The answer checked → the emperor’s refusal → threat → bargain. | Spoken; chess register. | 009, 061, 064 | OTE | R: necessity. U: durability. |
| SW-S-0158 | sw.monica | Reveals herself to Porter, Isaac and the council; asks for help. | DISPOSITION_CHANGE | Diary → refusal of sacrifice → the drawer → the reveal. | Spoken. | 084, 259, 283, 291 | OTE | R: none. U: the response. |
| SW-S-0159 | sw.monica | Chooses to save Isaac over clearing her father. | GOAL_CHANGE | Father’s case known → cannot → diary → resolve. | Private. | 182, 241, 253 | OTE | R: none. U: outcome. |
| SW-S-0160 | sw.monica | Binds Felix to remember her father’s name; cannot name what he is to her. | REVEALED_NOT_NEW | — | Private. | 180, 181, 240 | OTE | U: the feeling. |
| SW-S-0161 | sw.felix | Disclosed as Isaac Walker: a doctor’s son who lost his family to dragons. | REVEALED_NOT_NEW | — | Own memory. | 097–105 | OTE | Retrospective. |
| SW-S-0162 | sw.felix | The substitution accepted to keep the prince’s name; self-judged guilty. | REVEALED_NOT_NEW | — | Own memory. | 106–158 | OTE | Retrospective. |
| SW-S-0163 | sw.felix | Wildianu contracted alone; the Witch’s magic as the one thing he loves. | REVEALED_NOT_NEW | — | Own memory. | 159–175 | OTE | Retrospective. |
| SW-S-0164 | sw.felix | Suborns Emmanuel against Clockford; would sacrifice for the throne. | REVEALED_NOT_NEW | — | Private and spoken. | 090–094, 177 | OTE | Keep. |
| SW-S-0165 | sw.felix | Learns the father’s case; cannot harm Monica; arrested; plans to die a villain. | DEVELOPMENT | Porter → certainty → arrest → resolve. | Private. | 199, 202, 208, 260 | OTE | U: the misunderstanding. |
| SW-S-0166 | sw.arc | Frail, kind, self-blaming; the letter; the fall. | REVEALED_NOT_NEW | — | Own viewpoint in memory. | 127–146, 245, 246 | OTE | Retrospective. |
| SW-S-0167 | sw.duke-clockford | The bishop killed; the trap; the substitution; the discard; his father’s history. | REVEALED_NOT_NEW | — | Own viewpoint in the secret episode. | 026, 145, 156, 191, 294 | OTE | U: 閣下. |
| SW-S-0168 | sw.cyril | Praises Monica; collapses as a clown; recovers his choice. | DEVELOPMENT | Arrest → truth → shouted down → resolve. | — | 193, 227–229 | OTE | Keep. |
| SW-S-0169 | sw.elliott | Knew the substitution; chose to watch. | REVEALED_NOT_NEW | — | Retrospective. | 216–226 | OTE | Keep. |
| SW-S-0170 | sw.louis | Proves the prince false; plans denunciation; becomes a father. | REVEALED_NOT_NEW | — | — | 185–189, 252 | OTE | Keep thin. |
| SW-S-0171 | sw.yuan-master | The emperor’s argument against war and his bargain. | REVEALED_NOT_NEW | — | 余. | 054–066 | OTE | Keep. |
| SW-S-0172 | sw.porter, sw.hilda | The bystander and the keeper. | REVEALED_NOT_NEW | — | — | 001–006, 081–083, 264–267 | OTE | Keep thin. |
| SW-S-0173 | sw.wildianu | An unnamed love for Irene; the offer of himself. | REVEALED_NOT_NEW | — | — | 280–282 | OTE | Keep thin. |
| SW-S-0174 | sw.albert, sw.eliane, sw.bridget, sw.casey | Albert as reserve; Eliane’s engagement; Bridget’s grief; Casey’s blessing. | REVEALED_NOT_NEW | — | — | 224, 249, 284, 285 | OTE | Keep thin. |

Records at V09:

| ID | Key | State before → after | Kind | Process: perception → appraisal/affect → options → act/speech → consequence | Persona/private; recipient; register | Obs. | Class | Rival; uncertainty |
|---|---|---|---|---|---|---|---|---|
| SW-S-0175 | sw.monica | Reveals herself; asks for help; leads a collective plan. | DISPOSITION_CHANGE | Reveal → tears → plan → agreement. | Spoken. | 005–028 | OTE | R: none. U: none. |
| SW-S-0176 | sw.monica | Plays the Witch at the council by script; stages a truth; silences Clockford. | DEVELOPMENT | Heels, script, charm → performance. | Public register. | 082–099 | OTE | Keep. |
| SW-S-0177 | sw.monica | Chooses Isaac’s life over her father’s name; refuses revenge; calls him a friend. | GOAL_CHANGE | — | Spoken. | 119, 120, 126 | OTE | U: her feeling. |
| SW-S-0178 | sw.monica | Leaves the hut by choice; asks to be called Monica; takes an apprentice; coffee with friends. | DISPOSITION_CHANGE | — | — | 147–151, 173, 182 | OTE | Keep. |
| SW-S-0179 | sw.felix | Refuses a name; confesses all; recognizes the Witch. | REVEALED_NOT_NEW | — | Private. | 076–081 | OTE | Keep. |
| SW-S-0180 | sw.felix | Reads the diary; obsession ends; loves Monica. | DISPOSITION_CHANGE | Diary → accident → release. | Private viewpoint. | 121–128 | OTE | R: none. U: none. |
| SW-S-0181 | sw.felix | Duke of Erin; visits the grave; becomes her apprentice; jealous. | DEVELOPMENT | — | — | 164–181 | OTE | Keep. |
| SW-S-0182 | sw.cyril | Kneels; recovers; sacrifices himself against Louis; loyal. | REVEALED_NOT_NEW | — | — | 008–011, 066, 180 | OTE | Keep. |
| SW-S-0183 | sw.louis | First Minerva brat; barrier fighter; held off; concedes. | REVEALED_NOT_NEW | — | — | 047–072, 137 | OTE | Keep thin. |
| SW-S-0184 | sw.bridget | Coaches; grieves the clumsy prince; enters service; deflects the emperor. | DEVELOPMENT | — | — | 038, 140, 141, 155 | OTE | Keep. |
| SW-S-0185 | sw.ambrose | Knew; ratifies for the country; thanks as a father. | REVEALED_NOT_NEW | — | — | 105–109 | OTE | Keep thin. |
| SW-S-0186 | sw.duke-clockford | Silenced; recalled by Mary; expects to withdraw. | REVEALED_NOT_NEW | — | — | 099, 110–114 | OTE, CRB | U: the revenge reading. |
| SW-S-0187 | sw.yuan-master | Accepts the outcome; plans a treaty; proposes to Bridget. | REVEALED_NOT_NEW | — | — | 130, 131, 155 | OTE | Keep thin. |
| SW-S-0188 | sw.lana, sw.hubert-dee, sw.bernie, sw.bartholomeus, sw.albert, sw.glen, sw.robert, sw.neil, sw.claudia, sw.isabelle, sw.eliane | The helpers and their later lives. | REVEALED_NOT_NEW | — | — | 022–037, 068–070, 151–162 | OTE | Keep thin. |

Records at EXTRA09:

| ID | Key | State before → after | Kind | Process: perception → appraisal/affect → options → act/speech → consequence | Persona/private; recipient; register | Obs. | Class | Rival; uncertainty |
|---|---|---|---|---|---|---|---|---|
| SW-S-0189 | sw.monica | Early Sage: chosen solitude; indifference; readiness to shoot the dragon-cat. | REVEALED_NOT_NEW | — | Few words. | 019, 027, 029, 033 | OTE | Keep. |
| SW-S-0190 | sw.monica | Sage at fifteen; at the hut, wonders whether Bernie will forgive her. | REVEALED_NOT_NEW | — | Private. | 047–049 | OTE, CRB | Keep. |
| SW-S-0191 | sw.monica | Fears a future self who disappoints; hopes to end the mission proudly. | DEVELOPMENT | — | Spoken. | 061, 063 | OTE | Keep. |
| SW-S-0192 | sw.monica | Talks to Hilda at length; asks a personal favour; thanks Lana cleanly; unsettled by her name. | DEVELOPMENT | — | Spoken. | 010, 131, 165, 171 | OTE | Keep. |
| SW-S-0193 | sw.felix | Fan of the Witch; hidden treasures; burn order; "a future that cannot be". | REVEALED_NOT_NEW | — | Private viewpoint. | 123–125, 133–135 | OTE | Keep. |
| SW-S-0194 | sw.felix | Duke of Erin, a week a month as apprentice; bakes; glad to be "Ike". | DEVELOPMENT | — | — | 173, 177 | OTE | Keep. |
| SW-S-0195 | sw.cyril | Hidden chill; treasurer’s checks; mother’s song; secret help; apology. | REVEALED_NOT_NEW | — | Gentle when singing. | 037, 085–088, 100–102, 113 | OTE | Keep. |
| SW-S-0196 | sw.lana | Sees the scars; resolves to protect; makes gifts. | DEVELOPMENT | — | — | 106–108, 120, 142 | OTE | Keep. |
| SW-S-0197 | sw.mary | First prophecy; boys from orphanages; resolve to mourn Clockford. | REVEALED_NOT_NEW | — | Private. | 149–154 | OTE, CRB | U: her foreseen event. |
| SW-S-0198 | sw.louis, sw.lynn, sw.hilda, sw.elliott, sw.isabelle, sw.glen, sw.raul, sw.ray | Smaller states: newly married; the heartbeat; the plan; the bystander no more; the mission; the vow; roses; delight. | REVEALED_NOT_NEW | — | — | 007, 064, 093, 096, 112, 127, 131, 158 | OTE | Keep thin. |

## 2. Directional relationships and obligations — SW-R

Owns A-to-B relationship change; B-to-A is separate even within a shared episode.

Fields: actor; recipient; relation/role; actor's aim; trust/disclosure state before/after; obligation origin/terms; initiative/refusal; dependency/resources/power; concealment or disclosure act; conflict/repair; independent goals; reciprocity assessment; linked knowledge/state IDs.

Attraction, affection, loyalty, duty, dependence and understanding are separate variables. No romance score or assumed mutuality is stored.

Records at V01:

| ID | Actor → recipient | Relation and actor’s aim | Trust and disclosure, before → after | Obligation, power, initiative | Concealment, conflict, repair | Reciprocity; independent goals | Obs. |
|---|---|---|---|---|---|---|---|
| SW-R-0001 | Monica → Louis | Junior Sage; avoid his anger; complete the task. | Fear with trust in his competence → unchanged; goodwill to his family. | Obeys under coercion; reports in writing. | She privately reads his motives correctly. | Asymmetric; her goal is to survive the year. | 009, 011, 094 |
| SW-R-0002 | Louis → Monica | Uses her as an incongruous instrument; wants her confident. | Respect hidden behind insult. | Holds the king’s mandate and the power of choice; feeds her sweets. | Conceals his disciple and his reading of the order. | Asymmetric; his goals include his own pride and the king’s business. | 010, 011, 116, 117, 118, 119 |
| SW-R-0003 | Monica → Nero | Comfort; candour. | Full trust → unchanged. | Dependent for comfort and errands. | Unaware he withholds the kiss. | Mutual in care. | 039, 041 |
| SW-R-0004 | Nero → Monica | Teasing protector; calls her his favourite. | — | Volunteers; vows violence against anyone who breaks her. | Withholds the kiss; hides his own nature from others. | Possessive; own goals undisclosed. | 072, 076, 102 |
| SW-R-0005 | Monica → Isabelle | Grateful, bewildered; defers though older. | Low → grateful acceptance. | Receives protection by staged cruelty. | Worries for Isabelle’s reputation. | Unequal in enthusiasm. | 018, 025, 082 |
| SW-R-0006 | Isabelle → Monica | Adoration; collaborator in the cover. | Knows identity from the start. | Initiates every intervention. | Performs cruelty as care. | Her own enjoyment of the role. | 019, 025, 128 |
| SW-R-0007 | Monica → Lana | First friendship; wants to be liked; plain speech by exit. | Fear → trust; fears losing her over the post. | Initiates a request to be taught. | Does not disclose identity. | Becoming mutual. | 045, 046, 082, 083, 112 |
| SW-R-0008 | Lana → Monica | Brusque care; pride in her braiding. | Scorn → friendship. | Teaches, routes her round crowds, apologizes. | — | Lana has her own outsider wound. | 031, 047, 055, 083 |
| SW-R-0009 | Monica → Felix | Ward to be guarded; fear of proximity and rank. | Thanks him, avoids him. | Cannot refuse his assignments. | Unaware of his tests, kiss and devotion to her other self. | No romantic interest shown. | 048, 075, 085, 113 |
| SW-R-0010 | Felix → Monica | Suspect, pet, game; useful accountant. | Suspicion without fear → keeps her close. | Rank and charm; stakes his office on her. | Tests her; conceals much; kisses her cheek. | Asymmetric; his aims withheld. | 036, 063, 069, 073, 075, 078, 088 |
| SW-R-0011 | Monica → Cyril | Fear of his temper; admiration of his striving. | Fear → admiration. | Accepts his training. | Anonymous treatment and brooch repair. | One-sided care; he does not know. | 089, 101, 114 |
| SW-R-0012 | Cyril → Monica | Hostility for disrespect to Felix → professional recognition. | Distrust → qualified respect; private suspicion. | Supervises, investigates on her behalf. | Nearly checks her hand; interrupted. | Developing; his goal is Felix’s and his family’s approval. | 057, 080, 091, 111, 114 |
| SW-R-0013 | Felix → Cyril | Trusts his fairness; protects him. | — | Assigns him to Monica deliberately. | Hides Wildianu from him. | Partial disclosure only. | 103, 120 |
| SW-R-0014 | Cyril → Felix | Devoted loyalty; seeks recognition. | Total trust. | Defends him with force. | Unaware of Felix’s secrets. | Asymmetric knowledge. | 023, 096 |
| SW-R-0015 | Felix → Elliott | Uses his vigilance. | — | Lies to him about the night. | — | Partial disclosure. | 079 |
| SW-R-0016 | Elliott → Felix | Watchful friend; resents solo risks. | — | Sets traps on his behalf. | — | — | 036, 061 |
| SW-R-0017 | Felix → Duke Clockford | Grandson and dependant. | — | States he cannot defy the duke. | Removes the duke’s placements. | Conflict concealed. | 062, 120 |
| SW-R-0018 | Louis → Felix | Watcher; finds him uncanny. | Distrust. | King’s mandate. | Surveillance brooch disguised as a father’s gift. | Opponents. | 009, 119 |
| SW-R-0019 | Felix → Louis | Believes Louis watches him; resents theft of his prey. | Distrust. | Destroyed the brooch. | Hides his literacy. | Opponents; misattributes the arrest. | 120, 121 |
| SW-R-0020 | Thornley → Monica | Contempt → terror and recognition. | — | Attempted erasure and destruction of her mind. | — | Ended by arrest. | 104, 107 |
| SW-R-0021 | Selma → Aaron | Devotion without return. | — | Committed crimes for him. | — | Not reciprocated. | 064, 065 |
| SW-R-0022 | Lynn → Louis | Service without reverence. | — | Courier and transport. | — | — | 094, 117 |

Records at V02:

| ID | Actor → recipient | Relation and actor’s aim | Trust and disclosure, before → after | Obligation, power, initiative | Concealment, conflict, repair | Reciprocity; independent goals | Obs. |
|---|---|---|---|---|---|---|---|
| SW-R-0023 | Monica → Lana | Friend; wants to be with her. | Fear of shaming her → asks to go with her; treasures her notes. | Monica initiates a request for the first time. | Refusal repaired by Lana’s return. | Mutual; Lana has merchant ambitions. | 003, 008, 058 |
| SW-R-0024 | Lana → Monica | Friend and protector. | Pride-driven help → public claim of friendship. | Daily notes in convalescence. | Hurt at the tea, healed by the coffee. | Mutual. | 029, 031, 032 |
| SW-R-0025 | Monica → Casey | Friend, then rescuer. | Trust → knows of the discarded tea, chooses not to look → accuses → refuses to forget her. | Saves her from execution by bargaining. | Exposure; grief. | Asymmetric. | 027, 073, 090, 095 |
| SW-R-0026 | Casey → Monica | Instrument of access; ambivalent affection. | Cultivated trust → confession → farewell by name. | Uses Monica’s schedule access. | Throws away her tea to rescue her; final apology for promises. | Casey’s aim: kill or win Felix. | 082, 097 |
| SW-R-0027 | Monica → Cyril | Subordinate; growing trust; guilt. | Fear → trust; calls him Cyril. | Refuses to recant for his sake. | Lets him bear blame for the rope. | Asymmetric. | 043, 069, 098 |
| SW-R-0028 | Cyril → Monica | Concealed protector. | Fair judgment → active care disguised as duty. | Does her work; carries her; chocolate. | Apologizes for a fault not his. | Seeks the prince’s approval in parallel. | 026, 046, 059, 098 |
| SW-R-0029 | Elliott → Monica | Contempt cracked by shame and respect. | Distrust → trusts her eye; protects her as a noble. | Orders her to safety. | Cannot apologize for castling. | His code of roles. | 020, 021, 024 |
| SW-R-0030 | Monica → Elliott | Fear; unspoken debt for the idea of duty. | Unchanged outwardly. | — | Fears his anger over chess. | — | 033 |
| SW-R-0031 | Felix → Monica | Taming game, anger at harm, identification with his former self. | Suspicion → guardian presence at her bedside. | Demands she meet expectations. | Exploits her slip; joins the barbecue. | Seeks the Silent Witch, not Monica. | 036, 038, 049, 061 |
| SW-R-0032 | Monica → Felix | Wary duty. | Unchanged; registers his charm as pressure. | Must meet royal expectation. | Hides the attempt on his life. | — | 036, 038 |
| SW-R-0033 | Felix → the Silent Witch | Adoration and search. | From afar → resolved to find her. | — | Keeps her papers locked away. | Personal absorption. | 065, 087, 088 |
| SW-R-0034 | Louis → Monica | Instrumental care; values her cooperation. | Reward and warning. | Concedes on Casey for her sake. | Warns against attachment. | His faction and mission. | 009, 096, 099 |
| SW-R-0035 | Monica → Louis | Fear and trust; bargaining partner. | Trusts his word at once. | Wins a concession. | Asks his faction directly. | — | 095 |
| SW-R-0036 | Isabelle → Monica | Devotion as policy. | Unchanged; private debt explained. | Revenge on Caroline; convalescence room. | Public cruelty as cover. | Repays Kerbeck’s debt. | 052, 055 |
| SW-R-0037 | Claudia → Monica | Coerced friendship; lifesaver refusing thanks. | Jealous watching → claimed friendship. | Saves her life. | Baits her with the Silent Witch. | Devotion to Neil. | 047, 048, 050, 068 |
| SW-R-0038 | Claudia → Neil; Neil → Claudia | Devoted fiancée; dutiful, self-doubting fiancé. | — | Parents’ arrangement. | Height and rank disparity. | — | 048 |
| SW-R-0039 | Monica → Glen; Glen → Monica | Kinship in concealment; cheerful partnership. | Secret kept on both sides. | Dance partners. | Each unknowingly shields the other. | Glen’s master unnamed. | 015, 018 |
| SW-R-0040 | Felix → Glen | Suspicion because of his master. | Watchful. | Uses the dance to observe. | No link found. | — | 040 |
| SW-R-0041 | Bridget → Felix | Probing, unseduced; childhood acquaintance. | Tests his memory. | — | Underwater exchange at tea. | Her own judgment of Monica. | 039 |
| SW-R-0042 | Casey → Felix | Would-be assassin of the duke’s candidate. | — | Father’s order. | Thwarted. | Bright and Randall. | 080, 081 |

Records at V03:

| ID | Actor → recipient | Relation and actor’s aim | Trust and disclosure, before → after | Obligation, power, initiative | Concealment, conflict, repair | Reciprocity; independent goals | Obs. |
|---|---|---|---|---|---|---|---|
| SW-R-0043 | Monica → Bernie | Former friend; wanted his approval. | Longing and fear → renunciation; gratitude for his cover. | She defends Lana first. | Wants to apologize; asks why he protected her. | Asymmetric. | 028, 043, 045, 058 |
| SW-R-0044 | Bernie → Monica | Envious former helper. | Contempt → knows her identity and mission; protects her cover. | Holds her secret. | Demands lifelong gratitude. | His own pride. | 004, 046, 054, 056 |
| SW-R-0045 | Monica → Felix | Guard and, for one night, fellow ghost. | Wariness → gratitude and play; wants nothing from him. | She reaches out first. | Hides her identity and mission; keeps the pendant locked away. | No romantic interest shown. | 100, 107, 119, 120, 126 |
| SW-R-0046 | Felix → Monica | Pet, fellow delinquent, keeper of Ike’s memory. | Suspected assassin → secret-sharer. | Pays for the book; gives the pendant. | Self-exposure at the throat; possessive gift. | Seeks to be remembered. | 087, 107, 118, 119 |
| SW-R-0047 | Felix → the Silent Witch | Admiration he calls first love. | Papers collected; face never seen. | Plans to meet her as king. | — | Absorption in her magic. | 103, 104 |
| SW-R-0048 | Duke Clockford → Felix | Commander and grandfather. | Public warmth; private contempt. | Commands the school; punished the boy through his page (dream). | — | The house’s authority. | 061, 113 |
| SW-R-0049 | Felix → Duke Clockford | Obedient grandson outwardly. | Emptied compliance. | Gathers nobles who resent the duke. | Concealed. | Vow to the name. | 061, 082 |
| SW-R-0050 | Felix → the friend | Mourner and promise-keeper. | — | Pursues the friend’s wish. | — | Unnamed friend, presumed dead. | 101, 109 |
| SW-R-0051 | Monica → Lana | Friend defended. | Trust; credits her with steadiness. | Defends her against Bernie. | Still hides her identity. | Mutual. | 045 |
| SW-R-0052 | Lana → Monica | Friend, armourer, defender. | Guesses without prying. | Dresses and defends her. | — | Mutual. | 032, 044, 049 |
| SW-R-0053 | Elliott → Monica | Suspicious respect; warning. | — | Teaches by warning. | Apologizes in effect. | His code. | 017, 022 |
| SW-R-0054 | Louis → Monica | Instrumental user who judges her heartless. | Unchanged. | Lends Lynn; reports. | Contemptuous verdict to Casey. | Mission. | 029, 131 |
| SW-R-0055 | Mary → Monica | Colleague, user of her computations, tester. | — | Permits a crisis to test her. | Silent when questioned. | The stars’ reading. | 070, 093, 115, 116 |
| SW-R-0056 | Casey → Monica | Former friend at a distance. | Concern. | Sends a package without her name. | Angered by Louis’s verdict. | — | 129, 131 |
| SW-R-0057 | Porter → Monica’s father | Friend. | — | Values his book. | — | — | 106 |
| SW-R-0058 | Yuan → Monica, Felix | Hunter of secrets. | — | Commissions a forged uniform. | — | Imperial mission. | 125 |

Records at V04:

| ID | Actor → recipient | Relation and actor’s aim | Trust and disclosure, before → after | Obligation, power, initiative | Concealment, conflict, repair | Reciprocity; independent goals | Obs. |
|---|---|---|---|---|---|---|---|
| SW-R-0059 | Monica → Cyril | Grateful junior; borrows his “charm”. | Trust → fear for his life. | Testifies for him to his mother. | Does not know the flower’s meaning. | — | 032, 074, 090, 110, 111 |
| SW-R-0060 | Cyril → Monica | Concealed invitation and care. | Unspoken. | Gives flower, help, dance. | Calls it a charm; notices her hand. | Seeks Felix’s approval too. | 028, 032, 108–110 |
| SW-R-0061 | Monica → Felix | Guard who misses Ike. | Keeps his secrets from Louis. | — | Senses obsession. | — | 009, 067, 117 |
| SW-R-0062 | Felix → Monica | Attachment; jealousy; entrusts a wish. | — | Cannot give flowers. | Possessiveness over the pendant. | His own wish overrides. | 081, 114, 116 |
| SW-R-0063 | Monica → Bernie | Formal gratitude. | Friendship ended. | — | — | — | 038 |
| SW-R-0064 | Bernie → Monica | Rival; future ally. | Confession. | Offers help as count. | — | Heirship. | 037, 038 |
| SW-R-0065 | Louis → Monica | Indifference to her humanity; responsibility for the plan. | Withholds the hypothesis. | Takes blame. | — | Faction. | 050, 096, 119, 120 |
| SW-R-0066 | Louis → Glen | Master using an unknowing decoy. | Glen unaware. | Suit, discipline. | — | Mission. | 065, 101 |
| SW-R-0067 | Felix → Glen | Knowing use; praise. | — | Nominates him. | — | Managing Eliane. | 064, 079 |
| SW-R-0068 | Monica ↔ Ray | Fellow recluses. | Secret shared. | Invitation; rescue by curse. | — | Albright honour. | 023, 048, 094, 095 |
| SW-R-0069 | Myra → Cyril | Fearful mother → resolve to welcome. | — | Will write. | Unopened chocolate. | — | 077, 078 |
| SW-R-0070 | Cyril → Myra | Yearly invitations. | Longing. | — | — | — | 075, 076 |
| SW-R-0071 | Eliane → Felix; Eliane → Glen | Entitled pursuit; fury. | — | — | Sabotage. | The duke’s favour. | 054, 056, 063 |
| SW-R-0072 | Bridget → Felix | “My prince”, to be taken back. | — | Watching. | — | Ten-year endurance. | 027, 118 |
| SW-R-0073 | Neil ↔ Claudia | Flower given; dance. | — | Cyril makes time. | — | — | 106 |
| SW-R-0074 | The traitor → 閣下; → Venedict Rain | Dependence; hatred. | — | Puppet curse to complete. | Hiding. | Survival. | 122, 123 |

Records at AFTER04:

| ID | Actor → recipient | Relation and actor’s aim | Trust and disclosure, before → after | Obligation, power, initiative | Concealment, conflict, repair | Reciprocity; independent goals | Obs. |
|---|---|---|---|---|---|---|---|
| SW-R-0075 | Monica → Felix (as Ike) | Fellow delinquent; promises help with the next scheme. | Keeps his secret; uneasy at being his subject. | Initiative from him; she consents. | Lies about Heims-Naria. | — | 044, 063, 144 |
| SW-R-0076 | Felix → Monica | Listener and fellow delinquent; care and teasing. | Shares his love of the Witch’s work. | His initiative. | Source of the birthday unstated. | — | 062, 137, 138, 149 |
| SW-R-0077 | Monica → Lana | Friendship; a gift asked for. | Open. | — | Her planned departure unspoken. | Lana’s birthday planned. | 147, 148 |
| SW-R-0078 | Lana → Monica | A handmade gift chosen with care. | Hides the work until finished. | — | — | — | 146, 147 |
| SW-R-0079 | Monica → Cyril | Admiration; takes his lesson. | — | — | Draws him away from Benjamin. | — | 079; S21:E000604–E000626 |
| SW-R-0080 | Cyril → Glen; Glen → Cyril | Protection; admiration. | Oath before the prince. | Cyril’s authority. | — | Glen’s gifts of smoked meat. | 074, 075, 093, 097 |
| SW-R-0081 | Byron → Cyril; Cyril → Byron | Rivalry and praise; hoped-for friendship. | — | Duel by request. | Byron’s misreading of Sheila. | — | 049, 069, 109, 154 |
| SW-R-0082 | Byron ↔ Sheila | Unspoken attachment on both sides. | Thread and card. | Arranged engagement. | Misunderstanding; corrected on her side. | Graduation dance hoped for. | 155, 156, 158 |
| SW-R-0083 | Elliott ↔ Benjamin | Friendship across rank. | Elliott withholds an event. | — | Against Elliott’s creed. | Benjamin’s music as support. | 111, 112 |
| SW-R-0084 | Elliott → Felix (childhood) | Playmate and teacher. | A secret about tree-climbing. | — | — | Felix’s kindness to him. | 122, 123 |
| SW-R-0085 | Claudia → Felix | Contempt without address. | — | Felix tolerates. | — | — | 055, 057, 061 |
| SW-R-0086 | Isabelle → Monica | Devotion; support as theatre and method. | — | — | — | Birthday quill. | 128, 151 |
| SW-R-0087 | Monica → Hilda; Hilda → Monica | First season’s card; joy. | — | — | — | Solstice visit hoped. | 160, 162 |
| SW-R-0088 | Louis ↔ Rosalie | Devotion; a doctor’s care. | — | — | — | — | 023–028 |
| SW-R-0089 | Louis → Glen | Harsh teaching. | — | Master’s power. | — | — | 099 |

Records at V05:

| ID | Actor → recipient | Relation and actor’s aim | Trust and disclosure, before → after | Obligation, power, initiative | Concealment, conflict, repair | Reciprocity; independent goals | Obs. |
|---|---|---|---|---|---|---|---|
| SW-R-0090 | Felix → the Silent Witch | Admiration, longing; resolved to find her. | Paper shared. | His initiative. | She hides from him. | — | 042, 102, 133, 178 |
| SW-R-0091 | Monica (as the Witch) → Felix | Wants him not to give up; fears exposure; suspects him. | Writes to him; flinches. | — | Mutual concealment. | — | 055, 056, 121, 132 |
| SW-R-0092 | Felix → Nero | Keeps the secret under threat. | Disclosed. | Nero’s threat. | — | — | 107, 127 |
| SW-R-0093 | Nero → Monica | Master by choice; protective fury. | — | Dragon obeys the stronger. | — | — | 105, 124 |
| SW-R-0094 | Monica → Glen; Glen → the Witch | Secret help; wariness to trust. | — | — | Glen does not know. | — | 059, 060 |
| SW-R-0095 | Monica ↔ Ray | Respect; joint secret inquiry. | Partial: father withheld. | — | — | — | 113, 118, 121 |
| SW-R-0096 | Monica ↔ Bartholomeus | Hired helper on a mutual misunderstanding. | — | Employment. | Misreading. | — | 065, 066, 150 |
| SW-R-0097 | Monica ↔ Hilda | Homecoming; protective silence. | Partial. | — | The noble’s name. | — | 164, 167 |
| SW-R-0098 | Cyril ↔ his mother | Reconciliation. | Open. | — | Repaired. | — | 152–155 |
| SW-R-0099 | Felix → Clockford | Performed obedience; private resistance. | — | Clockford’s power. | Concealed. | — | 096, 097, 159 |
| SW-R-0100 | Albert → Felix; Albert → Lionel | Suspicion; affection. | — | — | — | — | 162 |
| SW-R-0101 | Bridget → Felix | Concealed grief. | — | — | — | — | 183 |
| SW-R-0102 | Sams → 閣下; Sams → Venedict | Dependence; guilt and terror. | — | — | — | — | 140, 147 |

Records at V06:

| ID | Actor → recipient | Relation and actor’s aim | Trust and disclosure, before → after | Obligation, power, initiative | Concealment, conflict, repair | Reciprocity; independent goals | Obs. |
|---|---|---|---|---|---|---|---|
| SW-R-0103 | Felix → Monica | Attentive; wants to be relied on; overlays a remembered friend. | — | — | She refuses. | — | 114, 115, 166, 167 |
| SW-R-0104 | Monica → Felix | Fear and suspicion beside attachment to Ike. | — | — | — | — | 026, 066, 113 |
| SW-R-0105 | Monica ↔ Cyril | Respect; need of his ordinary self; protection. | — | — | Her identity hidden. | — | 048, 127, 139, 157 |
| SW-R-0106 | Monica ↔ Raul, Ray | The three youngest Sages. | Partial. | — | — | — | 039, 046, 121 |
| SW-R-0107 | Monica ↔ Lana | A shared future offered; guilt. | — | — | Her departure hidden. | — | 124, 137 |
| SW-R-0108 | Hubert → Monica; Monica → Hubert | A hunter’s fixation; fear turned to anger. | Hubert knows her. | His knowledge. | — | — | 154, 156, 163, 164 |
| SW-R-0109 | Glen → Hubert | Grievance and resolve. | — | — | — | — | 094, 101, 143 |
| SW-R-0110 | Clockford → the Witch; the Witch → Clockford | Recruitment; refusal and anger. | — | His power; her rank. | — | — | 061–065 |
| SW-R-0111 | Albert → Felix; Albert → Glen, Monica | Rivalry; friendship by plan. | — | — | — | — | 107, 108, 117 |
| SW-R-0112 | Isabelle → Monica; Isabelle → Hubert | Guardian; threat. | — | Her family’s power. | — | — | 175, 176 |
| SW-R-0113 | Louis → Emmanuel; Mary → Emmanuel | Enmity; sorrow. | — | — | — | — | 016, 190; S28:E000066 |
| SW-R-0114 | Cyril ↔ the ice spirit | Courtesy; a promised offering. | — | — | — | — | 182, 192 |
| SW-R-0115 | Bartholomeus → Monica | Elder-brotherly care. | — | — | His misreading persists. | — | 207 |
| SW-R-0116 | Robert → Monica | A suit through chess. | — | — | — | — | 098, 099 |

Records at V07:

| ID | Actor → recipient | Relation and actor’s aim | Trust and disclosure, before → after | Obligation, power, initiative | Concealment, conflict, repair | Reciprocity; independent goals | Obs. |
|---|---|---|---|---|---|---|---|
| SW-R-0117 | Monica → Bartholomeus; Bartholomeus → Monica | Reliance; support funded by Mary. | — | — | His misreading persists. | — | 005, 015, 115 |
| SW-R-0118 | Monica ↔ Louis | Mutual concealment; a test. | Partial. | Rank and mission. | Each withholds. | — | 135, 136, 138, 143 |
| SW-R-0119 | Monica → Felix | The wish to know him. | — | — | Unspoken conclusion. | — | 179, 211 |
| SW-R-0120 | Bridget → Felix | Love for the boy; revulsion at the present prince. | — | — | Hidden. | — | 165, 172, 176 |
| SW-R-0121 | Bridget ↔ Monica | Bargain turned partnership. | Partial. | — | Monica withholds. | — | 153, 155, 182, 212 |
| SW-R-0122 | Cyril ↔ Romaria | A gift and a custody. | — | — | — | — | 124, 127 |
| SW-R-0123 | Raul → Cyril, Glen, Monica | Wish for friendship. | — | — | — | — | 033, 131 |
| SW-R-0124 | Emmanuel → Clockford; Emmanuel → Louis | Dependence and fear; envy. | — | Clockford’s power. | The whistle hidden. | — | 057, 058, 147 |
| SW-R-0125 | Felix → Emmanuel | An offer of help. | — | — | Motive withheld. | — | 148, 150 |
| SW-R-0126 | Sezdio → humans; Sezdio → Monica | Hostility; acknowledgement without thanks. | — | — | — | — | 045, 140 |
| SW-R-0127 | Lynn ↔ Carla | Gratitude and care. | — | — | — | — | 117 |
| SW-R-0128 | Mary → Bartholomeus; Mary → an unnamed person | Patronage; a wish to keep someone alive. | — | Leverage over the theft. | — | — | 114, 224, 225 |
| SW-R-0129 | Yuan → his master; the master → the Witch | Service; curiosity. | — | — | — | — | 220–223 |
| SW-R-0130 | The page → young Felix; young Felix → the page | Devotion; attachment, as reported. | — | — | — | — | 163, 205, 217 |

Records at V08:

| ID | Actor → recipient | Relation and actor’s aim | Trust and disclosure, before → after | Obligation, power, initiative | Concealment, conflict, repair | Reciprocity; independent goals | Obs. |
|---|---|---|---|---|---|---|---|
| SW-R-0131 | Monica → Isaac | Wish to save and to know. | — | — | Unnamed feeling. | — | 235, 240, 241 |
| SW-R-0132 | Isaac → Monica | Reverence; cannot harm; glad to be remembered. | — | — | — | — | 175, 202, 261 |
| SW-R-0133 | Isaac ↔ sw.arc | Master, friend, brother; guilt. | — | — | The double hidden. | — | 115, 118, 146 |
| SW-R-0134 | Clockford → Isaac; Isaac → Clockford | Tool and discard; planned assassination. | — | Total. | Each hides. | — | 090, 106, 191, 205 |
| SW-R-0135 | Clockford → sw.arc | Contempt. | — | Total. | — | — | 110, 111, 135, 145 |
| SW-R-0136 | Monica ↔ the emperor | Bargain under threat. | — | — | — | — | 061, 064 |
| SW-R-0137 | Monica ↔ Porter | The bystander and the daughter. | — | — | — | — | 081–085 |
| SW-R-0138 | Monica ↔ Hilda | Trust; the designs given. | — | — | — | — | 264–268 |
| SW-R-0139 | Elliott ↔ Isaac | Loathing; a bystander’s watch. | — | Threat. | — | — | 219–223 |
| SW-R-0140 | Cyril → the false prince; Monica → Cyril | Loyalty to his own choice; respect. | — | — | — | — | 228, 229 |
| SW-R-0141 | Isaac → Emmanuel; Clockford → Emmanuel | Coercion; the trap. | — | — | — | — | 089–094, 190 |
| SW-R-0142 | Louis → Monica; Louis → Lionel | Withholding; loyalty. | — | — | — | — | 187, 188 |
| SW-R-0143 | Wildianu → Irene, sw.arc, Isaac | Love unnamed; service. | — | — | — | — | 280–282 |
| SW-R-0144 | Mary ↔ Clockford; Monica ↔ Casey | Former fiancés; friendship renewed. | — | — | — | — | 249, 294, 296 |

Records at V09:

| ID | Actor → recipient | Relation and actor’s aim | Trust and disclosure, before → after | Obligation, power, initiative | Concealment, conflict, repair | Reciprocity; independent goals | Obs. |
|---|---|---|---|---|---|---|---|
| SW-R-0145 | Monica → Isaac | Friend; master to apprentice. | — | — | — | — | 126, 173 |
| SW-R-0146 | Isaac → Monica | Love; devotion; jealousy. | — | — | Unspoken to her. | — | 128, 143, 179 |
| SW-R-0147 | Monica ↔ Cyril | Senior and junior; joint work. | — | — | — | — | 011, 146, 147, 177 |
| SW-R-0148 | Bridget → Monica and Cyril | Belief that Monica loves Cyril unawares. | — | — | — | — | 040 |
| SW-R-0149 | Monica ↔ Lana | Friendship; neighbours. | — | — | — | — | 010, 151, 162 |
| SW-R-0150 | Monica ↔ Louis | Defeat and respect. | — | — | — | — | 104, 137 |
| SW-R-0151 | The king → Isaac | Knowledge; pardon; thanks. | — | Royal. | — | — | 106, 107 |
| SW-R-0152 | Monica → Clockford | A silent threat. | — | Knowledge. | — | — | 099 |
| SW-R-0153 | Cyril → Isaac | Respect unchanged. | — | — | — | — | 180 |
| SW-R-0154 | Elliott ↔ Isaac | Mutual dislike; help. | — | — | — | — | 027, 139 |
| SW-R-0155 | The emperor → Bridget; Albert → Bridget | Proposal; admiration. | — | — | — | — | 155 |
| SW-R-0156 | Glen ↔ Eliane | Her visit; his obliviousness. | — | — | — | — | 157 |

Records at EXTRA09:

| ID | Actor → recipient | Relation and actor’s aim | Trust and disclosure, before → after | Obligation, power, initiative | Concealment, conflict, repair | Reciprocity; independent goals | Obs. |
|---|---|---|---|---|---|---|---|
| SW-R-0157 | Hilda → Monica | Protection vowed; letting go. | — | — | — | — | 006, 012, 013 |
| SW-R-0158 | Louis → Monica (early) | Exasperation; his own standing; no curiosity. | — | — | — | — | 020, 023 |
| SW-R-0159 | Nero ↔ Monica (early) | Indifference met by insistence; the name learned. | — | — | — | — | 027, 029, 030 |
| SW-R-0160 | Lana → Monica | Protective resolve; gifts made; reunion. | — | — | — | — | 106–108, 120, 169 |
| SW-R-0161 | Cyril ↔ Monica | Apology; unexplained care; first name used. | — | — | — | — | 102, 137, 165 |
| SW-R-0162 | Isaac → Monica | Fan; apprentice; glad to be Ike. | — | — | — | — | 133, 173, 177 |
| SW-R-0163 | Mary → Clockford | Former fiancée; mourning resolved in advance. | — | — | — | — | 151–154 |
| SW-R-0164 | Cyril → Claudia and Neil | Secret help; brother-in-law to be. | — | — | — | — | 113 |

## 3. Chronology and epistemic state — SW-K

Owns proposition-specific participant/reader knowledge and event/revelation order.

Fields: proposition ID/formulation; event and disclosure anchors; order/date certainty; knower/attributing observer; knowledge/belief/suspicion/ignorance status; evidence available to that knower; truth assessment separately; prior/current state; source of change; withheld/false information; continuity conflict.

One character's known proposition cannot be inherited by all participants. Uncertain dates remain uncertain. Event order may be partial; no invented complete calendar is required.

Records at V01:

| ID | Proposition | Anchors | Knower: status | Truth assessment | Change source; withheld information | Obs. |
|---|---|---|---|---|---|---|
| SW-K-0001 | Relative chronology: Worgan dragon in late summer; three months later Louis’s visit; arrival day with Aaron’s trial and the signboard; school day 1 flowerpot and night sighting; day 2 proof, staircase, Selma, appointment, Cyril’s erasure that evening; day 3 badge, Cyril’s crisis, Thornley’s arrest; one week later epilogue and secret episode. Mission term about one year. | S15:E000033; S15:E000169; S15:E000661; S25:E000173 | Reader | Partial order; no calendar dates. | — | 001, 022, 081, 115 |
| SW-K-0002 | Monica Norton is the Silent Witch. | S15:E000351 | Monica, Nero, Louis, Lynn, Isabelle and household: know. Thornley: guessed, in custody. Cyril: suspects. Felix, council, Lana, school: do not know. | True. | Rosalie was not told at her examination. | 107, 111, 122 |
| SW-K-0003 | Monica’s mission is to guard the second prince. | S15:E000578 | Monica, Louis, Lynn, Isabelle, Nero: know. Felix: purpose unknown to him. | True as stated order. | — | 069 |
| SW-K-0004 | Monica is an agent of the king. | S21:E000347 | Felix: considered and rejected as she is too incompetent. | True in substance. | Felix’s model, SW-S-0011. | 069 |
| SW-K-0005 | The order’s real intent is surveillance. | S27:E000253 | Louis: believes. Monica: suspects a hidden purpose. | Unverified; king not shown. | — | 034, 119 |
| SW-K-0006 | Louis has planted a disciple in the academy. | S27:E000069 | Louis, reader: know. Monica: does not. | True per Louis. | Identity withheld. | 116 |
| SW-K-0007 | Felix holds an upper-spirit contract and knows magic. | S21:E000321; S27:E000367 | Felix, Wildianu, Nero, reader: know. Cyril, council, Monica: do not. Louis: senses something. | True. | Concealed even from Cyril. | 069, 102, 121 |
| SW-K-0008 | Felix’s night outing was a decoy operation. | S19:E000526; S21:E001056 | Elliott, Monica: believe. Felix: knows it false. | False. | Purpose withheld. | 079 |
| SW-K-0009 | Felix knew of Aaron’s fraud for a year. | S21:E000994 | Felix, Wildianu, reader. Council: told otherwise. | True. | — | 074, 077 |
| SW-K-0010 | Felix kissed Monica’s cheek. | S21:E000687 | Felix, officers present, Nero, reader: know. Monica: does not. | True. | Nero withholds it. | 073, 076 |
| SW-K-0011 | Thornley organized the embezzlement and erased Aaron’s and Cyril’s memories. | S24:E000556; S24:E000573 | Monica, Louis, Lynn, council, public via press: know of the crimes. Cyril: unaware of his own erasure. | True per culprit’s own dream. | — | 108 |
| SW-K-0012 | Thornley manipulated Selma. | S24:E000282; S27:E000030 | Monica: infers and reports. | Inference; culprit’s account silent. | Instigator of Selma’s phrase unnamed in her section. | 064, 108 |
| SW-K-0013 | Monica arrested Thornley. | S24:E000641; S27:E000340 | Monica, Lynn, Louis: know. Felix, public: credit Louis. | True. | Misattribution arranged by Louis’s leak. | 120 |
| SW-K-0014 | Authorities may investigate rather than defer to rank. | S22:E000902 | Monica: learns from Cyril. | True for Cyril. | — | 091 |
| SW-K-0015 | Monica treated Cyril in the forest. | S23:E000676 | Monica, Nero, Lynn: know. Cyril: remembers a monster. Felix: told it was a tall man. | True. | — | 098, 103 |
| SW-K-0016 | Louis was beaten by Monica in the selection duel. | S27:E000225 | Louis: remembers. Monica: participant who interprets her selection as pity. | True per Louis. | Examiners’ view unstated. | 013, 117 |
| SW-K-0017 | Felix destroyed Louis’s brooch himself. | S27:E000363 | Felix, Wildianu, reader. Louis: does not know the cause. | True. | — | 121 |
| SW-K-0018 | Monica’s father is dead; she was adopted by his pupil. | S18:E000278 | Monica, reader. | True. | Names, cause and the pupil’s identity withheld. | 032, 090 |
| SW-K-0019 | Thornley’s pride was wrecked by Monica’s published formula. | S24:E000518 | Thornley. Monica: unaware. | True per Thornley. | — | 107 |
| SW-K-0020 | Nero is non-human and probably not a spirit. | S24:E000195 | Felix: intuits. Monica: knows Nero’s abilities. | Undetermined. | Nature withheld. | 102 |

Records at V02:

| ID | Proposition | Anchors | Knower: status | Truth assessment | Change source; withheld information | Obs. |
|---|---|---|---|---|---|---|
| SW-K-0021 | Interval of V02. | From about two weeks after enrolment to about six weeks; festival next month. | Reader. | Stated. | S11:E000718; S21:E000232; S22:E000137. | 120 |
| SW-K-0022 | Monica Norton is the Silent Witch. | V02 exit. | Known: Monica, Nero, Louis, Lynn, Isabelle and her maid, Casey (removed). Not known: Felix, Cyril, the school. | True. | Casey learned by act and chant. | 084, 085 |
| SW-K-0023 | An assassination attempt with a 螺炎 failed. | Delivery day. | Known: Monica, Casey, Louis, Lynn, Nero, Felix by overhearing. Not known: Cyril, Elliott, the school. | True. | Concealed by Monica and Louis. | 076, 086, 087 |
| SW-K-0024 | The Silent Witch stopped it. | Same. | Known: as above, including Felix. | True. | Louis overheard. | 087 |
| SW-K-0025 | Casey was the culprit. | Same. | Known: Monica, Louis, Lynn, Nero. Not known: Felix, council, friends. | True. | Withheld from the council. | 080, 095 |
| SW-K-0026 | The timber fell by Cyril’s oversight. | Same. | Believed: Cyril, council. | False. | Monica knows the rope was cut. | 098 |
| SW-K-0027 | Glen is Louis’s disciple. | V02. | Louis; Felix knows Glen’s master’s identity. Not known: Monica, Glen as to decoy role. | Strong inference only. | Name withheld. | 010, 015, 040 |
| SW-K-0028 | Felix was the watcher at Kerbeck. | Three months before V01. | Felix, Wildianu, reader. Not known: Monica. | True. | Felix’s viewpoint. | 064 |
| SW-K-0029 | Felix studies magic and has a spirit. | V01–V02. | Felix, Wildianu, reader; Nero suspects. Not known: Monica, council. | True. | Public denial. | 014, 065, 075 |
| SW-K-0030 | Monica’s father was burned as a heretic; her uncle abused her. | Childhood, before Minerva. | Monica, reader. | Strong inference; memory and delirium. | No date or place. | 034, 044, 045 |
| SW-K-0031 | Caroline poisoned Monica. | Third week of V02 events, approx. | Felix, Cyril, Claudia, Isabelle, teachers; rumour. | True. | Caroline to be expelled. | 044, 052 |
| SW-K-0032 | The duke plans war on Randall as a step to the Empire. | — | Believed by Casey and Count Bright via Randall nobles. | Unverified report. | No scene with the duke. | 081 |
| SW-K-0033 | Claudia was following Monica over Neil. | Week before the poisoning. | Claudia, Monica, reader. | Stated by Claudia. | Whether she also suspects more, unknown. | 048, 050 |
| SW-K-0034 | MacLaggan does or does not recognize Monica. | V02. | Unknown. | Unresolved. | His remark in the secret episode. | 016, 089 |

Records at V03:

| ID | Proposition | Anchors | Knower: status | Truth assessment | Change source; withheld information | Obs. |
|---|---|---|---|---|---|---|
| SW-K-0035 | Monica Norton is the Silent Witch. | V03 exit. | Known: Monica, Nero, Louis, Lynn, Isabelle and her house, Casey, Bernie, Mary. Probable: MacLaggan. Suspicion of something: Yuan. Not known: Felix, Cyril, the council, Lana, Claudia, Glen. | True. | Bernie by test. | 042, 047, 125 |
| SW-K-0036 | Monica secretly guards Felix. | V03 exit. | Known: Louis, Lynn, Nero, Isabelle, Bernie. Not known: Felix, council. | True. | Bernie inferred from her commands. | 054 |
| SW-K-0037 | Felix studies magic, admires the Silent Witch and goes out at night. | Festival night. | Known: Felix, Wildianu; Monica now knows the study, the admiration and the nights. | True. | Felix told her. | 065, 082, 103 |
| SW-K-0038 | The impostor escaped; the body in the cell was the real Pittman. | Day after the festival. | Known: Louis, Lynn; Yuan, Heidi. Monica told in part. | True per Louis and Yuan. | Withheld from the school. | 122, 123, 125 |
| SW-K-0039 | Mary let the tool be stolen. | Festival night. | Mary; Lynn infers. | Not denied. | Mary’s reason withheld. | 116 |
| SW-K-0040 | The maid is the Silent Witch. | Festival night. | Believed by Bartholomeus. | False. | Overheard word. | 124 |
| SW-K-0041 | Porter is Dustin Günther and was Venedict Rain’s friend. | Festival night and morning. | Monica, Porter. | True. | Nero’s book. | 106, 126 |
| SW-K-0042 | Felix suspected Monica of being an assassin. | Festival night. | Felix, Monica. | True as stated. | Felix told her. | 118 |
| SW-K-0043 | Ten-year markers: Felix’s vow; Mary’s unreadable star. Elliott met the child Felix at six. | About ten years before V03. | Respective speakers. | Stated. | Relation unstated. | 018, 065, 070 |
| SW-K-0044 | Casey sent Monica a package. | After the festival. | Casey, Louis. | True. | Contents withheld. | 131 |
| SW-K-0045 | Interval and dates: about two months into the mission; the tournament a week before the festival; the bell festival the next evening; Monica nearly seventeen; her father’s book burned five years ago; the black dragon about half a year ago. | V03. | Reader. | Partial order. | — | 024, 066, 099, 105, 129 |

Records at V04:

| ID | Proposition | Anchors | Knower: status | Truth assessment | Change source; withheld information | Obs. |
|---|---|---|---|---|---|---|
| SW-K-0046 | Monica Norton is the Silent Witch. | V04 exit. | Adds Ray, Yuan, Heidi; Bridget has seen her fly; MacLaggan very probably. | True. | — | 023, 027, 069, 090 |
| SW-K-0047 | Glen is Louis’s disciple and decoy. | Festival day. | Disciple: public. Decoy: Louis, Lynn, Monica. Glen does not know. | True. | — | 065, 068 |
| SW-K-0048 | Yuan’s aims. | Festival evening. | Monica, Lynn, Louis. | Stated by Yuan. | — | 090, 091 |
| SW-K-0049 | Louis’s hypothesis. | Ball night. | Louis. | Withheld. | Kept from Monica. | 120 |
| SW-K-0050 | Ike’s confidences. | — | Monica, Felix. Not Louis. | True. | — | 067 |
| SW-K-0051 | Eliane caused the accidents. | Festival. | Felix (inferred), Eliane, Monica (the attack). | True. | Public: accident. | 061, 079 |
| SW-K-0052 | Myra came. | Festival. | Myra, Highorn, Cyril; Monica unknowingly. | True. | — | 074–078 |
| SW-K-0053 | The traitor and 閣下. | Day after. | The traitor. | Reader knows the words. | Identity withheld. | 122, 123 |
| SW-K-0054 | Casey’s handkerchief. | Festival evening. | Monica, Louis. | True. | — | 097 |
| SW-K-0055 | The flower’s meaning. | Festival. | Cyril, Lana, Felix, Elliott. | Monica does not know. | — | 071, 081, 099 |
| SW-K-0056 | Monica will leave at Felix’s graduation. | — | Monica. | Her plan. | Others assume she stays. | 098, 109 |
| SW-K-0057 | Interval and dates. | Four days before the festival to the ball; prologue from Monica’s tenth year; a year with the uncle. | Reader. | Partial order. | V03 book-date tension. | 001, 004 |

Records at AFTER04:

| ID | Proposition | Anchors | Knower: status | Truth assessment | Change source; withheld information | Obs. |
|---|---|---|---|---|---|---|
| SW-K-0058 | Monica Norton is the Silent Witch. | AFTER04 exit. | As at V04; Istreia senses her power. | Unchanged. | — | 092, 095 |
| SW-K-0059 | Monica keeps Cyril’s rose as a charm. | Case I. | Monica, Nero, Lynn. | True. | Cyril does not know. | 066 |
| SW-K-0060 | The hair charm was a curse; Cecily’s and Wanda’s parts. | Case IV. | Monica, Isabelle, Ray, Cecily. | True. | School and Felix not told. | 139–141 |
| SW-K-0061 | Byron trained in the forbidden garden. | Case III. | Monica, Byron. | True. | Covered by Monica’s lie. | 116, 119 |
| SW-K-0062 | Sheila loves Byron; the blue thread. | Epilogue. | Sheila, Monica. | True. | Byron unaware. | 156 |
| SW-K-0063 | The corsage reserves a dance. | Epilogue. | Sheila, Byron. | True. | Monica does not know. | 159 |
| SW-K-0064 | Elliott’s second turning point. | Before he was ten. | Elliott. | Unknown. | Withheld from Benjamin and the reader. | 112 |
| SW-K-0065 | MacLaggan’s concern about Glen and Minerva. | Case II. | MacLaggan. | Unknown. | Interrupted. | 094 |
| SW-K-0066 | Interval and dates. | Two days after the festival to a winter holiday; retrospective scenes from about a year to about ten years earlier. | Reader. | Partial order. | Heims-Naria date conflict. | 001, 029, 124, 133 |

Records at V05:

| ID | Proposition | Anchors | Knower: status | Truth assessment | Change source; withheld information | Obs. |
|---|---|---|---|---|---|---|
| SW-K-0067 | Nero is the Worgan black dragon. | V05. | Monica, Felix, Nero. | True. | Louis and others unaware. | 106, 111 |
| SW-K-0068 | The Silent Witch belongs to Serendia. | V05. | Felix (inferred), Monica. | True. | The school unaware. | 129 |
| SW-K-0069 | Monica Norton is the Silent Witch. | V05 exit. | As before; Bartholomeus added. | True. | Felix, Glen unaware. | 063, 064 |
| SW-K-0070 | Sams was Barry Oates and is dead. | V05. | Monica, Ray, Bartholomeus. | True. | Household believes he left; Felix believes he fled. | 148, 157 |
| SW-K-0071 | Sams sold Venedict to 閣下; Arthur named. | V05. | Monica, Bartholomeus heard. | Speaker’s claim. | Ray not told of the father. | 147; S27:E000714 |
| SW-K-0072 | A great noble pressed the execution. | Seven years ago. | Hilda; now Monica. | Hilda’s account. | Name withheld. | 166, 167 |
| SW-K-0073 | Felix’s night outing and the black flame. | V05. | Felix, Monica, Nero. | True. | Household unaware. | 109 |
| SW-K-0074 | Felix has a water spirit. | V05. | Felix, Nero, Monica. | True. | Reason unknown. | 131 |
| SW-K-0075 | Hubert Dee is transferring to Serendia. | V05. | Bernie; Monica by letter. | Reported. | — | 181 |
| SW-K-0076 | Bridget’s detective watches Monica. | V05. | Bridget, Dolly. | True. | Monica unaware. | 015, 030 |
| SW-K-0077 | Interval and dates. | A week before the break to New Year’s Day; retrospects. | Reader. | Partial order. | — | 001, 123 |

Records at V06:

| ID | Proposition | Anchors | Knower: status | Truth assessment | Change source; withheld information | Obs. |
|---|---|---|---|---|---|---|
| SW-K-0078 | Monica is the Silent Witch on a mission at Serendia. | V06. | Hubert, who infers a prince is its object. | True. | Felix, Glen, Cyril unaware. | 132, 133 |
| SW-K-0079 | The Silent Witch is at Serendia. | V06. | MacLaggan, silent. | True. | — | 174 |
| SW-K-0080 | Hubert called a small figure the Silent Witch. | The duel. | Cyril heard it. | True. | No conclusion shown. | 152 |
| SW-K-0081 | Monica and Ray suspect Clockford staged the dragon. | New Year. | Raul by eavesdropping. | Suspicion. | Monica believes only she and Ray know. | 038, 060 |
| SW-K-0082 | Clockford’s offer to the Witch. | New Year. | Clockford, Monica. | True. | Felix unaware. | 061, 066 |
| SW-K-0083 | Sams worked for Clockford from about eight years ago. | V06 epilogue. | Monica, Bartholomeus. | Reported. | — | 204, 205 |
| SW-K-0084 | Felix asked Ray about control by curse. | Before New Year. | Ray, Monica. | Ray’s report. | — | 023 |
| SW-K-0085 | Emmanuel holds Galanis. | V06. | Mary, Louis, the Sages, Monica; Felix in part. | True by the secret episode. | Bartholomeus unaware. | 180, 183; S28:E000009 |
| SW-K-0086 | Cyril and Glen were taken by spirits; the school hides it. | The duel’s evening. | Teachers, Felix, Louis, Monica. | True. | Students unaware. | 168; S23:E000276 |
| SW-K-0087 | Felix ordered Hubert’s death. | The duel. | Felix, Wildianu. | True. | Everyone else. | 149 |
| SW-K-0088 | Felix is in Kellylinden. | Next dawn. | Felix, Wildianu. | True. | The Sages. | 197 |
| SW-K-0089 | Interval and dates. | Before the solstice to the morning after the duel. | Reader. | Partial order. | — | 120; S19:E000016 |

Records at V07:

| ID | Proposition | Anchors | Knower: status | Truth assessment | Change source; withheld information | Obs. |
|---|---|---|---|---|---|---|
| SW-K-0090 | Monica is a mage with an injured left hand. | V07. | Bridget. | True. | Bridget does not know she is the Witch. | 146, 152 |
| SW-K-0091 | The Silent Witch’s left hand is cursed. | V07. | Cyril, from Ray. | True. | — | 061, 062 |
| SW-K-0092 | Romaria rests in Cyril’s brooch. | V07. | Cyril, Glen, Monica, Raul, Ray. | True. | Louis and Bradford. | 127 |
| SW-K-0093 | Monica has an undisclosed helper. | V07. | Louis suspects. | True. | Monica unaware of his suspicion. | 135 |
| SW-K-0094 | Felix met Emmanuel and offered help. | V07. | Felix, Emmanuel. | True. | The Sages. | 150 |
| SW-K-0095 | Sams served at Clockford’s house. | About ten years ago to recently. | The gardener; Monica; Bridget. | Reported. | — | 197–199 |
| SW-K-0096 | A fire killed Dr Arthur and Isaac Walker. | About ten years ago. | The gardener; Monica; Bridget. | Reported. | — | 202, 204 |
| SW-K-0097 | Bridget believes Felix false. | V07. | Bridget, Monica, Nero. | Belief. | Others. | 176 |
| SW-K-0098 | Monica’s conclusion about Felix. | V07. | Monica. | Unspoken. | Bridget in part. | 211, 213 |
| SW-K-0099 | Monica addressed Yuan by a notice. | Spring. | Monica; Yuan; his master. | True. | Louis. | 219 |
| SW-K-0100 | Emmanuel possessed; the whistle destroyed. | The forest day. | The Sages present, Mary, Carla. | True. | Clockford. | 103, 110 |
| SW-K-0101 | Interval and dates. | The forest day to early spring. | Reader. | Partial order. | — | 199, 218; S28:E000313 |

Records at V08:

| ID | Proposition | Anchors | Knower: status | Truth assessment | Change source; withheld information | Obs. |
|---|---|---|---|---|---|---|
| SW-K-0102 | The present Felix is Isaac Walker. | About ten years ago onward. | Clockford, Isaac, Elliott, Monica, Nero; Bridget, Cyril, Neil, Claudia by Elliott. | True. | The public. | 097, 216–224 |
| SW-K-0103 | The real prince died by a fall. | About ten years ago. | The same. | True. | The public. | 143, 220 |
| SW-K-0104 | The black chalice is Rain’s design and the motive. | V08. | Monica, Porter, Isaac, Hilda. | Narrated part; motive concluded. | Louis. | 077, 078, 265 |
| SW-K-0105 | Monica’s bargain with the emperor. | V08. | Monica, Nero, the emperor, Yuan, Heidi. | True. | Everyone else. | 064 |
| SW-K-0106 | Monica is the Silent Witch. | V08. | Porter; the council, Albert and Hubert at the close. | True. | The school at large. | 084, 291 |
| SW-K-0107 | Felix planned Clockford’s death. | V08. | Isaac; Clockford by inference. | True. | Others. | 090, 191 |
| SW-K-0108 | Emmanuel was killed and the note forged. | V08. | Clockford. | True. | Louis suspects. | 191, 251 |
| SW-K-0109 | Louis means to denounce Clockford at the garden party. | V08. | Louis, Lynn. | True. | Monica. | 187, 188 |
| SW-K-0110 | The prince’s diary and its last line. | V08. | Monica; Sister Lorna. | True. | Isaac; the reader in part. | 243–247 |
| SW-K-0111 | Wildianu is in Monica’s keeping. | V08. | Monica, Nero, Wildianu. | True. | Isaac does not know it was found. | 277–282 |
| SW-K-0112 | The official story. | V08. | Public. | False within the fiction. | — | 209, 211 |
| SW-K-0113 | Interval and dates. | The assembly to about two weeks before the council. | Reader. | Partial order. | — | 008, 254; S26:E000079 |

Records at V09:

| ID | Proposition | Anchors | Knower: status | Truth assessment | Change source; withheld information | Obs. |
|---|---|---|---|---|---|---|
| SW-K-0114 | The chalice trick used Albert’s blood. | The council. | Monica, Albert, Isaac, the conspirators. | True. | The council. | 116 |
| SW-K-0115 | The king knows Isaac’s identity. | V09. | The king, Isaac, Mary. | True. | Most. | 106 |
| SW-K-0116 | The prince’s death an accident, by the diary. | About ten years ago. | Isaac, Monica, the council members. | Account. | Clockford. | 122–124 |
| SW-K-0117 | Monica knows Clockford’s part. | V09. | Monica, Clockford, Mary. | True. | The public. | 099, 114 |
| SW-K-0118 | Isaac is Monica’s apprentice. | The coda. | Their friends, Cyril. | True. | The public. | 173, 183 |
| SW-K-0119 | Monica is the Silent Witch. | V09. | The school by rumour; the court. | True. | — | 082 |
| SW-K-0120 | Isaac loves Monica. | V09. | Isaac. | His viewpoint. | Monica. | 128 |
| SW-K-0121 | Interval and dates. | The council to a year after graduation. | Reader. | Partial order. | — | 138, 145; S24:E000134 |

Records at EXTRA09:

| ID | Proposition | Anchors | Knower: status | Truth assessment | Change source; withheld information | Obs. |
|---|---|---|---|---|---|---|
| SW-K-0122 | Monica became a Sage at fifteen. | Before V01. | Narration. | True. | — | 047 |
| SW-K-0123 | Hilda’s collaborators plan to relax the regulation of medical magical tools. | The prologue’s winter; to move the next year. | Hilda, the man. | Plan. | Monica. | 007, 008 |
| SW-K-0124 | The fiancé of Mary’s first prophecy is Clockford. | Before the story. | Mary, Bradford. | True by the joined record. | — | 151, 152; V08 obs. 294 |
| SW-K-0125 | Monica’s back is scarred. | V01 to V03 interval. | Lana. | True. | — | 106 |
| SW-K-0126 | Cyril blocked Thornley’s embezzlement for a year. | Two years before the transfer. | Thornley. | True. | Cyril. | 100 |
| SW-K-0127 | Interval and placement. | Before the appointment’s first year to the summer after the move. | Reader. | Partial order. | — | 002, 155, 162, 172 |

## 4. Institutions, world and magic — SW-W

Owns cumulative operational world/institution claims and their exceptions.

Fields: domain; stated rule/doctrine; asserting source position; demonstrated operation; conditions/costs/resources; exception/failure; enforcement versus nominal rule; role/political/material constraint; mathematical or magical reasoning basis; current formulation; competing causal model; linked chronology/claim IDs.

Character explanation, institutional belief, observed mechanism and universal law remain distinguishable. A single successful demonstration does not prove an unlimited rule.

Records at V01:

| ID | Domain | Current formulation | Asserting source | Demonstration; conditions and costs | Exceptions; open points | Locators |
|---|---|---|---|---|---|---|
| SW-W-0001 | Chanting | Humans must chant to shape magical power; formulas are woven by chant. | Narrator rule | Every human caster except Monica chants. | — | S15:E000357–E000358 |
| SW-W-0002 | Shortened chant | Shortened chanting halves the time but still takes seconds. | Narrator | Cyril, S17:E000447–E000448. | — | S15:E000362; S15:E000370 |
| SW-W-0003 | Chantless casting | Monica alone in the world; about eight in ten formulas; one reason she was chosen. | Narrator | Repeated throughout. | Which formulas resist is unstated. | S15:E000363–E000371 |
| SW-W-0004 | Spirits | Spirits need neither chant nor formula; have far more power; upper spirits contracted by about ten mages nationally. | Narrator | Lynn’s barrier and flight; Felix’s lizard. | — | S15:E000358; S15:E000432; S16:E000043 |
| SW-W-0005 | Spirit kinds | Lynn is wind and excels at flight; Wildianu is water and excels at illusion, weak at sensing. | Narrator | Transport; failed spying on Nero. | — | S23:E000197; S24:E000231 |
| SW-W-0006 | Spirit-king summoning | Few in the kingdom can summon a spirit king; Sheffield is the wind spirit king. | Narrator in Isabelle’s view | Prologue wyverns. | — | S12:E000008–E000009 |
| SW-W-0007 | Elements | People have an innate favoured element; many mages use only that one. | Nero’s judgment | Cyril ice-only per Nero; Monica multi-element. | Nero’s claim, not narrator law. | S24:E000027–E000028 |
| SW-W-0008 | Flight | Requires fine control and physical ability; upper-mage level; drains in about half an hour. | Narrator; Nero | Monica cannot fly. | — | S16:E000041; S23:E000194–E000195; S24:E000023–E000025 |
| SW-W-0009 | Mana in the body | Limited capacity; magic-made water carries power; excess causes poisoning; Sages tolerate more; casting consumes energy and mages favour sweets. | Narrator | Monica drinks a little magic water; flags after heavy casting. | — | S19:E000053–E000058; S25:E000049 |
| SW-W-0010 | Over-absorption | Absorption continues past capacity; must vent; five severity grades; early poisoning brings elation, later hallucination; treat by exhausting power; can be cultivated for faster recovery. | Narrator and Monica | Cyril’s crisis and treatment. | — | S23:E000262–E000269; S23:E000395; S23:E000677–E000678; S23:E000745–E000749 |
| SW-W-0011 | Magic tools | Treated gems carry formulas; usable by non-mages; very expensive; a protective formula normally guards the working formula; without it strong attack can cause misfire. | Narrator and Monica | Louis’s brooch; Cyril’s brooch reversed. | — | S15:E000501–E000506; S23:E000696–E000699 |
| SW-W-0012 | Enchantment | Imbuing objects is enchantment; Monica can rewrite a simple tool though not trained in it. | Narrator | Brooch repair. | — | S23:E000724–E000732 |
| SW-W-0013 | Spell interference | Interfering with another’s formula requires far superior skill and is wildly improper. | Narrator | Monica unpicks and reweaves Thornley’s spell. | — | S24:E000460–E000467 |
| SW-W-0014 | Mind interference | Restricted art; permitted for interrogating grave criminals or national emergency with authorization of the mages’ guild or the Seven Sages; side effects memory loss, derangement, unconsciousness; misuse costs the licence; completed form is butterfly-shaped. | Monica; narrator; old grimoires reported | Aaron, Selma, Cyril; Monica’s butterflies. | Whether a Sage may self-authorize is unresolved. | S17:E000562–E000571; S24:E000267–E000268; S24:E000495; S24:E000610 |
| SW-W-0015 | Sight magic | Far-sight and night-sight are not see-through and need line of sight. | Narrator | Night sighting from the attic. | — | S18:E000731 |
| SW-W-0016 | Seven Sages | Apex mages; staff as tall as the bearer; count-equivalent magic-count title; royal advisers; socially prominent. | Narrator; characters | — | — | S12:E000041–E000042; S16:E000221; S25:E000216 |
| SW-W-0017 | Sage selection | Two years ago one vacancy became two through a further illness; interview and attack-only duel; examiners named no ranking. | Monica; Louis | — | Examiners’ view unstated. | S15:E000835; S27:E000204–E000212 |
| SW-W-0018 | Named Sages | Barrier, Silent, Star-reading, Thorn, Cannon, Jewel; the Jewel Mage is a second-prince partisan whom Louis despises. | Characters | — | Seventh unnamed. | S25:E000218; S23:E000713–E000716 |
| SW-W-0019 | Mage institutions | Minerva trains mages; a mages’ guild licenses and disciplines; the magic corps employs upper mages; magic was once a noble monopoly. | Narrator | Thornley handed to the guild. | — | S15:E000159–E000164; S17:E000030–E000032; S27:E000053 |
| SW-W-0020 | Peerage | Duke, marquis, count, viscount, baron; lesser gentry below; dukes are royal kin; titles above count used as styles. | Louis | — | — | S16:E000177; S16:E000206 |
| SW-W-0021 | Succession | Three princes by different mothers; no heir named; second prince’s faction strongest with the duke’s backing. | Monica’s hearsay; Caroline’s belief | — | Character beliefs only. | S15:E000447–E000458; S21:E000403–E000412 |
| SW-W-0022 | Serendia Academy | Royal elite school under the duke; three great schools; donations buy privileges; council appointed by its president and bought through the duke; ledgers mismanaged for decades; dining tasted for poison. | Narrator; characters | Attic, appointments, ledgers. | — | S17:E000017–E000046; S17:E000110; S18:E000246; S24:E000328 |
| SW-W-0023 | Rank as truth | In the school’s practice a higher-ranked accuser decides truth; Cyril’s inquiry is a counterexample. | Monica’s knowledge; Cyril’s act | Staircase case. | Scope of the counterexample. | S20:E000423; S22:E000902 |
| SW-W-0024 | Dragons | Calamities; colour-named kinds superior and black worst; weak points between the eyes and in the eyes; wyverns flock around a greater dragon; Kerbeck guards the east. | Isabelle’s knowledge; Annie; narrator | Prologue. | — | S10:E000015–E000037; S10:E000097–E000156; S15:E000193–E000196 |

Records at V02:

| ID | Domain | Current formulation | Asserting source | Demonstration; conditions and costs | Exceptions; open points | Locators |
|---|---|---|---|---|---|---|
| SW-W-0025 | Measuring power | Crystal scale to 250; bands 1–49, 50–99, 100–129, 130+; 200+ rare; Sages 150+ measured yearly; peaks late teens; colour shows element. | Narrator, MacLaggan | Glen breaks it past 250; Monica last 202. | Fewer than a handful exceed 250; two Sages. | S14:E000235; S14:E000271–E000282; S14:E000331–E000333 |
| SW-W-0026 | Three talents | Quantity of power, understanding of formulas, control of power. | MacLaggan | Glen: control without precision. | — | S14:E000233–E000265 |
| SW-W-0027 | Chantless casting, public account | Instant derivation of the optimal formula. | Plate, MacLaggan, Felix | — | Narrative cause differs, SW-C-0001. | S12:E000004; S14:E000240; S20:E000621–E000626 |
| SW-W-0028 | Ritual chant | Summoning a higher being needs a chant of respect that cannot be omitted. | Narrator | Monica speaks it. | — | S23:E000538–E000545 |
| SW-W-0029 | Remote casting; two spells | Remote origin at a cost in precision; holding two spells is very hard. | Narrator, Monica | Monica does both. | — | S11:E000403; S11:E000503–E000505 |
| SW-W-0030 | Body magic | All magic on human bodies forbidden in Ridill, including healing; stricter than mind interference. | Monica, narrator | — | The Empire allows limited medical magic. | S16:E000324–E000347 |
| SW-W-0031 | The Empire | Largest continental state, east; young emperor; reforms; mages emigrating; merchants waiting. | Narrator, Lana, Neil | — | — | S16:E000339–E000347; S17:E000508–E000512 |
| SW-W-0032 | Randall | Small kingdom between Ridill and the Empire; first prince’s mother’s home; chocolate technology; secret aid to Bright. | Felix, Casey | — | Cross-border aid violates interstate rules. | S21:E000440–E000446; S23:E000170–E000171 |
| SW-W-0033 | Succession and factions | Three princes, three mothers; Lionel said indifferent; Felix’s mother the late second queen; duke wants Eliane for Felix; central versus regional nobles. | Felix, Louis, Elliott, Mary, Monica | — | All reports; king and duke off stage. | S17:E000516; S21:E000443; S23:E000073; S26:E000235; S28:E000232 |
| SW-W-0034 | The east and dragons | Front line; private armies; central fear of revolt; dragon knights slow to poor counties; Kerbeck strongest, neutral. | Cyril, Isabelle, Casey | Kreme earth dragon; Bright’s losses. | — | S20:E000242–E000300; S23:E000156–E000175 |
| SW-W-0035 | Seven Sages | Jade Room for king and Sages; issued robes; Thorn Witch male, of the oldest house, plant enchantment; Star-reading Witch Mary Harvey; Cannon Mage named. | Narrator, Monica, Felix | Rose trap. | — | S18:E000085; S23:E000480–E000487; S28:E000117; S28:E000214–E000224 |
| SW-W-0036 | Academy barrier and security | Louis’s dormant barrier with detection; node in the old-garden fountain; Thorn Witch’s rewrite trap; crest and permit checks; blades banned. | Monica, Lynn, Elliott | Monica rewrites it. | Inside threats not covered. | S17:E000735–E000751; S22:E000284; S23:E000431–E000486 |
| SW-W-0037 | 螺炎 | Fixed brooch-sized assassination device; absorbs ambient power; screw-shaped fire piercing most barriers; short range; stoppable only by its user. | Monica | Smothered without oxygen. | — | S23:E000190–E000211; S25:E000086–E000099 |
| SW-W-0038 | Mind interference in interrogation | Permitted for grave criminals; may leave subjects permanently unconscious. | Louis, narrator | Withdrawn for Casey. | — | S26:E000167–E000171 |
| SW-W-0039 | Academy life | Electives two of twenty-plus; dance and tea classes; cafeteria service billed to fees; fire needs application; festival play of the founding king and seven spirit kings. | Narrator, characters | — | — | S13:E000107; S16:E000056; S17:E000595–E000602; S22:E000029–E000031; S22:E000193–E000202 |
| SW-W-0040 | Reference paratext kept apart | Card statements absent from the narrative. | Character cards | — | Not narrative evidence. | S30:E000004–S33:E000004 |

Records at V03:

| ID | Domain | Current formulation | Asserting source | Demonstration; conditions and costs | Exceptions; open points | Locators |
|---|---|---|---|---|---|---|
| SW-W-0041 | Minerva | Gideon Rutherford’s laboratory produces Sages; MacLaggan taught practical magic; the journal 『ミネルヴァの泉』 appears twice a year, mostly magic research. | Bernie, Monica, narrator | — | — | S11:E000457–E000459; S23:E000151–E000153 |
| SW-W-0042 | Inter-school chess | Serendia, the temple-affiliated academy and Minerva, three a side; Serendia won last year. | Narrator, Redding | Tournament. | — | S15:E000587; S15:E000681 |
| SW-W-0043 | Magic battle | Duel in a barrier that converts damage to mana drain; physical attacks nullified after a past abuse. | Felix | Cyril’s duel. | Past student unnamed. | S13:E000558–E000577 |
| SW-W-0044 | Body magic | Forbidden worldwide except the Empire, Schwargald; dragonization grants scales, strength and speed with a weak brow; face alteration unstable after it. | Bernie, Louis, Yuan | Impostor. | — | S17:E000370–E000409; S26:E000574; S28:E000138–E000147 |
| SW-W-0045 | Seven Sages | Roster complete: Silent, Barrier, Star-reading (eldest), Jewel (Emmanuel Darwin), Thorn (Raul), Cannon (Bradford), Abyss Curse (Ray). | Mary, Felix | — | Revises SW-W-0018’s unnamed seventh. | S19:E000131; S21:E000450 |
| SW-W-0046 | Ancient tools | From an age of magic as mystery; unanalysable; wilful; irreparable; mostly national treasures. 〈星紡ぎのミラ〉 draws land mana, converts it to attack, manipulates low-resistance holders, kills male owners; sealed by a first-class barrier. | Louis, Mary, narrator | The theft and flight. | Sages resist its control. | S19:E000396–E000432; S20:E000026–E000037; S25:E000403 |
| SW-W-0047 | Magic offering | Mana release returns gathered land mana to the sky; excess mana draws spirits and dragons and harms people. | Mary, narrator | Offering seen. | — | S19:E000171–E000180; S23:E000448–E000452 |
| SW-W-0048 | Bell-ringing festival | Harvest thanks to the earth spirit king turned mourning for the dead loosed by the truant gatekeeper; animal costumes; bells; split pastry. | Isabelle, narrator | Coalrapton. | — | S18:E000438–E000475; S22:E000030; S23:E000459 |
| SW-W-0049 | Detection and flight | Detection is a speciality whose reading takes experience; flight is mana-hungry; flying limits Monica to one further spell. | Narrator | Monica. | — | S21:E000687–E000703; S22:E000487; S22:E000586 |
| SW-W-0050 | Mind interference | Quasi-forbidden, permitted only in specified situations; effective on a tool with a human will. | Narrator, Lynn | Dream on the tool. | Mary’s tolerance asserted by Lynn. | S22:E000579–E000583; S22:E000625–E000627 |
| SW-W-0051 | Spirit contract | Requires the contractor’s innate element to match the spirit’s. | The page in Felix’s dream | — | Dream source. | S25:E000247 |
| SW-W-0052 | Randall and the Empire | The 螺炎’s ruby came from the imperial Glocken mine, rarely exported; Louis fears an Empire–Randall alliance and war. | Louis | — | Hypothesis. | S28:E000112–E000154 |
| SW-W-0053 | Coalrapton night town | Brothels and stalls; nobles meet there; Porter’s shop of academic and rare books. | Narrator | Festival night. | — | S21:E000115–E000197; S23:E000106–E000121; S23:E000280 |
| SW-W-0054 | Convent refuge | Richerwood, in the northern mountains, shelters women with circumstances. | Narrator | Casey. | — | S28:E000024–E000025 |

Records at V04:

| ID | Domain | Current formulation | Asserting source | Demonstration; conditions and costs | Exceptions; open points | Locators |
|---|---|---|---|---|---|---|
| SW-W-0055 | Curse-casting | Only the Albright house; distinct from magic; inherited curses; absorption of curse tools; pain-reproducing curses magic cannot undo. | Narrator, Ray | Ray’s acts. | Traitor outside. | S14:E000394–E000407; S16:E000828–E000860; S23:E000336–E000337 |
| SW-W-0056 | Curse tools | Made to make someone suffer; 〈真紅の憤怒〉 steals composure; fragments persist briefly. | Narrator | Eliane. | — | S14:E000504–E000572; S18:E000639 |
| SW-W-0057 | Royal balance | The crown retained the Rosebarg magic house and the Albright curse house to balance regional nobles and the guild. | Conrad | — | — | S13:E000371 |
| SW-W-0058 | Medical magic | The mages’ guild seeks legalization; mediators judge it premature. | Baron Maywood, Highorn | — | — | S13:E000654–E000674 |
| SW-W-0059 | Imperial body magic | Research legalized about a year ago; Yuan’s skill implies longer work; dragon forms weak to cold. | Monica | Yuan. | State or private, unknown. | S20:E000351–E000353; S22:E000052–E000053 |
| SW-W-0060 | Spell absorption | A matching mana sequence absorbs a cast spell; Kalgodias sequence of the Duran faction. | Monica | Web. | — | S20:E000477–E000479 |
| SW-W-0061 | Festival institutions | Diplomacy; play; flowers as dance reservations in the giver’s colours; ball by the duke’s invitation. | Characters, narrator | — | — | S13:E001040–E001042; S15:E000030–E000032; S28:E000017 |
| SW-W-0062 | Founding myth | Ralph and Amelia; seven tribes; the dark dragon; Ralph’s constellation made by the dark spirit king. | Narrator, Felix | — | — | S17:E000192; S26:E000322 |
| SW-W-0063 | Houses | Maywood mediators; Ashley 〈識者の家系〉; magic-talented adopted heirs once common. | Felix, Claudia, Benjamin | — | — | S13:E000541–E000547; S19:E000085–E000086 |
| SW-W-0064 | Royal Magic Research Institute | Employer of Hilda. | Narrator | — | — | S11:E000184 |
| SW-W-0065 | Magic ice | Mana-bearing, inedible, usable for chilling. | Narrator | Monica. | — | S25:E000051–E000052 |
| SW-W-0066 | Spirit contracts | Contractor and spirit sense a call at a distance. | Narrator | Lynn. | — | S14:E000189–E000193 |

Records at AFTER04:

| ID | Domain | Current formulation | Asserting source | Demonstration; conditions and costs | Exceptions; open points | Locators |
|---|---|---|---|---|---|---|
| SW-W-0067 | Grimoires | Magic tools read aloud; sealed when unused; torn pages risk runaway. | Narrator | Sealing work; torn page sealed by MacLaggan. | Older tools largely replaced. | S12:E000255–E000269; S24:E000155–E000160 |
| SW-W-0068 | Rosebarg house | First Thorn Witch’s plant grimoire; the Rosebarg head always a Sage; fifth Thorn Witch now. | Narrator | Vine pit. | — | S12:E000670–E000691 |
| SW-W-0069 | Curses and charms | Dream-intrusion curse with one’s own hair; needs mana paper and training; a curse ritual involving royalty is capital. | Ray; Monica | Case IV. | Charm inverted onto the user. | S24:E000887–E000914 |
| SW-W-0070 | Spirits | Three ranks; mid-level spirits animal-formed and limited away from contractors; eye colour fixed; drawn to mana masses and high-mana land. | Narrator; Istreia | Bait with a heating tool. | — | S18:E000972–E000974; S18:E001075; S18:E001166–E001175 |
| SW-W-0071 | School and tools | Heating tool from Amberd; upper-floor water; magic-battle barrier needs land, tools and two mages. | Narrator | Case II. | Rare; costly. | S18:E000041–E000049; S18:E000421–E000424 |
| SW-W-0072 | Shelgria | Calendar month named for an ice spirit; season’s cards to family and lovers. | Narrator | Cards bought and sent. | — | S21:E000501–E000511 |
| SW-W-0073 | Charms in fashion | Dew; blue ink; hair under the pillow; popular astrology by Mary Harvey. | Louis; students | Cases I, III, IV. | Mood, by Louis’s account. | S12:E000424–E000437; S21:E000164–E000176 |
| SW-W-0074 | High-mana land | Old dormitory abandoned; mana poisoning; faster recovery tempts trainees. | Narrator; Monica | Byron’s training. | — | S15:E000589–E000598; S21:E001163–E001175 |

Records at V05:

| ID | Domain | Current formulation | Asserting source | Demonstration; conditions and costs | Exceptions; open points | Locators |
|---|---|---|---|---|---|---|
| SW-W-0075 | Dragons | Ranks; upper dragons speak the spirits’ tongue; cursed dragons the worst disaster; adult dragons resist human curses. | Narrator; Nero; Ray | Leinbourg. | Willing acceptance without precedent. | S17:E000183–E000231; S24:E000472–E000489 |
| SW-W-0076 | Black dragon and black flame | Black flame burns curses and barriers; forbidden with necromancy and weather control; only in true form. | Narrator; Nero | Image-set prose. | — | S25:E000306–E000325 |
| SW-W-0077 | Curse-craft | Leaves residue; ages its user; Albright monopoly. | Ray | Sams. | — | S24:E000214–E000231; S26:E000389–E000397 |
| SW-W-0078 | Spirit contracts and affinity | Rare upper-spirit contracts; affinity inherited and fixed; middle names honour spirit kings. | Monica | Felix’s spirit. | Felix’s case unexplained. | S25:E000494–E000514 |
| SW-W-0079 | Mana | Typical about 100; Sage 150; Monica just over 200; four above 250. | Narrator; Ray | Glen. | Unofficial record. | S24:E000285–E000294 |
| SW-W-0080 | Court and Sages | New Year week; magic offerings; factions court neutral Sages; a Sage’s magic-count rank. | Narrator | Prologue; epilogue. | — | S11:E000011–E000077; S27:E000624; S28:E000018–E000024 |
| SW-W-0081 | Politics | Falfolia’s lines; the garrison; the king ill; factions realigned. | Felix | Talks. | Felix’s inferences. | S17:E000013–E000065; S27:E000254–E000260 |
| SW-W-0082 | Seasonal customs | Solstice wreaths; the Ortelia chime; ten-day solstice break. | Narrator | Market; offering. | — | S13:E000018–E000061; S13:E000356–E000375 |

Records at V06:

| ID | Domain | Current formulation | Asserting source | Demonstration; conditions and costs | Exceptions; open points | Locators |
|---|---|---|---|---|---|---|
| SW-W-0083 | The Seven Sages | Seniority; factions; a rank like high nobility; the assembly’s ambitions; a proposed head of Sages. | Narrator; Louis; Clockford | Offering; banquet. | — | S13:E000051; S13:E000088; S14:E000377; S14:E000613; S23:E000040 |
| SW-W-0084 | The royal family | Ambrose; Wilma; Phyllis; Irene dead; Lionel; Albert. | Narrator | Ceremony. | — | S14:E000011–E000043 |
| SW-W-0085 | Ancient tools | Six held; one with Mary; Galanis lost; speaking; brings war. | Louis | Kellylinden. | — | S24:E000084–E000088; S24:E000149–E000153 |
| SW-W-0086 | Spirits | Dense land or contract; decline; offerings; eye colour; a forgotten name. | Narrator; spirits | Cave; forest. | — | S25:E000271–E000273; S25:E000318; S23:E000428; S24:E000334; S24:E000432 |
| SW-W-0087 | Magic battle and casting | Barrier rules; tools allowed; two spells; short chant; homing; remote casting; Magic Corps criteria. | Narrator | Duel. | Carla holds more than two. | S19:E000277–E000278; S20:E000188; S17:E000071–E000074; S19:E000478; S28:E000113 |
| SW-W-0088 | Magic tools | Enchantment limits; spirit-powered armour; ring tools; signed work. | Narrator; Bartholomeus | Forest; duel. | — | S23:E000485; S25:E000096–E000105; S20:E000297 |
| SW-W-0089 | Old houses | Roseburg plant magic and legend; Albright ethics. | Narrator; Ray | Garden; forest. | — | S13:E000406; S13:E000876–E000877; S14:E000122 |
| SW-W-0090 | Mana-dense lands | Off-limits; harmful; surveyed by a learned society. | Louis; Carla | Kellylinden. | — | S23:E000327–E000330; S22:E000252 |
| SW-W-0091 | Politics and trade | The young emperor’s tariffs; Southerndoor; garrison disputes. | Lana; Claudia; Eliane | School. | — | S18:E000122–E000128; S16:E000334 |

Records at V07:

| ID | Domain | Current formulation | Asserting source | Demonstration; conditions and costs | Exceptions; open points | Locators |
|---|---|---|---|---|---|---|
| SW-W-0092 | Ancient tools | Galanis’s wars; possession; Bern’s Mirror; Mira’s drawing and spreading of mana. | Louis; narrator | Forest. | — | obs. 071, 073, 074, 109 |
| SW-W-0093 | Reflection barriers | Five grades; humans reach the second; a first-class tool. | Narrator | Forest. | — | obs. 085, 090 |
| SW-W-0094 | Spirits | Offerings; forgetting; sensing by the mana-rich; spirit-god faith; contracts. | Sezdio; Ray; narrator | Forest. | — | obs. 041, 044, 046, 070 |
| SW-W-0095 | The Roseburgs | Rose fortress; cruel persona; grandmothers rule; a feared sister. | Narrator | Forest; Clockford’s house. | — | obs. 023, 036, 037, 209 |
| SW-W-0096 | Casting | Fixed and temporary seals; formula splitting; spirit-king power. | Narrator | Forest. | — | obs. 016, 053, 094 |
| SW-W-0097 | The Empire | The war fifty years ago; body manipulation legal recently; Yuan’s master. | Narrator | — | — | obs. 073, 192, 221 |
| SW-W-0098 | Clockford’s household | Gardener; the fire; Marcy; the collection; Sages for display. | Gardener; narrator | Clockford’s house. | — | obs. 202, 203, 208 |
| SW-W-0099 | Calendar | Widdle; Sheffield’s holiday and a week’s closure. | Narrator | School. | — | S28:E000364; S25:E000210–E000211 |

Records at V08:

| ID | Domain | Current formulation | Asserting source | Demonstration; conditions and costs | Exceptions; open points | Locators |
|---|---|---|---|---|---|---|
| SW-W-0100 | Body manipulation | Once on another; mana poisoning; banned in the Empire until the present emperor; scars made and erased. | Yuan; narrator | — | — | obs. 038, 045, 150, 152 |
| SW-W-0101 | Potions law | Temporary and fixed infusion; Ridill’s limit; the Roseburg exception; church enmity. | Narrator | — | — | obs. 021–023 |
| SW-W-0102 | The Empire | A young emperor; coups; spirits in his service; southern peoples subdued. | The emperor | — | — | obs. 053, 054, 065 |
| SW-W-0103 | War and mages | Mages as weapons; mana pollution; the war about fifty years ago and the old duke’s peace. | The emperor; narrator | — | — | obs. 058, 294 |
| SW-W-0104 | Upper-spirit contracts | About 150 mana; the stone; affinity bars contract; a spirit immobile without mana. | Narrator | — | — | obs. 130, 164, 262, 279 |
| SW-W-0105 | Succession and factions | Albert as reserve; Phyllis; covetous nobles; the Supreme Council. | Narrator | — | — | obs. 093, 207, 254, 284 |
| SW-W-0106 | Heredity and the chalice | Affinity inherited; the tool reads hereditary information from mana in blood. | Monica; narrator | — | — | obs. 077, 266 |
| SW-W-0107 | The prison tower | Royal and noble prisoners; anti-magic bracelet; spirit-repelling barrier. | Narrator | Castle | — | obs. 256, 263 |

Records at V09:

| ID | Domain | Current formulation | Asserting source | Demonstration; conditions and costs | Exceptions; open points | Locators |
|---|---|---|---|---|---|---|
| SW-W-0108 | The black chalice | A real tool proving kinship by colour; under analysis. | Narrator | — | — | obs. 030–033, 088, 131 |
| SW-W-0109 | Magic-battle rules | Mana drain; barrier strikes, trips and chokes pass; two keepers. | Narrator | — | — | obs. 036, 050, 060, 065 |
| SW-W-0110 | Louis’s techniques | The Mirror Prison; barrier fighting. | Narrator | — | — | obs. 059, 063 |
| SW-W-0111 | Curse and plant magic | Insect-attracting curses; mana-drinking flowers. | Narrator | — | — | obs. 071 |
| SW-W-0112 | The Supreme Council | King, nobles, Sages; verdict by royal word. | Narrator | Castle | — | obs. 073–098 |
| SW-W-0113 | Succession | Renunciation; Lionel to be named; Clockford to withdraw. | Narrator | — | — | obs. 112, 132 |
| SW-W-0114 | Southerndoor and trade | Port; Alpatra; the Flax Company; mana-infused cloth. | Narrator | Southerndoor | — | obs. 151, 161 |
| SW-W-0115 | The Sages | A seat unfilled; Raul’s planned study abroad. | Narrator | — | — | obs. 135, 136, 178 |

Records at EXTRA09:

| ID | Domain | Current formulation | Asserting source | Demonstration; conditions and costs | Exceptions; open points | Locators |
|---|---|---|---|---|---|---|
| SW-W-0116 | Contract stones | A spirit may sleep in its stone after its master’s death and weakens without a contract. | Narrator | Serendia | — | obs. 060 |
| SW-W-0117 | Spirit possession | A spirit may enter an animal and alter it. | Narrator | — | — | obs. 081 |
| SW-W-0118 | Spirit offerings | Wind spirits take music; their song works like an incantation. | Narrator | — | — | obs. 080 |
| SW-W-0119 | Medical regulation | The physicians’ association and the Mage Guild move to relax the regulation of medical tools. | Narrator | Capital | — | obs. 008 |
| SW-W-0120 | Plant enchantment | Edible parts store mana; peas absorb it. | Narrator | Highorn | — | obs. 162, 163 |
| SW-W-0121 | Ancient tools | 〈星紡ぎのミラ〉 is kept by women only. | Narrator | — | — | obs. 092 |

## 5. Load-bearing claims and revision history — SW-C / SW-CR

SW-C owns the current bounded formulation and its retrieval route. Fields: claim ID; question/domain; formulation; source/knowledge range; class; support; counterevidence; alternatives; confidence and reason; current transition/state; discriminating observation; dependent artifacts/IDs; revision references.

SW-CR owns append-only change events. Fields: revision ID; claim ID; earlier formulation and boundary; transition; new formulation and boundary; new support/counterevidence; reason; affected homes; correction versus later reinterpretation; date/reviewer. Allowed transitions:

| Transition | Meaning |
|---|---|
| PRESERVE | Material formulation retained after review. |
| STRENGTHEN | Same formulation receives stronger independent support. |
| REVISE | Wording, scope or mechanism materially changes. |
| DOWNGRADE | Confidence or warranted scope decreases. |
| REJECT | Claim is contradicted sufficiently to cease being accepted. |
| OPEN | Discriminating evidence remains insufficient or conflicting. |

An initial claim has no invented predecessor. It may begin OPEN or another justified initial assessment; a revision event requires an actual previous formulation. Preserve rejected claims for provenance rather than deleting their IDs. Normative criteria are explicit and separate from evidence confidence.

Claim records. Rows SW-C-0001 to SW-C-0018 were registered at V01, rows SW-C-0019 to SW-C-0026 at V02, rows SW-C-0027 to SW-C-0034 at V03, and rows SW-C-0035 onward at V04. Every row shows the current formulation after V04 review; earlier wording is preserved in the revision records below.

| ID | Question | Formulation | Range; class | Support | Counterevidence; alternatives | State; confidence | Discriminating observation | Dependents |
|---|---|---|---|---|---|---|---|---|
| SW-C-0001 | Origin of the silence | Chantless casting began as avoidance of speech, and silence and mastery are one mechanism; the avoidance has an earlier root in childhood punishment for speaking; before Minerva a year of abuse produced a dissociation in which she lost language, ended by Hilda Everett’s rescue; its occasion at Minerva was a friend’s plan to shorten her chant; the public account explains the capacity as instant computation. | V01–V04; NP, SI | V01 obs. 007, 033; V02 obs. 011, 016, 045; V03 obs. 003, 005–007; V04 obs. 004, 006–008 | Capacity may exceed any cause; the public account is not false. | REVISE at V02 (SW-CR-0001); high. V03: REVISE (SW-CR-0019). V04: REVISE (SW-CR-0045). AFTER04: STRENGTHEN (SW-CR-0079). V05: STRENGTHEN (SW-CR-0119). V06: STRENGTHEN (SW-CR-0163). V07: PRESERVE (SW-CR-0213). V08: PRESERVE (SW-CR-0269). V09: PRESERVE (SW-CR-0331). EXTRA09: STRENGTHEN (SW-CR-0399). | Monica’s own account of how she learned it. | SW-S-0002; SW-S-0026 |
| SW-C-0002 | Fear response | Pain, fear or exposure drive Monica into numerical absorption; the habit began as a child’s escape from her uncle into her father’s formulas and a vow to keep his numbers; she uses it to compute combat and to bear people, it fails when people she knows are threatened, and she now turns it outward as evidence, naming it no longer a refuge. | V01–V04; NP | V01 obs. 014, 037, 071, 072, 085; V02 obs. 004, 038, 044; V03 obs. 076, 096, 130; V04 obs. 003–005, 085, 090, 096 | Habit rather than defence. | STRENGTHEN at V02 (SW-CR-0002); high. V03: STRENGTHEN and REVISE (SW-CR-0020). V04: REVISE (SW-CR-0046). AFTER04: PRESERVE (SW-CR-0080). V05: REVISE (SW-CR-0120). V06: STRENGTHEN (SW-CR-0164). V07: STRENGTHEN (SW-CR-0214). V08: PRESERVE (SW-CR-0270). V09: PRESERVE (SW-CR-0332). EXTRA09: STRENGTHEN (SW-CR-0400). | Fear without absorption. | SW-S-0003; SW-F-0006 |
| SW-C-0003 | Past harm | Monica’s paternal uncle, after her father’s execution when she was ten, beat and starved her, shut her in a winter barn and forbade her to defend her father, for about a year until Hilda Everett took her; scars remain and touch still frightens her. | V01–V04; CRB under drug, SI | V01 obs. 037, 040, 057–059; V02 obs. 045; V03 obs. 106, 117, 121; V04 obs. 001–004 | Drug distortion; V02 reading section 8.1. | REVISE at V02 (SW-CR-0003): identity resolved; duration and end OPEN. V03: STRENGTHEN (SW-CR-0021). V04: REVISE (SW-CR-0047). AFTER04: PRESERVE (SW-CR-0081). V05: PRESERVE (SW-CR-0121). V06: PRESERVE (SW-CR-0165). V07: PRESERVE (SW-CR-0215). V08: PRESERVE (SW-CR-0271). V09: PRESERVE (SW-CR-0333). EXTRA09: PRESERVE (SW-CR-0401). | Sober account or third-party report. | SW-S-0004; SW-S-0026; SW-P-0005 |
| SW-C-0004 | Selection | The makeweight self-assessment is contradicted by Louis’s memory of the duel; the examiners’ ranking is unstated. | V01–V04; CRB | obs. 013, 117; V03 obs. 023 | Louis’s memory may be self-serving. | OPEN on examiners; high that her belief lacks support. Reviewed at V02: PRESERVE (SW-CR-0004). V03: PRESERVE (SW-CR-0022). V04: PRESERVE (SW-CR-0048). AFTER04: PRESERVE (SW-CR-0082). V05: STRENGTHEN (SW-CR-0122). V06: PRESERVE (SW-CR-0166). V07: PRESERVE (SW-CR-0216). V08: PRESERVE (SW-CR-0272). V09: PRESERVE (SW-CR-0334). EXTRA09: PRESERVE (SW-CR-0402). | Any examiner’s statement. | SW-S-0008; SW-K-0016 |
| SW-C-0005 | Mission purpose | Stated protection; Monica doubts it; Louis reads surveillance, uses a decoy, chose Monica because she distrusts, fears and hates people and can therefore be merciless, and calls himself first-prince because he dislikes the duke and Felix; the king is unshown. | V01–V04; CRB | V01 obs. 034, 119; V02 obs. 010, 096; V03 obs. 131; V04 obs. 120 | Protection and surveillance may coexist. | STRENGTHEN and partly REVISE at V02 (SW-CR-0005); king’s intent OPEN. V03: STRENGTHEN (SW-CR-0023). V04: STRENGTHEN (SW-CR-0049). AFTER04: PRESERVE (SW-CR-0083). V05: STRENGTHEN (SW-CR-0123). V06: STRENGTHEN (SW-CR-0167). V07: PRESERVE (SW-CR-0217). V08: PRESERVE (SW-CR-0273). V09: STRENGTHEN (SW-CR-0335). EXTRA09: PRESERVE (SW-CR-0403). | King or royal agent on stage. | SW-K-0005; SW-P-0007 |
| SW-C-0006 | The watcher | The prologue’s watcher is Felix. | V01–V04; OTE | V01 obs. 003, 024, 122; V02 obs. 064, 088 | — | STRENGTHEN to OTE at V02 (SW-CR-0006). V03: PRESERVE (SW-CR-0024). V04: PRESERVE (SW-CR-0050). AFTER04: PRESERVE (SW-CR-0084). V05: PRESERVE (SW-CR-0124). V06: PRESERVE (SW-CR-0168). V07: PRESERVE (SW-CR-0218). V08: STRENGTHEN (SW-CR-0274). V09: PRESERVE (SW-CR-0336). EXTRA09: PRESERVE (SW-CR-0404). | — | SW-S-0012; SW-S-0034 |
| SW-C-0007 | Felix’s divergence | Public and private selves diverge: he denies a talent for magic while studying it in secret because it is forbidden to him, and hides a spirit; he obeys the duke outwardly while removing his placements and gathering nobles who resent him; he must become king without wanting it, under a ten-year vow to make the name Felix Arc Ridill remembered, which he now expresses as a hero’s posthumous light and pursues even against his dead friend’s wish. | V01–V04; OTE, SI | V01 obs. 020, 062, 077, 078, 120; V02 obs. 014, 062, 065, 077; V03 obs. 061, 065, 082, 101, 103; V04 obs. 030, 064, 116, 117 | Prudence rather than resistance. | STRENGTHEN at V02 (SW-CR-0007); motive OPEN. V03: STRENGTHEN and partly REVISE (SW-CR-0025). V04: STRENGTHEN (SW-CR-0051). AFTER04: STRENGTHEN (SW-CR-0085). V05: STRENGTHEN (SW-CR-0125). V06: STRENGTHEN (SW-CR-0169). V07: STRENGTHEN (SW-CR-0219). V08: STRENGTHEN (SW-CR-0275). V09: PRESERVE (SW-CR-0337). EXTRA09: PRESERVE (SW-CR-0405). | Felix’s wish disclosed. | SW-S-0009; SW-S-0010; SW-S-0035; SW-C-0022 |
| SW-C-0008 | Recognition by Felix | Felix did not identify Monica as the Silent Witch from V01 to V08, though he admired the Witch and grew close to Monica; at V09 he recognizes her when she enters the Supreme Council, and calls himself a fool for not seeing it. | V01–V04 exit; OTE | V01 obs. 069, 122; V02 obs. 087; V03 obs. 104, 118; V04 obs. 081 | — | STRENGTHEN at V02 (SW-CR-0008). V03: STRENGTHEN (SW-CR-0026). V04: STRENGTHEN (SW-CR-0052). AFTER04: PRESERVE (SW-CR-0086). V05: STRENGTHEN (SW-CR-0126). V06: STRENGTHEN (SW-CR-0170). V07: STRENGTHEN (SW-CR-0220). V08: REVISE (SW-CR-0276). V09: REVISE (SW-CR-0338). EXTRA09: PRESERVE (SW-CR-0406). | Felix witnessing her magic. | SW-P-0003; SW-P-0014 |
| SW-C-0009 | Recognition by Cyril | Cyril held an unverified suspicion from V01 to V08; when Monica reveals herself at V09 he says he had half guessed from her hand and the hooded figure, kneels to apologize, and returns to scolding her as his junior. | V01–V04 exit; SI, CRB | V01 obs. 111; V02 obs. 054; V04 obs. 108 | Idle curiosity. | REVISE at V02 (SW-CR-0009). V03: PRESERVE; UNTESTED (SW-CR-0027). V04: REVISE (SW-CR-0053). AFTER04: PRESERVE (SW-CR-0087). V05: PRESERVE (SW-CR-0127). V06: REVISE (SW-CR-0171). V07: REVISE (SW-CR-0221). V08: REVISE (SW-CR-0277). V09: REVISE (SW-CR-0339). EXTRA09: PRESERVE (SW-CR-0407). | Cyril acting on either link. | SW-P-0004; SW-S-0038 |
| SW-C-0010 | Form of power | Awe at Monica’s power is narrated through external focalizers; from V02 her own viewpoint also narrates her power, as calculation under constraint; V03 extends this to sustained combat computation and gives her first chantless casting from a rival’s view. | V01–V04; SI | V01 obs. 002, 056, 098, 106, 117; V02 obs. 004, 025, 083, 086; V03 obs. 006, 096; V04 obs. 086, 087 | The V01 staircase anticipated this. | REVISE at V02 (SW-CR-0010). V03: STRENGTHEN (SW-CR-0028). V04: STRENGTHEN (SW-CR-0054). AFTER04: STRENGTHEN (SW-CR-0088). V05: STRENGTHEN (SW-CR-0128). V06: STRENGTHEN (SW-CR-0172). V07: STRENGTHEN (SW-CR-0222). V08: STRENGTHEN (SW-CR-0278). V09: STRENGTHEN (SW-CR-0340). EXTRA09: PRESERVE (SW-CR-0408). | — | SW-F-0001; SW-F-0010 |
| SW-C-0011 | Rank and truth | The school treats rank as epistemic authority; Cyril’s inquiry is the first counterexample; at V02 rank is also used as a weapon of justice (Felix, Isabelle) and Elliott’s code ties rank to duty; at V03 Elliott’s contempt for upstarts has a biographical root and he warns that talent crossing class walls is envied or used. | V01–V04; OTE, NP | V01 obs. 058, 091; V02 obs. 021, 024, 052, 053; V03 obs. 022, 037, 038; V04 obs. 044, 070 | Cyril’s fairness may be exceptional. | STRENGTHEN at V02 (SW-CR-0011). V03: STRENGTHEN (SW-CR-0029). V04: STRENGTHEN (SW-CR-0055). AFTER04: STRENGTHEN (SW-CR-0089). V05: STRENGTHEN (SW-CR-0129). V06: STRENGTHEN (SW-CR-0173). V07: STRENGTHEN (SW-CR-0223). V08: STRENGTHEN (SW-CR-0279). V09: STRENGTHEN (SW-CR-0341). EXTRA09: PRESERVE (SW-CR-0409). | Further authorities’ conduct. | SW-W-0023; SW-S-0007 |
| SW-C-0012 | Thornley’s crimes | Organized embezzlement; erased Aaron’s and Cyril’s memories; Selma’s manipulation inferred; at V04 a traitor curse-caster reveals that Thornley worked for a patron called 閣下 through mind interference and was discarded. | V01–V04; CRB, OTE | obs. 022, 081, 108; V03 obs. 092; V04 obs. 122 | Selma acted alone. | Aaron and Cyril established; Selma inferred. Reviewed at V02: PRESERVE (SW-CR-0012). V03: PRESERVE (SW-CR-0030). V04: REVISE (SW-CR-0056). AFTER04: PRESERVE (SW-CR-0090). V05: STRENGTHEN (SW-CR-0130). V06: PRESERVE (SW-CR-0174). V07: PRESERVE (SW-CR-0224). V08: PRESERVE (SW-CR-0280). V09: PRESERVE (SW-CR-0342). EXTRA09: PRESERVE (SW-CR-0410). | Thornley’s interrogation results. | SW-K-0011; SW-K-0012 |
| SW-C-0013 | Nero’s nature | Nero is the Worgan black dragon, driven from the Empire’s mountains, worshipped but not commanded by the wyverns, and Monica’s familiar by his own choice after she pulled a bone from his throat; he can use black flame only in his true form. | V01–V04; CRB | obs. 072, 102; V04 obs. 020, 092 | Unusual familiar spirit. | OPEN. Reviewed at V02: PRESERVE (SW-CR-0013). V03: PRESERVE (SW-CR-0031). V04: STRENGTHEN (SW-CR-0057). AFTER04: PRESERVE (SW-CR-0091). V05: REVISE (SW-CR-0131). V06: PRESERVE (SW-CR-0175). V07: PRESERVE (SW-CR-0225). V08: STRENGTHEN (SW-CR-0281). V09: PRESERVE (SW-CR-0343). EXTRA09: STRENGTHEN (SW-CR-0411). | Disclosure of origin. | SW-P-0008 |
| SW-C-0014 | Talent as curse | Monica regards her talent as a curse that took her father and friend; her father, Venedict Rain, author of a book on heredity and magical properties, was executed as a heretic when Monica was ten and his book burned; the friend, Bernie Jones, needed her dependence, turned away in envy, sent her to the hut, and wanted to be her equal rival; she has renounced his approval. Correction: the V03 formulation dated the execution five years before the present, but the V03 text dates only the book’s publication. | V01–V04; CRB, NP | V01 obs. 090, 101; V02 obs. 034, 044; V03 obs. 004, 007, 009, 045, 105; V04 obs. 001, 037 | Delirium distortion. | REVISE at V02 (SW-CR-0014); research OPEN. V03: REVISE (SW-CR-0032). V04: REVISE with correction (SW-CR-0058). AFTER04: PRESERVE (SW-CR-0092). V05: STRENGTHEN (SW-CR-0132). V06: STRENGTHEN (SW-CR-0176). V07: PRESERVE (SW-CR-0226). V08: PRESERVE (SW-CR-0282). V09: PRESERVE (SW-CR-0344). EXTRA09: PRESERVE (SW-CR-0412). | Account of the research. | SW-S-0008; SW-S-0025; SW-P-0017 |
| SW-C-0015 | Friendship | The bond with Lana rests on shared experience of being called boring and being out of place, and on mutual gestures of giving; Lana began from pride and stays from affection; at V03 Lana arms and defends her, and Monica defends Lana first. | V01–V04; OTE, CRB | V01 obs. 031, 046, 083, 112; V02 obs. 008, 029, 031, 032; V03 obs. 032, 044, 045; V04 obs. 052, 099 | Convenience on Lana’s side. | STRENGTHEN and REVISE at V02 (SW-CR-0015). V03: STRENGTHEN (SW-CR-0033). V04: STRENGTHEN (SW-CR-0059). AFTER04: STRENGTHEN (SW-CR-0093). V05: PRESERVE (SW-CR-0133). V06: STRENGTHEN (SW-CR-0177). V07: STRENGTHEN (SW-CR-0227). V08: STRENGTHEN (SW-CR-0283). V09: STRENGTHEN (SW-CR-0345). EXTRA09: STRENGTHEN (SW-CR-0413). | Disclosure strain. | SW-R-0007; SW-R-0008; SW-R-0023; SW-R-0024 |
| SW-C-0016 | Comedy and harm | The comedy of coercion registers harm in most cases; the non-consensual kiss is unevaluated and unknown to its recipient. | V01–V04; NE | obs. 010, 073, 076, 092; V03 obs. 083, 118 | The narration treats it as harmless play. Criterion: whether effect on the affected person is registered independent of tone. | Recorded. Reviewed at V02: PRESERVE; UNTESTED (SW-CR-0016). V03: PRESERVE; kiss UNTESTED (SW-CR-0034). V04: PRESERVE; kiss UNTESTED (SW-CR-0060). AFTER04: STRENGTHEN (SW-CR-0094). V05: STRENGTHEN (SW-CR-0134). V06: STRENGTHEN (SW-CR-0178). V07: STRENGTHEN (SW-CR-0228). V08: PRESERVE (SW-CR-0284). V09: PRESERVE (SW-CR-0346). EXTRA09: PRESERVE (SW-CR-0414). | Any later revisiting. | SW-F-0008 |
| SW-C-0017 | Louis’s stance | Louis combines coercion with investment in her self-respect and his own pride; at V02 also gifts, an unknowing decoy, and a concession calculated to keep her cooperation; at V03 he lends Lynn and, to Casey, judges her a heartless witch. | V01–V04; CRB, SI | V01 obs. 011, 117, 118; V02 obs. 009, 010, 096, 099; V03 obs. 029, 034, 131; V04 obs. 096, 101, 120 | Pure self-interest. | STRENGTHEN at V02 (SW-CR-0017). V03: STRENGTHEN (SW-CR-0035). V04: STRENGTHEN (SW-CR-0061). AFTER04: STRENGTHEN (SW-CR-0095). V05: STRENGTHEN (SW-CR-0135). V06: STRENGTHEN (SW-CR-0179). V07: STRENGTHEN (SW-CR-0229). V08: STRENGTHEN (SW-CR-0285). V09: PRESERVE (SW-CR-0347). EXTRA09: STRENGTHEN (SW-CR-0415). | Louis acting against her interests. | SW-S-0017; SW-S-0036 |
| SW-C-0018 | Source of perception | Monica’s numerical perception and comfort derive from her father’s teaching; his saying that the world is made of numbers became her means of fleeing reality under her uncle; she memorized his burning numbers and keeps his coffee pot; at V04 she refuses the saying as an excuse. | V01–V04; NP, CRB | V01 obs. 026, 043, 044; V02 obs. 034, 044, 058; V03 obs. 105; V04 obs. 005, 097 | Innate disposition. | STRENGTHEN at V02 (SW-CR-0018). V03: STRENGTHEN (SW-CR-0036). V04: REVISE (SW-CR-0062). AFTER04: PRESERVE (SW-CR-0096). V05: STRENGTHEN (SW-CR-0136). V06: PRESERVE (SW-CR-0180). V07: PRESERVE (SW-CR-0230). V08: PRESERVE (SW-CR-0286). V09: PRESERVE (SW-CR-0348). EXTRA09: STRENGTHEN (SW-CR-0416). | — | SW-S-0001; SW-S-0025 |
| SW-C-0019 | Casey and the prologue | Casey Grove is the prologue’s unnamed conspirator, acting on Count Bright’s order with a 螺炎, from grievance at central neglect and gratitude to Randall; her friendship was begun instrumentally; at V03 Count Bright claims sole responsibility, Louis suspects Randall and the Empire, and Casey asks after Monica and sends her a package, so that her feeling is evidenced as concern and its history remains OPEN. | V02–V04; OTE for identity, UQ for feeling | V02 obs. 027, 070, 079–082, 097, 111; V03 obs. 029, 128, 129, 131; V04 obs. 097 | Partly genuine friendship. | Identity established; feeling OPEN. V03: STRENGTHEN and partly REVISE (SW-CR-0037). V04: STRENGTHEN (SW-CR-0063). AFTER04: PRESERVE (SW-CR-0097). V05: PRESERVE (SW-CR-0137). V06: PRESERVE (SW-CR-0181). V07: PRESERVE (SW-CR-0231). V08: PRESERVE (SW-CR-0287). V09: PRESERVE (SW-CR-0349). EXTRA09: PRESERVE (SW-CR-0417). | Casey’s later testimony. | SW-S-0040; SW-P-0019 |
| SW-C-0020 | Duty | Monica derives a concept of duty from Elliott’s noblesse oblige and transposes it to her roles as treasurer and Sage; at V03 duty is joined by a personal motive she calls selfish, that the bereaved be able to mourn as she could not. | V02–V04; SI | V02 obs. 024, 033, 083, 084; V03 obs. 088, 097; V04 obs. 021, 103 | Compliance under pressure. | Strong inference. V03: REVISE (SW-CR-0038). V04: STRENGTHEN (SW-CR-0064). AFTER04: STRENGTHEN (SW-CR-0098). V05: STRENGTHEN (SW-CR-0138). V06: PRESERVE (SW-CR-0182). V07: STRENGTHEN (SW-CR-0232). V08: PRESERVE (SW-CR-0288). V09: PRESERVE (SW-CR-0350). EXTRA09: PRESERVE (SW-CR-0418). | Her conduct when duty and fear conflict again. | SW-S-0027 |
| SW-C-0021 | Concealment of the attempt | Monica’s concealment is a political bargain using Louis’s factional logic, at a cost to Cyril and her conscience; the volume presents it sympathetically and leaves its justice unjudged; at V03 Cyril still blames himself and she cannot clear him. | V02–V04; NE | V02 obs. 095, 096, 098; V03 obs. 016 | Mercy as plain virtue. Criterion: costs to others registered. | Recorded. V03: STRENGTHEN (SW-CR-0039). V04: PRESERVE (SW-CR-0065). AFTER04: PRESERVE (SW-CR-0099). V05: PRESERVE (SW-CR-0139). V06: PRESERVE (SW-CR-0183). V07: PRESERVE (SW-CR-0233). V08: PRESERVE (SW-CR-0289). V09: PRESERVE (SW-CR-0351). EXTRA09: PRESERVE (SW-CR-0419). | Later consequences. | SW-F-0015 |
| SW-C-0022 | Felix’s discontinuities | The cluster of details around Felix’s identity and history, held without hypothesis from V02 to V07, is explained in V08 by narration: the present Felix is the page Isaac Walker, remade by body manipulation after the real prince’s death about ten years ago; see SW-C-0063. | V02–V04; UQ | V02 obs. 039, 049, 062, 093; V03 obs. 018–020, 065, 070, 109, 112–114, 121; V04 obs. 027, 091, 113, 118, 120 | Ordinary nostalgia and rhetoric. | OPEN. V03: STRENGTHEN in scope (SW-CR-0040). V04: STRENGTHEN in scope (SW-CR-0066). AFTER04: STRENGTHEN (SW-CR-0100). V05: STRENGTHEN (SW-CR-0140). V06: STRENGTHEN (SW-CR-0184). V07: STRENGTHEN (SW-CR-0234). V08: REVISE (SW-CR-0290). V09: PRESERVE (SW-CR-0352). EXTRA09: PRESERVE (SW-CR-0420). | Any disclosure about his childhood. | SW-P-0016 |
| SW-C-0023 | Affiliation | Monica says she cannot expect anything of anyone, while her conduct shows growing attachment; no romantic interest on her side is shown and she does not wish to marry; Felix’s absorption in the Silent Witch as an idea is now joined, in his own viewpoint, by attachment and jealousy toward Monica herself. | V02–V04; CRB, SI | V02 obs. 038, 057, 071, 088; V03 obs. 103, 111, 119; V03 reading section 8.1; V04 obs. 081, 105, 114, 115 | Her statement is accurate for romance. | Recorded. V03: STRENGTHEN (SW-CR-0041). V04: REVISE (SW-CR-0067). AFTER04: PRESERVE (SW-CR-0101). V05: STRENGTHEN (SW-CR-0141). V06: STRENGTHEN (SW-CR-0185). V07: STRENGTHEN (SW-CR-0235). V08: STRENGTHEN (SW-CR-0291). V09: STRENGTHEN (SW-CR-0353). EXTRA09: PRESERVE (SW-CR-0421). | Her own account of attachment. | SW-S-0031 |
| SW-C-0024 | Mission and belonging | Louis chose Monica for her distrust, fear and hatred of people, calls her heartless, and reads her attachment as a risk; Monica shared the warning that Monica Norton is temporary; at V08 she ends it herself by revealing her identity to her council and asking their help. | V02–V04; CRB | V02 obs. 096; S18:E000792–E000798; V03 obs. 055, 131; V04 obs. 098, 119 | — | Recorded. V03: STRENGTHEN (SW-CR-0042). V04: STRENGTHEN (SW-CR-0068). AFTER04: STRENGTHEN (SW-CR-0102). V05: PRESERVE (SW-CR-0142). V06: STRENGTHEN (SW-CR-0186). V07: STRENGTHEN (SW-CR-0236). V08: REVISE (SW-CR-0292). V09: STRENGTHEN (SW-CR-0354). EXTRA09: STRENGTHEN (SW-CR-0422). | A conflict between friendship and mission. | SW-R-0034 |
| SW-C-0025 | Isabelle’s method | Isabelle’s cover-bullying is a deliberate deterrence policy and her revenge mirrors the crime; the volume treats humiliation as justice. | V02–V04; CRB, NE | V02 obs. 052–055; V03 obs. 066, 089; V04 obs. 046 | Pure enjoyment of the role. | Recorded. V03: PRESERVE (SW-CR-0043). V04: STRENGTHEN (SW-CR-0069). AFTER04: STRENGTHEN (SW-CR-0103). V05: STRENGTHEN (SW-CR-0143). V06: STRENGTHEN (SW-CR-0187). V07: PRESERVE (SW-CR-0237). V08: PRESERVE (SW-CR-0293). V09: PRESERVE (SW-CR-0355). EXTRA09: STRENGTHEN (SW-CR-0423). | — | SW-F-0016 |
| SW-C-0026 | Out of place | 場違い organizes the social plot through three outsiders by class or region, Monica, Lana and Casey, reversing from exclusion to self-gift. | V02–V04; SI (form) | V02 obs. 003, 029, 031; S15:E000845; S17:E000496 (incidental); V04 locators S14:E000534 and S16:E000894 | Common word. | Recorded. V03: PRESERVE (SW-CR-0044). V04: STRENGTHEN (SW-CR-0070). AFTER04: PRESERVE (SW-CR-0104). V05: PRESERVE (SW-CR-0144). V06: PRESERVE (SW-CR-0188). V07: PRESERVE (SW-CR-0238). V08: PRESERVE (SW-CR-0294). V09: PRESERVE (SW-CR-0356). EXTRA09: PRESERVE (SW-CR-0424). | Recurrence. | SW-F-0012 |
| SW-C-0027 | Bernie Jones | Bernie Jones is the Minerva friend; his help coexisted with a wish for her dependence; his envy ended the friendship and his curse began the hut life, which Monica entered at fifteen wondering whether he would now forgive her; he protected her cover as a noble’s duty, wanted to be her equal rival, and leaves Minerva as heir offering future help. | V03–V04; OTE for identity and acts, UQ for motive | V03 obs. 001–009, 042–046, 054, 056; V04 obs. 035–038 | Repentance or possession, V03 reading section 8.2. | Identity established; motive OPEN. V04: REVISE (SW-CR-0071). AFTER04: PRESERVE (SW-CR-0105). V05: STRENGTHEN (SW-CR-0145). V06: STRENGTHEN (SW-CR-0189). V07: PRESERVE (SW-CR-0239). V08: PRESERVE (SW-CR-0295). V09: PRESERVE (SW-CR-0357). EXTRA09: REVISE (SW-CR-0425). | His next act toward her. | SW-S-0053; SW-P-0025 |
| SW-C-0028 | Mourning | Mourning organizes V03: Monica’s motive in the climax is that the bereaved be able to mourn as she could not; burned books and festival bells join her strand and Felix’s. | V03–V04; SI (form) | V03 obs. 076–077, 088, 097, 105–109, 113 | Duty alone. | Strong inference. V04: PRESERVE (SW-CR-0072). AFTER04: PRESERVE (SW-CR-0106). V05: PRESERVE (SW-CR-0146). V06: PRESERVE (SW-CR-0190). V07: PRESERVE (SW-CR-0240). V08: PRESERVE (SW-CR-0296). V09: PRESERVE (SW-CR-0358). EXTRA09: PRESERVE (SW-CR-0426). | Recurrence of the motive. | SW-F-0018 |
| SW-C-0029 | Ike | Ike is the childhood name the real prince used for his page Isaac Walker; as Ike, the present Felix shows Monica the self outside his role; her answering self-description as a ghost was her first outreach; the persona persists in private moments, and Monica keeps its confidences from Louis. | V03–V04; CRB, SI | V03 obs. 078, 087, 100, 118–122; V04 obs. 009, 067, 113 | Pure performance on his side. | Recorded. V04: REVISE (SW-CR-0073). AFTER04: STRENGTHEN (SW-CR-0107). V05: PRESERVE (SW-CR-0147). V06: STRENGTHEN (SW-CR-0191). V07: STRENGTHEN (SW-CR-0241). V08: REVISE (SW-CR-0297). V09: STRENGTHEN (SW-CR-0359). EXTRA09: PRESERVE (SW-CR-0427). | Any return of Ike. | SW-S-0051; SW-R-0045; SW-R-0046 |
| SW-C-0030 | The duke’s hold | The duke dominated the boy by contempt, took Isaac to replace the prince and discarded him when he rebelled; at V09 his hold is broken by the settlement: he is silenced by Monica, expects to withdraw, and is read by Mary as a man who loves and hates the country. | V03–V04; OTE, SI | V03 obs. 061, 082, 113; V04 obs. 080, 104 | Felix’s compliance may be sincere. | Recorded; ground OPEN. V04: STRENGTHEN (SW-CR-0074). AFTER04: STRENGTHEN (SW-CR-0108). V05: STRENGTHEN (SW-CR-0148). V06: STRENGTHEN (SW-CR-0192). V07: STRENGTHEN (SW-CR-0242). V08: REVISE (SW-CR-0298). V09: REVISE (SW-CR-0360). EXTRA09: PRESERVE (SW-CR-0428). | The source of the hold. | SW-P-0007; SW-R-0048; SW-R-0049 |
| SW-C-0031 | Imperial agents | Imperial agents Yuan and Heidi serve the young emperor Leonhardt, who wants to avoid war by exposing the false prince at his accession; Yuan pursued Artur, his former friend who stole his body-manipulation research and served Clockford as the physician Arthur; the emperor came to Ridill himself and bargained with Monica. | V03–V04; OTE, CRB | V03 obs. 052, 123–125, 128; V04 obs. 083–094 | A renegade agent. | Established for the agents; alliance OPEN. V04: REVISE (SW-CR-0075). AFTER04: PRESERVE (SW-CR-0109). V05: PRESERVE (SW-CR-0149). V06: PRESERVE (SW-CR-0193). V07: STRENGTHEN (SW-CR-0243). V08: REVISE (SW-CR-0299). V09: PRESERVE (SW-CR-0361). EXTRA09: PRESERVE (SW-CR-0429). | The festival. | SW-P-0023; SW-W-0044; SW-W-0052 |
| SW-C-0032 | The father | Monica’s father was Venedict Rain, author of a book on heredity and magical properties, executed seven years ago, when Monica was ten, after a curse-caster he refused had him charged with necromancy on planted evidence, under a great noble’s pressure and without trial; his former assistant Hilda Everett adopted her; his friend Porter is Dustin Günther. The V04 correction stands. | V03–V04; OTE, paratext for the surname | V03 obs. 105–106, 126, 133; V04 obs. 001, 007, 123 | — | Established. V04: REVISE with correction (SW-CR-0076). AFTER04: PRESERVE (SW-CR-0110). V05: REVISE (SW-CR-0150). V06: PRESERVE (SW-CR-0194). V07: PRESERVE (SW-CR-0244). V08: STRENGTHEN (SW-CR-0300). V09: PRESERVE (SW-CR-0362). EXTRA09: PRESERVE (SW-CR-0430). | — | SW-P-0005; SW-P-0017 |
| SW-C-0033 | Louis’s model of Monica | Louis’s model of Monica as a heartless witch who sees people as numbers was half right; at V09 the narration names his error as assuming she would never ask others for help, and he concedes his second clean defeat by her. | V03–V04; CRB, NE | V03 obs. 130–131; V04 obs. 050, 088, 096 | Louis may be right about her toward strangers. Criterion: her conduct toward people in the same volume. | Recorded. V04: REVISE (SW-CR-0077). AFTER04: PRESERVE (SW-CR-0111). V05: PRESERVE (SW-CR-0151). V06: STRENGTHEN (SW-CR-0195). V07: STRENGTHEN (SW-CR-0245). V08: STRENGTHEN (SW-CR-0301). V09: REVISE (SW-CR-0363). EXTRA09: STRENGTHEN (SW-CR-0431). | Louis observing her with friends. | SW-S-0054; SW-F-0021 |
| SW-C-0034 | Mary’s test | Mary deliberately allowed the theft of the ancient tool, citing the stars’ guidance, and used the crisis to test Monica; the volume does not judge the risk to the town or the bystander. | V03–V04; CRB, NE | V03 obs. 093, 116 | Protective foresight. Criterion: risks to third parties registered. | Recorded. V04: PRESERVE (SW-CR-0078). AFTER04: PRESERVE (SW-CR-0112). V05: STRENGTHEN (SW-CR-0152). V06: PRESERVE (SW-CR-0196). V07: PRESERVE (SW-CR-0246). V08: PRESERVE (SW-CR-0302). V09: PRESERVE (SW-CR-0364). EXTRA09: PRESERVE (SW-CR-0432). | Mary’s own account. | SW-P-0024 |
| SW-C-0035 | Numbers as weapon and limit | Monica’s numerical dissociation, born of abuse, became a chosen weapon and a limit, and now also a means of evidence; she remains Monica Norton knowing it deceives her friends, and her purpose widens to her father’s innocence. | V04; SI | V04 obs. 003–005, 085, 090, 096–098 | Fatigue and poison explain the failure. | Strong inference. AFTER04: STRENGTHEN (SW-CR-0113). V05: REVISE (SW-CR-0153). V06: PRESERVE (SW-CR-0197). V07: PRESERVE (SW-CR-0247). V08: PRESERVE (SW-CR-0303). V09: PRESERVE (SW-CR-0365). EXTRA09: STRENGTHEN (SW-CR-0433). | Her next combat involving friends. | SW-S-0066; SW-C-0002 |
| SW-C-0036 | Misread gifts | V04 is organized by gifts whose meaning differs between giver and receiver: the rose, the cursed necklace, the pendant, the handkerchief and the friend’s wish. | V04; SI (form) | V04 obs. 032, 045, 097, 114, 116 | Festival props. | Recorded. AFTER04: STRENGTHEN (SW-CR-0114). V05: STRENGTHEN (SW-CR-0154). V06: PRESERVE (SW-CR-0198). V07: PRESERVE (SW-CR-0248). V08: PRESERVE (SW-CR-0304). V09: PRESERVE (SW-CR-0366). EXTRA09: PRESERVE (SW-CR-0434). | — | SW-F-0023 |
| SW-C-0037 | Cyril’s mirror | Cyril’s history mirrors Monica’s: a violent father, withheld praise and striving for recognition; his care for her is a disguised invitation and practical help, and his attention returns to her hand. | V04; OTE, SI | V04 obs. 015, 077, 078, 108–110 | Duty alone. | Recorded. AFTER04: STRENGTHEN (SW-CR-0115). V05: STRENGTHEN (SW-CR-0155). V06: STRENGTHEN (SW-CR-0199). V07: STRENGTHEN (SW-CR-0249). V08: STRENGTHEN (SW-CR-0305). V09: STRENGTHEN (SW-CR-0367). EXTRA09: STRENGTHEN (SW-CR-0435). | Cyril’s conclusion about her hand. | SW-S-0072; SW-S-0073; SW-P-0031 |
| SW-C-0038 | Felix’s star | The present Felix’s wish to be remembered was a wish that the dead prince’s name not be forgotten, overriding the prince’s last wish for Isaac’s own happiness; at V09 the diary shows him that wish and the obsession ends; he speaks the prince’s wish at graduation and pursues magic as his own. | V04; CRB, UQ | V04 obs. 064, 116, 117 | Rhetoric. | OPEN as to meaning. AFTER04: PRESERVE (SW-CR-0116). V05: STRENGTHEN (SW-CR-0156). V06: PRESERVE (SW-CR-0200). V07: PRESERVE (SW-CR-0250). V08: REVISE (SW-CR-0306). V09: REVISE (SW-CR-0368). EXTRA09: STRENGTHEN (SW-CR-0436). | Felix’s acts on the wish. | SW-S-0071; SW-P-0002 |
| SW-C-0039 | The traitor and 閣下 | The traitor curse-caster was Barry Oates, serving at Leinbourg as the footman Peter Sams; he denounced Venedict Rain and served at Clockford’s house after Clockford killed the physician Arthur; at V09 Monica’s viewpoint narration states that Clockford was the mastermind of the Leinbourg curse dragon and tied to Sams, and the council is told Sams alone was responsible; 閣下, Sams’s word for his patron, is not used in V09. | V04; OTE, UQ | V04 obs. 122, 123 | — | Identity OPEN. AFTER04: PRESERVE (SW-CR-0117). V05: REVISE (SW-CR-0157). V06: REVISE (SW-CR-0201). V07: REVISE (SW-CR-0251). V08: REVISE (SW-CR-0307). V09: REVISE (SW-CR-0369). EXTRA09: PRESERVE (SW-CR-0437). | Naming of 閣下. | SW-P-0029 |
| SW-C-0040 | Eliane’s responsibility | The volume assigns Eliane moral responsibility for acts partly amplified by a curse, and lets her go unexamined in the world. | V04; NE | V04 obs. 054, 061, 063, 079 | Curse excuses her. Criterion: responsibility assigned under external influence. | Recorded. AFTER04: PRESERVE (SW-CR-0118). V05: PRESERVE (SW-CR-0158). V06: PRESERVE (SW-CR-0202). V07: PRESERVE (SW-CR-0252). V08: PRESERVE (SW-CR-0308). V09: PRESERVE (SW-CR-0370). EXTRA09: PRESERVE (SW-CR-0438). | — | SW-S-0077 |
| SW-C-0041 | Charms as courage | The companion argues that charms work by giving the user courage through something special; Monica, who rejected the theory, makes and keeps charms herself, and the inverse case of a curse taken for a charm shows the danger of not knowing what one holds. | AFTER04; SI | AFTER04 obs. 014, 015, 066, 118, 139, 156–159 | Charms as mere comic motif. | Recorded; moderate. V05: STRENGTHEN (SW-CR-0159). V06: PRESERVE (SW-CR-0203). V07: PRESERVE (SW-CR-0253). V08: STRENGTHEN (SW-CR-0309). V09: STRENGTHEN (SW-CR-0371). EXTRA09: PRESERVE (SW-CR-0439). | Monica’s later use of charms. | SW-F-0028 |
| SW-C-0042 | Unseen power, small lies | Monica’s power was visible only to a spirit and the reader while she lived as Monica Norton; acting openly as the Silent Witch, her concealment fails before Felix, whose inferences outpace her small lies. | AFTER04; SI, OTE | AFTER04 obs. 044, 092, 095, 116, 119, 137 | The lies as harmless. | Recorded. V05: REVISE (SW-CR-0160). V06: STRENGTHEN (SW-CR-0204). V07: PRESERVE (SW-CR-0254). V08: STRENGTHEN (SW-CR-0310). V09: STRENGTHEN (SW-CR-0372). EXTRA09: PRESERVE (SW-CR-0440). | A lie’s cost to a friend. | SW-F-0030; SW-S-0088 |
| SW-C-0043 | Effort against strength | Cyril’s ethic of earned, patient effort is set against Louis’s maxim of money, violence and strength; Glen and Monica, who drifted into magic, take Cyril’s side. | AFTER04; SI | AFTER04 obs. 075, 079, 090, 099 | Louis’s maxim as joke only. | Recorded. V05: STRENGTHEN (SW-CR-0161). V06: STRENGTHEN (SW-CR-0205). V07: STRENGTHEN (SW-CR-0255). V08: STRENGTHEN (SW-CR-0311). V09: STRENGTHEN (SW-CR-0373). EXTRA09: PRESERVE (SW-CR-0441). | Later tests of either ethic. | SW-S-0086; SW-S-0091 |
| SW-C-0044 | Elliott’s creed | Elliott’s creed of rank rests on an uncle’s suicide and on what he saw before he was ten; the talented commoner he once said was ruined by cunning people is Isaac Walker, by his own acknowledgement; his own friendship contradicts it, and he cannot call Isaac a fool. | AFTER04; OTE; UQ | AFTER04 obs. 110–112 | Creed as class prejudice only. | Recorded; second event unknown. V05: PRESERVE (SW-CR-0162). V06: PRESERVE (SW-CR-0206). V07: PRESERVE (SW-CR-0256). V08: REVISE (SW-CR-0312). V09: STRENGTHEN (SW-CR-0374). EXTRA09: STRENGTHEN (SW-CR-0442). | Disclosure of the event. | SW-S-0095; SW-K-0064 |
| SW-C-0045 | The father framed | Monica’s father was framed through Sams’s denunciation; the narration states that Clockford arranged the execution; Monica forgoes clearing his name in order to save Isaac, and uses his design at the council. | V05; OTE | V05 obs. 147, 149, 166, 170, 180 | Sams’s words are a dying man’s; Hilda’s account is hers. | Recorded. V06: STRENGTHEN (SW-CR-0207). V07: STRENGTHEN (SW-CR-0257). V08: REVISE (SW-CR-0313). V09: REVISE (SW-CR-0375). EXTRA09: PRESERVE (SW-CR-0443). | The noble’s identity. | SW-S-0106 |
| SW-C-0046 | Concealment fails | Monica’s concealment fails in three directions in one break: Bartholomeus, Felix’s inference of her school, and Felix’s knowledge of her familiar. | V05; OTE, SI | V05 obs. 063, 106, 129 | Each breach partial. | Recorded. V06: STRENGTHEN (SW-CR-0208). V07: STRENGTHEN (SW-CR-0258). V08: STRENGTHEN (SW-CR-0314). V09: STRENGTHEN (SW-CR-0376). EXTRA09: PRESERVE (SW-CR-0444). | Felix’s search. | SW-K-0067; SW-K-0068 |
| SW-C-0047 | Felix the puppet | The present Felix believed his grandfather meant to make him a puppet, and plotted the duke’s death; at V09 he is rescued by a staged settlement, renounces the succession, and serves as Duke of Erin under the prince’s name. | V05; CRB | V05 obs. 096–099, 159 | His inferences, unconfirmed. | Recorded. V06: REVISE (SW-CR-0209). V07: STRENGTHEN (SW-CR-0259). V08: REVISE (SW-CR-0315). V09: REVISE (SW-CR-0377). EXTRA09: PRESERVE (SW-CR-0445). | Clockford’s acts. | SW-S-0109 |
| SW-C-0048 | The table lesson | The volume is framed by Louis’s lesson that the game begins before the table, which Monica learns by losing. | V05; SI | V05 obs. 005–007, 129, 130 | Comic prologue only. | Recorded. V06: PRESERVE (SW-CR-0210). V07: PRESERVE (SW-CR-0260). V08: PRESERVE (SW-CR-0316). V09: STRENGTHEN (SW-CR-0378). EXTRA09: PRESERVE (SW-CR-0446). | — | SW-F-0031 |
| SW-C-0049 | Vows before witnesses | Vows made before a witness organize the volume, and the chime sounds for each. | V05; SI | V05 obs. 020–022, 176–180 | Decoration. | Recorded. V06: PRESERVE (SW-CR-0211). V07: PRESERVE (SW-CR-0261). V08: STRENGTHEN (SW-CR-0317). V09: PRESERVE (SW-CR-0379). EXTRA09: PRESERVE (SW-CR-0447). | — | SW-F-0032 |
| SW-C-0050 | The cluster deepens | The contract stone, the water spirit against an earth name, the eye colour and a vow ending in Arc are explained at V08: the stone and spirit were Queen Irene’s, given by the real prince to Isaac; the prince’s affinity was earth; the eye colour differs between the two boys; Arc is the prince’s middle name used as his secret name. | V05; OTE; UQ | V05 reading section 6.9 | Each detail may be incidental. | No hypothesis registered. V06: STRENGTHEN (SW-CR-0212). V07: STRENGTHEN (SW-CR-0262). V08: REVISE (SW-CR-0318). V09: PRESERVE (SW-CR-0380). EXTRA09: PRESERVE (SW-CR-0448). | Later disclosure. | SW-C-0022 |
| SW-C-0051 | Anger named | Monica’s anger moves from an unnamed loss of control to a recognized feeling with a cause, and Louis licenses it; the volume does not judge it. | V06; OTE, SI | V06 obs. 064, 154, 155, 184, 185 | Two episodes only. | Recorded. V07: PRESERVE (SW-CR-0263). V08: PRESERVE (SW-CR-0319). V09: PRESERVE (SW-CR-0381). EXTRA09: PRESERVE (SW-CR-0449). | Durability. | SW-S-0121; SW-F-0035 |
| SW-C-0052 | Help asked | The volume repeatedly poses whether one may ask for help; Monica is urged to in V06 and first asks, of Bartholomeus, at the opening of V07. | V06; SI | V06 obs. 114, 130, 165, 166, 182, 207 | Coincidence of phrasing. | Recorded. V07: REVISE (SW-CR-0264). V08: STRENGTHEN (SW-CR-0320). V09: STRENGTHEN (SW-CR-0382). EXTRA09: STRENGTHEN (SW-CR-0450). | Whether she asks. | SW-F-0036 |
| SW-C-0053 | Clockford inferred | Monica inferred Clockford’s connection to her father’s death; V08 and V09 narration state it; 閣下 is not identified by name. Emmanuel’s patron is Clockford, SW-C-0057. | V06; CRB | V06 obs. 021–024, 063, 204–206, 211 | Her inference; the card is paratext. | No identification registered. V07: REVISE (SW-CR-0265). V08: REVISE (SW-CR-0321). V09: REVISE (SW-CR-0383). EXTRA09: PRESERVE (SW-CR-0451). | Later disclosure. | SW-S-0123 |
| SW-C-0054 | The Sages’ cover-up | The Seven Sages hide a member’s crime to keep their independence from the noble assembly; the volume presents this as self-protection, not justice. | V06; OTE | V06 obs. 050, 051, 187, 190 | Louis’s framing. | Recorded. V07: STRENGTHEN (SW-CR-0266). V08: STRENGTHEN (SW-CR-0322). V09: PRESERVE (SW-CR-0384). EXTRA09: PRESERVE (SW-CR-0452). | The affair’s end. | SW-W-0083 |
| SW-C-0055 | False chantless | Hubert’s imitation makes chantless magic a threat in others’ eyes and a thing of little worth in Monica’s; the plate’s words are his. | V06; OTE, SI | V06 obs. 011, 103, 118, 145, 156, 160 | — | Recorded. V07: PRESERVE (SW-CR-0267). V08: PRESERVE (SW-CR-0323). V09: PRESERVE (SW-CR-0385). EXTRA09: PRESERVE (SW-CR-0453). | — | SW-F-0037 |
| SW-C-0056 | Felix’s two registers | Felix pairs ruthless means with a wish to be relied on, and overlays a remembered friend on Monica. | V06; OTE | V06 obs. 147, 149, 165–167 | Private viewpoint only. | Recorded. V07: STRENGTHEN (SW-CR-0268). V08: STRENGTHEN (SW-CR-0324). V09: PRESERVE (SW-CR-0386). EXTRA09: STRENGTHEN (SW-CR-0454). | The friend’s identity. | SW-S-0127; SW-S-0128 |
| SW-C-0057 | Emmanuel’s patron | Emmanuel’s patron, called あの方 in his thoughts, is Duke Clockford; the identification rests on the same speaker’s usage in V06 and V07 and is not extended to 閣下 or the great noble. | V07; OTE | V07 S15:E000456–E000458; V06 obs. 211 | Two uses by one speaker. | Registered. V08: STRENGTHEN (SW-CR-0325). V09: PRESERVE (SW-CR-0387). EXTRA09: PRESERVE (SW-CR-0455). | — | SW-S-0152 |
| SW-C-0058 | Felix’s past gathered | V07’s account of Felix’s past (a sickly child, an illness and a fire, Mary’s lost star, Bridget’s belief) is explained at V08: the child was the real prince, who died by a fall; the fire burned his body and Arthur’s; the present Felix is the page Isaac Walker. | V07; OTE; UQ | V07 reading sections 6.5, 6.8, 8.1 | Reports and beliefs. | No hypothesis registered. V08: REVISE (SW-CR-0326). V09: PRESERVE (SW-CR-0388). EXTRA09: PRESERVE (SW-CR-0456). | Later disclosure. | SW-C-0022 |
| SW-C-0059 | Asking and knowing | Monica asks for help and wants to know another person for the first time, each by her own decision. | V07; OTE | V07 obs. 005, 157, 179 | Two episodes. | Recorded. V08: STRENGTHEN (SW-CR-0327). V09: STRENGTHEN (SW-CR-0389). EXTRA09: STRENGTHEN (SW-CR-0457). | Durability. | SW-S-0139; SW-S-0142 |
| SW-C-0060 | Uniqueness and competence | The volume sets uniqueness against competence and cooperation, and favours the latter. | V07; SI | V07 obs. 055, 078, 100, 111 | Louis’s voice. | Recorded. V08: PRESERVE (SW-CR-0328). V09: STRENGTHEN (SW-CR-0390). EXTRA09: PRESERVE (SW-CR-0458). | — | SW-F-0039 |
| SW-C-0061 | Helping spirits | Whether humans can help spirits is argued without resolution; Monica’s rescue of Romaria is presented as her ego. | V07; OTE, SI | V07 obs. 040, 112, 126, 130 | — | Recorded. V08: PRESERVE (SW-CR-0329). V09: PRESERVE (SW-CR-0391). EXTRA09: PRESERVE (SW-CR-0459). | — | SW-F-0040 |
| SW-C-0062 | United, divided | The Sages act as one in the forest and conceal from one another throughout. | V07; OTE | V07 obs. 052, 135, 136, 143 | — | Recorded. V08: STRENGTHEN (SW-CR-0330). V09: STRENGTHEN (SW-CR-0392). EXTRA09: PRESERVE (SW-CR-0460). | — | SW-R-0118 |
| SW-C-0063 | The Felix cluster disclosed | The present Felix is the page Isaac Walker, remade by body manipulation; the real prince died by a fall about ten years ago after learning of the substitution, by the diary and Isaac’s recollection an accident, and his body and the physician Arthur’s were burned; Ike is Isaac’s name and Arc the prince’s secret name; Yuan’s Artur is the physician Arthur; Wildianu was Queen Irene’s spirit. Not extended to 閣下. | V08; OTE | V08 reading section 6.2; obs. 097, 143–157, 219 | Narration from inside memory; independent accounts. | Registered. V09: REVISE (SW-CR-0393). EXTRA09: STRENGTHEN (SW-CR-0461). | The diary’s last line. | SW-C-0022; SW-C-0058 |
| SW-C-0064 | The father’s case | Venedict Rain’s death: V08 narration states Clockford had a part, and V09 narration states he arranged the execution; the motive given by Monica, Porter and Isaac is the hereditary tool that could expose the false prince; 閣下 remains unidentified by name. | V08; OTE, CRB | V08 obs. 077, 078, 197–199, 265 | Clockford silent on it. | Registered. V09: REVISE (SW-CR-0394). EXTRA09: PRESERVE (SW-CR-0462). | 閣下. | SW-C-0045; SW-C-0053 |
| SW-C-0065 | Isaac’s two halves | Isaac Walker combined devotion to a dead boy’s name with ruthless means and could not harm Monica; at V09 the obsession ends, he states to himself that he loves her, and he becomes her apprentice. | V08; OTE | V08 obs. 090, 148, 177, 202, 260 | — | Recorded. V09: REVISE (SW-CR-0395). EXTRA09: PRESERVE (SW-CR-0463). | — | SW-S-0164; SW-S-0165 |
| SW-C-0066 | The bargain | Monica bound herself to the emperor to avert war; at V09 he judges the promise kept, though he would have preferred Clockford’s fall, and turns to a treaty of exchange. | V08; OTE | V08 obs. 060–064 | — | Recorded. V09: REVISE (SW-CR-0396). EXTRA09: PRESERVE (SW-CR-0464). | Whether war comes. | SW-R-0136 |
| SW-C-0067 | Rescue over justice | Monica chooses to save Isaac over the exposure that would clear her father, and reveals herself to ask for help. | V08; OTE | V08 obs. 182, 253, 283, 291 | — | Recorded. V09: STRENGTHEN (SW-CR-0397). EXTRA09: PRESERVE (SW-CR-0465). | Outcome. | SW-S-0159 |
| SW-C-0068 | Remembering names | The volume turns on remembering names: the prince’s fear, Isaac’s assumed name, the curse of the father’s name, and the Witch’s knowledge of Isaac’s. | V08; SI | V08 obs. 114, 148, 180, 181, 261 | — | Recorded. V09: STRENGTHEN (SW-CR-0398). EXTRA09: STRENGTHEN (SW-CR-0466). | — | SW-F-0043 |
| SW-C-0069 | The staged truth | The Supreme Council’s verdict is a staged truth: a real tool with borrowed blood, a dead culprit, a performed cure and royal ratification, with Clockford held by Monica’s silence. | V09; OTE | V09 obs. 088–099, 113, 116 | — | Registered. EXTRA09: PRESERVE (SW-CR-0467). | Whether it holds. | SW-W-0112 |
| SW-C-0070 | An accident | The real prince’s death was an accident, by the diary’s last entry and Isaac’s recollection; his last wish was Isaac’s own life and a reunion. | V09; OTE | V09 obs. 122–125 | Through characters. | Registered. EXTRA09: PRESERVE (SW-CR-0468). | — | SW-C-0063 |
| SW-C-0071 | Revenge on the crown | Mary reads Clockford’s substitution as revenge on the crown, rooted in his father’s killing and his love and hatred of the country; he neither denies nor confirms it. Her first prophecy foretold that father’s death, and she resolves to mourn Clockford when he dies alone (SW-C-0077). | V09; CRB | V09 obs. 110, 111 | Mary’s inference. | Recorded. EXTRA09: REVISE (SW-CR-0469). | — | SW-S-0186 |
| SW-C-0072 | A collective rescue | Monica’s rescue is collective: every element is supplied by people she asked, and the narration names Louis’s error as assuming she would not ask. | V09; OTE, SI | V09 obs. 022–037, 048–072, 116 | — | Recorded. EXTRA09: STRENGTHEN (SW-CR-0470). | — | SW-C-0052 |
| SW-C-0073 | Isaac released | After the rescue Isaac’s obsession ends; his love for Monica is stated in his viewpoint; he becomes her apprentice, while she regards him as a friend. | V09; OTE | V09 obs. 125, 126, 128, 173 | — | Recorded. EXTRA09: STRENGTHEN (SW-CR-0471). | — | SW-R-0146 |
| SW-C-0074 | Arc closed | The volume closes the first arc on silence broken and imposed, and on Monica drinking coffee among friends. | V09; SI, PX | V09 obs. 099, 182, 184 | Afterword. | Recorded. EXTRA09: STRENGTHEN (SW-CR-0472). | — | SW-F-0050 |
| SW-C-0075 | The distance measured | The collection frames school-year stories with post-council scenes, so that the early Monica (chosen solitude, indifference, readiness to kill the dragon-cat) is set against the later one (asking, thanking, receiving); its new writing closes on thanks. | EXTRA09; SI | EXTRA09 obs. 019, 027, 029, 169–171, 177, 183 | — | Registered. | — | SW-F-0052 |
| SW-C-0076 | Hilda’s collaborators | An unnamed authority of the physicians’ association, trusted by the Mage Guild, helped Hilda escape with the chalice design and with others plans to relax the regulation of medical magical tools, which would reopen forbidden arts and the crime for which Venedict Rain died. | EXTRA09; OTE | EXTRA09 obs. 007, 008 | The man unnamed. | Registered. | What the plan brings. | SW-W-0119 |
| SW-C-0077 | Mary and Clockford | Mary’s first prophecy foretold the death of her then-fiancé’s father; with V08 obs. 294 the fiancé is Clockford; he refused to blame her and believes no prophecy; she resolves to mourn his solitary death and so to live long. | EXTRA09; OTE, CRB | EXTRA09 obs. 151–154; V08 obs. 294 | Joined record; her thoughts. | Recorded. | — | SW-R-0163 |
| SW-C-0078 | Cyril’s hidden care | Cyril’s care is given unasked or under stated pretexts: the tea, the treasurer’s checks that blocked Thornley unawares, Neil’s dance, the boxes; he sings only when someone needs help. | EXTRA09; OTE | EXTRA09 obs. 037, 085–087, 100, 113, 137 | — | Recorded. | — | SW-S-0195 |

Revision records at V01: none. Every V01 claim was an initial formulation with no predecessor.

Revision records at V02, 2026-10-14, reviewer the V02 sequential integrator:

| Revision | Claim | Earlier formulation and boundary | Transition | New formulation and boundary | Reason | Affected homes | Kind |
|---|---|---|---|---|---|---|---|
| SW-CR-0001 | SW-C-0001 | Chantless casting began as avoidance of speech; silence and mastery are one mechanism. (V01) | REVISE | Chantless casting began as avoidance of speech, and silence and mastery are one mechanism; the avoidance has an earlier root in childhood punishment for speaking, while the public account explains the capacity as instant computation. (V02) | See V02 reading section 9.1. | V02 evidence | Later reinterpretation, not correction. |
| SW-CR-0002 | SW-C-0002 | Pain, fear or exposure drive Monica into numerical absorption. (V01) | STRENGTHEN | Pain, fear or exposure drive Monica into numerical absorption; the habit began as a vow to keep her father’s numbers. (V02) | See V02 reading section 9.1. | V02 evidence | Later reinterpretation, not correction. |
| SW-CR-0003 | SW-C-0003 | V01 supplies associative evidence of past harm by a drinking adult man she called おじさん, linked to a learned rule of silence. (V01) | REVISE | The man in the V01 dream is Monica’s paternal uncle, who after her father’s execution beat her for reciting numbers and defending him and imposed silence about him in public. (V02) | See V02 reading section 9.1. | V02 evidence | Later reinterpretation, not correction. |
| SW-CR-0004 | SW-C-0004 | The makeweight self-assessment is contradicted by Louis’s memory of the duel; the examiners’ ranking is unstated. (V01) | PRESERVE | Unchanged (V02). | No new evidence on the selection. | — | Review, not change. |
| SW-CR-0005 | SW-C-0005 | Stated protection; Monica doubts it; Louis reads surveillance; king unshown. (V01) | STRENGTHEN | Stated protection; Monica doubts it; Louis reads surveillance, uses a decoy, chose Monica partly for her distrust of people, and calls himself first-prince because he dislikes the duke and Felix; the king is unshown. (V02) | See V02 reading section 9.1. | V02 evidence | Later reinterpretation, not correction. |
| SW-CR-0006 | SW-C-0006 | The prologue’s unnamed watcher is Felix. (V01) | STRENGTHEN | The prologue’s watcher is Felix. (V02) | See V02 reading section 9.1. | V02 evidence | Later reinterpretation, not correction. |
| SW-CR-0007 | SW-C-0007 | Public and private selves diverge; he removes the duke’s placements while professing he cannot defy him. (V01) | STRENGTHEN | Public and private selves diverge: he denies a talent for magic while studying it and hiding a spirit; he removes the duke’s placements while professing he cannot defy him; he must become king without wanting what is prepared for his name, holding the role while he bears it. (V02) | See V02 reading section 9.1. | V02 evidence | Later reinterpretation, not correction. |
| SW-CR-0008 | SW-C-0008 | Felix has not identified Monica as the Silent Witch. (V01) | STRENGTHEN | Felix has not identified Monica as the Silent Witch; at V02 exit he is searching the school for her and his search excludes Monica. (V02) | See V02 reading section 9.1. | V02 evidence | Later reinterpretation, not correction. |
| SW-CR-0009 | SW-C-0009 | Cyril holds an unverified suspicion from her hand and remark. (V01) | REVISE | Cyril holds an unverified suspicion from her hand and remark (V01), and at V02 links the forest mage with the Silent Witch; V02 shows no renewed link to Monica. (V02) | See V02 reading section 9.1. | V02 evidence | Later reinterpretation, not correction. |
| SW-CR-0010 | SW-C-0010 | Monica’s power is narrated through external focalizers; her own viewpoint narrates fear, comedy and small uses. (V01) | REVISE | Awe at Monica’s power is narrated through external focalizers; from V02 her own viewpoint also narrates her power, as calculation under constraint. (V02) | See V02 reading section 9.1. | V02 evidence | Later reinterpretation, not correction. |
| SW-CR-0011 | SW-C-0011 | The school treats rank as epistemic authority; Cyril’s inquiry is the first counterexample and revises her expectation. (V01) | STRENGTHEN | The school treats rank as epistemic authority; Cyril’s inquiry is the first counterexample; at V02 rank is also used as a weapon of justice (Felix, Isabelle) and Elliott’s code ties rank to duty. (V02) | See V02 reading section 9.1. | V02 evidence | Later reinterpretation, not correction. |
| SW-CR-0012 | SW-C-0012 | Organized embezzlement; erased Aaron’s and Cyril’s memories; Selma’s manipulation inferred. (V01) | PRESERVE | Unchanged (V02). | Only the investigators’ visits are shown. | — | Review, not change. |
| SW-CR-0013 | SW-C-0013 | Neither an ordinary cat nor, in Felix’s judgment, a spirit. (V01) | PRESERVE | Unchanged (V02). | No disclosure. | — | Review, not change. |
| SW-CR-0014 | SW-C-0014 | Monica regards her talent as a curse that took her father and friend; her care for Cyril projects this. (V01) | REVISE | Monica regards her talent as a curse that took her father and friend; her father was executed as a heretic for forbidden research into the body as number, and the friend turned away when she mastered chantless magic. (V02) | See V02 reading section 9.1. | V02 evidence | Later reinterpretation, not correction. |
| SW-CR-0015 | SW-C-0015 | The bond with Lana rests on a shared experience of being called boring. (V01) | STRENGTHEN | The bond with Lana rests on shared experience of being called boring and being out of place, and on mutual gestures of giving; Lana began from pride and stays from affection. (V02) | See V02 reading section 9.1. | V02 evidence | Later reinterpretation, not correction. |
| SW-CR-0016 | SW-C-0016 | The comedy of coercion registers harm in most cases; the non-consensual kiss is unevaluated and unknown to its recipient. (V01) | PRESERVE; UNTESTED | Unchanged (V02). | No recurrence of the kiss. | — | Review, not change. |
| SW-CR-0017 | SW-C-0017 | Coercion combined with investment in her self-respect and his own pride. (V01) | STRENGTHEN | Louis combines coercion with investment in her self-respect and his own pride; at V02 also gifts, an unknowing decoy, and a concession calculated to keep her cooperation. (V02) | See V02 reading section 9.1. | V02 evidence | Later reinterpretation, not correction. |
| SW-CR-0018 | SW-C-0018 | Monica’s numerical perception and comfort derive from her father’s teaching. (V01) | STRENGTHEN | Monica’s numerical perception and comfort derive from her father’s teaching; she memorized his burning numbers as proof he lived and keeps his coffee pot. (V02) | See V02 reading section 9.1. | V02 evidence | Later reinterpretation, not correction. |

Revision records at V03, 2026-10-14, reviewer the V03 sequential integrator:

| Revision | Claim | Earlier formulation and boundary | Transition | New formulation and boundary | Reason | Affected homes | Kind |
|---|---|---|---|---|---|---|---|
| SW-CR-0019 | SW-C-0001 | Chantless casting began as avoidance of speech, and silence and mastery are one mechanism; the avoidance has an earlier root in childhood punishment for speaking, while the public account explains the capacity as instant computation. (V02) | REVISE | Chantless casting began as avoidance of speech, and silence and mastery are one mechanism; the avoidance has an earlier root in childhood punishment for speaking and a long silence before Minerva; its occasion was a friend’s plan to shorten her chant, which she carried to no chant; the public account explains the capacity as instant computation. (V03) | See V03 reading section 9.1. | V03 evidence | Later reinterpretation, not correction. |
| SW-CR-0020 | SW-C-0002 | Pain, fear or exposure drive Monica into numerical absorption; the habit began as a vow to keep her father’s numbers. (V02) | STRENGTHEN and REVISE | Pain, fear or exposure drive Monica into numerical absorption; the habit began as a vow to keep her father’s numbers, and she also uses it deliberately to compute combat and to make people bearable by turning them into numbers. (V03) | See V03 reading section 9.1. | V03 evidence | Later reinterpretation, not correction. |
| SW-CR-0021 | SW-C-0003 | The man in the V01 dream is Monica’s paternal uncle, who after her father’s execution beat her for reciting numbers and defending him and imposed silence about him in public. (V02) | STRENGTHEN | The man in the V01 dream is Monica’s paternal uncle, who after her father’s execution beat her repeatedly for reciting numbers and for stating the worth of her father’s work, and imposed silence about him in public; scars remain on her back and touch still frightens her. (V03) | See V03 reading section 9.1. | V03 evidence | Later reinterpretation, not correction. |
| SW-CR-0022 | SW-C-0004 | The makeweight self-assessment is contradicted by Louis’s memory of the duel; the examiners’ ranking is unstated. (V02) | PRESERVE | Unchanged (V03) | No material new evidence; see V03 reading section 9.1. | — | Review, not change. |
| SW-CR-0023 | SW-C-0005 | Stated protection; Monica doubts it; Louis reads surveillance, uses a decoy, chose Monica partly for her distrust of people, and calls himself first-prince because he dislikes the duke and Felix; the king is unshown. (V02) | STRENGTHEN | Stated protection; Monica doubts it; Louis reads surveillance, uses a decoy, chose Monica because she distrusts, fears and hates people and can therefore be merciless, and calls himself first-prince because he dislikes the duke and Felix; the king is unshown. (V03) | See V03 reading section 9.1. | V03 evidence | Later reinterpretation, not correction. |
| SW-CR-0024 | SW-C-0006 | The prologue’s watcher is Felix. (V02) | PRESERVE | Unchanged (V03) | No material new evidence; see V03 reading section 9.1. | — | Review, not change. |
| SW-CR-0025 | SW-C-0007 | Public and private selves diverge: he denies a talent for magic while studying it and hiding a spirit; he removes the duke’s placements while professing he cannot defy him; he must become king without wanting what is prepared for his name, holding the role while he bears it. (V02) | STRENGTHEN and partly REVISE | Public and private selves diverge: he denies a talent for magic while studying it in secret because it is forbidden to him, and hides a spirit; he obeys the duke outwardly while removing his placements and gathering nobles who resent him; he must become king without wanting it, under a ten-year vow to inscribe the name Felix Arc Ridill in history; his time outside the role is a remainder he spends at night. (V03) | See V03 reading section 9.1. | V03 evidence | Later reinterpretation, not correction. |
| SW-CR-0026 | SW-C-0008 | Felix has not identified Monica as the Silent Witch; at V02 exit he is searching the school for her and his search excludes Monica. (V02) | STRENGTHEN | Felix has not identified Monica as the Silent Witch; at V03 exit he admires the Witch’s magic as a first love, has never seen her face, spent the festival night with Monica, briefly suspected her of being an assassin, and still does not connect them. (V03) | See V03 reading section 9.1. | V03 evidence | Later reinterpretation, not correction. |
| SW-CR-0027 | SW-C-0009 | Cyril holds an unverified suspicion from her hand and remark (V01), and at V02 links the forest mage with the Silent Witch; V02 shows no renewed link to Monica. (V02) | PRESERVE; UNTESTED | Unchanged (V03) | No material new evidence; see V03 reading section 9.1. | — | Review, not change. |
| SW-CR-0028 | SW-C-0010 | Awe at Monica’s power is narrated through external focalizers; from V02 her own viewpoint also narrates her power, as calculation under constraint. (V02) | STRENGTHEN | Awe at Monica’s power is narrated through external focalizers; from V02 her own viewpoint also narrates her power, as calculation under constraint; V03 extends this to sustained combat computation and gives her first chantless casting from a rival’s view. (V03) | See V03 reading section 9.1. | V03 evidence | Later reinterpretation, not correction. |
| SW-CR-0029 | SW-C-0011 | The school treats rank as epistemic authority; Cyril’s inquiry is the first counterexample; at V02 rank is also used as a weapon of justice (Felix, Isabelle) and Elliott’s code ties rank to duty. (V02) | STRENGTHEN | The school treats rank as epistemic authority; Cyril’s inquiry is the first counterexample; at V02 rank is also used as a weapon of justice (Felix, Isabelle) and Elliott’s code ties rank to duty; at V03 Elliott’s contempt for upstarts has a biographical root and he warns that talent crossing class walls is envied or used. (V03) | See V03 reading section 9.1. | V03 evidence | Later reinterpretation, not correction. |
| SW-CR-0030 | SW-C-0012 | Organized embezzlement; erased Aaron’s and Cyril’s memories; Selma’s manipulation inferred. (V02) | PRESERVE | Unchanged (V03) | No material new evidence; see V03 reading section 9.1. | — | Review, not change. |
| SW-CR-0031 | SW-C-0013 | Neither an ordinary cat nor, in Felix’s judgment, a spirit. (V02) | PRESERVE | Unchanged (V03) | No material new evidence; see V03 reading section 9.1. | — | Review, not change. |
| SW-CR-0032 | SW-C-0014 | Monica regards her talent as a curse that took her father and friend; her father was executed as a heretic for forbidden research into the body as number, and the friend turned away when she mastered chantless magic. (V02) | REVISE | Monica regards her talent as a curse that took her father and friend; her father, Venedict Rain, was executed as a heretic for forbidden research on heredity and magical properties five years before the present, and his book was burned; the friend, Bernie Jones, needed her dependence, turned away in envy when she mastered chantless magic, and sent her to the hut; at V03 she renounces his approval. (V03) | See V03 reading section 9.1. | V03 evidence | Later reinterpretation, not correction. |
| SW-CR-0033 | SW-C-0015 | The bond with Lana rests on shared experience of being called boring and being out of place, and on mutual gestures of giving; Lana began from pride and stays from affection. (V02) | STRENGTHEN | The bond with Lana rests on shared experience of being called boring and being out of place, and on mutual gestures of giving; Lana began from pride and stays from affection; at V03 Lana arms and defends her, and Monica defends Lana first. (V03) | See V03 reading section 9.1. | V03 evidence | Later reinterpretation, not correction. |
| SW-CR-0034 | SW-C-0016 | The comedy of coercion registers harm in most cases; the non-consensual kiss is unevaluated and unknown to its recipient. (V02) | PRESERVE; kiss UNTESTED | Unchanged (V03) | No material new evidence; see V03 reading section 9.1. | — | Review, not change. |
| SW-CR-0035 | SW-C-0017 | Louis combines coercion with investment in her self-respect and his own pride; at V02 also gifts, an unknowing decoy, and a concession calculated to keep her cooperation. (V02) | STRENGTHEN | Louis combines coercion with investment in her self-respect and his own pride; at V02 also gifts, an unknowing decoy, and a concession calculated to keep her cooperation; at V03 he lends Lynn and, to Casey, judges her a heartless witch. (V03) | See V03 reading section 9.1. | V03 evidence | Later reinterpretation, not correction. |
| SW-CR-0036 | SW-C-0018 | Monica’s numerical perception and comfort derive from her father’s teaching; she memorized his burning numbers as proof he lived and keeps his coffee pot. (V02) | STRENGTHEN | Monica’s numerical perception and comfort derive from her father’s teaching; she memorized his burning numbers as proof he lived and keeps his coffee pot; his book opens with the sentence that the world is made of numbers. (V03) | See V03 reading section 9.1. | V03 evidence | Later reinterpretation, not correction. |
| SW-CR-0037 | SW-C-0019 | Casey Grove is the prologue’s unnamed conspirator, acting on Count Bright’s order with a 螺炎, from grievance at central neglect and gratitude to Randall; her friendship was begun instrumentally and its later reality is left ambivalent. (V02) | STRENGTHEN and partly REVISE | Casey Grove is the prologue’s unnamed conspirator, acting on Count Bright’s order with a 螺炎, from grievance at central neglect and gratitude to Randall; her friendship was begun instrumentally; at V03 Count Bright claims sole responsibility, Louis suspects Randall and the Empire, and Casey asks after Monica and sends her a package, so that her feeling is evidenced as concern and its history remains OPEN. (V03) | See V03 reading section 9.1. | V03 evidence | Later reinterpretation, not correction. |
| SW-CR-0038 | SW-C-0020 | Monica derives a concept of duty from Elliott’s noblesse oblige and transposes it to her roles as treasurer and Sage; the climax is narrated as acceptance of the title as responsibility. (V02) | REVISE | Monica derives a concept of duty from Elliott’s noblesse oblige and transposes it to her roles as treasurer and Sage; at V03 duty is joined by a personal motive she calls selfish, that the bereaved be able to mourn as she could not. (V03) | See V03 reading section 9.1. | V03 evidence | Later reinterpretation, not correction. |
| SW-CR-0039 | SW-C-0021 | Monica’s concealment is a political bargain using Louis’s factional logic, at a cost to Cyril and her conscience; the volume presents it sympathetically and leaves its justice unjudged. (V02) | STRENGTHEN | Monica’s concealment is a political bargain using Louis’s factional logic, at a cost to Cyril and her conscience; the volume presents it sympathetically and leaves its justice unjudged; at V03 Cyril still blames himself and she cannot clear him. (V03) | See V03 reading section 9.1. | V03 evidence | Later reinterpretation, not correction. |
| SW-CR-0040 | SW-C-0022 | A cluster of unexplained details surrounds Felix’s identity and history: Bridget’s childhood test, his memory of a boy apologizing as a royal, the role held while he bears the name, the seer’s blindness to his star. No hypothesis is registered. (V02) | STRENGTHEN in scope | A cluster of unexplained details surrounds Felix’s identity and history: Bridget’s childhood test; his memory of a boy apologizing as a royal; the role held while he bears the name; the seer’s blindness to his star from about ten years ago; Elliott’s memory of a sickly, clumsy, shy, light-eyed, star-loving child scarred in the side with a more poised attendant; a ten-year vow to inscribe the name in history; a dead friend whose wish he pursues; a dream of a boy called Felix, a page and a burned astronomy book; a necessary scar. No hypothesis is registered. (V03) | See V03 reading section 9.1. | V03 evidence | Later reinterpretation, not correction. |
| SW-CR-0041 | SW-C-0023 | Monica says she cannot expect anything of anyone or be absorbed in anyone, while her conduct shows growing attachment; no romantic interest on her side is shown; Felix’s first-love-like absorption is directed at the Silent Witch as an idea. (V02) | STRENGTHEN | Monica says she cannot expect anything of anyone or be absorbed in anyone, while her conduct shows growing attachment; no romantic interest on her side is shown; Felix’s first-love-like absorption is directed at the Silent Witch as an idea; the festival night is shown as companionship, mourning and play, and she tells him she wants nothing from him. (V03) | See V03 reading section 9.1. | V03 evidence | Later reinterpretation, not correction. |
| SW-CR-0042 | SW-C-0024 | Louis chose Monica partly for her distrust of people and reads her attachment as a risk; Monica shares the warning that Monica Norton is temporary. (V02) | STRENGTHEN | Louis chose Monica for her distrust, fear and hatred of people, calls her heartless, and reads her attachment as a risk; Monica shares the warning that Monica Norton is temporary, and at V03 expected her false school life to end. (V03) | See V03 reading section 9.1. | V03 evidence | Later reinterpretation, not correction. |
| SW-CR-0043 | SW-C-0025 | Isabelle’s cover-bullying is a deliberate deterrence policy and her revenge mirrors the crime; the volume treats humiliation as justice. (V02) | PRESERVE | Unchanged (V03) | No material new evidence; see V03 reading section 9.1. | — | Review, not change. |
| SW-CR-0044 | SW-C-0026 | 場違い organizes the social plot through three outsiders by class or region, Monica, Lana and Casey, reversing from exclusion to self-gift. (V02) | PRESERVE | Unchanged (V03) | No material new evidence; see V03 reading section 9.1. | — | Review, not change. |

Revision records at V04, 2026-10-14, reviewer the V04 sequential integrator:

| Revision | Claim | Earlier formulation and boundary | Transition | New formulation and boundary | Reason | Affected homes | Kind |
|---|---|---|---|---|---|---|---|
| SW-CR-0045 | SW-C-0001 | Chantless casting began as avoidance of speech, and silence and mastery are one mechanism; the avoidance has an earlier root in childhood punishment for speaking and a long silence before Minerva; its occasion was a friend’s plan to shorten her chant, which she carried to no chant; the public account explains the capacity as instant computation. (V03) | REVISE | Chantless casting began as avoidance of speech, and silence and mastery are one mechanism; the avoidance has an earlier root in childhood punishment for speaking; before Minerva a year of abuse produced a dissociation in which she lost language, ended by Hilda Everett’s rescue; its occasion at Minerva was a friend’s plan to shorten her chant; the public account explains the capacity as instant computation. (V04) | See V04 reading section 9.1. | V04 evidence | Later reinterpretation, not correction. |
| SW-CR-0046 | SW-C-0002 | Pain, fear or exposure drive Monica into numerical absorption; the habit began as a vow to keep her father’s numbers, and she also uses it deliberately to compute combat and to make people bearable by turning them into numbers. (V03) | REVISE | Pain, fear or exposure drive Monica into numerical absorption; the habit began as a child’s escape from her uncle into her father’s formulas and a vow to keep his numbers; she also uses it deliberately to compute combat and to bear people, and it fails when people she knows are threatened. (V04) | See V04 reading section 9.1. | V04 evidence | Later reinterpretation, not correction. |
| SW-CR-0047 | SW-C-0003 | The man in the V01 dream is Monica’s paternal uncle, who after her father’s execution beat her repeatedly for reciting numbers and for stating the worth of her father’s work, and imposed silence about him in public; scars remain on her back and touch still frightens her. (V03) | REVISE | Monica’s paternal uncle, after her father’s execution when she was ten, beat and starved her, shut her in a winter barn and forbade her to defend her father, for about a year until Hilda Everett took her; scars remain and touch still frightens her. (V04) | See V04 reading section 9.1. | V04 evidence | Later reinterpretation, not correction. |
| SW-CR-0048 | SW-C-0004 | The makeweight self-assessment is contradicted by Louis’s memory of the duel; the examiners’ ranking is unstated. (V03) | PRESERVE | Unchanged (V04) | See V04 reading section 9.1. | — | Review, not change. |
| SW-CR-0049 | SW-C-0005 | Stated protection; Monica doubts it; Louis reads surveillance, uses a decoy, chose Monica because she distrusts, fears and hates people and can therefore be merciless, and calls himself first-prince because he dislikes the duke and Felix; the king is unshown. (V03) | STRENGTHEN | Unchanged (V04) | See V04 reading section 9.1. | — | Review, not change. |
| SW-CR-0050 | SW-C-0006 | The prologue’s watcher is Felix. (V03) | PRESERVE | Unchanged (V04) | See V04 reading section 9.1. | — | Review, not change. |
| SW-CR-0051 | SW-C-0007 | Public and private selves diverge: he denies a talent for magic while studying it in secret because it is forbidden to him, and hides a spirit; he obeys the duke outwardly while removing his placements and gathering nobles who resent him; he must become king without wanting it, under a ten-year vow to inscribe the name Felix Arc Ridill in history; his time outside the role is a remainder he spends at night. (V03) | STRENGTHEN | Public and private selves diverge: he denies a talent for magic while studying it in secret because it is forbidden to him, and hides a spirit; he obeys the duke outwardly while removing his placements and gathering nobles who resent him; he must become king without wanting it, under a ten-year vow to make the name Felix Arc Ridill remembered, which he now expresses as a hero’s posthumous light and pursues even against his dead friend’s wish. (V04) | See V04 reading section 9.1. | V04 evidence | Later reinterpretation, not correction. |
| SW-CR-0052 | SW-C-0008 | Felix has not identified Monica as the Silent Witch; at V03 exit he admires the Witch’s magic as a first love, has never seen her face, spent the festival night with Monica, briefly suspected her of being an assassin, and still does not connect them. (V03) | STRENGTHEN | Unchanged (V04) | See V04 reading section 9.1. | — | Review, not change. |
| SW-CR-0053 | SW-C-0009 | Cyril holds an unverified suspicion from her hand and remark (V01), and at V02 links the forest mage with the Silent Witch; V02 shows no renewed link to Monica. (V03) | REVISE | Cyril holds an unverified suspicion from her hand and remark (V01), links the forest mage with the Silent Witch (V02), and at V04 notices unexplained magical ice and her small, pen-callused hand; no conclusion is shown. (V04) | See V04 reading section 9.1. | V04 evidence | Later reinterpretation, not correction. |
| SW-CR-0054 | SW-C-0010 | Awe at Monica’s power is narrated through external focalizers; from V02 her own viewpoint also narrates her power, as calculation under constraint; V03 extends this to sustained combat computation and gives her first chantless casting from a rival’s view. (V03) | STRENGTHEN | Unchanged (V04) | See V04 reading section 9.1. | — | Review, not change. |
| SW-CR-0055 | SW-C-0011 | The school treats rank as epistemic authority; Cyril’s inquiry is the first counterexample; at V02 rank is also used as a weapon of justice (Felix, Isabelle) and Elliott’s code ties rank to duty; at V03 Elliott’s contempt for upstarts has a biographical root and he warns that talent crossing class walls is envied or used. (V03) | STRENGTHEN | Unchanged (V04) | See V04 reading section 9.1. | — | Review, not change. |
| SW-CR-0056 | SW-C-0012 | Organized embezzlement; erased Aaron’s and Cyril’s memories; Selma’s manipulation inferred. (V03) | REVISE | Organized embezzlement; erased Aaron’s and Cyril’s memories; Selma’s manipulation inferred; at V04 a traitor curse-caster reveals that Thornley worked for a patron called 閣下 through mind interference and was discarded. (V04) | See V04 reading section 9.1. | V04 evidence | Later reinterpretation, not correction. |
| SW-CR-0057 | SW-C-0013 | Neither an ordinary cat nor, in Felix’s judgment, a spirit. (V03) | STRENGTHEN | Neither an ordinary cat nor, in Felix’s judgment, a spirit; drug-immune, with a reptilian hiss and slit pupils, his human shape slipping in rage; a spirit finds him an anomalous familiar. Nature undisclosed. (V04) | See V04 reading section 9.1. | V04 evidence | Later reinterpretation, not correction. |
| SW-CR-0058 | SW-C-0014 | Monica regards her talent as a curse that took her father and friend; her father, Venedict Rain, was executed as a heretic for forbidden research on heredity and magical properties five years before the present, and his book was burned; the friend, Bernie Jones, needed her dependence, turned away in envy when she mastered chantless magic, and sent her to the hut; at V03 she renounces his approval. (V03) | REVISE | Monica regards her talent as a curse that took her father and friend; her father, Venedict Rain, author of a book on heredity and magical properties, was executed as a heretic when Monica was ten and his book burned; the friend, Bernie Jones, needed her dependence, turned away in envy, sent her to the hut, and wanted to be her equal rival; she has renounced his approval. Correction: the V03 formulation dated the execution five years before the present, but the V03 text dates only the book’s publication. (V04) | See V04 reading section 9.1. | V04 evidence | Correction of the V03 formulation and later reinterpretation. |
| SW-CR-0059 | SW-C-0015 | The bond with Lana rests on shared experience of being called boring and being out of place, and on mutual gestures of giving; Lana began from pride and stays from affection; at V03 Lana arms and defends her, and Monica defends Lana first. (V03) | STRENGTHEN | Unchanged (V04) | See V04 reading section 9.1. | — | Review, not change. |
| SW-CR-0060 | SW-C-0016 | The comedy of coercion registers harm in most cases; the non-consensual kiss is unevaluated and unknown to its recipient. (V03) | PRESERVE; kiss UNTESTED | Unchanged (V04) | See V04 reading section 9.1. | — | Review, not change. |
| SW-CR-0061 | SW-C-0017 | Louis combines coercion with investment in her self-respect and his own pride; at V02 also gifts, an unknowing decoy, and a concession calculated to keep her cooperation; at V03 he lends Lynn and, to Casey, judges her a heartless witch. (V03) | STRENGTHEN | Unchanged (V04) | See V04 reading section 9.1. | — | Review, not change. |
| SW-CR-0062 | SW-C-0018 | Monica’s numerical perception and comfort derive from her father’s teaching; she memorized his burning numbers as proof he lived and keeps his coffee pot; his book opens with the sentence that the world is made of numbers. (V03) | REVISE | Monica’s numerical perception and comfort derive from her father’s teaching; his saying that the world is made of numbers became her means of fleeing reality under her uncle; she memorized his burning numbers and keeps his coffee pot; at V04 she refuses the saying as an excuse. (V04) | See V04 reading section 9.1. | V04 evidence | Later reinterpretation, not correction. |
| SW-CR-0063 | SW-C-0019 | Casey Grove is the prologue’s unnamed conspirator, acting on Count Bright’s order with a 螺炎, from grievance at central neglect and gratitude to Randall; her friendship was begun instrumentally; at V03 Count Bright claims sole responsibility, Louis suspects Randall and the Empire, and Casey asks after Monica and sends her a package, so that her feeling is evidenced as concern and its history remains OPEN. (V03) | STRENGTHEN | Unchanged (V04) | See V04 reading section 9.1. | — | Review, not change. |
| SW-CR-0064 | SW-C-0020 | Monica derives a concept of duty from Elliott’s noblesse oblige and transposes it to her roles as treasurer and Sage; at V03 duty is joined by a personal motive she calls selfish, that the bereaved be able to mourn as she could not. (V03) | STRENGTHEN | Unchanged (V04) | See V04 reading section 9.1. | — | Review, not change. |
| SW-CR-0065 | SW-C-0021 | Monica’s concealment is a political bargain using Louis’s factional logic, at a cost to Cyril and her conscience; the volume presents it sympathetically and leaves its justice unjudged; at V03 Cyril still blames himself and she cannot clear him. (V03) | PRESERVE | Unchanged (V04) | See V04 reading section 9.1. | — | Review, not change. |
| SW-CR-0066 | SW-C-0022 | A cluster of unexplained details surrounds Felix’s identity and history: Bridget’s childhood test; his memory of a boy apologizing as a royal; the role held while he bears the name; the seer’s blindness to his star from about ten years ago; Elliott’s memory of a sickly, clumsy, shy, light-eyed, star-loving child scarred in the side with a more poised attendant; a ten-year vow to inscribe the name in history; a dead friend whose wish he pursues; a dream of a boy called Felix, a page and a burned astronomy book; a necessary scar. No hypothesis is registered. (V03) | STRENGTHEN in scope | Unchanged (V04) | See V04 reading section 9.1. | — | Review, not change. |
| SW-CR-0067 | SW-C-0023 | Monica says she cannot expect anything of anyone or be absorbed in anyone, while her conduct shows growing attachment; no romantic interest on her side is shown; Felix’s first-love-like absorption is directed at the Silent Witch as an idea; the festival night is shown as companionship, mourning and play, and she tells him she wants nothing from him. (V03) | REVISE | Monica says she cannot expect anything of anyone, while her conduct shows growing attachment; no romantic interest on her side is shown and she does not wish to marry; Felix’s absorption in the Silent Witch as an idea is now joined, in his own viewpoint, by attachment and jealousy toward Monica herself. (V04) | See V04 reading section 9.1. | V04 evidence | Later reinterpretation, not correction. |
| SW-CR-0068 | SW-C-0024 | Louis chose Monica for her distrust, fear and hatred of people, calls her heartless, and reads her attachment as a risk; Monica shares the warning that Monica Norton is temporary, and at V03 expected her false school life to end. (V03) | STRENGTHEN | Unchanged (V04) | See V04 reading section 9.1. | — | Review, not change. |
| SW-CR-0069 | SW-C-0025 | Isabelle’s cover-bullying is a deliberate deterrence policy and her revenge mirrors the crime; the volume treats humiliation as justice. (V03) | STRENGTHEN | Unchanged (V04) | See V04 reading section 9.1. | — | Review, not change. |
| SW-CR-0070 | SW-C-0026 | 場違い organizes the social plot through three outsiders by class or region, Monica, Lana and Casey, reversing from exclusion to self-gift. (V03) | STRENGTHEN | Unchanged (V04) | See V04 reading section 9.1. | — | Review, not change. |
| SW-CR-0071 | SW-C-0027 | Bernie Jones is the Minerva friend; his help coexisted with a wish for her dependence; his envy ended the friendship and his curse began the hut life; in V03 he protects her cover while demanding gratitude. (V03) | REVISE | Bernie Jones is the Minerva friend; his help coexisted with a wish for her dependence; his envy ended the friendship and his curse began the hut life; he protected her cover as a noble’s duty, wanted to be her equal rival, and leaves Minerva as heir offering future help. (V04) | See V04 reading section 9.1. | V04 evidence | Later reinterpretation, not correction. |
| SW-CR-0072 | SW-C-0028 | Mourning organizes V03: Monica’s motive in the climax is that the bereaved be able to mourn as she could not; burned books and festival bells join her strand and Felix’s. (V03) | PRESERVE | Unchanged (V04) | See V04 reading section 9.1. | — | Review, not change. |
| SW-CR-0073 | SW-C-0029 | Ike is a persona in which Felix shows Monica a self outside his role; her answering self-description as a ghost is her first outreach; he ends the persona with a gift framed as possession and farewell. (V03) | REVISE | Ike is a persona in which Felix shows Monica a self outside his role; her answering self-description as a ghost was her first outreach; the persona persists in private moments after the festival night, and Monica keeps its confidences from Louis. (V04) | See V04 reading section 9.1. | V04 evidence | Later reinterpretation, not correction. |
| SW-CR-0074 | SW-C-0030 | The duke dominates Felix by contempt and, in Felix’s dream, by punishing those the boy cares for; Felix obeys outwardly while gathering nobles who resent the duke. (V03) | STRENGTHEN | Unchanged (V04) | See V04 reading section 9.1. | — | Review, not change. |
| SW-CR-0075 | SW-C-0031 | Yuan used imperial body magic, escaped by a staged suicide with the real Pittman’s body, and with Heidi has commissioned a forged Serendia uniform for the festival; Louis suspects a Randall–Empire alliance behind the 螺炎. (V03) | REVISE | Imperial agents Yuan and Heidi, serving a master, used imperial body magic, impersonated Pittman and then Cyril, sought a trace on Felix that Yuan attributes to a traitor Arthur and the capture of the Silent Witch, threatened war, and escaped with Yuan cursed for at least a month; Louis suspects a Randall–Empire alliance. (V04) | See V04 reading section 9.1. | V04 evidence | Later reinterpretation, not correction. |
| SW-CR-0076 | SW-C-0032 | Monica’s father was Venedict Rain, author of a book on heredity and magical properties, executed for forbidden research five years before the present; his friend Porter is the novelist Dustin Günther; the character card gives Rain as Monica’s former surname. (V03) | REVISE | Monica’s father was Venedict Rain, author of a book on heredity and magical properties, executed for forbidden research when Monica was ten; his former assistant Hilda Everett adopted her; his friend Porter is Dustin Günther; a traitor curse-caster knew and hated him. Correction: the V03 formulation dated the execution five years before the present; the V03 text dates only the book’s publication, and the two dates are in tension. (V04) | See V04 reading section 9.1. | V04 evidence | Correction of the V03 formulation and later reinterpretation. |
| SW-CR-0077 | SW-C-0033 | Louis’s model of Monica as a heartless witch who fears and hates people is half right, is contradicted by the volume’s narrative, and is the explicit ground of his choice of her. (V03) | REVISE | Louis’s model of Monica as a heartless witch who sees people as numbers is half right: she accepts it and uses it as a technique, then fails to apply it to the people she knows; Louis says her humanity does not matter to him either way. (V04) | See V04 reading section 9.1. | V04 evidence | Later reinterpretation, not correction. |
| SW-CR-0078 | SW-C-0034 | Mary deliberately allowed the theft of the ancient tool, citing the stars’ guidance, and used the crisis to test Monica; the volume does not judge the risk to the town or the bystander. (V03) | PRESERVE | Unchanged (V04) | See V04 reading section 9.1. | — | Review, not change. |

Revision records at AFTER04, 2026-10-14, reviewer the AFTER04 sequential integrator:

| Revision | Claim | Earlier formulation and boundary | Transition | New formulation and boundary | Reason | Affected homes | Kind |
|---|---|---|---|---|---|---|---|
| SW-CR-0079 | SW-C-0001 | Chantless casting began as avoidance of speech, and silence and mastery are one mechanism; the avoidance has an earlier root in childhood punishment for speaking; before Minerva a year of abuse produced a dissociation in which she lost language, ended by Hilda Everett’s rescue; its occasion at Minerva was a friend’s plan to shorten her chant; the public account explains the capacity as instant computation. (V04) | STRENGTHEN | Wording unchanged; support extended (AFTER04) | First plain requests and thanks; the courage speech costs (AFTER04 obs. 147, 157, 160). | SW-S, SW-R as in the AFTER04 records | Strengthened by companion evidence. |
| SW-CR-0080 | SW-C-0002 | Pain, fear or exposure drive Monica into numerical absorption; the habit began as a child’s escape from her uncle into her father’s formulas and a vow to keep his numbers; she also uses it deliberately to compute combat and to bear people, and it fails when people she knows are threatened. (V04) | PRESERVE | Unchanged (AFTER04) | See AFTER04 reading section 9.1. | — | Review, not change. |
| SW-CR-0081 | SW-C-0003 | Monica’s paternal uncle, after her father’s execution when she was ten, beat and starved her, shut her in a winter barn and forbade her to defend her father, for about a year until Hilda Everett took her; scars remain and touch still frightens her. (V04) | PRESERVE | Unchanged (AFTER04) | See AFTER04 reading section 9.1. | — | Review, not change. |
| SW-CR-0082 | SW-C-0004 | The makeweight self-assessment is contradicted by Louis’s memory of the duel; the examiners’ ranking is unstated. (V04) | PRESERVE | Unchanged (AFTER04) | See AFTER04 reading section 9.1. | — | Review, not change. |
| SW-CR-0083 | SW-C-0005 | Stated protection; Monica doubts it; Louis reads surveillance, uses a decoy, chose Monica because she distrusts, fears and hates people and can therefore be merciless, and calls himself first-prince because he dislikes the duke and Felix; the king is unshown. (V04) | PRESERVE | Unchanged (AFTER04) | See AFTER04 reading section 9.1. | — | Review, not change. |
| SW-CR-0084 | SW-C-0006 | The prologue’s watcher is Felix. (V04) | PRESERVE | Unchanged (AFTER04) | See AFTER04 reading section 9.1. | — | Review, not change. |
| SW-CR-0085 | SW-C-0007 | Public and private selves diverge: he denies a talent for magic while studying it in secret because it is forbidden to him, and hides a spirit; he obeys the duke outwardly while removing his placements and gathering nobles who resent him; he must become king without wanting it, under a ten-year vow to make the name Felix Arc Ridill remembered, which he now expresses as a hero’s posthumous light and pursues even against his dead friend’s wish. (V04) | STRENGTHEN | Wording unchanged; support extended (AFTER04) | The grandfather’s surveillance of his reading; the childhood interlude (AFTER04 obs. 035, 122, 123). | SW-S, SW-R as in the AFTER04 records | Strengthened by companion evidence. |
| SW-CR-0086 | SW-C-0008 | Felix has not identified Monica as the Silent Witch; at V03 exit he admires the Witch’s magic as a first love, has never seen her face, spent the festival night with Monica, briefly suspected her of being an assassin, and still does not connect them. (V04) | PRESERVE | Unchanged (AFTER04) | See AFTER04 reading section 9.1. | — | Review, not change. |
| SW-CR-0087 | SW-C-0009 | Cyril holds an unverified suspicion from her hand and remark (V01), links the forest mage with the Silent Witch (V02), and at V04 notices unexplained magical ice and her small, pen-callused hand; no conclusion is shown. (V04) | PRESERVE | Unchanged (AFTER04) | See AFTER04 reading section 9.1. | — | Review, not change. |
| SW-CR-0088 | SW-C-0010 | Awe at Monica’s power is narrated through external focalizers; from V02 her own viewpoint also narrates her power, as calculation under constraint; V03 extends this to sustained combat computation and gives her first chantless casting from a rival’s view. (V04) | STRENGTHEN | Wording unchanged; support extended (AFTER04) | Power seen only by a spirit and the reader (AFTER04 obs. 092, 095, 116). | SW-S, SW-R as in the AFTER04 records | Strengthened by companion evidence. |
| SW-CR-0089 | SW-C-0011 | The school treats rank as epistemic authority; Cyril’s inquiry is the first counterexample; at V02 rank is also used as a weapon of justice (Felix, Isabelle) and Elliott’s code ties rank to duty; at V03 Elliott’s contempt for upstarts has a biographical root and he warns that talent crossing class walls is envied or used. (V04) | STRENGTHEN | Wording unchanged; support extended (AFTER04) | Elliott’s creed and its origin; Eliane’s reasoning (AFTER04 obs. 112, 130). | SW-S, SW-R as in the AFTER04 records | Strengthened by companion evidence. |
| SW-CR-0090 | SW-C-0012 | Organized embezzlement; erased Aaron’s and Cyril’s memories; Selma’s manipulation inferred; at V04 a traitor curse-caster reveals that Thornley worked for a patron called 閣下 through mind interference and was discarded. (V04) | PRESERVE | Unchanged (AFTER04) | See AFTER04 reading section 9.1. | — | Review, not change. |
| SW-CR-0091 | SW-C-0013 | Neither an ordinary cat nor, in Felix’s judgment, a spirit; drug-immune, with a reptilian hiss and slit pupils, his human shape slipping in rage; a spirit finds him an anomalous familiar. Nature undisclosed. (V04) | PRESERVE | Unchanged (AFTER04) | See AFTER04 reading section 9.1. | — | Review, not change. |
| SW-CR-0092 | SW-C-0014 | Monica regards her talent as a curse that took her father and friend; her father, Venedict Rain, author of a book on heredity and magical properties, was executed as a heretic when Monica was ten and his book burned; the friend, Bernie Jones, needed her dependence, turned away in envy, sent her to the hut, and wanted to be her equal rival; she has renounced his approval. Correction: the V03 formulation dated the execution five years before the present, but the V03 text dates only the book’s publication. (V04) | PRESERVE | Unchanged (AFTER04) | See AFTER04 reading section 9.1. | — | Review, not change. |
| SW-CR-0093 | SW-C-0015 | The bond with Lana rests on shared experience of being called boring and being out of place, and on mutual gestures of giving; Lana began from pride and stays from affection; at V03 Lana arms and defends her, and Monica defends Lana first. (V04) | STRENGTHEN | Wording unchanged; support extended (AFTER04) | Birthday cake and handmade pouch (AFTER04 obs. 146, 147). | SW-S, SW-R as in the AFTER04 records | Strengthened by companion evidence. |
| SW-CR-0094 | SW-C-0016 | The comedy of coercion registers harm in most cases; the non-consensual kiss is unevaluated and unknown to its recipient. (V04) | STRENGTHEN | Wording unchanged; support extended (AFTER04) | Comic register over capital danger and tyranny (AFTER04 reading sections 8.3, 8.4). | SW-S, SW-R as in the AFTER04 records | Strengthened by companion evidence. |
| SW-CR-0095 | SW-C-0017 | Louis combines coercion with investment in her self-respect and his own pride; at V02 also gifts, an unknowing decoy, and a concession calculated to keep her cooperation; at V03 he lends Lynn and, to Casey, judges her a heartless witch. (V04) | STRENGTHEN | Wording unchanged; support extended (AFTER04) | Tyranny, praise and a creed of strength, retrospective (AFTER04 obs. 007, 010, 099). | SW-S, SW-R as in the AFTER04 records | Strengthened by companion evidence. |
| SW-CR-0096 | SW-C-0018 | Monica’s numerical perception and comfort derive from her father’s teaching; his saying that the world is made of numbers became her means of fleeing reality under her uncle; she memorized his burning numbers and keeps his coffee pot; at V04 she refuses the saying as an excuse. (V04) | PRESERVE | Unchanged (AFTER04) | See AFTER04 reading section 9.1. | — | Review, not change. |
| SW-CR-0097 | SW-C-0019 | Casey Grove is the prologue’s unnamed conspirator, acting on Count Bright’s order with a 螺炎, from grievance at central neglect and gratitude to Randall; her friendship was begun instrumentally; at V03 Count Bright claims sole responsibility, Louis suspects Randall and the Empire, and Casey asks after Monica and sends her a package, so that her feeling is evidenced as concern and its history remains OPEN. (V04) | PRESERVE | Unchanged (AFTER04) | See AFTER04 reading section 9.1. | — | Review, not change. |
| SW-CR-0098 | SW-C-0020 | Monica derives a concept of duty from Elliott’s noblesse oblige and transposes it to her roles as treasurer and Sage; at V03 duty is joined by a personal motive she calls selfish, that the bereaved be able to mourn as she could not. (V04) | STRENGTHEN | Wording unchanged; support extended (AFTER04) | Her own claim to her council standing (AFTER04 obs. 077). | SW-S, SW-R as in the AFTER04 records | Strengthened by companion evidence. |
| SW-CR-0099 | SW-C-0021 | Monica’s concealment is a political bargain using Louis’s factional logic, at a cost to Cyril and her conscience; the volume presents it sympathetically and leaves its justice unjudged; at V03 Cyril still blames himself and she cannot clear him. (V04) | PRESERVE | Unchanged (AFTER04) | See AFTER04 reading section 9.1. | — | Review, not change. |
| SW-CR-0100 | SW-C-0022 | A cluster of unexplained details surrounds Felix’s identity and history: Bridget’s childhood test; his memory of a boy apologizing as a royal; the role held while he bears the name; the seer’s blindness to his star from about ten years ago; Elliott’s memory of a sickly, clumsy, shy, light-eyed, star-loving child scarred in the side with a more poised attendant; a ten-year vow to inscribe the name in history; a dead friend whose wish he pursues; a dream of a boy called Felix, a page and a burned astronomy book; a necessary scar. No hypothesis is registered. (V04) | STRENGTHEN | Wording unchanged; support extended (AFTER04) | The childhood interlude; the attendant form on the card as paratext; no hypothesis registered (AFTER04 reading section 6.10). | SW-S, SW-R as in the AFTER04 records | Strengthened by companion evidence. |
| SW-CR-0101 | SW-C-0023 | Monica says she cannot expect anything of anyone, while her conduct shows growing attachment; no romantic interest on her side is shown and she does not wish to marry; Felix’s absorption in the Silent Witch as an idea is now joined, in his own viewpoint, by attachment and jealousy toward Monica herself. (V04) | PRESERVE | Unchanged (AFTER04) | See AFTER04 reading section 9.1. | — | Review, not change. |
| SW-CR-0102 | SW-C-0024 | Louis chose Monica for her distrust, fear and hatred of people, calls her heartless, and reads her attachment as a risk; Monica shares the warning that Monica Norton is temporary, and at V03 expected her false school life to end. (V04) | STRENGTHEN | Wording unchanged; support extended (AFTER04) | Lana’s birthday marked as one she can still attend (AFTER04 obs. 148). | SW-S, SW-R as in the AFTER04 records | Strengthened by companion evidence. |
| SW-CR-0103 | SW-C-0025 | Isabelle’s cover-bullying is a deliberate deterrence policy and her revenge mirrors the crime; the volume treats humiliation as justice. (V04) | STRENGTHEN | Wording unchanged; support extended (AFTER04) | The villainy’s origin and its use as investigation (AFTER04 obs. 140–142, 151). | SW-S, SW-R as in the AFTER04 records | Strengthened by companion evidence. |
| SW-CR-0104 | SW-C-0026 | 場違い organizes the social plot through three outsiders by class or region, Monica, Lana and Casey, reversing from exclusion to self-gift. (V04) | PRESERVE | Unchanged (AFTER04) | See AFTER04 reading section 9.1. | — | Review, not change. |
| SW-CR-0105 | SW-C-0027 | Bernie Jones is the Minerva friend; his help coexisted with a wish for her dependence; his envy ended the friendship and his curse began the hut life; he protected her cover as a noble’s duty, wanted to be her equal rival, and leaves Minerva as heir offering future help. (V04) | PRESERVE | Unchanged (AFTER04) | See AFTER04 reading section 9.1. | — | Review, not change. |
| SW-CR-0106 | SW-C-0028 | Mourning organizes V03: Monica’s motive in the climax is that the bereaved be able to mourn as she could not; burned books and festival bells join her strand and Felix’s. (V04) | PRESERVE | Unchanged (AFTER04) | See AFTER04 reading section 9.1. | — | Review, not change. |
| SW-CR-0107 | SW-C-0029 | Ike is a persona in which Felix shows Monica a self outside his role; her answering self-description as a ghost was her first outreach; the persona persists in private moments after the festival night, and Monica keeps its confidences from Louis. (V04) | STRENGTHEN | Wording unchanged; support extended (AFTER04) | Ike in daylight; a card to the fellow delinquent (AFTER04 obs. 043, 149). | SW-S, SW-R as in the AFTER04 records | Strengthened by companion evidence. |
| SW-CR-0108 | SW-C-0030 | The duke dominates Felix by contempt and, in Felix’s dream, by punishing those the boy cares for; Felix obeys outwardly while gathering nobles who resent the duke. (V04) | STRENGTHEN | Wording unchanged; support extended (AFTER04) | Surveillance of the prince’s reading (AFTER04 obs. 035). | SW-S, SW-R as in the AFTER04 records | Strengthened by companion evidence. |
| SW-CR-0109 | SW-C-0031 | Imperial agents Yuan and Heidi, serving a master, used imperial body magic, impersonated Pittman and then Cyril, sought a trace on Felix that Yuan attributes to a traitor Arthur and the capture of the Silent Witch, threatened war, and escaped with Yuan cursed for at least a month; Louis suspects a Randall–Empire alliance. (V04) | PRESERVE | Unchanged (AFTER04) | See AFTER04 reading section 9.1. | — | Review, not change. |
| SW-CR-0110 | SW-C-0032 | Monica’s father was Venedict Rain, author of a book on heredity and magical properties, executed for forbidden research when Monica was ten; his former assistant Hilda Everett adopted her; his friend Porter is Dustin Günther; a traitor curse-caster knew and hated him. Correction: the V03 formulation dated the execution five years before the present; the V03 text dates only the book’s publication, and the two dates are in tension. (V04) | PRESERVE | Unchanged (AFTER04) | See AFTER04 reading section 9.1. | — | Review, not change. |
| SW-CR-0111 | SW-C-0033 | Louis’s model of Monica as a heartless witch who sees people as numbers is half right: she accepts it and uses it as a technique, then fails to apply it to the people she knows; Louis says her humanity does not matter to him either way. (V04) | PRESERVE | Unchanged (AFTER04) | See AFTER04 reading section 9.1. | — | Review, not change. |
| SW-CR-0112 | SW-C-0034 | Mary deliberately allowed the theft of the ancient tool, citing the stars’ guidance, and used the crisis to test Monica; the volume does not judge the risk to the town or the bystander. (V04) | PRESERVE | Unchanged (AFTER04) | See AFTER04 reading section 9.1. | — | Review, not change. |
| SW-CR-0113 | SW-C-0035 | Monica’s numerical dissociation, born of abuse, is now both a chosen weapon and a limit: it fails when the people of the school are at stake, and she chooses to remain Monica Norton while knowing it deceives her friends. (V04) | STRENGTHEN | Wording unchanged; support extended (AFTER04) | The drawer of gifts from people she will leave (AFTER04 obs. 067, 149). | SW-S, SW-R as in the AFTER04 records | Strengthened by companion evidence. |
| SW-CR-0114 | SW-C-0036 | V04 is organized by gifts whose meaning differs between giver and receiver: the rose, the cursed necklace, the pendant, the handkerchief and the friend’s wish. (V04) | STRENGTHEN | Wording unchanged; support extended (AFTER04) | Louis’s instruction misread; the rose as charm; the corsage misread (AFTER04 obs. 066, 151, 159). | SW-S, SW-R as in the AFTER04 records | Strengthened by companion evidence. |
| SW-CR-0115 | SW-C-0037 | Cyril’s history mirrors Monica’s: a violent father, withheld praise and striving for recognition; his care for her is a disguised invitation and practical help, and his attention returns to her hand. (V04) | STRENGTHEN | Wording unchanged; support extended (AFTER04) | Isolation at fourteen; earned pride; sincere duel (AFTER04 obs. 069, 079, 109). | SW-S, SW-R as in the AFTER04 records | Strengthened by companion evidence. |
| SW-CR-0116 | SW-C-0038 | Felix’s wish to be remembered tends toward a hero’s posthumous light and overrides his dead friend’s wish for him; Monica perceives obsession. (V04) | PRESERVE | Unchanged (AFTER04) | See AFTER04 reading section 9.1. | — | Review, not change. |
| SW-CR-0117 | SW-C-0039 | A traitor curse-caster protected by a patron called 閣下, who discarded Thornley, is working on a puppet curse and knew and hated Venedict Rain; the patron is unidentified. (V04) | PRESERVE | Unchanged (AFTER04) | See AFTER04 reading section 9.1. | — | Review, not change. |
| SW-CR-0118 | SW-C-0040 | The volume assigns Eliane moral responsibility for acts partly amplified by a curse, and lets her go unexamined in the world. (V04) | PRESERVE | Unchanged (AFTER04) | See AFTER04 reading section 9.1. | — | Review, not change. |

Revision records at V05, 2026-10-14, reviewer the V05 sequential integrator:

| Revision | Claim | Earlier formulation and boundary | Transition | New formulation and boundary | Reason | Affected homes | Kind |
|---|---|---|---|---|---|---|---|
| SW-CR-0119 | SW-C-0001 | Chantless casting began as avoidance of speech, and silence and mastery are one mechanism; the avoidance has an earlier root in childhood punishment for speaking; before Minerva a year of abuse produced a dissociation in which she lost language, ended by Hilda Everett’s rescue; its occasion at Minerva was a friend’s plan to shorten her chant; the public account explains the capacity as instant computation. (prior) | STRENGTHEN | Wording unchanged; support extended (V05) | See V05 reading section 9.1. | — | Strengthened. |
| SW-CR-0120 | SW-C-0002 | Pain, fear or exposure drive Monica into numerical absorption; the habit began as a child’s escape from her uncle into her father’s formulas and a vow to keep his numbers; she also uses it deliberately to compute combat and to bear people, and it fails when people she knows are threatened. (prior) | REVISE | Pain, fear or exposure drive Monica into numerical absorption; the habit began as a child’s escape from her uncle into her father’s formulas and a vow to keep his numbers; she uses it to compute combat and to bear people, it fails when people she knows are threatened, and she now turns it outward as evidence, naming it no longer a refuge. (V05) | Numbers as evidence (V05 obs. 139, 144). | See V05 reading section 9.1. | Revision on new evidence. |
| SW-CR-0121 | SW-C-0003 | Monica’s paternal uncle, after her father’s execution when she was ten, beat and starved her, shut her in a winter barn and forbade her to defend her father, for about a year until Hilda Everett took her; scars remain and touch still frightens her. (prior) | PRESERVE | Unchanged (V05) | See V05 reading section 9.1. | — | Review, not change. |
| SW-CR-0122 | SW-C-0004 | The makeweight self-assessment is contradicted by Louis’s memory of the duel; the examiners’ ranking is unstated. (prior) | STRENGTHEN | Wording unchanged; support extended (V05) | See V05 reading section 9.1. | — | Strengthened. |
| SW-CR-0123 | SW-C-0005 | Stated protection; Monica doubts it; Louis reads surveillance, uses a decoy, chose Monica because she distrusts, fears and hates people and can therefore be merciless, and calls himself first-prince because he dislikes the duke and Felix; the king is unshown. (prior) | STRENGTHEN | Wording unchanged; support extended (V05) | See V05 reading section 9.1. | — | Strengthened. |
| SW-CR-0124 | SW-C-0006 | The prologue’s watcher is Felix. (prior) | PRESERVE | Unchanged (V05) | See V05 reading section 9.1. | — | Review, not change. |
| SW-CR-0125 | SW-C-0007 | Public and private selves diverge: he denies a talent for magic while studying it in secret because it is forbidden to him, and hides a spirit; he obeys the duke outwardly while removing his placements and gathering nobles who resent him; he must become king without wanting it, under a ten-year vow to make the name Felix Arc Ridill remembered, which he now expresses as a hero’s posthumous light and pursues even against his dead friend’s wish. (prior) | STRENGTHEN | Wording unchanged; support extended (V05) | See V05 reading section 9.1. | — | Strengthened. |
| SW-CR-0126 | SW-C-0008 | Felix has not identified Monica as the Silent Witch; at V03 exit he admires the Witch’s magic as a first love, has never seen her face, spent the festival night with Monica, briefly suspected her of being an assassin, and still does not connect them. (prior) | STRENGTHEN | Wording unchanged; support extended (V05) | See V05 reading section 9.1. | — | Strengthened. |
| SW-CR-0127 | SW-C-0009 | Cyril holds an unverified suspicion from her hand and remark (V01), links the forest mage with the Silent Witch (V02), and at V04 notices unexplained magical ice and her small, pen-callused hand; no conclusion is shown. (prior) | PRESERVE | Unchanged (V05) | See V05 reading section 9.1. | — | Review, not change. |
| SW-CR-0128 | SW-C-0010 | Awe at Monica’s power is narrated through external focalizers; from V02 her own viewpoint also narrates her power, as calculation under constraint; V03 extends this to sustained combat computation and gives her first chantless casting from a rival’s view. (prior) | STRENGTHEN | Wording unchanged; support extended (V05) | See V05 reading section 9.1. | — | Strengthened. |
| SW-CR-0129 | SW-C-0011 | The school treats rank as epistemic authority; Cyril’s inquiry is the first counterexample; at V02 rank is also used as a weapon of justice (Felix, Isabelle) and Elliott’s code ties rank to duty; at V03 Elliott’s contempt for upstarts has a biographical root and he warns that talent crossing class walls is envied or used. (prior) | STRENGTHEN | Wording unchanged; support extended (V05) | See V05 reading section 9.1. | — | Strengthened. |
| SW-CR-0130 | SW-C-0012 | Organized embezzlement; erased Aaron’s and Cyril’s memories; Selma’s manipulation inferred; at V04 a traitor curse-caster reveals that Thornley worked for a patron called 閣下 through mind interference and was discarded. (prior) | STRENGTHEN | Wording unchanged; support extended (V05) | See V05 reading section 9.1. | — | Strengthened. |
| SW-CR-0131 | SW-C-0013 | Neither an ordinary cat nor, in Felix’s judgment, a spirit; drug-immune, with a reptilian hiss and slit pupils, his human shape slipping in rage; a spirit finds him an anomalous familiar. Nature undisclosed. (prior) | REVISE | Nero is the Worgan black dragon, driven from the Empire’s mountains, worshipped but not commanded by the wyverns, and Monica’s familiar by his own choice after she pulled a bone from his throat; he can use black flame only in his true form. (V05) | Disclosed (V05 obs. 106, 122–124). | See V05 reading section 9.1. | Revision on new evidence. |
| SW-CR-0132 | SW-C-0014 | Monica regards her talent as a curse that took her father and friend; her father, Venedict Rain, author of a book on heredity and magical properties, was executed as a heretic when Monica was ten and his book burned; the friend, Bernie Jones, needed her dependence, turned away in envy, sent her to the hut, and wanted to be her equal rival; she has renounced his approval. Correction: the V03 formulation dated the execution five years before the present, but the V03 text dates only the book’s publication. (prior) | STRENGTHEN | Wording unchanged; support extended (V05) | See V05 reading section 9.1. | — | Strengthened. |
| SW-CR-0133 | SW-C-0015 | The bond with Lana rests on shared experience of being called boring and being out of place, and on mutual gestures of giving; Lana began from pride and stays from affection; at V03 Lana arms and defends her, and Monica defends Lana first. (prior) | PRESERVE | Unchanged (V05) | See V05 reading section 9.1. | — | Review, not change. |
| SW-CR-0134 | SW-C-0016 | The comedy of coercion registers harm in most cases; the non-consensual kiss is unevaluated and unknown to its recipient. (prior) | STRENGTHEN | Wording unchanged; support extended (V05) | See V05 reading section 9.1. | — | Strengthened. |
| SW-CR-0135 | SW-C-0017 | Louis combines coercion with investment in her self-respect and his own pride; at V02 also gifts, an unknowing decoy, and a concession calculated to keep her cooperation; at V03 he lends Lynn and, to Casey, judges her a heartless witch. (prior) | STRENGTHEN | Wording unchanged; support extended (V05) | See V05 reading section 9.1. | — | Strengthened. |
| SW-CR-0136 | SW-C-0018 | Monica’s numerical perception and comfort derive from her father’s teaching; his saying that the world is made of numbers became her means of fleeing reality under her uncle; she memorized his burning numbers and keeps his coffee pot; at V04 she refuses the saying as an excuse. (prior) | STRENGTHEN | Wording unchanged; support extended (V05) | See V05 reading section 9.1. | — | Strengthened. |
| SW-CR-0137 | SW-C-0019 | Casey Grove is the prologue’s unnamed conspirator, acting on Count Bright’s order with a 螺炎, from grievance at central neglect and gratitude to Randall; her friendship was begun instrumentally; at V03 Count Bright claims sole responsibility, Louis suspects Randall and the Empire, and Casey asks after Monica and sends her a package, so that her feeling is evidenced as concern and its history remains OPEN. (prior) | PRESERVE | Unchanged (V05) | See V05 reading section 9.1. | — | Review, not change. |
| SW-CR-0138 | SW-C-0020 | Monica derives a concept of duty from Elliott’s noblesse oblige and transposes it to her roles as treasurer and Sage; at V03 duty is joined by a personal motive she calls selfish, that the bereaved be able to mourn as she could not. (prior) | STRENGTHEN | Wording unchanged; support extended (V05) | See V05 reading section 9.1. | — | Strengthened. |
| SW-CR-0139 | SW-C-0021 | Monica’s concealment is a political bargain using Louis’s factional logic, at a cost to Cyril and her conscience; the volume presents it sympathetically and leaves its justice unjudged; at V03 Cyril still blames himself and she cannot clear him. (prior) | PRESERVE | Unchanged (V05) | See V05 reading section 9.1. | — | Review, not change. |
| SW-CR-0140 | SW-C-0022 | A cluster of unexplained details surrounds Felix’s identity and history: Bridget’s childhood test; his memory of a boy apologizing as a royal; the role held while he bears the name; the seer’s blindness to his star from about ten years ago; Elliott’s memory of a sickly, clumsy, shy, light-eyed, star-loving child scarred in the side with a more poised attendant; a ten-year vow to inscribe the name in history; a dead friend whose wish he pursues; a dream of a boy called Felix, a page and a burned astronomy book; a necessary scar. No hypothesis is registered. (prior) | STRENGTHEN | Wording unchanged; support extended (V05) | See V05 reading section 9.1. | — | Strengthened. |
| SW-CR-0141 | SW-C-0023 | Monica says she cannot expect anything of anyone, while her conduct shows growing attachment; no romantic interest on her side is shown and she does not wish to marry; Felix’s absorption in the Silent Witch as an idea is now joined, in his own viewpoint, by attachment and jealousy toward Monica herself. (prior) | STRENGTHEN | Wording unchanged; support extended (V05) | See V05 reading section 9.1. | — | Strengthened. |
| SW-CR-0142 | SW-C-0024 | Louis chose Monica for her distrust, fear and hatred of people, calls her heartless, and reads her attachment as a risk; Monica shares the warning that Monica Norton is temporary, and at V03 expected her false school life to end. (prior) | PRESERVE | Unchanged (V05) | See V05 reading section 9.1. | — | Review, not change. |
| SW-CR-0143 | SW-C-0025 | Isabelle’s cover-bullying is a deliberate deterrence policy and her revenge mirrors the crime; the volume treats humiliation as justice. (prior) | STRENGTHEN | Wording unchanged; support extended (V05) | See V05 reading section 9.1. | — | Strengthened. |
| SW-CR-0144 | SW-C-0026 | 場違い organizes the social plot through three outsiders by class or region, Monica, Lana and Casey, reversing from exclusion to self-gift. (prior) | PRESERVE | Unchanged (V05) | See V05 reading section 9.1. | — | Review, not change. |
| SW-CR-0145 | SW-C-0027 | Bernie Jones is the Minerva friend; his help coexisted with a wish for her dependence; his envy ended the friendship and his curse began the hut life; he protected her cover as a noble’s duty, wanted to be her equal rival, and leaves Minerva as heir offering future help. (prior) | STRENGTHEN | Wording unchanged; support extended (V05) | See V05 reading section 9.1. | — | Strengthened. |
| SW-CR-0146 | SW-C-0028 | Mourning organizes V03: Monica’s motive in the climax is that the bereaved be able to mourn as she could not; burned books and festival bells join her strand and Felix’s. (prior) | PRESERVE | Unchanged (V05) | See V05 reading section 9.1. | — | Review, not change. |
| SW-CR-0147 | SW-C-0029 | Ike is a persona in which Felix shows Monica a self outside his role; her answering self-description as a ghost was her first outreach; the persona persists in private moments after the festival night, and Monica keeps its confidences from Louis. (prior) | PRESERVE | Unchanged (V05) | See V05 reading section 9.1. | — | Review, not change. |
| SW-CR-0148 | SW-C-0030 | The duke dominates Felix by contempt and, in Felix’s dream, by punishing those the boy cares for; Felix obeys outwardly while gathering nobles who resent the duke. (prior) | STRENGTHEN | Wording unchanged; support extended (V05) | See V05 reading section 9.1. | — | Strengthened. |
| SW-CR-0149 | SW-C-0031 | Imperial agents Yuan and Heidi, serving a master, used imperial body magic, impersonated Pittman and then Cyril, sought a trace on Felix that Yuan attributes to a traitor Arthur and the capture of the Silent Witch, threatened war, and escaped with Yuan cursed for at least a month; Louis suspects a Randall–Empire alliance. (prior) | PRESERVE | Unchanged (V05) | See V05 reading section 9.1. | — | Review, not change. |
| SW-CR-0150 | SW-C-0032 | Monica’s father was Venedict Rain, author of a book on heredity and magical properties, executed for forbidden research when Monica was ten; his former assistant Hilda Everett adopted her; his friend Porter is Dustin Günther; a traitor curse-caster knew and hated him. Correction: the V03 formulation dated the execution five years before the present; the V03 text dates only the book’s publication, and the two dates are in tension. (prior) | REVISE | Monica’s father was Venedict Rain, author of a book on heredity and magical properties, executed seven years ago, when Monica was ten, after a curse-caster he refused had him charged with necromancy on planted evidence, under a great noble’s pressure and without trial; his former assistant Hilda Everett adopted her; his friend Porter is Dustin Günther. The V04 correction stands. (V05) | Sams’s words and Hilda’s account (V05 obs. 147, 166). | See V05 reading section 9.1. | Revision on new evidence. |
| SW-CR-0151 | SW-C-0033 | Louis’s model of Monica as a heartless witch who sees people as numbers is half right: she accepts it and uses it as a technique, then fails to apply it to the people she knows; Louis says her humanity does not matter to him either way. (prior) | PRESERVE | Unchanged (V05) | See V05 reading section 9.1. | — | Review, not change. |
| SW-CR-0152 | SW-C-0034 | Mary deliberately allowed the theft of the ancient tool, citing the stars’ guidance, and used the crisis to test Monica; the volume does not judge the risk to the town or the bystander. (prior) | STRENGTHEN | Wording unchanged; support extended (V05) | See V05 reading section 9.1. | — | Strengthened. |
| SW-CR-0153 | SW-C-0035 | Monica’s numerical dissociation, born of abuse, is now both a chosen weapon and a limit: it fails when the people of the school are at stake, and she chooses to remain Monica Norton while knowing it deceives her friends. (prior) | REVISE | Monica’s numerical dissociation, born of abuse, became a chosen weapon and a limit, and now also a means of evidence; she remains Monica Norton knowing it deceives her friends, and her purpose widens to her father’s innocence. (V05) | V05 obs. 139, 149, 170. | See V05 reading section 9.1. | Revision on new evidence. |
| SW-CR-0154 | SW-C-0036 | V04 is organized by gifts whose meaning differs between giver and receiver: the rose, the cursed necklace, the pendant, the handkerchief and the friend’s wish. (prior) | STRENGTHEN | Wording unchanged; support extended (V05) | See V05 reading section 9.1. | — | Strengthened. |
| SW-CR-0155 | SW-C-0037 | Cyril’s history mirrors Monica’s: a violent father, withheld praise and striving for recognition; his care for her is a disguised invitation and practical help, and his attention returns to her hand. (prior) | STRENGTHEN | Wording unchanged; support extended (V05) | See V05 reading section 9.1. | — | Strengthened. |
| SW-CR-0156 | SW-C-0038 | Felix’s wish to be remembered tends toward a hero’s posthumous light and overrides his dead friend’s wish for him; Monica perceives obsession. (prior) | STRENGTHEN | Wording unchanged; support extended (V05) | See V05 reading section 9.1. | — | Strengthened. |
| SW-CR-0157 | SW-C-0039 | A traitor curse-caster protected by a patron called 閣下, who discarded Thornley, is working on a puppet curse and knew and hated Venedict Rain; the patron is unidentified. (prior) | REVISE | The traitor curse-caster was Barry Oates, serving at Leinbourg as the footman Peter Sams; he researched a puppet curse for a patron called 閣下, sold Venedict Rain to that patron, defined himself against Thornley, and died by his own curse; 閣下 is unidentified. (V05) | V05 obs. 140, 141, 147, 148. | See V05 reading section 9.1. | Revision on new evidence. |
| SW-CR-0158 | SW-C-0040 | The volume assigns Eliane moral responsibility for acts partly amplified by a curse, and lets her go unexamined in the world. (prior) | PRESERVE | Unchanged (V05) | See V05 reading section 9.1. | — | Review, not change. |
| SW-CR-0159 | SW-C-0041 | The companion argues that charms work by giving the user courage through something special; Monica, who rejected the theory, makes and keeps charms herself, and the inverse case of a curse taken for a charm shows the danger of not knowing what one holds. (prior) | STRENGTHEN | Wording unchanged; support extended (V05) | See V05 reading section 9.1. | — | Strengthened. |
| SW-CR-0160 | SW-C-0042 | Monica’s power is visible only to a spirit and the reader, and her cover holds through small lies; the volume treats both as comedy. (prior) | REVISE | Monica’s power was visible only to a spirit and the reader while she lived as Monica Norton; acting openly as the Silent Witch, her concealment fails before Felix, whose inferences outpace her small lies. (V05) | V05 obs. 038, 129. | See V05 reading section 9.1. | Revision on new evidence. |
| SW-CR-0161 | SW-C-0043 | Cyril’s ethic of earned, patient effort is set against Louis’s maxim of money, violence and strength; Glen and Monica, who drifted into magic, take Cyril’s side. (prior) | STRENGTHEN | Wording unchanged; support extended (V05) | See V05 reading section 9.1. | — | Strengthened. |
| SW-CR-0162 | SW-C-0044 | Elliott’s creed of rank rests on an uncle’s suicide and a further event before he was ten that he withholds; his own friendship contradicts it. (prior) | PRESERVE | Unchanged (V05) | See V05 reading section 9.1. | — | Review, not change. |

Revision records at V06, 2026-10-14, reviewer the V06 sequential integrator:

| Revision | Claim | Earlier formulation and boundary | Transition | New formulation and boundary | Reason | Affected homes | Kind |
|---|---|---|---|---|---|---|---|
| SW-CR-0163 | SW-C-0001 | Chantless casting began as avoidance of speech, and silence and mastery are one mechanism; the avoidance has an earlier root in childhood punishment for speaking; before Minerva a year of abuse produced a dissociation in which she lost language, ended by Hilda Everett’s rescue; its occasion at Minerva was a friend’s plan to shorten her chant; the public account explains the capacity as instant computation. (prior) | STRENGTHEN | Wording unchanged; support extended (V06) | See V06 reading section 9.1. | — | Strengthened. |
| SW-CR-0164 | SW-C-0002 | Pain, fear or exposure drive Monica into numerical absorption; the habit began as a child’s escape from her uncle into her father’s formulas and a vow to keep his numbers; she uses it to compute combat and to bear people, it fails when people she knows are threatened, and she now turns it outward as evidence, naming it no longer a refuge. (prior) | STRENGTHEN | Wording unchanged; support extended (V06) | See V06 reading section 9.1. | — | Strengthened. |
| SW-CR-0165 | SW-C-0003 | Monica’s paternal uncle, after her father’s execution when she was ten, beat and starved her, shut her in a winter barn and forbade her to defend her father, for about a year until Hilda Everett took her; scars remain and touch still frightens her. (prior) | PRESERVE | Unchanged (V06) | See V06 reading section 9.1. | — | Review, not change. |
| SW-CR-0166 | SW-C-0004 | The makeweight self-assessment is contradicted by Louis’s memory of the duel; the examiners’ ranking is unstated. (prior) | PRESERVE | Unchanged (V06) | See V06 reading section 9.1. | — | Review, not change. |
| SW-CR-0167 | SW-C-0005 | Stated protection; Monica doubts it; Louis reads surveillance, uses a decoy, chose Monica because she distrusts, fears and hates people and can therefore be merciless, and calls himself first-prince because he dislikes the duke and Felix; the king is unshown. (prior) | STRENGTHEN | Wording unchanged; support extended (V06) | See V06 reading section 9.1. | — | Strengthened. |
| SW-CR-0168 | SW-C-0006 | The prologue’s watcher is Felix. (prior) | PRESERVE | Unchanged (V06) | See V06 reading section 9.1. | — | Review, not change. |
| SW-CR-0169 | SW-C-0007 | Public and private selves diverge: he denies a talent for magic while studying it in secret because it is forbidden to him, and hides a spirit; he obeys the duke outwardly while removing his placements and gathering nobles who resent him; he must become king without wanting it, under a ten-year vow to make the name Felix Arc Ridill remembered, which he now expresses as a hero’s posthumous light and pursues even against his dead friend’s wish. (prior) | STRENGTHEN | Wording unchanged; support extended (V06) | See V06 reading section 9.1. | — | Strengthened. |
| SW-CR-0170 | SW-C-0008 | Felix has not identified Monica as the Silent Witch; at V03 exit he admires the Witch’s magic as a first love, has never seen her face, spent the festival night with Monica, briefly suspected her of being an assassin, and still does not connect them. (prior) | STRENGTHEN | Wording unchanged; support extended (V06) | See V06 reading section 9.1. | — | Strengthened. |
| SW-CR-0171 | SW-C-0009 | Cyril holds an unverified suspicion from her hand and remark (V01), links the forest mage with the Silent Witch (V02), and at V04 notices unexplained magical ice and her small, pen-callused hand; no conclusion is shown. (prior) | REVISE | Cyril holds an unverified suspicion from her hand and remark (V01), links the forest mage with the Silent Witch (V02), and at V04 notices unexplained magical ice and her small, pen-callused hand; at V06 he senses he has met the Witch, notices her injured left hand and Monica’s repeatedly flexed one, and before fainting hears Hubert call the small figure in the fog the Silent Witch; no conclusion is shown. (V06) | V06 obs. 031, 032, 083, 152. | See V06 reading section 9.1. | Revision on new evidence. |
| SW-CR-0172 | SW-C-0010 | Awe at Monica’s power is narrated through external focalizers; from V02 her own viewpoint also narrates her power, as calculation under constraint; V03 extends this to sustained combat computation and gives her first chantless casting from a rival’s view. (prior) | STRENGTHEN | Wording unchanged; support extended (V06) | See V06 reading section 9.1. | — | Strengthened. |
| SW-CR-0173 | SW-C-0011 | The school treats rank as epistemic authority; Cyril’s inquiry is the first counterexample; at V02 rank is also used as a weapon of justice (Felix, Isabelle) and Elliott’s code ties rank to duty; at V03 Elliott’s contempt for upstarts has a biographical root and he warns that talent crossing class walls is envied or used. (prior) | STRENGTHEN | Wording unchanged; support extended (V06) | See V06 reading section 9.1. | — | Strengthened. |
| SW-CR-0174 | SW-C-0012 | Organized embezzlement; erased Aaron’s and Cyril’s memories; Selma’s manipulation inferred; at V04 a traitor curse-caster reveals that Thornley worked for a patron called 閣下 through mind interference and was discarded. (prior) | PRESERVE | Unchanged (V06) | See V06 reading section 9.1. | — | Review, not change. |
| SW-CR-0175 | SW-C-0013 | Nero is the Worgan black dragon, driven from the Empire’s mountains, worshipped but not commanded by the wyverns, and Monica’s familiar by his own choice after she pulled a bone from his throat; he can use black flame only in his true form. (prior) | PRESERVE | Unchanged (V06) | See V06 reading section 9.1. | — | Review, not change. |
| SW-CR-0176 | SW-C-0014 | Monica regards her talent as a curse that took her father and friend; her father, Venedict Rain, author of a book on heredity and magical properties, was executed as a heretic when Monica was ten and his book burned; the friend, Bernie Jones, needed her dependence, turned away in envy, sent her to the hut, and wanted to be her equal rival; she has renounced his approval. Correction: the V03 formulation dated the execution five years before the present, but the V03 text dates only the book’s publication. (prior) | STRENGTHEN | Wording unchanged; support extended (V06) | See V06 reading section 9.1. | — | Strengthened. |
| SW-CR-0177 | SW-C-0015 | The bond with Lana rests on shared experience of being called boring and being out of place, and on mutual gestures of giving; Lana began from pride and stays from affection; at V03 Lana arms and defends her, and Monica defends Lana first. (prior) | STRENGTHEN | Wording unchanged; support extended (V06) | See V06 reading section 9.1. | — | Strengthened. |
| SW-CR-0178 | SW-C-0016 | The comedy of coercion registers harm in most cases; the non-consensual kiss is unevaluated and unknown to its recipient. (prior) | STRENGTHEN | Wording unchanged; support extended (V06) | See V06 reading section 9.1. | — | Strengthened. |
| SW-CR-0179 | SW-C-0017 | Louis combines coercion with investment in her self-respect and his own pride; at V02 also gifts, an unknowing decoy, and a concession calculated to keep her cooperation; at V03 he lends Lynn and, to Casey, judges her a heartless witch. (prior) | STRENGTHEN | Wording unchanged; support extended (V06) | See V06 reading section 9.1. | — | Strengthened. |
| SW-CR-0180 | SW-C-0018 | Monica’s numerical perception and comfort derive from her father’s teaching; his saying that the world is made of numbers became her means of fleeing reality under her uncle; she memorized his burning numbers and keeps his coffee pot; at V04 she refuses the saying as an excuse. (prior) | PRESERVE | Unchanged (V06) | See V06 reading section 9.1. | — | Review, not change. |
| SW-CR-0181 | SW-C-0019 | Casey Grove is the prologue’s unnamed conspirator, acting on Count Bright’s order with a 螺炎, from grievance at central neglect and gratitude to Randall; her friendship was begun instrumentally; at V03 Count Bright claims sole responsibility, Louis suspects Randall and the Empire, and Casey asks after Monica and sends her a package, so that her feeling is evidenced as concern and its history remains OPEN. (prior) | PRESERVE | Unchanged (V06) | See V06 reading section 9.1. | — | Review, not change. |
| SW-CR-0182 | SW-C-0020 | Monica derives a concept of duty from Elliott’s noblesse oblige and transposes it to her roles as treasurer and Sage; at V03 duty is joined by a personal motive she calls selfish, that the bereaved be able to mourn as she could not. (prior) | PRESERVE | Unchanged (V06) | See V06 reading section 9.1. | — | Review, not change. |
| SW-CR-0183 | SW-C-0021 | Monica’s concealment is a political bargain using Louis’s factional logic, at a cost to Cyril and her conscience; the volume presents it sympathetically and leaves its justice unjudged; at V03 Cyril still blames himself and she cannot clear him. (prior) | PRESERVE | Unchanged (V06) | See V06 reading section 9.1. | — | Review, not change. |
| SW-CR-0184 | SW-C-0022 | A cluster of unexplained details surrounds Felix’s identity and history: Bridget’s childhood test; his memory of a boy apologizing as a royal; the role held while he bears the name; the seer’s blindness to his star from about ten years ago; Elliott’s memory of a sickly, clumsy, shy, light-eyed, star-loving child scarred in the side with a more poised attendant; a ten-year vow to inscribe the name in history; a dead friend whose wish he pursues; a dream of a boy called Felix, a page and a burned astronomy book; a necessary scar. No hypothesis is registered. (prior) | STRENGTHEN | Wording unchanged; support extended (V06) | See V06 reading section 9.1. | — | Strengthened. |
| SW-CR-0185 | SW-C-0023 | Monica says she cannot expect anything of anyone, while her conduct shows growing attachment; no romantic interest on her side is shown and she does not wish to marry; Felix’s absorption in the Silent Witch as an idea is now joined, in his own viewpoint, by attachment and jealousy toward Monica herself. (prior) | STRENGTHEN | Wording unchanged; support extended (V06) | See V06 reading section 9.1. | — | Strengthened. |
| SW-CR-0186 | SW-C-0024 | Louis chose Monica for her distrust, fear and hatred of people, calls her heartless, and reads her attachment as a risk; Monica shares the warning that Monica Norton is temporary, and at V03 expected her false school life to end. (prior) | STRENGTHEN | Wording unchanged; support extended (V06) | See V06 reading section 9.1. | — | Strengthened. |
| SW-CR-0187 | SW-C-0025 | Isabelle’s cover-bullying is a deliberate deterrence policy and her revenge mirrors the crime; the volume treats humiliation as justice. (prior) | STRENGTHEN | Wording unchanged; support extended (V06) | See V06 reading section 9.1. | — | Strengthened. |
| SW-CR-0188 | SW-C-0026 | 場違い organizes the social plot through three outsiders by class or region, Monica, Lana and Casey, reversing from exclusion to self-gift. (prior) | PRESERVE | Unchanged (V06) | See V06 reading section 9.1. | — | Review, not change. |
| SW-CR-0189 | SW-C-0027 | Bernie Jones is the Minerva friend; his help coexisted with a wish for her dependence; his envy ended the friendship and his curse began the hut life; he protected her cover as a noble’s duty, wanted to be her equal rival, and leaves Minerva as heir offering future help. (prior) | STRENGTHEN | Wording unchanged; support extended (V06) | See V06 reading section 9.1. | — | Strengthened. |
| SW-CR-0190 | SW-C-0028 | Mourning organizes V03: Monica’s motive in the climax is that the bereaved be able to mourn as she could not; burned books and festival bells join her strand and Felix’s. (prior) | PRESERVE | Unchanged (V06) | See V06 reading section 9.1. | — | Review, not change. |
| SW-CR-0191 | SW-C-0029 | Ike is a persona in which Felix shows Monica a self outside his role; her answering self-description as a ghost was her first outreach; the persona persists in private moments after the festival night, and Monica keeps its confidences from Louis. (prior) | STRENGTHEN | Wording unchanged; support extended (V06) | See V06 reading section 9.1. | — | Strengthened. |
| SW-CR-0192 | SW-C-0030 | The duke dominates Felix by contempt and, in Felix’s dream, by punishing those the boy cares for; Felix obeys outwardly while gathering nobles who resent the duke. (prior) | STRENGTHEN | Wording unchanged; support extended (V06) | See V06 reading section 9.1. | — | Strengthened. |
| SW-CR-0193 | SW-C-0031 | Imperial agents Yuan and Heidi, serving a master, used imperial body magic, impersonated Pittman and then Cyril, sought a trace on Felix that Yuan attributes to a traitor Arthur and the capture of the Silent Witch, threatened war, and escaped with Yuan cursed for at least a month; Louis suspects a Randall–Empire alliance. (prior) | PRESERVE | Unchanged (V06) | See V06 reading section 9.1. | — | Review, not change. |
| SW-CR-0194 | SW-C-0032 | Monica’s father was Venedict Rain, author of a book on heredity and magical properties, executed seven years ago, when Monica was ten, after a curse-caster he refused had him charged with necromancy on planted evidence, under a great noble’s pressure and without trial; his former assistant Hilda Everett adopted her; his friend Porter is Dustin Günther. The V04 correction stands. (prior) | PRESERVE | Unchanged (V06) | See V06 reading section 9.1. | — | Review, not change. |
| SW-CR-0195 | SW-C-0033 | Louis’s model of Monica as a heartless witch who sees people as numbers is half right: she accepts it and uses it as a technique, then fails to apply it to the people she knows; Louis says her humanity does not matter to him either way. (prior) | STRENGTHEN | Wording unchanged; support extended (V06) | See V06 reading section 9.1. | — | Strengthened. |
| SW-CR-0196 | SW-C-0034 | Mary deliberately allowed the theft of the ancient tool, citing the stars’ guidance, and used the crisis to test Monica; the volume does not judge the risk to the town or the bystander. (prior) | PRESERVE | Unchanged (V06) | See V06 reading section 9.1. | — | Review, not change. |
| SW-CR-0197 | SW-C-0035 | Monica’s numerical dissociation, born of abuse, became a chosen weapon and a limit, and now also a means of evidence; she remains Monica Norton knowing it deceives her friends, and her purpose widens to her father’s innocence. (prior) | PRESERVE | Unchanged (V06) | See V06 reading section 9.1. | — | Review, not change. |
| SW-CR-0198 | SW-C-0036 | V04 is organized by gifts whose meaning differs between giver and receiver: the rose, the cursed necklace, the pendant, the handkerchief and the friend’s wish. (prior) | PRESERVE | Unchanged (V06) | See V06 reading section 9.1. | — | Review, not change. |
| SW-CR-0199 | SW-C-0037 | Cyril’s history mirrors Monica’s: a violent father, withheld praise and striving for recognition; his care for her is a disguised invitation and practical help, and his attention returns to her hand. (prior) | STRENGTHEN | Wording unchanged; support extended (V06) | See V06 reading section 9.1. | — | Strengthened. |
| SW-CR-0200 | SW-C-0038 | Felix’s wish to be remembered tends toward a hero’s posthumous light and overrides his dead friend’s wish for him; Monica perceives obsession. (prior) | PRESERVE | Unchanged (V06) | See V06 reading section 9.1. | — | Review, not change. |
| SW-CR-0201 | SW-C-0039 | The traitor curse-caster was Barry Oates, serving at Leinbourg as the footman Peter Sams; he researched a puppet curse for a patron called 閣下, sold Venedict Rain to that patron, defined himself against Thornley, and died by his own curse; 閣下 is unidentified. (prior) | REVISE | The traitor curse-caster was Barry Oates, serving at Leinbourg as the footman Peter Sams; before Leinbourg he worked for Duke Clockford from about eight years ago in work no one knew; his last tool was a failed curse meant to control its target; he sold Venedict Rain to a patron called 閣下, defined himself against Thornley, and died by his own curse; 閣下 is unidentified. (V06) | V06 obs. 021, 204, 205. | See V06 reading section 9.1. | Revision on new evidence. |
| SW-CR-0202 | SW-C-0040 | The volume assigns Eliane moral responsibility for acts partly amplified by a curse, and lets her go unexamined in the world. (prior) | PRESERVE | Unchanged (V06) | See V06 reading section 9.1. | — | Review, not change. |
| SW-CR-0203 | SW-C-0041 | The companion argues that charms work by giving the user courage through something special; Monica, who rejected the theory, makes and keeps charms herself, and the inverse case of a curse taken for a charm shows the danger of not knowing what one holds. (prior) | PRESERVE | Unchanged (V06) | See V06 reading section 9.1. | — | Review, not change. |
| SW-CR-0204 | SW-C-0042 | Monica’s power was visible only to a spirit and the reader while she lived as Monica Norton; acting openly as the Silent Witch, her concealment fails before Felix, whose inferences outpace her small lies. (prior) | STRENGTHEN | Wording unchanged; support extended (V06) | See V06 reading section 9.1. | — | Strengthened. |
| SW-CR-0205 | SW-C-0043 | Cyril’s ethic of earned, patient effort is set against Louis’s maxim of money, violence and strength; Glen and Monica, who drifted into magic, take Cyril’s side. (prior) | STRENGTHEN | Wording unchanged; support extended (V06) | See V06 reading section 9.1. | — | Strengthened. |
| SW-CR-0206 | SW-C-0044 | Elliott’s creed of rank rests on an uncle’s suicide and a further event before he was ten that he withholds; his own friendship contradicts it. (prior) | PRESERVE | Unchanged (V06) | See V06 reading section 9.1. | — | Review, not change. |
| SW-CR-0207 | SW-C-0045 | Monica’s father was framed by a curse-caster under a powerful patron, and her purpose widens from the mission to proving his innocence. (prior) | STRENGTHEN | Wording unchanged; support extended (V06) | See V06 reading section 9.1. | — | Strengthened. |
| SW-CR-0208 | SW-C-0046 | Monica’s concealment fails in three directions in one break: Bartholomeus, Felix’s inference of her school, and Felix’s knowledge of her familiar. (prior) | STRENGTHEN | Wording unchanged; support extended (V06) | See V06 reading section 9.1. | — | Strengthened. |
| SW-CR-0209 | SW-C-0047 | Felix believes his grandfather stages his heroism and means to make him a true puppet; he performs obedience and plans resistance. (prior) | REVISE | Felix believes his grandfather stages his heroism and means to make him a true puppet; he performs obedience and plans resistance; at V06 Clockford tells the Silent Witch that Felix moves at his will, while Felix, unaware of that offer, acts on his own hard judgement, including an order to kill and a plan to use Emmanuel. (V06) | V06 obs. 063, 066, 149, 183. | See V06 reading section 9.1. | Revision on new evidence. |
| SW-CR-0210 | SW-C-0048 | The volume is framed by Louis’s lesson that the game begins before the table, which Monica learns by losing. (prior) | PRESERVE | Unchanged (V06) | See V06 reading section 9.1. | — | Review, not change. |
| SW-CR-0211 | SW-C-0049 | Vows made before a witness organize the volume, and the chime sounds for each. (prior) | PRESERVE | Unchanged (V06) | See V06 reading section 9.1. | — | Review, not change. |
| SW-CR-0212 | SW-C-0050 | The cluster around Felix gains the contract stone, the water spirit against an earth name, the eye colour and a vow ending in Arc. (prior) | STRENGTHEN | Wording unchanged; support extended (V06) | See V06 reading section 9.1. | — | Strengthened. |

Revision records at V07, 2026-10-14, reviewer the V07 sequential integrator:

| Revision | Claim | Earlier formulation and boundary | Transition | New formulation and boundary | Reason | Affected homes | Kind |
|---|---|---|---|---|---|---|---|
| SW-CR-0213 | SW-C-0001 | Chantless casting began as avoidance of speech, and silence and mastery are one mechanism; the avoidance has an earlier root in childhood punishment for speaking; before Minerva a year of abuse produced a dissociation in which she lost language, ended by Hilda Everett’s rescue; its occasion at Minerva was a friend’s plan to shorten her chant; the public account explains the capacity as instant computation. (prior) | PRESERVE | Unchanged (V07) | See V07 reading section 9.1. | — | Review, not change. |
| SW-CR-0214 | SW-C-0002 | Pain, fear or exposure drive Monica into numerical absorption; the habit began as a child’s escape from her uncle into her father’s formulas and a vow to keep his numbers; she uses it to compute combat and to bear people, it fails when people she knows are threatened, and she now turns it outward as evidence, naming it no longer a refuge. (prior) | STRENGTHEN | Wording unchanged; support extended (V07) | See V07 reading section 9.1. | — | Strengthened. |
| SW-CR-0215 | SW-C-0003 | Monica’s paternal uncle, after her father’s execution when she was ten, beat and starved her, shut her in a winter barn and forbade her to defend her father, for about a year until Hilda Everett took her; scars remain and touch still frightens her. (prior) | PRESERVE | Unchanged (V07) | See V07 reading section 9.1. | — | Review, not change. |
| SW-CR-0216 | SW-C-0004 | The makeweight self-assessment is contradicted by Louis’s memory of the duel; the examiners’ ranking is unstated. (prior) | PRESERVE | Unchanged (V07) | See V07 reading section 9.1. | — | Review, not change. |
| SW-CR-0217 | SW-C-0005 | Stated protection; Monica doubts it; Louis reads surveillance, uses a decoy, chose Monica because she distrusts, fears and hates people and can therefore be merciless, and calls himself first-prince because he dislikes the duke and Felix; the king is unshown. (prior) | PRESERVE | Unchanged (V07) | See V07 reading section 9.1. | — | Review, not change. |
| SW-CR-0218 | SW-C-0006 | The prologue’s watcher is Felix. (prior) | PRESERVE | Unchanged (V07) | See V07 reading section 9.1. | — | Review, not change. |
| SW-CR-0219 | SW-C-0007 | Public and private selves diverge: he denies a talent for magic while studying it in secret because it is forbidden to him, and hides a spirit; he obeys the duke outwardly while removing his placements and gathering nobles who resent him; he must become king without wanting it, under a ten-year vow to make the name Felix Arc Ridill remembered, which he now expresses as a hero’s posthumous light and pursues even against his dead friend’s wish. (prior) | STRENGTHEN | Wording unchanged; support extended (V07) | See V07 reading section 9.1. | — | Strengthened. |
| SW-CR-0220 | SW-C-0008 | Felix has not identified Monica as the Silent Witch; at V03 exit he admires the Witch’s magic as a first love, has never seen her face, spent the festival night with Monica, briefly suspected her of being an assassin, and still does not connect them. (prior) | STRENGTHEN | Wording unchanged; support extended (V07) | See V07 reading section 9.1. | — | Strengthened. |
| SW-CR-0221 | SW-C-0009 | Cyril holds an unverified suspicion from her hand and remark (V01), links the forest mage with the Silent Witch (V02), and at V04 notices unexplained magical ice and her small, pen-callused hand; at V06 he senses he has met the Witch, notices her injured left hand and Monica’s repeatedly flexed one, and before fainting hears Hubert call the small figure in the fog the Silent Witch; no conclusion is shown. (prior) | REVISE | Cyril holds an unverified suspicion from her hand and remark (V01), links the forest mage with the Silent Witch (V02), and at V04 notices unexplained magical ice and her small, pen-callused hand; at V06 he senses he has met the Witch, notices her injured left hand and Monica’s repeatedly flexed one, and before fainting hears Hubert call the small figure in the fog the Silent Witch; at V07 he learns from Ray that the Witch’s left hand is cursed and remembers her shielding it; no conclusion is shown. (V07) | V07 obs. 061, 062. | See V07 reading section 9.1. | Revision on new evidence. |
| SW-CR-0222 | SW-C-0010 | Awe at Monica’s power is narrated through external focalizers; from V02 her own viewpoint also narrates her power, as calculation under constraint; V03 extends this to sustained combat computation and gives her first chantless casting from a rival’s view. (prior) | STRENGTHEN | Wording unchanged; support extended (V07) | See V07 reading section 9.1. | — | Strengthened. |
| SW-CR-0223 | SW-C-0011 | The school treats rank as epistemic authority; Cyril’s inquiry is the first counterexample; at V02 rank is also used as a weapon of justice (Felix, Isabelle) and Elliott’s code ties rank to duty; at V03 Elliott’s contempt for upstarts has a biographical root and he warns that talent crossing class walls is envied or used. (prior) | STRENGTHEN | Wording unchanged; support extended (V07) | See V07 reading section 9.1. | — | Strengthened. |
| SW-CR-0224 | SW-C-0012 | Organized embezzlement; erased Aaron’s and Cyril’s memories; Selma’s manipulation inferred; at V04 a traitor curse-caster reveals that Thornley worked for a patron called 閣下 through mind interference and was discarded. (prior) | PRESERVE | Unchanged (V07) | See V07 reading section 9.1. | — | Review, not change. |
| SW-CR-0225 | SW-C-0013 | Nero is the Worgan black dragon, driven from the Empire’s mountains, worshipped but not commanded by the wyverns, and Monica’s familiar by his own choice after she pulled a bone from his throat; he can use black flame only in his true form. (prior) | PRESERVE | Unchanged (V07) | See V07 reading section 9.1. | — | Review, not change. |
| SW-CR-0226 | SW-C-0014 | Monica regards her talent as a curse that took her father and friend; her father, Venedict Rain, author of a book on heredity and magical properties, was executed as a heretic when Monica was ten and his book burned; the friend, Bernie Jones, needed her dependence, turned away in envy, sent her to the hut, and wanted to be her equal rival; she has renounced his approval. Correction: the V03 formulation dated the execution five years before the present, but the V03 text dates only the book’s publication. (prior) | PRESERVE | Unchanged (V07) | See V07 reading section 9.1. | — | Review, not change. |
| SW-CR-0227 | SW-C-0015 | The bond with Lana rests on shared experience of being called boring and being out of place, and on mutual gestures of giving; Lana began from pride and stays from affection; at V03 Lana arms and defends her, and Monica defends Lana first. (prior) | STRENGTHEN | Wording unchanged; support extended (V07) | See V07 reading section 9.1. | — | Strengthened. |
| SW-CR-0228 | SW-C-0016 | The comedy of coercion registers harm in most cases; the non-consensual kiss is unevaluated and unknown to its recipient. (prior) | STRENGTHEN | Wording unchanged; support extended (V07) | See V07 reading section 9.1. | — | Strengthened. |
| SW-CR-0229 | SW-C-0017 | Louis combines coercion with investment in her self-respect and his own pride; at V02 also gifts, an unknowing decoy, and a concession calculated to keep her cooperation; at V03 he lends Lynn and, to Casey, judges her a heartless witch. (prior) | STRENGTHEN | Wording unchanged; support extended (V07) | See V07 reading section 9.1. | — | Strengthened. |
| SW-CR-0230 | SW-C-0018 | Monica’s numerical perception and comfort derive from her father’s teaching; his saying that the world is made of numbers became her means of fleeing reality under her uncle; she memorized his burning numbers and keeps his coffee pot; at V04 she refuses the saying as an excuse. (prior) | PRESERVE | Unchanged (V07) | See V07 reading section 9.1. | — | Review, not change. |
| SW-CR-0231 | SW-C-0019 | Casey Grove is the prologue’s unnamed conspirator, acting on Count Bright’s order with a 螺炎, from grievance at central neglect and gratitude to Randall; her friendship was begun instrumentally; at V03 Count Bright claims sole responsibility, Louis suspects Randall and the Empire, and Casey asks after Monica and sends her a package, so that her feeling is evidenced as concern and its history remains OPEN. (prior) | PRESERVE | Unchanged (V07) | See V07 reading section 9.1. | — | Review, not change. |
| SW-CR-0232 | SW-C-0020 | Monica derives a concept of duty from Elliott’s noblesse oblige and transposes it to her roles as treasurer and Sage; at V03 duty is joined by a personal motive she calls selfish, that the bereaved be able to mourn as she could not. (prior) | STRENGTHEN | Wording unchanged; support extended (V07) | See V07 reading section 9.1. | — | Strengthened. |
| SW-CR-0233 | SW-C-0021 | Monica’s concealment is a political bargain using Louis’s factional logic, at a cost to Cyril and her conscience; the volume presents it sympathetically and leaves its justice unjudged; at V03 Cyril still blames himself and she cannot clear him. (prior) | PRESERVE | Unchanged (V07) | See V07 reading section 9.1. | — | Review, not change. |
| SW-CR-0234 | SW-C-0022 | A cluster of unexplained details surrounds Felix’s identity and history: Bridget’s childhood test; his memory of a boy apologizing as a royal; the role held while he bears the name; the seer’s blindness to his star from about ten years ago; Elliott’s memory of a sickly, clumsy, shy, light-eyed, star-loving child scarred in the side with a more poised attendant; a ten-year vow to inscribe the name in history; a dead friend whose wish he pursues; a dream of a boy called Felix, a page and a burned astronomy book; a necessary scar. No hypothesis is registered. (prior) | STRENGTHEN | Wording unchanged; support extended (V07) | See V07 reading section 9.1. | — | Strengthened. |
| SW-CR-0235 | SW-C-0023 | Monica says she cannot expect anything of anyone, while her conduct shows growing attachment; no romantic interest on her side is shown and she does not wish to marry; Felix’s absorption in the Silent Witch as an idea is now joined, in his own viewpoint, by attachment and jealousy toward Monica herself. (prior) | STRENGTHEN | Wording unchanged; support extended (V07) | See V07 reading section 9.1. | — | Strengthened. |
| SW-CR-0236 | SW-C-0024 | Louis chose Monica for her distrust, fear and hatred of people, calls her heartless, and reads her attachment as a risk; Monica shares the warning that Monica Norton is temporary, and at V03 expected her false school life to end. (prior) | STRENGTHEN | Wording unchanged; support extended (V07) | See V07 reading section 9.1. | — | Strengthened. |
| SW-CR-0237 | SW-C-0025 | Isabelle’s cover-bullying is a deliberate deterrence policy and her revenge mirrors the crime; the volume treats humiliation as justice. (prior) | PRESERVE | Unchanged (V07) | See V07 reading section 9.1. | — | Review, not change. |
| SW-CR-0238 | SW-C-0026 | 場違い organizes the social plot through three outsiders by class or region, Monica, Lana and Casey, reversing from exclusion to self-gift. (prior) | PRESERVE | Unchanged (V07) | See V07 reading section 9.1. | — | Review, not change. |
| SW-CR-0239 | SW-C-0027 | Bernie Jones is the Minerva friend; his help coexisted with a wish for her dependence; his envy ended the friendship and his curse began the hut life; he protected her cover as a noble’s duty, wanted to be her equal rival, and leaves Minerva as heir offering future help. (prior) | PRESERVE | Unchanged (V07) | See V07 reading section 9.1. | — | Review, not change. |
| SW-CR-0240 | SW-C-0028 | Mourning organizes V03: Monica’s motive in the climax is that the bereaved be able to mourn as she could not; burned books and festival bells join her strand and Felix’s. (prior) | PRESERVE | Unchanged (V07) | See V07 reading section 9.1. | — | Review, not change. |
| SW-CR-0241 | SW-C-0029 | Ike is a persona in which Felix shows Monica a self outside his role; her answering self-description as a ghost was her first outreach; the persona persists in private moments after the festival night, and Monica keeps its confidences from Louis. (prior) | STRENGTHEN | Wording unchanged; support extended (V07) | See V07 reading section 9.1. | — | Strengthened. |
| SW-CR-0242 | SW-C-0030 | The duke dominates Felix by contempt and, in Felix’s dream, by punishing those the boy cares for; Felix obeys outwardly while gathering nobles who resent the duke. (prior) | STRENGTHEN | Wording unchanged; support extended (V07) | See V07 reading section 9.1. | — | Strengthened. |
| SW-CR-0243 | SW-C-0031 | Imperial agents Yuan and Heidi, serving a master, used imperial body magic, impersonated Pittman and then Cyril, sought a trace on Felix that Yuan attributes to a traitor Arthur and the capture of the Silent Witch, threatened war, and escaped with Yuan cursed for at least a month; Louis suspects a Randall–Empire alliance. (prior) | STRENGTHEN | Wording unchanged; support extended (V07) | See V07 reading section 9.1. | — | Strengthened. |
| SW-CR-0244 | SW-C-0032 | Monica’s father was Venedict Rain, author of a book on heredity and magical properties, executed seven years ago, when Monica was ten, after a curse-caster he refused had him charged with necromancy on planted evidence, under a great noble’s pressure and without trial; his former assistant Hilda Everett adopted her; his friend Porter is Dustin Günther. The V04 correction stands. (prior) | PRESERVE | Unchanged (V07) | See V07 reading section 9.1. | — | Review, not change. |
| SW-CR-0245 | SW-C-0033 | Louis’s model of Monica as a heartless witch who sees people as numbers is half right: she accepts it and uses it as a technique, then fails to apply it to the people she knows; Louis says her humanity does not matter to him either way. (prior) | STRENGTHEN | Wording unchanged; support extended (V07) | See V07 reading section 9.1. | — | Strengthened. |
| SW-CR-0246 | SW-C-0034 | Mary deliberately allowed the theft of the ancient tool, citing the stars’ guidance, and used the crisis to test Monica; the volume does not judge the risk to the town or the bystander. (prior) | PRESERVE | Unchanged (V07) | See V07 reading section 9.1. | — | Review, not change. |
| SW-CR-0247 | SW-C-0035 | Monica’s numerical dissociation, born of abuse, became a chosen weapon and a limit, and now also a means of evidence; she remains Monica Norton knowing it deceives her friends, and her purpose widens to her father’s innocence. (prior) | PRESERVE | Unchanged (V07) | See V07 reading section 9.1. | — | Review, not change. |
| SW-CR-0248 | SW-C-0036 | V04 is organized by gifts whose meaning differs between giver and receiver: the rose, the cursed necklace, the pendant, the handkerchief and the friend’s wish. (prior) | PRESERVE | Unchanged (V07) | See V07 reading section 9.1. | — | Review, not change. |
| SW-CR-0249 | SW-C-0037 | Cyril’s history mirrors Monica’s: a violent father, withheld praise and striving for recognition; his care for her is a disguised invitation and practical help, and his attention returns to her hand. (prior) | STRENGTHEN | Wording unchanged; support extended (V07) | See V07 reading section 9.1. | — | Strengthened. |
| SW-CR-0250 | SW-C-0038 | Felix’s wish to be remembered tends toward a hero’s posthumous light and overrides his dead friend’s wish for him; Monica perceives obsession. (prior) | PRESERVE | Unchanged (V07) | See V07 reading section 9.1. | — | Review, not change. |
| SW-CR-0251 | SW-C-0039 | The traitor curse-caster was Barry Oates, serving at Leinbourg as the footman Peter Sams; before Leinbourg he worked for Duke Clockford from about eight years ago in work no one knew; his last tool was a failed curse meant to control its target; he sold Venedict Rain to a patron called 閣下, defined himself against Thornley, and died by his own curse; 閣下 is unidentified. (prior) | REVISE | The traitor curse-caster was Barry Oates, serving at Leinbourg as the footman Peter Sams; before Leinbourg he served at Duke Clockford’s house as a physician or researcher, from about ten years ago by the gardener’s account (about eight by Bartholomeus’s), succeeding a Dr Arthur who died in a fire; his last tool was a failed curse meant to control its target; he sold Venedict Rain to a patron called 閣下, defined himself against Thornley, and died by his own curse; 閣下 is unidentified. (V07) | V07 obs. 197–199, 202. | See V07 reading section 9.1. | Revision on new evidence. |
| SW-CR-0252 | SW-C-0040 | The volume assigns Eliane moral responsibility for acts partly amplified by a curse, and lets her go unexamined in the world. (prior) | PRESERVE | Unchanged (V07) | See V07 reading section 9.1. | — | Review, not change. |
| SW-CR-0253 | SW-C-0041 | The companion argues that charms work by giving the user courage through something special; Monica, who rejected the theory, makes and keeps charms herself, and the inverse case of a curse taken for a charm shows the danger of not knowing what one holds. (prior) | PRESERVE | Unchanged (V07) | See V07 reading section 9.1. | — | Review, not change. |
| SW-CR-0254 | SW-C-0042 | Monica’s power was visible only to a spirit and the reader while she lived as Monica Norton; acting openly as the Silent Witch, her concealment fails before Felix, whose inferences outpace her small lies. (prior) | PRESERVE | Unchanged (V07) | See V07 reading section 9.1. | — | Review, not change. |
| SW-CR-0255 | SW-C-0043 | Cyril’s ethic of earned, patient effort is set against Louis’s maxim of money, violence and strength; Glen and Monica, who drifted into magic, take Cyril’s side. (prior) | STRENGTHEN | Wording unchanged; support extended (V07) | See V07 reading section 9.1. | — | Strengthened. |
| SW-CR-0256 | SW-C-0044 | Elliott’s creed of rank rests on an uncle’s suicide and a further event before he was ten that he withholds; his own friendship contradicts it. (prior) | PRESERVE | Unchanged (V07) | See V07 reading section 9.1. | — | Review, not change. |
| SW-CR-0257 | SW-C-0045 | Monica’s father was framed by a curse-caster under a powerful patron, and her purpose widens from the mission to proving his innocence. (prior) | STRENGTHEN | Wording unchanged; support extended (V07) | See V07 reading section 9.1. | — | Strengthened. |
| SW-CR-0258 | SW-C-0046 | Monica’s concealment fails in three directions in one break: Bartholomeus, Felix’s inference of her school, and Felix’s knowledge of her familiar. (prior) | STRENGTHEN | Wording unchanged; support extended (V07) | See V07 reading section 9.1. | — | Strengthened. |
| SW-CR-0259 | SW-C-0047 | Felix believes his grandfather stages his heroism and means to make him a true puppet; he performs obedience and plans resistance; at V06 Clockford tells the Silent Witch that Felix moves at his will, while Felix, unaware of that offer, acts on his own hard judgement, including an order to kill and a plan to use Emmanuel. (prior) | STRENGTHEN | Wording unchanged; support extended (V07) | See V07 reading section 9.1. | — | Strengthened. |
| SW-CR-0260 | SW-C-0048 | The volume is framed by Louis’s lesson that the game begins before the table, which Monica learns by losing. (prior) | PRESERVE | Unchanged (V07) | See V07 reading section 9.1. | — | Review, not change. |
| SW-CR-0261 | SW-C-0049 | Vows made before a witness organize the volume, and the chime sounds for each. (prior) | PRESERVE | Unchanged (V07) | See V07 reading section 9.1. | — | Review, not change. |
| SW-CR-0262 | SW-C-0050 | The cluster around Felix gains the contract stone, the water spirit against an earth name, the eye colour and a vow ending in Arc. (prior) | STRENGTHEN | Wording unchanged; support extended (V07) | See V07 reading section 9.1. | — | Strengthened. |
| SW-CR-0263 | SW-C-0051 | Monica’s anger moves from an unnamed loss of control to a recognized feeling with a cause, and Louis licenses it; the volume does not judge it. (prior) | PRESERVE | Unchanged (V07) | See V07 reading section 9.1. | — | Review, not change. |
| SW-CR-0264 | SW-C-0052 | The volume repeatedly poses whether one may ask for help; Monica is urged to and does not yet do so. (prior) | REVISE | The volume repeatedly poses whether one may ask for help; Monica is urged to in V06 and first asks, of Bartholomeus, at the opening of V07. (V07) | V07 obs. 005. | See V07 reading section 9.1. | Revision on new evidence. |
| SW-CR-0265 | SW-C-0053 | From three partial reports Monica infers that Clockford is likely connected to her father’s death; the volume confirms neither the staging, 閣下, the great noble nor Emmanuel’s patron. (prior) | REVISE | From three partial reports Monica infers that Clockford is likely connected to her father’s death; the volume confirms neither the staging, 閣下 nor the great noble. Emmanuel’s patron is identified as Clockford by his own usage, SW-C-0057. (V07) | V07 obs. 058; S15:E000458. | See V07 reading section 9.1. | Revision on new evidence. |
| SW-CR-0266 | SW-C-0054 | The Seven Sages hide a member’s crime to keep their independence from the noble assembly; the volume presents this as self-protection, not justice. (prior) | STRENGTHEN | Wording unchanged; support extended (V07) | See V07 reading section 9.1. | — | Strengthened. |
| SW-CR-0267 | SW-C-0055 | Hubert’s imitation makes chantless magic a threat in others’ eyes and a thing of little worth in Monica’s; the plate’s words are his. (prior) | PRESERVE | Unchanged (V07) | See V07 reading section 9.1. | — | Review, not change. |
| SW-CR-0268 | SW-C-0056 | Felix pairs ruthless means with a wish to be relied on, and overlays a remembered friend on Monica. (prior) | STRENGTHEN | Wording unchanged; support extended (V07) | See V07 reading section 9.1. | — | Strengthened. |

Revision records at V08, 2026-10-14, reviewer the V08 sequential integrator:

| Revision | Claim | Earlier formulation and boundary | Transition | New formulation and boundary | Reason | Affected homes | Kind |
|---|---|---|---|---|---|---|---|
| SW-CR-0269 | SW-C-0001 | Chantless casting began as avoidance of speech, and silence and mastery are one mechanism; the avoidance has an earlier root in childhood punishment for speaking; before Minerva a year of abuse produced a dissociation in which she lost language, ended by Hilda Everett’s rescue; its occasion at Minerva was a friend’s plan to shorten her chant; the public account explains the capacity as instant computation. (prior) | PRESERVE | Unchanged (V08) | See V08 reading section 9.1. | — | Review, not change. |
| SW-CR-0270 | SW-C-0002 | Pain, fear or exposure drive Monica into numerical absorption; the habit began as a child’s escape from her uncle into her father’s formulas and a vow to keep his numbers; she uses it to compute combat and to bear people, it fails when people she knows are threatened, and she now turns it outward as evidence, naming it no longer a refuge. (prior) | PRESERVE | Unchanged (V08) | See V08 reading section 9.1. | — | Review, not change. |
| SW-CR-0271 | SW-C-0003 | Monica’s paternal uncle, after her father’s execution when she was ten, beat and starved her, shut her in a winter barn and forbade her to defend her father, for about a year until Hilda Everett took her; scars remain and touch still frightens her. (prior) | PRESERVE | Unchanged (V08) | See V08 reading section 9.1. | — | Review, not change. |
| SW-CR-0272 | SW-C-0004 | The makeweight self-assessment is contradicted by Louis’s memory of the duel; the examiners’ ranking is unstated. (prior) | PRESERVE | Unchanged (V08) | See V08 reading section 9.1. | — | Review, not change. |
| SW-CR-0273 | SW-C-0005 | Stated protection; Monica doubts it; Louis reads surveillance, uses a decoy, chose Monica because she distrusts, fears and hates people and can therefore be merciless, and calls himself first-prince because he dislikes the duke and Felix; the king is unshown. (prior) | PRESERVE | Unchanged (V08) | See V08 reading section 9.1. | — | Review, not change. |
| SW-CR-0274 | SW-C-0006 | The prologue’s watcher is Felix. (prior) | STRENGTHEN | Wording unchanged; support extended (V08) | V08 obs. 172–175: the wyvern scene retold from his side. | — | Strengthened. |
| SW-CR-0275 | SW-C-0007 | Public and private selves diverge: he denies a talent for magic while studying it in secret because it is forbidden to him, and hides a spirit; he obeys the duke outwardly while removing his placements and gathering nobles who resent him; he must become king without wanting it, under a ten-year vow to make the name Felix Arc Ridill remembered, which he now expresses as a hero’s posthumous light and pursues even against his dead friend’s wish. (prior) | STRENGTHEN | Wording unchanged; support extended (V08) | V08 obs. 153, 160: magic forbidden because affinities differ. | — | Strengthened. |
| SW-CR-0276 | SW-C-0008 | Felix has not identified Monica as the Silent Witch; at V03 exit he admires the Witch’s magic as a first love, has never seen her face, spent the festival night with Monica, briefly suspected her of being an assassin, and still does not connect them. (prior) | REVISE | Felix has not identified Monica as the Silent Witch; at V03 exit he admires the Witch’s magic as a first love, has never seen her face, spent the festival night with Monica, briefly suspected her of being an assassin, and still does not connect them; at V08 he learns that Monica Norton is Venedict Rain’s daughter and that the Silent Witch knows his name, and is not shown to connect the two. (V08) | V08 obs. 199, 259, 261. | See V08 reading section 9.1. | Revision on new evidence. |
| SW-CR-0277 | SW-C-0009 | Cyril holds an unverified suspicion from her hand and remark (V01), links the forest mage with the Silent Witch (V02), and at V04 notices unexplained magical ice and her small, pen-callused hand; at V06 he senses he has met the Witch, notices her injured left hand and Monica’s repeatedly flexed one, and before fainting hears Hubert call the small figure in the fog the Silent Witch; at V07 he learns from Ray that the Witch’s left hand is cursed and remembers her shielding it; no conclusion is shown. (prior) | REVISE | Cyril held an unverified suspicion that grew through V01 to V07 without a conclusion; at the close of V08 Monica reveals herself as the Silent Witch to the council with Cyril present; his response is not shown. (V08) | V08 obs. 290, 291. | See V08 reading section 9.1. | Revision on new evidence. |
| SW-CR-0278 | SW-C-0010 | Awe at Monica’s power is narrated through external focalizers; from V02 her own viewpoint also narrates her power, as calculation under constraint; V03 extends this to sustained combat computation and gives her first chantless casting from a rival’s view. (prior) | STRENGTHEN | Wording unchanged; support extended (V08) | V08 obs. 050, 061: calculation against the emperor. | — | Strengthened. |
| SW-CR-0279 | SW-C-0011 | The school treats rank as epistemic authority; Cyril’s inquiry is the first counterexample; at V02 rank is also used as a weapon of justice (Felix, Isabelle) and Elliott’s code ties rank to duty; at V03 Elliott’s contempt for upstarts has a biographical root and he warns that talent crossing class walls is envied or used. (prior) | STRENGTHEN | Wording unchanged; support extended (V08) | V08 obs. 252: power decides what is true. | — | Strengthened. |
| SW-CR-0280 | SW-C-0012 | Organized embezzlement; erased Aaron’s and Cyril’s memories; Selma’s manipulation inferred; at V04 a traitor curse-caster reveals that Thornley worked for a patron called 閣下 through mind interference and was discarded. (prior) | PRESERVE | Unchanged (V08) | See V08 reading section 9.1. | — | Review, not change. |
| SW-CR-0281 | SW-C-0013 | Nero is the Worgan black dragon, driven from the Empire’s mountains, worshipped but not commanded by the wyverns, and Monica’s familiar by his own choice after she pulled a bone from his throat; he can use black flame only in his true form. (prior) | STRENGTHEN | Wording unchanged; support extended (V08) | V08 obs. 237, 257: dragon-form flight; Isaac knows him. | — | Strengthened. |
| SW-CR-0282 | SW-C-0014 | Monica regards her talent as a curse that took her father and friend; her father, Venedict Rain, author of a book on heredity and magical properties, was executed as a heretic when Monica was ten and his book burned; the friend, Bernie Jones, needed her dependence, turned away in envy, sent her to the hut, and wanted to be her equal rival; she has renounced his approval. Correction: the V03 formulation dated the execution five years before the present, but the V03 text dates only the book’s publication. (prior) | PRESERVE | Unchanged (V08) | See V08 reading section 9.1. | — | Review, not change. |
| SW-CR-0283 | SW-C-0015 | The bond with Lana rests on shared experience of being called boring and being out of place, and on mutual gestures of giving; Lana began from pride and stays from affection; at V03 Lana arms and defends her, and Monica defends Lana first. (prior) | STRENGTHEN | Wording unchanged; support extended (V08) | V08 obs. 274: the farewell to Lana. | — | Strengthened. |
| SW-CR-0284 | SW-C-0016 | The comedy of coercion registers harm in most cases; the non-consensual kiss is unevaluated and unknown to its recipient. (prior) | PRESERVE | Unchanged (V08) | See V08 reading section 9.1. | — | Review, not change. |
| SW-CR-0285 | SW-C-0017 | Louis combines coercion with investment in her self-respect and his own pride; at V02 also gifts, an unknowing decoy, and a concession calculated to keep her cooperation; at V03 he lends Lynn and, to Casey, judges her a heartless witch. (prior) | STRENGTHEN | Wording unchanged; support extended (V08) | V08 obs. 188, 210: Louis withholds his plan. | — | Strengthened. |
| SW-CR-0286 | SW-C-0018 | Monica’s numerical perception and comfort derive from her father’s teaching; his saying that the world is made of numbers became her means of fleeing reality under her uncle; she memorized his burning numbers and keeps his coffee pot; at V04 she refuses the saying as an excuse. (prior) | PRESERVE | Unchanged (V08) | See V08 reading section 9.1. | — | Review, not change. |
| SW-CR-0287 | SW-C-0019 | Casey Grove is the prologue’s unnamed conspirator, acting on Count Bright’s order with a 螺炎, from grievance at central neglect and gratitude to Randall; her friendship was begun instrumentally; at V03 Count Bright claims sole responsibility, Louis suspects Randall and the Empire, and Casey asks after Monica and sends her a package, so that her feeling is evidenced as concern and its history remains OPEN. (prior) | PRESERVE | Unchanged (V08) | See V08 reading section 9.1. | — | Review, not change. |
| SW-CR-0288 | SW-C-0020 | Monica derives a concept of duty from Elliott’s noblesse oblige and transposes it to her roles as treasurer and Sage; at V03 duty is joined by a personal motive she calls selfish, that the bereaved be able to mourn as she could not. (prior) | PRESERVE | Unchanged (V08) | See V08 reading section 9.1. | — | Review, not change. |
| SW-CR-0289 | SW-C-0021 | Monica’s concealment is a political bargain using Louis’s factional logic, at a cost to Cyril and her conscience; the volume presents it sympathetically and leaves its justice unjudged; at V03 Cyril still blames himself and she cannot clear him. (prior) | PRESERVE | Unchanged (V08) | See V08 reading section 9.1. | — | Review, not change. |
| SW-CR-0290 | SW-C-0022 | A cluster of unexplained details surrounds Felix’s identity and history: Bridget’s childhood test; his memory of a boy apologizing as a royal; the role held while he bears the name; the seer’s blindness to his star from about ten years ago; Elliott’s memory of a sickly, clumsy, shy, light-eyed, star-loving child scarred in the side with a more poised attendant; a ten-year vow to inscribe the name in history; a dead friend whose wish he pursues; a dream of a boy called Felix, a page and a burned astronomy book; a necessary scar. No hypothesis is registered. (prior) | REVISE | The cluster of details around Felix’s identity and history, held without hypothesis from V02 to V07, is explained in V08 by narration: the present Felix is the page Isaac Walker, remade by body manipulation after the real prince’s death about ten years ago; see SW-C-0063. (V08) | V08 obs. 097, 143–150; section 6.2. | See V08 reading section 9.1. | Revision on new evidence. |
| SW-CR-0291 | SW-C-0023 | Monica says she cannot expect anything of anyone, while her conduct shows growing attachment; no romantic interest on her side is shown and she does not wish to marry; Felix’s absorption in the Silent Witch as an idea is now joined, in his own viewpoint, by attachment and jealousy toward Monica herself. (prior) | STRENGTHEN | Wording unchanged; support extended (V08) | V08 obs. 240: she cannot name what Isaac is to her. | — | Strengthened. |
| SW-CR-0292 | SW-C-0024 | Louis chose Monica for her distrust, fear and hatred of people, calls her heartless, and reads her attachment as a risk; Monica shares the warning that Monica Norton is temporary, and at V03 expected her false school life to end. (prior) | REVISE | Louis chose Monica for her distrust, fear and hatred of people, calls her heartless, and reads her attachment as a risk; Monica shared the warning that Monica Norton is temporary; at V08 she ends it herself by revealing her identity to her council and asking their help. (V08) | V08 obs. 274, 283, 290, 291. | See V08 reading section 9.1. | Revision on new evidence. |
| SW-CR-0293 | SW-C-0025 | Isabelle’s cover-bullying is a deliberate deterrence policy and her revenge mirrors the crime; the volume treats humiliation as justice. (prior) | PRESERVE | Unchanged (V08) | See V08 reading section 9.1. | — | Review, not change. |
| SW-CR-0294 | SW-C-0026 | 場違い organizes the social plot through three outsiders by class or region, Monica, Lana and Casey, reversing from exclusion to self-gift. (prior) | PRESERVE | Unchanged (V08) | See V08 reading section 9.1. | — | Review, not change. |
| SW-CR-0295 | SW-C-0027 | Bernie Jones is the Minerva friend; his help coexisted with a wish for her dependence; his envy ended the friendship and his curse began the hut life; he protected her cover as a noble’s duty, wanted to be her equal rival, and leaves Minerva as heir offering future help. (prior) | PRESERVE | Unchanged (V08) | See V08 reading section 9.1. | — | Review, not change. |
| SW-CR-0296 | SW-C-0028 | Mourning organizes V03: Monica’s motive in the climax is that the bereaved be able to mourn as she could not; burned books and festival bells join her strand and Felix’s. (prior) | PRESERVE | Unchanged (V08) | See V08 reading section 9.1. | — | Review, not change. |
| SW-CR-0297 | SW-C-0029 | Ike is a persona in which Felix shows Monica a self outside his role; her answering self-description as a ghost was her first outreach; the persona persists in private moments after the festival night, and Monica keeps its confidences from Louis. (prior) | REVISE | Ike is the childhood name the real prince used for his page Isaac Walker; as Ike, the present Felix shows Monica the self outside his role; her answering self-description as a ghost was her first outreach; the persona persists in private moments, and Monica keeps its confidences from Louis. (V08) | V08 obs. 042, 115. | See V08 reading section 9.1. | Revision on new evidence. |
| SW-CR-0298 | SW-C-0030 | The duke dominates Felix by contempt and, in Felix’s dream, by punishing those the boy cares for; Felix obeys outwardly while gathering nobles who resent the duke. (prior) | REVISE | The duke dominated the boy by contempt and punished those the boy cared for; he took Isaac to replace the prince, cut a scar into him and calls him a tool; Isaac obeyed outwardly while gathering nobles who covet the duke’s place, and at V08 plots the duke’s death, after which the duke discards him. (V08) | V08 obs. 106, 123, 093, 090, 205. | See V08 reading section 9.1. | Revision on new evidence. |
| SW-CR-0299 | SW-C-0031 | Imperial agents Yuan and Heidi, serving a master, used imperial body magic, impersonated Pittman and then Cyril, sought a trace on Felix that Yuan attributes to a traitor Arthur and the capture of the Silent Witch, threatened war, and escaped with Yuan cursed for at least a month; Louis suspects a Randall–Empire alliance. (prior) | REVISE | Imperial agents Yuan and Heidi serve the young emperor Leonhardt, who wants to avoid war by exposing the false prince at his accession; Yuan pursued Artur, his former friend who stole his body-manipulation research and served Clockford as the physician Arthur; the emperor came to Ridill himself and bargained with Monica. (V08) | V08 obs. 037, 054, 059, 064. | See V08 reading section 9.1. | Revision on new evidence. |
| SW-CR-0300 | SW-C-0032 | Monica’s father was Venedict Rain, author of a book on heredity and magical properties, executed seven years ago, when Monica was ten, after a curse-caster he refused had him charged with necromancy on planted evidence, under a great noble’s pressure and without trial; his former assistant Hilda Everett adopted her; his friend Porter is Dustin Günther. The V04 correction stands. (prior) | STRENGTHEN | Wording unchanged; support extended (V08) | V08 obs. 001–006: the prologue of his arrest. | — | Strengthened. |
| SW-CR-0301 | SW-C-0033 | Louis’s model of Monica as a heartless witch who sees people as numbers is half right: she accepts it and uses it as a technique, then fails to apply it to the people she knows; Louis says her humanity does not matter to him either way. (prior) | STRENGTHEN | Wording unchanged; support extended (V08) | V08 obs. 188: Louis thinks her soft. | — | Strengthened. |
| SW-CR-0302 | SW-C-0034 | Mary deliberately allowed the theft of the ancient tool, citing the stars’ guidance, and used the crisis to test Monica; the volume does not judge the risk to the town or the bystander. (prior) | PRESERVE | Unchanged (V08) | See V08 reading section 9.1. | — | Review, not change. |
| SW-CR-0303 | SW-C-0035 | Monica’s numerical dissociation, born of abuse, became a chosen weapon and a limit, and now also a means of evidence; she remains Monica Norton knowing it deceives her friends, and her purpose widens to her father’s innocence. (prior) | PRESERVE | Unchanged (V08) | See V08 reading section 9.1. | — | Review, not change. |
| SW-CR-0304 | SW-C-0036 | V04 is organized by gifts whose meaning differs between giver and receiver: the rose, the cursed necklace, the pendant, the handkerchief and the friend’s wish. (prior) | PRESERVE | Unchanged (V08) | See V08 reading section 9.1. | — | Review, not change. |
| SW-CR-0305 | SW-C-0037 | Cyril’s history mirrors Monica’s: a violent father, withheld praise and striving for recognition; his care for her is a disguised invitation and practical help, and his attention returns to her hand. (prior) | STRENGTHEN | Wording unchanged; support extended (V08) | V08 obs. 193, 228: praise and its return. | — | Strengthened. |
| SW-CR-0306 | SW-C-0038 | Felix’s wish to be remembered tends toward a hero’s posthumous light and overrides his dead friend’s wish for him; Monica perceives obsession. (prior) | REVISE | The present Felix’s wish to be remembered is a wish that the dead prince’s name not be forgotten; it takes the form of a hero’s posthumous light and overrides the prince’s own last wish, that Isaac find happiness for himself; Monica perceives obsession. (V08) | V08 obs. 114, 140, 148, 166, 168. | See V08 reading section 9.1. | Revision on new evidence. |
| SW-CR-0307 | SW-C-0039 | The traitor curse-caster was Barry Oates, serving at Leinbourg as the footman Peter Sams; before Leinbourg he served at Duke Clockford’s house as a physician or researcher, from about ten years ago by the gardener’s account (about eight by Bartholomeus’s), succeeding a Dr Arthur who died in a fire; his last tool was a failed curse meant to control its target; he sold Venedict Rain to a patron called 閣下, defined himself against Thornley, and died by his own curse; 閣下 is unidentified. (prior) | REVISE | The traitor curse-caster was Barry Oates, serving at Leinbourg as the footman Peter Sams; he denounced Venedict Rain; before Leinbourg he served at Clockford’s house from about ten years ago, after Clockford killed the physician Arthur; he sold Rain to a patron called 閣下, and died by his own curse; 閣下 is unidentified. (V08) | V08 obs. 005, 156. | See V08 reading section 9.1. | Revision on new evidence. |
| SW-CR-0308 | SW-C-0040 | The volume assigns Eliane moral responsibility for acts partly amplified by a curse, and lets her go unexamined in the world. (prior) | PRESERVE | Unchanged (V08) | See V08 reading section 9.1. | — | Review, not change. |
| SW-CR-0309 | SW-C-0041 | The companion argues that charms work by giving the user courage through something special; Monica, who rejected the theory, makes and keeps charms herself, and the inverse case of a curse taken for a charm shows the danger of not knowing what one holds. (prior) | STRENGTHEN | Wording unchanged; support extended (V08) | V08 obs. 283: the dried rose as a charm. | — | Strengthened. |
| SW-CR-0310 | SW-C-0042 | Monica’s power was visible only to a spirit and the reader while she lived as Monica Norton; acting openly as the Silent Witch, her concealment fails before Felix, whose inferences outpace her small lies. (prior) | STRENGTHEN | Wording unchanged; support extended (V08) | V08 obs. 290: she acts openly as the Witch. | — | Strengthened. |
| SW-CR-0311 | SW-C-0043 | Cyril’s ethic of earned, patient effort is set against Louis’s maxim of money, violence and strength; Glen and Monica, who drifted into magic, take Cyril’s side. (prior) | STRENGTHEN | Wording unchanged; support extended (V08) | V08 obs. 226: Elliott concedes effort and talent. | — | Strengthened. |
| SW-CR-0312 | SW-C-0044 | Elliott’s creed of rank rests on an uncle’s suicide and a further event before he was ten that he withholds; his own friendship contradicts it. (prior) | REVISE | Elliott’s creed of rank rests on an uncle’s suicide and on what he saw before he was ten; the talented commoner he once said was ruined by cunning people is Isaac Walker, by his own acknowledgement; his own friendship contradicts it, and he cannot call Isaac a fool. (V08) | V08 obs. 216, 219–223, 226. | See V08 reading section 9.1. | Revision on new evidence. |
| SW-CR-0313 | SW-C-0045 | Monica’s father was framed by a curse-caster under a powerful patron, and her purpose widens from the mission to proving his innocence. (prior) | REVISE | Monica’s father was framed through a curse-caster’s denunciation; the narration states that Clockford had a part in his death, and Monica, Porter and Isaac conclude that the motive was his design for a tool that could expose the false prince; her purpose widens to proving his innocence, and she subordinates it to saving Isaac. (V08) | V08 obs. 005, 078, 199, 253, 265. | See V08 reading section 9.1. | Revision on new evidence. |
| SW-CR-0314 | SW-C-0046 | Monica’s concealment fails in three directions in one break: Bartholomeus, Felix’s inference of her school, and Felix’s knowledge of her familiar. (prior) | STRENGTHEN | Wording unchanged; support extended (V08) | V08 obs. 084, 259: Porter and Isaac learn. | — | Strengthened. |
| SW-CR-0315 | SW-C-0047 | Felix believes his grandfather stages his heroism and means to make him a true puppet; he performs obedience and plans resistance; at V06 Clockford tells the Silent Witch that Felix moves at his will, while Felix, unaware of that offer, acts on his own hard judgement, including an order to kill and a plan to use Emmanuel. (prior) | REVISE | The present Felix believed his grandfather staged his heroism and meant to make him a true puppet; at V08 he suborns Emmanuel to kill the duke; the duke, having had puppet curses researched, sets a trap, kills Emmanuel and discards him. (V08) | V08 obs. 090, 190, 191, 206. | See V08 reading section 9.1. | Revision on new evidence. |
| SW-CR-0316 | SW-C-0048 | The volume is framed by Louis’s lesson that the game begins before the table, which Monica learns by losing. (prior) | PRESERVE | Unchanged (V08) | See V08 reading section 9.1. | — | Review, not change. |
| SW-CR-0317 | SW-C-0049 | Vows made before a witness organize the volume, and the chime sounds for each. (prior) | STRENGTHEN | Wording unchanged; support extended (V08) | V08 obs. 100, 140, 249: promises to the father, the prince and Casey. | — | Strengthened. |
| SW-CR-0318 | SW-C-0050 | The cluster around Felix gains the contract stone, the water spirit against an earth name, the eye colour and a vow ending in Arc. (prior) | REVISE | The contract stone, the water spirit against an earth name, the eye colour and a vow ending in Arc are explained at V08: the stone and spirit were Queen Irene’s, given by the real prince to Isaac; the prince’s affinity was earth; the eye colour differs between the two boys; Arc is the prince’s middle name used as his secret name. (V08) | V08 obs. 115, 130, 141, 160–165, 219. | See V08 reading section 9.1. | Revision on new evidence. |
| SW-CR-0319 | SW-C-0051 | Monica’s anger moves from an unnamed loss of control to a recognized feeling with a cause, and Louis licenses it; the volume does not judge it. (prior) | PRESERVE | Unchanged (V08) | See V08 reading section 9.1. | — | Review, not change. |
| SW-CR-0320 | SW-C-0052 | The volume repeatedly poses whether one may ask for help; Monica is urged to in V06 and first asks, of Bartholomeus, at the opening of V07. (prior) | STRENGTHEN | Wording unchanged; support extended (V08) | V08 obs. 033, 271, 291: help asked repeatedly. | — | Strengthened. |
| SW-CR-0321 | SW-C-0053 | From three partial reports Monica infers that Clockford is likely connected to her father’s death; the volume confirms neither the staging, 閣下 nor the great noble. Emmanuel’s patron is identified as Clockford by his own usage, SW-C-0057. (prior) | REVISE | Monica infers Clockford’s connection to her father’s death; at V08 the narration states that Clockford had a part in it, and she, Porter and Isaac give the motive; 閣下 remains unidentified. Emmanuel’s patron is Clockford, SW-C-0057. (V08) | V08 obs. 078, 265. | See V08 reading section 9.1. | Revision on new evidence. |
| SW-CR-0322 | SW-C-0054 | The Seven Sages hide a member’s crime to keep their independence from the noble assembly; the volume presents this as self-protection, not justice. (prior) | STRENGTHEN | Wording unchanged; support extended (V08) | V08 obs. 252: the Sages accept the false story. | — | Strengthened. |
| SW-CR-0323 | SW-C-0055 | Hubert’s imitation makes chantless magic a threat in others’ eyes and a thing of little worth in Monica’s; the plate’s words are his. (prior) | PRESERVE | Unchanged (V08) | See V08 reading section 9.1. | — | Review, not change. |
| SW-CR-0324 | SW-C-0056 | Felix pairs ruthless means with a wish to be relied on, and overlays a remembered friend on Monica. (prior) | STRENGTHEN | Wording unchanged; support extended (V08) | V08 obs. 090, 202: ruthless means; the wish to be relied on. | — | Strengthened. |
| SW-CR-0325 | SW-C-0057 | Emmanuel’s patron, called あの方 in his thoughts, is Duke Clockford; the identification rests on the same speaker’s usage in V06 and V07 and is not extended to 閣下 or the great noble. (prior) | STRENGTHEN | Wording unchanged; support extended (V08) | V08 obs. 089: Emmanuel fears Clockford’s discard. | — | Strengthened. |
| SW-CR-0326 | SW-C-0058 | V07 gathers around Felix an account of a sickly, timid child; an illness and a fire about ten years ago in which his page Isaac Walker and a Dr Arthur died; Mary’s lost sight of his fate; and Bridget’s belief that he is false. No identification is registered. (prior) | REVISE | V07’s account of Felix’s past (a sickly child, an illness and a fire, Mary’s lost star, Bridget’s belief) is explained at V08: the child was the real prince, who died by a fall; the fire burned his body and Arthur’s; the present Felix is the page Isaac Walker. (V08) | V08 obs. 143–157; SW-C-0063. | See V08 reading section 9.1. | Revision on new evidence. |
| SW-CR-0327 | SW-C-0059 | Monica asks for help and wants to know another person for the first time, each by her own decision. (prior) | STRENGTHEN | Wording unchanged; support extended (V08) | V08 obs. 235, 241: to know and to save. | — | Strengthened. |
| SW-CR-0328 | SW-C-0060 | The volume sets uniqueness against competence and cooperation, and favours the latter. (prior) | PRESERVE | Unchanged (V08) | See V08 reading section 9.1. | — | Review, not change. |
| SW-CR-0329 | SW-C-0061 | Whether humans can help spirits is argued without resolution; Monica’s rescue of Romaria is presented as her ego. (prior) | PRESERVE | Unchanged (V08) | See V08 reading section 9.1. | — | Review, not change. |
| SW-CR-0330 | SW-C-0062 | The Sages act as one in the forest and conceal from one another throughout. (prior) | STRENGTHEN | Wording unchanged; support extended (V08) | V08 obs. 187, 253: Louis and Monica conceal their plans. | — | Strengthened. |

Revision records at V09, 2026-10-14, reviewer the V09 sequential integrator:

| Revision | Claim | Earlier formulation and boundary | Transition | New formulation and boundary | Reason | Affected homes | Kind |
|---|---|---|---|---|---|---|---|
| SW-CR-0331 | SW-C-0001 | Chantless casting began as avoidance of speech, and silence and mastery are one mechanism; the avoidance has an earlier root in childhood punishment for speaking; before Minerva a year of abuse produced a dissociation in which she lost language, ended by Hilda Everett’s rescue; its occasion at Minerva was a friend’s plan to shorten her chant; the public account explains the capacity as instant computation. (prior) | PRESERVE | Unchanged (V09) | See V09 reading section 9.1. | — | Review, not change. |
| SW-CR-0332 | SW-C-0002 | Pain, fear or exposure drive Monica into numerical absorption; the habit began as a child’s escape from her uncle into her father’s formulas and a vow to keep his numbers; she uses it to compute combat and to bear people, it fails when people she knows are threatened, and she now turns it outward as evidence, naming it no longer a refuge. (prior) | PRESERVE | Unchanged (V09) | See V09 reading section 9.1. | — | Review, not change. |
| SW-CR-0333 | SW-C-0003 | Monica’s paternal uncle, after her father’s execution when she was ten, beat and starved her, shut her in a winter barn and forbade her to defend her father, for about a year until Hilda Everett took her; scars remain and touch still frightens her. (prior) | PRESERVE | Unchanged (V09) | See V09 reading section 9.1. | — | Review, not change. |
| SW-CR-0334 | SW-C-0004 | The makeweight self-assessment is contradicted by Louis’s memory of the duel; the examiners’ ranking is unstated. (prior) | PRESERVE | Unchanged (V09) | See V09 reading section 9.1. | — | Review, not change. |
| SW-CR-0335 | SW-C-0005 | Stated protection; Monica doubts it; Louis reads surveillance, uses a decoy, chose Monica because she distrusts, fears and hates people and can therefore be merciless, and calls himself first-prince because he dislikes the duke and Felix; the king is unshown. (prior) | STRENGTHEN | Wording unchanged; support extended (V09) | V09 obs. 106: the king set Louis to probe the prince. | — | Strengthened. |
| SW-CR-0336 | SW-C-0006 | The prologue’s watcher is Felix. (prior) | PRESERVE | Unchanged (V09) | See V09 reading section 9.1. | — | Review, not change. |
| SW-CR-0337 | SW-C-0007 | Public and private selves diverge: he denies a talent for magic while studying it in secret because it is forbidden to him, and hides a spirit; he obeys the duke outwardly while removing his placements and gathering nobles who resent him; he must become king without wanting it, under a ten-year vow to make the name Felix Arc Ridill remembered, which he now expresses as a hero’s posthumous light and pursues even against his dead friend’s wish. (prior) | PRESERVE | Unchanged (V09) | See V09 reading section 9.1. | — | Review, not change. |
| SW-CR-0338 | SW-C-0008 | Felix has not identified Monica as the Silent Witch; at V03 exit he admires the Witch’s magic as a first love, has never seen her face, spent the festival night with Monica, briefly suspected her of being an assassin, and still does not connect them; at V08 he learns that Monica Norton is Venedict Rain’s daughter and that the Silent Witch knows his name, and is not shown to connect the two. (prior) | REVISE | Felix did not identify Monica as the Silent Witch from V01 to V08, though he admired the Witch and grew close to Monica; at V09 he recognizes her when she enters the Supreme Council, and calls himself a fool for not seeing it. (V09) | V09 obs. 080, 081. | See V09 reading section 9.1. | Revision on new evidence. |
| SW-CR-0339 | SW-C-0009 | Cyril held an unverified suspicion that grew through V01 to V07 without a conclusion; at the close of V08 Monica reveals herself as the Silent Witch to the council with Cyril present; his response is not shown. (prior) | REVISE | Cyril held an unverified suspicion from V01 to V08; when Monica reveals herself at V09 he says he had half guessed from her hand and the hooded figure, kneels to apologize, and returns to scolding her as his junior. (V09) | V09 obs. 008, 011. | See V09 reading section 9.1. | Revision on new evidence. |
| SW-CR-0340 | SW-C-0010 | Awe at Monica’s power is narrated through external focalizers; from V02 her own viewpoint also narrates her power, as calculation under constraint; V03 extends this to sustained combat computation and gives her first chantless casting from a rival’s view. (prior) | STRENGTHEN | Wording unchanged; support extended (V09) | V09 obs. 007, 052: power shown chantlessly and remotely. | — | Strengthened. |
| SW-CR-0341 | SW-C-0011 | The school treats rank as epistemic authority; Cyril’s inquiry is the first counterexample; at V02 rank is also used as a weapon of justice (Felix, Isabelle) and Elliott’s code ties rank to duty; at V03 Elliott’s contempt for upstarts has a biographical root and he warns that talent crossing class walls is envied or used. (prior) | STRENGTHEN | Wording unchanged; support extended (V09) | V09 obs. 096: power makes truth, used. | — | Strengthened. |
| SW-CR-0342 | SW-C-0012 | Organized embezzlement; erased Aaron’s and Cyril’s memories; Selma’s manipulation inferred; at V04 a traitor curse-caster reveals that Thornley worked for a patron called 閣下 through mind interference and was discarded. (prior) | PRESERVE | Unchanged (V09) | See V09 reading section 9.1. | — | Review, not change. |
| SW-CR-0343 | SW-C-0013 | Nero is the Worgan black dragon, driven from the Empire’s mountains, worshipped but not commanded by the wyverns, and Monica’s familiar by his own choice after she pulled a bone from his throat; he can use black flame only in his true form. (prior) | PRESERVE | Unchanged (V09) | See V09 reading section 9.1. | — | Review, not change. |
| SW-CR-0344 | SW-C-0014 | Monica regards her talent as a curse that took her father and friend; her father, Venedict Rain, author of a book on heredity and magical properties, was executed as a heretic when Monica was ten and his book burned; the friend, Bernie Jones, needed her dependence, turned away in envy, sent her to the hut, and wanted to be her equal rival; she has renounced his approval. Correction: the V03 formulation dated the execution five years before the present, but the V03 text dates only the book’s publication. (prior) | PRESERVE | Unchanged (V09) | See V09 reading section 9.1. | — | Review, not change. |
| SW-CR-0345 | SW-C-0015 | The bond with Lana rests on shared experience of being called boring and being out of place, and on mutual gestures of giving; Lana began from pride and stays from affection; at V03 Lana arms and defends her, and Monica defends Lana first. (prior) | STRENGTHEN | Wording unchanged; support extended (V09) | V09 obs. 010, 151: friendship kept and pursued. | — | Strengthened. |
| SW-CR-0346 | SW-C-0016 | The comedy of coercion registers harm in most cases; the non-consensual kiss is unevaluated and unknown to its recipient. (prior) | PRESERVE | Unchanged (V09) | See V09 reading section 9.1. | — | Review, not change. |
| SW-CR-0347 | SW-C-0017 | Louis combines coercion with investment in her self-respect and his own pride; at V02 also gifts, an unknowing decoy, and a concession calculated to keep her cooperation; at V03 he lends Lynn and, to Casey, judges her a heartless witch. (prior) | PRESERVE | Unchanged (V09) | See V09 reading section 9.1. | — | Review, not change. |
| SW-CR-0348 | SW-C-0018 | Monica’s numerical perception and comfort derive from her father’s teaching; his saying that the world is made of numbers became her means of fleeing reality under her uncle; she memorized his burning numbers and keeps his coffee pot; at V04 she refuses the saying as an excuse. (prior) | PRESERVE | Unchanged (V09) | See V09 reading section 9.1. | — | Review, not change. |
| SW-CR-0349 | SW-C-0019 | Casey Grove is the prologue’s unnamed conspirator, acting on Count Bright’s order with a 螺炎, from grievance at central neglect and gratitude to Randall; her friendship was begun instrumentally; at V03 Count Bright claims sole responsibility, Louis suspects Randall and the Empire, and Casey asks after Monica and sends her a package, so that her feeling is evidenced as concern and its history remains OPEN. (prior) | PRESERVE | Unchanged (V09) | See V09 reading section 9.1. | — | Review, not change. |
| SW-CR-0350 | SW-C-0020 | Monica derives a concept of duty from Elliott’s noblesse oblige and transposes it to her roles as treasurer and Sage; at V03 duty is joined by a personal motive she calls selfish, that the bereaved be able to mourn as she could not. (prior) | PRESERVE | Unchanged (V09) | See V09 reading section 9.1. | — | Review, not change. |
| SW-CR-0351 | SW-C-0021 | Monica’s concealment is a political bargain using Louis’s factional logic, at a cost to Cyril and her conscience; the volume presents it sympathetically and leaves its justice unjudged; at V03 Cyril still blames himself and she cannot clear him. (prior) | PRESERVE | Unchanged (V09) | See V09 reading section 9.1. | — | Review, not change. |
| SW-CR-0352 | SW-C-0022 | The cluster of details around Felix’s identity and history, held without hypothesis from V02 to V07, is explained in V08 by narration: the present Felix is the page Isaac Walker, remade by body manipulation after the real prince’s death about ten years ago; see SW-C-0063. (prior) | PRESERVE | Unchanged (V09) | See V09 reading section 9.1. | — | Review, not change. |
| SW-CR-0353 | SW-C-0023 | Monica says she cannot expect anything of anyone, while her conduct shows growing attachment; no romantic interest on her side is shown and she does not wish to marry; Felix’s absorption in the Silent Witch as an idea is now joined, in his own viewpoint, by attachment and jealousy toward Monica herself. (prior) | STRENGTHEN | Wording unchanged; support extended (V09) | V09 obs. 040, 126, 143: others’ beliefs; her own unstated. | — | Strengthened. |
| SW-CR-0354 | SW-C-0024 | Louis chose Monica for her distrust, fear and hatred of people, calls her heartless, and reads her attachment as a risk; Monica shared the warning that Monica Norton is temporary; at V08 she ends it herself by revealing her identity to her council and asking their help. (prior) | STRENGTHEN | Wording unchanged; support extended (V09) | V09 obs. 042, 182: Monica Norton ended; the friends remain. | — | Strengthened. |
| SW-CR-0355 | SW-C-0025 | Isabelle’s cover-bullying is a deliberate deterrence policy and her revenge mirrors the crime; the volume treats humiliation as justice. (prior) | PRESERVE | Unchanged (V09) | See V09 reading section 9.1. | — | Review, not change. |
| SW-CR-0356 | SW-C-0026 | 場違い organizes the social plot through three outsiders by class or region, Monica, Lana and Casey, reversing from exclusion to self-gift. (prior) | PRESERVE | Unchanged (V09) | See V09 reading section 9.1. | — | Review, not change. |
| SW-CR-0357 | SW-C-0027 | Bernie Jones is the Minerva friend; his help coexisted with a wish for her dependence; his envy ended the friendship and his curse began the hut life; he protected her cover as a noble’s duty, wanted to be her equal rival, and leaves Minerva as heir offering future help. (prior) | PRESERVE | Unchanged (V09) | See V09 reading section 9.1. | — | Review, not change. |
| SW-CR-0358 | SW-C-0028 | Mourning organizes V03: Monica’s motive in the climax is that the bereaved be able to mourn as she could not; burned books and festival bells join her strand and Felix’s. (prior) | PRESERVE | Unchanged (V09) | See V09 reading section 9.1. | — | Review, not change. |
| SW-CR-0359 | SW-C-0029 | Ike is the childhood name the real prince used for his page Isaac Walker; as Ike, the present Felix shows Monica the self outside his role; her answering self-description as a ghost was her first outreach; the persona persists in private moments, and Monica keeps its confidences from Louis. (prior) | STRENGTHEN | Wording unchanged; support extended (V09) | V09 obs. 126: she calls him Ike, a friend. | — | Strengthened. |
| SW-CR-0360 | SW-C-0030 | The duke dominated the boy by contempt and punished those the boy cared for; he took Isaac to replace the prince, cut a scar into him and calls him a tool; Isaac obeyed outwardly while gathering nobles who covet the duke’s place, and at V08 plots the duke’s death, after which the duke discards him. (prior) | REVISE | The duke dominated the boy by contempt, took Isaac to replace the prince and discarded him when he rebelled; at V09 his hold is broken by the settlement: he is silenced by Monica, expects to withdraw, and is read by Mary as a man who loves and hates the country. (V09) | V09 obs. 099, 110–112. | See V09 reading section 9.1. | Revision on new evidence. |
| SW-CR-0361 | SW-C-0031 | Imperial agents Yuan and Heidi serve the young emperor Leonhardt, who wants to avoid war by exposing the false prince at his accession; Yuan pursued Artur, his former friend who stole his body-manipulation research and served Clockford as the physician Arthur; the emperor came to Ridill himself and bargained with Monica. (prior) | PRESERVE | Unchanged (V09) | See V09 reading section 9.1. | — | Review, not change. |
| SW-CR-0362 | SW-C-0032 | Monica’s father was Venedict Rain, author of a book on heredity and magical properties, executed seven years ago, when Monica was ten, after a curse-caster he refused had him charged with necromancy on planted evidence, under a great noble’s pressure and without trial; his former assistant Hilda Everett adopted her; his friend Porter is Dustin Günther. The V04 correction stands. (prior) | PRESERVE | Unchanged (V09) | See V09 reading section 9.1. | — | Review, not change. |
| SW-CR-0363 | SW-C-0033 | Louis’s model of Monica as a heartless witch who sees people as numbers is half right: she accepts it and uses it as a technique, then fails to apply it to the people she knows; Louis says her humanity does not matter to him either way. (prior) | REVISE | Louis’s model of Monica as a heartless witch who sees people as numbers was half right; at V09 the narration names his error as assuming she would never ask others for help, and he concedes his second clean defeat by her. (V09) | V09 obs. 072, 137. | See V09 reading section 9.1. | Revision on new evidence. |
| SW-CR-0364 | SW-C-0034 | Mary deliberately allowed the theft of the ancient tool, citing the stars’ guidance, and used the crisis to test Monica; the volume does not judge the risk to the town or the bystander. (prior) | PRESERVE | Unchanged (V09) | See V09 reading section 9.1. | — | Review, not change. |
| SW-CR-0365 | SW-C-0035 | Monica’s numerical dissociation, born of abuse, became a chosen weapon and a limit, and now also a means of evidence; she remains Monica Norton knowing it deceives her friends, and her purpose widens to her father’s innocence. (prior) | PRESERVE | Unchanged (V09) | See V09 reading section 9.1. | — | Review, not change. |
| SW-CR-0366 | SW-C-0036 | V04 is organized by gifts whose meaning differs between giver and receiver: the rose, the cursed necklace, the pendant, the handkerchief and the friend’s wish. (prior) | PRESERVE | Unchanged (V09) | See V09 reading section 9.1. | — | Review, not change. |
| SW-CR-0367 | SW-C-0037 | Cyril’s history mirrors Monica’s: a violent father, withheld praise and striving for recognition; his care for her is a disguised invitation and practical help, and his attention returns to her hand. (prior) | STRENGTHEN | Wording unchanged; support extended (V09) | V09 obs. 066, 147: his sacrifice; her request. | — | Strengthened. |
| SW-CR-0368 | SW-C-0038 | The present Felix’s wish to be remembered is a wish that the dead prince’s name not be forgotten; it takes the form of a hero’s posthumous light and overrides the prince’s own last wish, that Isaac find happiness for himself; Monica perceives obsession. (prior) | REVISE | The present Felix’s wish to be remembered was a wish that the dead prince’s name not be forgotten, overriding the prince’s last wish for Isaac’s own happiness; at V09 the diary shows him that wish and the obsession ends; he speaks the prince’s wish at graduation and pursues magic as his own. (V09) | V09 obs. 121–125, 139, 169. | See V09 reading section 9.1. | Revision on new evidence. |
| SW-CR-0369 | SW-C-0039 | The traitor curse-caster was Barry Oates, serving at Leinbourg as the footman Peter Sams; he denounced Venedict Rain; before Leinbourg he served at Clockford’s house from about ten years ago, after Clockford killed the physician Arthur; he sold Rain to a patron called 閣下, and died by his own curse; 閣下 is unidentified. (prior) | REVISE | The traitor curse-caster was Barry Oates, serving at Leinbourg as the footman Peter Sams; he denounced Venedict Rain and served at Clockford’s house after Clockford killed the physician Arthur; at V09 Monica’s viewpoint narration states that Clockford was the mastermind of the Leinbourg curse dragon and tied to Sams, and the council is told Sams alone was responsible; 閣下, Sams’s word for his patron, is not used in V09. (V09) | V09 S18:E000522; obs. 094, 095. | See V09 reading section 9.1. | Revision on new evidence. |
| SW-CR-0370 | SW-C-0040 | The volume assigns Eliane moral responsibility for acts partly amplified by a curse, and lets her go unexamined in the world. (prior) | PRESERVE | Unchanged (V09) | See V09 reading section 9.1. | — | Review, not change. |
| SW-CR-0371 | SW-C-0041 | The companion argues that charms work by giving the user courage through something special; Monica, who rejected the theory, makes and keeps charms herself, and the inverse case of a curse taken for a charm shows the danger of not knowing what one holds. (prior) | STRENGTHEN | Wording unchanged; support extended (V09) | V09 obs. 039, 054, 143: charms as courage. | — | Strengthened. |
| SW-CR-0372 | SW-C-0042 | Monica’s power was visible only to a spirit and the reader while she lived as Monica Norton; acting openly as the Silent Witch, her concealment fails before Felix, whose inferences outpace her small lies. (prior) | STRENGTHEN | Wording unchanged; support extended (V09) | V09 obs. 082–099: power shown openly. | — | Strengthened. |
| SW-CR-0373 | SW-C-0043 | Cyril’s ethic of earned, patient effort is set against Louis’s maxim of money, violence and strength; Glen and Monica, who drifted into magic, take Cyril’s side. (prior) | STRENGTHEN | Wording unchanged; support extended (V09) | V09 obs. 057: Louis’s strength as effort. | — | Strengthened. |
| SW-CR-0374 | SW-C-0044 | Elliott’s creed of rank rests on an uncle’s suicide and on what he saw before he was ten; the talented commoner he once said was ruined by cunning people is Isaac Walker, by his own acknowledgement; his own friendship contradicts it, and he cannot call Isaac a fool. (prior) | STRENGTHEN | Wording unchanged; support extended (V09) | V09 obs. 027: help given in contempt. | — | Strengthened. |
| SW-CR-0375 | SW-C-0045 | Monica’s father was framed through a curse-caster’s denunciation; the narration states that Clockford had a part in his death, and Monica, Porter and Isaac conclude that the motive was his design for a tool that could expose the false prince; her purpose widens to proving his innocence, and she subordinates it to saving Isaac. (prior) | REVISE | Monica’s father was framed through Sams’s denunciation; the narration states that Clockford arranged the execution; Monica forgoes clearing his name in order to save Isaac, and uses his design at the council. (V09) | V09 S18:E000277; obs. 089, 120. | See V09 reading section 9.1. | Revision on new evidence. |
| SW-CR-0376 | SW-C-0046 | Monica’s concealment fails in three directions in one break: Bartholomeus, Felix’s inference of her school, and Felix’s knowledge of her familiar. (prior) | STRENGTHEN | Wording unchanged; support extended (V09) | V09 obs. 005: concealment ended by choice. | — | Strengthened. |
| SW-CR-0377 | SW-C-0047 | The present Felix believed his grandfather staged his heroism and meant to make him a true puppet; at V08 he suborns Emmanuel to kill the duke; the duke, having had puppet curses researched, sets a trap, kills Emmanuel and discards him. (prior) | REVISE | The present Felix believed his grandfather meant to make him a puppet, and plotted the duke’s death; at V09 he is rescued by a staged settlement, renounces the succession, and serves as Duke of Erin under the prince’s name. (V09) | V09 obs. 132, 164. | See V09 reading section 9.1. | Revision on new evidence. |
| SW-CR-0378 | SW-C-0048 | The volume is framed by Louis’s lesson that the game begins before the table, which Monica learns by losing. (prior) | STRENGTHEN | Wording unchanged; support extended (V09) | V09 obs. 104: the lesson turned back on Louis. | — | Strengthened. |
| SW-CR-0379 | SW-C-0049 | Vows made before a witness organize the volume, and the chime sounds for each. (prior) | PRESERVE | Unchanged (V09) | See V09 reading section 9.1. | — | Review, not change. |
| SW-CR-0380 | SW-C-0050 | The contract stone, the water spirit against an earth name, the eye colour and a vow ending in Arc are explained at V08: the stone and spirit were Queen Irene’s, given by the real prince to Isaac; the prince’s affinity was earth; the eye colour differs between the two boys; Arc is the prince’s middle name used as his secret name. (prior) | PRESERVE | Unchanged (V09) | See V09 reading section 9.1. | — | Review, not change. |
| SW-CR-0381 | SW-C-0051 | Monica’s anger moves from an unnamed loss of control to a recognized feeling with a cause, and Louis licenses it; the volume does not judge it. (prior) | PRESERVE | Unchanged (V09) | See V09 reading section 9.1. | — | Review, not change. |
| SW-CR-0382 | SW-C-0052 | The volume repeatedly poses whether one may ask for help; Monica is urged to in V06 and first asks, of Bartholomeus, at the opening of V07. (prior) | STRENGTHEN | Wording unchanged; support extended (V09) | V09 obs. 072: asking completed. | — | Strengthened. |
| SW-CR-0383 | SW-C-0053 | Monica infers Clockford’s connection to her father’s death; at V08 the narration states that Clockford had a part in it, and she, Porter and Isaac give the motive; 閣下 remains unidentified. Emmanuel’s patron is Clockford, SW-C-0057. (prior) | REVISE | Monica inferred Clockford’s connection to her father’s death; V08 and V09 narration state it; 閣下 is not identified by name. Emmanuel’s patron is Clockford, SW-C-0057. (V09) | V09 S18:E000277. | See V09 reading section 9.1. | Revision on new evidence. |
| SW-CR-0384 | SW-C-0054 | The Seven Sages hide a member’s crime to keep their independence from the noble assembly; the volume presents this as self-protection, not justice. (prior) | PRESERVE | Unchanged (V09) | See V09 reading section 9.1. | — | Review, not change. |
| SW-CR-0385 | SW-C-0055 | Hubert’s imitation makes chantless magic a threat in others’ eyes and a thing of little worth in Monica’s; the plate’s words are his. (prior) | PRESERVE | Unchanged (V09) | See V09 reading section 9.1. | — | Review, not change. |
| SW-CR-0386 | SW-C-0056 | Felix pairs ruthless means with a wish to be relied on, and overlays a remembered friend on Monica. (prior) | PRESERVE | Unchanged (V09) | See V09 reading section 9.1. | — | Review, not change. |
| SW-CR-0387 | SW-C-0057 | Emmanuel’s patron, called あの方 in his thoughts, is Duke Clockford; the identification rests on the same speaker’s usage in V06 and V07 and is not extended to 閣下 or the great noble. (prior) | PRESERVE | Unchanged (V09) | See V09 reading section 9.1. | — | Review, not change. |
| SW-CR-0388 | SW-C-0058 | V07’s account of Felix’s past (a sickly child, an illness and a fire, Mary’s lost star, Bridget’s belief) is explained at V08: the child was the real prince, who died by a fall; the fire burned his body and Arthur’s; the present Felix is the page Isaac Walker. (prior) | PRESERVE | Unchanged (V09) | See V09 reading section 9.1. | — | Review, not change. |
| SW-CR-0389 | SW-C-0059 | Monica asks for help and wants to know another person for the first time, each by her own decision. (prior) | STRENGTHEN | Wording unchanged; support extended (V09) | V09 obs. 120, 126: knowing and saving. | — | Strengthened. |
| SW-CR-0390 | SW-C-0060 | The volume sets uniqueness against competence and cooperation, and favours the latter. (prior) | STRENGTHEN | Wording unchanged; support extended (V09) | V09 obs. 069–072: pawns against a queen. | — | Strengthened. |
| SW-CR-0391 | SW-C-0061 | Whether humans can help spirits is argued without resolution; Monica’s rescue of Romaria is presented as her ego. (prior) | PRESERVE | Unchanged (V09) | See V09 reading section 9.1. | — | Review, not change. |
| SW-CR-0392 | SW-C-0062 | The Sages act as one in the forest and conceal from one another throughout. (prior) | STRENGTHEN | Wording unchanged; support extended (V09) | V09 obs. 049, 074: Sages split by the plan. | — | Strengthened. |
| SW-CR-0393 | SW-C-0063 | The present Felix is the page Isaac Walker, remade by body manipulation; the real prince died by a fall about ten years ago after learning of the substitution, and his body and the physician Arthur’s were burned; Ike is Isaac’s name and Arc the prince’s secret name; Yuan’s Artur is the physician Arthur; Wildianu was Queen Irene’s spirit. Not extended to 閣下. (prior) | REVISE | The present Felix is the page Isaac Walker, remade by body manipulation; the real prince died by a fall about ten years ago after learning of the substitution, by the diary and Isaac’s recollection an accident, and his body and the physician Arthur’s were burned; Ike is Isaac’s name and Arc the prince’s secret name; Yuan’s Artur is the physician Arthur; Wildianu was Queen Irene’s spirit. Not extended to 閣下. (V09) | V09 obs. 122–124. | See V09 reading section 9.1. | Revision on new evidence. |
| SW-CR-0394 | SW-C-0064 | The narration states that Clockford had a part in Venedict Rain’s death; Monica, Porter and Isaac give the motive as Rain’s hereditary tool, which could expose the false prince; 閣下 remains unidentified. (prior) | REVISE | Venedict Rain’s death: V08 narration states Clockford had a part, and V09 narration states he arranged the execution; the motive given by Monica, Porter and Isaac is the hereditary tool that could expose the false prince; 閣下 remains unidentified by name. (V09) | V09 S18:E000277. | See V09 reading section 9.1. | Revision on new evidence. |
| SW-CR-0395 | SW-C-0065 | Isaac Walker combines devotion to a dead boy’s name with ruthless means, and cannot bring himself to harm Monica. (prior) | REVISE | Isaac Walker combined devotion to a dead boy’s name with ruthless means and could not harm Monica; at V09 the obsession ends, he states to himself that he loves her, and he becomes her apprentice. (V09) | V09 obs. 125, 128, 173. | See V09 reading section 9.1. | Revision on new evidence. |
| SW-CR-0396 | SW-C-0066 | Monica is bound to the emperor: if Ridill declares war, she must serve him and end the war by presenting him the royal family’s heads. (prior) | REVISE | Monica bound herself to the emperor to avert war; at V09 he judges the promise kept, though he would have preferred Clockford’s fall, and turns to a treaty of exchange. (V09) | V09 obs. 130, 131. | See V09 reading section 9.1. | Revision on new evidence. |
| SW-CR-0397 | SW-C-0067 | Monica chooses to save Isaac over the exposure that would clear her father, and reveals herself to ask for help. (prior) | STRENGTHEN | Wording unchanged; support extended (V09) | V09 obs. 120: rescue chosen again. | — | Strengthened. |
| SW-CR-0398 | SW-C-0068 | The volume turns on remembering names: the prince’s fear, Isaac’s assumed name, the curse of the father’s name, and the Witch’s knowledge of Isaac’s. (prior) | STRENGTHEN | Wording unchanged; support extended (V09) | V09 obs. 076, 078, 166, 167: names refused, guessed, signed. | — | Strengthened. |

Revision records at EXTRA09, 2026-10-14, reviewer the EXTRA09 sequential integrator:

| Revision | Claim | Earlier formulation and boundary | Transition | New formulation and boundary | Reason | Affected homes | Kind |
|---|---|---|---|---|---|---|---|
| SW-CR-0399 | SW-C-0001 | Chantless casting began as avoidance of speech, and silence and mastery are one mechanism; the avoidance has an earlier root in childhood punishment for speaking; before Minerva a year of abuse produced a dissociation in which she lost language, ended by Hilda Everett’s rescue; its occasion at Minerva was a friend’s plan to shorten her chant; the public account explains the capacity as instant computation. (prior) | STRENGTHEN | Wording unchanged; support extended (EXTRA09) | EXTRA09 obs. 003: numbers not frightening. | — | Strengthened. |
| SW-CR-0400 | SW-C-0002 | Pain, fear or exposure drive Monica into numerical absorption; the habit began as a child’s escape from her uncle into her father’s formulas and a vow to keep his numbers; she uses it to compute combat and to bear people, it fails when people she knows are threatened, and she now turns it outward as evidence, naming it no longer a refuge. (prior) | STRENGTHEN | Wording unchanged; support extended (EXTRA09) | EXTRA09 obs. 003, 028: refuge in numbers. | — | Strengthened. |
| SW-CR-0401 | SW-C-0003 | Monica’s paternal uncle, after her father’s execution when she was ten, beat and starved her, shut her in a winter barn and forbade her to defend her father, for about a year until Hilda Everett took her; scars remain and touch still frightens her. (prior) | PRESERVE | Unchanged (EXTRA09) | See IX -extra- reading section 9.1. | — | Review, not change. |
| SW-CR-0402 | SW-C-0004 | The makeweight self-assessment is contradicted by Louis’s memory of the duel; the examiners’ ranking is unstated. (prior) | PRESERVE | Unchanged (EXTRA09) | See IX -extra- reading section 9.1. | — | Review, not change. |
| SW-CR-0403 | SW-C-0005 | Stated protection; Monica doubts it; Louis reads surveillance, uses a decoy, chose Monica because she distrusts, fears and hates people and can therefore be merciless, and calls himself first-prince because he dislikes the duke and Felix; the king is unshown. (prior) | PRESERVE | Unchanged (EXTRA09) | See IX -extra- reading section 9.1. | — | Review, not change. |
| SW-CR-0404 | SW-C-0006 | The prologue’s watcher is Felix. (prior) | PRESERVE | Unchanged (EXTRA09) | See IX -extra- reading section 9.1. | — | Review, not change. |
| SW-CR-0405 | SW-C-0007 | Public and private selves diverge: he denies a talent for magic while studying it in secret because it is forbidden to him, and hides a spirit; he obeys the duke outwardly while removing his placements and gathering nobles who resent him; he must become king without wanting it, under a ten-year vow to make the name Felix Arc Ridill remembered, which he now expresses as a hero’s posthumous light and pursues even against his dead friend’s wish. (prior) | PRESERVE | Unchanged (EXTRA09) | See IX -extra- reading section 9.1. | — | Review, not change. |
| SW-CR-0406 | SW-C-0008 | Felix did not identify Monica as the Silent Witch from V01 to V08, though he admired the Witch and grew close to Monica; at V09 he recognizes her when she enters the Supreme Council, and calls himself a fool for not seeing it. (prior) | PRESERVE | Unchanged (EXTRA09) | See IX -extra- reading section 9.1. | — | Review, not change. |
| SW-CR-0407 | SW-C-0009 | Cyril held an unverified suspicion from V01 to V08; when Monica reveals herself at V09 he says he had half guessed from her hand and the hooded figure, kneels to apologize, and returns to scolding her as his junior. (prior) | PRESERVE | Unchanged (EXTRA09) | See IX -extra- reading section 9.1. | — | Review, not change. |
| SW-CR-0408 | SW-C-0010 | Awe at Monica’s power is narrated through external focalizers; from V02 her own viewpoint also narrates her power, as calculation under constraint; V03 extends this to sustained combat computation and gives her first chantless casting from a rival’s view. (prior) | PRESERVE | Unchanged (EXTRA09) | See IX -extra- reading section 9.1. | — | Review, not change. |
| SW-CR-0409 | SW-C-0011 | The school treats rank as epistemic authority; Cyril’s inquiry is the first counterexample; at V02 rank is also used as a weapon of justice (Felix, Isabelle) and Elliott’s code ties rank to duty; at V03 Elliott’s contempt for upstarts has a biographical root and he warns that talent crossing class walls is envied or used. (prior) | PRESERVE | Unchanged (EXTRA09) | See IX -extra- reading section 9.1. | — | Review, not change. |
| SW-CR-0410 | SW-C-0012 | Organized embezzlement; erased Aaron’s and Cyril’s memories; Selma’s manipulation inferred; at V04 a traitor curse-caster reveals that Thornley worked for a patron called 閣下 through mind interference and was discarded. (prior) | PRESERVE | Unchanged (EXTRA09) | See IX -extra- reading section 9.1. | — | Review, not change. |
| SW-CR-0411 | SW-C-0013 | Nero is the Worgan black dragon, driven from the Empire’s mountains, worshipped but not commanded by the wyverns, and Monica’s familiar by his own choice after she pulled a bone from his throat; he can use black flame only in his true form. (prior) | STRENGTHEN | Wording unchanged; support extended (EXTRA09) | EXTRA09 obs. 025, 029, 030: the dragon who chose her. | — | Strengthened. |
| SW-CR-0412 | SW-C-0014 | Monica regards her talent as a curse that took her father and friend; her father, Venedict Rain, author of a book on heredity and magical properties, was executed as a heretic when Monica was ten and his book burned; the friend, Bernie Jones, needed her dependence, turned away in envy, sent her to the hut, and wanted to be her equal rival; she has renounced his approval. Correction: the V03 formulation dated the execution five years before the present, but the V03 text dates only the book’s publication. (prior) | PRESERVE | Unchanged (EXTRA09) | See IX -extra- reading section 9.1. | — | Review, not change. |
| SW-CR-0413 | SW-C-0015 | The bond with Lana rests on shared experience of being called boring and being out of place, and on mutual gestures of giving; Lana began from pride and stays from affection; at V03 Lana arms and defends her, and Monica defends Lana first. (prior) | STRENGTHEN | Wording unchanged; support extended (EXTRA09) | EXTRA09 obs. 106–108, 120, 139, 169: gifts made and kept. | — | Strengthened. |
| SW-CR-0414 | SW-C-0016 | The comedy of coercion registers harm in most cases; the non-consensual kiss is unevaluated and unknown to its recipient. (prior) | PRESERVE | Unchanged (EXTRA09) | See IX -extra- reading section 9.1. | — | Review, not change. |
| SW-CR-0415 | SW-C-0017 | Louis combines coercion with investment in her self-respect and his own pride; at V02 also gifts, an unknowing decoy, and a concession calculated to keep her cooperation; at V03 he lends Lynn and, to Casey, judges her a heartless witch. (prior) | STRENGTHEN | Wording unchanged; support extended (EXTRA09) | EXTRA09 obs. 020, 022, 023: his standing, and jam. | — | Strengthened. |
| SW-CR-0416 | SW-C-0018 | Monica’s numerical perception and comfort derive from her father’s teaching; his saying that the world is made of numbers became her means of fleeing reality under her uncle; she memorized his burning numbers and keeps his coffee pot; at V04 she refuses the saying as an excuse. (prior) | STRENGTHEN | Wording unchanged; support extended (EXTRA09) | EXTRA09 obs. 041, 175: the tape measure; watching him work. | — | Strengthened. |
| SW-CR-0417 | SW-C-0019 | Casey Grove is the prologue’s unnamed conspirator, acting on Count Bright’s order with a 螺炎, from grievance at central neglect and gratitude to Randall; her friendship was begun instrumentally; at V03 Count Bright claims sole responsibility, Louis suspects Randall and the Empire, and Casey asks after Monica and sends her a package, so that her feeling is evidenced as concern and its history remains OPEN. (prior) | PRESERVE | Unchanged (EXTRA09) | See IX -extra- reading section 9.1. | — | Review, not change. |
| SW-CR-0418 | SW-C-0020 | Monica derives a concept of duty from Elliott’s noblesse oblige and transposes it to her roles as treasurer and Sage; at V03 duty is joined by a personal motive she calls selfish, that the bereaved be able to mourn as she could not. (prior) | PRESERVE | Unchanged (EXTRA09) | See IX -extra- reading section 9.1. | — | Review, not change. |
| SW-CR-0419 | SW-C-0021 | Monica’s concealment is a political bargain using Louis’s factional logic, at a cost to Cyril and her conscience; the volume presents it sympathetically and leaves its justice unjudged; at V03 Cyril still blames himself and she cannot clear him. (prior) | PRESERVE | Unchanged (EXTRA09) | See IX -extra- reading section 9.1. | — | Review, not change. |
| SW-CR-0420 | SW-C-0022 | The cluster of details around Felix’s identity and history, held without hypothesis from V02 to V07, is explained in V08 by narration: the present Felix is the page Isaac Walker, remade by body manipulation after the real prince’s death about ten years ago; see SW-C-0063. (prior) | PRESERVE | Unchanged (EXTRA09) | See IX -extra- reading section 9.1. | — | Review, not change. |
| SW-CR-0421 | SW-C-0023 | Monica says she cannot expect anything of anyone, while her conduct shows growing attachment; no romantic interest on her side is shown and she does not wish to marry; Felix’s absorption in the Silent Witch as an idea is now joined, in his own viewpoint, by attachment and jealousy toward Monica herself. (prior) | PRESERVE | Unchanged (EXTRA09) | See IX -extra- reading section 9.1. | — | Review, not change. |
| SW-CR-0422 | SW-C-0024 | Louis chose Monica for her distrust, fear and hatred of people, calls her heartless, and reads her attachment as a risk; Monica shared the warning that Monica Norton is temporary; at V08 she ends it herself by revealing her identity to her council and asking their help. (prior) | STRENGTHEN | Wording unchanged; support extended (EXTRA09) | EXTRA09 obs. 050, 063: friends waiting; head held high. | — | Strengthened. |
| SW-CR-0423 | SW-C-0025 | Isabelle’s cover-bullying is a deliberate deterrence policy and her revenge mirrors the crime; the volume treats humiliation as justice. (prior) | STRENGTHEN | Wording unchanged; support extended (EXTRA09) | EXTRA09 obs. 066, 067: the Norton name used. | — | Strengthened. |
| SW-CR-0424 | SW-C-0026 | 場違い organizes the social plot through three outsiders by class or region, Monica, Lana and Casey, reversing from exclusion to self-gift. (prior) | PRESERVE | Unchanged (EXTRA09) | See IX -extra- reading section 9.1. | — | Review, not change. |
| SW-CR-0425 | SW-C-0027 | Bernie Jones is the Minerva friend; his help coexisted with a wish for her dependence; his envy ended the friendship and his curse began the hut life; he protected her cover as a noble’s duty, wanted to be her equal rival, and leaves Minerva as heir offering future help. (prior) | REVISE | Bernie Jones is the Minerva friend; his help coexisted with a wish for her dependence; his envy ended the friendship and his curse began the hut life, which Monica entered at fifteen wondering whether he would now forgive her; he protected her cover as a noble’s duty, wanted to be her equal rival, and leaves Minerva as heir offering future help. (EXTRA09) | EXTRA09 obs. 047–049, 115. | See IX -extra- reading section 9.1. | Revision on new evidence. |
| SW-CR-0426 | SW-C-0028 | Mourning organizes V03: Monica’s motive in the climax is that the bereaved be able to mourn as she could not; burned books and festival bells join her strand and Felix’s. (prior) | PRESERVE | Unchanged (EXTRA09) | See IX -extra- reading section 9.1. | — | Review, not change. |
| SW-CR-0427 | SW-C-0029 | Ike is the childhood name the real prince used for his page Isaac Walker; as Ike, the present Felix shows Monica the self outside his role; her answering self-description as a ghost was her first outreach; the persona persists in private moments, and Monica keeps its confidences from Louis. (prior) | PRESERVE | Unchanged (EXTRA09) | See IX -extra- reading section 9.1. | — | Review, not change. |
| SW-CR-0428 | SW-C-0030 | The duke dominated the boy by contempt, took Isaac to replace the prince and discarded him when he rebelled; at V09 his hold is broken by the settlement: he is silenced by Monica, expects to withdraw, and is read by Mary as a man who loves and hates the country. (prior) | PRESERVE | Unchanged (EXTRA09) | See IX -extra- reading section 9.1. | — | Review, not change. |
| SW-CR-0429 | SW-C-0031 | Imperial agents Yuan and Heidi serve the young emperor Leonhardt, who wants to avoid war by exposing the false prince at his accession; Yuan pursued Artur, his former friend who stole his body-manipulation research and served Clockford as the physician Arthur; the emperor came to Ridill himself and bargained with Monica. (prior) | PRESERVE | Unchanged (EXTRA09) | See IX -extra- reading section 9.1. | — | Review, not change. |
| SW-CR-0430 | SW-C-0032 | Monica’s father was Venedict Rain, author of a book on heredity and magical properties, executed seven years ago, when Monica was ten, after a curse-caster he refused had him charged with necromancy on planted evidence, under a great noble’s pressure and without trial; his former assistant Hilda Everett adopted her; his friend Porter is Dustin Günther. The V04 correction stands. (prior) | PRESERVE | Unchanged (EXTRA09) | See IX -extra- reading section 9.1. | — | Review, not change. |
| SW-CR-0431 | SW-C-0033 | Louis’s model of Monica as a heartless witch who sees people as numbers was half right; at V09 the narration names his error as assuming she would never ask others for help, and he concedes his second clean defeat by her. (prior) | STRENGTHEN | Wording unchanged; support extended (EXTRA09) | EXTRA09 obs. 019, 020, 027, 029: the early heartless witch. | — | Strengthened. |
| SW-CR-0432 | SW-C-0034 | Mary deliberately allowed the theft of the ancient tool, citing the stars’ guidance, and used the crisis to test Monica; the volume does not judge the risk to the town or the bystander. (prior) | PRESERVE | Unchanged (EXTRA09) | See IX -extra- reading section 9.1. | — | Review, not change. |
| SW-CR-0433 | SW-C-0035 | Monica’s numerical dissociation, born of abuse, became a chosen weapon and a limit, and now also a means of evidence; she remains Monica Norton knowing it deceives her friends, and her purpose widens to her father’s innocence. (prior) | STRENGTHEN | Wording unchanged; support extended (EXTRA09) | EXTRA09 obs. 028, 078: numbers as refuge and limit. | — | Strengthened. |
| SW-CR-0434 | SW-C-0036 | V04 is organized by gifts whose meaning differs between giver and receiver: the rose, the cursed necklace, the pendant, the handkerchief and the friend’s wish. (prior) | PRESERVE | Unchanged (EXTRA09) | See IX -extra- reading section 9.1. | — | Review, not change. |
| SW-CR-0435 | SW-C-0037 | Cyril’s history mirrors Monica’s: a violent father, withheld praise and striving for recognition; his care for her is a disguised invitation and practical help, and his attention returns to her hand. (prior) | STRENGTHEN | Wording unchanged; support extended (EXTRA09) | EXTRA09 obs. 085, 100, 102: mother, song, apology. | — | Strengthened. |
| SW-CR-0436 | SW-C-0038 | The present Felix’s wish to be remembered was a wish that the dead prince’s name not be forgotten, overriding the prince’s last wish for Isaac’s own happiness; at V09 the diary shows him that wish and the obsession ends; he speaks the prince’s wish at graduation and pursues magic as his own. (prior) | STRENGTHEN | Wording unchanged; support extended (EXTRA09) | EXTRA09 obs. 062: a prince changes his future. | — | Strengthened. |
| SW-CR-0437 | SW-C-0039 | The traitor curse-caster was Barry Oates, serving at Leinbourg as the footman Peter Sams; he denounced Venedict Rain and served at Clockford’s house after Clockford killed the physician Arthur; at V09 Monica’s viewpoint narration states that Clockford was the mastermind of the Leinbourg curse dragon and tied to Sams, and the council is told Sams alone was responsible; 閣下, Sams’s word for his patron, is not used in V09. (prior) | PRESERVE | Unchanged (EXTRA09) | See IX -extra- reading section 9.1. | — | Review, not change. |
| SW-CR-0438 | SW-C-0040 | The volume assigns Eliane moral responsibility for acts partly amplified by a curse, and lets her go unexamined in the world. (prior) | PRESERVE | Unchanged (EXTRA09) | See IX -extra- reading section 9.1. | — | Review, not change. |
| SW-CR-0439 | SW-C-0041 | The companion argues that charms work by giving the user courage through something special; Monica, who rejected the theory, makes and keeps charms herself, and the inverse case of a curse taken for a charm shows the danger of not knowing what one holds. (prior) | PRESERVE | Unchanged (EXTRA09) | See IX -extra- reading section 9.1. | — | Review, not change. |
| SW-CR-0440 | SW-C-0042 | Monica’s power was visible only to a spirit and the reader while she lived as Monica Norton; acting openly as the Silent Witch, her concealment fails before Felix, whose inferences outpace her small lies. (prior) | PRESERVE | Unchanged (EXTRA09) | See IX -extra- reading section 9.1. | — | Review, not change. |
| SW-CR-0441 | SW-C-0043 | Cyril’s ethic of earned, patient effort is set against Louis’s maxim of money, violence and strength; Glen and Monica, who drifted into magic, take Cyril’s side. (prior) | PRESERVE | Unchanged (EXTRA09) | See IX -extra- reading section 9.1. | — | Review, not change. |
| SW-CR-0442 | SW-C-0044 | Elliott’s creed of rank rests on an uncle’s suicide and on what he saw before he was ten; the talented commoner he once said was ruined by cunning people is Isaac Walker, by his own acknowledgement; his own friendship contradicts it, and he cannot call Isaac a fool. (prior) | STRENGTHEN | Wording unchanged; support extended (EXTRA09) | EXTRA09 obs. 126, 157, 158: rank kept; bystander no more. | — | Strengthened. |
| SW-CR-0443 | SW-C-0045 | Monica’s father was framed through Sams’s denunciation; the narration states that Clockford arranged the execution; Monica forgoes clearing his name in order to save Isaac, and uses his design at the council. (prior) | PRESERVE | Unchanged (EXTRA09) | See IX -extra- reading section 9.1. | — | Review, not change. |
| SW-CR-0444 | SW-C-0046 | Monica’s concealment fails in three directions in one break: Bartholomeus, Felix’s inference of her school, and Felix’s knowledge of her familiar. (prior) | PRESERVE | Unchanged (EXTRA09) | See IX -extra- reading section 9.1. | — | Review, not change. |
| SW-CR-0445 | SW-C-0047 | The present Felix believed his grandfather meant to make him a puppet, and plotted the duke’s death; at V09 he is rescued by a staged settlement, renounces the succession, and serves as Duke of Erin under the prince’s name. (prior) | PRESERVE | Unchanged (EXTRA09) | See IX -extra- reading section 9.1. | — | Review, not change. |
| SW-CR-0446 | SW-C-0048 | The volume is framed by Louis’s lesson that the game begins before the table, which Monica learns by losing. (prior) | PRESERVE | Unchanged (EXTRA09) | See IX -extra- reading section 9.1. | — | Review, not change. |
| SW-CR-0447 | SW-C-0049 | Vows made before a witness organize the volume, and the chime sounds for each. (prior) | PRESERVE | Unchanged (EXTRA09) | See IX -extra- reading section 9.1. | — | Review, not change. |
| SW-CR-0448 | SW-C-0050 | The contract stone, the water spirit against an earth name, the eye colour and a vow ending in Arc are explained at V08: the stone and spirit were Queen Irene’s, given by the real prince to Isaac; the prince’s affinity was earth; the eye colour differs between the two boys; Arc is the prince’s middle name used as his secret name. (prior) | PRESERVE | Unchanged (EXTRA09) | See IX -extra- reading section 9.1. | — | Review, not change. |
| SW-CR-0449 | SW-C-0051 | Monica’s anger moves from an unnamed loss of control to a recognized feeling with a cause, and Louis licenses it; the volume does not judge it. (prior) | PRESERVE | Unchanged (EXTRA09) | See IX -extra- reading section 9.1. | — | Review, not change. |
| SW-CR-0450 | SW-C-0052 | The volume repeatedly poses whether one may ask for help; Monica is urged to in V06 and first asks, of Bartholomeus, at the opening of V07. (prior) | STRENGTHEN | Wording unchanged; support extended (EXTRA09) | EXTRA09 obs. 131: a personal request. | — | Strengthened. |
| SW-CR-0451 | SW-C-0053 | Monica inferred Clockford’s connection to her father’s death; V08 and V09 narration state it; 閣下 is not identified by name. Emmanuel’s patron is Clockford, SW-C-0057. (prior) | PRESERVE | Unchanged (EXTRA09) | See IX -extra- reading section 9.1. | — | Review, not change. |
| SW-CR-0452 | SW-C-0054 | The Seven Sages hide a member’s crime to keep their independence from the noble assembly; the volume presents this as self-protection, not justice. (prior) | PRESERVE | Unchanged (EXTRA09) | See IX -extra- reading section 9.1. | — | Review, not change. |
| SW-CR-0453 | SW-C-0055 | Hubert’s imitation makes chantless magic a threat in others’ eyes and a thing of little worth in Monica’s; the plate’s words are his. (prior) | PRESERVE | Unchanged (EXTRA09) | See IX -extra- reading section 9.1. | — | Review, not change. |
| SW-CR-0454 | SW-C-0056 | Felix pairs ruthless means with a wish to be relied on, and overlays a remembered friend on Monica. (prior) | STRENGTHEN | Wording unchanged; support extended (EXTRA09) | EXTRA09 obs. 073, 134: caution and secret tastes. | — | Strengthened. |
| SW-CR-0455 | SW-C-0057 | Emmanuel’s patron, called あの方 in his thoughts, is Duke Clockford; the identification rests on the same speaker’s usage in V06 and V07 and is not extended to 閣下 or the great noble. (prior) | PRESERVE | Unchanged (EXTRA09) | See IX -extra- reading section 9.1. | — | Review, not change. |
| SW-CR-0456 | SW-C-0058 | V07’s account of Felix’s past (a sickly child, an illness and a fire, Mary’s lost star, Bridget’s belief) is explained at V08: the child was the real prince, who died by a fall; the fire burned his body and Arthur’s; the present Felix is the page Isaac Walker. (prior) | PRESERVE | Unchanged (EXTRA09) | See IX -extra- reading section 9.1. | — | Review, not change. |
| SW-CR-0457 | SW-C-0059 | Monica asks for help and wants to know another person for the first time, each by her own decision. (prior) | STRENGTHEN | Wording unchanged; support extended (EXTRA09) | EXTRA09 obs. 131: asking before the council. | — | Strengthened. |
| SW-CR-0458 | SW-C-0060 | The volume sets uniqueness against competence and cooperation, and favours the latter. (prior) | PRESERVE | Unchanged (EXTRA09) | See IX -extra- reading section 9.1. | — | Review, not change. |
| SW-CR-0459 | SW-C-0061 | Whether humans can help spirits is argued without resolution; Monica’s rescue of Romaria is presented as her ego. (prior) | PRESERVE | Unchanged (EXTRA09) | See IX -extra- reading section 9.1. | — | Review, not change. |
| SW-CR-0460 | SW-C-0062 | The Sages act as one in the forest and conceal from one another throughout. (prior) | PRESERVE | Unchanged (EXTRA09) | See IX -extra- reading section 9.1. | — | Review, not change. |
| SW-CR-0461 | SW-C-0063 | The present Felix is the page Isaac Walker, remade by body manipulation; the real prince died by a fall about ten years ago after learning of the substitution, by the diary and Isaac’s recollection an accident, and his body and the physician Arthur’s were burned; Ike is Isaac’s name and Arc the prince’s secret name; Yuan’s Artur is the physician Arthur; Wildianu was Queen Irene’s spirit. Not extended to 閣下. (prior) | STRENGTHEN | Wording unchanged; support extended (EXTRA09) | EXTRA09 obs. 134: things Felix must not possess. | — | Strengthened. |
| SW-CR-0462 | SW-C-0064 | Venedict Rain’s death: V08 narration states Clockford had a part, and V09 narration states he arranged the execution; the motive given by Monica, Porter and Isaac is the hereditary tool that could expose the false prince; 閣下 remains unidentified by name. (prior) | PRESERVE | Unchanged (EXTRA09) | See IX -extra- reading section 9.1. | — | Review, not change. |
| SW-CR-0463 | SW-C-0065 | Isaac Walker combined devotion to a dead boy’s name with ruthless means and could not harm Monica; at V09 the obsession ends, he states to himself that he loves her, and he becomes her apprentice. (prior) | PRESERVE | Unchanged (EXTRA09) | See IX -extra- reading section 9.1. | — | Review, not change. |
| SW-CR-0464 | SW-C-0066 | Monica bound herself to the emperor to avert war; at V09 he judges the promise kept, though he would have preferred Clockford’s fall, and turns to a treaty of exchange. (prior) | PRESERVE | Unchanged (EXTRA09) | See IX -extra- reading section 9.1. | — | Review, not change. |
| SW-CR-0465 | SW-C-0067 | Monica chooses to save Isaac over the exposure that would clear her father, and reveals herself to ask for help. (prior) | PRESERVE | Unchanged (EXTRA09) | See IX -extra- reading section 9.1. | — | Review, not change. |
| SW-CR-0466 | SW-C-0068 | The volume turns on remembering names: the prince’s fear, Isaac’s assumed name, the curse of the father’s name, and the Witch’s knowledge of Isaac’s. (prior) | STRENGTHEN | Wording unchanged; support extended (EXTRA09) | EXTRA09 obs. 164, 165, 174, 177: names as relationship. | — | Strengthened. |
| SW-CR-0467 | SW-C-0069 | The Supreme Council’s verdict is a staged truth: a real tool with borrowed blood, a dead culprit, a performed cure and royal ratification, with Clockford held by Monica’s silence. (prior) | PRESERVE | Unchanged (EXTRA09) | See IX -extra- reading section 9.1. | — | Review, not change. |
| SW-CR-0468 | SW-C-0070 | The real prince’s death was an accident, by the diary’s last entry and Isaac’s recollection; his last wish was Isaac’s own life and a reunion. (prior) | PRESERVE | Unchanged (EXTRA09) | See IX -extra- reading section 9.1. | — | Review, not change. |
| SW-CR-0469 | SW-C-0071 | Mary reads Clockford’s substitution as revenge on the crown, rooted in his father’s killing and his love and hatred of the country; he neither denies nor confirms it. (prior) | REVISE | Mary reads Clockford’s substitution as revenge on the crown, rooted in his father’s killing and his love and hatred of the country; he neither denies nor confirms it. Her first prophecy foretold that father’s death, and she resolves to mourn Clockford when he dies alone (SW-C-0077). (EXTRA09) | EXTRA09 obs. 151–154; V08 obs. 294. | See IX -extra- reading section 9.1. | Revision on new evidence. |
| SW-CR-0470 | SW-C-0072 | Monica’s rescue is collective: every element is supplied by people she asked, and the narration names Louis’s error as assuming she would not ask. (prior) | STRENGTHEN | Wording unchanged; support extended (EXTRA09) | EXTRA09 obs. 158: Elliott chose to help. | — | Strengthened. |
| SW-CR-0471 | SW-C-0073 | After the rescue Isaac’s obsession ends; his love for Monica is stated in his viewpoint; he becomes her apprentice, while she regards him as a friend. (prior) | STRENGTHEN | Wording unchanged; support extended (EXTRA09) | EXTRA09 obs. 173, 177: the apprentice in an apron. | — | Strengthened. |
| SW-CR-0472 | SW-C-0074 | The volume closes the first arc on silence broken and imposed, and on Monica drinking coffee among friends. (prior) | STRENGTHEN | Wording unchanged; support extended (EXTRA09) | EXTRA09 obs. 169–171, 178: thanks given. | — | Strengthened. |

## 6. Prospective questions and predictions — SW-P

Owns genuine prospective tests and open questions across source-unit boundaries.

Fields: ID; frozen wording; preparation boundary/reference; basis observations/claims; target opportunity; expected outcome if any; falsifying/weakening outcome; confidence basis; test status; eligible adjudicating observations; result/revision route.

Statuses: OPEN, TESTED_SUPPORTED, TESTED_COMPLICATED, TESTED_DISCONFIRMED, UNTESTED, or RETIRED_WITH_REASON. An open question needs no predicted answer. An absent opportunity is UNTESTED; a remembered later event is never a newly frozen prediction.

Records at V01. All were frozen at V01 closure on 2026-10-14 in the reading’s section 9.2. None carries a predicted answer: the entry freeze registered no predictions because of disclosed prior franchise exposure, and the same reason applies at exit.

| ID | Frozen wording | Basis | Target opportunity | Expected outcome | Weakening outcome | Status |
|---|---|---|---|---|---|---|
| SW-P-0001 | Who is the disciple Louis planted in the academy, and does Monica learn of it? | obs. 116 | A Louis-connected student or disclosure. | None. | — | RETIRED_WITH_REASON at V04: answered, Glen Dudley (V04 obs. 065). |
| SW-P-0002 | What is Felix’s wish, why is his life a remainder, and where does he go at night? | obs. 078, 079 | Felix viewpoint scenes. | None. | — | RETIRED_WITH_REASON at V08: answered, to keep the dead prince’s name in history; the remainder is Isaac Walker’s leftover life; the nights were outings (V08 obs. 166, 170). |
| SW-P-0003 | Will Felix connect Monica with the Silent Witch, and what would force it? | obs. 069, 122 | Felix witnessing or hearing of her magic. | None registered; see the bounded expectation in the reading’s section 10, which is not a prediction. | — | RETIRED_WITH_REASON at V09: he recognizes her at the council (V09 obs. 080, 081). |
| SW-P-0004 | Will Cyril verify his suspicion about her hand? | obs. 111 | Repeat of the glove scene; confrontation. | None. | — | RETIRED_WITH_REASON at V08: answered by Monica’s reveal before the council with Cyril present (V08 obs. 291). |
| SW-P-0005 | Who was the man in the dream; what happened to her father; how did talent take him? | obs. 037, 090 | Backstory disclosure. | None. | — | RETIRED_WITH_REASON at V04: answered through V02–V04 (V04 obs. 001–008). |
| SW-P-0006 | Who is the Minerva friend; does he return? | obs. 090 | A Minerva acquaintance appears. | None. | — | RETIRED_WITH_REASON at V03: answered, Bernie Jones (V03 obs. 001–009). |
| SW-P-0007 | What does the king intend, and what grounds the duke’s hold on Felix? | obs. 062, 119 | King or duke on stage. | None. | — | RETIRED_WITH_REASON at V09: the king knew and used Louis; the duke’s hold broken (V09 obs. 106, 112). |
| SW-P-0008 | What is Nero? | obs. 102 | Disclosure of origin or powers. | None. | — | RETIRED_WITH_REASON at V05: answered, the Worgan black dragon (V05 obs. 106). |
| SW-P-0009 | Does Monica’s use of mind interference have consequences? | obs. 110 | Guild or Sage reaction. | None. | — | OPEN; UNTESTED at V02 |
| SW-P-0010 | What role does the Jewel Mage play? | obs. 100 | Further appearance. | None. | — | RETIRED_WITH_REASON at V08: suborned by Felix, killed by Clockford’s trap, blamed by a forged note (V08 obs. 094, 191, 209). |
| SW-P-0011 | Do Elliott and Bridget accept Monica; how does Elliott’s contempt meet her concealed rank? | obs. 061, 070 | Council scenes. | None. | — | RETIRED_WITH_REASON at V09: both join the rescue (V09 obs. 025). |
| SW-P-0012 | Do Monica’s speech gains persist and generalize to strangers? | obs. 112, 114 | Ordinary scenes with strangers. | None. | — | RETIRED_WITH_REASON at V09: she speaks before the council and asks openly (V09 obs. 082–099). |

Status notes and records at V02. None carries a predicted answer, for the same exposure reason. V01’s bounded expectation is discussed in the V02 reading’s section 9.3 and not scored.

| ID | Frozen wording or V02 note | Basis | Target opportunity | Expected outcome | Weakening outcome | Status |
|---|---|---|---|---|---|---|
| SW-P-0001 | V02: decoy role and traits disclosed; Glen fits; unnamed; Monica unaware. | V02 obs. 010, 015, 040, 041 | Naming or Monica learning. | None. | — | OPEN |
| SW-P-0002 | V02: must become king without desire; nights not mentioned. | V02 obs. 077 | — | None. | — | OPEN |
| SW-P-0003 | V02: Felix searches for the Witch on campus. | V02 obs. 087 | — | None. | — | OPEN |
| SW-P-0005 | V02: uncle and father’s execution disclosed; research, place, date and passage to the guardian remain. | V02 obs. 034, 044, 045 | — | None. | — | OPEN |
| SW-P-0011 | V02: Elliott shamed and protective but still calls her presumptuous; Bridget unconvinced. | V02 obs. 021, 024, 039, 063 | — | None. | — | OPEN |
| SW-P-0012 | V02: refusals, accusation and bargaining; still fails at a simple request. | V02 obs. 023, 043, 072, 095 | — | None. | — | OPEN |
| SW-P-0013 | What does MacLaggan know about Monica and Glen? | V02 obs. 016, 089 | His conduct toward either. | None. | — | RETIRED_WITH_REASON at V06: answered, he knows she is the Silent Witch and keeps silent (V06 obs. 174). |
| SW-P-0014 | What will Felix’s search for the Silent Witch lead him to do? | V02 obs. 087 | Felix scenes. | None. | — | RETIRED_WITH_REASON at V09: he finds the Witch and becomes her apprentice (V09 obs. 081, 173). |
| SW-P-0015 | What is the tournament Boyd intends for Monica? | V02 obs. 089 | Chess scenes. | None. | — | RETIRED_WITH_REASON at V03: held (V03 obs. 037–050). |
| SW-P-0016 | What explains the cluster around Felix in SW-C-0022? | V02 obs. 039, 049, 062, 093 | Any disclosure about his childhood. | None. | — | RETIRED_WITH_REASON at V08: explained, SW-C-0063. |
| SW-P-0017 | What was her father’s forbidden research, and does it relate to the Empire’s legalization of body magic? | V02 obs. 034, 035, 044 | Backstory. | None. | — | RETIRED_WITH_REASON at V08: a tool reading hereditary information from mana in blood; no Empire link stated (V08 obs. 077, 266). |
| SW-P-0018 | What event does Mary Harvey foresee? | V02 obs. 093 | — | None. | — | OPEN |
| SW-P-0019 | Do Casey’s confession, Count Bright and the Randall connection have consequences? | V02 obs. 080, 081, 096 | Political scenes. | None. | — | OPEN |
| SW-P-0020 | What does Claudia know or suspect beyond her jealousy? | V02 obs. 050, 118 | Claudia scenes. | None. | — | OPEN |

Status notes and records at V03. None carries a predicted answer, for the same exposure reason.

| ID | Frozen wording or V03 note | Basis | Target opportunity | Expected outcome | Weakening outcome | Status |
|---|---|---|---|---|---|---|
| SW-P-0001 | V03: no new evidence. | — | — | None. | — | OPEN |
| SW-P-0002 | V03: the ten-year vow; the remainder is time outside the role before kingship; nights shown. | V03 obs. 065, 082, 101 | Why the vow. | None. | — | OPEN; partly answered |
| SW-P-0003 | V03: he suspected her as an assassin instead; Yuan hunts both secrets. | V03 obs. 104, 118, 125 | — | None. | — | OPEN |
| SW-P-0004 | V03: no Cyril viewpoint on either link. | — | — | None. | — | UNTESTED |
| SW-P-0005 | V03: father named; book identified; adoptive mother mentioned; scars. | V03 obs. 023, 105, 121, 133 | Passage from uncle to guardian. | None. | — | OPEN; narrowed |
| SW-P-0007 | V03: the duke on stage; contempt; the dream’s punishment by proxy. | V03 obs. 061, 113 | Ground of the hold; the king. | None. | — | OPEN; narrowed |
| SW-P-0008 | V03: no disclosure. | — | — | None. | — | UNTESTED |
| SW-P-0009 | V03: used again on the tool; tolerated in emergency per Lynn. | V03 obs. 099 | Institutional reaction. | None. | — | OPEN |
| SW-P-0010 | V03: named Emmanuel Darwin; a brooch resembling Cyril’s bears his name. | V03 obs. 068, 085 | His appearance. | None. | — | OPEN; narrowed |
| SW-P-0011 | V03: Elliott’s warning and memory; Bridget probes. | V03 obs. 017, 022, 038 | — | None. | — | OPEN |
| SW-P-0012 | V03: sustained declarations to Bernie, the tool and Felix. | V03 obs. 045, 097, 100 | — | None. | — | OPEN |
| SW-P-0013 | V03: emphasized remark on her other talents. | V03 obs. 047 | His conduct. | None. | — | OPEN; strong evidence he knows |
| SW-P-0014 | V03: reads her papers; plans to meet her as king. | V03 obs. 103, 104 | — | None. | — | OPEN |
| SW-P-0016 | V03: cluster extended. | V03 obs. 018–020, 065, 070, 109, 112–114, 121 | Any disclosure. | None. | — | OPEN; no hypothesis |
| SW-P-0017 | V03: heredity and magical properties; no Empire link stated. | V03 obs. 105 | — | None. | — | OPEN |
| SW-P-0018 | V03: the festival night as the country’s turning point. | V03 obs. 093 | — | None. | — | OPEN |
| SW-P-0019 | V03: Louis’s alliance hypothesis; Casey’s package. | V03 obs. 128, 131 | — | None. | — | OPEN |
| SW-P-0020 | V03: political reading of the duke. | V03 obs. 059 | — | None. | — | OPEN |
| SW-P-0021 | What is in Casey’s package, and does it reach Monica? | V03 obs. 131 | Louis meeting Monica. | None. | — | RETIRED_WITH_REASON at V04: a handkerchief (V04 obs. 097). |
| SW-P-0022 | Whose is the star of loss beside Monica’s? | V03 obs. 115 | Mary scenes. | None. | — | OPEN |
| SW-P-0023 | What will Yuan and Heidi do at the festival with a forged uniform? | V03 obs. 124, 125 | The festival. | None. | — | RETIRED_WITH_REASON at V04: answered (V04 obs. 083–094). |
| SW-P-0024 | Why did Mary let the tool be stolen, and what does she expect of Monica? | V03 obs. 093, 116 | Mary’s account. | None. | — | OPEN |
| SW-P-0025 | What will Bernie do with his knowledge of her mission? | V03 obs. 054, 056 | Minerva scenes. | None. | — | RETIRED_WITH_REASON at V04: leaves Minerva, offers help (V04 obs. 036–038). |
| SW-P-0026 | Does Porter know who Monica is? | V03 obs. 106 | Porter scenes. | None. | — | RETIRED_WITH_REASON at V08: he knew her as Rain’s daughter and learns she is the Witch (V08 obs. 074, 084). |

Status notes and records at V04. None carries a predicted answer.

| ID | Frozen wording or V04 note | Basis | Target opportunity | Expected outcome | Weakening outcome | Status |
|---|---|---|---|---|---|---|
| SW-P-0002 | V04: to be remembered like a star-hero, overriding his friend’s wish. | V04 obs. 116, 117 | — | None. | — | OPEN; narrowed |
| SW-P-0004 | V04: his attention returns to her hand and the ice. | V04 obs. 108 | — | None. | — | OPEN |
| SW-P-0007 | V04: Louis wonders what the king suspected. | V04 obs. 120 | — | None. | — | OPEN |
| SW-P-0008 | V04: reptilian traits; drug-immune. | V04 obs. 092 | — | None. | — | OPEN; narrowed |
| SW-P-0011 | V04: Elliott’s truce with Cyril; Bridget hostile. | V04 obs. 072, 118 | — | None. | — | OPEN |
| SW-P-0012 | V04: initiative toward a stranger. | V04 obs. 073 | — | None. | — | OPEN |
| SW-P-0013 | V04: very probably knows. | V04 obs. 069 | — | None. | — | OPEN |
| SW-P-0016 | V04: extended. | V04 obs. 027, 091, 113, 118, 120 | — | None. | — | OPEN; no hypothesis |
| SW-P-0019 | V04: war threatened by Yuan. | V04 obs. 094 | — | None. | — | OPEN |
| SW-P-0027 | What trace did Yuan confirm on Felix; who is Arthur; who is Yuan’s master? | V04 obs. 091 | — | None. | — | RETIRED_WITH_REASON at V08: Artur’s body manipulation; Artur is the physician Arthur; the master is the emperor Leonhardt (V08 obs. 037, 044, 054). |
| SW-P-0028 | What is Louis’s hypothesis, and what will he do with it? | V04 obs. 120 | — | None. | — | RETIRED_WITH_REASON at V08: the prince is false; he means to denounce Clockford at the garden party (V08 obs. 185, 187). |
| SW-P-0029 | Who is the traitor curse-caster, who is 閣下, and what is the puppet curse? | V04 obs. 122, 123 | — | None. | — | OPEN |
| SW-P-0030 | What does Bridget want of “her prince”, and what does she know of Monica? | V04 obs. 027, 118 | — | None. | — | RETIRED_WITH_REASON at V07: answered, to find the Felix she knew (V07 obs. 176–178). |
| SW-P-0031 | What will Cyril conclude from the ice and the hand? | V04 obs. 108 | — | None. | — | RETIRED_WITH_REASON at V08: superseded by Monica’s reveal (V08 obs. 291). |
| SW-P-0032 | Why has Bartholomeus entered Leinbourg service? | V04 obs. 121 | — | None. | — | RETIRED_WITH_REASON at V05: answered, a handyman saving to find “the Witch”, now hired by Monica (V05 obs. 035, 150). |

Status notes and records at AFTER04. None carries a predicted answer.

| ID | Frozen wording or AFTER04 note | Basis | Target opportunity | Expected outcome | Weakening outcome | Status |
|---|---|---|---|---|---|---|
| SW-P-0007 | AFTER04: the grandfather checks the prince’s reading. | AFTER04 obs. 035 | — | None. | — | OPEN |
| SW-P-0011 | AFTER04: Elliott infers that Bridget’s love crosses a wall of rank. | AFTER04 obs. 121 | — | None. | — | OPEN |
| SW-P-0012 | AFTER04: plain requests and thanks. | AFTER04 obs. 147, 160 | — | None. | — | OPEN |
| SW-P-0013 | AFTER04: his unfinished question about Glen and Minerva. | AFTER04 obs. 094 | — | None. | — | OPEN |
| SW-P-0014 | AFTER04: he reads her paper and a book about her. | AFTER04 obs. 034, 144 | — | None. | — | OPEN |
| SW-P-0016 | AFTER04: the childhood interlude added. | AFTER04 obs. 122, 123 | — | None. | — | OPEN |
| SW-P-0020 | AFTER04: her contempt for Felix. | AFTER04 obs. 055 | — | None. | — | OPEN |
| SW-P-0030 | AFTER04: Elliott’s and Benjamin’s inferences about Bridget. | AFTER04 obs. 121 | — | None. | — | OPEN |
| SW-P-0033 | What links Glen to Minerva, and why does MacLaggan ask whether he can be left alone? | AFTER04 obs. 094 | — | None. | — | OPEN |
| SW-P-0034 | What happened to Elliott before he was ten? | AFTER04 obs. 112 | — | None. | — | OPEN |
| SW-P-0035 | When did the Heims-Naria job take place? | AFTER04 obs. 001, 133 | — | None. | — | OPEN |
| SW-P-0036 | Whom did Felix mean by his complaint, and how did he know Monica’s birthday? | AFTER04 obs. 064, 149 | — | None. | — | OPEN |

Every other open question was reviewed at AFTER04 without new evidence.

Status notes and records at V05. None carries a predicted answer.

| ID | Frozen wording or V05 note | Basis | Target opportunity | Expected outcome | Weakening outcome | Status |
|---|---|---|---|---|---|---|
| SW-P-0003 | V05: Felix knows the Witch is at Serendia. | V05 obs. 129, 160 | — | None. | — | OPEN; narrowed |
| SW-P-0014 | V05: his search is active. | V05 obs. 160 | — | None. | — | OPEN |
| SW-P-0029 | V05: traitor identified and dead; puppet curse described; 閣下 open. | V05 obs. 140, 148 | — | None. | — | OPEN; narrowed |
| SW-P-0033 | V05: a past mana runaway; Louis took him in. | V05 obs. 115 | — | None. | — | OPEN; narrowed |
| SW-P-0037 | What is “the truth of the black chalice”, and what does Porter know? | V05 obs. 172, 173 | — | None. | — | RETIRED_WITH_REASON at V08: Rain’s hereditary tool, named after Porter’s novel (V08 obs. 076–079). |
| SW-P-0038 | Who is the great noble behind Venedict’s execution, and is it 閣下? | V05 obs. 166, 167 | — | None. | — | RETIRED_WITH_REASON at V09: the narration states Clockford arranged the execution (V09 S18:E000277); 閣下 tracked at SW-P-0029. |
| SW-P-0039 | Why does Felix hold a water spirit against an earth name? | V05 obs. 131 | — | None. | — | RETIRED_WITH_REASON at V08: Irene’s spirit, given by the prince to Isaac, who contracted it (V08 obs. 141, 160–165). |
| SW-P-0040 | What will Hubert Dee’s transfer bring? | V05 obs. 181 | — | None. | — | RETIRED_WITH_REASON at V06: answered, he discovered her, forced a duel, lost, and was warned off (V06 obs. 133, 160, 174, 175). |

Every other open question was reviewed at V05; statuses are in the V05 reading section 9.3.

Status notes and records at V06. None carries a predicted answer.

| ID | Frozen wording or V06 note | Basis | Target opportunity | Expected outcome | Weakening outcome | Status |
|---|---|---|---|---|---|---|
| SW-P-0004 | V06: he heard the title in the fog. | V06 obs. 152 | — | None. | — | OPEN; narrowed |
| SW-P-0010 | V06: fraud, spirit power, the whistle, a patron. | V06 obs. 194, 196, 211 | — | None. | — | OPEN; narrowed |
| SW-P-0029 | V06: the failed control curse; Sams worked for Clockford. | V06 obs. 021, 204 | — | None. | — | OPEN; narrowed |
| SW-P-0033 | V06: the night battle and runaway; the result withheld. | V06 obs. 088–090 | — | None. | — | OPEN; narrowed |
| SW-P-0041 | Who is the patron who wants war, and what is the whistle’s own ambition? | V06 obs. 211, 212 | — | None. | — | RETIRED_WITH_REASON at V07: the patron is Clockford by Emmanuel’s usage; the whistle seeks war and the making of kings (V07 S15:E000458; obs. 106). |
| SW-P-0042 | What is Emmanuel’s secret weapon, and how does the affair at Kellylinden end, Lynn included? | V06 obs. 209; S28:E000034 | — | None. | — | RETIRED_WITH_REASON at V07: the reflection mirror; the whistle destroyed, Lynn freed, the affair closed (V07 obs. 085, 110, 141). |
| SW-P-0043 | Will the noble assembly bring the Sages under it, and is that what Mary’s darkening star foretells? | V06 obs. 050, 051, 187 | — | None. | — | OPEN |
| SW-P-0044 | Why did Felix ask Ray whether a living thing can be controlled by curse? | V06 obs. 023 | — | None. | — | OPEN |

Every other open question was reviewed at V06; statuses are in the V06 reading section 9.3.

Status notes and records at V07. None carries a predicted answer.

| ID | Frozen wording or V07 note | Basis | Target opportunity | Expected outcome | Weakening outcome | Status |
|---|---|---|---|---|---|---|
| SW-P-0004 | V07: he knows the Witch’s hand is cursed. | V07 obs. 061, 062 | — | None. | — | OPEN; narrowed |
| SW-P-0016 | V07: extended by the account of Felix’s past. | V07 reading section 6.8 | — | None. | — | OPEN; no hypothesis |
| SW-P-0022 | V07: Mary names a holder of the star of loss near the Witch. | V07 obs. 145 | — | None. | — | OPEN; narrowed |
| SW-P-0027 | V07: Dr Arthur died in the fire; Yuan’s master on stage, unnamed. | V07 obs. 202, 213, 221 | — | None. | — | OPEN; narrowed |
| SW-P-0039 | V07: a card says Wildianu was Queen Irene’s spirit; paratext only. | V07 reading section 7.5 | — | None. | — | OPEN |
| SW-P-0045 | What does Felix intend with Emmanuel? | V07 obs. 150 | — | None. | — | RETIRED_WITH_REASON at V08: to have him kill Clockford (V08 obs. 090). |
| SW-P-0046 | What happened in the fire at Clockford’s house about ten years ago? | V07 obs. 202, 205 | — | None. | — | RETIRED_WITH_REASON at V08: the prince’s and Arthur’s bodies burned to fake Isaac’s death (V08 obs. 155–157). |
| SW-P-0047 | Who is Yuan’s master, and what will his coming bring? | V07 obs. 221, 223 | — | None. | — | RETIRED_WITH_REASON at V08: the emperor Leonhardt; the bargain (V08 obs. 054, 064). |
| SW-P-0048 | What will Monica’s notice to Yuan bring? | V07 obs. 219 | — | None. | — | RETIRED_WITH_REASON at V08: the meeting it brought (V08 obs. 019, 035). |

Every other open question was reviewed at V07; statuses are in the V07 reading section 9.3.

Status notes and records at V08. None carries a predicted answer.

| ID | Frozen wording or V08 note | Basis | Target opportunity | Expected outcome | Weakening outcome | Status |
|---|---|---|---|---|---|---|
| SW-P-0003 | V08: he learns Monica is Rain’s daughter and that the Witch knows his name. | V08 obs. 199, 261 | — | None. | — | OPEN; narrowed |
| SW-P-0007 | V08: Louis infers the king suspected a false prince. | V08 obs. 185 | — | None. | — | OPEN; narrowed |
| SW-P-0019 | V08: Count Bright named as a channel through Randall. | V08 obs. 046 | — | None. | — | OPEN; narrowed |
| SW-P-0029 | V08: Clockford had control curses researched; 閣下 open. | V08 obs. 206 | — | None. | — | OPEN; narrowed |
| SW-P-0034 | V08: he recognized the page in the new prince. | V08 obs. 219–223 | — | None. | — | OPEN; narrowed |
| SW-P-0038 | V08: the narration states Hilda hid Clockford’s part; 閣下 open. | V08 obs. 265 | — | None. | — | OPEN; narrowed |
| SW-P-0044 | V08: Clockford had control curses researched; Felix’s reason not stated. | V08 obs. 206 | — | None. | — | OPEN; narrowed |
| SW-P-0049 | What will the Supreme Council decide, and can the chalice be built in time? | V08 obs. 254, 269 | — | None. | — | RETIRED_WITH_REASON at V09: built in time; the verdict (V09 obs. 091, 098). |
| SW-P-0050 | What is the diary’s last sentence, and what has Isaac misunderstood? | V08 obs. 246, 247 | — | None. | — | RETIRED_WITH_REASON at V09: the prince’s wish to meet Ike again; the death an accident (V09 obs. 122, 123). |
| SW-P-0051 | What does Monica ask of Mary, and what does she fetch from the castle? | V08 obs. 255, 273 | — | None. | — | RETIRED_WITH_REASON at V09: a meeting with the king (V09 obs. 113); the errand not separately stated. |
| SW-P-0052 | Will Monica’s bargain with the emperor and Louis’s plan for the garden party collide? | V08 obs. 064, 187 | — | None. | — | RETIRED_WITH_REASON at V09: Louis held off; the emperor judges the promise kept (V09 obs. 048, 130). |

Every other open question was reviewed at V08; statuses are in the V08 reading section 9.3.

Status notes and records at V09. None carries a predicted answer.

| ID | Frozen wording or V09 note | Basis | Target opportunity | Expected outcome | Weakening outcome | Status |
|---|---|---|---|---|---|---|
| SW-P-0029 | V09: Clockford behind Sams’s dragon by narration; the word 閣下 not used. | V09 S18:E000522 | — | None. | — | OPEN; narrowed |
| SW-P-0053 | Who will fill the seventh Sage’s seat? | V09 obs. 135, 156 | — | None. | — | OPEN |
| SW-P-0054 | What will the emperor’s treaty and Raul’s incognito study bring? | V09 obs. 131, 178 | — | None. | — | OPEN |
| SW-P-0055 | Will Clockford keep his silence? | V09 obs. 099, 112 | — | None. | — | OPEN |
| SW-P-0056 | What will Isaac’s apprenticeship bring? | V09 obs. 173, 181 | — | None. | — | OPEN |

Every other open question was reviewed at V09; statuses are in the V09 reading section 9.3.

Status notes and records at EXTRA09. None carries a predicted answer.

| ID | Frozen wording or EXTRA09 note | Basis | Target opportunity | Expected outcome | Weakening outcome | Status |
|---|---|---|---|---|---|---|
| SW-P-0024 | EXTRA09: Mary’s lifelong relation to Clockford added; her reason not stated. | EXTRA09 obs. 151–154 | — | None. | — | OPEN |
| SW-P-0029 | EXTRA09: a design card gives Clockford a personal name; 閣下 not used; paratext only. | EXTRA09 S32 | — | None. | — | OPEN; narrowed |
| SW-P-0056 | EXTRA09: a week a month in Southerndoor; cooking. | EXTRA09 obs. 173 | — | None. | — | OPEN |
| SW-P-0057 | What will the plan to relax the regulation of medical magical tools bring, and who is Hilda’s collaborator? | EXTRA09 obs. 007, 008 | — | None. | — | OPEN |
| SW-P-0058 | What occasion does Lynn’s remembered heartbeat refer to? | EXTRA09 obs. 096, 097 | — | None. | — | OPEN |

Every other open question was reviewed at EXTRA09; statuses are in the IX -extra- reading section 9.3.

## 7. Literary form, motifs and evaluation — SW-F

Owns recurring prose/form and ethical-framing patterns that warrant cumulative retrieval.

Fields: feature/domain; textual/formal mechanism; focalization/withholding/reader alignment; Japanese wording/register evidence; recurrence and changed function; affected-person access; evaluative criterion; consequences/tone; strongest rival interpretation; one-off versus promoted reason; linked claims/observations.

A scene's comic tone is distinct from its represented act and normative assessment. Avoid compulsory ethical scoring of every passage. Isolated details without cumulative significance remain in their volume reading.

Records at V01:

| ID | Feature | Mechanism | Focalization and withholding | Wording evidence | Function and recurrence | Rival reading | Promotion reason | Obs. |
|---|---|---|---|---|---|---|---|---|
| SW-F-0001 | External focalization of power | Monica’s full power is shown through Isabelle, Cyril, Thornley and Louis; her own view narrates fear and small uses. | Reader sees awe others feel and fear she feels. | Repeated “monster” in four viewpoints. | Prologue, chapters 9 and 10, secret episode. | The staircase gives narrator praise in her view, but for a pratfall. | Governs how later power scenes should be read. | 002, 098, 106, 117 |
| SW-F-0002 | Typographic silence | Withheld words printed as dots or dashes. | Erasure shown as erasure. | Cyril’s blanked destination; elided object of his wish; elided dream content. | Chapters 8, 9, 10. | Ordinary ellipsis. | Recurs; links to the title’s silence. | 081, 096, 107 |
| SW-F-0003 | Narrator’s deadpan correction | One-line paragraphs that correct a character’s inference or name an abuse. | Keeps reader outside every character. | “The impressive one was Isabelle”; “abuse”; “human rights”. | Throughout. | Pure joke delivery. | Main evaluative voice of the series so far. | 010, 025, 092 |
| SW-F-0004 | Romance-novel intertext | Characters borrow plots, roles and nicknames from a popular novelist. | Genre self-awareness inside the story. | Cover story; villainess; “ice prince”; alias. | Chapters 1, 3, 8, 10. | Decoration. | Shapes the cover and its irony. | 012, 019, 102 |
| SW-F-0005 | Pet lexicon | Powerful people speak to Monica as an animal to be tamed, fed and disciplined. | Comic surface over asymmetry. | 子リス; taming; owner; reward. | Chapters 4–8, epilogue. | Affectionate teasing. | Central to the Felix relation. | 036, 075, 078, 092 |
| SW-F-0006 | The riddle-song’s series | The same number series serves escape, memory, explanation and punishment. | Ties comic and dark registers. | Pig counts following the sum of the two before. | Chapters 2, 4, 5, 10. | Running gag. | Four functions in one volume. | 014, 037, 049, 109 |
| SW-F-0007 | Three-layer discrepancy | Legend, observers’ misreadings, interior shown side by side. | Reader alone holds all three. | Isabelle’s praise and the narrator’s causes. | Throughout. | — | The volume’s structural engine. | 018, 131 |
| SW-F-0008 | Comedy and harm | Comic register applied to coercion, a blow and a non-consensual kiss. | Harm sometimes registered, the kiss not. | Narrator’s abuse line; paw-pad joke. | Chapters 1, 7, 8. | All harmless play. Criterion: effect on the affected person registered independently of tone. | Normative baseline for later volumes. | 010, 070, 073, 076 |
| SW-F-0009 | Edition-level disclosure order | Frontispieces and character card disclose name, scenes and lines before the text. | Packaging pre-empts prose withholding. | Character card; night-fight caption. | Front matter. | Standard LN packaging. | Disclosure order differs from narrative order. | 124, 130 |

Records at V02:

| ID | Feature | Mechanism | Focalization and withholding | Wording evidence | Function and recurrence | Rival reading | Promotion reason | Obs. |
|---|---|---|---|---|---|---|---|---|
| SW-F-0010 | Power in Monica’s own viewpoint | Her magic narrated as calculation under constraint; awe kept in others. | Revises SW-F-0001; withholding moves from power to past. | Clock tower; horses; rope; barrier rewrite. | Prologue, chapters 3, 10, 11. | Exceptional scenes. | Changes how power scenes work from V02. | 004, 025, 086 |
| SW-F-0011 | Mirrored scenes | Paired scenes that invert or answer each other. | Reader alone sees both halves. | Dosed tea twice; hidden rescue and spoken name; hard and soft walls. | Chapters 7–8, prologue and 11, 11 and epilogue. | Coincidence. | Structural habit. | 005, 052, 084, 098 |
| SW-F-0012 | 場違い | One word tracks three outsiders and reverses meaning. | Social plot. | Refusal, charge, self-gift. | Prologue, chapter 6. | Common word. | Organizes class theme. | 003, 029, 031 |
| SW-F-0013 | Anonymity resolved by object | An unnamed agent identified by an object, not a name. | Fair-play withholding. | Red jewel, three rivets. | Prologue and chapter 11. | — | Technique for later mysteries. | 080, 111 |
| SW-F-0014 | Disclosure of the past in altered states | Backstory given in memory under stress and in delirium. | Reliability question. | Fire, bottle, poker. | Chapters 4 and 7. | Hallucination. | Governs evidential weight of backstory. | 034, 044, 045 |
| SW-F-0015 | Comedy and harm, V02 | Mercy and revenge played warmly; costs registered in the prose. | Harm to Cyril registered; revenge enjoyed. | Guilt tears; high laugh. | Chapter 8, epilogue. | All harmless. Criterion as SW-F-0008. | Normative continuity. | 052, 098 |
| SW-F-0016 | Performance and roles | Characters act parts: villainess, prince, friend, decoy, transfer student. | Masks within masks. | Isabelle’s lessons; Elliott on actors; Felix’s name. | Throughout. | Genre convention. | Links cover, Felix and Casey. | 055, 062, 116, 119 |

Records at V03:

| ID | Feature | Mechanism | Focalization and withholding | Wording evidence | Function and recurrence | Rival reading | Promotion reason | Obs. |
|---|---|---|---|---|---|---|---|---|
| SW-F-0017 | Rival’s retrospective prologue | Monica’s origin as a Sage told inside the envious friend’s mind. | Her interior withheld; his self-indictment unintended. | Bernie’s looking away; the curse of the hut. | Prologue; answered in chapters 4–5. | Mere backstory. | Changes how the past is sourced. | 004, 007, 009 |
| SW-F-0018 | Mourning frame | Bells, burned books and the dead recur across Monica’s and Felix’s strands. | Reader alone sees both strands. | The bell lore; the book burned twice. | Chapters 6–11. | Festival colour. | Organizes the climax’s motive. | 066, 088, 105, 108, 109, 113 |
| SW-F-0019 | Masks and the ghost | Disguise as the condition of candour. | Felix’s 僕 and laughter under the mask; Monica’s outreach as a ghost. | Ike; the gatekeeper’s costume. | Chapters 8–11, epilogue. | Romance trope. | Governs the Felix relation. | 078, 087, 100, 122 |
| SW-F-0020 | Repeated lines across viewpoints | A line spoken in one strand is repeated in another. | Links without stating identity. | The page’s line and Felix’s line about value. | Chapters 11 and its continuation. | Coincidence. | Technique of the Felix cluster. | 107, 112 |
| SW-F-0021 | The authoritative wrong verdict | A knowing adult closes the volume with a judgment the reader has seen contradicted. | Dramatic irony against Louis. | Heartless witch; no feeling to expect. | Secret episode. | Louis is right about strangers. | Evaluative pattern. | 130, 131 |

Records at V04:

| ID | Feature | Mechanism | Focalization and withholding | Wording evidence | Function and recurrence | Rival reading | Promotion reason | Obs. |
|---|---|---|---|---|---|---|---|---|
| SW-F-0022 | Sober retelling | Backstory first given in delirium retold by a narrator. | Reliability raised. | The uncle; the barn. | Prologue. | — | Changes the evidential weight of SW-C-0003. | 001–004 |
| SW-F-0023 | Misread gifts | Objects whose meaning differs between giver and receiver. | Reader sees both meanings. | Rose; necklace; pendant; handkerchief; wish. | Throughout. | Props. | Organizes the volume. | 032, 045, 097, 114, 116 |
| SW-F-0024 | Paired abused children | Monica and Cyril given parallel histories. | Chapters of others’ memories. | Violent men; withheld praise. | Prologue and chapter 7. | Coincidence. | Structural rhyme. | 002, 077 |
| SW-F-0025 | Verdict printed and reversed | Opening plate prints Louis’s verdict; the plot breaks it. | Paratext anticipates; prose refutes. | Plate; chapter 8. | Plate, chapters 4, 8, 9. | — | Evaluative pattern after SW-F-0021. | 050, 096, 124 |
| SW-F-0026 | Hero and constellation | The founding myth frames Felix’s wish. | Felix’s viewpoint withheld. | Ralph; stars. | Chapters 5–6, epilogue. | Festival colour. | Governs SW-C-0038. | 053, 064, 117 |

Records at AFTER04:

| ID | Feature | Mechanism | Focalization and withholding | Wording evidence | Function and recurrence | Rival reading | Promotion reason | Obs. |
|---|---|---|---|---|---|---|---|---|
| SW-F-0027 | Casebook | Four cases with paired detectives; interludes of origin. | Each case focalizes a different investigator. | Headings; frontispiece album. | Whole book. | Episodic filler. | Organizes the companion. | 038, 074, 105, 140, 163 |
| SW-F-0028 | Charm theory tested | Prologue theory dismissed; every case tests it. | Monica’s rejection then practice. | 「つまりは気分です、気分」 (S12:E000437). | Prologue to epilogue. | Coincidence of motif. | Governs SW-C-0041. | 014, 015, 066, 118, 139, 158 |
| SW-F-0029 | Inventory of kept objects | A drawer of gifts from people she deceives or will leave. | Monica’s view. | The list. | Cases I and IV. | Simple sentiment. | Bears on SW-C-0035. | 067, 149 |
| SW-F-0030 | Power seen by a spirit | Only the spirit and the reader see her power. | Spirit focalization. | 「駄目です、よ」 (S18:E001215). | Cases II, III. | Slapstick. | Governs SW-C-0042. | 092, 095, 116 |

Records at V05:

| ID | Feature | Mechanism | Focalization and withholding | Wording evidence | Function and recurrence | Rival reading | Promotion reason | Obs. |
|---|---|---|---|---|---|---|---|---|
| SW-F-0031 | The table lesson | Prologue lesson replayed against the protagonist. | Monica’s memory at the moment of loss. | 「勝負はテーブルに着く前から」 (S11:E000261). | Prologue; chapter nine. | Comic prologue. | Governs SW-C-0048. | 005–007, 129 |
| SW-F-0032 | Chime frame | A ritual sound frames vows. | Three focalizers at once. | Chime scenes. | Chapter one; epilogue. | Decoration. | Governs SW-C-0049. | 019–022, 176–180 |
| SW-F-0033 | Separate channel | The largest disclosure printed in images. | Felix’s view. | Image-set prose. | Chapter seven. | Production choice. | Bears on SW-C-0013. | 106 |
| SW-F-0034 | Plate enacted | The plate’s sentence returns at the climax. | Monica. | Plate; chapter ten. | Plate; chapter ten. | — | Pattern after SW-F-0025. | 009, 149 |

Records at V06:

| ID | Feature | Mechanism | Focalization and withholding | Wording evidence | Function and recurrence | Rival reading | Promotion reason | Obs. |
|---|---|---|---|---|---|---|---|---|
| SW-F-0035 | Anger named | An unnamed feeling named in a later scene and licensed in a third. | Monica; Louis. | 「これは、怒りだ」 (S20:E000112). | Chapters two, eight, ten. | Character growth only. | Governs SW-C-0051. | 064, 154, 184, 185 |
| SW-F-0036 | Help refrain | The request for help returns across focalizers. | Felix; Monica; Cyril; Bartholomeus. | Five scenes. | Chapters five to eleven; epilogue. | Coincidence of phrasing. | Governs SW-C-0052. | 114, 130, 166, 182, 207 |
| SW-F-0037 | Plate assigned | The bilingual plate’s words given later to a character. | Hubert. | Plate; chapter eight. | Plate; chapter eight. | — | Pattern after SW-F-0034. | 011, 156 |
| SW-F-0038 | Traits before names | Figures enter unnamed and are named later. | Bartholomeus; Glen; the narrator. | Red hair, rings, humming; the old man. | Chapters three, four, six, eight; secret episode. | Mystery device. | Bears on SW-C-0055. | 068, 088, 094, 125, 171 |

Records at V07:

| ID | Feature | Mechanism | Focalization and withholding | Wording evidence | Function and recurrence | Rival reading | Promotion reason | Obs. |
|---|---|---|---|---|---|---|---|---|
| SW-F-0039 | Two halves | The volume turns on one chapter from one secret to another. | Several. | Chapter eight’s two waiting scenes. | Chapter eight. | Episodic accident. | Governs SW-C-0062. | 146, 150 |
| SW-F-0040 | Legend completed | A framed legend completed by its subject’s own account. | Romaria. | Legend; her story. | Chapters four and seven. | — | Bears on SW-C-0061. | 060, 120 |
| SW-F-0041 | Plate assigned | The bilingual plate’s words given to a character. | Yuan. | Plate; epilogue. | Plate; epilogue. | — | Pattern after SW-F-0037. | 007, 222 |
| SW-F-0042 | Names in two tongues | Equivalent names in two languages as a clue. | Monica. | Iris; Bartholomew; Artur. | Chapter thirteen; epilogue. | Incidental. | Bears on SW-C-0058. | 206, 213 |

Records at V08:

| ID | Feature | Mechanism | Focalization and withholding | Wording evidence | Function and recurrence | Rival reading | Promotion reason | Obs. |
|---|---|---|---|---|---|---|---|---|
| SW-F-0043 | Framed memory | The identity given from inside a dream framed by sleep and waking. | Isaac. | Chapters four and eight. | Chapters four to eight. | — | Governs SW-C-0063. | 097, 176 |
| SW-F-0044 | One secret thrice | The secret as conclusion, memory and consequence. | Several. | Chapters two, four to seven, eight to thirteen. | Whole volume. | — | Governs SW-C-0063. | 040, 097, 203 |
| SW-F-0045 | Document withheld | A document read in the story with its last line withheld from the reader. | Monica. | The diary. | Chapter eleven. | — | Bears on SW-P-0050. | 246, 247 |
| SW-F-0046 | Second reveal | The heroine’s self-revelation answers the hero’s. | Monica. | The epilogue. | Epilogue. | — | Bears on SW-C-0067. | 290, 291 |

Records at V09:

| ID | Feature | Mechanism | Focalization and withholding | Wording evidence | Function and recurrence | Rival reading | Promotion reason | Obs. |
|---|---|---|---|---|---|---|---|---|
| SW-F-0047 | Trial from both sides | The trial told alternately from the accused and the advocate. | Isaac, Monica. | Chapters five and six. | Chapters five to six. | — | Governs SW-C-0069. | 080, 091 |
| SW-F-0048 | Epigraph assigned | The plate’s words given to the heroine. | Monica. | Plate; chapter six. | Plate; chapter six. | — | Pattern after SW-F-0041. | 004, 099 |
| SW-F-0049 | Coda by time skips | Short scenes across a year closing an arc. | Several. | Chapters nine to twelve. | Chapters nine to the epilogue. | — | Bears on SW-C-0074. | 135, 145, 151 |
| SW-F-0050 | Coffee ending | The opening image of solitude answered by company. | Monica. | Epilogue. | Epilogue. | — | Governs SW-C-0074. | 182 |

Records at EXTRA09:

| ID | Feature | Mechanism | Focalization and withholding | Wording evidence | Function and recurrence | Rival reading | Promotion reason | Obs. |
|---|---|---|---|---|---|---|---|---|
| SW-F-0051 | Collection by interval | Bonus stories ordered by the main story’s intervals, each chapter labelled. | Several. | Contents; chapter headings. | Whole collection. | — | Governs SW-C-0075. | 014, 036, 109, 130, 156 |
| SW-F-0052 | Frame of new writing | Post-council scenes bracket the school years. | Hilda; Monica. | Prologue; epilogue. | Prologue to secret episode. | — | Governs SW-C-0075. | 002, 166, 172 |
| SW-F-0053 | Motto | "A new land, a new life" printed and narrated. | Monica. | Title page; epilogue. | Title page; epilogue. | — | Bears on SW-C-0075. | 170, 183 |

## 8. Reconstruction readiness — SW-RD

Owns local, domain-specific readiness decisions, not operational model rules or global grades.

Fields: local identity; continuity/state/source boundary; requested output tier/domain; readiness state; evidence variety/ordinary/recipient coverage; affirmative limitations; missing evidence; held-out/prospective test route; actual results; restrictions/abstentions; reviewer/date; existing model/evidence path only when created; prior decision/revision route.

Readiness vocabulary and tier criteria come from [the character method](../00%20Frameworks%20and%20Methods/SW_CHARACTER_RECONSTRUCTION_METHOD.md). Absence of evidence and affirmative negative evidence are separately recorded. No character is assessed in this bootstrap.

Records at V01. These are evidence reviews made under the character method after V01 closure, not models. No recognition profile, domain model, fuller reconstruction or synthetic dialogue exists; no rule IDs exist; no test has been run; no tier is awarded. Global capability assessment remains with the designated curation process and is not touched. Reviewer: the V01 sequential integrator, 2026-10-14.

| ID | Identity; state boundary | Tier considered | Readiness state | Evidence variety | Affirmative limitations | Missing evidence | Test route | Restrictions |
|---|---|---|---|---|---|---|---|---|
| SW-RD-0001 | sw.monica; V01 exit | Recognition profile | UNASSESSED. Evidence inventory appears adequate for a future assessment. | Ordinary life, crisis, study, work; at least eight recipients with contrasting speech; consistent fluency conditions; self-report against conduct; counterevidence recorded. | Key past withheld; much of her interior comic in register. | Speech with strangers beyond the school’s first week; reaction to disclosure. | Freeze anchors before V02; check against V02 ordinary scenes. | No profile may be drafted without separate authorization. |
| SW-RD-0002 | sw.monica; V01 exit | Domain-bounded model | INSUFFICIENT_EVIDENCE | As above. | Single volume; romance, politics, family and formal Sage duty barely sampled. | Longitudinal transitions; domains above. | Later volumes. | — |
| SW-RD-0003 | sw.felix; V01 exit | Any tier | INSUFFICIENT_EVIDENCE | Public scenes, three private scenes, two outside judgments. | Affirmative limitation: his motives are deliberately withheld and his public statements are shown to be unreliable. | His wish; the duke’s hold; his nights. | Later disclosure. | Public behaviour must not be taken as interior evidence. |
| SW-RD-0004 | sw.cyril; V01 exit | Any tier | INSUFFICIENT_EVIDENCE | Rich interior in two scenes; consistent public conduct; recipient contrast between Felix and Monica. | Few ordinary scenes. | Ordinary life; family scenes. | Later volumes. | — |
| SW-RD-0005 | sw.louis; V01 exit | Any tier | INSUFFICIENT_EVIDENCE | Coercive public scenes; candid private scene; domestic glimpse. | Only one private scene. | Professional and family conduct. | Later volumes. | — |
| SW-RD-0006 | sw.nero; V01 exit | Any tier | INSUFFICIENT_EVIDENCE | Frequent dialogue with Monica; one scene with Felix. | Nature undisclosed. | Origin and limits. | Later disclosure. | — |
| SW-RD-0007 | sw.isabelle, sw.lana; V01 exit | Any tier | INSUFFICIENT_EVIDENCE | Several scenes each. | Thin interiors. | Viewpoint scenes. | Later volumes. | Keep explicitly thin. |
| SW-RD-0008 | All other V01 identities | Any tier | INSUFFICIENT_EVIDENCE | One to three scenes each. | Thin. | — | — | Keep explicitly thin. |

Records at V02, reviewer the V02 sequential integrator, 2026-10-14. Evidence reviews only; no model, profile, dialogue or tier.

| ID | Identity; state boundary | Tier considered | Readiness state | Evidence variety | Affirmative limitations | Missing evidence | Test route | Restrictions |
|---|---|---|---|---|---|---|---|---|
| SW-RD-0009 | sw.monica; V02 exit | Recognition profile | UNASSESSED. Evidence now spans two volumes, many recipients, ordinary life, crisis, negotiation and disclosed history. | Adequate for a future assessment. | Key history from delirium; romance absent. | Formal Sage duties among peers; family. | Hold-out scenes from a later volume. | No profile without separate authorization. |
| SW-RD-0010 | sw.monica; V02 exit | Domain-bounded model | INSUFFICIENT_EVIDENCE | As above. | Two volumes; politics and romance thin. | Longitudinal transitions. | Later volumes. | — |
| SW-RD-0011 | sw.felix; V02 exit | Any tier | INSUFFICIENT_EVIDENCE | Rich private scenes added. | Affirmative limitation: identity cluster unexplained; public statements unreliable. | Disclosure of SW-C-0022 matters. | Later disclosure. | Public behaviour is not interior evidence. |
| SW-RD-0012 | sw.cyril, sw.louis, sw.elliott, sw.casey, sw.lana, sw.claudia, sw.isabelle and all other identities; V02 exit | Any tier | INSUFFICIENT_EVIDENCE | Cyril, Louis, Elliott and Lana gained viewpoint scenes. | Casey removed from the school. | More ordinary scenes. | Later volumes. | Keep thin entries thin. |

Records at V03, reviewer the V03 sequential integrator, 2026-10-14. Evidence reviews only; no model, profile, dialogue or tier.

| ID | Identity; state boundary | Tier considered | Readiness state | Evidence variety | Affirmative limitations | Missing evidence | Test route | Restrictions |
|---|---|---|---|---|---|---|---|---|
| SW-RD-0013 | sw.monica; V03 exit | Recognition profile | UNASSESSED. Evidence spans three volumes, a retrospective outside view, sustained declaration, mourning and combat. | Adequate for a future assessment. | Her past is mostly sourced through others’ memories and delirium. | Sage duty among peers; family. | Hold-out scenes from a later volume. | No profile without separate authorization. |
| SW-RD-0014 | sw.monica; V03 exit | Domain-bounded model | INSUFFICIENT_EVIDENCE | As above. | Romance, politics and family still thin. | Longitudinal transitions. | Later volumes. | — |
| SW-RD-0015 | sw.felix; V03 exit | Any tier | INSUFFICIENT_EVIDENCE | Extensive private scenes, a persona, a dream. | Affirmative limitation: identity cluster unexplained and extended; persona and role statements unreliable as interior evidence. | Disclosure of SW-C-0022 matters. | Later disclosure. | Public and persona behaviour are not interior evidence. |
| SW-RD-0016 | sw.bernie, sw.louis, sw.mary, sw.elliott, sw.lana and all other identities; V03 exit | Any tier | INSUFFICIENT_EVIDENCE | Bernie, Louis, Mary, Elliott and Bartholomeus gained viewpoint scenes. | Most new identities appear in one volume. | More ordinary scenes. | Later volumes. | Keep thin entries thin. |

Records at V04, reviewer the V04 sequential integrator, 2026-10-14. Evidence reviews only.

| ID | Identity; state boundary | Tier considered | Readiness state | Evidence variety | Affirmative limitations | Missing evidence | Test route | Restrictions |
|---|---|---|---|---|---|---|---|---|
| SW-RD-0017 | sw.monica; V04 exit | Recognition profile | UNASSESSED. Four volumes, a sober childhood account, combat, social initiative and attachment. | Adequate for a future assessment. | Her inner life after leaving the school untested. | Family life with Hilda; Sage duties. | Hold-out scenes. | No profile without authorization. |
| SW-RD-0018 | sw.monica; V04 exit | Domain-bounded model | INSUFFICIENT_EVIDENCE | As above. | Romance absent; politics thin. | Longitudinal transitions. | Later volumes. | — |
| SW-RD-0019 | sw.felix; V04 exit | Any tier | INSUFFICIENT_EVIDENCE | Private attachment and wish stated. | Affirmative limitation: identity cluster unexplained; wish’s meaning withheld. | SW-C-0022 disclosures. | Later disclosure. | Persona and public behaviour are not interior evidence. |
| SW-RD-0020 | sw.cyril and all other identities; V04 exit | Any tier | INSUFFICIENT_EVIDENCE | Cyril’s history and viewpoint scenes now substantial. | Cyril’s feeling unnamed by himself. | His own account. | Later volumes. | Keep thin entries thin. |

Records at AFTER04, reviewer the AFTER04 sequential integrator, 2026-10-14. Evidence reviews only.

| ID | Identity; state boundary | Tier considered | Readiness state | Evidence variety | Affirmative limitations | Missing evidence | Test route | Restrictions |
|---|---|---|---|---|---|---|---|---|
| SW-RD-0021 | sw.monica; AFTER04 exit | Domain-bounded model | INSUFFICIENT_EVIDENCE | Ordinary-time conduct added: gifts, thanks, small lies. | Comic register; romance absent. | Longitudinal transitions. | Later volumes. | — |
| SW-RD-0022 | sw.felix; AFTER04 exit | Any tier | INSUFFICIENT_EVIDENCE | Ike in daylight; childhood interlude. | Affirmative limitation: identity cluster unexplained. | SW-C-0022 disclosures. | Later disclosure. | Persona and public behaviour are not interior evidence. |
| SW-RD-0023 | sw.cyril, sw.elliott and all other identities; AFTER04 exit | Any tier | INSUFFICIENT_EVIDENCE | Origins for Cyril, Elliott, Glen, Isabelle. | Retrospective scenes are brief. | Present-time conduct. | Later volumes. | Keep thin entries thin. |

Records at V05, reviewer the V05 sequential integrator, 2026-10-14. Evidence reviews only.

| ID | Identity; state boundary | Tier considered | Readiness state | Evidence variety | Affirmative limitations | Missing evidence | Test route | Restrictions |
|---|---|---|---|---|---|---|---|---|
| SW-RD-0024 | sw.monica; V05 exit | Domain-bounded model | INSUFFICIENT_EVIDENCE | Public persona as the Witch; accusation; goal change. | Silence imposed by disguise. | Longitudinal transitions. | Later volumes. | — |
| SW-RD-0025 | sw.felix; V05 exit | Any tier | INSUFFICIENT_EVIDENCE | Private viewpoint on the Witch and on Clockford. | Affirmative limitation: identity cluster unexplained. | SW-C-0022 disclosures. | Later disclosure. | Persona and public behaviour are not interior evidence. |
| SW-RD-0026 | sw.nero and all other identities; V05 exit | Any tier | INSUFFICIENT_EVIDENCE | Nero’s nature disclosed. | Nero’s viewpoint absent. | Own account. | Later volumes. | Keep thin entries thin. |

Records at V06, reviewer the V06 sequential integrator, 2026-10-14. Evidence reviews only.

| ID | Identity; state boundary | Tier considered | Readiness state | Evidence variety | Affirmative limitations | Missing evidence | Test route | Restrictions |
|---|---|---|---|---|---|---|---|---|
| SW-RD-0027 | sw.monica; V06 exit | Domain-bounded model | INSUFFICIENT_EVIDENCE | Anger named; two selves; inquiry advanced. | Help refused. | Longitudinal transitions. | Later volumes. | — |
| SW-RD-0028 | sw.felix; V06 exit | Any tier | INSUFFICIENT_EVIDENCE | Private viewpoint on Monica and on means. | Affirmative limitation: identity cluster unexplained. | SW-C-0022 disclosures. | Later disclosure. | Persona and public behaviour are not interior evidence. |
| SW-RD-0029 | all other identities; V06 exit | Any tier | INSUFFICIENT_EVIDENCE | New Sages and spirits on stage. | Thin. | Own accounts. | Later volumes. | Keep thin entries thin. |

Records at V07, reviewer the V07 sequential integrator, 2026-10-14. Evidence reviews only.

| ID | Identity; state boundary | Tier considered | Readiness state | Evidence variety | Affirmative limitations | Missing evidence | Test route | Restrictions |
|---|---|---|---|---|---|---|---|---|
| SW-RD-0030 | sw.monica; V07 exit | Domain-bounded model | INSUFFICIENT_EVIDENCE | Help asked; wish to know; withheld conclusion. | Interior conclusion unspoken. | Longitudinal transitions. | Later volumes. | — |
| SW-RD-0031 | sw.felix; V07 exit | Any tier | INSUFFICIENT_EVIDENCE | Others’ accounts of his past. | Affirmative limitation: identity cluster unexplained. | SW-C-0022, SW-C-0058 disclosures. | Later disclosure. | Persona and public behaviour are not interior evidence. |
| SW-RD-0032 | all other identities; V07 exit | Any tier | INSUFFICIENT_EVIDENCE | New households and spirits on stage. | Thin. | Own accounts. | Later volumes. | Keep thin entries thin. |

Records at V08, reviewer the V08 sequential integrator, 2026-10-14. Evidence reviews only.

| ID | Identity; state boundary | Tier considered | Readiness state | Evidence variety | Affirmative limitations | Missing evidence | Test route | Restrictions |
|---|---|---|---|---|---|---|---|---|
| SW-RD-0033 | sw.monica; V08 exit | Domain-bounded model | INSUFFICIENT_EVIDENCE | Choice of rescue; bargain; reveal. | The outcome withheld. | Longitudinal transitions. | Later volumes. | — |
| SW-RD-0034 | sw.felix (Isaac Walker); V08 exit | Domain-bounded model | INSUFFICIENT_EVIDENCE | Own memory of ten years; present conduct. | Identity now disclosed; misunderstanding withheld. | Response to the diary. | Later volumes. | The persona is evidence of performance, not interior. |
| SW-RD-0035 | all other identities; V08 exit | Any tier | INSUFFICIENT_EVIDENCE | Clockford in his own viewpoint briefly. | Thin. | Own accounts. | Later volumes. | Keep thin entries thin. |

Records at V09, reviewer the V09 sequential integrator, 2026-10-14. Evidence reviews only.

| ID | Identity; state boundary | Tier considered | Readiness state | Evidence variety | Affirmative limitations | Missing evidence | Test route | Restrictions |
|---|---|---|---|---|---|---|---|---|
| SW-RD-0036 | sw.monica; V09 exit | Domain-bounded model | INSUFFICIENT_EVIDENCE | A completed arc of disposition change. | Her feelings toward others unstated. | Longitudinal transitions to V09. | Later volumes. | — |
| SW-RD-0037 | sw.felix (Isaac Walker); V09 exit | Domain-bounded model | INSUFFICIENT_EVIDENCE | Memory, release and a new pursuit. | The new phase thin. | Later volumes. | Later volumes. | — |
| SW-RD-0038 | all other identities; V09 exit | Any tier | INSUFFICIENT_EVIDENCE | Coda sketches. | Thin. | Own accounts. | Later volumes. | Keep thin entries thin. |

Records at EXTRA09, reviewer the EXTRA09 sequential integrator, 2026-10-14. Evidence reviews only.

| ID | Identity; state boundary | Tier considered | Readiness state | Evidence variety | Affirmative limitations | Missing evidence | Test route | Restrictions |
|---|---|---|---|---|---|---|---|---|
| SW-RD-0039 | sw.monica; EXTRA09 exit | Domain-bounded model | INSUFFICIENT_EVIDENCE | States across the whole span, early and late. | Her inner life after the move thin. | Longitudinal transitions to EXTRA09. | Later volumes. | — |
| SW-RD-0040 | sw.cyril; EXTRA09 exit | Domain-bounded model | INSUFFICIENT_EVIDENCE | Past and private conduct enlarged. | His view of Monica unstated. | Later volumes. | Later volumes. | — |
| SW-RD-0041 | all other identities; EXTRA09 exit | Any tier | INSUFFICIENT_EVIDENCE | Vignettes. | Thin. | Own accounts. | Later volumes. | Keep thin entries thin. |

## 9. Unit closure and acceptance — SW-U

Owns cumulative transaction bookkeeping separately from claims.

Fields: witness/unit; source lock and locator fidelity state; admitted prose/image/paratext coverage independently; inspection completed; semantic review/acceptance state; each typed responsibility's update IDs or no-material-update rationale; exit freeze; durable/committed closure reference; remaining mandatory/optional evidence; publication/audit routes.

At initialization no numbered volume, supplement, or web unit was closed. Repository-wide publication facts belong to the entrypoint/actual Git workflow; this ledger links their receipts without guessing.

Records at V01:

| Field | SW-U-V01 |
|---|---|
| Witness and unit | `SW-LNJP-V01`, Japanese LN Volume 01. |
| Source lock and locator fidelity | Byte-locked; original local locator package recovered and its six inner seals verified 2026-10-14; every quoted fragment and cited locator in the reading verified against the sealed block map. |
| Prose coverage | Complete: prologue, ten chapters, epilogue, in-volume secret episode. |
| Image coverage | Complete: all 24 image resources viewed, including frontispieces, story illustrations and the four character-reference pages. |
| Paratext coverage | Complete: contents, credits, afterword, colophon, notices, jacket. |
| Inspection | Completed 2026-10-14. |
| Semantic review | Author self-review including later-knowledge leakage check; owner semantic acceptance not claimed. |
| SW-S | SW-S-0001 to SW-S-0024. |
| SW-R | SW-R-0001 to SW-R-0022. |
| SW-K | SW-K-0001 to SW-K-0020. |
| SW-W | SW-W-0001 to SW-W-0024. |
| SW-C / SW-CR | SW-C-0001 to SW-C-0018; no revision events because no predecessors existed. |
| SW-P | SW-P-0001 to SW-P-0012, all OPEN; no predictions. |
| SW-F | SW-F-0001 to SW-F-0009. |
| SW-RD | SW-RD-0001 to SW-RD-0008, evidence reviews only. |
| Exit freeze | `SW-FR-V01-EXIT` in the reading’s section 10. |
| Durable closure | The commit that adds the V01 reading and this record; its identity and CI receipts are in Git history, not here. |
| Remaining mandatory evidence | None. |
| Remaining optional evidence | Publisher-original EPUB comparison; printed pagination; web and companion comparisons, each requiring authorization. |
| Architecture review | First closed-volume review recorded in the synthesis architecture; one master ledger remains adequate; no split. |
| Editorial revision | 2026-10-14: reading version 1.1 named-subject and referential-clarity repair, with one recorded erratum aligning the synopsis to SW-C-0009; no claim, observation, locator, quotation or freeze changed; two ledger cells in SW-S identities and SW-R-0013 clarified from “his spirit” to Wildianu. See the V01 named-subject editorial audit. |

Records at V02:

| Field | SW-U-V02 |
|---|---|
| Witness and unit | `SW-LNJP-V02`, Japanese LN Volume 02. |
| Source lock and locator fidelity | Byte-locked 2026-10-14 in the source lock register; package built with the generalized driver; every quoted fragment and cited locator in the reading verified against the sealed block map. |
| Prose coverage | Complete: prologue, eleven chapters with continuation, epilogue, secret episode. |
| Image coverage | Complete: all 29 image resources accounted for; every admitted image viewed; preview images excluded. |
| Paratext coverage | Complete: contents, credits, afterword, colophon, notices, jacket; publisher preview excluded. |
| Inspection | Completed 2026-10-14. |
| Semantic review | Author self-review with leakage check and name-and-reference check; owner acceptance not claimed. |
| SW-S | SW-S-0025 to SW-S-0044. |
| SW-R | SW-R-0023 to SW-R-0042. |
| SW-K | SW-K-0021 to SW-K-0034. |
| SW-W | SW-W-0025 to SW-W-0040. |
| SW-C / SW-CR | SW-C-0019 to SW-C-0026; SW-CR-0001 to SW-CR-0018 on all V01 claims. |
| SW-P | SW-P-0013 to SW-P-0020 added; twelve statuses noted; no predictions. |
| SW-F | SW-F-0010 to SW-F-0016. |
| SW-RD | SW-RD-0009 to SW-RD-0012, evidence reviews only. |
| Exit freeze | `SW-FR-V02-EXIT` in the reading’s section 10. |
| Durable closure | The commit that adds the V02 reading and these records; receipts in Git history. |
| Remaining mandatory evidence | None. |
| Remaining optional evidence | Publisher-original comparison; printed pagination; web comparison. |
| Architecture review | Not due: no supplemental admission, no ledger pressure; recorded as reviewed in the architecture at V02. |

Records at V03:

| Field | SW-U-V03 |
|---|---|
| Witness and unit | `SW-LNJP-V03`, Japanese LN Volume 03. |
| Source lock and locator fidelity | Byte-locked 2026-10-14 in the source lock register; package built with the generalized driver; every quoted fragment and cited locator in the reading verified against the sealed block map. |
| Prose coverage | Complete: prologue, eleven chapters with continuation, epilogue, secret episode. |
| Image coverage | Complete: all 31 image resources accounted for; every admitted image viewed; preview images excluded. |
| Paratext coverage | Complete: contents, credits, afterword, colophon, notices, jacket (viewed after reading); publisher preview excluded, with incidental on-screen display recorded. |
| Inspection | Completed 2026-10-14. |
| Semantic review | Author self-review with leakage check and name-and-reference check; owner acceptance not claimed. |
| SW-S | SW-S-0045 to SW-S-0064. |
| SW-R | SW-R-0043 to SW-R-0058. |
| SW-K | SW-K-0035 to SW-K-0045. |
| SW-W | SW-W-0041 to SW-W-0054. |
| SW-C / SW-CR | SW-C-0027 to SW-C-0034; SW-CR-0019 to SW-CR-0044 on all earlier claims. |
| SW-P | SW-P-0021 to SW-P-0026 added; two retired with reason; statuses noted; no predictions. |
| SW-F | SW-F-0017 to SW-F-0021. |
| SW-RD | SW-RD-0013 to SW-RD-0016, evidence reviews only. |
| Exit freeze | `SW-FR-V03-EXIT` in the reading’s section 10. |
| Durable closure | The commit that adds the V03 reading and these records; receipts in Git history. |
| Remaining mandatory evidence | None. |
| Remaining optional evidence | Publisher-original comparison; printed pagination; web comparison. |
| Architecture review | Not due: no supplemental admission; one master ledger remains adequate; recorded as reviewed in the architecture at V03. |

Records at V04:

| Field | SW-U-V04 |
|---|---|
| Witness and unit | `SW-LNJP-V04`, Japanese LN Volume 04. |
| Source lock and locator fidelity | Byte-locked 2026-10-14; package built with the generalized driver; every quoted fragment and cited locator verified. |
| Prose coverage | Complete: prologue, eleven chapters with continuation, epilogue, secret episode. |
| Image coverage | Complete: all 32 image resources accounted for; every admitted image viewed; preview images excluded. |
| Paratext coverage | Complete: contents, credits, afterword, advertisement, colophon, notices, jacket; preview excluded. |
| Inspection | Completed 2026-10-14. |
| Semantic review | Author self-review with leakage and name-and-reference checks; owner acceptance not claimed. |
| SW-S | SW-S-0065 to SW-S-0084. |
| SW-R | SW-R-0059 to SW-R-0074. |
| SW-K | SW-K-0046 to SW-K-0057. |
| SW-W | SW-W-0055 to SW-W-0066. |
| SW-C / SW-CR | SW-C-0035 to SW-C-0040; SW-CR-0045 to SW-CR-0078, two with correction. |
| SW-P | SW-P-0027 to SW-P-0032 added; five retired with reason; statuses noted. |
| SW-F | SW-F-0022 to SW-F-0026. |
| SW-RD | SW-RD-0017 to SW-RD-0020. |
| Exit freeze | `SW-FR-V04-EXIT` in the reading’s section 10. |
| Durable closure | The commit that adds the V04 reading and these records. |
| Remaining mandatory evidence | None. |
| Remaining optional evidence | Publisher-original comparison; printed pagination; web comparison. |
| Architecture review | Required before IV -after- is admitted; recorded in the architecture with the companion’s admission. |

Records at AFTER04:

| Field | SW-U-AFTER04 |
|---|---|
| Witness and unit | `SW-LNJP-AFTER04`, the Japanese companion IV -after-, a supplemental unit admitted after V04. |
| Source lock and locator fidelity | Byte-locked 2026-10-14; publisher-layout witness with a recorded packaging deviation; package built with the revised generalized driver; every quoted fragment and cited locator verified. |
| Prose coverage | Complete: prologue, five interludes, four cases, epilogue, secret episode. |
| Image coverage | Complete: 31 of 36 image resources viewed; the four preview images and the store image not viewed. |
| Paratext coverage | Complete: contents, credits, character reference, afterword, colophon, notices, jacket; preview excluded. |
| Placement | Story-level check in the reading’s section 10: every case inside the interval; five retrospective scenes; nothing held out. |
| Inspection | Completed 2026-10-14. |
| Semantic review | Author self-review with leakage, name-and-reference and placement checks; owner acceptance not claimed. |
| SW-S | SW-S-0085 to SW-S-0102. |
| SW-R | SW-R-0075 to SW-R-0089. |
| SW-K | SW-K-0058 to SW-K-0066. |
| SW-W | SW-W-0067 to SW-W-0074. |
| SW-C / SW-CR | SW-C-0041 to SW-C-0044; SW-CR-0079 to SW-CR-0118 on all earlier claims. |
| SW-P | SW-P-0033 to SW-P-0036 added; statuses noted. |
| SW-F | SW-F-0027 to SW-F-0030. |
| SW-RD | SW-RD-0021 to SW-RD-0023. |
| Exit freeze | `SW-FR-AFTER04-EXIT` in the reading’s section 10. |
| Durable closure | The commit that adds the companion reading and these records. |
| Remaining mandatory evidence | None. |
| Remaining optional evidence | Publisher-original comparison; printed pagination. |
| Architecture review | Performed before admission and recorded in the architecture. |

Records at V05:

| Field | SW-U-V05 |
|---|---|
| Witness and unit | `SW-LNJP-V05`, Japanese LN Volume 05. |
| Source lock and locator fidelity | Byte-locked 2026-10-14; publisher-layout witness with a packaging deviation; every quoted fragment and cited locator verified. |
| Prose coverage | Complete, including chapter seven’s image-set prose. |
| Image coverage | 24 of 31 image resources viewed; cover, title page, contents, store image, glyph and preview images not viewed. |
| Paratext coverage | Complete; preview excluded. |
| Inspection | Completed 2026-10-14. |
| Semantic review | Author self-review with leakage and name-and-reference checks; owner acceptance not claimed. |
| SW-S | SW-S-0103 to SW-S-0120. |
| SW-R | SW-R-0090 to SW-R-0102. |
| SW-K | SW-K-0067 to SW-K-0077. |
| SW-W | SW-W-0075 to SW-W-0082. |
| SW-C / SW-CR | SW-C-0045 to SW-C-0050; SW-CR-0119 to SW-CR-0162 on all earlier claims. |
| SW-P | SW-P-0037 to SW-P-0040 added; two retired with reason; statuses noted. |
| SW-F | SW-F-0031 to SW-F-0034. |
| SW-RD | SW-RD-0024 to SW-RD-0026. |
| Exit freeze | `SW-FR-V05-EXIT` in the reading’s section 10. |
| Durable closure | The commit that adds the V05 reading and these records. |
| Remaining mandatory evidence | None. |
| Remaining optional evidence | Publisher-original comparison; printed pagination; the unviewed identifying images. |
| Architecture review | Not due: no supplemental admission; recorded as a note in the architecture. |

Records at V06:

| Field | SW-U-V06 |
|---|---|
| Witness and unit | `SW-LNJP-V06`, Japanese LN Volume 06. |
| Source lock and locator fidelity | Byte-locked 2026-10-14; publisher-layout witness with a packaging deviation; every quoted fragment and cited locator verified. |
| Prose coverage | Complete, including chapter eight’s continuation and the secret episode. |
| Image coverage | 25 of 32 image resources viewed; cover, title page, contents, store image, glyph and preview images not viewed. |
| Paratext coverage | Complete; preview excluded. |
| Inspection | Completed 2026-10-14. |
| Semantic review | Author self-review with leakage and name-and-reference checks; owner acceptance not claimed. |
| SW-S | SW-S-0121 to SW-S-0138. |
| SW-R | SW-R-0103 to SW-R-0116. |
| SW-K | SW-K-0078 to SW-K-0089. |
| SW-W | SW-W-0083 to SW-W-0091. |
| SW-C / SW-CR | SW-C-0051 to SW-C-0056; SW-CR-0163 to SW-CR-0212 on all earlier claims. |
| SW-P | SW-P-0041 to SW-P-0044 added; two retired with reason; statuses noted. |
| SW-F | SW-F-0035 to SW-F-0038. |
| SW-RD | SW-RD-0027 to SW-RD-0029. |
| Exit freeze | `SW-FR-V06-EXIT` in the reading’s section 10. |
| Durable closure | The commit that adds the V06 reading and these records. |
| Remaining mandatory evidence | None. |
| Remaining optional evidence | Publisher-original comparison; printed pagination; the unviewed identifying images. |
| Architecture review | Not due: no supplemental admission; recorded as a note in the architecture. |

Records at V07:

| Field | SW-U-V07 |
|---|---|
| Witness and unit | `SW-LNJP-V07`, Japanese LN Volume 07. |
| Source lock and locator fidelity | Byte-locked 2026-10-14; publisher-layout witness, `mimetype` first; every quoted fragment and cited locator verified. |
| Prose coverage | Complete, including chapter six’s continuations and the secret episode. |
| Image coverage | 24 of 33 image resources viewed; cover, title page, contents, store image, glyph and preview images not viewed. |
| Paratext coverage | Complete; preview excluded. |
| Inspection | Completed 2026-10-14. |
| Semantic review | Author self-review with leakage and name-and-reference checks; owner acceptance not claimed. |
| SW-S | SW-S-0139 to SW-S-0156. |
| SW-R | SW-R-0117 to SW-R-0130. |
| SW-K | SW-K-0090 to SW-K-0101. |
| SW-W | SW-W-0092 to SW-W-0099. |
| SW-C / SW-CR | SW-C-0057 to SW-C-0062; SW-CR-0213 to SW-CR-0268 on all earlier claims. |
| SW-P | SW-P-0045 to SW-P-0048 added; three retired with reason; statuses noted. |
| SW-F | SW-F-0039 to SW-F-0042. |
| SW-RD | SW-RD-0030 to SW-RD-0032. |
| Exit freeze | `SW-FR-V07-EXIT` in the reading’s section 10. |
| Durable closure | The commit that adds the V07 reading and these records. |
| Remaining mandatory evidence | None. |
| Remaining optional evidence | Publisher-original comparison; printed pagination; the unviewed identifying images. |
| Architecture review | Not due: no supplemental admission; recorded as a note in the architecture. |

Records at V08:

| Field | SW-U-V08 |
|---|---|
| Witness and unit | `SW-LNJP-V08`, Japanese LN Volume 08. |
| Source lock and locator fidelity | Byte-locked 2026-10-14; publisher-layout witness, `mimetype` first; every quoted fragment and cited locator verified. |
| Prose coverage | Complete, including the epilogue’s closing line and the secret episode. |
| Image coverage | 25 of 33 image resources viewed; cover, title page, contents, store image, glyph and preview images not viewed. |
| Paratext coverage | Complete; preview excluded. |
| Inspection | Completed 2026-10-14. |
| Semantic review | Author self-review with leakage and name-and-reference checks; owner acceptance not claimed. |
| SW-S | SW-S-0157 to SW-S-0174. |
| SW-R | SW-R-0131 to SW-R-0144. |
| SW-K | SW-K-0102 to SW-K-0113. |
| SW-W | SW-W-0100 to SW-W-0107. |
| SW-C / SW-CR | SW-C-0063 to SW-C-0068; SW-CR-0269 to SW-CR-0330 on all earlier claims. |
| SW-P | SW-P-0049 to SW-P-0052 added; fifteen retired with reason; statuses noted. |
| SW-F | SW-F-0043 to SW-F-0046. |
| SW-RD | SW-RD-0033 to SW-RD-0035. |
| Exit freeze | `SW-FR-V08-EXIT` in the reading’s section 10. |
| Durable closure | The commit that adds the V08 reading and these records. |
| Remaining mandatory evidence | None. |
| Remaining optional evidence | Publisher-original comparison; printed pagination; the unviewed identifying images. |
| Architecture review | Not due: no supplemental admission; recorded as a note in the architecture. |

Records at V09:

| Field | SW-U-V09 |
|---|---|
| Witness and unit | `SW-LNJP-V09`, Japanese LN Volume 09. |
| Source lock and locator fidelity | Byte-locked 2026-10-14; converted witness re-packaged by calibre, `mimetype` first; every quoted fragment and cited locator verified. |
| Prose coverage | Complete, including chapter eight’s continuation. |
| Image coverage | 22 of 27 image resources viewed at the witness’s low resolution; cover, title page, contents, the V10 preview and store image not viewed. |
| Paratext coverage | Complete; the V10 preview page excluded. |
| Inspection | Completed 2026-10-14. |
| Semantic review | Author self-review with leakage and name-and-reference checks; owner acceptance not claimed. |
| SW-S | SW-S-0175 to SW-S-0188. |
| SW-R | SW-R-0145 to SW-R-0156. |
| SW-K | SW-K-0114 to SW-K-0121. |
| SW-W | SW-W-0108 to SW-W-0115. |
| SW-C / SW-CR | SW-C-0069 to SW-C-0074; SW-CR-0331 to SW-CR-0398 on all earlier claims. |
| SW-P | SW-P-0053 to SW-P-0056 added; ten retired with reason; statuses noted. |
| SW-F | SW-F-0047 to SW-F-0050. |
| SW-RD | SW-RD-0036 to SW-RD-0038. |
| Exit freeze | `SW-FR-V09-EXIT` in the reading’s section 10. |
| Durable closure | The commit that adds the V09 reading and these records. |
| Remaining mandatory evidence | None. |
| Remaining optional evidence | A full-resolution publisher witness; printed pagination; the unviewed identifying images. |
| Architecture review | Due before the IX -extra- admission: recorded as a note in the architecture. |

Records at EXTRA09:

| Field | SW-U-EXTRA09 |
|---|---|
| Witness and unit | `SW-LNJP-EXTRA09`, the Japanese companion IX -extra-. |
| Source lock and locator fidelity | Byte-locked 2026-10-14; converted EPUB 2 witness re-packaged by calibre; driver revised a second time; every quoted fragment and cited locator verified. |
| Prose coverage | Complete: prologue, fifty-four stories, epilogue and secret episode. |
| Image coverage | 39 of 43 image resources viewed; cover, title page, store image and an inline glyph not viewed. |
| Paratext coverage | Complete, including the design materials, the afterword and the provenance list. |
| Inspection | Completed 2026-10-14. |
| Semantic review | Author self-review with leakage and name-and-reference checks; owner acceptance not claimed. |
| SW-S | SW-S-0189 to SW-S-0198. |
| SW-R | SW-R-0157 to SW-R-0164. |
| SW-K | SW-K-0122 to SW-K-0127. |
| SW-W | SW-W-0116 to SW-W-0121. |
| SW-C / SW-CR | SW-C-0075 to SW-C-0078; SW-CR-0399 to SW-CR-0472 on all earlier claims. |
| SW-P | SW-P-0057 and SW-P-0058 added; none retired; statuses noted. |
| SW-F | SW-F-0051 to SW-F-0053. |
| SW-RD | SW-RD-0039 to SW-RD-0041. |
| Exit freeze | `SW-FR-EXTRA09-EXIT` in the reading’s section 10. |
| Durable closure | The commit that adds the IX -extra- reading and these records. |
| Remaining mandatory evidence | None. |
| Remaining optional evidence | A publisher-original witness; printed pagination; the unviewed identifying images; the original bonus printings. |
| Placement | Story-level check in the reading’s section 10; one label-versus-content discrepancy recorded. |

## Write, amend, and split rules

The authorized sequential integrator appends source-bearing state and revision events after full unit inspection. Patch current claim/readiness views only with preserved prior events. Record every affected responsibility's material delta or explained no-update in the unit closeout. Coverage completion never mechanically promotes an inference or readiness level.

Correct an objective error through an explicit correction event retaining old/new evidence routes and affected homes. Later reinterpretation is a source-bounded revision, not a rewrite of the historical freeze. If a record cannot be supported, defer or mark uncertainty rather than padding a table.

Split a typed responsibility only after recurring evidence establishes independent retrieval/revision pressure or a separate specialist dependency. Record exact transferred IDs, ownership, new path and necessary bounded backfill in architecture/entrypoint. Preserve historical routes and prohibit duplicate live datasets. Architecture-defined split decisions, not arbitrary row counts, govern this transition.
