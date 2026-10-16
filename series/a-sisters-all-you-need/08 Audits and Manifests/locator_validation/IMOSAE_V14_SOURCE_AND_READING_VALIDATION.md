---
series: IMOSAE
artifact_type: source_audit
scope: V14_prospective_reading_validation
generation: V1
status: canonical
source_boundary: Locked Japanese V14 EPUB and frozen NORM1.0 derivative; prior-byte preservation through V13
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
version: '1.0'
date: '2026-10-12'
result: PASS_WITH_DOCUMENTED_SEMANTIC_EXCEPTION
---

# V14 prospective reading: source and interpretation validation

The [V14 deep reading](../../02%20Sequential%20Readings/IMOSAE_V14_DEEP_READING.md) is substantively complete and source-validated for Phase A. This decision opens the final checkpoint/ledger transaction. It does not certify the still-unproduced specialist/model/full-series release or final Git integration.

| Check | Result and tested scope |
|---|---|
| Ordered intake | PASS: all2369 paragraph/visual records read in publication order, including both afterwords, final present frame, colophon and advertising |
| Visual perception | PASS: all35 non-gaiji images inspected; relevant scene/form/advertising distinctions recorded |
| Raw identity | PASS: 5,035,527-byte original matches SHA-256 86dd3d6ae2196f1255b9266003e0b6337ee5011e0d11d0a4d2afe25791d31fd5; full ZIP CRC test returns no bad member |
| Frozen derivatives | PASS: V14 Markdown and sidecar exact byte hashes stated in reading; frozen releases preserved |
| Analytical register | PASS: 87 unique contiguous IDs, 52 textual/paratext ranges and35 visual routes; all references resolve |
| Original-member provenance | PASS: 2341 distinct paragraphs covered by selected ranges resolve their recorded XPath in original XHTML; not a claim that XPath existence proves an interpretation |
| Visual bytes | PASS: all35 registered original assets match their frozen hashes; earlier full source verification covered all42 V14 assets |
| Japanese short anchors | PASS: 22 explicit load-bearing short phrases checked in original blocks, with ruby, attribution and gloss in table below |
| Knowledge and chronology | PASS for V14 reading: true promise separated from false report; actual Sora two; future draft separated from present; astronaut desire separated from achievement; pregnancy actual |
| Speaker/focalizer | Reviewed in ordered context: character/narrator/draft/author/image attribution explicit. Universal character beliefs are not made objective fact |
| Counterthesis | Incorporated: coercive influence, inequality, concentrated labor, deceptive friends, unsafe gags, imperfect author ethics and overbroad persistence claims |
| Immutable history | PASS: earlier13 readings, four checkpoints and two early monographs preserve exact intake bytes; ledger changes have not begun |
| G005 replacement semantics | EXCEPTION: frozen 吐 is wrong; original scolding glyph/ruby しか governs analytical reading. Releases are not mutated |
| Publication | Produced in worktree only; not committed, pushed, GitHub audited or merged at this gate |

The phrase audit originally exposed a wrong planned coordinate for ハイテク (the illness paragraph instead of the preceding technology critique). That candidate error was repaired to the actual paragraph before canonicalization. This is a tested correction, not an unacknowledged passing assertion.

## Short Japanese-anchor readbacks

| Anchor | Speaker / level | Gloss or interpretive limit | Exact locator |
|---|---|---|---|
| 結果的に超えても超えられなくても | Miyako direct speech | whether or not the work surpasses the benchmark | `V14\|chapter:北へ。\|spine:018\|xhtml:text/part0017.html\|p:0137\|fp:714eee4a9910` |
| 事実と違うことを伝えた | narrator describing Haruto | the report is deliberately false | `V14\|chapter:北へ。\|spine:018\|xhtml:text/part0017.html\|p:0157\|fp:c0d775800c9d` |
| 可児那由多 | Itsuki proposal target | professional writer as addressed reader | `V14\|chapter:シリウス\|spine:032\|xhtml:text/part0031.html\|p:0090\|fp:eb39782ba108` |
| 強い想い | Miyako-aligned narration | a strong feeling toward someone | `V14\|chapter:シリウス\|spine:032\|xhtml:text/part0031.html\|p:0093\|fp:e0d7057a603b` |
| 家事とか宙くんのこと | Nayuta speech | housework and care of Sora | `V14\|chapter:報いの虹\|spine:036\|xhtml:text/part0035.html\|p:0037\|fp:97a0583d5a77` |
| 小説を書きたいので | Nayuta attributed continuation | because she wants to write | `V14\|chapter:報いの虹\|spine:036\|xhtml:text/part0035.html\|p:0038\|fp:3f7fe285dcbb` |
| 全員まとめて | Itsuki public speech | suspended challenge completed in ILL021 | `V14\|chapter:報いの虹\|spine:036\|xhtml:text/part0035.html\|p:0230\|fp:9de6b749d5d0` |
| 人でなし | draft-Sora focalization | costly, inconsiderate creator aspiration | `V14\|chapter:青い小鳥たち\|spine:042\|xhtml:text/part0041.html\|p:0046\|fp:6c8f1b7f1698` |
| 現在２歳 | mainline narrator | Sora is currently two; future is manuscript | `V14\|chapter:青い小鳥たち\|spine:045\|xhtml:text/part0044.html\|p:0005\|fp:d33710a39fd0` |
| 生モノ | Chihiro speech | care around actual people used as fiction | `V14\|chapter:青い小鳥たち\|spine:045\|xhtml:text/part0044.html\|p:0010\|fp:b672901d8572` |
| 事後承諾 | Itsuki speech | permission sought after writing | `V14\|chapter:青い小鳥たち\|spine:045\|xhtml:text/part0044.html\|p:0031\|fp:fb1a989f17bc` |
| 曇ってる顔 | Itsuki speech | enjoying Nadeko's hurt face | `V14\|chapter:青い小鳥たち\|spine:045\|xhtml:text/part0044.html\|p:0036\|fp:bfd56c64f888` |
| ハイテク | Chihiro speech | vague future-technology critique | `V14\|chapter:青い小鳥たち\|spine:045\|xhtml:text/part0044.html\|p:0051\|fp:d16fd43a0896` |
| ご都合主義 | Chihiro speech | convenient fictional medicine | `V14\|chapter:青い小鳥たち\|spine:045\|xhtml:text/part0044.html\|p:0058\|fp:79d9cea49e96` |
| 宇宙飛行士になるんだから | Chihiro private speech | astronaut aspiration, not achievement | `V14\|chapter:青い小鳥たち\|spine:045\|xhtml:text/part0044.html\|p:0084\|fp:9df1829160c1` |
| 予知夢 | Chihiro private thought | brief prophetic-dream speculation | `V14\|chapter:青い小鳥たち\|spine:045\|xhtml:text/part0044.html\|p:0088\|fp:0667e7e6de30` |
| まさかね | Chihiro private speech | dismissal of that speculation | `V14\|chapter:青い小鳥たち\|spine:045\|xhtml:text/part0044.html\|p:0089\|fp:2a24a725a777` |
| 宙の妹 | mainline narrator through Chihiro | actual unborn younger sister | `V14\|chapter:青い小鳥たち\|spine:045\|xhtml:text/part0044.html\|p:0093\|fp:810b9318a768` |
| ないものねだり | Chihiro-aligned reflection | desire for what one lacks | `V14\|chapter:青い小鳥たち\|spine:045\|xhtml:text/part0044.html\|p:0096\|fp:621dfbecc807` |
| これさえあればいい。 | Chihiro-aligned reflection / narrator | particular sufficient story | `V14\|chapter:青い小鳥たち\|spine:045\|xhtml:text/part0044.html\|p:0101\|fp:b6ade6dc596e` |
| 実は本編でした | Yomi afterword | framing story actually main narrative | `V14\|chapter:あとがき２\|spine:046\|xhtml:text/part0045.html\|p:0002\|fp:7b3a47c8718f` |
| 関係ありますん | author biography | ambiguous comic negation | `V14\|chapter:あとがき２\|spine:048\|xhtml:text/part0047.html\|p:0003\|fp:eb6ab7975607` |

## Artifact identity and limitations

V14 analytical file: 119441 bytes; SHA-256 `b64b3f0c82569ae572eaa609116262ae4afd19f01b6b393b2ae253ec777cfea6`. [Machine validation](IMOSAE_V14_SOURCE_AND_READING_VALIDATION.json) contains these exact tested routes and results. This checksum fixes the analytical artifact at the Phase A boundary; it does not replace source authority.

Mechanical source routes, direct wording checks and manual scene attribution have different scopes. The V01-V13 register integrity checks do not themselves prove all older claim/speaker formulations; targeted old-ledger citation repairs and full-series controversial-claim review remain Phase B/F work. The G005 exception and primary-name corrections are exposed in the [identity/normalization errata](../../06%20Evidence%20and%20Indexes/IMOSAE_PRIMARY_IDENTITY_AND_NORMALIZATION_ERRATA.md).


## Extended primary-name correction

A subsequent original-ruby check corrected the new reading's mistaken Izumi label and romanizations before the Phase B freeze. Sōta Izumi is 和泉颯太, his former pen name is Misaka Sōma / 神坂蒼真, and current pen name 漬物ステーキ. 神戸聖 is Gōdo Satoshi; 城ヶ峰信長 is Shirogamine Nobunaga; 優羽 is Yū. 木曽撫子 is Nadeshiko Kiso, with なでこ as nickname. 熊野愛果 is Manaka Kumano, nickname Mana. Six original blocks were reopened and every ordered ruby base/reading pair matched the frozen sidecar. This additional audit is narrower than a claim that every inherited name or registry row has been checked. All earlier readings/checkpoints remain unchanged.


## First-publication representation

The original tranche identities reported above remain provenance of the executed Phase A/B checks. The [explicit compatibility transformation](../authority_audits/IMOSAE_FIRST_PUBLICATION_COMPATIBILITY_TRANSFORMATION.md) records required LF and opaque-Drive-ID presentation changes before initial Git publication, with evidence/interpretations/states preserved. Current machine validation and the final corpus manifest bind V14 `e3bdbec2041a19dac8ad37726f07ed5820f2102a4722f74bc23b2817f4f8b489` / 118708 bytes and checkpoint `bd21fbb5e24d86108e9296574f43779f5198caa0f36ab5346726747e48ac507b` / 47875 bytes. Raw/NORM releases, earlier thirteen readings/four checkpoints/two monographs and all eight ledger output hashes are unchanged.
