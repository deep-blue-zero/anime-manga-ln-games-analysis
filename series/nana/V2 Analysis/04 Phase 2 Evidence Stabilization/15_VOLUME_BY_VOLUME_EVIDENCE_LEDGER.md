---
corpus: NANA_JP_DEEP_READING
work: NANA
artifact: 15_VOLUME_BY_VOLUME_EVIDENCE_LEDGER
phase: 2
status: phase2_frozen_evidence_ledger
scope: "Volumes 1-21 + Chapters 81-84"
method: NANA_ANALYTICAL_METHOD_V2
architecture: NANA_MULTI_DOCUMENT_SYNTHESIS_ARCHITECTURE_V1
generated_from_canonical_artifacts: true
frozen: true
freeze_date: "2026-08-13"
sequential_primary_provenance_status: stabilized
---

# 15 — Volume-by-Volume Evidence Ledger
## Phase 2 evidence stabilization — frozen ledger

This document is the audit layer between the sequential close readings and the mature synthesis. It does **not** replace the volume artifacts. It records what each historical reading established, which evidence routes are mature enough to carry forward, which later volumes revise earlier interpretations, and where provenance remains incomplete. The governing rule is that later knowledge may revise the cumulative model without silently rewriting what an earlier spoiler-bounded artifact was entitled to conclude.

### Phase-2 frozen status

- Canonical sequential artifacts audited: **22** (Volumes 1–21 plus the combined Chapters 81–84 continuation).
- Volumes **1–3** now carry Phase-2 load-bearing evidence IDs and verified EPUB spine locators appended to their preserved legacy analyses. Their governing source hashes still match the integrity manifest.
- Volumes **4–19** retain their mature verified provenance/locator architecture.
- Volumes **20–21** contain verified evidence and locator ledgers; the absence of a `locator_status` YAML field is a metadata-normalization issue and is not a provenance blocker.
- Chapters **81–84** remain complete at the narrative/visual level under explicitly mixed English/Spanish fan-translation provenance; they remain barred from original-Japanese micro-linguistic claims.
- `NANA 7.8` remains outside this primary-fiction evidence freeze and is reserved for the later paratext phase.
- **Freeze condition met:** every load-bearing route required from the formerly legacy-provenance Volumes 1–3 now terminates in a reopened Japanese manga page or is explicitly left outside the stable synthesis route.

### Evidence-use conventions

- **Stabilized:** suitable to route into mature synthesis now.
- **Historical/provisional:** accurate to the earlier spoiler horizon but later revised or narrowed.
- **Open:** the extant corpus does not settle the proposition.
- **Legacy provenance gap:** analytically useful, but exact source routing still requires Phase-2 backfill.
- Evidence IDs quoted below remain owned by their original volume artifact; this ledger does not renumber them.

---

# Volume 01
**Canonical artifact:** `NANA_V01_DEEP_READING.md`  
**Artifact SHA-256 after Phase-2 backfill:** `6d769e62cb0b235f5dbe4fbeef0a9c7838740e230fae6b7d625d61fb7a7f9a31`  
**Primary source:** `Nana - Volume 01 [Japanese].epub`  
**Primary-source SHA-256:** `6531ED30FAD08FFBC2910F33DE7F657B7978C09A32256165BD41A989E1597A4D`  
**Spine extent:** 191  
**Chapter scope:** two origin narratives; no numbered chapter labels invented for this ledger  
**Provenance:** `migrated_legacy_analysis` + `phase2_backfill_status: complete`; locator state: `verified_backfill`  
**Stable evidence IDs present:** 10

## Stabilized historical thesis

Volume 1 is a diptych in which the two Nanas do not yet meet. Komatsu Nana and Osaki Nana independently confront the same underlying conflict from opposite directions: attachment can organize a life, but being attached does not settle who authors that life. Tokyo first functions as the place people leave *for*, forcing both women to face separation before it becomes their shared destination.

## Character, relationship, material, and formal delta

Komatsu Nana already combines romantic narrativization with partial self-knowledge: she can know that a relationship has no future and still experience its ending as apocalypse. Osaki Nana already combines fierce self-authorship with deep domestic and erotic attachment: Ren’s departure hurts precisely because the shared life mattered, while both Ren and Yasu explicitly leave the decision to follow or remain with Nana herself. Music becomes the route by which the post-Ren self begins to speak again.

## Decisive evidence routes

- `NANA_V01_E001` — TF/A — Komatsu origin, spine p.6 — 「金持ちでも貧乏でもない親に ほったらかされてスクスクと育ち」 — Komatsu Nana situates herself in an ordinary provincial family rather than an exceptional origin.
- `NANA_V01_E002` — TF/A — Komatsu origin, spine p.9 — 「東京？」 — Tokyo is isolated as a disruptive destination in the Asano departure sequence.
- `NANA_V01_E003` — TF/A — Komatsu origin, spine p.10 — 「今まで楽しかったよ ありがとう」 — Asano closes the relationship in moderate, concluded language, contrasting with Hachi’s apocalyptic experience of the same departure.
- `NANA_V01_E004` — CB/A — Komatsu origin, spine p.11 — 「この恋にしょせん未来なんかない」 — Hachi explicitly knew the relationship had no durable future even while organizing her present around it.
- `NANA_V01_E005` — CB/A — Komatsu origin, spine p.100 — 「映画みたいに ロマンチックで ドラマチックな恋」 — Hachi names the cinematic romantic script she wanted and immediately qualifies it through sexual/relational experience.
- `NANA_V01_E006` — CB/A — Osaki origin, spine p.129 — 「嫉妬が入り混じった羨望と 焦燥感 そして欲情」 — Nana retrospectively names her first response to Ren as a mixture of envy, impatience, and desire rather than a simple sweet romance.
- `NANA_V01_E007` — CB/A — Osaki origin, spine p.131, printed p.128 — 「レンと暮らすこの日常が 全て夢の中の出来事に思えたりする」 — Domestic life with Ren is experienced as emotionally precious and almost unreal, complicating any account of Nana as comfortable with pure autonomy.
- `NANA_V01_E008` — TF/A — Osaki origin, spine p.134 — 「おれ 東京行くから」／「おまえは おまえの好きに生きりゃいいさ」 — Ren announces his departure while explicitly leaving Nana’s life-choice to her.
- `NANA_V01_E009` — CB/A — Osaki origin, spine p.141 — 「ナナはレンの飼い猫じゃねぇぞ」／「それはナナが決める事だ」 — Yasu explicitly frames Nana as an autonomous adult whose decision cannot be made by Ren or the band.
- `NANA_V01_E010` — TF/A — Osaki origin, spine p.149 — 「ナナ！ おれのバンドで歌って！」／「溢れた想いが声になる」 — Nobu’s invitation and the narration route Nana’s post-separation affect back into singing and BLAST.

## Retrospective correction / later status

The Phase-2 backfill confirms rather than overturns the legacy thesis. It does, however, sharpen the status of several claims. Nana’s autonomy is not inferred from styling alone: Ren says she should live as she chooses, and Yasu explicitly rejects the idea that she is Ren’s “pet cat.” Conversely, her attachment to Ren is not a later projection: Volume 1 itself describes their domestic life as dreamlike and names her first response to him through desire, envy, and urgency. The mature synthesis may therefore use Volume 1 directly for the series’ attachment/self-authorship problem without relying on unlocated legacy prose.

**Phase-2 provenance state:** stabilized. Historical prose preserved; load-bearing routes verified against the Japanese EPUB.
---

# Volume 02
**Canonical artifact:** `NANA_V02_DEEP_READING.md`  
**Artifact SHA-256 after Phase-2 backfill:** `26a43cbc576c3f7b44e5ba4f9b46c3c89ffeec69d12a21132e75215f0f2b98f3`  
**Primary source:** `Nana - Volume 02 [Japanese].epub`  
**Primary-source SHA-256:** `5EE62617D0FFE23094DF4455B6FDBDE1B829EB09F5D1E860D72D62204D6270C6`  
**Spine extent:** 197  
**Chapter scope:** 1–4; title pages verified at spine pp.7, 62, 109, 148  
**Provenance:** `migrated_legacy_analysis` + `phase2_backfill_status: complete`; locator state: `verified_backfill`  
**Stable evidence IDs present:** 12

## Stabilized historical thesis

Volume 2 converts coincidence into infrastructure. The train encounter and shared name supply the language of fate, but Apartment 707 makes the relationship materially possible through something much less mystical: separate rooms, privacy, mutual aid, and half the rent. At the same time, Nana’s explicit loneliness prevents “independence” from being mistaken for comfort with isolation, while Hachi’s final experience of Nana’s voice turns the shared domestic space into remembered performance and magic.

## Character, relationship, material, and formal delta

Hachi’s migration is already more self-authored than the stereotype of simply following Shoji: she delays, saves, and intends to find work. Yet her domestic fantasy with Shoji still equates caring service with romantic happiness. With Nana, the shared home is instead founded on mutual choice and bounded privacy. Future Hachi also becomes an explicit internal critic of her younger perspective, and Nana/Ren is revealed to contain both a death-together fantasy and a direct fear of being left alone.

## Decisive evidence routes

- `NANA_V02_E001` — CB/A — Pre-Ch.1 future narration, spine p.6 — 「これはやっぱり運命だと思う 笑ってもいいよ」 — Future Hachi retrospectively frames the encounter as fate over an image of the still-empty 707.
- `NANA_V02_E002` — TF/A — Ch.1, spine p.31 — 「泣く泣く地元残って上京資金貯めたんだ」 — Hachi delayed migration and saved money for Tokyo rather than immediately following Shoji.
- `NANA_V02_E003` — TF/A — Ch.1, spine p.33 — 「同い年の女が 同じ電車で 同じ時刻に上京する」／「あたしもナナってゆーんだ」 — The same-name coincidence becomes the textual basis for Hachi’s fate framing.
- `NANA_V02_E004` — CB/A — Ch.1, spine p.35 — 「あたしは自分の事ばかりしゃべって ナナの話は少しも聞いてあげられなかったね」 — Future Hachi explicitly corrects the younger self’s information asymmetry and self-centered conversational gaze.
- `NANA_V02_E005` — CB/A — Ch.1, spine p.47 — 「毎日 こんな風に彼の身の周りのお世話をして暮らせたら どんなに幸せかしら♡」 — Hachi initially imagines domestic service to Shoji as an ideal form of romantic happiness.
- `NANA_V02_E006` — FP/A — Ch.1, spine p.61 — 「あの川べりで肩を並べて 水面を彩る光を見たよね」／「あの頃 口ずさんでいたメロディーを もう一度 聴かせてよ」 — Future address turns an early shared scene into anticipatory memory and links home, music, and loss without yet specifying later causes.
- `NANA_V02_E007` — TF/A — Ch.2, spine p.68 — 「ここにします♡」／「いや 決めた ここにする」 — Both women independently choose Apartment 707 before the shared-living proposal is finalized.
- `NANA_V02_E008` — TF/A — Ch.2, spine p.71 — 「お互いのプライバシーは守れるし けど いざという時は助け合える」 — 707 is explicitly described as an architecture combining privacy, mutual aid, and shared costs.
- `NANA_V02_E009` — TF/A — Ch.3, spine p.141 — 「もし あたしが死んだら 一緒に死んでくれる？」／「いいよ」 — The Nana/Ren flashback establishes an explicit fantasy of co-destruction within their romantic imagination.
- `NANA_V02_E010` — CB/A — Ch.3, spine p.142 — 「あたし ずっと 一人で寂しかった」／「もう二度と 独りぼっちは嫌だよ……」 — Nana directly distinguishes self-authored independence from painful aloneness.
- `NANA_V02_E011` — CB/A — Ch.4, spine p.187 — 「あたしは その声の虜になったんだよ」 — Future Hachi describes Nana’s unfinished-song performance as enchantment/captivity rather than mere technical admiration.
- `NANA_V02_E012` — CB/A — Ch.4, spine p.188 — 「食卓がステージに」／「携帯がマイクに」／「三日月がスポットライトになる」 — Future Hachi retrospectively transforms 707’s domestic objects into performance space and calls Nana’s effect singular magic.

## Retrospective correction / later status

The backfill confirms the legacy distinction between **independence and aloneness** and gives it a direct route at spine p.142. It also stabilizes the formal claim that 707 is not simply “found family” sentiment: the landlord’s description explicitly combines privacy, emergency mutual aid, and economics. The ending’s table/stage, phone/microphone, moon/spotlight transformation is now directly locatable and can support later synthesis on domestic space, music, and Hachi’s retrospective mythologization.

**Phase-2 provenance state:** stabilized. Historical prose preserved; load-bearing routes verified against the Japanese EPUB.
---

# Volume 03
**Canonical artifact:** `NANA_V03_DEEP_READING.md`  
**Artifact SHA-256 after Phase-2 backfill:** `d692655425259e7674d77650a93a2a70c5130826d81ead9c5da95213946cab41`  
**Primary source:** `Nana - Volume 03 [Japanese].epub`  
**Primary-source SHA-256:** `125294CD0155374764495E63341AFD91CC959DB3AD21EE0C90BC2A6DDAB0CE32`  
**Spine extent:** 189  
**Chapter scope:** 5–8; title pages verified at spine pp.7, 52, 99, 143  
**Provenance:** `migrated_legacy_analysis` + `phase2_backfill_status: complete`; locator state: `verified_backfill`  
**Stable evidence IDs present:** 13

## Stabilized historical thesis

Volume 3 asks what happens when romance and home stop pointing toward the same person. Hachi’s relation to Nana acquires explicit, qualified romantic language from future Hachi herself—`かなり恋に近い`, `初恋みたい`, and the counterfactual `もしもナナが男だったら 一世一代の恋`—without becoming an ordinary declared romance. In parallel, Shoji and Sachiko demonstrate how care without boundaries can become betrayal even when no participant begins with a simple malicious plan.

## Character, relationship, material, and formal delta

707 becomes a candidate “hometown” precisely because Nana claims she has none. Hachi’s adulthood also becomes materially legible through savings, work, and the house fantasy. Shoji’s affair arc is stabilized as an information-and-boundary problem: Junko predicts that continued consolation will deepen the entanglement; Shoji recognizes being emotionally soothed by Sachiko; Sachiko tries both self-removal and “friends only”; and Chapter 8 places Hachi’s joking `幸子と浮気中？` message over the already-real betrayal.

## Decisive evidence routes

- `NANA_V03_E001` — TF/A — Ch.5, spine p.19, printed p.16 — 「なんか ドキドキして眠れないね」／「違うよ そーゆードキドキじゃなくて！」 — The shared-bed scene introduces sexual/romantic possibility and immediately has Hachi verbally distinguish the excitement from that category.
- `NANA_V03_E002` — CB/A — Ch.5, spine p.50 — 「あたしのナナへの憧れは かなり恋に近いものだったと思います」 — Future Hachi explicitly classifies her admiration for Nana as quite close to romantic love, with retrospective qualification.
- `NANA_V03_E003` — CB/A — Ch.5, spine p.51 — 「とても幸福な初恋みたいだったよ」 — Future Hachi analogizes the relationship to a very happy first love while preserving “みたい” rather than asserting an ordinary romance category.
- `NANA_V03_E004` — CB/A — Ch.6, spine p.90 — 「あたしには故郷などない」 — Nana explicitly denies possessing a hometown/home-origin in response to Hachi’s homesickness question.
- `NANA_V03_E005` — FP/A — Ch.6, spine p.95 — 「あの窓辺の食卓も椅子も あの頃のまま あの場所にあるよ」 — Future Hachi answers Nana’s “no hometown” claim by locating home in the preserved material space of 707.
- `NANA_V03_E006` — CB/A — Ch.7, spine p.112 — 「お母さんがくれた30万は なるべく使わないで ちゃんと定期に入れて 更に自分で積み立てるんだ」 — Hachi makes a concrete savings plan tied to the imagined future house, showing material adulthood inside her romantic script.
- `NANA_V03_E007` — CB/A — Ch.7, spine p.123, printed p.120 — 「きっぱり縁を切る事ね」／「フォローすればフォローするほど どんどん傷つけて深みにハマるよ」 — Junko identifies continued consoling contact as the mechanism by which Shoji and Sachiko will deepen the boundary violation.
- `NANA_V03_E008` — CB/A — Ch.7, spine p.131 — 「何だっつうか おれは癒されてるんだ」 — Shoji recognizes that Sachiko provides emotional soothing even though he initially intended to avoid involvement.
- `NANA_V03_E009` — CB/A — Ch.7, spine p.136 — 「章司は全然悪くないもん」／「あたし…邪魔しないように気をつけるから……」 — Sachiko attempts to absolve Shoji and promises non-interference, revealing both her boundary awareness and self-erasing stance.
- `NANA_V03_E010` — CB/A — Ch.7, spine p.137 — 「友達でいいから……」／「縁を切るなんて言わないで」 — Sachiko asks to retain friendship rather than accept clean separation, enacting the exact boundary problem Junko predicted.
- `NANA_V03_E011` — TF/A — Ch.7, spine p.140 — 「じゃあ あたしが 歌で稼いで建ててやるよ」 — Nana jokingly/seriously offers musical earnings as an alternative provider route for Hachi’s house dream.
- `NANA_V03_E012` — CB/A — Ch.7, spine p.140 — 「もしもナナが男だったら 一世一代の恋が出来るのに」 — Future Hachi explicitly imagines gender as the missing permission for a once-in-a-lifetime romance with Nana.
- `NANA_V03_E013` — TF/A — Ch.8, spine p.144 — 「電話つながらないよー^^ 幸子と浮気中？ つもる話がいっぱいあるよ 会いたいよーー」 — Hachi jokingly names the actual affair while Shoji reads the message with Sachiko asleep behind him, producing direct dramatic irony and information asymmetry.

## Retrospective correction / later status

Phase 2 resolves the largest legacy provenance problem in the early corpus. The Nana/Hachi queer reading no longer depends on paraphrase: the exact qualified wording is routed to reopened Japanese pages. Likewise, the “707 as created hometown” thesis is grounded in Nana’s `故郷などない` and future Hachi’s answer through the preserved table/chairs. The Shoji/Sachiko moral analysis is now supported by a chain of separately locatable warnings, self-descriptions, attempted boundaries, and dramatic irony rather than by a single retrospective summary.

**Phase-2 provenance state:** stabilized. Historical prose preserved; load-bearing routes verified against the Japanese EPUB.
---

# Volume 04
**Canonical artifact:** `NANA_V04_DEEP_READING.md`  
**Artifact SHA-256:** `ca797fc9ea88699424e2a7206f21e75d2a87fd34f5d7c2e5393246ae8fc49939`  
**Primary source:** `Nana - Volume 04 [Japanese].epub`  
**Primary-source SHA-256:** `f2e9b71e5449f62ce2f215ee32e0d5f15440dcb35d2e7525be589a25f2b412f0`  
**Spine extent:** 197  
**Chapter scope:** 9-12  
**Provenance:** `full`; locator state: `verified`  
**Stable evidence IDs present:** 33

## Stabilized historical thesis

Volume 4 is the first volume in which *NANA* makes a major relationship collapse and then asks where the emotional energy of that collapse goes. Hachi loses Shoji. But the volume does not structurally leave her alone. Instead, the need that had been invested in the boyfriend category is redistributed across a relationship that the manga has already made difficult to classify: Hachi and Nana. That movement is not subtle by the end of the volume.

## Character, relationship, material, and formal delta

Major character field: 大崎ナナ / Osaki Nana, 小松奈々 / Komatsu Nana / Hachi, 遠藤章司 / Shoji Endo, 川村幸子 / Sachiko Kawamura, 寺島伸夫 / Nobu Terashima, 高木泰士 / Yasu Takagi, 岡崎真一 / Shin Okazaki, 本城蓮 / Ren Honjo, … Major relationship field: Nana/Hachi, Hachi/Shoji, Shoji/Sachiko, Nana/Ren, Nana/Yasu, Nana/BLAST, Hachi/707 network. Major thematic field: betrayal and breakup, love versus possession, friendship and queer ambiguity, jealousy, reciprocal care, home and domestic boundaries, family absence and inherited home, artistic vocation, celebrity and fandom, retrospective narration.

## Decisive evidence routes

- `NANA_V04_E005` — CB/A — Ch.9, spine 31 — 「戦わなきゃ負けだぞ！」「取り返せ！」 — Nana frames romantic betrayal through contest/reclamation
- `NANA_V04_E016` — TF/A — Ch.10, spine 86 — 「ヤキモチなんか…」「変なのはあたしの方かも」 — Hachi explicitly recognizes jealousy toward Misato over Nana
- `NANA_V04_E022` — TF/A — Ch.11, spine 113 — 「彼氏よりずっと大事だよ ナナは！」 — Hachi explicitly ranks Nana above boyfriend category
- `NANA_V04_E027` — TF/A — Ch.12, spine 161 — 「だから ちょっと憧れる」「にぎやかな家庭の雰囲気」 — Nana discloses family deprivation and longing for warm domesticity
- `NANA_V04_E033` — TF/A — Ch.12, spine 186 — 「ずっと握りしめていたかった」「いつまでもずっと」 — Future Hachi remembers joined hands and desire for permanence
- `NANA_V04_E001` — TI/B — Ch.9, spine 6 — 「東京はもっと暖かい所だと思ってた」 — Tokyo expectation versus lived cold; migration disappointment
- `NANA_V04_E002` — TF/A — Ch.9, spine 19 — 「もう純粋じゃなかった」「純粋なフリをした」 — Hachi knowingly performs innocence to preserve Nana's regard

## Retrospective correction / later status

The artifact predates the standardized v2 correction ledger. Later status must be routed through subsequent volume deltas rather than inferred backward into this historical file.
---

# Volume 05
**Canonical artifact:** `NANA_V05_DEEP_READING.md`  
**Artifact SHA-256:** `bd108402e3d140463a309167e93eb892a17ce43d5f52b123ba73c0af1347ac57`  
**Primary source:** `Nana - Volume 05 [Japanese].epub`  
**Primary-source SHA-256:** `b076dca671f9787954c8dea846025e8dbd17b68dea4d94a673471d5272b146da`  
**Spine extent:** 197  
**Chapter scope:** 13-16  
**Provenance:** `full`; locator state: `verified`  
**Stable evidence IDs present:** 42

## Stabilized historical thesis

Volume 5 is where *NANA* begins to distinguish **home** from **light**. By the end of Volume 4, Hachi has something that she did not possess when she first came to Tokyo: a genuine home. Apartment 707 is no longer merely cheap lodging. Nana worries when she is late. Hachi claims rights inside the apartment. They cook, sleep, wait, quarrel, reconcile, and organize their days around one another. Hachi has even said that Nana is more important than a boyfriend. Volume 5 does not undo any of that. Instead, it reveals that home does not exhaust Hachi's desire. She also wants to stand inside the **light** surrounding Nana: music, talent, beauty, celebrity, BLAST, Trapnest, Yasu's competence, Ren's fame, Reira's brilliance, Nobu's artistic romanticism, and the glamorous adult world that has suddenly opened around her because she happens to be Nana's roommate.

## Character, relationship, material, and formal delta

Major character field: 小松奈々 / Komatsu Nana / Hachi, 大崎ナナ / Osaki Nana, 本城蓮 / Ren Honjo, 一ノ瀬巧 / Takumi Ichinose, 寺島伸夫 / Nobu Terashima, 高木泰士 / Yasu Takagi, 芹澤レイラ / Reira Serizawa, 岡崎真一 / Shin Okazaki, … Major relationship field: Nana/Hachi, Nana/Ren, Hachi/Takumi, Hachi/Nobu, Hachi/Yasu, Yasu/Reira, Nana/Reira, Hachi/707 network. Major thematic field: admiration and access, celebrity and ordinariness, love fantasy and disposability, consent and emotional ambivalence, home versus light, work and unemployment, artistic rivalry, chosen family and secrecy, romantic scripts, aspiration and belonging.

## Decisive evidence routes

- `NANA_V05_E019` — RC/TI/B — Ch.15, p.139 — 「誰でもよかったわけじゃない」 / 「同じ光の中にいたかった」 — Hachi corrects indiscriminate-desire reading; attraction linked to Nana's luminous world
- `NANA_V05_E005` — TF/CB/A — Ch.14, p.64 — 「あんたとは暮らせない」 / 「あの家」 — Nana wants intimacy without present cohabitation; imagines later return
- `NANA_V05_E006` — TF/CB/A — Ch.14, p.94 — 「愛を感じた」 — Hachi interprets Nana arranging Takumi as practical love
- `NANA_V05_E040` — RC/TF/A — Ch.16, p.182 — 「誰にも相談出来なくて」 / 「苦しかった」 — Hachi's secrecy from Nana and Junko becomes the immediate pain of the Takumi relationship
- `NANA_V05_E018` — RC/CB/B — Ch.15, p.138 — 「空っぽのあたし」 — Future Hachi frames romance as filling an empty self
- `NANA_V05_E001` — TF/A — Ch.13, p.28 — 「待つの性に合わないんだ！」 — Nana refuses passive waiting and seeks Ren's number
- `NANA_V05_E002` — TF/A — Ch.13, p.42 — 「やり直す気ねえんだ」 / 「会いたかった」 — Declared non-restoration collides with embodied longing

## Retrospective correction / later status

Volume 5 is fundamentally about **what happens when Hachi mistakes access to an extraordinary world for a possible cure for ordinary insecurity**. The volume begins with Nana and Ren demonstrating that love can survive separation without returning to its old form. Hachi receives that complicated truth as romantic hope. Nana then repays Hachi's earlier intervention by bringing Takumi within reach. Hachi experiences that act as love. But the gift does more than satisfy a celebrity crush. It brings Hachi face-to-face with the social hierarchy she has only recently entered. Reira makes her feel ordinary. Yasu feels farther away. Nobu feels unexpectedly compatible. Takumi feels impossible—and then chooses her.
---

# Volume 06
**Canonical artifact:** `NANA_V06_DEEP_READING.md`  
**Artifact SHA-256:** `c04ff1f19d608e87405d76241e628b7b311dffbfde429261f77909728096b196`  
**Primary source:** `Nana - Volume 06 [Japanese].epub`  
**Primary-source SHA-256:** `23133AC0D27A5E604EDAE9D62BA9F8922B0A10C48E91336278BC8ADCEB0A6AEA`  
**Spine extent:** 197  
**Chapter scope:** 17-20  
**Provenance:** `native_v2_analysis`; locator state: `verified`  
**Stable evidence IDs present:** 60

## Stabilized historical thesis

Volume 6 is the first volume in which *NANA* turns one of its deepest relational problems into an explicit argument spoken by the characters themselves: > **What is the difference between loving someone and wanting to possess them?** The problem has existed from the beginning. Nana refused to follow Ren to Tokyo because loving him did not mean surrendering the authorship of her life. Hachi repeatedly wanted romantic partners to become secure homes. Shoji's betrayal demonstrated that a recognized relationship does not create ownership over another person's future. Apartment 707 established a different domestic model: two young women can share a life while retaining separate rooms, separate locks, separate money, separate obligations, and distinct selves. Volume 6 makes the latent tension verbal. Shin says that once people become accustomed to another person, they begin to want **「相手の全部」**—the whole of that person—and calls this **「人のサガ」**, human nature. Nobu tries to oppose that instinct with an ideal of **「本物の愛」**, a “real love” in which one asks for nothing and simply watches over the beloved kindly, only to admit that jealousy makes the ideal difficult to live. Takumi tells Hachi **「誰にも渡したくない」** and **「ずっとおれのものでいてよ」**: he does not want to give her to anyone and wants her to remain his. Ren, in a remembered conversation, admits that there are moments when he desperately wishes Nana were his.

## Character, relationship, material, and formal delta

Major character field: 小松奈々 / Komatsu Nana / Hachi, 大崎ナナ / Osaki Nana, 一ノ瀬巧 / Takumi Ichinose, 寺島伸夫 / Nobu Terashima, 岡崎真一 / Shin Okazaki, 本城蓮 / Ren Honjo, 高木泰士 / Yasu Takagi, 芹澤レイラ / Reira Serizawa. Major relationship field: Nana/Hachi, Hachi/Takumi, Hachi/Nobu, Nana/Ren, Nana/Yasu, Shin/Reira, BLAST/industry. Major thematic field: love versus possession, dream fulfillment versus happiness, loneliness and non-extractive care, sexual agency and relational ambivalence, shame and recognition, chosen home under strain, celebrity intimacy, public image and private self, reproductive autonomy, sex work and age/power, …

## Decisive evidence routes

- `NANA_V06_E001` — FP/A — Future Hachi says she had more wishes than she could count.
- `NANA_V06_E002` — TF/A — Hachi enjoys short-term department-store food-demonstration work.
- `NANA_V06_E003` — TF/A — Clouds hide the Milky Way, but the 707 group enjoys the Tanabata night.
- `NANA_V06_E004` — TI/B — Younger Hachi expects each fulfilled dream to increase happiness.
- `NANA_V06_E005` — TF/A — Hachi remembers Takumi's promise to see her first and eat her cooking again.
- `NANA_V06_E006` — CB/A — Hachi thinks Takumi keeping the promise would reduce her shame about sleeping with him.
- `NANA_V06_E007` — TF/A — Nana compares herself to Reira and feels depressed by Reira's talent.

## Retrospective correction / later status

Volume 6 begins with Tanabata. Hachi has innumerable wishes. Almost every major character has one: - Hachi wants Takumi to return. - Nana wants Ren and Hachi not to disappear. - Ren wants Nana. - Nobu wants Hachi. - Shin wants to understand what love is. - BLAST wants professional recognition. Then the wishes begin to come true. The story becomes less simple. That is not cynicism.
---

# Volume 07
**Canonical artifact:** `NANA_V07_DEEP_READING.md`  
**Artifact SHA-256:** `518c24e3765cca02abadf6d9fe0e144ef05dc6baedae2abf384e4af09d41fe92`  
**Primary source:** `Nana - Volume 07 [Japanese].epub`  
**Primary-source SHA-256:** `5F70DC04BEFB110160B77B4B6A17C7CDAF576C5DEF426C5490C71C8A88CC3908`  
**Spine extent:** 205  
**Chapter scope:** 21-24  
**Provenance:** `native_v2_analysis`; locator state: `verified`  
**Stable evidence IDs present:** 84

## Stabilized historical thesis

Volume 6 made possession explicit. Nana recognized that Ren and Hachi were not her property even while admitting that another person's separateness could make her desperately lonely. Ren had wished Nana were his. Takumi told Hachi to remain his. Shin argued that people eventually want 「相手の全部」—the whole beloved. Volume 7 shifts the problem from **possession** to **necessity**. Future Hachi gives the distinction herself: > 「ナナを独り占めしたかったんじゃない」   > 「ナナに必要とされたかっただけなの」 She did not want Nana all to herself. She wanted Nana to **need** her.

## Character, relationship, material, and formal delta

**Strengthened:** Nana/Hachi is organized around necessity as well as possession. Hachi wants irreplaceable value more than monopoly. **Complicated:** Nana's non-possession ethic. She respects Hachi's freedom but imagines it inside “my yard.” **Strengthened:** Hachi/Nobu is a genuine reciprocal romantic possibility, not merely a rebound. **Complicated:** Hachi/Nobu as mature solution. Fairy-tale idealization remains. **Strengthened:** Hachi's practical relationship skills: disclosure, decision, boundary speech, reciprocal care. **Reclassified:** Hachi's immediate belief that Takumi “did not call back” is incomplete. A blocked call attempt exists. This does not establish Takumi's love and does not cancel Hachi's breakup. **Complicated:** Takumi's respect for Hachi's boundary. He appears to minimize an explicit goodbye as mere anger.

## Decisive evidence routes

- `NANA_V07_E001` — TF/A — BLAST's growing audiences produce intense heat/vertigo for Hachi.
- `NANA_V07_E002` — TF/A — Hachi feels she is disappearing into the growing cheers.
- `NANA_V07_E003` — TF/A — Gaia observes BLAST and discusses Nana's charisma professionally.
- `NANA_V07_E004` — FP/A — Future Hachi says Nana's songs encourage her to live.
- `NANA_V07_E005` — CB/A — Hachi accepts Nana's career priorities as rational.
- `NANA_V07_E006` — CB/A — Hachi translates those priorities into “then you don't need me.”
- `NANA_V07_E007` — TF/A — Hachi tells Takumi not to come to 707 while Misato stays.

## Retrospective correction / later status

Volume 7 appears to give Hachi a solution. She explicitly ends a relationship she regards as unworkable and chooses a man she genuinely likes. Nobu wants her support. Hachi discovers that love can mean giving care rather than only receiving it. That is real progress. But the volume does not let a new romance erase the prior self. The poster is removed. The wall remembers. The wall is repainted. Hachi feels like she is destroying evidence. Future Hachi says wrongdoing and wounds remain even after they are covered. The same principle applies to Nana. Nana recognizes that Hachi is not property, yet imagines Hachi “free” inside Nana's yard. Moral understanding changes the form of possession without eliminating the attachment underneath it. And it applies to BLAST. Nana's professional dream is coming true, while Hachi feels herself disappear in the crowd. Shin's legal childhood is exposed because the band is becoming professional, then the industry immediately proposes hiding it again. The strongest compact thesis is therefore:
---

# Volume 08
**Canonical artifact:** `NANA_V08_DEEP_READING.md`  
**Artifact SHA-256:** `48d6adf9385b1f96a2abe48df079d0c6df50b2a84d6755e7ed358bd393a7f557`  
**Primary source:** `Nana - Volume 08 [Japanese].epub`  
**Primary-source SHA-256:** `DD895F84788D224343B421776FE6EB93796165000483FC47DDBDB6692459D96C`  
**Spine extent:** 205  
**Chapter scope:** 25-28  
**Provenance:** `native_v2_analysis`; locator state: `verified`  
**Stable evidence IDs present:** 95

## Stabilized historical thesis

Volume 7 ended with an apparently decisive movement toward self-authorship. Hachi stopped allowing the Takumi/Nobu triangle to remain undefined, told Takumi not to contact her again, and chose Nobu. Nana, meanwhile, recognized that loving Hachi could not ethically mean keeping her under literal control. The language of Volume 7 therefore seemed to point toward a difficult but intelligible principle: > **A person has to choose her own life, and love has to learn to survive that choice.** Volume 8 does not reject that principle. It asks what the principle costs once choice stops being abstract. Pregnancy turns self-authorship into a problem of body, time, money, employment, nausea, paternity uncertainty, medical deadlines, housing, career, public reputation, legal recognition, information access, and the willingness of other people to support the choice. The volume's deepest corrective comes from future Nana herself:

## Character, relationship, material, and formal delta

Major character field: 小松奈々 / Komatsu Nana / Hachi, 大崎ナナ / Osaki Nana, 一ノ瀬巧 / Takumi Ichinose, 寺島伸夫 / Nobu Terashima, 高木泰士 / Yasu Takagi, 本城蓮 / Ren Honjo, 岡崎真一 / Shin Okazaki, 芹澤レイラ / Reira Serizawa, … Major relationship field: Nana/Hachi, Hachi/Nobu, Hachi/Takumi, Nana/Ren, Nana/Yasu, Hachi/Junko, Shin/Reira, Nana/BLAST, … Major thematic field: limits of self-authorship, pregnancy and reproductive choice, material conditions of autonomy, information control, care and control in the same gesture, paternity uncertainty, legal recognition and marriage, money and parenthood, love versus possession, friendship as non-interference, …

## Decisive evidence routes

- `NANA_V08_E001` — FP/A — Future Hachi says she failed to fulfill a promise to build Nana a large house.
- `NANA_V08_E002` — TI/B — Hachi's imagined adult home includes a permanent return-place for Nana.
- `NANA_V08_E003` — TF/A — Nana insists her move to Tokyo is not simply a move to follow Ren.
- `NANA_V08_E004` — CB/A — Nana wants Yasu to come but cannot straightforwardly ask him to abandon his chosen life.
- `NANA_V08_E005` — TF/A — Nana explicitly wants huge stages, large applause, and substantial money.
- `NANA_V08_E006` — TF/A — Nana calls song a means of living rather than sufficient princess-like happiness.
- `NANA_V08_E007` — TF/A — Nana dates meeting Hachi to March 5, 2001, her twentieth birthday.

## Retrospective correction / later status

Volume 8 begins with Hachi imagining a house that could always take Nana back. It ends with Nana imagining the person she wanted to be when Hachi looked at her. Between those two future addresses, Hachi becomes pregnant and almost every major abstraction the series has built is forced into material form. Freedom becomes money. Love becomes disclosure. Responsibility becomes contraception, recognition, groceries, work schedules and who can afford a child. Possession becomes access to a phone.
---

# Volume 09
**Canonical artifact:** `NANA_V09_DEEP_READING.md`  
**Artifact SHA-256:** `bd94c782afe70640bd98e6103709692bf5a2dde5d78415f8ba09856f5f6a16d1`  
**Primary source:** `Nana - Volume 09 [Japanese].epub`  
**Primary-source SHA-256:** `7A7E22BBC010E4350DFE07E2914D54F0A4B803A1DA48D3CC3D032397047AD25C`  
**Spine extent:** 281  
**Chapter scope:** 29-32 + NAOKI [NANA 特別編]  
**Provenance:** `full`; locator state: `verified`  
**Stable evidence IDs present:** 105

## Stabilized historical thesis

Volume 8 made autonomy material. Pregnancy forced Hachi's life out of the abstract vocabulary of romance and into body, money, work, paternity, housing, childcare, information, and the practical resources that make a choice possible. Volume 9 asks what happens next, when those practical conditions are rapidly turned into **structures**. Takumi converts uncertainty into administration. Marriage becomes housing, security, rent, family notification, media strategy, and a timetable. Hachi's pregnancy becomes a problem that can be managed through money and planning. Nana's relationship with Hachi becomes something she tries to measure through emails, absence, longing, and the deliberate refusal to return. Paparazzi convert the private network into public information. BLAST's rivalry with Trapnest becomes commercially and emotionally legible. Even the strawberry glasses become evidence: an inexpensive object carries a history that a newly purchased identical object cannot actually replace. The volume's governing question is therefore: > **Who gets to author intimacy once intimacy becomes legible as a structure?** That question produces some of the darkest and most revealing material in the series so far.

## Character, relationship, material, and formal delta

Major character field: 小松奈々 / Komatsu Nana / Hachi, 大崎ナナ / Osaki Nana, 一ノ瀬巧 / Takumi Ichinose, 寺島伸夫 / Nobu Terashima, 本城蓮 / Ren Honjo, 高木泰士 / Yasu Takagi, 芹澤レイラ / Reira Serizawa, 岡崎真一 / Shin Okazaki, … Major relationship field: Nana/Hachi, Hachi/Takumi, Hachi/Nobu, Nana/Ren, Nana/Nobu, Nana/Yasu, Reira/Takumi, Reira/Yasu, … Major thematic field: intimate authorship and administration, sexual assault and entitlement, care and control, pregnancy and material security, marriage as legal/public structure, house versus home, possession and attachment testing, artistic identity and completion, celebrity surveillance, information and relationship evidence, …

## Decisive evidence routes

- `NANA_V09_E017` — VJ/A — The encounter is rape/sexual assault; the pregnancy predates it and earlier consensual encounters remain separately classified.
- `NANA_V09_E014` — TF/A — Takumi frames the sexual demand through jealousy over another man having had Hachi.
- `NANA_V09_E016` — VF — A / Visual sequence shows continued sexual activity with Hachi distressed. — Visual sequence shows continued sexual activity with Hachi distressed.
- `NANA_V09_E001` — TF/A — Takumi announces that he and Hachi have decided to marry.
- `NANA_V09_E033` — TI/A — Takumi conceptualizes Trapnest/Reira success as a growing castle that imprisons Reira in a tower.
- `NANA_V09_E035` — CB/A — Takumi wishes for a prince capable of reaching and embracing Reira.
- `NANA_V09_E039` — TF/A — Nobu learns that Hachi and Takumi are said to be marrying.

## Retrospective correction / later status

Volume 9 is about **who gets to author intimacy once intimacy becomes legible to the world**. Takumi turns pregnancy into marriage, housing, security, family meetings, and publicity with extraordinary competence. Those plans solve genuine problems. The same certainty becomes ethically catastrophic when he treats Hachi's body as something available to settle his jealousy and continues sex despite her repeated objections. Nana turns absence into a test of whether Hachi still needs her. She knows Hachi is not her possession, yet deliberately wants Hachi to become lonely enough to miss her. She transforms artistic rivalry into a fantasy of taking Hachi back. Then the empty room reveals that the test has succeeded too well: distance has created evidence of a life moving elsewhere. Nobu turns the marriage into evidence that he was not dependable enough, even though the reader knows the causal structure is far more complicated. Paparazzi turn relationships into public data. Phones turn silence into measurable proof. A cheap glass turns shared domestic history into something no identical replacement can reproduce.
---

# Volume 10
**Canonical artifact:** `NANA_V10_DEEP_READING.md`  
**Artifact SHA-256:** `cca16485fb603bf50ca7c45632666cc26528d834788f0a6b196d22fd2f4f5544`  
**Primary source:** `Nana - Volume 10 [Japanese].epub`  
**Primary-source SHA-256:** `192AB8B22D04185EB2390366B37DEB606ECFB4A50818BBB904AD2E6B26EC0211`  
**Spine extent:** 212  
**Chapter scope:** 33-36 + おまけページ / 淳子の部屋  
**Provenance:** `full`; locator state: `verified`  
**Stable evidence IDs present:** 127

## Stabilized historical thesis

Volume 9 asked who gets to author intimacy once intimacy becomes **administrative, evidentiary, and public**. Volume 10 makes that problem explicit by turning almost every major relationship into a **story somebody is telling**. The volume repeatedly uses the vocabulary of narrative itself: - **物語 / monogatari** — story; - **ヒーロー** — hero; - **ヒロイン** — heroine; - media narratives that turn partial facts into legible characters; - Hachi and Nobu imagining whether they still exist inside one another's stories; - Nana explicitly planning how BLAST can keep appearing in **「ハチの物語」**; - and future Nana correcting the role she once assigned herself. The strongest structural movement is this: > present Nana: **「『ハチ物語』のヒーローは あたしだ」**   > future Nana: **「あたしはもう あんたの物語のヒーローにはなれないけど」**   > future Nana: **「今もあたしの物語のヒロインの名前は奈々」**

## Character, relationship, material, and formal delta

Volume 10 does more than advance events. It **revises the confidence level of several Volume 9 interpretations** while preserving others unchanged.

## Decisive evidence routes

- `NANA_V10_E086` — CB/A — Present Nana thinks, `「ハチ物語」のヒーローは あたしだ`.
- `NANA_V10_E089` — FP/A — Future Nana says she can no longer be the hero of Hachi's story.
- `NANA_V10_E090` — FP/A — Future Nana says that the heroine of her own story is still named 奈々—Hachi.
- `NANA_V10_E051` — TF/A — Ren describes a band as a kind of `運命共同体`, a community bound by shared fate.
- `NANA_V10_E076` — TF/A — Nana and Nobu explicitly discuss a `伸夫物語`, treating life/relationship meaning as story roles.
- `NANA_V10_E126` — FP/A — Future Nana says glittering things still make her remember Ren.
- `NANA_V10_E001` — TF/A — Opening narration describes fighting as ultimately a collision of egos.

## Retrospective correction / later status

Volume 10 is the point where *NANA*'s private relationships become **competing narratives under public pressure**. The volume opens by saying that exposing true feelings does not guarantee understanding. It then spends four chapters demonstrating the proposition at every scale. Nana thinks she understands Hachi and imagines her as a ghost trapped inside Takumi's domestic system. Hachi, meanwhile, tells Shin and Junko something Nana does not know: she wants the child, loves Takumi, and chooses to build a household with him despite recognizing uncertainty. Nobu thinks he has disappeared from Hachi's story. The reader knows Hachi still asks about him and remembers their full-moon happiness as perhaps the happiest period of her life. The press tells stories about Nana, Ren, Yasu, and Shin from fragments that are partly true and profoundly deforming.
---

# Volume 11
**Canonical artifact:** `NANA_V11_DEEP_READING.md`  
**Artifact SHA-256:** `837eb3acdff6356bd24e4609960d4849c5cb707e78f69838beafc4a90042973f`  
**Primary source:** `Nana - Volume 11 [Japanese].epub`  
**Primary-source SHA-256:** `7323C8F77B843AF80331FE93360CD72C1DE202E1E7947829E6C95A008C6FE163`  
**Spine extent:** 258  
**Chapter scope:** 37-41 + おまけページ / 淳子の部屋  
**Provenance:** `full`; locator state: `verified`  
**Stable evidence IDs present:** 143

## Stabilized historical thesis

Volume 10 made **story** itself contested territory. Nana tried to cast herself as the hero of Hachi's story; future Nana relinquished that role while continuing to call Hachi the heroine of her own. Hachi, meanwhile, moved from being the object of Takumi's marriage announcement to explicitly authoring a future she wanted to try to build with Takumi and the child. Celebrity media took private lives and rewrote them as consumable narrative. Volume 11 asks the harder question that follows: > **Once a story has gone wrong, what does it mean to rewrite it?** The answer is not simply “go back.” In fact, the volume repeatedly distinguishes **repair** from **restoration**. Hachi finally identifies why her breakup with Shoji still hurts. It is not only that he cheated. Because they never faced one another calmly afterward, she never learned when the betrayal began, what he thought, or what part of their former intimacy remained true. Ignorance has contaminated memory itself. The happy period now feels painful because the ending has rewritten everything that came before it.

## Character, relationship, material, and formal delta

Volume 11 changes the cumulative *NANA* model in several important ways. These are **prospective-through-Volume-11** updates. “Retrospective correction” here means Volume 11 revises an inference that was reasonable through Volume 10; it does not import anything from later volumes.

## Decisive evidence routes

- `NANA_V11_E001` — TF/A — spine 5 — 向き合わなければいけない — The prefatory narration frames avoided ambiguity as something that must now be faced.
- `NANA_V11_E011` — TF/A — spine 29–30 — ちゃんと目を見て話がしたい — Reira wants face-to-face communication with Shin rather than continued mediated distance.
- `NANA_V11_E029` — TF/A — spine 68–72 — 寮と言う名の檻 — Shin describes the protected residence as “a cage called a dorm.”
- `NANA_V11_E050` — 第39話 — 122 / — — Page image inspected; anchor verified where quoted.
- `NANA_V11_E070` — CB/A — spine 166 — 結婚なんて形式的な発想 — Nana notes that formal marriage had not previously been central to her relationship with Ren.
- `NANA_V11_E121` — CB/A — spine 219 — 精神的な依存症だって立派な中毒 — Reira insists psychological dependence is still genuine dependence.
- `NANA_V11_E123` — CB/A — spine 219 — それはおれの役目じゃねぇ — Takumi defines person-level caretaking of Ren as outside his role.

## Retrospective correction / later status

The artifact predates the standardized v2 correction ledger. Later status must be routed through subsequent volume deltas rather than inferred backward into this historical file.
---

# Volume 12
**Canonical artifact:** `NANA_V12_DEEP_READING.md`  
**Artifact SHA-256:** `944ea137d676b4504ca4676bc02c2f974bcd65fb9ff9d377af70124322c2d9af`  
**Primary source:** `Nana - Volume 12 [Japanese].epub`  
**Primary-source SHA-256:** `289246C377D16F1F866D4A68FA64B1A864EC3280E330A064E60C113DEEB4FBC3`  
**Spine extent:** 204  
**Chapter scope:** 42-45 + おまけページ  
**Provenance:** `full`; locator state: `verified`  
**Stable evidence IDs present:** 163

## Stabilized historical thesis

Volume 11 ended by separating **repair** from **restoration**. Hachi's encounter with Shoji showed that a relationship can be faced honestly, its history partially repaired, and still remain over. Nana, by contrast, remained frightened of a future meeting with Hachi because she believed she would once again **甘える**—depend upon Hachi, lean into the relation, and risk losing whatever distance currently allows her to function. Volume 12 begins by refusing to answer the obvious plot question—*why are future Nana and Hachi apart?*—and instead shows the structure that survives the unknown separation. Future Hachi returns every summer to Room 707. The old network gathers. Fireworks bloom over the Tama River. Hachi has a child who calls her **ママ**. A matching yukata has been prepared for Nana. The room is full of people and yet organized around an absence: > **「707号室でみんなで待ってるよ」**   > *We're all waiting for you in Room 707.* Then the time layers fold into one another. Future fireworks become present fireworks. The room that was once domestic home, then scandalous media coordinate, then reunion site, becomes something else again: **ritual architecture**.

## Character, relationship, material, and formal delta

Volume 12 substantially changes the cumulative model established through Volume 11. The entries below are **prospective-through-Volume-12** updates only. When an earlier hypothesis is revised, the revision is based solely on material now reached in publication order.

## Decisive evidence routes

- `NANA_V12_E004` — TF/A — spine 12 — 「707号室でみんなで待ってるよ」 — Future Hachi says the old network waits for Nana at Room 707 during the summer fireworks.
- `NANA_V12_E108` — CB/A — spine 119 — 「軟禁」 — The celebrity-hotel arrangement is characterized as a form of soft confinement despite its luxury.
- `NANA_V12_E128` — CB/A — spine 141 — 「切れかけていた赤い糸」 — Future Hachi uses the red-thread-of-fate metaphor for the Nana/Hachi bond.
- `NANA_V12_E139` — CB/A — spine 169 — 「シンデレラの階段を 駆け上がってみるよ」 — Present Hachi casts her own domestic/romantic aspiration as climbing the Cinderella staircase.
- `NANA_V12_E152` — CB/A — spine 179 — 「花火大会に行く事だって許してくれた」 — Hachi explicitly frames the fireworks outing as something Takumi allowed.
- `NANA_V12_E158` — CB/A — spine 182 — 「シンデレラのガラスの靴は」 — Future Hachi returns to Cinderella at the volume ending and begins destabilizing the fairy-tale mechanism.
- `NANA_V12_E161` — CB/A — spine 182 — 「何をやっても空回りの一人芝居で」 — Future Hachi describes her own efforts as a futile one-woman play, returning to the earlier 空回り vocabulary.

## Retrospective correction / later status

The artifact predates the standardized v2 correction ledger. Later status must be routed through subsequent volume deltas rather than inferred backward into this historical file.
---

# Volume 13
**Canonical artifact:** `NANA_V13_DEEP_READING.md`  
**Artifact SHA-256:** `8b8c3aed3e00c9a18aa70d94774c8fad72b63babc7be3d7e2656f438136887c4`  
**Primary source:** `Nana - Volume 13 [Japanese].epub`  
**Primary-source SHA-256:** `7C12FFEDB5E4C34F96392FBC914FE343CC30934304D740E392F9F66633EF1926`  
**Spine extent:** 204  
**Chapter scope:** 46-49 + 淳子の部屋  
**Provenance:** `full`; locator state: `verified`  
**Stable evidence IDs present:** 210

## Stabilized historical thesis

Volume 12 ended by dismantling the idea that a recognizable happy-ending form can guarantee happiness. Hachi had climbed what she called the **シンデレラの階段**, only for her future narrating self to question the fairy tale's supposedly perfect shoe and to describe her own attempts at happiness as an **空回りの一人芝居**. The volume did not prove that love, marriage, wealth, or family were false. It proved that none of them can function as a self-executing ending. Volume 13 supplies the next piece of that argument. It repeatedly asks a deceptively simple question: > **「幸せのゴールなんてあるのかな」**   > *Is there really such a thing as a finish line for happiness?* The answer unfolds through several different relationships before future Hachi finally gives it grammatical form. At Shin and Reira's birthday party, Hachi is surrounded by almost every force currently capable of destabilizing her life: Takumi, Nobu, Nana, BLAST, Trapnest, Reira, Shin, Yuri, celebrity spectacle, jealousy, secrecy, desire, and the possibility of being abandoned. She sees Nobu disappear with another woman and discovers that having chosen Takumi does not erase jealousy. She sees Reira and realizes that the woman she idealizes as Trapnest's perfect princess may occupy a place in Takumi's life Hachi cannot rival. She imagines alternatives to Takumi that are strikingly concrete: work, Room 707, single motherhood, chosen kin. She then finds Nana in a crowd of roughly a hundred people with absolute confidence.

## Character, relationship, material, and formal delta

Volume 13 changes the cumulative reading more than its relatively compact four-chapter structure might suggest. Several questions carried forward from Volume 12 are answered directly; others are made more difficult rather than solved.

## Decisive evidence routes

- `NANA_V13_E017` — CB/A — spine 46 — 「幸せのゴールなんてあるのかな」 — Hachi questions whether happiness has any terminal finish line.
- `NANA_V13_E052` — CB/A — spine 72 — 「本人同士で納得行くまで話し合うしかねぇじゃん」 — Nobu says the couple themselves must talk until they reach an understanding.
- `NANA_V13_E099` — TF/A — spine 105 — 「無理矢理突っ込んで」 — Takumi himself acknowledges the force used during the sexual penetration.
- `NANA_V13_E146` — CB/A — spine 144 — 「人の絆は結べるものじゃない」 — Future Hachi rejects the idea of human bonds as things that can simply be tied/fastened into permanence.
- `NANA_V13_E147` — CB/A — spine 144 — 「繋ぐものなんだよ」 — Future Hachi reframes bonds as connections that must be maintained.
- `NANA_V13_E148` — CB/A — spine 144 — 「がんじがらめにならないで」 — Future Hachi warns against becoming completely bound by a relationship.
- `NANA_V13_E165` — 第49話 — 161 / — — Page image inspected; anchor verified where quoted.

## Retrospective correction / later status

The artifact predates the standardized v2 correction ledger. Later status must be routed through subsequent volume deltas rather than inferred backward into this historical file.
---

# Volume 14
**Canonical artifact:** `NANA_V14_DEEP_READING.md`  
**Artifact SHA-256:** `6ef8bf4bc52bdbc6b6ac14e8dbceff9ac50e81d4c8c15ab2c22561b908863c1e`  
**Primary source:** `Nana - Volume 14 [Japanese].epub`  
**Primary-source SHA-256:** `61FF000A29A21E93B39FB0B758D758E43CAEB5D109A5DE2AD0710F72116A3294`  
**Spine extent:** 193  
**Chapter scope:** 50-53 + おまけページ  
**Provenance:** `full`; locator state: `verified`  
**Stable evidence IDs present:** 151

## Stabilized historical thesis

Volume 13 ended with a mature-sounding principle: human bonds are not things one should tie into an inescapable knot; they are things one must **keep connected**. Its lexical distinction between **結ぶ** and **繋ぐ** was a warning against turning attachment into restraint. Volume 14 does not revoke that principle. It makes it harder. The problem now is epistemic as much as relational: > **How can people keep a bond connected when they do not fully know what is true inside it?** The volume repeatedly separates three things that characters want to treat as identical: 1. **what appears to be happening;** 2. **what is factually happening;** 3. **what remains durable despite changing appearances.**

## Character, relationship, material, and formal delta

Major character field: 小松奈々 / Komatsu Nana / Hachi, 大崎ナナ / Osaki Nana, 一ノ瀬巧 / Takumi Ichinose, 本城蓮 / Ren Honjo, 芹澤レイラ / Reira Serizawa, 高木泰士 / Yasu Takagi, 寺島伸夫 / Nobu Terashima, 岡崎真一 / Shin Okazaki, … Major relationship field: Nana/Hachi, Hachi/Takumi, Nana/Ren, Ren/Reira, Yasu/Miu, Nobu/Yuri, Shin/Reira, Nana/Yasu, … Major thematic field: appearance, fact, and durable reality, attachment substitution and fear of abandonment, marriage as love, contract, publicity, and possession, infidelity and asymmetric knowledge, jealousy, ownership, and lethal fantasy, substance use and self-destruction, adult intimacy without rescue, sex-work contracts and economic coercion, acceptance of a partner's past, fandom as support versus invasive possession, …

## Decisive evidence routes

- `NANA_V14_E072` — Nana - Volume 14 [Japanese].epub/「事実は事実としてありのまま受け入れろよ」 — Ch.52 — spine p. 112 — —
- `NANA_V14_E040` — Nana - Volume 14 [Japanese].epub/「AV女優を2年間続ける契約」 — Ch.51 — spine p. 76 — —
- `NANA_V14_E074` — Nana - Volume 14 [Japanese].epub/「物事を残酷な程ありのまま捉えて」 — Ch.52 — spine p. 113 — —
- `NANA_V14_E075` — Nana - Volume 14 [Japanese].epub/「タクミはありのままのあたしを受け入れてくれた」 — Ch.52 — spine p. 113 — —
- `NANA_V14_E079` — Nana - Volume 14 [Japanese].epub/「目に映るものはみんなまやかし」 — Ch.52 — spine p. 114 — —
- `NANA_V14_E085` — Nana - Volume 14 [Japanese].epub/「ヤスは精神安定剤みたいなもの」 — Ch.52 — spine p. 134 — —
- `NANA_V14_E092` — Nana - Volume 14 [Japanese].epub/「目に映るものはみんなまやかし」 — Ch.52 — spine p. 141 — —

## Retrospective correction / later status

The artifact predates the standardized v2 correction ledger. Later status must be routed through subsequent volume deltas rather than inferred backward into this historical file.
---

# Volume 15
**Canonical artifact:** `NANA_V15_DEEP_READING.md`  
**Artifact SHA-256:** `594b20901618c860110454b2bbbec2c30998467e4bb8ad519b76c3d657b5a675`  
**Primary source:** `Nana - Volume 15 [Japanese].epub`  
**Primary-source SHA-256:** `62E94E7A0A582EABD68602AAC16A7BF133FA13CF1084306C64972A4B35D504A6`  
**Spine extent:** 197  
**Chapter scope:** 54-57 + おまけページ  
**Provenance:** `full`; locator state: `verified`  
**Stable evidence IDs present:** 155

## Stabilized historical thesis

Volume 14 asked how anyone can distinguish appearance from fact when people possess unequal access to the truth. Volume 15 makes the problem more intimate. Its governing question is no longer only **what can I see?** It becomes: > **What does it mean for another person to live inside me, and how can someone remain inwardly present while still being badly misunderstood?** The volume builds that problem through three sensory and relational systems: **voice, scent, and legal inscription**. It opens with future Hachi saying that even when she and Nana are apart, Nana remains inside her. She can still summon Nana's strong, straight gaze and the singing voice that encourages her. But she immediately asks the question that governs the entire volume: > **「ねえナナには あたしの声が聞こえる？」**

## Character, relationship, material, and formal delta

Volume 15 is unusually important for the cumulative ledger because it does not merely add events. It **corrects how several earlier events should be understood**. The corrections below preserve the historical validity of the earlier volume readings while recording what the newly analyzed evidence now permits us to say.

## Decisive evidence routes

- `NANA_V15_E004` — FP/B — Ch.54, spine p. 10 — `あたしの声が聞こえる？` — Future Hachi questions reciprocal audibility.
- `NANA_V15_E039` — RC/A — Ch.55, spine p. 91 — `ナナを理想化した` — Future Hachi identifies her idealization of Nana as causal.
- `NANA_V15_E072` — CB/A — Ch.56, spine p. 124 — `刻印されちゃった感じ` — Miu describes Yasu’s scent as an imprint on herself.
- `NANA_V15_E073` — CB/A — Ch.56, spine p. 124 — `自分の中に誰かが住みついて` — Miu fears another person taking up residence inside her.
- `NANA_V15_E106` — CB/A — Ch.57, spine p. 158 — `赤い糸だ` — Reira explicitly names the ring connection as a red thread.
- `NANA_V15_E121` — RC/A — Ch.57, spine p. 168 — `おまえの意志をねじ伏せて来た` — Ren explicitly names his past override of Nana’s will.
- `NANA_V15_E001` — TF/A — Ch.54, spine p. 9 — `ハチ公へ` — Nana postcard preserves direct material communication with Hachi.

## Retrospective correction / later status

The artifact predates the standardized v2 correction ledger. Later status must be routed through subsequent volume deltas rather than inferred backward into this historical file.
---

# Volume 16
**Canonical artifact:** `NANA_V16_DEEP_READING.md`  
**Artifact SHA-256:** `137d83e55803bf3dc2190b1518e889aec4acf885f9fb6cf47ef67ab2a7315e33`  
**Primary source:** `Nana - Volume 16 [Japanese].epub`  
**Primary-source SHA-256:** `8AF53CF92B82157F624625E173E88951898CCA5BA0E131874A40ACAB7B6A34C2`  
**Spine extent:** 265  
**Chapter scope:** 58-61 + NOBU [NANA 特別編] + おまけページ / 淳子の部屋  
**Provenance:** `full`; locator state: `verified`  
**Stable evidence IDs present:** 159

## Stabilized historical thesis

Volume 15 ended with future Hachi making an ethically difficult choice. She would stop searching for Nana if finding her would expose her and wound her again, but she would continue to wait for Nana to stand up again. Volume 16 answers that gesture from the other side without resolving the absence itself. For the first time, the reader is given sustained, direct access to **future Nana**. She is alive. She is no longer merely the object of Hachi's address, the subject of rumor, or a missing figure inferred from photographs and annual rituals. Early in Chapter 58 the manga cuts to an unidentified pub or small performance venue marked `NAGORAD`. English is spoken around the room. A woman with very long straight hair stands at a microphone and sings. Her face is unmistakably Nana's. A man watches. Fireworks erupt outside. Shortly afterward, Search photographer Kurata reports that he could not find Nana, while another voice dismisses the search by saying that BLAST's Nana is, as rumored, already dead. The juxtaposition creates a radical information split:

## Character, relationship, material, and formal delta

Volume 16 produces several unusually large corrections to the cumulative model.

## Decisive evidence routes

- `NANA_V16_E011` — CB/A — Ch.58, spine p.20 — `ブラストのナナは噂通りもう死んだんだ` — A character repeats the rumor that Nana is dead; the reader has direct counterevidence.
- `NANA_V16_E048` — CB/A — Ch.59, spine p.89 — `もう 同じじゃなくてもいいから` — Nana explicitly imagines relation without sameness.
- `NANA_V16_E049` — CB/A — Ch.59, spine p.90 — `もっとちゃんと繋がりたい` — Nana substitutes genuine connection for sameness/matching.
- `NANA_V16_E051` — CB/A — Ch.59, spine p.98 — `母親に捨てられても 強く逞しく生きてる子供` — Editorial discussion converts Nana's abandonment into an inspirational narrative asset.
- `NANA_V16_E054` — TF/A — Ch.59, spine p.99-100 — `ここはあたしの家じゃない` — Future Nana recalls a lifelong sense that places were not truly her home.
- `NANA_V16_E095` — CB/B — Ch.61, spine p.153-155 — `[歌える仕事が少ない]` — Nana is frustrated that increasing fame does not produce enough singing work.
- `NANA_V16_E106` — CB/A — Ch.61, spine p.181 — `彼女や彼女の家族の為にも気をつけてあげる必要がある` — An investigator recognizes privacy obligations toward Nana's possible relatives.

## Retrospective correction / later status

The artifact predates the standardized v2 correction ledger. Later status must be routed through subsequent volume deltas rather than inferred backward into this historical file.
---

# Volume 17
**Canonical artifact:** `NANA_V17_DEEP_READING.md`  
**Artifact SHA-256:** `263b8423584d8b22f255052a04046ed302ff054efdffee51e993a7bce875c393`  
**Primary source:** `Nana - Volume 17 [Japanese].epub`  
**Primary-source SHA-256:** `1EB5CC05891734EA27EB900BDAF04BB8BAE8E447421AFD52A6EF3D0DF9E3BE2F`  
**Spine extent:** 196  
**Chapter scope:** 62-65 + おまけページ / 淳子の部屋  
**Provenance:** `full`; locator state: `verified`  
**Stable evidence IDs present:** 253

## Stabilized historical thesis

Volume 16 ended by changing the question of Nana's future absence. Nana was no longer merely a missing figure whose ontological status was uncertain: the reader had seen her alive, long-haired, singing at an unidentified venue marked `NAGORAD`. What remained missing was the bridge between that knowledge and the people still waiting for her. Volume 17 builds that bridge out of a photograph. Its central movement can be condensed to: > **searching → evidence → intrusion → failed protection → distributed care → permission to approach.** The opening future sequence returns to room 707 during the Christmas season. Hachi still maintains the ritual of placing a small tree on the table in the otherwise empty apartment. She says that as Christmas approaches she imagines an angel descending there and carrying happiness back to them. The desire is explicitly concentrated: `だけど今欲しいものはただひとつ`. The room remains materially unchanged, Nana's key has never been found among the things she left behind, and Hachi still imagines opening the door to find Nana returned.

## Character, relationship, material, and formal delta

Volume 17 produces more longitudinal corrections than its surface chronology initially suggests. It does not settle the major future catastrophe, Nana's reason for remaining away, the paternity questions, or the later configuration of the Ichinose marriage. What it does is change **who knows what**, **what kind of care the work is willing to endorse**, and **which objects now carry reliable versus unreliable knowledge**.

## Decisive evidence routes

- `NANA_V17_E009` — TF/A — Future prelude / Ch. 62, spine p.19 — `707号室の鍵は見つからなかった` — Nana's 707 key was not found among the belongings she left behind.
- `NANA_V17_E018` — SI/B — Future prelude / Ch. 62, spine p.23-25 — `写真` — Because Volume 16 independently showed the same long-haired Nana alive at the same venue, the photographs strongly corroborate Nana's survival for Hachi and Shin rather than functioning as an isolated rumor image.
- `NANA_V17_E019` — UA/A — Future prelude / Ch. 62, spine p.23-25 — `写真` — The sender, date, exact location, and route by which the photographs were obtained remain unresolved.
- `NANA_V17_E063` — TI/B — Ch. 62, spine p.56 — `写真` — The manga cuts from Hachi's past longing to future Hachi and Shin holding Nana's photographs, formally pairing desire with belated evidence.
- `NANA_V17_E137` — TI/A — Ch. 64, spine p.119 — `一人じゃない` — Hachi's new protective model centers relational plurality rather than solitary heroism.
- `NANA_V17_E147` — CB/A — Ch. 64, spine p.125 — `関係性はたいして重要じゃねぇ` — Yasu explicitly subordinates relationship labels to the persons involved.
- `NANA_V17_E149` — CB/A — Ch. 64, spine p.125 — `信頼で結ばれる` — Yasu identifies trust as the basis on which people are connected.

## Retrospective correction / later status

The artifact predates the standardized v2 correction ledger. Later status must be routed through subsequent volume deltas rather than inferred backward into this historical file.
---

# Volume 18
**Canonical artifact:** `NANA_V18_DEEP_READING.md`  
**Artifact SHA-256:** `cc36bcc47980d27093d4f1b7e77aad005f2936ebb02a36abc39cf120b71e1702`  
**Primary source:** `Nana - Volume 18 [Japanese].epub`  
**Primary-source SHA-256:** `88E91B44155D3B8DD9FF71791E49E7B07D2C954CDFAA2B513EF64F77F48BC40D`  
**Spine extent:** 253  
**Chapter scope:** 66-69 + 淳子の部屋 + [TAKUMI] タクミ [NANA 特別編]  
**Provenance:** `full`; locator state: `verified`  
**Stable evidence IDs present:** 364

## Stabilized historical thesis

Volume 17 ended with a future Hachi who finally possessed a possible route toward Nana and nevertheless phrased approach as a question: `あたしから 扉を開けてもいい?`. Volume 18 does not answer whether that door will be opened. Instead, it turns inward and asks what makes a person capable of remaining alive, working, singing, or moving at all when the structures that once made life legible have failed. The volume's deepest movement can be expressed as four linked corrections: > **how to die → how to live**   > **being alone → being abandoned**   > **receiving care → giving care back**   > **protecting a person → controlling the conditions around that person** These movements converge most clearly in Nana. The future sequence makes her suicidality textually explicit. At the snowy sea, she thinks that if the sea is there, death remains available to her. Paradoxically, that availability calms her enough to try living one more day: `もう1日生きてみようと思える`. Later she states that she came so far looking for a place to die. The sea's sound continues to invite surrender. Yet she also says that she cannot simply throw away the life Hachi once saved: `あんたに救われたこの命を / 捨てるなんて出来ないじゃない`.

## Character, relationship, material, and formal delta

Volume 18 produces several of the strongest cumulative corrections since Volume 13. The key is not that earlier interpretations become “wrong.” The v2 method preserves them as accurate descriptions of what the text had established at the earlier horizon. Volume 18 changes the evidence available.

## Decisive evidence routes

- `NANA_V18_E009` — CB/A — Ch. 66, spine p.20 — `いつでも死ぬ事は出来る` — Future Nana explicitly thinks that she can die whenever there is a sea.
- `NANA_V18_E026` — CB/B — Ch. 66, spine p.28 — `この命を繋ぎたい` — The montage links survival to keeping life connected for another day.
- `NANA_V18_E041` — CB/A — Ch. 66, spine p.45 — `あんたに救われたこの命` — Future Nana explicitly says Hachi saved her life.
- `NANA_V18_E043` — SI/A — Ch. 66, spine p.45 — `救われたこの命` — Hachi functions as a relational reason for Nana's continued life, while the source does not establish this as the only reason.
- `NANA_V18_E072` — `Nana - Volume 18 [Japanese].epub`/`レンと一緒に死ぬ` — Ch. 67 — p.72 — —
- `NANA_V18_E073` — `Nana - Volume 18 [Japanese].epub`/`ステージで死ぬ` — Ch. 67 — p.72 — —
- `NANA_V18_E077` — CB/A — Ch. 67, spine p.74 — `どう生きるか` — Nana explicitly says how one lives is what probably matters.

## Retrospective correction / later status

The artifact predates the standardized v2 correction ledger. Later status must be routed through subsequent volume deltas rather than inferred backward into this historical file.
---

# Volume 19
**Canonical artifact:** `NANA_V19_DEEP_READING.md`  
**Artifact SHA-256:** `77e4d95a4cbd00c5661f285c0d77b52a5f9cbcbd7bd0f1f7effbcb0a04f9b39f`  
**Primary source:** `Nana - Volume 19 [Japanese].epub`  
**Primary-source SHA-256:** `E38B3E2A27D585B78AF1809FFC793E30E2E089D40EAA690D852D7457B1E57652`  
**Spine extent:** 194  
**Chapter scope:** 70-73 + 淳子の部屋  
**Provenance:** `full`; locator state: `verified`  
**Stable evidence IDs present:** 199

## Stabilized historical thesis

Volume 18 asked whether a person can stand alone without becoming abandoned. Volume 19 asks the harder relational question that follows from that insight: > **Can another person reach toward you without making the reach into a claim?** The volume opens in the future with Hachi already possessing practical reasons not to rush toward Nana: children, work, family obligations, uncertainty about location. Yet she strips those explanations away from herself. What she is afraid of is not logistics. It is that the hand she extends will be refused: > `伸ばしたこの手を 振り払われる事が` That formulation changes the ethical shape of the future search. Hachi is no longer merely the abandoned friend trying to recover the person she loves. She recognizes that Nana may possess an answer of her own, including an answer Hachi does not want. The future reunion problem is therefore not only **finding Nana**. It is learning whether Hachi can approach Nana without treating discovery as entitlement to restoration.

## Character, relationship, material, and formal delta

Volume 19 is unusually revision-heavy. Several of its most important passages do not simply add new plot facts; they give characters language for structures that earlier volumes had already dramatized without naming. The v2 method therefore preserves prior readings as historically correct at their earlier spoiler horizons while recording how Volume 19 changes the cumulative model.

## Decisive evidence routes

- `NANA_V19_E035` — CB/A — Ch. 70, spine p.35 — `全てを犠牲にする必要はない` — Hachi explicitly rejects total sacrifice as a requirement of Ren’s love.
- `NANA_V19_E057` — CB/A — Ch. 71, spine p.65 — `ただの 愛人の一人` — Takumi frames becoming one of his mistresses as a degradation of Reira’s special position.
- `NANA_V19_E065` — CB/A — Ch. 71, spine p.73 — `そのうち迎えに行く` — Ren imagines eventually going to get Nana rather than immediate reunion.
- `NANA_V19_E107` — CB/A — Ch. 72, spine p.114 — `愛人失格` — Takumi uses mistress language while criticizing Reira’s visible lovestruck state.
- `NANA_V19_E114` — CB/A — Ch. 72, spine p.118 — `そいつの世界に閉じ込められて` — Takumi defines dependency as enclosure inside another person’s world.
- `NANA_V19_E153` — `Nana - Volume 19 [Japanese].epub`/`今度こそ 本気でがんばって` — Ch. 73 — p.149 — —
- `NANA_V19_E161` — `Nana - Volume 19 [Japanese].epub`/`自分を立て直すことに今は精一杯` — Ch. 73 — p.154 — —

## Retrospective correction / later status

Volume 19 begins with Hachi imagining the possibility that Nana may refuse her hand and ends with Takumi promising Reira that he will not let her die. Those lines belong together. Hachi's future position contains the painful maturity of someone who finally understands that love does not guarantee access. She may travel across the world, search for years, want reunion desperately, and still arrive before a person who has the right to say no. Takumi's final position contains a different kind of love. Reira is lonely enough to speak about dying. Takumi refuses the possibility that she will die. In human terms, this is profoundly moving. In ethical terms, the volume has just spent more than a hundred pages showing why being another person's sole rescue can become dangerous. Takumi wants Reira alive. He also wants to remain the person who decides the architecture in which she survives. The volume's most mature characters increasingly move away from certainty. Yasu does not tell Nana to become dependent; he tells her that connection creates responsibilities in both directions. Shin does not tell Reira to wait forever; he says he must rebuild himself, and if he still loves her when he is an adult, he may come. He refuses to promise.
---

# Volume 20
**Canonical artifact:** `NANA_V20_DEEP_READING.md`  
**Artifact SHA-256:** `bff960d7b56db6c532bf9bc5c545726a7fa549bbc422430d74d0e3072306439a`  
**Primary source:** `Nana - Volume 20 [Japanese].epub`  
**Primary-source SHA-256:** `cef275ddb704fa806a3117ad9f08091262ee6c6458ed9ab28bcc25bdc272b56f`  
**Spine extent:** 179  
**Chapter scope:** 74-77  
**Provenance:** `full`; locator state: `verified in artifact ledgers; YAML normalization pending`  
**Stable evidence IDs present:** 27

## Stabilized historical thesis

Volume 20 is the point at which Nana Osaki becomes unusually explicit about a contradiction the series has been building for years: she understands, intellectually, that the people she loves possess lives whose centers are not identical with her, but she cannot emotionally tolerate what that plurality means. The decisive formulation comes late in the volume: > 「レンには あたしより大切なものがある」   > 「ハチにも あたしより大切な人がいる」   > 「自分だって 譲れない夢があるのに」   > 「どうして あたしはそれが許せないんだよ」 Ren has something more important than Nana. Hachi has someone more important than Nana. Nana herself has a dream she will not surrender. She can see the symmetry. She can state it. What she cannot yet do is live inside it. That is why Volume 20 is less a volume of revelation than a volume of **self-recognition without release**.

## Character, relationship, material, and formal delta

This section records what Volume 20 changes in the series-so-far model without importing Volume 21.

## Decisive evidence routes

- `NANA_V20_E023` — TF/A — Ch.77, spine p.157 — 「他人を独り占めするなんて しょせん出来ない」 — Miu explicitly rejects monopolization and girlfriend role as potentially destructive demand
- `NANA_V20_E024` — TF/SI/A/B — Ch.77, spine p.158 — 「全てを犠牲にして あたしを愛して欲しい」 — Nana wants total sacrifice and fears taking everything from Ren
- `NANA_V20_E027` — TF/FP/UA/A/C — Ch.77, spine pp.174-176 — 「死ぬ時は道連れ」 / 「置き去りになんてされたくなかった」 — Old death pact and fear of being left behind close volume as ominous foreshadowing
- `NANA_V20_E015` — TF/SI/A/B — Ch.76, spine pp.123-124 — 「今出来る唯一の戦いは 歌わない事」 — Reira turns refusal to sing into leverage and reassesses meaning of song
- `NANA_V20_E019` — TF/SI/A/B — Ch.76, spine p.135 — 「自分だって 譲れない夢があるのに どうして あたしはそれが許せないんだよ」 — Nana explicitly recognizes contradiction between her autonomy and demand for priority
- `NANA_V20_E001` — TF/A — frontmatter, spine p.8 — 「レンが与えてくれたこの愛しい名前を」 — Ren-given name framed as beloved continuity
- `NANA_V20_E003` — TF/A — Ch.74, spine p.17 — 「おい蓮」「パパ」 — Future Hachi/Takumi household includes boy named Ren

## Retrospective correction / later status

Volume 20 is fundamentally about **the impossibility of making another person prove love by ceasing to be a person**. Everyone is confronting a version of that problem. Takumi cannot make Reira's desire mean whatever is operationally convenient for him. Trapnest cannot treat Ren's body as an endlessly schedulable resource. Reira discovers that even a singer may have to stop singing to reclaim herself. Miu refuses a role she thinks would tempt her to demand monopoly. Ren still loves Nana but begins to understand that love does not justify forcing himself upon her emotional world.

**Phase-2 metadata action:** locator tables are present and visually verified in the artifact; add/normalize `locator_status: verified` when canonical metadata is next revised.
---

# Volume 21
**Canonical artifact:** `NANA_V21_DEEP_READING.md`  
**Artifact SHA-256:** `cf11925c7d2dbe8dae8f0265d893f661686988fd58752d0aa9eac24ed4c4262a`  
**Primary source:** `Nana - Volume 21 [Japanese].epub`  
**Primary-source SHA-256:** `a085c40ce35538c097a852c3acac350ede83a67ee8873f62637eda1498b2d976`  
**Spine extent:** 197  
**Chapter scope:** 78-80  
**Provenance:** `full`; locator state: `verified in artifact ledgers; YAML normalization pending`  
**Stable evidence IDs present:** 36

## Stabilized historical thesis

Volume 21 is the catastrophe toward which Volume 20 was leaning but was not yet entitled to name. Ren dies on March 4, 2002, the night before Nana Osaki's twenty-first birthday. The old promise that Nana and Ren would die together is answered not through romantic consummation but through asymmetry: Ren dies and Nana remains. That distinction matters because Volume 20 had already made Nana's central relational contradiction explicit. She knew that Ren had commitments beyond her, that Hachi had people beyond her, and that she herself possessed a dream she would not surrender. Yet she still wanted the impossible form of love in which Ren would sacrifice everything for her, even life itself. The final line of Volume 20—「置き去りになんてされたくなかった」, not wanting to be left behind—was therefore correctly classified there as prospective rather than resolved evidence. Volume 21 retrospectively changes its status. Ren's death makes “being left behind” literal, but the volume does something more difficult than simply punishing Nana for possessiveness or converting a tragic romance into a cautionary tale. Its larger movement is from **the fantasy of dying together** toward an **ethic of remaining alive for the people who would be left behind**. That counter-ethic emerges most clearly through Hachi and Miu. Miu explains that the cuts on her wrist are shallow and habitual rather than an attempt to die. Hachi nevertheless recognizes that self-injury can become fatal without suicidal intent. She connects Miu's behavior to Ren's drug use: Ren probably was not taking drugs because he wanted to die either, but self-destruction can kill without a death …

## Character, relationship, material, and formal delta

Volume 21 is unusually important to the correction ledger because it converts several Volume 20 prospective signals into established facts while also overturning some overly simple ways those signals could have been read.

## Decisive evidence routes

- `NANA_V21_E036` — TF/UA/TI/A/C — Ch.80, p.174 — 「ナナがいないと」「始まらないの」 — Nana's future absence is established; cause is not
- `NANA_V21_E014` — TF/A — Ch.78, p.79 — 「レンが死んだ……」 — Nana receives explicit knowledge of death
- `NANA_V21_E007` — TF/CB/A — Ch.78, p.35 — 「レンが死んだんだよ！ ナナになんて言えばいいの？」 — Death becomes explicit and immediately creates speech/care problem around Nana
- `NANA_V21_E034` — TF/TI/A/B — Ch.80, p.169 — 「あたし達が目指していた未来は全て白紙になった」 — Ren's absence erases prior future blueprint
- `NANA_V21_E016` — TF/TI/A/B — Ch.78, p.82 — 「あたしの時間は止まった」 — Nana's grief represented as arrested subjective time
- `NANA_V21_E023` — CB/TI/A/B — Ch.79, p.118 — 「自分を痛めつけるのは やっぱり自殺行為だよ」 — Hachi distinguishes absence of suicidal intent from potentially lethal self-destructive behavior
- `NANA_V21_E025` — TF/TI/A/B — Ch.79, pp.120-121 — 「負けられない」「残された 大切な人達の為に」 — Survivors formulate persistence for people left behind

## Retrospective correction / later status

The artifact predates the standardized v2 correction ledger. Later status must be routed through subsequent volume deltas rather than inferred backward into this historical file.

**Phase-2 metadata action:** locator tables are present and visually verified in the artifact; add/normalize `locator_status: verified` when canonical metadata is next revised.
---

# Continuation — Chapters 81–84
**Canonical artifact:** `NANA_CH081_084_CONTINUATION_DEEP_READING.md`  
**Artifact SHA-256:** `eb4ba163759d98c7a5f94702b0c3f9579c782d7b7a50404be41e2e64eb988d78`  
**Source set:** `Nana Ch 81.cbz`, `Nana Ch 82.cbz`, `Nana Ch 83.cbz`, `Nana Ch 84.cbz`, `Nana Ch 84 (Espanol).cbz`  
**Source hashes:** ch81: `ed04613f587fcf53d0f9b8af8e17ff060fbdcd474db1a4751afd25e4e0c20c37`; ch82: `55dcdb42b41237e99ce67d1059f9958efc662a83b41d50e7d17867929dac4cc5`; ch83: `9d84857751c9197c675e610e77be7ff26af8da5cf2bd14fe4109d4d825a5ad9c`; ch84_en: `9e849d4ec99431803295dc1dc7121f9ecf844c6c2c8e1a402a219a48045d6e12`; ch84_es: `d942f1d72d50d796bae800c3bbe088362ecf776c377dc6ca728681556fe534ca`  
**Provenance:** `complete_mixed_translation`; canonical status: `canonical_phase1_endpoint`  
**Stable evidence IDs present:** 27

## Stabilized historical thesis
Volume 21 ended by destroying the characters' existing future. Ren's death did more than remove a person. It invalidated the network of plans that had organized BLAST, Trapnest, Nana, Hachi, Reira, Takumi, Shin, Nobu, and Yasu. The governing images were architectural and textual: yesterday's blueprint could no longer be used; the future had become blank paper; future Hachi still could not draw anything on it; and the numbered tankōbon run ended with the proposition that without Nana, nothing could begin. Chapters 81–84 begin inside that blankness. Their most important development, on the supplied evidence, is that *NANA* does **not** treat recovery as a dramatic conversion from grief to health. Instead it asks a series of narrower questions: - Who is allowed to collapse? - Who feels obligated to remain functional because someone else appears to need them? - Is being another person's refuge an expression of love, a self-imposed duty, or both? - Can physical closeness console without reopening a romance? - Can domestic routine keep a grieving community alive without pretending the loss has been solved? - When Nana laughs, sings, eats, or becomes angry again, is that recovery—or can apparent vitality coexist with surrender?

## Character, relationship, material, and formal delta


## Decisive evidence routes

- `NANA_C84_E007` — 84 — printed pp.11-12 / Spanish `013-014.jpg` / Takumi staying until Reira's mother can take over — B
- `NANA_C84_E011` — 84 — printed p.17 / English `...020...jpg`; Spanish `019.jpg` / work threat; Nana protests; “Takumi's wife” may no longer be needed — A/B
- `NANA_C81_E004` — 81 — `nana81_07-09` / “Takumi will have no one” — A/B
- `NANA_C82_E004` — 82 — `b05_1bnw.jpg` / “Takumi's wife” — A
- `NANA_C84_E005` — 84 — printed pp.7-10 / Reira unstable; Takumi work-focused; Hachi not mentioned — A/B
- `NANA_C84_E009` — 84 — printed pp.14-15 / Spanish `016-017.jpg` / Shin calls Reira's love long-unrequited; Hachi suspects Takumi loves Reira too — B/C
- `NANA_C83_E006` — 83 — printed p.5 / `iennana07` / “Takumi's refuge may not necessarily be me” — A/B
- `NANA_C84_E003` — 84 — printed pp.5-6 / Nana sings; Nobu guitar; Hachi joins — A/B
- `NANA_C81_E002` — 81 — `nana81_05-06` / “I want to stay with Nana / and everyone else” — A
- `NANA_C81_E003` — 81 — `nana81_07` / “I want to be spoiled like a child / and cry…” — A

## Retrospective correction / extant status


**Phase-2 language rule:** narrative, relational, chronology, visual, domestic, material, and broad thematic claims may be stabilized from these scans. Original-Japanese voice, pronoun, honorific, sentence-final, and lexical claims may **not** be stabilized from Chapters 81–84. Spanish-only Chapter-84 evidence remains translation-mediated even where its broad narrative content is clear.

---

# Cross-volume stabilization summary

The sequential corpus now supports a set of mature longitudinal propositions without erasing local ambiguity. The strongest are: (1) Nana/Hachi is the story’s most persistent temporal and domestic axis, but the work repeatedly refuses to collapse that axis into either ordinary friendship or a definitively consummated romance; (2) attachment becomes ethically dangerous when necessity, rescue, possession, or total sacrifice is treated as proof of love; (3) Hachi’s adulthood is materially authored through pregnancy, money, housing, marriage, work, and caregiving rather than romance alone; (4) Nana’s artistic vocation is both genuine self-authorship and, under stress, a defensive structure; (5) Takumi’s competence can provide real care while the same disposition repeatedly becomes unilateral control and, in at least one encounter, sexual violence; (6) BLAST and Trapnest transform private music into institutional labor, celebrity, surveillance, and commercial dependency; (7) future narration establishes absence, ritual, waiting, and later survival in stages, but never grants Hachi omniscience; and (8) the hiatus leaves trajectory without destination—especially Nana’s eventual departure, the final state of Hachi/Takumi/Nobu, Reira’s long-term future, and whether Nana/Hachi can reconnect without making need the condition of belonging.

## Phase-2 provenance freeze

The former unresolved queue for Volumes 1–3 is now closed. Their legacy analytical prose remains historically intact, but all early-series claims designated as load-bearing for mature synthesis now have stable evidence IDs and verified spine-page routes. Volumes 20–21 retain a minor YAML normalization task that does not affect retrievability because their evidence and locator ledgers are already present and verified. Chapters 81–84 retain their explicit translation boundary. No primary-fiction provenance issue remains that blocks structural synthesis.

**Document 15 freeze status:** **FROZEN for Phase 2 primary-fiction evidence stabilization.** Future changes should occur only if (a) a locator is discovered to be wrong, (b) superior original-language sources for Chapters 81–84 are supplied, or (c) a later synthesis claim requires reopening a currently non-load-bearing page. Such changes should be logged as explicit provenance revisions rather than silently edited.
