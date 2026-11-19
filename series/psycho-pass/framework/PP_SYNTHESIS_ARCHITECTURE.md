---
title: "Psycho-Pass — Synthesis and franchise architecture"
artifact_id: PP_SYNTHESIS_ARCHITECTURE
artifact_type: synthesis_architecture
series: psycho-pass
version: "1.0"
status: canonical
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
do_not_use_as_literary_evidence: true
authority_generation: PP-INITIAL
source_boundary: "NONE; metadata-only foundation, no admitted narrative"
canonical_home: series/psycho-pass/framework/PP_SYNTHESIS_ARCHITECTURE.md
created: 2026-11-18
last_updated: 2026-11-18
recommended_reasoning_class: PREMIUM_QUALITY_FIRST
---

# Psycho-Pass — Synthesis and franchise architecture

This architecture maintains one franchise root with bounded installment work and provenance-preserving longitudinal synthesis. Its day-one state is administrative: no admitted evidence, portraits, readings, narrative records or accepted claims. The [method](PP_ANALYTICAL_METHOD.md) supplies source-facing analytical duties. This document allocates their durable outputs.

## Canonical responsibilities and justified homes

| Home | Responsibility and update boundary |
| --- | --- |
| [Source register](../source-inventory/PP_SOURCE_REGISTER.md) | Immutable witness identities, available/candidate/admitted distinctions, technical clocks, edition relationships, missing evidence and admission checks. Mutable only through attributed inventory changes. |
| [S1 New Edit evidence/state](../installments/s01-new-edit/PP_S01NE_EVIDENCE_AND_STATE_LEDGER.md) | Primary observations, precise locators, scene causality and installment-bound character/relationship/institution states. Updated in each accepted episode transaction. |
| [S1 New Edit claims/disclosure](../installments/s01-new-edit/PP_S01NE_CLAIM_AND_DISCLOSURE_LEDGER.md) | Prospective freezes, edition-specific audience/character information, local claims, alternatives, revisions and independent-review substance. Per-unit acceptance preserves prior states. |
| [Franchise state](../franchise/ledgers/PP_FRANCHISE_STATE_LEDGER.md) | Current reconciled character, directed relationship and institution/world state; canonical portrait qualification and dependencies. Targeted materialized conclusions with lineage. |
| [Franchise continuity/claims](../franchise/ledgers/PP_CONTINUITY_AND_CLAIM_LEDGER.md) | Release/event/disclosure reconciliation, cross-installment propositions, audiovisual recurrence, contradictions and change lineage. Updates only affected records. |
| [Integration protocol](../integration/PP_RECONCILIATION_PROTOCOL.md) | Role responsibilities, AV evidence reconciliation, change proposals, acceptance, mutable ownership, freezes and handoffs. |
| [Entrypoint](../CURRENT_STATE_AND_CORPUS_MAP.md) | Present authority routes, source/admission boundary, gates and next permitted operation. No narrative replacement or duplicated history. |

Only `installments/s01-new-edit/` exists at bootstrap. The official catalogue identifies additional seasons and films, but no later-source assets have been verified in the inspected inventory and none are admitted. Create a new installment home only when a verified source and authorized responsibility warrant it. Do not create empty film readings, character files, motif studies, audit directories or final syntheses in advance.

Future episode readings belong under `installments/s01-new-edit/readings/PP_S01NE_E##_DEEP_READING.md`, with a structured sequential artifact type. Future local audits and installment synthesis remain in that installment's home with accurate non-sequential types. These are naming contracts, not links to existing files. Each later home declares its own edition/unit scheme, local evidence and claims responsibility, source boundary and route to the same franchise layer. All remain on `series/psycho-pass`; no per-season branches or independent continuities are implied.

## Local observations and materialized franchise synthesis

A local record owns what was observed and concluded at that installment's horizon. The master owns the current reconciled conclusion across admitted material. It must contain enough causal and psychological explanation to be useful without opening every source row, while retaining routes to those rows and readings. Merely copying references or duplicating all local events fails this responsibility.

A master claim includes its affected entity/topic, applicable continuity and knowledge boundary, current assertion and confidence, source installment/edition/unit, stable local evidence/claim IDs, decisive locators, contrary evidence, revision lineage and review disposition. A reader can recover why the present conclusion differs from the earlier one. A master conclusion is derived from source-facing work; its own authority cannot be circular evidence for that work.

During a run, each unit commits its local state and affected dependency markers. Reconcile master changes at a declared tranche or installment boundary, or earlier when a material contradiction would mislead the next unit. If batching is chosen, the entrypoint and affected master records state the actual reconciled boundary and pending delta IDs. Do not label the master current through evidence it has not integrated. No whole-franchise regeneration is required after every episode.

At a boundary, send new findings, character/relationship changes, institutional changes, revised interpretations, continuity disagreements, evidence gaps and proposed specialist obligations as reviewable deltas. The integrator applies accepted targeted edits and preserves rejected/qualified/open decisions. Split a disagreement that concerns both factual chronology and interpretation into separately adjudicable claims. Corrections propagate to their dependent portrait or synthesis and leave historical freezes intact.

## Three chronologies and edition relations

Release chronology records verified first availability of the exact edition or installment, with region/medium where relevant, precision and source. Catalog ordering or a contemporary rebroadcast date is not initial release evidence. In-universe chronology records depicted event dates or relative constraints, their evidence and uncertainty. Disclosure chronology records which character or audience learned what, where and in which edition. Keep time of occurrence, time of representation and time of learning separate even within one scene.

New Edit and original Season 1 share a continuity identity but have distinct source units, runtime clocks and disclosure sequences. Their comparison is a separate authorization and evidence operation. Original-only footage or a different cut may revise an edition claim without creating another fictional timeline. No automatic mapping from New Edit E01 to original E01/E02, no transfer of timestamps and no duplicated coverage credit. If a genuine continuity divergence is later evidenced, record the demonstrated divergence and its scope before changing the model.

The master may hold the latest retrospective interpretation while an earlier local reading remains frozen at its own boundary. A qualified earlier claim is not necessarily an error because later revelation changes it. Distinguish factual correction, previously unavailable information, edition difference and interpretive revision.

## Individuals and one canonical full portrait

Every differentiated named or identifiable subject is considered for monograph qualification; prominence or a preset roster is not the criterion. Review source distribution, independent behavioral pattern, development, relationships, ordinary life, psychological/cognitive evidence and consequential agency. A minor character may qualify; an institution spokesperson does not automatically qualify merely by delivering an important thesis. Keep group/institution studies separate from individual portraits.

The [franchise state ledger](../franchise/ledgers/PP_FRANCHISE_STATE_LEDGER.md) owns each qualification decision with stable subject ID, known names/aliases at relevant disclosure horizons, continuity, assessed source boundary, evidence-based rationale, gaps, trigger and current actual portrait path if one exists. Use the governing statuses `QUALIFIED_PENDING`, `COMPLETE_AT_BOUNDARY`, `DEFERRED_EVIDENCE` and `REASSESS_AFTER_REVISION`. Qualification creates a production obligation. Never claim the character layer complete while qualified portraits remain pending.

The eventual home is `franchise/characters/PP_<SUBJECT>_CHARACTER_MONOGRAPH.md`. Exactly one current canonical full portrait per individual, continuity and declared boundary is routed by the qualification record. Local ledgers preserve scoped states; local readings explain turning points; a new installment does not create a rival biography. Frozen historical portraits remain identifiable as noncurrent, and current mutable portraits carry dated, sourced revisions and supersession routes.

A standalone portrait must be independently usable: identity and embodied presentation, relevant history, motives/emotional patterns, cognition and knowledge, behavioral tendencies, speech and communicative behavior, directed relationships, ordinary life/preferences, source-bounded intimacy, abilities/limits, development across time, conditional behavior profile, uncertainty/contradictions and traceable evidence. Integrate the person into connected explanatory prose with representative scenes. Do not substitute trait tags, ideology labels, selected crisis behavior, a relationship diagram or ledger hyperlinks for a portrait. Unknown and untested domains are stated plainly.

Qualification, portrait completion and reconstruction validation are separate. A strong portrait does not earn a simulation-readiness grade without an independently defined and executed reconstruction validation. Conditional predictions identify their assumptions and extrapolation limits. No psychological diagnosis or unseen personal history is inferred simply to fill required sections.

Two independent assessments are required for completion at a boundary: **self-containment**, asking whether a reader can understand and distinguish the person without chasing missing narrative into ledgers; and **source fidelity**, checking representative decisive evidence, conflicting cases, baseline behavior, major relationships and meaningful transitions against the admitted sources. Sample introduction, middle and latest/exit material where present. Record coverage and limitations; one favorable example cannot certify the whole portrait. Meaningful shortcomings reopen the qualification record and dependent claims.

## Specialist and franchise synthesis

Create a relationship study when a sustained reciprocal/asymmetric system needs more explanatory space than current-state rows. Create an institutional study when procedures, authority, incentives, exceptions and historical change need joint examination. Philosophical/thematic and audiovisual studies require accumulated evidence, counterinstances and a real cross-unit question. Their material belongs in coherent analysis with source lineage, not a directory of short isolated motif entries.

Substantial installment synthesis reconciles its local readings and ledger state, changes over the installment, formal construction, unresolved contradictions and implications for existing master claims. A franchise synthesis becomes warranted only by admitted multi-installment evidence. It must preserve differences between eras, genres, focalizers and editions, not flatten them into a single formula. Fresh synthesis sessions retrieve actual accepted evidence, substantial independent findings and source routes before drafting.

A specialist synthesis may propose a change to another authoritative home, but the proposal is not automatically accepted authority. The local integrator checks its evidence, source horizon and dependencies, resolves targeted convergence and updates the owning record. Required channel deficits or unresolved load-bearing factual disputes block the relevant synthesis completion. Optional enrichment may stay open with a bounded effect and follow-up trigger.

## Extension and distinct completion gates

Extend this architecture when a dimension recurs, develops independent evidence, affects later synthesis or requires retrieval that existing homes cannot support. Assign one owner and canonical home, state why the present ledgers are inadequate, and update the current map and architecture revision history. Do not create a parallel authoritative home for an existing responsibility. Backfill only material evidence gaps that cannot be repaired responsibly from retained readings and primary evidence; a new question does not automatically mandate rereading the entire franchise.

Completion is assessed for an explicit installment, tranche or franchise boundary. These six states are distinct:

| Gate | Evidence required before passage |
| --- | --- |
| Sequential-source completion | Every authorized required unit has a complete accepted episode transaction, including synopsis, source coverage, independent contributions and review. No unauthorized or merely inventoried source counts. |
| Longitudinal reconciliation | Local states and claims are current at that boundary; affected master deltas, disclosure/chronology differences, revisions and dependencies are adjudicated. Material unresolved gaps are recorded as incomplete, not silently carried into a current-state claim. |
| Specialist-synthesis readiness | Required source channels and actual evidence packages are adequate for each proposed specialist responsibility. Conduct all-subject monograph qualification no later than this gate, expose qualified pending obligations, and identify the specialist's exact sources, rivals and open issues. Readiness permits defined specialist work, not a claim that its deliverables are complete. |
| Full-series synthesis readiness | An architecture/role-gap review verifies that source-derived responsibilities, required specialist work, qualified portraits, cumulative reconciliation and necessary revisions are satisfied for the declared scope. Sequential completion alone does not pass this gate. |
| Validation/audit completion | Independent substantive review verifies decisive evidence, causal/character transitions, three-clock integrity, self-containment, source fidelity, significant omissions and disposition of required corrections. Mechanical links/schema checks are additional, not substitutes. |
| Frozen/release state | Accepted exact artifact versions, source boundaries, open optional issues, current/noncurrent routes and dependency state are preserved and release-audited under live publication governance. Any run/terminal closure is a separate applicable controlled transaction. |

The ordinary dependency order is accepted units → reconciled state → specialist readiness/work → full-series readiness/work → validation → release. Bounded specialist work may occur earlier with an explicit narrower source boundary. No early task relabels the later gate complete. All six narrative completion states are currently **NOT_REACHED** because source admission is NONE.

Initial architecture history: version 1.0 establishes these responsibilities at PP-INITIAL. Future material amendments record their reason, affected homes, boundary and backfill decision here and update the current map.

## Execution ownership and reasoning

The [reasoning policy](../../../governance/source-policies/MANGA_ANIME_REASONING_AND_MODEL_ROUTING_POLICY.md) classifies work separately from provider choice. Mechanical hash/routing work is `ROUTINE_FAST`; inventory reconciliation is normally `BOUNDED_STANDARD`; mature sequential reading and bounded specialist work begin at `SUBSTANTIVE_ANALYSIS`; portrait, contradiction and cross-installment synthesis usually require `DEEP_SYNTHESIS`. Architecture and propagation-sensitive reconciliation may warrant `PREMIUM_QUALITY_FIRST` with a stated reliability benefit. More tokens never replace inaccessible evidence.

The principal owns complete source coverage and draft readings. Independent specialists own their assigned source-based findings, normally Japanese/institutional argument and performance/form as appropriate to the unit. The separate critical reviewer tests decisive evidence, the strongest rival explanations and omissions. The named analytical integrator alone edits shared current ledgers, accepts changes and controls dependency propagation. The repository integration owner handles exact-path publication under live governance. One person may hold principal/integrator responsibility with disclosure; they cannot be their own independent reviewer.

The owner prefers Gemini 4 Carbon High for principal continuous-AV work and OpenAI and/or Anthropic for independent specialties and critical adjudication. These are replaceable candidates. Capability verification, independence and evidence quality determine actual assignment. No model name provides a tie-breaker, and no reduced multi-agent configuration is planned for these extended, multi-channel episodes.

Long-series work follows the [hybrid protocol](../../../governance/source-policies/MANGA_ANIME_LONG_SERIES_HYBRID_EXECUTION_PROTOCOL.md): synchronized local source reading/ledgers, fresh adequately grounded synthesis sessions, and local acceptance/integration. Fresh cloud Pro is the preferred synthesis environment when it can receive the necessary lawful evidence and handoff, not a claim of universally superior interpretation. Actual working topology, capability and provider are recorded per run.

A checkpoint freezes accepted readings, prospective captures and independent observation/review records. Current ledgers, entrypoint and full portraits remain mutable through attributed revisions; source hashes are immutable and changed bytes create new witnesses. The [handoff contract](../../../governance/source-policies/MANGA_ANIME_ANALYTICAL_HANDOFF_AND_INTEGRATION_CONTRACT.md), [archive policy](../../../governance/source-policies/ARCHIVE_AUTHORITY_AND_SUPERSESSION_POLICY.md) and [local protocol](../integration/PP_RECONCILIATION_PROTOCOL.md) govern actual-byte handoffs, freeze protection and supersession. This initial CLOSED state has no historical run to seal.
