---
series: WUWA
character: Chisa
lore_entity_id: wuwa:lore-entity:chisa
artifact_type: character_baseline_reconciliation
analytical_responsibility: Retrieved report-level continuity, corrections, and comparison limits.
scope: CHISA_SOURCE_3_6_0_PRE_AV_REBUILD
analysis_generation: CHISA_PRE_AV_REBUILD_V0_1
generation: V0.1
status: active_provisional
release_state: current_provisional_pre_av
authority_state: owner_adopted_current_provisional
source_generation_frozen: true
source_boundary: Pinned 3.6.0 normalized semantic evidence; supplied installed-client voice metadata; no direct
  AV or raw-audio review in this rebuild.
source_generation: arikatsu-3.6.0-353f2eae-expanded-v0.3.0-ko
source_commit: 353f2eaed119bc9f680eab92807d20ac75a79b40
text_authority: zh-Hans
localization_witnesses:
- en
- ja
- ko
localization_review_scope: CN contextual pass; CN/EN archive pass; selected EN/JA/KO semantic checks.
method_state: Owner-adopted local AV amendments and recent packet practices; current Git adoption not certified.
intended_canonical_home: series/wuthering-waves/04 Character Analysis/Chisa/WUWA_CHISA_PRIOR_BASELINE_AND_SOURCE_RECONCILIATION.md
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
created: '2026-09-06'
authority_adoption: owner_2026_09_09_text_audio_baseline
---

> **Current authority — owner adoption, 2026-09-09.** This document is current `active_provisional` authority for its declared analytical or planning scope and inspected text/audio evidence. AV and other stated gaps limit the corresponding claims, not the entire model. Original local-draft and future-publication statements below describe preparation history. Coverage and completion claims remain as recorded; plans and probes are not observations. See the [adoption record](../../08%20Audits%20and%20Manifests/WUWA_CHARACTER_PACKET_AUTHORITY_ADOPTION.md).

# Chisa -- Prior-Baseline and Source Reconciliation

## Scope of this comparison

This document records what the rebuild preserves, expands, corrects, or leaves unresolved relative to the retrieved Chisa smoke-test reports. It is not a certified diff against current Git `main`, and it does not claim access to the complete earlier monograph or compiled character model.

The historical comparison inputs are `WUWA_CHISA_SOURCE_COVERAGE_AND_IDENTITY.md`, `WUWA_CHISA_SMOKE_TEST_COMPLETION_REPORT.md`, and the readable `WUWA_CHISA_EVIDENCE_BRIDGE.md`. The first two are retained locally without alteration and included in the README's input-hash table. The bridge routes to several analytical files not recovered in this rebuild. Their existence in a routing table is not equivalent to having read their contents.

Accordingly, an expansion below means expansion beyond the *retrieved report-level summary*, not proof that an unseen earlier monograph lacked the point. The complete source re-reading, claim register, and specialist profiles are new local artifacts with their own identities. No historical file has been overwritten or declared superseded.

## 1. Revision register

| ID | Earlier report-level position | Rebuild disposition | Basis and remaining limit |
|---|---|---|---|
| CHISA-R01 | Exceptional structural perception is held in tension with a desire for ordinary life. | PRESERVE / REFINE | The new thesis makes particular care and inhabitable ordinary time central, rather than treating perception and ordinary life as simple opposites. [CHISA-E01, CHISA-E17, CHISA-E52] |
| CHISA-R02 | Chisa moves from defensive self-effacement toward chosen participation. | PRESERVE / EXPAND | Later friendships, hosting, educational choices, and gratitude give that movement concrete forms. It does not prove complete security under refusal or failure. [CHISA-E26, CHISA-E31, CHISA-E35, CHISA-E45] |
| CHISA-R03 | Her constraints are not magically cured. | PRESERVE / SPECIFY | Acute convalescent findings, earlier face-recognition difficulty, subjective confidence, and power limitations remain separate. [CHISA-E03, CHISA-E04, CHISA-E22, CHISA-E23, CHISA-E39] |
| CHISA-R04 | The doctor's description is an in-source term rather than an independent diagnosis. | PRESERVE | The new perception profile additionally separates institutional hypotheses from observed behavior and from Chisa's own beliefs. [CHISA-E01, CHISA-E03] |
| CHISA-R05 | A five-phase continuity model runs from pre-Honami student life to Academy continuation. | EXPAND, NOT CLAIMED REFUTATION | The local model separates childhood, monitored adolescence, the first Academy period, Honami, convalescence, renewed participation, and the later farewell. These are useful analytical divisions, not new lore identities. |
| CHISA-R06 | The 733 accepted occurrences exclude all 18 generic candidates. | PRESERVE / RECOMPUTE | The supplied occurrence records support the same membership count. An unknown rejected speaker does not become Chisa merely because its own identity remains open. [CHISA-E60] |
| CHISA-R07 | All 607 semantic voice lines have complete media coverage. | PRESERVE WITH SCOPE | The supplied line records support the mapped four-language coverage; this rebuild does not independently re-decode every underlying recording. [CHISA-E60] |
| CHISA-R08 | 2,429 render variants are also 2,429 distinct canonical-PCM FLAC objects; no deduplication occurs. | CORRECT | There are 2,429 associations but 2,421 distinct supplied PCM/FLAC identities. Eight excess associations arise from two reused archive/event recordings in each of four languages. See section 2. |
| CHISA-R09 | Human performance remains open; no arbitrary listening cohort is required. | PRESERVE | Specific listening questions are nominated only as optional future work. Raw voice coverage and aggregate signal data do not establish acting. |
| CHISA-R10 | Selected AV was optional where a claim required staging evidence. | EXTEND UNDER OWNER-ADOPTED LOCAL METHOD | The new packet includes claim-driven nomination and a human-retrieval crosswalk. Direct review remains unperformed, and media symmetry is not mandatory. |
| CHISA-R11 | Rival readings and counterevidence are part of the packet. | EXPAND | The new matrix contains 50 claims and 60 evidence bundles, while the non-blind fidelity review includes 36 probes. These counts do not establish greater correctness by themselves. |
| CHISA-R12 | Romance-coded affordances are not relationship-state facts. | PRESERVE / STRENGTHEN CONTROLS | Explicit friendship, optional message branches, group meals, and separate educational futures constrain claims of compulsory exclusivity. [CHISA-E37, CHISA-E46, CHISA-E47] |
| CHISA-R13 | The bridge is a deterministic route to evidence and analytical material. | PRESERVE ROUTING / FLAG RETRIEVAL LIMIT | The source and voice routes were used; references to an old monograph or model were not treated as readable content. No current-main authority comparison is certified. |
| CHISA-R14 | No particular account of later disclosure, peer recognition, or graduation is summarized. | ADD REPORT-LEVEL DETAIL | Later residents' knowledge, reciprocal Lynae friendship, thesis permission, and Rover's rather than Chisa's graduation are now independently source-routed. Absence from a summary is not proof of absence from the old analysis. [CHISA-E33, CHISA-E37, CHISA-E45, CHISA-E47] |

## 2. The audio identity correction

The supplied acoustic and line records contain 2,429 language/render associations. Grouping those associations by canonical PCM identity yields 2,421 unique objects. The separately downloaded FLAC manifest supports the same distinct count using `expected_canonical_pcm_sha256`, `flac_sha256`, and `flac_relative_path`.

The repeated semantic uses are:

| Archive key | Event key using the same corresponding recording | Languages |
|---|---|---|
| `FavorWord_150824_Content` | `Event_XFCPZJZ_4_1` | Chinese, English, Japanese, Korean |
| `FavorWord_150825_Content` | `Event_XFCPZJZ_11_1` | Chinese, English, Japanese, Korean |

These are two duplicate pairs per language, accounting for eight associations beyond the unique-object count. The extra English variant belongs to `Shixifeidu_main_2_8_111_9`; a render variant and a reused object are different cardinality issues.

The numerical distinction has three consequences. First, the semantic census stays at 607: two uses of the same sound in different source positions do not cease to be different semantic records. Second, a repeated recording must not become independent performance corroboration merely because it occurs under two keys. Third, the old retained-byte total is association-weighted: 668,358,359 bytes. Summing each distinct supplied FLAC identity once yields 667,796,455 bytes.

This is a correction to what the historical report says about uniqueness, not a finding that eight lines are missing, that the recordings are corrupt, or that voice completeness has failed. It also does not reproduce the original source-WEM decoding and PCM round-trip tests. The present check concerns the identity metadata and its arithmetic. The [speech profile](WUWA_CHISA_SPEECH_AND_MACHINE_VOICE_PROFILE_PRE_AV.md) supplies the language aggregates and feature limits. [CHISA-E60]

## 3. Interpretive improvements that must not be overstated

The strongest new local contribution is an expanded set of constraints on the familiar cold-prodigy reading. Pre-Rover intervention, explicit resistance to numbness, ordinary preferences, friends, parents, and proposed future class attendance all resist it. But the earlier report already rejected a purely technical or magically cured character. That prior advance is credited rather than claimed as a discovery of this rebuild.

Likewise, the more detailed treatment of parents is not a verdict that an earlier analyst ignored them. It is a new source-facing account of how early loneliness and economic strain can coexist with a later twenty-year search and renewed ordinary care. The same restraint applies to Lynae: the dossier now gives the friendship a dedicated place because the retrieved evidence warrants it. It does not claim to have disproven a missing prior relationship section. [CHISA-E02, CHISA-E18, CHISA-E30, CHISA-E37]

The disclosure correction is more specifically evidence-driven. Early Honami conditions give knowledge a dangerous causal role; later side-story conditions differ. Any model that exports the early rule unchanged must be narrowed. This conclusion is independent of whether an earlier unseen monograph already made the distinction. [CHISA-E15, CHISA-E33]

## 4. Method adoption versus repository authority

The three AV-method documents supplied in the local amendment package govern this rebuild as owner-adopted working methods. This statement does not certify that they have been merged, that current Git governance uses identical wording, or that the new dossier may bypass publication checks.

Their analytical effects are straightforward: every nominated item has a purpose; public search terms are not evidence; official promotional framing is not automatic diegetic truth; matched-language groups require independent edit and semantic checks; and acquisition is not direct review. The optional human listening layer remains terminal rather than a prerequisite imposed on the project owner.

The rebuild does not modify either character registry output, create an enrollment-upsert file, revise source hashes, or change Drive sharing. It also does not reinstate the older proposal that every authoring session curate character enrollment. Future publication must use the live designated-curation-agent policy, not the historical checklist copies in the conversation.

## 5. What needs recovery before formal replacement

Before this local packet is promoted as a current authoritative replacement, retrieve the current Chisa entrypoint, all existing Chisa analytical files, and any character records that reference them. Record the current-main commit and reconcile the exact intended paths. A new additive reading may be safe without altering old evidence dependencies; replacing a referenced file, its anchors, authority, or content hash may require coordinated repair.

A full old-monograph comparison would also allow a more precise revision ledger. At present, the honest scope is the reports actually read and the primary evidence actually materialized. Do not convert this document into an assertion that all prior Chisa conclusions were reviewed. The input inventory, evidence matrix, and individual source locators are sufficient to continue the analytical work while keeping that limitation explicit.
