---
series: RE_ZERO
artifact_type: source_lock
scope: SOURCE_ADMISSION_CONTRACT_AND_CURRENT_INVENTORY_STATE
generation: V0.12
status: canonical
release_state: mutable_active
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
---

# Re:Zero — source lock and inventory

## Current lock state

**PARTIALLY LOCKED — ACQUIRED JAPANESE MAIN-LN SPINE V01-V43.**

The governed evidence locations contain a continuous Japanese main-light-novel sequence from Volume 01 through Volume 43. Those 43 objects are admitted as `MAIN_LN` witnesses. Forty-two main-volume files retain exact agreement with the 2026-08-31 manifest; the current V41 object was replaced after that manifest and is admitted under the bounded 2026-09-08 point re-audit recorded below.

This is **not a claim that the acquired corpus is current-complete**. A bibliographic freshness check on 2026-09-04 against official KADOKAWA/Re:Zero publication surfaces establishes that Volume 44 was released on 2026-03-25 and Volume 45 on 2026-06-25. Neither appears in the audited 2026-08-31 Drive manifest. The known current main-spine acquisition gaps are therefore **V44 and V45**.

The gap does **not** block a prospective Volume 01 reading. It prohibits describing the present acquisition as a complete-to-date Re:Zero main-light-novel corpus.

## Authority responsibility

This file owns the Git-side record of **which Re:Zero source witnesses are admitted for analysis and what each witness is allowed to support**.

Primary-source binaries, extracted prose, and detailed per-object audit data remain in the governed evidence plane. Git records the current admission decision, deterministic source identifiers, provenance anchors, integrity summary, known gaps, and analytical horizons.

The detailed per-file SHA-256 values remain authoritative in the Drive audit manifest identified below for the 44 audited objects whose current bytes still match it. V41 is the sole exception and is governed by the exact point-re-audit record below. Duplicating the entire otherwise unchanged machine inventory in this mutable analytical file would create two competing audit surfaces.

## Governed evidence anchors

- Primary-source Drive root: `1tNJvglC-ri_AEGTkJupZ78WddyiCqQMy`
- Re:Zero evidence folder: `14WoHQWhJ4rCtvLrrZpiwVXgnSJh37YOo`
- Drive audit manifest file: `16-fjuvDSqFGRdSoOE-WJy3uFBRwCYmgK`
- Manifest title: `audit_manifest.json`
- Manifest audit date: `2026-08-31`
- Manifest size: `23,584` bytes
- Manifest SHA-256 as retrieved for this admission audit: `3daa190cefda6ab894f5d62ff547a93856c8133f2d4fc1cbc552b99d73c73314`
- Current V41 Drive file: `1t2ppNA9sPYT4OFwZK0nG1Px1b7nc0Aon`

Normalized English filenames are locators only. Embedded Japanese titles and Japanese prose remain the semantic anchor.

## Observed Drive audit

The manifest records:

- `43` primary Japanese EPUB files representing distinct numbered main volumes V01-V43;
- no missing number inside V01-V43;
- `1` English alternate-edition EPUB for Volume 21, stored separately;
- `1` archived byte-identical duplicate of Japanese Volume 31;
- `45` audited EPUB objects total;
- all `45` passing ZIP CRC and EPUB-container checks;
- `23` packaging-conformant objects and `22` non-fatal packaging-warning objects across the 45-object audit;
- no supplemental/EX/short-story, IF/alternate-route, web-novel, or audiovisual witness represented in the manifest.

A live 2026-09-08 rescan found no new EPUB, no V44/V45, no missing manifest path, and no extra path. Forty-four of the 45 current EPUB objects reproduce the manifest size and SHA-256. The one exception is Japanese V41, whose current Drive metadata and local governed source copy both report `14,208,152` bytes rather than the manifest's `14,207,851`; its bounded replacement audit is recorded below.

The manifest states that the packaging warnings are non-fatal and that affected books remain readable after CRC/container validation.

## Admitted main-light-novel set

The following range admission is deterministic and exhaustive for the current Japanese main-LN lock:

- source IDs: `RZ-MAIN-LN-JA-V01` through `RZ-MAIN-LN-JA-V43`;
- witness class: `MAIN_LN`;
- language: `ja`;
- folder-relative locators: `Re Zero - Volume 01.epub` through `Re Zero - Volume 43.epub`;
- integrity: exact per-file SHA-256 plus CRC/container audit in the anchored Drive manifest, except V41 which uses the 2026-09-08 point-re-audit override below;
- arc: `UNASSIGNED_PENDING_SOURCE_VERIFICATION`;
- publication dates: not supplied by the local audit manifest and not globally backfilled from memory;
- horizon: V01=`START`; each VNN after the frozen prospective analysis of VNN-1.

This ranged admission is allowed because the manifest explicitly enumerates all 43 objects, reports no missing volume in the range, and records one primary Japanese edition per numbered volume, while the sole current hash replacement has now received a bounded identity/integrity audit. Any future changed hash, replacement file, revised edition, or gap invalidates the affected admission until re-audited.

## Volume 41 post-manifest point re-audit

The live source audit on 2026-09-08 found that V41 was modified after `audit_manifest.json`. The manifest remains historical evidence of its audited snapshot but no longer supplies the current V41 hash.

Current V41 identity:

- source ID: `RZ-MAIN-LN-JA-V41` (stable source identity retained);
- Drive file ID: `1t2ppNA9sPYT4OFwZK0nG1Px1b7nc0Aon`;
- locator: `Re Zero - Volume 41.epub`;
- Drive size: `14,208,152` bytes;
- governed local-source size: `14,208,152` bytes;
- current SHA-256: `abd148204c4cdd2cc52bde40fa399910fcb83661902b3ae98d16d249a2c04120`;
- language: Japanese (`ja`);
- embedded title: `Re：ゼロから始める異世界生活 41`;
- embedded creators: `長月　達平` and illustrator `大塚　真一郎`;
- publisher/label: `株式会社ＫＡＤＯＫＡＷＡ` / `ＭＦ文庫Ｊ`;
- embedded BookWalker identifier: `04684890A21975100000`;
- electronic/print basis: `2025年6月25日`, `ver.001`, first edition dated the same day;
- container root: `item/standard.opf`;
- package: 61 ZIP files, 23 manifest image resources, reflowable Japanese EPUB;
- integrity: NanaZip full-archive test passed; EPUB container metadata and package document resolved;
- packaging: non-fatal warning remains because `mimetype` is stored but is not the first ZIP entry.

The current Drive object has one retained revision only, so the earlier manifest-hashed bytes are not available for a bytewise semantic comparison. The current object is nevertheless re-admitted as the same numbered Japanese MF Bunko J V41 witness because its exact present bytes, internal bibliographic identity, language, edition/version, publisher, container structure, and archive integrity were verified. This override is limited to V41. Any future size/hash change or a mismatch between a fresh Drive download and the recorded current hash reopens V41 admission.

## Known current main-spine acquisition gaps

These are bibliographic gap records, **not admitted witnesses**.

| volume | official publication date | official evidence | acquisition state | analytical state |
|---|---|---|---|---|
| V44 | 2026-03-25 | KADOKAWA product `322511001158`; ISBN `9784046858207` | `NOT_PRESENT_IN_2026-08-31_MANIFEST` | `UNREAD / NOT_ADMITTED` |
| V45 | 2026-06-25 | KADOKAWA product `322602000800`; ISBN `9784046602145` | `NOT_PRESENT_IN_2026-08-31_MANIFEST` | `UNREAD / NOT_ADMITTED` |

Official freshness-check surfaces:

- `https://www.kadokawa.co.jp/product/322511001158/`
- `https://www.kadokawa.co.jp/product/322602000800/`
- `https://www.re-zero.com/books/`

This external check establishes publication existence/date only. It does not substitute for acquisition, file identity, hashing, or source admission.

## Alternate edition and duplicate control

The Drive manifest records two non-primary objects.

### English Volume 21 alternate edition

- path: `English Editions/Re Zero - Volume 21 - English Edition.epub`
- language: `en`
- SHA-256: `2541ba1973ca9af00b0c726d816c5dd3af817d44d6f23a012595f81ac4890c38`
- role: retained convenience/comparison witness;
- current admission state: `NOT_ADMITTED_FOR_SEQUENTIAL_READING`.

It is semantically distinct from the Japanese Volume 21 primary witness and must never be merged into the Japanese text stream.

### Japanese Volume 31 archived duplicate

- path: `_duplicates/Re Zero - Volume 31 - duplicate.epub`
- SHA-256: `5de35db8f7eba4f307b3c12ce6326fd97eb50e0f97579f7ef6ec69f7200e0921`
- exact-byte match to canonical `Re Zero - Volume 31.epub`;
- role: provenance-only archived duplicate;
- current admission state: `ARCHIVED_DUPLICATE_NOT_SEPARATE_WITNESS`.

## Supplemental and alternate witness acquisition state

**No supplemental or alternate-route primary text is admitted by the current source audit.**

The 2026-08-31 manifest contains no Japanese short-story collection, EX volume, IF/alternate-route text, web-novel corpus, guidebook, bonus story, or audiovisual witness. Their existence in the broader Re:Zero publication ecosystem does not place them inside this lock.

As a freshness/horizon test only, the official catalog establishes that `Ｒｅ：ゼロから始める異世界生活　短編集１４` was released on 2026-07-24. It is not present in the audited folder and is not admitted. If later acquired, its **publication-safe horizon** is at least `AFTER_V45_FREEZE`; its final safe horizon remains `OPEN` until diegetic/route dependencies are independently established.

That example is not an exhaustive supplemental bibliography.

## Required admission record for future items

For a newly admitted source item record, directly or through an exact manifest-anchored range admission:

| Field | Requirement |
|---|---|
| `source_id` | stable analytical identifier |
| `witness_class` | class defined by `REZERO_ROUTE_AND_WITNESS_PROTOCOL.md` |
| `language` | source language |
| `edition/publisher` | verified identity or explicitly unknown |
| `title` | printed/encoded title |
| `main_volume` | global numbered volume when applicable |
| `arc` | source-verified arc identity when applicable |
| `publication_date` | verified or explicitly unknown |
| `provenance_anchor` | governed Drive/reference locator |
| `integrity` | exact hash/audit evidence when available |
| `analytical_horizon` | earliest prospective opening point |
| `notes` | ambiguity, duplicate, variant, or routing concern |

## Supplemental placement control

Acquisition does not authorize reading.

For every future non-spine witness record:

- `H_pub`: publication-safe main-volume horizon;
- `H_diegetic`: source-verified diegetic dependency horizon, if applicable;
- `H_route`: divergence/route dependency horizon for alternate-route material, if applicable;
- `H_final`: latest established dependency among them;
- placement confidence: `VERIFIED`, `PROVISIONAL`, or `OPEN`.

The governing calculation and abstention rules are in `00 Frameworks and Methods/REZERO_ROUTE_AND_WITNESS_PROTOCOL.md`.

If a material dependency may exceed the established horizon, leave the witness unopened and `OPEN`.

## Version and duplication control

If multiple files appear to represent the same work:

- compare edition metadata;
- compare hashes where available;
- distinguish true duplicates from revised editions, bonus-text variants, or extraction differences;
- do not silently deduplicate semantically distinct witnesses.

## Volume 01 readiness decision

`RZ-MAIN-LN-JA-V01` is **READY FOR PROSPECTIVE SOURCE-FACING ANALYSIS**.

Verified evidence:

- locator: `Re Zero - Volume 01.epub`
- language: `ja`
- embedded title: `Ｒｅ：ゼロから始める異世界生活 1`
- embedded creator: `長月達平`
- size: `8,923,805` bytes
- SHA-256: `aab6d2e98cc002101cba862ed21b3750891f5e8a291e37490a06b5ea500ed627`
- EPUB/container integrity: passed;
- packaging: non-fatal `mimetype` compression warning;
- no bundled later main volume is represented by the admitted object.

Therefore `02 Sequential Readings/REZERO_LN_V01_DEEP_READING.md` may now be created from this exact Japanese witness under the prospective-freeze method.

## Volume 03 consumption record

`RZ-MAIN-LN-JA-V03` has been consumed into the frozen prospective V03 reading and the source-verified V02–V03 estate-story checkpoint.

Verified identity at consumption:

- source ID: `RZ-MAIN-LN-JA-V03`;
- Drive file ID: `1i9yf4dFhwpKclUgZI5rxTmb3TDdcSKIo`;
- locator: `Re Zero - Volume 03.epub`;
- language: Japanese (`ja`);
- embedded title: `Ｒｅ：ゼロから始める異世界生活3`;
- embedded creator: `長月達平`;
- embedded UUID: `431773eb-f119-4374-9cf7-cafc120bce17`;
- publication basis: Japanese MF Bunko J edition, 2014;
- size: `5,631,534` bytes;
- SHA-256: `6cdeb6d1f04566bdda39c9ef951ad6a33251987531dd9ff7cf2bce423d6d86b6`;
- manifest relation: exact size/hash agreement with the anchored 2026-08-31 Drive audit manifest;
- integrity: full archive test passed; 77 ZIP entries, including 20 image resources;
- analytical products: `02 Sequential Readings/REZERO_LN_V03_DEEP_READING.md` and `02 Sequential Readings/REZERO_ARC_ESTATE_STORY_CHECKPOINT.md`.

No V04 prose or previewed non-spine story was opened as part of this transaction. V04 remains admitted but analytically unopened until the user resumes the sequential run.

## Volume 04 consumption and resumed-source verification

The preceding paragraph records the historical V03 transaction, not the present opening state. The user resumed sequential analysis on 2026-10-19. The local governed source directory still supplies all 43 admitted Japanese numbered EPUBs. Their metadata/hash scan reproduces 42 manifest identities plus the already-admitted V41 override. The English V21 alternate and archived V31 duplicate are also present and reproduce their recorded hashes; neither was opened narratively. No V44/V45 or additional numbered source was found locally. This is a local acquisition check, not a fresh claim to exhaustive October publication coverage.

`RZ-MAIN-LN-JA-V04` was consumed in OPF spine order through the final publisher notice, with all 19 image resources visually inspected:

- locator: `Re Zero - Volume 04.epub`;
- language / embedded title: `ja`; `Ｒｅ：ゼロから始める異世界生活 4`;
- creator / publisher: `長月達平`; KADOKAWA / メディアファクトリー;
- UUID: `a492835f-e3b0-4837-a14a-730595c522f1`;
- package: `item/standard.opf`, 74 ZIP entries, 19 images;
- size: `9,686,186` bytes;
- SHA-256: `0439aebb5675d39e6705216db345e2faf4f780c4f15a7bc1bc7d88a18a0ed2ff`;
- manifest relation: exact size/hash agreement; manifest bytes/hash also reproduced;
- integrity: full ZIP CRC test passed; nonfatal compressed-`mimetype` warning;
- publication basis: Japanese MF Bunko J, 2014-06-30, ver.1.0;
- provenance: existing range admission under the governed folder/manifest anchors above; individual V04 Drive ID not separately resolved during local consumption;
- analytical product: `02 Sequential Readings/REZERO_LN_V04_DEEP_READING.md`, with internal block-locator convention and full coverage;
- source framing: author names `再来の王都編` as beginning here; no numeric LN arc or endpoint established.

V04's own V05 advertisement remains promotional paratext, not a V04 narrative gate prognosis or V05 source opening. The mentioned non-spine story remains unadmitted/unread. At that historical transaction, V05 and later narrative remained unopened until V04's complete publication gate; V05 consumption below occurred only after that gate closed.

## Volume 05 consumption record

`RZ-MAIN-LN-JA-V05` was consumed in exact OPF spine order through `p-bookwalker`, including all frontmatter, narrative, afterword, image columns, biographies and colophon. All 19 image resources were visually inspected.

- locator / title: `Re Zero - Volume 05.epub`; `Ｒｅ：ゼロから始める異世界生活5`;
- language / creator / publisher: `ja`; `長月達平`; KADOKAWA / メディアファクトリー;
- UUID: `198647d7-20df-47b5-9183-aec14335bd71`;
- size / SHA-256: `10,175,861` bytes; `d6c15d91fb0e67f25c9a9e02e225067f1aeb43c29b8db8ea121aadfeddf9c4a4`;
- package / integrity: `item/standard.opf`; 74 ZIP entries; 19 images; CRC test passed; nonfatal compressed-`mimetype` warning;
- manifest relation: exact size/hash agreement with the anchored manifest;
- edition basis: Japanese MF Bunko J; 2014-10-31 ver.1.0, first printing same date; afterword dated August 2014 separately;
- provenance: existing governed folder/manifest range admission; individual V05 Drive ID not separately resolved, not invented;
- analytical product: `02 Sequential Readings/REZERO_LN_V05_DEEP_READING.md`, with stable block locators, full coverage and bounded evidence planes.

At that historical V05 boundary no V06 source, supplement, IF, web-novel or audiovisual witness had been opened. V05's next-volume emphasis and promotional columns remain paratext, not later narrative evidence or a verified capital-section endpoint. V06 consumption below began only after the entire V05 atomic publication/audit gate succeeded. This record advances consumption, not admission or the historical publication-gap check.

## Volume 06 consumption record

`RZ-MAIN-LN-JA-V06` was consumed in exact OPF spine order through `p-bookwalker`: all 40 members, 3,669 nonempty text blocks in 20 prose members, all frontmatter, six chapters, afterword, image columns, biographies and colophon. All 20 source image resources were visually inspected.

- locator / title: `Re Zero - Volume 06.epub`; `Ｒｅ：ゼロから始める異世界生活６`;
- language / creator / publisher: `ja`; `長月達平`; KADOKAWA / メディアファクトリー;
- UUID: `07e0c98e-daf5-4dd3-a025-7dace78a6393`;
- size / SHA-256: `18,893,042` bytes; `924b0b2221b314911297a92579644bd9887c88bb7896625678150a3a88840ea5`;
- package / integrity: `item/standard.opf`; 74 ZIP entries, 40 spine members, 20 images; full CRC pass; nonfatal compressed-`mimetype` warning;
- manifest relation: exact size/hash match to anchored inventory;
- edition basis: Japanese MF Bunko J, 2015-03-31 ver.1.0/first-printing basis; author afterword February 2015;
- provenance: existing governed folder/manifest range admission; individual V06 Drive ID not separately resolved or invented;
- analytical product: `02 Sequential Readings/REZERO_LN_V06_DEEP_READING.md`, with reproducible block locators/full source-plane coverage;
- structural limit: author marks an achievement/restart and continuing counterattack, not closure of the named capital section.

At the historical V06 boundary V07 and every non-spine narrative witness remained unopened. Rem's domestic future is conditional speech within this admitted main-LN witness, not an IF source. Promotional manga/collection/goods/next-volume columns admit no later plot or extra edition. V07 consumption below began only after the complete V06 atomic publication/audit gate succeeded. Earlier freezes and source records retain their historical horizons.

## Volume 07 consumption record

`RZ-MAIN-LN-JA-V07` was consumed in exact OPF spine order through `p-bookwalker`: all37 members and3,493 body-order blocks (3,472 text +21 image-reference blocks), including frontmatter, narrative, afterword, design/image/promotional columns, biographies and colophon. All20 distinct source image resources were visually inspected, including lettering not captured as text.

- locator / title: `Re Zero - Volume 07.epub`; `Ｒｅ：ゼロから始める異世界生活 7`;
- language / creators / publisher: `ja`; `長月達平` / `大塚真一郎`; KADOKAWA;
- UUID: `412eb340-5e6f-474a-a860-03cad7f107d2`;
- size / SHA-256: `16,596,507` bytes; `d12ccb3b4ceb23a99166b940fdf85b250effd43151a4496794a634b41ecb89f1`;
- package / integrity: `item/standard.opf`;72 ZIP entries,37 spine members,20 images; full CRC pass; nonfatal compressed-first-`mimetype` warning;
- manifest relation: exact size/hash match to the anchored inventory;
- edition basis: electronic publication and stated first-edition/first-printing basis `2015-09-30`; afterword August2015;
- provenance: existing governed folder/manifest range admission; individual V07 Drive ID not separately resolved or invented;
- analytical product: `02 Sequential Readings/REZERO_LN_V07_DEEP_READING.md`; exact per-member coverage/block locators in §1;
- structural limit: one continuing V07-E1=V06-E2 state, no new Subaru death/return; Whale hunt ends, estate/Cult operation and private insurance/plan remain pending/withheld at dawn.

At the historical V07 boundary V08 and every non-spine narrative witness remained unopened. The design-page `モフっ子` note and `剣鬼恋歌` promotion remain bounded paratext. V08 below opened only after V07's complete source-audit, housekeeping and final actual exact-source full audit/status gate succeeded; earlier source records retain their horizons.

## Volume 08 consumption record

`RZ-MAIN-LN-JA-V08` was consumed in exact OPF spine order through `p-bookwalker`: all40 members and3,342 body-order blocks (3,320 text +22 image references), including all frontmatter, narrative, afterword, artist/promotional images, biographies, credits and colophon. All21 distinct image resources were visually inspected; repeated MFJ logo reference is not another distinct file.

- locator / title: `Re Zero - Volume 08.epub`; `Ｒｅ：ゼロから始める異世界生活 8`;
- language / creators / publisher: `ja`; `長月達平` / `大塚真一郎`; KADOKAWA / Media Factory;
- UUID: `dce9259f-d159-4958-af30-f0b2b657189f`;
- size / SHA-256: `20,623,478` bytes; `cd8c390f910aef162e4015398c66ece29fc074ad3f4c2ad33469831641e70321`;
- package / integrity: `item/standard.opf`;77 ZIP entries,40 spine members,21 images; full CRC pass; nonfatal compressed-first-`mimetype` warning;
- manifest relation: exact anchored size/hash match; manifest reverified unchanged;
- edition basis: electronic issue `2016-03-25`; stated underlying first edition/first printing `2016-03-31`; afterword February2016;
- provenance: existing governed folder/manifest range; individual V08 Drive ID not separately resolved or invented;
- analytical product: `02 Sequential Readings/REZERO_LN_V08_DEEP_READING.md`, exact per-member coverage/block convention §1;
- prospective record: exact45 inherited questions/ten forecasts fixed before archive opening, record SHA-256 `bc11d128b96492cdcbceea79622a891ce09582df90ab45985f198cc94f001c62`;
- structural limit: V08-E1 continues V07-E1/V06-E2/RZ-E-011 until Subaru death eleven; world flow narrated without successor arrival/checkpoint, no capital-section closure.

At the historical V08 boundary V09 and all non-spine narrative remained unopened. In-volume artist/promotional pages are paratext, not current Rem/Beatrice appearances or admission of advertised WN/anime/manga. Source identity/image-byte/prospective/prior-freeze guards passed; consumption rests on ordered full reading and visual inspection, not structural parsing alone. All seven earlier volume freezes and estate checkpoint remained unchanged. V09 below opened only after the complete V08 publication gate closed; admitted range and historical bibliographic-gap check do not advance.

## Volume 09 consumption record

`RZ-MAIN-LN-JA-V09` has been consumed through `p-bookwalker`: all44 OPF spine members and3,830 body-order blocks (3,806 text +24 image references), including frontmatter, narrative, internal escape-family fragment, afterword, artist/promotional pages, biographies, credits and colophon. All22 distinct image resources were visually inspected. One reading-order exception is disclosed below rather than described as flawless spine order.

- locator / title: `Re Zero - Volume 09.epub`; `Ｒｅ：ゼロから始める異世界生活 9`;
- language / creators / publisher: `ja`; `長月達平` / `大塚真一郎`; KADOKAWA / Media Factory;
- UUID: `9d0da354-8c4c-48df-a2f6-40e5fb94fd28`;
- size / SHA-256: `16,078,989` bytes; `5dc5fb10375bdcde0772e14ecf388f49c7a96e1772fd16307868e12d46d8e951`;
- package / integrity: `item/standard.opf`;82 ZIP entries,44 spine members,22 distinct images; full CRC pass; nonfatal compressed-first-`mimetype` warning;
- manifest relation: exact anchored size/hash match; manifest SHA-256 `3daa190cefda6ab894f5d62ff547a93856c8133f2d4fc1cbc552b99d73c73314` unchanged;
- edition basis: electronic issue `2016-09-23`; stated underlying first edition/first printing `2016-09-30`; afterword August2016;
- provenance: existing governed folder/manifest range; individual V09 Drive ID not separately resolved or invented;
- analytical product: `02 Sequential Readings/REZERO_LN_V09_DEEP_READING.md`, exact per-member coverage/block convention §1;
- prospective record: all50 inherited questions/ten forecasts fixed before archive opening, immutable record SHA-256 `072791ac49fbb1a2b2ac338b79f2f81387111002262bf9eae0a9b1c06a9e68a8`;
- structural boundary: council arrival RZ-E-012, actual death twelve/bedside arrival RZ-E-013; internal family not another return or current biography; explicit third-arc V04–V09 closure in afterword, not completed Rem restoration.

Reading-order exception: after the main-route nonrecognition line at `p-018#B0001`, `p275.jpg` was extracted/viewed before `p-019` prose. The exposure was immediately disclosed and interpretation quarantined; all209 `p-019` blocks were then read in order and the image reinspected at its actual `p-020` reference. No claim or prospective horizon was revised from the premature image; later argument rests on independently consumed prose. This is not an undisclosed perfect-order claim or an exposure to a later volume/non-spine source. The remaining ordered-consumption record accounts for all members/blocks/images, with no unresolved source gap.

Post-EOF exact source, manifest, image bytes, immutable prospect and all eight earlier freezes/estate-checkpoint guards passed. A structural guard does not prove reading; actual full text acquisition and visual inspection do. The internal married family is part of this MAIN_LN container under incompatible local premises, not admission of external IF/WN. Artist/promotional Rem/Emilia dialogue does not awaken current Rem or admit advertised anime/games/bonus witnesses. V10 and all separately acquired non-spine narrative remain unopened. At the V09 freeze the required next operation was the separately pending V04–V09 arc checkpoint, to be created only after V09's complete publication gate and closed before V10; its later completion record follows.

## Post-V09 third-arc checkpoint source boundary

`02 Sequential Readings/REZERO_ARC_03_CHECKPOINT.md` is a bounded synthesis of frozen V04–V09, created after V09 commit `ac38cbe884bdcd82919d34cfaea7fd3cacc4a46b` completed its exact-source publication gate. V09 `p-028#B0002–0004` verifies the third arc's V04 beginning and V09 closure; B0022 names the next arc. All six contributing EPUB SHA-256 identities were reverified read-only. The checkpoint uses their existing complete consumption/frozen evidence, not a new full reading or any additional witness. V09's image-order exception remains disclosed, not erased by synthesis.

No source is newly acquired/admitted/consumed, high-water remains V09, and all nine volume freezes/estate checkpoint remain unchanged. V09 §16's exact50-question/ten-forecast V10 prospect is retained, not hindsight-adjusted. The checkpoint's own approved commit/full-content remote readback, source audit, completed housekeeping and final actual exact-source full audit/status must pass before Japanese V10 opens. This record does not itself certify those future checks.

## Volume 10 consumption record

The separate third-arc checkpoint completed its exact-source publication gate at commit `ebd99a3cc5fe1806b094fbeddae5b6b2b37c0a06` before first V10 archive access. Its final actual full audit/status and completed housekeeping, not a dispatch's displayed branch label, controlled opening. The preceding checkpoint record preserves its then-pending future checks; they are now closed.

`RZ-MAIN-LN-JA-V10` was consumed in OPF spine order through `p-bookwalker`: all43 members/3,835 body-order blocks (3,812 text +23 image references). All22 distinct image resources were visually inspected at their references, including graphic text; repeated publisher logo reinspected at colophon. Actual acquired ranges/end cursors, reacquisition of lost output and visual inspection establish consumption; structural guards alone do not. One tiny informal artist-sketch mark is not reliably deciphered and supports no proposition; no narrative text gap remains.

- locator / embedded title: `Re Zero - Volume 10.epub`; `Ｒｅ：ゼロから始める異世界生活 10`;
- language / embedded creators / publisher: `ja`; `長月　達平` / `大塚　真一郎`; KADOKAWA / メディアファクトリー;
- UUID: `f0c1ea3f-bfae-419f-8287-3c870bbe1db5`;
- size / SHA-256:13,069,851 bytes; `92a5bbf737e25bac82e53ebaf4486d26ba89a97976d2ed21773a83e2c8f1a1b8`;
- package / integrity: `item/standard.opf`;81 ZIP entries; full CRC pass; nonfatal first-but-compressed `mimetype` warning;
- manifest: exact size/hash match to anchored manifest, unchanged SHA-256 `3daa190cefda6ab894f5d62ff547a93856c8133f2d4fc1cbc552b99d73c73314`;
- edition: electronic issue2016-10-25; stated first edition/first printing2016-10-31; afterword September2016 separately;
- provenance: governed folder/manifest range admission; individual V10 Drive ID unresolved, not invented;
- analytical product: `02 Sequential Readings/REZERO_LN_V10_DEEP_READING.md`, exact member/block/image coverage and locator convention §1;
- pre-opening prospect: all50 inherited questions/ten forecasts sealed, immutable record SHA-256 `cfe4058aa3177c9aed98ab876c3e7ff498fe9c69e1005ee297eae1508b6c6276` unchanged;
- ending: V10-E1 continues E013 until death13; restart declared without represented arrival,13 arrived segments/no E014; no collateral fate census;
- structure: afterword verifies fourth-arc beginning, not ending; parent trial is memory-based construction, not actual Earth receipt or external IF;
- guards: post-EOF source/manifest/image bytes/prospect and all eleven earlier frozen artifacts unchanged; no raw source/private acquisition objects committed.

V11 and all separate non-spine narrative remain unopened. V10 §16 fixes55 V11 questions/ten forecasts now, before the earned Subaru V01–V10 model/separate first fidelity audit. That operation follows V10's complete publication gate and must close before V11, without altering the prospect or admitting another witness. The source high-water becomes V10 only after the gate; admission range and historical gap check do not advance.

## Current source-state summary

- **Acquired/admitted Japanese main LN:** V01-V43 continuous.
- **Known published but not acquired/admitted main LN:** V44-V45.
- **Admitted translations:** none.
- **Retained non-admitted translation:** English V21, local hash reverified on resumption.
- **Admitted supplemental/EX/short-story:** none.
- **Admitted IF/alternate route:** none.
- **Admitted web novel:** none.
- **Admitted anime/audiovisual:** none.
- **Consumed into frozen prospective main-LN analysis:** V01-V10, effective after the complete V10 publication gate.
- **Next source acquisition priority:** Japanese V44 and V45 before the sequential read reaches that boundary.
- **Next analytical operation:** `SUBARU_V01_V10_MODEL_AND_FIDELITY_AUDIT` after V10's full gate; V11 remains unopened with55-question/ten-forecast horizon fixed, and opens only after that separate operation's complete gate.
- **Current execution state:** active continuous run; terminal V43 unchanged; model construction adds no new source or admission. No real-parent message, current IF-family biography, adaptation judgment or full-series completion is implied.
