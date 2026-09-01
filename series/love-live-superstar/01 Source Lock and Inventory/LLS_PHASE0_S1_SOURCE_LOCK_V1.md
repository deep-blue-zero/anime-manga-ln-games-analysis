---
series: "Love Live! Superstar!!"
artifact_id: "LLS_PHASE0_S1_SOURCE_LOCK_V1"
artifact_type: "phase0_source_lock"
scope: "Season 1 episodes S01E01-S01E12"
status: "complete"
---

# Love Live! Superstar!! — Phase 0 Season 1 Source Lock

## Result

All 12 Season 1 episode bundles were downloaded through the authenticated Google Drive raw-file stream and audited locally.

- Expected bundles: **12**
- Downloaded bundles: **12**
- ZIP CRC passes: **12/12**
- SHA-256 hashes computed: **12/12**
- Bundles with exactly one complete audio file: **12/12**
- Bundles with corrected Japanese ASS: **12/12**
- Bundles with English full + spoken derivative ASS: **12/12**
- Bundles with required manifests/indexes: **12/12**

## Per-episode lock table

| Episode | Bytes | SHA-256 | CRC | Duration | JA cues | Frames | Contact sheets | Schema | OP/ED dedup metadata |
|---|---:|---|---|---:|---:|---:|---:|---|---|
| S01E01 | 179,969,324 | `fc0efe0e3986a8b6472d426299de29285e4eef7654487957f07a64f869887d41` | PASS | 1423.126s | 400 | 832 | 42 | `1` | no |
| S01E02 | 182,490,649 | `7a9c2613d6eef2aa6190ee81d7b6392ced4c62f0d68d5c6d95e8852dd13d5d91` | PASS | 1422.101s | 437 | 836 | 42 | `1` | no |
| S01E03 | 187,403,713 | `f0cfbcf201be8e566676df5c99e6dc297aedec367e2676f1807f06270669b3a4` | PASS | 1423.090s | 397 | 911 | 46 | `1` | no |
| S01E04 | 156,091,741 | `fb4ddda572eeb06b6b37f5e8a4df0969fe3bd48373693da6bfd7c9ab95cfbbc2` | PASS | 1422.101s | 400 | 726 | 42 | `1` | yes |
| S01E05 | 144,116,532 | `f3ac759c0fa45844efe8c3c752db9c795e3395789d57822c279480e2920ef51f` | PASS | 1423.090s | 443 | 638 | 39 | `1` | yes |
| S01E06 | 155,091,870 | `e6e1d53f5f6cdd7a1a522572cce709b7651d0f24c221d23ed32c9b6a55bd076a` | PASS | 1422.123s | 401 | 718 | 43 | `1` | yes |
| S01E07 | 152,125,835 | `b8a243547635b800308d3c106624906f05b0f19c10a4509b4b221fe5ca71afd8` | PASS | 1423.090s | 446 | 728 | 45 | `2` | yes |
| S01E08 | 158,860,172 | `7d7688e520d0199d963d399d297cdef020cdf7650762238a395ac9cce8937f82` | PASS | 1422.088s | 404 | 738 | 42 | `2` | yes |
| S01E09 | 161,494,635 | `942bc737e0cdb608aaea07440117782a39fa1a89fcaa7bc77560462ebac3c7c7` | PASS | 1423.090s | 459 | 772 | 45 | `2` | yes |
| S01E10 | 177,180,055 | `e9aecc9a0dca7f1c53c6cd530275ffbbe3025ebfd3c5b8febf82ccdd628a0d2b` | PASS | 1422.088s | 402 | 820 | 48 | `2` | yes |
| S01E11 | 144,192,696 | `02a694be9a805fbf0db2c3e49c4fd9cdaf9710dcbbf77ccdc817f42e07d3c973` | PASS | 1423.090s | 397 | 719 | 43 | `2` | yes |
| S01E12 | 182,483,968 | `8923e49be232cc6f82dfc754736cc54a8e6532a857291d11ae225576b3aa1832` | PASS | 1422.140s | 403 | 824 | 47 | `2` | yes |

## Component contract

For a bundle to be semantically eligible for the V2 sequential pass, Phase 0 requires:

- clean ZIP CRC;
- stable SHA-256 and exact byte size;
- `bundle_metadata.json` and `analysis_stats.json`;
- corrected Japanese ASS as the governing textual track;
- English full dialogue track and spoken-dialogue derivative as navigation/comparison aids;
- one complete episode-audio file;
- retained timestamped frames;
- contact sheets and `contact_sheets.json`;
- dialogue and scene indexes in CSV + JSON;
- manifest in CSV + JSON.

All Season 1 bundles satisfy this contract.

## Noted schema variation

`S01E01` does not contain the later `op_ed_deduplication` block in `bundle_metadata.json`; later tested Season 1 bundles do. This is recorded as a bundle-generation/schema-era variation, not a source-integrity failure, because the required primary evidence and indexes are present and CRC-clean.

## Sequential boundary

Phase 1 may begin with `S01E01`. Its semantic evidence boundary is `S01E01` only. No later episode content may be used to construct the canonical first-pass interpretation.
