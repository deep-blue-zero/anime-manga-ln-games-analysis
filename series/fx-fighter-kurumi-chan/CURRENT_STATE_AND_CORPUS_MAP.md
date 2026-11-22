---
title: "FX Fighter Kurumi-chan — Current State and Corpus Map"
artifact_id: FX_KURUMI_CURRENT_STATE
artifact_type: current_state_and_corpus_map
series: fx-fighter-kurumi-chan
version: "1.5"
status: canonical
authority_generation: FX_KURUMI-INITIAL
authority_scope: "Canonical foundation navigation, source admission and execution state"
source_boundary: "Run FXK-RUN-20261119-V01-V10 authorizes the Japanese collected-manga main narrative V01–V10; accepted through V04"
created: 2026-11-15
last_updated: 2026-11-21
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
do_not_use_as_literary_evidence: true
project_initialization:
  status: canonical
  architecture_lifecycle: INITIAL
  governing_method: FX_KURUMI_ANALYTICAL_METHOD.md
  synthesis_architecture: FX_KURUMI_SYNTHESIS_ARCHITECTURE.md
  method_status: canonical
  architecture_status: canonical
  source_reconnaissance_complete: true
  required_day_one_infrastructure_initialized: true
  required_day_one_infrastructure:
    - FX_KURUMI_SOURCE_REGISTER.md
    - FX_KURUMI_DECISION_AND_EVIDENCE_LEDGER.md
  sequential_analysis_lock: OPEN
  next_permitted_operation: V05
sequential_execution:
  run_id: FXK-RUN-20261119-V01-V10
  mode: continuous_sequential
  unit_type: volume
  authorized_start: V01
  terminal_boundary: V10
  committed_high_water_mark: V04
  next_candidate_operation: V05
  confirmation_between_units: false
  run_state: active
source_admission: "V01–V10 main narrative authorized; each volume admitted at its own frontier; accepted through V04"
run_authorization: FXK-RUN-20261119-V01-V10
supplemental_execution:
  current_state: CLOSED_AWAITING_COMPONENT_ADMISSION
  other_narrative_admission: NOT_AUTHORIZED
recommended_reasoning_class: PREMIUM_QUALITY_FIRST
---

# FX Fighter Kurumi-chan — Current State and Corpus Map

The canonical destination is `series/fx-fighter-kurumi-chan/`. The subject is the Japanese collected manga **FX戦士くるみちゃん**, written by Demunyan and drawn by Tansan Daisuki.

**SEQUENTIAL_ANALYSIS_LOCK = OPEN.** The owner's November 19, 2026 instruction authorizes run **FXK-RUN-20261119-V01-V10**: one `continuous_sequential` run over the Japanese collected manga, authorized start V01, terminal boundary V10, one collected volume per atomic unit and no confirmation between successfully completed volumes. The run is **active**. Volumes V01–V04 have been accepted, so the committed high-water mark is **V04** and the next permitted and candidate operation is **V05**. Each volume is admitted only at its own frontier after the previous volume's transaction closes. The [source register](FX_KURUMI_SOURCE_REGISTER.md#run-activation-verification) records witness verification and the component scope below.

## Start here

| Governing document | Responsibility |
| --- | --- |
| [Analytical method](FX_KURUMI_ANALYTICAL_METHOD.md) | Manga page inspection and evidence for fictional uncertainty, decisions and consequences |
| [Synthesis architecture](FX_KURUMI_SYNTHESIS_ARCHITECTURE.md) | Cumulative state, independent source work, interpretation and acceptance |
| [Source register](FX_KURUMI_SOURCE_REGISTER.md) | Metadata reconnaissance, witness scope and pre-admission checks |
| [Decision and evidence ledger](FX_KURUMI_DECISION_AND_EVIDENCE_LEDGER.md) | Depicted decisions, numeric and visual evidence, human consequences and revisions |

The available range is ten Japanese manga EPUB witnesses, V01–V10. The register records the verified witness identities, package and image inventory, decode results and the actual inspection-lane probe. Reading order, page classification and legibility are confirmed for each volume inside its own transaction, at its own frontier, so that no later volume is exposed early.

## Accepted units

Each accepted volume has a canonical deep reading, a frozen checkpoint that records its multi-agent participation and dispositions, and a frozen entering state. Its rows are in the [decision and evidence ledger](FX_KURUMI_DECISION_AND_EVIDENCE_LEDGER.md) and its coverage is in the [source register](FX_KURUMI_SOURCE_REGISTER.md).

| Volume | Deep reading | Checkpoint | Entering state | Accepted |
| --- | --- | --- | --- | --- |
| V01 | [V01 deep reading](readings/FX_KURUMI_V01_DEEP_READING.md) | [V01 checkpoint](checkpoints/FX_KURUMI_V01_CHECKPOINT.md) | [V01 entering state](checkpoints/FX_KURUMI_V01_ENTERING_STATE.md) | 2026-11-21 |
| V02 | [V02 deep reading](readings/FX_KURUMI_V02_DEEP_READING.md) | [V02 checkpoint](checkpoints/FX_KURUMI_V02_CHECKPOINT.md) | [V02 entering state](checkpoints/FX_KURUMI_V02_ENTERING_STATE.md) | 2026-11-21 |
| V03 | [V03 deep reading](readings/FX_KURUMI_V03_DEEP_READING.md) | [V03 checkpoint](checkpoints/FX_KURUMI_V03_CHECKPOINT.md) | [V03 entering state](checkpoints/FX_KURUMI_V03_ENTERING_STATE.md) | 2026-11-21 |
| V04 | [V04 deep reading](readings/FX_KURUMI_V04_DEEP_READING.md) | [V04 checkpoint](checkpoints/FX_KURUMI_V04_CHECKPOINT.md) | [V04 entering state](checkpoints/FX_KURUMI_V04_ENTERING_STATE.md) | 2026-11-21 |

## Authorized run

| Field | State |
| --- | --- |
| Run | FXK-RUN-20261119-V01-V10, owner instruction of 2026-11-19; the private instruction receipt is recoverable through the run ID |
| Mode and unit | `continuous_sequential`; one collected volume |
| Bounds | Start V01, terminal V10 |
| Committed high-water mark | V04 |
| Next candidate | V05 |
| Authorized primary narrative | The Japanese commercial collected manga by Demunyan and Tansan Daisuki, in the supplied witnesses |
| Not authorized as evidence | The original Web manga, the anime adaptation, translations, external summaries and other separately published narrative |
| Historical-market concordance | A separate responsibility, not a condition of accepting any reading. Real exchange-rate history never enters a prospective reading |

The [V01 entering state](checkpoints/FX_KURUMI_V01_ENTERING_STATE.md) was frozen before any page image was displayed.

### Component scope

Each volume's principal classifies every image occurrence before analysis relies on it.

| Component | Scope in this run |
| --- | --- |
| Main narrative chapters | Admitted at the volume's frontier and analyzed |
| Covers, flaps, title and chapter-title pages, contents, colophon | Admitted as apparatus. Cited with an apparatus label and never as a diegetic fact. A cover image can carry information from later in the volume, so it is read after the main-narrative freeze |
| Authorial extras inside a volume (bonus strips, profiles, afterwords and similar) | Inventoried with locators and classified. The supplemental lane stays closed, so they are not narrative evidence in this run. Any exposure from classifying them is recorded in the checkpoint |
| Advertisements, previews of other works, next-volume previews | Excluded. A next-volume preview is not opened before that volume's admission |

### Multi-agent reading configuration

The architecture's standing configuration applies to every volume: an accountable principal analyst and integrator, an independent financial, causal and information-state specialist, and a distinct independent critical reviewer. Volumes whose character and relationship evidence is dense also have an independent character, relationship and Japanese-register specialist. No reduced configuration is used. Each role runs in its own execution context, opened with the same source frontier and its own assignment. Specialists work without the principal's draft. The reviewer inspects decisive pages before reading the candidate. The volume checkpoint records each role's coverage, independent findings, disagreements and the principal's disposition.

Every volume's principal role runs in a fresh context initialized from this entrypoint and the accepted durable state ([continuation policy](../../governance/source-policies/MANGA_ANIME_SEQUENTIAL_EXECUTION_SCOPE_AND_CONTINUATION_POLICY.md) Section 6). The run coordinator holds the run state, verifies each transaction for acceptance and publishes it. Specialists and reviewers write only to the working plane. The principal alone edits the reading, checkpoint and shared ledger in its own transaction.

### Execution profile

| Field | Observed value |
| --- | --- |
| Product surface | Antigravity agent application until 2026-11-21 13:50 (UTC−05:00), when the owner handed the run over; from then, the Claude Code desktop application. Owner-controlled Windows tool runtime throughout |
| Model setting | Under Antigravity: owner-selected Claude Opus 5.5 (High) for the coordinator, and every role context launched with the inherit setting. Under Claude Code: the coordinator session runs Claude Opus 5.5, and every role context is a separate Claude Code subagent that inherits the coordinator's model; no reasoning-effort setting is recorded for those subagents. No other model setting was observed |
| Source transport | Local EPUB files read in place; images extracted to a working directory outside Git |
| Filesystem read and write | VERIFIED |
| Image inspection (`STILL_IMAGE`) | VERIFIED on 2026-11-19 against a full-resolution V01 page with Japanese lettering and furigana and a 2.5× enlarged crop of small type. Each role context repeats a probe and records it |
| Text lane | No publisher text layer: the pages are images. Transcriptions are made from the page images |
| Git write | VERIFIED for the coordinator only |

The run proceeds one volume at a time in publication order. The project studies the fiction’s depictions of position, exposure, uncertainty, responsibility and harm. Its numerals and market language serve those literary questions. Consult the [initiation gate](../../governance/source-policies/MANGA_ANIME_PROJECT_INITIATION_AND_ARCHITECTURE_POLICY.md) and [continuation policy](../../governance/source-policies/MANGA_ANIME_SEQUENTIAL_EXECUTION_SCOPE_AND_CONTINUATION_POLICY.md) before changing execution state. After an interruption, recover the high-water mark from this file and the accepted checkpoints, never from a draft or a filename.

Resume from this map and its governing documents. The project-local [series descriptor](.repository/series-registry.json) supplies routing metadata for repository housekeeping. Admitted source files and evidence derivatives stay in the source or working plane.
