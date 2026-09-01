---
corpus: NANA_JP_DEEP_READING
artifact_type: retrieval_index
artifact: 16_JAPANESE_PASSAGE_LEXICAL_MOTIF_AND_SOURCE_INDEX
phase: 7
status: canonical_phase7_retrieval_index
scope: "Japanese Volumes 1-21 + translation-bounded Chapters 81-84 + NANA 7.8 paratext cross-index"
source_priority: "original Japanese manga > verified sequential deep readings/evidence ledgers > translated continuation for event/visual evidence only > direct Yazawa commentary > official editorial paratext"
primary_router: 15_VOLUME_BY_VOLUME_EVIDENCE_LEDGER.md
language_boundary: "No original-Japanese micro-linguistic claims are made from Chapters 81-84, whose surviving working corpus is fan-translated English/Spanish."
generated: "2026-08-14"
---

# 16 — Japanese Passage, Lexical, Motif, and Source Index
## Retrieval layer for the definitive *NANA* V2 analytical corpus

This document is the corpus's **retrieval layer**. It does not add a new master interpretation. Its job is to make mature claims auditable without reopening twenty-one volume analyses, the continuation file, and every specialist synthesis by hand.

The governing route is:

```text
synthesis document
→ NANA_VXX_DEEP_READING.md
→ NANA_VXX_E###
→ chapter / sequence
→ verified EPUB spine page
→ original Japanese page image
```

Where a printed page number was independently visible and verified, it is included. Where it was not, this index does **not** infer one from spine order. In those cases the verified EPUB spine page is itself the stable pointer to the Japanese page image.

For Chapters 81–84, the route stops at the mixed fan-translation archive locator. Those chapters remain valid for event, relationship, chronology, and visual-form claims but **not** for original-Japanese pronoun, honorific, register, sentence-ending, or exact lexical-recursion claims.

For *NANA 7.8*, this index distinguishes direct Yazawa commentary from editorial framing, cultural-reference material, reader reception, and metatext.

# 1. How to read the route notation
A compact route such as `D04 → V03 → NANA_V03_E002 → Ch.5 → spine 50` means: begin with the Nana/Hachi synthesis, descend to the Volume 3 deep reading, open evidence entry `NANA_V03_E002`, then verify the original Japanese page at EPUB spine 50. The evidence entry owns the classification and confidence; this document owns only retrieval.

Three rules govern this index:

1. **No locator invention.** A missing printed page remains missing.
2. **No lexical inference from translation.** Chapters 81–84 are segregated.
3. **No paratext override.** The manga establishes; Yazawa comments; official paratext frames; interpretation connects.

# 2. Synthesis-document directory

| Code | Canonical artifact | Primary analytical home |
|---|---|---|
| `D01` | `01_SERIES_ARCHITECTURE_CHRONOLOGY_AND_VOLUME_PROGRESSION.md` | chronology, structural progression, causal architecture |
| `D02` | `02_OSAKI_NANA_CHARACTER_SELFHOOD_LOVE_ART_AND_DEPENDENCY.md` | Osaki Nana |
| `D03` | `03_KOMATSU_NANA_HACHI_CHARACTER_DESIRE_HOME_MOTHERHOOD_AND_ADULTHOOD.md` | Hachi |
| `D04` | `04_NANA_HACHI_RELATIONSHIP_INTIMACY_CHOSEN_FAMILY_AND_QUEER_AMBIGUITY.md` | Nana/Hachi |
| `D05` | `05_RELATIONAL_CONSTELLATIONS_AND_SECONDARY_CHARACTER_SYSTEM.md` | supporting cast / relational system |
| `D06` | `06_HOME_FAMILY_PREGNANCY_MOTHERHOOD_MONEY_WORK_AND_MATERIAL_ADULTHOOD.md` | home, money, pregnancy, work, material adulthood |
| `D07` | `07_LOVE_SEX_CONSENT_COERCION_CARE_POSSESSION_AND_AUTONOMY.md` | ethics, consent, coercion, care, possession |
| `D08` | `08_MUSIC_CELEBRITY_BLAST_TRAPNEST_MEDIA_FANDOM_AND_PRIVACY.md` | music, celebrity, industry, media, fandom |
| `D09` | `09_NARRATION_MEMORY_TIME_ABSENCE_AND_THE_UNFINISHED_FUTURE.md` | future narration, memory, absence, unfinished future |
| `D10` | `10_JAPANESE_VOICE_ADDRESS_RELATIONAL_LANGUAGE_AND_LEXICAL_SYSTEM.md` | Japanese voice, address, lexical system |
| `D11` | `11_MANGA_FORM_SPACE_FASHION_BODY_OBJECT_AND_VISUAL_GRAMMAR.md` | manga form, bodies, objects, space, fashion |
| `D12` | `12_GENDER_SOCIAL_SCRIPTS_YOUTH_ADULTHOOD_AND_TURN_OF_THE_CENTURY_JAPAN.md` | gender / historical social scripts |
| `D13` | `13_NANA_7_8_PARATEXT_PUBLICATION_CONTEXT_AND_RETROSPECTIVE_REVISION.md` | official paratext / NANA 7.8 |
| `D14` | `14_COMPARATIVE_REFERENCE_MATRICES_AND_OPEN_QUESTIONS.md` | compression layer / open questions |
| `D15` | `15_VOLUME_BY_VOLUME_EVIDENCE_LEDGER.md` | frozen volume-by-volume evidence router |
| `D16` | `16_JAPANESE_PASSAGE_LEXICAL_MOTIF_AND_SOURCE_INDEX.md` | this retrieval index |

# 3. Primary-source and evidence-route directory

The table below is the quickest way to identify which sequential artifact owns a claim. Evidence counts are inherited from the frozen Document 15 audit.

| Vol. | Canonical deep reading | Japanese source | Source SHA-256 | Chapter scope | Stable evidence IDs |
|---:|---|---|---|---|---:|
| 01 | `NANA_V01_DEEP_READING.md` | `Nana - Volume 01 [Japanese].epub` | `6531ED30FAD08FFBC2910F33DE7F657B7978C09A32256165BD41A989E1597A4D` | two origin narratives; no numbered chapter labels invented for this ledger | 10 |
| 02 | `NANA_V02_DEEP_READING.md` | `Nana - Volume 02 [Japanese].epub` | `5EE62617D0FFE23094DF4455B6FDBDE1B829EB09F5D1E860D72D62204D6270C6` | 1–4; title pages verified at spine pp.7, 62, 109, 148 | 12 |
| 03 | `NANA_V03_DEEP_READING.md` | `Nana - Volume 03 [Japanese].epub` | `125294CD0155374764495E63341AFD91CC959DB3AD21EE0C90BC2A6DDAB0CE32` | 5–8; title pages verified at spine pp.7, 52, 99, 143 | 13 |
| 04 | `NANA_V04_DEEP_READING.md` | `Nana - Volume 04 [Japanese].epub` | `f2e9b71e5449f62ce2f215ee32e0d5f15440dcb35d2e7525be589a25f2b412f0` | 9-12 | 33 |
| 05 | `NANA_V05_DEEP_READING.md` | `Nana - Volume 05 [Japanese].epub` | `b076dca671f9787954c8dea846025e8dbd17b68dea4d94a673471d5272b146da` | 13-16 | 42 |
| 06 | `NANA_V06_DEEP_READING.md` | `Nana - Volume 06 [Japanese].epub` | `23133AC0D27A5E604EDAE9D62BA9F8922B0A10C48E91336278BC8ADCEB0A6AEA` | 17-20 | 60 |
| 07 | `NANA_V07_DEEP_READING.md` | `Nana - Volume 07 [Japanese].epub` | `5F70DC04BEFB110160B77B4B6A17C7CDAF576C5DEF426C5490C71C8A88CC3908` | 21-24 | 84 |
| 08 | `NANA_V08_DEEP_READING.md` | `Nana - Volume 08 [Japanese].epub` | `DD895F84788D224343B421776FE6EB93796165000483FC47DDBDB6692459D96C` | 25-28 | 95 |
| 09 | `NANA_V09_DEEP_READING.md` | `Nana - Volume 09 [Japanese].epub` | `7A7E22BBC010E4350DFE07E2914D54F0A4B803A1DA48D3CC3D032397047AD25C` | 29-32 + NAOKI [NANA 特別編] | 105 |
| 10 | `NANA_V10_DEEP_READING.md` | `Nana - Volume 10 [Japanese].epub` | `192AB8B22D04185EB2390366B37DEB606ECFB4A50818BBB904AD2E6B26EC0211` | 33-36 + おまけページ / 淳子の部屋 | 127 |
| 11 | `NANA_V11_DEEP_READING.md` | `Nana - Volume 11 [Japanese].epub` | `7323C8F77B843AF80331FE93360CD72C1DE202E1E7947829E6C95A008C6FE163` | 37-41 + おまけページ / 淳子の部屋 | 143 |
| 12 | `NANA_V12_DEEP_READING.md` | `Nana - Volume 12 [Japanese].epub` | `289246C377D16F1F866D4A68FA64B1A864EC3280E330A064E60C113DEEB4FBC3` | 42-45 + おまけページ | 163 |
| 13 | `NANA_V13_DEEP_READING.md` | `Nana - Volume 13 [Japanese].epub` | `7C12FFEDB5E4C34F96392FBC914FE343CC30934304D740E392F9F66633EF1926` | 46-49 + 淳子の部屋 | 210 |
| 14 | `NANA_V14_DEEP_READING.md` | `Nana - Volume 14 [Japanese].epub` | `61FF000A29A21E93B39FB0B758D758E43CAEB5D109A5DE2AD0710F72116A3294` | 50-53 + おまけページ | 151 |
| 15 | `NANA_V15_DEEP_READING.md` | `Nana - Volume 15 [Japanese].epub` | `62E94E7A0A582EABD68602AAC16A7BF133FA13CF1084306C64972A4B35D504A6` | 54-57 + おまけページ | 155 |
| 16 | `NANA_V16_DEEP_READING.md` | `Nana - Volume 16 [Japanese].epub` | `8AF53CF92B82157F624625E173E88951898CCA5BA0E131874A40ACAB7B6A34C2` | 58-61 + NOBU [NANA 特別編] + おまけページ / 淳子の部屋 | 159 |
| 17 | `NANA_V17_DEEP_READING.md` | `Nana - Volume 17 [Japanese].epub` | `1EB5CC05891734EA27EB900BDAF04BB8BAE8E447421AFD52A6EF3D0DF9E3BE2F` | 62-65 + おまけページ / 淳子の部屋 | 253 |
| 18 | `NANA_V18_DEEP_READING.md` | `Nana - Volume 18 [Japanese].epub` | `88E91B44155D3B8DD9FF71791E49E7B07D2C954CDFAA2B513EF64F77F48BC40D` | 66-69 + 淳子の部屋 + [TAKUMI] タクミ [NANA 特別編] | 364 |
| 19 | `NANA_V19_DEEP_READING.md` | `Nana - Volume 19 [Japanese].epub` | `E38B3E2A27D585B78AF1809FFC793E30E2E089D40EAA690D852D7457B1E57652` | 70-73 + 淳子の部屋 | 199 |
| 20 | `NANA_V20_DEEP_READING.md` | `Nana - Volume 20 [Japanese].epub` | `cef275ddb704fa806a3117ad9f08091262ee6c6458ed9ab28bcc25bdc272b56f` | 74-77 | 27 |
| 21 | `NANA_V21_DEEP_READING.md` | `Nana - Volume 21 [Japanese].epub` | `a085c40ce35538c097a852c3acac350ede83a67ee8873f62637eda1498b2d976` | 78-80 | 36 |
| 81–84 | `NANA_CH081_084_CONTINUATION_DEEP_READING.md` | mixed English/Spanish fan-translation archives | mixed translation provenance; see continuation artifact | Chapters 81–84 | continuation IDs `NANA_C81_E001`–`NANA_C84_E012` |

**Paratext:** `Nana 7.8 - Premium Fan Book [Japanese].pdf` is indexed through Document 13 and is not part of the primary-fiction freeze.

# 4. Major Japanese lexical and passage index

This is a **representative passage index**, not a concordance of every occurrence. Each entry identifies the phrase family most likely to be reused in later analysis, its primary interpretive home, and one or more verified source routes.

## 4.1 `生きる / 生きる為の手段` — living; living by one’s own choice; art as a means of living

**Primary home:** D02 / D08 / D09.  
**Use / caution:** Do not collapse survival, vocation, and happiness into one concept.

- `NANA_V01_E008` — `NANA_V01_DEEP_READING.md` — Osaki origin; spine 134 — 「おれ 東京行くから」／「おまえは おまえの好きに生きりゃいいさ」
- `NANA_V08_E006` — `NANA_V08_DEEP_READING.md` — 25; spine 21–22 — 大舞台・歓声・金 / 「歌はあたしの生きる為の手段」
- `NANA_V18_E011` — `NANA_V18_DEEP_READING.md` — Ch. 66; spine p.21 — もう1日生きてみよう

## 4.2 `決める` — to decide

**Primary home:** D02 / D07.  
**Use / caution:** A decision is strongest evidence of agency when the text shows who had the decision and what alternatives were materially available.

- `NANA_V01_E009` — `NANA_V01_DEEP_READING.md` — Osaki origin; spine 141 — 「ナナはレンの飼い猫じゃねぇぞ」／「それはナナが決める事だ」
- `NANA_V02_E007` — `NANA_V02_DEEP_READING.md` — Ch.2; spine 68 — 「ここにします♡」／「いや 決めた ここにする」

## 4.3 `所有物` — possession / owned thing

**Primary home:** D02 / D04 / D07.  
**Use / caution:** Nana explicitly recognizes that Ren and Hachi are not her possessions; recognition does not instantly eliminate possessive behavior.

- `NANA_V06_E020` — `NANA_V06_DEEP_READING.md` — 18; spine 76 — 「レンもハチ公も…あたしの所有物なわけじゃない」

## 4.4 `独り占め` — monopolize / keep entirely to oneself

**Primary home:** D04 / D07.  
**Use / caution:** Hachi distinguishes wanting to monopolize Nana from wanting to be needed; later text explicitly criticizes monopoly.

- `NANA_V07_E012` — `NANA_V07_DEEP_READING.md` — 21; spine 50 — 「独り占め…じゃない」「必要とされたかっただけ」
- `NANA_V20_E023` — `NANA_V20_DEEP_READING.md` — 77; spine 157 — 「他人を独り占め」

## 4.5 `必要 / 必要とされる` — need / to be needed

**Primary home:** D03 / D04 / D07.  
**Use / caution:** A central relational metric. Being needed is repeatedly confused with having a legitimate place beside someone.

- `NANA_V07_E012` — `NANA_V07_DEEP_READING.md` — 21; spine 50 — 「独り占め…じゃない」「必要とされたかっただけ」
- `NANA_V19_E035` — `NANA_V19_DEEP_READING.md` — Ch. 70; spine p.35 — 全てを犠牲にする必要はない

## 4.6 `繋ぐ / 繋がる` — connect; keep connected

**Primary home:** D04 / D07 / D10.  
**Use / caution:** Late relational vocabulary increasingly favors maintained connection over unbreakable binding.

- `NANA_V13_E147` — `NANA_V13_DEEP_READING.md` — 第48話; spine 144 — 「繋ぐものなんだよ」
- `NANA_V16_E049` — `NANA_V16_DEEP_READING.md` — Ch.59; spine 90 — もっとちゃんと繋がりたい
- `NANA_V17_E149` — `NANA_V17_DEEP_READING.md` — —; spine p.125 — 信頼で結ばれる

## 4.7 `信頼` — trust

**Primary home:** D05 / D07 / D10.  
**Use / caution:** Yasu’s mature relation-language treats trust as capable of binding persons without requiring a stronger formal label.

- `NANA_V17_E149` — `NANA_V17_DEEP_READING.md` — —; spine p.125 — 信頼で結ばれる

## 4.8 `依存 / 依存症` — dependence / dependency

**Primary home:** D02 / D07 / D10.  
**Use / caution:** The manga distinguishes chosen reliance from dependency severe enough to narrow agency; clinical language should not be generalized beyond the text.

- `NANA_V11_E121` — `NANA_V11_DEEP_READING.md` — 第41話; spine 219 — 精神的な依存症だって立派な中毒
- `NANA_V14_E086` — `NANA_V14_DEEP_READING.md` — Ch.52; spine spine p. 134 — 「もうおれに依存してちゃダメ」
- `NANA_V19_E115` — `NANA_V19_DEEP_READING.md` — Ch. 72; spine p.118 — そいつにすがらないと 生きて行く事も出来ない

## 4.9 `恋` — romantic love / being in love

**Primary home:** D04 / D10.  
**Use / caution:** The corpus uses 恋 directly around Nana/Hachi while also retaining qualifiers, analogy, and category ambiguity.

- `NANA_V03_E002` — `NANA_V03_DEEP_READING.md` — Ch.5; spine 50 — 「あたしのナナへの憧れは かなり恋に近いものだったと思います」
- `NANA_V03_E012` — `NANA_V03_DEEP_READING.md` — Ch.7; spine 140 — 「もしもナナが男だったら 一世一代の恋が出来るのに」
- `NANA_V09_E088` — `NANA_V09_DEEP_READING.md` — 32; spine 209 — 「誰に恋をしていても」「ヒーローはナナだけ」

## 4.10 `初恋` — first love

**Primary home:** D04 / D10.  
**Use / caution:** Hachi uses analogy (みたい); Nana is later described through a first-love-like boy comparison. Analogy is evidence of coding, not categorical closure.

- `NANA_V03_E003` — `NANA_V03_DEEP_READING.md` — Ch.5; spine 51 — 「とても幸福な初恋みたいだったよ」
- `NANA_V08_E012` — `NANA_V08_DEEP_READING.md` — 25; spine 33 — 「初めて恋を知った少年のように」

## 4.11 `恋人` — lover / romantic partner

**Primary home:** D04 / D10.  
**Use / caution:** Counterfactual relationship language matters because it makes the social category itself visible.

- `NANA_V07_E011` — `NANA_V07_DEEP_READING.md` — 21; spine 48 — 「たとえば あたし達が恋人同士なら」

## 4.12 `性欲` — sexual desire

**Primary home:** D04 / D10.  
**Use / caution:** Nana explicitly distinguishes her Nana/Hachi feeling from sexual desire as she understands it at that point. This is not a global declaration that sexuality is impossible.

- `NANA_V08_E013` — `NANA_V08_DEEP_READING.md` — 25; spine 34 — 「でも性欲ではない」

## 4.13 `愛してる` — I love you

**Primary home:** D05 / D07 / D10.  
**Use / caution:** Direct love-language is textually meaningful but cannot erase coercion, infidelity, or unequal power elsewhere in the relationship.

- `NANA_V13_E165` — `NANA_V13_DEEP_READING.md` — 第49話; spine 161 — 「愛してるって言ったの」

## 4.14 `愛情` — affection / love as care

**Primary home:** D06 / D07 / D10.  
**Use / caution:** The manga directly states that affection alone cannot raise a child; love is separated from material capacity.

- `NANA_V08_E080` — `NANA_V08_DEEP_READING.md` — 28; spine 175–177 — Nobu contraception/care guilt / explanation / 「愛情だけじゃ子供は育てられない」

## 4.15 `片想い` — unrequited love

**Primary home:** D04 / D10.  
**Use / caution:** Used by Hachi to name asymmetry without settling the final social category of the Nana/Hachi bond.

- `NANA_V13_E151` — `NANA_V13_DEEP_READING.md` — 第48話; spine 147 — 「なんだか やっぱり片想いだ」

## 4.16 `赤い糸` — red thread of fate

**Primary home:** D04 / D10 / D11.  
**Use / caution:** Fate imagery is culturally powerful but not an exclusive authorial stamp reserving one definitive couple.

- `NANA_V12_E128` — `NANA_V12_DEEP_READING.md` — 第44話; spine 141 — 「切れかけていた赤い糸」
- `NANA_V15_E106` — `NANA_V15_DEEP_READING.md` — Ch.57; spine 158 — 赤い糸だ

## 4.17 `運命` — fate

**Primary home:** D01 / D04 / D09 / D10.  
**Use / caution:** Future Hachi deploys fate language early; later characters also use it for other bonds. Treat as interpretive language, not automatic metaphysical fact.

- `NANA_V02_E001` — `NANA_V02_DEEP_READING.md` — Pre-Ch.1 future narration; spine 6 — 「これはやっぱり運命だと思う 笑ってもいいよ」
- `NANA_V12_E080` — `NANA_V12_DEEP_READING.md` — 第43話; spine 93 — 「ナナとレンは 結ばれなきゃ いけない運命なんだよ」
- `NANA_V12_E127` — `NANA_V12_DEEP_READING.md` — 第44話; spine 141 — 「それまで出会った誰より 運命を感じる相手だった」

## 4.18 `幸せ` — happiness

**Primary home:** D03 / D06 / D10.  
**Use / caution:** The series repeatedly separates wish fulfillment, romance, domesticity, and ordinary sustainable happiness.

- `NANA_V06_E013` — `NANA_V06_DEEP_READING.md` — 17; spine 50 — 「夢が叶う事と 幸せになる事は どうして別ものなんだろう」
- `NANA_V13_E017` — `NANA_V13_DEEP_READING.md` — 第46話; spine 46 — 「幸せのゴールなんてあるのかな」
- `NANA_V19_E131` — `NANA_V19_DEEP_READING.md` — Ch. 72; spine p.125 — フツーに幸せ

## 4.19 `夢` — dream

**Primary home:** D01 / D03 / D08 / D10.  
**Use / caution:** Dream fulfillment is repeatedly decoupled from happiness and from material sustainability.

- `NANA_V06_E004` — `NANA_V06_DEEP_READING.md` — 17; spine 18 — 「夢がひとつ叶う毎に 幸せになって行ける気がしてた」
- `NANA_V06_E013` — `NANA_V06_DEEP_READING.md` — 17; spine 50 — 「夢が叶う事と 幸せになる事は どうして別ものなんだろう」
- `NANA_V19_E193` — `NANA_V19_DEEP_READING.md` — Ch. 73; spine p.174 — 夢だけじゃ生きられない

## 4.20 `未来` — future

**Primary home:** D01 / D09 / D10.  
**Use / caution:** Early future language is prospective; after Ren’s death the old future becomes unusable rather than simply delayed.

- `NANA_V10_E047` — `NANA_V10_DEEP_READING.md` — 34; spine p090 / spine 91 — 「あたしが歌わなきゃ 未来がないじゃない」
- `NANA_V21_E029` — `NANA_V21_DEEP_READING.md` — 80; spine 148 — 「昨日までの設計図はもう使えない」
- `NANA_V21_E034` — `NANA_V21_DEEP_READING.md` — 80; spine 169 — 「未来は全て白紙になった」

## 4.21 `時間` — time

**Primary home:** D09 / D10.  
**Use / caution:** Subjective time can stop while chronological time continues; future narration records that mismatch.

- `NANA_V21_E016` — `NANA_V21_DEEP_READING.md` — 78; spine 82 — 「あたしの時間は止まった」

## 4.22 `白紙` — blank / blank page

**Primary home:** D09 / D10 / D11.  
**Use / caution:** The post-Ren future is not a liberating clean slate; it is a future whose previous design has become unusable.

- `NANA_V21_E034` — `NANA_V21_DEEP_READING.md` — 80; spine 169 — 「未来は全て白紙になった」
- `NANA_V21_E035` — `NANA_V21_DEEP_READING.md` — 80; spine 173 — 「今もそこに何も描けずにいるの」

## 4.23 `故郷` — hometown / native home

**Primary home:** D02 / D06 / D10.  
**Use / caution:** Nana denies having a hometown; later the work builds chosen return-spaces without pretending origin history disappears.

- `NANA_V03_E004` — `NANA_V03_DEEP_READING.md` — Ch.6; spine 90 — 「あたしには故郷などない」
- `NANA_V20_E022` — `NANA_V20_DEEP_READING.md` — 77; spine 151-152 — 「帰れる故郷がない」

## 4.24 `家庭` — household / family home

**Primary home:** D03 / D06 / D12.  
**Use / caution:** Hachi’s desire for household life is explicit and self-authored, even where gendered material asymmetries remain.

- `NANA_V04_E027` — `NANA_V04_DEEP_READING.md` — Ch.12; spine 161 — 「にぎやかな家庭の雰囲気」
- `NANA_V10_E073` — `NANA_V10_DEEP_READING.md` — 35; spine p128 / spine 129 — 「あたしは自分の家庭を持ちたいの！」

## 4.25 `家族` — family

**Primary home:** D05 / D06 / D12.  
**Use / caution:** Legal, biological, chosen, band, and lived-family categories overlap without becoming equivalent.

- `NANA_V11_E098` — `NANA_V11_DEEP_READING.md` — 第41話; spine 207 — 家族
- `NANA_V17_E035` — `NANA_V17_DEEP_READING.md` — —; spine p.39 — ナナの為にも 家族の為にも

## 4.26 `帰る` — return home

**Primary home:** D06 / D09 / D10.  
**Use / caution:** Return can mean physical residence, relational refuge, or re-entry into a chosen social world.

- `NANA_V13_E006` — `NANA_V13_DEEP_READING.md` — 第46話; spine 35 — 「出来るなら仕事を見つけて 707号室に帰りたい」
- `NANA_V13_E138` — `NANA_V13_DEEP_READING.md` — 第48話; spine 138 — 「今707号室に帰っても あたしはみんなの優しさに甘えちゃうだけだ」
- `NANA_V19_E141` — `NANA_V19_DEEP_READING.md` — Ch. 73; spine p.135 — 疲れたら帰りたいと思える場所

## 4.27 `戻る / 取り戻す` — return / restore / take back

**Primary home:** D04 / D07 / D09.  
**Use / caution:** The series increasingly questions whether a person or relationship can be “taken back” without erasing changed circumstances.

- `NANA_V11_E014` — `NANA_V11_DEEP_READING.md` — 第37話; spine 41–43 — ハチを取り戻す為に戦うわけじゃねえ
- `NANA_V13_E066` — `NANA_V13_DEEP_READING.md` — 第47話; spine 83 — 「707号室の鍵が またあたしの手の中に戻って来た」

## 4.28 `待つ` — wait

**Primary home:** D09 / D10.  
**Use / caution:** Waiting can preserve a receiving structure without guaranteeing reunion; it can also arrest the waiter’s future.

- `NANA_V12_E004` — `NANA_V12_DEEP_READING.md` — 第42話; spine 12 — 「707号室でみんなで待ってるよ」
- `NANA_V16_E001` — `NANA_V16_DEEP_READING.md` — Ch.58; spine 8 — ずっと待ってる

## 4.29 `探す` — search

**Primary home:** D08 / D09.  
**Use / caution:** Searching is ethically limited by privacy, publicity, practical feasibility, and fear that the absent person may not wish to be found.

- `NANA_V16_E009` — `NANA_V16_DEEP_READING.md` — Ch.58; spine 19 — ナナは見つかりませんでした
- `NANA_V17_E245` — `NANA_V17_DEEP_READING.md` — —; spine p.188 — 探すのをやめた今

## 4.30 `鍵` — key

**Primary home:** D06 / D09 / D11.  
**Use / caution:** 707 keys are material access before they are symbolic. Possession or absence of a key does not by itself settle emotional belonging.

- `NANA_V13_E061` — `NANA_V13_DEEP_READING.md` — 第47話; spine 79 — 「707号室の鍵がすぐにでも必要かもね」
- `NANA_V13_E066` — `NANA_V13_DEEP_READING.md` — 第47話; spine 83 — 「707号室の鍵が またあたしの手の中に戻って来た」
- `NANA_V17_E009` — `NANA_V17_DEEP_READING.md` — —; spine p.19 — 707号室の鍵は見つからなかった

## 4.31 `指輪` — ring

**Primary home:** D04 / D06 / D11.  
**Use / caution:** Rings can mark marriage, hope, continuity, public legibility, and attempted binding; meaning changes with wearer, hand, and time.

- `NANA_V12_E129` — `NANA_V12_DEEP_READING.md` — 第44話; spine 141 — 「お揃いの指輪が 繋ぎ止めてくれる気がした」

## 4.32 `ラブレター / 手紙` — love letter / letter

**Primary home:** D04 / D09 / D11.  
**Use / caution:** Written communication becomes a durable object that can outlast the state in which it was written.

- `NANA_V09_E093` — `NANA_V09_DEEP_READING.md` — 32; spine 216 — 「あんたがくれたラブレター」「今も大切に持ってる」
- `NANA_V13_E108` — `NANA_V13_DEEP_READING.md` — 第48話; spine 109 — 「タクミがいなければ ナナに手紙を書く事さえ きっと出来なかった」

## 4.33 `歌` — song / singing

**Primary home:** D02 / D08 / D10.  
**Use / caution:** Singing is emotion, vocation, work, public commodity, survival practice, and sometimes a field of coercion.

- `NANA_V01_E010` — `NANA_V01_DEEP_READING.md` — Osaki origin; spine 149 — 「ナナ！ おれのバンドで歌って！」／「溢れた想いが声になる」
- `NANA_V08_E006` — `NANA_V08_DEEP_READING.md` — 25; spine 21–22 — 大舞台・歓声・金 / 「歌はあたしの生きる為の手段」
- `NANA_V20_E015` — `NANA_V20_DEEP_READING.md` — 76; spine 123-124; printed 121-122 — 「唯一の戦いは 歌わない事」

## 4.34 `生きがい` — reason for living / life-purpose

**Primary home:** D05 / D08 / D10.  
**Use / caution:** Reira explicitly names singing as life-purpose; that strengthens the seriousness of her later refusal rather than authorizing institutional ownership.

- `NANA_V15_E060` — `NANA_V15_DEEP_READING.md` — Ch.56; spine 112 — 歌う事が生きがい

## 4.35 `仕事` — work

**Primary home:** D05 / D06 / D08 / D10.  
**Use / caution:** Work can be vocation, provider identity, grief compartment, schedule constraint, and source of authority.

- `NANA_V13_E019` — `NANA_V13_DEEP_READING.md` — 第46話; spine 47 — 「タクミは仕事最優先だから」
- `NANA_V13_E049` — `NANA_V13_DEEP_READING.md` — 第47話; spine 70 — 「タクミの信念は どこから仕事で どこまでが愛なんだろう」
- `NANA_V21_E019` — `NANA_V21_DEEP_READING.md` — 79; spine 108-110 — 「朝から仕事あるし」 / 「見送ってやれ」

## 4.36 `プロ` — professional

**Primary home:** D08 / D10.  
**Use / caution:** Professionalism in NANA is not the negation of artistic sincerity; it includes audience, market, discipline, and institutional obligation.

- `NANA_V16_E036` — `NANA_V16_DEEP_READING.md` — Ch.59; spine 74 — プロとしてはすっごいかっこいい

## 4.37 `商業的` — commercial / market-demanded

**Primary home:** D08 / D10.  
**Use / caution:** The text explicitly recognizes writing to commercial demand as a professional skill rather than automatically corrupt art.

- `NANA_V16_E035` — `NANA_V16_DEEP_READING.md` — Ch.59; spine 74 — 商業的に求められる曲が書けるなら
- `NANA_V16_E037` — `NANA_V16_DEEP_READING.md` — Ch.59; spine 74 — 自己満足の創作なら誰だって出来るよ

## 4.38 `発言権` — say / decision-making leverage

**Primary home:** D08 / D10.  
**Use / caution:** Nana’s mature commercial goal includes enough success to gain decision-making power over her own work.

- `NANA_V19_E100` — `NANA_V19_DEEP_READING.md` — Ch. 72; spine p.108 — それ位の発言権は持てるよね?

## 4.39 `プライバシー` — privacy

**Primary home:** D06 / D08 / D10 / D11.  
**Use / caution:** Privacy is both interpersonal boundary and celebrity infrastructure. Protection of privacy can itself become a rationale for control.

- `NANA_V02_E008` — `NANA_V02_DEEP_READING.md` — Ch.2; spine 71 — 「お互いのプライバシーは守れるし けど いざという時は助け合える」
- `NANA_V12_E084` — `NANA_V12_DEEP_READING.md` — 第43話; spine 95 — 「奈々と子供のプライバシーを守る為にも一切公表はしない」

## 4.40 `価値` — value / worth

**Primary home:** D02 / D05 / D08.  
**Use / caution:** Characters repeatedly risk equating worth with artistic output, usefulness, sexual desirability, or indispensability.

- `NANA_V09_E031` — `NANA_V09_DEEP_READING.md` — 30; spine 74 — 「歌っていないと 価値がない」

## 4.41 `始まらない` — cannot begin

**Primary home:** D04 / D09 / D10.  
**Use / caution:** Future Hachi’s statement centers Nana as restart condition without proving a final romantic category.

- `NANA_V21_E036` — `NANA_V21_DEEP_READING.md` — 80; spine 174 — 「ナナがいないと」「始まらないの」

# 5. Character retrieval index

Character entries route to their **primary analytical homes** and a small set of high-leverage evidence nodes. They are not substitutes for the full character documents.

| Character | Primary document(s) | High-value tags | Fast evidence routes |
|---|---|---|---|
| **大崎ナナ / Osaki Nana** | D02; D04; D08; D09; D11 | autonomy, abandonment, music, possession, body, celebrity, future absence | `NANA_V01_E009` (Osaki origin, spine 141); `NANA_V06_E020` (18, spine 76); `NANA_V08_E006` (25, spine 21–22); `NANA_V20_E023` (77, spine 157); `NANA_V21_E016` (78, spine 82) |
| **小松奈々 / Hachi** | D03; D04; D06; D09; D10 | home, romance scripts, motherhood, usefulness, mediation, future narration | `NANA_V03_E002` (Ch.5, spine 50); `NANA_V07_E012` (21, spine 50); `NANA_V10_E073` (35, spine p128 / spine 129); `NANA_V13_E138` (第48話, spine 138); `NANA_V21_E036` (80, spine 174) |
| **本城蓮 / Ren** | D05; D07; D08; D09 | fusion, music, addiction, plural duty, non-force, mortality | `NANA_V01_E008` (Osaki origin, spine 134); `NANA_V20_E013` (76, spine 88); `NANA_V21_E002` (78, spine 16); `NANA_V21_E025` (79, spine 120-121) |
| **一ノ瀬巧 / Takumi** | D05; D06; D07; D08 | competence, provider identity, control, work, coercion, family structure | `NANA_V06_E029` (18, spine 72); `NANA_V13_E019` (第46話, spine 47); `NANA_V13_E165` (第49話, spine 161) |
| **寺島伸夫 / Nobu** | D05; D07; D08 | ideal love, rescue fantasy, songwriting, restraint, lifelong friendship | `NANA_V06_E017` (18, spine 59); `NANA_V16_E150` (NOBU, spine 238) |
| **高木泰士 / Yasu** | D05; D07 | agency-restoring care, law/professionalism, paternalism, trust | `NANA_V01_E009` (Osaki origin, spine 141); `NANA_V17_E149` (—, spine p.125) |
| **芹澤レイラ / Reira** | D05; D07; D08 | voice, exceptional value, ordinary happiness, dependency, institutional use | `NANA_V15_E060` (Ch.56, spine 112); `NANA_V19_E131` (Ch. 72, spine p.125); `NANA_V20_E015` (76, spine 123-124, printed 121-122) |
| **岡崎真一 / Shin** | D05; D07; D12 | minority, performed adulthood, transactional sexuality, chosen family, accountability | `NANA_V07_E078` (24, spine 185–187); `NANA_V12_E146` (第45話, spine 175) |
| **早乙女淳子 / Junko** | D05 | counter-narration, ordinary friendship, blunt realism | `NANA_V03_E007` (Ch.7, spine 123, printed 120) |
| **高倉京助 / Kyosuke** | D05 | ordinary adult friendship, mediation, continuity |  |
| **遠藤章司 / Shoji** | D05; D07 | desire change, betrayal, apology, boundary failure | `NANA_V03_E008` (Ch.7, spine 131) |
| **川村幸子 / Sachiko** | D05; D07 | desire, attempted self-removal, complicity, ordinary relational ethics | `NANA_V03_E009` (Ch.7, spine 136); `NANA_V03_E010` (Ch.7, spine 137) |
| **篠田美雨 / Miu** | D05; D07 | solitude, anti-monopoly, care, self-harm, negotiated intimacy |  |
| **香坂百合 / Asami** | D05; D06 | public sexual persona, private name, labor, newer-partner legitimacy |  |
| **都築舞 / Mai / Misato** | D05; D08 | fan intimacy, alias, knowledge, labor, support | `NANA_V16_E046` (Ch.59, spine 84) |
| **藤枝直樹 / Naoki** | D05 | social permeability, comic normality, limited witness |  |

# 6. Relationship retrieval index

| Relationship / system | Primary home | Stable comparative description | Fast routes |
|---|---|---|---|
| **Nana / Hachi** | D04 primary; D03/D07/D09/D10/D11 supporting | friendship; chosen family; domestic partnership; queer/romantic coding; possession; need; future waiting | `NANA_V02_E007` (Ch.2, spine 68); `NANA_V03_E002` (Ch.5, spine 50); `NANA_V03_E012` (Ch.7, spine 140); `NANA_V07_E012` (21, spine 50); `NANA_V13_E147` (第48話, spine 144); `NANA_V21_E036` (80, spine 174) |
| **Nana / Ren** | D02/D05/D07 | explicit lovers; erotic/domestic intimacy; fusion fantasy; artistic separation; non-force; bereavement | `NANA_V01_E007` (Osaki origin, spine 131, printed 128); `NANA_V01_E008` (Osaki origin, spine 134); `NANA_V20_E013` (76, spine 88); `NANA_V21_E016` (78, spine 82) |
| **Hachi / Takumi** | D03/D06/D07 | marriage; affection; provider structure; sexual coercion; public status; unresolved future | `NANA_V06_E029` (18, spine 72); `NANA_V10_E074` (35, spine p128 / spine 129); `NANA_V13_E165` (第49話, spine 161) |
| **Hachi / Nobu** | D03/D05/D07 | genuine romance; rescue ideal; pregnancy/material limits; later restraint and consolation | `NANA_V06_E017` (18, spine 59); `NANA_V08_E080` (28, spine 175–177) |
| **Nana / Yasu** | D02/D05/D07 | deep trust, protection, quasi-familial dependence, agency restoration with paternalistic edges | `NANA_V01_E009` (Osaki origin, spine 141); `NANA_V17_E149` (—, spine p.125) |
| **Ren / Yasu** | D05 | friendship, mentorship, addiction concern, failed rescue, shared music history |  |
| **Reira / Takumi** | D05/D07/D08 | childhood recognition, artistic infrastructure, sanctuary fantasy, love/attachment asymmetry |  |
| **Shin / Reira** | D05/D07 | minor/adult asymmetry; money; desire; emotional attachment; adult responsibility | `NANA_V07_E078` (24, spine 185–187) |
| **Nobu / Asami** | D05/D06 | newer romantic bond, work/material reality, old-bond pressure, ordinary care |  |
| **Yasu / Miu** | D05/D07 | intimacy without monopoly; trust; private life beyond rescue role | `NANA_V17_E149` (—, spine p.125) |
| **Shoji / Sachiko** | D05/D07 | desire change, dishonesty, attempted boundaries, affair, later closure | `NANA_V03_E007` (Ch.7, spine 123, printed 120); `NANA_V03_E009` (Ch.7, spine 136); `NANA_V03_E010` (Ch.7, spine 137) |
| **Hachi / Shin** | D03/D05/D06 | chosen family; surrogate-maternal care; domestic inclusion | `NANA_V12_E146` (第45話, spine 175) |
| **BLAST as relational unit** | D05/D08 | band, work institution, chosen family, career vehicle, grief network | `NANA_V01_E010` (Osaki origin, spine 149) |
| **Trapnest as relational unit** | D05/D08 | professional institution, artistic history, work/family entanglement, Reira-dependence | `NANA_V15_E060` (Ch.56, spine 112) |

# 7. Object, space, and visual-motif index

The formal rule is that objects in *NANA* do not carry immutable symbolic definitions. Meaning depends on **material function + body + observer + access + historical accumulation**. The entries below therefore route recurring objects to the moments where their function changes.

| Object / motif | Primary home | Longitudinal function | Fast routes |
|---|---|---|---|
| **Apartment 707** | D06/D09/D11 | shared home → contested household → archive → ritual home → receiving address | `NANA_V02_E007` (Ch.2, spine 68); `NANA_V02_E008` (Ch.2, spine 71); `NANA_V17_E003` (—, spine p.12) |
| **707 key** | D06/D09/D11 | material access and possible return; not automatic restoration | `NANA_V13_E061` (第47話, spine 79); `NANA_V13_E066` (第47話, spine 83); `NANA_V17_E009` (—, spine p.19) |
| **strawberry glasses / いちごのグラス** | D04/D11 | cheap ordinary objects that become durable relationship-memory carriers | `NANA_V09_E026` (29, spine 64); `NANA_V16_E018` (Ch.58, spine 59) |
| **rings / matching rings** | D04/D06/D11 | marriage, hope, binding, public legibility, grief; hand placement matters | `NANA_V12_E129` (第44話, spine 141) |
| **joined hands / offered hands** | D04/D11 | connection as embodied action; later increasingly refusable rather than binding | `NANA_V12_E039` (第42話, spine 52); `NANA_V17_E120` (—, spine p.100-102); `NANA_V21_E031` (80, spine 155) |
| **collar / pet imagery** | D02/D04/D07/D11 | possession, domestication, dependency, self-aware desire to bind | `NANA_V01_E009` (Osaki origin, spine 141); `NANA_V08_E065` (27, spine 148–149) |
| **table / chairs / window** | D06/D09/D11 | ordinary domestic infrastructure becomes remembered home and performance apparatus | `NANA_V02_E012` (Ch.4, spine 188); `NANA_V03_E005` (Ch.6, spine 95) |
| **mobile phone / mediated contact** | D08/D09/D11 | access, delay, unreachable partners, public/private boundary, long-distance relation | `NANA_V03_E013` (Ch.8, spine 144) |
| **letters / love letters** | D04/D09/D11 | communication becomes archive; can outlast original relational state | `NANA_V09_E093` (32, spine 216); `NANA_V13_E108` (第48話, spine 109) |
| **photographs** | D08/D09/D11 | fragmentary evidence, celebrity image, leverage, survival corroboration, incomplete provenance | `NANA_V17_E018` (—, spine p.23-25) |
| **food / cooking** | D03/D06/D11 | care labor, household practice, grief infrastructure, ordinary reciprocity | `NANA_V07_E019` (22, spine 69) |
| **guitar** | D05/D08/D11 | vocation, memory, companionship, ordinary music outside spectacle | `NANA_V18_E012` (Ch. 66, spine p.22) |
| **rain** | D09/D11 | weather as temporal/affective overlay; never a fixed one-word symbol | `NANA_V13_E208` (第49話, spine 189) |
| **snow** | D09/D11 | accumulating temporal field; pursuit/death geography in V21 | `NANA_V17_E178` (—, spine p.146); `NANA_V21_E002` (78, spine 16) |
| **sea** | D09/D11 | future address, death-site thought, grief ritual, possible geography | `NANA_V14_E060` (Ch.51, spine spine p. 95); `NANA_V16_E013` (Ch.58, spine 21); `NANA_V18_E008` (Ch. 66, spine p.20) |
| **fireworks** | D09/D11 | ritual recurrence, brilliant brevity, waiting, remembered communal time | `NANA_V16_E003` (Ch.58, spine 13) |
| **birthday gift** | D09/D11 | delayed communication from Ren; Hachi vows to deliver the feeling to Nana | `NANA_V21_E032` (80, spine 159-162) |
| **stage / crowd / screen** | D08/D11 | amplification and distance: public visibility increases while ordinary access shrinks | `NANA_V08_E005` (25, spine 21–22) |

# 8. Future-narration and absence index

Future narration is organized as an epistemic ladder rather than an omniscient summary. The following nodes are the shortest route through that ladder.

| Temporal node | Primary home | Evidence routes |
|---|---|---|
| Fate framing before shared life hardens into memory | D09 | `NANA_V02_E001` (Pre-Ch.1 future narration, spine 6) |
| Early river/melody scene remembered from the future | D09 | `NANA_V02_E006` (Ch.1, spine 61) |
| Furniture preserved as evidence of former home | D09/D11 | `NANA_V03_E005` (Ch.6, spine 95) |
| 707 waiting ritual | D09 | `NANA_V12_E004` (第42話, spine 12); `NANA_V12_E043` (第42話, spine 55) |
| Future Nana directly addresses Hachi | D09/D10 | `NANA_V16_E012` (Ch.58, spine 21); `NANA_V16_E013` (Ch.58, spine 21) |
| Search reports Nana not found | D09 | `NANA_V16_E009` (Ch.58, spine 19) |
| Loneliness returns despite attempted domestication | D09 | `NANA_V16_E014` (Ch.58, spine 22); `NANA_V16_E015` (Ch.58, spine 22) |
| Future 707 remains empty and key absent | D09/D11 | `NANA_V17_E003` (—, spine p.12); `NANA_V17_E009` (—, spine p.19) |
| Hope that Nana has returned persists | D09 | `NANA_V17_E010` (—, spine p.19); `NANA_V17_E011` (—, spine p.20) |
| Nana survival inferred/affirmed within character search | D09 | `NANA_V17_E015` (—, spine p.22) |
| Future Nana chooses one more day of life | D09 | `NANA_V18_E011` (Ch. 66, spine p.21) |
| Ren’s death stops Nana’s subjective time | D09 | `NANA_V21_E016` (78, spine 82) |
| Survivor ethic: remain for those left behind | D07/D09 | `NANA_V21_E025` (79, spine 120-121) |
| Old future blueprint is unusable | D09 | `NANA_V21_E029` (80, spine 148) |
| Future becomes blank paper | D09 | `NANA_V21_E034` (80, spine 169); `NANA_V21_E035` (80, spine 173) |
| Hachi’s future cannot begin without Nana | D04/D09 | `NANA_V21_E036` (80, spine 174) |


## 8.1 What future narration establishes with high confidence

- Nana is absent from the 707 network in the depicted future.
- Hachi and the others continue waiting/searching structures around her.
- Future Nana is **alive** in the depicted future; early death inference is retrospectively corrected.
- Hachi remains intensely oriented toward Nana.
- Nana remains intensely oriented toward Hachi.
- Ren's death changes the temporal architecture from a shared imagined future to unusable blueprint / blank page.

## 8.2 What future narration does not establish

- the complete cause of Nana's disappearance;
- the exact bridge from Chapter 84 to future absence;
- whether Britain is definitively her location;
- whether Hachi caused the disappearance;
- whether Nana ultimately returns;
- the final legal/romantic state of Hachi/Takumi;
- the final social category of Nana/Hachi.

The governing distinction is: **retrospective interpretation is authoritative evidence of later self-understanding, not automatic omniscient causality.**

# 9. Ethical-question index

| Question | Primary home | Mature answer / boundary | Fast routes |
|---|---|---|---|
| **Who gets to decide?** | D07 | Agency is strongest where care returns decision space rather than using competence to preempt it. | `NANA_V01_E009` (Osaki origin, spine 141); `NANA_V20_E013` (76, spine 88) |
| **When does care become jurisdiction?** | D07 | Provision, protection, expertise, and love become ethically dangerous when treated as authority over another person. | `NANA_V06_E029` (18, spine 72) |
| **Can later love retroactively establish prior consent?** | D07 | No. Consent remains encounter-specific; later marriage/affection does not rewrite an earlier non-consensual act. |  |
| **Does dependence negate autonomy?** | D07 | No. The mature alternative is chosen interdependence with refusal intact. | `NANA_V17_E149` (—, spine p.125) |
| **Is possession proof of devotion?** | D07 | The series increasingly distinguishes commitment from monopoly. | `NANA_V06_E020` (18, spine 76); `NANA_V20_E023` (77, spine 157) |
| **Does sacrifice prove love?** | D07/D09 | Late corpus explicitly resists total-sacrifice logic. | `NANA_V19_E035` (Ch. 70, spine p.35); `NANA_V21_E025` (79, spine 120-121) |
| **Can a rescuer remain without reclaiming?** | D05/D07 | Nobu’s maturation and post-Ren presence make accompaniment without possession a major late ethic. |  |
| **Does a minor’s sophistication create adult responsibility?** | D07/D12 | No. Shin’s adult-coded performance does not erase adult responsibility around him. |  |
| **Can privacy be protected without enclosure?** | D07/D08 | Security, media strategy, and household control can protect and constrain simultaneously. | `NANA_V12_E084` (第43話, spine 95) |
| **Can an institution own output it depends on?** | D07/D08 | Reira’s refusal to sing answers no: institutional dependence is not ownership. | `NANA_V20_E015` (76, spine 123-124, printed 121-122) |
| **Can one person be sufficient for another’s entire life?** | D05/D07 | The mature ensemble increasingly answers no; distributed care is more durable than single-savior logic. | `NANA_V19_E115` (Ch. 72, spine p.118) |
| **Can belonging survive reduced necessity?** | D03/D04/D14 | The extant endpoint leaves this as the central Nana/Hachi question. |  |

# 10. Music, industry, media, and fandom index

| Concept | Primary home | Stable use | Fast routes |
|---|---|---|---|
| **歌 / song** | D08 | music as private expression, vocation, livelihood, product, memory, and connection | `NANA_V01_E010` (Osaki origin, spine 149); `NANA_V08_E006` (25, spine 21–22) |
| **生きがい / life-purpose** | D08 | Reira’s vocation makes professional exploitation more complex, not less real | `NANA_V15_E060` (Ch.56, spine 112) |
| **商業的 / commercially demanded** | D08 | commercial competence can be genuine artistic professionalism | `NANA_V16_E035` (Ch.59, spine 74); `NANA_V16_E036` (Ch.59, spine 74) |
| **発言権 / decision-making leverage** | D08 | success sought partly to obtain agency over one’s own work | `NANA_V19_E100` (Ch. 72, spine p.108) |
| **visibility vs access** | D08/D11 | public image multiplies while ordinary mobility/privacy shrink | `NANA_V08_E005` (25, spine 21–22) |
| **photograph as fragment** | D08/D11 | true image can be decontextualized into misleading total narrative | `NANA_V17_E018` (—, spine p.23-25) |
| **privacy as infrastructure** | D06/D08 | housing, security, schedules, media strategy, and phones structure who can reach whom | `NANA_V12_E084` (第43話, spine 95) |
| **fan knowledge vs relationship** | D08 | knowledge and protective intent do not automatically create relational entitlement |  |
| **professionalization of BLAST** | D08 | the manga rejects a clean authentic-BLAST / manufactured-Trapnest binary | `NANA_V16_E036` (Ch.59, spine 74) |
| **refusal to perform** | D08 | withholding output becomes available resistance when voice has become institutional infrastructure | `NANA_V20_E015` (76, spine 123-124, printed 121-122) |

# 11. Mature synthesis-claim router

This table allows later comparative work to begin from a mature proposition and descend to primary evidence. Confidence here refers to the **claim level**, not the individual evidence-class code owned by the volume artifact.

| Claim | Primary home | Mature formulation | Confidence | Fast routes |
|---|---|---|---|---|
| **Dual-protagonist architecture** | D01/D13 | The two Nanas are structurally co-central; NANA 7.8 confirms the paired conception early in serialization. | A/B | `NANA_V02_E003` (Ch.1, spine 33) |
| **707 as bounded intimacy** | D06/D11 | 707 succeeds because it combines privacy, separate rooms, shared cost, aid, and elective access. | A/B | `NANA_V02_E007` (Ch.2, spine 68); `NANA_V02_E008` (Ch.2, spine 71) |
| **Nana autonomy is explicit, not merely aesthetic** | D02 | Ren and Yasu directly preserve Nana’s formal decision authority. | A | `NANA_V01_E008` (Osaki origin, spine 134); `NANA_V01_E009` (Osaki origin, spine 141) |
| **Hachi domesticity is genuine vocation** | D03/D06 | Hachi repeatedly authors household/family desire; its vulnerability lies in usefulness becoming worth. | B | `NANA_V10_E073` (35, spine p128 / spine 129); `NANA_V10_E074` (35, spine p128 / spine 129) |
| **Takumi care and coercion coexist** | D05/D07 | Material provision and genuine affection do not erase sexual coercion or jurisdictional control. | B | `NANA_V06_E029` (18, spine 72); `NANA_V13_E165` (第49話, spine 161) |
| **Nobu matures toward accompaniment** | D05/D07 | Romantic rescue becomes restraint and presence without automatic reclamation. | B | `NANA_V06_E017` (18, spine 59) |
| **Yasu is strongest recurring agency-restoring caregiver** | D05/D07 | Trust and decision-space define his strongest care, though paternalistic edges remain. | B | `NANA_V17_E149` (—, spine p.125) |
| **Reira’s voice is vocation, not merely commodity** | D05/D08 | Singing is her 生きがい; later refusal is therefore an assertion of personhood, not simple dislike of work. | A/B | `NANA_V15_E060` (Ch.56, spine 112); `NANA_V20_E015` (76, spine 123-124, printed 121-122) |
| **Celebrity increases visibility while reducing ordinary freedom** | D08/D11 | Public image expands beyond the person while privacy/mobility contract. | B | `NANA_V12_E084` (第43話, spine 95) |
| **Future narration is witness, not omniscience** | D09 | Later regret and interpretation reveal later consciousness without proving complete causality. | B | `NANA_V02_E004` (Ch.1, spine 35) |
| **Future Nana is alive** | D09 | The depicted future directly overturns the earlier death inference. | A | `NANA_V16_E007` (Ch.58, spine 17) |
| **Nana’s absence cause remains unresolved** | D09/D14 | Absence is established; full cause, duration, and final outcome are not. | D |  |
| **Ren’s death rejects death-together as resolution** | D07/D09 | The death produces asymmetrical survival and an ethic of remaining for the living. | B | `NANA_V21_E025` (79, spine 120-121) |
| **Nana/Hachi structural romance** | D04 | The bond is structurally romantic, explicitly queer-coded, domestically/familially real, categorically unfinished. | B | `NANA_V03_E002` (Ch.5, spine 50); `NANA_V03_E012` (Ch.7, spine 140); `NANA_V07_E011` (21, spine 48) |
| **Possession is not connection** | D04/D07 | The late corpus increasingly shifts from ownership/monopoly toward trust and maintained connection. | B | `NANA_V06_E020` (18, spine 76); `NANA_V13_E147` (第48話, spine 144); `NANA_V17_E149` (—, spine p.125) |
| **Material adulthood changes feasible choices** | D06 | Pregnancy, money, work, housing, law, privacy, and transport constrain choices without dictating desire. | B | `NANA_V08_E080` (28, spine 175–177) |
| **Gender roles are neither pure liberation nor pure submission** | D12 | Roles can be desired, useful, unequal, and revisable at the same time. | B | `NANA_V10_E073` (35, spine p128 / spine 129) |
| **Objects are historical, not dictionary symbols** | D11 | Meaning changes through body, observer, access, location, and accumulated use. | B | `NANA_V13_E066` (第47話, spine 83); `NANA_V17_E009` (—, spine p.19) |
| **Late corpus favors maintenance over heroic solution** | D03/D05/D06/D07 | Food, waiting, work, letters, care, rehearsal, and ordinary presence repeatedly outperform fantasies of total rescue. | B | `NANA_V21_E025` (79, spine 120-121) |
| **Hiatus is an epistemic boundary** | D14 | Trajectory is legible; destination must not be invented. | A as corpus limit |  |


# 12. Chapters 81–84 continuation index — translation-bounded layer

The continuation corpus is narratively indispensable and linguistically restricted. The canonical continuation artifact is `NANA_CH081_084_CONTINUATION_DEEP_READING.md`.

| Evidence ID | Governing locator / event | Stable use | Language boundary |
|---|---|---|---|
| `NANA_C81_E002–E004` | Chapter 81 taxi/Shirokane sequence | Hachi wants Nana/everyone yet suppresses grief because she believes Takumi has no one | Event/character belief only; no Japanese register claim |
| `NANA_C82_E003` | Chapter 82 breakfast/cooking sequence | domestic labor becomes communal grief infrastructure | Visual/event evidence |
| `NANA_C82_E004–E005` | Chapter 82 Asami/Hachi tension | newer-partner insecurity has material and relational content | Translated wording only |
| `NANA_C83_E001` | Chapter 83 ring placement | Nana's ring placement changes after Ren's death | Visual fact |
| `NANA_C83_E002–E003` | Chapter 83 Hachi/Nobu embrace | physical consolation without automatic romance restoration | Event/form evidence |
| `NANA_C83_E004` | Chapter 83 Nobu guitar beside silent Nana | music becomes contact during shutdown | Event/form evidence |
| `NANA_C83_E005–E006` | Chapter 83 Hachi future-facing reflections | Hachi wants Nana's side; questions being Takumi's necessary refuge | Translation-mediated character belief |
| `NANA_C84_E001–E005` | Chapter 84 food, singing, Reira/Takumi | behavioral movement is not proof of psychological recovery | Mixed event/translation evidence |
| `NANA_C84_E006–E009` | Spanish-only printed pp.11–16 | Hachi refuses grief-driven drift to Nobu; marriage future remains unresolved; Reira/Takumi beliefs stay character-level | Spanish fan translation governs wording |
| `NANA_C84_E011–E012` | final printed page / black field | apparent Nana recovery reactivates whether Hachi is still needed beside her | Referent is clear in translations; exact Japanese wording unavailable |

The extant endpoint therefore supports the analytical question:

> **Can Hachi possess a place beside Nana that does not depend on Nana being broken enough to need rescuing?**

It does **not** supply the answer.


# 13. *NANA 7.8* paratext cross-index

The paratext layer is routed through Document 13. The active Japanese PDF has SHA-256 `f0184754d113350144b46ea3420af0a6b6d83c5f18825875bcd01b92dcdb3608`. The IDs below preserve source class so that direct Yazawa commentary is not silently merged with editorial copy.

| Paratext ID | Class | Locator | Reusable proposition |
|---|---|---|---|
| `NANA78-DF-001` | documentary fact | PDF p.200 | first printing 2003-03-19; fan book is an early-serialization object |
| `NANA78-YA-002` | Yazawa commentary | PDF p.117 / printed p.114 | paired same-name women / fate-conscious conception is early and deliberate |
| `NANA78-YA-003` | Yazawa commentary | PDF p.119 / printed p.116 | no simple one-to-one real-person character models |
| `NANA78-YA-004` | Yazawa commentary with editorial interview framing | PDF p.121 / printed p.118 | multi-perspectival reading is explicitly encouraged |
| `NANA78-YA-005` | Yazawa commentary | PDF p.123 / printed p.120 | future-looking-back form was conscious by 2003; character responses could still alter development |
| `NANA78-YA-006` | Yazawa commentary | PDF p.125 / printed p.122 | timing and contingency matter to process |
| `NANA78-CR-001` | cultural reference | PDF pp.106–113 | fictional geography becomes real-world fan pilgrimage |
| `NANA78-RC-001` | curated reader reception | PDF pp.132–145 | small early-reception snapshot; not population evidence |
| `NANA78-MT-001` | metatext | PDF pp.166–172 | simulated rock journalism demonstrates franchise/media mediation |

The paratext rule remains:

> **the manga establishes; Yazawa comments; the paratext frames; interpretation connects.**


# 14. Rapid Japanese concept lookup

This section is deliberately redundant with Section 4 in **function**, not in argument. It is an alphabetical lookup list for later searches.

- `愛 / 愛情 / 愛してる` → love, affection, direct declaration → D05/D07/D10
- `赤い糸` → fate-thread / attempted relational continuity → D04/D10/D11
- `依存` → dependency / narrowed autonomy → D02/D07/D10
- `運命` → fate as character/narrator framing → D01/D04/D09/D10
- `家族` → family as legal, biological, chosen, band, lived category → D05/D06/D12
- `家庭` → household / family home → D03/D06/D12
- `帰る` → return home / refuge / re-entry → D06/D09/D10
- `決める` → decision / authorship → D02/D07
- `故郷` → hometown / origin home → D02/D06/D10
- `幸せ` → happiness / sustainable life → D03/D06/D10
- `仕事` → work / provider identity / schedule / institutional duty → D05/D06/D08/D10
- `所有物` → possession → D02/D04/D07
- `性欲` → sexual desire → D04/D10
- `信頼` → trust → D05/D07/D10
- `生きがい` → life-purpose / vocation → D05/D08/D10
- `生きる` → live / survive / self-author life → D02/D08/D09
- `繋ぐ` → connect / maintain connection → D04/D07/D10
- `独り占め` → monopolize → D04/D07
- `必要` → need / being needed → D03/D04/D07
- `発言権` → decision-making leverage / say → D08/D10
- `片想い` → unrequited love → D04/D10
- `待つ` → wait / preserve receiving structure → D09/D10
- `未来` → future → D01/D09/D10
- `夢` → dream → D01/D03/D08/D10
- `恋 / 恋人 / 初恋` → romantic category and analogy → D04/D10


# 15. Open-question routing index

These questions are deliberately preserved as **open**. Future use of this corpus should route them to Document 14 rather than improvise answers from thematic momentum.

| Open question | Best retrieval path | Current status |
|---|---|---|
| Why exactly does Nana leave the 707 network? | D09 → V16–V21 future material → continuation | unresolved; likely multi-causal, but no complete causal bridge |
| When exactly does Nana leave? | D09 → V21 → Ch.81–84 → future scenes | unresolved |
| Does Nana know the group is still searching/waiting? | D09 | unresolved in complete form |
| Is Britain definitively Nana's location? | D09 → V17–V18 | inferential, not unique proof |
| Will Nana return to 707? | D09/D11 | prepared as possibility, not shown |
| What is Hachi/Takumi's final marital condition? | D03/D06/D07/D14 | unresolved beyond depicted family continuity |
| Is there a later Hachi/Nobu romantic restoration? | D03/D05/D07 | not established |
| What is the final Shin/Reira condition? | D05/D07 | unresolved |
| What is the final Reira/Takumi condition? | D05/D07/D08 | unresolved |
| What is the final social category of Nana/Hachi? | D04/D14 | structurally romantic and queer-coded; categorical endpoint unwritten |
| Can Hachi remain beside Nana without being needed as rescuer? | D03/D04/D14 + C84 | central extant-endpoint question; unanswered |
| Can Nana accept dependence without experiencing it as loss of self? | D02/D04/D09 | unresolved |


# 16. Integrity and reuse rules

1. **For exact Japanese wording, descend to the volume locator.** Specialist syntheses may paraphrase.
2. **For a mature interpretive claim, begin in its primary synthesis home.** Do not treat the index itself as the argument.
3. **For historical development of a claim, use Document 15.** It preserves when the interpretation was first available and how later volumes revised it.
4. **For unresolved questions, use Document 14.** Do not convert high thematic plausibility into canon fact.
5. **For Chapters 81–84, keep translation provenance visible.** No Japanese lexical claim may be back-constructed from English or Spanish.
6. **For *NANA 7.8*, preserve source class.** Direct author commentary and editorial/franchise metatext are not interchangeable.
7. **For visual motifs, follow function over dictionary symbolism.** A ring, key, photo, hand, room, or item of clothing changes meaning as its material and relational context changes.
8. **For consent and coercion, route encounter by encounter.** Later love, marriage, or continued relation cannot retroactively establish earlier consent.
9. **For future narration, distinguish fact, later interpretation, hope, fear, counterfactual regret, and apostrophic address.**
10. **For every claim that appears to exceed the cited route, reopen the source rather than extending the claim by analogy.**

This is the final retrieval principle of the V2 corpus:

> **A mature synthesis claim should be able to travel backward from interpretation to evidence without changing category on the way.**
