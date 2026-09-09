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

The Git WUWA root retains **bootstrap generation V0.1**, supplemented on `series/wuthering-waves` by the supplied Aemeath, Denia, and Lynae **pre-AV V0.1** character packets. All three are `active_provisional`; audiovisual analysis remains pending. The owner has adopted all five character packets, including the later Chisa and Cartethyia rebuilds, as current `active_provisional` authority within their stated text/audio scopes; AV-dependent questions remain open.

### Cartethyia

Cartethyia has an imported **V0.2 active-provisional analytical baseline**:

- canonical current monograph for this imported generation;
- relationship and state ledger;
- earlier ordinary-life and preferences profile, now archived under Cartethyia's legacy folder;
- speech, voice, and performance profile;
- claim/counterevidence ledger;
- claim-revision ledger;
- compiled character model;
- model-fidelity check.

The imported prose/model artifacts were written against the pinned 3.6.0 semantic boundary and the earlier bounded voice/AV review state. Drive now exposes a later Cartethyia V0.3.1 evidence package and a much larger machine-readable voice census. Therefore the Git analytical baseline is usable but must not be represented as already refreshed against every later evidence projection. Its current router is:

`04 Character Analysis/Cartethyia/WUWA_CARTETHYIA_CURRENT_STATE.md`

Cartethyia also has an owner-adopted current twelve-document pre-AV rebuild under `active_provisional`. Its newer ordinary-life draft remains at `WUWA_CARTETHYIA_ORDINARY_LIFE_AND_PREFERENCES_PROFILE.md`. The owner-retired older profile is preserved under `04 Character Analysis/Cartethyia/90 Legacy and Superseded/`; the newer profile is current and the archived profile is noncurrent. The newer packet is the current text/audio first read; the V0.2 artifacts retain their earlier-generation scopes.

### Chisa

Chisa now has a twelve-document **CHISA_PRE_AV_REBUILD_V0_1** current provisional packet alongside the original router. The deep dive, evidence/falsification matrix, specialist and reconstructive profiles, prior-baseline reconciliation, AV plan/crosswalk, and fidelity review use `status: active_provisional` and `do_not_use_as_current_authority: false` under the explicit owner adoption. AV completion and full audio profiling remain separate from current authority.

The existing evidence bridge reports 733 accepted solo occurrences, 607 semantic voice lines, 2,429 render associations, and zero human performance annotations. The supplied rebuild reports **2,421 distinct PCM/FLAC identities** underlying those associations. The [Chisa import record](08%20Audits%20and%20Manifests/WUWA_CHISA_PRE_AV_REBUILD_IMPORT.md) records the source hash, exact preservation, and remaining evidence-review limits.

`04 Character Analysis/Chisa/WUWA_CHISA_CURRENT_STATE.md`

### Lynae

Lynae has an imported nine-document pre-AV V0.1 reconstruction baseline; the inaugural end-to-end test remains incomplete pending audiovisual analysis and remaining voice review. Her additive Drive package reports 1,128 accepted solo occurrences, 251 scene contexts, 21 WavesLine records, five favor stories, 64 favor words, and 888 semantic voice lines. Of those lines, 885 have complete four-language media mappings. Collection integrity passed; formal voice completeness remains false because three PhoneMessage lines have unresolved runtime dispatch. Human performance annotations and dedicated audiovisual exports are not yet present.

`04 Character Analysis/Lynae/WUWA_LYNAE_CURRENT_STATE.md`

The original bootstrap created only the Lynae router. The later supplied packet now adds a deep dive, reconstructive profile, evidence/falsification matrix, relationship/state profile, ordinary-life profile, speech/machine-voice profile, AV nomination plan, fidelity/stress test, and packet entrypoint. No completed integrated AV monograph or compiled JSON model is claimed.

### Aemeath and Denia

Each character now has an 11-document pre-AV V0.1 packet, imported byte-for-byte with `active_provisional` status. Start at `04 Character Analysis/Aemeath/WUWA_AEMEATH_CURRENT_STATE.md` or `04 Character Analysis/Denia/WUWA_DENIA_CURRENT_STATE.md`. The packets include deep dives, reconstruction and specialist profiles, evidence/falsification matrices, AV nomination plans, human-retrieval crosswalks, and fidelity/stress tests.

These are analytical imports, not a new evidence acquisition or AV review. The [import record](08%20Audits%20and%20Manifests/WUWA_PRE_AV_CHARACTER_PACKET_IMPORT.md) explains preserved local-draft metadata and provides source hashes.

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

All five packets use the complete current-authority quartet and retain their actual modality coverage. See the [owner adoption record](08%20Audits%20and%20Manifests/WUWA_CHARACTER_PACKET_AUTHORITY_ADOPTION.md). Missing AV alone does not disqualify a text/audio model.

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

`SEQUENTIAL_ANALYSIS_LOCK = OPEN` records this verified governing infrastructure. Narrative-unit work continues to require the canonical narrative deep-reading protocol, exact source scope, and its same-change closeout. The chronology and world/faction ledgers contain bounded Cartethyia findings and explicit gaps; initialization is not a claim of complete story coverage.

## Corpus architecture

| Layer | Current role | State |
|---|---|---|
| `00 Frameworks and Methods` | Governing analytical and reconstruction protocols | populated, canonical V0.1 |
| `01 Source Lock and Inventory` | Git-side source boundary and Drive pointers | populated, canonical V0.1 |
| `02 Sequential Readings` | Quest/arc/event deep readings | contract present; no readings yet |
| `03 Longitudinal Ledgers` | Cross-reading state, relationship, chronology, world, and uncertainty infrastructure | initialized, active provisional |
| `04 Character Analysis` | Character syntheses, reconstruction profiles, models, and audits | Cartethyia populated; Aemeath/Denia/Lynae pre-AV packets active_provisional; Chisa pre-AV packet current provisional |
| `05 Specialist Synthesis` | Recurring thematic/institutional/media questions | not instantiated until justified |
| `06 Full-Series Synthesis` | Release-bounded title-level synthesis | not instantiated; live-service title incomplete |
| `07 Evidence and Indexes` | Character discovery, claim routing, Drive/Git crosswalk | populated, canonical/active |
| `08 Audits and Manifests` | Bootstrap, corpus, authority, and analytical audit records | populated |
| `90 Legacy and Superseded` | Materially distinct retired analysis | instantiated within Cartethyia for the owner-retired older ordinary-life profile |

The absence of an empty directory is intentional. Git does not need symmetry-only folders.

## Current analytical priorities

1. Maintain the merged bootstrap's routing and integrity metadata as the corpus evolves.
2. Continue the Lynae inaugural reconstruction from its imported pre-AV baseline and canonical Drive package; complete the pending AV evidence pass for those three imported packets and harden the current Chisa packet while preserving its declared evidence limits.
3. Generate comprehensive machine voice analysis across all usable Lynae audio before selecting a bounded human-review cohort.
4. Harden the supplied character artifacts only as their evidence warrants, preserving active_provisional status while audiovisual analysis is pending.
5. Update the character index, claim index, longitudinal ledgers, and current-state map in the same change.
6. Use the result to revise—not merely affirm—the WUWA character-folder and reconstruction contracts.

## Non-authority and abstentions

- The Drive normalized `dialogue.jsonl` and story graph are selected-quest projections, not an exhaustive normalized game graph.
- Absence from a selected projection is not evidence of absence from the pinned source.
- Machine acoustic measurements are not emotion, intent, intimacy, or acting labels.
- A dub-specific tendency is not a language-independent personality fact.
- Generated scenarios never become canonical evidence.
- Future patches do not silently revise the 3.6.0 source boundary. They require a new evidence generation or explicitly versioned delta.
