---
series: CHIRAMUNE
artifact_type: synthesis_architecture
scope: OPEN_ENDED_JAPANESE_LIGHT_NOVEL_FULL_SERIES
source_boundary: "Locked Japanese light-novel corpus through main Volume 09 plus acquired V03/V05/V08 supplements, Volume 06.5, Days of Endless Summer, and Volume 09.5; analysis frozen through main Volume 03 with its bundled bonus and separate booklet classified and integrated"
generation: V0.4
status: canonical
release_state: mutable_active
architecture_lifecycle: EVOLVING
governing_method: CHIRAMUNE_ANALYTICAL_METHOD.md
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
---

# Chiramune full-series architecture

## 1. Responsibility and lifecycle

This document governs how prospective Japanese-light-novel readings accumulate into a coherent Chiramune corpus: where source-unit findings are preserved, how later evidence revises earlier hypotheses, when ledgers or character models earn independent homes, and how the analyzed-to-date corpus can support synthesis without pretending that publication has ended.

"Full-series" names the architectural reach, not the current completion state. Chiramune is treated as an open-ended publishing corpus. Reaching every source currently held means **current-source analysis complete**, not "complete series," "final model," or "finished corpus."

This architecture is paired with `CHIRAMUNE_ANALYTICAL_METHOD.md`:

- the method governs what to notice and how to judge evidence;
- the longitudinal layer governs what must survive cumulatively;
- this architecture governs where those preserved states converge.

The architecture is governance, not literary evidence. It establishes no character or thematic conclusion merely by naming a responsibility.

## 2. Authority and canonical route

The canonical first-read surface is `../CURRENT_STATE_AND_CORPUS_MAP.md`. It must always state the live publication, acquisition, main-volume analysis, supplemental-analysis, and next-safe-reading horizons.

The source and authority split remains:

- Japanese EPUB witnesses and their integrity evidence stay in the governed primary-source plane outside Git;
- original analysis and its source hashes/locators belong under `series/chiramune/`;
- `series/chiramune` is the continuing working-publication branch;
- GitHub `main` remains current repository authority until a validated branch state is integrated through the owner-controlled process.

This architecture is subordinate to the live repository authority records, integration policies, project-initiation policy, reasoning-class policy, sequential-continuation policy, and archive/supersession policy.

## 3. Horizon vector

Do not collapse "available" or "complete" into one number. Maintain this five-part state in the current corpus map:

| Horizon | Meaning | Current post-V03-booklet checkpoint |
|---|---|---|
| `H_pub` | latest publication established by the current bibliographic/source audit | Volume 09.5; official Shogakukan series catalog rechecked 2026-09-07 |
| `H_acq` | latest acquired main and supplemental witnesses | main V09; supplemental V09.5; 14 locked EPUB objects total |
| `H_main` | latest numbered main volume prospectively frozen | V03 |
| `H_supp` | supplemental witnesses analytically integrated after a safe boundary | V03 in-EPUB pre-main birthday bonus (`BONUS_FICTION`) plus separate V03 illustration/SS booklet (`SUPPLEMENTAL_MAINLINE`) |
| `H_next` | next source safe to open without contaminating a prior freeze | main Volume 04 |

The live source inventory has no missing numbered main volume through V09. Known limits remain: retailer-exclusive bonuses are not claimed exhaustive; regular-edition V08 is not separately held, while the special edition contains the complete V08 narrative; supplemental placement must be resolved before analytical use.

Any later publication or acquisition changes `H_pub` or `H_acq` only after identity, provenance, and integrity are verified. It does not automatically advance analysis.

## 4. Source and witness model

Assign every admitted object one primary analytical role:

- `MAIN_LN` — numbered Japanese novel in the prospective spine;
- `BONUS_FICTION` — official fiction bundled inside a main-volume object but analytically separated from its numbered narrative and placed only with explicit publication/diegetic provenance;
- `SAME_EDITION_SUPPLEMENT` — additional material packaged with a main-volume witness but analytically separable from the narrative;
- `SUPPLEMENTAL_MAINLINE` — official half-volume, booklet, special-edition story, or comparable main-continuity witness;
- `SIDE_STORY_COLLECTION` — a later compilation whose component provenance and placement may differ;
- `PARATEXT` — afterword or official contextual material used only for the questions it can support;
- `ADAPTATION_PERFORMANCE` — anime, audio, staged, or other performance evidence kept distinct from novel authority;
- `OTHER_ADMITTED` — another verified witness with a separately documented responsibility.

Japanese main novels remain the primary semantic spine. Translation, synopsis, wiki, reception, and remembered plot knowledge may assist navigation only; they do not replace available Japanese text.

Before opening a non-spine witness analytically, record:

1. exact object identity and hash;
2. original publication relationship to the main sequence;
3. known diegetic placement and dependencies;
4. the earliest safe prospective insertion boundary;
5. what the witness is permitted to revise.

If publication or diegetic dependency is materially unresolved, keep the insertion boundary `OPEN`. A story set earlier is not automatically safe to read earlier.

Standing handling rules at this baseline are:

- freeze V03 before opening the V03 booklet;
- use regular V05 for the mainline freeze, then isolate distinct V05 special-edition material;
- classify V06.5 before integration;
- freeze the V08 main narrative inside the special edition before using its rough-illustration supplement;
- place *Days of Endless Summer* by verified provenance and diegetic dependency;
- keep V09.5 from rewriting the V09 freeze.

## 5. Atomic main-volume transaction

One numbered main novel is the default atomic sequential unit. A VNN transaction is complete only when every applicable responsibility closes:

1. verify the exact witness against the source lock;
2. recover the prior prospective freeze and current revision/open-question state;
3. record the entering expectations before opening VNN;
4. read the Japanese source closely and retain returnable locators;
5. write `CHIRAMUNE_VNN_DEEP_READING.md` with facts, inferences, rival readings, counterevidence, ordinary-life evidence, and limits;
6. adjudicate affected prior claims using `PRESERVE / STRENGTHEN / REVISE / DOWNGRADE / REJECT / OPEN`;
7. update only the rolling ledgers materially affected;
8. update or create character models only when the evidence threshold is met;
9. create `CHIRAMUNE_VNN_PROSPECTIVE_FREEZE.md` before any later numbered or unsafe supplemental source is opened;
10. advance the horizon vector and route in `CURRENT_STATE_AND_CORPUS_MAP.md`;
11. run the live stable-series author preflight, review the exact staged path set and diff, commit, push normally, and verify the exact remote checkpoint.

A drafted reading without its required cumulative updates, freeze, state advance, and verified checkpoint is not transactionally closed.

The current owner instruction authorizes `continuous_sequential` execution from V03 through every source in the live admitted inventory at run start. Each unit must still close atomically before the next source is opened.

## 6. Prospective history and claim revision

The dedicated rolling claim home is `../03 Longitudinal Ledgers/CHIRAMUNE_REVISION_LEDGER.md`.

For every material transition preserve:

- stable claim ID;
- earlier wording and the source boundary that made it reasonable;
- transition state;
- testing evidence and locator route;
- current formulation or explicit uncertainty;
- current authoritative artifact.

Deep readings and prospective freezes are source-bound historical records. They are not silently rewritten with later knowledge. A later volume changes the current model through the revision ledger and maintained syntheses; it does not erase what an earlier boundary supported.

## 7. Longitudinal infrastructure

The V01–V03 evidence maintains four independent thematic/relationship ledgers plus the revision ledger:

- self-authorship / performance / authenticity;
- agency / intervention / responsibility;
- social status / inclusion / group dynamics;
- relationship / recognition / intimacy.

These files are cumulative maintained documents. Update established rows when current meaning changes and append new boundary-specific entries without duplicating earlier sections. Git history records in-place maintenance; prospective freezes preserve immutable epistemic states.

Add another ledger only when a recurring dimension accumulates independently, affects downstream synthesis, and becomes unreliable to retrieve from the deep readings or current ledgers. Ordinary-life evidence, Fukui locality, humor, food, clothing, hobbies, and mundane continuity must remain visible, but do not split them into a dedicated artifact until retrieval pressure warrants it.

## 8. Character-model promotion

Create or update a monograph only after sufficient multi-scene evidence supports an independent reconstruction. A qualifying model should distinguish:

- first-person self-narration;
- internal focalization;
- external witness testimony;
- public/social performance;
- independently corroborated capability;
- stable tendency versus recipient, role, and stress state;
- contradiction, counterevidence, and abstention boundary;
- ordinary-life behavior, not crisis scenes alone.

V01–V03 justify active-provisional monographs for Saku Chitose, Yuzuki Nanase, and Asuka Nishino. Asuka crosses the threshold at V03 through direct focalization, formation history, ordinary-life evidence, family conflict, vocation, relationship evidence, and counterevidence. The corpus does not justify symmetrical monographs for every named character. Global character discovery remains the separate curation agent's responsibility.

## 9. Synthesis layers

Chiramune has two conceptually distinct integration targets:

1. **Current published-corpus synthesis** — a rolling, explicitly horizon-labeled synthesis of the analyzed corpus at a meaningful checkpoint. It remains revisable and may be updated in place as `H_main` and `H_supp` advance.
2. **Terminal full-series synthesis** — eligible only if the publication corpus is demonstrably closed, every admitted source is disposed, longitudinal and specialist responsibilities converge, and a role-gap audit shows the architecture is ready.

The route contract is `../06 Full-Series Synthesis/README.md`. Do not create a rolling synthesis merely to restate two volume readings. Promote it when cross-ledger convergence becomes independently useful, then identify `H_pub`, `H_acq`, `H_main`, and `H_supp` in its front matter and title.

Current-source completion is an operational checkpoint, not terminal synthesis readiness.

### 9.1 Multi-document synthesis portfolio

Full-series integration is explicitly a **multi-document architecture**, not a mandate to accumulate every conclusion in one monolith. The portfolio has separate retrieval and authority roles:

| Document class | Canonical location | Responsibility | Promotion state at V03 |
|---|---|---|---|
| Prospective volume readings and freezes | `../02 Sequential Readings/` | Preserve source-bound findings and the epistemic state at each boundary | active through V03 |
| Rolling revision and thematic ledgers | `../03 Longitudinal Ledgers/` | Maintain current cross-volume claims, transitions, and recurring dimensions | active through V03 |
| Character monographs | `../04 Character Analysis/` | Reconstruct independently warranted characters without flattening witness or state distinctions | Saku, Yuzuki, and Asuka active-provisional |
| Specialist syntheses | future `../05 Specialist Synthesis/` documents | Integrate one mature domain whose evidence and dependencies warrant independent retrieval | anticipated; none yet promoted |
| Current published-corpus synthesis | future `CHIRAMUNE_CURRENT_PUBLISHED_CORPUS_SYNTHESIS.md` under `../06 Full-Series Synthesis/` | Converge the analyzed-to-date portfolio while routing detail back to the specialist and cumulative homes | deferred at V03 until an independently useful convergence boundary |
| Terminal full-series synthesis | future separately named terminal artifact under `../06 Full-Series Synthesis/` | Integrate stabilized specialist outputs after publication closure and the terminal gates | ineligible |

The current published-corpus synthesis and eventual terminal synthesis are integrators and claim routers. They must cite or link to the relevant specialist, character, ledger, and prospective documents rather than absorb those documents' complete evidentiary burden. A specialist document remains separately authoritative for its bounded domain; a later integrator may reconcile domains but must record any material revision through the revision ledger.

The portfolio may expand or contract at architecture-review checkpoints. Promotion requires a recurring question, a distinct evidence base or dependency path, and independent retrieval value. A planned document that never meets that threshold remains deferred rather than being created as an empty category.

## 10. Specialist and adaptation responsibilities

Create specialist work only when a question has independent retrieval responsibility. Candidate Chiramune-specific domains include:

- social self-authorship, beauty, performance, authenticity, and enclosure;
- informal status, inclusion, embarrassment resilience, and legitimacy lending;
- agency, helping, consent, intervention, risk, and responsibility;
- directional romance, recognition, specialness, jealousy, and mutual knowledge;
- Fukui locality, ordinary youth, aspiration, future adulthood, and departure;
- prose voice, first-person rhetoric, humor, metaphor, and self-mythologizing.

Anime, audio drama, voice performance, music, staging, framing, editing, or other adaptation evidence must receive an `ADAPTATION_PERFORMANCE` identity and a declared source boundary. Such work may compare retention, omission, compression, changed focalization, visual direction, sound, and performance, but it cannot silently overwrite novel findings.

## 11. Evidence and locator routing

Use the lightest structure that preserves deterministic retrieval:

- source identity/hash -> source lock and source-plane audit manifest;
- passage evidence -> volume deep reading using extraction-resource/paragraph locators;
- frozen claim state -> prospective freeze;
- current cross-volume claim -> revision or thematic ledger;
- mature convergence -> character, specialist, or rolling synthesis.

Create a dedicated locator index under `../07 Evidence and Indexes/` only when cross-volume retrieval from local locator tables becomes unreliable. Do not duplicate primary-source text or full source manifests in Git.

## 12. State, focalization, and contradiction routing

Maintain distinctions among:

- source fact, inference, hypothesis, prediction, value judgment, and open question;
- character knowledge, narrator interpretation, reader knowledge, and independent corroboration;
- public role, private state, self-narration, external witness, and recipient-conditioned behavior;
- attraction, admiration, friendship, desire, jealousy, dependence, commitment, named love, and mutually acknowledged romance;
- numbered-main continuity, safely admitted supplement, paratext, and adaptation witness.

Classify apparent contradiction before harmonizing it. Possible causes include focalizer bias, deception, strategic disclosure, state/recipient change, later recontextualization, wording or edition variance, supplemental retrospection, adaptation divergence, or genuine inconsistency. Material unresolved conflict stays `OPEN` in the appropriate ledger.

## 13. Responsibility matrix

| Dimension | Sequential capture | Current cumulative home | Mature destination | Baseline state |
|---|---|---|---|---|
| Major claims and predictions | every material boundary | revision ledger + prospective freezes | specialist and rolling synthesis | initialized through V03 |
| Self-authorship/performance | when material | self-authorship ledger | character/specialist/rolling synthesis | initialized through V03 |
| Agency/intervention | when material | agency ledger | character/specialist/rolling synthesis | initialized through V03 |
| Status/group topology | when material | social-status ledger | ensemble/specialist/rolling synthesis | initialized through V03 |
| Relationships/intimacy | directional changes | relationship ledger | character/relationship/rolling synthesis | initialized through V03 |
| Character state | when evidence threshold is met | Saku, Yuzuki, and Asuka monographs plus relevant ledgers | mature character synthesis | active-provisional through V03 |
| Ordinary life/locality/humor | when diagnostic | deep reading and affected current ledger | specialist only if earned | local capture required |
| Exact locators/wording | for material claims | deep reading; source lock for identity | evidence index if promoted | local routing sufficient |
| Adaptation/performance | only after separate admission | future adaptation-specific route | comparative specialist synthesis | deferred |

## 14. Dependency order

The default convergence route is:

```text
source lock + method + architecture
                |
                v
       VNN deep reading + freeze
                |
                v
 revision ledger + affected rolling ledgers
                |
        +-------+--------+
        |                |
        v                v
 character promotion   specialist promotion
        +-------+--------+
                |
                v
 current published-corpus synthesis
                |
                v
 architecture/role-gap audit at current-source or publication closure
                |
                v
 terminal full-series synthesis only when actually eligible
```

## 15. Reasoning classes

| Operation | Default class |
|---|---|
| source inventory and locator administration | `BOUNDED_STANDARD` |
| numbered-volume deep reading and interpretive ledger update | `SUBSTANTIVE_ANALYSIS` |
| mature character or relationship synthesis | `DEEP_SYNTHESIS` |
| checkpoint convergence and architecture/role-gap audit | `DEEP_SYNTHESIS` |
| propagation-sensitive terminal full-series synthesis | `PREMIUM_QUALITY_FIRST` when eligibility is proven |

Reasoning class never changes source or artifact authority.

## 16. Mutability, extension, and completion states

- Current map, source lock, architecture, rolling ledgers, monographs, and rolling synthesis are maintained in place through targeted edits.
- Deep readings and prospective freezes become frozen source-boundary records after publication.
- A materially different superseded interpretation is retained through repository supersession semantics; redundant unpublished local copies are not promoted merely to preserve duplication.
- Extend the architecture when a dimension recurs independently, affects later synthesis, or cannot be represented responsibly in its current home. Record material changes in the corpus map.
- Backfill prior volumes only when the new responsibility exposes a material evidence gap that the existing freezes and source locators cannot repair.

Completion states are:

1. `BASELINE_ESTABLISHED` — architecture and reconciled V01–V02 corpus are published and verified;
2. `SEQUENTIAL_IN_PROGRESS` — main numbered volumes advance one prospective transaction at a time;
3. `CURRENT_SOURCE_MAINLINE_COMPLETE` — every held/admitted numbered main volume is frozen;
4. `CURRENT_SOURCE_SUPPLEMENTS_COMPLETE` — every safely placeable held supplement is integrated or explicitly deferred;
5. `ANALYZED_TO_DATE_RECONCILED` — map, ledgers, monographs, and rolling synthesis accurately reflect the current horizon;
6. `TERMINAL_SYNTHESIS_READY` — only after publication closure and role-gap/convergence gates;
7. `VALIDATED_RELEASE` — the eligible synthesis and exact repository state pass required audits.

At the post-V03-booklet checkpoint the architecture is `EVOLVING`, the main high-water mark is V03, the in-EPUB pre-main bonus is integrated under `BONUS_FICTION`, the separate V03 booklet is frozen under `SUPPLEMENTAL_MAINLINE`, the next safe source is main V04, and the continuous run remains open through the live admitted inventory.
