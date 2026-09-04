---
series: ASCENDANCE_OF_A_BOOKWORM
artifact_type: corpus_map
scope: JP_LIGHT_NOVEL_INITIAL_ARCHITECTURE
source_boundary: "Japanese-language light-novel EPUB corpus: numbered main Volumes 01-33 plus acquired Royal Academy Stories: First Year side-story volume; source audit dated 2026-08-30"
generation: V0.2
status: canonical
release_state: mutable_active
architecture_lifecycle: INITIAL
governing_method: "00 Frameworks and Methods/BOOKWORM_ANALYTICAL_METHOD.md"
synthesis_architecture: "00 Frameworks and Methods/BOOKWORM_SYNTHESIS_ARCHITECTURE.md"
master_longitudinal_state: "03 Longitudinal Ledgers/BOOKWORM_MASTER_LONGITUDINAL_LEDGER.md"
sequential_analysis_lock: OPEN
committed_high_water_mark: PRE_V01
next_sequential_operation: BOOKWORM_V01_DEEP_READING
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
  source_reconnaissance_complete: true
  governing_method: 00 Frameworks and Methods/BOOKWORM_ANALYTICAL_METHOD.md
  governing_method_status: canonical
  synthesis_architecture: 00 Frameworks and Methods/BOOKWORM_SYNTHESIS_ARCHITECTURE.md
  synthesis_architecture_status: canonical
  master_longitudinal_state: 03 Longitudinal Ledgers/BOOKWORM_MASTER_LONGITUDINAL_LEDGER.md
  required_day_one_infrastructure_initialized: true
  sequential_analysis_lock: OPEN
  committed_high_water_mark: PRE_V01
  next_sequential_operation: BOOKWORM_V01_DEEP_READING
```

The paired-foundation gate is therefore satisfied for the locked Japanese-light-novel boundary: the project has both a governing method and a governing synthesis/corpus architecture, plus the justified day-one cumulative state layer.

**No numbered volume has yet been analyzed.** Opening the sequential lock means V01 may begin when separately requested; it is not itself authorization to process later volumes.

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
6. the relevant frozen sequential reading(s), once they exist
7. only the character, specialist, or evidence artifact needed for the operation

## Materialized analytical architecture

| Layer | Responsibility | Current state |
|---|---|---|
| `00 Frameworks and Methods` | How evidence is read and where accumulated knowledge must converge | method + synthesis architecture present |
| `01 Source Lock and Inventory` | Exact source boundary, integrity, part routing, Drive provenance | present |
| `02 Sequential Readings` | Prospective V01-V33 atomic volume readings | contract present; no readings yet |
| `03 Longitudinal Ledgers` | Cumulative cross-volume state | master pre-split ledger initialized |
| `04 Character Analysis` | Evidence-earned character-specific analysis | router present; no monographs yet |
| `05 Specialist Synthesis` | Cross-volume domains with independent synthesis responsibility | router present; no specialist syntheses yet |
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
│   └── BOOKWORM_V01_DEEP_READING.md ... BOOKWORM_V33_DEEP_READING.md  [created only as completed]
├── 03 Longitudinal Ledgers/
│   ├── README.md
│   ├── BOOKWORM_MASTER_LONGITUDINAL_LEDGER.md
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

1. Perform a Japanese-primary V01 deep reading under `single_operation` unless the user explicitly authorizes a bounded continuous range.
2. Update `03 Longitudinal Ledgers/BOOKWORM_MASTER_LONGITUDINAL_LEDGER.md` with only material cumulative changes.
3. Adjudicate any material claims or prospective questions that V01 can actually test.
4. Advance this file's committed high-water mark to V01 only after the full atomic transaction is closed.
5. Freeze V01 before opening V02.
6. Review architecture at V03, V07, V12, V21, and V33, or earlier if a material recurring dimension lacks a proper home.
7. Keep *Royal Academy Stories: First Year* outside the numbered prospective chain until its publication/diegetic placement and legitimate retrospective scope are verified.

## Current abstentions

- No personality, relationship, political, ethical, religious, metaphysical, or thematic claim is canonical merely because it appears in a synopsis, adaptation, wiki, fandom discussion, prior conversation, or model memory.
- A focalizer's belief is evidence of that focalizer's model, not automatically an objective setting fact.
- Later titles, roles, identities, and institutional knowledge must not be projected backward as though earlier volumes already established them.
- No supplemental story is silently inserted into the numbered prospective chain.
- No translation replaces Japanese as the semantic anchor for wording-sensitive questions when Japanese is available.
- No PACTRIH score or other comparative ethical placement is assigned before source-grounded character evidence is sufficient.
- Later evidence may revise the current model but may not erase what an earlier prospective freeze reasonably supported.
