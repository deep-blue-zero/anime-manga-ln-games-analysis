---
title: Manga / Anime Project Initiation and Architecture Policy
artifact_id: MANGA_ANIME_PROJECT_INITIATION_AND_ARCHITECTURE_POLICY
artifact_type: project_initiation_architecture_policy
version: 1.3
status: canonical
generation: V1
scope: corpus-wide analytical project initiation and architecture governance
created: 2026-08-27
last_updated: 2026-08-27
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

- consult `MANGA_ANIME_DRIVE_INDEX.md`;
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

The exact key names may vary in mature projects, but the state must be recoverable without reconstructing it from conversation history.

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

## 3.8 Sequential analysis lock

Once Sections 3.1-3.7 are satisfied, the corpus map may record:

`SEQUENTIAL_ANALYSIS_LOCK = OPEN`

Before that point:

`SEQUENTIAL_ANALYSIS_LOCK = CLOSED`

This is an operational gate, not a claim about source completeness. Preliminary source auditing and architecture work can proceed while the lock is closed.

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

## v1.3 — 2026-08-27 — Administrative terminology hardening

- Reserved `status` for authority state in the initialization template and added `architecture_lifecycle: INITIAL` for lifecycle state.
- Preserved the corpus-wide minimum meaning of `episode bundle`; series architectures may accept a partial derivative for a bounded purpose but may not relabel it as a complete bundle.
- Replaced duplicated literal transport thresholds with routing to the episode-bundle specification's time-bounded provider snapshot.

