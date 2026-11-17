---
title: "Revue Starlight RS-AV-R2-GEMINI-CARBON — Noncurrent Checkpoint Archive (CP16, CP17A, CP18)"
artifact_id: "RS_AV_R2_CHECKPOINTS_PUBLICATION_README"
artifact_type: "publication_provenance"
generation: "RS-AV-R2-GEMINI-CARBON"
status: draft_noncurrent
supersedes: []
superseded_by: []
do_not_use_as_current_authority: true
do_not_use_as_literary_evidence: true
---

# Noncurrent `RS-AV-R2-GEMINI-CARBON` Checkpoint Archive (`CP16`, `CP17A`, `CP18`)

This subdirectory publishes complete, privacy-normalized archival copies of all `37` pure-text Markdown and JSON artifacts from the standalone `RS-AV-R2-GEMINI-CARBON` native-audiovisual reanalysis across its three frozen checkpoints. It contains **zero** copyrighted video, audio, extracted frames, or bulk subtitle files.

All files under `checkpoints/RS-AV-R2-GEMINI-CARBON/` carry `status: draft_noncurrent` and `do_not_use_as_current_authority: true`. Neither these checkpoints nor the preserved V1 synthesis unilaterally overrides the other; for current canonical authority, consult [CURRENT_STATE_AND_CORPUS_MAP.md](../../CURRENT_STATE_AND_CORPUS_MAP.md) and the reviewed [V2 audiovisual reconciliation](../../06%20Evidence%20and%20Indexes/16_ANIME_AV_RECONCILIATION_V2.md).

## Checkpoint topology and immutable local commit bindings

| Subdirectory | Checkpoint | Original local commit | Files | Scope and epistemic horizon |
| :--- | :--- | :--- | ---: | :--- |
| [CP16_independent_freeze/](CP16_independent_freeze/07_freeze/RS_AV_R2_IMMUTABLE_FREEZE_MANIFEST.md) | `CP16` (`CP16_IMMUTABLE_FREEZE`) | `224c52786b9b5a1d5edd6ce203bfb0714305627e` (tree `e45cae165d93b70b00dba20c690f97b094e3157d`) | `30` | Pre-exposure independent native-AV run (`TV01`–`TV12`, `OVA01`–`OVA03`, `2021` sequel film; `corpus_exposure: false`), with disclosed pretraining familiarity noted on `TV06`. |
| [CP17A_comparative_audit/](CP17A_comparative_audit/README.md) | `CP17A` | `724f8fb0fd79705fa3f1c558851d29b12dd2de1a` | `3` | First post-exposure symmetric comparison, self-audit, and integrator handoff against V1 at `0bae19f328c3fdef82047e5753568fbb8478daed`. |
| [CP18_track_c_reconciliation/](CP18_track_c_reconciliation/README.md) | `CP18` | `98115bee1a9ce0a7e50bd83c0f38ced130cea4b8` | `4` | Post-freeze Track C V2 reconciliation handoff (`REC-01`–`REC-22`), including targeted `TV05` and `OVA03` primary-source rechecks. |

## Provenance and technical normalization

The original commits (`224c5278...`, `724f8fb0...`, `98115bee...`) live in an offline local Git repository and are intentionally not Git ancestors in this public repository because historical workstation path strings cannot be published under `governance/AGENT_ROUTING.md` (§4.1). In these publication derivatives, private filesystem paths are deterministically replaced with relative repository links or `urn:rs-av-r2:` logical witness aliases, and noncurrent YAML/JSON authority headers and UTF-8/LF/NFC formatting are enforced without altering any analytical claim, timestamp, acoustic measurement, or Japanese quotation.

[PUBLICATION_MANIFEST.json](PUBLICATION_MANIFEST.json) records the exact `original_commit`, `original_blob`, `original_bytes`, `original_sha256`, `publication_bytes`, and `publication_sha256` for all `37` artifacts alongside [SOURCE_BOUNDARY.json](SOURCE_BOUNDARY.json). Embedded self-hashes inside historical freeze manifests (`07_freeze/`) continue to record the original unnormalized local blob digests.

## Primary entrypoints inside the archive

- **CP16 syntheses and ledgers:**
  - [Full Animated-Corpus Synthesis](CP16_independent_freeze/05_full_synthesis/RS_AV_R2_FULL_ANIMATED_CORPUS_SYNTHESIS.md)
  - [TV-Only Synthesis (Episodes 1–12)](CP16_independent_freeze/02_tv_synthesis/RS_AV_R2_TV_ONLY_SYNTHESIS.md)
  - [OVA-to-TV Supplement (#1–#3 99.419)](CP16_independent_freeze/03_ovas/RS_AV_R2_OVA_TO_TV_SUPPLEMENT.md)
  - [2021 Theatrical Sequel Monograph](CP16_independent_freeze/04_movie/RS_AV_R2_MOVIE_MONOGRAPH.md)
  - [Major Claim & Horizon Revision Register (CLM-0001..0035)](CP16_independent_freeze/06_ledgers/RS_AV_R2_MAJOR_CLAIM_AND_REVISION_REGISTER.md)
  - [Source & Execution Inventory](CP16_independent_freeze/00_inventory/RS_AV_R2_SOURCE_AND_EXECUTION_INVENTORY.md)
- **CP17A comparative audit:** [Symmetric Comparative Claim Audit](CP17A_comparative_audit/RS_AV_R2_SYMMETRIC_COMPARATIVE_CLAIM_AUDIT.md)
- **CP18 Track C handoff:** [Track C V2 Reconciliation Handoff](CP18_track_c_reconciliation/RS_AV_R2_TRACK_C_V2_RECONCILIATION_HANDOFF.md) and [REC-01..REC-22 Claim Ledger](CP18_track_c_reconciliation/RS_AV_R2_V2_CLAIM_BY_CLAIM_RECONCILIATION_LEDGER.md)
