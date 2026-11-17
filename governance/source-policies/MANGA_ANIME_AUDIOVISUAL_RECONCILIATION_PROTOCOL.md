---
title: Manga / Anime Audiovisual Reconciliation Protocol
artifact_id: MANGA_ANIME_AUDIOVISUAL_RECONCILIATION_PROTOCOL
artifact_type: audiovisual_reconciliation_protocol
version: "1.0"
status: canonical
scope: staged relay between bundle-mediated analysis and continuous audiovisual review, and integration of the result
created: 2026-10-24
maintainer: Claude + user
do_not_use_as_current_authority: false
do_not_use_as_literary_evidence: true
canonical_home: governance/source-policies/MANGA_ANIME_AUDIOVISUAL_RECONCILIATION_PROTOCOL.md
drafted_against_commit: 6a3afaaf1bb61e0993db379ab4074c46e9ea98dd
supersedes: null
superseded_by: null
---

# Manga / Anime Audiovisual Reconciliation Protocol

> **The bundle-mediated reading proposes. Continuous audiovisual review tests what it can perceive. The reading's author integrates. No lane overrules evidence on a channel it cannot inspect, and no disagreement is resolved by deference to a model.**

This protocol is a specialization of the [analytical handoff contract](MANGA_ANIME_ANALYTICAL_HANDOFF_AND_INTEGRATION_CONTRACT.md) for one recurring relay: a `BUNDLE_MEDIATED` reading, a `CONTINUOUS_AV` review, and integration by the reading's author. Lanes and their claim permissions are defined in the [medium and inspection-lane routing policy](MANGA_ANIME_MEDIUM_AND_INSPECTION_LANE_ROUTING_POLICY.md). Everything in the handoff contract still applies; this file adds only what the relay needs.

## 1. When to use it

Use this protocol when:

- a series' reconciliation profile routes a claim class through continuous AV review (lane policy Section 6); or
- a reading records `VIDEO_TARGETED_ESCALATION` or `VIDEO_FULL_EPISODE_ESCALATION` for a material claim, and a session with verified `continuous_av_inspection` is available.

It is proportional. A series need not reconcile every episode. Batch by episode or by tranche, as the reconciliation profile states.

**Mirror route.** For AV-primary sources (concerts, music videos, AV-first character studies), the order may be reversed: the `CONTINUOUS_AV` session authors and the `BUNDLE_MEDIATED` or `TEXT` session verifies wording, locators, and text-layer claims. Apply the same rules with the roles exchanged.

## 2. Roles and ownership

| Stage | Role | Lane | Owns |
|---|---|---|---|
| 1 | Reading author | `BUNDLE_MEDIATED` | The deep reading and its AV verification queue |
| 2 | AV reviewer | `CONTINUOUS_AV` | An AV review artifact: observation log, adjudications, new findings |
| 3 | Integrator, normally the reading author | `BUNDLE_MEDIATED` | The integrated reading, ledger updates, and the reconciliation summary |

One mutable owner per artifact (topology Section 9). The AV reviewer does not edit the deep reading or any ledger. It writes its own review artifact, which the integrator consumes.

## 3. Stage 1: the reading and its verification queue

The reading author completes the reading under the series method. Then it prepares:

**(a) The AV verification queue**, in two parts. Each queue entry asks for an observation; it does not ask for agreement.

The **observation packet** is what the reviewer receives first:

| Field | Content |
|---|---|
| `queue_id` | Stable ID, for example `Q-S01E24-07` |
| `question` | A neutral question the reviewer can answer by looking and listening, for example "Does the character's gaze move to the speaker before or after the line ends?" It must not name the expected answer or the interpretation under test |
| `channel` | Motion, camera, editing, delivery, music, sound–image, synchronization |
| `interval` | Start and end in the bundle's declared clock, with the nearest cue ID or frame filename |
| `escalation_state` | `VIDEO_TARGETED_ESCALATION` or `VIDEO_FULL_EPISODE_ESCALATION` |
| `requirement` | `REQUIRED` or `OPTIONAL` (handoff Section 6) |

The **adjudication packet** is withheld until the reviewer's observation log is frozen (Section 4.2):

| Field | Content |
|---|---|
| `queue_id` | Matches the observation packet |
| `claim_ref` | Claim ID or stable locator of the claim under test |
| `claim` | The claim as formulated in the reading |
| `would_disconfirm` | The observation that would weaken the claim |
| `reading_sections` | The reading sections the reviewer should consult when adjudicating |

**(b) The AV object and clock reference.** Identify the continuous object (source episode or derivative): bytes, hash, duration, video and audio stream identity, and its relation to the bundle. Record the bundle's timing reference, including any pre-roll offset. In a bundle whose frames start at the program start while its audio keeps the source timeline, both offsets are needed to cite one moment consistently. Prefer objects within the bundle specification's transport guidance (Section 8.6).

**(c) A packet** under the handoff contract and its [stage template](templates/MANGA_ANIME_ANALYTICAL_STAGE_HANDOFF_TEMPLATE.md), with `stage_state: READY_FOR_HANDOFF`. Its body carries the observation packet, the AV object identity, the clock reference, and necessary technical context. Deliver the adjudication packet and the reading only after the reviewer reports the log frozen, or as a separate file the reviewer opens only then.

## 4. Stage 2: continuous AV review

The reviewer follows the [generic continuous-AV method](../analytical-methods/GENERIC_CONTINUOUS_AUDIOVISUAL_ANALYTICAL_METHOD.md), or the series' AV companion method when one exists.

### 4.1 Capability and clock calibration

Before any observation:

1. Verify `continuous_av_inspection` on the supplied object. Record the effective visual sampling rate, or `UNKNOWN` when it cannot be established. Capability is necessary but not sufficient for fine-grained visual or synchronization claims (generic continuous-AV method, Section 6).
2. Calibrate the AV object against the bundle clock using the anchor hierarchy of the generic continuous-AV method (Section 5): verified subtitle or dialogue cues first, then distinctive audiovisual events, verified audio events or waveform features, frame or shot-index and presentation-time metadata, and other documented timing references. For a full episode the normal target is three or more anchors spread across beginning, middle, and end. A short or sparse object (a concert segment, a music video, a clip, an instrumental or nearly wordless sequence) needs enough independent anchors for the precision its queued questions require. Record the anchors used, the offset, any drift, and the precision achieved.
3. The default tolerance (±0.5 s unless the series sets another) is a baseline for ordinary episode navigation. It never authorizes a finer-grained claim; precision must be adequate to each claim (generic continuous-AV method, Section 5).
4. If no reliable mapping can be established, do not lower the standard. Mark the queue items whose answers depend on cross-object timing `BLOCKED`, and continue only with items whose answers do not depend on the alignment. Uncalibrated timestamps must not be cited.

### 4.2 Blind-first observation

To limit anchoring, the reviewer works in this order:

1. **Independent pass.** View the assigned scope (the full episode, or the queued intervals with their surrounding context) and write an observation log under the generic AV method, using only the observation packet.
2. **Queue pass.** Answer each neutral `question`, adding targeted observations. The adjudication packet is still unopened.
3. **Freeze the log.** Mark the observation log complete. Later entries are allowed but must be marked as made after reading the claims.
4. **Adjudication.** Only now open the adjudication packet: the claims under review, their disconfirmation criteria, and the relevant reading sections.

If the reviewer saw the adjudication packet, the reading, or claim formulations before freezing the log, whether through platform limits or packet error, record `blind_order_achieved: false` and what was seen. Do not claim independence.

### 4.3 Adjudication

For each queued claim, record one transition from the archive vocabulary:

| Field | Content |
|---|---|
| `queue_id`, `claim_ref` | From the queue |
| `transition` | `PRESERVE`, `STRENGTHEN`, `REVISE`, `DOWNGRADE`, `REJECT`, or `OPEN` |
| `observation_ids` | Entries in the observation log that support the transition |
| `observation_status` | `REPORTED`, or `ANCHORED` when every supporting observation is tied to a calibrated interval and a cue or frame, was re-viewed, lies within the effective sampling resolution, and has any corroboration the AV method requires (generic continuous-AV method, Sections 9 and 21–22) |
| `interval` | Calibrated interval actually inspected |
| `inspection_route` | Continuous AV, auditory observation, or measurement |
| `proposed_formulation` | For `REVISE` and `DOWNGRADE`: the bounded statement the evidence supports |
| `alternative_explanation` | Including production convention (held cels, reused cuts, limited animation) where relevant |
| `confidence` | High, medium, or low, with the reason |

Report every transition, including `PRESERVE`. A review that reports only disagreements hides how much of the reading survived.

### 4.4 New findings

Record observations the queue did not ask about, but that bear on the reading, in a separate **new findings** table: observation IDs, interval, channel, the observation, and the claim it would support or pressure. New findings are proposals to the integrator. They are not transitions on existing claims.

### 4.5 What the reviewer does not do

- Rewrite the reading's prose or its interpretations outside the queued channels.
- Override primary-language wording. Record `SUBTITLE_DIVERGENCE_SUSPECTED` with the interval when the audio appears to differ from the text layer; the text lane verifies it.
- Transcribe lyrics or dialogue as authoritative text.
- Attribute a singer or speaker by recognizing a voice actor.
- Convert perceived delivery into a statement about inner state.

### 4.6 Output

The AV review artifact contains:

- the session's execution profile, clock calibration, and effective sampling rate;
- a coverage statement per channel and interval, using the handoff contract's requirement and inspection states;
- the frozen observation log;
- the adjudication table;
- the new findings table;
- subtitle-divergence flags;
- `stage_state: READY_FOR_HANDOFF`.

## 5. Stage 3: integration

The integrator first performs receiver acceptance (handoff Section 9). Then:

### 5.1 The asymmetry rule

> **An observation on an otherwise inaccessible evidence channel is entitled to serious, source-grounded consideration, not automatic truth. The integrator may not dismiss it without evidence, but a load-bearing disputed observation can remain provisional pending targeted verification. No model's perceptual report has categorical authority over the underlying source.**

A model's observation log is an evidentiary report, not the source itself. Weigh each AV observation by its status:

| Status | Meaning | Use in integration |
|---|---|---|
| Reported | Recorded in the reviewer's log | Weighed with its stated confidence; may support claims that do not bear load |
| Anchored | `ANCHORED` under Section 4.3 | May support load-bearing claims |
| Disputed | Load-bearing and under a contradiction or verification request | Provisional: neither accepted into mainline authority nor rejected until resolved (Section 5.2) |
| Interpretation | A reading built on observations | Argued by either analyst on ordinary evidential grounds; the reviewer's interpretive remarks carry no special authority |

The integrator, who cannot inspect the channel, may respond to a load-bearing observation in two different ways.

**Contradiction.** A claim that the observation is wrong. It requires evidence the integrator can inspect:

1. a locator or clock failure, such as an interval that does not match the cited cue or frame;
2. internal inconsistency within the AV review;
3. conflict with the primary-language text layer or with bundle frames at the cited time;
4. a claim outside the `CONTINUOUS_AV` lane's permissions.

**Verification request.** A concrete reliability concern that the integrator cannot settle from text or frames. Recognized grounds:

- the observation bears load but lacks adequate source anchoring;
- the effective temporal resolution is unknown or inadequate for the claim;
- speaker or singer attribution is uncertain;
- shots or scenes appear to be conflated;
- the observation is inconsistent with independently available timing or media metadata, such as the shot index, cue timing, or durations;
- a consequential claim lacks the corroboration the AV method requires;
- independent audiovisual observers materially disagree.

A verification request is not a contradiction: it makes the observation disputed, not rejected. Preference, prior confidence, and the coherence of the existing reading are grounds for neither. Observations that bear no load are taken as reported, without verification.

### 5.2 Contest, return, and verification

A contradiction or verification request returns the item to the reviewer once, with a specific question and its grounds. The reviewer re-inspects the interval or explains why it cannot. If that round settles the item, apply the result.

If a material, load-bearing observation is still unsettled after that round, the integrator may route it once to independent verification: a second `CONTINUOUS_AV` session working blind from the observation packet, a higher-resolution inspection of a targeted clip, a deterministic measurement, or human viewing. Weigh the result under Section 5.1. Agreement between independent routes anchors the observation. Continued disagreement leaves the item `OPEN`, with every evidence route recorded.

Do not iterate further. `OPEN` is a valid outcome. Until resolved, the observation and the claims resting on it stay provisional, recorded as disputed rather than accepted or rejected. Never settle a dispute by authorship, model, or provider prestige.

### 5.3 Write-through

- Apply accepted transitions to the reading, preserving earlier formulations as the series' claim-revision system requires.
- Route accepted findings to the cumulative homes named in the series architecture, such as voice, performance, or musical-dramaturgy ledgers.
- For a frozen reading or checkpoint, record an erratum or claim revision. Never edit the frozen bytes.
- Send subtitle-divergence flags to whoever maintains the text layer, and resolve them before relying on the affected wording.

### 5.4 Reconciliation summary

Add a compact record to the reading, or to the series' execution record:

```yaml
av_reconciliation:
  route: BUNDLE_MEDIATED -> CONTINUOUS_AV -> BUNDLE_MEDIATED
  av_object: "<identity and hash>"
  clock_offset_seconds: 0.0
  calibration_anchors: "<kinds and count of anchors used>"
  alignment_precision_seconds: 0.5
  effective_visual_sampling: "<rate, or UNKNOWN>"
  blind_order_achieved: true
  queue_items: 0
  transitions: {PRESERVE: 0, STRENGTHEN: 0, REVISE: 0, DOWNGRADE: 0, REJECT: 0, OPEN: 0}
  new_findings_accepted: 0
  contested_items: []
  verification_routes: []
  provisional_observations: []
  open_disputes: []
  required_items_unresolved: []
```

Report the full distribution of transitions. Do not report only the changes that improved the reading.

## 6. Failure handling

| Condition | Result |
|---|---|
| The AV object cannot be retrieved, decoded, or perceived with audio | Inspection state `UNAVAILABLE`. Queue stays open. No completion claim for `REQUIRED` items |
| Clock calibration fails | Queue items that depend on cross-object timing are `BLOCKED`; fix the object or the clock reference, or find other anchors. Items that do not depend on the alignment may proceed |
| A load-bearing visual event is shorter than the effective sampling interval, or the rate is `UNKNOWN` | The claim stays `OPEN` until a higher-resolution inspection or a measurement resolves it |
| Independent verification is unavailable for a disputed observation | The observation stays provisional and the item `OPEN` |
| Only part of the scope was reviewed | Inspection state `PARTIAL`, with the remaining intervals listed |
| The reviewer read the claims before observing | Record that the blind order was not achieved. The adjudications stand, with that disclosure |
| Required items remain unresolved | The corresponding completion claim stays blocked (handoff Section 6) |

## 7. Evaluation

Topology Section 12 evaluates arrangements by accepted analytical quality, missing-evidence rate, transfer defects, and rework. For this relay, also track the share of queued claims revised or rejected, the share of new findings accepted, contested items, and items left `OPEN`. The generic continuous-AV method's ablation extension (Section IX) can compare reconciled and unreconciled readings of the same episode.

## Changelog

### v1.0 - 2026-10-24 - Initial protocol

Defines the bundle-mediated to continuous-AV to integration relay: a neutral verification queue, clock calibration, blind-first review, transitions from the archive vocabulary, a grounded-contest asymmetry rule, one bounded return round, and a reconciliation summary.
