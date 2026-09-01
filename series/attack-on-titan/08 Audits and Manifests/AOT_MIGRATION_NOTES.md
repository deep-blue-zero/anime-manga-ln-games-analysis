---
corpus: AOT_JP_DEEP_READING
document: migration_notes
version: "2.0"
date: "2026-08-11"
migrated_scope: "Volumes 1-18 plus the Volumes 1-9 checkpoint synthesis"
---

# Attack on Titan v2 Migration and Provenance Notes

## 1. Purpose

This package converts the existing *Attack on Titan* deep-reading project into a durable, Library-searchable Markdown corpus governed by `AOT_ANALYTICAL_METHOD_V2.md`.

The original work was produced conversationally, one volume at a time, before canonical Markdown artifacts, YAML metadata, evidence IDs, source checksums, and locator ledgers were mandatory.

The migration therefore had to preserve two different things:

1. the spoiler-bounded interpretations developed in the historical chat; and
2. the provenance standards required for future synthesis.

## 2. Provenance status of the volume files

The new `AOT_VXX_DEEP_READING.md` files are **not represented as byte-for-byte exports of the original chat responses**.

They are preservation-oriented canonical reconstructions that combine:

- the historical analysis and conclusions preserved in the current project conversation;
- a fresh structural audit of the mounted Japanese CBZ;
- verified filename, hash, image count, chapter range, and chapter-title metadata;
- v2 evidence classification;
- chapter-level source locators and selected Japanese anchors;
- explicit migration notes and current cumulative deltas.

The governing metadata is therefore:

```yaml
provenance_status: migrated_legacy_analysis_reconstructed
```

All eighteen Japanese CBZs were present and passed archive-integrity testing during migration. The artifacts should therefore be understood as **source-audited regenerated canonical editions**, not merely unsourced memory summaries.

## 3. What was deliberately not claimed

The package does not claim:

- that every sentence reproduces the historical response verbatim;
- that every original chat heading was preserved;
- that every load-bearing claim has a completed image-level locator;
- that later volumes were used to rewrite earlier interpretations;
- that the migration constitutes a full second pass through every panel of all eighteen volumes.

Where exact image-level verification was not completed, the volume artifact uses:

```yaml
locator_status: chapter_complete_page_selective
```

or records `pending_page_backfill` in the locator ledger.

A missing locator is preserved as an auditable gap. No CBZ image locator was fabricated from memory.

## 4. Spoiler-boundary preservation

Each volume artifact preserves the epistemic boundary through that volume.

For example:

- Volume 5 does not name the Female Titan operator;
- Volume 9 treats Ragako transformation as a strong inference rather than a settled mechanism;
- Volume 10 does not import the full later explanation of Ymir, Reiner, Bertolt, the Beast Titan, or the Reiss succession;
- Volume 14 does not use later knowledge to settle Rod Reiss's motives;
- Volume 18 does not use later battle results or basement revelations.

Later knowledge is reserved for explicitly labeled retrospective-correction entries after the relevant later volume has been analyzed.

## 5. Volume 1–3 status

The earliest three historical responses were not available in a separate machine-readable transcript at migration time.

Volumes 1–3 were therefore reconstructed from:

- the mounted original Japanese CBZs;
- the cumulative model established by the later volume analyses;
- the known original spoiler boundaries;
- and direct continuity with the canonical Volume 4 reading.

They are not described as verbatim legacy exports.

## 6. Volume 4–18 status

The historical analyses for Volumes 4–18 were preserved in the active project conversation and supplied the interpretive basis for the canonical reconstructions.

The new files preserve their major arguments, including:

- Volume 4's `原初的欲求` / birth-and-freedom thesis;
- Volume 5's seeing/knowledge architecture;
- Volumes 6–7's choice, trust, result, and regret problem;
- Volume 8's `良い人` and human/Titan boundary collapse;
- Volume 9's home/language/Ragako reading;
- Volumes 10–12's soldier/warrior, Ymir/Historia, recognition, and Coordinate arguments;
- Volumes 13–17's political legitimacy, memory, inheritance, self-authorship, and governance analysis;
- Volume 18's transformation of specialness and Eren's plural freedom claim.

The prose has been reorganized into the v2 twenty-one-function artifact structure.

## 7. Checkpoint synthesis

The previous Volumes 1–9 quarter-series synthesis is preserved as:

```text
AOT_CHECKPOINT_25P_V01-V09_SYNTHESIS.md
```

It is a reconstructed canonical checkpoint rather than a byte-identical chat export. Its claims remain bounded by Volume 9.

## 8. Correction of a prior project-planning error

One earlier cadence response referred to a full-series endpoint after **Volume 37**. That was incorrect.

The canonical manga ends at **Volume 34**.

All v2 filenames, checkpoint planning, and final-synthesis architecture use Volumes 1–34.

This correction is recorded explicitly rather than silently erased.

## 9. Checkpoint policy retained

The project retains the user's chosen cadence:

- 25% synthesis after Volumes 1–9;
- 50% synthesis around Volumes 18–19;
- 75% synthesis at a later natural threshold;
- definitive full-series synthesis after Volume 34.

The volume-by-volume close reading remains the default because each tankōbon functions as a dense formal and argumentative unit.

## 10. Canonical status

From this package onward:

- the downloadable Markdown file is the canonical analytical artifact for its volume;
- future corrections should be recorded rather than silently overwritten;
- future volume analyses should be emitted natively under v2;
- final synthesis should retrieve these artifacts first and reintroduce raw CBZs selectively for source verification.

## 11. Source exclusion

The delivery archive contains no copyrighted manga pages or CBZ payloads.

It contains only:

- analytical Markdown;
- method and provenance documents;
- manifests;
- checksums;
- machine-readable metadata.
