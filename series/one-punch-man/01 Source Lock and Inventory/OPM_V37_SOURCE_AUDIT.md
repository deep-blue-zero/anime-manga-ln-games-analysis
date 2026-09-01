---
series: OPM
artifact_type: source_audit
scope: V37
generation: V2
status: canonical
source_boundary: Isolated Japanese tankobon V37 holding; V35-V36 absent; outside V01-V34 build manifest
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
created: 2026-08-24
---

# One Punch Man — V37 Isolated Source Audit

## Result

**PASS for direct archive identity and Japanese-source usability; NOT YET SEMANTICALLY SOURCE-LOCKED FOR SEQUENTIAL ANALYSIS.**

The primary-source directory contains `One Punch Man - Volume 37 [Japanese].cbz`, but V35-V36 are currently absent and V37 is not represented in the V01-V34 `build_manifest.json`. It is therefore governed as an isolated later holding rather than silently extending the contiguous analytical boundary.

## Direct archive identity

- Drive ID: `1qz_DhT4bTX5pvLcg-_WpAQ--68oOwF1F`
- Drive/archive bytes: 129,215,110
- archive images: 207
- SHA-256: `3e01ca4d5a3f7791df96b8cdb153707cd6995b22a01bcddfe373dc92578ef8b9`
- ZIP entries: 208 including the directory entry
- `ComicInfo.xml`: absent
- visual spot-check: Japanese contents/front matter identifies Volume 37 and chapter entries beginning with 189撃目

## Authority state

V37 is `present / direct_archive_checked / semantic_lock_pending`. No V37 narrative claims should enter the V2 sequential model before V35-V36 are supplied or the project explicitly authorizes a discontinuous prospective reading.

## Reconciliation rule

When V35-V36 arrive:

1. inventory and archive-audit them;
2. confirm the V37 object remains byte-identical to the SHA-256 above or document replacement;
3. extend the chapter/extra crosswalk through V35-V37 in order;
4. only then extend the continuous sequential reading boundary beyond V34.

This audit preserves the useful later source without allowing source availability to become chronology leakage.
