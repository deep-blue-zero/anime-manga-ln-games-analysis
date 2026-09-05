---
series: WUWA
character: Denia
artifact_type: analysis_packet_entrypoint
scope: DENIA_SOURCE_3_6_0_PRE_AV
analysis_generation: DENIA_PRE_AV_V0_1
status: active_provisional
release_state: local_working_draft
foundation_authority: primary_and_deterministic_derived_evidence
analysis_authority_state: local_working_draft_not_promoted
source_generation: arikatsu-3.6.0-353f2eae-expanded-v0.3.0-ko
source_commit: 353f2eaed119bc9f680eab92807d20ac75a79b40
text_authority: zh-Hans
localization_witnesses: [ja, ko, en]
drive_character_bridge: 1RCrb3zpoAF05f9_YEC4CJ62zY9CoehrV
drive_voice_view: 1XdRw8wloHQiRTAvhIBS8hcNpAYhz7Oqy
governing_protocols:
  - WUWA_ANALYTICAL_METHOD.md
  - WUWA_CHARACTER_RECONSTRUCTION_PROTOCOL.md V0.2
  - WUWA_CHARACTER_FOLDER_CONTRACT.md
  - WUWA_MACHINE_VOICE_ANALYSIS_PROTOCOL.md
  - WUWA_AUDIOVISUAL_EVIDENCE_COLLECTION_PROTOCOL_V0_1.md proposed
  - WUWA_AUDIOVISUAL_HUMAN_RETRIEVAL_CROSSWALK_SPEC_V0_1.md proposed
  - WUWA_AV_EVIDENCE_MANIFEST_SPEC_V0_1.md proposed
intended_canonical_home: series/wuthering-waves/04 Character Analysis/Denia/
do_not_use_as_current_git_authority: true
created: 2026-09-03
---

# Denia reconstruction dossier — pre-audiovisual V0.1

## Purpose

This packet is a source-grounded reconstruction of **Denia / 达妮娅 / ダーニャ / 데니아** against the frozen *Wuthering Waves* 3.6.0 evidence generation. It applies the current Wuthering Waves character-analysis framework together with the proposed audiovisual collection and human-retrieval refinements that have not yet been committed to Git.

The packet is an analytical working set, not a publication event. It does not update the Wuthering Waves character index, title-wide state and relationship ledgers, claim-evidence index, current-state map, corpus manifest, or repository audit. Those changes must occur atomically when the owner authorizes promotion.

All files in this directory therefore carry the same authority boundary:

> **Local working analysis derived from canonical Drive evidence; not current Git authority.**

## Current analytical thesis

Denia is not best understood as an empty nihilist who discovers that friendship is real, nor as a liar whose false student persona conceals an already complete authentic self. She is a person **produced through imitation**.

The Fractsidus selected her as a vessel because she appeared to possess nothing: no secure origin, no verified family, no stable birthday, no trusted biography, and no attachments thought strong enough to resist Aleph-1. She then learned human conduct as performance. A smile was a low-cost social tool. Gentleness was a word she researched. Emotion could be studied, copied, and deployed. Student records could be falsified. Friendship could function as cover. Even a birthday could be invented as a useful fiction.

Yet repeated performance did not remain external. The copied smile altered how Sigrika approached her. The student role gave her classes, games, sweets, teachers, photographs, nicknames, irritation, embarrassment, and anticipated tomorrows. Lies acquired witnesses; witnesses acquired claims on her; and those claims became difficult to erase. The allegedly empty vessel developed what the Fractsidus dismisses as a fragile, aching “heart of the weak.” Her central movement is therefore not:

> deception → honesty

It is closer to:

> imposed emptiness  
> → human imitation as infiltration and survival  
> → performances that generate real attachment  
> → recognition that a constructed life can still be hers  
> → an attempt to author even her own death  
> → resistance to the owners who define her as replaceable  
> → a still-incomplete commitment to remain, choose, and protect.

The governing ethical question is **authorship**. Who gets to define which parts of Denia are false? Does uncertain origin invalidate present attachment? Can a fabricated birthday become real through ritual, witness, and future obligation? When does protective concealment become another form of control? What separates Denia's imitation, which accumulates answerability, from the Grand Architect's imitation, which appropriates and replaces?

Her answer is not a proof that the universe has meaning. Denia continues to regard the Void as unbeatable and suffering as structurally unfair. What changes is narrower and more concrete: she can hear her own heartbeat, remember shared laughter, fear loneliness, anticipate another cake, preserve a photograph, give names to other beings, and want tomorrow. Finite relational meaning does not defeat cosmic nihilism. It gives her a reason not to surrender jurisdiction over her life to it.

## Source boundary

The declared evidence boundary is the frozen Denia V0.1 Drive package built from:

- pinned Arikatsu source commit `353f2eaed119bc9f680eab92807d20ac75a79b40`;
- normalized generation `arikatsu-3.6.0-353f2eae-expanded-v0.3.0-ko`;
- Chinese as the primary semantic witness;
- Japanese, Korean, and English as aligned official localization witnesses;
- installed-client voice objects and content-addressed lossless derivatives as a distinct raw-media authority layer.

The accepted corpus reports:

| Surface | Count / state |
|---|---:|
| Accepted direct story/message occurrences | 439 |
| Source-voiced direct occurrences | 376 |
| Explicitly unvoiced direct occurrences | 63 |
| Favor stories | 5 |
| Favor/archive voice entries | 93 |
| Direct semantic voice lines | 469 |
| Four-language-complete semantic lines | 469 / 469 |
| Render associations | 1,876 |
| Runtime object rows | 1,864 |
| Unique PCM/FLAC objects | 1,852 |
| Retained FLAC bytes | 584,057,924 |
| Scene/action ledger records | 167 |
| Scene/action records containing direct Denia speech | 97 |
| Complete selected raw flow-state rows | 165 |
| Contextual text keys | 2,733 |
| Quest-reference records | 81 across 20 quest IDs |
| Relevant WavesLine records | 5 context records; no Denia-owned contact corpus established |
| Unresolved accepted identity candidates | 0 |
| Missing expected accepted voice mappings | 0 |
| Structured human performance annotations | 0 |
| Exported image/video witnesses | 0 |

These denominators are intentionally not interchangeable. A context record can contain many speakers. A quest-reference wrapper is not a full quest graph. A runtime render is not a new semantic line. Five relevant phone-message records do not establish a Denia-owned direct-message corpus; the retained records are contextual routes involving Arman or Sigrika.

The role package's `appearance_links` field is not treated as the story census. Occurrence and scene ledgers control narrative retrieval.

## Identity boundary

The reconstruction accepts:

- `200144` — main/source-named Denia;
- `850633` — explicitly historical/past-memory Denia, retained as a state rather than flattened into present behavior.

The source architecture also recognizes an offscreen-voice technical identity (`250055`), but no such rows enter the accepted direct denominator in this package. Two generic-speaker nominations at flow `8855/action 4` are rejected because the unnamed spear-user is immediately identified as Avidius. Generic speaker `178` is therefore never globally mapped to Denia.

Trial and duplicate role rows in `ROLE_VARIANTS.json` are technical variants, not additional Denia persons or developmental states.

Unlike Aemeath, Denia has no separately retained associated shell in this package. The main identity problem is not body-copy separation but **origin uncertainty and constructed social identity**: she cannot establish whether she was naturally born, manufactured, biologically copied, or furnished with implanted memories. The dossier treats that uncertainty as source fact and refuses to solve it through inference.

Gameplay labels such as Stagecraft Form and Breakdown Form are retained as ludic/representational forms. They are not promoted into independent personhood or developmental states without story or direct audiovisual support.

## Audio boundary

The complete accepted semantic voice set contains 469 lines, each with Chinese, English, Japanese, and Korean render coverage. The current machine layer preserves duration, RMS level, peak level, silence fraction, channel count, hashes, and exact source-to-render routing.

That is a strong technical base but does **not** satisfy the full `WUWA_MACHINE_VOICE_ANALYSIS_PROTOCOL.md`. The present layer does not yet provide the required robust pitch/F0 analysis, speaking-rate and articulation-rate proxies, pause segmentation, text-length controls, state-conditioned normalization, clustering, stability checks, or claim-driven cohort synthesis. Accordingly:

- complete media coverage is claimed;
- current basic signal measurements are reported;
- `machine_voice_profiled` is **not** claimed;
- no emotion, sincerity, flirtation, warmth, deception, or actor-intention label is inferred from the measurements;
- human listening remains an optional terminal addendum.

Each language has 421 mono and 48 stereo renders. The package reports no multichannel object requiring a spatial-layout adjudication beyond those stereo files. Stereo or scene-associated material is still not automatically an isolated vocal stem.

## Audiovisual boundary and updated protocol use

No direct image or video witness is included. `ASSET_REFERENCE_INDEX.json` contains source references only. Therefore the dossier makes no source-grounded claim about:

- facial acting;
- gaze;
- gesture;
- body language;
- blocking or interpersonal distance;
- camera position or lensing;
- lighting;
- editing rhythm;
- animation performance;
- costume behavior in motion;
- music placement in a scene;
- performed-voice character impressions.

The updated AV workflow is nevertheless applied prospectively. This packet includes:

1. a claim-driven AV hierarchy and nomination plan;
2. a human-retrieval crosswalk mapping internal locators to public story families, dialogue anchors, and suggested searches;
3. four authority dimensions: diegetic, representational, interpretive, and production-framing;
4. separate treatment of core diegetic AV, matched multilingual promotional AV, unmatched official promotional AV, and official static media;
5. explicit edit-equivalence and semantic-equivalence requirements for matched multilingual groups;
6. no empty `AV_EVIDENCE_MANIFEST.jsonl`, because no actual witness has yet been acquired.

Public story names and search strings are navigation aids, not evidence. Any acquired video or image must receive a stable witness ID, provenance, source URL, language, hashes or other integrity fields where possible, timecode, authority classification, and source-locator link before analytical use.

## Packet contents and analytical responsibilities

### 1. `WUWA_DENIA_CHARACTER_DEEP_DIVE_PRE_AV.md`

The source-facing interpretive center: identity, developmental architecture, lies, imitation, personhood, nihilism, usefulness, birthday, relationships, ordinary life, ethics, rival readings, and bounded predictions.

### 2. `WUWA_DENIA_EVIDENCE_AND_FALSIFICATION_MATRIX.md`

A claim-level matrix separating source fact, stable observation, inference, candidate thesis, counterevidence, and future falsification target.

### 3. `WUWA_DENIA_RELATIONSHIP_AND_STATE_PROFILE.md`

The canonical local home for developmental states, recurring operational contexts, relationship transitions, recipient modifiers, and continuity limits.

### 4. `WUWA_DENIA_ORDINARY_LIFE_AND_PREFERENCES_PROFILE.md`

A source-fact / analytical-implication / extrapolation-limit profile covering sleep, food, games, classes, festivals, photography, motorcycles, music, color, study, gifts, humor, boredom, rest, and everyday social behavior.

### 5. `WUWA_DENIA_SPEECH_AND_MACHINE_VOICE_PROFILE_PRE_AV.md`

Textual register and rhetoric plus bounded machine-acoustic accounting. No unreviewed acting interpretation.

### 6. `WUWA_DENIA_IDENTITY_DECEPTION_AND_PERSONHOOD_PROFILE.md`

A Denia-specific specialist artifact covering uncertain origin, name, birthday, imitation, smile, memory, truth categories, creator/creation claims, replaceability, and the conditions under which a constructed social identity becomes answerable and real.

### 7. `WUWA_DENIA_RECONSTRUCTIVE_PROFILE_PRE_AV.md`

An operational model for state selection, decision rules, stable drives, vulnerabilities, relationship-conditioned behavior, ordinary-life prediction, speech constraints, and mandatory abstentions.

### 8. `WUWA_DENIA_MODEL_FIDELITY_AND_STRESS_TEST_PRE_AV.md`

An adversarial test against nihilist flattening, “mask versus real self” simplification, liar archetype leakage, romance inflation, trauma-only readings, indiscriminate self-sacrifice, and unsupported AV/performance claims.

### 9. `WUWA_DENIA_AUDIOVISUAL_EVIDENCE_NOMINATION_PLAN.md`

Defines which story, promotional, combat, and static witnesses should be collected and what claim each could change.

### 10. `WUWA_DENIA_AV_HUMAN_RETRIEVAL_CROSSWALK.md`

Maps AV targets to internal source locators, public chapter/quest families, dialogue anchors, expected witness types, search terms, mapping confidence, and future acquisition fields.

The README is the packet entrypoint and routing authority within this local working set. It is not a substitute for any topical artifact above.

## Current completion assessment

| Completion state | Assessment | Basis |
|---|---|---|
| `textually_reconstructed` | **supported** | accepted identity boundary, complete contextual reading of the supplied character package, favor/archive material, selected flow rows, and falsification pass |
| `audiovisual_hierarchy_completed` | **provisionally supported** | source classes and claim-driven targets identified; human retrieval mapped; no acquisition yet |
| `fidelity_checked` | **supported for the pre-AV model** | adversarial stress test and mandatory abstentions recorded |
| `machine_voice_profiled` | **not claimed** | complete media and basic signal measurements, but full protocol feature/normalization/clustering requirements unmet |
| `audiovisually_hardened` | **false** | no direct AV witness reviewed |
| `integrated_reconstruction_completed` | **false** | relevant AV remains materially available but unreviewed |
| `model_compiled` | **not claimed as canonical** | reconstructive Markdown profile exists; no promoted machine-readable package |
| `human_performance_partially_reviewed` | **false** | no structured listening performed |
| `human_performance_hardened` | **false** | no structured listening performed |

## Recommended reading order

1. This README.
2. `WUWA_DENIA_CHARACTER_DEEP_DIVE_PRE_AV.md`.
3. `WUWA_DENIA_EVIDENCE_AND_FALSIFICATION_MATRIX.md`.
4. `WUWA_DENIA_IDENTITY_DECEPTION_AND_PERSONHOOD_PROFILE.md`.
5. `WUWA_DENIA_RELATIONSHIP_AND_STATE_PROFILE.md`.
6. `WUWA_DENIA_ORDINARY_LIFE_AND_PREFERENCES_PROFILE.md`.
7. `WUWA_DENIA_SPEECH_AND_MACHINE_VOICE_PROFILE_PRE_AV.md`.
8. `WUWA_DENIA_RECONSTRUCTIVE_PROFILE_PRE_AV.md`.
9. `WUWA_DENIA_MODEL_FIDELITY_AND_STRESS_TEST_PRE_AV.md`.
10. `WUWA_DENIA_AUDIOVISUAL_EVIDENCE_NOMINATION_PLAN.md`.
11. `WUWA_DENIA_AV_HUMAN_RETRIEVAL_CROSSWALK.md`.

For AV acquisition, reverse the last two only after reading the nomination responsibility: know **why** a witness is wanted before using the crosswalk to locate it.

## Promotion boundary

A later owner-authorized Git promotion should not simply copy this directory and call the transaction complete. The same change should, as applicable:

- create or update Denia's character current-state router;
- update `07 Evidence and Indexes/WUWA_CHARACTER_INDEX.md`;
- update the WUWA claim-evidence index;
- update title-wide character-state, relationship, chronology, and open-question ledgers;
- update `CURRENT_STATE_AND_CORPUS_MAP.md`;
- update corpus manifests and repository audits;
- preserve this generation's source boundary;
- identify which local filenames become canonical topical homes and whether any need renaming;
- keep the uncommitted AV methods marked proposed unless they have been promoted in the same or an earlier transaction.

No document here supersedes a current Git artifact until that promotion occurs.

## Source notation

- `flow 12588/action 5` means the action-level locator under the pinned `flowstate.json` row.
- `FavorStory_12110X_Content` and `FavorWord_1211XX_Content` are stable source text keys within this generation.
- English quotations are localization witnesses unless the surrounding analysis explicitly invokes Chinese wording.
- Public quest/PV names in the AV crosswalk are human retrieval labels, not deterministic source identity.
- Generated predictions and stress-test scenarios are not evidence and never feed back into the claim ledger.

## One-sentence working thesis

> **Denia is the lie that learned to want tomorrow: a manufactured vessel who copied human feeling as technique until performance accumulated memory, attachment, guilt, and expectation—and who becomes most fully a person not when every uncertainty is solved, but when she claims authorship over what those constructed ties require of her.**
