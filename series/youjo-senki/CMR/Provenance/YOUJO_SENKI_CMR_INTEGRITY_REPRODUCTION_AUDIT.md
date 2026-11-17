---
series: YOUJO_SENKI
artifact_id: YOUJO_SENKI_CMR_INTEGRITY_REPRODUCTION_AUDIT
artifact_type: source_integrity_reproduction_audit
scope: Japanese LN V01-V14 source routing and frozen CMR0/CMR2A/CMR2B-V12 preservation
source_boundary: Original Japanese light novels Volumes 01-14
status: active_provisional
version: '1.0'
observation_date: '2026-10-11'
repository_base_commit: 238fed779661f6a5a49d6a70034a6183d17ca175
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
---

# CMR source integrity and reproducibility audit

The current run verified all fourteen local user-supplied Japanese EPUB byte streams against the locked source audit, then reproduced the exact historical locator, member, candidate, and V12 cumulative adjudication hashes. No algorithmic change was needed. This establishes recoverable routing and preservation; it does not establish that every extracted paragraph was newly interpreted.

## Source identity and Drive navigation

The Drive metadata reads independently confirmed all fourteen original IDs, canonical filenames, byte sizes, EPUB MIME types and the parent source folder `1s8Ido1uUbAyR-lXstTyOVfoeHaUDop-g`. The connector does not expose byte-checksum or version fields in its normalized metadata response. The hashes below were measured from the authorized local files and matched the pre-existing lock; they are not claimed as new Drive-body downloads. The audited extractor binds these exact hashes to the same Drive IDs.

| Source | Drive object | Local bytes | Locked and measured SHA-256 | OPF member |
|---|---|---:|---|---|
| V01 | `1U8EVl8O36c0UNufRZ8FyECQn1OdX66O3` | 4,336,476 | `98176f853bca4a5dd8a565d50230e343153af889e9425a8815f5870b4a9afcf4` | `content.opf` |
| V02 | `1FDlbddgXsbMIM3owNB1gl-Sevri9qkkm` | 18,107,855 | `f174d85394d72b0e59945a7a2d99d4a1f632b2b6ad5a3de8b64feedcf84f5f49` | `item/standard.opf` |
| V03 | `1rf02o6MhrDg3ZZ5MRAcFl351P9RJVIOy` | 4,415,642 | `87c9063dbd3fc05b1af37a331224018ae5eef63f7ed50a31463dcf6659fa54fa` | `content.opf` |
| V04 | `1drbI91vxz7KlHmg18bRQcHqZi0TERZFr` | 16,201,497 | `37c31851cbdd82ebfe7f40c92171d9f965f8d7917f276332ba893a90fc96fa69` | `OEBPS/content.opf` |
| V05 | `1gr_NDKTkXiuuJxin59jav-EpzL9nC_tU` | 19,322,381 | `aef0af576f06dd2256073d98a3281db69392d51626a2cfc4fb28c033141152e8` | `OEBPS/content.opf` |
| V06 | `1kDkWgFZxp-FFXNPRaKGUpBSLsw3bs1U4` | 17,194,950 | `3b80de07d285619e5bc62f08a5b0386d025485d9fc4a6d6180f3e2f61483895d` | `OEBPS/content.opf` |
| V07 | `1Vod5TbjC9RhC8LUrLnYx8kNDmUfl05gx` | 16,373,031 | `3d74490e62679c03cc900e381808c8a5cfaa25d6a9aa553009e740e411257647` | `OEBPS/content.opf` |
| V08 | `1yQtGtiZhfEJiQwUQaDXt6jJdmYwe8Eqb` | 14,295,126 | `0b01d060abb752af7b83c6aa07d2cb3df71c1b93a6c1b043e4bec8094dd6282d` | `OEBPS/content.opf` |
| V09 | `1pCgiYrXBISzrIuHVMTuxZTZZ9WQ8i0PZ` | 1,762,494 | `e5c38fbdd2f741ce2ee306a07bf0358784ff15d274205b54482d4f588ae32219` | `content.opf` |
| V10 | `1tym5uP66m2NI9CY-Rw5luqx1CVBCl1MN` | 20,774,463 | `a036aa62a572c81d7e7b236a2178fc946d3c7fd10617fdd656a87e2b0b297857` | `OEBPS/content.opf` |
| V11 | `1zQw9hDWovkBGhA3KzGcBPC1jdGcolEyQ` | 24,762,051 | `f4ad2bd15896349f3e3097d132da4e6b4f03101b8c18365a86e91936097caf14` | `OEBPS/content.opf` |
| V12 | `1pDDFx2jWBxJ0rCzYXQnPEy4TBnyZaeVK` | 21,178,558 | `d2df10ca83887a0735e20d364eeded7e5bc5518d69a439b4081361dfef9436bf` | `OEBPS/content.opf` |
| V13 | `1-kQGGtMKjv5GODAY2Xdbx-7PxGJ7lEm4` | 22,572,251 | `bca62b18659738926b0865433ad099cbb628281b846406dd32dda3f82858ef97` | `item/standard.opf` |
| V14 | `1YHzsVf_qrg9_rqm2QjqTsUyzhKC0Navc` | 24,047,512 | `e6e9264aaec3cfed0b211a3142e77905be651eb33c7a1f0649887878d21aa046` | `item/standard.opf` |

Every archive passed its full ZIP CRC check and contained the expected OPF route. V02 retains the known mimetype-entry order/compression irregularity; its locked bytes and readable package are unchanged. Source illustrations, chapter-title images and image-only bonus pages are separate members. A zero text-block count does not mean those members contain no content.

The primary-source audit remains Drive `1JXarPgypYVSdzAexUyyOa4qH8mxlyHcx`. Safe source filenames are `Youjo Senki - Volume NN.epub`. Private acquisition filenames and source-delivery paths are excluded from this analytical record.

## Exact reproduced objects

| Object | Bytes | Logical rows | SHA-256 | Verification basis |
|---|---:|---:|---|---|
| Full locator index, Drive `140ow12czVj4J8Q_JR44MSWI98LUxj3uk` | 52,894,654 | 63,812 | `c84fa4c8e0251730887b51913a8f32ea68c39be68ff4adae8d995d49292f5cfe` | New deterministic output equals the frozen manifest hash; current Drive body was not downloaded |
| Member index, Drive `1GlDNvT5spgIQk5VaUU5S2Qsk5dF174hR` | 203,927 | 608 | `e05b9fe26ec35e4590b9e148005b49f7ed142ec2f6ca2868e99561981372e220` | New output equals exact recovered current original bytes |
| Tanya candidate pool, Drive `1LRcSX-k739E4O4xQ2ImZnawzx6IylARo` | 2,290,984 | 1,200 | `8344b6196565645cfe373d3468fa4f3c618d1c4d3afb363667c64a073a5c469a` | New output equals exact recovered current original bytes |
| Frozen V01-V12 ledger, Drive `1Eoz8hpJMoeksACmQgvJXntTEcYM-w20g` | 648,524 | 1,045 | `4391f1042668cdc2148f6e09b975317cb5ab9d20c9e0e1679d491c450a8e6fa0` | Exact recovered original equals the original audited V12 append build |
| Frozen V01-V12 diagnostic index, Drive `1i1Ov7u5yGciH55j-04LxIR4CWck61-KH` | 1,043,995 | 676 | `1240953f6174375e64ddf1eb44af83954984a438c4b2fbc5d8869dabcf42ce68` | Exact recovered original equals the original audited V12 append build |

The locator output contains 222 text-bearing members, 2,974,249 normalized Japanese characters and 8,997 ruby-bearing blocks. All 608 member routes were traversed with zero member extraction errors. Text-mode categories remain retrieval heuristics, not speaker attribution.

The candidate pool retains its original priorities: 388 HIGH, 762 MEDIUM and 50 LOW. These are review priorities, not confidence. Its exact volume counts remain V01 110, V02 110, V03 88, V04 110, V05 88, V06 62, V07 78, V08 76, V09 108, V10 94, V11 60, V12 61, V13 92 and V14 63. The final 155 centers still require source-contextual adjudication at this intake boundary.

## Script identity and runtime transformation

| Original source implementation | Drive ID | Original SHA-256 |
|---|---|---|
| CMR0 extractor | `1l8ok-FT2RMmDl-qeXJnVaj8hrS7pzKeu` | `e21635d9f19d5925e2ad3f40aaaf2ac8cfff4d0f1dee8082c49415be09f04adc` |
| Tanya CMR2A retrieval | `1GZMXU-ulPFfKFKGrjl6GjXUYtqnorwg5` | `95e52f0e50f42c16eec4bb421245d7f150959478451559e6e47614052c87a074` |
| Cumulative CMR2B V12 build | `1whdImFw-vUblagWfpiqEmY58hT1vd3LZ` | `23078662fed83e7aa8ba7c5e59fe9e0946a58ab75abab61a7de0a326e5e6909f` |

Each original script was obtained as exact authenticated bytes and hash-verified before execution. The working copies substitute only named source/output filesystem locations: two constants in CMR0, four file locations in CMR2A and three input/root locations in the V12 build. They preserve every extraction, selection, adjudication, serialization and guard rule. The working copies and their literal path diffs are build-plane records, not new canonical source implementations or Git deliverables.

The extractor ran with Python Unicode data 15.0.0, BeautifulSoup 4.15.0 and lxml 6.1.1. Its exact output equality supplies stronger evidence than an assumption of parser compatibility. The V12 build used its existing standard-library implementation. A separate unchanged validation environment provides the repository's hash-locked attrs/jsonschema/PyYAML/referencing/rpds dependencies; no environment was modified for this audit.

## Frozen history preservation

The V12 reproduction first reconstructed the 984-row ledger and 616-row diagnostic V01-V11 prefixes from exact frozen V12 data, using the original serialization contract. Both prefix hashes matched the audited build requirements:

- ledger prefix `2d5c280a7e2adfd8b78cd02165b642925ef693b08b22abe3334c8c26c4802bbd`;
- diagnostic prefix `193b73110644cac1602b07006a0349d0d23e1b2ab02da6f1faad6e8f4c6fc740`.

The unmodified guard logic validated every V01-V11 tranche's row counts, serialized slice hashes and diagnostic namespace. It then rebuilt V12 as 44 RETAIN, 12 MERGE and five REJECT dispositions, adding 60 diagnostics (53 HIGH and seven MODERATE). Cumulative hashes matched the direct current originals exactly. The V12-only ledger slice remained `f2d5eb87704eb4a2f8cc4a80ac1735c231ed251a3791341bf36d1e5a4c03fc8a`; its diagnostic slice remained `b0049083ee2ca1a39f79c2642a3e0fe0e6f916a35b8de457659ab87c8779e12a`.

This is a verified build reproduction, not a claim that every older Drive revision body was separately downloaded. Historical unavailable revisions remain documented in the [port audit](YOUJO_SENKI_CMR_PORT_AUDIT.md) and [intake disposition manifest](YOUJO_SENKI_CMR_DRIVE_DISPOSITION.jsonl).

Any successor must preserve all 1,045 existing ledger rows and all 676 diagnostic rows/IDs, with a separately auditable correction rather than a silent overwrite. Candidate tags, nearby names, external judgments and direct private cognition remain distinct. Semantic consolidation must add a many-to-one route while preserving every original witness.

## Analytical scope and open completion work

The newly authored Git interpretive index routes preserved judgments and explicit limits to exact source coordinates. It excludes bulk Japanese text and does not recategorize original retrieval hits as independently attributed speech. Source closure of V13-V14, ordinary-life supplements, current roster reassessment, model construction, directional relationships and QA are separate responsibilities. Source processing success cannot certify them.

Mature V2 files remain unchanged. The current entrypoint and restored Document 12 control the Japanese-primary V14 boundary; the historical Document 11 wording about an English V14 counterpart is retained as a frozen provenance discrepancy. The earlier V09 AZW3 witness described in V2 is distinct from the current hash-locked EPUB and is not silently equated with this extraction.
