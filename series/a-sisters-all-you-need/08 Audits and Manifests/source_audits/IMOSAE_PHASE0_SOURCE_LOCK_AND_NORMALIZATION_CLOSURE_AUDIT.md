---
series: IMOSAE
artifact_type: source_audit
scope: V01-V14_phase0_source_lock_and_normalization_closure
generation: V1
status: canonical
source_boundary: "IMOSAE-JP-LN-RAW-1.0 + IMOSAE-JP-LN-NORM-1.0-RC1 + mirrored Google Drive release candidate"
supersedes: null
superseded_by: null
do_not_use_as_current_authority: false
version: "1.0"
date: "2026-08-18"
audit_id: "IMOSAE-PHASE0-CLOSURE-AUDIT-1.0"
candidate_id: "IMOSAE-JP-LN-NORM-1.0-RC1"
promoted_release_id: "IMOSAE-JP-LN-NORM-1.0"
result: PASS
---

# IMOSAE Phase 0 Source Lock and Normalization Closure Audit
## 『妹さえいればいい。』 / *A Sister's All You Need*

## 0. Decision

**AUDIT RESULT: PASS.**

`IMOSAE-JP-LN-NORM-1.0-RC1` is promoted **without modification to its 32-file payload** as the frozen canonical normalized reading/retrieval release:

> **`IMOSAE-JP-LN-NORM-1.0`**

Phase 0 is therefore **CLOSED**. `IMOSAE_V01_DEEP_READING.md` is authorized as the next architecture-defined analytical artifact.

This promotion does **not** make the normalized layer superior to the Japanese EPUBs as textual evidence. `IMOSAE-JP-LN-RAW-1.0` remains the immutable primary-source authority; `IMOSAE-JP-LN-NORM-1.0` is the canonical loss-aware retrieval and analysis derivative. Exact wording, layout, or disputed encoding ultimately escalates to the raw EPUB.

## 1. Audit question and release rule

The closure gate asked whether RC1 could be trusted without any source-layer mutation. The rule was binary:

- **PROMOTE** only if raw-source identity, RC1 payload checksums, content classification, locator routing, annotation invariants, gaiji/visual crosswalks, round-trip evidence, and Drive mirroring all passed; or
- **REJECT** and require a new candidate if any corpus defect required changing a payload byte.

The final verifier executed **41/41 checks successfully**. No RC1 payload file was edited during audit.

## 2. Raw source-lock revalidation

The audit independently recomputed all fourteen raw EPUB SHA-256 hashes and byte sizes against `source_manifest.json`, then reran ZIP CRC validation.

| Measure | Result |
|---|---:|
| Raw EPUBs present | 14 / 14 |
| SHA-256 matches source lock | 14 / 14 |
| Byte-size matches source lock | 14 / 14 |
| ZIP CRC passes | 14 / 14 |
| Raw source bytes | **222,679,906** |
| Governing raw ID | `IMOSAE-JP-LN-RAW-1.0` |

The audit also reparsed each EPUB's `container.xml`, OPF manifest, and OPF spine and compared them to `spine_content_index.jsonl`. **All 981 OPF spine positions matched the indexed member and zero-based spine order exactly.**

## 3. RC1 payload integrity

The candidate manifest declared **32 payload files totaling 72,498,234 bytes**. The closure audit recomputed every payload file hash from disk and compared it with both `normalized_layer_manifest.json` and `normalized_layer_checksums.sha256`.

| Gate | Result |
|---|---:|
| Manifest payload files | 32 |
| Payload files present | 32 / 32 |
| Manifest byte-size matches | 32 / 32 |
| Manifest SHA-256 matches | 32 / 32 |
| Checksum ledger entries | 32 / 32 |
| Checksum ledger == manifest mapping | PASS |
| Payload bytes | **72,498,234** |
| Payload mutation during audit | **NONE** |

The exact pre-promotion RC1 manifest is preserved as `normalized_layer_manifest_RC1_pre_promotion.json` in this audit directory. Its SHA-256 is `74193178b7f0cab957a7b30fe6896a67a3f7c86545b9818d27ee2060cf1cecb8`. The current `normalized_layer_manifest.json` changes only release-state metadata; the frozen 32-file payload and `normalized_layer_checksums.sha256` remain unchanged.

## 4. Spine classification closure

All **981/981** spine items are classified. No `UNCLASSIFIED` state exists.

| Content class | Spine items |
|---|---:|
| `MAIN_NARRATIVE` | 335 |
| `ILLUSTRATION` | 305 |
| `TITLE_FRONTMATTER` | 124 |
| `PROMOTIONAL` | 108 |
| `AUTHOR_AFTERWORD` | 44 |
| `RETAILER_EBOOK_BONUS` | 27 |
| `OTHER_PARATEXT` | 14 |
| `COLOPHON` | 14 |
| `BONUS_FICTION` | 10 |

The classifier was additionally checked against raw OPF order, preventing a structurally complete but misrouted spine ledger from passing merely because its row count equaled 981.

## 5. Paragraph and locator closure

The full V01-V14 sidecar corpus was reparsed independently rather than trusting summary totals.

| Measure | Verified result |
|---|---:|
| Paragraph/block records | **34,766** |
| Unique locators | **34,766 / 34,766** |
| Surface SHA-256/fingerprint recomputations | **34,766 / 34,766 PASS** |
| Locator-index rows | **34,766** |
| Locator → sidecar line crosswalk | **34,766 / 34,766 PASS** |
| Human-readable Markdown locator coverage | **34,766 / 34,766 exactly once** |

Every locator was checked against the actual sidecar record for sidecar filename, line number, fingerprint, excerpt, and annotation counts. Every normalized Markdown volume was separately scanned to ensure its paragraph locator comments cover the same set exactly once.

## 6. Ruby, gaiji, typography, and visual invariants

| Invariant | Verified result |
|---|---:|
| Ruby annotations | **29,083** |
| Gaiji annotations | **651** |
| Raw format/style annotations | **15,175** |
| Paragraph-level illustration anchors | **552** |
| Invalid annotation ranges | **0** |
| Ruby base-text mismatches | **0** |
| Distinct frozen gaiji assets | **65** |
| Gaiji occurrence-register rows | **651** |
| Gaiji annotations inconsistent with frozen map | **0** |
| Full visual-index rows | **666** |
| Non-gaiji visual assets | **562** |
| Visual-anchor mismatches against visual index | **0** |

The audit therefore confirms that no lexically meaningful inline image disappears, ruby readings are not flattened into ordinary prose, annotation offsets remain valid, and normalized visual tokens still route to the authoritative visual index.

## 7. Round-trip evidence

`normalization_roundtrip_validation.json` contains **126 samples: 9 modes × 14 volumes**.

Required modes per volume:

`beginning · middle · end · ruby_heavy · gaiji_heavy · typography_heavy · dialogue · illustration_anchor · chapter_boundary`

**Result: 126 PASS / 0 FAIL.** Every stored sample reports both source-block hash agreement and independently normalized surface-hash agreement.

The closure verifier did not substitute this sample report for corpus-wide structural checks; it used the round-trip set as the raw-XHTML transformation check alongside the 34,766-record hash/locator audit.

## 8. Google Drive mirror audit

The paired source-tree mirror was read back through Google Drive after candidate upload.

| Drive layer | Expected | Observed | Result |
|---|---:|---:|---|
| Raw Japanese EPUBs | 14 | 14 | PASS |
| Human normalized Markdown sources | 14 | 14 | PASS |
| Paragraph JSONL sidecars | 14 | 14 | PASS |
| Payload-global records (`spine`, `locator`, validation ×2) | 4 | 4 | PASS |
| Candidate payload files | 32 | 32 | PASS |
| Release metadata (`manifest`, checksum ledger) | 2 | 2 | PASS |

All listed Drive byte sizes match the local/source manifests. To strengthen the metadata-only listing check, the audit performed authenticated exact-byte re-fetches and local SHA-256 comparisons for five high-leverage artifacts:

- `normalized_layer_manifest.json` — exact match to local **pre-promotion RC1 manifest**;
- `normalized_layer_checksums.sha256` — exact match;
- `IMOSAE_V01_NORMALIZED_SOURCE.md` — SHA-256 `0ca9147165d77f5cb62d4280b1bd44bd94309bb89a9cf19b7d6a053a91d9fef3`;
- `IMOSAE_V14_NORMALIZED_SOURCE.md` — SHA-256 `2f0745997a3e5b9ad2551004a37706b10ba2560642a6ab6edebcab61eab6e9f2`;
- `locator_index.jsonl` — SHA-256 `ebf39fc0deb4d9c910fc412c7f4f3060f2b3cbd8d187293bc2155c87a6e8e61e`.

This verifies both ends of the series, the global routing layer, and the release-control metadata by content rather than name/size alone.

## 9. Verifier self-audit / false-positive disposition

The first dry run of the newly written closure verifier produced four apparent failures. **No corpus file was changed in response.** Each was investigated before any authority decision:

1. locator excerpts were generated at 120 characters, while the first verifier draft incorrectly expected 160;
2. the visual index intentionally contains 104 `GAIJI_INLINE_IMAGE` package rows, so filtering merely on presence of `visual_id` incorrectly counted gaiji entries as non-gaiji visuals;
3. existing validation includes numeric zero-valued success fields (`unclassified_spines: 0`, `duplicate_locators: 0`), which the first verifier draft naïvely treated as boolean false;
4. the raw source manifest uses the more specific status string `canonical_raw_source_lock`, not literal `canonical`.

After correcting **the verifier only**, the complete closure suite returned **41/41 PASS**. This matters because promotion is explicitly of the **unchanged RC1 payload**, not a candidate silently repaired during its own audit.

## 10. Final closure-check ledger

| Check | Result |
|---|---|
| `raw_source_14_files_present` | PASS |
| `raw_source_sizes_match_lock` | PASS |
| `raw_source_hashes_match_lock` | PASS |
| `raw_source_zip_crc_pass` | PASS |
| `spine_index_matches_raw_opf_order` | PASS |
| `spine_count_981` | PASS |
| `spines_all_classified` | PASS |
| `candidate_manifest_id_rc1` | PASS |
| `candidate_manifest_32_files` | PASS |
| `candidate_files_all_present` | PASS |
| `candidate_file_sizes_match_manifest` | PASS |
| `candidate_file_hashes_match_manifest` | PASS |
| `candidate_total_bytes_match_manifest` | PASS |
| `checksum_file_exactly_matches_manifest` | PASS |
| `paragraph_count_34766` | PASS |
| `locators_unique_34766` | PASS |
| `surface_hashes_and_fingerprints_valid` | PASS |
| `paragraph_source_and_spec_ids_consistent` | PASS |
| `annotation_ranges_and_ruby_base_valid` | PASS |
| `ruby_count_29083` | PASS |
| `gaiji_count_651` | PASS |
| `format_annotation_count_15175` | PASS |
| `illustration_anchor_count_552` | PASS |
| `gaiji_annotations_match_frozen_map` | PASS |
| `illustration_anchors_match_visual_index` | PASS |
| `locator_index_34766_rows` | PASS |
| `locator_index_exact_sidecar_crosswalk` | PASS |
| `normalized_markdown_contains_all_34766_locators_once` | PASS |
| `gaiji_map_65_distinct_assets` | PASS |
| `gaiji_occurrence_register_651` | PASS |
| `gaiji_occurrence_ids_unique` | PASS |
| `gaiji_occurrence_assets_all_in_map` | PASS |
| `visual_index_666_rows` | PASS |
| `visual_index_562_non_gaiji_stable_ids` | PASS |
| `existing_validation_all_flags_pass` | PASS |
| `roundtrip_126_samples_present` | PASS |
| `roundtrip_126_pass_0_fail` | PASS |
| `roundtrip_all_14_volumes_have_9_required_modes` | PASS |
| `manifest_source_set_id_correct` | PASS |
| `manifest_normalization_spec_id_correct` | PASS |
| `source_manifest_status_canonical` | PASS |

## 11. Authority transition

Effective with this audit:

| Layer | Authority state |
|---|---|
| `IMOSAE-JP-LN-RAW-1.0` | **canonical / immutable primary source** |
| `IMOSAE-NORM-SPEC-1.0` | **canonical normalization specification** |
| `IMOSAE-GAIJI-MAP-1.0` | **canonical gaiji mapping** |
| `IMOSAE-VISUAL-INDEX-1.0` | **canonical visual/paratext routing layer** |
| `IMOSAE-JP-LN-NORM-1.0-RC1` | **historical release-candidate identity; payload promoted unchanged** |
| `IMOSAE-JP-LN-NORM-1.0` | **canonical / frozen normalized source release** |

The per-volume normalized Markdown files retain their build-time `status: active_provisional` front matter so the verified payload remains byte-identical to RC1. **Do not interpret those embedded build-state labels as current authority.** Current authority is controlled by this closure audit, `normalized_layer_manifest.json`, `IMOSAE_NORMALIZED_READING_LAYER_AND_LOCATOR_REGISTER.md`, and `CURRENT_STATE_AND_CORPUS_MAP.md`.

## 12. Immutability and correction policy

`IMOSAE-JP-LN-NORM-1.0` is now frozen. Do not silently regenerate, normalize, reflow, relabel, or overwrite any of its 32 payload files. If a future reading discovers a genuine normalization defect, record the defect and issue a later normalized release rather than mutating 1.0 in place.

The raw EPUBs remain separately frozen as `IMOSAE-JP-LN-RAW-1.0`; a corrected normalized release would normally continue to point to the same raw source set unless the raw-source lock itself is explicitly superseded.

## 13. Phase transition

**Phase 0 status: CLOSED / PASS.**

**Next architecture-defined artifact:**

> `IMOSAE_V01_DEEP_READING.md`

The Volume 1 reading should use the frozen normalized layer for retrieval, ruby/gaiji/typography/visual routing, and deterministic locators, while escalating exact textual disputes to `A Sister's All You Need - Volume 01 [Japanese].epub` under `IMOSAE-JP-LN-RAW-1.0`.
