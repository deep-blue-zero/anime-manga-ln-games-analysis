---
series: "Love Live! Superstar!!"
artifact_id: "LLS_PHASE0_S3_SOURCE_LOCK_V1"
artifact_type: "phase0_source_lock"
scope: "Season 3 episodes S03E01-S03E12"
status: "complete"
---

# Love Live! Superstar!! — Phase 0 Season 3 Source Lock

## Result

All 12 Season 3 episode bundles were downloaded through the authenticated Google Drive raw-file stream and audited locally.

- Expected bundles: **12**
- Downloaded bundles: **12**
- ZIP CRC passes: **12/12**
- SHA-256 hashes computed: **12/12**
- Bundles satisfying required primary-evidence component contract: **12/12**

## Per-episode lock table

| Episode | Bytes | SHA-256 | CRC | Duration | JA cues | JA format | Frames | Contact sheets | Schema |
|---|---:|---|---|---:|---:|---|---:|---:|---|
| S03E01 | 170,726,573 | `ba6e20dfeb26d973a4593fd46bdf1bcf2125d28afcc6c9d107de58ca61021cb3` | PASS | 1423.098s | 449 | `ass` | 802 | 41 | `2` |
| S03E02 | 174,251,003 | `fa246b0bb28c8c7d651902ff7ac34ae35767a54707187671305af15b45cab0c6` | PASS | 1422.098s | 454 | `ass` | 846 | 47 | `2` |
| S03E03 | 172,735,080 | `d764af25f9ce46c5ea9b7a05d027851e51089b2172ac9705ea9a3ad707ca985b` | PASS | 1423.098s | 453 | `ass` | 894 | 50 | `2` |
| S03E04 | 153,704,424 | `7aae6ed7c6cf3c8cb6ba096a1b21d002a3cf9ec72bb21a1bae54ba51a94808d3` | PASS | 1422.098s | 447 | `srt` | 707 | 40 | `2` |
| S03E05 | 160,766,094 | `e11f4e5389f90a002466808d1a06f7bff4da1e5368f1fb1f139a1c360344e39e` | PASS | 1423.098s | 459 | `ass` | 736 | 42 | `2` |
| S03E06 | 182,088,745 | `c89dc2d46214f021aafb508054147a930e3017687877b6669d9dc3d14d956e30` | PASS | 1422.098s | 378 | `srt` | 873 | 49 | `2` |
| S03E07 | 157,838,248 | `bd3843f006ee6de382ce0e32008710c79f83ad5391dfd4c3c28c761a7473af6b` | PASS | 1423.098s | 443 | `srt` | 719 | 41 | `2` |
| S03E08 | 165,059,864 | `dc985b4bcae1c85d6e15892c620fd56d104efeb79d9accb037549eacd826a8dd` | PASS | 1422.098s | 445 | `srt` | 830 | 46 | `2` |
| S03E09 | 162,739,046 | `8dd447b180ff37269f3df7681fcd112e2c0fed3aebe5ad4255f8e639b62fc71e` | PASS | 1423.098s | 466 | `srt` | 802 | 42 | `2` |
| S03E10 | 172,492,430 | `9ec7f0b22dc1c802b351a362c86665083271595b1f4b326d4e5c61d133d4bbc1` | PASS | 1422.098s | 438 | `srt` | 950 | 52 | `2` |
| S03E11 | 178,437,395 | `57cc79eb183b654045bbea2ca4c940f58f8ecbb1fcf5f4640b2705d8ed16468a` | PASS | 1423.098s | 417 | `srt` | 862 | 48 | `2` |
| S03E12 | 155,626,725 | `e9263ecb7cbb123f6eda89e695bed188101bc8fbd7936c0ec784a6b725e39bff` | PASS | 1422.098s | 393 | `ass` | 727 | 37 | `2` |

## Japanese subtitle packaging note

Corrected Japanese subtitles are present as SRT rather than ASS in: **S03E04, S03E06, S03E07, S03E08, S03E09, S03E10, S03E11**.

The `selected_subtitle` field correctly points to the retained SRT and the files contain valid timed Japanese dialogue. This is sufficient for wording/timing analysis, but ASS style metadata is not available for those episodes.

For **S03E04, S03E06, S03E07, S03E08, S03E09, S03E10, S03E11**, `subtitle_info.json` also retains a stale `language_tracks.japanese_corrected` / `comparison_pairing.primary` filename ending in `.ass` even though the actual selected and retained source is `.srt`. This is a metadata inconsistency, not missing Japanese dialogue.

## Eligibility

All Season 3 bundles are source-eligible for their future sealed sequential readings. Any subtitle-format caveats above must be preserved in episode provenance.
