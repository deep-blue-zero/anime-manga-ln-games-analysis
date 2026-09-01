---
series: AZUR_LANE
scope_character: BREMERTON_10324
generation: V1
semantic_authority: CN
performed_locale: JP
artifact_type: specialist_synthesis
scope: BREMERTON_10324_JP_VOICE_PERFORMANCE
status: active_provisional
source_boundary: 101 mapped JP spoken utterances in the canonical WAV manifest/index; 100 published Drive PCM WAV derivatives directly retrieved, SHA-256 verified, and acoustically measured; BREMERTON_103245_LOGIN_LOGIN_S042_cc507128.wav remains listed in the canonical manifest/index but is not retrievable from the current Drive publication surface; ear-dependent timbre remains OPEN
supersedes:
- series/azur-lane/03 Character Reconstruction/BREMERTON_10324/AZUR_LANE_BREMERTON_JP_AUDIO_PUBLICATION_GAP_AUDIT.md
superseded_by: []
do_not_use_as_current_authority: false
governing_method: AZUR_LANE_CHARACTER_RECONSTRUCTION_ANALYTICAL_METHOD.md
measurement_method_family: Takao/Baltimore frozen JP performed-acoustic method
measurement_completion: 100/101
ear_dependent_timbre_status: OPEN
---

# Azur Lane — Bremerton JP Voice Performance Profile

## 0. Verdict and authority boundary

The JP performed-voice layer is now **substantially reconstructed but not promotion-complete**.

The current Drive publication makes 100 of Bremerton's 101 mapped spoken utterances directly retrievable as lossless PCM WAV derivatives. All 100 retrieved files:

- match the WAV-manifest SHA-256 exactly;
- decode as 44.1 kHz mono PCM;
- match manifest duration to numerical tolerance;
- were measured once with the same frozen quantitative method family used for the mature Azur Lane voice passes.

One mapped record remains outside direct acoustic measurement:

`103245:login:0` — `BREMERTON_103245_LOGIN_LOGIN_S042_cc507128.wav`

The canonical WAV index and manifest list it, but the current Drive publication/search surface does not expose a retrievable file object for it. Accordingly, this document does **not** claim a 101/101 exhaustive acoustic pass and does **not** authorize Bremerton's frozen V1 promotion by itself.

The missing record is one body-care-skin login line. Its absence is too small to erase the broad performed-state model below, but the pre-existing promotion gate explicitly required all 101 measurements, so that gate remains open by one waveform.

Ear-dependent descriptors such as breathiness, grain, warmth, nasality, or perceived smile are also left **OPEN**. They are not inferred from F0/RMS proxies.

## 1. Frozen measurement method

For each directly retrieved WAV:

- Praat-style autocorrelation F0, 10 ms step, 75–700 Hz search range;
- median F0 plus p10–p90 span in semitones;
- 25 ms RMS activity windows with 10 ms hop;
- adaptive activity threshold `min(p20 + 0.30*(p90-p20), p90-12 dB)`;
- inactive gaps up to 80 ms bridged;
- active duration, lead/trail silence, internal inactivity, pause ratio, and pauses >=250 ms;
- active-speech RMS dBFS;
- Japanese content-character / active-speech-second rate proxy.

Interpretation order remains:

`semantic state -> situation / relationship -> JP text -> acoustics -> bounded inference`

Acoustics refine state realization; they do not override CN semantic authority or invent psychology.

## 2. Corpus-level acoustic shape

Across the 100 measured utterances, the median utterance has approximately:

| Measure | Median |
|---|---:|
| median F0 | **319.94 Hz** |
| p10–p90 F0 span | **15.06 st** |
| active RMS | **-18.36 dBFS** |
| JP content-character rate | **5.35 chars/s active speech** |
| pause ratio | **0.202** |
| active speech duration | **7.01 s** |
| substantial pauses | **2** |

The important result is not one global number. Bremerton's delivery has a **wide, context-sensitive state space**. The performance does not collapse her into one flirtatious, high-energy vocal mode.

## 3. Major state contrast: combat vs affinity

Family medians provide the cleanest broad contrast:

| Family | F0 median | F0 span | Active RMS | Char rate | Pause ratio | Active duration |
|---|---:|---:|---:|---:|---:|---:|
| combat | **377.43 Hz** | 12.19 st | **-17.86 dBFS** | 5.70 | **0.127** | **2.33 s** |
| everyday | 324.19 Hz | 15.06 st | -18.26 dBFS | 5.48 | 0.202 | 7.77 s |
| touch | 314.82 Hz | 15.42 st | -18.67 dBFS | 4.86 | 0.179 | 4.64 s |
| affinity/oath | **288.08 Hz** | 15.27 st | **-19.66 dBFS** | 5.21 | **0.240** | **12.51 s** |

This supports two strong performed-state rules.

### 3.1 Immediate danger compresses and activates

Combat is shorter, higher in F0, somewhat louder, and less pause-rich. Baseline examples include:

- battle: ~402 Hz median F0;
- skill: ~426 Hz and among the loudest measured lines;
- MVP: ~377 Hz.

This **STRENGTHENS** the textual rule that Bremerton compresses discourse under danger rather than carrying her consultation/social elaboration into combat.

The positive-energy surface therefore does not imply operational unseriousness. Her performance can become fast, brief, and activated when the task requires it.

### 3.2 Affinity creates temporal room rather than social collapse

Affinity/oath material is much longer and more pause-rich, with a lower family median F0 and quieter active level. This is compatible with greater interpersonal exposure and response-monitoring rather than withdrawal.

Crucially, speaking-rate proxy remains near the everyday range. She does not simply become globally slow or inert. The larger change is **more temporal space inside sustained interaction**.

## 4. Affinity ladder: no monotonic pitch law

The baseline affinity sequence prevents an overly neat reading:

| Slot | F0 median | Active RMS | Pause ratio | Active duration |
|---|---:|---:|---:|---:|
| feeling1 | 263.59 Hz | -18.86 | 0.239 | 7.10 s |
| feeling2 | 314.41 Hz | -19.82 | 0.269 | 12.31 s |
| feeling3 | 292.50 Hz | -20.57 | 0.188 | 16.18 s |
| feeling4 | 274.84 Hz | -19.50 | 0.150 | 11.17 s |
| feeling5 | 275.72 Hz | -20.91 | 0.276 | 15.95 s |
| propose | 282.83 Hz | -20.49 | 0.308 | 12.70 s |

The later baseline intimacy states are often lower and quieter than high-activation everyday/combat states, but **affection does not produce a monotonic F0 descent**. Feeling2 rises relative to feeling1, and alternate/skin feeling5 lines range broadly from about 284 to 366 Hz.

Therefore:

> **REJECT: “the more intimate Bremerton becomes, the lower her pitch.”**

A better model is:

> **STRENGTHEN: intimacy permits longer, quieter, more pause-rich response space, while local excitement, teasing, embarrassment, or role-play can still raise activation.**

## 5. Vulnerability is audible as regulation change, not loss of fluency

The strongest baseline vulnerability anchor is `feeling5`:

- ~275.7 Hz median F0;
- ~-20.9 dBFS active RMS;
- 0.276 pause ratio;
- 10 substantial pauses;
- nearly 16 seconds of active speech.

Its text contains explicit uncertainty about how the Commander will answer her DM. The performance is consistent with **visible interpersonal anticipation plus continued engagement**: she does not stop communicating; the line becomes more segmented and lower-energy.

The proposal line is similarly pause-rich (0.308, seven substantial pauses) while remaining directive and playful in content.

This **STRENGTHENS** the monograph's emotional-regulation rule:

`feel state visibly + keep talking/acting + redirect toward available next step`

It also argues against reconstructing her social ease as a facade hiding global interpersonal incompetence.

## 6. Role-play and self-authored performance

The action/performance skin `103242` is acoustically diagnostic. Its `main` median is roughly **401 Hz**, with relatively high active level (~-16.5 dBFS), and several theatrical/heroic lines sit among the most activated utterances in the corpus.

This supports the multilingual profile's distinction between:

- ordinary Bremerton conversational register; and
- deliberately performed “hero” language.

The performance is not evidence that her whole personality becomes theatrical. It is evidence that she can **intentionally widen/raise activation when inhabiting a self-conscious performance frame**, then return to ordinary commentary about fatigue, posing, or coordination.

## 7. Touch and boundary states are heterogeneous

Touch material does not support a generic “physical intimacy = softer voice” rule.

Examples vary sharply:

- baseline ordinary touch is highly activated (~423 Hz) while asking for a massage;
- baseline special touch is much lower (~265 Hz);
- consultation-room special touch is ~355 Hz despite a clear contextual boundary;
- body-care ordinary touch is one of the quietest measured lines (~-21.0 dBFS) without requiring a low F0.

This is analytically useful because Bremerton's physical-affection model is **contextual**, not a single seduction register. The meaning of contact depends on fatigue, role, teasing, care, and explicit situational boundaries.

## 8. Body-care `103245`: activation can coexist with apology/care

The body-care skin is not uniformly hushed. Its measured `feeling5` reaches ~340 Hz while the text includes an explicit apology for having pushed into the Commander's time too forcefully and an explanation of access anxiety.

That combination supports the existing scarcity/FOMO correction:

> Bremerton can become more activated and pushier when valued access feels scarce, while retaining the capacity to recognize and repair the overstep.

This is stronger than reading the scene either as proof of possessive jealousy or as proof that jealousy/competition is absent.

The one unmeasured mapped utterance belongs to this skin (`103245:login:0`), so fine-grained claims about the skin's complete acoustic distribution remain provisional.

## 9. Bridal `103248`: not a globally calmer endpoint

The bridal skin's overall measured median F0 is relatively high (~348 Hz), and its everyday lines remain lively. Its `feeling5` is lower (~327 Hz) and quiet (~-20.3 dBFS), but the skin as a whole does **not** acoustically collapse into a serene or subdued marriage register.

Therefore:

> **REJECT: “oath/bridal Bremerton becomes globally calmer, quieter, or less socially energetic.”**

The stronger reading remains textual + acoustic:

> established intimacy changes **priority and privacy**, not her fundamental social vitality.

## 10. Performance implications for reconstruction

### High-confidence performed rules

1. **Danger compression:** immediate combat favors short, activated, less pause-rich delivery.
2. **Relational expansion:** sustained affinity permits longer and more internally segmented delivery.
3. **Vulnerability without shutdown:** uncertainty can lower level/increase pauses while speech remains action- and response-oriented.
4. **Role-play amplification:** self-conscious theatrical frames can raise activation substantially without becoming baseline personality.
5. **No single flirt register:** physical/romantic lines occupy multiple acoustic states determined by local function.

### Bounded / do not overgeneralize

- Do not impose a monotonic intimacy-pitch slope.
- Do not equate higher F0 with happiness, jealousy, or embarrassment without textual state evidence.
- Do not equate lower RMS with “softness” or “warmth”; those are partly perceptual/timbral judgments.
- Do not treat skin medians as stable personality traits independent of scene function.
- Do not infer breathiness, smile, nasality, vocal fry, or resonance from these metrics alone.

## 11. Monograph impact ledger

| Existing claim | Transition | Performed-voice impact |
|---|---|---|
| positive affect does not make her operationally unserious | **STRENGTHEN** | combat materially compresses and activates delivery |
| emotional expression is permeable but action continues | **STRENGTHEN** | affinity/vulnerability changes timing and level without speech shutdown |
| social confidence is not epistemic certainty | **PRESERVE / STRENGTHEN** | thinking/response-monitoring states show segmentation rather than confident flattening |
| intimacy creates bounded priority rather than social contraction | **STRENGTHEN** | bridal register remains lively overall; intimacy does not globally suppress activation |
| scarcity/FOMO can increase pushiness | **STRENGTHEN, BOUND** | `103245 feeling5` combines activated delivery with explicit apology/access anxiety |
| theatrical hero language is a role layer, not baseline identity | **STRENGTHEN** | `103242` performance frame is acoustically amplified relative to ordinary speech |
| physical intimacy is one generic seductive register | **REJECT** | touch/touch2 states are acoustically heterogeneous and context-dependent |
| increasing affection monotonically lowers pitch | **REJECT** | affinity sequence and skin variants are non-monotonic |
| bridal/oath state is globally calmer | **REJECT** | `103248` remains comparatively activated outside specific quieter lines |
| ear-dependent timbre is now known | **OPEN** | quantitative waveform pass does not authorize timbral/aesthetic descriptors |

No core cognitive/behavioral claim requires rejection. The performed layer mostly **strengthens and bounds** the existing model rather than rewriting it.

## 12. Remaining exact gate

The acoustic reconstruction can be called **substantively complete for model-building**, but not **administratively exhaustive** under Bremerton's frozen promotion protocol.

Remaining requirement:

1. make `BREMERTON_103245_LOGIN_LOGIN_S042_cc507128.wav` directly retrievable from Drive (or expose its exact source stream through the reproducible decoder surface);
2. verify its SHA-256 against the canonical manifest;
3. run the frozen measurement once;
4. append its row to `AZUR_LANE_BREMERTON_JP_VOICE_ACOUSTIC_METRICS.csv`;
5. rerun the promotion decision only.

No R0–R8 reread is required.
