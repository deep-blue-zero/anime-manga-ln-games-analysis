---
series: CHIRAMUNE
artifact_type: corpus_map
scope: JP_LIGHT_NOVEL_OPEN_ENDED_ANALYSIS
source_boundary: "Japanese-language light-novel EPUB corpus through main Volume 09 plus acquired V03/V05/V08 supplements, Volume 06.5, Days of Endless Summer, and Volume 09.5; source audit dated 2026-08-29 and official publisher catalog rechecked 2026-09-07; main analysis frozen through Volume 09; all admitted narrative supplements integrated through Volume 09.5; V08 rough collection integrated as PRODUCTION_PARATEXT"
generation: V1.6
status: canonical
release_state: mutable_active
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
---

# Chitose Is in the Ramune Bottle — current state and corpus map

This is the canonical first read for the Git-side *Chitose Is in the Ramune Bottle* (`Chiramune`; Japanese: `千歳くんはラムネ瓶のなか`) analytical corpus.

## Authority split

- **GitHub `main` is the analytical authority.** Interpretive claims, methods, deep readings, longitudinal ledgers, character work, syntheses, and analytical audits belong under `series/chiramune/`.
- **Google Drive is the primary-source authority.** The Japanese EPUBs and their integrity/audit manifest remain in the governed primary-source Drive plane and are not copied into Git.
- **Local/Codex workspaces are working environments**, not authority unless an artifact is promoted through the governed Drive-evidence or Git-analysis route.

Primary-source Drive root: `1tNJvglC-ri_AEGTkJupZ78WddyiCqQMy`  
Chiramune source folder: `1bI8p0tRpD7_u6Xi3vubqydl-jR7gJFxx`  
Source audit manifest: `1Oq8MhiuNApwg-qv9PxEfJG9YTzLuZy52`  
Audited manifest SHA-256: `e4d302d662997ae67be9368d45dd2dc7fefd5918f5c8540cbe82a897c00a8231`

See `01 Source Lock and Inventory/CHIRAMUNE_SOURCE_LOCK_AND_INVENTORY.md` before any source-facing analysis.

## Project initialization state

```yaml
project_initialization:
  status: canonical
  architecture_lifecycle: EVOLVING
  analytical_phase: ANALYZED_TO_DATE_RECONCILED
  source_reconnaissance_complete: true
  governing_method: 00 Frameworks and Methods/CHIRAMUNE_ANALYTICAL_METHOD.md
  method_status: canonical
  synthesis_architecture: 00 Frameworks and Methods/CHIRAMUNE_FULL_SERIES_ARCHITECTURE.md
  architecture_status: canonical
  required_day_one_infrastructure_initialized: true
  required_day_one_infrastructure:
    - 03 Longitudinal Ledgers/CHIRAMUNE_REVISION_LEDGER.md
    - 03 Longitudinal Ledgers/CHIRAMUNE_SELF_AUTHORSHIP_PERFORMANCE_AND_AUTHENTICITY_LEDGER.md
    - 03 Longitudinal Ledgers/CHIRAMUNE_AGENCY_INTERVENTION_AND_RESPONSIBILITY_LEDGER.md
    - 03 Longitudinal Ledgers/CHIRAMUNE_SOCIAL_STATUS_INCLUSION_AND_GROUP_DYNAMICS_LEDGER.md
    - 03 Longitudinal Ledgers/CHIRAMUNE_RELATIONSHIP_RECOGNITION_AND_INTIMACY_LEDGER.md
  sequential_analysis_lock: OPEN
  committed_high_water_mark: VOLUME_09_5_SUPPLEMENTAL_CHECKPOINT
  next_sequential_operation: NONE__AWAIT_NEW_ADMISSION
```

The paired-foundation gate is open: the canonical analytical method governs what to notice and how to judge it; the canonical full-series architecture governs the multi-document accumulation and convergence route; and all five required cumulative ledgers are current through the Volume 09.5 supplemental boundary.

## Current analytical state

**The full-series architecture and prospective V01–V09 main analytical corpus are established on the continuing Chiramune branch. Volume 09 is the latest numbered prospective freeze; every admitted supplement through the three-chapter Volume 09.5 is integrated through a separate frozen checkpoint. All 14 objects in the live source lock are analyzed or explicitly bounded. No next source is admitted.**

The corpus contains distinct V01–V09 main deep readings and freezes, separate V03, V05, V06.5, V08-rough, *Days of Endless Summer*, and V09.5 supplemental readings/checkpoints, five rolling longitudinal responsibilities, ten active-provisional character monographs, two promoted specialist syntheses, and a mutable current published-corpus synthesis. The Volume 03 EPUB's own pre-main birthday story is `BONUS_FICTION`; the separate V03 booklet, individually routed V05 booklet stories, four late-August V06.5 components, individually placed *Days* fiction, and three V09.5 chapters are `SUPPLEMENTAL_MAINLINE`. The V05 Special Edition's regular-main duplicate is verified but not double-counted. Its revised V03 cap story is two edition witnesses to one event, with variants preserved. The V08 special-edition main froze first; its 50-page art collection then entered as `PRODUCTION_PARATEXT`, with design alternatives and rough/final stages barred from becoming extra events. V09 completes the V08 festival story through its own regular `MAIN_LN` boundary. *Days* republishes 36 stories across earlier boundaries and adds one post-festival bridge. V09.5 separates pre-series Misaki/Kuranosuke history, Nazuna's nested current/middle-school frame, and a post-*Days* adult coda. Earlier prospective artifacts remain separate epistemic states rather than being rewritten with later knowledge.

`00 Frameworks and Methods/CHIRAMUNE_FULL_SERIES_ARCHITECTURE.md` governs the open-ended corpus, atomic closeout, horizon tracking, revision route, synthesis layers, and adaptation boundary.

## Horizon vector

| Horizon | Current state | Evidence / limit |
|---|---|---|
| latest known publication (`H_pub`) | Volume 09.5 | official Shogakukan series catalog rechecked 2026-09-07: 14 listed releases, ending with Volume 09.5; retailer-exclusive completeness is not claimed |
| latest source acquired (`H_acq`) | main V09; supplemental V09.5 | 14 locked EPUB objects; all live local hashes reverified against the source lock before the V01–V02 baseline |
| latest main volume analyzed (`H_main`) | V09 main | V01–V09 main deep readings and prospective freezes present; V09 is a regular main-only witness |
| supplemental analysis (`H_supp`) | V03 in-EPUB birthday bonus, separate V03 illustration/SS booklet, V05 Special Edition 18-story booklet, V06.5 four-story volume, V08 rough collection, *Days of Endless Summer*, and Volume 09.5 | all admitted supplements are integrated through separate checkpoints; V08 art is production paratext, *Days* is component-routed, and V09.5 preserves three distinct chronology structures |
| next safe reading (`H_next`) | `NONE__AWAIT_NEW_ADMISSION` | every object in the live 14-file lock is analyzed or explicitly bounded; a later source requires fresh admission and source-lock verification |

Unresolved acquisition scope is limited to unclaimed retailer-exclusive or ephemeral bonuses and future publications. There is no missing numbered main volume through V09 in the locked inventory. Regular-edition V08 is not separately held, but its complete narrative is present in the special-edition witness.

```yaml
sequential_execution:
  mode: continuous_sequential
  unit_type: volume_then_safe_supplement
  authorized_start: V03
  terminal_boundary: ALL_ADMITTED_SOURCES_IN_LIVE_INVENTORY_AT_RUN_START
  committed_high_water_mark: VOLUME_09_5_SUPPLEMENTAL_CHECKPOINT
  next_candidate_operation: NONE__AWAIT_NEW_ADMISSION
  confirmation_between_units: false
  run_state: current_source_complete
```

## Source boundary

The current locked source set contains 14 Japanese EPUB objects representing:

- main narrative Volumes 01–09;
- the separate Volume 03 illustration/short-story booklet;
- the Volume 05 special edition/SS material in addition to the regular Volume 05 witness;
- Volume 06.5;
- *Days of Endless Summer*;
- Volume 08 as the special edition containing the complete Volume 08 novel plus the rough-illustration supplement;
- Volume 09.5.

The audit found no missing main numbered volume through Volume 09 and no exact duplicate file groups. The current lock does **not** claim exhaustive possession of every retailer-exclusive purchase bonus ever distributed. Such bonuses remain outside the source boundary until separately acquired and audited.

## Governing method

Read in this order for new Chiramune analytical work:

1. `CURRENT_STATE_AND_CORPUS_MAP.md`
2. `00 Frameworks and Methods/CHIRAMUNE_ANALYTICAL_METHOD.md`
3. `00 Frameworks and Methods/CHIRAMUNE_FULL_SERIES_ARCHITECTURE.md`
4. `01 Source Lock and Inventory/CHIRAMUNE_SOURCE_LOCK_AND_INVENTORY.md`
5. the latest prospective freeze and `03 Longitudinal Ledgers/CHIRAMUNE_REVISION_LEDGER.md`;
6. only the rolling ledger, character model, or earlier source-bound reading needed for the task.

The Japanese prose is the current semantic anchor. Later anime material, official interviews, reception research, translations, or other adaptations may become separate witnesses, but they do not silently alter this source boundary.

## Corpus architecture

| Layer | Analytical responsibility | Current state |
|---|---|---|
| `00 Frameworks and Methods` | Governing source-reading, inference, prospective-freeze, multi-document full-series accumulation, comparison, and synthesis rules | populated; analytical method V0.2 and full-series architecture V1.5, including the Volume 09.5 current-source role-gap review |
| `01 Source Lock and Inventory` | Exact acquired-source boundary, integrity state, and Drive routing | populated; canonical V1.3; all 14 objects disposed |
| `02 Sequential Readings` | Volume-by-volume prospective deep readings, immutable freezes, and warranted supplemental checkpoints | V01–V09 main frozen; every admitted supplement through Volume 09.5 integrated |
| `03 Longitudinal Ledgers` | Claim revision plus recurring cross-volume state/relationship/theme tracking | all five ledgers reconciled through Volume 09.5; retrospective testimony remains distinguished from current transition |
| `04 Character Analysis` | Character syntheses created only after evidence warrants them | ten active-provisional monographs; Misaki, Kuranosuke, and Nazuna promoted at V09.5 |
| `05 Specialist Synthesis` | Dense recurring thematic/relationship/form and future adaptation/performance questions | Fukui locality/departure/ordinary youth plus sport/effort/mentorship/institutional authority promoted; separate performance specialist deferred after review |
| `06 Full-Series Synthesis` | Router for the multi-document portfolio and rolling analyzed-to-date integration, conceptually separate from terminal full-series synthesis | router plus mutable current published-corpus synthesis through Volume 09.5; terminal synthesis ineligible |
| `07 Evidence and Indexes` | Git-side cross-volume claim/evidence routing if later needed | not instantiated; source lock plus reading-local locators and the *Days* component graph are sufficient through the current boundary |
| `08 Audits and Manifests` | Bootstrap inventory, package reconciliation, and later analytical/source-integrity records | bootstrap manifest plus V01–V02 reconciliation audit |
| `90 Legacy and Superseded` | Materially distinct superseded analysis | not instantiated; no legacy analytical corpus is being imported |

The absence of a directory is intentional. Do not create empty categories merely to make Chiramune resemble another project.

## Volume 09.5 reconciled state

The exact V08 main and supplemental boundaries and current rolling revisions live in:

- `02 Sequential Readings/CHIRAMUNE_V07_PROSPECTIVE_FREEZE.md`;
- `02 Sequential Readings/CHIRAMUNE_V07_DEEP_READING.md`;
- `02 Sequential Readings/CHIRAMUNE_V08_MAIN_PROSPECTIVE_FREEZE.md`;
- `02 Sequential Readings/CHIRAMUNE_V08_MAIN_DEEP_READING.md`;
- `02 Sequential Readings/CHIRAMUNE_V08_ROUGH_ILLUSTRATION_SUPPLEMENTAL_READING.md`;
- `02 Sequential Readings/CHIRAMUNE_V09_PROSPECTIVE_FREEZE.md`;
- `02 Sequential Readings/CHIRAMUNE_V09_DEEP_READING.md`;
- `02 Sequential Readings/CHIRAMUNE_DAYS_OF_ENDLESS_SUMMER_SUPPLEMENTAL_READING.md`;
- `02 Sequential Readings/CHIRAMUNE_V09_5_SUPPLEMENTAL_READING.md`;
- `03 Longitudinal Ledgers/CHIRAMUNE_REVISION_LEDGER.md`;
- the four thematic/relationship ledgers;
- the ten active character monographs, including Misaki, Kuranosuke, and Nazuna;
- `05 Specialist Synthesis/CHIRAMUNE_FUKUI_LOCALITY_DEPARTURE_AND_ORDINARY_YOUTH_SYNTHESIS.md`;
- `05 Specialist Synthesis/CHIRAMUNE_SPORT_EFFORT_MENTORSHIP_AND_INSTITUTIONAL_AUTHORITY_SYNTHESIS.md`;
- `06 Full-Series Synthesis/CHIRAMUNE_CURRENT_PUBLISHED_CORPUS_SYNTHESIS.md`.

The required current guardrails are:

- Saku's V07 five-person romantic enumeration remains unranked; V09 admits Momiji to the answerable field without directly naming current Saku-side romantic love for her;
- Saku's direct V08 romantic wording for Yuzuki, V09 mirror/moon recognition, acting-only stage choice, and conditional epilogue materially differentiate her without establishing singular selection or a couple;
- Yuzuki's V08 consent violation remains part of the continuing relation; V09 accountability and repair do not retroactively authorize or erase it;
- the play's best-actress result is Yuzuki for `today, this stage only` under the expressly non-romantic rule; the shared apple is not a lip kiss;
- Yua's public musical address is direct Yua-side romantic/self-authoring evidence and Saku's listening response is not selection;
- group-level direct repair with Momiji is complete, while prior harm and the absence of identical long dyadic adjudications remain preserved;
- Momiji's immediate dating request is refused; her attempted social expulsion is rescinded and she receives rooftop access plus answerable-claimant standing, not couple status;
- the unchanged blue group form ends, while lateral friendship, rivalry, sport, art, and ordinary relations continue;
- Haru's paired race strengthens reciprocal coordination and her primary Yuzuki partnership without settling basketball rank, team repair, romantic challenge, or vocation;
- Tomoya's apology and creative reintegration strengthen accountability without erasing stalking harm or entitling restored intimacy;
- the self-originated support-request, baseball, Tokyo, editing, and durable basketball-vocation tests remain open;
- preserve all earlier freezes and supplemental component graphs without back-projecting V08;
- the rough-illustration collection is `PRODUCTION_PARATEXT`: proposals are not hidden canon, rough/final stages are not separate events, retrospective early-volume art cannot rewrite freezes, and guest art has no diegetic authority;
- preserve F122–F148, DES-F01–DES-F11, and V095-F01–V095-F12 as distinct main and supplemental transitions.
- preserve all earlier prospective freezes: the 36 republished *Days* stories are later-admitted retrospective testimony, not earlier-boundary rewrites;
- preserve the collection's only present bridge as post-festival and pre-Okinawa: Momiji's third-key responsibility, Asuka/Yua dyads, and fair rivalry enact social admission without romantic acceptance;
- internal marriage, children, kissing, and cohabitation fantasies are not mutual outcomes; food, gifts, recipes, rooms, dances, and keys do not establish a couple;
- Yuzuki's historical fake-to-real love and future breakfast bid strengthen differentiation without converting the acting-only V09 choice into exclusive selection;
- Yua's restored routine does not erase the V08 consent violation, and her boundary around the dedicated stool is compatible with bounded repair;
- Volume 09.5 identifies Kuranosuke as Misaki's historical helper only at its later boundary; the V08 identity abstention remains correct and must not be retroactively rewritten;
- Misaki/Kuranosuke mutual historical love and adult intimacy do not establish a named couple, engagement, marriage, or cohabitation;
- Atomu's serious independent practice is not institutional return, and Nazuna's embodied inquiry is not competitive resumption;
- the roof lineage carries maintenance and access, not ownership or romantic rank;
- adult teaching/coaching paths are enacted, while current youth baseball, basketball, Tokyo, and editing futures remain open;
- sport/effort/mentorship now has a promoted specialist responsibility; performance remains independently retrievable through the self-authorship ledger and source-bound readings, so no separate performance specialist is promoted.

Comparisons to *Oregairu*, *AoButa*, *Classroom of the Elite*, PACTRIH, or other corpus frameworks remain downstream operations. Reconstruct Chiramune on its own evidence first.

## Work order after current-source reconciliation

1. Preserve the V01–V09 main freezes and every independently classified supplemental checkpoint as distinct source-boundary records.
2. Admit no new source through existence, marketing, or memory alone; verify identity, provenance, integrity, role, and safe insertion boundary first.
3. For a later source, record entering questions from the Volume 09.5 reconciled state before content use.
4. Update only materially affected ledgers, monographs, specialists, and synthesis layers; preserve current hard nonclaims until direct evidence revises them.
5. Publish each future coherent checkpoint to `series/chiramune` through the same staged preflight, remote audit, and exact-SHA validation gates.
6. Do not merge to `main`; integration remains owner-controlled and separately governed.

## Standing abstentions

- No character personality claim is current merely because it appeared in a synopsis, marketing copy, fandom discussion, or an earlier ChatGPT conversation.
- No kanji name reading is inferred by generic CJK transliteration when an official/furigana reading is available or required.
- No retailer-exclusive SS is treated as present unless it is actually acquired and audited.
- No PACTRIH score or other comparative ethical placement is assigned before source-grounded character evidence is sufficient.
- No later source is allowed to rewrite the record of what an earlier prospective reading reasonably inferred at the time.
