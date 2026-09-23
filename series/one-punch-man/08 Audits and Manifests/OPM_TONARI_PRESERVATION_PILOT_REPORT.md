---
series: OPM
artifact_type: technical_preservation_audit
scope: Isolated Tonari preservation pilot captured 2026-09-12
generation: V2
status: historical_legacy
source_boundary: Technical checks of publisher episodes 282-284; no narrative authority
supersedes: []
superseded_by: []
do_not_use_as_current_authority: true
created: 2026-09-13
---

Publication note: the report below preserves the technical result and the analytical boundary recorded at the time of capture. Its V27 statement is historical; current cumulative analysis is through V34. Local-only evidence references are rendered as paths because raw captures, manga images, scripts and packages are not included in this Git publication. Consult `CURRENT_STATE_AND_CORPUS_MAP.md` and the continuation hand-off for current work. No new narrative review was performed for publication.

# Tonari image preservation pilot — 12 September 2026

**PASS for the three sampled chapters.** All 58 main-page images were preserved at 800 × 1138 pixels, reconstructed using the public reader's tile permutation, and given local revision-specific citations. Fourteen beginning, middle and ending page samples matched official browser renders. This is a technical preservation result; reading comprehension and the Volume 37/web continuation boundary were not assessed.

The pilot remains quarantined here. No manga page was displayed to the model, no OCR or dialogue extraction was performed, and no narrative summaries or analytical entries were created. All 135 files in the recorded canonical corpus baseline remain byte-identical. The sequential analysis boundary remains V27 completed, V28 next.

| Publisher chapter | Published (JST) | Main images | Browser reference image ordinals |
|---|---|---:|---|
| [282](https://tonarinoyj.jp/episode/12207421984090138482) | 2026-08-13 | 24 | 1, 12, 13, 24 |
| [283](https://tonarinoyj.jp/episode/12207421984148777688) | 2026-08-27 | 17 | 1, 8, 9, 16, 17 |
| [284](https://tonarinoyj.jp/episode/12207421984214112687) | 2026-09-10 | 17 | 1, 8, 9, 16, 17 |

These are the three newest numbered chapter entries in the [official series feed](https://tonarinoyj.jp/rss/series/13932016480028984490) captured on 12 September 2026; episode metadata also links them in sequence, with no next episode for 284. These labels have not been equated to tankobon chapter numbers. The feed, its response metadata, episode HTML and reader metadata are preserved locally.

## Recovered transformation

The public reader selects its `baku` transformation for all three episodes. It transposes a 4 × 4 grid of whole tiles. For an image of width W and height H, tile width is `floor(W / 32) × 8` and tile height is `floor(H / 32) × 8`. A tile at column c, row r moves to column r, row c. Pixels inside each tile keep their positions; pixels beyond the grid remain unchanged.

For these 800 × 1138 images, each tile is 200 × 280 pixels, the grid covers 800 × 1120, and the bottom 18 rows remain unchanged. Applying the same permutation twice returns the original image. Reconstruction adds no resampling or JPEG recompression: the decoded JPEG pixels are saved as lossless PNG. It cannot recover detail already absent from the publisher's JPEG.

Source: [publisher reader JavaScript](https://cdn.tonarinoyj.jp/js/4767.d32012e63dba46862d9d.chunk.js), active module 55324, with an equivalent secondary implementation in module 91088. Preserved source SHA-256: `6df3e24b9962f0349fe76137b5a1051fe612fde09206eae603bd59e61ec5706e`.

Local reconstruction script (local-only: `OPM_ANALYSIS_ROOT/_staging/pilots/tonari_2026-09-12/restore_pages.py`) · Preserved publisher code (local-only: `OPM_ANALYSIS_ROOT/_staging/pilots/tonari_2026-09-12/provenance/renderer/4767.d32012e63dba46862d9d.chunk.js`)

## Verification and limits

All 58 original JPEGs fully decode, match the dimensions in the reader metadata, and retain their recorded SHA-256 hashes. All 58 restored PNGs match the reconstruction pixel-for-pixel, survive PNG encode/decode without pixel changes, return to the source when the permutation is applied again, and preserve the uncovered margin. Their order follows the publisher's `main` entries. The five other entries per episode remain documented as metadata; they are not counted as manga pages. No exact-byte duplicates were found.

All 14 browser references pass the retained thresholds of grayscale template correlation ≥ 0.985 and mean absolute RGB error ≤ 8 on a 0–255 scale. The lowest observed correlation was 0.997608; the largest mean error was 4.195. The references are JPEG browser screenshots, so bit equality with the source-derived PNGs is not expected. The remaining 44 pages passed mechanical checks but were not individually compared with browser screenshots.

Full-page browser capture shifted content horizontally after the DOM coordinates were measured. Matching therefore used native-size pages across the recorded frame width, within eight vertical pixels of the observed page area. Full screenshots, frame hashes, initial coordinates and final registration offsets are retained. This compares pixels without reading the content. Some initial DOM-only crops were misaligned and are explicitly marked as superseded diagnostics; they are not citation targets.

This validates the current reader mode on three episodes. A changed reader algorithm, a different image mode, source revisions or a different publication format require another check. Japanese text legibility, translation accuracy, narrative continuity and the full post-V37 backlog have not been evaluated by this isolated pilot.

Detailed browser comparison results (local-only: `OPM_ANALYSIS_ROOT/_staging/pilots/tonari_2026-09-12/fidelity_verification.json`) · Corpus isolation check (local-only: `OPM_ANALYSIS_ROOT/_staging/pilots/tonari_2026-09-12/corpus_isolation_verification.json`)

## Durable references

Open the local citation index (local-only: `OPM_ANALYSIS_ROOT/_staging/pilots/tonari_2026-09-12/CITATION_INDEX.md`). There are 58 verified local page links and three ordered CBZ archives, each checked for CRC integrity and exact PNG hashes. The archives include source/restoration manifests and portable citation records.

A citation identifies `OPM|WEB|episode:<publisher ID>|capture:<snapshot ID>|image:<four-digit ordinal>`. The index records the restored PNG hash, original JPEG hash and source URLs. Local files provide the evidence; URLs provide provenance. Image ordinals start at 1 and follow main-page order. Reader structure indices in the manifests are one-based; raw DOM receipt indices are zero-based.

For the backlog, preserve original bytes, reader metadata, a restored PNG set, algorithm provenance and an immutable snapshot ID together. A later publisher revision should receive a new snapshot directory and new hashes. Keep old versions so existing references remain resolvable. Crosswalk the first post-V37 web content only when the sequential reading reaches that boundary.

## Files and reproduction

Within each episode directory, `pages/` holds the scrambled original JPEG responses; `restored/` holds the usable preserved pages. `browser_frames/` holds untouched official screenshots and receipts, and `browser_reference_aligned/` holds the verified samples. `rendered/` contains superseded diagnostic crops. `manifest.json` records raw provenance, and `restoration_manifest.json` records the transformation and verification results. Root-level `provenance/` contains the feed, corpus baseline and reader JavaScript; `packages/` contains CBZ snapshots.

The scripts require Python with Pillow, NumPy and OpenCV. Reproduction order is `restore_pages.py`, `verify_render_fidelity.py`, then `finalize_pilot.py`. These scripts rebuild derived pilot outputs in this fixed directory. Do not rerun capture/download scripts here for a future publisher revision; start a fresh snapshot directory instead. The loopback capture receiver was stopped, the temporary browser viewport was reset, and pilot browser tabs were closed.
