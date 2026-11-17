---
series: CHIRAMUNE
artifact_type: reconciliation_audit
scope: V01_V02_ANALYSIS_BASELINE_PROMOTION
source_boundary: "Verified 16-file V01/V02 candidate package plus live Chiramune repository and 14-file local source inventory"
generation: V0.1
status: canonical
release_state: frozen_record
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
---

# Chiramune V01–V02 baseline reconciliation audit

## Input identity

Candidate package:

- filename: `CHIRAMUNE_V01_V02_ANALYSIS_HANDOFF.zip`;
- SHA-256: `27657108a21b1dd777a52f1588e32bae3b15d67d3452617799bf20aee8ccf19c`;
- package shape: 16 files under separate `V01/` and `V02/` roots;
- V01 source SHA-256: `440a634dac96f1a08ad698e1a6723dcf5075ff49ac8e2726be74c8ef50fce33d`;
- V02 source SHA-256: `521e764266f39d1f7be105711210badd6e0aba6d208878b5fe0d9961aeb7b056`.

The package hash exactly matched the handoff receipt before extraction.

## Current-state checks

- Upstream `series/chiramune` did not exist when the isolated branch was created.
- The branch began from then-current `origin/main` commit `2eec12ae1200d3aaaff3f754fd535808161226f8`.
- The existing registered Chiramune root contained bootstrap method, source lock, routers, and no substantive volume analysis.
- The live local source mirror contained exactly the 14 EPUB objects listed by the 2026-08-29 source lock.
- The local `audit_manifest.json` SHA-256 reproduced `e4d302d662997ae67be9368d45dd2dc7fefd5918f5c8540cbe82a897c00a8231`.
- Every EPUB SHA-256 reproduced the current source-lock value; no new holding or missing numbered main volume through V09 was observed.
- The official Shogakukan series catalog was rechecked on 2026-09-07 at `https://e-comi.shogakukan.co.jp/books/094532570000d0000000?page=1` and `?page=2`; it listed 14 releases through Volume 09.5 and no later numbered main volume.

The source bytes remain outside Git.

## Reconciliation decisions

### Preserved as distinct frozen records

The following four artifacts preserve independent prospective boundaries and were retained separately:

- `CHIRAMUNE_V01_DEEP_READING.md`;
- `CHIRAMUNE_V01_PROSPECTIVE_FREEZE.md`;
- `CHIRAMUNE_V02_DEEP_READING.md`;
- `CHIRAMUNE_V02_PROSPECTIVE_FREEZE.md`.

### Rolling ledger collisions

The V02 versions of the agency, self-authorship, and social-status ledgers contain the complete V01 body byte-for-byte after front matter, followed by a V02 update. Each V02 file is therefore the cumulative successor and becomes the single maintained repository ledger. Publishing both rolling copies would duplicate the V01 sections without creating a distinct current responsibility.

The V02 relationship ledger is newly justified by cross-volume directional intimacy and recognition state.

### Saku monograph collision

The V02 Saku file contains the complete V01 monograph body byte-for-byte after front matter, followed by its V02 longitudinal revision. It becomes the single maintained cumulative monograph. Its title, scope explanation, and V01 revision-target heading were corrected so the document no longer presents its current V01–V02 boundary as a V01-only artifact.

### Yuzuki monograph

The V02 corpus supplies direct focalization, multi-scene ordinary-life evidence, developmental history, crisis behavior, relationship contrast, counterevidence, and explicit abstention boundaries sufficient for an active-provisional monograph. No analogous monograph was created merely for cast symmetry.

### Metadata and ledger-integrity repairs

- Local-only publication markers were replaced with current-eligible repository authority metadata.
- Deep readings and freezes use `release_state: frozen_source_boundary`; rolling ledgers and monographs use `release_state: mutable_active`.
- Analytical status remains `active_provisional`; publication does not convert an ongoing-series interpretation into a final claim.
- The V02 self-authorship section's duplicate `SA-020` was renumbered contiguously as `SA-021` through `SA-033`, preserving the V01 `SA-020` identity.

### Local manifests

The two package manifests were not promoted as canonical repository manifests. They accurately record local unpublished candidate bytes, but those bytes and authority states changed during reconciliation, and their provenance responsibility is preserved here together with the package hash and semantic disposition. Publishing them unchanged would create stale authority and file-hash records.

## Architecture result

The baseline adds:

- an explicit open-ended full-series architecture;
- a dedicated rolling claim-revision ledger seeded with the V01→V02 transitions;
- a route separating current published-corpus synthesis from any eventual terminal full-series synthesis;
- explicit horizon tracking for publication, acquisition, main-volume analysis, supplemental analysis, and next safe reading;
- an atomic continuous-sequential contract for V03 onward;
- an adaptation/performance witness boundary subordinate to the Japanese novels.

## Publication boundary

The authored baseline is confined to `series/chiramune/`. No global routing output, character registry/index, authority record, migration crosswalk, source EPUB, or other series root is part of the authored change.

This audit records the reconciliation decision. Exact commit, remote head, and validation/CI state must be verified from Git and GitHub publication records; they are not predicted here.
