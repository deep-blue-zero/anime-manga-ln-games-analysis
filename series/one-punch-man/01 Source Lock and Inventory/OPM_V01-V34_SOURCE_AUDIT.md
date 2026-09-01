---
series: OPM
artifact_type: source_audit
scope: "Japanese tankobon V01-V34"
generation: V2
status: canonical
source_boundary: "Current Drive tankobon corpus V01-V34; official web folder excluded"
supersedes: null
superseded_by: null
do_not_use_as_current_authority: false
created: 2026-08-24
---

# One Punch Man — V01-V34 Source Audit

## Result

**PASS for archive-level Phase 0 readiness.** The Drive tankobon directory contains a contiguous V01-V34 Japanese-labeled CBZ set and `build_manifest.json`. The manifest reports `ok: true` and gives a unique SHA-256, byte count, and page count for each volume.

This audit authorizes sequential analysis to begin at V01 without waiting for later volumes. Its scope is specifically the V01-V34 build-manifested set and should not be read as a statement about later holdings.

## Integrity findings

- volumes: 34 (V01-V34 contiguous)
- source pages before duplicate removal: 7319
- archived pages: 7316
- exact duplicates removed: 3
- retained near-duplicate pairs: 0
- official web serialization files currently present: 0

### Duplicate-removal provenance

- V24: 221 source pages -> 220 archived pages; 1 exact duplicate removed.
- V27: 201 source pages -> 200 archived pages; 1 exact duplicate removed.
- V28: 217 source pages -> 216 archived pages; 1 exact duplicate removed.


No other volume reports source/archive page-count divergence.

## V01 direct spot-check

The V01 Drive object was separately downloaded and inspected:

- Drive ID: `1vH1iaEnUDNoncZGNZ6LubGl7oXRtCLqr`
- archive: `One Punch Man - Volume 01 [Japanese].cbz`
- manifest images: 206
- archive listing images: 206
- manifest bytes: 60,853,526
- Drive bytes: 60,853,526
- manifest SHA-256: `be3a749342e6c617ce0b9e55ed353ca5874c70df4f0467c27daf5b5215b7b3a0`

V01 therefore has no detected archive-identity mismatch and may proceed to semantic source lock/deep reading.

## Lock model

### Layer A — archive-integrity lock
Complete for V01-V34 from the build manifest and directory inspection.

### Layer B — semantic source lock
Completed per volume immediately before/during first deep reading:

- confirm readable page/image order;
- confirm Japanese source usability;
- map chapters, covers, title pages, extras, bonus manga, and advertisements/paratext where analytically relevant;
- record printed pagination where usable;
- record anomalies;
- preserve deterministic image locators.

This two-layer model prevents Phase 0 from pretending that filesystem verification alone is a close reading while still allowing the project to begin now.

## Open source gaps

1. V35-V36 are currently absent from the tankobon folder.
2. V37 is present but outside this V01-V34 build-manifest audit; see `OPM_V37_SOURCE_AUDIT.md`.
3. `02 Official Web Serialization` is empty.
4. Chapter/extra crosswalk beyond volumes already semantically opened remains pending incremental validation.

These are **open acquisition/mapping gaps**, not blockers for V01-V34 sequential analysis.

## Post-audit directory discovery

After this scoped V01-V34 audit was completed, a fresh directory listing identified an isolated `One Punch Man - Volume 37 [Japanese].cbz` (Drive ID `1qz_DhT4bTX5pvLcg-_WpAQ--68oOwF1F`). V35-V36 remain absent. This does **not** invalidate the V01-V34 audit because V37 is not represented in `build_manifest.json`; it is governed by a separate direct archive audit until the sequence gap is filled.

## Decision

Proceed to `OPM_V01_DEEP_READING.md` against the fixed V01 archive. Append later volumes and official web material when supplied; do not create a new generation or parallel root merely because the source boundary expands.
