---
series: ASCENDANCE_OF_A_BOOKWORM
artifact_type: evidence_index_router
scope: CROSS_VOLUME_EVIDENCE_AND_LOCATOR_ROUTING
generation: V0.1
status: canonical
release_state: mutable_active
architecture_lifecycle: INITIAL
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
---

# Ascendance of a Bookworm evidence-and-index router

This directory is the canonical future home for cross-volume evidence-retrieval structures that become necessary after local deep-reading locators are no longer sufficient.

At the pre-V01 boundary, **no dedicated cross-volume evidence index is required yet**. Source-file integrity and inventory live in `../01 Source Lock and Inventory/BOOKWORM_SOURCE_LOCK_AND_INVENTORY.md` and the governed Drive audit manifest; passage-level analytical evidence will initially live in the relevant sequential reading.

## Initial evidence route

```text
source-file identity / SHA-256
        -> source lock + Drive audit manifest
passage-level observation
        -> relevant BOOKWORM_VNN_DEEP_READING.md
current cumulative claim state
        -> BOOKWORM_MASTER_LONGITUDINAL_LEDGER.md
wording-sensitive Japanese evidence
        -> bounded quotation/description + source locator in the claim-bearing artifact
```

The goal is deterministic retrieval, not maximal duplication.

## Promotion threshold

Create an evidence/index artifact when one or more of the following become true:

- mature claims repeatedly need exact retrieval across multiple volumes;
- Japanese terminology, titles/forms of address, or wording-sensitive evidence accumulates independently;
- source coverage or claim coverage can no longer be audited reliably from individual readings;
- a specialist synthesis requires a reusable cross-volume evidence matrix;
- claim revision becomes dense enough to warrant a dedicated machine- or human-readable ledger;
- source locators have a stable schema that reduces repeated manual reconstruction.

Do not create an index merely to mirror another project.

## Candidate artifacts

Possible future homes include:

- `BOOKWORM_PRIMARY_SOURCE_LOCATOR_INDEX.tsv` — cross-volume source locators for major reusable evidence;
- `BOOKWORM_JAPANESE_TERMINOLOGY_AND_ADDRESS_INDEX.md` — wording, titles/forms of address, register, and translation-sensitive terms with source boundaries;
- `BOOKWORM_ANALYTICAL_COVERAGE_MATRIX.md` — source-unit coverage against mature analytical responsibilities;
- `BOOKWORM_CLAIM_REVISION_LEDGER.md` — only if claim state outgrows the master longitudinal ledger;
- a contradiction/evidence matrix when a specialist or final synthesis requires adversarial cross-volume adjudication.

These names are architectural candidates, not mandatory files.

## Source-byte boundary

Do not track the Japanese EPUBs, bulk extracted primary-source text, acquisition evidence, or a redundant copy of the complete 34-file checksum inventory in this directory.

The source audit manifest remains the canonical per-file integrity ledger in the governed primary-source evidence plane. Git should store only the analytical/provenance structure necessary to route claims back to that evidence.

Where bounded Japanese quotation is analytically necessary, keep it proportional to the claim and preserve a locator rather than reproducing large source passages.

## Relationship to longitudinal state

Evidence indexes answer **where the basis can be found**. Longitudinal ledgers answer **what the current analytical state is**. Do not duplicate the same current interpretation in both layers.

If a claim-revision ledger is eventually split into this directory, `../03 Longitudinal Ledgers/BOOKWORM_MASTER_LONGITUDINAL_LEDGER.md` should route to it rather than maintaining a competing detailed claim state.

## Current state

```yaml
evidence_index_layer:
  current_source_boundary: PRE_V01
  promoted_indexes: []
  source_integrity_home: ../01 Source Lock and Inventory/BOOKWORM_SOURCE_LOCK_AND_INVENTORY.md
  passage_locator_home: sequential_reading_local_until_promotion
  cross_volume_retrieval_pressure: none_yet
```
