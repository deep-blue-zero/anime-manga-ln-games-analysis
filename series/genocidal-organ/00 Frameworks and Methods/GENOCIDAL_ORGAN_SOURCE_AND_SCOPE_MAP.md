---
title: Genocidal Organ / 虐殺器官 — Source and scope / witness inventory
artifact_id: GENOCIDAL_ORGAN_SOURCE
artifact_type: source_scope_map
series: Genocidal Organ / 虐殺器官
series_id: genocidal-organ
generation: GENOCIDAL_ORGAN_BOOTSTRAP_V1
version: '0.1'
status: active_provisional
scope: Source and scope / witness inventory
source_boundary: Original Japanese prose novel; candidate EPUB structurally inspected; zero narrative units admitted or read
canonical_home: series/genocidal-organ/00 Frameworks and Methods/GENOCIDAL_ORGAN_SOURCE_AND_SCOPE_MAP.md
created: '2026-10-16'
review_status: OWNER_REVIEW_PENDING
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
do_not_use_as_literary_evidence: true
---

# Genocidal Organ / 虐殺器官 — source and scope map

Return to [the sole current entrypoint](../CURRENT_STATE_AND_CORPUS_MAP.md). This map records reconnaissance on 2026-10-16 UTC. **Inventory, bytes, source fidelity, admission and reading are separate states.**

## Bibliographic witnesses, not file identifications

| Reference key | Verified record | What it establishes |
| --- | --- | --- |
| `GO-BIB-ORIGINAL` | [NDL bibliographic record 000008596365](https://ndlsearch.ndl.go.jp/books/R100000002-I000008596365) | 伊藤計劃; 早川書房; 2007.6; Japanese; ハヤカワSFシリーズ Jコレクション; ISBN `978-4-15-208831-4`; 282 print pages, 19 cm |
| `GO-BIB-DIGITAL` | [Hayakawa electronic edition](https://www.hayakawa-online.co.jp/shop/g/g0000610281/) | Separate electronic product, publisher date 2012-08-01; product code `0000610281`; not proof of this EPUB's lineage |
| `GO-BIB-LATER-PRINT` | [Hayakawa 新版](https://www.hayakawa-online.co.jp/shop/g/g0000021165/) | Separate 2014-08-08 ハヤカワ文庫JA product; ISBN `9784150311650`; 432 pages; no textual-change claim inferred from 新版 |

Original publication year 2007 identifies the work; it does not identify the Drive object's edition. The print page counts above must never become EPUB page locators. Publisher descriptions were used only for bibliographic/form warnings, not narrative evidence. No online plot summary, adaptation or remembered plot is admitted. Other print impressions and translations remain distinct potential witnesses, not silently equivalent copies.

## Governed source route and search boundary

- Canonical evidence root ID: `1tNJvglC-ri_AEGTkJupZ78WddyiCqQMy`.
- Governing README ID: `1K5p3nbvCyNIkHrGID7iIp6KWx_k_yMZstEa6udHks1g` (read in full).
- Living series/evidence inventory ID: `1bfPi00AKmELjeXmdCudU_4HqOknTIOODANEi12GDJFw` (read in full; Project Itoh row identifies both Japanese EPUBs).
- Project Itoh collection ID: `1kP3-4QyvgbV9jVL84kI6Yj9Rww_otO_3`.

Direct folder retrieval returned exactly two EPUB entries, one per requested novel; per-file metadata verified their parent IDs. No collection-local README, extraction, checksum manifest, PDF, plain-text copy or English translation was shown in that returned listing. This is bounded observed availability, not a claim that no other copy exists anywhere. Broader title/alias search did not reliably rediscover the known EPUBs, and a parent-filter search returned an empty result despite direct retrieval success. Therefore indexed search is explicitly **incomplete for absence claims**; direct IDs and successful byte retrieval control this inventory. No inaccessible object is declared nonexistent, and no new source copy was acquired from outside the user's existing Drive holdings.

## Candidate witness `GO-JP-EPUB-001`

| Field | Observed value / verification level |
| --- | --- |
| Drive ID | `1KNobPhIZNRlFPkjqTMUwxxq-hw_Gs-w0` |
| Returned filename | `Genocidal Organ  - Project Itoh [Japanese].epub` |
| Format / downloaded length | `application/epub+zip`; EPUB 2.0; 317,774 bytes, equal to provider-reported size |
| SHA-256 | `a4107c01b69c0e8819818eabb0198cc62d4174aa173eb0ebdca3a0dbf93b7df0` |
| Hash method | Fresh Python `hashlib.sha256` over the complete retrieved archive on 2026-10-16; identifies these bytes only |
| Independent expected digest | Not supplied by returned Drive metadata; no preexisting checksum manifest found in the direct collection listing; no remote hash-equivalence or publisher-authenticity claim |
| Package metadata | `content.opf`: title `虐殺器官`, author `伊藤計劃`, language `ja`, publisher `早川書房` |
| Package date | `2012-08-02T05:00:00+00:00`; differs from the publisher's 2012-08-01 electronic date; unresolved, not silently normalized |
| Package identifier | `B009DEMA02` plus package UUID identifiers; no verified edition ISBN in inspected metadata |
| Transformation indications | Calibre metadata and split/generated packaging exist; exact acquisition and transformation lineage unverified |
| Archive/package | ZIP CRC check passed; container points to `content.opf`; all inspected XHTML parses; OPF declares vertical right-to-left writing; no encryption manifest detected |
| Text capability | Japanese codepoints mechanically detected in decodable XHTML; prose legibility, omissions, rendering and wording fidelity NOT certified by this scan |
| Pagination / CFI | No page-map member observed; edition-page mapping and stable CFI generation not verified. Use hash-bound member/DOM locators under the method |
| Reading authority | `SOURCE_NOT_YET_VERIFIED`; candidate only, no authoritative Japanese witness selected |
| Narrative state | `NOT_ADMITTED`; 0 units read; no character or interpretive findings |

SHA-256 and ZIP integrity detect byte changes/corruption; they do not authenticate the edition or establish textual completeness. Mechanical parsing did not display narrative passages to the analyst. Human-readable inspection was limited to package metadata and navigation. No normalized narrative derivative is promoted or published.

## Observed navigation and unresolved segmentation

The NCX lists five numbered parts with respectively 4, 6, 7, 5 and 5 numbered subsections, followed by an epilogue: **27 numbered subsections plus an epilogue**, not 44 literary units. The OPF has 44 linear spine occurrences including title and ancillary files. Part starts are `text/part0006.html`, `text/part0011.html`, `text/part0018.html`, `text/part0026.html`, and `text/part0032.html`. The first numbered subsection is `text/part0007.html`; the next starts at `text/part0008.html`; the epilogue navigation target is `text/part0038.html`. These are observed navigation targets, not certified literary boundaries. Front matter, part headings and trailing non-NCX material still need content-role classification. No part or section has been read.

Before the first reading, establish a whole-spine **coverage obligation map** without interpreting future text: each occurrence receives an exact identity and provisional role, with any undecided role explicit. Admit/render only the next authorized unit, revising uncertain classifications as reached. The map must account for every opening, section transition, epilogue continuation and ancillary item; a TOC list alone is not full coverage. No chapter/page numbers have been invented.

The future reader must verify prose, ruby, symbols and institutional terminology against a faithful rendering. A metadata language code does not establish reliable word-level transcription.

## Admission conditions and exclusions

Resolve the candidate's edition/provenance and usable Japanese representation; retain the bytes and source key; reconcile colophon/title metadata with an appropriate publication record or record an owner-accepted bounded uncertainty. Verify the opening's legibility and source/locator round trip, classify its actual literary limits, and document any omission or transformation. If these conditions cannot support the claim scope, keep `SOURCE_NOT_YET_VERIFIED` and the lock CLOSED. Owner approval cannot convert an unknown fact into a verified one.

Admitted scope is currently empty. The intended later scope is this original prose novel in a verified Japanese witness. Films/scripts, manga, *The Empire of Corpses / 屍者の帝国*, *The Indifference Engine*, *Metal Gear Solid* prose, other short stories, essays/interviews and reception are excluded. Embedded author biography, colophon, publisher material and any other extras require role classification; paratext is never silently treated as narrative. English translations, if later supplied, receive new witness keys and separate wording/locator records. No extra source acquisition, upload, Drive modification or cross-novel study is authorized now.

## First separately authorizable reading operation

After review and witness acceptance, authorize one transaction from the verified narrative beginning through the end of the first numbered subsection of Part I, including any preceding narrative framing. Candidate terminal boundary: immediately before `text/part0008.html`, subject to confirming that the real section boundary matches that navigation target. Do not discard earlier spine items as boilerplate without classifying them. No later subsection is authorized by this proposal.

That future instruction must explicitly authorize witness verification and the one narrative unit after owner review, including its permitted writes. Record the unit in a real run with a matching authorized start/terminal boundary, OPEN lock and consistent next fields only when those prerequisites are satisfied. Current next permission remains owner review.
