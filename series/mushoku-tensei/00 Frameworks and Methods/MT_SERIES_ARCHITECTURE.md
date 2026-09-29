---
title: "Mushoku Tensei - Series Architecture"
artifact_id: "MT_SERIES_ARCHITECTURE"
artifact_type: "synthesis_corpus_architecture"
series: "Mushoku Tensei"
generation: "V1"
version: "1.1"
status: canonical
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
do_not_use_as_literary_evidence: true
created: "2026-09-25"
design_reference_commit: "a2a1ab9a5ecd0512a5ac460c1b79655af1bca0bd"
adopted_on: "2026-09-25"
adoption_basis_commit: "a2a1ab9a5ecd0512a5ac460c1b79655af1bca0bd"
canonical_home: "series/mushoku-tensei/00 Frameworks and Methods/MT_SERIES_ARCHITECTURE.md"
source_boundary: "Accepted bootstrap method or template; no sequential novel readings or validated character models as of adoption."
recommended_reasoning_class: "PREMIUM_QUALITY_FIRST"
---

# Series architecture

## 1. One corpus, three end products

The project should support substantial literary interpretation, state-specific character reconstruction, and evidence-led assessment of public arguments. None is a substitute for the others. A collection of chapter summaries, a library of fluent roleplay, or a controversy verdict alone would not satisfy this architecture.

Resolved root: `series/mushoku-tensei/`. Continuing branch: `series/mushoku-tensei`. The one current entrypoint is `CURRENT_STATE_AND_CORPUS_MAP.md` at that root. The current main/branch/root and title-alias searches at adoption found no prior Mushoku Tensei analytical root or branch. Preserve this identity in later work.

The architecture is `INITIAL` at adoption, may become `EVOLVING` and `STABILIZED`, and is frozen only for a declared release. It does not supersede an undiscovered prior architecture. Current live repository governance, source precedence, and existing approved work remain controlling.

## 2. Governing document responsibilities

| Document | Sole governing responsibility |
|---|---|
| `MT_ANALYTICAL_METHOD.md` | How volumes are inspected and claims formed. |
| `MT_SERIES_ARCHITECTURE.md` | Artifact ownership, accumulation, dependencies, stage gates, and completion. |
| `MT_SOURCE_AND_SCOPE_MAP.md` | Source classes, edition identity, lane admission, and evidence-plane boundaries. |
| `MT_CHARACTER_RECONSTRUCTION_SPEC.md` | Operational character models, readiness, and validation. |
| `MT_NORMATIVE_FRAMING_PROTOCOL.md` | Tests of narrative evaluation and moral-development claims. |
| `MT_TEXTUAL_HISTORY_METHOD.md` | Comparison of witnesses and warranted claims about revision/intent. |
| `MT_DISCOURSE_HYPOTHESIS_METHOD.md` | Hypothesis formulation, reception sampling, and discourse adjudication. |
| `MT_VOLUME_READING_TEMPLATE.md` | Reusable output structure; not an actual source reading. |
| `MT_BOOTSTRAP_AND_LEDGER_TEMPLATES.md` | Initialization examples and local record formats; no completed state. |
| `MT_SYNTHESIS_AND_HANDOFF_SPEC.md` | Target-specific acceptance and transfer contracts. |

Do not repeat entire governing rules across artifacts. Link the owner. A template implements a method; it cannot override it. Method and architecture are the mandatory pair; this design also requires adopted source, character, and normative protocols before substantive LN execution. Textual-history and discourse protocols must be adopted before their respective lanes open. All ten can be adopted at bootstrap as design documents without claiming their downstream work is complete.

## 3. Three storage planes

**Evidence plane, ordinarily Drive:** primary editions, authenticated web snapshots, edition identifiers, hashes, normalized text, deterministic chapter/paragraph maps, source alignments, and authorized reception/paratext captures.

**Working/build plane:** temporary extraction files, code execution logs, caches, unfinished analyses, search results, and transport packages. Existence does not confer authority.

**Git analytical plane:** accepted methods, public-safe scope/admission records, readings, analytical ledgers, monographs, models, specialist arguments, and current routing.

Store what an artifact means according to its actual responsibility, not whether it is raw or processed. Deterministic alignment stays evidence; an argument that the alignment demonstrates mitigation belongs in Git. Do not commit raw novels, bulk translations, explicit sexual excerpts involving children, page/media dumps, package ZIPs, credentials, or private receipts.

## 4. Proposed tree and activation

```text
series/mushoku-tensei/
  CURRENT_STATE_AND_CORPUS_MAP.md
  .repository/
    series-registry.json
  00 Frameworks and Methods/
    [the ten framework documents listed above]
  01 Source Lock and Inventory/
    MT_SOURCE_LOCK_AND_INVENTORY.md
  02 Sequential Readings/
    MT_V01_DEEP_READING.md
    [one actual completed or accurately partial reading per admitted volume]
  03 Longitudinal Ledgers/
    MT_CLAIMS_AND_REVISIONS_LEDGER.md
    MT_CHARACTER_STATE_AND_READINESS_LEDGER.md
    MT_RELATIONSHIP_AND_AGENCY_LEDGER.md
    MT_CHRONOLOGY_AND_KNOWLEDGE_LEDGER.md
    MT_NORMATIVE_FRAMING_LEDGER.md
    MT_FORM_THEMES_AND_WORLD_LEDGER.md
  04 Character Analysis/
    <verified-local-character-key>/
      CHARACTER_MONOGRAPH.md
      RECONSTRUCTION_MODEL.md
      EVIDENCE_INDEX.md
      [STATE_HISTORY.md only if independently useful]
  05 Checkpoint Syntheses/
    [bounded, frozen checkpoints when earned]
  06 Literary and Thematic Studies/
    [independently justified specialists]
  07 Textual History and Adaptation/
    [variant ledger, comparisons, and separately scoped adaptation work]
  08 Reception and Discourse/
    [discourse ledger, reception studies, and claim studies when activated]
  09 Full-Series Synthesis/
    [integrated arguments after their gates pass]
  10 Audits and Handoffs/
    MT_BOOTSTRAP_REPORT.md
    [real audits and significant handoffs only]
```

Only create files with a present responsibility. The future tree is a plan, not an instruction to populate empty character folders, fictional V01 readings, or full-series titles. A templates file stays in `00 Frameworks and Methods`, never in the sequential-reading directory as a disguised reading.

## 5. Required day-one infrastructure

Six longitudinal homes are justified by the stated project objectives. Initialize each with its responsibility, record format, update rule, source boundary, and a truthful statement that no narrative evidence has yet been admitted. This is not permission to fabricate example scene rows.

| Home | Owns | Does not own |
|---|---|---|
| Claims/revisions | Load-bearing analytical propositions, competing explanations, prospective tests, and revision history | Raw transcript or every incidental remark. |
| Character state/readiness | Character encounter/evidence coverage, state-change events, readiness by domain, and model routing | A second global registry or competing current operational models. |
| Relationship/agency | Directed relationships, independent aims, initiative, constraints, refusal, and repair | A romance score or an assumption of reciprocity. |
| Chronology/knowledge | Event order, uncertain dates/ages, who knows which propositions, and branch/version distinctions | A forced complete calendar or an invented mental-age equation. |
| Normative framing | Diagnostic evaluation records and longitudinal ethical comparisons | A clinical diagnosis or automatic endorsement verdict. |
| Form/themes/world | Motifs, prose/tone patterns, structural questions, and consequential world/institution observations | An undifferentiated plot recap or a final world encyclopedia. |

A combined home is intentional early on. Split a dimension only when independent retrieval, volume, or synthesis responsibility warrants it. Record exact transfer of ownership, preserve IDs, and leave routing pointers instead of duplicate live datasets.

Deferred infrastructure: a variant ledger starts with actual version comparison; a discourse ledger starts when claims/sampling are commissioned; an adaptation ledger starts with an approved medium-specific task. Their existence is not a prerequisite for an LN-only first volume.

## 6. Artifact identity and authority

The transport files were `draft_noncurrent` with no authority. This adopted set has the complete live authority quartet, accepted version/date/basis, and exact canonical homes. Templates remain explicitly non-literary artifacts after adoption. Distinguish canonical methodology from completed analysis.

A new-root routing descriptor needs a current-eligible entrypoint. That entrypoint can accurately describe a closed bootstrap project; a noncurrent draft cannot serve as a verified canonical entrypoint. Do not mark a draft `active_provisional` merely to satisfy a validator. Conversely, accepted operational state can be canonical while documenting substantial evidence gaps.

Preserve authoritative predecessors if conflicts are unresolved. Do not add false supersession links or reset an existing high-water mark. Archive terms and statuses come from the live repository, not from ad hoc uppercase alternatives.

## 7. Source-unit transaction and closure

A volume transaction is:

`entering freeze -> full declared reading -> close analysis -> targeted source checks -> ledger/model updates -> exit freeze -> semantic review -> durable persistence -> accurate publication state`

Each volume reading also owns two reader-facing orientation functions near its beginning. A **story synopsis of the present volume**, composed after complete inspection, tells the causal story in ordinary prose: situation, consequential decisions, relationship changes, reversals, ending, and the place of any interlude or extra. For V02 onward, a distinct **developments through the previous volume** section establishes the narrative situation *before* the new volume from already closed LN units, including consequential changes and unresolved questions. For V01, state that there is no earlier LN unit or omit the prior-volume section. The latter is prepared without opening the new source; the former must not be mistaken for the entering prospective freeze. Both route to the detailed coverage map and evidence IDs rather than duplicating the ledgers or replacing source inspection. Keep reported or uncertain events qualified and sensitive scenes non-graphic. This is a presentation amendment prompted by the V01 pilot's readability review; V01 already has a synopsis, no earlier unit needs backfill, and no new evidence home is created.

The unit is not closed because its essay exists. At closure all affected references and current state must agree. Record no-material-update findings without adding padding.

Maintain distinct progress variables: authorized range, candidate unit, drafted coverage, semantically closed coverage, last persisted/committed closure, branch publication, and integration to main. Never infer one from another. The unit's containing commit can be recorded by a later receipt or Git history; do not insert a fabricated self-referential commit hash into the artifact.

Under an explicitly authorized continuous run, the next volume may begin after the preceding complete transaction is safely persisted under the governing continuation policy. Publication tranches can cover several closed units, but a new push must follow the live sequence for source audit, housekeeping, and final exact-head validation. Do not postpone cumulative updates until tranche end.

## 8. Canonical ownership and non-duplication

The volume reading owns diagnostic evidence observations and source locators. Raw normalized text is not duplicated there. A ledger owns its specialized interpretation of linked observations. A character evidence index is a curated map back to those homes, not another transcript or a second observation numbering system.

The character-state ledger owns the chronology of observed changes. Optional character `STATE_HISTORY.md` is a focused view with links to those events, not an independent history. The reconstruction model owns operational rules; the monograph explains them and their literary significance without maintaining rival rule sets.

The central claims ledger owns shared claim revision. A discourse claim has its own reception identity and links to the analytical claims that test it. A specialist owns an extended argument, not a second current-state map. A checkpoint owns a historical bounded synthesis, not live routing.

When a cross-series comparison outgrows an MT-local explanatory aside, route it under an approved `studies/<slug>/` rather than creating a second Mushoku root or silently extending this project's scope.

## 9. Checkpoints and longitudinal review

Propose checkpoints after V05, V10, V15, V20, and V26, contingent on the actual authorized source lock. Label each checkpoint's cumulative scope clearly: a document written at V10 normally synthesizes **V01-V10**, not only V06-V10. Record the latest tranche separately.

Also review at semantic pivots, major new sources, source contradictions, and before mature synthesis. Administrative blocks are not predeclared narrative arcs.

A checkpoint must assess durable changes, failed predictions, unresolved alternatives, unrepresented characters, recurring formal patterns, evidence gaps, and model calibration. It should challenge whether the current framework is missing something the novels make important. Freeze its input boundary and do not silently revise it after later disclosures.

## 10. Reconstruction and specialist activation

Open a living model once repeated or uniquely diagnostic evidence supports a useful bounded response model. Do not require a full-series monograph before useful local reconstruction. Do require enough ordinary and relationship-conditioned behavior for any claimed domain of readiness.

Open a mature monograph when state transitions, evidence variety, contradiction, and explanatory depth warrant one. The source boundary can be partial. Popularity or number of mentions is not sufficient. Major characters should not be reduced to a stock persona or a moral label; secondary characters can remain explicitly thin.

Anticipated specialists include narrative voice/reader alignment; continuity, embodiment, and the second life; family and generational responsibility; intimacy and power; competence and social circumstances; world/institutional constraints; and recurrence, genre, and form. These are **possible responsibilities**, not assertions about what the series proves. Promote, merge, or drop them at checkpoints. Textual history and reception are distinct specialists once their sources are admitted.

## 11. Dependency graph and stage ownership

```text
Live governance + reconnaissance
  -> accepted methods/architecture + truthful entrypoint + source admission
  -> authorized sequential LN readings + synchronized ledgers
  -> checkpoint/evidence-gap review
       -> bounded models and character studies
       -> isolated eligible textual comparisons, when authorized
  -> frozen target-specific synthesis inputs
  -> character/relationship/literary/normative specialists
  -> cross-specialist contradiction and source check
  -> integrated literary synthesis for the declared boundary

Separately admitted textual/reception/adaptation lanes
  -> their own source inspections and claim studies
  -> lane-specific synthesis
  -> scoped cross-lane convergence, without rewriting LN-only freezes
```

Prefer the repository's hybrid workflow: fresh well-grounded cloud architecture; an adequate Work/Codex environment for sequential source work and persistence; fresh substantial synthesis against a frozen snapshot; and an authorized integrator for evidence completion and publication. Environment preferences are not proof of capability or grants of write authority.

Reasoning classes: inventories and locator checks `BOUNDED_STANDARD`; normal deep readings `SUBSTANTIVE_ANALYSIS`, escalating for difficult units; monographs, textual history, and discourse adjudication `DEEP_SYNTHESIS`; architecture and especially propagation-sensitive convergence may warrant `PREMIUM_QUALITY_FIRST`. Resolve actual model/effort from live policy and observed access, not a hard-coded product name.

One integrator owns shared ledgers and entrypoint changes. Parallel specialists receive distinct target paths and the same frozen input commit. They return proposed deltas rather than writing competing versions of shared state.

## 12. Gates and honest completion

| Gate | Required condition |
|---|---|
| Bootstrap | Root/branch identity resolved; adopted design and truthful status; declared source reconnaissance; required templates/infrastructure; no fabricated findings. |
| Sequential readiness | Current-eligible method/architecture and required protocols; usable next source; initialized required ledgers; explicit OPEN gate under live policy. |
| Run authorization | Current owner instruction supplies the actual operation/range and allowed writes. This is separate from readiness. |
| Unit closure | Full declared coverage, supported reading, synchronized changes, locators, freezes, and durable state. |
| Main-LN sequential completion | Every unit in the declared main-LN scope closed, with omissions resolved or explicit scope reduction authorized. |
| Specialist readiness | Adequate bounded sources, claim/state reconciliation, named targets, and material channel debts resolved or honestly scoped. |
| Full-series literary synthesis | Completion and role-gap audit; required specialists; cross-specialist convergence; declared continuity and source boundary. |
| Textual/reception completion | Separate scope-specific coverage and limits, not implied by LN completion. |
| Release | Semantic acceptance, applicable repository audit, exact publication state, and frozen manifest/entrypoint routing. |

A core LN literary synthesis need not wait for all optional adaptations or rare bonuses. A thesis about a particular rewrite cannot be closed without the relevant witnesses. A whole-project release that promises all lanes must satisfy them; rename or narrow the declared release rather than hiding omissions.

## 13. Amendments, revisions, and interruptions

Use `PRESERVE`, `STRENGTHEN`, `REVISE`, `DOWNGRADE`, `REJECT`, and `OPEN` for claim transitions. These are not artifact authority statuses. Record evidence, prior formulation, new formulation, and dependent homes.

Maintained documents receive targeted patches against verified current contents. Frozen prospective readings and checkpoints keep their historical interpretations; correct objective mistakes visibly and route later discoveries through revisions. Do not regenerate large ledgers from memory or a truncated excerpt.

A new analytical dimension justifies an architecture change when recurring evidence or independent retrieval demands it. State why existing homes are inadequate, which prior material needs backfill, and what will not be reread. Changes affecting a central premise require dependent specialists to be reviewed, not merely an appended disclaimer.

At interruption, preserve exact files, partial coverage, base/input commit, last closed unit, unresolved work, next permitted action, and access limitations. A long conversation is not the corpus. Use the handoff specification; never claim complete preservation of details that were not externalized.

## 14. Publication controls

Before staging or committing, the receiver must read the live `governance/policies/CHANGE_INTEGRATION_CHECKLIST.md` and classify change obligations. Use the stable series branch and exact-path staging. No force push, history rewrite, wildcard staging, or unauthorized main integration.

Housekeeping owns its five deterministic routing outputs. The character curation agent owns `characters/registry.jsonl` and `CHARACTER_ANALYSIS_INDEX.md`. Bootstrap frameworks and cast mentions do not justify character enrollment. Existing discovery references must remain valid; coordinate any necessary repair with the designated writer.

The bootstrap report distinguishes semantic adoption, local checks, branch publication, housekeeping, exact-head integration audit, and actual main integration. Never manufacture a successful test or commit. Passing repository checks does not certify literary conclusions.
