---
series: HIBIKE
artifact_type: crosswalk
scope: GLOBAL_PLUS_V01-V14_RECONCILED
generation: V2
status: active_provisional
source_boundary: "Locked Japanese EPUB corpus HIBIKE-V01 through HIBIKE-V14; detailed V1 wording-sensitive reconciliation complete through legacy unit 10 / HIBIKE-V12; HIBIKE-V13 and HIBIKE-V14 recorded as V2-only source expansions"
supersedes: null
superseded_by: null
do_not_use_as_current_authority: false
---

# Sound! Euphonium — V1 OCR to V2 Clean-Text Crosswalk

## 1. Purpose

V1 used a **ten-unit analytical numbering system** that does not match the V2 publication-sequence corpus. V2 instead fixes `HIBIKE-V01` through `HIBIKE-V14` to the fourteen-book publication chronology.

This artifact prevents three classes of error:

1. treating V1 “Volume 5” as HIBIKE-V05 when it is actually HIBIKE-V07;
2. assuming the Rikka novels or later spin-off/anthology books were already covered by V1;
3. carrying OCR-sensitive wording claims forward without checking the clean Japanese text.

The crosswalk is **active provisional** because detailed wording-sensitive claim transitions will be populated during each V2 deep reading. The structural mapping below is authoritative now.

---

## 2. High-level V1 ↔ V2 mapping

| V2 source | V1 analytical artifact | V1 OCR pack | V1 coverage | V2 action |
|---|---|---|---|---|
| **HIBIKE-V01** | `SOUND! EUPHONIUM.md` | `hibike_euphonium_volume_01_analysis_pack.zip` | yes | reread from clean EPUB; audit baseline Kumiko/Reina/Kitauji voice and V1 claims |
| **HIBIKE-V02** | `SOUND! EUPHONIUM — Novel 2.md` | `hibike_euphonium_volume_02_analysis_pack.zip` | yes | reread from clean EPUB; preserve local ambiguity before later hindsight |
| **HIBIKE-V03** | `SOUND! EUPHONIUM — Novel 3.md` | `hibike_euphonium_volume_03_analysis_pack.zip` | yes | reread; high-priority exact-language/Asuka-family/institution audit |
| **HIBIKE-V04** | `SOUND! EUPHONIUM — Novel 4.md` | `hibike_euphonium_volume_04_analysis_pack.zip` | yes | reread anthology focalizers; expand autonomous character voice evidence |
| **HIBIKE-V05** | **none** | **none** | **V1 gap** | first canonical project reading; establish Azusa/Rikka state from scratch |
| **HIBIKE-V06** | **none** | **none** | **V1 gap** | first canonical project reading; complete Rikka comparative institution model |
| **HIBIKE-V07** | `SOUND! EUPHONIUM — Volume 5.md` | `hibike_euphonium_volume_05_analysis_pack.zip` | yes under V1 number 5 | reread; separate Takeda prose from guide/paratext; correct numbering |
| **HIBIKE-V08** | `SOUND! EUPHONIUM — Novel 6.md` | `hibike_euphonium_volume_06_analysis_pack.zip` | yes under V1 number 6 | reread; second-year baseline, Kanade/Mirei/Motomu and fairness architecture |
| **HIBIKE-V09** | `SOUND! EUPHONIUM — Novel 7.md` | `hibike_euphonium_volume_07_analysis_pack.zip` | yes under V1 number 7 | reread; consequences, defeat, relationship asymmetry, institutional state |
| **HIBIKE-V10** | `SOUND! EUPHONIUM — Novel 8.md` | `hibike_euphonium_volume_08_analysis_pack.zip` | yes under V1 number 8 | reread anthology/ordinary-life material for behavior and voice modeling |
| **HIBIKE-V11** | `SOUND! EUPHONIUM — Novel 9.md` | `hibike_euphonium_volume_09_analysis_pack.zip` | yes under V1 number 9 | reread clean third-year text; high-priority Kumiko/Mayu/Reina/Kanade audit |
| **HIBIKE-V12** | `SOUND! EUPHONIUM — Novel 10.md` | `hibike_euphonium_volume_10_analysis_pack.zip` | yes under V1 number 10 | reread clean finale; major V1 revision and mature-state integration |
| **HIBIKE-V13** | **none** | **none** | **V1 gap** | first canonical project reading; Nozomi/Mizore/Yuuko alternate-perspective expansion; includes `記憶のイルミネーション` |
| **HIBIKE-V14** | **none** | **none** | **V1 gap** | first canonical project reading; post-main-arc ensemble state and ordinary-life evidence |

### Critical numbering rule

From V2 onward, **never use bare “Volume 5,” “Novel 8,” etc. to route evidence without the `HIBIKE-VXX` identifier or Japanese title** when there is any possibility of V1 ambiguity.

In particular:

- V1 analytical **5** = HIBIKE-**V07**;
- V1 analytical **6** = HIBIKE-**V08**;
- V1 analytical **7** = HIBIKE-**V09**;
- V1 analytical **8** = HIBIKE-**V10**;
- V1 analytical **9** = HIBIKE-**V11**;
- V1 analytical **10** = HIBIKE-**V12**.

---

## 3. V1 gap expansion

Four locked V2 books have no V1 deep-reading counterpart:

### HIBIKE-V05 / V06 — Rikka/Tachibana duology

These are not OCR replacements. They are an entirely new analytical domain for the project.

V2 should use them to test:

- Azusa as an autonomous subject rather than a Kitauji-adjacent figure;
- comparative institutional culture;
- marching-band discipline and embodiment;
- alternative constructions of excellence and belonging;
- whether V1's Kitauji-centered claims overgeneralized high-school music culture.

### HIBIKE-V13 — 『飛び立つ君の背を見上げる』

New perspective architecture centered on Nozomi/Mizore/Yuuko and related characters. Especially valuable for correcting Kumiko-centered epistemic assumptions and for character models that need voices independent of Kumiko's observation.

### HIBIKE-V14 — 『みんなの話』

New post-main-series ensemble evidence. Particularly valuable for ordinary-life behavior, relationship state after the competitive climax, later character trajectories, and simulation-grade voice evidence.

---

## 4. OCR authority transition

### V1 OCR status

V1 repeatedly treated its OCR as suitable for narrative continuity and literary interpretation but not fully safe for quotation-grade linguistic claims. V2 therefore establishes:

> **When a locked EPUB exists, the V1 OCR pack has no authority over exact Japanese wording.**

OCR remains useful for:

- provenance;
- recovering how a V1 claim arose;
- visual-page evidence if a scan contains meaningful layout/illustration information absent from the ebook;
- locating OCR-specific corruption when a V1 interpretation looks suspicious.

OCR must not settle:

- particles;
- sentence endings;
- honorifics;
- punctuation;
- ruby;
- kana size/orthography;
- dialect/register;
- exact quotation;
- speaker attribution where the clean source differs.

---

## 5. High-priority V1 claim classes for clean-text audit

The detailed claim ledger will be updated volume by volume, but the following V1 domains receive automatic scrutiny:

| Claim class | Why V2 must recheck | Default disposition before reread |
|---|---|---|
| Character first/second-person forms | core to simulation-grade voice | OPEN |
| Honorific/casual switching | relationship-conditioned evidence | OPEN |
| Kansai/regional language | OCR-sensitive and socially meaningful | OPEN |
| Sentence-final particles / hedging | character-state and addressee conditioning | OPEN |
| Punctuation/ellipsis/repetition | emotional and interactional evidence | OPEN |
| Exact phrases used to anchor thematic claims | wording may strengthen or weaken interpretation | OPEN |
| Speaker attribution in dense dialogue | OCR segmentation may mislead | OPEN |
| Ruby-dependent wordplay/readings | OCR may omit reading information | OPEN |
| V1 claims based only on Kumiko's interpretation of others | focalization risk independent of OCR | OPEN |
| V1 macro thematic theses | generally stronger evidentiary foundation, but still tested | OPEN pending sequential audit |

No claim is automatically revised merely because V2 uses a better text. V2 uses `PRESERVE / STRENGTHEN / REVISE / DOWNGRADE / REJECT / OPEN` only after evidence is reviewed.

---

## 6. Per-volume expansion protocol

At the start of each `HIBIKE_VXX_DEEP_READING.md` that has V1 coverage:

1. identify the exact V1 artifact and OCR pack through this crosswalk;
2. perform the clean-text reading **before** allowing V1 conclusions to dominate interpretation;
3. identify wording-sensitive or focalization-sensitive V1 claims;
4. route exact source evidence through the locked locator grammar;
5. assign revision transitions only at the end of the volume;
6. append high-leverage corrections to `HIBIKE_V1_CLAIM_REVISION_LEDGER.md` once that ledger is instantiated.

For HIBIKE-V05, V06, V13, and V14 there is no V1 claim transition except where the new source retrospectively changes a cross-series claim from V1. Such changes should be attributed explicitly as **new-source revision**, not OCR correction.

---

## 7. Initial locator crosswalk

V2 evidence locator grammar:

`HIBIKE-VXX / SNN / P#### / <short exact Japanese cue>`

The V1 artifacts are not retrofitted with fake locators. When a V1 claim is rechecked, the crosswalk records the V2 locator that now supports, revises, or rejects it.

Recommended eventual row structure:

| V1 claim ID / cue | V1 artifact | V2 source | V2 locator(s) | Transition | Current formulation | Notes |
|---|---|---|---|---|---|---|

This scaffold should grow during the sequential reread; it is not a reason to duplicate all V1 analysis before HIBIKE-V01 begins.

---

## 8. Current state

The global structural crosswalk is complete enough to authorize Phase 1. Detailed textual reconciliation remains intentionally incremental and will be driven by each deep reading.


---

## 9. HIBIKE-V01 detailed reconciliation

V1 artifact: `SOUND! EUPHONIUM.md`  
Current source authority: `HIBIKE-V01` locked EPUB, SHA-256 `8b03b3aad0555b22cbb0ebe2f19b1adf9f3919b60487395dae0ab7958488e288`.

The V01 reread is complete. Exact-language claims are now routed to the clean EPUB; V1 OCR remains provenance only.

| V1 claim / section | Clean-text anchor | Transition | Crosswalk note |
|---|---|---|---|
| Executive thesis — difficulty of wanting | `HIBIKE-V01 / S03 / P0718 / それだけ、と久美子は曖昧に微笑んだ。自分の考えを言葉にするのが、久美子は`; `HIBIKE-V01 / S05 / P0727 / 全国に行けたらいいな。そう、久美子はずっと思っていた。中学生のころから、` | STRENGTHEN | clean text makes rejection-avoidance mechanism explicit |
| Kumiko “good girl” skin | `HIBIKE-V01 / S04 / P0560 / 「久美子ってさ、結構性格悪いやん？」`; `HIBIKE-V01 / S04 / P0564 / 「そのいい子ちゃんの皮、ぺりぺりってめくりたいなあと思って」` | STRENGTHEN | exact いい子ちゃん wording verified |
| Kumiko standard Japanese in Kyoto world | `HIBIKE-V01 / S02 / P0029 / 「っていうかさ、さっきから気になっててんけど、アンタなんで標準語なん？」`; `HIBIKE-V01 / S02 / P0032 / 「家族もみんな標準語だから、あんまりうつらないかな。あ、でも一緒にいた友` | STRENGTHEN | Tokyo residence + family standard speech explicit |
| Reina `アタシ / アンタ` and Kansai intensity | `HIBIKE-V01 / S01 / P0025 / 「悔しい。悔しくって死にそう。なんでみんな金賞なんかで喜べんの？アタシら`; `HIBIKE-V01 / S01 / P0029 / 「アンタは悔しくないわけ？」`; `HIBIKE-V01 / S01 / P0031 / 「アタシは悔しい。めっちゃ悔しいねん」` | STRENGTHEN | exact person reference and regional forms verified |
| Taki atmosphere engineering | `HIBIKE-V01 / S05 / P0195 / 「でも、滝先生はそうしいひんかった。多分、あの人は最初に見せつけたかった`; `HIBIKE-V01 / S05 / P0200 / 「先生の戦略は上手いわ。二回目の合奏で、うちらは一気に上手なった。滝先生` | DOWNGRADE | observed effects remain; exact strategy is Natsuki-mediated interpretation |
| Meritocracy as justice | `HIBIKE-V01 / S04 / P0036 / 「でも、いまの顧問は私ですよ？これまでのことなんて関係あります？」`; `HIBIKE-V01 / S04 / P0754 / 千五百以上ある高校のなかで、全国大会に残れるのはたった三十校足らず。京都` | REVISE | performance legitimacy must retain unequal-precondition critique |
| Aoi “no regrets” as lie | `HIBIKE-V01 / S04 / P0853 / 「してないよ。まったくしてない」`; `HIBIKE-V01 / S04 / P0854 / 晴れやかな表情で言う彼女の指が、自身の腕をぎゅうとつかむ。白い皮膚に残る` | REVISE | bodily contradiction direct; lie attribution remains focalized inference |
| Asuka neutrality | `HIBIKE-V01 / S02 / P0265 / その姿を見た瞬間、あすかの目が爛々と輝いた。楽器を部長に押しつけ、ズカズ`; `HIBIKE-V01 / S05 / P0628 / 「正直言って、心の底からどうでもいいよ。誰がソロとか、そんなくだらないこ` | REVISE | high intervention in affect/practice + selective conflict disengagement |
| Kaori wanted decisive defeat | `HIBIKE-V01 / S05 / P0688 / 「ソロは、あなたが吹くべきやと思う」`; `HIBIKE-V01 / S05 / P0695 / 不意にあすかの声が、耳元で蘇る。その言葉の意味を、久美子はここで初めて理` | PRESERVE with epistemic qualifier | acceptance direct; inner purpose is Kumiko interpretation |
| Shuuichi structural weight | `HIBIKE-V01 / S02 / P0178 / 「そう言うなら過去のことを謝罪してください」`; `HIBIKE-V01 / S02 / P0212 / 「もしかしてまたアレか？周りに流された？」`; `HIBIKE-V01 / S05 / P0820 / 「大丈夫だって、あんなに練習したんだからさ」` | STRENGTHEN | clean register evidence and regulation role sharpened |
| Embodied music | `HIBIKE-V01 / S03 / P0355 / 音のなかに溶け込ませる。その言葉を意識して、久美子は周りの音に耳を澄ませ`; `HIBIKE-V01 / S03 / P0434 / そしていま葉月が悪戦苦闘しているのが、リップスラーだ。ひとつの指使いでさ`; `HIBIKE-V01 / S04 / P0316 / 簡単そうな場面をひととおり吹いて確認してから、久美子は難関となるだろうメ` | STRENGTHEN | technical pedagogy now tracked as causal mechanism |
| Mirrored result boards | `HIBIKE-V01 / S01 / P0001 / 何百という顔が、一様に同じ方向を見つめていた。広場に渦巻く熱を帯びた空気`; `HIBIKE-V01 / S06 / P0001 / 何百という顔が、一様に同じ方向を見つめていた。広場に渦巻く熱を帯びた空気`; `HIBIKE-V01 / S06 / P0027 / 「麗奈、私、ほんとにうれしい」` | PRESERVE | formal mirror directly verified |

Detailed current formulations live in `HIBIKE_V1_CLAIM_REVISION_LEDGER.md`; this crosswalk's role is source transition and text recovery.

### V01 source-routing closure

- V1 OCR wording authority: **retired** for V01 where locked EPUB is available.
- V1 analysis: **historical legacy / revision provenance**.
- V2 current analytical authority: `HIBIKE_V01_DEEP_READING.md`.
- V2 exact-text authority: locked `HIBIKE-V01` EPUB.
- Full deterministic paragraph route: `HIBIKE_V01_LOCATOR_INDEX.md`.

---

## 10. HIBIKE-V02 detailed reconciliation

V1 artifact: `SOUND! EUPHONIUM — Novel 2.md`  
Current source authority: `HIBIKE-V02` locked EPUB, SHA-256 `fda7b77e5028f8e50d55cbffe883b3b63b57cf35d0abc1618e620b40c504cf12`.

The V02 reread is complete. The broad V1 interpretation survives, but the clean text sharpens temporal justice, relational asymmetry, competition epistemology, and character-conditioned speech. Exact-language authority now routes exclusively to HIBIKE-V02.

| V1 claim / section | Clean-text anchor | Transition | Crosswalk note |
|---|---|---|---|
| Executive — ranking / asymmetrical first places | `HIBIKE-V02 / S03 / P0710`; `HIBIKE-V02 / S04 / P0375` | REVISE | ranking remains important; missed timing and non-retroactive justice better organize the whole volume |
| Meritocracy necessary but insufficient | `HIBIKE-V02 / S03 / P0149`; `HIBIKE-V02 / S03 / P0710` | STRENGTHEN | fairer present procedure cannot repay people injured under prior rules |
| Effort not erased by bad result | `HIBIKE-V02 / S03 / P0702`; `HIBIKE-V02 / S04 / P0339` | STRENGTHEN | Yuuko makes distinction explicit; result changes meaning without nullifying labor |
| Kumiko observer→participant | `HIBIKE-V02 / S03 / P0201-P0208`; `HIBIKE-V02 / S03 / P0644` | STRENGTHEN | intervention becomes intentional; new risk is intervention before full knowledge |
| Kumiko/Reina privileged intimacy | `HIBIKE-V02 / S02 / P0150-P0157`; `HIBIKE-V02 / S02 / P0923-P0932`; `HIBIKE-V02 / S04 / P0482`; `HIBIKE-V02 / S04 / P0600` | STRENGTHEN | invitation embarrassment, fear of losing present closeness, practical care, musical dedication expand dyadic evidence |
| Reina is uniformly blunt/direct | V1 implied but did not fully model domain split | REVISE / STRENGTHEN model | musical propositions remain blunt; relational initiation and Taki uncertainty are much more vulnerable |
| Mizore hates competition because judgment is subjective | `HIBIKE-V02 / S03 / P0381-P0398` | STRENGTHEN | explicit theory distinguishes technical legibility from taste-dependent evaluation |
| Mizore technical perfection lacks expression | `HIBIKE-V02 / S03 / P0461-P0480`; `HIBIKE-V02 / S03 / P0747-P0753` | STRENGTHEN | Hashimoto and Niiyama separately establish expression/expectation problem |
| Nozomi sincere but blind to unequal attachment | `HIBIKE-V02 / S04 / P0369-P0380` | STRENGTHEN | direct explanation preserves care while narration preserves unequal heat |
| Jealousy helped cause Nozomi not to invite Mizore | `HIBIKE-V02 / S04 / P0369` | DOWNGRADE | jealousy is Kumiko's private suspicion; direct Nozomi explanation is respect for Mizore's persistence |
| Yuuko pluralizes Mizore's dependence | `HIBIKE-V02 / S04 / P0324-P0343`; `HIBIKE-V02 / S04 / P0423` | STRENGTHEN | second anchor becomes explicit; Nozomi remains first |
| Natsuki's return help is atonement | `HIBIKE-V02 / S04 / P0098` | STRENGTHEN | `罪滅ぼし` direct wording verified |
| Asuka neutrality→management | `HIBIKE-V02 / S02 / P0548`; `HIBIKE-V02 / S03 / P0544-P0554`; `HIBIKE-V02 / S04 / P0459` | STRENGTHEN | strategic triage and information control are explicit |
| Asuka's private musician beneath public utility | `HIBIKE-V02 / S03 / P0725`; `HIBIKE-V02 / S03 / P0732` | STRENGTHEN | 4 a.m. playing and `秘密` establish guarded noninstrumental interior |
| Reina plays for herself / Mizore for Nozomi | `HIBIKE-V02 / S04 / P0491`; `HIBIKE-V02 / S04 / P0594`; `HIBIKE-V02 / S04 / P0600` | STRENGTHEN | exact addressee contrast verified; Reina can still temporarily dedicate to Kumiko |
| Taki treats result as evaluation, not absolute worth | `HIBIKE-V02 / S04 / P0547` | STRENGTHEN | exact speech strongly grounds V1 competition reading |
| Taki teaching is definitively grief recovery | `HIBIKE-V02 / S03 / P0630` | REVISE | withdrawal/return testimony supported, but Hashimoto explicitly does not know causal trigger for taking Kitauji |
| Kitauji miracle vs powerhouse stability | `HIBIKE-V02 / S04 / P0640-P0641`; `HIBIKE-V02 / S04 / P0711` | STRENGTHEN | `安定感` directly names repeatability as elite difference |
| Reconciliation equalizes Mizore/Nozomi | V1 already rejected this | STRENGTHEN V1 | `HIBIKE-V02 / S04 / P0375`; `S04 / P0423` explicitly preserve unequal centrality |
| Epilogue proves competition fair | V1 already treated more carefully | STRENGTHEN V1 | `HIBIKE-V02 / S05 / P0041` makes change explicitly experiential: `たったいま` |

### V02 source-routing closure

- V1 OCR wording authority: **retired** for V02 where locked EPUB is available.
- V1 analysis: **historical legacy / revision provenance**.
- V2 current analytical authority: `HIBIKE_V02_DEEP_READING.md`.
- V2 exact-text authority: locked `HIBIKE-V02` EPUB.
- Full deterministic paragraph route: `HIBIKE_V02_LOCATOR_INDEX.md`.

---

## 11. HIBIKE-V03 detailed reconciliation

V1 artifact: `SOUND! EUPHONIUM — Novel 3.md`  
Current source authority: locked `HIBIKE-V03` EPUB.

The V03 reread closes the opening trilogy. V1's ownership thesis remains strong, but V2 revises the mechanism around epistemic humility, first-person claims, institutional redundancy, and the separation of formal adjudication from relational recognition.

| V1 claim / section | Clean-text anchor | Transition | Crosswalk note |
|---|---|---|---|
| V03 = desire becomes ownership | `HIBIKE-V03 / S04 / P0561-P0571` | STRENGTHEN / REVISE mechanism | ownership succeeds when Kumiko stops speaking for “the band” and speaks from first person |
| Asuka constructed as special | `HIBIKE-V03 / S02 / P0548-P0552` | STRENGTHEN | Haruka explicitly says the band drew a boundary around Asuka and withheld ordinary support |
| Necessary vs wanted | `HIBIKE-V03 / S04 / P0559-P0571` | REVISE | functional replaceability can coexist with relational irreplaceability; Natsuki's substitute readiness is ethically necessary |
| Kumiko's intervention | `HIBIKE-V03 / S04 / P0553-P0571` | REVISE | intervention is growth but V02/V03 show the risk of acting before full knowledge |
| Asuka competence as armor | `HIBIKE-V03 / S02 / P0383-P0436`; `S02 / P0552` | STRENGTHEN | competence also preserves bargaining power and continued permission to make music |
| Asuka regulates mother | `HIBIKE-V03 / S02 / P0383-P0436` | STRENGTHEN | clean text repeatedly shows de-escalation, environment management, and reassurance after harm |
| Mamiko outsourced life | `HIBIKE-V03 / S03 / P0415-P0443` | STRENGTHEN / REVISE | problem is not that the approved path is objectively false but that obedience outsourced authorship/responsibility |
| Taki carries wife's dream | `HIBIKE-V03 / S03 / P0848-P0882`; `S04 / P1431-P1434` | STRENGTHEN | private motive is explicit but analytically distinct from public legitimacy |
| Reina as strong/direct | `HIBIKE-V03 / S04 / P0787-P0819` | REVISE | attachment domain includes hurt trust, reassurance-seeking, and preference for painful truth over protective concealment |
| Shindō C and personal message | `HIBIKE-V03 / S04 / P1452-P1477` | STRENGTHEN | professional contest judgment and paternal/individual recognition are explicitly separate |
| Bronze as owned defeat | national-result sequence + `HIBIKE-V03 / S04 / P1452-P1454` | STRENGTHEN | external result remains meaningful without exhausting performance value |
| Notebook / title as inheritance | `HIBIKE-V03 / S05 / P0033-P0063` | STRENGTHEN | transmission becomes an explicit instruction to play for future juniors |
| Asuka secretly “needs rescue” | `HIBIKE-V03 / S04 / P0553-P0571` | DOWNGRADE | Kumiko matters, but the real academic/family/institutional constraints must not be erased by retrospective rescue narrative |
| Taki results prove legitimacy | `HIBIKE-V03 / S04 / P1431-P1434` | REVISE | Taki himself recognizes possible imposition; legitimacy remains procedurally bounded |

Detailed V03 transitions: see `HIBIKE_V1_CLAIM_REVISION_LEDGER.md` and `HIBIKE_V03_DEEP_READING.md`.

### V03 source-routing closure

- V1 OCR wording authority: **retired** for V03 where locked EPUB is available.
- V1 analysis: **historical legacy / revision provenance**.
- V2 current analytical authority: `HIBIKE_V03_DEEP_READING.md`.
- V2 exact-text authority: locked `HIBIKE-V03` EPUB.
- Full deterministic paragraph route: `HIBIKE_V03_LOCATOR_INDEX.md`.
- Opening-trilogy checkpoint: `HIBIKE_V01-V03_CHECKPOINT.md`.


---

## HIBIKE-V04 detailed reconciliation — V1 Novel 4 / anthology

V04 confirms that the V1 anthology reading was structurally strong while making its evidentiary claims more precise. The largest V2 gain is that clean text plus deterministic locators allow alternate focalizers to be used as **direct interior evidence** without treating any focalizer as omniscient.

| V1 claim / section | Clean-text anchor | Transition | Crosswalk note |
|---|---|---|---|
| Anthology becomes truly polyphonic | full S01–S14 architecture | STRENGTHEN | alternate focalization changes evidence class and supports simulation-grade reconstruction |
| Early Kumiko desire | `HIBIKE-V04 / S01 / P0114`, `P0121` | STRENGTHEN | hedged abstract commitment versus direct immediate musical want sharpens thought/speech/action model |
| Kaori envies low-brass ease | `S02 / P0190-P0195` | STRENGTHEN | exact wording plus Kumiko's tactful non-response recoverable |
| Aoi wants to be wanted | `S03 / P0092-P0098` | STRENGTHEN | direct focalized interior, no longer inference through Kumiko |
| Asuka hides deprivation | `S03 / P0083` | STRENGTHEN | direct self-description `隠すのが得意` anticipates V03 family crisis |
| Necessary versus wanted | `S03 / P0092-P0098` + V03 redundancy evidence | STRENGTHEN / REVISE architecture | distinguish visibility / necessity / replaceability / wantedness |
| Hazuki's generosity after rejection | `S06 / P0184-P0187` | REVISE | generosity is real; `作り物めいていた` laughter proves unresolved pain |
| Natsuki/Yuuko conflict = intimacy | `S07 / P0130-P0131`; `S12 / P0057-P0059` | STRENGTHEN / qualify | secure-return conflict can be intimacy; conflict in general is not sufficient evidence |
| Shuuichi performed adulthood | `S08 / P0136` | STRENGTHEN | focalized self-correction makes the mechanism explicit |
| Mizore/Yuuko origin | `S10 / P0067-P0068` | REVISE | Yuuko reaches immediately, but Mizore initially suspects pity; later trust must not be backported |
| Cultural festival ordinary youth | S11 | STRENGTHEN | becomes mandatory anti-overfitting evidence for character models |
| Yuuko/Natsuki leadership succession | `S12 / P0057-P0059` | STRENGTHEN | complementary friction is explicitly institutionalized |
| Reina privilege/infrastructure | `S13 / P0001-P0018` | STRENGTHEN | unequal training access is direct textual fact |
| Reina meritocracy invalidated by privilege | `S13 / P0011-P0018` | REVISE | opportunity affects merit production without erasing observed performance differences |
| Kumiko/Shuuichi explicit romance | `S14 / P0252-P0282` | STRENGTHEN | reciprocal `私も、秀一のこと好きだよ` is governing state evidence |
| Alternate viewpoints reveal objective hidden truth | anthology method | DOWNGRADE | they reveal focalizer interior directly, not universal objective truth |

Detailed V04 transitions: see `HIBIKE_V1_CLAIM_REVISION_LEDGER.md` and `HIBIKE_V04_DEEP_READING.md`.

### V04 source-routing closure

- V1 OCR wording authority: **retired** for V04 where locked EPUB exists.
- V1 analysis: **historical legacy / revision provenance**.
- V2 current analytical authority: `HIBIKE_V04_DEEP_READING.md`.
- V2 exact-text authority: locked `HIBIKE-V04` EPUB.
- Full deterministic paragraph route: `HIBIKE_V04_LOCATOR_INDEX.md`.
- V04 is the first anthology calibration layer after the canonical V01–V03 checkpoint.

## HIBIKE-V05 source-expansion routing — no V1 unit

| Field | Current routing |
|---|---|
| V2 source | `HIBIKE-V05` — 『響け！ ユーフォニアムシリーズ　立華高校マーチングバンドへようこそ 前編』 |
| Locked exact-text authority | `Sound! Euphonium - Novel 05 - Rikka High School Marching Band Welcome Part 1 [Japanese].epub` |
| V1 OCR pack / sequential reading counterpart | **None** |
| V1 bare-number warning | legacy V1 unit `05` corresponds to current **HIBIKE-V07**, not this book |
| Current analytical authority | `HIBIKE_V05_DEEP_READING.md` |
| Evidence route | `HIBIKE_V05_LOCATOR_INDEX.md` |
| Revision disposition | **N/A — V2 source expansion** |

No V1 wording authority is being retired for HIBIKE-V05 because V1 did not include this publication as a sequential unit. HIBIKE-V06 is expected to have the same expansion relationship. The V1→V2 claim ledger therefore retains 123 adjudicated claims after V05.

## HIBIKE-V06 source-expansion routing — no V1 unit

| Field | Current routing |
|---|---|
| V2 source | `HIBIKE-V06` — 『響け！ ユーフォニアムシリーズ　立華高校マーチングバンドへようこそ 後編』 |
| Locked exact-text authority | `Sound! Euphonium - Novel 06 - Rikka High School Marching Band Welcome Part 2 [Japanese].epub` |
| V1 OCR pack / sequential reading counterpart | **None** |
| V1 bare-number warning | legacy V1 unit `06` corresponds to current **HIBIKE-V08**, not this book |
| Current analytical authority | `HIBIKE_V06_DEEP_READING.md` |
| Evidence route | `HIBIKE_V06_LOCATOR_INDEX.md` |
| Rikka movement checkpoint | `HIBIKE_V05-V06_CHECKPOINT.md` |
| Revision disposition | **N/A — V2 source expansion** |

HIBIKE-V05 and V06 together are a self-contained V2 provenance expansion. No V1 wording authority is retired for either book because V1 had no sequential units for them. The next volume, HIBIKE-V07, returns to V1-covered territory: **legacy V1 unit 05 maps to HIBIKE-V07**. Claim-level adjudication therefore resumes with V07.


## HIBIKE-V07 detailed reconciliation — legacy V1 unit 05

| Field | Current routing |
|---|---|
| V2 source | `HIBIKE-V07` — 『響け！ ユーフォニアム　北宇治高校の吹奏楽部日誌』 |
| Locked exact-text authority | `Sound! Euphonium - Novel 07 - Kitauji High School Concert Band Diary [Japanese].epub` |
| Legacy V1 analytical counterpart | `SOUND! EUPHONIUM — Volume 5.md` |
| V1 numbering relation | legacy unit `05` → **HIBIKE-V07** |
| Current analytical authority | `HIBIKE_V07_DEEP_READING.md` |
| Evidence route | `HIBIKE_V07_LOCATOR_INDEX.md` |
| Narrative boundary | S01 `冬色ラプソディー` + S02 `星彩セレナーデ`; remaining book matter is F-class paratext |
| Revision status | **40 claim-level transitions complete** |

### High-priority V1→V2 routing changes

| V1 formulation | V2 clean-text anchor | Transition | Current formulation |
|---|---|---|---|
| Volume moves from being selected to selecting | `HIBIKE-V07 / S01 / P0293-P0367`; `P0482-P0554` | REVISE | macro-shift retained, but authorship is accountable curation; majority preference aggregation fails |
| Mizore as curator | `S01 / P0482-P0554` | STRENGTHEN | integrates distributed wishes under her own audience-facing frame `楽しい` |
| Hazuki performance anxiety | `S01 / P0633-P0664`; `P0742-P0805` | REVISE | fear is ensemble responsibility under perceived hierarchy, especially fear of degrading Reina's sound |
| Rikka as valid alternative culture | `S02 / P0050-P0089` + canonical V05–V06 checkpoint | STRENGTHEN | now grounded in autonomous Rikka primary-source model rather than foil-only inference |
| Azusa as alternative Kumiko | `S02 / P0140-P0286`; `HIBIKE-V07 / F01 / P0047-P0048` + V05–V06 | REVISE | contrast remains useful, but Azusa has independent causal architecture; Kumiko sees only current surface |
| Jealousy as information | `S02 / P0222-P0286` | STRENGTHEN | narration directly identifies disallowed equality desire |
| Shuuichi causes musical awakening | `S02 / P0287-P0325` | REVISE | his distinct function is permission without hierarchy, not authorship of Kumiko's ambition |
| `吹きたいです` as desire ownership | `S02 / P0326-P0339` | STRENGTHEN | high-cost artistic desire becomes explicit first-person speech |
| Asuka as mentor | `S02 / P0415-P0489` | STRENGTHEN | post-office mentorship is voluntary, technical, and still wrapped in teasing defense |
| Kumiko wins the soli | `S02 / P0494-P0512` | REVISE | Taki directly selects Reina/Kumiko; no formal audition/win is depicted |
| Illumination possessive intimacy | `S02 / P0599-P0641` | STRENGTHEN | explicit first-experience priority, physical intimacy, mutual possession narration, dyadic happiness |
| Music as hospitality | `S01 / P0094-P0102`; `P0538-P0545` | REVISE | audience-directed accountable authorship, not generic service or preference satisfaction |
| Midori inherits knowledge role | `S02 / P0007-P0027` | STRENGTHEN | stronger: performatively invented tradition becomes real through successor uptake |
| Rhapsody/serenade title symbolism | title architecture | DOWNGRADE | retain as [D/E] pattern inference, not fixed authorial allegorical code |

### V07 source-routing closure

- V1 OCR wording authority: **retired** for V07 where the locked EPUB is available.
- V1 analysis: **historical legacy / revision provenance**.
- V2 current analytical authority: `HIBIKE_V07_DEEP_READING.md`.
- V2 exact-text authority: locked `HIBIKE-V07` EPUB.
- Full narrative + selected paratext deterministic route: `HIBIKE_V07_LOCATOR_INDEX.md`.
- Claim-level disposition totals through V07: **113 STRENGTHEN / 19 PRESERVE / 25 REVISE / 6 DOWNGRADE = 163**.

## HIBIKE-V08 detailed reconciliation — legacy V1 unit 06

| Field | Current routing |
|---|---|
| V2 source | `HIBIKE-V08` — 『響け！ ユーフォニアム　北宇治高校吹奏楽部、波乱の第二楽章 前編』 |
| Locked exact-text authority | `Sound! Euphonium - Novel 08 - Kitauji High School Concert Band Turbulent Second Movement Part 1 [Japanese].epub` |
| SHA-256 | `478652db40270358fa36bede8a835076abe22a86177c251851623850dfc4b8cb` |
| Legacy V1 analytical counterpart | `SOUND! EUPHONIUM — Novel 6.md` |
| V1 numbering relation | legacy unit `06` → **HIBIKE-V08** |
| Current analytical authority | `HIBIKE_V08_DEEP_READING.md` |
| Evidence route | `HIBIKE_V08_LOCATOR_INDEX.md` — 3,308 narrative paragraphs |
| Revision status | **58 claim-level transitions complete** |

### High-priority V1→V2 routing changes

| V1 formulation | V2 clean-text anchor | Transition | Current formulation |
|---|---|---|---|
| Fair system vs trust in fairness | goal/audition rules + Kanade crisis | STRENGTHEN | decompose procedural, epistemic and social legitimacy |
| Unanimous national-gold vote as possible suppression | goal vote | REVISE | sincere unanimity is established; suppression remains a risk hypothesis, not observed fact here |
| Kumiko as institutional listener | Yume/Ririka/Kanade routing | STRENGTHEN | consultation role is now socially recognized but remains non-command authority |
| Tomoe's “selected truth” | `S04 / P0936-P0940` | STRENGTHEN | narration explicitly distinguishes genuine stated reason from exhaustive interior truth |
| Mirei must simply accept social correction | Mirei/Satsuki conflict | REVISE | grievance can be legitimate; later adaptation is self-authored rather than proof she was wrong |
| Motomu fears displacing Natsuki | `S04 / P0603-P0624` | DOWNGRADE | plausible Kumiko inference, not direct Motomu confession |
| Other euphonium selected over Kanade was a senior | Kanade middle-school account | REVISE | source does not establish competitor's year; only another euphonium + older students praising visible effort |
| Kanade ideal-junior persona | V08 broad behavior | STRENGTHEN | multi-register defensive social strategy; not simply fake/real binary |
| Kanade seeks exclusive reassurance from Kumiko | `S03 / P0690-P0720` | REVISE | strong selective senior recognition/testing; strict exclusivity not established |
| Kanade intentional audition loss | `S04 / P1141-P1253` | STRENGTHEN | self-sabotage explicitly protects against anticipated resentment/enemies |
| Natsuki refuses gifted A place | `S04 / P1218-P1236` | STRENGTHEN | seniority becomes responsibility not entitlement |
| `誰も私を望んでくれない` | `S04 / P1251-P1253` | STRENGTHEN | merit cannot answer relational wantedness |
| Kumiko's mistake | `S04 / P1263-P1268` | STRENGTHEN | recognition must precede desired reconciliation |
| `ここは北宇治` as completed institutional proof | `S04 / P1263-P1268` | REVISE | Kumiko's aspirational current-culture claim; selection later supports but does not universalize it |
| Asuka/Kumiko binary intervention styles | restaurant/audition crisis | REVISE | useful contrast but too clean; Kumiko consciously borrows Asuka-like pressure and then diverges |
| Three euphoniums | `S04 / P1331-P1359` | STRENGTHEN | Kanade's assumed zero-sum scarcity is false in actual ensemble configuration |
| Reina private *Liz* performance = explicit philosophy | `S04 / P0863-P0873` | REVISE | Kumiko's focalized interpretation of Reina's performance, not direct Reina self-report |
| Mizore future = autonomous music desire | `S05 / P0006-P0050` | STRENGTHEN V1 caution | opportunity/talent precede autonomy; Nozomi remains explicit causal criterion |

### V08 source-routing closure

- V1 OCR wording authority: **retired** for V08 where locked EPUB is available.
- V1 analysis: **historical legacy / revision provenance**.
- V2 current analytical authority: `HIBIKE_V08_DEEP_READING.md`.
- V2 exact-text authority: locked `HIBIKE-V08` EPUB.
- Deterministic route: `HIBIKE_V08_LOCATOR_INDEX.md`.
- V08 transitions: **45 STRENGTHEN / 3 PRESERVE / 9 REVISE / 1 DOWNGRADE = 58**.
- Cumulative through V08: **158 STRENGTHEN / 22 PRESERVE / 34 REVISE / 7 DOWNGRADE = 221**.
- Next legacy route: unit `07` → **HIBIKE-V09**.


## HIBIKE-V09 detailed reconciliation — legacy V1 unit 07

| Field | Current routing |
|---|---|
| V2 source | `HIBIKE-V09` — 『響け！ ユーフォニアム　北宇治高校吹奏楽部、波乱の第二楽章 後編』 |
| Locked exact-text authority | `Sound! Euphonium - Novel 09 - Kitauji High School Concert Band Turbulent Second Movement Part 2 [Japanese].epub` |
| SHA-256 | `3a5249c76be8618cf386fab5a9b3ab307ab424be09d7517665c77305fdbd1fb2` |
| Legacy V1 analytical counterpart | `SOUND! EUPHONIUM — Novel 7.md` |
| V1 numbering relation | legacy unit `07` → **HIBIKE-V09** |
| Current analytical authority | `HIBIKE_V09_DEEP_READING.md` |
| Evidence route | `HIBIKE_V09_LOCATOR_INDEX.md` — 3,213 narrative paragraphs |
| Movement checkpoint | `HIBIKE_V08-V09_CHECKPOINT.md` |
| Revision status | **76 claim-level transitions complete** |

### High-priority V1→V2 routing changes

| V1 formulation | V2 clean-text anchor | Transition | Current formulation |
|---|---|---|---|
| Kitauji plays objectively better than prior national-qualifying year | `HIBIKE-V09 / S05 / P0024-P0030` | REVISE | Yuuko explicitly believes it; objective cross-year superiority is not omniscient narrator fact |
| Nozomi loves music more than Mizore | `S04 / P0808` | DOWNGRADE | direct as Nozomi self-belief/self-justification, not objective comparison of inner love |
| Nozomi is burdened but emotionally detached | S01/S03/S04 | STRENGTHEN/REVISE | discomfort coexists with jealousy, significance-seeking, envy, and disciplined support |
| Mizore is “liberated” from Nozomi | `S04 / P1251-P1307`; `S05 / P0192-P0200` | REVISE | differentiated attachment / gift without required co-presence; love remains |
| Niiyama tells Mizore to express more | `S04 / P0668-P0709` | REVISE | changes representational role from Liz to blue bird, unlocking an inhabitable emotion |
| Mizore's sonority destabilizes ensemble | `S04 / P0730-P0747` | STRENGTHEN | score/tempo remain correct; Taki adapts ensemble around new capacity |
| Kumiko as mature ethical listener | `S04 / P0481-P0553` | REVISE | strong mediator with documented overreach risk and newly acquired epistemic brake |
| care vs hunger | `S04 / P0260-P0275`; `S05 / P0024-P0030` | STRENGTHEN | humane sustainability and competitive hunger remain non-equivalent constraints; loss does not prove care caused defeat |
| Yume coping | `S04 / P0962-P1154`; `S05 / P0246-P0292` | STRENGTHEN | supported exposure via trusted addressee is more durable mechanism than glasses blur alone |
| Team Oumae solves Asuka concentration problem | `S05 / P0312-P0366`; `S06 / P0027-P0037` | REVISE | role split/burden reduction are direct; “answer to Asuka's curse” remains [D/E] synthesis |
| Kumiko breakup as mature agency | `S04 / P1178-P1199`; `S05 / P0377-P0391` | REVISE | self-authored but also defensive simplification of untested role conflict |
| Motomu family relationship revealed | `S04 / P1511-P1545`; `S05 / P0091-P0103` | REVISE | surname link direct; exact family relation remains undisclosed and Midori protects privacy |

### V09 source-routing closure

- V1 OCR wording authority: **retired** for V09 where locked EPUB is available.
- V1 analysis: **historical legacy / revision provenance**.
- V2 current analytical authority: `HIBIKE_V09_DEEP_READING.md`.
- V2 exact-text authority: locked `HIBIKE-V09` EPUB.
- Deterministic route: `HIBIKE_V09_LOCATOR_INDEX.md`.
- V09 transitions: **48 STRENGTHEN / 2 PRESERVE / 25 REVISE / 1 DOWNGRADE = 76**.
- Cumulative through V09: **206 STRENGTHEN / 24 PRESERVE / 59 REVISE / 8 DOWNGRADE = 297**.
- Next legacy route: unit `08` → **HIBIKE-V10**.


## HIBIKE-V10 detailed reconciliation — legacy V1 unit 08

| Field | Current routing |
|---|---|
| V2 source | `HIBIKE-V10` — 『響け！ ユーフォニアム 北宇治高校吹奏楽部のホントの話』 |
| Locked exact-text authority | `Sound! Euphonium - Novel 10 - Kitauji High School Concert Band True Story [Japanese].epub` |
| SHA-256 | `04ae787ac0b852b5b83cf2077d602a242b31dd9c39b4e0fc71fb5467e3c477c1` |
| Legacy V1 analytical counterpart | `SOUND! EUPHONIUM — Novel 8.md` |
| V1 numbering relation | legacy unit `08` → **HIBIKE-V10** |
| Current analytical authority | `HIBIKE_V10_DEEP_READING.md` |
| Evidence route | `HIBIKE_V10_LOCATOR_INDEX.md` — **2,366 narrative paragraphs / 13 stories** |
| Revision status | **108 claim-level transitions complete** |

### Structural correspondence

V1's unit 08 already recognized the book as an ensemble of perspectives, but V2 formalizes the reconstruction consequence: **twelve alternate centers surround one long Kumiko-centered S12 institutional novella**, making V10 a deliberate anti-overfitting / ordinary-state calibration layer after V08–V09.

### High-priority V1→V2 routing changes

| V1 formulation | V2 clean-text anchor | Transition | Current formulation |
|---|---|---|---|
| Kaori's theory of Asuka's harshness / abandonment tests | `HIBIKE-V10 / S03 / P0066-P0104` | REVISE | high-value **Kaori [C] interpretation**, not direct Asuka motive |
| Taki cannot voice weakness alone | `S08 / P0061-P0067` | REVISE | Chihiro's privileged intimate assessment [C], not narrator-issued interior fact |
| Mirei/Satsuki hair play proves friction-free trust | `S09 / P0062-P0074` | REVISE | real trust plus explicit touch boundary and affective pressure; Mirei's accommodation is locally voluntary |
| Nozomi cannot name admiration | S10 | REVISE | she can name positive feeling toward Yuuko; liking, admiration, envy and comparison can coexist |
| free exit necessarily produces later re-entry | `S04 / P0053-P0103` | REVISE | Aoi's return proves re-entry is possible, not that a single causal law makes it inevitable |
| Ririka is safe for Kanade solely because both perform | S05 | REVISE | mutually legible performance helps; total causal exclusivity is not established |
| Takuya/Riko proves superior relationship ethic | S11 | REVISE | their reciprocal mobility is real; it is not an authorial moral ranking over Kumiko/Shuuichi |
| Team Oumae solves “Asuka's curse” | S12 governance | REVISE | burden-splitting/prospective design are direct; the named doctrine remains analytical synthesis |
| Kumiko filling leftovers would make her emotionally absent | `S12 / P0057-P0063` | REVISE | self-subordination is direct; exact counterfactual psychological outcome is not |
| Reina's musical choice equals total relational priority | `S12 / P0591-P0632` | REVISE | Kumiko entangles them; analysis must keep musical and relational specialness separate |
| Mizore automatically accepts Nozomi-linked requests | `S12 / P0712-P0739` | **REVISE** | directly falsified as a V10 behavioral prediction: Mizore says `私は出ない` and handles gratitude herself |
| Kanade's double-second is a perfectly designed named lesson | `S12 / P1110-P1115` | DOWNGRADE | result is direct; exact authorial pedagogical purpose is inference |
| Yuuko tells Natsuki to burn the letter because she secretly wants preservation | `S13 / P0084-P0086` | REVISE | vulnerability-management reading plausible; hidden preservation wish not established |

### V10 source-routing closure

- V1 OCR wording authority: **retired** for V10 where locked EPUB is available.
- V1 analysis: **historical legacy / revision provenance**.
- V2 current analytical authority: `HIBIKE_V10_DEEP_READING.md`.
- V2 exact-text authority: locked `HIBIKE-V10` EPUB.
- Deterministic route: `HIBIKE_V10_LOCATOR_INDEX.md`.
- V10 transitions: **82 STRENGTHEN / 8 PRESERVE / 17 REVISE / 1 DOWNGRADE = 108**.
- Cumulative through V10: **288 STRENGTHEN / 32 PRESERVE / 76 REVISE / 9 DOWNGRADE = 405**.
- Next legacy route: unit `09` → **HIBIKE-V11**.


## Detailed V11 reconciliation — legacy unit 09 -> HIBIKE-V11

| Field | Current route |
|---|---|
| Locked exact-text authority | `Sound! Euphonium - Novel 11 - Kitauji High School Concert Band Decisive Final Movement Part 1 [Japanese].epub` |
| SHA-256 | `56cc0592af7aff896dbffbb4f23444ee4e497e783a94f1338630bf6c82c0da45` |
| Legacy V1 analytical counterpart | `SOUND! EUPHONIUM — Novel 9.md` |
| V1 numbering relation | legacy unit `09` -> **HIBIKE-V11** |
| Current analytical authority | `HIBIKE_V11_DEEP_READING.md` |
| Evidence route | `HIBIKE_V11_LOCATOR_INDEX.md` — **3,495 narrative paragraphs / 6 segments** |
| Revision status | **164 major transitions complete** |

### High-priority V1 -> V2 routing changes

| Legacy formulation | Transition | Current formulation |
|---|---|---|
| repeated auditions adopted at Mayu's suggestion | **REVISE** | Mayu reports Seira practice; Team Oumae debates/chooses policy |
| Kumiko's current romantic attachment to Shuuichi is straightforwardly present | **REVISE** | affective/romantic residue remains; active relationship is suspended and current intention is not re-declared |
| Mayu self-erasure manipulates the emotional field | **REVISE** | coercive/reassurance-seeking effect can occur; conscious manipulative intent remains unestablished |
| Mayu's relocation philosophy makes sustained commitment difficult | **DOWNGRADE** | plausible predictive hypothesis, not demonstrated incapacity in Part One |
| Mayu photo aversion has a settled relocation/self-alienation cause | **OPEN** | behavior is direct; causal explanation remains underdetermined |
| Midori simply calls Motomu a younger brother | **REVISE** | exact exchange is framed through whether he sees her as an older sister; analogy is not a total mutual label |
| private recognition is simply a technique to neutralize public dissent | **REVISE** | V11 directly supports governance/containment overlap, but care and instrumental management should not be collapsed |
| Taki rejects absolute artistic judgment as a general doctrine | **REVISE** | contextual selection/player agency are direct; universal philosophical claim is stronger than source |
| Reina treats fear as insufficient resolve in all domains | **REVISE** | strongly true in public musical instruction; private relational Reina remains vulnerable and uncertain |
| visual cover/wrapper symbolism is V11 prose authority | **REVISE/DOWNGRADE** | retain as separately classified paratext/visual evidence only |

### V11 closure

- V11 transitions: **129 STRENGTHEN / 10 PRESERVE / 22 REVISE / 2 DOWNGRADE / 0 REJECT / 1 OPEN = 164**.
- Cumulative V01-V11: **417 STRENGTHEN / 42 PRESERVE / 98 REVISE / 11 DOWNGRADE / 0 REJECT / 1 OPEN = 569**.
- V1 OCR wording authority: retired wherever locked V11 EPUB supplies the text.
- Next legacy route: unit `10` -> **HIBIKE-V12**.


## Detailed V12 reconciliation - legacy unit 10 -> HIBIKE-V12

| Field | Current route |
|---|---|
| Locked exact-text authority | `Sound! Euphonium - Novel 12 - Kitauji High School Concert Band Decisive Final Movement Part 2 [Japanese].epub` |
| SHA-256 | `5e98951d0a5e7829d6cc99f37acedb3926a04664d032a17b231dee8242bbf46b` |
| Legacy V1 analytical counterpart | `SOUND! EUPHONIUM - Novel 10.md` |
| V1 numbering relation | legacy unit `10` -> **HIBIKE-V12** |
| Current analytical authority | `HIBIKE_V12_DEEP_READING.md` |
| Evidence route | `HIBIKE_V12_LOCATOR_INDEX.md` - **3,315 narrative paragraphs / 5 segments** |
| Revision status | **184 major transitions complete** |

### High-priority V1 -> V2 routing changes

| Legacy formulation | Transition | Current formulation |
|---|---|---|
| Mayu photo behavior has a clear transfer-history / self-alienation cause | **DOWNGRADE / OPEN** | behavior and motif are direct; causal explanation remains underdetermined |
| remaining behind the camera is proven to make departure easier | **DOWNGRADE** | coherent attachment hypothesis, not direct motive |
| Mayu's self-removal means she secretly wants Kumiko to defeat/reassure her | **REVISE** | withdrawal is a genuine conflict-management value and can pressure others without conscious manipulation |
| Mayu is a Kumiko who never met Reina | **REVISE** | useful analogy only; not causal biography or total model |
| final audition proves Kumiko was always musically superior | **REVISE** | repeated auditions sample changing state/context and do not create timeless scalar hierarchy |
| Kumiko's final freedom is proven to cause the selection result | **REVISE** | plausible mechanism; source does not isolate causal reason for Taki's choice |
| Reina evolves from blind Taki faith to Kumiko's trust model | **REVISE** | she admits Kumiko is also right and apologizes while retaining very strong Taki trust |
| Kumiko/Shuuichi immediately resume a formally labeled dating relationship | **REVISE** | reciprocal romantic love is explicit; exact immediate formal label is less explicit |
| teaching is Kumiko's predetermined correct destiny | **REVISE** | teaching emerges as authored fit after action-generated self-knowledge |
| national gold proves the repeated-audition system was right in every respect | **REVISE** | victory is meaningful but cannot erase social cost, opaque evaluation, or different legitimate value orders |
| cover/illustration composition is prose evidence | **REVISE / DOWNGRADE** | retain only as separately audited F-class visual/paratext evidence |

### V12 source-routing closure

- V1 OCR wording authority: **retired** for V12 where locked EPUB supplies exact text.
- V1 analysis: **historical legacy / revision provenance**.
- V2 current analytical authority: `HIBIKE_V12_DEEP_READING.md`.
- V2 exact-text authority: locked `HIBIKE-V12` EPUB.
- Deterministic route: `HIBIKE_V12_LOCATOR_INDEX.md`.
- V12 transitions: **124 STRENGTHEN / 6 PRESERVE / 49 REVISE / 4 DOWNGRADE / 0 REJECT / 1 OPEN = 184**.
- Cumulative V01-V12: **541 STRENGTHEN / 48 PRESERVE / 147 REVISE / 15 DOWNGRADE / 0 REJECT / 2 OPEN = 753**.
- Legacy sequential V1 audit is now complete through unit `10`.
- HIBIKE-V13 and V14 have no V1 sequential counterparts and enter as V2 source expansion.


## HIBIKE-V13 - V2-only source expansion / no V1 sequential mapping

| Field | Current route |
|---|---|
| Locked exact-text authority | `Sound! Euphonium - Novel 13 - Watching You Take Flight [Japanese].epub` |
| Japanese edition | 『飛び立つ君の背を見上げる』文庫版 |
| SHA-256 | `0728962b4793b2b59911cb332a0db174d47237a6e95011ffa408e2a91a1b733e` |
| Legacy V1 analytical counterpart | **none** |
| V1 numbering relation | **N/A - V2 source expansion** |
| Current analytical authority | `HIBIKE_V13_DEEP_READING.md` |
| Evidence route | `HIBIKE_V13_LOCATOR_INDEX.md` - **2,760 narrative paragraphs / 6 narrative segments + 28 separately indexed F-class commentary paragraphs** |
| Supplemental status | `記憶のイルミネーション` is included in the locked V13 EPUB and is therefore satisfied inside the governing core |
| V1 transition count | **0; cumulative total remains 753** |

### Source-boundary notes

- V13 should never be routed to an OCR/V1 unit by analogy. No such sequential V1 artifact exists.
- The main novel is Natsuki-centered retrospective prose; chapter titles naming Nozomi, Mizore and Yuuko do not themselves change focalizer authority.
- `記憶のイルミネーション` supplies a distinct Nozomi focalization and remains narrative evidence inside V13.
- Yoshida Reiko's commentary is indexed as **F-class paratext** and must not override narrative ambiguity.
- V13 can refine older character/history models but cannot retroactively mutate the frozen V11-V12 checkpoint.

### V13 closure

- V1 OCR wording authority: **not applicable** for this source expansion.
- V2 exact-text authority: locked HIBIKE-V13 EPUB.
- V2 current analytical authority: `HIBIKE_V13_DEEP_READING.md`.
- Deterministic route: `HIBIKE_V13_LOCATOR_INDEX.md`.
- Next V1 crosswalk status: HIBIKE-V14 likewise has no V1 sequential counterpart and should be recorded as V2 source expansion after its reading.

## HIBIKE-V14 - V2-only source expansion / no V1 sequential mapping

| Field | Current route |
|---|---|
| Locked exact-text authority | `Sound! Euphonium - Novel 14 - Kitauji High School Concert Band Everyone's Story [Japanese].epub` |
| Japanese edition | 『響け！ ユーフォニアム 北宇治高校吹奏楽部のみんなの話』 |
| SHA-256 | `b80455a6106a0a3fd54ff59826363d6a7f698efc710c1521e838501dbdfe24e9` |
| Legacy V1 analytical counterpart | **none** |
| V1 numbering relation | **N/A - V2 source expansion** |
| Current analytical authority | `HIBIKE_V14_DEEP_READING.md` |
| Evidence route | `HIBIKE_V14_LOCATOR_INDEX.md` - **2,166 narrative paragraphs / 15 narrative segments** |
| Paratext status | no narrative-adjacent commentary admitted; publisher/author boilerplate excluded from narrative locators |
| V1 transition count | **0; cumulative total remains 753** |

### Source-boundary notes

- V14 is the final sequential source in the **initial locked HIBIKE-V01-V14 core**.
- It must not be mapped by analogy to a V1 OCR/analysis unit; no V1 unit exists.
- Its rotating focalization supplies new direct interior evidence for Kanade, Mirei, Shuuichi, Reina, Sally, Natsuki, Motomu, Mayu, Niiyama, Ririka and Kumiko.
- The long final story supplies post-graduation end-state evidence; do not backport it into V11-V12 local truth.
- S09 is direct Mayu focalization and therefore supersedes speculative causal explanations of her self-adjustment where those explanations conflict with the clean source.

### V14 closure

- V1 OCR wording authority: **not applicable** for this source expansion.
- V2 exact-text authority: locked HIBIKE-V14 EPUB.
- V2 current analytical authority: `HIBIKE_V14_DEEP_READING.md`.
- Deterministic route: `HIBIKE_V14_LOCATOR_INDEX.md`.
- Initial locked-core sequential coverage: **HIBIKE-V01 through HIBIKE-V14 complete**.
- Legacy V1 sequential claim audit remains complete at **753** adjudicated claims.
