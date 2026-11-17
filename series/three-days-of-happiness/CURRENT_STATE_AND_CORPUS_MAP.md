---
title: "Three Days of Happiness — Current entrypoint"
artifact_id: TDH_CURRENT_STATE_AND_CORPUS_MAP
artifact_type: current_state_and_corpus_map
series: three-days-of-happiness
version: "1.1"
generation: INITIAL_BOOTSTRAP
status: canonical
scope: "Current entrypoint"
authority_scope: project_design_active_run_authority_source_boundary_and_corpus_routing
source_boundary: "TDH-JP-01 bound and admitted for run TDH-RUN-20261116-U01-U15; committed reading high-water mark U14; U15 is the next candidate"
last_updated: 2026-11-17
canonical_home: series/three-days-of-happiness/CURRENT_STATE_AND_CORPUS_MAP.md
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
project_initialization:
  status: canonical
  architecture_lifecycle: INITIAL
  governing_method: TDH_ANALYTICAL_METHOD.md
  method_status: canonical
  synthesis_architecture: TDH_SYNTHESIS_ARCHITECTURE.md
  architecture_status: canonical
  source_reconnaissance_complete: true
  required_day_one_infrastructure_initialized: true
  required_day_one_infrastructure:
    - TDH_SOURCE_REGISTER.md
    - TDH_LONGITUDINAL_NOTEBOOK.md
  sequential_analysis_lock: OPEN
  next_permitted_operation: U15
sequential_execution:
  run_id: TDH-RUN-20261116-U01-U15
  mode: continuous_sequential
  unit_type: chapter
  authorized_start: U01
  terminal_boundary: U15
  committed_high_water_mark: U14
  next_candidate_operation: U15
  confirmation_between_units: false
  run_state: active
recommended_reasoning_class: SUBSTANTIVE_ANALYSIS
---

# Three Days of Happiness — current state and corpus map

This is the single working entrypoint for **Three Days of Happiness / 三日間の幸福**, a standalone Japanese novel credited in the source metadata to **三秋 縋 (Sugaru Miaki)**. Its root is `series/three-days-of-happiness/`; its continuing branch is `series/three-days-of-happiness`.

## Authority and stop boundary

The method and architecture govern the project. The architecture lifecycle is `INITIAL`, with the targeted [§8.1 multi-agent amendment](TDH_SYNTHESIS_ARCHITECTURE.md#81-multi-agent-reading-configuration) of 2026-11-16. Owner run approval: **recorded 2026-11-16** (below).

*Bootstrap record (2026-11-07, superseded as current state on 2026-11-16):* the lock was then closed, no sequential execution existed, every frontier was empty, and the next permitted operation was `NONE_AWAITING_RUN_AUTHORIZATION`.

**SEQUENTIAL_ANALYSIS_LOCK = OPEN** from 2026-11-16, after SRC-01–SRC-04 were resolved in the [source register](TDH_SOURCE_REGISTER.md#admission-resolution-2026-11-16), the multi-agent configuration was recorded, and owner authorization was received. Run `TDH-RUN-20261116-U01-U15` is **active**. Committed reading high-water mark: **U14** (accepted 2026-11-17). Next candidate and next permitted operation: **U15**. The synthesis and reconstruction frontiers are **EMPTY**. An OPEN lock is a precondition for this run's admissions, not authority for any other source.

<a id="owner-run-authorization"></a>

### Owner run authorization

On 2026-11-16 the owner instructed one bounded analytical campaign. Its recoverable terms are:

| Term | Authorized value |
|---|---|
| Witness | The single Japanese EPUB bound as `TDH-JP-01` (verified as the intended complete witness of 三日間の幸福 at admission) |
| Mode | `continuous_sequential`; no confirmation between successfully completed units |
| Start | U01, the first narrative unit in canonical reading order, with its preceding front matter |
| Terminal source boundary | U15, the final narrative unit, together with the dispositions the register requires for end paratext and embedded images |
| Analysis language | English, with Japanese source text as interpretive authority and short original-language quotations |
| Execution ownership | Principal coordinator/integrator (role A) with independent source-aware specialists (B, C) |
| Review ownership | Independent critical reviewer (role D), distinct from the principal and the specialists |
| Stop boundary | All admitted units accepted, then completion audit, reconciliation, qualified monographs and earned studies, `synthesis/TDH_NOVEL_SYNTHESIS.md`, and the final validation audit; earlier only for a genuine access, evidence, authorization, capability or repository-integrity blocker |
| Not authorized | Other novels, editions, translations, manga or audiovisual adaptations, redistribution of source text, changes to global governance, global character or reconstruction files, or merging into `main` |

### Execution profile and prior exposure

```yaml
execution_profile:
  product_surface: "Claude Code desktop app (Code tab)"
  tool_runtime_location: "owner workstation (Windows)"
  observation_date: "2026-11-16"
  capability_scope: "Japanese EPUB text (normalized XHTML extraction), still images (JPEG/GIF via PNG), Git"
  source_transport: "local file read of the governed EPUB; private normalized extraction outside Git"
  filesystem_read: VERIFIED
  filesystem_write: VERIFIED
  image_inspection: VERIFIED
  audio_content_inspection: UNAVAILABLE
  continuous_av_inspection: UNAVAILABLE
  git_write: VERIFIED
  inspection_method: "principal session reads normalized Japanese text and views images; specialists and reviewer are native subagents in separate contexts reading the same per-unit frontier"
execution_record:
  principal_model_label_observed: "claude-opus-5-5 (runtime-declared)"
  subagent_model_label_observed: null
  reasoning_control_observed: null
  observation_basis: "runtime system declaration for the principal; subagent settings not exposed"
```

All participants are language-model instances and may hold training-derived familiarity with this published novel. Per method §2 and architecture §8.1, that familiarity is quarantined. Forecasts are labeled `PRIOR_EXPOSURE_POSSIBLE` and earn no blindness credit.

## Start here

| Responsibility | Current home | Use |
|---|---|---|
| How to read and substantiate claims | [TDH_ANALYTICAL_METHOD.md](TDH_ANALYTICAL_METHOD.md) | Text, narration, knowledge and linguistic evidence; acceptance of a future reading |
| How findings accumulate | [TDH_SYNTHESIS_ARCHITECTURE.md](TDH_SYNTHESIS_ARCHITECTURE.md) | Compact standalone design, responsibilities, dependencies and completion gates |
| Source identity, limits and admission | [TDH_SOURCE_REGISTER.md](TDH_SOURCE_REGISTER.md) | Bound witness `TDH-JP-01`, admission resolution, `TDH-NORM-v1` locators and the U01–U15 unit map with per-unit states |
| State, claims and readiness | [TDH_LONGITUDINAL_NOTEBOOK.md](TDH_LONGITUDINAL_NOTEBOOK.md) | Separate named sections for state, claims, form/register, and reconstruction eligibility |

Both supporting records are required day-one infrastructure. At the 2026-11-16 admission they hold source/control facts and empty analytical tables. No character state, narrative claim, reading, checkpoint, monograph or model exists yet.

## Reading corpus

| Unit | Canonical reading | Acceptance |
|---|---|---|
| U01 | [Front matter and chapter 1 「十年後の約束」](readings/TDH_U01_DEEP_READING.md) | Accepted 2026-11-17 (A + B + C + D; reviewer `ACCEPT_WITH_CORRECTIONS`, corrections adopted) |
| U02 | [Chapter 2 「終わりの始まり」](readings/TDH_U02_DEEP_READING.md) | Accepted 2026-11-17 (A + B + C + D; reviewer `ACCEPT_WITH_CORRECTIONS`, corrections adopted) |
| U03 | [Chapter 3 「三角座りの監視員」](readings/TDH_U03_DEEP_READING.md) | Accepted 2026-11-17 (A + B + C + D; reviewer `ACCEPT_WITH_CORRECTIONS`, corrections adopted) |
| U04 | [Chapter 4 「答えあわせといきましょう」](readings/TDH_U04_DEEP_READING.md) | Accepted 2026-11-17 (A + B + C + D; reviewer `ACCEPT_WITH_CORRECTIONS`, corrections adopted) |
| U05 | [Chapter 5 「これから起こることすべて」](readings/TDH_U05_DEEP_READING.md) | Accepted 2026-11-17 (A + B + C + D; reviewer `ACCEPT_WITH_CORRECTIONS`, corrections adopted) |
| U06 | [Chapter 6 「変わってしまった人、変われなかった人」](readings/TDH_U06_DEEP_READING.md) | Accepted 2026-11-17 (A + B + C + D; reviewer `ACCEPT_WITH_CORRECTIONS`, corrections adopted; specialist exposure incident disclosed) |
| U07 | [Chapter 7 「タイムカプセル荒らし」](readings/TDH_U07_DEEP_READING.md) | Accepted 2026-11-17 (A + B + C + D; reviewer `ACCEPT_WITH_CORRECTIONS`, corrections adopted) |
| U08 | [Chapter 8 「不適切な行動」](readings/TDH_U08_DEEP_READING.md) | Accepted 2026-11-17 (A + B + C + D; reviewer `ACCEPT_WITH_CORRECTIONS`, corrections adopted) |
| U09 | [Chapter 9 「できすぎた話」](readings/TDH_U09_DEEP_READING.md) | Accepted 2026-11-17 (A + B + C + D; reviewer `ACCEPT_WITH_CORRECTIONS`, corrections adopted) |
| U10 | [Chapter 10 「私の、たった一人の幼馴染へ」](readings/TDH_U10_DEEP_READING.md) | Accepted 2026-11-17 (A + B + C + D; reviewer `ACCEPT_WITH_CORRECTIONS`, corrections adopted) |
| U11 | [Chapter 11 「自販機巡りのすすめ」](readings/TDH_U11_DEEP_READING.md) | Accepted 2026-11-17 (A + B + C + D; reviewer `ACCEPT_WITH_CORRECTIONS`, corrections adopted) |
| U12 | [Chapter 12 「嘘つきと小さな願い」](readings/TDH_U12_DEEP_READING.md) | Accepted 2026-11-17 (A + B + C + D; reviewer `ACCEPT_WITH_CORRECTIONS`, corrections adopted) |
| U13 | [Chapter 13 「確かなこと」](readings/TDH_U13_DEEP_READING.md) | Accepted 2026-11-17 (A + B + C + D; reviewer `ACCEPT_WITH_CORRECTIONS`, corrections adopted) |
| U14 | [Chapter 14 「青の時代」](readings/TDH_U14_DEEP_READING.md) | Accepted 2026-11-17 (A + B + C + D; reviewer `ACCEPT_WITH_CORRECTIONS`, corrections adopted) |

## Reconnaissance actually achieved

On 2026-11-07, bounded reconnaissance established a source folder containing one novel EPUB and a prior technical audit. The audit dated 2026-08-30 reports a Japanese MediaWorks Bunko witness, 333,787 bytes, 40 archive entries, five image resources and successful container/CRC checks. Those are **reported earlier checks**, not this campaign's byte or page verification. The report labels the main novel complete; this bootstrap has not independently certified that claim. No prose, illustrations, chapter boundaries, reading order or rendered legibility was inspected. The inventory alias `ThreeDays` resolves to this work; it is not an additional project.

There is no admitted translation, manga adaptation, audio or screen adaptation. The title does not establish a narrative chronology or an interpretation of happiness, value or mortality. Such questions must arise from future inspected evidence.

*2026-11-16:* this run rehashed the witness and resolved structure, encoding, image decodability and edition identity; the results are in the [source register](TDH_SOURCE_REGISTER.md#admission-resolution-2026-11-16). The paragraph above stays as the bootstrap observation.

## Allowed bootstrap continuation

*Historical (bootstrap boundary).* The conditions below were satisfied on 2026-11-16 as recorded under [Owner run authorization](#owner-run-authorization) and in the source register's admission resolution.

Review the full method, architecture and empty-state contracts; resolve source identity and chapter/spine mapping using the source register; record any resulting design amendment. Source access alone does not authorize narrative reading. A future owner-authorized run must state the exact witness, admitted units, language, prospective horizon, execution owner, review ownership and stop boundary before the lock can be reconsidered.

The unresolved admission obligations are `SRC-01` through `SRC-04` in the source register. They concern witness binding, internal segmentation, source completeness/legibility and edition/paratext boundaries. They prevent sequential admission but do not prevent review of this architecture.

## Execution and resumption

Metadata reconciliation uses `BOUNDED_STANDARD`; future serious sequential reading uses `SUBSTANTIVE_ANALYSIS`, escalating if focalization or contradiction requires it. Architecture and the eventual integrated novel reading use `PREMIUM_QUALITY_FIRST`: errors would propagate across the whole work, so an independent counterreading and a duty-by-duty audit are the expected reliability gain. Character studies and reconstruction design use `DEEP_SYNTHESIS`. These are workload classes, not fixed product/model names.

Each unit follows the standing [multi-agent configuration](TDH_SYNTHESIS_ARCHITECTURE.md#81-multi-agent-reading-configuration). Resume by reading this entrypoint, then both frameworks and the latest source/control rows. After an interruption, the committed high-water mark in the front matter outranks remembered conversational state. Do not reconstruct state from chat. Future source-unit work must include the complete reading and ledger transaction; a handoff summary is a retrieval aid and cannot replace those artifacts. No reader-facing overview is required until there is a completed analytical corpus.
