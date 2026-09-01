---
title: "86 V2 Source Inventory"
series: "86―エイティシックス―"
artifact: "source_inventory"
version: "2.1-phase0-final"
date: "2026-08-13"
status: "FINAL_LOCKED_V1_14"
---

# 86―エイティシックス― — V2 Source Inventory

## Phase 0 status

**Phase 0 is complete and the Japanese-primary source lock is final for the currently supplied corpus.** The replacement Volume 14 has passed the same ZIP/package/spine/language/image audit used for the rest of the corpus, restoring an admissible Japanese V1–14 sequence. The previously rejected Chinese-dominant V14 (SHA-256 `93dd8fd85dd4753c398268402d1fc0f067a6d9c3385780981492b7bc61572e66`) has been removed from the active local and Drive source corpus; its hash is retained only as rejection-history provenance.

This document is the canonical Phase 0 inventory required by `86_MULTI_DOCUMENT_SYNTHESIS_ARCHITECTURE_V2.md`. It records source identity, integrity, language, internal structure, illustration payload, evidentiary status, supplements, and lock rules. It does **not** perform literary synthesis.

## 1. Governing source hierarchy

1. **Mainline Japanese primary prose:** numbered novels V1–14 are locked and admissible as the governing narrative corpus.
2. **Canonical/supplemental author prose:** `Alter.1` is admissible as Japanese author-written supplemental prose, but individual stories must be placed chronologically before being used for longitudinal claims.
3. **Official Dengeki web SS:** 27 stories are archived. The nine explicitly labeled `貴族if` stories are counterfactual. The remaining 18 are source-authentic but remain continuity-unclassified until contextual placement.
4. **Author-written counterfactual/AU prose:** `Alter.2` and the nine `貴族if` web stories are retained for controlled counterfactual characterization only. They cannot establish mainline events.
5. **Embedded visual/paratextual evidence:** covers, color inserts, monochrome illustrations, graphic dividers, afterwords and colophons may support visual/paratextual claims, but do not override the narrative prose.
6. **Legacy transcript:** the prior-chat transcript is a hypothesis/revision bank only. It is never a substitute for a primary-source locator.

## 2. EPUB audit matrix

| Source | Evidentiary status | ZIP | Spine | Images | Actual language | SHA-256 | Notes |
|---|---|---:|---:|---:|---|---|---|
| Volume 01 | `PRIMARY_JAPANESE` | PASS | 35 | 22 | Japanese | `09f9ef31033945e5…` | EPUB mimetype member is compressed |
| Volume 02 | `PRIMARY_JAPANESE` | PASS | 24 | 20 | Japanese | `aa78286d5036091e…` | EPUB mimetype member is compressed |
| Volume 03 | `PRIMARY_JAPANESE` | PASS | 28 | 20 | Japanese | `8d7708267ac15d1e…` | EPUB mimetype is not first ZIP member; EPUB mimetype member is compressed |
| Volume 04 | `PRIMARY_JAPANESE` | PASS | 26 | 21 | Japanese | `b01ea7cd93a09a7a…` | EPUB mimetype member is compressed |
| Volume 05 | `PRIMARY_JAPANESE` | PASS | 23 | 20 | Japanese | `6f415a5848985550…` | EPUB mimetype member is compressed |
| Volume 06 | `PRIMARY_JAPANESE` | PASS | 22 | 22 | Japanese | `58b18e7e12059014…` | Clean structural pass |
| Volume 07 | `PRIMARY_JAPANESE` | PASS | 23 | 21 | Japanese | `cbf40552883ad820…` | Clean structural pass |
| Volume 08 | `PRIMARY_JAPANESE` | PASS | 26 | 19 | Japanese | `c3de5072add0336e…` | Clean structural pass |
| Volume 09 | `PRIMARY_JAPANESE` | PASS | 27 | 20 | Japanese | `980e1fdb37bd3096…` | Clean structural pass |
| Volume 10 | `PRIMARY_JAPANESE` | PASS | 47 | 32 | Japanese | `38038c0fb4495eb4…` | Clean structural pass |
| Volume 11 | `PRIMARY_JAPANESE` | PASS | 46 | 31 | Japanese | `e79f5af1d3af6ab2…` | Clean structural pass |
| Volume 12 | `PRIMARY_JAPANESE` | PASS | 23 | 19 | Japanese | `5324b68ffb6a9be2…` | Clean structural pass |
| Alter 01 | `PRIMARY_JAPANESE` | PASS | 70 | 16 | Japanese | `226f1909fd53a39b…` | Clean structural pass |
| Volume 13 | `PRIMARY_JAPANESE` | PASS | 24 | 19 | Japanese | `e9e02b6bdabaf0b4…` | Clean structural pass |
| Alter 02 | `AUTHOR_COUNTERFACTUAL_AU` | PASS | 33 | 13 | Japanese | `b155b45bf2448f5b…` | Clean structural pass |
| Volume 14 | `PRIMARY_JAPANESE` | PASS | 23 | 17 | Japanese | `0530e6d0ad217fe1…` | EPUB mimetype member is compressed; replacement source accepted after language/content re-audit |

### Packaging warnings

The packaging warnings on V1, V2, V4, V5 and V14 concern EPUB conformance rather than narrative completeness: their `mimetype` member is compressed; V3 places `mimetype` outside the first archive position. These are reader/validator compatibility defects, not missing-text findings.

### Volume 14 replacement acceptance

The accepted replacement identifies itself as `８６―エイティシックス―Ep.14 ―ペイント・イット・ブラック―`, declares `ja`, and—unlike the rejected prior file—contains a strongly Japanese narrative body: approximately **98,015 kana** and **43,352 Han characters** across the extracted spine (kana/Han ratio ≈ **2.26**), with no Unicode replacement characters. The ZIP archive passes CRC testing; all 23 spine entries resolve and parse; all 17 image references resolve and all 17 raster images decode successfully. Its colophon identifies the Dengeki Bunko edition dated **2025-09-10**. The only warning is compressed EPUB `mimetype`, which is non-textual.

The earlier Chinese-dominant V14 is retained only in rejection-history metadata by checksum and must never be cited.

## 3. Publication-order lock

The reading sequence is anchored to the numbered novels. Supplemental collections are inserted by publication provenance but their internal stories are not assumed to occur at collection-publication time.

1. **Volume 01** — 2017
2. **Volume 02** — 2017
3. **Volume 03** — 2018
4. **Volume 04** — 2018
5. **Volume 05** — 2018
6. **Volume 06** — 2019
7. **Volume 07** — 2019
8. **Volume 08** — 2020
9. **Volume 09** — 2021
10. **Volume 10** — 2021
11. **Volume 11** — 2022
12. **Volume 12** — 2023-02-10
13. **Alter 01** — 2023-04-07
14. **Volume 13** — 2024-01-10
15. **Alter 02** — 2025-01-10
16. **Volume 14** — 2025-09-10

Operational rule: `Alter.1` was published between V12 and V13, but its stories span earlier continuity periods. The web SS likewise require story-level chronological placement. `Alter.2` remains a counterfactual branch regardless of publication position.

## 4. Chapter / structural inventory

### Volume 01
- 序章　戦野に紅く雛罌粟の咲く
- 第一章　戦死者ゼロの戦場
- 第二章　白骨戦線異状なし
- 第三章　夜闇の冥府のほとりにおけるご立派な君の
- 間章　首のない騎士
- 第四章　我が名は〈亡霊の軍勢〉、数多なれば
- 間章　首のない騎士Ⅱ
- 第五章　スピアヘッド戦隊にクソ栄光あれ
- 間章　首のない騎士Ⅲ
- 第六章　せめて人間たらんと
- 間章　首のない騎士Ⅳ
- 第七章　さよなら
- 終章　鮮血女王のお成り
- 終章─二　Ｒｅｂｏｏｔ──始動
- あとがき

### Volume 02
- 序章　女王陛下は戦都にいまし
- 第一章　ワルキューレの騎行
- 第二章　パンツァー・リート
- 第三章　ワイルド・ブルー・ヤンダー
- 第四章　双頭の鷲の旗の下に
- 第五章　クライズ・テイク・エイム
- 間章　ウェン・〝ジョン・ドゥ〟・カムズ・マーチング・ホーム
- あとがき

### Volume 03
- 間章　ゲット・ユア・ガンズ
- 第六章　オーバー・ゼア
- 第七章　死して甲斐あるものなれば
- 第八章　ラン・スルー・ザ・バトルフロント
- 第九章　久しく待ちにし
- 終章　ウィル・ミート・アゲイン
- あとがき

### Volume 04
- 序章　ミッシング・イン・アクション
- 第一章　コール・オン・デューティ
- 第二章　アイデンティフィケーション・フレンド・オア・フォー
- 第三章　フロント・トゥワード・エネミー
- 第四章　トリアージ
- 終章　ウーンデッド・イン・アクション
- あとがき

### Volume 05
- 序章　屍の王
- 第一章　怪物どもの憂愁
- 第二章　白鳥の砦
- 第三章　シンギング・バードの嘆きも知らず
- 第四章　エクスマキナ
- 終章　花など咲かぬ、雪の野に
- あとがき

### Volume 06
- 序章　ハーシュ・ミストレス
- 第一章　人狼は森に
- 第二章　ライフズ・バッド・ア・ウォーキング・シャドウ
- 第三章　シュート・ザ・ムーン
- 第四章　イン・ヒズ・ヘヴン
- 終章　ホーム・スイート・ホーム
- あとがき

### Volume 07
- 序章　戦場の霧
- 第一章　ヘイズ・ブルー
- 第二章　ミスト・ブルー
- 第三章　フォグ・ブルー
- 第四章　スターライト・ブルー
- あとがき

### Volume 08
- 序章　ザ・レッド・ドラゴン
- 第一章　ザ・ガン・イン・ザ・ハイ・キャッスル
- 第二章　モービィ・ディック・オア・ザ・ホエイル
- 第三章　イントゥ・ザ・ストーム
- 第四章　ザ・タワー（アップライト）
- 第五章　ザ・タワー（リバース）
- あとがき

### Volume 09
- 序章　暴食の獣
- 第一章　人魚の取引
- 間章　スペードの王とハートの女王の、とても永くてくだらない諍い
- 第二章　灰かぶりの戦場
- 間章　青い鳥はどこにいたのか
- 第三章　彼女の首を刎ねよ
- 間章　ところでジークフリートの殺し方を知るには
- 第四章　鏡よ鏡、ただの鏡に映るのは？
- 第五章　笛吹きはネズミどもと子供を連れて
- 終章　ワニの腹でも時計は進む
- あとがき

### Volume 10
- フラグメンタル・ネオテニー〈Pledge〉
- フラグメンタル・ネオテニー〈Misericorde〉
- フラグメンタル・ネオテニー〈Varlet〉
- フラグメンタル・ネオテニー〈Brand〉
- フラグメンタル・ネオテニー〈Undertaker〉
- フラグメンタル・ネオテニー〈Culpa〉
- トリアージタグ・ブラックのありふれた日常
- レテの畔
- ファイド
- 優しかった世界
- あとがき

### Volume 11
V11 uses a substantial sequence of image-only graphic dividers rather than a conventional machine-readable chapter TOC. Prominent D-Day labels are transcribed below; image-only transitions remain explicitly marked rather than guessed.
- D-DAY MINUS TWO
- D-DAY MINUS ONE
- D-DAY
- D-DAY PLUS ONE
- [image-only transition divider]
- D-DAY PLUS THREE
- [image-only transition divider]
- D-DAY PLUS TEN
- [image-only transition divider]
- D-DAY PLUS ELEVEN
- [image-only transition divider]
- D-DAY PLUS ELEVEN [second divider]
- D-DAY PLUS EIGHTEEN
- [image-only final transition divider]
- あとがき

### Volume 12
- 序章　メアリィ・ブルーの聖地
- 第一章　優しく美しきクイーン・メアリィの、美しく優しいはずだった世界
- 第二章　メアリィ・スーの行進
- 第三章　叶いたまえ、ヘイル・メアリィ
- 第四章　メアリィの小さな仔羊と、いつもの羊狩り骸骨たち
- 第五章　ブラッディ・メアリィは霧の中
- 終章　メアリィ・ジェーンの悪夢へようこそ、親愛なる鹿狩人
- あとがき

### Alter 01
- サンマグノリア共和国編
- 冬の日に、隻影二つ
- 八月二十五日（ライデン誕生日）
- レーナ＋アネット
- クレイモア戦隊
- ダイヤ＋アンジュ
- セオ＋カイエ＋ハルト＋ファイド
- ライデン＋クレナ
- シン＋レーナ
- 常闇のヘブンリー・ブルー
- 朽骨の剣尖
- 仔猫
- ギアーデ連邦編
- 成長
- 兄妹
- 買い物
- 徒歩圏内
- 哨戒任務
- 怪物の殻の向こう
- 死神ｍｅｅｔｓバカ兄貴＆堅物な親戚の兄ちゃん
- 這い飛ぶ大鳥
- いたずら（レーナ→シン）
- いたずら（シン→レーナ）
- 女王陛下、トレーニングをする
- ＨＥＬＰ！ （レーナの場合）
- 盃に射す影
- ＨＥＬＰ！ （シンの場合）
- 五月十九日（シン誕生日）
- 五月六日（クレナ誕生日）
- ロア＝グレキア連合王国編
- チェス
- もう少しだけ、このまま
- 君の気配・シンの場合
- 君の気配・レーナの場合
- コーヒーと紅茶と
- かつて共に極光を見た
- 死神ときどき青春編
- 五月十九日（シン誕生日）その二
- 学習しない死神
- ちなみにこの時のアネットとダスティン
- 君がいるから・レーナの場合
- 君がいるから・シンの場合
- 四月二十日（セオ誕生日）
- スターシャワー・レモネード
- 七月十二日（レーナ誕生日）
- 五月十九日（シン誕生日） ちょっとした仕掛け
- 七月十二日（レーナ誕生日）・その二
- ちびシンとちびアネット、からの今シンと今アネット
- 十月二日（アンジュ誕生日）
- 十一月十二日（アネット誕生日）
- オールスター香水バトル
- 奥付

### Volume 13
- 序章　ふりさけみれば
- 第一章　いざ言とはむ
- 第二章　面影は見ゆらむものを
- 第三章　いかが答へし
- 第四章　恨みつべしや
- 第五章　出でしあとの月影
- あとがき

### Alter 02
- 魔法少女レジーナ☆レーナ ～戦え！ 銀河航行戦艦サンマグノリア～
- 魔法少女レジーナ☆レーナ＆エンプレス☆フレデリカ ～必殺！ 〈レギオン〉殲滅砲～
- 魔法少女ラーカー☆ヴィーカ ～飛翔べ！ 火の鳥チャイカ！（…と我らがバカ王子！）～
- 奥付

### Volume 14
- 序章　小部屋の中の爬虫ども（キャタピラーズ・イン・セル）
- 第一章　泥を這いずる（ワーム・イン・マッド）
- 第二章　黒蝶の落とし仔（スパングルズ・スパウン）
- 第三章　血黒の蝶（ブラッドブラック・ヴァネッサ）
- 第四章　白蝶瞬きて（フェイント・ホワイト）
- 第五章　羽化について（ネゴシエーション・オン・イマージェンス）
- 終章　緋虎は赫々と（クリムゾン・タイガー・バーニング）
- あとがき

## 5. Illustration and visual-payload inventory

Every admissible EPUB has an embedded visual payload and all locally referenced image files in V1–14, Alter.1 and Alter.2 resolve without broken references; image decode checks pass. The inventory below records manifest image counts. These counts include covers and design/section art as well as narrative illustrations.

| Source | Manifest image items | Visual handling rule |
|---|---:|---|
| Volume 01 | 22 | Inspect scene-relevant illustrations during the corresponding volume pass. |
| Volume 02 | 20 | Inspect scene-relevant illustrations during the corresponding volume pass. |
| Volume 03 | 20 | Inspect scene-relevant illustrations during the corresponding volume pass. |
| Volume 04 | 21 | Inspect scene-relevant illustrations during the corresponding volume pass. |
| Volume 05 | 20 | Inspect scene-relevant illustrations during the corresponding volume pass. |
| Volume 06 | 22 | Inspect scene-relevant illustrations during the corresponding volume pass. |
| Volume 07 | 21 | Inspect scene-relevant illustrations during the corresponding volume pass. |
| Volume 08 | 19 | Inspect scene-relevant illustrations during the corresponding volume pass. |
| Volume 09 | 20 | Inspect scene-relevant illustrations during the corresponding volume pass. |
| Volume 10 | 32 | Inspect scene-relevant illustrations during the corresponding volume pass. |
| Volume 11 | 31 | Includes 14 graphic section-divider images; use visual inspection for divider semantics. |
| Volume 12 | 19 | Inspect scene-relevant illustrations during the corresponding volume pass. |
| Alter 01 | 16 | Inspect scene-relevant illustrations during the corresponding volume pass. |
| Volume 13 | 19 | Inspect scene-relevant illustrations during the corresponding volume pass. |
| Alter 02 | 13 | Counterfactual visual evidence only. |
| Volume 14 | 17 | Inspect scene-relevant illustrations during the corresponding volume pass. |

No stand-alone map payload has been asserted merely from filenames. Where a map, diagram, unit layout, memorial, machine schematic, or other materially informative visual appears during close reading, it must be inspected visually and logged with its EPUB locator rather than inferred from image naming conventions.

## 6. Supplemental web-SS archive

The Dengeki/Novecomi+ archive is independently validated and is accepted as a source package:

- **27/27 stories retrieved successfully**; 0 failures.
- **33,246 normalized Japanese prose characters**.
- Source-index order and canonical URLs match one-to-one.
- Five stories distributed across publisher categories were checked raw-versus-normalized at opening, middle and ending; all passed.
- SHA-256 validation passed for the archive manifest.
- Category distribution: 9 anniversary `貴族if`; 4 comic bonus SS; 1 China signing-event SS; 7 Taiwan signing-event SS; 2 Thailand signing-event SS; 3 overseas-fair SS; 1 `Alters` story.
- The nine explicit `貴族if` entries are `AUTHOR_COUNTERFACTUAL_IF`.
- The remaining 18 remain `UNCLASSIFIED` until story-level continuity placement; they are **not** automatically promoted to mainline canon by the retrieval process.

### Web-SS identifiers

- `86-dengeki-ss-001` — エイティシックス8.6周年記念SS　貴族if1 — １：8.6周年記念SS — `AUTHOR_COUNTERFACTUAL_IF`
- `86-dengeki-ss-002` — エイティシックス8.6周年記念SS　貴族if2 — １：8.6周年記念SS — `AUTHOR_COUNTERFACTUAL_IF`
- `86-dengeki-ss-003` — エイティシックス8.6周年記念SS　貴族if3 — １：8.6周年記念SS — `AUTHOR_COUNTERFACTUAL_IF`
- `86-dengeki-ss-004` — エイティシックス8.6周年記念SS　貴族if4 — １：8.6周年記念SS — `AUTHOR_COUNTERFACTUAL_IF`
- `86-dengeki-ss-005` — エイティシックス8.6周年記念SS　貴族if5 — １：8.6周年記念SS — `AUTHOR_COUNTERFACTUAL_IF`
- `86-dengeki-ss-006` — エイティシックス8.6周年記念SS　貴族if6 — １：8.6周年記念SS — `AUTHOR_COUNTERFACTUAL_IF`
- `86-dengeki-ss-007` — エイティシックス8.6周年記念SS　貴族if7 — １：8.6周年記念SS — `AUTHOR_COUNTERFACTUAL_IF`
- `86-dengeki-ss-008` — エイティシックス8.6周年記念SS　貴族if8 — １：8.6周年記念SS — `AUTHOR_COUNTERFACTUAL_IF`
- `86-dengeki-ss-009` — エイティシックス8.6周年記念SS　貴族if8.6 — １：8.6周年記念SS — `AUTHOR_COUNTERFACTUAL_IF`
- `86-dengeki-ss-010` — 無名戦士は墓も無きゆえ — ２：コミックス用書き下ろしSS — `UNCLASSIFIED`
- `86-dengeki-ss-011` — ある初夏の日 — ２：コミックス用書き下ろしSS — `UNCLASSIFIED`
- `86-dengeki-ss-012` — 花火の夢 — ２：コミックス用書き下ろしSS — `UNCLASSIFIED`
- `86-dengeki-ss-013` — 君のことを — ２：コミックス用書き下ろしSS — `UNCLASSIFIED`
- `86-dengeki-ss-014` — CICF×AGF — ３：2023年 中国サイン会のお礼SS — `UNCLASSIFIED`
- `86-dengeki-ss-015` — シェア・シンとレーナ — ４：2024年 台湾サイン会のお礼SS — `UNCLASSIFIED`
- `86-dengeki-ss-016` — シェア・ユートとチトリ — ４：2024年 台湾サイン会のお礼SS — `UNCLASSIFIED`
- `86-dengeki-ss-017` — シェア・アンジュとダスティン — ４：2024年 台湾サイン会のお礼SS — `UNCLASSIFIED`
- `86-dengeki-ss-018` — シェア・ライデンとクレナとフレデリカ — ４：2024年 台湾サイン会のお礼SS — `UNCLASSIFIED`
- `86-dengeki-ss-019` — シェア・セオとアネット — ４：2024年 台湾サイン会のお礼SS — `UNCLASSIFIED`
- `86-dengeki-ss-020` — シェア・おまけのマルセル — ４：2024年 台湾サイン会のお礼SS — `UNCLASSIFIED`
- `86-dengeki-ss-021` — シェア・おまけのおまけのシデン — ４：2024年 台湾サイン会のお礼SS — `UNCLASSIFIED`
- `86-dengeki-ss-022` — ジャスミン — ５：2025年 タイサイン会のお礼SS — `UNCLASSIFIED`
- `86-dengeki-ss-023` — 花冠と三つ編み — ５：2025年 タイサイン会のお礼SS — `UNCLASSIFIED`
- `86-dengeki-ss-024` — 彼女の戦争 — ６：海外フェア用書き下ろしSS — `UNCLASSIFIED`
- `86-dengeki-ss-025` — 学園の女王陛下 — ６：海外フェア用書き下ろしSS — `UNCLASSIFIED`
- `86-dengeki-ss-026` — 鮮血女王と死神と仔豚 — ６：海外フェア用書き下ろしSS — `UNCLASSIFIED`
- `86-dengeki-ss-027` — 〈レギオン〉は夢を見ない、が — ７：Alters — `UNCLASSIFIED`

## 7. Alter collections

### Alter.1 — `―死神ときどき青春―`

`Alter.1` passes ZIP/package/spine/image/language checks and contains a large Japanese supplemental prose corpus organized across Republic, Federacy, United Kingdom, and `死神ときどき青春` sections. Its function in V2 is primarily **ordinary-life, relationship, voice, developmental, and between-crisis characterization**. Individual stories must be assigned a chronological window before they update longitudinal ledgers.

### Alter.2 — `魔法少女レジーナ☆レーナ…`

`Alter.2` also passes technical integrity checks, but its evidentiary status is deliberately segregated as **author-written AU/counterfactual prose**. It may test trait stability under altered circumstances; it cannot establish mainline history, chronology, or literal beliefs without corroboration in mainline sources.

## 8. Legacy transcript status

The uploaded prior-chat transcript is retained as `LEGACY_HYPOTHESIS_BANK_ONLY`. It contains the earlier volume-by-volume readings and later synthesis work, including material extending through V14, but Phase 0 does not assume those conclusions are correct. Every reusable claim must be independently re-earned from the locked primary corpus.

The transcript export metadata itself contains two archival warnings: the exporter reports that the bottom of the scroll region was **not reached or unconfirmed**, and that the first conversation message was **not confirmed**. Attachments are also not embedded. This does not prevent Phase 1 from mining the transcript for hypotheses, but it prevents treating the transcript as an independently complete evidentiary archive.

## 9. Source-lock rules for later phases

1. A synthesis claim must ultimately terminate in an admissible primary-source locator, not the legacy transcript.
2. V14 is fully admissible Japanese-primary evidence under the same locator and quotation-verification rules as V1–13.
3. Counterfactual material must carry an explicit AU/IF label every time it is used.
4. Web SS remain continuity-unclassified until their temporal and contextual fit is established.
5. Later translation comparisons may use translations as secondary evidence, never to silently replace Japanese wording.
6. EPUB page numbers must not be invented. Use volume + chapter/section + internal spine/XHTML locator + short Japanese anchor.
7. Illustration-derived claims require visual inspection of the actual embedded image.
8. Packaging defects are not textual defects unless they produce missing/unreadable content.
9. If a source is replaced, its new SHA-256 must be recorded and this lock manifest version incremented.

## 10. Phase 0 completion gate

### Passed — final source lock

- V1–14: ZIP/package/spine/language verification completed.
- V1–13: hashes remain consistent with the original rename manifest; V14 is a post-audit replacement with its own newly locked SHA-256.
- V1–14: chapter/structural inventory established.
- V1–14: illustration payload inventoried; image-reference and decode checks passed.
- Alter.1 and Alter.2: technical integrity, language and structure verified.
- Dengeki web-SS archive: 27/27 validation accepted.
- Supplemental/counterfactual evidence classes established.
- Legacy transcript assigned non-authoritative role.
- Publication-order skeleton established.
- Rejected Chinese-dominant V14 removed from active local/Drive source locations; its hash retained only in rejection history.

**Phase 0 is complete.** The V2 project now has a fully locked Japanese V1–14 mainline corpus and may proceed into Phase 1 and, subsequently, the sequential Phase 2 reread without a source-availability blocker.

## Phase 0 revision note — Volume 14 replacement

Replacement file: `86 - Volume 14 [Japanese].epub`  
Locked SHA-256: `0530e6d0ad217fe1b74f6802be32b842a0facc81e5418cd0e8826a510fa54aaa`  
Byte size: `8,069,921`  
Drive file ID: `1L0UTKXvRmB3vil7GxLd1AP-VzkD2L7wG`

The prior rejected V14 checksum was `93dd8fd85dd4753c398268402d1fc0f067a6d9c3385780981492b7bc61572e66`. The replacement is a distinct payload with genuinely Japanese narrative text.

## 11. Machine-readable companion

The companion file `86_SOURCE_LOCK_MANIFEST.json` records hashes, byte sizes, metadata, language heuristics, spine counts, image counts, warnings, evidence status, and structural entries for automated QA and later archival packaging.
