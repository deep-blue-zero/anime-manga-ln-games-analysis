---
title: "Classroom of the Elite — Evidence Reconciliation Audit, Y1V08–Y1V10"
artifact_type: "checkpoint_evidence_provenance_audit"
checkpoint_id: "Y1-CP03"
version: "1.0"
status: "PASS"
source_boundary: "Y1V08–Y1V10"
cumulative_boundary: "Y1V01–Y1V10"
spoiler_boundary: "through Y1V10 only"
created_at: "2026-08-12"
updated_at: "2026-08-12"
result: "PASS_AFTER_ADMINISTRATIVE_INDEX_SOURCE_MAP_AND_CLASS_POLITY_REPAIRS"
---

# Evidence reconciliation and provenance audit
## `Y1V08–Y1V10`

# 1. Audit result

**PASS_AFTER_ADMINISTRATIVE_INDEX_SOURCE_MAP_AND_CLASS_POLITY_REPAIRS**

No canonical literary conclusion, evidence claim, Japanese passage, or volume-local spoiler boundary required correction. The repairs concerned active administrative metadata and retrieval infrastructure.

# 2. Canonical volume verification

| Code | Words | Bytes | Evidence rows | Artifact SHA-256 | Source SHA-256 | Normalized-text SHA-256 |
|---|---:|---:|---:|---|---|---|
| `Y1V08` | 17,801 | 135,527 | 152 | `d67fbdbffa165fe17d1bfdff3fd2d1cd65b31e13f21d58937063e2b49f6d9ba3` | `70fe11cf8145e97fcf17ea817f326d43ac0fe213b6ffeec7ee532acbd83ebb8e` | `a67725eb41238b1878ef4a2795fd91fc93fa2367d9374bae3af9bccc5f98df8a` |
| `Y1V09` | 14,361 | 103,977 | 110 | `4679597e4830718dfe39cc7cec059fe977ff567085ee37b4eaaad80d7703ef8a` | `0f615a16f03db32930f0a24ba41778fff30d5b1d8a4d21df625757fae576eaca` | `1fe037048c9cf5869dd7c387fe81ef7ba0f26dedb4b5579dd6e38bd22317b42c` |
| `Y1V10` | 17,134 | 125,862 | 123 | `b31c55f57159482db824b15aea1a493cd7de4527f3e98d742f9dfbe99172c090` | `2b3b83b5281ef7bdeb320bb9d0c24f58b67be044fda02724c3683b32fdc4d1e5` | `8c1d43dde96ffa772361b7d9c399ddda9321ff2019c8a379caa4ceed8c751d8c` |


- Evidence IDs are sequential and unique in all three artifacts.
- Artifact evidence union: **385/385** expected.
- Cumulative evidence ledger: **1,037/1,037** unique canonical IDs.
- Missing tranche IDs: **0**.
- Unexpected tranche IDs: **0**.

# 3. Locator verification

| Locator class | Validated | Errors |
|---|---:|---:|
| Text | 356 | 0 |
| Visual | 29 | 0 |
| **Total** | **385** | **0** |

Each text locator was checked against the frozen source-specific spine path and paragraph count. Each visual locator was checked against the source image inventory or verified image-count range. The audit preserves the source-specific index convention:

- `Y1V08`: zero-based spine indices;
- `Y1V09`: zero-based spine indices;
- `Y1V10`: one-based spine indices.

These differences are recorded in the source map rather than silently normalized after the fact.

# 4. Japanese terminology/passages

The rolling Japanese index contains **225** table entries. The checkpoint confirmed that its YAML count, actual table count, current thematic-ledger link, and Y1V10 boundary agree.

Tranche contributions:

| Volume | Entries |
|---|---:|
| `Y1V08` | 30 |
| `Y1V09` | 24 |
| `Y1V10` | 25 |

# 5. Administrative repairs

The following stale states were corrected and recorded:

1. **Source map** — CP01 deterministic entries were restored for V01–V04.5; CP02 entries were preserved for V05–V07.5; V08–V10 changed from `pending_sequential_pass` to complete deterministic maps with normalized fingerprints, spine documents, paragraph counts, index bases, and locator notes.
2. **Source inventory** — analytical boundary advanced from V09 to V10; V10 changed from planned to complete; V10 source notes added.
3. **Project status** — advanced from V09 to reconciled V10 with V11 as next source.
4. **Corpus index** — rebuilt from the active filesystem because the previous machine-readable index still reported V01 as the completion boundary.
5. **Class-polity ledger** — advanced from V09 to V10 and frozen in a checkpoint-specific snapshot.
6. **Evidence and terminology metadata** — checkpoint status advanced from CP02/post-checkpoint to CP03 complete.
7. **Artifact checksum registry** — rebuilt across all active non-work artifacts; the prior file contained only a stale subset.

# 6. Spoiler-boundary audit

The checkpoint reports, frozen ledgers, source maps, and package were scanned for later-source leakage. They do not answer:

- the outcome of the next special examination;
- the exact nature of Tsukishiro’s subsequent operation;
- the fate of the Protection Point;
- Hirata’s later recovery;
- later relationship outcomes;
- *First File* retrospective framing;
- any Year 2 or Volume 0 revelation.

# 7. Package policy

The checkpoint package contains no Japanese EPUB, extracted source text, raster source image, or other copyrighted primary-source payload. It includes only analytical artifacts, metadata, source fingerprints, deterministic source maps, and audit files.

# 8. Conclusion

The third tranche is internally consistent, deterministically recoverable, and safe to use as the evidence boundary before `Y1V11` begins.
