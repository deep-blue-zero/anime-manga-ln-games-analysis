---
title: Gakuen Idolmaster V2 — Targeted Rebuild Candidates
series: GKM
artifact_type: audit
scope: GAKUEN_IDOLMASTER_V2_TARGETED_AV_DOCUMENTATION_REBUILD_CANDIDATES
generation: V2
status: canonical
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
created: '2026-09-09'
last_updated: '2026-09-09'
source_lock: GAKUMAS V2 Source Lock 1.0
source_boundary: Repository control documents and recovered analytical release archives; no source-media reinspection or new measurements
---

# GKM TARGETED REBUILD CANDIDATES

## 1. Register status and boundary

**Two prospective candidates are open: Hiro and Misuzu. No rebuild, new measurement, or source-media reinspection has been performed by this audit.** This register records the documentary gaps and the evidence required to close them. It does not establish that a historical inspection never happened, nor does it certify that the inspection claimed by a completion report occurred.

The recovered Hiro and Misuzu release ZIPs pass CRC checks, match the existing outer checksum sidecars, and satisfy all ten internal artifact checksums in each package. Their incomplete technical records are present in the original releases. They are therefore original documentation gaps that recovery of these particular ZIPs does not resolve.

The [current-state map](../CURRENT_STATE_AND_CORPUS_MAP.md) remains the project entrypoint. [Source Lock 1.0](GKM_SOURCE_LOCK.md) controls exact Japanese wording and textual continuity. The existing qualitative baselines remain individually reviewable; an unresolved technical certification does not, by itself, identify which qualitative claims require revision. Revisions must follow the affected evidence and claim identifiers.

| Candidate | State | Required documentary outcome |
|---|---|---|
| `GKM-REBUILD-HIRO-01` | PROSPECTIVE — NOT EXECUTED | Resolve two late-Dear source records and the ungenerated source-metric/song-form documentation, or explicitly narrow the unsupported certification |
| `GKM-REBUILD-MISUZU-01` | PROSPECTIVE — NOT EXECUTED | Resolve 27 source records and the empty metric tables in two documents, or explicitly narrow the unsupported certification |

## 2. Hiro: source records and ungenerated technical support

### Evidence and affected files

| Existing artifact | Observed gap or dependency |
|---|---|
| [GKM_PHASE3_HIRO_AUDIOVISUAL_SOURCE_MANIFEST.json](../05_AUDIOVISUAL_ANALYSIS/07_SHINOSAWA_HIRO/GKM_PHASE3_HIRO_AUDIOVISUAL_SOURCE_MANIFEST.json) | 31 of 33 entries are materialized. Dear 021–027 and 028–037 have `local_materialized: false`, null hashes and null probe fields, while their authority notes claim direct inspection |
| [GKM_PHASE3_HIRO_AV_TECHNICAL_METRICS_APPENDIX.md](../05_AUDIOVISUAL_ANALYSIS/07_SHINOSAWA_HIRO/GKM_PHASE3_HIRO_AV_TECHNICAL_METRICS_APPENDIX.md) | Section 1 says `metrics_summary.md` was not generated. Section 2 has a header-only song-form table and two `nan (n=0)` summaries |
| [GKM_PHASE3_HIRO_AV_DELIVERY_AUDIT.md](../05_AUDIOVISUAL_ANALYSIS/07_SHINOSAWA_HIRO/GKM_PHASE3_HIRO_AV_DELIVERY_AUDIT.md) | Records 31/33 locally materialized objects alongside the release's completion claims |
| [GKM_PHASE3_HIRO_AUDIOVISUAL_COMPLETION_REPORT.md](../05_AUDIOVISUAL_ANALYSIS/07_SHINOSAWA_HIRO/GKM_PHASE3_HIRO_AUDIOVISUAL_COMPLETION_REPORT.md) | Claims complete Dear 001–037 coverage; requires reconciliation with the saved source records |
| [GKM_HIRO_AV_EVIDENCE_AND_METRICS_MATRIX.md](../05_AUDIOVISUAL_ANALYSIS/07_SHINOSAWA_HIRO/GKM_HIRO_AV_EVIDENCE_AND_METRICS_MATRIX.md) | Route any resulting source qualification or measured-claim correction to the affected evidence rows |

`metrics_summary.md` is a **promised output explicitly recorded as ungenerated**, not a confirmed lost file. A later completed version or underlying working output may be recoverable, but its existence is not established by the package.

### Prospective scope and acceptance criteria

1. Check for a later completed record or recoverable measurement output before regenerating anything. Bind a recovered object to its release/source identity and retain the original incomplete release as historical evidence.
2. Resolve the two late-Dear identities in Section 4. For each, record either a verified materialization with its byte hash and technical probe, a clearly identified equivalent surrogate with explicit equivalence evidence, or an unresolved status with corresponding limits on completion claims.
3. Account for the source-metric summary and song-form comparison advertised by the appendix. If rebuilding is necessary, document the actual included source set, exclusions, sample counts, software/method parameters and interpretation limits. Replace empty/undefined results with supported values or an explicit decision not to promote that measurement layer. Repair the ungenerated filename reference consistently with the chosen delivery form.
4. Audit only claims that depend on the disputed late-Dear inspection or missing quantitative support. Synchronize the manifest, appendix, evidence matrix and completion/audit wording. Amend the baseline or addendum only where a supported claim transition requires it.

The former `みちなるひろがる` song-commu gap is already closed through the [China source manifest](../05_AUDIOVISUAL_ANALYSIS/06_KURAMOTO_CHINA/GKM_PHASE3_CHINA_AUDIOVISUAL_SOURCE_MANIFEST.json), source `AV-CHINA-010`. It is outside this candidate's pending source scope.

## 3. Misuzu: acquisition accounting and empty technical tables

### Evidence and affected files

| Existing artifact | Observed gap or dependency |
|---|---|
| [GKM_PHASE3_MISUZU_AUDIOVISUAL_SOURCE_MANIFEST.json](../05_AUDIOVISUAL_ANALYSIS/11_HATAYA_MISUZU/GKM_PHASE3_MISUZU_AUDIOVISUAL_SOURCE_MANIFEST.json) | All 27 entries are `listed_not_materialized`; filenames, hashes and technical measurements remain null |
| [GKM_PHASE3_MISUZU_AV_TECHNICAL_METRICS_APPENDIX.md](../05_AUDIOVISUAL_ANALYSIS/11_HATAYA_MISUZU/GKM_PHASE3_MISUZU_AV_TECHNICAL_METRICS_APPENDIX.md) | Both the source-level and Dear-segment metric tables contain only headers |
| [GKM_MISUZU_AV_EVIDENCE_AND_METRICS_MATRIX.md](../05_AUDIOVISUAL_ANALYSIS/11_HATAYA_MISUZU/GKM_MISUZU_AV_EVIDENCE_AND_METRICS_MATRIX.md) | Repeats the two empty metric tables after 43 qualitative claim rows |
| [GKM_PHASE3_MISUZU_AV_DELIVERY_AUDIT.md](../05_AUDIOVISUAL_ANALYSIS/11_HATAYA_MISUZU/GKM_PHASE3_MISUZU_AV_DELIVERY_AUDIT.md) | Says Dear 021–027 was acquired through a raw/streaming route and is present, conflicting with the unmaterialized manifest row |
| [GKM_PHASE3_MISUZU_AUDIOVISUAL_COMPLETION_REPORT.md](../05_AUDIOVISUAL_ANALYSIS/11_HATAYA_MISUZU/GKM_PHASE3_MISUZU_AUDIOVISUAL_COMPLETION_REPORT.md) | Claims complete inspection and readiness; saved acquisition and metric records do not substantiate the full certification |

The mismatch establishes uncertainty in the saved documentation. It does not establish that all 27 source videos were absent from the historical workspace or that all qualitative readings were unperformed.

### Prospective scope and acceptance criteria

1. Resolve the manifest's 27 existing source identities, retaining their individual source classes and shared-object identities. Seek completed acquisition/measurement records first. Record verified hashes, sizes and technical properties for actual materializations; identify substitutes explicitly and preserve unresolved states where verification is unavailable.
2. Reconstruct only the advertised, supportable source-level and Dear-segment measurement layer if no completed output can be recovered. Record chapter boundaries and their derivation. Label modeled or inferred boundaries; do not present equal-duration segmentation as exact chapter timing.
3. Populate or explicitly retire the two empty table responsibilities consistently in both the appendix and evidence matrix. Document measurement scope and limits, including speaker mixture, BGM, effects, silence and uploader processing.
4. Review the 43 qualitative claim rows for dependencies on unresolved source inspection or newly produced measurements. Preserve unaffected claims. Reconcile the completion and delivery-audit certification with the resulting evidence state.

The three explicitly deferred solos — `標`, physical-release Misuzu `ENDLESS DANCE`, and Misuzu `ガラクタロード` — remain separate nonblocking backfills. They are not part of these 27 identities and do not justify expanding this candidate automatically.

## 4. Source-identity scope for record reconciliation

The two candidates concern **29 distinct source identities: two Hiro and 27 Misuzu**. The linked source manifests preserve the recorded source labels, classes, properties and retrieval identities. Missing filenames, hashes and technical fields are part of the reconciliation scope; a null field does not supply that evidence. The stable keys below support exact lookup through `sources[*].drive_id`; manifest order or a matching title alone is not an identity check.

| Character | Bounded source role | Manifest `drive_id` |
|---|---|---|
| Hiro | Dear 021–027 | `1EDx0YyXW11f6CNg2Too0fh-7jpaEVU9Q` |
| Hiro | Dear 028–037 | `1Toi0yHcoq0jV0GMcA4JalcrlLMbnFxQO` |
| Misuzu | Dear 001–010 | `1Fw_4i3PsiFG-qE3FcpTNPQEH7ZwcVEkd` |
| Misuzu | Dear 011–020 | `1NyhdO7zo56LTuHdfmfV2kznkr7o8IEqD` |
| Misuzu | Dear 021–027 | `149ubZq2LgWA1zuE4U8dICF0X9bZvWv5w` |
| Misuzu | Dear 028–037 | `1zZaheh3YRcrXMFCcWQIS-_Pxd32m3ChE` |
| Misuzu | ツキノカメ commu | `1zLIbXE_fU7Me1O3SiDs7GE0nKwRms7zz` |
| Misuzu | Campus mode!! commu | `1-MzZgO0DWfS-6F6QzyxB8-jVU00MLf2g` |
| Misuzu | Superlative commu | `1nN2PZIV2tV04PlGtsRTmXv3wKHAkVDYq` |
| Misuzu | VEIL commu | `1Mp9ze1ECRHV99ZKYEbWDF4lPDDonuf8_` |
| Misuzu | Star-mine commu | `1daR8DowUeKrFiEHPvHfOA_CHkOaZHgoO` |
| Misuzu | ツキノカメ 3DMV | `1WmrTOKijFtOCAUZeN_T361MXAx6SBgDC` |
| Misuzu | ツキノカメ authored MV | `1yZf5-OSc870QyVOWvfMrwse1rT3ide5j` |
| Misuzu | Campus mode!! 3DMV | `17qwFKYPq9dt5O9O8L-aWnu3d5zhNZRN0` |
| Misuzu | Superlative 3DMV | `1_TvGBz4HD-xZeysP98HQyNKLXH9RtMyD` |
| Misuzu | Superlative full mix | `1yQv_fbuqPScYz1q8haAT-Bv4HJv-CTNO` |
| Misuzu | VEIL 3DMV | `1IcGLjifbxfTFEeS9T429VS-rJWPIT-60` |
| Misuzu | VEIL authored MV | `1f-LzucKPa0x6XuAN7wvoqwM4FG5Fao11` |
| Misuzu | Begrazia Star-mine 3DMV | `1UyUsSr7ZUed6Kh6oHtIsmyjo4GiWvLTo` |
| Misuzu | Begrazia Star-mine authored MV | `1emxDRAvHC46s-v0x4eYFW1pCjdDGvIM9` |
| Misuzu | ENDLESS DANCE performance | `170-Xv0Fu8C_tZsuJd8zPOD6eMoQzVZie` |
| Misuzu | 初 3DMV | `16up-So-St6oIqDkLO8fO5hmDcp675ras` |
| Misuzu | ヨルニテ authored MV | `1Dnsksn6TEnzualJKSXeZEkzSMqoylzuv` |
| Misuzu | ミラクルナナウ performance | `1hoOWfl9Xf-XefaIRyTskrcUdHiQeOrNa` |
| Misuzu | Howling over the World solo performance | `1FD-G-EejV1b4YCNwfXdiTs4MC1y_fh4R` |
| Misuzu | がむしゃらに行こう！ performance | `14TF8iaQLD4mibJIlLy1UZmx43m4LffTM` |
| Misuzu | 初 alternate/full mix | `1vWmkHR3kPkpr5Vu_EVbPbDEtBAzsLW4N` |
| Misuzu | Ume/Misuzu/Sena Howling over the World full mix | `1RKfLuzy0LHXCOwYry2Dtv9XPAnngly55` |
| Misuzu | たいせつなもの contrast source | `1PfUQwi0zPWIIZUqnjfgjigMEhv4mBPx1` |

A Drive identity identifies the recorded object, not proof of current access, unchanged bytes, or completed inspection. Hash the materialization actually used. For a re-encode or surrogate, retain both identities and state which narrative span, image content and audio comparison establish equivalence; filename similarity and equal duration alone are insufficient. Preserve A1 textual locators and distinguish authored MV, rendered performance, voiced commu and full-mix evidence.

Full-mix acoustic values do not isolate a performer's voice; frame-difference and edit proxies do not establish narrative meaning. Any rebuilt output must state the method, input identity, sample/segment boundaries and limitations needed to assess its claim. Raw media, extracted audio/frames and source transcripts remain outside Git's analytical authority. Preserve immutable release hashes as historical checksums rather than overwriting them to fit revised files.

## 5. Disposition across the 13 playable characters

This table records the documentary screen, not a fresh verification of source media. A populated table or recorded hash supports recoverability and accounting; it does not independently prove every associated interpretation.

| Character | Evidence at review | Disposition |
|---|---|---|
| Saki | 19/19 media hashes; populated evidence/metric tables; missing package members recovered | Recovery integration; no technical rebuild warranted by this audit |
| Temari | 26/26 source hashes; current dialogue and music data recovered; predecessor music JSON/CSV differ materially | Restore current-release data and preserve predecessor provenance; no regeneration needed to resolve that version mismatch |
| Kotone | 25/27 media hashes; Dear 011–020 explicitly text-aligned/unmaterialized and GO MY WAY!! performance explicitly metadata-only | Preserve bounded source qualifications; optional targeted inspection remains separate |
| Mao | 24/24 source hashes; populated appendix; missing supporting exports recovered | Recovery integration; no technical rebuild indicated |
| Lilja | 22/22 canonical source hashes; populated appendix and exports; full release recovered | Release/provenance integration and separate map/ledger formulation review; no technical rebuild indicated |
| China | 22/22 physical-source hashes for 21 logical objects plus a supplement; populated appendix | Correct routing/count summaries where inconsistent; no technical rebuild indicated |
| Hiro | Two unmaterialized source records; ungenerated summary and empty song-form table | `GKM-REBUILD-HIRO-01` remains prospective |
| Rinami | 27/27 source hashes; populated R2 appendix and delivery audit | Reference corrected to existing R2 evidence; separately named file is unverified and carries no collection or rebuild action |
| Sumika | 22 logical sources; late-Dear surrogate has its own nested hash/probe; populated appendix; exports recovered | Preserve original/surrogate identities and integrate recovery; no technical rebuild indicated |
| Ume | 21/21 source hashes; populated appendix; five exports recovered | Recovery integration; no technical rebuild indicated |
| Misuzu | 27 unmaterialized rows and empty tables in two artifacts | `GKM-REBUILD-MISUZU-01` remains prospective |
| Sena | 33/33 materialized source hashes; 12 selected-song and eight Dear-proxy rows | Existing inline measurement responsibility is populated; no technical rebuild indicated |
| Tsubame | 21/21 source hashes: 14 canonical objects and seven excerpts; populated audio table; two exports recovered | Recovery integration and exact filename routing; no technical rebuild indicated |

### Rinami routing responsibility

The current-state map previously named `GKM_PHASE3_RINAMI_R2_HIGH_RESOLUTION_REINSPECTION_AUDIT.md`, which was not recovered as a separate file. The existing [R2 delivery audit](../05_AUDIOVISUAL_ANALYSIS/08_HIMESAKI_RINAMI/GKM_PHASE3_RINAMI_AV_DELIVERY_AUDIT.md) and [R2 technical appendix](../05_AUDIOVISUAL_ANALYSIS/08_HIMESAKI_RINAMI/GKM_PHASE3_RINAMI_AV_TECHNICAL_METRICS_APPENDIX.md) already record the upgraded Dear source qualities and D03/D04 elementary-audio-stream continuity. The current-state map now routes this responsibility to those existing documents and the R2 README. User-supplied excerpts of the generating conversation show no separately named audit link, and their final R2 ZIP hash matches the recovered archive (`62603b68f5fc3dee9192d7c1e527046a9290c4375409874350d16ed40e8f9ea5`). Neither inspected release lists this file in its members or checksum inventory. These excerpts are not a complete session export and do not prove that no such file ever existed. The supported disposition is **LIKELY STALE / UNVERIFIED FILENAME REFERENCE — NO FURTHER COLLECTION ACTION**. No missing analytical responsibility or new reinspection is inferred.

### Temari recovery responsibility

The recovered current-release `GKM_TEMARI_MUSIC_SIGNAL_METRICS.json` and `GKM_TEMARI_DIALOGUE_SCENE_SIGNAL_METRICS.json` supply the current generation's data. The prior music JSON/CSV and selected-scene proxy files represent a different measured generation. Restore their correct authority routing and retain identified predecessor evidence. The generation mismatch is not a reason to repeat the source analysis.

## 6. Separate future work

Rinha's targeted AV request/baseline and subsequent dossier remain planned Phase 6 work under the [Rinha evidence matrix](../06_RELATIONSHIP_AND_ENSEMBLE_SYNTHESIS/GKM_KAYA_RINHA_EVIDENCE_MATRIX.md) and [source crosswalk](../06_RELATIONSHIP_AND_ENSEMBLE_SYNTHESIS/GKM_KAYA_RINHA_SOURCE_CROSSWALK.md). They are not lost deliverables recovered by these releases, are not a fourteenth playable-character baseline, and are outside the two rebuild candidates above.

Future reviews should update a candidate's state only with cited recovery or execution evidence, list affected claim transitions, and record the acceptance result. Age, folder asymmetry, missing optional physical-release solos, or an old release checksum differing from a later living document does not independently establish a rebuild requirement.
