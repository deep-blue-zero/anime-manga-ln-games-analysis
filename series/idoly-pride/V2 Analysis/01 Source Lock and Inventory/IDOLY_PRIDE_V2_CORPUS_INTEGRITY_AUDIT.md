---
title: "IDOLY PRIDE V2 Corpus Integrity Audit"
project: "IDOLY PRIDE"
document_id: "IDOLY_PRIDE_V2_CORPUS_INTEGRITY_AUDIT"
version: "1.1"
status: "phase-0-audit-pass-with-known-gaps"
source_snapshot_id: "IP-V2-SNAPSHOT-2026-08-13-A"
source_cutoff: "2026-08-13"
created: "2026-08-13"
updated: "2026-08-13"
framework_version: "2.1"
canonical_framework_set: "IP-V2-FRAMEWORK-2026-08-13-AV"
---

# IDOLY PRIDE V2 CORPUS INTEGRITY AUDIT

## 1. Result

**PHASE 0 INTEGRITY RESULT: PASS WITH EXPLICIT NON-BLOCKING GAPS**

The source corpus is sufficiently complete, internally traceable, and technically coherent to begin the canonical next step, **Phase 0.5: prospective complete anime deep reading**, before Phase 1 game-corpus reconnaissance.

No evidence was found of broad narrative-data loss, cross-series contamination, duplicate story IDs, malformed ingestion, or incomplete episode coverage.

Known gaps are bounded and documented.

## 2. Game ingest validation

The `idoly-ingest` validation report records:

| Check | Result |
|---|---:|
| Source story folders discovered | 3,879 |
| Bundles created | 665 |
| Source stories included | 3,879 |
| Source stories excluded | 0 |
| Missing `script.md` | 0 |
| Missing `script.jsonl` | 0 |
| Duplicate story IDs | 0 |
| JSONL parse errors | 0 |
| Unreadable metadata files | 0 |
| Suspected missing numeric event/card parts | 0 |
| Bundles over hard cap | 0 |

Sixty-five bundles exceed the 20,000-character soft cap, but none exceeds the 30,000-character hard cap. This is a context-size management detail, not a completeness failure.

The ingest validator reports no failures and no warnings.

## 3. Analysis-bundle validation

The `analysis_bundles` validator reports an overall PASS.

Locked counts:

| Measure | Count |
|---|---:|
| Total scenes | 3,879 |
| Dialogue/items | 217,686 |
| Telephone references | 256 |
| Machine-generated telephone transcripts | 211 |
| Telephone audio unavailable upstream | 45 |
| Player-choice items preserved | 14,645 |
| Raw `{user}` placeholders preserved | 1,650 |
| Missing processed transcript assets | 32 |

This is strong evidence that the analysis layer is preserving the broad source corpus rather than silently reducing it to a curated subset.

## 4. Source snapshot coherence

The source snapshot and derived ingest agree on the 3,879-story ingestion frontier.

The lower-level source snapshot records:

- 2,067 story metadata records;
- 160 bond stories;
- 1,089 card story parts across 363 card-story stems;
- 2,120 unique transcript asset IDs discovered;
- 2,088 transcript JSON assets cached;
- 2,067 normalized story scripts;
- 173,316 normalized story utterances;
- 45 message groups;
- 1,812 message threads;
- 44,370 normalized message lines/items;
- 256 telephone references;
- 211 cached telephone audio files;
- 211 approximate ASR transcripts.

The difference between story metadata counts and total derived source-story folders is expected because the combined analytical corpus also contains cards, bonds, messages, specials, and other source classes organized above the core story-metadata count.

## 5. Transformation integrity

The analysis-bundle README documents the transformations applied to source dialogue:

- display wrapping is normalized away;
- raw title/section values are preserved;
- granular source paths are preserved;
- dialogue punctuation is otherwise untouched;
- `{user}` placeholders are retained;
- player choices are labeled `Manager (player)`;
- all choice branches are included.

No evidence in the inspected validation material suggests paraphrastic rewriting of ordinary Japanese game dialogue during bundle construction.

## 6. Missing processed assets

There are 32 stories with 32 missing processed asset references.

The missing-assets report shows that the overwhelming majority are `adv-live-*` assets associated with live/performance presentation rather than missing ordinary dialogue text.

One explicitly listed exception is a card visual (`card_kkr_16_02`).

Analytical implication:

- ordinary textual characterization remains broadly usable;
- formal/performance claims involving affected stories may require a `FORMAL-DEPENDENT` or `UNRESOLVED` status;
- the missing-asset list should be checked before making a load-bearing audiovisual claim from an affected source.

This gap does not justify downgrading the corpus as a whole.

## 7. Telephone coverage

Telephone coverage is incomplete by upstream availability, not by unexplained ingestion failure.

At source lock:

- 256 telephone references exist;
- 211 have cached source audio;
- 45 have no upstream source audio;
- 211 have machine-generated Whisper ASR.

Risk:

ASR can introduce wording, segmentation, name, particle, and register errors.

Mitigation:

- use ASR for discovery and semantic orientation;
- verify relevant audio for exact quotation or linguistic micro-analysis;
- mark unavailable-audio calls as `PHONE-GAP`.

## 8. Anime episode identity

All twelve supplied screenshot archives are confirmed as IDOLY PRIDE Episodes 01-12 by their internal metadata and extraction provenance.

The external extraction manifest independently identifies:

- show: `Idoly Pride`;
- item count: 12;
- source set: Episodes 01-12;
- Japanese audio source: FLAC stereo, 48 kHz;
- analysis outputs: `ep01_screenshots.zip` through `ep12_screenshots.zip`;
- bundled complete-audio MP3 for each episode.

No episode is missing from the sequence.

## 9. Anime visual extraction integrity

Locked aggregate extraction:

- 9,052 screenshots;
- 458 contact sheets;
- 12/12 episodes.

Per-episode counts recorded by the extraction manifest match the logical uploaded bundle identities.

Several archives differ slightly in total ZIP byte size from the earlier manifest. The user reports that screenshot deduplication may explain minor discrepancies.

Because the Phase 0 package hashes the exact supplied ZIPs, this does not create an identity ambiguity for future analysis.

## 10. Anime subtitle timing audit

The supplied subtitle timing audit reports:

- overall result: PASS;
- episodes checked: 12;
- rendered visual spot checks: 36;
- no series-wide offset;
- no progressive drift;
- no nonempty invalid cue;
- no out-of-bounds cue;
- three zero-duration empty placeholders in Episodes 09-11, classified as harmless ASS template events.

This is sufficient for dialogue-to-frame alignment during analytical review.

## 11. Episode 1 subtitle snapshot note

A small Episode 1 discrepancy exists between the subtitle copy embedded in the supplied ZIP and the separate timing-audit record.

The discrepancy is non-blocking because:

- the exact ZIP is cryptographically locked;
- episode identity is independently established;
- the episode has Japanese audio and a usable subtitle layer;
- quote-sensitive work can verify the exact locked subtitle/audio source.

The mismatch is preserved as provenance rather than erased.

## 12. 4koma integrity

The 4koma archive contains 151 images across five official series/subseries.

Its download manifest records source URLs, byte sizes, and SHA-256 hashes for the archived images.

This is sufficient for source attribution and later visual cross-checking.

## 13. Visual-assets integrity limitation

The Drive visual-assets tree clearly exposes cards, key visuals, and photos. Phase 0 does not claim a total visual-asset count because an authoritative aggregate count was not required to establish the source hierarchy.

Later formal analysis should use item-level locators or dedicated visual manifests rather than inferring completeness from folder presence alone.

## 14. Historical analysis contamination risk

Risk:

Existing Sunny Peace, Tsuki no Tempest, LizNoir, IIIX, general IDOLY PRIDE, and transcript-summary analyses could bias source selection if treated as truth.

Mitigation:

- historical analyses are hypothesis/provenance only;
- the historical curated `core-important` folder is non-authoritative;
- the V2 priority ledger is rebuilt from broad source coverage;
- load-bearing V1 claims receive explicit revision status.

## 15. Live-service staleness risk

Risk:

The game is live and will continue to add material after this audit.

Mitigation:

- freeze `IP-V2-SNAPSHOT-2026-08-13-A`;
- preserve `validated_through` on claims;
- compare future source snapshots using a delta audit;
- route new sources by Class 1/2/3 semantic impact;
- never silently mutate a frozen release.

## 16. Cryptographic baseline

Phase 0 computed SHA-256 hashes for:

- all twelve supplied anime ZIPs;
- the supplied anime extraction manifest;
- the supplied subtitle QA README;
- the supplied subtitle timing audit JSON;
- the game `source_snapshot.json`;
- the `analysis_bundles/manifest.json`;
- the `idoly-ingest/catalog.jsonl` payload;
- the 4koma `download_manifest.json`.

Hashes are recorded in the Phase 0 checksum artifact and the machine-readable source manifest.

## 17. Open integrity items

The following do not block Phase 0.5 or subsequent Phase 1 work:

1. 45 telephone references lack upstream audio.
2. 32 processed asset references are unavailable upstream.
3. Episode 1 has a small subtitle-snapshot provenance mismatch.
4. Several anime ZIP sizes differ slightly from the older extraction manifest, plausibly due to deduplication/repacking.
5. A full aggregate inventory of the visual-assets tree has not yet been generated.

No open item currently suggests narrative-corpus corruption.

## 18. Phase 0 judgment

The source corpus is **accepted for V2 analytical use**.

The project may proceed to **Phase 0.5** with the following rule. After the complete prospective anime baseline is frozen, Phase 1 begins broad game-text reconnaissance:

> The anime is first reviewed comprehensively as a bounded audiovisual work; broad game-text coverage then begins from `analysis_bundles`; exact evidentiary descent uses `idoly-ingest`; subsequent game audiovisual review is selectively escalated under the AV priority protocol; every known gap remains explicit rather than silently normalized.
