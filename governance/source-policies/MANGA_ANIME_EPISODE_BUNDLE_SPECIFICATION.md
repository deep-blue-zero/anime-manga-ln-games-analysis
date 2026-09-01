---
title: Manga / Anime Episode Bundle Specification
artifact_id: MANGA_ANIME_EPISODE_BUNDLE_SPECIFICATION
artifact_type: audiovisual_source_object_specification
version: 1.2
status: canonical
generation: V1
scope: corpus-wide anime episode conversion and analytical source-object semantics
created: 2026-08-27
last_updated: 2026-08-27
transport_constraints_verified: 2026-08-27
transport_constraints_are_provider_snapshot: true
maintainer: ChatGPT + user
source_boundary: "Corpus-wide definition of an analytically useful anime episode bundle and the current conversion-workflow exemplar LLS_s02e01_screenshots.zip"
supersedes: null
superseded_by: null
do_not_use_as_current_authority: false
do_not_use_as_literary_evidence: true
---

# Manga / Anime Episode Bundle Specification

## Governing definition

> **An anime episode bundle is a synchronized multimodal analytical source object derived from one episode. It is not merely a ZIP of screenshots.**

The purpose of an episode bundle is to transform an audiovisual episode into an object that can be inspected, cited, searched, cross-referenced, and analyzed without discarding the relationships among **image, time, dialogue, language, audio performance, shot structure, and source provenance**.

A complete bundle should allow an analyst to move in both directions:

> **dialogue / claim / performance observation -> timestamp -> frame / shot context -> audio / subtitle context -> source episode**

and

> **frame / visual event -> timestamp -> dialogue / subtitle context -> nearby shot context -> source episode**.

A screenshot archive that lacks these crosswalks may still be a useful derivative, but it should not be assumed to be a complete analytical episode bundle.

---

# 1. Why the bundle exists

Anime is not adequately represented by a transcript alone or by a collection of still images alone. A sequential deep reading may depend on several evidence channels at once:

- spoken Japanese and its timing;
- translation or paired-language comparison;
- voice performance and nonverbal vocalization;
- music and sound;
- shot changes and shot duration;
- character blocking, pose, gaze, costume, setting, and composition;
- visual transitions and editing rhythm;
- exact temporal relation between speech and image;
- source identity and extraction provenance.

The bundle is therefore an **analysis-oriented derivative of the episode**, not a replacement for the original encoded video and not an independent literary authority. Where exact motion, animation timing, continuous music, or another feature cannot be recovered adequately from the bundle, analysis must escalate back to the source video or another retained primary-source object.

---

# 2. Representative current-generation exemplar

This specification was grounded against the user-provided current conversion-workflow exemplar:

`LLS_s02e01_screenshots.zip`

Series: *Love Live! Superstar!!*  
Episode: `S02E01`  
Bundle schema reported by metadata: `2`

The exemplar contains **884 files** and approximately **187.3 MB uncompressed**. Its major layers are:

| Layer | Exemplar contents |
|---|---:|
| Timestamped clean episode frames | 824 JPEGs |
| Contact sheets | 42 JPEGs |
| Subtitle tracks | 3 ASS files |
| Complete Japanese episode audio | 1 MP3 |
| JSON metadata/index files | 10 |
| CSV indexes/manifests | 4 |

The exact counts, codecs, filenames, thresholds, schema version, and extraction heuristics are **implementation details of this exemplar**, not permanent corpus requirements. Future workflow versions may change them while still satisfying the semantic contract below.

---

# 3. Semantic layers of an episode bundle

A current complete bundle normally exposes the following layers or an explicitly documented equivalent.

## 3.1 Source identity and provenance

The bundle should identify the episode object from which it was derived and enough technical information to distinguish it from another encode or edition.

The exemplar's `bundle_metadata.json` records, among other things:

- series title and episode identifier;
- source-video path at extraction time;
- source byte size;
- episode duration;
- video stream index and codec;
- Japanese audio stream identity, codec, sample rate, and channels;
- embedded English subtitle stream identity;
- bundle generation timestamp;
- hashes for important extracted subtitle/audio components.

The local source path is provenance, not a portable retrieval route. Canonical Drive/source inventory documents should separately record where the retained source can currently be found.

## 3.2 Timestamped clean visual frames

The visual layer consists of clean source frames extracted at analytically useful events. In the exemplar these are 1920x1080 JPEGs with subtitle burning disabled.

A representative filename is:

`000003_shot-change+subtitle-start_00-00-01.001.jpg`

The filename encodes three useful dimensions:

1. a stable extraction/event sequence number;
2. one or more reasons the frame was selected;
3. the episode timestamp.

Observed selection labels in the exemplar include:

- `shot-change`;
- `shot-representative`;
- `subtitle-start`;
- `subtitle-midpoint`;
- `auto-visual-interval`;
- `silent-gap`.

Multiple reasons may be combined with `+`. This is intentional: a single frame can simultaneously represent a cut boundary, dialogue boundary, and periodic visual sample.

The selection labels describe **why a frame exists in the bundle**, not an interpretation of what the frame means.

## 3.3 Frame manifest

The screenshot filenames are not expected to carry all useful metadata. A manifest provides the machine-readable crosswalk.

The exemplar's `manifest.csv` / `manifest.json` associates frame events with fields including:

- event index;
- event kind;
- timestamp in seconds and formatted timestamp;
- filename;
- subtitle text where applicable;
- subtitle style and speaker fields where available;
- extraction details such as shot boundaries or cue duration;
- deduplication state;
- canonical-frame replacement when a frame has been externalized or deduplicated.

The manifest is the preferred way to understand *why* a frame was selected and how it relates to the extraction process.

## 3.4 Contact sheets

Contact sheets are browsing aids that compress groups of extracted frames into larger overview images.

The exemplar includes 42 contact sheets and `contact_sheets.json` as an index. Their purpose is rapid visual reconnaissance: scene progression, composition changes, costumes, locations, staging patterns, and candidate moments can be surveyed before opening individual full-resolution frames.

Contact sheets are derivatives of the timestamped frames. They should not be treated as a substitute for the underlying frame when fine visual evidence matters.

## 3.5 Primary-language subtitles / transcript layer

Where usable original-language subtitle or transcript material exists, the bundle should preserve it as the primary linguistic analysis layer and record its timing status.

The exemplar includes:

`subtitles/S02E01.ja.corrected.ass`

with metadata describing it as the **primary analysis and frame-timing track**. Its metadata also records a timing audit and the correction/shift used by the workflow.

A corrected or aligned subtitle derivative should remain distinguishable from the untouched source from which it was produced.

## 3.6 Paired translation layer

When available, a translated subtitle track can provide a secondary cross-language aid without replacing the original-language text.

The exemplar preserves both:

- `S02E01.en.dialogue.ass` — the full embedded Blu-ray Dialogue stream, including signs/song styling events; and
- `S02E01.en.spoken-dialogue.ass` — a filtered speech-only derivative used for dialogue pairing.

This distinction matters. A subtitle file labeled "Dialogue" by an encode may contain more than spoken dialogue, and a machine-friendly paired speech derivative may deliberately omit signs, songs, or styling events.

Original-language material remains the preferred basis for exact wording, speech-register, and translation-sensitive claims.

## 3.7 Dialogue index

The dialogue index binds language to audiovisual context.

The exemplar's `dialogue_index.csv` / `dialogue_index.json` contains one row per primary Japanese cue and fields including:

- cue index;
- start/end time and duration;
- speaker/style where available;
- Japanese text;
- paired English text and metadata where matched;
- nearest extracted frame;
- nearest contact sheet;
- cue-start frame;
- cue-midpoint frame;
- previous and next shot frames.

The exemplar reports 456 primary rows, with paired English available for 360 rows (about 78.9%). Missing paired text does **not** imply missing Japanese dialogue; it means no paired English cue satisfied the pairing rules.

This index is one of the bundle's highest-value analytical objects because it permits a dialogue observation to be routed immediately into its visual and temporal context.

## 3.8 Complete episode audio

A complete audio derivative preserves the episode's continuous audible layer for voice-performance, music, silence, sound-design, and timing analysis.

The exemplar includes:

`audio/s02e01.complete-audio.mp3`

identified as Japanese audio and duration-matched to the episode to within a fraction of a millisecond in the recorded metadata.

Compressed analysis audio is a derivative convenience object. When codec artifacts, channel structure, exact mix, or lossless fidelity matters, analysis should return to the retained source episode/audio stream.

## 3.9 Shot and scene indexes

Shot/scene indexes provide structural navigation rather than literary conclusions.

The exemplar's analysis metadata reports 375 shot changes / 355 shot segments, and `scene_index.csv` / `.json` provides a higher-level scene container with representative frames/contact sheets.

Scene segmentation produced mechanically by the conversion workflow must **not** automatically be treated as narratively meaningful scene analysis. In the exemplar, the scene index contains a single episode-spanning scene, demonstrating why these indexes should be treated as navigation metadata unless a series method explicitly validates a stronger semantic segmentation scheme.

## 3.10 Extraction and analysis statistics

Files such as `analysis_stats.json` and `batch_summary.json` record how the derivative was produced.

The exemplar records parameters and outcomes including:

- duration;
- cue count;
- shot-change count;
- automatically identified visually dense ranges;
- screenshot extraction mode;
- subtitle midpoint rules;
- event counts before and after time deduplication;
- visual deduplication counts;
- screenshot/contact-sheet counts;
- whether subtitles were burned into frames;
- hardware-acceleration state;
- batch success state.

These files are useful for QA and reproducibility. They are not evidence for literary interpretation.

## 3.11 Visual deduplication and shared OP/ED handling

A bundle may remove visually redundant frames while preserving an audit trail.

The exemplar contains:

- `manifest_visual_dedupe_removed.csv` / `.json`;
- `op_ed_dedup.json`.

Its OP/ED policy states that only strict aligned image matches should be externalized; ambiguous or unmatched frames remain local. It also defines a shared reference form:

`shared://<OP-or-ED>/<variant>/frames/<file>`

The exemplar identified its OP as a new variant and therefore preserved it locally rather than externalizing it.

Deduplication must never silently destroy the ability to reconstruct where an analytical frame came from. Removed frames require an auditable canonical replacement or other traceable disposition.

---

# 4. Bundle structure: conceptual tree

A current-generation bundle can be understood conceptually as:

```text
<episode_bundle>.zip
|
|-- timestamped clean visual frames (*.jpg)
|-- bundle_metadata.json
|-- analysis_stats.json
|-- batch_summary.json
|-- manifest.csv
|-- manifest.json
|-- dialogue_index.csv
|-- dialogue_index.json
|-- scene_index.csv
|-- scene_index.json
|-- contact_sheets.json
|-- manifest_visual_dedupe_removed.csv
|-- manifest_visual_dedupe_removed.json
|-- op_ed_dedup.json
|
|-- contact_sheets/
|   `-- contact_sheet_*.jpg
|
|-- subtitles/
|   |-- <episode>.ja.corrected.ass
|   |-- <episode>.en.dialogue.ass
|   |-- <episode>.en.spoken-dialogue.ass
|   `-- subtitle_info.json
|
`-- audio/
    `-- <episode>.complete-audio.mp3
```

This tree describes the **current exemplar**, not a frozen filename schema. Semantic roles are more important than literal names.

---

# 5. Minimum semantic contract for calling an object an episode bundle

The corpus should use the term **episode bundle** only when the object is intended to provide a synchronized analytical representation of a single episode.

At minimum, the bundle or its immediately associated source record should make the following recoverable:

1. **Episode identity and provenance** — what episode/encode/source object the derivative came from.
2. **Temporal coordinate system** — timestamps that allow evidence layers to be aligned back to the episode.
3. **Visual evidence layer** — extracted frames or an equivalent visual sampling strategy with selection provenance.
4. **Visual index/manifest** — machine-readable mapping from extracted visuals to timestamps and selection reasons.
5. **Dialogue/language layer** — primary-language subtitles/transcript when available, with timing retained.
6. **Cross-modal linkage** — a way to move between dialogue cues and nearby visual evidence.
7. **Audio access** — embedded analysis audio or an explicit, stable route to the aligned audio/source episode when voice/music/sound analysis is in scope.
8. **Extraction provenance/QA metadata** — enough information to understand major transformations such as subtitle correction, visual deduplication, or frame-selection heuristics.
9. **Missing-layer disclosure** — if an expected layer is absent, the absence is explicit rather than silently assumed.

A package containing only screenshots, only subtitles, only audio, or only contact sheets is a **partial episode derivative**, not a complete episode bundle. A series architecture may declare a partial derivative sufficient for a particular analytical purpose, but may not redefine the corpus-wide term `episode bundle` below this global minimum semantic contract.

Classify partial objects explicitly when practical: `partial_episode_derivative` for the general case, `screenshot_derivative` for still-image packages, `subtitle_derivative` for subtitle/transcript-only packages, and `audio_derivative` for audio-only packages. Existing packages do not need to be rebuilt solely for terminology; correct classification prospectively and when an old source record is next touched.

---

# 6. Core versus optional/enrichment layers

Not every source or series will support identical inputs. The semantic contract therefore distinguishes between structural requirements and enrichments.

## Core structural responsibilities

A complete analytical bundle should normally provide or route to:

- source identity/provenance;
- synchronized timing;
- visual samples plus manifest/index;
- primary-language dialogue/subtitle evidence where available;
- audio or an aligned audio route;
- cross-modal linkage;
- extraction/QA metadata.

## Common enrichments

These are high-value but may be unavailable or inappropriate in a particular source:

- paired English/translation cues;
- speaker attribution;
- cue-start and cue-midpoint frame links;
- previous/next shot context;
- contact sheets;
- automatic visually dense interval sampling;
- scene index;
- OP/ED cross-episode deduplication;
- lossless or multichannel audio derivatives;
- music-specific segmentation;
- OCR/sign-text indexes;
- face/character-presence indexes;
- shot-scale/camera-motion annotations.

The architecture should not pretend an enrichment exists merely because another anime project has it.

---

# 7. Evidence authority and limitations

An episode bundle occupies an intermediate evidentiary position.

It is usually more useful for analysis than repeatedly opening a full encoded episode because it exposes indexed, synchronized evidence. But it remains a **derived analytical representation**.

Use the bundle confidently for:

- locating candidate moments;
- checking static composition;
- associating dialogue with nearby frames;
- inspecting corrected subtitle text and timing metadata;
- listening to continuous analysis audio;
- tracking shot/event structure;
- producing timestamped evidence locators.

Escalate to the retained primary video/audio when the claim depends materially on:

- continuous motion or animation timing;
- exact transition behavior between sampled frames;
- frame-precise microtiming beyond the bundle's extraction resolution;
- original codec/channel fidelity;
- sound localization or mix details not preserved in the derivative;
- subtitle/transcript correctness that remains uncertain;
- a visual moment not captured by the selection strategy;
- verification against the untouched source encode.

A bundle's convenience must not be mistaken for higher source authority than the episode from which it was derived.

---

# 8. Continuous-video escalation protocol

## 8.1 Governing principle

> **Continuous video should be requested or supplied only when a material analytical question depends on temporally continuous audiovisual evidence that the episode bundle cannot preserve or reconstruct with adequate confidence.**

The episode bundle remains the default analytical object. Continuous video is an **escalation source**, not a routine prerequisite for every anime deep reading.

This protocol exists because sampled frames, subtitle timing, shot indexes, and continuous analysis audio preserve many important properties of an episode but cannot fully preserve motion, evolving performance, camera movement, transition behavior, audiovisual synchronization, or other phenomena whose meaning exists *between* sampled frames.

The escalation decision should therefore be driven by the **kind of claim under examination**, not by the mere availability of video.

## 8.2 Standard escalation states

Use the following states where a method, deep reading, source audit, or corpus map needs to record the decision explicitly:

| State | Meaning |
|---|---|
| `VIDEO_NOT_REQUIRED` | Existing bundle evidence is adequate for the material analytical question. |
| `VIDEO_TARGETED_ESCALATION` | Continuous audiovisual evidence is required, but the diagnostic interval or intervals are known and bounded. Prefer targeted clips or a bounded continuous segment when operationally available. |
| `VIDEO_FULL_EPISODE_ESCALATION` | The relevant phenomenon is distributed across a large portion of the episode, cannot safely be localized in advance, or the episode's continuous audiovisual structure is itself the object of analysis. |

These states describe **evidence need**, not literary authority. A higher escalation state does not make the resulting interpretation inherently more authoritative.

## 8.3 Positive escalation triggers

Continuous video is materially justified when one or more of the following conditions applies and the bundle cannot answer the question with adequate confidence:

| Trigger | Why the bundle may be insufficient |
|---|---|
| **Animation or bodily motion** | Gesture trajectory, movement quality, hesitation, acceleration, weight, choreography, or motion between retained frames matters. |
| **Camera movement** | Pans, tilts, tracking, zooms, reframing, rack focus, or changing spatial relationships carry analytical meaning. |
| **Editing rhythm** | Exact shot duration, cut timing, montage rhythm, reaction timing, or pacing is load-bearing. |
| **Transition behavior** | Match cuts, dissolves, wipes, transformations, compositing transitions, or other between-frame phenomena matter. |
| **Microperformance over time** | A changing expression, gaze movement, posture shift, delayed reaction, or acting beat cannot be represented reliably by isolated stills. |
| **Dialogue-performance synchronization** | The relation among speech, facial movement, gesture, pauses, overlap, silence, and reaction timing matters. |
| **Music dramaturgy** | Cue onset/termination, synchronization to cuts or gesture, development across a scene, dynamic change, or dialogue/music interaction matters. |
| **Sound-image relationship** | Offscreen sound, sound bridges, spatial cues, silence, effects, or audiovisual counterpoint require synchronized continuity. |
| **Action geography or blocking** | Continuous movement through space is necessary to understand staging, choreography, power relationships, or spatial logic. |
| **Sampling uncertainty** | The relevant event appears to fall between retained frames, or the bundle's visual sampling is too sparse for the claim. |
| **Derivative ambiguity** | Subtitle correction, frame selection, deduplication, scene segmentation, or another conversion step may have changed how the evidence appears. |
| **High-impact source verification** | A load-bearing claim remains disputed or uncertain after bundle inspection and should be verified against continuous source evidence. |

The trigger must connect to a **material analytical consequence**. Merely preferring to watch the video is not an escalation criterion.

## 8.4 Situations that normally do not justify video escalation

Continuous video usually adds little when the question is already adequately answered by synchronized bundle layers, for example:

- exact Japanese wording where the primary-language subtitle/transcript layer is reliable;
- static composition, costume, setting, pose, or isolated facial-expression inspection;
- ordinary dialogue chronology;
- character-presence or location checks;
- basic timestamp/evidence localization;
- a voice-performance question answerable from the aligned complete audio alone;
- source inventory or checksum work;
- a claim whose uncertainty is interpretive rather than caused by missing temporal audiovisual evidence.

Do not request full video merely because the project is important, the episode is climactic, or video happens to be available.

## 8.5 Targeted interval versus full episode

When continuous evidence is required, prefer the **smallest continuous object that preserves the relevant phenomenon**.

Use `VIDEO_TARGETED_ESCALATION` when:

- the relevant scene or temporal region is already known;
- a bounded confrontation, performance, transition, action passage, or musical sequence contains the diagnostic evidence;
- surrounding context available in the bundle is sufficient to interpret the continuous interval;
- one or several short clips would answer the question without losing necessary continuity.

Use `VIDEO_FULL_EPISODE_ESCALATION` when:

- the phenomenon is distributed across many separated regions;
- the analyst cannot safely identify the relevant intervals before viewing continuity;
- whole-episode pacing, editing, musical architecture, blocking, or audiovisual form is itself under study;
- repeated targeted escalations would be less reliable or less efficient than one complete episode object;
- contextual setup and payoff across the episode materially affect interpretation of the continuous evidence.

A full episode should not be the automatic first escalation when a bounded interval is sufficient.

## 8.6 Transport and size constraints

For the current corpus workflow, continuous-video derivatives should be prepared with connector accessibility in mind:

- **prefer `<=256 MB`** when practical, because this is the preferred working size for Drive-connector access;
- files **above 256 MB and up to 512 MB** are acceptable when duration or audiovisual fidelity materially warrants the larger object;
- **do not design routine analysis around files exceeding 512 MB**; when the retained source is larger, create a suitably compressed analytical derivative or targeted interval instead.

These limits are a **time-bounded provider/workflow snapshot**, verified on `2026-08-27`, rather than a permanent platform contract. Re-check current platform and connector capability when a new extraction pipeline is designed, a large-video workflow begins, connector/upload capabilities materially change, or the recorded snapshot is clearly stale.

These are **transport constraints, not evidentiary thresholds**. A phenomenon does not become less analytically important because the untouched source encode is large. The correct response is to produce a derivative that preserves the evidence required by the claim while remaining operationally accessible.

Compression should preserve the feature that motivated escalation. For example, an action/motion question requires sufficient frame rate and visual clarity; a music/sound-image question requires sufficiently faithful synchronized audio; a lip/gesture timing question requires stable audiovisual sync. File-size reduction that destroys the diagnostic feature defeats the purpose of escalation.

## 8.7 Temporal-claim discipline

> **Absence of continuous video should limit the claim, not invite reconstruction of unseen motion from sampled stills.**

For example, two retained frames may establish that a character looks downward at time A and toward another character at time B. Without continuous evidence, they do not by themselves establish that the intervening gaze shift was slow, hesitant, abrupt, rhythmically synchronized to music, or performed in a particular continuous manner.

When the bundle establishes endpoints but not the temporal path between them, the analysis should either:

1. formulate only the endpoint claim supported by the bundle; or
2. escalate to continuous video if the temporal path is materially important.

This rule applies equally to body movement, expression changes, camera movement, edit timing, choreography, and audiovisual synchronization.

## 8.8 Recording an escalation decision

Where continuous video materially affects a deep reading or source audit, record the decision compactly. A suitable machine-readable form is:

```yaml
continuous_video_escalation:
  state: VIDEO_TARGETED_ESCALATION
  reason: "Microperformance and dialogue/reaction timing cannot be established from sampled frames alone."
  interval: "00:12:41-00:14:08"
  supplied_object: null
  resolved: false
```

For a full episode:

```yaml
continuous_video_escalation:
  state: VIDEO_FULL_EPISODE_ESCALATION
  reason: "Whole-episode musical/editing architecture is under analysis."
  preferred_size_mb_max: 256
  acceptable_size_mb_max: 512
  supplied_object: null
  resolved: false
```

The exact schema may vary by series, but the analytical reason should remain recoverable. If the question is resolved, the deep reading or evidence ledger should identify the continuous object or interval actually inspected.

## 8.9 Relationship to series-specific methods

Series-specific analytical methods may strengthen this protocol when continuous form is unusually load-bearing. Examples include:

- dance, concert, revue, or music-driven anime;
- action works where choreography and spatial continuity are central;
- visually experimental works with meaningful camera or transition behavior;
- performance-heavy character studies where microacting and reaction timing are recurrent evidence channels.

They may also remain bundle-first when continuous evidence is rarely diagnostic.

Series-specific rules should refine the corpus-wide protocol rather than silently redefining the term `episode bundle` or treating continuous video as universally mandatory.

---

# 9. Relationship to deep-reading methods and synthesis architecture

For anime projects using episode bundles, the governing analytical method should state how the bundle is consumed. It should define, as relevant:

- whether clean frames or contact sheets are the default first-pass visual surface;
- when the dialogue index is used instead of reading ASS directly;
- when Japanese text must be checked against the corrected subtitle source;
- when audio must be listened to directly;
- when analysis escalates back to the source video;
- which continuous-video escalation state applies and whether targeted or full-episode continuity is required;
- how timestamps and frame filenames are cited in deep readings;
- how visual/music/voice observations flow into longitudinal ledgers.

The synthesis architecture should identify which bundle-derived evidence channels require cumulative homes. For example, a music-heavy anime may need a musical-dramaturgy ledger; a performance-heavy character project may need voice/performance tracking; a visually formalist work may need a visual-grammar ledger.

The existence of rich bundle data does **not** itself justify creating every possible ledger. Architecture remains proportional to the work.

---

# 10. Source inventory terminology

Use these terms consistently where practical:

**Source episode** — the retained encoded audiovisual episode or equivalent primary media object.

**Episode bundle** — the synchronized multimodal analytical derivative that satisfies this specification's corpus-wide minimum semantic contract.

**Screenshot/frame set** — extracted still images without implying the rest of the bundle contract.

**Contact sheets** — browsing composites derived from extracted frames.

**Subtitle/transcript derivative** — extracted, corrected, filtered, or aligned dialogue text.

**Analysis audio** — extracted audio derivative used for convenient listening/inspection.

**Bundle manifest/index** — machine-readable structures linking evidence layers to timestamps and one another.

**Partial episode derivative (`partial_episode_derivative`)** — useful extracted material that does not satisfy the complete bundle contract.

**Screenshot derivative (`screenshot_derivative`)** — still-image material that does not by itself satisfy the complete bundle contract.

**Subtitle derivative (`subtitle_derivative`)** — subtitle or transcript material that does not by itself satisfy the complete bundle contract.

**Audio derivative (`audio_derivative`)** — audio material that does not by itself satisfy the complete bundle contract.

This terminology is intended to prevent phrases such as "episode bundle," "screenshots," "transcript," and "source episode" from being treated as interchangeable.

---

# 11. Versioning and workflow evolution

The conversion pipeline is expected to evolve.

Future bundle schema versions may:

- change extraction thresholds;
- add or remove derivative indexes;
- alter visual deduplication;
- change audio codec or fidelity;
- improve speaker attribution;
- improve scene segmentation;
- add music, OCR, character-presence, or motion metadata;
- externalize shared OP/ED material differently;
- change filenames while retaining equivalent semantic roles.

Therefore series methods should normally depend on **semantic roles** such as `dialogue_index`, `clean_frames`, `primary_language_subtitles`, `analysis_audio`, and `manifest`, not on a permanent assumption that a particular workflow version or literal filename will always exist.

When a bundle schema changes materially, the source inventory or project corpus map should record the transition boundary so later analysts know which episodes expose which bundle capabilities.

---

# 12. Representative exemplar findings that must not be universalized

The following are true of the inspected `LLS_s02e01_screenshots.zip` exemplar but should **not** be treated as global constants:

- exactly 824 extracted episode frames;
- exactly 42 contact sheets;
- 1920x1080 JPEG visual frames;
- MP3 analysis audio;
- Japanese corrected ASS plus two English ASS derivatives;
- 456 Japanese dialogue-index rows;
- approximately 78.9% paired-English coverage;
- the current shot-change and visual-density thresholds;
- the one-scene result of the current scene-index heuristic;
- schema version 2;
- OP variant identifier `OP_V002`;
- current filenames or Windows source paths.

These details document the current workflow's output shape. The governing concept is the synchronized multimodal evidence object, not these particular numbers.

---

# 13. Relationship to corpus-wide governance

`MANGA_ANIME_PROJECT_INITIATION_AND_ARCHITECTURE_POLICY.md` governs whether a new anime project has an adequate method and synthesis architecture before sequential analysis begins.

This specification supplies a shared definition of one important anime source object that those methods and architectures may reference.

`MANGA_ANIME_DRIVE_INDEX.md` remains the routing surface for locating the current canonical specification and series-specific source routes.

Neither this specification nor an episode bundle determines literary authority by itself. Authority and supersession remain governed by the archive's authority policy and the relevant series architecture/source inventory.

---

# Changelog

## v1.2 — 2026-08-27 — Administrative semantic and transport hardening

- Corrected the duplicated word in the human-readable front-matter title.
- Made the global minimum episode-bundle contract non-overridable while preserving project-specific sufficiency judgments for explicitly labeled partial derivatives.
- Marked connector/upload thresholds as a time-bounded provider snapshot and added mandatory re-check triggers.

