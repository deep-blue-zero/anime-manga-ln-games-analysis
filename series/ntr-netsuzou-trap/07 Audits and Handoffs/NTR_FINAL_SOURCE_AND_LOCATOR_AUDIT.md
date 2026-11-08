---
title: "NTR — Final source and locator audit"
artifact_id: NTR_FINAL_SOURCE_AND_LOCATOR_AUDIT
artifact_type: source_locator_audit
series: "NTR: Netsuzou Trap / 捏造トラップ-NTR-"
generation: NTR_MAINLINE_V1
status: canonical
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
do_not_use_as_literary_evidence: true
created: "2026-10-01"
source_boundary: "Six exact Japanese numbered EPUBs; V06 CLOSED at 50f7e15b331d39e4df16f9b8d62b358933bffe83; no new source admission"
audited_corpus_commit: 50f7e15b331d39e4df16f9b8d62b358933bffe83
audited_corpus_tree: 2e7a984085418fbbbefec63587f4abc0d12295f9
canonical_home: series/ntr-netsuzou-trap/07 Audits and Handoffs/NTR_FINAL_SOURCE_AND_LOCATOR_AUDIT.md
---

# Final source and locator audit

The six local witnesses pass final mechanical identity and mapping reconciliation: **169 / 172 / 172 / 156 / 170 / 170 images, totaling 1,009**. The committed source map and all six reading routes identify these same witnesses and account for every spine ordinal. The corpus boundary is the individually CLOSED V06 commit `50f7e15b331d39e4df16f9b8d62b358933bffe83`, exact tree `2e7a984085418fbbbefec63587f4abc0d12295f9`. Earlier individual closures remain separately recoverable.

Three evidential levels remain distinct. **Mechanical verification** establishes byte identity, package order, and complete deterministic image mapping. **Recorded visual inspection** is the coordinator's page-reading activity, supported by committed coverage statements and retained working notes. **This audit** rechecks mechanical evidence and reconciles those statements; it performs no new narrative image inspection, OCR, independent whole-volume rereading, or new source discovery. It does not turn a machine count or a reading claim into independent proof of human attention. The coordinator attests personal inspection of all 1,009 images; the retained V01 working log has a narrower explicit coverage record, documented below.

## Exact admitted witnesses

The following exact filenames, Drive IDs, sizes, and local SHA-256 values agree across the source map, structural manifests, six canonical readings, and existing exact-object Drive receipts. The audit freshly recomputed local EPUB SHA-256 and MD5; it did not download new Drive bytes.

| Witness | Exact filename | Drive ID | Bytes | Spine/images | Fresh local SHA-256 |
| --- | --- | --- | ---: | ---: | --- |
| NTR-JP-V01 | NTR - Netsuzou Trap - Volume 01 [Japanese].epub | `1WBRS77YFOB0nj50iHu52ECDSCr89Lehc` | 103293058 | 169 | `36ea62dce3616941f99e7940132e864211fddf19aaab3fb542d7e1a5e7215d6b` |
| NTR-JP-V02 | NTR - Netsuzou Trap - Volume 02 [Japanese].epub | `1SFuOQ-2kPuCxefAQuQ4MdFZd5f_xqTXP` | 95932106 | 172 | `f92e5d52b348bae47c076a89033115ff3538ee014faf3e74e761d747b45da53c` |
| NTR-JP-V03 | NTR - Netsuzou Trap - Volume 03 [Japanese].epub | `1hjQf5tiP1_mlUq6yKrP-kbHYp4O9Rxzk` | 92250289 | 172 | `055e488d18090f913aee15d4af3ce581b88e990d0a333569e5977853a8a98f54` |
| NTR-JP-V04 | NTR - Netsuzou Trap - Volume 04 [Japanese].epub | `1S--_1t7PKpYLj7fSqVWVW6n6MacPIIMx` | 89972933 | 156 | `a0edcbb63e15d8c748ebf7fe115a35347eb2855790741e08dfd30c48442fcecf` |
| NTR-JP-V05 | NTR - Netsuzou Trap - Volume 05 [Japanese].epub | `1lv5br_YThe3RJGdR-f7XpPa_ibM97hri` | 92588880 | 170 | `ed7202d2f64b41b9df4fb632aed41368495e070fba3e5ce291dfb0e3d3ee7044` |
| NTR-JP-V06 | NTR - Netsuzou Trap - Volume 06 [Japanese].epub | `1GJLLrbhJy-9XcRviQgIg74TlVf-lLCPZ` | 98707220 | 170 | `613bb037decaddea3b77b71e8674ec746fe34cd5cfb8bd8ce9a7a302f5d0cee1` |

All six OPFs declare EPUB 3.0, Japanese `ja`, RTL progression, creator **コダマナオコ**, and publisher **一迅社**. Package modified timestamps are metadata, not independently verified publication or purchase dates. Identifiers are retained verbatim, including V01's legacy string; the audit does not normalize it into a different identity.

| Witness | OPF title | OPF modified UTC | Package unique identifier |
| --- | --- | --- | --- |
| V01 | 捏造トラップ-NTR-（１） | 2015-06-12T00:00:00Z | `urn:uuid:cpsj272z-x372-e76b-dzyo-3jllv3npv8zu` |
| V02 | 捏造トラップ-NTR-（２） | 2016-03-14T00:00:00Z | `urn:uuid:563336cf-d316-4971-8035-a94c773955f0` |
| V03 | 捏造トラップ-NTR-（３） | 2016-11-15T00:00:00Z | `urn:uuid:ddb86f93-a55a-41bb-90a3-d45dce2e0c47` |
| V04 | 捏造トラップ-NTR-（４） | 2017-04-12T00:00:00Z | `urn:uuid:93a75762-5f5c-463f-9736-f867b252b71a` |
| V05 | 捏造トラップ-NTR-（５） | 2017-07-12T00:00:00Z | `urn:uuid:f583f59a-7383-4c41-ae5e-2be192d94beb` |
| V06 | 捏造トラップ-NTR-（６） | 2018-01-15T00:00:00Z | `urn:uuid:93e4315e-a01d-43ee-96b7-d71c133f7008` |

The source map still leaves edition variants, independently established purchase provenance, and completeness against every possible publication form outside this six-file identification. This audit verifies the bounded admitted corpus, not an exhaustive bibliography of the franchise.

## Deterministic locator and mechanical completeness

Every source coordinate is `NTR-JP-VNN/SNNNN/I01`: `S` is the one-based OPF spine ordinal; `I` is the one-based image occurrence inside that document. All 1,009 spine documents contain exactly one image. The separate `sequence_image_index` is one-based **within its volume**, not a series-wide page number. Chapter, panel, balloon, and visible printed-number descriptions may supplement a citation without renumbering these structural coordinates. An OPF ordinal is not universal printed pagination.

The final recheck reread the actual EPUB container and OPF, resolved every manifest target, followed every actual spine `idref`, and resolved the image reference in each corresponding XHTML document. It reconciled those results against each structural manifest, ordered JSONL, and the consolidated CSV. Every coordinate and occurrence index is contiguous and unique. Every source image member and every extracted original was freshly SHA-256 checked; all 1,009 matches pass. All six fresh ZIP CRC tests pass. No missing target, non-spine image, unmanifested image member, or duplicate image byte hash within/across these witnesses was found. Byte uniqueness does not make a repeated narrative event an independent event.

The recorded 1441×2048 image-header dimensions remain bound by the freshly verified unchanged image bytes. This final audit did not decode or view the images. Current sheet manifests cover all locators in the same order: V01/V02/V03/V05/V06 each have 29 sheets; V04 has 26. Sheet-coordinate completeness establishes that no page was omitted from those prepared reading aids, not that a person looked at every cell. The sheet tiles are read left to right and top to bottom by sequence label; the Japanese panels inside each page retain their original RTL order. Original images remain the wording/composition verification source.

Numerical coverage of each reading's first routing table also passes: the union of its explicit route intervals and included separator intervals is exactly the corresponding S0001–final-spine range. Covers, blanks, dividers, illustrations, afterwords, advertising, body-cover gags, and colophons therefore stay inside the 1,009-image coverage denominator. V03 S0113–0116 remain narrative; V06 S0155 is a narrative pause rather than a dropped blank. Designed title positions and printed contents anchors remain interpreted routing facts rather than substitutes for the OPF coordinate.

## Embedded material and chronology

These chronology findings reconcile the source map with the canonical readings' routing and embedded-material sections. They are the coordinator's visually grounded classifications, **not an independent fresh visual verification by this auditor**.

| Witness / interval | Admitted route | Boundary retained |
| --- | --- | --- |
| V01 S0155–0162 | **旅行前日**, before the winter trip; the reading records the explicit return to printed page 75 at S0162 | Embedded earlier time, not a postendpoint continuation. Afterword S0164–0165 is production paratext. |
| V02 S0161–0166 | **NTR★P / 捏造トラップ・パラレル — 人妻たちの昼下がり**, expressly adult married parallel continuity | Source-inspected but not a mainline flashforward, marriage forecast, or mainline reconstruction-validation witness. |
| V03 S0159–0164 | **少女リプレイス**, expressly middle-school third-year backstory | Newly admitted earlier-time knowledge at V03, not a postV02 prospective outcome. |
| V04 S0148–0149 | **NTR★S / 捏造トラップ・summer**, compatible earlier beach preparation/outing comedy | Routed as earlier comic material, not a postV04 continuation or retrospective forecast rescue. |
| V05 S0159–0162 | **NTR★C / 捏造トラップcooking**, compatible earlier/undated domestic comedy | No dated postcirculation response; not prospective validation or proof that mundane competence repairs harm. |
| V06 S0166–0167 | **EXTRA PAGES / embedded body-cover gags**, after H's return to school; absence apology/admonition followed by separate study/food/care play | A bounded later school state inside V06, not graduation, completed cohabitation, V07, or standalone-supplement validation. The mainline fin remains S0162. |

Anticipatory color openings, chapter-boundary repetitions, recollections, and the V06 childhood/father/F–H history are separately routed by the readings. Later admission of earlier narrated time does not supply earlier reader knowledge or backdated forecast success. Afterwords, promotional blurbs, and production anime mentions were inspected as paratext; they do not admit adaptation narrative or override the source-limited interpretation.

## Visual coverage claims and retained-note limits

All six committed readings explicitly claim complete visual source coverage; V06 records the coordinator's personal all-corpus total. V02–V06 working notes contain interval/completion statements reaching their final spine and preserve entering boundaries, corrections, and original-page verification claims. These are reading receipts and attestation, distinct from the final hash/mapping proof.

The retained `V01-inspection-notes.md` is **29 lines and explicitly ends at S0102**, including the statement that the mainline is through 102 only at that append. It supplies no explicit working-log inspection entry for S0103–S0169. The committed V01 reading nevertheless attests visual inspection of S0001–S0169, and the coordinator now attests all 169. This audit records both facts: the working log does not independently corroborate the remaining 67 V01 images, but its narrower historical append does not prove those images were never later read. Do not recast this partial note as a contiguous contemporaneous 169-image log, fabricate missing notes, or treat mechanical availability as the missing visual receipt. The final 1,009 inspection statement rests on committed reading claims and coordinator attestation, with this explicit receipt limit.

| Witness | Individually CLOSED commit | Coverage statement |
| --- | --- | --- |
| V01 | `1599e107254657520c75e26e2933f4943df2b6ed` | Canonical reading and coordinator: 169/169; retained working log explicitly through 102 only |
| V02 | `69a3182de99b8afca1ec93a9fa89ace73472aaf3` | 172/172; retained intervals/completion reach S0172 |
| V03 | `c3fa81fe09c914e00ae82ac8b9123ec180aa5f97` | 172/172; retained intervals/completion reach S0172 |
| V04 | `e69f32f8b40808e0cb40c1205b1d7018d7eb74ae` | 156/156; retained intervals/completion reach S0156 |
| V05 | `2226f20120d0de9134e105ff5c8c15de2c6971bc` | 170/170; retained completion reaches S0170 |
| V06 | `50f7e15b331d39e4df16f9b8d62b358933bffe83` | 170/170 personally inspected; retained sequential range headers reach S0170 |

The original source-preparation manifest's inspection-state and pending-semantic fields describe its **historical mechanical checkpoint**. They were not overwritten with narrative claims after the coordinator read the corpus. Likewise its README's no-image-view statement describes that original preparation operation; later separately authorized bounded helper checks do not become whole-volume independent rereadings. Current admission/inspection/closure state belongs to the committed source map and readings.

## Drive and quarantine limitations

The existing metadata receipts match all six exact IDs, titles, byte sizes, EPUB MIME types, and evidence-folder parent `1jJBFGXROchjVNUeuy4oXRi3PDHCTCF4H`. Existing raw-object fetch receipts report success with `download_raw_file=true`, `include_base64=false`, no inline base64, and no returned `workspace_path`. Requested MD5/SHA-1/SHA-256 fields were not exposed by normalized metadata. Each local materialization attempt returned HTTP 403 and produced no local current-Drive bytes.

Therefore **current remote Drive SHA-256/MD5 and equality to the inspected local witness remain independently unverified**. Successful metadata/raw-reference retrieval is not downloaded-byte hashing. Omitted checksum fields do not prove Google Drive has no checksum. This audit reread and reconciled those retained receipts; it made no new Drive request, authentication workaround, upload, or source substitution. Local-source hashes must retain their local label in publication and handoff.

The LateWinter item is now metadata-located, rather than merely the original bootstrap discovery lead, but remains uninspected and quarantined: `NTR - Netsuzou Trap - LateWinter [Japanese].epub`, Drive `1OEGPdDprGkU7WVnItseHkTjkMtlTIz7X`, 13,260,813 bytes. Its existing receipt distinguishes current inventory metadata from a historical importer hash/routing label; that hash was not freshly verified here and the `after_story` import label is not narrative chronology evidence. No supplement, anime, localization, interview, standalone side story, or other external narrative enters this six-volume boundary.

## Git separation and durable handoff

The NTR series slice in the bound corpus tree contains **28 UTF-8 text blobs: 27 Markdown files and one series-registration JSON**. It contains no raw media, extracted originals, reading sheets, mechanical CSV/JSONL locator payload, or OCR dump file. The blobs also contain no binary NUL or embedded image/base64 payload detected by the audit. This claim is scoped to the bound NTR tree, not unrelated series or the entire Git object database. The source-preparation plane and working receipts remain outside the checkout. Interpreted citations and source/receipt identities remain recoverable from exact EPUB bytes and OPF order.

The fresh final mechanical receipt is `work/NTR-final-source-audit-mechanical-receipt.json`, created `2026-10-01T09:43:27.689735+00:00`, SHA-256 **`b496c99db687d054395810b1a2a3333fb60c961677dc6257ac1250a96c6ecd2c`**. It records fresh per-volume local MD5, structural/ordered/sheet manifest digests, canonical reading digests, retained inspection-note digests and range headers, all checks, close commits, and the same limitations. The mechanical producer stage changed no source media, canonical file, Git index/ref/commit or Drive content; it wrote only noncanonical audit outputs. This canonical promotion preserves that historical operation and its fixed corpus scope.

| Evidence receipt | SHA-256 |
| --- | --- |
| Source map bytes at the bound corpus commit | `9dc6d879b75de0543b1eb02b64dd44a3d9eb65d846aee1067f194a04db732d3d` |
| source-verification-manifest.json | `eabec461951ca460131c8a8977e3705f8494f5ee2242c03ac40feff6a26c1f21` |
| locator-index.csv | `76a5d8584f3863761707d90c71f459a5f7fa7f7491e60a5ecfa152af460f8ded` |
| drive-metadata-receipt.json | `2d38eb40a631d5d9e9540e52d6184327e8c16c8d7671e8929a9e65d9b9ed82dc` |
| drive-raw-fetch-receipt.json | `5dce7e29fd49d67e39e71a19ca0c37dbaa33e3e3aa102508d3d975711861e6a3` |
| drive-byte-verification.json | `f1381082a6e63e3cf5b33be2fded1a99f23734255d56ca97228fa4bff79e3fec` |
| bibliography-and-sheet-receipt.json | `4c22816527ce6b132402140f8091ac919aca7cddf73a234eb453cd91672e9bc1` |
| quarantined-LateWinter-metadata-receipt.json | `5b9b2ab7759ea9e311d9161eb9cf1ff0000922d42c23c42282c49c9b607b1b5b` |

Handoff result: the exact six-source identity and locator responsibility passes mechanical reconciliation, and every canonical route covers its complete witness. The all-corpus visual coverage is explicitly attributed to the coordinator and committed readings, with the V01 retained-note gap preserved. Current Drive-byte hashing and any future supplemental admission remain outside the verified claims. This bounded source audit does not itself certify mature-character, longitudinal, specialist, synthesis or publication responsibilities; those have separate acceptance and verification homes.
