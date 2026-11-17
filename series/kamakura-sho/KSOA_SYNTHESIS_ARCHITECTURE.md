---
title: "Kamakura Police Station — synthesis architecture"
series: "Kamakura Police Station: The Case Files of Asumi Ogasawara / 鎌倉署・小笠原亜澄の事件簿"
series_id: kamakura-sho
artifact_id: KSOA_SYNTHESIS_ARCHITECTURE
artifact_type: synthesis_architecture
generation: KSOA-G1
version: "1.2"
created: "2026-11-12"
last_updated: "2026-11-15"
status: canonical
scope: "Longitudinal evidence, claim revision, specialist responsibilities and series integration."
source_boundary: "KSOA-G1, seven accepted Japanese EPUB witnesses, through V07 EPI p[0151] and KSOA-V07-H-0015."
canonical_home: series/kamakura-sho/KSOA_SYNTHESIS_ARCHITECTURE.md
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
do_not_use_as_literary_evidence: true
architecture_lifecycle: STABILIZED
governing_method: KSOA_ANALYTICAL_METHOD.md
recommended_reasoning_class: DEEP_SYNTHESIS
---

# Synthesis architecture

## Purpose and source model

`KSOA-G1` is the initial analytical generation for Narukami's seven Japanese novels. It pairs with the [series method](KSOA_ANALYTICAL_METHOD.md) and supersedes no earlier architecture. The project will explain how the novels make events knowable through testimony, inference and narrative disclosure, how investigations depend on people and institutions, and how repeated professional and personal encounters alter what characters can do or know. The final synthesis needs to account for differences between cases as well as recurring patterns.

The [witness map](KSOA_SOURCE_AND_WITNESS_MAP.md) defines one observed Japanese EPUB witness per work, with images and paratext scoped by component. Japanese prose governs wording and narrated events. Image claims use the witnessed image and its placement. Paratext claims identify the creator or publisher voice and their evidentiary scope. Alternate editions, translations, related works and adaptations require their own identity and authorization. If admitted later, their evidence keeps its edition, language or continuity boundary. Case flashbacks receive both an event-time position and a disclosure position.

This design applies the repository's [initiation policy](../../governance/source-policies/MANGA_ANIME_PROJECT_INITIATION_AND_ARCHITECTURE_POLICY.md), [archive authority policy](../../governance/source-policies/ARCHIVE_AUTHORITY_AND_SUPERSESSION_POLICY.md) and [synthesis reference template](../../governance/analytical-methods/GENERIC_MULTI_DOCUMENT_SYNTHESIS_ARCHITECTURE_TEMPLATE.md). The [current state and corpus map](CURRENT_STATE_AND_CORPUS_MAP.md) is the sole first-read route and owns present authority, source frontier and next operation.

## From reading to synthesis

The canonical volume documents are `readings/KSOA_Vnn_DEEP_READING.md`, with a structured `novel_deep_reading` type. Each owns its continuous source-facing argument, paragraph locators for non-case passages, coverage by section, and committed prospective chapter freezes. The volume is the atomic advancement unit. The prologue, each chapter and the epilogue are smaller disclosure boundaries. A scene can have a finer freeze for a particular claim. A complete unit advances the reading, source coverage, case evidence, disclosure, longitudinal state, claims and current entrypoint together. Record when a home has no warranted update. Case IDs and natural units follow what the text establishes, so a case can span volumes and a volume can contain more than one investigation.

| Analytical dimension | Capture in each applicable unit | Canonical cumulative home | Final use | Day-one state |
|---|---|---|---|---|
| Witness and section coverage | Exact spans, verified role, images and fidelity gaps | [Source and witness map](KSOA_SOURCE_AND_WITNESS_MAP.md) | Completeness audit and source retrieval | Metadata and schemas initialized |
| Events and causal chronology | Time ranges, causal links, alternative timelines | [Case evidence ledger](KSOA_CASE_EVIDENCE_LEDGER.md) | Case reconstructions and cross-case causality | Schema initialized |
| Evidence, testimony and police work | Origin, acquisition, transfer, action, constraints and results | [Case evidence ledger](KSOA_CASE_EVIDENCE_LEDGER.md) | Procedural and institutional studies | Schema initialized |
| Reader and actor knowledge | Disclosure, access and open hypotheses at each freeze | [Disclosure and hypothesis ledger](KSOA_DISCLOSURE_AND_HYPOTHESIS_LEDGER.md) | Mystery structure and fair-play analysis | Schema initialized |
| Character, voice and relationship | Conduct, thought, register, context, directed state changes | [Character and relationship ledger](KSOA_CHARACTER_AND_RELATIONSHIP_LEDGER.md) | Monographs, dyadic/ensemble studies and reconstruction evidence | Schema initialized |
| Institution and professional ethics | Portrayed rule, asserted duty, practice, discretion, constraint and consequence | [Character and relationship ledger](KSOA_CHARACTER_AND_RELATIONSHIP_LEDGER.md#portrayed-institutional-practice) | Cross-case institutional and ethical synthesis | Schema initialized |
| Form, place and theme | Significant framing, wording, pace and setting effects with alternatives | [Claim revision ledger](KSOA_CLAIM_REVISION_LEDGER.md) for recurring propositions, volume readings for local detail | Narration, genre, Kamakura setting and thematic arguments | Schema initialized |
| Contradiction and change in interpretation | Original claim, evidence, competing reading, revised authority | [Claim revision ledger](KSOA_CLAIM_REVISION_LEDGER.md) | Current findings and durable disagreements | Schema initialized |
| Character reconstruction | Diagnostic passages and coverage opportunities in ordinary, professional and pressured situations | Character ledger and [reconstruction specification](KSOA_CHARACTER_RECONSTRUCTION_SPEC.md) | Scoped evidence assessment and separately authorized testing | Evidence routes and specification only |

An observation that matters only to a passage can stay in its volume reading. Repeated evidence that could change a cross-volume argument enters its row's cumulative home. Use cross-references when one passage supports different responsibilities. The case ledger owns what the evidence item is and how it entered the investigation. The disclosure ledger owns who could know what and when. The state ledger owns consequences for a person, directed relationship or institution. The claim ledger owns the later judgment about an interpretation.

### Volume reading openings

The [method's opening sequence](KSOA_ANALYTICAL_METHOD.md#opening-of-a-completed-volume-reading) places the source receipt, prior-volume developments and current-volume story synopsis before extended analysis in a completed volume reading. The synopsis is reader orientation through that volume's endpoint. Its links lead to the owning reading and evidence records. Prepare cutoff-bounded work from the disclosure ledger and the applicable freeze.

The V01–V07 readings are pinned by the [completed-run proof](.repository/completed-run-publication.json). Their retrospective openings live beside them at `readings/KSOA_Vnn_READING_INTRODUCTION.md`. The [corpus map](CURRENT_STATE_AND_CORPUS_MAP.md#accepted-readings) gives a synopsis-first route and a direct route to each preserved deep reading. Each opening identifies the witness and exit checkpoint and links onward to the full analysis. Evidence, forecasts, claim revisions and coverage remain in their existing canonical homes.

The [synopsis name-and-reference review](audits/KSOA_PRODUCER_REVIEW_AND_RECEIVING_HANDOFF.md#synopsis-name-and-reference-review) records the checked passages and editorial corrections for the seven openings.

## Evidence, state and revision

A mature claim links to its claim/version ID and stable section anchor, then to an evidence ID in the owning volume reading or case ledger, and from there to the exact witness, section, ZIP member and paragraph or element address. Use the volume reading for verified Japanese wording and glosses, and the witness map for packaging details. Use a dedicated retrieval matrix only when cross-case support or a body of disputed passages becomes hard to audit through those routes. A matrix points to the original evidence and claim IDs.

Maintain distinct event time, source disclosure and the evidence horizon at which a state is asserted. A character's later admission may clarify a prior motive, but it enters the reader's evidence horizon at its disclosure point. Classify potential conflicts before adjudication. Check differences in event time or reporting order, access or focalization, attribution, memory, deception, institutional reporting, language, edition and continuity. If two accounts remain incompatible, preserve both with diagnostic evidence, an explicit open issue and any targeted audit it warrants.

If V05 bears on a V01 inference, the V05 reading supplies new evidence IDs and a new horizon. The claim ledger links the V01 version to a V05 adjudication using the archive transitions, with support and counterevidence. Any changed character or institutional state gets its own dated state row. If the text has revealed an earlier condition rather than depicted a new change, record its original valid time and its V05 disclosure. Cite the V01 freeze for what could have been inferred then and the current eligible claim for the later interpretation. Revised claims route to dependent specialist sections through the ledger. Corrections to frozen material use attributable errata or successors, with reciprocal artifact supersession where applicable.

## Specialist and character studies

Before full-series integration, answer three questions using the completed corpus. Treat these as required responsibilities that can share a document when the evidence and argument overlap.

1. **Mystery form and causality.** Compare how cases distribute clues, hypotheses and investigative discoveries and how their resolutions earn or complicate retrospective coherence. Depend on case and disclosure reconciliation, including plausible alternatives and material information introduced after a reveal.
2. **Character and partnership.** Explain how recurring professional and private decisions, forms of address and asymmetric trust change across cases. Use baseline, turning-point, ordinary-life and counterexample evidence. Create monographs for subjects with distinct developmental or interpretive questions and sufficient independent evidence. Create a directed relationship or ensemble study when interaction itself needs sustained argument across cases. A case-local subject may warrant focused analysis where their agency and perspective materially affect the local case or the series argument.
3. **Policing, setting and literary form.** Examine how portrayed institutions, ethics and Kamakura's social and physical setting constrain actions and how narration makes those constraints meaningful. Test variation across cases. Keep any real-world comparison independently sourced and distinct from literary evidence.

Create specialist documents under `studies/` inside this project root when an argument requires its own home. Voice and language, geography/local history, and recurring thematic or ethical conflicts are anticipated specialist topics. Their breadth and standalone treatment depend on the actual readings. Keep local literary arguments in their volume readings when they have no material longitudinal role. The reconstruction specification governs possible derived work after evidence stabilizes. A monograph may supply input, and a tested reconstruction may prompt a new source check. Literary completion and reconstruction validation have separate acceptance decisions.

## Execution and acceptance gates

| Stage | Required input and evidence | Output and advancement condition |
|---|---|---|
| Foundation and admission | Foundation review under the initiation policy, recoverable owner authorization, adequate Japanese text capability, exact V01 witness, entering exposure record and gate consistency | Record `open`, `run_state: active`, matching next fields, actual mode, start and terminal limit under the [continuation policy](../../governance/source-policies/MANGA_ANIME_SEQUENTIAL_EXECUTION_SCOPE_AND_CONTINUATION_POLICY.md) |
| Sequential source completion | V01 first, then only the next authorized volume. Inspect each narrative section and any required image, account for remaining spine positions, verify key citations and close the ledger deltas | Commit the whole unit and confirm the new high-water mark before moving on. V01 alone uses `single_operation`. A bounded range may use `continuous_sequential` when explicitly authorized. At run close use the policy's completed-state fields and no next operation |
| Longitudinal reconciliation | Accepted readings and freezes, verified case closure or unresolved cases, identity and directed-state deltas, and covered/omitted sources | Reconcile at the first completed case, a meaningful middle boundary and after V07 when in scope. Preserve every earlier disclosure horizon. A distinct architecture/role-gap audit identifies missing responsibilities and backfill required for synthesis |
| Specialist readiness | Defined analytical question and scope, retrievable material claims, evidence and counterevidence, reconciled dependencies and scoped authority | Dispatch an immutable snapshot for the named argument. Partial source can support a bounded study when its claim scope is explicit |
| Full-series readiness | All V01–V07 accepted, completion and role-gap audits done, evidence and claims reconciled, required specialist arguments accepted | Resolve or bound cross-specialist disagreement. Produce one continuous series-level interpretation under explicit synthesis scope, with limitations and counterreadings |
| Validation and release | Scope-specific source/claim audit, role and editorial review, appropriate structural validation and integration checks. For authorized reconstruction, the separate operational test record | Record receiving acceptance and release/freeze state separately. Freeze an identified release only after acceptance, retaining exact evidence basis and residual limits |

Prospective checkpoints and complete volume reads are frozen at acceptance, with earlier commitments reproducible from Git. The entrypoint and cumulative views are mutable through attributable targeted changes. Source bindings and previous ledger rows retain their history. Use an erratum or reviewed successor for an immutable reading, and the applicable run-stop or terminal-closure rules when the owner adopts a seal. If circumstances interrupt a run, recover the committed high-water mark and authorization before resuming. Publication follows live repository rules, including active-to-completed or completed-run proof requirements where applicable.

## Ownership and reasoning

| Stage | Preferred owner and reasoning class |
|---|---|
| Inventory reconciliation and locator work | Source-capable local operator, `BOUNDED_STANDARD`. Mechanical row and link checks can use `ROUTINE_FAST` |
| Architecture and high-impact amendment | Source-grounded architecture author, `DEEP_SYNTHESIS`. Escalate fragile disclosure or dependency decisions to `PREMIUM_QUALITY_FIRST` where useful |
| Primary reading, ledger changes and checkpoints | One accountable principal per run with verified Japanese `TEXT` and the required `STILL_IMAGE` lane, supported by the standing source and review assignments below. Use `SUBSTANTIVE_ANALYSIS` for close reading, `DEEP_SYNTHESIS` for difficult revisions and checkpoints |
| Monographs, specialists and full-series integration | Prefer a fresh synthesis session with a pinned evidence snapshot. Use `DEEP_SYNTHESIS` for substantial specialists and `PREMIUM_QUALITY_FIRST` for series integration or propagation-sensitive audits |
| Receiving, convergence and publication | Git-capable local integrator verifies candidate scope, meaning, evidence and exact bytes. Housekeeping owns generated routing. CI agent or owner owns merge |
| Reconstruction and evaluation | Authorized model author and independent evaluator with horizon-appropriate access. Use `DEEP_SYNTHESIS` for model and test design, escalating adversarial or highly coupled review. Designated global agents own discovery and capability records |

The [reasoning policy](../../governance/source-policies/MANGA_ANIME_REASONING_AND_MODEL_ROUTING_POLICY.md), [capability policy](../../governance/source-policies/MANGA_ANIME_EXECUTION_TOPOLOGY_AND_CAPABILITY_ROUTING_POLICY.md), [inspection-lane policy](../../governance/source-policies/MANGA_ANIME_MEDIUM_AND_INSPECTION_LANE_ROUTING_POLICY.md) and [long-series protocol](../../governance/source-policies/MANGA_ANIME_LONG_SERIES_HYBRID_EXECUTION_PROTOCOL.md) guide assignments. Verify actual access, language and image fidelity, isolation and tooling before assignment. A transfer under the [handoff contract](../../governance/source-policies/MANGA_ANIME_ANALYTICAL_HANDOFF_AND_INTEGRATION_CONTRACT.md) pins the base commit, generation, exact source and knowledge frontiers, artifacts, required evidence and pending questions. The receiving integrator reviews the whole return and its evidence, preserves concurrent changes, records proposed claim transitions and checks drift before adoption.

Independent or blind passes require a distinct generation ID, a pinned witness and evidence cutoff, exposure disclosures and an isolated input view. Hold comparison criteria constant where practical. Keep their outputs outside the current route until reviewed. Use a later comparison to explain divergences at their own horizons and preserve both histories.

### Disclosure-bounded readings for a newly authorized unit

The principal reads the complete witness in order, owns the pre-revelation snapshots and integrates the reading and ledger deltas. An independent reader receives the authorized Japanese and the applicable entering disclosure horizon before seeing the principal's account. Reconstruct one contested inference from physical observation, attributed testimony, and what Motoya can know of Asumi's professional judgment or police constraints at that point. Return section/locator, witness, disclosure position, competing account and contrary evidence; preserve any prediction before learning the solution. A separate reviewer tests a load-bearing inference against the source and a contrary clue, checking who actually witnessed it and when it became available. Match each assignment to actual Japanese TEXT and direct STILL_IMAGE where a relevant image is used; disclose prior solution exposure.

Record assignments, actual inspected spans and channels, independent returns and material disagreements in the volume closeout. The principal records dispositions and updates the case, character/relationship or claim-revision home that owns the result. Use substantive analysis for each source judgment and deeper review for a resolution that changes earlier case attribution. Only an unusually bounded unit may combine specialist and review work in one context separate from the principal. Record why access, independence and critical scrutiny remain sufficient. At review, compare the integrated account with the evidence returns and restore any consequential detail lost in compression. Hold affected closure if the required source access or protected disclosure horizon cannot be recovered.

## V04 architecture review

The [midpoint reconciliation](audits/KSOA_V04_LONGITUDINAL_RECONCILIATION.md) moves this generation to `EVOLVING` through V04. The mystery study must explain direct action, enabling action and each actor's knowledge separately. V02 redirection, V03 successive assault and V04 key transfer and alleged instigation support materially different causal accounts. Each study should preserve the difference between verified physical absence and possible participation elsewhere. The completed readings and ledgers already preserve these roles, so this change requires no backfill. The character evidence now supports individual questions for both detectives in addition to their partnership. Final role placement and reconstruction readiness remain subject to the post-V07 review.

## V07 architecture review

The [terminal reconciliation](audits/KSOA_SOURCE_COMPLETION_AND_LONGITUDINAL_RECONCILIATION.md) and [role-gap audit](audits/KSOA_ARCHITECTURE_ROLE_GAP_AUDIT.md) establish the source and evidence basis. The five specialist studies and their [convergence review](audits/KSOA_SPECIALIST_CONVERGENCE.md) support the `STABILIZED` lifecycle. The two lead monographs and directed relationship study answer different questions. The mystery study tracks attribution and timing, and the policing study links access, place and prose. The [integrated synthesis](studies/KSOA_INTEGRATED_SERIES_SYNTHESIS.md) uses their bounded findings. This architecture amendment records those mature dependencies and the late cases’ distinct disclosure and concealment roles. No source-reading backfill is needed.

The [reconstruction readiness assessment](audits/KSOA_CHARACTER_RECONSTRUCTION_READINESS.md) records interpretive sufficiency and its limits. An operational candidate and its tests require their own authorization. The [release review](audits/KSOA_PRODUCER_REVIEW_AND_RECEIVING_HANDOFF.md) records producer validation and the receiving obligation.

## Independent reconciliation review (2026-11-15)

An independent, Claude-authored generation, **KSOA-CB1**, read the same seven witnesses blind. It used a sanitized methodological intake, had no exposure to KSOA-G1 interpretations, and froze before any comparison. A protocol registered before unblinding then compared the two generations. Independent adjudicators decided every material discrepancy against the Japanese text. Majority, length and confidence never decided. The [comparison and adjudication report](audits/KSOA_CB1_COMPARISON/KSOA_CB1_COMPARISON_AND_ADJUDICATION_REPORT.md) holds:
- the provenance and exposure record;
- the 129 discrepancy records;
- the dimension-by-dimension comparison;
- the integration record.

The review admits no source and alters no frozen reading. Its changes follow the existing revision routes:

| Responsibility | Canonical home |
|---|---|
| Corrections to the frozen deep readings | [Deep reading errata](audits/KSOA_DEEP_READING_ERRATA.md). The readings stay byte-unchanged; the errata govern their correction |
| Reader-facing openings | The `readings/KSOA_Vnn_READING_INTRODUCTION.md` pages, by targeted revision |
| Evidence additions and corrections | New rows in the case, disclosure and character ledgers, with existing rows preserved |
| Interpretive changes | `-RNN` revisions and new claims in the [claim revision ledger](KSOA_CLAIM_REVISION_LEDGER.md) |
| Comparison records | [`audits/KSOA_CB1_COMPARISON/`](audits/KSOA_CB1_COMPARISON/KSOA_CB1_COMPARISON_AND_ADJUDICATION_REPORT.md). The registers are historical inputs; the adjudications are canonical decisions |

KSOA-CB1 is an independently authored, noncurrent analysis with limited authority. It is not a second source of literary truth. Its frozen package remains outside Git and is identified by its manifest SHA-256, `35f7a16eddf07a6dffb0750e1146c34874d227a486886db36ca7bf9248113040`. Publishing it would require an owner-merged `frozen_generation_publications` binding under initiation policy §3.9.5. Where KSOA-CB1 contributed findings, they entered the canonical homes above only after adjudication.

### Character monograph qualification

This project's analytical purpose includes person-level literary synthesis. The [monograph qualification record](studies/KSOA_MONOGRAPH_QUALIFICATION_RECORD.md) is therefore the home for qualification decisions under the [self-contained character monograph standard](../../governance/source-policies/MANGA_ANIME_PROJECT_INITIATION_AND_ARCHITECTURE_POLICY.md#self-contained-character-monograph-standard).
- **Naming.** Monographs live under `studies/` and are named `KSOA_<GIVEN>_<FAMILY>.md`.
- **Supplying captures.** The volume readings, the character and relationship ledger, the case ledger and the disclosure ledger.
- **Eligibility.** Eligibility follows the standard's qualification test. The pre-standard criterion in [Specialist and character studies](#specialist-and-character-studies) operates only within that test and excludes no character the evidence qualifies.
- **Lead monographs.** The two lead monographs were generally revised to v2.0 under the standard.
- **Outstanding production.** Seven bounded or recurring non-lead characters qualify. Their monographs are outstanding production obligations, so the character layer is not complete until they exist.

## Architecture lifecycle and retrieval

At a complete early case, a material source or modality surprise, a midpoint reconciliation, or a synthesis boundary, review routing, coverage, dependencies and reasoning classes. Move from `INITIAL` to `EVOLVING` when recurring evidence justifies amendment, then to `STABILIZED` when the mature responsibilities are supported. Record material changes with scope, rationale, affected links and whether targeted backfill is necessary. Add a home when evidence recurs and accumulates independently or is otherwise materially hard to retrieve. Backfill only a material gap, first checking already accepted readings and using authorized source access when needed. A frozen release receives a new version for substantive changes.

Start with the [entrypoint](CURRENT_STATE_AND_CORPUS_MAP.md), then read the method, this architecture and witness map. Retrieve the prior eligible freeze and cumulative rows through the requested boundary before sequential work. Retrieve accepted volume readings and active claim versions before a specialist or final study. Repository routing and the entrypoint identify the current generation. Versioned histories and source locators supply the evidence when an argument is revisited.

The 2026-11-14 v1.1 amendment applies the opening sequence to future authorized readings and adds reader-facing introductions to the completed V01–V07 corpus. It addresses a retrieval gap in the original presentation using the already admitted Japanese evidence, with the completed reading transaction at `9fee95813a8df8c19621001ae7cb1c9bc02f76bc` as the fixed reading basis.
