---
title: Manga / Anime Project Initiation and Architecture Policy
artifact_id: MANGA_ANIME_PROJECT_INITIATION_AND_ARCHITECTURE_POLICY
artifact_type: project_initiation_architecture_policy
version: 1.8
status: canonical
generation: V1
scope: corpus-wide analytical project initiation and architecture governance
created: 2026-08-27
last_updated: 2026-10-20
maintainer: ChatGPT + user
source_boundary: "Corpus-wide governance for new and existing anime, manga, light-novel, novel, game, and related analytical projects"
supersedes: null
superseded_by: null
do_not_use_as_current_authority: false
do_not_use_as_literary_evidence: true
---

# Manga / Anime Project Initiation and Architecture Policy

## Governing rule

> **Before the first substantive sequential deep reading of a newly initiated analytical project, the project must establish both (1) a canonical analytical/deep-reading method and (2) a canonical synthesis/corpus architecture. A current-state/corpus-map entrypoint must identify both.**

This is a corpus-wide project-initiation gate. Its purpose is to prevent a recurring form of architectural debt: a project can successfully accumulate many volume, episode, chapter, route, or event readings while never defining how those readings will feed longitudinal ledgers, evidence infrastructure, specialist syntheses, character or relationship work, claim revision, and final integration. Discovering that gap near the end of a long source pass creates avoidable retrospective reconstruction work and can cause evidence that should have been tracked prospectively to be scattered across isolated readings.

The policy therefore requires a paired foundation before substantive sequential analysis begins:

1. **Analytical/deep-reading method** — governs how source units are read, what evidence is captured, what distinctions must be preserved, and how interpretation is disciplined.
2. **Synthesis/corpus architecture** — governs where accumulated knowledge goes, which longitudinal structures must exist, what specialist responsibilities are expected, how evidence and revisions route, and how the project eventually converges into mature synthesis.

The two responsibilities may live in two separate documents by default, but mature or unusually compact projects may combine them when both responsibilities remain explicit and independently recoverable. The policy standardizes semantic responsibilities, not an identical folder tree or document count.

---

# 1. Scope

This policy applies to newly initiated or materially restarted analytical projects involving, as applicable:

- manga;
- anime;
- light novels and prose novels;
- visual novels;
- games and live-service game narratives;
- mixed-media franchises;
- stage works, films, OVAs, ONAs, shorts, and specials;
- transcript/audio-driven character reconstruction projects;
- other source corpora incorporated into the Manga / Anime analytical archive.

It applies whether the eventual goal is full-series literary synthesis, character reconstruction, audiovisual analysis, ethics analysis, relationship modeling, music dramaturgy, institutional analysis, or another substantial interpretive program.

It does **not** require a full architecture for casual one-off discussion, ordinary question answering, source identification, preliminary scouting, or a narrowly bounded analysis that is not being opened as an ongoing corpus project.

---

# 2. Architecture precedence

Before creating or revising project infrastructure, use this precedence order:

1. existing canonical/frozen series architecture;
2. current `00_README_AND_CORPUS_MAP.md` or `CURRENT_STATE_AND_CORPUS_MAP.md`;
3. series-specific analytical method and synthesis architecture;
4. this corpus-wide policy;
5. the global analytical artifact naming/archive standard;
6. default project conventions only when no stronger rule exists.

A new chat, new reasoning model, new source tranche, or new analytical generation does **not** create a new corpus or justify parallel roots.

Mature architectures must be preserved unless a migration is explicitly undertaken. This policy is not permission to rename, renumber, relocate, or structurally normalize an established project merely for visual consistency.

---

# 3. Project Initiation Gate

A newly initiated substantive project should not begin its first sequential deep reading until the following gate conditions are satisfied.

## 3.1 Canonical project root resolved

Confirm that the work does not already have a canonical analytical root elsewhere.

Required actions:

- consult the corpus index (`governance/MANGA_ANIME_CORPUS_INDEX.md`) and the series and study registries (`series/registry.json`, `studies/registry.json`), and `MANGA_ANIME_DRIVE_INDEX.md` only for Drive-native or reference-only material;
- search for existing series roots, aliases, prior generations, and current-state files;
- identify the canonical analytical root;
- identify the source/ingestion root or source location where applicable;
- avoid creating a parallel root merely because the work is starting in a new chat.

## 3.2 Preliminary source reconnaissance complete

The project must know enough about the source object to design an appropriate method and architecture.

This does **not** require every source to be fully acquired or locked before architecture design. It requires sufficient understanding of questions such as:

- What is the primary narrative medium?
- What is the expected unit of sequential reading: episode, volume, chapter, route, event, commu, side story, film movement, etc.?
- What language(s) and editions are available?
- Are there adaptations or continuity branches?
- Is audiovisual performance analytically load-bearing?
- If continuous video may be needed, can an accessible derivative be supplied under the corpus video-escalation constraints?
- Are music, voice, staging, page composition, route state, event chronology, or supplemental prose likely to require dedicated treatment?
- Are side stories or later retrospectives likely to recontextualize earlier material?

Uncertainty is permitted. The architecture must be capable of evolving.

## 3.3 Governing analytical/deep-reading method established

A canonical method must exist before sequential analysis begins.

Typical filename:

`<SERIES>_ANALYTICAL_METHOD.md`

or a coherent existing project-specific equivalent.

The method should govern **how the source will be read**. Depending on medium and project purpose, it may define:

- source boundaries and edition/language precedence;
- prospective-reading or truth-freeze rules;
- textual, visual, audiovisual, musical, linguistic, or performance lenses;
- scene/chapter/episode segmentation;
- character-state and relationship-state observation;
- dialogue, translation, voice, and speech-register handling;
- fact/inference/speculation distinctions;
- narrator knowledge versus character knowledge;
- evidence notation and locators;
- prediction or hypothesis handling;
- contradiction handling within a sequential reading;
- what each sequential artifact must update before it can be considered complete.

For a new anime project with no existing analytical method, the [Generic Source-Bounded Anime Episode Analytical Method](../analytical-methods/GENERIC_ANIME_EPISODE_ANALYTICAL_METHOD.md) may be used as an optional bootstrap/design reference. It does not itself satisfy the project-local governing-method requirement. The project must adapt or author a series-specific method after source reconnaissance, include only analytically justified modules, pair it with a synthesis/corpus architecture, and expose both through the canonical project entrypoint before sequential analysis is unlocked.

## 3.4 Governing synthesis/corpus architecture established

A canonical architecture must exist before sequential analysis begins.

Typical filename:

`<SERIES>_SYNTHESIS_ARCHITECTURE.md`

or a coherent project-specific equivalent.

The architecture should govern **what analytical corpus the readings are building**. It must satisfy the Minimum Semantic Contract in Section 5.

## 3.5 Canonical entrypoint established

A project should have one clear first-read surface from initiation onward:

- `CURRENT_STATE_AND_CORPUS_MAP.md` while active; or
- another verified canonical equivalent when a mature architecture already exists.

At initialization, this file may be brief. It should identify:

- canonical project root;
- current source boundary;
- governing analytical method;
- governing synthesis architecture;
- initialization status;
- required day-one ledgers/infrastructure;
- next sequential operation;
- current reasoning-class routing where applicable.

Recommended machine-readable initialization block:

```yaml
project_initialization:
  status: canonical
  architecture_lifecycle: INITIAL
  governing_method: SERIES_ANALYTICAL_METHOD.md
  synthesis_architecture: SERIES_SYNTHESIS_ARCHITECTURE.md
  method_status: canonical
  source_reconnaissance_complete: true
  required_ledgers_initialized: true
  sequential_analysis_lock: open
```

The exact key names may vary in mature projects, but the state must be recoverable without reconstructing it from conversation history. Section 3.8 names the spellings the validator reads.

Keep the entrypoint about the present: current state, governing routes and the next permitted operation. When dated history accumulates, move it verbatim to a project changelog beside the entrypoint and link it, rather than deleting it. Do not record commit SHAs, workflow run IDs or publication status (such as `NOT_YET_PUBLISHED`) in entrypoint prose: Git history and the audit statuses own them, and prose copies go stale. Apply this at a project's next natural boundary, not as a corpus-wide sweep.

## 3.6 Required day-one longitudinal infrastructure initialized

Any ledger, evidence structure, or cumulative state tracker that the architecture identifies as necessary from the beginning should exist before the first source-unit deep reading.

Examples include, where justified:

- character-state ledger;
- relationship-state ledger;
- claim/revision ledger;
- prospective prediction register;
- institutional-state ledger;
- thematic evidence ledger;
- visual grammar ledger;
- musical dramaturgy ledger;
- voice/performance ledger;
- source-location index;
- route/continuity state ledger;
- character reconstruction readiness ledger.

This does not require creating empty infrastructure merely for symmetry. Only dimensions with a plausible recurring analytical responsibility should be initialized.

## 3.7 Reasoning class routing established

Major planned operation types should inherit or explicitly assign stable reasoning classes from `MANGA_ANIME_REASONING_AND_MODEL_ROUTING_POLICY.md` when doing so is useful.

Literal model names should not be hard-coded as durable architectural ontology when a stable reasoning class is sufficient.

### Execution ownership and synthesis dispatch

For substantial long-series work, the architecture should name preferred owners for framework/architecture design, sequential primary-source readings, synchronized ledgers, retrospective synthesis, required audiovisual completion, and repository integration. Apply the [long-series hybrid execution protocol](MANGA_ANIME_LONG_SERIES_HYBRID_EXECUTION_PROTOCOL.md) and [capability-routing policy](MANGA_ANIME_EXECUTION_TOPOLOGY_AND_CAPABILITY_ROUTING_POLICY.md); either environment may design architecture, with fresh cloud Pro preferred when adequately grounded.

Identify how a frozen evidence state will be handed to a fresh synthesis session and how returned work will be accepted. The [analytical handoff contract](MANGA_ANIME_ANALYTICAL_HANDOFF_AND_INTEGRATION_CONTRACT.md) governs the transfer. These execution descriptors do not satisfy the initiation gate by themselves, require new empty ledgers, or replace the current eligible method and synthesis/corpus architecture.

## 3.8 Sequential analysis lock

Once Sections 3.1-3.7 are satisfied, the corpus map may record:

`SEQUENTIAL_ANALYSIS_LOCK = OPEN`

Before that point:

`SEQUENTIAL_ANALYSIS_LOCK = CLOSED`

This is an operational gate, not a claim about source completeness. Preliminary source auditing and architecture work can proceed while the lock is closed.

When an authorized run completes, record completion and no next permitted/candidate source operation. The architecture lock may remain OPEN between runs; this does not authorize another source at handoff. The continuation policy owns owner authorization and recoverable run scope. A routine pause or completed run does not require a new closure record or a global amendment. When additional byte-sealed retention is needed, close the lock with one of the following records; existing seals remain mandatory:

- **Run stop.** At the end of a run that is not the project's final source boundary, the project records its own stop in `<project root>/.repository/run-closure.json` (schema `anime-manga-ln-games-analysis/project-run-closure/v1`, `state: CLOSED`) in the same commit that closes its lock. The record lives in the project's own root, so a series- or study-scoped task writes it on its stable branch and the nightly controller can integrate it. When the owner authorizes the next run, the project sets `state: REOPENED` and opens its lock: every sealed reading stays byte-checked against its seal while the run adds readings under the ordinary OPEN gate. When that run completes, the record returns to `CLOSED` with the new completion commit and the full set of readings. Do not delete the record to reopen. The validator compares the record with `main`'s record for the same registered root: every seal there must survive unchanged, in this record or in a terminal closure that replaces it, even if the root is moved or deregistered, unless `main`'s own `governance/repository-controls/project-initiation-gate.json` releases it through `run_closure_amendments`. A release names the SHA-256 of `main`'s current record, the reading, and the digest that record seals, with its authorization; it lapses as soon as `main`'s record changes, and a release added on the candidate branch itself does not count. Replacing a sealed reading therefore takes four steps: an owner-merged governance change records the release on `main`, the project leaves or reopens its run stop without that seal, it revises the reading under the OPEN lock and integrates it, and it seals the reading again when the run closes. The validator cannot tell who merged a release; housekeeping and the nightly controller refuse control paths, so it reaches `main` only through an owner-merged governance change. A closure covers every reading under its root, including readings of nested registered roots. The validator fails closed when `refs/remotes/origin/main` is unavailable; a checkout whose main remote has another name, or a mirror clone, creates that ref before validating. Adopting a run stop on a root that predates the gate classifies all its readings, including those in the activation baseline, so each must carry a structured `artifact_type` and be sealed. A project may instead keep its lock OPEN between runs while recording `run_state: completed` and no next candidate operation; its readings are then protected only by their freeze rules and Git history.
- **Terminal closure.** At the project's final source boundary, a reviewed `terminal_closures` record in `governance/repository-controls/project-initiation-gate.json` replaces the run stop; the change that adds it removes the run-closure record, and the validator rejects a project carrying both. Reopening a terminally closed project requires separate owner authorization and a reviewed closure-control amendment; source completion or unresolved analytical questions do not reopen the gate.

Both records carry `canonical_entrypoint`, `completion_commit`, `frozen_sequential_artifacts` (the exact paths and SHA-256 bytes of accepted sequential readings) and `supplemental_execution_required`, and preserve those readings behind the CLOSED lock without moving the activation baseline. The recorded `completion_commit` must resolve to a commit in the local Git validation context; every frozen seal must match a regular evidence blob in that historical tree. Missing history fails closed without fetching or substituting staged/current bytes. For a run stop, name a commit already on `main` that contains the sealed bytes, such as the integration commit of the run's last tranche. The validator rejects a completion commit that is not an ancestor of `refs/remotes/origin/main`: this limits sealed readings to ones already integrated on `main`, and keeps the commit reachable after a squash merge. These comparisons run on the source branch's audit against current `main`; protected `main` requires that audit on an up-to-date head, while the post-merge audit of `main` compares `main` with itself. Each record explicitly declares the boolean `supplemental_execution_required`; when true, the current entrypoint must retain a structured supplemental lane that is CLOSED with `other_narrative_admission: NOT_AUTHORIZED`. A present supplemental lane is checked even when not required. The validator still requires the current method, architecture and initialized infrastructure, and while a record is CLOSED rejects missing, altered or additional readings, an OPEN current lock, or resumed execution.

### Source admission, historical retention, and analytical revision

The lock and a closure record govern two of three distinct responsibilities:

- **Source admission** — whether another primary narrative unit may be admitted and analyzed. It requires owner authorization under the [sequential execution scope and continuation policy](MANGA_ANIME_SEQUENTIAL_EXECUTION_SCOPE_AND_CONTINUATION_POLICY.md) and, for a governed project, an OPEN lock. An OPEN lock is a precondition, never itself an authorization to admit a source.
- **Historical retention** — whether previously accepted readings remain preserved, identifiable, and valid within their historical authorization boundary. Frozen readings are not analytically rewritten; a run stop or a reviewed terminal closure byte-seals them, and a reopened run stop keeps those seals.
- **Analytical revision** — whether interpretations, ledgers, models, and syntheses derived from already admitted evidence may be corrected or superseded. Neither the lock nor a closure governs it. It follows the architecture's claim-revision behavior (Section 5.8), the archive authority policy, and the repository [correction procedure](../policies/CHANGE_INTEGRATION_CHECKLIST.md#analytical-corrections-and-procedural-conflicts).

A project can therefore be CLOSED to new admission, retain verified readings, and still correct its interpretations within the admitted corpus. Under a closure, a correction of a sealed reading is an erratum, claim revision, or superseding synthesis with a non-sequential `artifact_type`. It does not edit sealed bytes, carry a sequential type, or sit untyped in a sequential-reading directory; the validator treats each of those as alteration or admission. A complete replacement reading of an admitted unit cannot be machine-distinguished from a new unit, so it requires owner authorization and an amended seal in the governing closure record, like admission; for a run stop, the authorization is the release on `main` described above. The seal covers only artifacts the gate classifies as sequential readings; other frozen artifacts, such as differently typed paratext audits, remain protected by their project freeze rules and Git history.

A closure is one transaction: the entrypoint's CLOSED terminal state and its closure record land in the same commit. A series- or study-scoped task writes a run stop itself; a terminal closure lands only through an owner-merged governance change, so a task that reaches the final boundary first records a run stop and the blocker under the [correction and conflict procedure](../policies/CHANGE_INTEGRATION_CHECKLIST.md#analytical-corrections-and-procedural-conflicts). The validator reads terminal state from YAML front matter or the recognized fenced `project_initialization` block, the same surfaces it reads for the lock, and every statement of a field must agree: `project_initialization.next_permitted_operation` and `sequential_execution.next_candidate_operation` are `NONE` or an uppercase `NONE_` token; `sequential_execution.run_state` is `complete` or the continuation policy's `completed`; and a supplemental lane states `current_state` as `CLOSED` or an uppercase `CLOSED_` token, with `other_narrative_admission: NOT_AUTHORIZED`.

Use one spelling for each state field so the validator and later readers see the same state: `project_initialization.sequential_analysis_lock`, `project_initialization.next_permitted_operation`, `sequential_execution.run_state`, `sequential_execution.next_candidate_operation`, `supplemental_execution.current_state` and `supplemental_execution.other_narrative_admission`. Variant keys such as `next_sequential_operation`, `next_operation` or `next_sequential_operation_authorization` are not read; replace them at the project's next boundary. Keep the fields consistent with each other: a `completed` run names no next candidate operation, an `active` run requires an OPEN lock, and a CLOSED lock with a run-closure or terminal-closure record requires a completed run.

## 3.9 Repository enforcement

This section states how the repository validator applies Sections 3.1-3.8. The machine boundary is `../repository-controls/project-initiation-gate.json`; a new or materially restarted root declares `project_initiation_gate: REQUIRED` in its series/study routing descriptor and exposes a recoverable `project_initialization` state from its canonical entrypoint.

### 3.9.1 Architecture/bootstrap state

Architecture, source reconnaissance, source locking, corpus-map creation, method creation, synthesis-architecture creation, justified longitudinal-infrastructure initialization, and other pre-sequential setup may proceed while `SEQUENTIAL_ANALYSIS_LOCK = CLOSED`. CLOSED is the safe default. A project may remain incomplete in this state, and it must not create empty ledgers or placeholder artifact classes merely for symmetry. Creating directories, routing files, or an entrypoint does not by itself satisfy the initiation gate.

### 3.9.2 Sequential-analysis state

Before staging or committing the first substantive sequential deep reading for a governed project, verify all of the following:

- the governing analytical/deep-reading method exists as a tracked regular artifact and is current-eligible under repository authority rules;
- the governing synthesis/corpus architecture exists as a tracked regular artifact and is current-eligible under the same rules;
- the canonical current-state/corpus-map entrypoint identifies both governing artifacts;
- every day-one longitudinal artifact required by that architecture is initialized, with no requirement to invent analytically unnecessary infrastructure;
- the entrypoint's initialization state explicitly records `SEQUENTIAL_ANALYSIS_LOCK = OPEN`; and
- the new sequential artifact carries an accurate structured `artifact_type` rather than relying on its filename to establish its role.

An absent, CLOSED, malformed, or contradictory lock is a stop condition. OPEN is affirmative gate state, not a state inferred from the existence of a downstream reading. The validator recognizes substantive sequential roles through authority front matter and uses a narrow sequential-reading-directory fallback only to fail closed when such an artifact omits `artifact_type`.

Roots present at the machine control's activation baseline retain policy-defined legacy compatibility: a mature/imported project is not required to adopt the new initialization block merely for cosmetic uniformity, but any newly added sequential artifact must still route through a current-eligible canonical entrypoint that identifies a current-eligible method and synthesis/corpus architecture. Git-native post-cutover roots are checked against the full initiation contract before their next newly added sequential artifact. A material restart must opt into the prospective contract through its routing descriptor; the prior root's existence is not evidence that a new analytical generation has passed the gate.

When a project creates a bootstrap/initiation manifest, record at least its base state or bootstrap generation, governing method, governing synthesis architecture, canonical entrypoint, required day-one infrastructure state, sequential-analysis-lock state, whether substantive sequential findings existed at bootstrap, and the next permitted operation. Historical projects are not required to create a manifest retroactively. This record distinguishes path scaffolding from actual gate satisfaction.

### 3.9.3 Adoption boundary and work already on branches

The activation baseline is the immutable Git tree named by `activation_baseline_commit`, not a publication date, commit timestamp, moving `main`, or the base of the current pull request. "Newly added sequential artifact" means a classified Markdown path absent from that baseline tree. A path already in the baseline is outside this gate's new-reading detection; the repository's other integrity and authority checks still apply. New paths remain subject to the gate after their first integration. Renaming or importing an older reading to a new path can therefore invoke the gate without implying that its analysis was recently written.

Work authored on a branch before enforcement, but absent from the baseline, is checked when that branch incorporates the controls. An earlier green audit using older controls is not certification under the new gate. For an existing mature/imported root, retain the legacy route through its current method and architecture. For a Git-native root, verify existing governing artifacts and required infrastructure, then record truthful initialization state in the current entrypoint. Dates alone do not grant an exemption, and neither shifting the baseline nor marking a bootstrap OPEN without verification is an acceptable repair.

This activation-baseline test checks present governing structure; it does not authorize redoing earlier readings, rewriting prospective freezes, or replacing mature bespoke documents for cosmetic consistency. Preserve adequate existing work and backfill only material evidence gaps under the governing source policy. If an import or material restart cannot be classified from the reviewed provenance, resolve that classification explicitly before integration rather than inventing a timestamp-based exception.


### 3.9.4 Run-state consistency at admission

The activation baseline remains immutable and continues to govern architecture adoption. Separately, the validator checks a candidate's new or changed sequential artifacts against fetched `refs/remotes/origin/main`, resolved once to an immutable commit; the preparation command's `--base` cannot select this boundary. An exact-commit audit of that main head compares with its first parent so integration does not erase the admission transaction. Already integrated readings do not become new admissions merely because the current run later completes. Replacing or retyping an existing path is not a way to hide admission, including at pre-activation paths.

For a governed admission, the existing structured fields must agree: an OPEN lock, `run_state: active`, matching nonempty `next_permitted_operation` and `next_candidate_operation`, the continuation policy's mode, and recoverable `authorized_start` and `terminal_boundary`. A single-operation run has the same start and terminal unit. A completed run records both next fields as `NONE` or an uppercase `NONE_` token. Blocked, interrupted, missing, malformed or contradictory run state cannot admit a reading. Recognized run declarations in front matter and independent YAML fences must agree; deleting the execution block does not remove the check.

A final admission transaction may record `complete` or `completed` when main already records the run active with consistent next operations and bounds, the candidate preserves its mode/start/terminal boundary, and its committed high-water mark reaches that terminal boundary. A run completed on its source branch before publication may instead use the portable completion proof below. Without either route, publish under truthful active state while the run is active and record completion after acceptance; never relabel an already completed run to manufacture admission. These routes preserve an existing run's completion and do not authorize extending it.

#### Completed source-branch publication

An authorized source branch may publish its completed run in one batch using its own `.repository/completed-run-publication.json`, schema `anime-manga-ln-games-analysis/completed-run-publication/v1`. This is optional integrity evidence, not a new permission, a closure seal, a terminal-boundary amendment, or an exception to source review. It requires no project-specific global allowlist. Existing run-stop and terminal seals remain independently enforced.

The proof names the registered project root and canonical entrypoint, the exact completion commit and its direct active first parent. It carries their original textual Git commit objects, the tree nodes needed to resolve both entrypoints and the complete completion-time project tree, and historical Markdown blobs unavailable from exact candidate bytes. Every included commit, tree and blob is checked against its Git object hash; missing, malformed, substituted or contradictory evidence fails closed. The validator reconstructs all completion-time project Markdown to classify the full historical reading set, rather than trusting a declared reading list or an arbitrary active ancestor. The completed entrypoint must pass the ordinary active-to-completed transition check against that parent, and its operational fields must exactly agree with the current entrypoint.

The complete current reading set and bytes must equal that historical completed set. Added, removed, retyped, nonregular or altered readings cannot be laundered through an older completion proof, even if the proof is regenerated. Unrelated retrospective ledgers, syntheses and other nonreading changes may proceed while preserving the historical blobs needed for classification. A proof never overrides the bounds of a run already active on main. A later authorized active run uses the ordinary active admission route; an old proof grants it no source authority.

`tools/completed_run_publication.py` exports this text-only proof from available Git history and a candidate worktree. Review it with the exact publication candidate and run ordinary author preflight. A squash merge can discard source-history ancestry and object availability; the self-contained, hash-checked evidence permits the same validation in a fresh post-squash main audit without network retrieval, writing Git objects, moving comparison refs, or trusting a prior success flag. Original history remains recoverable through the source branch and publication backup. Missing proof objects still fail closed even if an unbound object happens to exist locally.

No-admission changes preserve accepted historical readings and permit retrospective claim revisions, syntheses and reconstruction. Existing inconsistent operational metadata need not be rewritten for an unrelated correction: consistency is checked when its operational fields change or admission is attempted. Mature legacy roots without structured run declarations retain their established architecture route; adopting or changing a declared run must be truthful. An existing CLOSED or terminal closure still enforces all its seals and final source boundary independently of this delta check.

These checks establish machine-readable consistency, not owner approval or semantic source-range membership. Before executing, recover the current owner instruction and its permitted units from the existing run/checkpoint or handoff record under continuation Sections 3-5 and 12; a next-operation label or agent-written `active` field is not permission. Source-inventory membership, unit identity, and whether a declared operation actually falls within a prose or live-service boundary still require source-grounded review. The local check trusts the fetched main ref; the protected exact-head audit supplies the provider-controlled context. Do not replace that ref, shift the activation baseline, or change classification to conceal an admission. No new authorization ledger or signature system is created.

---

# 4. Paired-foundation responsibility split

The required pair exists because the two governing responsibilities are different.

## 4.1 Analytical method: what to notice and how to judge it

The method answers questions such as:

- What constitutes evidence?
- Which source is authoritative?
- What must be observed prospectively?
- How do we distinguish fact from interpretation?
- How are visual/audio/textual layers handled?
- What does a complete volume/episode/chapter reading contain?
- How are predictions and contradictions treated?

## 4.2 Synthesis architecture: where accumulated knowledge goes

The architecture answers questions such as:

- Which observations must accumulate longitudinally?
- Which ledgers are canonical homes?
- Which specialist syntheses are expected?
- Which characters or relationships warrant independent synthesis?
- How are claims revised when later evidence changes earlier interpretation?
- How are evidence and locators routed?
- What must converge before full-series synthesis?
- What constitutes project completion or a frozen release?

## 4.3 The three-layer model

Projects should preserve the conceptual distinction:

> **Method -> what to notice**
>
> **Longitudinal infrastructure -> what to preserve cumulatively**
>
> **Synthesis architecture -> what the preserved evidence must ultimately support**

This distinction is one of the main safeguards against end-of-series architectural debt.

---

# 5. Minimum Semantic Contract for new synthesis architectures

Every newly created synthesis/corpus architecture must answer the following questions. It may use any structure appropriate to the work. These are required **semantic responsibilities**, not mandatory section titles or a fixed folder hierarchy.

## 5.1 Purpose, scope, and authority

The architecture must state:

- what project and source boundary it governs;
- what analytical generation it belongs to;
- its authority state;
- what governing method it depends on;
- what higher-level corpus policies govern it;
- whether any prior architecture is superseded or retained as legacy.

The architecture should normally carry machine-readable authority front matter consistent with the archive standard.

## 5.2 Source model

The architecture must explain enough of the source topology to route analysis correctly.

Depending on the project, this may include:

- primary canon;
- side stories;
- bonus chapters;
- alternate editions;
- adaptations;
- continuity branches;
- supplementary prose;
- game routes/events/commus;
- audiovisual bundles;
- original-language transcripts/subtitles;
- paratext or creator commentary.

Where source types can conflict, the architecture should identify how conflicts are classified or escalated.

### Anime episode-bundle terminology

For anime projects, the term **episode bundle** has a corpus-wide technical meaning defined by `MANGA_ANIME_EPISODE_BUNDLE_SPECIFICATION.md`. An episode bundle is a synchronized multimodal analytical derivative of one episode, not merely a screenshot ZIP. It normally binds source provenance, timestamped clean frames, manifests/indexes, primary-language subtitle or transcript material, cross-modal dialogue/frame links, audio access, and extraction/QA metadata.

Anime methods and architectures that rely on episode bundles should reference semantic roles from that specification rather than assuming a permanent literal filename set or extraction-workflow version. A screenshot-only, subtitle-only, audio-only, or contact-sheet-only package is a **partial episode derivative**, even when it is sufficient for a particular analytical purpose. Use explicit classifications such as `partial_episode_derivative`, `screenshot_derivative`, `subtitle_derivative`, and `audio_derivative`. A series architecture may declare one of these partial objects sufficient for a bounded purpose, but it may not redefine the corpus-wide term `episode bundle` below the global minimum semantic contract.

The same specification governs **continuous-video escalation**. Anime projects should remain bundle-first and request video only when a material claim depends on temporally continuous audiovisual evidence that the bundle cannot preserve with adequate confidence. Where relevant, methods should distinguish `VIDEO_NOT_REQUIRED`, `VIDEO_TARGETED_ESCALATION`, and `VIDEO_FULL_EPISODE_ESCALATION`; targeted intervals are preferred when the diagnostic region is known. Current connector/upload limits are maintained there as a time-bounded provider snapshot and must be rechecked at the specification's stated triggers. Transport constraints affect packaging and delivery, not what counts as primary audiovisual evidence.

## 5.3 Sequential-reading contract

The architecture must identify what each sequential deep reading is expected to contribute to the wider corpus.

It need not duplicate the analytical method. It should define the architectural outputs of a completed source-unit reading, for example:

- deep-reading artifact;
- cumulative ledger updates;
- new or revised claims;
- evidence locators;
- prospective register adjudication;
- source inventory advancement;
- readiness-state changes;
- corpus-map update.

A deep reading should not be considered architecturally complete merely because its standalone prose was written if required cumulative state was not advanced.

## 5.4 Longitudinal infrastructure

The architecture must identify which recurring analytical dimensions require cumulative homes.

The list must be proportional to the source. Possible dimensions include:

- character state;
- relationships;
- themes;
- institutions;
- causality;
- chronology;
- ethical reasoning;
- visual grammar;
- musical dramaturgy;
- voice/performance;
- speech register;
- world-state mechanics;
- route/branch state;
- claims and revisions;
- predictions;
- evidence locators;
- character reconstruction readiness.

A project must not create ledgers merely because another series has them.

## 5.5 Character and relationship synthesis responsibility

The architecture must state whether the project expects:

- character monographs;
- relationship specialist syntheses;
- ensemble/group syntheses;
- behavioral-policy models;
- voice/speech models;
- reconstruction/validation artifacts;
- or no dedicated character/relationship layer.

It should specify the conditions under which a character or relationship earns an independent canonical home rather than being handled inside a broader synthesis.

## 5.6 Specialist synthesis responsibilities

The architecture must identify known major analytical domains that will require specialist treatment before final integration.

These domains are series-specific. Examples might include:

- political/institutional structure;
- war and strategy;
- gender/sexuality/intimacy;
- ideology and ethics;
- memory and identity;
- music dramaturgy;
- performance and voice;
- visual grammar;
- metaphysics;
- genre structure;
- adaptation divergence;
- ending/causality;
- audience/stage ontology;
- education/work/social systems.

The architecture should distinguish **anticipated** specialists from those already mandatory. It must allow later discovery to add or remove responsibilities.

## 5.7 Evidence routing and locator responsibility

The architecture must state where mature claims obtain their evidence trail.

It should answer, where relevant:

- Where do exact chapter/page/episode/time locators live?
- Where do Japanese-language quotations or translation notes live?
- Where do screenshots/contact-sheet/shot references live?
- Where do audio/performance observations live?
- Where do source crosswalks live?
- When is a dedicated evidence matrix required?

The goal is not maximal duplication. The goal is deterministic retrieval from mature claim to source basis.

## 5.8 Claim revision and supersession behavior

The architecture must explain how later evidence can alter earlier interpretation.

For major rereads or V1->V2 work, use the established transition vocabulary where appropriate:

- `PRESERVE`
- `STRENGTHEN`
- `REVISE`
- `DOWNGRADE`
- `REJECT`
- `OPEN`

The architecture should identify whether a dedicated claim-revision ledger is required, how old claims remain discoverable, and which document becomes current authority after revision.

## 5.9 Temporal, developmental, epistemic, and continuity state

The architecture must specify how it avoids collapsing state across time.

It should distinguish as needed:

- true at source unit N versus true in the mature series interpretation;
- character knowledge versus reader knowledge;
- stated belief versus inferred motive;
- present behavior versus retrospective explanation;
- living versus posthumous evidence;
- pre-reveal versus post-reveal interpretation;
- route/branch A versus route/branch B;
- adaptation continuity versus source continuity.

This responsibility is mandatory even when the answer is simply that the source has one linear continuity and low state complexity.

## 5.10 Cross-source and contradiction handling

The architecture must state how apparent contradiction is routed rather than silently harmonized.

Potential causes may include:

- later textual revision;
- unreliable narration;
- character deception or ignorance;
- propaganda;
- translation variation;
- side-story retrospection;
- adaptation divergence;
- route divergence;
- audiovisual performance changing the force of transcript text;
- creator/paratext conflict;
- genuine inconsistency.

The architecture should identify when contradiction warrants an audit, claim revision, or unresolved/open state.

## 5.11 Synthesis dependency graph and integration order

The architecture must explain what depends on what.

At minimum, it should identify:

- what must be complete before specialist synthesis begins;
- which specialist outputs are inputs to other specialist outputs;
- whether claim/evidence stabilization precedes specialist synthesis;
- what must converge before final full-series synthesis;
- whether character reconstruction or validation occurs before or after literary integration;
- what audits are required before release/freeze.

A simple project may express this in a few lines. A complex project may need a dependency graph.

## 5.12 Architecture extension and amendment rule

The initial architecture must explicitly permit analytically justified evolution.

A new ledger, specialist responsibility, or analytical layer may be added when a dimension:

- recurs across multiple source units;
- accumulates evidence independently;
- affects later synthesis;
- cannot be represented adequately in existing canonical homes;
- or requires independent retrieval for future work.

Material changes should be recorded in the current corpus map and architecture revision history.

A newly discovered dimension does **not** automatically require re-reading all prior material. Backfill is required only when the missing dimension creates a material evidence gap that cannot be responsibly repaired from existing deep readings and retained primary sources.

## 5.13 Completion gates

The architecture must define meaningful completion boundaries.

At minimum, distinguish:

1. sequential-source completion;
2. longitudinal-state completion or reconciliation;
3. specialist-synthesis readiness;
4. full-series synthesis readiness;
5. validation/audit completion where applicable;
6. frozen/release state.

**Sequential completion does not automatically authorize full-series synthesis.**

Before full-series synthesis begins, the project should conduct an architecture/role-gap check to confirm that the specialist responsibilities and evidence/revision infrastructure actually needed by the completed source have been satisfied.

## 5.14 Reasoning-class assignments

The architecture should assign stable reasoning classes to major artifact roles when the workload materially differs.

Use `MANGA_ANIME_REASONING_AND_MODEL_ROUTING_POLICY.md` for definitions and current provider mappings.

Series-specific architecture may override corpus defaults when justified by unusual contradiction density, source complexity, branching state, audiovisual burden, or propagation risk.

## 5.15 Archival, mutable-state, and freeze behavior

The architecture must identify which files are expected to remain mutable and which become frozen.

Examples:

- current-state files and cumulative ledgers may be updated in place;
- frozen checkpoints should remain immutable;
- completed release packages should not be silently mutated;
- superseded analysis should route to legacy/provenance rather than disappearing;
- conversation archives are provenance, not preferred analytical authority once structured artifacts exist.

## 5.16 Entrypoint and retrieval route

The architecture must identify the canonical first-read document and recommended retrieval route.

A future chat or agent should be able to answer:

- Where do I start?
- What is current authority?
- What source boundary has been completed?
- What operation is next?
- Which artifacts must I read before changing project state?

without reconstructing those answers from old conversation transcripts.

---

# 6. Required responsibility matrix

New architectures should normally include a compact responsibility matrix connecting sequential observation to cumulative preservation and final synthesis.

Recommended form:

| Analytical dimension | Sequential capture? | Canonical cumulative home | Final analytical destination | Initialization state |
|---|---|---|---|---|
| Character state | As required | Character/state ledger | Character monographs or integrated synthesis | initialized / deferred / N/A |
| Relationships | As required | Relationship ledger | Dyadic/ensemble synthesis | initialized / deferred / N/A |
| Major claims | Yes for material claims | Claim/revision ledger or deep-reading state | Specialist + final synthesis | initialized / deferred / N/A |
| Visual evidence | If diagnostic | Visual evidence/index layer | Visual specialist synthesis | initialized / deferred / N/A |
| Institutions/world state | If recurring | Institutional/world ledger | Political/world synthesis | initialized / deferred / N/A |
| Music/voice/performance | If source-relevant | Performance/music ledger | Audiovisual specialist synthesis | initialized / deferred / N/A |

The rows are not standardized. The **mapping responsibility** is standardized.

Every recurring observation should have one of three explicit destinations:

1. cumulative canonical home;
2. direct specialist/final synthesis responsibility;
3. intentionally local-only evidence with no longitudinal responsibility.

This avoids accumulating analytically important observations that have no planned retrieval route.

---

# 7. Architecture lifecycle

Architecture is authoritative but not permanently frozen at project birth.

## 7.1 `INITIAL`

Created from source reconnaissance before substantive sequential reading.

The architecture establishes known responsibilities, initial ledgers, anticipated specialist domains, and completion gates while explicitly acknowledging uncertainty.

## 7.2 `EVOLVING`

Sequential reading has exposed recurring dimensions or source behavior that justify architectural extension.

Permitted actions include:

- adding a new cumulative ledger;
- defining a new specialist synthesis responsibility;
- revising dependency order;
- adding cross-source conflict handling;
- creating a backfill task where material evidence would otherwise be lost.

Changes must preserve prior authority history.

## 7.3 `STABILIZED`

Enough of the source has been analyzed that the mature synthesis responsibilities are substantially known.

The architecture may still change, but material changes should trigger explicit review because downstream specialist work may already depend on it.

## 7.4 `FROZEN` or release-locked architecture

When the project explicitly freezes an architecture as part of a release, later structural changes should normally become a new version rather than silently mutating the frozen release.

---

# 8. Architecture review checkpoints

Reviews should occur at semantic boundaries rather than by rigid percentage alone.

Useful triggers include:

- end of the first major arc;
- end of a season;
- completion of an early volume tranche;
- midpoint or established checkpoint;
- discovery of a major new source type;
- discovery of branching continuity;
- emergence of a recurring analytical dimension not covered by current ledgers;
- completion of sequential reading;
- immediately before specialist synthesis;
- immediately before full-series integration;
- before a frozen release.

A review asks:

1. Is the current method still capturing what the architecture now requires?
2. Are recurring observations being preserved in canonical cumulative homes?
3. Has any new specialist responsibility emerged?
4. Are any planned specialist documents no longer justified?
5. Are claim-revision and evidence routes sufficient?
6. Does any missing layer require backfill?
7. Does the dependency graph still reflect the actual project?
8. Is the current reasoning-class routing still appropriate?

---

# 9. Sequential completion and synthesis gate

A project reaching its final episode, volume, chapter, route, or event does **not** automatically transition to full-series synthesis.

The required transition is:

> **Sequential completion -> completion audit -> architecture/role-gap audit -> evidence/claim stabilization as required -> specialist synthesis -> cross-specialist convergence -> full-series synthesis -> validation/release audit as applicable**

Projects may compress these stages when the work is small, but they may not silently skip a material responsibility identified by their architecture.

This rule specifically prevents the situation in which a project completes sequential reading and only then discovers that no governing structure exists for character monographs, relationship studies, thematic specialists, evidence matrices, or claim revision.

---

# 10. Existing projects and grandfathering

This policy is prospective. Existing mature projects are **grandfathered**.

Do not create replacement documents solely to make old projects cosmetically conform.

At the next natural analytical boundary for an existing project:

1. inspect the canonical method and current corpus map;
2. determine whether both required responsibilities are already substantively covered;
3. preserve mature bespoke structures when adequate;
4. create or amend only genuinely missing governance;
5. initialize missing longitudinal infrastructure only when it adds real analytical value;
6. backfill prior readings only when a material evidence gap exists;
7. update the current corpus map to make present authority and next steps explicit.

Examples:

- A mature project with a strong deep-reading method and fully developed synthesis architecture needs no change.
- A project with a strong method but no synthesis architecture should create the missing architecture before entering synthesis.
- A project whose single governing document already explicitly covers both method and architecture may retain it.
- A completed/frozen corpus should not be restructured unless a migration or new analytical generation is explicitly initiated.

---

# 11. Proportionality rule

Architecture must be proportional to the source and analytical purpose.

Do not copy the complexity of large projects such as Revue Starlight, Monogatari, NANA, Gakuen Idolmaster, IDOLY PRIDE, or another mature corpus into a smaller work merely because those architectures exist.

Conversely, extend architecture when the source genuinely demands independent treatment of recurring dimensions.

A useful test for creating a new ledger or specialist home is whether the dimension:

- recurs;
- accumulates evidence;
- affects later interpretation;
- supports independent retrieval;
- or would otherwise be repeatedly reconstructed from scattered deep readings.

If not, keep it local or integrate it into an existing canonical home.

---

# 12. Medium-specific architecture examples

The minimum semantic contract does not imply identical implementations.

## 12.1 Manga

May emphasize:

- volume/chapter/page evidence;
- page composition and panel grammar;
- translation/source-language notes;
- visual motif indexing;
- character/relationship longitudinal state;
- claim revision across later revelations.

Voice-performance infrastructure is normally irrelevant unless an adaptation is explicitly inside the same source boundary.

## 12.2 Anime

May add:

- shot/staging/visual grammar;
- voice performance;
- music dramaturgy;
- subtitle/transcript crosswalks;
- episode-level audiovisual evidence bundles;
- production-specific or adaptation-divergence layers.

## 12.3 Light novels and novels

May emphasize:

- prose voice;
- focalization;
- narrator reliability;
- interiority;
- source-language wording;
- chronology and retrospective revelation;
- volume-level state transitions.

## 12.4 Games and branching narratives

May require:

- route/branch identity;
- continuity-state modeling;
- event chronology;
- character-state transitions across optional content;
- relationship-state branching;
- commu/story/song/MV layers;
- cross-game identity resolution;
- contradiction handling across parallel canons.

These examples are illustrative, not mandatory templates.

---

# 13. Naming and metadata expectations

For new projects, prefer the established naming grammar:

`<SERIES>_<SCOPE>_<ARTIFACT_ROLE>.md`

Common governing roles include:

- `ANALYTICAL_METHOD`
- `SYNTHESIS_ARCHITECTURE`
- `SOURCE_INVENTORY`
- `SOURCE_LOCK`
- `DEEP_READING`
- `LEDGER`
- `EVIDENCE_MATRIX`
- `CHARACTER_MONOGRAPH`
- `SPECIALIST_SYNTHESIS`
- `FULL_SERIES_SYNTHESIS`
- `CLAIM_REVISION_LEDGER`
- `LOCATOR_INDEX`
- `CROSSWALK`
- `CORPUS_MAP`
- `AUDIT`
- `MANIFEST`

New analytical Markdown artifacts should normally carry authority metadata including series, artifact type, scope, generation, status, source boundary, supersession state, and `do_not_use_as_current_authority` where applicable.

Existing mature naming conventions remain valid when coherent.

---

# 14. Relationship to other corpus-wide governance

This policy has a distinct responsibility from the other top-level policies.

## `ARCHIVE_AUTHORITY_AND_SUPERSESSION_POLICY.md`

Answers:

> **Which artifact is current authority, and how are legacy/superseded artifacts preserved?**

## `MANGA_ANIME_REASONING_AND_MODEL_ROUTING_POLICY.md`

Answers:

> **What stable reasoning class should perform a given analytical operation, and how does that currently map to available models?**

## `MANGA_ANIME_PROJECT_INITIATION_AND_ARCHITECTURE_POLICY.md`

Answers:

> **What governing infrastructure must exist before a new substantive analytical project begins, and what minimum responsibilities must every new synthesis architecture cover?**

## `MANGA_ANIME_EPISODE_BUNDLE_SPECIFICATION.md`

Answers:

> **What does the corpus mean by an anime episode bundle, which synchronized evidence layers does it expose, and how should analysts distinguish it from a screenshot set or other partial derivative?**

## `MANGA_ANIME_DRIVE_INDEX.md`

Answers:

> **Where is the current canonical project, governance file, analytical artifact, or source route?**

The Drive index is a router. It should point to this policy rather than duplicating its full contents.

---

# 15. Compliance checklist for a newly initiated project

Before opening the first substantive sequential deep reading, verify:

- canonical series root resolved;
- existing project/alias search completed;
- preliminary source reconnaissance sufficient;
- canonical analytical/deep-reading method exists;
- canonical synthesis/corpus architecture exists;
- architecture satisfies the Minimum Semantic Contract;
- current-state/corpus-map entrypoint exists;
- required day-one longitudinal ledgers are initialized;
- responsibility matrix is present or equivalently represented;
- source/conflict/continuity rules are explicit enough for the work;
- architecture extension rule exists;
- synthesis completion gates exist;
- reasoning classes are inherited or assigned appropriately;
- sequential-analysis lock is explicitly open.

If any analytically material item is missing, keep the lock closed and repair the project foundation before beginning the sequential pass.

---

# 16. Governing principle in compact form

> **Every new substantive project begins with a paired foundation: a method that defines how evidence will be read and an architecture that defines how evidence will accumulate, revise, specialize, and converge. The architecture must satisfy a minimum semantic contract, but its concrete structure must remain proportional to the work. New discoveries may extend the architecture without invalidating the project; mature projects are preserved rather than cosmetically normalized.**

This policy exists so that the corpus never again reaches the end of a long sequential reading program only to discover that the analytical infrastructure needed for synthesis should have existed from the beginning.

---

# Changelog

## v1.8 — 2026-10-20 — Completed source-branch publication

- Adds an optional portable, hash-checked completion proof for a run completed before its first batched publication.
- Requires a real active-to-completed transition, identical operational bounds and the exact complete reading set; preserves ordinary admission, architecture, source-authorization and closure checks.
- Makes proof validation independent of source object availability after a squash merge without adding a global project exception or weakening missing-evidence failures.

## v1.7 — 2026-10-15 — Run-state consistency without routine seals

- Makes an unsealed completed-run stop explicit and preserves optional run seals and required terminal seals.
- Separates immutable architecture adoption from incoming admission checks, including active-to-completed transactions and historical compatibility.
- Distinguishes state consistency from owner authorization and semantic source-scope review.

## v1.6 — 2026-10-15 — Run stops, one state vocabulary, and the gate's enforcement text

- Moved the repository-enforcement text for the gate from the change-integration checklist into Section 3.9, unchanged except for its headings and two closure paragraphs that restated Section 3.8.
- Pointed project-root resolution (Section 3.1) at the corpus index and the series and study registries, keeping the Drive index for Drive-native material.
- Added guidance to keep entrypoints about the present, with dated history moved verbatim to a project changelog (Section 3.5).
- Added the project-local run stop (`.repository/run-closure.json`, CLOSED or REOPENED) for the end of an authorized run, validated like a terminal closure, written on the project's own branch, and bound to `main` by completion-commit ancestry and seal continuity, with owner-merged one-shot releases.
- Reserved the global `terminal_closures` record for a project's final source boundary; a project may not carry both.
- Named the one spelling for each lock and run-state field and the consistency expected between them.
- Preserved the initiation lock, foundation requirements, seals, and the owner authorization required to admit a source.

## v1.5 — 2026-10-14 — Admission, retention, and revision at terminal closure

- Separated source admission, historical retention, and analytical revision in Section 3.8, and stated how corrections proceed under a terminal closure without admitting a source or editing sealed readings.
- Recorded the reviewed `terminal_closures` control, added on 2026-10-04, as one coordinated entrypoint and global-control transaction, with the disclosed interim state for a scope-limited task.
- Stated the surfaces and tokens the validator reads for terminal state, including the continuation policy's `completed` run state.
- Preserved the initiation lock, foundation requirements, closure seals, and owner-authorization boundaries.

## v1.4 — 2026-09-13 — Hybrid execution ownership

- Added execution ownership and synthesis-dispatch guidance through the capability, long-series, and handoff policies.
- Preserved the existing initiation lock, semantic foundation requirements, and machine enforcement boundary.

## v1.3 — 2026-08-27 — Administrative terminology hardening

- Reserved `status` for authority state in the initialization template and added `architecture_lifecycle: INITIAL` for lifecycle state.
- Preserved the corpus-wide minimum meaning of `episode bundle`; series architectures may accept a partial derivative for a bounded purpose but may not relabel it as a complete bundle.
- Replaced duplicated literal transport thresholds with routing to the episode-bundle specification's time-bounded provider snapshot.

