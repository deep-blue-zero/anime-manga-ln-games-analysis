---
title: Manga / Anime Sequential Execution Scope and Continuation Policy
artifact_id: MANGA_ANIME_SEQUENTIAL_EXECUTION_SCOPE_AND_CONTINUATION_POLICY
artifact_type: sequential_execution_scope_policy
version: 1.0
status: canonical
generation: V1
scope: corpus-wide sequential analytical execution authorization, continuation, checkpointing, recovery, and stop semantics
created: 2026-08-27
maintainer: ChatGPT + user
source_boundary: "Operational governance for sequential volume, episode, chapter, event, route, commu, movement, and comparable analytical units across the Manga / Anime corpus"
supersedes: null
superseded_by: null
do_not_use_as_current_authority: false
do_not_use_as_literary_evidence: true
---

# Manga / Anime Sequential Execution Scope and Continuation Policy

## Governing rule

> **Every sequential analytical request has an execution scope. Unless the user explicitly authorizes continued sequential execution, the default scope is `single_operation`: complete one canonical source-unit transaction, close it out fully, identify the next operation, and stop. When the user explicitly authorizes `continuous_sequential`, continue committing complete atomic source-unit transactions until the named terminal boundary is reached or a genuine blocker requires intervention.**

This policy governs **how far an analytical execution is authorized to proceed**, not how a source should be interpreted and not how the resulting corpus should be architected.

It exists to remove an ambiguity that became operationally significant in long-running corpus work: a completed deep reading or manifest often names a **next sequential operation**. That field is normally a routing statement, not an instruction to execute the next unit. Conversely, for large bounded runs such as all remaining manga volumes or hundreds of live-service events, requiring a new user message after every successfully committed unit creates unnecessary supervisory overhead.

The corpus therefore recognizes two explicit execution modes:

- `single_operation`
- `continuous_sequential`

Both modes preserve the same source discipline, atomic closeout requirements, authority rules, prospective boundaries, and cumulative-state obligations. They differ only in **continuation authorization and stop behavior**.

---

# 1. Scope and relationship to other corpus policies

This policy applies to sequential analytical operations across the Manga / Anime corpus, including as appropriate:

- manga volumes and chapters;
- anime episodes, films, movements, OVAs, ONAs, and specials;
- light-novel or prose volumes;
- game events, commus, routes, chapters, stories, and other ordered narrative units;
- live-service narrative releases;
- sequential source-reconstruction or extraction-backed analytical units;
- other corpus-defined source units whose analysis advances a durable high-water mark.

It is intentionally orthogonal to the other corpus-wide governance documents.

## `MANGA_ANIME_PROJECT_INITIATION_AND_ARCHITECTURE_POLICY.md`

Answers:

> **What governing infrastructure must exist before substantive sequential analysis begins, and where will accumulated knowledge go?**

## `MANGA_ANIME_REASONING_AND_MODEL_ROUTING_POLICY.md`

Answers:

> **What stable reasoning class should perform a given analytical operation, subject to current provider mappings?**

## Series-specific analytical method

Answers:

> **How should each source unit be read, what counts as evidence, and which prospective/epistemic distinctions must be preserved?**

## Series-specific synthesis/corpus architecture

Answers:

> **Which cumulative ledgers, specialist responsibilities, evidence structures, and synthesis targets must a completed source-unit reading advance?**

## This policy

Answers:

> **How many sequential source-unit transactions has the user authorized this execution to perform, when may it automatically proceed to the next unit, and when must it stop or recover?**

No execution mode overrides a stronger source, authority, architecture, safety, or user instruction.

---

# 2. Atomic sequential operation

The execution modes operate on **atomic sequential operations**.

An atomic sequential operation is the smallest architecturally complete unit by which the project normally advances its source high-water mark. Depending on the project, the unit may be:

- one volume;
- one episode;
- one chapter or chapter tranche;
- one event;
- one route;
- one commu;
- one film movement;
- another explicitly defined source unit.

Atomicity is architectural rather than conversational. One atomic operation may require many tool calls, source extractions, analysis passes, and artifact writes.

A source-unit transaction is not considered complete merely because its standalone deep-reading prose exists. Unless the governing project architecture says otherwise, completion normally requires all applicable responsibilities such as:

1. source resolution and source lock;
2. prospective entering boundary;
3. full deep-reading artifact or equivalent canonical unit artifact;
4. required cumulative ledger/state updates;
5. claim-revision or prediction adjudication where applicable;
6. source locator/evidence/index updates where applicable;
7. character/relationship/readiness changes where applicable;
8. current-state/corpus-map advancement;
9. update manifest, checkpoint, or equivalent transaction record where the project uses one;
10. a clearly frozen endpoint and next-operation route.

Only after the atomic unit is committed may `continuous_sequential` authorize movement to the next unit.

---

# 3. Execution mode: `single_operation`

## 3.1 Definition

`single_operation` authorizes exactly **one atomic sequential operation** from the verified current high-water mark or explicitly named target.

Examples:

- `Start MHA_SP2_V35_DEEP_READING.md.`
- `Analyze the next Love Live Superstar episode.`
- `Continue with EVENT_0053.`
- `Do Volume 8 next.`

Unless the wording explicitly grants broader continuation authority, these requests are interpreted as `single_operation`.

## 3.2 Required behavior

Under `single_operation`:

1. resolve the live canonical project state;
2. verify the requested unit is actually the next authorized/correct operation;
3. perform the complete atomic transaction;
4. commit all required artifacts and cumulative updates;
5. state the newly frozen high-water mark;
6. identify the next sequential operation;
7. **stop**.

The execution may complete as many internal substeps and create/update as many architecturally required artifacts as necessary to close the one unit. The limit is on **sequential source units**, not tool calls or artifact count.

## 3.3 `Next sequential operation` is informational by default

A line such as:

`Next sequential operation: MHA_SP2_V36_DEEP_READING.md`

or:

`Next: EVENT_0054`

is a **routing statement**, not continuation authorization.

Under `single_operation`, the presence of such a line in a deep reading, manifest, corpus map, handoff, or index must not by itself trigger execution of that next unit.

This rule applies even when the next unit is obvious, sources are already available, and no analytical blocker exists.

## 3.4 Default rule for ambiguity

If execution scope is ambiguous, use `single_operation`.

Examples that remain single-operation unless surrounding language clearly says otherwise:

- `continue`;
- `resume`;
- `do the next one`;
- `start V35`;
- `continue the sequential reading` when only one immediate unit is named and no terminal run boundary is granted.

The purpose is to prevent an informational handoff from silently becoming hours of additional analytical work.

---

# 4. Execution mode: `continuous_sequential`

## 4.1 Definition

`continuous_sequential` explicitly authorizes the execution to proceed from one completed atomic sequential operation directly into the next **without waiting for a new user message between ordinary units**.

The authorization must include or imply a recoverable terminal boundary.

Examples:

- `Process V35 through V42 continuously.`
- `Continue through all remaining currently published volumes.`
- `Process EVENT_0053 through EVENT_0211 sequentially.`
- `Analyze the rest of Season 2 continuously.`
- `Keep going episode by episode until the season is complete.`

A bounded range of two or three units is still `continuous_sequential`; no third execution mode is required.

## 4.2 Terminal boundary

The terminal boundary should be explicit whenever practical. Stable forms include:

- exact ordinal: `V42`, `E24`, `EVENT_0211`;
- exact source range: `V35-V42`;
- a frozen project phase: `through the end of Season 2`;
- a live-service boundary resolved at execution start: `through all events present in the locked inventory as of this run`.

Avoid open-ended formulations such as `forever` or `keep analyzing future releases` as the terminal definition for one execution contract. Future-release monitoring belongs to a separate scheduled/conditional workflow rather than an unbounded sequential transaction.

## 4.3 Required behavior

For each unit in a `continuous_sequential` run:

1. recover the live high-water mark;
2. resolve the next source unit;
3. establish that unit's prospective entering boundary;
4. perform the complete source-unit analysis;
5. commit immutable unit artifacts;
6. update required mutable cumulative state;
7. verify the closeout/high-water mark;
8. checkpoint the run state;
9. release unnecessary unit-local working context;
10. proceed immediately to the next authorized unit.

The next unit must not begin merely because analysis prose for the prior unit has been drafted. The prior unit must be transactionally closed to the degree required by its architecture.

## 4.4 Continuous authorization does not weaken prospective discipline

Continuous processing changes execution cadence, not evidence rules.

For a prospective reread, each unit must still behave as though later units are unavailable as evidence except where the governing method explicitly permits retrospective material.

For example, processing `EVENT_0053-EVENT_0211` in one continuous run does **not** allow an EVENT_0130 conclusion to leak backward into the canonical EVENT_0080 reading.

Each source unit receives its own frozen entering and exiting boundary.

## 4.5 Continuous authorization does not require one uninterrupted inference

`continuous_sequential` is a **workflow authorization**, not a claim that one model inference, frontend message, agent process, or context window is guaranteed to remain alive through the entire terminal boundary.

A long run may encounter:

- context compaction;
- tool or connector limits;
- UI timeout;
- execution interruption;
- environment restart;
- user interruption;
- another concurrent analytical transaction.

The durable corpus state, not uninterrupted conversational memory, must define what has actually completed.

Where the product/runtime supports continued execution, the run may proceed automatically after each checkpoint. Where a new execution must be started, the declared run target and last verified high-water mark should make recovery deterministic rather than forcing reconstruction from conversation history.

---

# 5. High-water-mark and checkpoint contract

Every continuous run should maintain a recoverable distinction between:

- **authorized terminal boundary** — how far the user has authorized the run to go;
- **verified committed high-water mark** — the latest atomic unit known to be canonically closed;
- **next candidate operation** — what would execute next if no blocker exists;
- **run state** — active, completed, blocked, or interrupted pending recovery.

Recommended machine-readable state for active projects:

```yaml
sequential_execution:
  mode: continuous_sequential
  unit_type: event
  authorized_start: EVENT_0053
  terminal_boundary: EVENT_0211
  committed_high_water_mark: EVENT_0052
  next_candidate_operation: EVENT_0053
  confirmation_between_units: false
  run_state: active
```

For an ordinary one-unit request:

```yaml
sequential_execution:
  mode: single_operation
  unit_type: volume
  authorized_start: V35
  terminal_boundary: V35
  committed_high_water_mark: V34
  next_candidate_operation: V35
  confirmation_between_units: true
  run_state: active
```

Projects do not need to reproduce these exact key names if an established architecture already stores equivalent state. Semantic recoverability matters more than identical YAML.

After each successful continuous transaction, advance `committed_high_water_mark` only after required canonical state has actually been written and verified.

---

# 6. Context discipline for long continuous runs

Continuous execution must not equate **live model context** with **canonical longitudinal memory**.

The corpus is the durable memory system. The active context is a working set.

## 6.1 Preferred per-unit context model

At the start of each unit, load only what is materially necessary, typically:

1. current corpus map / authoritative high-water mark;
2. governing analytical method;
3. governing synthesis/corpus architecture;
4. relevant current cumulative ledgers and open-claim/prediction state;
5. source inventory/locator state needed for the next unit;
6. the next unit's primary source and derivatives;
7. narrowly relevant prior unit evidence when the current task genuinely depends on it.

Do not require the full prose of every previously completed deep reading to remain in active context merely because the units were processed in one continuous authorization.

## 6.2 Commit, compact, continue

The preferred conceptual loop is:

> **load checkpoint -> process one atomic unit -> commit canonical state -> verify -> compact/release unit-local context -> process next unit**

not:

> **accumulate every prior reading verbatim in one ever-growing working context until the terminal boundary**

This reduces context pressure, retrieval noise, prospective contamination, and accidental preference for stale conversational memory over canonical artifacts.

## 6.3 Canonical artifacts dominate conversational recollection

If live context and current canonical artifacts disagree, re-resolve authority from the corpus before proceeding.

A remembered prior state is never sufficient reason to overwrite a newer mutable ledger or move a high-water mark backward.

---

# 7. Timeout, stall, and ambiguous-commit recovery

A UI message such as `message timed out`, an apparently stalled response, a lost frontend connection, or another incomplete presentation state must **not** be treated as proof that the analytical transaction was cancelled or rolled back.

Treat it as an **ambiguous transaction state**.

## 7.1 Recovery-only mode before new writes

After an ambiguous interruption, the next execution must enter recovery-only mode before performing new Drive writes.

At minimum:

1. re-read the live series `CURRENT_STATE_AND_CORPUS_MAP.md` or equivalent entrypoint;
2. re-read the live `MANGA_ANIME_DRIVE_INDEX.md` where corpus-wide state is relevant;
3. search for the interrupted target's canonical artifact and manifest;
4. search at least the immediately following sequential units when a prior execution could plausibly have continued;
5. inspect modification times/revisions for mutable state if concurrent overwrite is possible;
6. determine the actual canonical high-water mark;
7. only then decide what operation remains to be done.

## 7.2 High-water mark dominates requested ordinal after interruption

If a recovery request says `start V32` but live authority shows `V32-V34` are already canonically complete, do not recreate V32.

Adopt the observed canonical state and route from V35.

The same rule applies to events, episodes, chapters, routes, and other sequential units.

## 7.3 Continuous-run recovery

If a `continuous_sequential` run was authorized through EVENT_0211 and interruption occurs after EVENT_0096 is canonically committed, recovery state is conceptually:

```text
authorized terminal boundary = EVENT_0211
verified committed high-water mark = EVENT_0096
next candidate operation = EVENT_0097
```

The interruption does not retroactively invalidate EVENT_0053-EVENT_0096. Nor should EVENT_0097 be inferred complete merely because it may have been in progress.

Verify before resuming.

---

# 8. Concurrency and mutable-state protection

Sequential continuation authorization does not grant permission to overwrite concurrent work.

Before each mutable cumulative-file write:

1. fetch the current live copy/revision;
2. compare it with the state on which the pending update was based;
3. if the live state advanced, abort the stale replacement;
4. merge/rebase onto the newer state;
5. ensure the resulting high-water mark never regresses.

This applies especially to:

- current-state/corpus maps;
- cumulative character/relationship/thematic ledgers;
- readiness trackers;
- source inventories;
- claim/revision ledgers;
- global routing indexes.

Immutable per-unit deep readings and manifests are easier to deduplicate by content/hash. Mutable cumulative state is the greater concurrency risk because a stale writer can silently erase later progress.

The global `MANGA_ANIME_DRIVE_INDEX.md` should remain an end-of-transaction routing write and must be freshly rebased immediately before modification.

---

# 9. Genuine blockers and stop conditions

## 9.1 `single_operation` stops when

- the one authorized atomic operation is canonically closed; or
- a genuine blocker prevents its safe completion.

## 9.2 `continuous_sequential` stops when

- the terminal boundary is canonically completed;
- the user explicitly interrupts, narrows, or cancels the run;
- a required primary source is missing, corrupt, inaccessible, or cannot be unambiguously resolved;
- an authority/supersession conflict cannot be safely adjudicated from available canonical infrastructure;
- a required permission or tool capability is unavailable;
- a source-boundary ambiguity would materially contaminate prospective analysis;
- a concurrent transaction creates an unresolved state conflict;
- another genuine analytical or operational blocker requires user judgment.

Ordinary completion of one source unit, availability of the next source, or the existence of a `Next:` handoff line is **not** a blocker in continuous mode.

Runtime interruption is not itself evidence that the terminal boundary was reached. It triggers recovery semantics.

---

# 10. User-language resolution rules

Execution scope should normally be inferable without forcing the user to use the literal ontology names.

## Resolve to `single_operation`

Examples:

- `Start Volume 35.`
- `Do the next event.`
- `Continue with episode 9.`
- `Resume the V14 deep reading.`

## Resolve to `continuous_sequential`

Examples:

- `Do V35 through V42 continuously.`
- `Keep processing volumes until the manga is finished.`
- `Analyze every remaining episode in Season 3.`
- `Process all 211 events sequentially.`
- `Continue from EVENT_0053 through EVENT_0211 without asking me between events.`

If the user gives an explicit range or terminal boundary, that is strong evidence for `continuous_sequential` even if the literal term is not used.

If the user explicitly says to stop after each unit, that instruction overrides any broader default.

---

# 11. Worked corpus examples

## 11.1 My Hero Academia

Request:

`Start MHA_SP2_V35_DEEP_READING.md.`

Resolution:

`single_operation`

Expected behavior:

- verify V34 is the current high-water mark;
- complete and canonize V35 plus all required cumulative updates;
- identify V36 as next;
- stop.

Request:

`Process MHA V35 through V42 continuously.`

Resolution:

`continuous_sequential`

Expected behavior:

- V35 is one atomic transaction;
- commit/verify V35;
- continue to V36 without waiting for confirmation;
- repeat through V42;
- preserve a separate prospective freeze for each volume;
- stop when V42 is canonically closed or a genuine blocker occurs.

## 11.2 Project Sekai

Request:

`Continue with EVENT_0053.`

Resolution:

`single_operation`

Request:

`Process EVENT_0053 through EVENT_0211 sequentially, generating each event's canonical artifacts and cumulative updates.`

Resolution:

`continuous_sequential`

The correct implementation is **not** to keep the complete prose of 159 prior event readings in active context while processing EVENT_0211. Each event should close atomically, update the canonical longitudinal state, checkpoint the high-water mark, and release unnecessary event-local working material before the next event begins.

## 11.3 Short bounded batch

Request:

`Do episodes 7, 8, and 9 in sequence.`

Resolution:

`continuous_sequential`

Terminal boundary:

`E09`

No separate `batch` mode is necessary; continuous execution already supports finite ranges of any length greater than one.

---

# 12. Recommended project-state representation

Series corpus maps and long-running live-service projects may record execution authorization when it materially helps recovery.

Recommended fields:

```yaml
sequential_execution:
  mode: single_operation | continuous_sequential
  unit_type: volume | episode | event | chapter | route | commu | other
  authorized_start: <scope>
  terminal_boundary: <scope>
  committed_high_water_mark: <scope>
  next_candidate_operation: <scope>
  confirmation_between_units: true | false
  run_state: active | completed | blocked | interrupted_pending_recovery
```

This block is **operational state**, not literary evidence and not a substitute for the project's source inventory or prospective ledger.

When no continuous run is active, projects need not preserve stale `run_state: active` metadata merely because an earlier chat once requested a range. Completed or abandoned run metadata may be collapsed into manifests/audits according to the project's architecture.

---

# 13. Corpus-wide default

The final default is deliberately simple:

> **One named unit means one unit unless broader continuation is explicit.**

> **A named range, all-remaining instruction, or explicit terminal boundary authorizes continuous sequential execution through that boundary.**

> **Every unit remains atomic and independently recoverable.**

> **`Next sequential operation` is routing information, not authorization, unless the current execution is already in `continuous_sequential` mode.**

> **After interruption, observed canonical high-water mark outranks remembered conversational state.**

This preserves user control for ordinary deep readings while making large sequential corpora—such as long manga runs, multi-season anime passes, and hundreds of live-service events—operationally tractable without sacrificing source discipline, authority integrity, or recoverability.
