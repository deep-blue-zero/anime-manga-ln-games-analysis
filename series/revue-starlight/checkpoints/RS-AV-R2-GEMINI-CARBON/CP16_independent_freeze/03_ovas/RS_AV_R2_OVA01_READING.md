---
title: "RS-AV-R2-GEMINI-CARBON — OVA01 Independent Reading: 『#1 99.419 Measuring (採寸)』"
generation: "RS-AV-R2-GEMINI-CARBON"
artifact_type: "deep_reading"
status: draft_noncurrent
supersedes: []
superseded_by: []
do_not_use_as_current_authority: true
project: "series/revue-starlight"
execution_identity: "RS-AV-R2-GEMINI-CARBON"
source_unit: "OVA01"
episode_title_jp: "#1 99.419 採寸 (Measuring)"
episode_subtitle_en: "99.419 Measuring"
model: "Gemini 4 Carbon (High reasoning)"
corpus_exposure: false
prospective_horizon: "OVA01"
primary_video_witness: "urn:rs-av-r2:primary-media:ep01.analysis-softsub.mkv"
primary_video_sha256: "14bcfd93131d1cfeea41b52c3370ca877e48cfbe69e4fae8434f1e7d48d8c6c1"
duration_seconds: 419.42
japanese_text_witness: "NONE (0% Japanese subtitle tracks in local/upstream MKVs; all Japanese speech and song transcribed strictly by ear from 0:a:0 48 kHz lossless stereo FLAC + 1920x1080 onscreen Japanese signage)"
inspection_modes:
  - "Pass 1: 100% continuous synchronized unburned audiovisual inspection via 2 overlapping 720p H.264/AAC segments (00:00.000–03:45.000 and 03:35.000–06:59.420; -map 0:v:0 -map 0:a:0 -sn; 1.000 fps native visual sampling + continuous Japanese stereo audio)"
  - "Pass 2: Targeted 1920x1080 unburned PNG inspection (13 lossless stills: ova01_0009.5, 0042.0, 0046.5, 0055.5, 0080.5, 0095.5, 0175.5, 0220.5, 0337.5, 0393.0, 0403.0, 0407.5, 0411.0) + 256 kbps AAC audio-only verification from stream 0:a:0 (48 kHz lossless FLAC) + 838-bin 0.5s RMS acoustic envelope"
---

# `OVA01` — 『#1 99.419 Measuring (採寸)』: Independent Audiovisual Reading

## 0. Horizon, Witness Declaration, & Japanese-Only Audio Protocol

This reading records the first OVA horizon (`TV01`–`TV12` + `OVA01`) of run `RS-AV-R2-GEMINI-CARBON`, executed **strictly after** locking `CP13_TV_SYNTHESIS_FREEZE` (`c0e0559c72ab13f7ce87b3d381d4b4fcf1150e91`) and **prior to** inspecting `OVA02`, `OVA03`, the 2021 theatrical sequel film (`MOVIE`), or any existing repository analysis in `series/revue-starlight/`.

> [!IMPORTANT]
> **Strict Zero-English-Subtitle Protocol**: As verified during `CP00` (`RS_AV_R2_SOURCE_AND_EXECUTION_INVENTORY.md`), `ep01.analysis-softsub.mkv` (`urn:rs-av-r2:source:ep01.analysis-softsub.mkv`) (`150,123,066` bytes, `419.420s`) contains **no Japanese subtitle stream** (track `#0:2` is an English `[Ripple]` fan localization). All segments and stills were extracted with `-map 0:v:0 -map 0:a:0 -sn`, completely excluding the English subtitle stream from visual and textual context. Every spoken line and sung lyric below is transcribed directly by ear from primary stream `0:a:0` (`48 kHz` lossless Japanese `FLAC`) alongside `1920x1080` onscreen Japanese text; any phonetically rapid or low-volume syllable not verifiable at 100% certainty is marked `[聴取不確定]`.

---

## 1. Chronological Placement, Title Architecture, & Retrospective Revision to `TV12` (`[REV-OVA01-01]`)

### 1.1 Mid-January 2019 Setting & Calendar Correction for the `100th` Seishō Festival (`[REV-OVA01-01]`)

Written by **Higuchi Tatsuto (`脚本：樋口達人`)**, storyboarded and directed by **Hashimoto Hiroyuki (`絵コンテ・演出：橋本裕之`)** under Series Director **Furukawa Tomohiro (`監督：古川知宏`)**, with animation direction and costume-design cooperation by **Itō Masako (`作画監督・衣装デザイン協力：伊藤雅子`, `ova01_0407.5`)**, `OVA01` looks at first glance like a light Blu-ray bonus short. Direct `1920x1080` inspection of three diegetic documents inside the episode, however, yields a **decisive chronological revision (`[REV-OVA01-01]`)** to our `TV12` / `CP13` reading:

1. **Corridor Countdown & Nine-Lead `100th` Festival Poster (`00:09.5`, `ova01_0009.5` & `06:33.0`, `ova01_0393.0`)**: Outside the classroom, a hand-lettered countdown sign reads **`聖翔祭まで 50日`** ("**50 Days Until the Seishō Festival**") directly beside the official purple poster for **`第100回 聖翔祭 / STAR LIGHT 100th`**. That poster already carries the **post-`TV12` nine-actress billing** seen in `TV12` `22:00`–`23:16`:
   - Top-billed dual leads: **`KAREN AIJO / HIKARI KAGURA`**
   - Ensemble billing below: **`MAYA TENDO / JUNNA HOSHIMI / MAHIRU TSUYUZAKI / NANA DAIBA`** and **`CLAUDINE SAIJO / FUTABA ISURUGI / KAORUKO HANAYAGI`**
   - Tagline: **`お持ちなさい あなたの望んだ[その星を] / And it shall be bestowed upon you, the Star which you [have longed for]`**
2. **Class B Costume-Room Whiteboard (`01:20.5`, `ova01_0080.5`)**: Inside `衣装部屋(仮)` (`00:46.5`, `ova01_0046.5`), Class B's whiteboard is headed **`聖翔祭 2019 採寸 / 舞台創造科`** ("**Seishō Festival 2019 Measurements — Stage Creation Department**"). In the right margin sits a circled **`OK`** scheduling memo:
   - **`◎ 愛城さんと神楽さん 採寸時間変更 [OK]`** ("**Aijō-san and Kagura-san: measurement time changed — OK**") — concrete institutional evidence of the late lead/schedule adjustment triggered after Hikari's late-December 2018 return (`TV12` `21:43`)!
   - Additional production notes on the board: **`西條クロディーヌ → 着丈変更 ◎ 3cm長く`** ("Saijō Claudine → garment length change: +3 cm longer" — Claudine is still growing in early 2019!), `採寸の注意` (`・袖丈(肩〜手首) ← 裄丈も忘れずに！`, `・アームホール ← 去年より追加`), `スカートの場合 ウエスト2ヵ所必要です {身体のウエスト / 服のウエスト} → 了解！！ (は)`, `前回の会議より ・生地屋さんに電話しました(例の生地有り) ・ビーズは日暮里に種類豊富なお店有り` (a real-world Tokyo **Nippori Fabric Town** reference!), `レースの縫製ムズかしいよ… ↑頑張って！！`, a pink sticky note `[大]場なな [採]寸`, an ensemble sword/costume sketch, and—pinned in the upper-right corner—Nikolai Punin's Constructivist poster of **Tatlin's Monument to the Third International (`ПАМЯТНИК III ИНТЕРНАЦИОНАЛА` / `Н. ПУНИН`)**, visually rhyming with the spiraling iron lattice of the *Starlight* Tower!
3. **Claire Costume Tag (`01:35.5`, `ova01_0095.5`)**: Hanging on Class B's rack alongside the pink-and-yellow striped Goddess skirts (`ova01_0055.5`) is the royal-blue cloak bearing a printed tag:
   - **`#100 聖翔祭 | Character: クレール | Actor: 神楽ひかり | Scenes: 7, 9 ~ 10, 12`**

**Chronological Consequence (`[REV-OVA01-01]`)**: In `TV12` (`CP12`/`CP13`), the unmarked ellipsis between Room `203`'s late-December 2018 hotpot reunion (`TV12` `21:43`) and the curtain rise of `STAR LIGHT 100th` (`TV12` `22:00`) led us to place the `100th` Seishō Festival provisionally in late December 2018. `OVA01` proves instead that **`第100回 聖翔祭` takes place in `2019` (`聖翔祭 2019`)**, preserving the exact **early-March annual calendar** established for the `99th` Festival in `TV07` (`2018.3.3`). Counting **`50 days` backward** from early March 2019 situates `OVA01` in **mid-January 2019** (bare winter branches in the courtyard `ova01_0220.5`; winter cardigans; freezing measuring tape), squarely inside the **~2.5-month rehearsal and costume-building window** between Hikari's December 2018 return (`TV12` `21:43`) and the March 2019 `100th` Festival (`TV12` `22:00`–`23:48`). Even the minor costume detail at `01:29`–`01:33`—where two Class B costumers ask **`大場さんってフードありだっけ？`** / **`うん、ありのはず`** ("Does Daiba-san's costume have a hood?" / "Yeah, it's supposed to") whereas by performance day in `TV12` `22:02` the seven Goddesses wear **unhooded golden `V`-circlets**—captures a living production still revising its `100th` edition costumes fifty days before opening!

### 1.2 Metatextual Title Code: `#1 / 99.419 Measuring` (`ova01_0042.0`)

At `00:42.0`, the minimalist white title card prints **`#1 / 99.419 Measuring`** beneath the *Revue Starlight* emblem. Cross-checking against `ffprobe` container metadata (`duration = 419.420000s` = `06:59.420`) reveals an exact formal pun: **`99` (`99th` Class) + `.419` (`419` seconds exact runtime)**!
- *Prospective Hypothesis for `OVA02` & `OVA03`*: Since `OVA02` has verified container duration **`428.430s`** and `OVA03` has **`433.435s`** (`CP00`), we predict prior to opening them that their title cards will read **`#2 / 99.428 [...]`** and **`#3 / 99.433 [...]`**.

---

## 2. Scene-by-Scene Audiovisual & Acoustic Reconstruction (Method §4.A, §4.D, §4.E)

| Window | RMS Envelope (`0.5s` bins) | Dramatic & Visual Action | Verified Japanese Audio Witness (`0:a:0` Lossless FLAC) |
| :--- | :--- | :--- | :--- |
| **`00:00`–`00:46`** | `-35` to `-25.4 dBFS` (Mahiru shriek `00:14`) | Quiet winter campus establishing shots (`00:00`–`00:13`: leafless trees, `聖翔祭まで 50日` + `STAR LIGHT 100th` poster `ova01_0009.5`) shattered by Mahiru's shriek inside `衣装部屋(仮)`; Nana comforts her; Futaba & Hikari arrive together (`00:32`–`00:40`); title card `#1 / 99.419 Measuring` (`00:42.0`). | Mahiru: **`きゃあっ！ …メ、メジャーが冷たくて、びっくりしちゃった…`** (`00:14`–`00:24`) / Nana: **`びっくりした〜。…終わったらホットバナナミルク入れてあげる`** (`00:20`–`00:29`) / Futaba & Hikari: **`失礼しまーす！ 出席番号2番、石動双葉。…出席番号29番、神楽ひかり。採寸お願いします`** (`00:31`–`00:40`, matching the verified student numbers from `TV01`/`TV10`!). |
| **`00:47`–`01:47`** | `-31` to `-25.8 dBFS` | Bustling Class B workshop (`ova01_0055.5`): Stage Creation students in white T-shirts and waist-tied burgundy tracksuits measure Nana's bare foot, Futaba's upper arm, Claire's cloak (`ova01_0095.5`), and Mahiru's height (`162 cm`). | Nana: **`だって足くすぐったーい！`** (`00:58`) / Futaba: **`なんで採寸の時って半分裸なんだよー`** (`01:06`) → Mahiru: **`双葉ちゃん、去年と同じこと言ってる`** (`01:14`) / Class B: **`腕付け根周り、23センチ`** (`01:24`); **`大場さんってフードありだっけ？ / うん、ありのはず`** (`01:29`–`01:33`); **`サイズどうする？ Mだっけ？ / ちょっとタイトな方が良くない？ / そうだね、それで調整しよう`** (`01:35`–`01:41`); **`露崎さん、身長162センチでーす`** (`01:44`). |
| **`01:48`–`03:36`** | Peaks `-24.5 dBFS` (`02:59`) & **`-23.73 dBFS`** (`03:27.0`) | Futaba's comic **`舞台少女格差`** ("Stage Girl disparity") lament: first over height (`あと5センチ` so she isn't typecast into child/boy roles), then gawking at Mahiru's bust adjustment (`サイズ一つ上げないと… 二つでもいいくらい`, `ova01_0175.5`), ending in Futaba & Nana playfully dogpiling Mahiru (`03:25`–`03:34`). Meanwhile Hikari pauses thoughtfully (`02:27`, `03:13`). | Futaba: **`これが舞台少女格差か… あと5センチ… いや、贅沢言わねえ、3センチでいいから背が伸びてくれりゃあな〜！ この身長のせいで子供とか男の子役ばっかだし…`** (`01:49`–`02:15`) / Nana: **`私も夏の公演はバナナの木の役だったよ`** (`02:17` — comic sight-gag memory of Nana in a banana-tree suit!) → Futaba: **`だから上から見下ろすなって！`** (`02:22`) / Mahiru & Nana reassure her (`双葉ちゃんには双葉ちゃんにしかできない役があるってことだよ！` / `ちっちゃくて元気いっぱいなのも双葉ちゃんの魅力だよ`, `02:29`–`02:37`) / Futaba & Nana: **`まひるー、あたしにも分けてくれー！ / 私も分けてー！`** (`03:25`–`03:30`). |
| **`03:37`–`03:46`** | `-34` to `-28.2 dBFS` (bat *whoosh* `03:45.5`) | **Abrupt Courtyard Cutaway (`ova01_0220.5`)**: Outside before the armless *Venus de Milo* statue and bare winter trees, **Karen** (crown hairpin intact, winter cardigan) practices three intense wooden baseball-bat swings! The third swing's *whoosh* match-cuts directly into Hikari's snapping eyes (`03:47.0`). | Karen: **`ふっ！ …ふっ！ …ふっ！`** (`03:40`–`03:45`, crisp bat-swing air cuts). *(No explanation is given inside `OVA01`—held as an active simultaneity hook for `OVA02`/`OVA03`!)* |
| **`03:47`–`05:34`** | **Episode Peak `-20.98 dBFS`** (`229.0s` = `03:49.0`) | **Hikari's Delayed Theater-Nerd Outburst**: Hikari blurts **`クリスティン・マカードル！`** at maximum episode amplitude (`-20.98 dBFS`), linking small stature to the original star of the musical ***Ally* (`アリー`)**—which Futaba recalls was Claudine's child-actor musical (`TV10` `07:33.5`)! Mahiru, Nana, & Futaba sing a 10-second unison snatch of *Ally*, after which Hikari unleashes an uninterrupted **`46-second` rapid-fire monologue (`04:20`–`05:06`)** over nimble pizzicato strings before realizing the height topic already ended two minutes ago! | Hikari: **`クリスティン・マカードル！ …アリーの初演の主役`** (`03:49`–`03:55`) / Futaba: **`ああ、クロ子が子役の頃に出てたミュージカルか`** (`03:58`) / Mahiru, Nana, Futaba (singing): **`♪友よ 友よ みんなが友達 何でもありだよ〜`** (`04:04`–`04:14`) / Hikari: **`彼女も背が低くて子どもの役ばかりだった。大人になれば背が伸びて大人の役ができると思ってたけど、大人になっても背は伸びなかった。…でも彼女は諦めなかった。小さい体に秘めた大きな情熱で歌やダンスや演技を磨いて、大人になっても子どもの役を演じ続けた。そうしていつしか、小さいことは誰にも負けない彼女の武器になり、大きくキラめく小さな宝石、ビッグママ、グランド・クリスと呼ばれる大女優になったの。……以上`** (`04:20`–`05:07`) / Mahiru: **`ひかりちゃんがこんなに喋るの初めて聞いたかも… 怒涛のひかりちゃんだったわ`** (`05:10`–`05:15`) / Futaba: **`それってさっきまひるとナナが言ってくれたことだよな？ / そう / その話もう終わってるよー！`** (`05:23`–`05:31`). |
| **`05:35`–`06:59`** | `-32` to `-25.1 dBFS` (`ばなナイス！` `06:50`) | **Warm Resolution & First-Name Shift (`ova01_0337.5`, `0393.0`, `0403.0`)**: Touched that shy Hikari searched her memory to encourage her in her own words, Futaba pats Hikari's shoulder and shifts from `神楽` to bare **`ひかり`**. Hikari deadpans refusal (`それは嫌`), freezes the room, then flashes an ECU smirk (`ova01_0403.0`)—**`冗談`**—before gentle piano/woodwind chamber music closes over the `衣装部屋(仮)` door and scrolling white-on-black credits (`06:47`–`06:59`). | Futaba: **`ありがとな、神楽。…あたし、これからは神楽じゃなくて、ひかりって呼ぶ！ あたしのことは双葉でいいからな、ひかり！`** (`05:36`, `06:26`–`06:34`) / Hikari: **`それは嫌`** (`06:36`) → Futaba: **`えっ！？ なんでだよー！？`** (`06:38`) → Hikari (blushing smirk `ova01_0403.0`): **`…冗談。…冗談`** (`06:43`, `06:48`) / Mahiru: **`ひかりちゃんが冗談！？`** / Nana: **`ばなナイス！`** (`06:49`–`06:51`). |

---

## 3. Character, Register, & Everyday-vs.-Comic Baseline Calibration (Method §4.B, §4.C)

1. **Post-`TV12` Hikari's Everyday Personality (Freed from Secret Guilt)**: Throughout `TV01`–`TV12`, Hikari's laconic reserve was heavily overdetermined by secret trauma (`TV08` London collapse) and solitary atonement (`TV11`–`TV12`). Set in mid-January 2019 *after* Karen brings her back from the desert (`TV12` `21:38`), `OVA01` reveals what Hikari is actually like in ordinary school life when nobody's `キラめき` is being fuel-burned:
   - **Socially Delayed Timing (`マイペース`)**: She spends nearly ninety seconds (`02:15`–`03:47`) silently indexing stage history in her head while her classmates have already moved on to Mahiru's bust measurements, then blurts the answer (`クリスティン・マカードル！`) as if zero time had elapsed.
   - **Encyclopedic Theater Nerdiness**: Just as London's West End shaped her training (`TV08`), she has memorized the biography and nicknames (`大きくキラめく小さな宝石`, `ビッグママ`, `グランド・クリス`) of original *Ally* lead Christine McArdle, closing her 46-second breathless recital with a formal schoolgirl **`……以上`** (`05:07`).
   - **Dry Deadpan Humor (`冗談`)**: Her stone-faced **`それは嫌`** (`06:36`) followed seven seconds later by a tiny sideways smile and **`冗談`** (`06:43` `ova01_0403.0`) proves her stoic exterior now houses affectionate teasing rather than defensive isolation.
2. **Genuine Cross-Dyad Address-Register Shift (`Futaba ↔ Hikari`)**: Prior to `OVA01`, Futaba addressed Hikari by surname (`神楽`) and Hikari barely interacted one-on-one with Futaba outside `TV01`'s stairwell encounter. At `06:26`–`06:34`, Futaba explicitly negotiates mutual bare given names (**`神楽じゃなくて、ひかりって呼ぶ！ あたしのことは双葉でいいからな、ひかり`**), expanding Hikari's post-`TV12` social integration beyond Karen, Mahiru (`TV05`), and Nana (`TV07`/`TV12`). Meanwhile, Nana's habitual caretaker reflex (`ホットバナナミルク入れてあげる`, `00:27`) and spontaneous **`ばなナイス！`** (`06:50`) operate purely in benign everyday register, free of `TV07`'s temporal anxiety.
3. **Intertextual Continuity with `TV10` (`ミュージカル「アリー」`)**: `OVA01` (`03:54`–`04:14`) organically enriches `TV10` (`07:33.5`), where young Claudine starred in `ミュージカル「アリー」`. We now hear ten seconds of *Ally*'s actual diegetic melody (`♪友よ 友よ みんなが友達 何でもありだよ〜`)—known by heart to Mahiru, Nana, and Futaba as standard Seishō musical canon—and learn that its premiere protagonist, Christine McArdle, turned diminutive height into iconic stage presence.
4. **Stage Creation Department (`B組`) Material Craftsmanship**: Named in the credits (`B組クラスメイト：真野あゆみ、大前愛華、杉本優羽、園山ひかり`, `ova01_0407.5`), Class B is depicted not as background extras but as disciplined theatrical artisans tracking armhole additions (`去年より追加`), two-point skirt waists (`身体のウエスト / 服のウエスト`), Nippori bead sourcing, and Claire's exact four-scene cloak plot (`Scenes: 7, 9 ~ 10, 12`, `ova01_0095.5`).
5. **Explicit Anti-Overreading Guardrail (Comic Gag vs. Structural Evidence)**:
   - *Do NOT over-interpret*: Futaba and Nana's slapstick dogpile over Mahiru's bust size (`舞台少女格差`, `02:38`–`03:34`), Nana's cutaway sight gag in a banana-tree costume (`夏の公演はバナナの木の役`, `02:17`), or Hikari's two-minute conversational lag are light comedic exaggeration—not psychological regression or ensemble resentment.
   - *DO retain as structural corpus facts*: (a) the **mid-January 2019 (`50 days` pre-March `聖翔祭 2019`)** chronological anchor (`[REV-OVA01-01]`), (b) Claire's `100th` Festival cloak scene index (`Scenes: 7, 9 ~ 10, 12`), (c) the **`Futaba ↔ Hikari`** mutual given-name shift, and (d) the unexplained **courtyard cutaway of Karen swinging a baseball bat (`03:37`–`03:45`)**, held open to test whether `OVA02` and `OVA03` form a simultaneous multi-perspective triptych on the same January afternoon!
