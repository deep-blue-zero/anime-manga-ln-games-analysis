---
series: YOUJO_SENKI
artifact_type: audit
scope: V2 analytical corpus migration into canonical Google Drive root
generation: V2
status: canonical
source_boundary: Japanese light novels Volumes 01-14; migration provenance from 2026-08-11 generated/File Library artifacts
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
migration_date: '2026-08-22'
---

# YOUJO SENKI V2 — DRIVE MIGRATION AUDIT

## Purpose

This audit records the migration of the mature *Youjo Senki* V2 analytical corpus from the ChatGPT/File Library artifact layer into the canonical analytical Google Drive root.

Canonical locations:

- series root: `17UvtZCM9QBQdFtqKjDsebZfQXsuB2idH`
- V2 analysis folder: `1q1xEv83Ld8KGENT_cZTN3OhAzjoFqzzs`
- Japanese primary-source root: `1s8Ido1uUbAyR-lXstTyOVfoeHaUDop-g`
- Character Modeling and Reconstruction root: `1z-U_tluPeOwMuRIVzEbQOOxrI1cYlMK4`

The V2 literary/full-series synthesis remains the mature analytical authority. The CMR layer is a subordinate `active_provisional` derived-use layer and does not supersede it.

## Exact byte-verified migrations

The following files were reconstructed from standalone File Library artifacts and verified byte-for-byte against the original V2 corpus manifest before upload.

| File | Bytes | SHA-256 | Drive ID |
|---|---:|---|---|
| `00_README_AND_CORPUS_MAP.md` | 17,945 | `dfa52377f583f83aea3b31143ed83d2fe127a6ab5820e92056953302a7e727ac` | `1WaQA0qHSLBaWdQSusP7Pl4011XZChnY0` |
| `01_SERIES_ARCHITECTURE_AND_VOLUME_PROGRESSION.md` | 66,321 | `06fbdaab0ee2faf9a013747bc4f45fabb4b0f7bc1890ed752144d03c54873487` | `1op6rWbk-7YV6dboOazmeixiSoTjvAmfL` |
| `02_TANYA_DEGURECHAFF_CHARACTER_DEEP_DIVE.md` | 49,566 | `3846f3c278adf9ce05d59f98ac8151c28be43cc3866f9f56fcc2e52773075741` | `1lr6DtGMQBQV03v2h5Y-pTXTZlLuCNjQ2` |
| `03_IMPERIAL_PROFESSIONALS_RELATIONSHIPS_AND_COMMAND_CULTURE.md` | 45,538 | `ccf643c63d82f166c49cc910cf20ba0990510ab686a4193ae3ca8f0c038c545a` | `16ofuDPmpjtKWbcoISRSemC8xAZsqg4fn` |
| `04_COUNTERPERSPECTIVES_ENEMIES_ALLIES_AND_PARALLEL_PROFESSIONALS.md` | 56,253 | `554c28b4b5d602ce930af366081180467c5e869224d715b3bbf6d92b08dd7e1c` | `1ZOLENVk6dk9mRmSZ6rGH4sm6EwXfV0T4` |
| `05_POLITICS_INSTITUTIONS_STATECRAFT_AND_WAR_TERMINATION.md` | 78,371 | `26a0660ee137ffe46e1075ec6717cf3658053533a32af0b8fdb63f4a6f0e9080` | `15Pqw2MMmZLuv_ryGp114j3fOKElI15lq` |
| `06_STRATEGY_DOCTRINE_LOGISTICS_AND_ORGANIZATIONAL_LEARNING.md` | 66,406 | `a1e622e6f0cde8cd5eca6f43d5f16767387a7c957525ccad2f38b7ff91d590a9` | `1Luvjb_H0TNW5s9Xad8_5RK02Nfh5kbKO` |
| `07_ETHICS_LAW_AUTONOMY_AND_VIOLENCE.md` | 59,932 | `0d3fbd498e98d2c7f2423fc3a0e621e55db57c162b9cb407381d0b112b805b14` | `1qG-blLXHSgrD-E6foApUwq1qcfMnzBoo` |
| `08_FAITH_BEING_X_MAGIC_TECHNOLOGY_AND_BODILY_AUTHORSHIP.md` | 43,228 | `96012e5d0d7a23f24b2977d03e47e6ab2e50baa218426c73955f6f639fe97343` | `19tCDUUKjF4Qa_MBdUM__2TRF9xX5kjPi` |
| `09_NARRATION_LANGUAGE_HISTORIOGRAPHY_GENRE_AND_MOTIFS.md` | 64,020 | `54f59765f441cfb079215e600f77036ccbf86c86bfea46479858a1421931ef8b` | `1QJmg0Gby7L1QdO63bhw1-ROKRL4ZF-cE` |
| `10_COMPARATIVE_REFERENCE_AND_OPEN_QUESTIONS.md` | 75,512 | `4f611b694b195960768e259dfaf90d2fe044bb18b508c516017bccefdeef6b69` | `1ljhUEbikE93p1oDf8RTklPzjv0QZCzYz` |
| `11_VOLUME_BY_VOLUME_EVIDENCE_LEDGER.md` | 82,221 | `79c533c651380d26a9a037c74270b9a15caed45c436a0fbf4688b810aa55c29e` | `1HrNVDWDwJht_BYZo3PLHsQ4gx9bWUGtf` |

These twelve files total the original core corpus state of 99,955 whitespace-delimited words / 705,313 bytes recorded before the optional bilingual appendix was produced.

## Framework provenance recovered

`FRAMEWORK_MANIFEST.md` was recovered as a standalone File Library artifact and copied to Drive (`1nV2kPOhVempR-B1iecLMx9e8C_vFLs8s`). It records the two governing framework artifacts and their original hashes:

- `Youjo_Senki_Full_Series_Analytical_Method_v1.md` — SHA-256 `a1fcbb0a2ce5365ac80099161aea73ee37891386765ba78987c7c5d03cff9e36`
- `Youjo_Senki_Multi_Document_Synthesis_Architecture_v1.md` — SHA-256 `0bd7481a6df27b336957cd027105f0074838becd970674461f6f956518671300`

The framework manifest is provenance. The framework files themselves were not exposed as standalone byte-recoverable File Library objects during this migration and were therefore not reconstructed from summaries.

## Confirmed V2 package artifacts not byte-recoverable in the current artifact index

The 2026-08-11 completion record establishes that the final V2 package contained **Documents 00-12**, an updated corpus manifest and README, both governing framework documents, a delivery manifest, and checksum files. It records the final archive as approximately 110,900 words across 13 analytical documents and gives ZIP SHA-256:

`614ddc4381d29dd45e40a19f3b7e94553f3370c624db71bc62e089d26ff916f5`

The following final-package byte streams did not surface as independently retrievable artifacts after repeated File Library searches and therefore were **not fabricated or silently regenerated**:

- `12_JAPANESE_ENGLISH_TRANSLATION_AUDIT_LEDGER.md`
- final post-Document-12 `CORPUS_MANIFEST.md`
- final post-Document-12 `00_README_AND_CORPUS_MAP.md` revision
- `Youjo_Senki_Full_Series_Analytical_Method_v1.md`
- `Youjo_Senki_Multi_Document_Synthesis_Architecture_v1.md`
- `DELIVERY_MANIFEST.md`
- `SHA256SUMS.txt` and ZIP checksum sidecar
- final ZIP itself

The missing `12_JAPANESE_ENGLISH_TRANSLATION_AUDIT_LEDGER.md` is nevertheless confirmed to have existed. The completion record describes it as a roughly 10,900-word bilingual appendix through official English Volume 13, tracking `僕/私`, `思想の自由`, `規律`, `理屈`, human-resource vocabulary, `社会契約`, victory terminology, Reich/Heimat, titles/allusions, and stage/dice/liquidation language. It also records three confirmed corrections: V9 `低血圧` = low blood pressure; V10's deadline is about six months, not a year; V11 Chapter I begins September 10, 1927, not September 25. No English Volume 14 comparison was included.

## Authority and retrieval consequence

1. `CURRENT_STATE_AND_CORPUS_MAP.md` at the series root is the current first-read authority for project state.
2. `V2 Analysis/00_README_AND_CORPUS_MAP.md` is an exact frozen core-corpus snapshot from before the optional Document 12 was produced; its statement that Document 12 remained optional/unproduced is therefore historically correct for that snapshot but no longer the final production state.
3. `V2 Analysis/10_COMPARATIVE_REFERENCE_AND_OPEN_QUESTIONS.md` is the compact mature cross-series reference.
4. `V2 Analysis/11_VOLUME_BY_VOLUME_EVIDENCE_LEDGER.md` is the chronological evidentiary spine.
5. `V2 Analysis/02_TANYA_DEGURECHAFF_CHARACTER_DEEP_DIVE.md` is the primary mature Tanya character authority.
6. Exact Japanese wording or unresolved claims should escalate to the separate Japanese V01-V14 source root.
7. The CMR subtree is derived reconstruction infrastructure and generated simulations never become evidence.

## Migration result

The mature V2 **core** corpus (Documents 00-11) is now deterministically available in the canonical analytical Drive root with exact byte/hash verification. The migration is intentionally incomplete only for final-package artifacts whose original bytes are no longer exposed by the currently searchable artifact layer; this audit preserves that gap explicitly rather than substituting reconstructed approximations.
