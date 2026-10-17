---
title: Genocidal Organ / 虐殺器官 — Source and scope / witness inventory
artifact_id: GENOCIDAL_ORGAN_SOURCE
artifact_type: source_scope_map
series: Genocidal Organ / 虐殺器官
series_id: genocidal-organ
generation: GENOCIDAL_ORGAN_BOOTSTRAP_V1
version: '0.4'
status: active_provisional
scope: Source and scope / witness inventory
source_boundary: GO-JP-EPUB-001 through complete Part I subsection 4; GO-U004; exclusive before spine 13 text/part0011.html
canonical_home: series/genocidal-organ/00 Frameworks and Methods/GENOCIDAL_ORGAN_SOURCE_AND_SCOPE_MAP.md
created: '2026-10-16'
review_status: FOUNDATION_ACCEPTED_CONTINUATION_OWNER_AUTHORIZED
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

Before retention of the pilot verification bundles, direct folder retrieval returned exactly two EPUB entries, one per requested novel; per-file metadata verified their parent IDs. No collection-local README, extraction, checksum manifest, PDF, plain-text copy or English translation was shown in that returned listing. This is bounded observed availability, not a claim that no other copy exists anywhere. Broader title/alias search did not reliably rediscover the known EPUBs, and a parent-filter search returned an empty result despite direct retrieval success. Therefore indexed search is explicitly **incomplete for absence claims**; direct IDs and successful byte retrieval control this inventory. No inaccessible object is declared nonexistent, and no new source copy was acquired from outside the user's existing Drive holdings.

## Bounded reading witness `GO-JP-EPUB-001`

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
| Text capability | Authorized opening rendered legibly in vertical Japanese with ruby; all original p/h1 decoded text matches browser DOM without normalization. No missing Japanese source glyph in selected Noto Serif CJK JP font; this is witness fidelity, not comparison with an unavailable publisher master |
| Pagination / CFI | No page-map member observed; edition-page mapping and stable CFI generation not verified. Use hash-bound member/DOM locators under the method |
| Reading authority | `BOUNDED_WITNESS_VERIFIED_THROUGH_GO_U004`; admitted as the exact usable transformed witness through complete Part I for bounded textual claims, without first-print or publisher-master equivalence |
| Narrative state | GO-U001–004 fully read and prospectively frozen: 57 evidence records / 281 verified narrative locators; exclusive before spine13 text/part0011.html. Calibration supplies 6 additional admitted-source diagnostics. Publication state belongs to receipts/Git |

SHA-256 and ZIP integrity detect byte changes/corruption; they do not authenticate the edition or establish textual completeness. At bootstrap, mechanical parsing did not display narrative passages and human-readable inspection was limited to package metadata/navigation. The fresh G0 inspection below adds bounded opening and paratext rendering. No normalized narrative derivative is promoted or published.

## Observed navigation and unresolved segmentation

The NCX lists five numbered parts with respectively 4, 6, 7, 5 and 5 numbered subsections, followed by an epilogue: **27 numbered subsections plus an epilogue**, not 44 literary units. The OPF has 44 linear spine occurrences including title and ancillary files. Part starts are `text/part0006.html`, `text/part0011.html`, `text/part0018.html`, `text/part0026.html`, and `text/part0032.html`. The first numbered subsection is `text/part0007.html`; the next starts at `text/part0008.html`; the epilogue navigation target is `text/part0038.html`. These are observed navigation targets, not certified literary boundaries. The fresh obligation map below resolves opening roles and explicitly retains uncertain later roles. Beyond GO-U004, later prose remains semantically unread.

Before the first reading, establish a whole-spine **coverage obligation map** without interpreting future text: each occurrence receives an exact identity and provisional role, with any undecided role explicit. Admit/render only the next authorized unit, revising uncertain classifications as reached. The map must account for every opening, section transition, epilogue continuation and ancillary item; a TOC list alone is not full coverage. No chapter/page numbers have been invented.

The G0 inspection verifies the authorized opening against original markup and faithful local rendering. Later sections require their own word/form checks as reached within the authorized run; a metadata language code does not establish reliable transcription.

## Admission conditions and exclusions

G0 accepts a bounded witness identification under the owner's explicit instruction to retain transparent edition uncertainty when usable textual claims remain trustworthy. Fresh bytes, opening legibility, complete structural obligations and original-XML opening-locator retrieval pass. Publisher lineage, completeness against another edition and inactive alternate-stylesheet recovery remain unverified. They cannot support claims of original-edition equivalence. A newly material omission or failed wording locator would block its dependent claim or source unit.

The admitted/read scope is GO-U001–004, including opening literary framing and complete Part I; high-water is exclusive before spine13 text/part0011.html. No later narrative is yet admitted. The owner has now separately authorized continuous sequential reading of this original prose novel through its natural epilogue end. This permission does not pre-admit unread units. Films/scripts, manga, *The Empire of Corpses / 屍者の帝国*, *The Indifference Engine*, *Metal Gear Solid* prose, other short stories, essays/interviews and reception are excluded. Embedded author biography, colophon, publisher material and any other extras require role classification; paratext is never silently treated as narrative. English translations, if later supplied, receive new witness keys and separate wording/locator records. No additional source acquisition or cross-novel study is authorized. The owner-required private verification derivatives are retained in the existing approved evidence collection as identified below; original source objects are unchanged.

## Authorized pilot and stop boundary

The 2026-10-16 owner instruction authorized one transaction from the actual literary framing through the complete first numbered subsection of Part I. Rendered headings and complete ordered content confirm the exact exclusive end before `text/part0008.html`; opening ancillary spans and transitions are all disposed in GO-U001. This was the historical pilot stop; the current entrypoint records the subsequently authorized continuation.

The 2026-10-16 owner instruction now supplies this exact verification/one-unit authorization. G0 recorded an OPEN active single_operation run with GO-U001 as both start and terminal. The pilot now records completed/NONE state; exact-head publication remains independently verified by its operator. The subsequent owner instruction authorizes the current continuous run; pilot freezes remain historical.

## Fresh G0 source audit — 2026-10-16

Direct canonical-folder listing and fresh download reverified Drive ID `1KNobPhIZNRlFPkjqTMUwxxq-hw_Gs-w0`, parent `1kP3-4QyvgbV9jVL84kI6Yj9Rww_otO_3`, 317,774 bytes and unchanged SHA-256 above. Returned modified time: `2026-09-07T22:14:14Z`; shared=false. Retained unchanged original and private deterministic evidence are outside Git. ZIP has 56 members; CRC passes; `mimetype` is first/uncompressed and exact; container resolves `content.opf`; all 49 OPF manifest items exist, all 44 spine references resolve, and all XHTML parses. No encryption manifest, replacement codepoint or unexpected non-whitespace control was found.

Resource caveat: 43 XHTML files reference absent original alternate stylesheets (`styles/a61028197841503098480_h.css` or `_v.css`). Their `rel="alternate stylesheet"` links are inactive; the active bundled `stylesheet.css` and `page_styles.css` resolve. The active CSS supplies vertical-rl writing, ruby, indentation and class styles used by the inspected opening. No missing active image or CSS was found. This does not reconstruct the absent optional horizontal presentation or publisher typography.

Directly inspected title/credits identify the work/author and 2007 copyright; the colophon in spine 44 (`text/part0042.html`) states electronic publication **2012-04-25**, Hayakawa and ©2007. This differs from OPF **2012-08-02** and the separately attributed publisher catalog's **2012-08-01**. None is silently equated or explained. Calibre 5.11.0 metadata, a 2019 timestamp and an ASIN-like identifier confirm transformation traces, not authenticated acquisition lineage. Confidence is high in exact byte identity and usable authorized Japanese wording; bounded/incomplete in edition lineage and external completeness.

Execution: Python 3.12.14; lxml 6.1.1; Playwright 1.62.1; local Chrome headless shell 151.0.7922.34; Noto Serif CJK JP Regular, font SHA-256 `93069d8e9e45d515cc421c971a79e6a5777704b348e36a9ef86578bf58adef77`. Source bytes/CSS are unchanged. A 1500×1000 viewport, 24px inspection font and height constraint make a reflowed screen witness, never printed pages. Opening epigraph, Part I heading, entire subsection 1 and colophon were actually visually inspected; six ruby elements/readings in subsection 1 remain distinct and readable. A whole-source font-cmap check found zero missing codepoints.

Beginning/middle/end representational probes used opening `part0007`, middle `part0021` and end `part0039`. Later probes were rendered with a 10px CSS blur **before screenshots were displayed**; they establish vertical flow/resource/render capability only, not later wording or semantic inspection. Original XML p/h1 text matches browser p/h1 text exactly, including ruby and whitespace. Browser HTML parsing adds one trailing body-level newline; original XML, never browser-body offsets, owns locators. The opening node `/h:html[1]/h:body[1]/h:div[1]/h:p[3]`, spine 9/member `text/part0007.html`, chars 0–45, round-trips with selected-text SHA-256 `2269613562c13aea59ac8edc8fa7d0fe7d033d9d6c84abd78835c2ee93a273ed`. Namespace `h = http://www.w3.org/1999/xhtml`; no normalization.

Entering freeze `GO-U001-ENTER` was recorded at `2026-10-16T21:12:49.679753+00:00`, before narrative words, private record SHA-256 `f0215195bdecb6820964e3ee45a590bc5607e4bdd911912c8d6c60d9029841fd`. Preliminary opening fidelity inspection occurred while CLOSED, after that freeze; the complete short first-subsection screenshot was visible. G0 opened at `2026-10-16T21:20:21.919764+00:00`; ordered analytical rereading and claim authoring follow OPEN. This is disclosed exposure, not a blind test. No later narrative prose or other novel's findings entered the analytical context. Latent model familiarity cannot be certified absent.

### Whole-spine structural coverage obligations

Rows identify every one-based OPF occurrence. Later roles are provisional from navigation/element structure, never narrative interpretation. UNKNOWN means a retained obligation, not an omission.

| Spine | Exact member | Role and disposition (G0 baseline; current admission updated) |
| --- | --- | --- |
| 1 | `titlepage.xhtml` | Cover image; ancillary, inventory verified |
| 2 | `text/part0000.html` | Device display advisory; ancillary, directly inspected |
| 3 | `text/part0001.html` | Japanese title/author page; ancillary, directly inspected |
| 4 | `text/part0002.html` | English title/copyright/design credits; ancillary, directly inspected |
| 5 | `text/part0003.html` | Opening literary epigraph and attribution; included in GO-U001 |
| 6 | `text/part0004.html` | Contents; structural navigation, excluded as narrative |
| 7 | `text/part0005.html` | Work-title heading; transition included/accounted |
| 8 | `text/part0006.html` | Part I heading; included in GO-U001 |
| 9 | `text/part0007.html` | Part I numbered subsection 1; read/frozen in GO-U001, all paragraphs and spacing accounted |
| 10 | `text/part0008.html` | Part I numbered subsection2, completely read/closed as GO-U002; every paragraph/ruby/spacing accounted |
| 11 | `text/part0009.html` | Part I numbered subsection3, completely read/closed as GO-U003; all paragraphs/ruby/spacing accounted |
| 12 | `text/part0010.html` | Complete Part I numbered subsection4, read/closed GO-U004; all text/ruby/spacing accounted |
| 13 | `text/part0011.html` | Part II heading; unadmitted |
| 14 | `text/part0012.html` | Navigation-linked numbered subsection; unadmitted, prose unread |
| 15 | `text/part0013.html` | Navigation-linked numbered subsection; unadmitted, prose unread |
| 16 | `text/part0014.html` | Navigation-linked numbered subsection; unadmitted, prose unread |
| 17 | `text/part0015.html` | Navigation-linked numbered subsection; unadmitted, prose unread |
| 18 | `text/part0016.html` | Navigation-linked numbered subsection; unadmitted, prose unread |
| 19 | `text/part0017.html` | Navigation-linked numbered subsection; unadmitted, prose unread |
| 20 | `text/part0018.html` | Part III heading; unadmitted |
| 21 | `text/part0019.html` | Navigation-linked numbered subsection; unadmitted, prose unread |
| 22 | `text/part0020.html` | Navigation-linked numbered subsection; unadmitted, prose unread |
| 23 | `text/part0021.html` | Navigation-linked numbered subsection; unadmitted, prose unread |
| 24 | `text/part0022.html` | Navigation-linked numbered subsection; unadmitted, prose unread |
| 25 | `text/part0023.html` | Navigation-linked numbered subsection; unadmitted, prose unread |
| 26 | `text/part0024.html` | Navigation-linked numbered subsection; unadmitted, prose unread |
| 27 | `text/part0025.html` | Navigation-linked numbered subsection; unadmitted, prose unread |
| 28 | `text/part0026.html` | Part IV heading; unadmitted |
| 29 | `text/part0027.html` | Navigation-linked numbered subsection; unadmitted, prose unread |
| 30 | `text/part0028.html` | Navigation-linked numbered subsection; unadmitted, prose unread |
| 31 | `text/part0029.html` | Navigation-linked numbered subsection; unadmitted, prose unread |
| 32 | `text/part0030.html` | Navigation-linked numbered subsection; unadmitted, prose unread |
| 33 | `text/part0031.html` | Navigation-linked numbered subsection; unadmitted, prose unread |
| 34 | `text/part0032.html` | Part V heading; unadmitted |
| 35 | `text/part0033.html` | Navigation-linked numbered subsection; unadmitted, prose unread |
| 36 | `text/part0034.html` | Navigation-linked numbered subsection; unadmitted, prose unread |
| 37 | `text/part0035.html` | Navigation-linked numbered subsection; unadmitted, prose unread |
| 38 | `text/part0036.html` | Navigation-linked numbered subsection; unadmitted, prose unread |
| 39 | `text/part0037.html` | Navigation-linked numbered subsection; unadmitted, prose unread |
| 40 | `text/part0038.html` | Epilogue heading; unadmitted |
| 41 | `text/part0039.html` | Provisional epilogue continuation from adjacent heading/structure; unadmitted, semantics unread |
| 42 | `text/part0040.html` | UNKNOWN short trailing member; unadmitted, classify when reached |
| 43 | `text/part0041.html` | UNKNOWN note-class trailing member; unadmitted, classify when reached |
| 44 | `text/part0042.html` | Colophon; paratext, directly inspected for witness identity, not narrative admission |

## GO-U001 coverage closeout and next candidate

[GO-U001](../01%20Sequential%20Readings/GO_U001_OPENING_AND_PART_I_SUBSECTION_1.md) closes the epigraph at spine 5, accounted contents/work-title transitions, Part I heading at 8 and entire subsection at 9, including all 26 direct paragraphs (20 nonempty / 6 empty) and numbered heading. Subsection 1 has six ruby elements; raw body text has 1,606 Unicode codepoints with whitespace/rt. Eleven evidence IDs resolve through 24 original-XML selected-text hashes, all round-tripped; source identity and boundary remain unchanged. At GO-U001 exit, its source-frontier and three cumulative dispositions were complete, with one still-untested conditional prediction and no later validation; GO-U002 supplies the subsequent disposition below.

At pilot exit the next candidate was GO-U002, spine10 text/part0008.html; that historical boundary remains frozen in GO-U001. Current GO-U002 is now closed as recorded below. Retain subsection-level atomicity: short GO-U001 nevertheless contains several recognition/agency transitions, while next-member mechanical length alone does not justify grouping. At GO-U002 closeout GO-U003 was next; the latest current frontier is recorded in the GO-U004 closeout below. Later structural obligations/UNKNOWN classifications above remain open and are not counted as completed coverage.

## Private verification evidence retained — 2026-10-16

The coordinating operator retained the bounded source-verification material, locator/structural records, actual opening/paratext renders, concealed later-layout diagnostics, factual gate/exposure records and exact transformation/tool provenance as `GO-U001_PRIVATE_SOURCE_VERIFICATION_20261016_V1.zip`, Drive file ID `1dC6XV4cK5u9K2jYKOwyhjd2WJ8JWEStC`, in the same canonical Project Itoh folder. Original EPUB bytes remain unchanged at their original ID. The uploaded object is private (`shared=false`); its full downloaded readback matches **1,282,291 bytes**, SHA-256 `5b7f40e12ea3376bb00919f8a7a54da0f79453e277ea1c84db2c067d22058382`. The archive contains a per-object hash manifest and reproduction instructions. Reinstallable runtime binaries, caches, full-novel extractions/later plaintext, redundant original EPUB copies, failed render attempts and interpretive reading/ledger/exit prose are excluded. Git remains the canonical home for the frozen analytical states. These evidence files add no later semantic reading or edition-authentication claim.

## Historical GO-U002 coverage closeout and frontier at its exit

[GO-U002](../01%20Sequential%20Readings/GO_U002_PART_I_SUBSECTION_2.md) admits the entire visible numbered subsection2 at spine10/member `text/part0008.html`, exclusive before spine11/member `text/part0009.html`. Repeat original archive hash/CRC pass; member SHA-256 `669678376ca788b49d2f62d51f5523747603c3fb96b7bff520a61c6b2b65c015`. All101 p elements (nested numeral +100 direct outer paragraphs; six empty), 9,565 raw body codepoints, 52ruby/58rt and active-resource/form dispositions are verified. Original XML/browser texts match exactly. All nine overlapping right-to-left render tiles were actually visually inspected with every paragraph bound inside the widened viewport; no narrow-viewport columns are silently omitted. Sixteen evidence records /84 original-XML locators all round-trip. Private originals and render evidence stay outside public Git.

At GO-U002 exit, unit counts were two, with27 evidence records and108 verified narrative locators; the admitted-source GO-U001 calibration adds six exact diagnostics without a new unit. GO-PR001 now has its actual GO-U002 disposition; the frozen prior wording is preserved. At GO-U002 closeout, high-water was GO-U002 and next candidate GO-U003 is spine11 `text/part0009.html` through exclusive before spine12 `text/part0010.html`, subject to its own complete natural-boundary/form inspection. No next words had then been opened. The semantic terminal token remains bound to the original full archive hash above and all44 obligations, including classification of UNKNOWN trailing members when reached. Permission for the complete run is not a claim of completed novel coverage.

## GO-U002 adopted private source verification retention

The coordinating operator retained `GO-U002_PRIVATE_SOURCE_VERIFICATION_20261016_V2.zip` in the same approved Project Itoh folder `1kP3-4QyvgbV9jVL84kI6Yj9Rww_otO_3`, Drive ID `1N98EmdsjhUK5mycn380iIyALRl5uDMzP`, private (`shared=false`). Complete remote downloaded readback is **3,975,969 bytes**, SHA-256 `8c209bcfeb71edc1b509ff96b421df46ae77acb13fb62a3bbed2de2e55955ffc`. ZIP CRC, exact21-member listing and all20 manifest object byte/hash checks PASS; internal manifest SHA-256 `8835c73a4a944f5a1dfdcea53f6830103f36601d45a123c7b47b9fcb99ec5316`. The original EPUB and its permissions are unchanged.

The source-verification plane contains only the adopted bounded selected-member extraction, original-XML locators/hashes, coverage, all9 actual renders/geometry, source-only independent proof, noninterpretive gate timing/hash references, tools and reproduction provenance, plus admitted-GO-U001 source-only calibration context/diagnostics. Analytical entering/exit prose, ledger/reading/addendum copies, interpretive calibration candidate and full interpretive QA are preserved separately in canonical Git/private analytical checkpoints, not duplicated in this Drive source bundle. Original EPUB duplicates, full-novel/later plaintext and reinstallable runtime binaries are excluded. Retention adds no new narrative admission or edition-authentication claim.

## Historical GO-U003 coverage closeout and frontier at its exit

[GO-U003](../01%20Sequential%20Readings/GO_U003_PART_I_SUBSECTION_3.md) closes the entire visible Part I numbered subsection3 at spine11 `text/part0009.html`, exclusive before spine12 `text/part0010.html`. Member16,565 bytes, SHA-256 `fc034a3161ec84af0aa201c9fcd76746abe9c6f49bff1439cfb40e4c551d7ee6`; unchanged original archive hash above. All40 p elements (nested numeral +39direct outer;3empty),4,577raw body codepoints,17ruby/19rt and all5 overlapping right-to-left render tiles were inspected. Original XML/browser paragraph texts match; all paragraph bounds fit5,897px widened viewport. Ten evidence records /36original-XML locator hashes all round-trip, independently reverified. The three-disembarking/four-dead count relation is retained without numerical repair or invented extra subject.

At GO-U003 exit, high-water was GO-U003 with37evidence/144narrative locators plus6calibration diagnostics. GO-U004 was next at spine12, then unopened. Its complete source/housekeeping/final exact-head sequence subsequently passed before GO-U004 entry; the latest frontier is below. Later obligations including UNKNOWN42–43 and the natural epilogue remain open.

## GO-U003 adopted private source verification retention

The bounded source-verification bundle `GO-U003_PRIVATE_SOURCE_VERIFICATION_20261016_V1.zip` is retained in the approved original evidence folder `1kP3-4QyvgbV9jVL84kI6Yj9Rww_otO_3`, Drive ID `1uHXVL1QuqFryjPDtTnGzSfQxJZvLPUih`, private (`shared=false`). Full raw remote readback matches **2,204,416 bytes**, SHA-256 `b2b0d9ed7066ad6c23936066299af7b5495ab67eba0d1cf9c9c14adc6dacd18e`. Safe paths/ZIP CRC, exact17 members and all16 manifest objects' byte/hash checks PASS; manifest SHA-256 `d330cf14c764b3ffc4b2493f3823e4f804f23b4241d2bae399019764c3e233ad`. The delegated metadata-only custodian verified upload metadata and full readback. Original EPUB/permissions remain unchanged.

The bundle contains only the bounded admitted member's selected extract, locators/hashes, coverage/geometry, all5 actual renders, source-only independent proof, noninterpretive gate timestamp/hash references, scripts and reproduction provenance. Analytical entering/exit states, frozen reading/ledgers and interpretive QA remain in canonical Git/private analytical checkpoints, outside this source-evidence ZIP. No original EPUB duplicate, later plaintext or runtime binary is included.

## GO-U004 coverage closeout and current frontier — 2026-10-17

[GO-U004](../01%20Sequential%20Readings/GO_U004_PART_I_SUBSECTION_4.md) admits the complete final numbered subsection of Part I at spine12 `text/part0010.html`, exclusive before spine13 `text/part0011.html`. Current member54,128bytes, SHA-256 `afcae936629d87e30094f42ccecf2e9bef60dd4567b4dacabb4e4d6bcaca3b41`; unchanged archive317,774bytes/exact original hash/CRC PASS. All180p (nested numeral +179direct;7empty),14,941bodycodepoints,35ruby/45rt and14RTLrender tiles were actually read/viewed. All180originalXML/browser texts match; every bound fits19,694×1,000 viewport.20evidence/137selected originalXML locators independently round-trip, including spacing/form anchors. No Part II words/images were opened.

High-water is GO-U004, four completed units/complete Part I; cumulative57evidence/281narrative locators plus6retrospective calibration diagnostics. Next GO-U005 includes Part II heading spine13 `text/part0011.html` plus first subsection spine14 `text/part0012.html`, exclusive before spine15 `text/part0013.html`, subject to its prospective freeze and actual form/natural-boundary check. Source/housekeeping/final exact-head success for the current publication still precedes those words. All remaining structural obligations are retained, including classification of UNKNOWN42–43 when reached.

## GO-U004 adopted private source verification retention

`GO-U004_PRIVATE_SOURCE_VERIFICATION_20261017_V1.zip` is retained in approved folder `1kP3-4QyvgbV9jVL84kI6Yj9Rww_otO_3`, Drive ID `1dT441L1kEy9zXN_rSpt90So_AOCIrF7Z`, private (`shared=false`). Full raw remote readback matches **5,913,144bytes**, SHA-256 `7a57e3a9c6a29c58ef8a5bd0f3a5a04cd5dd3a338097827d9511ad5dbe81faa9`. ZIP CRC/safe paths, exact26members/all25manifest objects' complete byte/hash checks PASS; manifest SHA-256 `8e319d734aca28a9bd22ba6acd318dbafd1f95183279aa3587c04a641586d10f`. The delegated metadata-only custodian verified upload metadata and raw readback. Original EPUB/permissions are unchanged.

The adopted source-only plane contains current-member selected extraction, locators/hashes, coverage/geometry, all14actual renders, source-only independent proof, noninterpretive gate timing/hash references, scripts/groups and reproduction README. Full analytical entry/exit states, frozen reading/ledgers and interpretive QA remain separately canonical Git/private analytical checkpoints. No original duplicate, later plaintext or runtime binary is included.
