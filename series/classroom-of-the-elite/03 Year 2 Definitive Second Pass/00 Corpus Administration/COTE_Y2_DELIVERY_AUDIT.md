---
series: COTE
artifact_type: delivery_audit
scope: Y2
generation: V2
status: canonical
authority_state: canonical
source_boundary: Y2SL
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
---

# Year 2 V2 delivery audit

**PASS — local content, preservation and package checks.** Release state: `frozen`. Remote publication verification is recorded separately for the exact branch head; this report does not claim CI success before it has been observed.

- 167 core artifacts; 172 total package members, including release envelopes.
- Seventeen source-local artifacts match the starting boundary byte-for-byte.
- Seventeen source identities; 2,697 preserved evidence IDs; 43 Japanese retrieval entries; 23 calibrated protocol cases.
- Thirteen specialist/index slots and the full synthesis are canonical through Y2SL.
- UTF-8, YAML/JSON, declared package membership, 614 internal file links and 4 heading anchors pass.
- No new long verbatim analytical-paragraph duplication, forbidden placeholder or chat wrapper was found. 0 pre-existing long-repetition groups are preserved and individually identified in the machine audit.
- No primary-source binaries, Year-3 narrative analysis, extracted artwork, raw chapter exports or private work files are included.

## What the checks establish

The source checksum inventory records the identities independently verified from the external EPUBs during closeout. The evidence-router generator checks paragraph/resource bounds, source hashes and canonical locator conventions when supplied those sources; the release generator operates on analytical artifacts only. Structural locator validation does not claim that every interpretive assertion has been independently reread anew. The Japanese index's 52 short excerpts were directly verified against the locked primary sources, retaining speaker/narrator ownership and local ambiguity.

The protocol audit preserves support, determinacy, reconstruction permission and voice permission as distinct gates. All inherited question states remain intact, and the twelve new Y2H tests remain unanswered. The current correction routes cover the younger-cohort points table, V01 pictured companion and transfer destination. Earlier source-local readings and the Year-1 foundation retain their historical authority.

## Reproduction and final publication

Run [generate_y2_release.py](../04%20Source%20Maps%20and%20Support/generate_y2_release.py) with `--check` to compare all six generated outputs exactly. Its `--package PATH` option writes a deterministic ZIP and detached SHA-256, then verifies each member. The artifact checksum file covers every member except itself; the detached hash closes that remaining dependency.

The exact remote commit, changed-blob readback, current-main ancestry, completed housekeeping and successful Repository integration audit must all be verified before final release eligibility. The stable branch remains separate from main unless integration is separately authorized. See the [archival-lock record](COTE_Y2_V2_ARCHIVAL_LOCK.md), [machine audit](COTE_Y2_V2_FINAL_DELIVERY_AUDIT.json), [manifest](COTE_Y2_CORPUS_MANIFEST.md) and [README](../05%20Year-Level%20Synthesis/COTE_Y2_00_README_AND_CORPUS_MAP.md).
