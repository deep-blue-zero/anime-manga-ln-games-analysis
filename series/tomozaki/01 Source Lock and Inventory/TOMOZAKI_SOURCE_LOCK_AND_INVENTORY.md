---
series: TOMOZAKI
artifact_type: source_lock_and_inventory
scope: JP_LIGHT_NOVEL_EPUB_CORPUS
source_audit_date: 2026-08-29
generation: V0.1
status: canonical
release_state: mutable_active
---

# Bottom-Tier Character Tomozaki — source lock and inventory

## 1. Responsibility

This file defines the exact primary-source boundary for the initial Git-native Tomozaki analytical project. It is a source-routing and integrity artifact, not literary analysis.

If later source material is acquired, revise or supersede this lock explicitly. Do not silently treat adaptations, translations, later volumes, bonuses, interviews, remembered canon, or other witnesses as though they were present in the 2026-08-29 audit.

## 2. Canonical source locations

Primary-source Drive root: `1tNJvglC-ri_AEGTkJupZ78WddyiCqQMy`  
Series source folder: `1YldXgz3sglS1CLD_CvUieUM_GOr-VElg` (`Tomozaki`)  
Audit manifest file ID: `1W9CwbimSf5y1g59MMod1z5nybFyVXXtc` (`audit_manifest.json`)  
Audit manifest SHA-256: `64e5e9e722a24f578abc20b3de1b61269c1212e224b60786e7eab28d35b66257`  
Audit date: `2026-08-29`

The audit identifies the series as:

- English title: *Bottom-Tier Character Tomozaki*
- Japanese title: `弱キャラ友崎くん`
- author metadata: Yuki Yaku / 屋久ユウキ
- normalized filename convention: `Bottom-Tier Character Tomozaki - Volume NN[.5][ - Edition].epub`

The normalized English filename is an inventory label only. Source semantics remain Japanese.

## 3. Inventory lock

| Class | Count / state |
|---|---:|
| EPUB objects | 13 |
| Numbered main volumes | 11 |
| Main range | V01-V11 |
| Gaps inside numbered main range | none |
| Side-story volumes | V06.5, V08.5 |
| Special-edition witnesses | 1 (V07) |
| Exact duplicate groups | 0 |
| ZIP CRC checks passed | 13 / 13 |
| EPUB container checks passed | 13 / 13 |
| Packaging-conformant | 11 |
| Packaging warnings | 2 |

The audit manifest is the canonical per-file checksum, old-name/new-name, embedded-metadata, and packaging ledger. This Git file deliberately does **not** duplicate all 13 SHA-256 rows because that would create a second checksum ledger with no independent responsibility.

## 4. Locked EPUB witnesses

| Volume | Normalized filename | Drive file ID | Audit packaging state |
|---|---|---|---|
| V01 | `Bottom-Tier Character Tomozaki - Volume 01.epub` | `1B7r3rf0bIZ1gnFg88NTeDa5K6C4LVlF0` | conformant |
| V02 | `Bottom-Tier Character Tomozaki - Volume 02.epub` | `1kCgzfriuHOjBmDOqsgR0MpLEz3aTqI25` | conformant |
| V03 | `Bottom-Tier Character Tomozaki - Volume 03.epub` | `1-jH7p1p6e_VntksYmTbWsmLR_PXHOYJz` | conformant |
| V04 | `Bottom-Tier Character Tomozaki - Volume 04.epub` | `11uMXDm8P_rogddhc2zbFPUCIIzAV96yM` | warning: `mimetype` stored but not first ZIP entry |
| V05 | `Bottom-Tier Character Tomozaki - Volume 05.epub` | `1-jxcBWOue222BQgLe_YtCx2b-yxTwgey` | conformant |
| V06 | `Bottom-Tier Character Tomozaki - Volume 06.epub` | `1qLaYW6sAB53rRmy9e9JiY5kqYjLVyoea` | conformant |
| V06.5 | `Bottom-Tier Character Tomozaki - Volume 06.5.epub` | `1OsdRIVq-OlNt5H_IbuWQ520ukjA5ztMs` | conformant |
| V07 | `Bottom-Tier Character Tomozaki - Volume 07 - Special Edition.epub` | `1VEZAtMl5OCikfdXuNFwktUgJAWTelL_-` | conformant |
| V08 | `Bottom-Tier Character Tomozaki - Volume 08.epub` | `13BKJFLC8KlyTSTkYqnv7a7O4h0TMGmJi` | conformant |
| V08.5 | `Bottom-Tier Character Tomozaki - Volume 08.5.epub` | `1Xqu390B_qO1-Vb6aRiA1Dj8ZWWla7EhJ` | conformant |
| V09 | `Bottom-Tier Character Tomozaki - Volume 09.epub` | `16LTaamXaorLJSXLyz_-TyFanr0KDOfIM` | conformant |
| V10 | `Bottom-Tier Character Tomozaki - Volume 10.epub` | `13mY73cl9ICy-vPyrOUs5ADEHlxz8Zxw8` | conformant |
| V11 | `Bottom-Tier Character Tomozaki - Volume 11.epub` | `15oMprkgH7ZNAeipMu6Ahkcsa7wwCjjFa` | warning: `mimetype` stored but not first ZIP entry |

The Drive file IDs above identify the currently enumerated folder objects. The audited SHA-256 values in `audit_manifest.json` remain the byte-identity authority.

## 5. Main-chain routing

The prospective numbered reading chain is:

`V01 → V02 → V03 → V04 → V05 → V06 → V07 → V08 → V09 → V10 → V11`

Repository deep-reading filenames should use:

`TOMOZAKI_V01_DEEP_READING.md` through `TOMOZAKI_V11_DEEP_READING.md`.

Volumes V06.5 and V08.5 are available source witnesses but are not silently inserted into the integer-numbered chain. Their analytical placement must be explicitly decided from publication/diegetic context before consultation, then recorded without rewriting earlier prospective freezes.

## 6. Special-edition routing for Volume 07

The locked V07 witness is named `Bottom-Tier Character Tomozaki - Volume 07 - Special Edition.epub`.

This establishes only that the acquired source object is the Special Edition witness. It does **not** establish, without further source review, which contents differ from a standard edition or whether any extras should be analytically segregated.

When V07 is read:

1. record the exact audited witness;
2. identify any clearly separable special-edition material if present;
3. keep main-narrative evidence distinct from edition-specific supplements when the source structure warrants it;
4. do not infer standard-edition absence/presence from memory or retailer metadata alone.

## 7. Integrity notes and warnings

The 2026-08-29 audit records:

- all 13 files pass ZIP CRC testing;
- all 13 contain valid EPUB container metadata;
- 11 files are packaging-conformant under the audit's check;
- V04 and V11 store `mimetype` but do not place it first in the ZIP container;
- no byte-identical duplicate groups were found;
- the numbered main range V01-V11 has no gaps.

The V04/V11 findings are **packaging-structure warnings, not evidence that the books are corrupt or unreadable**.

## 8. Witness selection rules

For a numbered deep reading:

1. identify the exact normalized filename, Drive file ID, and audited SHA-256 from `audit_manifest.json`;
2. analyze the Japanese text;
3. if extraction or text conversion is used, preserve enough provenance to return to the EPUB passage;
4. use illustrations as evidence only when actually reviewed and relevant;
5. preserve focalizer and section identity when the volume contains appended or alternate-viewpoint material;
6. do not replace unread Japanese passages with adaptation memory, translation summaries, wiki descriptions, or model knowledge.

For wording-sensitive claims, preserve the Japanese expression and enough local context to adjudicate register and ambiguity.

## 9. Current exclusions / not-yet-integrated material

This lock contains only the audited 13 EPUB objects described above. It does not by itself establish presence or authority for:

- Volume 12 or any later numbered volume;
- anime adaptations;
- manga adaptations;
- official or unofficial translations;
- retailer-exclusive bonuses or purchase extras not represented by the audited files;
- drama/audio material;
- interviews or production commentary;
- reception material, reviews, social-media discussion, or fandom sources.

If any of these are later used, create or revise the appropriate source/evidence routing record first and state whether the witness is primary, supplemental, adaptation, translation, production-context, or reception evidence.

## 10. Source-lock change rule

A new acquisition does not retroactively alter what V0.1 contained.

When the source set changes:

- retain this audit date and manifest identity as historical provenance;
- create a new audited source boundary or explicit additive source record;
- identify added/removed/replaced witnesses by stable identity and hash;
- state which analytical artifacts require re-evaluation;
- preserve prior prospective freezes.

Do not overwrite source history for convenience.
