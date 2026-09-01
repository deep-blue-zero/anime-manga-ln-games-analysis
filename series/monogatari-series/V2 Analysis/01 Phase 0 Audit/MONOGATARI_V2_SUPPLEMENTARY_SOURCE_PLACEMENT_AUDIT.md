---
series: MONOGATARI
artifact_type: source_audit
scope: SUPPLEMENTARY_CORPUS_PLACEMENT
generation: V2
status: canonical
source_boundary: 'Three locked supplementary EPUBs only: 短物語; 佰物語オリジナルドラマCD シナリオブック; 化物語 アニメコンプリートガイドブック'
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
primary_numbered_boundary: V30
live_ledger_boundary_at_audit: C729
purpose: Placement, provenance, witness identity, and permitted revision scope; not claim-level supplementary deep reading
---

# MONOGATARI V2 — Supplementary Source Placement Audit

## 0. Audit decision

This document admits the **three supplied supplementary EPUBs into the V2 source architecture as placed sources**, but it does **not yet admit their story-level claims into L01–L09**.

The governing distinction is:

> **source placement is not claim admission.**

A supplementary story must first be given a recoverable publication/release horizon, an internal-story horizon where the text permits one, a narrator/focalizer or script-voice state, a source-authority class, and an explicit permitted revision scope. Only a later controlled supplementary deep reading may promote concrete claims from that story into the live evidence system.

This audit also rejects a single generic “bonus material” category. The three supplied files perform materially different analytical functions.
## 1. Governing authority and inherited locks

This audit is governed by, in order:

1. the canonical Monogatari V2 root and `CURRENT_STATE_AND_CORPUS_MAP.md` v1.15;
2. `PROJECT_DECISIONS_AND_SCOPE.md`, especially P0-SS-01 through P0-SS-04;
3. `MONOGATARI_V2_ANALYTICAL_METHOD.md`;
4. `MONOGATARI_V2_MULTI_DOCUMENT_SYNTHESIS_ARCHITECTURE.md`;
5. the frozen Final, Off, Monster, and V30 Family source-boundary checkpoints where their release horizons apply.

The analytical method already requires every side story to be tracked on **publication position** and **internal chronology** independently. The synthesis architecture additionally forbids specialist stabilization before narrator and chronology have been audited.

Therefore a later-published prequel may revise the reader's understanding of an earlier event through **RC**, but it cannot be treated as information that an earlier narrator or character already possessed.
## 2. File-level integrity and source identity

| Source | Drive ID | Bytes | SHA-256 | ZIP/EPUB integrity | File-level role |
|---|---:|---:|---|---|---|
| `短物語.epub` | `1jwAmH0lE59idvXCCWuzxIjCBWPLXvKfg` | 501,495 | `b6902c029d5743567df1987782aca0de586e5116f0731e4bc6e65e1f63b8e969` | PASS | 39-story authored supplementary-prose compilation; story-level first-release positions required |
| `佰物語オリジナルドラマCD シナリオブック.epub` | `1yqvK0plQHuyz-2-AjDTdnoIDiXboyTp8` | 197,107 | `fdc1f41f7b9b7562c4abc7871297d34cb2ceb3ba20cb881dd705e6db3cc4ac35` | PASS | Nisio-authored hybrid script/audio-adjacent ensemble source; 100 micro-sketches |
| `化物語 アニメコンプリートガイドブック.epub` | `1vYokBdaWcKmX_rSMFt3nOXc4EdPfz_ns` | 48,781 | `59e2747939e8d3d6edd292ddc38a77b47251323c03b889354c2730543e52481c` | PASS | Five authorized prose shorts; earliest textual witness for SHORT-001–005 |

### 2.1 Metadata cautions

- `短物語` has coherent EPUB metadata: 西尾維新 / 講談社 / Japanese, with an OPF date consistent with the 2024 compilation era. Publisher records give paper publication **2024-09-11** and electronic publication **2024-09-10**. Its internal electronic colophon is a separate wrapper/basis datum and must not be used to overwrite the publisher release record.
- `佰物語` has **bad wrapper metadata** (`Unknown`, language `en`, null-like date). Those fields are rejected as authority. Internal source text identifies 西尾維新 and records `2009年7月29日 第1刷発行`; the official Kodansha commercial-release record is **2009-08-04**.
- The guidebook EPUB's conversion metadata is not its first-publication date. Official Kodansha publication is **2010-10-28**.

Drive created/modified timestamps are file-history metadata only and have no publication authority.
## 3. Authority classes

### SUP-A — Authored supplementary prose

Applies primarily to the 39 individual stories now compiled in `短物語`.

**Default authority:** high for locally explicit events, voice, address, ordinary biography, relationship state, and self-presentation when story placement is secure; conditional for causal/metaphysical generalization; never permitted to erase earlier publication-local ambiguity simply because it was written later.

### SUP-B — Authorized paratextual-fiction witness

Applies to the five prose pieces in `化物語 アニメコンプリートガイドブック`.

These are not “production commentary.” They are authored fiction embedded in an anime guidebook. They are the **earliest-release witnesses** for the same five stories later compiled as `短物語` SHORT-001–005.

**Default authority:** same underlying fiction for story-level analysis; the 2010 witness controls 2010 release-local wording. The 2024 compilation witness controls 2024 compilation wording. The two witnesses are **not independent corroboration**.

### SUP-C — Nisio-authored hybrid scenario / audio-adjacent ensemble source

Applies to `佰物語`.

The internal afterword explicitly places it between novel and anime—“第三セクター,” and “どちらかと言えばアニメ寄り.” It is written by Nisio but designed as a performance script with ensemble rhythm rather than a conventional prose volume.

**Default authority:** very high for voice, address terms, comic timing, ensemble relation, repeated verbal routines, and locally explicit ordinary school-life details; lower than numbered novels for major plot chronology, metaphysics, or oddity rules.
## 4. Release horizon versus internal horizon

Every supplementary unit receives two independent coordinates:

- **Release horizon** — the numbered-volume knowledge available when that text first became available to readers.
- **Internal horizon** — the story-world position represented inside the short, if recoverable.

Neither coordinate substitutes for the other.

A 2017 short set during Kizumonogatari has a **2017 compositional/release horizon** and a **spring-break internal horizon**. It may therefore contain a later-authored reinterpretation of spring break, but the characters inside the spring-break scene do not inherit 2017 reader knowledge.

For frozen-checkpoint routing, this audit uses the latest checkpoint whose source boundary is already fully available at the supplementary text's first release. If no such checkpoint exists, the applicable release-local authority is the corresponding numbered-volume reading horizon rather than a later freeze.
## 5. `短物語` as a compilation: global placement

`短物語` cannot be assigned one analytical date.

Its preface states that the inherited short-shorts are arranged **basically in writing order**, not story chronology. The collection itself also contains multiple kinds of provenance:

- 33 earlier short-shorts first released through guidebooks, newspapers, heroine books, BD/DVD booklets, exhibition material, film books, event premiums, and related products;
- four stories written specifically for the 2024 collection (`よつぎスノードーム`, `おうぎロードムービー`, `そだちペナルティ`, `しのぶトゥナイト`);
- two 2024 official-web stories (`なでこパスト`, `しのぶフューチャー`) written as source prose for YOASOBI's `UNDEAD` / the Off & Monster Season anime project.

Accordingly, `短物語` is a **compilation witness and retrieval container**, while each of its 39 stories retains an independent first-release coordinate.
## 6. `短物語` story-by-story release placement

| ID | Story | First release / source | First-release date | Numbered release horizon | Governing frozen authority |
|---|---|---|---|---|---|
| SHORT-001 | ひたぎブッフェ | 『化物語 アニメコンプリートガイドブック』 | 2010-10-28 | through V08 | none; use V08 numbered authority |
| SHORT-002 | まよいルーム | 『化物語 アニメコンプリートガイドブック』 | 2010-10-28 | through V08 | none; use V08 numbered authority |
| SHORT-003 | するがコート | 『化物語 アニメコンプリートガイドブック』 | 2010-10-28 | through V08 | none; use V08 numbered authority |
| SHORT-004 | なでこプール | 『化物語 アニメコンプリートガイドブック』 | 2010-10-28 | through V08 | none; use V08 numbered authority |
| SHORT-005 | つばさソング | 『化物語 アニメコンプリートガイドブック』 | 2010-10-28 | through V08 | none; use V08 numbered authority |
| SHORT-006 | ひたぎネック | 『偽物語 アニメコンプリートガイドブック』 | 2012-09-28 | through V14 | none; use V14 numbered authority |
| SHORT-007 | かれんアームレッグ | 『偽物語 アニメコンプリートガイドブック』 | 2012-09-28 | through V14 | none; use V14 numbered authority |
| SHORT-008 | つきひエターナル | 『偽物語 アニメコンプリートガイドブック』 | 2012-09-28 | through V14 | none; use V14 numbered authority |
| SHORT-009 | しのぶハウス | 『偽物語 アニメコンプリートガイドブック』 | 2012-09-28 | through V14 | none; use V14 numbered authority |
| SHORT-010 | つばさボード | 読売新聞 | 2013-07-06 | through V15 | none; use V15 numbered authority |
| SHORT-011 | まよいキャッスル | 読売新聞 | 2013-08-17 | through V15 | none; use V15 numbered authority |
| SHORT-012 | ひたぎコイン | 『化物語［入門編］』 | 2013-09-13 | through V15 | none; use V15 numbered authority |
| SHORT-013 | なでこミラー | 読売新聞 | 2013-09-21 | through V15 | none; use V15 numbered authority |
| SHORT-014 | しのぶサイエンス | 読売新聞 | 2013-10-26 | through V16 | none; use V16 numbered authority |
| SHORT-015 | ひたぎフィギュア | 『「化物語」PremiumアイテムBOX』 | 2013-11-22 | through V16 | none; use V16 numbered authority |
| SHORT-016 | ひたぎサラマンダー | 読売新聞 | 2013-11-23 | through V16 | none; use V16 numbered authority |
| SHORT-017 | ひたぎスローイング | ヒロイン本 其ノ伍 戦場ヶ原ひたぎ | 2014-04-02 | through V18 | none; use V18 numbered authority |
| SHORT-018 | するがパレス | 『鬼物語』第一巻 限定版別冊 | 2014-04-23 | through V18 | none; use V18 numbered authority |
| SHORT-019 | よつぎフューチャー | 『鬼物語』第二巻 限定版別冊 | 2014-05-28 | through V18 | none; use V18 numbered authority |
| SHORT-020 | おうぎトラベル | 『鬼物語』第二巻 限定版別冊 | 2014-05-28 | through V18 | none; use V18 numbered authority |
| SHORT-021 | するがニート | 読売新聞 | 2014-08-16 | through V18 | none; use V18 numbered authority |
| SHORT-022 | ろうかゴッド | ヒロイン本 其ノ陸 神原駿河 | 2014-09-19 | through V19 | Final Season checkpoint through V19 |
| SHORT-023 | しのぶフィギュア | 『「偽物語」PremiumアイテムBOX』 | 2014-11-21 | through V19 | Final Season checkpoint through V19 |
| SHORT-024 | かれんブラッシング | ヒロイン本 其ノ漆 ファイヤーシスターズ | 2015-07-09 | through V19 | Final Season checkpoint through V19 |
| SHORT-025 | つきひブラッシング | ヒロイン本 其ノ漆 ファイヤーシスターズ | 2015-07-09 | through V19 | Final Season checkpoint through V19 |
| SHORT-026 | こよみヒストリー | MADOGATARI展 図録 | 2015-11-27 exhibition horizon | through V20 | Final Season checkpoint + V20 release horizon |
| SHORT-027 | よつぎストレス | ヒロイン本 其ノ捌 斧乃木余接 | 2015-12-23 | through V20 | Final Season checkpoint + V20 release horizon |
| SHORT-028 | 人として | 映画『傷物語』ビジュアルブック PART2 | 2017-01-14 | through V23 | Off Season checkpoint through V23 |
| SHORT-029 | どうかして | 映画『傷物語』ビジュアルブック PART2 | 2017-01-14 | through V23 | Off Season checkpoint through V23 |
| SHORT-030 | そして | 映画『傷物語』ビジュアルブック PART2 | 2017-01-14 | through V23 | Off Season checkpoint through V23 |
| SHORT-031 | どうして | 『西尾維新祭2016 SPECIAL FANBOOK』 | 2017-03 distribution; catalog gives 2017-03-01 | through V23 | Off Season checkpoint through V23 |
| SHORT-032 | 心して | 映画『傷物語』COMPLETE GUIDE BOOK | 2017-11-29 | through V24 | Off Season checkpoint + V24 release horizon |
| SHORT-033 | まよいウェルカム | 『西尾維新の挑戦状』AnimeJapan event prize | 2017-03-26 | through V23 | Off Season checkpoint through V23 |
| SHORT-034 | よつぎスノードーム | 『短物語』書き下ろし | 2024-09 | through V30 | V30 Family source-boundary checkpoint |
| SHORT-035 | おうぎロードムービー | 『短物語』書き下ろし | 2024-09 | through V30 | V30 Family source-boundary checkpoint |
| SHORT-036 | そだちペナルティ | 『短物語』書き下ろし | 2024-09 | through V30 | V30 Family source-boundary checkpoint |
| SHORT-037 | しのぶトゥナイト | 『短物語』書き下ろし | 2024-09 | through V30 | V30 Family source-boundary checkpoint |
| SHORT-038 | なでこパスト | Off & Monster Season official website / YOASOBI “UNDEAD” source prose | 2024; exact posting date not recovered | through V30 | V30 Family source-boundary checkpoint |
| SHORT-039 | しのぶフューチャー | Off & Monster Season official website / YOASOBI “UNDEAD” source prose | 2024; exact posting date not recovered | through V30 | V30 Family source-boundary checkpoint |

### 6.1 Publication-order cautions

- Collection order is **not** strict first-release order. The clearest example is `まよいウェルカム` (2017-03-26) appearing after `心して` (2017-11-29) in the compilation.
- `人として` / `どうかして` / `そして` first appeared only two days after the official **2017-01-12** release of `結物語`; their release-local reader horizon therefore includes V23 even though two of them return internally to Kizumonogatari-era material.
- `まよいウェルカム` was released after V23 but before V24 and internally advertises itself as something that can be called a prequel to `忍物語`.
- The 2024 pieces are post-V30 in publication horizon even where they are internally located in high school, university, or the V23→V30 adult bridge.
## 7. `短物語` narrator and internal-story placement

| ID | Story | Narrator/focalizer | Internal-story placement | Confidence | Permitted first-pass revision scope |
|---|---|---|---|---|---|
| SHORT-001 | ひたぎブッフェ | 阿良々木暦 | High-school dating period after crab/monkey relations are established; exact adjacency OPEN | bounded | Local relationship/voice/ordinary-life facts; no major metaphysics override |
| SHORT-002 | まよいルーム | 阿良々木暦 | Exam-study period; Hachikuji remains ghost; late third year, before deity state | strong | Local Araragi–Hachikuji relation and voice |
| SHORT-003 | するがコート | 阿良々木暦 | High-school period with Araragi/Kanbaru/Hitagi relation established; exact point OPEN | bounded | Local relationship/voice evidence |
| SHORT-004 | なでこプール | 阿良々木暦 | Araragi is exam candidate; Nadeko still in ordinary middle-school relation; likely before V11 rupture | bounded | Local relation/voice; do not backproject later Nadeko selves |
| SHORT-005 | つばさソング | 阿良々木暦 | High school; Araragi/Hitagi relationship established; Hanekawa braids cut at end; exact adjacency OPEN | bounded | Hanekawa/Araragi voice and relational evidence |
| SHORT-006 | ひたぎネック | 阿良々木暦 | Hitagi is about to be introduced to the Fire Sisters | strong | Local family-introduction/relationship evidence |
| SHORT-007 | かれんアームレッグ | 阿良々木暦 | Late summer vacation; Araragi has recently started dating Hitagi | strong | Family voice and ordinary-life relation |
| SHORT-008 | つきひエターナル | 阿良々木暦 | Immediately after Kagenui/Ononoki confrontation in V06; before summer break ends | strong | V06 aftermath / Tsukihi family relation; later outcomes forbidden |
| SHORT-009 | しのぶハウス | 阿良々木暦 | Night after the family “ガハラサミット” sequence in the associated short-fiction cluster | bounded | Local household/relationship evidence |
| SHORT-010 | つばさボード | 羽川翼 | Hanekawa self-narration; exact internal date OPEN | open | High-value Hanekawa voice/self-presentation; chronology-sensitive claims remain OPEN |
| SHORT-011 | まよいキャッスル | 八九寺真宵 | Ghost-era Hachikuji/Araragi relation; exact point OPEN | open | High-value Hachikuji voice; no later deity-state backprojection |
| SHORT-012 | ひたぎコイン | 阿良々木暦 | High-school conversation about Hitagi’s two years concealing her condition | bounded | Hitagi history/relationship framing; narrator filtered |
| SHORT-013 | なでこミラー | 千石撫子 | Middle-school Nadeko first-person before later god/self-authoring states; exact date OPEN | bounded | Very high Nadeko voice evidence; later Nadeko cannot be backprojected |
| SHORT-014 | しのぶサイエンス | 忍野忍 | Shinobu first-person speculative scene; exact internal date OPEN | open | High Shinobu voice; speculative metaphysics remains CD/IT unless corroborated |
| SHORT-015 | ひたぎフィギュア | 阿良々木暦 | “斧乃木余接との奇妙な同居生活が始まった直後頃”; exam-study period | strong | Late-third-year domestic/Ononoki relation |
| SHORT-016 | ひたぎサラマンダー | 貝木泥舟 | Kaiki/Hitagi discussion of reading/past; exact date broad/OPEN | open | Kaiki/Hitagi voice and history; Kaiki framing not objective fact |
| SHORT-017 | ひたぎスローイング | 神原駿河 | Kanbaru retrospective to first meeting Hitagi in middle school (Kanbaru ~12; Hitagi one school year older) | strong | Local prehistory via Kanbaru NR; no totalizing current relationship inference |
| SHORT-018 | するがパレス | 神原駿河 | Kanbaru current narrator; relationship with Araragi established; exact point broad | open | Kanbaru voice/relationship |
| SHORT-019 | よつぎフューチャー | 斧乃木余接 | Ononoki meta-dialogue with Araragi; exact date broad | open | Ononoki voice; meta claims not automatic ontology |
| SHORT-020 | おうぎトラベル | 忍野扇 | Ougi asks Hanekawa about intended post-graduation world travel; late high school, pre-graduation | strong | Ougi/Hanekawa relational and future-intent evidence |
| SHORT-021 | するがニート | 神原駿河 | Kanbaru dreams/converses with deceased Tooe; story-now chronology intentionally weak | open | Kanbaru/Tooe affective evidence; literal ontology and placement guarded |
| SHORT-022 | ろうかゴッド | 貝木泥舟 | Kaiki meets Rouka after she says she graduated middle school; likely pre-V10 / pre-demon-collection context | bounded | Can revise Rouka prehistory locally; cannot become Kanbaru’s earlier knowledge |
| SHORT-023 | しのぶフィギュア | 阿良々木暦 | Self-parodic chronology-joking short; exact position intentionally unstable | open | Voice/comic relation only unless locally explicit |
| SHORT-024 | かれんブラッシング | 阿良々木火憐 | School-era family comic; exact point broad | open | Karen voice/family routine; fetishized joke ≠ objective norm |
| SHORT-025 | つきひブラッシング | 阿良々木月火 | Araragi has graduated; Nadeko “だいぶん快方”; roughly post-V19/immediate post-graduation | bounded | Tsukihi voice and post-graduation family state |
| SHORT-026 | こよみヒストリー | 阿良々木暦 / meta-retrospective composite | Meta-retrospective dialogue montage, not one ordinary diegetic event | meta | Series-memory/voice evidence; no single-scene chronology |
| SHORT-027 | よつぎストレス | 羽川翼（ブラック羽川） | Black Hanekawa + Shinobu + Ononoki vs ape oddity; exact chronology uncertain/playful | open | Voice/interaction evidence; major oddity claims require numbered corroboration |
| SHORT-028 | 人として | キスショット／忍野忍 | Inserted Kizumonogatari spring-break viewpoint | strong | Can RC reader understanding of V04; cannot become V04 Araragi knowledge |
| SHORT-029 | どうかして | 羽川翼 | Inserted Kizumonogatari spring-break viewpoint | strong | Can RC reader understanding of V04; not retroactive consent/knowledge |
| SHORT-030 | そして | 阿良々木暦 | Dramaturgy visits exactly 360 days after spring-break fight; post-high-school graduation | strong | One-year-later Kizu aftermath; release-horizon hindsight distinct from event chronology |
| SHORT-031 | どうして | 忍野メメ | Meme retrospectively narrates spring-break first encounter with Kiss-shot/Araragi | strong | High Meme voice and V04 RC; distribution date medium confidence |
| SHORT-032 | 心して | 外部三人称／ハンター側 | Kizumonogatari hunter-side inserted scene | strong | Hunter-side RC of V04; later V24 knowledge cannot become spring-break character knowledge |
| SHORT-033 | まよいウェルカム | デストピア・ヴィルトゥオーゾ・スーサイドマスター | Explicitly a lead-in / “忍物語の前日譚とも言える”; immediately before V24 | very strong | Direct V24 prelude; V24 outcome cannot be backprojected into Suicide-Master’s pre-case knowledge |
| SHORT-034 | よつぎスノードーム | 阿良々木暦 | Preface: Araragi still at Naoetsu High; Ononoki recently live-in; entrance exams | strong | Later-authored prequel: may RC late-HS relation, not retroactively alter publication-local reader knowledge |
| SHORT-035 | おうぎロードムービー | 阿良々木暦 | Preface: immediately after graduation; university accepted, pre-entry interval | very strong | Post-graduation bridge; later adult outcomes cannot be imported unless stated |
| SHORT-036 | そだちペナルティ | 阿良々木暦 | Preface: during 曲直瀬大学; opening after semester exam; exact year OPEN | bounded | University Sodachi relation; exact year and later career states guarded |
| SHORT-037 | しのぶトゥナイト | 阿良々木暦 | Working adult: university graduate, police officer, upcoming long U.S. assignment; bridge V23→V30 | very strong | Adult bridge; V30 marriage/witness-protection state not assumed unless text states it |
| SHORT-038 | なでこパスト | 斧乃木余接 | Off/Monster-era reflective counseling with Nadeko; exact point OPEN | open | Voice/self-model evidence; do not assign to a specific V25/V29 stage without local proof |
| SHORT-039 | しのぶフューチャー | 斧乃木余接 | Off/Monster-era reflective counseling with Shinobu; exact point OPEN | open | Voice/future-self evidence; exact Monster/Family placement remains OPEN |

### 7.1 Internal-position locks for the most chronology-sensitive shorts

**Kizumonogatari insertions (`人として`, `どうかして`, `どうして`, `心して`).** These can supply RC evidence about the spring-break episode from other perspectives. They cannot be used to claim that V04 Araragi already knew those perspectives.

**`そして`.** This has a locally explicit “360 days later” relation to the Kizumonogatari fight and therefore provides a comparatively strong internal anchor, but its 2017 composition/release horizon remains separate.

**`まよいウェルカム`.** This is a particularly clean dual-position case: post-V23/pre-V24 publication, immediately-pre-V24 internal placement. It may become the direct supplementary prelude to the V24 reading in a later admission pass, but V24 outcomes must not be smuggled backward into Suicide-Master's pre-case knowledge.

**2024 collection-new stories.** Their preface-supplied chronology is useful evidence, but later publication means they are retrospective insertions. `しのぶトゥナイト` is especially important as a V23→V30 bridge; it may strengthen the adult-career transition without allowing V30 marriage/witness-protection facts to be presumed unless the story itself supplies them.

**`なでこパスト` / `しのぶフューチャー`.** Their Off/Monster reflective state is clear, but an exact numbered-volume slot is not. They remain OPEN at finer chronology until a dedicated deep reading finds a defensible local anchor.
## 8. Guidebook ↔ `短物語` duplicate-witness crosswalk

The guidebook EPUB contains exactly five prose stories, all narrated by Araragi. They correspond one-to-one with SHORT-001–005.

| Guide witness | Later compilation witness | Relationship | Normalized-text similarity | Authority rule |
|---|---|---|---:|---|
| GUIDE-001 `ひたぎブッフェ` | SHORT-001 | same story, later compilation witness | ~0.9955 | 2010 guide controls original release-local wording; 2024 collection controls compilation wording |
| GUIDE-002 `まよいルーム` | SHORT-002 | same story, later compilation witness | ~0.9891 | same |
| GUIDE-003 `するがコート` | SHORT-003 | same story, later compilation witness | ~0.9920 | same |
| GUIDE-004 `なでこプール` | SHORT-004 | same story, later compilation witness | ~0.9949 | same |
| GUIDE-005 `つばさソング` | SHORT-005 | same story, later compilation witness | ~0.9957 | same |

The witnesses are **not text-identical**. Differences are predominantly orthographic/editorial normalization, punctuation and glyph normalization, typo correction, and scattered small lexical/deletion differences. The audit does **not** assume every variation is an authorial revision.

Therefore:

1. never count GUIDE-001 + SHORT-001 as two independent pieces of corroboration;
2. when exact wording matters, cite the witness edition explicitly;
3. when a difference itself becomes analytically important, classify the change before interpreting it as intentional;
4. for 2010 publication-local reconstruction, use the guidebook witness;
5. for 2024 compilation-era framing, use the `短物語` witness.
## 9. `佰物語`: source identity and release position

### 9.1 Bibliographic placement

Internal source text identifies the work as `オリジナルドラマＣＤ シナリオブック 佰物語`, by 西尾維新, and records `2009年7月29日 第1刷発行`. Official Kodansha records commercial release **2009-08-04**.

This places the source **after V06 `偽物語（下）` and before V07 `猫物語（黒）`** in reader release order.

No later frozen V2 checkpoint may be treated as having existed at that publication horizon. Release-local reconstruction therefore uses the numbered authority available through V06.

### 9.2 Form and narrator state

`佰物語` is not a 100-chapter prose novel. It is a script/scenario book for an audio work comprising 100 school-life topic sketches plus framing material.

The afterword says Nisio wrote the scenario and characterizes the resulting work as neither simply the anime nor the original novel, but a third-sector production, somewhat closer to anime. It also describes Shinobu as a mysterious, halting narrator for the audio production.

For the **supplied scriptbook**, however, the story units are overwhelmingly **direct dialogue**. The correct unit-level focalization is therefore the named speaker ensemble, not “Shinobu first-person narration” for all 100 units.

### 9.3 Chronology class

The 100 sketches are not a continuous school day and should not be forced into a monotonic chronology. They move among school topics, recollections, hypotheticals, and stylized situations. The safest global class is:

> **high-school ensemble/topic-sketch space with late-third-year/post-event awareness in some units, but local reach into earlier school years and pre-high-school recollection.**

Exact internal dates are assigned only where a unit itself supplies an anchor.
## 10. `佰物語` 100-unit voice and placement index

| ID | Topic | Primary voices in supplied script | Internal-placement class |
|---|---|---|---|
| HYAKU-001 | 入学試験 | 阿良々木暦／戦場ヶ原ひたぎ | pre-entry topic/recollection; exact narrated now-position UA |
| HYAKU-002 | 合格発表 | 阿良々木暦／戦場ヶ原ひたぎ | pre-entry topic/recollection; exact narrated now-position UA |
| HYAKU-003 | 入学式 | 阿良々木暦／羽川翼 | entrance-ceremony/year-1 topic; exact enacted chronology UA |
| HYAKU-004 | 制服 | 阿良々木暦／羽川翼 | high-school ensemble/topic-sketch space; exact chronology UA unless later deep reading finds a local anchor |
| HYAKU-005 | クラス分け | 戦場ヶ原ひたぎ／阿良々木暦 | multi-year retrospective (explicitly looks across all three classes); late-HS awareness |
| HYAKU-006 | 週休二日 | 神原駿河／阿良々木暦 | high-school ensemble/topic-sketch space; exact chronology UA unless later deep reading finds a local anchor |
| HYAKU-007 | テスト | 阿良々木暦／羽川翼 | high-school ensemble/topic-sketch space; exact chronology UA unless later deep reading finds a local anchor |
| HYAKU-008 | 文系・理系 | 八九寺真宵／阿良々木暦 | high-school ensemble/topic-sketch space; exact chronology UA unless later deep reading finds a local anchor |
| HYAKU-009 | 国語 | 阿良々木暦／八九寺真宵 | high-school ensemble/topic-sketch space; exact chronology UA unless later deep reading finds a local anchor |
| HYAKU-010 | 数学 | 千石撫子／阿良々木暦 | high-school ensemble/topic-sketch space; exact chronology UA unless later deep reading finds a local anchor |
| HYAKU-011 | 社会 | 羽川翼／阿良々木暦 | high-school ensemble/topic-sketch space; exact chronology UA unless later deep reading finds a local anchor |
| HYAKU-012 | 英語 | 羽川翼／神原駿河 | high-school ensemble/topic-sketch space; exact chronology UA unless later deep reading finds a local anchor |
| HYAKU-013 | 理科 | 阿良々木暦／八九寺真宵 | high-school ensemble/topic-sketch space; exact chronology UA unless later deep reading finds a local anchor |
| HYAKU-014 | 体育 | 阿良々木暦／羽川翼 | high-school ensemble/topic-sketch space; exact chronology UA unless later deep reading finds a local anchor |
| HYAKU-015 | 保健体育 | 神原駿河／阿良々木暦 | high-school ensemble/topic-sketch space; exact chronology UA unless later deep reading finds a local anchor |
| HYAKU-016 | 音楽 | 羽川翼／阿良々木暦 | high-school ensemble/topic-sketch space; exact chronology UA unless later deep reading finds a local anchor |
| HYAKU-017 | 書道 | 阿良々木暦／神原駿河 | high-school ensemble/topic-sketch space; exact chronology UA unless later deep reading finds a local anchor |
| HYAKU-018 | 美術 | 戦場ヶ原ひたぎ／阿良々木暦 | high-school ensemble/topic-sketch space; exact chronology UA unless later deep reading finds a local anchor |
| HYAKU-019 | 家庭科 | 神原駿河／阿良々木暦 | high-school ensemble/topic-sketch space; exact chronology UA unless later deep reading finds a local anchor |
| HYAKU-020 | 教師 | 阿良々木暦／戦場ヶ原ひたぎ | high-school ensemble/topic-sketch space; exact chronology UA unless later deep reading finds a local anchor |
| HYAKU-021 | 登下校 | 阿良々木暦／神原駿河 | high-school ensemble/topic-sketch space; exact chronology UA unless later deep reading finds a local anchor |
| HYAKU-022 | クラブ活動 | 阿良々木暦／戦場ヶ原ひたぎ | high-school ensemble/topic-sketch space; exact chronology UA unless later deep reading finds a local anchor |
| HYAKU-023 | 放課後 | 阿良々木暦／火憐／月火 | high-school ensemble/topic-sketch space; exact chronology UA unless later deep reading finds a local anchor |
| HYAKU-024 | 私服 | 阿良々木暦／八九寺真宵 | high-school ensemble/topic-sketch space; exact chronology UA unless later deep reading finds a local anchor |
| HYAKU-025 | 友達 | 八九寺真宵／阿良々木暦 | high-school ensemble/topic-sketch space; exact chronology UA unless later deep reading finds a local anchor |
| HYAKU-026 | 携帯電話 | 阿良々木暦／羽川翼 | high-school ensemble/topic-sketch space; exact chronology UA unless later deep reading finds a local anchor |
| HYAKU-027 | メール | 羽川翼／阿良々木暦 | high-school ensemble/topic-sketch space; exact chronology UA unless later deep reading finds a local anchor |
| HYAKU-028 | アルバイト | 阿良々木暦／羽川翼 | high-school ensemble/topic-sketch space; exact chronology UA unless later deep reading finds a local anchor |
| HYAKU-029 | テレビ | 阿良々木暦／戦場ヶ原ひたぎ | high-school ensemble/topic-sketch space; exact chronology UA unless later deep reading finds a local anchor |
| HYAKU-030 | ラジオ | 阿良々木暦／羽川翼 | high-school ensemble/topic-sketch space; exact chronology UA unless later deep reading finds a local anchor |
| HYAKU-031 | 体操服 | 神原駿河／阿良々木暦 | high-school ensemble/topic-sketch space; exact chronology UA unless later deep reading finds a local anchor |
| HYAKU-032 | プール | 阿良々木暦／神原駿河 | high-school ensemble/topic-sketch space; exact chronology UA unless later deep reading finds a local anchor |
| HYAKU-033 | 喧嘩 | 火憐／阿良々木暦 | high-school ensemble/topic-sketch space; exact chronology UA unless later deep reading finds a local anchor |
| HYAKU-034 | 体育祭 | 神原駿河／阿良々木暦 | school-calendar/topic sketch; may recall multiple years; exact year UA |
| HYAKU-035 | ニックネーム | 阿良々木暦／羽川翼 | high-school ensemble/topic-sketch space; exact chronology UA unless later deep reading finds a local anchor |
| HYAKU-036 | 更衣室 | 阿良々木暦／神原駿河 | high-school ensemble/topic-sketch space; exact chronology UA unless later deep reading finds a local anchor |
| HYAKU-037 | 身体測定 | 八九寺真宵／阿良々木暦 | high-school ensemble/topic-sketch space; exact chronology UA unless later deep reading finds a local anchor |
| HYAKU-038 | 出欠 | 戦場ヶ原ひたぎ／阿良々木暦 | high-school ensemble/topic-sketch space; exact chronology UA unless later deep reading finds a local anchor |
| HYAKU-039 | 学級閉鎖 | 千石撫子／阿良々木暦 | high-school ensemble/topic-sketch space; exact chronology UA unless later deep reading finds a local anchor |
| HYAKU-040 | 保健室 | 阿良々木暦／羽川翼 | high-school ensemble/topic-sketch space; exact chronology UA unless later deep reading finds a local anchor |
| HYAKU-041 | 図書室 | 阿良々木暦／羽川翼 | high-school ensemble/topic-sketch space; exact chronology UA unless later deep reading finds a local anchor |
| HYAKU-042 | 夏休み | 阿良々木暦／羽川翼 | school-calendar/topic sketch; may recall multiple years; exact year UA |
| HYAKU-043 | 冬休み | 阿良々木暦／八九寺真宵 | school-calendar/topic sketch; may recall multiple years; exact year UA |
| HYAKU-044 | 春休み | 阿良々木暦／羽川翼 | calendar/topic sketch with spring-break/GW resonance; exact event chronology not presumed |
| HYAKU-045 | ゴールデンウィーク | 羽川翼／阿良々木暦 | calendar/topic sketch with spring-break/GW resonance; exact event chronology not presumed |
| HYAKU-046 | 避難訓練 | 八九寺真宵／阿良々木暦 | high-school ensemble/topic-sketch space; exact chronology UA unless later deep reading finds a local anchor |
| HYAKU-047 | 通知表 | 阿良々木暦／羽川翼 | high-school ensemble/topic-sketch space; exact chronology UA unless later deep reading finds a local anchor |
| HYAKU-048 | マラソン大会 | 阿良々木暦／千石撫子 | high-school ensemble/topic-sketch space; exact chronology UA unless later deep reading finds a local anchor |
| HYAKU-049 | 文房具 | 戦場ヶ原ひたぎ／阿良々木暦 | high-school ensemble/topic-sketch space; exact chronology UA unless later deep reading finds a local anchor |
| HYAKU-050 | 髪型 | 阿良々木暦／羽川翼 | high-school ensemble/topic-sketch space; exact chronology UA unless later deep reading finds a local anchor |
| HYAKU-051 | 委員長 | 阿良々木暦／羽川翼 | high-school ensemble/topic-sketch space; exact chronology UA unless later deep reading finds a local anchor |
| HYAKU-052 | 不良 | 阿良々木暦／神原駿河 | high-school ensemble/topic-sketch space; exact chronology UA unless later deep reading finds a local anchor |
| HYAKU-053 | 階段 | 戦場ヶ原ひたぎ／阿良々木暦 | high-school ensemble/topic-sketch space; exact chronology UA unless later deep reading finds a local anchor |
| HYAKU-054 | 怪談 | 羽川翼／阿良々木暦 | high-school ensemble/topic-sketch space; exact chronology UA unless later deep reading finds a local anchor |
| HYAKU-055 | 青春 | 阿良々木暦／忍野メメ | high-school ensemble/topic-sketch space; exact chronology UA unless later deep reading finds a local anchor |
| HYAKU-056 | 屋上 | 阿良々木暦／羽川翼 | high-school ensemble/topic-sketch space; exact chronology UA unless later deep reading finds a local anchor |
| HYAKU-057 | 授業 | 千石撫子／阿良々木暦 | high-school ensemble/topic-sketch space; exact chronology UA unless later deep reading finds a local anchor |
| HYAKU-058 | 席替え | 千石撫子／阿良々木暦 | high-school ensemble/topic-sketch space; exact chronology UA unless later deep reading finds a local anchor |
| HYAKU-059 | 教科書 | 阿良々木暦／八九寺真宵 | high-school ensemble/topic-sketch space; exact chronology UA unless later deep reading finds a local anchor |
| HYAKU-060 | ゲームセンター | 阿良々木暦／千石撫子 | high-school ensemble/topic-sketch space; exact chronology UA unless later deep reading finds a local anchor |
| HYAKU-061 | バレンタインデー | 八九寺真宵／阿良々木暦 | high-school ensemble/topic-sketch space; exact chronology UA unless later deep reading finds a local anchor |
| HYAKU-062 | 移動教室 | 戦場ヶ原ひたぎ／阿良々木暦 | high-school ensemble/topic-sketch space; exact chronology UA unless later deep reading finds a local anchor |
| HYAKU-063 | 黒板 | 戦場ヶ原ひたぎ／阿良々木暦 | high-school ensemble/topic-sketch space; exact chronology UA unless later deep reading finds a local anchor |
| HYAKU-064 | 将来の夢 | 忍野メメ／阿良々木暦 | high-school ensemble/topic-sketch space; exact chronology UA unless later deep reading finds a local anchor |
| HYAKU-065 | ラブレター | 八九寺真宵／阿良々木暦 | high-school ensemble/topic-sketch space; exact chronology UA unless later deep reading finds a local anchor |
| HYAKU-066 | 修学旅行 | 羽川翼／阿良々木暦 | school-calendar/topic sketch; may recall multiple years; exact year UA |
| HYAKU-067 | 宿題 | 阿良々木暦／羽川翼 | high-school ensemble/topic-sketch space; exact chronology UA unless later deep reading finds a local anchor |
| HYAKU-068 | お弁当 | 阿良々木暦／八九寺真宵 | high-school ensemble/topic-sketch space; exact chronology UA unless later deep reading finds a local anchor |
| HYAKU-069 | 受験勉強 | 阿良々木暦／羽川翼 | exam/admissions topic; late-third-year thematic placement, exact scene UA |
| HYAKU-070 | 推薦入試 | 阿良々木暦／戦場ヶ原ひたぎ | exam/admissions topic; late-third-year thematic placement, exact scene UA |
| HYAKU-071 | 合唱会 | 阿良々木暦／八九寺真宵 | school-calendar/topic sketch; may recall multiple years; exact year UA |
| HYAKU-072 | 肝試し | 阿良々木暦／八九寺真宵 | high-school ensemble/topic-sketch space; exact chronology UA unless later deep reading finds a local anchor |
| HYAKU-073 | 休み時間 | 阿良々木暦／羽川翼 | high-school ensemble/topic-sketch space; exact chronology UA unless later deep reading finds a local anchor |
| HYAKU-074 | 出席番号 | 神原駿河／阿良々木暦 | high-school ensemble/topic-sketch space; exact chronology UA unless later deep reading finds a local anchor |
| HYAKU-075 | 文化祭 | 八九寺真宵／阿良々木暦 | school-calendar/topic sketch; may recall multiple years; exact year UA |
| HYAKU-076 | 林間学校 | 八九寺真宵／阿良々木暦 | school-calendar/topic sketch; may recall multiple years; exact year UA |
| HYAKU-077 | 転校生 | 阿良々木暦／羽川翼 | high-school ensemble/topic-sketch space; exact chronology UA unless later deep reading finds a local anchor |
| HYAKU-078 | 学問 | 羽川翼／阿良々木暦 | high-school ensemble/topic-sketch space; exact chronology UA unless later deep reading finds a local anchor |
| HYAKU-079 | 読書 | 阿良々木暦／戦場ヶ原ひたぎ | high-school ensemble/topic-sketch space; exact chronology UA unless later deep reading finds a local anchor |
| HYAKU-080 | 衣替え | 阿良々木暦／八九寺真宵 | high-school ensemble/topic-sketch space; exact chronology UA unless later deep reading finds a local anchor |
| HYAKU-081 | 体育館 | 阿良々木暦／神原駿河 | high-school ensemble/topic-sketch space; exact chronology UA unless later deep reading finds a local anchor |
| HYAKU-082 | 気象警報 | 千石撫子／阿良々木暦 | high-school ensemble/topic-sketch space; exact chronology UA unless later deep reading finds a local anchor |
| HYAKU-083 | 掃除当番 | 羽川翼／阿良々木暦 | high-school ensemble/topic-sketch space; exact chronology UA unless later deep reading finds a local anchor |
| HYAKU-084 | 五月病 | 月火／阿良々木暦 | high-school ensemble/topic-sketch space; exact chronology UA unless later deep reading finds a local anchor |
| HYAKU-085 | 球技大会 | 神原駿河／阿良々木暦 | school-calendar/topic sketch; may recall multiple years; exact year UA |
| HYAKU-086 | 恋愛 | 阿良々木暦／八九寺真宵 | high-school ensemble/topic-sketch space; exact chronology UA unless later deep reading finds a local anchor |
| HYAKU-087 | 職員室 | 阿良々木暦／千石撫子 | high-school ensemble/topic-sketch space; exact chronology UA unless later deep reading finds a local anchor |
| HYAKU-088 | 朝礼 | 戦場ヶ原ひたぎ／阿良々木暦 | high-school ensemble/topic-sketch space; exact chronology UA unless later deep reading finds a local anchor |
| HYAKU-089 | 学級会 | 戦場ヶ原ひたぎ／阿良々木暦 | high-school ensemble/topic-sketch space; exact chronology UA unless later deep reading finds a local anchor |
| HYAKU-090 | ボランティア | 阿良々木暦／月火 | high-school ensemble/topic-sketch space; exact chronology UA unless later deep reading finds a local anchor |
| HYAKU-091 | 持ち物検査 | 阿良々木暦／戦場ヶ原ひたぎ | high-school ensemble/topic-sketch space; exact chronology UA unless later deep reading finds a local anchor |
| HYAKU-092 | テスト勉強 | 阿良々木暦／羽川翼 | high-school ensemble/topic-sketch space; exact chronology UA unless later deep reading finds a local anchor |
| HYAKU-093 | 廊下 | 火憐／阿良々木暦 | high-school ensemble/topic-sketch space; exact chronology UA unless later deep reading finds a local anchor |
| HYAKU-094 | 旅行 | 八九寺真宵／阿良々木暦 | high-school ensemble/topic-sketch space; exact chronology UA unless later deep reading finds a local anchor |
| HYAKU-095 | 告白 | 阿良々木暦／羽川翼 | high-school ensemble/topic-sketch space; exact chronology UA unless later deep reading finds a local anchor |
| HYAKU-096 | 掲示板 | 阿良々木暦／戦場ヶ原ひたぎ | high-school ensemble/topic-sketch space; exact chronology UA unless later deep reading finds a local anchor |
| HYAKU-097 | 買い食い | 羽川翼／阿良々木暦 | high-school ensemble/topic-sketch space; exact chronology UA unless later deep reading finds a local anchor |
| HYAKU-098 | ストーブ | 神原駿河／阿良々木暦 | high-school ensemble/topic-sketch space; exact chronology UA unless later deep reading finds a local anchor |
| HYAKU-099 | 体育倉庫 | 阿良々木暦／羽川翼 | high-school ensemble/topic-sketch space; exact chronology UA unless later deep reading finds a local anchor |
| HYAKU-100 | 卒業式 | 阿良々木暦／羽川翼（ブラック羽川） | graduation/meta-terminal sketch; stylized Black Hanekawa appearance; not strict chronology anchor |

### 10.1 `佰物語` evidentiary ceiling

Use `佰物語` confidently for:

- pronouns and self-reference;
- address terms and nicknames;
- banter structure;
- sentence-final habits;
- ordinary school-life assumptions;
- who can sustain what kind of joke with whom;
- ensemble rhythm and interpersonal familiarity;
- locally explicit mundane biography where no stronger numbered evidence contradicts it.

Do **not** allow `佰物語` by itself to settle:

- major oddity ontology;
- a contested supernatural rule;
- a numbered-volume contradiction;
- exact global chronology;
- a hidden motive that the script only jokes about;
- final moral or metaphysical doctrine.

If a Hyaku sketch conflicts with a numbered novel on a major plot/metaphysical issue, the numbered novel controls unless a later dedicated audit demonstrates a reason otherwise.
## 11. Supplementary claim-admission matrix

| Source class | Voice/address | Ordinary relationship state | Mundane biography | Internal chronology | Major plot | Oddity/metaphysics | Can RC earlier numbered reading? |
|---|---|---|---|---|---|---|---|
| SUP-A authored short prose | High | High when placement secure | High when explicit | Story-specific | Conditional | Conditional / corroboration required | Yes, with explicit release-vs-internal horizon |
| SUP-B guidebook fiction witness | High | High | High when explicit | Story-specific | Same underlying story as SHORT-001–005 | Same ceiling as underlying short | Yes; witness-specific wording only |
| SUP-C `佰物語` hybrid scenario | Very high | High | Conditional | Usually low unless locally explicit | Low | Low | Narrowly, chiefly voice/relation; numbered novels dominate plot/metaphysics |

This table defines **default ceilings**, not automatic truth values. A specific line can still be NR, CD, SI, IT, UA, RC, or VJ depending on speaker and context.
## 12. Checkpoint routing rules

### 12.1 Pre-Final supplementary releases

For supplementary pieces released before V19 was available, there is no frozen season checkpoint matching that historical release horizon. Use the latest numbered V2 reading available at first publication as the local authority. Later checkpoints may be used only in a separate retrospective RC layer.

### 12.2 Post-V19 / pre-V20

The frozen Final Season checkpoint may govern claims through V19.

### 12.3 Post-V20 but pre-Off freeze boundary

Use the Final checkpoint as the latest frozen base plus the specifically available Off Season numbered reading(s) as the release horizon.

### 12.4 Post-V23 / pre-V24

The frozen Off Season checkpoint is the proper baseline. This is especially important for the Kizu inserts and `まよいウェルカム`.

### 12.5 Post-V24 / pre-V25

Use the Off checkpoint plus V24 as the local numbered horizon; V25+ cannot backproject.

### 12.6 2024 supplementation after supplied V30

Use the V30 Family source-boundary checkpoint as the latest supplied numbered authority. This does **not** mean those 2024 shorts are internally set after V30.
## 13. Supplementary-placement locks

These locks govern all later supplementary reading and admission.

1. **SUP-PL-01 — Compilation date is not first-release date.** `短物語` must remain story-indexed.
2. **SUP-PL-02 — Publication horizon and internal horizon are independent.** Never substitute one for the other.
3. **SUP-PL-03 — Later prequel publication may revise reader interpretation without creating earlier character knowledge.**
4. **SUP-PL-04 — The guidebook five and `短物語` SHORT-001–005 are dual witnesses, not independent corroboration.**
5. **SUP-PL-05 — Exact wording is witness-sensitive.** Use the 2010 guide witness for 2010 wording and the 2024 collection witness for 2024 wording.
6. **SUP-PL-06 — Minor textual differences are not automatically authorial revisions.** Classify orthographic/editorial normalization before interpretation.
7. **SUP-PL-07 — `佰物語` wrapper metadata is not authority.** Internal colophon/source text and publisher bibliographic data control.
8. **SUP-PL-08 — `佰物語` is a hybrid scenario source, not a numbered prose novel.**
9. **SUP-PL-09 — The supplied Hyaku script is direct-dialogue dominant.** Do not assign Shinobu as prose narrator of all 100 units merely because the audio conception gives her a narrator role.
10. **SUP-PL-10 — Hyaku's 100 sketches are not a single continuous diegetic day.**
11. **SUP-PL-11 — Hyaku is high authority for voice and ensemble grammar, lower authority for plot/metaphysics.**
12. **SUP-PL-12 — A joke is not automatically biography, confession, or ontology.**
13. **SUP-PL-13 — `まよいウェルカム` is internally pre-V24, but V24 outcomes remain unavailable to its characters.**
14. **SUP-PL-14 — Kizumonogatari insertions can RC V04 reader understanding but cannot erase V04 uncertainty.**
15. **SUP-PL-15 — `そして` has a strong one-year-later internal anchor; its 2017 release horizon remains distinct.**
16. **SUP-PL-16 — Collection-new 2024 stories are retrospective insertions.** Their internal placement controls diegetic state; V30 controls only the later publication horizon.
17. **SUP-PL-17 — `しのぶトゥナイト` may bridge V23 to V30 without proving every intermediate career/family step.**
18. **SUP-PL-18 — `なでこパスト` and `しのぶフューチャー` remain fine-chronology OPEN until locally anchored.**
19. **SUP-PL-19 — Supplementary evidence may strengthen ordinary relational continuity without becoming a hidden “true canon” that supersedes numbered novels.**
20. **SUP-PL-20 — Production/adaptation context is not automatically diegetic fact.**
21. **SUP-PL-21 — A source's later availability does not make its internal event later in story chronology.**
22. **SUP-PL-22 — A source's earlier internal event does not make it earlier in publication-local reader knowledge.**
23. **SUP-PL-23 — Exact chronology remains UA where the short itself does not supply a defensible anchor.**
24. **SUP-PL-24 — No supplementary claim enters L01–L09 from this placement audit alone.** Claim admission requires controlled deep reading and locator-grade evidence.
## 14. What this audit authorizes next

### 14.1 `佰物語`

The source is now sufficiently placed for a dedicated deep reading.

Recommended artifact:

`MONOGATARI_V2_SUPP_HYAKUMONOGATARI_DEEP_READING.md`

That reading should prioritize:

- voice models;
- address-term matrix;
- pairwise conversational grammar;
- ordinary school-life relation;
- repeated jokes/routines;
- locally explicit mundane biography;
- contradictions against V01–V06 and later voice development.

It should not spend disproportionate effort trying to turn 100 topic sketches into a hidden plot.

### 14.2 `短物語`

Recommended later artifact:

`MONOGATARI_V2_SUPP_MIJIKANAMONOGATARI_DEEP_READING.md`

It should preserve all 39 story IDs and explicitly use **first-release horizon + internal horizon**. The five guidebook stories should be analyzed as dual-witness texts inside that artifact rather than duplicated into a second full deep reading.

### 14.3 Guidebook EPUB

No standalone full deep-reading artifact is recommended at present because its supplied fiction is fully crosswalked to SHORT-001–005. Its analytical responsibility is **earliest-witness comparison and release-local wording control**, which belongs in the `短物語` deep reading and eventual evidence crosswalk.

Creating a second five-story “guidebook deep reading” would produce near-duplicate semantic responsibility without adding a distinct corpus function.
## 15. Required ledger behavior during later admission

When controlled supplementary deep readings begin:

- L01 receives both first-release placement and internal chronology, not one merged date;
- L02 receives narrator/focalizer or direct-dialogue ensemble state;
- L03 receives oddity rules only when the source class permits and evidence is strong enough;
- L04/L05 receive character and relationship continuity with source-class labels;
- L06 records specialist claims with source ceiling visible;
- L07 records bodily/material evidence where applicable;
- L08 records source-specific Japanese wording and witness differences;
- L09 records any numbered-claim transition as PRESERVE/STRENGTHEN/REVISE/DOWNGRADE/REJECT/OPEN.

Supplement-specific evidence identifiers should remain traceable to story IDs (`SHORT-xxx`, `HYAKU-xxx`, `GUIDE-xxx`) so a later synthesis never loses which supplementary witness supplied the claim.
## 16. Bibliographic verification ledger

The following dates were checked against official publisher/franchise sources where available; supplied EPUB internal notices remain separately recorded rather than overwritten.

| Item | Verified publication/release datum | Verification class |
|---|---|---|
| `佰物語` | internal first print 2009-07-29; Kodansha commercial release 2009-08-04 | internal source + official publisher |
| `化物語 アニメコンプリートガイドブック` | 2010-10-28 | official Kodansha |
| `偽物語 アニメコンプリートガイドブック` | 2012-09-28 | official Kodansha |
| `化物語［入門編］` | 2013-09-13 | official Kodansha |
| `化物語 PremiumアイテムBOX` | 2013-11-22 | official Kodansha |
| Heroine Book 5 Hitagi | 2014-04-02 | official Kodansha |
| `鬼物語` BD first volume | 2014-04-23 | official franchise / Aniplex product record |
| `鬼物語` BD second volume | 2014-05-28 | official franchise / Aniplex product record |
| Heroine Book 6 Suruga | 2014-09-19 | official Kodansha |
| `偽物語 PremiumアイテムBOX` | 2014-11-21 | official Kodansha |
| Heroine Book 7 Fire Sisters | 2015-07-09 | official Kodansha |
| MADOGATARI Tokyo exhibition context | 2015-11-27 onward | official exhibition/franchise record |
| Heroine Book 8 Yotsugi | 2015-12-23 | official Kodansha |
| Kizumonogatari Visual Book PART2 | 2017-01-14 | official Kodansha |
| `結物語` | 2017-01-12 | official Kodansha; establishes V23 was already public for the 2017-01-14 shorts |
| `西尾維新祭2016 SPECIAL FANBOOK` | March 2017 distribution; secondary catalog records 2017-03-01 | campaign context official; exact distribution day medium confidence |
| `西尾維新の挑戦状` AnimeJapan event | 2017-03-26 | official festival/event record |
| Kizumonogatari COMPLETE GUIDE BOOK | 2017-11-29 | official Kodansha |
| `短物語` | paper 2024-09-11; electronic 2024-09-10 | official Kodansha |
| `なでこパスト` / `しのぶフューチャー` | official Off & Monster Season website, 2024 project context; exact posting day not recovered in this audit | official franchise; day OPEN |

This table is bibliographic/provenance evidence. It does not itself establish internal-story chronology.
## 17. Audit closeout

### 17.1 Placed corpus

- `短物語`: **PLACED at story level**, 39 independent first-release coordinates, narrator map, internal-position confidence, and revision ceilings established.
- `佰物語`: **PLACED at work and 100-unit voice/index level**, post-V06/pre-V07 release horizon, non-continuous high-school topic-sketch chronology, hybrid-script authority ceiling established.
- `化物語 アニメコンプリートガイドブック`: **PLACED as earliest-release dual witness** for SHORT-001–005; no independent corroboration count.

### 17.2 Live-authority state

This audit creates **source-placement authority only**.

It does **not** change:

- L01–L09 current evidence boundary: **V30 / C729**;
- numbered-volume authority: **V01–V30**;
- frozen Final / Off / Monster checkpoints;
- the V30 Family source-boundary checkpoint;
- any existing claim solely because a supplementary source exists.

### 17.3 Next architecture-defined artifact

`MONOGATARI_V2_SUPP_HYAKUMONOGATARI_DEEP_READING.md`

Reason: `佰物語` is the earliest supplementary source in publication order (post-V06/pre-V07), has now been fully placed at source/unit level, and has a distinct analytical responsibility not duplicated by the 39 prose shorts.
