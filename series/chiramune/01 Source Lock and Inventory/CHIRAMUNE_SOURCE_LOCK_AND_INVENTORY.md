---
series: CHIRAMUNE
artifact_type: source_lock_and_inventory
scope: ACQUIRED_JAPANESE_EPUB_CORPUS
source_boundary_date: 2026-08-29
generation: V0.8
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

The complete main reading and its entering-state freeze are in `../02 Sequential Readings/CHIRAMUNE_V07_DEEP_READING.md` and `../02 Sequential Readings/CHIRAMUNE_V07_PROSPECTIVE_FREEZE.md`. The next safe source is the exact locked Volume 08 special-edition object. Its complete main novel and rough-illustration supplement must be technically distinguished and routed separately before either is analyzed.

### Volume 04 analysis disposition

The locked Volume 04 witness was reverified at SHA-256 `96113f9d92616084144ea06172ad5ea1dee54e1f5b53ed872a717d4e5bac4470` before prospective reading. Its complete narrative, ten interior narrative illustrations, frontmatter, afterword, author profile, colophon, and advertising backmatter were classified. No embedded bonus fiction was found. The narrative and V04 freeze are complete; the known `mimetype` ZIP-order warning remains a packaging-only defect.

### Volume 03 booklet

The illustration/SS booklet is a separate acquired purchase-bonus object. The Volume 03 mainline reading froze before the booklet was opened. The exact booklet hash was then independently reproduced and the object was classified `SUPPLEMENTAL_MAINLINE`.

Its colophon dates publication to 2020-04-17 and identifies 裕夢 as author, raemz as illustrator, BOOK☆WALKER as producer, and Shogakukan's Gagaga Bunko editorial department as cooperating publisher. Its untitled story is a late-V03 interstitial set after Saku and Asuka return from Tokyo and separate at Fukui Station, but before the following Monday sequence. Because the object explicitly warns of major V03 spoilers, its safe prospective insertion boundary remains after the complete V03 main freeze. See `../02 Sequential Readings/CHIRAMUNE_V03_SUPPLEMENTAL_BOOKLET_READING.md`.

### Half-volumes and side stories

Volume 06.5 is integrated through its four-component late-August checkpoint while preserving the V06 main freeze. Volume 07 is now independently frozen after that checkpoint. *Days of Endless Summer* and Volume 09.5 still require publication/diegetic classification before longitudinal integration. Their existence does not authorize retroactive leakage into earlier prospective reading states.

## Completeness claim and limit

The current lock supports the claim **core Japanese light-novel corpus acquired through Volume 09/09.5 with the listed major supplements represented**.

It does **not** support the stronger claim that every retailer-exclusive purchase bonus or ephemeral promotional short story ever distributed has been acquired. Newly acquired official material must be added through a new source-lock revision with stable identity and integrity verification before it becomes part of the analytical source boundary.

## Git publication boundary

The EPUBs are primary-source artifacts and remain outside analytical Git. Git may contain original analysis, source hashes, stable Drive IDs, source locators, and narrowly necessary quotations under the project's publication policy. It must not become a mirror of copyrighted source text or illustrations.
