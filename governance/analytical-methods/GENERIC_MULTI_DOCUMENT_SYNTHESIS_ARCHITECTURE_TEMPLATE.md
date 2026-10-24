---
title: Generic Multi-Document Synthesis Architecture Template
artifact_id: GENERIC_MULTI_DOCUMENT_SYNTHESIS_ARCHITECTURE_TEMPLATE
artifact_type: generic_synthesis_architecture_template
artifact_role: reusable_corpus_level_architecture_template
version: "1.0"
status: canonical
scope: bootstrap template for a project's synthesis/corpus architecture in any medium
authority_scope: this_reusable_reference_only
adoption: opt_in
project_local_authority: false
created: 2026-10-24
maintainer: Claude + user
source_boundary: "Architectural reference only; no series findings or primary-source evidence"
do_not_use_as_current_authority: false
do_not_use_as_literary_evidence: true
canonical_home: governance/analytical-methods/GENERIC_MULTI_DOCUMENT_SYNTHESIS_ARCHITECTURE_TEMPLATE.md
drafted_against_commit: 6a3afaaf1bb61e0993db379ab4074c46e9ea98dd
supersedes: []
superseded_by: []
---

# Generic Multi-Document Synthesis Architecture Template

## Adoption and authority boundary

This artifact is a reusable, corpus-level template for writing a project's **synthesis/corpus architecture**: the governing document that says where accumulated knowledge goes. It is canonical only for this reference responsibility, and adoption is opt-in. It is not a repository policy, a project's architecture, a current-state entrypoint, or literary evidence.

1. Copying it does not satisfy the initiation policy's architecture requirement. A project satisfies that requirement with its own architecture, adapted from reconnaissance of its own source, exposed through its canonical entrypoint (initiation Sections 3.4–3.5).
2. Mature projects keep their architectures (initiation Section 10). This template is not grounds for normalizing them.
3. Every module below is conditional unless it implements a responsibility the [initiation policy](../source-policies/MANGA_ANIME_PROJECT_INITIATION_AND_ARCHITECTURE_POLICY.md) makes mandatory. Delete what the source does not earn (initiation Section 11).

The template follows the initiation policy's Minimum Semantic Contract (Section 5) in order, so a filled-in copy can be checked against it section by section. Section titles may change; the responsibilities may not disappear.

## How to use this template

1. Complete source reconnaissance first (initiation Section 3.2). An architecture designed before the medium, unit, languages, editions, and load-bearing channels are known will be wrong in predictable ways.
2. Choose the reference method for the medium (the [routing policy](../source-policies/MANGA_ANIME_MEDIUM_AND_INSPECTION_LANE_ROUTING_POLICY.md), Section 3) and adapt the project's analytical method alongside this architecture. The pair is designed together (initiation Section 4).
3. Copy Part I into `<SERIES>_SYNTHESIS_ARCHITECTURE.md` in the project's frameworks folder. Replace each bracketed prompt with project decisions. Remove guidance text.
4. Initialize only the day-one infrastructure the architecture names (Section 6 below).
5. Write the entrypoint (Section 20 below) and open the lock only when the compliance checklist (Part II) passes.

Notation: `<ANGLE>` marks a value to fill in; **Decide:** marks a question the architecture must answer.

---

# Part I: Architecture body

## 1. Front matter

```yaml
---
title: <Series> Synthesis Architecture
series: <stable-slug or series code>
artifact_type: synthesis_architecture
scope: <source boundary this architecture governs>
generation: <V1, V2, ...>
version: "1.0"
status: canonical
architecture_lifecycle: INITIAL
governing_method: <SERIES>_ANALYTICAL_METHOD.md
source_boundary: "<primary corpus and admitted supplements>"
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
---
```

## 2. Purpose, scope, and authority (contract 5.1)

State:

- the project and source boundary governed;
- the analytical generation, and whether a prior generation is superseded or retained as legacy;
- the governing method it pairs with;
- the corpus policies it sits under (initiation, archive authority, reasoning, topology, lane routing);
- the project's analytical purpose: full-series literary synthesis, character reconstruction, audiovisual analysis, or another program.

**Decide:** what questions must the finished corpus be able to answer, with traceable evidence? List them. Every later section should serve at least one.

## 3. Source model (contract 5.2)

Describe enough source topology to route analysis:

| Source class | Examples | Status | Conflict rule |
|---|---|---|---|
| Primary canon | <main volumes, episodes, chapters, routes> | In boundary | Governs |
| Side stories, extras, bonus chapters | <...> | <in / supplemental / excluded> | <how they rank> |
| Alternate editions or text histories | <web novel vs light novel, magazine vs tankobon, broadcast vs Blu-ray> | <...> | <which governs which claims> |
| Adaptations | <anime of a manga, manga of a novel> | <in / out> | <adaptation divergence is recorded, not harmonized> |
| Paratext | <afterwords, author comments, cast commentary> | <...> | <labeled supplementary evidence only> |

Medium prompts:

- **Novels and light novels**: language and edition precedence; illustrations as evidence; web-novel or revised-edition divergence.
- **Manga**: chapter versus volume edition; color pages; translation of lettering and sound effects.
- **Anime**: episode bundles under the [bundle specification](../source-policies/MANGA_ANIME_EPISODE_BUNDLE_SPECIFICATION.md); primary language; continuous-AV objects if the project adopts that lane.
- **Games**: routes, events, branch and variant identity, live-service release boundaries locked to exact inventories, the three current boundaries (source, analysis, reconstruction), and extracted-data witnesses, under the [generic game method](GENERIC_GAME_ANALYTICAL_METHOD.md).

**Decide:** which source types can conflict, and how each conflict is classified or escalated (Section 13 below).

## 4. Document set and layout

Name the canonical homes. A typical layout, to be trimmed:

```text
series/<slug>/
  CURRENT_STATE_AND_CORPUS_MAP.md        working entrypoint (Section 20)
  00 Frameworks and Methods/             method, this architecture, method family members
  01 Source and Scope/                   source inventory, source locks, locator conventions
  02 Sequential Readings/                one reading per source unit, plus frozen checkpoints
  03 Longitudinal Ledgers/               cumulative homes (Section 6)
  04 Specialist Synthesis/               specialist documents (Section 9)
  05 Character and Relationship Studies/ monographs, relationship studies, reconstruction (Section 8)
  06 Evidence and Indexes/               claim-revision ledger, locator and evidence matrices, crosswalks
  07 Full-Series Synthesis/              final integration
  08 Audits and Handoffs/                completion, role-gap, convergence and release audits; handoff receipts
  9x Legacy/                             superseded generations, retained as provenance
```

Mature projects number these folders differently after `03`; the roles are what recur. Do not create empty folders for symmetry: a folder appears with its first artifact.

Rules that mature architectures in this corpus share:

- **One primary home per question.** Each specialist or synthesis document states its governing question, its primary home for that question, and what it must not duplicate from other homes.
- **Working entrypoint versus reader entrypoint.** `CURRENT_STATE_AND_CORPUS_MAP.md` serves analysts while the project is active. A reader-facing README or corpus guide, if wanted, is written last, after synthesis.
- **Reading order differs from production order.** State both when they diverge.
- **Core versus apparatus.** Distinguish the reader-facing analytical core from supporting apparatus such as ledgers, matrices, audits, and receipts.

Use the repository naming grammar `<SERIES>_<SCOPE>_<ARTIFACT_ROLE>.md` (initiation Section 13). Keep checkpoints and frozen releases distinguishable by name from mutable files. Do not present a Drive folder tree as the project's layout; Drive is the evidence plane, not the analytical corpus.

**Decide:** which folders exist on day one, and which appear only when their first artifact does.

## 5. Sequential-reading contract (contract 5.3)

Define what a source-unit reading must contribute before it counts as architecturally complete:

- [ ] the deep-reading artifact, under the method's output structure;
- [ ] cumulative ledger updates, listed by ledger;
- [ ] new or revised claims entered in the claim-revision home;
- [ ] evidence locators in the declared grammar (Section 10);
- [ ] prediction-register adjudication, if the project keeps one;
- [ ] for reconciled lanes: the AV verification queue, or a statement that none is needed;
- [ ] source inventory and corpus-map advancement.

A reading whose prose is finished but whose required cumulative state was not advanced is incomplete.

## 6. Longitudinal infrastructure (contract 5.4)

List each cumulative home with its contract:

| Ledger | Purpose | Row unit | Update trigger | History model | Day one? |
|---|---|---|---|---|---|
| Character state | Time-indexed state per character | Character at unit N | Material change | Current rows plus history | <yes / deferred> |
| Relationship state | Directional relationship state | Pair or group at unit N | Material change | Current rows plus history | <...> |
| Claim revision | Claim transitions | Claim ID | Any transition | Append-only | <...> |
| Open questions and predictions | Prospective uncertainty and its later adjudication | Question or prediction ID | Raised or adjudicated | Append-only adjudications | <...> |
| <Earned ledger> | <...> | <...> | <...> | <...> | <...> |

Across this corpus:

- **Core, in nearly every architecture:** character state; directed relationship state (A toward B is not B toward A); claim revision with predictions and locators; voice, register, and address, where the source language makes it load-bearing; chronology and knowledge state, where the structure demands it.
- **Near-core, earned by most long works:** institutions and world state; ordinary life and everyday behavior; visual form.
- **Earned by particular sources:** musical dramaturgy; narrator or oddity ledgers; route and branch state; domain ledgers specific to a work's subject.

Apply the proportionality test (initiation Section 11): the dimension recurs, accumulates evidence independently, affects later interpretation, has no adequate existing home, and needs independent retrieval.

Ledger standards:

- one responsibility per ledger; do not stretch a narrow ledger to carry an unrelated dimension;
- visible chronology: every row says at which unit it became true;
- evidence-type labels on rows;
- contradictions recorded, not overwritten;
- a `NO CHANGE` row only when the absence of change is itself meaningful;
- per-character ledgers are retrieval maps into readings and evidence, not copies of them.

Initialize day-one ledgers before the first reading (initiation Section 3.6). Deferring them until after the pass is the most common source of retrospective reconstruction work.

## 7. Responsibility matrix (initiation Section 6)

Every recurring observation needs one of three destinations: a cumulative home, a direct specialist or final-synthesis responsibility, or explicitly local-only.

| Analytical dimension | Sequential capture? | Canonical cumulative home | Final analytical destination | Initialization state |
|---|---|---|---|---|
| <dimension> | <always / when present / if diagnostic> | <ledger or reading section> | <specialist or final synthesis> | initialized / deferred / N/A |

## 8. Character and relationship synthesis (contract 5.5)

State whether the project expects character monographs, relationship syntheses, ensemble syntheses, behavioral or voice models, reconstruction and validation artifacts, or no dedicated layer.

**Decide:** the conditions under which a character or relationship earns an independent home (for example, recurrence across a stated share of units, a distinct developmental arc, or a reconstruction target).

Monographs cite claims and locators, not whole readings. A monograph that links only to "see V3 reading" forces synthesis to reconstruct its evidence.

If reconstruction is in scope, adapt the [generic character reconstruction method](GENERIC_CHARACTER_RECONSTRUCTION_METHOD.md) and declare:

- **placement**: reconstruction is a derived-use layer that routes to the literary corpus. It is not a parallel canon and not the master interpretive layer;
- **timing**: evidence capture is prospective, during sequential reading; model building may run incrementally, mid-pipeline, or after literary release, as the dependency graph states;
- **artifact split**: per subject and state, an evidence ledger, an operational model, and (separately) any monograph. A monograph does not certify a model.

The project produces analysis and models. The reconstruction evaluator alone grades capability in `characters/reconstruction_capabilities.jsonl`; the architecture never assigns those grades.

## 9. Specialist synthesis (contract 5.6)

| Specialist domain | Status | Inputs | Trigger to begin |
|---|---|---|---|
| <domain> | mandatory / anticipated | <ledgers and readings> | <completion gate> |

Distinguish mandatory from anticipated specialists. Later discovery may add or remove them (Section 16 below).

## 10. Evidence routing and locators (contract 5.7)

Declare the locator grammar and where evidence trails live:

| Medium | Locator grammar example |
|---|---|
| Novel or light novel | `<SERIES> V03 Ch.4 p.112 ¶3` or an edition-stable equivalent |
| Manga | `<SERIES> Vol.5 Ch.38 p.12 panel 3` |
| Anime | `S01E24 00:12:41.200 cue 118, frame 000412_...jpg`, in the bundle's declared clock |
| Game | `<route or event ID> <scene or line ID>` |

Define locator levels so that each claim states how precisely it is anchored, for example:

| Level | Anchor |
|---|---|
| L1 | Exact: page and panel, paragraph, or calibrated timestamp with cue or frame |
| L2 | Scene or section within a unit |
| L3 | Unit only |
| L4 | Distributed pattern across units, with representative L1 instances |

Define the claim-routing chain: mature claim, then claim ID in the claim-revision ledger, then reading section, then locator, then source. Use stable heading anchors or IDs rather than line numbers, which drift.

**Decide:** where source-language quotations and translation notes live; where visual and audio observations live; when a dedicated evidence matrix is required. The goal is deterministic retrieval from mature claim to source basis, not duplication.

## 11. Claim revision and supersession (contract 5.8)

Use the transition vocabulary `PRESERVE`, `STRENGTHEN`, `REVISE`, `DOWNGRADE`, `REJECT`, `OPEN`. State where earlier formulations remain discoverable and which document becomes current authority after a revision. Frozen readings and checkpoints are corrected by errata or claim revision, never by editing their bytes.

## 12. Temporal, epistemic, and continuity state (contract 5.9)

State how the project avoids collapsing state across time. Distinguish, as the source requires: true at unit N versus true in the mature reading; character knowledge versus reader knowledge; stated belief versus inferred motive; pre-reveal versus post-reveal; route A versus route B; adaptation versus source continuity.

This section is mandatory even if the answer is "one linear continuity, low state complexity".

## 13. Contradiction handling (contract 5.10)

Name how apparent contradictions are classified rather than harmonized: textual revision, unreliable narration, character deception or ignorance, translation variance, side-story retrospection, adaptation or route divergence, performance changing the force of text, paratext conflict, or genuine inconsistency. State when a contradiction warrants an audit, a claim revision, or an `OPEN` state.

## 14. Dependency graph and integration order (contract 5.11)

A default order, to be adapted:

```text
source lock, method, architecture, day-one ledgers
  -> sequential readings (each a transaction that includes its ledger updates)
  -> checkpoint freezes at declared boundaries
  -> completion audit
  -> claim, evidence, and locator stabilization
  -> architecture / role-gap audit
  -> character monographs and relationship syntheses
  -> system and thematic specialists
  -> adversarial convergence and cross-specialist crosswalk
  -> source-language verification of load-bearing quotations
  -> full-series synthesis
  -> reconstruction and validation, if placed here
  -> reader-facing guide, release audit, and freeze
```

A useful stabilization gate: every major character has ordinary-scene evidence, not only crisis evidence, before monographs or models begin.

**Decide:** which specialists feed which; whether reconstruction precedes or follows literary integration; which audits gate release. Validation and synthesis must not be written before the cumulative and specialist layers they depend on; an audit that certifies against an incomplete role map has to be superseded.

## 15. Method family, lanes, and execution ownership

Name the method family (routing policy Section 6): the governing method; any AV-lane companion method; any reconciliation profile. For each stage, name the owner role and lane, not a provider:

| Stage | Owner role | Lane | Handoff |
|---|---|---|---|
| Framework and architecture design | <role> | <lane> | <packet> |
| Sequential readings and ledgers | <role> | <lane> | <...> |
| Continuous-AV review | <role> | `CONTINUOUS_AV` | Reconciliation protocol |
| Substantial synthesis | <role> | <lane> | Handoff contract |
| Repository integration | <role> | Not applicable | Checklist |

## 16. Extension, lifecycle, and review checkpoints (contract 5.12; initiation Sections 7–8)

Permit analytically justified evolution: a new ledger or specialist responsibility is added when a dimension recurs, accumulates evidence independently, affects later synthesis, cannot be represented in an existing home, or needs independent retrieval. Record changes in the architecture's revision history and the corpus map.

Track lifecycle (`INITIAL`, `EVOLVING`, `STABILIZED`, `FROZEN`) and name the review checkpoints: <end of first arc, end of season or volume tranche, discovery of a new source type, before specialist synthesis, before final integration, before release>.

At each checkpoint, run a role-gap audit: for every responsibility in this architecture, record one of `SATISFIED`, `PARTIALLY_SATISFIED`, `MISSING`, `MISROUTED`, `TOO_THIN`, or `NOT_APPLICABLE`, with the artifact that carries it and the repair route.

Keep these states distinct: an artifact exists; it is semantically accepted; it passes preflight; it is published on its branch; it is integrated on `main`. A file the entrypoint lists must exist and be accepted, not merely anticipated. A provisional file is never promoted by editing its front matter.

## 17. Completion gates (contract 5.13)

| Gate | Condition |
|---|---|
| Sequential completion | <all units in boundary read and their contracts met> |
| Longitudinal reconciliation | <ledgers current; open questions adjudicated or carried> |
| Specialist readiness | <role-gap audit passed> |
| Full-series synthesis readiness | <specialists converged> |
| Validation / audit | <named audits passed> |
| Frozen / release | <release audit; freeze recorded> |

Sequential completion does not authorize full-series synthesis by itself (initiation Section 9).

## 18. Reasoning classes (contract 5.14)

Assign stable classes from the [reasoning policy](../source-policies/MANGA_ANIME_REASONING_AND_MODEL_ROUTING_POLICY.md) to artifact roles whose workloads differ. Do not hard-code model names.

| Artifact role | Reasoning class |
|---|---|
| Sequential reading | `SUBSTANTIVE_ANALYSIS` |
| Ledger routing of established findings | `BOUNDED_STANDARD` |
| Specialist synthesis, monographs | `DEEP_SYNTHESIS` |
| Architecture design, full-series synthesis, contradiction matrices | `PREMIUM_QUALITY_FIRST` where justified |

## 19. Mutable and frozen state (contract 5.15)

List which files remain mutable (entrypoint, ledgers, current syntheses) and which freeze (checkpoints, completed releases, sealed sequential readings under a run stop). Superseded analysis moves to legacy or provenance; it does not disappear.

## 20. Entrypoint and retrieval route (contract 5.16; initiation Section 3.5)

Name `CURRENT_STATE_AND_CORPUS_MAP.md` (or the verified equivalent) as the first-read surface. It answers: where to start, what is current authority, what source boundary is complete, what operation is next, and what to read before changing state. Initialize it with:

```yaml
project_initialization:
  status: canonical
  architecture_lifecycle: INITIAL
  governing_method: <SERIES>_ANALYTICAL_METHOD.md
  synthesis_architecture: <SERIES>_SYNTHESIS_ARCHITECTURE.md
  method_status: canonical
  source_reconnaissance_complete: true
  required_ledgers_initialized: true
  sequential_analysis_lock: open
```

Use the key spellings the validator reads (initiation Section 3.8). Keep the entrypoint about the present; move dated history to a changelog beside it.

---

# Part II: Initialization checklist

Before the first substantive sequential reading, confirm (initiation Section 15):

- [ ] canonical root resolved; alias and prior-generation search done;
- [ ] reconnaissance sufficient for medium, unit, languages, editions, and load-bearing channels;
- [ ] project-local method exists, adapted from the relevant reference method;
- [ ] this architecture exists and every Part I responsibility is answered or explicitly marked N/A with a reason;
- [ ] responsibility matrix present;
- [ ] day-one ledgers initialized, and only those;
- [ ] source, conflict, and continuity rules explicit;
- [ ] extension rule and completion gates present;
- [ ] reasoning classes assigned;
- [ ] entrypoint written; lock recorded as open only after all of the above.

---

# Part III: Common architecture failures

Role-gap and integration audits in this corpus have found the following repeatedly. Treat each as a check.

1. **Architecture deferred to a scaffold.** Sequential reading began with only a placeholder architecture, so recurring dimensions had no homes until a late audit.
2. **Recurring observations with no cumulative home.** Character state, relationship state, claims, or voice recurred in every reading but lived only in reading prose (Section 7).
3. **Local claim IDs with no corpus-wide crosswalk.** Each reading numbered its own claims, and nothing recorded their later disposition (Section 11).
4. **Synthesis and validation before their inputs.** Specialist or validation documents were written before the cumulative and specialist layers they depended on (Section 14).
5. **Thin monographs.** Monographs linked to whole readings rather than to claims and locators (Section 8).
6. **Voice built from translation.** Voice and register models were built from English summaries rather than the source language.
7. **A narrow ledger stretched beyond its remit** to carry a dimension that needed its own home.
8. **Ledgers created for symmetry**, copied from another project, adding maintenance without retrieval value.
9. **State collapse.** Mature knowledge written back into early state, or character knowledge merged with reader knowledge (Section 12).
10. **Status drift.** Frozen files still labeled mutable; an entrypoint listing files that were never accepted; supersession links that are not reciprocal; line-number anchors that drifted.
11. **Compression on transfer.** A receiving session shortened mature analysis. Review transfers against the incoming text for lost substance; length alone is not a quality gate in either direction.

Hazards in architecture text itself:

- literal provider or model names as durable structure (use roles, lanes, and reasoning classes);
- a Drive folder tree presented as the current layout;
- "proposed" status labels left on a governing document;
- a private revision vocabulary instead of `PRESERVE` / `STRENGTHEN` / `REVISE` / `DOWNGRADE` / `REJECT` / `OPEN`;
- reconstruction positioned as the master interpretive layer, or any second canon parallel to the literary corpus.

---

# Repository context

- [Project initiation and architecture policy](../source-policies/MANGA_ANIME_PROJECT_INITIATION_AND_ARCHITECTURE_POLICY.md): the gate, the Minimum Semantic Contract, and the responsibility matrix this template implements.
- [Medium and inspection-lane routing policy](../source-policies/MANGA_ANIME_MEDIUM_AND_INSPECTION_LANE_ROUTING_POLICY.md): reference methods by medium and the method-family split.
- [Archive authority and supersession policy](../source-policies/ARCHIVE_AUTHORITY_AND_SUPERSESSION_POLICY.md): current versus historical authority.
- [Reasoning and model-routing policy](../source-policies/MANGA_ANIME_REASONING_AND_MODEL_ROUTING_POLICY.md): reasoning classes.
- [Character reconstruction maintenance policy](../policies/CHARACTER_RECONSTRUCTION_MAINTENANCE.md): the evaluator that grades reconstruction capability.
- [Change-integration checklist](../policies/CHANGE_INTEGRATION_CHECKLIST.md): authorized paths, validation, and publication.
