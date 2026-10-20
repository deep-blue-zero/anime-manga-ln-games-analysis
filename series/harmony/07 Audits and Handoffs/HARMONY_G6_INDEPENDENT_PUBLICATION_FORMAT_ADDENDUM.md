---
title: Harmony — independent final publication-format review
artifact_id: HARMONY_G6_INDEPENDENT_PUBLICATION_FORMAT_ADDENDUM
artifact_type: independent_review
series_id: harmony
generation: HARMONY_BOOTSTRAP_V1
version: '1.0'
status: active_provisional
scope: Exact payload preservation and publication-only format reconciliation
source_boundary: HAR-JP-EPUB-001 through HAR-U020; no new source
canonical_home: series/harmony/07 Audits and Handoffs/HARMONY_G6_INDEPENDENT_PUBLICATION_FORMAT_ADDENDUM.md
created: '2026-10-19'
review_status: INDEPENDENT_ACCEPTED_NO_SUBSTANTIVE_CHANGE
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
do_not_use_as_literary_evidence: true
---

# Harmony G6 independent publication-format addendum

Decision: **ACCEPT the publication derivatives.** The independent substantive acceptance remains unchanged. This addendum reviews the publication-format transition after the original final review; it does not rewrite that review or certify a future Git transaction.

I independently recovered all **16 complete UTF-8 beforeimages** from `HARMONY_PREPUBLICATION_REVIEW_PAYLOADS.json`, checked their declared byte lengths and SHA-256 values, computed physical CRLF-to-LF conversion, and compared every selected publication file to the exact recorded transformation. Fourteen files contain physical line-ending conversions; eleven JSON exports parse to exactly the same values. Escaped CR/LF characters inside JSON strings remain intact. The nonfrozen context-export helper has only the recorded line-ending change, with an identical parsed Python syntax tree.

The G4 synthesis is an **exact LF-only derivative**, with no added technical notice or analytical change: original SHA-256 `883eb143c012ab7c431de6946c567d90eedab6009d435a821874b68e9d045e75`; publication SHA-256 `24fc29b1ce66f46b8d1708f3ea171744a3f6e57473503baba8595a274767dbcd`. The earlier mistaken relative link was removed with that proposed notice. Its receiving review and G5 validation each preserve their complete prior file as an unchanged prefix and add only the archived factual identity notice. Both complete beforeimages and exact appended strings are retained.

The G6 adoption wrapper explicitly describes LF publication and distinguishes the prior inspection from the published derivative. Its only other recorded change replaces the former “adopted unchanged” wording. I verified that the complete original independent body remains recoverable, and that the current audit contains exactly one complete copy of its LF derivative with no other body edit:

| G6 body identity | SHA-256 |
| --- | --- |
| Original 36,593-byte body, 181 physical CRLF pairs | `f7c2433fa59ad23a1f84cde3da7261c4addf4c41b1c1902db3c3e1248bd02de2` |
| LF 36,412-byte body | `f001bbe7c529d4a25329080c095d9ddf8c51a784a4e55dcfee29b82fa9cf3b27` |

The original 91-file reviewed-candidate manifest remains a historical inspection record. All thirteen changed files from that set are individually accounted for by the publication archive/map; the other 78 hashes remain equal. Original/current models, protocols, freezes, suites, runtime prompts/events/responses, source records and the twenty frozen readings are unchanged. No judgment value, failed output, source citation or model instruction was altered. I also verified every file in the regenerated Interactive packet hash list and its complete directory coverage.

The inspected archive SHA-256 is `c44d137c863a9ccf886ccb2540260ee996d7c6c993b8e6645ea72c2884619375`. The inspected format-reconciliation SHA-256 is `9e930518007410d5962aa825aaa20c87bfd235b0699526d483dbd3aed6af064d`. The independent verification receipt, `HARMONY_G6_INDEPENDENT_PUBLICATION_FORMAT_REVIEW.json`, records each original, normalized and selected publication hash and the exact wrapper/append comparisons. Its SHA-256 is `f13760c841971bd4b3d7b6931716680ebca628469af4a23e68170cbecbd974d9`.

Historical hashes in the original reviews and handoff continue to identify their exact preserved inspection inputs; they are not asserted to hash later LF derivatives. Root may update only the reconciliation's independent-review status/pointer to this completed receipt, which creates a new metadata identity without changing the mapped payloads. The original substantive review body remains unchanged outside Git. Protected-main integration and the explicit audit of the actual resulting main remain separate pending release responsibilities.
