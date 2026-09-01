---
title: "Gakuen Idolmaster V2 - Audiovisual Source Crosswalk"
project: "Gakuen Idolmaster"
document_type: "persistent ledger"
version: "2.4"
source_lock: "GAKUMAS V2 Source Lock 1.0"
initialized: "2026-08-13"
last_updated: "2026-08-22 — Rinami crosswalk closed at integrated AV R2; 13/13 character baselines complete"
status: "active; Phase-3 character audiovisual crosswalk complete at 13/13"
---

# AUDIOVISUAL SOURCE CROSSWALK

This is a cumulative V2 project ledger. It is initialized in Phase 0 and must be updated rather than recreated as later phases add evidence.

## Schema

| field | meaning |
| --- | --- |
| AV_source_id |  |
| internal_source_id |  |
| character |  |
| story_state |  |
| official_or_UI_title |  |
| community_title |  |
| distinctive_Japanese_anchor |  |
| public_metadata_source |  |
| supplied_raw_file |  |
| verification_status |  |

## Seed entries

No substantive entries are asserted at Phase 0. The schema is intentionally initialized before close reading so later evidence can be added without changing data conventions.

## Phase 3 — Saki machine/human audiovisual crosswalk

### Music and MV objects

| AV ID | human-facing title | Japanese title | internal story anchors | official/public identity | supplied-file naming target | verification |
| --- | --- | --- | --- | --- | --- | --- |
| AV-MUS-SAKI-001 | Fighting My Way | `Fighting My Way` | `adv_cidol-hski-3-000_01..03` | official 1st single / official MV / streaming entry | `AV-MUS-SAKI-001_Fighting_My_Way_official_MV.*` | AV supplied and inspected |
| AV-MUS-SAKI-002 | Boom Boom Pow | `Boom Boom Pow` | later repertoire audit; no unique direct ADV story claim fixed | official 2nd-single lead track | `AV-MUS-SAKI-002_Boom_Boom_Pow.*` | AV supplied and inspected |
| AV-MUS-SAKI-003 | EGO | `EGO` | external image-song layer; no unique direct ADV story claim fixed | official 2nd-single track / official MV collection | `AV-MUS-SAKI-003_EGO_official_MV.*` | AV supplied and inspected |
| AV-MUS-SAKI-004 | Campus mode!! Saki Solo | `Campus mode!! [花海咲季 Solo ver.]` | `adv_cidol-hski-3-008_01..03` | official 1st-single track | `AV-MUS-SAKI-004_Campus_mode_Saki_Solo.*` | AV supplied and inspected |
| AV-MUS-SAKI-005 | Wildest Flower | `Wildest Flower` | `adv_dear_hski_028..036`; `cidol 017` | STEP3 streaming/MV; official 3rd-single lead | `AV-MUS-SAKI-005_Wildest_Flower_official_MV.*` | AV supplied and inspected |
| AV-MUS-SAKI-006 | Gamushara ni Ikou! Saki Solo | `がむしゃらに行こう！ [花海咲季 Solo ver.]` | `adv_cidol-hski-3-015_01..03` | official 2nd-single track | `AV-MUS-SAKI-006_Gamushara_Saki_Solo.*` | AV supplied and inspected |
| AV-MUS-SAKI-007 | Saki H.I.F. prescribed song | `ガラクタロード` | P3/D-SAKI final; `adv_cidol-hski-3-018_*` variant discussion | transcript/game performance identity | `AV-MUS-SAKI-007_Garakuta_Road_Saki_HIF.*` | AV supplied and inspected |
| AV-MUS-SAKI-008 | GO MY WAY!! Saki | `GO MY WAY!!` | `adv_cidol-hski-3-019_01..03` | inherited franchise song / game performance | `AV-MUS-SAKI-008_GO_MY_WAY_Saki.*` | AV supplied and inspected |
| AV-MUS-SAKI-009 | Hajime Saki Solo | `初 [花海咲季 Solo ver.]` | P1 institutional state | official 1st-single track | `AV-MUS-SAKI-009_Hajime_Saki_Solo.*` | AV supplied and inspected |
| AV-MUS-SAKI-010 | Endless Dance Saki Solo | `ENDLESS DANCE [花海咲季 Solo ver.]` | later title/succession context | official 3rd-single announced track | `AV-MUS-SAKI-010_ENDLESS_DANCE_Saki_Solo.*` | AV supplied and inspected |
| AV-MUS-SAKI-011 | Ameagari no Iris | `雨上がりのアイリス` | U1/Re;IRIS track | official Re;IRIS single/MV | `AV-MUS-SAKI-011_Ameagari_no_Iris_ReIRIS.*` | AV supplied and inspected; unit synthesis pending |

### Dialogue objects

| AV ID | internal ID | human description | exact Japanese search anchors | supplied-file naming target | priority |
| --- | --- | --- | --- | --- | --- |
| AV-DIA-SAKI-001 | `adv_dear_hski_023.txt` | private aftermath of Ume's summer-H.I.F. victory | `最後まで、お姉ちゃんらしく振る舞えていたかしら`; `はじめて――……妹に負けちゃった`; `あなたの選択を、わたしが正解にしてみせる` | `AV-DIA-SAKI-001_adv_dear_hski_023.*` | P0 |
| AV-DIA-SAKI-002 | `adv_dear_hski_027.txt` | weakest Saki wins; Producer defines indomitability | `もっとも弱い花海咲季`; `不屈とは、倒れないことでも、折れないことでもありません`; `折れた心だって燃え上がらせる` | `AV-DIA-SAKI-002_adv_dear_hski_027.*` | P1 |
| AV-DIA-SAKI-003 | `adv_cidol-hski-3-018_01.txt` | quiet reciprocal admission of Producer/Saki weakness | internal ID plus adjacent opening lines from source bundle | `AV-DIA-SAKI-003_adv_cidol_hski_3_018_01.*` | P1 |
| AV-DIA-SAKI-004 | `adv_dear_hski_035.txt` | Producer's dream overwritten by Saki | `花海咲季で塗りつぶされてしまった`; `アイドルを輝かせる、期待っていうのよ`; `夢を見せた責任、とってあげる` | `AV-DIA-SAKI-004_adv_dear_hski_035.*` | P1 |
| AV-DIA-SAKI-005 | `adv_dear_hski_036.txt` | Prima Stella victory speech/open challenge | `これで終わりじゃないわよね`; `全員わたしについてきなさい`; `お姉ちゃんが先陣を切るわ` | `AV-DIA-SAKI-005_adv_dear_hski_036.*` | P1 |
| AV-DIA-SAKI-006 | `adv_cidol-hski-3-000_03.txt` | fear of Ume seeing the weak Saki before Fighting My Way | `実は情けないお姉ちゃんなんだってばれたら`; `ありのままの咲季さんは、弱気で見栄っ張りで強がってばかりですが`; `心のままに、不屈と勝利を歌ってくるわ` | `AV-DIA-SAKI-006_adv_cidol_hski_3_000_03.*` | P1 |


### Supplied Saki AV objects resolved

| AV identity | supplied public/whole-file identity | exact internal crosswalk | resolution |
| --- | --- | --- | --- |
| FMW commu | `【楽曲コミュ】Fighting My Way【花海咲季】【学マス】` | `adv_cidol-hski-3-000_01..03`; requested scene `_03` | inspected |
| Garakuta commu | `【ガラクタロード】花海咲季 楽曲コミュまとめ` | `adv_cidol-hski-3-018_01..03`; requested scene `_01` | inspected |
| STEP3 compilation | `花海咲季 親愛度コミュ21～27話まとめ【STEP3】` | Dear 023 and Dear 027 | inspected |
| STEP4 compilation | `花海咲季 親愛度コミュ28～37話まとめ【H.I.F編】【STEP4】` | Dear 035 and Dear 036 | inspected |
| music/MV registry | 15 supplied music/MV files representing 11 work identities | `AV-MUS-SAKI-001..011` | inspected |

The exact byte sizes, hashes, codecs, resolutions, and durations are preserved in `GKM_PHASE3_SAKI_AUDIOVISUAL_SOURCE_MANIFEST.json`.
## Phase 3 — Temari public-search crosswalk (pending acquisition)

| human-facing identity | uploader-facing search/title | internal source | state |
| --- | --- | --- | --- |
| Temari affection 1–10 | `月村手毬 親愛度コミュ1～10話まとめ` | Dear 004, 009, 010 among packet | requested |
| Temari affection 11–20 / N.I.A. | `月村手毬 親愛度コミュ11～20話まとめ N.I.A` | Dear 015–017, 019–020 | requested |
| Temari affection 21–27 / STEP3 | `月村手毬 親愛度コミュ21～27話まとめ STEP3` | Dear 022, 023, 027 | requested |
| Temari affection 28–37 / H.I.F. | `月村手毬 親愛度コミュ28～37話まとめ H.I.F STEP4` | Dear 035–037 | requested |
| `Luna say maybe` commu | `【楽曲コミュ】Luna say maybe【月村手毬】【学マス】` | `adv_cidol-ttmr-3-000_01..03` | requested |
| STEP3 song commu | `月村手毬「一体いつから」楽曲コミュ` | `adv_cidol-ttmr-3-016_01..03` | probable identity; verify on acquisition |
| `ガラクタロード` commu | `【ガラクタロード】月村手毬 楽曲コミュまとめ` | `adv_cidol-ttmr-3-018_01..03` | requested |
| `Campus mode!!` commu | `月村手毬 Campus mode 楽曲コミュ` | `adv_cidol-ttmr-3-007_01..03` | secondary |
| `がむしゃらに行こう！` commu | `月村手毬 がむしゃらに行こう 楽曲コミュ` | `adv_cidol-ttmr-3-015_01..03` | secondary |
| music/MV registry | Temari six-work core + five supplemental works | `AV-MUS-TEMARI-001..011` | pending files |

## Phase 3 — Kotone public-search crosswalk

| human-facing identity | internal source | search anchor | state |
| --- | --- | --- | --- |
| Kotone affection 1–10 | Dear 001–010 | `藤田ことね 親愛度コミュ1～10話まとめ` | requested |
| Kotone affection 11–20 / N.I.A. | Dear 011–020 | `藤田ことね 親愛度コミュ11～20話まとめ N.I.A` | requested |
| Kotone affection 21–27 / STEP3 | Dear 021–027 | `藤田ことね 親愛度コミュ21～27話まとめ STEP3` | requested |
| `世界一可愛い私` commu | `adv_cidol-fktn-3-000_01..03` | `藤田ことね 世界一可愛い私 楽曲コミュ` | requested |
| `Yellow Big Bang！` commu | `adv_cidol-fktn-3-001_01..03` | `藤田ことね Yellow Big Bang 楽曲コミュ` | requested |
| `White Night! White Wish!` commu | `adv_cidol-fktn-3-006_01..03` | `藤田ことね White Night White Wish 楽曲コミュ` | requested |
| `Campus mode!!` commu | `adv_cidol-fktn-3-007_01..03` | `藤田ことね Campus mode 楽曲コミュ` | requested |
| `雨上がりのアイリス` commu | `adv_cidol-fktn-3-011_01..03` | `藤田ことね 雨上がりのアイリス 楽曲コミュ` | requested; group performance already held |
| `自己肯定感爆上げ↑↑しゅきしゅきソング` commu | `adv_cidol-fktn-3-013_01..03` | `藤田ことね 自己肯定感爆上げ しゅきしゅきソング 楽曲コミュ` | requested |
| `がむしゃらに行こう！` commu | `adv_cidol-fktn-3-016_01..03` | `藤田ことね がむしゃらに行こう 楽曲コミュ` | requested |
| `GO MY WAY!!` commu | `adv_cidol-fktn-3-019_01..03` | `藤田ことね GO MY WAY 楽曲コミュ` | requested |


## Phase 3 — Mao public-search crosswalk

| human-facing identity | internal source | search anchor | supplied public file / state |
| --- | --- | --- | --- |
| Mao affection 1–10 | Dear 001–010 | `有村麻央 親愛度コミュ1～10話まとめ` | **STAGED/INSPECTED** — 1080p30 compilation |
| Mao post-010 / 親愛度10.5 | `adv_dear_amao_010-01` | `有村麻央 親愛度10.5 麻央 覚醒` | **STAGED/INSPECTED** — `麻央、覚醒【有村麻央】親愛度コミュ10.5話...` 1080p30 |
| Mao affection 11–20 / N.I.A. | Dear 011–020 | `有村麻央 親愛度コミュ11～20話まとめ N.I.A` | **STAGED/INSPECTED** — 720p30 compilation |
| Mao affection 21–27 | Dear 021–027 | `有村麻央 親愛度コミュ21～27話まとめ STEP3` | **STAGED/INSPECTED** — 480p30 compilation |
| Mao affection 28–37 / H.I.F. | Dear 028–037 | `有村麻央 親愛度コミュ28～37話まとめ H.I.F STEP4` | **STAGED/INSPECTED** — 480p30 compilation |
| `Fluorite` commu | `adv_cidol-amao-3-000_01..03` | `有村麻央 Fluorite 楽曲コミュ` | **STAGED/INSPECTED** — 1080p30 |
| summer dorm / `キミとセミブルー` commu | `adv_cidol-amao-3-001_01..03` | `有村麻央 キミとセミブルー 楽曲コミュ` | **STAGED/INSPECTED** — 1080p30 |
| `Feel Jewel Dream` commu | `adv_cidol-amao-3-002_01..03` | `有村麻央 Feel Jewel Dream 楽曲コミュ` | **STAGED/INSPECTED** — 1080p30 |
| `Campus mode!!` commu | `adv_cidol-amao-3-007_01..03` | `有村麻央 Campus mode 楽曲コミュ` | **STAGED/INSPECTED** — 1080p60 |
| Hinamatsuri / `雪解けに` commu | `adv_cidol-amao-3-009_01..03` | `有村麻央 雪解けに 楽曲コミュ` | **STAGED/INSPECTED** — 1080p30 |
| `ミラクルナナウ(ﾟ∀ﾟ)！` Mao commu / Osaka homecoming | `adv_cidol-amao-3-013_01..03` | exact uploader-facing title: `【楽曲コミュ】ミラクルナナウ(ﾟ∀ﾟ)！【有村麻央】【学マス】`; fallback `有村麻央 ミラクルナナウ 大阪編` | **STAGED/VERIFIED** — 1080p60, AAC-LC ~128 kbps, ~8:44; Osaka/child-actor/parents sequence confirmed |
| `見て` / Ryuugetsu Maki commu | `adv_cidol-amao-3-015_01..03` | `有村麻央 見て 楽曲コミュ` | **STAGED/INSPECTED** — 1080p60 |
| `SUGAR FLAVOR` commu | `adv_cidol-amao-3-017_01..03` | `有村麻央 姫崎莉波 SUGAR FLAVOR 楽曲コミュ` | **STAGED/INSPECTED** — 1080p60 |
| Mao `ガラクタロード` | P3 prescribed-song context | `有村麻央 ガラクタロード H.I.F` | **STAGED** — 1080p60 rendered performance |

**2026-08-17 Mao acquisition delta:** the expanded communication boundary is now **complete**: all eight Mao `cidol` sequences and the full Dear spine including 親愛度10.5 are staged. Song communications remain in the Dialogue/Commu source branch; authored MVs, rendered 3DMVs, and full-song objects remain in the separate Music/MV branch.

## Phase 3 - Lilja public-search crosswalk

| human-facing identity | internal source | primary public search anchor | state |
| --- | --- | --- | --- |
| Lilja affection 1-10 | Dear 001-010 | `Gakumas Katsuragi Lilja affection commu 1-10` | requested; Japanese query in dedicated request doc |
| Lilja affection 11-20 / N.I.A. | Dear 011-020 | `Gakumas Katsuragi Lilja affection commu 11-20 NIA` | requested |
| Lilja affection 21-27 / STEP3 | Dear 021-027 | `Gakumas Katsuragi Lilja affection commu 21-27 STEP3` | requested |
| Lilja affection 28-37 / H.I.F. | Dear 028-037 | `Gakumas Katsuragi Lilja affection commu 28-37 HIF` | requested |
| `Shiroisen` commu | `adv_cidol-kllj-3-000_01..03` | `Gakumas Shiroisen Katsuragi Lilja song commu` | requested |
| `Campus mode!!` commu | `adv_cidol-kllj-3-006_01..03` | `Gakumas Campus mode Katsuragi Lilja song commu` | requested |
| `Atmosphere` commu | `adv_cidol-kllj-3-015_01..03` | `Gakumas Atmosphere Katsuragi Lilja song commu` | requested |
| REVERSI / `Tokimeki Emotion` | `adv_cidol-kllj-3-017_01..03` | `Gakumas Tokimeki Emotion REVERSI commu` | requested |
| `Garakuta Road` Lilja | especially `adv_cidol-kllj-3-018_03` | `Gakumas Garakuta Road Katsuragi Lilja song commu` | requested |
| Producer-history commu | `adv_cidol-kllj-3-010_01..03` | story-description search; title unresolved | requested P1 |
## Phase 3 — China public-search crosswalk and acquired-source closure

| human-facing identity | internal source | primary public search anchor | final state |
| --- | --- | --- | --- |
| China 親愛度 1–10 | Dear 001–010 | `学マス 倉本千奈 親愛度コミュ 1～10` | COMPLETE — Drive `1qB3EZXT46_teGexgHuk26rtYvPaZjPnJ` |
| China 親愛度 11–20 / N.I.A. | Dear 011–020 | `学マス 倉本千奈 親愛度コミュ 11～20 NIA` | COMPLETE — Drive `1A01BzommAVx79yDZIOmmI5WWzUq2AQ3z` |
| China 親愛度 21–27 / STEP3 | Dear 021–027 | `学マス 倉本千奈 親愛度コミュ 21～27 STEP3` | COMPLETE — Drive `1smRVO5UvSeYn1lYmSXnaNWTE_nPhJPFC` |
| China 親愛度 28–37 / H.I.F. | Dear 028–037 | `学マス 倉本千奈 親愛度コミュ 28～37 HIF` | COMPLETE — Drive `1BP3QbrYCASrYDsGVLESp7NVPo6aJHIc2` |
| `Wonder Scale` commu | `adv_cidol-kcna-3-000_01..03` | `学マス Wonder Scale 倉本千奈 楽曲コミュ` | COMPLETE — Drive `1c1k-nX0Ld76TLOmNJ16TrdoijJjCgFwN` |
| `日々、発見的ステップ！` commu | `adv_cidol-kcna-3-001_01..03` | `学マス 日々、発見的ステップ！ 倉本千奈 楽曲コミュ` | COMPLETE — Drive `143z8j5zrzTmpKL42OMjZ6mHGJTtQKdpl` |
| `Campus mode!!` commu | `adv_cidol-kcna-3-007_01..03` | `学マス Campus mode!! 倉本千奈 楽曲コミュ` | COMPLETE — Drive `1O3nx5Lw6MrAGiIfIXT4YHvW29qaAcM3H` |
| `雪解けに` family/Kanae commu | `adv_cidol-kcna-3-009_01..03` | `学マス 雪解けに 倉本千奈 楽曲コミュ` | COMPLETE; public-title mapping resolved — Drive `1LBaT5Ei7ND3qALQB22YwTqtc-YgJvUdc` |
| `空と約束` / STEP3 new-song commu | `adv_cidol-kcna-3-014_01..03` | `学マス 空と約束 倉本千奈 楽曲コミュ` | COMPLETE; title mapping directly verified — Drive `1fymSECYmKq4OOOGgkNUUfb_8cZGgvmBy` |
| ゆめぱしー `みちなるひろがる` | `adv_cidol-kcna-3-016_01..03` | `学マス みちなるひろがる ゆめぱしー コミュ` | COMPLETE — Drive `1cmKCgdek46iLWjcatXz7jhKIubJ0Kvfp` |

Canonical audiovisual source home: `VIDEO/06_KURAMOTO_CHINA` — Drive `1Dga2iSgb1O2o0wlXQ5zMeXCZBDNtyZCk`. Full 22-file technical identity, filename, duration and SHA-256 routing is governed by `GKM_PHASE3_CHINA_AUDIOVISUAL_SOURCE_MANIFEST.json` — Drive `1Sxn-q5KegPjQMcDmF0xLX2EKsHJYNdhT`.

## Phase 3 — Hiro public-search crosswalk

| human-facing identity | internal source | primary public search anchor | state |
| --- | --- | --- | --- |
| Hiro 親愛度 1–10 | Dear 001–010 | `学マス 篠澤広 親愛度コミュ 1～10 まとめ` | requested |
| Hiro 親愛度 11–20 / N.I.A. | Dear 011–020 | `学マス 篠澤広 親愛度コミュ 11～20 NIA` | requested |
| Hiro 親愛度 21–27 / STEP3 | Dear 021–027 | `学マス 篠澤広 親愛度コミュ 21～27 STEP3` | requested |
| Hiro 親愛度 28–37 / H.I.F. | Dear 028–037 | `学マス 篠澤広 親愛度コミュ 28～37 HIF` | requested |
| `光景` | earliest solo-song communication likely cidol 000 pending public alignment | `学マス 光景 篠澤広 楽曲コミュ` | title verified; internal episode mapping to verify on acquired file |
| `コントラスト` | public song; internal commu mapping to resolve on acquisition | `学マス コントラスト 篠澤広 楽曲コミュ` | requested |
| `サンフェーデッド` | public song; late-route comparator | `学マス サンフェーデッド 篠澤広 楽曲コミュ` | requested |
| `Campus mode!!` | `adv_cidol-shro-3-007_01..03` | `学マス Campus mode!! 篠澤広 楽曲コミュ` | requested; title explicit in source |
| retrospective `かわいくなりたかった` commu | `adv_cidol-shro-3-018_01..03` | title search first; fallback `学マス 篠澤広 かわいくなりたかった コミュ` | requested; public title unresolved |

## Rinami AV source crosswalk — requested, not yet inspected

| analytical object | human-facing retrieval identity | internal textual key | priority | state |
| --- | --- | --- | --- | --- |
| foundational solo | `clumsy trick / 姫崎莉波` | CIDOL 000 | P0 | REQUESTED |
| second solo | `L.U.V / 姫崎莉波` | exact internal song-commu mapping OPEN | P1 | REQUESTED |
| STEP3 solo | `36℃ U･B･U / 姫崎莉波` | CIDOL 013 | P0 | REQUESTED |
| inherited school song | `Campus mode!! / 姫崎莉波` | CIDOL 007 | P1 | REQUESTED |
| shared forceful song | `Howling over the World / 姫崎莉波` | CIDOL 012 | P1 | REQUESTED |
| H.I.F. theme | `ガラクタロード / 姫崎莉波` | CIDOL 017 | P1 | REQUESTED |
| peer duo | `SUGAR FLAVOR / RippleSign / 姫崎莉波・有村麻央` | CIDOL 018 | P1 | REQUESTED |
| supplementary original | `歌声は君いろ / 姫崎莉波` | official title; commu mapping not asserted | P1 | OPTIONAL |
| Dear STEP1 | `姫崎莉波 親愛度コミュ1～10話まとめ【STEP1】` | Dear 001–010 + 010-01 | P0 | REQUESTED |
| Dear STEP2/NIA | `姫崎莉波 親愛度コミュ11～20話まとめ【STEP2 / N.I.A.】` | Dear 011–020 | P0 | REQUESTED |
| Dear STEP3 | `姫崎莉波 親愛度コミュ21～27話まとめ【STEP3】` | Dear 021–027 | P0 | REQUESTED |
| Dear STEP4/HIF | `姫崎莉波 親愛度コミュ28～37話まとめ【STEP4 / H.I.F.】` | Dear 028–037 | P0 | REQUESTED |

See canonical request packet: `GKM_RINAMI_AUDIOVISUAL_BASELINE_AND_REQUESTS.md`.

## Sumika AV source crosswalk — integrated baseline complete

| layer | supplied / canonical source | internal crosswalk | priority | status |
| --- | --- | --- | --- | --- |
| foundational solo | `Tame-Lie-One-Step` official MV + 3DMV + song commu | CIDOL 000 | P0 | CLOSED — INSPECTED |
| second solo | `カクシタワタシ` full released audio + 3DMV + song commu | CIDOL 002 | P0 | CLOSED — INSPECTED; **no authored official MV asserted** |
| STEP3 solo | `Love & Joy` official MV + 3DMV + song commu | CIDOL 012 | P0 | CLOSED — INSPECTED |
| REVERSI unit | `ときめきエモーション` official MV + REVERSI 3DMV + song commu | CIDOL 017 + D-SUMIKA/D-LILJA | P0 | CLOSED — INSPECTED |
| inherited school song | `Campus mode!! [紫雲清夏]` 3DMV + song commu | CIDOL 007 | P1 | CLOSED — INSPECTED |
| supplementary original | `Kira Kira` official MV | exact commu mapping not asserted | P1 | CLOSED — BREADTH INSPECTED |
| common-song breadth | `がむしゃらに行こう！`, `Howling over the World`, `ミラクルナナウ(ﾟ∀ﾟ)！` 3DMVs | shared repertoire | P1 | CLOSED — BREADTH INSPECTED |
| Dear STEP1 | `紫雲清夏 親愛度コミュ1～10話` | Dear 001–010 + 010-01 | P0 | CLOSED — DIRECTLY INSPECTED |
| Dear STEP2/NIA | `紫雲清夏 親愛度コミュ11～20話` | Dear 011–020 | P0 | CLOSED — DIRECTLY INSPECTED |
| Dear STEP3 | `紫雲清夏 親愛度コミュ21～27話` | Dear 021–027 | P0 | CLOSED — DIRECTLY INSPECTED |
| Dear STEP4/HIF | `紫雲清夏 親愛度コミュ28～37話` | Dear 028–037 | P0 | CLOSED — DIRECTLY INSPECTED via equivalent 720p30 direct-upload materialization; oversized Drive original remains provenance |

Backfill note — 2026-08-17: the logical Dear 028–037 source remains Drive `1GDVAt5evYW4KoNAxLcZW5r3-u8qkW1Vn` (549,927,147-byte provenance object). Direct inspection used the equivalent 720p30/AAC-LC chat-upload materialization (195,093,333 bytes; SHA-256 `d95d80b4df9e104b4ed8a9c6f1c3c612f5907260f2e7b426eecafb537601a591`). This closes the former late acted-source gap without increasing the logical source count.

Canonical AV authority: `GKM_SUMIKA_COMPLETE_AUDIOVISUAL_BASELINE.md`. The old request packet is superseded provenance.

## Phase 3 Kotone source crosswalk — 2026-08-15

| layer | canonical source/home | scope/use |
| --- | --- | --- |
| staged songs/MVs/3DMVs | source root `3DMV and Songs/Kotone` — Drive folder `1vUlGpnLCt9zOiMdnaM0FObR1Iixp1Nb2` | 15 Kotone music/performance objects |
| staged commus | source root `Commus and Dialogue/Kotone` — Drive folder `1zVoR56SE0aAquEhkB_tOY8yvyyNY3Iss` | 11 Kotone whole commu objects |
| reused group performance | Re;IRIS `雨上がりのアイリス` — Drive `1YA2Z6qmQ-A9Bc8KMzTR5Oej9hV7KTGNz` | U1 distributed-focality comparison |
| exact song-commu control | `03_idol_communications.dialogue.txt` — Drive `1ddB7hr6IR6E4QaW67ikyOZ3n015KxFgo` | complete Kotone modular song-commu text |
| exact longitudinal control | `04_dear_idol.dialogue.txt` — Drive `1wUe9NuGF-96BLOsluxy4nKK6mj32Haw7` | complete Dear 1–27 text |
| source manifest | `GKM_PHASE3_KOTONE_AUDIOVISUAL_SOURCE_MANIFEST.json` — Drive `1rowv9DYPElYiV9RzvkogluB7zFQJ9NI8` | IDs, filenames, hashes, ffprobe, metrics, availability state |
| integrated analysis | `GKM_KOTONE_COMPLETE_AUDIOVISUAL_BASELINE.md` — Drive `1-fH6a0kyr-rkfRwJZFm0tHzQB2wtkkku` | governing Phase-3 AV interpretation |
| voice specialist | `GKM_KOTONE_DIALOGUE_VOICE_ACTING_CLOSE_READING.md` — Drive `1PxIQMjD4yPQKZIRAFBLP1foLA5GMJtOj` | acted register/longitudinal analysis |
| music specialist | `GKM_KOTONE_MUSIC_MV_AND_PERFORMANCE_CLOSE_READING.md` — Drive `1eSyTmXH8p_bnYmyrcEc9FbNUa0PBKuF8` | song, MV, 3DMV and repertoire analysis |
| unavailable exact comparator | Kotone `ガラクタロード` commu/3DMV | `OPEN-SOURCE`; do not infer from Saki/Temari versions |

## Hanami Ume — completed integrated AV crosswalk — 2026-08-19

Current authority: `GKM_UME_COMPLETE_AUDIOVISUAL_BASELINE.md` — Drive `1p-MzTVcTZ_Mercqc3WxHqXi1m8UwO7bV`. Historical acquisition register: Drive `1e3jV2sDoyyRMqUE5vSVMtEa3-7iGnuJa`; **superseded / do not use as current authority**.

Canonical source root: `VIDEO/10_HANAMI_UME` — Drive `1HjfDqEL12trHfV3gUMiwy52WI8Ns19Q0`. Canonical AV analysis home: Drive `1esibxxb2TD9RpSX3bsROE5Q4JHwL2HWY`.

| source ID | Drive ID | human-facing identity | canonical video folder | status |
| --- | --- | --- | --- | --- |
| `AV-UME-001` | `1px35YzmjVoIU78fuTRv3Zl2uXVIaHSd3` | Dear 001–010 compilation | `01_DEAR_ROUTE` | INSPECTED |
| `AV-UME-002` | `15bVizFZ9E9B-753sRleWPWl1rtZs4_yn` | Dear 011–020 compilation | `01_DEAR_ROUTE` | INSPECTED |
| `AV-UME-003` | `1ZJb5vRxCgzNy1X9nod-vlOIP9NUWECJ2` | Dear 021–027 compilation | `01_DEAR_ROUTE` | INSPECTED |
| `AV-UME-004` | `1B0M_2h4OalboPH5nyPTRznPSAgAjQEcW` | Dear 028–037 compilation | `01_DEAR_ROUTE` | INSPECTED |
| `AV-UME-005` | `1y7wQiV_EvUnM0HGSjC096djouF1W5vX-` | `The Rolling Riceball` song commu | `03_SONG_COMMUS` | INSPECTED |
| `AV-UME-006` | `1Lnb0F8tLLYu81k74VOfnZmdlMZ5mEX0-` | `グースーピー` song commu | `03_SONG_COMMUS` | INSPECTED |
| `AV-UME-007` | `1uzsjWQoSfl0EBsh8SkkjZJ1AFPwg0Yg5` | `真っ白いページと水彩の主人公` song commu | `03_SONG_COMMUS` | INSPECTED |
| `AV-UME-008` | `1PwyyN_u0c_7BCGaC0vJu53GN9AUdQCeE` | `Campus mode!!` song commu | `03_SONG_COMMUS` | INSPECTED |
| `AV-UME-009` | `1bpgJbU_aOdvO-Xea5p5tKveAcn-dJH6j` | `GO MY WAY!!` song commu | `03_SONG_COMMUS` | INSPECTED |
| `AV-UME-010` | `1m1YVGoWzVCrOpyMGV7wtM7R6dgcst1Ps` | `The Rolling Riceball` 3DMV | `04_MV_3DMV_AND_PERFORMANCE` | INSPECTED |
| `AV-UME-011` | `1yYvY6KwPdt8oyP7NwSRkJ2cUhKsCbNAW` | `The Rolling Riceball` official MV | `04_MV_3DMV_AND_PERFORMANCE` | INSPECTED |
| `AV-UME-012` | `1heKNzinpdTIidaVtWFDolKFXYDtU8Q2W` | `グースーピー` 3DMV | `04_MV_3DMV_AND_PERFORMANCE` | INSPECTED |
| `AV-UME-013` | `1-snA3qhHC8fRQlkrCKQDDr4XUS_LNLVM` | `グースーピー` complete-song asset | `04_MV_3DMV_AND_PERFORMANCE` | INSPECTED |
| `AV-UME-014` | `1mMPoCM6BxEh-FHPeCBQfeQq1HucFWqhS` | `真っ白いページと水彩の主人公` official MV | `04_MV_3DMV_AND_PERFORMANCE` | INSPECTED |
| `AV-UME-015` | `10l8cob-lmo-1g7A5KDfcmA6tx42tU2NI` | `Campus mode!!` Ume 3DMV | `04_MV_3DMV_AND_PERFORMANCE` | INSPECTED |
| `AV-UME-016` | `1HFVKsVdhJq5uEIqmNX9SyZc9ETTUIyE4` | `GO MY WAY!!` Ume 3DMV | `04_MV_3DMV_AND_PERFORMANCE` | INSPECTED |
| `AV-UME-017` | `1oBtWcbACnd5eymX1Avj_b4fhTH5A4lmf` | `つよつよ最強エクササイズ` official lyric video | `04_MV_3DMV_AND_PERFORMANCE` | INSPECTED |
| `AV-UME-018` | `1KRd0cLcCGn53lbuawpu2affoXAyHLjix` | `つよつよ最強エクササイズ` complete-song asset | `04_MV_3DMV_AND_PERFORMANCE` | INSPECTED |
| `AV-UME-019` | `19LxPYQCrsd4VI0Xjwvy9xOVrX70R5TdB` | `ENDLESS DANCE` Ume 3DMV | `04_MV_3DMV_AND_PERFORMANCE` | INSPECTED |
| `AV-UME-020` | `1-mghCIkRHuDPI06Mo7JSeF3XRC-tYYFb` | `Howling over the World` Ume 3DMV | `04_MV_3DMV_AND_PERFORMANCE` | INSPECTED |
| `AV-UME-021` | `1lbp2DWiDLBRNOTc6QcE7yPh9Qb7nFy6W` | `ミラクルナナウ(ﾟ∀ﾟ)！` Ume 3DMV | `04_MV_3DMV_AND_PERFORMANCE` | INSPECTED |

Source boundary: **21 canonical logical objects / 16,654.163 seconds / 4.626 hours / 2,097,560,948 bytes**. Complete technical metadata and SHA-256 hashes live in `GKM_PHASE3_UME_AUDIOVISUAL_SOURCE_MANIFEST.json` — Drive `1DOOKkdLf8_rWhGVGN22DpVTgLc7t9fib`.

A 2160p `The Rolling Riceball` capture (Drive `12UswhS3XfELuboQMZFtUQzXRu9JwUeRE`) is retained as a noncounted resolution duplicate. The matching 1080p60 object `AV-UME-010` was fully materialized, hashed, and inspected; no evidentiary gap follows from the connector's 256 MiB transfer ceiling.

## Hataya Misuzu — textual-to-AV crosswalk

| textual claim cluster | requested AV source | verification target | status |
| --- | --- | --- | --- |
| gentle surface / enormous appetite | Dear 1–10 + `ツキノカメ` | acoustic and facial coexistence of softness and capture rhetoric | REQUESTED |
| Temari containment → conflict → rivalry | Dear 6–10 and late Dear | addressee-specific voice/body changes | REQUESTED |
| Rinha separate-road friendship | Dear 11–20 | whether old-unit intimacy survives without reunion staging | REQUESTED |
| defeat pain / stored resentment | Dear 21–27 | public composure versus private vocal fracture | REQUESTED |
| night-sky sovereignty / Prima Stella | Dear 28–37 + `VEIL` / `Superlative` | celestial image, command, tears, open-future staging | REQUESTED |
| unit plurality | Begrazia `Star-mine` + Ume/Sena shared performance | center distribution and non-SyngUp unit identity | REQUESTED |
| permanent becoming | `VEIL` | arrangement/choreography/camera progression rather than fixed completed icon | REQUESTED |

## Juo Sena / 十王星南 Phase 3 crosswalk

| internal source family | public identity / search target | confidence | note |
| --- | --- | --- | --- |
| `adv_dear_jsna_001`-`010` | `学マス 十王星南 親愛度 1-10` | high | request one complete compilation |
| `adv_dear_jsna_011`-`020` | `学マス 十王星南 親愛度 11-20` | high | request one complete compilation |
| `adv_dear_jsna_021`-`027` | `学マス 十王星南 親愛度 21-27 HIF` | high | request one complete compilation |
| `adv_cidol-jsna-3-000_*` | `小さな野望` song commu | high | foundational solo |
| `adv_cidol-jsna-3-002_*` | `Campus mode!!` Sena commu | high | academy/family inheritance |
| `adv_cidol-jsna-3-003_*` | Valentine / `ハッピーミルフィーユ` packet | medium/high | source narrative and commercial song relation should be inspected directly |
| `adv_cidol-jsna-3-006_*` | `Our Chant` song commu | high | institutional address |
| `adv_cidol-jsna-3-011_*` | dream-unit construction; `Choo Choo Choo` candidate | provisional | do not collapse to named-song identity until public source confirms |
| `adv_cidol-jsna-3-015_*` | `赤裸々` song commu | high | STEP3 / exposure |
| `adv_cidol-jsna-3-016_*` | `ENDLESS DANCE` song commu | high | Sena/Ume/Misuzu shared context |
| Begrazia material | `Star-mine` MV/3DMV/commu | high official metadata | group focality |

Preferred Japanese search vocabulary: `親愛度コミュ`, `楽曲コミュ`, `プロデュースコミュ`, `3DMV`, `Solo ver.`, `全話`.

## Amaya Tsubame — completed integrated AV crosswalk — 2026-08-18

Current authority: `GKM_TSUBAME_COMPLETE_AUDIOVISUAL_BASELINE.md` — Drive `1OubUGaGvDwihXTFYbcft47uYYCc7zH50`. Historical acquisition register: Drive `1suCai5rq41r_paMGM7ZRyqSSW-e5iVmi`; **superseded / do not use as current authority**.

Canonical source root: `VIDEO/13_AMAYA_TSUBAME` — Drive `1QQD0Hzx31TFQwuFIaoiIQ2mOTa5Tpb14`. Canonical AV analysis home: Drive `1Uoc7z2Vg9U0xtMDpl1J-JCli1p9yX2Kj`.

| Drive ID | supplied title / object | source type | canonical analytical role | status |
|---|---|---|---|---|
| `1ZrBWq6qUu9vcWiFedI5DjodIg9agP_8s` | 親愛度0.5 / Dear 000 | Dear scene | pre-recruitment public/institutional baseline | INSPECTED |
| `1jluj7G5vkC0hoNgv1X84AYf7DMK8-Uex` | 親愛度1–10 | Dear compilation | shell-breaking, Misuzu loss, first Sena victory, childhood origin | INSPECTED |
| `1qJVs965ADATq5XO5REWD59hSluVxgK3S` | 親愛度11–20 | Dear compilation | N.I.A., Tsukika/Shion, hero ideal | INSPECTED |
| `1G6lu0SVhPL7aU-QUqfT2jI7hZdelV4TD` | 親愛度21–27 | Dear compilation | Sena retirement crisis, separation, star quality, summer defeat, winter wager | INSPECTED |
| `1Bn28xDmkBDOORLtjgpyn4TIfoMsgY8Wu` | おでかけコミュ全20種＋選択肢 | Produce-event compilation | formal/vendor, hobby, food, comedy, lower-stakes Producer registers | INSPECTED |
| `1DK6ev-04-cM7yzEfXi_rfx8RpJIgyTJL` | `理論武装して` 楽曲コミュ | song communication | heel/dark-hero authorship and fan-facing ethics | INSPECTED |
| `1wH2VSEp3ybnkSVvyFBdDURhzAppKPXH8` | `Campus mode!!` 楽曲コミュ | song communication | inherited institutional form under Tsubame authorship | INSPECTED |
| `1wmTQvEsbk371-a4DBd6jk5PuzOEM5T2c` | `クライアイ` 楽曲コミュ | song communication | rival-love, equal invitation, public redirection | INSPECTED |
| `1quXY7-DWBCwpuZUN80aUt6efj-JUnovg` | `理論武装して` Official Music Video | authored official MV | symbolic/editorial antagonism grammar | INSPECTED |
| `1r34FrA4oJQFIS2ReudVSqOqoJxtiSHQa` | `理論武装して` Tsubame rendering | 3DMV/game performance | embodied attack, angularity, direct camera confrontation | INSPECTED |
| `1X3qKG7Nq9nbhNLhf_HV1l3XyesNZ97ob` | `Campus mode!!` Tsubame rendering | 3DMV/game performance | bright institutional address with command/weight | INSPECTED |
| `15xIMZQ_pNrY7JOEyG5_1P2qpSQRxwjKV` | `クライアイ` Tsubame rendering | 3DMV/game performance | held center, beckoning authority, equal-facing invitation | INSPECTED |
| `1nUrWHkO7m5RvpIBLVLVTBWgCYSxP0ize` | `星南と燕の日常` | event communication | low-stakes Sena/Tsubame reciprocity and ordinary intimacy | INSPECTED |
| `1c2iTFS76Qu2V08L87Mn7WkMiFumqfeU-` | SSR support `やっと見つけたぞ！` | support communication | vice-president/institutional register and ensemble care | INSPECTED |

Source boundary: **14 canonical logical objects / 14,965.243 seconds / 4.157 hours / 1,347,835,563 bytes**. Seven isolated Dear clips are retained as supplemental inspection aids and are not counted as independent evidence. Complete technical metadata and SHA-256 hashes live in `GKM_PHASE3_TSUBAME_AUDIOVISUAL_SOURCE_MANIFEST.json` — Drive `1PuIH9a6NQ7TCYlrJe35LSnMQnPhDDB63`.
## Hataya Misuzu — completed AV crosswalk

| role | canonical location |
|---|---|
| music/performance source folder | Drive `1A7P4qm7AzuAaKZqWmp9dX7FUywxIfLSu` |
| speech/Dear/song-commu source folder | Drive `1OmMLf30qrLnLm-cMVWDHMKJNb7DtTCzL` |
| AV analytical home | Drive `1l5i5TIpuWe2_6L8jNQAujugqYFj5lJ4h` |
| textual-core home / revision addendum | Drive `1jBVPX6SZQDyLk4uQ21ImbuIjXCnD40t2` |
| source manifest | `GKM_PHASE3_MISUZU_AUDIOVISUAL_SOURCE_MANIFEST.json` |
| integrated authority | `GKM_MISUZU_COMPLETE_AUDIOVISUAL_BASELINE.md` |
| dialogue specialist | `GKM_MISUZU_DIALOGUE_VOICE_ACTING_CLOSE_READING.md` |
| music/MV specialist | `GKM_MISUZU_MUSIC_MV_AND_PERFORMANCE_CLOSE_READING.md` |
| evidence/metrics | `GKM_MISUZU_AV_EVIDENCE_AND_METRICS_MATRIX.md` |

Source boundary: 27 staged objects. Dear 021–027 used the raw/streamed connector path because its file size exceeds the ordinary connector threshold; it is present and hashed.

## Phase 3 Hiro complete source crosswalk

Canonical source folders:

- Dialogue/commus: Drive `1BHIqrWfgnE9kHHEAtjP9RY4ZB7kLgWlb`
- Music/3DMV: Drive `1x_yRi49R9YvrAAkHfgDTGxB1_xBJConW`

| drive_id | title | source type | evidence class | analytical role |
|---|---|---|---|---|
| 1UELlTgEu9lKMysQKjnLbt4MEUg9XWcbi | 【学マス】篠澤広　親愛度１～１０話【アイドルコミュ】-(720p30).mp4 | dear_compilation | S1-AV | Dear 001–010 / STEP1 |
| 15PC5cF8TmNAP9vi2ccO6M4Zw476JYWE8 | 【学マス】篠澤広　親愛度１１～２０話【アイドルコミュ】-(720p30).mp4 | dear_compilation | S1-AV | Dear 011–020 / N.I.A. |
| 1EDx0YyXW11f6CNg2Too0fh-7jpaEVU9Q | 【学マス】篠澤広  親愛度コミュ21～27話まとめ【STEP3】-(720p60).mp4 | dear_compilation | S1-AV | Dear 021–027 / STEP3 |
| 1Toi0yHcoq0jV0GMcA4JalcrlLMbnFxQO | 【学マス】 篠澤広 親愛度コミュ28～37話まとめ【H.I.F編】【STEP4】-(720p60).mp4 | dear_compilation | S1-AV | Dear 028–037 / H.I.F. |
| 10ZYoYqUEiQu4D5CllwOkhiEg0tsV4Kn4 | 【楽曲コミュ】光景【篠澤広】【学マス】-(720p30).mp4 | song_commu | S1-AV | 光景 song communication |
| 1SefKMkVth430vm0qAh4xzLcK_N0mbRrt | 【楽曲コミュ】コントラスト【篠澤広】【学マス】-(720p30).mp4 | song_commu | S1-AV | コントラスト song communication |
| 1DkdQlnwXXpyg-raVxgn3Hve7IBIhGBpS | 【Campus mode!!】篠澤広 楽曲コミュまとめ【学マス】-(720p30).mp4 | song_commu | S1-AV | Campus mode!! song communication |
| 1vo_bb3APWI46ouyP8gBLDT6IKYtEoKrD | 【サンフェーデッド】篠澤広 楽曲コミュまとめ【学マス】-(720p60).mp4 | song_commu | S1-AV | サンフェーデッド song communication |
| 1bFRSUu8i-L7iU9OWTQa_9HJPEDmf08ul | 【ガラクタロード】篠澤広  楽曲コミュまとめ【学マス】-(720p60).mp4 | song_commu | S1-AV | ガラクタロード song communication / CIDOL 018 |
| 1F9TUHsTmutf8wzxJjCRLwiTXa1CKfEUf | 【楽曲コミュ】ハッピーミルフィーユ（花海佑芽ボイス実装版）【篠澤広】【学マス】-(720p30).mp4 | song_commu | S1-AV | ハッピーミルフィーユ song communication |
| 13-Fh37KmKFvRLhWFaskIJE5royX6XZh1 | 【楽曲コミュ】仮装狂騒曲【篠澤広】【学マス】-(720p30).mp4 | song_commu | S1-AV | 仮装狂騒曲 song communication |
| 1Y5zbtbMqqZw8K12HjP5Up_54Ce3jWjBk | 4K HDR「光景」 (篠澤広 ソロ SSR)【学マス⧸学園アイドルマスタ⧸Gakuen idolm@ster MV】-(720p60).mp4 | 3dmv | S1-AV | 光景 Hiro rendered performance |
| 1BJxsuu7p4m4eUFOgXlstQI9AgWGnyWbC | 【アイマスMV】どんどん上手くなる光景  篠澤 広　学園アイドルマスター　学マス-(720p60).mp4 | derivative_reception | S4-DERIVATIVE | Fan comparative montage: progressively improving 光景 |
| 14mm43MjBvXxqXvEfgpxdgpzO_hYSyvLn | 初星学園 「光景」Official Music Video (HATSUBOSHI GAKUEN - Koukei)-(720p30).mp4 | official_mv | S2-OFFICIAL-AV | 光景 authored official MV |
| 1JbU-ssxlwCzUGTnq4i2JLO-fw3EaPBxR | 4K HDR「コントラスト」 (篠澤広 ソロ2 SSR)【学マス⧸学園アイドルマスタ⧸Gakuen idolm@ster MV】-(720p60).mp4 | 3dmv | S1-AV | コントラスト Hiro rendered performance |
| 11LEGW6hntUwu7GhljqYbqWzcO2lZFwDz | コントラスト-(720p25).mp4 | full_mix_presentation | S2-AV | コントラスト full/static presentation |
| 11Sf_pH-3JhiLcAUT4xLkm8rbzYL84f8E | 4K HDR「サンフェーデッド」 (篠澤広 ソロ3 SSR)【学マス⧸学園アイドルマスタ⧸Gakuen idolm@ster MV】-(720p60).mp4 | 3dmv | S1-AV | サンフェーデッド Hiro rendered performance |
| 14gD5uR2AdNK274Z8Juh6u5pY3pWYpMfF | 初星学園 「サンフェーデッド」Official Music Video (HATSUBOSHI GAKUEN - SUNFADED)-(720p24).mp4 | official_mv | S2-OFFICIAL-AV | サンフェーデッド authored official MV |
| 1NZfazcL67wDoVoFa5nuQp-y3E2-Edzmd | 4K HDR「Campus mode!!」(篠澤広 フェスSSR)【学マス⧸学園アイドルマスタ⧸Gakuen idolm@ster MV】-(720p60).mp4 | 3dmv | S1-AV | Campus mode!! Hiro rendered performance |
| 1zPxR0JyPp4JhLxWS_zfENcC9znXerQIj | 【学マス】篠澤広「初」 3DMV-(592p30).mp4 | 3dmv | S1-AV | 初 Hiro rendered performance |
| 1OXLlFgDZOfdom_Sywd_lF_j-dimUZeqp | 4K HDR「Howling over the World」 (篠澤広 ソロ SSR)【学マス⧸学園アイドルマスタ⧸Gakuen idolm@ster MV】-(720p60).mp4 | 3dmv | S1-AV | Howling over the World Hiro rendered performance |
| 1tdzAna_WcWmo9RzC5lyLnliiyJaoDGpy | 4K HDR「がむしゃらに行こう！」 (篠澤広 SSR)【学マス⧸学園アイドルマスタ⧸Gakuen idolm@ster MV】-(720p60).mp4 | 3dmv | S1-AV | がむしゃらに行こう！ Hiro rendered performance |
| 1P75Wv4Qu1W_R6lmZRs0fGmv4VOxoXcmG | 4K HDR「ミラクルナナウ(ﾟ∀ﾟ)！」 (篠澤広 SSR)【学マス⧸学園アイドルマスタ⧸Gakuen idolm@ster MV】-(720p60).mp4 | 3dmv | S1-AV | ミラクルナナウ(ﾟ∀ﾟ)！ Hiro rendered performance |
| 1oSoTZTGZNYN4Oq3R1Lwym0cZ8jWHtvxe | 初星学園 「コンテンポラリのダンス」Official Music Video (HATSUBOSHI GAKUEN - contemporary dance)-(720p30).mp4 | official_mv | S2-OFFICIAL-AV | コンテンポラリのダンス authored official MV |
| 1K9In8GKh9pP041E6A0zg3hyX-lKdug7G | 4K HDR「ENDLESS DANCE」(篠澤広 SSR)【学マス⧸学園アイドルマスタ⧸Gakuen idolm@ster MV】-(720p60).mp4 | 3dmv | S1-AV | ENDLESS DANCE Hiro rendered performance |
| 1laiDZzcPX6UA-Hz9NHaoAvdc8bX2Q6nW | 標　倉本千奈&篠澤広(ゆめぱしー)ver-(720p30).mp4 | duet_performance | S1-AV | 標 China/Hiro duet rendering |
| 1obrkIYn5VQl-7hkwnbC0Jck6ILDQH7Tv | 4K HDR「ガラクタロード」(篠澤広フェスSSR)【学マス⧸学園アイドルマスタ⧸Gakuen idolm@ster MV】-(720p30).mp4 | 3dmv | S1-AV | ガラクタロード Hiro rendered performance |
| 19ZDDv3IlyKBryQL9U9Xi7akxuW_ZJ5zt | 4K HDR「みちなるひろがる」 (篠澤広・倉本千奈 SSR)【学マス⧸学園アイドルマスタ⧸Gakuen idolm@ster MV】-(720p30).mp4 | duet_3dmv | S1-AV | みちなるひろがる Hiro/China rendered performance |
| 1S15fh_ENDBLtY8IhjdsHo1D4B8YjKp3E | 初星学園 「みちなるひろがる」Official Music Video (HATSUBOSHI GAKUEN - Unknown Unbound)-(720p30).mp4 | official_mv | S2-OFFICIAL-AV | みちなるひろがる authored official MV |
| 1UaOzLCa1P0Yd0Npw86Tj65NFGubgbbhw | 4K HDR「ハッピーミルフィーユ」(篠澤広 バレンタインSSR)【学マス⧸学園アイドルマスタ⧸Gakuen idolm@ster MV】-(720p30).mp4 | 3dmv | S1-AV | ハッピーミルフィーユ Hiro rendered performance |
| 16urNa641Iy6wsq-EWxQaqYgyFX4r1sfM | 4K HDR「仮装狂騒曲」(篠澤広 SSR)【学マス⧸学園アイドルマスタ⧸Gakuen idolm@ster MV】-(720p30).mp4 | 3dmv | S1-AV | 仮装狂騒曲 Hiro rendered performance |
| 1K1pfcfYCj7Xgs1Z5z0bbjwoo3Go7YRiq | 【学マス】篠澤 広 誕生日記念Single「メクルメ」- Game Sizeリリックビデオ CD予約受付中！【アイドルマスター】-(720p30).mp4 | official_lyric_video | S2-OFFICIAL-AV | メクルメ official Game Size lyric video |
| 10pmdSfOxpvp5x_zUh8KwmtgzZ9ALNI5C | メクルメ-(720p25).mp4 | full_mix_presentation | S2-AV | メクルメ full/static presentation |

Open/nonblocking: `みちなるひろがる` song commu.

### Mao analytical artifact crosswalk — 2026-08-17

| artifact role | canonical file | Drive ID |
| --- | --- | --- |
| AV release entrypoint | `00_README_AND_DOCUMENT_MAP.md` | `1tzxszq9GrjJgkdt-vtAk4xuYohe4Q37q` |
| integrated authority | `GKM_MAO_COMPLETE_AUDIOVISUAL_BASELINE.md` | `1P2He-LvbmAL58F1b--_UFO5woC7Z5_2X` |
| dialogue/voice specialist | `GKM_MAO_DIALOGUE_VOICE_ACTING_CLOSE_READING.md` | `10rIzRjSsnPhdN-HR6IK96zui7XNZYbRz` |
| music/MV specialist | `GKM_MAO_MUSIC_MV_AND_PERFORMANCE_CLOSE_READING.md` | `1q6G0kqpnyz2Q53K4BJxrkb5668m9D5zK` |
| evidence/metrics matrix | `GKM_MAO_AV_EVIDENCE_AND_METRICS_MATRIX.md` | `1hgTOuK1Ni1RCIxWErtk6g1mDcmaJH5PU` |
| source manifest | `GKM_PHASE3_MAO_AUDIOVISUAL_SOURCE_MANIFEST.json` | `1WriHnhC73XX6YHBXGZItaEJqQPz01hbi` |
| textual-core revision router | `GKM_CORE_04_ARIMURA_MAO_AV_REVISION_ADDENDUM.md` | `1Fyk7bd2_ZcP2OnPHJtzJxGgZ-o76O952` |
| completion report | `GKM_PHASE3_MAO_AUDIOVISUAL_COMPLETION_REPORT.md` | `1pjY72-gNXylQUw3_lLS3Gys0GJTpf8tg` |
| immutable release | `GAKUEN_IDOLMASTER_PHASE3_MAO_INTEGRATED_AV.zip` | `1Kyr-GuziRjC-zw83nvnMOVaBe16OzW1i` |

## Kuramoto China / 倉本千奈 — completed AV crosswalk (2026-08-21)

| logical object | public/uploader identity | source class | Drive source/home | state |
|---|---|---|---|---|
| Dear 001–010 | `倉本千奈 親愛度1～10` | acted Dear compilation | `VIDEO/06_KURAMOTO_CHINA/01_DEAR_ROUTE` | inspected |
| Dear 011–020 | `倉本千奈 親愛度11～20` | acted Dear compilation | same | inspected |
| Dear 021–027 | `倉本千奈 親愛度21～27 STEP3` | acted Dear compilation | same | inspected |
| Dear 028–037 | `倉本千奈 親愛度28～37 H.I.F.` | acted Dear compilation | same | inspected |
| CIDOL 000 | `Wonder Scale` 楽曲コミュ | acted song communication | `VIDEO/06_KURAMOTO_CHINA/03_SONG_COMMUS` | inspected |
| CIDOL 001 | `日々、発見的ステップ！` 楽曲コミュ | acted song communication | same | inspected |
| CIDOL 009 | `雪解けに` 楽曲コミュ | acted song communication / family-history object | same | inspected |
| CIDOL 007 | `Campus mode!!` 楽曲コミュ | acted song communication | same | inspected |
| CIDOL 014 | `空と約束` 楽曲コミュ | acted song communication | same | inspected |
| CIDOL 016 | ゆめぱしー `みちなるひろがる` 楽曲コミュ | acted duet communication | same | inspected |
| performance/MV corpus | nine rendered performances + two authored official MVs | rendered/authored AV | `VIDEO/06_KURAMOTO_CHINA/04_MV_3DMV_AND_PERFORMANCE` | inspected |

Canonical manifest: `GKM_PHASE3_CHINA_AUDIOVISUAL_SOURCE_MANIFEST.json` — Drive `1Sxn-q5KegPjQMcDmF0xLX2EKsHJYNdhT`.


<!-- LILJA_AV_R1_UPDATE_2026-08-22 -->
## Katsuragi Lilja AV source crosswalk — integrated baseline complete

| layer | canonical source set | status | current route |
|---|---|---|---|
| Dear acting spine | Dear 001–010; 011–020; 021–027; 028–037 | COMPLETE | `VIDEO/05_KATSURAGI_LILJA/01_DEAR_ROUTE/` |
| song communications | `白線`; `Campus mode!!`; `Atmosphere`; `ときめきエモーション`; `ガラクタロード`; `極光`; `桜フォトグラフ` | COMPLETE | `VIDEO/05_KATSURAGI_LILJA/03_SONG_COMMUS/` |
| Lilja performances/MVs | `白線`; `Campus mode!!`; `Atmosphere`; `ガラクタロード`; `極光`; `ENDLESS DANCE`; `Howling over the World`; authored `白線` and `Atmosphere` MVs | COMPLETE | `VIDEO/05_KATSURAGI_LILJA/04_MV_3DMV_AND_PERFORMANCE/` |
| REVERSI shared dyad | `ときめきエモーション` 3DMV + authored official MV | COMPLETE / shared canonical object | Sumika/shared ensemble source home; cross-reference rather than duplicate |
| integrated synthesis | 22 logical AV objects | COMPLETE | `GKM_LILJA_COMPLETE_AUDIOVISUAL_BASELINE.md` |

`桜フォトグラフ` resolves internal `adv_cidol-kllj-3-010_01–03`. The old acquisition request file is superseded.

<!-- RINAMI_AV_R2_UPDATE_2026-08-22 -->
## Himesaki Rinami — final integrated AV R2 crosswalk

| form | human title | textual mapping | current AV status |
| --- | --- | --- | --- |
| Dear STEP1 | `姫崎莉波 親愛度 001–010` | `adv_dear_hrnm_001`–`010` | CLOSED — 1080p30 direct-upload analysis materialization |
| Dear STEP2 / N.I.A. | `姫崎莉波 親愛度 011–020` | `adv_dear_hrnm_011`–`020` | CLOSED — 1080p30 direct-upload analysis materialization |
| Dear STEP3 | `姫崎莉波 親愛度 021–027` | `adv_dear_hrnm_021`–`027` | CLOSED — 720p60 direct-upload R2 materialization; SHA-256 `8a774bb1f2ad3b32b8bc7fe811ed7b56ca61d4c5b569eb99da191bbd0bad2d70` |
| Dear STEP4 / H.I.F. | `姫崎莉波 親愛度 028–037` | `adv_dear_hrnm_028`–`037` | CLOSED — 720p30 direct-upload R2 materialization; SHA-256 `3bedd68001ea277ddd50242da301fff1e1818a54505266dedccd7a340a25c876` |
| foundational solo | `clumsy trick` | CIDOL 000 | CLOSED — commu + 3DMV + official MV |
| second solo | `L.U.V` | CIDOL 001 | CLOSED — commu + 3DMV + full-song presentation |
| STEP3 solo | `36℃ U･B･U` | CIDOL 013 | CLOSED — commu + 3DMV + official MV |
| inherited school song | `Campus mode!!` | CIDOL 007 | CLOSED — commu + 3DMV |
| shared forceful song | `Howling over the World` | CIDOL 012 | CLOSED — commu + 3DMV |
| H.I.F.-era repertoire | `ガラクタロード` | CIDOL 017 | CLOSED — commu + 3DMV |
| peer duo | `SUGAR FLAVOR` / RippleSign | CIDOL 018 | CLOSED — commu + Rinami/Mao 3DMV + official MV |
| supplementary authored MV | `歌声は君いろ` | public title; no commu identity asserted | CLOSED as supplementary MV |
| breadth | `ENDLESS DANCE`, `がむしゃらに行こう！`, `ミラクルナナウ`, `初` | common/seasonal repertoire | CLOSED as range controls |

R2 source note: the high-resolution Dear 021–027 and 028–037 files replace only the physical R1 analysis representatives. Audio identity was verified; route timing, exact-text control, and logical-object count remain unchanged. Current manifest authority is `GKM_PHASE3_RINAMI_AUDIOVISUAL_SOURCE_MANIFEST.json` inside the R2 release.
