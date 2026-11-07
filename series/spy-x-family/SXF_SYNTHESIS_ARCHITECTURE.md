---
title: "SPY x FAMILY — Synthesis Architecture"
artifact_id: SXF_SYNTHESIS_ARCHITECTURE
artifact_type: synthesis_architecture
version: "1.0"
status: canonical
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
authority_generation: SXF-INITIAL
authority_scope: "INITIAL bootstrap rules and attributed metadata only; no literary findings"
source_boundary: "Metadata only: Japanese main manga V01–18 plus separate EYES ONLY fanbook; no narrative admitted"
created: 2026-11-07
last_updated: 2026-11-07
architecture_lifecycle: INITIAL
recommended_reasoning_class: PREMIUM_QUALITY_FIRST
---

# SPY x FAMILY synthesis architecture

## 1. Purpose and INITIAL authority

This architecture keeps **knowledge, enacted role, observed conduct and directed relationship** distinct while allowing evidence to show how they interact. It is designed to prevent an omniscient reader's information from being assigned to a subject, a role label from replacing lived behavior, or a fanbook assertion from silently entering prospective main analysis. No unread plot or character situation is asserted.

The planning boundary is Japanese main V01–18 plus separately cataloged EYES ONLY. No narrative or fanbook content is admitted. The [current entrypoint](CURRENT_STATE_AND_CORPUS_MAP.md) routes present authority; the [method](SXF_ANALYTICAL_METHOD.md) governs readings. INITIAL canonical authority covers these rules and attributed metadata only, with owner acceptance and readiness unclaimed.

The [initiation policy](../../governance/source-policies/MANGA_ANIME_PROJECT_INITIATION_AND_ARCHITECTURE_POLICY.md), [generic architecture](../../governance/analytical-methods/GENERIC_MULTI_DOCUMENT_SYNTHESIS_ARCHITECTURE_TEMPLATE.md), [reconstruction method](../../governance/analytical-methods/GENERIC_CHARACTER_RECONSTRUCTION_METHOD.md) and archive/execution/handoff governance remain controlling in their responsibilities.

## 2. Source classes and authority

Locked, readable, actually inspected Japanese main pages support claims about that witness's narrative and art. Metadata reports presence/identity, not content or readiness. Page order, completeness, legibility and inspection require their own verification.

EYES ONLY has a separate witness and component taxonomy: profile/data, editorial text, creator statement, interview, commentary, illustration, technical explanation, narrative/bonus or unresolved. “Official” does not confer one uniform evidentiary status. Stated intent, background data and depicted action answer different questions. Preserve the exact speaker, publication boundary, source type and contradiction where relevant.

A main prospective reading cannot use a later companion fact merely because it is available in the folder. Comparison requires separately authorized components and an explicitly retrospective or comparative scope. Shared creator identity with Shihou Yuugi supplies no narrative continuity. Adaptations, other editions and later acquisitions remain excluded until scoped and admitted.

Derived prose/ledgers/models route primary evidence; repeating their claims does not create independent support. External/contextual material is labeled and bounded. Primary pages, OCR, private source receipts and access identifiers remain outside Git.

## 3. Existing infrastructure and future homes

Five initialized registers divide recurring duties:

| Current home | Responsibility and limit |
|---|---|
| [Source/fanbook register](SOURCE_AND_FANBOOK_REGISTER.md) | Witness/version, component/page coverage and source-layer boundaries; not inspection itself |
| [Knowledge/role/disclosure matrix](KNOWLEDGE_ROLE_AND_DISCLOSURE_MATRIX.md) | Actor-specific information, audience-directed presentation and causal information flow; not motive certainty |
| [Relationship/routine/voice ledger](RELATIONSHIP_ROUTINE_AND_VOICE_LEDGER.md) | Directed ties, ordinary conduct, subject state and Japanese expression; not a monograph/model |
| [Page-form/claim ledger](PAGE_FORM_AND_CLAIM_LEDGER.md) | Deterministic evidence, developed causal/formal claims, rival readings and revision history |
| [Checkpoint/reconstruction register](CHECKPOINT_AND_RECONSTRUCTION_REGISTER.md) | Atomic closeout, freezes, role gaps, dependencies, coverage/evaluation and full-output handoff |

The current map and governing pair complete the existing Markdown foundation. No reading, specialist, model or archive directory exists just to fill a template.

Future full source readings use `readings/SXF_JP_Vnn_READING.md`. Checkpoints use `checkpoints/SXF_CPnn.md`. Evidence-earned subject, relationship, information/form or institutional studies have distinct topical homes under `studies/`. A separately admitted companion analysis uses `studies/paratext/SXF_EYES_ONLY_STUDY.md`. Continuous integration uses `synthesis/SXF_CONTINUOUS_SYNTHESIS.md`. Future reconstruction separates evidence, model and independent tests under `reconstruction/<subject-id>/`.

These planned homes do not authorize work. A new artifact requires independent responsibility, adequate evidence, declared boundary/authority and a current route. Revise an established topical home rather than create competing near-final summaries.

## 4. Responsibility matrix

| Dimension | Full reading capture | Cumulative home | Later destination |
|---|---|---|---|
| Source and component coverage | Exact witness, actual page map/inspection and exclusions | Source register | Every derivative boundary |
| Actor/reader knowledge | Proposition, knower, acquisition, belief/error, disclosure and uncertainty | Knowledge matrix | All subject/causal studies; information/form specialist if earned |
| Role/audience presentation | Actor, audience, observed presentation, supported objective and audience inference | Knowledge matrix | Role/institution specialist when warranted; monographs |
| Causal choice | Conditions, perception, appraisal, options, action/non-action and consequences with rivals | Knowledge matrix + full claim home | Continuous causal interpretation |
| Directed relationships | A→B and B→A, observed practice, obligations, knowledge/power asymmetry | Relationship ledger | Independent relationship studies when justified |
| Ordinary life and state | Routine, low-stakes controls, disposition/temporary condition and change causes | Relationship ledger | Every subject/relationship study and future model |
| Japanese voice | Exact forms, recipient, speech act, register/lettering and alternative gloss | Relationship ledger | Character/form studies; written/graphic model only |
| Page form and tone | Layout, reaction timing, silence, rendering, language/image interaction and rivals | Page/claim ledger | Formal specialist if recurring question earns it |
| Institution/domain | Stated rule/custom/observed enforcement, access/resources and exceptions | Knowledge matrix | Evidence-earned specialist, not assumed theme |
| Paratext comparison | Component authority, exact pairing, agreement/disagreement, publication boundary | Source + claim ledgers | Separate companion study after admission |
| Counterreading/revision | Strong alternatives, disconfirmation, former/new claim and dependencies | Page/claim ledger | Every developed output |
| Coverage/reconstruction | Time/context/relationship/audience gaps and exposure-controlled tests | Checkpoint register | Distinct model/evaluator; NOT_ASSESSED |

A matrix cell or ledger row is not an adequate analysis of role, motive, care, obligation or a formal effect. Full readings retain the complete reasoning and alternatives. A brief summary may guide retrieval but cannot replace them.

## 5. Sequential transactions and checkpoints

Verify numbered order and actual chapter/page/spread mapping before a run. A volume is the candidate source unit with chapter/movement frontiers inside it. Publication time, depicted time, disclosure order, actor information acquisition and analyst admission remain distinct.

The authorized run specifies start, terminal boundary and checkpoint cadence. A prospective planning ceiling of four volumes between reconciliation checkpoints is subject to evidence density and owner run scope; it is not a story arc or current authorization. Significant knowledge/audience reclassification, source problems or unresolved dependencies trigger earlier review.

At each accepted reading, close complete prose and all five registers as one transaction. Freeze entering/exit states and prospective forecasts. Scoped no-change findings show actual inspection; missing pages or absent edits are not no-change evidence. Checkpoints preserve full earlier readings and state histories, then audit cross-unit knowledge, roles, directed ties, language/form and unresolved claims. They must not replace routine scenes with a few relationship labels.

## 6. State, continuity and epistemic model

The state key is `source lane + witness/version + admitted frontier + disclosure position + story-time constraints + subject + proposition/knowledge + audience/role + physical/affective/resource condition + directed tie + interpretive mode`.

Modes are PROSPECTIVE_AT_BOUNDARY, RETROSPECTIVE_WITHIN_ADMITTED_BOUNDARY, FANBOOK_COMPARATIVE and UNRESOLVED. A model or reading can use the analyst's admitted evidence to infer a subject's state, but cannot grant that subject facts only the reader knows. Each proposition carries its acquisition evidence and uncertainty.

A role/presentation record stores actor, audience, public behavior, stated or inferred intention and audience response separately. Performance can coexist with sincere feeling, habit or changing commitment; neither authenticity nor deception follows automatically. An observed tie, a claimed tie and inferred affect have distinct evidence routes.

State changes classify DISPOSITION, KNOWLEDGE, RELATIONSHIP, CONTEXT, ROLE, RESOURCE, REVEALED_NOT_NEW or UNRESOLVED. Preserve ordinary controls and rival causes. Source-required anonymity, aliases and later disclosures retain their original knowledge boundaries rather than being globally renamed.

Main and fanbook states remain separate even where their statements agree. Any continuity or factual conflict requires source-specific adjudication, not silent substitution.

## 7. Contradictions and historical revision

Classify disputes by witness/component, chronology/disclosure, knowledge asymmetry, sincere error, role/audience, report reliability, rendering/tone convention, interpretation, missing evidence or possible textual inconsistency. Multiple causes can remain live. An audience being misinformed does not prove the actor intended to deceive it.

Use PRESERVE, STRENGTHEN, REVISE, DOWNGRADE, REJECT and OPEN. Keep prior/new formulations, exact boundaries, decisive evidence, counterevidence, rival disposition, authority home and dependencies. Current-view pointers may change after review; historical state rows and full arguments survive.

Material revisions propagate independently through knowledge matrix, directed ties, voice/form claims, specialists and models. Frozen readings/forecasts remain intact. Later corrections use errata or superseding current claims with reciprocal authority metadata, not retrospective rewriting.

## 8. Monographs, specialists and integrated interpretation

Character monographs require sufficient temporal, relational, audience and ordinary-context coverage to sustain a full literary question. They integrate behavior, self-presentation, knowledge, motives/rivals, language and narrative function. They are not compressed profiles.

Relationship studies earn separate homes where directional development, performed/claimed ties, actual conduct, power or surrounding institutional conditions require sustained independent argument. Keep small routine changes and contrary evidence rather than only declarations or climactic moments.

Possible information-distribution, role/institution, routine/relationship and page-form specialists remain **anticipated**, not established themes. Commission only when source evidence creates a recurring load-bearing question. If no independent specialist is warranted, role review must justify that from evidence and assign who discharges the responsibility.

Specialists receive complete frozen readings and tested primary routes. They return full arguments with evidence returns, counterreadings and limits. Convergence resolves or retains disagreements and dependencies before synthesis readiness. The continuous synthesis connects information, action, role, relationship, language and form without turning every local scene into evidence for one preselected thesis.

## 9. Reconstruction as conditional, source-bounded modeling

Reconstruction is intended later for sufficiently evidenced, source-established subjects; none is identified or ready now. A monograph, model, test record and global capability assessment have distinct responsibilities. Designated agents own discovery/readiness registries.

A dossier separates evidence/retrieval, operational conditional policies and independent tests. Identity is subject@main-witness/frontier/state; admitted reader knowledge must be filtered to that subject's supported knowledge. Unadmitted fanbook facts and adaptation performance are excluded.

Twelve descriptive coverage dimensions are goals/values, threat/appraisal, motive conflict, knowledge/errors, attention/reasoning, affect/regulation, disposition/condition, directed relations, role/audience, repertoire/inhibitors, Japanese/graphic voice, development/exceptions. Record gaps and contradictions, not self-awarded readiness grades.

Each policy gives trigger/stakes/current state → response family, inhibitors/overrides, exceptions, support, counterevidence, rival and falsifier. Distinguish temporary condition from disposition. Trace appraisal → decision → communicative objective → recipient/audience-conditioned expression. Record confidence and distance from observed contexts; abstain or provide multiple plausible responses where evidence cannot discriminate. OBSERVED, CANDIDATE_POLICY and PROMOTED_POLICY are not interchangeable.

Test ordinary interaction, pressure/conflict, uncertain/false information, changed recipient/tie, role/audience shift and consequential choice where coverage allows. Separate decision fidelity from Japanese/graphic expression fidelity. A role-consistent utterance cannot prove the model understood motive or information state.

Freeze genuine held-out predictions before source exposure, separate model author and evaluator, and disclose latent familiarity. Exposed work is RETROSPECTIVE_CONSISTENCY_TEST. Independent evaluation uses SUPPORTED, PARTLY_SUPPORTED, CONTRADICTED, NO_DIAGNOSTIC_OPPORTUNITY, CONFOUNDED or UNRESOLVED, with baselines, diagnostic perturbations, decoys/negative controls and opportunity denominators where meaningful. No invented accuracy percentage.

Synthetic dialogue and scenarios remain derived tests, never canonical quotes, primary evidence or independent corroboration. Monograph quality cannot certify predictive readiness.

## 10. Independent gates

| Gate | Acceptance responsibility |
|---|---|
| S0 Foundation | Source/fanbook boundaries, sixteen duties, schemas and depth reviewed |
| S1 Admission/run | Selected source/capability verification, bounded owner authorization and OPEN precondition; absent now |
| S2 Sequential completion | Full source-facing prose and actual component coverage accepted |
| S3 Longitudinal reconciliation | Knowledge/role/audience, causal, relationship/routine and voice/form histories reconciled |
| S4 Claim stabilization | Tested central routes, retained alternatives and propagated revisions |
| S5 Character/specialist readiness | Role-gap and context/audience/ordinary/linguistic coverage assessed |
| S6 Specialist completion | Complete scoped monographs/studies with evidence and limits |
| S7 Specialist convergence | Conflicts/dependencies handled; no-specialist alternative justified and owned |
| S8 Integrated synthesis readiness | Complete full inputs, adequate role coverage and stable source boundary |
| S9 Synthesis acceptance | Sustained integrated argument retaining routine, causal, linguistic and formal depth |
| S10 Reconstruction evaluation | Independent exposure-controlled model assessment, separate from literary acceptance |
| S11 Final validation | Actual files checked for routes, authority, names/references, depth and outstanding debt |
| S12 Release/freeze | Defined immutable corpus, limitations, current routes, history and integration acceptance |

Source-complete is not synthesis-ready. Main inventory closure does not imply fanbook closure, official full-work completion or new-run authorization. Genuine interpretive uncertainty may remain explicit; missing required evidence cannot be disguised as certainty or harmless ambiguity.

## 11. Execution, handoff and future growth

SUBSTANTIVE_ANALYSIS governs future readings and interpretive updates; DEEP_SYNTHESIS covers checkpoints, monographs, specialists, models/evaluation; PREMIUM_QUALITY_FIRST covers propagation-sensitive architecture and integrated synthesis. Stable indexing is BOUNDED_STANDARD and hashing ROUTINE_FAST. Resolve actual settings through the [reasoning policy](../../governance/source-policies/MANGA_ANIME_REASONING_AND_MODEL_ROUTING_POLICY.md), never invent them.

The [long-series protocol](../../governance/source-policies/MANGA_ANIME_LONG_SERIES_HYBRID_EXECUTION_PROTOCOL.md) favors local source-capable readings/ledgers, fresh fully supplied synthesis, independent review and designated integration. Current capability is metadata/documents only. Verify transport, processing, STILL_IMAGE/TEXT inspection, interpretation and persistence under [capability routing](../../governance/source-policies/MANGA_ANIME_EXECUTION_TOPOLOGY_AND_CAPABILITY_ROUTING_POLICY.md).

[Handoffs](../../governance/source-policies/MANGA_ANIME_ANALYTICAL_HANDOFF_AND_INTEGRATION_CONTRACT.md) contain base snapshot, complete input/output paths/digests, authority, source/admission/knowledge boundary, owners and unresolved obligations. Full returned outputs and change/evidence manifests are compared against both handed-off base and current target. Retrieve consequential evidence and inspect for lost ordinary routine, linguistic ambiguity, role/knowledge distinctions and counterarguments. One mutable owner per register applies.

Add sources only after identity and scope reconciliation; new inventory does not extend a run. Add infrastructure for demonstrated recurring responsibilities and record schema migration/proportional affected-evidence backfill. Current registers retain append-only history; accepted readings and checkpoints freeze. Create archive homes only for genuine superseded reasoning, with reciprocal authority metadata.

## 12. Sixteen-duty trace

| Duty | Discharge |
|---|---|
| 5.1 Purpose/scope/generation/authority | §1 and current map |
| 5.2 Source ranking | §2 and source register |
| 5.3 Sequential contract | §5 and method |
| 5.4 Cumulative infrastructure | §§3–4 and five operational registers |
| 5.5 Character/relationship synthesis | §8 and relationship ledger |
| 5.6 Specialist domains | §§4,8; anticipated versus earned |
| 5.7 Deterministic retrieval | Method §3 and page/evidence schema |
| 5.8 Revision/history | §7 and claim versions |
| 5.9 Temporal/epistemic/continuity | §6 and knowledge matrix |
| 5.10 Contradictions | §7 and classified disputes |
| 5.11 Dependencies/integration | §§10–11 and checkpoint register |
| 5.12 Extension/backfill | §11 |
| 5.13 Separate completion gates | §10 S0–S12 |
| 5.14 Reasoning classes | §11 |
| 5.15 Mutable/frozen/archive | §§7,11 |
| 5.16 Entry/retrieval | §1 and topology §3 |

Stress review with an actor who has less information than the reader, an audience-dependent utterance with multiple motives, ordinary conduct that complicates a declared role, and a later fanbook assertion. These are methodological scenarios, not invented source events.
