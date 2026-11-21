---
title: "FX Fighter Kurumi-chan — Source Register"
artifact_id: FX_KURUMI_SOURCE_REGISTER
artifact_type: source_register
series: fx-fighter-kurumi-chan
version: "1.1"
status: canonical
authority_generation: FX_KURUMI-INITIAL
authority_scope: "Bibliographic identity, witnessed reconnaissance and candidate corpus admission"
source_boundary: "Witnesses FXK-JP-V01-W01 to FXK-JP-V10-W01 verified for run FXK-RUN-20261119-V01-V10; each admitted only at its own frontier"
created: 2026-11-15
last_updated: 2026-11-19
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
do_not_use_as_literary_evidence: true
---

# FX Fighter Kurumi-chan — Source Register

## Identity and candidate range

KADOKAWA’s MF Comics Flapper releases identify **FX戦士くるみちゃん** with original story by Demunyan (でむにゃん) and manga by Tansan Daisuki (炭酸だいすき). The collected manga defines the candidate lane; publisher copy gives bibliographic context and the opening focus on a student and foreign-exchange trading. [KADOKAWA V01](https://www.kadokawa.co.jp/product/322104000251/), [KADOKAWA V10](https://www.kadokawa.co.jp/product/322605000254/).

| Candidate group | Ingest history | Admission |
| --- | --- | --- |
| Japanese manga V01–V09 | Nine existing EPUB candidates retained with standardized inventory names; exact editions pending | NONE |
| Japanese manga V10 | One Japanese publisher EPUB candidate added from the Calibre import | NONE |

The November 15 metadata reconciliation matched all ten numbered live candidates and their folder placement and file sizes to local layout receipts. The retained source audit and its ten-record manifest cover V01–V10, including V10. The audit reports a per-volume sample of visible Japanese pages, inspection of package, spine and resource structure, and distinct ordered image hashes. The November 15 import record for V10 reports ZIP CRC, container and mimetype checks, spine and resource parsing and SHA-256 match to the corresponding Calibre bytes. No full EPUBCheck run was reported. These are attributed preparation results; the reconciliation did not reread or rehash the live EPUBs. Sampled pages and distinct images do not establish verified reading order, legibility, missing-page status, or completeness of main and supplemental components. Only V10 has the new Calibre ingest lineage. The prior structural and sampled-page observations are attributed to that audit’s own boundary.

## Verify before admitting

Record edition, stable opaque witness, original and derived byte relationship and deterministic location binding in controlled storage. Check ordered spine/image positions, missing or duplicate occurrences, spreads and page labels. Classify covers, apparatus, main narrative, extras and previews before exposing analysts. Test the actual still-image inspection lane against both normal panels and dense inset figures. Source IDs, raw filenames, acquisition and mapping records, image bytes and OCR artifacts remain in the source or working plane. Report unreadable or unresolved numeric details separately from package integrity.

Web serial versions, other-language editions, adaptations and supplemental components have separate identity and scope. Any later comparison needs aligned loci and preserved variant evidence. An owner-authorized collected-manga run must give a start/terminal boundary and component scope even when more inventory exists. Approval of this foundation authorizes preparatory routing only.

## Run activation verification

On November 19, 2026, for run FXK-RUN-20261119-V01-V10, the run coordinator opened the ten supplied Japanese EPUBs in place and rehashed every package. The private witness receipt pins each package digest, its internal OPF path and the ordered map from spine item to image member. It also holds the package metadata, the source location and the per-image digests. The opaque public witness keys are `FXK-JP-V01-W01` to `FXK-JP-V10-W01`.

Every package passed a ZIP CRC test and resolved its container to one OPF. Each spine item is a fixed-layout page document that references exactly one raster image, and every image in each package is referenced from the spine. No image digest repeats within a volume. All 1,686 occurrences decoded as RGB rasters. Every OPF declares right-to-left page progression. The packages fall into two lineages. V01 and V03–V05 carry a Kindle-unpack tool signature, 1350×1920 pages and ASIN identifiers. V02 and V06–V10 have a different publisher-package layout with 1441×2048 pages and carry both creators (でむにゃん, 炭酸だいすき). The lineage difference does not affect page order. Each volume's checkpoint records whether it affects legibility or apparatus.

| Witness | Package title | Spine items = image occurrences | Page raster | Lineage |
| --- | --- | ---: | --- | --- |
| FXK-JP-V01-W01 | FX戦士くるみちゃん　1 | 171 | 1350×1920 | Kindle unpack |
| FXK-JP-V02-W01 | FX戦士くるみちゃん　2 | 171 | 1441×2048 | Publisher package |
| FXK-JP-V03-W01 | FX戦士くるみちゃん　3 | 171 | 1350×1920 | Kindle unpack |
| FXK-JP-V04-W01 | FX戦士くるみちゃん　4 | 163 | 1350×1920 | Kindle unpack |
| FXK-JP-V05-W01 | FX戦士くるみちゃん　5 | 171 | 1350×1920 | Kindle unpack |
| FXK-JP-V06-W01 | FX戦士くるみちゃん　6 | 163 | 1441×2048 | Publisher package |
| FXK-JP-V07-W01 | FX戦士くるみちゃん　7 | 163 | 1441×2048 | Publisher package |
| FXK-JP-V08-W01 | FX戦士くるみちゃん　８ | 171 | 1441×2048 | Publisher package |
| FXK-JP-V09-W01 | FX戦士くるみちゃん　9 | 171 | 1441×2048 | Publisher package |
| FXK-JP-V10-W01 | FX戦士くるみちゃん　10 | 171 | 1441×2048 | Publisher package |

**Locators.** `iNNNN` is the one-based image occurrence in spine order, including covers and apparatus. It is the same number as the spine position, because every spine item carries one image. Panel and balloon numbers are assigned by the analyst in Japanese reading order: right to left, then top to bottom. `p.visible` is recorded only where a printed folio is visible. A double-page spread is cited as both occurrences joined, `iNNNN+iNNNN`.

**Inspection lane.** The pages carry no text layer, so wording is transcribed directly from the images. A full-resolution V01 page with Japanese lettering and furigana and a 2.5× Lanczos-enlarged crop of small type were both legible in the coordinator's `STILL_IMAGE` route. Enlarged crops are the route for every dense screen, chart or small numeral. OCR, where used at all, is a retrieval aid and never a quotation source.

**Exposure control.** Images for V02–V10 were extracted and decoded only by script. They are held in a sealed working directory and released to analysts only when their volume is admitted. Beyond the V01 probe, no page of any volume was displayed during activation. Page classification, reading-order confirmation, spread detection and legibility for each volume belong to that volume's transaction.

| Obligation | State |
| --- | --- |
| FXK-SO-001 package identity and integrity | Resolved for all ten witnesses |
| FXK-SO-002 ordered image map and duplicate check | Resolved structurally for all ten; visual order confirmed per volume at admission |
| FXK-SO-003 component classification (main, apparatus, extras, previews) | Per volume, at admission, under the entrypoint's component scope |
| FXK-SO-004 legibility of dense screens and small numerals | Per volume; each unresolved value is recorded in that reading |
| FXK-SO-005 edition bibliography beyond package metadata (printing, revision state) | Open. Package metadata only; the V02 and V06–V10 packages carry no publication date |
