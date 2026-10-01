---
series: BLUE_ARCHIVE
artifact_type: synthesis_architecture
scope: Analytical corpus architecture for Japanese-primary Blue Archive interpretation
generation: V1
version: "1.9"
status: canonical
source_boundary: "Designed at the historical V1 witness cbe3fd623c2aab9e781ba0ce0483bc77c68bff86; current production boundary is all 480 canonical main units in electricgoat/ba-data@jp a038020f1f5ac02dcfe76962426d38f86414cdd8, generation BA_REFRESH_20260928T032248159554Z; 180 supplemental objects admitted with limits in Phase2 cycles001–005"
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
created: 2026-08-15
updated: 2026-10-01
---

# BLUE ARCHIVE SYNTHESIS ARCHITECTURE V1
## Canonical analytical responsibilities, document topology, ledgers, and release strategy

## 0. Architectural objective

This architecture converts the extracted Japanese Blue Archive corpus into a durable analytical project without duplicating the source pipeline or flattening a live-service work into one enormous synthesis.

The project uses one canonical analytical root and one canonical source/ingestion root.

**Analytical root:** `Blue Archive` under the Manga / Anime analytical hierarchy.\
**Source/ingestion root:** the existing `Blue_Archive` extraction mirror containing `blue-archive-corpus-pipeline/corpus`.

The two roots have different responsibilities:

- **source root** — raw upstream snapshots, promoted canonical story/data objects, structured data, character/relationship/institution/Sensei projections, LLM ingest, audits;
- **analytical root** — methods, sequential readings, cumulative ledgers, specialist interpretation, full/current-era synthesis, evidence indexes, manifests, and legacy analytical generations.

Do not duplicate the full transcript corpus into the analytical root. Analytical artifacts should link back to it through stable IDs and Drive routes.

### Authority direction, derived use, and feedback control

The complete analytical and reconstruction stack is:

```text
canonical Japanese source
  -> sequential deep reading
  -> longitudinal ledgers
  -> checkpoint and literary specialist synthesis
  -> character reconstruction model
  -> model validation record
  -> optional hypothetical application
```

Each step downward is more derived. A reconstruction model may compile accepted literary and ledger authority into conditional rules, but it does not replace the monograph, checkpoint, or source-facing reading. A hypothetical scene, generated line, crossover, or other model output can never become upstream evidence.

If hypothetical use exposes a weakness, reopen the canonical evidence and revise the artifact that owns the affected responsibility. Do not cite the generated output as proof. Literary interpretation and operational reconstruction can challenge one another, but corrections flow through evidence rather than circular inference.

## Source-projection versus analytical-artifact boundary

The promoted source corpus contains a derived layer. The quantitative examples below describe the historical V1 build; current inventory and admission state are routed through the [coverage index](../06%20Evidence%20and%20Indexes/BLUE_ARCHIVE_CHARACTER_ANALYTICAL_COVERAGE_INDEX.md) and [source reconciliation](../01%20Source%20Lock%20and%20Inventory/BLUE_ARCHIVE_SOURCE_RECONCILIATION_20260928.md). Preserve the following semantic separation:

| Source/ingestion artifact | What it does | Analytical counterpart |
|---|---|---|
| `04_CHARACTER_BUNDLES/<person>/` | gathers contextual scenes, dialogue, MomoTalk, variant, linguistic, relationship, and manifest evidence | character monograph / character-state ledger |
| `05_RELATIONSHIP_BUNDLES/BA_RELATIONSHIP_*` | gathers complete scenes for machine-selected co-occurring pairs | adjudicated relationship synthesis / relationship-state ledger |
| `RELATIONSHIP_CANDIDATES.csv` | measures 2,718 pairs by corpus features | relationship analytical-priority decision, not a direct copy of the ranking |
| `06_CLUB_AND_SCHOOL_BUNDLES/` | gathers master-data-backed institutional evidence | institutional synthesis / institution ledger |
| `07_SENSEI_RELATIONSHIP_BUNDLES/` | gathers student-Sensei evidence | Sensei relational analysis and ethics ledger |
| `08_LLM_INGEST/*.jsonl` | reversible retrieval chunks | never a terminal literary authority; route back to canonical scenes |

Do not promote source-side bundle names directly into analytical authority. In particular, a `BA_RELATIONSHIP_A__B.md` source file is an **evidence bundle**, not a completed relationship analysis.

---

# 1. Canonical analytical root

Use:

```text
Blue Archive/
  CURRENT_STATE_AND_CORPUS_MAP.md
  00 Frameworks and Methods/
  01 Source Lock and Inventory/
  02 Sequential Readings/
  03 Longitudinal Ledgers/
  04 Specialist Synthesis/
  05 Full-Series Synthesis/
  06 Evidence and Indexes/
  08 Audits and Manifests/
```

Do not create `07 Current Release` or `90 Legacy and Superseded` until there is actual content requiring those semantic homes.

This follows the global archive standard without manufacturing empty directories for symmetry.

---

# 2. `CURRENT_STATE_AND_CORPUS_MAP.md`

This is the mandatory first-read artifact while the project remains active.

It must answer:

- What is the current extraction generation?
- What upstream commits are locked?
- Has the extraction been bulk-promoted or is it still inspection-only?
- Which source classes are safe to analyze?
- What main-story range has been sequentially read?
- Which ledgers exist?
- Which specialist documents are current authority?
- What is the latest synthesis generation?
- What source gaps materially affect interpretation?
- What should the next analyst do?

Update this file in place whenever project state materially changes.

---

# 3. `00 Frameworks and Methods`

Canonical files:

```text
BLUE_ARCHIVE_ANALYTICAL_METHOD_V1.md
BLUE_ARCHIVE_SYNTHESIS_ARCHITECTURE_V1.md
BLUE_ARCHIVE_CHARACTER_RECONSTRUCTION_SPEC_V1.md
```

The analytical method governs source interpretation and sequential capture. The synthesis architecture governs artifact ownership and dependency order. The reconstruction specification governs the narrower derived-use model, readiness, scenario, and validation contracts. None substitutes for the others.

Possible future additions only when needed:

```text
BLUE_ARCHIVE_SOURCE_CLASS_AND_CONTINUITY_POLICY.md
BLUE_ARCHIVE_JAPANESE_LANGUAGE_ANALYSIS_PROTOCOL.md
BLUE_ARCHIVE_EVENT_CANON_AND_CONTINUITY_POLICY.md
```

Do not create these separate files until repeated work demonstrates that the method document is insufficient.

---

# 4. `01 Source Lock and Inventory`

This directory does **not** duplicate the pipeline's raw-data tree.

It contains analytical-side snapshots and routing artifacts such as:

```text
BLUE_ARCHIVE_SOURCE_LOCK_V1.md
BLUE_ARCHIVE_ANALYTICAL_SOURCE_INVENTORY.md
BLUE_ARCHIVE_SOURCE_GAP_IMPACT_REGISTER.md
```

The source lock should record:

- primary and reference commit IDs;
- game-data version;
- source root Drive ID/URL;
- current corpus generation/state;
- current coverage counts;
- unresolved speakers/person mappings;
- known missing main/group source units;
- parser ambiguities that affect literary reading;
- hash/manifest references in the extraction corpus.

The gap-impact register differs from the technical `KNOWN_GAPS.md`: it records **what a gap prevents us from claiming analytically**.

---

# 5. `02 Sequential Readings`

The main story is the spine of the literary analysis.

Recommended hierarchy:

```text
02 Sequential Readings/
  MAIN/
    <arc directories only when needed>/
      BLUE_ARCHIVE_<MAIN_SCOPE>_DEEP_READING.md
  EVENTS/
    CORE_CONTINUITY/
      BLUE_ARCHIVE_<EVENT_SCOPE>_DEEP_READING.md
```

Do not automatically turn an extraction inventory into one analytical file per event script group. The 492 recoverable groups were a historical V1 inventory, not a current analytical worklist. Events should first be triaged for continuity importance.

## 5.1 Main-story scope notation

Use a stable sortable scope derived from the corpus map rather than inventing English arc names prematurely.

Preferred examples once source metadata is stable:

```text
BLUE_ARCHIVE_MAIN_V01_C01_E01_DEEP_READING.md
BLUE_ARCHIVE_MAIN_V01_C01_E02_DEEP_READING.md
```

If the canonical source map provides another stable volume/chapter/episode grammar, follow it consistently.

## 5.2 Reading granularity

Default to one recoverable literary episode per deep reading when the episode is substantial.

Combine adjacent tiny units only if:

- they are structurally one scene sequence;
- separate files would add retrieval noise;
- source locators remain individually preserved.

Do not split a coherent episode merely to produce more artifacts.

## 5.3 Event triage

Maintain an event-priority index before creating many event analyses:

```text
BLUE_ARCHIVE_EVENT_ANALYTICAL_PRIORITY_INDEX.md
```

Use the [event analytical priority index](../06%20Evidence%20and%20Indexes/BLUE_ARCHIVE_EVENT_ANALYTICAL_PRIORITY_INDEX.md) for every event object's inventory route and for package-level review intake. Keep three dimensions separate:

- **Analytical priority after complete reading:** `CORE`, `HIGH`, `SUPPORTING`, or `UNASSESSED`. `CORE` means omission materially weakens a character, relationship, institution, continuity account **or the ordinary repertoire needed to interpret it**. `UNASSESSED` is not a low score.
- **Evidence function:** continuity/state, peer or Sensei relationship, institution/work, ordinary pleasure/routine/play, written voice/humor, contrary case, or chronology/identity. The former `LOW-STAKES / VOICE` label belongs here; it never means low analytical value.
- **Workflow:** inventory, intake candidate, reviewed, admitted, or deferred with a claim-specific reason and revisit trigger. `UNRESOLVED` marks an identity, chronology, provenance or source-class question, not a value rank.

Decide priority by literary characterization, underrepresented social contexts, recurrence or difference, interpretive consequences, and continuity needs. A quiet group, food, leisure or comic story may be `CORE` even with no plot-state change. Never defer a story solely for low stakes, seasonality, comedy or weak connection to the main plot. Keep every event story ID visible until inspected, including episodes inside a selected package. Metadata and person IDs can prompt intake but cannot establish story content, priority, chronology or admission. Read selected complete source sequences and preserve ordinary life, pleasure, humor, play, minor disputes and contrary evidence alongside crisis material. The [source-class crosswalk](../06%20Evidence%20and%20Indexes/BLUE_ARCHIVE_SOURCE_CLASS_CROSSWALK.md) governs provenance and chronology; the [gap-impact register](../01%20Source%20Lock%20and%20Inventory/BLUE_ARCHIVE_SOURCE_GAP_IMPACT_REGISTER.md) records the claims affected by what remains unread or unprinted.

---

# 6. `03 Longitudinal Ledgers`

Blue Archive's scale makes cumulative ledgers essential. Without them, later synthesis will overfit whichever arc was read most recently.

Start with a small number of durable ledgers, not one file per concept.

Recommended initial set:

```text
BLUE_ARCHIVE_CHARACTER_STATE_LEDGER.md
BLUE_ARCHIVE_RELATIONSHIP_STATE_LEDGER.md
BLUE_ARCHIVE_SCHOOL_CLUB_INSTITUTION_LEDGER.md
BLUE_ARCHIVE_SENSEI_ROLE_AND_ETHICS_LEDGER.md
BLUE_ARCHIVE_JAPANESE_VOICE_AND_ADDRESS_LEDGER.md
BLUE_ARCHIVE_MOTIF_THEME_AND_CALLBACK_LEDGER.md
BLUE_ARCHIVE_CLAIM_REVISION_LEDGER.md
```

## 6.1 Character-state ledger

Track only material changes:

- self-concept;
- goal;
- wound/fear;
- institutional role;
- major relationship state;
- post-crisis afterstate;
- source locator;
- confidence.

Do not turn it into a second character encyclopedia.

## 6.2 Relationship-state ledger

Track relationships that accumulate actual narrative weight. Use stable pair or ensemble IDs and include:

- current state;
- last material transition;
- evidence source;
- unresolved tension;
- whether a dedicated monograph exists.

## 6.3 Institution ledger

Track schools, clubs, Schale, councils, committees, and recurring political/administrative bodies.

Fields should include:

- formal function;
- practical power;
- leadership;
- internal factions;
- allies/adversaries;
- current crisis state;
- major legitimacy questions.

## 6.4 Sensei ledger

Because Sensei appears across almost every relational layer, maintain a dedicated cumulative ledger for:

- structural actions;
- choice-space tendencies;
- adult responsibility;
- uses/refusals of authority;
- risk acceptance;
- recurring ethical commitments;
- student-specific relational differences.

## 6.5 Claim-revision ledger

Use:

**PRESERVE · STRENGTHEN · REVISE · DOWNGRADE · REJECT · OPEN**

Suggested schema:

| Claim ID | Earlier claim | Status | Current formulation | Authority | Evidence route |
|---|---|---|---|---|---|

---

# 7. `04 Specialist Synthesis`

Specialist documents should exist only when they have a distinct analytical responsibility and enough evidence density to justify independent retrieval.

Recommended families are below. These are **categories, not mandatory empty folders**.

## 7.1 Character monographs

Naming:

```text
BLUE_ARCHIVE_HINA_CHARACTER_MONOGRAPH.md
BLUE_ARCHIVE_HOSHINO_CHARACTER_MONOGRAPH.md
```

A monograph should synthesize all relevant source classes but retain source-type labels.

Required sections:

- core thesis;
- longitudinal arc;
- public/private self;
- school/club role;
- ordinary life;
- crisis behavior;
- Sensei relationship;
- major peer relationships;
- language/voice;
- competing readings;
- evidence route.

A mature monograph owns the literary and psychological argument: development, causality, self-report versus action, narrative function, relationships, language, contradictions, and interpretive disputes. It may explain an accepted reconstruction mechanism and link rule IDs, but it must not maintain a competing operational rule set.

## 7.2 Relationship syntheses

Examples:

```text
BLUE_ARCHIVE_<A>_<B>_RELATIONSHIP_SYNTHESIS.md
BLUE_ARCHIVE_<ENSEMBLE>_RELATIONSHIP_SYNTHESIS.md
```

Create only for narratively significant relationships.

## 7.3 School / institutional syntheses

Examples:

```text
BLUE_ARCHIVE_ABYDOS_INSTITUTIONAL_SYNTHESIS.md
BLUE_ARCHIVE_GE HENNA...  # use verified canonical romanization before creating
```

Do not guess canonical ASCII spellings. If romanization is uncertain, use a verified project identifier or delay file creation.

Institutional synthesis should distinguish school mythology from actual governance.

## 7.4 Sensei synthesis

A mature project should eventually include:

```text
BLUE_ARCHIVE_SENSEI_CHARACTER_ETHICS_AND_INSTITUTIONAL_ROLE.md
```

This should be written later than the first few arcs because early overgeneralization from player choices is especially risky.

## 7.5 Japanese language and social register

Once enough characters have been read:

```text
BLUE_ARCHIVE_JAPANESE_VOICE_REGISTER_ADDRESS_AND_RELATIONAL_LANGUAGE.md
```

This document should compare stable speech patterns across schools, roles, intimacy levels, and crisis states.

## 7.6 Thematic / philosophical syntheses

Likely long-term responsibilities include:

- adulthood, childhood, and authority;
- education and institutional legitimacy;
- violence, protection, and normalized militarization;
- memory, grief, sacrifice, and recurrence;
- freedom, responsibility, and rescue;
- school identity and political pluralism;
- comedy/absurdity versus tragedy;
- Sensei as adult counter-institution.

Do not pre-create one file for each hypothesis. Let recurring evidence earn its own topical home.

## 7.7 Character reconstruction models

Reconstruction models are derived-use specialist artifacts with a distinct responsibility from literary monographs. Their canonical home is:

```text
04 Specialist Synthesis/Character Reconstruction/
  BLUE_ARCHIVE_<STABLE_CHARACTER_KEY>_RECONSTRUCTION_MODEL.md
```

Do not create the directory or a model to complete a roster. A model is warranted only when the coverage index and a bootstrap/promotion audit show enough time-bounded evidence for conditional behavioral rules.

Every model must declare:

- character/continuity identity and exact source state;
- literary, checkpoint, ledger, locator, and audit dependencies;
- temporal states and change causes;
- attention, appraisal, motives, inhibition/escalation, choice, action, and aftermath;
- directed relationship and institutional conditioning;
- ordinary-life and crisis contrast;
- Japanese written-speech constraints, separate from any performed-voice layer;
- counterevidence, negative constraints, gaps, and abstention conditions;
- project-local readiness and validation status;
- a counterfactual scenario envelope.

The detailed contract is `BLUE_ARCHIVE_CHARACTER_RECONSTRUCTION_SPEC_V1.md`. A model is operational authority only inside its declared state/domain envelope. It is never primary literary authority.

---

# 8. `05 Full-Series Synthesis`

Because *Blue Archive* remains a live-service work, the preferred artifact is initially a **current-era synthesis**, not a falsely final full-series synthesis.

Naming:

```text
BLUE_ARCHIVE_CURRENT_ERA_SYNTHESIS_<BOUNDARY>.md
```

When the project reaches a sufficiently stable or deliberately frozen boundary, a broader artifact may become:

```text
BLUE_ARCHIVE_FULL_SERIES_SYNTHESIS.md
```

The synthesis should not merely concatenate character monographs. Its responsibility is to answer:

- What kind of story is Blue Archive?
- What does Kivotos structurally represent?
- What is Sensei's function?
- How do schools and clubs distribute identity and authority?
- What does the work believe adults owe children?
- How does violence coexist with comedy and ordinary school life?
- How do grief, memory, sacrifice, miracle, and recurrence operate?
- What counts as legitimate authority?
- How does the work reconcile individual character intimacy with institutional-scale crisis?

A mature synthesis should route its major claims into specialist and sequential evidence rather than becoming its own untraceable authority.

---

# 9. `06 Evidence and Indexes`

This directory provides analytical retrieval infrastructure, not duplicated transcripts.

Recommended artifacts:

```text
BLUE_ARCHIVE_ANALYTICAL_LOCATOR_INDEX.md
BLUE_ARCHIVE_MAIN_STORY_TO_ANALYSIS_CROSSWALK.csv
BLUE_ARCHIVE_EVENT_ANALYTICAL_PRIORITY_INDEX.md
BLUE_ARCHIVE_CHARACTER_ANALYTICAL_COVERAGE_INDEX.md
BLUE_ARCHIVE_RELATIONSHIP_ANALYTICAL_COVERAGE_INDEX.md
BLUE_ARCHIVE_SOURCE_CLASS_CROSSWALK.md
```

The locator index should map mature claims and analytical artifacts back to stable corpus IDs.

The character coverage index should answer:

- main-story coverage read?;
- group/event coverage triaged?;
- bond coverage read?;
- MomoTalk read?;
- character-data inspected?;
- monograph status?;
- known source gaps?;
- current authority.

`BLUE_ARCHIVE_CHARACTER_ANALYTICAL_COVERAGE_INDEX.md` additionally owns project-local behavioral/reconstruction coverage and readiness. It must distinguish source availability from analyzed evidence, model artifact existence from distributed partial mechanisms, and domain readiness from whole-character claims. It does not create global character or capability records.

---

# 10. `08 Audits and Manifests`

Use for analytical-side audits such as:

```text
BLUE_ARCHIVE_ANALYTICAL_CORPUS_MANIFEST.md
BLUE_ARCHIVE_SOURCE_TO_ANALYSIS_COVERAGE_AUDIT.md
BLUE_ARCHIVE_LOCATOR_INTEGRITY_AUDIT.md
BLUE_ARCHIVE_DUPLICATION_AND_RESPONSIBILITY_AUDIT.md
BLUE_ARCHIVE_RELEASE_MANIFEST.md
```

Character reconstruction audits and future prediction/adjudication records also live here, for example:

```text
BLUE_ARCHIVE_CHARACTER_RECONSTRUCTION_BOOTSTRAP_AUDIT.md
BLUE_ARCHIVE_CHARACTER_MODEL_PROSPECTIVE_REGISTER_<BOUNDARY>.md
BLUE_ARCHIVE_CHARACTER_MODEL_ADJUDICATION_<BOUNDARY>.md
```

The bootstrap audit evaluates architecture and evidence readiness. A prospective register freezes exact rules before later source exposure. An adjudication record preserves the frozen wording and scores only fair diagnostic opportunities. These responsibilities must not be collapsed into a model's current prose.

Do not duplicate technical parser audits already authoritative in the extraction corpus. Link to them and add only the interpretive impact.

---

# 11. Phase architecture

## Phase 0 — Extraction readiness and analytical source lock

Inputs:

- pipeline specification;
- extraction `CURRENT_STATE_AND_CORPUS_MAP.md`;
- source/coverage report;
- known gaps;
- person/variant/speaker registries;
- canonical inspection samples.

Outputs:

- analytical method;
- synthesis architecture;
- analytical current-state map;
- source lock snapshot.

Exit condition:

> bulk canonical corpus has passed parser/choice/provenance review and has been promoted beyond inspection samples.

**Historical V1 promotion status: COMPLETE.** The V1 canonical build reports `PASS` with 2,716 canonical story/data objects, 2,047 scenes, 102,665 utterances, 8,774 preserved choice groups, 12,821 MomoTalk messages, and 7,089 character contextual lines. The derived build also reports `PASS` and provides the retrieval projections required for Phase 1 and later contextualization.

## Phase 1 — Main story pass

Read main story sequentially.

Outputs:

- deep readings;
- character/institution/Sensei ledger deltas;
- arc checkpoints.

Supplemental layers are consulted only when required to resolve source identity or when the governing reading plan explicitly backfills them after an arc.

**Current snapshot status: COMPLETE, 480 / 480 main units.** The last completed backfill checkpoint is `MAIN_V001_C003` through `BA:main:001:003:043`; the latest forward checkpoint is `MAIN_S2_V003_C001` through `BA:main:series2:003:001:014`. No main unit remains unopened in the audited snapshot. This completes the main-story pass at that boundary, while contextualization and reconstruction readiness remain separate gates.

## Phase 2 — Arc contextualization

After each major main-story arc:

- identify core related group stories;
- classify events by importance;
- read relevant bond/MomoTalk for major characters;
- inspect character-data voice for linguistic baseline;
- update ledgers.

This phase turns a plot reading into a social-world reading.

**Current status: IN PROGRESS.** [Cycle005](../02%20Sequential%20Readings/BLUE_ARCHIVE_PHASE2_CONTEXTUALIZATION_CYCLE_005_CHECKPOINT.md) brings scoped admission to180 objects:65 group,43 event,30 bond,30 full MomoTalk and12 character_data, all with limits. All65 group objects have complete accepted readings; the [group/arc relevance audit](../08%20Audits%20and%20Manifests/BLUE_ARCHIVE_PHASE2_GROUP_ARC_RELEVANCE_AUDIT.md) closes P2-R01 with limits. The [Phase2 acceptance audit](../08%20Audits%20and%20Manifests/BLUE_ARCHIVE_PHASE2_CONTEXTUALIZATION_AUDIT.md) owns all12 incomplete arc duties and the remaining8 requirements; [scope extension001](../08%20Audits%20and%20Manifests/BLUE_ARCHIVE_PHASE2_PRINCIPAL_SCOPE_EXTENSION_001.md) defines125 retrieval families/128 raw keys and3631 mandatory/3682 tracked objects. The [object crosswalk](../06%20Evidence%20and%20Indexes/BLUE_ARCHIVE_SUPPLEMENTAL_SOURCE_TO_ANALYSIS_CROSSWALK.csv) owns exact states, with3451 mandatory/3502 tracked objects still unaccepted. Ordinary pleasure has intrinsic value; priority determines review order. Group-duty acceptance or a successful pilot does not complete an arc.

## Phase 3 — Character / relationship / institution packages

Generate monographs only after enough material exists.

Suggested first prototypes, after the relevant main-story and contextual material has actually been read, should deliberately vary structure, for example:

- one major character with extensive main-story and institutional presence;
- one character with rich bond/MomoTalk/private material;
- one character whose playable variants complicate identity or chronology.

Do not lock specific names until coverage audits confirm the best prototypes.

## Phase 4 — Cross-arc specialist synthesis

Write only the specialist documents justified by repeated evidence across several arcs.

## Phase 5 — Current-era synthesis

Integrate the stable corpus up to an explicit source boundary.

## Phase 6 — Frozen release

Once a release is declared frozen:

- create `07 Current Release`;
- package the analytical artifacts and manifests;
- freeze them;
- route later changes through a new version;
- create `90 Legacy and Superseded` only when earlier materially distinct analysis must be preserved.

---

# 12. Current production sequence

The [source reconciliation](../01%20Source%20Lock%20and%20Inventory/BLUE_ARCHIVE_SOURCE_RECONCILIATION_20260928.md) fixes the current production boundary at `electricgoat/ba-data@jp a038020f1f5ac02dcfe76962426d38f86414cdd8`: **480 / 480** main units read, including `MAIN_V001_C003` E001–E043 backfill, with the latest forward unit `BA:main:series2:003:001:014`. No main unit remains unopened within that snapshot. The current sequence is:

1. retain the source-facing readings, chapter checkpoints, and seven cumulative ledgers with their local information boundaries; choose the checkpoint appropriate to the subject and story state rather than treating the last backfill as a universal chronological endpoint;
2. use the [coverage index](../06%20Evidence%20and%20Indexes/BLUE_ARCHIVE_CHARACTER_ANALYTICAL_COVERAGE_INDEX.md) and [bootstrap audit](../08%20Audits%20and%20Manifests/BLUE_ARCHIVE_CHARACTER_RECONSTRUCTION_BOOTSTRAP_AUDIT.md) and its linked contextual companion for current evidence readiness and any bounded pilot recommendation;
3. use the materialized event-priority index, source-class crosswalk, and source-gap impact register to select complete supplemental story sequences by character, relationship, institution and ordinary-life questions; verify source class, chronology, relevance, and claim-specific gap effects before admitting selected group, event, bond/MomoTalk, or character-data sources;
4. preserve the earlier checkpoint `DEFER` decisions as history; cycles001–005's180 supplemental objects have scoped admission; all other side sources require their own reasoned decision naming exact sources, question and limits;
5. create a monograph or standalone reconstruction pilot only when its distinct evidence, state/domain, and responsibility gates pass; full main-story coverage alone does not certify readiness;
6. freeze any intended prospective test before genuinely unexposed diagnostic source material is opened; comparisons against the completed main corpus are retrospective and must retain known prior exposure;
7. continue method §10.5 for later chapter checkpoints and update affected coverage/readiness rows, preserving previous bases, counterevidence, failed tests, and promotion or demotion reasons;
8. recheck released-source provenance and the canonical inventory before extending the main-story boundary.

No character model, prediction register, or empty model directory is required merely for symmetry.

## Historical C002 production sequence — 2026-09-25

The source-promotion milestone, Prologue checkpoint, and Volume 1 Chapters 1–2 checkpoints had passed. At that design boundary, `MAIN_V001_C002` represented **42 / 310** main units. The following instructions preserve the earlier production gate and its exposure discipline; they no longer describe the live reading frontier:

1. retain all three historical checkpoints and the recovered twenty C002 readings; use the C002 checkpoint as the current Volume 1 synthesis authority;
2. maintain the seven cumulative ledgers through `BA:main:001:002:020` without overwriting unit-local uncertainty;
3. use the canonical reconstruction specification, coverage index, and bootstrap audit as the operational architecture;
4. preserve the Chapter 2 contextual-backfill decision `DEFER`;
5. stop before `BA:main:002:001:001`; this architecture task does not authorize opening it;
6. on a later authorized sequential run, freeze any intended prospective tests before diagnostic source exposure, then perform literary reading and concise diagnostic behavioral deltas;
7. at every chapter checkpoint, apply method §10.5: new contexts, state changes, strengthened/narrowed/contradicted rules, directed conditions, ordinary-life and negative evidence, frozen-test outcomes, and readiness increases **and decreases**;
8. update material coverage/readiness changes in the index, preserving the previous basis and rationale;
9. admit side sources only through a reasoned source/chronology gate, never to fill a table;
10. create a monograph or standalone model only when its distinct evidence and responsibility gate passes.

The then-forthcoming Chapters 3–8 capture contract changed what the run recorded, not its canonical reading order. Chapter numbers in that planning phrase do not replace the crosswalk's volume/chapter IDs. No character model, prediction register, or empty model directory is required merely for symmetry.

---

# 13. Naming and metadata rules

Use stable uppercase ASCII series identifier:

`BLUE_ARCHIVE`

Preferred filenames:

`BLUE_ARCHIVE_<SCOPE>_<ARTIFACT_ROLE>.md`

Examples:

```text
BLUE_ARCHIVE_MAIN_V01_C01_E01_DEEP_READING.md
BLUE_ARCHIVE_CHARACTER_STATE_LEDGER.md
BLUE_ARCHIVE_HINA_CHARACTER_MONOGRAPH.md
BLUE_ARCHIVE_ABYDOS_INSTITUTIONAL_SYNTHESIS.md
BLUE_ARCHIVE_FULL_SERIES_SYNTHESIS.md
```

Every new Markdown analytical artifact should normally contain YAML front matter with:

```yaml
series: BLUE_ARCHIVE
artifact_type: deep_reading
scope: MAIN_V01_C01_E01
generation: V1
status: canonical
source_boundary: "..."
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
```

Authority states:

- `canonical`
- `active_provisional`
- `superseded`
- `historical_legacy`

---

# 14. Semantic responsibility test before creating a file

Before creating any new analytical artifact, ask:

1. Does a canonical topical home already exist?
2. Is this insight better added to a ledger, monograph, checkpoint, or synthesis?
3. Will this file be independently retrieved later?
4. Does it represent a recurring analytical dimension rather than one clever observation?
5. Can its source boundary and authority state be stated clearly?

If not, do not create the file.

---

# 15. Architecture-specific cautions for this corpus

## 15.1 Do not mirror the pipeline's generated bundles into analysis

The extraction tree already reserves:

- character bundles;
- relationship bundles;
- club/school bundles;
- Sensei bundles;
- LLM ingest.

Those are **source projections**, not analytical monographs. Keep them in the ingestion root. Analytical artifacts cite and interpret them.

## 15.2 Do not let `04_CHARACTER_BUNDLES` dictate the analysis tree

The existence of one generated package per literary person does not imply one analytical monograph per person. Many minor characters may never require a standalone synthesis.

## 15.3 Do not let source abundance erase narrative hierarchy

There may be more bond/event text than main-story text for some characters. Quantity is not authority. Weight evidence by narrative function and context.

## 15.4 Preserve remaining source ambiguity in analytical authority

The historical V1 full-build audit recorded these non-blocking limitations; retain them as provenance cautions and check the current source reconciliation before treating a count or gap as current:

- seven nonempty timing/control records remain typed as `unknown` with provenance;
- overarching Japanese event titles are unavailable for some records, so raw event IDs remain authoritative;
- generic group labels are not all institution-resolved;
- persistent upstream gaps and unresolved person/speaker mappings remain visible from the source-lock layer;
- release/source order is recorded where available, but **in-universe chronology is not globally resolved**.

No major synthesis should silently repair these limitations from memory or another localization.

## 15.5 Do not mistake machine relationship selection for narrative priority

`RELATIONSHIP_CANDIDATES.csv` is an excellent recall surface, not an interpretive ranking. Its metrics describe shared stories/scenes, adjacent turns, one-on-one scenes, school/club overlap, cross-school status, and Sensei presence. They do not measure:

- emotional importance;
- causality;
- intimacy;
- antagonistic or ideological weight;
- longitudinal transformation;
- whether co-presence is mostly ensemble structure.

The 40 source bundles selected in V1 were retrieval seeds, not an analytical relationship canon. Apply the same distinction to later source-bundle selections.

## 15.6 Treat main-arc maps and LLM chunks as navigation

The historical V1 source corpus exposed seven main-arc maps and reversible LLM chunks; later generations retain their own inventory. Use them to retrieve efficiently, then return to the complete canonical story for close reading. Chunk boundaries must not become literary scene boundaries unless they coincide with the source scene structure.

---

# 16. Long-term target corpus

A mature Blue Archive analytical corpus should eventually allow the following retrieval routes:

**Story question**\
`current map → main deep reading → canonical story → utterance/choice ID → raw record`

**Character question**\
`current map → character monograph → state / relationship / voice ledgers → canonical story/MomoTalk/bond → raw record`

Before a monograph exists:\
`current map → character analytical coverage index → checkpoint → applicable ledgers → source-facing reading → canonical source`

**Relationship question**\
`current map → relationship synthesis → relationship ledger → contextual scenes → source`

**Institution question**\
`current map → institutional synthesis → institution ledger → main/group/event sources`

**Exact Japanese wording question**\
`current map → locator index → canonical source → structured record → raw table`

**How did our interpretation change?**\
`current map → claim-revision ledger → prior artifact → current authority → evidence route`

**What would this bounded version of a character plausibly do?**\
`current map → reconstruction model (selected state/domain) → monograph + relevant ledgers → canonical evidence`

The coverage index first checks whether that model/domain exists; the specification governs its use. Validation records attach to the exact model/rule snapshot, and hypothetical applications remain downstream. Source bundles may accelerate retrieval but never replace complete canonical evidence for consequential inference.

If no current model or eligible domain exists, stop at the coverage index and answer from literary evidence without presenting the result as reconstruction capability.

This is the desired end state: **one analytical responsibility per artifact, one current authority path, and no loss of reversibility back to the Japanese source.**

## Phase2 cycle003 production boundary — 2026-10-01

[31 group objects](../02%20Sequential%20Readings/BLUE_ARCHIVE_PHASE2_CONTEXTUALIZATION_CYCLE_003_CHECKPOINT.md) bring scoped supplemental admission to100 while every whole-arc row remains incomplete. Ordinary enjoyment, personal wishes, fallible care, recipient objections and routine work enter the seven ledgers with exact evidence modes. Readiness remains23 partial/394 unmodeled/417, standalone NONE. The next major architectural phase is **Phase3 — Character / relationship / institution packages**, after Phase2 obligations are fulfilled; this tranche does not certify that transition.

## Phase2 cycle004 production boundary — 2026-10-01

[The remaining22 group objects](../02%20Sequential%20Readings/BLUE_ARCHIVE_PHASE2_CONTEXTUALIZATION_CYCLE_004_CHECKPOINT.md) close complete group-content intake at65/65 and bring supplemental admission to122. All seven ledgers and coverage/control effects retain ordinary value, actual recipients, source modes and contrary cases. [Fourteen group-grounded families](../08%20Audits%20and%20Manifests/BLUE_ARCHIVE_PHASE2_PRINCIPAL_SCOPE_EXTENSION_001.md) add227 required private objects and three mini relevance leads; current wholePhase2 scope is3631 mandatory/3682 tracked, with3560 still unaccepted. Readiness remains23 partial/432 unmodeled/455, standalone NONE. All12 arc rows and9 wholePhase2 requirements remain incomplete. Phase3 — Character / relationship / institution packages follows sufficient contextualization and its distinct evidence/readiness gates; no package/model is manufactured by this tranche.

## Phase2 cycle005 production boundary — 2026-10-01

[The58-object acceptance](../02%20Sequential%20Readings/BLUE_ARCHIVE_PHASE2_CONTEXTUALIZATION_CYCLE_005_CHECKPOINT.md) brings admitted contextual evidence to180:65 group/43 event/30 bond/30 MomoTalk/12 written-data. Reijo and Ayane complete their available required pools; baseballRei completes ten secure own objects, while four full Tsukuyo/Junko inquiry objects are accepted in their actual contexts without false appearance credit. EVENT807/814 are complete, with ordinary wishes, play, rest, giving and counterevidence retained. All seven ledgers and the five current coverage tables reconcile the accepted effects. Existing readiness stays fixed:23 partial/482 unmodeled/505 analytical subjects, every standaloneNONE.

The full scope remains3631 mandatory/3682 tracked, with3451 mandatory/3502 tracked objects unaccepted. Required private remainders1031B/1031M/422D;57 event packages/967 objects remain. All12 arc rows remain incomplete. Phase3 — Character / relationship / institution packages follows the architecture evidence gates; full-pool intake is distinct from broad transfer or a finished model. Chronology, actual recipients, raw actors, consent conditions and unprinted outcomes retain their limits. No stakes threshold excludes quiet character evidence.

The [complete65-group/12-arc relevance audit](../08%20Audits%20and%20Manifests/BLUE_ARCHIVE_PHASE2_GROUP_ARC_RELEVANCE_AUDIT.md) is parent-accepted as P2-R01 PASS_WITH_LIMITS with no additional source admission. Direct person/community core, bounded comparisons and inspected absence are grounded in the full accepted arguments. P2-R02–R09 and all12 full-arc rows remain incomplete; each source retains intrinsic ordinary value and its original knowledge/identity/chronology limits.
