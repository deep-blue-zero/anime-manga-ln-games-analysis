---
corpus: NANA_JP_DEEP_READING
artifact: PHASE8_FINAL_ARCHIVAL_AUDIT
release_version: "v1.0"
status: final_audit_passed
generated: "2026-08-14"
---

# NANA v1.0 — Phase 8 Final Archival Audit

## 1. Audit result

The v1.0 analytical corpus **passes the final archival audit**. The package is suitable to freeze as an immutable analytical release, with one disclosed corrective reconstruction: Document 10 was rebuilt from the frozen evidence layer because its earlier generated file was no longer recoverable when Phase 8 began.

The audit covers five required architecture-defined operations:

1. cross-document duplication control;
2. terminology and naming consistency;
3. evidence-ID and locator integrity;
4. artifact/source checksum consistency;
5. package-scope and release hygiene.

No audit result manufactures stronger source certainty than the active files support. In particular, Japanese source binaries for Volumes 4–19 were not mounted during Phase 8 and therefore were **not** falsely described as directly re-hashed. Their identities remain locked by the canonical volume YAML and the frozen evidence ledger.

## 2. Canonical corpus presence and text integrity

| Layer | Files | Whitespace-delimited words | Bytes |
|---|---:|---:|---:|
| Reader-facing Documents 00–14 | 15 | 127,433 | — |
| Archival/reference Documents 15–16 | 2 | 19,575 | — |
| Numbered corpus 00–16 | 17 | 147,008 | 1,036,795 |
| Sequential V01–V21 + Ch81–84 | 22 | 419,611 | 2,808,630 |
| Governing method + architecture | 2 | 10,026 | 73,197 |
| **Substantive analytical corpus** | **41** | **576,645** | **3,918,622** |

The separate Phase-2 evidence-stabilization audit adds 805 words of historical administrative provenance.

Validation results:

- canonical planned files missing: **0**;
- UTF-8 decoding failures: **0**;
- required YAML/front-matter parse failures: **0**;
- numbered document-map filename targets missing from the README: **0**;
- residual `sandbox:/` links: **0**;
- residual file-citation UI markup: **0**;
- residual writing-block/chat-turn markup: **0**;
- `TODO` / `TBD` / draft-placeholder markers: **0**.

Superseded/intermediate files were explicitly excluded from release scope, including `NANA_CH081_084_CONTINUATION_DEEP_READING_IN_PROGRESS.md`, the exact duplicate working export `14_original.md`, and the obsolete Drive-readability status note `NANA_READABILITY_AND_DRIVE_REPLICATION_AUDIT.md`.

## 3. Cross-document duplication audit

The duplication test was deliberately aimed at **argument duplication**, not at legitimate recurrence of evidence IDs, Japanese phrases, titles, headings, or short thesis summaries.

Across Documents 00–16:

- exact normalized paragraphs of at least **600 characters** duplicated across different numbered documents: **0**;
- exact normalized cross-document sequences of **50 consecutive words**: **0**;
- accidental duplicate numbered files in the release set: **0**.

This satisfies the architecture's rule that a scene may recur when the analytical question changes, but the same argument should not be reproduced wholesale across specialist documents.

`14_original.md` was confirmed byte-for-byte/content-hash identical to canonical Document 14 and is excluded from the archive rather than counted as a corpus duplicate.

## 4. Terminology and naming consistency audit

The corpus convention remains:

- **Hachi** for Komatsu Nana when disambiguation from Osaki Nana is required;
- **BLAST** for BLACK STONES;
- **Trapnest** as the standard group romanization;
- **Reira Serizawa**;
- **Takumi Ichinose**;
- **Ren Honjo**;
- **Shin Okazaki**;
- **NANA 7.8** for the official fan book;
- `707` / Room 707 / Apartment 707 where the prose distinguishes physical apartment, household, ritual/archive space, or receiving address.

Variant scan across Documents 00–16 found **zero** occurrences of the known conflicting forms `Layla`, `Leila`, `Raira`, `TrapNest`, all-caps `TRAPNEST`, title-case `Blast`, `Hachiko`, `Honjou`, `Honjō`, `Ichinose Takumi`, `Serizawa Reira`, `Shinichi Okazaki`, `NANA 7・8`, or `NANA 7,8`.

Japanese-order and English-order presentation of the two protagonists' full names is retained where context requires it—for example source metadata may say `大崎ナナ / Osaki Nana`, while English critical prose may naturally say `Nana Osaki`. This is a name-order convention difference, not a disagreement about identity.

Conceptual terminology also remains differentiated rather than normalized into false synonyms. The corpus continues to distinguish:

- friendship / chosen family / domestic partnership / romantic or erotic coding / structural romance / categorical romance;
- care / protection / provision / jurisdiction / coercion;
- dependence / being needed / possession / belonging;
- future-narrator interpretation / textual fact / character belief / unresolved ambiguity;
- trajectory / destination.

No terminology correction required rewriting a frozen sequential artifact.

## 5. Evidence-ID integrity audit

The sequential evidence layer owns **2,468 unique evidence IDs** across Volumes 1–21 and Chapters 81–84.

Results:

- evidence IDs with a recoverable primary-source locator route: **2,468 / 2,468**;
- evidence IDs lacking locator coverage: **0**;
- numbered-synthesis references to nonexistent evidence IDs: **0**.

The locator audit recognizes the different historically valid forms used by the corpus:

- full IDs such as `NANA_V21_E034`;
- volume-local shorthand such as `E001`;
- ranged locator rows such as `E001–E002`;
- continuation shorthand such as `C81_E001`;
- continuation evidence rows whose archive/printed-page locator is embedded directly in the evidence table.

No printed page number was inferred where the original artifact did not establish one. EPUB spine pages remain the stable governing locator for the Japanese tankōbon layer when printed pagination is unavailable.

## 6. Frozen-ledger artifact integrity

`15_VOLUME_BY_VOLUME_EVIDENCE_LEDGER.md` freezes the SHA-256 of each sequential analytical artifact.

Phase 8 re-hashed the current local files and found:

- Volume 1–21 analytical artifacts matching frozen Doc15 SHA-256: **21 / 21**;
- Chapters 81–84 continuation analytical artifact matching frozen Doc15 SHA-256: **1 / 1**;
- Volume 1–21 primary-source hashes recorded in Doc15 matching the corresponding per-volume YAML: **21 / 21**.

The two missing `locator_status` YAML fields in Volumes 20–21 remain a metadata-normalization issue only. Their evidence and locator tables are present and audited; changing the frozen files solely to add that metadata would unnecessarily invalidate the Doc15 artifact hashes.

## 7. Direct source-binary revalidation performed in Phase 8

The following source payloads were mounted and could therefore be directly tested:

- Japanese EPUBs: Volumes **1, 2, 3, 20, 21**;
- continuation CBZs: Chapters **81, 82, 83, 84 English, 84 Spanish**;
- official paratext PDF: **NANA 7.8**.

For the ten ZIP-based EPUB/CBZ files, SHA-256 matched the canonical record in **10 / 10** cases and archive CRC testing passed in **10 / 10** cases. `NANA 7.8` was re-hashed separately and matched its canonical Document-13 SHA-256 exactly.

For Volumes 4–19, the source payloads were not mounted at release time. Their hashes remain recorded and mutually consistent between the per-volume YAML and frozen Doc15 ledger, but Phase 8 makes no new binary-integrity claim for those unavailable payloads.

## 8. Continuation provenance boundary

The audit preserves the mixed-language status of Chapters 81–84:

- Ch81–83: English fan translations;
- Ch84: English fan translation where present;
- Ch84 printed pp.11–16: Spanish fan-translation fallback.

The continuation can stabilize events, chronology, visual form, relationship state, objects/spaces, and broad thematic interpretation. It cannot stabilize Japanese pronouns, honorifics, sentence-final register, exact wording, or lexical recurrence. Document 10 and Document 16 preserve this prohibition.

## 9. Corrective release note — Document 10

The originally generated Phase-5 file `10_JAPANESE_VOICE_ADDRESS_RELATIONAL_LANGUAGE_AND_LEXICAL_SYSTEM.md` was no longer present in the active local workspace and had not been successfully mirrored to Drive. An exact recovery attempt did not produce the missing canonical file.

Rather than silently omitting Document 10 or pretending the earlier bytes remained available, Phase 8 reconstructed the canonical release copy from:

- the frozen Japanese Volume 1–21 evidence corpus;
- the mature Nana/Hachi, ethics, and temporal syntheses;
- Document 14's settled comparative conclusions;
- Document 16's verified lexical/source routes;
- the already-settled Phase-5 linguistic conclusions.

The reconstructed file carries `release_reconstruction_note` in its YAML. Its evidence references were included in the global numbered-document evidence audit and resolve successfully. The v1.0 package therefore treats this reconstructed copy—not the unavailable earlier generation—as canonical.

## 10. Release-scope hygiene

The definitive package contains **analytical and audit artifacts only**. It excludes:

- all Japanese manga EPUB source payloads;
- all continuation CBZ source payloads;
- the `NANA 7.8` PDF source payload;
- superseded in-progress continuation analysis;
- intermediate exact-copy exports;
- stale Drive-replication administrative notes;
- temporary build scripts and audit scratch data.

Source identities remain auditable through `SOURCE_INVENTORY.md` without redistributing copyrighted primary material.

## 11. Freeze judgment

No unresolved issue found by the final audit requires reopening the literary synthesis. The v1.0 corpus may therefore be frozen under the following rule:

> **Corrections after this point create a new version. They do not silently mutate v1.0.**

The most likely future revision trigger is Japanese-original Chapters 81–84 or newly published canonical manga. Such material should be treated as source re-entry, with explicit claim revision and versioned release notes.
