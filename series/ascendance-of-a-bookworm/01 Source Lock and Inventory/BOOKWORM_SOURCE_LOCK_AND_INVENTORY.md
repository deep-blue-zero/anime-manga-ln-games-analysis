---
series: ASCENDANCE_OF_A_BOOKWORM
artifact_type: source_lock_and_inventory
scope: JP_LIGHT_NOVEL_EPUB_CORPUS
source_audit_date: 2026-08-30
generation: V0.1
status: canonical
release_state: mutable_active
---

# Ascendance of a Bookworm — source lock and inventory

## 1. Responsibility

This file defines the exact primary-source boundary for the initial Git-native Bookworm analytical project. It is a source-routing and integrity artifact, not literary analysis.

If later source material is acquired, revise or supersede this lock explicitly. Do not silently treat new files, adaptations, translations, web text, reference books, or remembered canon as though they were present in the 2026-08-30 audit.

## 2. Canonical source locations

Primary-source Drive root: `1tNJvglC-ri_AEGTkJupZ78WddyiCqQMy`  
Series source folder: `1jijErFCqkxFfP1C8s5SJkaphiImF_vvJ` (`Bookworm`)  
Audit manifest file ID: `1EWZLfUcopzCJT3iCZmCElOnq0jFUWgL0` (`audit_manifest.json`)  
Audit manifest SHA-256: `034f01acae4e14f58ad8f9ea925ef00813603c74b590f08c8ba4e628db147d82`  
Audit date: `2026-08-30`

The audit identifies the series as:

- English title: *Ascendance of a Bookworm*
- Japanese title: `本好きの下剋上～司書になるためには手段を選んでいられません～`
- author metadata: Miya Kazuki
- normalized filename convention: `Ascendance of a Bookworm - Volume NN.epub`

The normalized English filename is an inventory label only. Source semantics remain Japanese.

## 3. Inventory lock

| Class | Count / state |
|---|---:|
| EPUB objects | 34 |
| Numbered main volumes | 33 |
| Main range | V01-V33 |
| Gaps inside numbered main range | none |
| Side-story volumes | 1 |
| Side-story title in audit | *Royal Academy Stories: First Year* |
| Exact duplicate groups | 0 |
| ZIP CRC checks passed | 34 / 34 |
| EPUB container checks passed | 34 / 34 |
| Packaging-conformant | 22 |
| Packaging warnings | 12 |

The audit manifest is the canonical per-file checksum/old-name/new-name inventory. This Git file does not duplicate all 34 SHA-256 rows because that would create a second checksum ledger with no independent responsibility.

## 4. Numbered-main-series part routing

The Japanese filenames preserve the work's five-part structure. For deterministic Git routing, use global volume numbering while retaining this part identity in analytical metadata.

| Global volumes | Japanese part identity | Within-part labels represented |
|---|---|---|
| V01-V03 | `第一部「兵士の娘」` | I-III |
| V04-V07 | `第二部「神殿の巫女見習い」` | I-IV |
| V08-V12 | `第三部「領主の養女」` | I-V |
| V13-V21 | `第四部「貴族院の自称図書委員」` | I-IX |
| V22-V33 | `第五部「女神の化身」` | I-XII |

Repository deep-reading filenames therefore remain `BOOKWORM_V01_DEEP_READING.md` through `BOOKWORM_V33_DEEP_READING.md`. The deep-reading header should also record the Japanese part and within-part volume identity.

## 5. Supplemental source in the lock

The acquired non-numbered EPUB is normalized as:

`Ascendance of a Bookworm - Royal Academy Stories - First Year.epub`

The audit classifies it as a `side_story` and records SHA-256:

`a7542cb46e44be832c768d89ab4abf7d2bcf02423fbeb8a359ac13127771f986`

It is inside the **available source inventory** but not inside the numbered prospective reading chain. Before using it analytically, verify its publication/diegetic placement and focalization relative to the frozen numbered-volume state. Its later consultation may revise the current interpretation but must not rewrite earlier prospective predictions.

## 6. Integrity notes and warnings

The 2026-08-30 audit records:

- all 34 files pass 7-Zip CRC testing;
- all 34 contain valid EPUB container metadata;
- Volumes 01-12 are readable but do not place the uncompressed `mimetype` entry first as recommended by the EPUB packaging specification;
- Volumes 13-33 and *Royal Academy Stories: First Year* are packaging-conformant under the audit's check;
- no byte-identical duplicate files were found.

The first twelve packaging warnings are therefore **packaging-structure warnings, not evidence that the books are corrupt or missing**.

The audit also identifies a repeated embedded identifier (`urn:uuid:273fd756-62f2-4858-8d67-99e08f24bba9`) across Volumes 14-19 and *Royal Academy Stories: First Year* even though the files and contents are distinct. Treat that identifier as defective metadata and never use it alone as source identity. File identity is anchored by the audited filename, SHA-256, and source-folder provenance.

## 7. Witness selection rules

For a numbered deep reading:

1. identify the exact normalized filename and audited SHA-256 from `audit_manifest.json`;
2. record global volume number plus Japanese part/within-part identity;
3. analyze the Japanese text;
4. if extraction or text conversion is used, preserve enough provenance to return to the EPUB passage;
5. use images/illustrations as evidence only when actually reviewed and relevant;
6. do not replace unread Japanese passages with adaptation memory or translation summaries.

Where the EPUB contains multiple focalizers or appended stories, preserve their local viewpoint identity rather than treating the whole volume as a single omniscient voice.

## 8. Current exclusions / not-yet-integrated material

This lock contains only the audited 34 EPUB objects described above. It does not by itself establish presence or authority for:

- anime adaptations;
- manga adaptations;
- official or unofficial translations;
- web-publication versions;
- fanbooks/reference books;
- retailer-exclusive bonuses or purchase extras;
- other side-story collections or supplemental prose;
- interviews, production commentary, reception material, or fandom sources.

If any of these are later used, create or revise the appropriate source/evidence routing record first and state whether the witness is primary, supplemental, adaptation, translation, production-context, or reception evidence.

## 9. Source-lock change rule

A new acquisition does not retroactively alter what V0.1 contained.

When the source set changes:

- retain this audit date and manifest identity as historical provenance;
- create a new audited source boundary or explicit additive source record;
- identify added/removed/replaced witnesses by stable file identity and hash;
- state which analytical artifacts require re-evaluation;
- preserve prior prospective freezes.

Do not overwrite source history for convenience.
