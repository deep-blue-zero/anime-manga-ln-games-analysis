---
title: "Medalist — Continuous-Run Authorization, Publication Ceiling and Source Receipt"
artifact_id: "MEDALIST_CONTINUOUS_RUN_AUTHORIZATION_AND_SOURCE_RECEIPT"
artifact_type: "source_admission_authorization_receipt"
series: "Medalist / メダリスト"
series_id: "medalist"
generation: "MEDALIST_BOOTSTRAP_V1"
version: "1.0"
status: "canonical"
scope: "Owner continuous_sequential authorization, as-of-start publication ceiling, locked target inventory, structural witness verification and entering state"
canonical_home: "series/medalist/07 Audits and Handoffs/MEDALIST_CONTINUOUS_RUN_AUTHORIZATION_AND_SOURCE_RECEIPT.md"
source_boundary: "Japanese V01 closed at activation; V02–V15 and both fanbooks structurally verified only; no later narrative inspected at this snapshot"
created: "2026-10-12"
review_status: "OWNER_AUTHORIZED_CONTINUOUS_RUN_AUTHOR_VERIFIED_ACTIVATION"
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
do_not_use_as_literary_evidence: true
recommended_reasoning_class: "BOUNDED_STANDARD"
---

# Continuous-run authorization, publication ceiling and source receipt

This is an activation snapshot, not a reading-completion receipt. It records the owner's new execution-scope authorization, the dated publication ceiling that bounds it, the locked target inventory and the structural state of each candidate witness **before any V02 page was narratively read**. The historical [V01 authorization/source receipt](MEDALIST_V01_AUTHORIZATION_AND_SOURCE_RECEIPT.md) and [bootstrap receipt](MEDALIST_BOOTSTRAP_RECEIPT.md) keep their original snapshots; neither is superseded.

## Owner authorization

On 2026-10-12 (America/New_York) the owner issued a governing task specification and instructed its execution. Its operative terms, recorded here in the owner's own formulation:

- "**This instruction is the owner's new authorization for `continuous_sequential` execution** from the first uncompleted Japanese tankobon volume (expected V02) through the **complete, independently verified publication boundary as of the start of this run**."
- The authorization "removes the prior V01-only *execution-scope* restriction; it does not override initiation, source, integrity, authority, privacy, or publication controls. Do not ask for new approval between normally completed volumes within this fixed run."
- It also authorizes "evidence reconnaissance and, conditionally, full paratext audits for Official Fanbooks 01 and 02 **only at a verified safe manga checkpoint**"; an unestablished coverage boundary leaves that book unadmitted.
- "Anime/film audiovisual analysis is not authorized by this request."
- "Material published afterward requires a new run authorization."
- After the manga units close, evidence-grounded **provisional** character, relationship, specialist and integrated syntheses are authorized at the locked boundary; the series stays ONGOING.

The accompanying chat instruction repeats that V01 is frozen and must not be redone, that each volume transaction must be completed and verified before advancing, and that the run stops only at the verified terminal boundary or a genuine documented blocker. This is `continuous_sequential` under the corpus continuation policy; it changes cadence, not evidence rules.

## Recovered live state at activation

| Item | Verified value |
| --- | --- |
| Repository / branch | `deep-blue-zero/anime-manga-ln-games-analysis`, stable branch `series/medalist` |
| Branch tip | `f97675eddc8a81554462302b9bada1fc23ef65e0` (housekeeping child of authored `26233cb5f2f1048a21bbbad1113d71c3efb1b23c`); successful `Repository integration audit` status read back on that exact SHA |
| `origin/main` | `0ed395926cca502fe1461d8c172330baab99e70e`, an ancestor of the branch tip; no reconciliation needed at activation |
| Authority | Epoch 1, `GIT_ACTIVE_STABILIZING`; scope file SHA-256 reproduced as `008b7b2a…6ed0916`; protected activation tag dereferences to `01561d0c…7e98` |
| Entrypoint before this change | Version 0.4, `SEQUENTIAL_ANALYSIS_LOCK = OPEN`, `single_operation` V01 `COMPLETED`, high-water mark V01, V02 `NOT_AUTHORIZED` |
| Completed readings / freezes | One: V01, `MD-FR-V01`; seven ledgers at version 1.0; 13 claims at version 1; no `MD-PR`/`MD-RV` |
| Concurrent work | None found: no other author commit, open pull request or local worktree change on this root |

No other agent had advanced the branch. V01 is consumed as the frozen entering state for V02.

## Publication ceiling: as-of-start terminal snapshot

Observation date **2026-10-12, America/New_York** (provider timestamps may read 2026-10-13 UTC). These are publication-metadata observations; no chapter narrative was opened to obtain them.

| Record | Observation | Confidence / limit |
| --- | --- | --- |
| Collected ceiling | Kodansha's [series page](https://afternoon.kodansha.co.jp/c/medalist.html) lists **V15**, released 2026-07-22, as the latest volume; no V16 or later release notice appears. | HIGH for the page state on the observation date. |
| V15 Score range | The delivered V15 EPUB navigation lists **Scores 57–61**, ending with Score 61. A publisher product-record excerpt returned by search gives first publication as Afternoon 2026 January and March–August issues. | HIGH for the witness navigation (to be confirmed page by page when V15 is read); MODERATE for the product-record excerpt, because the product page itself refused direct retrieval. |
| Last serialized installment | The official Afternoon [August 2026 issue page](https://afternoon.kodansha.co.jp/afternoon/2026/08.html) (on sale 2026-06-25) lists メダリスト. [Comic DAYS](https://comic-days.com/magazine) still shows `score61 螺旋の途中②`, dated 2026-06-25, as the series' latest entry. | HIGH: two independent official records agree. |
| Later issues | The official [September](https://afternoon.kodansha.co.jp/afternoon/2026/09.html) (on sale 2026-07-24), [October](https://afternoon.kodansha.co.jp/afternoon/2026/10.html) (2026-08-25) and [November](https://afternoon.kodansha.co.jp/afternoon/) (2026-09-25) issue contents omit メダリスト. | HIGH for those three issue listings. They are complete official tables of contents, not a single absent listing. |
| Hiatus | A [news report](https://news.denfaminicogamer.jp/news/2609042p) dated 2026-09-04 relays the official account's notice that the series is on hiatus "制作上の都合により" with no resumption date. This agrees with the notice text the source map already holds as `MD-PUB-005`. | MODERATE as a secondary relay; the primary endpoint refused retrieval today. No resumption announcement was found. |
| Next issue | The December 2026 issue is expected on 2026-10-23, **after** this snapshot. | Not observed; outside this run by definition. |

**Locked terminal boundary: Japanese V15, ending at Score 61.** The collected ceiling and the serialized ceiling coincide: every installment published before the hiatus is collected in V15, so **no serial-only Score exists beyond V15 at this snapshot** and no `MEDALIST_SCORE_NNN_SERIAL_DEEP_READING` unit is scheduled. Score 61's two online installments (① and ②) are delivery segments of one Score. Anything published on or after the December 2026 issue, including a resumption chapter or a V16, needs a new run authorization. This ceiling is a dated observation, not a claim that the series has ended.

## Locked target inventory

Fourteen whole-volume transactions in numerical order, V02 through V15, each from one delivered Japanese witness on local route `MD-LOCAL-001`. Every container below passed a full ZIP CRC test, a complete decode of every image, and a per-container SHA-256 that matches the retained prior audit manifest. These are delivered-witness integrity facts. They do not authenticate a printing, and they are not narrative inspection.

| Unit | Source key | Container | Bytes | SHA-256 | Image occurrences | Typical pixels |
| --- | --- | --- | ---: | --- | ---: | --- |
| V02 | MD-MG-JP-TB-V002-W01 | CBZ | 99,839,392 | `03e206204d9e7bfb7b1e17456679edf9be2084d22263685e37eb682295a8a1ba` | 203 | 1530×2160; one 3060×2160 |
| V03 | MD-MG-JP-TB-V003-W01 | CBZ | 93,218,009 | `784ace216c600128205017a37b0d6d5ab69600f736322185f67e68f4d0d17805` | 203 | 1530×2160; one 3060×2160 |
| V04 | MD-MG-JP-TB-V004-W01 | CBZ | 95,294,653 | `b9608799a7358bbf63599d2d9f0f25bf6622091c7f39a304bbf44d8a8ff5bbfa` | 203 | 1530×2160; one 3060×2160 |
| V05 | MD-MG-JP-TB-V005-W01 | CBZ | 93,725,908 | `3e37c3a2bc03eefe46a06845faa0e7f3d1f7f4f142daf361ccea23353bd797c4` | 187 | 1530×2160; one 3060×2160 |
| V06 | MD-MG-JP-TB-V006-W01 | CBZ | 99,993,702 | `7ecbf94f03960c6a28879692a5241c76765cb99889da5be426cd5b8fe4777ee9` | 205 | 1530×2160; one 3060×2160 |
| V07 | MD-MG-JP-TB-V007-W01 | CBZ | 95,119,576 | `fc4b9defb25939f446ab22822d9b2340e1decf9f2f92b02f493584b17d36deb4` | 203 | 1125×1600 |
| V08 | MD-MG-JP-TB-V008-W01 | EPUB | 86,261,616 | `a506d396e29de7eb89796ad7bf191a01d32f6ba92864f55107d281bbf558db86` | 187 | 1125×1600 |
| V09 | MD-MG-JP-TB-V009-W01 | EPUB | 100,518,565 | `3ed1853cf7d76fbc182f8adb155969eb75f4fb0344a5eb64ed318b756ad5e816` | 203 | 1125×1600; one 1350×1920 |
| V10 | MD-MG-JP-TB-V010-W01 | CBZ | 105,504,581 | `c8386a98bb46255c6c197a8a81d47b820385950bd557c9c1cf27cfadeb8bb8c8` | 203 | 1125×1600 |
| V11 | MD-MG-JP-TB-V011-W01 | CBZ | 112,756,000 | `9a62b599a7f63ae05fb9de0cbf33b3599bc03232fb05c291ca0c1068cf513479` | 203 | 1125×1600 |
| V12 | MD-MG-JP-TB-V012-W01 | CBZ | 89,187,470 | `000a1e1b869f4654881985d31eff005660fab2b084fa1d7278b9317aeddee6a4` | 171 | 1125×1600 |
| V13 | MD-MG-JP-TB-V013-W01 | EPUB | 94,128,894 | `995df762df6d2dd376e581bc136dde9f473a601764dc7f6d67047c5ec26d4d75` | 203 | 1125×1600 |
| V14 | MD-MG-JP-TB-V014-W01 | EPUB | 115,194,640 | `57d1d9b915b3a375fa1dc5070aca376911c63bd857d12e11bbf2b6685209b960` | 256 | 1125×1600 |
| V15 | MD-MG-JP-TB-V015-W01 | EPUB | 98,048,078 | `ff5e8d1929625d2c35116ec32e18d33ef76a3204484ae6c5f55b9d57359531d9` | 221 | 1125×1600 |

Structural notes that bound later claims:

- **CBZ volumes** carry sequential `NNNN.jpg` members plus a builder-generated `ComicInfo.xml`, which is packaging metadata. Their Score ranges are not exposed by the container and are established only by reading each volume. Each of V02–V06 has one double-width image; whether it is a padded cover, as in V01, is decided on inspection.
- **EPUB volumes** are fixed-layout image books: every spine document resolves, each references exactly one image, no image is unreferenced or repeated, page progression is right-to-left, and the spine holds no body text beyond markup. Their dialogue is in the page images. Their navigation documents give Score ranges: V08 Scores 29–32, V09 Scores 33–36, V13 Scores 49–53, V14 Scores 54–56 with an exhibition piece and a Short Program, V15 Scores 57–61.
- **V14** navigation also names a first-chapter sample of a different series after the Medalist contents page. It is scheduled for exclusion exactly as V01's unrelated preview was; the boundary image is confirmed when V14 is admitted.
- **V13–V15 alternates.** A local CBZ also exists for each of these volumes (keys `…-V013-W02`, `…-V014-W02`, `…-V015-W02`). Image counts equal the EPUBs, yet no image is byte-identical between formats, so page-by-page equivalence is unproved. The EPUB is the admitted default because its spine fixes reading order; a CBZ is a collation aid for a doubtful page, never a second independent reading.
- **Drive relation.** The local V13–V15 EPUB byte sizes equal the sizes the source map recorded for the Drive objects. No Drive bytes were retrieved in this run, so byte identity with the Drive copies remains unverified and is not claimed. The Drive evidence root and the local source directory were opened read-only; nothing was written to either.
- **English volumes** V01–V12 remain translation witnesses. None is admitted, and none was opened.

Locator conventions. CBZ units keep `medalist-cbz-image-occurrence-v1` from V01: one-based original image occurrence, original member name, verified Score or component, and a panel-region description in Japanese reading order. EPUB units use `medalist-epub-spine-image-occurrence-v1`: one-based spine ordinal, spine document, one-based image occurrence and image resource, then Score or component and panel region. In these EPUBs spine ordinal and image occurrence coincide, because each spine document holds one image. Printed pagination is recorded only where a page shows it. Facing-page geometry is unverified for every unit, so readings describe the inspected image sequence, not an authenticated spread or page turn.

## Fanbooks: authenticated, not admitted

| Unit | Source key | Bytes | SHA-256 | Image occurrences | Container date field | Disposition |
| --- | --- | ---: | --- | ---: | --- | --- |
| FB01 | MD-SUP-JP-FB01-W01 | 72,171,652 | `f976c90184d32bea0c81a720cab082e3748099a306f4c3af649940de8b5154f0` | 171 | January 2025 | `HOLD_COVERAGE_UNVERIFIED` |
| FB02 | MD-SUP-JP-FB02-W01 | 82,359,592 | `ef3263ded06b40100857bcea3d61308356d527d7c4dfff605b890806c408a176` | 203 | January 2026 | `HOLD_COVERAGE_UNVERIFIED` |

Both are fixed-layout image EPUBs whose navigation shows a contents page and three parts: a character guide, a story guide and a further-material part. That wrapper structure and the container date fields are all that was inspected; no profile, story-guide page, interview or bonus fiction was opened. A date field narrows when a coverage check becomes safe but is not a coverage boundary. Each book's `covered_manga_boundary` and `admit_after` stay null until a bounded coverage reconnaissance is run at a manga checkpoint late enough that the reconnaissance cannot disclose unread material. Until then synthesis is scoped manga-only.

## Capability and exposure

Capability was probed on two pages of the **already closed** V01 witness, so the probe itself disclosed nothing new. Full-resolution page images display with legible dialogue, furigana, handwritten figures and a small rule footnote; the readings match the frozen V01 observations at images 0044 and 0208. Original-resolution reinspection is available for small lettering. OCR is not used as reading evidence. Text-layer extraction would return nothing, since no container holds dialogue as text.

Exposure accrued during this activation, disclosed and not used as evidence:

- EPUB navigation displayed the Score title labels of V08, V09 and V13–V15. Several name later competition contexts. Only the Score number ranges are retained above.
- The hiatus report quotes an author statement that the pause falls partway through a match in the main story.
- Search results for publication records returned adaptation scheduling facts (a second television season and a film announcement). The adaptation lane stays unadmitted.
- V01's own marketing pages, the earlier publisher snippets and model familiarity with the franchise remain as disclosed in the V01 receipt. No reading in this run claims a blind reader.

Each volume's entering state is the preceding committed freeze. Later-volume files are extracted to the working plane only when their turn arrives.

## Run state and recovery contract

| Field | Value at activation |
| --- | --- |
| mode | `continuous_sequential` |
| unit_type | Japanese tankōbon volume |
| authorized_start | V02 |
| terminal_boundary | V15 (Score 61), fixed at the 2026-10-12 snapshot |
| committed_high_water_mark | V01 |
| next_candidate_operation | V02 |
| confirmation_between_units | false |
| run_state | active |
| supplemental lane | Coverage reconnaissance and conditional audits authorized at a verified safe checkpoint; zero completed |

The [entrypoint](../CURRENT_STATE_AND_CORPUS_MAP.md) owns live progress and is the only surface to trust after an interruption. Recovery reads the remote branch head and its exact-head status, the entrypoint's `sequential_execution` block, the last `MD-FR-VNN` actually present in `02 Sequential Readings/`, and the ledger versions; a drafted but uncommitted reading has not advanced the high-water mark. Raw containers, extracted page images, per-batch reading notes, coverage manifests and publication receipts stay in the working plane outside Git. This receipt claims neither its own commit SHA nor any future audit result.
