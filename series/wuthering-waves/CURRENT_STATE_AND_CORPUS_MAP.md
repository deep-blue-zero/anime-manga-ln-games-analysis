---
series: WUWA
artifact_type: corpus_map
scope: SOURCE_3_6_0_AND_GIT_BOOTSTRAP
source_boundary: "Wuthering Waves 3.6.0; pinned Arikatsu semantic source commit 353f2eaed119bc9f680eab92807d20ac75a79b40; official zh-Hans, ja, ko, and en text witnesses; installed-client voice evidence; bounded audiovisual witnesses"
generation: V0.1
status: canonical
release_state: mutable_active
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
---

# Wuthering Waves — current state and corpus map

This is the canonical first read for the Git-side Wuthering Waves analytical corpus.

## Authority split

- **GitHub `main` is the analytical authority.** Interpretive claims, methods, readings, ledgers, monographs, model packages, and analytical audits belong here.
- **Google Drive is the primary and deterministic derived-evidence authority.** Raw semantic material, normalized corpora, large scene ledgers, text/voice mappings, FLAC objects, selected audiovisual witnesses, and evidence-release manifests remain in Drive.
- **Local/Codex workspaces are build environments.** They are not authority unless an artifact is promoted through the governed Drive-evidence or Git-analysis route.

Owner-authenticated Drive evidence root: `19ZmRcjKQR3g0lhU1A3sXujsyihhdKs-2`  
First-read evidence map: `1vZRelxjX95N-8O7byuYmQBc8uELyb0ht`  
Base evidence release: `wuwa-drive-evidence-v0.1`

See:

- `00 Frameworks and Methods/WUWA_EVIDENCE_ROUTING_AND_AUTHORITY.md`
- `01 Source Lock and Inventory/WUWA_DRIVE_EVIDENCE_RELEASE_POINTER.md`
- `07 Evidence and Indexes/WUWA_DRIVE_GIT_CROSSWALK.md`

## Current analytical generation

The Git WUWA root retains **bootstrap generation V0.1**, supplemented by **18 owner-adopted current character reconstruction packets** (`0` `draft_noncurrent` character packets remain in the repository), tiered by analytical and audiovisual coverage depth:

- **Three `canonical` character packets (`do_not_use_as_current_authority: false`)**: `Cartethyia` (`27/33` Chapter II EN scene-AV targets resolved + `29`-moment / `116`-render four-dub calibration across her V0.2 baseline and twelve-document rebuild), `Augusta` (`19/32` Chapter II EN scene-AV targets + `8/605` four-dub solo lines / `32` renders + bounded claim/model revisions), and `Iuno` (`21/39` Chapter II EN scene-AV targets + `8/540` four-dub solo lines / `32` renders + bounded claim/model revisions). `canonical` marks current corpus authority within each packet's declared 3.6.0 and Chapter II boundaries, not an all-line voice census or closure of optional/non-main-story content.
- **Six `active_provisional` partial-AV Chapter II packets (`do_not_use_as_current_authority: false`)**: `Brant` (`5/38` AV, `6/606` 4-dub), `Cantarella` (`4/36` AV, `6/845` 4-dub), `Phoebe` (`7/24` AV, `6/476` 4-dub), `Qiuyuan` (`5/27` AV, `5/255` 4-dub), `Shorekeeper` (`2/14` AV, `4/543` 4-dub), and `Zani` (`2/12` AV, `5/912` 4-dub), whose primary Companion, Chapter I, or Segue arcs lie partly outside the Chapter II main-story recording.
- **Nine `active_provisional` text/machine-audio pre-AV packets (`do_not_use_as_current_authority: false`)**: newly promoted `Changli`, `Jinhsi`, `Luuk Herssen`, and `Yinlin` alongside existing `Aemeath`, `Chisa`, `Denia`, `Lynae`, and `Sigrika`. Scene audiovisual observation and human four-dub listening remain open on these nine packets.

The character layer also includes a **V0.2 static visual-design generation** (`status: active_provisional`) for all 18 characters: Aemeath, Augusta, Brant, Cantarella, Cartethyia, Changli, Chisa, Denia, Iuno, Jinhsi, Luuk Herssen, Lynae, Phoebe, Qiuyuan, Shorekeeper, Sigrika, Yinlin, and Zani. Each individualized profile is grounded in direct inspection of three decoded official-client UI rasters tied to the normalized role record: a large head icon, formation art, and activity portrait. The Git artifacts contain analytical prose, machine-readable claims, asset/package locators, hashes, form/skin/state distinctions, uncertainty, and reverse provenance; the 54 PNGs remain restricted outside Git. This bounded layer does not constitute runtime-model reconstruction, rear-view inspection, animation analysis, a complete alternate-skin/form survey, promotional-art coverage, or scene-level audiovisual review.

### Title-wide character visual layer

Start with each character's `03 Audiovisual and Voice/CHARACTER_VISUAL_DESIGN_PROFILE.md`; use the adjacent `CHARACTER_VISUAL_DESIGN_PROFILE.json` for structured claims and `CHARACTER_VISUAL_REFERENCE_MANIFEST.json` for evidence identity and reverse provenance. Sigrika's triplet is one layer deeper, in `03 Audiovisual and Voice/Profiles and Plans/`. Direct visual observations are separated from design–narrative interpretation, counterreadings, and open questions. All 18 visual profiles remain `active_provisional` because the evidence set is intentionally narrow even where the observed details are high-confidence.

The [V0.2 visual-profile publication record](08%20Audits%20and%20Manifests/WUWA_CHARACTER_VISUAL_PROFILE_V0_2_IMPORT.md) binds the 54 Git artifacts to the read-only extraction receipt and documents the raw-media boundary.

### Full 18-character promotion and coverage-depth tiering after Chapter II audiovisual reconciliation

The owner-adopted [authority transition and tiering record](08%20Audits%20and%20Manifests/WUWA_CH2_AV_CHARACTER_PACKET_ADOPTION_2026_11_18.md) and companion [source-backed validation receipt](08%20Audits%20and%20Manifests/WUWA_CH2_CURRENT_SOURCE_VALIDATION_2026_11_19.json) promote all remaining draft packets out of `draft_noncurrent` (`Changli`, `Jinhsi`, `Luuk Herssen`, `Yinlin` -> `active_provisional`), retain `Brant`, `Cantarella`, `Phoebe`, `Qiuyuan`, `Shorekeeper`, and `Zani` at `active_provisional` alongside `Aemeath`, `Chisa`, `Denia`, `Lynae`, and `Sigrika`, elevate `Cartethyia`, `Augusta`, and `Iuno` to `canonical` within their 3.6.0 / Chapter II boundaries, record §15.6 name-and-reference and §5.5.1 self-containment + source-fidelity checks, and regenerate all twelve validator-backed `VALIDATION_REPORT.json` files in place (`3,160` passing checks with `source_crosscheck: passed`). The historical [Chapter II shared AV reconciliation audit](08%20Audits%20and%20Manifests/WUWA_RINASCITA_CH2_SHARED_AV_RECONCILIATION_AUDIT.md) retains its original `draft_noncurrent` / `active_provisional` snapshot statements because those accurately record packet states when the AV pass was first published.

### Chapter II (*Rinascita*) shared audiovisual reconciliation (`WUWA_RINASCITA_CH2_SHARED_AV_V01`)

A bounded multi-character scene-level audiovisual pass over the complete 1080p60 English-dubbed Chapter II *Rinascita* main-story recording witness `WUWA_CH2_FAYATO_1080P60_6076F127` (`105,804.732367 s` / `29:23:24.732`, Prologue `114000026` through Act XI `158800019`) is recorded in the [Chapter II shared AV reconciliation audit](08%20Audits%20and%20Manifests/WUWA_RINASCITA_CH2_SHARED_AV_RECONCILIATION_AUDIT.md), its companion manifest, and the paired [Chapter II four-dub voice ledger](08%20Audits%20and%20Manifests/WUWA_RINASCITA_CH2_FOUR_DUB_VOICE_LEDGER.md). It dispositions all `483` nominated crosswalk rows across the 16 crosswalk-bearing packets (`92` `inspected_resolved`, `13` `not_triggered_optional_in_recording`, `22` `out_of_scope_non_main_story`, `356` `out_of_recording_scope`), reconciles Cartethyia's specialist voice profile, router, crosswalk, matrix, compiled model, and fidelity/revision ledgers (`27/33` targets resolved plus `29`-moment / `116`-render four-dub calibration across `27/786` solo lines + `who=1626` + `who=1633`, falsifying the `ko` midpoint hypothesis while leaving `759/786` solo lines open), applies in-place specialist voice-profile updates (`48` moments / `192` renders) and crosswalk/revision-ledger updates across `Augusta`, `Iuno`, `Phoebe`, `Brant`, `Cantarella`, `Qiuyuan`, `Shorekeeper`, and `Zani` (including bounded claim/model corrections in `Augusta`, `Iuno`, and `Phoebe`), records `0`-spoken-scene scope-boundary crosswalk notes in `Changli`, `Jinhsi`, and `Yinlin` (all subsequently promoted to current authority under the 2026-11-19 tiering above), calibrates `30` four-dub moments (`120` renders) across `20` distinct unmodeled Chapter II entities (`23` speaker entries; `107` moments / `428` `zh-Hans`/`ja`/`ko`/`en` renders total), and indexes `27` multi-character evidence capsules in the restricted dataset outside Git. Full-census comparative four-dub human listening beyond that `107`-moment (`428`-render) calibration cohort, Patch `2.7` Segue `175000000`, Chapter I, `3.x` arcs, and Companion/Side/Event witnesses remain open.

### Cartethyia, Augusta, and Iuno (`status: canonical`)

Cartethyia combines her imported **V0.2 analytical baseline** (monograph, relationship/state ledger, speech/voice/performance profile, claim/counterevidence ledger, claim-revision ledger, compiled model, model-fidelity check) with her twelve-document **CARTETHYIA_PRE_AV_REBUILD_V0_1** packet (`04 Character Analysis/Cartethyia/WUWA_CARTETHYIA_CURRENT_STATE.md`), reconciled against `WUWA_RINASCITA_CH2_SHARED_AV_V01` (`27/33` Chapter II EN scene-AV targets + `29`-moment / `116`-render four-dub calibration; `759/786` solo lines and `6` optional/non-main-story targets open). Her retired older ordinary-life profile remains `historical_legacy` under `04 Character Analysis/Cartethyia/90 Legacy and Superseded/`.

Augusta (`04 Character Analysis/Augusta/WUWA_AUGUSTA_CURRENT_STATE.md`, `19/32` Chapter II scene-AV targets + `8/605` four-dub solo lines + `332` source-crosschecked validation checks) and Iuno (`04 Character Analysis/Iuno/WUWA_IUNO_CURRENT_STATE.md`, `21/39` Chapter II scene-AV targets + `8/540` four-dub solo lines + `612` source-crosschecked validation checks) likewise hold `canonical` status within their declared 3.6.0 / Chapter II boundaries while keeping unreviewed lines and targets explicitly open.

### Partial-AV Chapter II and Pre-AV Character Packets (`status: active_provisional`)

- **Bounded Chapter II AV + four-dub calibrated (`active_provisional`)**: `Brant` (`WUWA_BRANT_CURRENT_STATE.md`), `Cantarella` (`WUWA_CANTARELLA_CURRENT_STATE.md`), `Phoebe` (`WUWA_PHOEBE_CURRENT_STATE.md`), `Qiuyuan` (`WUWA_QIUYUAN_CURRENT_STATE.md`), `Shorekeeper` (`WUWA_SHOREKEEPER_CURRENT_STATE.md`), and `Zani` (`WUWA_ZANI_CURRENT_STATE.md`).
- **Promoted 3.6.0 text/machine-audio packets (`active_provisional`, scene AV and human listening pending)**: `Changli` (`WUWA_CHANGLI_CURRENT_STATE.md`, `610` semantic lines including `18` `runtime_dispatch_unsupported`), `Jinhsi` (`WUWA_JINHSI_CURRENT_STATE.md`, `547` semantic lines including `8` `runtime_dispatch_unsupported`), `Luuk Herssen` (`WUWA_LUUK_HERSSEN_CURRENT_STATE.md`, `719/719` semantic lines), and `Yinlin` (`WUWA_YINLIN_CURRENT_STATE.md`, `439/439` semantic lines).
- **Earlier owner-adopted pre-AV / machine-audio imports (`active_provisional`, scene AV and human listening pending)**: `Chisa` (`WUWA_CHISA_CURRENT_STATE.md`), `Lynae` (`WUWA_LYNAE_CURRENT_STATE.md`), `Aemeath` (`WUWA_AEMEATH_CURRENT_STATE.md`), `Denia` (`WUWA_DENIA_CURRENT_STATE.md`), and `Sigrika` (`WUWA_SIGRIKA_CURRENT_STATE.md`).

## Governing method

Read in this order for new analytical work:

1. `00 Frameworks and Methods/WUWA_ANALYTICAL_METHOD.md`
2. the relevant specialized protocol;
3. `00 Frameworks and Methods/WUWA_EVIDENCE_ROUTING_AND_AUTHORITY.md`
4. `01 Source Lock and Inventory/WUWA_SOURCE_BOUNDARY.md`
5. the relevant character or story evidence bridge in Drive;
6. the narrowest current Git analytical artifact capable of answering the question.

Character reconstruction is governed by:

- `WUWA_CHARACTER_RECONSTRUCTION_PROTOCOL.md`
- `WUWA_CHARACTER_FOLDER_CONTRACT.md`
- `WUWA_MACHINE_VOICE_ANALYSIS_PROTOCOL.md`

Sequential story analysis is governed by:

- `WUWA_NARRATIVE_DEEP_READING_PROTOCOL.md`
- `WUWA_LONGITUDINAL_STORY_ANALYSIS_ARCHITECTURE.md`

All 18 current packets carry `do_not_use_as_current_authority: false` (`3` `canonical`, `15` `active_provisional`) and retain their actual modality coverage. Missing AV alone does not disqualify a text/machine-audio model, and `canonical` status within a declared boundary does not erase open modality gates.

For the next authorized substantive story reading, the [standing team](00%20Frameworks%20and%20Methods/WUWA_LONGITUDINAL_STORY_ANALYSIS_ARCHITECTURE.md#standing-team-for-a-narrative-unit) reconciles its findings in the existing [narrative closeout](00%20Frameworks%20and%20Methods/WUWA_NARRATIVE_DEEP_READING_PROTOCOL.md#closeout).

## Project-initiation state

The existing Git-native bootstrap already supplies the canonical analytical method, synthesis architecture, and the five longitudinal artifacts required by that architecture. This declaration records their verified present state for imported character deep readings under the current initiation policy. It does not claim completed title-wide sequential analysis, claim unperformed audio/AV review, or authorize a new source acquisition.

```yaml
project_initialization:
  governing_method: 00 Frameworks and Methods/WUWA_ANALYTICAL_METHOD.md
  method_status: canonical
  synthesis_architecture: 00 Frameworks and Methods/WUWA_LONGITUDINAL_STORY_ANALYSIS_ARCHITECTURE.md
  architecture_status: canonical
  required_day_one_infrastructure_initialized: true
  required_day_one_infrastructure:
    - 03 Longitudinal Ledgers/WUWA_CHARACTER_STATE_CROSSWALK.md
    - 03 Longitudinal Ledgers/WUWA_RELATIONSHIP_NETWORK_LEDGER.md
    - 03 Longitudinal Ledgers/WUWA_WORLD_AND_FACTION_LEDGER.md
    - 03 Longitudinal Ledgers/WUWA_CHRONOLOGY_LEDGER.md
    - 03 Longitudinal Ledgers/WUWA_OPEN_QUESTIONS_LEDGER.md
  sequential_analysis_lock: OPEN
```

`SEQUENTIAL_ANALYSIS_LOCK = OPEN` records this verified governing infrastructure. Narrative-unit work continues to require the canonical narrative deep-reading protocol, exact source scope, and its same-change closeout. The chronology and world/faction ledgers contain bounded findings and explicit gaps; initialization is not a claim of complete story coverage.

## Corpus architecture

| Layer | Current role | State |
|---|---|---|
| `00 Frameworks and Methods` | Governing analytical and reconstruction protocols | populated, canonical V0.1 |
| `01 Source Lock and Inventory` | Git-side source boundary and Drive pointers | populated, canonical V0.1 |
| `02 Sequential Readings` | Quest/arc/event deep readings | contract present; no readings yet |
| `03 Longitudinal Ledgers` | Cross-reading state, relationship, chronology, world, and uncertainty infrastructure | initialized, active provisional |
| `04 Character Analysis` | Character syntheses, reconstruction profiles, models, audits, and bounded visual-design profiles | all 18 character packets current (`0` `draft_noncurrent`): 3 `canonical` (`Cartethyia`, `Augusta`, `Iuno`) + 6 `active_provisional` partial-AV Chapter II packets (`Brant`, `Cantarella`, `Phoebe`, `Qiuyuan`, `Shorekeeper`, `Zani`) + 9 `active_provisional` text/machine-audio packets (`Changli`, `Jinhsi`, `Luuk Herssen`, `Yinlin`, `Sigrika`, `Chisa`, `Lynae`, `Aemeath`, `Denia`); 18-character V0.2 static visual layer `active_provisional` |
| `05 Specialist Synthesis` | Recurring thematic/institutional/media questions | not instantiated until justified |
| `06 Full-Series Synthesis` | Release-bounded title-level synthesis | not instantiated; live-service title incomplete |
| `07 Evidence and Indexes` | Character discovery, claim routing, Drive/Git crosswalk | populated, canonical/active |
| `08 Audits and Manifests` | Bootstrap, corpus, authority, and analytical audit records | populated |
| `90 Legacy and Superseded` | Materially distinct retired analysis | instantiated within Cartethyia for the owner-retired older ordinary-life profile |

The absence of an empty directory is intentional. Git does not need symmetry-only folders.

## Current analytical priorities

1. Maintain the merged bootstrap's routing and integrity metadata as the corpus evolves.
2. Complete pending scene-level AV evidence passes and stratified four-dub human listening for the `active_provisional` packets (Chapter I / Companion / Segue / `3.x` witnesses, including `Changli`, `Jinhsi`, `Luuk Herssen`, `Yinlin`, `Sigrika`, `Chisa`, `Lynae`, `Aemeath`, and `Denia`), while preserving the distinction between moving-image observations and the bounded static-UI visual profiles.
3. Resolve the static `runtime_dispatch_unsupported` audio gaps in `Changli` (`18` lines at `flow#/3688/0`), `Jinhsi` (`8` lines at `flow#/3722/0`), and `Lynae` (`3` `PhoneMessage` lines), plus `flow#/8416` non-EN runtime dispatch in `Augusta`.
4. Harden `active_provisional` packets toward `canonical` only when direct multimodal coverage and claim reconciliation warrant it.
5. Update the character index, claim index, longitudinal ledgers, and current-state map in the same change.
6. Use empirical edge cases to refine the WUWA character-folder and reconstruction contracts.

## Non-authority and abstentions

- The Drive normalized `dialogue.jsonl` and story graph are selected-quest projections, not an exhaustive normalized game graph.
- Absence from a selected projection is not evidence of absence from the pinned source.
- Machine acoustic measurements are not emotion, intent, intimacy, or acting labels.
- A dub-specific tendency is not a language-independent personality fact.
- Generated scenarios never become canonical evidence.
- A head icon, formation illustration, or activity portrait is authored UI art, not proof of runtime geometry, rear construction, animation behavior, material truth, or unique authorial symbolism.
- Future patches do not silently revise the 3.6.0 source boundary. They require a new evidence generation or explicitly versioned delta.
