---
title: "Road to the Top — Synthesis and corpus architecture"
artifact_id: UM_RTTT_SYNTHESIS_ARCHITECTURE
artifact_type: synthesis_architecture
series: uma-musume
installment: road-to-the-top
version: "1.0"
status: canonical
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
do_not_use_as_literary_evidence: true
authority_generation: UM-RTTT-INITIAL
source_boundary: "Original 2023 four-episode anime only; architectural foundation with zero accepted narrative observations"
canonical_home: series/uma-musume/installments/road-to-the-top/00_Method/UM_RTTT_SYNTHESIS_ARCHITECTURE.md
created: 2026-11-22
last_updated: 2026-11-22
recommended_reasoning_class: DEEP_SYNTHESIS
---

# Road to the Top — Synthesis and corpus architecture

This architecture defines how episode work will become cumulative, revisable analysis of **Road to the Top**. Its companion [analytical method](UM_RTTT_ANALYTICAL_METHOD.md) governs observation and interpretation. Neither document asserts that an episode has been read. The only canonical franchise first-read surface is [CURRENT_STATE_AND_CORPUS_MAP.md](../../../CURRENT_STATE_AND_CORPUS_MAP.md); the [installment README](../README.md) supplies local navigation. Initialization is **architectural bootstrap; sequential lock CLOSED; no active analytical run and zero accepted narrative records**. The current entrypoint and [readiness audit](../05_Run_State/UM_RTTT_READINESS_AUDIT.md) own the live state.

## 1. Purpose, authority and source topology

The project has one franchise root, `series/uma-musume/`, and an initial installment root, `installments/road-to-the-top/`. This V1 architecture is canonical for that bounded responsibility, with no earlier project architecture superseded. Repository authority, the [initiation policy](../../../../../governance/source-policies/MANGA_ANIME_PROJECT_INITIATION_AND_ARCHITECTURE_POLICY.md), [routing](../../../../../governance/AGENT_ROUTING.md), [archive policy](../../../../../governance/source-policies/ARCHIVE_AUTHORITY_AND_SUPERSESSION_POLICY.md) and publication controls remain governing. Canonical procedure is not narrative proof, source admission or analysis authorization.

The primary intended source is the original 2023 four-episode web anime in Japanese. The 2024 theatrical re-edit is a distinct version, not an interchangeable copy. Other franchise media remain separate/unadmitted; real racing history is external context. The [source inventory](../01_Sources/UM_RTTT_SOURCE_INVENTORY.md), [machine-readable source manifest](../01_Sources/UM_RTTT_SOURCE_MANIFEST.json) and [production metadata](../01_Sources/UM_RTTT_PRODUCTION_METADATA.md) bind actual availability, source IDs and edition uncertainty. A source ID may change admission status without changing its byte identity. New encode/edition bytes receive a separate identity; derive a documented mapping rather than recycling the previous clock.

Git contains methods, brief evidence references, analytical arguments, cumulative state and sanitized provenance. Full subtitles, primary video, extracted audio, frame collections, private acquisition receipts and runtime caches remain in the source/working planes identified by the inventory and [AV workflow](../01_Sources/UM_RTTT_AV_WORKFLOW.md). A screenshot collection is a partial derivative unless it meets the [episode-bundle semantic contract](../../../../../governance/source-policies/MANGA_ANIME_EPISODE_BUNDLE_SPECIFICATION.md). Sufficient evidence for a bounded question does not make a partial object a complete bundle.

## 2. Capture, cumulative homes and destinations

Each recurring observation has one canonical cumulative home. Episode prose may explain it and link its ID without duplicating mutable rows. The following day-one structures are required for this four-episode project because character change, rivalry and the audiovisual construction of competition are explicit research priorities. A home is initialized when its schema, ID rules, ownership and truthful zero-record state exist; initialization does not imply evidence has been entered.

| Dimension | Episode capture | Canonical cumulative home | Eventual destination | Bootstrap state |
| --- | --- | --- | --- | --- |
| Chronology, scenes, source locations and short Japanese evidence | Scene intervals and `SC`/`OBS` IDs | [Scene/evidence ledger](../03_Ledgers/UM_RTTT_SCENE_EVIDENCE_LEDGER.md) | All analytical claims and retrieval | Required day-one home; zero accepted observations |
| Emotional, cognitive, motivational and behavioral state | `CS` IDs with explicit/stated/inferred distinctions | [Character/relationship ledger](../03_Ledgers/UM_RTTT_CHARACTER_AND_RELATIONSHIP_STATE_LEDGER.md) | Character trajectories and every evidence-qualified individual monograph | Required day-one home; metadata identity only |
| Directed relationships, recognition and ordinary interaction | `RS` IDs; A→B distinct from B→A | Character/relationship ledger | Rivalry/recognition specialist or integrated relationship argument | Required day-one home; no accepted relationship claims |
| Claims, alternatives, adverse evidence and revisions | Stable `RTTT-CLM...` references | [Claim/interpretation ledger](../03_Ledgers/UM_RTTT_CLAIM_INTERPRETATION_LEDGER.md) | Specialist and installment synthesis | Required day-one home; no established narrative claims |
| Depicted race structure and emotional stakes | `RACE` ID; before/during/after evidence | [Race/competition ledger](../03_Ledgers/UM_RTTT_RACE_COMPETITION_LEDGER.md) | Racing form and adaptation arguments | Required day-one home; no depicted race presumed |
| Visual motifs, music, vocal performance, rhythm and inspection queues | Evidence ID, channel, clock and actual route | [AV/motif/performance ledger](../03_Ledgers/UM_RTTT_AV_MOTIF_PERFORMANCE_LEDGER.md) | Audiovisual specialist and integrated reading | Required day-one home; no viewed/listened claims |
| Prospective questions and disconfirming tests | Entering/exiting `RTTT-HYP...` status | [Research register](../04_Research/UM_RTTT_RESEARCH_QUESTIONS.md) | Tested, revised or unresolved arguments | Questions initialized; no conclusions |
| Historical racing context | `RTTT-CTX...` plus an independent source | Context section of race/competition ledger, linked from claim ledger | Carefully bounded adaptation specialist | Schema required; research acquisition may be deferred |
| Source admission, evidence coverage and readiness | Witness/stream/derivative status | Source inventory and readiness audit | Reproducible source boundary | Technical status separately recorded by inventory |
| Participation, review and atomic completion | Episode transaction and contribution/disposition tables | Episode artifact plus current run checkpoint | Auditable acceptance and resumability | Transaction templates only; no completed reading |

Minor observations that have no recurring responsibility may remain local to an episode, but mature claims still need stable evidence locators. Add an institution, trainer-specific or broader ensemble ledger only if recurring independent evidence cannot be served adequately by these homes. Empty symmetry folders are unnecessary.

## 3. Sequential episode completion contract

The [episode index](../02_Episodes/UM_RTTT_EPISODE_ANALYSIS_INDEX.md) and E01–E04 templates begin as **templates**, not completed analytical records. The principal's coverage follows the authorized unit, and an E01 run stops at E01. Completion requires all of these to be recoverable:

1. Correct admitted source/version/stream, calibrated citation clock, entering knowledge frontier and actual inspection coverage.
2. A front-of-reading episode synopsis, completed only after full-unit inspection, and a source-facing scene chronology rather than a plot-only account.
3. Source-located formal, character, linguistic and competition observations with interpretations and alternatives kept distinct.
4. Genuine independent specialist contribution and critical review, the decisive material each participant inspected, and integrator dispositions of significant findings.
5. Updated evidence, character/relationship, claim, race, AV and hypothesis homes wherever the episode changed them; explicit no-change results where appropriate.
6. Closure of required evidence for the declared responsibility, or an accurate incomplete/pending status identifying what remains.
7. Exit state and checkpoint consistent with the source frontier, authorization endpoint and unresolved questions.

Drafted prose, extraction success and a passing structural validator do not individually satisfy this contract. Advance the accepted high-water only after atomic completion; preserve a partially finished transaction for resumption without pretending the next unit is authorized.

## 4. Character and relationship synthesis responsibility

The initial longitudinal responsibility is for **Narita Top Road, Admire Vega and T.M. Opera O as individually identified characters in this edition**, with other people added when source evidence warrants it. Track ordinary-life choices, preferences, speech, cognition, obligations, self-report versus conduct, support, competitive behavior and counterexamples. Do not let a proposed theme replace a person, and do not infer a stable trait from a single conspicuous moment.

The mature responsibility includes an integrated account of the three trajectories and individual portraits for every character whose admitted evidence qualifies under the initiation policy's [self-contained character monograph standard](../../../../../governance/source-policies/MANGA_ANIME_PROJECT_INITIATION_AND_ARCHITECTURE_POLICY.md#self-contained-character-monograph-standard). Qualification depends on convergent, differentiated evidence with contextual or interpersonal variation and meaningful constraints or counterexamples; a role label, one memorable moment, popularity or appearance count is insufficient. Eligibility is not restricted to the three leads: supporting characters, trainers, adults and any other evidenced person must be considered. Absence from a dedicated ledger is not disqualification.

Record qualification decisions in the mutable character-monograph qualification section of [UM_RTTT_READINESS_AUDIT.md](../05_Run_State/UM_RTTT_READINESS_AUDIT.md), no later than specialist-synthesis readiness and again whenever a material revision changes relevant history, behavior, relations or speech evidence. Each actual assessment records stable character identity, episode/edition boundary, outcome, source-grounded rationale and largest gaps, next review trigger, and monograph path once a real portrait exists. Bootstrap has no qualification outcomes. Use exactly these outcomes:

| Outcome | Meaning and action |
| --- | --- |
| `QUALIFIED_PENDING` | A differentiated portrait is supported; producing the monograph is an outstanding obligation |
| `COMPLETE_AT_BOUNDARY` | A real monograph meets the standard at its stated boundary and both acceptance properties have passed |
| `DEFERRED_EVIDENCE` | Current evidence is insufficient; record the specific deficiency and reassessment trigger, preserving existing analysis |
| `REASSESS_AFTER_REVISION` | Material new evidence challenges eligibility or the current portrait; preserve the earlier assessment while reviewing it |

The eventual canonical portrait naming is `06_Synthesis/Characters/UM_RTTT_<KEY>_CHARACTER_MONOGRAPH.md`, relative to the installment root, where `<KEY>` is a stable documented character key, with `artifact_type: character_monograph` and complete authority metadata. This is a naming rule, not a link to or request for a placeholder. Create the real document when evidence qualifies it; there is one current portrait per character subject/continuity at a declared boundary. The episode observations, `CS`/`RS` histories, Japanese language evidence, AV observations, claims and counterexamples supply its evidence. They verify and deepen the portrait but do not carry information omitted from it.

Before a monograph is accepted, promoted, integrated as current or recorded `COMPLETE_AT_BOUNDARY`, record **self-containment** and **fidelity** as separate results in the acceptance/integration record and reference them from the qualification decision. Self-containment tests whether the monograph alone answers representative questions about personality, motives, cognition, typical and exceptional decisions, speech, directed relationships, ordinary preferences, development, conditional reactions and uncertainty. Fidelity independently checks load-bearing interpretations against source locators and current claims. Unknown dimensions are explicitly bounded, not invented to complete a form. The portrait must address the standard's full coverage responsibilities and remain readable without retrieving neighboring files merely to reconstruct the person. A claim grid alone is insufficient.

`QUALIFIED_PENDING` creates a production obligation. A bounded task may leave it pending, but specialist/full-installment readiness and release audits must list every outstanding portrait, and none may call the character layer complete while any remains. Unassessed means neither qualified nor rejected. Qualification is an evidenced judgment, not an additional approval request. This task does not initiate behavioral simulation or reconstruction-capability grading.

For relationships, retain directed state, context, ambiguity and asymmetry. A dyadic study earns a distinct home only when it has a substantial evidence-based argument beyond the three-character account. Rivalry, empathy, friendship, admiration, intimacy and possible romantic subtext are alternatives to assess, not a fixed ladder. Do not promote a franchise-wide relationship from one version's evidence.

## 5. Specialist responsibilities and dependency order

These are anticipated analytical responsibilities, not conclusions or a demand for one file per topic:

| Responsibility | Inputs and readiness | Scope |
| --- | --- | --- |
| Three protagonists and meanings of excellence | All four accepted episode states, adverse cases, wording and relevant performance evidence | Compare goals, public/private identities, duty and response to outcomes without fixed archetypes |
| Rivalry and interpersonal recognition | Directed relation history, gestures/dialogue and counterexamples | Test empathy, growth, intimacy and alternative social readings |
| Racing as audiovisual narrative | Accepted race/AV records, resolved load-bearing motion/edit/audio questions | Explain viewer experience using spatial, temporal and sound evidence |
| Visual/musical dramaturgy and episode form | Recurrence index including OP/vocal placement, differences and negative cases | Test formal patterns and their narrative function |
| Historical adaptation | Independently cited racing records plus anime observations, kept separate | Preserve/rearrange/personify/transform hypotheses; no inferred authorial intention from resemblance |

Specialist work may begin as bounded local research before all episodes are complete, but it must name that partial frontier and remain nonfinal. The integration order is: admitted source → independently reviewed episode transaction → synchronized longitudinal/claim state → evidence and required AV reconciliation → warranted specialists/character accounts → architecture/role-gap check → full installment synthesis → source/claim/link/readiness audit → optional release/freeze. Reconstruction, if ever separately authorized, follows its own standards after adequate literary integration.

The full installment synthesis requires all four episode responsibilities and cumulative state to converge. It must explain and test an argument rather than compile episode summaries. Lack of an optional historical enrichment does not invalidate adequate anime analysis; a historical-adaptation claim itself cannot be complete without the relevant external record. Sequential completion does not automatically authorize specialist or full-series synthesis.

## 6. Time, knowledge, contradiction and revision

Retain three distinct orders: presentation/disclosure order, inferred fictional chronology and external historical chronology. Record a character's knowledge at the scene, the principal's completed-episode knowledge and the project's admitted frontier independently. Later evidence may revise an earlier interpretation without rewriting the earlier prospective freeze. Post-episode commentary must name its later boundary.

Apparent conflicts are first classified: source/version difference; translation or timing issue; character ignorance/deception; subjective presentation; editorial ambiguity; external-history difference; or possible actual inconsistency. Do not harmonize them by guessing. Route source identity and offsets to the inventory; wording to Japanese verification; temporal/performance questions to the AV queue; interpretation to the claim ledger; franchise/edition divergence to the franchise integration register.

The claim ledger retains original formulation, supporting/adverse IDs, alternative explanation, epistemic status and confidence, revision date/frontier and downstream effects. Use `PRESERVE`, `STRENGTHEN`, `REVISE`, `DOWNGRADE`, `REJECT` or `OPEN`. A rejected claim keeps its ID and evidence trail. Revisions cascade to affected current state, episode interpretation and synthesis; frozen bytes receive an attributable erratum or successor. Agreement among models is not evidence promotion.

## 7. AV method family and evidence dependencies

The governing method's [AV companion and reconciliation profile](UM_RTTT_ANALYTICAL_METHOD.md#6-av-companion-racing-performance-and-musical-form) are part of this architecture. Text wording and exact frames have their own evidentiary routes; continuous movement, voice, music and timing need verified channels. Their cumulative home is the AV ledger, joined to race/character/claim IDs. Raw derivatives stay outside Git.

For each episode, the verification queue states neutral questions, source/interval, actual requirement and escalation state. The reviewer freezes independent observation before receiving the proposed claim. The integrator applies the corpus reconciliation protocol, accepts adequately anchored findings, records scope and limitations, and preserves unsettled load-bearing items as provisional. No permanent vendor, paid API, full-episode escalation or unavailable modality is assumed. An actual missing capability is recorded as a concrete unresolved requirement, not solved by sampling claims beyond what stills show.

## 8. Owners, stage routing and handoff

Use the simplest adequate `LOCAL_ONLY` arrangement for source access, extraction, episode work and Git integration in this bounded project; later handoff to another adequate authorized environment is permitted when useful. The standing substantive unit configuration is principal/integrator, independently contributing source-language/character specialist and a distinct critical reviewer; add a verified AV specialist for required temporal/performed evidence. No standard episode is preapproved for reduced participation. The principal sees the full episode; others inspect scope appropriate to their assignments. Fresh independent contexts must not inherit the principal's working conclusions.

One active writer owns each mutable artifact. Specialists return contributions; the integrator serializes cumulative-ledger and entrypoint updates. The episode transaction preserves assignment, independence/exposure, actual source coverage, significant observations, counterreadings, corrections and integrator disposition. This architecture creates no permanent per-agent ledger. If independence or required source perception is unavailable, preserve valid work and leave acceptance/high-water pending under the exact blocker.

| Operation | Reasoning class | Accountable owner |
| --- | --- | --- |
| Checksums, manifest copying and explicit-path checks | ROUTINE_FAST | Source/integration operator |
| Edition/readiness reconciliation and locator verification | BOUNDED_STANDARD; escalate ambiguous identity | Source operator and integrator |
| Episode reading and interpretive state updates | SUBSTANTIVE_ANALYSIS | Principal plus independent specialists/reviewer |
| Character/relationship and audiovisual specialist argument | DEEP_SYNTHESIS | Assigned specialist, with independent review |
| Architecture amendment or final integrated synthesis | DEEP_SYNTHESIS; quality-first where propagation risk warrants | Integrator/assigned synthesis author |

Reasoning classes do not certify perception or grant source authority. Record actual configuration only when observed. For a substantial cross-session handoff, use the [handoff contract](../../../../../governance/source-policies/MANGA_ANIME_ANALYTICAL_HANDOFF_AND_INTEGRATION_CONTRACT.md): exact base/source frontier, full named artifacts and hashes, required coverage, open claims, target paths, permitted edits and receiver acceptance. Check base drift before replacement and preserve supported detail and historical freezes. An abstract alone cannot transfer substantive analysis.

## 9. Franchise reconciliation boundary

The root README and franchise integration register remain the franchise-level discovery and comparison surfaces; this installment is their only initial analytical responsibility. A recurring character name does not prove continuous identity, knowledge or relationship state across games, manga, television and films. Admit another installment only under its own scope, witness inventory and method fit. Cross-installment claims require local evidence from each side and explicit continuity/version labels. Historical similarities belong to context until argued, never to shared fictional canon by default.

The future theatrical comparison requires both actual versions, separate source IDs/clocks, a source-to-source correspondence table, and a bounded question about additions, omissions, order, sound or staging. Preparing that comparison route does not authorize viewing the re-edit or substitute it for unavailable web episodes.

## 10. Completion, freeze and amendments

| Boundary | What must be true |
| --- | --- |
| Bootstrap complete | Navigation, paired foundations, usable ledgers/templates, real source reconnaissance and explicit remaining gates exist; no episode analysis claimed |
| First run eligible | Applicable initialization conditions met and explicit lock opened in the entrypoint; actual E01 source/clock/language/evidence access verified; independent roles and owner E01 run scope recorded |
| Episode complete | Atomic contract in Section 3 satisfied; no concealed required-channel gap |
| Sequential corpus complete | E01–E04 accepted within authorized runs, with accurate frontiers |
| Longitudinal state reconciled | Evidence and state/claim histories consistent, meaningful contradictions preserved |
| Specialist-ready | Required inputs and formal/character/historical evidence fit the declared responsibility; every character with differentiated evidence has a recorded qualification assessment |
| Installment synthesis-ready | Required specialist responsibilities resolved or legitimately scoped; architecture/role-gap check completed; outstanding qualified portraits listed and character layer not called complete while any remain; explicit synthesis authority recovered |
| Audited/released | Scope, quotations, evidence links, epistemic states, names/references and applicable repository checks pass; all outstanding portrait obligations listed with no false character-layer completion; any freeze and its limits explicitly recorded |

The bootstrap does not request a run closure or terminal byte seal: no sequential reading exists to seal. Current-state and cumulative ledgers remain mutable through targeted attributed changes. Accepted prospective freezes and any later explicit byte seals remain protected. Publication and `main` integration are separate repository controls; no architecture state substitutes for an exact-head audit.

Amend this architecture when a recurring independently accumulating dimension affects later synthesis and cannot be served by an existing home. Record version, evidence for need, changed responsibilities, affected current-state routes and bounded backfill, if material. Do not create new roots because a session or model changes. Optional questions may stay unresolved; do not invent an unrelated governance barrier or require a full-franchise corpus before the four episodes can be studied.

| Version | Change |
| --- | --- |
| 1.0 | Initial four-episode architecture and explicit synthesis responsibilities; zero accepted narrative records |
