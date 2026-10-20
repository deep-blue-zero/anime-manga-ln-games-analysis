---
series: GKM
artifact_type: audiovisual_baseline_requests
analytical_role: distributed_character_targeted_av_acquisition_plan
scope: KAYA_RINHA
generation: V2
status: draft_noncurrent
source_boundary: "GAKUMAS V2 Source Lock 1.0 plus corrected GKM_KAYA_RINHA_SOURCE_CROSSWALK.md (118 unique objects / 43 direct-speaking objects / 620 logical Rinha messages) and GKM_KAYA_RINHA_EVIDENCE_MATRIX.md (73 adjudicated claims); no new Rinha AV inspected by this artifact"
source_lock: "GAKUMAS V2 Source Lock 1.0"
source_commit: "00d150a069a3ffa723a1ff264752ba242024caad"
source_revision: 32
governing_method: "GAKUEN_IDOLMASTER_FULL_CORPUS_ANALYTICAL_METHOD_V2.md v2.2"
governing_architecture: "GAKUEN_IDOLMASTER_MULTI_DOCUMENT_SYNTHESIS_ARCHITECTURE_V2.md v2.4"
governing_crosswalk: "GKM_KAYA_RINHA_SOURCE_CROSSWALK.md — Drive 16LQV0l604NU3E6-c5qusD7sy66xzu99a"
governing_evidence_matrix: "GKM_KAYA_RINHA_EVIDENCE_MATRIX.md — Drive 1kDlqf_puATpby_74TNTI_QM7uBQyT54n"
created: "2026-08-24"
review_state: "OWNER_APPROVED_EXECUTION; PERCEPTUAL_GATE_OPEN"
acquisition_gate: "REQUIRED_BEFORE_DOSSIER_FINALIZATION"
supersedes: []
superseded_by: []
do_not_use_as_current_authority: true
---

# GKM KAYA RINHA AUDIOVISUAL BASELINE AND REQUESTS

> **Execution adoption — 2026-09-11.** The owner authorized this plan. All 12 retained packets and 18 target scenes are present; the source/text, selected-mix measurement and sampled-still pass is delivered in [the integrated baseline](GKM_KAYA_RINHA_COMPLETE_AUDIOVISUAL_BASELINE.md). Direct listening and continuous-motion review remain unperformed, so the dossier gate stays open. The plan’s historical draft/acquisition prose and unchecked collector checklist are preserved below rather than treated as current missing-source claims. The current home is `05_AUDIOVISUAL_ANALYSIS/KAYA_RINHA/`. Exact speaker recount changes 621→620 and support0097 part02 10→9; the original supplied file remains unchanged. Current observations belong to the baseline, not this acquisition plan.

## 0. Purpose and review state

This is a **draft acquisition-facing document** for the targeted audiovisual reconstruction of **Kaya Rinha / 賀陽燐羽**.

It is intentionally `active_provisional` and `do_not_use_as_current_authority: true` until the acquisition plan is reviewed. It does **not** replace the canonical textual authorities:

1. `GKM_KAYA_RINHA_SOURCE_CROSSWALK.md` — where Rinha evidence exists and how it is routed;
2. `GKM_KAYA_RINHA_EVIDENCE_MATRIX.md` — what the current text evidence can prove and which claims require AV discrimination.

The evidence matrix has already resolved the AV gate:

> **A dedicated targeted Kaya Rinha audiovisual baseline is REQUIRED before `GKM_KAYA_RINHA_CHARACTER_DOSSIER.md` is finalized.**

The purpose of this document is therefore operational:

- define the **smallest discriminating scene set**;
- minimize redundant reacquisition of footage already retained from the 13 playable-character AV baselines;
- give stable internal names and exact Source-Lock locators;
- give human-facing Japanese search nomenclature for collection;
- define acceptable media quality and rejection conditions;
- define the manifest/checksum package to preserve provenance;
- state what each scene is expected to adjudicate;
- establish the inspection/closure gate before the Rinha dossier.

This is **not** an attempt to collect every scene in which Rinha appears. The governing rule is:

> **Acquire for discrimination, not audiovisual completeness for its own sake.**

---

# 1. Current textual baseline

The corrected Rinha corpus contains:

- **118** deduplicated canonical source objects;
- **43** objects with Rinha's own dialogue;
- **620** logical Rinha dialogue messages;
- direct material distributed principally across Temari, Misuzu, Saki, Ume, numbered events, support stories, and idol communications;
- no dedicated playable-character route and no dedicated Rinha musical corpus currently established.

The matrix shows that text alone already establishes many lexical facts, including stable first-person `私` and recurrent directive/adversarial forms. AV is needed primarily because **very similar words perform different relational functions**.

The baseline must discriminate at least these delivery states:

1. playful provocation;
2. technical/professional severity;
3. genuine anger or contempt;
4. defensive denial;
5. embarrassment / affect leakage;
6. grief, shame, or self-blame;
7. old-peer intimacy and sparring;
8. direct vulnerability;
9. fan-facing responsibility;
10. coaching that sounds harsh lexically but is behaviorally supportive;
11. present-tense future orientation after SyngUp.

---

# 2. Reuse-first acquisition policy

## 2.1 Do not automatically reacquire host-character Dear footage

The GKM corpus already completed integrated AV baselines for all **13/13 playable characters**, including Temari, Misuzu, Saki, and Ume. The Rinha targets embedded inside those routes may therefore already exist inside retained whole-video packets or source manifests.

Before external reacquisition, perform a Drive reuse audit against:

- `GKM_AUDIOVISUAL_SOURCE_CROSSWALK.md`;
- the Temari AV source manifest / retained Dear packets;
- the Misuzu AV source manifest / retained Dear packets;
- the Saki AV source manifest / retained Dear packets;
- the Ume AV source manifest / retained Dear packets.

If an existing retained object contains the exact target scene with intact Japanese audio and staging, **reuse it by reference**. Do not create a second media copy merely to give Rinha her own baseline.

## 2.2 Acquisition order

Use this order:

1. **Reuse existing playable-character AV** where exact scenes are already retained.
2. Acquire the **three-part Support `story_0097`** object if it is not already present as playable video.
3. Acquire **EVENT_016 `main-03`** or the narrowest whole event-story video containing it.
4. Fill any missing **P0 Dear** packets.
5. Fill **P1 breadth controls** only after P0 coverage is secure.
6. Do not expand to the rest of the 43 direct-speaking objects unless P0/P1 inspection exposes a specific unresolved contrast.

## 2.3 One acquisition may satisfy multiple scene targets

Whole route packets are preferred when they preserve the exact source boundaries and are easier to obtain. For example:

- one Temari Dear `11–20` video can cover Dear 015, 016, and 020;
- one Misuzu Dear `21–27` video can cover Dear 023 and 024;
- one Ume Dear `11–20` video can cover Dear 015 and 016;
- one complete `story_0097` support-commu video can cover all three P0 support parts.

Do **not** split or duplicate a whole packet merely to create one file per target scene. Scene-level analytical locators can point into the shared retained object.

---

# 3. Acquisition gate summary

## 3.1 P0 — minimum discriminating set

**11 scene targets.** These are blocking for the dossier unless an exact scene is genuinely unavailable after reasonable retrieval attempts.

| AV ID | target | crosswalk | exact A1 source | Rinha messages | principal matrix claims | discriminating question |
| --- | --- | --- | --- | ---: | --- | --- |
| `RINHA-AV-P0-001` | Temari Dear 015 | `RINHA-XW-037` | `transcripts_raw/05_dear_idol/ttmr=Temari_Tsukimura/dear_015.txt` | 18 | C034–C035, C067–C070 | Is Rinha's denial of martyr/protector framing flat, angry, ashamed, defensive, or affect-leaking? How is the public-blame discussion performed? |
| `RINHA-AV-P0-002` | Temari Dear 016 | `RINHA-XW-038` | `.../ttmr=Temari_Tsukimura/dear_016.txt` | 37 | C009, C012–C014, C057, C070 | How does retirement/fan handoff language sound around Temari's tears? Where does Rinha's composure visibly/vocally break or recover? |
| `RINHA-AV-P0-003` | Temari Dear 020 | `RINHA-XW-041` | `.../ttmr=Temari_Tsukimura/dear_020.txt` | 7 | C030, C073 | Rare Rinha interiority: what is the transition from private thought into outward coaching, and how different is internal voice from adversarial social register? |
| `RINHA-AV-P0-004` | Misuzu Dear 016 | `RINHA-XW-061` | `transcripts_raw/05_dear_idol/hmsz=Misuzu_Hataya/dear_016.txt` | 27 | C009, C012, C033, C058 | How does “I am not an idol” coexist with the dream wound and old-peer intimacy/conflict? Is the sharpness guarded, wounded, matter-of-fact, or provocative? |
| `RINHA-AV-P0-005` | Misuzu Dear 024 | `RINHA-XW-069` | `.../hmsz=Misuzu_Hataya/dear_024.txt` | 27 | C011, C018, C054, C066–C073 | Critical anchor for idol ontology, fandom vs self-disqualification, professional severity, and ordinary banter. Which abrasive forms are playful vs genuinely evaluative? |
| `RINHA-AV-P0-006` | Saki Dear 026 | `RINHA-XW-083` | `transcripts_raw/05_dear_idol/hski=Saki_Hanami/dear_026.txt` | 26 | C005–C008, C033, C059, C070 | Longest autobiographical disclosure: grief/shame/self-blame vs analytical narration. Where does vulnerability become direct rather than recoded? |
| `RINHA-AV-P0-007` | Ume Dear 024 | `RINHA-XW-097` | `transcripts_raw/05_dear_idol/hume=Ume_Hanami/dear_024.txt` | 27 | C020, C046–C047, C060 | Fan stewardship, concern about Saki burnout, hesitation, and acceptance of Ume's answer. How does Rinha yield a boundary without losing directive style? |
| `RINHA-AV-P0-008` | Support story 0097 part 01 | `RINHA-XW-113` | `transcripts_raw/04_support_card_stories/support_series_3/story_0097/part_01.txt` | 10 | C015, C021, C070, C073 | Present Rinha interiority, privacy control, public recognition, and explicit future-return promise. Establish late-state baseline. |
| `RINHA-AV-P0-009` | Support story 0097 part 02 | `RINHA-XW-114` | `.../story_0097/part_02.txt` | 9 | C037–C041, C055 | Mature Temari–Misuzu–Rinha triad banter and dissolution-live coordination. Test post-unit familiarity without unit restoration. |
| `RINHA-AV-P0-010` | Support story 0097 part 03 | `RINHA-XW-115` | `.../story_0097/part_03.txt` | 9 | C019, C060, C070 | Playful teasing shifts into a direct request for emotional help. Measure how vulnerability enters and exits the abrasive register. |
| `RINHA-AV-P0-011` | EVENT_016 main-03 | `RINHA-XW-106` | `transcripts_raw/06_story_events/event_016/main-03.txt` | 5 | C042–C043, C066–C068 | Childhood pedagogical harshness: timing between insult/provocation, concrete technique, persistence, and encouragement. Essential negative control against “harsh = hostile.” |

### P0 gate

The baseline should not be considered complete unless all **11** are either:

- `INSPECTED`, or
- explicitly documented as `UNAVAILABLE_AFTER_RETRIEVAL_AUDIT`, with a reason and substitution decision.

An unavailable P0 scene cannot be silently treated as if text settled its AV-sensitive claim.

---

# 4. P1 — breadth controls

**7 scene targets.** These are strongly preferred because they prevent the P0 set from overfitting Rinha to SyngUp trauma and high-stakes conflict.

| AV ID | target | crosswalk | exact A1 source | Rinha messages | control function |
| --- | --- | --- | --- | ---: | --- |
| `RINHA-AV-P1-001` | Saki Dear 016 | `RINHA-XW-079` | `transcripts_raw/05_dear_idol/hski=Saki_Hanami/dear_016.txt` | 14 | Defeat, envy, “no plating,” kiss/sister-play; tests intimacy/provocation after competition. |
| `RINHA-AV-P1-002` | Saki Dear 034 | `RINHA-XW-088` | `.../hski=Saki_Hanami/dear_034.txt` | 16 | Friendship/loneliness/date/“floating” teasing; useful ordinary-social register control. |
| `RINHA-AV-P1-003` | Ume Dear 016 | `RINHA-XW-093` | `transcripts_raw/05_dear_idol/hume=Ume_Hanami/dear_016.txt` | 16 | Direct liking, fan handoff, kiss/playful intimacy; tests positive affect inside abrasive vocabulary. |
| `RINHA-AV-P1-004` | Ume Dear 029 | `RINHA-XW-100` | `.../hume=Ume_Hanami/dear_029.txt` | 22 | Saki concern, accepted intervention boundary, mentor feedback; tests mature care without takeover. |
| `RINHA-AV-P1-005` | Temari Dear 024 | `RINHA-XW-043` | `transcripts_raw/05_dear_idol/ttmr=Temari_Tsukimura/dear_024.txt` | 32 | Embarrassment, “cut ties” rhetoric, renewed training; tests defensive social language in the repaired relation. |
| `RINHA-AV-P1-006` | Misuzu Dear 023 | `RINHA-XW-068` | `transcripts_raw/05_dear_idol/hmsz=Misuzu_Hataya/dear_023.txt` | 16 | Abrasive praise and concealed-frustration read; tests old-peer interpretive shortcuts. |
| `RINHA-AV-P1-007` | Ume Dear 015 | `RINHA-XW-092` | `transcripts_raw/05_dear_idol/hume=Ume_Hanami/dear_015.txt` | 17 | Imitation-based vocal pedagogy; especially valuable acoustically because the scene centers voice imitation. |

P1 scenes should be acquired when available in the same whole packets as P0 scenes even if a separate acquisition would not otherwise be justified.

---

# 5. Efficient whole-video packet plan

If public uploads or retained Drive sources are organized as multi-episode Dear compilations, the following **12 physical packets** can cover all 18 analytical scene targets. Many may already exist from the completed host-character baselines.

| packet ID | preferred whole artifact | targets covered | priority | primary Japanese search |
| --- | --- | --- | --- | --- |
| `RINHA-PKT-TEMARI-11-20` | 月村手毬 親愛度コミュ 11～20 | P0 Temari 015, 016, 020; also useful Dear 014 hostility/professional control if included | P0 | `学マス 月村手毬 親愛度コミュ11～20` |
| `RINHA-PKT-TEMARI-21-27` | 月村手毬 親愛度コミュ 21～27 | P1 Temari 024 | P1 | `学マス 月村手毬 親愛度コミュ21～27` |
| `RINHA-PKT-MISUZU-11-20` | 秦谷美鈴 親愛度コミュ 11～20 | P0 Misuzu 016 | P0 | `学マス 秦谷美鈴 親愛度コミュ11～20` |
| `RINHA-PKT-MISUZU-21-27` | 秦谷美鈴 親愛度コミュ 21～27 | P1 Misuzu 023 + P0 Misuzu 024 | P0 | `学マス 秦谷美鈴 親愛度コミュ21～27` |
| `RINHA-PKT-SAKI-11-20` | 花海咲季 親愛度コミュ 11～20 | P1 Saki 016 | P1 | `学マス 花海咲季 親愛度コミュ11～20` |
| `RINHA-PKT-SAKI-21-27` | 花海咲季 親愛度コミュ 21～27 | P0 Saki 026 | P0 | `学マス 花海咲季 親愛度コミュ21～27` |
| `RINHA-PKT-SAKI-28-37` | 花海咲季 親愛度コミュ 28～37 / H.I.F. | P1 Saki 034 | P1 | `学マス 花海咲季 親愛度コミュ28～37 H.I.F` |
| `RINHA-PKT-UME-11-20` | 花海佑芽 親愛度コミュ 11～20 | P1 Ume 015, 016 | P1 | `学マス 花海佑芽 親愛度コミュ11～20` |
| `RINHA-PKT-UME-21-27` | 花海佑芽 親愛度コミュ 21～27 | P0 Ume 024 | P0 | `学マス 花海佑芽 親愛度コミュ21～27` |
| `RINHA-PKT-UME-28-37` | 花海佑芽 親愛度コミュ 28～37 / H.I.F. | P1 Ume 029 | P1 | `学マス 花海佑芽 親愛度コミュ28～37 H.I.F` |
| `RINHA-PKT-SUPPORT-0097` | support commu containing `story_0097` parts 01–03 | P0 support 0097-01/02/03 | P0 | Prefer exact dialogue-anchor search if public card title is unknown: `学マス 賀陽燐羽 手毬 美鈴 サポートコミュ` / `私が戻るまで 待っていて 学マス` |
| `RINHA-PKT-EVENT-016` | event-story video containing EVENT_016 `main-03` | P0 EVENT_016 main-03 | P0 | `学マス 賀陽燐羽 イベントストーリー` plus distinctive scene dialogue; verify against Source-Lock text before acceptance |

### Packet rule

If a packet includes multiple targets, retain **one** source file and index multiple target locators into it. Do not create redundant clipped copies unless a later analytical release specifically needs bounded clips.

---

# 6. Search and identification protocol

## 6.1 Preferred search order

For Dear scenes:

1. exact host name + `親愛度コミュ` + range;
2. exact host name + exact episode number;
3. add `学マス` or `学園アイドルマスター`;
4. add `賀陽燐羽` / `燐羽` only if needed.

Examples:

- `学マス 月村手毬 親愛度コミュ16`
- `学マス 秦谷美鈴 親愛度コミュ24`
- `学マス 花海咲季 親愛度コミュ26`
- `学マス 花海佑芽 親愛度コミュ24`

For support/event scenes, internal IDs may not be public-facing. Use **dialogue anchors** and participant combinations rather than trusting a numeric search result from another game or dataset.

## 6.2 Identity verification before acceptance

A candidate video is accepted only after at least one exact dialogue sequence aligns with the Source-Lock scene. Verify:

- host character / scene family;
- Rinha is actually the speaker where expected;
- scene order matches the A1/A2 text;
- the video has not silently skipped dialogue lines;
- the Japanese audio corresponds to the visible scene rather than commentary or re-dubbed audio.

Do not accept a video solely because its title contains `燐羽`.

---

# 7. Media acceptance criteria

## 7.1 Required

For dialogue analysis, the retained object should preserve:

- original Japanese voice audio;
- intact scene dialogue;
- original BGM and major SFX where present;
- visible speaker/staging/character-expression context;
- enough lead-in and lead-out to judge pauses, turn-taking, interruptions, and affect transitions;
- stable playback without audio desynchronization.

## 7.2 Preferred

- 1080p if readily available;
- 720p is acceptable when it is the best reliable source;
- original or near-original frame rate;
- AAC/Opus or other non-destructive-enough consumer audio rather than heavily filtered repost audio;
- no added music over the game audio;
- no streamer facecam covering important expressions/UI;
- no commentary talking over the scene.

Resolution is **less important than complete, intelligible Japanese audio and intact timing**.

## 7.3 Subtitles

Separate subtitles are **not required** because the Japanese Source-Lock scripts are already canonical for wording. If subtitles are present:

- retain them as supplemental context only;
- do not let an EN translation override Japanese wording;
- do not reject otherwise good footage merely because it lacks subtitles.

## 7.4 Reject or quarantine

Do not use as baseline authority without a documented exception:

- clipped videos that begin after the relevant emotional setup;
- montage/compilation edits that remove pauses or reorder lines;
- videos with commentary obscuring Rinha's voice;
- dubbed or synthesized replacement speech;
- materially desynchronized audio/video;
- duplicate re-encodes when a higher-quality retained source already exists;
- unknown-source clips whose scene identity cannot be reconciled to a Source-Lock object.

---

# 8. Proposed staging filenames

Use normalized analytical aliases while preserving the original downloaded filename in the manifest.

## 8.1 Whole-packet aliases

```text
GKM_RINHA_AV_TEMARI_DEAR_011_020.mp4
GKM_RINHA_AV_TEMARI_DEAR_021_027.mp4
GKM_RINHA_AV_MISUZU_DEAR_011_020.mp4
GKM_RINHA_AV_MISUZU_DEAR_021_027.mp4
GKM_RINHA_AV_SAKI_DEAR_011_020.mp4
GKM_RINHA_AV_SAKI_DEAR_021_027.mp4
GKM_RINHA_AV_SAKI_DEAR_028_037.mp4
GKM_RINHA_AV_UME_DEAR_011_020.mp4
GKM_RINHA_AV_UME_DEAR_021_027.mp4
GKM_RINHA_AV_UME_DEAR_028_037.mp4
GKM_RINHA_AV_SUPPORT_STORY_0097.mp4
GKM_RINHA_AV_EVENT_016.mp4
```

## 8.2 Exact-scene aliases when only a scene object is available

Pattern:

```text
GKM_RINHA_AV_<HOST>_<SOURCE>_<NUMBER>.mp4
```

Examples:

```text
GKM_RINHA_AV_TEMARI_DEAR_015.mp4
GKM_RINHA_AV_MISUZU_DEAR_024.mp4
GKM_RINHA_AV_SAKI_DEAR_026.mp4
GKM_RINHA_AV_UME_DEAR_024.mp4
GKM_RINHA_AV_SUPPORT_0097_01.mp4
GKM_RINHA_AV_EVENT_016_MAIN_03.mp4
```

The alias is a retrieval aid. It must never replace the source URL, original public title, and exact Source-Lock locator in the manifest.

---

# 9. Proposed staging layout

Do **not** create a new numbered “14th character” core. Rinha remains a distributed non-playable specialist reconstruction.

Recommended temporary acquisition layout:

```text
KAYA_RINHA_AV_STAGING/
├── 00_MANIFEST/
├── 01_P0_REQUIRED/
├── 02_P1_BREADTH_CONTROLS/
├── 03_REUSED_EXISTING_GKM_AV_REFERENCES/
└── 90_REJECTED_OR_DUPLICATE_CANDIDATES/
```

For canonical Drive placement after review, use the existing GKM audiovisual hierarchy and create a **Rinha-specific distributed-character AV home only when media is actually staged**. Do not create an empty `14_KAYA_RINHA` playable-character slot.

---

# 10. Acquisition manifest schema

Create one row per **retained physical media object**, not one row per analytical target.

Suggested CSV/JSON fields:

| field | purpose |
| --- | --- |
| `asset_id` | stable local identifier, e.g. `RINHA-PKT-TEMARI-11-20` |
| `priority` | P0 / P1 / optional |
| `coverage_targets` | one or more `RINHA-AV-*` IDs |
| `source_lock_objects` | one or more `RINHA-XW-*` / exact A1 objects |
| `original_public_title` | title as retrieved |
| `source_url` | acquisition provenance |
| `uploader_or_provider` | source attribution/routing |
| `acquired_at` | timestamp |
| `original_filename` | downloaded/source filename |
| `normalized_alias` | GKM analytical staging name |
| `container` | mp4/mkv/webm/etc. |
| `duration_seconds` | technical check |
| `width` / `height` | technical check |
| `fps` | technical check |
| `video_codec` | technical check |
| `audio_codec` | technical check |
| `audio_sample_rate` | technical check |
| `audio_channels` | technical check |
| `sha256` | byte identity |
| `reuse_existing_drive_id` | existing GKM media ID if reused rather than reacquired |
| `scene_identity_verified` | yes/no |
| `audio_intact` | yes/no |
| `staging_intact` | yes/no |
| `acceptance_status` | ACCEPT / ACCEPT_WITH_LIMIT / REJECT_DUPLICATE / REJECT_QUALITY / REJECT_IDENTITY |
| `notes` | caveats |

---

# 11. Inspection protocol after collection

For each target scene, analyze at least:

1. **speech rate** — especially acceleration/deceleration around emotional leakage;
2. **pause placement** — pre-response hesitation, delayed acknowledgment, interrupted retorts;
3. **pitch movement** — mock sweetness, flat professional judgment, raised anger, vulnerable lowering;
4. **loudness / force** — challenge vs real escalation;
5. **laughter and breath** — `ふふ`, `クク`, sighs, clipped breath, recovery after emotional disruption;
6. **sentence-final delivery** — especially `でしょ`, `じゃない`, `～してあげる`, `なさい`, `くれる？`;
7. **address/name delivery** — Temari/Misuzu/Saki/Ume names versus `お姉ちゃん` play;
8. **timing against facial animation** — gaze, blink/aversion, smile, closed eyes, surprise, embarrassment;
9. **body/staging distance** — approach, withdrawal, contact, kiss/tactile provocation, side-by-side familiarity;
10. **BGM/SFX transition** — whether the scene itself marks a change in affective register;
11. **recipient response** — whether the other character treats Rinha's line as joke, instruction, attack, care, or disclosure;
12. **recovery grammar** — how Rinha exits vulnerability: joke, insult, command, topic shift, silence, or renewed technical focus.

Do not treat any single acoustic metric as a personality fact. The value comes from **within-character contrasts across relationship contexts**.

---

# 12. Matrix questions the AV baseline must answer

The baseline should return explicit findings for these questions.

## Q1 — Martyr/protector denial

When Rinha rejects the flattering interpretation that she deliberately took blame for Temari, does the delivery support:

- sincere rejection;
- defensive minimization;
- embarrassment;
- mixed affect;
- or genuine anger at being moralized?

AV may clarify delivery, but it **cannot by itself prove a hidden motive**. Claim C035 remains motive-bounded unless other evidence changes.

## Q2 — “I am not an idol”

Compare Temari/Misuzu scenes where Rinha disqualifies herself from idolhood against scenes where she becomes animated by idols, training, fans, or return. Determine whether the self-disqualification has a stable performed register distinct from simple indifference.

## Q3 — Professional severity versus hostility

Use Misuzu Dear 024, EVENT_016, and any freely included Temari Dear 014 material to separate:

- technical correction;
- fan/professional judgment;
- playful insult;
- genuine contempt/anger.

The baseline must preserve the matrix rejection of both equations:

> `harsh = hostile`

and

> `harsh = affection`.

## Q4 — Vulnerability and recoding

Use Saki Dear 026, Temari Dear 016, and Support 0097 part 03 to model how Rinha enters and exits direct vulnerability.

Key question:

> Does she lower the abrasive register itself, or does vulnerability appear *inside* the same lexical shell through timing, softness, silence, or recovery behavior?

## Q5 — Relationship-specific register

Establish whether recurring lexical forms are performed differently with:

- Temari;
- Misuzu;
- Saki;
- Ume;
- fans/public;
- childhood/teaching targets.

This will govern speech simulation in the dossier.

## Q6 — Sister/date/kiss coding

P1 Saki/Ume scenes should determine the **performed degree of intimacy/play**, but must not convert tone into categorical romance or ownership. Preserve the textual matrix status `ALLOW_CODING_ONLY` unless new explicit evidence exists.

## Q7 — Future-facing Rinha

Support `story_0097` should establish the performed late-state difference between:

- Rinha talking about unfinished obligations;
- Rinha coordinating with Temari/Misuzu;
- Rinha promising return;
- Rinha explicitly asking Ume's performance to affect her unresolved worry.

This is the principal AV control for the dossier's post-SyngUp model.

---

# 13. No current music/MV acquisition requirement

This baseline is **dialogue/performance-of-dialogue focused**.

Do not create a Rinha song/MV collection merely to mirror the 13 playable-character baselines. Current Source Lock and matrix evidence do not establish a character-specific musical corpus whose omission blocks the dossier.

Music/MV acquisition should be added only if a separately identifiable Rinha performance artifact is discovered and it can answer a specific open claim.

This preserves the architecture rule that Rinha is a distributed specialist reconstruction, not a synthetic fourteenth playable core.

---

# 14. Expected analytical outputs after acquisition

Once the media is staged and verified, produce only artifacts with distinct responsibilities. Recommended outputs:

1. **`GKM_KAYA_RINHA_COMPLETE_AUDIOVISUAL_BASELINE.md`**
   - canonical integrated AV findings;
   - scene-by-scene discrimination results;
   - relation-specific performed register;
   - explicit text→AV claim transitions.

2. **`GKM_KAYA_RINHA_DIALOGUE_VOICE_ACTING_CLOSE_READING.md`**
   - specialist acoustic/performance synthesis if the inspected set is rich enough to justify a separate topical home;
   - otherwise fold this responsibility into the complete baseline rather than creating a redundant document.

3. **`GKM_KAYA_RINHA_AV_EVIDENCE_AND_METRICS_MATRIX.md`**
   - target IDs, source assets, technical metadata, observed vocal/staging evidence, confidence, and affected RINHA-C claims.

4. **source manifest + SHA-256 audit**
   - one retained physical object per manifest row;
   - duplicate/reuse references explicit.

5. **Rinha evidence-matrix revision pass**
   - only AV-sensitive claims should change;
   - use `PRESERVE / STRENGTHEN / REVISE / DOWNGRADE / REJECT / OPEN`.

6. **`GKM_KAYA_RINHA_CHARACTER_DOSSIER.md`**
   - only after the AV gate is satisfied and matrix revisions are integrated.

---

# 15. AV completion criteria

The targeted Rinha AV baseline is complete when:

- all 11 P0 targets are inspected or explicitly unavailable after retrieval audit;
- P1 targets are inspected when reasonably obtainable, especially when included in already-retained whole packets;
- all retained media has source provenance and SHA-256 identity;
- each analytical target is mapped to one retained physical source object;
- no duplicate reacquisition is mistaken for additional evidence;
- playful / defensive / wounded / embarrassed / professionally severe / genuinely hostile delivery states have been compared rather than inferred from vocabulary alone;
- relationship-specific performed register is documented for Temari, Misuzu, Saki, and Ume;
- Support `story_0097` establishes a late present-tense control;
- the evidence matrix has been revised for AV-sensitive claims;
- the dossier no longer depends on unresolved tone assumptions for its core behavioral model.

---

# 16. Collector-facing checklist

## First pass — cheapest path

- [ ] Check whether existing **Temari Dear 11–20** AV is retained.
- [ ] Check whether existing **Misuzu Dear 11–20** AV is retained.
- [ ] Check whether existing **Misuzu Dear 21–27** AV is retained.
- [ ] Check whether existing **Saki Dear 21–27** AV is retained.
- [ ] Check whether existing **Ume Dear 21–27** AV is retained.
- [ ] Locate/acquire **Support story 0097**, ideally all three parts in one video.
- [ ] Locate/acquire **EVENT_016 main-03** or the narrowest full event-story video containing it.

These seven checks/acquisitions are the highest-value initial pass because they can close most P0 requirements quickly.

## Second pass — P0 cleanup

- [ ] Ensure Temari Dear 015 / 016 / 020 are all present.
- [ ] Ensure Misuzu Dear 016 / 024 are present.
- [ ] Ensure Saki Dear 026 is present.
- [ ] Ensure Ume Dear 024 is present.
- [ ] Ensure Support 0097 parts 01 / 02 / 03 are present.
- [ ] Ensure EVENT_016 main-03 is present.

## Third pass — P1 controls

- [ ] Saki Dear 016.
- [ ] Saki Dear 034.
- [ ] Ume Dear 016.
- [ ] Ume Dear 029.
- [ ] Temari Dear 024.
- [ ] Misuzu Dear 023.
- [ ] Ume Dear 015.

## For every new retained object

- [ ] save original URL/title/provider;
- [ ] preserve original filename;
- [ ] assign normalized GKM alias;
- [ ] record duration/resolution/FPS/audio properties;
- [ ] compute SHA-256;
- [ ] verify scene against Source-Lock dialogue;
- [ ] mark P0/P1 targets covered;
- [ ] avoid uploading a duplicate if an equivalent existing Drive source already survives.

---

# 17. Recommended next operation after user review

After this request packet is approved:

1. perform an **existing-Drive AV reuse audit** for the 18 target scenes;
2. convert the results into a concrete acquisition manifest with `REUSE_EXISTING / MISSING / ACQUIRED` state;
3. collect only the missing media;
4. verify hashes/technical metadata/source identity;
5. inspect the P0 set first;
6. inspect P1 breadth controls;
7. emit `GKM_KAYA_RINHA_COMPLETE_AUDIOVISUAL_BASELINE.md` and any justified specialist evidence artifacts;
8. revise AV-sensitive matrix claims;
9. proceed to `GKM_KAYA_RINHA_CHARACTER_DOSSIER.md`.

Until those steps occur, the current textual matrix remains authoritative for Rinha person-level claims and this request document remains operational/provisional.
