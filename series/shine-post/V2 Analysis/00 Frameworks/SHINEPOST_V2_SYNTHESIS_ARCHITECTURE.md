---
title: "SHINE POST V2 — Synthesis Architecture"
artifact_id: SHINEPOST_V2_SYNTHESIS_ARCHITECTURE
artifact_type: synthesis_architecture
series: SHINE POST
series_id: shine-post
generation: V2
version: "1.1"
status: canonical
architecture_lifecycle: INITIAL
authority_scope: "V2 document responsibilities, cumulative integration, qualification and convergence gates; design only"
source_boundary: "Japanese television anime E01–E12 intended; no V2 source admission or inspection at bootstrap"
canonical_home: series/shine-post/V2 Analysis/00 Frameworks/SHINEPOST_V2_SYNTHESIS_ARCHITECTURE.md
created: 2026-11-19
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
do_not_use_as_literary_evidence: true
recommended_reasoning_class: PREMIUM_QUALITY_FIRST
---

# SHINE POST V2 — Synthesis Architecture

## 1. Purpose, scope and authority

The architecture carries episode evidence into cumulative character, relationship and audiovisual understanding, then into independently usable syntheses. It aims to retain the people beyond their largest dramatic moments and to explain what the anime's performed form contributes. These are analytical questions, not preselected answers.

The [analytical method](SHINEPOST_V2_ANALYTICAL_METHOD.md) governs how evidence is inspected and judged. This document owns where each responsibility lives and what must be complete before an output can claim readiness. The [root entrypoint](../../CURRENT_STATE_AND_CORPUS_MAP.md) is the single current route and operational state. The bootstrap initializes this design; it supplies no new literary evidence.

The intended source is the Japanese TV anime E01–E12. The [source register](../01%20Source%20and%20Intake/SHINEPOST_V2_SOURCE_AND_INTAKE_REGISTER.md) records which episode witnesses, streams and derivatives have been verified. Correspondence with a candidate edition is checked during candidate intake. The unit of sequential reading is one complete admitted episode. Songs, scenes, shots and performance passages are evidence units within episodes; they are not extra episodes or independent canon. Later admissions must specify medium, edition and continuity rather than blending the franchise.

V1 remains byte-preserved in its established home. Its existing current findings retain their recorded scope until specific evidence-supported revisions exist. V2 framework authority does not claim a higher literary authority merely because of its generation label. Incoming Antigravity artifacts retain their original producer/version identity; V2 means the integrated project generation, not a retroactive rename of someone else's pass.

## 2. Canonical responsibility matrix

| Responsibility | Single cumulative or governing home | Local evidence / future output |
| --- | --- | --- |
| Current authority, gate and next operation | [Root entrypoint](../../CURRENT_STATE_AND_CORPUS_MAP.md) | Links to current homes, not duplicated analysis |
| Inspection and argument | [Method](SHINEPOST_V2_ANALYTICAL_METHOD.md) | Episode readings and source-aware reviews |
| Candidate transfer, capability, clocks and reconciliation | [Intake/AV protocol](SHINEPOST_V2_AV_RECONCILIATION_AND_INTAKE_PROTOCOL.md) | Actual receipt, observation log and disposition records |
| Witness, derivative and intake identity; coverage receipts | [Source/intake register](../01%20Source%20and%20Intake/SHINEPOST_V2_SOURCE_AND_INTAKE_REGISTER.md) | Exact source/derivative references; private media outside Git |
| Stable identity, developmental state, ordinary life, voice, capabilities and individual knowledge | [Character state ledger](../03%20Longitudinal%20Ledgers/SHINEPOST_V2_CHARACTER_STATE_LEDGER.md) | Episode evidence; qualified monographs |
| Directed attachment, trust, conflict, obligations and role asymmetry | [Relationship ledger](../03%20Longitudinal%20Ledgers/SHINEPOST_V2_RELATIONSHIP_LEDGER.md) | Episode evidence; earned relational synthesis |
| Music, performance, sound, movement, framing, editing and recurring motifs | [Performance/form ledger](../03%20Longitudinal%20Ledgers/SHINEPOST_V2_PERFORMANCE_AND_FORM_LEDGER.md) | Complete musical events; earned specialist synthesis |
| Source observations, Japanese quotations/translation notes, claims, uncertainty and revisions | [Evidence/claim ledger](../03%20Longitudinal%20Ledgers/SHINEPOST_V2_EVIDENCE_AND_CLAIM_LEDGER.md) | Bounded locators, alternatives, disputes, V1/candidate transitions |
| Story/presentation chronology, audience disclosure, recurring institution/world constraints | Evidence/claim ledger | Episode-local causal account; character-specific knowledge in character ledger |
| Monograph qualification and production obligation | Character state ledger | Separate self-containment and fidelity decisions |
| Reconstruction rules and validation boundaries | [Reconstruction protocol](SHINEPOST_V2_CHARACTER_RECONSTRUCTION_PROTOCOL.md) | Models/validation created only for a real authorized question |
| Source completeness, role gaps, acceptance, handoff and closure evidence | `07 Audits and Handoffs/` | Distinct bounded records; bootstrap manifest already exists |
| Legacy findings and provenance | [V1 map](../../V1%20Analysis/00_README_AND_CORPUS_MAP.md) | Original episode, character, specialist and synthesis artifacts |

An episode reading owns its local argument. A ledger owns the current cumulative state and recoverable change history for its responsibility. A synthesis owns a developed cross-episode explanation. Link between them; do not copy one claim into several rival current formulations. A one-off observation can stay in its episode reading with an evidence route. Promote it to cumulative state when it changes an ongoing question, relation, rule, motif or interpretation.

## 3. Layout and artifact creation

All new analytical work belongs under `V2 Analysis/`. The following paths are an allocation plan; uncreated directories and artifacts are deliberately not live links.

| Directory | Creation rule |
| --- | --- |
| `00 Frameworks/` | Four current framework documents initialized at bootstrap |
| `01 Source and Intake/` | Source/intake register now; create exact receipt/publication records only from real deliveries |
| `02 Sequential Episode Readings/` | Create each reading only after lawful admission/execution; use `SHINEPOST_V2_E01_DEEP_READING.md` through the actual accepted units |
| `03 Longitudinal Ledgers/` | Four initialized ledgers; no invented analytical rows |
| `04 Character and Relationship Syntheses/` | Each evidence-qualified individual's monograph and genuinely useful relationship syntheses |
| `05 Specialist Syntheses/` | Only a recurring analytical object that earns a separate responsibility |
| `06 Full-Series Synthesis/` | A converged source-bounded full-series account after its gates |
| `07 Audits and Handoffs/` | Bounded review, integration, validation and immutable decision records |

Name durable artifacts with stable identity, `artifact_type`, source boundary, generation/version, authority scope, `canonical_home` and the complete authority quartet. Use exact lowercase machine authority states. A future substantive episode artifact must declare a correct sequential type such as `anime_episode_deep_reading`; hiding it under an administrative type does not authorize publication.

The bootstrap ledgers carried a no-literary-evidence flag while they contained schemas only. Each ledger's first admitted findings require its authority scope, source boundary and evidence-use flag to be updated in the same transaction. Design protocols, source/administrative receipts and routing documents retain their own non-literary responsibility. Do not let bootstrap metadata misrepresent later analytical content.

Do not create empty monographs, speculative specialist essays, duplicate indexes, a second current-state page or per-agent permanent ledgers. When a formal model or validation program is actually commissioned, assign its one canonical home and evidence dependencies here before substantive work. The reconstruction protocol governs its content. It need not be built merely to finish a literary synthesis.

Use `04 Character and Relationship Syntheses/SHINEPOST_V2_<PERSON_ID>_<BOUNDARY>_CHARACTER_MONOGRAPH.md` for individual portraits: a stable verified person token and the actual evidence boundary, with the exact created path recorded in the qualification decision. A relationship synthesis uses `SHINEPOST_V2_<RELATIONSHIP_ID>_RELATIONSHIP_SYNTHESIS.md` in that directory; an earned specialist uses `05 Specialist Syntheses/SHINEPOST_V2_<RESPONSIBILITY>_SYNTHESIS.md`. The eventual series account is `06 Full-Series Synthesis/SHINEPOST_V2_FULL_SERIES_SYNTHESIS.md`. These conventions assign future identity; none is a placeholder artifact or asserted qualification.

## 4. Intake and sequential transaction

Verify each admitted episode's primary witnesses through the source register. For the owner's independent E01–E12 run, the crew reads those witnesses in order and preserves the accepted episode transactions. The producer's analytical corpus and the V1 literary conclusions remain sealed throughout that work. After the twelve independent readings, their evidence and the first-pass review have been durably frozen, recover the candidate and its provenance, compare the editions and choose its publication route under the intake protocol. Candidate recovery belongs to retrospective reconciliation. Its prior completion grants no new sequential admission.

After the correct admission and run state exist, each episode transaction proceeds from prior accepted state to source inspection, independent specialist findings, independent critical review, claim reconciliation and cumulative integration. The episode output contract is in method §§5–8. The principal/integrator is accountable for the whole unit and is the sole shared-state writer. Independent participants retain source, exposure, coverage and objection records; they do not silently edit the principal's analysis.

For each accepted episode, update character, relationship, performance and evidence/claim changes, or explicitly record why a responsibility had no material delta. Update actual source coverage and unresolved required items. A reading and its ledger updates form one semantic transaction. If interrupted, record the accepted boundary and incomplete work; do not advance the entrypoint to an unaccepted draft.

The standing AV mirror profile supports independent verification of a received continuous-AV candidate. It does not imply the original pass followed today's multi-agent method. A fresh source review may repair current evidential gaps without rewriting the producer's historical procedure or exposure.

## 5. Temporal, epistemic and continuity state

Use episode/presentation boundary and reconstructed story time as separate coordinates. Each character record distinguishes enduring disposition, developmental state, local situation, available knowledge and later disclosure. Each relationship edge records whose attitude or action is being described. Audience inference belongs in the evidence/claim ledger; it is not automatically character knowledge.

Recurring institutional rules, world mechanisms or constraints receive source-bounded claim records with confidence, exceptions and disconfirmation criteria when the anime establishes them. Local explanatory details stay local. Do not invent a world bible or assume a mechanism because a V1 conclusion describes one. If a recurring system earns independent synthesis, declare its responsibility before creating that artifact.

Episode exit states are bounded by their declared admitted source. Retrospective comparison may refer to later evidence only when marked as such. Preserve real earlier formulations and forecasts, if any; never backdate revised understanding. Different continuities or editions require separate identity and explicit comparison, not silent harmonization.

## 6. Claims, conflicts and propagation

Evidence and claim IDs are stable within V2. The claim ledger owns initial wording, current formulation, source routes, alternatives, disconfirmation tests, status and append-only revision history. Link the original V1/candidate artifact and exact passage when a comparison is made. Use `PRESERVE`, `STRENGTHEN`, `REVISE`, `DOWNGRADE`, `REJECT` or `OPEN`; absence of review is not `PRESERVE`.

Resolve source-identity, timing or attribution conflicts before using their dependent claims. A material interpretation disagreement with compatible observations may remain plural. If a source observation cannot be tested in the integrator's lane, use the bounded return/verification route in the AV protocol. Do not settle it by provider prestige, majority vote or repeated polling.

Every revision checks dependent state rows, musical-event consequences, monographs, specialist syntheses, full synthesis and any model/validation records. Record the affected IDs and dispositions in the same revision transaction. An unresolved material dependency remains visibly provisional or blocks the corresponding completion claim. A frozen artifact receives a separately attributable erratum or successor; preserve its original bytes and chronology.

## 7. Person-level and relationship synthesis

At specialist readiness, assess every evidence-bearing individual for monograph qualification, including supporting characters and adults. No fixed roster, V1 index membership or prominence threshold replaces an evidence-based decision. Record qualification in the character ledger as `QUALIFIED_PENDING`, `COMPLETE_AT_BOUNDARY`, `DEFERRED_EVIDENCE` or `REASSESS_AFTER_REVISION`, with boundary and reason. An unassessed individual has no qualification result yet.

Every qualified individual needs a self-contained monograph meeting all fourteen responsibilities in the reconstruction protocol. It must make the person intelligible without requiring ledger retrieval: history, psychology, cognition, behavior, voice, directed relations, ordinary preferences, source-bounded romance if supported, capabilities, development, operational summary, limits and traceability. Unknown domains stay unknown. A dyad essay cannot replace either qualified individual's monograph.

Check self-containment and source fidelity independently, with actual evidence scope and reviewer dispositions. A fluent monograph can fail fidelity; a heavily cited record can fail to explain the person. A compact operational summary is useful but does not confer validated reconstruction capability. Relationships may receive a separate synthesis when it adds a cross-episode argument; each participant remains independently retrievable.

## 8. Specialists, convergence and completion

Potential specialist responsibilities include musical dramaturgy, performed Japanese voice, public/stage versus private presentation, management and group coordination, and recurring visual form. These are candidates, not mandatory essays or asserted themes. Create a specialist only when repeated evidence requires an independent cross-episode account that would otherwise be too thin or misplaced.

At the first accepted multi-episode tranche, a major source/role change, and sequential completion, conduct a proportional architecture/role-gap review. Mark each responsibility `SATISFIED`, `PARTIALLY_SATISFIED`, `MISSING`, `MISROUTED`, `TOO_THIN` or `NOT_APPLICABLE`, with evidence and a concrete action. Use one evolving ledger only when recurrence earns it; otherwise put the bounded review in an audit record.

| Gate | Evidence needed before claiming it |
| --- | --- |
| Framework initialized | Current method/architecture, responsibility homes and explicit gate; satisfied by this design scope |
| Source/run readiness | Verified identity and authorized boundary, adequate required channels, capabilities, genuine assignments and consistent initiation/continuation record |
| Episode accepted | Full unit contract, actual coverage, independent review, objections/dispositions and cumulative deltas complete |
| Sequential pass complete | Every admitted unit accounted for; material coverage and unresolved-item audit; no hidden omissions |
| Specialist/monograph readiness | Role-gap review, qualification decisions, sufficiently stabilized claims and known source gaps |
| Convergence | Qualified monographs complete or accurately blocked; required specialists and claim revisions integrated; dependencies reconciled |
| Full-series synthesis accepted | Source-bounded causal, character, relational and formal argument; alternatives; remaining uncertainty; independent critical review and traceable evidence |
| Reconstruction validated | Separate task-specific model, tests, exposure records, errors and assessment under the reconstruction protocol |
| Release/closure | Authority routes, boundaries, unresolved claims, manifests and actual execution closure agree under live policy |

The final synthesis must explain the series across these responsibilities rather than concatenate episode summaries or force agreement among competing interpretations. Twelve completed episode files alone do not establish convergence. A literary release need not invent a reconstruction assessment; a later model cannot infer validation from that release.

## 9. Reasoning, mutable state and retrieval

| Responsibility | Starting reasoning class |
| --- | --- |
| Mechanical inventory, hashing and link checks | `ROUTINE_FAST` |
| Bounded source metadata and receipt checks | `BOUNDED_STANDARD` |
| Episode analysis, source-aware specialists and critical review | `SUBSTANTIVE_ANALYSIS`; escalate for material ambiguity |
| Mature monographs, specialist synthesis and difficult reconciliation | `DEEP_SYNTHESIS` |
| Architecture decisions or propagation-sensitive full convergence | `PREMIUM_QUALITY_FIRST` when warranted |

Resolve actual model/effort through current governance at execution time and record observed settings only. No provider or product name is an evidence grade. Acceptance quality, missing evidence and rework matter more than a declared tier.

The premium recommendation for architecture work addresses propagation risk: an inconsistent boundary or responsibility can spread through the entrypoint, intake procedure and all four cumulative homes. Its expected benefit is fewer authority contradictions, orphan responsibilities and missed dependencies. Assess that benefit through independent responsibility/gate review and the amount of correction required, rather than assuming the recommendation itself guarantees quality.

The entrypoint, source register, current ledger views and design contracts are mutable under targeted edits. Claim/revision history, delivered originals, frozen independent logs, source receipts and later accepted freezes preserve their historical bytes; corrections point forward. The bootstrap manifest is a bounded foundation record, not a second live progress tracker. Change architecture lifecycle only when substantive review warrants it and preserve the change reason and affected responsibilities.

Retrieval is: semantic hit → authority and boundary check → root entrypoint → current topical/episode home → claim/evidence route → exact primary witness. V1 remains reachable for its existing findings and provenance. Search rank, modification date and generation label never substitute for that authority check.
