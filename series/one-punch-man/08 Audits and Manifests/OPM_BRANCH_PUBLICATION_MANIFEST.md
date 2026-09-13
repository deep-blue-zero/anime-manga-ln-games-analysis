---
series: OPM
artifact_type: manifest
scope: Owner-authorized publication of the V34-complete and V35-interrupted checkpoint
generation: V2
status: active_provisional
source_boundary: V01-V34 closed; V35 notes durable through image 0008; web pilot technical only
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
created: 2026-09-13
---

# One Punch Man — branch publication manifest

## Authorization and boundary

The owner requested committing and pushing generated documents to the new `series/one-punch-man` branch of `deep-blue-zero/anime-manga-ln-games-analysis`, then supplying a hand-off at the stopped point. This supersedes the earlier instruction to wait until V37 before any commit for this checkpoint publication. V01–V34 remain complete; V35 remains a noncurrent, unfrozen draft with saved observations through image 0008. Session-reported viewing of 0009–0024 has no durable notes/receipt and must be reinspected. V36/V37 narrative and the post-V37 web backlog remain unprocessed.

The publication contains source audits, V28–V34 readings and Japanese/register audits, V27 reconciliation and V28–V34 closeouts, cumulative state through V34, the V35 partial source audit/draft, current routing and this hand-off. It also publishes an authored technical pilot report without image payloads. It does not certify the unfinished V28–V37 corpus-wide completion gate or a main merge.

## Reconciliation and preservation

- Original staging baseline: `de8ae99f0792b2c6d714f1f602b76be02a35803a`; OPM tree `70c84b23666cb9e75e515cb25e01da8e33b586ed`.
- Publication base: `82ed5e148dafe6411cce8c671622e7051a8d1c0a`, fetched current main before creating the branch. Every baseline OPM blob was compared with this base; none had upstream drift.
- All 113 unchanged local baseline documents remain untouched. Fifty-one staged analytical documents are imported, plus three publication/continuation documents, for 54 exact authored paths. Unrelated repository files are preserved.
- Complete local source files supply the publication bytes. The current map receives targeted publication-status and recovery updates; V35's draft status is normalized to repository vocabulary `draft_noncurrent` without promotion, and its recovery note is added. Historical prospective freezes, readings, judgments and checkpoint predictions are preserved.
- Historical `workspace_state: local_staged_unintegrated` fields retain their original closeout provenance. The current map records the later branch-publication authorization and takes precedence for present publication routing. These fields do not claim a main merge.
- Manga archives/images, raw acquisition/capture evidence, caches, scripts, verification JSON and `_staging/` remain local. The authored pilot report retains local evidence locations as plain paths and distinguishes capture-time V27 isolation from current V34 authority.

## Verification responsibility

Before commit, verify the exact allowlist, complete diff, authority metadata and source-preserving byte comparison, immutable checkpoint and prospective-region preservation, existing links/character references, approved identities, whitespace and the repository's staged stable-branch author preflight. After normal push, verify the remote branch and repository audit/housekeeping result on the exact final head. The local publication receipts under `_staging/git-publication/` record actual commands, hashes and outcomes; their existence is not a claim that an unperformed check passed. Git history and remote statuses identify the actual publication commit.

V28–V34 individual closeout results and source hashes remain in their existing manifests. Their checks occurred at their respective local boundaries and should not be rerun indiscriminately after later drafts open. The V35 source hash is `160d07bd53253d99b32e168e5b388c608327c0c6c9aa974ec291da8f54e74c9d`; its 207-image archive passed mechanical verification, while semantic lock remains pending.

## Declared publication transformation

The repository preflight prohibits publishing local absolute filesystem paths. Git copies therefore replace only the six reviewed location strings with portable root tokens: `OPM_SOURCE_ROOT` (immutable Japanese sources), `OPM_ANALYSIS_ROOT` (local analysis and cache workspace), `OPM_REPOSITORY_CHECKOUT`, `OPM_ORIGINAL_CONTINUATION_PROMPT` and `OPM_PYTHON`. The analysis-root token covers both path-separator spellings. Exact bindings and unmodified local readings remain in the local workspace; public readers must bind these locations to their own authorized environment. This is source-location normalization, not a change to narrative claims or evidence ordinals.

The source inventory also catches up V35's already-passed mechanical check without advancing semantic authority. Two trailing spaces on added power-ledger rows are removed for whitespace validation. The three new publication documents use LF. These narrow publication fixes are recorded separately from the historical closeouts.

Original prospective hashes remain provenance of the locally frozen regions. Published source-location-normalized regions have the hashes below. Each published region was verified as the exact declared substitution of its hash-verified local region; no other prospective bytes changed. Do not overwrite local freezes with the portable copies or test the old local hash against a normalized publication copy.

| Volume | Original local prospective SHA-256 | Published prospective SHA-256 |
|---|---|---|
| V28 | `12b42b5d8a529ffdaef93d514466bf55110e8aa9603d10a11d3d7ee8ae9c74f7` | `48bcbc231d3a827509d96e5bdb896c38d4081f6026ec0fee2d5dd1f87ed4e633` |
| V29 | `b0fc4b938fc48dc9a2b4d2521047e900c9066bcf8242a54db9f0a4739a2cffe4` | `8f16ffe947e5c5a304f65e05bbc72afdaba671b58605da7f1f5bbe332a411763` |
| V30 | `c36330b90d9d6d12184266115e791fb7a76988baf673e2c0870b8f3b61179cde` | `feb4145843301e6fc8ccb08b7c562a0cfe8d890a3004fa7d7bc5d10edddc67c9` |
| V31 | `41799967b8233ae02d0e5d52b68f441ee02b9a195b98d7219faa7a2ed305576b` | `20d141064db308849b89a30f0ece3fde416ce811f91aebdbbfd6fcdbb00d1890` |
| V32 | `e4eff4738de1897569ccfc8091bdb3d0018a7dd5e1998f1dc2ea526c9b297a73` | `2e290c1af72e92c95f3e578340e62b80c2d119ec17e1c6ff2f1a536703fa2c17` |
| V33 | `263fb7f1a6ab2a202d040e99044d5f8bad4d16ce16eca9acd0a2f759c1e0a1a2` | `138e82a8796cbffa671a583678920e9e57c2468b5016204dce301ddd3089407b` |
| V34 | `27501ce386d1e41d7f3a07e58986dea832a784615cb65b49c32a62ce29178857` | `8bb6510d2ab9a0393515bb9190c4fe701413bc4834c077b4928800e8eec44aa9` |

## Exact authored path allowlist

- `series/one-punch-man/01 Source Lock and Inventory/OPM_SOURCE_INVENTORY.md`
- `series/one-punch-man/01 Source Lock and Inventory/OPM_TANKOBON_CHAPTER_AND_EXTRA_CROSSWALK.md`
- `series/one-punch-man/01 Source Lock and Inventory/OPM_V01-V34_SOURCE_AUDIT.md`
- `series/one-punch-man/01 Source Lock and Inventory/OPM_V28_SOURCE_AUDIT.md`
- `series/one-punch-man/01 Source Lock and Inventory/OPM_V29_SOURCE_AUDIT.md`
- `series/one-punch-man/01 Source Lock and Inventory/OPM_V30_SOURCE_AUDIT.md`
- `series/one-punch-man/01 Source Lock and Inventory/OPM_V31_SOURCE_AUDIT.md`
- `series/one-punch-man/01 Source Lock and Inventory/OPM_V32_SOURCE_AUDIT.md`
- `series/one-punch-man/01 Source Lock and Inventory/OPM_V33_SOURCE_AUDIT.md`
- `series/one-punch-man/01 Source Lock and Inventory/OPM_V34_SOURCE_AUDIT.md`
- `series/one-punch-man/01 Source Lock and Inventory/OPM_V35_SOURCE_AUDIT.md`
- `series/one-punch-man/01 Source Lock and Inventory/OPM_V37_SOURCE_AUDIT.md`
- `series/one-punch-man/02 Sequential Readings/OPM_V28_DEEP_READING.md`
- `series/one-punch-man/02 Sequential Readings/OPM_V29_DEEP_READING.md`
- `series/one-punch-man/02 Sequential Readings/OPM_V30_DEEP_READING.md`
- `series/one-punch-man/02 Sequential Readings/OPM_V31_DEEP_READING.md`
- `series/one-punch-man/02 Sequential Readings/OPM_V32_DEEP_READING.md`
- `series/one-punch-man/02 Sequential Readings/OPM_V33_DEEP_READING.md`
- `series/one-punch-man/02 Sequential Readings/OPM_V34_DEEP_READING.md`
- `series/one-punch-man/02 Sequential Readings/OPM_V35_DEEP_READING.md`
- `series/one-punch-man/03 Longitudinal Ledgers and Checkpoints/Character State/OPM_HERO_CHARACTER_STATE_LEDGER.md`
- `series/one-punch-man/03 Longitudinal Ledgers and Checkpoints/Character State/OPM_INDEPENDENT_CIVILIAN_CHARACTER_STATE_LEDGER.md`
- `series/one-punch-man/03 Longitudinal Ledgers and Checkpoints/Character State/OPM_MONSTER_ANTAGONIST_CHARACTER_STATE_LEDGER.md`
- `series/one-punch-man/03 Longitudinal Ledgers and Checkpoints/Character State/OPM_SAITAMA_CHARACTER_STATE_LEDGER.md`
- `series/one-punch-man/03 Longitudinal Ledgers and Checkpoints/Checkpoints/OPM_CHECKPOINT_A_VALIDATION_LEDGER.md`
- `series/one-punch-man/03 Longitudinal Ledgers and Checkpoints/OPM_CHARACTER_MODEL_READINESS_INDEX.md`
- `series/one-punch-man/03 Longitudinal Ledgers and Checkpoints/OPM_HEROISM_RECOGNITION_RANK_AND_INSTITUTION_LEDGER.md`
- `series/one-punch-man/03 Longitudinal Ledgers and Checkpoints/OPM_MONSTERHOOD_PERSONHOOD_BODY_AND_TRANSFORMATION_LEDGER.md`
- `series/one-punch-man/03 Longitudinal Ledgers and Checkpoints/OPM_OPEN_QUESTIONS_AND_MYSTERY_LEDGER.md`
- `series/one-punch-man/03 Longitudinal Ledgers and Checkpoints/OPM_POWER_TECHNIQUE_LIMITER_GOD_AND_COSMIC_LEDGER.md`
- `series/one-punch-man/03 Longitudinal Ledgers and Checkpoints/OPM_RELATIONSHIP_STATE_LEDGER.md`
- `series/one-punch-man/03 Longitudinal Ledgers and Checkpoints/OPM_SATIRE_GENRE_AND_PUBLIC_NARRATIVE_LEDGER.md`
- `series/one-punch-man/03 Longitudinal Ledgers and Checkpoints/OPM_TECHNOLOGY_ORGANIZATION_AND_HIDDEN_ACTORS_LEDGER.md`
- `series/one-punch-man/03 Longitudinal Ledgers and Checkpoints/OPM_VISUAL_FORM_MOTIF_AND_REDRAW_LEDGER.md`
- `series/one-punch-man/08 Audits and Manifests/OPM_BRANCH_PUBLICATION_MANIFEST.md`
- `series/one-punch-man/08 Audits and Manifests/OPM_TONARI_PRESERVATION_PILOT_REPORT.md`
- `series/one-punch-man/08 Audits and Manifests/OPM_V27_UPDATE_MANIFEST.md`
- `series/one-punch-man/08 Audits and Manifests/OPM_V28_BOOTSTRAP_AUDIT.md`
- `series/one-punch-man/08 Audits and Manifests/OPM_V28_JAPANESE_DIALOGUE_AND_REGISTER_AUDIT.md`
- `series/one-punch-man/08 Audits and Manifests/OPM_V28_UPDATE_MANIFEST.md`
- `series/one-punch-man/08 Audits and Manifests/OPM_V29_JAPANESE_DIALOGUE_AND_REGISTER_AUDIT.md`
- `series/one-punch-man/08 Audits and Manifests/OPM_V29_UPDATE_MANIFEST.md`
- `series/one-punch-man/08 Audits and Manifests/OPM_V30_JAPANESE_DIALOGUE_AND_REGISTER_AUDIT.md`
- `series/one-punch-man/08 Audits and Manifests/OPM_V30_UPDATE_MANIFEST.md`
- `series/one-punch-man/08 Audits and Manifests/OPM_V31_JAPANESE_DIALOGUE_AND_REGISTER_AUDIT.md`
- `series/one-punch-man/08 Audits and Manifests/OPM_V31_UPDATE_MANIFEST.md`
- `series/one-punch-man/08 Audits and Manifests/OPM_V32_JAPANESE_DIALOGUE_AND_REGISTER_AUDIT.md`
- `series/one-punch-man/08 Audits and Manifests/OPM_V32_UPDATE_MANIFEST.md`
- `series/one-punch-man/08 Audits and Manifests/OPM_V33_JAPANESE_DIALOGUE_AND_REGISTER_AUDIT.md`
- `series/one-punch-man/08 Audits and Manifests/OPM_V33_UPDATE_MANIFEST.md`
- `series/one-punch-man/08 Audits and Manifests/OPM_V34_JAPANESE_DIALOGUE_AND_REGISTER_AUDIT.md`
- `series/one-punch-man/08 Audits and Manifests/OPM_V34_UPDATE_MANIFEST.md`
- `series/one-punch-man/08 Audits and Manifests/OPM_V35_CONTINUATION_HANDOFF.md`
- `series/one-punch-man/CURRENT_STATE_AND_CORPUS_MAP.md`
