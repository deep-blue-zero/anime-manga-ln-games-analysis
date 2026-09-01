---
title: "IDOLY PRIDE V2 Audiovisual Selection, Voice, Music, and Dramaturgy Protocol"
project: "IDOLY PRIDE"
document_id: "IDOLY_PRIDE_V2_AUDIOVISUAL_SELECTION_VOICE_MUSIC_DRAMATURGY_PROTOCOL"
version: "1.0"
status: "governing-framework"
created: "2026-08-13"
related_frameworks:
  - "IDOLY_PRIDE_V2_ANALYTICAL_METHOD"
  - "IDOLY_PRIDE_V2_SOURCE_EVIDENCE_AND_LEDGER_PROTOCOL"
  - "IDOLY_PRIDE_V2_ANIME_AND_CROSS_MEDIA_SEQUENCING_PROTOCOL"
scope:
  - "voice acting"
  - "music"
  - "songs and lyrics"
  - "3DMVs and live sequences"
  - "card/scene visuals"
  - "telephone audio"
---

# IDOLY PRIDE V2 AUDIOVISUAL SELECTION, VOICE, MUSIC, AND DRAMATURGY PROTOCOL

## 1. Purpose

The game contains far more voiced, musical, and visual material than can be efficiently uploaded or reviewed exhaustively.

This protocol defines how V2 selects audiovisual artifacts for close analysis without reducing the franchise to transcripts and without building an impractically complete video archive.

The governing workflow is:

> **text discovers questions → ledgers identify formal blind spots → audiovisual artifacts are selectively escalated → audiovisual findings return to the ledgers and synthesis**

The major exception is the bounded twelve-episode anime, which receives comprehensive prospective review under the separate anime sequencing protocol.

For game material, audiovisual ingestion is targeted.

---

# 2. Why transcript completeness is not analytical completeness

The extracted Japanese corpus is exceptionally valuable, but several major evidence classes disappear in transcription:

- pitch;
- vocal placement;
- timbre;
- breath;
- rhythm;
- hesitation;
- sarcasm;
- deadpan timing;
- emotional strain;
- softness;
- laughter;
- crying;
- overlapping speech;
- silence;
- score entrance;
- harmonic and melodic motion;
- orchestration;
- vocal blend;
- choreography;
- stage blocking;
- editing;
- lighting;
- audience framing;
- costume;
- body language.

Therefore:

> **A complete transcript corpus is not a complete performance corpus.**

At the same time, exhaustive audiovisual ingestion would create enormous cost with rapidly diminishing returns.

Selection must therefore be claim-driven.

---

# 3. Five kinds of voice

V2 should distinguish five related but non-identical forms of character voice.

## 3.1 Linguistic voice

Available primarily from transcripts.

Includes:

- vocabulary;
- pronouns;
- sentence endings;
- politeness;
- syntax;
- dialect;
- forms of address;
- repeated expressions;
- message-text style.

## 3.2 Performed voice

Requires audio.

Includes:

- pitch range;
- timbre;
- speed;
- breath;
- vocal weight;
- attack;
- softness;
- hesitation;
- laughter;
- deadpan delivery;
- emotional leakage;
- stylization.

## 3.3 Relational/social voice

Requires comparison across interaction partners.

Ask how the same character sounds with:

- unit peers;
- manager;
- family;
- rivals;
- juniors/seniors;
- fans;
- emotionally important individuals.

A relational register change may exist even when the lexical wording remains similar.

## 3.4 Embodied voice

Requires video/animation.

This is the relation among:

- speech;
- posture;
- facial expression;
- gesture;
- physical distance;
- eye line;
- movement.

## 3.5 Stage voice

Requires music/performance evidence.

Includes:

- singing timbre;
- blend;
- projection;
- line allocation;
- solo/ensemble contrast;
- MC voice;
- stage persona;
- audience address.

Do not infer one category automatically from another.

---

# 4. Audiovisual priority classes

Every potential artifact may receive an `AV_PRIORITY`.

## AV-A — MANDATORY

Review in full or near-full.

Typical cases:

- complete anime under the anime protocol;
- story-defining performances;
- songs inseparable from major character or unit transformation;
- scenes where delivery is itself central to the claim;
- major formal evidence that cannot be reconstructed from text.

## AV-B — TARGETED

Review the relevant scene/song/performance section.

Typical cases:

- relationship turning points;
- important confrontations;
- emotional register anomalies;
- selected card scenes;
- major unit lives;
- signature songs/MVs;
- scenes where transcript ambiguity matters.

## AV-C — REPRESENTATIVE SAMPLE

Use a small sample to establish a stable baseline.

Typical cases:

- ordinary speaking voice;
- comedy;
- embarrassment;
- public-facing persona;
- casual unit interaction;
- recurring relationship register.

## AV-D — TEXT SUFFICIENT

No audiovisual review is required unless later analysis creates a formal question.

Typical cases:

- routine voiced scenes whose contribution is fully recoverable from text;
- material redundant with already established voice/performance patterns;
- low-value variations that do not affect any claim.

AV priority is independent of textual source priority.

A FOUNDATIONAL text scene may still be AV-D if nothing important depends on performance form.

A minor card may become AV-B if a subtle delivery shift carries major relational meaning.

---

# 5. Audiovisual escalation triggers

A ledger entry should be escalated when one or more of the following applies.

## 5.1 Emotional-delivery ambiguity

The transcript cannot reliably distinguish:

- sincerity;
- teasing;
- sarcasm;
- false brightness;
- suppression;
- embarrassment;
- resignation;
- anger;
- grief;
- tenderness.

## 5.2 Relationship-register hypothesis

A claim depends on a character sounding systematically different with a specific person.

## 5.3 Turning-point significance

The source alters a stable character, relationship, unit, or professional state.

## 5.4 Baseline violation

A character who normally has one vocal pattern suddenly departs from it.

## 5.5 Formal dependence

Meaning depends on:

- music;
- choreography;
- blocking;
- camera;
- editing;
- lighting;
- costume;
- audience relation.

## 5.6 Textual conflict

Two textually similar scenes may have different performed meanings.

## 5.7 Claim uncertainty

A high-impact interpretation remains uncertain because performance evidence is missing.

## 5.8 Repeated motif

A visual, musical, or vocal motif appears to recur and may support a longitudinal claim.

---

# 6. AV review queue

Maintain:

`IDOLY_PRIDE_V2_AV_REVIEW_QUEUE.md`

Recommended entry:

```yaml
av_queue_id:
source_id:
artifact_type:
characters:
units:
claim_ids:
av_priority:
escalation_reason:
requested_artifact:
minimum_required_segment:
expected_question:
status:
reviewed_on:
result:
resulting_claim_revision:
```

`requested_artifact` should be as specific as possible.

Examples:

- full scene video;
- audio only;
- 45-second confrontation clip;
- complete song audio;
- lyrics + audio;
- 3DMV;
- card image;
- performance clip;
- telephone call.

The queue should avoid requesting a 20-minute video when 70 seconds answer the analytical question.

---

# 7. Character voice sampling strategy

Game voice analysis should use **representative sampling**, not coverage percentages.

For a major character, a useful initial sample usually includes some subset of:

1. ordinary neutral conversation;
2. emotionally stressed or vulnerable scene;
3. comedy/embarrassment;
4. interaction with a major relationship partner;
5. public/professional speech;
6. stage/performance voice.

Three to five strategically different samples may establish a good baseline.

Additional clips are added when later ledger findings create a reason.

The analytical target is:

> **stable vocal envelope + relationship-specific variation + meaningful departures from baseline**

not:

> "X percent of all voiced lines have been listened to."

---

# 8. Vocal-analysis record

For reviewed clips, record only observable or defensible features.

Possible fields:

```yaml
pitch_tendency:
tempo:
rhythmic_character:
timbre:
breathiness:
vocal_weight:
articulation:
sentence_final_delivery:
pause_pattern:
laughter:
emotional_leakage:
public_private_difference:
partner_specific_shift:
confidence:
```

Do not pseudo-measure acoustic features without actual measurement.

Qualitative descriptions should be comparative and source-grounded.

---

# 9. Music selection: dramaturgical priority

Songs should not be selected merely by:

- popularity;
- release date;
- chart status;
- personal preference;
- whether every unit has an equal number.

The main criterion is:

> **What narrative or character work does this song perform?**

For each major unit, begin by identifying up to three anchor roles.

## 9.1 Identity song

Best establishes the unit's performance proposition.

Question:

> What does this unit sound like when it most clearly states who it is?

## 9.2 Development/crisis song

Connected to meaningful narrative transformation, defeat, confrontation, re-founding, grief, or change.

Question:

> What changed in the unit such that this song can exist here?

## 9.3 Mature-state song

Best represents the later/mature form of the unit.

Question:

> What does the unit become after its major development?

One song may fill multiple roles.

Do not force exactly three songs when two explain the unit better.

---

# 10. Character-specific mandatory songs

Some songs deserve review even if they do not fit a unit-level sampling scheme.

Escalate when a song functions as:

- memorialization;
- confession;
- grief work;
- rivalry;
- apology;
- relationship statement;
- inheritance;
- professional proof;
- self-definition;
- survival;
- public reclamation;
- farewell;
- re-founding.

For such songs, the musical form may be part of the character argument.

---

# 11. Song analysis dimensions

A full musical/dramaturgical review may consider:

## Composition

- melodic contour;
- tonal/harmonic tension and release;
- cadence;
- refrain structure;
- key changes where relevant;
- build and release;
- repetition;
- contrast.

## Rhythm

- tempo;
- meter;
- rhythmic drive;
- syncopation;
- half-time/double-time feel;
- density changes.

## Arrangement

- instrumentation;
- texture;
- orchestration;
- electronic/acoustic balance;
- dynamic build;
- breakdown;
- transition;
- final-chorus expansion.

## Vocal writing

- solo allocation;
- duet/group distribution;
- call-and-response;
- harmony;
- unison;
- member contrast;
- vocal blend;
- climactic line assignment.

## Lyrics

- recurring terms;
- pronouns;
- temporal language;
- audience address;
- memory language;
- relational grammar;
- unit philosophy.

## Dramaturgy

- where the song occurs;
- what precedes it;
- what follows it;
- who hears it;
- whether it is diegetic;
- what unresolved tension it converts into performance;
- whether the song answers an earlier song or motif.

The essential question is:

> **Why does this song belong at this point in these characters' lives?**

---

# 12. Song versus MV

A song selected for musical analysis does **not** automatically require its 3DMV.

Review the MV when staging adds evidence that audio/lyrics cannot provide.

MV escalation triggers include:

- center distribution matters;
- choreography encodes relationships;
- member geometry changes;
- costume changes meaning;
- camera privileges or destabilizes a member;
- audience framing matters;
- repeated visual motifs appear;
- lyrics and staging create tension;
- later performances revise an earlier visual arrangement.

Otherwise, audio + lyrics may be sufficient.

---

# 13. Live/performance analysis

For selected live sequences, record:

- opening formation;
- center;
- member spacing;
- movement of center;
- solo/ensemble transitions;
- choreography motifs;
- gesture;
- audience shots;
- camera movement;
- lighting;
- costume;
- synchronization;
- final pose;
- relationship to lyrical climax.

A performance should not be reduced to "good choreography."

Ask what the performance argues about the unit.

---

# 14. Card and story-scene video

Do not upload every voiced card or event.

Escalate card/story video when:

- facial/body acting matters;
- delivery changes the interpretation;
- a recurring visual object becomes important;
- the scene is a relationship turning point;
- silence/pause is meaningful;
- the scene is difficult to classify from text;
- it supplies a rare relational vocal sample.

If only the illustration matters, upload the image rather than the whole sequence.

---

# 15. Telephone calls

Telephone audio is unusually useful for voice because the visual layer is minimized.

Use it for:

- intimacy;
- conversational rhythm;
- directness;
- hesitation;
- manager-specific register;
- affect without stage acting.

However, ASR remains provisional.

For subtle linguistic claims, verify the audio directly.

---

# 16. Evidence separation

A synthesis claim may combine several evidence streams, but the ledger should preserve them separately.

Example:

```text
TXT-MIHO-041
Text establishes what miho says.

VOICE-MIHO-012
Audio establishes unusually soft delivery.

VIS-MIHO-007
Card/scene visual foregrounds the black hair.

MUS-MIHO-004
Song transforms private remembrance into public performance.
```

The final prose may synthesize these into one argument.

The evidence index should not collapse them into a single undifferentiated citation.

---

# 17. Diminishing returns rule

Once a stable pattern has been established, additional audiovisual artifacts require a reason.

Examples:

- fifth ordinary miho scene that reproduces the same vocal baseline → likely AV-D;
- new miho scene with Yō-related material and altered delivery → likely AV-B;
- another generic unit live with unchanged staging → likely AV-D/C;
- new performance that redistributes center or revises a unit's signature song → AV-B/A.

This is how V2 maintains high audiovisual rigor without uncontrolled ingestion.

---

# 18. Cross-media feedback loop

Audiovisual review must return findings to the analytical corpus.

Possible outcomes:

- confirms text-derived claim;
- strengthens it;
- qualifies it;
- recontextualizes it;
- reveals a new relational register;
- reveals a new formal motif;
- rejects a transcript-based assumption;
- creates a new open question.

The AV review queue is not a separate side project.

It is part of the claim-revision system.

---

# 19. Priority examples

## Mandatory or near-mandatory

- complete anime;
- songs directly attached to major grief/inheritance arcs;
- unit-defining or re-founding performances;
- major scenes where delivery is the interpretive question.

## High-value targeted

- miho/Yō-related voiced material;
- IIIX re-founding or hostile-intimacy scenes;
- Kotono/Nagisa or Mana/Kotono turning points;
- Sakura/Mana inheritance material;
- Makino scenes whose ethical/relational reading depends on tone;
- major rival confrontations;
- later unit performances that revise earlier identity.

These are examples of routing logic, not a permanent hard-coded canon of AV importance.

The V2 ledger may reprioritize them.

---

# 20. Relationship to live-service updates

When new game material arrives:

1. ingest text first where available;
2. classify semantic impact;
3. update ledgers;
4. ask whether the source creates an audiovisual blind spot;
5. add only necessary artifacts to the AV review queue;
6. retest affected claims.

A new event does not automatically require its entire video.

A Class-3 narrative update may nevertheless generate multiple AV-A/B artifacts if performance form becomes architecturally important.

---

# 21. Minimum audiovisual archival outputs

The final analytical release should preserve:

- `IDOLY_PRIDE_V2_AV_REVIEW_QUEUE.md`;
- an `AUDIOVISUAL_EVIDENCE_INDEX.md`;
- selected clip/song/MV locators;
- reviewed-artifact metadata;
- claim routing;
- known audiovisual gaps.

The analytical release should not redistribute copyrighted source audiovisual files.

---

# 22. Governing principle

V2 should be neither transcript-reductionist nor ingestion-maximalist.

The correct standard is:

> **Review every audiovisual artifact that materially changes what we can know, and avoid uploading audiovisual material whose analytical contribution is already redundant.**

The purpose of audiovisual evidence is not completeness for its own sake.

It is to recover the dimensions of *IDOLY PRIDE* that only performance can reveal.
