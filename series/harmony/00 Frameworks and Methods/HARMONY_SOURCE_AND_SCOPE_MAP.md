---
title: Harmony / ハーモニー — Source and scope / witness inventory
artifact_id: HARMONY_SOURCE
artifact_type: source_scope_map
series: Harmony / ハーモニー
series_id: harmony
generation: HARMONY_BOOTSTRAP_V1
version: '0.5'
status: active_provisional
scope: Source and scope / witness inventory
source_boundary: HAR-JP-EPUB-001 d583f6dc36612eb1aec9b18c4ae5a61460388591ee00f38abc2bbd69071fbbae; HAR-U004 through spine 12, exclusive before text/part0006_split_005.html; later narrative unread
canonical_home: series/harmony/00 Frameworks and Methods/HARMONY_SOURCE_AND_SCOPE_MAP.md
created: '2026-10-16'
review_status: SCOPED_FOUNDATION_ACCEPTED_2026_10_16
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
do_not_use_as_literary_evidence: true
---

# Harmony / ハーモニー — source and scope map

Return to [the sole current entrypoint](../CURRENT_STATE_AND_CORPUS_MAP.md). This map records reconnaissance on 2026-10-16 UTC. **Inventory, bytes, source fidelity, admission and reading are separate states.** The dated pilot verification below supersedes the bootstrap’s pending operational source assertions without altering its historical receipt.

## Bibliographic witnesses, not file identifications

| Reference key | Verified record | What it establishes |
| --- | --- | --- |
| `HAR-BIB-ORIGINAL` | [NDL bibliographic record 000009987035](https://ndlsearch.ndl.go.jp/books/R100000002-I000009987035) | 伊藤計劃; 早川書房; 2008.12; Japanese; ハヤカワSFシリーズ Jコレクション; ISBN `978-4-15-208992-2`; 354 print pages, 19 cm |
| `HAR-BIB-DIGITAL` | [Hayakawa electronic edition](https://www.hayakawa-online.co.jp/shop/g/g0000610282/) | Separate electronic product, publisher date 2012-08-01; product code `0000610282`; not proof of this EPUB's lineage |
| `HAR-BIB-LATER-PRINT` | [Hayakawa 新版](https://www.hayakawa-online.co.jp/shop/g/g0000021166/) | Separate 2014-08-08 ハヤカワ文庫JA product; ISBN `9784150311667`; 400 pages; no textual-change claim inferred from 新版 |

Original publication year 2008 identifies the work; it does not identify the Drive object's edition. The print page counts above must never become EPUB page locators. Publisher descriptions were used only for bibliographic/form warnings, not narrative evidence. No online plot summary, adaptation or remembered plot is admitted. Other print impressions and translations remain distinct potential witnesses, not silently equivalent copies.

## Governed source route and search boundary

- Canonical evidence root ID: `1tNJvglC-ri_AEGTkJupZ78WddyiCqQMy`.
- Governing README ID: `1K5p3nbvCyNIkHrGID7iIp6KWx_k_yMZstEa6udHks1g` (read in full).
- Living series/evidence inventory ID: `1bfPi00AKmELjeXmdCudU_4HqOknTIOODANEi12GDJFw` (read in full; Project Itoh row identifies both Japanese EPUBs).
- Project Itoh collection ID: `1kP3-4QyvgbV9jVL84kI6Yj9Rww_otO_3`.

Before retention of the pilot verification bundles, direct folder retrieval returned exactly two EPUB entries, one per requested novel; per-file metadata verified their parent IDs. No collection-local README, extraction, checksum manifest, PDF, plain-text copy or English translation was shown in that returned listing. This is bounded observed availability, not a claim that no other copy exists anywhere. Broader title/alias search did not reliably rediscover the known EPUBs, and a parent-filter search returned an empty result despite direct retrieval success. Therefore indexed search is explicitly **incomplete for absence claims**; direct IDs and successful byte retrieval control this inventory. No inaccessible object is declared nonexistent, and no new source copy was acquired from outside the user's existing Drive holdings.

## Identified bounded witness `HAR-JP-EPUB-001`

| Field | Observed value / verification level |
| --- | --- |
| Drive ID | `1XBGr6QAThSu3rDAALR9DI_hMFD1cC6E3` |
| Returned filename | `Harmony - Project Itoh [Japanese].epub` |
| Format / downloaded length | `application/epub+zip`; EPUB 2.0; 454,020 bytes, equal to provider-reported size |
| SHA-256 | `d583f6dc36612eb1aec9b18c4ae5a61460388591ee00f38abc2bbd69071fbbae` |
| Hash method | Fresh Python `hashlib.sha256` over the complete retrieved archive on 2026-10-16; identifies these bytes only |
| Independent expected digest | Not supplied by returned Drive metadata; no preexisting checksum manifest found in the direct collection listing; no remote hash-equivalence or publisher-authenticity claim |
| Package metadata | `content.opf`: title `ハーモニー`, author `伊藤計劃`, language `ja`, publisher `早川書房` |
| Package date | `2012-08-02T05:00:00+00:00`; differs from the publisher's 2012-08-01 electronic date; unresolved, not silently normalized |
| Package identifier | `B009DEMA1Q` plus package UUID identifiers; no verified edition ISBN in inspected metadata |
| Transformation indications | Calibre metadata and split/generated packaging exist; exact acquisition and transformation lineage unverified |
| Archive/package | Fresh ZIP CRC passes; container resolves `content.opf`; 44 declared manifest resources and all 40 spine occurrences resolve/parse; active CSS resolves; 39 absent alternate-stylesheet links are separately bounded below; no encryption manifest |
| Text capability | Admitted units through HAR-U004 are legible Japanese; meaningful text/form round-trips through source XHTML, XML-aware extraction and faithful source-CSS rendering; prose beyond this frontier remains semantically uninspected |
| Pagination / CFI | No page-map member observed; edition-page mapping and stable CFI generation not verified. Use hash-bound member/DOM locators under the method |
| Reading authority | `VERIFIED_WITNESS_THROUGH_HAR_U004`; exact transformed Japanese witness, incremental unit fidelity, unchanged lineage caveats |
| Narrative state | `ADMITTED_THROUGH_HAR-U004`; opening/01 and entire02/03/04 fully read/closed; 50 evidence IDs / 53 spans; exclusive before 05 |

SHA-256 and ZIP integrity detect byte changes/corruption; they do not authenticate the edition or establish textual completeness. At bootstrap, mechanical parsing did not display narrative passages and human-readable inspection was limited to package metadata/navigation. The later pilot source audit is explicitly recorded below. No normalized narrative derivative is promoted or published.

## Observed navigation and unresolved segmentation

The NCX lists four numbered parts with respectively 6, 3, 6 and 4 numbered subsections, followed by an epilogue: **19 numbered subsections plus an epilogue**, not 40 literary units. The OPF has 40 linear spine occurrences. Part navigation targets are `text/part0005.html`, `text/part0007.html`, `text/part0009.html`, and `text/part0011.html`. Numbered subsection targets include `text/part0006_split_001.html` through `_006.html` for Part 1. The epilogue heading target is `text/part0014.html`; following material includes `text/part0015.html`, which must not be omitted by following TOC targets alone. Each part also has an unnumbered `_split_000.html` item. At bootstrap, opening/framing material, unnumbered items and non-NCX trailing material remained unclassified. The pilot audit classifies the current opening below; later roles remain provisional or UNKNOWN until separately authorized inspection. File splitting is not proof of a literary section. At bootstrap no part or section had been read. The later G0 source audit covered the opening representation only; HAR-U001 now owns the bounded literary reading, without later prose exposure.

The pilot audit established the whole-spine **coverage obligation map** below without interpreting future text: each occurrence receives an exact identity and provisional role, with any undecided role explicit. Admit/render only the next authorized unit, revising uncertain classifications as reached. The map must account for every opening, section transition, epilogue continuation and ancillary item; a TOC list alone is not full coverage. No chapter/page numbers have been invented.

The publisher form warning is at the electronic-edition record above. At bootstrap, literal angle-like notation had been mechanically detected but not visually round-tripped. The bounded pilot audit below closes that opening-form obligation; it does not certify typography throughout the novel.

## Admission conditions and exclusions

The pilot admitted only claims retrievable in this exact witness’s verified opening. The owner’s subsequent continuous run now authorizes the remaining original novel, with usable representation and exact locators verified incrementally before each unit’s claims are accepted. It does not certify publisher lineage, equivalence to the 2008 first printing, or later-narrative completeness. Any later material fidelity defect reopens the affected obligation; owner authorization cannot convert an unknown fact into a verified one.

At G0 the witness was verified for HAR-U001 with zero sequential-analysis admissions; the ensuing HAR-U001 transaction admits and closes only that opening unit. That pilot did not itself authorize broader reading; the later owner instruction now authorizes the original novel’s full sequential continuation as recorded below. Films/scripts, manga, *The Empire of Corpses / 屍者の帝国*, *The Indifference Engine*, *Metal Gear Solid* prose, other short stories, essays/interviews and reception are excluded. Embedded author biography, colophon, publisher material and any other extras require role classification; paratext is never silently treated as narrative. English translations, if later supplied, receive new witness keys and separate wording/locator records. No new source acquisition or cross-novel study is authorized. Private deterministic verification derivatives remain outside Git; no source payload is published.

## Authorized pilot and exclusive boundary

The owner’s 2026-10-16 pilot instruction authorizes one transaction from the opening framing, including the unnumbered Part I opening, through numbered 01. Source XHTML and rendering confirm the exclusive endpoint immediately before `text/part0006_split_002.html`, whose h2/NCX label is 02. No body prose from that member or later narrative is inspected. Preceding spine occurrences are disposed individually below.

G0 passed under the exact owner instruction, reviewed foundation, verified bounded witness/locators and initialized ledgers. The G0 entrypoint recorded OPEN and an active single_operation with start = terminal = HAR-U001. Main now preserves that exact admission checkpoint; the completed pilot branch records completed/NONE with both next-operation fields NONE, and the architecture lock remains OPEN without continuation permission. The historical bootstrap remains a truthful zero-unit CLOSED snapshot.


## Pilot witness verification — 2026-10-16

The canonical folder was directly listed again by the coordinating operator; file `1XBGr6QAThSu3rDAALR9DI_hMFD1cC6E3` retained its expected parent, name, 454,020-byte length and SHA-256 `d583f6dc36612eb1aec9b18c4ae5a61460388591ee00f38abc2bbd69071fbbae`. Provider metadata reports modified `2026-09-07T22:15:28Z`, `shared=false`. Fresh local hashing independently confirms the downloaded bytes. ZIP CRC, stored first `mimetype`, container, OPF/spine/manifest and all local active stylesheet/image references pass. The absent 39 links have `rel="alternate stylesheet"`; they request old horizontal/vertical variants, while both active bundled stylesheets resolve. Uncovered class names occur only on those alternate-link elements. This bounds the default presentation; the missing optional variants and original publisher layout are not reconstructed.

Directly inspected bibliographic paratext: title/author match; credit names Project Itoh and 2008; the cover image visibly bears 新版; colophon gives electronic publication **2012-04-25**. Publisher catalog date **2012-08-01**, OPF date **2012-08-02**, Calibre 5.44.0 packaging and later transformation timestamps remain separately attributed. Colophon date retrieval separately round-trips (bibliographic provenance, not a narrative evidence ID): `HAR-JP-EPUB-001@sha256:d583f6dc36612eb1aec9b18c4ae5a61460388591ee00f38abc2bbd69071fbbae::spine:40::member:text/part0019.html::node:/h:html[1]/h:body[1]/h:div[1]/h:p[3]::chars:0-19`; selected UTF-8 SHA-256 `4c79207a32b19e7b8d9204b74b669e1320a02dab8e62b8768ceec00379c597b9`. The cover designation and dates prevent a confident impression/edition assignment. They do not demonstrate a particular textual revision. This is an exact, usable **transformed Japanese digital witness**, not an authenticated original-print-equivalent edition.

Three-way opening check: original XHTML bytes versus `HAR-LOC-1` XML string-values/event export versus locally rendered, byte-identical XHTML views. Browser **Chrome headless shell 151.0.7922.34**, Playwright **1.62.1**; parser Python **3.12.14**, lxml **6.1.1**, libxml2 **2.14.6**. The original `.html` suffix initially invoked HTML parsing and added a final body newline; byte-identical private `.view.xhtml` copies force XHTML parsing and restore exact raw body lengths (159 and 103 codepoints for unnumbered opening and 01). Only font selection (`Noto Serif CJK JP`) is supplied as an ebook-viewer setting; source CSS, DOM content/order, spacing, indentation, line breaks, case and punctuation are retained. The font collection SHA-256 is `93069d8e9e45d515cc421c971a79e6a5777704b348e36a9ef86578bf58adef77`; all selected opening/colophon glyphs exist in it.

The source-facing analyst visually inspected nine original-content renders: cover, notice, title, credit, work-title divider, Part I heading, unnumbered framing, complete numbered 01 and colophon. The Part I heading is horizontal under bundled CSS; the framing and 01 are vertical-rl. Literal literary delimiters are **U+3008/U+3009**, not ASCII XHTML angle brackets; they remain text nodes. Protocol-like case, colon/slash nesting, the three separately indented declaration lines and explicit `br`/blank-paragraph events are preserved. No ruby occurs in the authorized opening. The colophon’s ruby base 伊藤計劃 and readings いとうけいかく remain separately associated and were visually checked; raw offset text includes readings, rather than pretending this is plain base text.

Later-spine processing is structural only: XML decoding succeeds, no replacement/private-use characters are detected, and ruby/resource counts are recorded without displaying later lexical content. Middle and epilogue-continuation presentation probes use browser geometry with every lexical glyph concealed before inspection; these establish only writing direction, resource/layout availability and ruby placement, not the wording or completeness of unread narrative. No later prose is used to interpret the pilot. Original EPUB, local source views, screenshots and deterministic event/text derivatives stay in the private evidence/working plane outside Git.

Before any source-containing display, the entering freeze pinned the exact witness, proposed boundary, empty claim/prediction state, unknown actor/narrator frontier and anti-spoiler rules. Freeze SHA-256: `48b64e6ab54dc9717e245ce6b4e1eb9a0d18f3e989a261b095910b3232a40729`. Opening representation words were then exposed as an authorized CLOSED-lock source audit. Package marketing metadata and cover/bibliographic paratext were also seen and excluded from literary evidence. Model pretraining exposure cannot be audited; the reading is constrained, not certified blind. No other novel’s source or analysis supplies evidence.

## Whole-spine structural coverage obligations

Roles after the current admitted frontier remain **provisional** from package/navigation structure; UNKNOWN means inspect/classify only when later authorized, not omit. Hash-bound occurrence identity is the source key/full archive digest above plus each exact one-based spine/member pair. This inventory does not grant narrative admission.

| Spine | Exact member | Structural role / required disposition |
| --- | --- | --- |
| 1 | `titlepage.xhtml` | Cover image; bibliographic inspection only |
| 2 | `text/part0000.html` | Device notice; inspected, not narrative |
| 3 | `text/part0001.html` | Title/author; inspected, not narrative |
| 4 | `text/part0002.html` | Credit; inspected, not narrative |
| 5 | `text/part0003.html` | Contents; navigation inventory only, no later-title inference |
| 6 | `text/part0004.html` | Work-title divider; inspected as opening wrapper |
| 7 | `text/part0005.html` | Part I heading; READ/CLOSED in HAR-U001 |
| 8 | `text/part0006_split_000.html` | Unnumbered Part I framing; READ/CLOSED in HAR-U001 |
| 9 | `text/part0006_split_001.html` | Numbered 01; READ/CLOSED in HAR-U001; exclusive before 02 |
| 10 | `text/part0006_split_002.html` | Part I numbered 02 verified; READ/CLOSED in HAR-U002; full body 0–12192 |
| 11 | `text/part0006_split_003.html` | Part I numbered 03 verified; READ/CLOSED in HAR-U003; full body0–11263 |
| 12 | `text/part0006_split_004.html` | Part I numbered 04 verified; READ/CLOSED in HAR-U004; full body0–6287 |
| 13 | `text/part0006_split_005.html` | Part I numbered 05 h2 only verified; body UNREAD; next frontier |
| 14 | `text/part0006_split_006.html` | Part I numbered 06 from NCX; UNREAD |
| 15 | `text/part0007.html` | Part II heading candidate; UNREAD |
| 16 | `text/part0008_split_000.html` | Unnumbered Part II transition; UNREAD |
| 17 | `text/part0008_split_001.html` | Part II numbered 01 from NCX; UNREAD |
| 18 | `text/part0008_split_002.html` | Part II numbered 02 from NCX; UNREAD |
| 19 | `text/part0008_split_003.html` | Part II numbered 03 from NCX; UNREAD |
| 20 | `text/part0009.html` | Part III heading candidate; UNREAD |
| 21 | `text/part0010_split_000.html` | Unnumbered Part III transition; UNREAD |
| 22 | `text/part0010_split_001.html` | Part III numbered 01 from NCX; UNREAD; masked geometry only |
| 23 | `text/part0010_split_002.html` | Part III numbered 02 from NCX; UNREAD |
| 24 | `text/part0010_split_003.html` | Part III numbered 03 from NCX; UNREAD |
| 25 | `text/part0010_split_004.html` | Part III numbered 04 from NCX; UNREAD |
| 26 | `text/part0010_split_005.html` | Part III numbered 05 from NCX; UNREAD |
| 27 | `text/part0010_split_006.html` | Part III numbered 06 from NCX; UNREAD |
| 28 | `text/part0011.html` | Part IV heading candidate; UNREAD |
| 29 | `text/part0012_split_000.html` | Unnumbered Part IV transition; UNREAD |
| 30 | `text/part0012_split_001.html` | Part IV numbered 01 from NCX; UNREAD |
| 31 | `text/part0012_split_002.html` | Part IV numbered 02 from NCX; UNREAD |
| 32 | `text/part0012_split_003.html` | Part IV numbered 03 from NCX; UNREAD |
| 33 | `text/part0012_split_004.html` | Part IV numbered 04 from NCX; UNREAD |
| 34 | `text/part0013.html` | UNKNOWN transition before epilogue navigation; UNREAD, classification obligation retained |
| 35 | `text/part0014.html` | Epilogue heading candidate from NCX; UNREAD |
| 36 | `text/part0015.html` | Epilogue continuation candidate; UNREAD, masked geometry only |
| 37 | `text/part0016.html` | UNKNOWN trailing component; UNREAD, classification obligation retained |
| 38 | `text/part0017.html` | UNKNOWN / possible author paratext; lexical prose UNREAD |
| 39 | `text/part0018.html` | UNKNOWN / possible rights paratext; lexical prose UNREAD |
| 40 | `text/part0019.html` | Colophon; direct bibliographic/ruby inspection only |

## HAR-U001 analytical closeout and future granularity

[HAR-U001](../01%20Sequential%20Readings/HAR-U001_OPENING_AND_PART_I_01_DEEP_READING.md) owns the opening evidence, all in-scope member/span dispositions and frozen entry/exit. Eight evidence IDs cover eleven selected exact spans; every span and selected SHA-256 round-trips to this archive under HAR-LOC-1. All three ledgers close independently: one anonymous teller/self-presentation/readiness row, no directional relation; explicit no-change for fictional knowledge/institutions/technology/coercion; four claims, no justified prediction and no revision. No named fictional actor or reconstructible behavioral model is established.

The post-pilot recommendation retains one numbered subsection for the next transaction: candidate HAR-U002 would start spine 10 `text/part0006_split_002.html` (02), exclusive before spine 11 `_003.html` (03). Mechanical body length is 12,192 codepoints, not a reading or a reason to group later sections. The pilot’s unusually dense framing merits its preserved independent freeze; causal/epistemic boundaries and ledger overhead after actual later reading can inform future grouping. At pilot closeout HAR-U002 was UNREAD / NOT AUTHORIZED. The later full continuation authorized this next unit, whose words remained unread until its recorded entering freeze. HAR-U002 is now fully closed below; this paragraph preserves the pilot-time recommendation.

## Private verification evidence retained — 2026-10-16

The coordinating operator retained the bounded source-verification material, locator/structural records, actual opening/paratext renders, concealed later-layout diagnostics, factual gate/exposure records and exact transformation/tool provenance as `HAR-U001_PRIVATE_SOURCE_VERIFICATION_20261016_V1.zip`, Drive file ID `1VBbeQIB4cUR8kugtw3Wen7K3JLhRdocw`, in the same canonical Project Itoh folder. Original EPUB bytes remain unchanged at their original ID. The uploaded object is private (`shared=false`); its full downloaded readback matches **8,312,672 bytes**, SHA-256 `7dbffbca8f7ccf024c77f2e6306654be17fa7ca1dbc25112a239764e97846ac9`. The archive contains a per-object hash manifest and reproduction instructions. Reinstallable runtime binaries, caches, full-novel extractions/later plaintext, redundant original EPUB copies, failed render attempts and interpretive reading/ledger/exit prose are excluded. Git remains the canonical home for the frozen analytical states. These evidence files add no later semantic reading or edition-authentication claim.

## Full sequential continuation — authorization and terminal definition

On 2026-10-16 the owner reviewed the pilot and requested continuation using the attached advisory guidance. The current authorized run begins HAR-U002, spine 10 `text/part0006_split_002.html`, and continues through **HARMONY_NATURAL_EPILOGUE_END** in `HAR-JP-EPUB-001` with archive SHA-256 `d583f6dc36612eb1aec9b18c4ae5a61460388591ee00f38abc2bbd69071fbbae`. This token means the actual natural epilogue’s end, including meaningful enclosing literary notation and explicit disposition of every trailing component; it is not a guessed filename or a predetermined count of twenty units. Known structural epilogue candidates are spine 35 `text/part0014.html` and 36 `text/part0015.html`. Spines 34 and 37–39 require classification chronologically when reached; no later prose is opened to fix that classification in advance. The final source/unit/span map will resolve the descriptive terminal token from admitted evidence.

Nineteen numbered subsections plus epilogue suggest HAR-U020 as an eventual ordinal, provisionally; natural/formal boundaries govern. Part headings and unnumbered framing attach to the next natural subsection with complete coverage, and closing transitions receive a reasoned disposition when reached. No spine occurrence is dropped. The original witness bytes, conversion/date caveats and HAR-LOC-1 grammar remain unchanged. The opening fidelity check does not certify unread prose: every newly admitted unit requires complete ordered reading, relevant source/ruby/notation/render comparison and exact load-bearing locator round trips. Historical pilot exposure and freezes remain intact.

## HAR-U002 incremental source and reading closeout

[HAR-U002](../01%20Sequential%20Readings/HAR-U002_PART_I_02_DEEP_READING.md) closes the entire spine 10 member `text/part0006_split_002.html`, including h2/blank/framing elements, raw body chars 0–12192; exclusive before spine 11 `_003.html` (h2 03 only inspected, body UNREAD). Member SHA-256 `3775707febf7c4bab0ed0fbb4fd1f849a6a2ba6aca1fbabc11aa1f3abd6bb6e8`. All 233 heading/paragraph blocks, 34 ruby and 232 br are accounted. All 19 load-bearing body-offset spans re-resolve with exact selected hashes; original XML raw body equals extraction and browser XHTML DOM text.

All seven actual vertical panels were visually inspected in source order. At fixed font/text height, widening the viewport from 1400 to 9448px moved initially negative-x columns into positive bounds; final body x 46.84375–9441.34375, all 233 paragraph rectangles within 9448×1000. Seven overlapping right-to-left panels cover the entire width. Source CSS, actual XHTML MIME parsing and Noto Serif CJK JP reader font preserve literal labels/case, U+3008/U+3009, hierarchy/indentation and ruby associations. The independent Harmony-only review checks the same complete span; later prose remains unexposed. No renderer/source substitution, new G0 or edition-authentication claim is made.

Three-ledger closeout: 5 recognized subjects, 6 historical actor-state rows/6 directional relations, 9 attributed world/information rows, 11 cumulative claims, 0 predictions, 2 pre-entry calibration revisions; 27 evidence records/30 exact spans across two frozen units. Retain one natural subsection per transaction: next HAR-U003 is spine 11 `_003.html`, exclusive before spine 12 `_004.html`; actual boundary/form to be checked only after the first-resumed checkpoint clearance.

## HAR-U002 private verification retention

The coordinator retained `HAR-U002_PRIVATE_SOURCE_VERIFICATION_20261016_V1.zip` as Drive file `1_WPObKLgFOprqr5zpWaNlDqAqJmfqHP7` in canonical folder `1kP3-4QyvgbV9jVL84kI6Yj9Rww_otO_3`, `shared=false`. Full independently downloaded readback matches **4,438,363 bytes**, SHA-256 `4370a19945884a546487dd23af7c614fb792b84ad7ba6eb6e07d8c09344a70e2`; local ZIP CRC and all 18 per-object manifest size/hash checks pass. Manifest SHA-256 `3f603f2ec2351ff70a8cc31e518d4b2a44db40433f9ea643b81b061cd608f7e6`. The bundle contains only this unit’s faithful extraction, actual renders, geometry/ruby records, locator verification, scripts/tool hashes and noninterpretive gate/inspection provenance. Analytical frontiers and interpretive review remain in canonical Git artifacts; whole-book originals, future plaintext, caches and binaries are excluded. The canonical original EPUB remains unchanged at its existing ID. This retention verifies persistence, not publisher authenticity.


## HAR-U003 incremental source and reading closeout

[HAR-U003](../01%20Sequential%20Readings/HAR-U003_PART_I_03_DEEP_READING.md) closes all spine11 `text/part0006_split_003.html`, raw body0–11263, including heading/blanks; exclusive before spine12 `_004.html`, whose h2 numeral04 alone was inspected. Member SHA-256 `ee2589838919b9edc6b94f10cf2e4b896be42b243092f9f6cf16dd000a17c21d`. All186 heading/paragraph blocks,49ruby and185br are accounted, with original XML/extraction/actual XHTML DOM equality and thirteen original-archive selected spans/hash round trips.

The source-facing successor inspected every actual panel: six overlapping right-to-left tiles. Fixed font/text height and viewport8149×1000 enclose all paragraph rectangles; bodyx46.34375–8142.34375. Original CSS, viewer font and XHTML MIME alias preserve source text/form/ruby. No04 body/later prose was displayed. First-resumed checkpoint cleared after HAR-U002 protected integration/post-main success; isolated staffing/exposure provenance is in the continuation receipt, without changing either frozen earlier reading.

Three-ledger closeout:7 subjects/11 historical actor-state rows/12 directional relation IDs with16 historical rows;13 world-information IDs;18 claims/0 predictions/2 earlier revisions;40 cumulative evidence records/43 spans. Two DOMAIN_BOUNDED and five RECOGNITION_ONLY current readiness decisions, no model/validation. Next candidate HAR-U004 is entire natural04, exclusive before `_005.html`; verify actual boundary/form in order after complete publication checks. Witness lineage/date uncertainties persist.


## HAR-U003 private verification retention

The designated metadata-only evidence custodian retained `HAR-U003_PRIVATE_SOURCE_VERIFICATION_20261016_V1.zip` as Drive file `1IV9Yay1GuJ5bXWlQMRPJChqdzzCmIFL6`, canonical folder `1kP3-4QyvgbV9jVL84kI6Yj9Rww_otO_3`, shared=false. Full raw remote readback equals **4,173,028 bytes**, SHA-256 `bffb10a248b392c7f02dc882582652189284f42eecc596372c63cc81bc725e40`; ZIP CRC, safe paths, exact membership and all18 manifest object size/hash checks PASS. Manifest SHA-256 `8ad02dd00253e786caec2cf2799325088c5d8d299dd5c1c67e5887758c14939d`. The bundle contains current-source extraction, six actual renders, geometry/ruby and locator proof, scripts/tool hashes and noninterpretive provenance. Locator labels/interpretive descriptions are excluded. Analytical frontiers remain in Git; future prose, originals, binaries/caches are excluded. Original EPUB is unchanged at its canonical ID. This verifies retention, not publisher authenticity.


## HAR-U004 incremental source and reading closeout

[HAR-U004](../01%20Sequential%20Readings/HAR-U004_PART_I_04_DEEP_READING.md) closes the entire spine12 `text/part0006_split_004.html`, body0–6287, all134 heading/paragraph blocks,27ruby and133br including heading/blanks. Member SHA-256 `53e4d2cdc35b42404b16290e43314e787cfce2db947ac57b857b864d964d6fae`. Next spine13 `_005.html` h2 numeral05 alone was queried; body/later prose remains unexposed. Original XML/extraction/actual XHTML DOM equality, all ten original selected-span/hash round trips and all paragraph bounds PASS. The body includes148 inter-block XML whitespace codepoints beyond the sum of block strings; these are retained, not normalized away.

All four actual overlapping right-to-left panels were inspected by the source author. Fixed font/text height and widened5390×1000 viewport enclose bodyx46.34375–5383.34375 and every paragraph rectangle. Aggregate Range bottom1000.046875 is a subpixel metric; actual panels and allparagraphbounds were inspected, without missing lexical columns. Source CSS, XHTML MIME alias, viewer font and all27ruby/base readings are preserved. A read-only helper's19mechanical checks independently confirm strings/counts/geometry; no independent literary or pixel review is claimed.

All three ledgers close:8subjects/16historicalactor-state rows/14directionalrelationIDs(21historicalrows)/17worldIDs/24claims/0predictions/2earlierrevisions;50cumulativeevidenceIDs/53spans. Two DOMAIN_BOUNDED/six RECOGNITION_ONLY current assessments, no reconstruction/validation/specialists. Next candidate HAR-U005 is natural05, exclusive before06; actual boundary/form inspected only after complete publication gates. Original witness bytes/edition/date caveats unchanged.


## HAR-U004 private verification retention

The designated metadata-only custodian retained `HAR-U004_PRIVATE_SOURCE_VERIFICATION_20261016_V1.zip` as private Drive file `1gI8P9xOwF6AK2Nb-ougj-sPqm53CRcnS`, canonical parent `1kP3-4QyvgbV9jVL84kI6Yj9Rww_otO_3`, shared=false. Full raw remote readback matches **2,389,948 bytes**, SHA-256 `2f5ddffd2994b91aab5b371e676782a9ea9d03662e72111b6afdc17e92f3121b`; safe paths, ZIP CRC, exact16object membership and every object's size/hash PASS. Manifest SHA-256 `1df3a3c911b2f0f66e5a93fb92d3ae9eb185d66bd26fb81e34eaf09cbb2449a7`. Only current faithful extraction/four actual panels/geometry/ruby/tenlocatorproof/scripts/tool hashes/factual gate provenance are retained. Interpretive locator descriptions, analytical frontiers, future prose, originals, binaries and caches are excluded. Original EPUB stays unchanged at its canonical ID. Retention is not publisher authentication.
