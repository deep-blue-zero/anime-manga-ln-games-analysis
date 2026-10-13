---
title: "Medalist — V01 Authorization and Delivered-Source Receipt"
artifact_id: "MEDALIST_V01_AUTHORIZATION_AND_SOURCE_RECEIPT"
artifact_type: "source_admission_authorization_receipt"
series: "Medalist / メダリスト"
series_id: "medalist"
generation: "MEDALIST_BOOTSTRAP_V1"
version: "1.0"
status: "canonical"
scope: "Owner foundation approval, single-operation V01 admission and entering state"
canonical_home: "series/medalist/07 Audits and Handoffs/MEDALIST_V01_AUTHORIZATION_AND_SOURCE_RECEIPT.md"
source_boundary: "Japanese delivered V01 witness; no completed reading at activation"
created: "2026-10-12"
review_status: "OWNER_APPROVED_FOUNDATION_AND_AUTHORIZED_V01"
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
do_not_use_as_literary_evidence: true
---

# V01 authorization and source receipt

This is the activation snapshot, not a reading-completion receipt. The owner explicitly stated: **I approve the revised foundation. Begin analysis/deep reading of Volume 1.** The approved design is the version-0.2 foundation at `4e287a1208265707bbab22037da5a405e7cd9631`. Local pre-activation reconciliation is `d12fb3ceab5df79da797e53f2d401311971d02ed`, preserving that complete Medalist tree while importing current main `ae6517f6213f3f362fb6fea99023969f3a69995e`. Approval does not imply a manga finding or authorize V02, either fanbook, English translation or adaptation.

After automatic approval review required direct chat confirmation of the persistent activation, the owner answered **Approve V01 activation and reading** to the explicit request to record foundation approval, open V01 only, admit its verified source and complete/publish its reading and ledger updates on `series/medalist`. This is the trusted confirmation for applying this receipt and the proposed activation. The prior rejected command applied no repository changes.

The [entrypoint](../CURRENT_STATE_AND_CORPUS_MAP.md) records canonical current methods/architecture, seven initialized ledger schemas, OPEN initiation gate, `single_operation`, authorized start and terminal operation V01, ACTIVE run and null completed high-water mark. Entering claims, character states, relationship states, sport results and predictions are empty. There are zero closed readings. The continuing project itself is not declared terminal or a finished-series release.

## Exact delivered source and checks

- Source key: `MD-MG-JP-TB-V001-W01`; local route: `MD-LOCAL-001`.
- Filename: `Medalist - Volume 01 [Japanese].cbz`; 130,779,405 bytes; SHA-256 `df9a4c1c4fd3cb04313e42af5a26781e96c74652e315bbfda6b7d9a7d68ba0fe`.
- 293 sequential image entries, `0001.jpg` through `0293.jpg`, plus generated ComicInfo.xml. Full ZIP CRC, every pixel decode and every image hash/order were independently checked against the retained build page map. Source-page bytes are preserved. The full locator manifest's normalized SHA-256 is `94d23e14e6d77b8e85c75b478ba19d67d292bb9332c121f30a756a44eaeb6ec6`.
- The cover identifies Japanese Medalist Volume 1 by つるまいかだ and AFTERNOON KC; `0004.jpg` identifies Score 1, 氷上の天才. Exact printing, colophon, complete chapter map and printed pagination are pending direct volume mapping. The wrapper ComicInfo is packaging metadata rather than publisher proof.
- Candidate admitted material: original images 0001–0233, with primary story and the volume's own extras/paratext independently classified during the complete transaction. Image 0234 directly confirms an unrelated Wandance trial-chapter title page. Images 0234–0293 are excluded from Medalist evidence; no preview-body reading occurred.
- Locator version: `medalist-cbz-image-occurrence-v1`; one-based original ZIP image index/entry + verified Score/component + panel/balloon when needed. A wide padded cover is not treated as a narrative spread. Digital image indices are not printed pages by assumption.

## Actual capability and exposure

Local full-resolution images were delivered through the image-inspection tool and their Japanese lettering was readable. No OCR-only reading is claimed. Compression softness and non-authorial watermark overlays remain limits; uncertain small text gets original-resolution crop/reinspection and is not guessed.

Structural verification displayed cover 0001, blank 0002, opening prologue/Score-title images 0003–0004, jacket gag images 0232–0233 and excluded preview title 0234. The narrative opening and gags were therefore incidentally visible before the OPEN record. This is disclosed prior exposure, not a blind-reader claim, complete reading or a retroactively invented earlier prediction. The primary chronological pass continues from the opening after activation and reinspects those pages in context.

Earlier publisher reconnaissance also exposed later synopsis snippets; no detail from them is admitted as V01 evidence. Model familiarity cannot certify ignorance of later franchise information. Interpretive claims must be supported by the actually inspected V01 witness and bounded to V01.

## Persistence and completion contract

The raw archive, original-image inspection copies and full byte/locator/coverage notes remain in the title evidence workspace, outside analytical Git. Only sanitized source identity, hashes, method/limitations and interpretive results enter Git. The activation commit is externally recovered from Git history; this receipt does not claim its own SHA or future CI outcome.

The remaining V01 operation must inspect every admitted component, establish the full chapter/component map, write `02 Sequential Readings/MEDALIST_V01_DEEP_READING.md`, update every materially affected ledger, freeze `MD-FR-V01`, update source/entrypoint progress and complete required staged validation and exact-head publication audits. An actual partial inspection cannot advance the completed boundary. V02 remains a candidate requiring separate authorization after V01 closes.
