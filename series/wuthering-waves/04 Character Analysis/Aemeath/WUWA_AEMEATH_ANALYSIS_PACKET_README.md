---
series: WUWA
character: Aemeath
artifact_type: analysis_packet_entrypoint
scope: AEMEATH_SOURCE_3_6_0_PRE_AV
analysis_generation: AEMEATH_PRE_AV_V0_1
status: active_provisional
release_state: local_working_draft
foundation_authority: primary_and_deterministic_derived_evidence
analysis_authority_state: local_working_draft_not_promoted
source_generation: arikatsu-3.6.0-353f2eae-expanded-v0.3.0-ko
source_commit: 353f2eaed119bc9f680eab92807d20ac75a79b40
text_authority: zh-Hans
localization_witnesses: [ja, ko, en]
drive_character_bridge: 13L8W_Gb15b1h-ovJ_MXOgJY8jr8uPyR_
drive_voice_view: 1EFlKk-HM23vmYbxxkPWaN9waGXaJqPcP
governing_protocols:
  - WUWA_ANALYTICAL_METHOD.md
  - WUWA_CHARACTER_RECONSTRUCTION_PROTOCOL.md V0.2
  - WUWA_CHARACTER_FOLDER_CONTRACT.md
  - WUWA_MACHINE_VOICE_ANALYSIS_PROTOCOL.md
  - WUWA_AUDIOVISUAL_EVIDENCE_COLLECTION_PROTOCOL_V0_1.md proposed
  - WUWA_AUDIOVISUAL_HUMAN_RETRIEVAL_CROSSWALK_SPEC_V0_1.md proposed
  - WUWA_AV_EVIDENCE_MANIFEST_SPEC_V0_1.md proposed
intended_canonical_home: series/wuthering-waves/04 Character Analysis/Aemeath/
do_not_use_as_current_git_authority: true
created: 2026-09-03
---

# Aemeath reconstruction dossier — pre-audiovisual V0.1

## Purpose

This packet is a source-grounded reconstruction of **Aemeath / 爱弥斯 / エイメス / 에이메스** against the frozen *Wuthering Waves* 3.6.0 evidence generation. It applies the current Wuthering Waves character-analysis method together with the proposed audiovisual collection and human-retrieval refinements that have not yet been committed to Git.

The packet has three immediate responsibilities:

1. reconstruct Aemeath from the complete accepted textual/contextual evidence currently materialized in Drive;
2. preserve the distinction among direct Aemeath, historical Aemeath states, her post-death embodiments, and the separately identified associated shell/remnant;
3. leave a collection-ready audiovisual hierarchy and human-facing retrieval crosswalk for the later AV hardening pass.

It is **not** a final integrated multimodal monograph. No selected Aemeath cutscene/PV/static-art tranche has yet been acquired into the AV evidence manifest and directly reviewed under the proposed protocol. It is also not a human voice-performance study. The direct voice corpus is technically complete inside its accepted boundary, but all structured human listening fields remain open.

Nothing in this directory has been committed, pushed, merged, or promoted to repository authority.

## Current analytical thesis

The strongest source-bounded interpretation is:

> **Aemeath is a character about inherited care becoming both a home and a binding command. Rover teaches her that another person's pain matters and that one should help when one can; she transforms that lesson into the dream of becoming a savior. The same love that gives her a life also teaches her to erase herself for others. Her maturation lies not in rejecting sacrifice, happiness, family, or the savior vocation, but in distinguishing chosen responsibility from copied compulsion and learning that love must preserve the other person's right to truth, grief, refusal, and shared burden.**

A shorter operational form is:

> **care inherited as command → happiness lived under concealment → protection through truth-erasure and self-erasure → confrontation with reciprocal choice → unilateral sacrifice → return, apology, and a chosen parallel vocation.**

The thesis must retain several contradictions:

- Aemeath's cheerful school life is genuine; it is not merely camouflage for despair.
- Cheerfulness also functions as an instrument of control, deflection, and protection in some scenes.
- Her savior dream begins in imitation of Rover but becomes a self-authored aspiration she refuses to surrender.
- She correctly criticizes the coercion imposed on Rover while reproducing its paternalistic logic when she decides what truth Rover may bear.
- Becoming a digital ghost expands her agency and technical reach while intensifying isolation, instrumental self-use, and embodiment uncertainty.
- Her 3.3 return revises unilateral sacrifice through shared rescue, apology, and future planning; it does not abolish her willingness to take on dangerous responsibility.
- The associated shell may carry instinct or communication from Aemeath, but the source explicitly refuses simple identity equivalence.

## Source boundary

Pinned semantic authority:

- Arikatsu commit: `353f2eaed119bc9f680eab92807d20ac75a79b40`
- normalized generation: `arikatsu-3.6.0-353f2eae-expanded-v0.3.0-ko`
- primary textual witness: `zh-Hans`
- official localization witnesses: `ja`, `ko`, `en`
- raw voice authority: installed-client media routed through semantic occurrence, runtime render, WEM, PCM, FLAC, and Drive-shard identities

The direct Aemeath collection contains:

- role 1210; voice slug `aimisi`;
- five favor stories and 116 favor/archive words;
- 678 accepted solo occurrences;
- 593 present/main-state occurrences;
- 54 childhood-state occurrences;
- 13 past/student-memory occurrences;
- 17 message occurrences;
- one contextually adjudicated hidden-speaker occurrence;
- 584 source-voiced and 94 explicitly unvoiced direct occurrences;
- 700 semantic direct voice lines: 584 story/message plus 116 archive/favor lines;
- complete four-language media coverage for all 700 semantic lines;
- 2,844 direct render associations and 2,842 unique direct FLAC objects;
- 195 direct-character scene/action contexts;
- 194 complete selected raw flow-state rows;
- 2,899 contextual text keys;
- four relevant WavesLine records;
- 88 quest-reference wrappers representing 16 distinct quest IDs.

The collection audit reports both `collection_integrity_valid: true` and `voice_completeness_valid: true` inside the accepted direct-character boundary. These are technical coverage statements, not claims that every wholly unmarked identity in the game has been discovered.

## Identity boundary

The accepted direct-character identity includes:

| Source identity | Analytical handling |
|---|---|
| speaker `150059` | present/main Aemeath |
| speaker `150064` | past student-memory Aemeath |
| speaker `150075` | childhood Aemeath |
| speaker `350187`, contact 74 | Aemeath's message identity |
| generic speaker `178` at `10663/3/6` only | accepted through immediate self-introduction; never globally mapped |
| Fleet Snowfluff / 飞行雪绒 | explicit performer/online alias |

Speaker `150086`, source-labeled `「爱弥斯」`, is **not** placed in that denominator. It is retained as `wuwa:lore-entity:aemeath-associated-shell`. At `11869/2/4`, Rover explicitly says the being is not Aemeath but a piece retained through the talisman. At `15760/4/19–20`, Mornye leaves residual instinct versus a weak transmitted signal from the real Aemeath unresolved. The shell receives its own identity/embodiment profile in this packet.

## Audio boundary

The direct voice evidence is unusually complete but does not satisfy the full analytical requirements of `machine_voice_profiled`.

What currently exists:

- all 700 semantic direct lines have complete CN/JP/KR/EN coverage;
- 2,844 render associations represent 2,842 unique direct FLACs;
- direct render counts: Chinese 700, Japanese 712, Korean 700, English 732;
- 21 direct recordings are multichannel: seventeen six-channel and four three-channel;
- exact ordered samples and framing were verified against decoded source WEMs;
- source WAVs do not establish spatial-layout labels, while FLAC tools infer layouts;
- no downmix, isolated-speaker claim, or spatial interpretation is authorized;
- machine measurements currently include duration, channels, sample rate, RMS, peak, and a silence-threshold fraction;
- zero structured human listening annotations exist.

The proposed machine-voice method calls for stronger pitch, pause, speaking-rate, normalization, partitioning, and clustering work than the present retrieval-feature layer provides. This packet therefore reports the current reproducible baseline but keeps `machine_voice_profiled` unclaimed.

## Audiovisual boundary and updated protocol use

No extracted Aemeath video, screenshots, promotional images, or matched multilingual PV groups are included in the source package. `ASSET_REFERENCE_INDEX.json` is a locator list, not visual evidence.

This packet applies the proposed four-dimensional AV authority model:

1. **diegetic authority** — whether an action/state occurs in story continuity;
2. **representational authority** — official choices about appearance, voice, movement, design, and embodiment;
3. **interpretive authority** — how strongly a witness can support a character/relationship/development claim;
4. **production-framing authority** — what Kuro deliberately foregrounds, packages, or associates with Aemeath for the audience.

The packet also separates:

- core diegetic AV;
- matched multilingual promotional AV;
- unmatched official promotional AV;
- official static/representational media.

Two distinct files implement the new collection bridge:

- `WUWA_AEMEATH_AUDIOVISUAL_EVIDENCE_NOMINATION_PLAN.md` answers **what should be collected and which claim it can change**;
- `WUWA_AEMEATH_AV_HUMAN_RETRIEVAL_CROSSWALK.md` answers **how a human can find it through public story names, objectives, dialogue anchors, and search terms**.

No `AV_EVIDENCE_MANIFEST.jsonl` is emitted because no actual AV witness has been acquired or stable-linked into the evidence plane. Creating an empty manifest would confuse intended schema with acquired evidence.

## Packet contents and analytical responsibilities

### 1. `WUWA_AEMEATH_CHARACTER_DEEP_DIVE_PRE_AV.md`

Canonical-candidate interpretive center for the pre-AV generation. It reconstructs the character's developmental logic, ethics, ordinary life, relationship architecture, speech, embodiment, motifs, contradictions, and rival readings.

### 2. `WUWA_AEMEATH_EVIDENCE_AND_FALSIFICATION_MATRIX.md`

Claim-level apparatus separating source fact, stable observation, strong inference, candidate thesis, and open hypothesis. It records counterevidence and later falsification targets so future AV/source work can revise rather than merely decorate the reconstruction.

### 3. `WUWA_AEMEATH_RELATIONSHIP_AND_STATE_PROFILE.md`

Canonical-candidate home for developmental state slices, operational contexts, and recipient-conditioned relationships. It prevents childhood, student-memory, digital-ghost, post-return, and shell evidence from being averaged into one timeless personality.

### 4. `WUWA_AEMEATH_ORDINARY_LIFE_AND_PREFERENCES_PROFILE.md`

Source fact → implication → extrapolation-limit treatment of games, music, photography, food, study, clubs, friends, markets, seals, travel, home, rest, gifts, hobbies, weather, and ordinary social initiative.

### 5. `WUWA_AEMEATH_SPEECH_AND_MACHINE_VOICE_PROFILE_PRE_AV.md`

Textual speech/register reconstruction plus the current reproducible four-language acoustic baseline. It marks acting/emotion conclusions open and identifies later matched-source listening cohorts.

### 6. `WUWA_AEMEATH_IDENTITY_EMBODIMENT_AND_SHELL_PROFILE.md`

Separate topical home for digital-ghost personhood, body/frequency relations, Exostrider integration, Reactor Core/Drive metaphors, returned embodiment, and the non-equivalent associated shell.

### 7. `WUWA_AEMEATH_RECONSTRUCTIVE_PROFILE_PRE_AV.md`

Operational Markdown model for state selection, drives, fears, values, behavior rules, exceptions, recipient modifiers, decision logic, prediction templates, and mandatory abstentions. It is not a promoted JSON model package.

### 8. `WUWA_AEMEATH_MODEL_FIDELITY_AND_STRESS_TEST_PRE_AV.md`

Adversarial evaluation against savior-archetype leakage, cheerfulness-as-mask reduction, Rover-satellite collapse, resurrection simplification, shell flattening, ordinary-life failure, and relationship-insensitive prediction.

### 9. `WUWA_AEMEATH_AUDIOVISUAL_EVIDENCE_NOMINATION_PLAN.md`

AV hierarchy and claim-driven acquisition plan using the proposed four authority dimensions and four source strata.

### 10. `WUWA_AEMEATH_AV_HUMAN_RETRIEVAL_CROSSWALK.md`

Human-facing retrieval map from exact flow/source locators to public chapter/quest names, distinctive lines, suggested YouTube terms, mapping confidence, expected witness type, and acquisition state.

## Current completion assessment

| Completion state | Assessment | Reason |
|---|---|---|
| `textually_reconstructed` | **supported** | Complete accepted textual/contextual corpus was read and synthesized with identity/state controls |
| `machine_voice_profiled` | **not claimed** | Coverage and basic measurements are complete; the stronger machine protocol's feature/normalization/clustering gate is unmet |
| `audiovisual_hierarchy_completed` | **provisionally supported** | Material source classes and claim-driven targets are authority-typed and human-routed; actual channel-wide promotional inventory remains non-exhaustive |
| `audiovisually_hardened` | **false** | No nominated AV witness has been directly reviewed |
| `integrated_reconstruction_completed` | **false** | Materially relevant AV remains available and unreviewed |
| `model_compiled` | **not claimed** | Operational Markdown profile exists; no canonical machine-readable package is promoted |
| `fidelity_checked` | **supported for pre-AV model only** | Adversarial textual/model tests were performed; AV-sensitive tests remain open |
| `human_performance_partially_reviewed` | **false** | No structured human listening |
| `human_performance_hardened` | **false** | No structured human listening |

## Recommended reading order

1. this entrypoint;
2. `WUWA_AEMEATH_CHARACTER_DEEP_DIVE_PRE_AV.md`;
3. `WUWA_AEMEATH_EVIDENCE_AND_FALSIFICATION_MATRIX.md`;
4. `WUWA_AEMEATH_RELATIONSHIP_AND_STATE_PROFILE.md`;
5. `WUWA_AEMEATH_IDENTITY_EMBODIMENT_AND_SHELL_PROFILE.md`;
6. `WUWA_AEMEATH_ORDINARY_LIFE_AND_PREFERENCES_PROFILE.md`;
7. `WUWA_AEMEATH_SPEECH_AND_MACHINE_VOICE_PROFILE_PRE_AV.md`;
8. `WUWA_AEMEATH_RECONSTRUCTIVE_PROFILE_PRE_AV.md`;
9. `WUWA_AEMEATH_MODEL_FIDELITY_AND_STRESS_TEST_PRE_AV.md`;
10. AV nomination plan;
11. AV human retrieval crosswalk.

## Promotion boundary

This packet should not be copied into Git in isolation. A promoted Aemeath character tranche would also need, as applicable:

- an Aemeath character current-state router;
- WUWA character index update;
- claim/evidence index update;
- title-wide state and relationship ledgers;
- chronology and open-question updates;
- current-state/corpus-map update;
- manifest/audit and tracked-path regeneration;
- explicit notation that AV review and optional human listening remain open.

The proposed generic AV framework files are not yet committed. Until they are adopted, packet front matter should continue to name them as proposed methods rather than current Git authority.

## Source notation

Narrative locators are written as `flow/action`, with talk indices or text keys added where needed—for example `11858/1`, `MAIN_YHX_105_11`. Favor materials use `FavorStory_121003` or `FavorWord_121005_Content`. Every such shorthand is recoverable through the Drive scene ledger, raw flow states, character source package, and text witnesses at the pinned commit.

## One-sentence working thesis

> **Aemeath learns that becoming a savior is morally different from making oneself disposable: responsibility becomes hers only when the people she loves retain the right to know, object, help, grieve, and choose beside her.**
