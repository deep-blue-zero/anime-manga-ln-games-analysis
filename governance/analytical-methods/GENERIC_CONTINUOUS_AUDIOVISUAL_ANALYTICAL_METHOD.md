---
title: Generic Source-Bounded Continuous Audiovisual Analytical Method
artifact_id: GENERIC_CONTINUOUS_AUDIOVISUAL_ANALYTICAL_METHOD
artifact_type: generic_continuous_av_analytical_method_reference
artifact_role: reusable_corpus_level_analytical_reference_method
version: "1.0"
status: canonical
scope: source-bounded analysis of time-based audiovisual units by an analyst with verified continuous audiovisual inspection, and new-project AV method bootstrap
authority_scope: this_reusable_reference_only
adoption: opt_in
project_local_authority: false
created: 2026-10-24
maintainer: Claude + user
source_boundary: "Methodological reference only; no series findings or primary-source evidence"
do_not_use_as_current_authority: false
do_not_use_as_literary_evidence: true
canonical_home: governance/analytical-methods/GENERIC_CONTINUOUS_AUDIOVISUAL_ANALYTICAL_METHOD.md
drafted_against_commit: 6a3afaaf1bb61e0993db379ab4074c46e9ea98dd
supersedes: []
superseded_by: []
---

# Generic Source-Bounded Continuous Audiovisual Analytical Method

## Adoption and authority boundary

This artifact is a reusable, corpus-level analytical reference for analysts that can inspect synchronized video and audio natively: the `CONTINUOUS_AV` lane of the [medium and inspection-lane routing policy](../source-policies/MANGA_ANIME_MEDIUM_AND_INSPECTION_LANE_ROUTING_POLICY.md). It is canonical only for this reference responsibility, and adoption is opt-in. It is not a repository policy, a project-local governing method, a synthesis architecture, a current-state entrypoint, or literary evidence.

1. It does not govern an existing series merely by residing in Git.
2. It does not by itself satisfy a project's governing-method requirement or open a `SEQUENTIAL_ANALYSIS_LOCK`.
3. A series adopts it by adapting an AV-lane companion method inside its method family (routing policy Section 6), naming the channels its source makes load-bearing.
4. Optional passes are activated only when the source earns them.

It has three uses:

- **Independent AV reading**: a standalone, source-bounded reading of an episode, film movement, cutscene, or performance.
- **Stage 2 review** under the [audiovisual reconciliation protocol](../source-policies/MANGA_ANIME_AUDIOVISUAL_RECONCILIATION_PROTOCOL.md), testing a bundle-mediated reading.
- **Blind benchmarking**: Part IX.

The [generic anime episode method](GENERIC_ANIME_EPISODE_ANALYTICAL_METHOD.md) remains the reference for the reading's dramatic, character, relationship, institutional, thematic, and counterevidence responsibilities. This method does not repeat those responsibilities. It specifies what continuous inspection adds and how to keep it honest. For blind use, give the analyst both documents.

## 0. Purpose

A transcript and a set of stills preserve much of an episode, but not what happens between the stills: how a gesture travels, how long a reaction is withheld, where a music cue enters relative to a cut, how a voice changes across a line. This method governs the observation and interpretation of those phenomena.

The governing principle is:

> **Observe what happens in time (between frames, across cuts, under and around speech), record it against the episode's clock before interpreting it, and claim no more than the continuous evidence shows.**

---

# I. Epistemic boundary

## 1. Sequential seal and prior-knowledge quarantine

Apply the generic anime method's Sections 1–2 unchanged. Continuous inspection adds three exposures that must be quarantined:

- **Recognition of performers.** Do not identify voice actors, singers, or musicians by ear, and do not import knowledge about them.
- **Recognition of music.** Do not import knowledge of a song's release, lyrics, credits, or later reuse from outside the authorized boundary.
- **Recognition of famous scenes.** A well-known scene can trigger remembered interpretation. Observe it as if it were unknown; record any intrusion of prior knowledge as such.

---

# II. Evidence classes

## 2. Classes for continuous inspection

| Class | Meaning |
|---|---|
| `CAV` | Continuous audiovisual observation by the model: motion, duration, order, synchronization, camera, and editing as perceived in playback |
| `AO` | Auditory observation by the model: vocal delivery, voice quality, breath, music texture, ambience |
| `FRM` | Sampled-frame evidence from the episode bundle |
| `TXT` | Primary-language text: subtitle, transcript, or onscreen text |
| `AM` | Measurement by a deterministic tool: durations, energy, shot boundaries, pitch where reliable |
| `HL` | Human listening or viewing observation |
| `INF` | Source-supported inference |
| `INT` | Interpretation |

Do not collapse these classes. A series that adopts this method may keep its own label vocabulary (for example, audiovisual, performance, and musical fact labels), provided each claim's inspection route remains recoverable.

## 3. What continuous observation can and cannot establish

`CAV` and `AO` can establish:

- the path between two moments: trajectory, hesitation, acceleration, a gaze that moves and returns;
- order and overlap among speech, gesture, cut, and sound;
- approximate durations of holds, pauses, and shots;
- camera movement and transition behavior;
- perceived qualities of delivery and music, as observations with stated confidence.

They cannot by themselves establish:

- exact timing finer than the effective sampling rate or the perception's precision (use `AM`);
- exact wording or lyrics (use `TXT`);
- who is singing in an unmarked ensemble, or which instrument plays, beyond what is clearly audible;
- emotion, intention, or motive;
- that an observed regularity is meaningful rather than conventional.

---

# III. Session preparation

## 4. Source lock

Record the AV object: identity, bytes, hash, duration, resolution, frame rate, audio stream (language, codec, channels), and its relation to the episode bundle and the source episode. Prefer the smallest faithful object that preserves the channels in question (bundle specification Section 8.6).

## 5. Clock calibration

Declare one citation clock, normally the episode bundle's timeline, and cite every observation against it with the nearest cue ID or frame filename.

1. Identify known offsets. Streaming pre-rolls, intro cards, or trimmed derivatives shift timelines. A bundle may exclude a pre-roll from its frames while its complete audio keeps the source timeline; record both values.
2. Align the AV object to the citation clock with anchors, preferring, in order:
   1. verified subtitle or dialogue cues;
   2. distinctive audiovisual events identifiable in both objects, such as a hard cut, a flash, or an impact;
   3. verified audio-event timestamps or waveform features, such as a song's first downbeat or a distinctive sound onset;
   4. frame or shot-index and presentation-time metadata;
   5. other independently documented timing references.

   Use several anchors spread across the object. For a full episode the normal target is three or more, spread across beginning, middle, and end. A short or sparse object (a music video, a concert segment, a clip, an instrumental or nearly wordless sequence) needs enough independent anchors for the precision its claims require; record which anchors were used and the resulting limitation. Few subtitles is a reason to use other anchors, not to accept a weaker alignment.
3. Record the offset, any drift, the anchors used, and the precision achieved.
4. Never cite a timestamp reported by the model without calibration. If no reliable mapping can be established, leave precise cross-object timing claims unresolved, and continue only with claims whose accuracy does not depend on the alignment, such as the order of events within one object or observations located by their content.

### Precision adequate to the claim

| Claim | Precision required |
|---|---|
| Scene or sequence location | Coarse alignment; the default tolerance is ample |
| Relative order of events | Alignment finer than the gap between the events |
| Approximate timing of gesture, speech, or music | The default tolerance, with the timing stated as approximate |
| Subsecond synchronization, such as a cut landing on a beat | Precision finer than the asserted offset, from a route that resolves it: frame-level inspection or measurement |
| Frame-accurate or sample-accurate values | Deterministic measurement (`AM`) on the source, not model perception |

The default tolerance (±0.5 s unless the series sets another) is a baseline for ordinary episode navigation. It never authorizes a finer-grained claim.

## 6. Capability probe and sampling rate

Before analysis, confirm that the session perceives picture and sound together. A short probe works: describe the lip movement and an audible sound onset at a known cue. Record the result in the execution profile.

Record the effective visual sampling rate when it is known, and `UNKNOWN` when it cannot be established. Some AV models sample video at a reduced rate while hearing audio continuously (on some surfaces, around one frame per second by default at the time of writing). Defaults differ by product and change over time; verify the rate rather than assume one.

A session may hold `CONTINUOUS_AV` capability while lacking sufficient visual temporal resolution for a particular claim. Capability verification is necessary but not sufficient for fine-grained visual or synchronization assertions. Therefore:

- do not claim motion or change inside an interval shorter than the effective sampling interval; a fast cut sequence, a flicker of expression, or a smear frame may fall between samples;
- when the rate is `UNKNOWN`, treat sub-second visual claims as unresolved until independently verified;
- for a load-bearing rapid visual event, use a higher-resolution inspection of a targeted clip, frame-level inspection of the bundle or source, or a measurement (`AM`);
- continuous audio does not compensate for missing visual samples: hearing an impact does not show the frame it lands on;
- if no available route resolves the event, the claim stays `OPEN`.

If the session cannot perceive the audio, it is not a `CONTINUOUS_AV` session; record the actual route.

## 7. Coverage plan

State whether the scope is the full object or targeted intervals, and which escalation state applies (`VIDEO_TARGETED_ESCALATION` or `VIDEO_FULL_EPISODE_ESCALATION`). For targeted intervals, include enough surrounding context to interpret them.

---

# IV. Observation discipline

## 8. Observation log before interpretation

Keep a log separate from the interpretation. Each entry records:

```text
obs_id
interval (declared clock)
anchor (cue ID or frame filename)
channel(s)
observation (descriptive)
class (CAV / AO / AM / HL)
confidence (high / medium / low)
re-viewed (yes / no)
```

Describe before naming. Prefer:

> "Loudness and pitch fall across the last three syllables; an audible inhalation precedes the line; her gaze leaves the interlocutor on the second syllable and does not return before the cut."

over:

> "She sounds sad and can't look at him."

## 9. Re-view rule

Inspect every load-bearing observation a second time, on its own interval, in a separate focused pass. Record discrepancies between the passes. An observation that does not survive re-viewing is not evidence.

## 10. Contrast baselines

Interpret delivery and movement relative to:

- the same character elsewhere in the unit;
- the same character with a different interlocutor;
- neighboring lines and shots;
- comparable situations earlier inside the authorized boundary.

Within-character contrast is preferable to generic claims such as "a high pitch means excitement."

## 11. Known AV-model failure modes

Treat these as mandatory checks.

| Failure mode | Check |
|---|---|
| **Event invention**: reporting a line, action, or sound that does not occur | Anchor every observation to a cue or frame; re-view load-bearing observations |
| **Timestamp drift or rounding** | Calibrate the clock (Section 5); cite only calibrated times |
| **Speaker or singer misattribution** | Use subtitle speaker fields, visible lip movement, and voice contrast; leave ensemble vocals unattributed when uncertain |
| **Transcription standing in for text** | A listening transcription is never `TXT`. Use the primary-language layer; flag suspected divergence |
| **Affect over-reading** | Describe delivery; label any inner-state claim `INF` or `INT` |
| **Smoothing**: merging shots, skipping brief events | Check dense intervals against the bundle's shot index; re-view at the interval |
| **Sampling blindness**: missing sub-interval events | Respect the effective sampling rate (Section 6) |
| **Prior contamination** | Apply the quarantine (Section 1); record intrusions |

---

# V. Analytical passes

Use only the passes the unit earns. The pass order is a working order, not a required document structure.

## 12. Pass 1: uninterrupted structural viewing

View the scope through once without stopping for detail. Divide it into dramatic movements with time ranges (generic anime method Section 7). Note pacing, density, and where the unit seems to place its weight. Make no load-bearing claims in this pass.

## 13. Pass 2: editing and rhythm

Track cut density by movement (count from the shot index; perceive rhythm in playback), holds, withheld or delayed reaction shots, cross-cutting, montage, match cuts, and transitions such as dissolves and wipes. Ask:

> What relation does the edit create, and when does it arrive relative to dialogue and music?

## 14. Pass 3: camera and space

Track pans, tilts, tracking, zooms, and focus changes; how blocking changes within a shot; movement through space; and, in action, the geography that makes choreography legible or deliberately illegible.

## 15. Pass 4: bodily and facial performance over time

Track gesture trajectories, gaze paths, onset delays, hesitations, approach and withdrawal, and incongruence between words and body.

Distinguish **production convention** from **performance choice**. Held cels, limited animation, reused cuts, bank sequences, and shared OP/ED footage are economies of production; a held frame is not by itself a character's hesitation. Claim performance meaning only where the animation actually varies, or where convention is broken.

## 16. Pass 5: vocal performance

Track, as `AO` with confidence: prosodic contour, rate, intensity, breath, voice quality (creak, tremor, falsetto, strain), laughter, crying coloration, overlap, and perceived response latency (exact latency is `AM`). Track register shifts across interlocutors. Build each character's baseline before interpreting departures from it.

## 17. Pass 6: dialogue–performance synchronization

Track the timing relations between speech and face or gesture: pauses filled by action, reactions that precede or lag the line, offscreen lines, and silences in which the picture carries the scene.

## 18. Pass 7: music dramaturgy

Screen each musical event for significance before analyzing it:

- **M0 incidental**: present but yields no material evidence;
- **M1 supportive**: reinforces an already-established state; compact notation;
- **M2 diagnostic**: musical or performance form supplies important evidence; full entry;
- **M3 state-changing**: the musical event produces, demonstrates, legitimizes, or transforms a state; full entry plus longitudinal updates.

For M2 and M3 events, track:

- cue entry and exit relative to cuts, gestures, and lines;
- diegetic, nondiegetic, or ambiguous status, and any shift between them;
- development within the cue (density, instrumentation, and dynamics as heard, at stated confidence);
- for songs, internal segmentation at audible and visible transitions;
- lyric allocation from the text layer, checked against visible performance;
- audience and witness configuration.

Required question:

> What does the musical event accomplish that ordinary dialogue could not?

If the answer is "nothing", say so.

## 19. Pass 8: sound–image relations

Track silence and near-silence, ambience, offscreen sound, sound bridges across cuts, effects, counterpoint between sound and picture, and changes in mix prominence. Silence is not automatically hesitation, sadness, or shock (generic anime method Section 21).

## 20. Pass 9: what the continuous form contributes

Close the analysis by stating what the continuous evidence established that a reading from text and sampled frames could not, and which of those findings change the interpretation rather than decorate it. If continuous inspection added nothing material, say so; that is a valid result.

---

# VI. Claim discipline

## 21. Path claims and their resolution

Continuous inspection can establish the path between endpoints that sampled frames cannot (bundle specification Section 8.7), but only at the resolution actually perceived. A path claim records its interval and the effective sampling rate. With an `UNKNOWN` rate, a sub-second path claim is unresolved until verified (Section 6).

## 22. Corroboration

Corroborate these claims through a second channel or a measurement before treating them as load-bearing:

- attribution of an unmarked voice;
- precise synchronization claims (for example, "the cut lands on the downbeat");
- exact durations;
- claims that a performance choice departs from production convention.

## 23. Lane boundaries

Exact wording and lyrics come from `TXT`. Exact durations come from `AM`. Performer identity is excluded. Emotion and intention remain `INF` or `INT`. When continuous evidence contradicts the text layer, record the divergence; do not silently prefer either.

---

# VII. Output

## 24. Independent AV reading structure

When the method is used for an independent reading, the output covers, as relevant:

- **A. Governing AV thesis**: what the unit's audiovisual form does.
- **B. Session profile and coverage**: lane, AV object, clock calibration, effective sampling rate, coverage and inspection states.
- **C. Dramatic movements**, with time ranges.
- **D. Editing, camera, and space.**
- **E. Bodily, facial, and vocal performance.**
- **F. Music and sound dramaturgy.**
- **G. Synchronization findings.**
- **H. What the continuous form contributes** (Section 20).
- **I. Counterevidence and alternative readings.** Mandatory, including production-convention alternatives.
- **J. Open questions.**
- **K. Observation log**, as an appendix.
- **L. Claim ledger** (Part VIII).

When the method serves as Stage 2 of the reconciliation protocol, produce that protocol's AV review artifact instead.

---

# VIII. Claim ledger

Extend the generic anime method's claim ledger with the fields continuous inspection needs:

```text
Claim ID
Claim
Observation IDs
Interval (declared clock) and anchor
Evidence class (CAV / AO / AM / FRM / TXT / HL / INF / INT)
Effective sampling rate (for path and timing claims)
Inference level
Confidence
Counterevidence and production-convention alternative
Status
```

---

# IX. Blind-analysis mode

## 25. Identity minimization

Apply the generic anime method's Sections 30–31. Continuous media leak identity in ways filenames do not:

- trim title cards, OP/ED sequences, previews, and credits from the AV object when they are not under analysis;
- instruct the analyst not to identify performers or music by recognition;
- accept that spoken names cannot be removed from audio; record when the analyst recognized the work, and what it recalled.

## 26. Modality-ablation extension

The generic anime method's Section 32 defines Passes A–D (text; text and visuals; plus measurements; plus auditory observation). Add:

### Pass E: continuous AV

Synchronized video and audio, under this method.

### Pass F: reconciled

A Pass B or C reading tested and integrated under the reconciliation protocol.

For each added condition, record new claims enabled, claims revised, confidence changes, contradictions introduced, false claims (checked against measurement or human review), unresolved claims closed, and unresolved claims correctly preserved.

The benchmark should measure **epistemic improvement**, not descriptive volume. A continuous pass that produces more adjectives but no better-supported claims has not improved the reading.

---

# X. Governing rules

1. **Calibrate the clock before citing time.**
2. **Observation precedes interpretation, and is logged separately.**
3. **A load-bearing observation is re-viewed before it is used.**
4. **Perceiving delivery is not perceiving an inner state.**
5. **Listening transcription is not source text.**
6. **A held frame is not automatically a character's hesitation.**
7. **Do not identify performers by ear.**
8. **A path claim is bounded by the resolution actually perceived.**
9. **Musical presence is not automatically musical meaning.**
10. **Report what continuous inspection did not change, as well as what it did.**
11. **Counterevidence belongs inside the analysis.**
12. **Every interpretive claim should remain traceable to a calibrated interval.**

---

# Repository context

These references establish integration boundaries; this method does not duplicate or replace them.

- [Medium and inspection-lane routing policy](../source-policies/MANGA_ANIME_MEDIUM_AND_INSPECTION_LANE_ROUTING_POLICY.md): lanes, lane claim permissions, and series adoption.
- [Audiovisual reconciliation protocol](../source-policies/MANGA_ANIME_AUDIOVISUAL_RECONCILIATION_PROTOCOL.md): the bundle-mediated to continuous-AV relay.
- [Generic anime episode method](GENERIC_ANIME_EPISODE_ANALYTICAL_METHOD.md): the companion reference for dramatic, character, relationship, and thematic responsibilities.
- [Anime episode-bundle specification](../source-policies/MANGA_ANIME_EPISODE_BUNDLE_SPECIFICATION.md): the citation coordinate system, partial derivatives, and video-escalation states.
- [Execution topology and capability-routing policy](../source-policies/MANGA_ANIME_EXECUTION_TOPOLOGY_AND_CAPABILITY_ROUTING_POLICY.md): capability verification and inspection provenance.
- [Project initiation and architecture policy](../source-policies/MANGA_ANIME_PROJECT_INITIATION_AND_ARCHITECTURE_POLICY.md): project-local method and architecture requirements.
- [Change-integration checklist](../policies/CHANGE_INTEGRATION_CHECKLIST.md): authorized paths, validation, and publication.
