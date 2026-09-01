---
series: BLUE_ARCHIVE
artifact_type: synthesis_architecture
scope: "Analytical corpus architecture for Japanese-primary Blue Archive interpretation"
generation: V1
status: canonical
source_boundary: "Designed for the Blue Archive extraction corpus pinned to electricgoat/ba-data@jp cbe3fd623c2aab9e781ba0ce0483bc77c68bff86 and its future promoted generations"
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
created: 2026-08-15
updated: 2026-08-15
---

# BLUE ARCHIVE SYNTHESIS ARCHITECTURE V1
## Canonical analytical responsibilities, document topology, ledgers, and release strategy

## 0. Architectural objective

This architecture converts the extracted Japanese Blue Archive corpus into a durable analytical project without duplicating the source pipeline or flattening a live-service work into one enormous synthesis.

The project uses one canonical analytical root and one canonical source/ingestion root.

**Analytical root:** `Blue Archive` under the Manga / Anime analytical hierarchy.\
**Source/ingestion root:** the existing `Blue_Archive` extraction mirror containing `blue-archive-corpus-pipeline/corpus`.

The two roots have different responsibilities:

- **source root** — raw upstream snapshots, 2,716 promoted canonical story/data objects, structured data, character/relationship/institution/Sensei projections, LLM ingest, audits;
- **analytical root** — methods, sequential readings, cumulative ledgers, specialist interpretation, full/current-era synthesis, evidence indexes, manifests, and legacy analytical generations.

Do not duplicate the full transcript corpus into the analytical root. Analytical artifacts should link back to it through stable IDs and Drive routes.

## Source-projection versus analytical-artifact boundary

The promoted source corpus now contains a mature derived layer. Preserve the following semantic separation:

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
```

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

Do not automatically deep-read all 492 recoverable event script groups as separate canonical analytical files. Events should first be triaged for continuity importance.

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

Classify each event:

- CORE
- HIGH
- SUPPORTING
- LOW-STAKES / VOICE
- DEFER
- UNRESOLVED

A CORE event deserves a sequential reading because omitting it would materially weaken understanding of a major character, relationship, institution, or continuity state.

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

**Status: COMPLETE.** The V1 canonical build reports `PASS` with 2,716 canonical story/data objects, 2,047 scenes, 102,665 utterances, 8,774 preserved choice groups, 12,821 MomoTalk messages, and 7,089 character contextual lines. The derived build also reports `PASS` and provides the retrieval projections required for Phase 1 and later contextualization.

## Phase 1 — Main story pass

Read main story sequentially.

Outputs:

- deep readings;
- character/institution/Sensei ledger deltas;
- arc checkpoints.

Supplemental layers are consulted only when required to resolve source identity or when the governing reading plan explicitly backfills them after an arc.

## Phase 2 — Arc contextualization

After each major main-story arc:

- identify core related group stories;
- classify events by importance;
- read relevant bond/MomoTalk for major characters;
- inspect character-data voice for linguistic baseline;
- update ledgers.

This phase turns a plot reading into a social-world reading.

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

The source-promotion milestone has passed. Proceed in this order:

1. `BLUE_ARCHIVE_SOURCE_LOCK_V1.md`
2. main-story corpus-map crosswalk on the analytical side;
3. first canonical main-story deep reading;
4. character-state ledger;
5. institution ledger;
6. Sensei-role ledger;
7. continue sequentially to the first natural arc checkpoint;
8. perform event/group/bond/MomoTalk contextual backfill for characters central to that arc;
9. write first checkpoint;
10. only then decide which first specialist monograph is justified.

This prevents the project from becoming a character-encyclopedia exercise before the main narrative establishes its world and causal architecture.

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
supersedes: null
superseded_by: null
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

Bulk promotion is complete, but the full build still records non-blocking limitations:

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

The 40 selected source bundles should therefore seed relationship review, not determine the analytical relationship canon.

## 15.6 Treat main-arc maps and LLM chunks as navigation

The source corpus now exposes seven main-arc maps and reversible LLM chunks. Use them to retrieve efficiently, then return to the complete canonical story for close reading. Chunk boundaries must not become literary scene boundaries unless they coincide with the source scene structure.

---

# 16. Long-term target corpus

A mature Blue Archive analytical corpus should eventually allow the following retrieval routes:

**Story question**\
`current map → main deep reading → canonical story → utterance/choice ID → raw record`

**Character question**\
`current map → character monograph → state ledger → contextual source bundle → canonical story/MomoTalk/bond → raw record`

**Relationship question**\
`current map → relationship synthesis → relationship ledger → contextual scenes → source`

**Institution question**\
`current map → institutional synthesis → institution ledger → main/group/event sources`

**Exact Japanese wording question**\
`current map → locator index → canonical source → structured record → raw table`

**How did our interpretation change?**\
`current map → claim-revision ledger → prior artifact → current authority → evidence route`

This is the desired end state: **one analytical responsibility per artifact, one current authority path, and no loss of reversibility back to the Japanese source.**
