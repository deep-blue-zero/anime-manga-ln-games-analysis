---
title: "NTR — LateWinter source and sealed-boundary audit"
artifact_id: NTR_LATEWINTER_SOURCE_AND_FREEZE_INTEGRITY_AUDIT
artifact_type: supplemental_source_integrity_audit
series: "NTR: Netsuzou Trap / 捏造トラップ-NTR-"
generation: NTR_SUPPLEMENT_LW_V1
status: canonical
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
do_not_use_as_literary_evidence: true
created: "2026-10-01"
source_boundary: "Exact NTR-JP-LW local witness, 24/24 visual inspections; frozen V01–V06 baseline"
canonical_home: series/ntr-netsuzou-trap/07 Audits and Handoffs/NTR_LATEWINTER_SOURCE_AND_FREEZE_INTEGRITY_AUDIT.md
---

# LateWinter source and sealed-boundary audit

**PASS_BOUNDED for genuine-author, post-finale supplemental admission and complete witness inspection.** Local bytes are fingerprinted and structurally complete; equality to current Drive bytes and the original physical edition's exact distribution day remain unverified. These limitations narrow provenance, not the visually and independently verified creator/series identity.

## Exact object and acquisition limits

| Field | Verified value / limit |
|---|---|
| Source key | `NTR-JP-LW`; never V07 |
| Exact filename | `NTR - Netsuzou Trap - LateWinter [Japanese].epub` |
| Drive file | `1OEGPdDprGkU7WVnItseHkTjkMtlTIz7X` |
| Drive parent | `1jJBFGXROchjVNUeuy4oXRi3PDHCTCF4H` |
| Bytes | **13,260,813** local; fresh connected Drive metadata/raw-reference response reports the same size/name/MIME |
| Local SHA-256 | `f2d70cdffaa8d15031bdec7b097a077662e7618791db265eec4a2141345e4a2d` |
| Local MD5 | `2fa84cd1a6deb0c2406e309718d131e2` |
| Current Drive checksum | **UNVERIFIED**: requested checksum fields not exposed; supplied authenticated raw reference materialization returned HTTP 403 |
| Permitted local route | Owner supplied the local manga directory; exact execution path retained outside Git |
| Purchase/store provenance | User-supplied witness; no receipt examined and no exact source retailer inferred from UUID/name/size |

The connected Drive response's “Action completed” and a full-sized reference are not independent byte hash verification. The actual reading uses the authorized local witness. Matching metadata supports identifying the intended candidate, not asserting remote byte equality. No copy, sharing, move or Drive write was performed.

## Identity, edition and publication class

The OPF supplies **捏造TRAP-LateWinter-**, **コダマナオコ**, `ja` and UUID `1b13e91a-1c0f-4701-85a6-15e5e08eb3be`. S0001/S0003 identify **2017winter comic market93** and **monaco meister**; S0004 introduces the creator and describes a small after-story to the completed serial's final episode. S0022 repeats creator/circle contact identifiers as publication footer. S0024 credits **著者 コダマナオコ** and **販売協力 株式会社ナンバーナイン**. This internally coherent creator-made publication is distinct from a numbered Ichijinsha tankōbon or an anime extra.

Independent authorized retail metadata identifies the same title/author as a post-final-episode work. [Rakuten Kobo](https://books.rakuten.co.jp/rk/7d4ed327e1c93affa3e847392368f24c/) lists Number Nine, 百合コレ, Japanese and digital release **2023-03-24**; [Comic Cmoa](https://www.cmoa.jp/title/265591/) corroborates that release/classification; [Renta](https://renta.papy.co.jp/renta/sc/frm/item/330784/) lists **24 pages** with cover/colophon included in its counting convention. Renta's own 2023-06-01 availability is platform-specific and does not replace the earlier digital release. These reads occurred **after** the analytical seal. Store descriptions establish bibliography only; every narrative claim is independently grounded in the inspected manga.

Classification: **creator/circle event-publication origin, retained within a later commercially distributed digital edition**. The event cover supports 2017 winter/C93 origin; no exact physical distribution day or independently authenticated physical colophon was recovered. Number Nine's witness wording is sales cooperation, while retailers use publisher metadata. Neither wording is silently replaced by the other. OPF modified time `2023-02-22T09:22:19Z` is a package timestamp, not a fictional date or proven public-release date. No different physical edition, revision history or complete comparison across editions is claimed.

S0004 directly establishes intended after-story continuity; S0005 school return and S0006 two/three-month graduation horizon corroborate a near-ending high-school state. There is no alternate-continuity label. S0022's peer comic is same-series post-exposure material; its exact placement relative to the private visit remains uncertain. Fiction/copyright notices do not make it a parallel timeline. Admission therefore meets the genuine Kodama/NTR and responsible continuity threshold before narrative interpretation.

## Mechanical and visual completeness

EPUB 3.0, `application/epub+zip`, OPF `item/contents.opf`, RTL spine, fixed pre-paginated layout. All **56 ZIP members** pass CRC; no duplicate member names, encryption descriptor or unresolved image targets. **52 manifest items, 24 spine documents, 24 image occurrences, 24 unique image members, zero unreferenced manifest images.** Every source image decodes at **1024×1456** and extraction preserves its bytes/hash. First document `item/xhtml/p-cover.xhtml`; remaining `p0000.xhtml` through `p0022.xhtml`. Extraction followed actual DOM image order, not lexical JPEG order.

Complete ordered visual inspection is **24/24**, personally performed on originals, without OCR. Sixteen principal-story images S0005–0020, the narrative extra S0022, and seven covers/blank/foreword/separator/colophon images are accounted for in the [deep reading](../02%20Supplemental%20Readings/NTR_LATEWINTER_DEEP_READING.md). S0001 and S0023 were additionally inspected for identity/paratext before the complete ordered pass, always after the seal. No narrative page was previewed before admission. No other supplement was read.

Mechanical completeness plus beginning/end/colophon and matching authorized-retail 24-page extent support completeness of **this digital witness**. They cannot prove identity to every original physical edition or undisclosed revision. There are no ads or unrelated inserts to exclude. The extra is interpreted, not silently discarded.

Reproducible coordinates: **NTR-JP-LW/SNNNN/I01**. Spine ordinal is one-based and not asserted to equal printed pagination. Source bytes, extracted images, OPF, per-member CRC/hash/dimensions, ordered manifest and direct reading notes remain outside Git. The completed inspection manifest SHA-256 is `fd4b3b0d51909a78de8f1ed9a70a6a041fe1b7be0a272c8f449777f554d1d3c0`; exact witness/OPF reconstruct its coordinates. Git holds interpreted evidence, not image or mechanical sidecar payloads.

## Sealed analytical order and historical integrity

Fresh starting `origin/main`: **a10ec34d5146bef26f2606a24c21386239db883c**; stable: **b845d8bccc7be905633558d2a767f22e9f78cc50**. Ordinary merge **1a58c7902f5cdd11d204133b358261861f1d31ff**, tree `76a70b637c739fcaf397eb5a38306aebfe11b67d`, imported 14 exact accepted Watayuri files and three accepted routing deltas. The NTR subtree stayed `8e4ebd7522ed865234fcc44715880538b678865f`: all 58 baseline files preserved. No foreign analysis was reauthored.

The pre-admission freeze was added in **882a66c6f48a0b66e4e0679b47417e61c77f61fd**, tree **c4e169a88d9bec690efc2b73795a8e9cf4e6eb76**, timestamp **2026-10-01T15:29:44-04:00**. Its SHA-256 is **3fdf9d40e00ff17bb722c33132f49c13a94831e90c58d5930e7ee9d949c2b6c0**. That commit preceded extraction, source-specific metadata searches, narrative viewing and scoring. The freeze records 7 Y, 7 H, 5 T and 5 F PC rules in literal wording, all originally POSTCORPUS_UNTESTED, plus open propositions and all 58 blob/hash identities. The complete pre-admission snapshot manifest is `c7d365d2c7e5c8bfdc4332d7ece70f07695c9acd12209502bfaae0b2d57e363a` in the working plane.

The twelve V01–V06 reading/freeze files match their individual close commits exactly. V06 close is **50f7e15b331d39e4df16f9b8d62b358933bffe83**, tree **2e7a984085418fbbbefec63587f4abc0d12295f9**; role-gap audit **8fe1601ba53d3188848b9fa58c9b5fc14f36a15d** remains recoverable. Mainline synthesis SHA-256 **7725e2656e57010162c5c9b11685a624addecad3ebe55aa72212260a0fb56fea** and ending study **e1fc1b79369d22fd9ba03d2688b98129a4a1a91ce8d99a777f9e9a1da32ba4db** retain their numbered-mainline identity. Final integration must recheck these bytes and all historical ledger/rule prefixes against the sealed snapshot; the repository audit owns that candidate check and remote readback.

Source audit acceptance is distinct from held-out result acceptance, model development, synthesis coverage, fresh adversarial review and exact-head CI publication. It neither certifies a future commit nor imports the other quarantined side story, drama CD, anime-disc extras, adaptation, interviews, localization or reception.
