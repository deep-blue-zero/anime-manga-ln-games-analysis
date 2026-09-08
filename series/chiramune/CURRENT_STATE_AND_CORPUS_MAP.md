---
series: CHIRAMUNE
artifact_type: corpus_map
scope: JP_LIGHT_NOVEL_OPEN_ENDED_ANALYSIS
source_boundary: "Japanese-language light-novel EPUB corpus through main Volume 09 plus acquired V03/V05/V08 supplements, Volume 06.5, Days of Endless Summer, and Volume 09.5; source audit dated 2026-08-29 and official publisher catalog rechecked 2026-09-07; main analysis frozen through Volume 08 main; V03 bundled bonus, separate V03 booklet, component-routed V05 special-edition booklet, and component-routed V06.5 volume integrated; V08 rough-illustration supplement unopened"
generation: V1.2
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
  analytical_phase: SEQUENTIAL_IN_PROGRESS
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
  committed_high_water_mark: V08_MAIN_PROSPECTIVE_CHECKPOINT
  next_sequential_operation: V08_ROUGH_ILLUSTRATION_SUPPLEMENTAL_READING
```

The paired-foundation gate is open: the canonical analytical method governs what to notice and how to judge it; the canonical full-series architecture governs the multi-document accumulation and convergence route; and all five required cumulative ledgers are initialized and current through V08 main.

## Current analytical state

**The full-series architecture and prospective V01–V08 main analytical corpus are established on the continuing Chiramune branch. The latest numbered prospective freeze is Volume 08 main; the V03 illustration/short-story booklet, V05 Special Edition 18-story booklet, and V06.5 four-story volume are integrated through separate frozen supplemental checkpoints. The separately titled V08 rough-illustration supplement is the next safe source and remains unopened.**

The corpus contains distinct V01–V08 main deep readings and freezes, separate V03, V05, and V06.5 supplemental readings/checkpoints, five rolling longitudinal responsibilities, seven active-provisional character monographs, the promoted Fukui locality/departure/ordinary-youth specialist synthesis, and a mutable current published-corpus synthesis. The Volume 03 EPUB's own pre-main birthday story is `BONUS_FICTION`; the separate V03 booklet, individually routed V05 booklet stories, and four late-August V06.5 components are `SUPPLEMENTAL_MAINLINE`. The V05 Special Edition's regular-main duplicate is verified but not double-counted. Its revised V03 cap story is two edition witnesses to one event, with variants preserved. The V08 special-edition main is frozen separately from its unopened rough-illustration supplement. V09 and later admitted sources remain unopened. Earlier prospective artifacts remain separate epistemic states rather than being rewritten with later knowledge.

`00 Frameworks and Methods/CHIRAMUNE_FULL_SERIES_ARCHITECTURE.md` governs the open-ended corpus, atomic closeout, horizon tracking, revision route, synthesis layers, and adaptation boundary.

## Horizon vector

| Horizon | Current state | Evidence / limit |
|---|---|---|
| latest known publication (`H_pub`) | Volume 09.5 | official Shogakukan series catalog rechecked 2026-09-07: 14 listed releases, ending with Volume 09.5; retailer-exclusive completeness is not claimed |
| latest source acquired (`H_acq`) | main V09; supplemental V09.5 | 14 locked EPUB objects; all live local hashes reverified against the source lock before the V01–V02 baseline |
| latest main volume analyzed (`H_main`) | V08 main | V01–V08 main deep readings and prospective freezes present; V08 main is separated from its rough supplement |
| supplemental analysis (`H_supp`) | V03 in-EPUB birthday bonus, separate V03 illustration/SS booklet, V05 Special Edition 18-story booklet, and V06.5 four-story volume | separate supplemental checkpoints preserve individual class, provenance, chronology, focalization, and edition-witness routing |
| next safe reading (`H_next`) | V08 rough-illustration supplement | V08 main is independently frozen; inspect the separate titled collection as supplemental production/design evidence before V09 |

Unresolved acquisition scope is limited to unclaimed retailer-exclusive or ephemeral bonuses and future publications. There is no missing numbered main volume through V09 in the locked inventory. Regular-edition V08 is not separately held, but its complete narrative is present in the special-edition witness.

```yaml
sequential_execution:
  mode: continuous_sequential
  unit_type: volume_then_safe_supplement
  authorized_start: V03
  terminal_boundary: ALL_ADMITTED_SOURCES_IN_LIVE_INVENTORY_AT_RUN_START
  committed_high_water_mark: V08_MAIN_PROSPECTIVE_CHECKPOINT
  next_candidate_operation: V08_ROUGH_ILLUSTRATION_SUPPLEMENTAL_READING_AFTER_V08_MAIN_PUBLICATION
  confirmation_between_units: false
  run_state: active
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
| `00 Frameworks and Methods` | Governing source-reading, inference, prospective-freeze, multi-document full-series accumulation, comparison, and synthesis rules | populated; analytical method V0.2 and full-series architecture V1.0, including compilation/edition-witness routing |
| `01 Source Lock and Inventory` | Exact acquired-source boundary, integrity state, and Drive routing | populated; canonical V0.8 |
| `02 Sequential Readings` | Volume-by-volume prospective deep readings, immutable freezes, and warranted supplemental checkpoints | V01–V08 main frozen; V03, V05, and V06.5 supplemental checkpoints integrated; V08 rough supplement next |
| `03 Longitudinal Ledgers` | Claim revision plus recurring cross-volume state/relationship/theme tracking | five ledgers active through V08 main; earlier frozen boundary states preserved |
| `04 Character Analysis` | Character syntheses created only after evidence warrants them | seven active-provisional monographs updated through V08 main; Momiji promoted at V07 |
| `05 Specialist Synthesis` | Dense recurring thematic/relationship/form and future adaptation/performance questions | Fukui locality/departure/ordinary youth promoted at V05 and updated through V08 main; other domains deferred |
| `06 Full-Series Synthesis` | Router for the multi-document portfolio and rolling analyzed-to-date integration, conceptually separate from terminal full-series synthesis | router plus mutable current published-corpus synthesis through V08 main; terminal synthesis ineligible |
| `07 Evidence and Indexes` | Git-side cross-volume claim/evidence routing if later needed | not instantiated; source lock plus reading-local locators are sufficient through V08 main |
| `08 Audits and Manifests` | Bootstrap inventory, package reconciliation, and later analytical/source-integrity records | bootstrap manifest plus V01–V02 reconciliation audit |
| `90 Legacy and Superseded` | Materially distinct superseded analysis | not instantiated; no legacy analytical corpus is being imported |

The absence of a directory is intentional. Do not create empty categories merely to make Chiramune resemble another project.

## Post-V08-main integrated state for the rough supplement

The exact V08 main boundary and current rolling revisions live in:

- `02 Sequential Readings/CHIRAMUNE_V07_PROSPECTIVE_FREEZE.md`;
- `02 Sequential Readings/CHIRAMUNE_V07_DEEP_READING.md`;
- `02 Sequential Readings/CHIRAMUNE_V08_MAIN_PROSPECTIVE_FREEZE.md`;
- `02 Sequential Readings/CHIRAMUNE_V08_MAIN_DEEP_READING.md`;
- `03 Longitudinal Ledgers/CHIRAMUNE_REVISION_LEDGER.md`;
- the four thematic/relationship ledgers;
- the Saku, Yuzuki, Asuka, Haru, Yuko, Yua, and Momiji monographs;
- `05 Specialist Synthesis/CHIRAMUNE_FUKUI_LOCALITY_DEPARTURE_AND_ORDINARY_YOUTH_SYNTHESIS.md`;
- `06 Full-Series Synthesis/CHIRAMUNE_CURRENT_PUBLISHED_CORPUS_SYNTHESIS.md`.

The required post-main guardrails are:

- Saku directly names equal romantic pain at the possible futures of Yuko, Yua, Yuzuki, Haru, and Asuka; this five-person enumeration establishes neither rank nor selection and does not include Momiji;
- Saku directly names romantic feeling for Yuzuki and promises an answer by next spring; neither fact identifies her as singular, creates a couple, or resolves the five-person field;
- Yuzuki crosses a sexual consent boundary; Saku's desire, her remorse, and their negotiated repair do not retroactively authorize or erase it;
- the play's best-actress choice is expressly restricted to acting and cannot by itself establish romantic selection; V08 ends before the festival;
- Yuko explicitly starts a new love while Saku's prior refusal remains governing;
- Yua and Asuka directly correct each other's riverbank/kitchen ownership claims, but direct repair with Momiji remains open;
- Yuzuki's 65–51 control strengthens capacity evidence while exposing team injury; Haru remains ace without guaranteed primacy;
- Momiji gains lateral intimacy and rival recognition from Yuzuki and Yuko without full purpose disclosure to Saku or Saku-side romantic reciprocity;
- the self-originated support-request, baseball, Tokyo, and durable basketball-vocation tests remain open;
- preserve all earlier freezes and supplemental component graphs without back-projecting V08;
- treat the rough-illustration collection as separate supplemental production/design evidence and do not double-count rough/final versions as events.

Comparisons to *Oregairu*, *AoButa*, *Classroom of the Elite*, PACTRIH, or other corpus frameworks remain downstream operations. Reconstruct Chiramune on its own evidence first.

## Continuous work order after the V08 main checkpoint

1. Preserve the published V01–V08 main freezes and independently classified V03/V05/V06.5 supplemental checkpoints as distinct source-boundary records.
2. Open the separately titled V08 rough-illustration supplement only after the complete V08 main transaction is committed, pushed, audited, and independently validated.
3. Inspect every supplement page, route rough/final image relationships, and distinguish production annotation from diegetic evidence.
4. Freeze the supplemental disposition before opening V09; do not rewrite V08 main or any earlier historical record.
5. Keep committing and pushing coherent validated checkpoints to `series/chiramune` until every currently admitted source reaches its safe chronological boundary.
6. Do not merge to `main`; integration remains owner-controlled and separately governed.

## Standing abstentions

- No character personality claim is current merely because it appeared in a synopsis, marketing copy, fandom discussion, or an earlier ChatGPT conversation.
- No kanji name reading is inferred by generic CJK transliteration when an official/furigana reading is available or required.
- No retailer-exclusive SS is treated as present unless it is actually acquired and audited.
- No PACTRIH score or other comparative ethical placement is assigned before source-grounded character evidence is sufficient.
- No later source is allowed to rewrite the record of what an earlier prospective reading reasonably inferred at the time.
