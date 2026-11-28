---
title: Love Live! Superstar!! — Multi-Document Analysis and Synthesis Architecture V2
series: LLS
artifact_type: synthesis_architecture
scope: TV S1E01-S3E12
generation: V2.4
version: '2.4'
date: '2026-11-26'
status: canonical
architecture_status: Paired architecture for LoveLiveSuperstar_Analytical_Method_V2.md
source_boundary: Japanese-audio television corpus; sequential semantic seal applies
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
do_not_use_as_literary_evidence: true
---

# Love Live! Superstar!! — Multi-Document Analysis and Synthesis Architecture V2

## 0. Purpose

This document defines where analytical work belongs, how duplication is controlled, what is frozen during the sequential pass, and how the final three-season synthesis should be assembled.

The method answers:

> **How should evidence be read?**

This architecture answers:

> **Where should each question live, when should it be written, and how should later evidence revise earlier conclusions without destroying provenance?**

Governing architectural principle:

> **Every major analytical problem receives one primary home. Other documents may cross-reference it, but should not reproduce the full argument.**

A second principle:

> **Sequential close reading and retrospective synthesis are distinct products.**

A third principle:

> **Season boundaries are epistemic checkpoints, not merely folders.**

## 0.1 Authority, adoption and the single entrypoint

The analytical root is `series/love-live-superstar/`, with Git-primary authority through reviewed `main`. The one canonical entrypoint remains [LLS_CURRENT_STATE_AND_CORPUS_MAP.md](../01%20Source%20Lock%20and%20Inventory/LLS_CURRENT_STATE_AND_CORPUS_MAP.md). External Drive bundles and locally accessible source media remain evidence, not competing analytical write surfaces. Branch candidates are proposed changes until integrated.

V2.4 retains the governing method, five cumulative ledgers, accepted episode readings, frozen checkpoints and the fourteen planned specialists. It adds the [continuous-AV companion](LoveLiveSuperstar_Continuous_AV_Companion_Method_V2.md), [reconciliation profile](LoveLiveSuperstar_AV_Reconciliation_Profile_V2.md), and [execution plan](../07%20Audits%20and%20Manifests/LLS_V2_4_AV_EXECUTION_PLAN.md). The [initiation policy](../../../governance/source-policies/MANGA_ANIME_PROJECT_INITIATION_AND_ARCHITECTURE_POLICY.md), [topology policy](../../../governance/source-policies/MANGA_ANIME_EXECUTION_TOPOLOGY_AND_CAPABILITY_ROUTING_POLICY.md) and [continuation policy](../../../governance/source-policies/MANGA_ANIME_SEQUENTIAL_EXECUTION_SCOPE_AND_CONTINUATION_POLICY.md) govern prospective adoption and execution. Current framework metadata does not relabel historical readings as V2.4 products.

The root opts into the prospective initiation contract through its routing descriptor. The entrypoint records a CLOSED preparation gate; this is not a terminal closure or a new byte seal over historical readings. No independent AV episode has been inspected or accepted by this amendment. Existing admitted-source corrections and the musical backfill can proceed within their own authorized scope while the preparation gate remains closed. A new substantive reread or source extension requires truthful OPEN initialization and an actual bounded execution record. The older S3E09 continuation hold remains a separate, explicit dependency.

---

# I. Repository directory plan

This is a responsibility plan, not a claim that every listed artifact exists. Use the current entrypoint for materialization and coverage. Retain mature paths; create a planned output only when its responsibility has actual work. Source manifests already use the `LLS_PHASE0_*` names below. New V2.4 inspection and claim records are initialized for the coming work, with no invented findings.

```text
series/love-live-superstar/
├── 00 Frameworks/
│   ├── LoveLiveSuperstar_Analytical_Method_V2.md
│   ├── LoveLiveSuperstar_Multi_Document_Architecture_V2.md
│   ├── LoveLiveSuperstar_Continuous_AV_Companion_Method_V2.md
│   └── LoveLiveSuperstar_AV_Reconciliation_Profile_V2.md
├── 01 Source Lock and Inventory/
│   ├── LLS_CURRENT_STATE_AND_CORPUS_MAP.md
│   ├── LLS_PROJECT_CHANGELOG.md
│   ├── LLS_PHASE0_CORPUS_INVENTORY_V1.md
│   ├── LLS_PHASE0_GLOBAL_SOURCE_LOCK_V1.md
│   └── LLS_PHASE0_* source-lock and manifest files
├── 02 Episode Deep Readings/
│   ├── Season 1/
│   │   └── LLS_S1E01_DEEP_READING_V2.md ... LLS_S1E12_DEEP_READING_V2.md
│   ├── Season 2/
│   │   └── LLS_S2E01_DEEP_READING_V2.md ... LLS_S2E12_DEEP_READING_V2.md
│   ├── Season 3/
│   │   └── LLS_S3E01_DEEP_READING_V2.md ... LLS_S3E12_DEEP_READING_V2.md
│   └── Independent AV V2.4/ (planned noncurrent candidate readings)
├── 03 Season Checkpoints/
│   ├── LLS_SEASON1_FROZEN_CHECKPOINT.md
│   ├── LLS_SEASON2_FROZEN_CHECKPOINT.md
│   ├── LLS_SEASON3_END_STATE_CHECKPOINT.md
│   ├── checkpoint_delta_files/
│   └── Independent AV V2.4/ (planned independent freezes)
├── 04 Retrospective Music and Performance/
│   ├── episode_addenda/
│   ├── song_performance_ledger/
│   └── score_sound_recurrence_index/
├── 05 Specialist Synthesis/
│   ├── character_and_relationship/
│   │   └── monographs/ (one current portrait per qualified subject and boundary)
│   ├── ensemble_cohort_succession/
│   ├── institution_competition_school/
│   ├── music_performance_voice/
│   ├── visual_spatial_motifs/
│   └── ethics_identity_future/
├── 06 Evidence and Indexes/
│   ├── LLS_EPISODE_EVIDENCE_LEDGER.md
│   ├── LLS_PRIMARY_SOURCE_LOCATOR_AND_CLAIM_REVISION_LEDGER.md
│   ├── LLS_CHARACTER_STATE_LEDGER.md
│   ├── LLS_CHARACTER_BEHAVIOR_AND_DECISION_LEDGER.md
│   ├── LLS_CHARACTER_VOICE_MODEL_LEDGER.md
│   ├── LLS_RELATIONSHIP_CONDITIONING_MATRIX.md
│   ├── LLS_MUSICAL_DRAMATURGY_LEDGER.md
│   ├── LLS_AV_EVIDENCE_AND_RECONCILIATION_INDEX.md
│   ├── LLS_JAPANESE_DIALOGUE_AND_ADDRESS_INDEX.md
│   ├── LLS_SONG_AND_PERFORMANCE_INDEX.md
│   ├── LLS_VISUAL_MOTIF_AND_CALLBACK_INDEX.md
│   └── machine_readable_indexes/
├── 07 Audits and Manifests/
│   ├── LLS_V2_4_AV_EXECUTION_PLAN.md
│   ├── LLS_CHARACTER_MONOGRAPH_QUALIFICATION.md
│   ├── duplication_audit/
│   ├── contradiction_audit/
│   ├── locator_validation/
│   ├── corpus_manifest/
│   └── final_release_checksums/
└── 08 Full-Series Synthesis and Release/
    ├── core_synthesis_documents/
    ├── comparative_reference/
    └── final_release_package/
```

---

# II. Production order

The production order is not the same as the final reader order.

1. Freeze source corpus and naming.
2. Complete Season 1 sequential readings. For each episode: fetch/unpack the Drive bundle locally, complete the audiovisual/acoustic reading, update all applicable model/evidence ledgers, verify durable analytical persistence, then clean only task-owned redundant local source copies before advancing. The current persistence route is Git; original Drive-era execution remains historical provenance.
3. Freeze Season 1 checkpoint.
4. Complete Season 2 sequential readings with the original V2.2 fetch → local analysis → model-ledger update → readback → cleanup lifecycle; use the current Git-primary route for future work.
5. Write Season-2 pressure deltas against the frozen Season-1 checkpoint.
6. Freeze Season 2 checkpoint.
7. Complete Season 3 sequential readings through **S3E08** under V2.2, then impose a deliberate continuation lock before S3E09.
8. Upgrade method/architecture to V2.3 and create `LLS_MUSICAL_DRAMATURGY_LEDGER.md` as canonical mutable infrastructure under `06 Evidence and Indexes`.
9. Backfill musical dramaturgy **sequentially from S1E01 through S3E08**, using existing canonical episode artifacts as retrieval/hypothesis layers and reacquiring primary AV evidence proportionally for M2/M3 events. Frozen season checkpoints are not rewritten; claim pressure is recorded by transition state.
10. Run a musical-dramaturgy integration audit at S3E08. Only after the ledger backfill boundary reaches S3E08 and the audit is verified may the **S3E09 continuation lock be removed**.
11. Resume S3E09–S3E12 only after that hold is removed and execution is authorized, using the current V2.4 method family, required independent participation, and musical-dramaturgy write-through during each episode lifecycle.
12. Freeze Season-3 end-state checkpoint.
13. Complete retrospective **cross-episode** music/performance work that remains necessary beyond the canonical ledger; basic episode-local audio inspection should already be present in canonical episode files.
14. Consolidate evidence/locator ledgers.
15. Draft specialist syntheses.
16. Draft full-series architecture and final thematic synthesis.
17. Run contradiction, duplication, and locator audits.
18. Produce release package.

Why this order?

> **Chronology first → frozen understanding → later pressure → specialist consolidation → retrospective full-series argument.**

The `04 Retrospective Music and Performance` lane remains the **working/reanalysis lane**: episode addenda, bounded AV re-audits, comparative song/score work, recurrence studies, and improved-tooling analysis. It is not the final authority for longitudinal musical state. `06 Evidence and Indexes/LLS_MUSICAL_DRAMATURGY_LEDGER.md` is the canonical cumulative home for verified music-as-action findings; `05 Specialist Synthesis/.../09_MUSIC_SONG_PERFORMANCE_AND_DRAMATURGY.md` is the eventual argumentative synthesis.

## V2.4 independent AV route

The optional independent reread is a separately identified execution inside this same project, with proposed scope S1E01–S3E12. It does not restart or replace the historical V2 lane merely by existing. Its prepared state is NOT_STARTED. The execution plan owns activation, the neutral dispatch packet, per-worker verification, role allocation, freeze barriers and recovery records.

There are two legitimate activation routes: retain the existing semantic ceiling while the older backfill and audit finish; or bind an owner-authorized independent full-series reread whose source range explicitly includes S3E09–S3E12 while retaining the older V2 hold. A directory, draft label, model assignment or planned scope is not that authorization. Use the ordinary root initialization and run fields for the actual active run, not a second canonical entrypoint or competing active root state. If ordinary run/closure mechanisms cannot represent a later independently frozen import, follow initiation Section 3.9.5's separately reviewed exact-publication route; do not invent an exemption in this architecture.

Within an activated run, process episodes chronologically and parallelize responsibilities within each episode. Close its reading, source-aware review, significant disagreements, candidate cumulative deltas and verified durable receipt before advancing. Freeze each independent season checkpoint before the next season. Finish and freeze the authorized scope’s independent retrospective account before exposing it to existing V2 interpretations; a full-series account is required only for a full-series scope. The current governing method's seven hypotheses, cohort studies and full historical map are withheld from neutral earlier-horizon workers.

Candidate episode readings use `02 Episode Deep Readings/Independent AV V2.4/LLS_SxEyy_INDEPENDENT_AV_DEEP_READING_V2_4.md`; candidate checkpoints use `03 Season Checkpoints/Independent AV V2.4/`. Create them only during the authorized run, with `draft_noncurrent`, empty supersession lists and `do_not_use_as_current_authority: true`. They remain recoverable independent evidence/interpretation records, not a second current reading or monograph. Working contribution packets may share a unit transaction artifact; no permanent file per worker is required.

Before reconciliation, cumulative deltas stay in candidate transaction records. They must not silently advance the five current ledgers. After the independent freeze, a named integrator compares the runs claim by claim, preserves both earlier formulations, rechecks load-bearing conflicts, and writes accepted changes into the existing canonical homes. For S3E09–S3E12, an independent candidate cannot by itself close the older V2 hold or fabricate that lane's prospective reading. Resolve the hold and actual exposure before authoring or accepting any current continuation; use a fresh, adequately bounded context where independence is still claimed.

---

# III. Episode artifact lane

`02 Episode Deep Readings` is canonical for local interpretation.

**Canonicalization gate:** verify the episode bundle against the Phase-0 source lock, its actual available evidence, and any synchronized AV object's identity. Complete the V2.4 method family's relevant channels, required independent contribution and critical review, claim-specific AV adjudication, and model-ledger workflow. When complete episode audio exists, this includes subtitle/audio alignment and targeted review of high-value silence, pause, dynamics, score, and performance transitions. Canonicalization requires the applicable five-ledger deltas, source/evidence and claim-revision routes, a current-unit story synopsis finalized after prospective captures, verified Git-primary persistence and truthful coverage. A candidate independent reading remains noncurrent until reconciliation and acceptance; required unresolved evidence blocks the corresponding completion claim. Cleanup follows verified receipt and preserves sources still needed by open items.

Each episode file is analytically immutable after canonicalization. Factual and interpretive corrections retain its original bytes and are attributed through:

- checkpoint delta files;
- specialist synthesis;
- claim-revision ledger.

Do not silently rewrite an early episode to make it “know” Season 3.

Recommended YAML fields:

- `series`
- `season`
- `episode`
- `artifact_id`
- `artifact_type`
- `analysis_mode`
- `source_bundle`
- `source_sha256`
- `source_language`
- `semantic_evidence_boundary`
- `future_semantic_evidence_used`
- `analysis_method`
- `architecture_protocol`
- `retained_frames`
- `contact_sheets_reviewed`
- `program_audio_duration_seconds`
- `audio_preflight_status`
- `audio_sha256` when practical
- `audio_codec`
- `audio_sample_rate_hz`
- `audio_channels`
- `acoustic_audit_status`
- `auditory_perception_mode`
- `source_lifecycle`
- `model_ledgers_updated`
- `local_cleanup_status`
- `retained_local_derivatives`
- `status`

For new V2.4 products also record or link `inspection_lanes`, the AV object and clock/sampling profile, actual participant contributions and exposure, observation-freeze references, critical-review dispositions, unresolved requirements, and the unit transaction receipt. The [AV evidence index](../06%20Evidence%20and%20Indexes/LLS_AV_EVIDENCE_AND_RECONCILIATION_INDEX.md) owns the compact receipt/coverage schema. No new field is backfilled as a fictitious historical execution fact.

---

# IV. Character-modeling and source-lifecycle lane

The V2 corpus is designed to support later character behavior/speech reconstruction without creating a separate simulation corpus or duplicating primary media.

## 1. Five canonical longitudinal/model-facing ledgers

The following mutable cumulative artifacts live under `06 Evidence and Indexes` and are updated in place:

- `LLS_CHARACTER_STATE_LEDGER.md` — time-indexed developmental state, desire, fear, self-conception, defenses, capacities, uncertainties;
- `LLS_CHARACTER_BEHAVIOR_AND_DECISION_LEDGER.md` — trigger → perceived stakes → goal/conflict → likely action patterns, exceptions, confidence, evidence;
- `LLS_CHARACTER_VOICE_MODEL_LEDGER.md` — contextual Japanese speech/register/address habits and only those performed/acoustic features directly supported by evidence;
- `LLS_RELATIONSHIP_CONDITIONING_MATRIX.md` — directional changes in behavior/speech by interlocutor, authority, intimacy, rivalry, care, and conflict state;
- `LLS_MUSICAL_DRAMATURGY_LEDGER.md` — time-indexed music-as-action evidence: performance authorship, performer/audience configuration, lyric allocation, sectional form, staging, performance ideology, formal-versus-dramatic outcome, recurrence, and claim transitions.

These are **active_provisional** cumulative infrastructure until the relevant analytical boundary is frozen. They do not replace the canonical episode readings; they distill them for longitudinal retrieval and later simulation/modeling.

## 2. Modeling authority rule

A character model must always declare its active temporal boundary. Do not merge early and late states into one timeless persona. Simulations should distinguish:

- stable disposition;
- current developmental state;
- relationship-conditioned mode;
- situational trigger/stakes;
- likely response;
- plausible alternatives;
- known counterexamples;
- confidence and evidence boundary.

The corpus should support **probabilistic reconstruction**, not claims that an invented situation has one uniquely canonical response.

## 3. Source lifecycle and storage authority

The original Drive episode ZIP is the canonical cold primary source. The local workspace is temporary hot storage. The File Library should not accumulate the 36 source bundles or their unpacked media merely because analysis progresses.

Per episode:

> **canonical external source → verified temporary fetch/unpack or AV access → governing V2.4 analysis → compact durable Git-primary analytical artifacts (or verified noncurrent working freeze) → readback → task-owned local cleanup.**

Normally delete after successful readback:

- local ZIP;
- extracted complete audio;
- ordinary frames;
- contact sheets;
- temporary clips/waveforms/spectrograms;
- redundant extraction trees.

Small text derivatives such as corrected Japanese subtitles, dialogue/scene indexes, or compact manifests may be retained only when they materially improve active longitudinal retrieval. Exact timestamps/cue/frame IDs in the durable ledgers should usually make later reacquisition preferable to permanent media duplication.

Those primary-source derivatives stay outside public Git. The public analytical record carries sanitized provenance, brief necessary source anchors and recoverable locators, not full subtitles, transcript dumps, source payloads or private local paths. Never delete the owner's cold-source collection as part of temporary cleanup.

Later checkpoints/specialist syntheses should reacquire only the exact episode bundles needed to verify load-bearing cross-episode claims.

## 4. Individual character monographs and qualification

Person-level synthesis is a required responsibility distinct from the existing cohort/relationship specialists. The [qualification record](../07%20Audits%20and%20Manifests/LLS_CHARACTER_MONOGRAPH_QUALIFICATION.md) is the mutable home for each assessed subject's identity, evidence boundary, outcome, rationale and largest gaps, review trigger, actual monograph path once written, and separate self-containment/fidelity acceptance results. Unassessed means unassessed; it is neither qualification nor rejection.

Apply [initiation Section 5.5.1](../../../governance/source-policies/MANGA_ANIME_PROJECT_INITIATION_AND_ARCHITECTURE_POLICY.md#self-contained-character-monograph-standard). Eligibility depends on differentiated convergent evidence, contextual/interlocutor variation and counterexamples, not a fixed eleven-member roster or narrative prominence. Assess supporting characters, adults and rivals when evidence warrants; a group-level role does not automatically qualify each individual. Use `QUALIFIED_PENDING`, `COMPLETE_AT_BOUNDARY`, `DEFERRED_EVIDENCE` and `REASSESS_AFTER_REVISION` as defined there. Every qualified subject creates a production obligation; character-layer completion is blocked while an obligation remains.

The planned home is `05 Specialist Synthesis/character_and_relationship/monographs/LLS_<SUBJECT>_CHARACTER_MONOGRAPH.md`, one current portrait per subject/continuity and declared boundary. Create no placeholder portrait. Kanon's existing planned center/leadership specialist remains a thematic argument; it does not substitute for a usable personal portrait. Cohort studies retain their relational questions and cross-reference individual consequences without duplicating the portraits.

Each portrait makes identity/circumstances, personal history and disclosure order, values and psychology, cognition and decisions, ordinary and exceptional conduct, Japanese speech and performed communication, directed relationships, preferences and everyday life, source-evidenced intimacy, capacities and limits, longitudinal development, a conditional behavioral profile, uncertainty and source traceability understandable in that document itself. Untested dimensions remain unknown; a tested absence needs evidence. For minors, intimacy discussion remains limited to what the source depicts. Links verify and deepen a portrait rather than carrying it. No word quota replaces evidence-proportional depth.

Episode captures feed the five existing ledgers and the AV index: preserve mundane preferences, reasoning and exceptions, voice/body interactions and relationship-specific differences, not just major arc conclusions. Review monographs separately for **self-containment** (document-only questions about this person) and **fidelity** (load-bearing claims against current source/claim state), preferably by a reviewer other than the author; record both outcomes. A compact operational profile is not an independently validated reconstruction model and grants no capability grade.

## 5. Responsibility matrix and execution ownership

| Recurring responsibility | Sequential capture | Cumulative home | Mature destination |
|---|---|---|---|
| State, history and development | Changes, disclosure/knowledge boundary and counterexamples | Character-state ledger | Individual monograph; cohort/series specialists |
| Reasoning, habits and ordinary choices | Conditional behavior, preferences versus accommodation, limits | Behavior/decision ledger | Monograph and separately scoped reconstruction |
| Language and performed acting | Attested wording; separately anchored voice/body interaction | Voice-model ledger; AV index for inspection/locators | Monograph and Specialist 10 |
| Directed relationships and group positioning | Interlocutor variation, trust, conflict/repair, staging | Relationship-conditioning matrix | Monographs; Specialists 03–06 |
| Songs as dramatic action | M0–M3 screening, segment-level diegesis/allocation and outcomes | Musical-dramaturgy ledger | Specialist 09; ensemble/character consequences |
| Score, ambience, silence and visual-motion recurrence | Observations, opportunities for absence and competing explanations | AV index recurrence routes to unit evidence; music ledger when music-as-action | Specialists 09–11 |
| Source inspection and independence | Actual coverage, calibration, exposure, freezes and contributions | AV evidence/reconciliation index and linked unit records | Acceptance and evidence audit |
| Claim changes and disputes | Earlier/new formulations, supporting/counterevidence, transition | Primary-source locator and claim-revision ledger | Corrected cumulative state and dependent syntheses |

Keep institution, competition and thematic observations in their source-facing readings and relevant existing cumulative entries until a separate recurring dimension demonstrates the need for its own ledger. Planned indexes are not automatically populated by their names. The two initialized V2.4 evidence/revision homes solve actual recurring retrieval and adjudication responsibilities; they carry no invented historical observations.

The execution plan records the standing whole-unit principal/integrator, musical dramaturgy, voice/acting, visual/choreographic form, score/sound, character/relationship/language and independent critical-review responsibilities. These are responsibilities, not a fixed worker quota: assign distinct contexts proportionally while retaining genuine independent specialist work and critical review. During the independent phase, the fresh principal/run integrator alone mutates candidate readings and run-local deltas; a separate repository-aware coordinator maintains current routing from receipts and withholds old interpretations. After the scoped cross-run freeze, one designated current-corpus integrator owns accepted shared-ledger and entrypoint changes. A context that inspected old ledgers for setup cannot also claim to be a blind independent principal. Specialists inspect their assigned source scope and preserve material contributions; no coordinator receives inspection credit merely for dispatching work. No ordinary full episode has an automatic reduced configuration.

Sequential readings, AV specialists, reviewers and interpretive ledger work inherit `SUBSTANTIVE_ANALYSIS`, escalating for demonstrated complexity. Checkpoints, monographs, specialist synthesis and architecture use `DEEP_SYNTHESIS`; difficult full-series convergence uses `PREMIUM_QUALITY_FIRST` with a stated reliability rationale. Mechanical source checks use `BOUNDED_STANDARD` or deterministic tools. Resolve actual model and effort on the live surface under the [reasoning policy](../../../governance/source-policies/MANGA_ANIME_REASONING_AND_MODEL_ROUTING_POLICY.md); providers and quota resets confer no evidence capability or authority.

Fresh synthesis receives a versioned, frozen evidence snapshot, actual output targets and the current boundary through the [handoff contract](../../../governance/source-policies/MANGA_ANIME_ANALYTICAL_HANDOFF_AND_INTEGRATION_CONTRACT.md). The receiving integrator checks complete returned contents, evidence debt, current target drift and lost detail before acceptance. If AV reconciliation changes a central premise, reopen the affected synthesis and its dependents before promotion.

---

# V. Season checkpoint lane

Checkpoints are prospective historical records.

## Season 1 checkpoint

Primary questions:

- What has the original five-member Liella! become?
- What does Kanon's centrality mean at this stage?
- What forms of ambition, fear, and belonging define Keke, Chisato, Sumire, and Ren?
- How does Yuigaoka function as a school and symbolic project?
- What has Love Live! competition taught or failed to teach?

## Season 2 checkpoint

Primary questions:

- How does Liella! absorb new members?
- Which inequalities of experience remain?
- Does “catching up” define juniors too narrowly?
- How do seniors change when they become responsible for successors?
- How does Wien alter the talent/competition problem?

## Season 3 checkpoint

Primary questions:

- What does Liella! mean when graduation becomes real?
- Which roles can persist after the original cohort leaves?
- Does the group successfully decenter its founders?
- What future forms are professional, educational, relational, and artistic rather than merely competitive?

---

# VI. Specialist synthesis package

Recommended core specialist documents follow. These are final proposed homes, not precommitted theses.

## `01_SERIES_ARCHITECTURE_THREE_YEARS_AND_THE_CHANGING_MEANING_OF_LIELLA.md`

Governing question:

> How does a five-member founding story become a three-cohort succession story without losing personal intimacy?

Primary home:

- three-season architecture;
- five → nine → eleven structure;
- season-to-season developmental handoffs;
- graduation horizon;
- final ensemble state.

## `02_KANON_CENTER_LEADERSHIP_VOICE_AND_DECENTERING.md`

Primary home:

- Kanon as protagonist;
- fear and singing;
- leadership;
- her capacity to perceive/activate others;
- risks of protagonist gravity;
- professional/future aspiration;
- whether the complete series successfully makes room beyond her.

## `03_KEKE_SUMIRE_CHISATO_REN_FOUNDING_FIVE_RELATIONSHIP_ECOLOGY.md`

Primary home:

- founding-five interpersonal system;
- pair bonds without flattening ensemble;
- Keke/Sumire conflict and recognition;
- Kanon/Chisato history;
- Ren and inherited school obligation;
- how the original five change once they become seniors.

## `04_SECOND_GENERATION_KINAKO_MEI_SHIKI_NATSUMI_ENTRY_AND_BELONGING.md`

Primary home:

- recruitment;
- junior anxiety;
- catching up;
- friendship and pair structures;
- outsider-to-member transitions;
- labor and aspiration;
- how second-years later become intermediaries between generations.

## `05_THIRD_GENERATION_TOMARI_WIEN_SUCCESSION_RIVALRY_AND_INHERITANCE.md`

Primary home:

- late entry into an established institution;
- Wien as competitor/member problem;
- Tomari and family/relational positioning;
- inheritance versus autonomy;
- what it means to join near the founders' exit.

## `06_LIELLA_AS_ENSEMBLE_COHORT_HIERARCHY_AND_SUCCESSION.md`

Primary home:

- whole-group ecology;
- center/periphery distribution;
- senior/junior hierarchy;
- transmission of knowledge;
- emotional/administrative labor;
- authority;
- succession;
- who gets narrative and musical space.

This document must include quantitative or semi-quantitative checks where useful (episode focus, song allocation, speaking/leadership concentration) without treating counts as self-interpreting.

## `07_YUIGAOKA_SCHOOL_INSTITUTION_FAMILY_AND_PLACE.md`

Primary home:

- school founding/history;
- institutional legitimacy;
- school reputation;
- family and local ties;
- physical/urban space;
- student life beyond idol competition;
- whether the school remains a living social world across seasons.

## `08_LOVE_LIVE_COMPETITION_TALENT_MERITOCRACY_AND_RECOGNITION.md`

Primary home:

- competition logic;
- evaluation;
- talent discourse;
- rivalry;
- defeat/victory;
- public recognition;
- Wien's challenge to the group's self-understanding;
- distinction between measurable excellence and human/artistic worth.

## `09_MUSIC_SONG_PERFORMANCE_AND_DRAMATURGY.md`

Primary home:

- song-as-action;
- recurring musical identities;
- solo/duet/group distribution;
- formation/choreography;
- lyric/drama relation;
- competition performances;
- rehearsal versus stage;
- how musical scale changes with membership growth.

## `10_JAPANESE_VOICE_ADDRESS_MULTILINGUALISM_AND_CHARACTERIZATION.md`

Primary home:

- pronouns;
- honorifics;
- nicknames;
- register;
- senior/junior speech;
- multilingual speech and foreignness;
- characteristic verbal habits;
- performed vocal-state changes.

This specialist also explains the relation between attested Japanese wording and performed delivery, listener-specific voice/body behavior, vocal interaction timing and the limits of inferring character state or production intention from performance. Individual monographs incorporate what those findings establish about each person rather than sending the reader here to recover their basic speech style.

## `11_VISUAL_SPATIAL_GRAMMAR_CITY_SCHOOL_STAGE_AND_THRESHOLD.md`

Primary home:

- recurring locations;
- center/periphery compositions;
- stairs/rooftops/thresholds/transit;
- city versus school space;
- group formations;
- costume recurrence;
- visual motifs and transformed callbacks.

Include motion, reaction timing, editing and audiovisual synchronization where actually inspected, and distinguish those path claims from static composition. Specialist 09 owns song-as-action; Specialist 10 owns performed communication; this specialist owns visual form. The AV evidence index routes source facts and recurrence comparisons shared by those arguments.

## `12_ETHICS_OF_AMBITION_CARE_LEADERSHIP_AND_BECOMING_ADULT.md`

Primary home:

- ambition versus care;
- autonomy versus responsibility;
- mentorship;
- senior obligation;
- professional aspiration;
- family expectation;
- separation;
- when helping another person enables or constrains agency.

## `13_ENDINGS_GRADUATION_FUTURE_AND_WHAT_CAN_CONTINUE.md`

Primary home:

- final episodes;
- graduation;
- succession;
- geographic/professional separation;
- group-name continuity;
- unresolved futures;
- distinction between ending school, ending a cohort, and ending Liella!.

## `14_COMPARATIVE_REFERENCE_MATRICES_AND_OPEN_QUESTIONS.md`

Primary home:

- compact character matrices;
- relationship matrices;
- cohort comparisons;
- performance comparisons;
- unresolved ambiguities;
- exportable comparison points for other idol anime.

---

# VII. Evidence/index package

## `LLS_EPISODE_EVIDENCE_LEDGER.md`

Chronological ledger of high-value scenes and claims across all 36 episodes.

Each row should include:

- episode;
- timestamp/range;
- evidence type;
- characters;
- relationship/system;
- claim supported;
- locator IDs;
- retrospective significance.

## `LLS_PRIMARY_SOURCE_LOCATOR_AND_CLAIM_REVISION_LEDGER.md`

Tracks:

- claim ID;
- original episode conclusion;
- exact primary-source locators;
- later evidence that pressures it;
- revision state: strengthened / weakened / narrowed / overturned / unresolved;
- transition: `PRESERVE`, `STRENGTHEN`, `REVISE`, `DOWNGRADE`, `REJECT`, or `OPEN` (retain any older descriptive state in its historical record);
- specialist document home.

This file is initialized in V2.4 as the current home for new attributable claim changes and disputes. Earlier transition histories in the musical and character ledgers remain in place and are cross-referenced when a claim is next touched; no bulk migration or invented retrospective claim IDs.

## `LLS_AV_EVIDENCE_AND_RECONCILIATION_INDEX.md`

Owns actual per-run/per-unit inspection coverage, calibration and exposure receipts, pointers to frozen observations and critical review, and source-locator/recurrence routes for acting, motion, score and sound. It distinguishes independent candidate findings from accepted write-through. The claim-revision ledger owns current formulations and transition history; the five existing ledgers own cumulative interpretation. An empty coverage table means no V2.4 inspection is recorded, not that the earlier corpus has no evidence.

## `LLS_CHARACTER_STATE_LEDGER.md`

Time-indexed state ledger. For each materially affected character record episode boundary, desire, fear, self-conception, role, defense, capacities, unresolved conflict, and confidence. Earlier rows are preserved rather than rewritten by later development.

## `LLS_CHARACTER_BEHAVIOR_AND_DECISION_LEDGER.md`

Model-facing conditional behavior evidence. Each row should include character, temporal boundary, trigger/context, perceived stakes, active goal/avoidance goal, likely response, escalation/de-escalation condition, known exception/counterexample, confidence, and exact episode locator.

## `LLS_CHARACTER_VOICE_MODEL_LEDGER.md`

Contextual Japanese voice model. Track self-reference, address, register, sentence endings, discourse markers, code-switching, ellipsis, interruption, public/private modes, conflict/support modes, and directly supported acoustic/performance facts. Do not treat imitation-friendly catchphrases as a complete voice model.

## `LLS_RELATIONSHIP_CONDITIONING_MATRIX.md`

Directional relation model. Record how Character A changes behavior and speech with Character B, including intimacy, authority, admiration, dependence, rivalry, care, conflict style, repair, and changes in who can challenge whom.

## `LLS_JAPANESE_DIALOGUE_AND_ADDRESS_INDEX.md`

Index load-bearing wording, recurring phrases, address forms, pronoun shifts, and difficult translation cases.

## `LLS_SONG_AND_PERFORMANCE_INDEX.md`

For each performance:

- song;
- episode;
- participants;
- dramatic setup;
- visual staging;
- notable lyric linkage;
- post-performance consequence;
- callbacks/reprises.

## `LLS_VISUAL_MOTIF_AND_CALLBACK_INDEX.md`

Record factual recurrence first; interpretation second.

---

# VIII. Cross-document duplication rules

1. A person's integrated portrait belongs in their qualified individual monograph; cohort and relationship specialists retain their distinct questions. The portrait must remain understandable without following links for basic personality, decisions, relationships or speech.
2. Whole-group hierarchy belongs in Document 06, even when examples involve Kanon.
3. Competition theory belongs in Document 08, not repeated in every character document.
4. Song mechanics belong in Document 09; character documents summarize only relationship-specific consequences.
5. Japanese wording belongs in Document 10/index when the linguistic pattern itself is the subject.
6. Visual recurrence belongs in Document 11/index; other documents cite it when necessary.
7. Ethical generalization belongs in Document 12, after character/institution evidence has been established.
8. Ending theory belongs in Document 13; earlier documents state their local endpoint and cross-reference.
9. Conditional behavior evidence belongs in the behavior/decision ledger; specialist character documents synthesize it rather than duplicating every row.
10. Contextual speech evidence belongs in the voice-model ledger and Japanese index; generated imitation examples are never evidence.
11. Relationship-specific behavior belongs in the conditioning matrix; whole-group hierarchy still belongs in Document 06.

---

# IX. Reader order for the mature full-series package

1. The registered `01 Source Lock and Inventory/LLS_CURRENT_STATE_AND_CORPUS_MAP.md` (retain this single current entrypoint).
2. `01_SERIES_ARCHITECTURE_THREE_YEARS_AND_THE_CHANGING_MEANING_OF_LIELLA.md`
3. `02_KANON_CENTER_LEADERSHIP_VOICE_AND_DECENTERING.md`
4. `03_KEKE_SUMIRE_CHISATO_REN_FOUNDING_FIVE_RELATIONSHIP_ECOLOGY.md`
5. `04_SECOND_GENERATION_KINAKO_MEI_SHIKI_NATSUMI_ENTRY_AND_BELONGING.md`
6. `05_THIRD_GENERATION_TOMARI_WIEN_SUCCESSION_RIVALRY_AND_INHERITANCE.md`
7. `06_LIELLA_AS_ENSEMBLE_COHORT_HIERARCHY_AND_SUCCESSION.md`
8. `07_YUIGAOKA_SCHOOL_INSTITUTION_FAMILY_AND_PLACE.md`
9. `08_LOVE_LIVE_COMPETITION_TALENT_MERITOCRACY_AND_RECOGNITION.md`
10. `09_MUSIC_SONG_PERFORMANCE_AND_DRAMATURGY.md`
11. `10_JAPANESE_VOICE_ADDRESS_MULTILINGUALISM_AND_CHARACTERIZATION.md`
12. `11_VISUAL_SPATIAL_GRAMMAR_CITY_SCHOOL_STAGE_AND_THRESHOLD.md`
13. `12_ETHICS_OF_AMBITION_CARE_LEADERSHIP_AND_BECOMING_ADULT.md`
14. `13_ENDINGS_GRADUATION_FUTURE_AND_WHAT_CAN_CONTINUE.md`
15. `14_COMPARATIVE_REFERENCE_MATRICES_AND_OPEN_QUESTIONS.md`
16. evidence/index appendices.

Individual monographs are a parallel person-first reader route from the qualification record once actual portraits exist. The numbered specialist package remains intact; it is not a substitute for that route.

---

# X. Release criteria

The corpus is ready for final release only when:

- all 36 canonical episode readings exist;
- all three season checkpoints are frozen;
- load-bearing claims have primary-source locators;
- later revisions are represented as deltas rather than silent retrofits;
- specialist documents have one clear primary home per major problem;
- contradiction and duplication audits are complete;
- music/performance and Japanese-language claims are source-grounded;
- the five canonical longitudinal/model-facing ledgers, including `LLS_MUSICAL_DRAMATURGY_LEDGER.md`, are current through S3E12 and preserve time-indexed states/counterexamples;
- no character simulation claim is presented as deterministic when the evidence supports multiple plausible responses;
- redundant episode ZIP/audio/frame payloads are not packaged into the analytical release;
- the final synthesis distinguishes fact, strong inference, interpretation, and speculation;
- the final ending analysis does not mistake closure for total resolution.

V2.4 distinguishes these gates explicitly:

| Gate | Required evidence of completion |
|---|---|
| Independent AV run completion | Authorized range fully inspected by its principals, required independent contributions/review, calibrated and adequately sampled load-bearing observations, closed unit transactions and independent season/full-run freezes; no automatic current authority |
| Existing V2 continuation release | Musical backfill through S3E08 and its verified integration/readback audit; no bypass from an independent candidate's later coverage |
| Current sequential-source completion | 36 accepted current episode readings and three season checkpoints, with truthful generation, source and exposure boundaries |
| Longitudinal and AV reconciliation | Five ledgers current at the declared boundary; evidence and claim histories consistent; required channel debt resolved or the affected completion scope explicitly bounded; material disagreements retained |
| Specialist readiness | Architecture/role-gap review, stable source/claim routes, qualification decisions and outstanding character obligations, scoped frozen synthesis inputs |
| Character-layer completion | Every qualified subject has an accepted self-contained portrait; self-containment and fidelity recorded separately; no deferred/unassessed candidate represented as completed |
| Full-series synthesis readiness | Required specialists and character responsibilities converge; changed central premises propagate to affected documents; unresolved interpretations remain visible |
| Release | Contradiction, duplication, locator, named-subject/reference and authority audits; source payload exclusion; repository publication checks; explicit freeze state |

An `OPEN` interpretation is a legitimate intellectual outcome, but it cannot certify an unresolved REQUIRED observation. Report the precise bounded scope that is complete. A successful repository check certifies structural/publication requirements, not source truth or character reconstruction readiness.

Extend the architecture only when a recurring dimension has independent evidence, retrieval or synthesis needs. Record material amendments and their justified backfill scope in the current map and revision history. Do not reread historical units solely to retrofit a field, synopsis or participation receipt. New framework versions preserve earlier evidentiary boundaries and frozen bytes.

The intended result is a reusable scholarly-style corpus: locally auditable at scene level, historically faithful to the sequential viewing experience, and strong enough for later cross-series comparison.


---

## V2.2 architecture revision — 2026-08-24

V2.2 formalizes character modeling as a native longitudinal product of episode analysis and adopts the cold-source/hot-workspace storage lifecycle. Four model-facing ledgers now have canonical homes under `06 Evidence and Indexes`. S1E01 is the seeded migration boundary; S1E02 is the first episode to use the complete lifecycle from initial Drive fetch through post-readback cleanup.


---

## V2.3 architecture revision — 2026-08-26

V2.3 introduces a canonical musical-dramaturgy ledger under `06 Evidence and Indexes`, distinguishes that authority from the `04 Retrospective Music and Performance` working lane, and establishes a temporary S3E09 continuation lock. The lock remains in force until sequential musical-dramaturgy backfill has advanced from S1E01 through S3E08 and an integration audit confirms ledger/corpus-map consistency. Existing V2.2 episode artifacts and frozen Season-1/Season-2 checkpoints retain their historical authority; the backfill creates deltas and transition records rather than silent rewrites.

## V2.4 architecture revision — 2026-11-26

Adopts the AV method family, source-aware multi-agent execution and a separately bounded independent reread plan; initializes inspection/reconciliation routing and claim-revision infrastructure; adds evidenced monograph qualification and separate individual portraits while retaining all fourteen specialists; defines responsibility, handoff and completion gates; and corrects analytical storage to Git-primary authority. The current map is reduced to present state by moving its historical progress blocks verbatim to the adjacent changelog. No historical reading, checkpoint, five-ledger entry or source-lock artifact is rewritten. The prospective gate remains CLOSED for preparation, independent AV coverage remains zero, and the existing S3E09 hold remains active.
