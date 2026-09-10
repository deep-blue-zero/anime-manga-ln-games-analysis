---
title: "Gakuen Idolmaster V2 File Organization Audit — 2026-09-09"
series: GKM
artifact_type: audit
scope: SERIES_FILE_ORGANIZATION_AND_RETRIEVAL
generation: V2
status: canonical
source_boundary: "Read-only structural inventory of the 350-file GKM tree at 19266f2a2cb47e177941fbc766559294746a1442; recovery integration and subsequent organization proposals are distinguished below"
audit_baseline_commit: "19266f2a2cb47e177941fbc766559294746a1442"
reconciled_creation_base_commit: "e0d07a6cc4709d6e3be562a273b2a947b4ff0fe3"
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
created: "2026-09-09"
last_updated: "2026-09-09"
---

# File organization audit

The established directory structure is serviceable. Its principal weakness is inconsistent retrieval routing, rather than redundant analytical content. Preserve existing homes, package identities, and distinct historical generations. Use the [AV file index](../05_AUDIOVISUAL_ANALYSIS/GKM_AUDIOVISUAL_FILE_INDEX.md) to navigate the character packages and the [current-state map](../CURRENT_STATE_AND_CORPUS_MAP.md) for project state.

## Scope and baseline

This audit inspected file placement, duplicate content, package aliases, archive boundaries, and current versus historical routing. It did not rewatch source media, repeat source-unit analysis, or certify live availability of external files.

The pre-integration baseline contains **350 files in 62 directories**, with **no empty directories**. The GKM tree remained identical when current repository governance was reconciled at `e0d07a6cc4709d6e3be562a273b2a947b4ff0fe3`. These are historical baseline counts; recovered files and the new audit/index increase the integrated inventory. Git's selected tree is the live path inventory.

| Check | Baseline result | Interpretation |
| --- | --- | --- |
| Exact byte duplicates | One pair | Documented Rinami package aliases |
| Markdown body duplicates after removing front matter | None | No duplicate analytical prose identified by this test |
| Equivalent JSON after normalizing key order | None | No duplicate structured payload identified by this test |
| Same-name Temari current/predecessor documents | Five pairs; every pair differs substantively | Distinct generations, not disposable copies |
| Empty directories | None | No empty future-phase scaffolding to remove |

These checks identify exact equivalence, not all possible conceptual overlap. Shared source coverage across a core, evidence matrix, specialist reading, and cumulative ledger is an intentional separation of responsibilities.

## Existing homes and legitimate asymmetries

All 13 integrated baselines occupy their numbered character homes under `05_AUDIOVISUAL_ANALYSIS/00_MUSICAL_IDENTITY_BASELINES/`. Dialogue and music specialists use two established arrangements:

- Saki, Temari, Kotone, Mao, Lilja, China, Rinami, and Ume use the separate dialogue/music role directories.
- Hiro, Sumika, Misuzu, Sena, and Tsubame keep both specialists with their character baseline.
- Lilja's music specialist sits directly in `02_MV_AND_VISUAL_PERFORMANCE_CLOSE_READINGS/`; its unique filename and the new index provide an explicit route.

Saki, Temari, and Kotone keep nine AV administrative files—their completion reports, delivery audits, and internal checksum manifests—in their textual-core homes. The other ten characters keep those controls in the AV baseline homes. All 13 AV revision addenda belong with the textual cores they qualify. These differences warrant links, not a mass move.

The archive homes also have distinct responsibilities:

| Home | Preserved responsibility | Disposition |
| --- | --- | --- |
| `90_LEGACY_V1_ANALYSIS/` | V1 conversation evidence | Retain as historical hypothesis/provenance |
| `90 Legacy and Superseded/TEMARI_AV_PREDECESSOR_GENERATION_20260815/` | Five documents at the audit baseline; recovery adds the predecessor evidence matrix and music JSON | Retain with explicit noncurrent/successor routing |
| Rinami `90_SUPERSEDED_RELEASES/` | R1 supersession note and outer checksum sidecar | Retain immutable release provenance |
| `10_RELEASE_MANIFEST_AND_ARCHIVE/` | Historical release identities and handoff | Retain; future Phase-10 closure is a separate responsibility |

The architecture's section titled “Proposed Google Drive / archive directory tree” is an illustrative earlier layout. Its numbering and names differ from the established Git tree. The source-facing, ledger, AV, and synthesis responsibilities are already represented under their actual homes. Missing proposed directories do not establish missing analysis or authorize new scaffolding.

## Duplicate and staging dispositions

Rinami's [named source inventory](../05_AUDIOVISUAL_ANALYSIS/00_MUSICAL_IDENTITY_BASELINES/08_HIMESAKI_RINAMI/SUPPORTING_DATA/GKM_PHASE3_RINAMI_SOURCE_INVENTORY.tsv) and [source-manifest TSV](../05_AUDIOVISUAL_ANALYSIS/00_MUSICAL_IDENTITY_BASELINES/08_HIMESAKI_RINAMI/SUPPORTING_DATA/source_manifest.tsv) are byte-identical. Both names are explicitly listed with the same original hash in the [R2 artifact manifest](../05_AUDIOVISUAL_ANALYSIS/00_MUSICAL_IDENTITY_BASELINES/08_HIMESAKI_RINAMI/GKM_PHASE3_RINAMI_AV_ARTIFACT_CHECKSUMS.sha256). Retain them as package aliases unless a separately reviewed migration supplies replacement routing and preserves provenance.

Misuzu's [_WORK inventory](../05_AUDIOVISUAL_ANALYSIS/00_MUSICAL_IDENTITY_BASELINES/11_HATAYA_MISUZU/_WORK_MISUZU_AV_INVENTORY.md) is an unreferenced six-line staging file reporting `Total: 0`. It is not an alternative completed source manifest. Explicit noncurrent classification is a later bounded cleanup candidate; this audit does not delete or reconstruct it.

## Recovery integration versus later proposals

The companion [recovery integration](../10_RELEASE_MANIFEST_AND_ARCHIVE/GKM_RECOVERY_INTEGRATION_AUDIT_20260909.md) adds eligible recovered evidence, makes Temari's preserved predecessor authority explicit, adds the AV file index, and labels obsolete next-step statements as historical. The current-state map also qualifies Hiro and Misuzu's technical-documentation completion through the [prospective rebuild register](GKM_TARGETED_REBUILD_CANDIDATES.md). It does not implement a broad directory reorganization or perform those rebuilds. Historical ZIP members and source hashes continue to describe their original release bytes and paths; the [integration manifest](../10_RELEASE_MANIFEST_AND_ARCHIVE/GKM_RECOVERY_INTEGRATION_MANIFEST_20260909.json) records original members, hashes, repository destinations, and declared transformations without rewriting frozen checksums.

The following dispositions distinguish the routing correction made in this integration from proposals that remain separately reviewable:

| Priority | Baseline finding | Integration disposition or bounded later action |
| --- | --- | --- |
| High | The current-state map's “Immediate next work” and several later checkpoints used operative “current/next” wording for completed event, support, or Rinha-matrix work | **ADDRESSED IN THIS INTEGRATION:** obsolete instructions are explicitly historical; the first-read status and final Phase-6 checkpoint retain the targeted Rinha AV operation as current |
| High | The governing method and synthesis architecture are classified `UNCLASSIFIED_LEGACY`, rather than current-eligible, by repository authority rules | Reconcile their artifact authority metadata or approved authority wrappers before adding new sequential readings; do not change governance to bypass the existing gate |
| Medium | The ledger index lists 16 responsibilities and omits the external-paratext register; existing schema locations are not explicitly linked | Complete [ledger-index](../04_CUMULATIVE_LEDGERS_AND_INDICES/GKM_LEDGER_INDEX_AND_SCHEMAS.md) routing to the 17 responsibilities and schemas already maintained elsewhere |
| Low | The architecture's proposed Drive layout can be mistaken for the current Git topology | Annotate its illustrative status and link the actual current-state route |
| Low | The Misuzu staging inventory has no explicit noncurrent metadata | Classify its working/provenance role without promoting empty data into evidence |

The method/architecture eligibility finding is a prospective continuation constraint. It does not invalidate preserved earlier readings or make this audit, a retrieval index, or recovery provenance into new sequential analysis. The governing documents remain [method v2.2](../00_ANALYSIS_FRAMEWORKS/GAKUEN_IDOLMASTER_FULL_CORPUS_ANALYTICAL_METHOD_V2.md) and [architecture v2.4](../00_ANALYSIS_FRAMEWORKS/GAKUEN_IDOLMASTER_MULTI_DOCUMENT_SYNTHESIS_ARCHITECTURE_V2.md).

## Preservation boundary

No move, deletion, folder merge, filename standardization, or reanalysis is authorized by this audit's recommendations alone. Preserve the separate legacy scopes, documented aliases, AV revision bridges, and numbered character homes. Recover absent eligible members into those homes; retain older ledger and current-map snapshots as release provenance instead of overwriting their evolved live counterparts.
