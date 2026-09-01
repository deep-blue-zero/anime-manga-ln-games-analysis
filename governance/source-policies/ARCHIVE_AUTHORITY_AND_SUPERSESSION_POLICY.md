---
title: Manga / Anime Archive Authority and Supersession Policy
artifact_id: MANGA_ANIME_AUTHORITY_POLICY
version: 1.0
status: CANONICAL
scope: corpus-wide archive management and retrieval
created: 2026-08-15
maintainer: ChatGPT + user
do_not_use_as_literary_evidence: true
---

# Manga / Anime Archive Authority and Supersession Policy

## Governing principle

> **The archive's primary retrieval problem is authority resolution, not storage volume.**

Preserve the history of interpretation, but make it computationally and visually difficult for an obsolete analytical state to masquerade as the present one.

This policy governs `MANGA_ANIME_DRIVE_INDEX.md`, series-level corpus maps, analytical artifacts, legacy material, conversation archives, and maintenance passes across the Manga / Anime Drive hierarchy.

## 1. Authority states

Every durable analytical artifact should converge toward one of four explicit states:

- **CANONICAL** — preferred current interpretation or routing surface.
- **ACTIVE / PROVISIONAL** — current work that may still change.
- **SUPERSEDED** — preserved for provenance but not current authority.
- **HISTORICAL / LEGACY** — previous analytical state retained for comparison, recovery, or intellectual history.

Dates and modification timestamps are not authority states.

Recommended front matter:

```yaml
status: SUPERSEDED
superseded_by: 07_ETHICS_REVENGE_AUTONOMY_AND_LOVE.md
do_not_use_as_current_authority: true
```

For current artifacts:

```yaml
status: CANONICAL
authority_generation: v2
source_boundary: "Japanese LN Volumes 1-10"
current_as_of: 2026-08-15
```

## 2. One canonical retrieval surface per series

Every mature or actively maintained series should have one first-read document answering:

> **What should an agent read first right now?**

Preferred filenames:

- `00_README_AND_CORPUS_MAP.md` for stable or released corpora;
- `CURRENT_STATE_AND_CORPUS_MAP.md` for active projects;
- an existing equivalent may be retained if it clearly performs the same function.

That surface should state:

1. current authoritative generation/version;
2. current source boundary;
3. current specialist syntheses;
4. current evidence/revision ledger;
5. legacy/superseded material locations;
6. project state: complete, frozen, provisional, or actively progressing;
7. the next architecture-defined step for active projects.

## 3. Retrieval order

Authority resolution precedes topical similarity.

Use:

> **semantic hit -> authority/supersession check -> series current surface -> specialist/sequential analysis -> evidence/revision ledger -> primary source**

If semantic search surfaces an older artifact with stronger lexical similarity, do not treat it as current until the series current surface and the master Authority Overrides registry have been checked.

## 4. Claim transition vocabulary

Reread and V1-to-V2 projects should use the following standardized claim states:

- **PRESERVE**
- **STRENGTHEN**
- **REVISE**
- **DOWNGRADE**
- **REJECT**
- **OPEN**

Recommended ledger schema:

| Claim ID | Earlier claim | Status | Current formulation | Current authority | Evidence route |
|---|---|---|---|---|---|

A claim ledger is core retrieval infrastructure, not optional project administration.

## 5. Legacy retention rule

> **Delete redundant artifacts; deprecate superseded thinking.**

Old analysis should usually be retained when it records a materially different interpretive state. It remains useful for:

- provenance;
- intellectual history;
- claim revision;
- reconstruction of why a conclusion changed;
- recovery of reasoning accidentally omitted from later synthesis.

Preferred legacy hierarchy:

```text
90 Legacy and Superseded/
    Conversation Archives/
```

Equivalent already-established structures such as `90 V1 Historical Analysis`, `90_LEGACY_V1_ANALYSIS`, or `00 Legacy V1 Provenance` are valid and should not be reorganized merely for cosmetic uniformity.

## 6. Misleading legacy filenames

Legacy files containing terms such as `Authoritative`, `Definitive`, `Comprehensive`, or `Full-Series Synthesis` are retrieval hazards after supersession.

Preferred mitigations, in descending order:

1. move them into a clearly marked legacy/superseded layer;
2. add explicit supersession front matter;
3. rename with `LEGACY_V1__` or an equivalent prefix when renaming will not break checksum/manifests or external references.

Do not rename immutable release members if doing so would invalidate checksums or archival manifests; use directory placement and routing metadata instead.

## 7. Conversation archives

Once a structured V2 corpus exists, full chat transcripts are cold-storage provenance.

Recommended notice:

> Historical conversational record. Useful for provenance and recovery of lost reasoning. Do not prefer over the current structured analytical corpus.

Long transcripts should not be preferred analytical sources because they frequently contain early speculation, abandoned hypotheses, corrections, and final conclusions in the same semantic object.

## 8. Redundancy and deletion

Safe deletion candidates include:

- byte-identical duplicates;
- duplicate folders caused by connector retries;
- abandoned temporary copies;
- obsolete provisional manifests after a verified frozen manifest exists;
- redundant archive packages;
- phase-handoff artifacts whose entire informational content is incorporated into the canonical current surface.

Before deletion, verify both identity/redundancy and that no current corpus map, manifest, checksum, or external route depends on the target.

**Old is not synonymous with redundant.**

## 9. Topical-home rule

Durable new conclusions should normally update their established topical home or a revision ledger rather than create another near-final synthesis.

Create a new free-standing synthesis only when the governing architecture calls for it or when the new analytical object genuinely has an independent scope.

## 10. Project-source / bookmark layer

The lightweight project-source layer should function as a high-precision router, not a historical archive.

Prefer retaining:

- `MANGA_ANIME_DRIVE_INDEX.md`;
- current per-series corpus maps where useful;
- durable cross-project conventions not represented elsewhere.

De-emphasize obsolete V1 conclusions, intermediate phase summaries, temporary source inventories, superseded current-state claims, and duplicated summaries already represented in canonical Drive artifacts.

## 11. Maintenance-pass requirements

Each master-index maintenance pass should check, where practical:

1. whether each active/mature series still has one clear current retrieval surface;
2. whether that surface identifies current authority and source boundary;
3. whether new V2/deep-reading work supersedes an older artifact;
4. whether revision/claim ledgers have advanced;
5. whether misleading legacy files have entered current folders;
6. whether conversation transcripts are being used as preferred current sources;
7. whether duplicate folders/files were created by connector retries;
8. whether a frozen release has made provisional manifests redundant;
9. whether the Authority Overrides registry in the master index needs revision.

## 12. Change-control rule

Do not perform broad destructive reorganization automatically.

Safe automatic/maintenance actions:

- update current-state routing metadata;
- add or update authority registry entries;
- create missing legacy containers when a supersession relationship is already verified;
- move clearly version-marked legacy artifacts out of a current-release directory after verifying parents and current replacements;
- preserve Drive IDs when updating canonical text artifacts in place.

Actions requiring stronger verification before execution:

- renaming immutable release members;
- deleting non-identical analysis;
- moving files referenced by manifests/checksums;
- declaring a work superseded without a verified successor;
- rewriting historical analytical prose merely to conform to current terminology.

