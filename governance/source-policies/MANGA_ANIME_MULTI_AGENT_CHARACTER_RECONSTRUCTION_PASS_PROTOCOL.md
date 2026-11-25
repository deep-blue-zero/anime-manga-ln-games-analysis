---
title: Manga / Anime Multi-Agent Character Reconstruction Pass (MACRP) Protocol
artifact_id: MANGA_ANIME_MULTI_AGENT_CHARACTER_RECONSTRUCTION_PASS_PROTOCOL
artifact_type: character_reconstruction_pass_protocol
version: "1.0"
status: canonical
scope: corpus-wide, owner-invoked post-analysis operation for deepening the character evidence and reconstruction models of a mature series or study, in any medium
created: 2026-11-24
last_updated: 2026-11-24
maintainer: Claude + user
do_not_use_as_current_authority: false
do_not_use_as_literary_evidence: true
canonical_home: governance/source-policies/MANGA_ANIME_MULTI_AGENT_CHARACTER_RECONSTRUCTION_PASS_PROTOCOL.md
drafted_against_commit: bf571a7d5d47cf845f6ead633eb41b568b6e9659
supersedes: null
superseded_by: null
---

# Manga / Anime Multi-Agent Character Reconstruction Pass (MACRP) Protocol

> **A reconstruction pass makes a mature project's characters more specific, better evidenced and more transferable. It does this through independent multi-agent work on the project's existing analysis and, where the diagnosis requires, on its admitted sources. It changes canonical analysis only through the project's own correction routes. It never admits a source, grades a capability or writes a global registry.**

Character reconstruction, in this protocol, is the disciplined recombination of established behavioral mechanisms, dispositions, relationships, capabilities, preferences and state-dependent constraints in circumstances the source does not supply. A pass aims at that capability: reasoning about how a character would perceive, interpret, judge, feel, decide, speak, relate, live ordinarily, err, take correction and change, and where the evidence supports no determinate prediction. It does not aim at a deterministic personality algorithm, unrestricted role-play, a trivia encyclopedia or a longer monograph for its own sake. Better reconstruction does not mean eliminating uncertainty.

This protocol is an operation. It composes existing governance and adds only what a pass needs that no existing document standardizes: eligibility and diagnosis, mode selection, workstream ownership, the observation and mechanism conventions, reconciliation dispositions, the test battery and its exposure controls, baseline comparison, completion and referral records, and resumption. The [run record template](templates/MANGA_ANIME_MACRP_RUN_RECORD_TEMPLATE.md) and the [execution runbook](templates/MANGA_ANIME_MACRP_EXECUTION_RUNBOOK.md) implement it.

## 1. Purpose and applicability

### 1.1 Applicability

A pass is owner-invoked. It applies when an owner instruction names a MACRP mode for a registered `series/` or `studies/` root whose admitted analysis already supports differentiated character work (Section 2), in any medium: light novels and general fiction, manga, anime, visual novels, games, live-service narratives and mixed-media projects. One run covers one registered root; comparative work across roots belongs to a `studies/` root under its own run. Ordinary monograph production, a deepening pass under the long-series protocol, claim revision and evaluator work remain available under their own rules without invoking this protocol.

A project needs no amendment to become eligible. It adopts the protocol for a run by recording the run in its canonical entrypoint (Section 13.2).

### 1.2 What this protocol composes

| Responsibility | Governing document, which remains binding |
|---|---|
| Model structure, evidence classes, voice, conditioning, confidence and distance, validation records, failure modes | [Generic character reconstruction method](../analytical-methods/GENERIC_CHARACTER_RECONSTRUCTION_METHOD.md), or the project's own adapted reconstruction method |
| Monograph qualification, coverage, self-containment and fidelity acceptance | [Initiation policy Section 5.5.1](MANGA_ANIME_PROJECT_INITIATION_AND_ARCHITECTURE_POLICY.md#self-contained-character-monograph-standard) |
| Independent participation in substantive source readings | [Topology policy Section 4.1](MANGA_ANIME_EXECUTION_TOPOLOGY_AND_CAPABILITY_ROUTING_POLICY.md#multi-agent-source-reading) |
| Run authorization, atomic units, high-water marks, prospective discipline, recovery | [Continuation policy](MANGA_ANIME_SEQUENTIAL_EXECUTION_SCOPE_AND_CONTINUATION_POLICY.md) |
| Locks, run stops, terminal closures, material restarts | [Initiation policy Sections 3.8-3.9](MANGA_ANIME_PROJECT_INITIATION_AND_ARCHITECTURE_POLICY.md) |
| Inspection lanes and lane claim permissions | [Medium and inspection-lane routing policy](MANGA_ANIME_MEDIUM_AND_INSPECTION_LANE_ROUTING_POLICY.md) and the [audiovisual reconciliation protocol](MANGA_ANIME_AUDIOVISUAL_RECONCILIATION_PROTOCOL.md) |
| Reasoning classes and execution records | [Reasoning and model-routing policy](MANGA_ANIME_REASONING_AND_MODEL_ROUTING_POLICY.md) Sections 12-15 |
| Transfers, semantic acceptance, named-subject check | [Handoff contract](MANGA_ANIME_ANALYTICAL_HANDOFF_AND_INTEGRATION_CONTRACT.md) Sections 2-15 and its [stage handoff template](templates/MANGA_ANIME_ANALYTICAL_STAGE_HANDOFF_TEMPLATE.md) |
| Deepening passes and convergence in long projects | [Long-series protocol](MANGA_ANIME_LONG_SERIES_HYBRID_EXECUTION_PROTOCOL.md) Sections 6-13 |
| Authority states, transitions, supersession and frozen artifacts | [Archive authority policy](ARCHIVE_AUTHORITY_AND_SUPERSESSION_POLICY.md), [`characters/README.md`](../../characters/README.md#artifact-authority) and routing Sections 4 and 8.2 |
| Corrections and procedural conflicts | [Checklist correction procedure](../policies/CHANGE_INTEGRATION_CHECKLIST.md#analytical-corrections-and-procedural-conflicts) |
| Discovery enrollment and broken-reference repair | [Discovery policy](../policies/CHARACTER_DISCOVERY_MAINTENANCE.md) |
| Capability grades and owner calibration rulings | [Reconstruction maintenance policy](../policies/CHARACTER_RECONSTRUCTION_MAINTENANCE.md) and [`characters/RECONSTRUCTION_CAPABILITY_SPEC.md`](../../characters/RECONSTRUCTION_CAPABILITY_SPEC.md) |

Where a project's established method or architecture is more specific or more demanding, it governs; this protocol applies where it is silent. A local rule cannot lower the independence, evidence, reconciliation or authority requirements below.

### 1.3 What a pass never does

A pass, in any mode, never:

- admits a source, source class, adaptation, language witness or live-service release beyond the project's admitted boundary, or treats an available source as admitted;
- changes the analytical content of, retypes or replaces a frozen reading, prospective freeze, checkpoint, seal, historical monograph or artifact of a frozen release, or edits in any way an artifact declared byte-immutable, hash-locked or archival-locked, or a `NONE_FROZEN` object (Section 9.5). The only exception is MACRP-F replacing an admitted reading through the owner-authorized release route of initiation Section 3.8;
- self-assigns, predicts or edits a global capability tier or dimension grade, or presents a local readiness label as one;
- writes the discovery partitions, the capability partitions or any generated global index. A discovery repair on the run's branch is the discovery agent's commit, not the pass's (Section 13.1);
- writes the `sequential_execution` or `project_initialization` state fields for an R or T run (Section 12.2);
- creates a second current portrait, model or entrypoint for a subject that already has one;
- treats generated output, consensus among agents, agent count, document length or observation count as evidence or as a measure of quality.

## 2. Eligibility and maturity assessment

### 2.1 Baseline freeze

Freeze the baseline first. Choose one full commit SHA on `main` containing the project's integrated state, and record it as `baseline_commit` with the paths of the baseline artifacts. Unintegrated work on the project branch is not part of the baseline; wait for its integration, or record it separately as an unintegrated delta that carries no authority. The baseline is never edited to make later work look consistent. When execution begins after a configure-only instruction, compare current `main` with the baseline. If a target artifact changed, refreeze and record the drift (handoff Section 10).

### 2.2 Eligibility

Assess eligibility at the baseline commit and record it in the run record. A project is eligible when all of these hold:

1. its registry row has `canonical_entrypoint_status: PRESENT_VERIFIED`, and the entrypoint has been read in full (routing Section 6);
2. its governing method and synthesis architecture are current-eligible, or the root keeps its legacy mature route (initiation Section 3.9.2). MACRP-F needs a current-eligible method for its generation (Section 4.3);
3. its admitted source boundary is recorded and recoverable;
4. each target subject already has substantial analysis in canonical homes (a monograph, model, ledger or substantial distributed analysis) or, for MACRP-F, a completed or substantially advanced earlier generation exists to serve as the frozen comparison baseline;
5. no target artifact has `UNRESOLVED` authority, and the freeze, release or lock state of each target is recorded, distinguishing a declared byte lock from a hash merely recorded by an audit or manifest (Section 9.5), so that the run plans successors where edits are prohibited;
6. no other active mutable owner holds a target artifact, unless one accountable integrator coordinates both (topology Section 9). MACRP-F never runs concurrently with another sequential run on the same root;
7. the execution environment provides genuinely independent contexts and the inspection lanes the declared workstreams need (Sections 5.4 and 6.1).

Record one outcome: `ELIGIBLE`, `ELIGIBLE_WITH_LIMITS` (scope narrowed, with the reason) or `NOT_ELIGIBLE`, naming the route that applies instead (project initiation, sequential continuation, ordinary monograph production, or an owner request for source admission). Resolve each target subject to its discovery `analysis_subject_id` when a discovery row exists, and otherwise to the project's own stable identity. Never invent a discovery identity.

### 2.3 Baseline assessment

The assessment records, with paths and locators:

- **analytical maturity**: completed source coverage, current generation and the state of the character layer;
- **source boundary and availability**: the admitted boundary, the inventory actually reachable now and its route, editions, languages and continuities;
- **current canonical character artifacts**: monographs, operational models, state, relationship, voice and ordinary-life records for each target subject, with their authority states and frozen-release, byte-lock or recorded-hash state (Section 9.5), plus the project's qualification record (initiation Section 5.5.1), including unassessed or `QUALIFIED_PENDING` characters;
- **validation and review history**: earlier probes, audits and predictions with their recorded exposure (Section 10.3), attached to the rule and model version they tested;
- **known deficiencies**, as the project records them and as the assessment finds them;
- **continuity and chronology constraints**: state boundaries, routes, incarnations, narrators and knowledge boundaries;
- **execution capability**: the independent contexts and verified inspection lanes (topology Section 5 profile);
- **current-state consistency**: disagreements among the entrypoint, local routers, model headers, ledger coverage blocks and registry notes. Each disagreement is an integration finding to resolve through the ordinary routes within the run's scope, never a reason to trust either side unchecked.

### 2.4 Limitation diagnosis

The assessment classifies each material deficiency by its principal cause. The diagnosis determines the work; do not prescribe a rereading when reconciliation or targeted inspection is sufficient.

| Principal limitation | Typical indication | Work it calls for |
|---|---|---|
| Missing primary-source evidence | The deciding behavior lies outside the admitted boundary | No MACRP work. Record the gap. Admission is a separate owner decision under the continuation policy |
| Evidence present but not extracted | The sources were read, but the dimension was not captured | MACRP-T on diagnostic units; MACRP-F only when the omission is pervasive |
| Extracted but not integrated | Ledgers or readings hold it; the monograph or model ignores it | MACRP-R |
| Insufficiently specific mechanisms | Trait adjectives; rules without triggers, counterconditions, exceptions or priority arbitration | MACRP-R; MACRP-T where the discriminating evidence was never captured |
| Inadequate source verification | Missing or suspect locators, or claims resting on summaries or translation | MACRP-R decisive-passage verification, or MACRP-T |
| Missing operational artifacts | No model, state record, voice profile or abstention boundary exists | MACRP-R, built from existing evidence |
| Not enrolled for discovery or evaluation | Analysis exists but no discovery row cites it | A lead (Section 14); this alone does not justify a pass |
| Evidence gap the admitted source cannot close | The source never gives the character the opportunity | Record an evidence gap (generic method Section 8); further analysis cannot resolve it |
| Evidence-backed limitation | The source gives the opportunity and shows the character does not, cannot or would not | Record it as an evidence-backed limitation; it is evidence, not a deficiency |

## 3. Authorization and scope

### 3.1 Owner instruction

A run requires a current owner instruction that names the project, the mode and the target subjects, or a rule for selecting them. A run may apply different modes to different subjects when the instruction covers each. In addition:

- **MACRP-R** needs nothing more. Its source access is limited to inspection inside the admitted boundary for verification and a proportionate counterexample search (Section 6.2). Inspection that would fill a capture gap is MACRP-T work and needs escalation.
- **MACRP-T** names the deficiencies or workstreams to address. It may also name the diagnostic units or a selection rule and boundary. When it names neither, the boundary is the admitted boundary, and the principal selects units by a recorded rule that passes the reread test (Section 4.2).
- **MACRP-F** names the source boundary to reinspect and the comparison baseline generation, and is a run authorization under the continuation policy (mode, start and terminal boundary). It is subject to every gate in Section 4.3.

An instruction to *configure* a run authorizes only the baseline freeze, the eligibility and baseline assessments, the diagnosis and the proposed configuration in the run record. An instruction to *execute* covers execution within the recorded scope. Record the instruction's recoverable wording or reference in the run record. A `next` field, an `active` state or an agent's own proposal is never authorization.

### 3.2 Declared scope

Before execution, the run record declares: the subjects and states (`Character@Unit` boundaries) in scope with the mode for each, the source boundary, the workstreams (Section 5.2), the diagnostic units (MACRP-T), the write paths inside the project root, the artifacts the run holds as their mutable owner, the outputs (Section 9), the test strategy (Section 10), the run-specific acceptance criteria and the stop conditions. Requirements and inspection states use the handoff contract's Section 6 vocabulary. A `REQUIRED` item never silently becomes `OPTIONAL`.

### 3.3 Scope changes and escalation

The principal may narrow a scope, recording the reason. Broadening the subjects, workstreams or source units, or changing mode, needs a new owner instruction. Escalation runs from MACRP-R to MACRP-T or MACRP-F, and from MACRP-T to MACRP-F. When the gap assessment shows the current mode cannot meet a `REQUIRED` item, record the evidence and the proposed escalation, finish or bound the work that remains valid, and stop that item pending direction. A targeted pass is never silently converted into a full rereading. A pass may also complete without escalation and without changing any model; a reduced or unchanged assessment is a legitimate outcome.

## 4. Execution modes

### 4.1 MACRP-R: reconstruction reconciliation

Use when substantial character evidence and mature analytical artifacts already exist. The run inspects the existing monographs, ledgers, operational models, specialist syntheses and audits. It identifies integration problems and missing mechanisms, verifies decisive source passages, searches admitted source the baseline did not cite for counterexamples (Section 6.2), and improves the integration, specificity and transferability of the models. It names existing but unenrolled artifacts as discovery leads (Section 14). It requires no full source reread, admits nothing and creates no sequential readings. It is retrospective synthesis without admission (routing Section 6), so a CLOSED lock or a closure does not prevent it.

### 4.2 MACRP-T: targeted reconstruction reanalysis

Use when the gap assessment identifies deficiencies that require renewed inspection of admitted source units. The run sets out a source-grounded gap assessment and selects diagnostic units (Section 6.2). It assigns independent specialists to extract evidence on those deficiencies, searches deliberately for counterexamples and rival readings, reconciles findings with existing authority (Section 8) and improves the affected models and canonical artifacts.

MACRP-T is retrospective evidence work inside the admitted boundary, not a reread:

- its source-facing records carry a non-sequential `artifact_type`, either the project's established retrospective evidence type or `macrp_targeted_evidence_record`, and never sit in a sequential-reading directory;
- it does not replace, retype or restate a unit's general reading, and does not advance a high-water mark;
- a correction of a sealed or frozen reading enters as an erratum, claim revision or superseding synthesis (initiation Section 3.8);
- it is described as targeted coverage of named units for named deficiencies, never as comprehensive coverage.

**Reread test.** The work is a reread, whatever the number of named deficiencies, when the selection would inspect in full every unit, or most units, of the admitted boundary or of a contiguous arc, or when it produces a record per unit for a sequence of units. Then stop and seek MACRP-F authorization.

### 4.3 MACRP-F: full reconstruction-oriented rereading

Use only when the owner authorizes comprehensive reinspection of an established corpus. The run reinspects the entire authorized boundary, applies independent multi-agent analysis to every substantive unit, extracts character evidence at a finer resolution than the preceding generation, and preserves narrative, chronology, thematic and source context. It reconciles new findings against the frozen preceding generation and produces integrated reconstruction artifacts and independent reviews.

MACRP-F is a newly authorized reread or reanalysis generation (topology Section 4.1.1) and offers no shortcut around rereading controls:

- **Gate.** A new analytical generation is a material restart. It must opt into the prospective contract (`project_initiation_gate: REQUIRED` in the root's routing descriptor) and satisfy the whole initiation gate before its first reading: a current-eligible method and architecture for the generation, its multi-agent configuration (initiation Section 3.7), initialized day-one infrastructure and an OPEN lock. A project with a run stop reopens it only by owner authorization. One with a terminal closure needs separate owner authorization and a reviewed closure-control amendment.
- **Run.** The generation's run is declared under the continuation policy with its own mode, start, terminal boundary and high-water mark. The preceding generation's high-water mark and checkpoints are preserved as history and never moved backward.
- **Readings.** Every per-unit reading is a substantive sequential source reading under topology Section 4.1 and carries an `artifact_type` that the project-initiation gate classifies as sequential (initiation Section 3.9.2). Readings go to new paths. Replacing an admitted reading at its sealed path is possible only through the release route of initiation Section 3.8.
- **Entrypoint.** The generation stays in the same registered root with one canonical entrypoint (initiation Section 2). An entrypoint carries one set of sequential state, so the generation has its own entrypoint, and the root's routing descriptor reroutes the registered entrypoint to it. The preceding entrypoint remains the preceding generation's historical surface. It gains a pointer to its successor by an ordinary edit, or, if it belongs to a frozen release, as the administrative metadata routing Section 8.2 permits. Never two current entrypoints.
- **Prospective discipline.** The generation's method states whether, and how, its unit readings may use retrospective material (continuation Section 4.4). Rereading agents usually know the corpus. Where the method requires prospective capture, only an uncontaminated agent supplies it, as a separately attributable account frozen before exposure (topology Section 4.1.4). Exposure is recorded either way.
- **Unit and pass reconciliation.** Each unit transaction reconciles its findings against the preceding generation's reading of the same unit, using Section 8's dispositions, and records them in the unit's transaction record. Pass-level reconciliation runs at the generation's synthesis stage against its cumulative homes.

### 4.4 Mode selection

| Choose | When |
|---|---|
| MACRP-R | The principal limitations are integration, specificity, missing operational artifacts or verification, and the evidence is already captured in canonical homes |
| MACRP-T | Named deficiencies need renewed source inspection, and the evidence can be localized to diagnostic units that pass the reread test |
| MACRP-F | Deficiencies are pervasive across subjects and dimensions, or the preceding generation's capture method systematically omitted needed evidence (for example, it read a translation, ignored the source language or excluded an admitted channel), and the owner authorizes comprehensive reinspection |

Start from the least expensive mode the diagnosis supports.

## 5. Multi-agent configuration

### 5.1 Roles

| Role | Responsibility |
|---|---|
| Principal | Accountable analyst and integrator: baseline, eligibility, diagnosis, assignments, its own inspection, literary comprehension, continuity, the occurrence register (Section 7.1), reconciliation, integration into canonical homes and the completion record |
| Specialist | Independent, source-aware work on assigned workstreams, frozen before reconciliation |
| Reviewer A | Source fidelity, attribution, locators, epistemic labels and evidence integrity, checked against source passages inspected directly, including an independently drawn sample |
| Reviewer B | Owner of workstream 12: rival interpretations, counterexamples, omissions, overreach and caricature risk, including a search of uncited source |
| Probe designer | An independent context that writes and seals the probes; never a reviser of the models under test |
| Probe respondent | A fresh context that answers probes from exactly the recorded inputs |
| Probe judge | A context, other than the respondent and the model's author, that judges responses against the source and the sealed basis |

Repository publication remains a separate responsibility under the checklist. Only the principal, as integrator, writes shared ledgers, models, monographs or the entrypoint (topology Section 9). Participants other than the principal perform no repository operation. The principal commits each participant's findings unaltered, except for source-text sanitization (Section 6.6), as that participant's own finding record. Any participant that does write to Git performs the full repository acquisition and uses an approved identity.

### 5.2 Workstreams

These twelve analytical responsibilities are ownership units, not twelve agents. Every workstream that applies to the declared scope has a named owner in the run record; one that does not apply records why. They map onto existing coverage duties and evaluator dimensions and create no capability taxonomy.

| Workstream | Covers | Monograph coverage (5.5.1) | Evaluator dimension the evidence informs |
|---|---|---|---|
| 1 Psychology | Personality, motives, fears, desires, values, self-conception, defenses, contradictions, vulnerabilities | 3 | `PSYCHOLOGICAL_MODEL` |
| 2 Cognition | Attention, interpretation, inference, reasoning, epistemic errors, problem-solving, decisions, which competing priority wins | 4 | `PSYCHOLOGICAL_MODEL` |
| 3 Interiority | Represented thought, private narration, stated motive, concealment, self-deception, the thought-conduct gap; direct interior evidence kept apart from inference | 3, 6 | `INTERIORITY` |
| 4 Behavioral microanalysis | Initiative, gesture, facial reaction, hesitation, avoidance, habits, minor-event responses, repeated mistakes and corrections, within the medium's affordances | 5 | `CONFLICT_BEHAVIOR`, `MUNDANE_BEHAVIOR` |
| 5 Ordinary life | Food, drink, clothing, shopping, leisure, hobbies, routines, domestic arrangements, spending, preferences, aversions, practical habits (Section 6.3) | 8 | `MUNDANE_BEHAVIOR` |
| 6 Linguistic behavior | Source-language register, pronouns, address, vocabulary, syntax, rhetoric, silence, turn-taking, recipient-conditioned variation (Section 6.4) | 6 | `VOICE_REGISTER` |
| 7 Humor and play | Joke initiation and reception, teasing, irony, self-deprecation, embarrassment, playful competition, repair, social enjoyment | 5, 6 | `HUMOR_PLAY` |
| 8 Relationship conditioning | Trust, familiarity, attachment, rivalry, obligation, intimacy, disclosure, dependency, boundaries, directed differences toward particular people | 7, 9 | `RELATIONSHIP_CONDITIONING` |
| 9 Ethics and conflict | Moral commitments, practical judgment, conflicting obligations, refusal, intervention, pressure, overreach, accountability, responses to correction; harmful conduct recorded as faithfully as beneficial | 3, 4, 5 | `ETHICAL_DELIBERATION`, `CONFLICT_BEHAVIOR` |
| 10 Competence and agency | Skills, professional conduct, initiative, technical knowledge, institutional roles, limits, the difference between capacity and willingness | 10 | Scenario readiness `PROFESSIONAL_CONTEXT` |
| 11 Longitudinal development | Changes in dispositions, motives, habits, knowledge, relationships, skills and self-understanding, separated from late disclosure of an existing trait | 2, 11 | `LONGITUDINAL_STATE`, `TEMPORAL_SPECIFICITY` |
| 12 Adversarial evidence | Counterexamples, rival explanations, inconsistency, misleading focalization, negative constraints, unsupported generalization, genuine gaps | 13 | `NEGATIVE_EVIDENCE` for evidence-backed limitations only; gaps inform `SOURCE_COMPLETENESS` |

Monograph items 1, 12 and 14 and the operational model draw on every workstream. Every specialist reports adverse evidence in its own workstreams; Reviewer B owns workstream 12 as a whole. Projects may merge or subdivide workstreams by scale, medium and evidence density, and the recorded ownership must stay identifiable.

### 5.3 Configurations

Scale the configuration to the work, and impose no fixed agent count. A role is a responsibility; one participant may hold several only where the independence rules allow. Specialists may divide work by subject or source tranche as well as by workstream, so that no context must hold more than it can inspect.

| Configuration | Suitable for | Shape |
|---|---|---|
| Dense | A long, analytically dense corpus or many central subjects | Principal; specialists A (workstreams 1-3), B (4-5), C (6-7), D (8), E (9-10) and F (11), split further by subject or tranche as needed; Reviewers A and B; probe designer, respondents and judges |
| Standard | A typical MACRP-R or MACRP-T run | Principal; two or three specialists grouping the applicable workstreams; Reviewer A; Reviewer B, who may share one independent context with Reviewer A when the reason is recorded; probe designer, respondents and judges |
| Bounded | A MACRP-R run on one subject and a few workstreams | Principal; one independent context that both contributes and reviews, with the reason recorded; separate probe contexts |

For source-facing work the topology governs the configuration, and the shapes above describe how a pass distributes workstreams across it:

- MACRP-T applies topology Section 4.1.2's default configuration to each diagnostic batch. The reduced configuration is available only for a batch that meets that section's conditions for an unusually bounded unit;
- MACRP-F applies topology Section 4.1 to every unit. The Dense or Standard shape assigns workstreams to the specialists who serve the units in turn; it does not multiply contexts per unit beyond what the unit's evidence requires;
- no run completes on one agent's unreviewed work.

### 5.4 Independence

Topology Sections 4.1.3-4.1.5 define genuine independence, knowledge boundaries and durable contributions, and govern here. A pass adds the following.

- **Controlled exposure.** A specialist, reviewer or probe respondent whose assignment depends on limited exposure receives an assignment packet: the authorized source or its retrieval route, the necessary source and chronology metadata, the governing method constraints, the source-handling limits (Section 6.6; no transmission of source material beyond the authorized route, topology Section 4.1.7), its assigned workstreams and the output and locator conventions. It is instructed not to retrieve other repository or project content. It is not performing a repository operation; the principal, who writes to Git, performs the routing Section 6 acquisition. Where a runtime loads repository instructions automatically, the receipt records what was loaded and what it exposed. Where practicable, initial observations precede exposure to the principal's draft or the preceding generation's conclusions. In MACRP-R the baseline artifacts are the input, so independence means forming an assessment of them, and of the source passages, without the principal's diagnosis or revisions. For a decisive passage, the participant inspects the source before reading the baseline's interpretation of it, and records that order.
- **Latent knowledge.** Models may already know a well-known work. Each receipt records whether the participant recognized the work or recalled events beyond its packet, and Section 10.3 records the same for probes.
- **Frozen findings.** Each participant's material findings are its own output. They are committed, sanitized only to remove source text beyond brief anchors (Section 6.6), in its own finding record or the unit's transaction record, before the principal reconciles them. A finding record is provenance and carries the `draft_noncurrent` quartet. A digest may supplement the committed record and never replaces it. Reconciliation cites findings by ID, and a later change to a finding is a new entry.
- **Reviewers inspect sources.** Reviewers A and B examine source passages directly, where practical before reading the candidate interpretation. Besides the passages the principal names as decisive, each draws its own sample. Approving prose is not review.
- **Receipts.** Every participant's receipt states its role, context separation, assignment packet, the material it actually inspected, what it saw of baseline, draft and probe material, its latent-knowledge statement and, only where observed, model and reasoning settings (reasoning policy Section 12). Never invent participation, model identity or runtime facts.
- **Unavailable capability.** Without genuine independent contexts or a required inspection lane, follow topology Section 4.1.7. One context playing several specialists satisfies nothing.

### 5.5 Reasoning and execution records

Each role resolves its reasoning class from its actual responsibility (reasoning policy Sections 13-15). Model building and adjudication start at `DEEP_SYNTHESIS`. Record one shared execution profile (topology Section 5) and a planned roster of roles and context types in the run record, and record per-stage observations only where observed. A stage that moves between environments, for example cloud monograph authoring or a continuous audiovisual relay, uses the handoff contract and its template.

## 6. Source inspection and evidence capture

### 6.1 Boundaries and lanes

Every participant works inside the admitted boundary and the run's declared scope. A live-service boundary is an exact locked inventory, never all current material (handoff Section 4). Each participant records its inspection lane per stage (inspection-lane policy Section 2) and claims only what that lane permits (Section 4 there). Account for inspection by boundary: a sample of clips is not `audio: COMPLETE`, and when no continuous viewing occurred, the record says zero rather than leaving the field out. Lane disputes follow the audiovisual reconciliation protocol.

### 6.2 Selection and counterexample search

MACRP-T selects diagnostic units by an explicit rule tied to the deficiency, for example the units in which a dimension is most often tested, a stratified sample across developmental states, units with ordinary-life scenes or rich dialogue, units flagged as contested, and units likely to contain counterexamples. Record the rule, the units chosen and rejected with reasons, and what the selection cannot show.

In every mode, part of the source inspected is drawn independently of the baseline's citations, so that the search can find counterexamples the baseline never cited. Reviewer B owns that search, and its scope is recorded. In MACRP-R the search is a proportionate sample aimed at the load-bearing rules, not a capture pass. Where an owner instruction limits an R run to artifact review, the run limits the search to cited passages and records that counterexample coverage is limited to them. Re-reading only the passages a model already cites tests locator fidelity, not the model.

### 6.3 Ordinary life and personal preference

Ordinary life is a first-class workstream (generic method Section 6). Sample it deliberately wherever the source shows it: food and drink, clothing and presentation, shopping and spending, hobbies, reading, music and entertainment, domestic routine, gift-giving and social ritual, work and study habits, practical skills, social initiative, unstructured time, ordinary disagreements, and responses to minor inconvenience, failure and embarrassment.

Each preference observation records the speaker and any persona or role in play, the audience, and whether the conduct was voluntary, accommodating or imposed. Each preference claim, built from those observations, carries one category:

| Category | Meaning |
|---|---|
| `EXPLICIT_PREFERENCE` | A sincere, direct expression of liking or disliking, not made in a performed persona or to accommodate someone |
| `REPEATED_VOLUNTARY_CHOICE` | The same voluntary choice across independent occurrences |
| `SITUATIONAL_CHOICE` | A local choice under particular circumstances |
| `ACCOMMODATION` | A choice or statement conditioned mainly by another person's needs |
| `IMPOSED_CONDUCT` | Conduct substantially constrained by duty, authority or resources |
| `UNKNOWN` | Insufficient evidence to infer a preference |

A stable preference needs an explicit preference that conduct does not contradict, or a repeated voluntary choice. One meal does not establish a favorite food, and one outfit does not establish an aesthetic. A paratext field, such as a game profile's favorite food, is recorded under its own source class and authority. Record absent evidence as `UNKNOWN` where the source gave no opportunity. Where it did, the absence is an evidence-backed limitation (generic method Section 8). Never invent a personal detail to complete a template.

### 6.4 Source language and communication

Where dialogue reconstruction is an objective and the source is available, voice analysis uses the primary language (generic method Section 7). For Japanese sources examine, as the evidence allows: first- and second-person reference; forms of address and honorifics; status distinctions; sentence-final forms; politeness and register; vocabulary and recurring rhetorical structures; questions, refusals, requests and evasions; interruption and turn-taking; humor and wordplay; teasing and repair; emotion-conditioned variation; narration versus spoken dialogue; and relationship-specific change over time. Other languages use the equivalent categories. Do not reduce a voice to catchphrases or a few sentence endings.

Deterministic textual analysis (counts, concordances, distributions) is useful for large machine-readable corpora. It runs in the working plane, deduplicates repeated text before counting (generic game method, counting and absence), interprets distributions in context, and commits only aggregate results and short anchors.

### 6.5 Performance, visual and game evidence

For audiovisual sources, examine performed voice, cadence, pauses, prosody, gesture, posture, facial expression and timing only where the assigned context can inspect them. Keep three voice layers separate: written or subtitled wording, measured acoustics and perceived delivery. Written dialogue is not performed voice, subtitles are not acoustic evidence, and sampled stills are not continuous motion. Manga supports a written register and drawn behavior, not timbre, and a rendering-register shift is framing, not event (generic manga method). Games declare the admitted source classes and scope each observation to its route, variant, manifestation or branch (generic game method, Parts IV and V). An alternate frame supplies only conditional characterization (generic method Section 4).

### 6.6 What enters Git

Use precise locators and the minimum lexical evidence a claim needs, within the project's quotation practice. Observation fields paraphrase; they quote only where a claim depends on exact wording. Ledgers must not accumulate a substantial share of a character's dialogue or of a unit's text. Never commit complete source passages, scripts, transcripts, subtitle files, media, extraction outputs or private source inventories (topology Section 8). Private raw transcripts and caches stay outside Git, so the committed record must carry the material findings itself.

## 7. Character observations and behavioral mechanisms

### 7.1 Observation record convention

This is a documented record convention, not a repository schema or a new database. A project records observations in its established evidence ledger, model evidence section, MACRP-T record or MACRP-F unit record, in its own format (table rows, YAML blocks or project-local JSONL), provided these fields are recoverable where they apply:

| Field | Content |
|---|---|
| `observation_id` | Stable ID in the project's ID scheme |
| `occurrence_id` | The canonical occurrence ID from the run's occurrence register |
| `re_presentation_of` | For a flashback, recap, retelling, adaptation or shared text, the original occurrence |
| `subject` and `state` | The analysis subject and `Character@Unit` state |
| `locator` | Exact source locator in the project's grammar, plus edition or witness |
| `source_class` | The source's class and authority under the project's admission rules |
| `publication_position` and `internal_chronology` | Where the unit sits in publication order and in story time |
| `knowledge_state` | What the character knows at this point, and whether a relevant memory is accessible to the character |
| `analyst_exposure` | Whether the interpretation was formed with knowledge of later units (`PRE_REVEAL` or `POST_REVEAL`) |
| `focalizer`, `narrator`, `speaker` | Whose perspective, narration and speech carry the evidence |
| `addressee` and `audience` | Who is addressed and who else is present, with the relationship state of each |
| `situation` | The immediate situation and its constraints, ordinary or crisis, and who is in control in an altered state |
| `opportunity` | Whether the situation gave the character a real opportunity to show the behavior at issue |
| `conduct` | What the character does or says, paraphrased |
| `expressed_reason` | The reason the character gives, if any |
| `interior_evidence` | Directly represented thought or feeling, if any |
| `expression` | Verbal and nonverbal expression, with its inspection lane |
| `outcome` | The actual result and the feedback the character receives |
| `interpretation` | The behavioral reading, with its own epistemic status |
| `capacity_and_willingness` | Where competence is at issue, whether the evidence shows ability, choice or both |
| `alternatives` | Rival explanations |
| `related` | Counterexamples and related observation IDs |
| `transfer_supported` and `transfer_unsupported` | Conditions under which the observation transfers, and extrapolations it does not support, each with its own status |
| `preference_category` | Section 6.3, for preference evidence |
| `confidence` and `limitations` | Qualitative confidence (generic method Section 11) and evidentiary limits |
| `contributor` and `review` | The participant, its frozen-finding ID and the review disposition (Section 8) |

The generic method's evidence classes (`DS`, `DB`, `NI`, `RB`, `OS`, `PF`, `INF`) or the project's equivalents describe each observation's evidence route alongside these fields.

**Occurrences.** An occurrence is one depicted happening at one point of story time. The principal keeps the run's occurrence register and maps each specialist's local IDs, and each baseline citation of the same locator, to one canonical `occurrence_id` during reconciliation. A flashback, recap, retelling by another narrator, adaptation of the same event, or text shared across routes or reprints is a re-presentation of the original occurrence. It may add a channel, such as performance in an adaptation, but it is not independent support. Corroboration counts distinct occurrences, never observations, specialists, documents or re-presentations. Agreement among specialists about one occurrence is interpretive agreement, not independent source support.

### 7.2 Epistemic status

Status attaches to each proposition, not to a whole record. The conduct, utterance or represented thought, the interpretation and each transfer claim carry their own status. A project with an established evidence vocabulary keeps it and records the mapping.

| Status | Meaning |
|---|---|
| `DIRECT_OBSERVATION` | That the source presents something: an action, an utterance, or a thought represented as occurring |
| `SOURCE_ATTRIBUTED` | An explanation, motive or trait the source itself asserts. This includes a narrator's or focalizer's account of their own or another's motive, another character's reading, and a character's self-report. It is bounded by that viewpoint's reliability |
| `ANALYTICAL_INFERENCE` | An interpretation the analysis draws from several observations |
| `HYPOTHESIS` | A proposed explanation the evidence permits but does not establish |
| `UNRESOLVED` | Supported rival readings remain open |
| `UNSUPPORTED` | The proposition rests on premises the evidence does not supply |

"The text represents X as the character's thought" is a direct observation. "X is the operative motive" never is: it is source-attributed when the text asserts it, and an inference or hypothesis otherwise.

### 7.3 Conditional behavioral mechanisms

A pass prefers mechanisms to descriptive traits. Use the generic method's decision-rule form and statuses (Section 10 there: `OBSERVED`, `CANDIDATE_POLICY`, `PROMOTED_POLICY`). A mechanism records, where the evidence permits:

- triggering conditions;
- the relevant perception and appraisal;
- motivations and competing priorities, and **which priority wins under which conditions**, or that the evidence cannot tell. Being unable to tell which competing motive decides a choice is a limit to record, not something to fill;
- the likely behavior or family of alternatives;
- counterconditions, inhibitors and overrides;
- developmental applicability (`valid_from` and `valid_until`);
- recipient conditioning, directed toward particular people;
- characteristic errors and overreach;
- supporting and adverse evidence, by `occurrence_id`;
- the observation that would disconfirm it; and
- transfer limits, by distance (generic method Section 11).

Three levels illustrate the preference. *Insufficient*: a pair of trait adjectives. *Better*: a recurring behavior with its typical cost. *Preferred*: the conditions under which the character favors that behavior, the appraisals and competing priorities that select it, the later developmental states that constrain it, and the people toward whom it changes. Do not fabricate conditional precision to fill the preferred form. A mechanism compatible with every behavior predicts nothing.

**Promotion.** A rule reaches `PROMOTED_POLICY` only by surviving a sealed test on occurrences that were not used to derive or revise it, or a prospective test (Section 10.3). Occurrences can be held out for one rule even in a fully read work. The rule's own supporting occurrences never promote it, and a reviser-exposed probe never does. The latent-knowledge status is recorded and weighed. A project's established promotion standard governs its own statuses, and the pass records the exposure of whatever test promoted a rule. Rule status is not a tier criterion. A rule left at `CANDIDATE_POLICY` is not a regression; the comparison reports status changes with their reasons. Test results attach to rule IDs. A rule the pass preserves unchanged keeps its earlier results, labeled with the model version tested, and a changed rule does not.

**Cognitive-behavioral reconstruction.** Where the evidence permits, reconstruct how attention, interpretation and appraisal, emotional response, motivational activation, deliberation or habit, behavioral selection, communicative expression, external feedback and subsequent revision or resistance connect. This is an analytical model, not a sequence every character consciously runs. Mark each link the evidence does not support as unknown. Preserve whether the character deliberates explicitly, acts by habit or impulse, or acts with incomplete awareness.

### 7.4 State selection and continuity

Every model states the selectors that choose the right version of the character, from among: developmental period; knowledge and information state; memories and experienced events, with their accessibility; current role; relationship status; acute emotional or crisis state; agency or control state (possession, override, an alternate or fused self); audience; institutional environment; material resources; physical or supernatural capability; and continuity, route or adaptation incarnation. Selectors are categorical, evidence-grounded conditions, never numerical personality coefficients.

- Do not merge early, late and exceptional states into one composite personality. Do not generalize an exceptional or terminal transformation, and attribute behavior to whoever is in control in that state (owner calibration safeguards).
- Do not backproject later-acquired knowledge or development. Mark a late disclosure of an existing trait as `REVEALED_NOT_NEW` (generic method Section 10) only when the evidence shows the trait was already operative: earlier conduct consistent with it, or a source statement that dates it. Otherwise record development or `UNRESOLVED`.
- A temporal boundary limits which evidence a model may use; it never limits what the character knows. Memories revealed late belong to the character at every earlier state they predate. Whether the character can access them (suppressed, erased, dissociated or unattended) is itself a state to model.
- Keep publication chronology, internal chronology, narrator access, character knowledge and analyst exposure apart (initiation Section 5.9).
- Split a unit at a located state change inside it rather than labeling it with one state.

## 8. Reconciliation with existing analysis

### 8.1 Dispositions

After independent findings are frozen, the principal compares them with the frozen baseline and records one disposition per material finding. Where a finding changes a canonical claim, the principal also records the archive transition (`PRESERVE`, `STRENGTHEN`, `REVISE`, `DOWNGRADE`, `REJECT`, `OPEN`) in the project's claim-revision home. A project may keep its established vocabulary and record the mapping.

| Disposition | Meaning | Usual transition of an affected claim |
|---|---|---|
| `NEW_EVIDENCE` | Newly extracted source evidence from an occurrence the baseline did not cite, consistent with the claim | `STRENGTHEN`, or a new claim |
| `INDEPENDENT_CONFIRMATION` | A participant inspected the source occurrence directly and confirms the baseline reading of it | `PRESERVE` (the same occurrence, so not new support) |
| `INCREASED_SPECIFICITY` | Conditions, triggers, priorities or exceptions sharpened | `STRENGTHEN` or `REVISE` |
| `ADDED_CONTEXT` | Situational, chronological or relational context added | `PRESERVE` or `STRENGTHEN` |
| `MATERIAL_CORRECTION` | The baseline claim is shown wrong or overstated | `REVISE`, `DOWNGRADE` or `REJECT` |
| `NEW_COUNTEREXAMPLE` | Newly found evidence the claim does not cover or that contradicts it | `DOWNGRADE`, `REVISE` or `OPEN` |
| `RIVAL_INTERPRETATION` | A competing supported reading | `OPEN`, recording both |
| `UNRESOLVED_CONFLICT` | Findings conflict, and the evidence does not settle them | `OPEN` |
| `REJECTED_INFERENCE` | A candidate interpretation is not adopted | None; recorded with its reason |
| `PERSISTENT_LIMITATION` | A known limitation remains | `PRESERVE` the limit |

Re-extraction of an occurrence the baseline already cites is never `NEW_EVIDENCE`. It may confirm, refine (specificity or context), rival or correct the baseline reading, and its disposition says which. Agreement reached from the baseline artifacts alone, without inspecting the source, confirms nothing and receives no confirmation disposition.

### 8.2 Principles

- A new observation is not automatically a new interpretation, and a new interpretation is not automatically a valid correction.
- Consensus among agents does not substitute for source evidence. Resolve material disagreements by source inspection, attribution, chronology and explicit reasoning, and preserve genuinely unresolved alternatives.
- A correction shows an error, not a preference: locators, counterevidence, competing readings and remaining uncertainty (checklist correction procedure).
- Never rewrite frozen forecasts, checkpoints or historical portraits to make earlier analysis look correct. Use errata, claim revisions or successors that keep the original state recoverable (routing Section 4.2).

## 9. Integrated reconstruction-model production

### 9.1 Outputs and homes

Where the scope calls for them, a pass produces or improves: individual monographs; operational models; state and transition records; relationship-conditioned models; ordinary-life and preference evidence; source-language communication profiles; conditional decision rules; negative constraints and abstention boundaries; and source-indexed diagnostic examples. Each output goes to its existing canonical home, or to a successor of it when that home is frozen, byte-locked or `NONE_FROZEN` (Section 9.5). A new home is created only when the architecture's extension rule supports it (initiation Section 5.12), recorded in the architecture's revision history, never as a parallel authority for a subject that already has one.

### 9.2 Drafts before acceptance

Until the run's acceptance (Section 12.1), a new or revised monograph, model, ledger section or MACRP-T record that would become current is published only as a working draft under the `draft_noncurrent` quartet at its own working path (`characters/README.md`). It never edits a current artifact in place, and never supersedes one. In-place revisions, promotions to current status and supersession links land together in the acceptance tranche (Section 13.1). At acceptance, a draft either becomes the current successor at its own path, or its accepted content is applied to the current artifact in place and the draft is retired as `historical_legacy`. Discovery and the evaluator therefore never meet an unreviewed revision as current evidence.

### 9.3 Authority ceilings

Operational models and reconstruction profiles are derived use (generic method Section 1). A new substantive interpretation is first accepted in its canonical analytical home (ledger, claim register, reading erratum or monograph), and the model follows. A model never outranks or originates the literary analysis it derives from. A project that declares a different layering keeps it and records how the pass respects it.

### 9.4 Monographs

A new or generally revised monograph meets the self-contained standard and passes its separate self-containment and fidelity reviews (initiation Section 5.5.1) and the named-subject check (handoff Section 15.6). One subject at one boundary has one current portrait. A revision keeps the earlier-boundary portrait recoverable through the architecture's revision route. A monograph's operational profile does not claim that a separate model exists or has been validated. A pass records changed qualification outcomes in the project's qualification home. It neither discharges nor hides a monograph production obligation outside its scope.

### 9.5 Model versions

Follow the project's convention for revising models, subject to these limits:

- **Frozen release.** A target in a frozen, final or archival release is analytically immutable (routing Section 8.2). The pass issues a successor, and the predecessor receives only the administrative supersession metadata that section permits.
- **Byte lock.** A target explicitly declared byte-immutable, hash-locked or archival-locked, or a `NONE_FROZEN` object, receives no edit at all. Reciprocal supersession would change its bytes, so its successor stays `draft_noncurrent`. The run records the blocker and asks the owner for the route, for example a separate routing record the architecture adopts. It never leaves two current artifacts for one subject.
- **Recorded hash.** A hash that an audit or manifest merely records is not a lock. The audit remains the record of the bytes it examined, and the manifest is refreshed by its owning process.

Where the project has no convention, issue a new version that supersedes the old one, with reciprocal authority links (generic method Section 13), rather than rewriting a model a capability assessment may cite. A revision that makes an assessment stale is never blocked by it; the evaluator reconciles. Every new or revised artifact carries the complete authority quartet.

## 10. Independent review and reconstruction testing

### 10.1 Fidelity and adversarial review

Before acceptance, Reviewer A checks that every source-facing record's units lie inside the admitted boundary and the declared selection. It audits the revised models and monographs rule by rule against source passages, including its own sample (generic method Section 17 statuses: `PASS`, `PASS_WITH_BOUND`, `NEEDS_TARGETED_SOURCE_REVIEW`, `INSUFFICIENT_EVIDENCE`). Reviewer B challenges them for rival readings, counterexamples found in uncited source, omitted evidence, state collapse, caricature, over-hedging and the generic method's failure modes. Both record their sampled scope; neither implies exhaustive verification.

### 10.2 Test battery

Testing diagnoses model quality. It is configurable, and it is never a prerequisite for, or a substitute for, a capability grade.

| Test | Design | Existing method it applies |
|---|---|---|
| A Canonical encounter | Give a respondent a bounded model and the opening conditions of a source encounter, withholding the subsequent behavior; a judge compares the predicted behavior families, priorities, reasoning, register and limits with the observed conduct | Generic method Sections 14-15 |
| B Controlled counterfactual | Paired scenarios differing in one consequential variable (interlocutor relationship, stakes, information, audience, developmental state, resources or authority). Prefer pairs grounded in attested contrasting occurrences. Otherwise the expected direction of change is justified from evidence independent of the model's own rules, so that a wrong rule cannot pass and a model without explicit rules is judged fairly | Generic method Section 16, perturbation |
| C Cross-character discrimination | Identical circumstances given to several models. Differences in attention, appraisal, motive, behavior, communication and error must be source-grounded. Convergence that the source supports is correct, and exaggerated difference is caricature | Generic method Section 16, baseline comparison, extended across characters |
| D Extended interaction | A sustained social or professional encounter with several decisions, new information and changing relations; check that the state selectors evolve consistently | This protocol's Section 7.4 |
| E Adversarial out-of-character | Attractive but misleading readings: a strategist who manipulates in every scene, intellect taken as complete self-knowledge, practicality taken as no personal taste, helpfulness taken as respect for autonomy, a self-description taken as a full account of motive. Check that source constraints and counterexamples resist the caricature | Generic method Section 16, decoys |
| F Monograph-only usability | A respondent receives only the monograph and answers questions about personality, ordinary behavior, relationships, speech constraints, development and limits; a source-aware judge checks the answers against the source. It complements, and never replaces, the 5.5.1 self-containment review | Initiation Section 5.5.1 monograph-only probe |
| G Calibration and abstention | Underspecified or unsupported scenarios, mixed with positive controls where the evidence does support a prediction. Check that the model names the missing variable, states its assumptions, separates strong predictions from weak analogies, keeps viable alternatives, abstains where evidence is inadequate, and does not abstain where it is adequate | Generic method Section 16, negative controls, and Section 11, distance |

**Controls.** Where feasible, Tests A, C and F include a control arm: a generic personality sketch of the same character, or no model at all, answered by a respondent under the same conditions. A model that does no better than its control shows insufficient individuation, or shows that the respondent is drawing on latent knowledge (Section 10.3).

**Default battery.** For each target subject whose model or monograph changed, run E, G and an individuation check: Test C, or the control arm of Test A. Add F for every new or generally revised monograph of a central subject, and at least one of A or B. Add D where extended interaction matters to the declared use. For a large cast, the full battery may run on a recorded, stratified sample of subjects, with E and G for every changed subject. Record each omission and its reason.

### 10.3 Exposure

Every probe records three exposure facts with its result.

**Outcome exposure** — one class:

| Class | Meaning |
|---|---|
| `SOURCE_KNOWN_RETROSPECTIVE` | The model's authors knew the outcome. This tests consistency and retrieval, not prediction |
| `MASKED` | The respondent did not see the outcome, but the model, or a derived artifact the respondent received (such as a monograph that digests the tested unit), was built with knowledge of it |
| `HELD_OUT` | The tested material was excluded from model construction, from every input the respondent received and from the model authors' exposure, by a recorded design |
| `PROSPECTIVE` | Predictions were frozen before anyone on the run had read the material |
| `NO_GROUND_TRUTH` | A novel hypothetical; there is no source outcome to match |

**Latent knowledge** — `EXCLUDED_BY_DESIGN`, `CANNOT_BE_EXCLUDED` or `RECOGNIZED`. For a widely known work, the default is `CANNOT_BE_EXCLUDED`. A respondent who recognizes the work, or recalls events beyond its inputs, is `RECOGNIZED`, and its `HELD_OUT` or `PROSPECTIVE` claim is qualified accordingly.

**Probe exposure** — `SEALED_FROM_REVISERS` or `REVISERS_EXPOSED`: whether anyone who revised the model saw the probe before the revised artifacts were frozen.

Never present a retrospective, masked or reviser-exposed result as prediction or improvement (generic method Section 15). Disclose accidental exposure; it downgrades the record.

### 10.4 Records, leakage and judging

- **Design and seal.** The probe designer writes each probe's definition: ID, test, subject and state, conditions, the varied variable, exposure classes, withheld material and the basis for judging. It seals the set before revision begins. It keeps the full set outside the revisers' view, and the run record holds only its digest until the revised artifacts are frozen; then the set is committed and checked against the digest. A set that the principal or another reviser has seen is `REVISERS_EXPOSED`.
- **Untargeted probes.** Each set includes probes drawn independently of the diagnostic units and of the deficiencies the revision addresses, to catch regressions. A Test A encounter taken from a unit the revision mined is source-known for the revised model.
- **No re-validation by the probe that drove a fix.** A defect fixed after testing is re-checked by a fresh, sealed probe. Rerunning the probe that exposed it records `REVISERS_EXPOSED` and shows nothing about improvement.
- **Respondents and judges.** A respondent answers from exactly its recorded inputs and states confidence and distance with each prediction. A judge other than the respondent and the model's author judges with source locators and the sealed basis. One respondent context may answer several probes under identical model and exposure conditions. Baseline and revised artifacts, and model-based and monograph-only conditions, use separate contexts.
- **Blinding.** When baseline and revised outputs are compared, present them in a normalized form (the same format and length bounds) under neutral labels, and judge by a rubric that disregards length.
- **Synthetic-output firewall.** Generated responses are labeled noncanonical, kept only as far as adjudication needs, and never cited as evidence about the character (generic method Section 1).
- **Scoring.** Source-outcome tests use the generic method's outcome vocabulary (Section 14 there). A response family so broad that it excludes nothing is scored as non-diagnostic, not as support. `NO_GROUND_TRUTH` scenarios are judged on evidentiary fidelity, internal consistency, individuation and justified transfer, and are never reported as `SUPPORTED` or `PASS`. Test G and every response with stated confidence also record calibration as `CALIBRATED`, `OVERCONFIDENT` or `UNDERCONFIDENT`. Over-abstention and blanket hedging are failures, just as unjustified certainty is: a useful model predicts mistakes and overreach (owner calibration rulings). State denominators and exclusions, and report no accuracy percentages (generic method Section 18). Plausible fan fiction is not validation.
- **Conditions.** Record observed model versions, the inputs given, all three exposure facts, and the reviewers' and judges' limitations.

## 11. Comparison against the pre-pass baseline

Every completed run compares its result with the frozen baseline, covering what applies: newly extracted observations; independently verified existing observations, counting only those confirmed by direct source inspection; materially refined interpretations; corrected claims; new counterexamples; additional ordinary-life and preference evidence; more differentiated linguistic behavior; newly supported conditional mechanisms and priority arbitration; improved relationship conditioning; better state and chronology separation; reduced reliance on generic personality assumptions, shown against the control arm; changed test results; new and persistent limitations; and evidence that an earlier interpretation was overconfident.

Where feasible, administer equivalent sealed probes to the baseline and the revised artifacts in separate fresh contexts, under the blinding rules of Section 10.4. Record every exposure so that reused probes are never later mistaken for fresh ones. Results attach to the rule and model version tested; a test of an earlier version does not describe a changed rule. Document length, agent count, observation count and the number of characters touched are not measures of quality. One decisive counterexample can outweigh hundreds of repetitive observations.

## 12. Acceptance and completion criteria

### 12.1 Acceptance

A run is semantically accepted when its records show:

1. a correctly authorized and bounded operation;
2. source and analytical coverage appropriate to the declared scope;
3. genuine independent participation, with receipts;
4. traceable, source-grounded findings;
5. explicit reconciliation against existing authority;
6. integrated and differentiated character models;
7. correct chronology, knowledge-state and control-state handling;
8. meaningful negative constraints and abstention boundaries;
9. an independent source-fidelity review;
10. proportionate reconstruction testing, with exposure recorded;
11. an explicit baseline comparison;
12. documented persistent uncertainty;
13. correct authority treatment and publication;
14. a resumable state record if the run is incomplete; and
15. discovery and evaluation leads where they apply;

plus the run-specific acceptance criteria declared in Section 3.2.

Acceptance applies handoff Section 11; topology Section 4.1.6 for every MACRP-F reading, and its criteria within the targeted scope for MACRP-T source-facing batches; initiation Section 5.5.1 for monographs; and handoff Section 15.6 for analytical prose. Mechanical validation is necessary where required and is never semantic acceptance. A receipt proves process, not literary correctness.

### 12.2 Completion and state

A run completes when its declared scope is accepted, or truthfully bounded with every remaining `REQUIRED` item recorded as a blocker. A targeted run may complete without addressing every character or dimension, provided its scope and limits are stated accurately. Success is never defined by grades: no number of characters moved to any tier, and no expected tier, is a completion criterion.

A configure-only run records `pass_state: blocked`, with the next action to await execution authorization. It writes nothing to the entrypoint and holds no artifacts until execution is authorized.

The run's state lives under its own key, `macrp_run.pass_state`, using the continuation policy's values (`active`, `completed`, `blocked`, `interrupted_pending_recovery`), with per-stage states in the handoff contract's vocabulary. An R or T run never writes `sequential_execution` or `project_initialization` fields; those fields describe source admission, and the validator reads them. A MACRP-F generation's run declaration is the real sequential state of that generation and uses those fields truthfully.

## 13. Publication and authority treatment

### 13.1 Branch, tranches and checks

A run publishes on the project's continuing `series/<stable-slug>` or `studies/<stable-slug>` branch and writes only its own root and routing descriptor (`BRANCH_LIFECYCLE.md`). It follows the checklist's author preflight and the [stable analytical publication sequence](../policies/CHANGE_INTEGRATION_CHECKLIST.md#stable-analytical-publication-sequence): one validation at a time, start from both current heads, push without force, and wait for the exact-head audit before the next tranche. The CI agent merges the PR.

Natural tranches are:

1. configuration and baseline;
2. frozen independent findings;
3. drafts of reconciled and revised artifacts, all `draft_noncurrent` (Section 9.2);
4. acceptance: review, testing, comparison, the in-place revisions, promotions and supersession links, the completion record with `pass_state: completed`, and the leads in that PR's description.

A MACRP-F run publishes per-unit transactions under the continuation policy instead of tranche 2, and closes with tranches 3 and 4 at its synthesis stage. When a supersession or revision breaks an existing character reference, the PR cannot merge until the discovery outputs are repaired in a separately identifiable commit on the same branch. That commit is the discovery agent's, or the CI agent's when the repair is purely mechanical (discovery policy, "Lag and broken references"). The pass's own commits never touch discovery or capability outputs. Record any owner hold, the PR number and the last audited head in the run record.

### 13.2 Records

- **Entrypoint.** When execution is authorized, the project's canonical entrypoint records the run under its own key or prose section: ID, modes, `pass_state`, the run record's path, the artifacts the run holds, and the next authorized action. Later writers, such as a sequential unit that would update a held artifact, coordinate through that record (topology Section 9). The run record is never a second entrypoint.
- **Run record.** One operational record per run, at a path inside the project root that the project names, preferably its existing audit, checkpoint or manifest home. It carries `artifact_type: macrp_run_record` and the `draft_noncurrent` quartet with `do_not_use_as_current_authority: true`, because it is operational provenance and never character evidence. It holds what has no existing home: authorization, baseline, eligibility, diagnosis, configuration and roster, assignment packets, receipts, the occurrence register, the reconciliation register, probe digests and, after release, probe definitions and results, the comparison, completion and leads. A responsibility the project already houses stays there, and the run record links to it. Sealed probes and material withheld from blind participants stay out of it until released.
- **Separation of record types.** Keep temporary execution records (working plane, outside Git), durable provenance (receipts and frozen findings), historical snapshots (frozen and never edited), canonical source-facing analysis, current monographs and derived-use models apart, each with its own authority state.

## 14. Discovery and capability-evaluation leads

The completion tranche's record, and the description of the PR that integrates it, name leads. Leads are unverified hints under the discovery and reconstruction policies. Those agents' Git-derived work queues find integrated changes regardless, and a lead adds no subject the evaluator's queue does not already contain.

- **Discovery leads**: new or revised canonical artifacts per subject, with their paths, stable anchors, the analytical dimensions they substantially support and their coverage boundary, plus existing substantial analysis the pass found unenrolled.
- **Evaluation leads**: subjects whose evidence changed, what changed per workstream and evaluator dimension, the tests run with their exposure facts, new evidence-backed limits and remaining evidence gaps, kept distinct.

A lead never states, proposes or implies a tier or a dimension grade. The A-E definitions, the owner calibration rulings and the evaluator's judgment are untouched. A legitimate outcome may support a stronger assessment, a narrower but more defensible scope, an unchanged assessment, lower confidence after adverse evidence, or a documented source limitation. Missing held-out validation, incomplete biography, absent performed voice or unresolved exceptional situations are limits for the evaluator to weigh under its specification, not barriers this protocol adds. Productive uncertainty about wording or affect differs from inability to tell which competing motive decides a choice; record which one the evidence shows.

## 15. Failure, interruption and resumption

- **Checkpoints.** After each stage, the run record states the stage, its handoff stage state, the commit holding its outputs and the next authorized action. Advance only after the stage's outputs are written and verified. A MACRP-F generation's unit progress lives in its high-water mark and unit transaction records.
- **Recovery first.** After an interruption, recover verified state from the run record, the branch and `main` before writing (continuation Section 7). Observed state outranks remembered state, and a polished draft never becomes canonical because a session ended.
- **Lost or contaminated contributions.** A specialist context lost before its findings were committed, or a frozen record that cannot be recovered, is rerun fresh with a new receipt, never reconstructed from memory or from a digest. A contaminated contribution is disclosed and loses independent or prospective credit for whatever the exposure touched.
- **Stops.** Stop the affected item on: missing or inaccessible required sources; a required lane or independent context that is unavailable; unresolved authority; a scope boundary the work would cross; a concurrent conflict on a held artifact; or a base drift that is semantically material (handoff Section 10). Continue independent authorized work that stays valid.
- **Partial completion.** Preserve valid work, record every unmet `REQUIRED` item with its blocker and next owner, and never report the run complete. An abandoned run records `pass_state: blocked` with its reason, keeps its accepted outputs and leaves its drafts noncurrent.

## 16. Artifact responsibilities

A run fulfills these logical responsibilities. Existing canonical artifacts fulfill them where the project already houses them; the run record holds the rest. No responsibility requires its own file.

| Responsibility | Usual home |
|---|---|
| 1 Run manifest and authorization | Run record |
| 2 Baseline and gap assessment | Run record |
| 3 Assignments and participation receipts | Run record, or each MACRP-F unit's transaction record |
| 4 Independent source-facing observations | Each participant's finding record, MACRP-T records, or MACRP-F unit records |
| 5 Character evidence and observation ledgers | The project's existing evidence ledgers |
| 6 Claim reconciliation and correction register | The project's claim-revision ledger; dispositions and the occurrence register in the run record |
| 7 Monographs and reconstruction models | Their existing canonical homes, or successors |
| 8 Probe definitions and outputs | Run record, after release, or the project's validation home |
| 9 Independent fidelity and reconstruction review | The project's audit home, or the run record |
| 10 Baseline comparison | Run record |
| 11 Completion, remaining gaps and leads | Run record, the entrypoint's run summary and the PR description |

## 17. Invoking a pass

An owner instruction names the mode, the project, the subjects or selection rule, the boundary and the comparison baseline, for example:

- *Configure and execute MACRP-F for* `<project>` *through* `<admitted boundary and supplements>`*, using* `<earlier generation>` *as the frozen comparison baseline.*
- *Execute MACRP-T for* `<subject>`*, concentrating on* `<deficiencies, such as mundane behavior, written voice, humor and independent practical competence>`*.*
- *Execute MACRP-R for* `<subjects>`*, integrating and independently reviewing their existing reconstruction models before deciding whether further source inspection is warranted.*

When an instruction omits a required element, the agent configures the run, records the gap and proposes the missing element, and does not execute beyond what the instruction covers.

## Changelog

### v1.0 - 2026-11-24 - Initial protocol

Establishes the owner-invoked MACRP operation:

- baseline freeze, eligibility and limitation diagnosis;
- owner authorization by mode, and the R, T and F modes with a reread test and the F gate route through the initiation policy;
- twelve workstreams mapped to the monograph standard and the evaluator dimensions;
- configurations that defer to topology Section 4.1, with controlled exposure and committed frozen findings;
- ordinary-life, source-language and medium rules;
- the observation, occurrence, epistemic-status and mechanism conventions;
- reconciliation dispositions mapped to the archive transitions;
- drafts that stay noncurrent until acceptance;
- the A-G test battery with controls, three exposure facts, sealed probes and two-sided calibration;
- baseline comparison, acceptance and completion, publication, leads and resumption.

It adds no schema, validator, workflow, registry or capability criterion.
