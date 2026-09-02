---
series: LLS
artifact_type: ledger
artifact_role: CHARACTER_VOICE_MODEL_LEDGER
scope: through S3E08
generation: V2.2
status: active_provisional
source_boundary: S1E01-S3E08 only
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
mutable_in_place: true
next_update: S3E09
recommended_reasoning_for_next_update: High
season1_frozen_checkpoint: LLS_SEASON1_FROZEN_CHECKPOINT.md
season1_frozen_checkpoint_drive_id: 1EYyIn802sbQftv7Xcs-_Xmq_RNearAq5
season1_checkpoint_status: frozen
season2_frozen_checkpoint: LLS_SEASON2_FROZEN_CHECKPOINT.md
season2_frozen_checkpoint_drive_id: 1a5gTLsDUVMSGCSo8Je_2kVR8admZwvZn
season2_checkpoint_status: frozen
season2_frozen_checkpoint_required_before_next_update: false
next_update_semantic_boundary: S1E01-S3E09 only
---

# Love Live! Superstar!! — Character Voice Model Ledger

## Purpose

Contextual Japanese speech reconstruction for later character modeling. This ledger distinguishes attested linguistic/performance behavior from phrases that merely sound plausible in imitation.

Do not flatten a character into catchphrases. Voice is modeled as **register + pragmatic function + interlocutor + state + recurring linguistic choice**, with acoustic evidence added only where directly supportable.

---

## S1E01 — Shibuya Kanon

### Public aspirational mode

- Can produce a polished self-introduction and articulate a socially legible dream when the dream is still prospective: entering Yuigaoka's music course and making people smile through song.
- Formal evaluative pressure disrupts this mode: entrance-exam self-introduction begins with visible textual hesitation/stammering (`が… 外苑西中学の澁谷かのんです`).

### Private/home colloquial mode

- Uses considerably rougher/casual speech than the aspirational introduction, e.g. `バーカ 歌えたら苦労しないっつーの`.
- The `～っつーの` construction is evidence of colloquial private register here; do not generalize it as a mandatory sentence ending.

### Defensive-minimization mode

- Uses formulations that rhetorically reduce importance: `もう気にしてないし`, `普通科の方が気楽だしね`, `嫌いじゃないけど`.
- Pragmatic pattern: indirect/minimizing phrasing when a direct admission would expose continued investment.

### Other-protective confrontation mode

- Speech becomes direct and sustained when defending Keke: `生半可かどうかなんて分からないでしょ`, `なんでスクールアイドルがダメか ちゃんと説明してあげなよ`.
- This is important for simulation: “hesitant Kanon” is not a globally valid speech style.

### Self-desire under direct pressure

- Ren's direct question produces `私は…` followed by non-completion.
- Acoustic audit records a substantial response gap/energy withdrawal before this answer; use as state-conditioned hesitation evidence, not as a permanent delivery signature.

### Self-authorizing declaration

- Climactic `歌が好きだ！` is maximally direct compared with the earlier `嫌いじゃないけど` / other-directed `歌は大好き` formulations.
- Model implication: directness increases when Kanon stops framing desire as a proposition that requires external qualification.

---

## S1E01 — Tang Keke

- Publicly exposes her school-idol desire with little hedging compared with Kanon's defensive language.
- Japanese subtitles stylize some utterances with forms such as `デス`; treat this as attested textual representation, **not** permission to caricature accent or invent phonetic errors.
- Excitement can trigger multilingual code-switching; exact language use should be recorded case by case.
- Recurrent functional tendency at this boundary: praise and recruitment are highly explicit rather than indirect.
- Insufficient evidence yet for stable intimate/conflict/family voice modes.

---

## S1E01 — Arashi Chisato

- With Kanon, support is phrased through self-positioning rather than imperative: `私はかのんちゃんの歌 聴いていたいけどな`.
- The current evidence supports a familiar, non-commanding mode with Kanon.
- Insufficient evidence at this boundary for broader voice grammar.

---

## S1E01 — Hazuki Ren

- Uses formal/polite register during confrontation.
- Frames objection procedurally/institutionally rather than through casual insult.
- Direct question `あなたもやりたいのですか スクールアイドルを` can be socially penetrating despite formal grammar.
- Do not equate politeness with gentleness or agreement; pragmatic force and register are separate variables.

---

## S1E02 voice updates

### Shibuya Kanon

#### Qualified-ownership mode

- `本気で ちょっとスクールアイドルに興味があるの` combines an intensifier (`本気で`) with mitigation (`ちょっと`).
- Unlike S1E01's defensive minimization, the utterance is complete and followed by sustained action.
- **Model rule:** mitigation in Kanon's speech must be interpreted against behavior/state; after S1E02 it can mark careful exposure rather than disavowal.

#### Principle-confrontation mode

- Uses direct generalized fairness language with Ren: `生徒が集まって やりたいことをやって何がいけないの` and later argues that accepting unilateral control is wrong.
- This mode is more abstract/general than S1E01's immediate defense of Keke.

#### Practical-boundary mode

- Uses quick, direct refusals when a proposal violates practical/social limits: `待って待って`, `やめない 大丈夫`, `それじゃダメ`, `可可ちゃん それは無理`.
- These do not necessarily indicate emotional withdrawal; they often function as boundary-setting.

#### Reflective temporal mode

- The `終わった` repetition at `00:20:41–20:59` builds a retrospective account of failed time before the concise turn `でも やっと始まった / 次の私が 始まった`.
- Model implication: when Kanon achieves conceptual clarity, her language can become structurally simple and declarative even while vulnerability remains.

#### Public-performance uncertainty

- `人がいるから ここじゃ恥ずかしいよ` followed by `歌えるかな` preserves a softer/uncertain mode around being asked to sing publicly.
- The 0.33-second low-level mixed-track interval after `歌えるかな` is AM evidence of a brief acoustic hinge, not a permanent vocal-delivery signature.

### Tang Keke

#### Theatrical mobilization mode

- Public petition rhetoric scales upward quickly: `我々に自由を`, `部活動は常に 皆に平等であるべきデス`, `共に闘おうではありませんか`.
- The grand register is partly comic but clearly attested; model it as an available rhetorical mode when Keke is campaigning, not her universal baseline.

#### First-name self-reference

- Attested examples include `可可 運動苦手デス` and `可可 かのんさんの歌っているところが見たい`.
- Preserve as a recurring candidate pattern; do not force it into every utterance.

#### Relational directness

- `どうしても私はかのんさんとスクールアイドルを始めたい` is unusually explicit about the desired partner.
- At the ending, Keke answers Kanon's capability question with collective imperative language: `響かせましょう` rather than a long reassurance argument.

### Arashi Chisato

#### Familiar teasing mode

- With Kanon: `ちぃちゃんの授業料は高いよ` uses self-nickname and playful mock-transactional framing before sincere help.

#### Coaching mode

- Becomes concise/direct around training: `できる？`, `続けていれば 基礎体力はついてくるから`, `そのあと並行で…`, `でも 2人の実力には合わせないよ`.
- The directness is instructional rather than hostile.

#### Positive diagnostic reframing

- After Keke's rhythm-game boast, Chisato salvages a usable observation: `でも リズム感はあるってことだね`.
- Model implication: coaching speech can convert a comic deficit into a workable strength without denying the deficit.

### Hazuki Ren

- Formal/polite register continues while substantive content becomes harsher: `どうしてもやりたいのであれば 他の学校に行くことですね`.
- Uses institutional-value vocabulary rather than personal insult.
- Under headmistress correction, response compresses to compliant `はい`; current voice model should include deference to recognized higher authority.

### Yuigaoka headmistress

- Institutional language centers jurisdiction and policy: `止める権限はありません`, `本学の方針に沿って…禁止はしません`.
- Corrects Ren's attempted maternal appeal with concise `お母さんはここでは関係ありません`.
- Does not need aesthetic disparagement to exercise authority; speech mode is bounded, administrative, and decisive at this boundary.

### Heanna Sumire

- Public/comic mode includes stylized English/rap-like `YO` insertions in the Manmaru sequence and report (`ないYO`).
- This is an attested performance/persona sample, not yet enough to define her private baseline.


---

## S1E03 voice updates

### Shibuya Kanon

#### Self-reassurance / attempted regulation

- Repetition `大丈夫　大丈夫　大丈夫…` appears when Kanon is not actually behaviorally settled.
- Earlier opening `何でもない　だいじょぶだいじょぶ` similarly shuts down Keke's concern before the problem is resolved.
- **Model rule:** Kanon's `大丈夫` can be performative self-management or social closure, not a reliable literal indicator that she feels safe.

#### Identity-negative explanatory mode

- `たまたまだよ / 今の姿が本当の私なんだよ　きっと` linguistically discounts positive counterevidence while granting ontological authority to the negative state.
- Later self-blame escalates through repeated `私のせいで` and `足手まといにしかならない`.
- This is stronger than ordinary uncertainty; the speech converts situational failure into a totalizing self-description.

#### Action-under-uncertainty mode

- `私　歌ってみる` and `ギリギリまで自分を信じて　やれることを精いっぱい頑張る` avoid false certainty.
- Kanon can become direct about **trying** even when she cannot truthfully become direct about **succeeding**.

#### Intimacy/address request

- `かのんでいい / かのんって呼んでよ` explicitly requests a reduction from `かのんさん` to bare-name address.
- A roughly 1.96 s low-level acoustic interval separates the two Kanon lines; 100 ms median mixed-track level is approximately −65.2 dBFS.
- **Do not record Keke's uptake yet:** Keke does not produce a later audible `かのん` in S1E03 after the request.

#### Performance-capability statement

- `歌える / 一人じゃないから` is causal and relational, not a generalized confidence declaration.
- For simulation, prefer “I can because I am not alone” over paraphrases such as “I'm finally not scared.”

### Tang Keke

#### Adaptive support/directive mode

- When continued pressure is counterproductive, Keke can reverse tactics explicitly: `今は無理に歌おうとするのはやめましょう`.
- She then gives a concrete contingency: she will sing; Kanon need only stand onstage; they can work on singing again afterward.
- This mode is directive but protective rather than demanding.

#### Counter-self-denigration mode

- `自分のことを悪く言わないでクダサイ` is direct prohibition.
- Keke then uses a comic relational inversion: if Kanon denigrates herself, the person who had her heart captured becomes pitiable too.
- This pattern combines humor with very explicit valuation.

#### Reflective autobiographical mode

- S1E03 establishes that Keke can sustain serious explanatory speech about family educational pressure, lack of self-chosen desire, the discovery of school idols, and wanting to sing feelings freely.
- This is important counterevidence to any voice model that overweights stylized `デス`, excitement, or campaigning rhetoric.

#### Elevated relational naming

- Calls Kanon `スター` and `夢`, then specifies that sharing a stage with her is one of Keke's dreams.
- Treat these as load-bearing attested words, not generic compliments to sprinkle into unrelated dialogue.

#### Fandom reverence mode

- Sunny Passion triggers honorific/elevated reference (`サニパ様`, members described with `様`) and highly enthusiastic descriptive language.
- This mode can coexist with temporary strategic tunnel vision.

### Arashi Chisato

#### Clear positive refusal

- `あるよ` answers school-idol interest without hedging.
- The refusal follows through priority language: `私にはダンスがあるの`, `今の私の一番の目標`, `掛け持ちできるほど余裕はない`.
- She does not need to say she dislikes school idols in order to decline.

#### Seriousness norm

- `かのんちゃんも真剣だし　生半可な気持ちではやれない` frames refusal partly as respect for the activity's seriousness.

#### Dyad-aware support

- `2人で過ごす時間も大事だよ / ステージに立つのは君たちなんだから` is a concise relational-boundary statement: Chisato names when her own presence should recede.

### Hazuki Ren

- Prestige/reputation vocabulary persists: `醜態をさらせば　この学校の評判にも関わります`.
- Formal grammar remains compatible with severe negative judgment.

### Heanna Sumire

- Theatrical self-commentary remains available under mishap/visibility conditions (`やっちゃったったらやっちゃったのよ`).
- Evidence still favors a conspicuous public/performance register; private baseline remains underdetermined.

---

## S1E04 voice updates

### Tang Keke

#### Bare-name Kanon — confirmed uptake

- S1E03 left `かのん` uptake open after Kanon requested `かのんって呼んでよ`.
- S1E04 repeatedly attests bare-name use: `かのん 怖いのデスカ`, `かのんがいいデス`, `かのんのほうが…`.
- No story-dialogue `かのんさん` occurs.
- **Model rule:** from the S1E04 boundary onward, default Keke→Kanon address is bare `かのん` unless a later context specifically establishes a reversion/formal shift.

#### Recruitment-overdrive mode

- Tentative `ちょっと興味` is answered with `今日からあなたもスクールアイドルデス`.
- Speech becomes declarative/accelerating before Sumire has actually consented; Kanon slows the interaction.

#### Sacred-domain anger mode

- `それはスクールアイドルに対する侮辱デス / 冒涜デス`.
- Rough comic imperative: `お昼休みに屋上に来やがれデス`, `いいから 来やがれデス`.
- The coexistence of `来やがれ` with stylized `デス` is directly attested. Use only under strong value-protective anger/comic escalation.

#### Center-language mode

- Uses `カリスマ性`, later `オーラ` / `華` to argue that center suitability exceeds visible technical skill.
- This is conceptual vocabulary available in performance/group-governance contexts, not generic everyday speech.

### Heanna Sumire

#### Theatrical emphatic `ったら`

Recurring S1E04 examples:

- `やるわったらやってやるわ`
- `納得できないったらできないの`
- `いくら出すったら出すのよ`

**Model rule:** `～ったら` is now a strong candidate signature for intensified theatrical insistence/frustration. It is not mandatory sentence decoration.

#### `ギャラクシー` self-branding

- Appears at heightened visibility/excitement points and at the final contribution scene.
- Do not overgenerate: long serious conversations in the same episode omit it entirely.

#### Status/directness mode

- `スカウトじゃないなら 声かけないで` is unusually brusque and directly exposes preoccupation with scouting.
- `センターになれないんだったら こんなところいる意味ないもの` converts status disappointment into categorical membership language.

#### Vulnerable autobiographical mode

- `私ね 小さい頃からずっと…` initiates sustained explanatory speech about auditions, main-role aspiration, effort, and minor roles.
- Fatalistic conclusion becomes concise/absolute: `そういう星のもとに生まれているの`; `どんなに頑張っても 真ん中で輝くことはできない`.
- Simulation must permit serious unbranded speech; “Galaxy Sumire at all times” is inaccurate.

#### Professional-pride conflict mode

- `ショービジネスの世界を甘く見ないで`; `これくらいはできるの`; `こんなアマチュアの世界でもね`.
- Directly challenges Keke through competence/status language rather than apologetic retreat.

#### Contractual humor as pride-protection

- After Kanon's emotionally specific scouting, Sumire shifts into `いくら出すのよ` / `契約金は必要よ`.
- The joke lets her accept being wanted without immediately answering in exposed sentimental language.

### Shibuya Kanon

#### Explicit school-idol ownership

- `それはできない` precedes a direct account of why she wants more/better school-idol performance.
- Compared with S1E02's mitigated `ちょっと興味`, this is substantially less hedged activity-specific commitment.

#### Recruitment-mirroring formal mode

- `平安名すみれさん / 私 こういう者です / すみれさん あなたをスカウトに来ました`.
- This is strategic formality/role-play chosen to mirror Sumire's recognition script; do not treat as baseline peer register.

#### Competitive invitation

- `センターが欲しかったら 奪いに来てよ` is direct and challenging, followed by the cooperative rationale `競い合えば グループもきっと良くなる`.
- Kanon can therefore use confrontation language affiliatively when it preserves another person's agency.

### Hazuki Ren

- Formal/polite register remains stable while content is domain-specific and severe.
- `スクールアイドルじゃなければ いくらでも応援してあげられますから` distinguishes opposition to the activity from hostility toward the girls.
- `今の「ラブライブ！」で あなたたちが勝てるとはとても思えません` is predictive evaluative language, not insult register.

### Yuigaoka headmistress

- Continues concise institutional language.
- `努力しようとする者からその場を奪うのが良いことだとは思いません` states a norm through general principle rather than personalized reassurance.
- Maternal appeal is framed as a rhetorical ethical question: `そう言うと思いませんか あなたのお母さんも`.


---

## S1E05 voice updates

### Arashi Chisato

#### Formal deliberation

- `少し 考えさせてください` is restrained, formally appropriate language when asked to accept Yuigaoka's summer dance-representative role.
- It follows an approximately **4.51 s** low-energy mixed-track interval after the question, supporting deliberate staging without licensing a specific subjective-emotion label.

#### Self-authored separation

- `夏休みは別行動をとろうと思うんだ` explicitly foregrounds a deliberate separate course of action.
- `スケジュール重なっちゃってごめんね` keeps the separation relationally considerate rather than defensive.

#### Modest helper label

- `私はお手伝いで` minimizes formal status despite substantial technical influence.
- For simulation, do not equate this self-description with low actual importance to the trio's dance infrastructure.

### Shibuya Kanon

#### Fairness register

- `もしそれで許可が出ても 他の普通科の子に悪いよ / 同じ学校なのに` is concise moral reasoning rather than bureaucratic argument.
- The repeated school-membership frame makes equal standing more important than group convenience.

#### Stage-seeking school-idol mode

- `出たいです / 出演させてください` is direct polite acceptance.
- `私たち 今歌える場所があったら どんどん歌いたい` expresses expansion rather than hesitation; by S1E05 Kanon can speak as someone actively seeking performance opportunities.

#### Relational-category questioning

- `ちぃちゃんって何なんだろう` is a bare, compact question that precedes a search for adequate relational language.
- `一緒にやっているわけでもないし / コーチでもないし` resists easy categorical naming.
- A roughly **1.04 s** low-energy interval follows the question before Keke answers.

#### Instrumental desire disclosed without euphemism

- `私 可可ちゃんのためにも スクールアイドルで結果出したい` admits that results matter relationally.
- Kanon does not hide that Chisato joining would be useful; subsequent childhood reflection complicates rather than erases the practical desire.

### Tang Keke

#### Bare-name Kanon — PRESERVE

- Bare `かのん` remains the stable Keke→Kanon address form in S1E05, strengthening the S1E04 transition.

#### Hyperbolic commitment

- Recurring `この命に代えましても…` / life-staking formulations appear in comic high-enthusiasm contexts.
- Other members explicitly push back (`いちいち命に代えないの`), so the model should retain both Keke's hyperbole and the group's normalization/correction of it.

#### Fandom over-formality / reverence

- Sunny Passion continues to elicit unusually elevated enthusiasm and deference.
- Treat this as idol/fandom-conditioned voice, not baseline speech with peers.

#### Self-report under physical overextension

- Keke's verbal insistence on continuing can conflict with visible bodily limits. In simulation, explicit “I'm fine / I can continue” style content should be checked against context rather than accepted as a perfect state report.

### Heanna Sumire

#### Irritated caretaking

- `いいから あんたは水飲みなさい` is direct, rough, and practical.
- `あんた 何かある度に倒れているわね` combines complaint with pattern recognition.
- This register can be caring without becoming soft or explicitly affectionate.

#### Formal guest etiquette

- `これ ささやかなものですが` shows access to conventional polite gift-giving language with hosts.
- This is useful counterevidence to a voice model dominated by `ギャラクシー` and combative `ったら` forms.

#### Competitive/playful show-business mode

- During thumb wrestling, Sumire can use misdirection and then narrativize it as `これがショウビジネスの世界 / 油断した方が負けなの`.
- Show-business vocabulary therefore also functions as playful self-mythologizing in low-stakes peer conflict.

### Sunny Passion

- Collective voice currently combines informal hospitality with precise performance criticism.
- `どこか自分たちで動いてる感じがしないんだ` and `自分たちで動いていく力強さ` should be preserved as **self-directed/self-propelled agency** language, not flattened into “authenticity.”
- Individual member voice models remain underdetermined; do not overfit a collective sample into separate personalities yet.

## Dual-subtitle pressure notes from S1E05

The paired English track remains useful specifically where localization can shift analytical category:

- JP `自分たちで動いてる感じがしない` / `自分たちで動いていく力強さ` emphasizes acting/moving under one's own power; an English “moving as themselves” wording can invite a stronger authenticity/identity reading than the Japanese warrants.
- `そんなにかしこまらないでよ` is closer to “don't be so formal / stand on ceremony” than a self-esteem reassurance such as “don't put yourself down.”
- `一緒にやっているわけでもないし` is deliberately less categorical than simply “she's not a member.”
- `夏休みは別行動をとろうと思うんだ` foregrounds Chisato's chosen separate action more strongly than a generic “I'll be busy.”

## Acoustic/performance rule

V2.2 may attach pause duration, overlap, RMS/dBFS change, onset/offset, or other AM evidence to a voice state. It must not infer unsupported timbre, precise accent quality, or instrument/vocal emotion labels merely from spectral numbers.

S1E05 adds useful acoustic hinges:

- ~**4.51 s** low-energy interval before Chisato's `少し 考えさせてください` (~−50.3 dBFS RMS);
- ~**4.18 s** lower-energy reaction interval after Sunny Passion's agency critique (~−36.3 dBFS RMS; median 100 ms ~−40.5 dBFS);
- ~**1.04 s** low-energy interval after Kanon's `ちぃちゃんって何なんだろう` (~−50.1 dBFS RMS);
- ~**15.05 s** transition after Kanon's desire to put Chisato's meaning into song before Chisato's final `よし`, with the final utterance itself around −29.0 dBFS RMS.

## S1E06 voice updates

### Arashi Chisato

#### Self-minimizing withheld-disclosure mode

- `いや 私は大したことじゃないから`
- `ただ 大会が終わったら`
- `やっぱり何でもない`

The content is demonstrably high-stakes despite minimization. A roughly **3.01 s** lower-energy interval follows `大会が終わったら` before withdrawal (`~−38.89 dBFS RMS`, 100 ms median ~−42.57 dBFS).

**Model rule:** with Kanon, `大したことじゃない` can function as burden-avoidant postponement rather than genuine trivialization.

#### Independence/qualification lexicon

High-density recurrence:

- `一人でできるようにならなきゃ`
- `一人で結果を出して`
- `自分に自信を持てるようになりたい`
- `自分で決めたこと`
- `自分で思えるまでは`
- `一人で頑張らなきゃいけない`

Use this lexicon primarily when competence, equality with Kanon, or self-proof is activated; do not turn `一人` into a universal catchphrase.

#### Self-condemnation after relief

- `やっぱりダメだな`
- `悪いのは弱い私`

The language converts a state-dependent experience (feeling relieved by Kanon's arrival) into a global negative self-assessment. Preserve as a stress mode, not narrator truth.

#### Light grammar can carry extreme stakes

`海外で修業するのも悪くないなって` occurs inside the explanation of a prepared school-withdrawal contingency. Textual casualness/understatement should not automatically be interpreted as low importance.

#### Side-by-side/equality language

`かのんちゃんの横に立てる人になりたくて` is central. Preserve `横に立てる` as equality/co-presence imagery rather than reducing it to generic “help.”

### Shibuya Kanon

#### Epistemically careful intervention

- `勘違いかもしれないけど`
- `私が伝えたかったのは一つだけ`
- `私 いつもちぃちゃんのこと尊敬してる`

Kanon can intervene decisively while marking that her reading of the other's state may be wrong. This is a high-value simulation distinction from omniscient/confident reassurance.

#### Symmetry/reframing mode

- `じゃあ 2人一緒だね`
- `2人とも頑張ってきた`
- `お互いがお互いを見て お互いを大切に思って`

When Kanon finds a relational conceptual core, speech can become short and declarative. Here directness functions as model correction, not command.

#### Causal gratitude

`あの言葉があったから 私 今こうして歌っていられる` is unusually explicit about Chisato's causal importance. Use as evidence that Kanon can articulate debt/gratitude without converting it into inferiority.

#### Emerging service-purpose register

- `いろんな人の力になりたい`
- `みんなのために歌いたい`

This is attested reflective speech about school-idol purpose, not yet a mandatory slogan.

#### Provisional self-regulation

`今はそう思うようにしています` must remain distinct from simple `そう思います`. The form presents a view Kanon is consciously trying to maintain.

#### Long-felt dream articulation

`ずっと夢見ていた気がする / こういう日が来ることを` combines `ずっと` with epistemic/retrospective `気がする`. Preserve the under-specified, reflective quality; do not rewrite it as a precise childhood plan.

### Hazuki Ren

#### Personal-concern hesitation

Short forms such as `あの…`, `いえ`, and the attempt to explain accidental discovery appear before serious questions. Formal register remains, but force is lower/more tentative than Ren's institutional prohibitions.

**Model rule:** Ren's politeness does not uniquely map to cold gatekeeping; it can also carry personal concern and uncertainty.

### Tang Keke

#### Reciprocal-debt comedy

`これで夕食の借りは返しましたよ / ザ・チャラ デス` uses stylized language to perform actual relationship accounting. Keke can make reciprocity explicit through comic grandiosity.

#### Fandom/effort mode — preserve

Sunny Passion proximity continues to support excited, high-output speech and bodily overextension. Do not infer that verbal enthusiasm means sustainable physical capacity.

### Heanna Sumire

#### Professional face-management doctrine

`笑顔で堂々としているのも ショウビジネスの世界では必要なこと` continues her tendency to formulate show-business behaviors as explicit professional rules.

This register is increasingly backed by practical contribution, not merely self-branding.

## Dual-subtitle pressure notes from S1E06

- JP `今はそう思うようにしています` is more provisional/self-regulatory than the paired English formulation; Japanese governs Kanon's state.
- JP `かのんちゃんと一緒に何かやるのはやめよう` concerns doing something together until Chisato's threshold is met, not ceasing ordinary contact with Kanon.
- `横に立てる` carries side-by-side/equality structure that a generic “help” gloss can flatten.
- Visual JP text distinguishes `退学届` from later `転科届`; subtitle-only reading would miss a crucial institutional contrast.

## Acoustic/performance rule additions

- ~**3.01 s** lower-energy gap after Chisato's `ただ 大会が終わったら` before `やっぱり何でもない` (RMS ~−38.89 dBFS; 100 ms median ~−42.57).
- ~**3.13 s** very low-energy gap after Kanon's incomplete `だから…` before Chisato `やっぱりダメだな` (RMS ~−48.59; median ~−49.39; 77.4% of 100 ms blocks below −45).
- ~**5.76 s** pronounced pre-performance low-energy interval after `こういう日が来ることを` and before `さあ いきますよ` (RMS ~−38.36; 100 ms median ~−51.63; 96.5% blocks below −45).

These remain mixed-track structural measurements, not claims about subjective timbre/emotion.

## S1E07 voice updates

### Arashi Chisato

#### Low-drama commitment mode

- `やろうかなって` and `そんな大したことじゃないけど` accompany decisions that are objectively large: school-idol membership and course transfer.
- **Model rule:** Chisato can linguistically understate major commitments once she has internally resolved them; lack of grand rhetoric does not imply weak investment.

#### Internal-specialist coaching mode

- `これからは前よりもみっちりダンスの練習するんだから` preserves direct instructional authority after she becomes a member.
- Membership changes role location, not the existence of domain expertise.

### Shibuya Kanon

#### Categorical consent refusal

- `嫌だ 絶対に出ない` is short, unmitigated, and directed toward close collaborators when they assign her an unwanted formal role.
- **Model rule:** relational warmth does not eliminate hard-boundary speech.

#### Epistemic-care / hidden-reason mode

- `理由が知りたいんだ` is paired with a practical purpose: if she understands why, they may find another method.
- Later `確かにそんな気もするけど / それにしても 何か理由がある気がするんだよねえ` preserves uncertainty.
- The paired English tends to make the latter more categorical (“I'm sure”); **Japanese governs**. The construction is inference-with-reservation, consistent with S1E06 `勘違いかもしれないけど`.

#### Normative conviction without personal essentialization

- `葉月さんは受け入れられないのかもしれないけど / スクールアイドルはやっぱり悪いものじゃないって思うから` allows Kanon to oppose Ren's position without converting Ren into a malicious person.

#### Self-scaling / visibility lag

- `ほら 私なんて全然目立たないし` uses `私なんて` to downscale Kanon's own public prominence.
- Sumire's reaction makes the formulation socially salient/irritating.
- **Do not** automatically convert this into a global insecurity catchphrase; current evidence supports possible lag between self-image and externally visible centrality.

### Tang Keke

#### Pseudo-legal threat theater

- Under anxiety about Ren's potential authority, Keke invents exaggerated rule numbers and enforcement language (`校則第10条325項`, `ひっ捕らえなさい`).
- This extends her theatrical mobilization register into bureaucratic dystopia/comedy.
- **Model rule:** use only when a valued activity feels institutionally threatened; it is not literal knowledge of school rules.

#### Role-imposition language

- Campaign preparation precedes Kanon's consent. Keke's speech treats Kanon's candidacy as a solution already in motion rather than a proposal needing permission.
- This is a pragmatic pattern more than a lexical tic.

### Heanna Sumire

#### Electoral `ギャラクシー`

- `ギャラクシーな一票を` adapts self-branding to campaign rhetoric.
- Her persona is portable across public-performance domains even when the domain is a poor fit for her actual goals.

#### Humiliation emphasis

- `なんでったらなんで` confirms `～ったら` remains available under frustrated public defeat.
- Unlike S1E04, the emphatic register is followed by comic rebound rather than existential/fatalistic language.

### Hazuki Ren

#### Inaugural institutional register

- `改めまして この学校の初代生徒会長に任命された 葉月恋です`
- `この名誉ある仕事につくことができ 光栄であると同時に`
- `誠心誠意努力する所存です`
- These are among Ren's most formal public formulations so far and should be available specifically for ceremonial/institutional speech.

#### Community-continuity vocabulary

- `この結ヶ丘女子を地域に根ざし / 途切れることなく続いていく学校にするために` explicitly uses **`地域` = local community/region**.
- Paired English pressure may redirect this toward “tradition”; do not import that semantic substitution into the Japanese voice model.

#### Policy-transition hesitation

- Repeated `そのために…` is separated by two pronounced low-energy intervals before the music-course-centered festival announcement.
- First gap: ~4.26 s, mixed RMS ~−44.54 dBFS, ~90.5% of 100-ms blocks below −45.
- Second gap: ~4.42 s, RMS ~−50.38 dBFS, ~97.7% below −45.
- **Voice rule:** formal register can contain extended hesitation at a high-stakes commitment conflict. Acoustic evidence does not identify the emotion causing it.

#### Private formal self-containment

- Even in the household disclosure, Ren remains formal: `平気ですよ`, `悲観しているのではありませんよ`.
- There is no evidence yet of a radically casual private baseline.

#### Solitary-obligation grammar

- `母が残した学校を続けるためには / わたくしが頑張るしかない` uses `しかない` to linguistically remove alternatives.
- **Model rule:** under inherited-duty/survival pressure, Ren can frame effort as compulsory personal necessity rather than collective choice.

#### Domestic dog-command code-switching

- `Come` / `Sit` / `Stay` are directly attested with Chibi.
- Preserve as narrow domestic texture; do not generalize English-command use to unrelated contexts without recurrence.

## Dual-subtitle pressure notes from S1E07

- `地域に根ざし` must remain local-community/region rootedness; paired English can overemphasize “tradition.”
- `きっと…何か理由がある気がする` is more epistemically qualified than a categorical “I'm sure.”
- `音楽科をメイン` establishes the music course as the **main focus** of the festival; it does not by itself say ordinary-course students are totally excluded.

## Acoustic/performance rule additions

- Ren's polished preceding inaugural phrase is around −29.38 dBFS mixed RMS; the two subsequent `そのために…` gaps drop sharply to approximately −44.54 and −50.38 dBFS before the controversial policy announcement.
- A short ~0.50 s hinge after `そのままの意味です` before `この家に残っているのはわたくし一人` measures ~−64.65 dBFS with all 100-ms blocks below −50. Treat as a brief structural hinge, not evidence of a named emotional state.
- The ~5.08 s delay after `別に何もありません` before Ren's school-centered explanation retains active soundtrack energy (~−37.3 dBFS), so it should **not** be described as silence.


---

## S1E08 voice updates

### Shibuya Kanon

#### Conviction plus source-verification language

- `スクールアイドル活動を後悔していたようにはどうしても思えない` expresses strong conviction, but Kanon does **not** convert conviction into certainty about Ren's mother.
- `私 確かめたい` moves directly from disagreement to verification.
- **Voice rule:** Kanon's epistemic-care mode can combine strong felt inconsistency with an explicit demand for evidence rather than a categorical claim about another person's inner state.

#### Public-attention acknowledgment without withdrawal

- At the assembly, `すごい注目されてる` directly registers attention.
- She nevertheless proceeds with the chosen speech after a measurable low-energy interval (~8.47 s; mixed RMS ~−42.32 dBFS).
- Do not rewrite this as confident stage ease; speech and singing remain different tasks.

#### Self-correcting motive language

- `この学校のために… / いや / この場所でつくられた たくさんの想いのために` is a directly attested self-repair.
- **Model rule:** when an institutional/utilitarian formulation feels insufficient, Kanon can interrupt herself and replace it with more relational language.
- Preserve `想い` as a broad field of feelings/wishes/attachments; English “memories” is narrower.

#### Beginning-oriented self-description

- `そんなことないよ / ただ 私ね 始まりの瞬間が好きなの` rejects Ren's global `強い` characterization and substitutes a situational self-theory.
- Use as a candidate recurring concept, not a mandatory philosophical line in imitation.

#### Ren address shift

- Moves from `葉月さん` to `恋ちゃん` at the invitation threshold.
- This is a relationally marked change, not permission to use `恋ちゃん` retroactively in earlier states.

### Hazuki Ren

#### Legacy-hypothesis modality

- `もしかしたら 母は後悔していたのではないか` and `...感じていたのではないかと` are explicitly inferential.
- **Voice rule:** even when Ren has governed policy around the inference, her explanatory language can preserve grammatical uncertainty rather than falsely claiming maternal testimony.

#### Domain-exception prohibition

- `ただ スクールアイドルは… / スクールアイドルだけはやめてほしいのです` marks school idols as the exceptional prohibited case after she concedes broader shared-festival participation.
- The ~3.17 s low-energy interval after the first fragment is a formal hinge, not proof of a named emotion.

#### Guilt/self-disqualification register

- `今まで澁谷さんたちの邪魔をし続けてしまったわたくしに / そのような資格は…` frames membership through moral qualification and trails off.
- Contrast later behavior: she accepts participation when others define the relation through present desire rather than eligibility accounting.

#### Kanon address shift

- Later `かのんさん` replaces earlier `澁谷さん` in a more affiliative state.
- Maintain `さん` and Ren's formal grammar; reduced distance does not produce a casual speech collapse.

### Tang Keke

#### Rapid nickname affiliation

- `レンレン` is directly attested shortly after Ren's incorporation.
- Treat as a Keke-specific affiliative nickname, not evidence that all peers use it.

#### Multilingual welcome

- `私たちはいつでも欢迎欢迎ですよ` embeds repeated Chinese `欢迎` inside Japanese grammar.
- This is strong direct evidence for multilingual code-switching under excited affiliative conditions.
- Do not invent arbitrary Chinese phrases outside attested/contextually warranted modes.

### Heanna Sumire

#### Future-stage center framing

- `私はセンターをやるのは もっと大きなステージって決めているから` is less wounded/defensive than S1E04 center language.
- Voice model should permit strategic, future-oriented center claims rather than assuming every center discussion triggers `ったら` escalation.

### Yuigaoka headmistress

#### Public administrative vs private familiar register

- S1E08 explicitly exposes a more casual private/familiar register and includes `もともとはこういう性格なの`.
- Preserve the contrast with her concise institutional mode from S1E02.
- The register switch is evidence of contextual voice variation, not inconsistency.

## Dual-subtitle pressure notes from S1E08

- `想い` should not be flattened to English “memories”; in the episode it carries wishes, feelings, attachments, inherited aspiration, and relational accumulation.
- `結` / `結ばれる` forms an explicit lexical architecture across school name, maternal dream, institutional purpose, and final performance language.
- The paired English insertion of “grudge” around `少なくとも私らには何にも関係ないことだもんね` is stronger/more personalized than the Japanese wording and should not govern character modeling.
- Some English pairing around comic lines is timing-misaligned; paired-track coverage is high but not evidence of one-to-one cue identity.
- `自分たちがつくっていく` retains a direct self-agency recurrence with S1E05's `自分たちで` language that English paraphrase can partially obscure.

## Acoustic/performance rule additions

- Ren's school-idol exception has a ~3.17 s low-energy hinge after `ただ スクールアイドルは…`; mixed RMS ~−38.24 dBFS, median ~−47.99 dBFS. Call it a marked mixed-track withdrawal, not silence.
- Kanon's school-assembly attention acknowledgment is followed by ~8.47 s of low-energy mixed track (~−42.32 dBFS RMS) before she continues.
- Ren's fragmented `最高の… / 思い出…` response after the notebook interpretation is **music-filled**, with gaps roughly −27.5 and −30.0 dBFS; do not describe them as silence.
- The final chant-to-`Wish Song` boundary is acoustically continuous/active; measured song core is roughly −18.33 dBFS mixed RMS. The performance functions as a continuation of the collective declaration rather than an acoustically isolated reset.


## S1E09 voice updates

### Shibuya Kanon

#### Workload-boundary mode

- `ずるいよ 私にばっかり押しつけて` / `みんな私に頼りすぎなんだよ` are direct complaints about unequal task allocation.
- These lines should not be rewritten as hidden self-hatred: at this boundary Kanon can object to overreliance while remaining a group member and continuing the task.

#### Mediated-visibility embarrassment

- During livestream preparation Kanon attempts to remain on the filming side and later says `恥ずかしいからやめよっか`.
- Public assembly competence therefore does not generalize to effortless comfort with casual livestream exposure.

#### Exploratory synthesis mode

- After being told the group is still `真っ白`, Kanon initially answers only `そうかな` rather than mounting a rebuttal.
- Later: `分からないけど` → low-energy pause → `でも` → `何かこの5人が何なのか分かった気がした`.
- Her final explanation of `Liella!` becomes fluent and metaphorically structured around `結ぶ`, `いろんな色の光`, `何色でもない`, and forms they themselves cannot yet imagine.
- **Model rule:** uncertainty markers can precede—not negate—highly generative conceptual speech once an internal synthesis is forming.

### Hazuki Ren

#### Formal digital-novice mode

- `動画配信とは何なのですか` / `動画を配るのですか どこかに` are literal Japanese questions about an unfamiliar medium.
- Do **not** import the English subtitle's river/stream pun as Japanese characterization.
- Her trial livestream begins with full institutional self-positioning: `わたくし結ヶ丘女子高等学校の生徒会長をしております / 葉月恋と申します`.
- When she learns the stream has begun without sufficient notice: `こんなの断りもなく始めないでください / すぐ切ってください`.
- Formality remains her default tool even inside comic unfamiliarity.

#### Kanon address / peer accountability

- Repeated `かのんさん` strengthens the post-S1E08 first-name-plus-honorific relationship state.
- `ずるいですよ / わたくしたちだけに押しつけて` demonstrates that polite grammar can carry direct peer accusation inside the group.

#### Competition-from-within mode

- `勝たないといけませんね` shows that Ren's excellence/competitive vocabulary survives incorporation and is now expressed as shared group obligation rather than exclusionary gatekeeping.

### Tang Keke

#### Love Live urgency / mobilization

- Competition explanation and promotional planning produce Keke's familiar high-energy, declarative mode.
- Stylized subtitle spellings/comic pronunciation should remain exact-locator evidence only and must not be generalized into invented phonetic caricature.
- `レンレン` is **not re-attested in S1E09**. Preserve it as an available S1E08 affiliative form, not a mandatory default.

### Heanna Sumire

#### Show-business evaluative mode

- `ショウビジネス的には致命的よね それって` turns an abstract identity problem into a professional branding diagnosis.
- Jingu Stadium activates explicit large-audience fantasy language (`何万人もの注目`) and `ギャラクシー` self-branding.
- She can nevertheless accept another naming proposal with understated `悪くないんじゃない`, demonstrating that theatrical branding language does not monopolize all evaluative speech.

### Arashi Chisato

#### Evidence-based optimism

- When evaluating Love Live prospects, Chisato names concrete member capacities rather than asserting vague confidence.
- Her speech remains concise and domain-aware: optimism is bounded by `勝てるかどうかは分からない`-type uncertainty rather than inflated certainty.

## Dual-subtitle pressure notes from S1E09

- English's livestream/river joke should not be imported into Ren's Japanese voice; the Japanese supports literal unfamiliarity, not the same pun structure.
- `何色でもない` is more literally a **not-yet-any-color** formulation than English “blank canvas.” The English is thematically compatible but loses the episode's recurring color/light grammar.
- Naming semantics should preserve Kanon's own wording that `Liella!` was made from a French word meaning `結ぶ`; do not substitute later franchise etymology into the sealed S1E09 record.

## Acoustic/performance rule additions

- After Kanon's `そうかな`, a ~3.34 s low-energy interval precedes Chisato's call; 100 ms median mixed-track level is about −60.6 dBFS. Treat as a marked processing hinge, not proof of a named emotion.
- After `分からないけど`, the ~1.46 s interval before `でも` is strongly low-energy (median about −63.8 dBFS); the following interval before `ぜーんぶ` becomes much more acoustically active.
- The insert song begins only ~0.37 s after Kanon's spoken `何かこの5人が何なのか分かった気がした` begins, overlapping the act of verbal definition. Music enters **inside** the identity formulation.
- Name acceptance and the final `私たちの名は` transition remain acoustically active rather than being isolated by silence.

## Next step

S1E10 should test speech under formal Love Live pressure: whether Ren's `かのんさん` and Keke/Ren distance stabilize, whether Liella! develops group-internal naming conventions, and how competition changes each member's public/private register.

**Recommended reasoning:** High.

## S1E10 voice updates

### Shibuya Kanon

#### Future-oriented anti-determinist mode

- `それ言ったら私だって歌えなかったよ / 今までは今まで / 大切なのはこれからだよ` is concise, autobiographically grounded counterargument rather than generic cheerleading.
- The follow-up `そうそう Liella!と同じで / これからいろいろ始まっていいんじゃないかな` turns the new group identity into permissive future grammar.
- **Model rule:** when Kanon reaches a relationally workable formulation, she can reject deterministic precedent with simple past/future contrast rather than ornate motivational speech.

#### Task-limitation without self-denigration

- Rap attempt produces `こ… 言葉が… / 出てこない`, followed by continued collaboration rather than identity-negative explanation.
- Do not map every Kanon hesitation onto the S1E03 burden/stage-fright register; task form and enacted response must be checked.

### Tang Keke

#### Sacred Love Live! / standards mode

- Load-bearing examples: `大切なラブライブ！の最初の課題`, `スクールアイドルを甘く見たら承知しません`, `本気で頂点を目指すつもりでいてクダサイ`, `神聖なラブライブ！`.
- The stylized `デス/クダサイ` register coexists with genuinely consequential evaluation; do not classify the mode as joke-only.

#### Evidence-based recognition while remaining forceful

- `可可があなたに任せたのは / あなたがふさわしいと思ったからデス` and `練習を見て その歌声を聴いて` are precise evaluative explanations.
- Recognition does not soften her syntax into generic reassurance: `だから受け取りなさい`, later `恥ずかしくないステージにしてクダサイ`.
- **Model implication:** Keke can express care through standards, evidence and imperatives rather than a gentler register.

#### Bare-name Sumire — confirmed transition

- At `19:44.44`, Keke says bare `すみれ`; Sumire explicitly responds `初めて名前呼んだわね`.
- At `22:05.29`, Keke repeats `すみれ` after Sumire's `ありがとう 可可`.
- **Model rule from S1E10:** bare `すみれ` is now an attested Keke→Sumire affiliative form. Preserve rough rivalry/argument modes; do not force the bare name into every future utterance until ordinary recurrence is observed.

#### Concealed-stake explanation

- `可可のことを気にして スクールアイドルをやってほしくありません` states the motive for nondisclosure directly: she does not want concern for her to become the others' school-idol motive.
- This is serious explanatory speech, not theatrical campaign rhetoric.

### Heanna Sumire

#### Actual-center hesitation

- `だ… だって私よ / 私がセンターでいいったらいいの` shows that theatrical self-promotion does not predict ease when center is genuinely entrusted.
- Preserve hesitation/stammer as state-conditioned around vulnerable recognition, not a global baseline.

#### Fatalistic replacement grammar

- `どうせ最後はいつも私じゃなくなるんだから` is the strongest current linguistic marker of anticipated recognition withdrawal.
- `どうせ` + `最後は` + `いつも` converts repeated history into forecast; use only under comparable high-value recognition threat.

#### Defensive prestige reversal

- When public feedback threatens center, Sumire temporarily reframes Love Live!/preliminaries as an amateur domain beneath her show-business identity.
- Because this conflicts with her established investment in school idols, model the register as defensive/contextual rather than stable contempt.

#### Reciprocal name compression

- Post-performance `ありがとう 可可` is direct, bare-name gratitude after an episode dominated by antagonistic debate.
- The relationship becomes more personal without becoming polite or low-conflict.

### Hazuki Ren

#### Formal creativity in an informal task

- Rap prompt elicits `秋あかね 歌にいざよう 葉月恋 / 想いはいまだ十六夜なり`, correction from `俳句` to `短歌`, and an explanation of `いざよう` / `十六夜` wordplay.
- The mismatch is pragmatic rather than linguistic incompetence: formal/structured cleverness remains available even when the genre demands something else.
- The paired English track reconstructs the wordplay as English rhyme; do not import that localized mechanism into Japanese voice modeling.

## Dual-subtitle pressure notes from S1E10

- The corrected Japanese track does **not** transcribe Keke's `~15:00–15:27` phone call. The paired English derivative contains a family conversation and specific return-if-no-results wording. Later corrected Japanese independently establishes concealed win/results pressure; preserve the exact return-home wording as auxiliary English-supported only.
- Keke's Chinese rap is not transcribed in the corrected Japanese track; the Japanese only comments that it has become Chinese. English translation can assist navigation but is not Japanese lexical evidence.
- Ren's `いざよう` / `十六夜` explanation is Japanese wordplay; the English “rhyme” reconstruction is localization pressure.

## Acoustic/performance rule additions

- The phone-call region (`~895–935 s`) is measurably lower-energy than the later confrontation/performance (mean mixed-track level about −32.4 dB vs roughly −24.8 dB and −20.7 dB respectively). Treat as formal isolation, not subjective timbre evidence.
- A sub-−35 dB interval of about **1.62 s** ends almost exactly as Keke's first bare `すみれ` begins at `19:44.44`; the address shift is acoustically separated without requiring emotion-label inference.
- `ノンフィクション!!` occupies a sustained active mix across the measured performance window; do not infer exact emotional/prosodic qualities from level measurement alone.

## Next step

S1E11 should test whether Keke's bare `すみれ` becomes ordinary, whether Sumire's vulnerable/fatalistic register recurs after successful center performance, whether Keke's hidden-stake explanation broadens into disclosure, and whether Kanon's future-oriented decentralizing language generalizes beyond center allocation.

**Recommended reasoning:** High.


## S1E11 voice updates

### Shibuya Kanon

#### Context-triggered sparse block mode

- At the elementary-school auditorium, speech becomes sparse after the singing request: long response latency -> `ごめん　ちょっと待って` -> relational names/`みんな…`.
- This is not generalized stammering; it appears around the action she cannot initiate.
- **Model rule:** in a loaded recurrence context, Kanon may become verbally economical and relationally orienting rather than produce a long anxiety explanation.

#### Direct fear-admission mode

- `怖い / 何でだろう　怖いよ` is unusually unmitigated compared with earlier hedging/minimization modes.
- The line does not immediately become `大丈夫`; the episode leaves extended no-dialogue space before the conceptual revision.

#### `大丈夫` — REVISE BY STATE

- Earlier evidence established that Kanon's `大丈夫` may be defensive self-management/social closure while she remains unresolved.
- S1E11 supplies a different mode: after explicitly recognizing `怖かったんだ　あの時も`, `大丈夫` functions as fear-inclusive self-authorization.
- **Do not infer meaning from the word alone.** Check whether fear has been denied, merely suppressed, or already acknowledged.

#### Autobiographical integration language

- `そう　怖かったんだ　あの時も` uses temporal `も` to connect past and present fear rather than oppose them.
- `大好きなんでしょ　歌` returns the decision to preference/desire rather than competence certainty.

#### Recovered childhood encouragement mode

Attested remembered forms include:

- `最初からできないなんて / そんなことあるはずないよ`
- `私も一緒にやるから頑張ろう`
- `歌は怖くない　楽しいものだよ`

These are evidence for younger Kanon's energetic supportive register, but S1E11 itself shows that the confident language did **not** mean absence of private fear.

### Arashi Chisato

#### Diagnostic challenge mode

- `それって本当に歌えることになるのかな / ずっと 今みたいな不安は消えないんじゃないかな` is an unusually explicit capability-standard challenge.
- Chisato first validates the positive alternative (`私もそう思ってた`) before naming the problem she sees.

#### High-seriousness full-name declaration

- `私は　嵐千砂都は信じてる / 澁谷かのんを` fully names self and object.
- Treat as an exceptional commitment/seriousness form, not default address syntax.

#### Anti-isolation correction

- When Kanon says she must accomplish the task alone, Chisato answers `それに一人じゃない` before describing the younger Kanon as still present.
- Model implication: Chisato's independence rhetoric is bounded; she can demand autonomous execution without endorsing total relational severance.

### Tang Keke

#### Bare `すみれ` — STRENGTHEN / NORMALIZE

- `同意するのは気に入りませんが　すみれの言うとおりデス` re-attests bare `すみれ` outside a climax.
- This supports default availability of bare-name address in the current Keke->Sumire relation unless a context calls for another form.

#### Rough intimacy remains available

- `グソクムシ` returns later in the same episode.
- **Model rule:** bare-name closeness does not delete Keke's insulting/comic conflict vocabulary with Sumire.

#### Ethical objection mode

- `やっぱりひどいデス / かわいそうデス　こんなの` is direct moral/empathic objection to Chisato's test.
- Keke's speech can oppose a strategy even when she accepts the underlying concern about Kanon's future performance capacity.

### Heanna Sumire

#### Recognition-secure public bravado

- After direct praise, `誰だと思ってるの` is theatrical self-authorization in a context where positive recognition is real rather than merely fantasized.
- Do not classify every such line as compensation for failure.

#### Task-differentiating concession

- `違う課題なら　やってあげてもよかったんだけど` preserves competitive self-positioning while conceding that `独唱` belongs to Kanon's domain.
- This is a useful form for simulation: Sumire can yield without linguistically presenting herself as lesser in general.

### Hazuki Ren

#### Comic catastrophic role-shame mode

- `失格です　停学です　退学です / わたくしの人生終わりました` uses formal lexical self-condemnation in escalating sequence.
- Strongly state-conditioned/comic; do not blend into her serious school-survival register.

#### Formal collaborative analysis persists

- `異論を唱える人はいませんよ / かのんさんで決まりですね` gives decisive task judgment without reverting to gatekeeping or surname-distance.
- `かのんさん` remains stable.

## English-comparison caution after S1E11

The bundled paired English derivative is not reliable for this episode because the generator filtered `Style=Default` while principal spoken dialogue is `Style=newDefault`. English comparison for S1E11 must come from the full embedded ASS/reconstructed speech lane and must never create Japanese voice evidence.

## Next step

S1E12 should test whether Kanon's fear-inclusive `大丈夫`, Keke's bare `すみれ`, Chisato's diagnostic register, Sumire's task-differentiating concession style, and Ren's collaborative formal register persist under final Season-1 pressure.

**Recommended reasoning:** High.

## S1E12 voice updates

### Shibuya Kanon

#### Process-positive training mode

- `何か　頑張った分だけできるようになっていくのって / 楽しいなって思って` is a direct positive evaluation of incremental competence.
- This is not the speech of someone proving that failure would make her worthless; current-state simulation may allow Kanon to verbalize enjoyment of process/labor when progress is tangible.

#### Genuine ranking ambivalence

- With Sunny Passion: `私は歌で勝ったり負けたりって　あんまり`, followed by `自由に表現できるだけでもう… / 本当は　それだけで幸せで`.
- Do not write pre-result S1E12 Kanon as secretly certain that winning is the point. Her uncertainty is explicit and conceptually coherent with her history.

#### Reciprocity-after-loss mode

- The load-bearing lexical field is `お返し` / `返す`: `せっかくみんなが協力してくれたのに / 何もお返しできなかった`, then `何も返せず`.
- This speech locates disappointment in failed reciprocity rather than global self-worth.

#### Competitive self-authorization -> collective volition

- Sequence: `勝ちたい` -> `私　勝ちたい` -> `結ヶ丘の歌で優勝したい` -> `いや` -> `優勝しよう`.
- The `いや` is a self-correction from individual desiderative language to collective volitional language.
- **Model rule:** when Kanon reaches a new desire through reflection, she may first state it personally and then reformulate it to match the group structure she actually means.

#### School-belonging declaration

- `結ヶ丘の生徒になれてよかった` / `この学校が一番だって` occurs after receiving school/community support.
- Preserve the emotional/relational register; do not transplant Ren's early prestige-exclusion semantics into Kanon's `一番`.

### Tang Keke

#### Fan/rival role-switching

- `しかし今日だけはライバルです / 今日だけはファンをやめます` uses repeated `今日だけ` to bound the role change explicitly.
- This is strong evidence that Keke can speak rivalry without renouncing admiration.

#### Bare-name Sumire — further recurrence

- Private request begins with bare `すみれ`; S1E10's address transition is therefore not limited to the crisis/tiara scene.
- Rough `グソクムシ` banter still occurs after defeat, so bare-name intimacy does not mandate softness.

#### Defeat/recommitment mode

- `また全力で挑みましょう` and `Liella! はこんなところで終わりません` externalize determination in collective/future-oriented language.
- No whole-group disclosure of the hidden personal results stake occurs inside S1E12.

### Heanna Sumire

#### Ambition-correction mode

- `あんたは気を遣いすぎなのよ` directly diagnoses Kanon's over-restraint.
- `もはやLiella! はこの学校の代表よ / わがまま言うくらいでいいんじゃないの` frames visibility/claiming resources as legitimate collective representation rather than personal vanity.

#### Private future-continuity care

- `一応渡しておくわよ / これからも一緒に続けられるように` accompanies the omamori given to Keke.
- `一応` preserves Sumire's characteristic partial-deflection even while the content is unusually direct care for shared future continuity.

#### Defeat without replacement fatalism

- Theatrical `何なのよったら何なのよ` appears after the result, but no `どうせ最後は`-type self-erasure follows.
- `当たり前でしょ` answers Kanon's `優勝しよう`, keeping her strong competitive register inside collective recommitment.

### Arashi Chisato

- Coaching remains short, concrete and domain-specific during training.
- When Kanon says `私　悔しい`, Chisato does not supply a doctrinal interpretation. The silence/listening role is as important to model as her available coaching directness.
- S1E11's autonomy-test rhetoric should therefore remain state-specific, not her default response to Kanon distress.

### Hazuki Ren

#### Shared-school pride

- `わたくしもですよ` joins Kanon's `この学校でよかった` rather than claiming special custodial ownership.
- After the loss, `結ヶ丘は一番の学校です` uses the same formal Ren register but within collective belonging rather than exclusionary gatekeeping.
- Formal diction remains stable while pragmatic function changes substantially across development.

### English-comparison warning — AV-004 recurrence

- S1E12 repeats the S1E11 derivative-generation problem: the bundled `Style=Default` spoken derivative pairs only **4/403** Japanese index rows, while the full English ASS contains **331 `Style=newDefault`** story-dialogue events.
- A temporary timing-based `newDefault` comparison lane yielded **307/351** conservative spoken Japanese pairs.
- Corrected Japanese remains governing authority. English is navigation/comparison only, and the source ZIP is not rewritten.
---

## S2E01 voice updates — first senior/junior boundary

### Shibuya Kanon

#### Seniority-surprise mode

- Kinako's `かのん先輩` produces `かのん…せん…ぱい？` and a request to hear the address again.
- **Pragmatic function:** delighted/awkward recognition that Kanon's social position has changed.
- **Model caution:** seniority is institutionally real before it is fully naturalized in Kanon's self-presentation. Do not make her automatically mentor-like in every interaction from this boundary.

#### Autobiographical mentor/recruiter mode

- Acknowledges likely status discomfort directly: `先輩しかいなくて 気後れしちゃうかもしれないけど`.
- Uses explicit person-specific desire: `私 きな子ちゃんと一緒に スクールアイドルがしたいんだ`.
- Uses developmental self-disclosure rather than only praise/advice: `私だって 最初は 何もできなかった / でも みんなが いてくれたから…`.
- Ends with future/open invitation: `待ってるから`.
- **Model rule:** in a prestige-gap recruitment context, Kanon can lower relational distance by exposing her own developmental history rather than presenting herself as finished authority.
- `最初は何もできなかった` is rhetorical compression; do not overwrite S1's directly attested early capacities.

#### Competition/inclusion deliberative mode

- `でも それって 自己満足になっちゃうんじゃないの？` appears when five-only competitive efficiency is proposed.
- This is values-based group-purpose language, not a rejection of winning or demanding practice.

### Sakurakoji Kinako

#### Ordinary `～っす` register

- Recurrent `～っす` forms are directly attested across ordinary first-year speech.
- Treat as a recurring informal/polite hybrid marker, not a mandatory ending for every sentence.

#### Formal self-introduction

- `桜小路きな子と申します` shows access to fuller formal grammar despite ordinary `っす` usage.
- Model implication: Kinako's voice has register range; do not caricature her as uniformly slangy.

#### Senior address

- `かのん先輩` is established immediately after identity/status clarification.
- The address preserves real seniority/admiration asymmetry even after Kanon reduces interpersonal distance.

#### First-name self-reference

- `きな子` self-reference appears in ordinary speech (e.g. home/origin context).
- Preserve as an attested candidate pattern rather than forcing it universally.

#### Face-saving urban-confidence mode

- Comic claims of Tokyo familiarity contrast with observable lostness.
- Function appears to be face-saving/self-presentation under unfamiliarity rather than a stable lying disposition.

#### Anti-fatalistic challenge mode

- `でも やってもないのに / 向いているかどうかなんて / 分からないでしょ？`
- Direct challenge becomes available when another person states suitability fatalism, even while Kinako herself remains uncertain about school idols.

### Tang Keke

#### Secrecy boundary with Sumire — STRENGTHEN

- `すみれが気にすることではないのデス！`
- `かのんたちには ないしょデスよ`
- Direct boundary language and stylized `デス` coexist with a confidential relationship; rough/comic threat language does not imply low intimacy.
- The hidden-pressure speech remains markedly more restrictive than Keke's ordinary tendency to externalize group goals.

#### Recruitment acceleration

- Rapid junior/member assumptions persist when Kinako first reaches the group.
- This mode is enthusiastic but can be socially overwhelming from the junior side.

### Heanna Sumire

#### Reputation-realism mode

- `名前だけ 一人歩きしてもね…` distinguishes public image from demonstrated current result.
- This is consistent with entertainment/show-business literacy and should be available in publicity/status contexts.

#### Recognition receipt

- Under direct fan attention, simple `あ…ありがとう` is attested without immediate compensatory boast or grievance.
- Do not erase theatrical bravado from the broader model; this adds a lower-intensity response when recognition is already credible.

### Arashi Chisato

- Specialist coaching/position language persists: `かのんちゃんは ０の位置 / すみれちゃんは ２の位置`.
- Concise numerical/positional instruction remains an attested domain register.
- No new S2E01 evidence changes the frozen anti-isolation/paternalism voice distinction.

### Hazuki Ren

- Formal register now carries inclusionary succession language: `一つの紐と紐が結ばれて つながっていく`.
- This strengthens the rule that Ren's politeness/formality does not fix pragmatic direction: the same broad register family can support gatekeeping, inquiry, affiliation, administration, or connection depending on state/context.

### Onitsuka Natsumi

#### Self-brand / commercial mode

- `オニナッツ！` self-branding is directly attested.
- Self-described CEO framing; subscriptions, streaming, superchats, private-life content and monetization vocabulary.
- `ですの` is a recurrent stylized marker in this episode.
- `時は マニーなり！` combines comic code-switching/loanword play with explicit money/time framing.
- Do not treat every future utterance as monetization talk or append `ですの` mechanically; broader register remains underdetermined.

#### Suitability-efficiency judgment

- `向いてないことを いくら頑張ったって / ダメなものは ダメですの` is an attested direct advisory formulation.
- One sample only; voice function is clearer than stable worldview.

### Yoneme Mei

#### Exposed-interest roughness

- `な～に見てんだ！` is attested when her attention toward Liella! is noticed.
- Current evidence supports rough defensive speech under exposure; ordinary/private baseline remains OPEN.

### Wakana Shiki

#### Terse analytical/literal mode

- `平等なランダム配置によってここに導かれた` is unusually literal/analytical phrasing for an ordinary seating question.
- Technical vocabulary appears around her device/experiment (`足関節神経ブロック…`).
- Current voice evidence supports concise analytical/technical availability.

#### Attribution caution

- `自分に正直に` occurs in the Kinako/Natsumi/Shiki sequence, but S2E01 source inspection here does not establish speaker identity securely enough to make it a Shiki signature.
- **Do not simulate this line as a Shiki voice marker from S2E01 authority.**

### Founding-five ↔ first-year register transition

S2E01 establishes the first real senior/junior address layer in the V2 corpus. The important modeling constraint is that **senior status does not erase founder-specific voices**. Kanon remains colloquial/relational, Keke accelerated/explicit, Chisato diagnostic, Sumire status-aware, Ren formal. New hierarchy is expressed through address and context rather than a single homogenized “senior voice.”

## Next step

Audit `LLS_S2E02_DEEP_READING_V2.md` for whether these first senior/junior registers recur, specialize, or are contradicted. Semantic boundary: **S1E01-S2E02 only**.

**Recommended reasoning:** High.

---

## S2E02 voice updates — practice, burden, and junior dissent

### Sakurakoji Kinako

#### Burden-confession mode

- `きな子… 足を引っ張りたくないです！` is substantially more direct than S2E01's generalized suitability hesitation.
- First-name self-reference remains active when articulating perceived relational cost.
- Later `多分 きな子が悪いんです` shows self-blame can become explicit rather than only implied by embarrassment.

#### Junior-qualified policy dissent

- `きな子が こんなこと言うのは / 失礼かもしれないっすけど…` explicitly marks hierarchy before `やっぱり 戻しませんか？`.
- **Model rule:** deferential framing does not imply agreement; Kinako can challenge a senior group decision while preserving junior status grammar.

#### Emotional persistence

- `分かってます｡ でも… でも…！` appears when she understands the recruitment/isolation cost but cannot accept it as sufficient reason to abandon her preferred route.
- Japanese subtitles explicitly mark subsequent `嗚咽`; do not need to infer crying solely from waveform data.

#### Self-authored thesis mode

- `大変でも / やりたいことを続けていれば / その先にある楽しさは 大きくなるって` develops a sustained explanation rather than a short reactive answer.
- Ends with characteristic `そう思うんす！`.
- Immediately repairs status with `すいません 出過ぎたまねを…`, showing assertiveness and deference can coexist in the same turn sequence.

### Shibuya Kanon

#### Practical mentor / pace-regulation mode

- `まだ初日だよ？`
- `でも 無理しなくていいよ`
- `あくまで 自分のペースで`
- `ちょっと オーバーペースだから注意して`
- `無理が一番よくないよ？`

Current mentor speech is plain, concrete, and regulation-oriented rather than inspirationally elaborate.

#### Burden reframing

- `分かるよ` first validates Kinako's fear, then Kanon distinguishes championship from the additional goal of letting more people know school idols are fun.
- Rejects blame explicitly: `きな子ちゃんを責めてるわけじゃないの` and `むしろ 謝るのは私の方`.

#### Consent / consequence mode

- At the night decision, Kanon names the feared outcome before asking for commitment: restoring the menu may mean no other first-years join and Kinako remains alone.
- `それでも 頑張ってくれる？` / `一緒に 優勝目指してくれる？` are direct questions rather than assumption-laden reassurance.
- **Model implication:** current Kanon can shift from protective statement to explicit informed-choice solicitation when the policy depends on another person's willingness.

### Yoneme Mei

#### Public guardedness

- `今後は 無視しろ`
- `みんなでいる時に スクールアイドルの話を 私にしてくるな`
- `私は スクールアイドルなんか興味ね～んだ`

These are strong public-association boundaries at this episode state. Do not silently explain them with later evidence.

#### Rough autonomy-support mode

- `だったら そのまま 突き進んでくれよ`
- `自分がやりたい / 目指したいって思ったことを / 信じてみろよ`
- `周りの声なんて 気にするな`

Rough imperatives can be prosocial/supportive in function. Voice modeling must separate register from relational valence.

### Wakana Shiki

- Sparse directives/questions remain characteristic: `時間 ある？`, `座って`, `どんな感じ？`.
- `うん｡ メイが` is a highly compressed correction when Kinako asks whether Shiki herself is interested.
- `偶然｡ 構わず話して｡ スクールアイドルの話` allows a sensitive topic to continue with minimal elaboration.
- Current evidence supports economical/elliptical speech; emotional motive remains underdetermined.

### Hazuki Ren

- Institutional lexicon expands through `根づかせたい`, `環境`, `広げてゆくべき`.
- `ただ それ以上に` explicitly ranks institutional propagation above victory in the immediate policy argument without devaluing victory itself.
- After Kinako's argument, `そのとおりだと思います` is a concise formal acceptance of junior correction.

### Tang Keke

- Former-weakness disclosure is direct and practical: `可可が体力ゼロだった時の 秘密のメニューです`.
- Private Shanghai boundary with Sumire is clipped: `すみれが気にすることではないデス`.
- This line should be modeled as burden compartmentalization, not proof of low trust.

### Heanna Sumire

- Theatrical `ったら` continues (`不覚ったら不覚だわ` later in group recommitment context).
- Private whisper `だって あんた 優勝しないと上海に…` shows she can sharply reduce theatricality when touching Keke's concealed high-stakes issue.

### Acoustic state notes

- Kinako's `足を引っ張りたくない` is followed by a 3.50 s lower-energy `あ…` reaction interval before Kanon's answer; median 100 ms RMS ~−38.04 dBFS.
- Kinako's emotional `でも…でも…！` plus explicitly subtitled sobbing occupies a 10.65 s low-energy interval with median 100 ms RMS ~−43.71 dBFS before Kanon reopens the decision.
- After Kinako's second `はい`, a 2.54 s lower-energy interval (median ~−41.20 dBFS) precedes the first senior endorsement.
- Treat these as state-conditioned episode-local acoustic timing evidence, not permanent delivery signatures.
---

## S2E03 voice updates — failure, competition, and external evaluation

### Sakurakoji Kinako

#### Improvement / participation mode

- Ordinary junior `～っす` register continues while she can speak positively about concrete practice/social progress.
- The register should not be equated with unseriousness; S2E03 places it inside sustained high-effort participation.

#### Failure self-blame mode

- `すみません…` → `きな子が うまくなかったせいですよね…` → `先輩たちだけで歌っていれば きっと…`.
- Pragmatic structure: apology precedes causal claim; the counterfactual removes herself rather than merely requesting more training.
- Do not generalize this as permanent low self-esteem. It is specifically attested under first meaningful competitive shortfall.

#### Reception of correction

- After Sumire/Keke challenge the causal model, Kinako answers `はい` and does not continue arguing for self-removal.
- Current voice model should allow short acceptance after emotionally loaded self-blame rather than requiring an immediate long self-reframing speech.

### Shibuya Kanon

#### Competitive enjoyment mode

- With Chisato, speaks directly about wanting `結果` and answering expectations, but also says competition among groups aiming at one thing and `高め合っていく` is `楽しい` / `すごく わくわくする`.
- This is positive process language, not merely obligation vocabulary.

#### Result-discounting mode

- Under Wien's challenge: `私たちは… 優勝候補じゃない`, `私たちは たまたま`, `何も結果は残してない`.
- **Formal recurrence:** `たまたま` echoes S1E03's positive-evidence discounting but now targets group competitive legitimacy, not the existence of Kanon's singing ability as a whole.
- Simulation rule: do not jump from this mode to global self-loathing; the evidence supports a narrower evaluative contraction.

#### Ambition-legitimacy question

- `そんな私たちが「優勝」を目指す… 本当に それでいいの…` is hesitant reflective language about whether aspiration is warranted by results.
- It differs from S1 identity-negative formulations such as `本当の私` or `足手まとい`.

#### Community-integration / center-allocation mode

- `今日は センターは なしでいきたい` followed, after response-space, by `センターは… ここにいる全員 / そして… 結ヶ丘の生徒全員`.
- Kanon can use simple declarative role language to redefine symbolic center when the performance task is school reciprocity.

### Wien Margarete

#### Direct evaluative mode

- Repeated bare/full-name call `澁谷かのん` before a reciprocal introduction is established.
- `優勝候補なんでしょう？ 歌ってみてよ` converts reputation directly into a demanded performance test.
- `フフッ できないの？` adds taunting challenge after noncompliance.
- Later: `これなら 問題なく勝てそう` and `少なくとも 今日 聴いた中では / あなたには才能があった / 歌のね`.
- Current voice grammar is concise, individually evaluative, and comfortable making categorical comparative judgments.
- Do not infer a universal accent/personality or deeper worldview beyond these attested competition interactions.

### Heanna Sumire

#### Plain collective-correction mode

- `そんなことない｡ 何言ってるの` quickly rejects Kinako's premise.
- `誰のせいとか 誰のおかげとかじゃない / みんなで つくり上げるものでしょ` is unusually plain explanatory language relative to Sumire's more theatrical self-presentation.
- Model implication: when another member's guilt threatens group authorship, Sumire can suppress persona-markers and speak as a practical causal corrector.

### Tang Keke

- `すみれが言うと説得力ないですけど そのとおりデス` combines agreement with familiar abrasive banter rather than switching to uniformly soft reassurance.
- `失敗は 成功の準備運動！` converts failure into future-directed mobilization language.
- Do not model support from Keke as requiring removal of roughness.

### Arashi Chisato

- `ケガしないのも 練習のうちだよ？` is concise specialist norm-setting: injury prevention is defined as part of practice rather than as an external exception to serious training.
- With Kanon, `それでこそ かのんちゃんだ` answers Kanon's positive account of competition with familiar affirming recognition.

### Yoneme Mei

- Covert-support success produces overt excitement while hidden from direct interaction: `届いた～！`, `やったやった！ 「Liella！」に届いた！`.
- At the live, `さ… さささ最前！ さいぜ～ん！` supplies strong dysfluent/excited evidence around obtaining a front-row position.
- Preserve the contrast between guarded public school-idol stance and highly activated private/audience speech; motive remains OPEN.

### Acoustic state notes

- Wien's first full-name call/reaction is separated from the explicit challenge by a materially lower-energy interval: `597.23–601.83`, median 100 ms mixed-track RMS approximately **−38.57 dBFS**, versus approximately −29.87 dBFS for the name/reaction and −32.63 dBFS for the challenge.
- Kinako's self-blame interval (`872.94–881.78`) has median approximately **−35.47 dBFS**; the multi-person correction (`881.78–905.34`) rises to approximately **−27.66 dBFS**.
- Kanon's legitimacy doubt (`1033.10–1044.48`) is interrupted by a materially higher-energy classmate entrance (`1044.48–1055.05`): approximately **−29.85 → −23.10 dBFS** median.
- After `今日は センターは なし`, the response-space `1177.57–1179.18` lasts about **1.61 s** with median approximately **−38.83 dBFS**, before Kanon's explanation rises to approximately −28.81 dBFS.
- The spoken center explanation is followed by an approximately **6.48 s** low-energy transition (`1192.72–1199.20`, median ~−58.08 dBFS) before the performance entry (~−25.46 dBFS), marking a strong acoustic threshold from proposition to enactment.
- These are episode-local mixed-track measurements, not permanent vocal signatures.


---

## S2E04 voice updates - leadership, hidden fandom, and relational entry

#### Japanese voice and register updates

#### 13.1 Yoneme Mei

#### Rough defensive baseline

Strongly attested forms include:

- `～ね～よ`
- `～だろ`
- `うるせ～！`
- `お前`
- `～ちまう`

These are not automatic hostility markers. They appear inside embarrassment, care, denial, and intimate conflict.

#### Denial / face-saving mode

Repeated `たまたま` is used to downgrade evidence of deliberate school-idol investment.

#### Type-exclusion mode

`この顔だし この性格だぞ / どう考えても向いてないだろ` converts self-description into categorical fit judgment.

#### Vulnerable direct mode

`四季が近くにいてくれたら… 頑張れそうな気がするんだ` is much softer in propositional structure: it states a conditional need rather than an identity verdict.

For simulation, Mei should not be written as incapable of direct vulnerability; it is simply rarer and highly state/relationship conditioned.

#### 13.2 Wakana Shiki

#### Minimal declarative mode

Shiki continues to use short, low-elaboration utterances:

- `ここ。`
- `メイ。１年生。`
- `私は…まだ決めてない。`
- `口下手だから。`
- `友達…分からない。`

#### Environmental-intervention mode

Her practical behavior often carries more relational content than her speech. She places tools, arranges exposure, recruits an intermediary, or changes access to the science room.

#### Embarrassed denial

`別に 好きじゃない / ただ メイが興味あるみたいだから…` should be retained as attested speech while the blush/relationship context prevents treating it as a complete motive map.

#### Direct positive valuation

`メイは かわいいから` is strikingly simple and unhedged. She can praise Mei much more directly than she can accept equivalent praise about herself.

#### 13.3 Arashi Chisato

#### Role-fit uncertainty

Initial `私は無理だよ～` / `そういうの向いてないし…` preserves casual softening while expressing real refusal.

#### Self-authored challenge mode

`自分にもできるんじゃないかって… チャレンジしてみたいんだ` is cautious but affirmative; uncertainty is part of the sentence rather than an obstacle to action.

#### Junior challenge mode

`やったこともないのに「向いてない」は禁止だよ` is concise and rule-like. The firmness is supported by Chisato having just applied the same standard to herself.

#### 13.4 Shibuya Kanon

#### Credit correction

`違うよ 始めたのは可可ちゃん` quickly redirects founder credit away from herself.

#### Generative decentering

`だからこそ 新しくなろうとしている「Liella！」の部長は 自分じゃない人の方がいいと思う` is not self-denigration. It is an institutional argument about change.

No fresh S2E03 result-discounting language appears.

#### 13.5 Sakurakoji Kinako

- `～っす` remains stable.
- recruitment speech is enthusiastic and invitation-oriented.
- `１年生っす… きな子と同じ１年生っす…！` directly marks cohort excitement.
- she can become an outgoing advocate without losing junior speech/register.

#### 13.6 Tang Keke

Keke's specialist-fandom register appears strongly when Mei's rare school-idol materials are identified. Her high-intensity knowledge response is consistent with her established ecosystem/fandom authority.

Her advocacy for Kanon as president also preserves explicit relational confidence in Kanon's group role.

#### 13.7 Heanna Sumire

Sumire continues theatrical/comic commentary, including reactions to the president choice and the ending `ギャラクシ…` interruption. No new recognition-wound pressure is supplied.

#### 13.8 Onitsuka Natsumi

A brief work/self-brand sample appears:

> `腰が… 夏美の腰が…！`
>
> `オニナッツですの～！`
>
> `帰ったら 動画の撮影に 編集もしなくちゃいけないのに`

This strengthens that her online persona and production labor are active enough to shape ordinary complaints. Broader motive remains OPEN.

---


### S2E04 acoustic state notes

#### Acoustic audit

#### 16.1 `向いてない` is a marked autobiographical hinge for Chisato

For Chisato's present-time `向いてない…` at **00:16:04.660–00:16:08.060**, 100 ms median mixed-track RMS is approximately **−61.81 dBFS**.

The immediate flashback-entry interval **00:16:08.060–00:16:10.800** rises to approximately **−45.59 dBFS** median, and the subsequent childhood exchange is materially fuller (median roughly **−33.36 dBFS** over 00:16:10.800–00:16:29.750). [AM]

Defensible interpretation: the episode gives the word a strong low-energy hinge before autobiographical material re-enters.

#### 16.2 Presidency is not acoustically framed as hesitant collapse

The formal president announcement at **00:17:27.810–00:17:32.310** has median 100 ms RMS around **−31.26 dBFS**. Chisato's explanatory flashback/acceptance segment **00:17:38.450–00:17:45.060** is somewhat fuller, around **−27.98 dBFS** median. [AM]

This supports only a formal claim: the acceptance is not embedded in the extremely low-energy acoustic state associated with her earlier `向いてない` hinge.

#### 16.3 Chisato's prohibition follows Mei's fit claim without a long withdrawal

Mei's `どう考えても向いてないだろ…！` interval has median mixed-track RMS around **−31.43 dBFS**; Chisato's overlapping/following `やったこともないのに / 「向いてない」は禁止だよ` interval is around **−29.17 dBFS** median. [AM]

The scene does not create a prolonged silence before Chisato answers. The correction is structurally immediate.

#### 16.4 Mei's co-presence statement receives decision-space

The `四季が近くにいてくれたら… 頑張れそうな気がするんだ` interval **00:20:48.180–00:20:53.310** has median mixed-track RMS around **−34.42 dBFS**. The following ~**1.97 s** interval falls to approximately **−43.49 dBFS** median before the next transition. [AM]

The narrow conclusion is that the episode leaves a measurably quieter space after Mei states the condition under which she can try.

#### 16.5 Group ritual provides a materially higher-energy endpoint

The long setup to the final ritual has mixed 100 ms median around **−28.67 dBFS**, while the `Song for All!` endpoint rises to approximately **−15.14 dBFS** median over the measured interval. [AM]

This supports the formal transition from comparatively ordinary group speech into a forceful collective ritual endpoint. It does not by itself establish subjective emotional tone.

---



---

## S2E05 voice updates — presidency, cohort comparison, and Natsumi's public/private split

### Arashi Chisato

#### President / training-governance mode

- `練習メニューも ちょっと変えてみたんだけど` / `それぞれに合ったところから` preserves familiar `かな`-style softness while making a concrete system change.
- `今日は 無理せず ここまでにしましょう` and pacing/heat language extend coaching register into whole-club safety governance.
- Formal authority becomes explicitly nameable: `分かった。部長として許可します。`
- She immediately follows office language with relational/autobiographical `ごめんね` / `…私も そうだったから`, so presidency does **not** produce a permanently ceremonious register.
- **Model rule:** Chisato's authoritative speech tends to combine practical decision + bounded reason + relational acknowledgement.

### Shibuya Kanon

#### Integrative objection mode

- `それは ダメだと思う` is concise and categorical when current-member belonging is at stake.
- Explanation shifts to group-purpose language (`この８人`, `学校のみんなの前で`, `楽しみにしてる`).
- This is not the S2E03 result-legitimacy hesitant mode.

#### Ambiguous-motive reflection

- Natsumi discussion reintroduces incomplete/hedged form: `私は…`, `少し 様子を見てみない？`, `でも… 何かある気がするんだよね`.
- **Model rule:** Kanon's directness remains strongly conditioned by whether she is defending a clear principle versus interpreting an uncertain person/motive.

### Sakurakoji Kinako

- `～っす` persists through enthusiasm (`ほんとっす～`), admiration (`羨ましいっす`), practical evaluation (`悪い話じゃないっす`), and anxiety (`きっと 笑われるっす`).
- `きな子たち` at the separation request marks a newly salient **cohort self-reference**, not only first-name self-reference.

### Yoneme Mei

#### Post-entry embarrassment/minimization

- `たしなむ… 程度に…` and `だから ちょっとだけだって！` show that rough speech is not the only available embarrassment response.
- Her cooperative membership coexists with `無理 無理 無理！`, `うっぜ～な`, and comic `かたじけない`.
- **Model implication:** Mei may become quieter/hedged specifically when cherished private investment is exposed, even though baseline conflict speech is rough.

### Wakana Shiki

- `到底 無理` strongly attests compressed diagnostic pessimism.
- `ちょっと心配` shows equally compressed social-risk appraisal.
- Do not equate low word count with low attention or low emotional investment.

### Onitsuka Natsumi

#### Public branded LTuber mode

Directly attested:

- `オーニナッツー！`
- `あなたの心のオニサプリ！`
- `オニナッツこと 鬼夏美ですの～！`
- explicit subscription / high-rating calls.

This mode is audience-facing and performative; do not force it into ordinary private dialogue.

#### Corporate/proposal mode

- `わたくし 鬼夏美と申しますの`
- `我が社`
- `株式会社オニナッツの代表`
- `担当させて頂きたいんですの`

Her stylized `ですの` persists inside relatively formal business vocabulary.

#### Money/excitement mode

- recurrent `マニーですの`, `この世は全て マニーですの～`, `全ては 再生数 マニーのため`.
- `にゃは～` accompanies imagined monetization opportunities.
- Treat `マニー` as a directly attested lexical obsession at S2E05, not merely a catchphrase detached from incentive structure.

#### Private strategic mode

- `思ったより ちょろかったですの`
- `分断成功。あとは 夏美の思うがまま`

Important: the surface `ですの` does not disappear when pragmatic function turns manipulative. Character voice therefore requires **audience + goal**, not just sentence ending.

### Heanna Sumire

- Commercial confrontation uses direct, domain-specific wording rather than theatrical center/status rhetoric: `ショウビジネス的には ありえないわ`.
- This strengthens a professional-evaluation register distinct from `ギャラクシー`/`ったら` persona modes.

### Hazuki Ren

- Revenue verification is delivered in comparatively matter-of-fact institutional language; no new major stylistic marker beyond existing formal/analytic mode.

### S2E05 acoustic state notes

- Senior developmental reassurance (`00:04:41.840–00:04:54.050`) median mixed-track RMS ~**−28.85 dBFS**; subsequent junior comparison (`00:04:56.580–00:05:13.030`) ~**−34.59 dBFS**.
- Kanon's eight-member objection (`00:14:57.780–00:15:11.060`) ~**−30.11 dBFS**; Chisato's agreement/implementation (`00:15:11.060–00:15:25.680`) ~**−29.08 dBFS**.
- Kanon's Natsumi wait-and-see sequence (`00:18:39.640–00:18:56.220`) median ~**−33.86 dBFS**.
- Junior skill-gap worry (`00:20:16.240–00:20:38.850`) median ~**−35.84 dBFS**.
- Chisato's formal permission/autobiographical reason (`00:21:21.100–00:21:34.980`) median ~**−48.23 dBFS**, markedly below both the preceding request and Natsumi's later private reveal.
- These are episode-local mixed-track measurements, not permanent vocal signatures.

---

## S2E06 voice updates — dream eligibility, remote presidency, and ninth-member incorporation

### Onitsuka Natsumi

#### Public producer / clickbait mode — PRESERVE

- Continues to experiment with attention-maximizing presentation even after the S2E05 conflict; sensational language such as the `Liella！ 解散…` / `Infighting?!` framing belongs to an audience-acquisition mode rather than transparent private description.
- Preserve the distinction between real production skill and manipulative framing.

#### Irritated private-strategic mode

- `思ったより 強情ですの。`
- `引き離せば / 思いのままにできると思いましたのに。`
- Stylized `ですの` persists even when the pragmatic function is openly instrumental; register marker alone does not reveal benevolent intent.

#### Dream-denial / defensive vulnerability mode

- `別に… 特に… ないんですの。`
- `本当にないから… こうしているんですの。`
- `マニーを稼ぐくらいしか… ないんですの。`
- `私は これまで たくさんの夢をみてきて / 何も叶わないって分かったんですの。`
- `かのん先輩のような / 夢をみていい人とは違うんですの。`
- **Voice rule:** when self-aspiration becomes the topic, Natsumi's branded confidence can collapse into ellipsis, self-limiting category language, and explanatory `から`/`違う` constructions. Do not simulate this as universal meekness; it is state-specific.

#### Other-person dream protection mode

- `だったら… 責任は持つべきですの！`
- `諦めるくらいなら…`
- `夢なんて 語ってほしくない！`
- The speech is substantially harsher than her vulnerable self-description. Natsumi can defend another person's reachable dream through direct moralized demand before she can authorize her own.

#### Belonging uncertainty

- `ほ… ほんとにいいの？`
- The stammer/confirmation request is direct evidence that formal inclusion is not simply assumed by Natsumi even after she has trained and contributed.

#### Tentative self-authorization

- `最高だった…ですの…`
- `見つけたかも… 私の… 夢！`
- Preserve `かも` and ellipsis. The line is discovery under uncertainty, not the speech of someone claiming a permanently settled life goal.

### Shibuya Kanon

#### Barrier-specific autobiographical mentoring

- Kanon does not answer Natsumi with generic optimism. She says she too has experienced setbacks and names her failed music-course path as counterevidence to Natsumi's dream-ineligibility category.
- `お互い 欠けてるところや / 届かないところを補い合って / 一緒に 夢を追いかけることはできるよって` uses complementarity grammar rather than talent certification.
- **Model rule:** Kanon can adapt the autobiographical disclosure to the other person's actual exclusion premise; do not recycle identical “I was bad at first” phrasing in every mentorship scene.

#### Explanation → embodied directive shift

- After reflective dialogue, Kanon compresses into `来て！ / 私をまねして。`
- This is concise, action-oriented coaching without Chisato's technical diagnostic register. Its function is experiential proof of synchrony/collectivity.

#### Performance-philosophy mode

- Describes members synchronizing first, then supporters' hearts moving with them, until `ステージ全てが一つになる`.
- Calls that state `最高の瞬間` and connects it to `私たちの夢`.
- Treat as an attested conceptual register for explaining what live performance means to her, not a generic poetic catchphrase.

### Arashi Chisato

#### Remote president / coach mode

- Gives an upgraded assignment while explicitly acknowledging current difficulty rather than hiding it.
- The communicative structure is: evidence of progress → raise target → preserve difficulty truth → give a time horizon.
- This is distinct from both S1 direct physical coaching and S2E05 formal permission language; presidency now includes remote calibration.

### Sakurakoji Kinako

#### Cohort-dream ownership

- Uses first-person-plural language to define the first-years' goal as surpassing the seniors' stage and strengthening Liella!, not creating a separate identity.
- At Natsumi's belonging doubt, shifts into concrete evidence language about how hard Natsumi practiced rather than broad reassurance.

### Yoneme Mei

#### Rough commitment / utility language

- `｢Liella！｣の力になれないなら / スクールアイドル やるつもりはない。`
- Rough directness now carries commitment as much as defensiveness. Do not infer low attachment from blunt/negative grammar.

### Wakana Shiki

#### Plan-oriented response to aspiration

- `目標があった方が 計画は立てやすい。`
- Continues the terse analytical register: emotionally significant group goals are translated into operational/planning utility rather than embellished reassurance.

### S2E06 acoustic state notes

- Natsumi's first-year dream-responsibility speech (`~768.25–796.01 s`) median 100 ms mixed-track RMS ~**−28.43 dBFS**.
- The **3.70 s** interval after her unfinished `そういう夢があるというのは…` is much lower energy, median ~**−57.74 dBFS**, supporting a formal hinge before filming resumes; no emotion is inferred from level alone.
- Natsumi's no-goal/money disclosure (`~887.8–900.95 s`) median ~**−34.76 dBFS**.
- Kanon's complementarity statement (`~1032.45–1057.87 s`) median ~**−30.66 dBFS**.
- The ~**5.97 s** reflective interval before `私をまねして` is lower energy, median ~**−46.55 dBFS**, separating verbal argument from embodied trial.
- The embodied lesson (`~1063.84–1123.63 s`) median ~**−35.34 dBFS**.
- Nine-member count-in (`~1178.33–1216.70 s`) median ~**−30.50 dBFS**.
- Final `見つけたかも… 私の…夢！` median ~**−25.37 dBFS**; first ~6 s of ED ~**−24.82 dBFS**. These measurements describe episode-local mix structure, not permanent vocal timbre.



---

## S2E07 voice updates — role-purity shame, reciprocal mentoring, and cooperative authority

### Hazuki Ren

#### Concern-closing formal reassurance

- `心配ご無用です！` remains a polished concern-closing phrase.
- S2E07 proves it can be behaviorally inaccurate as a state report: Ren is overloaded and sleep-deprived while using it.
- **Model rule:** do not treat Ren's formal reassurance as automatic evidence that no support is needed.

#### Role-purity shame mode

- `仮にも わたくしは生徒会長` and `この学校をまとめる 私が…` convert a private self-control problem into office/institution vocabulary.
- The formality persists under shame; Ren does not become colloquially rough merely because the problem is private.

#### Polite help-seeking under concealment

- `これを 預かって頂けませんか？` preserves deferential request grammar even when Ren is panicked and trying to hide the issue.
- Her help-seeking can therefore be genuine while still serving a defensive strategy.

#### Old-self restoration language

- `今までのわたくしに / きっと戻れる` is a load-bearing identity phrase: the desired outcome is restoration of a prior self, not merely fewer play hours.

#### Game-strategy command mode

- `皆さん まずは 体力を半分まで削ります！`
- `かのんさん！ 後ろに回って！`
- Direct tactical imperatives coexist with polite address and task clarity.
- **Simulation rule:** Ren can become highly directive when she has domain knowledge without abandoning formal speech identity.

#### Disclosure/apology mode

- `黙っていて すみませんでした！` is concise and responsibility-taking; once she chooses disclosure, she does not bury it in a long justification.

#### Reflective institutional mode — REVISE content, PRESERVE register

- `お母様のつくってくれた学校` remains formal and maternal, but now leads to `とてもステキな出会い` and future improvement.
- Formality should not be equated with rigid duty; content/state determine meaning.

#### Acoustic state notes

- `心配ご無用です` is mixed-track high enough to function as confident closure (median100 ~−22.73 dBFS).
- Disclosure (`黙っていて…`) is followed by materially higher-energy group relief/laughter (median100 ~−31.77 → ~−22.95 dBFS).
- Ending reflection/piano occupies a lower-energy zone than the cooperative boss sequence.

### Shibuya Kanon

#### Residual self-diminishing entry

- `私なんて…` recurs when Chisato proposes a formal role.
- Do not interpret recurrence as reset: it is followed by institutional preparation and a direct vice-presidential request.

#### Qualified formal-service mode

- `私に 副会長 やらせてほしい`
- `力になりたいの`
- `頼りない私だけど…`
- This mode combines direct commitment with competence qualification.

#### Warm procedural/consent mode

- `理事長の許可は もらってきたよ`
- `あとは 恋ちゃんさえよければ…`
- Kanon can integrate relationship language, institutional procedure, and consent in the same support action.

#### Acoustic state notes

- `私なんて…` is materially lower-energy than Chisato's following returned rule (median100 ~−45.80 vs ~−33.38 dBFS).
- The vice-president offer is followed by a marked ~4.24-second lower-energy response interval.

### Arashi Chisato

#### Reciprocal mentoring mode

- `私も 部長にチャレンジしたよ？`
- `自分ができないって 思い込んでるだけ`
- `かのんちゃんの言葉だよ？`
- Pragmatic function: returns the interlocutor's own previously successful rule rather than giving generic reassurance.

### Yoneme Mei

#### Direct disclosure counsel

- `正直に 全部 話した方がいい` is concise, rough-casual, and autonomy-supportive.
- Mei does not threaten to expose Ren herself.

#### Conflict-tolerant friendship model

- `たまには ケンカもして / 仲良くなるもんだろ`.
- Rough register carries a nuanced relational thesis: intimacy does not require permanent harmony.

#### Incomplete autobiographical disclosure

- `私も昔 四季と…` trails off before the historical content is specified.
- Do not fill the ellipsis with later knowledge.

### Wakana Shiki

- `禁止` remains an extremely compressed boundary-setting form, here used to stop Natsumi's sensationalist content idea.
- `メイ… 思わせぶり…` adds an embarrassment/relational-reactivity mode under direct appreciation from Mei.

### Onitsuka Natsumi

#### Dream-aligned producer/support mode — STRENGTHEN

- `スクールアイドルを夢と定めた以上` explicitly upgrades S2E06's tentative dream grammar.
- familiar `マニー` / influencer vocabulary is redirected toward `Liella！を全力サポート`.

#### Sensationalist opportunity mode — PRESERVE

- apparent romance immediately triggers attention-oriented packaging.
- Shiki's `禁止` interrupts this mode externally; internal norm change remains OPEN.

### Tang Keke

- Love Live! announcement retains high-energy/theatrical competition presentation.
- Quickly challenges an authority assumption (`せっかく１年生が入ったのに？`) rather than treating senior creative ownership as invisible background.


---

## S2E08 voice updates — competitive visibility, distributed synthesis, and public junction language

### Shibuya Kanon

#### Integrative concept-compression mode

- During the search for a stage concept, Kanon can take another person's longer situated description and repeat it in compressed conceptual form.
- Kinako's account of crowded, lively streets becomes `どこも にぎやか... 人が集まる街...`.
- Later attention to `表参道` compresses further toward `道` before the full junction explanation.
- **Model rule:** when Kanon is close to conceptual synthesis, speech may move from repeated fragment/keyword → pause/movement → expanded explanatory structure.

#### Public representative mode

- Final address is explanatory and relational rather than boastful despite direct competition:
  - `誰かと誰かがつながり 結ばれていく`
  - `結ヶ丘は そんな学校です`
  - `｢Liella！｣の道が 結ヶ丘の道が あなたと 交わりますように`
- **Simulation implication:** competitive Kanon does not default to dominance rhetoric; resolved stage meaning can produce inclusive civic/relational language.

#### Acoustic architecture

- Concept seed (`1040.25–1052.56`) median mixed-track ~**−37.16 dBFS**.
- Run (`1054.70–1091.70`) ~**−32.93 dBFS**.
- Junction explanation (`1107.75–1143.65`) ~**−28.58 dBFS**.
- Treat as formal energy progression, not timbre/emotion evidence.

### Hazuki Ren

#### Shared-institution register — STRENGTHEN

- Student-council speech uses explicit co-authorship language: `ここにいる全員が誇れるような すばらしい学校を 共につくっていきましょう`.
- This differs materially from old solitary-duty formulations while preserving formal/polite register.

#### Residual dependency-shame vocabulary

- When peers offer long-duration support, Ren still frames the risk through `そこまで甘えるのは...`.
- **Model implication:** formal acceptance of help does not remove the lexical/moral association between prolonged dependence and `甘える`; relationship evidence can correct the inference afterward.

### Sakurakoji Kinako

#### Load-bearing newcomer enthusiasm

- `どこに行っても にぎやかで み～んな笑顔で`
- `きな子は 人が少ないところで育ったから`
- `それだけで ワクワクしてくるっす`
- Her established `～っす` register carries analytically important perception here; do not treat it as merely comic stylization.
- Self-disclosure about rural background is direct and unashamed.

### Tang Keke

#### Competitive spectacle / perseverance mode

- `目立つことが必要なのデス！` directly names the visibility problem.
- Grand-scale proposal language remains available under competition urgency.
- With Mei, school-idol persistence becomes theatrical collective rhetoric around refusing to give up before trying.
- She can abandon one impractical means without abandoning the underlying competitive goal.

### Yoneme Mei

#### School-idol anti-fatalistic rhetoric

- Joins/echoes Keke's `試してもみずに` / `諦めない` logic.
- Important developmental contrast: the girl who previously used `向いてない` as categorical self-exclusion can now voice a domain norm against premature surrender.
- Do not infer that this automatically resolves her own utility-conditioned exit risk under failure.

### Onitsuka Natsumi

#### Pro-group optimization mode — STRENGTHEN

- Competition still activates measurable-attention vocabulary: viewer interest, private incentives, `マニー` tiers.
- Trusted rival content activates `バズりますの` reflex even when confidentiality is central to the relation.
- These are now embedded-member speech modes, not only external producer modes.

#### Boundary-responsive trust mode

- After interruption, `信頼関係｡ わ... 分かってますの` shows explicit uptake of the trust frame.
- The slight textual stumble around `わ...` should be preserved as attested wording; do not inflate it into a stable vocal trait without recurrence.
- Current distinction: **recognizes a named relationship norm after prompting; does not yet reliably foreground it before optimization begins.**

### Heanna Sumire

#### Concise professional veto — STRENGTHEN

- Natsumi's vote/photo/money pitch is stopped with concise `無理！`.
- Her show-business/media judgment can surface as short practical boundary language without the longer recognition/status rhetoric associated with earlier Sumire conflict.

### Aria

- S2E08 gives a calm information-seeking/questioning sample around Yuigaoka's site history.
- Insufficient evidence for a broad voice grammar; preserve only the episode-local tendency to ask the structurally useful question others have normalized past.

### S2E08 acoustic transition into `Chance Way`

- Stage declaration (`1150.79–1183.83`) median mixed-track ~**−28.43 dBFS**.
- Declaration-to-song transition (`1183.83–1194.90`) lasts **~11.07 s**, median ~**−45.34 dBFS**, p10 ~**−81.77 dBFS**.
- Performance opening (`1194.90–1215.86`) median ~**−21.04 dBFS**.
- **Formal interpretation only:** spoken civic thesis is separated from the song by a materially lower-energy threshold before a higher-energy performance entrance.


---

## S2E09 voice updates — secrecy, sacrifice, competitive legitimacy, and antagonistic attachment

### Shibuya Kanon

#### Constitutive-membership declaration

- `５人だけで出場して勝っても 何の意味もない`
- `「Liella！」全員で挑まなきゃ意味がない！`
- `ここにいる全員が「Liella！」なんだもん！`
- Under group-definition pressure, Kanon's speech becomes short, categorical, and first-principle oriented rather than probabilistic.

#### Immediate defense against Wien

- Wien's `本当の歌` / `ちっぽけで くだらない` challenge receives immediate `くだらなくなんかない！` and `「ラブライブ！」は 最高の場所！`
- No `たまたま` or result-minimizing qualifier appears here.
- Model implication: direct external devaluation can currently activate defense of the shared domain rather than inward evidence discounting.

#### Repair self-correction

- After anger at Sumire, Kanon can acknowledge that Sumire may have her own circumstances and apologize for yelling.
- Do not model Kanon's categorical group language as inability to revise interpersonal handling.

### Tang Keke

#### Protective nondisclosure / boundary refusal

- `すみれには… 関係ないデス`
- Asked whether she cannot trust the others, Keke answers `できません`.
- She then specifies the value being protected: `可可は みんなと楽しく歌っていたいのデス` / `それが 可可が夢みた スクールアイドルなのデス`.
- The blunt refusal should not be flattened into simple distrust; the following explanation defines a protected relational ideal.

#### Junior-protective serious mode

- On whether to tell first-years about the gap, Keke speaks without comic escalation: `今 話したら きっと 頑張りすぎてしまう気がします` and fears `歌うのが つらくなってしまう`.
- This is a load-regulation register: direct concern about how information can change effort and affect.

#### Nine-member restoration

- `９人でいいんですよ`
- `大切なのは 全員で歌うことデス`
- `みんなで 最高のステージにすることなんデス`
- When the group has begun treating skill hierarchy as roster hierarchy, Keke uses simple declarative value language rather than elaborate persuasion.

#### Anger + attachment coexistence

- `うるさい！` and repeated `大嫌いデス` remain semantically real anger.
- Endpoint: `大嫌いで… 大好きデス`.
- Simulation rule: with Sumire under high-intensity relational conflict, contradiction can be expressed explicitly rather than resolved into a single clean affective label.
- Do not automatically convert this into romance; it is direct evidence of antagonistic high attachment.

### Heanna Sumire

#### Strategically selfish public register

- Foregrounds `ショウビジネスの世界に返り咲きたい` and `目立って 目立って 目立ちまくって` when defending the five-member proposal.
- These statements correspond to real prior ambitions, but S2E09 shows the register can also function as plausible cover for a concealed protective stake.

#### Private villain-self-talk

- `悪者になる覚悟は できてたはずでしょ？`
- Private speech makes explicit that being negatively judged is an accepted cost, not an unintended surprise.

#### Attachment disclosure

- `あんたと一緒にいたいのよ…`
- `３年間 一緒に スクールアイドル やりきりたいの！`
- Under collapse of strategic cover, Sumire becomes direct, relational, and temporally concrete.

#### Public disclosure under overload

- `帰っちゃうのよ… 勝てないと…`
- `結果残さないと この子が…`
- `可可が… 連れ戻されちゃうの…！`
- `いなくなっちゃうの～！`
- Speech breaks from strategy into repeated consequence/person naming; preserve the escalation rather than smoothing it into a calm summary.

### Arashi Chisato

#### Specialist competitive calibration

- `まだ 私たちと かなり実力差がある`
- `できてるのと 勝てるかどうかは また別の話`
- Coaching/presidential speech remains concise and criterion-based; “can execute” and “can win” are explicitly separated.

#### Consent-facing escalation

- `じゃあ １年生 覚悟はいい？`
- `今日から特訓開始するよ`
- `この９人で勝つために！`
- After the governance crisis becomes explicit, Chisato frames harder training as a challenge that requires acknowledgement rather than a hidden workload increase.

### Sakurakoji Kinako / first-year cohort

#### Self-removal as supportive request

- `だから 次のステージには立たない`
- `東京大会は ２年生 ５人で立つんですの`
- `勝つところを 見せて下さいっす！`
- The register is not defeatist collapse; the juniors present withdrawal as a contribution to the collective goal.
- This is important for simulation: harmful self-exclusion can be voiced positively/prosocially.

### Wien Margarete

#### Aesthetic-legitimacy challenge

- `私が 本当の歌を教えてあげる`
- `当日 その意味が分かるから`
- The challenge is declarative and instructional in form: Wien positions herself as the person who will demonstrate a standard to Kanon.
- `ちっぽけで くだらない` directly devalues Kanon's stage/community framework.
- Do not invent the unstated criteria behind `本当の歌`.

### Sunny Passion

#### Loss-without-devaluation mode

- Can say `慢心` / `油断` may have contributed while also stating they did not deliberately hold back.
- `たった一人に負けちゃったんだよね` names the structural shock without denying Wien's result.
- Advice to Liella! becomes temporally urgent: `一回一回を これが最後ってつもりで 挑んだ方がいいよ`.
- Their voice under loss remains generous toward Liella!, preserving mentor/rival coexistence.

### Onitsuka Natsumi

#### Threat-response attention tactics

- Under Wien threat, Natsumi can rapidly propose sabotage or online `炎上` manipulation in a comic operational register.
- The scene is evidence of available proposal grammar, not execution.
- Peer veto remains sufficient to stop the tactic in this boundary.

### Acoustic notes

- First-year message setup (`~1042.3–1057.18`) is unusually low-energy at about **−59.82 dBFS median**, followed by the first-year song (`~1062.65–1087.58`) at about **−25.83 dBFS median** and then the verbal withdrawal proposal.
- The formal sequence therefore moves **quiet approach → materially fuller musical statement → self-removal declaration**.
- Keke/Sumire confession/disclosure scenes sit in a lower-energy mixed-track range overall than the first-year song, but local escalation into the public Shanghai disclosure and `大嫌いで…大好きデス` is directly visible in cue structure and timing. Use these measurements as formal energy/timing evidence only.

---

## S2E10 voice updates — shared authorship, non-instrumental desire, and competing `true song` grammars

### Shibuya Kanon

#### Reciprocal creative-vulnerability mode

- With Kinako, Kanon does not speak from a completed/mastered position. Directly attested: `私もね すっごい恥ずかしいんだ`, `ノート全部 ビリビリにしたいくらい`, `私なんて 一人じゃ てんでダメ`.
- Pragmatic function: reduce prestige distance by exposing an ongoing matched vulnerability, then invite `一緒に 頑張ってみよ？`.
- **Simulation caution:** `私なんて` is not automatically identity collapse. Here it coexists with agency, mentoring, and creative work; interpret against behavior/state.

#### Rival-interpretive inquiry mode

- `本当の歌って 何なんだろう？` converts threatening comparison into a meaning question.
- Kanon can give direct positive evaluation of an antagonist: `すごいと思うよ`, `自分の世界を完全に描けてる`.
- She then marks inference explicitly/semantically: `マルガレーテちゃんも きっと歌が大好き`—the `きっと` belongs to Kanon's interpretation, not narrator-level certainty.
- Her reception language becomes image-based: `ただ それだけが胸に刺さる` / `まるで氷… みたいで…` for the `勝つ` motive she perceives.

#### Situated reflective `true song` mode

- Group reflection uses the qualifier `私たちにとって` and tentative `なんじゃないかな`.
- Model implication: when not in direct conflict, Kanon's meaning language can be situated and exploratory rather than universalizing.

#### Antagonistic categorical correction

- Backstage Wien challenge produces compressed repetition: `違う…` → `違うよ…` → `そんなの… 本当の歌じゃない`.
- This mode is more categorical than the earlier reflective formulation; preserve state dependence rather than smoothing into one philosophical register.

#### Public representation despite discomfort

- Remote press: after Keke's `えっと…`, Kanon continues a coherent institutional statement integrating previous failure, `全員で決勝`, possible `優勝`, and audience smiles.
- Afterward, she admits formal public speech still feels unfamiliar/uncomfortable in substance; competence ≠ comfort.

#### Post-rival mobilization

- After `Edelstein`, concise action language returns: `さあ いこう！` / `Liella！の歌を 渋谷の街に響かせようよ！`.
- Function: does not debate Wien further; redirects group attention to audience/community task.

### Arashi Chisato

#### Task-reframing mentorship

- `別に ダンスで 私と競争しようっていうんじゃないよ？` explicitly rejects Shiki's assumed comparison frame.
- `一緒に 振り付けを考える` / `力を貸してほしいんだ` gives direct collaborative purpose while preserving Chisato's specialist position.
- Her next lines operationalize participation through first-move → observe → opinion, showing coaching language can redesign the task rather than merely encourage effort.

#### Playful authoritative rest mode

- `今日は～ 練習なし～！` uses playful elongation for a real policy decision.
- Followed by concise principle `頑張るためには 休みも大事！` and then stronger de-instrumentalization `歌も練習も 全部忘れて みんなで楽しく遊ぼう！`.
- **Model rule:** playful delivery does not imply low authority; Chisato can soften the surface while making a binding training decision.

### Yonome Mei

#### Rough competence-minimization mode

- `私に期待すんなよ？` and `勘弁してくれよ…` occur inside a scene in which Mei ultimately contributes.
- She frames piano history bluntly: `小さい頃から 親にやらされてただけだからな`.
- **Simulation caution:** rough/negative surface is compatible with cooperation and vulnerability; do not overtranslate into hostility/refusal.

#### Creative completion mode

- Later reports `曲も完成したぞ` with direct, compact completion language.
- Current voice model includes an available matter-of-fact competence mode after participation has become concrete.

### Wakana Shiki

#### Compressed feasibility judgment

- `それは理解｡ でも無理｡` separates intellectual agreement from practical self-assessment with minimal verbal padding.
- Extended beetle/roly-poly analogy supplies a dry, technical-comic comparison framework rather than emotional self-denigration.
- The subsequent behavioral shift after task reframing means `無理` should often be treated as a current model of feasibility, not a permanent preference/value.

#### Creative completion mode

- `振り付け 決まった` is maximally compressed and matter-of-fact; high-value sample for confident domain-status reporting.

### Sakurakoji Kinako

#### Creative-shame mode

- Begins with enthusiastic senior address `かのん先輩～` and asks whether lyrics have “descended,” then reveals the notebook before retracting: `やっぱり 恥ずかしい！`.
- Self-minimization: `そんな… きな子の言葉なんて とても…`.
- Under matched vulnerability, she can accept collaboration without needing a dramatic confidence declaration.

#### Authorship completion

- `出来たっす 歌詞` preserves characteristic `っす` register while announcing a serious creative output.
- Model implication: Kinako's informal junior speech does not diminish substantive authorship.

### Hazuki Ren

#### Ordinary co-op mode

- Gaming can elicit overt frustration/excitement (`難しすぎます！`) within her otherwise formal baseline.
- The mode is not incompatible with rapid return to composed mentoring.

#### Evidence-based encouragement with inference

- `続けてこられたということは 嫌いじゃなかったはずです` uses polished inference rather than empty praise.
- Important simulation rule: Ren may reason from behavior/history to motive, but such statements remain her inference and can be wrong.

#### Turn-allocation mentorship

- `フフッ｡ 次は メイさんですよ` combines mild warmth with direct task handoff.

### Tang Keke

#### Formal-public stall

- `えっと…` during the remote press event is a meaningful vulnerable mode because ordinary Keke is often highly explicit and forward-moving.
- She later thanks Kanon for helping. Do not model Keke as universally fluent merely because she is enthusiastic and theatrical in familiar contexts.

#### Post-repair bickering with Sumire

- `すみれが うるさいからデ～ス！` returns to familiar irritated/comic dyadic grammar after S2E09's emotional confession.
- The `デ～ス` stylization here belongs to low-stakes conflict continuity, not relational rupture.

### Heanna Sumire

#### Post-repair ordinary irritation

- `可可が強情なだけよ` presents Keke's stubbornness as a mundane explanation while the relationship remains intact.
- Useful contrast with S2E09's serious attachment/villain-mode speech.

### Onitsuka Natsumi

#### Relationship-model confusion

- Observes Keke/Sumire: `抱き合って 泣いてみたり けんかしてみたり / それで いいんですの？`.
- This is a compact attested sample of Natsumi trying to reconcile affective closeness with overt conflict.

#### Non-monetized desire-search mode

- `私の… やりたいこと…` contains a rare pause around first-person desire not already formatted as a business/content objective.
- Once identified, speech becomes exuberant: `思い切り 雪合戦したかったんですの～！`.

#### Metric reflex recurrence

- `もっと 映える映像を`, money-value talk, `時間を無駄にしてしまったですの`, and later `これは バズる話題ですの！` preserve a strong attention/productivity lexical field.
- The new desire mode and old metric mode coexist; neither should erase the other.

### Wien Margarete

#### Public universal-evaluator mode

- `ここが いかに低レベルであるかを / スクールアイドルたちに 知ってもらうため` positions Wien above the field as evaluator/teacher.
- `私が 本当の歌を教えてあげる` is declarative and hierarchical, with almost no mitigation.

#### Self-authored power doctrine

- `歌は力` is extremely compressed definitional grammar.
- `そして 私は 未来を 私自身でビルドする / 歌の力で` combines self-emphasis (`私自身で`) with directly attested loanword `ビルドする`.
- Model implication: Wien's current serious ideological mode is concise, declarative, self-authorizing, and future-oriented.
- **Do not** invent accent/foreign phonology from this textual evidence.

#### Kanon-targeted address

- Repeated full-name `澁谷かのん` functions as marked direct targeting before the doctrinal challenge.
- Motive for the targeting remains OPEN.

### Liella! ensemble / ritual

- Public identity line remains `結ヶ丘スクールアイドル部 ｢Liella！｣！` followed by outward task `たくさんの人に歌を届けよう！`.
- Inherited ritual persists under maximum rival intimidation: `Song for Me！ Song for You！ / Song for All！`.
- The ensemble voice therefore preserves self → other → all sequencing at the point of direct competition.

### Acoustic-state notes @ S2E10

- Kanon's reflective `true song` block (630.61–699.38) is a lower-energy mixed-track space (~−31.68 dBFS) than nearby junior practice/rest decisions.
- Wien backstage declaration/pre-performance window (~−44.59) contains substantial low-energy gaps; do **not** convert this into “quiet voice” characterization.
- `Edelstein` (~−20.39) → post-stage reaction/setup (~−29.83) produces a marked formal energy drop before Kanon mobilizes Liella!.
- `Sing! Shine! Smile!` (~−18.25) is high mixed-track energy; production/mix/crowd factors prevent using this as artistic-superiority evidence.
---

## S2E11 voice updates — result legitimacy, dream-route disclosure, and owned counter-preference

### Shibuya Kanon

#### Result-legitimacy mode

- Against Wien's attempt to invalidate the verdict, Kanon says `それは できない｡ / だって 私たちの方が… 勝ったと思ったから｡`
- The ellipsis/qualification does not prevent completion into a direct comparative judgment.
- **Longitudinal contrast:** unlike S2E03's `たまたま`, Kanon does not verbally downgrade the favorable result merely because another performer is obviously formidable.
- **Simulation rule:** current Kanon can state that her group legitimately won without becoming boastful or claiming universal technical supremacy.

#### Sacred-domain / participation-boundary mode

- Immediately after Wien rejects the result, Kanon says `スクールアイドルは 一人じゃない` and then `マルガレーテちゃんには スクールアイドルのステージに立ってほしくない` if the collective dimension cannot be understood.
- This is unusually categorical/gatekeeping language for Kanon.
- Do not smooth this into purely empathetic pluralism; under direct devaluation of a practice she treats as relationally sacred, her speech can become exclusionary before motive inquiry resumes.

#### Motive-inquiry mode after conflict

- `なんで あんなこと言ったんだろう` followed by `それだけなのかな…` rejects the easy explanation that Wien is merely frustrated.
- This mode is quieter and epistemic rather than accusatory: Kanon marks explanatory incompleteness and then investigates.

#### Structural-analogy empathy without leveling

- After Wien says `一緒にしないで！ / あんたなんかとは レベルが違う`, Kanon does not defend equal ability.
- She narrows the claim: `でも 夢が奪われたように思えたのは きっと同じ…｡`
- `きっと` functions as bounded inference; the utterance preserves analogy while respecting the contested competence asymmetry.

#### Dream-autobiography mode

- Kanon can sustain direct autobiographical explanation about childhood aspiration, enjoyable practice, sudden inability to sing publicly, and the music-course route becoming unavailable.
- This is not framed to prove technical equivalence with Wien; it is used to disclose a structure of dream loss.

#### Present-route authorship mode

- Key sequence:
  - `歌が大好きって また言えるようになった｡`
  - `だから この学校に ずっといたい｡`
  - `私の選んできた道は 間違ってなかった`
- The language is affirmative and temporally integrative: prior failure, present recovery, and future desire are connected without claiming the childhood route must be restored.

#### Formal refusal with mitigation

- `はい｡ やっぱり ピンとこなくて…｡` is mitigated/phenomenological rather than triumphant.
- After the headmistress says `決めるのはあなたよ`, Kanon gives a final `…はい`.
- **Model rule:** in Kanon's current voice, soft/qualified language can carry a firm decision. Do not equate `ピンとこない`, ellipses, or quiet delivery with indecision when enacted choice is explicit.

### Wien Margarete

#### Result-rejection mode

- `ありえない！ / 私は この結果を認めない！`
- Highly categorical; no mitigation or procedural appeal.
- The voice treats the verdict as invalid rather than merely disappointing.

#### Hierarchy-defense interpersonal mode

- `一緒にしないで！`
- `あんたなんかとは レベルが違う｡`
- Rougher interpersonal grammar (`あんた`) appears when Kanon proposes experiential analogy that Wien hears as status leveling.
- Preserve separately from Wien's polished/public declarative doctrine.

#### `フン！` nonlexical-pragmatic marker — established Season-2 baseline

- **~08:18.96:** corrected Japanese ASS explicitly contains `フン！`; English comparison ASS explicitly contains `Hmph.`
  - Function: **grudging engagement / pride-preserving concession** after Kanon persists and Wien allows the interaction to continue.
- **~11:22.01:** corrected Japanese ASS explicitly contains `フン！ 意味分かんない｡`; English comparison ASS explicitly contains `Hmph! Whatever.`
  - Function: **defensive dismissal / retreat** after Kanon's relational performance argument reaches a point Wien cannot assimilate within her current hierarchy-first model.
- **Longitudinal rule:** treat `フン！` as an attested Wien voice marker already present by S2E11, but do **not** assign it one fixed meaning. Track the same surface form across later episodes for context-dependent shifts such as contempt, embarrassment repair, reluctant comprehension, attachment management, or other functions only when locally evidenced.
- **Correction provenance:** these subtitle events were present in the canonical S2E11 JP/EN source bundle but were under-formalized in the original V2.2 voice-ledger update. This is a factual/source-locator correction, not a retrospective Season-3 inference.

#### Vulnerable factual-disclosure mode

- After Kanon's repeated demand, Wien begins with compressed `条件だったの｡`
- She then shifts into institutional nouns and procedures: exam failure, recommendation, transfer, family recommendation, sisters.
- **Voice implication:** when cornered into explaining a vulnerable constraint, Wien can become terse and concrete rather than grandiose.

#### Privileged-evaluator appeal

- `あなたなら分かるでしょ？`
- Wien expects Kanon specifically to recognize the individual-performance hierarchy she believes the audience failed to respect.
- This is not generic audience persuasion; it is relationally targeted epistemic pressure.

#### Reluctant-dependency grammar

- `かのんに連れられて戻るのは 癪だけど`
- `それで 学校に入れるのなら それでも…`
- The concessive structure preserves resentment **inside** acceptance rather than replacing it.
- If Kanon will not go: `自分の力だけで` restores the self-reliance register.
- For simulation, Wien can accept help/dependency while verbally marking the status cost very sharply.

### Arashi Chisato

#### Urgent information-demand mode

- `教えてくれるまで 離さない！`
- Direct, persistent, and physically backed by refusal to release Wien.
- This is high-stakes person-protective speech, not baseline coaching/playfulness.

#### Owned counter-preference mode

- Sequence:
  - `反対されるのは分かってる｡`
  - `でも 正直な気持ちだから はっきり言うね｡`
  - `私 かのんちゃんに… 留学してほしい｡`
- Pragmatic structure: **anticipate opposition → identify statement as own honest feeling → speak directly**.
- Crucially absent: `部長として`, imperative grammar, claim of decision authority.
- This extends Chisato's long-standing tendency to state her desire rather than substitute it for Kanon's choice, while greatly raising the stakes.

### Tang Keke

#### Sacred-domain roughness — recurrence

- `神聖な｢ラブライブ！｣に 泥を塗りやがって！`
- Confirms the rough `～やがって` family remains available when Keke experiences devaluation of school idols as sacrilege.
- Do not generalize to ordinary interpersonal irritation.

### Onitsuka Natsumi

#### Reputation-diagnostic media mode

- Reports that Wien is receiving criticism `ものすごい勢いで` and reads representative comments.
- This mode uses media awareness for situational diagnosis rather than immediate revenue/virality planning.
- Preserve alongside older `マニー`/viral/production modes; it is an added register, not replacement.

### Hazuki Ren

#### Plural institutional gratitude mode

- `私たちと 学校のみんなの力で！`
- Later public thanks while naming both student-council president and Liella! membership.
- Formal register remains, but the subject of achievement is deliberately plural rather than solitary or prestige-gatekeeping.

### Sakurakoji Kinako

#### Founder-trust comic disclosure

- In panic about Kanon leaving, says that without Kanon there is no remaining senior she can trust.
- The comedic surrounding reaction matters; do not treat the wording as a fully deliberated relationship ranking.
- It nevertheless provides attested speech evidence that Kinako can disclose extreme dependence/trust asymmetry bluntly under separation threat.

### Headmistress

#### Autonomy-supporting institutional mode

- Presents the Vienna offer as opportunity, not command.
- `もちろん 自由よ`
- `ゆっくり考えなさい`
- final `決めるのはあなたよ｡ いいのね？`
- This voice grammar is important institutional counterevidence: authority can foreground stakes and verify regret without substituting its own choice.

### S2E11 acoustic-state notes for voice modeling

- After Kanon's `教えて！`, the ~2.11 s low-energy gap before Wien's `条件だったの` supports a formal threshold into disclosure; do not infer a named emotion from RMS alone.
- The Chisato/Wien exchange contains ~6.08 s of materially lower-energy space before the family-condition disclosure, marking a prolonged transition from resistance to explanation.
- Kanon's final formal `…はい` is followed by ~4.28 s at roughly −68.21 dBFS median before the Chisato doorway reveal. Treat this as a formal separation between completed decision and newly introduced counter-pressure.
- Chisato's final `留学してほしい` sequence remains acoustically restrained relative to public result blocks; its force comes from direct wording and unresolved cut rather than sheer mixed-track loudness.

---

## S2E12 voice updates — route reconsideration, continuity, championship, and canceled departure

### Shibuya Kanon

#### Authorship-defense mode

- `でも 決めたのは私｡ 私は この学校に…！`
- The wording locates agency explicitly in the first-person chooser even while Kanon is under direct relational challenge.
- Do not paraphrase this as inability to hear others; it is defense of ownership, not refusal of dialogue.

#### Fear-disclosure mode

- `そんな大切な場所と 仲間を失ってしまうのが 正直 怖いんだ｡`
- `正直` marks the disclosure as an admission about decision weight, not a replacement statement that Yuigaoka is only fear.
- This is important for simulation: Kanon can name fear directly after substantial development instead of converting it into `私は無理` or burden self-erasure.

#### Re-authored decision mode

- `私 ここに来る前に決めてきた｡`
- `留学… しようと思う｡`
- followed by positive-purpose language: represent Yuigaoka, grow further, `挑戦してみる`.
- The pause/ellipsis preserves difficulty, but the grammatical structure is first-person decision rather than submission.

#### Formal future-commitment mode

- `歌で世界を幸せにしたい｡`
- `世界に 歌を響かせられるよう 精いっぱい頑張ります｡`
- This reconnects childhood/global aspiration to the current relationally formed self without claiming the old route was always continuously active.

#### Liella-continuity mode

- `一人でも欠けたら ｢Liella！｣じゃない`
- `この９人で｢Liella！｣だって気持ちは 私だって そう思う`
- then `でも やめてほしくない`.
- Kanon can hold apparent contradiction in explicit paired clauses rather than resolving it by redefining the current nine as non-constitutive.

### Arashi Chisato

#### Direct counter-preference mode

- `私は かのんちゃんに夢を叶えてほしい｡`
- `かのんちゃんにしか叶えられない夢を｡`
- `今しかない… チャンスなんだよ…？`
- High relational force, but the pronoun ownership remains Chisato's desire rather than an institutional command.

#### Answer-verification mode

- `かのんちゃんが考えて出した答え もう一度 確かめたくて｡`
- This is the cleanest verbal evidence that her intervention aims to reopen deliberation rather than simply announce the correct answer.

#### Talent-recognition mode

- `｢Liella！｣で 一番のスーパースター`
- `それって… 才能だと思う`
- The target is Kanon's ability to energize/give courage and reach people, not a narrow technical-score vocabulary.

### Wien Margarete

#### Self-contradiction recognition

- `私ってば 口先ばっかり｡`
- A rare self-indicting compression after her own behavior contradicts `自分の力だけで` rhetoric.

#### Pride-qualified dependency mode

- `あなたに連れられて戻るのは 正直 嫌だけど`
- `自分の夢のためだから どんな方法でも 条件でも 私は かまわない｡`
- Preserves both aversion and willingness; do not simplify into either “she welcomes help” or “she refuses dependence.”

#### Transparent instrumental mode

- `勘違いしないでね｡ 私は ウィーンに戻れたら それでいいの｡`
- Wien can offer a plausible benefit to Yuigaoka while explicitly refusing altruistic misattribution of motive.

#### Cancellation announcement

- `見てのとおりよ｡ 留学は中止｡`
- At the seal, treat as statement of state only. No causal explanation is admissible.

### Heanna Sumire

#### Ambivalent attachment mode

- `いてほしいし いてほしくない｡`
- Compactly carries selfish desire for proximity and prosocial desire not to block the opportunity.
- Keke's `何デス？ それ｡` and Sumire's `相変わらず 鈍感ね｡` preserve ordinary interpersonal friction around the serious content.

#### Post-goal continuation mode

- `全国大会が終わったら ｢Liella！｣は解散かと思ってたのに`
- `やめられなくなっちゃったよ｡`
- This is unusually direct evidence that attachment has outgrown the bounded original competition horizon.

### Onitsuka Natsumi

#### Public boast / private first-place split

- public: `ま 私がいれば 当然ですの｡`
- private/lowered-exposure: `初めての １等賞…｡`
- when noticed: `何でもないですの！`
- Preserve the mode switch: self-branding does not exhaust the meaning of the result.

### Wakana Shiki

#### Laconic affective deflection

- `みんな 頑張った…`
- after Chisato reacts: `違う｡ これは汗｡`
- Physical reclassification remains an available low-exposure defense against emotional naming.

### Hazuki Ren

#### Intimate autobiographical formality

- Says that before Yuigaoka she had no friend with whom she felt a deep bond and that others viewed her as from a different world.
- Her polite/structured grammar remains even while the content is unusually personal.

#### Explicit friendship naming

- Chisato: `もちろん恋ちゃんも 親友だと思ってるよ｡`
- Ren: `わたくしもです｡`
- This is direct mutual relational labeling, not inferred closeness.

#### Distributed-stewardship gratitude

- `お母様のつくった学校を みんなの力で 大きく成長させることができました｡`
- Formal speech now encodes plural agency where earlier Ren language concentrated duty in the self.

### Tang Keke

#### Shared-dream support mode

- `かのんの夢は みんなの夢デス！`
- This is support language, not evidence that the group owns Kanon's decision.
- Later departure preparation converts support from rhetoric into behavior: she promises to work harder and tells Kanon to leave confidently.

### Yoneme Mei

#### Jurisdictional rough restraint

- `私らが どうこう言える話じゃないだろ｡`
- Rough register functions here as principled restraint rather than rejection or indifference.

### Sakurakoji Kinako

#### Uncertain-action pair

- `できるかな…`
- `きな子 やるっす！ やってみるっす！`
- The pair should be preserved together. Her mature mode is not certainty; it is action chosen while uncertainty remains.

### S2E12 acoustic-state notes for voice modeling

- Opening Chisato challenge window: median mixed/mono RMS approximately **−36.36 dBFS**.
- Chisato/Ren friendship: approximately **−30.87 dBFS**.
- Family deliberation: approximately **−29.69 dBFS**.
- Wien self-revision: approximately **−32.84 dBFS**; Kanon fear disclosure approximately **−29.63 dBFS**; Wien route reframe approximately **−29.04 dBFS**.
- Night-school Chisato answer-verification: approximately **−32.15 dBFS**; Kanon Vienna choice approximately **−27.78 dBFS**; following group support approximately **−29.38 dBFS**.
- Formal headmistress commitment: approximately **−27.97 dBFS**.
- National song: approximately **−17.98 dBFS**, far higher mixed-track energy than adjacent dialogue. Do not use this to infer vocal/performer superiority because music/production dominate the measurement.
- Winner celebration: approximately **−25.23 dBFS**.
- Cancellation cliffhanger: approximately **−28.47 dBFS**.
- These are formal timing/energy observations only; do not assign timbre, precise emotion, or actor intent from RMS values.



---

## S3E01 voice updates — chosen differentiation and rival-club formation

### Shibuya Kanon

#### Social-embarrassment / return-without-reset mode

- After the canceled departure, Kanon hides rather than immediately announce herself to Liella! because the group has already performed a farewell and reorganized around her absence.
- The language is comic/social (`戻ってきちゃいました`-type imagined reentry), not a return to early `歌えない` incapacity language.
- **Model rule:** hesitation after a public relational commitment can reflect concern about invalidating a shared narrative, not generalized low confidence.

#### Direct organizational-boundary mode

- `私 「Liella!」には戻らない。` is concise, first-person, and unhedged.
- Kanon then expands from boundary declaration into relational/system language: `切磋琢磨`, `みんなが納得できる ゴール`, `もっとステキな未来`.
- **Voice implication:** mature Kanon can state a painful boundary directly, then explain it through collective future construction rather than soften the boundary itself.

#### Formal applicant mode

- `私 入部を希望します！` uses clear institutional club-entry language.
- The written `入部届` complements rather than contradicts her spoken route: teammate reciprocity, communicating the appeal of Wien's singing, mutual elevation.

### Arashi Chisato

#### Direct personal-preference mode

- `私は かのんちゃんに戻ってきてほしい` is a clear first-person desire statement.
- It does not hide behind club-presidential procedure or neutral advice.

#### Autonomy-restoring close

- `急がなくていい` explicitly removes urgency.
- `自分の信じる道を 突き進む かのんちゃんでいて` returns decision ownership to Kanon while preserving Chisato's prior disagreement.
- `おかえりなさい` closes on relational welcome rather than organizational demand.
- **Cross-episode voice rule:** Chisato can be direct about what she wants and still linguistically restore another person's authorship.

### Wien Margarete

#### Rival/enemy categorization

- Continues to use sharp categorical competition language, including `敵` for Liella! and repeated `勝ちたい` formulations.
- `私は私 かのんはかのんよ` is a compact identity-separation statement when others try to connect her route automatically to Kanon's.

#### Self-legitimation directness

- `そんなことは分かってる！` explicitly concedes the strategic argument before rejecting it.
- `でも私は あなたたちに勝ちたいの！` / `Liella!に勝ちたい！` / `じゃなきゃ 自分が納得できないの！` form an unusually transparent motive sequence: knowledge → preference → self-congruence criterion.

#### `フン！` baseline audit — PRESERVE, no new explicit instance

- S2E11 remains the established baseline with at least two explicitly subtitled `フン！` occurrences carrying different pragmatic functions.
- S3E01 corrected Japanese contains **no explicit `フン` / `ふん`** attributable to Wien; the English subtitle layers contain no `Hmph` equivalent.
- `フフッ`-type laughter/chuckles are not counted as the same marker.
- **Model rule strengthened:** `フン！` is a context-dependent nonlexical-pragmatic device, not mandatory punctuation for every contemptuous, rivalrous, or embarrassed Wien scene.
- Subtitle absence is not proof that every nonverbal exhalation is acoustically absent; no new confident unsubtitled instance is asserted.

### Hazuki Ren

#### Formal integration-to-pluralism mode

- Ren's speech first frames two internal idol groups through school efficiency/cohesion, then shifts after Wien's refusal to the broader common identity of being Yuigaoka students.
- Politeness/formality remains compatible with changing institutional strategy rather than rigid enforcement.

### Tang Keke

#### Restoration-expectation mode

- Kanon's return immediately activates shared-route language: the intuitive assumption is resumption of Liella! and repeat championship.
- After Kanon's refusal, Keke can state non-understanding rather than instantly simulate agreement.
- Do not convert this into a universal possessive register; S3E01 shows confusion and attachment, not coercive speech authority.

### Sakurakoji Kinako

#### Responsibility-plus-loneliness mode

- Supports harder training under Kanon absence, then later openly says she is lonely and cries at the organizational split.
- The voice model should permit practical commitment and emotionally transparent attachment in the same state.

### Onitsuka Natsumi

#### Commercial-metrics recurrence

- Views/monetization/sponsor framing remains readily available and can push her into rationalizing publication behavior against group rules.
- Preserve separately from the private noncommercial meaning of S2E12's first-place experience.

### Unidentified apparent first-year

- Post-credits speech includes the English phrase `アイ アンダースタンド。` after she approaches the new school-idol club.
- At the S3E01 boundary her identity, stable register, and multilingual pattern are **OPEN**. Do not assign a future name or trait set.

### S3E01 acoustic-state notes for voice modeling

- Liella successor-practice block (~05:27–06:40.5): median 100 ms mixed-track RMS **−25.96 dBFS**.
- Hidden-Kanon interval (~06:40.3–06:53.3): **−31.50 dBFS** median; formal energy drop from active group block into liminal observation.
- Wien self-legitimation confrontation (~12:47–13:30.9): **−27.96 dBFS** median with 10th percentile ~**−55.75 dBFS**, indicating wide speech/space dynamics without licensing timbre/emotion claims.
- Chisato/Kanon route conversation (~14:29–15:47.22): **−33.31 dBFS** median.
- 4.97 s post-`おかえりなさい` transition (~15:47.22–15:52.19): **−49.96 dBFS** median before the performance block.
- These are AM/formal measurements only. Do not infer actor intention, exact emotional color, accent, or timbre from them.

---

## S3E02 voice updates — Wien huff recurrence, Tomari procedural register, and post-performance disclosure

### Wien Margarete

#### `フン！` — third established longitudinal role

- **00:45.39–00:47.33:** corrected Japanese explicitly captions `フン！` after Kanon invokes Wien's own `学年 経験 問いません` recruitment terms.
- English contains no `Hmph` equivalent.
- Current function: **rule-trapped resistance / pride-preserving objection**.
- This differs from S2E11's grudging-engagement and defensive-dismissal instances while preserving the common grammar that Wien has been affected/boxed into a position she does not want to grant cleanly.

#### Do not overcount huffs

- Around ~10:38.7, Wien says `本当？` after Kanon calls her cute, while corrected Japanese explicitly captions Kanon's concurrent `フフフフッ`.
- Around ~11:55.8, Wien has accurately summarized Kanon's school-idol logic, while corrected Japanese explicitly captions Kanon's `そうそう！ ウフフッ`.
- Historical V1 analysis proposed additional Wien huffs in these intervals, but the V2.2 mixed audio cannot uniquely isolate or lexically identify a Wien `ふん` from the overlapping laughter.
- **Canonical count for S3E02: one explicit new `フン！`; two historical/provisional candidates not promoted.**

#### Spontaneous-receptivity → defensive-repair mode

- `本当？` momentarily exposes pleasure/interest in Kanon's praise.
- `かのんが うるさいから アイドルっぽくしてみただけ` retroactively reframes the action as reluctant compliance.
- Model the transition rather than forcing a catchphrase into it.

#### Anti-pity directness

- `黙らないでよ。みじめな気持ちにさせたいの？`
- Wien prefers direct interaction to careful silence that positions her as pitiable.

#### Relationship-label defense

- `あんたと友達になるために来たわけじゃない` / `勘違いしないでよね`.
- Strong tsun-coded grammar; function is to deny interlocutor authority to label practical/domestic proximity as friendship.

#### Vulnerable positive-state report

- `歌… 久しぶりに 楽しいって思えた` is a new major mode: direct positive internal-state disclosure to Kanon with no immediate conversion into superiority rhetoric.

### Onitsuka Tomari

#### Formal/procedural baseline

Attested recurrent constructions include:

- `契約において`
- `通常無効とされます`
- `必要と判断すれば`
- `無駄な時間は過ごしたくない`
- `不可能と判断されます`
- `したがって`
- `お構いなく`

Model as **condition → calculation → conclusion → action** syntax. Do not caricature as emotionless or robotic.

#### Family address

- Calls Natsumi `姉者`.
- The marked family term coexists with public correction, analytic distance, and private concern.
- Do not generalize one address term into a globally archaic register.

#### Post-participation skepticism

- `価値のあるものとは 思えませんが` retains controlled/formal skepticism even after the shared live.
- Participation should not be simulated as automatic warm speech shift.

### Shibuya Kanon

#### Compact value-boundary refusal

- Tomari's monetization proposal receives immediate `ダ～メ！`.
- Contrast with Kanon's willingness to accept Tomari's forecasting/publicity work: direct refusal is value-specific, not anti-specialist.

#### Crisis reorientation mode

- `歌おう` is short/direct, followed by explicit challenge/effort/song-power reasoning.
- When Kanon has reached conceptual clarity, she can become more linguistically compressed rather than more hedged.

#### Mentoring without forced conversion

- Tomari's `価値...思えません` is answered by laughter + `いつか分かるよ！`, not argument demanding immediate assent.

### Onitsuka Natsumi

- Tomari quoting Natsumi's dream language triggers sharp embarrassment/interruption.
- Later Natsumi becomes direct about seriousness toward the practice and teammates.
- Preserve both commercial/persona modes and this more exposed sister-conditioned mode.

### Tang Keke

- Split anxiety produces exaggerated accusation/manipulation framing early.
- Endpoint `かのん 最高デス～！` confirms extremely explicit praise remains available despite unresolved disagreement over Kanon's route.

### S3E02 acoustic notes for voice modeling

- Explicit `フン！` window 00:45.39–00:47.33: median 100 ms mixed-track RMS **−58.51 dBFS**, with a brief local peak region around 00:45.61.
- ~10:37.62–10:39.89 overlap: median **−41.25 dBFS**; attribution contaminated by explicitly subtitled Kanon laughter.
- ~11:54.79–11:57.16 overlap: median **−38.36 dBFS**; same limitation.
- Wien-accountability / transition block 18:08.50–18:41.53: median **−49.44 dBFS**; especially 18:28.62–18:41.53 median **−50.83 dBFS**.
- Kanon crisis-reorientation block 18:41.53–19:25.31: median **−37.34 dBFS**.
- Pre-performance bridge 19:25.31–19:34.29: median **−64.47 dBFS**.
- These are AM/formal facts only; no timbre/emotion/actor-intent claims should be generated from them.



---

## S3E03 voice updates — succession, role redefinition, and guarded rival investment

### Arashi Chisato

#### Post-achievement uncertainty mode

- Sustains vulnerable reflective speech about winning Love Live!: `これ以上 幸せな瞬間ってあるのかな`, `目指す目標とか なくなっちゃうのかな`.
- This is not a collapse of leadership; it precedes a clear new-goal formulation around rivalry/creation.

#### Kanon-comparison self-doubt

- `やっぱり 私じゃ かのんちゃんみたいには うまく回せないな` is direct and self-comparative.
- Model rule: Chisato can openly admit leadership uncertainty rather than maintaining a permanently competent coaching voice.

#### Role-reframing declaration

- `待って！` sharply interrupts the replacement consensus.
- Repeated structures `いろんな人`, `いろんなセンター` turn plurality into a governance argument.
- `ひと言でいうと 「白」！` compresses a complex person/role thesis into a concrete visual metaphor.
- Voice model should allow a path **reflection -> self-doubt -> conceptual simplification -> decisive proposal**.

### Wakana Shiki

#### Structured self-classification mode

- Despite generally low-temperature speech, Shiki sustains a long causal account of her own social history and center mismatch.
- Load-bearing phrases: `自分はそういう人なんだって`, `私は違う`, `私じゃない方がいい`, `みんなに迷惑かけるだけ`.
- Do not simulate Shiki as incapable of extended self-analysis merely because her baseline is quiet/elliptical.

#### High-exposure state

- `まぶ…しい…` precedes collapse in the initial center test.
- Before the live: `倒れそう…`, `すごく…` in response to nervousness.
- Successful performance does not erase hesitant/low-output speech before action.

#### Emerging self-authorship

- Post-live `これが… センター…`, later `私だけの…` is fragmentary rather than triumphant rhetoric.
- Model the change as experiential discovery emerging through Shiki's existing concise register.

### Yoneme Mei

#### Concrete protective commitment mode

- Direct/rough supportive grammar: `私が陰になってやる`, `私も一緒に引っ張ってやる`.
- Before live: offers `私が注目を集めてやる` even though Shiki notes Mei also dislikes standing out.
- This register should be read as committed action under intimacy, not aggression.

#### Shiki-specific validation

- `そんな四季だから できるセンターだってある` / `そんな四季じゃなきゃ...` validates identity while refusing self-exclusion.
- Distinguish from generic “you can do it” reassurance.

### Shibuya Kanon

#### Pluralist membership boundary

- `嫌だよ！` is immediate/direct when Wien proposes exclusion.
- Follow-up uses inclusive generalized propositions rather than personal pleading: `いろんな人がいるから`, `いろんな色があるから`.
- Her leadership voice can convert a concrete interpersonal dispute into a portable principle.

### Wien Margarete

#### `フン！` longitudinal audit — no new S3E03 occurrence

- Corrected Japanese S3E03 contains no `フン` / `ふん`.
- English layers contain no `Hmph`.
- **Canonical baseline remains:** S2E11 two distinct uses + S3E02 rule-trapped pride-preserving objection.
- Negative evidence further supports a context-conditioned marker rather than mandatory Wien punctuation.

#### Rival-investment defensive repair

- `まったく なんて混雑よ / だから 来たくなかったのよ` presents attendance as unwanted.
- Tomari's first-ticket fact triggers `うっ うるさい！`.
- Do not reclassify this as `フン！`; it is separately attested flustered denial/defensive repair.

#### Post-performance action-directive

- `かのん。練習 行くわよ。` is concise, imperative, and immediately action-oriented.
- Exact internal motive remains open; the available voice fact is a direct turn from spectatorship to practice.

### Onitsuka Tomari

- Formal/analytic baseline persists around necessity-filtered attendance.
- At Liella! live, dry factual correction (`いの一番に チケット購入したと聞きましたが`) punctures Wien's self-presentation without matching her emotional heat.
- `姉者` remains attested in sibling-conditioned speech/action.

### S3E03 acoustic notes for voice/performance modeling

- Shiki spotlight/collapse ~08:57.29–09:07.20: median 100 ms mixed-track RMS **−41.48 dBFS**, q10 **−58.38 dBFS**.
- Chisato self-doubt ~10:25.91–10:30.75: median **−28.39 dBFS**.
- Mei/Shiki support ~16:44.99–18:03.53: median **−36.96 dBFS**, q10 **−51.95 dBFS**.
- Pre-performance support ~19:13.47–19:52.51: median **−34.23 dBFS**.
- Shiki-centered performance ~19:54.28–21:26.27: median **−19.06 dBFS**; about **15 dB** above the immediately preceding support block median.
- Post-performance ~21:28.97–22:00.94: median **−28.21 dBFS**.
- Treat as AM/formal evidence only; do not infer timbre or actor intention from these numbers.

---

## S3E04 voice updates — Onitsuka failure language, protective formality, and accepted-risk declaration

### Onitsuka Natsumi

#### Cumulative-failure compression

- `あれもダメ これもダメ 全部ダメ` compresses multiple discrete failures into one global pattern before the speech shifts to identity (`才能がない`) and entitlement (`夢を追う資格も…ない`).
- **Model rule:** under accumulated failure, Natsumi can move rapidly from event description to categorical self-definition.

#### Money-as-protection register

- `お金なら裏切らない` / `マニーが命` / `大切なのは夢なんかより現実。マニーですの！` uses the familiar `マニー` surface form in a specifically defensive/security context.
- Do **not** treat `マニー` as functionally identical across scenes. Here it converts uncertain aspiration into countable safety.

#### Autobiographical boundary assertion

- `やめて！` sharply interrupts Kanon before a serious first-person account: `実際 私は「Liella!」に入るまで 何一つ 夢を叶えてこられなかった`.
- The comic-commercial register drops away while Natsumi refuses supportive simplification.

#### Successor-dream directness

- `もう一度 あそこで歌いたい` -> `今度は 自分が中心になって` -> `頼られるような存在になりたい` -> `それが 今の私の夢` forms a progressively specified current-desire chain.
- This is stronger simulation evidence than a generic “Natsumi became ambitious” gloss.

#### Accepted-risk intimate declaration

- Final speech thanks Tomari directly, concedes `落ち込む時や 傷つく時` can occur, then contrasts `本当に 楽しいって思える笑顔` with money and asks `これからも 私を 見ていてほしい`.
- **Voice rule:** mature aspiration can be expressed by Natsumi without certainty language; vulnerability and future-positive declaration coexist.

### Onitsuka Tomari

#### Evidence-demanding challenge mode

- `分からない？ 何を根拠に？` directly requests grounds.
- She follows with observable evidence: Kanon's singing ability and Love Live! victory as support for a talent-based explanation.
- **Model rule:** when presented with generalized value claims, Tomari may demand causal evidence and offer a measurable alternative model.

#### Direct-system investigative language

- `直接 入部して学ぼうと判断し 行動しました` frames joining as deliberate inquiry/action rather than affective enthusiasm.
- This formal causal chain is characteristic of Tomari's self-explanatory register.

#### Protective formal intimacy

- `これまでも これからも ずっと見ていくのです。姉者のことを` and `もう… 傷ついてほしくない` preserve formal sentence structure while carrying highly personal attachment.
- Do not infer emotional distance from grammatical formality.

#### Norm-responsive apology

- `…すみません` is concise acknowledgment after others identify her wording as excessive.
- The apology changes social posture without an explicit retraction of the underlying prediction.

#### `姉者`

- Strongly attested across childhood/present sibling states; preserve as Tomari -> Natsumi address marker when relation/context supports it.

### Shibuya Kanon

#### Generative-rivalry formulation

- `お互い 足を引っ張り合うんじゃなく / 高め合って` explicitly contrasts sabotage with reciprocal improvement.
- `最高の歌` / `最高の思い出` expands the rivalry endpoint beyond rank while preserving real competition.

#### General-principle mode can be interrupted

- `夢を持っているから 自分が思っていた以上の力を出せる` is an abstract portable proposition.
- S3E04 supplies a necessary simulation limitation: such principle-language can be challenged as overgeneralized, and Kanon need not dominate the conversational resolution.

### Wien Margarete

#### Self-authored persistence mode

- `私だったら 誰がなんと言おうと諦めないわ` is a concise first-person counterfactual/resolve formulation.
- Use as evidence of stubborn dream persistence, not a generic encouragement script toward others.

#### `フン！` longitudinal audit — no new S3E04 occurrence

- Corrected Japanese SRT contains no Wien `フン` / `ふん`.
- English layers contain no `Hmph`.
- Natsumi's `ふんぬ` is excluded by speaker and function.
- **Canonical baseline remains:** S2E11 two distinct uses + S3E02 rule-trapped pride-preserving objection.

### Wakana Shiki

#### Compact metaphor/explanation mode

- `No Rain, No Rainbow.` is followed by the literal explanation `雨が降らなければ 虹は出ない` rather than an elaborate emotional speech.
- Fits Shiki's recurrent capacity for concise conceptual contribution without requiring conspicuous performative rhetoric.

### S3E04 acoustic notes for voice/formal modeling

- childhood failure/rain ~00:39–01:11: median 100 ms mixed-track RMS **−36.20 dBFS**.
- institutional/rivalry block ~03:28–05:15: median **−29.48 dBFS**.
- Tomari anti-dream challenge ~06:57–07:42: median **−34.01 dBFS**.
- failed-dream origin ~11:08–13:24: median **−36.65 dBFS**.
- Onitsuka-house argument ~13:54–16:48: median **−31.69 dBFS**.
- reflective second-year discussion ~17:08–20:39: median **−33.26 dBFS**.
- final Natsumi/Tomari declaration ~20:44–22:10: median **−31.49 dBFS**, but contains a pronounced low-energy interval with 5-second medians around **−47 to −49 dBFS** near 20:50–21:05 before progressive rise.
- ending-song surface ~22:12 onward: median **−22.33 dBFS**.
- Treat as AM/formal evidence only; do not infer timbre, instrumentation, or actor intention from these values.


---

## S3E05 voice updates — future avoidance, epistemic commitment, two Wien huffs, and Mengmeng orchestration

### Tang Keke

#### Temporally bounded dream formulation

- `可可の夢は 高校３年間を / 精いっぱい スクールアイドルとして過ごすことです` is explicit about duration as well as domain.
- **Model implication:** do not automatically write post-graduation professional-idol ambition into Keke's S3E05 voice. Her directly owned dream is the high-school period.

#### Presentist conviction

- `可可は とにかく 今を一番大事にしたい`.
- `今のために 生きてるんデス`.
- These are generalized declaratives rather than flustered evasions; present-focus is an articulated value position.

#### Unshielded uncertainty / meta-avoidance

- `正直 分かりません` provides direct uncertainty without theatrical cover.
- `ほんとに 今は スクールアイドル活動以外 考えられない`.
- `考えたくないって思ってしまうんデス` explicitly identifies her own avoidance.
- **Model rule:** Keke can recognize a defensive/avoidant process while still being unable to stop it immediately.

#### Family-evaluation anticipation

- `親に 将来のこと考えてないなんて 絶対 言えないんデス / きっと すごく がっかりする`.
- This is evidence about Keke's anticipation of parental disappointment, not direct evidence of an on-screen parental threat.

#### Chinese-language performance

- Primary Japanese subtitle track marks the performance `(中国語)` without a Chinese transcription.
- Full English ASS supplies a comparison-layer lyric translation under `HoshikuzuCruisingEnglish`.
- **Do not invent Chinese wording/phonetics** from the translation layer; safely model only the fact that Keke can sustain a solo Chinese-language performance.

### Shibuya Kanon

#### Permission-based listening

- `聞いてるよ。`
- `言える範囲でかまわないから。`
- This is a mature intimate-support construction: presence plus bounded permission rather than immediate advice or demand for full disclosure.

#### Accepted route / lagging affect

- After Wien says the Vienna study route is decided, Kanon says `頭が 全然 追いつかなくって` and that she needs to switch emotional gears.
- **Model implication:** Kanon's uncertainty language can concern adaptation to an accepted decision rather than reversal of the decision itself.

#### Fair-rivalry principle

- `確かに 私たちは 今 別のグループ` preserves the organizational fact before she invokes common Yuigaoka identity.
- `相手が困っている時に 差を広げて / それで勝っても 全然うれしくないよ` is unusually direct value language about legitimate competition.

### Onitsuka Tomari

#### Commitment parsing remains explicit

- `「ラブライブ！」出場という目的に コミットする理由は 私にはありません` separates terminal-goal endorsement from current participation.
- `休む理由もありませんので` preserves necessity/reason framing.
- `姉者の気持ちを確かめるには / 私も 本気で挑むしかないというだけです` converts serious effort into epistemic necessity rather than enthusiasm.
- **Simulation rule:** even substantial participation should remain linguistically rationalized through evidence/necessity until later text establishes genuine value-language change.

#### Emerging low-stakes teammate sociality

- Asks Wien to tell her about other countries sometime and says `楽しみにしています`.
- This provides a small anticipatory-positive mode that should not be erased by overmodeling Tomari as purely clinical.

### Wien Margarete

#### `フン！` instance 1 — competence/status face repair

- Time: ~00:02:56.45–00:02:58.38.
- Japanese: `フン！`
- English: `Hmph!`
- Context: academic comparison / face-saving after Tomari's stronger apparent performance.
- Pragmatic function: **embarrassed competence/status repair; pride-preserving face defense.**

#### `フン！` instance 2 — rivalry-ethic disagreement

- Time: ~00:10:47.15–00:10:50.56.
- Japanese: `フン！ あんたは お人よしがすぎるのよ！`
- English comparison translates the proposition but omits the `Hmph` marker.
- Pragmatic function: **skeptical dismissal and pride-preserving disagreement with Kanon's prosocial rivalry norm.**

#### Longitudinal huff rule through S3E05

- S2E11: two established functions.
- S3E02: one rule-trapped pride-preserving objection.
- S3E03: none.
- S3E04: none.
- S3E05: two explicit functions above.

**Current model:** `フン！` is a context-conditioned regulator around pride, face, reluctant concession, or sharp disagreement. It is not mandatory punctuation and must not be inserted into arbitrary Wien lines.

#### International-experience statement

- Says she has traveled to many countries since childhood.
- With Tomari, answers `ええ いいわよ` to a future request to hear more. This gives a straightforward cooperative low-stakes mode distinct from confrontation.

### Tang Mengmeng

#### Polite theatrical-host mode

- Can sustain elaborate polite phrasing while presenting herself as a guide who already knows the group and has deliberately structured their Shanghai experience.
- Her language supports a socially confident organizer/host mode rather than a shy family-introduction mode.

#### Abrupt direct plea

- At the goal reveal: `お願い。 可可ちゃんを 助けて！`
- The utterance sharply compresses the elaborate staging into a direct request.
- **Model implication:** Mengmeng's performative/polite orchestration can coexist with simple high-stakes directness once she exposes the actual ask.

#### Playful withholding

- Keke explicitly describes her as kind but somewhat prank-loving.
- Do not generalize deception as malicious; the available voice evidence supports playful/theatrical withholding whose underlying goal is not yet fully disclosed.

### Onitsuka Natsumi

#### Shanghai content-hype mode — PRESERVE

- `上海に来たからこそ「Liella!」の新しい一面を...`
- `バズりますの～！`
- Media/virality language remains available even after S3E04's accepted-risk dream disclosure.
- **Simulation implication:** growth does not delete the flamboyant optimization/content vocabulary.

### Acoustic/formal S3E05 notes

- Keke future disclosure ~03:49–05:34: median mixed-track ~**−33.51 dBFS**, p10 ~**−61.24 dBFS**; unusually sparse low-level structure among main dialogue blocks.
- cross-group solidarity ~09:44–10:54: median ~**−28.66 dBFS**.
- Keke Chinese solo ~19:34–20:16: median ~**−26.84 dBFS**.
- Treat as mixed-track AM/formal evidence only; do not infer actor intention/timbre from values.

---

## S3E06 voice updates — Keke repayment/foreclosure language, Kanon contradiction challenge, and Wien huff expansion

### Tang Keke

#### Gratitude / repayment register

- `大学に行けば お父さんもお母さんも安心する` frames education through parental reassurance rather than only self-interest.
- `両親への恩返しにもなる` introduces explicit debt/reciprocity vocabulary.
- `日本に送り出してくれた親に / 進路は もうちょっと待ってなんて 言えません` turns prior permission into a constraint Keke applies to herself.
- **Model implication:** Keke can become unusually formal/moralized about her own future when gratitude is active; do not reduce the Beijing route to external command.

#### Temporal-foreclosure register

- `可可の青春は ここまで`
- `もうすぐ終わるんです`
- `今年が 最後デスから！`

These are stronger than ordinary uncertainty. They rhetorically close the current identity epoch.

#### Decision-ownership defense

- To Sumire: `自分で決めたことデス。ほっといてクダサイ。`
- To Kanon: `もう 決めたんデス！`
- Escalation: `うるさいデス！ / かのんなら 分かってくれると思ってたのに…`.
- **Pragmatic function:** protect declared choice from relational re-opening; the directness rises because trusted people are challenging a decision Keke wants treated as settled.

#### Chinese public declaration — evidence-boundary note

The governing Japanese SRT marks the relevant post-performance speech as `(中国語)`. The English comparison translates Keke as stating continued-stage desire, school-idol transformation of her world, and asking her parents to keep watching her move forward. These meanings are usable as **translated Chinese evidence**, not as Japanese lexical/voice evidence.

#### Exact Japanese closing state

- `可可は… 今 一番幸せデスよ` preserves a familiar direct first-name self-reference + stylized `デス` while shifting `今` from defensive present-boundedness toward positive current-state ownership after future continuity has reopened.

### Shibuya Kanon

#### Direct contradiction-challenge mode

- `可可ちゃん 自分に うそついてるよ！` is substantially stronger than S3E05's permission-based listener mode.
- Kanon legitimizes the challenge by quoting/returning Keke's earlier principle: `好きなことを 頑張ることに おしまいなんてあるの？`
- `私の宝物にしている言葉` marks received language as identity-forming memory rather than disposable reassurance.
- **Simulation constraint:** use this mode only when Kanon possesses strong historical evidence; do not generalize to routine disagreement.

#### Renewed future declaration

- `私は 卒業したら ウィーンに 歌を勉強しに行く。`
- Simple first-person future form; no elaborate justification in the line itself.
- Pragmatic function in context: expose her own chosen future before urging Keke not to foreclose hers.

#### Structural-action register

- `私 やる。`
- `可可ちゃんが 一番 祝福される状況を 私が作る。`
- `やろう！ 私たちに 今できること！`
- When conceptual clarity turns into leadership, Kanon can compress into short action declarations and immediately recruit collaborators.

### Heanna Sumire

#### Ownership-respecting direct desire

- `ま 可可がいいならいいけど` acknowledges Keke's authority condition.
- Then emphatic self-positioning: `私は見たいわ！ / 可可が ステージに立ち続ける姿を！`
- **Voice rule:** Sumire can support through strong first-person desire rather than softened reassurance; bluntness and respect for choice are compatible.

### Wien Margarete

#### S3E06 speaker-clear `フンッ` #1 — reluctant-investment rationalization

- Time: ~13:46.495.
- Japanese: `帰りますか？ フンッ それこそ…。`
- English comparison: `Hmph. If I did…`
- Followed by `上海まで来た意味 ないじゃない！`
- Pragmatic function: pride-preserving rationalization when withdrawal would expose how invested she already is.

#### S3E06 speaker-clear `フンッ` #2 — caught-in-inconsistency face seal

- Time: ~13:55.201.
- Tomari: `「『Liella!』は敵」では？`
- Wien: `フンッ。`
- English comparison: `Hmph.`
- Pragmatic function: refuses to verbally reconcile `enemy` rhetoric with support behavior after being directly caught in the contradiction.

#### High-confidence attributed candidate ~04:00 — not in strict count

- Japanese SRT cue: `だから 敵じゃないって！ もう！ フンッ。`
- English separates `Like I said, they're not our enemy!` from `Hmph!`.
- Turn-taking strongly favors Wien for the final marker, but the Japanese SRT does not speaker-label/split the cue.
- **Taxonomy:** retain as high-confidence turn-attributed candidate; do not give it equal status with speaker-clear cases.

#### Strict longitudinal huff rule through S3E06

- S2E11: **2** speaker-established instances.
- S3E02: **1** speaker-established instance.
- S3E03: **0**.
- S3E04: **0**.
- S3E05: **2** speaker-established instances.
- S3E06: **2** new speaker-clear instances + **1** high-confidence attributed candidate.
- **Strict definitive total: 7.**

The function set now includes grudging engagement, defensive dismissal, rule-trapped objection, status repair, skeptical disagreement, reluctant-investment rationalization, and caught-in-inconsistency face sealing. The marker remains context-conditioned pride/face regulation, not mandatory punctuation.

### Onitsuka Tomari

- `私の目的は 変わりません` is concise goal-continuity language.
- `姉者の発言が本気かどうか それを この目で確認したいだけです` keeps the first-person verification register intact.
- No new lexical concession equivalent to `価値がある` appears.
- **Model implication:** cooperative action should not be simulated as warmer/value-converted speech unless later evidence supplies it.

### Tang Mengmeng

- `両親に見てもらいたいからです` presents the intervention in simple causal language after the elaborate S3E05 logistics.
- `可可ちゃんは これからも 歌の道を突き進むのです` is confident future assertion on Keke's behalf.
- **Voice/agency caution:** supportive content and declarative certainty coexist; Mengmeng may speak as if the desired creative route is already decided even when Keke has not publicly finalized it.

### Arashi Chisato

- `今日だけ 特別！` explicitly marks exception design.
- `かのんちゃんと一緒に ライブしない？` invites rather than commands.
- Final escalation: `最高の瞬間を！ / 結ヶ丘のスクールアイドル全員で！`
- **Voice rule:** Chisato can turn a practical exception into high-order group framing while keeping the invitation relational and context-specific.

### S3E06 acoustic-form note

100 ms mixed-track medians:
- Mengmeng explanation: **−26.16 dBFS**.
- Keke origin/discovery: **−35.29 dBFS**.
- Kanon–Keke tea/future disclosure: **−30.52 dBFS**.
- Keke parent-college declaration: **−33.46 dBFS**.
- Sumire–Keke exchange: **−35.78 dBFS**.
- Kanon–Keke confrontation: **−32.42 dBFS**.
- TomaKanoTe crowd-call: **−22.62 dBFS**.
- joint pre-song address: **−20.33 dBFS**.
- joint performance: **−18.99 dBFS**.
- Keke public family declaration: **−28.45 dBFS**.
- final happiness/thanks: **−31.93 dBFS**.

Formal sequence only: private/paired future talk -> public intervention -> high-energy collective performance -> quieter direct family/future address. Do not infer timbre or actor intention from these values.


---

## S3E07 voice updates -- rival-boundary huffs, private-interest breakthrough, and communication language

### Wien Margarete

#### S3E07 definitive `フン！` #1 -- rival-distance restoration after Shanghai

- **Time:** ~01:15.
- **Japanese:** explicitly speaker-labeled `（マルガレーテ）フン！`, followed by `なれなれしくしないで！`.
- **English comparison:** isolated `Hmph!`.
- **Function:** anti-chumminess boundary restoration after the Shanghai joint live; pride-protective reassertion of rival distance.

#### S3E07 definitive `フン！` #2 -- pride-sealed acknowledgment of being accurately known

- **Time:** ~11:40.
- **Context:** Wien begins to state her purpose; Kanon accurately completes it as defeating Liella! and winning Love Live!.
- **Japanese:** isolated `フン！`.
- **English comparison:** isolated `Hmph!`.
- **Function:** acknowledgment without explicit warm confirmation; being accurately known is accepted under pride cover.

#### S3E07 definitive `フン！` #3 -- reluctant intimacy concession

- **Time:** ~12:19.
- **Japanese:** `フン！ 別にいいけど！`
- **English comparison:** isolated `Hmph.` followed by acceptance.
- **Function:** accepts Kanon's three-person sleepover/talk while protecting against the appearance of eager intimacy.

#### S3E07 definitive `フン！` #4 -- competitive-memory face regulation

- **Time:** ~18:08.
- **Context:** Kanon recalls their prior Tokyo competition and Liella! advancing.
- **Japanese:** `フン！` followed by a brief laugh-like textual marker.
- **English comparison:** isolated `Hmph.`.
- **Function:** pride-regulated response to a shared history containing competitive loss.

#### Strict longitudinal huff rule through S3E07

- S2E11: **2** definitive.
- S3E02: **1** definitive.
- S3E03: **0**.
- S3E04: **0**.
- S3E05: **2** definitive.
- S3E06: **2** definitive + **1** separately retained high-confidence attributed candidate.
- S3E07: **4** definitive.
- **Strict definitive total: 11**, plus the one separately tracked S3E06 candidate.

The function set now includes grudging engagement, defensive dismissal, rule-trapped objection, status repair, skeptical disagreement, reluctant-investment rationalization, inconsistency face sealing, rival-distance restoration after closeness, reluctant intimacy acceptance, acknowledgment of being accurately known, and regulation around remembered competitive loss. The marker remains **context-conditioned pride/face regulation**, never mandatory sentence punctuation.

### Onitsuka Tomari

#### Formal refusal / single-purpose mode

- `アグリーしかねます。`
- `その一点のみ。`
- `今 なれ合って ひとつになることを 私はベストだとは思いません。`
- Model implication: formal analytic grammar remains available even in emotionally loaded sibling/group questions.

#### Private-interest affective breakthrough

- Sweets: `大好きです。` immediately paired with physique-maintenance self-regulation.
- Jellyfish: after a minimizing comment, strongly counters `そんなことはありません！` and describes them as uniquely cute/soothing; says she watches them every night before sleep.
- Missing volume: rapid `７巻がない！` and immediate bookstore solution.
- **Voice rule:** do not simulate Tomari as uniformly flat/formal. Low-threat person-specific interests can unlock emphatic, fast, openly affective language.

#### Relational softening without register collapse

- Kanon says knowing Tomari herself is important and wants to know her better; Tomari's compact `先輩…` marks reception without requiring a full warmth conversion.
- Final full-force agreement returns to characteristic concise `アグリーです。`

### Shibuya Kanon

#### Person-knowledge mode

- Explicitly distinguishes sleepover communication from a merger pitch: `違うよ。`
- `二人のこと もっと知りたくなって。`
- When Tomari tries to dismiss her own personal material as irrelevant, Kanon answers `そんなことないよ。 すっごく大事！`.
- **Voice rule:** team-governance speech can move from functional rationale into explicit curiosity about the person, not just their utility to performance.

#### Motive-synthesis mode

- `今こそ 二人の気持ちを / 解放させる時が 来たんだよ。`
- `今こそ 私たち３人で / 全力で Liella!にぶつかろう！`
- Conceptual language remains direct, but the synthesis preserves different motives rather than forcing one interpretation.

### Arashi Chisato

- `今は 急がず焦らず` and `あの二人の気持ちも 大事にしていこ？` preserve patient governance language after the eleven-person wish appears.
- This is useful counterevidence against a voice model that makes post-S3E06 Chisato automatically push immediate integration.

### S3E07 acoustic-form note

100 ms mixed-track medians:

| Block | Median dBFS | Formal use |
|---|---:|---|
| Wien opening introspection ~00:42-00:49 | -48.31 | notably sparse/quiet opening block |
| greeting + huff + rival vow ~01:10-01:30 | -33.21 | return to social/competitive scene |
| Love Live announcement + selection setup ~03:02-05:40 | -25.56 | denser institutional announcement block |
| Liella! invitation/refusal ~07:42-10:03 | -27.81 | sustained group negotiation |
| Kanon/Wien goal + sleepover invite ~11:26-12:23 | -33.12 | lower-density personal negotiation |
| sleepover communication ~13:01-17:04 | -29.66 | extended domestic dialogue |
| night walk / resolve ~17:35-21:59 | -33.38 | lower-density decision block with a transition near silence |
| ending song ~22:16-23:28 | -18.97 | much denser/louder mixed-track endpoint |

Huff-centered micro-window medians are approximately -38.96, -47.30, -40.61, and -36.59 dBFS for the four S3E07 markers respectively. These measurements support formal density/segmentation claims only; do not infer actor emotion, timbre, or intention from RMS values.


---

## S3E08 voice updates — unrestricted sibling attachment, successor disagreement, and recognition-exposed pride

### Onitsuka Natsumi

#### Joint-ownership argument mode

- `ここに この４人が集められたのは / どちらのグループも 納得できる曲にするため。`
- `お互いに 話し合った方がいいのでは？`
- Speech is process-oriented rather than simply emotive: Natsumi can argue that collaboration provenance is part of output validity.

#### Unrestricted sibling-attachment declaration

- `私は冬毬と話がしたい。`
- `全部受け止めるから 心を開いてほしい…！`
- `私に何でも話して！`
- `スクールアイドルと 全然関係ない話だって かまわない！`
- `ずっと冬毬と話がしたい…！`
- `冬毬のことが 大好きなんだから…。`

**Voice rule:** when the sibling relationship itself becomes the issue, Natsumi can drop producer/commercial framing and become unusually repetitive, scope-expanding and emotionally direct. The repeated `ずっと` and `何でも` broaden the request beyond the immediate school-idol dispute.

#### Commercial-product register persists

- `そう言われるのは 織り込み済み。`
- immediately follows with product/nutritional explanation.
- Keep this as an available competent promotional mode; S3E08 context is norm-compatible and does not justify caricaturing every ordinary interaction as marketing.

### Onitsuka Tomari

#### Procedural optimization mode

- `それぞれが 歌詞と曲を持ち寄って`
- proposes leader selection for `公平` and `クオリティー`.
- `必要ないと思います。`
- `アグリーできません。`

This is characteristic Tomari: formal efficiency language can be a real substantive preference, not only a defense.

#### Attachment-breakthrough mode

- `姉者はいつも ずるいです…！`
- `私が どれだけ姉者を… 心配してきたと思ってるんですかぁ…！`

The key shift is not loss of intelligence/formality as a trait. It is a state in which the relational stake finally outruns the controlled explanatory register.

#### Ordinary preference correction

- `姉者… 私は 甘い飲み物が好きなのです。`
- Useful low-stakes evidence that Tomari can correct Natsumi plainly even after major reconciliation; intimacy does not imply presumed mind-reading.

### Wien Margarete

#### Aesthetic challenge mode

- `せっかく 新たに曲を作るんだから / 今までにないようなものにしたい！`
- Innovation demand is direct and self-confident; conflict with Mei is about artistic criteria rather than generalized hostility.

#### Pre-performance competitive directness

- `勝つ。`
- Remains maximally concise before the equal-condition contest.

#### Recognition-exposed response

- after Liella! recognizes TomaKanoTe's performance: text records visible/emotional exposure and compact `うるさい！` when Tomari says it is acceptable to cry.
- Model as pride-protective reaction under received recognition, not as rejection of the recognition itself.

#### S3E08 definitive `フン！` — embarrassed emotional-concealment / face sealing

- **Time:** ~14:15-14:17.
- **Context:** after the Natsumi/Tomari breakdown, Mei is teased for crying and points out Wien is also crying.
- **Japanese:** isolated `フン！`.
- **English comparison:** isolated `Hmph!` at ~14:16.75-14:17.09.
- **Function:** embarrassed emotional-concealment / face sealing after being socially identified as affected.
- **Exclusion:** Natsumi's later festival `フッフーン！` is a different speaker/function and is not part of Wien's taxonomy.

#### Strict longitudinal huff rule through S3E08

- S2E11: **2** definitive.
- S3E02: **1** definitive.
- S3E03: **0**.
- S3E04: **0**.
- S3E05: **2** definitive.
- S3E06: **2** definitive + **1** separately retained high-confidence attributed candidate.
- S3E07: **4** definitive.
- S3E08: **1** definitive.
- **Strict definitive total: 12**, plus the one separately tracked S3E06 candidate.

The function set now additionally includes embarrassed emotional-concealment after attachment-related social exposure. The marker remains context-conditioned pride/face regulation, not mandatory punctuation.

### Yoneme Mei

#### Domain-value aesthetic objection

- `これは スクールアイドル向きじゃない気がする。`
- `曲にも ちゃんと スクールアイドルへの愛が あふれていないと！`

Do not reduce this to “Mei hates rock/novelty.” She states a criterion about the representational purpose of a Love Live! song.

#### Succession-responsibility mode

- `先輩に頼るわけにはいかないし…`
- Directly encodes task ownership as generational responsibility rather than merely stubbornness.

### Wakana Shiki

#### Relational-mechanism compression

- `大好きだから 見たくない。`
- `傷つくところも 悲しむところも…。`

Shiki continues to produce sparse high-information formulations. In simulation, her low word count should not be mistaken for low inferential involvement.

### Eleven-member collective declaration

- `私たち 結ヶ丘女子高等学校スクールアイドル！`
- `「Liella!」です！`

This is organizationally performative speech: the utterance does not merely describe a pre-existing condition; at the episode boundary it publicly confirms the newly integrated current unit.

### S3E08 acoustic-form note

100 ms mixed-track medians:

| Block | Median dBFS |
|---|---:|
| opening / contest setup | -25.80 |
| composition conflict | -27.14 |
| Onitsuka repair | -29.17 |
| festival build | -22.97 |
| shared-song contest | -18.83 |
| result / eleven-member resolution | -25.13 |
| ending | -19.31 |

The Onitsuka block contains several especially low five-second medians, including approximately **-55.97 dBFS** around 12:45-12:50 and **-48.26 dBFS** around 11:15-11:20. Use only as evidence of formal sparse/low-energy hinges, not actor emotion or timbre.
