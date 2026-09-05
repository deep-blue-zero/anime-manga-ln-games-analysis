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

The Git WUWA root retains **bootstrap generation V0.1**, supplemented on `series/wuthering-waves` by the supplied Aemeath, Denia, and Lynae **pre-AV V0.1** character packets. All three are `active_provisional`; audiovisual analysis remains pending.

### Cartethyia

Cartethyia has an imported **V0.2 active-provisional analytical baseline**:

- canonical current monograph for this imported generation;
- relationship and state ledger;
- ordinary-life and preferences profile;
- speech, voice, and performance profile;
- claim/counterevidence ledger;
- claim-revision ledger;
- compiled character model;
- model-fidelity check.

The imported prose/model artifacts were written against the pinned 3.6.0 semantic boundary and the earlier bounded voice/AV review state. Drive now exposes a later Cartethyia V0.3.1 evidence package and a much larger machine-readable voice census. Therefore the Git analytical baseline is usable but must not be represented as already refreshed against every later evidence projection. Its current router is:

`04 Character Analysis/Cartethyia/WUWA_CARTETHYIA_CURRENT_STATE.md`

### Chisa

Chisa has a mature Drive evidence bridge but no Git-side character monograph in this bootstrap. Her current source package reports 733 accepted solo occurrences, 607 semantic voice lines, 2,429 render associations, and zero human performance annotations. The Git directory contains only an authority/status router until a separate analysis operation is performed.

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

## Corpus architecture

| Layer | Current role | State |
|---|---|---|
| `00 Frameworks and Methods` | Governing analytical and reconstruction protocols | populated, canonical V0.1 |
| `01 Source Lock and Inventory` | Git-side source boundary and Drive pointers | populated, canonical V0.1 |
| `02 Sequential Readings` | Quest/arc/event deep readings | contract present; no readings yet |
| `03 Longitudinal Ledgers` | Cross-reading state, relationship, chronology, world, and uncertainty infrastructure | initialized, active provisional |
| `04 Character Analysis` | Character syntheses, reconstruction profiles, models, and audits | Cartethyia populated; Aemeath/Denia/Lynae pre-AV packets active_provisional; Chisa routed |
| `05 Specialist Synthesis` | Recurring thematic/institutional/media questions | not instantiated until justified |
| `06 Full-Series Synthesis` | Release-bounded title-level synthesis | not instantiated; live-service title incomplete |
| `07 Evidence and Indexes` | Character discovery, claim routing, Drive/Git crosswalk | populated, canonical/active |
| `08 Audits and Manifests` | Bootstrap, corpus, authority, and analytical audit records | populated |
| `90 Legacy and Superseded` | Materially distinct superseded analysis | not instantiated; no current legacy artifact |

The absence of an empty directory is intentional. Git does not need symmetry-only folders.

## Current analytical priorities

1. Maintain the merged bootstrap's routing and integrity metadata as the corpus evolves.
2. Continue the Lynae inaugural reconstruction from its imported pre-AV baseline and canonical Drive package; complete the pending AV evidence pass for all three imported packets.
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
