---
title: "Classroom of the Elite — Year 2 V2 Archival Lock"
series: COTE
artifact_type: archival_lock
scope: Y2
generation: V2
status: active_provisional
authority_state: active_provisional
source_boundary: Y2SL
release_state: prepared_for_publication
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
updated_at: "2026-09-09"
---

# Year 2 V2 archival lock

The analytical corpus is complete through Second List. This prepared release binds the seventeen source-local records, nineteen rolling-ledger files (seventeen topical/current-state roles, the Volume-0 revision ledger and the inherited-question tracker), thirteen specialist/index slots, full synthesis, audited reconstruction protocol and release infrastructure. The source-local records remain byte-identical to the verified starting boundary.

## Publication gate

Release preparation is complete; final freezing and the existing `year3_unlock` state in the [README](../05%20Year-Level%20Synthesis/COTE_Y2_00_README_AND_CORPUS_MAP.md#201-active-state) remain conditional on successful publication and exact remote verification. A local manifest or passing author preflight alone does not establish integration readiness. The final remote head must pass Repository integration audit after housekeeping and current-main reconciliation. The release receipt records that exact head outside the committed corpus to avoid a self-referential commit hash.

Year-3 narrative evidence is absent. Eligibility to open the later gate never means that this task has started Year 3. After verified closure, the next permitted analytical operation belongs to a later execution: bootstrap and sequential analysis from Y3V01 under COTE_Y3_ANALYTICAL_METHOD_V2.md.

## Immutable content and correction policy

The clean archive contains analytical documents, retrieval data, governing methods and reproducibility tools, with the unchanged Year-1 foundation needed for historical reference. It contains no novels, guidebook binary, extracted illustrations, raw chapter dumps, private working audits, runtime environment or Git internals. Historical Year-1 manifests and Drive fingerprints describe their original releases; the Year-2 artifact checksum file owns the actual bytes included here.

After final freezing, a correction requires an explicit later revision and new archive fingerprint. Do not silently replace the immutable ZIP under the same recorded SHA-256. An original source-local misidentification remains visible with a current correction overlay rather than a rewritten epistemic record. The cohort, V01 illustration and transfer-destination corrections are routed in Y2_10 and Y2_12.

## Checksum topology and reproducibility

[COTE_Y2_CORPUS_MANIFEST.md](COTE_Y2_CORPUS_MANIFEST.md) and [COTE_Y2_CORPUS_INDEX.json](COTE_Y2_CORPUS_INDEX.json) enumerate the core artifacts with type, boundary, status, words, bytes, SHA-256, supersession and primary-home subject. [COTE_Y2_SOURCE_CHECKSUMS.sha256](COTE_Y2_SOURCE_CHECKSUMS.sha256) lists the seventeen external source identities; those source files are excluded.

The generated manifest, index and delivery-audit envelopes do not recursively hash themselves. [COTE_Y2_ARTIFACT_CHECKSUMS.sha256](COTE_Y2_ARTIFACT_CHECKSUMS.sha256) covers every package member except itself, including those envelopes. A detached ZIP SHA-256 covers the final whole archive, including the checksum file. The final publication receipt binds the commit, remote blob readback, CI and archive fingerprint.

The designated generator is [generate_y2_release.py](../04%20Source%20Maps%20and%20Support/generate_y2_release.py), with reviewed [release specification](../04%20Source%20Maps%20and%20Support/COTE_Y2_RELEASE_SPEC.json). Run it from a repository checkout with Python and PyYAML, using `--check` for byte-exact regeneration validation or `--package PATH` for the reproducible archive. The separate evidence-router generator verifies original EPUBs when supplied the external source directory. Generated files are never edited by hand.
