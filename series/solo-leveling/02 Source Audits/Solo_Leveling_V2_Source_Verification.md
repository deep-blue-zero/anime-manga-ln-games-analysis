---
title: Solo Leveling — V2 source verification
artifact_id: SL_SOURCE_VERIFICATION_V2
artifact_type: source_audit
authority_generation: v2
status: canonical
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
canonical_home: series/solo-leveling/02 Source Audits/Solo_Leveling_V2_Source_Verification.md
source_boundary: "Chugong's Korean omnibus and Yen Press English manhwa V01–V15"
---

# Solo Leveling — V2 source verification

The operative baseline is `df01a0dea291e3d1827479e5ffae6438dd5e854c` on `main`. This is the merge commit of [PR #602](https://github.com/deep-blue-zero/anime-manga-ln-games-analysis/pull/602), with series parent `627aab9bf41f8473a143c6cdfc692d99a76fc0d8`. The final Phase 3 register contains 109 independently reviewed findings and seven closing-pass findings with separate coverage. Git history through this baseline contains the reviewed amendments to that audit. This verification records differences from the accepted [Phase 3 audit](Solo_Leveling_Phase_3_Korean_Source_Evidence_Audit.md) where the primary bytes establish a correction.

## Source identity and inspection

| Witness | Verified identity | Scope of verification |
| --- | --- | --- |
| Chugong's Korean prose | `나 혼자만 레벨업.epub`, 1,549,240 bytes, SHA-256 `ddb2527fd0e273ecf17dc54ced1bc5354c25e89b19929fb16fb584c64bd5d6f0` | ZIP CRC passes across 43 members. All 33 numbered body files and 59,567 nonempty paragraphs reproduce Phase 3. The principal and the independent source-structure specialist separately opened the EPUB in place. |
| Yen Press digital English manhwa, V01–V15 | Each filename, byte count, and SHA-256 matches the [Phase 1 machine audit](Solo_Leveling_Phase_1_CBZ_Machine_Audit.json). | Fresh CRC checks pass for all 15 archives. Archive-entry counts match Phase 1. The established page inventory contains 4,479 JPEG members and 4,635 logical pages. Page-level claims require actual viewing of the cited sequence. |

The named source directory held the EPUB and the fifteen CBZs in separate folders. The inventory turned up no local index, extraction package, English novel edition, or original Korean-language manhwa. The Korean novel governs wording, narration, and prose continuity. The English manhwa governs panel order, visual presentation, and English adaptation dialogue. Comparison across these witnesses can identify an adaptation difference. Translation attribution to a Korean comic balloon requires its own verified witness. Anime and sequel continuities fall outside this evidence boundary.

## Reproduce the locators

1. Open the identified EPUB as a ZIP and follow `META-INF/container.xml` to the OPF. Resolve the manifest IDs in spine order. After the title page, this edition contains `index_split_000.html` through `index_split_032.html` in numeric order.
2. In each XHTML body, traverse its `<p>` elements in document order. Collect text from inline children, decode HTML entities, and trim surrounding whitespace. Count each nonempty paragraph once and restart at one in each file. The 434 `<hr>` breaks, 11 asterisk breaks in `<pre>`, images and list items do not receive paragraph numbers. The 184 standalone equals-sign paragraphs do, as do heading and completion paragraphs.
3. Read `s024¶1908` as the 1,908th nonempty paragraph of split 024. Add its literary unit, as in `ch.191 · s024¶1908`. Two or more splits can carry one unit. Mark a range crossing a split with both endpoint locators.
4. Assign the main-story chapter from the last standing numbered heading. The first narrative paragraph is `s000¶2`, after the work title. The numbered sequence is `2화` through `243화`. Chs. 17 and 19 have a terminal period at `s001¶813` and `s001¶1222`. Use the main completion marker, then index `외전` and `후일담` separately.
5. For the manhwa, cite the volume and logical page printed in the member name. A member with `p066-p067` represents both pages. Preserve their joint composition when viewing it. Use the cover and story ranges in the [Phase 1 integrity audit](Solo_Leveling_Phase_1_Source_Integrity_Audit.md#4-archive-segment-and-logical-page-boundaries) to distinguish story breaks from cover or back matter.

| Splits | Nonempty paragraphs, in order |
| --- | --- |
| s000–s010 | 2562, 2291, 2804, 1846, 2571, 973, 1826, 2309, 2428, 2014, 1613 |
| s011–s021 | 1930, 1187, 2596, 2198, 1154, 2773, 1465, 1711, 2328, 60, 581 |
| s022–s032 | 199, 239, 2183, 2351, 2024, 1343, 1493, 2098, 2230, 2237, 1950 |

## Early named labels and numbered chapters

The single NCX entry is `Start`. The EPUB body contains two independently recoverable text layers. A consecutive main-story chapter sequence survives in paragraphs. The early named labels separately survive as 18 standalone HTML list items. Their placement between paragraphs excludes them from a paragraph-only search. For instance, `프롤로그` appears after `s000¶1` and `전직 퀘스트` after `s003¶973`. Neither is a separate numbered chapter or an NCX link. The numbered title-like fragments `2.악마성` at `s002¶914` and `5.톱니바퀴` at `s002¶2121` use yet another form.

| Early label | After paragraph | Early label | After paragraph |
| --- | --- | --- | --- |
| 프롤로그 | s000¶1 | 도마뱀들 | s001¶790 |
| E급 헌터 | s000¶18 | 기브 앤 테이크 | s001¶1622 |
| 이중 던전 | s000¶209 | 정리 | s002¶255 |
| 시작된 공격 | s000¶460 | 거래 | s002¶518 |
| 세 가지 규율 | s000¶628 | 우연 | s002¶1218 |
| 마지막 시험 | s000¶1048 | B급 강태식 | s002¶1667 |
| 페널티 | s000¶1489 | 이상한 레이드 | s002¶2547 |
| 일일 퀘스트. | s000¶2067 | 대박의 예감 | s003¶258 |
| 레벨 업! | s000¶2494 | 전직 퀘스트 | s003¶973 |

V1 correctly retained the early labels and missed the numbered chapters as a stable route for later prose. Phase 3 recovered the chapter sequence and reported the labels absent after a search that excluded their HTML elements. Phase 1 §6.4 describes the packaging and the limit on Korean print-volume claims. The V2 dispositions for P-01, S1-12, S2-01, S6-10, and S6-11 carry both observed structures forward. Numbered units and paragraph locators together give the more precise crosswalk.

## Narrative boundaries

| Boundary | Location |
| --- | --- |
| Chapter 1 begins under the title | First narrative at s000¶2, title at s000¶1 |
| Chapter 243 heading | s030¶1353 |
| Chapter 243 transition and closing vignettes | ch.243 · s030¶1463–1608 |
| Main-story completion marker | ch.243 · s030¶1609 |
| Side stories begin | 외전 1 · s030¶1612 |
| Side story 4 continues into the next body | 외전 4 · s030¶2136–s031¶94 |
| Side story 14 continues into the next body | 외전 14 · s031¶2077–s032¶32 |
| Side story 18 opens on a bare heading | 외전 18 · s032¶650 |
| Side stories close | s032¶1524 |
| Postscript block heading | s032¶1525 |
| Postscript 1 `베르의 기억` | 후일담 1 · s032¶1526 |
| Postscript 2 `다시 만날 때까지` | 후일담 2 · s032¶1748 |
| Final prose paragraph, Sung Suho's dream | 후일담 2 · s032¶1950 |

The closing transition at `s030¶1463–1467` belongs to the narrative. The scene with Go Gunhee in `ch.243 · s030¶1562–1608` is Jinwoo's first visit after the reset. Go Gunhee recalls that visit when Sung Jinwoo returns about ten years later in `외전 21 · s032¶1438–1484`. These are separate adaptation witnesses. The exam morning appears first from Sung Jinwoo's side in `외전 14 · s032¶1–32`. Sung Il-hwan's perspective in `외전 18 · s032¶752–773` partially revisits it. A matching image of the morning alone cannot settle the adaptation of Sung Il-hwan's coda.
