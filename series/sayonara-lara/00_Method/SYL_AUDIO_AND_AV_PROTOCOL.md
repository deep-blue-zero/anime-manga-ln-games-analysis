---
title: "Sayonara Lara: Audio, Voice Performance, and AV Inspection Protocol"
artifact_id: "SYL_AUDIO_AND_AV_PROTOCOL"
artifact_type: audio_av_method
version: "1.1-adopted"
status: canonical
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
do_not_use_as_literary_evidence: true
prepared_on: "2026-09-20 America/New_York"
drafted_against_commit: "f9dda552a5735f454e3bb99b4af6c920235a618d"
source_boundary: "Governing audio and audiovisual protocol for Japanese-language TV anime Episodes 01-12"
canonical_home: "series/sayonara-lara/00_Method/SYL_AUDIO_AND_AV_PROTOCOL.md"
generation: V1_JP_AUDITED
adopted_on: "2026-09-20 America/New_York"
---

# Audio, performed voice, and audiovisual inspection

## 1. The failure this protocol prevents

An MP3 in the filesystem is not evidence that the analytical model heard it. Successful decoding, a waveform plot, an ASR transcript, and a generated description of delivery are four different events. Each supports different claims.

The earlier conversation described relative vocal registers and prosodic patterns as if they had been measured or directly inspected. This packet has not recovered the corresponding measurements, listening records, or model-input receipts. Preserve those descriptions as candidate interpretations, not verified findings. Their possible correctness does not repair missing provenance.

The right question is not whether an AI has human auditory consciousness. It is **what representation of the sound reached which inspecting process, and what that process can reliably establish**. An audio-capable model may analyze supplied audio; a text-only orchestrator may delegate to one. Neither capability follows from the name Codex, Work, ChatGPT, Pro, or a model's own assertion.

Repository capability policy [G07] already requires this distinction. This document operationalizes it for the series without claiming a new corpus-wide policy.

## 2. Separate capabilities, not one 'audio support' flag

| Capability | Practical proof | Supports | Does not establish |
|---|---|---|---|
| Transport | File retrieved; size/hash checked | Availability and identity | Decoding or inspection |
| Decode/extract | ffprobe plus successful decode | Format, track, duration, samples | Listening, words, delivery |
| ASR | Real inference on actual audio, output retained | Candidate speech content | Timbre, affection, irony, authoritative transcript |
| Forced alignment | Language-compatible aligner run on supplied text | Candidate placement of that text | That the supplied words were actually spoken |
| Signal analysis | Reproducible measurement and valid segment selection | Bounded acoustic descriptors | Emotional intention or personality |
| Direct model audio inspection | Actual audio payload accepted by an audio-input model; probe and output retained | Fallible auditory observations, including nonverbal sound within tested capability | Perfect hearing, human experience, guaranteed interpretation |
| Human listening | Identified reviewer, interval, notes, uncertainty | Human auditory observations | Automatic correctness or universal consensus |
| Continuous AV inspection | Verified route exposing synchronized moving image and sound | Motion/sound relationship within the inspected interval | Full-episode coverage from a few clips |

The capabilities are independent. ASR success does not promote signal analysis into direct hearing. Native audio capability does not certify speaker identity or Japanese transcription accuracy. Playing a file in a notebook or issuing `ffplay` lets a human listen; it does not by itself feed sound into the model.

Use `VERIFIED`, `UNVERIFIED`, `UNAVAILABLE`, and actual run references per capability. Tool presence is only a prerequisite. Test the route on a representative Japanese clip before assigning analytical work.

## 3. Recommended practical stack

These are sourced tool roles, not a claim that the packages are installed or that every current version interoperates. Verify documentation and pin the actual working environment at execution time. Do not make new purchases, disclose source audio to external services, accept gated-model conditions, or download large models without the applicable permission.

### Core local layer

**FFmpeg/ffprobe:** establish streams, make bounded derivatives, retain time mappings, and inspect signal-level properties [T01-T02]. Preserve the original mixed audio. Do not use a normalized or separated derivative as the only sound witness.

**Existing Japanese subtitle parser and crosswalk:** prefer the owner's established extraction pipeline. Preserve ASS formatting/speaker/style information and source cue identity. Do not rebuild an adequate pipeline merely because another library is fashionable.

**faster-whisper, multilingual checkpoint:** optional local ASR for missing/contested wording, subtitle mismatch, and navigation [T03]. A predownloaded multilingual `large-v3` is a reasonable candidate to test, not a mandatory quality guarantee. Use a CPU/int8 or compatible GPU configuration after a real probe. Do not use an English-only checkpoint for Japanese.

**WhisperX:** optional language-compatible forced alignment and candidate diarization, when finer timing is necessary [T04]. Verify the selected Japanese alignment model, dictionary coverage, and package compatibility. Upstream explicitly warns about overlapping speech and imperfect diarization. A confidence-like alignment output cannot certify linguistic correctness.

**Praat through Parselmouth:** optional pitch/intensity and other targeted acoustic inspection on suitable segments [T05]. Use only for a question the measurement can answer. Do not compute a character's whole-episode pitch median from the mixed soundtrack and call it her natural register.

### Conditional helpers

**pyannote speaker diarization:** helpful when speaker boundaries are unclear, but cluster labels are not character identities [T06]. Verify through dialogue context and audible/visual evidence. The documented community model has gated access conditions; do not accept terms or expose tokens silently. Avoid deploying it when existing speaker annotations already solve the task.

**Source separation:** last-resort listening aid for difficult mixtures, not a new clean ground truth. Retain the original mix; record model/version and artifacts; recheck claims against the original. Breath, sibilants, music, and quiet responses are particularly vulnerable to transformation artifacts.

### Actual auditory interpretation

**Preferred when available:** a verified native-audio inspection route, with short, source-linked scenes and a task-specific probe. Current OpenAI documentation gives `gpt-audio-1.5` through Chat Completions as an example audio-input route [T07]. This is a dated API option, not a promise about this Chat, Work, or Codex runtime. Verify the exact endpoint/model/schema and account access before execution.

**Fallback:** human listening notes from the owner or an authorized reviewer, with interval, speaker, observed feature, and uncertainty. The literary analyst must attribute those observations rather than claim personal listening.

**Not a fallback:** asking the text model to imagine the actor's delivery from subtitles, a cast biography, or an interview. That is interpretive invention, not missing-channel recovery.

OpenAI's dedicated transcription documentation describes a speech-to-text workflow separate from audio chat [T08]. Do not treat a transcription endpoint's output as if it were an auditory character-performance review. API usage and sending files off-device require their own authorization; a Chat subscription does not imply this permission.

## 4. A bounded capability probe

Before full work, select short contrasting Japanese intervals, including neutral dialogue, emotional speech, comic turn-taking, a nonverbal vocalization, and music/ambience with little or no speech. Include overlap if that is a planned task. Do not send the desired personality interpretation with the first probe.

Record:

- product surface, model/provider, endpoint or tool, tool-runtime location;
- file hash, selected track, source interval, derivative transformations;
- what bytes/representation reached the model;
- request configuration and actual response;
- whether words, speakers, nonverbal events, and delivery contrasts were recoverable;
- known failure modes, human spot-check, and approved analytical scope.

A transcript hidden inside a tool response is not native audio input. A probe that only asks for transcription cannot establish competence on laughter, sarcasm, breath, or rhythm. A useful diagnostic compares clips whose text alone cannot explain their delivery, plus a low-speech clip that tests hallucinated dialogue. One successful example is not a benchmark.

If the route is unverified or fails, mark direct audio inspection unavailable for that stage. Continue supported text/static work, and route material sound claims to a named later task. Do not report a new performance conclusion while that task is pending.

## 5. Three-pass workflow for each relevant scene

### Pass A: hear/observe before interpreting

Where possible, give the auditory reviewer a neutral scene identifier and source audio without the prior thesis. Ask for speech/nonverbal events, delivery changes, uncertainty, and mixed-sound limitations. Avoid prompts such as 'show how Mari hides her love' or 'confirm Lara's high-pitched innocence'.

### Pass B: align language and context

Compare the observation with the Japanese witness, scene participants, visual evidence, and relevant prior state. Resolve speaker attribution, exact words, omitted responses, and cue timing. Preserve disagreements. For disputed high-impact lines, use a second independently capable route or human verification.

### Pass C: interpret and challenge

Only now ask what the observed performance does: contrast characters, mask or expose care, make a threat habitual, change a joke, qualify an apparent confession, or complicate narration. Give at least one alternative explanation and the evidentiary limits.

This is a bias-reduction design, not a guarantee of independence. Model consensus does not count as multiple independent witnesses when both outputs derive from the same transcript or leading prompt.

## 6. Suggested extraction recipes

The following are **recipes, not commands already run on these episodes**. Use an isolated working directory outside the analytical repository. Set source, verified stream index, interval, and tool environment deliberately. Preserve logs privately.

```bash
# POSIX shell example. Supply a real source and an existing working directory.
SOURCE='/absolute/path/to/episode.mkv'
WORK='/absolute/path/to/private-working-directory'
AUDIO_STREAM_INDEX='1'  # Example only: replace after inspecting ffprobe output.

ffprobe -v error \
  -show_entries format=duration,start_time:stream=index,codec_type,codec_name,sample_rate,channels,channel_layout,start_time:stream_tags=language,title \
  -of json "$SOURCE" > "$WORK/probe.json"

# Preserve the selected encoded track without another lossy generation.
ffmpeg -n -i "$SOURCE" -map "0:${AUDIO_STREAM_INDEX}" -vn \
  -c:a copy "$WORK/selected-track.mka"

# Example interval values ONLY; they are not claimed Sayonara Lara scene times.
START='00:10:00.000'
DURATION='00:00:30.000'

# Audition derivative: retain source rate/channels; no normalization.
ffmpeg -n -i "$SOURCE" -ss "$START" -t "$DURATION" \
  -map "0:${AUDIO_STREAM_INDEX}" -vn -c:a pcm_f32le \
  "$WORK/clip-audition.wav"

# Separate convenience derivative for a pipeline expecting mono 16 kHz.
ffmpeg -n -i "$WORK/clip-audition.wav" -ac 1 -ar 16000 \
  -c:a pcm_s16le "$WORK/clip-asr.wav"
```

Record actual decoded duration and the source time mapping; container start times, seek semantics, and encode delay can affect offsets. Check an audible/visible anchor rather than assuming numerical timestamps are sample-accurate. Decoding MP3 to WAV does not restore lost fidelity. Inspect channel layout before downmixing; a mono ASR derivative is not appropriate evidence for spatial sound.

For ASR, an implementation may use the following documented interface pattern after a local environment probe [T03]. This example is intentionally local-model-only; it does not silently download weights.

```python
from pathlib import Path
from faster_whisper import WhisperModel

def transcribe_japanese(audio_path: Path, model_dir: Path) -> list[dict]:
    if not audio_path.is_file():
        raise FileNotFoundError(audio_path)
    if not model_dir.is_dir():
        raise FileNotFoundError('A verified local multilingual model directory is required')
    model = WhisperModel(str(model_dir), device='cpu', compute_type='int8')
    segments, info = model.transcribe(
        str(audio_path), language='ja', task='transcribe',
        beam_size=5, word_timestamps=True, vad_filter=True,
        condition_on_previous_text=False,
    )
    # The generator must be consumed for transcription to execute.
    rows = []
    for segment in segments:
        rows.append({
            'start': segment.start, 'end': segment.end, 'text': segment.text,
            'words': [
                {'start': w.start, 'end': w.end, 'text': w.word,
                 'model_probability': w.probability}
                for w in (segment.words or [])
            ],
        })
    return rows
```

Record package/model revision, actual options, failures, and output hash. These candidate probabilities are not calibrated evidence confidence. Compare VAD-on and unfiltered context where quiet speech, breath, crying, or timing matters. An ASR language hint does not guarantee correct names or wording. If Japanese captions already provide reliable language, do not transcribe the entire season simply to generate redundant text.

## 7. What acoustic measurements can and cannot do

For a clean, speaker-verified utterance, useful descriptors may include voiced F0 median and range, within-utterance contour, reliable voiced fraction, amplitude envelope, approximate response latency, overlap, and duration. Report algorithm, pitch bounds, sample rate, interval, exclusions, and uncertainty. Use a few defensible descriptors, not an unexplained dashboard.

Key safeguards:

- Estimate voice pitch only where the signal and speaker attribution support it; music can dominate the pitch tracker.
- Check octave errors and unvoiced regions. High or low tracker values can be estimation failures.
- Compare like conditions and within-speaker states before broad cross-character claims. Running, crying, shouting, whispering, and neutral conversation are different tasks.
- Do not conflate F0 with timbre, perceived maturity, gender identity, personality, affection, or narrative power.
- Mixed-track RMS is not actor loudness; soundtrack level is not vocal effort. Compression, distance, and mixing matter.
- Subtitle cue gaps are display gaps, not measured silence. Distinguish no dialogue, no voice, ambience-only, and near-zero signal.
- Word/character counts per cue are not Japanese articulation rate. Mora-based estimates require reviewed linguistic segmentation and audible timing.
- ASR word timestamps and forced alignment are estimates; millisecond precision in a file is not millisecond accuracy.
- Do not infer emotion from jitter, shimmer, or similar measures on a compressed mixed anime soundtrack. Such measurements may be unsuitable even before interpretation.

Measurements can challenge an impression. They cannot independently establish that a line is affectionate, sarcastic, coercive, or romantically charged. Those are contextual performance interpretations requiring more than a number.

## 8. Performance sampling that can support characterization

Build **state-conditioned cohorts**, not a universal voice ranking. For Lara and Mari, seek ordinary conversation, comedy, stress, refusal, practical care, vulnerable disclosure, and an episode-specific change. For Grace, compare authority, comedy, and any verified change in control. For other speakers, use a scoped sample proportionate to their role.

Document selection and omissions. Several clips from one noisy boxing scene do not establish a season-long baseline. A full-series voice claim needs coverage across relevant temporal phases and interlocutors, including contrary examples. There is no prescribed minimum number that magically certifies the model.

Potential questions, not findings:

- Does Lara's variation reflect emotional openness, theatrical fantasy-world diction, situational alarm, or a combination?
- Is Mari actually monotone, or does contrast come mainly from short turns, pragmatic understatement, dialect, and timing?
- When does Mari become expansive outside boxing, and does Lara ever underplay?
- Does Grace's authority persist acoustically across bodily/comic changes, or is it mainly in wording and others' reactions?
- How do the two leads' turn-taking and mutual familiarity change over time?

## 9. Record format

Use the language/performance ledger as the interpretive home. Keep large raw outputs in the evidence plane.

```yaml
performance_id: SYL-P0001
status: pending
source_id: null
source_sha256: null
episode: null
source_interval: null
speaker_identity: unverified
inspection_route: unverified
run_or_reviewer_record: null
observed_auditory_feature: null
measurement_reference: null
linguistic_context: null
visual_context: null
interpretation: null
alternative_explanation: null
limitations: null
affected_claims: []
```

An actual record must name a real interval and route. Illustrative nulls must never be promoted into performed observations. Distinguish `DELEGATED_AUDIO_OBSERVATION`, `HUMAN_LISTENING_OBSERVATION`, `ACOUSTIC_MEASUREMENT`, and `TEXT_BASED_SPEECH_ANALYSIS` in the record.

Acceptable wording: 'In the inspected exchange, the auditory reviewer reports a shorter, clipped response; in context this may help produce the deadpan contrast.' Unacceptable: 'Mari has the lowest pitch and therefore conceals romantic attraction', without valid measurement or adequate contextual evidence.

## 10. Audio-review prompt

> Inspect the attached source-linked audio, not an imagined delivery from its transcript. First identify which intervals you actually received and whether your route supports audio-content inspection. Describe audible events, speaker uncertainty, delivery contrasts, pauses, overlap, and nonverbal vocalization. Separate observation from inferred attitude. Do not infer a personality trait or relationship category from pitch alone. Use turn-relative references when exact timestamps are not available; do not invent precision. Mark music/overlap/codec limitations. After the neutral observation pass, compare the Japanese transcript and scene context. Give the strongest alternative interpretation of any emotionally consequential delivery. Return observations with source IDs, actual route, uncertainty, and claims needing human or continuous-AV verification.

## 11. Continuous-video escalation

Use the repository's existing `VIDEO_NOT_REQUIRED`, `VIDEO_TARGETED_ESCALATION`, and `VIDEO_FULL_EPISODE_ESCALATION` states [G06]. These describe need, not successful inspection.

For this series, likely candidates include comic response timing, the boxing interruption, changes of expression during relationship acknowledgment, and the final departure. The earlier chat's clip intervals are **locator leads**, not verified cut boundaries. Re-locate them from the actual bundle and include enough setup and aftermath to prevent a decontextualized reading.

Audio alone can answer some vocal questions. Video is needed when gaze changes, gesture, editing, motion, or synchronization materially affect the conclusion. Extracting more frames may narrow uncertainty but remains sampled reconstruction, not native continuous viewing.

Respect actual delivery limits and source fidelity; do not hard-code the repository's dated transport numbers as permanent product guarantees. Failure to transport a diagnostic clip leaves a debt. It does not make the claim unimportant or convert the clip into optional evidence.

## 12. Completion rule

A final performance study must disclose its sampling and actual routes. No unqualified 'full audio analyzed' label is allowed for selected scenes. Each sound-dependent conclusion must be traceable to an auditory observation or valid measurement, with interpretation identified separately.

If native audio is unavailable, the correct output is a strong text/visual analysis plus scoped, attributable human/delegated audio work where available and explicit remaining debts. Fluent descriptions of unheard voices are not an acceptable substitute.

## Source key

Governance [Gxx], tooling [Txx], and creator-context [Pxx] identifiers resolve in the [method sources and design notes](SYL_METHOD_SOURCES_AND_DESIGN_NOTES.md).
