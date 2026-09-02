---
title: "Classroom of the Elite - Year 1 V2 Archival Lock"
series: COTE
artifact_type: archival_lock
scope: Y1
generation: V2
status: canonical
release_date: "2026-08-15"
source_boundary: "Japanese light novels Y1V01-Y1V11.5 + First File"
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
---

# COTE Year 1 V2 - Archival Lock

This document declares the packaged Year 1 V2 analytical corpus immutable once the outer ZIP and its SHA-256 sidecar are produced.

## Locked invariants

- Primary analytical boundary: Y1V01-Y1V11.5 plus *First File*.
- Canonical scene-evidence namespace: 1,419 stable records.
- Canonical exact-language namespace: `JY1-001-JY1-283`.
- Canonical Year 2 handoff namespace: `Y1H-001-Y1H-042`.
- Canonical entrypoint: `COTE_Y1_00_README_AND_CORPUS_MAP.md`.
- Canonical continuous synthesis: `COTE_Y1_FULL_SYNTHESIS.md`.
- No copyrighted Japanese primary-source binary is included.

## Mutation rule

The ZIP identified by the external `.zip.sha256` sidecar is immutable. Any correction, addition, renamed artifact, changed byte stream, or revised analysis requires a later release and a new archive hash. Historical releases remain provenance.

## Retrieval rule

`README -> full synthesis or topical specialist -> Y1_12 evidence -> Y1_13 exact Japanese when material -> deterministic primary-source locator`.
