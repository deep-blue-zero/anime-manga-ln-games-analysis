---
series: BLUE_ARCHIVE
artifact_type: source_lock
scope: Promoted Japanese V1 canonical and derived source corpus
generation: V1
status: canonical
source_boundary: electricgoat/ba-data@jp cbe3fd623c2aab9e781ba0ce0483bc77c68bff86 / game-data v1.71.447596-r94_y2ha6vgythtil9ja597o; independent reference HePudding/ba-storybook@main 6c4091603ca76d7d8c3cdb9104933f52cd8cab8e
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
created: 2026-08-15
---

# BLUE ARCHIVE SOURCE LOCK V1
## Analytical-side lock for the promoted Japanese canonical corpus

## 0. Purpose

This document freezes the exact **source boundary used to begin Phase 1 literary analysis** of 『ブルーアーカイブ -Blue Archive-』.

It does not duplicate the extraction pipeline's technical manifests. Its responsibility is to answer a narrower analytical question:

> **What Japanese corpus is authorized for the V1 deep-reading project, what passed audit, what remains uncertain, and what do those uncertainties prevent the analysis from claiming?**

The extraction corpus remains in the primary-source / ingestion Drive root. Analytical artifacts cite its stable story, scene, utterance, choice, MomoTalk, character-data, person, variant, school, and club identifiers rather than copying the complete transcript tree into the analytical root.

---

# 1. Locked upstream sources

## 1.1 Primary Japanese extraction source

- repository: `electricgoat/ba-data`
- branch: `jp`
- commit: `cbe3fd623c2aab9e781ba0ce0483bc77c68bff86`
- recorded game-data version: `v1.71.447596-r94_y2ha6vgythtil9ja597o`
- source snapshot reported by the pipeline: 2026-08-12

This is the governing raw-data source for the V1 analytical generation.

## 1.2 Independent reference / parser cross-check

- repository: `HePudding/ba-storybook`
- branch: `main`
- commit: `6c4091603ca76d7d8c3cdb9104933f52cd8cab8e`

The reference snapshot is older than the primary pinned Japanese game-data snapshot. It is used for parser/reference comparison and discrepancy detection, not as an automatic override of the primary data.

## 1.3 Drive routing

Primary-source / ingestion root:

- `Blue_Archive`
- Drive ID: `1b6HBjC56XzoyEj7iLbn5CSthj-qsscl0`

Pipeline root:

- `blue-archive-corpus-pipeline`
- Drive ID: `1TZdTKLillDDcyFCHn7O0Gicx2YaHgiVF`

Canonical corpus root:

- `corpus`
- Drive ID: `1ZyZt7RFYhopnZkWCZPCluSCZURfg_Zoe`

Analytical root:

- `Blue Archive`
- Drive ID: `1kIOCMVnDdTONH8vbcodKGhKPQU4uzTIr`

---

# 2. Canonical-build lock

The promoted canonical build is:

`BA_FULL_20260816T002743Z`

Technical status: **PASS**.

Canonical object counts:

| Source class | Objects |
|---|---:|
| main | 310 |
| group | 53 |
| event | 490 |
| bond | 694 |
| mini | 5 |
| MomoTalk | 920 |
| character data | 244 |
| **total** | **2,716** |

Additional normalized counts:

- scenes: **2,047**
- utterances: **102,665**
- choice groups: **8,774**
- MomoTalk messages: **12,821**
- character contextual lines: **7,089**
- rerun event aliases consolidated without losing contexts: **9**

The promoted canonical count is the analysis-facing count. Earlier inspection-era reports contained raw/recoverable grouping counts that were useful for parser validation but should not supersede this normalized build boundary.

---

# 3. Blocking audit status

## 3.1 Stable identifiers

Stable-ID uniqueness: **PASS**.

Analytical implication:

> stable corpus IDs may be used as primary locators across sequential readings, ledgers, specialist syntheses, and later claim-revision infrastructure.

## 3.2 Sensei choice preservation

Choice audit: **PASS**.

- expected raw choice records: **8,774**
- parsed choice records: **8,774**
- choice groups: **8,774**
- missing source records: **0**
- unexpected source records: **0**

Analytical implication:

> the V1 corpus is suitable for the method's distinction among choice-space Sensei, structural Sensei, and relational Sensei. Alternative choices remain alternatives; audit completeness does not make them simultaneously spoken canon.

## 3.3 Provenance round-trip

Provenance audit: **PASS** with no failures in the sampled records.

Sample classes checked by the extraction audit:

- 200 utterances;
- 50 scenes;
- 30 choice groups;
- 30 MomoTalk sequences;
- 30 character-data records.

Analytical implication:

> sampled normalized records demonstrably route back through the pipeline's source provenance. Exact wording or disputed structural claims should still descend to the complete canonical record and raw source when needed.

## 3.4 Coverage regression

Coverage regression: **PASS**.

Analytical implication:

> the promoted corpus did not knowingly lose a previously recoverable source class during normalization.

---

# 4. Derived-build lock

The current derived build is:

`BA_DERIVED_20260816T010224Z`

Technical status: **PASS**.

Generated projections:

- character packages: **128**
- measured relationship candidates: **2,718**
- selected relationship bundles: **40**
- club packages: **47**
- school packages: **15**
- Sensei relationship packages: **128**
- main arc maps: **7**
- character context chunks: **5,154**
- relationship chunks: **2,433**
- institution chunks: **2,103**

Derived-provenance audit: **PASS**.

- sampled character-bundle sections checked: **30**
- failures: **0**
- oversized artifacts in the deterministic sharding audit: **0**

The LLM ingest map also exposes **2,047 canonical scene chunks**. Chunk text is explicitly defined by the source corpus as a reversible projection rather than a replacement for the complete Japanese story.

---

# 5. Authority of derived projections

The following rule is binding for V1 analysis:

> **Derived source packages accelerate retrieval; they do not become analytical conclusions merely because they were generated deterministically.**

## Character packages

Use them to recover:

- contextual scenes;
- dialogue evidence;
- low-stakes/MomoTalk material;
- variant crosswalks;
- linguistic baselines;
- relationship indices;
- source manifests;
- bond-story routes.

Do not equate the presence of a package with the need for a standalone analytical monograph. There are 130 literary persons but 128 current character packages; package coverage and literary-person ontology are different concepts.

## Relationship layer

`RELATIONSHIP_CANDIDATES.csv` measures corpus features including shared stories/scenes, adjacent turns, one-on-one scenes, source classes, school/club overlap, cross-school status, and Sensei presence.

These metrics do **not** directly measure:

- intimacy;
- affection;
- rivalry intensity;
- ideological opposition;
- causality;
- character-changing importance;
- whether repeated co-presence is mostly ensemble structure.

The 40 selected `BA_RELATIONSHIP_*` bundles are therefore **scene-retrieval corpora**, not an analytical top-40 relationship canon.

## Institution layer

School and club labels/memberships are backed by raw master data. Do not guess unsupported Japanese institution names.

The school projection includes core Kivotos institutions as well as crossover/external or miscellaneous categories. Institutional synthesis must classify those categories before using them to characterize Kivotos's political order.

## Sensei layer

Student-Sensei bundles are useful for relational triangulation but remain subject to choice semantics, source class, adult/student role asymmetry, and context.

## LLM ingest

Use chunks for retrieval only. Close reading and final evidence citation should return to the complete canonical scene/story whenever available.

---

# 6. Known source gaps and ambiguity

The source is sufficiently complete for Phase 1, not perfectly complete.

Current non-blocking limitations include:

1. **Seven nonempty timing/control records** remain classified as `unknown` with provenance.
2. **Overarching Japanese event titles** are unavailable for some records in the current raw localization tables; raw event IDs remain authoritative.
3. **Generic group labels** are not all institution-resolved.
4. Earlier source audits retain **unresolved/review person mappings** and **unresolved raw speaker labels**.
5. Documented upstream gaps in certain main/group records remain provenance issues unless repaired by a later pinned source generation.
6. **In-universe chronology is not globally resolved.** Release/source order is recorded where the upstream exposes dates, but documentary order must not be silently converted into diegetic chronology.

---

# 7. Analytical impact register

| Limitation | What may still be analyzed | What must not be overclaimed |
|---|---|---|
| unknown control/timing records | surrounding dialogue, scene structure, character/action content | precise staging/timing dependent on unresolved command semantics |
| missing overarching event title | event text, raw event identity, scene/episode title where present | invented canonical Japanese event-series title |
| unresolved generic group label | story content and participants | canonical club/institution identity inferred from the group label alone |
| unresolved person/speaker mapping | all securely resolved speakers and scenes | identity of the unresolved label without explicit verification |
| upstream missing main/group units | neighboring recovered material | complete textual knowledge of the missing unit |
| unresolved in-universe chronology | source/release-order reading, local causal order inside stories | total timeline or claims that `first_cooccurrence` equals first diegetic meeting |
| crossover/misc school package | the package's documented affiliation/context | treating every school package as a core Kivotos institution |

When one of these limitations bears directly on a claim, record the claim as `OPEN`, qualify confidence, or descend to another verified source rather than silently filling the gap.

---

# 8. Main-story reading boundary

The source tree exposes seven current main-story volume/arc map groupings:

- `VOLUME_000`
- `VOLUME_001`
- `VOLUME_002`
- `VOLUME_003`
- `VOLUME_004`
- `VOLUME_005`
- `VOLUME_100`

The V1 analytical project will use the canonical main-story corpus map and stable source IDs to establish the sequential reading order. Numerical scope should be preferred over invented English arc names when source nomenclature is not yet independently stabilized.

Phase 1 first-pass readings preserve the local information boundary. Later contextualization may add group, event, bond, MomoTalk, character-data, relationship, institution, and Sensei projections without rewriting the fact that the earlier story was initially ambiguous.

---

# 9. Update and supersession rule

This lock governs **V1** analysis only.

When the Japanese source advances to a later pinned commit:

- do not silently redefine this source boundary;
- create or update the source inventory for the new generation;
- compare changed/added source objects;
- update mutable current-state and ledgers;
- use the claim-transition vocabulary `PRESERVE · STRENGTHEN · REVISE · DOWNGRADE · REJECT · OPEN` where new material affects existing interpretation;
- preserve any explicitly frozen analytical release.

A new upstream snapshot does not retroactively make a V1 reading dishonest; it changes the source boundary for the next analytical generation or update.

---

# 10. Phase authorization

**Phase 0 exit condition: satisfied.**

The promoted source corpus is authorized for sequential literary analysis under `BLUE_ARCHIVE_ANALYTICAL_METHOD_V1.md`.

Next step:

> **Begin Phase 1 from the first canonical main-story unit defined by the promoted main-story corpus map, then initialize cumulative ledgers from evidence actually encountered.**
