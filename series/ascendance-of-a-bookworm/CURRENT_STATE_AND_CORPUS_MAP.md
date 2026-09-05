---
series: ASCENDANCE_OF_A_BOOKWORM
artifact_type: corpus_map
scope: JP_LIGHT_NOVEL_SEQUENTIAL_ANALYSIS
source_boundary: "Japanese-language light-novel EPUB corpus: numbered main Volumes 01-33 plus acquired Royal Academy Stories: First Year side-story volume; source audit dated 2026-08-30"
generation: V0.4
status: canonical
release_state: mutable_active
architecture_lifecycle: INITIAL
analytical_phase: SEQUENTIAL_IN_PROGRESS
governing_method: "00 Frameworks and Methods/BOOKWORM_ANALYTICAL_METHOD.md"
synthesis_architecture: "00 Frameworks and Methods/BOOKWORM_SYNTHESIS_ARCHITECTURE.md"
master_longitudinal_state: "03 Longitudinal Ledgers/BOOKWORM_MASTER_LONGITUDINAL_LEDGER.md"
sequential_analysis_lock: OPEN
committed_high_water_mark: V02
latest_frozen_reading: "02 Sequential Readings/BOOKWORM_V02_DEEP_READING.md"
next_sequential_operation: BOOKWORM_V03_DEEP_READING
next_sequential_operation_authorization: separate
next_part_boundary_review: V03_POST_FREEZE
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
---

# Ascendance of a Bookworm — current state and corpus map

This is the canonical first-read surface for the Git-side *Ascendance of a Bookworm* (Japanese: `本好きの下剋上～司書になるためには手段を選んでいられません～`) analytical corpus.

It owns current project state and routing. The analytical method and synthesis architecture are separate governing artifacts so that each has one clear responsibility.

## Authority and working branch

- **GitHub `main` is the current analytical authority.** The continuing branch `series/ascendance-of-a-bookworm` is the working integration surface for new Bookworm analysis until reviewed content is integrated.
- **Google Drive is the primary-source evidence plane.** Japanese EPUBs and their audit manifest remain outside Git.
- **Local/Codex workspaces are working environments**, not authority unless promoted through a governed route.

Primary-source Drive root: `1tNJvglC-ri_AEGTkJupZ78WddyiCqQMy`  
Bookworm source folder: `1jijErFCqkxFfP1C8s5SJkaphiImF_vvJ`  
Source audit manifest: `1EWZLfUcopzCJT3iCZmCElOnq0jFUWgL0`  
Audited manifest SHA-256: `034f01acae4e14f58ad8f9ea925ef00813603c74b590f08c8ba4e628db147d82`

Read `01 Source Lock and Inventory/BOOKWORM_SOURCE_LOCK_AND_INVENTORY.md` before any source-facing analysis.

## Project initialization state

```yaml
project_initialization:
  status: canonical
  architecture_lifecycle: INITIAL
  analytical_phase: SEQUENTIAL_IN_PROGRESS
  source_reconnaissance_complete: true
  governing_method: 00 Frameworks and Methods/BOOKWORM_ANALYTICAL_METHOD.md
  governing_method_status: canonical
  synthesis_architecture: 00 Frameworks and Methods/BOOKWORM_SYNTHESIS_ARCHITECTURE.md
  synthesis_architecture_status: canonical
  master_longitudinal_state: 03 Longitudinal Ledgers/BOOKWORM_MASTER_LONGITUDINAL_LEDGER.md
  required_day_one_infrastructure_initialized: true
  sequential_analysis_lock: OPEN
  committed_high_water_mark: V02
  numbered_volumes_completed:
    - V01
    - V02
  latest_frozen_reading: 02 Sequential Readings/BOOKWORM_V02_DEEP_READING.md
  next_sequential_operation: BOOKWORM_V03_DEEP_READING
  next_sequential_operation_authorization: separate
  next_part_boundary_review: V03_POST_FREEZE
```

The paired-foundation gate remains satisfied for the locked Japanese-light-novel boundary: the project has both a governing method and a governing synthesis/corpus architecture, plus the justified cumulative state layer.

**V01 and V02 are complete and prospectively frozen.** V03 is the next architectural source unit and the final volume of Part 1, but it requires a separate user instruction. After V03 freezes, the first mandatory part-boundary architecture/promotion review must run before the project simply advances onward.

## Current V02 freeze

The second source-unit transaction is closed at global **V02**, Japanese identity **第一部「兵士の娘」II**.

Canonical source-facing artifact:

`02 Sequential Readings/BOOKWORM_V02_DEEP_READING.md`

Primary witness:

- normalized filename: `Ascendance of a Bookworm - Volume 02.epub`;
- SHA-256: `d075f1856cd233729c4873b576464a87597d7240977ca1e4b4d7e77500a2eeca`;
- entering state: `V01`;
- exiting state: `V02`;
- prospective state: `FROZEN`;
- later numbered-volume knowledge used: `false`.

The V02 transaction adjudicates all ten V01-facing predictions and propagates material cumulative state into `03 Longitudinal Ledgers/BOOKWORM_MASTER_LONGITUDINAL_LEDGER.md`.

The most important boundary conditions are:

- plant-fiber paper is now a demonstrated product, but scaling remains incomplete;
- Myne/Lutz complementarity now includes explicit identity disclosure/recognition and survival care;
- Myne's positive attachment to current life is materially stronger;
- `身食い` is strongly corroborated as the local diagnosis matching Myne's escalating internal-heat crisis;
- the exact metaphysical mechanism and the outcome of the emergency intervention remain open because V02 ends before treatment is shown;
- magical contracts, guild authorization/finance, and noble-linked survival access establish that magic is institutional infrastructure as well as a supernatural phenomenon;
- ordinary noble-only magic doctrine remains in tension with commoner `身食い` evidence;
- no dedicated character monograph, relationship synthesis, specialist synthesis, or split ledger is yet required before the V03 Part 1 checkpoint.

## Historical V01 freeze

V01 remains a frozen historical source boundary and is not superseded by V02.

Canonical source-facing artifact:

`02 Sequential Readings/BOOKWORM_V01_DEEP_READING.md`

Primary witness:

- normalized filename: `Ascendance of a Bookworm - Volume 01.epub`;
- SHA-256: `10c8e7b69054f721036b8bef37e77005fe4046ff216aa9b7b078ec20cbcf77d0`;
- entering state: `PRE_V01`;
- exiting state: `V01`;
- prospective state: `FROZEN`.

V02 may revise the current model while leaving the V01 historical formulation intact. In particular, Benno's V01 `身食い` hypothesis was correctly frozen as unconfirmed at V01 even though V02 later provides much stronger corroboration.

## Locked source boundary

The 2026-08-30 audit records **34 Japanese EPUB objects**:

- **33 numbered main volumes**, V01-V33, with no gaps;
- **one side-story volume**, *Royal Academy Stories: First Year*;
- no byte-identical duplicate groups.

The Japanese source filenames encode five parts:

| Part | Japanese part title | Numbered volumes |
|---|---|---:|
| Part 1 | `第一部「兵士の娘」` | V01-V03 |
| Part 2 | `第二部「神殿の巫女見習い」` | V04-V07 |
| Part 3 | `第三部「領主の養女」` | V08-V12 |
| Part 4 | `第四部「貴族院の自称図書委員」` | V13-V21 |
| Part 5 | `第五部「女神の化身」` | V22-V33 |

The normalized English filenames are routing conveniences; Japanese remains the semantic anchor.

This boundary does **not** silently include anime, manga, translations, web-publication versions, fanbooks/reference works, other side stories, retailer bonuses, interviews, production commentary, reception material, or fandom sources.

## Governing read order

For new Bookworm analytical work, read in this order:

1. `CURRENT_STATE_AND_CORPUS_MAP.md`
2. `00 Frameworks and Methods/BOOKWORM_ANALYTICAL_METHOD.md`
3. `00 Frameworks and Methods/BOOKWORM_SYNTHESIS_ARCHITECTURE.md`
4. `01 Source Lock and Inventory/BOOKWORM_SOURCE_LOCK_AND_INVENTORY.md`
5. `03 Longitudinal Ledgers/BOOKWORM_MASTER_LONGITUDINAL_LEDGER.md`
6. the relevant frozen sequential readings, currently V01 and V02
7. only the character, specialist, or evidence artifact needed for the operation

Before opening V03, recover the V02-frozen prospective state from the master ledger and `BOOKWORM_V02_DEEP_READING.md`. Do not use later-volume memory to adjust those predictions after the fact.

## Materialized analytical architecture

| Layer | Responsibility | Current state |
|---|---|---|
| `00 Frameworks and Methods` | How evidence is read and where accumulated knowledge must converge | method + synthesis architecture present |
| `01 Source Lock and Inventory` | Exact source boundary, integrity, part routing, Drive provenance | present |
| `02 Sequential Readings` | Prospective V01-V33 atomic volume readings | V01 and V02 present/frozen; V03 next but separately authorized |
| `03 Longitudinal Ledgers` | Cumulative cross-volume state | master pre-split ledger current through V02; no split yet warranted |
| `04 Character Analysis` | Evidence-earned character-specific analysis | router present; no monographs yet; promotion review due after V03 |
| `05 Specialist Synthesis` | Cross-volume domains with independent synthesis responsibility | router present; no specialist syntheses yet; promotion review due after V03 |
| `06 Full-Series Synthesis` | Final integrated synthesis after completion gates | router present; gate closed |
| `07 Evidence and Indexes` | Cross-volume locator/terminology/coverage/revision structures when needed | router present; no promoted index yet |
| `08 Audits and Manifests` | Historical bootstrap and later audit/manifests as warranted | bootstrap manifest present |
| `90 Legacy and Superseded` | Materially distinct superseded analysis | not instantiated; no superseded Bookworm analysis exists |

Git does not track empty directories. Future artifact homes are materialized by their routing files only when the routing responsibility is useful; `90 Legacy and Superseded` remains absent until an actual supersession creates a reason for it.

## Proposed mature activation tree

```text
series/ascendance-of-a-bookworm/
├── CURRENT_STATE_AND_CORPUS_MAP.md
├── 00 Frameworks and Methods/
│   ├── BOOKWORM_ANALYTICAL_METHOD.md
│   └── BOOKWORM_SYNTHESIS_ARCHITECTURE.md
├── 01 Source Lock and Inventory/
│   └── BOOKWORM_SOURCE_LOCK_AND_INVENTORY.md
├── 02 Sequential Readings/
│   ├── README.md
│   ├── BOOKWORM_V01_DEEP_READING.md  [present; frozen]
│   ├── BOOKWORM_V02_DEEP_READING.md  [present; frozen]
│   └── BOOKWORM_V03_DEEP_READING.md ... BOOKWORM_V33_DEEP_READING.md  [created only as completed]
├── 03 Longitudinal Ledgers/
│   ├── README.md
│   ├── BOOKWORM_MASTER_LONGITUDINAL_LEDGER.md  [current through V02]
│   └── <split ledgers only when retrieval pressure warrants>
├── 04 Character Analysis/
│   ├── README.md
│   └── <Character>/...  [evidence-triggered]
├── 05 Specialist Synthesis/
│   ├── README.md
│   └── <part-boundary/domain syntheses when earned>
├── 06 Full-Series Synthesis/
│   ├── README.md
│   └── BOOKWORM_FULL_SERIES_SYNTHESIS.md  [completion-gated]
├── 07 Evidence and Indexes/
│   ├── README.md
│   └── <locator/terminology/coverage/revision indexes when warranted>
├── 08 Audits and Manifests/
│   └── BOOKWORM_BOOTSTRAP_PATH_MANIFEST.json
└── 90 Legacy and Superseded/  [deferred until real supersession]
```

This tree shares the archive's common analytical language without forcing Bookworm into another project's ledger count or specialist structure.

## Atomic sequential work order

1. Treat V01 and V02 as frozen historical boundaries and recover V02's prospective claims from `BOOKWORM_V02_DEEP_READING.md` plus the master ledger.
2. Open V03 only on separate authorization and read it as the new source increment without importing still-later knowledge.
3. Update `03 Longitudinal Ledgers/BOOKWORM_MASTER_LONGITUDINAL_LEDGER.md` with only material cumulative changes.
4. Adjudicate V02 claims and V03-facing predictions that V03 actually tests.
5. Advance this file's committed high-water mark only after the full V03 atomic transaction closes.
6. Freeze V03.
7. **Immediately after V03 freeze, perform the mandatory Part 1 architecture/promotion review** before opening V04. Reconsider character, relationship, specialist, evidence-index, and ledger-split responsibilities against the completed Part 1 evidence.
8. Continue later mandatory architecture reviews at V07, V12, V21, and V33, or earlier if a material recurring dimension lacks a proper home.
9. Keep *Royal Academy Stories: First Year* outside the numbered prospective chain until its publication/diegetic placement and legitimate retrospective scope are verified.

## V03-facing prospective priorities

The master ledger holds the exact frozen predictions. High-priority questions entering V03 include:

- whether the Guild Master/Frieda household can provide emergency magical-tool intervention and what the actual result is;
- whether any intervention is merely temporary;
- whether earnings/product knowledge increasingly become survival capital;
- how Frieda functions as a `身食い`/wealth/noble-access comparison;
- whether Lutz's merchant route can resolve conflict with family expectations;
- whether Lutz remains the only local peer with explicit Urano identity knowledge;
- how paper scaling and hair-ornament diffusion change labor, market, and competitive structure;
- how the apparent noble-only magic doctrine can coexist with commoner `身食い`;
- whether stronger attachment to current life changes Myne's response to worsening bodily risk.

These are hypotheses and retrieval priorities, not facts about unread V03.

## Current abstentions

- V01-V02 do not settle the metaphysical relationship between Urano Motosu and the prior Myne. Lutz's deliberate acceptance settles a relationship question, not the ontology.
- `身食い` is strongly corroborated by V02 as the local diagnosis matching Myne's syndrome, but V02 does not supply a complete magic-system explanation or show the outcome of the emergency intervention at its ending.
- Do not project any later treatment result backward into V02.
- The statement that magic belongs to nobles remains in unresolved tension with commoner `身食い` evidence; do not harmonize it from unread later lore.
- Myne's Japanese/Earth analogies are evidence of her interpretive process and must not be promoted automatically to objective setting facts.
- No personality, relationship, political, ethical, religious, metaphysical, or thematic claim is canonical merely because it appears in a synopsis, adaptation, wiki, fandom discussion, prior conversation, model memory, or unread later volume.
- A focalizer's belief is evidence of that focalizer's model, not automatically an objective setting fact.
- Later titles, roles, identities, and institutional knowledge must not be projected backward as though V01-V02 already established them.
- No supplemental story is silently inserted into the numbered prospective chain.
- No translation replaces Japanese as the semantic anchor for wording-sensitive questions when Japanese is available.
- No PACTRIH score or other comparative ethical placement is assigned before source-grounded character evidence is sufficient.
- Later evidence may revise the current model but may not erase what an earlier prospective freeze reasonably supported.
