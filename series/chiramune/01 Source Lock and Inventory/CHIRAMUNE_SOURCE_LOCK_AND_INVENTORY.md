---
series: CHIRAMUNE
artifact_type: source_lock_and_inventory
scope: ACQUIRED_JAPANESE_EPUB_CORPUS
source_boundary_date: 2026-08-29
generation: V1.2
status: canonical
release_state: mutable_active
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
---

# Chiramune source lock and inventory

## Authority and location

This document is the Git-side routing record for the acquired Japanese *Chitose Is in the Ramune Bottle* source corpus. It does not contain or replace the EPUB source bytes.

- Primary-source Drive root: `1tNJvglC-ri_AEGTkJupZ78WddyiCqQMy`
- Chiramune source folder: `1bI8p0tRpD7_u6Xi3vubqydl-jR7gJFxx`
- Drive audit manifest: `1Oq8MhiuNApwg-qv9PxEfJG9YTzLuZy52`
- `audit_manifest.json` SHA-256: `e4d302d662997ae67be9368d45dd2dc7fefd5918f5c8540cbe82a897c00a8231`
- Audit date recorded by manifest: `2026-08-29`
- Original series title: `千歳くんはラムネ瓶のなか`
- Author/creator metadata: `裕夢` (Hiromu)

## Locked inventory

| Role | Source object | Drive file ID | SHA-256 |
|---|---|---|---|
| main volume | Volume 01 | `11DXxG7Ca3ugbM6WyRLpAnLob31OH-HaE` | `440a634dac96f1a08ad698e1a6723dcf5075ff49ac8e2726be74c8ef50fce33d` |
| main volume | Volume 02 | `1YL_ucWYHXDmRlu7B7_FosaA3izp5a23u` | `521e764266f39d1f7be105711210badd6e0aba6d208878b5fe0d9961aeb7b056` |
| main volume | Volume 03 | `1pmpRNfflS675u6jxakP65mwYMYtUAj-w` | `7e161668c65aaaef324c07e64810227e880600b0db59111e6ce4219ed5f5e2af` |
| supplemental booklet | Volume 03 illustration and SS booklet | `1St3ayvwF-7uzbjk4xQT0074B9rwr4AyC` | `0edde35a6a9ec238c31aefc3ede00aca5ab1276a9d2c9eaa01a67da787eb70fd` |
| main volume | Volume 04 | `1k6G6EwwTthxdByyCwj5AkjUKOGFRBnI6` | `96113f9d92616084144ea06172ad5ea1dee54e1f5b53ed872a717d4e5bac4470` |
| main volume | Volume 05 | `1Tb9Oa2GbYykPqX0PcJqwU_wSX249yyEv` | `6266d27492bcc2a966ca3aa7fca98a47e9bd830a0e71cfeb62df4aeedf3efc7e` |
| alternate/supplemental edition | Volume 05 special edition | `1CUzsfbC57YmOJ2gvYkBZfzfqGjR4cMds` | `4cd54018dc4f9bde7fc34ee9efff01b5c22cfce2fedda5db579ac7c04aef767e` |
| main volume | Volume 06 | `1Ht_zhXrF3yaDW5Fr3zhvf72Q3JN9jBzt` | `f9bfe6dfd72ac2032b291c8b1a7b6e2a52e3a6e74f1b03cdcc0ffa33d3fb706b` |
| supplemental volume | Volume 06.5 | `1WzGkGeIr58Zj8fxuNqJm4n4thGGCeH9G` | `ab19b4561ad8486b95ba0bfdb489c2003736bcb8c3bcdade36bb9d1a3718b921` |
| main volume | Volume 07 | `1C9RUUVWKkt1gMUdjJS3WKH7fXvWq63XR` | `6c6018e65f021ecea9c9cafd464fa5b42e887e6317931162efedc01ac020edd1` |
| main + supplemental edition | Volume 08 special edition | `1yGrcEag09mib-lSly4WSXW0-vlP5Wsr4` | `124d66e237efd52873dca5bbff1141a56dcad30821365da69553b54e2955dc03` |
| main volume | Volume 09 | `1IQrypUsZEIgeqpMUpHVxU37BGSQfANot` | `3e2de8091542d4658884dd069ede4d64b9587248dbd1e3c30905684b435335eb` |
| side-story collection | Days of Endless Summer | `1YHn0YaSorG9SfZKw1JXjPMZeJQt0Yxpf` | `24a92c80666b95658a2c2e6ab03434996233cb9357cea9981da3fc6566455c39` |
| supplemental volume | Volume 09.5 | `1-lVx6za7q9cmGnWcI1j1xETFK-8g9reU` | `0f2ca4c31b19356f153a04b9c026ddba43f57a11c439b78d63f6cd44b9dbddb2` |

## Integrity state

The source audit records:

- 14 EPUB files;
- nine distinct numbered main volumes, Volumes 01–09;
- zero missing numbered main volumes through Volume 09;
- zero exact-duplicate groups;
- ZIP CRC checks passed for all 14;
- EPUB container checks passed for all 14;
- 11 packaging-conformant EPUBs and three packaging warnings.

Independent pre-bootstrap verification of the Drive-resident copies reproduced all 14 manifest SHA-256 values and confirmed that every EPUB container resolves to an existing OPF package. The three warnings affect Volumes 02, 03, and 04: their uncompressed `mimetype` member is not the first ZIP entry. Treat this as a packaging-order defect, not content corruption; preserve the original bytes rather than repacking merely to normalize the warning.

All 14 acquired EPUB package metadata records Japanese language (`ja`) and creator `裕夢`.

## Coverage decisions

### Volume 08

A separate regular Volume 08 EPUB is not held. The acquired special edition contains the complete Volume 08 novel plus its rough-illustration supplement, so the narrative witness is present. Do not count the absent regular-edition SKU as missing narrative content.

### Volume 05

Both the regular Volume 05 witness and a special-edition object are present. Use the regular witness for the clean mainline prospective reading unless a later source audit identifies a reason not to. Treat distinct special-edition SS/supplemental material separately after the Volume 05 mainline reading has frozen.

### Volume 05 regular-main analysis disposition

The regular Volume 05 witness was reverified at SHA-256 `6266d27492bcc2a966ca3aa7fca98a47e9bd830a0e71cfeb62df4aeedf3efc7e` before prospective reading. Its complete narrative, cover, five frontmatter images, ten narrative illustrations, afterword, author profile, colophon, and eleven advertising/editorial backmatter images were classified. No embedded bonus fiction was found.

The afterword confirms that the separate special edition contains an approximately 130-page short-story booklet combining retailer bonus stories and a newly written first-year Yuzuki/Haru story. That paratext establishes narrative material exists but does not admit any event from the separate object into the regular-main freeze. The regular V05 main reading and prospective freeze are complete and remain the historical main boundary.

### Volume 05 Special Edition analysis disposition

The locked Special Edition was independently reverified at SHA-256 `4cd54018dc4f9bde7fc34ee9efff01b5c22cfce2fedda5db579ac7c04aef767e`. OPF metadata identifies `千歳くんはラムネ瓶のなか　５　ＳＳ冊子付き電子特装版`, 裕夢, 小学館, Japanese, publication date 2021-04-25, and ASIN `B091T3MBHQ`.

Its complete regular-main text was compared with the admitted regular Volume 05 witness: both ordered normalized streams contain 5,479 text rows and no difference. The duplicate main text is therefore verified but not counted as a second narrative event stream.

The appended booklet contains 17 republished bonus stories originally associated with Volumes 01–04 and one newly written first-year Yuzuki/Haru story. Each component was separately inventoried and placed. `シャンプーにキャップ` is a revised witness of the same late-V03 event found in the separate V03 booklet: shared evidence is counted once, while material edition additions remain addressable. Contents/dividers, creator commentary, profiles, colophon, and advertising were audited under bounded paratext roles.

The complete disposition and frozen supplemental checkpoint are in `../02 Sequential Readings/CHIRAMUNE_V05_SPECIAL_EDITION_SUPPLEMENTAL_READING.md`. At that checkpoint, the next safe source was Volume 06 main.

### Volume 06 analysis disposition

The locked Volume 06 witness was independently reverified at SHA-256 `f9bfe6dfd72ac2032b291c8b1a7b6e2a52e3a6e74f1b03cdcc0ffa33d3fb706b` before prospective reading. OPF metadata identifies `千歳くんはラムネ瓶のなか　６`, 裕夢, 株式会社小学館, Japanese, and modification timestamp `2021-08-13T00:00:00Z`.

Its complete narrative—prologue, Chapters 5–8, and two epilogues—was extracted and read. The continuation of chapter numbering makes it narratively coupled to V05 while preserving a distinct source and freeze boundary. Ten interior narrative illustrations, frontmatter, afterword, author profile, colophon, and advertising backmatter were classified; no embedded bonus fiction was found.

The extraction produced 7,616 locator rows and 7,716 reading lines. The locator TSV SHA-256 is `d1fa9c512de0fe4b25d1efe71e66a85453df6f1537ab084102d4a8cd4b57de63`. The V06 main reading and prospective freeze are complete. Volume 06.5 was subsequently integrated through its own supplemental checkpoint without rewriting this main boundary.

### Volume 06.5 analysis disposition

The locked Volume 06.5 witness was independently reverified at SHA-256 `ab19b4561ad8486b95ba0bfdb489c2003736bcb8c3bcdade36bb9d1a3718b921`. OPF metadata identifies `千歳くんはラムネ瓶のなか　6.5`, 裕夢, 株式会社小学館, Japanese, publication date 2022-03-23, and modification timestamp `2022-08-19T08:39:55Z`.

The volume contains four separately focalized stories, all securely placed after the V06 festival and before second term. They are integrated as `SUPPLEMENTAL_MAINLINE` components. Editorial contents order is preserved, but no exact total cross-story calendar is asserted because the stories do not supply sufficient mutual reference.

The whole-object extraction produced 5,342 non-empty text/image locator rows and 5,440 reading lines. The locator TSV SHA-256 is `0f016c2f6bea54e497327622d4ed0c0e590ab535349ef88377d4d0dc24918986`; the reading projection SHA-256 is `a41cdc60e93413b7629eafdd4258f55db19b6dcdd093156403e759a5cc4de623`. Six frontmatter images, four story-title images, eleven unique narrative scene illustrations, the afterword, author profile, colophon, and ten advertising images were inspected and bounded by role. The repeating `叶` ornament is not counted as three narrative scenes.

The afterword identifies real `URALA` and `HOSHIDO` interviews as production inputs while stating that most story material was fictionally reconstructed. It also describes local collaboration as locally initiated rather than quid-pro-quo placement. These statements are retained as production context only and do not override diegetic evidence.

The complete disposition and frozen supplemental checkpoint are in `../02 Sequential Readings/CHIRAMUNE_V06_5_SUPPLEMENTAL_READING.md`. At that checkpoint, the next safe source was the exact locked Volume 07 main witness.

### Volume 07 analysis disposition

The locked Volume 07 witness was independently reverified at SHA-256 `6c6018e65f021ecea9c9cafd464fa5b42e887e6317931162efedc01ac020edd1` before prospective reading. OPF metadata identifies `千歳くんはラムネ瓶のなか　７`, 裕夢, 株式会社小学館, Japanese, electronic publication date 2022-08-18, ASIN `B0B8CHWGTT`, and print-base ISBN 978-4-09-453085-8.

The narrative contains four numbered chapters followed by a short component literally titled `プロローグ　ヒーロー見参`. Its post-Chapter-4 title and placement are preserved rather than normalized into an epilogue. The afterword, author profile, colophon, and advertising images remain bounded non-narrative evidence. No embedded bonus fiction was found.

The extraction produced 7,047 non-empty text/image locator rows and 7,133 reading lines. The locator TSV SHA-256 is `32ac689226ca5d46fdcd2e58f26d0cf27c72db1f0332720a1a420a5d61fc560e`; the reading projection SHA-256 is `d50cdfdc32a75c40c35cba05392b077805e4cb59c85f467ed0425814ea29f233`. Cover, color frontmatter, ten interior narrative images, and backmatter images were inspected and routed by role.

The afterword calls V06.5 `実質的な本編` and names multiple V06.5 elements as V07 dependencies. This supports the existing separate-but-linked supplemental architecture as bounded production testimony; it does not overwrite fictional evidence or make V06.5 a numbered-main freeze.

The complete main reading and its entering-state freeze are in `../02 Sequential Readings/CHIRAMUNE_V07_DEEP_READING.md` and `../02 Sequential Readings/CHIRAMUNE_V07_PROSPECTIVE_FREEZE.md`. The exact locked Volume 08 special-edition object was subsequently component-classified, and its complete main novel was frozen before the rough-illustration supplement was opened.

### Volume 08 special-edition main analysis disposition

The locked witness was independently reverified at 18,750,992 bytes and SHA-256 `124d66e237efd52873dca5bbff1141a56dcad30821365da69553b54e2955dc03`. OPF metadata identifies `千歳くんはラムネ瓶のなか　８　ラフイラスト集付き特装版`, 裕夢, 株式会社小学館, Japanese, and modification timestamp `2023-06-12T00:00:00Z`.

The exact spine was classified before interpretation. `p-0001`–`p-0009` contain cover/title/frontmatter/contents; the complete main novel runs from prologue `p-0010` through two chapters `p-0011`–`p-0032`; the main afterword is `p-0033`. The separately titled `『千歳くんはラムネ瓶の中８』 ラフイラスト集` occupies `p-0034`–`p-0083` and remained unopened throughout the main transaction. Author profile, colophon, and advertising follow.

The main-only extraction produced 4,977 non-empty locator rows and 5,047 reading lines. The locator TSV SHA-256 is `4ec83a133c29de2c772ac38af5a3d1b27a0640fc8a1412c990e759297c4a7e04`; the reading projection SHA-256 is `8aeabf3e37a4e65e9c091064c969908a179832c28ee03bddc440ee2a9109526a`. Cover, principal frontmatter, two color spreads, and ten narrative illustrations were inspected; supplement pages were excluded.

The afterword states that V08 and V09 were conceived as one story and that V08 intentionally ends after two chapters before the festival. This is bounded production testimony, not a license to predict V09. The complete main reading and entering-state freeze are `../02 Sequential Readings/CHIRAMUNE_V08_MAIN_DEEP_READING.md` and `../02 Sequential Readings/CHIRAMUNE_V08_MAIN_PROSPECTIVE_FREEZE.md`.

### Volume 08 rough-illustration supplement disposition

After the V08 main checkpoint passed local, GitHub, and exact fresh-clone validation at commit `8aaa45acb17d40dc81e03fefb29a464b7cc83134`, the separately titled `『千歳くんはラムネ瓶の中８』 ラフイラスト集` at `p-0034`–`p-0083` was inspected page by page.

The component contains 50 XHTML pages routing 50 JPEG resources totaling 10,577,106 bytes. The SHA-256 of the UTF-8 page/file/dimension/size/file-hash manifest is `c028da414ed88216103db58666125aaf070d686259cdf00243bb7042d8dbe791`.

Its own contents declare four chapters: character-design proposals, V01–V03 cover rough proposals, a selected rough gallery, and guest illustrations. Its colophon and back cover close a separate art-book topology. The component is classified `PRODUCTION_PARATEXT`, not narrative supplement. Alternative designs, rough/final stages, and artist-signed guest works create no new diegetic events, chronology, character state, or relationship fact. See `../02 Sequential Readings/CHIRAMUNE_V08_ROUGH_ILLUSTRATION_SUPPLEMENTAL_READING.md`.

The next safe source was the exact locked Volume 09 main EPUB.

### Volume 09 analysis disposition

The locked Volume 09 witness was independently reverified at 5,549,138 bytes and SHA-256 `3e2de8091542d4658884dd069ede4d64b9587248dbd1e3c30905684b435335eb` before prospective reading. OPF metadata identifies `千歳くんはラムネ瓶のなか　９`, 裕夢, 株式会社小学館, Japanese, and modification timestamp `2024-08-09T00:00:00Z`. The colophon records electronic publication on 2024-08-20, print-base publication on 2024-08-25, and ISBN 978-4-09-453203-6.

The exact spine contains frontmatter `p-0001`–`p-0009`, Chapter 3 `結んで、解いて` at `p-0010`–`p-0024`, Chapter 4 `悠な月` at `p-0025`–`p-0029`, epilogue `七瀬悠月` at `p-0030`, afterword at `p-0031`, and bounded backmatter at `p-0032`–`p-0035`. Continued chapter numbering completes the V08 festival story while preserving V09 as a distinct `MAIN_LN` source and freeze. No embedded bonus fiction or separately titled supplement was found.

The extraction produced 5,571 non-empty locator rows and 5,641 reading lines. The locator TSV SHA-256 is `9bc0adec392041db4ad6efa7b47553ca5b1fa2b733079f3b6e0a66e30ab1ec3e`; the reading projection SHA-256 is `3ce61e6a34a4620191c7feed6af138408c32087610ebef47abebdb95e7f95eb9`. Cover, five frontmatter images, nine narrative illustrations, and two backmatter images were inspected and bounded by role.

The afterword announces a 2025 television anime, explains the more-than-one-year delay in relation to that announcement, and describes a 2024 Fukui collaboration. These are source-era production statements, not current-status verification or diegetic evidence. The complete reading and freeze are `../02 Sequential Readings/CHIRAMUNE_V09_DEEP_READING.md` and `../02 Sequential Readings/CHIRAMUNE_V09_PROSPECTIVE_FREEZE.md`.

The next safe source is the exact locked *Days of Endless Summer* EPUB. It must be classified component by component before fiction enters the longitudinal corpus.

### *Days of Endless Summer* analysis disposition

The locked collection witness was independently reverified at 11,663,969 bytes and SHA-256 `24a92c80666b95658a2c2e6ab03434996233cb9357cea9981da3fc6566455c39` before opening. OPF metadata identifies `千歳くんはラムネ瓶のなか Days of Endless Summer`, 裕夢, 株式会社小学館, and Japanese; the colophon records electronic publication on 2025-08-20, a 2025-08-25 print base, and ISBN 978-4-09-453257-9.

The exact package contains 152 extracted files, 93 linear XHTML spine entries, and 50 JPEG assets. Its fiction graph contains 36 republished stories in seven provenance groups plus one newly written long story. All 50 images were inspected and bounded by role. Extraction produced 3,094 non-empty locator rows and 3,280 reading lines; the locator TSV SHA-256 is `574272d8ac39d4d978f27e7129651c8de1f2c0bdc1358ce59be9d950ca2de6ac`, the reading projection SHA-256 is `dba2217ee070e0b0e09198ade530df6cab6618a84776f9e2aee9e0495ca07eed`, and the image-inventory SHA-256 is `ade9401ea9dd69465e9e51cf7bf118116e4c3cf8679991276e24cf6877327d13`.

The 36 republished stories retain individual earlier diegetic placements and enter as later-admitted testimony rather than rewriting their main-volume freezes. `長く短い祭りのあと` is the only newly written current bridge: it occurs the day after the culture festival and before the Okinawa class trip. The afterword supplies bounded production history, including the author's anime-script participation; it does not admit the anime into the novel evidence plane. The complete component graph and checkpoint are `../02 Sequential Readings/CHIRAMUNE_DAYS_OF_ENDLESS_SUMMER_SUPPLEMENTAL_READING.md`.

The next safe source is the exact locked Volume 09.5 witness.

### Volume 04 analysis disposition

The locked Volume 04 witness was reverified at SHA-256 `96113f9d92616084144ea06172ad5ea1dee54e1f5b53ed872a717d4e5bac4470` before prospective reading. Its complete narrative, ten interior narrative illustrations, frontmatter, afterword, author profile, colophon, and advertising backmatter were classified. No embedded bonus fiction was found. The narrative and V04 freeze are complete; the known `mimetype` ZIP-order warning remains a packaging-only defect.

### Volume 03 booklet

The illustration/SS booklet is a separate acquired purchase-bonus object. The Volume 03 mainline reading froze before the booklet was opened. The exact booklet hash was then independently reproduced and the object was classified `SUPPLEMENTAL_MAINLINE`.

Its colophon dates publication to 2020-04-17 and identifies 裕夢 as author, raemz as illustrator, BOOK☆WALKER as producer, and Shogakukan's Gagaga Bunko editorial department as cooperating publisher. Its untitled story is a late-V03 interstitial set after Saku and Asuka return from Tokyo and separate at Fukui Station, but before the following Monday sequence. Because the object explicitly warns of major V03 spoilers, its safe prospective insertion boundary remains after the complete V03 main freeze. See `../02 Sequential Readings/CHIRAMUNE_V03_SUPPLEMENTAL_BOOKLET_READING.md`.

### Half-volumes and side stories

Volume 06.5 is integrated through its four-component late-August checkpoint while preserving the V06 main freeze. Volumes 07, V08 main, and V09 main are independently frozen after that checkpoint. The V08 rough-illustration collection is separately integrated as `PRODUCTION_PARATEXT`. *Days of Endless Summer* is integrated through a 37-component graph that preserves original provenance, individual placement, and duplicate-event controls. Volume 09.5 still requires publication/diegetic classification before longitudinal integration. Its existence does not authorize retroactive leakage into earlier prospective reading states.

## Completeness claim and limit

The current lock supports the claim **core Japanese light-novel corpus acquired through Volume 09/09.5 with the listed major supplements represented**.

It does **not** support the stronger claim that every retailer-exclusive purchase bonus or ephemeral promotional short story ever distributed has been acquired. Newly acquired official material must be added through a new source-lock revision with stable identity and integrity verification before it becomes part of the analytical source boundary.

## Git publication boundary

The EPUBs are primary-source artifacts and remain outside analytical Git. Git may contain original analysis, source hashes, stable Drive IDs, source locators, and narrowly necessary quotations under the project's publication policy. It must not become a mirror of copyrighted source text or illustrations.
