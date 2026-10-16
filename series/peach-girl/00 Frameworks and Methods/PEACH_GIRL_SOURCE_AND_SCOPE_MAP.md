---
title: "Peach Girl — Source and Scope Map"
artifact_id: PEACH_GIRL_SOURCE_AND_SCOPE_MAP
artifact_type: source_scope_map
series: "Peach Girl / ピーチガール"
series_id: peach-girl
generation: PEACH_GIRL_BOOTSTRAP_V1
version: "0.2"
status: active_provisional
scope: "Sanitized witness identities, preliminary provenance, structural reconnaissance and admission gaps"
source_boundary: "Original Japanese 新装版 V01–V18; all 18 witnesses byte- and package-verified 2026-10-16; admission proceeds volume by volume under the authorized run"
canonical_home: series/peach-girl/00 Frameworks and Methods/PEACH_GIRL_SOURCE_AND_SCOPE_MAP.md
created: "2026-10-16"
observed_at_utc: "2026-10-16"
review_status: OWNER_EXECUTION_AUTHORIZED_LOCAL_RESULT_UNREVIEWED
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
do_not_use_as_literary_evidence: true
---

# Source and scope map

This is the single project-local inventory/admission home, subordinate to the [current entrypoint](../CURRENT_STATE_AND_CORPUS_MAP.md). It distinguishes live metadata, historical provenance reports and actual downloaded-byte inspection. It contains no story findings. Observation date is 2026-10-16 UTC, corresponding to the owner's 2026-10-15 evening in America/Denver.

## Canonical evidence route and prior infrastructure

Canonical primary/derived evidence root: Manga / Anime / LN / Games, Drive folder ID `1tNJvglC-ri_AEGTkJupZ78WddyiCqQMy`. The Peach Girl collection, Drive folder ID `1kxx4orHjiHg_CEI1fZyifjt8_e9WNmMp`, has 21 observed direct children: 18 numbered EPUBs and three provenance files, no child folders. A bounded direct-child listing with limit 100 returned this set; all 18 EPUB IDs, names, sizes and current parents were individually read and reconciled with the propagation manifest. No source object in this observed set was missing at metadata level.

The series/evidence inventory, Drive document ID `1bfPi00AKmELjeXmdCudU_4HqOknTIOODANEi12GDJFw`, independently routes this same folder as Japanese new-edition V01–V18. The evidence root's governing README, Drive document ID `1K5p3nbvCyNIkHrGID7iIp6KWx_k_yMZstEa6udHks1g`, keeps primary and deterministic derived evidence in Drive and interpretations in Git. The historical analytical Drive master index (ID `1o1oJ-LM7FgIzX-x8XQB34ucKYx-TeR8-`) was searched for Peach Girl and ピーチガール; no project route was found. It is a historical router, not stronger authority than current Git. A metadata-name search for Peach returned only the existing evidence folder among the connector's supported file classes; it is not an exhaustive search of unindexed private material.

At starting Git main `23f439fe7c9102760154def56ea7e50eca4b5984`, repository-wide title/alias search, registries, migration crosswalks, reference artifacts, all fetched branch names and commit-title search found no existing Peach Girl analytical project or partial bootstrap. The existing Drive ingestion infrastructure is retained and referenced, not replaced. Search absence does not prove there is no unindexed private artifact elsewhere.

## Bibliographic identity, separate from availability

| Fact | Primary reference and limit |
| --- | --- |
| Original title ピーチガール; creator 上田美和 / Miwa Ueda; publisher 講談社; serialization in 別冊フレンド | Publisher records for [original V01](https://www.kodansha.co.jp/comic/products/0000028867) and [original V18](https://www.kodansha.co.jp/comic/products/0000037013); import metadata independently reports Japanese title, author and publisher |
| Original collected structure reaches V18, marked complete | Original V01 released 1998-01-10; V18 released 2004-02-13. Publisher first-publication fields cover magazine issues 1997-10 through 2004-01; issue dates are not asserted as exact on-sale serialization dates |
| 新装版 is a separately identified edition, also through V18 | [New-edition V18](https://www.kodansha.co.jp/comic/products/0000047019) is marked complete: print 2017-03-13, electronic 2017-03-31, print ISBN 9784063920772; no claim that the Drive UUID is this ISBN/JDCN or that all editions are page-identical |
| 裏ピーチガール and ピーチガールNEXT are related separate publications | Publisher catalogs list [裏ピーチガール, three items](https://www.kodansha.co.jp/titles/1000001688) and [NEXT, eight items](https://www.kodansha.co.jp/titles/1000028921). Their narrative relation/continuity is unassessed here; both are excluded from this mainline scope |

Publisher records were consulted for bibliographic fields and related-work identity only. Promotional/search-result story descriptions are excluded from the evidence set and all analytical claims. No online synopsis or fan wiki substitutes for the Drive corpus. Published V18 and Drive V18 are independently identified facts; neither proves the internal completeness of the other.

## Provenance objects and verification strength

| Object | Stable Drive ID | What was actually inspected |
| --- | --- | --- |
| CALIBRE_IMPORT.md | `1nU1C5KZP8eg5woEFBnIpBxDcXclrnaFV` | Readable import report: 18 Japanese 新装版 EPUBs, original bytes preserved, purchase origin user-reported, receipts not inspected |
| calibre_import_manifest.json | `1u_0nmaFcgdTZ2djkL9yXA877Y1-9nzUe` | Complete 53,571-byte manifest fetched/decoded; SHA-256 `30d7a625678abbe18d02956570b995046e9d9eb0afdf35c51f0d302f79a8cbe8`; 18 source/destination records, OPF metadata, local hashes and packaging reports |
| drive_propagation_manifest.json | `1p9JT14wyycPW2ZZBg7cqMg1ST0LAmwRt` | Complete 50,709-byte manifest fetched/decoded; SHA-256 `b13bd21be8b6146e352da731302ceda2790f6ee867fdf24675e51a25f418d872`; maps source hashes to Drive objects, but its verification explicitly covers metadata readback rather than remote checksum equivalence |

The import audit began 2026-09-28T01:14:23.368829+00:00 and reports completion at 01:16:50.007948+00:00. Propagation reports completion 2026-09-28 02:01:40 UTC. It reports 18 media additions, no reused media and two provenance-document uploads. These are attributed historical receipts. Absolute acquisition paths, library/database details and original private manifests are not copied into Git.

All 18 import records report language `ja`, creator 上田美和, publisher 講談社, package `item/standard.opf`, passing ZIP/container/resource checks, no packaging warnings and no encryption descriptor. Only V01's complete source bytes were independently downloaded and checked in this bootstrap. V02–V18 packaging/integrity statements remain historical manifest reports. Requested checksum/version fields were not exposed in the connector's normalized metadata response; this does not prove that Google stores no such fields.

## Exact candidate witnesses

Source keys are `PG-JP-NE-VNN-W01`; this is an edition-specific inventory identity, not an admission. Common filename grammar: `Peach Girl - Volume NN - New Edition [Japanese].epub`; common MIME `application/epub+zip`. Total observed sizes sum to 1,646,685,778 bytes. The checksum column is the import manifest's local-source/destination SHA-256, independently confirmed against downloaded Drive bytes **only for V01**. Spine-image counts for other volumes are reported counts, not inspected page counts.

| Source key | Drive object ID | Bytes | Manifest SHA-256 | Reported spine images | Current verification |
| --- | --- | ---: | --- | ---: | --- |
| PG-JP-NE-V01-W01 | `1oEdegOleO9oHdqVViFJQ6Vk_5wW0kvRk` | 98471638 | `25fff75c79fa8475afe35b817418ea76c27092f80343a83729a3ef65819d78ea` | 187 | BYTES_AND_PACKAGE_VERIFIED |
| PG-JP-NE-V02-W01 | `1-3q4yqfW-qI-9ovcdlyNaYUcEu-SyBFx` | 101616697 | `c79174f8791e8bbc41cde944344d258369ac4bc7f23d39972a2dccf2b40e73f0` | 175 | BYTES_AND_PACKAGE_VERIFIED |
| PG-JP-NE-V03-W01 | `1ij9gbkFoklZTB4_ZAu3zr7etZIWOeH2d` | 99813938 | `9086a57ecdd13f9d601fc7558787f14f7c13356d52de716c15962f5536838cdf` | 183 | BYTES_AND_PACKAGE_VERIFIED |
| PG-JP-NE-V04-W01 | `1AgAnqAR7Va8GqfU5bVtexSaUh-r6zUsn` | 86369890 | `84899238f7fbc0858ccabad7a5bdddfbdfba860ab75b143d268aa39c4a1bba43` | 179 | BYTES_AND_PACKAGE_VERIFIED |
| PG-JP-NE-V05-W01 | `16SZN77M12VyU2SyomngwkLnZAylL71s7` | 88975596 | `66205a1bfc3903f356fa0df36cdfb2707106fc7e7e423fee81d45b17555f12ad` | 181 | BYTES_AND_PACKAGE_VERIFIED |
| PG-JP-NE-V06-W01 | `1dWf0AjMEdgcHqzEdSMXPdCAk2YcPqTiC` | 88959368 | `b7a84c4ac1445af67666f552cb30f49c7b362e21abda404dc51a8fa577a154eb` | 175 | BYTES_AND_PACKAGE_VERIFIED |
| PG-JP-NE-V07-W01 | `1ycdZzPU3RUlOxTKNXWbzfsPIMjxxMLqH` | 94777974 | `afe975190a1d5a7a8b606de1cb83ad4d10206bb7acdea2fe4412f34e021c7724` | 183 | BYTES_AND_PACKAGE_VERIFIED |
| PG-JP-NE-V08-W01 | `12Jl-GFVzm-yYMPToFzJWzJKFWTw8C_gj` | 80842608 | `20103e40f320257760a0d3014e02f2e2162ca44e0e081bf2e006ebde452ccf5e` | 177 | BYTES_AND_PACKAGE_VERIFIED |
| PG-JP-NE-V09-W01 | `1Iybn-Z9lvQbjyegripSC3vPg7xhVCFq5` | 84679968 | `6131b243dc9b586567b2b899aad0cfdc2c70724e3e21c8e4d2cc614bb7fbae7e` | 175 | BYTES_AND_PACKAGE_VERIFIED |
| PG-JP-NE-V10-W01 | `1-4WKChuDhom5dm8sVOSUGx49H9CAiUQC` | 87791228 | `ef55cdbd83dd604b833ff7c8f26e6d778609f022f9ab6dd7d48125a7b3ee4d88` | 179 | BYTES_AND_PACKAGE_VERIFIED |
| PG-JP-NE-V11-W01 | `1CeTLy9KX3wiB-ZfmSHjCYTZRepyFbdC1` | 86855316 | `95f066f1958c95c41a4aff74ca504760111ec363ec59c6d2c9f4480bb2b86d8c` | 175 | BYTES_AND_PACKAGE_VERIFIED |
| PG-JP-NE-V12-W01 | `1dUdyqIwbcY5WmJF_I8q5EXDvICcelpC-` | 98616828 | `0309a8bc68b0db42555a00444d3140e2b9c133483e8a367d33ef6b5b30506238` | 177 | BYTES_AND_PACKAGE_VERIFIED |
| PG-JP-NE-V13-W01 | `1be4xH4q5qiC_ZMuDZyl18ah-exZU_fLj` | 84591252 | `78878d47d8d0e4d900ab35825cfa8a843fdc6e34187c99e8bbfc4e9bc55405e9` | 171 | BYTES_AND_PACKAGE_VERIFIED |
| PG-JP-NE-V14-W01 | `1xFJti84nqmuCtuNys-JFWHPrs_Ne5ZFy` | 91533584 | `36952289f8ea23fb71ec0ce777e057057ada4835baab14294f28ca9603259c16` | 175 | BYTES_AND_PACKAGE_VERIFIED |
| PG-JP-NE-V15-W01 | `1B0sO1qGJyWMRePYraosMGHBQqXotm_-p` | 93922336 | `24b4f17f77fad3e125786cdbde460bc37f72c085dd5d2b1d6c4ea6a44fab4714` | 175 | BYTES_AND_PACKAGE_VERIFIED |
| PG-JP-NE-V16-W01 | `1dnLe89Lk3GE745l5szeviRlOitE28y4l` | 85468879 | `0160eb9af93379a42e1fe7da7c2419c7358163ccb683cbe5a09fed598383ee3d` | 171 | BYTES_AND_PACKAGE_VERIFIED |
| PG-JP-NE-V17-W01 | `1qtNqAKN9Q6b7i56R1O_qA4Tj6GpliMMn` | 94041107 | `5213feb9f62724cfe80cc8139aa407e6a4c0349a1b163cebc96d42aa09a36bc1` | 173 | BYTES_AND_PACKAGE_VERIFIED |
| PG-JP-NE-V18-W01 | `1j_jgkUFoTOVEc3-nL-84ipGDkXlDDN9F` | 99357571 | `00222d219ee6b844207ac825a194397057c51ba51b2471d762e8c87f8b0af720` | 187 | BYTES_AND_PACKAGE_VERIFIED |

Every witness has `narrative_admission: NOT_ADMITTED`, `narrative_inspection: NOT_STARTED`, `sequential_completion: NOT_STARTED`. There are no missing numbered volumes in the observed V01–V18 metadata set. That is not a claim that every chapter/page/component is intact, legible, correctly identified or already available to a future execution. No PDF, CBZ, separate booklet, sequel or adaptation file was observed in this folder. Embedded supplements remain unverified, not absent.

## V01 non-narrative structural probe

Downloaded V01 has 98,471,638 bytes and SHA-256 `25fff75c79fa8475afe35b817418ea76c27092f80343a83729a3ef65819d78ea`, matching the manifest. ZIP CRC verification found no bad member. There are 382 ZIP entries; the OPF declares 187 image resources and 187 spine wrappers, each referencing one unique image, with no missing referenced image. The package declares right-to-left progression, pre-paginated layout and landscape spreads. OPF title is ピーチガール　新装版（１）, language ja, creator 上田美和, publisher 講談社, UUID `urn:uuid:5186c967-f87f-47dc-950f-2b8817b32bee`; the date field is empty.

The first wrapper is `item/xhtml/p-cover.xhtml`, the last `item/xhtml/p-185.xhtml`. Navigation has three anchor references: twice to `xhtml/p-cover.xhtml`, once to `xhtml/p-000.xhtml`. These do not supply a verified chapter segmentation. Wrapper inspection found no nonempty p/span text nodes; narrative readability therefore requires actual image inspection, not extraction of a prose EPUB. Images were not rendered, visually examined or OCR'd. CRC/decompression and resource linkage do not establish image legibility or story completeness.

Publisher pagination, chapter counts/labels/boundaries, mainline versus extras, and any source/publisher page crosswalk are **UNVERIFIED**. V01's package-level result cannot be generalized to V02–V18. A full source-side deterministic locator map has not been admitted or durably released by this bootstrap; it must be generated, verified and retained in the evidence plane for the authorized reading stage.

## Retrieval, admission and open requirements

1. Resolve the source key to the stable Drive ID above; read current metadata/parent and retrieve the complete stored EPUB using authenticated Drive raw-file fetch, streamed without inline base64. Materialize the returned authenticated file reference in the permitted working environment. Do not publish signed transfer URLs.
2. Verify exact bytes/length/SHA-256 against this map. On mismatch, hold the source, compare current provenance and allocate a new witness only after resolution. Preserve prior identities/checksums.
3. Check ZIP CRC, container/OPF metadata, spine and every referenced resource. Enumerate spine occurrences from OPF order, resolving each wrapper's image path relative to its member. Do not sort image filenames to invent page order. Record extraction implementation/version, parameters and source/derivative digests; keep the full deterministic map and any derivative images in Drive.
4. Before narrative work, obtain owner approval of foundation and explicit unit scope. Within that authorization, verify legibility, chapter/page/component boundaries and any publisher pagination. Define included mainline and separately bounded paratext/bonus objects; uncertain supplements remain quarantined. This is the first point at which narrative pages may be inspected, not a permission supplied by this checklist itself.
5. Advance independently recorded states only on evidence: `INVENTORY_VISIBLE → BYTES_VERIFIED → PACKAGE_VERIFIED → ADMITTED → INSPECTED → CLOSED`. Legibility/component limitations can prevent admission despite package verification. A partial reading never becomes CLOSED.

Required before the first narrative transaction: approve the proposed original-mainline/新装版 boundary and locator convention; verify the active source/derivative route survives the session; resolve V01 component/legibility requirements under explicit admission. Required per later volume: independently verify bytes and structure, then component coverage. No inaccessible or corrupted object was established; V02–V18 raw transport and integrity have simply not been tested. No narrative component is ready merely because metadata matches.

Related manga, adaptations, novelizations, creator/editorial supplements and reception need separate provenance, continuity, spoiler/disclosure placement and owner admission. Prefer assessing later supplements after the original-mainline freeze unless a bounded earlier admission is explicitly approved. Do not backdate their information. No acquisition of missing franchise material or Drive reorganization is authorized by this map.

## Full witness acquisition and package verification (execution run, 2026-10-16)

Under the owner's execution authorization (see the [initiation record](../07%20Audits%20and%20Handoffs/PEACH_GIRL_EXECUTION_AUTHORIZATION_AND_INITIATION_RECORD.md)), all 18 EPUBs were retrieved read-only from their Drive objects above. The connector's 10 MB download ceiling was bypassed through owner-enabled temporary link-sharing over HTTPS; no Drive object was modified. Results, per witness: byte length and SHA-256 equal the table above; ZIP CRC check clean; OPF title `ピーチガール　新装版（N）` with matching N, creator 上田美和, publisher 講談社, language ja; `rtl`, `pre-paginated`, `landscape` spreads; spine counts equal the reported counts; each spine wrapper references exactly one present image. The verification column is updated to `BYTES_AND_PACKAGE_VERIFIED` on that basis. The two provenance manifests' SHA-256 values match those recorded above; `CALIBRE_IMPORT.md` (3,240 bytes) has SHA-256 `eff1f1317365f18bd72a8e416716171a6f74a88e1290939d664a1b048fcc42f0`.

Every package's navigation holds only 表紙 (twice, → `p-cover`) and 本編 (→ `p-000`), so navigation supplies no chapter segmentation. Wrapper names `p-NNN` are packaging identifiers, not verified printed pages. `iNNNN` counts spine occurrences from `p-cover` = `i0001`. Chapter labels/boundaries, printed pagination and components are established by inspection at each volume's admission and recorded in its reading's source receipt.

Deterministic locator maps (`PG-JP-NE-VNN-W01.locmap.json`, generator `locmap.py` v1) record occurrence, wrapper, `idref`, viewBox and image member with byte length and SHA-256 for every occurrence. They are **locally staged, pending authorized promotion to the Drive evidence plane**; this run is prohibited from Drive writes and does not claim publication. Map checksums are recorded in the run's source manifest. Admission states per witness advance only through each volume's sequential transaction: `BYTES_VERIFIED → PACKAGE_VERIFIED` is now true for all 18. `ADMITTED → INSPECTED → CLOSED` is recorded in each reading and in the entrypoint's high-water mark, not by editing this table at each unit.

Revision history: 0.1 — metadata/provenance reconciliation plus V01 byte/container probe; zero narrative inspection, 2026-10-16 UTC. 0.2 — all 18 witnesses byte/package-verified; locator maps staged locally; zero narrative inspection, 2026-10-16 UTC.
