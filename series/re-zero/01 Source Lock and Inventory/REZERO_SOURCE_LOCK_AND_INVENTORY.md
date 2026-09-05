---
series: RE_ZERO
artifact_type: source_lock
scope: SOURCE_ADMISSION_CONTRACT_AND_CURRENT_INVENTORY_STATE
generation: V0.2
status: canonical
release_state: mutable_active
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
---

# Re:Zero — source lock and inventory

## Current lock state

**PARTIALLY LOCKED — ACQUIRED JAPANESE MAIN-LN SPINE V01-V43.**

The governed Drive evidence folder contains a continuous, integrity-audited Japanese main-light-novel sequence from Volume 01 through Volume 43. Those 43 objects are admitted as `MAIN_LN` witnesses.

This is **not a claim that the acquired corpus is current-complete**. A bibliographic freshness check on 2026-09-04 against official KADOKAWA/Re:Zero publication surfaces establishes that Volume 44 was released on 2026-03-25 and Volume 45 on 2026-06-25. Neither appears in the audited 2026-08-31 Drive manifest. The known current main-spine acquisition gaps are therefore **V44 and V45**.

The gap does **not** block a prospective Volume 01 reading. It prohibits describing the present acquisition as a complete-to-date Re:Zero main-light-novel corpus.

## Authority responsibility

This file owns the Git-side record of **which Re:Zero source witnesses are admitted for analysis and what each witness is allowed to support**.

Primary-source binaries, extracted prose, and detailed per-object audit data remain in the governed evidence plane. Git records the current admission decision, deterministic source identifiers, provenance anchors, integrity summary, known gaps, and analytical horizons.

The detailed per-file SHA-256 values remain authoritative in the Drive audit manifest identified below. Duplicating that entire machine inventory in this mutable analytical file would create two competing audit surfaces.

## Governed evidence anchors

- Primary-source Drive root: `1tNJvglC-ri_AEGTkJupZ78WddyiCqQMy`
- Re:Zero evidence folder: `14WoHQWhJ4rCtvLrrZpiwVXgnSJh37YOo`
- Drive audit manifest file: `16-fjuvDSqFGRdSoOE-WJy3uFBRwCYmgK`
- Manifest title: `audit_manifest.json`
- Manifest audit date: `2026-08-31`
- Manifest size: `23,584` bytes
- Manifest SHA-256 as retrieved for this admission audit: `3daa190cefda6ab894f5d62ff547a93856c8133f2d4fc1cbc552b99d73c73314`

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

The manifest states that the packaging warnings are non-fatal and that affected books remain readable after CRC/container validation.

## Admitted main-light-novel set

The following range admission is deterministic and exhaustive for the current Japanese main-LN lock:

- source IDs: `RZ-MAIN-LN-JA-V01` through `RZ-MAIN-LN-JA-V43`;
- witness class: `MAIN_LN`;
- language: `ja`;
- folder-relative locators: `Re Zero - Volume 01.epub` through `Re Zero - Volume 43.epub`;
- integrity: exact per-file SHA-256 plus CRC/container audit in the anchored Drive manifest;
- arc: `UNASSIGNED_PENDING_SOURCE_VERIFICATION`;
- publication dates: not supplied by the local audit manifest and not globally backfilled from memory;
- horizon: V01=`START`; each VNN after the frozen prospective analysis of VNN-1.

This ranged admission is allowed because the manifest explicitly enumerates all 43 objects, hashes each one, reports no missing volume in the range, and records one primary Japanese edition per numbered volume. Any future changed hash, replacement file, revised edition, or gap invalidates the range assumption until re-audited.

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

## Current source-state summary

- **Acquired/admitted Japanese main LN:** V01-V43 continuous.
- **Known published but not acquired/admitted main LN:** V44-V45.
- **Admitted translations:** none.
- **Retained non-admitted translation:** English V21.
- **Admitted supplemental/EX/short-story:** none.
- **Admitted IF/alternate route:** none.
- **Admitted web novel:** none.
- **Admitted anime/audiovisual:** none.
- **Next source acquisition priority:** Japanese V44 and V45 before the sequential read reaches that boundary.
- **Next analytical operation permitted now:** Japanese V01 deep reading.
