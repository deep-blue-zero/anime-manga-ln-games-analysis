---
title: "To Be Hero X V2 — Multi-Document Synthesis Architecture"
project: "To Be Hero X V2"
artifact_type: "synthesis_architecture"
version: "1.5"
created: "2026-08-13"
last_updated: "2026-10-25"
status: "governing"
architecture_lifecycle: "STABILIZED"
current_entrypoint: "TBHX_CURRENT_STATE_AND_CORPUS_MAP.md"
governing_method: "TBHX_V2_ANALYTICAL_METHOD.md"
character_reconstruction_method: "TBHX_V2_CHARACTER_RECONSTRUCTION_METHOD.md"
primary_spoken_language: "Mandarin Chinese"
primary_subtitle_script: "Simplified Chinese (zh-Hans)"
spoiler_scope: "Season 1, Episodes 1-24"
source_drive_folder_id: "11D1wSxD5OsF3MgRzHuTw9rUZlTHtpVME"
analysis_drive_folder_id: "1pD8ayXzaZpwX4td3Dl559bgm3z-oUSSs"
crosswalk_lifecycle: "live Phase 1 updates -> Phase 2 audit -> Phase 7 evidence audit -> Phase 9 freeze"
targeted_av_evidence_lifecycle: "post-freeze clip/still intake -> targeted evidence ledger -> topical propagation -> claim-revision routing -> Phase 7 locator backfill"
---

# To Be Hero X V2 — Multi-Document Synthesis Architecture

## 1. Architectural goal

The V2 corpus should not become another long chat transcript or a pile of disconnected character essays. Its structure must preserve four things simultaneously:

1. **episode-local understanding** in broadcast order;
2. **longitudinal correction** as perspectives and chronology are revised;
3. **specialist synthesis** by character, system, language, and form;
4. **source traceability** back to Mandarin audio and visual evidence.

The architecture is deliberately layered. Episode documents are the observation layer. Ledgers are the memory and correction layer. Specialist documents are the analytical layer. The full-series synthesis is the reader-facing literary argument. The evidence/locator layer prevents that argument from floating free of the source.

---

## 2. Proposed Google Drive tree

The existing `Anime bundle metadata` directory remains untouched.

```text
To Be Hero X — analytical material root/
├── Anime bundle metadata/                  # existing pipeline reports; preserve
├── 00 V2 Frameworks/
│   ├── TBHX_CURRENT_STATE_AND_CORPUS_MAP.md        # sole current entrypoint (§10.2)
│   ├── TBHX_V2_CORPUS_AUDIT_AND_SOURCE_PROFILE.md
│   ├── TBHX_V2_ANALYTICAL_METHOD.md
│   ├── TBHX_V2_CHARACTER_RECONSTRUCTION_METHOD.md  # governs Document 20 (§10.1)
│   └── TBHX_V2_MULTI_DOCUMENT_SYNTHESIS_ARCHITECTURE.md
├── 01 V2 Episode Deep Readings/
│   ├── TBHX_V2_E01_DEEP_READING.md
│   ├── ...
│   └── TBHX_V2_E24_DEEP_READING.md
├── 02 V2 Longitudinal Ledgers/
│   ├── TRUST_FEAR_AND_POWER_MECHANICS_LEDGER.md
│   ├── PUBLIC_NARRATIVE_PRIVATE_EVENT_LEDGER.md
│   ├── BROADCAST_ORDER_AND_DIEGETIC_CHRONOLOGY_LEDGER.md
│   ├── HERO_IMAGE_PERSONHOOD_AND_IDENTITY_LEDGER.md
│   ├── INSTITUTIONS_MEDIA_RANKINGS_AND_POLITICAL_ECONOMY_LEDGER.md
│   ├── CHARACTER_RELATIONSHIP_AND_RECOGNITION_LEDGER.md
│   ├── CHINESE_LANGUAGE_VOICE_AND_NAMING_LEDGER.md
│   ├── VISUAL_AUDIO_MOTIF_AND_FORM_LEDGER.md
│   ├── CLAIM_REVISION_AND_CONFIDENCE_LEDGER.md
│   └── V1_TO_V2_REVISION_LEDGER.md
├── 03 V2 Specialist Syntheses/
│   ├── 01 Characters and Relationships/
│   ├── 02 Systems Institutions and Themes/
│   └── 03 Language Audio and Visual Form/
├── 04 V2 Evidence and Revision/
│   ├── PRIMARY_SOURCE_LOCATOR_LEDGER.md
│   ├── CLAIM_TO_SOURCE_ROUTING_INDEX.md
│   ├── SUBTITLE_AND_TRANSLATION_AUDIT.md
│   ├── TBHX_NAME_LOCALIZATION_CROSSWALK.md
│   ├── TBHX_V2_TARGETED_AV_EVIDENCE_LEDGER.md
│   ├── TBHX_COMPARATIVE_REFERENCE_MATRICES_AND_OPEN_QUESTIONS.md  # Phase 6, unnumbered (§10.1)
│   ├── Targeted AV Evidence/
│   │   └── TBHX_E##_SHORT_DESCRIPTIVE_SCOPE/
│   └── PROVENANCE_AND_CORRECTION_LOG.md
├── 05 V2 Full Series Synthesis/
│   ├── 00_READER_GUIDE_AND_READING_ORDER.md  # optional, subordinate to the entrypoint (§10.2)
│   └── TBHX_FULL_SERIES_SYNTHESIS.md
├── 90 V1 Historical Analysis/
│   └── [backported V1 analyses and transcript extracts]
└── 99 V2 Archive and Delivery/
    ├── CORPUS_MANIFEST.md
    ├── DELIVERY_AUDIT.md
    ├── SHA256SUMS.txt
    └── release archives/
```

The `90` directory is intentionally segregated. V1 should remain available for intellectual history and comparison without being mistaken for V2 source evidence.

**v1.5 layout note.** The tree above is the original Drive design, amended in v1.5 only where an artifact identity changed. It is not a statement of current inventory: the live Git layout and current authority are recorded in `TBHX_CURRENT_STATE_AND_CORPUS_MAP.md` §3, and a folder appears with its first accepted artifact. Several planned `04` apparatus files were never created as separate artifacts; §10.11 records where their responsibilities now live, so they must not be created merely to match this tree.

---

## 3. Phase structure

### Phase 0 — Corpus audit, source lock, and V1 hypothesis import

Outputs:

- `TBHX_V2_CORPUS_AUDIT_AND_SOURCE_PROFILE.md`
- finalized source inventory / identity records
- initial `V1_TO_V2_REVISION_LEDGER.md`
- locator convention
- source-access exceptions list

Goal: establish what evidence exists and convert V1 conclusions into testable hypotheses.

### Phase 1 — Sequential episode deep reading, Episodes 1–24

Output one canonical artifact per episode:

`TBHX_V2_E01_DEEP_READING.md` through `TBHX_V2_E24_DEEP_READING.md`

The episode sequence remains in broadcast order. Each document freezes a prospective reading, then later receives clearly labeled retrospective addenda.

This phase is the analytical backbone. Specialist synthesis should not replace it.

During Phase 1, maintain `TBHX_NAME_LOCALIZATION_CROSSWALK.md` as a live `active_provisional` evidence/index artifact. Update the **same Drive object in place** whenever an episode or official multilingual source establishes a new name, hero/person equivalence, title/address relation, or localization divergence. Frozen episode bodies are not rewritten merely to hide earlier uncertainty; the crosswalk and revision ledgers route old forms to current authority.

### Phase 2 — Longitudinal ledger stabilization

Ledgers are updated during Phase 1 but receive a dedicated audit after Episode 24.

The most important deliverables are:

- definitive broadcast/diegetic timeline mapping;
- repeated-event perspective map;
- Trust/Fear rule table with exceptions;
- hero-image/personhood state table;
- institutional and ranking map;
- relationship-state map;
- Chinese terminology/voice index;
- V1→V2 claim disposition;
- **first systematic audit of `TBHX_NAME_LOCALIZATION_CROSSWALK.md`** against all 24 episodes and official multilingual naming sources.

#### Post-freeze targeted audiovisual evidence

When a later analytical question requires direct reinspection of a short continuous sequence, use `TBHX_V2_TARGETED_AV_EVIDENCE_LEDGER.md` as the canonical intake/routing surface rather than rewriting the frozen episode body or creating a new mini-synthesis.

Store the reviewed media under `04 V2 Evidence and Revision/Targeted AV Evidence/` in an episode-scoped packet folder. The ledger must distinguish raw clips/stills from derived contact sheets, record locator/hash metadata where recoverable, identify what motion or audio adds beyond screenshot/transcript evidence, assign a revision transition, and route only the mature consequence into the appropriate mutable ledger or later specialist synthesis.

The targeted AV layer is **evidence infrastructure**, not a new analytical phase. It may be updated at any point before archival freeze and should be consulted by `CLAIM_REVISION_AND_CONFIDENCE_LEDGER.md` and Phase-7 source routing whenever a mature claim depends on a post-freeze reinspection.

### Phase 3 — Character and relationship syntheses

The following documents are the default plan. They may be merged only when the episode evidence shows that two characters cannot be analyzed responsibly in isolation.

1. `06_LIN_LING_NICE_MOON_AND_THE_REPLACEMENT_HERO.md`
2. `07_YANG_CHENG_ESOUL_POMELO_AND_INHERITED_HEROISM.md`
3. `08_LUCKY_CYAN_HOPE_SURVIVORHOOD_AND_PUBLIC_NEED.md`
4. `09_QUEEN_ORDER_GOVERNANCE_SOLITUDE_AND_REFORM.md`
5. `10_LUO_LI_CUTENESS_TECHNOLOGY_GRIEF_AND_SELF_AUTHORSHIP.md`
6. `11_GHOSTBLADE_SILENCE_VIOLENCE_FATHERHOOD_AND_REFUSAL.md`
7. `12_LITTLE_JOHNNY_BIG_JOHNNY_FAMILY_MONSTERHOOD_AND_RECOGNITION.md`
8. `13_DRAGON_BOY_SMILE_PAIN_FEAR_AND_PUNITIVE_HEROISM.md`
9. `14_AHU_LOCAL_HEROISM_BELIEF_MYTH_AND_MISRECOGNITION.md`
10. `15_X_ZERO_GODHOOD_FATE_AND_THE_LIMIT_OF_PUBLIC_WILL.md`
11. `16_CROSS_ARC_RELATIONSHIPS_ALLIANCES_MENTORSHIP_AND_RECOGNITION.md`

These filenames are architectural targets, not conclusions about which character is morally central.

### Phase 4 — System, institution, and thematic syntheses

Default documents:

1. `01_NARRATIVE_ARCHITECTURE_CHRONOLOGY_PERSPECTIVE_AND_RECONTEXTUALIZATION.md`
2. `02_TRUST_FEAR_POWER_AND_SOCIAL_ONTOLOGY.md`
3. `03_HEROISM_POWER_LEGITIMACY_DIGNITY_AND_COERCION.md`
4. `04_AGENCIES_COMMISSION_RANKINGS_MEDIA_RESEARCH_AND_POLITICAL_ECONOMY.md`
5. `05_PUBLIC_NARRATIVE_BRANDING_CELEBRITY_MYTH_AND_COLLECTIVE_BELIEF.md`

These establish the world-model before the final character arguments are generalized into a full-series thesis.

### Phase 5 — Language, audio, visual-form, and character-modeling syntheses

Default architecture-defined specialist documents:

1. `17_MANDARIN_DIALOGUE_VOICE_NAMING_REGISTER_AND_JAPANESE_REFERENCE_AUDIT.md`
2. `18_VISUAL_FORM_ANIMATION_MODES_COLOR_EDITING_SCREENS_AND_SPECTACLE.md`
3. `19_MUSIC_SOUND_SILENCE_PERFORMANCE_AND_THE_PUBLIC_VOICE.md`
4. `20_CHARACTER_BEHAVIOR_PERSONALITY_SPEECH_AND_SITUATIONAL_MODELING_REFERENCE.md`

Companion appendix:

- `TBHX_NAME_LOCALIZATION_CROSSWALK.md` — canonical appendix reconciling Mandarin names, standardized pinyin/V2 analytical forms, English-localized names, Japanese renderings, titles/aliases, and identity-equivalence notes.

Documents 17–19 establish the linguistic and audiovisual evidence needed for Document 20. Document 20 is the reconstruction-oriented integration layer: it does not replace the Phase-3 character monographs, but converts their mature psychological and relational findings plus Phase-5 speech/performance evidence into bounded models of how sufficiently evidenced characters are likely to perceive, decide, speak, act, and recover in situations not directly depicted by the source.

These are not appendices. *To Be Hero X* is unusually dependent on mediated speech, public performance, image construction, and changes in representational mode. Formal and behavioral reconstruction analysis belongs in the main corpus.

#### Required Phase-5 E05–E07 audiovisual-form microsequence audit

After Document 17 and **before Documents 18–19**, complete one bounded continuous-video/audio evidence pass:

`TBHX_V2_E05-E07_AV_FORM_MICROSEQUENCE_AUDIT.md`

Canonical home: `04 V2 Evidence and Revision/Targeted AV Evidence/`. This is a formal audiovisual evidence audit supporting the visual-form and music/sound syntheses, not a replacement episode deep reading and not a duplicate of the Yan Mo causal audit below. The prospective bodies of `TBHX_V2_E05_DEEP_READING.md`, `TBHX_V2_E06_DEEP_READING.md`, and `TBHX_V2_E07_DEEP_READING.md` remain frozen.

Primary responsibility: recover what continuous motion, editing, performance timing, original Mandarin audio, music, silence, sound bridges, and shot duration add beyond screenshots/transcripts. English subtitles may be used as a locating/navigation layer; Mandarin dialogue/audio remains primary and the aligned Japanese track remains a secondary semantic witness.

Minimum required sequences:

**Episode 05 — role, rescue, and awakening**

- the climax beginning before Yang reaches/rescues Pomelo/Yòuzi and continuing through the first E-Soul manifestation;
- veteran E-Soul's mask/covenant speech crosscut against powerless Yang's continuing rescue attempt;
- Pomelo/Yòuzi's recognition call and the exact audiovisual transition into manifestation;
- the immediate aftermath through the “best performance/stage” language and Shang Chao naming Yang beneath the role.

Test whether dialogue, score, sound continuity, and editing make the veteran's speech function as an inherited/parallel ethical register for Yang's action, and whether the formal ordering strengthens the existing claim that **agency precedes amplification**.

**Episode 06 — mediation, public capture, and mistaken visual identity**

- representative viral/public-transformation material where private rescue becomes scalable hero image/Trust;
- technical training and the transition from relational heroism into managed/public hero production where useful to Documents 18–19;
- scandal/exoneration/coronation material where editing or sound materially changes the interpretation of narrative capture;
- the prototype E-Soul helmet and Shang Chao shooting sequence, preserving enough lead-in/out to establish visual mistaken-target logic and the irony that hidden technical/support labor becomes lethally misrecognized as the visible hero image.

The E06 shooting sequence may be cited by both this formal audit and the separate Yan Mo causal audit, but each document must retain its distinct responsibility: **formal construction** here; **causal/claim adjudication** there.

**Episode 07 — grief, duel, spectacle, concern, and retrospective revelation**

- Shang Chao's funeral and Yang's counterweight declaration;
- MG's pressure on veteran E-Soul to accept the duel;
- Yan Mo and Yang's `电光斩` tactical discussion and the engineered-publicity sequence;
- a substantial uninterrupted section of the E-Soul duel, including **Lucky Cyan's visible/vocal concern and its juxtaposition with the duel's violence and crowd/spectacle register**;
- the duel climax, veteran E-Soul's death, and Trust consolidation;
- the complete Yan Mo/“Uncle Rock” ending reveal montage through the Da Hu/Er Hu concrete disposal.

The Lucky Cyan material must test, rather than assume, whether the episode creates an **ethical counter-register** to competitive spectacle. At minimum audit:

- what exactly Lucky Cyan is watching and to whom/what her concern is directed;
- whether duel/crowd audio continues over her reaction shots;
- whether music changes, thins, interrupts, resolves, or bridges across her appearances;
- shot duration and return-cut logic between concern and bodily violence;
- whether crowd excitement and her affect are formally contrasted;
- whether later Lucky Cyan knowledge legitimately strengthens a retrospective reading without being retrojected into the frozen E07 prospective body;
- whether the sequence anticipates the later series-wide distinction between ranking/spectacle and person-level recognition.

Across all three episodes, record source/program timestamps, clip/hash metadata where recoverable, shot/motion boundaries, dialogue/audio bridges, music entrance/exit points, silence, visible performance cues, and the exact interpretive consequence of each formal observation. Do not infer instrumentation, leitmotif identity, prosody, or mix behavior that has not been directly auditioned.

Required routing after completion:

- `18_VISUAL_FORM_ANIMATION_MODES_COLOR_EDITING_SCREENS_AND_SPECTACLE.md`;
- `19_MUSIC_SOUND_SILENCE_PERFORMANCE_AND_THE_PUBLIC_VOICE.md`;
- `VISUAL_AUDIO_MOTIF_AND_FORM_LEDGER.md`;
- `TBHX_V2_TARGETED_AV_EVIDENCE_LEDGER.md`;
- `07_YANG_CHENG_ESOUL_POMELO_AND_INHERITED_HEROISM.md` and/or `08_LUCKY_CYAN_HOPE_SURVIVORHOOD_AND_PUBLIC_NEED.md` only where the formal evidence materially revises or strengthens their mature retrospective claims;
- Phase-7 locator/claim routing for any final synthesis claim that depends on these sequences.

This audit should be completed **before drafting Documents 18 and 19**, so those syntheses can incorporate continuous audiovisual evidence rather than relying on post-hoc correction.

#### Required character reconstruction/modeling synthesis — `20_CHARACTER_BEHAVIOR_PERSONALITY_SPEECH_AND_SITUATIONAL_MODELING_REFERENCE.md`

Document 20 is mandatory after Documents 18 and 19 and before Phase-5 closure. It has one distinct analytical responsibility: **convert the mature character corpus into evidence-bounded situational models that support plausible reconstruction of behavior, personality, speech, and decision-making in novel contexts without collapsing into generic fanfiction characterization**.

Canonical home: `03 V2 Specialist Syntheses/03 Language Audio and Visual Form/`.

Document 20 must integrate rather than duplicate:

- Phase-3 Specialists 06–16 for mature personality, worldview, developmental history, relationship structure, ethical commitments, wounds, and failure modes;
- `CHARACTER_RELATIONSHIP_AND_RECOGNITION_LEDGER.md` for relationship-conditioned behavior and recognition states;
- `17_MANDARIN_DIALOGUE_VOICE_NAMING_REGISTER_AND_JAPANESE_REFERENCE_AUDIT.md` for lexical/discourse voice, address, modality, identity grammar, and speech-operation profiles;
- `18_VISUAL_FORM_ANIMATION_MODES_COLOR_EDITING_SCREENS_AND_SPECTACLE.md` for gesture, posture, movement, visual self-presentation, framing-dependent behavioral evidence, and embodied performance;
- `19_MUSIC_SOUND_SILENCE_PERFORMANCE_AND_THE_PUBLIC_VOICE.md` for directly auditioned acoustic modulation, pause, tempo, vocal-performance, silence, and stress-state evidence;
- directly reviewed Mandarin audiovisual evidence whenever a reconstruction claim depends on timing, tone, gesture, or behavior not adequately preserved by transcript-level evidence.

For each sufficiently evidenced character, the modeling reference should include at least:

1. **baseline temperament and behavioral set point** — ordinary affect, sociability, initiative, inhibition, patience, conflict style, and default public/private presentation;
2. **values, worldview, and salience map** — what the character notices first, what they consider threatening, admirable, humiliating, unjust, desirable, or irrelevant;
3. **decision heuristics** — recurring rules of thumb used under uncertainty, including how the character trades loyalty, self-protection, status, truth, risk, care, and institutional obligation;
4. **emotional needs, wounds, defenses, and trigger conditions** — including how those structures alter behavior without being treated as deterministic diagnoses;
5. **relationship-conditioned variants** — how behavior changes with intimates, family, mentors, rivals, subordinates, institutions, strangers, publics, and adversaries;
6. **speech-generation constraints** — vocabulary, sentence shape, modality, self-reference, address, metaphor, register switching, likely evasions, directness, humor, and taboo/unlikely formulations;
7. **acoustic and embodied performance constraints** — only where directly auditioned/observed, covering pace, pause, loudness, tension, posture, gesture, proximity, gaze, and stress-state changes;
8. **behavior under key situational classes** — ordinary domestic/social interaction, professional/public performance, competition, embarrassment, anger, grief, fear, moral disagreement, acute danger, caregiving, intimacy, institutional pressure, and recovery after crisis;
9. **failure modes and atypical states** — what pushes the character outside baseline, how overcontrol/avoidance/aggression/deference/withdrawal appears, and what tends to restore regulation;
10. **negative constraints** — actions, attitudes, phrasings, or social moves the evidence makes comparatively unlikely, to prevent generic or personality-inconsistent extrapolation;
11. **situational inference chain** — `stimulus -> interpretation -> emotional response -> competing priorities -> likely behavior -> likely speech strategy -> aftereffect/recovery`;
12. **confidence and evidence grade** for every reconstructive rule, distinguishing recurrent source behavior, strong extrapolation, plausible but underdetermined inference, and unsupported invention.

The document should use a tiered character-coverage model rather than forcing equal depth on every named person. Major characters with adequate longitudinal evidence receive full profiles; important supporting characters receive bounded profiles; minor characters remain explicitly underdetermined rather than being filled out from archetype assumptions.

Document 20 must preserve the distinction between **prediction** and **canon**. A plausible response in a hypothetical scene is an evidence-based inference, not a newly established source fact. When several behaviors remain plausible, the model should give a ranked range and identify which contextual variable would most likely decide among them.

Phase 5 does not close until Document 20 is stabilized alongside Documents 17–19.

**Governing reconstruction method (v1.5).** Document 20 is written under `00 V2 Frameworks/TBHX_V2_CHARACTER_RECONSTRUCTION_METHOD.md`, the project's adaptation of the opt-in corpus reference `governance/analytical-methods/GENERIC_CHARACTER_RECONSTRUCTION_METHOD.md`. The method governs how mature literary character understanding becomes conditional behavioral and speech constraints. It does not replace this section's twelve required profile elements; it supplies their operational form:

- elements 1–2 → stable disposition, appraisal and salience layers;
- element 3 → decision rules (`trigger + perceived stakes + current state → likely response family`, with inhibitors, overrides, exceptions, counterevidence and status);
- element 4 → developmental state and situational delta, without diagnosis;
- element 5 → directed relationship conditioning (A toward B is not B toward A);
- elements 6–7 → the speech-generation model and the lane-bounded embodied/vocal performance layer;
- element 8 → the situation-class tags and ordinary-life control sample;
- element 9 → developmental-state change classes and the counter-structure;
- element 10 → negative constraints, typed as evidence-backed limitation or evidence gap;
- element 11 → the conditional inference chain, expressed through the method's rule and speech layers;
- element 12 → rule status (`OBSERVED`, `CANDIDATE_POLICY`, `PROMOTED_POLICY`), extrapolation distance (`D0`–`D3`) and the project's qualitative confidence scale.

The method adds three obligations that the twelve elements did not state explicitly: every model is bound to a time-indexed state with a recorded knowledge boundary (`Subject@State`), so later revelations cannot become an earlier state's conscious reason; subject, role/office, presentation and other characters' beliefs remain separate; and validation is labeled prospective or retrospective, with simulated output never admitted as evidence. Where the method and the twelve elements appear to differ, the stricter evidence requirement governs. The “ranked range” in the prediction/canon paragraph above is an ordinal ordering with its deciding variable, never a numeric probability, and the model may instead record that the source does not distinguish the alternatives.

Document 20 describes coverage, maturity and evidence deficits per subject. It never assigns the global reconstruction evaluator's A–E tiers, dimension grades or scenario-readiness states, and no series task edits `characters/reconstruction_capabilities.jsonl`, `characters/CHARACTER_RECONSTRUCTION_INDEX.md` or a character-discovery partition. §10.3 states its dependencies and §10.5 its completion conditions.

#### Required naming/localization appendix — `TBHX_NAME_LOCALIZATION_CROSSWALK.md`

This document begins during Phase 1 as a live `active_provisional` artifact and is updated in place throughout sequential reading. Phase 5 performs a language/localization synthesis pass over the live crosswalk; Phase 7 performs the second evidence-routing audit and finalizes it for release. It is a canonical retrieval and disambiguation artifact, not an optional glossary.

Minimum columns/fields:

- Chinese characters / source-script name;
- standardized pinyin and canonical V2 analytical form;
- English-localized name(s);
- Japanese subtitle/reference rendering;
- hero name, legal/personal name, title, kinship/address form, or organizational label;
- first verified episode and source locator;
- equivalence/identity notes;
- localization type: literal, transliterated, compressed, adapted, substantially renamed, or misleading/non-equivalent;
- confidence and unresolved ambiguity;
- cross-references to the Chinese-language/naming ledger and relevant character/institution documents.

Canonical policy: the V2 synthesis should continue to use one stable Mandarin-primary analytical name for each entity. The crosswalk establishes equivalence across subtitle/localization tracks; it does **not** authorize free alternation among localized forms. Examples such as `娟姐 -> Juān jiě -> Miss J`, `岩莫 -> Yan Mo -> Rock`, and `岩叔 -> Yán-shū` (address to Yan Mo) should preserve relational or semantic information that localization may flatten or replace. Do not retroject a later English alias into an earlier prospective episode reading before the broadcast/source establishes the relevant identity.

During Phase 1, every newly encountered proper noun, title, hero identity, address form, or materially different English/Japanese rendering should be logged in `CHINESE_LANGUAGE_VOICE_AND_NAMING_LEDGER.md` **and propagated into the live crosswalk in place** with the best available provenance.

#### Phase 5A — targeted E05–E07 Yan Mo retrospective AV correction

Before Phase 6 begins, complete one bounded post-freeze evidence/revision work unit:

`TBHX_V2_E05-E07_YAN_MO_RETROSPECTIVE_AV_EVIDENCE_AUDIT.md`

Canonical home: `04 V2 Evidence and Revision/Targeted AV Evidence/`. This is an evidence audit, not a replacement episode deep reading. The prospective bodies of `TBHX_V2_E05_DEEP_READING.md`, `TBHX_V2_E06_DEEP_READING.md`, and `TBHX_V2_E07_DEEP_READING.md` remain frozen.

The audit must use the Mandarin-primary E05–E07 bundles, the supplied motion clips/stills, and Japanese/English subtitle tracks only as secondary semantic/navigation witnesses. It must test and route at least the following claims:

- the E05 distorted `大单子` kidnapping call and the E07 Yan Mo callback, including whether Yan Mo is securely identified as the original Pomelo/Yòuzi kidnapping client;
- Yan Mo's direct role in excluding zero-Trust Yang Cheng from the 34th-anniversary E-Soul selection;
- `岩叔 / Yán-shū / Uncle Rock` as the earlier familiar address/presentation of Yan Mo, preserving the distinction between address form and personal name;
- the E06 assassination chain: Yan Mo's intended target, the prototype E-Soul helmet, mistaken-target logic, and Shang Chao's death;
- the E07 order to `解决掉 / 始末しろ` the “impostor,” including coercion through the threatened younger brother;
- Yan Mo's personal disposal of Da Hu and Er Hu in concrete, with the act separated from the inferred cleanup/loose-end motive;
- the temporal pivot from attempted elimination of New E-Soul to active assistance in Yang's victory through paid `电光斩` expectation engineering;
- the post-duel Trust-value consolidation/merger and what it can and cannot establish about Yan Mo's prior knowledge;
- whether the evidence supports **planned awakening**, **engineered opportunity**, or the narrower model of **adaptive authorship / opportunistic conversion of contingency into leverage**;
- the official organizational characterization of Yan Mo as Mighty Glory's `代表` / head-representative, while avoiding an unsupported CEO title unless another primary/official source establishes it explicitly.

Required claim discipline:

- preserve `engineered agency / choice architecture` where supported;
- do **not** promote “Yan Mo planned the entire awakening/succession from the beginning” without direct evidence of that specific forecast;
- distinguish intended target from actual casualty;
- distinguish direct act from inferred motive;
- distinguish prospective episode uncertainty from retrospective full-series authority.

After the audit, propagate only mature revisions into the established canonical topical homes rather than creating duplicate syntheses. At minimum review/update:

- `CLAIM_REVISION_AND_CONFIDENCE_LEDGER.md`;
- `BROADCAST_ORDER_AND_DIEGETIC_CHRONOLOGY_LEDGER.md`;
- `PUBLIC_NARRATIVE_PRIVATE_EVENT_LEDGER.md`;
- `INSTITUTIONS_MEDIA_RANKINGS_AND_POLITICAL_ECONOMY_LEDGER.md`;
- `HERO_IMAGE_PERSONHOOD_AND_IDENTITY_LEDGER.md` where identity/role attribution changes;
- `07_YANG_CHENG_ESOUL_POMELO_AND_INHERITED_HEROISM.md`;
- `04_AGENCIES_COMMISSION_RANKINGS_MEDIA_RESEARCH_AND_POLITICAL_ECONOMY.md`;
- `TBHX_V2_TARGETED_AV_EVIDENCE_LEDGER.md`;
- `TBHX_NAME_LOCALIZATION_CROSSWALK.md` if source-title/address evidence changes;
- this architecture/corpus map if the audit materially changes current authority.

Phase 7 must then route the final mature Yan Mo/E-Soul claims through this audit and its source locators. The audit should not be treated as optional cleanup: it is a prerequisite for freezing the E05–E07 Yan Mo causal chain in the final claim-routing layer.

### Phase 6 — Comparative matrix and open-question control

Output:

`TBHX_COMPARATIVE_REFERENCE_MATRICES_AND_OPEN_QUESTIONS.md`

Canonical home: `04 V2 Evidence and Revision/`. **v1.5 identity correction:** earlier versions assigned this artifact the number 20, which collided with the mandatory Phase-5 Document 20 (`20_CHARACTER_BEHAVIOR_PERSONALITY_SPEECH_AND_SITUATIONAL_MODELING_REFERENCE.md`). Document 20 keeps its number. The comparative artifact is an unnumbered, series-specific reference and control apparatus, not a numbered specialist synthesis. No `20_COMPARATIVE_REFERENCE_MATRICES_AND_OPEN_QUESTIONS.md` exists, and none may be created; the former filename survives only as provenance in this paragraph and in Git history.

Phase 6 begins only after the Phase-5 closure checkpoint. Its inputs are the canonical specialists 01–20, Part I of `CLAIM_REVISION_AND_CONFIDENCE_LEDGER.md` (including its protected-uncertainty section) and the current map's protected full-series questions. It may compare and compress; it may not resolve a protected open question, promote a claim beyond its current confidence, or become a substitute for the specialists it indexes.

Purpose:

- compact character ethical profiles;
- competing concepts of heroism;
- types of public/private identity conflict;
- agency and institutional positions;
- Trust/Fear dependency types;
- unresolved mechanics;
- questions that must remain unanswered rather than smoothed over.

This document is intended for future cross-series use without replacing the deeper source documents.

### Phase 7 — Evidence routing and claim revision

Outputs:

- `21_PRIMARY_SOURCE_LOCATOR_AND_CLAIM_REVISION_LEDGER.md`
- `22_V1_TO_V2_REVISION_AND_CONFIDENCE_AUDIT.md`
- finalized `TBHX_NAME_LOCALIZATION_CROSSWALK.md`

Canonical home for Documents 21 and 22: `04 V2 Evidence and Revision/`. Their numbers are established and unchanged.

Document 21 routes every mature high-level judgment back through episode artifacts to source locators.
Where a mature claim was strengthened or changed by post-freeze clip review, Document 21 must also route through `TBHX_V2_TARGETED_AV_EVIDENCE_LEDGER.md` and the referenced raw media packet before assigning final source locators.

Before Phase 7 closes, perform the **second** crosswalk audit against all 24 episode naming entries, official multilingual materials, and Phase-5 language findings. Ensure that every materially different English localization or Japanese rendering can be resolved to the canonical Mandarin-primary entity without relying on chat memory.

Document 22 gives the intellectual history of the project: what V1 got right, what Chinese-source access strengthened, what became narrower, what was corrected, what was overturned, and what remains uncertain.

### Phase 8 — Full-series synthesis

Output:

`TBHX_FULL_SERIES_SYNTHESIS.md`

This should be a continuous literary argument, not a stitched summary of Documents 01–22. It should use the specialist corpus as evidence while building its own narrative progression.

The synthesis should answer, without presupposing the V1 wording:

- What kind of work is *To Be Hero X*?
- What is the relation between belief and power?
- What makes a hero morally legitimate when public belief is manipulable?
- How do hero images create, sustain, deform, or erase persons?
- Why does the work retell events from different perspectives?
- What do its institutions fear, and when is that fear rational or corrupting?
- What does the series finally claim about heroism that survives its critique of hero systems?

### Phase 9 — Reader map, archival cleanup, checksum lock

**v1.5 entrypoint rule.** `00 V2 Frameworks/TBHX_CURRENT_STATE_AND_CORPUS_MAP.md` remains the project's only current entrypoint through Phase 9 and after the archival freeze. Phase 9 does not create a second first-read surface. Earlier versions instructed a final `00_README_AND_CORPUS_MAP.md`; that instruction is withdrawn because the filename is one the corpus initiation policy recognizes as an entrypoint, and a separate status-bearing map would compete with the established one and go stale.

Phase 9 instead decides, and records in its checkpoint, one of two options:

1. **Single combined entrypoint (default).** Add a reader-facing orientation and reading-order section to the current map.
2. **Subordinate reader guide.** Write `05 V2 Full Series Synthesis/00_READER_GUIDE_AND_READING_ORDER.md` **last**, after terminology and mature conclusions have stabilized. It offers orientation, reading order and pointers to the canonical documents. It must declare itself subordinate to the current map, and it must not state current analytical authority, phase or completion status, counts, hashes, open debts or next permitted operations; for those it links to the map.

§10.2 states the full rule. Then emit:

- final manifest;
- word counts;
- source and artifact inventory;
- checksums;
- internal-link audit;
- duplicate-prose audit;
- delivery archive that excludes copyrighted source payloads unless the user explicitly wants a private source-inclusive backup;
- promote `TBHX_NAME_LOCALIZATION_CROSSWALK.md` from `active_provisional` to `canonical`, checksum it, and freeze it with the archival release.

---

## 4. Specialist synthesis numbering

The final reader-facing specialist corpus should use the following stable numbering:

| No. | Document |
|---:|---|
| 00 | Reader Guide and Reading Order — optional, Phase 9, subordinate to `TBHX_CURRENT_STATE_AND_CORPUS_MAP.md` (§10.2) |
| 01 | Narrative Architecture, Chronology, Perspective, Recontextualization |
| 02 | Trust, Fear, Power, and Social Ontology |
| 03 | Heroism, Power, Legitimacy, Dignity, and Coercion |
| 04 | Agencies, Commission, Rankings, Media, Research, Political Economy |
| 05 | Public Narrative, Branding, Celebrity, Myth, Collective Belief |
| 06 | Lin Ling / Nice / Moon / Replacement Hero |
| 07 | Yang Cheng / E-Soul / Pomelo / Inherited Heroism |
| 08 | Lucky Cyan / Hope / Survivorhood / Public Need |
| 09 | Queen / Order / Governance / Solitude / Reform |
| 10 | Luo Li / Cuteness / Technology / Grief / Self-Authorship |
| 11 | Ghostblade / Silence / Violence / Fatherhood / Refusal |
| 12 | Little Johnny & Big Johnny / Family / Monsterhood / Recognition |
| 13 | Dragon Boy / Smile / Pain / Fear / Punitive Heroism |
| 14 | Ahu / Local Heroism / Belief / Myth / Misrecognition |
| 15 | X / Zero / Godhood / Fate / Limit of Public Will |
| 16 | Cross-Arc Relationships, Alliances, Mentorship, Recognition |
| 17 | Mandarin Dialogue, Voice, Naming, Register, Japanese Reference Audit |
| 18 | Visual Form, Animation Modes, Color, Editing, Screens, Spectacle |
| 19 | Music, Sound, Silence, Performance, Public Voice |
| 20 | Character Behavior, Personality, Speech, and Situational Modeling Reference |
| 21 | Primary-Source Locator and Claim Revision Ledger |
| 22 | V1→V2 Revision and Confidence Audit |

`TBHX_FULL_SERIES_SYNTHESIS.md` sits above the numbered specialist set as the final continuous argument.

Unnumbered series-level artifacts keep their `TBHX_` identities: the current map, the methods, the comparative matrices and open-question control (`TBHX_COMPARATIVE_REFERENCE_MATRICES_AND_OPEN_QUESTIONS.md`), the naming crosswalk and the evidence ledgers. A number, once published or architecture-assigned, is never reassigned for cosmetic uniformity; an artifact without an established number takes an unnumbered identity rather than displacing one (§10.1).

---

## 5. Why this architecture fits *To Be Hero X*

### 5.1 It prevents chronology from flattening narrative form

The series' repeated perspectives and temporal displacement are not problems to be cleaned up. They are part of the meaning. Separate broadcast and chronology ledgers let us reconstruct causal order without pretending viewers received the story that way.

### 5.2 It treats public belief as a causal layer

A false story can still produce real power, fear, stigma, ranking movement, institutional response, or social obligation. The public/private event ledger preserves this instead of simply replacing “false” information with “true” information.

### 5.3 It gives the Mandarin original its own analytical home

The V2 language document is not a translation appendix. It can revise characterization, ethics, institutional tone, and relationship readings when Chinese wording or performance contains distinctions that Japanese or English rendering smooths out.

### 5.4 It keeps visual style from becoming decoration

If shifts in rendering, dimensionality, editing grammar, media-screen language, or performance staging correspond to changes in public/private identity, they need a dedicated longitudinal record before a formal thesis is made.

### 5.5 It makes V2 genuinely revisionary

A second pass is only useful if it can say “the first pass was wrong.” The dedicated V1→V2 ledger prevents the earlier synthesis from becoming invisible prior belief.

---

## 6. Canonical naming and metadata

### Episode files

`TBHX_V2_E01_DEEP_READING.md` … `TBHX_V2_E24_DEEP_READING.md`

### Specialist files

Use the two-digit numbering above and uppercase descriptive filenames for stable search.

### Naming/localization crosswalk

Use the exact stable filename `TBHX_NAME_LOCALIZATION_CROSSWALK.md`. Treat it as an evidence/index appendix under `04 V2 Evidence and Revision`, with authority equal to the language/naming ledger for cross-track identity reconciliation after final audit.

### YAML minimum

Every canonical artifact should include:

```yaml
---
project: "To Be Hero X V2"
artifact_type: "episode_deep_reading | ledger | specialist_synthesis | full_series_synthesis"
version: "1.0"
status: "working | frozen | final"
source_scope: "S01E01-S01E##"
spoiler_boundary: "..."
primary_language: "Mandarin Chinese"
source_profile: "Chinese audio + reconstructed zh-Hans hardsub OCR + visual archive"
prospective_freeze: true
retrospective_hindsight: "none | bounded | full-series"
confidence: "mixed"
---
```

This standard makes the corpus searchable and reduces ambiguity when artifacts are later moved into Library or another archival system.

**v1.5 authority metadata.** In Git, current-authority status is carried by the repository's recognized front-matter quartet (`status`, `supersedes`, `superseded_by`, `do_not_use_as_current_authority`) with reciprocal supersession links, as specified in `characters/RECONSTRUCTION_CAPABILITY_SPEC.md`. The `working | frozen | final` values above are descriptive project labels; they never stand in for the quartet. A provisional artifact is never promoted by editing its front matter.

---

## 7. Revision semantics

Never silently overwrite a mature conclusion when later evidence changes it.

Use the following dispositions:

- `CONFIRMED` — later evidence supports the original claim substantially as written;
- `STRENGTHENED` — same claim, now with better or broader evidence;
- `NARROWED` — direction remains useful but scope was too broad;
- `CORRECTED` — factual or causal detail changed materially;
- `OVERTURNED` — claim no longer survives the evidence;
- `UNRESOLVED` — competing readings remain live.

The final synthesis should reflect the revised state, while the ledgers preserve the path by which the project got there.

**v1.5 vocabulary crosswalk.** Current V2 ledgers record transitions in the corpus-wide vocabulary `PRESERVE / STRENGTHEN / REVISE / DOWNGRADE / REJECT / OPEN`. The labels above remain valid as legacy equivalents: `CONFIRMED` = `PRESERVE`; `STRENGTHENED` = `STRENGTHEN`; `NARROWED` and `CORRECTED` = `REVISE`; confidence reduction = `DOWNGRADE`; `OVERTURNED` = `REJECT`; `UNRESOLVED` = `OPEN`. New entries use the current vocabulary.

---

## 8. Recommended working cadence

A practical cadence is:

1. analyze one episode completely;
2. update ledgers immediately;
3. only then move to the next episode;
4. after a clearly completed character/arc movement, write a short checkpoint if needed, but do not finalize the specialist character document;
5. after Episode 24, stabilize chronology and repeated-event mappings before writing any definitive full-series claims.

This avoids the common failure mode where later episodes dominate memory and earlier episodes are reduced to foreshadowing.

---

## 9. Final corpus standard

The final V2 project should allow a future reader—or a future comparative analysis—to answer not only **what we concluded**, but:

- which episode first supported the claim;
- what the Mandarin line actually said;
- whether the claim depended on public narrative or privately established fact;
- how later episodes revised it;
- what visual/audio evidence supported it;
- what counterargument was considered;
- and how confident the final corpus is;
- and, for reconstruction-oriented character claims, whether the behavior/speech rule is directly recurrent, strongly extrapolated, merely plausible, or unsupported, with hypothetical predictions kept distinct from canon.

That is the standard that turns the V2 analysis from a sophisticated recap into an archival close reading and a bounded character-reconstruction reference.

---

## 10. v1.5 repair: artifact identity, authority states, dependencies, and completion gates

Version 1.5 (2026-10-25) is a targeted amendment, not a regenerated architecture. It repairs defects introduced when the mandatory character-modeling specialist was added after the original phase plan: two artifacts held Document 20, the Phase-9 plan called for a second first-read map beside the established current entrypoint, the Phase-5-to-9 dependency order was implicit, and the architecture did not distinguish possession of external audiovisual evidence from verified, accepted, synthesized, closed and published states. It also adapts a small number of responsibilities from the opt-in corpus reference `governance/analytical-methods/GENERIC_MULTI_DOCUMENT_SYNTHESIS_ARCHITECTURE_TEMPLATE.md` where they improve this mature architecture. Sections 1–9 remain governing except where this section or a marked v1.5 note says otherwise; their v1.4 wording is recoverable from Git history.

The governing rule of the repair is:

> **Every artifact has one clear identity, analytical responsibility, scope, authority state, and canonical home. The project has one current entrypoint.**

### 10.1 Artifact identity register

| Identity | Single responsibility | Phase | Canonical home | State at v1.5 |
|---|---|---|---|---|
| `TBHX_CURRENT_STATE_AND_CORPUS_MAP.md` | Sole current entrypoint: current authority, lifecycle and phase state, completion status, retrieval routes, next permitted operation | all | `00 V2 Frameworks/` | canonical; mutable |
| `TBHX_V2_ANALYTICAL_METHOD.md` | How source units are read and evidence classified | all | `00 V2 Frameworks/` | governing |
| this architecture | Where knowledge goes; identities, dependencies, gates | all | `00 V2 Frameworks/` | governing v1.5; `STABILIZED` |
| `TBHX_V2_CHARACTER_RECONSTRUCTION_METHOD.md` | How literary character understanding becomes conditional behavioral and speech models; governs Document 20 and any later subject models | 5 onward | `00 V2 Frameworks/` | canonical v1.0; method lifecycle `INITIAL` |
| Specialists 06–16 | Characters and relationships as literary subjects | 3 | `03 …/01 Characters and Relationships/` | canonical; closed |
| Specialists 01–05 | Systems, institutions and themes | 4 | `03 …/02 Systems Institutions and Themes/` | canonical; closed |
| Document 17 | Mandarin dialogue, discourse voice, naming, register; Japanese reference | 5 | `03 …/03 Language Audio and Visual Form/` | canonical |
| Document 18 | Visual form, animation modes, color, editing, screens, embodiment, spectacle | 5 | same | not begun; gate §10.5 |
| Document 19 | Music, sound, silence, vocal performance, public voice | 5 | same | not begun; gate §10.5 |
| Document 20 | Evidence-bounded character behavior, personality, speech and situational modeling | 5 | same | not begun; gate §10.5 |
| `TBHX_COMPARATIVE_REFERENCE_MATRICES_AND_OPEN_QUESTIONS.md` | Comparative matrices and protected-open-question control (unnumbered) | 6 | `04 V2 Evidence and Revision/` | not begun |
| Document 21 | Final claim-to-source locator and claim-revision routing | 7 | `04 V2 Evidence and Revision/` | not begun |
| Document 22 | V1→V2 intellectual history and confidence audit | 7 | `04 V2 Evidence and Revision/` | not begun |
| `TBHX_NAME_LOCALIZATION_CROSSWALK.md` | Cross-track identity resolution | 1–9 | `04 V2 Evidence and Revision/` | `active_provisional` until Phase 9 |
| `TBHX_V2_TARGETED_AV_EVIDENCE_LEDGER.md` | Post-freeze audiovisual intake and routing | 2–9 | `04 V2 Evidence and Revision/` | `active_provisional`; mutable |
| `TBHX_FULL_SERIES_SYNTHESIS.md` | Continuous full-series literary argument | 8 | `05 V2 Full Series Synthesis/` | not begun |
| `00_READER_GUIDE_AND_READING_ORDER.md` | Optional reader orientation; never status | 9 | `05 V2 Full Series Synthesis/` | optional; decided at Phase 9 |

The numbers 01–22 identify the reader-facing specialist and evidence documents named in §4. A published or architecture-assigned number is never reassigned. An artifact without an established number takes a series-prefixed unnumbered identity rather than displacing one, which is why the Phase-6 artifact is `TBHX_COMPARATIVE_REFERENCE_MATRICES_AND_OPEN_QUESTIONS.md` and Documents 17–22 keep their numbers.

### 10.2 One current entrypoint

`TBHX_CURRENT_STATE_AND_CORPUS_MAP.md` is the project's only current entrypoint, and the series registry names it. It alone states current analytical authority, phase and lifecycle state, completion status, publication state, retrieval routes and the next permitted operation. Methods, this architecture, specialists, ledgers, audits and checkpoints may report their own state, but none declares the project's current state; checkpoints under `99 V2 Archive and Delivery/` are receipts.

The requirement is one authoritative entrypoint, not one navigational document. A reader-facing guide may exist if Phase 9 finds it useful (Phase 9, above). It is subordinate: it states that it is not current authority for project status, carries no counts, hashes, open debts or next operations, and links to the current map for all of them. Its filename deliberately avoids `00_README_AND_CORPUS_MAP.md`, a name the initiation policy's precedence list recognizes as an entrypoint pattern. If no guide is written, the current map gains a reading-order section instead. Either way, there is never a second status-bearing map.

### 10.3 Dependency graph, Phase 3 through Phase 9

```text
Phase 3  Specialists 06–16 (characters, relationships)          closed
Phase 4  Specialists 01–05 (systems, institutions, themes)      closed
   │
Phase 5  Document 17 (language, discourse voice, naming)        canonical
   ├──► Document 18 (visual form, embodiment, editing)  ┐  may proceed in parallel;
   └──► Document 19 (music, sound, silence, performance) ┘  each consumes 17
            │
            ▼
         Document 20 (character modeling) ◄── reconstruction method; Phase-3/4 corpus
            │
         Phase-5 closure checkpoint (evidence limits and unresolved debts named)
   │
Phase 6  TBHX_COMPARATIVE_REFERENCE_MATRICES_AND_OPEN_QUESTIONS.md
Phase 7  Documents 21 and 22; second crosswalk audit; final claim revision
Phase 8  TBHX_FULL_SERIES_SYNTHESIS.md
Phase 9  reader orientation decision; archival audits; checksum lock; crosswalk freeze
```

1. **Phase-3 character and relationship specialists** explain characters as literary subjects. They are the literary authority for Document 20 and are not regenerated or absorbed by it.
2. **Phase-4 system and thematic syntheses** supply the world-model in which character conduct is interpreted.
3. **Document 17** supplies lexical and discourse voice: identity grammar, address, modality, register and speech operations.
4. **Document 18** supplies visual form, motion, gesture, posture, framing and embodiment evidence within its motion-evidence gate.
5. **Document 19** supplies acoustic modulation, pause, vocal performance, music and silence within its audition gate.
6. **Document 20** translates mature, source-grounded character understanding into structured behavioral and speech constraints for conditional extrapolation, under the reconstruction method. Where Document 20's modeling and a Phase-3 monograph disagree, the disagreement is resolved in the literary corpus through claim revision, and the model follows.
7. **Phase-5 closure** records which source limitations remain and which claim classes they bound.
8. **Phase 6** compares and controls protected open questions without resolving them.
9. **Phase 7** routes final claims to sources and finalizes claim revision and the crosswalk.
10. **Phase 8** writes the continuous literary argument from the specialist corpus.
11. **Phase 9** completes reader orientation and archival freeze.

Evidence intake through `TBHX_V2_TARGETED_AV_EVIDENCE_LEDGER.md` runs throughout. Evidence accepted after a document becomes canonical revises it through a labeled current revision and a receipt, never by silent rewrite. Reconstruction is a derived-use layer placed inside Phase 5 as Document 20; subject-level operational models and their validation records may continue after Phase 8 and do not block it.

### 10.4 Evidence and authority states

The following states are distinct. None implies the next, and each is recorded where its owning artifact records state.

| State | Meaning | What it does not establish |
|---|---|---|
| `ACQUIRED` | An evidence object is in hand or located: an external handoff bundle, a clip, a native source file. Integrity may be checked. | That anything inside it was perceived correctly, or that its claims are accepted |
| `PRODUCER_REPORTED` | An observation reported by the producing lane, recorded with attribution. The reconciliation protocol's `REPORTED` and `ANCHORED` statuses are qualifiers within this state. | Independent verification, acceptance, or certification of continuous or acoustic coverage |
| `INDEPENDENTLY_VERIFIED` | The receiving analyst or an independent route inspected the specific channel at the cited locator: native frames or displayed hardsubs for static and text claims, continuous inspection for motion, original-speed audition for sound. Verification is per channel. | Verification of any other channel, or acceptance into current authority |
| `ACCEPTED_CLAIM` | Adjudicated into current authority (a `P2-CR-*` key, a topical ledger or a targeted AV entry) with a transition. | That a specialist has synthesized it |
| `SYNTHESIS_COMPLETE` | A specialist document is semantically accepted and canonical. | Phase closure |
| `CLOSURE_AUTHORIZED` | A phase-closure checkpoint names the closed scope and remaining limits. | Publication |
| `INTEGRATED` | The change is on `main` with a successful exact-head repository audit. | Literary or audiovisual truth |

Rules:

- Possession of a Gemini handoff bundle, or of any external bundle, is `ACQUIRED`. Its observation logs are `PRODUCER_REPORTED` until adjudicated.
- A load-bearing accepted claim rests on evidence `INDEPENDENTLY_VERIFIED` on the channel it asserts, or on a producer observation that is `ANCHORED` and accepted under Section 5 of the audiovisual reconciliation protocol without an unresolved contradiction or verification request.
- A claim resting only on producer reports may be retained as `REPORTED`: retrievable, weighed with its stated confidence, never load-bearing.
- Internal contradiction inside a producer report keeps the disputed item `OPEN` until source evidence settles it; agreement among models is not verification.
- Analytical acceptance and Git publication are separate. A canonical file on an unmerged branch is not current integrated authority.

### 10.5 Completion conditions and load-bearing source debts

The project does not require a fresh uninterrupted audition of all twenty-four episodes. It requires that each specialist's load-bearing claims rest on evidence adequate to their channel, and that the specialist's responsibility statement does not claim coverage it lacks.

| Unit | Completion condition | Debts that block only the claims they name |
|---|---|---|
| Document 17 | Satisfied. Further quotation-grade promotion follows analytical method §5.4 at native hardsubs. | Each audit's lexical debts, for example `E08A-D1` (dates, orthography, counters, long quotations) |
| Document 18 | Every load-bearing static claim (composition, costume, color, displayed text, screen content) cites a native or verified bundle frame. Every load-bearing motion, gesture-trajectory, editing, transition or duration claim cites an accepted motion audit (the E19–E24 video audits, the E21 retrospective motion audit, the E24 credits-coda audit, the E05–E07 formal audit within its limits) or a newly satisfied targeted inspection at adequate density. Producer-reported motion remains retrievable and unweighted. | `AV-D01`, `AV-D02`, `AV-D05`; `E08A-D3` (Dean rescue, marble chain); `E24-D02` (complete roster), `E24-D04` (subsecond order); the remaining-arcs checkpoint's qualified-AV-reviewer row |
| Document 19 | Every acoustic claim (delivery, timbre, prosody, breath, laughter quality, silence as design, cue-to-image synchronization, song or performer identity) rests on an original-speed audition record by a lane with verified listening capability and calibrated clock, or is restated as acoustic measurement or text-layer fact. Song identity also needs a credit or official witness; ASR is not audition. Questions not auditioned are declared `OPEN`, and the document claims no complete acoustic coverage. | `AV-D03`, `AV-D04`, `AV-D06`; `E08A-D4` (E09 whisper 19:34–19:36, outro 22:09–22:47.5); `E24-D04`; the remaining-arcs checkpoint's listening-reviewer row |
| Document 20 | The reconstruction method's Document-20 conditions (reconstruction method §13) are met: every included subject has a declared coverage tier and state binding; rules carry evidence routes, knowledge boundaries, status, distance, confidence and counterevidence; embodied and acoustic constraints are limited to Document 18/19 accepted evidence; evidence gaps are recorded; no capability grade appears. Document 20 may begin once 18 and 19 are canonical, even if they leave bounded `OPEN` questions, which its acoustic and embodied layers then inherit. | Inherits 18/19 limits; any rule depending on a named open debt is labeled with it |
| Phase-5 closure | Documents 17–20 canonical; the closure checkpoint lists each unresolved debt with the claim classes it bounds; role-gap audit (§10.11) rerun; integration verified. | — |
| Phases 6–9 | As in §3 and §10.3. | — |

**Not closure blockers.** Protected full-series questions (current map §15; claim register §9) — exact Trust/Fear equations, Zero's literal persistence, X's ontology, the coin's mechanism, conventional time travel, the literal status of credits-coda images — are preserved as `OPEN`; they never block closure and are never answered to satisfy a checklist. Optional debts such as `E08A-D5` (full arc rewatch) and `E24-D05` (literal persistence) stay optional unless a later artifact claims the coverage they would supply.

### 10.6 Responsibility matrix

| Dimension | Sequential capture | Cumulative home | Final destination |
|---|---|---|---|
| Character state, personhood | always | relationship and hero-image ledgers | Specialists 06–16; Document 20 (derived models) |
| Directed relationships | always | `CHARACTER_RELATIONSHIP_AND_RECOGNITION_LEDGER.md` | Specialist 16; Document 20 relationship conditioning |
| Trust/Fear mechanics | when present | mechanics ledger | Specialist 02 |
| X world-state mechanics | when present | `TBHX_X_REPRESENTATIONAL_SOVEREIGNTY_LEDGER.md` | Specialists 15/02 |
| Chronology, broadcast order | always | chronology ledger | Specialist 01 |
| Public narrative | always | public-narrative ledger | Specialist 05 |
| Institutions, rankings | when present | institutions ledger | Specialist 04 |
| Lexical voice, naming, register | always | Chinese-language ledger; crosswalk | Document 17 |
| Visual form, motion, objects | if diagnostic | form ledger; motion audits; targeted AV ledger | Document 18 |
| Sound, music, vocal performance | if diagnostic | form ledger (bounded); targeted AV ledger and audits | Document 19 |
| Behavior/speech model evidence | at Document 20 | reconstruction evidence ledgers (reconstruction method §11), initialized with Document 20 | Document 20; subject models |
| Claims and revisions | always | claim register | Document 21 |
| V1 history | at import | V1→V2 ledger | Document 22 |
| Comparison, protected unknowns | at synthesis | claim register §9; current map §15 | Phase-6 artifact |

No dedicated cumulative acoustic-performance ledger is initialized. Accepted listening evidence currently lives in the targeted AV ledger and the evidence audits. Document 19 decides at its start whether accepted audition records need an independent cumulative home (§10.11).

### 10.7 Source and edition topology

| Source class | Object | Role | Clock and conflict rule |
|---|---|---|---|
| Primary audiovisual | Bilibili 2160p Mandarin WEB-DL with burned-in Simplified-Chinese hardsubs | Primary picture, sound and displayed wording | Cite WEB source-absolute time; preroll varies by episode |
| Displayed hardsub | Native frames of the same files | Lexical witness of record | Outranks reconstructed OCR text |
| Reconstructed OCR ASS | Legacy production subtitles | Navigation and indexing | Yields to native frames and audio; content-quality warnings apply |
| Mandarin ASR | Diagnostic transcripts | Diagnostic only | Never overrides displayed text |
| Japanese reference | Aligned Japanese subtitles | Secondary semantic witness | Never Mandarin register authority |
| DB Blu-ray release and English tracks | Separate release, English BD/SDH subtitles | Secondary witnesses | Separate clock; no universal BD↔WEB offset across insertions |
| External handoff bundles | Gemini continuous-AV bundles and QA supplements | `PRODUCER_REPORTED` evidence | Adjudicated per §10.4 and the reconciliation protocol |
| Paratext | Opening, ending, credits coda, official naming and song announcements | Supplemental | Classified before any chronology or behavior use |

### 10.8 Lanes, ownership and reasoning classes

Stages name roles and inspection lanes, not providers; the owner's current provider assignment is a dated fact in the lane-routing policy, not architecture.

| Stage | Owner role | Lanes | Reasoning class |
|---|---|---|---|
| Documents 17 and 20; Phase 6 | analysis author | `TEXT`, `STILL_IMAGE`, `BUNDLE_MEDIATED` | `DEEP_SYNTHESIS`; Document 20 `PREMIUM_QUALITY_FIRST` |
| Document 18 | analysis author integrating accepted motion evidence | static claims in still or bundle lanes; motion through `CONTINUOUS_AV` review under the reconciliation protocol | `DEEP_SYNTHESIS` |
| Document 19 | analysis author integrating audition records | acoustic claims require a verified `CONTINUOUS_AV` or `audio_content_inspection` route | `DEEP_SYNTHESIS` |
| Targeted AV intake and evidence audits | any analyst, within lane permissions | per claim channel | `BOUNDED_STANDARD`; consequential identity or causal adjudication `SUBSTANTIVE_ANALYSIS` |
| Phases 7–8 | analysis author | `TEXT`, `STILL_IMAGE` | `PREMIUM_QUALITY_FIRST` |
| Architecture amendments | analysis author | `TEXT` | `PREMIUM_QUALITY_FIRST` |
| Repository integration | integration owner | not applicable | checklist |

### 10.9 Mutable and frozen artifacts

- **Frozen:** E01–E24 prospective episode bodies; phase, closure and integration checkpoints and their checksum files.
- **Mutable current authority:** the current map; Phase-2 ledgers through evidence-backed updates; the claim register; the targeted AV ledger; the X sovereignty ledger; the crosswalk until Phase 9.
- **Canonical specialists:** revised only by a bounded, labeled current revision, a revision identifier in front matter and a receipt checkpoint recording bytes, whitespace words and SHA-256; the current map's entry is refreshed in the same change.
- **Supersession:** reciprocal `supersedes`/`superseded_by` links in the recognized front-matter quartet (§6 note). Superseded analysis remains as provenance.

### 10.10 Contradiction routing

| Contradiction | Route |
|---|---|
| Public narrative versus private event | Preserve both layers (method §2.3, §9.2) |
| Retrospective revelation versus prospective boundary | Claim revision or erratum; the frozen reading stays as written |
| A producer report contradicting itself | Keep `OPEN` until source evidence settles it; never choose by model agreement |
| Disagreement between inspection lanes | Reconciliation protocol §5; a lane contests only on a channel it can inspect |
| Localization divergence | Crosswalk; Mandarin governs |
| X's history-space testimony versus public history | Authored testimony, not a self-authenticating archive |
| Paratext versus diegesis | Paratext classification governs chronology use |
| Genuine source inconsistency | Record it; do not harmonize |

A contradiction warrants an evidence audit when a load-bearing claim depends on it, a claim revision when evidence settles it, and an `OPEN` state when it does not.

### 10.11 Role-gap audit at v1.5

| Responsibility | State | Carried by / repair route |
|---|---|---|
| Sequential readings E01–E24 | `SATISFIED` | frozen readings |
| Longitudinal ledgers and claim register | `SATISFIED` | Phase-2 ledgers; claim register |
| Phases 3–4 | `SATISFIED` | specialists 01–16 |
| Document 17 | `SATISFIED` | Document 17 |
| Documents 18, 19, 20 | `MISSING` | gates in §10.5 |
| Character reconstruction method | `SATISFIED` | `TBHX_V2_CHARACTER_RECONSTRUCTION_METHOD.md` |
| Reconstruction evidence ledgers | `MISSING`, not day-one | initialized with Document 20 work |
| Cumulative acoustic-performance home | `PARTIALLY_SATISFIED` | targeted AV ledger and audits; Document 19 decides |
| Phase-6 comparative artifact | `MISSING`, identity resolved | Phase 6 |
| Documents 21–22 | `MISSING` | Phase 7 |
| Planned `PRIMARY_SOURCE_LOCATOR_LEDGER.md` and `CLAIM_TO_SOURCE_ROUTING_INDEX.md` | `MISROUTED` as separate files | carried by Document 21; not to be created separately |
| Planned `SUBTITLE_AND_TRANSLATION_AUDIT.md` | `NOT_APPLICABLE` as a separate file | Document 17 and the subtitle and evidence audits |
| Planned `PROVENANCE_AND_CORRECTION_LOG.md` | `NOT_APPLICABLE` as a separate file | claim register §12, targeted AV ledger, integration checkpoints |
| Naming crosswalk | `PARTIALLY_SATISFIED` | Phase-7 audit; Phase-9 freeze |
| Current entrypoint | `SATISFIED` | current map |
| Reader orientation | `NOT_APPLICABLE` until Phase 9 | §10.2 |
| Archival manifest, checksums, release audit | `MISSING`, scheduled | Phase 9 |

The audit is repeated before Phase-5 closure, before Phase 8 and before the Phase-9 freeze.

### 10.12 Retrieval routes added at v1.5

The current map's retrieval route remains authoritative. Version 1.5 adds:

1. architecture identity, dependency or gate questions → this §10;
2. how a character model is built, bounded or validated → `TBHX_V2_CHARACTER_RECONSTRUCTION_METHOD.md`; after Phase 5, Document 20; for literary authority, the relevant Phase-3 specialist;
3. comparative questions and protected unknowns → claim register §9 and current map §15 until the Phase-6 artifact exists;
4. whether external audiovisual evidence is accepted → the targeted AV ledger and the relevant evidence audit, read through §10.4.

### 10.13 Revision history

- **v1.5 — 2026-10-25.** Document 20 confirmed as character modeling; the Phase-6 artifact renamed to unnumbered `TBHX_COMPARATIVE_REFERENCE_MATRICES_AND_OPEN_QUESTIONS.md`; homes declared for Documents 21–22; the numbering table corrected; the Phase-9 second map replaced by the single-entrypoint rule and an optional subordinate reader guide; the reconstruction method adopted for Document 20; dependency graph, evidence and authority states, completion gates, responsibility matrix, source topology, lane ownership, mutable/frozen rules, contradiction routing and role-gap audit added; legacy revision labels crosswalked.
- **v1.0–v1.4 — 2026-08-13 to 2026-08-18.** Original phase plan and its Drive-era amendments. By v1.4, which entered Git unchanged in the 2026-09-01 migration, the mandatory Document 20 had been added to Phase 5 without retiring the Phase-6 use of the number 20 — the defect v1.5 repairs. Earlier text is recoverable from Git and Drive provenance.
