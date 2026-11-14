---
title: "The Apothecary Diaries — Synthesis Architecture"
artifact_id: AP_SYNTHESIS_ARCHITECTURE
artifact_type: synthesis_architecture
version: "1.1"
status: canonical
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
authority_generation: AP-INITIAL
authority_scope: "INITIAL bootstrap method, architecture, and administrative metadata only; no literary findings"
source_boundary: "Metadata reconnaissance: Japanese volumes 01–16 and separate simplified Chinese volume 15; no narrative admitted"
created: 2026-11-07
last_updated: 2026-11-13
architecture_lifecycle: INITIAL
recommended_reasoning_class: PREMIUM_QUALITY_FIRST
---

# The Apothecary Diaries synthesis architecture

## 1. Purpose and INITIAL authority

This architecture makes a future serial Japanese prose corpus recoverable at the level of causal reasoning, partial knowledge, character development, directed relationships and language. It covers the supplied V01–16 inventory as a prospective planning boundary and keeps the Chinese V15 witness separate. No source unit has been admitted. Neither collection completeness, architecture owner approval nor a reconstruction readiness assessment is claimed.

The [current entrypoint](CURRENT_STATE_AND_CORPUS_MAP.md) is the only authority router. The [local method](AP_ANALYTICAL_METHOD.md) governs readings. The [initiation policy](../../governance/source-policies/MANGA_ANIME_PROJECT_INITIATION_AND_ARCHITECTURE_POLICY.md), [generic synthesis architecture](../../governance/analytical-methods/GENERIC_MULTI_DOCUMENT_SYNTHESIS_ARCHITECTURE_TEMPLATE.md), [generic reconstruction method](../../governance/analytical-methods/GENERIC_CHARACTER_RECONSTRUCTION_METHOD.md), archive, execution and handoff policies govern their respective responsibilities.

This is a source-specific accumulation design, not a claim that particular anticipated themes have been found. The serial ledger is mandatory because a numbered multi-volume prose inventory needs recoverable state across prospective readings. A standalone medical, political or institutional study is not mandatory merely because the title suggests one. It must earn a recurring, independent question from admitted evidence.

## 2. Source model and ranking

| Source class | Permitted role and precedence |
|---|---|
| Locked Japanese primary prose | Anchor for claims about its own narrative; actual inspected wording and source boundary outrank catalog metadata |
| Japanese illustrations and paratext | Distinct component evidence with placement and modality limits; no automatic override of prose |
| Simplified Chinese V15 | Separate language witness; not a missing-volume substitute or silently interchangeable wording |
| Historical source audit / current inventory metadata | Provenance and access planning only; never evidence of character or literary meaning |
| Adaptation, sequel, other edition or later acquisition | Excluded until independently identified and explicitly admitted; never retroactive fill |
| External research / secondary discussion | Explicitly labeled contextual or critical claim, if authorized and useful; no primary-source replacement |
| Analytical reading, ledger, monograph or reconstruction | Derived reasoning with recoverable evidence; no number of derivative restatements creates independent corroboration |

The [source map](SOURCE_WITNESS_AND_COVERAGE_MAP.md) separates inventory presence, witness verification, authorization, inspection and analytical completion. Its V15 identities survive any filename change and UUID collision. A witness digest change creates a distinct version pending equivalence assessment. Public-safe routing keys resolve through governed private receipts; no credential, source identifier or restricted path belongs in Git.

## 3. Artifact taxonomy and state

Only eight Markdown foundation files and the routing descriptor exist at INITIAL. This deliberately avoids empty future-study folders. Planned homes below are filenames or patterns, **not claims that those artifacts exist**.

| Artifact class | Distinct responsibility | Planned home / status |
|---|---|---|
| Current entrypoint | Present boundary, lock, governing routes and next allowed operation | Existing current map |
| Method / architecture | How evidence is read / how outputs accumulate and converge | Existing two governing files |
| Source and cumulative registers | Identity, inspectability, claims, serial state, character/register and integration control | Existing five mandatory ledgers below |
| Full sequential volume reading | Sustained argument and detailed source-facing analysis at the authorized prospective boundary | Future `readings/AP_JP_Vnn_READING.md`; created only for authorized inspected units |
| Checkpoint report | Cross-unit reconciliation, preserved alternatives, frozen prospective state and role gaps | Future `checkpoints/AP_CPnn.md` after a bounded completed tranche |
| Character monograph | Diachronic literary account integrating form, motivation, relationship and function | Future `studies/characters/<source-established-id>_MONOGRAPH.md`; evidence threshold required |
| Relationship / specialist study | Independent longitudinal question requiring full argument beyond a subject monograph | Future `studies/relationships/` or `studies/domains/`; earned scope only |
| Continuous synthesis | Reconstruct the work's connected interpretation across specialists, not concatenate their abstracts | Future `synthesis/AP_CONTINUOUS_SYNTHESIS.md`; convergence gate first |
| Reconstruction dossier / tests | Time-indexed operational model and independently evaluated predictions | Future `reconstruction/<subject-id>/`; distinct evidence, model and test files |
| Erratum / historical generation | Preserve displaced reasoning and explain correction without rewriting frozen readings | Future explicit erratum or `90_LEGACY/` route when warranted |

These homes do not authorize new artifact classes automatically. A new file must declare scope, authority quartet, source boundary, responsibility and current route. A study that merely repeats an existing home should revise that home rather than compete with it.

## 4. Responsibility matrix

Every substantive dimension has a source-facing capture obligation, cumulative home and eventual synthesis destination. “Deferred” concerns the destination, not permission to omit evidence now.

| Dimension | Full reading must capture | Cumulative home | Synthesis destination / state |
|---|---|---|---|
| Witness identity and coverage | Exact receipt, narrative/image/paratext scope and exclusions | [Source map](SOURCE_WITNESS_AND_COVERAGE_MAP.md) | Every derivative boundary; initialized |
| Event causation and practical explanation | Conditions, information, choices, consequences, failed links and rivals | [Serial ledger](SERIAL_CAUSAL_AND_KNOWLEDGE_LEDGER.md), causal register | Continuous synthesis; dedicated specialist only if recurring mechanism earns it |
| Narrative order and knowledge | Disclosure frontier, narrator/subject/reader positions, withheld facts | Serial ledger, chronology and knowledge registers | Form/epistemic study if warranted; always required in synthesis |
| Character continuity and development | Speech, action, interiority, reports, state changes and ordinary controls | [Character ledger](CHARACTER_RELATIONSHIP_AND_REGISTER_LEDGER.md), subject register | Monographs and later reconstruction; destinations deferred |
| Directed relationships and roles | Asymmetric beliefs, obligations, audience and resource conditions | Character ledger, directed-edge register | Relationship studies where independently useful; deferred |
| Written Japanese voice and register | Exact wording, rhetorical action, recipient, alternatives and gloss limits | Character ledger, language register | Character/form studies and written-voice model; deferred |
| Institutions / specialized domains | Observed rule versus assertion, mechanism, exception and limitation | Serial ledger, institution register plus full reading | Domain study only after evidence establishes recurring load-bearing need |
| Ordinary life and negative opportunity | Routine, low-stakes contexts, explicit opportunities and absences | Character ledger with opportunity tags | Every character/relationship study; required, no separate empty folder |
| Motifs, narrative form and value questions | Pattern plus variation, counterexample and interpretive rivals | [Claim ledger](CLAIM_EVIDENCE_AND_REVISION_LEDGER.md), typed evidence routes | Specialist or continuous synthesis; deferred |
| Illustrations and paratext | Actual modality inspection, placement, spoiler boundary and disagreement | Source map coverage + claim ledger evidence type | Local full reading first; cross-volume visual study only if earned |
| Translation / witness comparison | Verified alignment, omission/addition/ambiguity and non-equivalence | Source map witness relation + claim ledger | Separate comparison study only after explicit scope authorization |
| Counterreadings and revision | Strongest viable alternative, disconfirmers and displaced reasoning | Claim ledger + full reading | All syntheses; mandatory retained argument |
| Coverage, freezes and dependencies | Atomic unit updates, modality/retrieval debt, remaining role work | [Checkpoint ledger](CHECKPOINT_AND_INTEGRATION_LEDGER.md) | Convergence and release decisions; initialized |
| Reconstruction | Observed context-dependent policies with exceptions and source limits | Character ledger evidence routes and coverage debts initially | Distinct future model/tests; no readiness claim |

A ledger is an index and state record. Full causal, linguistic or relational arguments remain in the reading or study. Summaries may assist navigation only; they cannot be handed off as replacements for the complete outputs.

## 5. Sequential contract and cumulative transaction

The prospective unit is a verified volume, with chapter/movement frontiers inside it. Before the first run, verify numbered order and any exceptional component ordering. Publication date, narrative chronology and disclosure remain separate even when the reading order is straightforward. A Chinese comparison is a separate operation and cannot occur as an unrecorded detour during Japanese V15.

Each future unit starts from the accepted source frontier, current eligible claims, prior freeze and unresolved evidence debts. Record local interpretations before later disclosures. At the end, submit the full reading together with source coverage, new evidence routes, claim revisions, serial/knowledge deltas, subject/relationship/register deltas and integration record. A no-change result is recorded with its inspected scope; absence of ledger edits is not evidence of no change.

The owner-authorized run determines its start, terminal unit, checkpoint rhythm and permitted operations. This architecture does not issue a run. At a natural causal/disclosure transition or a bounded tranche boundary, create a checkpoint only after all unit transactions are closed. Configure the initial cadence before a run rather than invent a current checkpoint. Review triggers also include consequential witness changes, unresolved causal contradictions, large state revisions and unretrievable central evidence.

Sequential closure is source-facing completion at that boundary. It is not proof that all synthesis roles have been filled. Detailed readings remain available for later specialists even where checkpoint prose summarizes a result.

## 6. Time, knowledge and continuity

The state vector is `{witness/edition, admitted frontier, disclosure position, story-time constraints, focalization, subject knowledge, reader knowledge, physical/affective condition, role, resources, directed relationships}`. Unknown fields stay unknown. “Same person” and “same event” links must be source-supported; no title familiarity fills them.

The Japanese anchor lane is a working source partition, not an unexamined assertion that every supplied artifact has identical continuity. The Chinese V15 has its own witness state. A future comparison can link passages without merging chronology, narrator stance or language evidence. Adaptations have no state in this corpus.

Retain `PROSPECTIVE_AT_BOUNDARY`, `RETROSPECTIVE_WITHIN_ADMITTED_BOUNDARY`, `EDITION_COMPARATIVE` and `UNRESOLVED` epistemic modes. Later evidence can strengthen an explanation without making it available earlier. Record disclosure time separately from event time and character acquisition time. Use relative precedence and uncertainty ranges where calendar dates are unsupported.

Continuity disputes must distinguish an edition difference, translation choice, knowledge asymmetry, unreliable claim, deliberate performance, temporal reordering, missing source and genuine textual inconsistency. A dispute can remain unresolved with precise dependencies. Do not harmonize incompatible evidence because a monograph needs a smooth arc.

## 7. Claims, revision and argument preservation

The shared transition vocabulary is `PRESERVE`, `STRENGTHEN`, `REVISE`, `DOWNGRADE`, `REJECT`, `OPEN`. Each change preserves the earlier formulation, its boundary and route, the new formulation, the decisive evidence, counterevidence, authority destination and unresolved implications. Confidence changes alone need reasons.

A claim's current pointer may move; its historical version is not deleted. A central revision triggers a dependency review of readings cited as evidence, causal state, subject models, relationship studies and synthesis. Frozen readings are cited and corrected through an erratum/revision rather than overwritten. Different interpretive theses may remain live when evidence does not discriminate them. Source discrepancy is not the same as interpretive disagreement.

No summary, schema, table or reconstruction policy may replace the full account of a disputed motive, linguistic ambiguity, mechanism or relationship. Integration review explicitly compares the returned output with its input scope for lost ordinary-life evidence, causal steps, competing theses and uncertainty.

## 8. Monographs and specialists

A character monograph begins when enough admitted evidence spans meaningful situations, knowledge states, relationships and low-stakes contexts to support a coherent question. Frequency of appearance alone is insufficient. It integrates narrative presentation, behavior, motive alternatives, development, language and literary function; it does not merely print the character ledger.

A directed relationship study is warranted when reciprocal/asymmetric development, institutional constraints or persistent interpretive conflict cannot be adequately owned by either subject monograph. Its scope must identify both directions and surrounding relations, not assume symmetrical affection or trust.

Specialist commissioning requires an independent recurring question, evidence spanning the relevant boundary, a named topical owner, key counterexamples and a declared contribution to continuous synthesis. Potential professional-knowledge, institutional, language or form studies remain **anticipated**, not mandatory established themes. The role-gap review can require one later if evidence makes omission material. Routine dimensions still receive full reading coverage before that decision.

Specialists work from frozen full readings and retrievable primary evidence. They may return to admitted sources for verification under applicable scope; unavailable evidence is a debt, not a warrant to improvise. They return complete prose, not compressed conclusions for the integrator to expand from memory.

## 9. Character reconstruction pathway

Reconstruction is an intended later responsibility when source-grounded character coverage supports it. It is **distinct from** a monograph and is not operationally ready at bootstrap. No subject dossier or global readiness grade is initialized without discovered subject evidence. The character ledger holds an explicit coverage gap rather than invented personalities.

Each future dossier separates (a) evidence ledger and retrieval map, (b) time-indexed operational model, and (c) test record and independent evaluation. Its key is `subject@Japanese-witness-boundary/state`; a Chinese comparison cannot silently augment the Japanese model. Record excluded sources, latent familiarity and unobserved modalities.

Model dimensions include goals/values, threat and appraisal, motives/conflicts, knowledge/errors, attention and reasoning, affect/regulation, dispositions versus temporary state, directed relationships, role/audience presentation, action repertoire/inhibitors, Japanese written voice, and development/exception history. Coverage is descriptive with evidence and gaps, not an unsupported letter grade.

A candidate policy must specify trigger, stakes, current state, likely response family, inhibitors/overrides, exceptions, support, counterevidence, rival explanation and falsifier. Each projected response records confidence, its distance from observed situations/relationships/states, and an abstention or multiple-plausible-responses rule when that distance exceeds the evidence. Classify evidence as direct speech, behavior, narrated interiority, reported behavior, observer/role presentation or inference. Distinguish `OBSERVED`, `CANDIDATE_POLICY` and `PROMOTED_POLICY`. A vivid episode is not enough to promote a global trait.

Test a meaningful range when available: ordinary low-stakes interaction, pressure/conflict, uncertainty or false belief, changed recipient/relationship, role/audience shift, and a morally or practically consequential choice. Unavailable scenarios remain gaps. Written voice tests separately assess decision fidelity and surface/register fidelity; they cannot certify performed voice.

Prospective predictions are frozen **before** held-out source admission. Select holdouts and prevent model-author leakage; record any unavoidable exposure. After exposure, label the exercise `RETROSPECTIVE_CONSISTENCY_TEST`, never genuinely held out, and give it lower evidentiary weight. An independent evaluator assesses supported, partly supported, contradicted, no diagnostic opportunity, confounded or unresolved outcomes against explicit criteria. Use counterfactual perturbations, plausible decoys, negative controls and a simple baseline where diagnostic. Record denominators/opportunities and avoid unsupported accuracy percentages.

All synthetic dialogue, scenario completions and model predictions are labeled derived outputs with a synthetic-evidence firewall: they never become primary evidence, quotations, training exemplars masquerading as canon, or independent corroboration. A monograph's literary adequacy does not certify predictive validity. Designated evaluators own readiness and global capability registry outputs; this series author supplies evidence and limitations only.

## 10. Separate gates and convergence

| Gate | Evidence required; never inferred from the previous row |
|---|---|
| G0 Foundation review | Current method/architecture, all sixteen duties, initialized justified schemas, explicit source uncertainty and closed lock |
| G1 Run authorization / admission | Owner-bounded scope, verified capability/source identities and OPEN precondition; absent now |
| G2 Sequential source closure | Every selected component accounted for, full readings accepted, retrieval and ledger transactions complete |
| G3 Longitudinal reconciliation | Accepted units reconciled across time, knowledge, causal, character, relationship and register histories; unresolved contradictions bounded |
| G4 Evidence and claim stabilization | Central locators tested; alternatives preserved; high-impact revisions propagated; unresolved debts bounded |
| G5 Character / specialist readiness | Source omissions and ordinary-life/voice/relationship gaps audited; each required role assigned adequate evidence or a precise hold |
| G6 Specialist / monograph completion | Full role-specific outputs accepted at frozen source boundaries; evidence returns completed |
| G7 Specialist convergence | Cross-study dependencies and disagreements reconciled or explicitly retained; if no independent specialist is warranted, record an evidence-based rationale and who discharges every role |
| G8 Integrated synthesis readiness | Complete inputs, chronology/knowledge state, accepted specialist obligations and remaining limits reviewed before commissioning continuous synthesis |
| G9 Continuous synthesis acceptance | One integrated argument with causal, linguistic, relational and temporal depth; no concatenation of abstracts |
| G10 Reconstruction evaluation | Independent held-out assessment for each model/scope; distinct from literary synthesis readiness |
| G11 Final validation | Scope, source routes, full-text completeness, names/references, authority and unresolved limitations checked against the actual final files |
| G12 Release / freeze | Defined immutable output set, hashes, current routes, history and designated integration acceptance; publication never authorizes a new run |

The current state is INITIAL foundation preparation/review only. No gate beyond documentary initialization is claimed passed. A future partial-boundary release must say exactly what it covers; V16 inventory closure is not necessarily work completion. Missing material or capabilities can block affected claims while other authorized work proceeds.

## 11. Execution, dependencies and handoff

Architecture and continuous synthesis use `PREMIUM_QUALITY_FIRST` for high downstream error cost; sequential readings and interpretive state changes use `SUBSTANTIVE_ANALYSIS`; checkpoints, monographs, specialists and model/test adjudication use `DEEP_SYNTHESIS`. Mechanical routing is `BOUNDED_STANDARD` or `ROUTINE_FAST` only where no interpretive judgment is being disguised. Use the live [reasoning policy](../../governance/source-policies/MANGA_ANIME_REASONING_AND_MODEL_ROUTING_POLICY.md) to resolve actual configurations; record observed model/effort only, never invented settings.

The preferred [long-series arrangement](../../governance/source-policies/MANGA_ANIME_LONG_SERIES_HYBRID_EXECUTION_PROTOCOL.md) has one local owner for sequential readings/ledgers, fresh adequately supplied synthesis specialists, an independent reviewer and a designated integration owner. Architecture can be prepared locally when bounded metadata is adequate, as here; this is not a claim of primary-text capability. The [capability policy](../../governance/source-policies/MANGA_ANIME_EXECUTION_TOPOLOGY_AND_CAPABILITY_ROUTING_POLICY.md) requires separate transport, processing, inspection, interpretation and persistence verification.

A handoff names the base snapshot, full exact input/output paths and digests, witness/admission/knowledge boundaries, authority generation, work owner, open dependencies and permitted revisions. Include complete method, architecture, readings, relevant cumulative ledgers and prior argument—not an abstract alone. The returning stage supplies complete files and a change/evidence manifest. The integrator compares base, candidate and current target, retrieves load-bearing evidence, and checks depth before acceptance. Changed branch state prohibits blind replacement. One mutable owner per artifact applies even when different specialists work in parallel.

## 12. Growth, freezes and semantic duty audit

New volumes extend the source map only after identity reconciliation; they do not automatically extend an authorized run. A new language or adaptation requires explicit source ranking, continuity and modality decisions. Add infrastructure when a recurring responsibility cannot be represented adequately, with a documented schema migration and proportional backfill of affected admitted evidence. No blanket reread or cosmetic restructuring is implied.

Mutable ledgers preserve append-only revisions and current views. Accepted prospective readings and checkpoint snapshots are frozen at their boundary. Later synthesis may supersede current claims with reciprocal authority metadata while preserving prior intellectual history. Create archive containers only when real superseded work exists. An erratum does not gain source-admission authority.

The sixteen mandatory architectural duties are discharged here:

| Initiation policy duty | Concrete discharge |
|---|---|
| 5.1 Purpose, scope, generation, authority | §§1,3 and current entrypoint |
| 5.2 Source classes/ranking | §2; source map identity states |
| 5.3 Sequential contract | §5; method §§2–9; required [current-unit story synopsis](AP_ANALYTICAL_METHOD.md#current-unit-story-synopsis) within the complete plot-bearing reading |
| 5.4 Cumulative infrastructure | §§3–4; five initialized ledgers with schemas and update rules |
| 5.5 Character/relationship synthesis | §8; directed state and ordinary-life capture |
| 5.6 Specialist domains | §§4,8; earned versus anticipated responsibilities |
| 5.7 Deterministic retrieval | Method §3; source map; claim evidence schema |
| 5.8 Revision vocabulary/history | §7; versioned claim transitions |
| 5.9 Temporal/epistemic/continuity state | §6; serial and subject schemas |
| 5.10 Contradictions | §§6–7; typed dispute procedure and rival retention |
| 5.11 Dependencies/integration | §§10–11; checkpoint dependency and handoff schemas |
| 5.12 Extension/backfill | §12; bounded source/schema change and affected-evidence review |
| 5.13 Distinct completion gates | §10; no source-complete-to-synthesis-ready shortcut |
| 5.14 Stable reasoning classes | §11 and current execution profile |
| 5.15 Mutable/frozen/archive behavior | §§7,12; preserved prospective bytes and reciprocal supersession |
| 5.16 Entry/retrieval route | §1, current entrypoint and artifact map |

A future architecture review should test these responsibilities against actual edge cases, especially the two V15 witnesses, a later revelation affecting an earlier inference, ordinary behavior conflicting with a crisis impression, and a register shift with multiple explanations. Passing a heading-count check alone is not semantic acceptance.

## Prospective amendment record

- **2026-11-13 — v1.1:** Linked the initiation-policy §5.3 current-unit story synopsis to the local method for future eligible Japanese prose readings. Existing analytical responsibilities, witness distinctions, INITIAL lifecycle and CLOSED authorization boundary remain unchanged.
