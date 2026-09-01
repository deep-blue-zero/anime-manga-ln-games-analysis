---
title: "Love Live! Superstar!! — Multi-Document Analysis and Synthesis Architecture V2"
series: LLS
artifact_type: synthesis_architecture
scope: "TV S1E01-S3E12"
generation: V2.3
version: "2.3"
date: "2026-08-26"
status: canonical
architecture_status: "Paired architecture for LoveLiveSuperstar_Analytical_Method_V2.md"
source_boundary: "Japanese-audio television corpus; sequential semantic seal applies"
supersedes: null
superseded_by: null
do_not_use_as_current_authority: false
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

---

# I. Drive directory tree

```text
Love Live! Superstar!!/
├── 00 Frameworks/
│   ├── LoveLiveSuperstar_Analytical_Method_V2.md
│   └── LoveLiveSuperstar_Multi_Document_Architecture_V2.md
├── 01 Source Lock and Inventory/
│   ├── 00_PRIMARY_SOURCE_CORPUS_MAP.md
│   ├── 01_SOURCE_MANIFEST.md
│   └── checksum_and_bundle_inventory.*
├── 02 Episode Deep Readings/
│   ├── Season 1/
│   │   └── LLS_S1E01_DEEP_READING_V2.md ... LLS_S1E12_DEEP_READING_V2.md
│   ├── Season 2/
│   │   └── LLS_S2E01_DEEP_READING_V2.md ... LLS_S2E12_DEEP_READING_V2.md
│   └── Season 3/
│       └── LLS_S3E01_DEEP_READING_V2.md ... LLS_S3E12_DEEP_READING_V2.md
├── 03 Season Checkpoints/
│   ├── LLS_SEASON1_FROZEN_CHECKPOINT.md
│   ├── LLS_SEASON2_FROZEN_CHECKPOINT.md
│   ├── LLS_SEASON3_END_STATE_CHECKPOINT.md
│   └── checkpoint_delta_files/
├── 04 Retrospective Music and Performance/
│   ├── episode_addenda/
│   ├── song_performance_ledger/
│   └── score_sound_recurrence_index/
├── 05 Specialist Synthesis/
│   ├── character_and_relationship/
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
│   ├── LLS_JAPANESE_DIALOGUE_AND_ADDRESS_INDEX.md
│   ├── LLS_SONG_AND_PERFORMANCE_INDEX.md
│   ├── LLS_VISUAL_MOTIF_AND_CALLBACK_INDEX.md
│   └── machine_readable_indexes/
├── 07 Audits and Manifests/
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
2. Complete Season 1 sequential readings. For each episode: fetch/unpack the Drive bundle locally, complete the audiovisual/acoustic reading, update all applicable model/evidence ledgers, verify durable Drive writes, then delete redundant local source payloads before advancing.
3. Freeze Season 1 checkpoint.
4. Complete Season 2 sequential readings with the same V2.2 fetch → local analysis → model-ledger update → Drive readback → cleanup lifecycle.
5. Write Season-2 pressure deltas against the frozen Season-1 checkpoint.
6. Freeze Season 2 checkpoint.
7. Complete Season 3 sequential readings through **S3E08** under V2.2, then impose a deliberate continuation lock before S3E09.
8. Upgrade method/architecture to V2.3 and create `LLS_MUSICAL_DRAMATURGY_LEDGER.md` as canonical mutable infrastructure under `06 Evidence and Indexes`.
9. Backfill musical dramaturgy **sequentially from S1E01 through S3E08**, using existing canonical episode artifacts as retrieval/hypothesis layers and reacquiring primary AV evidence proportionally for M2/M3 events. Frozen season checkpoints are not rewritten; claim pressure is recorded by transition state.
10. Run a musical-dramaturgy integration audit at S3E08. Only after the ledger backfill boundary reaches S3E08 and the audit is verified may the **S3E09 continuation lock be removed**.
11. Resume S3E09–S3E12 under native V2.3, with musical-dramaturgy write-through performed during each episode lifecycle.
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

---

# III. Episode artifact lane

`02 Episode Deep Readings` is canonical for local interpretation.

**Canonicalization gate:** the episode bundle must be fetched from the canonical Drive source, verified against the Phase-0 source lock, unpacked locally, and passed through the governing V2.3 audiovisual/audio, musical-dramaturgy, and model-ledger workflow before its Markdown artifact is declared canonical. When complete episode audio exists, this includes exact subtitle/audio alignment and targeted review of high-value silence, pause, dynamics, score, and performance transitions. Canonicalization also requires the applicable character-state, behavior/decision, voice-model, relationship-conditioning, and musical-dramaturgy deltas to be written, followed by Drive readback and cleanup of redundant local source payloads.

Each episode file is immutable after canonicalization except for factual correction. Later interpretive changes belong in:

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

> **canonical Drive ZIP → temporary local fetch/unpack → governing V2.3 analysis → compact durable Markdown/ledgers/locators in Drive → readback verification → local cleanup.**

Normally delete after successful readback:

- local ZIP;
- extracted complete audio;
- ordinary frames;
- contact sheets;
- temporary clips/waveforms/spectrograms;
- redundant extraction trees.

Small text derivatives such as corrected Japanese subtitles, dialogue/scene indexes, or compact manifests may be retained only when they materially improve active longitudinal retrieval. Exact timestamps/cue/frame IDs in the durable ledgers should usually make later reacquisition preferable to permanent media duplication.

Later checkpoints/specialist syntheses should reacquire only the exact episode bundles needed to verify load-bearing cross-episode claims.

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

## `11_VISUAL_SPATIAL_GRAMMAR_CITY_SCHOOL_STAGE_AND_THRESHOLD.md`

Primary home:

- recurring locations;
- center/periphery compositions;
- stairs/rooftops/thresholds/transit;
- city versus school space;
- group formations;
- costume recurrence;
- visual motifs and transformed callbacks.

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
- specialist document home.

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

1. Character biography belongs in the character's primary specialist home.
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

1. `00_README_AND_CORPUS_MAP.md`
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

The intended result is a reusable scholarly-style corpus: locally auditable at scene level, historically faithful to the sequential viewing experience, and strong enough for later cross-series comparison.


---

## V2.2 architecture revision — 2026-08-24

V2.2 formalizes character modeling as a native longitudinal product of episode analysis and adopts the cold-source/hot-workspace storage lifecycle. Four model-facing ledgers now have canonical homes under `06 Evidence and Indexes`. S1E01 is the seeded migration boundary; S1E02 is the first episode to use the complete lifecycle from initial Drive fetch through post-readback cleanup.


---

## V2.3 architecture revision — 2026-08-26

V2.3 introduces a canonical musical-dramaturgy ledger under `06 Evidence and Indexes`, distinguishes that authority from the `04 Retrospective Music and Performance` working lane, and establishes a temporary S3E09 continuation lock. The lock remains in force until sequential musical-dramaturgy backfill has advanced from S1E01 through S3E08 and an integration audit confirms ledger/corpus-map consistency. Existing V2.2 episode artifacts and frozen Season-1/Season-2 checkpoints retain their historical authority; the backfill creates deltas and transition records rather than silent rewrites.
