---
title: "To Be Hero X V2 — Multi-Document Synthesis Architecture"
project: "To Be Hero X V2"
artifact_type: "synthesis_architecture"
version: "1.4"
created: "2026-08-13"
last_updated: "2026-08-18"
status: "governing"
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
│   ├── TBHX_V2_CORPUS_AUDIT_AND_SOURCE_PROFILE.md
│   ├── TBHX_V2_ANALYTICAL_METHOD.md
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
│   ├── Targeted AV Evidence/
│   │   └── TBHX_E##_SHORT_DESCRIPTIVE_SCOPE/
│   └── PROVENANCE_AND_CORRECTION_LOG.md
├── 05 V2 Full Series Synthesis/
│   ├── 00_README_AND_CORPUS_MAP.md
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

`20_COMPARATIVE_REFERENCE_MATRICES_AND_OPEN_QUESTIONS.md`

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

Write `00_README_AND_CORPUS_MAP.md` **last**, after terminology and mature conclusions have stabilized.

Then emit:

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
| 00 | README and Corpus Map |
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
| 20 | Comparative Reference Matrices and Open Questions |
| 21 | Primary-Source Locator and Claim Revision Ledger |
| 22 | V1→V2 Revision and Confidence Audit |

`TBHX_FULL_SERIES_SYNTHESIS.md` sits above the numbered specialist set as the final continuous argument.

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
