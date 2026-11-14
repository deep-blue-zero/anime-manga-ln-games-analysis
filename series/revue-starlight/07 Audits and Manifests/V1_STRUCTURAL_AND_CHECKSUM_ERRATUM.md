---
title: "Revue Starlight — V1 Structural and Checksum Erratum"
artifact_id: REVUE_STARLIGHT_V1_STRUCTURAL_AND_CHECKSUM_ERRATUM
artifact_type: erratum
series_id: revue-starlight
version: "1.0"
status: canonical
authority_scope: frozen_release_integrity_and_editorial_corrections
source_boundary: "TV01–TV12, OVA01–OVA03, and the complete 2021 sequel film, including credits and post-credit material"
canonical_home: "series/revue-starlight/07 Audits and Manifests/V1_STRUCTURAL_AND_CHECKSUM_ERRATUM.md"
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
---

# Revue Starlight — V1 Structural and Checksum Erratum

This record accompanies the [V1 release guide](../05%20Full-Series%20Synthesis/00_README_AND_CORPUS_MAP.md), [checksum list](FILE_CHECKSUMS.sha256), [integrity audit](CHECKSUM_AUDIT.md), and [V2 reconciliation](../06%20Evidence%20and%20Indexes/16_ANIME_AV_RECONCILIATION_V2.md). Line numbers refer to the V1 files at comparison commit `0bae19f328c3fdef82047e5753568fbb8478daed`, which have the same project bytes at the receiving `main` commit `73caf927b4ffe1c4a2ad1590d4d24b9a4a755e77`.

## Package checksum and Git history

The checksum list contains **23 named entries**. A byte-for-byte audit of the Git objects at the comparison point found **22 matches and one mismatch**, the V1 corpus guide. The baseline package digest agrees with the guide imported by `9957068cc942bdfbfb4f3fbd39c0c6aca13ed2ea`. The later routing edit `e9cdbd8f068f903cd7679a6003c9760f80f81e29` altered the guide's authority fields and governance reference. The release's recorded digest and the currently tracked digest therefore apply to different objects.

| V1 corpus guide object | SHA-256 |
| --- | --- |
| Release checksum and initial Git import | `497d68dcfb717f453ab04025751e975ef4325b99498bed18134deaee8e1cf41a` |
| Comparison and receiving Git snapshots | `495020d5a686d602454ec351918a88dfc13629c912cbe2de86776141ddbcd868` |

Use Git blob bytes for this comparison. A Windows checkout may differ when Git converts line endings. The original checksum list continues to identify the historical release payload.

## Numbering and overlap

The reported exact level-one-heading check concerns identical heading text. A recheck of the comparison tree's Markdown found zero identical level-one headings repeated within one file. The following are numbering collisions, gaps, and substantially overlapping material, which require a different check.

| Document | Reader correction |
| --- | --- |
| [04 — Maya and Claudine](../05%20Full-Series%20Synthesis/04_MAYA_CLAUDINE_RIVALRY_PERFECTION_AND_EXPOSURE.md) | After “XXXVII. Final synthesis” at line 915, numbering restarts at “XIV” at line 947 and reaches a second synthesis (“XXIII”) at line 1524. The tail through line 1643 mixes overlap with substantive material. Identify passages by heading text and line rather than by Roman numeral alone. |
| [05 — Mahiru, Futaba, and Kaoruko](../05%20Full-Series%20Synthesis/05_MAHIRU_FUTABA_KAORUKO_CARE_DEPENDENCE_AND_DIFFERENT_ROADS.md) | A second Appendix A starts at line 1690 after Appendix G at line 1659. Later sections include overlapping outcome audits and fresh material. Cite the appendix title together with its number. |
| [06 — 99th class ensemble](../05%20Full-Series%20Synthesis/06_SEISHO_99TH_CLASS_ENSEMBLE_AND_CHARACTER_ECOLOGY.md) | Appendix E at line 1519 is followed by Appendix L at line 1610. The numbering skips F through K. The contents of any intervening draft are unknown. |
| [15 — Dialogue, lyric, and motif index](../06%20Evidence%20and%20Indexes/15_JAPANESE_DIALOGUE_LYRIC_AND_MOTIF_INDEX.md) | Line 400 begins “XIII. Index-use principle”. Line 417 begins “XIII. Formal self-introductions and identity declarations”. Related address and motif tables recur. Cite the table and the scene locator. |

The original audit also records a pre-release correction of Document 10.

## Gemini packet corrections

- The named-entry audit above corrects CP18's statement that all 25 V1 checksums passed. The tracked V1 source inventory is a 119-line Markdown document headed “Scope” following the title and defines the governing media and source priority. CP18's metadata fields describe its proposed replacement.
- The CP16 source inventory and rehashed local witnesses agree. For TV01 the actual Japanese ASS digest is `06c35606770414ff4e4bde6225c6d853ba5f27c8eed992d0208cb6f9e78a8e4e`, as recorded by the inventory. Use it in place of the alternate value in the frozen reading header. The [V2 witness supplement](../01%20Source%20Lock%20and%20Inventory/SOURCE_WITNESS_SUPPLEMENT_V2.md) supplies the corrected full identity table.
- CP18 retracts two assertions from CP17A about TV05. The [Day 4 bouts](../06%20Evidence%20and%20Indexes/16_ANIME_AV_RECONCILIATION_V2.md#tv05--day-4-bouts) and [language and music](../06%20Evidence%20and%20Indexes/16_ANIME_AV_RECONCILIATION_V2.md#language-and-music) decisions record the action and voice distinctions and correct CP18's transposed pairings. [TV08](../06%20Evidence%20and%20Indexes/16_ANIME_AV_RECONCILIATION_V2.md#tv08--the-weight-of-hikaris-loss) and [film framing and Position Zero](../06%20Evidence%20and%20Indexes/16_ANIME_AV_RECONCILIATION_V2.md#film-framing-and-position-zero) record locator differences found during the receiver's source checks.
