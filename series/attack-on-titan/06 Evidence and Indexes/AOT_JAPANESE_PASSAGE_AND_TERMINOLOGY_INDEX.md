---
series: AOT
artifact_type: japanese_passage_and_terminology_index
artifact_role: JAPANESE_PASSAGE_AND_TERMINOLOGY_INDEX
scope: V01-V34
generation: V2
version: '1.0'
status: canonical
date: '2026-08-28'
source_boundary: Japanese manga V01-V34; seeded from canonical deep readings, AOT_JAPANESE_VOICE_AND_VOCABULARY_LEDGER.md v2.1, AOT_V01-V34_SYNTHESIS_EVIDENCE_MATRIX.md v1.0, and AOT_PRIMARY_SOURCE_LOCATOR_INDEX_V01-V34.tsv v1.0; no English comparison corpus
governing_architecture: AOT_FULL_SERIES_SYNTHESIS_ARCHITECTURE_V1.md v1.2
governing_method: AOT_ANALYTICAL_METHOD_V2.md v2.1
canonical_home: 06 Evidence and Indexes/AOT_JAPANESE_PASSAGE_AND_TERMINOLOGY_INDEX.md
canonical_drive_id: 1QtdYKIs0Lq6ph91GMageDGEcjSbdfG76
supersedes: []
superseded_by: []
publication_state: canonical Drive placement and initial byte-for-byte readback verified
do_not_use_as_current_authority: false
---

# 『進撃の巨人』 / *Attack on Titan* — Japanese Passage and Terminology Index

## 0. Purpose and authority

This document is the canonical **Japanese-language retrieval layer** for the complete V01–V34 manga synthesis corpus once promoted from provisional publication state. It does not replace the volume deep readings, the claim-revision ledger, the synthesis evidence matrix, the primary-source locator TSV, or the Japanese voice/vocabulary ledger. Its job is narrower: make short exact/transcribed Japanese anchors, recurrent lexical networks, address/register distinctions, and translation-sensitive retrieval obligations findable before specialist drafting.

The index intentionally does **not** reproduce long passages. A short anchor may be sufficient to locate the relevant page, but any specialist claim that turns on exact wording, punctuation, omitted subject, sentence-final force, panel sequence, or visual context must reopen the primary Japanese manga according to the verification state recorded below.

### Authority distinctions

- **Locator-backed anchor:** Japanese-bearing anchor already present in `AOT_PRIMARY_SOURCE_LOCATOR_INDEX_V01-V34.tsv`; inherits that locator row’s verification state.
- **Supplemental canonical transcription:** short wording preserved in a canonical deep reading / Japanese voice ledger but absent as Japanese-bearing text from the locator TSV; evidence ID and page range are supplied here.
- **Lexical/register synthesis:** cross-volume grouping derived from repeated canonical anchors; useful for retrieval and hypothesis formation, but not itself a quotation or translation ruling.
- **Translation audit:** explicitly **not active**. `AOT_JAPANESE_ENGLISH_TRANSLATION_AUDIT_LEDGER.md` remains conditional on an English comparison corpus or a concrete disputed rendering.

## I. Coverage summary

- Locator-backed Japanese-bearing seed rows: **142**.
- Volumes represented by locator-backed Japanese anchors: **31/34**.
- Supplemental canonical short transcriptions added to close obvious language-retrieval gaps: **16**.
- Total seeded passage/term retrieval entries in Appendix A: **158**.
- Lexical/register clusters normalized below: **24**.
- Character self-reference/address profiles normalized below: **12**.

The uneven volume counts are not evidence that early volumes contain less important Japanese. V01–V18 are migrated V2 readings whose evidence IDs and chapter identities are stable while exact image locators remain selectively backfilled. V19–V34 were produced under progressively richer source-review infrastructure and therefore preserve more explicit page-level wording.

## II. High-value translation-sensitive anchor set

| Scope | Evidence | Japanese anchor | Speaker/domain | Why it matters | Locator / verification |
|---|---|---|---|---|---|
| V01 | `AOT_V01_E003` | 家畜 | Eren — Freedom deprivation | Safety without authorship is framed as domestication; compare later 奴隷. | 第1話 二千年後の君へ; CHAPTER_VERIFIED_PAGE_PENDING; P1 |
| V01 | `AOT_V01_E004` | 「駆逐してやる!!」 | Eren — Elimination lexicon | Early exterminatory formula; later target classes change. | 第2話 その日; CHAPTER_VERIFIED_PAGE_PENDING; P1 |
| V02 | `AOT_V02_E001` | 「この世界は残酷だ…そして…とても美しい」 | Mikasa — World evaluation | Co-presence of cruelty and beauty resists single-valence world description. | 第6話 少女が見た世界; CHAPTER_VERIFIED_PAGE_PENDING; P1 |
| V02 | `AOT_V02_E002` | 「戦え」 | Eren — Imperative | Early other-directed survival imperative; compare V26 self-command and V30 Grisha-directed command. | 第6話 少女が見た世界; CHAPTER_VERIFIED_PAGE_PENDING; P1 |
| V04 | `AOT_V04_E001` | 「オレが!! この世に生まれたからだ!!」 | Eren — Birth / entitlement | Birth is sufficient ground for world-claim; later reused against inherited instrumentalization. | 第14話 原初的欲求; CHAPTER_VERIFIED_PAGE_PENDING; P1 |
| V04 | `AOT_V04_E004` | 「命を投げうつことだけが戦うことじゃない」 | Armin — 戦う semantic range | Expands fighting beyond bodily sacrifice. | 第16話 必要; CHAPTER_VERIFIED_PAGE_PENDING; P1 |
| V06 | `AOT_V06_E005` | 「悔いが残らない方を自分で選べ」 | Levi — Choice / uncertainty | Agency returned when no chooser has privileged certainty. | 第25話 噛みつく; CHAPTER_VERIFIED_PAGE_PENDING; P1 |
| V09 | `AOT_V09_E001` | 「同じ言語のはずなんだが」 | Zeke — Language / outsider knowledge | Language recognition becomes an early world-model anomaly. | 第35話 獣の巨人; CHAPTER_VERIFIED_PAGE_PENDING; P1 |
| V10 | `AOT_V10_E004` | 「私の名前…ヒストリアって言うの」 | Historia — Name / identity | True-name declaration marks authored identity shift. | 第41話 ヒストリア; CHAPTER_VERIFIED_PAGE_PENDING; P1 |
| V10 | `AOT_V10_E007` | 「戦士として 最後まで責任を果たす」 | Reiner — 戦士 / 兵士 | Warrior role is explicitly distinguished from soldier performance. | 第42話 戦士; CHAPTER_VERIFIED_PAGE_PENDING; P1 |
| V12 | `AOT_V12_E007` | 「何度でも巻いてやる」 | Eren — Scarf / relationship | Concrete relational promise rather than abstract declaration. | 第50話 叫び; CHAPTER_VERIFIED_PAGE_PENDING; P1 |
| V12 | `AOT_V12_E008` | 座標 | Reiner — Titan ontology | Early in-world label for Coordinate/Founder-linked power. | 第50話 叫び; CHAPTER_VERIFIED_PAGE_PENDING; P1 |
| V16 | `AOT_V16_E006` | 「何が神だ!!」 | Historia — Sacred authority rejection | Religious/royal legitimacy language rejected under bodily coercion. | 第66話 願い; CHAPTER_VERIFIED_PAGE_PENDING; P1 |
| V16 | `AOT_V16_E007` | 「私は人類の敵…エレンの味方」 | Historia — Abstract humanity vs particular loyalty | Deliberately provocative category opposition; not a stable anti-human doctrine. | 第66話 願い; CHAPTER_VERIFIED_PAGE_PENDING; P1 |
| V17 | `AOT_V17_E006` | 「みんな…何かの奴隷だった」 | Kenny — 奴隷 metaphor | Dependency/addiction metaphor broadens beyond literal enslavement. | 第69話 友人; CHAPTER_VERIFIED_PAGE_PENDING; P1 |
| V18 | `AOT_V18_E007` | 「そこで初めて知ったんだ オレは不自由なんだって」 | Eren — 不自由 | Freedom consciousness emerges through recognition of confinement. | 第73話 はじまりの街; CHAPTER_VERIFIED_PAGE_PENDING; P1 |
| V19 | `AOT_V19_E002` | 「心臓を捧げよ」 | Survey Corps / Erwin-Levi context — Institutional formula | Sacrificial command formula later migrates into intimate farewell. | See canonical deep reading / Appendix A |
| V19 | `AOT_V19_E011` | 「まだ…ちゃんと…話し合ってないじゃないか」 | Marco — Dialogue / procedure | Moral failure framed as absence of completed discussion. | See canonical deep reading / Appendix A |
| V19 | `AOT_V19_E019` | 「君達は大切な仲間だ ちゃんと殺そうと思ってる」 | Bertolt — Recognition + lethal action | Attachment and lethal intention explicitly coexist. | Ch78; page0165; CANONICAL_DEEP_READING_LOCATOR; P2 |
| V20 | `AOT_V20_E005` | 「俺は選ぶぞ」 | Levi — Decision ownership | Direct choice assumption under acute clarity. | See canonical deep reading / Appendix A |
| V20 | `AOT_V20_E015` | 「僕がエレンにウソついたことあった?」 | Armin — Trust / deception | Sincerity reputation becomes deceptive instrument. | 第82話 勇者; page0156; CANONICAL_DEEP_READING_LOCATOR; P2 |
| V21 | `AOT_V21_E005` | 「辛い…辛いよ」 / 「それでも 前に進まなきゃいけない…」 | Hange — Grief + forward motion | Forward motion does not entail emotional acceptance. | See canonical deep reading / Appendix A |
| V22 | `AOT_V22_E021` | 「壁の中で人を愛せ」 | Eren Kruger — Love / recurrence | Relational imperative tied to preventing repetition. | Ch89; page0140-page0142; CANONICAL_DEEP_READING_LOCATOR; P2 |
| V22 | `AOT_V22_E032` | 「全部殺せば…オレ達 自由になれるのか?」 | Eren — Freedom interrogative | Elimination lexicon ends in question, not settled doctrine. | See canonical deep reading / Appendix A |
| V23 | `AOT_V23_E003` | 善良なエルディア人 | Gabi / institutional category — Identity qualification | Good-Eldian category encodes internalized conditional legitimacy. | See canonical deep reading / Appendix A |
| V24 | `AOT_V24_E010` | 「ライナーは死んだ」 | Reiner — Identity substitution | Explicit role fracture; not retrospective proof earlier self was fake. | See canonical deep reading / Appendix A |
| V24 | `AOT_V24_E022` | 「自分で自分の背中を押した奴」 | Eren — Self-authorship | Separates externally pushed hell from self-pushed action. | See canonical deep reading / Appendix A |
| V24 | `AOT_V24_E002` | 物語 / 語り手 / 演出家 / 舞台 | Willy Tybur — Dramaturgical politics | Political legitimacy and historical framing expressed through theater/story vocabulary. | See canonical deep reading / Appendix A |
| V25 | `AOT_V25_E008` | 「海の外も壁の中も同じなんだ」 | Eren — Recognition | De-essentializes enemy populations without guaranteeing restraint. | Ch100; page0075.jpeg; CANONICAL_DEEP_READING_LOCATOR; P2 |
| V25 | `AOT_V25_E010` | 「時代や環境のせいじゃなくて…俺が悪いんだよ」 | Reiner — Responsibility | Rejects total exculpation by context; current state may over-condemn self. | See canonical deep reading / Appendix A |
| V26 | `AOT_V26_E029` | 「戦わなければ / 勝てない / 戦え / 戦え」 | Eren — Self-command | Imperative direction becomes inward. | Ch106; page0188; CANONICAL_DEEP_READING_LOCATOR; P2 |
| V26 | `AOT_V26_E016` | 肉 | Sasha — Ordinary lexical recurrence | Terminal speech remains ordinary appetite-signature rather than elevated ideology. | Ch105; page0128-page0132; CANONICAL_DEEP_READING_LOCATOR; P2 |
| V27 | `AOT_V27_E014` | 「お前らが大事だからだ / 他の誰よりも… / だから…長生きしてほしい」 | Eren — Particular care | Named-intimate care is strong but cannot be universalized into anti-instrumental ethic. | See canonical deep reading / Appendix A |
| V28 | `AOT_V28_E016` | 自由 / 自由意志 | Eren / Zeke debate — Freedom vs free will | Distinct terms must not be flattened into one English freedom label. | Ch112; page0067-page0069; CANONICAL_DEEP_READING_LOCATOR; P2 |
| V28 | `AOT_V28_E024` | 奴隷 / 家畜 | Multiple — Agency-deprivation metaphors | Related but non-identical metaphors; literal and figurative uses must be separated. | Ch112; page0082-page0083; CANONICAL_DEEP_READING_LOCATOR; P2 |
| V28 | `AOT_V28_E008` | 「せめて子供達はこの森から出してやらんといかん」 | Artur Braus — 森 / children | Forest becomes intergenerational violence metaphor rooted in concrete adult responsibility. | Ch111; page0044-page0045; CANONICAL_DEEP_READING_LOCATOR; P2 |
| V29 | `AOT_V29_E037` | 「嘘だと思う」 | Armin — Epistemic hedge | と思う marks reconstruction as inference rather than certainty. | Ch118; page0156-page0158; CANONICAL_DEEP_READING_LOCATOR; P2 |
| V29 | `AOT_V29_E023` | 「私はマーレを信じてない」 | Pieck — Trust | Institutional distrust coexists with trust in comrades. | Ch116; page0091-page0096; CANONICAL_DEEP_READING_LOCATOR; P2 |
| V29 | `AOT_V29_E047` | 「悪魔なんていなかった… / この島には…人がいるだけ」 | Gabi — Category revision | 悪魔 collapses into 人 without erasing prior harm. | See canonical deep reading / Appendix A |
| V29 | `AOT_V29_E036` | 「子供は未来だ!!」 | Onyankopon — Children / futurity | Compressed anti-euthanasia value claim. | See canonical deep reading / Appendix A |
| V30 | `AOT_V30_E017` | 「こんなふざけた計画 オレは到底受け入れられない」 | Eren — Deception reveal | Explicitly retracts apparent euthanasia assent. | Ch120; page0073-page0074; CANONICAL_DEEP_READING_LOCATOR; P0 |
| V30 | `AOT_V30_E048` | 「お前は奴隷じゃない / 神でもない / ただの人だ」 | Eren -> Ymir — Personhood | Opposes slave/deity categories with personhood. | See canonical deep reading / Appendix A |
| V30 | `AOT_V30_E049` | 「お前が決めていい」 | Eren -> Ymir — Choice | Direct invitation to decide; relation to broader coercive politics must remain bounded. | See canonical deep reading / Appendix A |
| V30 | `AOT_V30_E019` | 「俺は王家の血を引く者だ / 俺の命令に従え」 | Zeke — Royal command | Bloodline used as explicit jurisdiction claim. | Ch120; page0076-page0079; CANONICAL_DEEP_READING_LOCATOR; P0 |
| V31 | `AOT_V31_E009` | 「オレの名は / オレの目的は / オレはその望みを拒む」 | Eren — Population address | Direct first-person broadcast architecture. | Ch123; page0044-page0046; CANONICAL_DEEP_READING_LOCATOR; P0 |
| V31 | `AOT_V31_E013` | 「前代未聞の大虐殺」 | Armin — Massacre naming | Analytical speaker uses blunt categorical moral description. | Ch124; page0061-page0062; CANONICAL_DEEP_READING_LOCATOR; P0 |
| V32 | `AOT_V32_E042` | 「世界を滅ぼす」 | Eren — Operational target | Private formulation names civilizational destruction directly. | Ch130; page0154-page0155; CANONICAL_DEEP_READING_LOCATOR; P0 |
| V32 | `AOT_V32_E042` | 「そんなの間違ってる!!」 | Historia — Moral refusal | Direct authored disagreement under constrained political burden. | Ch130; page0154-page0155; CANONICAL_DEEP_READING_LOCATOR; P0 |
| V32 | `AOT_V32_E043` | 「胸を張って生きていく」 / 「普通に生きる」 / 「幸せに生きる」 | Historia / Magath / Eren contexts — Ordinary-life lexicon | Positive-life vocabulary counterweights hereditary and exterminatory systems. | See canonical deep reading / Appendix A |
| V33 | `AOT_V33_E007` | 「壁の外に人類が生きてると知って…オレは…ガッカリした」 | Eren — Disappointment | High-value private motive anchor; does not replace other motives. | Ch131; page0027; CANONICAL_DEEP_READING_LOCATOR; P0 |
| V33 | `AOT_V33_E050` | 「君のどこが自由なのか」 | Armin -> Eren — Freedom challenge | Interrogative turns Erenian freedom claim back against him. | Ch134; page0181; CANONICAL_DEEP_READING_LOCATOR; P0 |
| V33 | `AOT_V33_E022` | 「理解することをあきらめない姿勢」 | Hange — Command epistemics | Understanding persistence becomes succession criterion. | Ch132; page0082; CANONICAL_DEEP_READING_LOCATOR; P0 |
| V34 | `AOT_V34_E040` | 「何でかわかんねぇけど」 / 「やりたかったんだ」 | Eren — Uncertainty / desire | Private terminal disclosure resists single-cause motive closure. | Ch139; page0205-page0207; CANONICAL_DEEP_READING_LOCATOR; P0 |
| V34 | `AOT_V34_E039` | 「死にたくねぇ」 | Eren — Mortality | Ordinary fear and attachment coexist with categorical public shell. | Ch139; page0200-page0204; CANONICAL_DEEP_READING_LOCATOR; P0 |
| V34 | `AOT_V34_E018` | 「このなんでもない一瞬」 | Armin — Ordinary value | Meaning attaches to purposeless ordinary experience. | Ch137; page0106-page0107; CANONICAL_DEEP_READING_LOCATOR; P0 |
| V34 | `AOT_V34_E046` | 「我々が人である何よりの証明」 | Armin — Evidence / personhood | Formal proof language in diplomacy. | Ch139; page0225-page0228; CANONICAL_DEEP_READING_LOCATOR; P0 |
| V34 | `AOT_V34_E049` | 「僕達の物語」 | Armin — Narrative diplomacy | Story becomes postwar political action rather than mere retrospective narration. | Ch139; page0235-page0242; CANONICAL_DEEP_READING_LOCATOR; P0 |
| V34 | `AOT_V34_E020` | 「ただ投げて / 取って… / また投げる」 | Zeke — Ordinary repetition | Purposeless catch punctures totalizing salvation theory. | Ch137; page0108-page0111; CANONICAL_DEEP_READING_LOCATOR; P0 |

## III. Lexical cluster index

| Cluster | Working gloss | Retrieval / interpretation rule |
|---|---|---|
| `自由 / 自由意志 / 不自由` | freedom, free will, unfreedom | Do not collapse 自由 and 自由意志. Erenian 自由 often concerns authorship/nonconfinement; V28 explicitly raises 自由意志 as a distinct free-will concept. 不自由 is experiential deprivation. |
| `戦え / 戦う` | fight; imperative fight | Track direction and audience. The same lexeme appears as Eren-to-Mikasa survival command, Eren self-command, Eren-to-Grisha pressure, and postwar institutional slogan. |
| `駆逐` | drive out / eradicate / exterminate | Stable Eren lexical shell with changing target class. Translation should not erase the continuity or imply identical moral object across contexts. |
| `進む / 進み続ける / 前に進む` | move forward / keep advancing | Speaker-state matters. Erenian advance vocabulary, Hange grief-driven continuation, and Reiner persistence share motion imagery without sharing motive or ethic. |
| `奴隷 / 家畜` | slave / livestock | Both mark deprived agency, but one invokes mastery/subjection and the other domestication. Figurative uses must be separated from literal Ymir slavery. |
| `戦士 / 兵士` | Warrior / soldier | A load-bearing institutional/identity opposition for Reiner/Bertolt/Annie. Preserve role distinction in translation and character modeling. |
| `悪魔 / 人` | devil / person | Enemy-construction vocabulary becomes explicit category revision in Gabi. Do not treat 悪魔 as a timeless ontological label. |
| `救う / 救い / 救済` | save / salvation | Morally non-uniform. Used for interpersonal rescue, euthanasia theory, world-saving hero rhetoric, and protection of children/future. |
| `子供 / 未来` | children / future | Central to inherited burden, reproductive policy, ordinary futurity, and anti-euthanasia claims. |
| `森` | forest | Literal space and social ontology of inherited killing. Artur Braus gives the clearest intergenerational formulation. |
| `道 / 座標 / 始祖 / 地鳴らし` | Paths / Coordinate / Founder / Rumbling | Mechanism terms carry different levels of in-world certainty. Do not harmonize later knowledge retroactively into earlier speakers. |
| `家族 / 仲間 / 相棒` | family / comrades / partner | Distinct relationship categories. Bertolt can call targets 仲間 while intending lethal action; Reiner/Bertolt 相棒 marks familiar entrustment; 家族 often anchors nonfungible attachment. |
| `兄さん / お兄ちゃん / 父さん / 母ちゃん` | older brother / dad / mom address forms | Kinship address encodes stance and intimacy. Zeke’s お兄ちゃん rhetoric is especially paternalistic and should not be flattened to neutral brother. |
| `信頼 / 信じる / 嘘 / 騙し討ち` | trust / believe / lie / surprise attack | Trust is proposition- and relationship-specific. Armin’s lie to Eren and Pieck’s institutional distrust are key counterexamples to simple sincerity models. |
| `話し合う / 話をする / 交渉` | talk things through / talk / negotiate | Marco’s procedural plea, Armin’s negotiation language, and later coalition dialogue should not be collapsed into generic pacifism. |
| `意味 / 無意味 / 何の意味も無い` | meaning / meaningless | Erwin’s charge rhetoric and Ymir/Zeke ordinary-life arguments use meaning language differently: assigned remembrance, existential nonnecessity, or purposeless value. |
| `生まれる / 生まれてきた` | to be born | Birth-based worth recurs from Eren’s world-claim through Carla/Keith and later anti-hereditary/anti-euthanasia reasoning. |
| `普通 / なんでもない一瞬 / 幸せに生きる` | ordinary / nothing-special moment / live happily | Positive-value lexicon. The series increasingly treats ordinary life as an end not exhausted by heroic or national purpose. |
| `正義 / 正当化 / 責任` | justice / justification / responsibility | Magath and coalition-era language differentiates causal explanation from moral cleansing. Responsibility should not be translated as mere blame when institutional accountability is intended. |
| `物語 / 語り手 / 演出家 / 舞台` | story / narrator / director / stage | Willy’s dramaturgical political lexicon and Armin’s postwar 僕達の物語 should be related but not equated: propaganda-stagecraft and dialogic testimony are different uses of narrative. |
| `理解 / 理解者 / わからない / と思う` | understanding / one-who-understands / not know / think | Epistemic stance markers. Zeke can claim privileged 理解者 status while Armin/Levi explicitly hedge; Eren’s V34 わかんねぇ is a major anti-omniscience anchor. |
| `帰る / 帰りたい / 帰ってきて` | return / want to return / come back | Home-return language can motivate care, coercion, betrayal, or refusal. Annie, Reiner, Mikasa and Warrior contexts require separate relationship-state tagging. |
| `心臓を捧げよ` | devote your heart | Institutional Survey Corps formula that later acquires intimate memorial/farewell force. Formulaic recurrence does not imply unchanged pragmatic function. |
| `オレ / 俺 / 僕 / 私` | first-person forms | Orthography and pronoun choice are high-value voice evidence but must be state- and speaker-indexed. Do not normalize all to English “I” when analyzing register. |

## IV. Self-reference, address, and register map

This table is a **retrieval model**, not a free-generation license. It records currently recurring written-Japanese forms in the manga corpus and must remain state/role/relationship conditioned.

| Character | Self-reference | Address / relation markers | Register constraint |
|---|---|---|---|
| Eren | `オレ; オレ達` | `お前; 父さん; 兄さん (contextual)` | Direct, low-hedge shell; can become interrogative/uncertain in private or terminal states. |
| Armin | `僕` | `君; names` | Explanatory/counterfactual; と思う and わからない preserve epistemic hedging; capable of tactical lying. |
| Reiner | `俺` | `お前; 相棒` | Role-conditioned: soldier/Warrior/partner/private guilt states differ sharply. |
| Bertolt | `僕` | `君達` | V19+ calm first-person ownership; attachment can be expressed without de-escalation. |
| Levi | `俺` | `お前; 団長` | Compressed command speech; uncertainty and direct choice coexist by state. |
| Erwin | `私 / 俺 (private desire sample)` | `兵士 (vocative)` | Public institutional rhetoric versus private first-person desire is load-bearing. |
| Historia | `私` | `names` | Temporal register shift from Christa-role performance to blunt self-authoring speech. |
| Annie | `私` | `names` | Low-temperature, anti-euphemistic directness; emotional intensity need not produce high elaboration. |
| Zeke | `俺` | `弟; お兄ちゃん (self-positioning); names` | Conversational softness can coexist with absolute command/jurisdiction. |
| Gabi | `私` | `peer names / direct address` | Categorical public merit language plus expressive peer register; ideology revision retains intensity. |
| Floch | `俺` | `お前ら / collective political address` | Self-lowering survivor rhetoric can transform into coercive collective-authority rhetoric. |
| Hange | `私 (where explicit)` | `names / 団長 context` | Technical explanation, grief, and succession speech are distinct states. |

## V. Names, roles, titles, and institutional terminology

| Term / contrast | Function in corpus | Retrieval caution |
|---|---|---|
| `クリスタ・レンズ → ヒストリア・レイス` | Identity/name transition | Treat as temporal self-presentation change, not a cosmetic alias swap. |
| `ユミルの民 / エルディア人` | Ethno-historical categories | Speaker/institution matters; later world knowledge should not rewrite earlier terminology. |
| `ユミル様` | Sacral address | Early Ilse/Titan evidence is historically suggestive but not a complete Founder ontology. |
| `戦士長` | Marley Warrior rank | Rank term encodes hierarchy even when Zeke’s surface tone is casual. |
| `団長` | Commander title | Address can become relationally loaded, especially Levi/Hange succession contexts. |
| `相棒` | Partner | Reiner/Bertolt familiar entrustment; do not generalize to all Warrior relations. |
| `始祖の巨人` | Founding Titan | Mechanism knowledge changes over time; tag source boundary. |
| `進撃の巨人` | Attack Titan | Title/name revelation has both diegetic and series-title resonance; avoid assuming one fixed English semantic paraphrase answers all uses. |
| `鎧の巨人 / 超大型巨人 / 獣の巨人` | Named Titan roles | Role labels participate in institutional identity and inheritance, not merely creature taxonomy. |
| `地鳴らし` | Rumbling | Operational referent evolves from deterrent concept to executed world-destruction process; context is mandatory. |
| `島の悪魔` | island devils | Political enemy category; later Gabi revision explicitly contests the category. |
| `善良なエルディア人` | good Eldian | Conditional-legitimacy category internalized by continental Eldians; not neutral praise. |
| `真の英雄ヘーロス` | true hero Helos | Heroic legitimacy label within Marleyan political mythology and later strategic rhetoric. |
| `自由の翼` | Wings of Freedom | Institutional symbol whose later political meaning should not be inferred solely from lexical form. |

## VI. Translation-sensitive distinctions to preserve in specialist drafting

### Directness is not certainty
Eren can use concrete elimination vocabulary and still end in `自由になれるのか?`; Armin can use categorical language tactically while privately hedging with `と思う`; Levi can speak tersely while explicitly denying knowledge of the correct counterfactual.

### Recognition is not de-escalation
Bertolt’s `大切な仲間` coexists with `殺そうと思ってる`; Annie and Reiner likewise show person-recognition without automatic cessation of violence. Translation should not soften or intensify this contradiction away.

### Care is not universal jurisdiction
Eren’s `長生きしてほしい` language toward named intimates is genuine. It must not be promoted into a universal anti-instrumental principle when the same speaker later names world destruction.

### Forward-motion vocabulary is speaker-dependent
`進み続ける`, `前に進む`, and related forms recur in Eren, Hange, Reiner and institutional afterlives. Shared lexeme does not mean shared ethic.

### Personhood labels are argumentative acts
`人`, `奴隷`, `神`, `悪魔`, `家畜` are not merely descriptive nouns. Speakers use them to grant, deny, or contest agency and moral standing.

### Pronouns and orthography matter
`オレ`, `俺`, `僕`, `私` are flattened by English first-person translation. For character voice, preserve who uses which form, under what state, and whether the orthographic choice itself is stable.

### Kinship language can be coercive
Zeke’s brother language and Founder/royal family vocabulary show that intimacy terms can claim interpretive or political jurisdiction rather than merely affection.

### Meaning and ordinary life must remain distinct
`意味` discourse around sacrifice should not absorb later `なんでもない一瞬`, catch, food, family, and ordinary-future vocabulary. The ending’s positive value often lies in experiences that do not require heroic justification.

## VII. Primary-source reinspection queue

| Priority | Scope | Why Japanese matters | Verification class | Required behavior |
|---|---|---|---|---|
| P0 | V30-V34 | Eren terminal motive, Founder causality, Ymir/personhood, Mikasa agency, ending recurrence | `PSV-JA / PSV-JA+VIS / PSV-MIX` | Reinspect primary Japanese pages before specialist publication; current index supplies retrieval anchors, not final translation adjudication. |
| P1 | V01-V18 | Load-bearing early claims whose locator rows remain page-pending | `PSV-JA or PSV-JA+VIS when elevated` | Chapter/evidence identity is stable; page/image backfill should be selective rather than a wholesale reread. |
| P2 | V19-V29 | Mature locator-backed wording used in specialist arguments | `normal verification` | Existing image/page locators make primary-page reopening mechanical when exact nuance matters. |
| OPEN | All | English-equivalent disputes | `conditional translation audit only` | Do not create AOT_JAPANESE_ENGLISH_TRANSLATION_AUDIT_LEDGER.md without an English comparison corpus or a concrete disputed rendering. |

### P0 late-series anchor families

Before Documents 02, 03, 07, 13, 14, 17, or 19 publish a wording-dependent conclusion, reopen the relevant V30–V34 primary pages for at least these families: Eren’s `自由 / 駆逐 / 戦え / 進み続ける / ガッカリした / やりたかった / わかんねぇ / 死にたくねぇ`; Ymir-directed `奴隷 / 神 / 人 / 決めていい`; Mikasa’s `家族 / 帰りたい` and scarf-related wording; Armin’s `前代未聞の大虐殺 / どこが自由 / なんでもない一瞬 / 証明 / 物語`; the V34 Founder-time and Ymir-love explanations; and postwar recurrence of `戦え`.

## VIII. Specialist routing

| Specialist | Japanese-language dependency |
|---|---|
| `AOT_02_EREN_JAEGER_FREEDOM_DESIRE_CAUSALITY_AND_RESPONSIBILITY.md` | Highest: freedom, advance, elimination, birth, self-command, terminal uncertainty, pronoun/register shifts. |
| `AOT_03_MIKASA_ACKERMAN_LOVE_AGENCY_HOME_AND_MEMORY.md` | High: sparse speech, family/home/scarf wording, object-action relation, cabin/final address. |
| `AOT_04_ARMIN_ARLERT_KNOWLEDGE_IMAGINATION_DIALOGUE_AND_RESPONSIBILITY.md` | High: epistemic hedging, possibility, dialogue/negotiation, deception, proof/narrative diplomacy. |
| `AOT_05_REINER_BRAUN_ROLE_IDENTITY_GUILT_RECOGNITION_AND_SURVIVAL.md` | High: 戦士/兵士, identity substitution, responsibility/exculpation, partner address. |
| `AOT_06_ZEKE_JAEGER_FAMILY_SALVATION_ANTINATALISM_AND_INSTRUMENTAL_REASON.md` | High: salvation vocabulary, brother/royal jurisdiction, free will, ordinary catch revision. |
| `AOT_07_HISTORIA_YMIR_IDENTITY_SOVEREIGNTY_AND_CHOSEN_OBLIGATION.md` | High: naming, sacred authority, personhood, sacrifice/reproduction language, Ymir wording limits. |
| `AOT_08_LEVI_ERWIN_HANGE_COMMAND_SACRIFICE_AND_SUCCESSION.md` | High: choice/uncertainty, command formulae, public/private Erwin register, Hange grief/understanding. |
| `AOT_09_104TH_WARRIORS_AND_GENERATIONAL_ENSEMBLE_BELONGING_BETRAYAL_AND_REPAIR.md` | Moderate-high: 仲間/裏切り者, ordinary-peer registers, Gabi category revision. |
| `AOT_10_STATES_EMPIRE_NATIONALISM_LEGITIMACY_AND_POLITICAL_VIOLENCE.md` | Moderate-high: empire/hero/devil/good-Eldian/state-legitimacy terminology. |
| `AOT_12_RACE_MEMORY_HISTORY_PROPAGANDA_AND_ENEMY_CONSTRUCTION.md` | High: truth, story, devil/person categories, ethnonyms, source-position language. |
| `AOT_13_TITANS_PATHS_BODY_MEMORY_INHERITANCE_AND_PERSONHOOD_ONTOLOGY.md` | High: 道/座標/始祖/地鳴らし and uncertainty around mechanism terms. |
| `AOT_14_FREEDOM_AUTONOMY_PERSONHOOD_INHERITANCE_AND_RESPONSIBILITY.md` | Highest: 自由/自由意志/不自由, 奴隷/家畜, birth, choice, responsibility. |
| `AOT_15_CHILDHOOD_HOME_FAMILY_ORDINARY_LIFE_AND_THE_FUTURE.md` | High: 子供/未来/普通/幸せ/なんでもない一瞬/home-return language. |
| `AOT_16_RELATIONSHIPS_LOVE_LOYALTY_RECOGNITION_BETRAYAL_AND_NONPOSSESSION.md` | High: 家族/仲間/相棒, trust/deception, recognition-without-deescalation, scarf/home language. |
| `AOT_17_JAPANESE_LANGUAGE_NAMES_REGISTER_KEY_TERMS_AND_TRANSLATION_SENSITIVITIES.md` | Primary consumer of this index; should reopen every wording-dependent anchor rather than merely summarize this document. |
| `AOT_19_ENDING_CAUSALITY_MEMORY_HISTORICAL_RECURRENCE_AND_POSTWAR_TIME.md` | Highest: V30–V34 causal/temporal statements, terminal motive language, Ymir-love wording, epilogue recurrence. |

## IX. Appendix A — locator-backed and supplemental Japanese seed registry

The table below is the machine-like retrieval core of this Markdown index. It deliberately preserves evidence IDs and verification states. `PENDING` means “do not invent the missing page”; it does **not** mean the wording/evidence row is analytically unusable.

| JP ID | Volume | Chapter | Short Japanese anchor | Anchor class | Evidence | Locator | Claims | Specialist docs | Verification | Priority |
|---|---|---|---|---|---|---|---|---|---|---|
| `AOT-JP-001` | V01 | 第1話 二千年後の君へ | 「いってらっしゃい エレン」 | QUOTED_SHORT_ANCHOR | `AOT_V01_E001` | AOT-LOC-01-001 |  | 02,03,04 | CHAPTER_VERIFIED_PAGE_PENDING | P1 |
| `AOT-JP-002` | V01 | 第1話 二千年後の君へ | 家畜 | LEXICAL_ANCHOR | `AOT_V01_E003` | AOT-LOC-01-003 |  | 02,03,04 | CHAPTER_VERIFIED_PAGE_PENDING | P1 |
| `AOT-JP-003` | V01 | 第2話 その日 | 「駆逐してやる!!」 | QUOTED_SHORT_ANCHOR | `AOT_V01_E004` | AOT-LOC-01-004 |  | 02,03,04 | CHAPTER_VERIFIED_PAGE_PENDING | P1 |
| `AOT-JP-004` | V02 | 第6話 少女が見た世界 | 「この世界は残酷だ…そして…とても美しい」 | QUOTED_SHORT_ANCHOR | `AOT_V02_E001` | AOT-LOC-02-001 |  | 02,03,04 | CHAPTER_VERIFIED_PAGE_PENDING | P1 |
| `AOT-JP-005` | V02 | 第6話 少女が見た世界 | 「戦え」 | QUOTED_SHORT_ANCHOR | `AOT_V02_E002` | AOT-LOC-02-002 |  | 02,03,04 | CHAPTER_VERIFIED_PAGE_PENDING | P1 |
| `AOT-JP-006` | V03 | 第11話 応える | 「人か？ 巨人か？」 / 「人間です」 | QUOTED_SHORT_ANCHOR | `AOT_V03_E002` | AOT-LOC-03-002 |  | 02,03,04 | CHAPTER_VERIFIED_PAGE_PENDING | P1 |
| `AOT-JP-007` | V04 | 第14話 原初的欲求 | 「オレが!! この世に生まれたからだ!!」 | QUOTED_SHORT_ANCHOR | `AOT_V04_E001` | AOT-LOC-04-001 |  | 02,04,09 | CHAPTER_VERIFIED_PAGE_PENDING | P1 |
| `AOT-JP-008` | V04 | 第16話 必要 | 「命を投げうつことだけが戦うことじゃない」 | QUOTED_SHORT_ANCHOR | `AOT_V04_E004` | AOT-LOC-04-004 |  | 02,04,09 | CHAPTER_VERIFIED_PAGE_PENDING | P1 |
| `AOT-JP-009` | V04 | 第17話 武力幻想 | 「兵士ごっこ」 | QUOTED_SHORT_ANCHOR | `AOT_V04_E005` | AOT-LOC-04-005 |  | 02,04,09 | CHAPTER_VERIFIED_PAGE_PENDING | P1 |
| `AOT-JP-010` | V05 | 特別編 イルゼの手帳 | 「ユミルの民」 / 「ユミル様」 | QUOTED_SHORT_ANCHOR | `AOT_V05_E001` | AOT-LOC-05-001 |  | 02,08 | CHAPTER_VERIFIED_PAGE_PENDING | P1 |
| `AOT-JP-011` | V05 | 特別編 イルゼの手帳 | 「イルゼ・ラングナーの戦果だ」 | QUOTED_SHORT_ANCHOR | `AOT_V05_E002` | AOT-LOC-05-002 |  | 02,08 | CHAPTER_VERIFIED_PAGE_PENDING | P1 |
| `AOT-JP-012` | V05 | 第19話 まだ目を見れない | 「全部オレに投資しろ!!」 | QUOTED_SHORT_ANCHOR | `AOT_V05_E003` | AOT-LOC-05-003 |  | 02,08 | CHAPTER_VERIFIED_PAGE_PENDING | P1 |
| `AOT-JP-013` | V05 | 第20話 特別作戦班 | 「違う視点から巨人を見てみたい」 | QUOTED_SHORT_ANCHOR | `AOT_V05_E005` | AOT-LOC-05-005 |  | 02,08 | CHAPTER_VERIFIED_PAGE_PENDING | P1 |
| `AOT-JP-014` | V05 | 第22話 長距離索敵陣形 | 「知性」 | QUOTED_SHORT_ANCHOR | `AOT_V05_E008` | AOT-LOC-05-008 |  | 02,08 | CHAPTER_VERIFIED_PAGE_PENDING | P1 |
| `AOT-JP-015` | V06 | 第25話 噛みつく | 「私達を信じて」 | QUOTED_SHORT_ANCHOR | `AOT_V06_E003` | AOT-LOC-06-003 |  | 02,04,05,08 | CHAPTER_VERIFIED_PAGE_PENDING | P1 |
| `AOT-JP-016` | V06 | 第25話 噛みつく | 「俺にはわからない」 | QUOTED_SHORT_ANCHOR | `AOT_V06_E004` | AOT-LOC-06-004 |  | 02,04,05,08 | CHAPTER_VERIFIED_PAGE_PENDING | P1 |
| `AOT-JP-017` | V06 | 第25話 噛みつく | 「悔いが残らない方を自分で選べ」 | QUOTED_SHORT_ANCHOR | `AOT_V06_E005` | AOT-LOC-06-005 |  | 02,04,05,08 | CHAPTER_VERIFIED_PAGE_PENDING | P1 |
| `AOT-JP-018` | V06 | 第26話 好都合な道を | 「都合がいいから」 | QUOTED_SHORT_ANCHOR | `AOT_V06_E007` | AOT-LOC-06-007 |  | 02,04,05,08 | CHAPTER_VERIFIED_PAGE_PENDING | P1 |
| `AOT-JP-019` | V07 | 第27話 エルヴィン・スミス | 「結果を知った後で…」 | QUOTED_SHORT_ANCHOR | `AOT_V07_E001` | AOT-LOC-07-001 |  | 02,03,04,08 | CHAPTER_VERIFIED_PAGE_PENDING | P1 |
| `AOT-JP-020` | V07 | 第27話 エルヴィン・スミス | 「100人の仲間の命を切り捨てる」 | QUOTED_SHORT_ANCHOR | `AOT_V07_E002` | AOT-LOC-07-002 |  | 02,03,04,08 | CHAPTER_VERIFIED_PAGE_PENDING | P1 |
| `AOT-JP-021` | V07 | 第27話 エルヴィン・スミス | 「人間性をも捨てる」 | QUOTED_SHORT_ANCHOR | `AOT_V07_E003` | AOT-LOC-07-003 |  | 02,03,04,08 | CHAPTER_VERIFIED_PAGE_PENDING | P1 |
| `AOT-JP-022` | V07 | 第28話 選択と結果 | 「オレが選択を間違えた」 | QUOTED_SHORT_ANCHOR | `AOT_V07_E005` | AOT-LOC-07-005 |  | 02,03,04,08 | CHAPTER_VERIFIED_PAGE_PENDING | P1 |
| `AOT-JP-023` | V07 | 第30話 敗者達 | 「作戦の本質を見失うな」 | QUOTED_SHORT_ANCHOR | `AOT_V07_E007` | AOT-LOC-07-007 |  | 02,03,04,08 | CHAPTER_VERIFIED_PAGE_PENDING | P1 |
| `AOT-JP-024` | V08 | 第31話 微笑み | 「良い人」 / 「都合の良い人」 | QUOTED_SHORT_ANCHOR | `AOT_V08_E002` | AOT-LOC-08-002 |  | 02,03,04,08,09 | CHAPTER_VERIFIED_PAGE_PENDING | P1 |
| `AOT-JP-025` | V08 | 第33話 壁 | 「帰ってくるって約束してくれ」 | QUOTED_SHORT_ANCHOR | `AOT_V08_E006` | AOT-LOC-08-006 |  | 02,03,04,08,09 | CHAPTER_VERIFIED_PAGE_PENDING | P1 |
| `AOT-JP-026` | V08 | 第34話 戦士は踊る | 「光を遮る」 | QUOTED_SHORT_ANCHOR | `AOT_V08_E008` | AOT-LOC-08-008 |  | 02,03,04,08,09 | CHAPTER_VERIFIED_PAGE_PENDING | P1 |
| `AOT-JP-027` | V09 | 第35話 獣の巨人 | 「同じ言語のはずなんだが」 | QUOTED_SHORT_ANCHOR | `AOT_V09_E001` | AOT-LOC-09-001 |  | 05,07,09 | CHAPTER_VERIFIED_PAGE_PENDING | P1 |
| `AOT-JP-028` | V09 | 第35話 獣の巨人 | 「あ もう動いていいよ」 | QUOTED_SHORT_ANCHOR | `AOT_V09_E002` | AOT-LOC-09-002 |  | 05,07,09 | CHAPTER_VERIFIED_PAGE_PENDING | P1 |
| `AOT-JP-029` | V09 | 第36話 ただいま | 「我々は世界に生かしてもらっとる」 | QUOTED_SHORT_ANCHOR | `AOT_V09_E003` | AOT-LOC-09-003 |  | 05,07,09 | CHAPTER_VERIFIED_PAGE_PENDING | P1 |
| `AOT-JP-030` | V09 | 第36話 ただいま | 「走らんかい!!」 | QUOTED_SHORT_ANCHOR | `AOT_V09_E004` | AOT-LOC-09-004 |  | 05,07,09 | CHAPTER_VERIFIED_PAGE_PENDING | P1 |
| `AOT-JP-031` | V09 | 第36話 ただいま | 「ただいま」 | QUOTED_SHORT_ANCHOR | `AOT_V09_E005` | AOT-LOC-09-005 |  | 05,07,09 | CHAPTER_VERIFIED_PAGE_PENDING | P1 |
| `AOT-JP-032` | V09 | 第37話 南西へ | 「おかえり」 | QUOTED_SHORT_ANCHOR | `AOT_V09_E006` | AOT-LOC-09-006 |  | 05,07,09 | CHAPTER_VERIFIED_PAGE_PENDING | P1 |
| `AOT-JP-033` | V10 | 第40話 ユミル | 「彼らの死を利用するな」 | QUOTED_SHORT_ANCHOR | `AOT_V10_E002` | AOT-LOC-10-002 |  | 02,03,05,07,09 | CHAPTER_VERIFIED_PAGE_PENDING | P1 |
| `AOT-JP-034` | V10 | 第40話 ユミル | 「元の名前を名乗って生きろ」 | QUOTED_SHORT_ANCHOR | `AOT_V10_E003` | AOT-LOC-10-003 |  | 02,03,05,07,09 | CHAPTER_VERIFIED_PAGE_PENDING | P1 |
| `AOT-JP-035` | V10 | 第41話 ヒストリア | 「私の名前…ヒストリアって言うの」 | QUOTED_SHORT_ANCHOR | `AOT_V10_E004` | AOT-LOC-10-004 |  | 02,03,05,07,09 | CHAPTER_VERIFIED_PAGE_PENDING | P1 |
| `AOT-JP-036` | V10 | 第42話 戦士 | 「俺が鎧の巨人で こいつが超大型巨人」 | QUOTED_SHORT_ANCHOR | `AOT_V10_E006` | AOT-LOC-10-006 |  | 02,03,05,07,09 | CHAPTER_VERIFIED_PAGE_PENDING | P1 |
| `AOT-JP-037` | V10 | 第42話 戦士 | 「戦士として 最後まで責任を果たす」 | QUOTED_SHORT_ANCHOR | `AOT_V10_E007` | AOT-LOC-10-007 |  | 02,03,05,07,09 | CHAPTER_VERIFIED_PAGE_PENDING | P1 |
| `AOT-JP-038` | V11 | 第43話 鎧の巨人 | 「本当に気持ち悪いよ」 / 「駆除してやる」 | QUOTED_SHORT_ANCHOR | `AOT_V11_E001` | AOT-LOC-11-001 |  | 02,03,04,05,09 | CHAPTER_VERIFIED_PAGE_PENDING | P1 |
| `AOT-JP-039` | V11 | 第45話 追う者 | 「俺は…あの日常が好きだ」 | QUOTED_SHORT_ANCHOR | `AOT_V11_E003` | AOT-LOC-11-003 |  | 02,03,04,05,09 | CHAPTER_VERIFIED_PAGE_PENDING | P1 |
| `AOT-JP-040` | V11 | 第46話 開口 | Reiner; split identity; 兵士 | LEXICAL_ANCHOR | `AOT_V11_E004` | AOT-LOC-11-004 |  | 02,03,04,05,09 | CHAPTER_VERIFIED_PAGE_PENDING | P1 |
| `AOT-JP-041` | V11 | 第46話 開口 | 「兵士じゃないだろ…僕らは戦士なんだから」 | QUOTED_SHORT_ANCHOR | `AOT_V11_E005` | AOT-LOC-11-005 |  | 02,03,04,05,09 | CHAPTER_VERIFIED_PAGE_PENDING | P1 |
| `AOT-JP-042` | V11 | 第46話 開口 | 「気の毒だと思ったよ」 | QUOTED_SHORT_ANCHOR | `AOT_V11_E006` | AOT-LOC-11-006 |  | 02,03,04,05,09 | CHAPTER_VERIFIED_PAGE_PENDING | P1 |
| `AOT-JP-043` | V11 | 第46話 開口 | 「ただの人殺し」 / 「もう人間じゃねぇ」 | QUOTED_SHORT_ANCHOR | `AOT_V11_E007` | AOT-LOC-11-007 |  | 02,03,04,05,09 | CHAPTER_VERIFIED_PAGE_PENDING | P1 |
| `AOT-JP-044` | V11 | 第46話 開口 | 「お前はこの世界に先があると思うのか？」 | QUOTED_SHORT_ANCHOR | `AOT_V11_E008` | AOT-LOC-11-008 |  | 02,03,04,05,09 | CHAPTER_VERIFIED_PAGE_PENDING | P1 |
| `AOT-JP-045` | V12 | 第47話 子供達 | 「60年ぐらいだ」 / 「終わらない悪夢」 | QUOTED_SHORT_ANCHOR | `AOT_V12_E001` | AOT-LOC-12-001 |  | 02,03,04,05,07,08,09 | CHAPTER_VERIFIED_PAGE_PENDING | P1 |
| `AOT-JP-046` | V12 | 第48話 誰か | 「すべてが嘘じゃない！」 | QUOTED_SHORT_ANCHOR | `AOT_V12_E002` | AOT-LOC-12-002 |  | 02,03,04,05,07,08,09 | CHAPTER_VERIFIED_PAGE_PENDING | P1 |
| `AOT-JP-047` | V12 | 第48話 誰か | 「誰か僕らを見つけてくれ」 | QUOTED_SHORT_ANCHOR | `AOT_V12_E003` | AOT-LOC-12-003 |  | 02,03,04,05,07,08,09 | CHAPTER_VERIFIED_PAGE_PENDING | P1 |
| `AOT-JP-048` | V12 | 第49話 突撃 | 「進め!!」 | QUOTED_SHORT_ANCHOR | `AOT_V12_E005` | AOT-LOC-12-005 |  | 02,03,04,05,07,08,09 | CHAPTER_VERIFIED_PAGE_PENDING | P1 |
| `AOT-JP-049` | V12 | 第50話 叫び | 「何度でも巻いてやる」 | QUOTED_SHORT_ANCHOR | `AOT_V12_E007` | AOT-LOC-12-007 |  | 02,03,04,05,07,08,09 | CHAPTER_VERIFIED_PAGE_PENDING | P1 |
| `AOT-JP-050` | V12 | 第50話 叫び | 「座標」 | QUOTED_SHORT_ANCHOR | `AOT_V12_E008` | AOT-LOC-12-008 |  | 02,03,04,05,07,08,09 | CHAPTER_VERIFIED_PAGE_PENDING | P1 |
| `AOT-JP-051` | V12 | 第50話 叫び | 「お前の声が聞こえちまったからかな」 | QUOTED_SHORT_ANCHOR | `AOT_V12_E009` | AOT-LOC-12-009 |  | 02,03,04,05,07,08,09 | CHAPTER_VERIFIED_PAGE_PENDING | P1 |
| `AOT-JP-052` | V13 | 第51話 リヴァイ班 | 「活かすか殺すかは お前次第」 | QUOTED_SHORT_ANCHOR | `AOT_V13_E001` | AOT-LOC-13-001 |  | 02,07,08,09 | CHAPTER_VERIFIED_PAGE_PENDING | P1 |
| `AOT-JP-053` | V13 | 第51話 リヴァイ班 | 「つまり巨人の正体は 人間であると」 | QUOTED_SHORT_ANCHOR | `AOT_V13_E003` | AOT-LOC-13-003 |  | 02,07,08,09 | CHAPTER_VERIFIED_PAGE_PENDING | P1 |
| `AOT-JP-054` | V13 | 第52話 クリスタ・レンズ | 「こいつを殺す勇気が…」 | QUOTED_SHORT_ANCHOR | `AOT_V13_E004` | AOT-LOC-13-004 |  | 02,07,08,09 | CHAPTER_VERIFIED_PAGE_PENDING | P1 |
| `AOT-JP-055` | V13 | 第52話 クリスタ・レンズ | 「君の名は クリスタ・レンズだ」 | QUOTED_SHORT_ANCHOR | `AOT_V13_E005` | AOT-LOC-13-005 |  | 02,07,08,09 | CHAPTER_VERIFIED_PAGE_PENDING | P1 |
| `AOT-JP-056` | V13 | 第53話 狼煙 | 「誰が選ぶ？」 | QUOTED_SHORT_ANCHOR | `AOT_V13_E007` | AOT-LOC-13-007 |  | 02,07,08,09 | CHAPTER_VERIFIED_PAGE_PENDING | P1 |
| `AOT-JP-057` | V13 | 第54話 反撃の場所 | 「別にお前は普通だよ」 | QUOTED_SHORT_ANCHOR | `AOT_V13_E008` | AOT-LOC-13-008 |  | 02,07,08,09 | CHAPTER_VERIFIED_PAGE_PENDING | P1 |
| `AOT-JP-058` | V13 | 第54話 反撃の場所 | 「王政を打倒し」 / 「実権を握る」 | QUOTED_SHORT_ANCHOR | `AOT_V13_E009` | AOT-LOC-13-009 |  | 02,07,08,09 | CHAPTER_VERIFIED_PAGE_PENDING | P1 |
| `AOT-JP-059` | V14 | 第55話 痛み | 「部下を人同士の争いに導くような権利は無い」 | QUOTED_SHORT_ANCHOR | `AOT_V14_E001` | AOT-LOC-14-001 |  | 04,07,08,09 | CHAPTER_VERIFIED_PAGE_PENDING | P1 |
| `AOT-JP-060` | V14 | 第55話 痛み | 「父の仮説は私の中で真実となり」 | QUOTED_SHORT_ANCHOR | `AOT_V14_E002` | AOT-LOC-14-002 |  | 04,07,08,09 | CHAPTER_VERIFIED_PAGE_PENDING | P1 |
| `AOT-JP-061` | V14 | 第55話 痛み | 「俺達第一憲兵が この汚ぇ手で守ってきた」 | QUOTED_SHORT_ANCHOR | `AOT_V14_E003` | AOT-LOC-14-003 |  | 04,07,08,09 | CHAPTER_VERIFIED_PAGE_PENDING | P1 |
| `AOT-JP-062` | V14 | 第56話 役者 | 「私の…次の役は 女王ですね」 | QUOTED_SHORT_ANCHOR | `AOT_V14_E004` | AOT-LOC-14-004 |  | 04,07,08,09 | CHAPTER_VERIFIED_PAGE_PENDING | P1 |
| `AOT-JP-063` | V14 | 第57話 切り裂きケニー | 「エレンは器であって 交換可能な存在」 | QUOTED_SHORT_ANCHOR | `AOT_V14_E005` | AOT-LOC-14-005 |  | 04,07,08,09 | CHAPTER_VERIFIED_PAGE_PENDING | P1 |
| `AOT-JP-064` | V14 | 第57話 切り裂きケニー | 「思えば俺の思考はヤツの影響が強い」 | QUOTED_SHORT_ANCHOR | `AOT_V14_E006` | AOT-LOC-14-006 |  | 04,07,08,09 | CHAPTER_VERIFIED_PAGE_PENDING | P1 |
| `AOT-JP-065` | V14 | 第57話 切り裂きケニー | 「お前だっててめぇのために殺すだろ？」 / 「ああ」 | QUOTED_SHORT_ANCHOR | `AOT_V14_E007` | AOT-LOC-14-007 |  | 04,07,08,09 | CHAPTER_VERIFIED_PAGE_PENDING | P1 |
| `AOT-JP-066` | V15 | 第59話 外道の魂 | 「お前の手はもう汚れちまった」 / 「ありがとう」 | QUOTED_SHORT_ANCHOR | `AOT_V15_E001` | AOT-LOC-15-001 |  | 02,04,07,08 | CHAPTER_VERIFIED_PAGE_PENDING | P1 |
| `AOT-JP-067` | V15 | 第59話 外道の魂 | 「お前は本当に間違っていたのか？」 | QUOTED_SHORT_ANCHOR | `AOT_V15_E002` | AOT-LOC-15-002 |  | 02,04,07,08 | CHAPTER_VERIFIED_PAGE_PENDING | P1 |
| `AOT-JP-068` | V15 | 第60話 信頼 | 「何が事実かを決めるのは王政だ」 | QUOTED_SHORT_ANCHOR | `AOT_V15_E003` | AOT-LOC-15-003 |  | 02,04,07,08 | CHAPTER_VERIFIED_PAGE_PENDING | P1 |
| `AOT-JP-069` | V15 | 第61話 回答 | 「ならば俺はウォール・ローゼ側の人間だ」 | QUOTED_SHORT_ANCHOR | `AOT_V15_E004` | AOT-LOC-15-004 |  | 02,04,07,08 | CHAPTER_VERIFIED_PAGE_PENDING | P1 |
| `AOT-JP-070` | V15 | 第61話 回答 | 「一人一人の選択が この世界を変えたんだ」 | QUOTED_SHORT_ANCHOR | `AOT_V15_E005` | AOT-LOC-15-005 |  | 02,04,07,08 | CHAPTER_VERIFIED_PAGE_PENDING | P1 |
| `AOT-JP-071` | V15 | 第62話 罪 | 「父親の罪を」 | QUOTED_SHORT_ANCHOR | `AOT_V15_E009` | AOT-LOC-15-009 |  | 02,04,07,08 | CHAPTER_VERIFIED_PAGE_PENDING | P1 |
| `AOT-JP-072` | V16 | 第66話 願い | 「初代王の思想に支配される」 | QUOTED_SHORT_ANCHOR | `AOT_V16_E005` | AOT-LOC-16-005 |  | 02,03,07,08 | CHAPTER_VERIFIED_PAGE_PENDING | P1 |
| `AOT-JP-073` | V16 | 第66話 願い | 「何が神だ!!」 | QUOTED_SHORT_ANCHOR | `AOT_V16_E006` | AOT-LOC-16-006 |  | 02,03,07,08 | CHAPTER_VERIFIED_PAGE_PENDING | P1 |
| `AOT-JP-074` | V16 | 第66話 願い | 「私は人類の敵…エレンの味方」 | QUOTED_SHORT_ANCHOR | `AOT_V16_E007` | AOT-LOC-16-007 |  | 02,03,07,08 | CHAPTER_VERIFIED_PAGE_PENDING | P1 |
| `AOT-JP-075` | V16 | 第66話 願い | 「最後に一度だけ…自分を信じることを」 | QUOTED_SHORT_ANCHOR | `AOT_V16_E008` | AOT-LOC-16-008 |  | 02,03,07,08 | CHAPTER_VERIFIED_PAGE_PENDING | P1 |
| `AOT-JP-076` | V16 | 第66話 願い | 「ヨロイ」 | QUOTED_SHORT_ANCHOR | `AOT_V16_E009` | AOT-LOC-16-009 |  | 02,03,07,08 | CHAPTER_VERIFIED_PAGE_PENDING | P1 |
| `AOT-JP-077` | V17 | 第67話 オルブド区外壁 | 「むしろ…始祖の巨人を取り上げている今の状態こそ」 | QUOTED_SHORT_ANCHOR | `AOT_V17_E001` | AOT-LOC-17-001 |  | 02,07,08 | CHAPTER_VERIFIED_PAGE_PENDING | P1 |
| `AOT-JP-078` | V17 | 第68話 壁の王 | 「自分の果たすべき使命を自分で見つけた」 | QUOTED_SHORT_ANCHOR | `AOT_V17_E003` | AOT-LOC-17-003 |  | 02,07,08 | CHAPTER_VERIFIED_PAGE_PENDING | P1 |
| `AOT-JP-079` | V17 | 第68話 壁の王 | 「ヒストリア・レイス この壁の真の王です」 | QUOTED_SHORT_ANCHOR | `AOT_V17_E004` | AOT-LOC-17-004 |  | 02,07,08 | CHAPTER_VERIFIED_PAGE_PENDING | P1 |
| `AOT-JP-080` | V17 | 第69話 友人 | 「みんな…何かの奴隷だった」 | QUOTED_SHORT_ANCHOR | `AOT_V17_E006` | AOT-LOC-17-006 |  | 02,07,08 | CHAPTER_VERIFIED_PAGE_PENDING | P1 |
| `AOT-JP-081` | V17 | 第69話 友人 | 「ただの…兄貴だ」 / 「人の親にはなれねぇ」 | QUOTED_SHORT_ANCHOR | `AOT_V17_E007` | AOT-LOC-17-007 |  | 02,07,08 | CHAPTER_VERIFIED_PAGE_PENDING | P1 |
| `AOT-JP-082` | V18 | 第71話 傍観者 | 「特別じゃなきゃいけないんですか？」 | QUOTED_SHORT_ANCHOR | `AOT_V18_E002` | AOT-LOC-18-002 |  | 02,04,05,08 | CHAPTER_VERIFIED_PAGE_PENDING | P1 |
| `AOT-JP-083` | V18 | 第71話 傍観者 | 「この世界に 生まれて来てくれたんだから」 | QUOTED_SHORT_ANCHOR | `AOT_V18_E003` | AOT-LOC-18-003 |  | 02,04,05,08 | CHAPTER_VERIFIED_PAGE_PENDING | P1 |
| `AOT-JP-084` | V18 | 第72話 奪還作戦の夜 | 「人類の勝利より？」 / 「……ああ」 | QUOTED_SHORT_ANCHOR | `AOT_V18_E005` | AOT-LOC-18-005 |  | 02,04,05,08 | CHAPTER_VERIFIED_PAGE_PENDING | P1 |
| `AOT-JP-085` | V18 | 第73話 はじまりの街 | 「そこで初めて知ったんだ オレは不自由なんだって」 | QUOTED_SHORT_ANCHOR | `AOT_V18_E007` | AOT-LOC-18-007 |  | 02,04,05,08 | CHAPTER_VERIFIED_PAGE_PENDING | P1 |
| `AOT-JP-086` | V18 | 第73話 はじまりの街 | 「オレ達ならできる」 / 「皆 特別で 自由」 | QUOTED_SHORT_ANCHOR | `AOT_V18_E008` | AOT-LOC-18-008 |  | 02,04,05,08 | CHAPTER_VERIFIED_PAGE_PENDING | P1 |
| `AOT-JP-087` | V19 | Ch75 | 「イヤ迷うな 先に殺すのは馬だ」 | QUOTED_SHORT_ANCHOR | `AOT_V19_E004` | AOT-LOC-19-004 / page0028 |  | 02,04,05,08,09 | CANONICAL_DEEP_READING_LOCATOR | P2 |
| `AOT-JP-088` | V19 | Ch77 | 「証明」 | QUOTED_SHORT_ANCHOR | `AOT_V19_E010` | AOT-LOC-19-010 / page0106-page0110 |  | 02,04,05,08,09 | CANONICAL_DEEP_READING_LOCATOR | P2 |
| `AOT-JP-089` | V19 | Ch77 | 「戦士長」 | QUOTED_SHORT_ANCHOR | `AOT_V19_E013` | AOT-LOC-19-013 / page0119-page0123 |  | 02,04,05,08,09 | CANONICAL_DEEP_READING_LOCATOR | P2 |
| `AOT-JP-090` | V19 | Ch78 | 「話をしよう」 / 「僕が決めた」 | QUOTED_SHORT_ANCHOR | `AOT_V19_E017` | AOT-LOC-19-017 / page0156-page0160 |  | 02,04,05,08,09 | CANONICAL_DEEP_READING_LOCATOR | P2 |
| `AOT-JP-091` | V19 | Ch78 | 「君達は大切な仲間だ ちゃんと殺そうと思ってる」 | QUOTED_SHORT_ANCHOR | `AOT_V19_E019` | AOT-LOC-19-019 / page0165 |  | 02,04,05,08,09 | CANONICAL_DEEP_READING_LOCATOR | P2 |
| `AOT-JP-092` | V19 | Ch78 | 「まるで別人に見えた」 / 「僕もだ」 | QUOTED_SHORT_ANCHOR | `AOT_V19_E023` | AOT-LOC-19-023 / page0172 |  | 02,04,05,08,09 | CANONICAL_DEEP_READING_LOCATOR | P2 |
| `AOT-JP-093` | V19 | Ch78 | 「ハンジ班は!?」 | QUOTED_SHORT_ANCHOR | `AOT_V19_E027` | AOT-LOC-19-027 / page0185-page0188 |  | 02,04,05,08,09 | CANONICAL_DEEP_READING_LOCATOR | P2 |
| `AOT-JP-094` | V22 | Ch88 | 「これは お前が始めた物語だろ」 | QUOTED_SHORT_ANCHOR | `AOT_V22_E011` | AOT-LOC-22-011 / page0091 |  | 02,04,07,08 | CANONICAL_DEEP_READING_LOCATOR | P2 |
| `AOT-JP-095` | V23 | Ch92 | 「また壁かよ」 | QUOTED_SHORT_ANCHOR | `AOT_V23_E008` | AOT-LOC-23-008 / page0080 | AOT-FSCR-C015 | 05 | CANONICAL_DEEP_READING_LOCATOR | P2 |
| `AOT-JP-096` | V24 | Ch95 | 世界はもうエルディア人を人権の定義に当てはめる必要は無い` | TRANSCRIBED_LEXICAL_ANCHOR | `AOT_V24_E001` | AOT-LOC-24-001 / page0017.jpeg |  | 02,05,06,09 | CANONICAL_DEEP_READING_LOCATOR | P2 |
| `AOT-JP-097` | V24 | Ch95 | `ふざけるな!!` / `エルディアの悪魔の親子` | TRANSCRIBED_LEXICAL_ANCHOR | `AOT_V24_E004` | AOT-LOC-24-004 / page0039.jpeg |  | 02,05,06,09 | CANONICAL_DEEP_READING_LOCATOR | P2 |
| `AOT-JP-098` | V24 | Ch97 | `銅像の中は空洞` | TRANSCRIBED_LEXICAL_ANCHOR | `AOT_V24_E024` | AOT-LOC-24-024 / page0135.jpeg |  | 02,05,06,09 | CANONICAL_DEEP_READING_LOCATOR | P2 |
| `AOT-JP-099` | V24 | Ch98 | northern route / 32 lost ships; `ファルコまで巨人にならなくたって… | TRANSCRIBED_LEXICAL_ANCHOR | `AOT_V24_E026` | AOT-LOC-24-026 / page0144.jpeg |  | 02,05,06,09 | CANONICAL_DEEP_READING_LOCATOR | P2 |
| `AOT-JP-100` | V24 | Ch98 | `あなたがどんな目に遭うかわからない` | TRANSCRIBED_LEXICAL_ANCHOR | `AOT_V24_E032` | AOT-LOC-24-032 / page0171.jpeg |  | 02,05,06,09 | CANONICAL_DEEP_READING_LOCATOR | P2 |
| `AOT-JP-101` | V24 | Ch98 | `4年振りだな ライナー` | TRANSCRIBED_LEXICAL_ANCHOR | `AOT_V24_E034` | AOT-LOC-24-034 / page0179.jpeg |  | 02,05,06,09 | CANONICAL_DEEP_READING_LOCATOR | P2 |
| `AOT-JP-102` | V25 | Ch100 | 敵と同じ屋根の下で | TRANSCRIBED_LEXICAL_ANCHOR | `AOT_V25_E008` | AOT-LOC-25-008 / page0075.jpeg | AOT-FSCR-C001 | 02 | CANONICAL_DEEP_READING_LOCATOR | P2 |
| `AOT-JP-103` | V25 | Ch101 | `お願い…帰ってきて` | TRANSCRIBED_LEXICAL_ANCHOR | `AOT_V25_E020` | AOT-LOC-25-020 / page0141.jpeg | AOT-FSCR-C017,AOT-FSCR-C019 | 03,16 | CANONICAL_DEEP_READING_LOCATOR | P2 |
| `AOT-JP-104` | V25 | Ch102 | `この戦いの先に何があるのか / それを見極めるためには…生き残らねぇと` | TRANSCRIBED_LEXICAL_ANCHOR | `AOT_V25_E029` | AOT-LOC-25-029 / page0164.jpeg |  | 02,03,05,09 | CANONICAL_DEEP_READING_LOCATOR | P2 |
| `AOT-JP-105` | V25 | Ch102 | `逃がすな / 殲滅しろ` / `死ぬな / 生き延びろ` | TRANSCRIBED_LEXICAL_ANCHOR | `AOT_V25_E034` | AOT-LOC-25-034 / page0185.jpeg |  | 02,03,05,09 | CANONICAL_DEEP_READING_LOCATOR | P2 |
| `AOT-JP-106` | V26 | Ch105 | 「凶弾」 | QUOTED_SHORT_ANCHOR | `AOT_V26_E012` | AOT-LOC-26-012 / page0098 | AOT-FSCR-C011 | 14 | CANONICAL_DEEP_READING_LOCATOR | P2 |
| `AOT-JP-107` | V26 | Ch105 | Sasha’s death; `肉 | TRANSCRIBED_LEXICAL_ANCHOR | `AOT_V26_E016` | AOT-LOC-26-016 / page0128-page0132 | AOT-FSCR-C032 | 15 | CANONICAL_DEEP_READING_LOCATOR | P2 |
| `AOT-JP-108` | V26 | Ch106 | 戦わなければ | LEXICAL_ANCHOR | `AOT_V26_E029` | AOT-LOC-26-029 / page0188 | AOT-FSCR-C002 | 14 | CANONICAL_DEEP_READING_LOCATOR | P2 |
| `AOT-JP-109` | V27 | Ch108 | officers speculate / Nile `根拠は無いんだな？ | TRANSCRIBED_LEXICAL_ANCHOR | `AOT_V27_E011` | AOT-LOC-27-011 / page0054-page0057 | AOT-FSCR-C030 | 12 | CANONICAL_DEEP_READING_LOCATOR | P2 |
| `AOT-JP-110` | V28 | Ch111 | `服従ではない` | TRANSCRIBED_LEXICAL_ANCHOR | `AOT_V28_E001` | AOT-LOC-28-001 / page0006-page0014 | AOT-FSCR-C023,AOT-FSCR-H007 | 10 | CANONICAL_DEEP_READING_LOCATOR | P2 |
| `AOT-JP-111` | V28 | Ch111 | 子供達はこの森から | LEXICAL_ANCHOR | `AOT_V28_E008` | AOT-LOC-28-008 / page0044-page0045 | AOT-FSCR-C027 | 14 | CANONICAL_DEEP_READING_LOCATOR | P2 |
| `AOT-JP-112` | V28 | Ch112 | ジークがそう言っただけだ | LEXICAL_ANCHOR | `AOT_V28_E013` | AOT-LOC-28-013 / page0053-page0055 | AOT-FSCR-M006 | 08 | CANONICAL_DEEP_READING_LOCATOR | P2 |
| `AOT-JP-113` | V28 | Ch112 | オレは自由だ` | TRANSCRIBED_LEXICAL_ANCHOR | `AOT_V28_E016` | AOT-LOC-28-016 / page0067-page0069 | AOT-FSCR-C002,AOT-FSCR-H001 | 14 | CANONICAL_DEEP_READING_LOCATOR | P2 |
| `AOT-JP-114` | V28 | Ch112 | 無知ほど自由から` | TRANSCRIBED_LEXICAL_ANCHOR | `AOT_V28_E019` | AOT-LOC-28-019 / page0073-page0077 | AOT-FSCR-C030 | 12 | CANONICAL_DEEP_READING_LOCATOR | P2 |
| `AOT-JP-115` | V28 | Ch112 | freedom critique / `誰が…奴隷だ | TRANSCRIBED_LEXICAL_ANCHOR | `AOT_V28_E024` | AOT-LOC-28-024 / page0082-page0083 | AOT-FSCR-C002,AOT-FSCR-H001 | 14 | CANONICAL_DEEP_READING_LOCATOR | P2 |
| `AOT-JP-116` | V28 | Ch114 | お前が みんなを救うんだ | LEXICAL_ANCHOR | `AOT_V28_E039` | AOT-LOC-28-039 / page0146-page0148 | AOT-FSCR-M009 | 06 | CANONICAL_DEEP_READING_LOCATOR | P2 |
| `AOT-JP-117` | V28 | Ch114 | 見ててくれよ` + detonation + blast-aftermath image | TRANSCRIBED_LEXICAL_ANCHOR | `AOT_V28_E050` | AOT-LOC-28-050 / page0185-page0188 | AOT-FSCR-C010 | 08 | CANONICAL_DEEP_READING_LOCATOR | P2 |
| `AOT-JP-118` | V29 | Ch115 | `兄さん` | TRANSCRIBED_LEXICAL_ANCHOR | `AOT_V29_E006` | AOT-LOC-29-006 / page0021-page0023 | AOT-FSCR-C009,AOT-FSCR-H008 | 06,16 | CANONICAL_DEEP_READING_LOCATOR | P2 |
| `AOT-JP-119` | V30 | Ch120 | Eren grounds refusal in `オレがこの世に生まれたからだ | TRANSCRIBED_LEXICAL_ANCHOR | `AOT_V30_E018` | AOT-LOC-30-018 / page0074-page0075 | AOT-FSCR-C027,AOT-FSCR-H004 | 02,14 | CANONICAL_DEEP_READING_LOCATOR | P0 |
| `AOT-JP-120` | V30 | Ch121 | 未来の継承者の記憶` establishes future-memory access | TRANSCRIBED_LEXICAL_ANCHOR | `AOT_V30_E027` | AOT-LOC-30-027 / page0116-page0117 | AOT-FSCR-C024,AOT-FSCR-C029,AOT-FSCR-C030 | 12,13 | CANONICAL_DEEP_READING_LOCATOR | P0 |
| `AOT-JP-121` | V30 | Ch121 | 進み続けるんだ | TRANSCRIBED_LEXICAL_ANCHOR | `AOT_V30_E030` | AOT-LOC-30-030 / page0123-page0124 | AOT-FSCR-C002 | 14 | CANONICAL_DEEP_READING_LOCATOR | P0 |
| `AOT-JP-122` | V30 | Ch121 | Grisha apologizes to Zeke and says `お前を愛している | TRANSCRIBED_LEXICAL_ANCHOR | `AOT_V30_E034` | AOT-LOC-30-034 / page0132-page0133 | AOT-FSCR-M009 | 06 | CANONICAL_DEEP_READING_LOCATOR | P0 |
| `AOT-JP-123` | V30 | Ch121 | Eren says he saw future-self memory through Grisha four years earlier; `あの景色 | TRANSCRIBED_LEXICAL_ANCHOR | `AOT_V30_E037` | AOT-LOC-30-037 / page0138 | AOT-FSCR-C024,AOT-FSCR-H004 | 02,12 | CANONICAL_DEEP_READING_LOCATOR | P0 |
| `AOT-JP-124` | V30 | Ch122 | `お前は自由だ` | TRANSCRIBED_LEXICAL_ANCHOR | `AOT_V30_E041` | AOT-LOC-30-041 / page0149-page0151 | AOT-FSCR-C029 | 13 | CANONICAL_DEEP_READING_LOCATOR | P0 |
| `AOT-JP-125` | V30 | Ch122 | `起きて働け` | TRANSCRIBED_LEXICAL_ANCHOR | `AOT_V30_E045` | AOT-LOC-30-045 / page0164-page0167 | AOT-FSCR-C029 | 13 | CANONICAL_DEEP_READING_LOCATOR | P0 |
| `AOT-JP-126` | V32 | Ch127 | `俺達はまだ話し合ってない` | TRANSCRIBED_LEXICAL_ANCHOR | `AOT_V32_E009` | AOT-LOC-32-009 / page0033-page0036 | AOT-FSCR-C015,AOT-FSCR-C018,AOT-FSCR-M004 | 05,16 | CANONICAL_DEEP_READING_LOCATOR | P0 |
| `AOT-JP-127` | V32 | Ch128 | `断ります` | TRANSCRIBED_LEXICAL_ANCHOR | `AOT_V32_E020` | AOT-LOC-32-020 / page0066-page0067 | AOT-FSCR-C006,AOT-FSCR-C011,AOT-FSCR-C012,AOT-FSCR-C020 | 04,13,14 | CANONICAL_DEEP_READING_LOCATOR | P0 |
| `AOT-JP-128` | V32 | Ch130 | `世界を滅ぼす` | TRANSCRIBED_LEXICAL_ANCHOR | `AOT_V32_E042` | AOT-LOC-32-042 / page0154-page0155 | AOT-FSCR-C014,AOT-FSCR-H005,AOT-FSCR-H006 | 02,07 | CANONICAL_DEEP_READING_LOCATOR | P0 |
| `AOT-JP-129` | V33 | Ch131 | ガッカリした` confession: populated outside world violated Eren's childhood horizon. | TRANSCRIBED_LEXICAL_ANCHOR | `AOT_V33_E007` | AOT-LOC-33-007 / page0027 | AOT-FSCR-C001,AOT-FSCR-C017,AOT-FSCR-H002,AOT-FSCR-H004,AOT-FSCR-M001 | 02,16 | CANONICAL_DEEP_READING_LOCATOR | P0 |
| `AOT-JP-130` | V33 | Ch131 | `自由だ` | TRANSCRIBED_LEXICAL_ANCHOR | `AOT_V33_E010` | AOT-LOC-33-010 / page0039 | AOT-FSCR-C001,AOT-FSCR-C002 | 02,14 | CANONICAL_DEEP_READING_LOCATOR | P0 |
| `AOT-JP-131` | V33 | Ch132 | `私はもう戦えない` | TRANSCRIBED_LEXICAL_ANCHOR | `AOT_V33_E014` | AOT-LOC-33-014 / page0056 | AOT-FSCR-C013,AOT-FSCR-M008 | 09 | CANONICAL_DEEP_READING_LOCATOR | P0 |
| `AOT-JP-132` | V33 | Ch132 | 理解することをあきらめない姿勢` is named as the defining commander qualification. | TRANSCRIBED_LEXICAL_ANCHOR | `AOT_V33_E022` | AOT-LOC-33-022 / page0082 | AOT-FSCR-C007 | 01 | CANONICAL_DEEP_READING_LOCATOR | P0 |
| `AOT-JP-133` | V33 | Ch132 | `心臓を捧げよ` | TRANSCRIBED_LEXICAL_ANCHOR | `AOT_V33_E023` | AOT-LOC-33-023 / page0083 | AOT-FSCR-C021,AOT-FSCR-H010,AOT-FSCR-M006 | 08,10 | CANONICAL_DEEP_READING_LOCATOR | P0 |
| `AOT-JP-134` | V33 | Ch132 | `素晴らしい` | TRANSCRIBED_LEXICAL_ANCHOR | `AOT_V33_E024` | AOT-LOC-33-024 / page0086 | AOT-FSCR-C008,AOT-FSCR-C031 | 11 | CANONICAL_DEEP_READING_LOCATOR | P0 |
| `AOT-JP-135` | V33 | Ch133 | `俺達は同じだ…ライナー` | TRANSCRIBED_LEXICAL_ANCHOR | `AOT_V33_E029` | AOT-LOC-33-029 / page0105 | AOT-FSCR-C020,AOT-FSCR-H009 | 04 | CANONICAL_DEEP_READING_LOCATOR | P0 |
| `AOT-JP-136` | V33 | Ch133 | `戦え` | TRANSCRIBED_LEXICAL_ANCHOR | `AOT_V33_E036` | AOT-LOC-33-036 / page0119 | AOT-FSCR-C002,AOT-FSCR-H001 | 14 | CANONICAL_DEEP_READING_LOCATOR | P0 |
| `AOT-JP-137` | V34 | Ch137 | `生まれてきたんじゃないか` | TRANSCRIBED_LEXICAL_ANCHOR | `AOT_V34_E017` | AOT-LOC-34-017 / page0103-page0105 | AOT-FSCR-C007,AOT-FSCR-C020,AOT-FSCR-C027,AOT-FSCR-C028,AOT-FSCR-C032,AOT-FSCR-H003,AOT-FSCR-H009,AOT-FSCR-M003,AOT-FSCR-M009 | 01,04,06,14,15 | CANONICAL_DEEP_READING_LOCATOR | P0 |
| `AOT-JP-138` | V34 | Ch137 | `何でもない一瞬` | TRANSCRIBED_LEXICAL_ANCHOR | `AOT_V34_E018` | AOT-LOC-34-018 / page0106-page0107 | AOT-FSCR-C020,AOT-FSCR-C027,AOT-FSCR-C032,AOT-FSCR-M009 | 04,06,14,15 | CANONICAL_DEEP_READING_LOCATOR | P0 |
| `AOT-JP-139` | V34 | Ch139 | `死にたくねぇ` | TRANSCRIBED_LEXICAL_ANCHOR | `AOT_V34_E039` | AOT-LOC-34-039 / page0200-page0204 | AOT-FSCR-C001,AOT-FSCR-C017,AOT-FSCR-M001 | 02,16 | CANONICAL_DEEP_READING_LOCATOR | P0 |
| `AOT-JP-140` | V34 | Ch139 | `やりたかったんだ` | TRANSCRIBED_LEXICAL_ANCHOR | `AOT_V34_E040` | AOT-LOC-34-040 / page0205-page0207 | AOT-FSCR-C001,AOT-FSCR-C002,AOT-FSCR-C024,AOT-FSCR-H001,AOT-FSCR-H004,AOT-FSCR-H006,AOT-FSCR-M001 | 02,12,14 | CANONICAL_DEEP_READING_LOCATOR | P0 |
| `AOT-JP-141` | V34 | Ch139 | `最悪の過ち` | TRANSCRIBED_LEXICAL_ANCHOR | `AOT_V34_E041` | AOT-LOC-34-041 / page0207-page0209 | AOT-FSCR-C002,AOT-FSCR-C009,AOT-FSCR-C011,AOT-FSCR-C012,AOT-FSCR-C018,AOT-FSCR-C020,AOT-FSCR-H001,AOT-FSCR-H002,AOT-FSCR-H009,AOT-FSCR-M003,AOT-FSCR-M011 | 04,14,16,20 | CANONICAL_DEEP_READING_LOCATOR | P0 |
| `AOT-JP-142` | V34 | Ch139 | `僕達の物語` | TRANSCRIBED_LEXICAL_ANCHOR | `AOT_V34_E049` | AOT-LOC-34-049 / page0235-page0242 | AOT-FSCR-C003,AOT-FSCR-C006,AOT-FSCR-C009,AOT-FSCR-C011,AOT-FSCR-C014,AOT-FSCR-C018,AOT-FSCR-C020,AOT-FSCR-C022,AOT-FSCR-C023,AOT-FSCR-C026,AOT-FSCR-C030,AOT-FSCR-C032,AOT-FSCR-H002,AOT-FSCR-H003,AOT-FSCR-H005,AOT-FSCR-H009,AOT-FSCR-H010,AOT-FSCR-M012 | 04,07,10,12,13,14,15,16,20 | CANONICAL_DEEP_READING_LOCATOR | P0 |
| `AOT-JP-143` | V20 | 第80話 名も無き兵士 | 「俺は選ぶぞ」 | SUPPLEMENTAL_CANONICAL_TRANSCRIPTION | `AOT_V20_E005` | page0077-0078.jpeg |  | 17 | DEEP_READING_TRANSCRIPTION / REOPEN_PRIMARY_IF_LOAD_BEARING | P0-P2 by volume |
| `AOT-JP-144` | V20 | 第80話 名も無き兵士 | 「夢を諦めて死んでくれ」 | SUPPLEMENTAL_CANONICAL_TRANSCRIPTION | `AOT_V20_E005` | page0077-0078.jpeg |  | 17 | DEEP_READING_TRANSCRIPTION / REOPEN_PRIMARY_IF_LOAD_BEARING | P0-P2 by volume |
| `AOT-JP-145` | V20 | 第80話 名も無き兵士 | 「兵士よ怒れ」「兵士よ叫べ」「兵士よ!! 戦え!!」 | SUPPLEMENTAL_CANONICAL_TRANSCRIPTION | `AOT_V20_E006` | page0089-0095.jpeg |  | 17 | DEEP_READING_TRANSCRIPTION / REOPEN_PRIMARY_IF_LOAD_BEARING | P0-P2 by volume |
| `AOT-JP-146` | V20 | 第81話 約束 | 「何事も楽しまなくちゃ」 | SUPPLEMENTAL_CANONICAL_TRANSCRIPTION | `AOT_V20_E007` | page0103-0104.jpeg |  | 17 | DEEP_READING_TRANSCRIPTION / REOPEN_PRIMARY_IF_LOAD_BEARING | P0-P2 by volume |
| `AOT-JP-147` | V20 | 第82話 勇者 | 「僕がエレンにウソついたことあった?」 | SUPPLEMENTAL_CANONICAL_TRANSCRIPTION | `AOT_V20_E015` | page0156-0157.jpeg |  | 17 | DEEP_READING_TRANSCRIPTION / REOPEN_PRIMARY_IF_LOAD_BEARING | P0-P2 by volume |
| `AOT-JP-148` | V21 | 第84話 白夜 | 「人類を救うのは オレでも団長でもない!! アルミンだ!!」 | SUPPLEMENTAL_CANONICAL_TRANSCRIPTION | `AOT_V21_E003` | page0062-page0064.jpeg |  | 17 | DEEP_READING_TRANSCRIPTION / REOPEN_PRIMARY_IF_LOAD_BEARING | P0-P2 by volume |
| `AOT-JP-149` | V21 | 第84話 白夜 | 「辛い…辛いよ」 | SUPPLEMENTAL_CANONICAL_TRANSCRIPTION | `AOT_V21_E005` | page0072-page0076.jpeg |  | 17 | DEEP_READING_TRANSCRIPTION / REOPEN_PRIMARY_IF_LOAD_BEARING | P0-P2 by volume |
| `AOT-JP-150` | V21 | 第84話 白夜 | 「それでも 前に進まなきゃいけない…」 | SUPPLEMENTAL_CANONICAL_TRANSCRIPTION | `AOT_V21_E005` | page0072-page0076.jpeg |  | 17 | DEEP_READING_TRANSCRIPTION / REOPEN_PRIMARY_IF_LOAD_BEARING | P0-P2 by volume |
| `AOT-JP-151` | V21 | 第83話 大鉈 | 「俺はお前の理解者だ」 / 「俺達は あの父親の 被害者」 / 「お前は父親に 洗脳されている」 | SUPPLEMENTAL_CANONICAL_TRANSCRIPTION | `AOT_V21_E001` | page0014-page0015.jpeg |  | 17 | DEEP_READING_TRANSCRIPTION / REOPEN_PRIMARY_IF_LOAD_BEARING | P0-P2 by volume |
| `AOT-JP-152` | V22 | 第89話 会議 | 「壁の中で人を愛せ」 | SUPPLEMENTAL_CANONICAL_TRANSCRIPTION | `AOT_V22_E021` | page0140-page0142.jpeg |  | 17 | DEEP_READING_TRANSCRIPTION / REOPEN_PRIMARY_IF_LOAD_BEARING | P0-P2 by volume |
| `AOT-JP-153` | V22 | 第90話 壁の向こう側へ | 「可能性はいくらでも広がっている」 | SUPPLEMENTAL_CANONICAL_TRANSCRIPTION | `AOT_V22_E027` | page0163-page0165.jpeg |  | 17 | DEEP_READING_TRANSCRIPTION / REOPEN_PRIMARY_IF_LOAD_BEARING | P0-P2 by volume |
| `AOT-JP-154` | V22 | 第90話 壁の向こう側へ | 「向こうにいる敵…全部殺せば…オレ達 自由になれるのか?」 | SUPPLEMENTAL_CANONICAL_TRANSCRIPTION | `AOT_V22_E032` | page0186-page0188.jpeg |  | 17 | DEEP_READING_TRANSCRIPTION / REOPEN_PRIMARY_IF_LOAD_BEARING | P0-P2 by volume |
| `AOT-JP-155` | V31 | 第123話 島の悪魔 | 「オレの名は」 / 「オレの目的は」 / 「オレはその望みを拒む」 | SUPPLEMENTAL_CANONICAL_TRANSCRIPTION | `AOT_V31_E009` | p0044-p0046 |  | 17 | DEEP_READING_TRANSCRIPTION / REOPEN_PRIMARY_IF_LOAD_BEARING | P0-P2 by volume |
| `AOT-JP-156` | V31 | 第123話 島の悪魔 | 「駆逐」 | SUPPLEMENTAL_CANONICAL_TRANSCRIPTION | `AOT_V31_E010` | p0047-p0050 |  | 17 | DEEP_READING_TRANSCRIPTION / REOPEN_PRIMARY_IF_LOAD_BEARING | P0-P2 by volume |
| `AOT-JP-157` | V31 | 第124話 氷解 | 「前代未聞の大虐殺」 | SUPPLEMENTAL_CANONICAL_TRANSCRIPTION | `AOT_V31_E013` | p0061-p0062 |  | 17 | DEEP_READING_TRANSCRIPTION / REOPEN_PRIMARY_IF_LOAD_BEARING | P0-P2 by volume |
| `AOT-JP-158` | V31 | 第123話 島の悪魔 | 「家族」 | SUPPLEMENTAL_CANONICAL_TRANSCRIPTION | `AOT_V31_E004` | p0021-p0024 |  | 17 | DEEP_READING_TRANSCRIPTION / REOPEN_PRIMARY_IF_LOAD_BEARING | P0-P2 by volume |

## X. Appendix B — volume coverage ledger

| Volume | Locator-backed JP rows | Supplemental rows | Current language-retrieval state |
|---|---:|---:|---|
| V01 | 3 | 0 | CHAPTER/EVIDENCE VERIFIED; SELECTIVE PAGE BACKFILL WHEN LOAD-BEARING |
| V02 | 2 | 0 | CHAPTER/EVIDENCE VERIFIED; SELECTIVE PAGE BACKFILL WHEN LOAD-BEARING |
| V03 | 1 | 0 | CHAPTER/EVIDENCE VERIFIED; SELECTIVE PAGE BACKFILL WHEN LOAD-BEARING |
| V04 | 3 | 0 | CHAPTER/EVIDENCE VERIFIED; SELECTIVE PAGE BACKFILL WHEN LOAD-BEARING |
| V05 | 5 | 0 | CHAPTER/EVIDENCE VERIFIED; SELECTIVE PAGE BACKFILL WHEN LOAD-BEARING |
| V06 | 4 | 0 | CHAPTER/EVIDENCE VERIFIED; SELECTIVE PAGE BACKFILL WHEN LOAD-BEARING |
| V07 | 5 | 0 | CHAPTER/EVIDENCE VERIFIED; SELECTIVE PAGE BACKFILL WHEN LOAD-BEARING |
| V08 | 3 | 0 | CHAPTER/EVIDENCE VERIFIED; SELECTIVE PAGE BACKFILL WHEN LOAD-BEARING |
| V09 | 6 | 0 | CHAPTER/EVIDENCE VERIFIED; SELECTIVE PAGE BACKFILL WHEN LOAD-BEARING |
| V10 | 5 | 0 | CHAPTER/EVIDENCE VERIFIED; SELECTIVE PAGE BACKFILL WHEN LOAD-BEARING |
| V11 | 7 | 0 | CHAPTER/EVIDENCE VERIFIED; SELECTIVE PAGE BACKFILL WHEN LOAD-BEARING |
| V12 | 7 | 0 | CHAPTER/EVIDENCE VERIFIED; SELECTIVE PAGE BACKFILL WHEN LOAD-BEARING |
| V13 | 7 | 0 | CHAPTER/EVIDENCE VERIFIED; SELECTIVE PAGE BACKFILL WHEN LOAD-BEARING |
| V14 | 7 | 0 | CHAPTER/EVIDENCE VERIFIED; SELECTIVE PAGE BACKFILL WHEN LOAD-BEARING |
| V15 | 6 | 0 | CHAPTER/EVIDENCE VERIFIED; SELECTIVE PAGE BACKFILL WHEN LOAD-BEARING |
| V16 | 5 | 0 | CHAPTER/EVIDENCE VERIFIED; SELECTIVE PAGE BACKFILL WHEN LOAD-BEARING |
| V17 | 5 | 0 | CHAPTER/EVIDENCE VERIFIED; SELECTIVE PAGE BACKFILL WHEN LOAD-BEARING |
| V18 | 5 | 0 | CHAPTER/EVIDENCE VERIFIED; SELECTIVE PAGE BACKFILL WHEN LOAD-BEARING |
| V19 | 7 | 0 | MATURE LOCATOR-SEEDED; NORMAL PRIMARY REOPENING FOR NUANCE |
| V20 | 0 | 5 | MATURE LOCATOR-SEEDED; NORMAL PRIMARY REOPENING FOR NUANCE |
| V21 | 0 | 4 | MATURE LOCATOR-SEEDED; NORMAL PRIMARY REOPENING FOR NUANCE |
| V22 | 1 | 3 | MATURE LOCATOR-SEEDED; NORMAL PRIMARY REOPENING FOR NUANCE |
| V23 | 1 | 0 | MATURE LOCATOR-SEEDED; NORMAL PRIMARY REOPENING FOR NUANCE |
| V24 | 6 | 0 | MATURE LOCATOR-SEEDED; NORMAL PRIMARY REOPENING FOR NUANCE |
| V25 | 4 | 0 | MATURE LOCATOR-SEEDED; NORMAL PRIMARY REOPENING FOR NUANCE |
| V26 | 3 | 0 | MATURE LOCATOR-SEEDED; NORMAL PRIMARY REOPENING FOR NUANCE |
| V27 | 1 | 0 | MATURE LOCATOR-SEEDED; NORMAL PRIMARY REOPENING FOR NUANCE |
| V28 | 8 | 0 | MATURE LOCATOR-SEEDED; NORMAL PRIMARY REOPENING FOR NUANCE |
| V29 | 1 | 0 | MATURE LOCATOR-SEEDED; NORMAL PRIMARY REOPENING FOR NUANCE |
| V30 | 7 | 0 | P0 PRIMARY-PAGE REINSPECTION BEFORE WORDING-DEPENDENT SPECIALIST CLAIMS |
| V31 | 0 | 4 | P0 PRIMARY-PAGE REINSPECTION BEFORE WORDING-DEPENDENT SPECIALIST CLAIMS |
| V32 | 3 | 0 | P0 PRIMARY-PAGE REINSPECTION BEFORE WORDING-DEPENDENT SPECIALIST CLAIMS |
| V33 | 8 | 0 | P0 PRIMARY-PAGE REINSPECTION BEFORE WORDING-DEPENDENT SPECIALIST CLAIMS |
| V34 | 6 | 0 | P0 PRIMARY-PAGE REINSPECTION BEFORE WORDING-DEPENDENT SPECIALIST CLAIMS |

## XI. Completion / growth rule

This v1.0 seed is complete for **Phase-1 retrieval stabilization**, not frozen against future additions. During specialist drafting, add a passage or term only when it has a distinct retrieval responsibility: exact wording changes interpretation, a recurring lexical cluster becomes analytically material, an address/register contrast matters to character reconstruction, or a disputed translation requires explicit audit. Do not turn the index into a transcription dump. Long passages remain in the primary manga; this artifact should continue to store only the shortest anchor necessary to recover them.

The next architecture-defined production phase is **Phase 2 macroarchitecture**, beginning with `AOT_01_SERIES_ARCHITECTURE_VOLUME_PROGRESSION_AND_MASTER_THESIS.md`, unless an audit of this seed discovers a blocking retrieval defect.

