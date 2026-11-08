---
title: "Rent-a-Girlfriend - Series and Synthesis Architecture"
artifact_id: RAG_SERIES_ARCHITECTURE
artifact_type: synthesis_architecture
series: Rent-a-Girlfriend
generation: V1
version: "1.0"
status: canonical
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
do_not_use_as_literary_evidence: true
created: "2026-09-19"
canonical_home: "series/rent-a-girlfriend/00 Frameworks and Methods/RAG_SERIES_ARCHITECTURE.md"
design_reference_commit: "6d027e55f2eb38ec04ceed16bddc25015dc8a180"
adopted_at: "2026-09-19"
adopted_against_commit: "6d027e55f2eb38ec04ceed16bddc25015dc8a180"
source_boundary: "Architecture proposal for a sequential manga project; source inventory not yet verified."
recommended_reasoning_class: DEEP_SYNTHESIS
---

# Rent-a-Girlfriend: series and synthesis architecture

## 1. Identity, purpose, and current state

Create one continuing manga analytical project with one canonical entrypoint and a finite, verified source boundary. Its products are sequential deep readings, synchronized longitudinal evidence, substantial character/relationship synthesis, operational reconstruction models, and a corpus-bounded account of narrative progression and form.

The recommended new identity is:

```text
Repository: deep-blue-zero/anime-manga-ln-games-analysis
Stable branch: series/rent-a-girlfriend
Analytical root: series/rent-a-girlfriend/
Canonical entrypoint: series/rent-a-girlfriend/CURRENT_STATE_AND_CORPUS_MAP.md
Artifact prefix: RAG
Analytical generation: V1
Primary continuity: manga
```

No Rent-a-Girlfriend row was found in the main series registry inspected for this proposal. That is not proof that no unintegrated branch, alias, or older source exists. At adoption, recheck the live registry, relevant branches, and source routing. Preserve an existing reviewed stable identity if one is discovered; do not create a parallel root.

The main head observed at design closeout was `6d027e55f2eb38ec04ceed16bddc25015dc8a180`. The package is not a validated repository transaction, has not been committed, and has inspected no manga volumes. All supplied governing documents are noncurrent proposals until accepted and reconciled with live governance.

### Foundations

- `RAG_ANALYTICAL_METHOD.md` owns reading and evidence discipline.
- This document owns artifact responsibilities, paths, dependencies, and completion.
- `RAG_CHARACTER_RECONSTRUCTION_SPEC.md` owns model content, operational use, and local validation.

The analytical output `RAG_SERIES_ARCHITECTURE_AND_PROGRESSION.md` planned below is a different artifact: it will explain the **manga's causal narrative structure**, not govern the project's filesystem. Do not confuse the two because both contain the word architecture.

## 2. Branch and publication model

Use the single stable `series/rent-a-girlfriend` branch for continuing series work. Ten-volume blocks are analytical checkpoints, not ten different long-lived branches. Different sessions may contribute to this branch, but one active owner must control each shared mutable surface.

Before a commit, read the live `governance/policies/CHANGE_INTEGRATION_CHECKLIST.md`. Preserve exact-path staging, approved identities, current-base reconciliation, ordinary non-forced pushes, and final-head verification. Do not rewrite history or directly modify `main` under this architecture.

For a new root, author its local `.repository/series-registry.json` descriptor. On the stable branch, housekeeping owns the five global series/study routing outputs; the separate character curation agent owns `characters/registry.jsonl` and `CHARACTER_ANALYSIS_INDEX.md`. Do not manually update those files or introduce character-upsert inputs as part of ordinary series authorship.

Use the current owner-controlled integration process. The stable branch may be periodically integrated during a block once actual checks pass; analytic checkpoints do not require postponing all repository integration until V010. A green source preflight with pending routing is not integration readiness. Final integration requires the synchronized exact head and successful `Repository integration audit` status.

## 3. Source topology and authority

The acquired main manga is the prospective source. Lock witness identity, language, edition, chapter mapping, source route, file integrity where accessible, and coverage. The number of volumes remains unresolved until inventory inspection. Do not assume that "all published" means the same endpoint across Japanese and localized editions.

The Drive evidence root supplied by the owner is `1tNJvglC-ri_AEGTkJupZ78WddyiCqQMy`. An exact Rent-a-Girlfriend folder/file route has not been located in this task. Approved local sources are also permitted by live governance. Neither option authorizes uploading raw sources to Git.

The source map will distinguish available, verified, admitted, inspected, and completed material. Narrative extras receive their own placement decisions. Spin-offs, anime, author commentary, reception, and alternate-language comparisons remain separate optional scopes until admitted. Formal analysis of manga drawings is mandatory for a full manga reading; anime voice inspection is not.

## 4. Recommended target directory tree

The following is a planned architecture, **not a claim that these files already exist**. Initialize the foundation and justified day-one instruments first. Create readings, character artifacts, specialists, and audits only when there is actual work to contain.

```text
series/rent-a-girlfriend/
|-- CURRENT_STATE_AND_CORPUS_MAP.md
|-- README.md                         # Optional pointer only; no duplicated current state.
|-- .repository/
|   `-- series-registry.json
|
|-- 00 Frameworks and Methods/
|   |-- RAG_ANALYTICAL_METHOD.md
|   |-- RAG_SERIES_ARCHITECTURE.md
|   |-- RAG_CHARACTER_RECONSTRUCTION_SPEC.md
|   `-- RAG_SOURCE_AND_SCOPE_MAP.md
|
|-- 01 Sequential Readings/
|   |-- Volumes 001-010/
|   |   |-- RAG_V001_DEEP_READING.md
|   |   `-- ... RAG_V010_DEEP_READING.md
|   |-- Volumes 011-020/
|   |-- Volumes 021-030/
|   |-- Volumes 031-040/
|   `-- Volumes 041-050/               # Extend in fixed ten-volume slots as needed.
|
|-- 02 Block Syntheses/
|   |-- RAG_CP_V010.md
|   |-- RAG_CP_V020.md
|   `-- ...                           # Exact endpoint for any partial final checkpoint.
|
|-- 03 Ledgers/
|   |-- RAG_CHRONOLOGY_LEDGER.md
|   |-- RAG_RELATIONSHIP_STATE_LEDGER.md
|   |-- RAG_INFORMATION_AND_DECEPTION_LEDGER.md
|   |-- RAG_AGENCY_AND_INITIATIVE_LEDGER.md
|   |-- RAG_TRANSACTION_AND_INTIMACY_LEDGER.md
|   |-- RAG_PROGRESS_AND_REGRESSION_LEDGER.md
|   |-- RAG_REPETITION_AND_VISUAL_FORM_LEDGER.md
|   |-- RAG_CLAIMS_PREDICTIONS_AND_REVISIONS_LEDGER.md
|   `-- RAG_CAST_AND_RECONSTRUCTION_READINESS.md
|
|-- 04 Character Analysis/
|   |-- Kazuya Kinoshita/
|   |   |-- RAG_KAZUYA_EVIDENCE_LEDGER.md
|   |   |-- RAG_KAZUYA_RECONSTRUCTION_MODEL.md
|   |   `-- RAG_KAZUYA_CHARACTER_MONOGRAPH.md
|   |-- Chizuru Ichinose/
|   |   |-- RAG_CHIZURU_EVIDENCE_LEDGER.md
|   |   |-- RAG_CHIZURU_RECONSTRUCTION_MODEL.md
|   |   `-- RAG_CHIZURU_CHARACTER_MONOGRAPH.md
|   `-- [Other evidence-supported character homes]
|
|-- 05 Relationship Analysis/
|   |-- RAG_KAZUYA_CHIZURU_RELATIONSHIP_ARCHITECTURE.md
|   `-- [Other substantive dyadic or ensemble analyses]
|
|-- 06 Specialist Synthesis/
|   |-- RAG_SERIES_ARCHITECTURE_AND_PROGRESSION.md
|   |-- RAG_ROMANTIC_PROGRESS_AND_STASIS.md
|   |-- RAG_TRANSACTION_PERFORMANCE_AND_AUTHENTICITY.md
|   |-- RAG_DECEPTION_SOCIAL_PERFORMANCE_AND_FACE.md
|   |-- RAG_DESIRE_GAZE_AND_VISUAL_COMEDY.md
|   |-- RAG_REPETITION_SERIALITY_AND_TEMPORAL_FORM.md
|   `-- RAG_CONTINUOUS_SERIES_SYNTHESIS.md
|
`-- 07 Audits and Handoffs/
    |-- RAG_CODEX_CHATGPT_STARTUP_HANDOFF.md
    |-- RAG_BOOTSTRAP_RECEIPT.md
    |-- RAG_RECONSTRUCTION_AUDIT_V010.md
    |-- RAG_RECONSTRUCTION_AUDIT_V020.md
    `-- [Scoped transfer, contradiction, and completion audits as needed]
```

Use fixed three-digit volume labels consistently. A partial terminal tranche stays in its fixed storage slot; never create a moving `Volumes 041-Current` identity. Exact narrative arcs are discovered in the reading and can cross block boundaries. Do not pre-name a ten-volume block as an arc based on outside plot knowledge.

The startup handoff is an operational instruction/provenance artifact, not another series entrypoint. Its original content is retained; resumed work starts from the live current-state map, not a stale handoff.

## 5. Artifact responsibility and initialization matrix

The volume deep readings own primary analytical observation entries and evidence IDs. The following ledgers own longitudinal interpretation in their stated dimensions. Sharing an evidence reference does not duplicate authority; independently maintaining the same conclusion in two homes does.

| Dimension | Canonical cumulative home | Destination | Initialization |
|---|---|---|---|
| Witness identity and admitted scope | `RAG_SOURCE_AND_SCOPE_MAP.md` | All analysis and audit scope | Required before V001. |
| Event time, durations, calendar constraints | `RAG_CHRONOLOGY_LEDGER.md` | Progression and temporal-form specialists | Required instrument before V001. |
| Directed relationship conditions | `RAG_RELATIONSHIP_STATE_LEDGER.md` | Dyadic studies and character models | Required instrument before V001. |
| Knowledge, false belief, disclosure, lies | `RAG_INFORMATION_AND_DECEPTION_LEDGER.md` | Deception specialist and models | Required instrument before V001. |
| Choice, opportunity, initiative, refusal | `RAG_AGENCY_AND_INITIATIVE_LEDGER.md` | Character and relationship synthesis | Required instrument before V001. |
| Contract, payment, gift, care, boundary | `RAG_TRANSACTION_AND_INTIMACY_LEDGER.md` | Transaction/authenticity specialist | Required instrument before V001. |
| Domain-specific change and durability | `RAG_PROGRESS_AND_REGRESSION_LEDGER.md` | Progress/stasis specialist | Required instrument before V001. |
| Recurrence, page form, focalization, gaze | `RAG_REPETITION_AND_VISUAL_FORM_LEDGER.md` | Visual-comedy and seriality specialists | Required instrument before V001. |
| Claims, counterreadings, predictions, revisions | `RAG_CLAIMS_PREDICTIONS_AND_REVISIONS_LEDGER.md` | All current interpretations | Required before V001; initial questions are not findings. |
| Cast identity, artifact routes, local readiness | `RAG_CAST_AND_RECONSTRUCTION_READINESS.md` | Retrieval and scoped model audits | Required instrument before V001. |
| Individual developmental evidence | Each character's `EVIDENCE_LEDGER` | Model and monograph | Create with substantive character evidence. |
| Time-indexed operational rules | Each `RECONSTRUCTION_MODEL` | Monograph's reconstruction account and scenario work | Begin early when support exists. |
| Integrated character meaning | Each `CHARACTER_MONOGRAPH` | Relationship and series convergence | Evidence-based promotion; no fixed volume threshold. |

Every required day-one instrument must contain a responsibility statement, source boundary, record schema, update rule, evidence-routing rule, and an honest initial coverage state. Zero evidence rows before V001 are expected; invented observations or decorative placeholder claims are prohibited. These are justified prospective instruments, not a demand to instantiate every eventual artifact class.

The cast/readiness file is not a second character-state ledger and not a global registry. It routes identities and available analysis. Character-state history belongs in the person's evidence ledger; behavioral rules belong in the model.

## 6. Minimum ledger records

The tables below specify semantic content, not mandatory serialization. Markdown tables plus prose are adequate. Split an overlarge table into stable sections rather than sacrificing detail to fit one row.

### Chronology

Record ID, source evidence, event, temporal expression, anchor type, earliest/latest plausible placement when supportable, ordering constraints, uncertainty, contradictions, and revision links. Do not force precise dates from loose cues.

### Directed relationship state

Record ID, pair, direction, entering state, action or disclosure, public label, private acknowledgment, beliefs on each side, boundary changes, consequences, exiting state, and evidence. Shared factual status and each person's understanding must remain distinguishable.

### Information and deception

Proposition ID, what the source establishes, each relevant person's knowledge/belief, basis of that attribution, disclosure/withholding event, intended audience, maintenance cost, and unresolved alternatives. Track higher-order beliefs only where consequential; do not build an exhaustive combinatorial matrix.

### Agency and initiative

Decision ID, agent, opportunity, available alternatives, action/refusal/non-action, constraints, expected and actual cost, beneficiary, outcome, counterevidence, and source. A non-action requires evidence of an opportunity; absence from the scene is not a refusal.

### Transaction and intimacy

Event ID, parties, resource/service, stated agreement, compensation, voluntary versus obligatory elements, boundary/consent evidence, interpretation alternatives, and consequences. Unknown monetary amounts remain unknown. Do not impute a market price to emotional care.

### Progress and regression

Change ID, construct/domain, prior state, represented delta, who knows/acknowledges it, persistence observed through which boundary, later reversal or reconfiguration, and evidence. Character-model updates may cite the same change without keeping a second progress history.

### Repetition and visual form

Pattern ID, scene/formal mechanism, occurrences, prior/current state, invariant and altered elements, panel/page evidence, focalization, comic/romantic effects, alternative readings, and links to progress claims. The canonical formal pattern classification lives here; the progress ledger links to it.

### Claims, predictions, and revisions

Use separate sections within this file for current claims, competing hypotheses, frozen predictions, adjudications, revisions, and open evidence questions. Each material claim gets a stable ID, scope, evidence, counterevidence/gap, epistemic class, and current formulation. Revision entries preserve prior wording and use `PRESERVE`, `STRENGTHEN`, `REVISE`, `DOWNGRADE`, `REJECT`, or `OPEN`.

A generated counterfactual can test clarity but cannot count as confirming canon evidence. Formal narrative hypotheses and psychological hypotheses should not be silently merged into one claim.

## 7. Checkpoints and the ten-volume rhythm

The initial planned block sequence is V001-V010, V011-V020, V021-V030, V031-V040, then fixed ten-volume slots through the verified terminal inventory. Actual run authority is bounded separately.

Each `RAG_CP_VNNN.md` contains:

- exact completed/source boundary, witness coverage, frozen Git input state, and omissions;
- the new block's causal and formal contribution;
- the cumulative interpretation through VNNN, explicitly distinguished from the local block;
- character and directed-relationship transitions, including what persisted;
- chronology status and source conflicts;
- progress/repetition diagnosis with nonconfirming cases;
- revised claims and unresolved alternatives;
- model readiness and links to the separate local reconstruction audit;
- monograph/specialist readiness, architecture debt, and the next permitted operation.

A checkpoint is not ten volume abstracts concatenated. It must test the explanatory account developed so far. An apparent arc still in progress can be analyzed as incomplete; do not import its later resolution to finish a neat essay.

Freeze the checkpoint's exact scope. Later checkpoints are new bounded records, not replacements with the same scope. A partial terminal checkpoint names the actual terminal volume and identifies the unfinished storage block. If more sources are later admitted, create a new endpoint checkpoint and retain the earlier one.

## 8. Character and relationship products

Kazuya and Chizuru are the planned central reconstruction targets. Other characters receive independent homes when they have a recurring, evidence-supported analytical responsibility. Supporting figures with limited evidence remain bounded dossiers or routed observations; the number of volumes in the series does not confer evidence density on every person.

Models begin before monographs mature. A mature monograph must include the reconstruction account required by `RAG_CHARACTER_RECONSTRUCTION_SPEC.md`, tied to the detailed operational model. It must not be a biography followed by an adjective list.

Relationship specialists own the **interaction system**: reciprocal and asymmetric knowledge, complementary or conflicting incentives, recurring feedback, negotiated boundaries, shared history, and conditions that sustain or disrupt the relationship. They do not merely paste two character profiles together.

The Kazuya-Chizuru relationship is the initial planned central dyad. Other dyads or an ensemble account are promoted when they can support an independent argument. Family, friendships, professional relations, and rivals must not be excluded solely because they are not the main romance.

## 9. Specialist responsibilities and convergence

The following are required analytical responsibilities before a mature corpus-bounded continuous synthesis. Separate files are the planned default, not a mandate for empty documents. If evidence later justifies merging responsibilities, record an explicit architecture amendment and preserve a single home for every claim family.

| Specialist | Distinct question it owns |
|---|---|
| Series architecture and progression | How do the manga's causal systems and emergent phases change over time? |
| Romantic progress and stasis | What changes, what resets, and which kinds of transition are delayed? |
| Transaction, performance, and authenticity | How do paid/professional roles, chosen care, obligations, and personal feeling interact? |
| Deception, social performance, and face | How do information asymmetries and public/private accounts sustain the social system? |
| Desire, gaze, and visual comedy | How do framing, fantasy, embarrassment, idealization, and visual attention shape interpretation? |
| Repetition, seriality, and temporal form | How do repeated devices, chapter/page duration, and diegetic time create the reading's rhythms? |
| Continuous series synthesis | What integrated account survives reconciliation of all load-bearing specialist findings? |

A separate chronology essay, PACTRIH study, creator/paratext study, formal reception study, or adaptation comparison is **conditional**, not day-one mandatory. Add it only when the evidence and requested scope justify it. Do not infer author motives or audience consensus from narrative repetition alone.

The continuous synthesis must make a coherent argument; it is not a stack of specialist summaries. Its title and metadata must say "through VNNN" or otherwise name the actual corpus boundary. "Full series" is prohibited when it implies unread, unavailable, future, or out-of-scope content.

## 10. Dependency graph and execution owners

```text
Verified identity/source reconnaissance
    -> accepted method + architecture + reconstruction specification
    -> source map + day-one instruments + OPEN initiation gate
    -> each complete volume transaction
       -> diagnostic observations and synchronized longitudinal records
       -> bounded operational-model updates and prediction adjudication
    -> exact ten-volume / terminal checkpoint + local reconstruction audit
    -> frozen synthesis input snapshot + target-specific readiness
       -> substantive monographs and relationship/specialist drafts
    -> required source checks + contradiction and dependency reconciliation
       -> affected model/monograph/specialist revision where necessary
    -> corpus-bounded continuous synthesis
    -> semantic audit + applicable repository checks + authorized publication
```

This is not a rule that no useful synthesis occurs until the final volume. Checkpoint syntheses happen throughout. Monographs and specialists can mature against earlier bounded snapshots. Final convergence requires their boundaries and claims to be reconciled.

Preferred ownership follows the live hybrid protocol:

| Work | Preferred owner | Reasoning class |
|---|---|---|
| Foundation design | Fresh cloud synthesis session | `DEEP_SYNTHESIS`; escalate for propagation-sensitive architecture. |
| Source verification and local integration | Adequate owner-controlled Work/Codex environment | `BOUNDED_STANDARD` for inventory; higher for authority/interpretive decisions. |
| Volume readings and interpretive ledgers | Local Work/Codex with verified visual access | `SUBSTANTIVE_ANALYSIS`; escalate dense units. |
| Reconstruction rules and checkpoints | Adequate analytical owner | `DEEP_SYNTHESIS`. |
| Major monographs and specialists | Fresh cloud synthesis session, against a frozen snapshot | `DEEP_SYNTHESIS`; stronger review where justified. |
| Adversarial convergence and continuous synthesis | Named synthesis/review owner | `PREMIUM_QUALITY_FIRST` where broad and load-bearing. |
| Evidence completion and publication | Authorized local integrator | Capability-appropriate analysis plus required repository checks. |

These are workload classes, not promises about a particular product or account. Verify required transport, page inspection, persistence, and write capabilities. A tool that can extract images is not automatically a model that inspected them.

At a checkpoint, close and record the checkpoint before opening the next block. Heavy specialist work may be separately dispatched from that frozen state. Later sequential work must not leak into an earlier scoped draft. Parallelize distinct targets, not shared ledgers or the current entrypoint.

## 11. Completion and promotion gates

**Foundation gate:** stable root resolved; sources sufficiently reconnoitered; method, architecture, and reconstruction specification accepted; required instruments initialized; usable manga inspection route verified; current entrypoint accurately OPEN.

**Volume gate:** full declared narrative coverage, diagnostic evidence, deep reading, required ledger/model updates, adjudications, exiting freeze, current-state update, and authorized committed transaction verified. Unresolved mandatory coverage blocks completion of the affected volume.

**Block gate:** every volume transaction in scope closed; local/cumulative checkpoint written; local reconstruction audit completed; claims reconciled; next-block admission still withheld until closeout.

**Synthesis-readiness gate:** exact frozen inputs, target/source scope, substantial evidence coverage, source routes, unresolved obligations, and acceptance criteria supplied. A synopsis alone does not qualify.

**Monograph/model gate:** the reconstruction specification's substantive contracts are met at the claimed scope. Operational capability can remain conditional even when literary synthesis is mature.

**Continuous-synthesis gate:** required specialists and major character/relationship arguments are available at compatible boundaries; an architecture/role-gap review identifies and resolves material missing responsibilities; central contradictions are reconciled or explicitly bounded.

**Release gate:** semantic adequacy, source/locator checks, authority metadata, dependency consistency, repository validation, exact publication state, and remaining limitations are truthfully recorded. Source completion, accepted prose, local commit, branch push, and main integration remain separate facts.

## 12. Authority, mutability, and historical scope

Mutable current surfaces are the entrypoint, source map, cumulative ledgers, living models, and accepted rolling monographs/specialists. Update them by targeted edits to verified contents. Preserve identifiers, unaffected prose, and history.

Volume readings and checkpoints are frozen in their declared prospective scope. Their source observations remain usable; their early interpretations must be read with the revision trail. An old checkpoint is not the current endpoint, but a later differently scoped checkpoint does not automatically supersede it.

Use the live complete authority quartet. Noncurrent proposals use:

```yaml
status: draft_noncurrent
supersedes: []
superseded_by: []
do_not_use_as_current_authority: true
```

Accepted canonical artifacts use `status: canonical` with a false veto and appropriate valid supersession links, or `active_provisional` when current but explicitly provisional. Do not promote a draft just to make validation pass. A frozen file can be canonical for its historical evidence scope without claiming to contain the current whole-corpus interpretation.

When an actual replacement changes an artifact's identity/home, use reciprocal exact-path supersession and preserve necessary provenance. Ordinary in-place revisions use version history; they do not require a new file every time.

## 13. Current entrypoint and initialization example

The sole entrypoint records current scope, governing files, source location, completed high-water mark, active operation, next candidate, current checkpoint, reconstruction routes, material debt, and authorization boundary. A README, local cast index, or handoff must not maintain a competing copy of that state.

The following is an **illustrative bootstrap block**, not a claim that the gate is satisfied or a substitute for the current machine policy:

```yaml
project_initialization:
  status: canonical
  architecture_lifecycle: INITIAL
  governing_method: "00 Frameworks and Methods/RAG_ANALYTICAL_METHOD.md"
  synthesis_architecture: "00 Frameworks and Methods/RAG_SERIES_ARCHITECTURE.md"
  method_status: draft_noncurrent
  source_reconnaissance_complete: false
  required_ledgers_initialized: false
  sequential_analysis_lock: closed
project_run:
  execution_mode: single_operation
  admitted_through_volume: null
  completed_through_volume: null
  active_operation: BOOTSTRAP
  next_candidate: V001
  authorized_terminal_volume: null
  latest_checkpoint: null
```

The outer entrypoint's authority quartet describes the truthful current setup record; the nested `method_status` describes the separate method artifact. Do not leave it inconsistent after acceptance. The bootstrap may legitimately have a current-eligible entrypoint and a CLOSED gate. Before OPEN, resolve paths under the live validator's convention, promote genuinely accepted foundations, update all actual initialization facts, and ensure the prose `SEQUENTIAL_ANALYSIS_LOCK` agrees with the structured value.

Maintain factual read, drafted, analytically closed, committed, and published states without inventing a commit hash inside the commit being created. Record exact resulting commit IDs in an external/post-publication receipt or subsequently verified state record.

## 14. Handoff, scope control, and recovery

A synthesis transfer contains exact source/commit boundary, full target inputs or reliable routes, target artifact IDs/paths, evidence inspection status, current hypotheses and counterreadings, requested revisions, source debts, named integration owner, and file hashes when accessible. Do not transfer only a chat summary.

On return, compare base, candidate, and current target. Preserve newer ledger rows and later source progress. If source checks change a central premise, revise the affected argument and dependent specialists before semantic acceptance. A repository test pass cannot certify interpretive quality.

After interruption, recover the last verified transaction from Git and the entrypoint. Partial volume work is resumed at its documented internal position; it does not become complete because a previous session said "next." Do not redo closed volumes just to reestablish conversational familiarity.

The initial block is V001-V010 only when explicitly authorized. At its checkpoint, the next candidate is V011; that is not automatic authority to read it. Repeat the same bounded process for later owner-authorized blocks.

## 15. Architecture amendments and non-goals

Add a ledger or specialist only when a recurring dimension has independent evidence, downstream consequences, and no adequate current home. Amend the responsibility matrix and current entrypoint; backfill only material gaps that existing readings cannot responsibly supply. Do not restructure merely to resemble another series.

This package does not authorize acquiring more sources, creating extraction infrastructure, paid API calls, new automation, global registry writes, history rewriting, direct main edits, or unbounded future-volume processing. It does not claim a complete publication census or existing character models.

## 16. Governing sources

The decisions are grounded in this conversation and the supplied project source map, reconciled with these live repository surfaces inspected on 2026-09-19:

- `AGENTS.md` and `governance/CHATGPT_AUTHORITY_AND_ROUTING.md`;
- `governance/AUTHORITY_STATE.yaml` and `governance/AUTHORITY_SCOPE.json`;
- `governance/MANGA_ANIME_CORPUS_INDEX.md` and `series/registry.json`;
- `governance/policies/CHANGE_INTEGRATION_CHECKLIST.md`;
- `governance/policies/BRANCH_LIFECYCLE.md`;
- `governance/policies/AUTOMATED_GLOBAL_INDEX_MAINTENANCE.md`;
- the initiation, continuation, reasoning, capability-routing, long-series, and handoff policies under `governance/source-policies/`;
- `characters/README.md` and `characters/RECONSTRUCTION_CAPABILITY_SPEC.md`.

Repository reference: https://github.com/deep-blue-zero/anime-manga-ln-games-analysis/tree/6d027e55f2eb38ec04ceed16bddc25015dc8a180

The companion package guide identifies what was actually produced and what remains to be verified. Live governance outranks this proposal if the repository changes before adoption.
